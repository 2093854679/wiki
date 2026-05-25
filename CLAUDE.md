# LLM Knowledge Base — Claude Code Integration

This vault is an LLM-powered knowledge base. Raw source documents live in `raw/`,
the compiled wiki lives in `wiki/`. Everything is managed via the `kb` CLI.

## Key directories

```
raw/
├── beken/                        # Beken (博通集成) chip docs
│   ├── bk_idk/                   # 6 chips: BK7235/7236/7236N/7239/7256/7258
│   │   └── <Chip>/               # Each chip follows 总分 hierarchy:
│   │       ├── api-reference.md   #   hub page (overview)
│   │       ├── api-reference/     #   sub-module dir (details)
│   │       │   ├── wifi.md        #     sub-hub page
│   │       │   ├── wifi/          #     leaf content dir
│   │       │   │   └── bk_wifi.md #       actual doc
│   │       │   └── ...
│   │       └── ...
│   └── bk_matter/                # Matter framework docs (same hierarchy)
├── Study_Note/                   # Study notes by topic (01-06 categories)
├── 智能桌面萌宠项目笔记/           # Desktop pet project notes
└── (future sources)              # e.g. esp/, papers/, etc.

wiki/
├── summaries/                    # Per-document summaries (Tier 2 only)
├── concepts/                     # Cross-cutting concept articles (Tier 3)
├── categories/                   # Auto-generated category hub pages
├── outputs/                      # Q&A answers, slides, charts
└── index.md                      # Master index (auto-generated)
```

## 总分 hierarchy convention (CRITICAL)

**Every directory `foo/` MUST have a matching `foo.md` hub page at the same level.**

This is enforced by `cleanup_bk_doc_output.py`. The convention applies to ALL raw
sources, not just Beken docs:

- `foo.md` = overview / hub page that links to everything under `foo/`
- `foo/` = sub-modules and detail pages
- Deep nesting OK: `a/b/c.md` hub with `a/b/c/` sub-dir
- No `index.md` files — flattened to parent directory name
- No `dir/dir.md` (hub page stuck inside its own directory)

## Adding a new source — the complete pipeline

### 1. Crawl

For Beken docs, use the specialized crawlers (they handle SafeLine auth):

```bash
python tools/web2md/scripts/bk_doc_to_md.py       # BK_IDK chips
python tools/web2md/scripts/crawl_bk_matter.py     # BK_Matter
```

For other sources, write a crawler that:
- Saves each page as `<name>.md` (NOT `index.md`)
- Uses the flatten convention: `a/b/index.html` → `a/b.md`

### 2. Cleanup (MANDATORY after every crawl)

```bash
python tools/web2md/scripts/cleanup_bk_doc_output.py [--root <path>]
```

This single command does everything:
1. Removes Sphinx artifacts (`genindex.md`, `search.md`)
2. Rewrites `.html` → `.md` in links
3. Removes `[[English]]` language switcher links
4. **Enforces 总分 hierarchy**:
   - Deletes residual `index.md` duplicates
   - Moves stuck `dir/dir.md` → `../dir.md` with link correction
   - Fixes all hub page internal links to point into sibling directories
   - Adds `## 模块导航` to chip root pages
5. Prunes non-markdown/image files and empty directories

```bash
# Optional: download external images to _images/
python tools/web2md/scripts/localize_bk_doc_images.py
```

### 3. Ingest into wiki

```
python -m tools.kb ingest --status new    # check new files
# → assess each against tier table
# → Tier 1 (API ref): update manifest only
# → Tier 2 (overview/guide): write summary to wiki/summaries/
# → Tier 3 (cross-cutting): write concept to wiki/concepts/
python -m tools.kb index                  # rebuild index
python -m tools.kb stats                  # confirm
```

`kb index` rebuilds the search cache over both `wiki/` and `raw/`. For Beken chip docs,
raw technical files are first-class searchable sources, not fallback material.

## Tiered strategy — NOT every raw file needs a summary

Raw files fall into three tiers:

| Tier | What | Action |
|------|------|--------|
| **1. API reference** | `bk_uart.md`, `bk_gpio.md` 等函数签名文档 | 不写摘要。芯片 hub 页已有导航链接，读 raw 原文即可 |
| **2. Overview / Guide** | `bk_overview.md`, `bk_wifi.md` 等架构级文档 | 写摘要。这些是高频入口，TLDR 有价值 |
| **3. Cross-cutting concepts** | 跨多篇 raw 才能理解的主题 | 写 concept。如安全体系、WiFi 架构、OTA 流程 |

