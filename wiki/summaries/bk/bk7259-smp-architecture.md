---
type: summary
source_root: beken
sdk_family: bk_avdk_smp
chip: BK7259
sdk_version: v4.0.1
processor: AP/CP
verified_at: 2026-10-21
---

# BK7259 SMP 的架构、启动与内存

> **TLDR:** BK7259 AVDK SMP v4.0.1 中 CPU0／CPU1 属于 CP，CPU2／CPU3 属于 AP；AP 默认 SMP，CP 可按工程配置为单核或 SMP，两侧独立镜像、链接与初始化。

> **Source:** [架构](../../../raw/beken/bk_avdk_smp/developer-guide/architecture.md), [系统启动](../../../raw/beken/bk_avdk_smp/developer-guide/system_boot.md), [内存资源](../../../raw/beken/bk_avdk_smp/developer-guide/memory_resource.md)

## 要点

- AP 主要承载应用与多媒体；CP 主要承载连接、低功耗保活和系统管理。是否启用 CP SMP 等能力以工程 Kconfig／sdkconfig 为准。
- CP 先初始化并启动调度，再由 `user_app` 路径拉起 AP；AP 完成初始化后向 CP 同步启动状态。具体入口和线程生命周期应查系统启动原文。
- 两侧各自生成链接结果与 RAM 区域配置。共享窗口、AP 辅助堆和 PSRAM 的约束不同；示例地址与容量不能当成所有工程固定值。
- Mailbox、共享内存、通道与 IPC 分层承担通知、控制和数据交换。Cache 属性及维护策略必须按本版本内存指南和工程配置核对。
- BK7258 v3.1.1 的三核分工不能直接用于本芯片；写代码前先确认目标芯片、AP／CP 及文档版本。

## 导航

- [AP 文档](../../../raw/beken/bk_avdk_smp/ap_doc/index.md)
- [CP 文档](../../../raw/beken/bk_avdk_smp/cp_doc/index.md)
- [官方架构页](https://docs.bekencorp.com/arminodoc/bk_avdk_smp/smp_doc/bk7259/zh_CN/v4.0.1/developer-guide/architecture/index.html)

## Related

- [[bk-smp-ap-cp-boundaries]]
- [[bk7258-smp-architecture]]
- [[freertos-memory-management]]
