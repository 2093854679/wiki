---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_aidk/bk7258/zh_CN/v2.0.1/projects/beken_wss_nopsram/index.html
sdk_family: bk_aidk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="beken-wss-psram"></a>

# Beken WSS 无 PSRAM 工程

<a id="id1"></a>

## 1\. 简介

> 本工程是 `beken_wss` 的\*\*无 PSRAM\*\* 裁剪版：同样用 WebSocket 传音频，但关闭 PSRAM，把缓冲和任务栈收进 SRAM，方便无 PSRAM 的模组或 BK7257 方案。
>
> 工程目录：`<source code>/projects/beken_wss_nopsram`
>
> 有 PSRAM、需要单屏字幕时请用 [Beken WSS 工程](beken_wss.md)。
> 配网 / 按键 / App 仍参考：[博通集成精灵AI（Beken\_Genie）工程](beken_genie.md)

<a id="beken-wss"></a>

## 2\. 与 beken\_wss 的差异

> - 同时打开 `CONFIG_BK_WSS_TRANS=y` 和 `CONFIG_BK_WSS_TRANS_NOPSRAM=y`。
> - `CONFIG_PSRAM=n`，`CONFIG_PSRAM_AS_SYS_MEMORY=n`，音频走 SRAM（`CONFIG_AUD_TRAS_USE_SRAM=y`）。
> - **BK7258**：关闭 LVGL 与单屏字幕（`CONFIG_SINGLE_SCREEN_FONT_DISPLAY=n`，`CONFIG_LVGL=n`），无 SD 卡 / FATFS，以省 RAM。
> - **BK7257**：同一工程另有 `config/bk7257`，打开 `CONFIG_DUAL_SCREEN_AVI_PLAY`，LDO 控制脚默认 GPIO42。
> - `bk_wss.c` / `bk_wss_main.c` 里多处 `#if CONFIG_BK_WSS_TRANS_NOPSRAM`：减小帧缓冲、关闭依赖 PSRAM 的路径。
> - 默认 WSS 地址与 `beken_wss` 相同：`wss://ai.aclsemi.com:9015`。

<a id="id2"></a>

## 3\. 支持芯片

<a id="bk7258"></a>

## 4\. 主要配置（BK7258）

> |  |  |  |  |
> | --- | --- | --- | --- |
> | Kconfig | CPU | Format | Value |
> | CONFIG\_BK\_WSS\_TRANS | CPU0 | bool | y |
> | CONFIG\_BK\_WSS\_TRANS\_NOPSRAM | CPU0 | bool | y |
> | CONFIG\_PSRAM | CPU0 \& CPU1 | bool | n |
> | CONFIG\_SINGLE\_SCREEN\_FONT\_DISPLAY | CPU0 \& CPU1 | bool | n |
> | CONFIG\_LVGL | CPU1 | bool | n |
> | CONFIG\_AUD\_TRAS\_USE\_SRAM | CPU0 | bool | y |
> | CONFIG\_WEBSOCKET / CONFIG\_WEBSOCKET\_TLS | CPU0 | bool | y |
>
> BK7258 CPU0 SRAM 默认 `CONFIG_CPU0_SPE_RAM_SIZE=0x68000`。内存紧张时优先关日志、关未用外设，不要再打开 LVGL 字幕。

<a id="id3"></a>

## 5\. 编译与烧录

> - BK7258 固件：`<source code>/build/beken_wss_nopsram/bk7258/all-app.bin`
> - BK7257 固件：`<source code>/build/beken_wss_nopsram/bk7257/all-app.bin`
> - 无 SD-NAND 资源依赖（7258 默认关了 SD / FATFS）。烧录 all-app.bin 即可。

<a id="id4"></a>

## 6\. 问题\&回答

Q：为什么 7258 没有字幕？

A：无 PSRAM 时 SRAM 不够同时跑 LVGL 字库和音频环。字幕请用带 PSRAM 的 `beken_wss`。

Q：运行中出现 malloc 失败 / heap\_4 assert？

A：先确认 `CONFIG_PSRAM=n` 且没有组件仍按 PSRAM 地址申请。可关 `CONFIG_DEBUG_DUMP`、减小 `CONFIG_TRANS_APP_TASK_SIZE`，并看串口 `memory_free_show` 日志。

Q：WSS 地址怎么改？

A：与 `beken_wss` 相同，改 `bk_wss_main.c` 的 `websocket_cfg.uri`。
