---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_doorbell/bk7258/zh_CN/v3.1.1/intro/index.html
sdk_family: bk_doorbell
chip: BK7258
processor: ''
sdk_version: v3.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bk7258"></a>

# BK7258 门铃方案简介

<a id="id1"></a>

## 概述

BK7258 门铃方案是博通集成电路（上海）股份有限公司基于 BK7258 主控、Armino SMP（BK AVDK SMP）v3.1.x 架构开发的可视门铃与智能门锁音视频参考设计。该方案提供从摄像头采集、本地显示到网络图传与双向对讲的完整端到端示例工程，覆盖：

- UVC / DVP 摄像头采集；
- MJPEG 解码与 H.264 编码；
- LCD 显示与 LVGL；
- 双向音频与 AEC、Wi-Fi 图传、BLE 配网；
- AP 掉电低功耗保活。

本方案基于 BK7258 开发板运行，并配合 LCD、UVC/DVP 摄像头与 Speaker / Mic 或 UAC。开发板硬件资料见 [H/W 参考](hw-reference.md)。

各工程的默认分辨率、传感器与图传格式以该工程文档和 `defconfig` 为准，不要把某一种屏或某一种摄像头理解成全方案唯一配置。

备注

环境搭建、源码下载、编译与烧录，请参阅 [快速入门](get-started.md)。
配套软件下载与使用，请参阅 [配套软件](software.md)。
各参考工程的功能与使用说明，请参阅 [参考工程](projects.md)。

<a id="id2"></a>

## 设计理念

BK7258 门铃方案在 Armino SMP 之上交付门铃与门锁音视频业务：

- **BK7258 主控**：负责采集、本地显示、图传、双向音频、BLE 配网与门铃业务；
- **Armino SMP**：提供芯片、RTOS、驱动与网络协议栈；
- **本仓库**：提供方案与业务代码（`components/`、`projects/`），仓库根目录直接挂载。

<a id="id3"></a>

## 核心特性

<a id="id4"></a>

### 1\. 采集与显示

- UVC / DVP 采集；
- H.264 与 MJPEG 图传路径（按工程选择）；
- LCD 本地预览。

<a id="id5"></a>

### 2\. 图传与对讲

- Wi-Fi 图传；
- 双向音频与 AEC；
- BLE 配网。

<a id="id6"></a>

### 3\. 低功耗

- AP 掉电低功耗保活（`doorbell_lp`）。

<a id="id7"></a>

## 系统架构

BK7258 门铃方案与 BK AVDK SMP 的关系

本仓库交付的门铃方案与底层 BK AVDK SMP（Armino SMP SDK v3.1.x）的分工如下：

1. **开发与定位**：本方案是在 BK AVDK SMP 之上实现的场景化解决方案，聚焦门铃采集、图传、对讲与配网；芯片、RTOS、驱动、网络协议栈由 BK AVDK SMP 提供。
2. **代码边界**：本仓库（`bk_solution_doorbell`）主要提供方案与业务代码；硬件驱动、RTOS、内存管理、Wi-Fi / BLE 协议栈在 SMP 中。

Armino SMP 在 BK7258 上采用 AP（应用处理器） \+ CP（通信处理器）划分：

- **AP**：运行采集、编码、LCD、双向音频与门铃业务；
- **CP**：运行 Wi-Fi、BLE、协议栈与低功耗管理。
