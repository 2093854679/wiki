---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/examples/audio/G711A_demo.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="g711a-demo"></a>

# G711A编解码，向量测试demo

<a id="id1"></a>

## 1 功能概述

> 对指定的 `xx.pcm` 音频文件进行G711A的编解码，并输出编解码处理后的音频到 `xx.pcm` 文件

<a id="id2"></a>

## 2 代码路径

> demo路径: `\components\demos\media\audio\g711`
>
> G711A库API接口的详细说明请参考同网页: `/api-reference/multi_media/bk_aec.html`

<a id="cli"></a>

## 3 cli命令简介

demo支持的命令如下表:

| Command | Description |
| --- | --- |
| g711\_encoder\_test | 运行G711编码测试demo |
| g711\_decoder\_test | 运行G711解码测试demo |

demo运行依赖的宏配置:

| Name | Description | File | value |
| --- | --- | --- | --- |
| CONFIG\_AUDIO\_G711 | 配置G711是否编译为库 | `\properties\soc\bk7256\bk7256.defconfig` | y |
| CONFIG\_AUDIO\_G711\_TEST | 配置demo是否生效 | `\middleware\soc\bk7256\bk7256.defconfig` | y |

demo运行依赖的库和驱动:
:   - libg711.a G711编解码库
    - SD SDcard及文件系统驱动

<a id="id3"></a>

## 4 演示介绍

demo执行的步骤如下:

> 1.准备测试需要的音频文件
> :   - 将demo路径下提供的用于编码测试的音频文件 `mic_data.pcm` 和用于解码测试的音频文件 `encoder_mic_data.pcm` 保存在TF卡根目录
>
> 2.挂载TF卡
> :   - Uart发送AT指令 `fatfstest M 1` 挂载TF卡
>
> 3.执行编码测试
> :   - Uart发送AT指令 `g711_encoder_test` 执行测试，并输出编码后的音频文件 `out_encoder_data.pcm` 至TF卡根目录
>
> 4.执行解码测试
> :   - Uart发送AT指令 `g711_decoder_test` 执行测试，并输出解码后的音频文件 `out_decoder_data.pcm` 至TF卡根目录

<a id="id4"></a>

## 5 详细配置及说明

重要

注意事项:
:   - 1.G711编解码库也支持G711U编解码，测试demo演示的是G711A编解码;
    - 2.G711编解码的音频信号是单声道16bit的。
