"""SQLite FTS5 full-text search engine over the wiki."""

import sqlite3
from pathlib import Path

import click

from .llm import get_config


class SearchEngine:
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(str(self.db_path)) as conn:
            conn.execute("""
                CREATE VIRTUAL TABLE IF NOT EXISTS documents
                USING fts5(path, title, content, tokenize='porter unicode61')
            """)
            conn.commit()

    def index(self, wiki_dir: Path):
        """Index all markdown files in the wiki."""
        with sqlite3.connect(str(self.db_path)) as conn:
            conn.execute("DELETE FROM documents")
            for md in wiki_dir.rglob("*.md"):
                if md.name == "index.md":
                    continue
                try:
                    text = md.read_text(encoding="utf-8")
                    rel = str(md.relative_to(wiki_dir)).replace("\\", "/")
                    title = rel
                    for line in text.splitlines():
                        line = line.strip()
                        if line.startswith("# ") and not line.startswith("## "):
                            title = line[2:].strip()
                            break
                    conn.execute(
                        "INSERT INTO documents (path, title, content) VALUES (?, ?, ?)",
                        (rel, title, text),
                    )
                except Exception:
                    pass
            conn.commit()

    def search(self, query: str, limit: int = 20) -> list[dict]:
        """Search the index and return ranked results."""
        with sqlite3.connect(str(self.db_path)) as conn:
            try:
                rows = conn.execute(
                    """SELECT path, title, snippet(documents, 2, '<b>', '</b>', '...', 40)
                       FROM documents WHERE documents MATCH ?
                       ORDER BY rank LIMIT ?""",
                    (query, limit),
                ).fetchall()
            except sqlite3.OperationalError:
                # Fallback for invalid FTS queries (special chars)
                rows = conn.execute(
                    """SELECT path, title, substr(content, 1, 200)
                       FROM documents WHERE content LIKE ?
                       LIMIT ?""",
                    (f"%{query}%", limit),
                ).fetchall()

            return [
                {"path": r[0], "title": r[1], "snippet": r[2]}
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
    """Full-text search over the wiki."""
    cfg = get_config()
    wiki_dir = Path(cfg["paths"]["wiki_dir"])
    db_path = Path(cfg["paths"]["search_db"])

    engine = SearchEngine(db_path)

    if reindex or engine.document_count == 0:
        if wiki_dir.exists():
            click.echo("Indexing wiki...")
            engine.index(wiki_dir)
        else:
            click.echo("Wiki directory not found. Run 'kb compile' first.")
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
        click.echo(f"  [{r['title']}]({r['path']})")
        snippet = r["snippet"].replace("\n", " ")[:150]
        click.echo(f"  {snippet}\n")
