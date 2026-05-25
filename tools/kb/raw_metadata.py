"""Heuristics for raw document metadata."""

from __future__ import annotations

import re
from pathlib import Path


CHIP_RE = re.compile(r"BK\d{4}[A-Z]?", re.IGNORECASE)


def _normalize_token(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def _doc_type_from_path(path: Path) -> str:
    stem = path.stem.lower()
    parts = [p.lower() for p in path.parts]
    if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}:
        return "image"
    if stem in {"index", "genindex", "search", "wiki"}:
        return "hub"
    if "matter-tools" in parts or "tools" in parts:
        return "tool"
    if "get-started" in parts or stem in {"get-started", "overview", "introduction"}:
        return "guide"
    if "api-reference" in parts or any(tok in stem for tok in ["api", "driver", "hal"]):
        return "api"
    if "developer-guide" in parts or "projects" in parts or "examples" in parts:
        return "guide"
    return "doc"


def _chip_from_path(path: Path) -> str:
    for part in path.parts:
        match = CHIP_RE.fullmatch(part)
        if match:
            return match.group(0).upper()
    if path.stem.upper().startswith("BK") and CHIP_RE.match(path.stem):
        return path.stem.upper()
    return ""


def infer_raw_metadata(raw_root: Path, file_path: Path) -> dict:
    """Infer lightweight metadata for a raw document."""
    rel = file_path.relative_to(raw_root).as_posix()
    parts = [p for p in rel.split("/") if p]
    root = parts[0] if parts else "Other"
    chip = _chip_from_path(file_path)

    if not chip:
        for part in parts:
            if CHIP_RE.fullmatch(part):
                chip = part.upper()
                break

    module = ""
    if chip and chip in parts:
        idx = parts.index(chip)
        tail = parts[idx + 1 :]
        if tail:
            if tail[-1].lower().endswith(".md"):
                tail = tail[:-1]
            if tail:
                if tail[0] in {"api-reference", "developer-guide", "examples", "projects"} and len(tail) > 1:
                    module = tail[1]
                else:
                    module = tail[0]

    if not module and len(parts) > 1:
        module = parts[1]

    doc_type = _doc_type_from_path(file_path)
    title = file_path.stem.replace("-", " ").replace("_", " ").strip().title()
    if doc_type == "api" and "api" not in title.lower():
        title = f"{title} API"
    aliases = {title}
    if chip:
        aliases.update({chip, chip.lower()})
    if module:
        aliases.update({module, module.replace("-", " "), module.replace("_", " ")})
    if doc_type == "api":
        stem_alias = file_path.stem.replace("-", " ").replace("_", " ")
        aliases.update({
            f"{stem_alias} API",
            f"{file_path.stem} API",
        })
        if chip and module:
            aliases.update({
                f"{chip} {module} API",
                f"{chip} {stem_alias} API",
            })

    keywords = {
        root,
        doc_type,
        chip.lower() if chip else "",
        module.lower() if module else "",
        *(_normalize_token(p) for p in parts[-4:]),
    }
    keywords = {k for k in keywords if k}

    return {
        "path": rel,
        "root": root,
        "chip": chip,
        "module": module,
        "doc_type": doc_type,
        "title": title,
        "aliases": sorted(aliases),
        "keywords": sorted(keywords),
        "workspace_path": f"raw/{rel}",
    }


def metadata_index(raw_root: Path) -> dict[str, dict]:
    """Build metadata for every raw file."""
    index = {}
    for f in sorted(raw_root.rglob("*")):
        if f.is_file() and not f.name.startswith("."):
            index[f.relative_to(raw_root).as_posix()] = infer_raw_metadata(raw_root, f)
    return index
