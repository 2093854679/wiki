---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7258/zh_CN/v2.0.1/developer-guide/peripheral/bk_usb.html
sdk_family: bk_idk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="usb"></a>

# USB 使用指南

<a id="id1"></a>

## 概述

> 当前芯片支持的USB类型如下所示：

| USB类型 | 工作电压 | USB协议 | 设备协议 | 速度 | 编码协议 | 分辨率 | 端点\`wMaxPacketSize\` | 备注 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UVC | 5.0v | USB 1.1/2.0 | UVC 1.5 | High/Full-Speed | MJPEG | 1280\*720 | 1024 | 不支持DRI字段 |
| UAC | 5.0v | USB 1.1/2.0 | UAC 1.0 | High/Full-Speed | ALL | N | 1024 |  |

## 模块导航

- [简介](../../introduction.md)
- [快速入门](../../get-started.md)
- [H/W 参考手册](../../hw-reference.md)
- [API 参考手册](../../api-reference.md)
- [开发者指南](../../developer-guide.md)
- [软件架构与分层](../architecture.md)
- [构建](../build_config.md)
- [配置与工具](../config_tools.md)
- [系统安全](../security.md)
- [低功耗与电源管理](../power_save.md)
- [内存与性能](../memory_perf.md)
- [设备管理框架](../driver_model.md)
- [外设与驱动](../peripheral.md)
- [DMA](bk_dma.md)
- [ICU](bk_interrupt.md)
- [PWM](bk_pwm.md)
- [TRNG](bk_trng.md)
- [SARADC](bk_adc.md)
- [SPI](bk_spi.md)
- [UART](bk_uart.md)
- [WDT](bk_wdt.md)
- [I2C](bk_i2c.md)
- [I2S](bk_i2s.md)
- [事件机制](../event.md)
- [出错与日志](../error_log.md)
- [系统调试](../debug_trace.md)
- [稳定性问题调试](../debug_stability.md)
- [Wi-Fi](../wifi.md)
- [Bluetooth](../bluetooth.md)
- [HTTP](../http.md)
- [OS 抽象层](../os_abstraction.md)
- [Bootloader与Ota](../bootloader_ota.md)
- [用例编写](../examples.md)
- [文档系统](../documentation.md)
- [OS 相关参考](../../os.md)
- [样例演示](../../examples.md)
- [应用开发](../../application.md)
- [开发与贡献代码流程](../../process.md)
- [云平台](../../cloud.md)
- [工程与示例](../../projects/projects.md)
