---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7236n/zh_CN/v2.2.1/examples/peripheral/bk_sdio.html
sdk_family: bk_idk
chip: BK7236N
processor: ''
sdk_version: v2.2.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="fatfssd"></a>

# fatfs文件系统和SD卡读写

<a id="id1"></a>

## 1 功能概述

> BEKEN项目支持使用SD卡，FLASH和USB等外设存储用户数据，用户实际操作数据时通常只需要调用开源的文件系统函数，就可以将用户数据读写到存储设备中。
>
> SDK工程主要采用FatFS文件系统，来实现对SD卡和USB的读写操作；主要采用EasyFlash，来实现对flash的操作。两者都是开源的应用程序，SDK工程中用户只需要进行简单的配置，就可以通过文件系统函数操作SD卡和flash等存储设备。
>
> SDK工程中使用FatFS文件系统对SD卡进行文件管理，用户只需要进行简单的配置就可以使用SD卡，本文档主要对操作fatfs文件系统的API和cli命令进行介绍。
>
> FatFs是面向小型嵌入式系统的一种通用的FAT文件系统。它完全是由ANSI C语言编写并且完全独立于底层的I/O介质，因此它可以很容易地移植到其他的处理器当中，如8051、PIC和ARM等。
>
> FatFs支持FAT12、FAT16、FAT32等格式，所以我们基于SDIO或者SPI Flash芯片驱动，把FatFs文件系统代码移植到工程之中，就可以利用文件系统的各种函数，实现对SD卡或者SPI Flash芯片以“文件”格式进行读写操作。

<a id="fatfs-demo"></a>

## 2 FatFS demo代码路径

> demo路径：`components\bk_cli\cli_fatfs.c` `components\fatfs\test_fatfs.c`

<a id="fatfs-api"></a>

## 3 FatFS API简介

> SDK工程中已经移植好fatfs文件系统，详细的fatfs相关API介绍可参见链接：`http://elm-chan.org/fsw/ff/00index_e.html`
>
> 下面介绍常用的FatFS API函数：
>
> 1、f\_mount
> :   1. 功能： 在FatFs模块上注册、注销一个工作区（文件系统对象）
>     2. 函数定义： FRESULT f\_mount(FATFS\* fs, const TCHAR\* path, BYTE opt)
>     3. 参数： fs：工作区（文件系统对象）指针; path：注册/注销工作区的逻辑驱动器号; opt：注册或注销选项
>     4. 返回： 操作结果
>
> 2、f\_open
> :   1. 功能： 创建/打开一个文件对象
>     2. 函数定义： FRESULT f\_open(FIL\* fp, const TCHAR\* path, BYTE mode)
>     3. 参数： fp：将被创建的文件对象结构的指针; path：文件名指针，指定将创建或打开的文件名; mode：访问类型和打开方法，由一下标准的一个组合指定的;
>     4. 返回： 操作结果
>
> 3、f\_close
> :   1. 功能： 关闭一个打开的文件
>     2. 函数定义： FRESULT f\_close(FIL\* fp)
>     3. 参数： fp：指向将被关闭的已打开的文件对象结构的指针
>     4. 返回： 操作结果
>
> 4、f\_read
> :   1. 功能： 从一个打开的文件中读取数据
>     2. 函数定义： FRESULT f\_read(FIL\* fp, void\* buff, UINT btr, UINT\* br)
>     3. 参数： fp：指向将被读取的已打开的文件对象结构的指针; buff：指向存储读取数据的缓冲区的指针; btr：要读取的字节数; br：指向返回已读取字节数的UINT变量的指针，返回为实际读取的字节数;
>     4. 返回： 操作结果
>
> 5、 f\_write
> :   1. 功能： 写入数据到一个已打开的文件
>     2. 函数定义： FRESULT f\_write(FIL\* fp, void\* buff, UINT btw, UINT\* bw)
>     3. 参数： fp：指向将被写入的已打开的文件对象结构的指针; buff：指向存储写入数据的缓冲区的指针; btw：要写入的字节数; bw：指向返回已写入字节数的UINT变量的指针，返回为实际写入的字节数;
>     4. 返回： 操作结果
>
> FatFs还有很多API操作函数，在这里不再作详细的介绍，详细信息请查看FatFs文件系统官网。

