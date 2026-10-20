---
type: summary
source_root: beken
sdk_family: bk_idk
chip: BK7236
sdk_version: v2.0.1
processor: null
---

# BK7236 低功耗与电源管理概览

> **TLDR:** BK7236 低功耗要联合检查系统睡眠模式、RTOS 空闲、模块投票、唤醒源和业务收尾；低压保活与深度睡眠的恢复行为不同，功耗必须在具体板卡及业务下测量。
> **Source:** [低功耗总目录](../../../raw/beken/bk_idk/BK7236/developer-guide/power_save.md)、[系统状态机](../../../raw/beken/bk_idk/BK7236/developer-guide/power_save/bk_fsm.md)、[Wi-Fi 低压保活](../../../raw/beken/bk_idk/BK7236/developer-guide/power_save/bk_wifi_alive.md)、[问题检查清单](../../../raw/beken/bk_idk/BK7236/developer-guide/power_save/bk_lowpower_checklist.md)

## 关键要点

- **先区分模式。** 普通睡眠是空闲任务进入 WFI；低压睡眠降低电压并暂停部分模块；深度睡眠唤醒后系统复位。不能统一写成“RTC sleep 后原程序继续运行”。[状态机](../../../raw/beken/bk_idk/BK7236/developer-guide/power_save/bk_fsm.md)
- **睡眠与唤醒要配套。** RTOS 空闲及模块投票共同决定能否进入睡眠；该版本的低压模式支持 GPIO/RTC/Touch/Wi-Fi/BT 唤醒，深度睡眠列出的唤醒源为 GPIO/RTC/Touch。[状态机与唤醒矩阵](../../../raw/beken/bk_idk/BK7236/developer-guide/power_save/bk_fsm.md)
- **Wi-Fi 保活按流程配置。** 指南示例设置 listen interval、选择低压模式、连接路由器，并强调拿到 IP 后再投 APP 睡眠票；不再需要 BT 时可关闭它，但不能据此保证通用的微安级平均电流。[Wi-Fi 保活](../../../raw/beken/bk_idk/BK7236/developer-guide/power_save/bk_wifi_alive.md)
- **主频由投票协调。** 动态主频文档说明统一在 CPU0 配置并采用模块请求中的最高频率，使用结束要以同一模块 ID 恢复默认；具体核及频率联动仍应核对实际芯片工程。[主频投票](../../../raw/beken/bk_idk/BK7236/developer-guide/power_save/bk_cpu_vote_freq.md)
- **排障靠日志与电流对照。** 检查清单建议核对外设供电、模块投票、原版 SDK 基线、DTIM 配置及 `pm_debug` 日志，并对比正常/异常电流波形。[检查清单](../../../raw/beken/bk_idk/BK7236/developer-guide/power_save/bk_lowpower_checklist.md)

## 适用范围

只覆盖 BK7236 IDK v2.0.1 文档。原文部分电源指南含其它 CPU 编号表述，本文不由此推断核拓扑；不提供跨芯片通用电流表，板级静态电流也不等于包含无线活动的长期平均电流。

## Related

- [[bk-wifi-api-v2]]
- [[wifi-dtim10-tcp-keepalive]]
- [[bk-wifi-ble-coexistence]]
- [[freertos-task-management]]
