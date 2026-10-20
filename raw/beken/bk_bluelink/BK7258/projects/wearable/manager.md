---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_bluelink/bk7258/zh_CN/v2.0.1/projects/wearable/manager.html
sdk_family: bk_bluelink
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bt-manager"></a>

# bt\_manager 使用说明

bt\_manager 模块是蓝牙设备管理的核心模块，负责蓝牙模式切换、链路状态管理和GAP Event处理。

<a id="header-file"></a>

## Header File

- [bt\_manager.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/bt_manager.h)

<a id="functions"></a>

## Functions

<a id="_CPPv428bt_manager_register_callbackP14btm_callback_s"></a>

<a id="_CPPv328bt_manager_register_callbackP14btm_callback_s"></a> <a id="_CPPv228bt_manager_register_callbackP14btm_callback_s"></a> <a id="bt_manager_register_callback__btm_callback_sP"></a> <a id="bt__manager_8h_1a51dd280bad8e2aeedeb4f0ef4d40382d"></a> int bt\_manager\_register\_callback([btm\_callback\_s](#_CPPv414btm_callback_s "btm_callback_s") \*cb)
:   Register callback functions for the Bluetooth manager.

    参数
    :   **cb** – Pointer to the callback structure.

    返回
    :   0 on success, otherwise error code.

<a id="_CPPv426bt_manager_start_reconnectP7uint8_t7uint8_t"></a>

<a id="_CPPv326bt_manager_start_reconnectP7uint8_t7uint8_t"></a> <a id="_CPPv226bt_manager_start_reconnectP7uint8_t7uint8_t"></a> <a id="bt_manager_start_reconnect__uint8_tP.uint8_t"></a> <a id="bt__manager_8h_1af1b32a73463acad6ccad32f9db85a6bc"></a> void bt\_manager\_start\_reconnect(uint8\_t \*addr, uint8\_t immediate)
:   Start the reconnection process to a specified device.

    参数
    :   - **addr** – Pointer to the address of the device to reconnect to.
        - **immediate** – Whether to initiate the reconnection immediately.

<a id="_CPPv419bt_manager_set_mode7uint8_t"></a>

<a id="_CPPv319bt_manager_set_mode7uint8_t"></a> <a id="_CPPv219bt_manager_set_mode7uint8_t"></a> <a id="bt_manager_set_mode__uint8_t"></a> <a id="bt__manager_8h_1ab46879b59f772290a4940d0ef6761a3d"></a> void bt\_manager\_set\_mode(uint8\_t mode)
:   Set the operation mode of the Bluetooth manager.

    参数
    :   **mode** – The mode to set.

<a id="_CPPv419bt_manager_get_modev"></a>

<a id="_CPPv319bt_manager_get_modev"></a> <a id="_CPPv219bt_manager_get_modev"></a> <a id="bt_manager_get_mode__void"></a> <a id="bt__manager_8h_1a680795cb921c74857b85250f6d19916c"></a> uint8\_t bt\_manager\_get\_mode(void)
:   Get the current operation mode of the Bluetooth manager.

    返回
    :   The current operation mode.

<a id="_CPPv415bt_manager_initv"></a>

<a id="_CPPv315bt_manager_initv"></a> <a id="_CPPv215bt_manager_initv"></a> <a id="bt_manager_init__void"></a> <a id="bt__manager_8h_1ae16eef4171f1c2ea6b71c76b45a4ef20"></a> int bt\_manager\_init(void)
:   Initialize the Bluetooth manager.

    返回
    :   0 on success, otherwise error code.

<a id="_CPPv417bt_manager_deinitv"></a>

<a id="_CPPv317bt_manager_deinitv"></a> <a id="_CPPv217bt_manager_deinitv"></a> <a id="bt_manager_deinit__void"></a> <a id="bt__manager_8h_1a807b6eb9b56db06c86d436558e282e2e"></a> int bt\_manager\_deinit(void)
:   Deinitialize the Bluetooth manager.

    返回
    :   0 on success, otherwise error code.

<a id="_CPPv428bt_manager_get_connect_statev"></a>

<a id="_CPPv328bt_manager_get_connect_statev"></a> <a id="_CPPv228bt_manager_get_connect_statev"></a> <a id="bt_manager_get_connect_state__void"></a> <a id="bt__manager_8h_1a42d200bbc3376c9ad8984c015e213905"></a> uint8\_t bt\_manager\_get\_connect\_state(void)
:   Get the current connection state of the Bluetooth manager.

    返回
    :   The current connection state.

<a id="_CPPv428bt_manager_set_connect_state7uint8_t"></a>

<a id="_CPPv328bt_manager_set_connect_state7uint8_t"></a> <a id="_CPPv228bt_manager_set_connect_state7uint8_t"></a> <a id="bt_manager_set_connect_state__uint8_t"></a> <a id="bt__manager_8h_1a6021b125db046eb5c9e8b3813b070b5b"></a> void bt\_manager\_set\_connect\_state(uint8\_t state)
:   Set the current connection state of the Bluetooth manager.

    参数
    :   **state** – The connection state to set.

<a id="_CPPv431bt_manager_get_reconnect_deviceP7uint8_t"></a>

<a id="_CPPv331bt_manager_get_reconnect_deviceP7uint8_t"></a> <a id="_CPPv231bt_manager_get_reconnect_deviceP7uint8_t"></a> <a id="bt_manager_get_reconnect_device__uint8_tP"></a> <a id="bt__manager_8h_1ad82efd8e097bb3058b53560761384a13"></a> void bt\_manager\_get\_reconnect\_device(uint8\_t \*addr)
:   Get the address of the device to reconnect to.

    参数
    :   **addr** – Pointer to store the address of the device to reconnect to.

<a id="_CPPv431bt_manager_get_connected_devicev"></a>

<a id="_CPPv331bt_manager_get_connected_devicev"></a> <a id="_CPPv231bt_manager_get_connected_devicev"></a> <a id="bt_manager_get_connected_device__void"></a> <a id="bt__manager_8h_1af1b51c9c4946e391fee291992ca79863"></a> uint8\_t \*bt\_manager\_get\_connected\_device(void)
:   Get the address of the currently connected device.

    返回
    :   Pointer to the address of the currently connected device.

<a id="_CPPv430bt_manager_unregister_callback7uint8_t"></a>

<a id="_CPPv330bt_manager_unregister_callback7uint8_t"></a> <a id="_CPPv230bt_manager_unregister_callback7uint8_t"></a> <a id="bt_manager_unregister_callback__uint8_t"></a> <a id="bt__manager_8h_1a1c1abbcd8e691d842ee31326a06f78c0"></a> int bt\_manager\_unregister\_callback(uint8\_t index)
:   Unregister a callback function by index.

    参数
    :   **index** – The index of the callback to unregister.

    返回
    :   0 on success, otherwise error code.

<a id="_CPPv424bk_bt_enter_pairing_modev"></a>

<a id="_CPPv324bk_bt_enter_pairing_modev"></a> <a id="_CPPv224bk_bt_enter_pairing_modev"></a> <a id="bk_bt_enter_pairing_mode__void"></a> <a id="bt__manager_8h_1a247a2b0324873e69b6e7af262bea0011"></a> void bk\_bt\_enter\_pairing\_mode(void)
:   Enter the Bluetooth pairing mode.

<a id="_CPPv421bt_manager_clean_bondv"></a>

<a id="_CPPv321bt_manager_clean_bondv"></a> <a id="_CPPv221bt_manager_clean_bondv"></a> <a id="bt_manager_clean_bond__void"></a> <a id="bt__manager_8h_1aa985d038fab9b30b7995644224a858da"></a> void bt\_manager\_clean\_bond(void)
:   Clean the bonded devices.

<a id="structures"></a>

## Structures

<a id="_CPPv414btm_callback_s"></a>

<a id="_CPPv314btm_callback_s"></a> <a id="_CPPv214btm_callback_s"></a> <a id="btm_callback_s"></a> <a id="structbtm__callback__s"></a> struct btm\_callback\_s
:   Structure for Bluetooth manager callbacks.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N14btm_callback_s6gap_cbE"></a>

    <a id="_CPPv3N14btm_callback_s6gap_cbE"></a> <a id="_CPPv2N14btm_callback_s6gap_cbE"></a> <a id="btm_callback_s::gap_cb__btm_gap_event_cb"></a> <a id="structbtm__callback__s_1a15db5a0d3b33d257ad9e792022889631"></a> [btm\_gap\_event\_cb](#_CPPv416btm_gap_event_cb "btm_gap_event_cb") gap\_cb
    :   GAP event callback function.

    <a id="_CPPv4N14btm_callback_s16start_connect_cbE"></a>

    <a id="_CPPv3N14btm_callback_s16start_connect_cbE"></a> <a id="_CPPv2N14btm_callback_s16start_connect_cbE"></a> <a id="btm_callback_s::start_connect_cb__btm_start_profile_connect_cb"></a> <a id="structbtm__callback__s_1a6a677565715a39a2ec1cf943d2fdac60"></a> [btm\_start\_profile\_connect\_cb](#_CPPv428btm_start_profile_connect_cb "btm_start_profile_connect_cb") start\_connect\_cb
    :   Callback for starting profile connection.

    <a id="_CPPv4N14btm_callback_s15stop_connect_cbE"></a>

    <a id="_CPPv3N14btm_callback_s15stop_connect_cbE"></a> <a id="_CPPv2N14btm_callback_s15stop_connect_cbE"></a> <a id="btm_callback_s::stop_connect_cb__btm_stop_profile_connect_cb"></a> <a id="structbtm__callback__s_1ab0b87e2ffc3233a083f4425e5436d572"></a> [btm\_stop\_profile\_connect\_cb](#_CPPv427btm_stop_profile_connect_cb "btm_stop_profile_connect_cb") stop\_connect\_cb
    :   Callback for stopping profile connection.

    <a id="_CPPv4N14btm_callback_s19start_disconnect_cbE"></a>

    <a id="_CPPv3N14btm_callback_s19start_disconnect_cbE"></a> <a id="_CPPv2N14btm_callback_s19start_disconnect_cbE"></a> <a id="btm_callback_s::start_disconnect_cb__btm_start_profile_disconnect_cb"></a> <a id="structbtm__callback__s_1a4361305ecfd728e2e5431f561c99f304"></a> [btm\_start\_profile\_disconnect\_cb](#_CPPv431btm_start_profile_disconnect_cb "btm_start_profile_disconnect_cb") start\_disconnect\_cb
    :   Callback for starting profile disconnection.

<a id="type-definitions"></a>

## Type Definitions

<a id="_CPPv416btm_gap_event_cb"></a>

<a id="_CPPv316btm_gap_event_cb"></a> <a id="_CPPv216btm_gap_event_cb"></a> <a id="btm_gap_event_cb"></a> <a id="bt__manager_8h_1a898bc8189df1c853082fa380e72f5e92"></a> typedef void (\*btm\_gap\_event\_cb)(bk\_gap\_bt\_cb\_event\_t event, bk\_bt\_gap\_cb\_param\_t \*param)
:   Callback function type for GAP (Generic Access Profile) events.

    Param event
    :   The GAP event type.

    Param param
    :   Pointer to the GAP callback parameter structure.

<a id="_CPPv428btm_start_profile_connect_cb"></a>

<a id="_CPPv328btm_start_profile_connect_cb"></a> <a id="_CPPv228btm_start_profile_connect_cb"></a> <a id="btm_start_profile_connect_cb"></a> <a id="bt__manager_8h_1ac5f11528d4387fcdfa4b4c31c4c0d5c6"></a> typedef void (\*btm\_start\_profile\_connect\_cb)(uint8\_t \*remote\_addr)
:   Callback function type for starting profile connection.

    Param remote\_addr
    :   Pointer to the remote device address.

<a id="_CPPv431btm_start_profile_disconnect_cb"></a>

<a id="_CPPv331btm_start_profile_disconnect_cb"></a> <a id="_CPPv231btm_start_profile_disconnect_cb"></a> <a id="btm_start_profile_disconnect_cb"></a> <a id="bt__manager_8h_1a172aae613c15618eeb6ba75395f29e99"></a> typedef void (\*btm\_start\_profile\_disconnect\_cb)(uint8\_t \*remote\_addr)
:   Callback function type for starting profile disconnection.

    Param remote\_addr
    :   Pointer to the remote device address.

<a id="_CPPv427btm_stop_profile_connect_cb"></a>

<a id="_CPPv327btm_stop_profile_connect_cb"></a> <a id="_CPPv227btm_stop_profile_connect_cb"></a> <a id="btm_stop_profile_connect_cb"></a> <a id="bt__manager_8h_1a77a6e8f09293dfe99296fc92dcac5d1a"></a> typedef void (\*btm\_stop\_profile\_connect\_cb)(void)
:   Callback function type for stopping profile connection.

<a id="enumerations"></a>

## Enumerations

<a id="_CPPv4Ut1_0"></a>

<a id="_CPPv3Ut1_0"></a> <a id="bt__manager_8h_1a06fc87d81c62e9abb8790b6e5713c55b"></a> enum \[anonymous\]
:   Enumeration of Bluetooth manager operation modes.

    *Values:*

    <a id="_CPPv4NUt1_019BT_MNG_MODE_PAIRINGE"></a>

    <a id="_CPPv3NUt1_019BT_MNG_MODE_PAIRINGE"></a> <a id="bt__manager_8h_1a06fc87d81c62e9abb8790b6e5713c55bad0d7447d563469ae09ad20ff80cd5386"></a> enumerator BT\_MNG\_MODE\_PAIRING
    :   connectable and discoverable

    <a id="_CPPv4NUt1_024BT_MNG_MODE_RECONNECTINGE"></a>

    <a id="_CPPv3NUt1_024BT_MNG_MODE_RECONNECTINGE"></a> <a id="bt__manager_8h_1a06fc87d81c62e9abb8790b6e5713c55ba42b296733defaf911db2953e8dd2dc53"></a> enumerator BT\_MNG\_MODE\_RECONNECTING
    :   no-connectable and no-discoverable

    <a id="_CPPv4NUt1_022BT_MNG_MODE_CONNECTEEDE"></a>

    <a id="_CPPv3NUt1_022BT_MNG_MODE_CONNECTEEDE"></a> <a id="bt__manager_8h_1a06fc87d81c62e9abb8790b6e5713c55baff7104fc9d8934e0b863039da932b2b6"></a> enumerator BT\_MNG\_MODE\_CONNECTEED
    :   no-connectable and no-discoverable

    <a id="_CPPv4NUt1_023BT_MNG_MODE_CONNECTABLEE"></a>

    <a id="_CPPv3NUt1_023BT_MNG_MODE_CONNECTABLEE"></a> <a id="bt__manager_8h_1a06fc87d81c62e9abb8790b6e5713c55baf824a506e58240d198ff5b5ab0b1b2ec"></a> enumerator BT\_MNG\_MODE\_CONNECTABLE
    :   connectable and no-discoverable

    <a id="_CPPv4NUt1_016BT_MNG_MODE_IDLEE"></a>

    <a id="_CPPv3NUt1_016BT_MNG_MODE_IDLEE"></a> <a id="bt__manager_8h_1a06fc87d81c62e9abb8790b6e5713c55baccc24e0dbc2bb59296359585469179e2"></a> enumerator BT\_MNG\_MODE\_IDLE
    :   no-connectable and no-discoverable

    <a id="_CPPv4NUt1_029BT_MNG_MODE_DISCOVERABLE_ONLYE"></a>

    <a id="_CPPv3NUt1_029BT_MNG_MODE_DISCOVERABLE_ONLYE"></a> <a id="bt__manager_8h_1a06fc87d81c62e9abb8790b6e5713c55babeff69d1e7287631f65b13ff80112cd2"></a> enumerator BT\_MNG\_MODE\_DISCOVERABLE\_ONLY
    :   no-connectable and discoverable

    <a id="_CPPv4NUt1_019BT_MNG_MODE_ALL_OFFE"></a>

    <a id="_CPPv3NUt1_019BT_MNG_MODE_ALL_OFFE"></a> <a id="bt__manager_8h_1a06fc87d81c62e9abb8790b6e5713c55ba0359824052d470d38a3413fe58d4207e"></a> enumerator BT\_MNG\_MODE\_ALL\_OFF
    :   no-connectable and no-discoverable

<a id="_CPPv4Ut1_1"></a>

<a id="_CPPv3Ut1_1"></a> <a id="bt__manager_8h_1adf764cbdea00d65edcd07bb9953ad2b7"></a> enum \[anonymous\]
:   Enumeration of Bluetooth connection states.

    *Values:*

    <a id="_CPPv4NUt1_113BT_STATE_IDLEE"></a>

    <a id="_CPPv3NUt1_113BT_STATE_IDLEE"></a> <a id="bt__manager_8h_1adf764cbdea00d65edcd07bb9953ad2b7aa980786e228b58789cce8629b821b6fa"></a> enumerator BT\_STATE\_IDLE
    :   Bluetooth is in idle state.

    <a id="_CPPv4NUt1_127BT_STATE_WAIT_FOR_RECONNECTE"></a>

    <a id="_CPPv3NUt1_127BT_STATE_WAIT_FOR_RECONNECTE"></a> <a id="bt__manager_8h_1adf764cbdea00d65edcd07bb9953ad2b7afc0b84d52360b4385bd36e571434d130"></a> enumerator BT\_STATE\_WAIT\_FOR\_RECONNECT
    :   Waiting to initiate a reconnection.

    <a id="_CPPv4NUt1_121BT_STATE_RECONNECTINGE"></a>

    <a id="_CPPv3NUt1_121BT_STATE_RECONNECTINGE"></a> <a id="bt__manager_8h_1adf764cbdea00d65edcd07bb9953ad2b7a7fdd3326f76638ad728776cf9c563c5a"></a> enumerator BT\_STATE\_RECONNECTING
    :   Currently in the process of reconnecting.

    <a id="_CPPv4NUt1_123BT_STATE_LINK_CONNECTEDE"></a>

    <a id="_CPPv3NUt1_123BT_STATE_LINK_CONNECTEDE"></a> <a id="bt__manager_8h_1adf764cbdea00d65edcd07bb9953ad2b7a930e5efca490d4c203522fa8340158f1"></a> enumerator BT\_STATE\_LINK\_CONNECTED
    :   The link layer is connected.

    <a id="_CPPv4NUt1_126BT_STATE_PROFILE_CONNECTEDE"></a>

    <a id="_CPPv3NUt1_126BT_STATE_PROFILE_CONNECTEDE"></a> <a id="bt__manager_8h_1adf764cbdea00d65edcd07bb9953ad2b7a957a36a998670efc3a2b63931f6b93b6"></a> enumerator BT\_STATE\_PROFILE\_CONNECTED
    :   The profile is connected.

    <a id="_CPPv4NUt1_120BT_STATE_KEY_MISSINGE"></a>

    <a id="_CPPv3NUt1_120BT_STATE_KEY_MISSINGE"></a> <a id="bt__manager_8h_1adf764cbdea00d65edcd07bb9953ad2b7af3f7170ea581187c24e78ef5f17e9ccf"></a> enumerator BT\_STATE\_KEY\_MISSING
    :   The encryption key is missing.
