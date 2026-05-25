"""LLM-powered Q&A against the compiled wiki."""

from pathlib import Path

import click

from .llm import complete_with_context, get_config
from .search_engine import SearchEngine

SYSTEM_PROMPT = """You are a research assistant answering questions against a personal knowledge base wiki.
You have access to relevant wiki articles provided as context documents.

Guidelines:
- Base your answer on the provided wiki articles. Cite specific articles using [[wikilinks]].
- If the wiki doesn't contain enough information, say so clearly.
- Structure long answers with headings and bullet points.
- Include a ## Sources section listing the wiki articles you referenced.
- Be thorough but concise — prefer depth over breadth."""


def _load_wiki_documents(wiki_dir: Path, max_docs: int = 15) -> list[dict]:
    """Load wiki markdown files as context documents."""
    docs = []
    for md in sorted(wiki_dir.rglob("*.md")):
        if md.name == "index.md":
            continue
        try:
            content = md.read_text(encoding="utf-8")
            if len(content) > 6000:
                content = content[:6000] + "\n\n[... truncated ...]"
            docs.append({
                "path": str(md.relative_to(wiki_dir)).replace("\\", "/"),
                "content": content,
            })
        except Exception:
            pass
    return docs[:max_docs]


def _load_specific_docs(wiki_dir: Path, paths: list[str]) -> list[dict]:
    """Load specific wiki documents by relative path."""
    docs = []
    for p in paths:
        fpath = wiki_dir / p
        if fpath.exists():
            try:
                content = fpath.read_text(encoding="utf-8")
                docs.append({
                    "path": p,
                    "content": content[:8000],
                })
            except Exception:
                pass
        else:
            click.echo(f"  [warn] Not found: {p}", err=True)
    return docs


@click.command("query")
@click.argument("question")
@click.option("--format", "-f", "output_format",
              type=click.Choice(["md", "slides", "chart"]), default="md",
              help="Output format")
@click.option("--docs", "-d", multiple=True,
              help="Specific wiki documents to include (relative paths)")
@click.option("--search", "-s", "use_search", is_flag=True, default=True,
              help="Use search to find relevant documents")
@click.option("--max-docs", default=15, help="Max documents to load")
@click.option("--save/--no-save", default=True, help="Save output to wiki/outputs/")
def cmd_query(question, output_format, docs, use_search, max_docs, save):
    """Ask a question against the wiki and get an LLM-researched answer."""
    cfg = get_config()
    wiki_dir = Path(cfg["paths"]["wiki_dir"])

    if not wiki_dir.exists() or not list(wiki_dir.rglob("*.md")):
        click.echo("Wiki is empty. Run 'kb compile' first.")
        return

    documents = []

    if list(docs):
        documents = _load_specific_docs(wiki_dir, list(docs))
        click.echo(f"Loaded {len(documents)} specified documents.")
    elif use_search:
        engine = SearchEngine(Path(cfg["paths"]["search_db"]))
        results = engine.search(question, limit=max_docs)
        if results:
            paths = [r["path"] for r in results]
            documents = _load_specific_docs(wiki_dir, paths)
            click.echo(f"Search found {len(documents)} relevant documents.")
        else:
            documents = _load_wiki_documents(wiki_dir, max_docs)
            click.echo(f"Loaded {len(documents)} documents (search index empty, using all).")
    else:
        documents = _load_wiki_documents(wiki_dir, max_docs)
        click.echo(f"Loaded {len(documents)} documents.")

    if not documents:
        click.echo("No documents found to answer the question.")
        return

    if output_format == "slides":
        prompt = f"""Question: {question}

Write a Marp slide deck (markdown with --- slide separators) answering this question.
Use Marp directives for theming at the top. Cite wiki articles with [[wikilinks]].
Each slide should be focused on one key point. 5-10 slides total.

Start with:
---
marp: true
theme: default
---"""
    elif output_format == "chart":
        prompt = f"""Question: {question}

Generate Python matplotlib code that creates a chart visualizing the answer to this question.
The chart should be well-labeled with title, axis labels, and legend if applicable.
Output ONLY the Python code in a ```python code block. Use data from the wiki articles provided.
Keep the chart simple but informative."""
    else:
        prompt = f"""Question: {question}

Answer this question using the wiki articles provided as context. Write a thorough, well-structured
response in markdown. Use [[wikilinks]] to reference wiki articles. Include a ## Sources section."""

    click.echo("Researching...")
    answer = complete_with_context(
        prompt,
        documents,
        system=SYSTEM_PROMPT,
    )

    click.echo(f"\n{'='*60}\n")
    click.echo(answer)

    if save:
        outputs_dir = wiki_dir / "outputs"
        outputs_dir.mkdir(parents=True, exist_ok=True)
        slug = question[:60].replace(" ", "-").replace("?", "").lower()
        ext = "md"
        if output_format == "slides":
            ext = "md"
            slug = f"slides-{slug}"
        elif output_format == "chart":
            ext = "py"
            slug = f"chart-{slug}"
        out_path = outputs_dir / f"{slug}.{ext}"
        out_path.write_text(answer, encoding="utf-8")
        click.echo(f"\nSaved to wiki/outputs/{slug}.{ext}")
