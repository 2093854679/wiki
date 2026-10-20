---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/examples/cli/saradc/saradc.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="saradc-cli"></a>

# SARADC Cli

<a id="id1"></a>

## 1、功能概述

> 为了方便验证SARADC功能，SDK提供了SARADC CMD示例。SARADC CMD命令以 `adc_test` 开头，后接具体命令和参数。执行命令，返回SARADC的采样值。

<a id="id2"></a>

## 2、代码路径

> 路径: `\components\bk_cli\cli_adc.c`

<a id="cli"></a>

## 3、cli命令简介

支持的命令如下:

> 1.adc\_test
> :   - 功能说明
>       :   用来设置SARADC，获取采样值
>     - 命令格式
>       :   adc\_test param1 adc\_example
>
>           |  |  |
>           | --- | --- |
>           | param1 | adc channel |
>     - 测试用例
>       :   设置SARADC channel 3参数：`adc_test 3 adc_example`

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
- [触摸](../touch.md)
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
