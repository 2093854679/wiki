---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/examples/cli/bluetooth/bt.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bt-cli"></a>

# BT Cli

<a id="id1"></a>

## 1\. 功能概述

> 为了便于验证BT相关功能，为此设计了一系列AT CMD。所有BLE AT CMD命令以 `AT+BT=` 开头，后接具体命令和参数。如果命令执行成功，则返回 `CMDRSP:OK`。如果命令执行失败，则返回 `CMDRSP:ERROR`。

<a id="id2"></a>

## 2\. 代码路径

> 路径: `\components\at\src\bt_at_command.c`

<a id="cli"></a>

## 3\. cli命令简介

支持的命令如下:

> 1.AT\+BT\=INQUIRY
> :   - 功能说明
>       :   扫描命令，用于扫描周围可见的classic设备
>     - 命令格式
>       :   AT\+BT\=INQUIRY
>     - 参数说明
>       :   无参数
>     - 返回值说明
>       :   扫描到的设备地址
>
> 2.AT\+BT\=READ\_SCAN\_ENABLE
> :   - 功能说明
>       :   获取当前设备可见性
>     - 命令格式
>       :   AT\+BT\=READ\_SCAN\_ENABLE
>     - 参数说明
>       :   无参数
>     - 返回值说明
>       :   | Value | Parameter Description |
>           | --- | --- |
>           | 0x00 | No Scans enabled. |
>           | 0x01 | Inquiry Scan enabled. Page Scan disabled. |
>           | 0x02 | Inquiry Scan disabled. Page Scan enabled. |
>           | 0x03 | Inquiry Scan enabled. Page Scan enabled. |
>
> 3.AT\+BT\=WRITE\_SCAN\_ENABLE
> :   - 功能说明
>       :   设置当前设备可见性
>     - 命令格式
>       :   AT\+BT\=WRITE\_SCAN\_ENABLE,param1
>     - 参数说明
>       :   | Param1 | Parameter Description |
>           | --- | --- |
>           | 0x00 | No Scans enabled. |
>           | 0x01 | Inquiry Scan enabled. Page Scan disabled. |
>           | 0x02 | Inquiry Scan disabled. Page Scan enabled. |
>           | 0x03 | Inquiry Scan enabled. Page Scan enabled. |
>
> 4.AT\+BT\=CONNECT
> :   - 功能说明
>       :   连接指定设备
>     - 命令格式
>       :   AT\+BT\=CONNECT,param1,param2
>     - 参数说明
>       :   | Param | Parameter Description |
>           | --- | --- |
>           | param1 | Bluetooth address |
>           | param2 | Allow\_Role\_Switch  0x00 not accept role switch  0x01 accept role switch |
>
> 5.AT\+BT\=DISCONNECT
> :   - 功能说明
>       :   断开指定设备
>     - 命令格式
>       :   AT\+BT\=DISCONNECT,param1
>     - 参数说明
>       :   | Param | Parameter Description |
>           | --- | --- |
>           | param1 | Bluetooth address |
>
> 6.AT\+BT\=SPP\_INIT
> :   - 功能说明
>       :   SPP初始化，注册SDP
>     - 命令格式
>       :   AT\+BT\=SPP\_INIT
>     - 参数说明
>       :   无参数
>
> 7.AT\+BT\=SPP\_CONNECT
> :   - 功能说明
>       :   SPP连接指定设备
>     - 命令格式
>       :   AT\+BT\=SPP\_CONNECT,param1
>     - 参数说明
>       :   | Param | Parameter Description |
>           | --- | --- |
>           | param1 | Bluetooth address |
>
> 8.AT\+BT\=SPP\_TX
> :   - 功能说明
>       :   SPP发送指定数据
>     - 命令格式
>       :   AT\+BT\=SPP\_TX,param1
>     - 参数说明
>       :   | Param | Parameter Description |
>           | --- | --- |
>           | param1 | send data |
>     - 测试用例
>       :   AT\+BT\=SPP\_TX,beken-spp-tx\_test!!!!
>
> 9.AT\+BT\=SPP\_THROUGH\_TEST
> :   - 功能说明
>       :   SPP吞吐测试，发送的数据为随机生成的数据
>     - 命令格式
>       :   AT\+BT\=SPP\_THROUGH\_TEST,param1
>     - 参数说明
>       :   | Param | Parameter Description |
>           | --- | --- |
>           | param1 | send data length |
>     - 返回值说明
>       :   指定长度的数据发送完成后，client和server会从log中输出以发送数据计算的CRC值以及传输速率。
>     - 测试用例
>       :   AT\+BT\=SPP\_THROUGH\_TEST,0xfffff
