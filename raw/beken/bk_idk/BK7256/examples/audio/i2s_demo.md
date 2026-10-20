---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/examples/audio/i2s_demo.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="i2s-demo"></a>

# I2S demo

<a id="id1"></a>

## 1 功能概述

> I2S demo支持不同工作模式下master发送数据和salve接收数据。

<a id="id2"></a>

## 2 代码路径

> demo路径: `\components\demos\media\audio\i2s`
>
> I2S模块API接口的详细说明请参考同网页: `/api-reference/multi_media/bk_i2s.html`

<a id="cli"></a>

## 3 cli命令简介

demo支持的命令如下表:

| Command | Description |
| --- | --- |
| i2s\_master\_test {start\|stop} | 作为master在I2S模式下发送数据 |
| i2s\_slave\_test {start\|stop} | 作为slave在I2S模式下接收数据 |
| pcm\_master\_test {start\|stop} | 作为master在PCM模式下发送数据 |
| pcm\_slave\_test {start\|stop} | 作为slave在PCM模式下接收数据 |
| dtm\_master\_test {start\|stop} | 作为master在DTM\+PCM模式下发送数据 |
| dtm\_slave\_test {start\|stop} | 作为slave在DTM\+PCM模式下接收数据 |
| 2bd\_master\_test {start\|stop} | 作为master在2B\+D模式下发送数据 |
| 2bd\_slave\_test {start\|stop} | 作为slave在2B\+D模式下接收数据 |

demo运行依赖的宏配置:

| Name | Description | File | value |
| --- | --- | --- | --- |
| CONFIG\_I2S | 配置I2S功能使能 | `\middleware\soc\bk7256\bk7256.defconfig` | y |
| CONFIG\_I2S\_TEST | 配置demo是否生效 | `\middleware\soc\bk7256\bk7256.defconfig` | y |

demo运行依赖的库和驱动:
:   - GPIO GPIO驱动
    - DMA DMA驱动

<a id="id3"></a>

## 4 演示介绍

以I2S工作模式的demo为例，demo执行的步骤如下:

> 1.连接两块测试板子
> :   - 使用两块开发板进行测试，一块作为master端，一块作为slave端
>     - 将两块板子的GPIO6和GPIO7引脚互连
>     - 将master端的GPIO8和slave端的GPIO9连接
>     - 将master端的GPIO9和slave端的GPIO8连接
>
> 2.开始slave端测试
> :   - slave端Uart发送AT指令 `i2s_slave_test start` 执行slave角色的I2S功能测试
>
> 3.开始master端测试
> :   - Uart发送AT指令 `i2s_master_test start` 执行master角色的I2S功能测试
>
> 4.停止测试
> :   - 观察串口log打印，待测试完成后，slave和master端分别Uart发送AT指令 `i2s_slave_test stop` 和 `i2s_master_test stop` 停止执行I2S功能测试

<a id="id4"></a>

## 5 详细配置及说明

重要

注意事项:
:   - 1.I2S通讯时master和slave的DIN和DOUT引脚连接要正确，master的DIN和slave的DOUT连接，master的DOUT和slave的DIN连接;
    - 2.master和slave的工作模式要一致;
