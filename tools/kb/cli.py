"""Main CLI entry point for the kb tool."""

import click

from .ingest import cmd_ingest, cmd_metadata, cmd_update_manifest
from .compiler import cmd_compile
from .query import cmd_query
from .linter import cmd_lint
from .indexer import cmd_index
from .search_engine import cmd_search
from .server import cmd_serve
from .renderer import cmd_render
from .graph_health import cmd_graph_health
from .workflow import cmd_refresh


@click.group()
@click.version_option(version="0.1.0", prog_name="kb")
def main():
    """kb — LLM-powered personal knowledge base toolkit.

    Build, query, lint, and search a markdown wiki compiled by LLMs
    from source documents in raw/.
    """
    pass


main.add_command(cmd_ingest, name="ingest")
main.add_command(cmd_compile, name="compile")
main.add_command(cmd_query, name="query")
main.add_command(cmd_lint, name="lint")
main.add_command(cmd_index, name="index")
main.add_command(cmd_search, name="search")
main.add_command(cmd_serve, name="serve")
main.add_command(cmd_render, name="render")
main.add_command(cmd_graph_health, name="graph-health")
main.add_command(cmd_update_manifest, name="update-manifest")
main.add_command(cmd_metadata, name="metadata")
main.add_command(cmd_refresh, name="refresh")

# stats is inline since it's simple
@main.command("stats")
def cmd_stats():
    """Show wiki statistics."""
    from pathlib import Path
    from .llm import get_config

    cfg = get_config()
    wiki = Path(cfg["paths"]["wiki_dir"])
    if not wiki.exists():
        click.echo("Wiki directory not found. Run 'kb compile' first.")
        return

    md_files = []
    for p in wiki.rglob("*.md"):
        rel = p.relative_to(wiki)
        rel_text = str(rel).replace("\\", "/")
        if p.name in {"index.md", "WIKI.md"} or rel_text.startswith("categories/"):
            continue
        if rel_text == "summaries/index.md" or (rel_text.startswith("summaries/") and rel_text.endswith("/index.md")):
            continue
        md_files.append(p)
    total_words = 0
    for f in md_files:
        try:
            total_words += len(f.read_text(encoding="utf-8").split())
        except Exception:
            pass

    summaries = []
    if (wiki / "summaries").exists():
        for p in (wiki / "summaries").rglob("*.md"):
            rel_text = str(p.relative_to(wiki)).replace("\\", "/")
            if rel_text == "summaries/index.md" or (rel_text.startswith("summaries/") and rel_text.endswith("/index.md")):
                continue
            summaries.append(p)
    concepts = list((wiki / "concepts").rglob("*.md")) if (wiki / "concepts").exists() else []
    outputs = list((wiki / "outputs").rglob("*")) if (wiki / "outputs").exists() else []

    click.echo(f"Articles (total):  {len(md_files)}")
    click.echo(f"  Summaries:       {len(summaries)}")
    click.echo(f"  Concepts:        {len(concepts)}")
    click.echo(f"  Outputs:         {len(outputs)}")
    click.echo(f"Total words:       {total_words:,}")
    click.echo(f"Index:             {'present' if (wiki / 'index.md').exists() else 'missing'}")


if __name__ == "__main__":
    main()
