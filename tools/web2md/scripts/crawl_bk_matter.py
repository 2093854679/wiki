#!/usr/bin/env python3
"""Crawl BK_Matter docs and save as markdown to raw/bk/bk_matter/."""

from __future__ import annotations

import re
import time
from collections import deque
from pathlib import Path
from urllib.parse import urldefrag, urljoin, urlparse

import requests
from bs4 import BeautifulSoup

from app.services.converter import ConverterService

ROOT_URL = "https://docs.bekencorp.com/arminodoc/bk_matter/matter/zh_CN/v2.0.1/"
ROOT_OUT = Path(r"D:\Desktop\obsidian\raw\bk\bk_matter")

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"
)


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


def discover_client_id(session: requests.Session, url: str) -> str:
    response = session.get(url, timeout=30)
    match = re.search(r"SafeLineChallenge\(\"([^\"]+)\"", response.text)
    if match:
        return match.group(1)
    return "424b5f37a1df48d1971652925e47ee2e_0"


def solve_safeline(session: requests.Session, url: str) -> str:
    client_id = discover_client_id(session, url)
    issue = session.post(
        "https://challenge.rivers.chaitin.cn/challenge/v2/api/issue",
        json={"client_id": client_id, "level": 1},
        timeout=30,
    ).json()
    result = safeline_calc(issue["data"]["data"])
    verify = session.post(
        "https://challenge.rivers.chaitin.cn/challenge/v2/api/verify",
        json={
            "issue_id": issue["data"]["issue_id"],
            "result": result,
            "serials": [],
            "client": {
                "userAgent": USER_AGENT,
                "platform": "Win32",
                "language": "zh-CN,en-US",
                "vendor": "Google Inc.",
                "screen": [1920, 1080],
                "visitorId": "web2md-bk-doc",
                "score": 100,
                "target": 100,
            },
        },
        timeout=30,
    ).json()
    return verify["data"]["jwt"]


def make_session(jwt: str | None = None) -> requests.Session:
    session = requests.Session()
    session.headers.update({
        "User-Agent": USER_AGENT,
        "Referer": "https://docs.bekencorp.com/arminodoc/chipchoose/?dk=BK_Matter&lan=zh",
    })
    if jwt:
        session.headers.update({"Cookie": f"sl-challenge-server=cloud; sl-challenge-jwt={jwt}"})
    return session


def page_to_md_path(out_dir: Path, root_url: str, page_url: str) -> Path:
    root_path = urlparse(root_url).path
    parsed = urlparse(page_url)
    rel = parsed.path.removeprefix(root_path).strip("/")
    if not rel:
        return out_dir / "index.md"
    if rel.endswith("/"):
        rel = rel.rstrip("/")
    if rel.endswith(".html"):
        rel = rel[:-5]
    # Flatten: a/b/c/index → a/b/c.md, sibling/ → sibling.md
    parts = rel.split("/")
    if parts[-1] == "index":
        del parts[-1]
    name = parts[-1]
    parent = out_dir / "/".join(parts[:-1])
    parent.mkdir(parents=True, exist_ok=True)
    return parent / f"{name}.md"


def extract_links(html: str, base_url: str, root_url: str) -> list[str]:
    links = []
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all(["a", "link", "script", "img"]):
        attr = "href" if tag.name in ("a", "link") else "src"
        value = tag.get(attr)
        if not value or value.startswith(("javascript:", "mailto:", "tel:", "#")):
            continue
        absolute = urldefrag(urljoin(base_url, value))[0]
        if absolute.startswith(root_url) and (
            absolute.endswith("/")
            or absolute.endswith(".html")
            or "." not in Path(urlparse(absolute).path).name
        ):
            links.append(absolute)
    return links


def main():
    raw_session = make_session()
    jwt = solve_safeline(raw_session, ROOT_URL)
    session = make_session(jwt)
    converter = ConverterService()
    ROOT_OUT.mkdir(parents=True, exist_ok=True)

    queue = deque([ROOT_URL])
    seen: set[str] = set()
    page_count = 0
    error_count = 0

    while queue:
        url = queue.popleft()
        if url in seen:
            continue
        seen.add(url)

        try:
            response = session.get(url, timeout=30)
            if response.status_code == 468:
                jwt = solve_safeline(make_session(), url)
                session = make_session(jwt)
                response = session.get(url, timeout=30)
            if response.status_code >= 400:
                print(f"  [ERR {response.status_code}] {url}")
                error_count += 1
                continue

            html = response.text
            markdown = converter.convert_to_markdown(html, url)["markdown"]
            out_file = page_to_md_path(ROOT_OUT, ROOT_URL, url)
            out_file.parent.mkdir(parents=True, exist_ok=True)
            out_file.write_text(markdown, encoding="utf-8")
            page_count += 1
            print(f"  [{page_count}] {out_file.relative_to(ROOT_OUT)}")

            for link in extract_links(html, url, ROOT_URL):
                if link not in seen:
                    queue.append(link)
            time.sleep(0.08)
        except Exception as e:
            print(f"  [ERR] {url}: {e}")
            error_count += 1

    print(f"\nDone: {page_count} pages, {error_count} errors")


if __name__ == "__main__":
    main()
