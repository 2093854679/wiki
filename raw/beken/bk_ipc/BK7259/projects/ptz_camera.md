---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_ipc/bk7259/zh_CN/v4.0.1/projects/ptz_camera/index.html
sdk_family: bk_ipc
chip: BK7259
processor: ''
sdk_version: v4.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bk7259"></a>

# BK7259 云台摄像机示例工程

<a id="id1"></a>

## 1\. 工程简介

`ptz_camera` 是面向 BK7259 云台网络摄像机的示例工程，集成 MIPI 摄像头、双轴步进电机、BLE/二维码配网、设备云连接、移动侦测、人形检测与自动跟随、日夜模式切换、红外灯/白光灯控制和远程设备控制。

工程基于 BK7259 AP/CP 双核架构。AP 运行摄像头、AI、云台和网络业务，CP 提供基础控制能力。当前默认配置为 Always-on 工作模式，不进入 AP 掉电保活流程。

本文只介绍当前工程中已经接入、可以通过硬件动作、串口日志或客户端命令观察和验证的功能。

<a id="id2"></a>

## 2\. 主要功能

- **启动状态机**：支持 `BOOTING`、`UNPROVISIONED`、`WORKING` 和 `ERROR` 状态；
- **电机自检**：上电后执行水平/垂直云台自检，再回到默认中间位置；
- **BLE 配网**：通过 `BK_IPC_XXXXXX` 广播接收 JSON-RPC 格式的配网参数；
- **二维码配网**：使用 ISP SP `640×360 NV12` 图像和 ZBar 解码配网二维码；
- **设备云连接**：解析二维码中的 Wi-Fi 和设备注册参数，完成联网、绑定和在线连接；
- **工作摄像头**：ISP MP 使用 `1920×1080 NV12 Flexa`，SP 使用 `320×180 NV12`；
- **移动侦测**：对 SP 灰度数据执行帧间检测，触发时编码 `320×180 JPEG` 并上传设备云；
- **人形检测**：使用 `320×180` 灰度输入运行 TFLite Micro 人形检测；
- **自动跟随**：根据人形框位置驱动水平/垂直步进电机，使目标保持在画面中心区域；
- **OSD 检测框**：将人形检测框更新到 1920×1080 视频坐标；
- **手动云台控制**：支持上、下、左、右、停止和回中；
- **自动日夜切换**：根据 ISP 亮度在日间彩色和夜间红外模式之间切换；
- **智能补光**：夜间检测到移动时可切换白光灯，移动结束后恢复红外模式；
- **报警音**：移动告警图片上传成功后可播放报警提示音；
- **恢复配置**：长按复位键 5 秒清除已保存的设备云配置并重启；
- **网络连接**：支持 Wi-Fi 和以太网 DHCP。

<a id="id3"></a>

## 3\. 工作流程

<a id="id4"></a>

### 3.1 首次启动与配网

设备首次启动或没有有效注册信息时，流程如下：

```
上电
  │
  ▼
云台电机自检并回中
  │
  ▼
进入 UNPROVISIONED
  │
  ├── BLE：广播 BK_IPC_XXXXXX，接收 ipc.provision.start
  │
  └── 二维码：打开 ISP SP 640×360 NV12，由 ZBar 扫描
  │
  ▼
解析 Wi-Fi / 注册地址 / 配网码
  │
  ▼
连接 Wi-Fi并完成设备云注册、绑定和上线
  │
  ▼
进入 WORKING
```

未注册状态下，BLE 配网和二维码配网可以作为两种配网入口，获得有效配置后共用相同的
Wi-Fi 连接、设备注册、绑定和上线流程。

<a id="ble"></a>

#### 3.1.1 BLE 配网

设备启动 BLE 广播，名称格式为 `BK_IPC_XXXXXX`，其中 `XXXXXX` 为设备蓝牙
MAC 地址后三个字节的十六进制表示。
客户端连接设备后，通过 JSON-RPC 调用 `ipc.provision.start`，参数放在 `params` 中：

```
{
  "jsonrpc": "2.0",
  "id": "request-1",
  "method": "ipc.provision.start",
  "params": {
    "v": 1,
    "s": "wifi_ssid",
    "p": "wifi_password",
    "id": "provision_code",
    "url": "https://provision.example.com"
  }
}
```

设备接受配置后返回：

```
{
  "jsonrpc": "2.0",
  "id": "request-1",
  "result": {
    "accepted": true
  }
}
```

随后设备停止 BLE 配网连接，使用收到的 Wi-Fi 信息联网并继续设备云注册流程。
串口可观察 `BLE provisioning config accepted` 和
`BLE provisioning accepted sent` 日志。

<a id="id5"></a>

