---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_ipc/bk7259/zh_CN/v4.0.1/projects/aov/index.html
sdk_family: bk_ipc
chip: BK7259
processor: ''
sdk_version: v4.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bk7259-aov"></a>

# BK7259 AOV 低功耗摄像头示例工程

\> **开发状态：开发中（WIP）。**
\> 本工程用于验证 BK7259 CP/AP 协同、周期唤醒和低功耗运动检测，当前接口和测试覆盖仍在持续完善，暂不建议直接用于量产。

<a id="id1"></a>

## 1\. 工程简介

`aov` 是基于 BK7259 AP/CP 双核架构的 AOV（Always-On Video）低功耗摄像头示例工程。CP 常驻并维护产品状态、AON RTC 定时器和 AP 电源投票；需要采集图像时由 CP 启动 AP，AP 完成摄像头采集和运动检测后释放多媒体资源，再由 CP 关闭 AP。

当前默认检测周期为 1 秒。检测任务使用 MIPI CSI 摄像头的 ISP SP 通道采集 `640×360 NV12` 图像，通过 VG Lite GPU 转换为 `320×180 L8` 灰度图，再调用 SDK `motion_detect_compare_gray()` 完成帧间运动检测。

本文只介绍当前工程中已经接入、可以通过硬件动作、串口日志或调试命令观察和验证的功能。

<a id="id2"></a>

## 2\. 主要功能

- **CP/AP 状态机**：CP 管理产品状态和 AP job，AP 执行二维码扫描、Wi-Fi 连接或运动检测任务；
- **周期唤醒**：CP 使用 AON RTC 定时触发运动检测，默认周期为 1 秒；
- **AP 电源控制**：CP 按任务启动 AP，并在 AP 释放资源后关闭 AP；
- **SP-only 采集**：运动检测任务只打开 MIPI ISP SP 通道；
- **GPU 灰度转换**：VG Lite 将 `640×360 NV12` 转换并缩放为 `320×180 L8`；
- **运动检测**：使用 `motion_detect_compare_gray()` 比较当前帧和上一帧；
- **灰度帧保留**：CP 保存最后一帧灰度图，供下一次 AP 启动后继续比较；
- **AE 参数保留**：AP 关闭摄像头前保存曝光参数，下次启动时用于 Sensor 曝光预热；
- **安全下电握手**：AP 上报 `LAST_GRAY_READY` 和 `POWERDOWN_READY` 后，CP 才关闭 AP；
- **二维码扫描**：使用 ZBar 扫描 `640×360 NV12` 图像，可通过串口观察识别结果；
- **Wi-Fi 调试配置**：CP 使用 EasyFlash 保存测试凭据，通过跨核 IPC 下发给 AP；
- **AT 子系统**：默认端口为 5，启用 Wi-Fi/MISC AT 命令。

<a id="id3"></a>

## 3\. 工作流程

<a id="cp-ap"></a>

### 3.1 CP/AP 周期检测流程

```
CP AON RTC 周期到期
        │
        ▼
CP 设置 MOTION_CHECK job 并启动 AP
        │
        ▼
AP 打开 MIPI ISP SP 通道
        │
        ▼
640×360 NV12
        │
        ▼
VG Lite 转换/缩放
        │
        ▼
320×180 L8 灰度图
        │
        ▼
motion_detect_compare_gray()
        │
        ├── 未检测到运动：保存当前灰度帧和 AE 参数
        │
        └── 检测到运动：持续检测，连续 30 帧无运动后结束
        │
        ▼
AP 停止 Camera/GPU，回报 LAST_GRAY_READY、POWERDOWN_READY
        │
        ▼
CP 关闭 AP，并等待下一次 RTC 周期
```

RTC 保持固定周期运行。如果定时器到期时 AP 仍在工作，CP 会跳过本次重复唤醒，不会同时启动第二个检测任务。

<a id="id4"></a>

### 3.2 灰度帧与运动检测

