---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/examples/video/lcd/bk_picture_display.html
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

> 显示一张JPEG图片到mcu/rgb LCD屏幕。

<a id="id2"></a>

## 2、代码路径

> - Demo 涉及的模块AP接口的详细说明请参考同网页: `/api-reference/multi_media/bk_display.html`
> - Demo 具体的示例代码详见: `\components\demos\media\lcd\picture_display`

demo运行依赖的宏配置:

| Name | Description | File | value |
| --- | --- | --- | --- |
| CONFIG\_LCD | 配置LCD功能 | `\middleware\soc\bk7256\bk7256.defconfig` | y |
| CONFIG\_LCD\_TEST | LCD DEMO使能 | `\middleware\soc\bk7256\bk7256.defconfig` | y |

demo运行依赖的库和驱动:
:   - LCD LCD模块驱动
    - JPEG JPEG模块驱动
    - SD 模块驱动

<a id="cli"></a>

## 3、cli命令简介

> 从SD卡读取一张jpeg图片显示到屏幕上,参数3可以修改使用的屏幕大小，比如320X480,480X800.
> \- \`\` fatfstest M 1\`\`
> \- \`\` lcd\=file\_display,filename,480X272\`\`

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
- [LCD RGB JPEG Display](bk_lcd_display_jpeg.md)
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
