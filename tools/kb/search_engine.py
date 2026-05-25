"""SQLite FTS5 full-text search engine over the wiki and raw docs."""

import sqlite3
from pathlib import Path
import sys

import click

from .llm import get_config
from .raw_metadata import infer_raw_metadata


def _safe_console(text: str) -> str:
    """Make console output safe for legacy Windows encodings."""
    encoding = getattr(sys.stdout, "encoding", None) or "utf-8"
    try:
        return text.encode(encoding, errors="replace").decode(encoding, errors="replace")
    except Exception:
        return text.encode("utf-8", errors="replace").decode("utf-8", errors="replace")


class SearchEngine:
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(str(self.db_path)) as conn:
            existing = conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='documents'"
            ).fetchone()
            if existing:
                cols = [row[1] for row in conn.execute("PRAGMA table_info(documents)").fetchall()]
                if "scope" not in cols:
                    conn.execute("DROP TABLE IF EXISTS documents")
            conn.execute("""
                CREATE VIRTUAL TABLE IF NOT EXISTS documents
                USING fts5(scope, path, title, content, tokenize='porter unicode61')
            """)
            conn.commit()

    def _index_root(self, conn: sqlite3.Connection, root: Path, scope: str):
        """Index all markdown files under one root."""
        for md in sorted(root.rglob("*.md")):
            rel = str(md.relative_to(root)).replace("\\", "/")
            if scope == "wiki" and (md.name in {"index.md", "WIKI.md"} or rel.startswith("categories/")):
                continue
            try:
                text = md.read_text(encoding="utf-8")
                title = rel
                for line in text.splitlines():
                    line = line.strip()
                    if line.startswith("# ") and not line.startswith("## "):
                        title = line[2:].strip()
                        break
                if scope == "raw":
                    meta = infer_raw_metadata(root, md)
                    metadata_text = "\n".join([
                        f"chip: {meta.get('chip', '')}",
                        f"module: {meta.get('module', '')}",
                        f"doc_type: {meta.get('doc_type', '')}",
                        "aliases: " + ", ".join(meta.get("aliases", [])),
                        "keywords: " + ", ".join(meta.get("keywords", [])),
                    ])
                    text = metadata_text + "\n\n" + text
                    if meta.get("title") and title == rel:
                        title = meta["title"]

                conn.execute(
                    "INSERT INTO documents (scope, path, title, content) VALUES (?, ?, ?, ?)",
                    (scope, rel, title, text),
                )
            except Exception:
                pass

    def index(self, wiki_dir: Path, raw_dir: Path | None = None):
        """Index all markdown files in the wiki and optional raw sources."""
        with sqlite3.connect(str(self.db_path)) as conn:
            conn.execute("DELETE FROM documents")
            if wiki_dir.exists():
                self._index_root(conn, wiki_dir, "wiki")
            if raw_dir and raw_dir.exists():
                self._index_root(conn, raw_dir, "raw")
            conn.commit()

    def search(self, query: str, limit: int = 20) -> list[dict]:
        """Search the index and return ranked results."""
        with sqlite3.connect(str(self.db_path)) as conn:
            try:
                rows = conn.execute(
                    """SELECT scope, path, title, snippet(documents, 3, '<b>', '</b>', '...', 40),
                              bm25(documents, 0.2, 2.0, 8.0, 1.0) AS score
                       FROM documents WHERE documents MATCH ?
                       ORDER BY score LIMIT ?""",
                    (query, limit),
                ).fetchall()
            except sqlite3.OperationalError:
                # Fallback for invalid FTS queries (special chars)
                rows = conn.execute(
                    """SELECT scope, path, title, substr(content, 1, 200)
                       FROM documents WHERE content LIKE ?
                       LIMIT ?""",
                    (f"%{query}%", limit),
                ).fetchall()

            return [
                {
                    "source": r[0],
                    "path": r[1],
                    "workspace_path": f"{r[0]}/{r[1]}",
                    "title": r[2],
                    "snippet": r[3],
                }
                for r in rows
            ]

    @property
    def document_count(self) -> int:
        with sqlite3.connect(str(self.db_path)) as conn:
            row = conn.execute("SELECT COUNT(*) FROM documents").fetchone()
            return row[0] if row else 0


@click.command("search")
@click.argument("query")
@click.option("--limit", "-n", default=20, help="Max results")
@click.option("--json-output", is_flag=True, help="Output as JSON")
@click.option("--reindex", is_flag=True, help="Rebuild index before searching")
def cmd_search(query, limit, json_output, reindex):
    """Full-text search over the wiki and raw docs."""
    cfg = get_config()
    wiki_dir = Path(cfg["paths"]["wiki_dir"])
    raw_dir = Path(cfg["paths"]["raw_dir"])
    db_path = Path(cfg["paths"]["search_db"])

    engine = SearchEngine(db_path)

    if reindex or engine.document_count == 0:
        if wiki_dir.exists() or raw_dir.exists():
            click.echo("Indexing wiki and raw docs...")
            engine.index(wiki_dir, raw_dir)
        else:
            click.echo("Knowledge base not found. Run 'kb ingest' and 'kb index' first.")
            return

    results = engine.search(query, limit=limit)

    if json_output:
        import json
        click.echo(json.dumps(results, indent=2))
        return

    if not results:
        click.echo(f"No results for: {query}")
        return

    click.echo(f"\n{len(results)} result(s) for: {query}\n")
    for r in results:
        title = _safe_console(f"[{r['title']}]({r.get('workspace_path', r['path'])})")
        click.echo(f"  {title}")
        snippet = _safe_console(r["snippet"].replace("\n", " ")[:150])
        click.echo(f"  {snippet}\n")
