"""LLM-powered compilation: raw documents → wiki summaries + concepts."""

import json
from datetime import datetime, timezone
from pathlib import Path

import click

from .llm import complete, complete_with_context, get_config
from .ingest import scan_raw, _load_manifest, _save_manifest, _file_hash

SYSTEM_PROMPT = """You are a knowledge-base compiler. Your job is to read source documents
and produce well-structured, interlinked markdown articles for a personal wiki.

Guidelines:
- Write clear, concise summaries that capture the key arguments and evidence.
- When extracting concepts, synthesize across documents — don't just repeat one source.
- Use [[wikilink]] syntax for internal links to other articles.
- Every article should have a one-sentence TLDR at the top.
- Include a ## Related section with links to related concepts.
- Attribute sources: mention which raw/ file the information came from.
- Prefer specific facts over vague generalizations.
- Write in the same language as the source document."""


def _ensure_dirs(cfg: dict):
    for key in ["wiki_dir", "summaries_dir", "concepts_dir"]:
        Path(cfg["paths"][key]).mkdir(parents=True, exist_ok=True)


def _slug_from_path(file_path: str) -> str:
    """Convert a raw file path to a wiki-safe slug."""
    p = Path(file_path)
    return p.stem.replace(" ", "-").lower()


def _source_metadata(file_path: str) -> dict[str, str]:
    """Derive stable source metadata from a raw file path."""
    parts = [p for p in Path(file_path).parts if p not in ("", ".")]
    root = parts[0] if parts else "Other"
    if root.lower() == "bk_doc":
        section = parts[2] if len(parts) > 2 else (parts[1] if len(parts) > 1 else "")
    else:
        section = parts[1] if len(parts) > 1 else ""

    return {
        "source_root": root,
        "source_section": section,
    }


def compile_summary(raw_dir: Path, file_info: dict, cfg: dict) -> str:
    """Generate a summary of a single raw document."""
    fpath = Path(file_info["absolute_path"])
    content = fpath.read_text(encoding="utf-8", errors="replace")
    max_chunk = cfg["compiler"]["max_chunk_size"]
    if len(content) > max_chunk:
        content = content[:max_chunk] + "\n\n[... content truncated ...]"

    prompt = f"""Read the following source document and write a summary.

<source path="{file_info['path']}">
{content}
</source>

Write a summary (max {cfg['compiler']['summary_max_words']} words) with:
1. A one-sentence TLDR
2. Key points as bullet list
3. Main arguments / findings
4. ## Related — suggest 2-4 related concept articles (use [[wikilinks]])

Output as a markdown article. Title: {_slug_from_path(file_info['path'])}"""

    summary = complete(prompt, system=SYSTEM_PROMPT).strip()
    meta = _source_metadata(file_info["path"])
    frontmatter = [
        "---",
        f"source_path: {json.dumps(file_info['path'], ensure_ascii=False)}",
        f"source_root: {json.dumps(meta['source_root'], ensure_ascii=False)}",
        f"source_section: {json.dumps(meta['source_section'], ensure_ascii=False)}",
        f"compiled_at: {json.dumps(datetime.now(timezone.utc).isoformat(), ensure_ascii=False)}",
        "---",
        "",
    ]
    return "\n".join(frontmatter) + summary + "\n"


def extract_concepts(raw_dir: Path, new_summaries: list[dict], existing_concepts: list[str], cfg: dict) -> list[dict]:
    """Extract new concept articles by synthesizing across summaries."""
    summaries_text = []
    for s in new_summaries:
        spath = Path(cfg["paths"]["summaries_dir"]) / f"{s['slug']}.md"
        if spath.exists():
            summaries_text.append({
                "path": str(spath),
                "content": spath.read_text(encoding="utf-8"),
            })

    if not summaries_text:
        return []

    existing_list = "\n".join(f"- {c}" for c in existing_concepts) if existing_concepts else "(none yet)"

    prompt = f"""I have the following new document summaries:

{chr(10).join(f"- {s['path']}" for s in summaries_text)}

Existing concept articles:
{existing_list}

Read the summaries (attached below) and identify 2-5 new concept articles that should be written.
These should SYNTHESIZE across multiple sources, not just repeat one document.

For each concept, provide:
1. A title (slug format, e.g. "transformer-attention-mechanism")
2. A 2-3 sentence scope description

Output as JSON array:
[{{"title": "...", "slug": "...", "scope": "..."}}]"""

    response = complete_with_context(
        prompt,
        summaries_text,
        system=SYSTEM_PROMPT,
    )
    try:
        # Extract JSON array from response
        start = response.index("[")
        end = response.rindex("]") + 1
        return json.loads(response[start:end])
    except (ValueError, json.JSONDecodeError):
        click.echo("  Warning: could not parse concept suggestions from LLM response", err=True)
        return []


