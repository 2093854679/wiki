"""LLM-powered Q&A against the compiled wiki and raw technical docs."""

from pathlib import Path

import click

from .llm import complete_with_context, get_config
from .search_engine import SearchEngine
from .retrieval_engine import filter_options

SYSTEM_PROMPT = """You are a research assistant answering questions against a personal knowledge base.
You have access to relevant wiki articles and raw technical documents provided as context documents.

Guidelines:
- Base your answer on the provided context documents.
- Cite specific wiki articles using [[wikilinks]].
- For raw technical documents, cite the file path explicitly.
- If the provided context doesn't contain enough information, say so clearly.
- Structure long answers with headings and bullet points.
- Include a ## Sources section listing the documents you referenced.
- Be thorough but concise - prefer depth over breadth."""


def _resolve_document_path(workspace_dir: Path, rel_path: str) -> Path | None:
    """Resolve a wiki-relative or workspace-relative markdown path."""
    rel = rel_path.replace("\\", "/").lstrip("/")

    candidates = []
    if rel.startswith(("wiki/", "raw/")):
        candidates.append(workspace_dir / rel)
    else:
        candidates.append(workspace_dir / "wiki" / rel)
        candidates.append(workspace_dir / "raw" / rel)

    for candidate in candidates:
        if candidate.exists():
            return candidate
    return None


def _load_documents(workspace_dir: Path, paths: list[str]) -> list[dict]:
    """Load markdown files by workspace-relative path."""
    docs = []
    for rel_path in paths:
        fpath = _resolve_document_path(workspace_dir, rel_path)
        if not fpath:
            click.echo(f"  [warn] Not found: {rel_path}", err=True)
            continue
        try:
            content = fpath.read_text(encoding="utf-8")
            if len(content) > 8000:
                content = content[:8000] + "\n\n[... truncated ...]"
            docs.append({
                "path": str(fpath.relative_to(workspace_dir)).replace("\\", "/"),
                "content": content,
            })
        except Exception:
            pass
    return docs


@click.command("query")
@click.argument("question")
@click.option("--format", "-f", "output_format",
              type=click.Choice(["md", "slides", "chart"]), default="md",
              help="Output format")
@click.option("--docs", "-d", multiple=True,
              help="Specific documents to include (wiki-relative or raw-relative paths)")
@click.option("--search", "-s", "use_search", is_flag=True, default=True,
              help="Use search to find relevant documents")
@click.option("--max-docs", default=15, type=click.IntRange(1, 30), help="Max passages to load")
@click.option("--save/--no-save", default=True, help="Save output to wiki/outputs/")
@filter_options
def cmd_query(question, output_format, docs, use_search, max_docs, save, **filters):
    """Ask a question against the knowledge base and get an LLM-researched answer."""
    cfg = get_config()
    wiki_dir = Path(cfg["paths"]["wiki_dir"])
    raw_dir = Path(cfg["paths"]["raw_dir"])
    workspace_dir = wiki_dir.parent

    if not wiki_dir.exists() and not raw_dir.exists():
        click.echo("Knowledge base is empty. Run 'kb ingest' and 'kb index' first.")
        return

    documents = []

    if list(docs):
        documents = _load_documents(workspace_dir, list(docs))
        click.echo(f"Loaded {len(documents)} specified documents.")
    else:
        engine = SearchEngine(Path(cfg["paths"]["search_db"]))
        if engine.document_count == 0 and (wiki_dir.exists() or raw_dir.exists()):
            click.echo("Indexing wiki and raw docs...")
            engine.index(wiki_dir, raw_dir)
        pack = engine.context(question, limit=min(max_docs, 12), max_chars=18000, **filters)
        documents = [{"path": r["citation"], "content": r["content"]} for r in pack["documents"]]
        click.echo(f"Search found {len(documents)} relevant passages.")

    if not documents:
        click.echo("No documents found to answer the question.")
        return

    if output_format == "slides":
        prompt = f"""Question: {question}

Write a Marp slide deck (markdown with --- slide separators) answering this question.
Use Marp directives for theming at the top. Cite wiki articles with [[wikilinks]] and
cite raw technical documents by file path.
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
Output ONLY the Python code in a ```python code block. Use data from the provided wiki and raw documents.
Keep the chart simple but informative."""
    else:
        prompt = f"""Question: {question}

Answer this question using the provided wiki articles and raw technical documents as context.
Write a thorough, well-structured response in markdown. Use [[wikilinks]] to reference wiki articles
and raw file paths for direct technical citations. Include a ## Sources section."""

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
