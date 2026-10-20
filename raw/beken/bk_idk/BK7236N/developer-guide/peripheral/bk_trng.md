---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7236n/zh_CN/v2.2.1/developer-guide/peripheral/bk_trng.html
sdk_family: bk_idk
chip: BK7236N
processor: ''
sdk_version: v2.2.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="trng"></a>

# TRNG 使用指南

<a id="id1"></a>

## 概述

TRNG 真随机数发生器，集成在 Beken 芯片内部，通过随机噪声产生真随机数，不依赖于其他模块。

<a id="id2"></a>

## TRNG 使用方法

> - TRNG使能，可调用 bk\_trng\_start() 使能
> - 获取随机数，调用 bk\_rand() 获取

备注

默认情况下系统已经初始化 TRNG 模块，应用可以直接使用 bk\_rand()

## 模块导航

- [简介](../../introduction.md)
- [快速入门](../../get-started.md)
- [H/W 参考手册](../../hw-reference.md)
- [API 参考手册](../../api-reference.md)
- [开发者指南](../../developer-guide.md)
- [软件架构与分层](../architecture.md)
- [构建](../build_config.md)
- [配置与工具](../config_tools.md)
- [低功耗与电源管理](../power_save.md)
- [设备管理框架](../driver_model.md)
- [外设与驱动](../peripheral.md)
- [DMA](bk_dma.md)
- [ICU](bk_interrupt.md)
- [PMW](bk_pwm.md)
- [SARADC](bk_adc.md)
- [SPI](bk_spi.md)
- [UART](bk_uart.md)
- [WDT](bk_wdt.md)
- [I2C](bk_i2c.md)
- [IOMUX](bk_iomux.md)
- [RTC](bk_rtc.md)
- [事件机制](../event.md)
- [出错与日志](../error_log.md)
- [系统调试](../debug_trace.md)
- [Wi-Fi](../wifi.md)
- [Bluetooth](../bluetooth.md)
- [HTTP](../http.md)
- [OS 抽象层](../os_abstraction.md)
- [Bootloader与Ota](../bootloader_ota.md)
- [用例编写](../examples.md)
- [文档系统](../documentation.md)
- [安全](../../security.md)
- [OS 相关参考](../../os.md)
- [购买 BK7236N 开发板](../../boards.md)
- [用例指南](../../examples.md)
- [开发与贡献代码流程](../../process.md)
