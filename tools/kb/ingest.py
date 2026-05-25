"""Scan and categorize documents in the raw/ directory."""

import json
import hashlib
from datetime import datetime, timezone
from pathlib import Path

import click

from .llm import get_config

MIME_MAP = {
    ".md": "markdown",
    ".txt": "text",
    ".pdf": "paper",
    ".png": "image",
    ".jpg": "image",
    ".jpeg": "image",
    ".gif": "image",
    ".svg": "image",
    ".webp": "image",
    ".py": "code",
    ".js": "code",
    ".ts": "code",
    ".json": "dataset",
    ".csv": "dataset",
    ".yaml": "config",
    ".yml": "config",
    ".ipynb": "notebook",
    ".html": "web",
    ".pptx": "slides",
    ".docx": "document",
}


def _file_hash(path: Path) -> str:
    """SHA256 hash of file contents."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _load_manifest(manifest_path: Path) -> dict:
    if manifest_path.exists():
        return json.loads(manifest_path.read_text(encoding="utf-8"))
    return {}


def _save_manifest(manifest_path: Path, manifest: dict):
    manifest_path.write_text(json.dumps(manifest, indent=2, encoding="utf-8"))


def scan_raw(raw_dir: Path, manifest: dict) -> list[dict]:
    """Scan raw/ and return list of file metadata, marking new/changed."""
    results = []
    for f in sorted(raw_dir.rglob("*")):
        if f.is_file() and not f.name.startswith("."):
            fhash = _file_hash(f)
            rel = str(f.relative_to(raw_dir)).replace("\\", "/")
            prev = manifest.get(rel, {})
            status = "new"
            if rel in manifest:
                status = "changed" if prev.get("hash") != fhash else "unchanged"

            results.append({
                "path": rel,
                "absolute_path": str(f),
                "type": MIME_MAP.get(f.suffix.lower(), "unknown"),
                "size": f.stat().st_size,
                "hash": fhash,
                "status": status,
                "last_compiled": prev.get("last_compiled"),
            })
    return results


@click.command("ingest")
@click.option("--status", "-s", type=click.Choice(["new", "changed", "unchanged", "all"]),
              default="all", help="Filter by file status")
@click.option("--type", "-t", "file_type", help="Filter by file type (markdown, paper, image, etc.)")
@click.option("--json-output", is_flag=True, help="Output as JSON")
def cmd_ingest(status, file_type, json_output):
    """Scan raw/ directory and list files by category and status."""
    cfg = get_config()
    raw_dir = Path(cfg["paths"]["raw_dir"])
    if not raw_dir.exists():
        click.echo(f"raw/ directory not found at {raw_dir.absolute()}")
        return

    manifest_path = Path(cfg["paths"]["manifest_file"])
    manifest = _load_manifest(manifest_path)
    files = scan_raw(raw_dir, manifest)

    if status != "all":
        files = [f for f in files if f["status"] == status]
    if file_type:
        files = [f for f in files if f["type"] == file_type]

    if json_output:
        click.echo(json.dumps(files, indent=2))
        return

    if not files:
        click.echo("No files found matching criteria.")
        return

    type_counts = {}
    status_counts = {"new": 0, "changed": 0, "unchanged": 0}
    for f in files:
        t = f["type"]
        type_counts[t] = type_counts.get(t, 0) + 1
        status_counts[f["status"]] = status_counts.get(f["status"], 0) + 1

    click.echo(f"\n{'='*60}")
    click.echo(f"  raw/ scan — {len(files)} files")
    click.echo(f"{'='*60}")
    click.echo(f"\nBy type:")
    for t, c in sorted(type_counts.items(), key=lambda x: -x[1]):
        click.echo(f"  {t:<15} {c:>4}")

    click.echo(f"\nBy status:")
    for s, c in status_counts.items():
        if c > 0:
            click.echo(f"  {s:<15} {c:>4}")

    new_or_changed = [f for f in files if f["status"] in ("new", "changed")]
    if new_or_changed:
        click.echo(f"\n{'─'*60}")
        click.echo(f"  Pending compilation: {len(new_or_changed)} files")
        click.echo(f"{'─'*60}")
        for f in new_or_changed:
            click.echo(f"  [{f['status']:>7}] {f['path']}  ({f['type']})")


@click.command("update-manifest")
@click.argument("file_path")
@click.argument("file_hash")
def cmd_update_manifest(file_path, file_hash):
    """Mark a raw file as compiled in the manifest."""
    cfg = get_config()
    manifest_path = Path(cfg["paths"]["manifest_file"])
    manifest = _load_manifest(manifest_path)
    manifest[file_path] = {
        "hash": file_hash,
        "last_compiled": datetime.now(timezone.utc).isoformat(),
    }
    _save_manifest(manifest_path, manifest)
