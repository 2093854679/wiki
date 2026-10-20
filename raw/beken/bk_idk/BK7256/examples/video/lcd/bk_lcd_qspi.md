---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/examples/video/lcd/bk_lcd_qspi.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="lcd-qspi-display"></a>

# LCD QSPI Display

<a id="id1"></a>

## 1、功能概述

> lcd qspi demo展示了LCD QSPI接口的API使用，主要包括显示纯色的demo以及从SDCard读取一张RGB888的图片并显示的demo。

<a id="id2"></a>

## 2、代码路径

> Demo的示例代码详见: `\components\demos\media\lcd\lcd_qspi\lcd_qspi_demo.c`
>
> demo运行依赖的宏配置:
>
> | Name | Description | File | value |
> | --- | --- | --- | --- |
> | CONFIG\_QSPI | 配置QSPI的驱动使能 | `\middleware\soc\bk7256\bk7256.defconfig` | y |
> | CONFIG\_LCD\_QSPI | 配置LCD QSPI驱动使能 | `\middleware\soc\bk7256\bk7256.defconfig` | y |
> | CONFIG\_LCD\_QSPI\_SH8601A  CONFIG\_LCD\_QSPI\_ST77903 | 配置LCD QSPI的屏幕使能 | `\middleware\soc\bk7256\bk7256.defconfig` | y |
> | CONFIG\_LCD\_QSPI\_TEST | 配置LCD QSPI DEMO使能 | `\middleware\soc\bk7256\bk7256.defconfig` | y |
>
> demo运行依赖的其他库和驱动:
>
> > - DMA2D DMA2D模块驱动
> > - QSPI QSPI模块驱动

<a id="cli"></a>

## 3、cli命令简介

支持的命令如下:

> 1、lcd\_qspi\_display\_pure\_color\_test
> :   - 功能说明
>       :   用来测试lcd qspi显示纯色的功能。
>     - 命令格式
>       :   lcd\_qspi\_display\_pure\_color\_test start param1
>
>           | Param | value |
>           | --- | --- |
>           | param1 | 屏幕型号  选择：sh8601a/st77903 |
>     - 测试用例
>       :   测试sh8601a屏幕显示纯色：`lcd_qspi_display_pure_color_test start sh8601a`
>
> 2、lcd\_qspi\_display\_picture\_test
> :   - 功能说明
>       :   用来测试lcd qspi显示图片的功能。
>     - 命令格式
>       :   lcd\_qspi\_display\_picture\_test start param1 param2
>
>           | Param | value |
>           | --- | --- |
>           | param1 | 文件名 |
>           | param2 | 屏幕型号 选择: sh8601a/st77903 |
>     - 测试用例
>       :   1.挂载SDCard：`fatfstest M 1`。
>
>           2.测试sh8601a屏幕显示图片：`lcd_qspi_display_picture_test start beken.rgb sh8601a`。
