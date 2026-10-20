---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/btif/gatt_if.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="gatt-interface-functions"></a>

# GATT Interface Functions

<a id="gatt-if-api-brief"></a>

## GATT\_IF API Brief

| Application | Brief |
| --- | --- |
| [`btif_gatts_attr_read_included()`](#_CPPv429btif_gatts_attr_read_includedP20btif_att_chan_info_tPKvP7uint8_t8uint16_t8uint16_t8uint16_t "btif_gatts_attr_read_included") | read GATT service include information |
| [`btif_gatt_server_rd_service()`](#_CPPv427btif_gatt_server_rd_serviceP20btif_att_chan_info_tPKvP7uint8_t8uint16_t8uint16_t8uint16_t "btif_gatt_server_rd_service") | read GATT service data |
| [`btif_gatt_server_rd_characters()`](#_CPPv430btif_gatt_server_rd_charactersP20btif_att_chan_info_tPKvP7uint8_t8uint16_t8uint16_t8uint16_t "btif_gatt_server_rd_characters") | read GATT characters data |
| [`btif_gatt_server_register_service()`](#_CPPv433btif_gatt_server_register_serviceP19btif_gatt_service_t "btif_gatt_server_register_service") | register a GATT service |
| [`btif_gatt_server_unregister_service()`](#_CPPv435btif_gatt_server_unregister_serviceP19btif_gatt_service_t "btif_gatt_server_unregister_service") | unregister a GATT service |
| [`btif_gatt_server_send_notify()`](#_CPPv428btif_gatt_server_send_notify8uint16_tP15btif_gatt_nty_t "btif_gatt_server_send_notify") | GATT server send notify |
| [`btif_gatt_server_send_indicate()`](#_CPPv430btif_gatt_server_send_indicate8uint16_tP15btif_gatt_ind_t "btif_gatt_server_send_indicate") | GATT server send indicate |
| [`btif_gatt_server_read_attr()`](#_CPPv426btif_gatt_server_read_attrP7uint8_t8uint16_tP7uint8_t8uint16_t8uint16_t "btif_gatt_server_read_attr") | read GATT server specific attribute data |

<a id="gatt-if-api-reference"></a>

## GATT\_IF API Reference

<a id="header-file"></a>

### Header File

- [btif/inc/gatt\_if.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/btif/inc/gatt_if.h)

<a id="functions"></a>

### Functions

<a id="_CPPv429btif_gatts_attr_read_includedP20btif_att_chan_info_tPKvP7uint8_t8uint16_t8uint16_t8uint16_t"></a>

<a id="_CPPv329btif_gatts_attr_read_includedP20btif_att_chan_info_tPKvP7uint8_t8uint16_t8uint16_t8uint16_t"></a> <a id="_CPPv229btif_gatts_attr_read_includedP20btif_att_chan_info_tPKvP7uint8_t8uint16_t8uint16_t8uint16_t"></a> <a id="btif_gatts_attr_read_included__btif_att_chan_info_tP.voidCP.uint8_tP.uint16_t.uint16_t.uint16_t"></a> <a id="gatt__if_8h_1a6b2b8b073fe390ef2732b2f01d062792"></a> int16\_t btif\_gatts\_attr\_read\_included([btif\_att\_chan\_info\_t](#_CPPv420btif_att_chan_info_t "btif_att_chan_info_t") \*p\_att\_chan, const void \*p\_attr, uint8\_t \*p\_buf, uint16\_t len, uint16\_t offset, uint16\_t svs\_end\_handle)
:   btif\_gatts\_attr\_read\_included brief description

    read GATT service include information

    参数:
    :   - **p\_att\_chan** – **\[in\]** ATT L2CAP channel information struct
        - **p\_attr** – **\[in\]** buffer for GATT service include information
        - **p\_buf** – **\[out\]** buffer data for read result
        - **len** – **\[in\]** data length of p\_buf try to get
        - **offset** – **\[in\]** offset for p\_attr
        - **svs\_end\_handle** – **\[in\]** service end index

    返回值:
    :   - **\>** – 0 data length
        - **other** – error index (0 \- @ERR\_INVALID\_OFFSET)

    返回:
    :   read length or error index

<a id="_CPPv427btif_gatt_server_rd_serviceP20btif_att_chan_info_tPKvP7uint8_t8uint16_t8uint16_t8uint16_t"></a>

<a id="_CPPv327btif_gatt_server_rd_serviceP20btif_att_chan_info_tPKvP7uint8_t8uint16_t8uint16_t8uint16_t"></a> <a id="_CPPv227btif_gatt_server_rd_serviceP20btif_att_chan_info_tPKvP7uint8_t8uint16_t8uint16_t8uint16_t"></a> <a id="btif_gatt_server_rd_service__btif_att_chan_info_tP.voidCP.uint8_tP.uint16_t.uint16_t.uint16_t"></a> <a id="gatt__if_8h_1a6c5e49795ba0c4a7e5397226812494c5"></a> int16\_t btif\_gatt\_server\_rd\_service([btif\_att\_chan\_info\_t](#_CPPv420btif_att_chan_info_t "btif_att_chan_info_t") \*p\_att\_chan, const void \*p\_attr, uint8\_t \*buf, uint16\_t len, uint16\_t offset, uint16\_t svs\_end\_handle)
:   btif\_gatt\_server\_rd\_service brief description

    read GATT service data

    参数:
    :   - **p\_att\_chan** – **\[in\]** ATT L2CAP channel information struct
        - **p\_attr** – **\[in\]** buffer for GATT service data
        - **buf** – **\[out\]** buffer data for read result
        - **len** – **\[in\]** data length of p\_buf try to get
        - **offset** – **\[in\]** offset for p\_attr
        - **svs\_end\_handle** – **\[in\]** service end index

    返回值:
    :   - **\>** – 0 data length
        - **other** – error index (0 \- @ERR\_INVALID\_OFFSET)

    返回:
    :   read length or error index

<a id="_CPPv430btif_gatt_server_rd_charactersP20btif_att_chan_info_tPKvP7uint8_t8uint16_t8uint16_t8uint16_t"></a>

<a id="_CPPv330btif_gatt_server_rd_charactersP20btif_att_chan_info_tPKvP7uint8_t8uint16_t8uint16_t8uint16_t"></a> <a id="_CPPv230btif_gatt_server_rd_charactersP20btif_att_chan_info_tPKvP7uint8_t8uint16_t8uint16_t8uint16_t"></a> <a id="btif_gatt_server_rd_characters__btif_att_chan_info_tP.voidCP.uint8_tP.uint16_t.uint16_t.uint16_t"></a> <a id="gatt__if_8h_1ad485d880cd338124f898631bff077645"></a> int16\_t btif\_gatt\_server\_rd\_characters([btif\_att\_chan\_info\_t](#_CPPv420btif_att_chan_info_t "btif_att_chan_info_t") \*p\_att\_chan, const void \*p\_attr, uint8\_t \*buf, uint16\_t len, uint16\_t offset, uint16\_t svs\_end\_handle)
:   btif\_gatt\_server\_rd\_characters brief description

    read GATT characters data

    参数:
    :   - **p\_att\_chan** – **\[in\]** ATT L2CAP channel information struct
        - **p\_attr** – **\[in\]** buffer for GATT characters data
        - **buf** – **\[out\]** buffer data for read result
        - **len** – **\[in\]** data length of p\_buf try to get
        - **offset** – **\[in\]** offset for p\_attr
        - **svs\_end\_handle** – **\[in\]** service end index

    返回值:
    :   - **\>** – 0 data length
        - **other** – error index (0 \- @ERR\_INVALID\_OFFSET)

    返回:
    :   read length or error index

<a id="_CPPv433btif_gatt_server_register_serviceP19btif_gatt_service_t"></a>

<a id="_CPPv333btif_gatt_server_register_serviceP19btif_gatt_service_t"></a> <a id="_CPPv233btif_gatt_server_register_serviceP19btif_gatt_service_t"></a> <a id="btif_gatt_server_register_service__btif_gatt_service_tP"></a> <a id="gatt__if_8h_1ab7023cdc755ac3a61d0cbae6153cba20"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") btif\_gatt\_server\_register\_service([btif\_gatt\_service\_t](#_CPPv419btif_gatt_service_t "btif_gatt_service_t") \*p\_service)
:   btif\_gatt\_server\_register\_service brief description

    register a GATT service

    参数:
    :   **p\_service** – **\[in\]** GATT service data struct

    返回值:
    :   - **0** – success
        - **-1** – fail

    返回:
    :   result

<a id="_CPPv435btif_gatt_server_unregister_serviceP19btif_gatt_service_t"></a>

<a id="_CPPv335btif_gatt_server_unregister_serviceP19btif_gatt_service_t"></a> <a id="_CPPv235btif_gatt_server_unregister_serviceP19btif_gatt_service_t"></a> <a id="btif_gatt_server_unregister_service__btif_gatt_service_tP"></a> <a id="gatt__if_8h_1a9d9bfb9ffc69767279eb3a94aedf7c07"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") btif\_gatt\_server\_unregister\_service([btif\_gatt\_service\_t](#_CPPv419btif_gatt_service_t "btif_gatt_service_t") \*p\_service)
:   btif\_gatt\_server\_unregister\_service brief description

    unregister a GATT service

    参数:
    :   **p\_service** – **\[in\]** GATT service data struct

    返回值:
    :   - **0** – success
        - **-1** – fail

    返回:
    :   result

<a id="_CPPv428btif_gatt_server_send_notify8uint16_tP15btif_gatt_nty_t"></a>

<a id="_CPPv328btif_gatt_server_send_notify8uint16_tP15btif_gatt_nty_t"></a> <a id="_CPPv228btif_gatt_server_send_notify8uint16_tP15btif_gatt_nty_t"></a> <a id="btif_gatt_server_send_notify__uint16_t.btif_gatt_nty_tP"></a> <a id="gatt__if_8h_1afea2b8520bf697f96af04c6220dc7c3a"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") btif\_gatt\_server\_send\_notify(uint16\_t hci\_handle, [btif\_gatt\_nty\_t](#_CPPv415btif_gatt_nty_t "btif_gatt_nty_t") \*p\_para)
:   btif\_gatt\_server\_send\_notify brief description

    GATT server send notify

    参数:
    :   - **hci\_handle** – **\[in\]** connection handle
        - **p\_para** – **\[in\]** GATT notify strcut

    返回值:
    :   - **0** – success
        - **-1** – fail

    返回:
    :   result

<a id="_CPPv430btif_gatt_server_send_indicate8uint16_tP15btif_gatt_ind_t"></a>

<a id="_CPPv330btif_gatt_server_send_indicate8uint16_tP15btif_gatt_ind_t"></a> <a id="_CPPv230btif_gatt_server_send_indicate8uint16_tP15btif_gatt_ind_t"></a> <a id="btif_gatt_server_send_indicate__uint16_t.btif_gatt_ind_tP"></a> <a id="gatt__if_8h_1afb29e50e4cb8e7f20d366dc6819d1d7d"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") btif\_gatt\_server\_send\_indicate(uint16\_t hci\_handle, [btif\_gatt\_ind\_t](#_CPPv415btif_gatt_ind_t "btif_gatt_ind_t") \*p\_para)
:   btif\_gatt\_server\_send\_indicate brief description

    GATT server send indicate

    参数:
    :   - **hci\_handle** – **\[in\]** connection handle
        - **p\_para** – **\[in\]** GATT indicate strcut

    返回值:
    :   - **0** – success
        - **-1** – fail

    返回:
    :   result

<a id="_CPPv426btif_gatt_server_read_attrP7uint8_t8uint16_tP7uint8_t8uint16_t8uint16_t"></a>

<a id="_CPPv326btif_gatt_server_read_attrP7uint8_t8uint16_tP7uint8_t8uint16_t8uint16_t"></a> <a id="_CPPv226btif_gatt_server_read_attrP7uint8_t8uint16_tP7uint8_t8uint16_t8uint16_t"></a> <a id="btif_gatt_server_read_attr__uint8_tP.uint16_t.uint8_tP.uint16_t.uint16_t"></a> <a id="gatt__if_8h_1a8a64330f1e344afb55c669999d1950ee"></a> int16\_t btif\_gatt\_server\_read\_attr(uint8\_t \*p\_dst\_buf, uint16\_t dst\_len, uint8\_t \*p\_src\_buf, uint16\_t src\_len, uint16\_t rd\_offset)
:   btif\_gatt\_server\_read\_attr brief description

    read GATT server specific attribute data

    参数:
    :   - **p\_dst\_buf** – **\[out\]** buffer for destination data
        - **dst\_len** – **\[in\]** destination data length
        - **p\_src\_buf** – **\[in\]** buffer for source data
        - **src\_len** – **\[in\]** source data length
        - **rd\_offset** – **\[in\]** read offset for source data

    返回值:
    :   - **\>** – 0 data length
        - **other** – error index (0 \- @ERR\_INVALID\_OFFSET)

    返回:
    :   read length or error index

<a id="structures"></a>

### Structures

<a id="_CPPv420btif_att_chan_info_t"></a>

<a id="_CPPv320btif_att_chan_info_t"></a> <a id="_CPPv220btif_att_chan_info_t"></a> <a id="btif_att_chan_info_t"></a> <a id="structbtif__att__chan__info__t"></a> struct btif\_att\_chan\_info\_t
:   ATT channel information struct.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N20btif_att_chan_info_t6handleE"></a>

    <a id="_CPPv3N20btif_att_chan_info_t6handleE"></a> <a id="_CPPv2N20btif_att_chan_info_t6handleE"></a> <a id="btif_att_chan_info_t::handle__uint16_t"></a> <a id="structbtif__att__chan__info__t_1ad1ca90b7b6cc257390e0a4c86483ebb9"></a> uint16\_t handle
    :   connection handle

    <a id="_CPPv4N20btif_att_chan_info_t11remote_addrE"></a>

    <a id="_CPPv3N20btif_att_chan_info_t11remote_addrE"></a> <a id="_CPPv2N20btif_att_chan_info_t11remote_addrE"></a> <a id="btif_att_chan_info_t::remote_addr__btif_le_bd_addr_t"></a> <a id="structbtif__att__chan__info__t_1a7f3ef25101c3e208ade98a514ad4cf14"></a> [btif\_le\_bd\_addr\_t](btif_type.md#_CPPv417btif_le_bd_addr_t "btif_le_bd_addr_t") remote\_addr
    :   remote BT address

    <a id="_CPPv4N20btif_att_chan_info_t6tx_mtuE"></a>

    <a id="_CPPv3N20btif_att_chan_info_t6tx_mtuE"></a> <a id="_CPPv2N20btif_att_chan_info_t6tx_mtuE"></a> <a id="btif_att_chan_info_t::tx_mtu__uint16_t"></a> <a id="structbtif__att__chan__info__t_1aa5d7e1841833143242cc9f1d14431dbe"></a> uint16\_t tx\_mtu
    :   TX MTU size

    <a id="_CPPv4N20btif_att_chan_info_t6rx_mtuE"></a>

    <a id="_CPPv3N20btif_att_chan_info_t6rx_mtuE"></a> <a id="_CPPv2N20btif_att_chan_info_t6rx_mtuE"></a> <a id="btif_att_chan_info_t::rx_mtu__uint16_t"></a> <a id="structbtif__att__chan__info__t_1a45ef66e8ccf39aec45365272ce7f79cc"></a> uint16\_t rx\_mtu
    :   RX MTU size

<a id="_CPPv417btif_attr_const_t"></a>

<a id="_CPPv317btif_attr_const_t"></a> <a id="_CPPv217btif_attr_const_t"></a> <a id="btif_attr_const_t"></a> <a id="structbtif__attr__const__t"></a> struct btif\_attr\_const\_t
:   GATT attribute configured data struct.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N17btif_attr_const_t6p_uuidE"></a>

    <a id="_CPPv3N17btif_attr_const_t6p_uuidE"></a> <a id="_CPPv2N17btif_attr_const_t6p_uuidE"></a> <a id="btif_attr_const_t::p_uuid__btif_uuid_tP"></a> <a id="structbtif__attr__const__t_1adf544f2ec80247eba625d332a42b8f5a"></a> [btif\_uuid\_t](btif_type.md#_CPPv411btif_uuid_t "btif_uuid_t") \*p\_uuid
    :   UUID value

    <a id="_CPPv4N17btif_attr_const_t6p_readE"></a>

    <a id="_CPPv3N17btif_attr_const_t6p_readE"></a> <a id="_CPPv2N17btif_attr_const_t6p_readE"></a> <a id="btif_attr_const_t::p_read__btif_att_read_fp"></a> <a id="structbtif__attr__const__t_1a2b7a9c072104f94b70e9c175efcfd378"></a> [btif\_att\_read\_fp](#_CPPv416btif_att_read_fp "btif_att_read_fp") p\_read
    :   callback function for ATT read command

    <a id="_CPPv4N17btif_attr_const_t7p_writeE"></a>

    <a id="_CPPv3N17btif_attr_const_t7p_writeE"></a> <a id="_CPPv2N17btif_attr_const_t7p_writeE"></a> <a id="btif_attr_const_t::p_write__btif_att_write_fp"></a> <a id="structbtif__attr__const__t_1af22212dd7608a2ed5cc4b6eb1f0655ac"></a> [btif\_att\_write\_fp](#_CPPv417btif_att_write_fp "btif_att_write_fp") p\_write
    :   callback function for ATT write command

    <a id="_CPPv4N17btif_attr_const_t10permissionE"></a>

    <a id="_CPPv3N17btif_attr_const_t10permissionE"></a> <a id="_CPPv2N17btif_attr_const_t10permissionE"></a> <a id="btif_attr_const_t::permission__uint8_t"></a> <a id="structbtif__attr__const__t_1aee17e106241dfe30192ccb2ae73fa28c"></a> uint8\_t permission
    :   permission setting for attribute

<a id="_CPPv411btif_attr_t"></a>

<a id="_CPPv311btif_attr_t"></a> <a id="_CPPv211btif_attr_t"></a> <a id="btif_attr_t"></a> <a id="structbtif__attr__t"></a> struct btif\_attr\_t
:   GATT attribute data struct.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N11btif_attr_t12p_const_attrE"></a>

    <a id="_CPPv3N11btif_attr_t12p_const_attrE"></a> <a id="_CPPv2N11btif_attr_t12p_const_attrE"></a> <a id="btif_attr_t::p_const_attr__btif_attr_const_tCP"></a> <a id="structbtif__attr__t_1a79555619c98771190dd536926981bfdb"></a> const [btif\_attr\_const\_t](#_CPPv417btif_attr_const_t "btif_attr_const_t") \*p\_const\_attr
    :   attribute configured data

    <a id="_CPPv4N11btif_attr_t11p_user_dataE"></a>

    <a id="_CPPv3N11btif_attr_t11p_user_dataE"></a> <a id="_CPPv2N11btif_attr_t11p_user_dataE"></a> <a id="btif_attr_t::p_user_data__voidP"></a> <a id="structbtif__attr__t_1a7f99c9d691ef9b36a8bdd20903222818"></a> void \*p\_user\_data
    :   data buffer for attribute user defined

    <a id="_CPPv4N11btif_attr_t11attr_handleE"></a>

    <a id="_CPPv3N11btif_attr_t11attr_handleE"></a> <a id="_CPPv2N11btif_attr_t11attr_handleE"></a> <a id="btif_attr_t::attr_handle__uint16_t"></a> <a id="structbtif__attr__t_1a5d4ee80e6e89c3eb45bc3336b0db7f5b"></a> uint16\_t attr\_handle
    :   attribute handle index

<a id="_CPPv415btif_gatt_ind_t"></a>

<a id="_CPPv315btif_gatt_ind_t"></a> <a id="_CPPv215btif_gatt_ind_t"></a> <a id="btif_gatt_ind_t"></a> <a id="structbtif__gatt__ind__t"></a> struct btif\_gatt\_ind\_t
:   GATT indicate data struct.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N15btif_gatt_ind_t6p_attrE"></a>

    <a id="_CPPv3N15btif_gatt_ind_t6p_attrE"></a> <a id="_CPPv2N15btif_gatt_ind_t6p_attrE"></a> <a id="btif_gatt_ind_t::p_attr__btif_attr_tCP"></a> <a id="structbtif__gatt__ind__t_1a0795719107fed7167df2ff6dc2df89a9"></a> const [btif\_attr\_t](#_CPPv411btif_attr_t "btif_attr_t") \*p\_attr
    :   GATT attribute information

    <a id="_CPPv4N15btif_gatt_ind_t4funcE"></a>

    <a id="_CPPv3N15btif_gatt_ind_t4funcE"></a> <a id="_CPPv2N15btif_gatt_ind_t4funcE"></a> <a id="btif_gatt_ind_t::func__btif_att_indicate_cb_fp"></a> <a id="structbtif__gatt__ind__t_1a18705dd6480143ddb4c1414ecbb9b37c"></a> [btif\_att\_indicate\_cb\_fp](#_CPPv423btif_att_indicate_cb_fp "btif_att_indicate_cb_fp") func
    :   indicate done callback function

    <a id="_CPPv4N15btif_gatt_ind_t6p_dataE"></a>

    <a id="_CPPv3N15btif_gatt_ind_t6p_dataE"></a> <a id="_CPPv2N15btif_gatt_ind_t6p_dataE"></a> <a id="btif_gatt_ind_t::p_data__voidCP"></a> <a id="structbtif__gatt__ind__t_1ad7cde96f96f66817fe0739ac41959dfc"></a> const void \*p\_data
    :   data buffer will be sent

    <a id="_CPPv4N15btif_gatt_ind_t3lenE"></a>

    <a id="_CPPv3N15btif_gatt_ind_t3lenE"></a> <a id="_CPPv2N15btif_gatt_ind_t3lenE"></a> <a id="btif_gatt_ind_t::len__uint16_t"></a> <a id="structbtif__gatt__ind__t_1ae48a7944e073231797e8360dc80d7cd7"></a> uint16\_t len
    :   data length of p\_data

    <a id="_CPPv4N15btif_gatt_ind_t11p_user_dataE"></a>

    <a id="_CPPv3N15btif_gatt_ind_t11p_user_dataE"></a> <a id="_CPPv2N15btif_gatt_ind_t11p_user_dataE"></a> <a id="btif_gatt_ind_t::p_user_data__voidP"></a> <a id="structbtif__gatt__ind__t_1a448f7e29ec19ecddd3c377c731395843"></a> void \*p\_user\_data
    :   data buffer for user data

<a id="_CPPv415btif_gatt_nty_t"></a>

<a id="_CPPv315btif_gatt_nty_t"></a> <a id="_CPPv215btif_gatt_nty_t"></a> <a id="btif_gatt_nty_t"></a> <a id="structbtif__gatt__nty__t"></a> struct btif\_gatt\_nty\_t
:   GATT notify data struct.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N15btif_gatt_nty_t6p_attrE"></a>

    <a id="_CPPv3N15btif_gatt_nty_t6p_attrE"></a> <a id="_CPPv2N15btif_gatt_nty_t6p_attrE"></a> <a id="btif_gatt_nty_t::p_attr__btif_attr_tCP"></a> <a id="structbtif__gatt__nty__t_1a88c87579a9305f185a67fe1514810105"></a> const [btif\_attr\_t](#_CPPv411btif_attr_t "btif_attr_t") \*p\_attr
    :   GATT attribute information

    <a id="_CPPv4N15btif_gatt_nty_t6p_dataE"></a>

    <a id="_CPPv3N15btif_gatt_nty_t6p_dataE"></a> <a id="_CPPv2N15btif_gatt_nty_t6p_dataE"></a> <a id="btif_gatt_nty_t::p_data__voidCP"></a> <a id="structbtif__gatt__nty__t_1a93e00158dab4ae22cb1712698595fa25"></a> const void \*p\_data
    :   data buffer will be sent

    <a id="_CPPv4N15btif_gatt_nty_t3lenE"></a>

    <a id="_CPPv3N15btif_gatt_nty_t3lenE"></a> <a id="_CPPv2N15btif_gatt_nty_t3lenE"></a> <a id="btif_gatt_nty_t::len__uint16_t"></a> <a id="structbtif__gatt__nty__t_1ad9e53c380eb9b6846813761b3848336a"></a> uint16\_t len
    :   data length of p\_data

    <a id="_CPPv4N15btif_gatt_nty_t5tx_cbE"></a>

    <a id="_CPPv3N15btif_gatt_nty_t5tx_cbE"></a> <a id="_CPPv2N15btif_gatt_nty_t5tx_cbE"></a> <a id="btif_gatt_nty_t::tx_cb__btif_att_tx_cb_fp"></a> <a id="structbtif__gatt__nty__t_1a8e14e83347f5a4ec96c01eeae12082ab"></a> [btif\_att\_tx\_cb\_fp](#_CPPv417btif_att_tx_cb_fp "btif_att_tx_cb_fp") tx\_cb
    :   notify done callback function

<a id="_CPPv419btif_gatt_service_t"></a>

<a id="_CPPv319btif_gatt_service_t"></a> <a id="_CPPv219btif_gatt_service_t"></a> <a id="btif_gatt_service_t"></a> <a id="structbtif__gatt__service__t"></a> struct btif\_gatt\_service\_t
:   GATT service information struct.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N19btif_gatt_service_t9dlst_nodeE"></a>

    <a id="_CPPv3N19btif_gatt_service_t9dlst_nodeE"></a> <a id="_CPPv2N19btif_gatt_service_t9dlst_nodeE"></a> <a id="btif_gatt_service_t::dlst_node__dl_list_t"></a> <a id="structbtif__gatt__service__t_1a9ac0de6b146d1483b71c65e2b594ade8"></a> dl\_list\_t dlst\_node
    :   node for application handler will be linked to orthers

    <a id="_CPPv4N19btif_gatt_service_t14svs_end_handleE"></a>

    <a id="_CPPv3N19btif_gatt_service_t14svs_end_handleE"></a> <a id="_CPPv2N19btif_gatt_service_t14svs_end_handleE"></a> <a id="btif_gatt_service_t::svs_end_handle__uint16_t"></a> <a id="structbtif__gatt__service__t_1af7f19ce17056c7a474186ffe97c585e6"></a> uint16\_t svs\_end\_handle
    :   service handle end value

    <a id="_CPPv4N19btif_gatt_service_t6p_attrE"></a>

    <a id="_CPPv3N19btif_gatt_service_t6p_attrE"></a> <a id="_CPPv2N19btif_gatt_service_t6p_attrE"></a> <a id="btif_gatt_service_t::p_attr__btif_attr_tP"></a> <a id="structbtif__gatt__service__t_1a075260ff334e874d7fb41af9bbf530d9"></a> [btif\_attr\_t](#_CPPv411btif_attr_t "btif_attr_t") \*p\_attr
    :   service attribute struct

    <a id="_CPPv4N19btif_gatt_service_t10attr_countE"></a>

    <a id="_CPPv3N19btif_gatt_service_t10attr_countE"></a> <a id="_CPPv2N19btif_gatt_service_t10attr_countE"></a> <a id="btif_gatt_service_t::attr_count__uint8_t"></a> <a id="structbtif__gatt__service__t_1a54aba09e82859632af65a112142dcbf0"></a> uint8\_t attr\_count
    :   attribute count

<a id="_CPPv418btif_gatt_charac_t"></a>

<a id="_CPPv318btif_gatt_charac_t"></a> <a id="_CPPv218btif_gatt_charac_t"></a> <a id="btif_gatt_charac_t"></a> <a id="structbtif__gatt__charac__t"></a> struct btif\_gatt\_charac\_t
:   GATT character information struct.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18btif_gatt_charac_t6p_uuidE"></a>

    <a id="_CPPv3N18btif_gatt_charac_t6p_uuidE"></a> <a id="_CPPv2N18btif_gatt_charac_t6p_uuidE"></a> <a id="btif_gatt_charac_t::p_uuid__btif_uuid_tP"></a> <a id="structbtif__gatt__charac__t_1ae55c69cc2ed193eb1460e82275350959"></a> [btif\_uuid\_t](btif_type.md#_CPPv411btif_uuid_t "btif_uuid_t") \*p\_uuid
    :   character’s UUID

    <a id="_CPPv4N18btif_gatt_charac_t12value_handleE"></a>

    <a id="_CPPv3N18btif_gatt_charac_t12value_handleE"></a> <a id="_CPPv2N18btif_gatt_charac_t12value_handleE"></a> <a id="btif_gatt_charac_t::value_handle__uint16_t"></a> <a id="structbtif__gatt__charac__t_1a1ebb7a9a6e42c562e4073aa2a5200541"></a> uint16\_t value\_handle
    :   handel index

    <a id="_CPPv4N18btif_gatt_charac_t10propertiesE"></a>

    <a id="_CPPv3N18btif_gatt_charac_t10propertiesE"></a> <a id="_CPPv2N18btif_gatt_charac_t10propertiesE"></a> <a id="btif_gatt_charac_t::properties__uint8_t"></a> <a id="structbtif__gatt__charac__t_1a48449226331a93bf2c13e11caee0d25a"></a> uint8\_t properties
    :   character properties

<a id="macros"></a>

### Macros

<a id="c.BTIF_GATT_CCC_NTF"></a>

<a id="gatt__if_8h_1a2b519b2f90e0afc1bfea1fbd0e271d36"></a> BTIF\_GATT\_CCC\_NTF

<a id="c.BTIF_GATT_CCC_IND"></a>

<a id="gatt__if_8h_1a83522a1694f66a74eed798d58b0a4b8f"></a> BTIF\_GATT\_CCC\_IND

<a id="c.BTIF_GATT_ERR"></a>

<a id="gatt__if_8h_1ab1c469c7ef3380401d621629b586478a"></a> BTIF\_GATT\_ERR(att\_err)

<a id="c.BTIF_UUID_GATT_PRIMARY"></a>

<a id="gatt__if_8h_1a2fc315f594b5f37554daf2e6fe27ea88"></a> BTIF\_UUID\_GATT\_PRIMARY

<a id="c.BTIF_UUID_GATT_SECONDARY"></a>

<a id="gatt__if_8h_1a04d7d538d8fe7c83c3d6ae0f6fe04949"></a> BTIF\_UUID\_GATT\_SECONDARY

<a id="c.BTIF_UUID_GATT_INCLUDE"></a>

<a id="gatt__if_8h_1a78d9471f82cec521f8b859a0f9274d34"></a> BTIF\_UUID\_GATT\_INCLUDE

<a id="c.BTIF_UUID_GATT_CHRC"></a>

<a id="gatt__if_8h_1af03c32ec0fad5318ae8068ebd550b6da"></a> BTIF\_UUID\_GATT\_CHRC

<a id="c.BTIF_UUID_GATT_CCC"></a>

<a id="gatt__if_8h_1ae112c4471fec9ba645db54a3692decdd"></a> BTIF\_UUID\_GATT\_CCC

<a id="c.BTIF_UUID_GATT_CPF"></a>

<a id="gatt__if_8h_1ad9d1b01b8290acb752dd285bd7fa9013"></a> BTIF\_UUID\_GATT\_CPF

<a id="c.BTIF_GATT_CHARAC_INIT"></a>

<a id="gatt__if_8h_1a244227c1d889ae84d0acfd87edd058ec"></a> BTIF\_GATT\_CHARAC\_INIT(\_uuid, \_props)

<a id="c.BTIF_CONST_ATTR"></a>

<a id="gatt__if_8h_1a1edd79f0c2cd597755470530eca1c233"></a> BTIF\_CONST\_ATTR(\_uuid, \_perm, \_read, \_write)

<a id="c.BTIF_GATT_ATTRIBUTE"></a>

<a id="gatt__if_8h_1a7bb4c758397bdc257e82d2ecef022b5e"></a> BTIF\_GATT\_ATTRIBUTE(\_uuid, \_perm, \_read, \_write, \_p\_user\_data, \_att\_handle)

<a id="c.BTIF_GATT_PRIMARY_SERVICE"></a>

<a id="gatt__if_8h_1a0c53ccbeba45b1a0995f22e5f2591f73"></a> BTIF\_GATT\_PRIMARY\_SERVICE(\_service)

<a id="c.BTIF_GATT_SECONDARY_SERVICE"></a>

<a id="gatt__if_8h_1a205396426549e95477823f82b1391e61"></a> BTIF\_GATT\_SECONDARY\_SERVICE(\_service)

<a id="c.BTIF_GATT_CHARACTERISTIC"></a>

<a id="gatt__if_8h_1ab3422678e3b4277d1afc10e90c158dae"></a> BTIF\_GATT\_CHARACTERISTIC(\_uuid, \_props, \_perm, \_read, \_write, \_user\_data)

<a id="c.BTIF_GATT_DESCRIPTOR"></a>

<a id="gatt__if_8h_1a73a6dd43b9efd5a56d826d2f3c260ad5"></a> BTIF\_GATT\_DESCRIPTOR(\_uuid, \_perm, \_read, \_write, \_user\_data)

<a id="c.BTIF_GATT_INCLUDE_SERVICE"></a>

<a id="gatt__if_8h_1aefe76ae56efce08cd878957c41272dc1"></a> BTIF\_GATT\_INCLUDE\_SERVICE(\_service\_incl)

<a id="c.BTIF_GATT_CCC"></a>

<a id="gatt__if_8h_1adc76c0dc8ea690c23246e0b333f15492"></a> BTIF\_GATT\_CCC(\_perm, \_read, \_write, \_user\_data)

<a id="c.BTIF_GATT_CPF"></a>

<a id="gatt__if_8h_1ac6918057cc0950c5d509487f4d1bbd1b"></a> BTIF\_GATT\_CPF(\_perm, \_read, \_write, \_user\_data)

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv423btif_att_indicate_cb_fp"></a>

<a id="_CPPv323btif_att_indicate_cb_fp"></a> <a id="_CPPv223btif_att_indicate_cb_fp"></a> <a id="btif_att_indicate_cb_fp"></a> <a id="gatt__if_8h_1ad58e6d2dbb3ccec2d92422a8399bd5ab"></a> typedef void (\*btif\_att\_indicate\_cb\_fp)(void \*p\_att\_chan, void \*p\_para, uint8\_t err)

<a id="_CPPv417btif_att_tx_cb_fp"></a>

<a id="_CPPv317btif_att_tx_cb_fp"></a> <a id="_CPPv217btif_att_tx_cb_fp"></a> <a id="btif_att_tx_cb_fp"></a> <a id="gatt__if_8h_1a7dfd14931e429422007cbd19159849f7"></a> typedef void (\*btif\_att\_tx\_cb\_fp)([btif\_att\_chan\_info\_t](#_CPPv420btif_att_chan_info_t "btif_att_chan_info_t") \*p\_att\_chan, void \*p\_user\_data)

<a id="_CPPv416btif_att_read_fp"></a>

<a id="_CPPv316btif_att_read_fp"></a> <a id="_CPPv216btif_att_read_fp"></a> <a id="btif_att_read_fp"></a> <a id="gatt__if_8h_1a4a4d00f67661141e6bb9aa1035559ec8"></a> typedef int16\_t (\*btif\_att\_read\_fp)([btif\_att\_chan\_info\_t](#_CPPv420btif_att_chan_info_t "btif_att_chan_info_t") \*p\_att\_chan, const void \*p\_gatt\_svc, uint8\_t \*p\_buf, uint16\_t len, uint16\_t offset, uint16\_t svs\_end\_handle)

<a id="_CPPv417btif_att_write_fp"></a>

<a id="_CPPv317btif_att_write_fp"></a> <a id="_CPPv217btif_att_write_fp"></a> <a id="btif_att_write_fp"></a> <a id="gatt__if_8h_1a81c79d0cbe9896a5365678a082acdca3"></a> typedef int16\_t (\*btif\_att\_write\_fp)([btif\_att\_chan\_info\_t](#_CPPv420btif_att_chan_info_t "btif_att_chan_info_t") \*p\_att\_chan, const void \*p\_gatt\_svc, const uint8\_t \*p\_buf, uint16\_t len, uint16\_t offset, uint8\_t w\_flags, uint16\_t svs\_end\_handle)
