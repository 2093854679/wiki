# 工程介绍

> **TLDR:** 这是一个面向 Obsidian 的 LLM 知识库工程：把 `raw/` 里的原始学习资料、文档、网页、论文和项目笔记，经过 `kb` CLI 扫描、摘要、概念抽取、索引和搜索，编译成 `wiki/` 里的可查询知识网络。

## 工程定位

这个工程不是传统业务应用，而是一个本地知识库编译系统。它把零散资料放在 `raw/`，再通过 `kb` 命令行工具生成结构化 wiki：

- `wiki/summaries/`：每份或每组源文档的摘要。
- `wiki/concepts/`：跨文档提炼出来的概念文章。
- `wiki/outputs/`：问答、报告、幻灯片、图表等生成结果。
- `wiki/index.md`：自动生成的总索引。
- `.kb_search.db`：SQLite FTS5 全文搜索索引。

## 主要目录

- `kb/`：Python CLI 源码，包含 ingest、compile、query、index、search、serve、lint 等功能。
- `raw/`：原始资料库，目前包含嵌入式、C 语言、FreeRTOS、网络协议、面试记录、智能桌面萌宠项目笔记等内容。
- `wiki/`：已编译 wiki，目前有 summaries、concepts 和 outputs。
- `templates/`：Jinja2 模板，用于生成 summary、concept、index、Marp slides 等 Markdown。
- `static/`：本地搜索页面资源。
- `config.yaml`：统一配置 raw/wiki 路径、LLM 模型、编译参数、搜索端口等。

## 工作流

1. `python -m kb ingest` 扫描 `raw/`，识别新文件、变更文件和文件类型。
2. LLM 读取新/变更源文档，写入 `wiki/summaries/`，并抽取可复用概念到 `wiki/concepts/`。
3. `python -m kb index` 扫描 wiki Markdown，重建 `wiki/index.md`。
4. `python -m kb search --reindex` 或 `python -m kb serve` 建立/使用 SQLite FTS5 搜索。
5. `python -m kb query "问题"` 可以基于 wiki 检索相关文档并生成答案，结果可保存到 `wiki/outputs/`。

## 关键模块

- `kb/ingest.py`：扫描 `raw/`，计算文件 hash，根据 `.kb_manifest.json` 判断 new/changed/unchanged。
- `kb/compiler.py`：调用 LLM，把文本类源文档编译成摘要，并进一步抽取概念文章。
- `kb/indexer.py`：从 wiki Markdown 中抽取标题、TLDR、wikilinks，生成总索引。
- `kb/search_engine.py`：用 SQLite FTS5 建全文搜索库。
- `kb/query.py`：搜索 wiki，加载相关文档，调用 LLM 生成回答/幻灯片/图表。
- `kb/server.py`：启动本地搜索 Web UI。
- `kb/linter.py`：做一致性、缺口、关联建议等知识库健康检查。

## 当前状态

- `python -m kb ingest` 扫描到 `raw/` 下 1926 个文件，其中 Markdown 97 个。
- `python -m kb stats` 显示当前 wiki 有 61 个 Markdown 条目：52 篇 summaries、7 篇 concepts、1 篇 output、1 个 index。
- 当前未发现 `.kb_manifest.json`，所以 ingest 会把所有 raw 文件都标记为 new。这说明已有 wiki 内容和增量 manifest 状态没有对齐，后续最好补齐 manifest 或重新做一次受控编译。

## 维护建议

- 不要直接调用 `python -m kb compile`，除非配置了外部 API key；当前约定是由 Codex 作为 LLM 编译器直接读取 raw 并写 wiki。
- 每次新增资料到 `raw/` 后，先跑 `ingest`，只处理 new/changed 文件。
- 编译后固定跑 `index` 和 `stats`，必要时再跑 `search --reindex`。
- 好的问答结果应保存到 `wiki/outputs/`，稳定后再提升为 `wiki/concepts/`。

## Related

- [[embedded-software-design-patterns]]
- [[embedded-communication-protocols]]
- [[iot-communication-protocols]]
- [[wifi-networking-stack]]
