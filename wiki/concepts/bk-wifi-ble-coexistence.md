---
type: concept
aliases:
  - BK WiFi BLE 共存与功耗
verified_at: 2026-10-21
---

# BK WiFi 与 BLE 的保活及功耗边界

> **TLDR:** 在 BK7236 IDK v2.0.1 的低压保活流程中，WiFi、BT、应用投票和唤醒源共同影响睡眠；关闭不用的 BT 可减少功耗，但不能据此推定固定电流或所有射频场景都没有约束。

## 已核实的流程

[WiFi 低压保活指南](../../raw/beken/bk_idk/BK7236/developer-guide/power_save/bk_wifi_alive.md) 给出设置 listen interval、选择低压模式、连接路由器及取得 IP 后投 APP 睡眠票的示例，并建议在 BT 配网结束且后续不用 BT 时关闭它。

[系统状态机](../../raw/beken/bk_idk/BK7236/developer-guide/power_save/bk_fsm.md) 将普通睡眠、低压睡眠与深度睡眠分开：低压模式支持 WiFi／BT 等唤醒源，深度睡眠唤醒后走复位流程。因此 WiFi 关联保活不能直接等同于深度睡眠。

## 两类限制要分开

- **WiFi 接口限制**：[[bk-wifi-api-v2]] 对应原文明确 Monitor 与 STA 存在启动限制。
- **无线共存与系统功耗**：需另查目标芯片 SDK 配置、BT 活动、模块投票与板级实测；WiFi 接口限制不能证明所有 WiFi／BLE 组合都无冲突。

## 排查入口

- [[bk-low-power]]：睡眠模式、唤醒和功耗排查。
- [低功耗检查清单](../../raw/beken/bk_idk/BK7236/developer-guide/power_save/bk_lowpower_checklist.md)：核对模块投票、外设供电、CLI 日志和正常／异常电流波形。
- [[wifi-dtim10-tcp-keepalive]]：项目中的低功耗与连接保活任务；示例参数需重新匹配目标版本。

本文不提供跨芯片通用电流表，也不将芯片静态电流当作包含无线活动的长期平均值。

## Related

- [[bk-armino-framework]]
- [[bk-low-power]]
- [[bk-wifi-api-v2]]
- [[wifi-networking-stack]]
