#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Repair local Markdown links after Sphinx mirrors are flattened.

The BK doc cleanup step flattens many ``foo/index.md`` pages into ``foo.md``.
Sphinx-generated table-of-contents links can still point to the old shape.
This script rewrites only local links whose target file is missing and where a
nearby flattened target can be found.
"""

from __future__ import annotations

import argparse
import os
import re
from pathlib import Path, PurePosixPath


LINK_RE = re.compile(r"(!?)\[([^\]]*)\]\(([^)\n]+)\)")
EXTERNAL_PREFIXES = ("http://", "https://", "mailto:", "tel:", "javascript:", "data:")


def split_link_body(body: str) -> tuple[str, str]:
    body = body.strip()
    if body.startswith("<"):
        end = body.find(">")
        if end != -1:
            return body[1:end], body[end + 1 :]
    match = re.match(r"(\S+)(.*)", body, flags=re.S)
    if not match:
        return body, ""
    return match.group(1), match.group(2)


def split_fragment(target: str) -> tuple[str, str]:
    if "#" not in target:
        return target, ""
    path, fragment = target.split("#", 1)
    return path, "#" + fragment


def flatten_index_path(path: str) -> str | None:
    posix = PurePosixPath(path)
    if posix.name.lower() != "index.md" or len(posix.parts) < 2:
        return None
    return posix.parent.as_posix() + ".md"


def append_md_path(path: str) -> str | None:
    posix = PurePosixPath(path)
    if posix.suffix:
        return None
    return (posix.parent / f"{posix.name}.md").as_posix()


def exists_from(md_file: Path, path: str) -> bool:
    return (md_file.parent / path).exists()


def sibling_target(md_file: Path, path: str) -> str | None:
    sibling_dir = md_file.parent / md_file.stem
    if not sibling_dir.is_dir():
        return None
    if (sibling_dir / path).exists():
        return f"{md_file.stem}/{path}"
    return None


def relative_to_file(md_file: Path, target_file: Path) -> str:
    return os.path.relpath(target_file, md_file.parent).replace("\\", "/")


def root_mapped_target(md_file: Path, root: Path, path: str) -> str | None:
    parts = PurePosixPath(path).parts
    if "examples" in parts and "projects" in parts:
        idx = parts.index("projects")
        rest = list(parts[idx + 1 :])
        if rest:
            project_path = PurePosixPath(*rest).as_posix()
            flattened = flatten_index_path(project_path) or project_path
            for section in ("multimedia", "tflite_micro", "bluetooth", "lvgl"):
                candidate = root / "ap_doc" / "examples" / "projects" / section / flattened
                if candidate.exists():
                    return relative_to_file(md_file, candidate)
            candidate = root / "ap_doc" / "examples" / "projects" / flattened
            if candidate.exists():
                return relative_to_file(md_file, candidate)

    for marker in ("ap_doc", "cp_doc"):
        if marker not in parts:
            continue
        idx = parts.index(marker)
        rest = list(parts[idx + 1 :])
        if len(rest) >= 3 and rest[0] == "bk7259" and rest[1] == "zh_CN":
            rest = rest[3:]
        candidate = root.joinpath(marker, *rest)
        if candidate.exists():
            return relative_to_file(md_file, candidate)

    for marker, mapped in (("ap", "ap_doc"), ("cp", "cp_doc")):
        if len(parts) >= 4 and parts[0] == marker and parts[1] == "docs":
            rest = list(parts[4:]) if parts[2] == "bk7259" and parts[3] == "zh_CN" else []
            if rest:
                candidate = root.joinpath(mapped, *rest)
                if candidate.exists():
                    return relative_to_file(md_file, candidate)
    return None


def fewer_parent_candidates(path: str) -> list[str]:
    out = []
    current = path
    while current.startswith("../"):
        current = current[3:]
        out.append(current)
    return out


def choose_replacement(md_file: Path, root: Path, target: str) -> str | None:
    lower = target.lower()
    if lower.startswith(EXTERNAL_PREFIXES) or target.startswith("#"):
        return None

    path, fragment = split_fragment(target)
    if not path:
        return None

    if exists_from(md_file, path):
        return None

    candidates: list[str] = []
    flattened = flatten_index_path(path)
    if flattened:
        candidates.append(flattened)
    md_path = append_md_path(path)
    if md_path:
        candidates.append(md_path)
    candidates.append(path)
    for candidate in list(candidates):
        for fewer_parent in fewer_parent_candidates(candidate):
            if fewer_parent not in candidates:
                candidates.append(fewer_parent)

    for candidate in candidates:
        if exists_from(md_file, candidate):
            return candidate + fragment

    for candidate in candidates:
        mapped = root_mapped_target(md_file, root, candidate)
        if mapped:
            return mapped + fragment

    for candidate in candidates:
        sibling = sibling_target(md_file, candidate)
        if sibling:
            return sibling + fragment

    return None


def repair_file(path: Path, root: Path, write: bool) -> tuple[int, list[tuple[str, str]]]:
    text = path.read_text(encoding="utf-8")
    changes: list[tuple[str, str]] = []

    def repl(match: re.Match[str]) -> str:
        bang, label, body = match.groups()
        target, title = split_link_body(body)
        replacement = choose_replacement(path, root, target)
        if not replacement:
            return match.group(0)

        new_title = title
        if title:
            new_title = title.replace(target, replacement)
        changes.append((target, replacement))
        return f"{bang}[{label}]({replacement}{new_title})"

    new_text = LINK_RE.sub(repl, text)
    if write and new_text != text:
        path.write_text(new_text, encoding="utf-8")

    return len(changes), changes


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    files_changed = 0
    links_repaired = 0
    examples: list[tuple[str, str, str]] = []

    for path in sorted(args.root.rglob("*.md")):
        count, changes = repair_file(path, args.root, args.write)
        if count:
            files_changed += 1
            links_repaired += count
            for old, new in changes[:5]:
                if len(examples) < 50:
                    examples.append((path.relative_to(args.root).as_posix(), old, new))

    mode = "write" if args.write else "dry-run"
    print(f"mode={mode} files_changed={files_changed} links_repaired={links_repaired}")
    for src, old, new in examples:
        print(f"{src}: {old} -> {new}")


if __name__ == "__main__":
    main()
