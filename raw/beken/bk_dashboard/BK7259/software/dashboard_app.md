---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_dashboard/bk7259/zh_CN/v4.0.1/software/dashboard_app/index.html
sdk_family: bk_dashboard
chip: BK7259
processor: ''
sdk_version: v4.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="dashboard-app"></a>

# Dashboard App 使用指南

<a id="id1"></a>

## 1 下载

扫描二维码，下载安装。

<a id="id16"></a>
[![android_download_qr_code](../../../_assets/a724cb29b2a04e82171e-download_qr_code_v2.png)](../../../_assets/a724cb29b2a04e82171e-download_qr_code_v2.png)


Android App

<a id="id17"></a>
[![ios_download_qr_code](../../../_assets/17ba50c5f97ee4a98651-download_qr_code_ios.png)](../../../_assets/17ba50c5f97ee4a98651-download_qr_code_ios.png)


iOS App

<a id="id2"></a>

## 2 简介

通过此app,让开发板播放导航语音，显示导航图片。根据图传方式的不同，分为蓝牙图传和wifi图传。

<a id="id3"></a>

## 3\. 开发板介绍

以如下开发板举例。

- reset 按键：复位开发板
- 长按下键: 清除配网信息并复位开发板

<a id="id18"></a>
[![board](../../../_assets/253a4bb4c299dc72d5d1-dashboard_v1.jpg)](../../../_assets/253a4bb4c299dc72d5d1-dashboard_v1.jpg)


示例开发板

<a id="wifi"></a>

## 4\. WIFI图传使用步骤

通过wifi传输图片,通过经典蓝牙传输语音。

<a id="id4"></a>

### 4.1 重置开发板

长按下键，重置开发板。

<a id="id5"></a>

### 4.2 配置

根据需要选择配置，注意宽度和高度需要配成与开发板屏幕尺寸一致。

<a id="id19"></a>
[![config_center](../../../_assets/bc6ee1065ba28161f2f4-config_center_0701.jpg)](../../../_assets/bc6ee1065ba28161f2f4-config_center_0701.jpg)


配置中心

<a id="id6"></a>

### 4.3 配网

使用BLE进行配网。

<a id="id20"></a>
[![dashboard_home](../../../_assets/a0bbdc3b0f9284588e3a-dashboard_home_0701.jpg)](../../../_assets/a0bbdc3b0f9284588e3a-dashboard_home_0701.jpg)


首页与当前配置

<a id="id21"></a>
[![bluetooth_devices](../../../_assets/8d7d71a6b7891116f51c-bluetooth_devices_0701.jpg)](../../../_assets/8d7d71a6b7891116f51c-bluetooth_devices_0701.jpg)


蓝牙设备扫描结果

<a id="id22"></a>
[![provision_type](../../../_assets/cf9e32a7feb0433dcf32-provision_type_0701.jpg)](../../../_assets/cf9e32a7feb0433dcf32-provision_type_0701.jpg)


选择配网方式

<a id="id23"></a>
[![wifi_config](../../../_assets/64408c8f666d8d4dfa9d-wifi_config_0701.jpg)](../../../_assets/64408c8f666d8d4dfa9d-wifi_config_0701.jpg)


输入 Wi-Fi 配置信息

<a id="id24"></a>
[![provision_progress](../../../_assets/0d0e4ac14478accdbc54-provision_progress_0701.jpg)](../../../_assets/0d0e4ac14478accdbc54-provision_progress_0701.jpg)


配网进度提示

<a id="id7"></a>

### 4.4 语音配置

导航语音通过经典蓝牙进行传输。

<a id="id25"></a>
[![bt_pair](../../../_assets/27a557bcd5e9339549d3-bt_pair.png)](../../../_assets/27a557bcd5e9339549d3-bt_pair.png)


蓝牙配对

<a id="id8"></a>

### 4.5 发现设备

点击搜索，选择类型，开始搜索设备。

<a id="id26"></a>
[![wifi_devices](../../../_assets/a4b79cc27fdcec4ad5d2-wifi_devices_0701.jpg)](../../../_assets/a4b79cc27fdcec4ad5d2-wifi_devices_0701.jpg)


Wi-Fi 设备列表

<a id="id9"></a>

### 4.6 导航与图传

点击导航功能按钮，开始导航。导航开始后，可以点击投屏按钮，开始投屏。

<a id="id27"></a>
[![casting_running](../../../_assets/408acfd9a6696723fa82-casting_running_0701.jpg)](../../../_assets/408acfd9a6696723fa82-casting_running_0701.jpg)


投屏进行中

<a id="id10"></a>

## 5\. 蓝牙图传使用步骤

通过BLE传输图片,通过经典蓝牙传输语音。

<a id="id11"></a>

### 5.1 重置开发板

长按下键，重置开发板。

<a id="id12"></a>

### 5.2 设置

根据需要选择配置。

<a id="id28"></a>
[![ble_config_center](../../../_assets/d420cd0ad6b5e079d757-ble_config_center_0701.jpg)](../../../_assets/d420cd0ad6b5e079d757-ble_config_center_0701.jpg)


BLE 图传配置

<a id="id13"></a>

### 5.3 选择图传设备

<a id="id29"></a>
[![ble_dashboard_home](../../../_assets/4e92af44309dd9e5ae09-ble_dashboard_home_0701.jpg)](../../../_assets/4e92af44309dd9e5ae09-ble_dashboard_home_0701.jpg)


BLE 图传首页与当前配置

<a id="id30"></a>
[![ble_devices](../../../_assets/0da92a3f9a8923e93d00-ble_devices_0701.jpg)](../../../_assets/0da92a3f9a8923e93d00-ble_devices_0701.jpg)


蓝牙设备列表

<a id="id14"></a>

### 5.4 语音配置

导航语音通过经典蓝牙进行传输。

<a id="id31"></a>
[![bt_pair](../../../_assets/27a557bcd5e9339549d3-bt_pair.png)](../../../_assets/27a557bcd5e9339549d3-bt_pair.png)


蓝牙配对

<a id="id15"></a>

### 5.5 导航与图传

点击导航功能按钮，开始导航。导航开始后，可以点击投屏按钮，开始投屏。

<a id="id32"></a>
[![ble_casting_running](../../../_assets/9da0cec3f1034ee04a46-ble_casting_running_0701.jpg)](../../../_assets/9da0cec3f1034ee04a46-ble_casting_running_0701.jpg)


BLE 投屏进行中
