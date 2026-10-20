"""Scoped, passage-level local retrieval, with machine-readable citations."""
from __future__ import annotations

import hashlib
import json
import re
import sqlite3
import sys
from collections import Counter
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import unquote

import click

from .llm import get_config
from .raw_metadata import infer_raw_metadata
from .retrieval import CHIP_RE, clean_text, frontmatter, list_values, passages, query_plan, terms

SCHEMA_VERSION = "passages-1"


def _scopes(meta):
    chips = meta.get("chips") or list_values(meta.get("chip")) or [""]
    families = list_values(meta.get("sdk_family")) or [""]
    versions = list_values(meta.get("sdk_version")) or [""]
    sides = re.findall(r"\b(?:AP|CP|SMP)\b", str(meta.get("processor") or "")) or [""]
    return [{"chip": c.upper(), "family": f.lower(), "version": v.lower(), "processor": s.upper()}
            for c in chips for f in families for v in versions for s in sides]


class SearchEngine:
    def __init__(self, db_path: Path):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.workspace_dir = Path(get_config()["paths"]["wiki_dir"]).resolve().parent
        self._init_db()

    @contextmanager
    def connection(self):
        con = sqlite3.connect(self.db_path)
        try:
            with con:
                yield con
        finally:
            con.close()

    def _init_db(self):
        with self.connection() as con:
            con.executescript("""
                CREATE TABLE IF NOT EXISTS kb_settings (key TEXT PRIMARY KEY, value TEXT);
                CREATE TABLE IF NOT EXISTS kb_docs (
                    id INTEGER PRIMARY KEY, scope TEXT NOT NULL, path TEXT NOT NULL,
                    title TEXT NOT NULL, kind TEXT NOT NULL, status TEXT NOT NULL,
                    meta TEXT NOT NULL, absolute_path TEXT NOT NULL, source_url TEXT NOT NULL,
                    UNIQUE(scope,path)
                );
                CREATE TABLE IF NOT EXISTS kb_scopes (
                    doc_id INTEGER NOT NULL, chip TEXT, family TEXT, version TEXT, processor TEXT
                );
                CREATE INDEX IF NOT EXISTS kb_scopes_filter ON kb_scopes(chip,family,version,processor,doc_id);
                CREATE VIRTUAL TABLE IF NOT EXISTS kb_passages USING fts5(
                    doc_id UNINDEXED, start_line UNINDEXED, end_line UNINDEXED,
                    anchor UNINDEXED, title, heading, keywords, content,
                    tokenize='porter unicode61'
                );
            """)

    @property
    def document_count(self):
        with self.connection() as con:
            ready = con.execute("SELECT value FROM kb_settings WHERE key='schema'").fetchone()
            return con.execute("SELECT count(*) FROM kb_docs").fetchone()[0] if ready and ready[0] == SCHEMA_VERSION else 0

    def index(self, wiki_dir, raw_dir=None):
        wiki_dir = Path(wiki_dir).resolve()
        self.workspace_dir = wiki_dir.parent
        raw_dir = Path(raw_dir).resolve() if raw_dir else None
        raw_scopes = {}
        counts = Counter()
        with self.connection() as con:
            con.execute("DELETE FROM kb_passages")
            con.execute("DELETE FROM kb_scopes")
            con.execute("DELETE FROM kb_docs")
            for scope, root in [("raw", raw_dir), ("wiki", wiki_dir)]:
                if root is None or not root.exists():
                    continue
                for file in sorted(root.rglob("*.md")):
                    rel = file.relative_to(root).as_posix()
                    if scope == "wiki" and (file.name in {"index.md", "WIKI.md", "AI-SEARCH.md"} or rel.startswith("categories/")):
                        continue
                    try:
                        text = file.read_text(encoding="utf-8-sig")
                    except (OSError, UnicodeError) as exc:
                        raise RuntimeError(f"Cannot index {file}: {exc}") from exc
                    fm, _ = frontmatter(text)
                    if scope == "raw":
                        meta = infer_raw_metadata(root, file)
                        scopes = _scopes(meta)
                        raw_scopes[file.resolve()] = scopes
                        kind = meta["doc_type"]
                        if "examples" in file.parts or "projects" in file.parts:
                            kind = "example"
                    else:
                        meta = dict(fm)
                        kind = {"summaries": "summary", "concepts": "concept", "outputs": "output"}.get(rel.split("/", 1)[0], "guide")
                        if kind not in {"summary", "concept", "output"}:
                            kind = "guide"
                        scopes = []
                        source = re.search(r"^> \*\*Source:\*\*(.*)$", text, re.M)
                        if source:
                            for target in re.findall(r'\]\(([^\s)]+)', source.group(1)):
                                target_path = (file.parent / unquote(target.split("#")[0])).resolve()
                                scopes.extend(raw_scopes.get(target_path, []))
                        if not scopes:
                            scopes = _scopes(meta)
                    heading = re.search(r"^# (.+)$", text, re.M)
                    title = clean_text(heading.group(1)) if heading else meta.get("title", file.stem)
                    meta.update(kind=kind, title=title)
                    status = str(meta.get("mirror_status") or "current")
                    source_url = str(meta.get("source_url") or "")
                    doc_id = con.execute("INSERT INTO kb_docs(scope,path,title,kind,status,meta,absolute_path,source_url) VALUES(?,?,?,?,?,?,?,?)",
                                         (scope, rel, title, kind, status, json.dumps(meta, ensure_ascii=False, default=str), str(file), source_url)).lastrowid
                    unique_scopes = {tuple(s.get(k, "") for k in ("chip", "family", "version", "processor")) for s in scopes}
                    con.executemany("INSERT INTO kb_scopes VALUES(?,?,?,?,?)", [(doc_id, *s) for s in unique_scopes])
                    aliases = meta.get("aliases") or []
                    aliases = aliases if isinstance(aliases, list) else [str(aliases)]
                    keywords = " ".join(terms(" ".join([title, file.stem, *aliases])))
                    for chunk in passages(text):
                        # CJK bigrams live in the searchable content, while results
                        # are read from the original file using these line bounds.
                        normalized = " ".join(sorted(terms(chunk["content"])))
                        con.execute("INSERT INTO kb_passages VALUES(?,?,?,?,?,?,?,?)",
                                    (doc_id, chunk["start_line"], chunk["end_line"], chunk["anchor"], " ".join(terms(title)), chunk["heading"] + "\n" + " ".join(terms(chunk["heading"])), keywords, normalized))
                        counts["passages"] += 1
                    counts[scope] += 1
            con.execute("INSERT OR REPLACE INTO kb_settings VALUES('schema',?)", (SCHEMA_VERSION,))
            con.execute("INSERT OR REPLACE INTO kb_settings VALUES('workspace',?)", (str(self.workspace_dir),))
            con.execute("INSERT OR REPLACE INTO kb_settings VALUES('indexed_at',?)", (datetime.now(timezone.utc).isoformat(),))
        return dict(counts)

    def _where(self, plan, *, version=None, kind=None, scope=None, include_historical=False):
        clauses, params = [], []
        if not include_historical:
            clauses.append("d.status != 'historical-unverified'")
        if kind:
            clauses.append("d.kind=?")
            params.append(kind)
        else:
            clauses.append("d.kind != 'output'")
        if scope:
            clauses.append("d.scope=?")
            params.append(scope)
        restrictions, scope_params = [], []
        if plan["chips"]:
            restrictions.append("s.chip IN (" + ",".join("?" for _ in plan["chips"]) + ")")
            scope_params.extend(plan["chips"])
        for key, value in [("family", plan["family"]), ("version", version.lower() if version else None), ("processor", plan["processor"])]:
            if value:
                restrictions.append(f"s.{key}=?")
                scope_params.append(value)
        if restrictions:
            clauses.append("EXISTS (SELECT 1 FROM kb_scopes s WHERE s.doc_id=d.id AND " + " AND ".join(restrictions) + ")")
            params.extend(scope_params)
        return " AND ".join(clauses) or "1=1", params

    def search(self, query, limit=20, *, chip=None, family=None, version=None, processor=None, kind=None, scope=None, include_historical=False, per_document=1):
        if not query.strip() or limit < 1:
            return []
        if not self.document_count:
            raise RuntimeError("Search index needs rebuilding. Run kb index.")
        plan = query_plan(query, chip=chip, family=family, processor=processor)
        where, params = self._where(plan, version=version, kind=kind, scope=scope, include_historical=include_historical)
        tokens = sorted(set(plan["expanded"]))[:70]
        match = " OR ".join('"' + t.replace('"', '""') + '"' for t in tokens)
        if not match and not (plan["chips"] or plan["family"] or version or plan["processor"]):
            return []
        with self.connection() as con:
            con.row_factory = sqlite3.Row
            rows = con.execute(f"""
                SELECT p.rowid, p.doc_id, p.start_line, p.end_line, p.anchor,
                       p.heading, p.content, d.*,
                       bm25(kb_passages,0,0,0,0,8,6,2,1) AS rank
                FROM kb_passages p JOIN kb_docs d ON d.id=p.doc_id
                WHERE {('kb_passages MATCH ? AND ') if match else ''}{where}
                ORDER BY {"rank" if match else "CASE d.kind WHEN 'summary' THEN 0 WHEN 'guide' THEN 1 ELSE 2 END"} LIMIT 350
            """, ([match] if match else []) + params).fetchall()
            candidates = []
            file_lines = {}
            for row in rows:
                meta = json.loads(row["meta"])
                path = Path(row["absolute_path"])
                if not path.exists():
                    continue
                if path not in file_lines:
                    file_lines[path] = path.read_text(encoding="utf-8").splitlines()
                lines = file_lines[path]
                content = "\n".join(lines[row["start_line"] - 1:row["end_line"]])
                normalized = clean_text(content).lower()
                title = row["title"].lower()
                heading = clean_text(row["heading"]).lower()
                # BM25 is useful within a topic but rare action words must not
                # outrank a document whose title matches the requested module.
                score = min(15.0, -float(row["rank"]))
                title_terms, heading_terms, content_terms = terms(title), terms(heading), terms(normalized)
                for token in plan["primary"]:
                    if (token in title_terms if token.isascii() else token in title):
                        score += 8 if token.isascii() else 3
                    elif (token in heading_terms if token.isascii() else token in heading):
                        score += 5 if token.isascii() else 1.5
                    elif token.isascii() and token in content_terms:
                        score += 3
                    elif token.isascii():
                        score -= 15
                for group in plan["groups"]:
                    if any(t in title for t in group):
                        score += 18
                    elif any(t in heading for t in group):
                        score += 7
                    elif any(t in normalized for t in group):
                        score += 2
                if plan["symbols"]:
                    score += 30 * sum(bool(re.search(r"(?<!\w)" + re.escape(s) + r"(?!\w)", normalized)) for s in plan["symbols"])
                    score += 20 * sum(s in row["anchor"].lower() or s in heading for s in plan["symbols"])
                    score += 10 if row["kind"] == "api" else 0
                elif not plan["chips"] and row["kind"] in {"summary", "concept"}:
                    score += 2
                if row["kind"] == "hub":
                    score -= 4
                all_scopes = [dict(s) for s in con.execute("SELECT chip,family,version,processor FROM kb_scopes WHERE doc_id=?", (row["doc_id"],))]
                filtered = [s for s in all_scopes if (not plan["chips"] or s["chip"] in plan["chips"]) and (not plan["family"] or s["family"] == plan["family"]) and (not plan["processor"] or s["processor"] == plan["processor"]) and (not version or s["version"] == version.lower())]
                workspace_path = row["scope"] + "/" + row["path"]
                candidates.append({"source": row["scope"], "path": row["path"], "workspace_path": workspace_path,
                                   "absolute_path": str(path), "title": row["title"], "kind": row["kind"], "status": row["status"],
                                   "start_line": row["start_line"], "end_line": row["end_line"], "heading": row["heading"].split("\n", 1)[0], "anchor": row["anchor"],
                                   "source_url": row["source_url"] + (("#" + row["anchor"]) if row["source_url"] and row["anchor"] else ""),
                                   "matching_scopes": filtered, "snippet": clean_text(content), "score": round(score, 4),
                                   "citation": f"{workspace_path}:{row['start_line']}-{row['end_line']}"})
        candidates.sort(key=lambda x: (-x["score"], x["workspace_path"], x["start_line"]))
        results, used, content_seen = [], Counter(), set()
        for row in candidates:
            if used[row["workspace_path"]] >= per_document:
                continue
            fingerprint = hashlib.sha256((row["snippet"] + json.dumps(row["matching_scopes"], sort_keys=True)).encode()).hexdigest()
            if fingerprint in content_seen:
                continue
            content_seen.add(fingerprint)
            used[row["workspace_path"]] += 1
            results.append(row)
            if len(results) >= min(limit, 100):
                break
        return results

    def context(self, query, *, limit=6, max_chars=12000, **filters):
        results = self.search(query, limit=limit * 2, per_document=2, **filters)
        documents, used = [], 0
        for row in results:
            remaining = max_chars - used
            if remaining < 100:
                break
            item = dict(row)
            item["content"] = item.pop("snippet")[:remaining]
            item["truncated"] = len(row["snippet"]) > remaining
            used += len(item["content"])
            documents.append(item)
            if len(documents) >= limit:
                break
        plan = query_plan(query, chip=filters.get("chip"), family=filters.get("family"), processor=filters.get("processor"))
        applied = {k: plan[k] for k in ("chips", "family", "processor")}
        applied["version"] = filters.get("version")
        return {"query": query, "filters": filters, "applied_filters": applied, "characters": used, "max_chars": max_chars, "documents": documents,
                "guidance": "Use matching_scopes and citations; verify APIs with kb read. No matching evidence means unknown; do not switch chip or processor."}


