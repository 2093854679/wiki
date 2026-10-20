---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_ai_smp/bk7258/zh_CN/v3.1.1/projects/volc_rtc/index.html
sdk_family: bk_ai_smp
chip: BK7258
processor: ''
sdk_version: v3.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="rtc-demo"></a>

# 火山引擎 RTC 解决方案DEMO开发指南

<a id="id1"></a>

## 1 项目概述

本项目是一个基于BK7258芯片和火山引擎RTC SDK的实时音视频通信解决方案，实现了通过WiFi传输音视频数据，支持与云端AI Agent进行实时对话的功能。项目集成了火山引擎RTC SDK、音频处理引擎、网络传输模块和事件管理系统，适用于智能AI设备、语音助手等应用场景的开发。

<a id="id2"></a>

## 2 功能特性

<a id="id3"></a>

### 2.1 实时音视频通信

- 支持双向音视频通信
- 支持多路音视频流
- 支持自适应码率控制（BWE）
- 支持关键帧请求机制

<a id="id4"></a>

### 2.2 音频处理

- 支持多种音频编码格式：
  \- G.722
  \- OPUS（推荐）
  \- PCM
- 支持AEC（回声消除）
- 支持NS（噪声抑制）
- 支持音频采集和播放

<a id="id5"></a>

### 2.3 视频处理（可选）

- 支持H264编码
- 支持JPEG编码
- 支持视频采集和传输

<a id="id6"></a>

### 2.4 网络功能

- 支持WiFi STA模式连接
- 支持WiFi AP模式热点
- 支持TCP/UDP协议
- 支持HTTP/HTTPS请求

<a id="ai-agent"></a>

### 2.5 AI Agent集成

- 支持与火山引擎AI Agent服务集成
- 支持语音对话和图像识别
- 支持Agent启动、停止和更新
- 支持从BK服务器或自定义服务器启动Agent

<a id="id7"></a>

### 2.6 房间管理

- 支持加入/离开RTC房间
- 支持用户上线/下线通知
- 支持Token权限管理
- 支持Token过期警告和自动刷新

<a id="id8"></a>

## 3 快速开始

<a id="id9"></a>

### 3.1 编译和烧录

