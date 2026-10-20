---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/projects/lvgl/86box_smart_panel/index.html
sdk_family: bk_avdk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 支持离线语音识别的86盒子工程

<a id="id2"></a>

## 1\. 简介

本工程是基于lvgl和华镇语音识别算法实现的一个86box应用ui，支持开关状态显示、触摸控制和语音控制。

离线语音识别部分软件框架和code和 `<bk_avdk源代码路径>/thirdparty/wanson_asr` 一致。

请参考 [华镇语音识别工程](../thirdparty/wanson_asr.md)

<a id="id4"></a>

### 1.1 规格

> - 硬件配置：
>   :   - 核心板，**BK7258\_QFN88\_9X9\_V3.2**
>       - 屏幕转接板，**BEKEN\_LCD\_V3**
>       - PSRAM 8M/16M
>       - 屏幕，**ST7701S**，480 \* 480 RGB LCD
>       - 麦克小板，**BK\_Module\_Microphone\_V1.1**
> - 支持的唤醒词
>   :   - `阿尔米诺`
> - 支持的命令词
>   :   - `会客模式`
>       - `用餐模式`
>       - `离开模式`
>       - `回家模式`

<a id="id5"></a>

### 1.2 路径

> 工程路径: `<bk_avdk源代码路径>/project/lvgl/86box_smart_panel`

<a id="id6"></a>

## 2\. 框架图

<a id="id7"></a>

### 2.1 软件模块架构图

软件模块架构图见 [图形用户界面](../../gui/lvgl.md) 中的lvgl framework图。

<a id="id9"></a>

### 2.2 代码模块关系图

LVGL的接口都定义在 **lv\_vendor.h** 和 **lvgl.h** 中。

<a id="id10"></a>

## 3\. 演示说明

> 烧录上电后lvgl ui会自动启动运行，对着麦克风首先发出 **阿尔米诺** 切换到灯光控制页面，之后可以发出其他唤醒词进行不同模式下的灯光UI控制。此外还可以通过滑动界面和点击控制来调节开关组件的工作状态。

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
- [benchmark](benchmark.md)
- [camera](camera.md)
- [keypad_encoder](keypad_encoder.md)
- [meter](meter.md)
- [meter_rgb_16M](meter_rgb_16M.md)
- [meter_spi](meter_spi.md)
- [music](music.md)
- [stress](stress.md)
- [widgets](widgets.md)
- [第三方工程](../thirdparty.md)
- [Wi-Fi 工程](../wifi.md)
- [外设应用工程](../peripheral.md)
- [低功耗](../../power_save.md)
- [音频算法](../../audio_algorithms.md)
- [FAQ](../../FAQ.md)
