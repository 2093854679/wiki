"""Simple HTTP server for the search web UI."""

import json
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

import click

from .llm import get_config
from .search_engine import SearchEngine


class SearchHandler(SimpleHTTPRequestHandler):
    engine: SearchEngine = None
    static_dir: Path = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(self.static_dir), **kwargs)

    def do_GET(self):
        if self.path == "/api/search":
            self._handle_search()
        elif self.path == "/":
            self._serve_search_page()
        elif self.path == "/api/stats":
            self._handle_stats()
        else:
            super().do_GET()

    def _handle_search(self):
        import urllib.parse
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        query = params.get("q", [""])[0]
        limit = int(params.get("limit", ["20"])[0])

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        results = self.engine.search(query, limit=limit) if query else []
        self.wfile.write(json.dumps({"results": results, "query": query}).encode())

    def _handle_stats(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        cfg = get_config()
        wiki_dir = Path(cfg["paths"]["wiki_dir"])
        md_count = len(list(wiki_dir.rglob("*.md"))) if wiki_dir.exists() else 0
        total_words = 0
        if wiki_dir.exists():
            for md in wiki_dir.rglob("*.md"):
                try:
                    total_words += len(md.read_text(encoding="utf-8").split())
                except Exception:
                    pass

        self.wfile.write(json.dumps({
            "documents_indexed": self.engine.document_count,
            "total_articles": md_count,
            "total_words": total_words,
        }).encode())

    def _serve_search_page(self):
        html_path = self.static_dir / "search.html"
        if html_path.exists():
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html_path.read_bytes())
        else:
            self.send_error(404, "search.html not found")

    def log_message(self, format, *args):
        # Quieter logging
        if "/api/" in str(args[0]):
            click.echo(f"  search: {args[0]}")


@click.command("serve")
@click.option("--port", "-p", default=None, help="Port to listen on")
@click.option("--reindex", is_flag=True, help="Rebuild index before serving")
def cmd_serve(port, reindex):
    """Start a local web UI for searching the wiki."""
    cfg = get_config()
    p = port or cfg["search"]["port"]
    wiki_dir = Path(cfg["paths"]["wiki_dir"])
    db_path = Path(cfg["paths"]["search_db"])
    static_dir = Path(cfg["paths"]["static_dir"])

    engine = SearchEngine(db_path)
    if reindex or engine.document_count == 0:
        click.echo("Indexing wiki...")
        engine.index(wiki_dir)

    SearchHandler.engine = engine
    SearchHandler.static_dir = static_dir.resolve()

    server = HTTPServer(("0.0.0.0", p), SearchHandler)
    click.echo(f"\n  kb search server running at http://localhost:{p}")
    click.echo(f"  Indexed: {engine.document_count} documents")
    click.echo(f"  Press Ctrl+C to stop.\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        click.echo("\nShutting down...")
        server.shutdown()