#### 3.1.2 二维码配网

二维码内容必须为 JSON，并包含以下字段：

- `s`：Wi-Fi SSID；
- `p`：Wi-Fi 密码，可以为空字符串；
- `id`：设备配网码；
- `url`：设备配网服务地址；
- `v`：可选的协议版本号。

示例结构：

```
{
  "v": 1,
  "s": "wifi_ssid",
  "p": "wifi_password",
  "id": "provision_code",
  "url": "https://provision.example.com"
}
```

识别到有效二维码后，串口会输出 `QR provision config parsed`，随后可继续观察
Wi-Fi 和设备云事件日志。

<a id="id6"></a>

### 3.2 正常工作模式

进入 `WORKING` 后，摄像头同时启用：

- MP：1920×1080 NV12，Flexa 开启；
- SP：320×180 NV12，用于移动侦测和人形检测。

人形检测关闭时，监控任务执行灰度帧间移动侦测：

1. 读取 SP 帧的 Y 平面；
2. 调用 `motion_detect_compare_gray()`；
3. 首次检测到移动时编码一张 320×180 JPEG；
4. 设备云在线时立即上传，离线时保留一张待上传图片；
5. 连续 8 秒没有再次检测到移动后清除告警状态；
6. 报警音开启时，图片上传成功后播放报警提示音。

人形检测开启时，监控任务改为运行人形检测和自动跟随，并暂停普通帧间移动告警。

<a id="id7"></a>

### 3.3 人形检测与自动跟随

人形检测结果包含目标框、置信度和帧号。自动跟随使用第一目标框的中心位置控制云台：

- 置信度低于 0.60 时不跟随；
- 目标进入中心停止区域后停止电机；
- 目标偏离中心时控制水平、垂直或对角方向；
- 对检测框位置进行平滑和跳变确认，降低电机抖动；
- 最短控制命令间隔为 200 ms。

客户端执行手动 PTZ 控制时会暂停自动跟随；手动控制结束 10 秒后，如果人形检测仍然
开启，则恢复自动跟随。

<a id="id8"></a>

### 3.4 日夜模式与补光

自动灯光服务每秒读取一次 ISP 亮度，支持：

- `day`：日间彩色，红外灯和白光灯关闭；
- `night-ir`：夜间黑白，红外灯开启并切换 IR-CUT；
- `smart-white`：夜间移动触发时关闭红外灯并开启白光灯。

默认日转夜亮度阈值为 1000，夜转日阈值为 2000；连续 6 次满足条件后才切换，
避免环境亮度临界波动造成频繁切换。

<a id="id9"></a>

## 4\. 客户端控制能力

工程通过 `smart_ipc` 设备控制接口接收客户端命令，支持：

- 查询和开关人形检测；
- 查询和开关智能补光；
- 查询和开关报警音；
- 云台上、下、左、右移动；
- 停止云台；
- 云台回到默认中间位置。

当前电机移动速度为固件固定值；客户端命令中的 `speed` 参数会记录到日志，但不会改变
实际步进速度。方向移动达到软件边界或指定持续时间后自动停止。

<a id="id10"></a>

## 5\. 硬件配置

<a id="id11"></a>

### 5.1 摄像头

摄像头板级配置位于 `ap/ap_main.c`：

- MIPI I2C SCL：GPIO\_64，I2C bus id 1；
- MIPI I2C SDA：GPIO\_65；
- Sensor Reset：GPIO\_60；
- Sensor XCLK：GPIO\_59；
- 最大采集尺寸：1920×1080@20fps；
- 水平镜像：开启；
- 垂直翻转：关闭。

defconfig 编译了 GC20C3、SC3336 和 SC3336P MIPI Sensor 驱动。

<a id="id12"></a>

### 5.2 云台电机

云台使用两个四相步进电机：

- 水平 Pan：GPIO\_32、GPIO\_33、GPIO\_34、GPIO\_35；
- 垂直 Tilt：GPIO\_36、GPIO\_37、GPIO\_38、GPIO\_39；
- Pan 软件范围：0～4050 步，默认位置 2025；
- Tilt 软件范围：0～1100 步，默认位置 550。

软件步数用于位置控制，不代表固定机械角度；实际转动范围取决于电机、减速机构和安装结构。

<a id="id13"></a>

### 5.3 灯光与按键

- IR-CUT 夜间控制：GPIO\_47；
- IR-CUT 日间控制：GPIO\_48；
- 红外灯：GPIO\_49；
- 白光灯：GPIO\_50；
- 恢复配置按键：GPIO\_29，低电平有效，长按 5 秒。

<a id="id14"></a>

### 5.4 以太网

