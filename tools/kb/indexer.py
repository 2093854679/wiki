"""Auto-generate wiki indexes with raw-source category grouping."""

from __future__ import annotations

from pathlib import Path
import re
import unicodedata

import click
from jinja2 import Environment, FileSystemLoader
import yaml

from .llm import get_config


CATEGORY_DISPLAY_NAMES = {
    "bk_doc": "BK Docs",
    "Study_Note": "Study Note",
    "desktop_pet": "Desktop Pet",
    "Other": "Other",
}

CATEGORY_SLUGS = {
    "bk_doc": "bk-doc",
    "Study_Note": "study-note",
    "desktop_pet": "desktop-pet",
}


def _canonical_category(value: str) -> str:
    """Return a stable internal category name."""
    raw = (value or "").replace("\\", "/").strip()
    lower = raw.lower()

    if lower in {"beken", "beken.md", "bk_doc", "bk-doc", "bk_doc.md"}:
        return "bk_doc"
    if lower in {"study_note", "study-note", "study_note.md"}:
        return "Study_Note"
    if (
        lower in {"desktop_pet", "desktop-pet"}
        or "智能桌面" in raw
        or "桌面萌宠" in raw
        or "鏅鸿兘" in raw
        or "钀屽疇" in raw
    ):
        return "desktop_pet"
    return raw or "Other"


def _title_from_md(filepath: Path) -> str:
    """Extract first heading from a markdown file."""
    try:
        for line in filepath.read_text(encoding="utf-8-sig").splitlines():
            line = line.strip()
            if line.startswith("# ") and not line.startswith("## "):
                return line[2:].strip()
    except Exception:
        pass
    return filepath.stem.replace("-", " ").title()


def _tldr_from_md(filepath: Path) -> str:
    """Extract TLDR line from a markdown file."""
    try:
        text = filepath.read_text(encoding="utf-8-sig")
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
    try:
        text = filepath.read_text(encoding="utf-8-sig")
        return re.findall(r"\[\[([^\]]+)\]\]", text)
    except Exception:
        return []


def _frontmatter_from_md(filepath: Path) -> dict:
    """Parse optional YAML frontmatter from a markdown file."""
    try:
        text = filepath.read_text(encoding="utf-8-sig")
    except Exception:
        return {}

    if not text.startswith("---\n"):
        return {}

    end = text.find("\n---\n", 4)
    if end == -1:
        return {}

    try:
        data = yaml.safe_load(text[4:end]) or {}
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def _source_from_md(filepath: Path) -> str:
    """Extract the raw source path from a summary file."""
    meta = _frontmatter_from_md(filepath)
    if meta.get("source_path"):
        return str(meta["source_path"])

    try:
        for line in filepath.read_text(encoding="utf-8-sig").splitlines():
            if line.startswith("> **Source:**"):
                match = re.search(r"\(([^)]+)\)", line)
                if match:
                    return match.group(1)
    except Exception:
        pass
    return ""


def _category_from_source(
    source: str,
    md_path: Path | None = None,
    title: str = "",
    source_root: str = "",
    source_section: str = "",
) -> str:
    """Map a raw source path to its top-level category."""
    if source_root:
        return _canonical_category(source_root)

    raw_path = source.replace("\\", "/")
    idx = raw_path.lower().find("raw/")
    if idx >= 0:
        rel = raw_path[idx + 4 :]
        parts = [p for p in rel.split("/") if p]
        if parts:
            return _canonical_category(parts[0])

    hint = f"{title} {(md_path.stem if md_path else '')} {source}".lower()
    if any(token in hint for token in ["bk723", "bk_doc", "beken", "cli_api", "armino"]):
        return "bk_doc"
    if any(token in hint for token in ["desktop-pet", "desktop_pet", "宠物", "萌宠"]):
        return "desktop_pet"
    if any(token in hint for token in ["interview", "task-development", "study_note", "study note", "面试", "task"]):
        return "Study_Note"

    parts = [p for p in raw_path.split("/") if p]
    return _canonical_category(parts[0] if parts else "Other")


def _pretty_category_name(category: str) -> str:
    """Human-friendly display name for a raw category."""
    return CATEGORY_DISPLAY_NAMES.get(category, category)


def _category_slug(category: str) -> str:
    """Stable filename for a category hub page."""
    if category in CATEGORY_SLUGS:
        return CATEGORY_SLUGS[category]
    normalized = unicodedata.normalize("NFKD", category).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", normalized.lower()).strip("-")
    return slug or "category"


