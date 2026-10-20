---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7236/zh_CN/v2.0.1/controller-guide/demo_project.html
sdk_family: bk_controller
chip: BK7236
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="demo"></a>

# demo工程介绍

<a id="id1"></a>

## **demo工程介绍**

目前Controller SDK中主要包含两个demo工程，分别是controller\_4wire和controller。

- controller\_4wire工程，编译命令：make bk7236 PROJECT\=wifi/controller\_4wire
- controller工程，编译命令：make bk7236 PROJECT\=wifi/controller

备注

controller\_4wire工程配置： **4线SDIO，1.8V I/O**； controller工程配置： **1线SDIO，3.3V I/O**。

<a id="id2"></a>

## **demo工程配置**

demo工程中有两个关键配置需要关注，分别是I/O相关配置和工程相关配置，我们以wifi/controller demo工程为例介绍相关配置

<a id="i-o"></a>

### I/O相关配置

IO相关配置主要子如下两个文件中配置： `/bk_idk_controller/project/wifi/controller/config/bk7236/usr_gpio_config.h`
文件实现GPIO功能配置和关键I/O定义，比如关键的SDIO中断I/O、主控上电控制I/O等

![关键I/O配置](../../../_assets/3f89181e44d11b3e63f0-usr_gpio_cfg.png)

`/bk_idk_controller/project/wifi/controller/main/cifd_gpio_config.h` 文件定义demo工程功能I/O定义，比如按键和电量检测等

![工程I/O配置](../../../_assets/97a0723da62beea904cd-cifd_gpio_config.png)

重要

*务必根据实际硬件情况配置I/O，controller工程为单线SDIO配置，SDIO D1/D2/D3被占用*
*如果使用4线SDIO，请编译controller\_4wire工程*

<a id="id3"></a>

### 工程相关配置

工程相关配置通过 `/bk_idk_controller/project/wifi/controller/config/bk7236/config` 文件实现
该文件主要配置相关宏，其中比较重要的是SDIO 1线/4线配置和I/O供电电压是1.8V/3.3V配置。
CONFIG\_GPIO\_1V8\_EN\=y用来能1.8V I/O供电，CONFIG\_SDIO\_4LINES\_EN\=y用来使能4线SDIO。

![config配置](../../../_assets/7b174234ac685de0cd0e-controller_config.png)
