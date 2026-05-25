# BK WiFi-BLE 共存与功耗权衡

> **TLDR:** BK7235/7236 的 WiFi 和 BLE 是独立驱动，可以同时运行。PM 模块通过独立休眠投票机制协调两者——只有当 WiFi 和 BLE 都投票睡眠后 MCU 才进入低电压模式。同时开启意味着 MCU 更难深度睡眠，不需要 BLE 时应关闭以降功耗。

## 共存机制

WiFi 和 BLE 两套驱动完全独立，各自有初始化入口和事件系统：

```
bk_wifi_init() ─── WiFi Driver ─── EVENT_WIFI_*
                                        \
                    PM 模块 ←── 双方独立投票睡眠
                                        /
bk_ble_create_db() ─ BLE Driver ─── BLE_5_*_EVENT
```

- PM 模块定义了 `wifi_bt_wakeup_type_e` 枚举，区分 `WIFI_WAKEUP` 和 `BT_WAKEUP`
- `bk_pm_module_vote_sleep_ctrl()` 允许各模块独立向 PM 投票
- **MCU 进入低电压/深度睡眠的条件：所有模块都投了 sleep 票**

唯一的互斥限制在 **WiFi 内部**（STA 与 Monitor 不能共存），与 BLE 无关。

## 功耗层次

| 配置 | 功耗量级 | 机制 |
|------|---------|------|
| WiFi STA TX + BLE 连接 | 最高 (~60-100mA) | 两模块全开 |
| WiFi STA DTIM10 + BLE advertising | 较低 (mA 级) | 双方周期性休眠 |
| WiFi STA PM enabled + BLE idle | 更低 | WiFi 深度休眠，BLE 待命 |
| WiFi STA PM enabled + BLE disabled | 最低 (~μA) | 只有 WiFi DTIM 唤醒 |
| Power OFF | ~0 | 完全断电 |

## 实际建议

1. **配网场景** — BLE 配完网即关。来自 BK 官方文档：
   > "当使用BT配置完网络，不要使用BT时，可以把它关掉，这样可以达到更低的功耗"

2. **长连接场景** — 如需 BLE 保持连接：
   - WiFi 启用 PM：`bk_wifi_sta_pm_enable()`
   - 设置合理的 Listen Interval（推荐 1/3/10）
   - BLE 用最大的连接间隔

3. **同时传输场景** — 两个射频同时活跃时功耗最高，但硬件处理了共存仲裁，不会有功能冲突

## Related

- [[bk-armino-framework|BK ARMINO 开发框架]]
- [[wifi-networking-stack|WiFi网络技术栈]]
- [[../summaries/bk-wifi-api-v2|BK WiFi API v2.0]]
- [[../summaries/bk-low-power|BK 低功耗与电源管理]]
- [BK7235 PM API](../../raw/beken/bk_idk/BK7235/api-reference/pm/bk_pm.md)
- [BK7236 WiFi Alive](../../raw/beken/bk_idk/BK7236/developer-guide/power_save/bk_wifi_alive.md)
