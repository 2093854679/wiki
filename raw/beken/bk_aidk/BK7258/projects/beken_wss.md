---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_aidk/bk7258/zh_CN/v2.0.1/projects/beken_wss/index.html
sdk_family: bk_aidk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="beken-wss"></a>

# Beken WSS 工程

<a id="id1"></a>

## 1\. 简介

> 本工程基于 `beken_genie` 的 BLE 配网框架，用 **WebSocket（WSS）** 代替声网 / 火山 RTC 传音视频流，并在\*\*单屏\*\*上用 LVGL 字体滚动显示对话字幕。
>
> 配网、按键、灯效、唤醒词、提示音与精灵工程相同。屏幕方案接近 `ai_dashboard`：一块 360x360 QSPI LCD（ST77916），不做双屏眼睛 AVI。
>
> 硬件原理图、按键、灯效、App 配网请参考：[博通集成精灵AI（Beken\_Genie）工程](beken_genie.md)
>
> 工程目录：`<source code>/projects/beken_wss`
>
> `projects/readme.txt` 说明：基于 beken\_genie 配网框架 \+ websocket 传输流 \+ 单屏字幕显示。

<a id="beken-genie-ai-dashboard"></a>

## 2\. 与 beken\_genie / ai\_dashboard 的差异

> - 传输宏：`CONFIG_BK_WSS_TRANS=y`，代码在 `projects/common_components/network_transfer/bk_wss/`。
> - 默认 WSS 地址写在 `bk_wss_main.c`：`wss://ai.aclsemi.com:9015`。量产请改成客户自己的 WSS 服务。
> - 显示：`CONFIG_SINGLE_SCREEN_FONT_DISPLAY=y`，组件 `single_screen_font_display` 用 LVGL label 按 UTF-8 逐字刷新字幕。
> - 不做 `CONFIG_DUAL_SCREEN_AVI_PLAY`，也不走声网 / 火山 RTC。
> - 仍使用 PSRAM（与下面的 `beken_wss_nopsram` 相对）。

<a id="id2"></a>

## 3\. 主要配置

> |  |  |  |  |
> | --- | --- | --- | --- |
> | Kconfig | CPU | Format | Value |
> | CONFIG\_BK\_WSS\_TRANS | CPU0 | bool | y |
> | CONFIG\_SINGLE\_SCREEN\_FONT\_DISPLAY | CPU0 \& CPU1 | bool | y |
> | CONFIG\_LCD\_QSPI\_ST77916 | CPU1 | bool | y |
> | CONFIG\_LCD\_BACKLIGHT\_GPIO | CPU1 | int | 25 |
> | CONFIG\_LCD\_QSPI\_RESET\_PIN | CPU1 | int | 45 |
> | CONFIG\_LCD\_QSPI\_ID | CPU1 | int | 1 |
> | CONFIG\_WEBSOCKET / CONFIG\_WEBSOCKET\_TLS | CPU0 | bool | y |
>
> `CONFIG_LCD_BACKLIGHT_GPIO`、`CONFIG_LCD_QSPI_RESET_PIN`、`CONFIG_LCD_QSPI_ID` 需在工程 `Kconfig.projbuild` 里定义才生效。
>
> 字幕 UI：`projects/common_components/single_screen_font_display/lvgl_ui.c`。
> 配网 adapter：`projects/common_components/bk_smart_config/src/adapter/wss/`。

<a id="id3"></a>

## 4\. 工作流程

> 1. BLE 配网（Beken App），SSID / 密码写入设备。
> 2. STA 连上后 `beken_auto_run()` → `beken_wss_main()` 建立 WSS。
> 3. MIC 编码后经 `rtc_websocket_audio_send_data` 上行；下行 PCM / G722 进喇叭。
> 4. 服务端下发的文本进入 LVGL 字幕队列，单屏滚动显示。
>
> 音频默认 16 kHz，G722 或 PCM，AEC 打开。

<a id="id4"></a>

## 5\. 编译与烧录

> - 源码根目录：`make bk7258 PROJECT=beken_wss`
> - 固件：`<source code>/build/beken_wss/bk7258/all-app.bin`
> - 单屏字幕依赖字库资源，请按 `single_screen_font_display` 中打开的字体文件放到 SD-NAND（或按工程实际资源路径）。
> - 烧录方法同 IDK：[代码烧录](../../../bk_idk/BK7258/get-started.md)

<a id="id6"></a>

## 6\. 问题\&回答

Q：如何改 WSS 服务器？

A：改 `projects/common_components/network_transfer/bk_wss/bk_wss_main.c` 里 `websocket_cfg.uri`，并保证证书 / SNI 与 `CONFIG_WEBSOCKET_TLS` 匹配。

Q：屏幕能否换成别的 QSPI / SPI LCD？

A：可以，分辨率宽需为 16 的倍数、高为 8 的倍数。同时改 CPU1 的 LCD 宏和 `lv_vendor_init()` 宽高，参考 `ai_dashboard`。

Q：和 `beken_wss_nopsram` 怎么选？

A：板子有 PSRAM、需要单屏字幕，用本工程。无 PSRAM 或要编 BK7257，用 [Beken WSS 无 PSRAM 工程](beken_wss_nopsram.md)。
