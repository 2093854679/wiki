"""Render outputs: apply Jinja2 templates, generate Marp slides, matplotlib charts."""

import subprocess
import tempfile
from pathlib import Path

import click
from jinja2 import Environment, FileSystemLoader

from .llm import get_config


def render_template(template_name: str, data: dict, cfg: dict) -> str:
    """Render a Jinja2 template with the given data."""
    templates_dir = Path(cfg["paths"]["templates_dir"])
    if not templates_dir.exists():
        raise FileNotFoundError(f"Templates directory not found: {templates_dir}")
    env = Environment(loader=FileSystemLoader(str(templates_dir)))
    tpl = env.get_template(template_name)
    return tpl.render(**data)


@click.command("render")
@click.argument("template")
@click.option("--data", "-d", "data_file", help="JSON or YAML file with template data")
@click.option("--output", "-o", "output_file", help="Output file path")
@click.option("--inline", "-i", "inline_data", help="Inline JSON data string")
def cmd_render(template, data_file, output_file, inline_data):
    """Render a template with data."""
    import json
    cfg = get_config()

    if data_file:
        dp = Path(data_file)
        if dp.suffix in (".yaml", ".yml"):
            import yaml
            data = yaml.safe_load(dp.read_text(encoding="utf-8-sig"))
        else:
            data = json.loads(dp.read_text(encoding="utf-8-sig"))
    elif inline_data:
        data = json.loads(inline_data)
    else:
        data = {}

    result = render_template(template, data, cfg)

    if output_file:
        Path(output_file).write_text(result, encoding="utf-8")
        click.echo(f"Rendered to {output_file}")
    else:
        click.echo(result)
