---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/controller-guide/bluetooth_guide/bk_ble.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="ble"></a>

# 低功耗蓝牙(BLE)

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

蓝牙app流程：请参考 [beken armino idk蓝牙配网示例工程说明](../../project-example/bluetooth/provisioning.md)

其他蓝牙用法：请参考 [蓝牙API](../api-reference/bluetooth.md)

示例工程:

> - `projects/bluetooth/provisioning`

测试方法：

> - 1. `bluetooth_demo on` 开启蓝牙
> - 2. `bluetooth_demo test` 开启广播

重要

- 主控app与蓝牙app的交互协议需要用户自行定义
- 请不要将armino idk的配网与本sdk的配网工程弄混，二者有一定区别

## 模块导航

- [简介](../../introduction.md)
- [快速入门](../../get-started.md)
- [硬件开发指南](../../hw-reference.md)
- [Controller软件开发指南](../../controller-guide.md)
- [软件架构](../sw_arch.md)
- [配置与构建](../config_and_build.md)
- [API参考手册](../api-reference.md)
- [平台开发指南](../platform_guide.md)
- [Wi-Fi开发指南](../wifi_guide.md)
- [蓝牙开发指南](../bluetooth_guide.md)
- [经典蓝牙(BT)](bk_bt.md)
- [网络协议开发指南](../network_protocol_guide.md)
- [低功耗开发指南](../low_power_guide.md)
- [外设开发指南](../peripheral_guide.md)
- [主控平台软件开发指南](../../host-guide.md)
- [工程与示例](../../project-example.md)
- [开发工具介绍](../../dev-tool.md)
- [调测指导](../../debug-guide.md)
- [产测指导](../../production-test-guide.md)
- [常见问题解答](../../faq.md)
