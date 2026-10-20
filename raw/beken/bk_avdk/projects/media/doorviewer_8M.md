---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_avdk/bk7258/zh_CN/v2.0.1/projects/media/doorviewer_8M/index.html
sdk_family: bk_avdk
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="doorviewer-8m"></a>

# Doorviewer\_8M

<a id="id1"></a>

## 1\. 简介

本工程是USB/DVP摄像头门锁的一个demo，支持端（BK7258设备）到端（手机APP端）的演示。默认使用8Mbyte PSRAM。

<a id="id2"></a>

### 1.1 规格

> 请参考 [../doorbell/index.html#id2](doorbell.md#id2)

<a id="id3"></a>

### 1.2 路径

> \<bk\_avdk源代码路径\>/projects/media/doorviewer\_8M

<a id="id4"></a>

## 2\. 框架图

> 请参考 [框架图](doorviewer.md#id4)

<a id="id6"></a>

## 3\. 配置

> 请参考 [配置](doorviewer.md#id7)

<a id="id8"></a>

### 3.1 区别

> doorviewer\_8M与doorviewer的区别在于前一个配置使用的8M psram，后一个配置使用的是16M psram。
>
> doorviewer\_8M工程cpu0上psram基本的宏配置如下：
>
> |  |  |  |
> | --- | --- | --- |
> | marco | value | implication |
> | CONFIG\_PSRAM | Y | 使能PSRAM模块 |
> | CONFIG\_PSRAM\_AS\_SYS\_MEMORY | Y | 使能PSRAM作为Heap |
> | CONFIG\_USE\_PSRAM\_HEAP\_AT\_SRAM\_OOM | N | 使能sram申请不到内存，从psram申请 |
> | CONFIG\_PSRAM\_HEAP\_BASE | 0x60700000 | 当前CPU上psram作为heap的起始地址 |
> | CONFIG\_PSRAM\_HEAP\_SIZE | 0x80000 | 当前CPU上psram作为heap的长度 |
> | CONFIG\_PSRAM\_HEAP\_CPU0\_BASE\_ADDER | 0x60700000 | psram作为heap的起始地址 |
>
> doorviewer\_8M工程cpu1上psram基本的宏配置如下：
>
> |  |  |  |
> | --- | --- | --- |
> | marco | value | implication |
> | CONFIG\_PSRAM | Y | 使能PSRAM模块 |
> | CONFIG\_PSRAM\_AS\_SYS\_MEMORY | Y | 使能PSRAM作为Heap |
> | CONFIG\_USE\_PSRAM\_HEAP\_AT\_SRAM\_OOM | N | 使能sram申请不到内存，从psram申请 |
> | CONFIG\_PSRAM\_HEAP\_BASE | 0x60780000 | 当前CPU上psram作为heap的起始地址 |
> | CONFIG\_PSRAM\_HEAP\_SIZE | 0x80000 | 当前CPU上psram作为heap的长度 |
> | CONFIG\_PSRAM\_HEAP\_CPU0\_BASE\_ADDER | 0x60700000 | psram作为heap的起始地址 |
>
> 从上面可以分析出，针对8M psram从0x60700000（CONFIG\_PSRAM\_HEAP\_CPU0\_BASE\_ADDER）-0x60800000作为heap使用，
> 两个核上各分了0x80000。

警告

使用时请注意工程与PSRAM大小（型号）是否适配，如果使用16M psram的配置在8M板子上运行时，可能使用的psram会超过最大范围，则会造成dump。

<a id="id9"></a>

## 4\. 演示说明

> 请访问
> [APP使用文档](../../../bk_toolkit/iotapp/app_usage/app_usage_guide.md#debug)
> 查看。
>
> 演示结果：运行时会启动UVC/DVP，LCD和AUDIO，LCD显示UVC输出JPEG（864X480）图像经过解码和旋转90°后显示到LCD(480X854)上，
> 同一JPEG图像经WIFI图传到手机上显示(864X480)。

提示

如果您没有云账号权限，可以使用debug模式，设置局域网TCP图传方式。

<a id="id10"></a>

## 5\. 代码讲解

> 请参考 [代码讲解](doorviewer.md#id13)
