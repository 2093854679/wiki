---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_findmy/bk3633/zh_CN/v2.0.1/developer-guide/ota/index.html
sdk_family: bk_findmy
chip: BK3633
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="ota"></a>

# OTA

<a id="id1"></a>

## 1、OTA

> 目前 OTA 升级只能使用 Android 设备进行,且需要保证bin文件版本号大于板子固件中版本号;
> 版本号修改 projects/app\_findmy/Makefile 中的APP\_VERSION 和 STACK\_VERSION，升级固件时选择修改后的 bk3633\_findmy\_stack\_oad\_rbl.bin

备注

支持OTA升级需要使用8Mb的flash;

<a id="id2"></a>

## 2、 OTA升级流程

1.在Android设备上安装Beken\_RC\_OTA\_V3.1.apk应用程序，在代码中tools/ota目录下

2.将待更新的OTA firmware存放在android文件系统的任意目录下，推荐放在/Download文件夹下（程序默认搜索该目录下文件并显示在APP界面）

3.点击手机上RC\_OTA图标，打开APP，分别如一下两张图所示：

<a id="id3"></a>
[![ota_1](../../../_assets/374bf513cc6a3b12d286-ota_1.png)](../../../_assets/374bf513cc6a3b12d286-ota_1.png)


手机上显示RC\_OTA图标

<a id="id4"></a>
[![ota_2](../../../_assets/fdb8c69f7fae9137bbd0-ota_2.png)](../../../_assets/fdb8c69f7fae9137bbd0-ota_2.png)


APP主界面

4.选择下方的“scan”按钮开始扫描设备，扫描到的BLE设备会显示在列表中，如下：

<a id="id5"></a>
[![ota_3](../../../_assets/2111730352698356402d-ota_3.png)](../../../_assets/2111730352698356402d-ota_3.png)


扫描界面

5.点击对应的设备，进入设备详情页面，如下：

<a id="id6"></a>
[![ota_4](../../../_assets/3530cc6067ad72c102a7-ota_4.png)](../../../_assets/3530cc6067ad72c102a7-ota_4.png)


设备详情界面

6.点击“OTA”按钮，进入OTA界面，如果待升级固件存放在/Download目录下，能直接在界面上看到保存的固件，否则需要点击“Other Files”按钮,找到并选择对应固件：

<a id="id7"></a>
[![ota_5](../../../_assets/4d339a1a7f6b2c75aa4f-ota_5.png)](../../../_assets/4d339a1a7f6b2c75aa4f-ota_5.png)


设备详情界面

7.选择需要升级的bin文件，准备OTA升级，当bin文件版本号大于板子固件中版本号才能升级，

<a id="id8"></a>
[![ota_6](../../../_assets/997c9a2bb34d754c426d-ota_6.png)](../../../_assets/997c9a2bb34d754c426d-ota_6.png)


OTA文件选择界面

8.点击页面右下方的“Partical OTA”或“Full OTA”按钮，启动OTA流程，如下：

<a id="id9"></a>
[![ota_7](../../../_assets/a96b56523ffdc79e3e0d-ota_7.png)](../../../_assets/a96b56523ffdc79e3e0d-ota_7.png)


OTA升级过程

9.等待OTA升级成功后，设备会断开与手机的连接，并退回主界面
