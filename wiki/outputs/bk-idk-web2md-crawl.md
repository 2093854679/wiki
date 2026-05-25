# BK_IDK 文档抓取记录

> **TLDR:** 使用 `YouChenJun/web2md` 的 `ConverterService` 将 Beken BK_IDK 芯片文档转换为 Markdown，并保存到 `raw/bk_doc/bk_idk/`。

## Source

- 入口页：`https://docs.bekencorp.com/arminodoc/chipchoose/?dk=BK_IDK&lan=zh`
- 工具：`YouChenJun/web2md`
- 输出目录：`raw/bk_doc/bk_idk/`

## Converted Chips

- `BK7235`：170 个 Markdown 页面
- `BK7236`：234 个 Markdown 页面
- `BK7236N`：189 个 Markdown 页面
- `BK7239`：186 个 Markdown 页面
- `BK7256`：253 个 Markdown 页面
- `BK7258`：241 个 Markdown 页面

## Notes

- 站点存在 Safeline `HTTP 468` 挑战页，原始 web2md 渲染器会提前把 468 当作失败。
- 本次使用 web2md 的 HTML 到 Markdown 转换逻辑，配合脚本刷新 Safeline JWT 后抓取页面。
- 脚本位置：`tools/web2md/scripts/bk_doc_to_md.py`

## Related

- [[bk7236-cli-api-reference]]
- [[embedded-communication-protocols]]
- [[wifi-networking-stack]]

