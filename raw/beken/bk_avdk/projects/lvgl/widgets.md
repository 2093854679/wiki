---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/projects/lvgl/widgets/index.html
sdk_family: bk_avdk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="widgets"></a>

# widgets工程

<a id="id1"></a>

## 1\. 简介

本工程是基于lvgl实现官方提供的widgets功能。

<a id="id2"></a>

### 1.1 规格

> - 硬件配置：
>   :   - 核心板，**BK7258\_QFN88\_9X9\_V3.2**
>       - 屏幕转接板，**BEKEN\_LCD\_V3**
>       - PSRAM 8M/16M
>       - 屏幕，**HX8282**，1024 \* 600 RGB LCD

<a id="id3"></a>

### 1.2 路径

> 工程路径: `<bk_avdk源代码路径>/project/lvgl/widgets`

<a id="id4"></a>

## 2\. 框架图

<a id="id5"></a>

### 2.1 软件模块架构图

软件模块架构图见 [图形用户界面](../../gui/lvgl.md) 中的lvgl framework图。

<a id="id7"></a>

### 2.2 代码模块关系图

LVGL的接口都定义在 **lv\_vendor.h** 和 **lvgl.h** 中。

<a id="id8"></a>

## 3\. 演示说明

> 烧录上电后lvgl ui会自动启动运行widgets功能。

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
- [86box](86box.md)
- [86box_smart_panel](86box_smart_panel.md)
- [benchmark](benchmark.md)
- [camera](camera.md)
- [keypad_encoder](keypad_encoder.md)
- [meter](meter.md)
- [meter_rgb_16M](meter_rgb_16M.md)
- [meter_spi](meter_spi.md)
- [music](music.md)
- [stress](stress.md)
- [第三方工程](../thirdparty.md)
- [Wi-Fi 工程](../wifi.md)
- [外设应用工程](../peripheral.md)
- [低功耗](../../power_save.md)
- [音频算法](../../audio_algorithms.md)
- [FAQ](../../FAQ.md)
