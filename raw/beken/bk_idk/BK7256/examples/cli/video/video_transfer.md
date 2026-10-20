---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/examples/cli/video/video_transfer.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="video-transfer-cli"></a>

# VIDEO\_TRANSFER Cli

<a id="id1"></a>

## 1、功能概述

> 为了便于验证video\_transfer的相关功能，为此设计了一系列的CLI CMD。所有的图传CLI命令以 `video_transfer` 开头，后面接具体命令和参数。如果命令执行成功，则返回 `CMDRSP:OK`。如果命令执行失败，则返回 `CMDRSP:ERROR`。
> 当前命令是否生效是由宏 `CLI_CFG_DVP` 和 `CONFIG_NET_WORK_VIDEO_TRANSFER` 控制, 路径：`components\bk_cli\cli_config.h`。

<a id="id2"></a>

## 2、代码路径

> 路径: `\components\app\net_work\video_demo_main.c`

<a id="cli"></a>

## 3、cli命令简介

支持的命令如下:
:   1.video\_transfer
    :   - 功能说明
          :   开始进行图传测试
        - 命令格式
          :   video\_transfer param1 param2 param3

              |  |  |
              | --- | --- |
              | param1 | video transfer ways: -s: current device as station, connect a softap -a: current device as softap, peer device connect this softap |
              | param2 | ssid: the connect device name |
              | param3 | key: password, this can omit |
        - 测试用例
          :   图传常规测试：`video_transfer -a demo 12345678`

## 模块导航

- [简介](../../../introduction.md)
- [快速入门](../../../get-started.md)
- [H/W 参考手册](../../../hw-reference.md)
- [API 参考手册](../../../api-reference.md)
- [开发者指南](../../../developer-guide.md)
- [OS 相关参考](../../../os.md)
- [样例演示](../../../examples.md)
- [视频](../../video.md)
- [音频](../../audio.md)
- [蓝牙](../../bluetooth.md)
- [门铃](../../doorbell.md)
- [命令](../../cli.md)
- [蓝牙](../bluetooth.md)
- [音频](../audio.md)
- [视频](../video.md)
- [DVP](dvp.md)
- [DOORBELL](doorbell.md)
- [MEDIA](media.md)
- [PSRAM](psram.md)
- [VIDEO AT CMD](video_at.md)
- [触摸](../touch.md)
- [saradc](../saradc/saradc.md)
- [flashdb](../flashdb/flashdb.md)
- [外设](../../peripheral.md)
- [平台](../../platform.md)
- [LVGL](../../lvgl/lvgl.md)
- [尚云P2P](../../cs2_p2p.md)
- [wifi](../../wifi.md)
- [VND_CAL](../../vnd_cal/vnd_cal.md)
- [应用开发](../../../application.md)
- [工程](../../../projects_work.md)
- [产品解决方案](../../../projects.md)
- [开发与贡献代码流程](../../../process.md)
- [云平台](../../../clounds.md)
- [版本](../../../release-notes.md)
