"""Shared LLM client wrapper. All modules use this for Anthropic API calls."""

import os
from pathlib import Path
import yaml
import anthropic


def _load_config():
    cfg_path = Path(__file__).resolve().parents[2] / "config.yaml"
    with open(cfg_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


_config = _load_config()


def get_client() -> anthropic.Anthropic:
    api_key = _config["llm"].get("api_key") or os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Set ANTHROPIC_API_KEY env var or api_key in config.yaml"
        )
    return anthropic.Anthropic(api_key=api_key)


def get_model() -> str:
    return _config["llm"]["model"]


def get_config():
    return _config


def complete(
    prompt: str,
    *,
    system: str = "",
    model: str | None = None,
    max_tokens: int | None = None,
    temperature: float | None = None,
) -> str:
    """Single-turn completion. Returns text response."""
    client = get_client()
    cfg = _config["llm"]
    msg = client.messages.create(
        model=model or cfg["model"],
        max_tokens=max_tokens or cfg["max_tokens"],
        temperature=temperature if temperature is not None else cfg["temperature"],
        system=system,
        messages=[{"role": "user", "content": prompt}],
    )
    return msg.content[0].text


def complete_with_context(
    prompt: str,
    documents: list[dict[str, str]],
    *,
    system: str = "",
    model: str | None = None,
    max_tokens: int | None = None,
) -> str:
    """Completion with multiple context documents interleaved."""
    client = get_client()
    cfg = _config["llm"]

    content = []
    for doc in documents:
        content.append({
            "type": "text",
            "text": f"<document path=\"{doc['path']}\">\n{doc['content']}\n</document>",
        })
    content.append({"type": "text", "text": prompt})

    msg = client.messages.create(
        model=model or cfg["model"],
        max_tokens=max_tokens or cfg["max_tokens"],
        temperature=cfg["temperature"],
        system=system,
        messages=[{"role": "user", "content": content}],
    )
    return msg.content[0].text


def chat(
    messages: list[dict],
    *,
    system: str = "",
    model: str | None = None,
    max_tokens: int | None = None,
) -> str:
    """Multi-turn conversation."""
    client = get_client()
    cfg = _config["llm"]
    msg = client.messages.create(
        model=model or cfg["model"],
        max_tokens=max_tokens or cfg["max_tokens"],
        temperature=cfg["temperature"],
        system=system,
        messages=messages,
    )
    return msg.content[0].text
