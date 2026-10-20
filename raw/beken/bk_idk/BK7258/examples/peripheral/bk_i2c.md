---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7258/zh_CN/v2.0.1/examples/peripheral/bk_i2c.html
sdk_family: bk_idk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="i2c"></a>

# I2C

<a id="id1"></a>

## 1 功能概述

> 通过I2C接口完成对EEPROM芯片的数据读写。

<a id="id2"></a>

## 2 代码路径

> demo路径：`components\bk_cli\cli_i2c.c`

<a id="cli"></a>

## 3 cli命令简介

demo运行依赖的宏配置：

> | NAME | Description | File | value |
> | --- | --- | --- | --- |
> | CONFIG\_I2C | support i2c | `middleware\soc\bk7236\bk7236.defconfig` | y |

demo支持的命令如下表：

> | Command | Param | Description |
> | --- | --- | --- |
> | i2c\_driver init | none | init I2C driver control memory |
> | i2c\_driver deinit | none | free all resource related to I2C |
> | i2c {id} init | i2c id number | power up and start the I2C id |
> | i2c {id} deinit | i2c id number | power down and Stop the I2C id |
> | i2c {id} memory\_write {data\_size} {dev\_addr} | id: i2c id number | write data\_size bytes of data to the slave device with address dev\_id |
> | data\_size:size of data written |
> | dev\_addr: slave device address |
> | i2c {id} memory\_read {data\_size} | id: i2c id | read data\_size bytes of data from slave device |
> | data\_size:size of data read |

<a id="id3"></a>

## 4 演示介绍

> > demo执行的步骤如下：
>
> 1、准备好EEPROM的模块，型号为FM24C04B，连接方式如下：
>
> > ```
> > SCL----GPIO0
> > SDA----GPIO1
> > Vcc----3.3V
> > ```
>
> 2、顺序发送以下命令
>
> > ```
> > i2c_driver init
> >
> > i2c 1 init
> >
> > i2c 1 memory_write 8 50   //向EEPROM中写入8字节数据
> >
> > i2c 1 memory_read 8       //从EEPROM中读取8字节数据
> > ```

备注

注意：memory\_write命令中的dev\_addr 50为16进制，因为i2c驱动中会将dev\_addr左移一位，所以传入的dev\_addr需要将FM24C04B的dev\_addr（1010b）右移一位。
