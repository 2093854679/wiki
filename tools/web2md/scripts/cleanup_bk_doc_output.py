#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Clean BK_IDK mirror output for wiki ingestion.

The crawler can leave Sphinx site artifacts in the Markdown mirror. Keep the
actual documents and images, remove generated search/index pages, and rewrite
local Markdown links away from stale .html targets.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


KEEP_IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp", ".ico"}
DROP_MARKDOWN_NAMES = {"genindex.md", "search.md"}
DEFAULT_ROOT = Path(r"D:\Desktop\obsidian\raw\beken\bk_idk")
MARKDOWN_LINK_RE = re.compile(r"(\]\()([^)\s]+)(\s+\"[^\"]*\")?(\))")
SPHINX_PERMALINK_RE = re.compile(r"\[\uf0c1(?:\]\(#[^)]+\))?|\uf0c1")


def is_excluded(path: Path, root: Path, excluded_dirs: set[str]) -> bool:
    if not excluded_dirs:
        return False
    try:
        rel = path.relative_to(root)
    except ValueError:
        return False
    return bool(rel.parts) and rel.parts[0] in excluded_dirs


def rewrite_markdown_links(text: str) -> str:
    text = text.lstrip("\ufeff")
    lines = []
    for line in text.splitlines(keepends=True):
        if "[[English]](" in line:
            continue
        if any(f"]({name}" in line.lower() for name in DROP_MARKDOWN_NAMES):
            continue

        def repl(match: re.Match[str]) -> str:
            prefix, target, title, suffix = match.groups()
            lower_target = target.lower()
            if (
                lower_target.startswith(("http://", "https://", "mailto:", "javascript:"))
                or lower_target.startswith("#")
                or ".html" not in lower_target
            ):
                return match.group(0)

            new_target = re.sub(r"\.html(?=($|#))", ".md", target, flags=re.I)
            new_title = re.sub(r"\.html", ".md", title or "", flags=re.I)
            return f"{prefix}{new_target}{new_title}{suffix}"

        cleaned = SPHINX_PERMALINK_RE.sub("", line)
        lines.append(MARKDOWN_LINK_RE.sub(repl, cleaned))

    return "".join(lines)


def clean_markdown(root: Path, excluded_dirs: set[str]) -> tuple[int, int, int]:
    removed_site_pages = 0
    rewritten_files = 0
    removed_language_links = 0

    for path in sorted(root.rglob("*.md")):
        if is_excluded(path, root, excluded_dirs):
            continue
        if path.name.lower() in DROP_MARKDOWN_NAMES:
            path.unlink()
            removed_site_pages += 1
            continue

        text = path.read_text(encoding="utf-8")
        removed_language_links += text.count("[[English]](")
        new_text = rewrite_markdown_links(text)
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            rewritten_files += 1

    return removed_site_pages, rewritten_files, removed_language_links


def prune(root: Path, excluded_dirs: set[str]) -> tuple[int, int]:
    removed_files = 0
    removed_dirs = 0

    for path in sorted(root.rglob("*"), reverse=True):
        if is_excluded(path, root, excluded_dirs):
            continue
        if path.is_file():
            suffix = path.suffix.lower()
            if suffix == ".md" or suffix in KEEP_IMAGE_SUFFIXES:
                continue
            path.unlink()
            removed_files += 1

    for path in sorted((p for p in root.rglob("*") if p.is_dir()), reverse=True):
        if is_excluded(path, root, excluded_dirs):
            continue
        try:
            next(path.iterdir())
        except StopIteration:
            path.rmdir()
            removed_dirs += 1

    return removed_files, removed_dirs


LINK_RE = re.compile(r'\[([^\]]*)\]\(([^)\s"]+)(\s*"[^"]*")?\)')

# Human-readable module names for chip hub nav generation
MODULE_NAMES = {
    'api-reference': 'API 参考',
    'developer-guide': '开发者指南',
    'examples': '示例',
    'get-started': '快速入门',
    'hw-reference': '硬件参考',
    'introduction': '概述',
    'os': '操作系统',
    'process': '开发流程',
    'application': '应用',
    'clounds': '云端',
    'cloud': '云端',
    'projects': '解决方案',
    'projects_work': '项目实战',
    'release-notes': '发布说明',
    'security': '安全',
    'boards': '开发板',
}


