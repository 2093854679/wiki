---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/btif/a2dp_if.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="a2dp-interface-functions"></a>

# A2DP Interface Functions

<a id="a2dp-if-api-brief"></a>

## A2DP\_IF API Brief

| Application | Brief |
| --- | --- |
| [`a2dp_if_snk_connect()`](#_CPPv419a2dp_if_snk_connectP14btif_bd_addr_t "a2dp_if_snk_connect") | A2DP sink connect API |
| [`a2dp_if_snk_disconnect()`](#_CPPv422a2dp_if_snk_disconnect8uint16_t "a2dp_if_snk_disconnect") | A2DP sink disconnect API |
| [`a2dp_if_snk_set_active_device()`](#_CPPv429a2dp_if_snk_set_active_device8uint16_tb "a2dp_if_snk_set_active_device") | Set active device to the a2dp stack |
| [`a2dp_if_snk_register_stack_callback()`](#_CPPv435a2dp_if_snk_register_stack_callbackP20btif_a2dp_register_t "a2dp_if_snk_register_stack_callback") | A2DP sink register event callback API |
| [`a2dp_if_snk_init()`](#_CPPv416a2dp_if_snk_initP28btif_a2dp_snk_register_sep_t7uint8_t "a2dp_if_snk_init") | A2DP sink init function API |
| [`a2dp_if_get_sync_len()`](#_CPPv420a2dp_if_get_sync_lenP14btif_bd_addr_t "a2dp_if_get_sync_len") | return the profile sync used max buffer size |
| [`a2dp_if_conn_sync()`](#_CPPv417a2dp_if_conn_syncP14btif_bd_addr_tP7uint8_t8uint16_tP8uint16_t "a2dp_if_conn_sync") | TWS master used to send sync profile data to slave |
| [`a2dp_if_conn_restore()`](#_CPPv420a2dp_if_conn_restoreP14btif_bd_addr_tP7uint8_t8uint16_t "a2dp_if_conn_restore") | TWS slave used to rebuild its host stack |
| [`a2dp_if_conn_restore_specific()`](#_CPPv429a2dp_if_conn_restore_specificP14btif_bd_addr_t8uint16_t "a2dp_if_conn_restore_specific") | TWS slave update A2DP connection handle and recover relevant settings |
| [`a2dp_if_snk_stream_is_started()`](#_CPPv429a2dp_if_snk_stream_is_started8uint16_t "a2dp_if_snk_stream_is_started") | check A2DP music is streaming or not |
| [`a2dp_if_set_delay_rpt()`](#_CPPv421a2dp_if_set_delay_rpt8uint16_t8uint16_t "a2dp_if_set_delay_rpt") | update delay report aluje |

<a id="a2dp-if-api-reference"></a>

## A2DP\_IF API Reference

<a id="header-file"></a>

### Header File

- [btif/inc/a2dp\_if.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/btif/inc/a2dp_if.h)

<a id="functions"></a>

### Functions

<a id="_CPPv419a2dp_if_snk_connectP14btif_bd_addr_t"></a>

<a id="_CPPv319a2dp_if_snk_connectP14btif_bd_addr_t"></a> <a id="_CPPv219a2dp_if_snk_connectP14btif_bd_addr_t"></a> <a id="a2dp_if_snk_connect__btif_bd_addr_tP"></a> <a id="a2dp__if_8h_1a4971dc5db17ce0288640e2727def0c15"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") a2dp\_if\_snk\_connect([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)
:   a2dp\_if\_snk\_connect brief description

    A2DP sink connect API

    参数:
    :   **p\_addr** – **\[in\]** remote BT MAC address

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv422a2dp_if_snk_disconnect8uint16_t"></a>

<a id="_CPPv322a2dp_if_snk_disconnect8uint16_t"></a> <a id="_CPPv222a2dp_if_snk_disconnect8uint16_t"></a> <a id="a2dp_if_snk_disconnect__uint16_t"></a> <a id="a2dp__if_8h_1abf7257668800989c34018ea06b02eee9"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") a2dp\_if\_snk\_disconnect(uint16\_t handle)
:   a2dp\_if\_snk\_disconnect brief description

    A2DP sink disconnect API

    参数:
    :   **handle** – **\[in\]** connection handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv429a2dp_if_snk_set_active_device8uint16_tb"></a>

<a id="_CPPv329a2dp_if_snk_set_active_device8uint16_tb"></a> <a id="_CPPv229a2dp_if_snk_set_active_device8uint16_tb"></a> <a id="a2dp_if_snk_set_active_device__uint16_t.b"></a> <a id="a2dp__if_8h_1adfe63cef7fdc7d233a7f6b4152d93a1c"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") a2dp\_if\_snk\_set\_active\_device(uint16\_t handle, bool active)
:   a2dp\_if\_snk\_set\_active\_device brief description

    Set active device to the a2dp stack

    参数:
    :   - **handle** – **\[in\]** acl handle
        - **active** – **\[in\]** true:active false:not Active

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv435a2dp_if_snk_register_stack_callbackP20btif_a2dp_register_t"></a>

<a id="_CPPv335a2dp_if_snk_register_stack_callbackP20btif_a2dp_register_t"></a> <a id="_CPPv235a2dp_if_snk_register_stack_callbackP20btif_a2dp_register_t"></a> <a id="a2dp_if_snk_register_stack_callback__btif_a2dp_register_tP"></a> <a id="a2dp__if_8h_1ad2544d3b30e2638d201bcc1f04045898"></a> void a2dp\_if\_snk\_register\_stack\_callback([btif\_a2dp\_register\_t](#_CPPv420btif_a2dp_register_t "btif_a2dp_register_t") \*p\_callback)
:   a2dp\_if\_snk\_register\_stack\_callback brief description

    A2DP sink register event callback API

    参数:
    :   **p\_callback** – **\[in\]** strcut of callback function

    返回:
    :   N/A

<a id="_CPPv416a2dp_if_snk_initP28btif_a2dp_snk_register_sep_t7uint8_t"></a>

<a id="_CPPv316a2dp_if_snk_initP28btif_a2dp_snk_register_sep_t7uint8_t"></a> <a id="_CPPv216a2dp_if_snk_initP28btif_a2dp_snk_register_sep_t7uint8_t"></a> <a id="a2dp_if_snk_init__btif_a2dp_snk_register_sep_tP.uint8_t"></a> <a id="a2dp__if_8h_1a1b1a8f90b413b20339f7c79086101d75"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") a2dp\_if\_snk\_init([btif\_a2dp\_snk\_register\_sep\_t](#_CPPv428btif_a2dp_snk_register_sep_t "btif_a2dp_snk_register_sep_t") \*p\_reg\_sep, uint8\_t sep\_cnt)
:   a2dp\_if\_snk\_init brief description

    A2DP sink init function API

    参数:
    :   - **p\_reg\_sep** – **\[in\]** configured setting of stream end point array
        - **sep\_cnt** – **\[in\]** count of stream end point

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv420a2dp_if_get_sync_lenP14btif_bd_addr_t"></a>

<a id="_CPPv320a2dp_if_get_sync_lenP14btif_bd_addr_t"></a> <a id="_CPPv220a2dp_if_get_sync_lenP14btif_bd_addr_t"></a> <a id="a2dp_if_get_sync_len__btif_bd_addr_tP"></a> <a id="a2dp__if_8h_1a7d458e4c0fa4334715d8f98c75a466eb"></a> uint16\_t a2dp\_if\_get\_sync\_len([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)
:   a2dp\_if\_get\_sync\_len brief description

    return the profile sync used max buffer size

    参数:
    :   **p\_addr** – **\[in\]** remote BT MAC address

    返回:
    :   data length

<a id="_CPPv417a2dp_if_conn_syncP14btif_bd_addr_tP7uint8_t8uint16_tP8uint16_t"></a>

<a id="_CPPv317a2dp_if_conn_syncP14btif_bd_addr_tP7uint8_t8uint16_tP8uint16_t"></a> <a id="_CPPv217a2dp_if_conn_syncP14btif_bd_addr_tP7uint8_t8uint16_tP8uint16_t"></a> <a id="a2dp_if_conn_sync__btif_bd_addr_tP.uint8_tP.uint16_t.uint16_tP"></a> <a id="a2dp__if_8h_1ab0d431508247b7b1eca9810cd6c44723"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") a2dp\_if\_conn\_sync([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr, uint8\_t \*p\_buff, uint16\_t buff\_len, uint16\_t \*p\_length)
:   a2dp\_if\_conn\_sync brief description

    TWS master used to send sync profile data to slave

    参数:
    :   - **addr** – **\[in\]** remote BT MAC addresss
        - **p\_buff** – **\[out\]** buffer used to sync profile data
        - **buff\_len** – **\[in\]** p\_buff allocated length
        - **p\_length** – **\[out\]** sync profile data length will be sent

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv420a2dp_if_conn_restoreP14btif_bd_addr_tP7uint8_t8uint16_t"></a>

<a id="_CPPv320a2dp_if_conn_restoreP14btif_bd_addr_tP7uint8_t8uint16_t"></a> <a id="_CPPv220a2dp_if_conn_restoreP14btif_bd_addr_tP7uint8_t8uint16_t"></a> <a id="a2dp_if_conn_restore__btif_bd_addr_tP.uint8_tP.uint16_t"></a> <a id="a2dp__if_8h_1a825fc6da4fbc12d249e11c86f5d89a5e"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") a2dp\_if\_conn\_restore([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr, uint8\_t \*p\_buff, uint16\_t length)
:   a2dp\_if\_conn\_restore brief description

    TWS slave used to rebuild its host stack

    参数:
    :   - **addr** – **\[in\]** remote BT MAC address
        - **p\_buff** – **\[in\]** sync profile data
        - **length** – **\[in\]** p\_buff data length

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv429a2dp_if_conn_restore_specificP14btif_bd_addr_t8uint16_t"></a>

<a id="_CPPv329a2dp_if_conn_restore_specificP14btif_bd_addr_t8uint16_t"></a> <a id="_CPPv229a2dp_if_conn_restore_specificP14btif_bd_addr_t8uint16_t"></a> <a id="a2dp_if_conn_restore_specific__btif_bd_addr_tP.uint16_t"></a> <a id="a2dp__if_8h_1a6d12dd400d90c5c8ba7b9d7a9dfdbc66"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") a2dp\_if\_conn\_restore\_specific([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr, uint16\_t handle)
:   a2dp\_if\_conn\_restore\_specific brief description

    TWS slave update A2DP connection handle and recover relevant settings

    参数:
    :   - **p\_addr** – **\[in\]** remote BT MAC address
        - **handle** – **\[in\]** connection handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv429a2dp_if_snk_stream_is_started8uint16_t"></a>

<a id="_CPPv329a2dp_if_snk_stream_is_started8uint16_t"></a> <a id="_CPPv229a2dp_if_snk_stream_is_started8uint16_t"></a> <a id="a2dp_if_snk_stream_is_started__uint16_t"></a> <a id="a2dp__if_8h_1a9cdfb72d370aab90274141e10ce6d641"></a> bool a2dp\_if\_snk\_stream\_is\_started(uint16\_t handle)
:   a2dp\_if\_snk\_stream\_is\_started brief description

    check A2DP music is streaming or not

    参数:
    :   **handle** – **\[in\]** connection handle

    返回值:
    :   - **true** – start
        - **fail** – stop

    返回:
    :   result

<a id="_CPPv421a2dp_if_set_delay_rpt8uint16_t8uint16_t"></a>

<a id="_CPPv321a2dp_if_set_delay_rpt8uint16_t8uint16_t"></a> <a id="_CPPv221a2dp_if_set_delay_rpt8uint16_t8uint16_t"></a> <a id="a2dp_if_set_delay_rpt__uint16_t.uint16_t"></a> <a id="a2dp__if_8h_1a1deedf88ddc881397367030df53726e6"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") a2dp\_if\_set\_delay\_rpt(uint16\_t handle, uint16\_t delay\_rpt\_100us)
:   a2dp\_if\_set\_delay\_rpt brief description

    update delay report aluje

    参数:
    :   - **handle** – **\[in\]** connection handle
        - **delay\_rpt\_100us** – **\[in\]** delay report value(unit:100us)

    返回:
    :   result

<a id="structures"></a>

### Structures

<a id="_CPPv418btif_a2dp_cb_hdr_t"></a>

<a id="_CPPv318btif_a2dp_cb_hdr_t"></a> <a id="_CPPv218btif_a2dp_cb_hdr_t"></a> <a id="btif_a2dp_cb_hdr_t"></a> <a id="structbtif__a2dp__cb__hdr__t"></a> struct btif\_a2dp\_cb\_hdr\_t
:   A2DP header data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18btif_a2dp_cb_hdr_t5eventE"></a>

    <a id="_CPPv3N18btif_a2dp_cb_hdr_t5eventE"></a> <a id="_CPPv2N18btif_a2dp_cb_hdr_t5eventE"></a> <a id="btif_a2dp_cb_hdr_t::event__btif_a2dp_evt_t"></a> <a id="structbtif__a2dp__cb__hdr__t_1af307a1256e3e0c8748e9e8c8ea5c850d"></a> [btif\_a2dp\_evt\_t](#_CPPv415btif_a2dp_evt_t "btif_a2dp_evt_t") event
    :   event index

    <a id="_CPPv4N18btif_a2dp_cb_hdr_t6handleE"></a>

    <a id="_CPPv3N18btif_a2dp_cb_hdr_t6handleE"></a> <a id="_CPPv2N18btif_a2dp_cb_hdr_t6handleE"></a> <a id="btif_a2dp_cb_hdr_t::handle__uint16_t"></a> <a id="structbtif__a2dp__cb__hdr__t_1afb630d5294c382474893d1a1f386f428"></a> uint16\_t handle
    :   connection handle

    <a id="_CPPv4N18btif_a2dp_cb_hdr_t4scidE"></a>

    <a id="_CPPv3N18btif_a2dp_cb_hdr_t4scidE"></a> <a id="_CPPv2N18btif_a2dp_cb_hdr_t4scidE"></a> <a id="btif_a2dp_cb_hdr_t::scid__uint16_t"></a> <a id="structbtif__a2dp__cb__hdr__t_1a42b59135d72fc85d54cc45f4b6bc3044"></a> uint16\_t scid
    :   source CID

<a id="_CPPv419btif_a2dp_conn_cb_t"></a>

<a id="_CPPv319btif_a2dp_conn_cb_t"></a> <a id="_CPPv219btif_a2dp_conn_cb_t"></a> <a id="btif_a2dp_conn_cb_t"></a> <a id="structbtif__a2dp__conn__cb__t"></a> struct btif\_a2dp\_conn\_cb\_t
:   A2DP connect status data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N19btif_a2dp_conn_cb_t3hdrE"></a>

    <a id="_CPPv3N19btif_a2dp_conn_cb_t3hdrE"></a> <a id="_CPPv2N19btif_a2dp_conn_cb_t3hdrE"></a> <a id="btif_a2dp_conn_cb_t::hdr__btif_a2dp_cb_hdr_t"></a> <a id="structbtif__a2dp__conn__cb__t_1afe2d3a27fe930d4838366d63ce34590f"></a> [btif\_a2dp\_cb\_hdr\_t](#_CPPv418btif_a2dp_cb_hdr_t "btif_a2dp_cb_hdr_t") hdr
    :   A2DP header data struct

    <a id="_CPPv4N19btif_a2dp_conn_cb_t4addrE"></a>

    <a id="_CPPv3N19btif_a2dp_conn_cb_t4addrE"></a> <a id="_CPPv2N19btif_a2dp_conn_cb_t4addrE"></a> <a id="btif_a2dp_conn_cb_t::addr__btif_bd_addr_t"></a> <a id="structbtif__a2dp__conn__cb__t_1ab293c3f9cf1b5b58a32ca6081a8f71ae"></a> [btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr
    :   remote BT MAC address

    <a id="_CPPv4N19btif_a2dp_conn_cb_t6statusE"></a>

    <a id="_CPPv3N19btif_a2dp_conn_cb_t6statusE"></a> <a id="_CPPv2N19btif_a2dp_conn_cb_t6statusE"></a> <a id="btif_a2dp_conn_cb_t::status__uint8_t"></a> <a id="structbtif__a2dp__conn__cb__t_1a7c0d41749d6221d908a33fd63a52d240"></a> uint8\_t status
    :   status result @btif\_ret\_t

<a id="_CPPv423btif_a2dp_sec_ctrl_cb_t"></a>

<a id="_CPPv323btif_a2dp_sec_ctrl_cb_t"></a> <a id="_CPPv223btif_a2dp_sec_ctrl_cb_t"></a> <a id="btif_a2dp_sec_ctrl_cb_t"></a> <a id="structbtif__a2dp__sec__ctrl__cb__t"></a> struct btif\_a2dp\_sec\_ctrl\_cb\_t
:   A2DP security control data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N23btif_a2dp_sec_ctrl_cb_t3hdrE"></a>

    <a id="_CPPv3N23btif_a2dp_sec_ctrl_cb_t3hdrE"></a> <a id="_CPPv2N23btif_a2dp_sec_ctrl_cb_t3hdrE"></a> <a id="btif_a2dp_sec_ctrl_cb_t::hdr__btif_a2dp_cb_hdr_t"></a> <a id="structbtif__a2dp__sec__ctrl__cb__t_1a577d7343b7575e9c32cca6a86abc6d39"></a> [btif\_a2dp\_cb\_hdr\_t](#_CPPv418btif_a2dp_cb_hdr_t "btif_a2dp_cb_hdr_t") hdr
    :   A2DP header data struct

    <a id="_CPPv4N23btif_a2dp_sec_ctrl_cb_t3lenE"></a>

    <a id="_CPPv3N23btif_a2dp_sec_ctrl_cb_t3lenE"></a> <a id="_CPPv2N23btif_a2dp_sec_ctrl_cb_t3lenE"></a> <a id="btif_a2dp_sec_ctrl_cb_t::len__uint8_t"></a> <a id="structbtif__a2dp__sec__ctrl__cb__t_1aa02bc824d270cbf6cfcfd8a06ab6fbf8"></a> uint8\_t len
    :   length of p\_data

    <a id="_CPPv4N23btif_a2dp_sec_ctrl_cb_t6p_dataE"></a>

    <a id="_CPPv3N23btif_a2dp_sec_ctrl_cb_t6p_dataE"></a> <a id="_CPPv2N23btif_a2dp_sec_ctrl_cb_t6p_dataE"></a> <a id="btif_a2dp_sec_ctrl_cb_t::p_data__uint8_tCP"></a> <a id="structbtif__a2dp__sec__ctrl__cb__t_1ab58ed1ef211f0091da731b823b60ef36"></a> const uint8\_t \*p\_data
    :   security control data buffer

<a id="_CPPv425btif_a2dp_media_data_cb_t"></a>

<a id="_CPPv325btif_a2dp_media_data_cb_t"></a> <a id="_CPPv225btif_a2dp_media_data_cb_t"></a> <a id="btif_a2dp_media_data_cb_t"></a> <a id="structbtif__a2dp__media__data__cb__t"></a> struct btif\_a2dp\_media\_data\_cb\_t
:   A2DP media data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N25btif_a2dp_media_data_cb_t3hdrE"></a>

    <a id="_CPPv3N25btif_a2dp_media_data_cb_t3hdrE"></a> <a id="_CPPv2N25btif_a2dp_media_data_cb_t3hdrE"></a> <a id="btif_a2dp_media_data_cb_t::hdr__btif_a2dp_cb_hdr_t"></a> <a id="structbtif__a2dp__media__data__cb__t_1a5df2fcc690a16e79d3518c2f82f47009"></a> [btif\_a2dp\_cb\_hdr\_t](#_CPPv418btif_a2dp_cb_hdr_t "btif_a2dp_cb_hdr_t") hdr
    :   A2DP header data struct

    <a id="_CPPv4N25btif_a2dp_media_data_cb_t3lenE"></a>

    <a id="_CPPv3N25btif_a2dp_media_data_cb_t3lenE"></a> <a id="_CPPv2N25btif_a2dp_media_data_cb_t3lenE"></a> <a id="btif_a2dp_media_data_cb_t::len__uint16_t"></a> <a id="structbtif__a2dp__media__data__cb__t_1ab9b40b5e7a4a3e80d903ab2b3845c29b"></a> uint16\_t len
    :   length of p\_data

    <a id="_CPPv4N25btif_a2dp_media_data_cb_t6p_dataE"></a>

    <a id="_CPPv3N25btif_a2dp_media_data_cb_t6p_dataE"></a> <a id="_CPPv2N25btif_a2dp_media_data_cb_t6p_dataE"></a> <a id="btif_a2dp_media_data_cb_t::p_data__uint8_tCP"></a> <a id="structbtif__a2dp__media__data__cb__t_1a6b79cdc10aecf3e45306b9451315e022"></a> const uint8\_t \*p\_data
    :   media data buffer

<a id="_CPPv422btif_a2dp_sep_cfg_cb_t"></a>

<a id="_CPPv322btif_a2dp_sep_cfg_cb_t"></a> <a id="_CPPv222btif_a2dp_sep_cfg_cb_t"></a> <a id="btif_a2dp_sep_cfg_cb_t"></a> <a id="structbtif__a2dp__sep__cfg__cb__t"></a> struct btif\_a2dp\_sep\_cfg\_cb\_t
:   A2DP set configure data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N22btif_a2dp_sep_cfg_cb_t3hdrE"></a>

    <a id="_CPPv3N22btif_a2dp_sep_cfg_cb_t3hdrE"></a> <a id="_CPPv2N22btif_a2dp_sep_cfg_cb_t3hdrE"></a> <a id="btif_a2dp_sep_cfg_cb_t::hdr__btif_a2dp_cb_hdr_t"></a> <a id="structbtif__a2dp__sep__cfg__cb__t_1a553c62e7f63ef53171c730aa3f125119"></a> [btif\_a2dp\_cb\_hdr\_t](#_CPPv418btif_a2dp_cb_hdr_t "btif_a2dp_cb_hdr_t") hdr
    :   A2DP header data struct

    <a id="_CPPv4N22btif_a2dp_sep_cfg_cb_t11remote_seidE"></a>

    <a id="_CPPv3N22btif_a2dp_sep_cfg_cb_t11remote_seidE"></a> <a id="_CPPv2N22btif_a2dp_sep_cfg_cb_t11remote_seidE"></a> <a id="btif_a2dp_sep_cfg_cb_t::remote_seid__uint8_t"></a> <a id="structbtif__a2dp__sep__cfg__cb__t_1ae94ae8323196232a9b38060110860d6b"></a> uint8\_t remote\_seid
    :   remote stream end point ID

    <a id="_CPPv4N22btif_a2dp_sep_cfg_cb_t10local_seidE"></a>

    <a id="_CPPv3N22btif_a2dp_sep_cfg_cb_t10local_seidE"></a> <a id="_CPPv2N22btif_a2dp_sep_cfg_cb_t10local_seidE"></a> <a id="btif_a2dp_sep_cfg_cb_t::local_seid__uint8_t"></a> <a id="structbtif__a2dp__sep__cfg__cb__t_1a192c98c55b82c5da9241ac44762174b9"></a> uint8\_t local\_seid
    :   local stream end point ID

    <a id="_CPPv4N22btif_a2dp_sep_cfg_cb_t10media_typeE"></a>

    <a id="_CPPv3N22btif_a2dp_sep_cfg_cb_t10media_typeE"></a> <a id="_CPPv2N22btif_a2dp_sep_cfg_cb_t10media_typeE"></a> <a id="btif_a2dp_sep_cfg_cb_t::media_type__uint8_t"></a> <a id="structbtif__a2dp__sep__cfg__cb__t_1a21aeaff8d61b6bde3deb801de72988ec"></a> uint8\_t media\_type
    :   media type @btif\_a2dp\_media\_type\_t

    <a id="_CPPv4N22btif_a2dp_sep_cfg_cb_t10codec_typeE"></a>

    <a id="_CPPv3N22btif_a2dp_sep_cfg_cb_t10codec_typeE"></a> <a id="_CPPv2N22btif_a2dp_sep_cfg_cb_t10codec_typeE"></a> <a id="btif_a2dp_sep_cfg_cb_t::codec_type__uint8_t"></a> <a id="structbtif__a2dp__sep__cfg__cb__t_1a2402327f20aa92c2ae429a09d3bf9951"></a> uint8\_t codec\_type
    :   codec type

    <a id="_CPPv4N22btif_a2dp_sep_cfg_cb_t8data_lenE"></a>

    <a id="_CPPv3N22btif_a2dp_sep_cfg_cb_t8data_lenE"></a> <a id="_CPPv2N22btif_a2dp_sep_cfg_cb_t8data_lenE"></a> <a id="btif_a2dp_sep_cfg_cb_t::data_len__uint8_t"></a> <a id="structbtif__a2dp__sep__cfg__cb__t_1aa6156cff2e3f499a1e403a8dab6a7dc9"></a> uint8\_t data\_len
    :   data length of p\_data

    <a id="_CPPv4N22btif_a2dp_sep_cfg_cb_t6p_dataE"></a>

    <a id="_CPPv3N22btif_a2dp_sep_cfg_cb_t6p_dataE"></a> <a id="_CPPv2N22btif_a2dp_sep_cfg_cb_t6p_dataE"></a> <a id="btif_a2dp_sep_cfg_cb_t::p_data__uint8_tCP"></a> <a id="structbtif__a2dp__sep__cfg__cb__t_1aa65ed0f99e04ab9c12ea9bd64ebc5bce"></a> const uint8\_t \*p\_data
    :   configurtion data buffer

<a id="_CPPv417btif_a2dp_cp_cb_t"></a>

<a id="_CPPv317btif_a2dp_cp_cb_t"></a> <a id="_CPPv217btif_a2dp_cp_cb_t"></a> <a id="btif_a2dp_cp_cb_t"></a> <a id="structbtif__a2dp__cp__cb__t"></a> struct btif\_a2dp\_cp\_cb\_t
:   A2DP content protection data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N17btif_a2dp_cp_cb_t3hdrE"></a>

    <a id="_CPPv3N17btif_a2dp_cp_cb_t3hdrE"></a> <a id="_CPPv2N17btif_a2dp_cp_cb_t3hdrE"></a> <a id="btif_a2dp_cp_cb_t::hdr__btif_a2dp_cb_hdr_t"></a> <a id="structbtif__a2dp__cp__cb__t_1a657cf743ca7e50c5d69ee822e1943be2"></a> [btif\_a2dp\_cb\_hdr\_t](#_CPPv418btif_a2dp_cb_hdr_t "btif_a2dp_cb_hdr_t") hdr
    :   A2DP header data struct

    <a id="_CPPv4N17btif_a2dp_cp_cb_t9is_enableE"></a>

    <a id="_CPPv3N17btif_a2dp_cp_cb_t9is_enableE"></a> <a id="_CPPv2N17btif_a2dp_cp_cb_t9is_enableE"></a> <a id="btif_a2dp_cp_cb_t::is_enable__uint8_t"></a> <a id="structbtif__a2dp__cp__cb__t_1a8724f5140c983cc573dc4bee0379f9d0"></a> uint8\_t is\_enable
    :   value for enable or disable

    <a id="_CPPv4N17btif_a2dp_cp_cb_t7cp_typeE"></a>

    <a id="_CPPv3N17btif_a2dp_cp_cb_t7cp_typeE"></a> <a id="_CPPv2N17btif_a2dp_cp_cb_t7cp_typeE"></a> <a id="btif_a2dp_cp_cb_t::cp_type__uint16_t"></a> <a id="structbtif__a2dp__cp__cb__t_1a0b992a4d4d31f11210b5606617ffd9a4"></a> uint16\_t cp\_type
    :   content protection type @btif\_a2dp\_cp\_type\_t

    <a id="_CPPv4N17btif_a2dp_cp_cb_t8data_lenE"></a>

    <a id="_CPPv3N17btif_a2dp_cp_cb_t8data_lenE"></a> <a id="_CPPv2N17btif_a2dp_cp_cb_t8data_lenE"></a> <a id="btif_a2dp_cp_cb_t::data_len__uint8_t"></a> <a id="structbtif__a2dp__cp__cb__t_1aefedee61f86b4d697cba680ddcbaec5e"></a> uint8\_t data\_len
    :   data length of p\_data

    <a id="_CPPv4N17btif_a2dp_cp_cb_t6p_dataE"></a>

    <a id="_CPPv3N17btif_a2dp_cp_cb_t6p_dataE"></a> <a id="_CPPv2N17btif_a2dp_cp_cb_t6p_dataE"></a> <a id="btif_a2dp_cp_cb_t::p_data__uint8_tCP"></a> <a id="structbtif__a2dp__cp__cb__t_1a07897533d7f024511309c2f88b8a2e09"></a> const uint8\_t \*p\_data
    :   content protection data buffer

<a id="_CPPv422btif_a2dp_recover_cb_t"></a>

<a id="_CPPv322btif_a2dp_recover_cb_t"></a> <a id="_CPPv222btif_a2dp_recover_cb_t"></a> <a id="btif_a2dp_recover_cb_t"></a> <a id="structbtif__a2dp__recover__cb__t"></a> struct btif\_a2dp\_recover\_cb\_t
:   A2DP recover callback data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N22btif_a2dp_recover_cb_t3hdrE"></a>

    <a id="_CPPv3N22btif_a2dp_recover_cb_t3hdrE"></a> <a id="_CPPv2N22btif_a2dp_recover_cb_t3hdrE"></a> <a id="btif_a2dp_recover_cb_t::hdr__btif_a2dp_cb_hdr_t"></a> <a id="structbtif__a2dp__recover__cb__t_1a0b7993624c7d5f28d7ffac20d6251326"></a> [btif\_a2dp\_cb\_hdr\_t](#_CPPv418btif_a2dp_cb_hdr_t "btif_a2dp_cb_hdr_t") hdr
    :   A2DP header data struct

    <a id="_CPPv4N22btif_a2dp_recover_cb_t13active_deviceE"></a>

    <a id="_CPPv3N22btif_a2dp_recover_cb_t13active_deviceE"></a> <a id="_CPPv2N22btif_a2dp_recover_cb_t13active_deviceE"></a> <a id="btif_a2dp_recover_cb_t::active_device__b"></a> <a id="structbtif__a2dp__recover__cb__t_1a722694f2cad20501a3ade650edc599d4"></a> bool active\_device
    :   flag for playing music

<a id="_CPPv428btif_a2dp_snk_register_sep_t"></a>

<a id="_CPPv328btif_a2dp_snk_register_sep_t"></a> <a id="_CPPv228btif_a2dp_snk_register_sep_t"></a> <a id="btif_a2dp_snk_register_sep_t"></a> <a id="structbtif__a2dp__snk__register__sep__t"></a> struct btif\_a2dp\_snk\_register\_sep\_t
:   A2DP sink SEP setting data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N28btif_a2dp_snk_register_sep_t10media_typeE"></a>

    <a id="_CPPv3N28btif_a2dp_snk_register_sep_t10media_typeE"></a> <a id="_CPPv2N28btif_a2dp_snk_register_sep_t10media_typeE"></a> <a id="btif_a2dp_snk_register_sep_t::media_type__btif_a2dp_media_type_t"></a> <a id="structbtif__a2dp__snk__register__sep__t_1a26abc569f3dd5d0f7ebe564923fcbfe7"></a> [btif\_a2dp\_media\_type\_t](btif_type.md#_CPPv422btif_a2dp_media_type_t "btif_a2dp_media_type_t") media\_type
    :   medit type

    <a id="_CPPv4N28btif_a2dp_snk_register_sep_t10codec_typeE"></a>

    <a id="_CPPv3N28btif_a2dp_snk_register_sep_t10codec_typeE"></a> <a id="_CPPv2N28btif_a2dp_snk_register_sep_t10codec_typeE"></a> <a id="btif_a2dp_snk_register_sep_t::codec_type__btif_a2dp_codec_type_t"></a> <a id="structbtif__a2dp__snk__register__sep__t_1ac986d75110df7bb5010d2b7455ccb2ca"></a> [btif\_a2dp\_codec\_type\_t](btif_type.md#_CPPv422btif_a2dp_codec_type_t "btif_a2dp_codec_type_t") codec\_type
    :   codec type

    <a id="_CPPv4N28btif_a2dp_snk_register_sep_t13codec_cap_lenE"></a>

    <a id="_CPPv3N28btif_a2dp_snk_register_sep_t13codec_cap_lenE"></a> <a id="_CPPv2N28btif_a2dp_snk_register_sep_t13codec_cap_lenE"></a> <a id="btif_a2dp_snk_register_sep_t::codec_cap_len__uint16_t"></a> <a id="structbtif__a2dp__snk__register__sep__t_1afbb65628bd017a9275f9616f82ceb366"></a> uint16\_t codec\_cap\_len
    :   length of codec capability

    <a id="_CPPv4N28btif_a2dp_snk_register_sep_t11p_codec_capE"></a>

    <a id="_CPPv3N28btif_a2dp_snk_register_sep_t11p_codec_capE"></a> <a id="_CPPv2N28btif_a2dp_snk_register_sep_t11p_codec_capE"></a> <a id="btif_a2dp_snk_register_sep_t::p_codec_cap__uint8_tCP"></a> <a id="structbtif__a2dp__snk__register__sep__t_1a95ccb7409954ab526a434245ed727941"></a> const uint8\_t \*p\_codec\_cap
    :   data pointer for codec capability

    <a id="_CPPv4N28btif_a2dp_snk_register_sep_t7cp_typeE"></a>

    <a id="_CPPv3N28btif_a2dp_snk_register_sep_t7cp_typeE"></a> <a id="_CPPv2N28btif_a2dp_snk_register_sep_t7cp_typeE"></a> <a id="btif_a2dp_snk_register_sep_t::cp_type__btif_a2dp_cp_type_t"></a> <a id="structbtif__a2dp__snk__register__sep__t_1a30ceb288cc7b439bd3166f295d92fa9a"></a> [btif\_a2dp\_cp\_type\_t](btif_type.md#_CPPv419btif_a2dp_cp_type_t "btif_a2dp_cp_type_t") cp\_type
    :   content protection type

    <a id="_CPPv4N28btif_a2dp_snk_register_sep_t10cp_val_lenE"></a>

    <a id="_CPPv3N28btif_a2dp_snk_register_sep_t10cp_val_lenE"></a> <a id="_CPPv2N28btif_a2dp_snk_register_sep_t10cp_val_lenE"></a> <a id="btif_a2dp_snk_register_sep_t::cp_val_len__uint16_t"></a> <a id="structbtif__a2dp__snk__register__sep__t_1a0dec5182da14673bf60cc88446a2511b"></a> uint16\_t cp\_val\_len
    :   content protection value length

    <a id="_CPPv4N28btif_a2dp_snk_register_sep_t8p_cp_valE"></a>

    <a id="_CPPv3N28btif_a2dp_snk_register_sep_t8p_cp_valE"></a> <a id="_CPPv2N28btif_a2dp_snk_register_sep_t8p_cp_valE"></a> <a id="btif_a2dp_snk_register_sep_t::p_cp_val__uint8_tCP"></a> <a id="structbtif__a2dp__snk__register__sep__t_1ae25f9f2e6067e1312046c2fa0c570c9f"></a> const uint8\_t \*p\_cp\_val
    :   data pointer for content protection value

<a id="_CPPv420btif_a2dp_register_t"></a>

<a id="_CPPv320btif_a2dp_register_t"></a> <a id="_CPPv220btif_a2dp_register_t"></a> <a id="btif_a2dp_register_t"></a> <a id="structbtif__a2dp__register__t"></a> struct btif\_a2dp\_register\_t
:   callback struct definition

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N20btif_a2dp_register_t9dlst_nodeE"></a>

    <a id="_CPPv3N20btif_a2dp_register_t9dlst_nodeE"></a> <a id="_CPPv2N20btif_a2dp_register_t9dlst_nodeE"></a> <a id="btif_a2dp_register_t::dlst_node__dl_list_t"></a> <a id="structbtif__a2dp__register__t_1ac6e0fa32fd297d94119295fabc68d688"></a> dl\_list\_t dlst\_node
    :   node for application handler will be linked to orthers

    <a id="_CPPv4N20btif_a2dp_register_t8callbackE"></a>

    <a id="_CPPv3N20btif_a2dp_register_t8callbackE"></a> <a id="_CPPv2N20btif_a2dp_register_t8callbackE"></a> <a id="btif_a2dp_register_t::callback__btif_a2dp_event_callback"></a> <a id="structbtif__a2dp__register__t_1ac2acd2aea74c37d88b89dbe765e76c19"></a> [btif\_a2dp\_event\_callback](btif_type.md#_CPPv424btif_a2dp_event_callback "btif_a2dp_event_callback") callback
    :   function pointer for callback function

<a id="macros"></a>

### Macros

<a id="c.BTIF_A2DP_EVT_SIG_CONNECT"></a>

<a id="a2dp__if_8h_1a5ad31ef8ff41fe976247888dac29fe75"></a> BTIF\_A2DP\_EVT\_SIG\_CONNECT
:   callback struct see @btif\_a2dp\_conn\_cb\_t

<a id="c.BTIF_A2DP_EVT_SIG_DISCONNECT"></a>

<a id="a2dp__if_8h_1ace14501e0c6e89f17c8297902b21081a"></a> BTIF\_A2DP\_EVT\_SIG\_DISCONNECT
:   callback struct see @btif\_a2dp\_conn\_cb\_t

<a id="c.BTIF_A2DP_EVT_MEDIA_CONNECT"></a>

<a id="a2dp__if_8h_1a7fcfb60ff19bd2ec5f9b006a53e5fcbf"></a> BTIF\_A2DP\_EVT\_MEDIA\_CONNECT
:   callback struct see @btif\_a2dp\_conn\_cb\_t

<a id="c.BTIF_A2DP_EVT_MEDIA_DISCONNECT"></a>

<a id="a2dp__if_8h_1a32e6d96bd00b3f2573ec0c5208620586"></a> BTIF\_A2DP\_EVT\_MEDIA\_DISCONNECT
:   callback struct see @btif\_a2dp\_conn\_cb\_t

<a id="c.BTIF_A2DP_EVT_SIG_DELAY_RPT_SUPP"></a>

<a id="a2dp__if_8h_1a7e412e5b0a64e953046889b8146e7619"></a> BTIF\_A2DP\_EVT\_SIG\_DELAY\_RPT\_SUPP
:   callback struct see @btif\_a2dp\_cb\_hdr\_t

<a id="c.BTIF_A2DP_EVT_SIG_DELAY_RPT_VAL_CHANGED"></a>

<a id="a2dp__if_8h_1acde4ac18f6c1ddba1f3c9daa17d9a19e"></a> BTIF\_A2DP\_EVT\_SIG\_DELAY\_RPT\_VAL\_CHANGED
:   callback struct see @ NULL

<a id="c.BTIF_A2DP_EVT_SIG_CP"></a>

<a id="a2dp__if_8h_1aa4ad0d4cddc0040c8fc45ded2fc4c563"></a> BTIF\_A2DP\_EVT\_SIG\_CP
:   callback struct see @btif\_a2dp\_cp\_cb\_t

<a id="c.BTIF_A2DP_EVT_SIG_SEC_CTRL"></a>

<a id="a2dp__if_8h_1afa643c96437d36f90f76a0b099d3dc8e"></a> BTIF\_A2DP\_EVT\_SIG\_SEC\_CTRL
:   callback struct see @btif\_a2dp\_sec\_ctrl\_cb\_t

<a id="c.BTIF_A2DP_EVT_MEDIA_CODEC_CFG"></a>

<a id="a2dp__if_8h_1a0aa2b4ea13fb8888ada91a17e5308bd2"></a> BTIF\_A2DP\_EVT\_MEDIA\_CODEC\_CFG
:   callback struct see @btif\_a2dp\_sep\_cfg\_cb\_t

<a id="c.BTIF_A2DP_EVT_STREAM_START"></a>

<a id="a2dp__if_8h_1a347bff019f12daf06cb9ce630dedec1e"></a> BTIF\_A2DP\_EVT\_STREAM\_START
:   callback struct see @btif\_a2dp\_cb\_hdr\_t

<a id="c.BTIF_A2DP_EVT_STREAM_SUSPEND"></a>

<a id="a2dp__if_8h_1af060ab957a61a2a1afdc988738fd5106"></a> BTIF\_A2DP\_EVT\_STREAM\_SUSPEND
:   callback struct see @btif\_a2dp\_cb\_hdr\_t

<a id="c.BTIF_A2DP_EVT_RECOVER_START"></a>

<a id="a2dp__if_8h_1afadcbb84dcf64dd509649ba035e209b9"></a> BTIF\_A2DP\_EVT\_RECOVER\_START
:   callback struct see @btif\_a2dp\_cb\_hdr\_t

<a id="c.BTIF_A2DP_EVT_RECOVER_DONE"></a>

<a id="a2dp__if_8h_1a0c1009e0f6d0fa973f009afe000107b2"></a> BTIF\_A2DP\_EVT\_RECOVER\_DONE
:   callback struct see @btif\_a2dp\_recover\_cb\_t

<a id="c.BTIF_A2DP_EVT_MEDIA_DATA"></a>

<a id="a2dp__if_8h_1a316795ab68ddf4d185bbf8e66f2dd9af"></a> BTIF\_A2DP\_EVT\_MEDIA\_DATA
:   callback struct see @btif\_a2dp\_media\_data\_cb\_t

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv415btif_a2dp_evt_t"></a>

<a id="_CPPv315btif_a2dp_evt_t"></a> <a id="_CPPv215btif_a2dp_evt_t"></a> <a id="btif_a2dp_evt_t"></a> <a id="a2dp__if_8h_1aaed8076fb9cc872797fa2639da1bb803"></a> typedef uint8\_t btif\_a2dp\_evt\_t
