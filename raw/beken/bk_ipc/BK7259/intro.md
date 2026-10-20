---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_ipc/bk7259/zh_CN/v4.0.1/intro/index.html
sdk_family: bk_ipc
chip: BK7259
processor: ''
sdk_version: v4.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bk7259-ipc"></a>

# BK7259 IPC 方案简介

<a id="id1"></a>

## 概述

BK7259 IPC 方案是博通集成电路（上海）股份有限公司基于 BK7259 主控、Armino SMP（BK AVDK SMP）v4.0.x 架构开发的智能网络摄像头参考设计。该方案提供无屏 IPC、AOV 低功耗与 ISP/H264E 图像质量联调等示例工程，覆盖：

- MIPI CSI 摄像头采集与 H.264 硬件编码；
- Wi-Fi 实时图传、BLE 配网；
- 双向音频与 AEC、语音唤醒（KWS/ASR）；
- AP 掉电低功耗保活。

本方案基于 BK7259 开发板运行，并配合 MIPI CSI 摄像头与 Speaker / Mic。开发板硬件资料见 [H/W 参考](hw-reference.md)。

各工程的默认传感器与分辨率以该工程文档和 `defconfig` 为准，不要把某一种 Sensor 或某一种分辨率理解成全方案唯一配置。

备注

环境搭建、源码下载、编译与烧录，请参阅 [快速入门](get-started.md)。
配套软件下载与使用，请参阅 [配套软件](software.md)。
各参考工程的功能与使用说明，请参阅 [参考工程](projects.md)。

<a id="id2"></a>

## 设计理念

BK7259 IPC 方案在 Armino SMP 之上交付网络摄像头业务：

- **BK7259 主控**：负责采集、编码、图传、双向音频、BLE 配网与 IPC 业务；
- **Armino SMP**：提供芯片、RTOS、驱动与网络协议栈；
- **本仓库**：提供方案与业务代码（`components/`、`projects/`），仓库根目录直接挂载。

<a id="id3"></a>

## 核心特性

<a id="id4"></a>

### 1\. 采集与编码

- MIPI CSI 采集；
- H.264 硬件编码；
- ISP / H264E 联调工程可通过 Wi-Fi 预览原始帧与码流。

<a id="id5"></a>

### 2\. 图传与配网

- Wi-Fi 实时图传；
- BLE 配网；
- 双向音频与语音唤醒。

<a id="id6"></a>

### 3\. 低功耗

- AP 掉电低功耗保活；
- AOV 工程提供 CP/AP 状态机与事件唤醒（开发中）。

<a id="id7"></a>

## 系统架构

BK7259 IPC 方案与 BK AVDK SMP 的关系

本仓库交付的 IPC 方案与底层 BK AVDK SMP（Armino SMP SDK v4.0.x）的分工如下：

1. **开发与定位**：本方案是在 BK AVDK SMP 之上实现的场景化解决方案，聚焦无屏 IPC 采集、图传、配网与低功耗；芯片、RTOS、驱动、网络协议栈由 BK AVDK SMP 提供。
2. **代码边界**：本仓库（`bk_solution_ipc`）主要提供方案与业务代码；硬件驱动、RTOS、内存管理、Wi-Fi / BLE 协议栈在 SMP 中。

Armino SMP 在 BK7259 上采用 AP（应用处理器） \+ CP（通信处理器）划分：

- **AP**：运行采集、编码、图传与 IPC 业务；
- **CP**：运行 Wi-Fi、BLE、协议栈与低功耗管理。

软件架构层次（示意）:

```
应用层 (IPC 业务 / 配网 / 联调)
        ↓
多媒体 (采集 / 编码 / 音频)
        ↓
OS 层 (RTOS)
        ↓
硬件层 (BK7259 AP+CP)
```
