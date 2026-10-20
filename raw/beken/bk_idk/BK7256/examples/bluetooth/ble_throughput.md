---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/examples/bluetooth/ble_throughput.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="ble"></a>

# ble吞吐

<a id="id1"></a>

## 概述

本示例介绍如何通过两块开发板测试双板BLE吞吐速率

<a id="id2"></a>

## 简介

本示例的发送方使用gatt notify，当对端收到后立刻发下一包，从而可得出最大吞吐。

<a id="id3"></a>

## 单板与手机测试

> 1. 开发板A作为server,串口下发AT命令
>
> AT\+BLE\=REGPERFORMANCESERVICE,1,0x1234,0x5678 (注册服务)
>
> AT\+BLE\=SETADVPARAM,7,120,120,0,0,3,1,1 (设置广播参数)
>
> AT\+BLE\=SETADVDATA,0201060908373235365f424c45,D (设置广播内容)
>
> AT\+BLE\=SETADVENABLE,1 （开启广播）
>
> 2. 用手机nrf连接并discovery service
> 3. nrf更新mtu为251
> 4. A板输入 `AT+BLE=SETTXTESTPARAM,240,100` (240为每次发送payload的长度，必须小于gatt mtu)
> 5. A板输入 `AT+BLE=ENABLEPERFORMANCESTATISTIC,tx,1`
> 6. 手机开启notify(可以看到只有一个可以开启)
> 7. log会输出统计的速率

<a id="id4"></a>

## 双板对测

> 1. 开发板A作为server,串口下发AT命令
>
> AT\+BLE\=REGPERFORMANCESERVICE,1,0x1234,0x5678 (注册服务)
>
> AT\+BLE\=SETADVPARAM,7,120,120,0,0,3,1,1 (设置广播参数)
>
> AT\+BLE\=SETADVDATA,0201060908373235365f424c45,D (设置广播内容)
>
> AT\+BLE\=SETADVENABLE,1 （开启广播）
>
> 2. 开发板B作为client,串口下发AT命令发起连接: `AT+BLE=CREATECONNECT,6,0,200,1,0,xx:xx:xx:xx:xx:xx` (包括开发板A蓝牙地址)
> 3. B板输入 `AT+BLE=UPDATEMTU2MAX,8,251` (更新gatt mtu至251，其中8是步骤2返回的conn\_id)
> 4. A板输入 `AT+BLE=SETTXTESTPARAM,240,100` (240为每次发送payload的长度，必须小于gatt mtu)
> 5. A板输入 `AT+BLE=ENABLEPERFORMANCESTATISTIC,tx,1`
> 6. B板输入 `AT+BLE=ENABLEPERFORMANCESTATISTIC,rx,1`
> 7. B板输入 `AT+BLE=ATTWRITE,8,13,0001` (其中8为步骤2返回的conn\_id，13为0x1234特征的client config attribute hande，0001为开启notify)
> 8. log会输出统计的速率

<a id="id5"></a>

## 示例

> 相关AT测试代码可参考: `components/at/src/ble_at_command.c`

<a id="id6"></a>

## 参考链接

> [API参考:](../../api-reference/bluetooth.md) 介绍了蓝牙API接口
>
> [开发者指南:](../../developer-guide/bluetooth.md) 介绍了蓝牙常用使用场景
>
> [样例演示:](../bluetooth.md) 介绍了蓝牙样例使用和操作
>
> [蓝牙工程:](../../projects_work/bluetooth.md) 介绍了蓝牙相关工程
