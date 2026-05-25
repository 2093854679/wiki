"""LLM health checks: find inconsistencies, gaps, and suggest improvements."""

from pathlib import Path

import click

from .llm import complete_with_context, get_config

SYSTEM_PROMPT = """You are a knowledge-base quality auditor. Your job is to review wiki articles
and identify issues, inconsistencies, gaps, and opportunities for improvement.

Be specific: cite exact article names and quote problematic passages.
Use [[wikilinks]] when referencing articles."""


def _load_articles(wiki_dir: Path, section: str | None, limit: int) -> list[dict]:
    """Load wiki articles for linting."""
    docs = []
    search_dir = wiki_dir / section if section else wiki_dir

    for md in sorted(search_dir.rglob("*.md")):
        if md.name == "index.md":
            continue
        try:
            content = md.read_text(encoding="utf-8")
            docs.append({
                "path": str(md.relative_to(wiki_dir)).replace("\\", "/"),
                "content": content[:5000],
            })
        except Exception:
            pass
        if len(docs) >= limit:
            break
    return docs


@click.command("lint")
@click.option("--check", "-c", "checks", multiple=True,
              type=click.Choice(["consistency", "gaps", "suggestions", "all"]),
              help="What to check for")
@click.option("--section", "-s", help="Limit to a wiki section (summaries, concepts, outputs)")
@click.option("--max-articles", default=30, help="Max articles to include")
def cmd_lint(checks, section, max_articles):
    """Run LLM health checks on the wiki."""
    cfg = get_config()
    wiki_dir = Path(cfg["paths"]["wiki_dir"])

    if not wiki_dir.exists():
        click.echo("Wiki directory not found. Run 'kb compile' first.")
        return

    if not checks:
        checks = ("all",)

    articles = _load_articles(wiki_dir, section, max_articles)
    if not articles:
        click.echo("No articles found to lint.")
        return

    click.echo(f"Linting {len(articles)} articles...")

    if "consistency" in checks or "all" in checks:
        _check_consistency(articles)
    if "gaps" in checks or "all" in checks:
        _check_gaps(articles)
    if "suggestions" in checks or "all" in checks:
        _check_suggestions(articles)


def _check_consistency(articles: list[dict]):
    """Find inconsistent claims across articles."""
    click.echo("\n--- Consistency Check ---\n")
    prompt = """Review these wiki articles and identify any CONTRADICTORY or INCONSISTENT claims.

For each issue found:
1. Quote the conflicting passages
2. Name the articles involved (use [[wikilinks]])
3. Suggest a resolution

If no inconsistencies are found, say so clearly.

Articles:"""

    result = complete_with_context(prompt, articles, system=SYSTEM_PROMPT)
    click.echo(result)


def _check_gaps(articles: list[dict]):
    """Identify missing topics or under-developed areas."""
    click.echo("\n--- Gap Analysis ---\n")
    prompt = """Review these wiki articles and identify MISSING TOPICS or gaps in coverage.

Consider:
- Topics referenced by [[wikilinks]] but not yet written
- Important subtopics that deserve their own article
- Areas where the existing coverage is too shallow
- Missing counter-arguments or alternative perspectives

Articles:"""

    result = complete_with_context(prompt, articles, system=SYSTEM_PROMPT)
    click.echo(result)


def _check_suggestions(articles: list[dict]):
    """Suggest new connections and article ideas."""
    click.echo("\n--- Suggestions ---\n")
    prompt = """Review these wiki articles and suggest:

1. INTERESTING CROSS-CONNECTIONS: Articles that should link to each other but don't
2. NEW ARTICLE CANDIDATES: Synthesize across articles to propose new concept articles
3. QUESTIONS TO EXPLORE: Interesting questions that arise from reading these articles

Be specific and use [[wikilinks]].

Articles:"""

    result = complete_with_context(prompt, articles, system=SYSTEM_PROMPT)
    click.echo(result)
