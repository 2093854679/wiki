---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/controller-guide/api-reference/netif/index.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 网络接口

网络接口API提供网络配置和状态管理接口。

<a id="header-file"></a>

## Header File

- [netif.h](https://github.com/bekencorp/armino/blob/main/components/netif.h)

<a id="functions"></a>

## Functions

<a id="_CPPv413bk_netif_initv"></a>

<a id="_CPPv313bk_netif_initv"></a> <a id="_CPPv213bk_netif_initv"></a> <a id="bk_netif_init__void"></a> <a id="group__bk__api__netif_1ga720871c7f8c43476bf38f991333fa194"></a> [bk\_err\_t](system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_netif\_init(void)
:   Initialize the TCP/IP stack.

    **Attention**
    :   This API should be called exactly once from application code, when the application starts up.

    返回
    :   - BK\_OK: success
        - BK\_FAIL: otherwise

<a id="_CPPv423bk_netif_set_ip4_config10netif_if_tPK18netif_ip4_config_t"></a>

<a id="_CPPv323bk_netif_set_ip4_config10netif_if_tPK18netif_ip4_config_t"></a> <a id="_CPPv223bk_netif_set_ip4_config10netif_if_tPK18netif_ip4_config_t"></a> <a id="bk_netif_set_ip4_config__netif_if_t.netif_ip4_config_tCP"></a> <a id="group__bk__api__netif_1gadd74802f5d3fc434591918381e307cf6"></a> [bk\_err\_t](system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_netif\_set\_ip4\_config(netif\_if\_t ifx, const netif\_ip4\_config\_t \*config)
:   Set netif interface’s IP4 address information.

    This function is mainly used to set a static IP on an interface.

    **Attention**
    :   1\. For STA, if this API never calls, it gets the IP address via DHCP by default.

    **Attention**
    :   2\. If the interface is already up, we need to stop the interface first before calling this API, or restart the interface after the this API is called.

    **Attention**
    :   3\. Currently no sanity checking for the IP4 address to be configured, also no checking about the relationship between ip/mask/gateway/dns, the API caller need to guarantee that the correctness of the configured info.

    **Attention**
    :   4\. Avoid configuring same subnet for STA and AP.

    参数
    :   - **ifx** – The interface index
        - **config** – the IP4 information of the interface

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NETIF\_IF: invalid netif interface ID
        - BK\_ERR\_NULL\_PARAM: config is NULL

<a id="_CPPv423bk_netif_get_ip4_config10netif_if_tP18netif_ip4_config_t"></a>

<a id="_CPPv323bk_netif_get_ip4_config10netif_if_tP18netif_ip4_config_t"></a> <a id="_CPPv223bk_netif_get_ip4_config10netif_if_tP18netif_ip4_config_t"></a> <a id="bk_netif_get_ip4_config__netif_if_t.netif_ip4_config_tP"></a> <a id="group__bk__api__netif_1ga634a0e17fa52056d78f5f5c83af69173"></a> [bk\_err\_t](system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_netif\_get\_ip4\_config(netif\_if\_t ifx, netif\_ip4\_config\_t \*config)
:   Get netif interface’s IP address information.

    If the interface is up, IP information is read directly from the TCP/IP stack. If the interface is down, the API just return all 0 information

    参数
    :   - **ifx** – netif interface ID
        - **config** – store the IP4 configuration info

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NETIF\_IF: invalid netif interface ID
        - BK\_ERR\_NULL\_PARAM: config is NULL

<a id="_CPPv426bk_netif_get_ip6_addr_info10netif_if_t"></a>

<a id="_CPPv326bk_netif_get_ip6_addr_info10netif_if_t"></a> <a id="_CPPv226bk_netif_get_ip6_addr_info10netif_if_t"></a> <a id="bk_netif_get_ip6_addr_info__netif_if_t"></a> <a id="group__bk__api__netif_1ga8c7db2d41ccae10db35a5b31f90baf44"></a> [bk\_err\_t](system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_netif\_get\_ip6\_addr\_info(netif\_if\_t ifx)
:   Get netif interface’s IP6 address information.

    If the interface is up, IP6 information is read directly from the TCP/IP stack. If the interface is down, the API just return all 0 information

    参数
    :   **ifx** – netif interface ID

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NETIF\_IF: invalid netif interface ID
        - BK\_ERR\_NULL\_PARAM: config is NULL

<a id="_CPPv420bk_netif_dhcpc_start10netif_if_t"></a>

<a id="_CPPv320bk_netif_dhcpc_start10netif_if_t"></a> <a id="_CPPv220bk_netif_dhcpc_start10netif_if_t"></a> <a id="bk_netif_dhcpc_start__netif_if_t"></a> <a id="group__bk__api__netif_1ga91b4e04aa1b04f721f9d88f03b7fe451"></a> [bk\_err\_t](system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_netif\_dhcpc\_start(netif\_if\_t ifx)
:   Start the DHCP client for specified interface.

    If this API is called, the interface will get the IP address via DHCP.

    If the interface is has a static IP and is already up, we need to stop the interface (for STA, call [bk\_wifi\_sta\_stop()](wifi.md#group__bk__api__wifi__v2_1ga6f40eb9305ae390f7d777d652197894b) or [bk\_wifi\_sta\_disconnect()](wifi.md#group__bk__api__wifi__v2_1gae00bc75a589a66a378037c5adb05bc11) to stop the interface) before this API is called, or restart the interface after this API is called.

    参数
    :   **ifx** – netif interface ID, currently only support NETIF\_IF\_STA.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NETIF\_IF: invalid netif interface ID

<a id="_CPPv418bk_netif_static_ip18netif_ip4_config_t"></a>

<a id="_CPPv318bk_netif_static_ip18netif_ip4_config_t"></a> <a id="_CPPv218bk_netif_static_ip18netif_ip4_config_t"></a> <a id="bk_netif_static_ip__netif_ip4_config_t"></a> <a id="group__bk__api__netif_1ga9fd50f873579d4d8a9f85e6af28225dc"></a> [bk\_err\_t](system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_netif\_static\_ip(netif\_ip4\_config\_t static\_ip4\_config)
:   this function is only for the interface of NETIF\_IF\_STA to set a static IP .

    call back this function in netif\_wifi\_event\_cb()(in components/bk\_netif/bk\_netif.c) when case EVENT\_WIFI\_STA\_CONNECTED, and pass the param static\_ip4\_config includes ip, mask, gateway and dns for your static IP config. example: switch (event\_id) { case EVENT\_WIFI\_STA\_CONNECTED: #if CONFIG\_LWIP bk\_netif\_static\_ip(static\_ip4\_config); sta\_ip\_start(); #endif

    参数
    :   **static\_ip4\_config** – ipv4 config for this netif(only for NETIF\_IF\_STA).

    返回
    :   - BK\_OK: succeed
        - else: fail
