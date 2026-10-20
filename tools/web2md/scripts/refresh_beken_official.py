"""Refresh the public Beken documentation using ordinary HTTPS requests.

Stage first, then explicitly publish validated Markdown and referenced assets.
No challenge solving, authentication, deletion, or JavaScript execution.
"""
from __future__ import annotations

import argparse
import concurrent.futures as futures
import hashlib
import json
import os
import re
import shutil
import threading
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from urllib.parse import quote, unquote, urldefrag, urljoin, urlsplit, urlunsplit

import requests
import yaml
from bs4 import BeautifulSoup
from markdownify import markdownify

HERE = Path(__file__).resolve().parent
STAMP = datetime.now(timezone.utc).isoformat()
HOSTS = {"docs.bekencorp.com", "dl.bekencorp.com"}
SKIP_NAMES = {"404", "search", "genindex", "py-modindex"}
ASSET_EXT = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp", ".pdf"}
LOCAL = threading.local()
LOCK = threading.Lock()
LAST_REQUEST = 0.0


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(path)


def canonical(url):
    p = urlsplit(url)
    path = quote(unquote(p.path), safe="/:@-._~!$&'()*+,;=")
    if path.endswith("/"):
        path += "index.html"
    return urlunsplit((p.scheme, p.netloc, path, "", ""))


def fetch(url, *, binary=False, refresh=False):
    global LAST_REQUEST
    if urlsplit(url).hostname not in HOSTS:
        return {"url": url, "error": "outside official documentation hosts"}
    cache = HERE / "http-cache" / (hashlib.sha256(url.encode()).hexdigest() + ".bin")
    meta = cache.with_suffix(".json")
    if not refresh and cache.exists() and meta.exists():
        result = json.loads(meta.read_text(encoding="utf-8"))
        result["body"] = cache.read_bytes()
        return result
    if not hasattr(LOCAL, "session"):
        LOCAL.session = requests.Session()
        LOCAL.session.headers.update({"User-Agent": "Beken-KnowledgeBase-Mirror/1.0 (public documentation refresh)", "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.5"})
    for attempt in range(3):
        try:
            # Global limit: at most eight request starts per second.
            with LOCK:
                delay = max(0, LAST_REQUEST + .125 - time.monotonic())
                if delay:
                    time.sleep(delay)
                LAST_REQUEST = time.monotonic()
            with LOCAL.session.get(url, timeout=(10, 40), stream=True) as response:
                if response.status_code in {429, 500, 502, 503, 504} and attempt < 2:
                    time.sleep(min(30, int(response.headers.get("Retry-After", 2 ** (attempt + 1)))))
                    continue
                result = {"url": url, "final_url": response.url, "status": response.status_code, "content_type": response.headers.get("Content-Type", ""), "fetched_at": STAMP}
                if response.status_code != 200:
                    return result | {"error": f"HTTP {response.status_code}"}
                if urlsplit(response.url).hostname not in HOSTS:
                    return result | {"error": "redirect outside documentation hosts"}
                chunks, size = [], 0
                for chunk in response.iter_content(1024 * 128):
                    size += len(chunk)
                    if size > 50 * 1024 * 1024:
                        return result | {"error": "attachment exceeds 50 MiB; official link retained"}
                    chunks.append(chunk)
                body = b"".join(chunks)
                if not binary and (b"SafeLineChallenge" in body or b"captcha" in body[:5000].lower()):
                    return result | {"error": "access challenge; not bypassed"}
                cache.parent.mkdir(parents=True, exist_ok=True)
                cache.write_bytes(body)
                write_json(meta, result)
                return result | {"body": body}
        except requests.RequestException as exc:
            if attempt < 2:
                time.sleep(attempt + 1)
            else:
                return {"url": url, "error": str(exc)}
    return {"url": url, "error": "retry limit reached"}


def load_catalog():
    config = HERE / "roots.json"
    if not config.exists():
        config = Path(__file__).with_name("beken_official_roots.json")
    return json.loads(config.read_text(encoding="utf-8"))


def page_path(root, url):
    base = root["url"]
    rel = unquote(urlsplit(url).path[len(urlsplit(base).path):]).strip("/")
    if not rel or rel == "index.html":
        return PurePosixPath(root["root_file"])
    path = PurePosixPath(rel)
    if ".." in path.parts or any(":" in x for x in path.parts):
        raise ValueError("unsafe relative path")
    if path.name == "index.html":
        path = path.parent.with_suffix(".md")
    else:
        path = path.with_suffix(".md")
    return PurePosixPath(root["out_dir"]) / path


