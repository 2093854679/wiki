---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_arduino/bk7239n/zh_CN/index.html
sdk_family: bk_arduino
chip: BK7239N
processor: ''
sdk_version: not-declared
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="beken-arduino"></a>

# Beken Arduino 开发指南

欢迎使用 Beken Arduino 开发文档。本指南提供了使用 Arduino 框架在 Beken 系列芯片上开发应用程序的全面信息。

<a id="id1"></a>

## 概述

本文档涵盖了在 Beken 微控制器上开发 Arduino 应用程序所需了解的所有内容。Beken Arduino 框架在流行的 Arduino 生态系统和 Beken 的无线微控制器解决方案之间提供了无缝集成，能够快速开发物联网应用。

该框架的主要特性包括：

- 完整的 Arduino API 兼容性
- 支持 Beken 的 BK7239N 芯片
- 集成的 Wi-Fi 和蓝牙低功耗连接功能
- 外设支持（GPIO、PWM、ADC、I2C、SPI、UART）
- 简单的设置和部署工具

文档

- [1\. 文档概述](chapters/overview.md)
  - [文档结构说明](chapters/overview.md#id2)
  - [其他资源](chapters/overview.md#id3)
- [2\. 平台与硬件](chapters/platform.md)
  - [芯片支持列表](chapters/platform.md#id2)
  - [芯片数据手册](chapters/platform.md#id3)
  - [外设支持列表](chapters/platform.md#id4)
  - [模块/开发套件硬件介绍](chapters/platform.md#id5)
- [3\. Arduino 框架](chapters/framework.md)
  - [Arduino 框架基础](chapters/framework.md#id1)
  - [数据类型和基本语法](chapters/framework.md#id4)
- [4\. 环境搭建](chapters/setup.md)
  - [支持的操作系统](chapters/setup.md#id2)
  - [1\. 安装 Python 环境](chapters/setup.md#python)
  - [2\. 安装 Arduino IDE](chapters/setup.md#arduino-ide)
  - [3\. 安装 Beken 开发板支持包 (BSP)](chapters/setup.md#beken-bsp)
  - [4\. 验证安装](chapters/setup.md#id6)
  - [示例程序](chapters/setup.md#id7)
- [5\. 外设](chapters/peripherals.md)
  - [ADC](chapters/peripherals/adc.md)
  - [GPIO](chapters/peripherals/gpio.md)
  - [I2C](chapters/peripherals/i2c.md)
  - [PWM](chapters/peripherals/pwm.md)
  - [SPI](chapters/peripherals/spi.md)
  - [UART](chapters/peripherals/uart.md)
- [6\. 定时器函数](chapters/system.md)
  - [HardwareTimer](chapters/hardware-timer.md)
  - [Ticker](chapters/software-timer.md)
- [7\. 无线功能](chapters/wireless.md)
  - [BLE (蓝牙低功耗)](chapters/wireless/ble.md)
  - [Wi-Fi](chapters/wireless/wifi.md)
- [8\. 调试指南](chapters/debug.md)
  - [SWD 系统调试](chapters/debug.md#swd)
  - [串口调试](chapters/debug.md#id4)
  - [常见编译问题排查](chapters/debug.md#id6)
  - [下载问题排查](chapters/debug.md#id7)
  - [硬件适配故障排查](chapters/debug.md#id8)
- [附录](appendix.md)
  - [官方资源和链接](appendix.md#id2)
  - [贡献指南](appendix.md#id4)
  - [版本更新记录](appendix.md#id5)