def _category_subgroup(item: dict) -> str:
    """Return a second-level subgroup name from the source path."""
    if item.get("source_section"):
        return str(item["source_section"])

    source = item.get("source", "").replace("\\", "/")
    idx = source.lower().find("raw/")
    if idx >= 0:
        source = source[idx + 4 :]
    parts = [p for p in source.split("/") if p]
    if item.get("category") == "bk_doc" and len(parts) > 2:
        return parts[2]
    return parts[1] if len(parts) > 1 else "Misc"


def _build_category_page(category: dict, wiki_dir: Path) -> str:
    """Render a standalone category hub page."""
    lines = [
        f"# {category['display_name']}",
        "",
        f"*{len(category['items'])} summaries from `{category['name']}`.*",
        "",
    ]

    # For BK Docs with chip hub pages, skip flat listing — chip pages have their own
    has_chip_nav = False
    if category["name"] == "bk_doc":
        chip_dir = wiki_dir / "categories" / "bk-doc"
        if chip_dir.is_dir():
            chips = sorted(chip_dir.glob("*.md"))
            if chips:
                has_chip_nav = True
                lines.append("## Chip Hubs")
                lines.append("")
                labels = {
                    "bk7235": "BK7235",
                    "bk7236": "BK7236",
                    "bk7236n": "BK7236N",
                    "bk7239": "BK7239",
                    "bk7256": "BK7256",
                    "bk7258": "BK7258",
                    "matter": "BK Matter",
                }
                for chip in chips:
                    stem = chip.stem
                    label = labels.get(stem, stem.upper())
                    lines.append(f"- **[{label}](bk-doc/{stem})**")
                lines.append("")
                lines.append("Open a chip hub for module navigation, curated summaries, and raw document links.")
                lines.append("")

    if not has_chip_nav:
        subgroups: dict[str, list[dict]] = {}
        for item in category["items"]:
            subgroups.setdefault(_category_subgroup(item), []).append(item)

        for subgroup_name in sorted(subgroups, key=lambda s: s.lower()):
            items = subgroups[subgroup_name]
            lines.append(f"## {subgroup_name} ({len(items)})")
            lines.append("")
            for item in items:
                link = f"[{item['title']}](../{item['path']})"
                if item["tldr"]:
                    lines.append(f"- {link} - {item['tldr']}")
                else:
                    lines.append(f"- {link}")
            lines.append("")

    lines.append("---")
    lines.append("*Generated by `kb index`.*")
    return "\n".join(lines)


def _is_generated_category_page(filepath: Path) -> bool:
    """Detect whether a category page was generated by kb index."""
    try:
        return "*Generated by `kb index`.*" in filepath.read_text(encoding="utf-8-sig")
    except Exception:
        return False


def _scan_wiki(wiki_dir: Path) -> dict:
    """Scan wiki directory and return structured data."""
    sections = {"summaries": [], "concepts": [], "outputs": [], "other": []}
    source_categories: dict[str, list[dict]] = {}
    manual_categories: list[dict] = []

    for md in sorted(wiki_dir.rglob("*.md")):
        rel = str(md.relative_to(wiki_dir)).replace("\\", "/")
        if rel in {"index.md", "WIKI.md", "AI-SEARCH.md"} or rel.startswith("categories/"):
            continue
        if rel == "summaries/index.md" or (rel.startswith("summaries/") and rel.endswith("/index.md")):
            continue

        entry = {
            "path": rel,
            "title": _title_from_md(md),
            "tldr": _tldr_from_md(md),
            "backlinks": _backlinks_from_md(md),
        }

        if rel.startswith("summaries/"):
            meta = _frontmatter_from_md(md)
            entry["source"] = meta.get("source_path") or _source_from_md(md)
            entry["source_root"] = meta.get("source_root", "")
            entry["source_section"] = meta.get("source_section", "")
            entry["category"] = _category_from_source(
                entry["source"],
                md,
                entry["title"],
                entry["source_root"],
                entry["source_section"],
            )
            sections["summaries"].append(entry)
            source_categories.setdefault(entry["category"], []).append(entry)
        elif rel.startswith("concepts/"):
            sections["concepts"].append(entry)
        elif rel.startswith("outputs/"):
            sections["outputs"].append(entry)
        else:
            sections["other"].append(entry)

    grouped = [
        {
            "name": name,
            "slug": _category_slug(name),
            "display_name": _pretty_category_name(name),
            "items": items,
        }
        for name, items in sorted(source_categories.items(), key=lambda x: x[0].lower())
    ]

    categories_dir = wiki_dir / "categories"
    if categories_dir.is_dir():
        known_slugs = {group["slug"] for group in grouped}
        for md in sorted(categories_dir.glob("*.md")):
            if _is_generated_category_page(md):
                continue
            slug = md.stem
            if slug in known_slugs:
                continue
            manual_categories.append(
                {
                    "name": slug,
                    "slug": slug,
                    "display_name": _title_from_md(md),
                    "items": [],
                    "path": f"categories/{slug}.md",
                    "manual": True,
                }
            )

    sections["concepts"] = sorted(sections["concepts"], key=lambda item: item["title"].lower())
    sections["groups"] = grouped
    sections["manual_categories"] = manual_categories
    return sections


