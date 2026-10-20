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

## AI 检索方式

从仓库根目录运行；在 `wiki/` 中把 `python kb.py` 换成 `python ../kb.py`。
也可在任意目录调用 `python D:/Desktop/obsidian/kb.py`。
完整说明见 [AI 检索指南](wiki/AI-SEARCH.md)。

```powershell
# 自然语言问题 → 有预算、带原文行号和适用范围的 JSON 证据包
python kb.py context "串口初始化" --chip BK7236 --json-output

# 精确限定芯片、SDK、版本、处理器
python kb.py search "UART 中断接收" --chip BK7259 --family bk_avdk_smp --version v4.0.1 --processor AP --json-output

# 长 API 文档也按匹配段落返回，再用实际结果中的路径和行号核对
python kb.py search "bk_wifi_sta_start" --chip BK7236 --kind api --json-output
python kb.py read "<结果中的 workspace_path>" --start-line 100 --end-line 160 --json-output

python kb.py ingest --status new
python kb.py index
python kb.py stats
```

检索支持中文词组、常见中英文别名、函数名和按标题切分的原文段落。
默认排除未验证历史镜像和输出记录；空结果不会改用其他芯片或随机文章。
`search`、`context`、`read` 完全本地运行，无需 LLM API 密钥。
`query` 是可选的外部 LLM 问答命令，使用相同检索证据。

浏览入口：[简短首页](wiki/index.md) · [官网 SDK / 默认版本目录](wiki/categories/beken-official.md) · [全部概念](wiki/categories/concepts.md)。

## 网站文档更新流程

当网站内容更新、`raw/` 里已有页面被覆盖时，按这个顺序处理：

```powershell
python -m tools.kb ingest --status changed --type markdown
python -m tools.kb index
python -m tools.kb stats
```

如果站点结构、图片或目录也变了，先跑对应 crawler / cleanup / 图片本地化脚本，再执行上面的流程。  
Beken 这类文档优先复用现有 crawler，`changed` 文件会被 `ingest` 识别出来；需要的话，再补 `wiki/summaries/` 或 `wiki/concepts/`。


## 克隆完整知识库

SMP 文档保存在子仓库，克隆时包含子模块：

```powershell
git clone --recurse-submodules git@github.com:2093854679/wiki.git
```

已有克隆可运行 `git submodule update --init --recursive` 补齐文档，随后运行 `python kb.py index` 建立本地检索缓存。
