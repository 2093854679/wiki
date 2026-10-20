---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/host-guide/host_adapt.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 主控平台适配指南

本章节主要介绍BK7239N主控平台适配指南，按照本章节文档修改主控平台代码后，即可完成BK7239N主控平台适配。

BK7239N主控侧代码以源码形式发布，可将相关代码放入主控平台代码中参与编译，主要分为两部分：
\- 内核修改
\- 用户空间API接口

<a id="linux"></a>

## **Linux内核修改**

Linux内核主要增加BK7239N驱动，详细介绍如下。

备注

BK7239N驱动源码以源码方式提供，相关文件路径 `/bk_idk_controller/host/driver/linux/beken_vnet`

<a id="bk7239n"></a>

### BK7239N驱动

beken\_vnet驱动是BK7239N驱动的核心代码，首先将代码放在内核 `/kernel/drivers/net/wireless/beken_vnet` 目录下，
然后修改 `/kernel/drivers/net/wireless` 目录下的makefile和Kconfig将代码编译进内核，具体修改如下图所示：

![Kconfig](../../../_assets/ce61f0d9261c60a000d7-beken_vent_kconfig.png)
![makefile](../../../_assets/5a280f9b8b6138b4a2c0-beken_vent_makefile.png)

<a id="api"></a>

## **用户空间API接口**

用户空间主要包含bk\_ioctl API接口和demo APP，相关代码路径： `/bk_idk_controller/host/demo_app/bk_ioctrl`

<a id="bk-ioctl-api"></a>

### bk\_ioctl API接口

为了方便应用开放，在Linux系统用户空间提供了API接口，这部分代码路径： `/bk_idk_controller/host/demo_app/bk_ioctrl/bk_ioctl_api.h`
SDK提供的基础API接口如下：

```
 1 /**************************WLAN API**************************/
 2 int bk_ioctl_scan_wifi(void);
 3 int bk_ioctl_set_sta(char *ssid, char *key);
 4 int bk_ioctl_disc_sta(void);
 5 int bk_ioctl_start_softap(char *ssid, char *pw);
 6 int bk_ioctl_stop_softap(void);
 7 int bk_ioctl_get_wlan_status(bk_ioctl_wlan_status_t *status);
 8 int bk_ioctl_wifi_multimedia_config(bool wifi_mmd_en);
 9 int bk_ioctl_set_net_info(struct bk_ioctl_net_info *info);
10 int bk_ioctl_get_net_info(bk_ioctl_net_info_t *net_info);
11 int bk_ioctl_get_rssi(int32_t *rssi);
12 int bk_ioctl_get_wifi_info(bk_wifi_info *info);
13 int bk_ioctl_set_auto_reconnect(bool auto_connect_en);
14
15 /**************************BLE API**************************/
16 int bk_ioctl_open_ble(void);
17 int bk_ioctl_close_ble(void);
18
19 /**************************SYSTEM API**************************/
20 int bk_ioctl_set_mac(uint8_t *mac);
21 int bk_ioctl_get_mac(uint8_t *mac, int len);
22 int bk_ioctl_enter_sleep(void);
23 int bk_ioctl_exit_sleep(void);
24 int bk_ioctl_send_at(char *at_str);
25 int bk_ioctl_keepalive_cfg(struct bk_ioctl_keepalive_cfg *cfg);
26 int bk_ioctl_set_time(uint32_t time);
27 int bk_ioctl_get_time(uint32_t *time);
28 int bk_ioctl_send_customer_data(uint8_t *data, uint16_t len, uint8_t *rsp_data, uint16_t rsp_len);
29 int bk_ioctl_start_ota(void);
30 int bk_ioctl_send_ota_pkt(bk_ioctl_ota_req_t *ota_info, uint16_t len);
31 int bk_ioctl_stop_ota(void);
32
33 /**************************Other API**************************/
34 void bk_ioctl_register_callback(bk_ioctl_callback_t callback);
35 int bk_ioctl_init(void);
36 void bk_ioctl_deinit(void);
```

备注

API接口具体含义请参考 `/bk_idk_controller/host/demo_app/bk_ioctrl/bk_ioctl_api.h`

<a id="demo-app"></a>

### demo APP

bk\_ioctrl目录提供了与beken\_vnet驱动对应的上层demo应用程序，分别是bk\_ioctrl和bk\_rx\_evt
用户可通过bk\_ioctrl中相关命令实现对BK7239N的操作，如Wi-Fi的扫描和连接等，
通过 `bk_ioctl_register_callback` 完成接收消息注册，实现接收Controller主动上报的消息

bk\_ioctrl支持命令和bk\_rx\_evt支持的消息可参考 [主控Demo APP介绍](host_demo.md)
