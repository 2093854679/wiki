---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/examples/video/lcd/bk_lcd_8080.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="lcd-8080-display"></a>

# LCD 8080 display

<a id="id1"></a>

## 1、功能概述

> lcd 8080 demo 展示了LCD 8080 接口的API使用

<a id="id2"></a>

## 2、代码路径

> - Demo 涉及的模块AP接口的详细说明请参考同网页: `/api-reference/multi_media/bk_display.html`
> - Demo 具体的示例代码详见: `\components\demos\media\lcd\lcd_8080`
> - Demo 功能会用到DMA2D功能,DMA2D代码使用详见: `/components/demos/media/dma2d`

demo运行依赖的宏配置:

| Name | Description | File | value |
| --- | --- | --- | --- |
| CONFIG\_LCD | 配置LCD功能 | `\middleware\soc\bk7256\bk7256.defconfig` | y |
| CONFIG\_LCD\_TEST | LCD DEMO使能 | `\middleware\soc\bk7256\bk7256.defconfig` | y |

demo运行依赖的其他库和驱动:

> - DMA2D DMA2D模块驱动
> - LCD\_Display LCD模块驱动

<a id="cli"></a>

## 3、cli命令简介

> 1、Demo运行硬件环境:
> :   - BK7256开发板以及下载固件的环境
>     - 配套8080 接口的LCD屏幕
>     - 可以接收串口命令的串口工具，波特率为115200.
>     - RGB565格式 红色-0xf800, 绿色-0xffe0, 蓝色-0x001f, 黄色-0xffe0
>
> 2、刷全屏为红色
> :   - lcd\_8080\=cpu\_fill,0x60000000,0xf800f800
>     - lcd\_8080\=init,4
>     - lcd\_8080\=frame\_disp,0x60000000
>
> 3、刷纯色
> :   - 初始化：lcd\_8080\=init,4
>     - 全屏红色：lcd\_8080\=lcd\_fill\_color,0xf800,0,0,320,480,0x60000000
>     - 局部蓝色：lcd\_8080\=lcd\_fill\_color,0x001f,10,10,200,200,0x60000000
>     - 局部黄色：lcd\_8080\=lcd\_fill\_color,0xffe0,50,50,102,102,0x60000000
>
> 4、局部刷图片,图片位置在0x60000000
> :   - 初始化：lcd\_8080\=init,4
>     - 全屏红色：lcd\_8080\=lcd\_fill\_data,20,20,200,300,0x60000000
>
> 5、MCU屏幕显示dvp摄像头320\*480 像素的图片
> :   - lcd\_8080\_yuv\=4
>
> 6、MCU屏幕显示dvp摄像头640\*480 像素的图片
> :   - lcd\_8080\_yuv\_partical\=4
>
> 7、停止测试
> :   - Uart发送AT指令 `lcd_8080=close` 停止测试
