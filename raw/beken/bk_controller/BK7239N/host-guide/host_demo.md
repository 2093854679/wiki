---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/host-guide/host_demo.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="demo-app"></a>

# 主控Demo APP介绍

<a id="id1"></a>

## **demo APP介绍**

BK Controller SDK在主控侧提供了两个demo APP，分别是bk\_ioctrl和bk\_rx\_evt。

<a id="bk-ioctrl"></a>

### bk\_ioctrl

在客户应用导入前，可以通过bk\_ioctrl APP进行对Controller进行控制，目前支持两种方式进行Controller的控制，支持的命令目前如下:

> ```
> bk_ioctrl <arg1> <arg2> <arg3> <arg4>
> -----------------------WLAN COMMAND---------------------------------
> bk_ioctrl scan_wifi                                 - scan AP
> bk_ioctrl connect [ssid] [password]                 - connect with AP
> bk_ioctrl disconnect                                - disconnect with ap
> bk_ioctrl start_ap [ssid] [password]                - start SoftAP
> bk_ioctrl stop_ap                                   - stop softAP
> bk_ioctrl get_wlan_stat                             - get wlan status
> bk_ioctrl wifi_mmd [enable]                         - config Wi-Fi multimedia mode
> bk_ioctrl set_netinfo [ip] [mask] [gw] [dns]        - config net info
> bk_ioctrl set_ar [ar_en]                            - config auto reconnect
> -----------------------BLE COMMAND----------------------------------
> bk_ioctrl open_ble                                  - open ble
> bk_ioctrl close ble                                 - close ble
> -----------------------SYSTEM COMMAND-------------------------------
> bk_ioctrl set_mac [mac]                             - set mac addr(set_mac 112233aabbcc)
> bk_ioctrl get_mac                                   - get mac addr
> bk_ioctrl enter_sleep                               - ask controller goto sleep
> bk_ioctrl exit_sleep                                - ask controller exit sleep
> bk_ioctrl send_at [AT string]                       - send AT command
> bk_ioctrl keepalive_cfg [ip] [port]                 - start keepalive demo
> bk_ioctrl set_time [time]                           - set time
> bk_ioctrl get_time                                  - get time
> bk_ioctrl cust [data string]                        - start customer demo
> bk_ioctrl start_ota                                 - notify controller to START OTA
> bk_ioctrl send_ota_pkt [offset] [size] [finish]     - send demo OTA packet
> bk_ioctrl stop_ota                                  - notify controller to STOP OTA
> -----------------------Customer COMMAND---------------------------------
> bk_ioctrl cust                                      - help infomation
> bk_ioctrl cust version                              - print controller version information
> bk_ioctrl cust reboot                               - reboot wifi controller
> bk_ioctrl cust poweroff                             - power off the wifi controller
> bk_ioctrl cust powerup_reason                       - get power up reason
> bk_ioctrl cust reboot_reason                        - get reboot reason
> bk_ioctrl cust start_ka                             - start keep alive with server demo
> bk_ioctrl cust set_param [key] [value]              - set parameter
> bk_ioctrl cust get_param                            - get parameter
> bk_ioctrl cust control [para]                       - start keep avlive with host(eg. cust control alive/stop)
> bk_ioctrl cust battery                              - get wifi controller battery voltage
> ```

备注

bk\_ioctrl命令可能更新，请以实际代码为准

<a id="bk-rx-evt"></a>

### bk\_rx\_evt

bk\_rx\_evt APP可以通过bk\_ioctl\_register\_callback完成接收消息注册，实现接收Controller主动上报的消息。目前支持的消息如下所示：

