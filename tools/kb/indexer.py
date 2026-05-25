"""Auto-generate wiki indexes with raw-source category grouping."""

from __future__ import annotations

from pathlib import Path
import re
import unicodedata

import click
from jinja2 import Environment, FileSystemLoader
import yaml

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
    try:
        text = filepath.read_text(encoding="utf-8")
        return re.findall(r"\[\[([^\]]+)\]\]", text)
    except Exception:
        return []


def _frontmatter_from_md(filepath: Path) -> dict:
    """Parse optional YAML frontmatter from a markdown file."""
    try:
        text = filepath.read_text(encoding="utf-8")
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
        for line in filepath.read_text(encoding="utf-8").splitlines():
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
        if source_root.lower() == "study_note":
            return "Study_Note"
        if source_root.lower() == "bk_doc":
            return "bk_doc"
        if source_root in {"智能桌面萌宠项目笔记", "desktop-pet"}:
            return "智能桌面萌宠项目笔记"
        return source_root

    raw_path = source.replace("\\", "/")
    idx = raw_path.lower().find("raw/")
    if idx >= 0:
        rel = raw_path[idx + 4 :]
        parts = [p for p in rel.split("/") if p]
        if parts:
            return parts[0]

    hint = f"{title} {(md_path.stem if md_path else '')} {source}".lower()
    if any(token in hint for token in ["bk723", "bk_doc", "cli_api", "armino"]):
        return "bk_doc"
    if any(token in hint for token in ["desktop-pet", "宠物", "萌宠"]):
        return "智能桌面萌宠项目笔记"
    if any(token in hint for token in ["interview", "task-development", "study_note", "study note", "面试", "task"]):
        return "Study_Note"

    parts = [p for p in raw_path.split("/") if p]
    category = parts[0] if parts else "Other"
    if category.lower() == "study_note":
        return "Study_Note"
    if category.lower() == "bk_doc":
        return "bk_doc"
    return category


def _pretty_category_name(category: str) -> str:
    """Human-friendly display name for a raw category."""
    mapping = {
        "bk_doc": "BK Docs",
        "Study_Note": "Study Note",
        "智能桌面萌宠项目笔记": "Desktop Pet",
        "Other": "Other",
    }
    return mapping.get(category, category)


def _category_slug(category: str) -> str:
    """Stable filename for a category hub page."""
    explicit = {
        "bk_doc": "bk-doc",
        "Study_Note": "study-note",
        "智能桌面萌宠项目笔记": "desktop-pet",
    }
    if category in explicit:
        return explicit[category]
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
                lines.append("## 芯片导航")
                lines.append("")
                for chip in chips:
                    stem = chip.stem
                    label = {"bk7235": "BK7235 (第一代)", "bk7236": "BK7236 (第二代)", "bk7236n": "BK7236N (增强版)", "bk7239": "BK7239 (旗舰)", "matter": "BK Matter (Matter协议)"}.get(stem, stem.upper())
                    lines.append(f"- **[{label}](bk-doc/{stem})**")
                lines.append("")
                lines.append("点击芯片查看完整的模块索引、摘要列表和原始文档链接。")
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


def _scan_wiki(wiki_dir: Path) -> dict:
    """Scan wiki directory and return structured data."""
    sections = {"summaries": [], "concepts": [], "outputs": [], "other": []}
    source_categories: dict[str, list[dict]] = {}

    for md in sorted(wiki_dir.rglob("*.md")):
        rel = str(md.relative_to(wiki_dir)).replace("\\", "/")
        if rel == "index.md" or rel.startswith("categories/"):
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
    sections["groups"] = grouped
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
        f"*Auto-generated index of {len(sections['summaries']) + len(sections['concepts']) + len(sections['outputs']) + len(sections['other'])} articles.*",
        "",
    ]

    groups = sections.get("groups", [])
    if groups:
        lines.append("## Raw Categories")
        lines.append("")
        for group in groups:
            lines.append(f"### [{group['display_name']}](categories/{group['slug']}.md) ({len(group['items'])})")
            lines.append("")
            preview = group["items"][:5]
            for item in preview:
                link = f"[{item['title']}]({item['path']})"
                if item["tldr"]:
                    lines.append(f"- {link} - {item['tldr']}")
                else:
                    lines.append(f"- {link}")
            if len(group["items"]) > len(preview):
                lines.append(f"- ... and {len(group['items']) - len(preview)} more")
            lines.append("")

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
                lines.append(f"- {link} - {item['tldr']}")
            else:
                lines.append(f"- {link}")
        lines.append("")

    lines.append("## Backlink Graph")
    lines.append("")
    all_articles: dict[str, set[str]] = {}
    for items in sections.values():
        if isinstance(items, list):
            for item in items:
                all_articles[item["title"]] = set()

    for items in sections.values():
        if isinstance(items, list):
            for item in items:
                for bl in item["backlinks"]:
                    if bl in all_articles:
                        all_articles[bl].add(item["title"])

    for title, linked_from in sorted(all_articles.items()):
        if linked_from:
            lines.append(f"- [[{title}]] - referenced by: {', '.join(sorted(linked_from)[:5])}")
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
    total = len(sections["summaries"]) + len(sections["concepts"]) + len(sections["outputs"]) + len(sections["other"])

    click.echo(f"Indexing {total} articles...")
    click.echo(f"  Summaries: {len(sections['summaries'])}")
    click.echo(f"  Concepts:  {len(sections['concepts'])}")
    click.echo(f"  Outputs:   {len(sections['outputs'])}")

    (wiki_dir / "index.md").write_text(_build_index(sections, cfg), encoding="utf-8")

    categories_dir = wiki_dir / "categories"
    categories_dir.mkdir(parents=True, exist_ok=True)
    for path in categories_dir.glob("*.md"):
        path.unlink()
    for group in sections.get("groups", []):
        out_path = categories_dir / f"{group['slug']}.md"
        out_path.write_text(_build_category_page(group, wiki_dir), encoding="utf-8")

    try:
        from .search_engine import SearchEngine

        engine = SearchEngine(Path(cfg["paths"]["search_db"]))
        engine.index(wiki_dir)
        click.echo("  -> search cache updated.")
    except Exception as exc:
        click.echo(f"  [warn] search cache not updated: {exc}", err=True)

    click.echo("  -> wiki/index.md updated.")
