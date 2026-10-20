---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7239/zh_CN/v2.2.1/examples/cli/sd_card/sd_cli.html
sdk_family: bk_idk
chip: BK7239
processor: ''
sdk_version: v2.2.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="sd-card-cli"></a>

<a id="sd-cli"></a>

# **SD Card cli命令**

重要

*sd\_card功能需要使用fatfstest命令进行测试。与sd\_card测试用例需要打开CONFIG\_FATFS宏*

- [fatfstest M](#sd-sdm) :执行对sd card进行挂载
- [fatfstest U](#sd-sdu) :执行对sd card进行卸载
- [fatfstest G](#sd-sdg) :查询sd card当前剩余空间
- [fatfstest S](#sd-sds) :扫描sd card文件
- [fatfstest F](#sd-sdf) :格式化sd card设备
- [fatfstest R](#sd-sdr) :读取sd card中文件
- [fatfstest W](#sd-sdw) :向sd card中文件中写入内容
- [fatfstest D](#sd-sdd) :dump sd card中文件内容到一个空间
- [fatfstest A](#sd-sda) :自动测试写入文件

<a id="fatfstest-m-sd-card"></a>

<a id="sd-sdm"></a>

## [fatfstest M](#sd-cli) **:执行对sd card进行挂载**

**命令**

```
fatfstest M {DISK_NUMBER}
```

**参数**

```
DISK_NUMBER：磁盘号，1表示SD卡
```

**使用场景**

```
输入：

    fatfstest M 1：挂载sd卡

挂载成功会显示f_mount OK，打印内容如下：

(68861838):error file name,use defaultfilename.txt

sdio_hos:I(68861838):dst start addr=0x458d003c

sdio_hos:I(68861838):s_sdio_host.dma_tx_id = 0.

sdio_hos:I(68861838):s_sdio_host.dma_tx_id = 12.

sdio_hos:I(68861838):s_sdio_host.dma_rx_id = 13.

sd_card:I(68861840):sdio host init ok, clock_freq:7

sd_card:I(68861922):sd card support voltage 2.7-3.6 V
sd_card:I(68861990):card capacity SDHC_SDXC

sd_card:I(68861998):sd card class:0x5b5

sd_card:I(68862010):sdio clock freq:7->11

(68862014):fmt=2

(68862016):fmt2=1

Fatfs:I(68862016):f_mount OK!

Fatfs:I(68862016):----- test_mount 1 over  -----
```

备注

*打印error file name,use defaultfilename.txt是由于测试命令中会扫描defaultfilename.txt文件，无此文件会打印error*

备注

*与sd\_card测试用例需要打开CONFIG\_FATFS宏*

**响应**

```
CMDRSP:OK

CMDRSP:ERROR
```

<a id="fatfstest-u-sd-card"></a>

<a id="sd-sdu"></a>

## [fatfstest U](#sd-cli) **:执行对sd card进行卸载**

**命令**

```
fatfstest U {DISK_NUMBER}
```

**参数**

```
DISK_NUMBER：磁盘号，1表示SD卡
```

**使用场景**

```
输入：

    fatfstest U 1：卸载sd卡

挂载成功会显示f_mount OK，打印内容如下：

卸载成功会显示f_unmount OK，打印内容如下：

fatfstest U 1

$(404554):error file name,use defaultfilename.txt

(404554):f_unmount OK!

(404554):----- test_unmount 1 over  -----

(404554):unmount:sdio_sd
```

备注

*与sd\_card测试用例需要打开CONFIG\_FATFS宏*

**响应**

```
CMDRSP:OK

CMDRSP:ERROR
```

<a id="fatfstest-g-sd-card"></a>

<a id="sd-sdg"></a>

## [fatfstest G](#sd-cli) **:查询sd card当前剩余空间**

**命令**

```
fatfstest G {DISK_NUMBER}
```

**参数**

```
DISK_NUMBER：磁盘号，1表示SD卡
```

**使用场景**

```
输入：

    fatfstest G 1：查询剩余空间

查询成功会显示f_getfree OK!，打印内容如下：

sdio_hos:I(69876174):dst start addr=0x458d003c

sdio_hos:I(69876174):s_sdio_host.dma_tx_id = 12.

sdio_hos:I(69876174):s_sdio_host.dma_rx_id = 13.

sd_card:I(69876174):sdio host init ok, clock_freq:7

sd_card:I(69876254):sd card support voltage 2.7-3.6 V

sd_card:I(69876324):card capacity SDHC_SDXC

sd_card:I(69876334):sd card class:0x5b5

sd_card:I(69876344):sdio clock freq:7->11

(69876538):test_getfree getnclst:DEC 949435 free space: 59339MB

(69876540):f_getfree OK!

(69876540):----- test_getfree 1 over  -----

(69876540):getfree:sdio_sd
```

备注

*与sd\_card测试用例需要打开CONFIG\_FATFS宏*

**响应**

```
CMDRSP:OK

CMDRSP:ERROR
```

<a id="fatfstest-s-sd-card"></a>

<a id="sd-sds"></a>

## [fatfstest S](#sd-cli) **:扫描sd card文件**

**命令**

```
fatfstest S {DISK_NUMBER}
```

**参数**

```
DISK_NUMBER：磁盘号，1表示SD卡
```

**使用场景**

```
输入：

    fatfstest G 1：扫描文件

扫描成功会显示scan_files OK!，打印内容如下：

Fatfs:I(70912942):

----- scan_file_system 1 start -----

Fatfs:I(70912942):1:/

sdio_hos:I(70912942):dst start addr=0x458d003c

sdio_hos:I(70912942):s_sdio_host.dma_tx_id = 12.

sdio_hos:I(70912944):s_sdio_host.dma_rx_id = 13.

sd_card:I(70912944):sdio host init ok, clock_freq:7

sd_card:I(70913024):sd card support voltage 2.7-3.6 V

sd_card:I(70913094):card capacity SDHC_SDXC

sd_card:I(70913104):sd card class:0x5b5

sd_card:I(70913112):sdio clock freq:7->11

Fatfs:I(70913118):1:/test.txt

Fatfs:I(70913118):1:/autotest_1.txt

Fatfs:I(70913118):1:/autotest_2.txt

Fatfs:I(70913118):1:/autotest_3.txt

Fatfs:I(70913118):1:/dump_psram.txt

$Fatfs:I(70913118):1:/dump_2.txt

Fatfs:I(70913118):scan_files OK!

Fatfs:I(70913118):----- scan_file_system 1 over  -----

(70913118):scan
```

备注

*与sd\_card测试用例需要打开CONFIG\_FATFS宏*

**响应**

```
CMDRSP:OK

CMDRSP:ERROR
```

<a id="fatfstest-f-sd-card"></a>

<a id="sd-sdf"></a>

## [fatfstest F](#sd-cli) **:格式化sd card设备**

**命令**

```
fatfstest F {DISK_NUMBER}
```

**参数**

```
DISK_NUMBER：磁盘号，1表示SD卡
```

**使用场景**

```
输入：

    fatfstest F 1：格式化SD卡

格式化成功显示f_mkfs OK!，输出内容如下：

sdio_hos:I(439300):dst start addr=0x458d003c

sdio_hos:I(439300):s_sdio_host.dma_tx_id = 12.

sdio_hos:I(439300):s_sdio_host.dma_rx_id = 13.

sd_card:I(439302):sdio host init ok, clock_freq:7

sd_card:I(439384):sd card support voltage 2.7-3.6 V

sd_card:I(439472):card capacity SDHC_SDXC

sd_card:I(439484):sd card class:0x5b5

sd_card:I(439492):sdio clock freq:7->11

(439496):part=0

sd_card:I(439496):card ver=2.0,size:0x073e8000 sector(sector=512bytes)

(439496):sdcard sector cnt=121536512

Fatfs:I(441532):f_mkfs OK!

(441532):format :1
```

备注

*与sd\_card测试用例需要打开CONFIG\_FATFS宏*

**响应**

```
CMDRSP:OK

CMDRSP:ERROR
```

<a id="fatfstest-r-sd-card"></a>

<a id="sd-sdr"></a>

## [fatfstest R](#sd-cli) **:读取sd card中文件**

**命令**

```
fatfstest R {DISK_NUMBER} {file_name} {length}
```

**参数**

```
DISK_NUMBER：磁盘号，1表示SD卡

file_name: 读取的文件名

length: 读取内容长度
```

**使用场景**

```
 在SD卡挂载情况下，输入:

    fatfstest R 1 test.txt 10

读取成功会输出文件内容，打印内容如下：

 ----- test_fatfs 1 start -----

 Fatfs:I(71732504):f_open "1:/test.txt"

 sdio_hos:I(71732504):dst start addr=0x458d003c

 sdio_hos:I(71732506):s_sdio_host.dma_tx_id = 12.

 sdio_hos:I(71732506):s_sdio_host.dma_rx_id = 13.

 sd_card:I(71732506):sdio host init ok, clock_freq:7

 sd_card:I(71732588):sd card support voltage 2.7-3.6 V

 sd_card:I(71732656):card capacity SDHC_SDXC

 sd_card:I(71732666):sd card class:0x5b5

 sd_card:I(71732676):sdio clock freq:7->11

 Fatfs:I(71732680):will read left_len = 10

 ====== f_read one cycle - dump(len=10) begin ======

 61 63 6c 5f 62 6b 37 32 35 38

 ====== f_read one cycle - dump(len=10)   end ======

 $Fatfs:I(71732680):f_read start:10 bytes

 Fatfs:I(71732688):f_read one cycle finish:left_len = 0

 Fatfs:I(71732688):f_read: read total byte = 10

 Fatfs:I(71732688):f_close OK

 Fatfs:I(71732688):----- test_fatfs 1 over  -----
```

备注

*与sd\_card测试用例需要打开CONFIG\_FATFS宏*

**响应**

```
CMDRSP:OK

CMDRSP:ERROR
```

<a id="fatfstest-w-sd-card"></a>

<a id="sd-sdw"></a>

## [fatfstest W](#sd-cli) **:向sd card中文件中写入内容**

**命令**

```
fatfstest W {DISK_NUMBER} {file_name} {content} {length}
```

**参数**

```
DISK_NUMBER：磁盘号，1表示SD卡

file_name: 写入的文件名

content: 写入内容

length: 写入内容长度，一次最多64字节
```

**使用场景**

```
在SD卡挂载情况下，输入:

   fatfstest W 1 autotest.txt Aclsemi 7:向autotest.txt写入文件内容Aclsemi

写入成功会输出append and write:autotest.txt,Aclsemi，打印内容如下：

Fatfs:I(82556592):

----- test_fatfs 1 start -----

Fatfs:I(82556592):f_open "1:/autotest.txt"

sdio_hos:I(82556594):dst start addr=0x458d003c

sdio_hos:I(82556594):s_sdio_host.dma_tx_id = 12.

sdio_hos:I(82556594):s_sdio_host.dma_rx_id = 13.

sd_card:I(82556594):sdio host init ok, clock_freq:7

sd_card:I(82556676):sd card support voltage 2.7-3.6 V

sd_card:I(82556752):card capacity SDHC_SDXC

sd_card:I(82556764):sd card class:0x5b5

sd_card:I(82556772):sdio clock freq:7->11

Fatfs:I(82556778):.Fatfs:I(82556794):f_close OK

Fatfs:I(82556794):----- test_fatfs 1 over  -----

$(82556794):append and write:autotest.txt,Aclsemi
```

备注

*与sd\_card测试用例需要打开CONFIG\_FATFS宏*

**响应**

```
CMDRSP:OK

CMDRSP:ERROR
```

<a id="fatfstest-d-dump-sd-card"></a>

<a id="sd-sdd"></a>

## [fatfstest D](#sd-cli) **:dump sd card中文件内容到一个空间**

**命令**

```
fatfstest D {DISK_NUMBER} {file_name} {start_addr} {length}
```

**参数**

```
DISK_NUMBER：磁盘号，1表示SD卡

file_name: 写入的文件名

start_addr: dump起始地址

length:内容长度
```

**使用场景**

```
在SD卡挂载情况下，输入:

   fatfstest D 1 autotest.txt 0x23da000 7

dump成功输出一下内容：

Fatfs:I(116672):

----- test_fatfs_dump 1 start -----

Fatfs:I(116672):file_name=test.txt,start_addr=0x23da000,len=16

Fatfs:I(116672):f_open start "1:/test.txt"

sdio_hos:I(116674):dst start addr=0x458d003c

sdio_hos:I(116674):s_sdio_host.dma_tx_id = 12.

sdio_hos:I(116674):s_sdio_host.dma_rx_id = 13.

sd_card:I(116674):sdio host init ok, clock_freq:7

sd_card:I(116756):sd card support voltage 2.7-3.6 V

sd_card:I(116770):card capacity SDHC_SDXC

sd_card:I(116780):sd card class:0x5b5

sd_card:I(116788):sdio clock freq:7->11

Fatfs:I(116794):f_write start

Fatfs:I(116794):f_write end len = 16

Fatfs:I(116794):f_lseek start

Fatfs:I(116794):f_close start
```

备注

*与sd\_card测试用例需要打开CONFIG\_FATFS宏*

**响应**

```
CMDRSP:OK

CMDRSP:ERROR
```

<a id="fatfstest-a"></a>

<a id="sd-sda"></a>

## [fatfstest A](#sd-cli) **:自动测试写入文件**

**命令**

```
fatfstest A {DISK_NUMBER} {file_name} {length} {test_cnt} {start_addr}
```

**参数**

```
DISK_NUMBER：磁盘号，1表示SD卡

file_name: 写入的文件名

length:内容长度

test_cnt:自动循环写入的次数

start_addr:起始地址
```

**使用场景**

```
在SD卡挂载情况下，输入:

   fatfstest A 1 autotest1.txt 1024 1 0x23da000

测试成功输出一下内容：

sdio_hos:I(28686):dst start addr=0x458d003c

sdio_hos:I(28686):s_sdio_host.dma_tx_id = 12.

sdio_hos:I(28686):s_sdio_host.dma_rx_id = 13.

sd_card:I(28686):sdio host init ok, clock_freq:7

sd_card:I(28768):sd card support voltage 2.7-3.6 V

sd_card:I(28782):card capacity SDHC_SDXC

sd_card:I(28794):sd card class:0x5b5

sd_card:I(28802):sdio clock freq:7->11

Fatfs:I(28814):auto test succ
```

备注

*与sd\_card测试用例需要打开CONFIG\_FATFS宏*

**响应**

```
CMDRSP:OK

CMDRSP:ERROR
```
