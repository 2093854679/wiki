---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/projects_work/bluetooth/headset/index.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 耳机

<a id="id2"></a>

## 1 功能概述

> 用于手机、拨号盘等主设备场景，开启a2dp sink、avrcp ct/tg、ble等feature。

<a id="id3"></a>

## 2 代码路径

> demo路径：`./projects/bluetooth/headset/main/armino_main.c`
>
> 编译命令：`make bk7256 PROJECT=bluetooth/headset`

<a id="cli"></a>

## 3 cli 命令

> 连接后可以使用cli命令测试avrcp等功能。注意，某些命令是否生效视手机、手机app而定)
>
> |  |  |
> | --- | --- |
> | AT\+BT\=AVRCP\_CTRL,play | 播放 |
> | AT\+BT\=AVRCP\_CTRL,pause | 暂停 |
> | AT\+BT\=AVRCP\_CTRL,next | 下一曲 |
> | AT\+BT\=AVRCP\_CTRL,prev | 上一曲 |
> | AT\+BT\=AVRCP\_CTRL,rewind\[,msec\] | 快退，可指定时间 |
> | AT\+BT\=AVRCP\_CTRL,fast\_forward\[,msec\] | 快进，可指定时间 |
> | AT\+BT\=AVRCP\_CTRL,vol\_up | 音量增加 |
> | AT\+BT\=AVRCP\_CTRL,vol\_down | 音量减少 |
> | AT\+BT\=ENTER\_PAIRING\_MODE | 进入配对模式 |

<a id="id4"></a>

## 参考链接

> [API参考:](https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/projects_work/api-reference/bluetooth/index.html) 介绍了蓝牙API接口
>
> [开发者指南:](https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/projects_work/developer-guide/bluetooth/index.html) 介绍了蓝牙常用使用场景
>
> [样例演示:](https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/projects_work/examples/bluetooth/index.html) 介绍了蓝牙样例使用和操作
>
> [蓝牙工程:](https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/projects_work/projects_work/bluetooth/index.html) 介绍了蓝牙相关工程

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
- [中控](central.md)
- [多媒体工程(Multi-media)工程](../media.md)
- [图形界面(LVGL)工程](../lvgl.md)
- [第三方工程](../thirdparty.md)
- [Wi-Fi 工程](../wifi.md)
- [产品解决方案](../../projects.md)
- [开发与贡献代码流程](../../process.md)
- [云平台](../../clounds.md)
- [版本](../../release-notes.md)
