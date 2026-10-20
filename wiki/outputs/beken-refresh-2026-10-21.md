# Beken 官网文档更新记录

> **TLDR:** 2026-10-21 按官网默认版本、中文优先重新抓取并分类；官方 API 以原文和导航保留，高价值指南另做摘要。

## 结果

- 官网 17 个已发布文档族，37 个产品项；共享 Matter 文档去重，SMP 拆分 AP／CP 后实际抓取 37 个文档根。
- 成功转换 3027 页正文，保存 1997 个图片／PDF 资源。
- 官网索引列出的页面全部覆盖，缺失 0 页；正文另含 69 个返回 404 的链接，均保留官网 URL 并登记。
- 资源失败 7 项：2 个官网 404、3 个需要登录、2 个返回 HTML 而非 PDF；未保存错误页冒充附件。另有 9 处原文锚点不存在，本地链接落到对应页面。
- 新增 12 篇高价值摘要，更新 6 篇已有摘要；新增 1 篇跨文档概念，更新 2 篇已有 BK 概念。
- 历史 Markdown 124 篇按原路径保留并标记；清单中已不存在的 154 条 Beken 记录另存档。

## 分类与来源

- [官方文档分类](../categories/beken-official.md)
- [SMP 芯片与处理器侧边界](../concepts/bk-smp-ap-cp-boundaries.md)
- 每篇原文 frontmatter 保存官网 URL、芯片、文档族、版本、AP／CP 和抓取时间。
- 官网标为开发中的 AT／HomeKit／OTT／Auto 未构造地址；BLE 下载目录保留官网外链。
- 本轮只覆盖官网默认版本，中文优先，不覆盖全部历史版本或双语副本。

## 可核验记录

- [完整分类、失败链接与验证数据](beken-refresh-2026-10-21-details.json)
- 3,027 篇正文和 1,997 个资源的实际文件字节 hash 校验全部通过；新 Beken 分类、摘要和概念的本地链接检查无失效项。
- 3,027 篇当前官方正文均进入搜索库；124 篇历史资料保留原路径并退出默认搜索。
- manifest 检查：新增 0、变更 0、失效记录 0。按 BK7259／AVDK SMP／AP 筛选得到 403 篇；共享 Matter 文档也可按任一关联芯片定位。
- 官网机器人简介与 SMP 总架构的核编号冲突已在 AI 摘要中并列标注，未作为统一拓扑传播。
- 抓取清单、失败项、校验与备份目录：`C:/Users/48527/.codex/visualizations/2026/10/20/01a15a2a-40b3-79a1-9f1e-ba1ebda07ac1/beken-refresh-2026-10-21`
- 持久来源目录：`tools/kb/cache/beken_official_sources.json`。
- 可重复抓取脚本：`tools/web2md/scripts/refresh_beken_official.py`，默认入口快照：`beken_official_roots.json`；用 `--work-dir` 指定新的暂存目录，先 `crawl`，验证后 `publish`。
- 旧文件覆盖前已备份；本轮不删除历史文档和原有图片。

## Related

- [[concept-map]]
- [[bk-smp-ap-cp-boundaries]]
