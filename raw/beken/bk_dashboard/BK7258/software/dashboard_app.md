---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_dashboard/bk7258/zh_CN/v3.1.1/software/dashboard_app/index.html
sdk_family: bk_dashboard
chip: BK7258
processor: ''
sdk_version: v3.1.1
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
[![downlaod_qr_code](../../../_assets/e07f5044d20d43659ae0-download_qr_code.png)](../../../_assets/e07f5044d20d43659ae0-download_qr_code.png)


下载二维码

<a id="id2"></a>

## 2 简介

通过此app,让开发板播放导航语音，显示导航图片。根据图传方式的不同，分为蓝牙图传和wifi图传。

<a id="id3"></a>

## 3\. 开发板介绍

以如下开发板举例。

- reset 按键：复位开发板
- K1 按键：清除配网信息并复位开发板

<a id="id17"></a>
![board](../../../_assets/76e09e92306e9a67b96a-board.png)


示例开发板

<a id="wifi"></a>

## 4\. WIFI图传使用步骤

通过wifi传输图片,通过经典蓝牙传输语音。

<a id="id4"></a>

### 4.1 重置开发板

点击K1按键，重置开发板。

<a id="id5"></a>

### 4.2 配置

根据需要选择配置。

<a id="id18"></a>
[![setting](../../../_assets/bf38d546a5f54af1e179-setting.png)](../../../_assets/bf38d546a5f54af1e179-setting.png)


设置

<a id="id6"></a>

### 4.3 配网

使用BLE进行配网。

<a id="id19"></a>
[![wifi_working_page](../../../_assets/4088969dccd2cb903d66-wifi_working_page.png)](../../../_assets/4088969dccd2cb903d66-wifi_working_page.png)


wifi界面功能介绍

<a id="id20"></a>
[![wifi_tip](../../../_assets/fe4a4a46e7e2b9a1468a-wifi_tips.png)](../../../_assets/fe4a4a46e7e2b9a1468a-wifi_tips.png)


配网提示

<a id="id21"></a>
[![ble_scan](../../../_assets/5bf18dcce31310ec31dd-ble_scan.png)](../../../_assets/5bf18dcce31310ec31dd-ble_scan.png)


蓝牙扫描结果

<a id="id22"></a>
[![wifi_select_type](../../../_assets/92e6b80ff078b0ee9c16-wifi_select_type.png)](../../../_assets/92e6b80ff078b0ee9c16-wifi_select_type.png)


选择配网类型

<a id="id23"></a>
[![wifi_input_pwd](../../../_assets/6f384aa866ab251b256d-wifi_input_pwd.png)](../../../_assets/6f384aa866ab251b256d-wifi_input_pwd.png)


输入配网信息

<a id="id24"></a>
[![wifi_dn_done](../../../_assets/c81d932ccd0044347acc-wifi_dn_done.png)](../../../_assets/c81d932ccd0044347acc-wifi_dn_done.png)


配网成功

<a id="id7"></a>

### 4.4 语音配置

导航语音通过经典蓝牙进行传输。

<a id="id25"></a>
[![bt_pair](../../../_assets/1c9b31ee588f41bc931f-bt_pair.png)](../../../_assets/1c9b31ee588f41bc931f-bt_pair.png)


蓝牙配对

<a id="id8"></a>

### 4.5 发现设备

点击搜索，选择类型，开始搜索设备。

<a id="id26"></a>
[![wifi_select_type_discovery](../../../_assets/616989392fa9094ca787-wifi_select_type_discovery.png)](../../../_assets/616989392fa9094ca787-wifi_select_type_discovery.png)


发现设备

<a id="id27"></a>
[![wifi_discover_success](../../../_assets/b332abfdee164add3ef0-wifi_discover_success.png)](../../../_assets/b332abfdee164add3ef0-wifi_discover_success.png)


发现设备成功

<a id="id9"></a>

### 4.6 导航与图传

点击导航功能按钮，开始导航。导航开始后，可以点击投屏按钮，开始投屏。

<a id="id10"></a>

## 5\. 蓝牙图传使用步骤

通过BLE传输图片,通过经典蓝牙传输语音。

<a id="id11"></a>

### 5.1 重置开发板

点击K1按键，重置开发板。

<a id="id12"></a>

### 5.2 设置

根据需要选择配置。

<a id="id28"></a>
[![setting](../../../_assets/bf38d546a5f54af1e179-setting.png)](../../../_assets/bf38d546a5f54af1e179-setting.png)


设置

<a id="id13"></a>

### 5.3 选择图传设备

<a id="id29"></a>
[![ble_working_page](../../../_assets/9ad1e0b278de071894c1-ble_working_page.png)](../../../_assets/9ad1e0b278de071894c1-ble_working_page.png)


蓝牙图传界面功能介绍

<a id="id30"></a>
[![ble_tips](../../../_assets/736f8a75a8603fa37956-ble_tips.png)](../../../_assets/736f8a75a8603fa37956-ble_tips.png)


蓝牙提示

<a id="id31"></a>
[![ble_tips](../../../_assets/db0263cb703eb059ba99-ble_scan_ble.jpg)](../../../_assets/db0263cb703eb059ba99-ble_scan_ble.jpg)


蓝牙扫描结果

<a id="id14"></a>

### 5.4 语音配置

导航语音通过经典蓝牙进行传输。

<a id="id32"></a>
[![bt_pair](../../../_assets/1c9b31ee588f41bc931f-bt_pair.png)](../../../_assets/1c9b31ee588f41bc931f-bt_pair.png)


蓝牙配对

<a id="id15"></a>

### 5.5 导航与图传

点击导航功能按钮，开始导航。导航开始后，可以点击投屏按钮，开始投屏。