```
 1 /* event-table from controller to host app */
 2 enum BK_EVENT_TYPE
 3 {
 4     // Wi-Fi连接成功通知
 5     BK_EVT_CONNECT_IND          = 0x1,
 6     // Wi-Fi断链通知
 7     BK_EVT_DISCONNECT_IND       = 0x2,
 8     // SoftAP启动通知
 9     BK_EVT_START_AP_IND         = 0x3,
10     // 其他Wi-Fi设备连接SoftAP通知
11     BK_EVT_ASSOC_AP_IND         = 0x4,
12     // 其他Wi-Fi设备断开SoftAP通知
13     BK_EVT_DISASSOC_AP_IND      = 0x5,
14     // SoftAP关闭通知
15     BK_EVT_STOP_AP_IND          = 0x6,
16     // Wi-Fi扫描结果通知
17     BK_EVT_SCAN_WIFI_IND        = 0x7,
18     // Wi-Fi连接失败通知
19     BK_EVT_WIFI_FAIL_IND        = 0x8,
20
21     // BLE event
22     // BK_EVT_BLE_XX            = 0x101
23
24     // system event
25     BK_EVT_CONTROLLER_AT_IND    = 0x201,
26     BK_EVT_CUSTOMER_IND         = 0x202,
27
28     BK_EVT_BUTT                 = BK_MAX_MSG_CNT - 1
29 };
```

<a id="demo"></a>

## **demo程序演示**

在参考 [主控平台适配指南](host_adapt.md) 完成主控平台适配后并编译生成BK7239N驱动ko文件后，即可配合demo APP进行demo展示。
首先加载beken\_vnet驱动，然后在后台运行bk\_rx\_evt用来接收Event事件，随后就通过bk\_ioctrl命令进行功能验证。
如下是通过demo程序进行连接Wi-Fi和ping网关的演示

