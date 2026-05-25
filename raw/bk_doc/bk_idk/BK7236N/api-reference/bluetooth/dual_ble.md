# Dual BLE APIs[](#dual-ble-apis "永久链接至标题")


重要

The Dual BLE API v1.0 is the lastest stable Dual BLE APIs. All new applications should use Dual BLE API v1.0.


## Dual BLE API Categories[](#dual-ble-api-categories "永久链接至标题")

Most of Dual BLE APIs can be categoried as:

Interface specific BLE APIs:
:   - BLE gap interface

    - BLE gatt common interface

    - BLE gattc interface

    - BLE gatts interface


## Compatibility and Extension[](#compatibility-and-extension "永久链接至标题")

The Dual BLE APIs are flexible, easy to be extended and backward compatible. For most of the BLE configurations, we put some reserved fields in the config struct for future extendence. The API users need to make sure the reserved fields are initialized to 0, otherwise the compatibility may be broken as more fields are added.


## Programing Principle[](#programing-principle "永久链接至标题")

重要

Here is some general principle for BLE API users:
:   - Always init the reserved fields of config stuct to 0

    - Use BK_ERR_CHECK to check the return value of the BLE API

    - If you are not sure how to use BLE APIs, study the BLE example code first

    - If you are not sure how to initialize some fields of config struct, use the default configuration macro to use the config first and then set application specific fields.

    - Don’t do too much work in BLE event callback, relay the event to your own application task.


## User Development Model[](#user-development-model "永久链接至标题")

Similar as most popular BLE driver, the Beken BLE driver is implemented as event driver. The application call BLE APIs to operate the BLE driver and get notified by BLE event.


## User Guide[](#user-guide "永久链接至标题")


- create att database


```
static const bk_gatts_attr_db_t s_gatts_attr_db_service_1[] =
{
    //service
    {
        BK_GATT_PRIMARY_SERVICE_DECL(INTERESTING_SERIVCE_UUID),
    },

    //char 1
    {
        BK_GATT_CHAR_DECL(INTERESTING_CHAR_UUID,
                          sizeof(s_char_buff), s_char_buff,
                          BK_GATT_CHAR_PROP_BIT_READ | BK_GATT_CHAR_PROP_BIT_WRITE_NR | BK_GATT_CHAR_PROP_BIT_WRITE | BK_GATT_CHAR_PROP_BIT_NOTIFY,
                          BK_GATT_PERM_READ_ENCRYPTED | BK_GATT_PERM_WRITE_ENCRYPTED,
                          BK_GATT_RSP_BY_APP),
    },
    {
        BK_GATT_CHAR_DESC_DECL(BK_GATT_UUID_CHAR_CLIENT_CONFIG,
                               sizeof(s_char_desc_buff), (uint8_t *)&s_char_desc_buff,
                               BK_GATT_PERM_READ | BK_GATT_PERM_WRITE,
                               BK_GATT_RSP_BY_APP),
    },
};

ret = bk_ble_gatts_create_attr_tab(s_gatts_attr_db_service_1, s_gatts_if, sizeof(s_gatts_attr_db_service_1) / sizeof(s_gatts_attr_db_service_1[0]), 30);

if (ret != 0)
{
    gatt_loge("bk_ble_gatts_create_attr_tab err %d", ret);
    return -1;
}

```


- start adv


```
bk_ble_gap_ext_adv_params_t adv_param = {0};

adv_param = (bk_ble_gap_ext_adv_params_t)
{
    .type = BK_BLE_GAP_SET_EXT_ADV_PROP_LEGACY_IND,
    .interval_min = 120 * 1,
    .interval_max = 160 * 1,
    .channel_map = BK_ADV_CHNL_ALL,
    .filter_policy = ADV_FILTER_ALLOW_SCAN_ANY_CON_ANY,
    .primary_phy = BK_BLE_GAP_PRI_PHY_1M,
    .secondary_phy = BK_BLE_GAP_PHY_1M,
    .sid = 0,
    .scan_req_notif = 0,
    .own_addr_type = BLE_ADDR_TYPE_PUBLIC,
    .peer_addr_type = BLE_ADDR_TYPE_PUBLIC,
};

ret = bk_ble_gap_set_adv_params(ADV_HANDLE, &adv_param);

bk_ble_adv_data_t adv_data =
{
    .set_scan_rsp = 0,
    .include_name = 1,
    .min_interval = 0x0006,
    .max_interval = 0x0010,
    .appearance = 0,
    .manufacturer_len = 0,
    .p_manufacturer_data = NULL,
    .service_data_len = 0,
    .p_service_data = NULL,
    .service_uuid_len = 0,
    .p_service_uuid = NULL,
    .flag = 0x06,
};

ret = bk_ble_gap_set_adv_data((bk_ble_adv_data_t *)&adv_data);

const bk_ble_gap_ext_adv_t ext_adv =
{
    .instance = 0,
    .duration = 0,
    .max_events = 0,
};

ret = bk_ble_gap_adv_start(1, &ext_adv);

```


- start a connect


```
bk_gap_create_conn_params_t param = {0};

param.scan_interval = 800;
param.scan_window = param.scan_interval / 2;
param.initiator_filter_policy = 0;
param.conn_interval_min = 0x20;
param.conn_interval_max = 0x20;
param.conn_latency = 0;
param.supervision_timeout = 500;
param.min_ce = 0;
param.max_ce = 0;
param.local_addr_type = BLE_ADDR_TYPE_PUBLIC;
param.peer_addr_type = BLE_ADDR_TYPE_PUBLIC;

err = bk_ble_gap_connect(&param);

```


## API Reference[](#api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [bluetooth/bk_dm_gap_ble.h](https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_gap_ble.h "https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_gap_ble.h")


### Functions[](#functions "永久链接至标题")

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_register_callback([bk_ble_gap_cb_t](#_CPPv415bk_ble_gap_cb_t "bk_ble_gap_cb_t") callback)[](#_CPPv428bk_ble_gap_register_callback15bk_ble_gap_cb_t "永久链接至目标")
:   This function is called to occur gap event, such as scan result.

    参数
    :   **callback** – **[in]** callback function

    返回
    :   - BK_OK : success

        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_update_conn_params([bk_ble_conn_update_params_t](#_CPPv427bk_ble_conn_update_params_t "bk_ble_conn_update_params_t") *params)[](#_CPPv429bk_ble_gap_update_conn_paramsP27bk_ble_conn_update_params_t "永久链接至目标")
:   Update connection parameters, can only be used when connection is up.

    参数
    :   **params** – **[in]** - connection update parameters

    返回
    :   - BK_OK : success

        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_set_pkt_data_len([bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") remote_device, uint16_t tx_data_length)[](#_CPPv427bk_ble_gap_set_pkt_data_len12bk_bd_addr_t8uint16_t "永久链接至目标")
:   This function is to set maximum LE data packet size.

    参数
    :   - **remote_device** – **[in]** - remote device

        - **tx_data_length** – **[in]** - data len

    返回
    :   - BK_OK : success

        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_set_rand_addr([bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") rand_addr)[](#_CPPv424bk_ble_gap_set_rand_addr12bk_bd_addr_t "永久链接至目标")
:   This function sets the static Random Address and Non-Resolvable Private Address for the application.

    参数
    :   **rand_addr** – **[in]** the random address which should be setting

    返回
    :   - BK_OK : success

        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_config_local_privacy(bool privacy_enable)[](#_CPPv431bk_ble_gap_config_local_privacyb "永久链接至目标")
:   Enable/disable privacy on the local device.

    参数
    :   **privacy_enable** – **[in]** - enable/disable privacy on remote device.

    返回
    :   - BK_OK : success

        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_config_local_icon(uint16_t icon)[](#_CPPv428bk_ble_gap_config_local_icon8uint16_t "永久链接至目标")
:   set local gap appearance icon

    参数
    :   **icon** – **[in]** - External appearance value, these values are defined by the Bluetooth SIG, please refer to [https://specificationrefs.bluetooth.com/assigned-values/Appearance%20Values.pdf](https://specificationrefs.bluetooth.com/assigned-values/Appearance%20Values.pdf "https://specificationrefs.bluetooth.com/assigned-values/Appearance%20Values.pdf")

    返回
    :   - BK_OK : success

        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_update_whitelist(bool add_remove, [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") remote_bda, [bk_ble_wl_addr_type_t](#_CPPv421bk_ble_wl_addr_type_t "bk_ble_wl_addr_type_t") wl_addr_type)[](#_CPPv427bk_ble_gap_update_whitelistb12bk_bd_addr_t21bk_ble_wl_addr_type_t "永久链接至目标")
:   Add or remove device from white list.

    参数
    :   - **add_remove** – **[in]** the value is true if added the ble device to the white list, and false remove to the white list.

        - **remote_bda** – **[in]** the remote device address add/remove from the white list.

        - **wl_addr_type** – **[in]** whitelist address type

    返回
    :   - BK_OK : success

        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_clear_whitelist(void)[](#_CPPv426bk_ble_gap_clear_whitelistv "永久链接至目标")
:   Clear all white list.

    返回
    :   - BK_OK : success

        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_get_whitelist_size(uint16_t *length)[](#_CPPv429bk_ble_gap_get_whitelist_sizeP8uint16_t "永久链接至目标")
:   Get the whitelist size in the controller.

    参数
    :   **length** – **[out]** the white list length.

    返回
    :   - BK_OK : success

        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_set_device_name(const char *name)[](#_CPPv426bk_ble_gap_set_device_namePKc "永久链接至目标")
:   Set device name to the local device.

    参数
    :   **name** – **[in]** - device name.

    返回
    :   - BK_OK : success

        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_get_device_name(char *name, uint32_t *size)[](#_CPPv426bk_ble_gap_get_device_namePcP8uint32_t "永久链接至目标")
:   Get device name of the local device.

    参数
    :   - **name** – **[out]** - device name.

        - **size** – **[inout]** - name output max size, and real size after return.

    返回
    :   - BK_OK : success

        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_get_local_used_addr([bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") local_used_addr, uint8_t *addr_type)[](#_CPPv430bk_ble_gap_get_local_used_addr12bk_bd_addr_tP7uint8_t "永久链接至目标")
:   This function is called to get local used address and address type. uint8_t *bk_bt_dev_get_address(void) get the public address.

    参数
    :   - **local_used_addr** – **[in]** - current local used ble address (six bytes)

        - **addr_type** – **[in]** - ble address type

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_read_rssi([bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") remote_addr)[](#_CPPv420bk_ble_gap_read_rssi12bk_bd_addr_t "永久链接至目标")
:   This function is called to read the RSSI of remote device. The address of link policy results are returned in the gap callback function with BK_GAP_BLE_READ_RSSI_COMPLETE_EVT event.

    参数
    :   **remote_addr** – **[in]** : The remote connection device address.

    返回
    :   - BK_OK : success

        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_set_security_param([bk_ble_sm_param_t](#_CPPv417bk_ble_sm_param_t "bk_ble_sm_param_t") param_type, void *value, uint8_t len)[](#_CPPv429bk_ble_gap_set_security_param17bk_ble_sm_param_tPv7uint8_t "永久链接至目标")
:   Set a GAP security parameter value. Overrides the default value.

    ```
                   Secure connection is highly recommended to avoid some major
                   vulnerabilities like 'Impersonation in the Pin Pairing Protocol'
                   (CVE-2020-26555) and 'Authentication of the LE Legacy Pairing
                   Protocol'.

                   To accept only `secure connection mode`, it is necessary do as following:

                   1. Set bit `BK_LE_AUTH_REQ_SC_ONLY` (`param_type` is
                   `BK_BLE_SM_AUTHEN_REQ_MODE`), bit `BK_LE_AUTH_BOND` and bit
                   `BK_LE_AUTH_REQ_MITM` is optional as required.

                   2. Set to `BK_BLE_ONLY_ACCEPT_SPECIFIED_AUTH_ENABLE` (`param_type` is
                   `BK_BLE_SM_ONLY_ACCEPT_SPECIFIED_SEC_AUTH`).

                   3. Set to `bk_ble_key_distr_mask_t` (`param_type` is
                   `BK_BLE_SM_SET_INIT_KEY` or `BK_BLE_SM_SET_RSP_KEY`).
    ```

    参数
    :   - **param_type** – **[in]** : the type of the param which to be set

        - **value** – **[in]** : the param value

        - **len** – **[in]** : the length of the param value

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_security_rsp([bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr, bool accept)[](#_CPPv423bk_ble_gap_security_rsp12bk_bd_addr_tb "永久链接至目标")
:   Grant security request access.

    参数
    :   - **bd_addr** – **[in]** : BD address of the peer

        - **accept** – **[in]** : accept the security request or not

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_set_encryption([bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr, [bk_ble_sec_act_t](#_CPPv416bk_ble_sec_act_t "bk_ble_sec_act_t") sec_act)[](#_CPPv421bk_ble_set_encryption12bk_bd_addr_t16bk_ble_sec_act_t "永久链接至目标")
:   Set a gap parameter value. Use this function to change the default GAP parameter values.

    参数
    :   - **bd_addr** – **[in]** : the address of the peer device need to encryption

        - **sec_act** – **[in]** : This is the security action to indicate what kind of BLE security level is required for the BLE link if the BLE is supported

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_passkey_reply([bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr, bool accept, uint32_t passkey)[](#_CPPv420bk_ble_passkey_reply12bk_bd_addr_tb8uint32_t "永久链接至目标")
:   Reply the key value to the peer device in the legacy connection stage.

    参数
    :   - **bd_addr** – **[in]** : BD address of the peer

        - **accept** – **[in]** : passkey entry successful or declined.

        - **passkey** – **[in]** : passkey value, must be a 6 digit number, can be lead by 0.

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_confirm_reply([bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr, bool accept)[](#_CPPv420bk_ble_confirm_reply12bk_bd_addr_tb "永久链接至目标")
:   Reply the confirm value to the peer device in the secure connection stage.

    参数
    :   - **bd_addr** – **[in]** : BD address of the peer device

        - **accept** – **[in]** : numbers to compare are the same or different.

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_pair_key_reply([bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr, bool accept, [bk_ble_key_type_t](#_CPPv417bk_ble_key_type_t "bk_ble_key_type_t") type, void *data, uint32_t len)[](#_CPPv421bk_ble_pair_key_reply12bk_bd_addr_tb17bk_ble_key_type_tPv8uint32_t "永久链接至目标")
:   Reply the save key.

    参数
    :   - **bd_addr** – **[in]** : BD address of the peer device

        - **accept** – **[in]** : true or false

        - **type** – **[in]** : key type.

        - **data** – **[in]** : key data, when type is: BK_LE_KEY_LENC, data is [bk_ble_lenc_keys_t](#structbk__ble__lenc__keys__t "#structbk__ble__lenc__keys__t"). When accept is false, data and len will be ignore.

        - **len** – **[in]** : key len

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_remove_bond_device([bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr)[](#_CPPv425bk_ble_remove_bond_device12bk_bd_addr_t "永久链接至目标")
:   Removes a device from the security database list of peer device. It manages unpairing event while connected.

    参数
    :   **bd_addr** – **[in]** : BD address of the peer device

    返回
    :   - BK_OK : success


        - other : failed

int bk_ble_get_bond_device_num(void)[](#_CPPv426bk_ble_get_bond_device_numv "永久链接至目标")
:   Get the device number from the security database list of peer device. It will return the device bonded number immediately.

    返回
    :   - >= 0 : bonded devices number.


        - BK_FAIL : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_get_bond_device_list(int *dev_num, [bk_ble_bond_dev_t](#_CPPv417bk_ble_bond_dev_t "bk_ble_bond_dev_t") *dev_list)[](#_CPPv427bk_ble_get_bond_device_listPiP17bk_ble_bond_dev_t "永久链接至目标")
:   Get the device from the security database list of peer device. It will return the device bonded information immediately.

    参数
    :   - **dev_num** – **[inout]** Indicate the dev_list array(buffer) size as input. If dev_num is large enough, it means the actual number as output. Suggest that dev_num value equal to [bk_ble_get_bond_device_num()](#group__dm__gap__defines__v1_1ga197bcd6bbaf7eabfddabce66be9fad92 "#group__dm__gap__defines__v1_1ga197bcd6bbaf7eabfddabce66be9fad92").

        - **dev_list** – **[out]** an array(buffer) of `bk_ble_bond_dev_t` type. Use for storing the bonded devices address. The dev_list should be allocated by who call this API.

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_connect([bk_gap_create_conn_params_t](#_CPPv427bk_gap_create_conn_params_t "bk_gap_create_conn_params_t") *param)[](#_CPPv418bk_ble_gap_connectP27bk_gap_create_conn_params_t "永久链接至目标")
:   This function is to connect the physical connection of the peer device.


    **Attention**
    :   1. local_addr_type can be BLE_ADDR_TYPE_PUBLIC ~ BLE_ADDR_TYPE_RPA_RANDOM.


    **Attention**
    :   2. if local_addr_type is BLE_ADDR_TYPE_PUBLIC, and initiator_filter_policy policy not enable, host will use local public addr/peer_addr/peer_addr_type to connect.


    **Attention**
    :   3. if local_addr_type is BLE_ADDR_TYPE_RANDOM, and initiator_filter_policy policy not enable, host will use peer_addr/peer_addr_type, random addr that set in bk_ble_gap_set_adv_rand_addr to connect.


    **Attention**
    :   4. if local_addr_type is BLE_ADDR_TYPE_RPA_PUBLIC, host will try search bond list’s nominal addr by peer_addr/peer_addr_type, if found and BK_LE_KEY_PID | BK_LE_KEY_LID present then host will generate RPA addr to connect peer RPA ADV, otherwise see attention 2.


    **Attention**
    :   5. if local_addr_type is BLE_ADDR_TYPE_RPA_RANDOM, host will try search bond list’s nominal addr by peer_addr/peer_addr_type, if found and BK_LE_KEY_PID | BK_LE_KEY_LID present then host will generate RPA addr to connect peer RPA ADV, otherwise see attention 3.

    参数
    :   **param** – **[in]** : connect param

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_disconnect([bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") remote_device)[](#_CPPv421bk_ble_gap_disconnect12bk_bd_addr_t "永久链接至目标")
:   This function is to disconnect the physical connection of the peer device.

    参数
    :   **remote_device** – **[in]** : BD address of the peer device

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_cancel_connect(void)[](#_CPPv425bk_ble_gap_cancel_connectv "永久链接至目标")
:   This function is to cancel the physical connection that have not connect completed.

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_get_current_conn_params([bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr, [bk_gap_conn_params_t](#_CPPv420bk_gap_conn_params_t "bk_gap_conn_params_t") *conn_params)[](#_CPPv430bk_ble_get_current_conn_params12bk_bd_addr_tP20bk_gap_conn_params_t "永久链接至目标")
:   This function is called to read the connection parameters information of the device.

    参数
    :   - **bd_addr** – **[in]** BD address of the peer device.

        - **conn_params** – **[out]** the connection parameters information

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_gap_ble_set_channels([bk_ble_gap_channels](#_CPPv419bk_ble_gap_channels "bk_ble_gap_channels") channels)[](#_CPPv423bk_gap_ble_set_channels19bk_ble_gap_channels "永久链接至目标")
:   BLE set channels.

    参数
    :   **channels** – **[in]** : The n th such field (in the range 0 to 36) contains the value for the link layer channel index n. 0 means channel n is bad. 1 means channel n is unknown. The most significant bits are reserved and shall be set to 0. At least one channel shall be marked as unknown.

    返回
    :   - BK_OK : success


        - BK_ERR_INVALID_STATE: if bluetooth stack is not yet enabled

        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_read_phy([bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr)[](#_CPPv419bk_ble_gap_read_phy12bk_bd_addr_t "永久链接至目标")
:   This function is used to read the current transmitter PHY and receiver PHY on the connection identified by remote address.

    参数
    :   **bd_addr** – **[in]** : BD address of the peer device

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_set_preferred_default_phy([bk_ble_gap_phy_mask_t](#_CPPv421bk_ble_gap_phy_mask_t "bk_ble_gap_phy_mask_t") tx_phy_mask, [bk_ble_gap_phy_mask_t](#_CPPv421bk_ble_gap_phy_mask_t "bk_ble_gap_phy_mask_t") rx_phy_mask)[](#_CPPv436bk_ble_gap_set_preferred_default_phy21bk_ble_gap_phy_mask_t21bk_ble_gap_phy_mask_t "永久链接至目标")
:   This function is used to allows the Host to specify its preferred values for the transmitter PHY and receiver PHY to be used for all subsequent connections over the LE transport.

    参数
    :   - **tx_phy_mask** – **[in]** : indicates the transmitter PHYs that the Host prefers the Controller to use

        - **rx_phy_mask** – **[in]** : indicates the receiver PHYs that the Host prefers the Controller to use

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_set_preferred_phy([bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr, [bk_ble_gap_all_phys_t](#_CPPv421bk_ble_gap_all_phys_t "bk_ble_gap_all_phys_t") all_phys_mask, [bk_ble_gap_phy_mask_t](#_CPPv421bk_ble_gap_phy_mask_t "bk_ble_gap_phy_mask_t") tx_phy_mask, [bk_ble_gap_phy_mask_t](#_CPPv421bk_ble_gap_phy_mask_t "bk_ble_gap_phy_mask_t") rx_phy_mask, [bk_ble_gap_prefer_phy_options_t](#_CPPv431bk_ble_gap_prefer_phy_options_t "bk_ble_gap_prefer_phy_options_t") phy_options)[](#_CPPv428bk_ble_gap_set_preferred_phy12bk_bd_addr_t21bk_ble_gap_all_phys_t21bk_ble_gap_phy_mask_t21bk_ble_gap_phy_mask_t31bk_ble_gap_prefer_phy_options_t "永久链接至目标")
:   This function is used to set the PHY preferences for the connection identified by the remote address. The Controller might not be able to make the change (e.g. because the peer does not support the requested PHY) or may decide that the current PHY is preferable.

    参数
    :   - **bd_addr** – **[in]** : remote address

        - **all_phys_mask** – **[in]** : a bit field that allows the Host to specify

        - **tx_phy_mask** – **[in]** : a bit field that indicates the transmitter PHYs that the Host prefers the Controller to use

        - **rx_phy_mask** – **[in]** : a bit field that indicates the receiver PHYs that the Host prefers the Controller to use

        - **phy_options** – **[in]** : a bit field that allows the Host to specify options for PHYs

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_set_adv_rand_addr(uint8_t instance, [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") rand_addr)[](#_CPPv428bk_ble_gap_set_adv_rand_addr7uint8_t12bk_bd_addr_t "永久链接至目标")
:   This function is used by the Host to set the random device address specified by the Random_Address parameter.

    参数
    :   - **instance** – **[in]** : Used to identify an advertising set

        - **rand_addr** – **[in]** : Random Device Address

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_set_adv_params(uint8_t instance, const [bk_ble_gap_ext_adv_params_t](#_CPPv427bk_ble_gap_ext_adv_params_t "bk_ble_gap_ext_adv_params_t") *params)[](#_CPPv425bk_ble_gap_set_adv_params7uint8_tPK27bk_ble_gap_ext_adv_params_t "永久链接至目标")
:   This function is used by the Host to set the advertising parameters.


    **Attention**
    :   1. local_addr_type can be BLE_ADDR_TYPE_PUBLIC ~ BLE_ADDR_TYPE_RPA_RANDOM.


    **Attention**
    :   2. if local_addr_type is BLE_ADDR_TYPE_PUBLIC, host will use public addr to send adv.


    **Attention**
    :   3. if local_addr_type is BLE_ADDR_TYPE_RANDOM, host will use random addr that set in bk_ble_gap_set_adv_rand_addr to send adv.


    **Attention**
    :   4. if local_addr_type is BLE_ADDR_TYPE_RPA_PUBLIC, host will try search bond list by peer_addr/peer_addr_type, if found and BK_LE_KEY_PID | BK_LE_KEY_LID present then host will generate RPA addr to send ADV, otherwise see attention 2.


    **Attention**
    :   5. if local_addr_type is BLE_ADDR_TYPE_RPA_RANDOM, host will try search bond list by peer_addr/peer_addr_type, if found and BK_LE_KEY_PID | BK_LE_KEY_LID present then host will generate RPA addr to send ADV, otherwise see attention 3.

    参数
    :   - **instance** – **[in]** : identifies the advertising set whose parameters are being configured.

        - **params** – **[in]** : advertising parameters

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_set_adv_data([bk_ble_adv_data_t](#_CPPv417bk_ble_adv_data_t "bk_ble_adv_data_t") *adv_data)[](#_CPPv423bk_ble_gap_set_adv_dataP17bk_ble_adv_data_t "永久链接至目标")
:   This function is used to set the data used in advertising PDUs that have a data field.

    参数
    :   - **instance** – **[in]** : identifies the advertising set whose data are being configured

        - **length** – **[in]** : data length

        - **data** – **[in]** : data information

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_set_adv_data_raw(uint8_t instance, uint16_t length, const uint8_t *data)[](#_CPPv427bk_ble_gap_set_adv_data_raw7uint8_t8uint16_tPK7uint8_t "永久链接至目标")
:   This function is used to set the data used in advertising PDUs that have a data field.

    参数
    :   - **instance** – **[in]** : identifies the advertising set whose data are being configured

        - **length** – **[in]** : data length

        - **data** – **[in]** : data information

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_set_scan_rsp_data_raw(uint8_t instance, uint16_t length, const uint8_t *scan_rsp_data)[](#_CPPv432bk_ble_gap_set_scan_rsp_data_raw7uint8_t8uint16_tPK7uint8_t "永久链接至目标")
:   This function is used to provide scan response data used in scanning response PDUs.

    参数
    :   - **instance** – **[in]** : identifies the advertising set whose response data are being configured.

        - **length** – **[in]** : responsedata length

        - **scan_rsp_data** – **[in]** : response data information

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_adv_start(uint8_t num_adv, const [bk_ble_gap_ext_adv_t](#_CPPv420bk_ble_gap_ext_adv_t "bk_ble_gap_ext_adv_t") *ext_adv)[](#_CPPv420bk_ble_gap_adv_start7uint8_tPK20bk_ble_gap_ext_adv_t "永久链接至目标")
:   This function is used to request the Controller to enable one or more advertising sets using the advertising sets identified by the instance parameter.

    参数
    :   - **num_adv** – **[in]** : Number of advertising sets to enable or disable

        - **ext_adv** – **[in]** : adv parameters

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_adv_stop(uint8_t num_adv, const uint8_t *ext_adv_inst)[](#_CPPv419bk_ble_gap_adv_stop7uint8_tPK7uint8_t "永久链接至目标")
:   This function is used to request the Controller to disable one or more advertising sets using the advertising sets identified by the instance parameter.

    参数
    :   - **num_adv** – **[in]** : Number of advertising sets to enable or disable

        - **ext_adv_inst** – **[in]** : ext adv instance

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_adv_set_remove(uint8_t instance)[](#_CPPv425bk_ble_gap_adv_set_remove7uint8_t "永久链接至目标")
:   This function is used to remove an advertising set from the Controller.

    参数
    :   **instance** – **[in]** : Used to identify an advertising set

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_adv_set_clear(void)[](#_CPPv424bk_ble_gap_adv_set_clearv "永久链接至目标")
:   This function is used to remove all existing advertising sets from the Controller.

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_set_periodic_adv_params(uint8_t instance, const [bk_ble_gap_periodic_adv_params_t](#_CPPv432bk_ble_gap_periodic_adv_params_t "bk_ble_gap_periodic_adv_params_t") *params)[](#_CPPv434bk_ble_gap_set_periodic_adv_params7uint8_tPK32bk_ble_gap_periodic_adv_params_t "永久链接至目标")
:   This function is used by the Host to set the parameters for periodic advertising.

    参数
    :   - **instance** – **[in]** : identifies the advertising set whose periodic advertising parameters are being configured.

        - **params** – **[in]** : periodic adv parameters

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_set_periodic_adv_data_raw(uint8_t instance, uint16_t length, const uint8_t *data)[](#_CPPv436bk_ble_gap_set_periodic_adv_data_raw7uint8_t8uint16_tPK7uint8_t "永久链接至目标")
:   This function is used to set the data used in periodic advertising PDUs.

    参数
    :   - **instance** – **[in]** : identifies the advertising set whose periodic advertising parameters are being configured.

        - **length** – **[in]** : the length of periodic data

        - **data** – **[in]** : periodic data information

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_periodic_adv_start(uint8_t instance)[](#_CPPv429bk_ble_gap_periodic_adv_start7uint8_t "永久链接至目标")
:   This function is used to request the Controller to enable the periodic advertising for the advertising set specified.

    参数
    :   **instance** – **[in]** : Used to identify an advertising set

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_periodic_adv_stop(uint8_t instance)[](#_CPPv428bk_ble_gap_periodic_adv_stop7uint8_t "永久链接至目标")
:   This function is used to request the Controller to disable the periodic advertising for the advertising set specified.

    参数
    :   **instance** – **[in]** : Used to identify an advertising set

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_periodic_adv_create_sync(const [bk_ble_gap_periodic_adv_sync_params_t](#_CPPv437bk_ble_gap_periodic_adv_sync_params_t "bk_ble_gap_periodic_adv_sync_params_t") *params)[](#_CPPv435bk_ble_gap_periodic_adv_create_syncPK37bk_ble_gap_periodic_adv_sync_params_t "永久链接至目标")
:   This function is used to synchronize with periodic advertising from an advertiser and begin receiving periodic advertising packets.

    参数
    :   **params** – **[in]** : sync parameters

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_periodic_adv_sync_cancel(void)[](#_CPPv435bk_ble_gap_periodic_adv_sync_cancelv "永久链接至目标")
:   This function is used to cancel the LE_Periodic_Advertising_Create_Sync command while it is pending.

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_periodic_adv_sync_terminate(uint16_t sync_handle)[](#_CPPv438bk_ble_gap_periodic_adv_sync_terminate8uint16_t "永久链接至目标")
:   This function is used to stop reception of the periodic advertising identified by the Sync Handle parameter.

    参数
    :   **sync_handle** – **[in]** : identify the periodic advertiser

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_periodic_adv_add_dev_to_list([bk_ble_addr_type_t](#_CPPv418bk_ble_addr_type_t "bk_ble_addr_type_t") addr_type, [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") addr, uint8_t sid)[](#_CPPv439bk_ble_gap_periodic_adv_add_dev_to_list18bk_ble_addr_type_t12bk_bd_addr_t7uint8_t "永久链接至目标")
:   This function is used to add a single device to the Periodic Advertiser list stored in the Controller.

    参数
    :   - **addr_type** – **[in]** : address type

        - **addr** – **[in]** : Device Address

        - **sid** – **[in]** : Advertising SID subfield in the ADI field used to identify the Periodic Advertising

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_periodic_adv_remove_dev_from_list([bk_ble_addr_type_t](#_CPPv418bk_ble_addr_type_t "bk_ble_addr_type_t") addr_type, [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") addr, uint8_t sid)[](#_CPPv444bk_ble_gap_periodic_adv_remove_dev_from_list18bk_ble_addr_type_t12bk_bd_addr_t7uint8_t "永久链接至目标")
:   This function is used to remove one device from the list of Periodic Advertisers stored in the Controller. Removals from the Periodic Advertisers List take effect immediately.

    参数
    :   - **addr_type** – **[in]** : address type

        - **addr** – **[in]** : Device Address

        - **sid** – **[in]** : Advertising SID subfield in the ADI field used to identify the Periodic Advertising

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_periodic_adv_clear_dev(void)[](#_CPPv433bk_ble_gap_periodic_adv_clear_devv "永久链接至目标")
:   This function is used to remove all devices from the list of Periodic Advertisers in the Controller.

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_set_scan_params(const [bk_ble_ext_scan_params_t](#_CPPv424bk_ble_ext_scan_params_t "bk_ble_ext_scan_params_t") *params)[](#_CPPv426bk_ble_gap_set_scan_paramsPK24bk_ble_ext_scan_params_t "永久链接至目标")
:   This function is used to set the extended scan parameters to be used on the advertising channels.

    参数
    :   **params** – **[in]** : scan parameters

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_start_scan(uint32_t duration, uint16_t period)[](#_CPPv421bk_ble_gap_start_scan8uint32_t8uint16_t "永久链接至目标")
:   This function is used to enable scanning.

    参数
    :   - **duration** – **[in]** : Scan duration

        - **period** – **[in]** : Time interval from when the Controller started its last Scan Duration until it begins the subsequent Scan Duration.

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_stop_scan(void)[](#_CPPv420bk_ble_gap_stop_scanv "永久链接至目标")
:   This function is used to disable scanning.

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_prefer_connect_params_set([bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") addr, [bk_ble_gap_phy_mask_t](#_CPPv421bk_ble_gap_phy_mask_t "bk_ble_gap_phy_mask_t") phy_mask, const [bk_ble_gap_conn_params_t](#_CPPv424bk_ble_gap_conn_params_t "bk_ble_gap_conn_params_t") *phy_1m_conn_params, const [bk_ble_gap_conn_params_t](#_CPPv424bk_ble_gap_conn_params_t "bk_ble_gap_conn_params_t") *phy_2m_conn_params, const [bk_ble_gap_conn_params_t](#_CPPv424bk_ble_gap_conn_params_t "bk_ble_gap_conn_params_t") *phy_coded_conn_params)[](#_CPPv436bk_ble_gap_prefer_connect_params_set12bk_bd_addr_t21bk_ble_gap_phy_mask_tPK24bk_ble_gap_conn_params_tPK24bk_ble_gap_conn_params_tPK24bk_ble_gap_conn_params_t "永久链接至目标")
:   This function is used to set aux connection parameters.

    参数
    :   - **addr** – **[in]** : device address

        - **phy_mask** – **[in]** : indicates the PHY(s) on which the advertising packets should be received on the primary advertising channel and the PHYs for which connection parameters have been specified.

        - **phy_1m_conn_params** – **[in]** : Scan connectable advertisements on the LE 1M PHY. Connection parameters for the LE 1M PHY are provided.

        - **phy_2m_conn_params** – **[in]** : Connection parameters for the LE 2M PHY are provided.

        - **phy_coded_conn_params** – **[in]** : Scan connectable advertisements on the LE Coded PHY. Connection parameters for the LE Coded PHY are provided.

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_create_bond([bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr)[](#_CPPv422bk_ble_gap_create_bond12bk_bd_addr_t "永久链接至目标")
:   This function is used to create bond to peer, this function must used after connected.

    参数
    :   **bd_addr** – **[in]** : peer address

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_bond_dev_list_operation([bk_gap_bond_dev_list_operation_t](#_CPPv432bk_gap_bond_dev_list_operation_t "bk_gap_bond_dev_list_operation_t") op, [bk_ble_bond_dev_t](#_CPPv417bk_ble_bond_dev_t "bk_ble_bond_dev_t") *device)[](#_CPPv434bk_ble_gap_bond_dev_list_operation32bk_gap_bond_dev_list_operation_tP17bk_ble_bond_dev_t "永久链接至目标")
:   This function is used to add, remove or clean bond dev info. BK_BLE_GAP_BOND_DEV_LIST_OPERATEION_COMPLETE_EVT evt will report when completed.


    **Attention**
    :   1. Because app layer save bond info, when ble power on, app layer must add bond dev info one by one.


    **Attention**
    :   2. When app layer remove bond info from it self storage, app layer should call BK_GAP_BOND_DEV_LIST_OPERATION_REMOVE or BK_GAP_BOND_DEV_LIST_OPERATION_CLEAN after it done.


    **Attention**
    :   3. This func can’t be call when ble connection/adv/scan is exist.

    参数
    :   - **op** – **[in]** : operation

        - **device** – **[in]** : device info

    返回
    :   - BK_OK : success


        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gap_generate_rpa(uint8_t *irk)[](#_CPPv423bk_ble_gap_generate_rpaP7uint8_t "永久链接至目标")
:   This function is used to generate rpa. BK_BLE_GAP_GENERATE_RPA_COMPLETE_EVT evt will report when completed.

    参数
    :   **irk** – **[in]** : the key which used to generate rpa, when this argument is NULL, host will use current local irk to generate. If local irk is not exist(suchas ir not set), will return fail.

    返回
    :   - BK_OK : success


        - other : failed


### Header File[](#id1 "永久链接至标题")


- [bluetooth/bk_dm_gattc.h](https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_gattc.h "https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_gattc.h")


### Functions[](#id2 "永久链接至标题")

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gattc_register_callback([bk_gattc_cb_t](#_CPPv413bk_gattc_cb_t "bk_gattc_cb_t") callback)[](#_CPPv430bk_ble_gattc_register_callback13bk_gattc_cb_t "永久链接至目标")
:   This function is called to register application callbacks with GATTC module.

    参数
    :   **callback** – **[in]** : pointer to the application callback function.

    返回
    :   - BK_ERR_BLE_SUCCESS: success

        - other: failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gattc_app_register(uint16_t app_id)[](#_CPPv425bk_ble_gattc_app_register8uint16_t "永久链接至目标")
:   This function is called to register application callbacks with GATTC module.

    参数
    :   **app_id** – **[in]** : Application Identify (UUID), for different application

    返回
    :   - BK_ERR_BLE_SUCCESS: success

        - other: failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gattc_app_unregister([bk_gatt_if_t](#_CPPv412bk_gatt_if_t "bk_gatt_if_t") gattc_if)[](#_CPPv427bk_ble_gattc_app_unregister12bk_gatt_if_t "永久链接至目标")
:   This function is called to unregister an application from GATTC module.

    参数
    :   **gattc_if** – **[in]** Gatt client access interface.

    返回
    :   - BK_ERR_BLE_SUCCESS: success

        - other: failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gattc_send_mtu_req([bk_gatt_if_t](#_CPPv412bk_gatt_if_t "bk_gatt_if_t") gattc_if, uint16_t conn_id)[](#_CPPv425bk_ble_gattc_send_mtu_req12bk_gatt_if_t8uint16_t "永久链接至目标")
:   Configure the MTU size in the GATT channel. This can be done only once per connection. Before using, use [bk_ble_gatt_set_local_mtu()](#group__dm__gatt__common__functions__v1_1ga07d73be77fe528eeaa17df45fb6d4efe "#group__dm__gatt__common__functions__v1_1ga07d73be77fe528eeaa17df45fb6d4efe") to configure the local MTU size.

    参数
    :   - **gattc_if** – **[in]** Gatt client access interface.

        - **conn_id** – **[in]** connection ID.

    返回
    :   - BK_ERR_BLE_SUCCESS: success

        - other: failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gattc_read_char([bk_gatt_if_t](#_CPPv412bk_gatt_if_t "bk_gatt_if_t") gattc_if, uint16_t conn_id, uint16_t handle, [bk_gatt_auth_req_t](#_CPPv418bk_gatt_auth_req_t "bk_gatt_auth_req_t") auth_req)[](#_CPPv422bk_ble_gattc_read_char12bk_gatt_if_t8uint16_t8uint16_t18bk_gatt_auth_req_t "永久链接至目标")
:   This function is called to read a service’s characteristics of the given characteristic handle.

    参数
    :   - **gattc_if** – **[in]** Gatt client access interface.

        - **conn_id** – **[in]** : connection ID.

        - **handle** – **[in]** : characteritic handle to read.

        - **auth_req** – **[in]** : authenticate request type

    返回
    :   - BK_ERR_BLE_SUCCESS: success

        - other: failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gattc_read_by_type([bk_gatt_if_t](#_CPPv412bk_gatt_if_t "bk_gatt_if_t") gattc_if, uint16_t conn_id, uint16_t start_handle, uint16_t end_handle, [bk_bt_uuid_t](#_CPPv412bk_bt_uuid_t "bk_bt_uuid_t") *uuid, [bk_gatt_auth_req_t](#_CPPv418bk_gatt_auth_req_t "bk_gatt_auth_req_t") auth_req)[](#_CPPv425bk_ble_gattc_read_by_type12bk_gatt_if_t8uint16_t8uint16_t8uint16_tP12bk_bt_uuid_t18bk_gatt_auth_req_t "永久链接至目标")
:   This function is called to read a service’s characteristics of the given characteristic UUID.

    参数
    :   - **gattc_if** – **[in]** Gatt client access interface.

        - **conn_id** – **[in]** : connection ID.

        - **start_handle** – **[in]** : the attribute start handle.

        - **end_handle** – **[in]** : the attribute end handle

        - **uuid** – **[in]** : The UUID of attribute which will be read.

        - **auth_req** – **[in]** : authenticate request type

    返回
    :   - BK_ERR_BLE_SUCCESS: success

        - other: failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gattc_read_multiple([bk_gatt_if_t](#_CPPv412bk_gatt_if_t "bk_gatt_if_t") gattc_if, uint16_t conn_id, [bk_gattc_multi_t](#_CPPv416bk_gattc_multi_t "bk_gattc_multi_t") *read_multi, [bk_gatt_auth_req_t](#_CPPv418bk_gatt_auth_req_t "bk_gatt_auth_req_t") auth_req)[](#_CPPv426bk_ble_gattc_read_multiple12bk_gatt_if_t8uint16_tP16bk_gattc_multi_t18bk_gatt_auth_req_t "永久链接至目标")
:   This function is called to read multiple characteristic or characteristic descriptors.

    参数
    :   - **gattc_if** – **[in]** Gatt client access interface.

        - **conn_id** – **[in]** : connection ID.

        - **read_multi** – **[in]** : pointer to the read multiple parameter.

        - **auth_req** – **[in]** : authenticate request type

    返回
    :   - BK_ERR_BLE_SUCCESS: success

        - other: failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gattc_read_char_descr([bk_gatt_if_t](#_CPPv412bk_gatt_if_t "bk_gatt_if_t") gattc_if, uint16_t conn_id, uint16_t handle, [bk_gatt_auth_req_t](#_CPPv418bk_gatt_auth_req_t "bk_gatt_auth_req_t") auth_req)[](#_CPPv428bk_ble_gattc_read_char_descr12bk_gatt_if_t8uint16_t8uint16_t18bk_gatt_auth_req_t "永久链接至目标")
:   This function is called to read a characteristics descriptor.

    参数
    :   - **gattc_if** – **[in]** Gatt client access interface.

        - **conn_id** – **[in]** : connection ID.

        - **handle** – **[in]** : descriptor handle to read.

        - **auth_req** – **[in]** : authenticate request type

    返回
    :   - BK_ERR_BLE_SUCCESS: success

        - other: failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gattc_write_char([bk_gatt_if_t](#_CPPv412bk_gatt_if_t "bk_gatt_if_t") gattc_if, uint16_t conn_id, uint16_t handle, uint16_t value_len, uint8_t *value, [bk_gatt_write_type_t](#_CPPv420bk_gatt_write_type_t "bk_gatt_write_type_t") write_type, [bk_gatt_auth_req_t](#_CPPv418bk_gatt_auth_req_t "bk_gatt_auth_req_t") auth_req)[](#_CPPv423bk_ble_gattc_write_char12bk_gatt_if_t8uint16_t8uint16_t8uint16_tP7uint8_t20bk_gatt_write_type_t18bk_gatt_auth_req_t "永久链接至目标")
:   This function is called to write characteristic value.

    参数
    :   - **gattc_if** – **[in]** Gatt client access interface.

        - **conn_id** – **[in]** : connection ID.

        - **handle** – **[in]** : characteristic handle to write.

        - **value_len** – **[in]** length of the value to be written.

        - **value** – **[in]** : the value to be written.

        - **write_type** – **[in]** : the type of attribute write operation.

        - **auth_req** – **[in]** : authentication request.

    返回
    :   - BK_ERR_BLE_SUCCESS: success

        - other: failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gattc_write_char_descr([bk_gatt_if_t](#_CPPv412bk_gatt_if_t "bk_gatt_if_t") gattc_if, uint16_t conn_id, uint16_t handle, uint16_t value_len, uint8_t *value, [bk_gatt_write_type_t](#_CPPv420bk_gatt_write_type_t "bk_gatt_write_type_t") write_type, [bk_gatt_auth_req_t](#_CPPv418bk_gatt_auth_req_t "bk_gatt_auth_req_t") auth_req)[](#_CPPv429bk_ble_gattc_write_char_descr12bk_gatt_if_t8uint16_t8uint16_t8uint16_tP7uint8_t20bk_gatt_write_type_t18bk_gatt_auth_req_t "永久链接至目标")
:   This function is called to write characteristic descriptor value.

    参数
    :   - **gattc_if** – **[in]** Gatt client access interface.

        - **conn_id** – **[in]** : connection ID

        - **handle** – **[in]** : descriptor handle to write.

        - **value_len** – **[in]** length of the value to be written.

        - **value** – **[in]** : the value to be written.

        - **write_type** – **[in]** : the type of attribute write operation.

        - **auth_req** – **[in]** : authentication request.

    返回
    :   - BK_ERR_BLE_SUCCESS: success

        - other: failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gattc_prepare_write([bk_gatt_if_t](#_CPPv412bk_gatt_if_t "bk_gatt_if_t") gattc_if, uint16_t conn_id, uint16_t handle, uint16_t offset, uint16_t value_len, uint8_t *value, [bk_gatt_auth_req_t](#_CPPv418bk_gatt_auth_req_t "bk_gatt_auth_req_t") auth_req)[](#_CPPv426bk_ble_gattc_prepare_write12bk_gatt_if_t8uint16_t8uint16_t8uint16_t8uint16_tP7uint8_t18bk_gatt_auth_req_t "永久链接至目标")
:   This function is called to prepare write a characteristic value.

    参数
    :   - **gattc_if** – **[in]** Gatt client access interface.

        - **conn_id** – **[in]** : connection ID.

        - **handle** – **[in]** : characteristic handle to prepare write.

        - **offset** – **[in]** : offset of the write value.

        - **value_len** – **[in]** length of the value to be written.

        - **value** – **[in]** : the value to be written.

        - **auth_req** – **[in]** : authentication request.

    返回
    :   - BK_ERR_BLE_SUCCESS: success

        - other: failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gattc_prepare_write_char_descr([bk_gatt_if_t](#_CPPv412bk_gatt_if_t "bk_gatt_if_t") gattc_if, uint16_t conn_id, uint16_t handle, uint16_t offset, uint16_t value_len, uint8_t *value, [bk_gatt_auth_req_t](#_CPPv418bk_gatt_auth_req_t "bk_gatt_auth_req_t") auth_req)[](#_CPPv437bk_ble_gattc_prepare_write_char_descr12bk_gatt_if_t8uint16_t8uint16_t8uint16_t8uint16_tP7uint8_t18bk_gatt_auth_req_t "永久链接至目标")
:   This function is called to prepare write a characteristic descriptor value.

    参数
    :   - **gattc_if** – **[in]** Gatt client access interface.

        - **conn_id** – **[in]** : connection ID.

        - **handle** – **[in]** : characteristic descriptor handle to prepare write.

        - **offset** – **[in]** : offset of the write value.

        - **value_len** – **[in]** length of the value to be written.

        - **value** – **[in]** : the value to be written.

        - **auth_req** – **[in]** : authentication request.

    返回
    :   - BK_ERR_BLE_SUCCESS: success

        - other: failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gattc_execute_write([bk_gatt_if_t](#_CPPv412bk_gatt_if_t "bk_gatt_if_t") gattc_if, uint16_t conn_id, bool is_execute)[](#_CPPv426bk_ble_gattc_execute_write12bk_gatt_if_t8uint16_tb "永久链接至目标")
:   This function is called to execute write a prepare write sequence.

    参数
    :   - **gattc_if** – **[in]** Gatt client access interface.

        - **conn_id** – **[in]** : connection ID.

        - **is_execute** – **[in]** : execute or cancel.

    返回
    :   - BK_ERR_BLE_SUCCESS: success

        - other: failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gattc_discover([bk_gatt_if_t](#_CPPv412bk_gatt_if_t "bk_gatt_if_t") gattc_if, uint16_t conn_id, [bk_gatt_auth_req_t](#_CPPv418bk_gatt_auth_req_t "bk_gatt_auth_req_t") auth_req)[](#_CPPv421bk_ble_gattc_discover12bk_gatt_if_t8uint16_t18bk_gatt_auth_req_t "永久链接至目标")
:   Triggle a discovery of the remote device.

    参数
    :   - **gattc_if** – **[in]** Gatt client access interface.

        - **handle** – **[in]** : GATT characteristic handle.

        - **auth_req** – **[in]** : authentication request.

    返回
    :   - BK_ERR_BLE_SUCCESS: success

        - other: failed


### Unions[](#unions "永久链接至标题")

union bk_ble_gattc_cb_param_t[](#_CPPv423bk_ble_gattc_cb_param_t "永久链接至目标")
:   *#include <bk_dm_gattc.h>*

    Gatt client callback parameters union.

    Public Members

    struct [bk_ble_gattc_cb_param_t](#_CPPv423bk_ble_gattc_cb_param_t "bk_ble_gattc_cb_param_t")::[gattc_reg_evt_param](#_CPPv4N23bk_ble_gattc_cb_param_t19gattc_reg_evt_paramE "bk_ble_gattc_cb_param_t::gattc_reg_evt_param") reg[](#_CPPv4N23bk_ble_gattc_cb_param_t3regE "永久链接至目标")
    :   Gatt client callback param of BK_GATTC_REG_EVT

    struct [bk_ble_gattc_cb_param_t](#_CPPv423bk_ble_gattc_cb_param_t "bk_ble_gattc_cb_param_t")::[gattc_cfg_mtu_evt_param](#_CPPv4N23bk_ble_gattc_cb_param_t23gattc_cfg_mtu_evt_paramE "bk_ble_gattc_cb_param_t::gattc_cfg_mtu_evt_param") cfg_mtu[](#_CPPv4N23bk_ble_gattc_cb_param_t7cfg_mtuE "永久链接至目标")
    :   Gatt client callback param of BK_GATTC_CFG_MTU_EVT

    struct [bk_ble_gattc_cb_param_t](#_CPPv423bk_ble_gattc_cb_param_t "bk_ble_gattc_cb_param_t")::[gattc_read_char_evt_param](#_CPPv4N23bk_ble_gattc_cb_param_t25gattc_read_char_evt_paramE "bk_ble_gattc_cb_param_t::gattc_read_char_evt_param") read[](#_CPPv4N23bk_ble_gattc_cb_param_t4readE "永久链接至目标")
    :   Gatt client callback param of BK_GATTC_READ_CHAR_EVT

    struct [bk_ble_gattc_cb_param_t](#_CPPv423bk_ble_gattc_cb_param_t "bk_ble_gattc_cb_param_t")::[gattc_write_evt_param](#_CPPv4N23bk_ble_gattc_cb_param_t21gattc_write_evt_paramE "bk_ble_gattc_cb_param_t::gattc_write_evt_param") write[](#_CPPv4N23bk_ble_gattc_cb_param_t5writeE "永久链接至目标")
    :   Gatt client callback param of BK_GATTC_WRITE_DESCR_EVT

    struct [bk_ble_gattc_cb_param_t](#_CPPv423bk_ble_gattc_cb_param_t "bk_ble_gattc_cb_param_t")::[gattc_exec_cmpl_evt_param](#_CPPv4N23bk_ble_gattc_cb_param_t25gattc_exec_cmpl_evt_paramE "bk_ble_gattc_cb_param_t::gattc_exec_cmpl_evt_param") exec_cmpl[](#_CPPv4N23bk_ble_gattc_cb_param_t9exec_cmplE "永久链接至目标")
    :   Gatt client callback param of BK_GATTC_EXEC_EVT

    struct [bk_ble_gattc_cb_param_t](#_CPPv423bk_ble_gattc_cb_param_t "bk_ble_gattc_cb_param_t")::[gattc_notify_evt_param](#_CPPv4N23bk_ble_gattc_cb_param_t22gattc_notify_evt_paramE "bk_ble_gattc_cb_param_t::gattc_notify_evt_param") notify[](#_CPPv4N23bk_ble_gattc_cb_param_t6notifyE "永久链接至目标")
    :   Gatt client callback param of BK_GATTC_NOTIFY_EVT

    struct [bk_ble_gattc_cb_param_t](#_CPPv423bk_ble_gattc_cb_param_t "bk_ble_gattc_cb_param_t")::[gattc_srvc_chg_evt_param](#_CPPv4N23bk_ble_gattc_cb_param_t24gattc_srvc_chg_evt_paramE "bk_ble_gattc_cb_param_t::gattc_srvc_chg_evt_param") srvc_chg[](#_CPPv4N23bk_ble_gattc_cb_param_t8srvc_chgE "永久链接至目标")
    :   Gatt client callback param of BK_GATTC_SRVC_CHG_EVT

    struct [bk_ble_gattc_cb_param_t](#_CPPv423bk_ble_gattc_cb_param_t "bk_ble_gattc_cb_param_t")::[gattc_connect_evt_param](#_CPPv4N23bk_ble_gattc_cb_param_t23gattc_connect_evt_paramE "bk_ble_gattc_cb_param_t::gattc_connect_evt_param") connect[](#_CPPv4N23bk_ble_gattc_cb_param_t7connectE "永久链接至目标")
    :   Gatt client callback param of BK_GATTC_CONNECT_EVT

    struct [bk_ble_gattc_cb_param_t](#_CPPv423bk_ble_gattc_cb_param_t "bk_ble_gattc_cb_param_t")::[gattc_disconnect_evt_param](#_CPPv4N23bk_ble_gattc_cb_param_t26gattc_disconnect_evt_paramE "bk_ble_gattc_cb_param_t::gattc_disconnect_evt_param") disconnect[](#_CPPv4N23bk_ble_gattc_cb_param_t10disconnectE "永久链接至目标")
    :   Gatt client callback param of BK_GATTC_DISCONNECT_EVT

    struct [bk_ble_gattc_cb_param_t](#_CPPv423bk_ble_gattc_cb_param_t "bk_ble_gattc_cb_param_t")::[gattc_dis_srvc_cmpl_evt_param](#_CPPv4N23bk_ble_gattc_cb_param_t29gattc_dis_srvc_cmpl_evt_paramE "bk_ble_gattc_cb_param_t::gattc_dis_srvc_cmpl_evt_param") dis_srvc_cmpl[](#_CPPv4N23bk_ble_gattc_cb_param_t13dis_srvc_cmplE "永久链接至目标")
    :   Gatt client callback param of BK_GATTC_DIS_SRVC_CMPL_EVT

    struct [bk_ble_gattc_cb_param_t](#_CPPv423bk_ble_gattc_cb_param_t "bk_ble_gattc_cb_param_t")::[gattc_dis_res_service_evt_param](#_CPPv4N23bk_ble_gattc_cb_param_t31gattc_dis_res_service_evt_paramE "bk_ble_gattc_cb_param_t::gattc_dis_res_service_evt_param") dis_res_service[](#_CPPv4N23bk_ble_gattc_cb_param_t15dis_res_serviceE "永久链接至目标")
    :   Gatt client callback param of BK_GATTC_DIS_RES_SERVICE_EVT

    struct [bk_ble_gattc_cb_param_t](#_CPPv423bk_ble_gattc_cb_param_t "bk_ble_gattc_cb_param_t")::[gattc_dis_res_char_evt_param](#_CPPv4N23bk_ble_gattc_cb_param_t28gattc_dis_res_char_evt_paramE "bk_ble_gattc_cb_param_t::gattc_dis_res_char_evt_param") dis_res_char[](#_CPPv4N23bk_ble_gattc_cb_param_t12dis_res_charE "永久链接至目标")
    :   Gatt client callback param of BK_GATTC_DIS_RES_CHAR_EVT

    struct [bk_ble_gattc_cb_param_t](#_CPPv423bk_ble_gattc_cb_param_t "bk_ble_gattc_cb_param_t")::[gattc_dis_res_char_desc_evt_param](#_CPPv4N23bk_ble_gattc_cb_param_t33gattc_dis_res_char_desc_evt_paramE "bk_ble_gattc_cb_param_t::gattc_dis_res_char_desc_evt_param") dis_res_char_desc[](#_CPPv4N23bk_ble_gattc_cb_param_t17dis_res_char_descE "永久链接至目标")
    :   Gatt client callback param of BK_GATTC_DIS_RES_CHAR_DESC_EVT

    struct [bk_ble_gattc_cb_param_t](#_CPPv423bk_ble_gattc_cb_param_t "bk_ble_gattc_cb_param_t")::[gattc_read_by_type_evt_param](#_CPPv4N23bk_ble_gattc_cb_param_t28gattc_read_by_type_evt_paramE "bk_ble_gattc_cb_param_t::gattc_read_by_type_evt_param") read_by_type[](#_CPPv4N23bk_ble_gattc_cb_param_t12read_by_typeE "永久链接至目标")

    struct gattc_cfg_mtu_evt_param[](#_CPPv4N23bk_ble_gattc_cb_param_t23gattc_cfg_mtu_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gattc.h>*

        BK_GATTC_CFG_MTU_EVT.

        Public Members

        [bk_gatt_status_t](#_CPPv416bk_gatt_status_t "bk_gatt_status_t") status[](#_CPPv4N23bk_ble_gattc_cb_param_t23gattc_cfg_mtu_evt_param6statusE "永久链接至目标")
        :   Operation status

        uint16_t conn_id[](#_CPPv4N23bk_ble_gattc_cb_param_t23gattc_cfg_mtu_evt_param7conn_idE "永久链接至目标")
        :   Connection id

        uint16_t mtu[](#_CPPv4N23bk_ble_gattc_cb_param_t23gattc_cfg_mtu_evt_param3mtuE "永久链接至目标")
        :   MTU size

    struct gattc_connect_evt_param[](#_CPPv4N23bk_ble_gattc_cb_param_t23gattc_connect_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gattc.h>*

        BK_GATTC_CONNECT_EVT.

        Public Members

        uint16_t conn_id[](#_CPPv4N23bk_ble_gattc_cb_param_t23gattc_connect_evt_param7conn_idE "永久链接至目标")
        :   Connection id

        uint8_t link_role[](#_CPPv4N23bk_ble_gattc_cb_param_t23gattc_connect_evt_param9link_roleE "永久链接至目标")
        :   Link role : master role = 0 ; slave role = 1

        [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") remote_bda[](#_CPPv4N23bk_ble_gattc_cb_param_t23gattc_connect_evt_param10remote_bdaE "永久链接至目标")
        :   Remote bluetooth device address

        [bk_gatt_conn_params_t](#_CPPv421bk_gatt_conn_params_t "bk_gatt_conn_params_t") conn_params[](#_CPPv4N23bk_ble_gattc_cb_param_t23gattc_connect_evt_param11conn_paramsE "永久链接至目标")
        :   current connection parameters

    struct gattc_dis_res_char_desc_evt_param[](#_CPPv4N23bk_ble_gattc_cb_param_t33gattc_dis_res_char_desc_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gattc.h>*

        BK_GATTC_DIS_RES_CHAR_DESC_EVT.

        Public Members

        uint16_t conn_id[](#_CPPv4N23bk_ble_gattc_cb_param_t33gattc_dis_res_char_desc_evt_param7conn_idE "永久链接至目标")
        :   Connection id

        uint16_t char_handle[](#_CPPv4N23bk_ble_gattc_cb_param_t33gattc_dis_res_char_desc_evt_param11char_handleE "永久链接至目标")
        :   which char handle own this desc

        uint16_t desc_handle[](#_CPPv4N23bk_ble_gattc_cb_param_t33gattc_dis_res_char_desc_evt_param11desc_handleE "永久链接至目标")
        :   desc handle

        [bk_gatt_id_t](#_CPPv412bk_gatt_id_t "bk_gatt_id_t") uuid[](#_CPPv4N23bk_ble_gattc_cb_param_t33gattc_dis_res_char_desc_evt_param4uuidE "永久链接至目标")

        struct [bk_ble_gattc_cb_param_t](#_CPPv423bk_ble_gattc_cb_param_t "bk_ble_gattc_cb_param_t")::[gattc_dis_res_char_desc_evt_param](#_CPPv4N23bk_ble_gattc_cb_param_t33gattc_dis_res_char_desc_evt_paramE "bk_ble_gattc_cb_param_t::gattc_dis_res_char_desc_evt_param")::[anonymous] *array[](#_CPPv4N23bk_ble_gattc_cb_param_t33gattc_dis_res_char_desc_evt_param5arrayE "永久链接至目标")

        uint32_t count[](#_CPPv4N23bk_ble_gattc_cb_param_t33gattc_dis_res_char_desc_evt_param5countE "永久链接至目标")

    struct gattc_dis_res_char_evt_param[](#_CPPv4N23bk_ble_gattc_cb_param_t28gattc_dis_res_char_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gattc.h>*

        BK_GATTC_DIS_RES_CHAR_EVT.

        Public Members

        uint16_t conn_id[](#_CPPv4N23bk_ble_gattc_cb_param_t28gattc_dis_res_char_evt_param7conn_idE "永久链接至目标")
        :   Connection id

        uint16_t start_handle[](#_CPPv4N23bk_ble_gattc_cb_param_t28gattc_dis_res_char_evt_param12start_handleE "永久链接至目标")
        :   char start handle

        uint16_t end_handle[](#_CPPv4N23bk_ble_gattc_cb_param_t28gattc_dis_res_char_evt_param10end_handleE "永久链接至目标")
        :   char end handle

        uint16_t char_value_handle[](#_CPPv4N23bk_ble_gattc_cb_param_t28gattc_dis_res_char_evt_param17char_value_handleE "永久链接至目标")
        :   char declar value handle

        [bk_gatt_id_t](#_CPPv412bk_gatt_id_t "bk_gatt_id_t") uuid[](#_CPPv4N23bk_ble_gattc_cb_param_t28gattc_dis_res_char_evt_param4uuidE "永久链接至目标")
        :   uuid

        struct [bk_ble_gattc_cb_param_t](#_CPPv423bk_ble_gattc_cb_param_t "bk_ble_gattc_cb_param_t")::[gattc_dis_res_char_evt_param](#_CPPv4N23bk_ble_gattc_cb_param_t28gattc_dis_res_char_evt_paramE "bk_ble_gattc_cb_param_t::gattc_dis_res_char_evt_param")::[anonymous] *array[](#_CPPv4N23bk_ble_gattc_cb_param_t28gattc_dis_res_char_evt_param5arrayE "永久链接至目标")

        uint32_t count[](#_CPPv4N23bk_ble_gattc_cb_param_t28gattc_dis_res_char_evt_param5countE "永久链接至目标")

    struct gattc_dis_res_service_evt_param[](#_CPPv4N23bk_ble_gattc_cb_param_t31gattc_dis_res_service_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gattc.h>*

        BK_GATTC_DIS_RES_SERVICE_EVT.

        Public Members

        uint16_t conn_id[](#_CPPv4N23bk_ble_gattc_cb_param_t31gattc_dis_res_service_evt_param7conn_idE "永久链接至目标")
        :   Connection id

        uint16_t start_handle[](#_CPPv4N23bk_ble_gattc_cb_param_t31gattc_dis_res_service_evt_param12start_handleE "永久链接至目标")
        :   Service start handle

        uint16_t end_handle[](#_CPPv4N23bk_ble_gattc_cb_param_t31gattc_dis_res_service_evt_param10end_handleE "永久链接至目标")
        :   Service end handle

        [bk_gatt_id_t](#_CPPv412bk_gatt_id_t "bk_gatt_id_t") srvc_id[](#_CPPv4N23bk_ble_gattc_cb_param_t31gattc_dis_res_service_evt_param7srvc_idE "永久链接至目标")
        :   Service id, include service uuid and other information

        bool is_primary[](#_CPPv4N23bk_ble_gattc_cb_param_t31gattc_dis_res_service_evt_param10is_primaryE "永久链接至目标")
        :   True if this is the primary service

        struct [bk_ble_gattc_cb_param_t](#_CPPv423bk_ble_gattc_cb_param_t "bk_ble_gattc_cb_param_t")::[gattc_dis_res_service_evt_param](#_CPPv4N23bk_ble_gattc_cb_param_t31gattc_dis_res_service_evt_paramE "bk_ble_gattc_cb_param_t::gattc_dis_res_service_evt_param")::[anonymous] *array[](#_CPPv4N23bk_ble_gattc_cb_param_t31gattc_dis_res_service_evt_param5arrayE "永久链接至目标")

        uint32_t count[](#_CPPv4N23bk_ble_gattc_cb_param_t31gattc_dis_res_service_evt_param5countE "永久链接至目标")

    struct gattc_dis_srvc_cmpl_evt_param[](#_CPPv4N23bk_ble_gattc_cb_param_t29gattc_dis_srvc_cmpl_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gattc.h>*

        BK_GATTC_DIS_SRVC_CMPL_EVT.

        Public Members

        [bk_gatt_status_t](#_CPPv416bk_gatt_status_t "bk_gatt_status_t") status[](#_CPPv4N23bk_ble_gattc_cb_param_t29gattc_dis_srvc_cmpl_evt_param6statusE "永久链接至目标")
        :   Operation status

        uint16_t conn_id[](#_CPPv4N23bk_ble_gattc_cb_param_t29gattc_dis_srvc_cmpl_evt_param7conn_idE "永久链接至目标")
        :   Connection id

    struct gattc_disconnect_evt_param[](#_CPPv4N23bk_ble_gattc_cb_param_t26gattc_disconnect_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gattc.h>*

        BK_GATTC_DISCONNECT_EVT.

        Public Members

        [bk_gatt_conn_reason_t](#_CPPv421bk_gatt_conn_reason_t "bk_gatt_conn_reason_t") reason[](#_CPPv4N23bk_ble_gattc_cb_param_t26gattc_disconnect_evt_param6reasonE "永久链接至目标")
        :   The reason of gatt connection close

        uint16_t conn_id[](#_CPPv4N23bk_ble_gattc_cb_param_t26gattc_disconnect_evt_param7conn_idE "永久链接至目标")
        :   Connection id

        [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") remote_bda[](#_CPPv4N23bk_ble_gattc_cb_param_t26gattc_disconnect_evt_param10remote_bdaE "永久链接至目标")
        :   Remote bluetooth device address

    struct gattc_exec_cmpl_evt_param[](#_CPPv4N23bk_ble_gattc_cb_param_t25gattc_exec_cmpl_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gattc.h>*

        BK_GATTC_EXEC_EVT.

        Public Members

        [bk_gatt_status_t](#_CPPv416bk_gatt_status_t "bk_gatt_status_t") status[](#_CPPv4N23bk_ble_gattc_cb_param_t25gattc_exec_cmpl_evt_param6statusE "永久链接至目标")
        :   Operation status

        uint16_t conn_id[](#_CPPv4N23bk_ble_gattc_cb_param_t25gattc_exec_cmpl_evt_param7conn_idE "永久链接至目标")
        :   Connection id

    struct gattc_notify_evt_param[](#_CPPv4N23bk_ble_gattc_cb_param_t22gattc_notify_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gattc.h>*

        BK_GATTC_NOTIFY_EVT.

        Public Members

        uint16_t conn_id[](#_CPPv4N23bk_ble_gattc_cb_param_t22gattc_notify_evt_param7conn_idE "永久链接至目标")
        :   Connection id

        [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") remote_bda[](#_CPPv4N23bk_ble_gattc_cb_param_t22gattc_notify_evt_param10remote_bdaE "永久链接至目标")
        :   Remote bluetooth device address

        uint16_t handle[](#_CPPv4N23bk_ble_gattc_cb_param_t22gattc_notify_evt_param6handleE "永久链接至目标")
        :   The Characteristic or descriptor handle

        uint16_t value_len[](#_CPPv4N23bk_ble_gattc_cb_param_t22gattc_notify_evt_param9value_lenE "永久链接至目标")
        :   Notify attribute value

        uint8_t *value[](#_CPPv4N23bk_ble_gattc_cb_param_t22gattc_notify_evt_param5valueE "永久链接至目标")
        :   Notify attribute value

        bool is_notify[](#_CPPv4N23bk_ble_gattc_cb_param_t22gattc_notify_evt_param9is_notifyE "永久链接至目标")
        :   True means notify, false means indicate

    struct gattc_read_by_type_evt_param[](#_CPPv4N23bk_ble_gattc_cb_param_t28gattc_read_by_type_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gattc.h>*

        BK_GATTC_READ_BY_TYPE_EVT.

        Public Members

        [bk_gatt_status_t](#_CPPv416bk_gatt_status_t "bk_gatt_status_t") status[](#_CPPv4N23bk_ble_gattc_cb_param_t28gattc_read_by_type_evt_param6statusE "永久链接至目标")
        :   Operation status

        uint16_t conn_id[](#_CPPv4N23bk_ble_gattc_cb_param_t28gattc_read_by_type_evt_param7conn_idE "永久链接至目标")
        :   Connection id

        uint16_t elem_count[](#_CPPv4N23bk_ble_gattc_cb_param_t28gattc_read_by_type_evt_param10elem_countE "永久链接至目标")

        uint16_t handle[](#_CPPv4N23bk_ble_gattc_cb_param_t28gattc_read_by_type_evt_param6handleE "永久链接至目标")

        uint8_t *value[](#_CPPv4N23bk_ble_gattc_cb_param_t28gattc_read_by_type_evt_param5valueE "永久链接至目标")
        :   attr handle

        uint16_t len[](#_CPPv4N23bk_ble_gattc_cb_param_t28gattc_read_by_type_evt_param3lenE "永久链接至目标")
        :   attr value

        struct [bk_ble_gattc_cb_param_t](#_CPPv423bk_ble_gattc_cb_param_t "bk_ble_gattc_cb_param_t")::[gattc_read_by_type_evt_param](#_CPPv4N23bk_ble_gattc_cb_param_t28gattc_read_by_type_evt_paramE "bk_ble_gattc_cb_param_t::gattc_read_by_type_evt_param")::[anonymous] *elem[](#_CPPv4N23bk_ble_gattc_cb_param_t28gattc_read_by_type_evt_param4elemE "永久链接至目标")
        :   elem_count

    struct gattc_read_char_evt_param[](#_CPPv4N23bk_ble_gattc_cb_param_t25gattc_read_char_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gattc.h>*

        BK_GATTC_READ_CHAR_EVT, BK_GATTC_READ_DESCR_EVT, BK_GATTC_READ_MULTIPLE_EVT.

        Public Members

        [bk_gatt_status_t](#_CPPv416bk_gatt_status_t "bk_gatt_status_t") status[](#_CPPv4N23bk_ble_gattc_cb_param_t25gattc_read_char_evt_param6statusE "永久链接至目标")
        :   Operation status

        uint16_t conn_id[](#_CPPv4N23bk_ble_gattc_cb_param_t25gattc_read_char_evt_param7conn_idE "永久链接至目标")
        :   Connection id

        uint16_t handle[](#_CPPv4N23bk_ble_gattc_cb_param_t25gattc_read_char_evt_param6handleE "永久链接至目标")
        :   Characteristic handle, Not used when BK_GATTC_READ_MULTIPLE_EVT

        uint8_t *value[](#_CPPv4N23bk_ble_gattc_cb_param_t25gattc_read_char_evt_param5valueE "永久链接至目标")
        :   Characteristic value

        uint16_t value_len[](#_CPPv4N23bk_ble_gattc_cb_param_t25gattc_read_char_evt_param9value_lenE "永久链接至目标")
        :   Characteristic value length

    struct gattc_reg_evt_param[](#_CPPv4N23bk_ble_gattc_cb_param_t19gattc_reg_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gattc.h>*

        BK_GATTC_REG_EVT.

        Public Members

        [bk_gatt_status_t](#_CPPv416bk_gatt_status_t "bk_gatt_status_t") status[](#_CPPv4N23bk_ble_gattc_cb_param_t19gattc_reg_evt_param6statusE "永久链接至目标")
        :   Operation status

        uint16_t app_id[](#_CPPv4N23bk_ble_gattc_cb_param_t19gattc_reg_evt_param6app_idE "永久链接至目标")
        :   Application id which input in register API

        [bk_gatt_if_t](#_CPPv412bk_gatt_if_t "bk_gatt_if_t") gatt_if[](#_CPPv4N23bk_ble_gattc_cb_param_t19gattc_reg_evt_param7gatt_ifE "永久链接至目标")

    struct gattc_srvc_chg_evt_param[](#_CPPv4N23bk_ble_gattc_cb_param_t24gattc_srvc_chg_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gattc.h>*

        BK_GATTC_SRVC_CHG_EVT.

        Public Members

        [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") remote_bda[](#_CPPv4N23bk_ble_gattc_cb_param_t24gattc_srvc_chg_evt_param10remote_bdaE "永久链接至目标")
        :   Remote bluetooth device address

    struct gattc_write_evt_param[](#_CPPv4N23bk_ble_gattc_cb_param_t21gattc_write_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gattc.h>*

        BK_GATTC_WRITE_CHAR_EVT, BK_GATTC_PREP_WRITE_EVT, BK_GATTC_WRITE_DESCR_EVT.

        Public Members

        [bk_gatt_status_t](#_CPPv416bk_gatt_status_t "bk_gatt_status_t") status[](#_CPPv4N23bk_ble_gattc_cb_param_t21gattc_write_evt_param6statusE "永久链接至目标")
        :   Operation status

        uint16_t conn_id[](#_CPPv4N23bk_ble_gattc_cb_param_t21gattc_write_evt_param7conn_idE "永久链接至目标")
        :   Connection id

        uint16_t handle[](#_CPPv4N23bk_ble_gattc_cb_param_t21gattc_write_evt_param6handleE "永久链接至目标")
        :   The Characteristic or descriptor handle

        uint16_t offset[](#_CPPv4N23bk_ble_gattc_cb_param_t21gattc_write_evt_param6offsetE "永久链接至目标")
        :   The prepare write offset, this value is valid only when prepare write


### Type Definitions[](#type-definitions "永久链接至标题")

typedef int32_t (*bk_gattc_cb_t)([bk_gattc_cb_event_t](#_CPPv419bk_gattc_cb_event_t "bk_gattc_cb_event_t") event, [bk_gatt_if_t](#_CPPv412bk_gatt_if_t "bk_gatt_if_t") gattc_if, [bk_ble_gattc_cb_param_t](#_CPPv423bk_ble_gattc_cb_param_t "bk_ble_gattc_cb_param_t") *param)[](#_CPPv413bk_gattc_cb_t "永久链接至目标")
:   GATT Client callback function type.

    Param event
    :   : Event type

    Param gattc_if
    :   : GATT client access interface, normally different gattc_if correspond to different profile

    Param param
    :   : Point to callback parameter, currently is union type


### Enumerations[](#enumerations "永久链接至标题")

enum bk_gattc_cb_event_t[](#_CPPv419bk_gattc_cb_event_t "永久链接至目标")
:   GATT Client callback function events.


    *Values:*

    enumerator BK_GATTC_REG_EVT[](#_CPPv4N19bk_gattc_cb_event_t16BK_GATTC_REG_EVTE "永久链接至目标")
    :   When GATT client is registered, the event comes

    enumerator BK_GATTC_UNREG_EVT[](#_CPPv4N19bk_gattc_cb_event_t18BK_GATTC_UNREG_EVTE "永久链接至目标")
    :   When GATT client is unregistered, the event comes

    enumerator BK_GATTC_READ_CHAR_EVT[](#_CPPv4N19bk_gattc_cb_event_t22BK_GATTC_READ_CHAR_EVTE "永久链接至目标")
    :   When GATT characteristic is read, the event comes

    enumerator BK_GATTC_WRITE_CHAR_EVT[](#_CPPv4N19bk_gattc_cb_event_t23BK_GATTC_WRITE_CHAR_EVTE "永久链接至目标")
    :   When GATT characteristic write operation completes, the event comes

    enumerator BK_GATTC_READ_DESCR_EVT[](#_CPPv4N19bk_gattc_cb_event_t23BK_GATTC_READ_DESCR_EVTE "永久链接至目标")
    :   When GATT characteristic descriptor read completes, the event comes

    enumerator BK_GATTC_WRITE_DESCR_EVT[](#_CPPv4N19bk_gattc_cb_event_t24BK_GATTC_WRITE_DESCR_EVTE "永久链接至目标")
    :   When GATT characteristic descriptor write completes, the event comes

    enumerator BK_GATTC_NOTIFY_EVT[](#_CPPv4N19bk_gattc_cb_event_t19BK_GATTC_NOTIFY_EVTE "永久链接至目标")
    :   When GATT notification or indication arrives, the event comes

    enumerator BK_GATTC_PREP_WRITE_EVT[](#_CPPv4N19bk_gattc_cb_event_t23BK_GATTC_PREP_WRITE_EVTE "永久链接至目标")
    :   When GATT prepare-write operation completes, the event comes

    enumerator BK_GATTC_EXEC_EVT[](#_CPPv4N19bk_gattc_cb_event_t17BK_GATTC_EXEC_EVTE "永久链接至目标")
    :   When write execution completes, the event comes

    enumerator BK_GATTC_CFG_MTU_EVT[](#_CPPv4N19bk_gattc_cb_event_t20BK_GATTC_CFG_MTU_EVTE "永久链接至目标")
    :   When configuration of MTU completes, the event comes

    enumerator BK_GATTC_CONNECT_EVT[](#_CPPv4N19bk_gattc_cb_event_t20BK_GATTC_CONNECT_EVTE "永久链接至目标")
    :   When the ble physical connection is set up, the event comes

    enumerator BK_GATTC_DISCONNECT_EVT[](#_CPPv4N19bk_gattc_cb_event_t23BK_GATTC_DISCONNECT_EVTE "永久链接至目标")
    :   When the ble physical connection disconnected, the event comes

    enumerator BK_GATTC_READ_MULTIPLE_EVT[](#_CPPv4N19bk_gattc_cb_event_t26BK_GATTC_READ_MULTIPLE_EVTE "永久链接至目标")
    :   When the ble characteristic or descriptor multiple complete, the event comes

    enumerator BK_GATTC_DIS_SRVC_CMPL_EVT[](#_CPPv4N19bk_gattc_cb_event_t26BK_GATTC_DIS_SRVC_CMPL_EVTE "永久链接至目标")
    :   When the ble discover service complete, the event comes

    enumerator BK_GATTC_DIS_RES_SERVICE_EVT[](#_CPPv4N19bk_gattc_cb_event_t28BK_GATTC_DIS_RES_SERVICE_EVTE "永久链接至目标")

    enumerator BK_GATTC_DIS_RES_CHAR_EVT[](#_CPPv4N19bk_gattc_cb_event_t25BK_GATTC_DIS_RES_CHAR_EVTE "永久链接至目标")

    enumerator BK_GATTC_DIS_RES_CHAR_DESC_EVT[](#_CPPv4N19bk_gattc_cb_event_t30BK_GATTC_DIS_RES_CHAR_DESC_EVTE "永久链接至目标")

    enumerator BK_GATTC_READ_BY_TYPE_EVT[](#_CPPv4N19bk_gattc_cb_event_t25BK_GATTC_READ_BY_TYPE_EVTE "永久链接至目标")


### Header File[](#id3 "永久链接至标题")


- [bluetooth/bk_dm_gatts.h](https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_gatts.h "https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_gatts.h")


### Functions[](#id4 "永久链接至标题")

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gatts_register_callback([bk_gatts_cb_t](#_CPPv413bk_gatts_cb_t "bk_gatts_cb_t") callback)[](#_CPPv430bk_ble_gatts_register_callback13bk_gatts_cb_t "永久链接至目标")
:   This function is called to register application callbacks with BTA GATTS module.

    参数
    :   **callback** – : see bk_gatts_cb_t

    返回
    :   - BK_ERR_BLE_SUCCESS : success

        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gatts_app_register(uint16_t app_id)[](#_CPPv425bk_ble_gatts_app_register8uint16_t "永久链接至目标")
:   This function is called to register application identifier.

    参数
    :   **app_id** – : app id, not used now

    返回
    :   - BK_ERR_BLE_SUCCESS : success

        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gatts_app_unregister([bk_gatt_if_t](#_CPPv412bk_gatt_if_t "bk_gatt_if_t") gatts_if)[](#_CPPv427bk_ble_gatts_app_unregister12bk_gatt_if_t "永久链接至目标")
:   unregister with GATT Server.

    参数
    :   **gatts_if** – **[in]** GATT server access interface

    返回
    :   - BK_ERR_BLE_SUCCESS : success

        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gatts_create_service([bk_gatt_if_t](#_CPPv412bk_gatt_if_t "bk_gatt_if_t") gatts_if, [bk_gatt_srvc_id_t](#_CPPv417bk_gatt_srvc_id_t "bk_gatt_srvc_id_t") *service_id, uint16_t num_handle)[](#_CPPv427bk_ble_gatts_create_service12bk_gatt_if_tP17bk_gatt_srvc_id_t8uint16_t "永久链接至目标")
:   Create a service. When service creation is done, a callback event BK_GATTS_CREATE_EVT is called to report status and service ID to the profile. The service ID obtained in the callback function needs to be used when adding included service and characteristics/descriptors into the service.

    参数
    :   - **gatts_if** – **[in]** GATT server access interface

        - **service_id** – **[in]** service ID.

        - **num_handle** – **[in]** number of handle requested for this service.

    返回
    :   - BK_ERR_BLE_SUCCESS : success

        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gatts_create_attr_tab(const [bk_gatts_attr_db_t](#_CPPv418bk_gatts_attr_db_t "bk_gatts_attr_db_t") *gatts_attr_db, [bk_gatt_if_t](#_CPPv412bk_gatt_if_t "bk_gatt_if_t") gatts_if, uint16_t count, uint32_t max_attr_count)[](#_CPPv428bk_ble_gatts_create_attr_tabPK18bk_gatts_attr_db_t12bk_gatt_if_t8uint16_t8uint32_t "永久链接至目标")
:   Create a service attribute tab. Only one service once.

    参数
    :   - **gatts_attr_db** – **[in]** the pointer to the service attr tab. At least has one service declar

        - **gatts_if** – **[in]** GATT server access interface

        - **count** – **[in]** the number of gatts_attr_db.

        - **max_attr_count** – **[in]** max attr num of this service.

    返回
    :   - BK_ERR_BLE_SUCCESS : success

        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gatts_add_char(uint16_t service_handle, [bk_bt_uuid_t](#_CPPv412bk_bt_uuid_t "bk_bt_uuid_t") *char_uuid, [bk_gatt_perm_t](#_CPPv414bk_gatt_perm_t "bk_gatt_perm_t") perm, [bk_gatt_char_prop_t](#_CPPv419bk_gatt_char_prop_t "bk_gatt_char_prop_t") property, [bk_attr_value_t](#_CPPv415bk_attr_value_t "bk_attr_value_t") *char_val, [bk_attr_control_t](#_CPPv417bk_attr_control_t "bk_attr_control_t") *control)[](#_CPPv421bk_ble_gatts_add_char8uint16_tP12bk_bt_uuid_t14bk_gatt_perm_t19bk_gatt_char_prop_tP15bk_attr_value_tP17bk_attr_control_t "永久链接至目标")
:   This function is called to add a characteristic into a service.

    参数
    :   - **service_handle** – **[in]** service handle to which this included service is to be added.

        - **char_uuid** – **[in]** : Characteristic UUID.

        - **perm** – **[in]** : Characteristic value declaration attribute permission.

        - **property** – **[in]** : Characteristic Properties

        - **char_val** – **[in]** : Characteristic value

        - **control** – **[in]** : attribute response control byte

    返回
    :   - BK_ERR_BLE_SUCCESS : success

        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gatts_add_char_descr(uint16_t service_handle, uint16_t char_handle, [bk_bt_uuid_t](#_CPPv412bk_bt_uuid_t "bk_bt_uuid_t") *descr_uuid, [bk_gatt_perm_t](#_CPPv414bk_gatt_perm_t "bk_gatt_perm_t") perm, [bk_attr_value_t](#_CPPv415bk_attr_value_t "bk_attr_value_t") *char_descr_val, [bk_attr_control_t](#_CPPv417bk_attr_control_t "bk_attr_control_t") *control)[](#_CPPv427bk_ble_gatts_add_char_descr8uint16_t8uint16_tP12bk_bt_uuid_t14bk_gatt_perm_tP15bk_attr_value_tP17bk_attr_control_t "永久链接至目标")
:   This function is called to add characteristic descriptor. When it’s done, a callback event BK_GATTS_ADD_DESCR_EVT is called to report the status and an ID number for this descriptor.

    参数
    :   - **service_handle** – **[in]** service handle to which this characteristic descriptor is to be added.

        - **char_handle** – **[in]** which characteristic descriptor is to be added.

        - **char_handle** – **[in]** which characteristic descriptor is to be added.

        - **perm** – **[in]** descriptor access permission.

        - **descr_uuid** – **[in]** descriptor UUID.

        - **char_descr_val** – **[in]** : Characteristic descriptor value

        - **control** – **[in]** : attribute response control byte

    返回
    :   - BK_ERR_BLE_SUCCESS : success

        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gatts_start_service(uint16_t service_attr_handle)[](#_CPPv426bk_ble_gatts_start_service8uint16_t "永久链接至目标")
:   This function is called to start a service.

    参数
    :   **service_attr_handle** – **[in]** the service handle to be started.

    返回
    :   - BK_ERR_BLE_SUCCESS : success

        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gatts_stop_service(uint16_t service_attr_handle)[](#_CPPv425bk_ble_gatts_stop_service8uint16_t "永久链接至目标")
:   This function is called to stop a service.

    参数
    :   **service_attr_handle** – **[in]** the service handle to be stop.

    返回
    :   - BK_ERR_BLE_SUCCESS : success

        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gatts_send_indicate([bk_gatt_if_t](#_CPPv412bk_gatt_if_t "bk_gatt_if_t") gatts_if, uint16_t conn_id, uint16_t attr_handle, uint16_t value_len, uint8_t *value, bool need_confirm)[](#_CPPv426bk_ble_gatts_send_indicate12bk_gatt_if_t8uint16_t8uint16_t8uint16_tP7uint8_tb "永久链接至目标")
:   Send indicate or notify to GATT client. Set param need_confirm as false will send notification, otherwise indication.

    参数
    :   - **gatts_if** – **[in]** GATT server access interface

        - **conn_id** – **[in]** - connection handle.

        - **attr_handle** – **[in]** - attribute handle to indicate.

        - **value_len** – **[in]** - indicate value length.

        - **value** – **[in]** value to indicate.

        - **need_confirm** – **[in]** - Whether a confirmation is required. false sends a GATT notification, true sends a GATT indication.

    返回
    :   - BK_ERR_BLE_SUCCESS : success

        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gatts_send_response([bk_gatt_if_t](#_CPPv412bk_gatt_if_t "bk_gatt_if_t") gatts_if, uint16_t conn_id, uint32_t trans_id, [bk_gatt_status_t](#_CPPv416bk_gatt_status_t "bk_gatt_status_t") status, [bk_gatt_rsp_t](#_CPPv413bk_gatt_rsp_t "bk_gatt_rsp_t") *rsp)[](#_CPPv426bk_ble_gatts_send_response12bk_gatt_if_t8uint16_t8uint32_t16bk_gatt_status_tP13bk_gatt_rsp_t "永久链接至目标")
:   This function is called to send a response to a request.

    参数
    :   - **gatts_if** – **[in]** GATT server access interface

        - **conn_id** – **[in]** - connection handle.

        - **trans_id** – **[in]** - Transaction id

        - **status** – **[in]** - response status

        - **rsp** – **[in]** - response data.

    返回
    :   - BK_ERR_BLE_SUCCESS : success

        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gatts_set_attr_value(uint16_t attr_handle, uint16_t length, const uint8_t *value)[](#_CPPv427bk_ble_gatts_set_attr_value8uint16_t8uint16_tPK7uint8_t "永久链接至目标")
:   This function is called to set the attribute value by the application.

    参数
    :   - **attr_handle** – **[in]** the attribute handle which to be set

        - **length** – **[in]** the value length

        - **value** – **[in]** the pointer to the attribute value

    返回
    :   - BK_ERR_BLE_SUCCESS : success

        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gatts_get_attr_value(uint16_t attr_handle, uint16_t *length, uint8_t **value)[](#_CPPv427bk_ble_gatts_get_attr_value8uint16_tP8uint16_tPP7uint8_t "永久链接至目标")
:   Retrieve attribute value.

    参数
    :   - **attr_handle** – **[in]** Attribute handle.

        - **length** – **[out]** pointer to the attribute value length

        - **value** – **[out]** Pointer to attribute value payload, the value cannot be modified by user

    返回
    :   - BK_ERR_BLE_SUCCESS : success

        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gatts_send_service_change_indicate([bk_gatt_if_t](#_CPPv412bk_gatt_if_t "bk_gatt_if_t") gatts_if, uint16_t conn_id, uint8_t all_connected)[](#_CPPv441bk_ble_gatts_send_service_change_indicate12bk_gatt_if_t8uint16_t7uint8_t "永久链接至目标")
:   Send service change indicate.

    参数
    :   - **gatts_if** – **[in]** GATT server access interface

        - **conn_id** – **[in]** - connection handle.

        - **all_connected** – **[in]** - If all_connected is true then it will send service change indicate to all the connected devices and conn_id will be ignore.

    返回
    :   - BK_ERR_BLE_SUCCESS : success

        - other : failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gatts_char_property_operation([bk_gatts_char_property_bit_mask_op_t](#_CPPv436bk_gatts_char_property_bit_mask_op_t "bk_gatts_char_property_bit_mask_op_t") op, uint16_t attr_handle, uint16_t *io)[](#_CPPv436bk_ble_gatts_char_property_operation36bk_gatts_char_property_bit_mask_op_t8uint16_tP8uint16_t "永久链接至目标")
:   Get or set characteristic property.

    参数
    :   - **op** – **[in]** GATT get or set.

        - **attr_handle** – **[in]** char value attr handle.

        - **[in|out]** – io: input when set and output when set

    返回
    :   - BK_ERR_BLE_SUCCESS : success

        - other : failed


### Unions[](#id5 "永久链接至标题")

union bk_ble_gatts_cb_param_t[](#_CPPv423bk_ble_gatts_cb_param_t "永久链接至目标")
:   *#include <bk_dm_gatts.h>*

    Gatt server callback parameters union.

    Public Members

    struct [bk_ble_gatts_cb_param_t](#_CPPv423bk_ble_gatts_cb_param_t "bk_ble_gatts_cb_param_t")::[gatts_reg_evt_param](#_CPPv4N23bk_ble_gatts_cb_param_t19gatts_reg_evt_paramE "bk_ble_gatts_cb_param_t::gatts_reg_evt_param") reg[](#_CPPv4N23bk_ble_gatts_cb_param_t3regE "永久链接至目标")
    :   Gatt server callback param of BK_GATTS_REG_EVT

    struct [bk_ble_gatts_cb_param_t](#_CPPv423bk_ble_gatts_cb_param_t "bk_ble_gatts_cb_param_t")::[gatts_read_evt_param](#_CPPv4N23bk_ble_gatts_cb_param_t20gatts_read_evt_paramE "bk_ble_gatts_cb_param_t::gatts_read_evt_param") read[](#_CPPv4N23bk_ble_gatts_cb_param_t4readE "永久链接至目标")
    :   Gatt server callback param of BK_GATTS_READ_EVT

    struct [bk_ble_gatts_cb_param_t](#_CPPv423bk_ble_gatts_cb_param_t "bk_ble_gatts_cb_param_t")::[gatts_write_evt_param](#_CPPv4N23bk_ble_gatts_cb_param_t21gatts_write_evt_paramE "bk_ble_gatts_cb_param_t::gatts_write_evt_param") write[](#_CPPv4N23bk_ble_gatts_cb_param_t5writeE "永久链接至目标")
    :   Gatt server callback param of BK_GATTS_WRITE_EVT

    struct [bk_ble_gatts_cb_param_t](#_CPPv423bk_ble_gatts_cb_param_t "bk_ble_gatts_cb_param_t")::[gatts_exec_write_evt_param](#_CPPv4N23bk_ble_gatts_cb_param_t26gatts_exec_write_evt_paramE "bk_ble_gatts_cb_param_t::gatts_exec_write_evt_param") exec_write[](#_CPPv4N23bk_ble_gatts_cb_param_t10exec_writeE "永久链接至目标")
    :   Gatt server callback param of BK_GATTS_EXEC_WRITE_EVT

    struct [bk_ble_gatts_cb_param_t](#_CPPv423bk_ble_gatts_cb_param_t "bk_ble_gatts_cb_param_t")::[gatts_mtu_evt_param](#_CPPv4N23bk_ble_gatts_cb_param_t19gatts_mtu_evt_paramE "bk_ble_gatts_cb_param_t::gatts_mtu_evt_param") mtu[](#_CPPv4N23bk_ble_gatts_cb_param_t3mtuE "永久链接至目标")
    :   Gatt server callback param of BK_GATTS_MTU_EVT

    struct [bk_ble_gatts_cb_param_t](#_CPPv423bk_ble_gatts_cb_param_t "bk_ble_gatts_cb_param_t")::[gatts_conf_evt_param](#_CPPv4N23bk_ble_gatts_cb_param_t20gatts_conf_evt_paramE "bk_ble_gatts_cb_param_t::gatts_conf_evt_param") conf[](#_CPPv4N23bk_ble_gatts_cb_param_t4confE "永久链接至目标")
    :   Gatt server callback param of BK_GATTS_CONF_EVT (confirm)

    struct [bk_ble_gatts_cb_param_t](#_CPPv423bk_ble_gatts_cb_param_t "bk_ble_gatts_cb_param_t")::[gatts_create_evt_param](#_CPPv4N23bk_ble_gatts_cb_param_t22gatts_create_evt_paramE "bk_ble_gatts_cb_param_t::gatts_create_evt_param") create[](#_CPPv4N23bk_ble_gatts_cb_param_t6createE "永久链接至目标")
    :   Gatt server callback param of BK_GATTS_CREATE_EVT

    struct [bk_ble_gatts_cb_param_t](#_CPPv423bk_ble_gatts_cb_param_t "bk_ble_gatts_cb_param_t")::[gatts_add_char_evt_param](#_CPPv4N23bk_ble_gatts_cb_param_t24gatts_add_char_evt_paramE "bk_ble_gatts_cb_param_t::gatts_add_char_evt_param") add_char[](#_CPPv4N23bk_ble_gatts_cb_param_t8add_charE "永久链接至目标")
    :   Gatt server callback param of BK_GATTS_ADD_CHAR_EVT

    struct [bk_ble_gatts_cb_param_t](#_CPPv423bk_ble_gatts_cb_param_t "bk_ble_gatts_cb_param_t")::[gatts_add_char_descr_evt_param](#_CPPv4N23bk_ble_gatts_cb_param_t30gatts_add_char_descr_evt_paramE "bk_ble_gatts_cb_param_t::gatts_add_char_descr_evt_param") add_char_descr[](#_CPPv4N23bk_ble_gatts_cb_param_t14add_char_descrE "永久链接至目标")
    :   Gatt server callback param of BK_GATTS_ADD_CHAR_DESCR_EVT

    struct [bk_ble_gatts_cb_param_t](#_CPPv423bk_ble_gatts_cb_param_t "bk_ble_gatts_cb_param_t")::[gatts_start_evt_param](#_CPPv4N23bk_ble_gatts_cb_param_t21gatts_start_evt_paramE "bk_ble_gatts_cb_param_t::gatts_start_evt_param") start[](#_CPPv4N23bk_ble_gatts_cb_param_t5startE "永久链接至目标")
    :   Gatt server callback param of BK_GATTS_START_EVT

    struct [bk_ble_gatts_cb_param_t](#_CPPv423bk_ble_gatts_cb_param_t "bk_ble_gatts_cb_param_t")::[gatts_stop_evt_param](#_CPPv4N23bk_ble_gatts_cb_param_t20gatts_stop_evt_paramE "bk_ble_gatts_cb_param_t::gatts_stop_evt_param") stop[](#_CPPv4N23bk_ble_gatts_cb_param_t4stopE "永久链接至目标")
    :   Gatt server callback param of BK_GATTS_STOP_EVT

    struct [bk_ble_gatts_cb_param_t](#_CPPv423bk_ble_gatts_cb_param_t "bk_ble_gatts_cb_param_t")::[gatts_connect_evt_param](#_CPPv4N23bk_ble_gatts_cb_param_t23gatts_connect_evt_paramE "bk_ble_gatts_cb_param_t::gatts_connect_evt_param") connect[](#_CPPv4N23bk_ble_gatts_cb_param_t7connectE "永久链接至目标")
    :   Gatt server callback param of BK_GATTS_CONNECT_EVT

    struct [bk_ble_gatts_cb_param_t](#_CPPv423bk_ble_gatts_cb_param_t "bk_ble_gatts_cb_param_t")::[gatts_disconnect_evt_param](#_CPPv4N23bk_ble_gatts_cb_param_t26gatts_disconnect_evt_paramE "bk_ble_gatts_cb_param_t::gatts_disconnect_evt_param") disconnect[](#_CPPv4N23bk_ble_gatts_cb_param_t10disconnectE "永久链接至目标")
    :   Gatt server callback param of BK_GATTS_DISCONNECT_EVT

    struct [bk_ble_gatts_cb_param_t](#_CPPv423bk_ble_gatts_cb_param_t "bk_ble_gatts_cb_param_t")::[gatts_rsp_evt_param](#_CPPv4N23bk_ble_gatts_cb_param_t19gatts_rsp_evt_paramE "bk_ble_gatts_cb_param_t::gatts_rsp_evt_param") rsp[](#_CPPv4N23bk_ble_gatts_cb_param_t3rspE "永久链接至目标")
    :   Gatt server callback param of BK_GATTS_RESPONSE_EVT

    struct [bk_ble_gatts_cb_param_t](#_CPPv423bk_ble_gatts_cb_param_t "bk_ble_gatts_cb_param_t")::[gatts_add_attr_tab_evt_param](#_CPPv4N23bk_ble_gatts_cb_param_t28gatts_add_attr_tab_evt_paramE "bk_ble_gatts_cb_param_t::gatts_add_attr_tab_evt_param") add_attr_tab[](#_CPPv4N23bk_ble_gatts_cb_param_t12add_attr_tabE "永久链接至目标")
    :   Gatt server callback param of BK_GATTS_CREAT_ATTR_TAB_EVT

    struct [bk_ble_gatts_cb_param_t](#_CPPv423bk_ble_gatts_cb_param_t "bk_ble_gatts_cb_param_t")::[gatts_set_attr_val_evt_param](#_CPPv4N23bk_ble_gatts_cb_param_t28gatts_set_attr_val_evt_paramE "bk_ble_gatts_cb_param_t::gatts_set_attr_val_evt_param") set_attr_val[](#_CPPv4N23bk_ble_gatts_cb_param_t12set_attr_valE "永久链接至目标")
    :   Gatt server callback param of BK_GATTS_SET_ATTR_VAL_EVT

    struct [bk_ble_gatts_cb_param_t](#_CPPv423bk_ble_gatts_cb_param_t "bk_ble_gatts_cb_param_t")::[gatts_send_service_change_evt_param](#_CPPv4N23bk_ble_gatts_cb_param_t35gatts_send_service_change_evt_paramE "bk_ble_gatts_cb_param_t::gatts_send_service_change_evt_param") service_change[](#_CPPv4N23bk_ble_gatts_cb_param_t14service_changeE "永久链接至目标")
    :   Gatt server callback param of BK_GATTS_SEND_SERVICE_CHANGE_EVT

    struct gatts_add_attr_tab_evt_param[](#_CPPv4N23bk_ble_gatts_cb_param_t28gatts_add_attr_tab_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gatts.h>*

        BK_GATTS_CREAT_ATTR_TAB_EVT.

        Public Members

        [bk_gatt_status_t](#_CPPv416bk_gatt_status_t "bk_gatt_status_t") status[](#_CPPv4N23bk_ble_gatts_cb_param_t28gatts_add_attr_tab_evt_param6statusE "永久链接至目标")
        :   Operation status

        [bk_bt_uuid_t](#_CPPv412bk_bt_uuid_t "bk_bt_uuid_t") svc_uuid[](#_CPPv4N23bk_ble_gatts_cb_param_t28gatts_add_attr_tab_evt_param8svc_uuidE "永久链接至目标")
        :   Service uuid type

        uint16_t num_handle[](#_CPPv4N23bk_ble_gatts_cb_param_t28gatts_add_attr_tab_evt_param10num_handleE "永久链接至目标")
        :   The number of the attribute handle to be added to the gatts database

        uint16_t *handles[](#_CPPv4N23bk_ble_gatts_cb_param_t28gatts_add_attr_tab_evt_param7handlesE "永久链接至目标")
        :   The number to the handles

    struct gatts_add_char_descr_evt_param[](#_CPPv4N23bk_ble_gatts_cb_param_t30gatts_add_char_descr_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gatts.h>*

        BK_GATTS_ADD_CHAR_DESCR_EVT.

        Public Members

        [bk_gatt_status_t](#_CPPv416bk_gatt_status_t "bk_gatt_status_t") status[](#_CPPv4N23bk_ble_gatts_cb_param_t30gatts_add_char_descr_evt_param6statusE "永久链接至目标")
        :   Operation status

        uint16_t attr_handle[](#_CPPv4N23bk_ble_gatts_cb_param_t30gatts_add_char_descr_evt_param11attr_handleE "永久链接至目标")
        :   Descriptor attribute handle

        uint16_t service_handle[](#_CPPv4N23bk_ble_gatts_cb_param_t30gatts_add_char_descr_evt_param14service_handleE "永久链接至目标")
        :   Service attribute handle

        [bk_bt_uuid_t](#_CPPv412bk_bt_uuid_t "bk_bt_uuid_t") descr_uuid[](#_CPPv4N23bk_ble_gatts_cb_param_t30gatts_add_char_descr_evt_param10descr_uuidE "永久链接至目标")
        :   Characteristic descriptor uuid

    struct gatts_add_char_evt_param[](#_CPPv4N23bk_ble_gatts_cb_param_t24gatts_add_char_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gatts.h>*

        BK_GATTS_ADD_CHAR_EVT.

        Public Members

        [bk_gatt_status_t](#_CPPv416bk_gatt_status_t "bk_gatt_status_t") status[](#_CPPv4N23bk_ble_gatts_cb_param_t24gatts_add_char_evt_param6statusE "永久链接至目标")
        :   Operation status

        uint16_t attr_handle[](#_CPPv4N23bk_ble_gatts_cb_param_t24gatts_add_char_evt_param11attr_handleE "永久链接至目标")
        :   Characteristic attribute handle

        uint16_t service_handle[](#_CPPv4N23bk_ble_gatts_cb_param_t24gatts_add_char_evt_param14service_handleE "永久链接至目标")
        :   Service attribute handle

        [bk_bt_uuid_t](#_CPPv412bk_bt_uuid_t "bk_bt_uuid_t") char_uuid[](#_CPPv4N23bk_ble_gatts_cb_param_t24gatts_add_char_evt_param9char_uuidE "永久链接至目标")
        :   Characteristic uuid

    struct gatts_conf_evt_param[](#_CPPv4N23bk_ble_gatts_cb_param_t20gatts_conf_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gatts.h>*

        BK_GATTS_CONF_EVT.

        Public Members

        [bk_gatt_status_t](#_CPPv416bk_gatt_status_t "bk_gatt_status_t") status[](#_CPPv4N23bk_ble_gatts_cb_param_t20gatts_conf_evt_param6statusE "永久链接至目标")
        :   Operation status

        uint16_t conn_id[](#_CPPv4N23bk_ble_gatts_cb_param_t20gatts_conf_evt_param7conn_idE "永久链接至目标")
        :   Connection id

        uint16_t handle[](#_CPPv4N23bk_ble_gatts_cb_param_t20gatts_conf_evt_param6handleE "永久链接至目标")
        :   attribute handle. Not used when send indicate

        uint16_t len[](#_CPPv4N23bk_ble_gatts_cb_param_t20gatts_conf_evt_param3lenE "永久链接至目标")
        :   The indication or notification value length, len is valid when send notification or indication failed. Not used when indicate

        uint8_t *value[](#_CPPv4N23bk_ble_gatts_cb_param_t20gatts_conf_evt_param5valueE "永久链接至目标")
        :   The indication or notification value , value is valid when send notification or indication failed. Not used when indicate

    struct gatts_connect_evt_param[](#_CPPv4N23bk_ble_gatts_cb_param_t23gatts_connect_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gatts.h>*

        BK_GATTS_CONNECT_EVT.

        Public Members

        uint16_t conn_id[](#_CPPv4N23bk_ble_gatts_cb_param_t23gatts_connect_evt_param7conn_idE "永久链接至目标")
        :   Connection id

        uint8_t link_role[](#_CPPv4N23bk_ble_gatts_cb_param_t23gatts_connect_evt_param9link_roleE "永久链接至目标")
        :   Link role : master role = 0 ; slave role = 1

        [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") remote_bda[](#_CPPv4N23bk_ble_gatts_cb_param_t23gatts_connect_evt_param10remote_bdaE "永久链接至目标")
        :   Remote bluetooth device address

        [bk_gatt_conn_params_t](#_CPPv421bk_gatt_conn_params_t "bk_gatt_conn_params_t") conn_params[](#_CPPv4N23bk_ble_gatts_cb_param_t23gatts_connect_evt_param11conn_paramsE "永久链接至目标")
        :   current Connection parameters. Not used now

    struct gatts_create_evt_param[](#_CPPv4N23bk_ble_gatts_cb_param_t22gatts_create_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gatts.h>*

        BK_GATTS_UNREG_EVT.

        BK_GATTS_CREATE_EVT

        Public Members

        [bk_gatt_status_t](#_CPPv416bk_gatt_status_t "bk_gatt_status_t") status[](#_CPPv4N23bk_ble_gatts_cb_param_t22gatts_create_evt_param6statusE "永久链接至目标")
        :   Operation status

        uint16_t service_handle[](#_CPPv4N23bk_ble_gatts_cb_param_t22gatts_create_evt_param14service_handleE "永久链接至目标")
        :   Service attribute handle

        [bk_gatt_srvc_id_t](#_CPPv417bk_gatt_srvc_id_t "bk_gatt_srvc_id_t") service_id[](#_CPPv4N23bk_ble_gatts_cb_param_t22gatts_create_evt_param10service_idE "永久链接至目标")
        :   Service id, include service uuid and other information

    struct gatts_disconnect_evt_param[](#_CPPv4N23bk_ble_gatts_cb_param_t26gatts_disconnect_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gatts.h>*

        BK_GATTS_DISCONNECT_EVT.

        Public Members

        [bk_gatt_conn_reason_t](#_CPPv421bk_gatt_conn_reason_t "bk_gatt_conn_reason_t") reason[](#_CPPv4N23bk_ble_gatts_cb_param_t26gatts_disconnect_evt_param6reasonE "永久链接至目标")
        :   The reason of gatt connection close

        uint16_t conn_id[](#_CPPv4N23bk_ble_gatts_cb_param_t26gatts_disconnect_evt_param7conn_idE "永久链接至目标")
        :   Connection id

        [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") remote_bda[](#_CPPv4N23bk_ble_gatts_cb_param_t26gatts_disconnect_evt_param10remote_bdaE "永久链接至目标")
        :   Remote bluetooth device address

    struct gatts_exec_write_evt_param[](#_CPPv4N23bk_ble_gatts_cb_param_t26gatts_exec_write_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gatts.h>*

        BK_GATTS_EXEC_WRITE_EVT.

        Public Members

        uint16_t conn_id[](#_CPPv4N23bk_ble_gatts_cb_param_t26gatts_exec_write_evt_param7conn_idE "永久链接至目标")
        :   Connection id

        uint32_t trans_id[](#_CPPv4N23bk_ble_gatts_cb_param_t26gatts_exec_write_evt_param8trans_idE "永久链接至目标")
        :   Transaction id

        [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bda[](#_CPPv4N23bk_ble_gatts_cb_param_t26gatts_exec_write_evt_param3bdaE "永久链接至目标")
        :   The bluetooth device address which been written

        uint8_t exec_write_flag[](#_CPPv4N23bk_ble_gatts_cb_param_t26gatts_exec_write_evt_param15exec_write_flagE "永久链接至目标")
        :   Execute write flag

        bool need_rsp[](#_CPPv4N23bk_ble_gatts_cb_param_t26gatts_exec_write_evt_param8need_rspE "永久链接至目标")

    struct gatts_mtu_evt_param[](#_CPPv4N23bk_ble_gatts_cb_param_t19gatts_mtu_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gatts.h>*

        BK_GATTS_MTU_EVT.

        Public Members

        uint16_t conn_id[](#_CPPv4N23bk_ble_gatts_cb_param_t19gatts_mtu_evt_param7conn_idE "永久链接至目标")
        :   Connection id

        uint16_t mtu[](#_CPPv4N23bk_ble_gatts_cb_param_t19gatts_mtu_evt_param3mtuE "永久链接至目标")
        :   MTU size

    struct gatts_read_evt_param[](#_CPPv4N23bk_ble_gatts_cb_param_t20gatts_read_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gatts.h>*

        BK_GATTS_READ_EVT.

        Public Members

        uint16_t conn_id[](#_CPPv4N23bk_ble_gatts_cb_param_t20gatts_read_evt_param7conn_idE "永久链接至目标")
        :   Connection id

        uint32_t trans_id[](#_CPPv4N23bk_ble_gatts_cb_param_t20gatts_read_evt_param8trans_idE "永久链接至目标")
        :   Transaction id

        [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bda[](#_CPPv4N23bk_ble_gatts_cb_param_t20gatts_read_evt_param3bdaE "永久链接至目标")
        :   The bluetooth device address which been read

        uint16_t handle[](#_CPPv4N23bk_ble_gatts_cb_param_t20gatts_read_evt_param6handleE "永久链接至目标")
        :   The attribute handle

        uint16_t offset[](#_CPPv4N23bk_ble_gatts_cb_param_t20gatts_read_evt_param6offsetE "永久链接至目标")
        :   Offset of the value, if the value is too long

        bool is_long[](#_CPPv4N23bk_ble_gatts_cb_param_t20gatts_read_evt_param7is_longE "永久链接至目标")
        :   The value is too long or not

        bool need_rsp[](#_CPPv4N23bk_ble_gatts_cb_param_t20gatts_read_evt_param8need_rspE "永久链接至目标")
        :   The read operation need to do response

    struct gatts_reg_evt_param[](#_CPPv4N23bk_ble_gatts_cb_param_t19gatts_reg_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gatts.h>*

        BK_GATTS_REG_EVT.

        Public Members

        [bk_gatt_status_t](#_CPPv416bk_gatt_status_t "bk_gatt_status_t") status[](#_CPPv4N23bk_ble_gatts_cb_param_t19gatts_reg_evt_param6statusE "永久链接至目标")
        :   Operation status

        uint16_t app_id[](#_CPPv4N23bk_ble_gatts_cb_param_t19gatts_reg_evt_param6app_idE "永久链接至目标")
        :   Application id which input in register API, not used now

        [bk_gatt_if_t](#_CPPv412bk_gatt_if_t "bk_gatt_if_t") gatt_if[](#_CPPv4N23bk_ble_gatts_cb_param_t19gatts_reg_evt_param7gatt_ifE "永久链接至目标")

    struct gatts_rsp_evt_param[](#_CPPv4N23bk_ble_gatts_cb_param_t19gatts_rsp_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gatts.h>*

        BK_GATTS_RESPONSE_EVT.

        Public Members

        [bk_gatt_status_t](#_CPPv416bk_gatt_status_t "bk_gatt_status_t") status[](#_CPPv4N23bk_ble_gatts_cb_param_t19gatts_rsp_evt_param6statusE "永久链接至目标")
        :   Operation status

        uint16_t handle[](#_CPPv4N23bk_ble_gatts_cb_param_t19gatts_rsp_evt_param6handleE "永久链接至目标")
        :   Attribute handle which send response

        uint16_t conn_id[](#_CPPv4N23bk_ble_gatts_cb_param_t19gatts_rsp_evt_param7conn_idE "永久链接至目标")
        :   Connection id

        [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") remote_bda[](#_CPPv4N23bk_ble_gatts_cb_param_t19gatts_rsp_evt_param10remote_bdaE "永久链接至目标")
        :   Remote bluetooth device address

    struct gatts_send_service_change_evt_param[](#_CPPv4N23bk_ble_gatts_cb_param_t35gatts_send_service_change_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gatts.h>*

        BK_GATTS_SEND_SERVICE_CHANGE_EVT.

        Public Members

        [bk_gatt_status_t](#_CPPv416bk_gatt_status_t "bk_gatt_status_t") status[](#_CPPv4N23bk_ble_gatts_cb_param_t35gatts_send_service_change_evt_param6statusE "永久链接至目标")
        :   Operation status

        uint16_t conn_id[](#_CPPv4N23bk_ble_gatts_cb_param_t35gatts_send_service_change_evt_param7conn_idE "永久链接至目标")
        :   Connection id

        [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") remote_bda[](#_CPPv4N23bk_ble_gatts_cb_param_t35gatts_send_service_change_evt_param10remote_bdaE "永久链接至目标")
        :   Remote bluetooth device address

    struct gatts_set_attr_val_evt_param[](#_CPPv4N23bk_ble_gatts_cb_param_t28gatts_set_attr_val_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gatts.h>*

        BK_GATTS_SET_ATTR_VAL_EVT.

        Public Members

        uint16_t srvc_handle[](#_CPPv4N23bk_ble_gatts_cb_param_t28gatts_set_attr_val_evt_param11srvc_handleE "永久链接至目标")
        :   The service handle

        uint16_t attr_handle[](#_CPPv4N23bk_ble_gatts_cb_param_t28gatts_set_attr_val_evt_param11attr_handleE "永久链接至目标")
        :   The attribute handle

        [bk_gatt_status_t](#_CPPv416bk_gatt_status_t "bk_gatt_status_t") status[](#_CPPv4N23bk_ble_gatts_cb_param_t28gatts_set_attr_val_evt_param6statusE "永久链接至目标")
        :   Operation status

    struct gatts_start_evt_param[](#_CPPv4N23bk_ble_gatts_cb_param_t21gatts_start_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gatts.h>*

        BK_GATTS_START_EVT.

        Public Members

        [bk_gatt_status_t](#_CPPv416bk_gatt_status_t "bk_gatt_status_t") status[](#_CPPv4N23bk_ble_gatts_cb_param_t21gatts_start_evt_param6statusE "永久链接至目标")
        :   Operation status

        uint16_t service_handle[](#_CPPv4N23bk_ble_gatts_cb_param_t21gatts_start_evt_param14service_handleE "永久链接至目标")
        :   Service attribute handle

    struct gatts_stop_evt_param[](#_CPPv4N23bk_ble_gatts_cb_param_t20gatts_stop_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gatts.h>*

        BK_GATTS_STOP_EVT.

        Public Members

        [bk_gatt_status_t](#_CPPv416bk_gatt_status_t "bk_gatt_status_t") status[](#_CPPv4N23bk_ble_gatts_cb_param_t20gatts_stop_evt_param6statusE "永久链接至目标")
        :   Operation status

        uint16_t service_handle[](#_CPPv4N23bk_ble_gatts_cb_param_t20gatts_stop_evt_param14service_handleE "永久链接至目标")
        :   Service attribute handle

    struct gatts_write_evt_param[](#_CPPv4N23bk_ble_gatts_cb_param_t21gatts_write_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gatts.h>*

        BK_GATTS_WRITE_EVT.

        Public Members

        uint16_t conn_id[](#_CPPv4N23bk_ble_gatts_cb_param_t21gatts_write_evt_param7conn_idE "永久链接至目标")
        :   Connection id

        uint32_t trans_id[](#_CPPv4N23bk_ble_gatts_cb_param_t21gatts_write_evt_param8trans_idE "永久链接至目标")
        :   Transaction id

        [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bda[](#_CPPv4N23bk_ble_gatts_cb_param_t21gatts_write_evt_param3bdaE "永久链接至目标")
        :   The bluetooth device address which been written

        uint16_t handle[](#_CPPv4N23bk_ble_gatts_cb_param_t21gatts_write_evt_param6handleE "永久链接至目标")
        :   The attribute handle

        uint16_t offset[](#_CPPv4N23bk_ble_gatts_cb_param_t21gatts_write_evt_param6offsetE "永久链接至目标")
        :   Offset of the value, if the value is too long

        bool need_rsp[](#_CPPv4N23bk_ble_gatts_cb_param_t21gatts_write_evt_param8need_rspE "永久链接至目标")
        :   The write operation need to do response

        bool is_prep[](#_CPPv4N23bk_ble_gatts_cb_param_t21gatts_write_evt_param7is_prepE "永久链接至目标")
        :   This write operation is prepare write

        uint16_t len[](#_CPPv4N23bk_ble_gatts_cb_param_t21gatts_write_evt_param3lenE "永久链接至目标")
        :   The write attribute value length

        uint8_t *value[](#_CPPv4N23bk_ble_gatts_cb_param_t21gatts_write_evt_param5valueE "永久链接至目标")
        :   The write attribute value


### Macros[](#macros "永久链接至标题")

BK_GATT_PREP_WRITE_CANCEL[](#c.BK_GATT_PREP_WRITE_CANCEL "永久链接至目标")
:   Prepare write flag to indicate cancel prepare write

BK_GATT_PREP_WRITE_EXEC[](#c.BK_GATT_PREP_WRITE_EXEC "永久链接至目标")
:   Prepare write flag to indicate execute prepare write


### Type Definitions[](#id6 "永久链接至标题")

typedef int32_t (*bk_gatts_cb_t)([bk_gatts_cb_event_t](#_CPPv419bk_gatts_cb_event_t "bk_gatts_cb_event_t") event, [bk_gatt_if_t](#_CPPv412bk_gatt_if_t "bk_gatt_if_t") gatts_if, [bk_ble_gatts_cb_param_t](#_CPPv423bk_ble_gatts_cb_param_t "bk_ble_gatts_cb_param_t") *param)[](#_CPPv413bk_gatts_cb_t "永久链接至目标")
:   GATT Server callback function type.

    Param event
    :   : Event type

    Param gatts_if
    :   : GATT server access interface, normally different gatts_if correspond to different profile

    Param param
    :   : Point to callback parameter, currently is union type


### Enumerations[](#id7 "永久链接至标题")

enum bk_gatts_cb_event_t[](#_CPPv419bk_gatts_cb_event_t "永久链接至目标")
:   GATT Server callback function events.


    *Values:*

    enumerator BK_GATTS_REG_EVT[](#_CPPv4N19bk_gatts_cb_event_t16BK_GATTS_REG_EVTE "永久链接至目标")
    :   When register application id, the event comes

    enumerator BK_GATTS_READ_EVT[](#_CPPv4N19bk_gatts_cb_event_t17BK_GATTS_READ_EVTE "永久链接至目标")
    :   When gatt client request read operation, the event comes

    enumerator BK_GATTS_WRITE_EVT[](#_CPPv4N19bk_gatts_cb_event_t18BK_GATTS_WRITE_EVTE "永久链接至目标")
    :   When gatt client request write operation, the event comes

    enumerator BK_GATTS_EXEC_WRITE_EVT[](#_CPPv4N19bk_gatts_cb_event_t23BK_GATTS_EXEC_WRITE_EVTE "永久链接至目标")
    :   When gatt client request execute write, the event comes

    enumerator BK_GATTS_MTU_EVT[](#_CPPv4N19bk_gatts_cb_event_t16BK_GATTS_MTU_EVTE "永久链接至目标")
    :   When set mtu complete, the event comes

    enumerator BK_GATTS_CONF_EVT[](#_CPPv4N19bk_gatts_cb_event_t17BK_GATTS_CONF_EVTE "永久链接至目标")
    :   When receive confirm after send notify or indicate, the event comes

    enumerator BK_GATTS_UNREG_EVT[](#_CPPv4N19bk_gatts_cb_event_t18BK_GATTS_UNREG_EVTE "永久链接至目标")
    :   When unregister gatt_if, the event comes

    enumerator BK_GATTS_CREATE_EVT[](#_CPPv4N19bk_gatts_cb_event_t19BK_GATTS_CREATE_EVTE "永久链接至目标")
    :   When create service complete, the event comes

    enumerator BK_GATTS_ADD_CHAR_EVT[](#_CPPv4N19bk_gatts_cb_event_t21BK_GATTS_ADD_CHAR_EVTE "永久链接至目标")
    :   When add characteristic complete, the event comes

    enumerator BK_GATTS_ADD_CHAR_DESCR_EVT[](#_CPPv4N19bk_gatts_cb_event_t27BK_GATTS_ADD_CHAR_DESCR_EVTE "永久链接至目标")
    :   When add descriptor complete, the event comes

    enumerator BK_GATTS_START_EVT[](#_CPPv4N19bk_gatts_cb_event_t18BK_GATTS_START_EVTE "永久链接至目标")
    :   When start service complete, the event comes

    enumerator BK_GATTS_STOP_EVT[](#_CPPv4N19bk_gatts_cb_event_t17BK_GATTS_STOP_EVTE "永久链接至目标")
    :   When stop service complete, the event comes

    enumerator BK_GATTS_CONNECT_EVT[](#_CPPv4N19bk_gatts_cb_event_t20BK_GATTS_CONNECT_EVTE "永久链接至目标")
    :   When gatt client connect, the event comes

    enumerator BK_GATTS_DISCONNECT_EVT[](#_CPPv4N19bk_gatts_cb_event_t23BK_GATTS_DISCONNECT_EVTE "永久链接至目标")
    :   When gatt client disconnect, the event comes

    enumerator BK_GATTS_RESPONSE_EVT[](#_CPPv4N19bk_gatts_cb_event_t21BK_GATTS_RESPONSE_EVTE "永久链接至目标")
    :   When gatt send write/read/error response complete, the event comes

    enumerator BK_GATTS_CREAT_ATTR_TAB_EVT[](#_CPPv4N19bk_gatts_cb_event_t27BK_GATTS_CREAT_ATTR_TAB_EVTE "永久链接至目标")
    :   When gatt create table complete, the event comes

    enumerator BK_GATTS_SET_ATTR_VAL_EVT[](#_CPPv4N19bk_gatts_cb_event_t25BK_GATTS_SET_ATTR_VAL_EVTE "永久链接至目标")
    :   When gatt set attr value complete, the event comes

    enumerator BK_GATTS_SEND_SERVICE_CHANGE_EVT[](#_CPPv4N19bk_gatts_cb_event_t32BK_GATTS_SEND_SERVICE_CHANGE_EVTE "永久链接至目标")
    :   When gatt send service change indication complete, the event comes

enum bk_gatts_char_property_bit_mask_op_t[](#_CPPv436bk_gatts_char_property_bit_mask_op_t "永久链接至目标")
:   *Values:*

    enumerator BK_GATTS_CHAR_PROPERTY_BIT_MASK_OP_GET[](#_CPPv4N36bk_gatts_char_property_bit_mask_op_t38BK_GATTS_CHAR_PROPERTY_BIT_MASK_OP_GETE "永久链接至目标")

    enumerator BK_GATTS_CHAR_PROPERTY_BIT_MASK_OP_SET[](#_CPPv4N36bk_gatts_char_property_bit_mask_op_t38BK_GATTS_CHAR_PROPERTY_BIT_MASK_OP_SETE "永久链接至目标")


### Header File[](#id8 "永久链接至标题")


- [bluetooth/bk_dm_gatt_common.h](https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_gatt_common.h "https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_gatt_common.h")


### Functions[](#id9 "永久链接至标题")

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_gatt_set_local_mtu(uint16_t mtu)[](#_CPPv425bk_ble_gatt_set_local_mtu8uint16_t "永久链接至目标")
:   This function is called to set local MTU, the function is called before BLE connection.

    参数
    :   **mtu** – **[in]** the size of MTU. Max is 517, min is 23

    返回
    :   - BK_ERR_BLE_SUCCESS: success

        - other: failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_get_hci_handle_from_gatt_conn_id(uint16_t gatt_conn_id, uint16_t *hci_handle)[](#_CPPv439bk_ble_get_hci_handle_from_gatt_conn_id8uint16_tP8uint16_t "永久链接至目标")
:   This function is use to get hci_handle from gatt conn id,.


    **Attention**
    :   1. This function only could be used when connection exist.

    参数
    :   - **gatt_conn_id** – **[in]** id from gatts_connect_evt_param/gattc_connect_evt_param

        - **[in|out]** – hci_handle: output hci handle

    返回
    :   - BK_ERR_BLE_SUCCESS: success

        - other: failed

[ble_err_t](single_ble.md#_CPPv49ble_err_t "ble_err_t") bk_ble_get_gatt_conn_id_from_hci_handle(uint16_t hci_handle, uint16_t *gatt_conn_id)[](#_CPPv439bk_ble_get_gatt_conn_id_from_hci_handle8uint16_tP8uint16_t "永久链接至目标")
:   This function is use to get gatt conn id from hci_handle,.


    **Attention**
    :   1. This function only could be used when connection exist.

    参数
    :   - **hci_handle** – **[in]** hci handle from BK_BLE_GAP_CONNECT_COMPLETE_EVT

        - **[in|out]** – gatt_conn_id: output gatt conn id

    返回
    :   - BK_ERR_BLE_SUCCESS: success

        - other: failed


## API Typedefs[](#api-typedefs "永久链接至标题")


### Header File[](#id10 "永久链接至标题")


- [bluetooth/bk_dm_gap_ble_types.h](https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_gap_ble_types.h "https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_gap_ble_types.h")


### Unions[](#id11 "永久链接至标题")

union bk_ble_key_value_t[](#_CPPv418bk_ble_key_value_t "永久链接至目标")
:   *#include <bk_dm_gap_ble_types.h>*

    union type of the security key value

    Public Members

    [bk_ble_penc_keys_t](#_CPPv418bk_ble_penc_keys_t "bk_ble_penc_keys_t") penc_key[](#_CPPv4N18bk_ble_key_value_t8penc_keyE "永久链接至目标")
    :   received peer encryption key

    [bk_ble_pcsrk_keys_t](#_CPPv419bk_ble_pcsrk_keys_t "bk_ble_pcsrk_keys_t") pcsrk_key[](#_CPPv4N18bk_ble_key_value_t9pcsrk_keyE "永久链接至目标")
    :   received peer device SRK

    [bk_ble_pid_keys_t](#_CPPv417bk_ble_pid_keys_t "bk_ble_pid_keys_t") pid_key[](#_CPPv4N18bk_ble_key_value_t7pid_keyE "永久链接至目标")
    :   peer device ID key

    [bk_ble_lenc_keys_t](#_CPPv418bk_ble_lenc_keys_t "bk_ble_lenc_keys_t") lenc_key[](#_CPPv4N18bk_ble_key_value_t8lenc_keyE "永久链接至目标")
    :   local encryption reproduction keys LTK = = d1(ER,DIV,0)

    [bk_ble_lcsrk_keys_t](#_CPPv419bk_ble_lcsrk_keys_t "bk_ble_lcsrk_keys_t") lcsrk_key[](#_CPPv4N18bk_ble_key_value_t9lcsrk_keyE "永久链接至目标")
    :   local device CSRK = d1(ER,DIV,1)

union bk_ble_sec_t[](#_CPPv412bk_ble_sec_t "永久链接至目标")
:   *#include <bk_dm_gap_ble_types.h>*

    union associated with ble security

    Public Members

    [bk_ble_sec_key_notif_t](#_CPPv422bk_ble_sec_key_notif_t "bk_ble_sec_key_notif_t") key_notif[](#_CPPv4N12bk_ble_sec_t9key_notifE "永久链接至目标")
    :   passkey notification/req or number compare notification

    [bk_ble_sec_req_t](#_CPPv416bk_ble_sec_req_t "bk_ble_sec_req_t") ble_req[](#_CPPv4N12bk_ble_sec_t7ble_reqE "永久链接至目标")
    :   BLE SMP related request

    [bk_ble_local_keys_t](#_CPPv419bk_ble_local_keys_t "bk_ble_local_keys_t") ble_local_keys[](#_CPPv4N12bk_ble_sec_t14ble_local_keysE "永久链接至目标")
    :   BLE local event

    [bk_ble_auth_cmpl_t](#_CPPv418bk_ble_auth_cmpl_t "bk_ble_auth_cmpl_t") auth_cmpl[](#_CPPv4N12bk_ble_sec_t9auth_cmplE "永久链接至目标")
    :   Authentication complete indication.

union bk_ble_gap_cb_param_t[](#_CPPv421bk_ble_gap_cb_param_t "永久链接至目标")
:   *#include <bk_dm_gap_ble_types.h>*

    Gap callback parameters union.

    Public Members

    [bk_ble_sec_t](#_CPPv412bk_ble_sec_t "bk_ble_sec_t") ble_security[](#_CPPv4N21bk_ble_gap_cb_param_t12ble_securityE "永久链接至目标")
    :   ble gap security union type

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_set_rand_cmpl_evt_param](#_CPPv4N21bk_ble_gap_cb_param_t27ble_set_rand_cmpl_evt_paramE "bk_ble_gap_cb_param_t::ble_set_rand_cmpl_evt_param") set_rand_addr_cmpl[](#_CPPv4N21bk_ble_gap_cb_param_t18set_rand_addr_cmplE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_SET_STATIC_RAND_ADDR_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_update_conn_params_evt_param](#_CPPv4N21bk_ble_gap_cb_param_t32ble_update_conn_params_evt_paramE "bk_ble_gap_cb_param_t::ble_update_conn_params_evt_param") update_conn_params[](#_CPPv4N21bk_ble_gap_cb_param_t18update_conn_paramsE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_UPDATE_CONN_PARAMS_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_pkt_data_length_cmpl_evt_param](#_CPPv4N21bk_ble_gap_cb_param_t34ble_pkt_data_length_cmpl_evt_paramE "bk_ble_gap_cb_param_t::ble_pkt_data_length_cmpl_evt_param") pkt_data_length_cmpl[](#_CPPv4N21bk_ble_gap_cb_param_t20pkt_data_length_cmplE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_SET_PKT_LENGTH_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_local_privacy_cmpl_evt_param](#_CPPv4N21bk_ble_gap_cb_param_t32ble_local_privacy_cmpl_evt_paramE "bk_ble_gap_cb_param_t::ble_local_privacy_cmpl_evt_param") local_privacy_cmpl[](#_CPPv4N21bk_ble_gap_cb_param_t18local_privacy_cmplE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_SET_LOCAL_PRIVACY_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_bond_dev_key_req_evt_param](#_CPPv4N21bk_ble_gap_cb_param_t30ble_bond_dev_key_req_evt_paramE "bk_ble_gap_cb_param_t::ble_bond_dev_key_req_evt_param") bond_key_req_evt[](#_CPPv4N21bk_ble_gap_cb_param_t16bond_key_req_evtE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_BOND_KEY_REQ_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_bond_dev_key_evt_param](#_CPPv4N21bk_ble_gap_cb_param_t26ble_bond_dev_key_evt_paramE "bk_ble_gap_cb_param_t::ble_bond_dev_key_evt_param") bond_dev_key_generate_evt[](#_CPPv4N21bk_ble_gap_cb_param_t25bond_dev_key_generate_evtE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_BOND_KEY_GENERATE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_bond_dev_list_evt_param](#_CPPv4N21bk_ble_gap_cb_param_t27ble_bond_dev_list_evt_paramE "bk_ble_gap_cb_param_t::ble_bond_dev_list_evt_param") bond_dev_list_op_cmpl[](#_CPPv4N21bk_ble_gap_cb_param_t21bond_dev_list_op_cmplE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_BOND_DEV_LIST_OPERATEION_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_read_rssi_cmpl_evt_param](#_CPPv4N21bk_ble_gap_cb_param_t28ble_read_rssi_cmpl_evt_paramE "bk_ble_gap_cb_param_t::ble_read_rssi_cmpl_evt_param") read_rssi_cmpl[](#_CPPv4N21bk_ble_gap_cb_param_t14read_rssi_cmplE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_READ_RSSI_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_update_whitelist_cmpl_evt_param](#_CPPv4N21bk_ble_gap_cb_param_t35ble_update_whitelist_cmpl_evt_paramE "bk_ble_gap_cb_param_t::ble_update_whitelist_cmpl_evt_param") update_whitelist_cmpl[](#_CPPv4N21bk_ble_gap_cb_param_t21update_whitelist_cmplE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_UPDATE_WHITELIST_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_set_channels_cmpl_evt_param](#_CPPv4N21bk_ble_gap_cb_param_t31ble_set_channels_cmpl_evt_paramE "bk_ble_gap_cb_param_t::ble_set_channels_cmpl_evt_param") ble_set_channels[](#_CPPv4N21bk_ble_gap_cb_param_t16ble_set_channelsE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_SET_CHANNELS_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_read_phy_cmpl_evt_param](#_CPPv4N21bk_ble_gap_cb_param_t27ble_read_phy_cmpl_evt_paramE "bk_ble_gap_cb_param_t::ble_read_phy_cmpl_evt_param") read_phy[](#_CPPv4N21bk_ble_gap_cb_param_t8read_phyE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_READ_PHY_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_set_perf_def_phy_cmpl_evt_param](#_CPPv4N21bk_ble_gap_cb_param_t35ble_set_perf_def_phy_cmpl_evt_paramE "bk_ble_gap_cb_param_t::ble_set_perf_def_phy_cmpl_evt_param") set_perf_def_phy[](#_CPPv4N21bk_ble_gap_cb_param_t16set_perf_def_phyE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_SET_PREFERRED_DEFAULT_PHY_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_set_perf_phy_cmpl_evt_param](#_CPPv4N21bk_ble_gap_cb_param_t31ble_set_perf_phy_cmpl_evt_paramE "bk_ble_gap_cb_param_t::ble_set_perf_phy_cmpl_evt_param") set_perf_phy[](#_CPPv4N21bk_ble_gap_cb_param_t12set_perf_phyE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_SET_PREFERRED_PHY_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_adv_set_rand_addr_cmpl_evt_param](#_CPPv4N21bk_ble_gap_cb_param_t36ble_adv_set_rand_addr_cmpl_evt_paramE "bk_ble_gap_cb_param_t::ble_adv_set_rand_addr_cmpl_evt_param") adv_set_rand_addr[](#_CPPv4N21bk_ble_gap_cb_param_t17adv_set_rand_addrE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_EXT_ADV_SET_RAND_ADDR_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_adv_params_set_cmpl_evt_param](#_CPPv4N21bk_ble_gap_cb_param_t33ble_adv_params_set_cmpl_evt_paramE "bk_ble_gap_cb_param_t::ble_adv_params_set_cmpl_evt_param") adv_params_set[](#_CPPv4N21bk_ble_gap_cb_param_t14adv_params_setE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_EXT_ADV_PARAMS_SET_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_adv_data_set_cmpl_evt_param](#_CPPv4N21bk_ble_gap_cb_param_t31ble_adv_data_set_cmpl_evt_paramE "bk_ble_gap_cb_param_t::ble_adv_data_set_cmpl_evt_param") adv_data_set[](#_CPPv4N21bk_ble_gap_cb_param_t12adv_data_setE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_EXT_ADV_DATA_SET_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_adv_scan_rsp_set_cmpl_evt_param](#_CPPv4N21bk_ble_gap_cb_param_t35ble_adv_scan_rsp_set_cmpl_evt_paramE "bk_ble_gap_cb_param_t::ble_adv_scan_rsp_set_cmpl_evt_param") scan_rsp_data_set[](#_CPPv4N21bk_ble_gap_cb_param_t17scan_rsp_data_setE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_EXT_SCAN_RSP_DATA_SET_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_adv_data_raw_set_cmpl_evt_param](#_CPPv4N21bk_ble_gap_cb_param_t35ble_adv_data_raw_set_cmpl_evt_paramE "bk_ble_gap_cb_param_t::ble_adv_data_raw_set_cmpl_evt_param") adv_data_raw_set[](#_CPPv4N21bk_ble_gap_cb_param_t16adv_data_raw_setE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_EXT_ADV_DATA_SET_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_scan_rsp_data_raw_set_cmpl_evt_param](#_CPPv4N21bk_ble_gap_cb_param_t40ble_scan_rsp_data_raw_set_cmpl_evt_paramE "bk_ble_gap_cb_param_t::ble_scan_rsp_data_raw_set_cmpl_evt_param") scan_rsp_data_raw_set[](#_CPPv4N21bk_ble_gap_cb_param_t21scan_rsp_data_raw_setE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_EXT_SCAN_RSP_DATA_RAW_SET_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_adv_start_cmpl_evt_param](#_CPPv4N21bk_ble_gap_cb_param_t28ble_adv_start_cmpl_evt_paramE "bk_ble_gap_cb_param_t::ble_adv_start_cmpl_evt_param") adv_start[](#_CPPv4N21bk_ble_gap_cb_param_t9adv_startE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_EXT_ADV_START_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_adv_stop_cmpl_evt_param](#_CPPv4N21bk_ble_gap_cb_param_t27ble_adv_stop_cmpl_evt_paramE "bk_ble_gap_cb_param_t::ble_adv_stop_cmpl_evt_param") adv_stop[](#_CPPv4N21bk_ble_gap_cb_param_t8adv_stopE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_EXT_ADV_STOP_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_adv_set_remove_cmpl_evt_param](#_CPPv4N21bk_ble_gap_cb_param_t33ble_adv_set_remove_cmpl_evt_paramE "bk_ble_gap_cb_param_t::ble_adv_set_remove_cmpl_evt_param") adv_remove[](#_CPPv4N21bk_ble_gap_cb_param_t10adv_removeE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_ADV_SET_REMOVE_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_adv_set_clear_cmpl_evt_param](#_CPPv4N21bk_ble_gap_cb_param_t32ble_adv_set_clear_cmpl_evt_paramE "bk_ble_gap_cb_param_t::ble_adv_set_clear_cmpl_evt_param") adv_clear[](#_CPPv4N21bk_ble_gap_cb_param_t9adv_clearE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_ADV_SET_CLEAR_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_periodic_adv_set_params_cmpl_param](#_CPPv4N21bk_ble_gap_cb_param_t38ble_periodic_adv_set_params_cmpl_paramE "bk_ble_gap_cb_param_t::ble_periodic_adv_set_params_cmpl_param") peroid_adv_set_params[](#_CPPv4N21bk_ble_gap_cb_param_t21peroid_adv_set_paramsE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_PERIODIC_ADV_SET_PARAMS_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_periodic_adv_data_set_cmpl_param](#_CPPv4N21bk_ble_gap_cb_param_t36ble_periodic_adv_data_set_cmpl_paramE "bk_ble_gap_cb_param_t::ble_periodic_adv_data_set_cmpl_param") period_adv_data_set[](#_CPPv4N21bk_ble_gap_cb_param_t19period_adv_data_setE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_PERIODIC_ADV_DATA_SET_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_periodic_adv_start_cmpl_param](#_CPPv4N21bk_ble_gap_cb_param_t33ble_periodic_adv_start_cmpl_paramE "bk_ble_gap_cb_param_t::ble_periodic_adv_start_cmpl_param") period_adv_start[](#_CPPv4N21bk_ble_gap_cb_param_t16period_adv_startE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_PERIODIC_ADV_START_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_periodic_adv_stop_cmpl_param](#_CPPv4N21bk_ble_gap_cb_param_t32ble_periodic_adv_stop_cmpl_paramE "bk_ble_gap_cb_param_t::ble_periodic_adv_stop_cmpl_param") period_adv_stop[](#_CPPv4N21bk_ble_gap_cb_param_t15period_adv_stopE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_PERIODIC_ADV_STOP_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_period_adv_create_sync_cmpl_param](#_CPPv4N21bk_ble_gap_cb_param_t37ble_period_adv_create_sync_cmpl_paramE "bk_ble_gap_cb_param_t::ble_period_adv_create_sync_cmpl_param") period_adv_create_sync[](#_CPPv4N21bk_ble_gap_cb_param_t22period_adv_create_syncE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_PERIODIC_ADV_CREATE_SYNC_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_period_adv_sync_cancel_cmpl_param](#_CPPv4N21bk_ble_gap_cb_param_t37ble_period_adv_sync_cancel_cmpl_paramE "bk_ble_gap_cb_param_t::ble_period_adv_sync_cancel_cmpl_param") period_adv_sync_cancel[](#_CPPv4N21bk_ble_gap_cb_param_t22period_adv_sync_cancelE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_PERIODIC_ADV_SYNC_CANCEL_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_period_adv_sync_terminate_cmpl_param](#_CPPv4N21bk_ble_gap_cb_param_t40ble_period_adv_sync_terminate_cmpl_paramE "bk_ble_gap_cb_param_t::ble_period_adv_sync_terminate_cmpl_param") period_adv_sync_term[](#_CPPv4N21bk_ble_gap_cb_param_t20period_adv_sync_termE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_PERIODIC_ADV_SYNC_TERMINATE_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_period_adv_add_dev_cmpl_param](#_CPPv4N21bk_ble_gap_cb_param_t33ble_period_adv_add_dev_cmpl_paramE "bk_ble_gap_cb_param_t::ble_period_adv_add_dev_cmpl_param") period_adv_add_dev[](#_CPPv4N21bk_ble_gap_cb_param_t18period_adv_add_devE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_PERIODIC_ADV_ADD_DEV_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_period_adv_remove_dev_cmpl_param](#_CPPv4N21bk_ble_gap_cb_param_t36ble_period_adv_remove_dev_cmpl_paramE "bk_ble_gap_cb_param_t::ble_period_adv_remove_dev_cmpl_param") period_adv_remove_dev[](#_CPPv4N21bk_ble_gap_cb_param_t21period_adv_remove_devE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_PERIODIC_ADV_REMOVE_DEV_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_period_adv_clear_dev_cmpl_param](#_CPPv4N21bk_ble_gap_cb_param_t35ble_period_adv_clear_dev_cmpl_paramE "bk_ble_gap_cb_param_t::ble_period_adv_clear_dev_cmpl_param") period_adv_clear_dev[](#_CPPv4N21bk_ble_gap_cb_param_t20period_adv_clear_devE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_PERIODIC_ADV_CLEAR_DEV_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_scan_params_set_cmpl_param](#_CPPv4N21bk_ble_gap_cb_param_t30ble_scan_params_set_cmpl_paramE "bk_ble_gap_cb_param_t::ble_scan_params_set_cmpl_param") scan_params_set[](#_CPPv4N21bk_ble_gap_cb_param_t15scan_params_setE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_SCAN_PARAMS_SET_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_scan_start_cmpl_param](#_CPPv4N21bk_ble_gap_cb_param_t25ble_scan_start_cmpl_paramE "bk_ble_gap_cb_param_t::ble_scan_start_cmpl_param") scan_start[](#_CPPv4N21bk_ble_gap_cb_param_t10scan_startE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_SCAN_START_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_scan_stop_cmpl_param](#_CPPv4N21bk_ble_gap_cb_param_t24ble_scan_stop_cmpl_paramE "bk_ble_gap_cb_param_t::ble_scan_stop_cmpl_param") scan_stop[](#_CPPv4N21bk_ble_gap_cb_param_t9scan_stopE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_SCAN_STOP_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_conn_params_set_cmpl_param](#_CPPv4N21bk_ble_gap_cb_param_t30ble_conn_params_set_cmpl_paramE "bk_ble_gap_cb_param_t::ble_conn_params_set_cmpl_param") conn_params_set[](#_CPPv4N21bk_ble_gap_cb_param_t15conn_params_setE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_PREFER_CONN_PARAMS_SET_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_adv_terminate_param](#_CPPv4N21bk_ble_gap_cb_param_t23ble_adv_terminate_paramE "bk_ble_gap_cb_param_t::ble_adv_terminate_param") adv_terminate[](#_CPPv4N21bk_ble_gap_cb_param_t13adv_terminateE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_ADV_TERMINATED_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_scan_req_received_param](#_CPPv4N21bk_ble_gap_cb_param_t27ble_scan_req_received_paramE "bk_ble_gap_cb_param_t::ble_scan_req_received_param") scan_req_received[](#_CPPv4N21bk_ble_gap_cb_param_t17scan_req_receivedE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_SCAN_REQ_RECEIVED_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_channel_sel_alg_param](#_CPPv4N21bk_ble_gap_cb_param_t25ble_channel_sel_alg_paramE "bk_ble_gap_cb_param_t::ble_channel_sel_alg_param") channel_sel_alg[](#_CPPv4N21bk_ble_gap_cb_param_t15channel_sel_algE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_CHANNEL_SELECT_ALGORITHM_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_periodic_adv_sync_lost_param](#_CPPv4N21bk_ble_gap_cb_param_t32ble_periodic_adv_sync_lost_paramE "bk_ble_gap_cb_param_t::ble_periodic_adv_sync_lost_param") periodic_adv_sync_lost[](#_CPPv4N21bk_ble_gap_cb_param_t22periodic_adv_sync_lostE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_PERIODIC_ADV_SYNC_LOST_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_periodic_adv_sync_estab_param](#_CPPv4N21bk_ble_gap_cb_param_t33ble_periodic_adv_sync_estab_paramE "bk_ble_gap_cb_param_t::ble_periodic_adv_sync_estab_param") periodic_adv_sync_estab[](#_CPPv4N21bk_ble_gap_cb_param_t23periodic_adv_sync_estabE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_PERIODIC_ADV_SYNC_ESTAB_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_phy_update_cmpl_param](#_CPPv4N21bk_ble_gap_cb_param_t25ble_phy_update_cmpl_paramE "bk_ble_gap_cb_param_t::ble_phy_update_cmpl_param") phy_update[](#_CPPv4N21bk_ble_gap_cb_param_t10phy_updateE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_PHY_UPDATE_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_ext_adv_report_param](#_CPPv4N21bk_ble_gap_cb_param_t24ble_ext_adv_report_paramE "bk_ble_gap_cb_param_t::ble_ext_adv_report_param") ext_adv_report[](#_CPPv4N21bk_ble_gap_cb_param_t14ext_adv_reportE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_EXT_ADV_REPORT_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_periodic_adv_report_param](#_CPPv4N21bk_ble_gap_cb_param_t29ble_periodic_adv_report_paramE "bk_ble_gap_cb_param_t::ble_periodic_adv_report_param") period_adv_report[](#_CPPv4N21bk_ble_gap_cb_param_t17period_adv_reportE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_PERIODIC_ADV_REPORT_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_connect_complete_param](#_CPPv4N21bk_ble_gap_cb_param_t26ble_connect_complete_paramE "bk_ble_gap_cb_param_t::ble_connect_complete_param") connect_complete[](#_CPPv4N21bk_ble_gap_cb_param_t16connect_completeE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_CONNECT_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_disconnect_complete_param](#_CPPv4N21bk_ble_gap_cb_param_t29ble_disconnect_complete_paramE "bk_ble_gap_cb_param_t::ble_disconnect_complete_param") disconnect_complete[](#_CPPv4N21bk_ble_gap_cb_param_t19disconnect_completeE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_DISCONNECT_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_connect_cancel_param](#_CPPv4N21bk_ble_gap_cb_param_t24ble_connect_cancel_paramE "bk_ble_gap_cb_param_t::ble_connect_cancel_param") connect_cancel[](#_CPPv4N21bk_ble_gap_cb_param_t14connect_cancelE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_CONNECT_CANCEL_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_conntection_update_param_req](#_CPPv4N21bk_ble_gap_cb_param_t32ble_conntection_update_param_reqE "bk_ble_gap_cb_param_t::ble_conntection_update_param_req") update_conn_param_req[](#_CPPv4N21bk_ble_gap_cb_param_t21update_conn_param_reqE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_UPDATE_CONN_PARAMS_REQ_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_set_security_params_cmpl](#_CPPv4N21bk_ble_gap_cb_param_t28ble_set_security_params_cmplE "bk_ble_gap_cb_param_t::ble_set_security_params_cmpl") set_security_params_cmpl[](#_CPPv4N21bk_ble_gap_cb_param_t24set_security_params_cmplE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_SET_SECURITY_PARAMS_COMPLETE_EVT

    struct [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t")::[ble_generate_rpa_cmpl](#_CPPv4N21bk_ble_gap_cb_param_t21ble_generate_rpa_cmplE "bk_ble_gap_cb_param_t::ble_generate_rpa_cmpl") generate_rpa_cmpl[](#_CPPv4N21bk_ble_gap_cb_param_t17generate_rpa_cmplE "永久链接至目标")
    :   Event parameter of BK_BLE_GAP_GENERATE_RPA_COMPLETE_EVT

    struct ble_adv_data_raw_set_cmpl_evt_param[](#_CPPv4N21bk_ble_gap_cb_param_t35ble_adv_data_raw_set_cmpl_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_EXT_ADV_DATA_RAW_SET_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t35ble_adv_data_raw_set_cmpl_evt_param6statusE "永久链接至目标")
        :   Indicate extend advertising data set status

    struct ble_adv_data_set_cmpl_evt_param[](#_CPPv4N21bk_ble_gap_cb_param_t31ble_adv_data_set_cmpl_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_EXT_ADV_DATA_SET_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t31ble_adv_data_set_cmpl_evt_param6statusE "永久链接至目标")
        :   Indicate extend advertising data set status

    struct ble_adv_params_set_cmpl_evt_param[](#_CPPv4N21bk_ble_gap_cb_param_t33ble_adv_params_set_cmpl_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_EXT_ADV_PARAMS_SET_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t33ble_adv_params_set_cmpl_evt_param6statusE "永久链接至目标")
        :   Indicate extend advertising parameters set status

    struct ble_adv_scan_rsp_set_cmpl_evt_param[](#_CPPv4N21bk_ble_gap_cb_param_t35ble_adv_scan_rsp_set_cmpl_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_EXT_SCAN_RSP_DATA_SET_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t35ble_adv_scan_rsp_set_cmpl_evt_param6statusE "永久链接至目标")
        :   Indicate extend advertising scan response data set status

    struct ble_adv_set_clear_cmpl_evt_param[](#_CPPv4N21bk_ble_gap_cb_param_t32ble_adv_set_clear_cmpl_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_EXT_ADV_SET_CLEAR_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t32ble_adv_set_clear_cmpl_evt_param6statusE "永久链接至目标")
        :   Indicate advertising stop operation success status

    struct ble_adv_set_rand_addr_cmpl_evt_param[](#_CPPv4N21bk_ble_gap_cb_param_t36ble_adv_set_rand_addr_cmpl_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_EXT_ADV_SET_RAND_ADDR_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t36ble_adv_set_rand_addr_cmpl_evt_param6statusE "永久链接至目标")
        :   Indicate extend advertising random address set status

    struct ble_adv_set_remove_cmpl_evt_param[](#_CPPv4N21bk_ble_gap_cb_param_t33ble_adv_set_remove_cmpl_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_EXT_ADV_SET_REMOVE_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t33ble_adv_set_remove_cmpl_evt_param6statusE "永久链接至目标")
        :   Indicate advertising stop operation success status

    struct ble_adv_start_cmpl_evt_param[](#_CPPv4N21bk_ble_gap_cb_param_t28ble_adv_start_cmpl_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_EXT_ADV_START_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t28ble_adv_start_cmpl_evt_param6statusE "永久链接至目标")
        :   Indicate advertising start operation success status

    struct ble_adv_stop_cmpl_evt_param[](#_CPPv4N21bk_ble_gap_cb_param_t27ble_adv_stop_cmpl_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_EXT_ADV_STOP_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t27ble_adv_stop_cmpl_evt_param6statusE "永久链接至目标")
        :   Indicate advertising stop operation success status

    struct ble_adv_terminate_param[](#_CPPv4N21bk_ble_gap_cb_param_t23ble_adv_terminate_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_ADV_TERMINATED_EVT.

        Public Members

        uint8_t status[](#_CPPv4N21bk_ble_gap_cb_param_t23ble_adv_terminate_param6statusE "永久链接至目标")
        :   Indicate adv terminate status

        uint8_t adv_instance[](#_CPPv4N21bk_ble_gap_cb_param_t23ble_adv_terminate_param12adv_instanceE "永久链接至目标")
        :   extend advertising handle

        uint16_t conn_idx[](#_CPPv4N21bk_ble_gap_cb_param_t23ble_adv_terminate_param8conn_idxE "永久链接至目标")
        :   connection index

        uint8_t completed_event[](#_CPPv4N21bk_ble_gap_cb_param_t23ble_adv_terminate_param15completed_eventE "永久链接至目标")
        :   the number of completed extend advertising events

    struct ble_bond_dev_key_evt_param[](#_CPPv4N21bk_ble_gap_cb_param_t26ble_bond_dev_key_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_BOND_KEY_GENERATE_EVT.

        Public Members

        [bk_ble_bond_dev_t](#_CPPv417bk_ble_bond_dev_t "bk_ble_bond_dev_t") bond_dev[](#_CPPv4N21bk_ble_gap_cb_param_t26ble_bond_dev_key_evt_param8bond_devE "永久链接至目标")
        :   bond device Structure

    struct ble_bond_dev_key_req_evt_param[](#_CPPv4N21bk_ble_gap_cb_param_t30ble_bond_dev_key_req_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_BOND_KEY_REQ_EVT.

        Public Members

        [bk_ble_bond_key_req_t](#_CPPv421bk_ble_bond_key_req_t "bk_ble_bond_key_req_t") key_req[](#_CPPv4N21bk_ble_gap_cb_param_t30ble_bond_dev_key_req_evt_param7key_reqE "永久链接至目标")
        :   bond device Structure

    struct ble_bond_dev_list_evt_param[](#_CPPv4N21bk_ble_gap_cb_param_t27ble_bond_dev_list_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_BOND_DEV_LIST_OPERATEION_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t27ble_bond_dev_list_evt_param6statusE "永久链接至目标")

        [bk_gap_bond_dev_list_operation_t](#_CPPv432bk_gap_bond_dev_list_operation_t "bk_gap_bond_dev_list_operation_t") op[](#_CPPv4N21bk_ble_gap_cb_param_t27ble_bond_dev_list_evt_param2opE "永久链接至目标")
        :   operation id

    struct ble_channel_sel_alg_param[](#_CPPv4N21bk_ble_gap_cb_param_t25ble_channel_sel_alg_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_CHANNEL_SELECT_ALGORITHM_EVT.

        Public Members

        uint16_t conn_handle[](#_CPPv4N21bk_ble_gap_cb_param_t25ble_channel_sel_alg_param11conn_handleE "永久链接至目标")
        :   connection handle

        uint8_t channel_sel_alg[](#_CPPv4N21bk_ble_gap_cb_param_t25ble_channel_sel_alg_param15channel_sel_algE "永久链接至目标")
        :   channel selection algorithm

    struct ble_conn_params_set_cmpl_param[](#_CPPv4N21bk_ble_gap_cb_param_t30ble_conn_params_set_cmpl_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_PREFER_CONN_PARAMS_SET_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t30ble_conn_params_set_cmpl_param6statusE "永久链接至目标")
        :   Indicate extend connection parameters set status

    struct ble_connect_cancel_param[](#_CPPv4N21bk_ble_gap_cb_param_t24ble_connect_cancel_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_CONNECT_CANCEL_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t24ble_connect_cancel_param6statusE "永久链接至目标")

    struct ble_connect_complete_param[](#_CPPv4N21bk_ble_gap_cb_param_t26ble_connect_complete_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_CONNECT_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t26ble_connect_complete_param6statusE "永久链接至目标")

        [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") remote_bda[](#_CPPv4N21bk_ble_gap_cb_param_t26ble_connect_complete_param10remote_bdaE "永久链接至目标")
        :   Remote bluetooth device address

        [bk_ble_addr_type_t](#_CPPv418bk_ble_addr_type_t "bk_ble_addr_type_t") remote_bda_type[](#_CPPv4N21bk_ble_gap_cb_param_t26ble_connect_complete_param15remote_bda_typeE "永久链接至目标")

        uint8_t link_role[](#_CPPv4N21bk_ble_gap_cb_param_t26ble_connect_complete_param9link_roleE "永久链接至目标")
        :   Link role : master role = 0 ; slave role = 1

        uint16_t conn_intv[](#_CPPv4N21bk_ble_gap_cb_param_t26ble_connect_complete_param9conn_intvE "永久链接至目标")

        uint16_t conn_latency[](#_CPPv4N21bk_ble_gap_cb_param_t26ble_connect_complete_param12conn_latencyE "永久链接至目标")

        uint16_t supervision_timeout[](#_CPPv4N21bk_ble_gap_cb_param_t26ble_connect_complete_param19supervision_timeoutE "永久链接至目标")

        uint16_t hci_handle[](#_CPPv4N21bk_ble_gap_cb_param_t26ble_connect_complete_param10hci_handleE "永久链接至目标")

    struct ble_conntection_update_param_req[](#_CPPv4N21bk_ble_gap_cb_param_t32ble_conntection_update_param_reqE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_UPDATE_CONN_PARAMS_REQ_EVT.

        Public Members

        uint8_t can_modify[](#_CPPv4N21bk_ble_gap_cb_param_t32ble_conntection_update_param_req10can_modifyE "永久链接至目标")
        :   if true, param can be modify before accept

        [bk_ble_conn_update_params_t](#_CPPv427bk_ble_conn_update_params_t "bk_ble_conn_update_params_t") param[](#_CPPv4N21bk_ble_gap_cb_param_t32ble_conntection_update_param_req5paramE "永久链接至目标")

        uint8_t accept[](#_CPPv4N21bk_ble_gap_cb_param_t32ble_conntection_update_param_req6acceptE "永久链接至目标")

    struct ble_disconnect_complete_param[](#_CPPv4N21bk_ble_gap_cb_param_t29ble_disconnect_complete_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_DISCONNECT_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t29ble_disconnect_complete_param6statusE "永久链接至目标")

        [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") remote_bda[](#_CPPv4N21bk_ble_gap_cb_param_t29ble_disconnect_complete_param10remote_bdaE "永久链接至目标")
        :   Remote bluetooth device address

        [bk_ble_addr_type_t](#_CPPv418bk_ble_addr_type_t "bk_ble_addr_type_t") remote_bda_type[](#_CPPv4N21bk_ble_gap_cb_param_t29ble_disconnect_complete_param15remote_bda_typeE "永久链接至目标")

        uint8_t reason[](#_CPPv4N21bk_ble_gap_cb_param_t29ble_disconnect_complete_param6reasonE "永久链接至目标")

        uint16_t hci_handle[](#_CPPv4N21bk_ble_gap_cb_param_t29ble_disconnect_complete_param10hci_handleE "永久链接至目标")

    struct ble_ext_adv_report_param[](#_CPPv4N21bk_ble_gap_cb_param_t24ble_ext_adv_report_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_EXT_ADV_REPORT_EVT.

        Public Members

        [bk_ble_gap_ext_adv_reprot_t](#_CPPv427bk_ble_gap_ext_adv_reprot_t "bk_ble_gap_ext_adv_reprot_t") params[](#_CPPv4N21bk_ble_gap_cb_param_t24ble_ext_adv_report_param6paramsE "永久链接至目标")
        :   extend advertising report parameters

    struct ble_generate_rpa_cmpl[](#_CPPv4N21bk_ble_gap_cb_param_t21ble_generate_rpa_cmplE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_GENERATE_RPA_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t21ble_generate_rpa_cmpl6statusE "永久链接至目标")

        [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") addr[](#_CPPv4N21bk_ble_gap_cb_param_t21ble_generate_rpa_cmpl4addrE "永久链接至目标")

        [bk_ble_addr_type_t](#_CPPv418bk_ble_addr_type_t "bk_ble_addr_type_t") addr_type[](#_CPPv4N21bk_ble_gap_cb_param_t21ble_generate_rpa_cmpl9addr_typeE "永久链接至目标")

    struct ble_local_privacy_cmpl_evt_param[](#_CPPv4N21bk_ble_gap_cb_param_t32ble_local_privacy_cmpl_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_SET_LOCAL_PRIVACY_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t32ble_local_privacy_cmpl_evt_param6statusE "永久链接至目标")
        :   Indicate the set local privacy operation success status

    struct ble_period_adv_add_dev_cmpl_param[](#_CPPv4N21bk_ble_gap_cb_param_t33ble_period_adv_add_dev_cmpl_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_PERIODIC_ADV_ADD_DEV_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t33ble_period_adv_add_dev_cmpl_param6statusE "永久链接至目标")
        :   Indicate periodic advertising device list add status

    struct ble_period_adv_clear_dev_cmpl_param[](#_CPPv4N21bk_ble_gap_cb_param_t35ble_period_adv_clear_dev_cmpl_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_PERIODIC_ADV_CLEAR_DEV_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t35ble_period_adv_clear_dev_cmpl_param6statusE "永久链接至目标")
        :   Indicate periodic advertising device list clean status

    struct ble_period_adv_create_sync_cmpl_param[](#_CPPv4N21bk_ble_gap_cb_param_t37ble_period_adv_create_sync_cmpl_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_PERIODIC_ADV_CREATE_SYNC_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t37ble_period_adv_create_sync_cmpl_param6statusE "永久链接至目标")
        :   Indicate periodic advertising create sync status

    struct ble_period_adv_remove_dev_cmpl_param[](#_CPPv4N21bk_ble_gap_cb_param_t36ble_period_adv_remove_dev_cmpl_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_PERIODIC_ADV_REMOVE_DEV_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t36ble_period_adv_remove_dev_cmpl_param6statusE "永久链接至目标")
        :   Indicate periodic advertising device list remove status

    struct ble_period_adv_sync_cancel_cmpl_param[](#_CPPv4N21bk_ble_gap_cb_param_t37ble_period_adv_sync_cancel_cmpl_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_PERIODIC_ADV_SYNC_CANCEL_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t37ble_period_adv_sync_cancel_cmpl_param6statusE "永久链接至目标")
        :   Indicate periodic advertising sync cancel status

    struct ble_period_adv_sync_terminate_cmpl_param[](#_CPPv4N21bk_ble_gap_cb_param_t40ble_period_adv_sync_terminate_cmpl_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_PERIODIC_ADV_SYNC_TERMINATE_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t40ble_period_adv_sync_terminate_cmpl_param6statusE "永久链接至目标")
        :   Indicate periodic advertising sync terminate status

    struct ble_periodic_adv_data_set_cmpl_param[](#_CPPv4N21bk_ble_gap_cb_param_t36ble_periodic_adv_data_set_cmpl_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_PERIODIC_ADV_DATA_SET_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t36ble_periodic_adv_data_set_cmpl_param6statusE "永久链接至目标")
        :   Indicate periodic advertising data set status

    struct ble_periodic_adv_report_param[](#_CPPv4N21bk_ble_gap_cb_param_t29ble_periodic_adv_report_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_PERIODIC_ADV_REPORT_EVT.

        Public Members

        [bk_ble_gap_periodic_adv_report_t](#_CPPv432bk_ble_gap_periodic_adv_report_t "bk_ble_gap_periodic_adv_report_t") params[](#_CPPv4N21bk_ble_gap_cb_param_t29ble_periodic_adv_report_param6paramsE "永久链接至目标")
        :   periodic advertising report parameters

    struct ble_periodic_adv_set_params_cmpl_param[](#_CPPv4N21bk_ble_gap_cb_param_t38ble_periodic_adv_set_params_cmpl_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_PERIODIC_ADV_SET_PARAMS_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t38ble_periodic_adv_set_params_cmpl_param6statusE "永久链接至目标")
        :   Indicate periodic advertisingparameters set status

    struct ble_periodic_adv_start_cmpl_param[](#_CPPv4N21bk_ble_gap_cb_param_t33ble_periodic_adv_start_cmpl_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_PERIODIC_ADV_START_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t33ble_periodic_adv_start_cmpl_param6statusE "永久链接至目标")
        :   Indicate periodic advertising start status

    struct ble_periodic_adv_stop_cmpl_param[](#_CPPv4N21bk_ble_gap_cb_param_t32ble_periodic_adv_stop_cmpl_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_PERIODIC_ADV_STOP_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t32ble_periodic_adv_stop_cmpl_param6statusE "永久链接至目标")
        :   Indicate periodic advertising stop status

    struct ble_periodic_adv_sync_estab_param[](#_CPPv4N21bk_ble_gap_cb_param_t33ble_periodic_adv_sync_estab_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_PERIODIC_ADV_SYNC_ESTAB_EVT.

        Public Members

        uint8_t status[](#_CPPv4N21bk_ble_gap_cb_param_t33ble_periodic_adv_sync_estab_param6statusE "永久链接至目标")
        :   periodic advertising sync status

        uint16_t sync_handle[](#_CPPv4N21bk_ble_gap_cb_param_t33ble_periodic_adv_sync_estab_param11sync_handleE "永久链接至目标")
        :   periodic advertising sync handle

        uint8_t sid[](#_CPPv4N21bk_ble_gap_cb_param_t33ble_periodic_adv_sync_estab_param3sidE "永久链接至目标")
        :   periodic advertising sid

        [bk_ble_addr_type_t](#_CPPv418bk_ble_addr_type_t "bk_ble_addr_type_t") adv_addr_type[](#_CPPv4N21bk_ble_gap_cb_param_t33ble_periodic_adv_sync_estab_param13adv_addr_typeE "永久链接至目标")
        :   periodic advertising address type

        [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") adv_addr[](#_CPPv4N21bk_ble_gap_cb_param_t33ble_periodic_adv_sync_estab_param8adv_addrE "永久链接至目标")
        :   periodic advertising address

        [bk_ble_gap_phy_t](#_CPPv416bk_ble_gap_phy_t "bk_ble_gap_phy_t") adv_phy[](#_CPPv4N21bk_ble_gap_cb_param_t33ble_periodic_adv_sync_estab_param7adv_phyE "永久链接至目标")
        :   periodic advertising phy type

        uint16_t period_adv_interval[](#_CPPv4N21bk_ble_gap_cb_param_t33ble_periodic_adv_sync_estab_param19period_adv_intervalE "永久链接至目标")
        :   periodic advertising interval

        uint8_t adv_clk_accuracy[](#_CPPv4N21bk_ble_gap_cb_param_t33ble_periodic_adv_sync_estab_param16adv_clk_accuracyE "永久链接至目标")
        :   periodic advertising clock accuracy

    struct ble_periodic_adv_sync_lost_param[](#_CPPv4N21bk_ble_gap_cb_param_t32ble_periodic_adv_sync_lost_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_PERIODIC_ADV_SYNC_LOST_EVT.

        Public Members

        uint16_t sync_handle[](#_CPPv4N21bk_ble_gap_cb_param_t32ble_periodic_adv_sync_lost_param11sync_handleE "永久链接至目标")
        :   sync handle

    struct ble_phy_update_cmpl_param[](#_CPPv4N21bk_ble_gap_cb_param_t25ble_phy_update_cmpl_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_PHY_UPDATE_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t25ble_phy_update_cmpl_param6statusE "永久链接至目标")
        :   phy update status

        [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bda[](#_CPPv4N21bk_ble_gap_cb_param_t25ble_phy_update_cmpl_param3bdaE "永久链接至目标")
        :   address

        [bk_ble_gap_phy_t](#_CPPv416bk_ble_gap_phy_t "bk_ble_gap_phy_t") tx_phy[](#_CPPv4N21bk_ble_gap_cb_param_t25ble_phy_update_cmpl_param6tx_phyE "永久链接至目标")
        :   tx phy type

        [bk_ble_gap_phy_t](#_CPPv416bk_ble_gap_phy_t "bk_ble_gap_phy_t") rx_phy[](#_CPPv4N21bk_ble_gap_cb_param_t25ble_phy_update_cmpl_param6rx_phyE "永久链接至目标")
        :   rx phy type

    struct ble_pkt_data_length_cmpl_evt_param[](#_CPPv4N21bk_ble_gap_cb_param_t34ble_pkt_data_length_cmpl_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_SET_PKT_LENGTH_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t34ble_pkt_data_length_cmpl_evt_param6statusE "永久链接至目标")
        :   Indicate the set pkt data length operation success status

        [bk_ble_pkt_data_length_params_t](#_CPPv431bk_ble_pkt_data_length_params_t "bk_ble_pkt_data_length_params_t") params[](#_CPPv4N21bk_ble_gap_cb_param_t34ble_pkt_data_length_cmpl_evt_param6paramsE "永久链接至目标")
        :   pkt data length value

    struct ble_read_phy_cmpl_evt_param[](#_CPPv4N21bk_ble_gap_cb_param_t27ble_read_phy_cmpl_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_READ_PHY_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t27ble_read_phy_cmpl_evt_param6statusE "永久链接至目标")
        :   read phy complete status

        [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bda[](#_CPPv4N21bk_ble_gap_cb_param_t27ble_read_phy_cmpl_evt_param3bdaE "永久链接至目标")
        :   read phy address

        [bk_ble_gap_phy_t](#_CPPv416bk_ble_gap_phy_t "bk_ble_gap_phy_t") tx_phy[](#_CPPv4N21bk_ble_gap_cb_param_t27ble_read_phy_cmpl_evt_param6tx_phyE "永久链接至目标")
        :   tx phy type

        [bk_ble_gap_phy_t](#_CPPv416bk_ble_gap_phy_t "bk_ble_gap_phy_t") rx_phy[](#_CPPv4N21bk_ble_gap_cb_param_t27ble_read_phy_cmpl_evt_param6rx_phyE "永久链接至目标")
        :   rx phy type

    struct ble_read_rssi_cmpl_evt_param[](#_CPPv4N21bk_ble_gap_cb_param_t28ble_read_rssi_cmpl_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_READ_RSSI_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t28ble_read_rssi_cmpl_evt_param6statusE "永久链接至目标")
        :   Indicate the read adv tx power operation success status

        int8_t rssi[](#_CPPv4N21bk_ble_gap_cb_param_t28ble_read_rssi_cmpl_evt_param4rssiE "永久链接至目标")
        :   The ble remote device rssi value, the range is from -127 to 20, the unit is dbm, if the RSSI cannot be read, the RSSI metric shall be set to 127.

        [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") remote_addr[](#_CPPv4N21bk_ble_gap_cb_param_t28ble_read_rssi_cmpl_evt_param11remote_addrE "永久链接至目标")
        :   The remote device address

    struct ble_scan_params_set_cmpl_param[](#_CPPv4N21bk_ble_gap_cb_param_t30ble_scan_params_set_cmpl_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_SCAN_PARAMS_SET_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t30ble_scan_params_set_cmpl_param6statusE "永久链接至目标")
        :   Indicate extend advertising parameters set status

    struct ble_scan_req_received_param[](#_CPPv4N21bk_ble_gap_cb_param_t27ble_scan_req_received_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_SCAN_REQ_RECEIVED_EVT.

        Public Members

        uint8_t adv_instance[](#_CPPv4N21bk_ble_gap_cb_param_t27ble_scan_req_received_param12adv_instanceE "永久链接至目标")
        :   extend advertising handle

        [bk_ble_addr_type_t](#_CPPv418bk_ble_addr_type_t "bk_ble_addr_type_t") scan_addr_type[](#_CPPv4N21bk_ble_gap_cb_param_t27ble_scan_req_received_param14scan_addr_typeE "永久链接至目标")
        :   scanner address type

        [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") scan_addr[](#_CPPv4N21bk_ble_gap_cb_param_t27ble_scan_req_received_param9scan_addrE "永久链接至目标")
        :   scanner address

    struct ble_scan_rsp_data_raw_set_cmpl_evt_param[](#_CPPv4N21bk_ble_gap_cb_param_t40ble_scan_rsp_data_raw_set_cmpl_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_EXT_SCAN_RSP_DATA_RAW_SET_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t40ble_scan_rsp_data_raw_set_cmpl_evt_param6statusE "永久链接至目标")
        :   Indicate extend advertising scan response data set status

    struct ble_scan_start_cmpl_param[](#_CPPv4N21bk_ble_gap_cb_param_t25ble_scan_start_cmpl_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_SCAN_START_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t25ble_scan_start_cmpl_param6statusE "永久链接至目标")
        :   Indicate extend advertising start status

    struct ble_scan_stop_cmpl_param[](#_CPPv4N21bk_ble_gap_cb_param_t24ble_scan_stop_cmpl_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_SCAN_STOP_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t24ble_scan_stop_cmpl_param6statusE "永久链接至目标")
        :   Indicate extend advertising stop status

    struct ble_set_channels_cmpl_evt_param[](#_CPPv4N21bk_ble_gap_cb_param_t31ble_set_channels_cmpl_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_SET_CHANNELS_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t31ble_set_channels_cmpl_evt_param6statusE "永久链接至目标")
        :   BLE set channel status

    struct ble_set_perf_def_phy_cmpl_evt_param[](#_CPPv4N21bk_ble_gap_cb_param_t35ble_set_perf_def_phy_cmpl_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_SET_PREFERRED_DEFAULT_PHY_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t35ble_set_perf_def_phy_cmpl_evt_param6statusE "永久链接至目标")
        :   Indicate perf default phy set status

    struct ble_set_perf_phy_cmpl_evt_param[](#_CPPv4N21bk_ble_gap_cb_param_t31ble_set_perf_phy_cmpl_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_SET_PREFERRED_PHY_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t31ble_set_perf_phy_cmpl_evt_param6statusE "永久链接至目标")
        :   Indicate perf phy set status

    struct ble_set_rand_cmpl_evt_param[](#_CPPv4N21bk_ble_gap_cb_param_t27ble_set_rand_cmpl_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_SET_STATIC_RAND_ADDR_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t27ble_set_rand_cmpl_evt_param6statusE "永久链接至目标")
        :   Indicate set static rand address operation success status

    struct ble_set_security_params_cmpl[](#_CPPv4N21bk_ble_gap_cb_param_t28ble_set_security_params_cmplE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_SET_SECURITY_PARAMS_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t28ble_set_security_params_cmpl6statusE "永久链接至目标")

        [bk_ble_sm_param_t](#_CPPv417bk_ble_sm_param_t "bk_ble_sm_param_t") param[](#_CPPv4N21bk_ble_gap_cb_param_t28ble_set_security_params_cmpl5paramE "永久链接至目标")

    struct ble_update_conn_params_evt_param[](#_CPPv4N21bk_ble_gap_cb_param_t32ble_update_conn_params_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_UPDATE_CONN_PARAMS_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t32ble_update_conn_params_evt_param6statusE "永久链接至目标")
        :   Indicate update connection parameters success status

        [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bda[](#_CPPv4N21bk_ble_gap_cb_param_t32ble_update_conn_params_evt_param3bdaE "永久链接至目标")
        :   Bluetooth device address

        uint16_t min_int[](#_CPPv4N21bk_ble_gap_cb_param_t32ble_update_conn_params_evt_param7min_intE "永久链接至目标")
        :   Min connection interval

        uint16_t max_int[](#_CPPv4N21bk_ble_gap_cb_param_t32ble_update_conn_params_evt_param7max_intE "永久链接至目标")
        :   Max connection interval

        uint16_t latency[](#_CPPv4N21bk_ble_gap_cb_param_t32ble_update_conn_params_evt_param7latencyE "永久链接至目标")
        :   Slave latency for the connection in number of connection events. Range: 0x0000 to 0x01F3

        uint16_t conn_int[](#_CPPv4N21bk_ble_gap_cb_param_t32ble_update_conn_params_evt_param8conn_intE "永久链接至目标")
        :   Current connection interval

        uint16_t timeout[](#_CPPv4N21bk_ble_gap_cb_param_t32ble_update_conn_params_evt_param7timeoutE "永久链接至目标")
        :   Supervision timeout for the LE Link. Range: 0x000A to 0x0C80. Mandatory Range: 0x000A to 0x0C80 Time = N * 10 msec

    struct ble_update_whitelist_cmpl_evt_param[](#_CPPv4N21bk_ble_gap_cb_param_t35ble_update_whitelist_cmpl_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_ble_types.h>*

        BK_BLE_GAP_UPDATE_WHITELIST_COMPLETE_EVT.

        Public Members

        [bk_bt_status_t](#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N21bk_ble_gap_cb_param_t35ble_update_whitelist_cmpl_evt_param6statusE "永久链接至目标")
        :   Indicate the add or remove whitelist operation success status

        [bk_ble_wl_operation_t](#_CPPv421bk_ble_wl_operation_t "bk_ble_wl_operation_t") wl_operation[](#_CPPv4N21bk_ble_gap_cb_param_t35ble_update_whitelist_cmpl_evt_param12wl_operationE "永久链接至目标")
        :   The value is BK_BLE_WHITELIST_ADD if add address to whitelist operation success, BK_BLE_WHITELIST_REMOVE if remove address from the whitelist operation success


### Structures[](#structures "永久链接至标题")

struct bk_ble_adv_params_t[](#_CPPv419bk_ble_adv_params_t "永久链接至目标")
:   Advertising parameters.

    Public Members

    uint16_t adv_int_min[](#_CPPv4N19bk_ble_adv_params_t11adv_int_minE "永久链接至目标")
    :   Minimum advertising interval for undirected and low duty cycle directed advertising. Range: 0x0020 to 0x4000 Default: N = 0x0800 (1.28 second) Time = N * 0.625 msec Time Range: 20 ms to 10.24 sec

    uint16_t adv_int_max[](#_CPPv4N19bk_ble_adv_params_t11adv_int_maxE "永久链接至目标")
    :   Maximum advertising interval for undirected and low duty cycle directed advertising. Range: 0x0020 to 0x4000 Default: N = 0x0800 (1.28 second) Time = N * 0.625 msec Time Range: 20 ms to 10.24 sec Advertising max interval

    [bk_ble_adv_type_t](#_CPPv417bk_ble_adv_type_t "bk_ble_adv_type_t") adv_type[](#_CPPv4N19bk_ble_adv_params_t8adv_typeE "永久链接至目标")
    :   Advertising type

    [bk_ble_addr_type_t](#_CPPv418bk_ble_addr_type_t "bk_ble_addr_type_t") own_addr_type[](#_CPPv4N19bk_ble_adv_params_t13own_addr_typeE "永久链接至目标")
    :   Owner bluetooth device address type

    [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") peer_addr[](#_CPPv4N19bk_ble_adv_params_t9peer_addrE "永久链接至目标")
    :   Peer device bluetooth device address

    [bk_ble_addr_type_t](#_CPPv418bk_ble_addr_type_t "bk_ble_addr_type_t") peer_addr_type[](#_CPPv4N19bk_ble_adv_params_t14peer_addr_typeE "永久链接至目标")
    :   Peer device bluetooth device address type, only support public address type and random address type

    [bk_ble_adv_channel_t](#_CPPv420bk_ble_adv_channel_t "bk_ble_adv_channel_t") channel_map[](#_CPPv4N19bk_ble_adv_params_t11channel_mapE "永久链接至目标")
    :   Advertising channel map

    [bk_ble_adv_filter_t](#_CPPv419bk_ble_adv_filter_t "bk_ble_adv_filter_t") adv_filter_policy[](#_CPPv4N19bk_ble_adv_params_t17adv_filter_policyE "永久链接至目标")
    :   Advertising filter policy

struct bk_ble_adv_data_t[](#_CPPv417bk_ble_adv_data_t "永久链接至目标")
:   Advertising data content, according to “Supplement to the Bluetooth Core Specification”.

    Public Members

    bool set_scan_rsp[](#_CPPv4N17bk_ble_adv_data_t12set_scan_rspE "永久链接至目标")
    :   Set this advertising data as scan response or not

    bool include_name[](#_CPPv4N17bk_ble_adv_data_t12include_nameE "永久链接至目标")
    :   Advertising data include device name or not

    bool include_txpower[](#_CPPv4N17bk_ble_adv_data_t15include_txpowerE "永久链接至目标")
    :   Advertising data include TX power

    int min_interval[](#_CPPv4N17bk_ble_adv_data_t12min_intervalE "永久链接至目标")
    :   Advertising data show slave preferred connection min interval. The connection interval in the following manner: connIntervalmin = Conn_Interval_Min * 1.25 ms Conn_Interval_Min range: 0x0006 to 0x0C80 Value of 0xFFFF indicates no specific minimum. Values not defined above are reserved for future use.

    int max_interval[](#_CPPv4N17bk_ble_adv_data_t12max_intervalE "永久链接至目标")
    :   Advertising data show slave preferred connection max interval. The connection interval in the following manner: connIntervalmax = Conn_Interval_Max * 1.25 ms Conn_Interval_Max range: 0x0006 to 0x0C80 Conn_Interval_Max shall be equal to or greater than the Conn_Interval_Min. Value of 0xFFFF indicates no specific maximum. Values not defined above are reserved for future use.

    int appearance[](#_CPPv4N17bk_ble_adv_data_t10appearanceE "永久链接至目标")
    :   External appearance of device

    uint16_t manufacturer_len[](#_CPPv4N17bk_ble_adv_data_t16manufacturer_lenE "永久链接至目标")
    :   Manufacturer data length

    uint8_t *p_manufacturer_data[](#_CPPv4N17bk_ble_adv_data_t19p_manufacturer_dataE "永久链接至目标")
    :   Manufacturer data point

    uint16_t service_data_len[](#_CPPv4N17bk_ble_adv_data_t16service_data_lenE "永久链接至目标")
    :   Service data length

    uint8_t *p_service_data[](#_CPPv4N17bk_ble_adv_data_t14p_service_dataE "永久链接至目标")
    :   Service data point

    uint16_t service_uuid_len[](#_CPPv4N17bk_ble_adv_data_t16service_uuid_lenE "永久链接至目标")
    :   Service uuid length

    uint8_t *p_service_uuid[](#_CPPv4N17bk_ble_adv_data_t14p_service_uuidE "永久链接至目标")
    :   Service uuid array point

    uint8_t flag[](#_CPPv4N17bk_ble_adv_data_t4flagE "永久链接至目标")
    :   Advertising flag of discovery mode, see BLE_ADV_DATA_FLAG detail

struct bk_ble_scan_params_t[](#_CPPv420bk_ble_scan_params_t "永久链接至目标")
:   Ble scan parameters.

    Public Members

    [bk_ble_scan_type_t](#_CPPv418bk_ble_scan_type_t "bk_ble_scan_type_t") scan_type[](#_CPPv4N20bk_ble_scan_params_t9scan_typeE "永久链接至目标")
    :   Scan type

    [bk_ble_addr_type_t](#_CPPv418bk_ble_addr_type_t "bk_ble_addr_type_t") own_addr_type[](#_CPPv4N20bk_ble_scan_params_t13own_addr_typeE "永久链接至目标")
    :   Owner address type

    [bk_ble_scan_filter_t](#_CPPv420bk_ble_scan_filter_t "bk_ble_scan_filter_t") scan_filter_policy[](#_CPPv4N20bk_ble_scan_params_t18scan_filter_policyE "永久链接至目标")
    :   Scan filter policy

    uint16_t scan_interval[](#_CPPv4N20bk_ble_scan_params_t13scan_intervalE "永久链接至目标")
    :   Scan interval. This is defined as the time interval from when the Controller started its last LE scan until it begins the subsequent LE scan. Range: 0x0004 to 0x4000 Default: 0x0010 (10 ms) Time = N * 0.625 msec Time Range: 2.5 msec to 10.24 seconds

    uint16_t scan_window[](#_CPPv4N20bk_ble_scan_params_t11scan_windowE "永久链接至目标")
    :   Scan window. The duration of the LE scan. LE_Scan_Window shall be less than or equal to LE_Scan_Interval Range: 0x0004 to 0x4000 Default: 0x0010 (10 ms) Time = N * 0.625 msec Time Range: 2.5 msec to 10240 msec

    [bk_ble_scan_duplicate_t](#_CPPv423bk_ble_scan_duplicate_t "bk_ble_scan_duplicate_t") scan_duplicate[](#_CPPv4N20bk_ble_scan_params_t14scan_duplicateE "永久链接至目标")
    :   The Scan_Duplicates parameter controls whether the Link Layer should filter out duplicate advertising reports (BLE_SCAN_DUPLICATE_ENABLE) to the Host, or if the Link Layer should generate advertising reports for each packet received

struct bk_gap_create_conn_params_t[](#_CPPv427bk_gap_create_conn_params_t "永久链接至目标")
:   create connection param

    Public Members

    uint16_t scan_interval[](#_CPPv4N27bk_gap_create_conn_params_t13scan_intervalE "永久链接至目标")
    :   scan interval, unit in 0.625ms

    uint16_t scan_window[](#_CPPv4N27bk_gap_create_conn_params_t11scan_windowE "永久链接至目标")
    :   scan window, unit in 0.625ms

    uint8_t initiator_filter_policy[](#_CPPv4N27bk_gap_create_conn_params_t23initiator_filter_policyE "永久链接至目标")
    :   policy that how to use white list. 0 means not used, 1 means only connect device that in white list

    [bk_ble_addr_type_t](#_CPPv418bk_ble_addr_type_t "bk_ble_addr_type_t") local_addr_type[](#_CPPv4N27bk_gap_create_conn_params_t15local_addr_typeE "永久链接至目标")
    :   local address type

    [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") peer_addr[](#_CPPv4N27bk_gap_create_conn_params_t9peer_addrE "永久链接至目标")
    :   peer addr

    [bk_ble_addr_type_t](#_CPPv418bk_ble_addr_type_t "bk_ble_addr_type_t") peer_addr_type[](#_CPPv4N27bk_gap_create_conn_params_t14peer_addr_typeE "永久链接至目标")
    :   Peer address type, only BLE_ADDR_TYPE_PUBLIC or BLE_ADDR_TYPE_RANDOM available

    uint16_t conn_interval_min[](#_CPPv4N27bk_gap_create_conn_params_t17conn_interval_minE "永久链接至目标")
    :   conn min interval, unit in 1.25ms, Range: 7.5ms to 4s

    uint16_t conn_interval_max[](#_CPPv4N27bk_gap_create_conn_params_t17conn_interval_maxE "永久链接至目标")
    :   conn max interval, unit in 1.25ms, Range: 7.5ms to 4s

    uint16_t conn_latency[](#_CPPv4N27bk_gap_create_conn_params_t12conn_latencyE "永久链接至目标")
    :   latency Range: 0x0000 to 0x01F3

    uint16_t supervision_timeout[](#_CPPv4N27bk_gap_create_conn_params_t19supervision_timeoutE "永久链接至目标")
    :   conn timeout, unit in 10ms Range: 100ms to 32s

    uint16_t min_ce[](#_CPPv4N27bk_gap_create_conn_params_t6min_ceE "永久链接至目标")
    :   minimum length of connection event recommended, unit in 0.625ms Range: 0x0000 to 0xFFFF

    uint16_t max_ce[](#_CPPv4N27bk_gap_create_conn_params_t6max_ceE "永久链接至目标")
    :   maximum length of connection event recommended, unit in 0.625ms Range: 0x0000 to 0xFFFF

struct bk_gap_conn_params_t[](#_CPPv420bk_gap_conn_params_t "永久链接至目标")
:   connection parameters information

    Public Members

    uint16_t interval[](#_CPPv4N20bk_gap_conn_params_t8intervalE "永久链接至目标")
    :   connection interval

    uint16_t latency[](#_CPPv4N20bk_gap_conn_params_t7latencyE "永久链接至目标")
    :   Slave latency for the connection in number of connection events. Range: 0x0000 to 0x01F3

    uint16_t timeout[](#_CPPv4N20bk_gap_conn_params_t7timeoutE "永久链接至目标")
    :   Supervision timeout for the LE Link. Range: 0x000A to 0x0C80. Mandatory Range: 0x000A to 0x0C80 Time = N * 10 msec Time Range: 100 msec to 32 seconds

struct bk_ble_conn_update_params_t[](#_CPPv427bk_ble_conn_update_params_t "永久链接至目标")
:   Connection update parameters.

    Public Members

    [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bda[](#_CPPv4N27bk_ble_conn_update_params_t3bdaE "永久链接至目标")
    :   Bluetooth device address

    uint16_t min_int[](#_CPPv4N27bk_ble_conn_update_params_t7min_intE "永久链接至目标")
    :   Min connection interval

    uint16_t max_int[](#_CPPv4N27bk_ble_conn_update_params_t7max_intE "永久链接至目标")
    :   Max connection interval

    uint16_t latency[](#_CPPv4N27bk_ble_conn_update_params_t7latencyE "永久链接至目标")
    :   Slave latency for the connection in number of connection events. Range: 0x0000 to 0x01F3

    uint16_t timeout[](#_CPPv4N27bk_ble_conn_update_params_t7timeoutE "永久链接至目标")
    :   Supervision timeout for the LE Link. Range: 0x000A to 0x0C80. Mandatory Range: 0x000A to 0x0C80 Time = N * 10 msec Time Range: 100 msec to 32 seconds

struct bk_ble_pkt_data_length_params_t[](#_CPPv431bk_ble_pkt_data_length_params_t "永久链接至目标")
:   BLE pkt date length keys.

    Public Members

    uint16_t rx_len[](#_CPPv4N31bk_ble_pkt_data_length_params_t6rx_lenE "永久链接至目标")
    :   pkt rx data length value

    uint16_t tx_len[](#_CPPv4N31bk_ble_pkt_data_length_params_t6tx_lenE "永久链接至目标")
    :   pkt tx data length value

struct bk_ble_penc_keys_t[](#_CPPv418bk_ble_penc_keys_t "永久链接至目标")
:   BLE encryption keys.

    Public Members

    [bk_bt_octet16_t](#_CPPv415bk_bt_octet16_t "bk_bt_octet16_t") ltk[](#_CPPv4N18bk_ble_penc_keys_t3ltkE "永久链接至目标")
    :   The long term key

    [bk_bt_octet8_t](#_CPPv414bk_bt_octet8_t "bk_bt_octet8_t") rand[](#_CPPv4N18bk_ble_penc_keys_t4randE "永久链接至目标")
    :   The random number

    uint16_t ediv[](#_CPPv4N18bk_ble_penc_keys_t4edivE "永久链接至目标")
    :   The ediv value

    uint8_t sec_level[](#_CPPv4N18bk_ble_penc_keys_t9sec_levelE "永久链接至目标")
    :   The security level of the security link, see bk_ble_security_level_t

    uint8_t key_size[](#_CPPv4N18bk_ble_penc_keys_t8key_sizeE "永久链接至目标")
    :   The key size(7~16) of the security link

struct bk_ble_pcsrk_keys_t[](#_CPPv419bk_ble_pcsrk_keys_t "永久链接至目标")
:   BLE CSRK keys.

    Public Members

    uint32_t counter[](#_CPPv4N19bk_ble_pcsrk_keys_t7counterE "永久链接至目标")
    :   The counter

    [bk_bt_octet16_t](#_CPPv415bk_bt_octet16_t "bk_bt_octet16_t") csrk[](#_CPPv4N19bk_ble_pcsrk_keys_t4csrkE "永久链接至目标")
    :   The csrk key

    uint8_t sec_level[](#_CPPv4N19bk_ble_pcsrk_keys_t9sec_levelE "永久链接至目标")
    :   The security level see bk_ble_security_level_t

struct bk_ble_pid_keys_t[](#_CPPv417bk_ble_pid_keys_t "永久链接至目标")
:   BLE pid keys.

    Public Members

    [bk_bt_octet16_t](#_CPPv415bk_bt_octet16_t "bk_bt_octet16_t") irk[](#_CPPv4N17bk_ble_pid_keys_t3irkE "永久链接至目标")
    :   The irk value

    [bk_ble_addr_type_t](#_CPPv418bk_ble_addr_type_t "bk_ble_addr_type_t") addr_type[](#_CPPv4N17bk_ble_pid_keys_t9addr_typeE "永久链接至目标")
    :   The address type

    [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") static_addr[](#_CPPv4N17bk_ble_pid_keys_t11static_addrE "永久链接至目标")
    :   The static address

struct bk_ble_lenc_keys_t[](#_CPPv418bk_ble_lenc_keys_t "永久链接至目标")
:   BLE Encryption reproduction keys.

    Public Members

    [bk_bt_octet16_t](#_CPPv415bk_bt_octet16_t "bk_bt_octet16_t") ltk[](#_CPPv4N18bk_ble_lenc_keys_t3ltkE "永久链接至目标")
    :   The long term key

    [bk_bt_octet8_t](#_CPPv414bk_bt_octet8_t "bk_bt_octet8_t") rand[](#_CPPv4N18bk_ble_lenc_keys_t4randE "永久链接至目标")
    :   The random number

    uint16_t div[](#_CPPv4N18bk_ble_lenc_keys_t3divE "永久链接至目标")
    :   The div value

    uint8_t key_size[](#_CPPv4N18bk_ble_lenc_keys_t8key_sizeE "永久链接至目标")
    :   The key size of the security link

    uint8_t sec_level[](#_CPPv4N18bk_ble_lenc_keys_t9sec_levelE "永久链接至目标")
    :   The security level of the security link see bk_ble_security_level_t

struct bk_ble_lcsrk_keys_t[](#_CPPv419bk_ble_lcsrk_keys_t "永久链接至目标")
:   BLE SRK keys.

    Public Members

    uint32_t counter[](#_CPPv4N19bk_ble_lcsrk_keys_t7counterE "永久链接至目标")
    :   The counter value

    uint16_t div[](#_CPPv4N19bk_ble_lcsrk_keys_t3divE "永久链接至目标")
    :   The div value

    uint8_t sec_level[](#_CPPv4N19bk_ble_lcsrk_keys_t9sec_levelE "永久链接至目标")
    :   The security level of the security link see bk_ble_security_level_t

    [bk_bt_octet16_t](#_CPPv415bk_bt_octet16_t "bk_bt_octet16_t") csrk[](#_CPPv4N19bk_ble_lcsrk_keys_t4csrkE "永久链接至目标")
    :   The csrk key value

struct bk_ble_link_keys_t[](#_CPPv418bk_ble_link_keys_t "永久链接至目标")

struct bk_ble_sec_key_notif_t[](#_CPPv422bk_ble_sec_key_notif_t "永久链接至目标")
:   Structure associated with BK_KEY_NOTIF_EVT.

    Public Members

    [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr[](#_CPPv4N22bk_ble_sec_key_notif_t7bd_addrE "永久链接至目标")
    :   peer address

    uint32_t passkey[](#_CPPv4N22bk_ble_sec_key_notif_t7passkeyE "永久链接至目标")
    :   the passkey or numeric value for comparison. If just_works, do not show this number to UI

struct bk_ble_sec_req_t[](#_CPPv416bk_ble_sec_req_t "永久链接至目标")
:   Structure of the security request.

    Public Members

    [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr[](#_CPPv4N16bk_ble_sec_req_t7bd_addrE "永久链接至目标")
    :   peer address

struct bk_ble_bond_key_info_t[](#_CPPv422bk_ble_bond_key_info_t "永久链接至目标")
:   struct type of the bond key information value

    Public Members

    [bk_ble_key_mask_t](#_CPPv417bk_ble_key_mask_t "bk_ble_key_mask_t") key_mask[](#_CPPv4N22bk_ble_bond_key_info_t8key_maskE "永久链接至目标")
    :   the key mask to indicate witch key is present

    [bk_ble_penc_keys_t](#_CPPv418bk_ble_penc_keys_t "bk_ble_penc_keys_t") penc_key[](#_CPPv4N22bk_ble_bond_key_info_t8penc_keyE "永久链接至目标")
    :   received peer encryption key

    [bk_ble_pid_keys_t](#_CPPv417bk_ble_pid_keys_t "bk_ble_pid_keys_t") pid_key[](#_CPPv4N22bk_ble_bond_key_info_t7pid_keyE "永久链接至目标")
    :   peer device ID key

    [bk_ble_pcsrk_keys_t](#_CPPv419bk_ble_pcsrk_keys_t "bk_ble_pcsrk_keys_t") pcsrk_key[](#_CPPv4N22bk_ble_bond_key_info_t9pcsrk_keyE "永久链接至目标")
    :   received peer device SRK

    [bk_ble_lenc_keys_t](#_CPPv418bk_ble_lenc_keys_t "bk_ble_lenc_keys_t") lenc_key[](#_CPPv4N22bk_ble_bond_key_info_t8lenc_keyE "永久链接至目标")
    :   local encryption reproduction keys LTK = = d1(ER,DIV,0)

    [bk_ble_pid_keys_t](#_CPPv417bk_ble_pid_keys_t "bk_ble_pid_keys_t") lid_key[](#_CPPv4N22bk_ble_bond_key_info_t7lid_keyE "永久链接至目标")
    :   local device ID key

    [bk_ble_lcsrk_keys_t](#_CPPv419bk_ble_lcsrk_keys_t "bk_ble_lcsrk_keys_t") lcsrk_key[](#_CPPv4N22bk_ble_bond_key_info_t9lcsrk_keyE "永久链接至目标")
    :   local device CSRK = d1(ER,DIV,1)

struct bk_ble_bond_dev_t[](#_CPPv417bk_ble_bond_dev_t "永久链接至目标")
:   struct type of the bond device value

    Public Members

    [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr[](#_CPPv4N17bk_ble_bond_dev_t7bd_addrE "永久链接至目标")
    :   peer nominal address

    [bk_ble_bond_key_info_t](#_CPPv422bk_ble_bond_key_info_t "bk_ble_bond_key_info_t") bond_key[](#_CPPv4N17bk_ble_bond_dev_t8bond_keyE "永久链接至目标")
    :   peer address type

        the bond key information

struct bk_ble_local_keys_t[](#_CPPv419bk_ble_local_keys_t "永久链接至目标")
:   structure type of the ble local keys value

    Public Members

    [bk_bt_octet16_t](#_CPPv415bk_bt_octet16_t "bk_bt_octet16_t") ir[](#_CPPv4N19bk_ble_local_keys_t2irE "永久链接至目标")
    :   the 16 bits of the ir value

    [bk_bt_octet16_t](#_CPPv415bk_bt_octet16_t "bk_bt_octet16_t") er[](#_CPPv4N19bk_ble_local_keys_t2erE "永久链接至目标")
    :   the 16 bits of the er value

    [bk_bt_octet16_t](#_CPPv415bk_bt_octet16_t "bk_bt_octet16_t") dhk[](#_CPPv4N19bk_ble_local_keys_t3dhkE "永久链接至目标")
    :   the 16 bits of the dh key value

struct bk_ble_auth_cmpl_t[](#_CPPv418bk_ble_auth_cmpl_t "永久链接至目标")
:   Structure associated with BK_AUTH_CMPL_EVT.

    Public Members

    [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr[](#_CPPv4N18bk_ble_auth_cmpl_t7bd_addrE "永久链接至目标")
    :   BD address peer device.

    bool success[](#_CPPv4N18bk_ble_auth_cmpl_t7successE "永久链接至目标")
    :   TRUE of authentication succeeded, FALSE if failed.

    uint8_t fail_reason[](#_CPPv4N18bk_ble_auth_cmpl_t11fail_reasonE "永久链接至目标")
    :   The HCI reason/error code for when success=FALSE

    [bk_ble_addr_type_t](#_CPPv418bk_ble_addr_type_t "bk_ble_addr_type_t") addr_type[](#_CPPv4N18bk_ble_auth_cmpl_t9addr_typeE "永久链接至目标")
    :   Peer device address type

    [bk_bt_dev_type_t](#_CPPv416bk_bt_dev_type_t "bk_bt_dev_type_t") dev_type[](#_CPPv4N18bk_ble_auth_cmpl_t8dev_typeE "永久链接至目标")
    :   Device type

    [bk_ble_auth_req_t](#_CPPv417bk_ble_auth_req_t "bk_ble_auth_req_t") auth_mode[](#_CPPv4N18bk_ble_auth_cmpl_t9auth_modeE "永久链接至目标")
    :   authentication mode

struct bk_ble_bond_key_req_t[](#_CPPv421bk_ble_bond_key_req_t "永久链接至目标")

struct bk_ble_gap_ext_adv_params_t[](#_CPPv427bk_ble_gap_ext_adv_params_t "永久链接至目标")
:   ext adv parameters

    Public Members

    [bk_ble_ext_adv_type_mask_t](#_CPPv426bk_ble_ext_adv_type_mask_t "bk_ble_ext_adv_type_mask_t") type[](#_CPPv4N27bk_ble_gap_ext_adv_params_t4typeE "永久链接至目标")
    :   ext adv type

    uint32_t interval_min[](#_CPPv4N27bk_ble_gap_ext_adv_params_t12interval_minE "永久链接至目标")
    :   ext adv minimum interval

    uint32_t interval_max[](#_CPPv4N27bk_ble_gap_ext_adv_params_t12interval_maxE "永久链接至目标")
    :   ext adv maximum interval

    [bk_ble_adv_channel_t](#_CPPv420bk_ble_adv_channel_t "bk_ble_adv_channel_t") channel_map[](#_CPPv4N27bk_ble_gap_ext_adv_params_t11channel_mapE "永久链接至目标")
    :   ext adv channel map

    [bk_ble_addr_type_t](#_CPPv418bk_ble_addr_type_t "bk_ble_addr_type_t") own_addr_type[](#_CPPv4N27bk_ble_gap_ext_adv_params_t13own_addr_typeE "永久链接至目标")
    :   ext adv own address type

    [bk_ble_addr_type_t](#_CPPv418bk_ble_addr_type_t "bk_ble_addr_type_t") peer_addr_type[](#_CPPv4N27bk_ble_gap_ext_adv_params_t14peer_addr_typeE "永久链接至目标")
    :   ext adv peer address type, only BLE_ADDR_TYPE_PUBLIC and BLE_ADDR_TYPE_RANDOM is valid

    [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") peer_addr[](#_CPPv4N27bk_ble_gap_ext_adv_params_t9peer_addrE "永久链接至目标")
    :   ext adv peer address

    [bk_ble_adv_filter_t](#_CPPv419bk_ble_adv_filter_t "bk_ble_adv_filter_t") filter_policy[](#_CPPv4N27bk_ble_gap_ext_adv_params_t13filter_policyE "永久链接至目标")
    :   ext adv filter policy

    int8_t tx_power[](#_CPPv4N27bk_ble_gap_ext_adv_params_t8tx_powerE "永久链接至目标")
    :   ext adv tx power

    [bk_ble_gap_pri_phy_t](#_CPPv420bk_ble_gap_pri_phy_t "bk_ble_gap_pri_phy_t") primary_phy[](#_CPPv4N27bk_ble_gap_ext_adv_params_t11primary_phyE "永久链接至目标")
    :   ext adv primary phy

    uint8_t max_skip[](#_CPPv4N27bk_ble_gap_ext_adv_params_t8max_skipE "永久链接至目标")
    :   ext adv maximum skip

    [bk_ble_gap_phy_t](#_CPPv416bk_ble_gap_phy_t "bk_ble_gap_phy_t") secondary_phy[](#_CPPv4N27bk_ble_gap_ext_adv_params_t13secondary_phyE "永久链接至目标")
    :   ext adv secondary phy

    uint8_t sid[](#_CPPv4N27bk_ble_gap_ext_adv_params_t3sidE "永久链接至目标")
    :   ext adv sid

    bool scan_req_notif[](#_CPPv4N27bk_ble_gap_ext_adv_params_t14scan_req_notifE "永久链接至目标")
    :   ext adv scan request event notify

struct bk_ble_ext_scan_cfg_t[](#_CPPv421bk_ble_ext_scan_cfg_t "永久链接至目标")
:   ext scan config

    Public Members

    [bk_ble_scan_type_t](#_CPPv418bk_ble_scan_type_t "bk_ble_scan_type_t") scan_type[](#_CPPv4N21bk_ble_ext_scan_cfg_t9scan_typeE "永久链接至目标")
    :   ext scan type

    uint16_t scan_interval[](#_CPPv4N21bk_ble_ext_scan_cfg_t13scan_intervalE "永久链接至目标")
    :   ext scan interval

    uint16_t scan_window[](#_CPPv4N21bk_ble_ext_scan_cfg_t11scan_windowE "永久链接至目标")
    :   ext scan window

struct bk_ble_ext_scan_params_t[](#_CPPv424bk_ble_ext_scan_params_t "永久链接至目标")
:   ext scan parameters

    Public Members

    [bk_ble_addr_type_t](#_CPPv418bk_ble_addr_type_t "bk_ble_addr_type_t") own_addr_type[](#_CPPv4N24bk_ble_ext_scan_params_t13own_addr_typeE "永久链接至目标")
    :   ext scan own address type

    [bk_ble_scan_filter_t](#_CPPv420bk_ble_scan_filter_t "bk_ble_scan_filter_t") filter_policy[](#_CPPv4N24bk_ble_ext_scan_params_t13filter_policyE "永久链接至目标")
    :   ext scan filter policy

    [bk_ble_scan_duplicate_t](#_CPPv423bk_ble_scan_duplicate_t "bk_ble_scan_duplicate_t") scan_duplicate[](#_CPPv4N24bk_ble_ext_scan_params_t14scan_duplicateE "永久链接至目标")
    :   ext scan duplicate scan

    [bk_ble_ext_scan_cfg_mask_t](#_CPPv426bk_ble_ext_scan_cfg_mask_t "bk_ble_ext_scan_cfg_mask_t") cfg_mask[](#_CPPv4N24bk_ble_ext_scan_params_t8cfg_maskE "永久链接至目标")
    :   ext scan config mask

    [bk_ble_ext_scan_cfg_t](#_CPPv421bk_ble_ext_scan_cfg_t "bk_ble_ext_scan_cfg_t") uncoded_cfg[](#_CPPv4N24bk_ble_ext_scan_params_t11uncoded_cfgE "永久链接至目标")
    :   ext scan uncoded config parameters

    [bk_ble_ext_scan_cfg_t](#_CPPv421bk_ble_ext_scan_cfg_t "bk_ble_ext_scan_cfg_t") coded_cfg[](#_CPPv4N24bk_ble_ext_scan_params_t9coded_cfgE "永久链接至目标")
    :   ext scan coded config parameters

struct bk_ble_gap_conn_params_t[](#_CPPv424bk_ble_gap_conn_params_t "永久链接至目标")
:   create extend connection parameters

    Public Members

    uint16_t scan_interval[](#_CPPv4N24bk_ble_gap_conn_params_t13scan_intervalE "永久链接至目标")
    :   init scan interval

    uint16_t scan_window[](#_CPPv4N24bk_ble_gap_conn_params_t11scan_windowE "永久链接至目标")
    :   init scan window

    uint16_t interval_min[](#_CPPv4N24bk_ble_gap_conn_params_t12interval_minE "永久链接至目标")
    :   minimum interval

    uint16_t interval_max[](#_CPPv4N24bk_ble_gap_conn_params_t12interval_maxE "永久链接至目标")
    :   maximum interval

    uint16_t latency[](#_CPPv4N24bk_ble_gap_conn_params_t7latencyE "永久链接至目标")
    :   ext scan type

    uint16_t supervision_timeout[](#_CPPv4N24bk_ble_gap_conn_params_t19supervision_timeoutE "永久链接至目标")
    :   connection supervision timeout

    uint16_t min_ce_len[](#_CPPv4N24bk_ble_gap_conn_params_t10min_ce_lenE "永久链接至目标")
    :   minimum ce length

    uint16_t max_ce_len[](#_CPPv4N24bk_ble_gap_conn_params_t10max_ce_lenE "永久链接至目标")
    :   maximum ce length

struct bk_ble_gap_ext_adv_t[](#_CPPv420bk_ble_gap_ext_adv_t "永久链接至目标")
:   extend adv enable parameters

    Public Members

    uint8_t instance[](#_CPPv4N20bk_ble_gap_ext_adv_t8instanceE "永久链接至目标")
    :   advertising handle

    int duration[](#_CPPv4N20bk_ble_gap_ext_adv_t8durationE "永久链接至目标")
    :   advertising duration

    int max_events[](#_CPPv4N20bk_ble_gap_ext_adv_t10max_eventsE "永久链接至目标")
    :   maximum number of extended advertising events

struct bk_ble_gap_periodic_adv_params_t[](#_CPPv432bk_ble_gap_periodic_adv_params_t "永久链接至目标")
:   periodic adv parameters

    Public Members

    uint16_t interval_min[](#_CPPv4N32bk_ble_gap_periodic_adv_params_t12interval_minE "永久链接至目标")
    :   periodic advertising minimum interval

    uint16_t interval_max[](#_CPPv4N32bk_ble_gap_periodic_adv_params_t12interval_maxE "永久链接至目标")
    :   periodic advertising maximum interval

    uint8_t properties[](#_CPPv4N32bk_ble_gap_periodic_adv_params_t10propertiesE "永久链接至目标")
    :   periodic advertising properties

struct bk_ble_gap_periodic_adv_sync_params_t[](#_CPPv437bk_ble_gap_periodic_adv_sync_params_t "永久链接至目标")
:   periodic adv sync parameters

    Public Members

    [bk_ble_gap_sync_t](#_CPPv417bk_ble_gap_sync_t "bk_ble_gap_sync_t") filter_policy[](#_CPPv4N37bk_ble_gap_periodic_adv_sync_params_t13filter_policyE "永久链接至目标")
    :   periodic advertising sync filter policy

    uint8_t sid[](#_CPPv4N37bk_ble_gap_periodic_adv_sync_params_t3sidE "永久链接至目标")
    :   periodic advertising sid

    [bk_ble_addr_type_t](#_CPPv418bk_ble_addr_type_t "bk_ble_addr_type_t") addr_type[](#_CPPv4N37bk_ble_gap_periodic_adv_sync_params_t9addr_typeE "永久链接至目标")
    :   periodic advertising address type

    [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") addr[](#_CPPv4N37bk_ble_gap_periodic_adv_sync_params_t4addrE "永久链接至目标")
    :   periodic advertising address

    uint16_t skip[](#_CPPv4N37bk_ble_gap_periodic_adv_sync_params_t4skipE "永久链接至目标")
    :   the maximum number of periodic advertising events that can be skipped

    uint16_t sync_timeout[](#_CPPv4N37bk_ble_gap_periodic_adv_sync_params_t12sync_timeoutE "永久链接至目标")
    :   synchronization timeout

struct bk_ble_gap_ext_adv_reprot_t[](#_CPPv427bk_ble_gap_ext_adv_reprot_t "永久链接至目标")
:   extend adv report parameters

    Public Members

    [bk_ble_gap_adv_type_t](#_CPPv421bk_ble_gap_adv_type_t "bk_ble_gap_adv_type_t") event_type[](#_CPPv4N27bk_ble_gap_ext_adv_reprot_t10event_typeE "永久链接至目标")
    :   extend advertising type

    uint8_t addr_type[](#_CPPv4N27bk_ble_gap_ext_adv_reprot_t9addr_typeE "永久链接至目标")
    :   extend advertising address type

    [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") addr[](#_CPPv4N27bk_ble_gap_ext_adv_reprot_t4addrE "永久链接至目标")
    :   extend advertising address

    [bk_ble_gap_pri_phy_t](#_CPPv420bk_ble_gap_pri_phy_t "bk_ble_gap_pri_phy_t") primary_phy[](#_CPPv4N27bk_ble_gap_ext_adv_reprot_t11primary_phyE "永久链接至目标")
    :   extend advertising primary phy

    [bk_ble_gap_phy_t](#_CPPv416bk_ble_gap_phy_t "bk_ble_gap_phy_t") secondly_phy[](#_CPPv4N27bk_ble_gap_ext_adv_reprot_t12secondly_phyE "永久链接至目标")
    :   extend advertising secondary phy

    uint8_t sid[](#_CPPv4N27bk_ble_gap_ext_adv_reprot_t3sidE "永久链接至目标")
    :   extend advertising sid

    uint8_t tx_power[](#_CPPv4N27bk_ble_gap_ext_adv_reprot_t8tx_powerE "永久链接至目标")
    :   extend advertising tx power

    int8_t rssi[](#_CPPv4N27bk_ble_gap_ext_adv_reprot_t4rssiE "永久链接至目标")
    :   extend advertising rssi

    uint16_t per_adv_interval[](#_CPPv4N27bk_ble_gap_ext_adv_reprot_t16per_adv_intervalE "永久链接至目标")
    :   periodic advertising interval

    uint8_t dir_addr_type[](#_CPPv4N27bk_ble_gap_ext_adv_reprot_t13dir_addr_typeE "永久链接至目标")
    :   direct address type

    [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") dir_addr[](#_CPPv4N27bk_ble_gap_ext_adv_reprot_t8dir_addrE "永久链接至目标")
    :   direct address

    [bk_ble_gap_ext_adv_data_status_t](#_CPPv432bk_ble_gap_ext_adv_data_status_t "bk_ble_gap_ext_adv_data_status_t") data_status[](#_CPPv4N27bk_ble_gap_ext_adv_reprot_t11data_statusE "永久链接至目标")
    :   data type

    uint8_t adv_data_len[](#_CPPv4N27bk_ble_gap_ext_adv_reprot_t12adv_data_lenE "永久链接至目标")
    :   extend advertising data length

    uint8_t adv_data[251][](#_CPPv4N27bk_ble_gap_ext_adv_reprot_t8adv_dataE "永久链接至目标")
    :   extend advertising data

struct bk_ble_gap_periodic_adv_report_t[](#_CPPv432bk_ble_gap_periodic_adv_report_t "永久链接至目标")
:   periodic adv report parameters

    Public Members

    uint16_t sync_handle[](#_CPPv4N32bk_ble_gap_periodic_adv_report_t11sync_handleE "永久链接至目标")
    :   periodic advertising train handle

    uint8_t tx_power[](#_CPPv4N32bk_ble_gap_periodic_adv_report_t8tx_powerE "永久链接至目标")
    :   periodic advertising tx power

    int8_t rssi[](#_CPPv4N32bk_ble_gap_periodic_adv_report_t4rssiE "永久链接至目标")
    :   periodic advertising rssi

    [bk_ble_gap_ext_adv_data_status_t](#_CPPv432bk_ble_gap_ext_adv_data_status_t "bk_ble_gap_ext_adv_data_status_t") data_status[](#_CPPv4N32bk_ble_gap_periodic_adv_report_t11data_statusE "永久链接至目标")
    :   periodic advertising data type

    uint8_t data_length[](#_CPPv4N32bk_ble_gap_periodic_adv_report_t11data_lengthE "永久链接至目标")
    :   periodic advertising data length

    uint8_t data[251][](#_CPPv4N32bk_ble_gap_periodic_adv_report_t4dataE "永久链接至目标")
    :   periodic advertising data

struct bk_ble_gap_periodic_adv_sync_estab_t[](#_CPPv436bk_ble_gap_periodic_adv_sync_estab_t "永久链接至目标")
:   perodic adv sync establish parameters

    Public Members

    uint8_t status[](#_CPPv4N36bk_ble_gap_periodic_adv_sync_estab_t6statusE "永久链接至目标")
    :   periodic advertising sync status

    uint16_t sync_handle[](#_CPPv4N36bk_ble_gap_periodic_adv_sync_estab_t11sync_handleE "永久链接至目标")
    :   periodic advertising train handle

    uint8_t sid[](#_CPPv4N36bk_ble_gap_periodic_adv_sync_estab_t3sidE "永久链接至目标")
    :   periodic advertising sid

    [bk_ble_addr_type_t](#_CPPv418bk_ble_addr_type_t "bk_ble_addr_type_t") addr_type[](#_CPPv4N36bk_ble_gap_periodic_adv_sync_estab_t9addr_typeE "永久链接至目标")
    :   periodic advertising address type

    [bk_bd_addr_t](#_CPPv412bk_bd_addr_t "bk_bd_addr_t") adv_addr[](#_CPPv4N36bk_ble_gap_periodic_adv_sync_estab_t8adv_addrE "永久链接至目标")
    :   periodic advertising address

    [bk_ble_gap_phy_t](#_CPPv416bk_ble_gap_phy_t "bk_ble_gap_phy_t") adv_phy[](#_CPPv4N36bk_ble_gap_periodic_adv_sync_estab_t7adv_phyE "永久链接至目标")
    :   periodic advertising adv phy type

    uint16_t period_adv_interval[](#_CPPv4N36bk_ble_gap_periodic_adv_sync_estab_t19period_adv_intervalE "永久链接至目标")
    :   periodic advertising interval

    uint8_t adv_clk_accuracy[](#_CPPv4N36bk_ble_gap_periodic_adv_sync_estab_t16adv_clk_accuracyE "永久链接至目标")
    :   periodic advertising clock accuracy


### Macros[](#id12 "永久链接至标题")

BK_BLE_ONLY_ACCEPT_SPECIFIED_AUTH_DISABLE[](#c.BK_BLE_ONLY_ACCEPT_SPECIFIED_AUTH_DISABLE "永久链接至目标")
:   authentication disable

BK_BLE_ONLY_ACCEPT_SPECIFIED_AUTH_ENABLE[](#c.BK_BLE_ONLY_ACCEPT_SPECIFIED_AUTH_ENABLE "永久链接至目标")
:   authentication enable

BK_BLE_GAP_CHANNELS_LEN[](#c.BK_BLE_GAP_CHANNELS_LEN "永久链接至目标")
:   channel length

BK_BLE_ADV_DATA_LEN_MAX[](#c.BK_BLE_ADV_DATA_LEN_MAX "永久链接至目标")
:   Advertising data maximum length.

BK_BLE_SCAN_RSP_DATA_LEN_MAX[](#c.BK_BLE_SCAN_RSP_DATA_LEN_MAX "永久链接至目标")
:   Scan response data maximum length.

BK_BLE_GAP_SET_EXT_ADV_PROP_LEGACY_IND[](#c.BK_BLE_GAP_SET_EXT_ADV_PROP_LEGACY_IND "永久链接至目标")
:   ADV_DIRECT_IND (low duty cycle)

BK_BLE_GAP_SET_EXT_ADV_PROP_LEGACY_LD_DIR[](#c.BK_BLE_GAP_SET_EXT_ADV_PROP_LEGACY_LD_DIR "永久链接至目标")
:   ADV_DIRECT_IND (high duty cycle)

BK_BLE_GAP_SET_EXT_ADV_PROP_LEGACY_HD_DIR[](#c.BK_BLE_GAP_SET_EXT_ADV_PROP_LEGACY_HD_DIR "永久链接至目标")
:   ADV_SCAN_IND

BK_BLE_GAP_SET_EXT_ADV_PROP_LEGACY_SCAN[](#c.BK_BLE_GAP_SET_EXT_ADV_PROP_LEGACY_SCAN "永久链接至目标")
:   ADV_NONCONN_IND

BK_BLE_GAP_SET_EXT_ADV_PROP_LEGACY_NONCONN[](#c.BK_BLE_GAP_SET_EXT_ADV_PROP_LEGACY_NONCONN "永久链接至目标")

EXT_ADV_TX_PWR_NO_PREFERENCE[](#c.EXT_ADV_TX_PWR_NO_PREFERENCE "永久链接至目标")
:   Extend advertising tx power, range: [-127, +126] dBm.

    host has no preference for tx power


### Type Definitions[](#id13 "永久链接至标题")

typedef uint8_t bk_ble_key_type_t[](#_CPPv417bk_ble_key_type_t "永久链接至目标")
:   see bk_le_key_enum_t

typedef uint8_t bk_ble_key_mask_t[](#_CPPv417bk_ble_key_mask_t "永久链接至目标")
:   see bk_le_key_enum_t

typedef uint8_t bk_ble_auth_req_t[](#_CPPv417bk_ble_auth_req_t "永久链接至目标")
:   see bk_le_auth_enum_t

typedef uint8_t bk_ble_gap_channels[BK_BLE_GAP_CHANNELS_LEN][](#_CPPv419bk_ble_gap_channels "永久链接至目标")

typedef uint16_t bk_ble_ext_adv_type_mask_t[](#_CPPv426bk_ble_ext_adv_type_mask_t "永久链接至目标")
:   such as BK_BLE_GAP_SET_EXT_ADV_PROP_CONNECTABLE and BK_BLE_GAP_SET_EXT_ADV_PROP_LEGACY_IND

typedef uint8_t bk_ble_gap_phy_t[](#_CPPv416bk_ble_gap_phy_t "永久链接至目标")
:   see bk_ble_gap_phy_enum_t

typedef uint8_t bk_ble_gap_all_phys_t[](#_CPPv421bk_ble_gap_all_phys_t "永久链接至目标")

typedef uint8_t bk_ble_gap_pri_phy_t[](#_CPPv420bk_ble_gap_pri_phy_t "永久链接至目标")
:   see bk_ble_gap_pri_phy_enum_t

typedef uint8_t bk_ble_gap_phy_mask_t[](#_CPPv421bk_ble_gap_phy_mask_t "永久链接至目标")
:   see bk_ble_gap_phy_pref_enum_t

typedef uint16_t bk_ble_gap_prefer_phy_options_t[](#_CPPv431bk_ble_gap_prefer_phy_options_t "永久链接至目标")
:   see bk_ble_gap_coded_phy_pref_enum_t

typedef uint8_t bk_ble_ext_scan_cfg_mask_t[](#_CPPv426bk_ble_ext_scan_cfg_mask_t "永久链接至目标")
:   see bk_ble_gap_ext_scan_cfg_enum_t

typedef uint8_t bk_ble_gap_ext_adv_data_status_t[](#_CPPv432bk_ble_gap_ext_adv_data_status_t "永久链接至目标")
:   see bk_ble_gap_ext_adv_data_seg_enum_t

typedef uint8_t bk_ble_gap_sync_t[](#_CPPv417bk_ble_gap_sync_t "永久链接至目标")
:   see bk_ble_gap_sync_policy_enum_t

typedef uint8_t bk_ble_gap_adv_type_t[](#_CPPv421bk_ble_gap_adv_type_t "永久链接至目标")
:   see bk_ble_adv_report_ext_type_enum_t

typedef void (*bk_ble_gap_cb_t)([bk_ble_gap_cb_event_t](#_CPPv421bk_ble_gap_cb_event_t "bk_ble_gap_cb_event_t") event, [bk_ble_gap_cb_param_t](#_CPPv421bk_ble_gap_cb_param_t "bk_ble_gap_cb_param_t") *param)[](#_CPPv415bk_ble_gap_cb_t "永久链接至目标")
:   GAP callback function type, todo: modify docx.

    Param event
    :   : Event type

    Param param
    :   : Point to callback parameter, currently is union type


### Enumerations[](#id14 "永久链接至标题")

enum bk_le_key_enum_t[](#_CPPv416bk_le_key_enum_t "永久链接至目标")
:   *Values:*

    enumerator BK_LE_KEY_NONE[](#_CPPv4N16bk_le_key_enum_t14BK_LE_KEY_NONEE "永久链接至目标")
    :   No encryption key

    enumerator BK_LE_KEY_PENC[](#_CPPv4N16bk_le_key_enum_t14BK_LE_KEY_PENCE "永久链接至目标")
    :   encryption key, encryption information of peer device

    enumerator BK_LE_KEY_PID[](#_CPPv4N16bk_le_key_enum_t13BK_LE_KEY_PIDE "永久链接至目标")
    :   identity key of the peer device

    enumerator BK_LE_KEY_PCSRK[](#_CPPv4N16bk_le_key_enum_t15BK_LE_KEY_PCSRKE "永久链接至目标")
    :   peer SRK

    enumerator BK_LE_KEY_PLK[](#_CPPv4N16bk_le_key_enum_t13BK_LE_KEY_PLKE "永久链接至目标")
    :   Link key

    enumerator BK_LE_KEY_LLK[](#_CPPv4N16bk_le_key_enum_t13BK_LE_KEY_LLKE "永久链接至目标")
    :   link key

    enumerator BK_LE_KEY_LENC[](#_CPPv4N16bk_le_key_enum_t14BK_LE_KEY_LENCE "永久链接至目标")
    :   master role security information:div

    enumerator BK_LE_KEY_LID[](#_CPPv4N16bk_le_key_enum_t13BK_LE_KEY_LIDE "永久链接至目标")
    :   master device ID key

    enumerator BK_LE_KEY_LCSRK[](#_CPPv4N16bk_le_key_enum_t15BK_LE_KEY_LCSRKE "永久链接至目标")
    :   local CSRK has been deliver to peer

enum bk_le_auth_enum_t[](#_CPPv417bk_le_auth_enum_t "永久链接至目标")
:   *Values:*

    enumerator BK_LE_AUTH_NO_BOND[](#_CPPv4N17bk_le_auth_enum_t18BK_LE_AUTH_NO_BONDE "永久链接至目标")
    :   0 no bondingv

    enumerator BK_LE_AUTH_BOND[](#_CPPv4N17bk_le_auth_enum_t15BK_LE_AUTH_BONDE "永久链接至目标")
    :   1 << 0 device in the bonding with peer

    enumerator BK_LE_AUTH_REQ_MITM[](#_CPPv4N17bk_le_auth_enum_t19BK_LE_AUTH_REQ_MITME "永久链接至目标")
    :   1 << 2 man in the middle attack

    enumerator BK_LE_AUTH_REQ_BOND_MITM[](#_CPPv4N17bk_le_auth_enum_t24BK_LE_AUTH_REQ_BOND_MITME "永久链接至目标")
    :   0101 banding with man in the middle attack

    enumerator BK_LE_AUTH_REQ_SC_ONLY[](#_CPPv4N17bk_le_auth_enum_t22BK_LE_AUTH_REQ_SC_ONLYE "永久链接至目标")
    :   1 << 3 secure connection

    enumerator BK_LE_AUTH_REQ_SC_BOND[](#_CPPv4N17bk_le_auth_enum_t22BK_LE_AUTH_REQ_SC_BONDE "永久链接至目标")
    :   1001 secure connection with band

    enumerator BK_LE_AUTH_REQ_SC_MITM[](#_CPPv4N17bk_le_auth_enum_t22BK_LE_AUTH_REQ_SC_MITME "永久链接至目标")
    :   1100 secure conn with MITM

    enumerator BK_LE_AUTH_REQ_SC_MITM_BOND[](#_CPPv4N17bk_le_auth_enum_t27BK_LE_AUTH_REQ_SC_MITM_BONDE "永久链接至目标")
    :   1101 SC with MITM and Bonding

enum bk_io_cap_enum_t[](#_CPPv416bk_io_cap_enum_t "永久链接至目标")
:   IO capability.


    *Values:*

    enumerator BK_IO_CAP_DISPLAY_ONLY[](#_CPPv4N16bk_io_cap_enum_t22BK_IO_CAP_DISPLAY_ONLYE "永久链接至目标")
    :   output: display, input: none

    enumerator BK_IO_CAP_DISPLAY_YESNO[](#_CPPv4N16bk_io_cap_enum_t23BK_IO_CAP_DISPLAY_YESNOE "永久链接至目标")
    :   output: display, input: yes or no

    enumerator BK_IO_CAP_KEYBOARD_ONLY[](#_CPPv4N16bk_io_cap_enum_t23BK_IO_CAP_KEYBOARD_ONLYE "永久链接至目标")
    :   output: none, input: keyboard. note: when both local and peer are keyboard only, both side should input same passkey which negotiated in other way, such as oral speak

    enumerator BK_IO_CAP_NONE[](#_CPPv4N16bk_io_cap_enum_t14BK_IO_CAP_NONEE "永久链接至目标")
    :   NoInputNoOutput

    enumerator BK_IO_CAP_KEYBOARD_DISPLAY[](#_CPPv4N16bk_io_cap_enum_t26BK_IO_CAP_KEYBOARD_DISPLAYE "永久链接至目标")
    :   output: display, input: keyboard

enum bk_ble_gap_cb_event_t[](#_CPPv421bk_ble_gap_cb_event_t "永久链接至目标")
:   GAP BLE callback event type.


    *Values:*

    enumerator BK_BLE_GAP_ADV_DATA_SET_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t36BK_BLE_GAP_ADV_DATA_SET_COMPLETE_EVTE "永久链接至目标")
    :   When advertising data set complete, the event comes

    enumerator BK_BLE_GAP_SCAN_RSP_DATA_SET_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t41BK_BLE_GAP_SCAN_RSP_DATA_SET_COMPLETE_EVTE "永久链接至目标")
    :   When scan response data set complete, the event comes

    enumerator BK_BLE_GAP_SCAN_PARAM_SET_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t38BK_BLE_GAP_SCAN_PARAM_SET_COMPLETE_EVTE "永久链接至目标")
    :   When scan parameters set complete, the event comes

    enumerator BK_BLE_GAP_SCAN_RESULT_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t26BK_BLE_GAP_SCAN_RESULT_EVTE "永久链接至目标")
    :   When one scan result ready, the event comes each time

    enumerator BK_BLE_GAP_ADV_DATA_RAW_SET_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t40BK_BLE_GAP_ADV_DATA_RAW_SET_COMPLETE_EVTE "永久链接至目标")
    :   When raw advertising data set complete, the event comes

    enumerator BK_BLE_GAP_SCAN_RSP_DATA_RAW_SET_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t45BK_BLE_GAP_SCAN_RSP_DATA_RAW_SET_COMPLETE_EVTE "永久链接至目标")
    :   When raw advertising data set complete, the event comes

    enumerator BK_BLE_GAP_ADV_START_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t33BK_BLE_GAP_ADV_START_COMPLETE_EVTE "永久链接至目标")
    :   When start advertising complete, the event comes

    enumerator BK_BLE_GAP_SCAN_START_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t34BK_BLE_GAP_SCAN_START_COMPLETE_EVTE "永久链接至目标")
    :   When start scan complete, the event comes

    enumerator BK_BLE_GAP_AUTH_CMPL_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t24BK_BLE_GAP_AUTH_CMPL_EVTE "永久链接至目标")
    :   Authentication complete indication, param is [bk_ble_sec_t](#unionbk__ble__sec__t "#unionbk__ble__sec__t").

    enumerator BK_BLE_GAP_KEY_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t18BK_BLE_GAP_KEY_EVTE "永久链接至目标")
    :   BLE key event for peer device keys, param is [bk_ble_sec_t](#unionbk__ble__sec__t "#unionbk__ble__sec__t")

    enumerator BK_BLE_GAP_SEC_REQ_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t22BK_BLE_GAP_SEC_REQ_EVTE "永久链接至目标")
    :   BLE security request, param is [bk_ble_sec_t](#unionbk__ble__sec__t "#unionbk__ble__sec__t").

    enumerator BK_BLE_GAP_PASSKEY_NOTIF_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t28BK_BLE_GAP_PASSKEY_NOTIF_EVTE "永久链接至目标")
    :   passkey notification event, param is [bk_ble_sec_t](#unionbk__ble__sec__t "#unionbk__ble__sec__t")

    enumerator BK_BLE_GAP_PASSKEY_REQ_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t26BK_BLE_GAP_PASSKEY_REQ_EVTE "永久链接至目标")
    :   passkey request event, param is [bk_ble_sec_t](#unionbk__ble__sec__t "#unionbk__ble__sec__t")

    enumerator BK_BLE_GAP_OOB_REQ_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t22BK_BLE_GAP_OOB_REQ_EVTE "永久链接至目标")
    :   OOB request event, param is [bk_ble_sec_t](#unionbk__ble__sec__t "#unionbk__ble__sec__t")

    enumerator BK_BLE_GAP_LOCAL_IR_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t23BK_BLE_GAP_LOCAL_IR_EVTE "永久链接至目标")
    :   BLE local IR (Encryption Root value used to generate identity resolving key) event

    enumerator BK_BLE_GAP_LOCAL_ER_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t23BK_BLE_GAP_LOCAL_ER_EVTE "永久链接至目标")
    :   BLE local ER (identity Root 128-bit random static value used to generate Long Term Key) event

    enumerator BK_BLE_GAP_NC_REQ_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t21BK_BLE_GAP_NC_REQ_EVTE "永久链接至目标")
    :   Numeric Comparison request event, param is [bk_ble_sec_t](#unionbk__ble__sec__t "#unionbk__ble__sec__t")

    enumerator BK_BLE_GAP_BOND_KEY_REQ_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t27BK_BLE_GAP_BOND_KEY_REQ_EVTE "永久链接至目标")
    :   the mapping relation of param.ble_key.key_type is : when BK_LE_KEY_LENC, app need reply BK_LE_KEY_LENC with bk_ble_pair_key_reply according compare param.ble_key.lenc_key

    enumerator BK_BLE_GAP_BOND_KEY_GENERATE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t32BK_BLE_GAP_BOND_KEY_GENERATE_EVTE "永久链接至目标")
    :   app layer should save to storage for next power on.

    enumerator BK_BLE_GAP_BOND_DEV_LIST_OPERATEION_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t48BK_BLE_GAP_BOND_DEV_LIST_OPERATEION_COMPLETE_EVTE "永久链接至目标")

    enumerator BK_BLE_GAP_ADV_STOP_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t32BK_BLE_GAP_ADV_STOP_COMPLETE_EVTE "永久链接至目标")
    :   When stop adv complete, the event comes

    enumerator BK_BLE_GAP_SCAN_STOP_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t33BK_BLE_GAP_SCAN_STOP_COMPLETE_EVTE "永久链接至目标")
    :   When stop scan complete, the event comes

    enumerator BK_BLE_GAP_SET_STATIC_RAND_ADDR_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t35BK_BLE_GAP_SET_STATIC_RAND_ADDR_EVTE "永久链接至目标")
    :   When set the static rand address complete, the event comes

    enumerator BK_BLE_GAP_UPDATE_CONN_PARAMS_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t33BK_BLE_GAP_UPDATE_CONN_PARAMS_EVTE "永久链接至目标")
    :   When update connection parameters complete, the event comes

    enumerator BK_BLE_GAP_SET_PKT_LENGTH_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t38BK_BLE_GAP_SET_PKT_LENGTH_COMPLETE_EVTE "永久链接至目标")
    :   When set pkt length complete, the event comes

    enumerator BK_BLE_GAP_SET_LOCAL_PRIVACY_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t41BK_BLE_GAP_SET_LOCAL_PRIVACY_COMPLETE_EVTE "永久链接至目标")
    :   When Enable/disable privacy on the local device complete, the event comes

    enumerator BK_BLE_GAP_READ_RSSI_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t33BK_BLE_GAP_READ_RSSI_COMPLETE_EVTE "永久链接至目标")
    :   When read the rssi complete, the event comes

    enumerator BK_BLE_GAP_UPDATE_WHITELIST_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t40BK_BLE_GAP_UPDATE_WHITELIST_COMPLETE_EVTE "永久链接至目标")
    :   When add or remove whitelist complete, the event comes

    enumerator BK_BLE_GAP_UPDATE_DUPLICATE_EXCEPTIONAL_LIST_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t57BK_BLE_GAP_UPDATE_DUPLICATE_EXCEPTIONAL_LIST_COMPLETE_EVTE "永久链接至目标")
    :   When update duplicate exceptional list complete, the event comes

    enumerator BK_BLE_GAP_SET_CHANNELS_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t36BK_BLE_GAP_SET_CHANNELS_COMPLETE_EVTE "永久链接至目标")
    :   When setting BLE channels complete, the event comes

    enumerator BK_BLE_GAP_READ_PHY_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t32BK_BLE_GAP_READ_PHY_COMPLETE_EVTE "永久链接至目标")
    :   when reading phy complete, this event comes

    enumerator BK_BLE_GAP_SET_PREFERRED_DEFAULT_PHY_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t49BK_BLE_GAP_SET_PREFERRED_DEFAULT_PHY_COMPLETE_EVTE "永久链接至目标")
    :   when preferred default phy complete, this event comes

    enumerator BK_BLE_GAP_SET_PREFERRED_PHY_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t41BK_BLE_GAP_SET_PREFERRED_PHY_COMPLETE_EVTE "永久链接至目标")
    :   when preferred phy complete , this event comes

    enumerator BK_BLE_GAP_EXT_ADV_SET_RAND_ADDR_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t45BK_BLE_GAP_EXT_ADV_SET_RAND_ADDR_COMPLETE_EVTE "永久链接至目标")
    :   when extended set random address complete, the event comes

    enumerator BK_BLE_GAP_EXT_ADV_PARAMS_SET_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t42BK_BLE_GAP_EXT_ADV_PARAMS_SET_COMPLETE_EVTE "永久链接至目标")
    :   when extended advertising parameter complete, the event comes

    enumerator BK_BLE_GAP_EXT_ADV_DATA_SET_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t40BK_BLE_GAP_EXT_ADV_DATA_SET_COMPLETE_EVTE "永久链接至目标")
    :   when extended advertising data complete, the event comes

    enumerator BK_BLE_GAP_EXT_SCAN_RSP_DATA_SET_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t45BK_BLE_GAP_EXT_SCAN_RSP_DATA_SET_COMPLETE_EVTE "永久链接至目标")
    :   when extended scan response data complete, the event comes

    enumerator BK_BLE_GAP_EXT_ADV_DATA_RAW_SET_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t44BK_BLE_GAP_EXT_ADV_DATA_RAW_SET_COMPLETE_EVTE "永久链接至目标")
    :   when raw extended advertising data complete, the event comes

    enumerator BK_BLE_GAP_EXT_SCAN_RSP_DATA_RAW_SET_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t49BK_BLE_GAP_EXT_SCAN_RSP_DATA_RAW_SET_COMPLETE_EVTE "永久链接至目标")
    :   when raw extended scan response data complete, the event comes

    enumerator BK_BLE_GAP_EXT_ADV_START_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t37BK_BLE_GAP_EXT_ADV_START_COMPLETE_EVTE "永久链接至目标")
    :   when extended advertising start complete, the event comes

    enumerator BK_BLE_GAP_EXT_ADV_STOP_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t36BK_BLE_GAP_EXT_ADV_STOP_COMPLETE_EVTE "永久链接至目标")
    :   when extended advertising stop complete, the event comes

    enumerator BK_BLE_GAP_EXT_ADV_SET_REMOVE_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t42BK_BLE_GAP_EXT_ADV_SET_REMOVE_COMPLETE_EVTE "永久链接至目标")
    :   when extended advertising set remove complete, the event comes

    enumerator BK_BLE_GAP_EXT_ADV_SET_CLEAR_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t41BK_BLE_GAP_EXT_ADV_SET_CLEAR_COMPLETE_EVTE "永久链接至目标")
    :   when extended advertising set clear complete, the event comes

    enumerator BK_BLE_GAP_PERIODIC_ADV_SET_PARAMS_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t47BK_BLE_GAP_PERIODIC_ADV_SET_PARAMS_COMPLETE_EVTE "永久链接至目标")
    :   when periodic advertising parameter complete, the event comes

    enumerator BK_BLE_GAP_PERIODIC_ADV_DATA_SET_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t45BK_BLE_GAP_PERIODIC_ADV_DATA_SET_COMPLETE_EVTE "永久链接至目标")
    :   when periodic advertising data complete, the event comes

    enumerator BK_BLE_GAP_PERIODIC_ADV_START_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t42BK_BLE_GAP_PERIODIC_ADV_START_COMPLETE_EVTE "永久链接至目标")
    :   when periodic advertising start complete, the event comes

    enumerator BK_BLE_GAP_PERIODIC_ADV_STOP_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t41BK_BLE_GAP_PERIODIC_ADV_STOP_COMPLETE_EVTE "永久链接至目标")
    :   when periodic advertising stop complete, the event comes

    enumerator BK_BLE_GAP_PERIODIC_ADV_CREATE_SYNC_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t48BK_BLE_GAP_PERIODIC_ADV_CREATE_SYNC_COMPLETE_EVTE "永久链接至目标")
    :   when periodic advertising create sync complete, the event comes

    enumerator BK_BLE_GAP_PERIODIC_ADV_SYNC_CANCEL_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t48BK_BLE_GAP_PERIODIC_ADV_SYNC_CANCEL_COMPLETE_EVTE "永久链接至目标")
    :   when extended advertising sync cancel complete, the event comes

    enumerator BK_BLE_GAP_PERIODIC_ADV_SYNC_TERMINATE_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t51BK_BLE_GAP_PERIODIC_ADV_SYNC_TERMINATE_COMPLETE_EVTE "永久链接至目标")
    :   when extended advertising sync terminate complete, the event comes

    enumerator BK_BLE_GAP_PERIODIC_ADV_ADD_DEV_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t44BK_BLE_GAP_PERIODIC_ADV_ADD_DEV_COMPLETE_EVTE "永久链接至目标")
    :   when extended advertising add device complete , the event comes

    enumerator BK_BLE_GAP_PERIODIC_ADV_REMOVE_DEV_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t47BK_BLE_GAP_PERIODIC_ADV_REMOVE_DEV_COMPLETE_EVTE "永久链接至目标")
    :   when extended advertising remove device complete, the event comes

    enumerator BK_BLE_GAP_PERIODIC_ADV_CLEAR_DEV_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t46BK_BLE_GAP_PERIODIC_ADV_CLEAR_DEV_COMPLETE_EVTE "永久链接至目标")
    :   when extended advertising clear device, the event comes

    enumerator BK_BLE_GAP_EXT_SCAN_PARAMS_SET_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t43BK_BLE_GAP_EXT_SCAN_PARAMS_SET_COMPLETE_EVTE "永久链接至目标")
    :   when extended scan parameter complete, the event comes

    enumerator BK_BLE_GAP_EXT_SCAN_START_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t38BK_BLE_GAP_EXT_SCAN_START_COMPLETE_EVTE "永久链接至目标")
    :   when extended scan start complete, the event comes

    enumerator BK_BLE_GAP_EXT_SCAN_STOP_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t37BK_BLE_GAP_EXT_SCAN_STOP_COMPLETE_EVTE "永久链接至目标")
    :   when extended scan stop complete, the event comes

    enumerator BK_BLE_GAP_PREFER_EXT_CONN_PARAMS_SET_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t50BK_BLE_GAP_PREFER_EXT_CONN_PARAMS_SET_COMPLETE_EVTE "永久链接至目标")
    :   when extended prefer connection parameter set complete, the event comes

    enumerator BK_BLE_GAP_PHY_UPDATE_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t34BK_BLE_GAP_PHY_UPDATE_COMPLETE_EVTE "永久链接至目标")
    :   when ble phy update complete, the event comes

    enumerator BK_BLE_GAP_EXT_ADV_REPORT_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t29BK_BLE_GAP_EXT_ADV_REPORT_EVTE "永久链接至目标")
    :   when extended advertising report complete, the event comes

    enumerator BK_BLE_GAP_SCAN_TIMEOUT_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t27BK_BLE_GAP_SCAN_TIMEOUT_EVTE "永久链接至目标")
    :   when scan timeout complete, the event comes

    enumerator BK_BLE_GAP_ADV_TERMINATED_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t29BK_BLE_GAP_ADV_TERMINATED_EVTE "永久链接至目标")
    :   when advertising terminate data complete, the event comes

    enumerator BK_BLE_GAP_SCAN_REQ_RECEIVED_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t32BK_BLE_GAP_SCAN_REQ_RECEIVED_EVTE "永久链接至目标")
    :   when scan req received complete, the event comes

    enumerator BK_BLE_GAP_CHANNEL_SELECT_ALGORITHM_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t39BK_BLE_GAP_CHANNEL_SELECT_ALGORITHM_EVTE "永久链接至目标")
    :   when channel select algorithm complete, the event comes

    enumerator BK_BLE_GAP_PERIODIC_ADV_REPORT_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t34BK_BLE_GAP_PERIODIC_ADV_REPORT_EVTE "永久链接至目标")
    :   when periodic report advertising complete, the event comes

    enumerator BK_BLE_GAP_PERIODIC_ADV_SYNC_LOST_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t37BK_BLE_GAP_PERIODIC_ADV_SYNC_LOST_EVTE "永久链接至目标")
    :   when periodic advertising sync lost complete, the event comes

    enumerator BK_BLE_GAP_PERIODIC_ADV_SYNC_ESTAB_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t38BK_BLE_GAP_PERIODIC_ADV_SYNC_ESTAB_EVTE "永久链接至目标")
    :   when periodic advertising sync establish complete, the event comes

    enumerator BK_BLE_GAP_CONNECT_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t31BK_BLE_GAP_CONNECT_COMPLETE_EVTE "永久链接至目标")
    :   when ble connection complete, the event comes

    enumerator BK_BLE_GAP_DISCONNECT_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t34BK_BLE_GAP_DISCONNECT_COMPLETE_EVTE "永久链接至目标")
    :   when ble disconnect complete, the event comes

    enumerator BK_BLE_GAP_CONNECT_CANCEL_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t29BK_BLE_GAP_CONNECT_CANCEL_EVTE "永久链接至目标")
    :   when ble connect cancel complete, the event comes

    enumerator BK_BLE_GAP_UPDATE_CONN_PARAMS_REQ_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t37BK_BLE_GAP_UPDATE_CONN_PARAMS_REQ_EVTE "永久链接至目标")
    :   when peer req update param, the event comes

    enumerator BK_BLE_GAP_SET_SECURITY_PARAMS_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t43BK_BLE_GAP_SET_SECURITY_PARAMS_COMPLETE_EVTE "永久链接至目标")
    :   when set security params complete, the event comes

    enumerator BK_BLE_GAP_GENERATE_RPA_COMPLETE_EVT[](#_CPPv4N21bk_ble_gap_cb_event_t36BK_BLE_GAP_GENERATE_RPA_COMPLETE_EVTE "永久链接至目标")
    :   when generate rpa complete, the event comes

    enumerator BK_BLE_GAP_EVT_MAX[](#_CPPv4N21bk_ble_gap_cb_event_t18BK_BLE_GAP_EVT_MAXE "永久链接至目标")
    :   when maximum advertising event complete, the event comes

enum bk_ble_adv_data_type[](#_CPPv420bk_ble_adv_data_type "永久链接至目标")
:   The type of advertising data(not adv_type)


    *Values:*

    enumerator BK_BLE_AD_TYPE_FLAG[](#_CPPv4N20bk_ble_adv_data_type19BK_BLE_AD_TYPE_FLAGE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_16SRV_PART[](#_CPPv4N20bk_ble_adv_data_type25BK_BLE_AD_TYPE_16SRV_PARTE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_16SRV_CMPL[](#_CPPv4N20bk_ble_adv_data_type25BK_BLE_AD_TYPE_16SRV_CMPLE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_32SRV_PART[](#_CPPv4N20bk_ble_adv_data_type25BK_BLE_AD_TYPE_32SRV_PARTE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_32SRV_CMPL[](#_CPPv4N20bk_ble_adv_data_type25BK_BLE_AD_TYPE_32SRV_CMPLE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_128SRV_PART[](#_CPPv4N20bk_ble_adv_data_type26BK_BLE_AD_TYPE_128SRV_PARTE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_128SRV_CMPL[](#_CPPv4N20bk_ble_adv_data_type26BK_BLE_AD_TYPE_128SRV_CMPLE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_NAME_SHORT[](#_CPPv4N20bk_ble_adv_data_type25BK_BLE_AD_TYPE_NAME_SHORTE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_NAME_CMPL[](#_CPPv4N20bk_ble_adv_data_type24BK_BLE_AD_TYPE_NAME_CMPLE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_TX_PWR[](#_CPPv4N20bk_ble_adv_data_type21BK_BLE_AD_TYPE_TX_PWRE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_DEV_CLASS[](#_CPPv4N20bk_ble_adv_data_type24BK_BLE_AD_TYPE_DEV_CLASSE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_SM_TK[](#_CPPv4N20bk_ble_adv_data_type20BK_BLE_AD_TYPE_SM_TKE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_SM_OOB_FLAG[](#_CPPv4N20bk_ble_adv_data_type26BK_BLE_AD_TYPE_SM_OOB_FLAGE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_INT_RANGE[](#_CPPv4N20bk_ble_adv_data_type24BK_BLE_AD_TYPE_INT_RANGEE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_SOL_SRV_UUID[](#_CPPv4N20bk_ble_adv_data_type27BK_BLE_AD_TYPE_SOL_SRV_UUIDE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_128SOL_SRV_UUID[](#_CPPv4N20bk_ble_adv_data_type30BK_BLE_AD_TYPE_128SOL_SRV_UUIDE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_SERVICE_DATA[](#_CPPv4N20bk_ble_adv_data_type27BK_BLE_AD_TYPE_SERVICE_DATAE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_PUBLIC_TARGET[](#_CPPv4N20bk_ble_adv_data_type28BK_BLE_AD_TYPE_PUBLIC_TARGETE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_RANDOM_TARGET[](#_CPPv4N20bk_ble_adv_data_type28BK_BLE_AD_TYPE_RANDOM_TARGETE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_APPEARANCE[](#_CPPv4N20bk_ble_adv_data_type25BK_BLE_AD_TYPE_APPEARANCEE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_ADV_INT[](#_CPPv4N20bk_ble_adv_data_type22BK_BLE_AD_TYPE_ADV_INTE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_LE_DEV_ADDR[](#_CPPv4N20bk_ble_adv_data_type26BK_BLE_AD_TYPE_LE_DEV_ADDRE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_LE_ROLE[](#_CPPv4N20bk_ble_adv_data_type22BK_BLE_AD_TYPE_LE_ROLEE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_SPAIR_C256[](#_CPPv4N20bk_ble_adv_data_type25BK_BLE_AD_TYPE_SPAIR_C256E "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_SPAIR_R256[](#_CPPv4N20bk_ble_adv_data_type25BK_BLE_AD_TYPE_SPAIR_R256E "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_32SOL_SRV_UUID[](#_CPPv4N20bk_ble_adv_data_type29BK_BLE_AD_TYPE_32SOL_SRV_UUIDE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_32SERVICE_DATA[](#_CPPv4N20bk_ble_adv_data_type29BK_BLE_AD_TYPE_32SERVICE_DATAE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_128SERVICE_DATA[](#_CPPv4N20bk_ble_adv_data_type30BK_BLE_AD_TYPE_128SERVICE_DATAE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_LE_SECURE_CONFIRM[](#_CPPv4N20bk_ble_adv_data_type32BK_BLE_AD_TYPE_LE_SECURE_CONFIRME "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_LE_SECURE_RANDOM[](#_CPPv4N20bk_ble_adv_data_type31BK_BLE_AD_TYPE_LE_SECURE_RANDOME "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_URI[](#_CPPv4N20bk_ble_adv_data_type18BK_BLE_AD_TYPE_URIE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_INDOOR_POSITION[](#_CPPv4N20bk_ble_adv_data_type30BK_BLE_AD_TYPE_INDOOR_POSITIONE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_TRANS_DISC_DATA[](#_CPPv4N20bk_ble_adv_data_type30BK_BLE_AD_TYPE_TRANS_DISC_DATAE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_LE_SUPPORT_FEATURE[](#_CPPv4N20bk_ble_adv_data_type33BK_BLE_AD_TYPE_LE_SUPPORT_FEATUREE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_CHAN_MAP_UPDATE[](#_CPPv4N20bk_ble_adv_data_type30BK_BLE_AD_TYPE_CHAN_MAP_UPDATEE "永久链接至目标")

    enumerator BK_BLE_AD_TYPE_MANU[](#_CPPv4N20bk_ble_adv_data_type19BK_BLE_AD_TYPE_MANUE "永久链接至目标")

enum bk_ble_adv_type_t[](#_CPPv417bk_ble_adv_type_t "永久链接至目标")
:   Advertising mode.


    *Values:*

    enumerator ADV_TYPE_IND[](#_CPPv4N17bk_ble_adv_type_t12ADV_TYPE_INDE "永久链接至目标")
    :   adv that can be scan and connect

    enumerator ADV_TYPE_DIRECT_IND_HIGH[](#_CPPv4N17bk_ble_adv_type_t24ADV_TYPE_DIRECT_IND_HIGHE "永久链接至目标")
    :   adv that can be connect by special device(white list). This send adv more frequently.

    enumerator ADV_TYPE_SCAN_IND[](#_CPPv4N17bk_ble_adv_type_t17ADV_TYPE_SCAN_INDE "永久链接至目标")
    :   adv that can be scan

    enumerator ADV_TYPE_NONCONN_IND[](#_CPPv4N17bk_ble_adv_type_t20ADV_TYPE_NONCONN_INDE "永久链接至目标")
    :   adv that can’t be scan and connect

    enumerator ADV_TYPE_DIRECT_IND_LOW[](#_CPPv4N17bk_ble_adv_type_t23ADV_TYPE_DIRECT_IND_LOWE "永久链接至目标")
    :   adv that can be connect by special device(white list). This send adv more few.

enum bk_ble_adv_channel_t[](#_CPPv420bk_ble_adv_channel_t "永久链接至目标")
:   Advertising channel mask.


    *Values:*

    enumerator BK_ADV_CHNL_37[](#_CPPv4N20bk_ble_adv_channel_t14BK_ADV_CHNL_37E "永久链接至目标")
    :   channel 37

    enumerator BK_ADV_CHNL_38[](#_CPPv4N20bk_ble_adv_channel_t14BK_ADV_CHNL_38E "永久链接至目标")
    :   channel 38

    enumerator BK_ADV_CHNL_39[](#_CPPv4N20bk_ble_adv_channel_t14BK_ADV_CHNL_39E "永久链接至目标")
    :   channel 39

    enumerator BK_ADV_CHNL_ALL[](#_CPPv4N20bk_ble_adv_channel_t15BK_ADV_CHNL_ALLE "永久链接至目标")
    :   channel all

enum bk_ble_adv_filter_t[](#_CPPv419bk_ble_adv_filter_t "永久链接至目标")
:   Advertising filter.


    *Values:*

    enumerator ADV_FILTER_ALLOW_SCAN_ANY_CON_ANY[](#_CPPv4N19bk_ble_adv_filter_t33ADV_FILTER_ALLOW_SCAN_ANY_CON_ANYE "永久链接至目标")
    :   Allow both scan and connection requests from anyone.

    enumerator ADV_FILTER_ALLOW_SCAN_WLST_CON_ANY[](#_CPPv4N19bk_ble_adv_filter_t34ADV_FILTER_ALLOW_SCAN_WLST_CON_ANYE "永久链接至目标")
    :   Allow both scan req from White List devices only and connection req from anyone.

    enumerator ADV_FILTER_ALLOW_SCAN_ANY_CON_WLST[](#_CPPv4N19bk_ble_adv_filter_t34ADV_FILTER_ALLOW_SCAN_ANY_CON_WLSTE "永久链接至目标")
    :   Allow both scan req from anyone and connection req from White List devices only.

    enumerator ADV_FILTER_ALLOW_SCAN_WLST_CON_WLST[](#_CPPv4N19bk_ble_adv_filter_t35ADV_FILTER_ALLOW_SCAN_WLST_CON_WLSTE "永久链接至目标")
    :   Allow scan and connection requests from White List devices only.

enum bk_ble_sec_act_t[](#_CPPv416bk_ble_sec_act_t "永久链接至目标")
:   ble encrypt method


    *Values:*

    enumerator BK_BLE_SEC_ENCRYPT[](#_CPPv4N16bk_ble_sec_act_t18BK_BLE_SEC_ENCRYPTE "永久链接至目标")
    :   If the device has already bonded, the stack will used Long Term Key (LTK) to encrypt with the remote device directly. Else if the device hasn’t bonded, the stack will used the default authentication request used the bk_ble_gap_set_security_param function set by the user.

    enumerator BK_BLE_SEC_ENCRYPT_NO_MITM[](#_CPPv4N16bk_ble_sec_act_t26BK_BLE_SEC_ENCRYPT_NO_MITME "永久链接至目标")
    :   If the device has been already bonded, the stack will check the LTK (Long Term Key) Whether the authentication request has been met, and if met, use the LTK to encrypt with the remote device directly, else re-pair with the remote device. Else if the device hasn’t been bonded, the stack will use NO MITM authentication request in the current link instead of using the authreq in the bk_ble_gap_set_security_param function set by the user.

    enumerator BK_BLE_SEC_ENCRYPT_MITM[](#_CPPv4N16bk_ble_sec_act_t23BK_BLE_SEC_ENCRYPT_MITME "永久链接至目标")
    :   If the device has been already bonded, the stack will check the LTK (Long Term Key) whether the authentication request has been met, and if met, use the LTK to encrypt with the remote device directly, else re-pair with the remote device. Else if the device hasn’t been bonded, the stack will use MITM authentication request in the current link instead of using the authreq in the bk_ble_gap_set_security_param function set by the user.

enum bk_ble_sm_param_t[](#_CPPv417bk_ble_sm_param_t "永久链接至目标")
:   ble sm option


    *Values:*

    enumerator BK_BLE_SM_AUTHEN_REQ_MODE[](#_CPPv4N17bk_ble_sm_param_t25BK_BLE_SM_AUTHEN_REQ_MODEE "永久链接至目标")
    :   Authentication requirements of local device, see bk_ble_auth_req_t.

    enumerator BK_BLE_SM_IOCAP_MODE[](#_CPPv4N17bk_ble_sm_param_t20BK_BLE_SM_IOCAP_MODEE "永久链接至目标")
    :   The IO capability of local device, see bk_io_cap_enum_t.

    enumerator BK_BLE_SM_SET_INIT_KEY[](#_CPPv4N17bk_ble_sm_param_t22BK_BLE_SM_SET_INIT_KEYE "永久链接至目标")
    :   Initiator Key Distribution/Generation, use BK_BLE_SM_SET_LOCAL_REMOTE_KEY instead !!!

    enumerator BK_BLE_SM_SET_RSP_KEY[](#_CPPv4N17bk_ble_sm_param_t21BK_BLE_SM_SET_RSP_KEYE "永久链接至目标")
    :   Responder Key Distribution/Generation, use BK_BLE_SM_SET_LOCAL_REMOTE_KEY instead !!!

    enumerator BK_BLE_SM_MAX_KEY_SIZE[](#_CPPv4N17bk_ble_sm_param_t22BK_BLE_SM_MAX_KEY_SIZEE "永久链接至目标")
    :   Maximum Encryption key size to support.

    enumerator BK_BLE_SM_MIN_KEY_SIZE[](#_CPPv4N17bk_ble_sm_param_t22BK_BLE_SM_MIN_KEY_SIZEE "永久链接至目标")
    :   Minimum Encryption key size requirement from Peer.

    enumerator BK_BLE_SM_SET_STATIC_PASSKEY[](#_CPPv4N17bk_ble_sm_param_t28BK_BLE_SM_SET_STATIC_PASSKEYE "永久链接至目标")
    :   Set static Passkey.

    enumerator BK_BLE_SM_CLEAR_STATIC_PASSKEY[](#_CPPv4N17bk_ble_sm_param_t30BK_BLE_SM_CLEAR_STATIC_PASSKEYE "永久链接至目标")
    :   Reset static Passkey.

    enumerator BK_BLE_SM_ONLY_ACCEPT_SPECIFIED_SEC_AUTH[](#_CPPv4N17bk_ble_sm_param_t40BK_BLE_SM_ONLY_ACCEPT_SPECIFIED_SEC_AUTHE "永久链接至目标")
    :   Accept only specified SMP Authentication requirement.

    enumerator BK_BLE_SM_OOB_SUPPORT[](#_CPPv4N17bk_ble_sm_param_t21BK_BLE_SM_OOB_SUPPORTE "永久链接至目标")
    :   Enable/Disable OOB support.

    enumerator BK_BLE_SM_SET_ER[](#_CPPv4N17bk_ble_sm_param_t16BK_BLE_SM_SET_ERE "永久链接至目标")
    :   set ER, 16 bytes

    enumerator BK_BLE_SM_SET_IR[](#_CPPv4N17bk_ble_sm_param_t16BK_BLE_SM_SET_IRE "永久链接至目标")
    :   set IR, 16 bytes

    enumerator BK_BLE_SM_SET_LOCAL_REMOTE_KEY[](#_CPPv4N17bk_ble_sm_param_t30BK_BLE_SM_SET_LOCAL_REMOTE_KEYE "永久链接至目标")
    :   local and remote init key, first 4 bits means local, last 4 bits means remote

enum bk_ble_key_distr_mask_t[](#_CPPv423bk_ble_key_distr_mask_t "永久链接至目标")
:   the key distribution mask type


    *Values:*

    enumerator BK_BLE_KEY_DISTR_ENC_KEY_MASK[](#_CPPv4N23bk_ble_key_distr_mask_t29BK_BLE_KEY_DISTR_ENC_KEY_MASKE "永久链接至目标")

    enumerator BK_BLE_KEY_DISTR_ID_KEY_MASK[](#_CPPv4N23bk_ble_key_distr_mask_t28BK_BLE_KEY_DISTR_ID_KEY_MASKE "永久链接至目标")
    :   Used to exchange the encryption key in the init key & response key, not used now.

    enumerator BK_BLE_KEY_DISTR_CSR_KEY_MASK[](#_CPPv4N23bk_ble_key_distr_mask_t29BK_BLE_KEY_DISTR_CSR_KEY_MASKE "永久链接至目标")
    :   Used to exchange the IRK key in the init key & response key, not used now.

    enumerator BK_BLE_KEY_DISTR_LINK_KEY_MASK[](#_CPPv4N23bk_ble_key_distr_mask_t30BK_BLE_KEY_DISTR_LINK_KEY_MASKE "永久链接至目标")
    :   Used to exchange the CSRK key in the init key & response key, not used now.

        Used to exchange the link key(this key just used in the BLE & BR/EDR coexist mode) in the init key & response key, must used with BK_LE_AUTH_REQ_SC_MITM_BOND.

enum bk_ble_scan_type_t[](#_CPPv418bk_ble_scan_type_t "永久链接至目标")
:   Ble scan type.


    *Values:*

    enumerator BLE_SCAN_TYPE_PASSIVE[](#_CPPv4N18bk_ble_scan_type_t21BLE_SCAN_TYPE_PASSIVEE "永久链接至目标")
    :   Passive scan

    enumerator BLE_SCAN_TYPE_ACTIVE[](#_CPPv4N18bk_ble_scan_type_t20BLE_SCAN_TYPE_ACTIVEE "永久链接至目标")
    :   Active scan

enum bk_ble_scan_filter_t[](#_CPPv420bk_ble_scan_filter_t "永久链接至目标")
:   Ble scan filter type.


    *Values:*

    enumerator BLE_SCAN_FILTER_ALLOW_ALL[](#_CPPv4N20bk_ble_scan_filter_t25BLE_SCAN_FILTER_ALLOW_ALLE "永久链接至目标")
    :   Accept all :

        1. advertisement packets except directed advertising packets not addressed to this device (default).

    enumerator BLE_SCAN_FILTER_ALLOW_ONLY_WLST[](#_CPPv4N20bk_ble_scan_filter_t31BLE_SCAN_FILTER_ALLOW_ONLY_WLSTE "永久链接至目标")
    :   Accept only :

        1. advertisement packets from devices where the advertiser’s address is in the White list.
        2. Directed advertising packets which are not addressed for this device shall be ignored.

    enumerator BLE_SCAN_FILTER_ALLOW_UND_RPA_DIR[](#_CPPv4N20bk_ble_scan_filter_t33BLE_SCAN_FILTER_ALLOW_UND_RPA_DIRE "永久链接至目标")
    :   Accept all :

        1. undirected advertisement packets, and
        2. directed advertising packets where the initiator address is a resolvable private address, and
        3. directed advertising packets addressed to this device.

    enumerator BLE_SCAN_FILTER_ALLOW_WLIST_RPA_DIR[](#_CPPv4N20bk_ble_scan_filter_t35BLE_SCAN_FILTER_ALLOW_WLIST_RPA_DIRE "永久链接至目标")
    :   Accept all :

        1. advertisement packets from devices where the advertiser’s address is in the White list, and
        2. directed advertising packets where the initiator address is a resolvable private address, and
        3. directed advertising packets addressed to this device.

enum bk_ble_scan_duplicate_t[](#_CPPv423bk_ble_scan_duplicate_t "永久链接至目标")
:   Ble scan duplicate type.


    *Values:*

    enumerator BLE_SCAN_DUPLICATE_DISABLE[](#_CPPv4N23bk_ble_scan_duplicate_t26BLE_SCAN_DUPLICATE_DISABLEE "永久链接至目标")
    :   the Link Layer should generate advertising reports to the host for each packet received

    enumerator BLE_SCAN_DUPLICATE_ENABLE[](#_CPPv4N23bk_ble_scan_duplicate_t25BLE_SCAN_DUPLICATE_ENABLEE "永久链接至目标")
    :   the Link Layer should filter out duplicate advertising reports to the Host

    enumerator BLE_SCAN_DUPLICATE_MAX[](#_CPPv4N23bk_ble_scan_duplicate_t22BLE_SCAN_DUPLICATE_MAXE "永久链接至目标")
    :   0x02 – 0xFF, Reserved for future use

enum bk_ble_security_level_t[](#_CPPv423bk_ble_security_level_t "永久链接至目标")
:   *Values:*

    enumerator BK_BLE_SECURITY_LEVEL_1[](#_CPPv4N23bk_ble_security_level_t23BK_BLE_SECURITY_LEVEL_1E "永久链接至目标")

    enumerator BK_BLE_SECURITY_LEVEL_2[](#_CPPv4N23bk_ble_security_level_t23BK_BLE_SECURITY_LEVEL_2E "永久链接至目标")

    enumerator BK_BLE_SECURITY_LEVEL_3[](#_CPPv4N23bk_ble_security_level_t23BK_BLE_SECURITY_LEVEL_3E "永久链接至目标")

    enumerator BK_BLE_SECURITY_LEVEL_4[](#_CPPv4N23bk_ble_security_level_t23BK_BLE_SECURITY_LEVEL_4E "永久链接至目标")

enum bk_gap_bond_dev_list_operation_t[](#_CPPv432bk_gap_bond_dev_list_operation_t "永久链接至目标")
:   bond dev list operation


    *Values:*

    enumerator BK_GAP_BOND_DEV_LIST_OPERATION_ADD[](#_CPPv4N32bk_gap_bond_dev_list_operation_t34BK_GAP_BOND_DEV_LIST_OPERATION_ADDE "永久链接至目标")

    enumerator BK_GAP_BOND_DEV_LIST_OPERATION_REMOVE[](#_CPPv4N32bk_gap_bond_dev_list_operation_t37BK_GAP_BOND_DEV_LIST_OPERATION_REMOVEE "永久链接至目标")

    enumerator BK_GAP_BOND_DEV_LIST_OPERATION_CLEAN[](#_CPPv4N32bk_gap_bond_dev_list_operation_t36BK_GAP_BOND_DEV_LIST_OPERATION_CLEANE "永久链接至目标")

enum bk_gap_search_evt_t[](#_CPPv419bk_gap_search_evt_t "永久链接至目标")
:   Sub Event of BK_BLE_GAP_SCAN_RESULT_EVT.


    *Values:*

    enumerator BK_GAP_SEARCH_INQ_RES_EVT[](#_CPPv4N19bk_gap_search_evt_t25BK_GAP_SEARCH_INQ_RES_EVTE "永久链接至目标")
    :   Inquiry result for a peer device.

    enumerator BK_GAP_SEARCH_INQ_CMPL_EVT[](#_CPPv4N19bk_gap_search_evt_t26BK_GAP_SEARCH_INQ_CMPL_EVTE "永久链接至目标")
    :   Inquiry complete.

    enumerator BK_GAP_SEARCH_DISC_RES_EVT[](#_CPPv4N19bk_gap_search_evt_t26BK_GAP_SEARCH_DISC_RES_EVTE "永久链接至目标")
    :   Discovery result for a peer device.

    enumerator BK_GAP_SEARCH_DISC_BLE_RES_EVT[](#_CPPv4N19bk_gap_search_evt_t30BK_GAP_SEARCH_DISC_BLE_RES_EVTE "永久链接至目标")
    :   Discovery result for BLE GATT based service on a peer device.

    enumerator BK_GAP_SEARCH_DISC_CMPL_EVT[](#_CPPv4N19bk_gap_search_evt_t27BK_GAP_SEARCH_DISC_CMPL_EVTE "永久链接至目标")
    :   Discovery complete.

    enumerator BK_GAP_SEARCH_DI_DISC_CMPL_EVT[](#_CPPv4N19bk_gap_search_evt_t30BK_GAP_SEARCH_DI_DISC_CMPL_EVTE "永久链接至目标")
    :   Discovery complete.

    enumerator BK_GAP_SEARCH_SEARCH_CANCEL_CMPL_EVT[](#_CPPv4N19bk_gap_search_evt_t36BK_GAP_SEARCH_SEARCH_CANCEL_CMPL_EVTE "永久链接至目标")
    :   Search cancelled

    enumerator BK_GAP_SEARCH_INQ_DISCARD_NUM_EVT[](#_CPPv4N19bk_gap_search_evt_t33BK_GAP_SEARCH_INQ_DISCARD_NUM_EVTE "永久链接至目标")
    :   The number of pkt discarded by flow control

enum bk_ble_evt_type_t[](#_CPPv417bk_ble_evt_type_t "永久链接至目标")
:   Ble scan result event type, to indicate the result is scan response or advertising data or other.


    *Values:*

    enumerator BK_BLE_EVT_CONN_ADV[](#_CPPv4N17bk_ble_evt_type_t19BK_BLE_EVT_CONN_ADVE "永久链接至目标")
    :   Connectable undirected advertising (ADV_IND)

    enumerator BK_BLE_EVT_CONN_DIR_ADV[](#_CPPv4N17bk_ble_evt_type_t23BK_BLE_EVT_CONN_DIR_ADVE "永久链接至目标")
    :   Connectable directed advertising (ADV_DIRECT_IND)

    enumerator BK_BLE_EVT_DISC_ADV[](#_CPPv4N17bk_ble_evt_type_t19BK_BLE_EVT_DISC_ADVE "永久链接至目标")
    :   Scannable undirected advertising (ADV_SCAN_IND)

    enumerator BK_BLE_EVT_NON_CONN_ADV[](#_CPPv4N17bk_ble_evt_type_t23BK_BLE_EVT_NON_CONN_ADVE "永久链接至目标")
    :   Non connectable undirected advertising (ADV_NONCONN_IND)

    enumerator BK_BLE_EVT_SCAN_RSP[](#_CPPv4N17bk_ble_evt_type_t19BK_BLE_EVT_SCAN_RSPE "永久链接至目标")
    :   Scan Response (SCAN_RSP)

enum bk_ble_wl_operation_t[](#_CPPv421bk_ble_wl_operation_t "永久链接至目标")
:   white list op


    *Values:*

    enumerator BK_BLE_WHITELIST_REMOVE[](#_CPPv4N21bk_ble_wl_operation_t23BK_BLE_WHITELIST_REMOVEE "永久链接至目标")
    :   remove mac from whitelist

    enumerator BK_BLE_WHITELIST_ADD[](#_CPPv4N21bk_ble_wl_operation_t20BK_BLE_WHITELIST_ADDE "永久链接至目标")
    :   add address to whitelist

    enumerator BK_BLE_WHITELIST_CLEAN[](#_CPPv4N21bk_ble_wl_operation_t22BK_BLE_WHITELIST_CLEANE "永久链接至目标")
    :   clean whitelist

enum bk_ble_gap_set_ext_adv_prop_t[](#_CPPv429bk_ble_gap_set_ext_adv_prop_t "永久链接至目标")
:   ext adv prop


    *Values:*

    enumerator BK_BLE_GAP_SET_EXT_ADV_PROP_NONCONN_NONSCANNABLE_UNDIRECTED[](#_CPPv4N29bk_ble_gap_set_ext_adv_prop_t59BK_BLE_GAP_SET_EXT_ADV_PROP_NONCONN_NONSCANNABLE_UNDIRECTEDE "永久链接至目标")
    :   Non-Connectable and Non-Scannable Undirected advertising

    enumerator BK_BLE_GAP_SET_EXT_ADV_PROP_CONNECTABLE[](#_CPPv4N29bk_ble_gap_set_ext_adv_prop_t39BK_BLE_GAP_SET_EXT_ADV_PROP_CONNECTABLEE "永久链接至目标")
    :   Connectable advertising

    enumerator BK_BLE_GAP_SET_EXT_ADV_PROP_SCANNABLE[](#_CPPv4N29bk_ble_gap_set_ext_adv_prop_t37BK_BLE_GAP_SET_EXT_ADV_PROP_SCANNABLEE "永久链接至目标")
    :   Scannable advertising

    enumerator BK_BLE_GAP_SET_EXT_ADV_PROP_DIRECTED[](#_CPPv4N29bk_ble_gap_set_ext_adv_prop_t36BK_BLE_GAP_SET_EXT_ADV_PROP_DIRECTEDE "永久链接至目标")
    :   Directed advertising

    enumerator BK_BLE_GAP_SET_EXT_ADV_PROP_HD_DIRECTED[](#_CPPv4N29bk_ble_gap_set_ext_adv_prop_t39BK_BLE_GAP_SET_EXT_ADV_PROP_HD_DIRECTEDE "永久链接至目标")
    :   High Duty Cycle Directed Connectable advertising (<= 3.75 ms Advertising Interval)

    enumerator BK_BLE_GAP_SET_EXT_ADV_PROP_LEGACY[](#_CPPv4N29bk_ble_gap_set_ext_adv_prop_t34BK_BLE_GAP_SET_EXT_ADV_PROP_LEGACYE "永久链接至目标")
    :   Use legacy advertising PDUs

    enumerator BK_BLE_GAP_SET_EXT_ADV_PROP_ANON_ADV[](#_CPPv4N29bk_ble_gap_set_ext_adv_prop_t36BK_BLE_GAP_SET_EXT_ADV_PROP_ANON_ADVE "永久链接至目标")
    :   Omit advertiser’s address from all PDUs (“anonymous advertising”)

    enumerator BK_BLE_GAP_SET_EXT_ADV_PROP_INCLUDE_TX_PWR[](#_CPPv4N29bk_ble_gap_set_ext_adv_prop_t42BK_BLE_GAP_SET_EXT_ADV_PROP_INCLUDE_TX_PWRE "永久链接至目标")
    :   Include TxPower in the extended header of the advertising PDU

    enumerator BK_BLE_GAP_SET_EXT_ADV_PROP_MASK[](#_CPPv4N29bk_ble_gap_set_ext_adv_prop_t32BK_BLE_GAP_SET_EXT_ADV_PROP_MASKE "永久链接至目标")
    :   Reserved for future use

enum bk_ble_gap_phy_enum_t[](#_CPPv421bk_ble_gap_phy_enum_t "永久链接至目标")
:   *Values:*

    enumerator BK_BLE_GAP_PHY_1M[](#_CPPv4N21bk_ble_gap_phy_enum_t17BK_BLE_GAP_PHY_1ME "永久链接至目标")
    :   Secondery Advertisement PHY is LE1M

    enumerator BK_BLE_GAP_PHY_2M[](#_CPPv4N21bk_ble_gap_phy_enum_t17BK_BLE_GAP_PHY_2ME "永久链接至目标")
    :   Secondery Advertisement PHY is LE2M

    enumerator BK_BLE_GAP_PHY_CODED[](#_CPPv4N21bk_ble_gap_phy_enum_t20BK_BLE_GAP_PHY_CODEDE "永久链接至目标")
    :   Secondery Advertisement PHY is LE Coded

enum bk_ble_gap_noprefer_enum_t[](#_CPPv426bk_ble_gap_noprefer_enum_t "永久链接至目标")
:   ble gap noprefer phy


    *Values:*

    enumerator BK_BLE_GAP_NO_PREFER_TRANSMIT_PHY[](#_CPPv4N26bk_ble_gap_noprefer_enum_t33BK_BLE_GAP_NO_PREFER_TRANSMIT_PHYE "永久链接至目标")
    :   No Prefer TX PHY supported by controller

    enumerator BK_BLE_GAP_NO_PREFER_RECEIVE_PHY[](#_CPPv4N26bk_ble_gap_noprefer_enum_t32BK_BLE_GAP_NO_PREFER_RECEIVE_PHYE "永久链接至目标")
    :   No Prefer RX PHY supported by controller

enum bk_ble_gap_pri_phy_enum_t[](#_CPPv425bk_ble_gap_pri_phy_enum_t "永久链接至目标")
:   Primary phy only support 1M and LE coded phy.


    *Values:*

    enumerator BK_BLE_GAP_PRI_PHY_1M[](#_CPPv4N25bk_ble_gap_pri_phy_enum_t21BK_BLE_GAP_PRI_PHY_1ME "永久链接至目标")
    :   Primary Phy is LE1M

    enumerator BK_BLE_GAP_PRI_PHY_CODED[](#_CPPv4N25bk_ble_gap_pri_phy_enum_t24BK_BLE_GAP_PRI_PHY_CODEDE "永久链接至目标")
    :   Primary Phy is LE CODED

enum bk_ble_gap_phy_pref_enum_t[](#_CPPv426bk_ble_gap_phy_pref_enum_t "永久链接至目标")
:   *Values:*

    enumerator BK_BLE_GAP_PHY_1M_PREF_MASK[](#_CPPv4N26bk_ble_gap_phy_pref_enum_t27BK_BLE_GAP_PHY_1M_PREF_MASKE "永久链接至目标")
    :   The Host prefers use the LE1M transmitter or reciever PHY

    enumerator BK_BLE_GAP_PHY_2M_PREF_MASK[](#_CPPv4N26bk_ble_gap_phy_pref_enum_t27BK_BLE_GAP_PHY_2M_PREF_MASKE "永久链接至目标")
    :   The Host prefers use the LE2M transmitter or reciever PHY

    enumerator BK_BLE_GAP_PHY_CODED_PREF_MASK[](#_CPPv4N26bk_ble_gap_phy_pref_enum_t30BK_BLE_GAP_PHY_CODED_PREF_MASKE "永久链接至目标")
    :   The Host prefers use the LE CODED transmitter or reciever PHY

enum bk_ble_gap_coded_phy_pref_enum_t[](#_CPPv432bk_ble_gap_coded_phy_pref_enum_t "永久链接至目标")
:   ble gap coded phy pref param


    *Values:*

    enumerator BK_BLE_GAP_PHY_OPTIONS_NO_PREF[](#_CPPv4N32bk_ble_gap_coded_phy_pref_enum_t30BK_BLE_GAP_PHY_OPTIONS_NO_PREFE "永久链接至目标")
    :   The Host has no preferred coding when transmitting on the LE Coded PHY

    enumerator BK_BLE_GAP_PHY_OPTIONS_PREF_S2_CODING[](#_CPPv4N32bk_ble_gap_coded_phy_pref_enum_t37BK_BLE_GAP_PHY_OPTIONS_PREF_S2_CODINGE "永久链接至目标")
    :   The Host prefers that S=2 coding be used when transmitting on the LE Coded PHY

    enumerator BK_BLE_GAP_PHY_OPTIONS_PREF_S8_CODING[](#_CPPv4N32bk_ble_gap_coded_phy_pref_enum_t37BK_BLE_GAP_PHY_OPTIONS_PREF_S8_CODINGE "永久链接至目标")
    :   The Host prefers that S=8 coding be used when transmitting on the LE Coded PHY

enum bk_ble_gap_ext_scan_cfg_enum_t[](#_CPPv430bk_ble_gap_ext_scan_cfg_enum_t "永久链接至目标")
:   ble gap ext scan cfg


    *Values:*

    enumerator BK_BLE_GAP_EXT_SCAN_CFG_UNCODE_MASK[](#_CPPv4N30bk_ble_gap_ext_scan_cfg_enum_t35BK_BLE_GAP_EXT_SCAN_CFG_UNCODE_MASKE "永久链接至目标")
    :   Scan Advertisements on the LE1M PHY

    enumerator BK_BLE_GAP_EXT_SCAN_CFG_CODE_MASK[](#_CPPv4N30bk_ble_gap_ext_scan_cfg_enum_t33BK_BLE_GAP_EXT_SCAN_CFG_CODE_MASKE "永久链接至目标")
    :   Scan advertisements on the LE coded PHY

enum bk_ble_gap_ext_adv_data_seg_enum_t[](#_CPPv434bk_ble_gap_ext_adv_data_seg_enum_t "永久链接至目标")
:   Advertising data seg.


    *Values:*

    enumerator BK_BLE_GAP_EXT_ADV_DATA_COMPLETE[](#_CPPv4N34bk_ble_gap_ext_adv_data_seg_enum_t32BK_BLE_GAP_EXT_ADV_DATA_COMPLETEE "永久链接至目标")
    :   extended advertising data compete

    enumerator BK_BLE_GAP_EXT_ADV_DATA_INCOMPLETE[](#_CPPv4N34bk_ble_gap_ext_adv_data_seg_enum_t34BK_BLE_GAP_EXT_ADV_DATA_INCOMPLETEE "永久链接至目标")
    :   extended advertising data incomplete

    enumerator BK_BLE_GAP_EXT_ADV_DATA_TRUNCATED[](#_CPPv4N34bk_ble_gap_ext_adv_data_seg_enum_t33BK_BLE_GAP_EXT_ADV_DATA_TRUNCATEDE "永久链接至目标")
    :   extended advertising data truncated mode

enum bk_ble_gap_sync_policy_enum_t[](#_CPPv429bk_ble_gap_sync_policy_enum_t "永久链接至目标")
:   Advertising SYNC policy.


    *Values:*

    enumerator BK_BLE_GAP_SYNC_POLICY_BY_ADV_INFO[](#_CPPv4N29bk_ble_gap_sync_policy_enum_t34BK_BLE_GAP_SYNC_POLICY_BY_ADV_INFOE "永久链接至目标")
    :   sync policy by advertising info

    enumerator BK_BLE_GAP_SYNC_POLICY_BY_PERIODIC_LIST[](#_CPPv4N29bk_ble_gap_sync_policy_enum_t39BK_BLE_GAP_SYNC_POLICY_BY_PERIODIC_LISTE "永久链接至目标")
    :   periodic advertising sync policy

enum bk_ble_adv_report_ext_type_enum_t[](#_CPPv433bk_ble_adv_report_ext_type_enum_t "永久链接至目标")
:   Advertising report.


    *Values:*

    enumerator BK_BLE_ADV_REPORT_EXT_ADV_IND[](#_CPPv4N33bk_ble_adv_report_ext_type_enum_t29BK_BLE_ADV_REPORT_EXT_ADV_INDE "永久链接至目标")
    :   advertising report with extended advertising indication type

    enumerator BK_BLE_ADV_REPORT_EXT_SCAN_IND[](#_CPPv4N33bk_ble_adv_report_ext_type_enum_t30BK_BLE_ADV_REPORT_EXT_SCAN_INDE "永久链接至目标")
    :   advertising report with extended scan indication type

    enumerator BK_BLE_ADV_REPORT_EXT_DIRECT_ADV[](#_CPPv4N33bk_ble_adv_report_ext_type_enum_t32BK_BLE_ADV_REPORT_EXT_DIRECT_ADVE "永久链接至目标")
    :   advertising report with extended direct advertising indication type

    enumerator BK_BLE_ADV_REPORT_EXT_SCAN_RSP[](#_CPPv4N33bk_ble_adv_report_ext_type_enum_t30BK_BLE_ADV_REPORT_EXT_SCAN_RSPE "永久链接至目标")
    :   advertising report with extended scan response indication type

    enumerator BK_BLE_LEGACY_ADV_TYPE_IND[](#_CPPv4N33bk_ble_adv_report_ext_type_enum_t26BK_BLE_LEGACY_ADV_TYPE_INDE "永久链接至目标")
    :   advertising report with legacy advertising indication type

    enumerator BK_BLE_LEGACY_ADV_TYPE_DIRECT_IND[](#_CPPv4N33bk_ble_adv_report_ext_type_enum_t33BK_BLE_LEGACY_ADV_TYPE_DIRECT_INDE "永久链接至目标")
    :   advertising report with legacy direct indication type

    enumerator BK_BLE_LEGACY_ADV_TYPE_SCAN_IND[](#_CPPv4N33bk_ble_adv_report_ext_type_enum_t31BK_BLE_LEGACY_ADV_TYPE_SCAN_INDE "永久链接至目标")
    :   advertising report with legacy scan indication type

    enumerator BK_BLE_LEGACY_ADV_TYPE_NONCON_IND[](#_CPPv4N33bk_ble_adv_report_ext_type_enum_t33BK_BLE_LEGACY_ADV_TYPE_NONCON_INDE "永久链接至目标")
    :   advertising report with legacy non connectable indication type

    enumerator BK_BLE_LEGACY_ADV_TYPE_SCAN_RSP_TO_ADV_IND[](#_CPPv4N33bk_ble_adv_report_ext_type_enum_t42BK_BLE_LEGACY_ADV_TYPE_SCAN_RSP_TO_ADV_INDE "永久链接至目标")
    :   advertising report with legacy scan response indication type

    enumerator BK_BLE_LEGACY_ADV_TYPE_SCAN_RSP_TO_ADV_SCAN_IND[](#_CPPv4N33bk_ble_adv_report_ext_type_enum_t47BK_BLE_LEGACY_ADV_TYPE_SCAN_RSP_TO_ADV_SCAN_INDE "永久链接至目标")
    :   advertising report with legacy advertising with scan response indication type


### Header File[](#id15 "永久链接至标题")


- [bluetooth/bk_dm_gatt_types.h](https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_gatt_types.h "https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_gatt_types.h")


### Structures[](#id16 "永久链接至标题")

struct bk_gatt_id_t[](#_CPPv412bk_gatt_id_t "永久链接至目标")
:   Gatt id, include uuid and instance id.

    Public Members

    [bk_bt_uuid_t](#_CPPv412bk_bt_uuid_t "bk_bt_uuid_t") uuid[](#_CPPv4N12bk_gatt_id_t4uuidE "永久链接至目标")
    :   UUID

struct bk_gatt_srvc_id_t[](#_CPPv417bk_gatt_srvc_id_t "永久链接至目标")
:   Gatt service id, include id (uuid and instance id) and primary flag.

    Public Members

    [bk_gatt_id_t](#_CPPv412bk_gatt_id_t "bk_gatt_id_t") id[](#_CPPv4N17bk_gatt_srvc_id_t2idE "永久链接至目标")
    :   Gatt id, include uuid and instance

    bool is_primary[](#_CPPv4N17bk_gatt_srvc_id_t10is_primaryE "永久链接至目标")
    :   This service is primary or not

struct bk_attr_value_t[](#_CPPv415bk_attr_value_t "永久链接至目标")
:   set the attribute value type

    Public Members

    uint16_t attr_max_len[](#_CPPv4N15bk_attr_value_t12attr_max_lenE "永久链接至目标")
    :   attribute max value length

    uint16_t attr_len[](#_CPPv4N15bk_attr_value_t8attr_lenE "永久链接至目标")
    :   attribute current value length

    uint8_t *attr_value[](#_CPPv4N15bk_attr_value_t10attr_valueE "永久链接至目标")
    :   the pointer to attribute value

struct bk_attr_desc_t[](#_CPPv414bk_attr_desc_t "永久链接至目标")
:   Attribute description (used to create database)

    Public Members

    [bk_bt_uuid_t](#_CPPv412bk_bt_uuid_t "bk_bt_uuid_t") attr_content[](#_CPPv4N14bk_attr_desc_t12attr_contentE "永久链接至目标")
    :   attr type

    [bk_attr_value_t](#_CPPv415bk_attr_value_t "bk_attr_value_t") value[](#_CPPv4N14bk_attr_desc_t5valueE "永久链接至目标")
    :   attr content if attr_type is service or char

    [bk_gatt_char_prop_t](#_CPPv419bk_gatt_char_prop_t "bk_gatt_char_prop_t") prop[](#_CPPv4N14bk_attr_desc_t4propE "永久链接至目标")
    :   Element value if attr_type is char or desc.

    [bk_gatt_perm_enum_t](#_CPPv419bk_gatt_perm_enum_t "bk_gatt_perm_enum_t") perm[](#_CPPv4N14bk_attr_desc_t4permE "永久链接至目标")
    :   char prop, only used if attr_type is char

        Attribute permission

struct bk_attr_control_t[](#_CPPv417bk_attr_control_t "永久链接至目标")
:   attribute auto response flag

    Public Members

    uint8_t auto_rsp[](#_CPPv4N17bk_attr_control_t8auto_rspE "永久链接至目标")
    :   if auto_rsp set to BK_GATT_RSP_BY_APP, means the response of Write/Read operation will by replied by application. if auto_rsp set to BK_GATT_AUTO_RSP, means the response of Write/Read operation will be replied by GATT stack automatically.

struct bk_gatts_attr_db_t[](#_CPPv418bk_gatts_attr_db_t "永久链接至目标")
:   attribute type added to the gatt server database

    Public Members

    [bk_attr_desc_t](#_CPPv414bk_attr_desc_t "bk_attr_desc_t") att_desc[](#_CPPv4N18bk_gatts_attr_db_t8att_descE "永久链接至目标")
    :   The attribute type

    [bk_attr_control_t](#_CPPv417bk_attr_control_t "bk_attr_control_t") attr_control[](#_CPPv4N18bk_gatts_attr_db_t12attr_controlE "永久链接至目标")
    :   The attribute control type, not used if attr type is service

struct bk_gatt_value_t[](#_CPPv415bk_gatt_value_t "永久链接至目标")
:   Gatt attribute value.

    Public Members

    uint8_t *value[](#_CPPv4N15bk_gatt_value_t5valueE "永久链接至目标")
    :   Gatt attribute value

    uint16_t handle[](#_CPPv4N15bk_gatt_value_t6handleE "永久链接至目标")
    :   Gatt attribute handle

    uint16_t offset[](#_CPPv4N15bk_gatt_value_t6offsetE "永久链接至目标")
    :   Gatt attribute value offset

    uint16_t len[](#_CPPv4N15bk_gatt_value_t3lenE "永久链接至目标")
    :   Gatt attribute value length

    [bk_gatt_auth_req_t](#_CPPv418bk_gatt_auth_req_t "bk_gatt_auth_req_t") auth_req[](#_CPPv4N15bk_gatt_value_t8auth_reqE "永久链接至目标")
    :   Gatt authentication request see bk_gatt_auth_req_t

struct bk_gatt_rsp_t[](#_CPPv413bk_gatt_rsp_t "永久链接至目标")
:   GATT remote read request response type.

    Public Members

    [bk_gatt_value_t](#_CPPv415bk_gatt_value_t "bk_gatt_value_t") attr_value[](#_CPPv4N13bk_gatt_rsp_t10attr_valueE "永久链接至目标")
    :   Gatt attribute structure

struct bk_gatt_conn_params_t[](#_CPPv421bk_gatt_conn_params_t "永久链接至目标")
:   Connection parameters information.

    Public Members

    uint16_t interval[](#_CPPv4N21bk_gatt_conn_params_t8intervalE "永久链接至目标")
    :   connection interval

    uint16_t latency[](#_CPPv4N21bk_gatt_conn_params_t7latencyE "永久链接至目标")
    :   Slave latency for the connection in number of connection events. Range: 0x0000 to 0x01F3

    uint16_t timeout[](#_CPPv4N21bk_gatt_conn_params_t7timeoutE "永久链接至目标")
    :   Supervision timeout for the LE Link. Range: 0x000A to 0x0C80. Mandatory Range: 0x000A to 0x0C80 Time = N * 10 msec Time Range: 100 msec to 32 seconds

struct bk_gattc_multi_t[](#_CPPv416bk_gattc_multi_t "永久链接至目标")
:   read multiple attribute

    Public Members

    uint8_t num_attr[](#_CPPv4N16bk_gattc_multi_t8num_attrE "永久链接至目标")
    :   The number of the attribute

    uint16_t handles[BK_GATT_MAX_READ_MULTI_HANDLES][](#_CPPv4N16bk_gattc_multi_t7handlesE "永久链接至目标")
    :   The handles list


### Macros[](#id17 "永久链接至标题")

BK_GATT_MAX_READ_MULTI_HANDLES[](#c.BK_GATT_MAX_READ_MULTI_HANDLES "永久链接至目标")

BK_GATT_RSP_BY_APP[](#c.BK_GATT_RSP_BY_APP "永久链接至目标")

BK_GATT_AUTO_RSP[](#c.BK_GATT_AUTO_RSP "永久链接至目标")


### Type Definitions[](#id18 "永久链接至标题")

typedef uint16_t bk_gatt_perm_t[](#_CPPv414bk_gatt_perm_t "永久链接至目标")
:   see bk_gatt_perm_enum_t

typedef uint8_t bk_gatt_char_prop_t[](#_CPPv419bk_gatt_char_prop_t "永久链接至目标")
:   see bk_gatt_char_prop_enum_t

typedef uint8_t bk_gatt_if_t[](#_CPPv412bk_gatt_if_t "永久链接至目标")
:   Gatt interface type, different application on GATT client use different gatt_if


### Enumerations[](#id19 "永久链接至标题")

enum bk_gatt_uuid_enum_t[](#_CPPv419bk_gatt_uuid_enum_t "永久链接至目标")
:   gatt uuid type, All “BK_GATT_UUID_xxx” is attribute types


    *Values:*

    enumerator BK_GATT_UUID_GAP_SVC[](#_CPPv4N19bk_gatt_uuid_enum_t20BK_GATT_UUID_GAP_SVCE "永久链接至目标")

    enumerator BK_GATT_UUID_GATT_SVC[](#_CPPv4N19bk_gatt_uuid_enum_t21BK_GATT_UUID_GATT_SVCE "永久链接至目标")
    :   Generic Access Profile service.

    enumerator BK_GATT_UUID_IMMEDIATE_ALERT_SVC[](#_CPPv4N19bk_gatt_uuid_enum_t32BK_GATT_UUID_IMMEDIATE_ALERT_SVCE "永久链接至目标")
    :   Generic Attribute Profile service.

    enumerator BK_GATT_UUID_LINK_LOSS_SVC[](#_CPPv4N19bk_gatt_uuid_enum_t26BK_GATT_UUID_LINK_LOSS_SVCE "永久链接至目标")
    :   Immediate alert service.

    enumerator BK_GATT_UUID_TX_POWER_SVC[](#_CPPv4N19bk_gatt_uuid_enum_t25BK_GATT_UUID_TX_POWER_SVCE "永久链接至目标")
    :   Link Loss service.

    enumerator BK_GATT_UUID_CURRENT_TIME_SVC[](#_CPPv4N19bk_gatt_uuid_enum_t29BK_GATT_UUID_CURRENT_TIME_SVCE "永久链接至目标")
    :   TX Power service.

    enumerator BK_GATT_UUID_REF_TIME_UPDATE_SVC[](#_CPPv4N19bk_gatt_uuid_enum_t32BK_GATT_UUID_REF_TIME_UPDATE_SVCE "永久链接至目标")
    :   Current Time Service service.

    enumerator BK_GATT_UUID_NEXT_DST_CHANGE_SVC[](#_CPPv4N19bk_gatt_uuid_enum_t32BK_GATT_UUID_NEXT_DST_CHANGE_SVCE "永久链接至目标")
    :   Reference Time Update service.

    enumerator BK_GATT_UUID_GLUCOSE_SVC[](#_CPPv4N19bk_gatt_uuid_enum_t24BK_GATT_UUID_GLUCOSE_SVCE "永久链接至目标")
    :   Next DST Change service.

    enumerator BK_GATT_UUID_HEALTH_THERMOM_SVC[](#_CPPv4N19bk_gatt_uuid_enum_t31BK_GATT_UUID_HEALTH_THERMOM_SVCE "永久链接至目标")
    :   Glucose service.

    enumerator BK_GATT_UUID_DEVICE_INFO_SVC[](#_CPPv4N19bk_gatt_uuid_enum_t28BK_GATT_UUID_DEVICE_INFO_SVCE "永久链接至目标")
    :   Health Thermometer service.

    enumerator BK_GATT_UUID_HEART_RATE_SVC[](#_CPPv4N19bk_gatt_uuid_enum_t27BK_GATT_UUID_HEART_RATE_SVCE "永久链接至目标")
    :   Device Information service.

    enumerator BK_GATT_UUID_PHONE_ALERT_STATUS_SVC[](#_CPPv4N19bk_gatt_uuid_enum_t35BK_GATT_UUID_PHONE_ALERT_STATUS_SVCE "永久链接至目标")
    :   Heart Rate service.

    enumerator BK_GATT_UUID_BATTERY_SERVICE_SVC[](#_CPPv4N19bk_gatt_uuid_enum_t32BK_GATT_UUID_BATTERY_SERVICE_SVCE "永久链接至目标")
    :   Phone Alert Status service.

    enumerator BK_GATT_UUID_BLOOD_PRESSURE_SVC[](#_CPPv4N19bk_gatt_uuid_enum_t31BK_GATT_UUID_BLOOD_PRESSURE_SVCE "永久链接至目标")
    :   Battery service.

    enumerator BK_GATT_UUID_ALERT_NTF_SVC[](#_CPPv4N19bk_gatt_uuid_enum_t26BK_GATT_UUID_ALERT_NTF_SVCE "永久链接至目标")
    :   Blood Pressure service.

    enumerator BK_GATT_UUID_HID_SVC[](#_CPPv4N19bk_gatt_uuid_enum_t20BK_GATT_UUID_HID_SVCE "永久链接至目标")
    :   Alert Notification service.

    enumerator BK_GATT_UUID_SCAN_PARAMETERS_SVC[](#_CPPv4N19bk_gatt_uuid_enum_t32BK_GATT_UUID_SCAN_PARAMETERS_SVCE "永久链接至目标")
    :   HID service.

    enumerator BK_GATT_UUID_RUNNING_SPEED_CADENCE_SVC[](#_CPPv4N19bk_gatt_uuid_enum_t38BK_GATT_UUID_RUNNING_SPEED_CADENCE_SVCE "永久链接至目标")
    :   Scan Parameters service.

    enumerator BK_GATT_UUID_Automation_IO_SVC[](#_CPPv4N19bk_gatt_uuid_enum_t30BK_GATT_UUID_Automation_IO_SVCE "永久链接至目标")
    :   Running Speed and Cadence service.

    enumerator BK_GATT_UUID_CYCLING_SPEED_CADENCE_SVC[](#_CPPv4N19bk_gatt_uuid_enum_t38BK_GATT_UUID_CYCLING_SPEED_CADENCE_SVCE "永久链接至目标")
    :   Automation IO service.

    enumerator BK_GATT_UUID_CYCLING_POWER_SVC[](#_CPPv4N19bk_gatt_uuid_enum_t30BK_GATT_UUID_CYCLING_POWER_SVCE "永久链接至目标")
    :   Cycling Speed and Cadence service.

    enumerator BK_GATT_UUID_LOCATION_AND_NAVIGATION_SVC[](#_CPPv4N19bk_gatt_uuid_enum_t40BK_GATT_UUID_LOCATION_AND_NAVIGATION_SVCE "永久链接至目标")
    :   Cycling Power service.

    enumerator BK_GATT_UUID_ENVIRONMENTAL_SENSING_SVC[](#_CPPv4N19bk_gatt_uuid_enum_t38BK_GATT_UUID_ENVIRONMENTAL_SENSING_SVCE "永久链接至目标")
    :   Location and Navigation service.

    enumerator BK_GATT_UUID_BODY_COMPOSITION[](#_CPPv4N19bk_gatt_uuid_enum_t29BK_GATT_UUID_BODY_COMPOSITIONE "永久链接至目标")
    :   Environmental Sensing service.

    enumerator BK_GATT_UUID_USER_DATA_SVC[](#_CPPv4N19bk_gatt_uuid_enum_t26BK_GATT_UUID_USER_DATA_SVCE "永久链接至目标")
    :   Body Composition service.

    enumerator BK_GATT_UUID_WEIGHT_SCALE_SVC[](#_CPPv4N19bk_gatt_uuid_enum_t29BK_GATT_UUID_WEIGHT_SCALE_SVCE "永久链接至目标")
    :   User Data service.

    enumerator BK_GATT_UUID_BOND_MANAGEMENT_SVC[](#_CPPv4N19bk_gatt_uuid_enum_t32BK_GATT_UUID_BOND_MANAGEMENT_SVCE "永久链接至目标")
    :   Weight Scale service.

    enumerator BK_GATT_UUID_CONT_GLUCOSE_MONITOR_SVC[](#_CPPv4N19bk_gatt_uuid_enum_t37BK_GATT_UUID_CONT_GLUCOSE_MONITOR_SVCE "永久链接至目标")
    :   Bond Management service.

    enumerator BK_GATT_UUID_PRI_SERVICE[](#_CPPv4N19bk_gatt_uuid_enum_t24BK_GATT_UUID_PRI_SERVICEE "永久链接至目标")
    :   Continuous Glucose Monitoring service.

        Declarations

    enumerator BK_GATT_UUID_SEC_SERVICE[](#_CPPv4N19bk_gatt_uuid_enum_t24BK_GATT_UUID_SEC_SERVICEE "永久链接至目标")

    enumerator BK_GATT_UUID_INCLUDE_SERVICE[](#_CPPv4N19bk_gatt_uuid_enum_t28BK_GATT_UUID_INCLUDE_SERVICEE "永久链接至目标")

    enumerator BK_GATT_UUID_CHAR_DECLARE[](#_CPPv4N19bk_gatt_uuid_enum_t25BK_GATT_UUID_CHAR_DECLAREE "永久链接至目标")

    enumerator BK_GATT_UUID_CHAR_EXT_PROP[](#_CPPv4N19bk_gatt_uuid_enum_t26BK_GATT_UUID_CHAR_EXT_PROPE "永久链接至目标")
    :   Characteristic Declaration.

        Descriptors

    enumerator BK_GATT_UUID_CHAR_USER_DESCRIPTION[](#_CPPv4N19bk_gatt_uuid_enum_t34BK_GATT_UUID_CHAR_USER_DESCRIPTIONE "永久链接至目标")
    :   Characteristic Extended Properties.

    enumerator BK_GATT_UUID_CHAR_CLIENT_CONFIG[](#_CPPv4N19bk_gatt_uuid_enum_t31BK_GATT_UUID_CHAR_CLIENT_CONFIGE "永久链接至目标")
    :   Characteristic User Description.

    enumerator BK_GATT_UUID_CHAR_SRVR_CONFIG[](#_CPPv4N19bk_gatt_uuid_enum_t29BK_GATT_UUID_CHAR_SRVR_CONFIGE "永久链接至目标")
    :   Client Characteristic Configuration.

    enumerator BK_GATT_UUID_CHAR_PRESENT_FORMAT[](#_CPPv4N19bk_gatt_uuid_enum_t32BK_GATT_UUID_CHAR_PRESENT_FORMATE "永久链接至目标")
    :   Server Characteristic Configuration.

    enumerator BK_GATT_UUID_CHAR_AGG_FORMAT[](#_CPPv4N19bk_gatt_uuid_enum_t28BK_GATT_UUID_CHAR_AGG_FORMATE "永久链接至目标")
    :   Characteristic Presentation Format.

    enumerator BK_GATT_UUID_CHAR_VALID_RANGE[](#_CPPv4N19bk_gatt_uuid_enum_t29BK_GATT_UUID_CHAR_VALID_RANGEE "永久链接至目标")
    :   Characteristic Aggregate Format.

    enumerator BK_GATT_UUID_EXT_RPT_REF_DESCR[](#_CPPv4N19bk_gatt_uuid_enum_t30BK_GATT_UUID_EXT_RPT_REF_DESCRE "永久链接至目标")
    :   Characteristic Valid Range.

    enumerator BK_GATT_UUID_RPT_REF_DESCR[](#_CPPv4N19bk_gatt_uuid_enum_t26BK_GATT_UUID_RPT_REF_DESCRE "永久链接至目标")
    :   External Report Reference.

    enumerator BK_GATT_UUID_NUM_DIGITALS_DESCR[](#_CPPv4N19bk_gatt_uuid_enum_t31BK_GATT_UUID_NUM_DIGITALS_DESCRE "永久链接至目标")
    :   Report Reference.

    enumerator BK_GATT_UUID_VALUE_TRIGGER_DESCR[](#_CPPv4N19bk_gatt_uuid_enum_t32BK_GATT_UUID_VALUE_TRIGGER_DESCRE "永久链接至目标")
    :   Number of Digitals.

    enumerator BK_GATT_UUID_ENV_SENSING_CONFIG_DESCR[](#_CPPv4N19bk_gatt_uuid_enum_t37BK_GATT_UUID_ENV_SENSING_CONFIG_DESCRE "永久链接至目标")
    :   Value Trigger Setting.

    enumerator BK_GATT_UUID_ENV_SENSING_MEASUREMENT_DESCR[](#_CPPv4N19bk_gatt_uuid_enum_t42BK_GATT_UUID_ENV_SENSING_MEASUREMENT_DESCRE "永久链接至目标")
    :   Environmental Sensing Configuration.

    enumerator BK_GATT_UUID_ENV_SENSING_TRIGGER_DESCR[](#_CPPv4N19bk_gatt_uuid_enum_t38BK_GATT_UUID_ENV_SENSING_TRIGGER_DESCRE "永久链接至目标")
    :   Environmental Sensing Measurement.

    enumerator BK_GATT_UUID_TIME_TRIGGER_DESCR[](#_CPPv4N19bk_gatt_uuid_enum_t31BK_GATT_UUID_TIME_TRIGGER_DESCRE "永久链接至目标")
    :   Environmental Sensing Trigger Setting.

    enumerator BK_GATT_UUID_BR_EDR_TRANS_BLOCK_DATA[](#_CPPv4N19bk_gatt_uuid_enum_t36BK_GATT_UUID_BR_EDR_TRANS_BLOCK_DATAE "永久链接至目标")
    :   Time Trigger Setting.

    enumerator BK_GATT_UUID_OBSERVATION_SCHEDULE[](#_CPPv4N19bk_gatt_uuid_enum_t33BK_GATT_UUID_OBSERVATION_SCHEDULEE "永久链接至目标")
    :   Complete BRT-EDR Transport BLock Data.

    enumerator BK_GATT_UUID_VALID_RANGE_ACCURACY[](#_CPPv4N19bk_gatt_uuid_enum_t33BK_GATT_UUID_VALID_RANGE_ACCURACYE "永久链接至目标")
    :   Observation Schedule.

    enumerator BK_GATT_UUID_MEASUREMENT_DESCRIPTION[](#_CPPv4N19bk_gatt_uuid_enum_t36BK_GATT_UUID_MEASUREMENT_DESCRIPTIONE "永久链接至目标")
    :   Valid Range and Accuracy.

    enumerator BK_GATT_UUID_MANUFACTURER_LIMITS[](#_CPPv4N19bk_gatt_uuid_enum_t32BK_GATT_UUID_MANUFACTURER_LIMITSE "永久链接至目标")

    enumerator BK_GATT_UUID_PROCESS_TOLERANCES[](#_CPPv4N19bk_gatt_uuid_enum_t31BK_GATT_UUID_PROCESS_TOLERANCESE "永久链接至目标")

    enumerator BK_GATT_UUID_IMD_TRIGGER_SETTING[](#_CPPv4N19bk_gatt_uuid_enum_t32BK_GATT_UUID_IMD_TRIGGER_SETTINGE "永久链接至目标")

    enumerator BK_GATT_UUID_GAP_DEVICE_NAME[](#_CPPv4N19bk_gatt_uuid_enum_t28BK_GATT_UUID_GAP_DEVICE_NAMEE "永久链接至目标")
    :   GAP Profile Attributes.

    enumerator BK_GATT_UUID_GAP_APPEARANCE[](#_CPPv4N19bk_gatt_uuid_enum_t27BK_GATT_UUID_GAP_APPEARANCEE "永久链接至目标")

    enumerator BK_GATT_UUID_GAP_PREF_CONN_PARAM[](#_CPPv4N19bk_gatt_uuid_enum_t32BK_GATT_UUID_GAP_PREF_CONN_PARAME "永久链接至目标")

    enumerator BK_GATT_UUID_GAP_CENTRAL_ADDR_RESOL[](#_CPPv4N19bk_gatt_uuid_enum_t35BK_GATT_UUID_GAP_CENTRAL_ADDR_RESOLE "永久链接至目标")

    enumerator BK_GATT_UUID_GAP_RESOLV_RPVIATE_ADDR_ONLY[](#_CPPv4N19bk_gatt_uuid_enum_t41BK_GATT_UUID_GAP_RESOLV_RPVIATE_ADDR_ONLYE "永久链接至目标")

    enumerator BK_GATT_UUID_GAP_ENCRYPT_DATA_KEY_MATERIAL[](#_CPPv4N19bk_gatt_uuid_enum_t42BK_GATT_UUID_GAP_ENCRYPT_DATA_KEY_MATERIALE "永久链接至目标")

    enumerator BK_GATT_UUID_GAP_BLE_GATT_SECURITY_LVL[](#_CPPv4N19bk_gatt_uuid_enum_t38BK_GATT_UUID_GAP_BLE_GATT_SECURITY_LVLE "永久链接至目标")

    enumerator BK_GATT_UUID_GATT_SRV_CHGD[](#_CPPv4N19bk_gatt_uuid_enum_t26BK_GATT_UUID_GATT_SRV_CHGDE "永久链接至目标")
    :   Attribute Profile Attribute UUID.

    enumerator BK_GATT_UUID_GATT_CLI_SUPPORT_FEAT[](#_CPPv4N19bk_gatt_uuid_enum_t34BK_GATT_UUID_GATT_CLI_SUPPORT_FEATE "永久链接至目标")

    enumerator BK_GATT_UUID_GATT_DATABASE_HASH[](#_CPPv4N19bk_gatt_uuid_enum_t31BK_GATT_UUID_GATT_DATABASE_HASHE "永久链接至目标")

    enumerator BK_GATT_UUID_GATT_SRV_SUPPORT_FEAT[](#_CPPv4N19bk_gatt_uuid_enum_t34BK_GATT_UUID_GATT_SRV_SUPPORT_FEATE "永久链接至目标")

    enumerator BK_GATT_UUID_ALERT_LEVEL[](#_CPPv4N19bk_gatt_uuid_enum_t24BK_GATT_UUID_ALERT_LEVELE "永久链接至目标")
    :   Link BK_Loss Service.

    enumerator BK_GATT_UUID_TX_POWER_LEVEL[](#_CPPv4N19bk_gatt_uuid_enum_t27BK_GATT_UUID_TX_POWER_LEVELE "永久链接至目标")
    :   Alert Level.

    enumerator BK_GATT_UUID_CURRENT_TIME[](#_CPPv4N19bk_gatt_uuid_enum_t25BK_GATT_UUID_CURRENT_TIMEE "永久链接至目标")
    :   TX power level.

        Current Time Service

    enumerator BK_GATT_UUID_LOCAL_TIME_INFO[](#_CPPv4N19bk_gatt_uuid_enum_t28BK_GATT_UUID_LOCAL_TIME_INFOE "永久链接至目标")
    :   Current Time.

    enumerator BK_GATT_UUID_REF_TIME_INFO[](#_CPPv4N19bk_gatt_uuid_enum_t26BK_GATT_UUID_REF_TIME_INFOE "永久链接至目标")
    :   Local time info.

    enumerator BK_GATT_UUID_NW_STATUS[](#_CPPv4N19bk_gatt_uuid_enum_t22BK_GATT_UUID_NW_STATUSE "永久链接至目标")
    :   reference time information

        Network availability Profile

    enumerator BK_GATT_UUID_NW_TRIGGER[](#_CPPv4N19bk_gatt_uuid_enum_t23BK_GATT_UUID_NW_TRIGGERE "永久链接至目标")
    :   network availability status

    enumerator BK_GATT_UUID_ALERT_STATUS[](#_CPPv4N19bk_gatt_uuid_enum_t25BK_GATT_UUID_ALERT_STATUSE "永久链接至目标")
    :   Network availability trigger.

        Phone alert

    enumerator BK_GATT_UUID_RINGER_CP[](#_CPPv4N19bk_gatt_uuid_enum_t22BK_GATT_UUID_RINGER_CPE "永久链接至目标")
    :   alert status

    enumerator BK_GATT_UUID_RINGER_SETTING[](#_CPPv4N19bk_gatt_uuid_enum_t27BK_GATT_UUID_RINGER_SETTINGE "永久链接至目标")
    :   ringer control point

    enumerator BK_GATT_UUID_GM_MEASUREMENT[](#_CPPv4N19bk_gatt_uuid_enum_t27BK_GATT_UUID_GM_MEASUREMENTE "永久链接至目标")
    :   ringer setting

        Glucose Service

    enumerator BK_GATT_UUID_GM_CONTEXT[](#_CPPv4N19bk_gatt_uuid_enum_t23BK_GATT_UUID_GM_CONTEXTE "永久链接至目标")

    enumerator BK_GATT_UUID_GM_CONTROL_POINT[](#_CPPv4N19bk_gatt_uuid_enum_t29BK_GATT_UUID_GM_CONTROL_POINTE "永久链接至目标")

    enumerator BK_GATT_UUID_GM_FEATURE[](#_CPPv4N19bk_gatt_uuid_enum_t23BK_GATT_UUID_GM_FEATUREE "永久链接至目标")

    enumerator BK_GATT_UUID_SYSTEM_ID[](#_CPPv4N19bk_gatt_uuid_enum_t22BK_GATT_UUID_SYSTEM_IDE "永久链接至目标")
    :   device information characteristic

    enumerator BK_GATT_UUID_MODEL_NUMBER_STR[](#_CPPv4N19bk_gatt_uuid_enum_t29BK_GATT_UUID_MODEL_NUMBER_STRE "永久链接至目标")

    enumerator BK_GATT_UUID_SERIAL_NUMBER_STR[](#_CPPv4N19bk_gatt_uuid_enum_t30BK_GATT_UUID_SERIAL_NUMBER_STRE "永久链接至目标")

    enumerator BK_GATT_UUID_FW_VERSION_STR[](#_CPPv4N19bk_gatt_uuid_enum_t27BK_GATT_UUID_FW_VERSION_STRE "永久链接至目标")

    enumerator BK_GATT_UUID_HW_VERSION_STR[](#_CPPv4N19bk_gatt_uuid_enum_t27BK_GATT_UUID_HW_VERSION_STRE "永久链接至目标")

    enumerator BK_GATT_UUID_SW_VERSION_STR[](#_CPPv4N19bk_gatt_uuid_enum_t27BK_GATT_UUID_SW_VERSION_STRE "永久链接至目标")

    enumerator BK_GATT_UUID_MANU_NAME[](#_CPPv4N19bk_gatt_uuid_enum_t22BK_GATT_UUID_MANU_NAMEE "永久链接至目标")

    enumerator BK_GATT_UUID_IEEE_DATA[](#_CPPv4N19bk_gatt_uuid_enum_t22BK_GATT_UUID_IEEE_DATAE "永久链接至目标")

    enumerator BK_GATT_UUID_PNP_ID[](#_CPPv4N19bk_gatt_uuid_enum_t19BK_GATT_UUID_PNP_IDE "永久链接至目标")

    enumerator BK_GATT_UUID_HID_INFORMATION[](#_CPPv4N19bk_gatt_uuid_enum_t28BK_GATT_UUID_HID_INFORMATIONE "永久链接至目标")
    :   HID characteristics.

    enumerator BK_GATT_UUID_HID_REPORT_MAP[](#_CPPv4N19bk_gatt_uuid_enum_t27BK_GATT_UUID_HID_REPORT_MAPE "永久链接至目标")

    enumerator BK_GATT_UUID_HID_CONTROL_POINT[](#_CPPv4N19bk_gatt_uuid_enum_t30BK_GATT_UUID_HID_CONTROL_POINTE "永久链接至目标")

    enumerator BK_GATT_UUID_HID_REPORT[](#_CPPv4N19bk_gatt_uuid_enum_t23BK_GATT_UUID_HID_REPORTE "永久链接至目标")

    enumerator BK_GATT_UUID_HID_PROTO_MODE[](#_CPPv4N19bk_gatt_uuid_enum_t27BK_GATT_UUID_HID_PROTO_MODEE "永久链接至目标")

    enumerator BK_GATT_UUID_HID_BT_KB_INPUT[](#_CPPv4N19bk_gatt_uuid_enum_t28BK_GATT_UUID_HID_BT_KB_INPUTE "永久链接至目标")

    enumerator BK_GATT_UUID_HID_BT_KB_OUTPUT[](#_CPPv4N19bk_gatt_uuid_enum_t29BK_GATT_UUID_HID_BT_KB_OUTPUTE "永久链接至目标")

    enumerator BK_GATT_UUID_HID_BT_MOUSE_INPUT[](#_CPPv4N19bk_gatt_uuid_enum_t31BK_GATT_UUID_HID_BT_MOUSE_INPUTE "永久链接至目标")

    enumerator BK_GATT_HEART_RATE_MEAS[](#_CPPv4N19bk_gatt_uuid_enum_t23BK_GATT_HEART_RATE_MEASE "永久链接至目标")
    :   Heart Rate Measurement.

    enumerator BK_GATT_BODY_SENSOR_LOCATION[](#_CPPv4N19bk_gatt_uuid_enum_t28BK_GATT_BODY_SENSOR_LOCATIONE "永久链接至目标")
    :   Body Sensor Location.

    enumerator BK_GATT_HEART_RATE_CNTL_POINT[](#_CPPv4N19bk_gatt_uuid_enum_t29BK_GATT_HEART_RATE_CNTL_POINTE "永久链接至目标")
    :   Heart Rate Control Point.

    enumerator BK_GATT_UUID_BATTERY_LEVEL[](#_CPPv4N19bk_gatt_uuid_enum_t26BK_GATT_UUID_BATTERY_LEVELE "永久链接至目标")
    :   Battery Service characteristics.

    enumerator BK_GATT_UUID_SC_CONTROL_POINT[](#_CPPv4N19bk_gatt_uuid_enum_t29BK_GATT_UUID_SC_CONTROL_POINTE "永久链接至目标")
    :   Sensor Service.

    enumerator BK_GATT_UUID_SENSOR_LOCATION[](#_CPPv4N19bk_gatt_uuid_enum_t28BK_GATT_UUID_SENSOR_LOCATIONE "永久链接至目标")

    enumerator BK_GATT_UUID_RSC_MEASUREMENT[](#_CPPv4N19bk_gatt_uuid_enum_t28BK_GATT_UUID_RSC_MEASUREMENTE "永久链接至目标")
    :   Runners speed and cadence service.

    enumerator BK_GATT_UUID_RSC_FEATURE[](#_CPPv4N19bk_gatt_uuid_enum_t24BK_GATT_UUID_RSC_FEATUREE "永久链接至目标")

    enumerator BK_GATT_UUID_CSC_MEASUREMENT[](#_CPPv4N19bk_gatt_uuid_enum_t28BK_GATT_UUID_CSC_MEASUREMENTE "永久链接至目标")
    :   Cycling speed and cadence service.

    enumerator BK_GATT_UUID_CSC_FEATURE[](#_CPPv4N19bk_gatt_uuid_enum_t24BK_GATT_UUID_CSC_FEATUREE "永久链接至目标")

    enumerator BK_GATT_UUID_SCAN_INT_WINDOW[](#_CPPv4N19bk_gatt_uuid_enum_t28BK_GATT_UUID_SCAN_INT_WINDOWE "永久链接至目标")
    :   Scan BK_Parameter characteristics.

    enumerator BK_GATT_UUID_SCAN_REFRESH[](#_CPPv4N19bk_gatt_uuid_enum_t25BK_GATT_UUID_SCAN_REFRESHE "永久链接至目标")

enum bk_gatt_status_t[](#_CPPv416bk_gatt_status_t "永久链接至目标")
:   GATT success code and error codes.


    *Values:*

    enumerator BK_GATT_OK[](#_CPPv4N16bk_gatt_status_t10BK_GATT_OKE "永久链接至目标")

    enumerator BK_GATT_INVALID_HANDLE[](#_CPPv4N16bk_gatt_status_t22BK_GATT_INVALID_HANDLEE "永久链接至目标")

    enumerator BK_GATT_READ_NOT_PERMIT[](#_CPPv4N16bk_gatt_status_t23BK_GATT_READ_NOT_PERMITE "永久链接至目标")

    enumerator BK_GATT_WRITE_NOT_PERMIT[](#_CPPv4N16bk_gatt_status_t24BK_GATT_WRITE_NOT_PERMITE "永久链接至目标")

    enumerator BK_GATT_INVALID_PDU[](#_CPPv4N16bk_gatt_status_t19BK_GATT_INVALID_PDUE "永久链接至目标")

    enumerator BK_GATT_INSUF_AUTHENTICATION[](#_CPPv4N16bk_gatt_status_t28BK_GATT_INSUF_AUTHENTICATIONE "永久链接至目标")

    enumerator BK_GATT_REQ_NOT_SUPPORTED[](#_CPPv4N16bk_gatt_status_t25BK_GATT_REQ_NOT_SUPPORTEDE "永久链接至目标")

    enumerator BK_GATT_INVALID_OFFSET[](#_CPPv4N16bk_gatt_status_t22BK_GATT_INVALID_OFFSETE "永久链接至目标")

    enumerator BK_GATT_INSUF_AUTHORIZATION[](#_CPPv4N16bk_gatt_status_t27BK_GATT_INSUF_AUTHORIZATIONE "永久链接至目标")

    enumerator BK_GATT_PREPARE_Q_FULL[](#_CPPv4N16bk_gatt_status_t22BK_GATT_PREPARE_Q_FULLE "永久链接至目标")

    enumerator BK_GATT_NOT_FOUND[](#_CPPv4N16bk_gatt_status_t17BK_GATT_NOT_FOUNDE "永久链接至目标")

    enumerator BK_GATT_NOT_LONG[](#_CPPv4N16bk_gatt_status_t16BK_GATT_NOT_LONGE "永久链接至目标")

    enumerator BK_GATT_INSUF_KEY_SIZE[](#_CPPv4N16bk_gatt_status_t22BK_GATT_INSUF_KEY_SIZEE "永久链接至目标")

    enumerator BK_GATT_INVALID_ATTR_LEN[](#_CPPv4N16bk_gatt_status_t24BK_GATT_INVALID_ATTR_LENE "永久链接至目标")

    enumerator BK_GATT_ERR_UNLIKELY[](#_CPPv4N16bk_gatt_status_t20BK_GATT_ERR_UNLIKELYE "永久链接至目标")

    enumerator BK_GATT_INSUF_ENCRYPTION[](#_CPPv4N16bk_gatt_status_t24BK_GATT_INSUF_ENCRYPTIONE "永久链接至目标")

    enumerator BK_GATT_UNSUPPORT_GRP_TYPE[](#_CPPv4N16bk_gatt_status_t26BK_GATT_UNSUPPORT_GRP_TYPEE "永久链接至目标")

    enumerator BK_GATT_INSUF_RESOURCE[](#_CPPv4N16bk_gatt_status_t22BK_GATT_INSUF_RESOURCEE "永久链接至目标")

    enumerator BK_GATT_DB_OUT_OF_SYNC[](#_CPPv4N16bk_gatt_status_t22BK_GATT_DB_OUT_OF_SYNCE "永久链接至目标")

    enumerator BK_GATT_PARAM_VAL_NOT_ALLOW[](#_CPPv4N16bk_gatt_status_t27BK_GATT_PARAM_VAL_NOT_ALLOWE "永久链接至目标")

    enumerator BK_GATT_WRITE_REQ_REJECT[](#_CPPv4N16bk_gatt_status_t24BK_GATT_WRITE_REQ_REJECTE "永久链接至目标")

    enumerator BK_GATT_CCC_CFG_ERR[](#_CPPv4N16bk_gatt_status_t19BK_GATT_CCC_CFG_ERRE "永久链接至目标")
    :   Write Request Rejected.

    enumerator BK_GATT_PRC_IN_PROGRESS[](#_CPPv4N16bk_gatt_status_t23BK_GATT_PRC_IN_PROGRESSE "永久链接至目标")
    :   0xFD Client Characteristic Configuration Descriptor Improperly Configured

    enumerator BK_GATT_OUT_OF_RANGE[](#_CPPv4N16bk_gatt_status_t20BK_GATT_OUT_OF_RANGEE "永久链接至目标")
    :   0xFE Procedure Already in progress

    enumerator BK_GATT_UNKNOWN_ERROR[](#_CPPv4N16bk_gatt_status_t21BK_GATT_UNKNOWN_ERRORE "永久链接至目标")
    :   0xFF Attribute value out of range */

enum bk_gatt_conn_reason_t[](#_CPPv421bk_gatt_conn_reason_t "永久链接至目标")
:   Gatt Connection reason enum.


    *Values:*

    enumerator BK_GATT_CONN_UNKNOWN[](#_CPPv4N21bk_gatt_conn_reason_t20BK_GATT_CONN_UNKNOWNE "永久链接至目标")
    :   Gatt connection unknown

enum bk_gatt_auth_req_t[](#_CPPv418bk_gatt_auth_req_t "永久链接至目标")
:   Gatt authentication request type.


    *Values:*

    enumerator BK_GATT_AUTH_REQ_NONE[](#_CPPv4N18bk_gatt_auth_req_t21BK_GATT_AUTH_REQ_NONEE "永久链接至目标")

enum bk_gatt_perm_enum_t[](#_CPPv419bk_gatt_perm_enum_t "永久链接至目标")
:   Attribute permissions.


    **Attention**
    :   When MITM is enable, key generation method can not be Just Work. This require both local and peer iocap configuration suitable. See bluetooth core specification Version 5.4 | Vol 3, Part H, 2.3.5.1 Selecting key generation method.


    *Values:*

    enumerator BK_GATT_PERM_READ[](#_CPPv4N19bk_gatt_perm_enum_t17BK_GATT_PERM_READE "永久链接至目标")

    enumerator BK_GATT_PERM_READ_ENCRYPTED[](#_CPPv4N19bk_gatt_perm_enum_t27BK_GATT_PERM_READ_ENCRYPTEDE "永久链接至目标")

    enumerator BK_GATT_PERM_READ_ENC_MITM[](#_CPPv4N19bk_gatt_perm_enum_t26BK_GATT_PERM_READ_ENC_MITME "永久链接至目标")

    enumerator BK_GATT_PERM_WRITE[](#_CPPv4N19bk_gatt_perm_enum_t18BK_GATT_PERM_WRITEE "永久链接至目标")

    enumerator BK_GATT_PERM_WRITE_ENCRYPTED[](#_CPPv4N19bk_gatt_perm_enum_t28BK_GATT_PERM_WRITE_ENCRYPTEDE "永久链接至目标")

    enumerator BK_GATT_PERM_WRITE_ENC_MITM[](#_CPPv4N19bk_gatt_perm_enum_t27BK_GATT_PERM_WRITE_ENC_MITME "永久链接至目标")

    enumerator BK_GATT_PERM_WRITE_SIGNED[](#_CPPv4N19bk_gatt_perm_enum_t25BK_GATT_PERM_WRITE_SIGNEDE "永久链接至目标")

    enumerator BK_GATT_PERM_WRITE_SIGNED_MITM[](#_CPPv4N19bk_gatt_perm_enum_t30BK_GATT_PERM_WRITE_SIGNED_MITME "永久链接至目标")

    enumerator BK_GATT_PERM_READ_AUTHORIZATION[](#_CPPv4N19bk_gatt_perm_enum_t31BK_GATT_PERM_READ_AUTHORIZATIONE "永久链接至目标")

    enumerator BK_GATT_PERM_WRITE_AUTHORIZATION[](#_CPPv4N19bk_gatt_perm_enum_t32BK_GATT_PERM_WRITE_AUTHORIZATIONE "永久链接至目标")

enum bk_gatt_char_prop_enum_t[](#_CPPv424bk_gatt_char_prop_enum_t "永久链接至目标")
:   definition of characteristic properties


    *Values:*

    enumerator BK_GATT_CHAR_PROP_BIT_BROADCAST[](#_CPPv4N24bk_gatt_char_prop_enum_t31BK_GATT_CHAR_PROP_BIT_BROADCASTE "永久链接至目标")

    enumerator BK_GATT_CHAR_PROP_BIT_READ[](#_CPPv4N24bk_gatt_char_prop_enum_t26BK_GATT_CHAR_PROP_BIT_READE "永久链接至目标")

    enumerator BK_GATT_CHAR_PROP_BIT_WRITE_NR[](#_CPPv4N24bk_gatt_char_prop_enum_t30BK_GATT_CHAR_PROP_BIT_WRITE_NRE "永久链接至目标")

    enumerator BK_GATT_CHAR_PROP_BIT_WRITE[](#_CPPv4N24bk_gatt_char_prop_enum_t27BK_GATT_CHAR_PROP_BIT_WRITEE "永久链接至目标")

    enumerator BK_GATT_CHAR_PROP_BIT_NOTIFY[](#_CPPv4N24bk_gatt_char_prop_enum_t28BK_GATT_CHAR_PROP_BIT_NOTIFYE "永久链接至目标")

    enumerator BK_GATT_CHAR_PROP_BIT_INDICATE[](#_CPPv4N24bk_gatt_char_prop_enum_t30BK_GATT_CHAR_PROP_BIT_INDICATEE "永久链接至目标")

    enumerator BK_GATT_CHAR_PROP_BIT_AUTH_SIGNED_WRITE[](#_CPPv4N24bk_gatt_char_prop_enum_t39BK_GATT_CHAR_PROP_BIT_AUTH_SIGNED_WRITEE "永久链接至目标")

    enumerator BK_GATT_CHAR_PROP_BIT_EXT_PROP[](#_CPPv4N24bk_gatt_char_prop_enum_t30BK_GATT_CHAR_PROP_BIT_EXT_PROPE "永久链接至目标")

enum bk_service_source_t[](#_CPPv419bk_service_source_t "永久链接至目标")
:   gatt service source


    *Values:*

    enumerator BK_GATT_SERVICE_FROM_REMOTE_DEVICE[](#_CPPv4N19bk_service_source_t34BK_GATT_SERVICE_FROM_REMOTE_DEVICEE "永久链接至目标")

    enumerator BK_GATT_SERVICE_FROM_NVS_FLASH[](#_CPPv4N19bk_service_source_t30BK_GATT_SERVICE_FROM_NVS_FLASHE "永久链接至目标")

    enumerator BK_GATT_SERVICE_FROM_UNKNOWN[](#_CPPv4N19bk_service_source_t28BK_GATT_SERVICE_FROM_UNKNOWNE "永久链接至目标")

enum bk_gatt_write_type_t[](#_CPPv420bk_gatt_write_type_t "永久链接至目标")
:   Gatt write type.


    *Values:*

    enumerator BK_GATT_WRITE_TYPE_NO_RSP[](#_CPPv4N20bk_gatt_write_type_t25BK_GATT_WRITE_TYPE_NO_RSPE "永久链接至目标")
    :   Gatt write attribute need no response

    enumerator BK_GATT_WRITE_TYPE_RSP[](#_CPPv4N20bk_gatt_write_type_t22BK_GATT_WRITE_TYPE_RSPE "永久链接至目标")
    :   Gatt write attribute need remote response


### Header File[](#id20 "永久链接至标题")


- [bluetooth/bk_dm_bluetooth.h](https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_bluetooth.h "https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_bluetooth.h")


### Functions[](#id21 "永久链接至标题")

[bk_bluetooth_status_t](#_CPPv421bk_bluetooth_status_t "bk_bluetooth_status_t") bk_bluetooth_get_status(void)[](#_CPPv423bk_bluetooth_get_statusv "永久链接至目标")
:   Get bluetooth status.

    返回
    :   Bluetooth status

[bt_err_t](#_CPPv48bt_err_t "bt_err_t") bk_bluetooth_init(void)[](#_CPPv417bk_bluetooth_initv "永久链接至目标")
:   init bluetooth.

    返回
    :   - BT_OK: success

        - others: fail

[bt_err_t](#_CPPv48bt_err_t "bt_err_t") bk_bluetooth_deinit(void)[](#_CPPv419bk_bluetooth_deinitv "永久链接至目标")
:   deinit bluetooth.

    返回
    :   - BT_OK: success

        - others: fail

[bt_err_t](#_CPPv48bt_err_t "bt_err_t") bk_bluetooth_get_address(uint8_t *addr)[](#_CPPv424bk_bluetooth_get_addressP7uint8_t "永久链接至目标")
:   Get bluetooth device address. Must use after “bk_bluetooth_init”.

    参数
    :   **addr** – **[out]** - bluetooth device address

    返回
    :   - BT_OK: success

        - others: fail


### Header File[](#id22 "永久链接至标题")


- [bluetooth/bk_dm_bluetooth_types.h](https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_bluetooth_types.h "https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_bluetooth_types.h")


### Structures[](#id23 "永久链接至标题")

struct bt_cmd_param_t[](#_CPPv414bt_cmd_param_t "永久链接至目标")
:   Public Members

    uint8_t cmd_idx[](#_CPPv4N14bt_cmd_param_t7cmd_idxE "永久链接至目标")
    :   actv_idx

    [bt_err_t](#_CPPv48bt_err_t "bt_err_t") status[](#_CPPv4N14bt_cmd_param_t6statusE "永久链接至目标")
    :   The status for this command

struct bk_bt_uuid_t[](#_CPPv412bk_bt_uuid_t "永久链接至目标")
:   UUID type.

    Public Members

    uint16_t len[](#_CPPv4N12bk_bt_uuid_t3lenE "永久链接至目标")
    :   UUID length, 16bit, 32bit or 128bit

    uint16_t uuid16[](#_CPPv4N12bk_bt_uuid_t6uuid16E "永久链接至目标")
    :   16bit UUID

    uint32_t uuid32[](#_CPPv4N12bk_bt_uuid_t6uuid32E "永久链接至目标")
    :   32bit UUID

    uint8_t uuid128[BK_UUID_LEN_128][](#_CPPv4N12bk_bt_uuid_t7uuid128E "永久链接至目标")
    :   128bit UUID

    union [bk_bt_uuid_t](#_CPPv412bk_bt_uuid_t "bk_bt_uuid_t")::[anonymous] uuid[](#_CPPv4N12bk_bt_uuid_t4uuidE "永久链接至目标")
    :   UUID


### Macros[](#id24 "永久链接至标题")

BK_BT_ADDR_LEN[](#c.BK_BT_ADDR_LEN "永久链接至目标")

BK_ERR_BT_SUCCESS[](#c.BK_ERR_BT_SUCCESS "永久链接至目标")
:   success

BK_ERR_BT_FAIL[](#c.BK_ERR_BT_FAIL "永久链接至目标")
:   fail

BK_ERR_BT_NO_MEM[](#c.BK_ERR_BT_NO_MEM "永久链接至目标")
:   no mem

BK_ERR_BT_PROFILE[](#c.BK_ERR_BT_PROFILE "永久链接至目标")
:   profile err

BK_ERR_BT_CMD_NOT_SUPPORT[](#c.BK_ERR_BT_CMD_NOT_SUPPORT "永久链接至目标")
:   unknow cmd err

BK_ERR_BT_UNKNOW_IDX[](#c.BK_ERR_BT_UNKNOW_IDX "永久链接至目标")
:   index err, suchas conn_ind

BK_ERR_BT_BT_STATUS[](#c.BK_ERR_BT_BT_STATUS "永久链接至目标")
:   ble status not match

BK_ERR_BT_CMD_RUN[](#c.BK_ERR_BT_CMD_RUN "永久链接至目标")
:   cmd run err

BK_ERR_BT_INIT_CREATE[](#c.BK_ERR_BT_INIT_CREATE "永久链接至目标")
:   create init err, such as bk_ble_create_init

BK_ERR_BT_INIT_STATE[](#c.BK_ERR_BT_INIT_STATE "永久链接至目标")
:   current init status not match

BT_OK[](#c.BT_OK "永久链接至目标")
:   success

BT_FAIL[](#c.BT_FAIL "永久链接至目标")
:   failure

BT_INTERFACE_NOT_SUPPORT[](#c.BT_INTERFACE_NOT_SUPPORT "永久链接至目标")
:   interface not support

BK_BT_OCTET16_LEN[](#c.BK_BT_OCTET16_LEN "永久链接至目标")

BK_BT_OCTET8_LEN[](#c.BK_BT_OCTET8_LEN "永久链接至目标")

BK_UUID_LEN_16[](#c.BK_UUID_LEN_16 "永久链接至目标")

BK_UUID_LEN_32[](#c.BK_UUID_LEN_32 "永久链接至目标")

BK_UUID_LEN_128[](#c.BK_UUID_LEN_128 "永久链接至目标")

BK_BD_ADDR_LEN[](#c.BK_BD_ADDR_LEN "永久链接至目标")
:   Bluetooth address length.


### Type Definitions[](#id25 "永久链接至标题")

typedef [bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") ble_err_t[](#_CPPv49ble_err_t "永久链接至目标")
:   ble api return enum

typedef int bt_err_t[](#_CPPv48bt_err_t "永久链接至目标")

typedef uint8_t bk_bt_octet16_t[BK_BT_OCTET16_LEN][](#_CPPv415bk_bt_octet16_t "永久链接至目标")

typedef uint8_t bk_bt_octet8_t[BK_BT_OCTET8_LEN][](#_CPPv414bk_bt_octet8_t "永久链接至目标")

typedef uint8_t bk_link_key_t[BK_BT_OCTET16_LEN][](#_CPPv413bk_link_key_t "永久链接至目标")

typedef uint8_t bk_bd_addr_t[BK_BD_ADDR_LEN][](#_CPPv412bk_bd_addr_t "永久链接至目标")
:   Bluetooth device address.

typedef void (*bt_cmd_cb_t)([bt_cmd_t](#_CPPv48bt_cmd_t "bt_cmd_t") cmd, [bt_cmd_param_t](#_CPPv414bt_cmd_param_t "bt_cmd_param_t") *param)[](#_CPPv411bt_cmd_cb_t "永久链接至目标")
:   for sync bt api call return

    most bt api have bt_cmd_cb_t param, you must wait is callback.

    Param -
    :   cmd: cmd id.


        - param: param


### Enumerations[](#id26 "永久链接至标题")

enum bk_bluetooth_status_t[](#_CPPv421bk_bluetooth_status_t "永久链接至目标")
:   Bluetooth status type, to indicate whether the bluetooth is ready.


    *Values:*

    enumerator BK_BLUETOOTH_STATUS_UNINITIALIZED[](#_CPPv4N21bk_bluetooth_status_t33BK_BLUETOOTH_STATUS_UNINITIALIZEDE "永久链接至目标")
    :   Bluetooth not initialized

    enumerator BK_BLUETOOTH_STATUS_ENABLED[](#_CPPv4N21bk_bluetooth_status_t27BK_BLUETOOTH_STATUS_ENABLEDE "永久链接至目标")
    :   Bluetooth initialized and enabled

enum BK_BT_CONTROLLER_STACK_TYPE[](#_CPPv427BK_BT_CONTROLLER_STACK_TYPE "永久链接至目标")
:   *Values:*

    enumerator BK_BT_CONTROLLER_STACK_TYPE_BTDM_5_2[](#_CPPv4N27BK_BT_CONTROLLER_STACK_TYPE36BK_BT_CONTROLLER_STACK_TYPE_BTDM_5_2E "永久链接至目标")

    enumerator BK_BT_CONTROLLER_STACK_NOT_SUPPORT[](#_CPPv4N27BK_BT_CONTROLLER_STACK_TYPE34BK_BT_CONTROLLER_STACK_NOT_SUPPORTE "永久链接至目标")

enum BK_BT_HOST_STACK_TYPE[](#_CPPv421BK_BT_HOST_STACK_TYPE "永久链接至目标")
:   *Values:*

    enumerator BK_BT_HOST_STACK_TYPE_ETHERMIND[](#_CPPv4N21BK_BT_HOST_STACK_TYPE31BK_BT_HOST_STACK_TYPE_ETHERMINDE "永久链接至目标")

    enumerator BK_BT_HOST_STACK_TYPE_NOT_SUPPORT[](#_CPPv4N21BK_BT_HOST_STACK_TYPE33BK_BT_HOST_STACK_TYPE_NOT_SUPPORTE "永久链接至目标")

enum bk_bt_status_t[](#_CPPv414bk_bt_status_t "永久链接至目标")
:   Status Return Value.


    *Values:*

    enumerator BK_BT_STATUS_SUCCESS[](#_CPPv4N14bk_bt_status_t20BK_BT_STATUS_SUCCESSE "永久链接至目标")

    enumerator BK_BT_STATUS_UNKNOWN_HCI_COMMAND[](#_CPPv4N14bk_bt_status_t32BK_BT_STATUS_UNKNOWN_HCI_COMMANDE "永久链接至目标")

    enumerator BK_BT_STATUS_UNKNOWN_CONNECTION_ID[](#_CPPv4N14bk_bt_status_t34BK_BT_STATUS_UNKNOWN_CONNECTION_IDE "永久链接至目标")

    enumerator BK_BT_STATUS_HARDWARE_FAILURE[](#_CPPv4N14bk_bt_status_t29BK_BT_STATUS_HARDWARE_FAILUREE "永久链接至目标")

    enumerator BK_BT_STATUS_PAGE_TIMEOUT[](#_CPPv4N14bk_bt_status_t25BK_BT_STATUS_PAGE_TIMEOUTE "永久链接至目标")

    enumerator BK_BT_STATUS_AUTH_FAILURE[](#_CPPv4N14bk_bt_status_t25BK_BT_STATUS_AUTH_FAILUREE "永久链接至目标")

    enumerator BK_BT_STATUS_PIN_MISSING[](#_CPPv4N14bk_bt_status_t24BK_BT_STATUS_PIN_MISSINGE "永久链接至目标")

    enumerator BK_BT_STATUS_MEMORY_CAPA_EXCEED[](#_CPPv4N14bk_bt_status_t31BK_BT_STATUS_MEMORY_CAPA_EXCEEDE "永久链接至目标")

    enumerator BK_BT_STATUS_CON_TIMEOUT[](#_CPPv4N14bk_bt_status_t24BK_BT_STATUS_CON_TIMEOUTE "永久链接至目标")

    enumerator BK_BT_STATUS_CON_LIMIT_EXCEED[](#_CPPv4N14bk_bt_status_t29BK_BT_STATUS_CON_LIMIT_EXCEEDE "永久链接至目标")

    enumerator BK_BT_STATUS_SYNC_CON_LIMIT_DEV_EXCEED[](#_CPPv4N14bk_bt_status_t38BK_BT_STATUS_SYNC_CON_LIMIT_DEV_EXCEEDE "永久链接至目标")

    enumerator BK_BT_STATUS_CON_ALREADY_EXISTS[](#_CPPv4N14bk_bt_status_t31BK_BT_STATUS_CON_ALREADY_EXISTSE "永久链接至目标")

    enumerator BK_BT_STATUS_COMMAND_DISALLOWED[](#_CPPv4N14bk_bt_status_t31BK_BT_STATUS_COMMAND_DISALLOWEDE "永久链接至目标")

    enumerator BK_BT_STATUS_CONN_REJ_LIMITED_RESOURCES[](#_CPPv4N14bk_bt_status_t39BK_BT_STATUS_CONN_REJ_LIMITED_RESOURCESE "永久链接至目标")

    enumerator BK_BT_STATUS_CONN_REJ_SECURITY_REASONS[](#_CPPv4N14bk_bt_status_t38BK_BT_STATUS_CONN_REJ_SECURITY_REASONSE "永久链接至目标")

    enumerator BK_BT_STATUS_CONN_REJ_UNACCEPTABLE_BDADDR[](#_CPPv4N14bk_bt_status_t41BK_BT_STATUS_CONN_REJ_UNACCEPTABLE_BDADDRE "永久链接至目标")

    enumerator BK_BT_STATUS_CONN_ACCEPT_TIMEOUT_EXCEED[](#_CPPv4N14bk_bt_status_t39BK_BT_STATUS_CONN_ACCEPT_TIMEOUT_EXCEEDE "永久链接至目标")

    enumerator BK_BT_STATUS_UNSUPPORTED[](#_CPPv4N14bk_bt_status_t24BK_BT_STATUS_UNSUPPORTEDE "永久链接至目标")

    enumerator BK_BT_STATUS_INVALID_HCI_PARAM[](#_CPPv4N14bk_bt_status_t30BK_BT_STATUS_INVALID_HCI_PARAME "永久链接至目标")

    enumerator BK_BT_STATUS_REMOTE_USER_TERM_CON[](#_CPPv4N14bk_bt_status_t33BK_BT_STATUS_REMOTE_USER_TERM_CONE "永久链接至目标")

    enumerator BK_BT_STATUS_REMOTE_DEV_TERM_LOW_RESOURCES[](#_CPPv4N14bk_bt_status_t42BK_BT_STATUS_REMOTE_DEV_TERM_LOW_RESOURCESE "永久链接至目标")

    enumerator BK_BT_STATUS_REMOTE_DEV_POWER_OFF[](#_CPPv4N14bk_bt_status_t33BK_BT_STATUS_REMOTE_DEV_POWER_OFFE "永久链接至目标")

    enumerator BK_BT_STATUS_CON_TERM_BY_LOCAL_HOST[](#_CPPv4N14bk_bt_status_t35BK_BT_STATUS_CON_TERM_BY_LOCAL_HOSTE "永久链接至目标")

    enumerator BK_BT_STATUS_REPEATED_ATTEMPTS[](#_CPPv4N14bk_bt_status_t30BK_BT_STATUS_REPEATED_ATTEMPTSE "永久链接至目标")

    enumerator BK_BT_STATUS_PAIRING_NOT_ALLOWED[](#_CPPv4N14bk_bt_status_t32BK_BT_STATUS_PAIRING_NOT_ALLOWEDE "永久链接至目标")

    enumerator BK_BT_STATUS_UNKNOWN_LMP_PDU[](#_CPPv4N14bk_bt_status_t28BK_BT_STATUS_UNKNOWN_LMP_PDUE "永久链接至目标")

    enumerator BK_BT_STATUS_UNSUPPORTED_REMOTE_FEATURE[](#_CPPv4N14bk_bt_status_t39BK_BT_STATUS_UNSUPPORTED_REMOTE_FEATUREE "永久链接至目标")

    enumerator BK_BT_STATUS_SCO_OFFSET_REJECTED[](#_CPPv4N14bk_bt_status_t32BK_BT_STATUS_SCO_OFFSET_REJECTEDE "永久链接至目标")

    enumerator BK_BT_STATUS_SCO_INTERVAL_REJECTED[](#_CPPv4N14bk_bt_status_t34BK_BT_STATUS_SCO_INTERVAL_REJECTEDE "永久链接至目标")

    enumerator BK_BT_STATUS_SCO_AIR_MODE_REJECTED[](#_CPPv4N14bk_bt_status_t34BK_BT_STATUS_SCO_AIR_MODE_REJECTEDE "永久链接至目标")

    enumerator BK_BT_STATUS_INVALID_LMP_PARAM[](#_CPPv4N14bk_bt_status_t30BK_BT_STATUS_INVALID_LMP_PARAME "永久链接至目标")

    enumerator BK_BT_STATUS_UNSPECIFIED_ERROR[](#_CPPv4N14bk_bt_status_t30BK_BT_STATUS_UNSPECIFIED_ERRORE "永久链接至目标")

    enumerator BK_BT_STATUS_UNSUPPORTED_LMP_PARAM_VALUE[](#_CPPv4N14bk_bt_status_t40BK_BT_STATUS_UNSUPPORTED_LMP_PARAM_VALUEE "永久链接至目标")

    enumerator BK_BT_STATUS_ROLE_CHANGE_NOT_ALLOWED[](#_CPPv4N14bk_bt_status_t36BK_BT_STATUS_ROLE_CHANGE_NOT_ALLOWEDE "永久链接至目标")

    enumerator BK_BT_STATUS_LMP_RSP_TIMEOUT[](#_CPPv4N14bk_bt_status_t28BK_BT_STATUS_LMP_RSP_TIMEOUTE "永久链接至目标")

    enumerator BK_BT_STATUS_LMP_COLLISION[](#_CPPv4N14bk_bt_status_t26BK_BT_STATUS_LMP_COLLISIONE "永久链接至目标")

    enumerator BK_BT_STATUS_LMP_PDU_NOT_ALLOWED[](#_CPPv4N14bk_bt_status_t32BK_BT_STATUS_LMP_PDU_NOT_ALLOWEDE "永久链接至目标")

    enumerator BK_BT_STATUS_ENC_MODE_NOT_ACCEPT[](#_CPPv4N14bk_bt_status_t32BK_BT_STATUS_ENC_MODE_NOT_ACCEPTE "永久链接至目标")

    enumerator BK_BT_STATUS_LINK_KEY_CANT_CHANGE[](#_CPPv4N14bk_bt_status_t33BK_BT_STATUS_LINK_KEY_CANT_CHANGEE "永久链接至目标")

    enumerator BK_BT_STATUS_QOS_NOT_SUPPORTED[](#_CPPv4N14bk_bt_status_t30BK_BT_STATUS_QOS_NOT_SUPPORTEDE "永久链接至目标")

    enumerator BK_BT_STATUS_INSTANT_PASSED[](#_CPPv4N14bk_bt_status_t27BK_BT_STATUS_INSTANT_PASSEDE "永久链接至目标")

    enumerator BK_BT_STATUS_PAIRING_WITH_UNIT_KEY_NOT_SUP[](#_CPPv4N14bk_bt_status_t42BK_BT_STATUS_PAIRING_WITH_UNIT_KEY_NOT_SUPE "永久链接至目标")

    enumerator BK_BT_STATUS_DIFF_TRANSACTION_COLLISION[](#_CPPv4N14bk_bt_status_t39BK_BT_STATUS_DIFF_TRANSACTION_COLLISIONE "永久链接至目标")

    enumerator BK_BT_STATUS_QOS_UNACCEPTABLE_PARAM[](#_CPPv4N14bk_bt_status_t35BK_BT_STATUS_QOS_UNACCEPTABLE_PARAME "永久链接至目标")

    enumerator BK_BT_STATUS_QOS_REJECTED[](#_CPPv4N14bk_bt_status_t25BK_BT_STATUS_QOS_REJECTEDE "永久链接至目标")

    enumerator BK_BT_STATUS_CHANNEL_CLASS_NOT_SUP[](#_CPPv4N14bk_bt_status_t34BK_BT_STATUS_CHANNEL_CLASS_NOT_SUPE "永久链接至目标")

    enumerator BK_BT_STATUS_INSUFFICIENT_SECURITY[](#_CPPv4N14bk_bt_status_t34BK_BT_STATUS_INSUFFICIENT_SECURITYE "永久链接至目标")

    enumerator BK_BT_STATUS_PARAM_OUT_OF_MAND_RANGE[](#_CPPv4N14bk_bt_status_t36BK_BT_STATUS_PARAM_OUT_OF_MAND_RANGEE "永久链接至目标")

    enumerator BK_BT_STATUS_ROLE_SWITCH_PEND[](#_CPPv4N14bk_bt_status_t29BK_BT_STATUS_ROLE_SWITCH_PENDE "永久链接至目标")

    enumerator BK_BT_STATUS_RESERVED_SLOT_VIOLATION[](#_CPPv4N14bk_bt_status_t36BK_BT_STATUS_RESERVED_SLOT_VIOLATIONE "永久链接至目标")

    enumerator BK_BT_STATUS_ROLE_SWITCH_FAIL[](#_CPPv4N14bk_bt_status_t29BK_BT_STATUS_ROLE_SWITCH_FAILE "永久链接至目标")

    enumerator BK_BT_STATUS_EIR_TOO_LARGE[](#_CPPv4N14bk_bt_status_t26BK_BT_STATUS_EIR_TOO_LARGEE "永久链接至目标")

    enumerator BK_BT_STATUS_SP_NOT_SUPPORTED_HOST[](#_CPPv4N14bk_bt_status_t34BK_BT_STATUS_SP_NOT_SUPPORTED_HOSTE "永久链接至目标")

    enumerator BK_BT_STATUS_HOST_BUSY_PAIRING[](#_CPPv4N14bk_bt_status_t30BK_BT_STATUS_HOST_BUSY_PAIRINGE "永久链接至目标")

    enumerator BK_BT_STATUS_CONTROLLER_BUSY[](#_CPPv4N14bk_bt_status_t28BK_BT_STATUS_CONTROLLER_BUSYE "永久链接至目标")

    enumerator BK_BT_STATUS_UNACCEPTABLE_CONN_PARAM[](#_CPPv4N14bk_bt_status_t36BK_BT_STATUS_UNACCEPTABLE_CONN_PARAME "永久链接至目标")

    enumerator BK_BT_STATUS_ADV_TO[](#_CPPv4N14bk_bt_status_t19BK_BT_STATUS_ADV_TOE "永久链接至目标")

    enumerator BK_BT_STATUS_TERMINATED_MIC_FAILURE[](#_CPPv4N14bk_bt_status_t35BK_BT_STATUS_TERMINATED_MIC_FAILUREE "永久链接至目标")

    enumerator BK_BT_STATUS_CONN_FAILED_TO_BE_EST[](#_CPPv4N14bk_bt_status_t34BK_BT_STATUS_CONN_FAILED_TO_BE_ESTE "永久链接至目标")

    enumerator BK_BT_STATUS_CCA_REJ_USE_CLOCK_DRAG[](#_CPPv4N14bk_bt_status_t35BK_BT_STATUS_CCA_REJ_USE_CLOCK_DRAGE "永久链接至目标")

    enumerator BK_BT_STATUS_TYPE0_SUBMAP_NOT_DEFINED[](#_CPPv4N14bk_bt_status_t37BK_BT_STATUS_TYPE0_SUBMAP_NOT_DEFINEDE "永久链接至目标")

    enumerator BK_BT_STATUS_UNKNOWN_ADVERTISING_ID[](#_CPPv4N14bk_bt_status_t35BK_BT_STATUS_UNKNOWN_ADVERTISING_IDE "永久链接至目标")

    enumerator BK_BT_STATUS_LIMIT_REACHED[](#_CPPv4N14bk_bt_status_t26BK_BT_STATUS_LIMIT_REACHEDE "永久链接至目标")

    enumerator BK_BT_STATUS_OPERATION_CANCELED_BY_HOST[](#_CPPv4N14bk_bt_status_t39BK_BT_STATUS_OPERATION_CANCELED_BY_HOSTE "永久链接至目标")

    enumerator BK_BT_STATUS_PKT_TOO_LONG[](#_CPPv4N14bk_bt_status_t25BK_BT_STATUS_PKT_TOO_LONGE "永久链接至目标")

    enumerator BK_BT_STATUS_TOO_LATE[](#_CPPv4N14bk_bt_status_t21BK_BT_STATUS_TOO_LATEE "永久链接至目标")

    enumerator BK_BT_STATUS_TOO_EARLY[](#_CPPv4N14bk_bt_status_t22BK_BT_STATUS_TOO_EARLYE "永久链接至目标")

    enumerator BK_BT_STATUS_UNDEFINED[](#_CPPv4N14bk_bt_status_t22BK_BT_STATUS_UNDEFINEDE "永久链接至目标")

enum bt_cmd_t[](#_CPPv48bt_cmd_t "永久链接至目标")
:   *Values:*

    enumerator BT_CMD_INQUIRY[](#_CPPv4N8bt_cmd_t14BT_CMD_INQUIRYE "永久链接至目标")

    enumerator BT_CMD_CREATE_CONNECT[](#_CPPv4N8bt_cmd_t21BT_CMD_CREATE_CONNECTE "永久链接至目标")

    enumerator BT_CMD_DISCONNECT[](#_CPPv4N8bt_cmd_t17BT_CMD_DISCONNECTE "永久链接至目标")

    enumerator BT_CMD_SDP[](#_CPPv4N8bt_cmd_t10BT_CMD_SDPE "永久链接至目标")

    enumerator BT_CMD_READ_SCAN_ENABLE[](#_CPPv4N8bt_cmd_t23BT_CMD_READ_SCAN_ENABLEE "永久链接至目标")

    enumerator BT_CMD_WRITE_SCAN_ENABLE[](#_CPPv4N8bt_cmd_t24BT_CMD_WRITE_SCAN_ENABLEE "永久链接至目标")

    enumerator BT_CMD_MAX[](#_CPPv4N8bt_cmd_t10BT_CMD_MAXE "永久链接至目标")

enum bk_bt_dev_type_t[](#_CPPv416bk_bt_dev_type_t "永久链接至目标")
:   Bluetooth device type.


    *Values:*

    enumerator BK_BT_DEVICE_TYPE_BREDR[](#_CPPv4N16bk_bt_dev_type_t23BK_BT_DEVICE_TYPE_BREDRE "永久链接至目标")

    enumerator BK_BT_DEVICE_TYPE_BLE[](#_CPPv4N16bk_bt_dev_type_t21BK_BT_DEVICE_TYPE_BLEE "永久链接至目标")

    enumerator BK_BT_DEVICE_TYPE_DUMO[](#_CPPv4N16bk_bt_dev_type_t22BK_BT_DEVICE_TYPE_DUMOE "永久链接至目标")

enum bk_ble_addr_type_t[](#_CPPv418bk_ble_addr_type_t "永久链接至目标")
:   BLE device address type.


    *Values:*

    enumerator BLE_ADDR_TYPE_PUBLIC[](#_CPPv4N18bk_ble_addr_type_t20BLE_ADDR_TYPE_PUBLICE "永久链接至目标")

    enumerator BLE_ADDR_TYPE_RANDOM[](#_CPPv4N18bk_ble_addr_type_t20BLE_ADDR_TYPE_RANDOME "永久链接至目标")

    enumerator BLE_ADDR_TYPE_RPA_PUBLIC[](#_CPPv4N18bk_ble_addr_type_t24BLE_ADDR_TYPE_RPA_PUBLICE "永久链接至目标")
    :   when used with own addr, below means rpa effort, otherwise public when used with peer addr, below doesn’t used

    enumerator BLE_ADDR_TYPE_RPA_RANDOM[](#_CPPv4N18bk_ble_addr_type_t24BLE_ADDR_TYPE_RPA_RANDOME "永久链接至目标")
    :   when used with own addr, below means rpa effort, otherwise random when used with peer addr, below doesn’t used

enum bk_ble_wl_addr_type_t[](#_CPPv421bk_ble_wl_addr_type_t "永久链接至目标")
:   white list address type


    *Values:*

    enumerator BLE_WL_ADDR_TYPE_PUBLIC[](#_CPPv4N21bk_ble_wl_addr_type_t23BLE_WL_ADDR_TYPE_PUBLICE "永久链接至目标")

    enumerator BLE_WL_ADDR_TYPE_RANDOM[](#_CPPv4N21bk_ble_wl_addr_type_t23BLE_WL_ADDR_TYPE_RANDOME "永久链接至目标")


## Reference link[](#reference-link "永久链接至标题")

> [API Reference :](../../api-reference/bluetooth/index.md "../../api-reference/bluetooth/index.md") Introduced the Bluetooth API interface