def write_concept_article(concept: dict, all_summaries: list[dict], cfg: dict) -> str:
    """Write a full concept article using all relevant summaries as context."""
    prompt = f"""Write a comprehensive concept article:

Title: {concept['title']}
Scope: {concept['scope']}

Guidelines:
- Max {cfg['compiler']['concept_max_words']} words
- Synthesize information from multiple source summaries (attached)
- Include a one-sentence TLDR
- Use [[wikilinks]] to link to related concepts and summaries
- Include a ## Related section
- Attribute sources to specific raw/ files

Write the full article in markdown."""

    return complete_with_context(
        prompt,
        all_summaries,
        system=SYSTEM_PROMPT,
        max_tokens=cfg["compiler"]["concept_max_words"] * 3,
    )


@click.command("compile")
@click.option("--files", "-f", multiple=True, help="Specific raw files to compile")
@click.option("--new", "only_new", is_flag=True, help="Only compile new/changed files")
@click.option("--all", "compile_all", is_flag=True, help="Recompile all files")
@click.option("--concepts-only", is_flag=True, help="Only extract/write concept articles")
@click.option("--summaries-only", is_flag=True, help="Only write summaries")
@click.option("--dry-run", is_flag=True, help="Show what would be compiled without doing it")
def cmd_compile(files, only_new, compile_all, concepts_only, summaries_only, dry_run):
    """Compile raw documents into wiki summaries and concept articles using LLM."""
    cfg = get_config()
    raw_dir = Path(cfg["paths"]["raw_dir"])
    manifest_path = Path(cfg["paths"]["manifest_file"])
    manifest = _load_manifest(manifest_path)

    _ensure_dirs(cfg)

    all_files = scan_raw(raw_dir, manifest)
    targets = all_files

    if list(files):
        targets = [f for f in all_files if f["path"] in files]
    elif only_new:
        targets = [f for f in all_files if f["status"] in ("new", "changed")]
    elif not compile_all:
        targets = [f for f in all_files if f["status"] in ("new", "changed")]

    if not targets:
        click.echo("No files to compile. Use --all to recompile everything.")
        return

    compilable = [f for f in targets if f["type"] in ("markdown", "text", "web", "document")]
    skipped = [f for f in targets if f not in compilable]

    click.echo(f"Compiling {len(compilable)} files...")
    for s in skipped:
        click.echo(f"  [skip] {s['path']} (type={s['type']} — not text-based)")

    if dry_run:
        for f in compilable:
            click.echo(f"  [would compile] {f['path']}")
        return

    summaries_dir = Path(cfg["paths"]["summaries_dir"])
    concepts_dir = Path(cfg["paths"]["concepts_dir"])

    new_slugs = []

    if not concepts_only:
        for i, f in enumerate(compilable):
            slug = _slug_from_path(f["path"])
            click.echo(f"  [{i+1}/{len(compilable)}] Summarizing: {f['path']}")

            try:
                summary = compile_summary(raw_dir, f, cfg)
                out_path = summaries_dir / f"{slug}.md"
                out_path.write_text(summary, encoding="utf-8")
                manifest[f["path"]] = {
                    "hash": f["hash"],
                    "last_compiled": datetime.now(timezone.utc).isoformat(),
                    "slug": slug,
                }
                new_slugs.append({"slug": slug, "path": f["path"]})
                click.echo(f"         -> wiki/summaries/{slug}.md")
            except Exception as e:
                click.echo(f"         [error] {e}", err=True)

        _save_manifest(manifest_path, manifest)

    if not summaries_only and cfg["compiler"]["extract_concepts"]:
        existing = [p.stem for p in concepts_dir.rglob("*.md")] if concepts_dir.exists() else []
        click.echo("\n  Extracting concept articles...")
        try:
            concepts = extract_concepts(raw_dir, new_slugs, existing, cfg)
        except Exception as e:
            click.echo(f"  [error] Concept extraction failed: {e}", err=True)
            concepts = []

        existing_summaries = []
        for smd in summaries_dir.rglob("*.md"):
            existing_summaries.append({
                "path": str(smd),
                "content": smd.read_text(encoding="utf-8"),
            })

        for c in concepts:
            click.echo(f"  Writing concept: {c['title']}")
            try:
                article = write_concept_article(c, existing_summaries, cfg)
                (concepts_dir / f"{c['slug']}.md").write_text(article, encoding="utf-8")
                click.echo(f"         -> wiki/concepts/{c['slug']}.md")
            except Exception as e:
                click.echo(f"         [error] {e}", err=True)

    click.echo(f"\nDone. {len(compilable)} summaries, concepts extracted. Run 'kb index' next.")