> ```
> [root@Zeratul:~]# insmod /tmp/mnt/sdcard/beken_netdrv.ko
> [root@Zeratul:~]#
> [root@Zeratul:~]# bk_rx_evt &
> [root@Zeratul:~]# bk_ioctrl scan_wifi
> if:wlan0 is UP!
> [root@Zeratul:~]# RX event id:7 len:2080
> MCU-SCAN-WIFI:
>             SSID                     BSSID         RSSI CHAN SECURITY
> -------------------------------- -----------------   ---- ---- ---------
>
> Product_test                     10:5f:02:f8:5c:38    -21    6 WPA2-AES
>                                  12:5f:02:58:5c:38    -21    6 WPA2-AES
> Redmi_ETH                        5c:02:14:b3:02:86    -38    6 WPA2-AES
> Redmi_253C                       24:cf:24:3a:25:3e    -40    9 WPA2-AES
> mlhuawei                         82:75:9f:c9:59:c0    -42    1 WPA2-AES
> avdk                             68:dd:b7:03:f2:b3    -44    4 WPA2-AES
> aclsemi                          58:c7:ac:7e:2d:f0    -45   11 WPA2-AES
> NNN                              44:df:65:d9:c6:92    -47    4 WPA2-AES
> cyg                              0c:d8:6c:3a:3e:50    -49    1 WPA2-AES
>                                  d6:31:27:58:ac:d9    -50    1 WPA2-AES
> XiaoMi_123                       d4:da:21:57:7e:aa    -51    9 WPA3-SAE
> stability-router2                d4:31:27:58:ac:d9    -51    1 WPA2-AES
> stability-router1                04:42:1a:7d:bb:e0    -52    2 WPA3-SAE
> aclsemi                          58:c7:ac:7e:32:a0    -52    1 WPA2-AES
> bk_mesh_w1                       c8:47:8c:07:74:e0    -53    1 WPA2-AES
> Xiaomi_A29E                      3c:cd:57:50:a2:9f    -55    1 WPA2-MIX
> ruijie                           c0:a4:76:2c:72:fc    -57   10 WPA3-SAE
> ChinaNet-AbO3                    ba:a1:4a:65:54:b5    -57   11 WPA2-MIX
> stability-router3                a0:36:bc:9a:9c:48    -57    1 WPA3-SAE
> test_duan                        cc:28:aa:ad:11:e8    -57    6 WPA2-AES
> softAP_C8:47:8C:01:39:74         ca:47:8c:01:39:74    -57   11 WPA2-AES
> NETGEAR55                        74:d0:2b:6d:6b:cc    -57    3 WPA3-SAE
>                                  f6:6d:2f:a8:bd:35    -59    5 WPA2-AES
> bk_mesh_w1                       c8:47:8c:9d:a6:62    -60    1 WPA2-AES
> TP                               74:05:a5:d5:b9:58    -61    5 WPA2-AES
> bk_mesh_w1                       c8:47:8c:74:fd:3f    -64    1 WPA2-AES
> softAP_2025-03-10-19_58_53       c8:47:8c:d7:b0:d9    -64    1 WPA2-AES
> biubiubiu                        04:42:1a:d4:d6:90    -65   11 WPA2-AES
> ax56u-IT-verify                  3c:37:86:c3:bb:de    -68   10 WPA2-AES
> aclsemi                          74:50:4e:3f:7e:d0    -68    6 WPA2-AES
> JIEWU                            12:71:11:71:0b:71    -61    6 WEP
> OpenWrt                          d4:da:21:76:0d:d9    -26    6 NONE
> Redmi_ExTest                     d4:da:21:0e:7a:ef    -44   11 NONE
> ASUS_20                          d4:5d:64:ce:cc:20    -44    1 NONE
> ASUS_F8                          50:eb:f6:ab:1b:f8    -45    5 NONE
> tuituitui                        5c:02:14:7b:b1:b7    -46    4 NONE
> LTE                              60:c5:a8:e0:c3:bc    -48    2 NONE
>                                  da:da:21:57:7e:aa    -48    9 NONE
> HUAWEI_B535_2417                 62:c7:ca:17:24:28    -57    6 NONE
> Xiaomi_44D1                      8c:53:c3:dc:0b:23    -57   11 NONE
>
> [root@Zeratul:~]#
> [root@Zeratul:~]#
> [root@Zeratul:~]# bk_ioctrl connect OpenWrt
> bk_ioctl_set_sta_cmd ret:0
> [root@Zeratul:~]# RX event id:1 len:56
> STA CONNECT IND: connect to 'OpenWrt' (-27 dBm)
> ip: 192.168.1.172, mk: 255.255.255.0, gw: 192.168.1.1, dns: 192.168.1.1
> lo      Link encap:Local Loopback
>         inet addr:127.0.0.1  Mask:255.0.0.0
>         UP LOOPBACK RUNNING  MTU:65536  Metric:1
>         RX packets:0 errors:0 dropped:0 overruns:0 frame:0
>         TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
>         collisions:0 txqueuelen:0
>         RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
>
> wlan0   Link encap:Ethernet  HWaddr 8C:87:D0:04:2D:6E
>         inet addr:192.168.1.172  Bcast:192.168.1.255  Mask:255.255.255.0
>         UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
>         RX packets:0 errors:0 dropped:0 overruns:0 frame:0
>         TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
>         collisions:0 txqueuelen:1000
>         RX bytes:0 (0.0 B)  TX bytes:0 (0.0 B)
>
> Kernel IP routing table
> Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
> 0.0.0.0         192.168.1.1     0.0.0.0         UG    0      0        0 wlan0
> 192.168.1.0     0.0.0.0         255.255.255.0   U     0      0        0 wlan0
>
> [root@Zeratul:~]# ping 192.168.1.1
> PING 192.168.1.1 (192.168.1.1): 56 data bytes
> 64 bytes from 192.168.1.1: seq=0 ttl=64 time=39.365 ms
> 64 bytes from 192.168.1.1: seq=1 ttl=64 time=18.441 ms
> 64 bytes from 192.168.1.1: seq=2 ttl=64 time=11.139 ms
> 64 bytes from 192.168.1.1: seq=3 ttl=64 time=3.062 ms
> 64 bytes from 192.168.1.1: seq=4 ttl=64 time=3.544 ms
>
> --- 192.168.1.1 ping statistics ---
> 5 packets transmitted, 5 packets received, 0% packet loss
> round-trip min/avg/max = 3.062/15.110/39.365 ms
> ```