工程启用了 Ethernet DHCP 和 JLSEMI PHY：

- PHY 硬件复位：GPIO\_30；
- PHY 参考时钟：DCO 输出；
- 其余 ENET 引脚映射见 `ap/config/bk7259_ap/usr_gpio_cfg.h`。

<a id="id15"></a>

## 6 快速开始

取码、编译环境和通用烧录见
[BK7259 IPC 方案快速入门](../get-started.md)。

本工程编译：

```
cd ~/armino/bk_solution_ipc/projects/ptz_camera
make bk7259 SDK_DIR=~/armino/bk_avdk_smp PROJECT=ptz_camera
```

本工程产物：

```
build/bk7259/ptz_camera/package/all-app.bin
```

将该文件按方案快速入门中的 BKFIL 步骤烧录。

<a id="id16"></a>

## 7\. 使用与验证

<a id="id17"></a>

### 7.1 使用前准备

1. 连接 MIPI 摄像头、水平/垂直电机、IR-CUT、红外灯、白光灯和复位按键；
2. 根据需要连接麦克风、扬声器、Wi-Fi 天线或以太网；
3. 编译并烧录 `all-app.bin`；
4. 打开串口日志；
5. 首次启动时准备支持本工程 BLE 配网协议的客户端，或符合第 3.1 节格式的二维码。

上电后可以依次观察：

- 云台电机自检及回中；
- 状态从 `BOOTING` 进入 `UNPROVISIONED` 或 `WORKING`；
- 未注册设备启动 BLE 广播和二维码扫描；
- 已注册设备恢复网络和设备云连接；
- `WORKING` 状态下启动 Camera、Light 和 Monitor 服务。

<a id="id18"></a>

### 7.2 解除设备注册

执行以下任一命令可清除已保存的设备云注册信息：

```
pt_cloud unregister
pt_cloud reset_registration
```

执行成功后重启设备，会重新进入未注册和二维码配网流程。

也可以长按 GPIO\_29对应按键 5 秒清除注册信息并自动重启。

<a id="id19"></a>

### 7.3 日志检查

常用日志标签：

- `pt_state`：状态切换和设备云事件；
- `pt_hw`：电机自检、Camera 和恢复按键；
- `device_cloud`、`db-bd`：BLE 配网数据和设备云流程；
- `pt_qr`：二维码扫描与配置解析；
- `pt_monitor`：移动侦测、JPEG 上传和人形检测；
- `pt_motor`：电机初始化和速度模式；
- `pt_light`：亮度、日夜模式、IR-CUT 和补光状态；
- `pt_ctrl`：客户端设备控制命令。

<a id="id20"></a>

## 8\. 工程目录

```
projects/ptz_camera
├── ap/
│   ├── ap_main.c
│   ├── include/
│   │   ├── pt_state_types.h
│   │   ├── pt_motor.h
│   │   ├── pt_person_detect.h
│   │   └── ...
│   ├── src/
│   │   ├── services/
│   │   │   ├── pt_state_machine.c
│   │   │   ├── pt_hardware_service.c
│   │   │   ├── pt_qr_provision_service.c
│   │   │   ├── pt_monitor_service.c
│   │   │   ├── pt_light_service.c
│   │   │   └── pt_device_control.c
│   │   └── modules/
│   │       ├── pt_motor.c
│   │       ├── pt_person_detect.cc
│   │       └── pt_person_follow.c
│   └── config/bk7259_ap/
├── cp/
│   ├── cp_main.c
│   ├── db_ipc_msg/
│   ├── keepalive/
│   ├── powerctrl/
│   └── config/bk7259/
├── partitions/bk7259/
├── CMakeLists.txt
├── Makefile
└── dbuild.sh / dbuild.ps1
```

公共组件位于 `../../components/`。

<a id="id21"></a>

## 9\. 常见问题

**Q：为什么打开人形检测后不再上传普通移动侦测图片？**

A：当前监控任务在两种模式之间切换。人形检测开启时运行人形检测和自动跟随；
关闭后运行帧间移动侦测、JPEG 告警上传和报警音。

**Q：手动控制云台后为什么不会立刻恢复自动跟随？**

A：为避免手动命令与自动跟随争抢电机，手动控制结束后设置了 10 秒冷却时间。

**Q：当前是否会进入 AP 掉电低功耗？**

A：不会。默认配置为 `CONFIG_DOORBELL_KEEPALIVE_ALWAYS_ON=y`，当前工程保持 AP 常开。

**Q：如何重新进入配网状态？**

A：执行 `pt_cloud unregister` 后重启，或长按 GPIO\_29 对应按键 5 秒。
清除注册信息后，设备会同时恢复 BLE 广播和二维码扫描。
