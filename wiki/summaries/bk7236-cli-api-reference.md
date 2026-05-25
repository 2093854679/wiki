# BK7236 CLI & API参考

> **Source:** 10 cli_api/*.md files
> **TLDR:** BK7236 ARMINO SDK的CLI命令和API速查手册——覆盖WiFi、BLE、GPIO、UART、SPI、I2C、PWM、ADC、DMA、电源管理、安全启动和属性库的完整接口参考。

## Key Points

- **系统API**：`bk_init()`/`rtos_set_user_app_entry()`初始化；`rtos_create_thread()`创建任务；`rtos_delay_milliseconds()`延时
- **WiFi CLI**：`sta_connect SSID PASSWORD`连接AP；`ap SSID PASSWORD`创建热点；`iperp scan/ap/sta/stop`吞吐测试
- **WiFi API**：`bk_wifi_init()`/`bk_wifi_sta_connect()`/`bk_wifi_softap_start()`/`bk_wifi_scan_start()`/`bk_wifi_get_link_status()`
- **BLE CLI**：`ble_gatts`/`ble_gattc`/`ble_spp`/`bt_hidd`/`ble_mesh`
- **BLE API**：`ble_gatts_init()`/`ble_gattc_init()`/`ble_advertising_start()`/`ble_connection_update()`
- **外设API**：SPI（`bk_spi_driver_init`/`write_bytes`/`read_bytes`）、I2C（`bk_i2c_driver_init`/`memory_write`/`memory_read`）、PWM（`bk_pwm_init`/`set_period_duty`/`start`）、ADC（`bk_adc_driver_init`/`acquire`/`read`）
- **安全启动**：SecureBoot（XIP/TFM/Overwrite/No-TFM四种配置）
- **电源管理**：PM模块API（休眠/唤醒/功耗模式切换）

## Related Concepts

- [[wifi-basics]] — WiFi功能
- [[ble-protocol-overview]] — BLE功能
- [[task-development-records]] — 实习Task开发
