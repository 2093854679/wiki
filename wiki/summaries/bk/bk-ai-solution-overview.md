---
type: summary
source_root: beken
sdk_family: [bk_aidk, bk_ai_smp]
chip: [BK7258, BK7259]
sdk_version:
  bk_aidk/BK7258: v2.0.1
  bk_ai_smp/BK7258: v3.1.1
  bk_ai_smp/BK7259: v4.0.1
processor: null
---

# BK AI 开发框架与机器人方案概览

> **TLDR:** BK AI 文档分为基于 IDK/AVDK 的 AIDK 和基于 AVDK SMP 的场景方案；BK7259 机器人方案进一步明确端侧、RTC 云通道与模型服务的分工。
> **Source:** [AIDK BK7258](../../../raw/beken/bk_aidk/BK7258/index.md)、[AI SMP BK7258](../../../raw/beken/bk_ai_smp/BK7258/index.md)、[AI SMP BK7259](../../../raw/beken/bk_ai_smp/BK7259/index.md)、[机器人架构简介](../../../raw/beken/bk_ai_smp/BK7259/intro.md)

## 关键要点

- **先选 SDK 底座。** AIDK BK7258 明确依赖 Armino IDK 与 AVDK；AI SMP BK7258 则依赖对应版本的 AVDK SMP，两个文档族应分别检索。[AIDK 原文](../../../raw/beken/bk_aidk/BK7258/index.md)／[AI SMP 原文](../../../raw/beken/bk_ai_smp/BK7258/index.md)
- **按应用工程进入。** AIDK 的工程目录列有 Beken-Genie、AI_Dashboard、火山 RTC、灵芯、百炼和 WSS 等入口，具体接入、硬件和配置以各工程页为准。[工程索引](../../../raw/beken/bk_aidk/BK7258/projects.md)
- **BK7259 是机器人参考方案。** 官方概览覆盖 LVGL UI、本地语音唤醒、Agora RTC AI 对话、视觉问答及 BLE 配网；它提供业务代码，工具链、构建系统和驱动底座由 AVDK SMP 提供。[方案简介](../../../raw/beken/bk_ai_smp/BK7259/intro.md)
- **官网核编号存在冲突。** BK7259 机器人简介把 AP 写成 CPU1+CPU2、CP 写成 CPU0；同默认 v4.0.1 的 AVDK SMP 总架构则把 AP 写成 CPU2+CPU3、CP 写成 CPU0+CPU1（CP 可配置单核或 SMP）。不能将机器人页的核编号当作已确认拓扑；落地时需核对目标 SDK 的物理核、逻辑 core ID 和工程配置。[机器人简介](../../../raw/beken/bk_ai_smp/BK7259/intro.md)／[SMP 总架构](../../../raw/beken/bk_avdk_smp/developer-guide/architecture.md)

## 适用范围

本摘要覆盖 AIDK BK7258 v2.0.1、AI SMP BK7258 v3.1.1、AI SMP BK7259 v4.0.1 的官网默认中文入口。不同芯片和底座的工程路径、外设及配置不能互换；本文不推定其它版本兼容性。

## Related

- [[bk-armino-framework]]
- [[freertos-kernel-mechanisms]]
- [[desktop-pet-docs]]
- [[iot-communication-protocols]]
