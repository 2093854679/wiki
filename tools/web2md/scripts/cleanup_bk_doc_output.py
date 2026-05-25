#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Remove non-Markdown, non-image artifacts from the BK_IDK mirror."""

from __future__ import annotations

import argparse
from pathlib import Path


KEEP_IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp", ".ico"}
DEFAULT_ROOT = Path(r"D:\Desktop\obsidian\raw\bk_doc\bk_idk")


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

    removed_files, removed_dirs = prune(args.root)
    print(f"pruned_files={removed_files} pruned_dirs={removed_dirs}")


if __name__ == "__main__":
    main()