- ISP SP 输入：`640×360 NV12`；
- 检测图像：`320×180 L8`；
- CP 灰度缓冲区：57600 字节；
- 默认差异阈值：64；
- 默认运动计数阈值：128；
- 首次没有历史帧时，两次采样间隔：1000 ms；
- 检测到运动后，连续 30 帧无运动才结束本次任务。

第一次运行没有历史灰度帧时，AP 会在当前启动周期内采集两帧建立基线。后续运行直接使用 CP 保存的上一帧进行第一次比较。

<a id="id5"></a>

### 3.3 二维码扫描

未配置 Wi-Fi 信息时，CP 启动 AP 执行二维码扫描任务。二维码输入来自 ISP SP 通道的 `640×360 NV12` 图像，ZBar 使用其灰度数据进行扫描。

识别到二维码后，串口日志会输出二维码数量、角点、长度和内容，可用于验证摄像头与二维码解码链路。

<a id="wi-fi"></a>

### 3.4 Wi-Fi 调试连接

测试 Wi-Fi 配置保存在 CP EasyFlash 的 `aov_device_info` 记录中。重启后，CP 启动 AP 并通过跨核 IPC 下发凭据，AP 发起 STA 连接，并在获取 IPv4 地址或连接失败后向 CP 上报结果。

当前调试记录中的密码以明文保存，请勿写入正式产品凭据。

<a id="id6"></a>

## 4\. 调试能力

<a id="id7"></a>

### 4.1 状态机检查

```
aov_sm status
aov_sm gray_info
aov_sm inject <event_id> [result]
```

- `status`：显示 CP 状态、AP 电源投票、当前 job 和序列号；
- `gray_info`：显示已保存灰度帧的尺寸、帧号和 CRC；
- `inject`：向 CP 状态机注入测试事件，仅用于状态机 smoke 测试。

<a id="id8"></a>

### 4.2 Wi-Fi 配置

```
aov_wifi set <ssid> <password|->
aov_wifi show
aov_wifi clear
```

- `set`：写入测试 SSID 和密码，使用 `-` 表示开放网络；
- `show`：显示 SSID、密码长度和有效状态，不输出密码；
- `clear`：清除测试 Wi-Fi 配置；
- 配置修改后需要重启设备才能应用。

<a id="id9"></a>

## 5\. 硬件配置

<a id="id10"></a>

### 5.1 摄像头

摄像头板级配置位于 `ap/ap_main.c`：

- MIPI I2C SCL：GPIO\_69，I2C bus id 1；
- MIPI I2C SDA：GPIO\_70；
- Sensor Reset：GPIO\_71；
- Sensor XCLK：GPIO\_59；
- Sensor 最大尺寸：2304×1296@20fps；
- ISP MP：2304×1296 NV12，Flexa 开启；
- AOV ISP SP：运行时配置为 640×360 NV12。

defconfig 同时编译 `CONFIG_CSI_SC3336` 和 `CONFIG_CSI_GC2053` Sensor 驱动；`ap_main.c` 当前板级尺寸按 SC3336 2304×1296@20fps 配置。

<a id="gpu"></a>

### 5.2 GPU 与显示

本工程不启用 LCD、MIPI DSI 和 DPU 显示链路，但启用 `CONFIG_VG_LITE_GPU` 和 `CONFIG_APP_GPU`。GPU 用于 AOV 灰度图转换和缩放，不用于显示。

<a id="id11"></a>

### 5.3 可选外设

- 串口：用于观察 AP/CP 日志和执行调试命令；
- LCD：不需要。

<a id="id12"></a>

## 6\. 快速开始

取码、编译环境和通用烧录见
[BK7259 IPC 方案快速入门](../get-started.md)。

本工程编译：

```
cd ~/armino/bk_solution_ipc/projects/aov
make bk7259 SDK_DIR=~/armino/bk_avdk_smp PROJECT=aov
```

本工程产物：

