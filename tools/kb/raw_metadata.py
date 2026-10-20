"""Heuristics for raw document metadata."""

from __future__ import annotations

import re
from pathlib import Path

import yaml


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
    meta = {}
    heading = ""
    if file_path.suffix.lower() == ".md":
        try:
            with file_path.open(encoding="utf-8-sig") as handle:
                text = handle.read(65536)
            if text.startswith("---\n"):
                end = text.find("\n---\n", 4)
                if 0 < end < 8192:
                    value = yaml.safe_load(text[4:end])
                    if isinstance(value, dict):
                        meta = value
                    text = text[end + 5:]
            match = re.search(r"^# (.+)$", text, re.M)
            if match:
                heading = match.group(1).strip()
        except (OSError, UnicodeError, yaml.YAMLError):
            pass
    chip = str(meta.get("chip") or _chip_from_path(file_path))

    if not chip:
        for part in parts:
            if CHIP_RE.fullmatch(part):
                chip = part.upper()
                break

    module = str(meta.get("module") or "")
    if not module and chip and chip in parts:
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

    for section in ("api-reference", "developer-guide", "examples", "projects", "get-started", "security", "os"):
        if not meta.get("module") and section in parts:
            tail = parts[parts.index(section) + 1:]
            module = tail[0] if len(tail) > 1 else section
            break
    if not module and len(parts) > 1:
        module = parts[-2] if len(parts) > 2 else parts[1]

    doc_type = _doc_type_from_path(file_path)
    title = heading or file_path.stem.replace("-", " ").replace("_", " ").strip().title()
    if doc_type == "api" and "api" not in title.lower():
        title = f"{title} API"
    aliases = {title, file_path.stem, file_path.stem.replace("_", " ")}
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

    processor = str(meta.get("processor") or ("AP" if "ap_doc" in parts else "CP" if "cp_doc" in parts else ""))
    sdk_family = str(meta.get("sdk_family") or (parts[1] if root == "beken" and len(parts) > 1 else ""))
    return {
        "path": rel,
        "root": root,
        "chip": chip,
        "chips": sorted(set(CHIP_RE.findall(chip.upper()))),
        "sdk_family": sdk_family,
        "sdk_version": str(meta.get("sdk_version") or ""),
        "processor": processor,
        "language": str(meta.get("language") or ""),
        "source_url": str(meta.get("source_url") or ""),
        "fetched_at": str(meta.get("fetched_at") or ""),
        "mirror_status": str(meta.get("mirror_status") or ""),
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
