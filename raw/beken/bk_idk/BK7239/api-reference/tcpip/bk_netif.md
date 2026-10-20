---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_idk/bk7239/zh_CN/v2.2.1/api-reference/tcpip/bk_netif.html
sdk_family: bk_idk
chip: BK7239
processor: ''
sdk_version: v2.2.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bk-netif"></a>

# BK NETIF

<a id="netif-api-reference"></a>

## Netif API Reference

<a id="header-file"></a>

### Header File

- [netif.h](https://github.com/bekencorp/armino/blob/main/components/netif.h)

<a id="functions"></a>

### Functions

<a id="_CPPv413bk_netif_initv"></a>

<a id="_CPPv313bk_netif_initv"></a> <a id="_CPPv213bk_netif_initv"></a> <a id="bk_netif_init__void"></a> <a id="group__bk__api__netif_1ga720871c7f8c43476bf38f991333fa194"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_netif\_init(void)
:   Initialize the TCP/IP stack.

    **Attention**
    :   This API should be called exactly once from application code, when the application starts up.

    返回
    :   - BK\_OK: success
        - BK\_FAIL: otherwise

<a id="_CPPv423bk_netif_set_ip4_config10netif_if_tPK18netif_ip4_config_t"></a>

<a id="_CPPv323bk_netif_set_ip4_config10netif_if_tPK18netif_ip4_config_t"></a> <a id="_CPPv223bk_netif_set_ip4_config10netif_if_tPK18netif_ip4_config_t"></a> <a id="bk_netif_set_ip4_config__netif_if_t.netif_ip4_config_tCP"></a> <a id="group__bk__api__netif_1gadd74802f5d3fc434591918381e307cf6"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_netif\_set\_ip4\_config([netif\_if\_t](#_CPPv410netif_if_t "netif_if_t") ifx, const [netif\_ip4\_config\_t](#_CPPv418netif_ip4_config_t "netif_ip4_config_t") \*config)
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

<a id="_CPPv323bk_netif_get_ip4_config10netif_if_tP18netif_ip4_config_t"></a> <a id="_CPPv223bk_netif_get_ip4_config10netif_if_tP18netif_ip4_config_t"></a> <a id="bk_netif_get_ip4_config__netif_if_t.netif_ip4_config_tP"></a> <a id="group__bk__api__netif_1ga634a0e17fa52056d78f5f5c83af69173"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_netif\_get\_ip4\_config([netif\_if\_t](#_CPPv410netif_if_t "netif_if_t") ifx, [netif\_ip4\_config\_t](#_CPPv418netif_ip4_config_t "netif_ip4_config_t") \*config)
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

<a id="_CPPv326bk_netif_get_ip6_addr_info10netif_if_t"></a> <a id="_CPPv226bk_netif_get_ip6_addr_info10netif_if_t"></a> <a id="bk_netif_get_ip6_addr_info__netif_if_t"></a> <a id="group__bk__api__netif_1ga8c7db2d41ccae10db35a5b31f90baf44"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_netif\_get\_ip6\_addr\_info([netif\_if\_t](#_CPPv410netif_if_t "netif_if_t") ifx)
:   Get netif interface’s IP6 address information.

    If the interface is up, IP6 information is read directly from the TCP/IP stack. If the interface is down, the API just return all 0 information

    参数
    :   **ifx** – netif interface ID

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NETIF\_IF: invalid netif interface ID
        - BK\_ERR\_NULL\_PARAM: config is NULL

<a id="_CPPv420bk_netif_dhcpc_start10netif_if_t"></a>

<a id="_CPPv320bk_netif_dhcpc_start10netif_if_t"></a> <a id="_CPPv220bk_netif_dhcpc_start10netif_if_t"></a> <a id="bk_netif_dhcpc_start__netif_if_t"></a> <a id="group__bk__api__netif_1ga91b4e04aa1b04f721f9d88f03b7fe451"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_netif\_dhcpc\_start([netif\_if\_t](#_CPPv410netif_if_t "netif_if_t") ifx)
:   Start the DHCP client for specified interface.

    If this API is called, the interface will get the IP address via DHCP.

    If the interface is has a static IP and is already up, we need to stop the interface (for STA, call [bk\_wifi\_sta\_stop()](../wifi/bk_wifi.md#group__bk__api__wifi__v2_1ga6f40eb9305ae390f7d777d652197894b) or [bk\_wifi\_sta\_disconnect()](../wifi/bk_wifi.md#group__bk__api__wifi__v2_1gae00bc75a589a66a378037c5adb05bc11) to stop the interface) before this API is called, or restart the interface after this API is called.

    参数
    :   **ifx** – netif interface ID, currently only support NETIF\_IF\_STA.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NETIF\_IF: invalid netif interface ID

<a id="_CPPv418bk_netif_static_ip18netif_ip4_config_t"></a>

<a id="_CPPv318bk_netif_static_ip18netif_ip4_config_t"></a> <a id="_CPPv218bk_netif_static_ip18netif_ip4_config_t"></a> <a id="bk_netif_static_ip__netif_ip4_config_t"></a> <a id="group__bk__api__netif_1ga9fd50f873579d4d8a9f85e6af28225dc"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_netif\_static\_ip([netif\_ip4\_config\_t](#_CPPv418netif_ip4_config_t "netif_ip4_config_t") static\_ip4\_config)
:   this function is only for the interface of NETIF\_IF\_STA to set a static IP .

    call back this function in netif\_wifi\_event\_cb()(in components/bk\_netif/bk\_netif.c) when case EVENT\_WIFI\_STA\_CONNECTED, and pass the param static\_ip4\_config includes ip, mask, gateway and dns for your static IP config. example: switch (event\_id) { case EVENT\_WIFI\_STA\_CONNECTED: #if CONFIG\_LWIP bk\_netif\_static\_ip(static\_ip4\_config); sta\_ip\_start(); #endif

    参数
    :   **static\_ip4\_config** – ipv4 config for this netif(only for NETIF\_IF\_STA).

    返回
    :   - BK\_OK: succeed
        - else: fail

<a id="netif-api-typedefs"></a>

## Netif API Typedefs

<a id="id1"></a>

### Header File

- [netif\_types.h](https://github.com/bekencorp/armino/blob/main/components/netif_types.h)

<a id="structures"></a>

### Structures

<a id="_CPPv418netif_ip4_config_t"></a>

<a id="_CPPv318netif_ip4_config_t"></a> <a id="_CPPv218netif_ip4_config_t"></a> <a id="netif_ip4_config_t"></a> <a id="structnetif__ip4__config__t"></a> struct netif\_ip4\_config\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18netif_ip4_config_t2ipE"></a>

    <a id="_CPPv3N18netif_ip4_config_t2ipE"></a> <a id="_CPPv2N18netif_ip4_config_t2ipE"></a> <a id="netif_ip4_config_t::ip__cA"></a> <a id="structnetif__ip4__config__t_1a2fa5668658e3cd4267ea2db731d20fe7"></a> char ip\[NETIF\_IP4\_STR\_LEN\]
    :   Local IP address.

    <a id="_CPPv4N18netif_ip4_config_t4maskE"></a>

    <a id="_CPPv3N18netif_ip4_config_t4maskE"></a> <a id="_CPPv2N18netif_ip4_config_t4maskE"></a> <a id="netif_ip4_config_t::mask__cA"></a> <a id="structnetif__ip4__config__t_1a4cac0e2c02e738cd8aee1a4a79df163e"></a> char mask\[NETIF\_IP4\_STR\_LEN\]
    :   Netmask.

    <a id="_CPPv4N18netif_ip4_config_t7gatewayE"></a>

    <a id="_CPPv3N18netif_ip4_config_t7gatewayE"></a> <a id="_CPPv2N18netif_ip4_config_t7gatewayE"></a> <a id="netif_ip4_config_t::gateway__cA"></a> <a id="structnetif__ip4__config__t_1af885cd7d2ab730b9507abc4f9dc360d8"></a> char gateway\[NETIF\_IP4\_STR\_LEN\]
    :   Gateway IP address.

    <a id="_CPPv4N18netif_ip4_config_t3dnsE"></a>

    <a id="_CPPv3N18netif_ip4_config_t3dnsE"></a> <a id="_CPPv2N18netif_ip4_config_t3dnsE"></a> <a id="netif_ip4_config_t::dns__cA"></a> <a id="structnetif__ip4__config__t_1a4c2c025eaa7c1d4a3c7011377ad65b48"></a> char dns\[NETIF\_IP4\_STR\_LEN\]
    :   DNS server IP address.

<a id="_CPPv421netif_event_got_ip4_t"></a>

<a id="_CPPv321netif_event_got_ip4_t"></a> <a id="_CPPv221netif_event_got_ip4_t"></a> <a id="netif_event_got_ip4_t"></a> <a id="structnetif__event__got__ip4__t"></a> struct netif\_event\_got\_ip4\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N21netif_event_got_ip4_t8netif_ifE"></a>

    <a id="_CPPv3N21netif_event_got_ip4_t8netif_ifE"></a> <a id="_CPPv2N21netif_event_got_ip4_t8netif_ifE"></a> <a id="netif_event_got_ip4_t::netif_if__netif_if_t"></a> <a id="structnetif__event__got__ip4__t_1a343bd40a06dc6cd07a6054fe5e90bbb1"></a> [netif\_if\_t](#_CPPv410netif_if_t "netif_if_t") netif\_if
    :   Netif interface ID

    <a id="_CPPv4N21netif_event_got_ip4_t2ipE"></a>

    <a id="_CPPv3N21netif_event_got_ip4_t2ipE"></a> <a id="_CPPv2N21netif_event_got_ip4_t2ipE"></a> <a id="netif_event_got_ip4_t::ip__cA"></a> <a id="structnetif__event__got__ip4__t_1ac7bb091a006f53a76a16aac95e5d52f3"></a> char ip\[NETIF\_IP4\_STR\_LEN\]
    :   Local IP address.

    <a id="_CPPv4N21netif_event_got_ip4_t4maskE"></a>

    <a id="_CPPv3N21netif_event_got_ip4_t4maskE"></a> <a id="_CPPv2N21netif_event_got_ip4_t4maskE"></a> <a id="netif_event_got_ip4_t::mask__cA"></a> <a id="structnetif__event__got__ip4__t_1aaff692e9b033d02ab994258b9c65d882"></a> char mask\[NETIF\_IP4\_STR\_LEN\]
    :   Netmask.

    <a id="_CPPv4N21netif_event_got_ip4_t7gatewayE"></a>

    <a id="_CPPv3N21netif_event_got_ip4_t7gatewayE"></a> <a id="_CPPv2N21netif_event_got_ip4_t7gatewayE"></a> <a id="netif_event_got_ip4_t::gateway__cA"></a> <a id="structnetif__event__got__ip4__t_1a800a212a62817056124f680b43c98a99"></a> char gateway\[NETIF\_IP4\_STR\_LEN\]
    :   Gateway IP address.

<a id="macros"></a>

### Macros

<a id="c.NETIF_IP4_STR_LEN"></a>

<a id="group__bk__api__netif__typedef_1ga759a49b7285f6291564fed85c38244fe"></a> NETIF\_IP4\_STR\_LEN
:   IP4 string length

<a id="c.BK_ERR_NETIF_IF"></a>

<a id="group__bk__api__netif__typedef_1ga2b28552175259825f7e58af945507ddb"></a> BK\_ERR\_NETIF\_IF
:   Invalid interface ID

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv410netif_if_t"></a>

<a id="_CPPv310netif_if_t"></a> <a id="_CPPv210netif_if_t"></a> <a id="group__bk__api__netif__typedef_1gafd0e8f6d2cd5550a97425b19e844266e"></a> enum netif\_if\_t
:   *Values:*

    <a id="_CPPv4N10netif_if_t12NETIF_IF_STAE"></a>

    <a id="_CPPv3N10netif_if_t12NETIF_IF_STAE"></a> <a id="_CPPv2N10netif_if_t12NETIF_IF_STAE"></a> <a id="group__bk__api__netif__typedef_1ggafd0e8f6d2cd5550a97425b19e844266eadc188233960b61928d00b47db2e42931"></a> enumerator NETIF\_IF\_STA
    :   WiFi STA interface

    <a id="_CPPv4N10netif_if_t11NETIF_IF_APE"></a>

    <a id="_CPPv3N10netif_if_t11NETIF_IF_APE"></a> <a id="_CPPv2N10netif_if_t11NETIF_IF_APE"></a> <a id="group__bk__api__netif__typedef_1ggafd0e8f6d2cd5550a97425b19e844266ea2a6344633c82cd07692275647736200a"></a> enumerator NETIF\_IF\_AP
    :   WiFi AP interface

    <a id="_CPPv4N10netif_if_t15NETIF_IF_BRIDGEE"></a>

    <a id="_CPPv3N10netif_if_t15NETIF_IF_BRIDGEE"></a> <a id="_CPPv2N10netif_if_t15NETIF_IF_BRIDGEE"></a> <a id="group__bk__api__netif__typedef_1ggafd0e8f6d2cd5550a97425b19e844266ea73c86e8425a30941da583eb34cf8ee77"></a> enumerator NETIF\_IF\_BRIDGE
    :   WiFi BR interface

    <a id="_CPPv4N10netif_if_t12NETIF_IF_ETHE"></a>

    <a id="_CPPv3N10netif_if_t12NETIF_IF_ETHE"></a> <a id="_CPPv2N10netif_if_t12NETIF_IF_ETHE"></a> <a id="group__bk__api__netif__typedef_1ggafd0e8f6d2cd5550a97425b19e844266ea8e2d44ceed69642a5745927a02cc626d"></a> enumerator NETIF\_IF\_ETH
    :   ETH interface

    <a id="_CPPv4N10netif_if_t14NETIF_IF_COUNTE"></a>

    <a id="_CPPv3N10netif_if_t14NETIF_IF_COUNTE"></a> <a id="_CPPv2N10netif_if_t14NETIF_IF_COUNTE"></a> <a id="group__bk__api__netif__typedef_1ggafd0e8f6d2cd5550a97425b19e844266eaac5e277f9669fb8db044fcb3ac33b237"></a> enumerator NETIF\_IF\_COUNT
    :   Number of BK netif

    <a id="_CPPv4N10netif_if_t16NETIF_IF_INVALIDE"></a>

    <a id="_CPPv3N10netif_if_t16NETIF_IF_INVALIDE"></a> <a id="_CPPv2N10netif_if_t16NETIF_IF_INVALIDE"></a> <a id="group__bk__api__netif__typedef_1ggafd0e8f6d2cd5550a97425b19e844266eac6a9cc0e75a493b3f06f729393896f31"></a> enumerator NETIF\_IF\_INVALID
    :   Invalid BK netif

<a id="_CPPv413netif_event_t"></a>

<a id="_CPPv313netif_event_t"></a> <a id="_CPPv213netif_event_t"></a> <a id="group__bk__api__netif__typedef_1gaee42e295fc1554aa4e1a496eca95bdb1"></a> enum netif\_event\_t
:   *Values:*

    <a id="_CPPv4N13netif_event_t19EVENT_NETIF_GOT_IP4E"></a>

    <a id="_CPPv3N13netif_event_t19EVENT_NETIF_GOT_IP4E"></a> <a id="_CPPv2N13netif_event_t19EVENT_NETIF_GOT_IP4E"></a> <a id="group__bk__api__netif__typedef_1ggaee42e295fc1554aa4e1a496eca95bdb1ad73d2fcda5d6a347b3e72364fd1791db"></a> enumerator EVENT\_NETIF\_GOT\_IP4
    :   Netif get IP4 event

    <a id="_CPPv4N13netif_event_t19EVENT_NETIF_GOT_IP6E"></a>

    <a id="_CPPv3N13netif_event_t19EVENT_NETIF_GOT_IP6E"></a> <a id="_CPPv2N13netif_event_t19EVENT_NETIF_GOT_IP6E"></a> <a id="group__bk__api__netif__typedef_1ggaee42e295fc1554aa4e1a496eca95bdb1a47b2c36ba948a8dfc449fa8c36243282"></a> enumerator EVENT\_NETIF\_GOT\_IP6
    :   Netif get IP6 event

    <a id="_CPPv4N13netif_event_t24EVENT_NETIF_DHCP_TIMEOUTE"></a>

    <a id="_CPPv3N13netif_event_t24EVENT_NETIF_DHCP_TIMEOUTE"></a> <a id="_CPPv2N13netif_event_t24EVENT_NETIF_DHCP_TIMEOUTE"></a> <a id="group__bk__api__netif__typedef_1ggaee42e295fc1554aa4e1a496eca95bdb1a1700ebfc3560dd7f451b3feabe0872c0"></a> enumerator EVENT\_NETIF\_DHCP\_TIMEOUT