def matched_root(url, roots):
    return next((r for r in sorted(roots, key=lambda x: -len(x["url"])) if url.startswith(r["url"])), None)


def asset_path(url):
    p = urlsplit(url)
    suffix = PurePosixPath(p.path).suffix.lower()
    basename = re.sub(r"[^\w.-]+", "-", unquote(PurePosixPath(p.path).stem))[:55]
    return PurePosixPath("beken/_assets") / (hashlib.sha256(url.encode()).hexdigest()[:20] + "-" + basename + suffix)


def local_link(target, source_path):
    return quote(os.path.relpath(str(target), str(source_path.parent)).replace("\\", "/"), safe="/._-~")


def inventory(root):
    result = fetch(root["url"] + "searchindex.js")
    names = []
    if "body" in result:
        text = result["body"].decode("utf-8", errors="replace")
        match = re.search(r'["\']?docnames["\']?\s*:\s*', text)
        if match:
            try:
                names = json.JSONDecoder().raw_decode(text[match.end():])[0]
            except (ValueError, TypeError):
                pass
    urls = {canonical(root["url"])}
    for name in names:
        if isinstance(name, str) and name not in SKIP_NAMES and ".." not in PurePosixPath(name).parts:
            urls.add(canonical(urljoin(root["url"], name + ".html")))
    return {"id": root["id"], "url": root["url"], "searchindex_status": result.get("status"), "searchindex_error": result.get("error"), "urls": sorted(urls)}


def convert(root, url, response, roots):
    soup = BeautifulSoup(response["body"], "lxml")
    body = soup.select_one('[itemprop="articleBody"]') or soup.select_one("article") or soup.select_one('[role="main"]') or soup.select_one("main") or soup.select_one(".rst-content .document")
    if body is None:
        return {"url": url, "root_id": root["id"], "error": "no documentation article body; not published"}
    if not body.get_text(" ", strip=True):
        return {"url": url, "root_id": root["id"], "error": "empty documentation article"}
    path = page_path(root, url)
    title_tag = body.select_one("h1")
    if title_tag:
        title = title_tag.get_text(" ", strip=True).replace("\uf0c1", "").replace("¶", "").strip()
    else:
        title = soup.title.get_text(" ", strip=True).split("—")[0] if soup.title else PurePosixPath(path).stem
    discovered, assets, external, references = set(), {}, set(), {}
    for a in soup.select("a[href]"):
        absolute = canonical(urljoin(url, a["href"]))
        if absolute.startswith(root["url"]) and urlsplit(absolute).path.endswith(".html"):
            if PurePosixPath(urlsplit(absolute).path).stem not in SKIP_NAMES:
                discovered.add(absolute)
    for tag in body.select("a.headerlink,script,style,.articleComments,.feedback,.rst-footer-buttons"):
        tag.decompose()
    for a in list(body.select("a[href]")):
        if a.get_text(" ", strip=True) in {"[English]", "English", "[中文]"}:
            parent = a.parent
            a.decompose()
            if parent and not parent.get_text(strip=True):
                parent.decompose()
    for tag in body.select("a[href],img[src],source[src]"):
        attr = "href" if tag.name == "a" else "src"
        old = tag.get(attr, "")
        if not old or old.startswith(("#", "data:", "mailto:", "javascript:", "tel:")):
            if old.startswith("javascript:"):
                tag.attrs.pop(attr, None)
            continue
        absolute, fragment = urldefrag(urljoin(url, old))
        absolute = urlunsplit(urlsplit(absolute)._replace(query=""))
        target_root = matched_root(absolute, roots)
        ext = PurePosixPath(urlsplit(absolute).path).suffix.lower()
        if ext in ASSET_EXT and urlsplit(absolute).hostname in HOSTS:
            target = asset_path(absolute)
            assets[absolute] = target.as_posix()
            tag[attr] = local_link(target, path)
            references[tag[attr]] = {"path": target.as_posix(), "url": absolute}
        elif target_root and (ext == ".html" or absolute.endswith("/")):
            if PurePosixPath(urlsplit(absolute).path).stem in SKIP_NAMES:
                tag[attr] = absolute
            else:
                target = page_path(target_root, canonical(absolute))
                tag[attr] = local_link(target, path) + ("#" + fragment if fragment else "")
                references[tag[attr]] = {"path": target.as_posix(), "url": absolute + ("#" + fragment if fragment else "")}
                if target_root["id"] == root["id"]:
                    discovered.add(canonical(absolute))
        else:
            tag[attr] = absolute + ("#" + fragment if fragment else "")
            if urlsplit(absolute).hostname in HOSTS:
                external.add(absolute)
    # Preserve Sphinx anchor IDs, since rewritten links keep original fragments.
    anchors = {}
    for tag in body.select("[id]"):
        ident = tag.get("id", "")
        if ident and tag.name not in {"img", "a"}:
            token = "BEKENANCHOR" + hashlib.sha256(ident.encode()).hexdigest()[:20] + "END"
            anchors[token] = '<a id="' + ident.replace('"', '&quot;') + '"></a>'
            tag.insert_before(token + "\n\n")
    md = markdownify(str(body), heading_style="ATX", bullets="-", escape_misc=True, code_language_callback=lambda el: next((str(c)[len('highlight-'):] for c in el.get('class', []) if str(c).startswith('highlight-')), None), keep_inline_images_in=["td", "th"])
    md = re.sub(r"\n{4,}", "\n\n\n", md).strip()
    for token, anchor in anchors.items():
        md = md.replace(token, anchor)
    if not re.search(r"^# ", md, re.M):
        md = "# " + title + "\n\n" + md
    # Some Sphinx home pages have an empty body TOC; retain actual sidebar routes.
    if len(md) < 1200:
        nav = []
        for a in soup.select(".wy-menu-vertical a[href]"):
            target = canonical(urljoin(url, a["href"]))
            label = a.get_text(" ", strip=True)
            if label and target in discovered and target != canonical(url):
                entry = f"- [{label}]({local_link(page_path(root,target), path)})"
                if entry not in nav:
                    nav.append(entry)
                    references[local_link(page_path(root, target), path)] = {"path": page_path(root, target).as_posix(), "url": target}
        if nav:
            md += "\n\n## 模块导航\n\n" + "\n".join(nav)
    metadata = {"type": "official-document", "source_url": url, "sdk_family": root["family"], "chip": root.get("chip", ""), "processor": root.get("processor", ""), "sdk_version": root.get("version", ""), "language": root.get("language", "zh_CN"), "fetched_at": response.get("fetched_at", STAMP), "mirror_status": "current"}
    text = "---\n" + yaml.safe_dump(metadata, allow_unicode=True, sort_keys=False) + "---\n\n" + md + "\n"
    stage = HERE / "stage" / "raw" / str(path)
    stage.parent.mkdir(parents=True, exist_ok=True)
    stage.write_text(text, encoding="utf-8", newline="\n")
    module = unquote(urlsplit(url).path[len(urlsplit(root["url"]).path):]).split("/", 1)[0]
    tier = "reference" if module in {"api-reference", "examples", "projects"} else "guide"
    return {"url": url, "root_id": root["id"], "path": path.as_posix(), "title": title, "module": module, "tier": tier, "sha256": hashlib.sha256(stage.read_bytes()).hexdigest(), "characters": len(md), "discovered": sorted(discovered), "assets": assets, "references": references, "external_document_links": sorted(external)}


