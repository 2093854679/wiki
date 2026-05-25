# BK WiFi API v2.0

> **TLDR:** BK WiFi 驱动 v2.0 是事件驱动架构，支持 STA/AP/Monitor 三种接口独立运行，提供 Common/Interface/Module 三类 API；配置结构体预留字段必须清零保证向前兼容，回调中不应执行繁重操作。

> **Source:** [bk_wifi.md](../../raw/bk_doc/bk_idk/BK7236/api-reference/wifi/bk_wifi.md)

## 三种 WiFi 接口

| 接口 | 功能 | 互斥限制 |
|------|------|----------|
| **STA** | 连接外部 AP | 不能与 Monitor 同时启用 |
| **AP** | 创建热点，接受 STA 连接 | — |
| **Monitor** | 嗅探所有 802.11 帧 | 启用时 STA 无法连接/扫描 |

## API 三层分类

### Common APIs (通用)
- `bk_wifi_init()` / `bk_wifi_deinit()` — 初始化/反初始化
- `bk_wifi_set_country()` / `bk_wifi_get_country()` — 国家码配置
- `bk_wifi_send_raw()` — 发送原始 802.11 帧

### Interface APIs (接口级) — 前缀 `bk_wifi_{interface}_`
- **STA**: `_sta_start/stop/set_config/connect/disconnect/pm_enable/pm_disable/get_mac`
  - `bk_wifi_sta_set_config()` 支持设置自动重连次数和超时
- **AP**: `_ap_start/stop/set_config/get_sta_list/get_mac`
  - `bk_wifi_ap_update_hidden_cap()` 支持运行时切换隐藏 SSID
- **Monitor**: `_monitor_start/stop/set_config/register_cb/set_channel/suspend/resume`

### Module APIs (模块级) — 前缀 `bk_wifi_{module}_`
- **Scan**: `_scan_register_cb/start/stop/get_result/dump_result/free_result`
- **Filter**: `_filter_set_config/register_cb` — 控制接收哪些管理帧

## 编程原则

1. **配置结构体预留字段必须清零** — 使用 `WIFI_DEFAULT_INIT_CONFIG()` 等宏初始化
2. **返回值检查** — 用 `BK_ERR_CHECK` 检查所有 API 返回值
3. **Event 回调中不要做繁重处理** — relay 事件到应用任务
4. **参考示例代码** — 不确定时先看 WiFi 示例

## 关键机制

### Filter 机制
通过 `bk_wifi_filter_set_config()` 控制哪些管理帧能到达应用层：
- 默认只接收与当前接口相关帧（STA 连 AP 时只收该 AP 的 beacon）
- `rx_all_beacon` 标志可以收所有信标
- `rx_all_default_mgmt` 控制是否接收所有默认管理帧

### 电源管理
- `bk_wifi_sta_pm_enable/disable()` — STA 端开关省电模式
- `bk_wifi_send_listen_interval_req()` — 设置侦听间隔（推荐 1/3/10）
- `bk_wifi_set_min_rsv_mem()` — 限制 WiFi TX 预留堆内存（默认 10KB，最大 30KB）

### 多媒体优化
- `bk_wifi_set_wifi_media_mode()` — 视频传输时优化流畅度
- `bk_wifi_set_video_quality()` — 三档画质：FD(流畅)/SD(标清)/HD(高清，默认)

## Related

- [[../concepts/bk-armino-framework|BK ARMINO 开发框架]]
- [[../concepts/wifi-networking-stack|WiFi网络技术栈]]
- [[wifi-basics|WiFi 802.11基础]]
