---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/examples/video/qrcodegen.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="qr-code-generator"></a>

# QR-Code Generator

<a id="id1"></a>

## 1、功能概述

> qrcodegen demo主要介绍了二维码生成的API使用，该demo主要是生成二维码并将生成的二维码保存到SDCard中，最后通过图片查看软件打开保存的文件。

<a id="id2"></a>

## 2、代码路径

> Demo具体的示例代码详见: `\components\demos\media\lcd\qrcodegen\qrcodegen_demo.c`
>
> demo运行依赖的宏配置:
>
> | Name | Description | File | value |
> | --- | --- | --- | --- |
> | CONFIG\_QRCODEGEN\_TEST | 配置二维码生成demo使能 | `\middleware\soc\bk7256\bk7256.defconfig` | y |

<a id="cli"></a>

## 3、cli命令简介

支持的命令如下:

> 1、qrcodegen\_text\_test
> :   - 功能说明
>       :   用来测试二维码生成的功能。
>     - 命令格式
>       :   qrcodegen\_text\_test param1 param2
>
>           | Param | value |
>           | --- | --- |
>           | param1 | 保存的文件名 |
>           | param2 | 规模倍数  选择：1/2/3/4…… |
>     - 测试用例
>       :   1.挂载SDCard：`fatfstest M 1`。
>
>           2.测试二维码生成：`qrcodegen_text_test qr1.rgb 4`。

<a id="demo"></a>

## 4、demo说明

> - 查看保存的图片时数据类型设置为RGB565；
> - 分辨率设置为116 \* 116；
> - demo中默认配置了根据text内容长度自动生成二维码的边长，可根据输出的log：`size =` 获取，可自由更改text内容进行测试，当前size默认输出为21；
> - demo中默认配置了边界长度为4，所以实际的二维码长度为 `size + 4 * 2`，再根据输入的扩大倍数即可得出最终的二维码边长。

## 模块导航

- [简介](../../introduction.md)
- [快速入门](../../get-started.md)
- [H/W 参考手册](../../hw-reference.md)
- [API 参考手册](../../api-reference.md)
- [开发者指南](../../developer-guide.md)
- [OS 相关参考](../../os.md)
- [样例演示](../../examples.md)
- [视频](../video.md)
- [LCD Display](lcd.md)
- [Camera](camera.md)
- [DMA2D](dma2d.md)
- [音频](../audio.md)
- [蓝牙](../bluetooth.md)
- [门铃](../doorbell.md)
- [命令](../cli.md)
- [外设](../peripheral.md)
- [平台](../platform.md)
- [LVGL](../lvgl/lvgl.md)
- [尚云P2P](../cs2_p2p.md)
- [wifi](../wifi.md)
- [VND_CAL](../vnd_cal/vnd_cal.md)
- [应用开发](../../application.md)
- [工程](../../projects_work.md)
- [产品解决方案](../../projects.md)
- [开发与贡献代码流程](../../process.md)
- [云平台](../../clounds.md)
- [版本](../../release-notes.md)