def ensure_engine(reindex=False):
    cfg = get_config()
    engine = SearchEngine(Path(cfg["paths"]["search_db"]))
    if reindex or not engine.document_count:
        engine.index(Path(cfg["paths"]["wiki_dir"]), Path(cfg["paths"]["raw_dir"]))
    return engine


def filter_options(fn):
    for option in [click.option("--chip", multiple=True, help="Exact chip; repeat for comparisons"),
                   click.option("--family", help="SDK family, e.g. bk_avdk_smp"),
                   click.option("--version", help="Exact SDK version, e.g. v4.0.1"),
                   click.option("--processor", type=click.Choice(["AP", "CP", "SMP"], case_sensitive=False)),
                   click.option("--kind", type=click.Choice(["api", "guide", "example", "summary", "concept", "hub", "output", "doc"])),
                   click.option("--scope", type=click.Choice(["wiki", "raw"])),
                   click.option("--include-historical", is_flag=True)]:
        fn = option(fn)
    return fn


@click.command("search")
@click.argument("query")
@click.option("--limit", "-n", default=8, type=click.IntRange(1, 100))
@click.option("--json-output", is_flag=True)
@click.option("--reindex", is_flag=True)
@filter_options
def cmd_search(query, limit, json_output, reindex, **filters):
    """Find relevant passages with exact scope filters and source lines."""
    results = ensure_engine(reindex).search(query, limit=limit, **filters)
    if json_output:
        click.echo(json.dumps(results, ensure_ascii=False))
        return
    if not results:
        click.echo("No matching evidence in the requested scope.")
    for row in results:
        click.echo(f"{row['title']} | {row['citation']} | {row['kind']}")
        click.echo(row["snippet"][:700] + "\n")


