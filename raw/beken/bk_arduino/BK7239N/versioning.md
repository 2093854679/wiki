---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_arduino/bk7239n/zh_CN/versioning.html
sdk_family: bk_arduino
chip: BK7239N
processor: ''
sdk_version: not-declared
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 版本与发布通道说明

<a id="id2"></a>

## 目的

本页说明当文档站点通过本地或 CI 驱动的 Sphinx 流程发布时，应该如何描述版本通道。

<a id="id3"></a>

## 推荐的通道含义

建议始终保持下面的含义：

- `latest`：当前开发分支对应的文档
- `stable`：面向普通用户的最新已发布 tag 版本文档

<a id="latest"></a>

## 哪些内容应该进入 `latest`

`latest` 更适合承载：

- 正在推进中的 target
- 新增但尚未随正式版本发布的示例
- 已进入默认分支但尚未进入 release 的功能说明
- 尚未进入正式发布包的 staging / 打包行为变化

<a id="stable"></a>

## 哪些内容应该进入 `stable`

`stable` 更适合描述：

- 最新正式发布的平台版本
- 面向普通用户可预期可用的 target 和工作流
- 与已发布产物相匹配的安装方式

<a id="id4"></a>

## 文档编写约束

当开发通道和发布通道存在差异时：

- 明确页面默认针对哪个通道
- 不要把未发布命令混进 stable 安装路径
- package index 和 release URL 优先只在 `stable` 路径中给出

<a id="id5"></a>

## 仓库版本来源

当前文档配置从仓库顶层 `VERSION` 文件读取版本号。对于初始站点这已经够用，但正式托管发布时，仍应让 tag 名称、package 版本和文档通道标签保持一致。

<a id="id6"></a>

## 实际建议

只要页面依赖尚未发布的仓库状态，就应默认把它当作 `latest` 内容，直到相同流程已经出现在正式发布产物中。

## 模块导航

- [1. 文档概述](chapters/overview.md)
- [2. 平台与硬件](chapters/platform.md)
- [3. Arduino 框架](chapters/framework.md)
- [4. 环境搭建](chapters/setup.md)
- [5. 外设](chapters/peripherals.md)
- [6. 定时器函数](chapters/system.md)
- [7. 无线功能](chapters/wireless.md)
- [8. 调试指南](chapters/debug.md)
- [附录](appendix.md)
