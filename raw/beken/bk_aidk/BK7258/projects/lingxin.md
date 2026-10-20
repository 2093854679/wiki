---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_aidk/bk7258/zh_CN/v2.0.1/projects/lingxin/index.html
sdk_family: bk_aidk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="lingxin"></a>

# 阿里灵芯（Lingxin）工程

<a id="id1"></a>

## 1\. 简介

> 本工程基于 `beken_genie`，将云端对话通道从声网 RTC 切换为\*\*阿里灵芯（LingXin）语音对话引擎\*\*。
>
> 配网、按键、灯效、双屏 AVI、唤醒词、提示音等交互与 `beken_genie` 一致，硬件仍是 AIDK AI 玩具开发板（双 SPI LCD GC9D01）。
>
> 详细硬件、按键、灯效、配网与 App 操作请参考：[博通集成精灵AI（Beken\_Genie）工程](beken_genie.md)
>
> 工程目录：`<source code>/projects/lingxin`

<a id="beken-genie"></a>

## 2\. 与 beken\_genie 的差异

> - 传输与对话栈使用 `LingXin_AI_IoT_VoiceChatEngine`，由 `CONFIG_LINGXIN_AI_EN=y` 打开。
> - 配网成功后走 `bk_smart_config` 的灵芯 adapter：向 Beken 服务器 `activate_agent` 领取 `appId` / `appKey` / `sn` / `agentCode`，再调用 `voice_chat_init()` 启动对话。
> - 显示仍为双屏 AVI（`CONFIG_DUAL_SCREEN_AVI_PLAY=y`），不是单屏字幕。
> - 音频默认 PCM 16 kHz，支持 G722、AEC、KWS。

<a id="id2"></a>

## 3\. 主要配置

> |  |  |  |  |
> | --- | --- | --- | --- |
> | Kconfig | CPU | Format | Value |
> | CONFIG\_LINGXIN\_AI\_EN | CPU0 | bool | y |
> | CONFIG\_BK\_SMART\_CONFIG | CPU0 | bool | y |
> | CONFIG\_DUAL\_SCREEN\_AVI\_PLAY | CPU0 \& CPU1 | bool | y |
> | CONFIG\_WEBSOCKET | CPU0 | bool | y |
>
> 关键代码：
>
> - 灵芯配网 / 鉴权：`projects/common_components/bk_smart_config/src/adapter/lingxin/`
> - 对话启动：`projects/common_components/network_transfer/lingxin_wss/lingxin_wss_main.c`
> - 引擎组件：`bk_avdk/components/bk_thirdparty/LingXin_AI_IoT_VoiceChatEngine`

<a id="id3"></a>

## 4\. 鉴权说明

> 默认（未打开 `CONFIG_ENABLE_LINGXIN_COSTOM_AUTH`）：
>
> 1. 设备用芯片 UID 作为 channel，通过 BLE 配网把 channel 交给 App / 服务器。
> 2. 联网后 HTTP POST `activate_agent`，解析返回的 `app_id`、`app_key`、`sn`、`agent_code`。
> 3. 把上述四个回调注册进 `VoiceChatInitProps`，再 `voice_chat_init()`。
>
> 若使用自有灵芯租户，打开 `CONFIG_ENABLE_LINGXIN_COSTOM_AUTH`，在 adapter 里自行提供 appId / appKey / SN / agentCode，不再走 Beken `activate_agent`。

<a id="id4"></a>

## 5\. 编译与烧录

> - [AIDK 代码下载](../get-started.md#armino-aidk-sdk)
> - 在源码根目录编译：`make bk7258 PROJECT=lingxin`
> - 固件：`<source code>/build/lingxin/bk7258/all-app.bin`
> - 烧录与 SD-NAND 资源（眼睛 AVI 等）与 `beken_genie` 相同，见精灵工程 3.5 节。

<a id="id5"></a>

## 6\. 问题\&回答

Q：和声网精灵工程比，客户侧要改什么？

A：配网 App 流程可复用。差异在云端：本工程连灵芯对话引擎，需要有效的灵芯 `appId` / `appKey` / [<a id="id7"></a>
\`\`](#id6)agentCode\`\`（默认由 Beken 服务器下发）。

Q：没有屏幕能不能编过？

A：可以，但默认打开了双屏 AVI。无屏产品需在 menuconfig 里关闭 `CONFIG_DUAL_SCREEN_AVI_PLAY` 并核对 CPU1 内存。