@click.command("context")
@click.argument("query")
@click.option("--limit", default=6, type=click.IntRange(1, 30))
@click.option("--max-chars", default=12000, type=click.IntRange(100, 100000))
@click.option("--json-output", is_flag=True)
@filter_options
def cmd_context(query, limit, max_chars, json_output, **filters):
    """Return a bounded evidence pack for any AI, without an external API."""
    pack = ensure_engine().context(query, limit=limit, max_chars=max_chars, **filters)
    if json_output:
        click.echo(json.dumps(pack, ensure_ascii=False))
        return
    if not pack["documents"]:
        click.echo("No matching evidence in the requested scope.")
    for row in pack["documents"]:
        click.echo(f"\n<source path=\"{row['workspace_path']}\" lines=\"{row['start_line']}-{row['end_line']}\">\n{row['content']}\n</source>")


def read_document(path, start_line=1, end_line=None, max_chars=12000):
    cfg = get_config()
    roots = [Path(cfg["paths"][k]).resolve() for k in ("wiki_dir", "raw_dir")]
    workspace = roots[0].parent
    requested = Path(path)
    file = requested.resolve() if requested.is_absolute() else (workspace / requested).resolve()
    if file.suffix.lower() != ".md" or not any(file.is_relative_to(root) for root in roots):
        raise ValueError("Only Markdown under raw/ or wiki/ can be read.")
    lines = file.read_text(encoding="utf-8").splitlines()
    stop = min(end_line or len(lines), len(lines))
    if start_line < 1 or stop < start_line:
        raise ValueError("Invalid or empty line range.")
    selected, count, actual_end, clipped = [], 0, start_line - 1, False
    for number in range(start_line, stop + 1):
        line = lines[number - 1]
        if count + len(line) + 1 > max_chars:
            if not selected:
                selected.append(line[:max_chars])
                actual_end = number
                clipped = True
            break
        selected.append(line)
        count += len(line) + 1
        actual_end = number
    return {"path": str(file), "start_line": start_line, "end_line": actual_end, "total_lines": len(lines),
            "truncated": clipped or actual_end < stop, "content": "\n".join(selected)}


@click.command("read")
@click.argument("path")
@click.option("--start-line", default=1, type=click.IntRange(1))
@click.option("--end-line", type=click.IntRange(1))
@click.option("--max-chars", default=12000, type=click.IntRange(100, 100000))
@click.option("--json-output", is_flag=True)
def cmd_read(path, start_line, end_line, max_chars, json_output):
    """Read the exact original lines cited by search/context."""
    try:
        row = read_document(path, start_line, end_line, max_chars)
    except (OSError, ValueError) as exc:
        raise click.ClickException(str(exc)) from exc
    if json_output:
        click.echo(json.dumps(row, ensure_ascii=False))
    else:
        click.echo(f"{row['path']}:{row['start_line']}-{row['end_line']}\n{row['content']}")
