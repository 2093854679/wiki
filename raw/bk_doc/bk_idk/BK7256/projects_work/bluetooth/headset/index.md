# 耳机[](#id1 "永久链接至标题")

[[English]](../../../../../en/v1.5/projects_work/bluetooth/headset/index.html "../../../../../en/v1.5/projects_work/bluetooth/headset/index.html")


## 1 功能概述[](#id2 "永久链接至标题")

> 用于手机、拨号盘等主设备场景，开启a2dp sink、avrcp ct/tg、ble等feature。


## 2 代码路径[](#id3 "永久链接至标题")

> demo路径：`./projects/bluetooth/headset/main/armino_main.c`
>
> 编译命令：`make bk7256 PROJECT=bluetooth/headset`


## 3 cli 命令[](#cli "永久链接至标题")

> 连接后可以使用cli命令测试avrcp等功能。注意，某些命令是否生效视手机、手机app而定)
>
> |  |  |
> | --- | --- |
> | AT+BT=AVRCP_CTRL,play | 播放 |
> | AT+BT=AVRCP_CTRL,pause | 暂停 |
> | AT+BT=AVRCP_CTRL,next | 下一曲 |
> | AT+BT=AVRCP_CTRL,prev | 上一曲 |
> | AT+BT=AVRCP_CTRL,rewind[,msec] | 快退，可指定时间 |
> | AT+BT=AVRCP_CTRL,fast_forward[,msec] | 快进，可指定时间 |
> | AT+BT=AVRCP_CTRL,vol_up | 音量增加 |
> | AT+BT=AVRCP_CTRL,vol_down | 音量减少 |
> | AT+BT=ENTER_PAIRING_MODE | 进入配对模式 |


## 参考链接[](#id4 "永久链接至标题")

> [API参考:](../../api-reference/bluetooth/index.html "../../api-reference/bluetooth/index.html") 介绍了蓝牙API接口
>
> [开发者指南:](../../developer-guide/bluetooth/index.html "../../developer-guide/bluetooth/index.html") 介绍了蓝牙常用使用场景
>
> [样例演示:](../../examples/bluetooth/index.html "../../examples/bluetooth/index.html") 介绍了蓝牙样例使用和操作
>
> [蓝牙工程:](../../projects_work/bluetooth/index.html "../../projects_work/bluetooth/index.html") 介绍了蓝牙相关工程
