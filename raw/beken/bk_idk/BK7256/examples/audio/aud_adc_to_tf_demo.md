---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/examples/audio/aud_adc_to_tf_demo.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="audio-record-demo"></a>

# Audio record demo

<a id="id1"></a>

## 1、功能概述

> mic采集音频数据并保存为 `xx.pcm` 文件存储至TF卡。

<a id="id2"></a>

## 2、代码路径

> demo路径: `\components\demos\media\audio\aud_intf\demo\aud_intf_demo.c`
>
> Aud\_Intf API接口的详细说明请参考同网页: `/api-reference/multi_media/bk_aud_intf.html`

<a id="cli"></a>

## 3、cli命令简介

demo支持的命令如下表:

| Command | Description |
| --- | --- |
| aud\_intf\_record\_test {init\|start\|pause\|stop\|deinit} xx.pcm | 录音到xx.pcm文件 |

demo运行依赖的宏配置:

| Name | Description | File | value |
| --- | --- | --- | --- |
| CONFIG\_AUDIO | 配置audio功能 | `\middleware\soc\bk7256\bk7256.defconfig` | y |
| CONFIG\_AUDIO\_RISCV\_IP\_V1\_0 | 配置audio ip | `\middleware\soc\bk7256\bk7256.defconfig` | y |
| CONFIG\_AUD\_INTF | 配置aud\_intf使能 | `\middleware\soc\bk7256\bk7256.defconfig` | y |
| CONFIG\_AUD\_INTF\_VER\_NEW | 配置aud\_intf版本使能 | `\middleware\soc\bk7256\bk7256.defconfig` | y |
| CONFIG\_AUD\_INTF\_TEST | 配置demo使能 | `\middleware\soc\bk7256\bk7256.defconfig` | y |
| CONFIG\_AUDIO\_TRANSFER | 配置语音传输使能 | `\middleware\soc\bk7256\bk7256.defconfig` | y |
| CONFIG\_AUD\_TRAS\_MODE\_CPU0 | 配置语音传输模式 | `\middleware\soc\bk7256\bk7256.defconfig` | y |

demo运行依赖的库和驱动:
:   - DMA DMA驱动
    - AUD audio模块驱动
    - Sdcard 模块驱动

<a id="id3"></a>

## 4 演示介绍

demo执行的步骤如下:

> 1.挂载TF卡
> :   - Uart发送AT指令 `fatfstest M 1` 挂载TF卡
>
> 2.准备录音
> :   - Uart发送AT指令 `aud_intf_record_test init xx.pcm` 初始化录音
>
> 3.开始录音
> :   - Uart发送AT指令 `aud_intf_record_test start xx.pcm` 开始录音, 音频会保存在TF卡的根目录文件 `xx.pcm` 中
>
> 4.暂停录音
> :   - Uart发送AT指令 `aud_intf_record_test pause xx.pcm` 暂停录音
>
> 5.恢复录音
> :   - Uart发送AT指令 `aud_intf_record_test start xx.pcm` 恢复录音
>
> 6.停止录音
> :   - Uart发送AT指令 `aud_intf_record_test stop xx.pcm` 停止录音
>
> 7.结束录音
> :   - Uart发送AT指令 `aud_intf_record_test deinit xx.pcm` 结束录音, 关闭录音文件, 注销录音通路

<a id="id4"></a>

## 5、详细配置及说明

备注

- 1.执行此demo前请确保tf卡可正常使用;
- 3.此demo源码较多, 所以就不在此处展开说明了，请参考源码;
