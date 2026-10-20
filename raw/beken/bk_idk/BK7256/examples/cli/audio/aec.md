---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/examples/cli/audio/aec.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="aec-cli"></a>

# AEC Cli

<a id="id1"></a>

## 1、功能概述

> 为了便于验证AEC回声消除相关的功能，为此设计了一系列cli CMD，同时也是回声消除功能场景demo，供客户参考使用。

<a id="id2"></a>

## 2、代码路径

> 路径: `components\demos\media\audio\aec\aec_demo.c`

<a id="cli"></a>

## 3、cli命令简介

支持的命令如下:

> 1.aec\_test
> :   - 功能说明
>       :   用来测试回声消除功能。
>     - 命令格式
>       :   aec\_test
>     - 测试用例
>       :   对TF卡中的 `mic.pcm和ref.pcm` 进行回声消除，并输出至 `out.pcm` ：`aec_test`

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
- [AUDIO](audio.md)
- [EQ](eq.md)
- [G711](g711.md)
- [MP3](mp3.md)
- [SBC_DEC](sbc_dec.md)
- [I2S](i2s.md)
- [视频](../video.md)
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
