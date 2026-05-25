#!/usr/bin/env python3
"""Post-process BK_Matter docs: download images + flatten index.md structure."""

from __future__ import annotations

import os
import re
import shutil
import time
from pathlib import Path
from urllib.parse import unquote, urlparse

import requests

ROOT = Path(r"D:\Desktop\obsidian\raw\bk_doc\bk_matter")
IMAGE_DIR = ROOT / "_images"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\((https://docs\.bekencorp\.com/[^)]+?\.(?:png|jpg|jpeg|gif|svg|webp))\)", re.I)


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


def refresh_safeline(session: requests.Session) -> None:
    issue = session.post(
        "https://challenge.rivers.chaitin.cn/challenge/v2/api/issue",
        json={"client_id": "424b5f37a1df48d1971652925e47ee2e_0", "level": 1},
        timeout=30,
    ).json()
    verify = session.post(
        "https://challenge.rivers.chaitin.cn/challenge/v2/api/verify",
        json={
            "issue_id": issue["data"]["issue_id"],
            "result": safeline_calc(issue["data"]["data"]),
            "serials": [],
            "client": {
                "userAgent": USER_AGENT,
                "platform": "Win32",
                "language": "zh-CN,en-US",
                "vendor": "Google Inc.",
                "screen": [1920, 1080],
                "visitorId": "web2md-matter-post",
                "score": 100,
                "target": 100,
            },
        },
        timeout=30,
    ).json()
    session.cookies.set("sl-challenge-server", "cloud", domain="docs.bekencorp.com", path="/")
    session.cookies.set("sl-challenge-jwt", verify["data"]["jwt"], domain="docs.bekencorp.com", path="/")


def download_images() -> None:
    """Download all remote images and rewrite links to local paths."""
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT, "Referer": "https://docs.bekencorp.com/arminodoc/bk_matter/matter/zh_CN/v2.0.1/"})
    refresh_safeline(session)

    downloaded = 0
    failed = 0

    for md_file in sorted(ROOT.rglob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        changed = False

        def repl(match: re.Match[str]) -> str:
            nonlocal downloaded, failed, changed
            alt, url = match.group(1), match.group(2)
            fname = unquote(Path(urlparse(url).path).name)
            out = IMAGE_DIR / fname
            if not out.exists():
                try:
                    resp = session.get(url, timeout=30)
                    if resp.status_code == 468:
                        refresh_safeline(session)
                        resp = session.get(url, timeout=30)
                    if resp.status_code >= 400:
                        print(f"  [IMG ERR {resp.status_code}] {url}")
                        failed += 1
                        return match.group(0)
                    out.write_bytes(resp.content)
                    downloaded += 1
                    print(f"  [IMG OK] {fname}")
                except Exception as e:
                    print(f"  [IMG ERR] {url}: {e}")
                    failed += 1
                    return match.group(0)
            changed = True
            rel = f"../_images/{fname}"
            # Compute proper relative path from md file to image
            try:
                rel = os.path.relpath(str(out), str(md_file.parent)).replace("\\", "/")
            except Exception:
                pass
            return f"![{alt}]({rel})"

        new_text = IMAGE_RE.sub(repl, text)
        if changed:
            md_file.write_text(new_text, encoding="utf-8")

    print(f"Images: {downloaded} downloaded, {failed} failed")


def flatten_index_files() -> None:
    """Rename xxx/index.md to xxx.md and fix internal links."""
    moved = 0

    # Collect all index.md files except root
    index_files = sorted(ROOT.rglob("index.md"), key=lambda p: len(p.parts), reverse=True)

    # Map old path → new path
    path_map: dict[Path, Path] = {}

    for idx_file in index_files:
        if idx_file.parent == ROOT:
            continue  # Keep root index.md

        # e.g. matter-basic/index.md → matter-basic.md
        parent_dir = idx_file.parent
        new_name = parent_dir.name + ".md"
        new_path = parent_dir.parent / new_name

        # If destination exists, skip
        if new_path.exists():
            print(f"  [SKIP] {idx_file.relative_to(ROOT)} → {new_path.relative_to(ROOT)} (exists)")
            continue

        # Move file
        shutil.move(str(idx_file), str(new_path))
        path_map[idx_file] = new_path
        print(f"  [MV] {idx_file.relative_to(ROOT)} → {new_path.relative_to(ROOT)}")
        moved += 1

        # Remove empty directory
        try:
            next(parent_dir.iterdir())
        except StopIteration:
            parent_dir.rmdir()
            # Remove nested empty parents too
            for ancestor in parent_dir.parents:
                if ancestor == ROOT:
                    break
                try:
                    next(ancestor.iterdir())
                    break
                except StopIteration:
                    ancestor.rmdir()

    # Fix internal links in all markdown files
    for md_file in sorted(ROOT.rglob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        changed = False

        for old_path, new_path in path_map.items():
            old_rel = str(old_path.relative_to(ROOT)).replace("\\", "/")
            new_rel = str(new_path.relative_to(ROOT)).replace("\\", "/")

            # Fix [text](path) format
            for pattern in [f"]({old_rel})", f"]({old_rel.replace('.md', '.html')})"]:
                replacement = f"]({new_rel})"
                if pattern in text:
                    text = text.replace(pattern, replacement)
                    changed = True

            # Fix [text](../dir/index.md) patterns that crossed directories
            # After flattening, links like "../matter-tools/index.md" become "../matter-tools.md"
            for parent_old, parent_new in path_map.items():
                parent_old_rel = str(parent_old.relative_to(ROOT)).replace("\\", "/")
                parent_new_rel = str(parent_new.relative_to(ROOT)).replace("\\", "/")
                for pat in [f"]({parent_old_rel})", f"]({parent_old_rel.replace('.md', '.html')})"]:
                    if pat in text:
                        text = text.replace(pat, f"]({parent_new_rel})")
                        changed = True

        if changed:
            md_file.write_text(text, encoding="utf-8")

    print(f"Flatten: {moved} files moved")


def main() -> None:
    print("=== Downloading images ===")
    download_images()
    print("\n=== Flattening index.md files ===")
    flatten_index_files()
    print("\nDone.")


if __name__ == "__main__":
    main()
