# BK ARMINO 开发框架

> **TLDR:** ARMINO 是博通集成(Beken)的新一代 AIoT 软件开发框架，基于 CMake+Kconfig 构建系统，支持多芯片(BK7235/7236/7236N/7239)、多 RTOS(FreeRTOS/AliOS/LiteOS/RT-Thread)、WiFi+BT+低功耗+多媒体+安全启动的全功能 IoT 开发平台。

## 框架定位

ARMINO = **Ar** (ARM) + **mino** (minimal, 精简)，寓意轻量级 ARM IoT 框架。

对标 ESP-IDF (Espressif)，提供：
- 硬件无关的开发抽象层
- CMake 灵活构建 + Kconfig 配置
- 事件驱动的 WiFi/BT 驱动模型
- 完整的物联网安全框架
- 多 RTOS 适配层

## 芯片矩阵

```
BK7235 ——— 第一代 Armino，WiFi+BT，基础多媒体
   └─ BK7236  ——— 第二代 ARMINO IDK，双核(ARM+RISC-V)，安全启动，A/B OTA
       ├─ BK7236N ——— BK7236 增强版，新增 USB、更多低功耗模式
       └─ BK7239  ——— 旗舰，WiFi+BT+DVP Camera，强化安全
```

关键差异：
- **BK7235** 只有 ARM 核；**BK7236/7236N/7239** 支持 ARM+RISC-V 双核
- **BK7236N** 在 BK7236 基础上新增 USB、Close Multimedia 低功耗、CPU 投票频率
- **BK7239** 新增 DVP Camera 接口、mem API、更多安全特性
- WiFi API 在 BK7236+ 上统一为 v2.0（事件驱动，更灵活）

## 核心架构

### 构建系统

```
CMakeLists.txt (项目级)
  ├─ Kconfig (菜单配置)
  ├─ components/ (组件目录)
  │   ├─ wifi/
  │   ├─ bluetooth/
  │   ├─ peripheral/
  │   └─ ...
  └─ projects/ (项目模板)
      ├─ wifi/sta_connect/
      ├─ bluetooth/gatt_server/
      └─ ...
```

- CMake 管理组件依赖和编译
- Kconfig 生成 `sdkconfig` 配置
- 支持纯 CMake 项目和 Makefile 项目集成
- `bkfil` 工具用于 OTP/eFuse 烧录

### 驱动模型

三层抽象：
1. **BSP 层** — 芯片寄存器级驱动
2. **HAL 层** — 硬件抽象接口（如 `bk_gpio_t`, `bk_i2c_t`）
3. **Framework 层** — 事件驱动的应用接口（如 WiFi STA/AP/Monitor）

### WiFi 架构

```
App
 ├─ bk_wifi_sta_start/stop/connect/disconnect  (STA 操作)
 ├─ bk_wifi_ap_start/stop/set_config            (AP 操作)
 ├─ bk_wifi_monitor_start/stop                  (Monitor 模式)
 ├─ bk_wifi_scan_start/get_result               (扫描)
 └─ Event callback (EVENT_WIFI_STA_CONNECTED / DISCONNECTED / SCAN_DONE)
     ↓
WiFi Driver (supplicant + hardware)
```

### 安全体系

五层安全保障：
1. **Secure Boot** — 启动链校验（ROM → Bootloader → App）
2. **Flash AES** — 固件加密存储
3. **eFuse/OTP** — 硬件唯一标识和密钥存储
4. **LCS** (Life Cycle State) — 芯片生命周期管理（开发→量产→报废）
5. **FIH** (Fault Injection Hardening) — 抗故障注入攻击

## 关键技术点

### WiFi API v2.0 设计原则
- 事件驱动：调用 API 操作硬件，结果通过 Event 回调通知
- 配置结构体预留字段必须清零（保证前向兼容）
- 使用 `WIFI_DEFAULT_INIT_CONFIG()` 等宏初始化
- 不要在回调中做繁重处理，relay 到应用任务

### 低功耗方案
- DTIM 机制：基于 DTIM 间隔或 Listen Interval 唤醒
- RTC Sleep：深度睡眠，支持 GPIO/Touch 唤醒
- CPU 频率投票：根据外设需求动态调频
- 32K 时钟源选择：内部/外部 32K
- WiFi 保活：定时唤醒维持 TCP 连接

### A/B OTA 升级
- 双分区无位置依赖升级
- Hash 校验确保固件完整性
- 回滚机制：升级失败自动回退

## 与其他平台的对比

| | ARMINO (BK) | ESP-IDF (Espressif) |
|---|---|---|
| 构建系统 | CMake + Kconfig | CMake + Kconfig |
| WiFi 协议栈 | 自研 | 自研 (lwIP) |
| RTOS | FreeRTOS/AliOS/LiteOS/RTT | FreeRTOS |
| 双核 | ARM+RISC-V | Xtensa LX6/LX7 |
| 安全 | 五层安全体系 | Secure Boot + Flash Enc |

## Related

- [[iot-communication-protocols|物联网通信协议全景]]
- [[wifi-networking-stack|WiFi网络技术栈]]
- [[freertos-kernel-mechanisms|FreeRTOS内核机制全景]]
- [[embedded-software-design-patterns|嵌入式软件设计模式]]
- [[embedded-communication-protocols|嵌入式外设通信协议全景对比]]
- [BK Docs 分类页面](../categories/bk-doc.md)
