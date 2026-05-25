"""Health checks for the Obsidian wiki graph and raw manifest."""

from __future__ import annotations

from collections import Counter
import hashlib
import json
import posixpath
import re
from pathlib import Path

import click

from .llm import get_config

WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
GENERATED_WIKI_FILES = {"index.md", "WIKI.md"}


def _file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _load_manifest(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except json.JSONDecodeError:
        return {}


def _wiki_rel(path: Path, wiki_dir: Path) -> str:
    return str(path.relative_to(wiki_dir)).replace("\\", "/")


def _is_generated(rel: str) -> bool:
    return rel in GENERATED_WIKI_FILES or rel.startswith("categories/")


def _target_keys(path: Path, wiki_dir: Path) -> set[str]:
    rel = _wiki_rel(path, wiki_dir)
    no_ext = rel[:-3] if rel.endswith(".md") else rel
    keys = {
        path.stem,
        no_ext,
        rel,
    }
    return {key.lower() for key in keys if key}


def _resolve_target(target: str, source: Path, wiki_dir: Path, targets: dict[str, Path]) -> Path | None:
    cleaned = target.split("|", 1)[0].split("#", 1)[0].strip().replace("\\", "/")
    if not cleaned:
        return None

    if cleaned.endswith(".md"):
        cleaned = cleaned[:-3]

    candidates = [cleaned]
    if cleaned.startswith("."):
        source_dir = posixpath.dirname(_wiki_rel(source, wiki_dir))
        candidates.append(posixpath.normpath(posixpath.join(source_dir, cleaned)))
    if "/" in cleaned:
        candidates.append(posixpath.basename(cleaned))

    for candidate in candidates:
        found = targets.get(candidate.lower())
        if found:
            return found
    return None


def analyze_graph_health(cfg: dict | None = None) -> dict:
    """Return wiki link and manifest health statistics."""
    cfg = cfg or get_config()
    wiki_dir = Path(cfg["paths"]["wiki_dir"])
    raw_dir = Path(cfg["paths"]["raw_dir"])
    manifest_path = Path(cfg["paths"]["manifest_file"])

    wiki_files = sorted(wiki_dir.rglob("*.md")) if wiki_dir.exists() else []
    article_files = [p for p in wiki_files if not _is_generated(_wiki_rel(p, wiki_dir))]

    targets: dict[str, Path] = {}
    for path in wiki_files:
        for key in _target_keys(path, wiki_dir):
            targets.setdefault(key, path)

    incoming: dict[Path, set[Path]] = {path: set() for path in article_files}
    outgoing: dict[Path, list[str]] = {path: [] for path in article_files}
    unresolved: list[dict] = []

    for path in article_files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for raw_link in WIKILINK_RE.findall(text):
            outgoing[path].append(raw_link)
            resolved = _resolve_target(raw_link, path, wiki_dir, targets)
            if resolved:
                if resolved in incoming:
                    incoming[resolved].add(path)
            else:
                unresolved.append({
                    "source": _wiki_rel(path, wiki_dir),
                    "target": raw_link,
                })

    orphans = [
        _wiki_rel(path, wiki_dir)
        for path in article_files
        if not outgoing.get(path) and not incoming.get(path)
    ]

    top_incoming = Counter({
        _wiki_rel(path, wiki_dir): len(refs)
        for path, refs in incoming.items()
    }).most_common(10)
    top_outgoing = Counter({
        _wiki_rel(path, wiki_dir): len(links)
        for path, links in outgoing.items()
    }).most_common(10)

    manifest = _load_manifest(manifest_path)
    raw_files = {}
    if raw_dir.exists():
        for path in raw_dir.rglob("*"):
            if path.is_file() and not path.name.startswith("."):
                rel = str(path.relative_to(raw_dir)).replace("\\", "/")
                raw_files[rel] = path

    manifest_new = sorted(rel for rel in raw_files if rel not in manifest)
    manifest_stale = sorted(rel for rel in manifest if rel not in raw_files)
    manifest_changed = []
    for rel in raw_files.keys() & manifest.keys():
        expected = manifest.get(rel, {}).get("hash")
        if expected and expected != _file_hash(raw_files[rel]):
            manifest_changed.append(rel)

    return {
        "wiki_files": len(wiki_files),
        "articles": len(article_files),
        "wikilinks": sum(len(links) for links in outgoing.values()),
        "unresolved": unresolved,
        "orphans": orphans,
        "top_incoming": top_incoming,
        "top_outgoing": top_outgoing,
        "manifest": {
            "path": str(manifest_path),
            "entries": len(manifest),
            "raw_files": len(raw_files),
            "new": manifest_new,
            "changed": sorted(manifest_changed),
            "stale": manifest_stale,
        },
    }


def _format_report(report: dict) -> str:
    lines = [
        "Wiki graph health",
        "",
        f"Articles:       {report['articles']} ({report['wiki_files']} markdown files including generated pages)",
        f"Wikilinks:      {report['wikilinks']}",
        f"Unresolved:     {len(report['unresolved'])}",
        f"Orphans:        {len(report['orphans'])}",
        "",
        "Manifest",
        f"  Raw files:    {report['manifest']['raw_files']}",
        f"  Entries:      {report['manifest']['entries']}",
        f"  New:          {len(report['manifest']['new'])}",
        f"  Changed:      {len(report['manifest']['changed'])}",
        f"  Stale:        {len(report['manifest']['stale'])}",
    ]

    if report["unresolved"]:
        lines.extend(["", "Unresolved sample"])
        for item in report["unresolved"][:20]:
            lines.append(f"  {item['source']} -> [[{item['target']}]]")

    if report["orphans"]:
        lines.extend(["", "Orphan sample"])
        for item in report["orphans"][:20]:
            lines.append(f"  {item}")

    if report["top_incoming"]:
        lines.extend(["", "Top incoming links"])
        for path, count in report["top_incoming"][:10]:
            if count:
                lines.append(f"  {count:>3}  {path}")

    return "\n".join(lines)


@click.command("graph-health")
@click.option("--json-output", is_flag=True, help="Output raw health data as JSON")
def cmd_graph_health(json_output):
    """Inspect unresolved wikilinks, orphan articles, and manifest drift."""
    report = analyze_graph_health()
    if json_output:
        click.echo(json.dumps(report, ensure_ascii=False, indent=2))
        return
    click.echo(_format_report(report))
