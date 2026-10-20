---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/examples/video/lcd/bk_lcd_display_yuv.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="lcd-rgb-display-yuv"></a>

# LCD RGB Display YUV

<a id="id1"></a>

## 1、功能概述

> lcd rgb display yuv demo 实现了RGB屏幕实时显示dvp camera yuv 数据的功能。

<a id="id2"></a>

## 2、代码路径

> - Demo 涉及的模块AP接口的详细说明请参考同网页: `/api-reference/multi_media/bk_display.html`
> - Demo 具体的示例代码详见: `/components/demos/media/lcd/lcd_rgb/lcd_rgb`

| Name | Description | File | value |
| --- | --- | --- | --- |
| CONFIG\_LCD | 配置LCD功能 | `\middleware\soc\bk7256\bk7256.defconfig` | y |
| CONFIG\_LCD\_TEST | LCD DEMO使能 | `\middleware\soc\bk7256\bk7256.defconfig` | y |

demo运行依赖的库和驱动:
:   - DMA DMA驱动
    - LCD LCD模块驱动
    - JPEG JPEG模块驱动

<a id="cli"></a>

## 3、cli命令简介

> 命令针对480\*272 LCD屏幕
>
> > 1\. RGB 屏幕刷红色
> > \- \`\` lcd\_8080\=dma2d\_fill,0x60000000,0xf800\`\`
> > \- \`\` rgb565\_display\=8\`\`
>
> 2、RGB屏幕显示dvp摄像头480\*272 像素的图片
> :   - \`\` lcd\_rgb\_yuv\=480p\`\`
>
> 3、RGB屏幕显示dvp摄像头640\*480 像素的图片
> :   - \`\` lcd\_rgb\_yuv\=480p,0,display\_partical\`\`
>
> 4、RGB屏幕显示720p摄像头480\*272 像素的图片
> :   - \`\` lcd\_rgb\_yuv\=720p,0,display\_partical\`\`
>
> 5、RGB屏幕显示dvp摄像头640\*480 像素的图片
> :   - \`\` lcd\_rgb\_yuv\=480p,0,display\_partical\`\`
>
> 2.停止测试
> :   - Uart发送AT指令 \`\` lcd\_close\=yuv\`\` 停止测试

<a id="lcd"></a>

## 4、LCD 代码实现

LCD显示YUV图像软件实现流程大致可以分为4个步骤：

> 1. 配置RGB LCD
> 2. 配置JPEG\_ENC和camera
> 3. 处理JPEG\_ENC完成一帧压缩的中断回调
> 4. 配置LCD 刷屏的数据地址，并使能传输
