---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/examples/cli/audio/eq.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="eq-cli"></a>

# EQ Cli

<a id="id1"></a>

## 1、功能概述

> 为了便于验证EQ的功能，为此设计了一个cli CMD，设计思路是设置dance的一系列参数测试均衡效果，当前cli命令是否生效由宏 `CLI_CFG_AUD` 决定，宏控制位置在：`components\bk_cli\cli_config.h` 文件中，该宏是否生效由内部宏 `CONFIG_AUDIO` 和 `CONFIG_AUDIO_TEST` 决定。

<a id="id2"></a>

## 2、代码路径

> 路径：`components\demos\media\audio\aud\aud_cp1.c`

<a id="cli"></a>

## 3、cli命令简介

支持的命令如下:

> 1.aud\_eq\_test
> :   - 功能说明
>       :   用来测试语音Dance均衡功能。
>     - 命令格式
>       :   aud\_eq\_test param1
>
>           | Param | value |
>           | --- | --- |
>           | param1 | start / stop  start：开始  stop ：停止 |
>     - 测试用例
>       :   开始测试：`aud_eq_test start`
>
>           停止测试并释放资源：`aud_eq_test stop`

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
- [AEC](aec.md)
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
