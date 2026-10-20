---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/examples/video/lcd/bk_lcd_display_jpeg.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="lcd-rgb-display-jpeg"></a>

# LCD RGB Display JPEG

<a id="id1"></a>

## 1、功能概述

> lcd rgb display jpeg demo 实现了RGB屏幕实时显示dvp camera jpeg 数据的功能。

<a id="id2"></a>

## 2、代码路径

> - Demo 涉及的模块AP接口的详细说明请参考同网页: `/api-reference/multi_media/bk_display.html`
> - Demo 具体的示例代码详见: `\components\demos\media\lcd\lcd_rgb`

demo运行依赖的宏配置:

| Name | Description | File | value |
| --- | --- | --- | --- |
| CONFIG\_LCD | 配置LCD功能 | `\middleware\soc\bk7256\bk7256.defconfig` | y |
| CONFIG\_LCD\_TEST | LCD DEMO使能 | `\middleware\soc\bk7256\bk7256.defconfig` | y |

demo运行依赖的库和驱动:
:   - LCD LCD模块驱动
    - JPEG JPEG模块驱动

<a id="id3"></a>

## 3、演示介绍

demo执行的步骤如下:

> 1、Demo运行硬件环境:
> :   1. BK7256开发板以及下载固件的环境
>     2. 配套RGB接口的LCD屏幕
>     3. 需要提供稳压电源供23V电压给RGB LCD
>     4. 可以接收串口命令的串口工具，波特率为115200.
>
> 1.执行测试
> :   - Uart发送AT指令 \`\` lcd\_rgb\_jpeg\=480p ,25\`\` 执行测试
>
> 3.停止测试
> :   - Uart发送AT指令 `lcd_rgb_close=jpeg` 停止测试

<a id="lcd"></a>

## 5、LCD 代码实现

LCD显示JPEG图像软件实现流程大致可以分为6个步骤：

> 1. 配置RGB LCD
> 2. 配置JPEG\_ENC和camera
> 3. 配置JPEG\_DEC
> 4. 处理JPEG\_ENC完成一帧压缩的中断回调
> 5. 处理JPEG\_DEC完成一帧解压的中断回调
> 6. 配置LCD 刷屏的数据地址，并使能传输

## 模块导航

- [简介](../../../introduction.md)
- [快速入门](../../../get-started.md)
- [H/W 参考手册](../../../hw-reference.md)
- [API 参考手册](../../../api-reference.md)
- [开发者指南](../../../developer-guide.md)
- [OS 相关参考](../../../os.md)
- [样例演示](../../../examples.md)
- [视频](../../video.md)
- [LCD Display](../lcd.md)
- [LCD 8080 Display](bk_lcd_8080.md)
- [LCD RGB YUV Display](bk_lcd_display_yuv.md)
- [LCD 显示一张jpeg图片](bk_picture_display.md)
- [LCD QSPI Display](bk_lcd_qspi.md)
- [Camera](../camera.md)
- [DMA2D](../dma2d.md)
- [QR-Code Generator](../qrcodegen.md)
- [音频](../../audio.md)
- [蓝牙](../../bluetooth.md)
- [门铃](../../doorbell.md)
- [命令](../../cli.md)
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