## Auto-ingest rule

**Every time this conversation starts, or the user says "处理一下" / "有新内容" / "更新wiki" / "编译"**:

1. `python -m tools.kb ingest --status new` — check only genuinely new files
2. If new markdown files exist: assess each against the tier table above
   - Tier 1 (API ref): ensure linked from the appropriate chip hub page, then `python -m tools.kb update-manifest <path> <hash>`
   - Tier 2 (overview/guide): read, write summary to `wiki/summaries/`, update manifest
   - Tier 3 (cross-cutting): extract concepts to `wiki/concepts/`
3. If new module directories appear in raw: update the chip hub page navigation
4. `python -m tools.kb index` — rebuild index
5. `python -m tools.kb stats` — confirm

Never wait for the user to ask twice. The raw/ directory is the trigger — new content there means
the wiki needs updating. You are the LLM compiler, so do the compilation directly
(do NOT call `python -m tools.kb compile` — that requires an external API key; you ARE the LLM).

## Common workflows

### Answering a question against the wiki (CRITICAL)

Just answer the question! `wiki/index.md` will tell you what wiki articles are available.

**MUST follow the navigation hierarchy — DO NOT jump directly to raw files or use grep:**
1. Read `wiki/index.md` first — find relevant wiki articles (summaries + concepts)
2. If wiki doesn't cover it, walk the navigation: `wiki/categories/bk-doc.md` → chip hub page → module index → raw doc
3. For BK chip questions, the lookup path is: `categories/bk-doc.md` → chip hub → raw `beken/<chip>/<module>.md`

This hierarchy exists for a reason. Skipping it and grepping raw directly defeats the purpose of the navigation system.

### Search / retrieval behavior

- `python -m tools.kb search` searches both `wiki/` and `raw/`.
- Beken queries should surface raw chip docs directly when the question is technical.
- `python -m tools.kb query` may synthesize an answer from both wiki notes and raw technical docs.
- When citing technical details, prefer raw file paths for exactness and wiki wikilinks for synthesized concepts.

### Health check / Linting
Run `python -m tools.kb lint --check consistency|gaps|suggestions` to find:
- Inconsistent data across articles
- Missing topics or data gaps
- Interesting cross-connections for new articles

### Relationship graph

The Obsidian graph (`Ctrl+G`) shows the knowledge hierarchy. Config in `.obsidian/graph.json`:
- **Orange** = wiki content (`path:wiki`)
- **Blue-gray** = raw documents (`path:raw`)
- Images excluded (`-path:_images`)
- If nodes appear scattered, the 总分 hierarchy is broken — run `cleanup_bk_doc_output.py`

### Enhancing the wiki — the Karpathy loop

Every Q&A session should "add up" in the knowledge base. After answering a question:

1. **Write answer to `wiki/outputs/`** — always. This is the session log.
2. **If the answer is cross-document synthesis** → promote to `wiki/concepts/` (as `bk-wifi-ble-coexistence.md` was)
3. **Cross-links discovered** → Update `[[wikilinks]]` in relevant articles

This way queries never go to waste — the wiki grows with every question you ask.

## Wiki Conventions
- Use `[[wikilinks]]` for internal links (Obsidian format)
- Concept articles should have a `## Related` section with backlinks
- Summaries should use `> **Source:** [text](path)` format (not `[[wikilinks]]`) for indexer compatibility
- Every concept article needs a brief TLDR at the top

## Templates
Jinja2 templates in `tools/kb/templates/` define the structure for generated content.
Use `python -m tools.kb render` to apply a template to data.

## Website Update Flow

When an external site updates and you mirror new content into `raw/`, use this flow:

1. Re-run the site-specific crawler so the updated pages overwrite the same raw paths.
2. If the site changed structure or images, run the matching cleanup / image-localization script first.
3. Run `python -m tools.kb ingest --status changed --type markdown` to find changed markdown files.
4. Update `wiki/summaries/` for higher-value overview pages, and `wiki/concepts/` for cross-cutting changes.
5. Rebuild with `python -m tools.kb index`.
6. Confirm with `python -m tools.kb stats`.

For Beken docs, keep using the existing crawlers and cleanup scripts. If a raw file was already compiled, remember to update the manifest hash for that path after you finish handling it.
