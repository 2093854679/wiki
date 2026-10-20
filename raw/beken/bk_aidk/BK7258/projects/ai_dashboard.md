---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_aidk/bk7258/zh_CN/v2.0.1/projects/ai_dashboard/index.html
sdk_family: bk_aidk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="ai-dashboard"></a>

# AI Dashboard

<a id="id1"></a>

## 1\. 简介

> 本工程是基于beken\_genie工程，实现的单屏显示工程。该工程包含的功能与beken\_genie工程的功能一致，区别是beken\_genie工程是双屏显示，本工程是单屏显示，本工程采用的是360x360分辨率的QSPI LCD，屏幕IC型号为ST77916。
>
> 详细说明和介绍请参考：[博通集成精灵AI（Beken\_Genie）工程](beken_genie.md)

<a id="id2"></a>

## 2\. 代码说明

> - 1、相比于beken\_genie工程，本工程需要配置QSPI LCD的相关宏，具体如下所示：
>
> |  |  |  |  |
> | --- | --- | --- | --- |
> | Kconfig | CPU | Format | Value |
> | CONFIG\_LCD\_QSPI\_ST77916 | CPU1 | bool | y |
> | CONFIG\_LCD\_BACKLIGHT\_GPIO | CPU1 | int | 25 |
> | CONFIG\_LCD\_QSPI\_RESET\_PIN | CPU1 | int | 45 |
> | CONFIG\_LCD\_QSPI\_ID | CPU1 | int | 1 |
> | CONFIG\_LCD\_QSPI\_DEVICE\_NUM | CPU1 | int | 1 |
> | CONFIG\_SINGLE\_SCREEN\_AVI\_PLAY | CPU0 \& CPU1 | bool | y |
> | CONFIG\_DUAL\_SCREEN\_AVI\_PLAY | CPU0 \& CPU1 | bool | n |
>
> 其中，`CONFIG_LCD_BACKLIGHT_GPIO` 、 `CONFIG_LCD_QSPI_RESET_PIN` 和 `CONFIG_LCD_QSPI_ID` 这三个宏需要在工程的Kconfig.projbuild文件中进行定义才能生效。
>
> - 2、该工程的代码与beken\_genie工程的代码主要差异点是 `avi_play.c` 文件，可通过比较该文件查看具体差异，具体如下：
>
>   > - 传入的lcd ppi和name需要修改为所使用的lcd分辨率和名称；
>   > - lvgl初始化中传入函数lv\_vendor\_init()中的lcd\_hor\_res和lcd\_ver\_res两个参数需要设置为LCD的宽和高；
>   > - img\_dsc结构体中的宽度和高度需要设置为资源文件的宽度和高度，资源文件的宽度和高度可在调用函数bk\_avi\_play\_open()之后获取到；
>   > - 函数bk\_avi\_play\_open()中的资源文件名称需要修改为所用的资源文件名称，且第三个参数需要传入0，不进行图像分割操作。
> - 3、此外，由于单屏的分辨率更大，需要消耗更多的内存，注意CPU1上的SRAM内存分配。

<a id="id3"></a>

## 3\. 问题\&回答

Q：本工程使用的LCD可以替换成其他的屏幕吗？

A：可以支持不同型号的QSPI/SPI LCD，但屏幕显示动画或视频的分辨率必须满足宽度是16的倍数，高度是8的倍数，例如：该工程中的LCD分辨率是360x360，建议资源文件的分辨率修改为352x352或者352x360。

Q：如何理解函数bk\_avi\_play\_open()的第三个参数？

A：第三个参数表示图像是否需要分割为连续地址，对于本工程来说，该参数需要设置为0。
