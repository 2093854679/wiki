"""Main CLI entry point for the kb tool."""

import click

from .ingest import cmd_ingest
from .compiler import cmd_compile
from .query import cmd_query
from .linter import cmd_lint
from .indexer import cmd_index
from .search_engine import cmd_search
from .server import cmd_serve
from .renderer import cmd_render


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

    md_files = [
        p for p in wiki.rglob("*.md")
        if p.name != "index.md" and "categories" not in p.parts
    ]
    total_words = 0
    for f in md_files:
        try:
            total_words += len(f.read_text(encoding="utf-8").split())
        except Exception:
            pass

    summaries = list((wiki / "summaries").rglob("*.md")) if (wiki / "summaries").exists() else []
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
