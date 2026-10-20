---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7236/zh_CN/v2.0.1/developer-guide/peripheral/bk_dma.html
sdk_family: bk_idk
chip: BK7236
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="dma"></a>

# DMA 使用指南

<a id="id1"></a>

## 概述

DMA 传输将数据从一个地址空间复制到另一个地址空间，提供在外设和存储器之间或者存储器与存储器之间的高速数据传输。
一个典型的 DMA 实现通常如下图所示。

<a id="id10"></a>
![DMA Overview](../../../../_assets/2b86f9450b737a167f1f-dma.png)


DMA Overview

备注

实际 DMA 架构实现可能与上图不同，上图主要为方便理解的一个抽象概述图。

CPU，DMA 控制器，DMA 内存通过总线相连。一个 DMA 控制器可支持多个通道，不同的通道可并发传输。外设与内存之间进行数据传输前，需要先选择一个通道，配置好相应的参数。

BK7236 支持两个 DMA 控制器，第个控制器支持 8 个 DMA 通道，虽然 8 个通道能同时工作，但由于总线只有一条，因此在特定时刻实际只有一个通道能在总线上传输数据。当多个
不同的 DMA 通道在同一时刻均有数据传输时，由 DMA 对通道进行调度。DMA 通道有两种调度方式：

> - 轮询调度，所有通道同一优先级，先请求先调度
> - 基于优先级调度，优先级高的先调度，可通过:cpp:func:bk\_dma\_init 设置调度方式与优先级。

<a id="id2"></a>

## DMA 配置

为了进行 DMA 传输，通常需要进行下述配置:

> - 配置源与目的设备
> - 设置源与目的设备的数据宽度
> - 设置数据量
> - 传输次数（单次传输或者循环传输)

<a id="id3"></a>

## DMA 传输次数设置

DMA 传输次数可通过传输模式来设置， DMA 有两种传输模式：

> - SINGLE 模式
> - REPEAT 模式

<a id="id4"></a>

### 单次模式

单次模式如下图所示，从 start 传输到 start \+ len 结束， 通常 len 设置成 end \- start， 即整个块的长度。

<a id="id11"></a>
![DMA Single Mode](../../../../_assets/acad70249622cd84bcab-dma_single.png)


DMA Single Mode

<a id="id5"></a>

### 循环模式

循环模式如下图所示，DMA 从 start 传输到 end 后会再次从 start 传输到 end, 一直重复直到 DMA 被 stop。
当 SRC or DST 设备为单地址时，在 Repeat 模式下每次均传输 Start 所指向的地址，直到 DMA 被 stop。

<a id="id12"></a>
![DMA Repeat Mode](../../../../_assets/c36e97b66daee66a4b5a-dma_repeat.png)


DMA Repeat Mode

<a id="id6"></a>

## DMA 传输场景

DMA 地址配置基本原则：

> - 如果要传输的地址为单地址，即进行 DMA 传输时设备地址可用的地址长度等于数据宽度时，
>   则只需配置 start 地址，end 地址配置成 0。如 UART 设备， 位宽为 8bits, DMA 传输时每次都只使用这 8bits 传输，
>   因此只需配置 start 地址为 UART FIFO 地址，end 设置成 0\.
> - 如果要传输的地址为块地址，即地址长度超过数据宽度，则 Start配置成块地址的起始地址， end 配置成块地址的结束地址

具体应用可分成下述三种场景：

> - 单地址到单地址传输
> - 单地址到块地址传输
> - 块地址到块地址传输

<a id="id7"></a>

### 单地址到单地址传输

<a id="id13"></a>
![DMA case1](../../../../_assets/f48c645bf0d33fa61226-dma_s3.png)


DMA case1

如上图所示, SRC/DST 设备均只需要配置 start 地址， end 为 0\.

<a id="id8"></a>

### 单地址到块地址传输

<a id="id14"></a>
![DMA case2](../../../../_assets/cf8efe7dd36ef65a574b-dma_s2.png)


DMA case2

如上图所示, SRC 设备均只需要配置 start 地址， end 为 0， end 设备配置 start/end 地址。

<a id="id9"></a>

### 块地址到块地址传输

<a id="id15"></a>
![DMA case3](../../../../_assets/381b9100d3901d13785b-dma_s1.png)


DMA case3

如上图所示, SRC 设备均只需要配置 start 地址， end 为 0， end 设备配置 start/end 地址。
