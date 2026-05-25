# OV‑Watch 任务系统概览

目录
- [1. user_TasksInit.c — FreeRTOS 任务初始化](#1-usertasksinitc--freertos-任务初始化)
- [2. user_HardwareInitTask.c — 硬件初始化任务](#2-userhardwareinittaskc--硬件初始化任务)
- [3. user_RunModeTasks.c — 运行模式任务](#3-userrunmodetasksc--运行模式任务)
- [4. user_KeyTask.c — 按键任务](#4-userkeytaskc--按键任务)
- [5. user_ScrRenewTask.c — 屏幕刷新任务](#5-userscrrenewtaskc--屏幕刷新任务)
- [6. user_ChargCheckTask.c — 充电检查任务](#6-userchargchecktaskc--充电检查任务)
- [7. user_DataSaveTask.c — 数据保存任务](#7-userdatasavetaskc--数据保存任务)
- [8. user_SensUpdateTask.c — 传感器更新任务](#8-usersensupdatetaskc--传感器更新任务)
- [9. user_MessageSendTask.c — 消息发送任务](#9-usermessagesendtaskc--消息发送任务)
- [任务优先级](#任务优先级)
- [消息队列](#消息队列)
- [传感器数值更新机制](#传感器数值更新机制)
- [系统运行模式详解](#系统运行模式详解)
- [待机模式唤醒机制详解](#待机模式唤醒机制详解)

## 1. user_TasksInit.c — FreeRTOS 任务初始化

### 头文件包含 (第1-21行)
- 包含系统、GUI、任务相关的头文件

### 定时器句柄 (第32行)
- `IdleTimerHandle`: 空闲定时器句柄

### 任务句柄和属性定义 (第35-138行)
- 定义所有任务的句柄和属性（名称、栈大小、优先级）
- 包括硬件初始化、LVGL处理、看门狗、空闲、停止、按键、屏幕刷新、传感器数据、心率数据、充电检查、消息发送、MPU检查、数据保存等任务

### 消息队列定义 (第141-148行)
- 定义6个消息队列：按键、空闲、停止、空闲打断、Home更新、数据保存

### User_Tasks_Init() 函数 (第159-200行)
- 创建定时器（100ms周期）
- 创建所有消息队列
- 创建所有任务
- 发送初始Home更新消息

### TaskTickHook() 函数 (第208-239行)
- 每1ms调用一次
- 更新LVGL时钟
- 处理计时器页面的时间计数
- 更新心率时间计数

### LvHandlerTask() 函数 (第247-260行)
- LVGL主处理任务
- 检测LVGL非活跃时间，发送空闲打断消息
- 调用LVGL任务处理器

### WDOGFeedTask() 函数 (第268-278行)
- 看门狗喂狗任务
- 每100ms喂一次狗

## 2. user_HardwareInitTask.c — 硬件初始化任务

### 头文件包含 (第1-31行)
- 包含系统、用户、BSP、UI相关头文件

### HardwareInitTask() 函数 (第46-185行)
- **第50行**: 挂起所有任务
- **第53-56行**: 配置RTC唤醒定时器
- **第58-59行**: 启动UART DMA接收
- **第62行**: 启动PWM
- **第65行**: 初始化延时函数
- **第70行**: 初始化电源管理
- **第73行**: 初始化按键
- **第76-82行**: 初始化AHT21温湿度传感器（重试3次）
- **第84-90行**: 初始化LSM303指南针传感器（重试3次）
- **第92-97行**: 初始化SPL06气压传感器（重试3次）
- **第99-105行**: 初始化MPU6050陀螺仪（重试3次）
- **第107-114行**: 初始化EM7028心率传感器（重试3次）
- **第117-146行**: 初始化EEPROM并读取设置
- **第149-151行**: 初始化BLE并禁用
- **第157-159行**: 初始化触摸屏
- **第161-171行**: 初始化LCD并显示欢迎界面
- **第174-179行**: 初始化LVGL和UI
- **第181行**: 恢复所有任务
- **第182行**: 删除自身任务

## 3. user_RunModeTasks.c — 运行模式任务

### 全局变量 (第25行)
- `IdleTimerCount`: 空闲计时器计数

### IdleEnterTask() 函数 (第36-55行)
- 处理屏幕亮度控制
- 接收空闲消息时降低亮度到5
- 接收空闲打断消息时恢复亮度并重置计时器

### StopEnterTask() 函数 (第62-165行)
- 处理STOP低功耗模式
- **第69行**: 等待停止消息
- **第73-86行**: 进入睡眠前的操作（关闭UART、LCD、触摸）
- **第91-97行**: 进入STOP模式
- **第105-110行**: 唤醒后恢复系统时钟
- **第116-133行**: 检查MPU抬腕状态
- **第136-145行**: 检查唤醒条件（按键、充电、抬腕）
- **第147-158行**: 唤醒后恢复外设

### IdleTimerCallback() 函数 (第167-185行)
- 每100ms调用一次
- 根据设置的时间值发送息屏和待机消息

## 4. user_KeyTask.c — 按键任务

### KeyTask() 函数 (第22-52行)
- 循环扫描按键状态
- **第29行**: 调用按键扫描函数
- **第31-35行**: 按键1按下时发送按键消息和空闲打断消息
- **第37-48行**: 按键2按下时，如果在Home页面则进入待机，否则发送按键消息

## 5. user_ScrRenewTask.c — 屏幕刷新任务

### ScrRenewTask() 函数 (第26-60行)
- 处理按键消息
- **第34-45行**: 按键1按下时返回上一页，如果回到菜单页则让传感器休眠
- **第47-56行**: 按键2按下时返回底部页面，并让传感器休眠

## 6. user_ChargCheckTask.c — 充电检查任务

### ChargPageEnterTask() 函数 (第25-45行)
- 监控充电状态变化
- **第30行**: 检查充电中断标志
- **第32-33行**: 重置空闲计时器和中断标志
- **第34-36行**: 如果正在充电且不在充电页面，则进入充电页面
- **第38-41行**: 如果不在充电且在充电页面，则退出充电页面

## 7. user_DataSaveTask.c — 数据保存任务

### EEPROM数据描述 (第21-32行)
- 说明EEPROM中存储的数据结构

### DataSaveTask() 函数 (第44-88行)
- 接收数据保存消息队列
- **第57-60行**: 保存用户设置（抬腕开关、APP开关）
- **第62-75行**: 检查日期变化，如果日期改变则重置步数
- **第76-83行**: 如果日期未变则保存当前步数

## 8. user_SensUpdateTask.c — 传感器更新任务

### MPUCheckTask() 函数 (第46-74行)
- MPU6050状态检查任务
- 检测抬腕/放腕状态
- 300ms周期检查

### HRDataUpdateTask() 函数 (第81-108行)
- 心率数据更新任务
- 只在心率页面时工作
- 50ms周期更新

### SensorDataUpdateTask() 函数 (第116-233行)
- 传感器数据更新任务
- 500ms周期更新
- 更新电池、步数、温湿度、指南针、气压等数据

## 9. user_MessageSendTask.c — 消息发送任务

### MessageSendTask() 函数 (第85-136行)
- 串口/BLE消息处理任务
- 处理命令接收和数据发送
- 1000ms周期检查

## 任务优先级

1. **osPriorityHigh3**: HardwareInitTask (硬件初始化)

2. **osPriorityHigh2**: WDOGFeedTask (看门狗)

3. **osPriorityHigh1**: StopEnterTask (停止模式)

4. **osPriorityHigh**: IdleEnterTask (空闲模式)

5. **osPriorityNormal**: KeyTask (按键)

6. **osPriorityLow1**: ScrRenewTask, SensorDataTask, HRDataTask, ChargPageEnterTask, MessageSendTask (按键屏幕刷新、传感器数据、心率数据、充电检查、串口消息发送)

7. **osPriorityLow2**: MPUCheckTask, DataSaveTask (MPU检查、数据保存)

8. **osPriorityLow**: LvHandlerTask (LVGL处理)

	- 总体原则：先保**系统安全与功耗，再保交互实时性，最后做后台工作**。

	- osPriorityHigh3 HardwareInitTask：尽快完成一次性硬件/外设/传感器初始化，缩短上电到可用时间；完成后自删，避免长期占用高优先级。

	- osPriorityHigh2 WDOGFeedTask：喂狗属于“安全底线”，优先级必须高于大  多数任务，避免因排队导致误复位。

	- osPriorityHigh1 StopEnterTask：待机/唤醒切换牵涉功耗与时钟/外设重配，要求响应迅速，优先于一般交互与后台采集。

	- osPriorityHigh IdleEnterTask：屏幕亮度/空闲管理需较快响应用户操作与定时事件，但不应压过喂狗与待机切换。

	- osPriorityNormal KeyTask：按键是人机交互入口，延迟容忍度中等（毫秒级即可），置于常规优先级即可确保流畅。

	- osPriorityLow1 ScrRenewTask/SensorDataTask/HRDataTask/ChargPageEnterTask/MessageSendTask：界面刷新与周期采集/通信属“业务层后台”，可被更高优先级打断，不影响安全与功耗控制。

	- osPriorityLow2 MPUCheckTask/DataSaveTask：抬腕判定/数据落盘更不敏感（几十到上百毫秒可接受），置更低优先级减少对前台交互与功耗控制的干扰。

	- osPriorityLow LvHandlerTask：LVGL主循环已配合 osDelay(1) 让出CPU，置最低优先级以避免抢占时序关键任务；UI帧率主要受空闲时间与定时驱动影响。

	- 额外考虑：

	- 高优先级任务须短小、少阻塞，避免饿死低优先级。

	- 涉及互斥/队列时，尽量由低优先级向高优先级发送，避免优先级反转风险。

	- 若后期发现交互卡顿或功耗切换不够迅速，可在 High/Normal/Low1 间微调对应任务。

## 消息队列

### 1. **Key_MessageQueue** - 按键消息队列

**发送者**：
- `user_KeyTask.c` - `KeyTask()` 函数
  - 第33行：KEY1按键按下时发送1
  - 第45行：KEY2按键按下时发送2

**接收者**：
- `user_ScrRenewTask.c` - `ScrRenewTask()` 函数
  - 第31行：接收按键消息进行屏幕更新

**用途**：处理物理按键事件，触发屏幕刷新

---

### 2. **Idle_MessageQueue** - 空闲息屏消息队列

**发送者**：
- `user_RunModeTasks.c` - `IdleTimerCallback()` 函数
  - 第176行：100ms空闲定时器达到息屏时间时发送

**接收者**：
- `user_RunModeTasks.c` - `IdleEnterTask()` 函数
  - 第44行：接收息屏消息，降低屏幕亮度到5%

**用途**：触发屏幕亮度降低，进入息屏状态

---

### 3. **Stop_MessageQueue** - 



**发送者**：
- `user_KeyTask.c` - `KeyTask()` 函数
  - 第40行：KEY2在HomePage按下时发送
- `user_RunModeTasks.c` - `IdleTimerCallback()` 函数
  - 第184行：空闲定时器达到待机时间时发送
- `user_SensUpdateTask.c` - `MPUCheckTask()` 函数
  - 第66行：检测到手腕放下时发送

**接收者**：
- `user_RunModeTasks.c` - `StopEnterTask()` 函数
  - 第70行：接收待机消息，进入STOP模式

**用途**：触发系统进入深度睡眠模式

---

### 4. **IdleBreak_MessageQueue** - 空闲打断消息队列

**发送者**：
- `user_TasksInit.c` - `TaskTickHook()` 函数
  - 第226行：LVGL不活跃时发送
- `user_TasksInit.c` - `LvHandlerTask()` 函数
  - 第255行：LVGL处理任务中发送
- `user_KeyTask.c` - `KeyTask()` 函数
  - 第34行：KEY1按键时发送
  - 第46行：KEY2按键时发送
- `user_SensUpdateTask.c` - 多个函数
  - 第90行：`HRDataUpdateTask()` 中发送
  - 第167行：`SensorDataUpdateTask()` 中发送
  - 第179行：`SensorDataUpdateTask()` 中发送
  - 第198行：`SensorDataUpdateTask()` 中发送
- `user_MessageSendTask.c` - `MessageSendTask()` 函数
  - 第93行：处理UART消息时发送

**接收者**：
- `user_RunModeTasks.c` - `IdleEnterTask()` 函数
  - 第49行：接收打断消息，恢复屏幕亮度

**用途**：打断空闲状态，恢复屏幕亮度

---

### 5. **HomeUpdata_MessageQueue** - Home页面更新消息队列

**发送者**：
- `user_TasksInit.c` - `User_Tasks_Init()` 函数
  - 第198行：系统初始化时发送
- `user_RunModeTasks.c` - `StopEnterTask()` 函数
  - 第159行：从STOP模式唤醒后发送

**接收者**：
- `user_SensUpdateTask.c` - `SensorDataUpdateTask()` 函数
  - 第124行：接收Home更新消息，更新传感器数据

**用途**：触发Home页面传感器数据更新

---

### 6. **DataSave_MessageQueue** - 数据保存消息队列

**发送者**：
- `user_SensUpdateTask.c` - `SensorDataUpdateTask()` 函数
  - 第159行：完成Home数据更新后发送

**接收者**：
- `user_DataSaveTask.c` - `DataSaveTask()` 函数
  - 第50行：接收数据保存消息，保存到EEPROM

**用途**：触发用户设置和步数数据保存到EEPROM

---

### 消息队列流程图

```
按键事件 → Key_MessageQueue → 屏幕更新
    ↓
空闲定时器 → Idle_MessageQueue → 屏幕变暗
    ↓
空闲定时器 → Stop_MessageQueue → 深度睡眠
    ↓
用户交互 → IdleBreak_MessageQueue → 屏幕恢复
    ↓
系统唤醒 → HomeUpdata_MessageQueue → 传感器更新
    ↓
数据更新 → DataSave_MessageQueue → EEPROM保存
```

**总结**：这6个消息队列构成了完整的用户交互、电源管理和数据持久化系统！

## 定时器使用情况

### 定时器类型和数量
**OV-Watch 项目使用了多种类型的定时器**，总共约 **10+ 个定时器**：

#### 1. FreeRTOS 软件定时器
- **IdleTimerHandle**: 空闲定时器
  - **周期**: 100ms
  - **功能**: 管理屏幕亮度和待机时间
  - **回调函数**: `IdleTimerCallback()`
  - **处理任务**:
    - 屏幕亮度管理（息屏）
    - 待机时间计数
    - 自动进入停止模式

#### 2. LVGL 软件定时器
- **ui_MainTimer**: 主定时器
  - **周期**: 1000ms (1秒)
  - **功能**: 主界面更新

- **ui_HomePageTimer**: 主页定时器
  - **周期**: 500ms
  - **功能**: 主页时钟和传感器数据更新

- **ui_HRPageTimer**: 心率页定时器
  - **周期**: 50ms
  - **功能**: 心率数据实时更新

- **ui_SPO2PageTimer**: 血氧页定时器
  - **周期**: 500ms
  - **功能**: 血氧数据更新

- **ui_EnvPageTimer**: 环境页定时器
  - **周期**: 500ms
  - **功能**: 环境传感器数据更新

- **ui_EcompassPageTimer**: 指南针页定时器
  - **周期**: 500ms
  - **功能**: 指南针数据更新

- **ui_TimerPageTimer**: 计时器页定时器
  - **周期**: 10ms
  - **功能**: 计时器精确计时

- **ui_ChargPageTimer**: 充电页定时器
  - **周期**: 2000ms
  - **功能**: 充电状态更新

#### 3. 硬件定时器
- **TIM3_CH3**: PWM定时器
  - **功能**: LCD背光亮度控制
  - **启动**: `HAL_TIM_PWM_Start(&htim3,TIM_CHANNEL_3)`

- **RTC Wake-up Timer**: RTC唤醒定时器
  - **周期**: 约0.98秒 (2000/16)
  - **功能**: 从STOP模式唤醒MCU
  - **配置**: `HAL_RTCEx_SetWakeUpTimer_IT(&hrtc, 2000, RTC_WAKEUPCLOCK_RTCCLK_DIV16)`

#### 4. 系统定时器
- **SysTick**: 系统滴答定时器
  - **周期**: 1ms
  - **功能**: FreeRTOS任务调度、LVGL tick更新
  - **回调**: `TaskTickHook()`

### 定时器处理的任务

#### 1. 用户界面更新
- **主页时钟**: 每500ms更新一次
- **传感器数据**: 各页面定时更新传感器数据
- **动画效果**: LVGL内部动画定时器

#### 2. 系统管理
- **空闲管理**: 100ms检查一次空闲状态
- **电源管理**: 定时检查充电状态
- **看门狗**: 100ms喂一次外部看门狗

#### 3. 硬件控制
- **背光控制**: PWM控制LCD背光亮度
- **唤醒机制**: RTC定时唤醒MCU
- **传感器采样**: 定时读取传感器数据

#### 4. 数据采集
- **心率数据**: 50ms高频率采集
- **环境数据**: 500ms采集温湿度、气压等
- **运动数据**: 定时采集加速度、磁力计数据

### 定时器设计特点

#### 1. 分层设计
- **硬件层**: RTC、PWM等硬件定时器
- **系统层**: FreeRTOS软件定时器
- **应用层**: LVGL定时器

#### 2. 频率优化
- **高频**: 心率数据采集 (50ms)
- **中频**: 界面更新 (500ms)
- **低频**: 系统管理 (1000ms+)

#### 3. 功耗考虑
- **RTC唤醒**: 低功耗STOP模式下的唯一唤醒源
- **动态调整**: 根据页面需求动态创建/删除定时器
- **智能管理**: 空闲时减少定时器活动

## 信号量使用情况

### 信号量使用现状
**OV-Watch 项目中基本没有使用信号量**，具体情况如下：

#### 1. 信号量相关代码
- **仅发现一处声明**: `BSP\LCD\lcd.c` 第10行声明了 `extern osSemaphoreId_t DMA_SemaphoreHandle;`
- **但未实际使用**: 在整个项目中没有找到 `osSemaphoreNew`、`osSemaphoreAcquire`、`osSemaphoreRelease` 等信号量操作函数

#### 2. 为什么没有使用信号量？

**项目采用了消息队列替代信号量**：
- 使用 **6个消息队列** 进行任务间通信
- 消息队列比信号量更适合这种应用场景

#### 3. 消息队列 vs 信号量的选择

**消息队列的优势**：
- **数据传递**: 可以传递具体数据，而不仅仅是信号
- **多任务通信**: 支持一对多、多对一的通信模式
- **优先级管理**: 支持消息优先级
- **缓冲机制**: 内置消息缓冲，避免消息丢失

**信号量的优势**：
- **资源保护**: 更适合保护共享资源
- **同步机制**: 更适合任务同步
- **轻量级**: 占用资源更少

#### 4. 项目中的同步机制

**替代方案**：
- **任务挂起/恢复**: `vTaskSuspendAll()` / `xTaskResumeAll()`
- **消息队列**: 6个消息队列处理所有任务间通信
- **定时器**: `osTimerNew()` 处理周期性任务
- **中断**: 硬件中断处理外部事件

#### 5. 总结

OV-Watch 项目**没有使用信号量**，而是采用了：
- **消息队列** 进行任务间通信
- **任务挂起/恢复** 进行任务同步
- **定时器** 处理周期性任务
- **中断** 处理外部事件

这种设计更适合智能手表的应用场景，通过消息队列实现了清晰的任务间通信机制。

### 消息队列发送者详解

#### DataSave_MessageQueue (数据保存消息)
- **发送者**: `SensorDataUpdateTask` (第159行)
- **触发时机**: 完成Home页面数据更新后
- **发送位置**: `user_SensUpdateTask.c` 第159行
- **消息内容**: `uint8_t Datastr = 3`
- **接收者**: `DataSaveTask` → 保存数据到EEPROM
- **作用**: 触发传感器数据的持久化存储

#### HomeUpdata_MessageQueue (Home页面更新消息)
- **发送者1**: `User_Tasks_Init` (第281行) - 系统启动时
- **发送者2**: `StopEnterTask` (第298行) - 从睡眠唤醒后
- **发送者3**: `LvHandlerTask` (第48行) - 检测到用户交互时
- **接收者**: `SensorDataUpdateTask` → 更新传感器数据
- **作用**: 触发Home页面数据刷新

#### Idle_MessageQueue (空闲息屏消息)
- **发送者**: `IdleTimerCallback` (第176行)
- **触发条件**: 空闲时间达到 `ui_LTimeValue` 秒
- **接收者**: `IdleEnterTask` → 降低屏幕亮度到5%
- **作用**: 实现息屏节能

#### Stop_MessageQueue (停止待机消息)
- **发送者1**: `IdleTimerCallback` (第184行) - 自动超时
- **发送者2**: `MPUCheckTask` (第66行) - 智能放腕检测
- **发送者3**: `KeyTask` (第40行) - 用户手动触发
- **接收者**: `StopEnterTask` → 进入深度睡眠
- **作用**: 触发系统进入低功耗待机模式

#### IdleBreak_MessageQueue (空闲打断消息)
- **发送者**: 多个任务在用户操作时发送
  - `KeyTask` (第35行) - 按键操作
  - `LvHandlerTask` (第48行) - 触摸操作
- **接收者**: `IdleEnterTask` → 恢复屏幕亮度并重置计时器
- **作用**: 打断空闲状态，恢复正常显示

#### Key_MessageQueue (按键消息)
- **发送者**: `KeyTask` (第35行和第45行)
- **触发条件**: 按键1或按键2按下
- **接收者**: `ScrRenewTask` → 处理页面切换
- **作用**: 处理用户按键输入

## 传感器数值更新机制

- **总体策略（按需+周期）**
  - `SensorDataUpdateTask`：每500ms轮询一次，根据消息与当前页面按需读取并写回 `HWInterface.*`。
  - `HRDataUpdateTask`：仅在 `ui_HRPage` 时，每50ms计算心率并更新。
  - 完成Home数据后发送 `DataSave_MessageQueue` 触发持久化。

- **触发时机**
  - 启动/唤醒：`StopEnterTask` 发送 `HomeUpdata_MessageQueue` 触发一次Home刷新。
  - 页面相关：
    - `ui_EnvPage` 连续读温湿度（AHT21）。
    - `ui_CompassPage` 读加速度/磁场（LSM303）与海拔（SPL06）。
    - `ui_HRPage` 心率启用（EM7028）。
  - Home页平时刷新：收到 `HomeUpdata_MessageQueue` 才读一次电量/步数/温湿度。

- **具体更新点（示例）**
  - 电量/步数：`HWInterface.Power.BatCalculate()`；`HWInterface.IMU.GetSteps()`。
  - 温湿度（AHT21）：`HWInterface.AHT21.GetHumiTemp(&humi,&temp)` → 校验后写 `HWInterface.AHT21.humidity/temperature`。
  - 指南针/海拔：`LSM303_ReadAcceleration/ReadMagnetic` → 方位角 → `HWInterface.Ecompass.direction`；`Altitude_Calculate()` → `HWInterface.Barometer.altitude`。
  - 心率（EM7028）：`HR_Calculate(EM7028_Get_HRS1(), user_HR_timecount)` 合法区间再写入 `HWInterface.HR_meter.HrRate`。

- **省电**
  - 非当前页面时休眠相关传感器（如 `LSM303DLH_Sleep`, `SPL_Sleep`, `EM7028_hrs_DisEnable`）。
  - IIC不做后台常驻轮询，全部由任务按需触发读取。

## 系统运行模式详解

### 运行模式分类
1. **正常运行模式** (Active Mode)
   - 系统全速运行，所有外设正常工作
   - 屏幕正常亮度显示，传感器数据采集，用户交互响应

2. **息屏模式** (Idle Mode)
   - 屏幕亮度降低到5%，系统继续运行
   - 触发条件：用户无操作达到 `ui_LTimeValue` 秒
   - 发送者：`IdleTimerCallback` → `Idle_MessageQueue` → `IdleEnterTask`

3. **待机模式** (Stop Mode)
   - 系统进入深度睡眠，大部分外设关闭
   - 触发条件：息屏后继续无操作达到 `ui_TTimeValue` 秒
   - 发送者：`IdleTimerCallback` → `Stop_MessageQueue` → `StopEnterTask`

### 消息队列发送者总结

#### Idle_MessageQueue (息屏消息)
- **发送者**: `IdleTimerCallback` (第176行)
- **触发条件**: 空闲时间达到 `ui_LTimeValue` 秒
- **接收者**: `IdleEnterTask` → 降低屏幕亮度到5%

#### Stop_MessageQueue (待机消息)
- **发送者1**: `IdleTimerCallback` (第184行) - 自动超时
- **发送者2**: `MPUCheckTask` (第66行) - 智能放腕检测
- **发送者3**: `KeyTask` (第40行) - 用户手动触发
- **接收者**: `StopEnterTask` → 进入深度睡眠

#### IdleBreak_MessageQueue (空闲打断消息)
- **发送者**: 多个任务在用户操作时发送
- **接收者**: `IdleEnterTask` → 恢复屏幕亮度并重置计时器

### IdleTimerCount 清零位置
1. **IdleEnterTask** (第51行) - 用户操作打断空闲
2. **StopEnterTask** (第75行) - 准备进入睡眠
3. **StopEnterTask** (第131行) - 检测到放腕动作
4. **StopEnterTask** (第144行) - 无有效唤醒条件
5. **ChargCheckTask** (第32行) - 充电状态变化
6. **IdleTimerCallback** (第182行) - 达到待机时间后重置

### 主页时钟更新机制
- **更新频率**: 500ms (通过 `ui_HomePageTimer`)
- **更新函数**: `HomePage_timer_cb` (在 `LvHandlerTask` 中执行)
- **数据来源**: `HWInterface.RealTimeClock.GetTimeDate()` 获取RTC时间
- **更新策略**: 只有时间值变化时才更新UI显示
- **显示元素**: 小时、分钟、日期、星期等

### RTC时间戳获取和保护
- **获取方式**: `HAL_RTC_GetTime()` + `HAL_RTC_GetDate()` (HAL库函数)
- **硬件保护**: LSE时钟源、备份域供电、RTC唤醒定时器
- **软件保护**: 原子操作、同步等待、错误处理、格式转换
- **系统保护**: 看门狗、低功耗模式保护

## 待机模式唤醒机制详解

### 唤醒条件
1. **按键唤醒**
   - KEY1按下 (`!KEY1`)
   - KEY2按下
   - 代码位置：`StopEnterTask` 第137行

2. **充电唤醒**
   - 充电插拔检测 (`HardInt_Charg_flag`)
   - 代码位置：`StopEnterTask` 第137行

3. **抬腕唤醒**
   - MPU6050检测到抬腕动作 (`Wrist_Flag`)
   - 代码位置：`StopEnterTask` 第118-127行
   - 条件：`HWInterface.IMU.wrist_is_enabled` 启用

4. **RTC定时器唤醒**
   - 每约1秒自动唤醒一次
   - 配置：`HAL_RTCEx_SetWakeUpTimer_IT(&hrtc, 2000, RTC_WAKEUPCLOCK_RTCCLK_DIV16)`
   - 计算：2000 / (32768/16) ≈ 0.98秒

### 唤醒处理流程
1. **系统恢复** (第105-113行)
   - 恢复系统时钟：`SET_BIT(SysTick->CTRL, SysTick_CTRL_TICKINT_Msk)`
   - 重新配置系统时钟：`SystemClock_Config()`
   - 喂狗：`WDOG_Feed()`
   - 恢复所有任务：`xTaskResumeAll()`

2. **外设恢复** (第147-158行)
   - UART恢复：`HAL_UART_MspInit(&huart1)`
   - LCD恢复：`LCD_Init()` + `LCD_Set_Light(ui_LightSliderValue)`
   - 触摸屏恢复：`CST816_Wakeup()`
   - 充电检测：`ChargeCheck()`
   - 发送Home更新消息：`osMessageQueuePut(HomeUpdata_MessageQueue, &HomeUpdataStr, 0, 1)`

3. **唤醒条件判断** (第137-146行)
   ```c
   if(!KEY1 || KEY2 || HardInt_Charg_flag || Wrist_Flag)
   {
       Wrist_Flag = 0;
       //resume, go on  // 有有效唤醒条件，继续运行
   }
   else
   {
       IdleTimerCount = 0;
       goto sleep;     // 无有效唤醒条件，重新进入睡眠
   }
   ```

### 功耗优化策略
- **定期唤醒**: 每1秒唤醒一次检查状态
- **快速判断**: 唤醒后立即检查唤醒条件
- **立即睡眠**: 无有效事件时立即重新进入睡眠
- **睡眠比例**: 99%+ 的时间在睡眠状态
- **唤醒时间**: 仅几毫秒，功耗极低

### 设计原理
- **平衡响应性和功耗**: 既保证用户操作及时响应，又最大化省电
- **智能检测**: 通过多种传感器检测用户意图
- **快速恢复**: 唤醒后快速恢复系统状态
- **标准模式**: 符合智能手表等低功耗设备的设计规范

