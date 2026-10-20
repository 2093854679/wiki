---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/projects/peripheral/lcd_spi/index.html
sdk_family: bk_avdk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="spi-lcd"></a>

# SPI LCD

<a id="id1"></a>

## 1 功能概述

> 本工程主要验证了SPI驱动ST7796U屏幕的功能，上电后会在屏幕上每隔500ms刷新显示红绿蓝三种颜色，用于调试验证新的SPI LCD显示。

<a id="id2"></a>

## 2 代码路径

> demo路径：`./projects/peripheral/lcd_spi`

<a id="id3"></a>

## 3 编译命令

> 编译命令：`make bk7258 PROJECT=peripheral/lcd_spi`

<a id="id4"></a>

## 4 演示介绍

> 编译该工程进行烧录后上电，屏幕每隔500ms依次循环全屏刷新红绿蓝三种颜色。

## 模块导航

- [快速入门](../../get-started.md)
- [H/W 参考](../../hw-reference.md)
- [API 参考](../../api-reference.md)
- [支持外设](../../support_peripherals.md)
- [摄像头](../../camera.md)
- [DISPLAY](../../display.md)
- [PSRAM内存分配](../../psram_config.md)
- [视频编解码](../../video_codec.md)
- [图形用户界面](../../gui.md)
- [参考工程](../../projects.md)
- [蓝牙(Bluetooth)工程](../bluetooth.md)
- [多媒体工程(Multi-media)工程](../media.md)
- [图形界面(LVGL)工程](../lvgl.md)
- [第三方工程](../thirdparty.md)
- [Wi-Fi 工程](../wifi.md)
- [外设应用工程](../peripheral.md)
- [dvp](dvp.md)
- [uvc](uvc.md)
- [slcd](slcd.md)
- [lcd_qspi](lcd_qspi.md)
- [lcd_rgb565](lcd_rgb565.md)
- [lcd_rgb888](lcd_rgb888.md)
- [lcd_rgb666](lcd_rgb666.md)
- [lcd_8080](lcd_8080.md)
- [低功耗](../../power_save.md)
- [音频算法](../../audio_algorithms.md)
- [FAQ](../../FAQ.md)
