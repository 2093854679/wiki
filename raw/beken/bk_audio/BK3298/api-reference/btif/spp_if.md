---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/btif/spp_if.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="spp-interface-functions"></a>

# SPP Interface Functions

<a id="spp-if-api-brief"></a>

## SPP\_IF API Brief

| Application | Brief |
| --- | --- |
| [`spp_if_is_connected()`](#_CPPv419spp_if_is_connectedP14btif_bd_addr_t "spp_if_is_connected") | return the connect status of the addr mobile link |
| [`spp_if_send_data()`](#_CPPv416spp_if_send_data8uint16_t7uint8_tP7uint8_t8uint16_t "spp_if_send_data") | send SPP data on dedicated SPP link |
| [`spp_if_client_create_slc()`](#_CPPv424spp_if_client_create_slcP12spp_client_t "spp_if_client_create_slc") | SPP client create service level connection |
| [`spp_if_server_start()`](#_CPPv419spp_if_server_startP12spp_server_t "spp_if_server_start") | start new SPP server connection |
| [`spp_if_init()`](#_CPPv411spp_if_initv "spp_if_init") | SPP init function |
| [`spp_if_send_credit()`](#_CPPv418spp_if_send_credit7uint8_t7uint8_t7uint8_t "spp_if_send_credit") | send credit on dedicated SPP connection |
| [`spp_if_get_sync_len()`](#_CPPv419spp_if_get_sync_len14btif_bd_addr_t "spp_if_get_sync_len") | get SPP sync profile total length required |
| [`spp_if_conn_sync()`](#_CPPv416spp_if_conn_syncP14btif_bd_addr_tP7uint8_t8uint16_tP8uint16_t "spp_if_conn_sync") | TWS master used to send sync profile data to slave |
| [`spp_if_conn_restore()`](#_CPPv419spp_if_conn_restoreP14btif_bd_addr_tP7uint8_t8uint16_t "spp_if_conn_restore") | TWS slave used to rebuild its host stack |
| [`spp_if_conn_restore_specific()`](#_CPPv428spp_if_conn_restore_specificP14btif_bd_addr_t8uint16_t "spp_if_conn_restore_specific") | TWS slave update SPP connection handle and recover relevant settings |
| [`spp_if_register_event_callback()`](#_CPPv430spp_if_register_event_callbackP16sppif_callback_t "spp_if_register_event_callback") | register callback function to get system BT SPP event |

<a id="spp-if-api-reference"></a>

## SPP\_IF API Reference

<a id="header-file"></a>

### Header File

- [btif/inc/spp\_if.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/btif/inc/spp_if.h)

<a id="functions"></a>

### Functions

<a id="_CPPv419spp_if_is_connectedP14btif_bd_addr_t"></a>

<a id="_CPPv319spp_if_is_connectedP14btif_bd_addr_t"></a> <a id="_CPPv219spp_if_is_connectedP14btif_bd_addr_t"></a> <a id="spp_if_is_connected__btif_bd_addr_tP"></a> <a id="spp__if_8h_1a84b4f268b41c7fa0b364903eb04c93bf"></a> bool spp\_if\_is\_connected([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr)
:   spp\_if\_is\_connected brief description

    return the connect status of the addr mobile link

    参数:
    :   **p\_addr** – **\[in\]** remote BT MAC address

    返回值:
    :   - **true** – connected
        - **fail** – disconnected

    返回:
    :   result

<a id="_CPPv416spp_if_send_data8uint16_t7uint8_tP7uint8_t8uint16_t"></a>

<a id="_CPPv316spp_if_send_data8uint16_t7uint8_tP7uint8_t8uint16_t"></a> <a id="_CPPv216spp_if_send_data8uint16_t7uint8_tP7uint8_t8uint16_t"></a> <a id="spp_if_send_data__uint16_t.uint8_t.uint8_tP.uint16_t"></a> <a id="spp__if_8h_1abe2b76335e5a9ceed97d88559d31113e"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") spp\_if\_send\_data(uint16\_t handle, uint8\_t dlci, uint8\_t \*p\_data, uint16\_t len)
:   spp\_if\_send\_data brief description

    send SPP data on dedicated SPP link

    参数:
    :   - **handle** – **\[in\]** connection handle
        - **dlci** – **\[in\]** DLCI value
        - **p\_data** – **\[in\]** data buffer need to be sent
        - **len** – **\[in\]** data buffer length

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv424spp_if_client_create_slcP12spp_client_t"></a>

<a id="_CPPv324spp_if_client_create_slcP12spp_client_t"></a> <a id="_CPPv224spp_if_client_create_slcP12spp_client_t"></a> <a id="spp_if_client_create_slc__spp_client_tP"></a> <a id="spp__if_8h_1a97806bec1b3e08fab2500ef6de61ef28"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") spp\_if\_client\_create\_slc([spp\_client\_t](#_CPPv412spp_client_t "spp_client_t") \*p\_spp\_input)
:   spp\_if\_client\_create\_slc brief description

    SPP client create service level connection

    参数:
    :   **p\_spp\_input** – **\[in\]** SPP client setting sturct

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv419spp_if_server_startP12spp_server_t"></a>

<a id="_CPPv319spp_if_server_startP12spp_server_t"></a> <a id="_CPPv219spp_if_server_startP12spp_server_t"></a> <a id="spp_if_server_start__spp_server_tP"></a> <a id="spp__if_8h_1ae657a475a0a682706c18bf1d3c3b7858"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") spp\_if\_server\_start([spp\_server\_t](#_CPPv412spp_server_t "spp_server_t") \*p\_spp\_server)
:   spp\_if\_server\_start brief description

    start new SPP server connection

    参数:
    :   **p\_spp\_server** – **\[in\]** SPP server setting sturct

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv411spp_if_initv"></a>

<a id="_CPPv311spp_if_initv"></a> <a id="_CPPv211spp_if_initv"></a> <a id="spp_if_init__void"></a> <a id="spp__if_8h_1a6478a6aa0cf275f7e2552d9fa00beaad"></a> void spp\_if\_init(void)
:   spp\_if\_init brief description

    SPP init function

    返回:
    :   N/A

<a id="_CPPv418spp_if_send_credit7uint8_t7uint8_t7uint8_t"></a>

<a id="_CPPv318spp_if_send_credit7uint8_t7uint8_t7uint8_t"></a> <a id="_CPPv218spp_if_send_credit7uint8_t7uint8_t7uint8_t"></a> <a id="spp_if_send_credit__uint8_t.uint8_t.uint8_t"></a> <a id="spp__if_8h_1a8b2a8af526e9747cfcb9725a9815fecf"></a> void spp\_if\_send\_credit(uint8\_t handle, uint8\_t dlci, uint8\_t credit)
:   spp\_if\_send\_credit brief description

    send credit on dedicated SPP connection

    参数:
    :   - **handle** – **\[in\]** connection handle
        - **dlci** – **\[in\]** DLCI value
        - **credit** – **\[in\]** credit value

    返回:
    :   N/A

<a id="_CPPv419spp_if_get_sync_len14btif_bd_addr_t"></a>

<a id="_CPPv319spp_if_get_sync_len14btif_bd_addr_t"></a> <a id="_CPPv219spp_if_get_sync_len14btif_bd_addr_t"></a> <a id="spp_if_get_sync_len__btif_bd_addr_t"></a> <a id="spp__if_8h_1a9ed7b648d674df7b4ce887eb9e6b72c4"></a> uint16\_t spp\_if\_get\_sync\_len([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr)
:   spp\_if\_get\_sync\_len brief description

    get SPP sync profile total length required

    参数:
    :   **addr** – **\[in\]** remote BT MAC address

    返回:
    :   data length

<a id="_CPPv416spp_if_conn_syncP14btif_bd_addr_tP7uint8_t8uint16_tP8uint16_t"></a>

<a id="_CPPv316spp_if_conn_syncP14btif_bd_addr_tP7uint8_t8uint16_tP8uint16_t"></a> <a id="_CPPv216spp_if_conn_syncP14btif_bd_addr_tP7uint8_t8uint16_tP8uint16_t"></a> <a id="spp_if_conn_sync__btif_bd_addr_tP.uint8_tP.uint16_t.uint16_tP"></a> <a id="spp__if_8h_1a9eefb33efda58dc58a478f2f3d051909"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") spp\_if\_conn\_sync([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr, uint8\_t \*p\_buff, uint16\_t buff\_len, uint16\_t \*p\_length)
:   spp\_if\_conn\_sync brief description

    TWS master used to send sync profile data to slave

    参数:
    :   - **p\_addr** – **\[in\]** remote BT MAC addresss
        - **p\_buff** – **\[out\]** buffer used to sync profile data
        - **buff\_len** – **\[in\]** p\_buff allocated length
        - **p\_length** – **\[out\]** sync profile data length will be sent

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv419spp_if_conn_restoreP14btif_bd_addr_tP7uint8_t8uint16_t"></a>

<a id="_CPPv319spp_if_conn_restoreP14btif_bd_addr_tP7uint8_t8uint16_t"></a> <a id="_CPPv219spp_if_conn_restoreP14btif_bd_addr_tP7uint8_t8uint16_t"></a> <a id="spp_if_conn_restore__btif_bd_addr_tP.uint8_tP.uint16_t"></a> <a id="spp__if_8h_1a50141206518d955dfa058c68accf1b14"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") spp\_if\_conn\_restore([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr, uint8\_t \*p\_buff, uint16\_t length)
:   spp\_if\_conn\_restore brief description

    TWS slave used to rebuild its host stack

    参数:
    :   - **p\_addr** – **\[in\]** remote BT MAC address
        - **p\_buff** – **\[in\]** sync profile data
        - **length** – **\[in\]** p\_buff data length

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv428spp_if_conn_restore_specificP14btif_bd_addr_t8uint16_t"></a>

<a id="_CPPv328spp_if_conn_restore_specificP14btif_bd_addr_t8uint16_t"></a> <a id="_CPPv228spp_if_conn_restore_specificP14btif_bd_addr_t8uint16_t"></a> <a id="spp_if_conn_restore_specific__btif_bd_addr_tP.uint16_t"></a> <a id="spp__if_8h_1a314fea0c79a54daf7b8c862c653c3a01"></a> [btif\_ret\_t](btif_type.md#_CPPv410btif_ret_t "btif_ret_t") spp\_if\_conn\_restore\_specific([btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr, uint16\_t acl\_handle)
:   spp\_if\_conn\_restore\_specific brief description

    TWS slave update SPP connection handle and recover relevant settings

    参数:
    :   - **p\_addr** – **\[in\]** remote BT MAC address
        - **acl\_handle** – **\[in\]** connection handle

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv430spp_if_register_event_callbackP16sppif_callback_t"></a>

<a id="_CPPv330spp_if_register_event_callbackP16sppif_callback_t"></a> <a id="_CPPv230spp_if_register_event_callbackP16sppif_callback_t"></a> <a id="spp_if_register_event_callback__sppif_callback_tP"></a> <a id="spp__if_8h_1a9fbee6a392f3f1c0232c46d3345e5343"></a> void spp\_if\_register\_event\_callback([sppif\_callback\_t](#_CPPv416sppif_callback_t "sppif_callback_t") \*p\_event\_handle)
:   spp\_if\_register\_event\_callback brief description

    register callback function to get system BT SPP event

    参数:
    :   **p\_event\_handle** – **\[in\]** callback struct from uplayer

    返回:
    :   N/A

<a id="structures"></a>

### Structures

<a id="_CPPv416sppif_callback_t"></a>

<a id="_CPPv316sppif_callback_t"></a> <a id="_CPPv216sppif_callback_t"></a> <a id="sppif_callback_t"></a> <a id="structsppif__callback__t"></a> struct sppif\_callback\_t
:   callback struct definition

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N16sppif_callback_t9dlst_nodeE"></a>

    <a id="_CPPv3N16sppif_callback_t9dlst_nodeE"></a> <a id="_CPPv2N16sppif_callback_t9dlst_nodeE"></a> <a id="sppif_callback_t::dlst_node__dl_list_t"></a> <a id="structsppif__callback__t_1a37dcb15a642d2a3e9087da3bafac1a02"></a> dl\_list\_t dlst\_node
    :   node for application handler will be linked to orthers

    <a id="_CPPv4N16sppif_callback_t8callbackE"></a>

    <a id="_CPPv3N16sppif_callback_t8callbackE"></a> <a id="_CPPv2N16sppif_callback_t8callbackE"></a> <a id="sppif_callback_t::callback__sppif_callback_handle"></a> <a id="structsppif__callback__t_1a678bf561974a2e8923a4996f1d65b544"></a> [sppif\_callback\_handle](#_CPPv421sppif_callback_handle "sppif_callback_handle") callback
    :   function pointer for callback function

<a id="_CPPv412spp_client_t"></a>

<a id="_CPPv312spp_client_t"></a> <a id="_CPPv212spp_client_t"></a> <a id="spp_client_t"></a> <a id="structspp__client__t"></a> struct spp\_client\_t
:   SPP client struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N12spp_client_t4addrE"></a>

    <a id="_CPPv3N12spp_client_t4addrE"></a> <a id="_CPPv2N12spp_client_t4addrE"></a> <a id="spp_client_t::addr__btif_bd_addr_t"></a> <a id="structspp__client__t_1a2565c508a26bf1fc11e98e97781cd930"></a> [btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr
    :   remote BT address

    <a id="_CPPv4N12spp_client_t4uuidE"></a>

    <a id="_CPPv3N12spp_client_t4uuidE"></a> <a id="_CPPv2N12spp_client_t4uuidE"></a> <a id="spp_client_t::uuid__btif_uuid_t"></a> <a id="structspp__client__t_1afb174a997920be2d1c743a44a1150355"></a> [btif\_uuid\_t](btif_type.md#_CPPv411btif_uuid_t "btif_uuid_t") uuid
    :   remote servcie UUID

    <a id="_CPPv4N12spp_client_t12init_creditsE"></a>

    <a id="_CPPv3N12spp_client_t12init_creditsE"></a> <a id="_CPPv2N12spp_client_t12init_creditsE"></a> <a id="spp_client_t::init_credits__uint8_t"></a> <a id="structspp__client__t_1a8f56a1c04ff524d93b37cfee31432992"></a> uint8\_t init\_credits
    :   initial credits

    <a id="_CPPv4N12spp_client_t11data_handleE"></a>

    <a id="_CPPv3N12spp_client_t11data_handleE"></a> <a id="_CPPv2N12spp_client_t11data_handleE"></a> <a id="spp_client_t::data_handle__sppif_callback_t"></a> <a id="structspp__client__t_1a70d4ce32f440de7c5ce44bce73f6a1c6"></a> [sppif\_callback\_t](#_CPPv416sppif_callback_t "sppif_callback_t") data\_handle
    :   callback struct for SPP data

    <a id="_CPPv4N12spp_client_t12event_handleE"></a>

    <a id="_CPPv3N12spp_client_t12event_handleE"></a> <a id="_CPPv2N12spp_client_t12event_handleE"></a> <a id="spp_client_t::event_handle__sppif_callback_t"></a> <a id="structspp__client__t_1a89bc30a8ba5257177a54e272762a1aea"></a> [sppif\_callback\_t](#_CPPv416sppif_callback_t "sppif_callback_t") event\_handle
    :   callback struct for SPP event

<a id="_CPPv412spp_server_t"></a>

<a id="_CPPv312spp_server_t"></a> <a id="_CPPv212spp_server_t"></a> <a id="spp_server_t"></a> <a id="structspp__server__t"></a> struct spp\_server\_t
:   SPP server struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N12spp_server_t4uuidE"></a>

    <a id="_CPPv3N12spp_server_t4uuidE"></a> <a id="_CPPv2N12spp_server_t4uuidE"></a> <a id="spp_server_t::uuid__btif_uuid_t"></a> <a id="structspp__server__t_1acd89dc0ddf5e536bed4a81e05fd1d4f7"></a> [btif\_uuid\_t](btif_type.md#_CPPv411btif_uuid_t "btif_uuid_t") uuid
    :   UUID of server

    <a id="_CPPv4N12spp_server_t12init_creditsE"></a>

    <a id="_CPPv3N12spp_server_t12init_creditsE"></a> <a id="_CPPv2N12spp_server_t12init_creditsE"></a> <a id="spp_server_t::init_credits__uint8_t"></a> <a id="structspp__server__t_1a8b197e1b6f8c71ddd9bb8bc1452cd770"></a> uint8\_t init\_credits
    :   initial credits

    <a id="_CPPv4N12spp_server_t4portE"></a>

    <a id="_CPPv3N12spp_server_t4portE"></a> <a id="_CPPv2N12spp_server_t4portE"></a> <a id="spp_server_t::port__uint8_t"></a> <a id="structspp__server__t_1ac0cb8bb2eaf9abf68ae9d4622d340e8e"></a> uint8\_t port
    :   RFCOMM port

    <a id="_CPPv4N12spp_server_t4dlciE"></a>

    <a id="_CPPv3N12spp_server_t4dlciE"></a> <a id="_CPPv2N12spp_server_t4dlciE"></a> <a id="spp_server_t::dlci__uint8_t"></a> <a id="structspp__server__t_1ac4428b0ee7fb8c900fc47e93865179e2"></a> uint8\_t dlci
    :   DLCI value

    <a id="_CPPv4N12spp_server_t6p_nameE"></a>

    <a id="_CPPv3N12spp_server_t6p_nameE"></a> <a id="_CPPv2N12spp_server_t6p_nameE"></a> <a id="spp_server_t::p_name__cP"></a> <a id="structspp__server__t_1a42deb11091e9dda6900f3a4dfae0b362"></a> char \*p\_name
    :   service name

    <a id="_CPPv4N12spp_server_t11data_handleE"></a>

    <a id="_CPPv3N12spp_server_t11data_handleE"></a> <a id="_CPPv2N12spp_server_t11data_handleE"></a> <a id="spp_server_t::data_handle__sppif_callback_t"></a> <a id="structspp__server__t_1a751a0b01a4bb40be2835dd860511b666"></a> [sppif\_callback\_t](#_CPPv416sppif_callback_t "sppif_callback_t") data\_handle
    :   callback struct for SPP data

    <a id="_CPPv4N12spp_server_t12event_handleE"></a>

    <a id="_CPPv3N12spp_server_t12event_handleE"></a> <a id="_CPPv2N12spp_server_t12event_handleE"></a> <a id="spp_server_t::event_handle__sppif_callback_t"></a> <a id="structspp__server__t_1a7f9a3fcf113c1f9ca2d2e5dd87c70a09"></a> [sppif\_callback\_t](#_CPPv416sppif_callback_t "sppif_callback_t") event\_handle
    :   callback struct for SPP event

<a id="_CPPv416sppif_event_cb_t"></a>

<a id="_CPPv316sppif_event_cb_t"></a> <a id="_CPPv216sppif_event_cb_t"></a> <a id="sppif_event_cb_t"></a> <a id="structsppif__event__cb__t"></a> struct sppif\_event\_cb\_t
:   SPP if event callback struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N16sppif_event_cb_t5eventE"></a>

    <a id="_CPPv3N16sppif_event_cb_t5eventE"></a> <a id="_CPPv2N16sppif_event_cb_t5eventE"></a> <a id="sppif_event_cb_t::event__uint8_t"></a> <a id="structsppif__event__cb__t_1a4e51bbf0be5744a0028ef351297be063"></a> uint8\_t event
    :   index of SPP event

    <a id="_CPPv4N16sppif_event_cb_t4dlciE"></a>

    <a id="_CPPv3N16sppif_event_cb_t4dlciE"></a> <a id="_CPPv2N16sppif_event_cb_t4dlciE"></a> <a id="sppif_event_cb_t::dlci__uint8_t"></a> <a id="structsppif__event__cb__t_1a6e1aa28048cf96ec24d2bf3b1ffff3f5"></a> uint8\_t dlci
    :   DLCI value

    <a id="_CPPv4N16sppif_event_cb_t6handleE"></a>

    <a id="_CPPv3N16sppif_event_cb_t6handleE"></a> <a id="_CPPv2N16sppif_event_cb_t6handleE"></a> <a id="sppif_event_cb_t::handle__uint16_t"></a> <a id="structsppif__event__cb__t_1a0644ebce2a73096452fa65a75fb6b784"></a> uint16\_t handle
    :   connection handle

    <a id="_CPPv4N16sppif_event_cb_t4addrE"></a>

    <a id="_CPPv3N16sppif_event_cb_t4addrE"></a> <a id="_CPPv2N16sppif_event_cb_t4addrE"></a> <a id="sppif_event_cb_t::addr__btif_bd_addr_t"></a> <a id="structsppif__event__cb__t_1a3e007ab33679002cbe5a878e4fbc8b0f"></a> [btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr
    :   remote BT MAC address

    <a id="_CPPv4N16sppif_event_cb_t4uuidE"></a>

    <a id="_CPPv3N16sppif_event_cb_t4uuidE"></a> <a id="_CPPv2N16sppif_event_cb_t4uuidE"></a> <a id="sppif_event_cb_t::uuid__btif_uuid_t"></a> <a id="structsppif__event__cb__t_1a6e67c57b6df3887a08768edab270ef27"></a> [btif\_uuid\_t](btif_type.md#_CPPv411btif_uuid_t "btif_uuid_t") uuid
    :   UUID of service

<a id="_CPPv420sppif_data_cb_para_t"></a>

<a id="_CPPv320sppif_data_cb_para_t"></a> <a id="_CPPv220sppif_data_cb_para_t"></a> <a id="sppif_data_cb_para_t"></a> <a id="structsppif__data__cb__para__t"></a> struct sppif\_data\_cb\_para\_t
:   SPP if data callback struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N20sppif_data_cb_para_t4dlciE"></a>

    <a id="_CPPv3N20sppif_data_cb_para_t4dlciE"></a> <a id="_CPPv2N20sppif_data_cb_para_t4dlciE"></a> <a id="sppif_data_cb_para_t::dlci__uint8_t"></a> <a id="structsppif__data__cb__para__t_1aebe21dc0291a33fa31392f0dbeccf551"></a> uint8\_t dlci
    :   DLCI value

    <a id="_CPPv4N20sppif_data_cb_para_t6handleE"></a>

    <a id="_CPPv3N20sppif_data_cb_para_t6handleE"></a> <a id="_CPPv2N20sppif_data_cb_para_t6handleE"></a> <a id="sppif_data_cb_para_t::handle__uint16_t"></a> <a id="structsppif__data__cb__para__t_1aef50c6ed7732e3b45a184c618aad42e2"></a> uint16\_t handle
    :   connection handle

    <a id="_CPPv4N20sppif_data_cb_para_t3lenE"></a>

    <a id="_CPPv3N20sppif_data_cb_para_t3lenE"></a> <a id="_CPPv2N20sppif_data_cb_para_t3lenE"></a> <a id="sppif_data_cb_para_t::len__uint16_t"></a> <a id="structsppif__data__cb__para__t_1ac6dfaa95a3aa9ef7c1468da1c8b6ceda"></a> uint16\_t len
    :   length for the p\_data

    <a id="_CPPv4N20sppif_data_cb_para_t6p_dataE"></a>

    <a id="_CPPv3N20sppif_data_cb_para_t6p_dataE"></a> <a id="_CPPv2N20sppif_data_cb_para_t6p_dataE"></a> <a id="sppif_data_cb_para_t::p_data__uint8_tP"></a> <a id="structsppif__data__cb__para__t_1a31c61d5e00cdcdfb6a2deeae10420221"></a> uint8\_t \*p\_data
    :   data buffer

<a id="macros"></a>

### Macros

<a id="c.SPPIF_EVENT_PACKET"></a>

<a id="spp__if_8h_1a489d0198079d536ac9c34a6c33590f81"></a> SPPIF\_EVENT\_PACKET

<a id="c.SPPIF_DATA_PACKET"></a>

<a id="spp__if_8h_1a0c49536022370fdc9a76d06a956d5907"></a> SPPIF\_DATA\_PACKET

<a id="c.SPPIF_SERVICE_LEVEL_CONNECTED"></a>

<a id="spp__if_8h_1aee849adb9999e55c1091ae550f6cf2fd"></a> SPPIF\_SERVICE\_LEVEL\_CONNECTED

<a id="c.SPPIF_SERVICE_LEVEL_DISCONNECTED"></a>

<a id="spp__if_8h_1a4440a4f1150e54ffe5dc335bf89c837e"></a> SPPIF\_SERVICE\_LEVEL\_DISCONNECTED

<a id="c.SPPIF_DATA_TX_DONE"></a>

<a id="spp__if_8h_1a4c38549c11d57eddab8d971f49753e20"></a> SPPIF\_DATA\_TX\_DONE

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv421sppif_callback_handle"></a>

<a id="_CPPv321sppif_callback_handle"></a> <a id="_CPPv221sppif_callback_handle"></a> <a id="sppif_callback_handle"></a> <a id="spp__if_8h_1aeaf1297f47893a9e92421271792886fd"></a> typedef void (\*sppif\_callback\_handle)(uint8\_t \*p\_data, uint16\_t size)
