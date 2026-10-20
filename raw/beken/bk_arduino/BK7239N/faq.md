---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_arduino/bk7239n/zh_CN/faq.html
sdk_family: bk_arduino
chip: BK7239N
processor: ''
sdk_version: not-declared
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="faq"></a>

# FAQ

<a id="arduino-core"></a>

## 这个仓库只是 Arduino Core 吗？

不是。仓库同时还包含 staging、打包和 SDK 导出逻辑，这些部分共同决定了 Arduino CLI / Arduino IDE 能否真正消费这个平台。

<a id="target"></a>

## 当前支持哪些 target？

当前公开支持的 target 是：

- `bk7239n`

<a id="prepare-platform"></a>

## `prepare-platform` 需要每次都手动运行吗？

不一定。`cli-compile`、`build`、`export-sdk` 以及 release 相关目标本身已经会串上所需生成步骤。只有当你想显式检查或刷新 staged platform 时，才需要单独跑一次。

<a id="id1"></a>

## 第一次验证更推荐哪条路径？

第一次成功路径更建议直接用 Arduino CLI 编译仓库自带示例，因为这更接近最终用户消费 staged platform 的方式。

<a id="generic-variant"></a>

## generic variant 能等同于板卡定义吗？

不能完全等同。它更像平台基线，而不是所有第三方板卡的完整定义。如果某块板在线路或引脚暴露上差异很大，应把 generic variant 当起点，而不是最终答案。

<a id="id2"></a>

## 为什么有些示例会在运行时做防御性检查？

有些功能依赖最终镜像里实际链接进去的 staged SDK 内容。相比让整个示例无法编译，运行时明确报告能力边界有时更利于平台持续可用。

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
