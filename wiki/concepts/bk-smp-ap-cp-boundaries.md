---
type: concept
aliases:
  - BK SMP AP CP 分工
  - BK7258 与 BK7259 SMP 差异
verified_at: 2026-10-21
---

# BK SMP 的芯片、处理器侧与版本边界

> **TLDR:** 查 BK SMP 资料时，必须先锁定芯片、SDK 文档族／版本与 AP／CP；相同的 AP／CP 术语和 API 名称不代表物理核编号、内存布局或运行约束相同。

## 两个已核实的基线

- [[bk7258-smp-architecture]] 对应 BK7258 AVDK SMP v3.1.1：CPU0 是 CP，CPU1＋CPU2 是 AP SMP。
- [[bk7259-smp-architecture]] 对应 BK7259 AVDK SMP v4.0.1：CPU0／CPU1 属于 CP，CPU2／CPU3 属于 AP；CP 是否启用双核 SMP 取决于工程配置。

这两种分工分别来自 [BK7258 架构原文](../../raw/beken/bk_avdk_smp/BK7258/developer-guide/architecture.md) 和 [BK7259 架构原文](../../raw/beken/bk_avdk_smp/developer-guide/architecture.md)，不能只用“AP 是双核”推断物理核编号。

## 检索与实现顺序

1. 选择芯片与 SDK 文档族，确认官网默认版本及本地文件 frontmatter。
2. 先读 SMP 总架构和资源分配，再进入目标 AP 或 CP 的模块指南。
3. 将同一侧的 API reference 与 examples 配对核对；跨侧能力先查 IPC 或虚拟 UART 设计。
4. 修改内存、PSRAM 或低功耗配置时，回到该工程的分区与 RAM 配置；文档示例容量只代表对应基线。

## 易混淆处

- SMP 内部逻辑 core 编号与芯片物理 CPU 编号。
- AVDK v2.0.1 的 CPU1 多媒体用法与 AVDK SMP 的 AP 子系统。
- AP 与 CP 同名外设 API 的资源归属、初始化顺序及可用配置。
- 旧芯片示例的内存地址与新工程生成的 RAM／Flash 布局。

## Related

- [[bk-avdk-overview]]
- [[bk7258-smp-architecture]]
- [[bk7259-smp-architecture]]
- [[bk-armino-framework]]
- [[freertos-task-management]]
