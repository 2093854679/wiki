#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Mirror Beken BK_IDK docs as Markdown using web2md's ConverterService."""

from __future__ import annotations

import re
import time
from collections import deque
from pathlib import Path
from urllib.parse import urldefrag, urljoin, urlparse

import requests
from bs4 import BeautifulSoup

from app.services.converter import ConverterService


ROOT_OUT = Path(r"D:\Desktop\obsidian\raw\bk_doc\bk_idk")

CHIPS = {
    "BK7235": "https://docs.bekencorp.com/armino/bk7235/zh_CN/v1.5/",
    "BK7236": "https://docs.bekencorp.com/arminodoc/bk_idk/bk7236/zh_CN/v2.0.1/",
    "BK7236N": "https://docs.bekencorp.com/arminodoc/bk_idk/bk7236n/zh_CN/v2.2.1/",
    "BK7256": "https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/",
    "BK7258": "https://docs.bekencorp.com/arminodoc/bk_idk/bk7258/zh_CN/v2.0.1/",
    "BK7239": "https://docs.bekencorp.com/arminodoc/bk_idk/bk7239/zh_CN/v2.2.1/",
}

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
    session.headers.update(
        {
            "User-Agent": USER_AGENT,
            "Referer": "https://docs.bekencorp.com/arminodoc/chipchoose/?dk=BK_IDK&lan=zh",
        }
    )
    if jwt:
        session.headers.update({"Cookie": f"sl-challenge-server=cloud; sl-challenge-jwt={jwt}"})
    return session


def page_to_md_path(chip_dir: Path, root_url: str, page_url: str) -> Path:
    root_path = urlparse(root_url).path
    parsed = urlparse(page_url)
    rel = parsed.path.removeprefix(root_path).strip("/")
    if not rel:
        rel = "index.html"
    if rel.endswith("/"):
        rel += "index.html"
    if rel.endswith(".html"):
        rel = rel[:-5] + ".md"
    else:
        rel = rel + ".md"
    return chip_dir / rel


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


def crawl_chip(chip: str, root_url: str) -> dict[str, int]:
    raw_session = make_session()
    jwt = solve_safeline(raw_session, root_url)
    session = make_session(jwt)
    converter = ConverterService()
    chip_dir = ROOT_OUT / chip
    chip_dir.mkdir(parents=True, exist_ok=True)

    queue = deque([root_url])
    seen: set[str] = set()
    stats = {"pages": 0, "errors": 0}

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
                stats["errors"] += 1
                continue

            html = response.text
            markdown = converter.convert_to_markdown(html, url)["markdown"]
            out_file = page_to_md_path(chip_dir, root_url, url)
            out_file.parent.mkdir(parents=True, exist_ok=True)
            out_file.write_text(markdown, encoding="utf-8")
            stats["pages"] += 1

            for link in extract_links(html, url, root_url):
                if link not in seen:
                    queue.append(link)
            time.sleep(0.08)
        except Exception:
            stats["errors"] += 1

    return stats


def main() -> None:
    ROOT_OUT.mkdir(parents=True, exist_ok=True)
    for chip, root_url in CHIPS.items():
        stats = crawl_chip(chip, root_url)
        print(f"{chip}: {stats['pages']} markdown pages, {stats['errors']} errors")


if __name__ == "__main__":
    main()
