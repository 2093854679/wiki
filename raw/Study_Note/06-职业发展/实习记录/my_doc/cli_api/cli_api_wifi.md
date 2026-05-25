# WiFi相关CLI命令与常用API速查

本笔记整理了projects/wifi下各例程main目录中注册的CLI命令，以及常用WiFi API，便于开发和调试。

---

## ap 例程
- **编译命令**：`make bk7236 PROJECT=wifi/ap`
- **命令名**：无专用CLI命令（ap_main.c为纯例程，未注册cli命令）
- **说明**：演示如何启动SoftAP，配置SSID、密码、IP等参数，支持终端连接和断开事件日志输出。

---

## sta_connect 例程
- **编译命令**：`make bk7236 PROJECT=wifi/sta_connect`
- **命令名**：无专用CLI命令（sta_connect_main.c为纯例程，未注册cli命令）
- **说明**：演示如何以STA模式连接指定WiFi，支持连接/断开事件日志输出。

---

## iperf 例程
- **编译命令**：`make bk7236 PROJECT=wifi/iperf`
- **命令名**：`scan`、`ap`、`sta`、`stop`、`iperf`
- **用法**：
    - `scan [ssid]` —— 扫描WiFi（可指定SSID）
    - `ap ssid [password] [channel]` —— 启动AP
    - `sta ssid [password] [bssid] [channel]` —— 连接STA
    - `stop {sta|ap}` —— 停止STA或AP
    - `iperf help` —— iperf性能测试
- **说明**：支持WiFi扫描、AP/STA模式切换、性能测试等。

---

## repeater 例程
- **编译命令**：`make bk7236 PROJECT=wifi/repeater`
- **命令名**：`scan`、`ap`、`sta`、`stop`、`iperf`
- **用法**：
    - `scan [ssid]` —— 扫描WiFi（可指定SSID）
    - `ap ssid [password] [channel]` —— 启动AP
    - `sta ssid [password] [bssid] [channel]` —— 连接STA
    - `stop {sta|ap}` —— 停止STA或AP
    - `iperf help` —— iperf性能测试
- **说明**：支持WiFi扫描、AP/STA模式切换、性能测试等，与iperf例程类似。

---

## 其它例程
- softap、static_ip、wapi、csi、ftm、rlk_demo等未发现注册专用CLI命令，主要为功能演示代码。

---

## WiFi常用API速查

### 1. WiFi初始化与配置
- `bk_wifi_init(wifi_init_config_t *config)` —— 初始化WiFi模块
- `bk_wifi_deinit(void)` —— 反初始化WiFi模块
- `bk_wifi_get_mac(uint8_t *mac)` —— 获取MAC地址

### 2. AP模式相关
- `bk_wifi_ap_set_config(wifi_ap_config_t *config)` —— 设置AP参数
- `bk_wifi_ap_start(void)` —— 启动AP
- `bk_wifi_ap_stop(void)` —— 停止AP

### 3. STA模式相关
- `bk_wifi_sta_set_config(wifi_sta_config_t *config)` —— 设置STA参数
- `bk_wifi_sta_start(void)` —— 启动STA
- `bk_wifi_sta_stop(void)` —— 停止STA
- `bk_wifi_sta_connect(void)` —— 连接指定AP
- `bk_wifi_sta_disconnect(void)` —— 断开连接

### 4. 扫描与事件
- `bk_wifi_scan(void)` —— 启动WiFi扫描
- `bk_event_register_cb(event_module_t mod, int event_id, event_cb_t cb, void *arg)` —— 注册事件回调

### 5. 网络与IP配置
- `bk_netif_init(void)` —— 初始化网络接口
- `bk_netif_set_ip4_config(netif_if_t netif, netif_ip4_config_t *config)` —— 设置IP、掩码、网关、DNS

### 6. 其它常用API
- `bk_wifi_get_link_status(wifi_link_status_t *status)` —— 获取连接状态
- `bk_wifi_get_rssi(int *rssi)` —— 获取信号强度

### 7. 常用结构体与类型
- `wifi_ap_config_t` —— AP配置参数
- `wifi_sta_config_t` —— STA配置参数
- `wifi_init_config_t` —— WiFi初始化参数
- `netif_ip4_config_t` —— IPv4网络参数
- `wifi_link_status_t` —— WiFi连接状态

---

> 说明：
> - 以上命令和API均为常用WiFi开发接口，具体参数和用法请参考头文件和官方文档。
> - 如需补充其它WiFi相关CLI命令或API，请告知具体例程或接口。
