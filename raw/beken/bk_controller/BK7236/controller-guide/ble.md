---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7236/zh_CN/v2.0.1/controller-guide/ble.html
sdk_family: bk_controller
chip: BK7236
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="ble"></a>

# ble使用介绍

<a id="id1"></a>

## 1 功能概述

一般来讲，在wifi controller这个SDK里，ble主要功能是配网(开发板连接wifi ap)，其功能实现依赖于ble sdk与上层app的关系，有两种模式

> - 1.标准hci模式
> - 2.host controller all in one模式

<a id="hci"></a>

### 1.1 标准hci模式

蓝牙app、host运行在主控端，通过标准hci(通路可以是UART)与开发板的蓝牙controller交互。这种模式开发板几乎不参与任何业务逻辑，完全受主控的控制。

开启方式：

> - CONFIG\_BLUETOOTH\=y
> - CONFIG\_BT\=n
> - CONFIG\_BTDM\_CONTROLLER\_ONLY\=y

主要流程：调用bk\_ble\_enable\_uart\_controller\_only，设置对应的UART参数即可

示例工程： `projects/wifi/controller`

<a id="host-controller-all-in-one"></a>

### 1.2 host controller all in one模式

蓝牙app、host、controller都运行在开发板，app负责开启广播、设置gatt数据库、收发对端数据，主控app再通过UART、USB、PCIE等方式与蓝牙app交互。这种模式主控和开发板都需要编写业务逻辑。

开启方式：

> - CONFIG\_BLUETOOTH\=y
> - CONFIG\_BT\=n
> - CONFIG\_BTDM\_CONTROLLER\_ONLY\=n

蓝牙app流程：请参考 [beken armino idk蓝牙配网示例工程说明](../../../bk_idk/BK7236/projects/bluetooth/provisioning/provisioning.md)

其他蓝牙用法：请参考 [beken armino idk ble api接口说明](../../../bk_idk/BK7236/api-reference/bluetooth/ble.md)

示例工程:

> - `projects/bluetooth/provisioning`

测试方法：

> - 1. `bluetooth_demo on` 开启蓝牙
> - 2. `bluetooth_demo test` 开启广播

重要

- 主控app与蓝牙app的交互协议需要用户自行定义
- 请不要将armino idk的配网与本sdk的配网工程弄混，二者有一定区别

## 模块导航

- [简介](../introduction.md)
- [快速入门](../get-started.md)
- [硬件设计指南](../hw-reference.md)
- [软件方案介绍](../sw-detail.md)
- [主控开发适配指南](../host-guide.md)
- [Controller开发指南](../controller-guide.md)
- [SDK下载及介绍](cntrl_sdk.md)
- [编译环境搭建](sdk_build.md)
- [demo工程介绍](demo_project.md)
- [创建新工程](new_project.md)
- [低功耗开发指南](low_power.md)
- [按键开发](button.md)
- [自定义Event发送](event_notify.md)
- [常见问题解答](../frequently-asked-questions.md)
