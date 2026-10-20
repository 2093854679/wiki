---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/debug-guide/at_command_guide.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="at"></a>

# [AT命令开发指南](#id2)

<a id="id1"></a>

目录

- [AT命令开发指南](#at)

  - [Wi-Fi基础AT命令](#wi-fiat)
  - [PLATFORM](#platform)
  - [DATACTL](#datactl)
  - [TCP](#tcp)
  - [UDP](#udp)
  - [HTTP](#http)
  - [MQTT](#mqtt)
  - [AT DATA](#at-data)

<a id="wi-fiat"></a>

## [Wi-Fi基础AT命令](#id3)

这节主要分析的是Wi-Fi设备扫描、连接等基础AT命令。

<a id="at-wifiscan"></a>

### AT\+WIFISCAN

功能说明
:   用于扫描一次当前空口环境的路由器或热点，全信道扫描。

命令格式
:   `AT+WIFISCAN`

参数说明
:   无参数

测试用例
:   输入：`AT+WIFISCAN`

    如果输入这条命令，命令执行成功，则上报扫描结果，并返回：
    `CMDRSP:OK`

    否则返回：
    `CMDRSP:ERROR`

响应格式
:   `<SSID> <BSSID> < RSSI> <CHANNEL> < SECURITY >`

参数说明
:   - `<SSID>`：字符串参数，AP的SSID
    - `<BSSID>`：字符串参数，AP的MAC地址
    - `< RSSI>`：信号强度
    - `<CHAN>`：信道号
    - `< SECURITY >`：加密方式

测试实例
:   ```
    发送命令：【bk_ioctrl send_at AT+WIFISCAN】
    返回结果：最多支持48个结果输出
    scan found 48 APs
                SSID                     BSSID      RSSI  CHAN  SECURITY
    ------------------------------------------------    ----   ----  ---------
    Product_test                     10:5f:02:f8:5c:38    -37    6  WPA2-AES
    stability-router2                  d4:31:27:58:ac:d9    -43    6  WPA2-AES
    H3C_OTA                        34:ca:81:a9:c5:0f    -43    6  WPA2-AES
    ······
    EVT:WLAN STA SCAN_DONE
    CMDRSP:OK
    ```

<a id="at-wifiscan-ssid"></a>

### AT\+WIFISCAN\=SSID

功能说明
:   用于扫描指定SSID的路由器或者热点。

命令格式
:   `AT+WIFISCAN =ssid`

参数说明
:   支持1个参数

    - `ssid`：指定扫描的路由器或者热点名称

测试用例
:   输入：`AT+WIFISCAN=aclsemi`

    如果输入这条命令，命令执行成功，则上报扫描结果，并返回：
    `CMDRSP:OK`

    否则返回：
    `CMDRSP:ERROR`

测试实例
:   ```
    发送命令：【bk_ioctrl send_at AT+WIFISCAN=aclsemi】
    返回结果：
    scan found 3 APs
                  SSID             BSSID      RSSI  CHAN  SECURITY
    ----------------------------------------    ----   ----  ---------
    aclsemi                    58:c7:ac:7e:2d:f0    -42    11  WPA2-AES
    aclsemi                    58:c7:ac:7e:2a:30    -45    6  WPA2-AES
    aclsemi                    74:50:4e:3f:7e:d0    -53    1  WPA2-AES
    EVT:WLAN STA SCAN_DONE
    CMDRSP:OK
    ```

<a id="at-stastart-ssid-pwd"></a>

### AT\+STASTART\=SSID,PWD

功能说明
:   用于连接到指定的路由器或者热点。

命令格式
:   `AT+STASTART=ssid,<pwd>`

参数说明
:   支持2个参数

    - `ssid`：指定连接的路由器或者热点名称
    - `pwd`：指定连接的路由器或者热点的密码（连接不加密的，该参数可省略）

测试用例
:   1. 输入：`AT+STASTART=Atest,12345678`
    2. 输入：`AT+STASTART=Atest`

    如果输入这条命令，连接完成并获取IP则成功，则返回：
    `CMDRSP:OK`

    否则返回：
    `CMDRSP:ERROR`

测试实例
:   **1、连接成功的场景：**

    ```
    发送命令：【bk_ioctrl send_at AT+STASTART=Xiaomi】
    返回结果：
    EVT:WLAN STA CONNECTED
    CONNECTED SSID:Xiaomi
    STA CONNECT IND: connect to 'Xiaomi' (-35 dBm)
    ip: 192.168.31.43, mk: 255.255.255.0, gw: 192.168.31.1, dns: 192.168.31.1

    EVT:BK STA GOT IP
    sta got ip:192.168.31.43

    CMDRSP:OK
    ```

    **2、连接错误SSID的场景：**

    ```
    发送命令：【bk_ioctrl send_at AT+STASTART=Xiaomixxxxx】
    返回结果：
    EVT:WLAN STA DISCONNECTED
    EVT:DISCONNECT REASON:NO_AP_FOUND(REASON CODE:257)【连接失败的原因】
    local generated:yes
    CMDRSP:ERROR
    ```

参数说明
:   REASON CODE:错误码，仅供参考

    - 256：无法探知已连接的AP
    - 257：未找到连接AP
    - 258：密码错误
    - 259：应用断开连接
    - 260：获取IP地址超时；
    - 其他失败原因，参考wifi协议reason code

<a id="at-sapstart-ssid-pwd-chan"></a>

### AT\+SAPSTART\=SSID,PWD,CHAN

功能说明
:   用于开启Wi-Fi热点。

命令格式
:   `AT+SAPSTART =ssid,<pwd>,<chan>`

参数说明
:   支持3个参数

    - `ssid`：指定的热点名称(less than 32 Bytes)
    - `pwd`：指定的热点密码或信道号
      \- 密码：开启加密热点，该参数可缺省。请输入8\~64个字符以上的密码！！！，如果密码的字符长度小于8，会默认为不加密。
      \- 信道：当输入字符小于2个字符时，认定输入为信道号
    - `chan`：信道：想要启动热点的所属信道，可以缺省

测试用例
:   1. 输入：`AT+SAPSTART=Atest,12345678`
    2. 输入：`AT+SAPSTART=Atest,11`
    3. 输入：`AT+SAPSTART=Atest,12345678，11`
    4. 输入：`AT+SAPSTART=Atest`

    如果输入这条命令，配置成功，则返回：
    `CMDRSP:OK`

    否则返回：
    `CMDRSP:ERROR`

测试实例
:   ```
    发送命令：【bk_ioctrl send_at AT+SAPSTART=SSID,PWD123454】
    返回结果：
    CMDRSP:OK
    ```

<a id="at-stastop"></a>

### AT\+STASTOP

功能说明
:   用于关闭Wi-Fi STA模式。

命令格式
:   `AT+STASTOP`

参数说明
:   无参数

测试用例
:   输入：`AT+STASTOP`

    如果Wi-Fi STA功能关闭成功，则返回：
    `CMDRSP:OK`

    否则返回：
    `CMDRSP:ERROR`

测试实例
:   ```
    发送命令：【bk_ioctrl send_at AT+STASTOP】
    返回结果：
    STA DISCONNECT IND: disconnect
    CMDRSP:OK
    EVT:WLAN STA DISCONNECTED
    EVT:DISCONNECT REASON:DEAUTH_LEAVING(REASON CODE:3)
    ```

<a id="at-sapstop"></a>

### AT\+SAPSTOP

功能说明
:   用于关闭Wi-Fi SoftAP模式。

命令格式
:   `AT+SAPSTOP`

参数说明
:   无参数

测试用例
:   输入：`AT+SAPSTOP`

    如果Wi-Fi SoftAP功能关闭成功，则返回：
    `CMDRSP:OK`

    否则返回：
    `CMDRSP:ERROR`

测试实例
:   ```
    发送命令：【bk_ioctrl send_at AT+SAPSTOP】
    返回结果：
    CMDRSP:OK
    ```

<a id="at-wifistatus"></a>

### AT\+WIFISTATUS

功能说明
:   用于查看Wi-Fi设备当前的模式状态：SoftAP/STA模式，及当前模式下的IP地址等信息。

命令格式
:   `AT+WIFISTATUS`

参数说明
:   无参数

    如果获取状态成功，上报各个模式的状态信息，并返回：
    `CMDRSP:OK`

    否则返回：
    `CMDRSP:ERROR`

响应格式
:   `sta: <enable>, ap: <enable>, <sap capacity>`

参数说明
:   - `<enable>`：模式是否使能
      \- 1：使能
      \- 0：未使能
    - `<sap capacity>`：SoftAP支持的能力
      \- b：支持11b
      \- g：支持11g
      \- n：支持11n

测试实例
:   ```
    发送命令：【bk_ioctrl send_at AT+WIFISTATUS】
    返回结果：
    sta: 1, ap: 1, b/g/n
    EVT:sta:rssi=-46,aid=23,ssid=ax86u,bssid=50:eb:f6:34:13:e8,channel=10,cipher_type=WPA2-AES
    softap: ssid=SSID, channel=1, cipher_type=WPA2-AES
    EVT:ap_ip=192.168.176.1,ap_gate=192.168.176.1,ap_mask=255.255.255.0,ap_dns=0.0.0.0
    CMDRSP:OK
    ```

<a id="at-wifistatus-param1-param2"></a>

### AT\+WIFISTATUS\=PARAM1,PARAM2

功能说明
:   用于查询模组指定模式下指定的参数信息。

命令格式
:   `AT+ WIFISTATUS =param1, <param2>`

参数说明
:   支持2个参数

    - `param1`：选择STA/SoftAP模式。参数范围：STA/AP
    - `param2`：指定参数信息。该参数可缺省，缺省时只会查询参数1选择模式的启停状态。参数范围：RSSIBSSIDSSIDIPCHANNEL（SoftAP模式不支持RSSI和BSSID）

测试用例
:   1. 输入：`AT+ WIFISTATUS =STA`
    2. 输入：`AT+ WIFISTATUS =STA, RSSI`

    如果获取状态成功，上报查询结果，并返回：
    `CMDRSP:OK`

    否则返回：
    `CMDRSP:ERROR`

测试实例
:   **1、查看STA的IP：**

    ```
    发送命令：【bk_ioctrl send_at AT+WIFISTATUS=STA,IP】
    返回结果：
    CMDRSP:STA_IP=192.168.32.201,GATE=192.168.32.3,MASK=255.255.255.0,DNS=114.114.114.114
    CMDRSP:OK
    ```

    **2、查看STA的RSSI：**

    ```
    发送命令：【bk_ioctrl send_at AT+WIFISTATUS= STA,RSSI】
    返回结果：
    CMDRSP:sta_rssi:-47
    CMDRSP:OK
    ```

<a id="at-staping"></a>

### AT\+STAPING

功能说明
:   用于执行PING包操作。

命令格式
:   `AT+STAPING =ip,<pkn>,<size>`

参数说明
:   支持3个参数

    - `ip`：IP地址
    - `pkn`：PING包的数量，默认ping 4包
    - `size`：每个PING包的大小

测试用例
:   1. 输入：`AT+STAPING =192.168.30.1`
    2. 输入：`AT+STAPING =192.168.30.1,10`
    3. 输入：`AT+STAPING =192.168.30.1,10,100`

    如果指令发送成功，则返回：
    `CMDRSP:OK`

    并且开始上报每次PING包的结果，执行完成上报全部PING包统计结果

    否则返回：
    `CMDRSP:ERROR`

测试实例
:   ```
    发送命令：【bk_ioctrl send_at AT+STAPING=192.168.31.1】
    返回结果：
    CMDRSP:OK
    60 bytes from 192.168.31.1 icmp_seq=0 ttl=64 time=52 ticks
    60 bytes from 192.168.31.1 icmp_seq=1 ttl=64 time=6 ticks
    60 bytes from 192.168.31.1 icmp_seq=2 ttl=64 time=24 ticks
    60 bytes from 192.168.31.1 icmp_seq=3 ttl=64 time=178 ticks
    ping end, sent cnt: 4, recv cnt: 4, drop cnt: 0(0.0%)
    ```

<a id="at-stapingstop"></a>

### AT\+STAPINGSTOP

功能说明
:   用于执行停止PING包操作。

命令格式
:   `AT+STAPINGSTOP`

参数说明
:   无参数

测试用例
:   输入：`AT+STAPINGSTOP`

    如果指令发送并执行成功，上报之前已经PING包的统计结果，并返回：
    `CMDRSP:OK`

    否则返回：
    `CMDRSP:ERROR`

测试实例
:   ```
    发送命令：【bk_ioctrl send_at AT+STAPINGSTOP】
    返回结果：
    CMDRSP:OK
    60 bytes from 192.168.31.1 icmp_seq=3 ttl=64 time=26 ticks
    ping end, sent cnt: 4, recv cnt: 4, drop cnt: 0(0.0%)【返回已经发送完成的包的统计结果】
    ```

<a id="at-closecsa"></a>

### AT\+CLOSECSA

功能说明
:   用于执行关闭Wi-Fi多身份（SoftAP\+ STA）共存模式下SoftAP的CSA。

    注意：该命令并不是关闭SoftAP的CSA功能，只用于关闭STA\+ SoftAP时SoftAP会做CSA切换到与STA相同的信道上的功能。

命令格式
:   `AT+CLOSECSA=param1`

参数说明
:   支持1个参数

    - `param1`：是否关闭共存模式下的CSA，参数取值范围：0/1

测试用例
:   输入：`AT+CLOSECSA=1`

    如果设置成功，则返回：
    `CMDRSP:OK`

    否则返回：
    `CMDRSP:ERROR`

命令使用要求
:   该命令需要在起STA之前下发，否则会返回错误（因为该命令在起STA之后发送无法生效，因此加了错误返回提醒）。

测试实例
:   ```
    发送命令：【bk_ioctrl send_at AT+CLOSECSA=0】
    返回结果：
    CMDRSP:OK
    ```

<a id="platform"></a>

## [PLATFORM](#id4)

<a id="at-rst"></a>

### AT\+RST

功能说明
:   用于重置模组。

命令格式
:   `AT+RST`

<a id="at-version"></a>

### AT\+VERSION

功能说明
:   用于获取当前的版本信息。

命令格式
:   `AT+VERSION`

    如果查询成功，上报版本信息，并返回：
    `CMDRSP:OK`

    否则返回：
    `CMDRSP:ERROR`

参数说明
:   版本信息包含：

    - Version：固件版本编译时间；
    - chip id：芯片版本
    - soc：芯片型号

测试实例
:   ```
    发送命令：【bk_ioctrl send_at AT+VERSION】
    返回结果：
    EVT:version:Jun  9 2025 11:50:19
    EVT:chip id:72390101
    EVT:soc: bk7239
    CMDRSP:OK
    ```

<a id="at-wlmac"></a>

### AT\+WLMAC

功能说明
:   用于查询当前的mac地址。

命令格式
:   `AT+WLMAC`

参数说明
:   无参数

测试用例
:   输入：`AT+WLMAC`

    如果查询成功，上报MAC地址结果，并返回：
    `CMDRSP:OK`

    否则返回：
    `CMDRSP:ERROR`

测试实例
:   ```
    发送命令：【bk_ioctrl send_at AT+WLMAC】
    返回结果：
    base mac: 8c:87:d0:04:2d:6e
    sta mac: 8c:87:d0:04:2d:6e
    ap mac: 8c:87:d0:04:2d:6f
    CMDRSP:OK
    ```

<a id="at-wlmac-mac"></a>

### AT\+WLMAC\=MAC

功能说明
:   用于配置设备MAC地址。

命令格式
:   `AT+WLMAC =mac`

参数说明
:   支持1个参数

    - `mac`：MAC地址。例如配置MAC地址为：c8:93:ff:dd:ee:bb，该值写为：c893ffddeebb

测试用例
:   输入：`AT+WLMAC=c893ffddeebb`

    如果输入这条命令，配置成功，则返回：
    `CMDRSP:OK`

    否则返回：
    `CMDRSP:ERROR`

测试实例
:   ```
    发送命令：
       【bk_ioctrl send_at AT+WLMAC=8c87d0042d6e】
    返回结果：
       set base mac: 8c:87:d0:04:2d:6e
       CMDRSP:OK
    ```

<a id="datactl"></a>

## [DATACTL](#id5)

这节主要阐述DATACTL的AT命令，该命令用于控制数据通路，如果需要使用TCPUDPHTTPMQTT以及数传等AT命令，需要先使用该命令配置为1。每次上电，该命令配置一次即一直生效，如果不需要使用可以手动关闭，使用该命令配置为0。

<a id="at-datactl"></a>

### AT\+DATACTL

功能说明
:   控制是否使用mac的数据通路

命令格式
:   `AT+TCPSTART= ctrl`

参数说明
:   支持2个参数

    - `ctrl`：控制是否使用mac的数据通路

测试用例
:   输入：

    `AT+DATACTL=1`

    发送成功，并则返回：

    `CMDRSP:OK`

    否则返回：

    `CMDRSP:ERROR`

测试实例
:   ```
    发送命令：
       【bk_ioctrl send_at AT+DATACTL=1】
    返回结果：
       CMDRSP:OK
    ```

<a id="tcp"></a>

## [TCP](#id6)

这节主要阐述TCP相关的AT命令

<a id="at-tcpstart"></a>

### AT\+TCPSTART

功能说明
:   用于建立一个TCP客户端，并且与指定地址和端口号的TCP服务器进行连接。

命令格式
:   `AT+TCPSTART= port,ip`

参数说明
:   支持2个参数

    - `port`：想要连接的TCP服务器的端口号
    - `ip`：想要连接的TCP服务器的IP地址

测试用例
:   输入：

    `AT+TCPSTART=12138,192.168.0.2`

    如果建立TCP客户端并且连接服务器成功，上报连接信息，并则返回：

    `CMDRSP:OK`

    否则返回：

    `CMDRSP:ERROR`

AT回显事件
:   - `EVT:TCP CLIENT CONNECTED,LINK-ID: %d.`：TCP客户端已经连接至指定的TCP服务器
    - `EVT:TCP_CLIENT ID NUMS REACHES LIMITED NUM.`：TCP客户端建立数量已经超过最大允许数量，不再接收新的TCP客户端连接
    - `EVT:TCP CLIENT FD:%d, RECVED LENGTH:%d DATA,FROM FD:%d`：TCP客户端从所连接的TCP服务器上接收到数据

测试实例
:   ```
    发送命令：
       【bk_ioctrl send_at AT+TCPSTART=5150,192.168.31.165】

    返回结果：
       EVT:TCP CLIENT PORT:64256,SOCKET ID:0,CONNECTED TO SERVER
       SOCKET CREATE SUCCESS
       CMDRSP:OK
    ```

<a id="at-serverstart"></a>

### AT\+SERVERSTART

功能说明
:   用于建立一个指定端口号的TCP服务器并监听即将到来的连接。

命令格式
:   `AT+SERVERSTART=port`

参数说明
:   支持1个参数

    - `port`：想要建立服务器的端口号

测试用例
:   输入：

    `AT+SERVERSTART=12138`

    如果输入这条命令，创建TCP 服务端成功，上报创建信息，并返回：

    `CMDRSP:OK`

    否则返回：

    `CMDRSP:ERROR`

测试实例
:   ```
    发送命令：
       【bk_ioctrl send_at AT+SERVERSTART=5350】
    返回结果：
       CMDRSP:OK
       EVT:TCP SERVER INFO:PORT:5350,IP:192.168.32.201,LISTEN FD:0
    ```

<a id="at-tcpclose"></a>

### AT\+TCPCLOSE

功能说明
:   用于关闭指定的TCP服务器或客户端。

命令格式
:   `AT+TCPCLOSE=param1,param2`

参数说明
:   支持2个参数

    - `param1`：取值范围0/1。0表示服务器，1表示客户端
    - `param2`：需要删除的socket ID（即创建时返回的LISTEN FD）。

测试用例
:   输入：

    `AT+TCPCLOSE=0,0`

    如果关闭指定TCP成功，则返回：

    `CMDRSP:OK`

    否则返回：

    `CMDRSP:ERROR`

测试实例
:   ```
    发送命令：
    【bk_ioctrl send_at AT+TCPCLOSE=1,0】

    返回结果：

    CMDRSP:OK
    ```

<a id="udp"></a>

## [UDP](#id7)

这节主要阐述UDP相关的AT命令

<a id="at-udpstart"></a>

### AT\+UDPSTART

功能说明
:   用于建立一个UDP客户端，并且与指定地址和端口号的UDP服务器进行连接。

命令格式
:   `AT+UDPSTART= port`

参数说明
:   支持2个参数

    - `port`：想要连接的UDP服务器的端口号

测试用例
:   输入：

    `AT+UDPSTART=8080`

    如果输入这条命令，UDP配置成功，上报连接信息，并返回：

    `CMDRSP:OK`

    否则返回：

    `CMDRSP:ERROR`

测试实例：
:   ```
    发送命令：
       【bk_ioctrl send_at AT+UDPSTART=8084】

    返回结果：
       EVT:UDP CONNECTION SOCKET ID:0,PORT:8084,IP:192.168.32.201,ESTABLISHED.
       SOCKET CREATE SUCCESS
       CMDRSP:OK
    ```

<a id="at-udpclose"></a>

### AT\+UDPCLOSE

功能说明
:   用于关闭指定的UDP客户端。

命令格式
:   `AT+UDPCLOSE=self_fd`

参数说明
:   支持1个参数

    - `self_fd`：需要删除的socket ID（即创建时返回的LISTEN FD）。

测试用例
:   输入：
    `AT+UDPCLOSE=0`

    如果关闭指定UDP成功，则返回：

    `CMDRSP:OK`

    否则返回：

    `CMDRSP:ERROR`

测试实例：
:   ```
    发送命令：
       【bk_ioctrl send_at AT+UDPCLOSE=0】

    返回结果：
       CMDRSP:OK
    ```

<a id="http"></a>

## [HTTP](#id8)

这节主要阐述HTTP的AT命令，暂时不支持https。

<a id="at-httpstart"></a>

### AT\+HTTPSTART

功能说明
:   用于建立一个HTTP客户端，并可携带自定义的HTTP header并使用对应的GET/HEAD方法进行HTTP操作

命令格式
:   GET:

    `AT+HTTPSTART=method,content,data_total_len,uri_len,0,header_len`

    POST:

    `AT+HTTPSTART=method,content,data_total_len,uri_len,data_len,header_len`

参数说明
:   支持6个参数

    - `method`：HTTP方法，0:RESERVED，1:GET，2:POST
    - `content`：HTTP内容类型，0:RESERVED，1:application/x-www-form-urlencoded，2:application/json，3:multipart/form-data，4:text/xml
    - `data_total_len`：想要发送数据的总长度，为后面几个发送数据长度之和
    - `uri_len`：HTTP URI长度
    - `data_len`：想要POST的数据的长度(GET方法此长度设置为0)
    - `header_len`：HTTP header长度

测试用例
:   输入：

    `AT+HTTPSTART=1,0,20,20,0,0`

    `http://www.baidu.com`

HTTP 数据格式

格式示例:

```
|               |                       |                    |
|               |                       |                    |
—— ———URI—— —— —— —— DATA(POST)—— —— —— —— header —— ——
```

如果建立HTTP客户端并且连接服务器成功，上报连接信息，并则返回：

> `CMDRSP:OK`
>
> 否则返回：
>
> `CMDRSP:ERROR`

测试实例：
:   ```
    发送命令：
       【bk_ioctrl send_at AT+HTTPSTART=1,0,39,39,0,0】

    返回结果：
       EVT:READY TO RECV DATA

    发送命令：
       【bk_ioctrl send_at http://192.168.50.60/E%3A/otarbl/1.html】

    返回结果：
       webclient get response data bytes_read:4
       test       【 get 到的数据，每1024 byte的数据通过1条消息发送】
       EVT: GET SUCCESS
       CMDRSP:OK
    ```

    **注意：此命令只适合GET和POST长数据，如果仅仅是操作短数据，可以使用AT\+HTTPGET与AT\+HTTPPOST命令**

<a id="at-httphead"></a>

### AT\+HTTPHEAD

功能说明
:   用于发送HTTP HEAD请求。

命令格式
:   `AT+HTTPHEAD= url`

参数说明
:   支持1个参数

    - `url`：HTTP请求的URL地址

测试用例
:   输入：

    `AT+HTTPHEAD=http://ww.baidu.com`

    如果发送HTTP HEAD请求成功，上报响应信息，并则返回：

    `CMDRSP:OK`

    否则返回：

    `CMDRSP:ERROR`

测试实例：
:   ```
    发送命令：
       【bk_ioctrl send_at AT+HTTPHEAD=http://www.baidu.com】

    返回结果：
       HTTP/1.1 200 OK
       Accept-Ranges: bytes
       Cache-Control: private, no-cache, no-store, proxy-revalidate, no-transform
       Connection: keep-alive
       Content-Length: 277
       Content-Type: text/html
       Date: Tue, 10 Jun 2025 05:56:26 GMT
       Etag: "575e1f60-115"
       Last-Modified: Mon, 13 Jun 2016 02:50:08 GMT
       Pragma: no-cache
       Server: bfe/1.0.8.18
       CMDRSP:OK
    ```

<a id="at-httpget"></a>

### AT\+HTTPGET

功能说明
:   用于发送HTTP GET请求。

命令格式
:   `AT+ HTTPGET = content,data_total_len`

参数说明
:   支持2个参数

    - `content`：HTTP内容类型，0:RESERVED，1:application/x-www-form-urlencoded，2:application/json，3:multipart/form-data，4:text/xml
    - `data_total_len`：想要发送数据的总长度，为后面几个发送数据长度之和

测试用例：

> 输入：
>
> > `AT+HTTPGET=0,20`
> > `http://ww.baidu.com`
>
> 如果发送HTTP GET请求成功，上报响应信息，并返回：
>
> > `CMDRSP:OK`
>
> 否则返回：
>
> > `CMDRSP:ERROR`

测试实例：
:   ```
    发送命令：
       【bk_ioctrl send_at AT+HTTPGET=0,39】

    返回结果：
       EVT:READY TO RECV DATA

    发送命令：
       【bk_ioctrl send_at http://192.168.50.60/E%3A/otarbl/1.html】

    返回结果：
       AT_HTTP get position handle response status(200).
       EVT: GET SUCCESS, resp data len 4
       test      【 get 到的数据，每1024 byte的数据通过1条消息发送】
       CMDRSP:OK
    ```

<a id="at-httppost"></a>

### AT\+HTTPPOST

功能说明
:   用于发送HTTP POST请求，不使用自定义header。

命令格式
:   `AT+HTTPHEAD = content,data_total_len,uri_len,data_len`

参数说明
:   支持4个参数

    - `content`：HTTP内容类型，0:RESERVED，1:application/x-www-form-urlencoded，2:application/json，3:multipart/form-data，4:text/xml
    - `data_total_len`：想要发送数据的总长度，为后面几个发送数据长度之和
    - `uri_len`：HTTP URI长度
    - `data_len`：想要POST的数据的长度

测试用例：

> 输入：
>
> > `AT+HTTPPOST=2,53,37,16`
> > `http://www.rt-thread.com/service/echolove_from_Beken!`
>
> 如果发送HTTP POST请求成功，上报响应信息，并返回：
>
> > `CMDRSP:OK`
>
> 否则返回：
>
> > `CMDRSP:ERROR`

测试实例：
:   ```
    1、示例一

       发送命令：
          【bk_ioctrl send_at AT+HTTPPOST=2,48,39,9】

       返回结果：
          EVT:READY TO RECV DATA

       发送命令：
          【bk_ioctrl send_at http://192.168.50.60/E%3A/otarbl/1.html123456789】

       返回结果：
          AT_HTTP post response status (400)
          CMDRSP:ERROR

    2、示例二

       发送命令：
          【bk_ioctrl send_at AT+HTTPPOST=2,152,37,115】

       返回结果：
          EVT:READY TO RECV DATA

       发送数据：
          【bk_ioctrl send_at http://www.rt-thread.com/service/echodevices
          Code=120002000814&userKey=6b6d71e72c70d136179177ddd231af7d&devicesName=bk7256&random=ZWVUTR&token=2c70426994】

       返回结果：
          HTTP/1.1 200 OK
          Server: nginx/1.18.0 (Ubuntu)
          Date: Thu, 12 Jun 2025 06:54:51 GMT
          Content-Type: text/html
          Content-Length: 26
          Connection: keep-alive
          X-Powered-By: PHP/5.5.9-1ubuntu4.25
          AT_HTTP post response status (200)
          AT_HTTP post response data resp_len:26
          AT_HTTP post response data resp:::devicesCode=120002000814
          CMDRSP:OK
    ```

<a id="mqtt"></a>

## [MQTT](#id9)

这节主要阐述MQTT相关的AT命令

<a id="at-mqttclient"></a>

### AT\+MQTTCLIENT

功能说明
:   用于建立一个MQTT客户端

命令格式
:   `AT+MQTTCLIENT=host_name/ip,username,password<,topic>`

参数说明
:   支持3/4个参数

    - `host_name/ip`：想要连接的MQTT服务器的域名或IP地址
    - `username`：MQTT用户名
    - `password`：MQTT密码
    - `topic`：想要订阅的topic(可选)

测试用例
:   输入：

    `AT+MQTTCLIENT=222.71.10.2,aclsemi,******, /aclsemi/bk7256/cmd/1234`

    如果建立MQTT客户端并且连接服务器成功，上报连接信息，并则返回：

    `CMDRSP:OK`

    否则返回：

    `CMDRSP:ERROR`

测试实例：
:   ```
    发送命令：
       【bk_ioctrl send_at AT+MQTTCLIENT=222.71.10.2,aclsemi,***,/aclsemi/bk7256/cmd/changyun】

    返回结果：
       CMDRSP:OK
    ```

<a id="at-mqttsend"></a>

### AT\+MQTTSEND

功能说明
:   用于发送MQTT消息。

命令格式
:   `AT+MQTTSEND= topic,message`

参数说明
:   支持2个参数

    - `topic`：MQTT主题
    - `message`：MQTT消息内容

测试用例
:   输入:

    `AT+MQTTSEND = aclsemi/bk7256/cmd/1234, 12345678999999999`

    如果发送MQTT消息成功，上报发送信息，并则返回：

    `CMDRSP:OK`

    否则返回：

    `CMDRSP:ERROR`

测试实例：
:   ```
    发送命令：
       【bk_ioctrl send_at AT+MQTTSEND=/aclsemi/bk7256/cmd/changyun,123456】

    返回结果：
       CMDRSP:OK
    ```

<a id="at-data"></a>

## [AT DATA](#id10)

这节主要阐述数据发送和接收相关的AT命令

<a id="at-ipsend"></a>

### AT\+IPSEND

功能说明
:   用于通过TCP/UDP连接发送数据。

命令格式
:   TCP：
    :   `AT+IPSEND=selftype,self_fd,peer_fd,data_len`

    UDP
    :   `AT+IPSEND=selftype,self_fd,peer_port,peer_ip,data_len`

参数说明
:   支持4-5个参数

    - `selftype`：想要发送的身份类型，0:客户端，1：服务器
    - `self_fd`：想要发送的身份的FD值
    - `peer_fd`：想要发送的对端FD值(tcp only)，当对端为服务端时，值等于self\_fd。
    - `peer_port`：想要发送的对端端口号(udp only)
    - `peer_ip`：想要发送的对端IP地址(udp only)
    - `data_len`：想要发送的数据长度

测试用例

> TCP：
> :   `AT+IPSEND=1,0,1,8`
>
>     `Beken666`
>
> UDP：
> :   `AT+IPSEND=0,0,12138,192.168.0.3,8`
>
>     `Beken666`
>
> 如果发送数据成功，则返回：
>
> `CMDRSP:OK`
>
> 否则返回：
>
> `CMDRSP:ERROR`

测试实例：
:   ```
    1、发送成功

       发送命令：
          【bk_ioctrl send_at AT+IPSEND=0,0,0,4】

       返回结果：
          EVT:READY TO RECV DATA

       发送命令：
          【bk_ioctrl send_at 1234】

       【注意：使用串口测试命令中数据应为可打印字符，否则AP侧需要调用bk_ioctl_send_at_data发送数据】

       返回结果：
          EVT:lWIP_DATA_READY_SEND
          EVT:SERVER AT_SAL_DATA_SEND SUCCESS
          CMDRSP:OK

    2、发送超时：

       发送命令：
          【bk_ioctrl send_at AT+IPSEND=0,0,0,4】

       返回结果：
          EVT:READY TO RECV DATA
          EVT:AT_SAL_SEND_DATA_TIMEOUT
          CMDRSP:ERROR
    ```

<a id="at-datarecv"></a>

### AT\+DATARECV

功能说明
:   用于从模组获取指定长度的接收数据至用户端。当接收到MAC层上报接收到消息的EVENT的时候，发送该命令可以从MAC获取到接收的数据。数据在MAC层保存一段时间，如果长时间不接收，MAC层会主动删除数据，目前时间为5s。。

命令格式
:   - TCP：
      :   `AT+IPDATARECV=type,self_fd,peer_fd,data_index,size`
    - UDP：
      :   `AT+IPDATARECV=type,self_fd,peer_port,ip,data_index,size`

参数说明
:   支持5/6个参数

    - `type`：想要接收的身份类型, 1:客户端，0：服务器，UDP默认为客户端
    - `self_fd`：想要接收的身份的FD值
    - `peer_fd`：想要接收的对端FD值(tcp only)
    - `peer_port`：想要接收的对端端口号(udp only)
    - `peer_ip`：想要接收的对端IP地址(udp only)
    - `data_index`：想要接收的数据序号
    - `size`：想要接收的数据大小

测试用例

> 输入：
>
> TCP：
> :   `AT+IPDATARECV=0,0,1,0,9`
>
> UDP：
> :   `AT+IPDATARECV=1,0,12138,192.168.0.3,0,9`
>
> 如果接收数据成功，上报接收到的数据，并则返回：
> :   `CMDRSP:OK`
>
> 否则返回：
> :   `CMDRSP:ERROR`

测试实例：
:   ```
    1、正常接收：

       上报结果：
          EVT:TCP CLIENT FD:0, RECVED LENGTH:4 DATA,FROM FD:0

       发送命令：
          【bk_ioctrl send_at AT+IPDATARECV=1,0,0,0,4】

       返回结果：
          1234                【接收到的数据】
          CMDRSP:OK

    2、接收处理超时：

       上报结果：
          EVT:TCP CLIENT FD:0, RECVED LENGTH:4 DATA,FROM FD:0
          EVT:recv packet 0 save too long,discard
    ```
