---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/examples/audio/AEC_demo.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="aec-demo"></a>

# AEC回声消除，向量测试demo

<a id="id1"></a>

## 1 功能概述

> 回声消除库的主要作用是消除语音通话场景中的回声，确保高质量的语音通话，同时也有降噪和调节音量的功能。

<a id="id2"></a>

## 2 代码路径

> demo路径: `\components\demos\media\audio\aec`
>
> AEC库API接口的详细说明请参考同网页: `/api-reference/multi_media/bk_aec.html`

<a id="cli"></a>

## 3 cli命令简介

demo支持的命令如下表:

| Command | Description |
| --- | --- |
| aec\_test | 运行AEC向量测试demo |

demo运行依赖的宏配置:

| Name | Description | File | value |
| --- | --- | --- | --- |
| CONFIG\_AUDIO\_AEC | 配置AEC是否编译为库 | `\properties\soc\bk7256\bk7256.defconfig` | y |
| CONFIG\_AUDIO\_TEST | 配置demo是否生效 | `\middleware\soc\bk7256\bk7256.defconfig` | y |

demo运行依赖的库和驱动:
:   - libaec.a AEC回声消除库
    - SD SDcard及文件系统驱动

<a id="id3"></a>

## 4 演示介绍

demo执行的步骤如下:

> 1.准备测试需要的音频文件
> :   - 将demo路径下提供的需要回声消除降噪的mic原始音频文件 `mic.pcm` 和对应的参考信号 `ref.pcm` 文件保存在TF卡根目录
>
> 2.挂载TF卡
> :   - Uart发送AT指令 `fatfstest M 1` 挂载TF卡
>
> 3.执行测试
> :   - Uart发送AT指令 `aec_test` 执行测试，并输出回声消除后的音频文件 `out.pcm`

执行测试指令，case的工作流程如下图所示：

<a id="id5"></a>
![aec_demo软件流程](../../../../_assets/98f111344ad680130711-aec_demo_flow.png)


Figure 1\. aec demo flow chart

<a id="id4"></a>

## 5 详细配置及说明

重要

注意事项:
:   - 1.AEC算法需要buffer约二十多kByte，初始化前需要分配AECContext的内存;
    - 2.算法参数的调节使用 `aec_ctrl` 接口。
