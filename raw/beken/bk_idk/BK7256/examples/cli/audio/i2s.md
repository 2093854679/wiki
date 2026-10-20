---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/examples/cli/audio/i2s.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="i2s-cli"></a>

# I2S Cli

<a id="id1"></a>

## 1、功能概述

> 为了便于验证i2s相关的功能，为此设计了一系列cli CMD，同时也是i2s的各功能场景demo，供客户参考使用。

<a id="id2"></a>

## 2、代码路径

> 路径: `components\demos\media\audio\aud_intf\demo\i2s_demo.c`

<a id="cli"></a>

## 3、cli命令简介

支持的命令如下:

> 1.i2s\_master\_test
> :   - 功能说明
>       :   用来测试作为 `master` 在标准 `Philips` 模式下发送数据。
>     - 命令格式
>       :   i2s\_master\_test param1
>
>           | Param | value |
>           | --- | --- |
>           | param1 | opcode  start : Start send  stop : Stop send |
>     - 测试用例
>       :   开始发送：`i2s_master_test start`
>
>           停止发送：`i2s_master_test stop`
>
> 2.i2s\_slave\_test
> :   - 功能说明
>       :   用来测试作为 `slave` 在标准 `Philips` 模式下接收数据。
>     - 命令格式
>       :   i2s\_slave\_test param1
>
>           | Param | value |
>           | --- | --- |
>           | param1 | opcode  start : Start receive  stop : Stop receive |
>     - 测试用例
>       :   开始接收：`i2s_slave_test start`
>
>           停止接收：`i2s_slave_test stop`
>
> 3.pcm\_master\_test
> :   - 功能说明
>       :   用来测试作为 `master` 在 `PCM` 模式下发送数据。
>     - 命令格式
>       :   pcm\_master\_test param1
>
>           | Param | value |
>           | --- | --- |
>           | param1 | opcode  start : Start send  stop : Stop send |
>     - 测试用例
>       :   开始发送：`pcm_master_test start`
>
>           停止发送：`pcm_master_test stop`
>
> 4.pcm\_slave\_test
> :   - 功能说明
>       :   用来测试作为 `slave` 在标准 `PCM` 模式下接收数据。
>     - 命令格式
>       :   pcm\_slave\_test param1
>
>           | Param | value |
>           | --- | --- |
>           | param1 | opcode  start : Start receive  stop : Stop receive |
>     - 测试用例
>       :   开始接收：`pcm_slave_test start`
>
>           停止接收：`pcm_slave_test stop`
>
> 5.dtm\_master\_test
> :   - 功能说明
>       :   用来测试作为 `master` 在 `PCM+DTM` 模式下发送数据。
>     - 命令格式
>       :   dtm\_master\_test param1
>
>           | Param | value |
>           | --- | --- |
>           | param1 | opcode  start : Start send  stop : Stop send |
>     - 测试用例
>       :   开始发送：`dtm_master_test start`
>
>           停止发送：`dtm_master_test stop`
>
> 6.dtm\_slave\_test
> :   - 功能说明
>       :   用来测试作为 `slave` 在标准 `PCM+DTM` 模式下接收数据。
>     - 命令格式
>       :   dtm\_slave\_test param1
>
>           | Param | value |
>           | --- | --- |
>           | param1 | opcode  start : Start receive  stop : Stop receive |
>     - 测试用例
>       :   开始接收：`dtm_slave_test start`
>
>           停止接收：`dtm_slave_test stop`
>
> 7.2bd\_master\_test
> :   - 功能说明
>       :   用来测试作为 `master` 在 `2B+D` 模式下发送数据。
>     - 命令格式
>       :   2bd\_master\_test param1
>
>           | Param | value |
>           | --- | --- |
>           | param1 | opcode  start : Start send  stop : Stop send |
>     - 测试用例
>       :   开始发送：`2bd_master_test start`
>
>           停止发送：`2bd_master_test stop`
>
> 8.2bd\_slave\_test
> :   - 功能说明
>       :   用来测试作为 `slave` 在标准 `2B+D` 模式下接收数据。
>     - 命令格式
>       :   2bd\_slave\_test param1
>
>           | Param | value |
>           | --- | --- |
>           | param1 | opcode  start : Start receive  stop : Stop receive |
>     - 测试用例
>       :   开始接收：`2bd_slave_test start`
>
>           停止接收：`2bd_slave_test stop`
