---
type: summary
source_root: beken
sdk_family: bk_avdk_smp
chip: BK7258
sdk_version: v3.1.1
processor: AP/CP
verified_at: 2026-10-21
---

# BK7258 SMP 的 AP／CP 架构

> **TLDR:** BK7258 AVDK SMP v3.1.1 将 CPU0 作为 CP，CPU1／CPU2 组成 AP SMP；两侧独立编译，通过 Mailbox 与共享内存交互，应用开发主要在 AP。

> **Source:** [AP(SMP)+CP 架构](../../../raw/beken/bk_avdk_smp/BK7258/developer-guide/architecture.md)

## 要点

- CP 承载 WiFi、BLE、低功耗保活及部分基础外设；AP 承载多媒体和主要应用逻辑。这里的核编号是 BK7258 此版本的物理核编号。
- AP／CP 有各自的组件、驱动和工程代码；构建生成 AP、CP、bootloader 镜像，再按工程分区打包。
- 两侧通过 Mailbox＋共享内存交互；上层还可使用虚拟 UART 抽象。AP 日志经 CP 的 UART 输出，AP CLI 需使用文档规定的 `ap_cmd` 前缀。
- SRAM／PSRAM 分配由工程配置约束。指南明确要求 CP 不把长期运行的任务、队列或代码放入可能掉电的 PSRAM。
- 物理核编号与 SMP 内部逻辑核编号不能混用；外设 API 应同时核对 AP 或 CP 的参考与示例。

## 导航

- [AP 文档](../../../raw/beken/bk_avdk_smp/BK7258/ap_doc/index.md)
- [CP 文档](../../../raw/beken/bk_avdk_smp/BK7258/cp_doc/index.md)
- [官方架构页](https://docs.bekencorp.com/arminodoc/bk_avdk_smp/smp_doc/bk7258/zh_CN/v3.1.1/developer-guide/architecture/index.html)

## Related

- [[bk-smp-ap-cp-boundaries]]
- [[bk7259-smp-architecture]]
- [[freertos-task-management]]