def crawl(workers=6):
    roots = load_catalog()
    print(f"Inventory: {len(roots)} documentation roots", flush=True)
    with futures.ThreadPoolExecutor(max_workers=workers) as pool:
        inventories = list(pool.map(inventory, roots))
    write_json(HERE / "inventory.json", inventories)
    root_by_id = {r["id"]: r for r in roots}
    tasks = {(r["id"], u) for r in inventories for u in r["urls"]}
    print(f"Inventory pages: {len(tasks)}", flush=True)
    done, records, failures, assets = set(), [], [], {}
    with futures.ThreadPoolExecutor(max_workers=workers) as pool:
        while tasks:
            batch = sorted(tasks - done)
            tasks.clear()
            if not batch:
                break
            pending = {pool.submit(fetch, url): (rid, url) for rid, url in batch}
            for job in futures.as_completed(pending):
                rid, url = pending[job]
                done.add((rid, url))
                response = job.result()
                if "body" not in response:
                    failures.append(response | {"root_id": rid})
                else:
                    try:
                        row = convert(root_by_id[rid], url, response, roots)
                    except Exception as exc:
                        row = {"root_id": rid, "url": url, "error": f"convert: {type(exc).__name__}: {exc}"}
                    if row.get("error"):
                        failures.append(row)
                    else:
                        assets.update(row.pop("assets"))
                        tasks.update((rid, link) for link in row.pop("discovered") if (rid, link) not in done)
                        records.append(row)
                if len(done) % 100 == 0:
                    print(f"Pages completed: {len(done)}; usable: {len(records)}; failures: {len(failures)}", flush=True)
                    write_json(HERE / "progress.json", {"completed": len(done), "usable": len(records), "failures": len(failures), "asset_urls": len(assets), "per_root": dict(Counter(x["root_id"] for x in records))})
                    write_json(HERE / "pages.json", records)
                    write_json(HERE / "failures.json", failures)
                if len(done) + len(tasks) > 20000:
                    raise RuntimeError("unexpected inventory expansion; inspect scope")
        write_json(HERE / "pages.json", records)
        write_json(HERE / "failures.json", failures)
        print(f"Downloading {len(assets)} referenced images/PDFs", flush=True)
        asset_results = []
        jobs = {pool.submit(fetch, u, binary=True): (u, path) for u, path in assets.items()}
        for job in futures.as_completed(jobs):
            url, rel = jobs[job]
            response = job.result()
            row = {k: v for k, v in response.items() if k != "body"} | {"path": rel}
            if "body" in response:
                content_type = response.get("content_type", "")
                if "html" in content_type:
                    row["error"] = "HTML returned for image/PDF; not published"
                else:
                    dest = HERE / "stage/raw" / rel
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_bytes(response["body"])
                    row["bytes"] = len(response["body"])
                    row["sha256"] = hashlib.sha256(response["body"]).hexdigest()
            asset_results.append(row)
            if len(asset_results) % 200 == 0:
                print(f"Assets completed: {len(asset_results)}/{len(assets)}", flush=True)
        write_json(HERE / "assets.json", asset_results)
    # A failed download must retain a usable official link, not a broken local link.
    available = {r["path"] for r in records} | {a["path"] for a in asset_results if not a.get("error")}
    restored = 0
    for row in records:
        path = HERE / "stage/raw" / row["path"]
        text = path.read_text(encoding="utf-8")
        for relative, ref in row["references"].items():
            if ref["path"] not in available:
                text = re.sub(r'(\]\()' + re.escape(relative) + r'(?=[\s)])', lambda m: m.group(1) + ref["url"], text)
                restored += 1
        path.write_text(text, encoding="utf-8", newline="\n")
        row["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    write_json(HERE / "pages.json", records)
    summary = {"fetched_at": STAMP, "roots": len(roots), "pages": len(records), "page_failures": len(failures), "assets": len([a for a in asset_results if not a.get("error")]), "asset_failures": len([a for a in asset_results if a.get("error")]), "failed_local_links_restored_to_official_urls": restored, "per_root": dict(Counter(x["root_id"] for x in records))}
    write_json(HERE / "crawl-summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False), flush=True)


def publish(repo):
    repo = Path(repo).resolve()
    target_root = (repo / "raw/beken").resolve()
    records = json.loads((HERE / "pages.json").read_text(encoding="utf-8"))
    assets = json.loads((HERE / "assets.json").read_text(encoding="utf-8"))
    published, updated, unchanged = [], 0, 0
    for row in records + [a for a in assets if not a.get("error")]:
        rel = Path(row["path"])
        source = HERE / "stage/raw" / rel
        target = (repo / "raw" / rel).resolve()
        if not target.is_relative_to(target_root):
            raise RuntimeError(f"unsafe publish destination: {target}")
        if not source.is_file() or hashlib.sha256(source.read_bytes()).hexdigest() != row["sha256"]:
            raise RuntimeError(f"staged content missing or changed: {source}")
        if target.exists():
            if target.read_bytes() == source.read_bytes():
                unchanged += 1
                continue
            backup = HERE / "backups/raw" / rel
            backup.parent.mkdir(parents=True, exist_ok=True)
            if not backup.exists():
                shutil.copy2(target, backup)
            updated += 1
        target.parent.mkdir(parents=True, exist_ok=True)
        temp = target.with_suffix(target.suffix + ".refresh-tmp")
        shutil.copyfile(source, temp)
        os.replace(temp, target)
        published.append(row["path"])
    result = {"new": len(published) - updated, "updated": updated, "unchanged": unchanged, "files": published, "backup_dir": str(HERE / "backups")}
    write_json(HERE / "publish-summary.json", result)
    cache = repo / "tools/kb/cache/beken_official_sources.json"
    write_json(cache, {"fetched_at": STAMP, "catalog_source": "https://docs.bekencorp.com/", "roots": load_catalog(), "pages": records, "assets": assets})
    print(json.dumps({k:v for k,v in result.items() if k != "files"}, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["crawl", "publish"])
    parser.add_argument("--repo", default=r"D:\Desktop\obsidian")
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--work-dir", type=Path, help="Staging, logs and backups directory")
    args = parser.parse_args()
    if args.work_dir:
        HERE = args.work_dir.resolve()
    if args.mode == "crawl":
        crawl(args.workers)
    else:
        publish(args.repo)