def _build_index(sections: dict, cfg: dict) -> str:
    """Generate the master index.md using a Jinja2 template."""
    templates_dir = Path(cfg["paths"]["templates_dir"])
    if templates_dir.exists() and (templates_dir / "index.md.j2").exists():
        env = Environment(loader=FileSystemLoader(str(templates_dir)))
        tpl = env.get_template("index.md.j2")
        return tpl.render(
            sections=sections,
            groups=sections.get("groups", []),
            summary_count=len(sections["summaries"]),
            concept_count=len(sections["concepts"]),
            total_count=len(sections["summaries"]) + len(sections["concepts"]) + len(sections["outputs"]) + len(sections["other"]),
        )
    return _build_index_plain(sections)


def _build_index_plain(sections: dict) -> str:
    """Build a plain index.md without templates."""
    lines = [
        "# Wiki Index",
        "",
        f"*Auto-generated dashboard for {len(sections['summaries']) + len(sections['concepts']) + len(sections['outputs']) + len(sections['other'])} articles.*",
        "",
    ]

    lines.append("## Semantic Map")
    lines.append("")
    lines.append("- [Concept Map](concepts/concept-map.md) - LLM routing layer across domains, concepts, summaries, and raw sources")
    lines.append("")

    groups = sections.get("groups", [])
    if groups:
        lines.append("## Categories")
        lines.append("")
        for group in groups:
            lines.append(f"- [{group['display_name']}](categories/{group['slug']}.md) - {len(group['items'])} summaries")
        lines.append("")

    manual_categories = sections.get("manual_categories", [])
    if manual_categories:
        lines.append("## Doc Families")
        lines.append("")
        for item in manual_categories:
            lines.append(f"- [{item['display_name']}]({item['path']})")
        lines.append("")

    lines.append("- [All concepts](categories/concepts.md)")
    lines.append("- [AI search guide](AI-SEARCH.md)")
    lines.append("")

    if sections.get("outputs"):
        lines.append(f"## Outputs ({len(sections['outputs'])})")
        lines.append("")
        for item in sections["outputs"]:
            lines.append(f"- [{item['title']}]({item['path']})")
        lines.append("")

    lines.append("## Maintenance")
    lines.append("")
    lines.append("- `python -m tools.kb ingest --status new` - detect new raw files")
    lines.append("- `python -m tools.kb index` - rebuild this dashboard and category pages")
    lines.append("- `python -m tools.kb graph-health` - inspect unresolved links, orphans, and manifest drift")
    lines.append("- `python -m tools.kb stats` - count current wiki articles")

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
    total = len(sections["summaries"]) + len(sections["concepts"]) + len(sections["outputs"]) + len(sections["other"])

    click.echo(f"Indexing {total} articles...")
    click.echo(f"  Summaries: {len(sections['summaries'])}")
    click.echo(f"  Concepts:  {len(sections['concepts'])}")
    click.echo(f"  Outputs:   {len(sections['outputs'])}")

    (wiki_dir / "index.md").write_text(_build_index(sections, cfg), encoding="utf-8")

    categories_dir = wiki_dir / "categories"
    categories_dir.mkdir(parents=True, exist_ok=True)
    for path in categories_dir.glob("*.md"):
        if _is_generated_category_page(path):
            path.unlink()
    for group in sections.get("groups", []):
        out_path = categories_dir / f"{group['slug']}.md"
        out_path.write_text(_build_category_page(group, wiki_dir), encoding="utf-8")

    concept_lines = ["# 全部概念", "", "按主题浏览跨文档结论；具体 API 参数请核对 raw 原文。", ""]
    for item in sections["concepts"]:
        concept_lines.append(f"- [{item['title']}](../{item['path']})")
    concept_lines.extend(["", "*Generated by `kb index`.*"])
    (categories_dir / "concepts.md").write_text("\n".join(concept_lines), encoding="utf-8")

    try:
        from .search_engine import SearchEngine

        engine = SearchEngine(Path(cfg["paths"]["search_db"]))
        raw_dir = Path(cfg["paths"]["raw_dir"])
        engine.index(wiki_dir, raw_dir)
        click.echo("  -> search cache updated.")
    except Exception as exc:
        click.echo(f"  [warn] search cache not updated: {exc}", err=True)

    click.echo("  -> wiki/index.md updated.")