def enforce_hierarchy(root: Path, excluded_dirs: set[str]) -> tuple[int, int]:
    """Ensure the 总分 (overview + details) hierarchy is consistent.

    After crawling, the raw directory should have:
    - Every directory foo/ has a matching foo.md hub page at the same level
    - Every hub page's internal links point to the correct sub-directory paths
    - Chip root pages have module navigation linking to all sub-modules

    Returns (files_fixed, dirs_removed).
    """
    import os as _os
    fixed = 0

    # ── Pass 1: remove residual index.md ────────────────────────────
    for index_file in sorted(root.rglob("index.md")):
        if is_excluded(index_file, root, excluded_dirs):
            continue
        parent = index_file.parent
        if parent == root:
            continue
        hub = parent.parent / f"{parent.name}.md"
        if not hub.exists():
            index_file.rename(hub)
            print(f"  [flatten] {index_file.relative_to(root)} -> {hub.relative_to(root)}")
            fixed += 1
        else:
            index_file.unlink()
            print(f"  [dedup] {index_file.relative_to(root)}")

    # ── Pass 2: unstuck dir/dir.md recursively ──────────────────────
    while True:
        stuck_found = False
        for md_file in sorted(root.rglob("*.md")):
            if is_excluded(md_file, root, excluded_dirs):
                continue
            parent = md_file.parent
            if parent == root:
                continue
            if md_file.stem != parent.name:
                continue
            target = parent.parent / f"{parent.name}.md"
            if target.exists():
                md_file.unlink()
                print(f"  [dedup] {md_file.relative_to(root)}")
                stuck_found = True
                continue

            content = md_file.read_text(encoding='utf-8')
            changed = [False]

            def adjust_stuck(m):
                text, tgt, suffix = m.group(1), m.group(2), m.group(3) or ''
                if '/' in tgt or tgt.startswith(('#', '.')) or '://' in tgt:
                    return m.group(0)
                changed[0] = True
                return f'[{text}]({parent.name}/{tgt}{suffix})'

            new_content = LINK_RE.sub(adjust_stuck, content)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(new_content, encoding='utf-8')
            md_file.unlink()
            print(f"  [unstuck] {md_file.relative_to(root)} -> {target.relative_to(root)}")
            fixed += 1
            stuck_found = True

        if not stuck_found:
            break

    # ── Pass 3: fix hub page internal links ─────────────────────────
    # For every hub page foo.md (with sibling foo/ dir), ensure all
    # relative links that should point into foo/ actually do.
    links_fixed = 0
    for hub_file in sorted(root.rglob("*.md")):
        if is_excluded(hub_file, root, excluded_dirs):
            continue
        sibling_dir = hub_file.parent / hub_file.stem
        if not sibling_dir.is_dir():
            continue

        content = hub_file.read_text(encoding='utf-8')
        changed = [False]

        def fix_link(m):
            text, target, suffix = m.group(1), m.group(2), m.group(3) or ''
            if target.startswith('#') or '://' in target:
                return m.group(0)
            if target.startswith(hub_file.stem + '/'):
                return m.group(0)

            # Already resolves correctly from current location
            if (hub_file.parent / target).exists():
                return m.group(0)

            # Should point into sibling dir
            if (sibling_dir / target).exists():
                changed[0] = True
                return f'[{text}]({hub_file.stem}/{target}{suffix})'

            # Old stuck pattern: X/X.md where X.md was unstuck to sibling/
            parts = target.split('/')
            if len(parts) == 2 and parts[0] == parts[1].replace('.md', ''):
                flat = f"{parts[0]}.md"
                if (sibling_dir / flat).exists():
                    changed[0] = True
                    return f'[{text}]({hub_file.stem}/{flat}{suffix})'

            return m.group(0)

        new_content = LINK_RE.sub(fix_link, content)
        if changed[0]:
            hub_file.write_text(new_content, encoding='utf-8')
            links_fixed += 1

    if links_fixed:
        print(f"  [links] fixed internal links in {links_fixed} hub pages")
    fixed += links_fixed

    # ── Pass 4: add module nav to chip root pages ───────────────────
    nav_added = 0
    for chip_dir in sorted(p for p in root.iterdir() if p.is_dir() and not p.name.startswith('_')):
        if chip_dir.name in excluded_dirs:
            continue
        chip_md = chip_dir.parent / f"{chip_dir.name}.md"
        if not chip_md.exists():
            continue

        content = chip_md.read_text(encoding='utf-8')
        if '## 模块导航' in content:
            continue

        modules = []
        for item in sorted(chip_dir.iterdir()):
            if item.is_dir() and item.name != '_images':
                continue
            if item.suffix != '.md':
                continue
            name = MODULE_NAMES.get(item.stem, item.stem)
            modules.append((name, item.stem))

        if not modules:
            continue

        nav = '\n\n## 模块导航\n\n'
        prefix = f"{chip_dir.name}/"
        for name, fname in modules:
            nav += f'- [{name}]({prefix}{fname}.md)\n'

        # Remove any existing nav (in case of partial update)
        lines = content.split('\n')
        new_lines = []
        skip = False
        for line in lines:
            if line.strip() == '## 模块导航':
                skip = True
                continue
            if skip and line.startswith('## '):
                skip = False
                new_lines.append(line)
                continue
            if skip:
                continue
            new_lines.append(line)
        while new_lines and new_lines[-1].strip() == '':
            new_lines.pop()

        new_content = '\n'.join(new_lines) + nav + '\n'
        chip_md.write_text(new_content, encoding='utf-8')
        nav_added += 1

    if nav_added:
        print(f"  [nav] added module navigation to {nav_added} chip hubs")
    fixed += nav_added

    # ── Clean empty dirs ────────────────────────────────────────────
    dirs_removed = 0
    for dirpath in sorted((p for p in root.rglob("*") if p.is_dir()), reverse=True):
        if is_excluded(dirpath, root, excluded_dirs):
            continue
        try:
            next(dirpath.iterdir())
        except StopIteration:
            dirpath.rmdir()
            dirs_removed += 1

    return fixed, dirs_removed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--exclude-dir", action="append", default=[])
    args = parser.parse_args()
    excluded_dirs = set(args.exclude_dir)

    removed_site_pages, rewritten_files, removed_language_links = clean_markdown(args.root, excluded_dirs)
    hierarchy_fixed, hierarchy_dirs = enforce_hierarchy(args.root, excluded_dirs)
    removed_files, removed_dirs = prune(args.root, excluded_dirs)
    print(
        " ".join(
            [
                f"site_pages_removed={removed_site_pages}",
                f"md_files_rewritten={rewritten_files}",
                f"language_links_removed={removed_language_links}",
                f"hierarchy_fixed={hierarchy_fixed}",
                f"hierarchy_dirs_removed={hierarchy_dirs}",
                f"pruned_files={removed_files}",
                f"pruned_dirs={removed_dirs}",
            ]
        )
    )


if __name__ == "__main__":
    main()
