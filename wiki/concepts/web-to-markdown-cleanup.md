---
type: concept
aliases:
  - Markdown conversion cleanup
  - 网页转 Markdown 清洗
  - Sphinx 锚点清理
---

# 网页转 Markdown 清洗

> **TLDR:** 抓取网页并转换为 Markdown 时，应在转换/落盘环节清理标题锚点、永久链接和 Sphinx 生成的跳转噪音，避免这些残留进入 raw、summary 和后续 LLM 上下文。

## 适用场景

- 使用浏览器、爬虫、web2md、HTML-to-Markdown 工具抓取网页文档。
- 抓取 Sphinx、ReadTheDocs、Doxygen+Breathe 等文档站点。
- 原始 Markdown 中出现大量 `[](#... "永久链接至标题")`、`[](#... "永久链接至目标")`、`永久链接至表格`、`永久链接至图片`、`永久链接至代码` 等转换残留。

## 清洗规则

在网页转 Markdown 的转换阶段执行清理，不要等到摘要或概念抽取阶段再处理。

- 删除标题后的 Sphinx permalink 残留：

```md
# 驱动开发规范[](#id1 "永久链接至标题")
```

应清理为：

```md
# 驱动开发规范
```

- 删除 API、表格、图片、代码标题后面的永久链接噪音：

```md
bk_uart_driver_init(void)[](#_CPPv419bk_uart_driver_initv "永久链接至目标")
Certification Steps[](#id11 "永久链接至图片")
设备证书配置[](#id1 "永久链接至表格")
```

应清理为：

```md
bk_uart_driver_init(void)
Certification Steps
设备证书配置
```

- 清理目录项中被转换器拼进文本的锚点字样：

```md
- [快速入门id1 永久链接至标题](bk_matter/get-started.md)
```

应尽量恢复为：

```md
- [快速入门](bk_matter/get-started.md)
```

## 建议匹配模式

优先清理这些形态：

```text
[](#... "永久链接至标题")
[](#... "永久链接至目标")
[](#... "永久链接至表格")
[](#... "永久链接至图片")
[](#... "永久链接至代码")
```

以及链接文本中夹带的：

```text
id数字 永久链接至标题
id数字 永久链接至目标
永久链接至表格
永久链接至图片
永久链接至代码
```

## 保留规则

- 不要删除真实的章节标题、API 名称、参数名、图片说明或表格标题。
- 不要删除正常的站内链接、外部链接和 Obsidian `[[wikilinks]]`。
- 对 API reference，允许保留函数签名和类型链接的可读文本，但应移除永久链接锚点噪音。

## Related

- [[embedded-coding-standards]]
- [[bk-armino-framework]]
