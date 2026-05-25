# ARMINO 开发框架概述

> **TLDR:** ARMINO 是博通集成(Beken)的新一代 AIoT 软件开发框架，基于 CMake+Kconfig，支持 BK7235/7236/7236N/7239 多芯片平台，提供 WiFi/BT/低功耗/多媒体/安全启动的全功能 IoT 开发环境。

> **Source:** [BK7235 bk_overview.md](../../../raw/beken/bk_idk/BK7235/introduction/bk_overview.md), [BK7236 bk_overview.md](../../../raw/beken/bk_idk/BK7236/introduction/bk_overview.md), [BK7236N bk_overview.md](../../../raw/beken/bk_idk/BK7236N/introduction/bk_overview.md), [BK7239 bk_overview.md](../../../raw/beken/bk_idk/BK7239/introduction/bk_overview.md)

## 框架特性

- **硬件无关的开发框架** — 统一的 API 接口，跨芯片复用代码
- **丰富的 API 和应用实例** — WiFi、BLE、外设、安全等完整覆盖
- **CMake 灵活构建** — 支持组件管理、条件编译、纯 CMake 项目集成
- **Kconfig 配置系统** — 菜单化配置，与 ESP-IDF 体验一致
- **灵活的项目创建** — 基于模板快速创建新项目
- **物联网安全框架** — Secure Boot、Flash AES、eFuse、LCS、FIH 五层防护
- **多 RTOS 支持** — FreeRTOS、AliOS、LiteOS、RT-Thread
- **文档在线更新** — 文档系统自包含，支持随 SDK 迭代

## 芯片演进

| 代 | 芯片 | 核心特性 |
|---|---|---|
| 1 | BK7235 | ARM 单核，WiFi+BT，基础多媒体 |
| 2 | BK7236 | ARM+RISC-V 双核，安全启动，A/B OTA，WiFi v2.0 |
| 2.5 | BK7236N | BK7236 增强，+USB、+低功耗模式、+CPU 频率投票 |
| 3 | BK7239 | ARM+RISC-V 双核，+DVP Camera，强化安全 |

## 主要模块

1. **WiFi** — STA/AP/Monitor 三种接口，事件驱动，v2.0 API
2. **Bluetooth** — BLE (GAP/GATT/SMP) + BT Classic
3. **Peripheral** — GPIO/I2C/SPI/UART/PWM/ADC/DMA/Timer/WDT/QSPI/Flash
4. **System** — OS 适配层、POSIX 接口、Event 机制
5. **Security** — 安全启动、Flash 加密、eFuse/OTP、证书管理
6. **Power Save** — RTC Sleep、DTIM 保活、GPIO/Touch 唤醒、CPU 变频
7. **Multimedia** — DVP Camera、JPEG Encoder、Video Transfer

## Related

- [[../concepts/bk-armino-framework|BK ARMINO 开发框架]]
- [[../../categories/bk-doc|BK Docs 分类页面]]