```
build/bk7259/aov/package/all-app.bin
```

将该文件按方案快速入门中的 BKFIL 步骤烧录。

<a id="id13"></a>

## 7\. 使用与验证

<a id="id14"></a>

### 7.1 使用前准备

1. 连接 BK7259 开发板和 MIPI CSI 摄像头；
2. 连接用于观察 AP/CP 日志和执行调试命令的串口；
3. 编译并烧录 `all-app.bin`；
4. 无需连接 LCD。

<a id="id15"></a>

### 7.2 Wi-Fi 与运动检测验证

写入测试 Wi-Fi：

```
aov_wifi set <ssid> <password|->
aov_wifi show
```

重启设备后可依次观察：

1. CP 从 EasyFlash 恢复 Wi-Fi 配置；
2. CP 启动 AP 并下发 Wi-Fi 凭据；
3. AP 发起 STA 连接并获取 IPv4 地址；
4. AP 进入灰度运动检测；
5. AP 保存灰度帧和 AE 参数并停止 Camera/GPU；
6. CP 收到就绪报告后关闭 AP；
7. RTC 周期到期后再次启动 AP 检测。

清除测试配置：

```
aov_wifi clear
```

<a id="id16"></a>

### 7.3 二维码扫描验证

清除 Wi-Fi 调试配置并重启后，AP 进入二维码扫描状态。将二维码置于摄像头视野内，可通过 `aov_ap_qr` 日志观察扫描耗时、二维码角点和识别内容。

<a id="id17"></a>

### 7.4 状态与灰度帧检查

```
aov_sm status
aov_sm gray_info
```

`status` 用于确认 CP 状态、AP 电源投票和当前 job；`gray_info` 用于确认最后一帧灰度图是否有效，并查看尺寸、帧号和 CRC。

<a id="id18"></a>

## 8\. 工程目录

```
projects/aov
├── common/
│   ├── aov_state_protocol.h      # CP/AP 状态、job、报告和共享数据
│   └── aov_debug.h
├── ap/
│   ├── ap_main.c                 # AP 初始化和 backend 注册
│   ├── state_machine/
│   │   ├── aov_ap_state_machine.c
│   │   ├── aov_ap_motion.c       # SP 采集、GPU 灰度转换、运动检测
│   │   ├── aov_ap_qr_provision.c # ZBar 二维码扫描
│   │   └── aov_ap_wifi.c         # Wi-Fi 连接和结果上报
│   └── config/bk7259_ap/defconfig
├── cp/
│   ├── cp_main.c
│   ├── state_machine/
│   │   ├── aov_cp_state_machine.c
│   │   ├── aov_cp_device.c       # 设备配置及 CLI
│   │   └── aov_cp_device_store.c # EasyFlash 持久化
│   ├── db_ipc_msg/               # CP/AP 消息通道
│   ├── powerctrl/                # AP 上下电控制
│   └── config/bk7259/defconfig
├── partitions/bk7259/
├── CMakeLists.txt
├── Makefile
└── dbuild.sh / dbuild.ps1
```

公共组件位于 `../../components/`。

<a id="id19"></a>

## 9\. 常见问题

**Q：为什么没有 LCD，却启用了 GPU？**

A：LCD、DSI 和 DPU 显示链路默认关闭；GPU 用于将 640×360 NV12 图像转换并缩放为 320×180 L8 灰度图，供运动检测使用。

**Q：为什么 AP 下电前需要两种报告？**

A：`LAST_GRAY_READY` 表示最后一帧灰度图已经写入 CP 共享缓冲区；`POWERDOWN_READY` 表示 AP 已停止 Camera/GPU 等资源。CP 同时满足条件后才关闭 AP，避免灰度数据尚未保存或硬件仍在使用时直接掉电。

**Q：如何查看上一帧是否保存成功？**

A：执行 `aov_sm gray_info`，检查 `valid`、尺寸、帧号和 CRC。
