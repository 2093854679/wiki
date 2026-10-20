---
type: concept
aliases:
  - BK ARMINO 开发框架
  - Beken SDK 选型与导航
verified_at: 2026-10-21
---

# BK ARMINO 开发框架

> **TLDR:** Beken 文档应按 IDK 底座、AVDK 音视频、SMP 平台及产品方案分层检索；芯片、SDK 版本和 AP／CP 是使用 API 前必须确认的范围。

## 文档族与开发任务

- [[bk-armino-overview]]：IDK 的组件、构建配置、驱动、网络与安全入口；不同芯片的能力由各自文档和工程配置确认。
- [[bk-avdk-overview]]：BK7258 AVDK v2.0.1 的音视频、PSRAM 与媒体模块功耗。
- [[bk7258-smp-architecture]]、[[bk7259-smp-architecture]]：各自版本的 AP／CP 分工、构建和资源边界。
- [[bk-ai-solution-overview]]、[[bk-smp-product-solutions-overview]]：AI、仪表、门铃和 IPC 等产品业务及接入流程。
- [[bk-toolkit-overview]]：烧录、射频、音频、UI 与开发环境工具。

所有产品、版本与模块入口见 [Beken 官方文档分类](../categories/beken-official.md)。官网默认版本不等同于所有历史版本，工具的 `latest` 也不代表统一的 SDK 发布版本。

## 构建与配置

IDK 文档将目标芯片、项目和组件区分：CMake 组织组件依赖与构建，Kconfig 定义配置项，实际值由芯片与工程配置共同决定。图形菜单是否可用必须查对应版本；[BK7236 v2.0.1 配置说明](../../raw/beken/bk_idk/BK7236/developer-guide/config_tools/bk_config_kconfig.md) 明确不支持 menuconfig。

## 网络、安全与升级

- [[bk-wifi-api-v2]] 只核验 BK7236 IDK v2.0.1：关注初始化、事件、接口限制和函数支持状态。
- [[bk-security-framework]] 区分 TrustZone 隔离、安全启动和 Flash AES／CRC；目录中的章节不等于已给出完整实现说明。
- [[bk-bootloader-ota]] 区分常规 OTA、A/B 位置无关升级和 TF-M 安全升级；镜像布局、确认和回退条件应按所选方案读取。
- [[bk-low-power]] 区分普通睡眠、低压保持与深度睡眠；功耗量级需要具体板卡和业务测量。

这里不再沿用缺少来源的芯片代际表、跨芯片 CPU 拓扑或“所有芯片统一五层安全”的推断。

## 检索顺序

1. 明确芯片、文档族和版本；SMP 还需明确 AP 或 CP。
2. 架构问题先读概览，函数参数直接查目标 raw API。
3. 实现前同时核对同芯片、同侧的指南和示例。
4. 原文冲突、缺失或标为 TBC 时明确记录，不补猜结论。

## Related

- [[bk-smp-ap-cp-boundaries]]
- [[wifi-networking-stack]]
- [[freertos-kernel-mechanisms]]
- [[embedded-software-design-patterns]]
- [[iot-communication-protocols]]
