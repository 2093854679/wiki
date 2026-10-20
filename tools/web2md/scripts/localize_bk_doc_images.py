#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Download images referenced by mirrored Beken Markdown files and rewrite links local."""

from __future__ import annotations

import re
import argparse
from pathlib import Path
from urllib.parse import urlparse, unquote

import requests

DEFAULT_ROOT = Path(r"D:\Desktop\obsidian\raw\beken\bk_idk")
DEFAULT_REFERER = "https://docs.bekencorp.com/arminodoc/chipchoose/?dk=BK_IDK&lan=zh"
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\((https://docs\.bekencorp\.com/[^)]+?\.(?:png|jpg|jpeg|gif|svg|webp))\)", re.I)
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"
CHALLENGE_URL = "https://docs.bekencorp.com/arminodoc/chipchoose/?dk=BK_IDK&lan=zh"
KEEP_IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp", ".ico"}


def safe_name(url: str) -> str:
    parsed = urlparse(url)
    return unquote(Path(parsed.path).name)


def relpath(from_file: Path, to_file: Path) -> str:
    import os

    return os.path.relpath(to_file, from_file.parent).replace("\\", "/")


def prune_non_markdown_and_images(root: Path) -> tuple[int, int]:
    removed_files = 0
    removed_dirs = 0

    for path in sorted(root.rglob("*"), reverse=True):
        if path.is_file():
            if path.suffix.lower() == ".md" or path.suffix.lower() in KEEP_IMAGE_SUFFIXES:
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


def safeline_calc(values: list[int]) -> list[int]:
    t = 1
    n = sum(values)
    r = (6 + len(values) + n) % 6 + 6
    for _ in range(r):
        t *= 6
    if t < 6666:
        t *= len(values)
    if t > 0x3F940AA:
        t //= len(values)
    for idx, value in enumerate(values):
        t += value**3
        t ^= idx
        t ^= value + idx
    out = []
    while t > 0:
        out.insert(0, 63 & t)
        t >>= 6
    return out


def post_challenge_json(session: requests.Session, url: str, payload: dict) -> dict:
    last_error: Exception | None = None
    for attempt in range(4):
        try:
            return session.post(url, json=payload, timeout=60).json()
        except requests.RequestException as exc:
            last_error = exc
            import time

            time.sleep(2 * (attempt + 1))
    if last_error:
        raise last_error
    raise RuntimeError("challenge request failed")


def refresh_safeline_cookie(session: requests.Session, visitor_id: str) -> None:
    issue = post_challenge_json(
        session,
        "https://challenge.rivers.chaitin.cn/challenge/v2/api/issue",
        {"client_id": "424b5f37a1df48d1971652925e47ee2e_0", "level": 1},
    )
    verify = post_challenge_json(
        session,
        "https://challenge.rivers.chaitin.cn/challenge/v2/api/verify",
        {
            "issue_id": issue["data"]["issue_id"],
            "result": safeline_calc(issue["data"]["data"]),
            "serials": [],
            "client": {
                "userAgent": USER_AGENT,
                "platform": "Win32",
                "language": "zh-CN,en-US",
                "vendor": "Google Inc.",
                "screen": [1920, 1080],
                "visitorId": visitor_id,
                "score": 100,
                "target": 100,
            },
        },
    )
    session.cookies.set("sl-challenge-server", "cloud", domain="docs.bekencorp.com", path="/")
    session.cookies.set("sl-challenge-jwt", verify["data"]["jwt"], domain="docs.bekencorp.com", path="/")


def main() -> None:
    global ROOT
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--referer", default=DEFAULT_REFERER)
    parser.add_argument("--timeout", type=int, default=30)
    args = parser.parse_args()
    ROOT = args.root
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Referer": args.referer})
    cookie_ready = False
    downloaded = 0
    rewritten = 0
    failed = 0

    doc_roots = [ROOT] + sorted(p for p in ROOT.iterdir() if p.is_dir())
    for chip_dir in doc_roots:
        image_dir = chip_dir / "_images"
        image_dir.mkdir(parents=True, exist_ok=True)

        md_files = chip_dir.glob("*.md") if chip_dir == ROOT else chip_dir.rglob("*.md")
        for md_file in md_files:
            text = md_file.read_text(encoding="utf-8")
            changed = False

            def repl(match: re.Match[str]) -> str:
                nonlocal downloaded, rewritten, failed, changed
                alt, url = match.group(1), match.group(2)
                out = image_dir / safe_name(url)
                if not out.exists():
                    try:
                        nonlocal cookie_ready
                        if not cookie_ready:
                            refresh_safeline_cookie(session, "web2md-bk-doc-images")
                            cookie_ready = True
                        response = session.get(url, timeout=args.timeout)
                        if response.status_code == 468:
                            refresh_safeline_cookie(session, "web2md-bk-doc-images")
                            cookie_ready = True
                            response = session.get(url, timeout=args.timeout)
                        if response.status_code >= 400:
                            failed += 1
                            return match.group(0)
                        out.write_bytes(response.content)
                        downloaded += 1
                    except Exception:
                        failed += 1
                        return match.group(0)
                changed = True
                rewritten += 1
                return f"![{alt}]({relpath(md_file, out)})"

            new_text = IMAGE_RE.sub(repl, text)
            if changed:
                md_file.write_text(new_text, encoding="utf-8")

    removed_files, removed_dirs = prune_non_markdown_and_images(ROOT)
    print(f"downloaded={downloaded} rewritten={rewritten} failed={failed}")
    print(f"pruned_files={removed_files} pruned_dirs={removed_dirs}")


if __name__ == "__main__":
    main()
