# BK NETIF[](#bk-netif "永久链接至标题")

[[English]](../../../../en/v2.2.1/api-reference/tcpip/bk_netif.html "../../../../en/v2.2.1/api-reference/tcpip/bk_netif.html")


## Netif API Reference[](#netif-api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [netif.h](https://github.com/bekencorp/armino/blob/main/components/netif.h "https://github.com/bekencorp/armino/blob/main/components/netif.h")


### Functions[](#functions "永久链接至标题")

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_netif_init(void)[](#_CPPv413bk_netif_initv "永久链接至目标")
:   Initialize the TCP/IP stack.


    **Attention**
    :   This API should be called exactly once from application code, when the application starts up.

    返回
    :   - BK_OK: success

        - BK_FAIL: otherwise

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_netif_set_ip4_config([netif_if_t](#_CPPv410netif_if_t "netif_if_t") ifx, const [netif_ip4_config_t](#_CPPv418netif_ip4_config_t "netif_ip4_config_t") *config)[](#_CPPv423bk_netif_set_ip4_config10netif_if_tPK18netif_ip4_config_t "永久链接至目标")
:   Set netif interface’s IP4 address information.

    This function is mainly used to set a static IP on an interface.


    **Attention**
    :   1. For STA, if this API never calls, it gets the IP address via DHCP by default.


    **Attention**
    :   2. If the interface is already up, we need to stop the interface first before calling this API, or restart the interface after the this API is called.


    **Attention**
    :   3. Currently no sanity checking for the IP4 address to be configured, also no checking about the relationship between ip/mask/gateway/dns, the API caller need to guarantee that the correctness of the configured info.


    **Attention**
    :   4. Avoid configuring same subnet for STA and AP.

    参数
    :   - **ifx** – The interface index

        - **config** – the IP4 information of the interface

    返回
    :   - BK_OK: succeed

        - BK_ERR_NETIF_IF: invalid netif interface ID

        - BK_ERR_NULL_PARAM: config is NULL

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_netif_get_ip4_config([netif_if_t](#_CPPv410netif_if_t "netif_if_t") ifx, [netif_ip4_config_t](#_CPPv418netif_ip4_config_t "netif_ip4_config_t") *config)[](#_CPPv423bk_netif_get_ip4_config10netif_if_tP18netif_ip4_config_t "永久链接至目标")
:   Get netif interface’s IP address information.

    If the interface is up, IP information is read directly from the TCP/IP stack. If the interface is down, the API just return all 0 information

    参数
    :   - **ifx** – netif interface ID

        - **config** – store the IP4 configuration info

    返回
    :   - BK_OK: succeed

        - BK_ERR_NETIF_IF: invalid netif interface ID

        - BK_ERR_NULL_PARAM: config is NULL

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_netif_get_ip6_addr_info([netif_if_t](#_CPPv410netif_if_t "netif_if_t") ifx)[](#_CPPv426bk_netif_get_ip6_addr_info10netif_if_t "永久链接至目标")
:   Get netif interface’s IP6 address information.

    If the interface is up, IP6 information is read directly from the TCP/IP stack. If the interface is down, the API just return all 0 information

    参数
    :   **ifx** – netif interface ID

    返回
    :   - BK_OK: succeed

        - BK_ERR_NETIF_IF: invalid netif interface ID

        - BK_ERR_NULL_PARAM: config is NULL

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_netif_dhcpc_start([netif_if_t](#_CPPv410netif_if_t "netif_if_t") ifx)[](#_CPPv420bk_netif_dhcpc_start10netif_if_t "永久链接至目标")
:   Start the DHCP client for specified interface.

    If this API is called, the interface will get the IP address via DHCP.

    If the interface is has a static IP and is already up, we need to stop the interface (for STA, call [bk_wifi_sta_stop()](../wifi/bk_wifi.html#group__bk__api__wifi__v2_1ga6f40eb9305ae390f7d777d652197894b "../wifi/bk_wifi.html#group__bk__api__wifi__v2_1ga6f40eb9305ae390f7d777d652197894b") or [bk_wifi_sta_disconnect()](../wifi/bk_wifi.html#group__bk__api__wifi__v2_1gae00bc75a589a66a378037c5adb05bc11 "../wifi/bk_wifi.html#group__bk__api__wifi__v2_1gae00bc75a589a66a378037c5adb05bc11") to stop the interface) before this API is called, or restart the interface after this API is called.

    参数
    :   **ifx** – netif interface ID, currently only support NETIF_IF_STA.

    返回
    :   - BK_OK: succeed

        - BK_ERR_NETIF_IF: invalid netif interface ID

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_netif_static_ip([netif_ip4_config_t](#_CPPv418netif_ip4_config_t "netif_ip4_config_t") static_ip4_config)[](#_CPPv418bk_netif_static_ip18netif_ip4_config_t "永久链接至目标")
:   this function is only for the interface of NETIF_IF_STA to set a static IP .

    call back this function in netif_wifi_event_cb()(in components/bk_netif/bk_netif.c) when case EVENT_WIFI_STA_CONNECTED, and pass the param static_ip4_config includes ip, mask, gateway and dns for your static IP config. example: switch (event_id) { case EVENT_WIFI_STA_CONNECTED: #if CONFIG_LWIP bk_netif_static_ip(static_ip4_config); sta_ip_start(); #endif

    参数
    :   **static_ip4_config** – ipv4 config for this netif(only for NETIF_IF_STA).

    返回
    :   - BK_OK: succeed

        - else: fail


## Netif API Typedefs[](#netif-api-typedefs "永久链接至标题")


### Header File[](#id1 "永久链接至标题")


- [netif_types.h](https://github.com/bekencorp/armino/blob/main/components/netif_types.h "https://github.com/bekencorp/armino/blob/main/components/netif_types.h")


### Structures[](#structures "永久链接至标题")

struct netif_ip4_config_t[](#_CPPv418netif_ip4_config_t "永久链接至目标")
:   Public Members

    char ip[NETIF_IP4_STR_LEN][](#_CPPv4N18netif_ip4_config_t2ipE "永久链接至目标")
    :   Local IP address.

    char mask[NETIF_IP4_STR_LEN][](#_CPPv4N18netif_ip4_config_t4maskE "永久链接至目标")
    :   Netmask.

    char gateway[NETIF_IP4_STR_LEN][](#_CPPv4N18netif_ip4_config_t7gatewayE "永久链接至目标")
    :   Gateway IP address.

    char dns[NETIF_IP4_STR_LEN][](#_CPPv4N18netif_ip4_config_t3dnsE "永久链接至目标")
    :   DNS server IP address.

struct netif_event_got_ip4_t[](#_CPPv421netif_event_got_ip4_t "永久链接至目标")
:   Public Members

    [netif_if_t](#_CPPv410netif_if_t "netif_if_t") netif_if[](#_CPPv4N21netif_event_got_ip4_t8netif_ifE "永久链接至目标")
    :   Netif interface ID

    char ip[NETIF_IP4_STR_LEN][](#_CPPv4N21netif_event_got_ip4_t2ipE "永久链接至目标")
    :   Local IP address.


### Macros[](#macros "永久链接至标题")

NETIF_IP4_STR_LEN[](#c.NETIF_IP4_STR_LEN "永久链接至目标")
:   IP4 string length

BK_ERR_NETIF_IF[](#c.BK_ERR_NETIF_IF "永久链接至目标")
:   Invalid interface ID


### Enumerations[](#enumerations "永久链接至标题")

enum netif_if_t[](#_CPPv410netif_if_t "永久链接至目标")
:   *Values:*

    enumerator NETIF_IF_STA[](#_CPPv4N10netif_if_t12NETIF_IF_STAE "永久链接至目标")
    :   WiFi STA interface

    enumerator NETIF_IF_AP[](#_CPPv4N10netif_if_t11NETIF_IF_APE "永久链接至目标")
    :   WiFi AP interface

    enumerator NETIF_IF_BRIDGE[](#_CPPv4N10netif_if_t15NETIF_IF_BRIDGEE "永久链接至目标")
    :   WiFi BR interface

    enumerator NETIF_IF_ETH[](#_CPPv4N10netif_if_t12NETIF_IF_ETHE "永久链接至目标")
    :   ETH interface

    enumerator NETIF_IF_COUNT[](#_CPPv4N10netif_if_t14NETIF_IF_COUNTE "永久链接至目标")
    :   Number of BK netif

    enumerator NETIF_IF_INVALID[](#_CPPv4N10netif_if_t16NETIF_IF_INVALIDE "永久链接至目标")
    :   Invalid BK netif

enum netif_event_t[](#_CPPv413netif_event_t "永久链接至目标")
:   *Values:*

    enumerator EVENT_NETIF_GOT_IP4[](#_CPPv4N13netif_event_t19EVENT_NETIF_GOT_IP4E "永久链接至目标")
    :   Netif get IP4 event

    enumerator EVENT_NETIF_GOT_IP6[](#_CPPv4N13netif_event_t19EVENT_NETIF_GOT_IP6E "永久链接至目标")
    :   Netif get IP6 event

    enumerator EVENT_NETIF_DHCP_TIMEOUT[](#_CPPv4N13netif_event_t24EVENT_NETIF_DHCP_TIMEOUTE "永久链接至目标")
