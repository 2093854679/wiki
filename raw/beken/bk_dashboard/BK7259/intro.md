---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_dashboard/bk7259/zh_CN/v4.0.1/intro/index.html
sdk_family: bk_dashboard
chip: BK7259
processor: ''
sdk_version: v4.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bk7259"></a>

# BK7259 两轮车方案简介

<a id="id1"></a>

## 概述

BK7259 两轮车方案是博通集成电路（上海）股份有限公司基于 BK7259 主控、Armino SMP（BK AVDK SMP）v4.0.x 架构开发的两轮车智能仪表参考设计。该方案采用 BK7259 与 BK3515N 双芯片，以 1280x720 横屏仪表为主，同时提供 1024x600 示例工程，并具备：

- MIPI DSI \+ DPU \+ LVGL 仪表显示与开机 AVI 播放；
- 手机 JPEG 投屏，以及 Wi-Fi / BLE 图传；
- BLE / Wi-Fi 配网；
- 经典蓝牙音频、导航语音与多控制器蓝牙；
- SD 卡存储，以及完整的端到端示例工程。

备注

环境搭建、源码下载、编译、烧录与 BK3515N 从控烧录，请参阅 [快速入门](get-started.md)。
配套软件下载与使用，请参阅 [配套软件](software.md)。
各示例工程的功能与使用说明，请参阅 [参考工程](projects.md)。

<a id="id2"></a>

## 设计理念

BK7259 两轮车方案采用「主控 \+ 蓝牙从控」双芯片分工：

- **BK7259 主控**：负责仪表 UI、图传、配网、本地音视频与存储；
- **BK3515N 从控**：负责经典蓝牙等从控侧无线能力，与主控配合完成整机蓝牙体验；
- **Armino SMP**：提供芯片、RTOS、驱动与网络协议栈；本仓库在其上实现仪表业务与示例工程。

<a id="id3"></a>

## 核心特性

<a id="id4"></a>

### 1\. 仪表显示

- 1280x720 横屏 MIPI DSI \+ DPU；
- LVGL 仪表界面与开机 AVI 播放。

<a id="id5"></a>

### 2\. 图传与投屏

- 手机 JPEG 投屏；
- Wi-Fi 图传与 BLE 图传。

<a id="id6"></a>

### 3\. 无线连接

- BLE / Wi-Fi 配网；
- 经典蓝牙音频、导航语音、多控制器蓝牙。

<a id="id7"></a>

### 4\. 存储与整机外设

- **显示**：1280x720 横屏 MIPI DSI；
- **输入**：复位（RESET）、配网复位（K1）等按键；
- **存储**：SD 卡；
- **从控**：BK3515N 蓝牙。

开发板硬件资料见 [H/W 参考手册](hw-reference.md)。

<a id="id8"></a>

## 系统架构

BK7259 两轮车方案与 BK AVDK SMP 的关系

本仓库交付的两轮车方案与底层 BK AVDK SMP（Armino SMP SDK v4.0.x）的分工如下：

1. **开发与定位**：本方案是在 BK AVDK SMP 之上实现的场景化解决方案，聚焦仪表 UI、图传、配网与蓝牙音频等；芯片、RTOS、驱动、网络协议栈由 BK AVDK SMP 提供。
2. **代码边界**：本仓库（`bk_solution_dashboard`）主要提供方案与业务代码（`components/`、`projects/`，仓库根目录直接挂载）；硬件驱动、RTOS、内存管理、Wi-Fi / BLE 协议栈在 SMP 中。

Armino SMP 在 BK7259 上采用 AP（应用处理器） \+ CP（通信处理器）划分：

- **AP**：运行 LVGL 仪表、图传、音视频与业务逻辑；
- **CP**：运行 Wi-Fi、BLE、协议栈与低功耗管理。

软件架构层次（示意）:

```
应用层 (LVGL 仪表 / 投屏 / 音乐 / 电话)
        ↓
业务组件 (图传 / 音频 / 配网 / Dashcam)
        ↓
OS 层 (RTOS)
        ↓
硬件层 (BK7259 AP+CP + BK3515N)
```

<a id="id9"></a>

## 主要应用场景

1. **两轮车智能仪表**：LVGL 仪表显示、开机动画、物理按键交互；
2. **行车记录与回放**：Dashcam 循环录像、本地回放；
3. **手机投屏与图传**：JPEG 投屏、Wi-Fi / BLE 图传；
4. **车载娱乐**：本地音乐、K 歌 / MV、蓝牙电话与通讯录。

<a id="id10"></a>

## 技术优势

1. **与 SMP 配套的完整解决方案**：本方案聚焦两轮车仪表业务与 UI；硬件驱动 / RTOS / 协议栈由 BK AVDK SMP 提供。
2. **双芯片整机参考**：BK7259 主控 \+ BK3515N 从控，覆盖仪表显示与蓝牙从控侧能力。
3. **多套可跑示例工程**：1280x720 / 1024x600 仪表、行车记录、投屏配网，以及 Klok K 歌等产品形态，见 [参考工程](projects.md)。
