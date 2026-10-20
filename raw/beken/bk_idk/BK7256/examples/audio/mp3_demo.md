---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/examples/audio/mp3_demo.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="mp3-demo"></a>

# MP3 demo

<a id="id1"></a>

## 1、功能概述

> 对指定的 `xx.mp3` 音频文件进行MP3解码，并输出解码后的音频到 `xx.pcm` 文件
> 对指定的 `xx.mp3` 音频文件进行MP3解码，并输出解码后的音频通过Audio DAC进行播放

<a id="id2"></a>

## 2、代码路径

> demo路径: `\components\demos\media\audio\mp3`
>
> MP3库API接口的详细说明请参考同网页: `/api-reference/multi_media/bk_mp3.html`

<a id="cli"></a>

## 3、cli命令简介

demo支持的命令如下表:

| Command | Description |
| --- | --- |
| mp3\_decode\_test | MP3解码并将解码后的音频存储到sdcard |
| mp3\_play\_test | MP3解码并进行实时播放 |

demo运行依赖的宏配置:

| Name | Description | File | value |
| --- | --- | --- | --- |
| CONFIG\_AUDIO\_MP3\_TEST | 配置demo是否生效 | `\middleware\soc\bk7256\bk7256.deconfig` | y |
| CONFIG\_AUDIO | 配置audio功能是否生效 | `\middleware\soc\bk7256\bk7256.deconfig` | y |
| CONFIG\_AUDIO\_MP3 | 配置helix是否编译为库 | `\properties\soc\bk7256\bk7256.deconfig` | y |

demo运行依赖的库和驱动:
:   - libhelix.a MP3解码库
    - SD SDcard及文件系统驱动

<a id="id3"></a>

## 4、演示介绍

> 1.准备测试需要的音频文件
> :   - 将需要测试的xx.mp3文件保存在SDCARD卡根目录
>
> 2.挂载TF卡
> :   - 串口工具发送指令 `fatfstest M 1` 挂载TF卡
>
> 3.执行解码测试
> :   - 串口工具发送指令 `mp3_decode_test start xx.mp3 xx.pcm` 执行测试，并输出解码后的xx.pcm音频文件至TF卡根目录
>
> 4.执行解码并进行播放测试
> :   - 串口工具发送指令 `mp3_play_test start/stop xx.mp3` 执行测试，可以实时播放或停止播放MP3文件

<a id="id4"></a>

## 5、详细配置及说明

重要

注意事项:
:   - 1.解码后存放PCM数据的buffer分配空间大小需要根据MP3类型进行分配，常见分配大小为1152B或者2304B;
    - 2.MP3解码流程为：MP3DecoderInit —\> MP3FindSyncWord —\> MP3Decode —\> MP3GetLastFrameInfo —\> MP3FreeDecoder
    - 3.MP3的具体使用可完全移植mp3\_demo.c文件中的cli\_mp3\_play\_test\_cmd()的测试demo。
