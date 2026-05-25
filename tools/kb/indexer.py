"""Auto-generate index.md and per-section index files."""

from pathlib import Path

import click
from jinja2 import Environment, FileSystemLoader

from .llm import get_config


def _title_from_md(filepath: Path) -> str:
    """Extract first heading from a markdown file."""
    try:
        for line in filepath.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("# ") and not line.startswith("## "):
                return line[2:].strip()
    except Exception:
        pass
    return filepath.stem.replace("-", " ").title()


def _tldr_from_md(filepath: Path) -> str:
    """Extract TLDR line from a markdown file."""
    try:
        text = filepath.read_text(encoding="utf-8")
        for line in text.splitlines():
            if line.strip().lower().startswith("tldr") or line.strip().lower().startswith("> **tldr"):
                return line.strip()
            if line.strip().startswith("> ") and "tldr" in line.lower():
                return line.strip()
    except Exception:
        pass
    return ""


def _backlinks_from_md(filepath: Path) -> list[str]:
    """Extract [[wikilinks]] from a markdown file."""
    import re
    try:
        text = filepath.read_text(encoding="utf-8")
        return re.findall(r"\[\[([^\]]+)\]\]", text)
    except Exception:
        return []


def _scan_wiki(wiki_dir: Path) -> dict:
    """Scan wiki directory and return structured data."""
    sections = {
        "summaries": [],
        "concepts": [],
        "outputs": [],
        "other": [],
    }

    for md in sorted(wiki_dir.rglob("*.md")):
        rel = str(md.relative_to(wiki_dir)).replace("\\", "/")
        if rel == "index.md":
            continue

        entry = {
            "path": rel,
            "title": _title_from_md(md),
            "tldr": _tldr_from_md(md),
            "backlinks": _backlinks_from_md(md),
        }

        if rel.startswith("summaries/"):
            sections["summaries"].append(entry)
        elif rel.startswith("concepts/"):
            sections["concepts"].append(entry)
        elif rel.startswith("outputs/"):
            sections["outputs"].append(entry)
        else:
            sections["other"].append(entry)

    return sections


def _build_index(sections: dict, cfg: dict) -> str:
    """Generate the master index.md using a Jinja2 template."""
    templates_dir = Path(cfg["paths"]["templates_dir"])
    if templates_dir.exists() and (templates_dir / "index.md.j2").exists():
        env = Environment(loader=FileSystemLoader(str(templates_dir)))
        tpl = env.get_template("index.md.j2")
        return tpl.render(
            sections=sections,
            summary_count=len(sections["summaries"]),
            concept_count=len(sections["concepts"]),
            total_count=sum(len(v) for v in sections.values()),
        )
    else:
        return _build_index_plain(sections)


def _build_index_plain(sections: dict) -> str:
    """Build a plain index.md without templates."""
    lines = [
        "# Wiki Index",
        "",
        f"*Auto-generated index of {sum(len(v) for v in sections.values())} articles.*",
        "",
    ]

    for section_key, section_name in [
        ("concepts", "Concepts"),
        ("summaries", "Summaries"),
        ("outputs", "Outputs"),
        ("other", "Other"),
    ]:
        items = sections.get(section_key, [])
        if not items:
            continue
        lines.append(f"## {section_name} ({len(items)})")
        lines.append("")
        for item in items:
            link = f"[{item['title']}]({item['path']})"
            if item["tldr"]:
                lines.append(f"- {link} — {item['tldr']}")
            else:
                lines.append(f"- {link}")
        lines.append("")

    # Backlink graph section
    lines.append("## Backlink Graph")
    lines.append("")
    all_articles = {}
    for items in sections.values():
        for item in items:
            all_articles[item["title"]] = set()

    for items in sections.values():
        for item in items:
            for bl in item["backlinks"]:
                if bl in all_articles:
                    all_articles[bl].add(item["title"])

    for title, linked_from in sorted(all_articles.items()):
        if linked_from:
            lines.append(f"- [[{title}]] ← referenced by: {', '.join(sorted(linked_from)[:5])}")
            if len(linked_from) > 5:
                lines[-1] += f" (+ {len(linked_from) - 5} more)"

    lines.append("")
    lines.append("---")
    lines.append("*Run `kb index` to regenerate this file.*")

    return "\n".join(lines)


@click.command("index")
def cmd_index():
    """Rebuild wiki index files from current content."""
    cfg = get_config()
    wiki_dir = Path(cfg["paths"]["wiki_dir"])

    if not wiki_dir.exists():
        click.echo("Wiki directory not found. Run 'kb compile' first.")
        return

    sections = _scan_wiki(wiki_dir)
    total = sum(len(v) for v in sections.values())

    click.echo(f"Indexing {total} articles...")
    click.echo(f"  Summaries: {len(sections['summaries'])}")
    click.echo(f"  Concepts:  {len(sections['concepts'])}")
    click.echo(f"  Outputs:   {len(sections['outputs'])}")

    index_content = _build_index(sections, cfg)
    (wiki_dir / "index.md").write_text(index_content, encoding="utf-8")

    click.echo(f"  -> wiki/index.md updated.")
