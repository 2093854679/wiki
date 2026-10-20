---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/projects_work/media/audio_player/index.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="audio-player"></a>

# Audio Player

<a id="id1"></a>

## 1 功能概述

> 本工程展示了网络音乐播放器的功能，主要实现了网络音乐下载及播放、暂停、继续播放、设置音量、上一曲及下一曲的功能。

<a id="id2"></a>

## 2 代码路径

> demo路径：`./projects/media/audio_player/main/app_main.c`
>
> 编译命令：`make bk7256 PROJECT=media/audio_player`

<a id="cli"></a>

## 3 cli命令简介

> 本工程首先需要发送命令 `sta {ssid} {password}` 连接可用的网络，其余功能的命令如下所示：
>
> |  |  |
> | --- | --- |
> | audio\_player start | 开始播放 |
> | audio\_player pause | 暂停播放 |
> | audio\_player play | 继续播放 |
> | audio\_player {volume\_value} | 设置音量 |
> | audio\_player last | 上一曲 |
> | audio\_player next | 下一曲 |

其中，音量值的设置范围为0x00\~0x3F，当前音量默认设置为0x2D。

## 模块导航

- [简介](../../introduction.md)
- [快速入门](../../get-started.md)
- [H/W 参考手册](../../hw-reference.md)
- [API 参考手册](../../api-reference.md)
- [开发者指南](../../developer-guide.md)
- [OS 相关参考](../../os.md)
- [样例演示](../../examples.md)
- [应用开发](../../application.md)
- [工程](../../projects_work.md)
- [蓝牙(Bluetooth)工程](../bluetooth.md)
- [多媒体工程(Multi-media)工程](../media.md)
- [doorbell](doorbell.md)
- [图形界面(LVGL)工程](../lvgl.md)
- [第三方工程](../thirdparty.md)
- [Wi-Fi 工程](../wifi.md)
- [产品解决方案](../../projects.md)
- [开发与贡献代码流程](../../process.md)
- [云平台](../../clounds.md)
- [版本](../../release-notes.md)
