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
DEFAULT_ROOT = Path(r"D:\Desktop\obsidian\raw\bk_doc\bk_idk")
MARKDOWN_LINK_RE = re.compile(r"(\]\()([^)\s]+)(\s+\"[^\"]*\")?(\))")


def rewrite_markdown_links(text: str) -> str:
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

        lines.append(MARKDOWN_LINK_RE.sub(repl, line))

    return "".join(lines)


def clean_markdown(root: Path) -> tuple[int, int, int]:
    removed_site_pages = 0
    rewritten_files = 0
    removed_language_links = 0

    for path in sorted(root.rglob("*.md")):
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


def prune(root: Path) -> tuple[int, int]:
    removed_files = 0
    removed_dirs = 0

    for path in sorted(root.rglob("*"), reverse=True):
        if path.is_file():
            suffix = path.suffix.lower()
            if suffix == ".md" or suffix in KEEP_IMAGE_SUFFIXES:
                continue
            path.unlink()
            removed_files += 1

    for path in sorted((p for p in root.rglob("*") if p.is_dir()), reverse=True):
        try:
            next(path.iterdir())
        except StopIteration:
            path.rmdir()
            removed_dirs += 1

    return removed_files, removed_dirs


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    args = parser.parse_args()

    removed_site_pages, rewritten_files, removed_language_links = clean_markdown(args.root)
    removed_files, removed_dirs = prune(args.root)
    print(
        " ".join(
            [
                f"site_pages_removed={removed_site_pages}",
                f"md_files_rewritten={rewritten_files}",
                f"language_links_removed={removed_language_links}",
                f"pruned_files={removed_files}",
                f"pruned_dirs={removed_dirs}",
            ]
        )
    )


if __name__ == "__main__":
    main()
