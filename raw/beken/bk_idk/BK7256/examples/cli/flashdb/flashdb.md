---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/examples/cli/flashdb/flashdb.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="flashdb-cli"></a>

# flashdb Cli

<a id="flashdb"></a>

## 1、flashdb介绍

> FlashDB 是一款超轻量级的嵌入式数据库，专注于提供嵌入式产品的数据存储方案。与传统的基于文件系统的数据库不同，FlashDB 结合了 Flash 的特性，具有较强的性能及可靠性。并在保证极低的资源占用前提下，尽可能延长 Flash 使用寿命。
>
> FlashDB 提供两种数据库模式：
> :   - 键值数据库 ：是一种非关系数据库，它将数据存储为键值（Key-Value）对集合，其中键作为唯一标识符。KVDB 操作简洁，可扩展性强。
>     - 时序数据库 ：时间序列数据库 （Time Series Database , 简称 TSDB），它将数据按照 时间顺序存储 。TSDB 数据具有时间戳，数据存储量大，插入及查询性能高。
>
> 接口：
> <http://armink.gitee.io/flashdb/#/zh-cn/api>
>
> 示例说明：
> <http://armink.gitee.io/flashdb/#/zh-cn/demo-details>
>
> 更多信息可访问：
> <https://gitee.com/armink/FlashDB>

重要

FlashDB 的kvdb和easyflash的功能一致，所以如果使用FlashDB时，建议关闭easyflash功能，以减少代码空间。

<a id="id1"></a>

## 2、代码路径

> 路径: `\components\bk_cli\cli_flashdb.c`

<a id="id2"></a>

## 3、依赖配置

备注

起始地址和大小可依据实际需要调整。

> | CONFIG | value |
> | --- | --- |
> | CONFIG\_FLASHDB | y，flashdb总开关 |
> | CONFIG\_FLASHDB\_USING\_KVDB | y，kvdb功能开关 |
> | CONFIG\_FLASHDB\_KVDB\_START\_ADDR | 0x3EF000，kvdb存放在flash里的起始地址 |
> | CONFIG\_FLASHDB\_KVDB\_SIZE | 0x2000，kvdb存放在flash里的空间大小 |
> | CONFIG\_NTP\_SYNC\_RTC | y，ntp开关，用来给tsdb提供时间 |
> | CONFIG\_FLASHDB\_USING\_TSDB | y，tsdb功能开关 |
> | CONFIG\_FLASHDB\_TSDB\_START\_ADDR | 0x3F1000，tsdb存放在flash里的起始地址 |
> | CONFIG\_FLASHDB\_TSDB\_SIZE | 0x4000，tsdb存放在flash里的空间大小 |
> | CONFIG\_FLASHDB\_DEMO | y，flashdb测试开关 |

<a id="cli"></a>

## 4、cli命令简介

支持的命令如下:

> > 1.flashdb\_init
> > :   - 功能说明
> >       :   初始化flashdb里的kvdb和tsdb
> >
> > 2.flashdb\_kvdb
> > :   - 功能说明
> >       :   该示例主要演示了kvdb的基础功能，包含blob和string类型的写入和读取、kvdb的遍历，具体参见：
> >           <http://armink.gitee.io/flashdb/#/zh-cn/sample-kvdb-basic>
>
> 3.flashdb\_tsdb
> :   - 功能说明
>       :   该示例主要演示了 TSDB 的基础功能，包括 TSL（时序记录）的追加、查询及状态修改功能，具体参见：
>           <http://armink.gitee.io/flashdb/#/zh-cn/sample-tsdb-basic>
