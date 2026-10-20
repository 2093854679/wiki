---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_app/app/zh_CN/v2.0.1/android_sdk/android_sdk_guide/index.html
sdk_family: bk_toolkit
chip: ''
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="sdk"></a>

# SDK概述

BKSmartSDK
提供了与远端摄像头设备通讯的接口封装，加速应用开发过程，后面章节统一称为
SDK 。主要包括了以下功能：

- 对设备进行配网
- 获取摄像头实时采集的影像。
- 获取摄像头传来的音频与摄像头设备通话。
- 音频的录制与播放。

**AVDK版本对应:**

| 芯片名称 | 产品类型 | AVDK版本 |
| --- | --- | --- |
| BK7258 | 智能门铃、门锁 | 2.0.1.9\+ |

<a id="id1"></a>

# 开发指南

<a id="id2"></a>

## 快速集成

本文介绍如何将SDK快速集成到您的项目中，需要安卓 5.0 以及以上版本。

<a id="id3"></a>

### 下载SDK

访问
[Gitlab仓库](https://gitlab.bekencorp.com/armino/app/sdk/smart_sdk/-/tree/release/v2.0.1)
下载SDK即可。

备注

从官网的gitlab下载的为最近的SDK代码，相关账号找项目上审核申请。

<a id="id4"></a>

### 集成

将下载的aar包，放入项目的libs文件夹下，并通过gradle的方式进行引入。

示例：

```
implementation(files("libs/iotsdk-v2.0.1.aar"))
```

<a id="id5"></a>

## 设备配网

<a id="id6"></a>

### 系统要求

蓝牙使用需要安卓 5.0 以及以上版本

<a id="manifest"></a>

### **Manifest权限**

```
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.BLUETOOTH" />
<uses-permission android:name="android.permission.BLUETOOTH_ADMIN" />
```

<a id="id7"></a>

### **蓝牙权限检测**

每次扫描和连接前，都要进行检测，否则 App 无法使用后续功能。

- App 在使用蓝牙连接或者扫描操作前，需要检查 App 定位权限是否被允许。
- 检查蓝牙状态是否为开启
- 位置服务是否打开

<a id="id8"></a>

### 功能说明

**相关类（协议）说明**

| **类名（协议名）** | **说明** |
| --- | --- |
| BkSmartBleScanOptions | ble扫描配置类 |
| BkSmartBleActivateOptions | ble配网配置类 |
| BKSmartBleActivator | ble扫描和配网的代理 |

<a id="id9"></a>

### 扫描流程

<a id="id10"></a>

#### **接口说明**

配置扫描选项

```
fun setActivateOptions(options: BkSmartBleActivateOptions)
```

开始扫描

```
fun startScan(context: Context)
```

结束扫描

```
fun stopScan(context: Context)
```

<a id="id11"></a>

#### **代理回调**

扫描结果

```
fun onScanResult(device: BluetoothDevice, rssi: Int)
```

扫描出错

```
fun onError(code: Int)
```

<a id="id12"></a>

### **配网**

<a id="id13"></a>

<a id="id14"></a>

#### **接口说明**

设置配网选项

```
fun setActivateOptions(options: BkSmartBleActivateOptions)
```

开始配网

```
fun activate(context: Context)
```

结束配网

```
fun stopActivate(context: Context)
```

<a id="id15"></a>

<a id="id16"></a>

#### **代理回调**

配网信息回调

```
fun onProgressMsg(msg: String)
```

配网结束

```
fun onResult(code: Int)
```

<a id="id17"></a>

## **摄像头功能**

SDK
提供智能摄像头的实时视频图像获取，摄像头音频数据获取，与摄像头实时通话等基础能力。

<a id="id18"></a>

<a id="id19"></a>

### 系统要求

蓝牙使用需要安卓 5.0 以及以上版本

<a id="manifest-1"></a>

<a id="id20"></a>

### **Manifest权限**

```
<uses-permission android:name="android.permission.RECORD_AUDIO" />
<uses-permission android:name="android.permission.INTERNET" />
```

<a id="id21"></a>

### **相关类（协议）说明**

| **类名（协议名）** | **说明** |
| --- | --- |
| BKSmartCameraDelegate | 操作camera的类 |
| BkSmartCameraConnectOptions | camera连接的配置类 |
| BkSmartCameraVideoOptions | camera video的配置类 |
| BkSmartCameraLcdOptions | camera lcd的配置类 |
| BkSmartCameraAudioOptions | camera audio的配置类 |

<a id="p2p"></a>

### P2P连接

在开始播放视频之前，需要先连接尚云 p2p 通道。p2p
的连接状态需要开发者自己维护，SDK 只负责下发命令和接收摄像机响应结果。

<a id="id22"></a>

<a id="id23"></a>

#### **接口说明**

配置连接选项

```
fun setConnectOptions(bkSmartCameraConnectOptions: BkSmartCameraConnectOptions)
```

开始连接p2p通道

```
fun connect()
```

断开p2p通道

```
fun disconnect()
```

<a id="id24"></a>

<a id="id25"></a>

#### **代理回调**

p2p通道连接成功

```
fun onConnected()
```

p2p通道断开连接

```
fun onDisconnected()
```

<a id="id26"></a>

### 实时视频

p2p连接成功以后，就可以开始获取实时视频图像数据了。

<a id="id27"></a>

<a id="id28"></a>

#### **接口说明**

配置视频选项

```
fun setVideoOptions(bkSmartCameraVideoOptions: BkSmartCameraVideoOptions)
```

开启视频播放

```
fun openVideoPreview()
```

关闭视频播放

```
fun closeVideoPreview()
```

降噪开关

```
fun enableNoiseReduction(enable: Boolean)
```

<a id="id29"></a>

<a id="id30"></a>

#### **代理回调**

videopreview开关回调

```
fun onVideoPreviewState(videoPreviewOn: Boolean)
```

解包后的可用数据

```
fun onReceiveFrameUnpackedData(frameData: ByteArray)
```

解包以后的坏数据

```
fun onReceiveFrameUnpackedBadData(frameData: ByteArray)
```

解包以后的数据帧，可直接显示

```
fun onReceiveFrame(bitmap: Bitmap, noiseReduction: Boolean)
```

<a id="id31"></a>

### 音频

p2p连接成功以后，就可以开始获取音频数据了。

<a id="id32"></a>

<a id="id33"></a>

#### **接口说明**

配置音频选项

```
fun setAudioOptions(bkSmartCameraAudioOptions: BkSmartCameraAudioOptions)
```

开启音频（板子发送给手机端的音频）

```
fun openAudio()
```

关闭音频（板子发送给手机端的音频）

```
fun closeAudio()
```

开启对讲(会同时打开板子发给手机端的音频)

```
fun openIntercom()
```

关闭对讲

```
fun closeIntercom()
```

<a id="id34"></a>

<a id="id35"></a>

#### **代理回调**

player和recorder的状态回调

```
fun onState(playerOn: Boolean, recorderOn: Boolean)
```

audio channel的操作状态回调

```
fun onChannelState(operating: Boolean)
```

错误回调

```
fun onError(code: Int)
```

上传的原始录音数据

```
fun onAudioUpOriginalStream(pcmData: ByteArray)
```

上传的编码后的数据

```
fun onAudioUpEncodedStream(encodedData: ByteArray, format: Int)
```

接收到板子的编码数据

```
fun onAudioDownUnpackedStream(unpackedData: ByteArray, format: Int)
```

接收到板子数据，然后手机端进行解码的数据

```
fun onAudioDownDecodedStream(pcmData: ByteArray)
```

<a id="lcd"></a>

### LCD控制

p2p连接成功以后，就可以控制LCD了。

<a id="id36"></a>

<a id="id37"></a>

#### 接口说明

获取LCD状态

```
fun fetchLcdState()
```

打开LCD

```
fun openLcd()
```

关闭LCD

```
fun closeLcd()
```

<a id="id38"></a>

<a id="id39"></a>

#### **代理回调**

lcd状态回调

```
fun onLcdState(on: Boolean)
```

错误回调

```
fun onError(code: Int)
```

<a id="code"></a>

## Code

| **名称** | 值 | **说明** |
| --- | --- | --- |
| SUCCESS | 0 | 成功 |
| BLE\_NOT\_AVAILABLE | 100 | 蓝牙 状态不可用（不支持或未开启蓝牙授权等 |
| BLE\_DEVICE\_NOT\_FOUND | 101 | 连接时，设备查找失败 |
| BLE \_DEVICE\_CONNECT\_FAILED | 102 | 设备连接失败 |
| B LE\_DEVICE\_DISCONNECTED | 103 | 与设备断开连接 |
| BLE\_ACTIVATE\_FAILED | 104 | 配网失败 |
| BLE\_ACTIVATE\_TIME\_OUT | 105 | 配网超时 |
| BLE\_SCAN\_TIME\_OUT | 106 | 扫描超时 |
| P2P\_LICENSE\_INVALID | 200 | key无效 |
| P2P\_CONNECT\_FAILED | 201 | 连接失败 |
| P2P\_DISCONNECTED | 202 | 断连 |
| P2P\_CONNECT\_SUCCESS | 203 | 连接成功 |
| OPEN\_VIDEO\_FAILED | 300 | 打开video失败 |
| CLOSE\_VIDEO\_FAILED | 301 | 关闭video失败 |
| OPEN\_AUDIO\_FAILED | 400 | 打开audio失败 |
| CLOSE\_AUDIO\_FAILED | 401 | 关闭video失败 |
| OPEN\_LCD\_FAILED | 500 | 打开lcd失败 |
| CLOSE\_LCD\_FAILED | 501 | 关闭lcd失败 |