<a id="fatfs-cli"></a>

## 4 FatFS cli命令简介

> > SDIO demo运行依赖的宏配置：
> >
> > | NAME | Description | File | value |
> > | --- | --- | --- | --- |
> > | CONFIG\_SDIO\_V1P0 | support SDIO version V1P0,unused | `middleware\soc\bk7236n\bk7236n.defconfig` | n |
> > | CONFIG\_SDIO\_V2P0 | support SDIO version V2P0,current version | `middleware\soc\bk7236n\bk7236n.defconfig` | y |
> > | CONFIG\_SDIO\_HOST | set to host mode for connecting SD card | `middleware\soc\bk7236n\bk7236n.defconfig` | y |
> > | CONFIG\_SDIO\_SLAVE | support SDIO slave mode,unused | `middleware\soc\bk7236n\bk7236n.defconfig` | n |
> > | CONFIG\_SDIO\_CHANNEL\_EN | support SDIO logical channel,depend on CONFIG\_SDIO\_SLAVE | `middleware\soc\bk7236n\bk7236n.defconfig` | n |
> > | CONFIG\_SDIO\_BIDIRECT\_CHANNEL\_EN | support SDIO bidirect channel,depend on CONFIG\_SDIO\_SLAVE | `middleware\soc\bk7236n\bk7236n.defconfig` | n |
> > | CONFIG\_SDIO\_GDMA\_EN | support SDIO GDMA,unsuport,depend on CONFIG\_SDIO\_SLAVE | `middleware\soc\bk7236n\bk7236n.defconfig` | n |
> > | CONFIG\_GPIO\_NOTIFY\_TRANSACTION\_EN | support notify transaction,,depend on CONFIG\_SDIO\_SLAVE | `middleware\soc\bk7236n\bk7236n.defconfig` | n |
> > | CONFIG\_SDIO\_4LINES\_EN | support SDIO 4 line,if no,support 1 line | `middleware\soc\bk7236n\bk7236n.defconfig` | n |
> > | CONFIG\_SDIO\_TEST\_EN | support SDIO testself | `middleware\soc\bk7236n\bk7236n.defconfig` | n |
> > | CONFIG\_SDIO\_DEBUG\_EN | support SDIO debug | `middleware\soc\bk7236n\bk7236n.defconfig` | n |
> > | CONFIG\_SDIO\_HOST\_DEFAULT\_CLOCK\_FREQ\=7 | set SDIO host clk,default 100k | `middleware\soc\bk7236n\bk7236n.defconfig` | 7 |
> >
> > SD card demo运行依赖的宏配置：
> >
> > | NAME | Description | File | value |
> > | --- | --- | --- | --- |
> > | CONFIG\_SDCARD\_HOST | support SD card,host mode | `middleware\soc\bk7236n\bk7236n.defconfig` | y |
> > | CONFIG\_SDCARD\_V2P0 | support SD version V2P0 | `middleware\soc\bk7236n\bk7236n.defconfig` | y |
> > | CONFIG\_SDCARD\_V1P0 | support SD version V1P0 | `middleware\soc\bk7236n\bk7236n.defconfig` | n |
> > | CONFIG\_SDCARD\_BUSWIDTH\_4LINE | support SD card 4 line | `middleware\soc\bk7236n\bk7236n.defconfig` | n |
> >
> > fatfs demo运行依赖的宏配置：
> >
> > | NAME | Description | File | value |
> > | --- | --- | --- | --- |
> > | CONFIG\_FATFS | support fatfs | `middleware\soc\bk7236n\bk7236n.defconfig` | y |
> > | CONFIG\_FATFS\_SDCARD | SD card support fatfs | `middleware\soc\bk7236n\bk7236n.defconfig` | y |
> >
> > demo支持的cli命令如下表：
> >
> > | Command | Param | Description |
> > | --- | --- | --- |
> > | fatfstest {M\|U} {DISK\_NUMBER} | {M\|U}: mount\|unmount | apply for or release the workspace for logical drivers |
> > | {DISK\_NUMBER}:logical driver number |
> > | fatfstest G {DISK\_NUMBER} | {DISK\_NUMBER}:logical driver number | get the size of remaining disk space |
> > | fatfstest S {DISK\_NUMBER} | {DISK\_NUMBER}:logical driver number | scan all files on disk |
> > | fatfstest F {DISK\_NUMBER} | {DISK\_NUMBER}:logical driver number | format disk |
> > | fatfstest R {DISK\_NUMBER}{file\_name}  {length} | {DISK\_NUMBER}:logical driver number | read specified length of data  from the file |
> > | {file\_name}:file to story read data |
> > | {length}: length to be read |
> > | fatfstest W {DISK\_NUMBER}{file\_name}  {content\_p}{content\_len} | {DISK\_NUMBER}:logical driver number | write data to a file |
> > | {file\_name}:file to be written |
> > | {content\_p}: pointer to the data to be written |
> > | {content\_len}:length to be written |
> > | fatfstest D {DISK\_NUMBER}{file\_name}  {start\_addr}{content\_len} | {DISK\_NUMBER}:logical driver number | read the specified length of data from the specified address and write it to the specified file |
> > | {file\_name}:file to be written |
> > | {start\_addr}: start address for reading |
> > | {content\_len}:length to be written |
> > | fatfstest A {DISK\_NUMBER}{file\_name}  {content\_len}{test\_cnt} {start\_addr} | {DISK\_NUMBER}:logical driver number | auto test,write the data to the file and then read it, and compare the result  note: the data written to the SD card is read from the specified start\_addr |
> > | {file\_name}:file to be written |
> > | {content\_len}: length of comparison |
> > | {test\_cnt}:number of cycle tests |
> > | {start\_addr}:start address for reading |
> >
> > disk\_number的定义：
>
> ```
>         typedef enum
> {
>     DISK_NUMBER_RAM  = 0,
>     DISK_NUMBER_SDIO_SD = 1,
>     DISK_NUMBER_UDISK   = 2,
>     DISK_NUMBER_FLASH   = 3,
>     DISK_NUMBER_COUNT,
> } DISK_NUMBER;
> ```

