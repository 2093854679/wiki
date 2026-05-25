# LLM Knowledge Base

基于 Andrej Karpathy 的 LLM Knowledge Base 思想构建的 Obsidian 知识库。

**核心思路**: 你只投放 raw 源文件，LLM 负责编译、索引、导航和回答。你几乎不手动写 wiki。

## 工作流

```
① 网页抓取 (tools/web2md/)
         ↓
② raw/ 源文件投放
         ↓
③ kb ingest 检测新文件 → LLM 分级处理
         ↓
④ wiki/summaries/  (Tier 2: 架构级摘要)
   wiki/concepts/   (Tier 3: 跨文档综合分析)
         ↓
⑤ kb index 重建索引
         ↓
⑥ 查 wiki → index → chip hub → raw 原文
   好的答案写回 concepts/outputs，wiki 随提问长大
```

## 目录结构

```
raw/                          ← 源文件（只读，你只往里放）
  bk_doc/bk_idk/              ← BK7235/7236/7236N/7239 芯片文档 (1261篇)
  bk_doc/bk_matter/           ← BK Matter 协议文档
  Study_Note/                 ← 学习笔记
  智能桌面萌宠项目笔记/        ← Desktop Pet 项目

wiki/                         ← LLM 编译的知识库
  index.md                    ← 总索引（自动生成）
  categories/                 ← 分类导航（自动生成）
    bk-doc.md                 ← BK Docs 入口 + 芯片导航
    bk-doc/bk7236.md          ← 单芯片 hub 页（模块索引 → raw 链接）
    bk-doc/matter.md          ← Matter hub 页
  summaries/bk/               ← BK 架构级摘要 (7篇)
  concepts/                   ← 跨文档综合分析 (9篇)
  outputs/                    ← 问答记录草稿，有价值则 promote 到 concepts

tools/
  kb/                         ← kb CLI：ingest / index / query / lint / stats
  kb/cache/                   ← 搜索缓存
  web2md/scripts/             ← 网页 → Markdown 爬取工具
```

## 分级策略

| Tier | 类型 | 示例 | 写摘要？ |
|------|------|------|----------|
| 1 | API 参考 | `bk_uart.md`, `bk_gpio.md` | 否，chip hub 导航直达 raw |
| 2 | 架构/指南 | `bk_overview.md`, `matter-basic.md` | 是，写 TLDR 摘要 |
| 3 | 跨文档概念 | WiFi+BLE 共存、安全体系 | 是，写 concept |

**不是每篇 raw 都需要摘要。** API 文档本身就是答案。

## 常用命令

```powershell
python -m tools.kb ingest --status new    # 检测新文件
python -m tools.kb index                   # 重建索引
python -m tools.kb stats                   # 查看统计
python tools/kb/bootstrap_manifest.py      # 重建 manifest
```

## 网页抓取

```powershell
cd tools/web2md

# 抓取 BK_IDK 芯片文档
python scripts/bk_doc_to_md.py

# 单 URL 爬取（如 Matter 文档）
PYTHONPATH=. python scripts/crawl_bk_matter.py

# 图片本地化 + 结构扁平化
python scripts/postprocess_matter.py
```

## 查询导航

查 BK 芯片问题时的标准路径：

```
wiki/index.md → BK Docs → 芯片 hub → 模块 → raw 原文
```

不要绕过导航直接 grep raw。导航是地图，raw 是矿场。
