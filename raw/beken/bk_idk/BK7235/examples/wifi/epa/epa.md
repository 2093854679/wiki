---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7235/zh_CN/v1.5/examples/wifi/epa/epa.html
sdk_family: bk_idk
chip: BK7235
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="epa"></a>

# EPA

<a id="id1"></a>

## 1、功能概述

> 为了方便验证EPA功能，SDK提供了打开EPA功能的宏开关，将EPA\_ENABLE\_FLAG置为1，打开EPA功能。

<a id="id2"></a>

## 2、代码路径

> 路径: `\middleware\boards\bk7235\vnd_cal\vnd_cal.c`

<a id="id3"></a>

## 3、EPA配置简介

1. 修改默认晶体值

> - 外置EPA方案，需要根据客户的板子调整晶体值，使频偏在-20ppm到20ppm内，将此时对应的晶体值給vnd\_cal.c中被EPA\_ENABLE\_FLAG宏包着的默认晶体值DEFAULT\_TXID\_XTAL

2. 修改功率表

> - 外置EPA方案，需要根据客户的板子调整被宏EPA\_ENABLE\_FLAG包着的gtxpwr\_tab\_def\_b，gtxpwr\_tab\_def\_g，gtxpwr\_tab\_def\_n\_40，gtxpwr\_tab\_def\_ble默认功率表

## 模块导航

- [简介](../../../introduction.md)
- [快速入门](../../../get-started.md)
- [H/W 参考手册](../../../hw-reference.md)
- [API 参考手册](../../../api-reference.md)
- [开发者指南](../../../developer-guide.md)
- [OS 相关参考](../../../os.md)
- [样例演示](../../../examples.md)
- [视频](../../video.md)
- [蓝牙](../../bluetooth.md)
- [Command Line](../../cli.md)
- [外设](../../peripheral.md)
- [平台](../../platform.md)
- [wifi](../../wifi.md)
- [VND_CAL](../../vnd_cal/vnd_cal.md)
- [应用开发](../../../application.md)
- [产品解决方案](../../../projects.md)
- [开发与贡献代码流程](../../../process.md)
- [云平台](../../../clounds.md)
- [版本](../../../release-notes.md)
