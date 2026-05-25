# LLM Knowledge Base

这是一个基于 Obsidian 的 LLM 知识库。

核心原则：
- `raw/` 放原始资料
- `wiki/` 放编译后的摘要、概念页、分类页和输出
- `kb` CLI 负责 ingest、index、search、query 和维护

## 工作流

```text
1. 抓取网页/导入资料 -> raw/
2. `python -m tools.kb ingest --status new`
3. 按 tier 处理：
   - Tier 1: 只更新 manifest 和导航
   - Tier 2: 写 `wiki/summaries/`
   - Tier 3: 写 `wiki/concepts/`
4. `python -m tools.kb index`
5. `python -m tools.kb stats`
```

## 目录结构

```text
raw/                          原始文档，只读
  beken/bk_idk/               BK7235/7236/7236N/7239/7256/7258 芯片文档
  beken/bk_matter/            BK Matter 文档
  Study_Note/                 学习笔记
  智能桌面萌宠项目笔记/        Desktop Pet 项目

wiki/                         LLM 编译后的知识库
  index.md                    总索引
  categories/                 分类 hub
  summaries/                  单篇摘要
  concepts/                   跨文档概念页
  outputs/                    问答、图表、草稿

tools/
  kb/                         kb CLI
  kb/cache/                   manifest、搜索索引、raw metadata 缓存
  web2md/scripts/             网页抓取和清理脚本
```

## 检索方式

- `python -m tools.kb search` 同时搜索 `wiki/` 和 `raw/`
- Beken 技术文档优先直接命中 `raw/` 原文
- `python -m tools.kb query` 会把命中的 wiki + raw 一起喂给 LLM

## 常用命令

```powershell
python -m tools.kb ingest --status new
python -m tools.kb index
python -m tools.kb search BK7258 --limit 10
python -m tools.kb query "BK7258 的 UART 有几个" --no-save
python -m tools.kb metadata --chip BK7258 --limit 20
python -m tools.kb graph-health
python -m tools.kb stats
```

## BK 文档导航

```text
wiki/index.md -> BK Docs -> 芯片 hub -> 模块 -> raw 原文
```

不要直接跳过导航去 grep `raw/`，先路由，再下钻。