<a id="id2"></a>

## 5 演示介绍

> demo执行的步骤如下：
>
> 1、将SD卡插入开发板，GPIO 连接方式如下（因为GPIO复用，此demo SDIO配置为单线模式）：
>
> ```
> SD_CLK----GPIO14
> SD_CMD----GPIO15
> SD_D0-----GPIO16
> SD_D1-----GPIO17
> SD_D2-----GPIO18
> SD_D3-----GPIO19
> ```
>
> 2、SD卡操作

fatfstest M 1 //挂载SD卡

> ```
> [16:06:10.103]发→◇fatfstest M 1
> [16:06:10.108]收←◆fatfstest M 1
> error file name,use defaultfilename.txt
> sd_card:I(203942):sd card has inited
> fmt=2
> fmt2=0
> Fatfs:I(203944):f_mount OK!
> Fatfs:I(203944):----- test_mount 1 over  -----
> ```

fatfstest S 1 //扫描SD卡

> ```
> [16:11:39.041]发→◇fatfstest S 1
> [16:11:39.046]收←◆fatfstest S 1
> error file name,use defaultfilename.txt
> Fatfs:I(532878):
> ----- scan_file_system 1 start -----
> Fatfs:I(532878):1:/
> Fatfs:I(532880):1:/autotest_400.txt
> Fatfs:I(532882):1:/dump_1.txt
> Fatfs:I(532884):scan_files OK!
> Fatfs:I(532886):----- scan_file_system 1 over  -----
> ```

