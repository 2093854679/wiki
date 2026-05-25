# BK 低功耗与电源管理

> **TLDR:** BK 芯片低功耗方案涵盖时钟管理、CPU 变频、RTC 深度睡眠、WiFi DTIM 保活和多媒体关断——通过 32K 时钟源选择、FSM 状态机、GPIO/Touch 唤醒实现从微安级到毫安级的动态功耗调节。

> **Source:** [power_save/index.md](../../../raw/beken/bk_idk/BK7236/developer-guide/power_save/index.md)

## 低功耗层次

```
完全运行 (Full Active)    →  ~几十 mA
  ├─ CPU Frequency Vote    →  按需降频
  ├─ WiFi DTIM Sleep       →  周期性休眠 (毫秒级)
  ├─ Close Multimedia      →  关断未用多媒体模块
  ├─ RTC Sleep             →  深度睡眠 (微安级)
  └─ Power OFF             →  完全断电
```

## 关键机制

### 时钟管理
- **32K 时钟源选择** — 内部 RC 振荡器 vs 外部 32.768KHz 晶振（精度更高）
- **CPU 频率投票** (CPU Vote Frequency) — 外设驱动向电源管理模块"投票"请求最低 CPU 频率，空闲时自动降频
- **时钟门控** — 未使用模块自动关断时钟

### FSM 电源状态机
- 硬件自动管理电压域开关
- 不同芯片有不同电源域划分
- 关机时不需供电的域自动断电

### WiFi 低功耗
- **DTIM 机制** — AP 每 N 个 Beacon 才缓存广播帧，STA 可跳过中间 Beacon 深度休眠
- **Listen Interval** — STA 可设置 1~N 个 Beacon 间隔才醒来检查
- **WiFi Alive** — 周期性唤醒维持 TCP 长连接，防止服务器超时断连
- **WiFi PM (Power Management)** — `bk_wifi_sta_pm_enable/disable()` 开关

### RTC 深度睡眠
- GPIO 唤醒 (上升/下降沿)
- Touch 唤醒 (触摸按键)
- 定时唤醒 (RTC Timer)
- 需配置唤醒后外设重初始化流程

### 低功耗检查清单 (Lowpower Checklist)
- 确保所有未用 GPIO 配置为模拟输入或下拉
- 检查是否有未释放的唤醒源
- 使用外部 32K 晶振以获得稳定的休眠定时精度

## 典型功耗场景

| 场景 | 功耗水平 | 机制 |
|------|---------|------|
| WiFi 大数据传输 | ~60-100mA | Full Active |
| WiFi 待机 (DTIM10) | ~1-5mA 平均 | DTIM Sleep |
| BLE 广播 | ~几百μA 平均 | 周期性唤醒 |
| RTC Sleep + GPIO 唤醒 | ~几μA | 深度睡眠 |
| Power OFF | ~0 | 完全断电 |

## Related

- [[../concepts/bk-armino-framework|BK ARMINO 开发框架]]
- [[bk-wifi-api-v2|BK WiFi API v2.0]]
- [[../../categories/bk-doc|BK Docs 分类页面]]
