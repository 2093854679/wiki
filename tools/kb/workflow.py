"""Convenience workflows for the kb CLI."""

from __future__ import annotations

from pathlib import Path

import click

from .graph_health import analyze_graph_health, _format_report
from .indexer import cmd_index
from .ingest import _load_manifest, scan_raw
from .llm import get_config


@click.command("refresh")
def cmd_refresh():
    """Run the usual local maintenance pass without calling an external LLM."""
    cfg = get_config()
    raw_dir = Path(cfg["paths"]["raw_dir"])
    manifest = _load_manifest(Path(cfg["paths"]["manifest_file"]))
    files = scan_raw(raw_dir, manifest) if raw_dir.exists() else []
    status_counts = {"new": 0, "changed": 0, "unchanged": 0}
    for item in files:
        status_counts[item["status"]] = status_counts.get(item["status"], 0) + 1

    click.echo("Raw scan")
    click.echo(f"  New:       {status_counts.get('new', 0)}")
    click.echo(f"  Changed:   {status_counts.get('changed', 0)}")
    click.echo(f"  Unchanged: {status_counts.get('unchanged', 0)}")
    click.echo("")

    cmd_index.callback()
    click.echo("")
    click.echo(_format_report(analyze_graph_health(cfg)))