fatfstest W 1 test.txt acl\_bk7236n\_write\_to\_test 24 //向文件test.txt中写入字符串”acl\_bk7236n\_write\_to\_test”

> ```
> [16:15:02.687]发→◇fatfstest W 1 test.txt acl_bk7236n_write_to_test 24
>
> [16:15:02.696]收←◆fatfstest W 1 test.txt acl_bkFatfs:I(736530):
> ----- test_fatfs 1 start -----
> Fatfs:I(736530):f_open "1:/test.txt"
> Fatfs:I(736530):.7236_write_to_test 24
>
> [16:15:02.837]收←◆TODO:FATFS sync feature
> Fatfs:I(736678):f_close OK
> Fatfs:I(736678):----- test_fatfs 1 over  -----
>
> append and write:test.txt
> [16:15:02.866]收←◆,acl_bk7236n_write_to_test
> ```

fatfstest R 1 test.txt 32 //从文件test.txt中读取32字节数据

> ```
> [16:18:30.473]发→◇fatfstest R 1 test.txt 32
> [16:18:30.478]收←◆fatfstest R 1 test.txt 32
> Fatfs:I(944312):
> ----- test_fatfs 1 start -----
> Fatfs:I(944312):f_open "1:/test.txt"
> Fatfs:I(944314):will read left_len = 24
> Fatfs:I(944314):f_read start:24 bytes
>
> ====== f_read one cycle - dump(len=24) begin ======
> 61 63 6c 5f 62 6b 37 32 35 36 5f 77 72 69 74 65
> 5f 74 6f 5f 74 65 73 74
> ====== f_read one cycle - dump(len=24)   end ======
>
> Fatfs:I(944328):f_read one cycle finish:left_len = 0
> Fatfs:I(944332):f_read: read total byte = 24
> Fatfs:I(944336):f_close OK
> Fatfs:I(944338):----- test_fatfs 1 over  -----
>
> read test.txt, len_h = 0, len_l = 32
> ```

fatfstest A 1 autotest.txt 2222 1 0 //从flash 0x0 地址读取2222字节数据保存到SD卡autotest.txt中，再将数据从autotest.txt中读取出来进行比较；此操作进行1次

> ```
> [16:31:11.077]发→◇fatfstest A 1 autotest.txt 2222 1 0
> [16:31:11.083]收←◆fatfstest A 1 autotest.txt 2222 1 0
>
> [16:31:11.143]收←◆TODO:FATFS sync feature
> Fatfs:I(195362):auto test succ
> ```

fatfstest D 1 dump.txt 0 10240 //从0x0地址读取10240字节数据保存到文件dump.txt中

> ```
> [16:33:15.934]发→◇fatfstest D 1 dump.txt 0 10240
> [16:33:15.939]收←◆fatfstest D 1 dump.txt 0 10240
> Fatfs:I(320154):
> ----- test_fatfs_dump 1 start -----
> Fatfs:I(320154):file_name=dump.txt,start_addr=0x0,len=10240
> Fatfs:I(320154):f_open start "1:/dump.txt"
> Fatfs:I(320154):f_write start
> Fatfs:I(320158):f_write end len = 10240
> Fatfs:I(320158):f_lseek start
> Fatfs:I(320158):f_close start
> TODO:FATFS sync feature
> ```

fatfstest F 1 //对SD卡进行格式化

> ```
> [17:43:49.985]发→◇fatfstest F 1
> [17:43:49.990]收←◆fatfstest F 1
> error file name,use defaultfilename.txt
> sd_card:I(327564):sd card has inited
> part=0
> sd_card:I(327564):card ver=2.0,size:0x01dacc00 sector(sector=512bytes)
> sdcard sector cnt=31116288
>
> [17:43:55.480]收←◆TODO:FATFS sync feature
> Fatfs:I(333054):f_mkfs OK!
> format :1
> ```