编译流程参考 [AI 解决方案](https://docs.bekencorp.com/arminodoc/bk_ai_smp/bk7258/zh_CN/v3.1.1/README_CN.md)

烧录流程参考 具体 [烧录流程](../../../bk_avdk_smp/BK7258/get-started.md) 请参考 [SMP](../../../bk_avdk_smp/BK7258/index.md)

编译生成的烧录bin文件路径：`projects/volc_rtc/build/bk7258/volc_rtc/package/all-app.bin`

**编译命令示例：**

```
cd ~/armino/bk_solution_ai/projects/volc_rtc
export SDK_DIR=~/armino/bk_avdk_smp
make clean
make bk7258
```

<a id="api"></a>

## 4 API参考

本章节提供项目中核心功能的API接口说明，这些接口通过封装火山引擎RTC SDK实现了高级功能调用。

备注

建议开发者不要直接调用以下接口实现自定义方案，而是参考这些接口的实现方式，通过组合封装SDK接口来构建符合自身需求的功能模块。

<a id="agentapi"></a>

### 4.1 Agent管理API

<a id="bk-byte-agent-start"></a>

#### 4.1.1 bk\_byte\_agent\_start

```
/**
 * @brief 启动AI Agent服务
 *
 * @param room_info 房间信息结构体指针（输出参数）
 *        - 函数会填充App ID、Room ID、Token等信息
 *
 * @param device_id 设备ID字符串
 *
 * @return int 操作结果
 *         - BK_OK: 启动成功
 *         - BK_FAIL: 启动失败
 *
 * @note 此函数会：
 *       1. 根据配置选择从BK服务器或自定义服务器启动
 *       2. 发送HTTP请求到服务器
 *       3. 解析响应获取房间信息
 *       4. 填充room_info结构体
 *
 * @warning 调用此函数前应确保网络连接正常
 *
 * @see bk_byte_agent_stop()
 */
int bk_byte_agent_start(byte_rtc_room_info_t *room_info, void *device_id);
```

<a id="bk-byte-agent-stop"></a>

#### 4.1.2 bk\_byte\_agent\_stop

```
/**
 * @brief 停止AI Agent服务
 *
 * @param room_info 房间信息结构体指针
 * @param device_id 设备ID字符串
 *
 * @return int 操作结果
 *         - BK_OK: 停止成功
 *         - BK_FAIL: 停止失败
 *
 * @note 此函数会：
 *       1. 根据配置选择从BK服务器或自定义服务器停止
 *       2. 发送HTTP请求到服务器
 *       3. 清理本地资源
 *
 * @see bk_byte_agent_start()
 */
int bk_byte_agent_stop(byte_rtc_room_info_t *room_info, void *device_id);
```

<a id="id11"></a>

### 4.2 高级API

<a id="bk-byte-start"></a>

#### 4.2.1 bk\_byte\_start

```
/**
 * @brief 启动完整的RTC和Agent服务
 *
 * @param device_id 设备ID字符串
 *
 * @return int 操作结果
 *         - BK_OK: 启动成功
 *         - BK_FAIL: 启动失败
 *
 * @note 此函数会：
 *       1. 挂载SD卡文件系统（如果启用License）
 *       2. 启动AI Agent服务（获取房间信息）
 *       3. 初始化RTC引擎
 *       4. 加入RTC房间
 *       5. 开始音视频传输
 *
 * @warning 这是一个高级接口，会同时启动Agent和RTC
 *
 * @see bk_byte_stop()
 */
int bk_byte_start(void *device_id);
```

<a id="bk-byte-stop"></a>

#### 4.2.2 bk\_byte\_stop

```
/**
 * @brief 停止完整的RTC和Agent服务
 *
 * @param device_id 设备ID字符串
 *
 * @return int 操作结果
 *         - BK_OK: 停止成功
 *         - BK_FAIL: 停止失败
 *
 * @note 此函数会：
 *       1. 停止RTC服务（离开房间、销毁引擎）
 *       2. 停止AI Agent服务
 *       3. 释放房间信息内存
 *       4. 卸载SD卡文件系统
 *
 * @see bk_byte_start()
 */
int bk_byte_stop(void *device_id);
```

<a id="id12"></a>

### 4.3 音视频发送API

<a id="byte-rtc-send-audio"></a>

#### 4.3.1 byte\_rtc\_send\_audio

```
/**
 * @brief 发送音频数据到RTC房间
 *
 * @param engine RTC引擎句柄
 * @param room 房间ID字符串
 * @param data 音频数据指针
 * @param data_len 音频数据长度
 *
 * @return int 操作结果
 *         - 0: 发送成功
 *         - <0: 发送失败
 *
 * @note 此函数会：
 *       1. 检查RTC引擎和房间状态
 *       2. 调用SDK接口发送音频数据
 *       3. 自动处理编码格式转换
 *
 * @warning 调用此函数前应确保已加入房间
 *
 * @see byte_rtc_send_video()
 */
int byte_rtc_send_audio(byte_rtc_engine_t engine,
                        const char *room,
                        const void *data,
                        size_t data_len);
```

<a id="byte-rtc-send-video"></a>

#### 4.3.2 byte\_rtc\_send\_video

```
/**
 * @brief 发送视频数据到RTC房间
 *
 * @param engine RTC引擎句柄
 * @param room 房间ID字符串
 * @param data 视频数据指针
 * @param data_len 视频数据长度
 * @param codec 视频编码格式
 *
 * @return int 操作结果
 *         - 0: 发送成功
 *         - <0: 发送失败
 *
 * @note 此函数会：
 *       1. 检查RTC引擎和房间状态
 *       2. 构造视频帧信息
 *       3. 调用SDK接口发送视频数据
 *
 * @warning 调用此函数前应确保已加入房间
 *
 * @see byte_rtc_send_audio()
 */
int byte_rtc_send_video(byte_rtc_engine_t engine,
                        const char *room,
                        const void *data,
                        size_t data_len,
                        video_data_type_e codec);
```

<a id="id13"></a>

## 5 关于工程详细介绍以及指南请跳转如下链接

- [Armino SMP SDK 文档](../../../bk_avdk_smp/BK7258/index.md)
- [火山引擎 RTC 文档](https://www.volcengine.com/docs/6348)

- [<a id="id15"></a>
  \`\`](#id14)火山DEMO工程具体详情请参考文档链接：\<[https://docs.bekencorp.com/arminodoc/bk\_ai\_smp/bk7258/zh\_CN/v3.1.1/projects/volc\_rtc/index.html](volc_rtc.md)\>\`\`\_
