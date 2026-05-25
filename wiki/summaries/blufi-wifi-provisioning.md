# BluFi 配网（集成 esp-wifi-connect）

> **Source:** [blufi.md](../../raw/智能桌面萌宠项目笔记/blufi.md)
> **TLDR:** 通过 BLE BluFi 协议实现 ESP32 Wi-Fi 配网——手机 App 通过蓝牙发送 Wi-Fi 凭证，设备写入 NVS 后自动连接；需在 menuconfig 中关闭 Hotspot 配网避免冲突。

## Key Points

- 需在 menuconfig 中启用 `CONFIG_USE_ESP_BLUFI_WIFI_PROVISIONING=y`，同时关闭 Hotspot 配网
- 蓝牙协议栈二选一：`CONFIG_BT_BLUEDROID_ENABLED` 或 `CONFIG_BT_NIMBLE_ENABLED`
- 工作流程：手机 BluFi App 连接设备→发送 SSID/密码→设备写入 SsidManager（NVS）→启动 WifiStation 扫描连接
- 官方 EspBlufi App 可直接使用；自定义客户端需遵循 BluFi 协议帧格式
- 多次测试时建议清除 NVS 中 `wifi` 命名空间避免旧配置干扰

## Related Concepts

- [[wifi-basics]] — WiFi 基础
- [[mqtt-udp-protocol]] — MQTT+UDP 混合通信
