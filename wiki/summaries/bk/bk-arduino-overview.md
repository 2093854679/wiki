---
type: summary
source_root: beken
sdk_family: bk_arduino
chip: BK7239N
sdk_version: null
processor: null
---

# BK7239N Arduino 开发概览

> **TLDR:** Beken Arduino 把 BK7239N 的无线与外设能力接入 Arduino 开发生态，入门从 Python、Arduino IDE 和开发板支持包开始，再用基础示例逐层验证。
> **Source:** [Arduino 首页](../../../raw/beken/bk_arduino/BK7239N/index.md)、[环境搭建与验证](../../../raw/beken/bk_arduino/BK7239N/chapters/setup.md)

## 关键要点

- **芯片与功能范围。** 首页明确 BK7239N、Wi-Fi、BLE，以及 GPIO/PWM/ADC/I2C/SPI/UART 外设支持，并将框架、环境、定时器、无线和调试分章。[首页](../../../raw/beken/bk_arduino/BK7239N/index.md)
- **先安装板卡支持。** 官方搭建流程先准备 Python、Arduino IDE，再使用 Boards Manager 安装 Beken BK7239N 支持包并选择对应板卡。[环境搭建](../../../raw/beken/bk_arduino/BK7239N/chapters/setup.md)
- **用示例分层验证。** 指南建议先跑 Blink、SerialEcho、WiFiScan、WireScanner，再进入 ADC、PWM、硬件定时器等外设示例。[验证顺序](../../../raw/beken/bk_arduino/BK7239N/chapters/setup.md)
- **宿主机步骤不同。** 文档列 Windows、Linux 和 macOS 环境；macOS 有单独的 uploader 与 zstd 安装要求，不能直接套用 Windows 步骤。[平台差异](../../../raw/beken/bk_arduino/BK7239N/chapters/setup.md)

## 适用范围

官网入口路径未声明固定文档版本，因此 `sdk_version` 留空。环境页引用的 Boards Manager 发布标签不等于整个文档当前版本。未核实 AP/CP 架构，不与 IDK/AVDK 的构建命令混用。

## Related

- [[bk-armino-framework]]
- [[embedded-communication-protocols]]
- [[ble-protocol-overview]]
- [[custom-board-guide]]
