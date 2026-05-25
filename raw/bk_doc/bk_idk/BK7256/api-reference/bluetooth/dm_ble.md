# DM BLE APIs[](#dm-ble-apis "永久链接至标题")

[[English]](../../../../en/v1.5/api-reference/bluetooth/dm_ble.html "../../../../en/v1.5/api-reference/bluetooth/dm_ble.html")

重要

The DM BLE API v1.0 is the lastest stable DM BLE APIs. All new applications should use DM BLE API v1.0.


## DM BLE API Categories[](#dm-ble-api-categories "永久链接至标题")

Most of DM BLE APIs can be categoried as:

Interface specific DM BLE APIs:
:   - BLE common interface

    - BLE scan interface

    - BLE ADV interface

    - BLE connect interface


## Compitability and Extension[](#compitability-and-extension "永久链接至标题")

The DM BLE APIs are flexible, easy to be extended and backward compatible. For most of the BLE configurations, we put some reserved fields in the config struct for future extendence. The API users need to make sure the reserved fields are initialized to 0, otherwise the compatibility may be broken as more fields are added.


## Programing Principle[](#programing-principle "永久链接至标题")

重要

Here is some general principle for DM BLE API users:
:   - Always init the reserved fields of config stuct to 0

    - Use BK_ERR_CHECK to check the return value of the DM BLE API

    - If you are not sure how to use DM BLE APIs, study the BLE example code first

    - If you are not sure how to initialize some fields of config struct, use the default configuration macro to use the config first and then set application specific fields.

    - Don’t do too much work in BLE event callback, relay the event to your own application task.


## User Development Model[](#user-development-model "永久链接至标题")

Similar as most popular BLE driver, the Beken BLE driver is implemented as event driver. The application call DM BLE APIs to operate the BLE driver and get notified by BLE event.


## User Guide[](#user-guide "永久链接至标题")


- create att database


```
typedef struct
{
    uint16_t pri_service_handle;
    uint16_t chara_notify_handle;
    uint16_t chara_ssid_handle;
    uint16_t chara_pass_handle;
}boarding_env_s;

static boarding_env_s boarding_env;

void ble_do_reg_db(void)
{
    int retval = kNoErr;

    GATT_DB_SERVICE_INFO service_info;
    uint16_t num_attr_handles;
    uint16_t service_handle;
    GATT_DB_UUID_TYPE char_uuid;
    uint16_t perm;
    uint16_t property;
    ATT_VALUE char_value;
    UINT16 char_handle;

    bk_ble_set_notice_cb(ble_at_notice_cb);

    service_info.is_primary = 1;
    service_info.uuid.uuid_format = ATT_16_BIT_UUID_FORMAT;
    service_info.uuid.uuid.uuid_16 = GATT_BOARDING_SERVICE_UUID;
    service_info.link_req = GATT_DB_SER_SUPPORT_ANY_LINK_TYPE;
    service_info.sec_req = GATT_DB_SER_NO_SECURITY_PROPERTY;
    num_attr_handles = 30U;
    retval = bk_ble_gatt_db_add_service
               (
                   &service_info,
                   num_attr_handles,
                   &service_handle
               );

    if (0 != retval)
    {
        os_printf("%s: BT_gatt_db_add_service() failed. Result: 0x%04X\n", __func__, retval);
        goto error;
    }
    else
    {
        boarding_env.pri_service_handle = service_handle;
    }

    char_uuid.uuid_format = ATT_16_BIT_UUID_FORMAT;
    char_uuid.uuid.uuid_16 = GATT_BOARDING_NOTIFY_CHARACTERISTIC;
    perm = GATT_DB_PERM_READ;
    property = (GATT_DB_CHAR_READ_PROPERTY | GATT_DB_CHAR_NOTIFY_PROPERTY);
    char_value.val = s_boarding_notify;
    char_value.len = sizeof(s_boarding_notify);
    char_value.actual_len = char_value.len;
    retval = bk_ble_gatt_db_add_characteristic
                   (
                       service_handle,
                       &char_uuid,
                       perm,
                       property,
                       &char_value,
                       &char_handle
                   );
    if (0 != retval)
    {
        os_printf("%s: bk_ble_gatt_db_add_characteristic() failed. Result: 0x%04X\n", __func__, retval);
        goto error;
    }
    else
    {
        boarding_env.chara_notify_handle = char_handle;
    }

    GATT_DB_UUID_TYPE    desc_uuid;
    ATT_VALUE            desc_value;

    uint8_t cccd_value[2U]    = { 0x00U, 0x00U };

    desc_uuid.uuid_format  = ATT_16_BIT_UUID_FORMAT;
    desc_uuid.uuid.uuid_16 = GATT_CLIENT_CONFIG;

    perm                   = (GATT_DB_PERM_READ | GATT_DB_PERM_WRITE);

    desc_value.val         = cccd_value;
    desc_value.len         = 2U;
    desc_value.actual_len  = desc_value.len;

    /* Add descriptor CCCD */
    retval = bk_ble_gatt_db_add_characteristic_descriptor
             (
                 service_handle,
                 boarding_env.chara_notify_handle,
                 &desc_uuid,
                 perm,
                 &desc_value
             );
    if (0 != retval)
    {
        os_printf("%s: bk_ble_gatt_db_add_characteristic_descriptor() failed. Result: 0x%04X\n", __func__, retval);
        goto error;
    }

    char_uuid.uuid_format = ATT_16_BIT_UUID_FORMAT;
    char_uuid.uuid.uuid_16 = GATT_BOARDING_SSID_CHARACTERISTIC;
    perm = GATT_DB_PERM_READ | GATT_DB_PERM_WRITE;
    property = (GATT_DB_CHAR_READ_PROPERTY | GATT_DB_CHAR_WRITE_PROPERTY | GATT_DB_CHAR_WRITE_WITHOUT_RSP_PROPERTY);
    char_value.val = s_boarding_ssid;
    char_value.len = sizeof(s_boarding_ssid);
    char_value.actual_len = char_value.len;
    retval = bk_ble_gatt_db_add_characteristic
                   (
                       service_handle,
                       &char_uuid,
                       perm,
                       property,
                       &char_value,
                       &char_handle
                   );
    if (0 != retval)
    {
        os_printf("%s: bk_ble_gatt_db_add_characteristic() failed. Result: 0x%04X\n", __func__, retval);
        goto error;
    }
    else
    {
        boarding_env.chara_ssid_handle = char_handle;
    }

    char_uuid.uuid_format = ATT_16_BIT_UUID_FORMAT;
    char_uuid.uuid.uuid_16 = GATT_BOARDING_PASSWORD_CHARACTERISTIC;
    perm = GATT_DB_PERM_READ | GATT_DB_PERM_WRITE;
    property = (GATT_DB_CHAR_READ_PROPERTY | GATT_DB_CHAR_WRITE_PROPERTY | GATT_DB_CHAR_WRITE_WITHOUT_RSP_PROPERTY);
    char_value.val = s_boarding_password;
    char_value.len = sizeof(s_boarding_password);
    char_value.actual_len = char_value.len;
    retval = bk_ble_gatt_db_add_characteristic
                   (
                       service_handle,
                       &char_uuid,
                       perm,
                       property,
                       &char_value,
                       &char_handle
                   );
    if (0 != retval)
    {
        os_printf("%s: bk_ble_gatt_db_add_characteristic() failed. Result: 0x%04X\n", __func__, retval);
        goto error;
    }
    else
    {
        boarding_env.chara_pass_handle = char_handle;
    }

    retval = bk_ble_gatt_db_add_completed();

    if (retval != 0)
    {
        os_printf("%s GATT Database Registration err: 0x%04X\n", __func__, retval);
        goto error;
    }

    retval = bk_ble_gatt_db_set_callback(gatt_db_boarding_gatt_char_handler);

    if (retval != 0)
    {
        os_printf("%s bk_ble_gatt_db_set_callback err: 0x%04X\n", __func__, retval);
        goto error;
    }
}

static API_RESULT gatt_db_boarding_gatt_char_handler(GATT_DB_HANDLE    * handle, GATT_DB_PARAMS    * params)
{
    uint16_t config;

    if(handle->service_id == boarding_env.pri_service_handle)
    {
        switch (params->db_op)
        {
            case GATT_DB_CHAR_PEER_CLI_CNFG_WRITE_REQ:
            {
                if(handle->char_id == boarding_env.chara_notify_handle)
                {
                    config = (((uint16_t)(params->value.val[1]))<<8) | params->value.val[0];
                    if (GATT_CLI_CNFG_NOTIFICATION == config)
                    {
                        os_printf("client notify config open\r\n");
                    }
                    else if(GATT_CLI_CNFG_DEFAULT == config)
                    {
                        os_printf("client notify config close\r\n");
                    }
                    else
                    {
                        //nothing to do
                    }
                }
            }
            break;

            case GATT_DB_CHAR_PEER_READ_REQ:
            {
                if(handle->char_id == boarding_env.chara_pass_handle)
                {
                    ATT_VALUE param;
                    bk_ble_gatt_get_char_val(handle, &param);
                    os_printf("Borading read PASS:%s, %d \r\n",param.val, param.actual_len);
                }
                else if(handle->char_id == boarding_env.chara_ssid_handle)
                {
                    ATT_VALUE param;
                    bk_ble_gatt_get_char_val(handle, &param);
                    os_printf("Borading read SSID:%s, %d \r\n",param.val, param.actual_len);
                }
                else
                {
                    //nothing to do
                }
            }
            break;

            case GATT_DB_CHAR_PEER_WRITE_REQ:
            {
                if(handle->char_id == boarding_env.chara_pass_handle)
                {
                    s_boarding_password_len = 0;
                    os_memset((uint8_t *)s_boarding_password, 0, sizeof(s_boarding_password)/sizeof(s_boarding_password[0]));
                    os_memcpy((uint8_t *)s_boarding_password, params->value.val, params->value.len);
                    s_boarding_password_len = params->value.len;
                    os_printf("Boarding write PASS:%s, %d, %d\r\n",s_boarding_password, s_boarding_password_len, params->value.actual_len);
                    demo_sta_app_init((char *)s_boarding_ssid, (char *)s_boarding_password);
                }
                else if(handle->char_id == boarding_env.chara_ssid_handle)
                {
                    s_boarding_ssid_len = 0;
                    os_memset((uint8_t *)s_boarding_ssid, 0, sizeof(s_boarding_ssid)/sizeof(s_boarding_ssid[0]));
                    os_memcpy((uint8_t *)s_boarding_ssid, params->value.val, params->value.len);
                    s_boarding_ssid_len = params->value.len;
                    os_printf("Boarding write SSID:%s, %d, %d\r\n",s_boarding_ssid, s_boarding_ssid_len, params->value.actual_len);
                }
                else
                {
                    //nothing to do
                }
            }
            break;
            default:
                os_printf("No Specific Application Handling Required for Operation 0x%02X\n", params->db_op);
                break;
        }
    }

    return 0;
}

```


- start adv

::
:   int retval;
    ble_adv_parameter_t tmp_param;

    memset(&tmp_param, 0, sizeof(tmp_param));

    tmp_param.adv_intv_max = 160;
    tmp_param.adv_intv_min = 120;
    tmp_param.adv_type = ADV_LEGACY_TYPE_ADV_IND;
    tmp_param.chnl_map = ADV_ALL_CHNLS;
    tmp_param.filter_policy = ADV_FILTER_POLICY_ALLOW_SCAN_ANY_CONNECT_ANY;
    tmp_param.own_addr_type = 0;
    tmp_param.peer_addr_type = 0;

    const uint8_t adv_data[] = {0x02, 0x01, 0x06, 0x0f, 0x08, 0x53, 0x6d, 0x61, 0x72, 0x74, 0x2d, 0x44, 0x6f, 0x6f, 0x72, 0x62, 0x65, 0x6c, 0x6c};

    //wait for ble_at_cmd_cb
    retval = bk_ble_set_advertising_data(adv_len, adv_data, ble_at_cmd_cb);
    if (retval != BK_ERR_BLE_SUCCESS)
    {

    }

    retval = bk_ble_set_advertising_enable(1, ble_at_cmd_cb);
    //wait for ble_at_cmd_cb
    if (retval != BK_ERR_BLE_SUCCESS)
    {

    }


## API Reference[](#api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [dm_ble.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/dm_ble.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/dm_ble.h")


### Functions[](#functions "永久链接至标题")

void bk_ble_set_event_callback([ble_event_cb_t](#_CPPv414ble_event_cb_t "ble_event_cb_t") func)[](#_CPPv425bk_ble_set_event_callback14ble_event_cb_t "永久链接至目标")
:   Register dm_ble event notification callback.

    User example:


    **Attention**
    :   1. you must regist it, otherwise you cant get any event !

        2. you must regist it before bk_ble_create_db, otherwise you cant get BLE_5_CREATE_DB event

    参数
    :   **func, :** – event callback

    返回
    :   - void

[ble_err_t](ble.html#_CPPv49ble_err_t "ble_err_t") bk_ble_set_advertising_params([ble_adv_parameter_t](#_CPPv419ble_adv_parameter_t "ble_adv_parameter_t") *param, [ble_cmd_cb_t](ble.html#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)[](#_CPPv429bk_ble_set_advertising_paramsP19ble_adv_parameter_t12ble_cmd_cb_t "永久链接至目标")
:   Set adv param.


    **Attention**
    :   1.you must wait callback status, 0 mean success.

    参数
    :   - **param, :** – adv param see [ble_adv_parameter_t](#structble__adv__parameter__t "#structble__adv__parameter__t")

        - **callback, :** – register a callback for this action, ble_cmd_t: BLE_CREATE_ADV

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](ble.html#_CPPv49ble_err_t "ble_err_t") bk_ble_set_advertising_data(uint8_t adv_len, uint8_t *adv_buff, [ble_cmd_cb_t](ble.html#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)[](#_CPPv427bk_ble_set_advertising_data7uint8_tP7uint8_t12ble_cmd_cb_t "永久链接至目标")
:   Set adv data.


    **Attention**
    :   1.you must wait callback status, 0 mean success.

    参数
    :   - **adv_len, :** – adv data len

        - **adv_buff, :** – adv data

        - **callback, :** – register a callback for this action, ble_cmd_t: BLE_SET_ADV_DATA

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](ble.html#_CPPv49ble_err_t "ble_err_t") bk_ble_set_scan_response_data(uint8_t scan_response_data_length, uint8_t *scan_response_data, [ble_cmd_cb_t](ble.html#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)[](#_CPPv429bk_ble_set_scan_response_data7uint8_tP7uint8_t12ble_cmd_cb_t "永久链接至目标")
:   Set adv scan response data.


    **Attention**
    :   1.you must wait callback status, 0 mean success.

    参数
    :   - **scan_response_data_length, :** – data len

        - **scan_response_data, :** – data

        - **callback, :** – register a callback for this action, ble_cmd_t: BLE_SET_RSP_DATA

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](ble.html#_CPPv49ble_err_t "ble_err_t") bk_ble_set_advertising_enable(uint8_t enable, [ble_cmd_cb_t](ble.html#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)[](#_CPPv429bk_ble_set_advertising_enable7uint8_t12ble_cmd_cb_t "永久链接至目标")
:   Set enable/disable adv.


    **Attention**
    :   1.you must wait callback status, 0 mean success.

    参数
    :   - **enable, :** – enable or disable

        - **callback, :** – register a callback for this action, ble_cmd_t: BLE_START_ADV(enable) BLE_STOP_ADV(disable)

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](ble.html#_CPPv49ble_err_t "ble_err_t") bk_ble_disconnect_connection([bd_addr_t](ble.html#_CPPv49bd_addr_t "bd_addr_t") *addr, [ble_cmd_cb_t](ble.html#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)[](#_CPPv428bk_ble_disconnect_connectionP9bd_addr_t12ble_cmd_cb_t "永久链接至目标")
:   disconnect ble connection


    **Attention**
    :   1.you must wait callback status, 0 mean success.

    参数
    :   - **addr, :** – peer addr

        - **callback, :** – register a callback for this action, ble_cmd_t: BLE_CONN_DIS_CONN

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](ble.html#_CPPv49ble_err_t "ble_err_t") bk_ble_gatt_db_add_service([GATT_DB_SERVICE_INFO](#_CPPv420GATT_DB_SERVICE_INFO "GATT_DB_SERVICE_INFO") *service_info, uint16_t num_attr_handles, uint16_t *service_handle)[](#_CPPv426bk_ble_gatt_db_add_serviceP20GATT_DB_SERVICE_INFO8uint16_tP8uint16_t "永久链接至目标")
:   add a primary service in gatt db

    User example:

    ```
    GATT_DB_SERVICE_INFO service_info;
    uint16_t num_attr_handles;
    uint16_t service_handle;

    service_info.is_primary = 1;
    service_info.uuid.uuid_format = ATT_16_BIT_UUID_FORMAT;
    service_info.uuid.uuid.uuid_16 = GATT_BOARDING_SERVICE_UUID;
    service_info.link_req = GATT_DB_SER_SUPPORT_ANY_LINK_TYPE;
    service_info.sec_req = GATT_DB_SER_NO_SECURITY_PROPERTY;
    num_attr_handles = 30U;
    retval = bk_ble_gatt_db_add_service
               (
                   &service_info,
                   num_attr_handles,
                   &service_handle
               );
    ```


    **Attention**
    :   1.you must wait callback status, 0 mean success.

    参数
    :   - **service_info, :** – service info

        - **num_attr_handles, :** – how many attr in this service

        - **service_handle, :** – **[out]** out put a handle to user.

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](ble.html#_CPPv49ble_err_t "ble_err_t") bk_ble_gatt_db_add_characteristic(uint16_t service_handle, [GATT_DB_UUID_TYPE](#_CPPv417GATT_DB_UUID_TYPE "GATT_DB_UUID_TYPE") *char_uuid, uint16_t perm, uint16_t property, [ATT_VALUE](#_CPPv49ATT_VALUE "ATT_VALUE") *char_value, uint16_t *char_handle)[](#_CPPv433bk_ble_gatt_db_add_characteristic8uint16_tP17GATT_DB_UUID_TYPE8uint16_t8uint16_tP9ATT_VALUEP8uint16_t "永久链接至目标")
:   add a characteristic in a gatt service

    User example:

    ```
    GATT_DB_UUID_TYPE char_uuid;
    uint16_t perm;
    uint16_t property;
    ATT_VALUE char_value;
    UINT16 char_handle;

    char_uuid.uuid_format = ATT_16_BIT_UUID_FORMAT;
    char_uuid.uuid.uuid_16 = GATT_BOARDING_NOTIFY_CHARACTERISTIC;
    perm = GATT_DB_PERM_READ;
    property = (GATT_DB_CHAR_READ_PROPERTY | GATT_DB_CHAR_NOTIFY_PROPERTY);
    char_value.val = s_boarding_notify;
    char_value.len = sizeof(s_boarding_notify);
    char_value.actual_len = char_value.len;
    retval = bk_ble_gatt_db_add_characteristic
                   (
                       service_handle,
                       &char_uuid,
                       perm,
                       property,
                       &char_value,
                       &char_handle
                   );
    ```


    **Attention**
    :   1.you must wait callback status, 0 mean success.

    参数
    :   - **service_handle, :** – service handle, get from bk_ble_gatt_db_add_service

        - **char_uuid, :** – characteristic’s uuid, in ATT_UUID16 or [ATT_UUID128](#structATT__UUID128 "#structATT__UUID128"), see [GATT_DB_UUID_TYPE](#structGATT__DB__UUID__TYPE "#structGATT__DB__UUID__TYPE")

        - **perm, :** – permission, such as GATT_DB_PERM_READ GATT_DB_PERM_WRITE

        - **property, :** – property, such as [GATT_DB_CHAR_READ_PROPERTY](#group__gatt__characteristic__properties_1ggab04a0655cd1e3bcac5e8f48c18df1a57a90ebdf42e3bda749182f0229c30c3495 "#group__gatt__characteristic__properties_1ggab04a0655cd1e3bcac5e8f48c18df1a57a90ebdf42e3bda749182f0229c30c3495") [GATT_DB_CHAR_NOTIFY_PROPERTY](#group__gatt__characteristic__properties_1ggab04a0655cd1e3bcac5e8f48c18df1a57a4c0b4fe5642fc1602ed91532da1492bb "#group__gatt__characteristic__properties_1ggab04a0655cd1e3bcac5e8f48c18df1a57a4c0b4fe5642fc1602ed91532da1492bb")

        - **char_value, :** – att data, see [ATT_VALUE](#structATT__VALUE "#structATT__VALUE")

        - **char_handle, :** – **[out]** output a handle

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](ble.html#_CPPv49ble_err_t "ble_err_t") bk_ble_gatt_db_add_characteristic_descriptor(uint16_t service_handle, uint16_t char_handle, [GATT_DB_UUID_TYPE](#_CPPv417GATT_DB_UUID_TYPE "GATT_DB_UUID_TYPE") *desc_uuid, uint16_t perm, [ATT_VALUE](#_CPPv49ATT_VALUE "ATT_VALUE") *desc_value)[](#_CPPv444bk_ble_gatt_db_add_characteristic_descriptor8uint16_t8uint16_tP17GATT_DB_UUID_TYPE8uint16_tP9ATT_VALUE "永久链接至目标")
:   add a characteristic descriptor in a characteristic

    User example:

    ```
    GATT_DB_UUID_TYPE    desc_uuid;
    ATT_VALUE            desc_value;

    uint8_t cccd_value[2U]    = { 0x00U, 0x00U };

    desc_uuid.uuid_format  = ATT_16_BIT_UUID_FORMAT;
    desc_uuid.uuid.uuid_16 = GATT_CLIENT_CONFIG;

    perm                   = (GATT_DB_PERM_READ | GATT_DB_PERM_WRITE);

    desc_value.val         = cccd_value;
    desc_value.len         = 2U;
    desc_value.actual_len  = desc_value.len;

    // Add descriptor CCCD
    retval = bk_ble_gatt_db_add_characteristic_descriptor
             (
                 service_handle,
                 boarding_env.chara_notify_handle,
                 &desc_uuid,
                 perm,
                 &desc_value
             );
    ```


    **Attention**
    :   1.you must wait callback status, 0 mean success.

    参数
    :   - **service_handle, :** – service handle, get from bk_ble_gatt_db_add_service

        - **char_handle, :** – get from bk_ble_gatt_db_add_characteristic

        - **desc_uuid, :** – characteristic’s uuid, in ATT_UUID16 or [ATT_UUID128](#structATT__UUID128 "#structATT__UUID128"), see [GATT_DB_UUID_TYPE](#structGATT__DB__UUID__TYPE "#structGATT__DB__UUID__TYPE")

        - **perm, :** – permission, such as GATT_DB_PERM_READ GATT_DB_PERM_WRITE

        - **desc_value, :** – att data, see [ATT_VALUE](#structATT__VALUE "#structATT__VALUE")

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](ble.html#_CPPv49ble_err_t "ble_err_t") bk_ble_gatt_db_add_completed(void)[](#_CPPv428bk_ble_gatt_db_add_completedv "永久链接至目标")
:   call when gatt db add completed


    **Attention**
    :   1.you must wait callback status, 0 mean success.

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](ble.html#_CPPv49ble_err_t "ble_err_t") bk_ble_gatt_db_set_callback([ble_gatt_db_callback_t](#_CPPv422ble_gatt_db_callback_t "ble_gatt_db_callback_t") hndlr_cb)[](#_CPPv427bk_ble_gatt_db_set_callback22ble_gatt_db_callback_t "永久链接至目标")
:   set callback, when recv write read req


    **Attention**
    :   1.you must wait callback status, 0 mean success.

    参数
    :   **hndlr_cb, :** – callback, see ble_gatt_db_callback_t

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](ble.html#_CPPv49ble_err_t "ble_err_t") bk_ble_gatt_read_resp(uint8_t conn_handle, uint8_t *value, uint16_t length)[](#_CPPv421bk_ble_gatt_read_resp7uint8_tP7uint8_t8uint16_t "永久链接至目标")
:   When recv GATT_DB_CHAR_PEER_READ_REQ, async response.


    **Attention**
    :   1.you must wait callback status, 0 mean success.

    参数
    :   - **conn_handle, :** – connection handle

        - **value, :** – a point to buffer

        - **length, :** – buffer len

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](ble.html#_CPPv49ble_err_t "ble_err_t") bk_ble_send_notify(uint8_t conn_handle, uint16_t service_handle, uint16_t char_handle, uint8_t *data, uint16_t len)[](#_CPPv418bk_ble_send_notify7uint8_t8uint16_t8uint16_tP7uint8_t8uint16_t "永久链接至目标")
:   send notify when recv enable notify


    **Attention**
    :   1.you must wait callback status, 0 mean success.

    参数
    :   - **conn_handle, :** – connection handle

        - **adv** – service_handle: from bk_ble_gatt_db_add_service

        - **char_handle, :** – get from bk_ble_gatt_db_add_characteristic

        - **data, :** – a point to buffer

        - **len, :** – buffer len

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](ble.html#_CPPv49ble_err_t "ble_err_t") bk_ble_gatt_get_char_val([GATT_DB_HANDLE](#_CPPv414GATT_DB_HANDLE "GATT_DB_HANDLE") *handle, [ATT_VALUE](#_CPPv49ATT_VALUE "ATT_VALUE") *attr_value)[](#_CPPv424bk_ble_gatt_get_char_valP14GATT_DB_HANDLEP9ATT_VALUE "永久链接至目标")
:   get db value


    **Attention**
    :   1.you must wait callback status, 0 mean success.

    参数
    :   - **handle, :** – handle

        - **attr_value, :** – attr

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](ble.html#_CPPv49ble_err_t "ble_err_t") bk_ble_set_random_addr([bd_addr_t](ble.html#_CPPv49bd_addr_t "bd_addr_t") *addr, [ble_cmd_cb_t](ble.html#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)[](#_CPPv422bk_ble_set_random_addrP9bd_addr_t12ble_cmd_cb_t "永久链接至目标")
:   set random addr


    **Attention**
    :   1.you must wait callback status, 0 mean success.

        2.this api must call after bk_ble_set_advertising_params now !

    参数
    :   - **addr, :** – addr

        - **callback, :** – register a callback for this action, ble_cmd_t: BLE_SET_RANDOM_ADDR

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](ble.html#_CPPv49ble_err_t "ble_err_t") bk_ble_update_connection_params([ble_update_conn_param_t](#_CPPv423ble_update_conn_param_t "ble_update_conn_param_t") *conn_param)[](#_CPPv431bk_ble_update_connection_paramsP23ble_update_conn_param_t "永久链接至目标")
:   update connection param, result as BK_DM_BLE_EVENT_CONN_UPDATA


    **Attention**
    :   1.you must wait callback status, 0 mean success.

        2.you don’t need to wait BK_DM_BLE_EVENT_CONN_UPDATA because it is an aysnc procedure.

    参数
    :   **conn_param, :** – [ble_update_conn_param_t](#structble__update__conn__param__t "#structble__update__conn__param__t")

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.


## API Typedefs[](#api-typedefs "永久链接至标题")


### Header File[](#id1 "永久链接至标题")


- [dm_ble_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/dm_ble_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/dm_ble_types.h")


### Unions[](#unions "永久链接至标题")

union ATT_UUID[](#_CPPv48ATT_UUID "永久链接至目标")
:   *#include <dm_ble_types.h>*

    att uuid struct

    Public Members

    [ATT_UUID16](#_CPPv410ATT_UUID16 "ATT_UUID16") uuid_16[](#_CPPv4N8ATT_UUID7uuid_16E "永久链接至目标")

    [ATT_UUID128](#_CPPv411ATT_UUID128 "ATT_UUID128") uuid_128[](#_CPPv4N8ATT_UUID8uuid_128E "永久链接至目标")


### Structures[](#structures "永久链接至标题")

struct ATT_UUID128[](#_CPPv411ATT_UUID128 "永久链接至目标")
:   Abstracts 128 Bit UUID.

struct ATT_VALUE[](#_CPPv49ATT_VALUE "永久链接至目标")
:   att value struct

    Public Members

    uint8_t *val[](#_CPPv4N9ATT_VALUE3valE "永久链接至目标")
    :   Value to be packed

    uint16_t len[](#_CPPv4N9ATT_VALUE3lenE "永久链接至目标")
    :   Length of Value

    uint16_t actual_len[](#_CPPv4N9ATT_VALUE10actual_lenE "永久链接至目标")
    :   Out Parameter Indicating Actual Length Packed

struct ATT_HANDLE_VALUE_PAIR[](#_CPPv421ATT_HANDLE_VALUE_PAIR "永久链接至目标")
:   Abstracts Handle Value Pair This is used in multiple PDUs - see ATT_WRITE_REQ_PARAM, ATT_WRITE_CMD_PARAM etc.

    Public Members

    [ATT_VALUE](#_CPPv49ATT_VALUE "ATT_VALUE") value[](#_CPPv4N21ATT_HANDLE_VALUE_PAIR5valueE "永久链接至目标")
    :   Attribute Value

    [ATT_ATTR_HANDLE](#_CPPv415ATT_ATTR_HANDLE "ATT_ATTR_HANDLE") handle[](#_CPPv4N21ATT_HANDLE_VALUE_PAIR6handleE "永久链接至目标")
    :   Attribute Handle

struct ATT_HANDLE[](#_CPPv410ATT_HANDLE "永久链接至目标")
:   ATT Handle.

    Public Members

    [DEVICE_HANDLE](#_CPPv413DEVICE_HANDLE "DEVICE_HANDLE") device_id[](#_CPPv4N10ATT_HANDLE9device_idE "永久链接至目标")
    :   Identifies the peer instance

    [ATT_CON_ID](#_CPPv410ATT_CON_ID "ATT_CON_ID") att_id[](#_CPPv4N10ATT_HANDLE6att_idE "永久链接至目标")
    :   Identifies the ATT Instance

struct ATT_HANDLE_RANGE[](#_CPPv416ATT_HANDLE_RANGE "永久链接至目标")
:   ATT range.

    Public Members

    [ATT_ATTR_HANDLE](#_CPPv415ATT_ATTR_HANDLE "ATT_ATTR_HANDLE") start_handle[](#_CPPv4N16ATT_HANDLE_RANGE12start_handleE "永久链接至目标")
    :   Start Handle

    [ATT_ATTR_HANDLE](#_CPPv415ATT_ATTR_HANDLE "ATT_ATTR_HANDLE") end_handle[](#_CPPv4N16ATT_HANDLE_RANGE10end_handleE "永久链接至目标")
    :   End Handle

struct GATT_DB_UUID_TYPE[](#_CPPv417GATT_DB_UUID_TYPE "永久链接至目标")
:   gatt db uuid type

    Public Members

    uint8_t uuid_format[](#_CPPv4N17GATT_DB_UUID_TYPE11uuid_formatE "永久链接至目标")
    :   Format indicating, 16 bit or 128 bit UUIDs, see ATT_16_BIT_UUID_FORMAT ATT_128_BIT_UUID_FORMAT.

    [ATT_UUID](#_CPPv48ATT_UUID "ATT_UUID") uuid[](#_CPPv4N17GATT_DB_UUID_TYPE4uuidE "永久链接至目标")
    :   Attribute UUID.

struct GATT_DB_SERVICE_INFO[](#_CPPv420GATT_DB_SERVICE_INFO "永久链接至目标")
:   used in [bk_ble_gatt_db_add_service](#group__bk__dm__ble__api__v1_1gae22cd028b7b7b834f0136a4b7fac339e "#group__bk__dm__ble__api__v1_1gae22cd028b7b7b834f0136a4b7fac339e")

    Public Members

    [GATT_DB_UUID_TYPE](#_CPPv417GATT_DB_UUID_TYPE "GATT_DB_UUID_TYPE") uuid[](#_CPPv4N20GATT_DB_SERVICE_INFO4uuidE "永久链接至目标")
    :   UUID, see [GATT_DB_UUID_TYPE](#structGATT__DB__UUID__TYPE "#structGATT__DB__UUID__TYPE")

    uint8_t is_primary[](#_CPPv4N20GATT_DB_SERVICE_INFO10is_primaryE "永久链接至目标")
    :   If this service is primary or not

    [GATT_DB_SERVICE_DESC](#_CPPv420GATT_DB_SERVICE_DESC "GATT_DB_SERVICE_DESC") sec_req[](#_CPPv4N20GATT_DB_SERVICE_INFO7sec_reqE "永久链接至目标")
    :   Security Requrirements for the Service Logical OR of desired combinations of

        1. Security Mode
        2. Security Level
        3. Encryption Key Size

        Acceptable values for Security Mode are: [GATT_DB_SER_SECURITY_MODE1](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da74841772cdaba7022c4c0350846e928c "#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da74841772cdaba7022c4c0350846e928c") [GATT_DB_SER_SECURITY_MODE2](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da7459a951c37cece87b3bf40773884978 "#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da7459a951c37cece87b3bf40773884978")

        Acceptable values for Security Level are: [GATT_DB_SER_SECURITY_LEVEL1](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da97297f1172c56e0335ada7ec9a95523f "#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da97297f1172c56e0335ada7ec9a95523f") [GATT_DB_SER_SECURITY_LEVEL2](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035daeee0be171bf53f0b5e9394163254b85c "#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035daeee0be171bf53f0b5e9394163254b85c") [GATT_DB_SER_SECURITY_LEVEL3](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da43c32dae35af6c45c3e6e3a9b7b8697a "#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da43c32dae35af6c45c3e6e3a9b7b8697a")

        Acceptable values for Encryption Key Size are: [GATT_DB_SER_ENCRYPT_KEY_SIZE_7](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035daf26237278d04eb8e0f0b6d458e4101a8 "#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035daf26237278d04eb8e0f0b6d458e4101a8") [GATT_DB_SER_ENCRYPT_KEY_SIZE_8](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da578f242314247aabe4766585b213935d "#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da578f242314247aabe4766585b213935d") [GATT_DB_SER_ENCRYPT_KEY_SIZE_9](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da0b721e086f412de7f0b881434193421f "#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da0b721e086f412de7f0b881434193421f") [GATT_DB_SER_ENCRYPT_KEY_SIZE_10](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da0af0e5686c4872b497be8568ec7c8ad7 "#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da0af0e5686c4872b497be8568ec7c8ad7") [GATT_DB_SER_ENCRYPT_KEY_SIZE_11](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da22ae7f4b2be7c145dd54d8f58720041f "#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da22ae7f4b2be7c145dd54d8f58720041f") [GATT_DB_SER_ENCRYPT_KEY_SIZE_12](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da62c6ca9b86cda66475dc31c721f31ee5 "#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da62c6ca9b86cda66475dc31c721f31ee5") [GATT_DB_SER_ENCRYPT_KEY_SIZE_13](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035dada15fde570ee125f1e273c0e15416ac0 "#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035dada15fde570ee125f1e273c0e15416ac0") [GATT_DB_SER_ENCRYPT_KEY_SIZE_14](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035daae41a9c45197bf1897c25206b7833552 "#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035daae41a9c45197bf1897c25206b7833552") [GATT_DB_SER_ENCRYPT_KEY_SIZE_15](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da0f7f2aac54861fbefd0054f3ac911fa2 "#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da0f7f2aac54861fbefd0054f3ac911fa2") [GATT_DB_SER_ENCRYPT_KEY_SIZE_16](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da15388d866bc04cfba206ce44726d6e0e "#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da15388d866bc04cfba206ce44726d6e0e") When the Service does not mandate any specific Key size [GATT_DB_SER_ENC_KEY_SIZE_DONT_CARE](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da9d8f85a9e69bab3d04f0c9c035bc20df "#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da9d8f85a9e69bab3d04f0c9c035bc20df") shall be used.

        When No Security is mandated for the service Value [GATT_DB_SER_NO_SECURITY_PROPERTY](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035dab307287b35dec27c88ec7030aca6fb84 "#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035dab307287b35dec27c88ec7030aca6fb84") shall be used.

    [GATT_DB_SERVICE_DESC](#_CPPv420GATT_DB_SERVICE_DESC "GATT_DB_SERVICE_DESC") link_req[](#_CPPv4N20GATT_DB_SERVICE_INFO8link_reqE "永久链接至目标")
    :   Transport Requrirements for the Service. This describes the Transport on which this required to be operational. GATT_DB_SER_SUPPORT_ANY_LINK_TYPE GATT_DB_SER_SUPPORT_LE_LINK_TYPE GATT_DB_SER_SUPPORT_BR_LINK_TYPE

struct GATT_DB_HANDLE[](#_CPPv414GATT_DB_HANDLE "永久链接至目标")
:   GATT db handle.

    Public Members

    [DEVICE_HANDLE](#_CPPv413DEVICE_HANDLE "DEVICE_HANDLE") device_id[](#_CPPv4N14GATT_DB_HANDLE9device_idE "永久链接至目标")
    :   Identifies the peer accessing the database

    uint8_t service_id[](#_CPPv4N14GATT_DB_HANDLE10service_idE "永久链接至目标")
    :   Identifies the Service being Accessed

    uint8_t char_id[](#_CPPv4N14GATT_DB_HANDLE7char_idE "永久链接至目标")
    :   Identifies the Characteristic being Accessed

struct GATT_DB_PARAMS[](#_CPPv414GATT_DB_PARAMS "永久链接至目标")
:   GATT db param.

    Public Members

    [ATT_VALUE](#_CPPv49ATT_VALUE "ATT_VALUE") value[](#_CPPv4N14GATT_DB_PARAMS5valueE "永久链接至目标")
    :   Abstracts Value to get/set the Attribute Value

    [ATT_ATTR_HANDLE](#_CPPv415ATT_ATTR_HANDLE "ATT_ATTR_HANDLE") handle[](#_CPPv4N14GATT_DB_PARAMS6handleE "永久链接至目标")
    :   Abstracts the handle information

    [GATT_DB_OPERATION](#_CPPv417GATT_DB_OPERATION "GATT_DB_OPERATION") db_op[](#_CPPv4N14GATT_DB_PARAMS5db_opE "永久链接至目标")
    :   Abstracts the Access Operation, such as [GATT_DB_CHAR_PEER_READ_REQ](#group__gatt__db__operations_1ggabed82baf7f470b522273a3e37c24c600a61a516866cd39e8f02f29096ae3f191a "#group__gatt__db__operations_1ggabed82baf7f470b522273a3e37c24c600a61a516866cd39e8f02f29096ae3f191a")


        **Attention**
        :   when recv GATT_DB_CHAR_PEER_READ_REQ and you dont want response immediately, return GATT_DB_DELAYED_RESPONSE in ble_gatt_db_callback_t

struct GATT_SERVICE_PARAM[](#_CPPv418GATT_SERVICE_PARAM "永久链接至目标")
:   gatt Service param

    Public Members

    [ATT_UUID](#_CPPv48ATT_UUID "ATT_UUID") uuid[](#_CPPv4N18GATT_SERVICE_PARAM4uuidE "永久链接至目标")
    :   Service UUID

    uint8_t uuid_type[](#_CPPv4N18GATT_SERVICE_PARAM9uuid_typeE "永久链接至目标")
    :   Service UUID Type

    [ATT_HANDLE_RANGE](#_CPPv416ATT_HANDLE_RANGE "ATT_HANDLE_RANGE") range[](#_CPPv4N18GATT_SERVICE_PARAM5rangeE "永久链接至目标")
    :   Service Range

struct GATT_CHAR_DESC_PARAM[](#_CPPv420GATT_CHAR_DESC_PARAM "永久链接至目标")
:   gatt Characteristic Descriptor Information

    Public Members

    [ATT_ATTR_HANDLE](#_CPPv415ATT_ATTR_HANDLE "ATT_ATTR_HANDLE") handle[](#_CPPv4N20GATT_CHAR_DESC_PARAM6handleE "永久链接至目标")
    :   Descriptor handle

    [ATT_UUID](#_CPPv48ATT_UUID "ATT_UUID") uuid[](#_CPPv4N20GATT_CHAR_DESC_PARAM4uuidE "永久链接至目标")
    :   Descriptor UUID

    uint8_t uuid_type[](#_CPPv4N20GATT_CHAR_DESC_PARAM9uuid_typeE "永久链接至目标")
    :   Descriptor UUID Type

struct GATT_CHARACTERISTIC_PARAM[](#_CPPv425GATT_CHARACTERISTIC_PARAM "永久链接至目标")
:   gatt Characteristic Information

    Public Members

    [ATT_HANDLE_RANGE](#_CPPv416ATT_HANDLE_RANGE "ATT_HANDLE_RANGE") range[](#_CPPv4N25GATT_CHARACTERISTIC_PARAM5rangeE "永久链接至目标")
    :   Characteristic Range

    uint8_t cproperty[](#_CPPv4N25GATT_CHARACTERISTIC_PARAM9cpropertyE "永久链接至目标")
    :   Characteristic Property

    [ATT_ATTR_HANDLE](#_CPPv415ATT_ATTR_HANDLE "ATT_ATTR_HANDLE") value_handle[](#_CPPv4N25GATT_CHARACTERISTIC_PARAM12value_handleE "永久链接至目标")
    :   Characteristic Value Handle

    [ATT_UUID](#_CPPv48ATT_UUID "ATT_UUID") uuid[](#_CPPv4N25GATT_CHARACTERISTIC_PARAM4uuidE "永久链接至目标")
    :   Characteristic UUID

    uint8_t uuid_type[](#_CPPv4N25GATT_CHARACTERISTIC_PARAM9uuid_typeE "永久链接至目标")
    :   Characteristic UUID Type

    uint8_t desc_index[](#_CPPv4N25GATT_CHARACTERISTIC_PARAM10desc_indexE "永久链接至目标")
    :   ATT_128_BIT_UUID_FORMAT Characteristic desciptor index

    uint16_t val_offset[](#_CPPv4N25GATT_CHARACTERISTIC_PARAM10val_offsetE "永久链接至目标")
    :   Characteristics Value Offset

    uint16_t val_length[](#_CPPv4N25GATT_CHARACTERISTIC_PARAM10val_lengthE "永久链接至目标")
    :   Characteristic Value Length

    [GATT_CHAR_DESC_PARAM](#_CPPv420GATT_CHAR_DESC_PARAM "GATT_CHAR_DESC_PARAM") descriptor[GATT_MAX_CHAR_DESCRIPTORS][](#_CPPv4N25GATT_CHARACTERISTIC_PARAM10descriptorE "永久链接至目标")
    :   Characteristic descriptor array

struct ble_adv_parameter_t[](#_CPPv419ble_adv_parameter_t "永久链接至目标")
:   use in [bk_ble_set_advertising_params](#group__bk__dm__ble__api__v1_1gac82851a90130a907f6a3f58863aae7d5 "#group__bk__dm__ble__api__v1_1gac82851a90130a907f6a3f58863aae7d5")

    Public Members

    uint32_t adv_intv_min[](#_CPPv4N19ble_adv_parameter_t12adv_intv_minE "永久链接至目标")
    :   Minimum advertising interval (in unit of 625us). Must be greater than or equal to 20ms.

    uint32_t adv_intv_max[](#_CPPv4N19ble_adv_parameter_t12adv_intv_maxE "永久链接至目标")
    :   Maximum advertising interval (in unit of 625us). Must be greater than or equal to 20ms.

    uint8_t adv_type[](#_CPPv4N19ble_adv_parameter_t8adv_typeE "永久链接至目标")
    :   Advertising type, see advertise_legacy_type.

    uint8_t own_addr_type[](#_CPPv4N19ble_adv_parameter_t13own_addr_typeE "永久链接至目标")
    :   Own address type: public=0 / random=1 / rpa_or_pub=2 / rpa_or_rnd=3.

    [bd_addr_t](ble.html#_CPPv49bd_addr_t "bd_addr_t") peer_address[](#_CPPv4N19ble_adv_parameter_t12peer_addressE "永久链接至目标")
    :   Peer address.

    uint8_t peer_addr_type[](#_CPPv4N19ble_adv_parameter_t14peer_addr_typeE "永久链接至目标")
    :   Peer address type: public or public identity addr =0 / RDP or random Identity Addr =1.

    uint8_t chnl_map[](#_CPPv4N19ble_adv_parameter_t8chnl_mapE "永久链接至目标")
    :   Bit field indicating the channel mapping (.

        参见

        enum [adv_chnl_map](ble.html#group__bk__ble__api__v1__typedef_1ga57c9e3ee8efb2e8c2fcc35e570f8679a "ble.html#group__bk__ble__api__v1__typedef_1ga57c9e3ee8efb2e8c2fcc35e570f8679a"))

    uint16_t filter_policy[](#_CPPv4N19ble_adv_parameter_t13filter_policyE "永久链接至目标")
    :   advertising policy see advertise_filter_policy

struct ble_conn_att_t[](#_CPPv414ble_conn_att_t "永久链接至目标")
:   use in BK_DM_BLE_EVENT_CONNECT BK_DM_BLE_EVENT_DISCONNECT

    Public Members

    uint8_t peer_addr_type[](#_CPPv4N14ble_conn_att_t14peer_addr_typeE "永久链接至目标")
    :   Peer address type.

    uint8_t peer_addr[6][](#_CPPv4N14ble_conn_att_t9peer_addrE "永久链接至目标")
    :   Peer BT address.

struct ble_att_tx_compl_t[](#_CPPv418ble_att_tx_compl_t "永久链接至目标")
:   use in BK_DM_BLE_EVENT_TX_DONE

struct ble_att_notify_t[](#_CPPv416ble_att_notify_t "永久链接至目标")
:   use in BK_DM_BLE_EVENT_RECV_NOTIFY

struct ble_conn_update_param_ind_t[](#_CPPv427ble_conn_update_param_ind_t "永久链接至目标")
:   use in BK_DM_BLE_EVENT_CONN_UPD_PAR_ASK

struct ble_conn_update_param_compl_ind_t[](#_CPPv433ble_conn_update_param_compl_ind_t "永久链接至目标")
:   use in BK_DM_BLE_EVENT_CONN_UPDATA

struct ble_update_conn_param_t[](#_CPPv423ble_update_conn_param_t "永久链接至目标")
:   use when we need to trigger an update

struct ble_att_rw_t[](#_CPPv412ble_att_rw_t "永久链接至目标")
:   use in BK_DM_BLE_EVENT_ATT_READ_RESPONSE


### Macros[](#macros "永久链接至标题")

_H_GATT_DEFINES_[](#c._H_GATT_DEFINES_ "永久链接至目标")

ATT_APPL_PROCEDURE_ALREADY_IN_PROGRESS[](#c.ATT_APPL_PROCEDURE_ALREADY_IN_PROGRESS "永久链接至目标")

ATT_APPL_CCD_IMPROPERLY_CONFIGURED[](#c.ATT_APPL_CCD_IMPROPERLY_CONFIGURED "永久链接至目标")

_H_BT_ERROR_[](#c._H_BT_ERROR_ "永久链接至目标")
:   *H_GATT_DEFINES*

GATT_DB_ERR_ID[](#c.GATT_DB_ERR_ID "永久链接至目标")

GATT_DB_DELAYED_RESPONSE[](#c.GATT_DB_DELAYED_RESPONSE "永久链接至目标")
:   Not an error code. More of a status code

GATT_DB_DONOT_RESPOND[](#c.GATT_DB_DONOT_RESPOND "永久链接至目标")

GATT_DB_ALREADY_RESPONDED[](#c.GATT_DB_ALREADY_RESPONDED "永久链接至目标")

_H_BT_DEVICE_QUEUE_[](#c._H_BT_DEVICE_QUEUE_ "永久链接至目标")

_H_BT_ATT_API_[](#c._H_BT_ATT_API_ "永久链接至目标")

ATT_AUTH_SIGNATURE_SIZE[](#c.ATT_AUTH_SIGNATURE_SIZE "永久链接至目标")
:   ATT Default MTU ATT Signature Size in Signed Write

ATT_EXECUTE_WRITE_CANCEL_FLAG[](#c.ATT_EXECUTE_WRITE_CANCEL_FLAG "永久链接至目标")
:   ATT Execute Write Cancel Flag

ATT_EXECUTE_WRITE_EXEC_FLAG[](#c.ATT_EXECUTE_WRITE_EXEC_FLAG "永久链接至目标")
:   ATT Execute Write Execute Flag

ATT_16_BIT_UUID_FORMAT[](#c.ATT_16_BIT_UUID_FORMAT "永久链接至目标")
:   ATT Identification for 16-bit UUID Format

ATT_128_BIT_UUID_FORMAT[](#c.ATT_128_BIT_UUID_FORMAT "永久链接至目标")
:   ATT Identification for 128-bit UUID Format

ATT_16_BIT_UUID_SIZE[](#c.ATT_16_BIT_UUID_SIZE "永久链接至目标")
:   ATT 16-bit UUID Size

ATT_128_BIT_UUID_SIZE[](#c.ATT_128_BIT_UUID_SIZE "永久链接至目标")
:   ATT 128-bit UUID Size

ATT_CON_ID_INIT_VAL[](#c.ATT_CON_ID_INIT_VAL "永久链接至目标")
:   ATT Connection Instance Initialization Value.

ATT_APPL_CB_INIT_VAL[](#c.ATT_APPL_CB_INIT_VAL "永久链接至目标")
:   ATT Application Callback Initialization Value.

ATT_INVALID_ATTR_HANDLE_VAL[](#c.ATT_INVALID_ATTR_HANDLE_VAL "永久链接至目标")
:   ATT Invalid Attribute Handle Value

ATT_ATTR_HANDLE_START_RANGE[](#c.ATT_ATTR_HANDLE_START_RANGE "永久链接至目标")
:   ATT Attribute Handle Start Range

ATT_ATTR_HANDLE_END_RANGE[](#c.ATT_ATTR_HANDLE_END_RANGE "永久链接至目标")
:   ATT Attribute Handle End Range

_H_BT_GATT_DB_API_[](#c._H_BT_GATT_DB_API_ "永久链接至目标")

_H_GATT_[](#c._H_GATT_ "永久链接至目标")

GATT_MAX_CHAR_DESCRIPTORS[](#c.GATT_MAX_CHAR_DESCRIPTORS "永久链接至目标")


### Type Definitions[](#type-definitions "永久链接至标题")

typedef uint16_t API_RESULT[](#_CPPv410API_RESULT "永久链接至目标")

typedef uint8_t DEVICE_HANDLE[](#_CPPv413DEVICE_HANDLE "永久链接至目标")

typedef uint8_t ATT_CON_ID[](#_CPPv410ATT_CON_ID "永久链接至目标")

typedef uint16_t ATT_ATTR_HANDLE[](#_CPPv415ATT_ATTR_HANDLE "永久链接至目标")
:   ble att protocol handle

typedef uint16_t ATT_UUID16[](#_CPPv410ATT_UUID16 "永久链接至目标")
:   Abstracts 16 Bit UUID

typedef uint8_t GATT_DB_OPERATION[](#_CPPv417GATT_DB_OPERATION "永久链接至目标")
:   such as GATT_DB_CHAR_VALUE_READ_REQ

typedef uint32_t GATT_DB_SERVICE_DESC[](#_CPPv420GATT_DB_SERVICE_DESC "永久链接至目标")
:   such as [GATT_DB_SER_NO_SECURITY_PROPERTY](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035dab307287b35dec27c88ec7030aca6fb84 "#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035dab307287b35dec27c88ec7030aca6fb84") GATT_DB_SER_SUPPORT_ANY_LINK_TYPE

typedef [bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") (*ble_gatt_db_callback_t)(uint8_t conn_handle, [GATT_DB_HANDLE](#_CPPv414GATT_DB_HANDLE "GATT_DB_HANDLE") *handle, [GATT_DB_PARAMS](#_CPPv414GATT_DB_PARAMS "GATT_DB_PARAMS") *param)[](#_CPPv422ble_gatt_db_callback_t "永久链接至目标")
:   GATT DB callback extension, GATT DB Handler Callback. The GATT DB PL extension calls the registered callback to indicate any ongoing GATT DB Operation. The Upper Layer can implement specific handling for any Characterisitc or Characteritistic Descriptor depending on its requirement.

    Param conn_handle
    :   **[in]** connection handle, see BK_DM_BLE_EVENT_CONNECT

    Param handle
    :   **[in]** Pointer to GATT DB identifier [GATT_DB_HANDLE](#structGATT__DB__HANDLE "#structGATT__DB__HANDLE")

    Param param
    :   **[in]** Pointer to GATT DB Parameters [GATT_DB_PARAMS](#structGATT__DB__PARAMS "#structGATT__DB__PARAMS")

    Return
    :   API_SUCCESS if ATT/GATT response for the incoming request to be sent from the below layer GATT_DB_DELAYED_RESPONSE if ATT/GATT response will be sent at a later point by the application GATT_DB_DONOT_RESPOND if ATT/GATT response will be sent at a later point by the application GATT_DB_ALREADY_RESPONDED if ATT/GATT response is already sent the application else and Error code describing cause of failure.

typedef uint32_t (*ble_event_cb_t)([ble_event_enum_t](#_CPPv416ble_event_enum_t "ble_event_enum_t") event, void *param)[](#_CPPv414ble_event_cb_t "永久链接至目标")
:   for async dm_ble api event.

    ble event report.

    Param event, :
    :   event id. see ble_event_enum_t


        - param: param


### Enumerations[](#enumerations "永久链接至标题")

enum [anonymous][](#_CPPv4Ut1_3 "永久链接至目标")
:   GATT Attributes.


    *Values:*

    enumerator GATT_PRIMARY_SERVICE[](#_CPPv4NUt1_320GATT_PRIMARY_SERVICEE "永久链接至目标")

    enumerator GATT_SECONDARY_SERVICE[](#_CPPv4NUt1_322GATT_SECONDARY_SERVICEE "永久链接至目标")

    enumerator GATT_INCLUDE[](#_CPPv4NUt1_312GATT_INCLUDEE "永久链接至目标")

    enumerator GATT_CHARACTERISTIC[](#_CPPv4NUt1_319GATT_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_EXTENDED_PROPERTIES[](#_CPPv4NUt1_324GATT_EXTENDED_PROPERTIESE "永久链接至目标")

    enumerator GATT_USER_DESCRIPTION[](#_CPPv4NUt1_321GATT_USER_DESCRIPTIONE "永久链接至目标")

    enumerator GATT_CLIENT_CONFIG[](#_CPPv4NUt1_318GATT_CLIENT_CONFIGE "永久链接至目标")

    enumerator GATT_SERVER_CONFIG[](#_CPPv4NUt1_318GATT_SERVER_CONFIGE "永久链接至目标")

    enumerator GATT_FORMAT[](#_CPPv4NUt1_311GATT_FORMATE "永久链接至目标")

    enumerator GATT_AGGREGATE_FORMAT[](#_CPPv4NUt1_321GATT_AGGREGATE_FORMATE "永久链接至目标")

    enumerator GATT_VALID_RANGE[](#_CPPv4NUt1_316GATT_VALID_RANGEE "永久链接至目标")

    enumerator GATT_EXTERNAL_REPORT_REF[](#_CPPv4NUt1_324GATT_EXTERNAL_REPORT_REFE "永久链接至目标")

    enumerator GATT_IP_OP_FEATURE_REPORT_REF[](#_CPPv4NUt1_329GATT_IP_OP_FEATURE_REPORT_REFE "永久链接至目标")

enum [anonymous][](#_CPPv4Ut1_4 "永久链接至目标")
:   GATT Configuration.


    *Values:*

    enumerator GATT_CLI_CNFG_NOTIFICATION[](#_CPPv4NUt1_426GATT_CLI_CNFG_NOTIFICATIONE "永久链接至目标")
    :   GATT Client Configuration values

    enumerator GATT_CLI_CNFG_INDICATION[](#_CPPv4NUt1_424GATT_CLI_CNFG_INDICATIONE "永久链接至目标")

    enumerator GATT_CLI_CNFG_DEFAULT[](#_CPPv4NUt1_421GATT_CLI_CNFG_DEFAULTE "永久链接至目标")

    enumerator GATT_SER_CNFG_BROADCAST[](#_CPPv4NUt1_423GATT_SER_CNFG_BROADCASTE "永久链接至目标")
    :   GATT Server Configuration values

    enumerator GATT_SER_CNFG_DEFAULT[](#_CPPv4NUt1_421GATT_SER_CNFG_DEFAULTE "永久链接至目标")

enum [anonymous][](#_CPPv4Ut1_5 "永久链接至目标")
:   GATT Services.


    *Values:*

    enumerator GATT_GAP_SERVICE[](#_CPPv4NUt1_516GATT_GAP_SERVICEE "永久链接至目标")

    enumerator GATT_GATT_SERVICE[](#_CPPv4NUt1_517GATT_GATT_SERVICEE "永久链接至目标")

    enumerator GATT_IMMEDIATE_ALERT_SERVICE[](#_CPPv4NUt1_528GATT_IMMEDIATE_ALERT_SERVICEE "永久链接至目标")

    enumerator GATT_LINK_LOSS_SERVICE[](#_CPPv4NUt1_522GATT_LINK_LOSS_SERVICEE "永久链接至目标")

    enumerator GATT_TX_POWER_SERVICE[](#_CPPv4NUt1_521GATT_TX_POWER_SERVICEE "永久链接至目标")

    enumerator GATT_CURRENT_TIME_SERVICE[](#_CPPv4NUt1_525GATT_CURRENT_TIME_SERVICEE "永久链接至目标")

    enumerator GATT_REF_TIME_UPDATE_SERVICE[](#_CPPv4NUt1_528GATT_REF_TIME_UPDATE_SERVICEE "永久链接至目标")

    enumerator GATT_NEXT_DST_CHANGE_SERVICE[](#_CPPv4NUt1_528GATT_NEXT_DST_CHANGE_SERVICEE "永久链接至目标")

    enumerator GATT_GLUCOSE_SERVICE[](#_CPPv4NUt1_520GATT_GLUCOSE_SERVICEE "永久链接至目标")

    enumerator GATT_HEALTH_THERMOMETER_SERVICE[](#_CPPv4NUt1_531GATT_HEALTH_THERMOMETER_SERVICEE "永久链接至目标")

    enumerator GATT_DEVICE_INFO_SERVICE[](#_CPPv4NUt1_524GATT_DEVICE_INFO_SERVICEE "永久链接至目标")

    enumerator GATT_NWA_SERVICE[](#_CPPv4NUt1_516GATT_NWA_SERVICEE "永久链接至目标")

    enumerator GATT_WATCH_DOG_SERVICE[](#_CPPv4NUt1_522GATT_WATCH_DOG_SERVICEE "永久链接至目标")

    enumerator GATT_HEART_RATE_SERVICE[](#_CPPv4NUt1_523GATT_HEART_RATE_SERVICEE "永久链接至目标")

    enumerator GATT_PHONE_ALERT_STATUS_SERVICE[](#_CPPv4NUt1_531GATT_PHONE_ALERT_STATUS_SERVICEE "永久链接至目标")

    enumerator GATT_BATTERY_SERVICE[](#_CPPv4NUt1_520GATT_BATTERY_SERVICEE "永久链接至目标")

    enumerator GATT_BLOOD_PRESSURE_SERVICE[](#_CPPv4NUt1_527GATT_BLOOD_PRESSURE_SERVICEE "永久链接至目标")

    enumerator GATT_ALERT_NOTIFICATION_SERVICE[](#_CPPv4NUt1_531GATT_ALERT_NOTIFICATION_SERVICEE "永久链接至目标")

    enumerator GATT_HID_SERVICE[](#_CPPv4NUt1_516GATT_HID_SERVICEE "永久链接至目标")

    enumerator GATT_SCAN_PARAM_SERVICE[](#_CPPv4NUt1_523GATT_SCAN_PARAM_SERVICEE "永久链接至目标")

    enumerator GATT_RUNNING_SPEED_AND_CADENCE_SERVICE[](#_CPPv4NUt1_538GATT_RUNNING_SPEED_AND_CADENCE_SERVICEE "永久链接至目标")

    enumerator GATT_AIOS_SERVICE[](#_CPPv4NUt1_517GATT_AIOS_SERVICEE "永久链接至目标")

    enumerator GATT_CYCLING_SPEED_AND_CADENCE_SERVICE[](#_CPPv4NUt1_538GATT_CYCLING_SPEED_AND_CADENCE_SERVICEE "永久链接至目标")

    enumerator GATT_CPM_SERVICE[](#_CPPv4NUt1_516GATT_CPM_SERVICEE "永久链接至目标")

    enumerator GATT_LOCATION_AND_NAVIGATION_SERVICE[](#_CPPv4NUt1_536GATT_LOCATION_AND_NAVIGATION_SERVICEE "永久链接至目标")

    enumerator GATT_ENVIRONMENTAL_SENSING_SERVICE[](#_CPPv4NUt1_534GATT_ENVIRONMENTAL_SENSING_SERVICEE "永久链接至目标")

    enumerator GATT_BODY_COMPOSITION_SERVICE[](#_CPPv4NUt1_529GATT_BODY_COMPOSITION_SERVICEE "永久链接至目标")

    enumerator GATT_USER_DATA_SERVICE[](#_CPPv4NUt1_522GATT_USER_DATA_SERVICEE "永久链接至目标")

    enumerator GATT_WEIGHT_SCALE_SERVICE[](#_CPPv4NUt1_525GATT_WEIGHT_SCALE_SERVICEE "永久链接至目标")

    enumerator GATT_BM_SERVICE[](#_CPPv4NUt1_515GATT_BM_SERVICEE "永久链接至目标")

    enumerator GATT_CGM_SERVICE[](#_CPPv4NUt1_516GATT_CGM_SERVICEE "永久链接至目标")

    enumerator GATT_INT_PS_SERVICE[](#_CPPv4NUt1_519GATT_INT_PS_SERVICEE "永久链接至目标")

    enumerator GATT_IPS_SERVICE[](#_CPPv4NUt1_516GATT_IPS_SERVICEE "永久链接至目标")

    enumerator GATT_PULSE_OXIMETER_SERVICE[](#_CPPv4NUt1_527GATT_PULSE_OXIMETER_SERVICEE "永久链接至目标")

    enumerator GATT_HPS_SERVICE[](#_CPPv4NUt1_516GATT_HPS_SERVICEE "永久链接至目标")

    enumerator GATT_TDS_SERVICE[](#_CPPv4NUt1_516GATT_TDS_SERVICEE "永久链接至目标")

    enumerator GATT_OBJECT_TRANSFER_SERVICE[](#_CPPv4NUt1_528GATT_OBJECT_TRANSFER_SERVICEE "永久链接至目标")

    enumerator GATT_FTMS_SERVICE[](#_CPPv4NUt1_517GATT_FTMS_SERVICEE "永久链接至目标")

    enumerator GATT_RCS_SERVICE[](#_CPPv4NUt1_516GATT_RCS_SERVICEE "永久链接至目标")

    enumerator GATT_INSULIN_DELIVERY_SERVICE[](#_CPPv4NUt1_529GATT_INSULIN_DELIVERY_SERVICEE "永久链接至目标")

    enumerator GATT_FIND_ME_SERVICE[](#_CPPv4NUt1_520GATT_FIND_ME_SERVICEE "永久链接至目标")
    :   Dont find this on .org

    enumerator GATT_TPMS_SERVICE[](#_CPPv4NUt1_517GATT_TPMS_SERVICEE "永久链接至目标")
    :   Still not adopted, may need updation

enum [anonymous][](#_CPPv4Ut1_6 "永久链接至目标")
:   GATT Characteristic.


    *Values:*

    enumerator GATT_DEVICE_NAME_CHARACTERISTIC[](#_CPPv4NUt1_631GATT_DEVICE_NAME_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_APPEARANCE_CHARACTERISTIC[](#_CPPv4NUt1_630GATT_APPEARANCE_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_PERIPHRL_PRIVCY_FLG_CHARACTERISTIC[](#_CPPv4NUt1_639GATT_PERIPHRL_PRIVCY_FLG_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_RECONNECT_ADDR_CHARACTERISTIC[](#_CPPv4NUt1_634GATT_RECONNECT_ADDR_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_PRFRRD_CNXN_PARAM_CHARACTERISTIC[](#_CPPv4NUt1_637GATT_PRFRRD_CNXN_PARAM_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_SERVICE_CHANGED_CHARACTERISTIC[](#_CPPv4NUt1_635GATT_SERVICE_CHANGED_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_ALERT_LEVEL_CHARACTERISTIC[](#_CPPv4NUt1_631GATT_ALERT_LEVEL_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_TX_POWER_LEVEL_CHARACTERISTIC[](#_CPPv4NUt1_634GATT_TX_POWER_LEVEL_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_DATE_TIME_CHARACTERISTIC[](#_CPPv4NUt1_629GATT_DATE_TIME_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_DAY_OF_WEEK_CHARACTERISTIC[](#_CPPv4NUt1_631GATT_DAY_OF_WEEK_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_DAY_DATE_TIME_CHARACTERISTIC[](#_CPPv4NUt1_633GATT_DAY_DATE_TIME_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_EXACT_TIME_100_CHARACTERISTIC[](#_CPPv4NUt1_634GATT_EXACT_TIME_100_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_EXACT_TIME_256_CHARACTERISTIC[](#_CPPv4NUt1_634GATT_EXACT_TIME_256_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_DST_OFFSET_CHARACTERISTIC[](#_CPPv4NUt1_630GATT_DST_OFFSET_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_TIME_ZONE_CHARACTERISTIC[](#_CPPv4NUt1_629GATT_TIME_ZONE_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_LOCAL_TIME_INFO_CHARACTERISTIC[](#_CPPv4NUt1_635GATT_LOCAL_TIME_INFO_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_SEC_TIME_ZONE_CHARACTERISTIC[](#_CPPv4NUt1_633GATT_SEC_TIME_ZONE_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_TIME_WITH_DST_CHARACTERISTIC[](#_CPPv4NUt1_633GATT_TIME_WITH_DST_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_TIME_ACCURACY_CHARACTERISTIC[](#_CPPv4NUt1_633GATT_TIME_ACCURACY_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_TIME_SOURCE_CHARACTERISTIC[](#_CPPv4NUt1_631GATT_TIME_SOURCE_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_REF_TIME_INFO_CHARACTERISTIC[](#_CPPv4NUt1_633GATT_REF_TIME_INFO_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_TIME_BROADCAST_CHARACTERISTIC[](#_CPPv4NUt1_634GATT_TIME_BROADCAST_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_TIME_UPDATE_CONTROL_POINT[](#_CPPv4NUt1_630GATT_TIME_UPDATE_CONTROL_POINTE "永久链接至目标")

    enumerator GATT_TIME_UPDATE_STATE_CHARACTERISTIC[](#_CPPv4NUt1_637GATT_TIME_UPDATE_STATE_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_GLUCOSE_MSRMNT_CHARACTERISTIC[](#_CPPv4NUt1_634GATT_GLUCOSE_MSRMNT_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_BATTERY_LEVEL_CHARACTERISTIC[](#_CPPv4NUt1_633GATT_BATTERY_LEVEL_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_BATTERY_PWR_ST_CHARCTERISTIC[](#_CPPv4NUt1_633GATT_BATTERY_PWR_ST_CHARCTERISTICE "永久链接至目标")

    enumerator GATT_BATTERY_LEVEL_ST_CHARACTERISTIC[](#_CPPv4NUt1_636GATT_BATTERY_LEVEL_ST_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_TEMPERATURE_MSMNT_CHARACTERISTIC[](#_CPPv4NUt1_637GATT_TEMPERATURE_MSMNT_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_TEMPERATURE_TYPE_CHARACTERISTIC[](#_CPPv4NUt1_636GATT_TEMPERATURE_TYPE_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_INTERMEDIATE_TEMP_CHARACTERISTIC[](#_CPPv4NUt1_637GATT_INTERMEDIATE_TEMP_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_MSMNT_INTERVAL_CHARATACTERISTIC[](#_CPPv4NUt1_636GATT_MSMNT_INTERVAL_CHARATACTERISTICE "永久链接至目标")

    enumerator GATT_BOOT_KYBRD_IN_RPT_CHARACTERISTIC[](#_CPPv4NUt1_637GATT_BOOT_KYBRD_IN_RPT_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_SYSTEM_ID_CHARACTERISTIC[](#_CPPv4NUt1_629GATT_SYSTEM_ID_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_MODEL_NUMBER_CHARACTERISTIC[](#_CPPv4NUt1_632GATT_MODEL_NUMBER_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_SERIAL_NUMBER_CHARACTERISTIC[](#_CPPv4NUt1_633GATT_SERIAL_NUMBER_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_FIRMWARE_REV_CHARACTERISTIC[](#_CPPv4NUt1_632GATT_FIRMWARE_REV_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_HARDWARE_REV_CHARACTERISTIC[](#_CPPv4NUt1_632GATT_HARDWARE_REV_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_SOFTWARE_REV_CHARACTERISTIC[](#_CPPv4NUt1_632GATT_SOFTWARE_REV_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_MANUFACTURER_NAME_CHARACTERISTIC[](#_CPPv4NUt1_637GATT_MANUFACTURER_NAME_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_REG_CERT_DATA_CHARACTERISTIC[](#_CPPv4NUt1_633GATT_REG_CERT_DATA_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_CURRENT_TIME_CHARACTERISTIC[](#_CPPv4NUt1_632GATT_CURRENT_TIME_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_SCAN_REFRESH_CHARACTERISTIC[](#_CPPv4NUt1_632GATT_SCAN_REFRESH_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_BOOT_KYBRD_OP_CHARACTERISTIC[](#_CPPv4NUt1_633GATT_BOOT_KYBRD_OP_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_MOUSE_IP_CHARACTERISTIC[](#_CPPv4NUt1_628GATT_MOUSE_IP_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_GL_MSRMT_CTX_CHARACTERISTIC[](#_CPPv4NUt1_632GATT_GL_MSRMT_CTX_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_BP_MSRMT_CHARACTERISTIC[](#_CPPv4NUt1_628GATT_BP_MSRMT_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_INTRMDT_CUFF_PRSR_CHARACTERISTIC[](#_CPPv4NUt1_637GATT_INTRMDT_CUFF_PRSR_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_HR_MSRMT_CHARACTERISTIC[](#_CPPv4NUt1_628GATT_HR_MSRMT_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_BODY_SENSOR_LOC_CHARACTERISTIC[](#_CPPv4NUt1_635GATT_BODY_SENSOR_LOC_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_HR_CNTRL_POINT[](#_CPPv4NUt1_619GATT_HR_CNTRL_POINTE "永久链接至目标")

    enumerator GATT_NWA_CHARACTERISTIC[](#_CPPv4NUt1_623GATT_NWA_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_ALERT_STATUS_CHARACTERISTIC[](#_CPPv4NUt1_632GATT_ALERT_STATUS_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_RINGER_CONTROL_POINT_CHARACTERISTIC[](#_CPPv4NUt1_640GATT_RINGER_CONTROL_POINT_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_RINGER_SETTING_CHARACTERISTIC[](#_CPPv4NUt1_634GATT_RINGER_SETTING_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_ALERT_ID_BIT_MASK_CHARACTERISTIC[](#_CPPv4NUt1_637GATT_ALERT_ID_BIT_MASK_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_ALERT_ID_CHARACTERISTIC[](#_CPPv4NUt1_628GATT_ALERT_ID_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_ALERT_NTF_CONTROL_POINT[](#_CPPv4NUt1_628GATT_ALERT_NTF_CONTROL_POINTE "永久链接至目标")

    enumerator GATT_UNREAD_ALRT_STATUS_CHARACTERISTIC[](#_CPPv4NUt1_638GATT_UNREAD_ALRT_STATUS_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_NEW_ALERT_CHARACTERISTIC[](#_CPPv4NUt1_629GATT_NEW_ALERT_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_SPRTD_NEW_ALRT_CTGRY_CHARACTERISTIC[](#_CPPv4NUt1_640GATT_SPRTD_NEW_ALRT_CTGRY_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_SPRT_UNRD_ALRT_CTGRY_CHARACTERISTIC[](#_CPPv4NUt1_640GATT_SPRT_UNRD_ALRT_CTGRY_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_BP_FEATURE_CHARACTERISTIC[](#_CPPv4NUt1_630GATT_BP_FEATURE_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_HID_INFO_CHARACTERISTIC[](#_CPPv4NUt1_628GATT_HID_INFO_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_HID_RPT_MAP_CHARACTERISTIC[](#_CPPv4NUt1_631GATT_HID_RPT_MAP_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_HID_CP_CHARACTERISTIC[](#_CPPv4NUt1_626GATT_HID_CP_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_HID_RPT_CHARACTERISTIC[](#_CPPv4NUt1_627GATT_HID_RPT_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_HID_PROTO_MODE_CHARACTERISTIC[](#_CPPv4NUt1_634GATT_HID_PROTO_MODE_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_SCAN_WINDOW_CHARACTERISTIC[](#_CPPv4NUt1_631GATT_SCAN_WINDOW_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_PNP_ID_CHARACTERISTIC[](#_CPPv4NUt1_626GATT_PNP_ID_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_GL_FEATURE_CHARACTERISTIC[](#_CPPv4NUt1_630GATT_GL_FEATURE_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_RACP_CHARACTERISTIC[](#_CPPv4NUt1_624GATT_RACP_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_RSC_MSRMT_CHARACTERISTIC[](#_CPPv4NUt1_629GATT_RSC_MSRMT_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_RSC_FEATURE_CHARACTERISTIC[](#_CPPv4NUt1_631GATT_RSC_FEATURE_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_SC_CONTROL_POINT_CHARACTERISTIC[](#_CPPv4NUt1_636GATT_SC_CONTROL_POINT_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_CSC_MSRMT_CHARACTERISTIC[](#_CPPv4NUt1_629GATT_CSC_MSRMT_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_CSC_FEATURE_CHARACTERISTIC[](#_CPPv4NUt1_631GATT_CSC_FEATURE_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_SENSOR_LOCATION_CHARACTERISTIC[](#_CPPv4NUt1_635GATT_SENSOR_LOCATION_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_POX_SPOT_CHK_MSRMT_CHARACTERISTIC[](#_CPPv4NUt1_638GATT_POX_SPOT_CHK_MSRMT_CHARACTERISTICE "永久链接至目标")
    :   Still Not Adopted, may need updation Pulse Oximeter Characteristics defines

    enumerator GATT_POX_CONTINUOUS_MSRMT_CHARACTERISTIC[](#_CPPv4NUt1_640GATT_POX_CONTINUOUS_MSRMT_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_POX_PULSATILE_EVENT_CHARACTERISTIC[](#_CPPv4NUt1_639GATT_POX_PULSATILE_EVENT_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_POX_FEATURES_CHARACTERISTIC[](#_CPPv4NUt1_632GATT_POX_FEATURES_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_POX_CONTROL_POINT_CHARACTERISTIC[](#_CPPv4NUt1_637GATT_POX_CONTROL_POINT_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_CPM_MSRMT_CHARACTERISTIC[](#_CPPv4NUt1_629GATT_CPM_MSRMT_CHARACTERISTICE "永久链接至目标")
    :   CPM Characteristics Measurments

    enumerator GATT_CPM_VECTOR_CHARACTERISTIC[](#_CPPv4NUt1_630GATT_CPM_VECTOR_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_CPM_FEATURE_CHARACTERISTIC[](#_CPPv4NUt1_631GATT_CPM_FEATURE_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_CPM_CNTRL_PNT_CHARACTERISTIC[](#_CPPv4NUt1_633GATT_CPM_CNTRL_PNT_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_CPM_SENSOR_LOCATION_CHARACTERISTIC[](#_CPPv4NUt1_639GATT_CPM_SENSOR_LOCATION_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_LOCATION_AND_SPEED_CHARACTERISTIC[](#_CPPv4NUt1_638GATT_LOCATION_AND_SPEED_CHARACTERISTICE "永久链接至目标")
    :   Location and Navigation Characteristics

    enumerator GATT_NAVIGATION_CHARACTERISTIC[](#_CPPv4NUt1_630GATT_NAVIGATION_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_LN_POSITION_QUALITY_CHARACTERISTIC[](#_CPPv4NUt1_639GATT_LN_POSITION_QUALITY_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_LN_FEATURE_CHARACTERISTIC[](#_CPPv4NUt1_630GATT_LN_FEATURE_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_LN_CNTRL_PNT_CHARACTERISTIC[](#_CPPv4NUt1_632GATT_LN_CNTRL_PNT_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_CGM_MSRMT_CHARACTERISTIC[](#_CPPv4NUt1_629GATT_CGM_MSRMT_CHARACTERISTICE "永久链接至目标")
    :   CGM Characteristics defines

    enumerator GATT_CGM_FEATURES_CHARACTERISTIC[](#_CPPv4NUt1_632GATT_CGM_FEATURES_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_CGM_STATUS_CHARACTERISTIC[](#_CPPv4NUt1_630GATT_CGM_STATUS_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_CGM_SSN_STRT_TIME_CHARACTERISTIC[](#_CPPv4NUt1_637GATT_CGM_SSN_STRT_TIME_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_CGM_SSN_RUN_TIME_CHARACTERISTIC[](#_CPPv4NUt1_636GATT_CGM_SSN_RUN_TIME_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_CGM_SPECIFIC_OPS_CP_CHARACTERISTIC[](#_CPPv4NUt1_639GATT_CGM_SPECIFIC_OPS_CP_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_BATTERY_REMOVABLE_CHARACTERISTIC[](#_CPPv4NUt1_637GATT_BATTERY_REMOVABLE_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_BATTERY_SERV_REQRD_CHARACTERISTIC[](#_CPPv4NUt1_638GATT_BATTERY_SERV_REQRD_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_WS_MSRMT_CHARACTERISTIC[](#_CPPv4NUt1_628GATT_WS_MSRMT_CHARACTERISTICE "永久链接至目标")
    :   Weight Scale Characteristics define

    enumerator GATT_WS_FEATURE_CHARACTERISTIC[](#_CPPv4NUt1_630GATT_WS_FEATURE_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_BC_MSRMT_CHARACTERISTIC[](#_CPPv4NUt1_628GATT_BC_MSRMT_CHARACTERISTICE "永久链接至目标")
    :   Body Composition Characteristics define

    enumerator GATT_BC_FEATURE_CHARACTERISTIC[](#_CPPv4NUt1_630GATT_BC_FEATURE_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_FIRST_NAME_CHARACTERISTIC[](#_CPPv4NUt1_633GATT_UD_FIRST_NAME_CHARACTERISTICE "永久链接至目标")
    :   User Name Characterictics define

    enumerator GATT_UD_LAST_NAME_CHARACTERISTIC[](#_CPPv4NUt1_632GATT_UD_LAST_NAME_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_EMAIL_CHARACTERISTIC[](#_CPPv4NUt1_628GATT_UD_EMAIL_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_AGE_CHARACTERISTIC[](#_CPPv4NUt1_626GATT_UD_AGE_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_GENDER_CHARACTERISTIC[](#_CPPv4NUt1_629GATT_UD_GENDER_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_DB_CHNG_INC_CHARACTERISTIC[](#_CPPv4NUt1_634GATT_UD_DB_CHNG_INC_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_DOB_CHARACTERISTIC[](#_CPPv4NUt1_626GATT_UD_DOB_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_WEIGHT_CHARACTERISTIC[](#_CPPv4NUt1_629GATT_UD_WEIGHT_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_HEIGHT_CHARACTERISTIC[](#_CPPv4NUt1_629GATT_UD_HEIGHT_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_VO2MAX_CHARACTERISTIC[](#_CPPv4NUt1_629GATT_UD_VO2MAX_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_HRMAX_CHARACTERISTIC[](#_CPPv4NUt1_628GATT_UD_HRMAX_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_RHR_CHARACTERISTIC[](#_CPPv4NUt1_626GATT_UD_RHR_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_MAXRHR_CHARACTERISTIC[](#_CPPv4NUt1_629GATT_UD_MAXRHR_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_AEROTH_CHARACTERISTIC[](#_CPPv4NUt1_629GATT_UD_AEROTH_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_ANAETH_CHARACTERISTIC[](#_CPPv4NUt1_629GATT_UD_ANAETH_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_SPORTTYPE_CHARACTERISTIC[](#_CPPv4NUt1_632GATT_UD_SPORTTYPE_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_DATETHASS_CHARACTERISTIC[](#_CPPv4NUt1_632GATT_UD_DATETHASS_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_WAISTCIR_CHARACTERISTIC[](#_CPPv4NUt1_631GATT_UD_WAISTCIR_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_HIPCIR_CHARACTERISTIC[](#_CPPv4NUt1_629GATT_UD_HIPCIR_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_FATBURN_LOW_CHARACTERISTIC[](#_CPPv4NUt1_634GATT_UD_FATBURN_LOW_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_FATBURN_UPL_CHARACTERISTIC[](#_CPPv4NUt1_634GATT_UD_FATBURN_UPL_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_AERO_LOW_CHARACTERISTIC[](#_CPPv4NUt1_631GATT_UD_AERO_LOW_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_AERO_UPL_CHARACTERISTIC[](#_CPPv4NUt1_631GATT_UD_AERO_UPL_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_ANAE_LOW_CHARACTERISTIC[](#_CPPv4NUt1_631GATT_UD_ANAE_LOW_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_ANAE_UPL_CHARACTERISTIC[](#_CPPv4NUt1_631GATT_UD_ANAE_UPL_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_FIVEZONE_HRL_CHARACTERISTIC[](#_CPPv4NUt1_635GATT_UD_FIVEZONE_HRL_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_THREEZONE_HRL_CHARACTERISTIC[](#_CPPv4NUt1_636GATT_UD_THREEZONE_HRL_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_TWOZONE_HRL_CHARACTERISTIC[](#_CPPv4NUt1_634GATT_UD_TWOZONE_HRL_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_USER_INDEX_CHARACTERISTIC[](#_CPPv4NUt1_633GATT_UD_USER_INDEX_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_USER_CNTRL_PNT_CHARACTERISTIC[](#_CPPv4NUt1_637GATT_UD_USER_CNTRL_PNT_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_LANGUAGE_CHARACTERISTIC[](#_CPPv4NUt1_631GATT_UD_LANGUAGE_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_UD_REGISTERED_USER_CHARACTERISTIC[](#_CPPv4NUt1_638GATT_UD_REGISTERED_USER_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_ESS_DVC_CHARACTERISTIC[](#_CPPv4NUt1_627GATT_ESS_DVC_CHARACTERISTICE "永久链接至目标")
    :   Environmental Sensing Characterisitcs define

    enumerator GATT_ESS_TEMP_CHARACTERISTIC[](#_CPPv4NUt1_628GATT_ESS_TEMP_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_ES_MEASURMENT_DESCRIPTOR[](#_CPPv4NUt1_629GATT_ES_MEASURMENT_DESCRIPTORE "永久链接至目标")

    enumerator GATT_ES_TRIGGER_SETTING_DESCRIPTOR[](#_CPPv4NUt1_634GATT_ES_TRIGGER_SETTING_DESCRIPTORE "永久链接至目标")

    enumerator GATT_ES_CONFIGURATION_DESCRIPTOR[](#_CPPv4NUt1_632GATT_ES_CONFIGURATION_DESCRIPTORE "永久链接至目标")

    enumerator GATT_ES_MEASUREMENT_DESCRIPTOR[](#_CPPv4NUt1_630GATT_ES_MEASUREMENT_DESCRIPTORE "永久链接至目标")

    enumerator GATT_BM_FEATURES_CHARACTERISTIC[](#_CPPv4NUt1_631GATT_BM_FEATURES_CHARACTERISTICE "永久链接至目标")
    :   Bond Management Characteritiscs defines

    enumerator GATT_BM_CNTRL_PNT_CHARACTERISTIC[](#_CPPv4NUt1_632GATT_BM_CNTRL_PNT_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_AIO_DIGITAL_CHARACTERISTIC[](#_CPPv4NUt1_631GATT_AIO_DIGITAL_CHARACTERISTICE "永久链接至目标")
    :   Automation IO Service Characteritiscs defines

    enumerator GATT_AIO_ANALOG_CHARACTERISTIC[](#_CPPv4NUt1_630GATT_AIO_ANALOG_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_AIO_AGGREGATE_CHARACTERISTIC[](#_CPPv4NUt1_633GATT_AIO_AGGREGATE_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_IP_INDOOR_POS_CONFIG_CHARACTERISTIC[](#_CPPv4NUt1_640GATT_IP_INDOOR_POS_CONFIG_CHARACTERISTICE "永久链接至目标")
    :   Indoor Positioning Characteritiscs defines

    enumerator GATT_IP_LATITUDE_CHARACTERISTIC[](#_CPPv4NUt1_631GATT_IP_LATITUDE_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_IP_LONGITUDE_CHARACTERISTIC[](#_CPPv4NUt1_632GATT_IP_LONGITUDE_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_IP_LOCAL_NORTH_CHARACTERISTIC[](#_CPPv4NUt1_634GATT_IP_LOCAL_NORTH_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_IP_LOCAL_EAST_CHARACTERISTIC[](#_CPPv4NUt1_633GATT_IP_LOCAL_EAST_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_IP_FLOOR_NUM_CHARACTERISTIC[](#_CPPv4NUt1_632GATT_IP_FLOOR_NUM_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_IP_ALTITUDE_CHARACTERISTIC[](#_CPPv4NUt1_631GATT_IP_ALTITUDE_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_IP_UNCERTAINTY_CHARACTERISTIC[](#_CPPv4NUt1_634GATT_IP_UNCERTAINTY_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_IP_LOCAL_NAME_CHARACTERISTIC[](#_CPPv4NUt1_633GATT_IP_LOCAL_NAME_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_OTS_FEATURE_CHARACTERISTIC[](#_CPPv4NUt1_631GATT_OTS_FEATURE_CHARACTERISTICE "永久链接至目标")
    :   Object Transfer Characteritics defines

    enumerator GATT_OTS_OBJ_NAME_CHARACTERISTIC[](#_CPPv4NUt1_632GATT_OTS_OBJ_NAME_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_OTS_OBJ_TYPE_CHARACTERISTIC[](#_CPPv4NUt1_632GATT_OTS_OBJ_TYPE_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_OTS_OBJ_SIZE_CHARACTERISTIC[](#_CPPv4NUt1_632GATT_OTS_OBJ_SIZE_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_OTS_OBJ_FIRST_CRTD_CHARACTERISTIC[](#_CPPv4NUt1_638GATT_OTS_OBJ_FIRST_CRTD_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_OTS_OBJ_LAST_MODFD_CHARACTERISTIC[](#_CPPv4NUt1_638GATT_OTS_OBJ_LAST_MODFD_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_OTS_OBJ_ID_CHARACTERISTIC[](#_CPPv4NUt1_630GATT_OTS_OBJ_ID_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_OTS_OBJ_PRPTY_CHARACTERISTIC[](#_CPPv4NUt1_633GATT_OTS_OBJ_PRPTY_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_OTS_OACP_CHARACTERISTIC[](#_CPPv4NUt1_628GATT_OTS_OACP_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_OTS_OLCP_CHARACTERISTIC[](#_CPPv4NUt1_628GATT_OTS_OLCP_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_OTS_OBJ_LIST_FILTER_CHARACTERISTIC[](#_CPPv4NUt1_639GATT_OTS_OBJ_LIST_FILTER_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_OTS_OBJ_CHANGED_CHARACTERISTIC[](#_CPPv4NUt1_635GATT_OTS_OBJ_CHANGED_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_OTS_LE_PSM_CHARACTERISTIC[](#_CPPv4NUt1_630GATT_OTS_LE_PSM_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_OTS_OBJ_LAST_ACCSD_CHARACTERISTIC[](#_CPPv4NUt1_638GATT_OTS_OBJ_LAST_ACCSD_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_OTS_OBJ_CHECKSUM_CHARACTERISTIC[](#_CPPv4NUt1_636GATT_OTS_OBJ_CHECKSUM_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_OTS_OCTECT_OFFSET_CHARACTERISTIC[](#_CPPv4NUt1_637GATT_OTS_OCTECT_OFFSET_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_TPM_TIRE_PRESSURE_CHARACTERISTIC[](#_CPPv4NUt1_637GATT_TPM_TIRE_PRESSURE_CHARACTERISTICE "永久链接至目标")
    :   Tire Pressure Monitoring Characteritiscs defines Needs to update the opcode once TPMS spec is adopted

    enumerator GATT_TPM_TIRE_TEMP_CHARACTERISTIC[](#_CPPv4NUt1_633GATT_TPM_TIRE_TEMP_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_TPM_PRESSURE_CALIBN_CHARACTERISTIC[](#_CPPv4NUt1_639GATT_TPM_PRESSURE_CALIBN_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_TPM_TEMP_CALIBN_CHARACTERISTIC[](#_CPPv4NUt1_635GATT_TPM_TEMP_CALIBN_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_TPM_DISRY_CONN_MGMNT_CHARACTERISTIC[](#_CPPv4NUt1_640GATT_TPM_DISRY_CONN_MGMNT_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_TPM_ADV_PERIOD_CHARACTERISTIC[](#_CPPv4NUt1_634GATT_TPM_ADV_PERIOD_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_TD_CONTROL_POINT_CHARACTERISTIC[](#_CPPv4NUt1_636GATT_TD_CONTROL_POINT_CHARACTERISTICE "永久链接至目标")
    :   Transport Discovery Characteristics defines

    enumerator GATT_HPC_URI_CHARACTERISTIC[](#_CPPv4NUt1_627GATT_HPC_URI_CHARACTERISTICE "永久链接至目标")
    :   HTTP Proxy Characteristics defines

    enumerator GATT_HPC_HTTP_HEADERS_CHARACTERISTIC[](#_CPPv4NUt1_636GATT_HPC_HTTP_HEADERS_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_HPC_HTTP_ENTITY_BODY_CHARACTERISTIC[](#_CPPv4NUt1_640GATT_HPC_HTTP_ENTITY_BODY_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_HPC_HTTP_CP_CHARACTERISTIC[](#_CPPv4NUt1_631GATT_HPC_HTTP_CP_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_HPC_HTTP_STATUS_CODE_CHARACTERISTIC[](#_CPPv4NUt1_640GATT_HPC_HTTP_STATUS_CODE_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_HPC_HTTPS_SECURITY_CHARACTERISTIC[](#_CPPv4NUt1_638GATT_HPC_HTTPS_SECURITY_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_FTM_FEATURE_CHARACTERISTIC[](#_CPPv4NUt1_631GATT_FTM_FEATURE_CHARACTERISTICE "永久链接至目标")
    :   Fitness Machine Characteristics defines

    enumerator GATT_FTM_TREADMILL_CHARACTERISTIC[](#_CPPv4NUt1_633GATT_FTM_TREADMILL_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_FTM_CROSS_TRAINER_CHARACTERISTIC[](#_CPPv4NUt1_637GATT_FTM_CROSS_TRAINER_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_FTM_STEP_CLIMBER_CHARACTERISTIC[](#_CPPv4NUt1_636GATT_FTM_STEP_CLIMBER_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_FTM_STAIR_CLIMBER_CHARACTERISTIC[](#_CPPv4NUt1_637GATT_FTM_STAIR_CLIMBER_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_FTM_ROWER_DATA_CHARACTERISTIC[](#_CPPv4NUt1_634GATT_FTM_ROWER_DATA_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_FTM_INDOOR_BIKE_CHARACTERISTIC[](#_CPPv4NUt1_635GATT_FTM_INDOOR_BIKE_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_FTM_TRAINING_STATUS_CHARACTERISTIC[](#_CPPv4NUt1_639GATT_FTM_TRAINING_STATUS_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_FTM_SUPPD_SPEED_RNG_CHARACTERISTIC[](#_CPPv4NUt1_639GATT_FTM_SUPPD_SPEED_RNG_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_FTM_SUPPD_INCLN_RNG_CHARACTERISTIC[](#_CPPv4NUt1_639GATT_FTM_SUPPD_INCLN_RNG_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_FTM_SUPPD_RESIS_RNG_CHARACTERISTIC[](#_CPPv4NUt1_639GATT_FTM_SUPPD_RESIS_RNG_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_FTM_SUPPD_POWER_RNG_CHARACTERISTIC[](#_CPPv4NUt1_639GATT_FTM_SUPPD_POWER_RNG_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_FTM_SUPPD_HRTRE_RNG_CHARACTERISTIC[](#_CPPv4NUt1_639GATT_FTM_SUPPD_HRTRE_RNG_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_FTM_CONTROL_POINT_CHARACTERISTIC[](#_CPPv4NUt1_637GATT_FTM_CONTROL_POINT_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_FTM_MACHINE_STATUS_CHARACTERISTIC[](#_CPPv4NUt1_638GATT_FTM_MACHINE_STATUS_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_RC_FEATURE_CHARACTERISTIC[](#_CPPv4NUt1_630GATT_RC_FEATURE_CHARACTERISTICE "永久链接至目标")
    :   Reconnection Configuration Characteristic defines

    enumerator GATT_RC_SETTING_CHARACTERISTIC[](#_CPPv4NUt1_630GATT_RC_SETTING_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_RC_CP_CHARACTERISTIC[](#_CPPv4NUt1_625GATT_RC_CP_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_IDD_STATUS_CHANGED_CHARACTERISTIC[](#_CPPv4NUt1_638GATT_IDD_STATUS_CHANGED_CHARACTERISTICE "永久链接至目标")
    :   Insulin Delivery Characteristics defines

    enumerator GATT_IDD_STATUS_CHARACTERISTIC[](#_CPPv4NUt1_630GATT_IDD_STATUS_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_IDD_ANNUN_STATUS_CHARACTERISTIC[](#_CPPv4NUt1_636GATT_IDD_ANNUN_STATUS_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_IDD_FEATURE_CHARACTERISTIC[](#_CPPv4NUt1_631GATT_IDD_FEATURE_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_IDD_STATUS_READER_CP_CHARACTERISTIC[](#_CPPv4NUt1_640GATT_IDD_STATUS_READER_CP_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_IDD_COMMAND_CP_CHARACTERISTIC[](#_CPPv4NUt1_634GATT_IDD_COMMAND_CP_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_IDD_COMMAND_DATA_CHARACTERISTIC[](#_CPPv4NUt1_636GATT_IDD_COMMAND_DATA_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_IDD_RACP_CHARACTERISTIC[](#_CPPv4NUt1_628GATT_IDD_RACP_CHARACTERISTICE "永久链接至目标")

    enumerator GATT_IDD_HISTORY_DATA_CHARACTERISTIC[](#_CPPv4NUt1_636GATT_IDD_HISTORY_DATA_CHARACTERISTICE "永久链接至目标")

enum [anonymous][](#_CPPv4Ut1_7 "永久链接至目标")
:   only use for Operations Notified In Characteristic Callback


    *Values:*

    enumerator GATT_DB_READ[](#_CPPv4NUt1_712GATT_DB_READE "永久链接至目标")
    :   Read operation for Attribute

    enumerator GATT_DB_WRITE[](#_CPPv4NUt1_713GATT_DB_WRITEE "永久链接至目标")
    :   Write operation for Attribute

    enumerator GATT_DB_READ_BLOB[](#_CPPv4NUt1_717GATT_DB_READ_BLOBE "永久链接至目标")
    :   Read blob operation for Attribute

    enumerator GATT_DB_WRITE_WITHOUT_RSP[](#_CPPv4NUt1_725GATT_DB_WRITE_WITHOUT_RSPE "永久链接至目标")
    :   Write Without Response operation for Attribute

    enumerator GATT_DB_READ_BY_TYPE[](#_CPPv4NUt1_720GATT_DB_READ_BY_TYPEE "永久链接至目标")
    :   Read by UUID/Type operation for Attribute

    enumerator GATT_DB_SIGNED_WRITE[](#_CPPv4NUt1_720GATT_DB_SIGNED_WRITEE "永久链接至目标")
    :   Signed Write operation for Attribute

    enumerator GATT_DB_EXECUTE[](#_CPPv4NUt1_715GATT_DB_EXECUTEE "永久链接至目标")
    :   Execute Write operation for Attribute

    enumerator GATT_DB_PREPARE[](#_CPPv4NUt1_715GATT_DB_PREPAREE "永久链接至目标")
    :   Prepare Write operation for Attribute

    enumerator GATT_DB_UPDATE[](#_CPPv4NUt1_714GATT_DB_UPDATEE "永久链接至目标")
    :   Local update of a Readable Attribute Value using [GATT_DB_HANDLE](#structGATT__DB__HANDLE "#structGATT__DB__HANDLE") instead of Attribute Handle. See BT_gatt_db_set_char_val for more details.

    enumerator GATT_DB_128_BIT_UUID_FORMAT[](#_CPPv4NUt1_727GATT_DB_128_BIT_UUID_FORMATE "永久链接至目标")
    :   128 Bit Attribute UUID

    enumerator GATT_DB_PEER_INITIATED[](#_CPPv4NUt1_722GATT_DB_PEER_INITIATEDE "永久链接至目标")
    :   Peer initiated operation, needed when Peer is Reading or Writing Values either using GATT Read Procedures for Value and Descriptors.

    enumerator GATT_DB_LOCALLY_INITIATED[](#_CPPv4NUt1_725GATT_DB_LOCALLY_INITIATEDE "永久链接至目标")
    :   Locally initiated operation, needed for local updates based on Attribute Handles. In case [GATT_DB_HANDLE](#structGATT__DB__HANDLE "#structGATT__DB__HANDLE") is known, use of access through GATT_DB_UPDATE is recommended.

enum [anonymous][](#_CPPv4Ut1_8 "永久链接至目标")
:   *Values:*

    enumerator GATT_DB_CHAR_VALUE_READ_REQ[](#_CPPv4NUt1_827GATT_DB_CHAR_VALUE_READ_REQE "永久链接至目标")
    :   Characteristic Value Local Read Operation

    enumerator GATT_DB_CHAR_VALUE_WRITE_REQ[](#_CPPv4NUt1_828GATT_DB_CHAR_VALUE_WRITE_REQE "永久链接至目标")
    :   Characteristic Value Local Write Operation

    enumerator GATT_DB_CHAR_VALUE_WRITE_WITHOUT_REQ[](#_CPPv4NUt1_836GATT_DB_CHAR_VALUE_WRITE_WITHOUT_REQE "永久链接至目标")
    :   Characteristic Value Local Write Without Response Operation

    enumerator GATT_DB_CHAR_CLI_CNFG_READ_REQ[](#_CPPv4NUt1_830GATT_DB_CHAR_CLI_CNFG_READ_REQE "永久链接至目标")
    :   Characteristic Client Configuration Local Read Operation

    enumerator GATT_DB_CHAR_CLI_CNFG_WRITE_REQ[](#_CPPv4NUt1_831GATT_DB_CHAR_CLI_CNFG_WRITE_REQE "永久链接至目标")
    :   Characteristic Client Configuration Local Write Operation

    enumerator GATT_DB_CHAR_SER_CNFG_READ_REQ[](#_CPPv4NUt1_830GATT_DB_CHAR_SER_CNFG_READ_REQE "永久链接至目标")
    :   Characteristic Server Configuration Local Read Operation

    enumerator GATT_DB_CHAR_SER_CNFG_WRITE_REQ[](#_CPPv4NUt1_831GATT_DB_CHAR_SER_CNFG_WRITE_REQE "永久链接至目标")
    :   Characteristic Server Configuration Local Write Operation

    enumerator GATT_DB_CHAR_PEER_READ_REQ[](#_CPPv4NUt1_826GATT_DB_CHAR_PEER_READ_REQE "永久链接至目标")
    :   Characteristic Value Peer Read Operation

    enumerator GATT_DB_CHAR_PEER_WRITE_REQ[](#_CPPv4NUt1_827GATT_DB_CHAR_PEER_WRITE_REQE "永久链接至目标")
    :   Characteristic Value Peer Write Operation

    enumerator GATT_DB_CHAR_PEER_READ_BLOB_REQ[](#_CPPv4NUt1_831GATT_DB_CHAR_PEER_READ_BLOB_REQE "永久链接至目标")
    :   Characteristic Value Peer Read Blob Operation

    enumerator GATT_DB_CHAR_PEER_WRITE_CMD[](#_CPPv4NUt1_827GATT_DB_CHAR_PEER_WRITE_CMDE "永久链接至目标")
    :   Characteristic Value Peer Write Command

    enumerator GATT_DB_CHAR_PEER_READ_BY_TYPE_REQ[](#_CPPv4NUt1_834GATT_DB_CHAR_PEER_READ_BY_TYPE_REQE "永久链接至目标")
    :   Characteristic Value Peer Read by Type Operation

    enumerator GATT_DB_CHAR_PEER_SIGNED_WRITE_CMD[](#_CPPv4NUt1_834GATT_DB_CHAR_PEER_SIGNED_WRITE_CMDE "永久链接至目标")
    :   Characteristic Value Peer Signed Write Operation

    enumerator GATT_DB_CHAR_PEER_EXECUTE_WRITE_REQ[](#_CPPv4NUt1_835GATT_DB_CHAR_PEER_EXECUTE_WRITE_REQE "永久链接至目标")
    :   Characteristic Value Peer Execute Write Req

    enumerator GATT_DB_CHAR_PEER_PREPARE_WRITE_REQ[](#_CPPv4NUt1_835GATT_DB_CHAR_PEER_PREPARE_WRITE_REQE "永久链接至目标")
    :   Characteristic Value Peer Prepare Write Req

    enumerator GATT_DB_CHAR_PEER_CLI_CNFG_READ_REQ[](#_CPPv4NUt1_835GATT_DB_CHAR_PEER_CLI_CNFG_READ_REQE "永久链接至目标")
    :   Characteristic Client Configuration Peer Read Operation

    enumerator GATT_DB_CHAR_PEER_CLI_CNFG_WRITE_REQ[](#_CPPv4NUt1_836GATT_DB_CHAR_PEER_CLI_CNFG_WRITE_REQE "永久链接至目标")
    :   Characteristic Client Configuration Peer Write Operation

    enumerator GATT_DB_CHAR_PEER_SER_CNFG_READ_REQ[](#_CPPv4NUt1_835GATT_DB_CHAR_PEER_SER_CNFG_READ_REQE "永久链接至目标")
    :   Characteristic Server Configuration Peer Read Operation

    enumerator GATT_DB_CHAR_PEER_SER_CNFG_WRITE_REQ[](#_CPPv4NUt1_836GATT_DB_CHAR_PEER_SER_CNFG_WRITE_REQE "永久链接至目标")
    :   Characteristic Server Configuration Peer Write Operation

    enumerator GATT_DB_CHAR_PEER_USR_DESC_READ_REQ[](#_CPPv4NUt1_835GATT_DB_CHAR_PEER_USR_DESC_READ_REQE "永久链接至目标")
    :   Characteristic User Description Peer Read Operation

    enumerator GATT_DB_CHAR_PEER_USR_DESC_WRITE_REQ[](#_CPPv4NUt1_836GATT_DB_CHAR_PEER_USR_DESC_WRITE_REQE "永久链接至目标")
    :   Characteristic User Description Peer Write Operation

    enumerator GATT_DB_CHAR_PEER_HLD_DESC_READ_REQ[](#_CPPv4NUt1_835GATT_DB_CHAR_PEER_HLD_DESC_READ_REQE "永久链接至目标")
    :   Characteristic Higher Layer Defined Descriptor Peer Read Operation

    enumerator GATT_DB_CHAR_PEER_HLD_DESC_WRITE_REQ[](#_CPPv4NUt1_836GATT_DB_CHAR_PEER_HLD_DESC_WRITE_REQE "永久链接至目标")
    :   Characteristic Higher Layer Defined Descriptor Peer Write Operation

enum [anonymous][](#_CPPv4Ut1_9 "永久链接至目标")
:   *Values:*

    enumerator GATT_DB_CHAR_BROADCAST_PROPERTY[](#_CPPv4NUt1_931GATT_DB_CHAR_BROADCAST_PROPERTYE "永久链接至目标")
    :   Characteristic support Broadcast of its value to the peer. Setting this property automatically includes Characteristic Server Configuration Descriptor to the Characteristic

    enumerator GATT_DB_CHAR_READ_PROPERTY[](#_CPPv4NUt1_926GATT_DB_CHAR_READ_PROPERTYE "永久链接至目标")
    :   Characteristic support Reading its value by peer

    enumerator GATT_DB_CHAR_WRITE_WITHOUT_RSP_PROPERTY[](#_CPPv4NUt1_939GATT_DB_CHAR_WRITE_WITHOUT_RSP_PROPERTYE "永久链接至目标")
    :   Characteristic support Writing its value by peer Without Response

    enumerator GATT_DB_CHAR_WRITE_PROPERTY[](#_CPPv4NUt1_927GATT_DB_CHAR_WRITE_PROPERTYE "永久链接至目标")
    :   Characteristic supports Writing its value by peer

    enumerator GATT_DB_CHAR_NOTIFY_PROPERTY[](#_CPPv4NUt1_928GATT_DB_CHAR_NOTIFY_PROPERTYE "永久链接至目标")
    :   Characteristic supports Notifying its value to the peer. Setting this property automatically includes Characteristic Server Configuration Descriptor to the Characteristic

    enumerator GATT_DB_CHAR_INDICATE_PROPERTY[](#_CPPv4NUt1_930GATT_DB_CHAR_INDICATE_PROPERTYE "永久链接至目标")
    :   Characteristic supports Indicating its value to the peer

    enumerator GATT_DB_CHAR_SIGNED_WRITE_PROPERTY[](#_CPPv4NUt1_934GATT_DB_CHAR_SIGNED_WRITE_PROPERTYE "永久链接至目标")
    :   Characteristic supports Signed Write on its value

    enumerator GATT_DB_CHAR_WRIEABLE_AUX_PROPERTY[](#_CPPv4NUt1_934GATT_DB_CHAR_WRIEABLE_AUX_PROPERTYE "永久链接至目标")
    :   Characteristic supports write on its User Description Descriptor

    enumerator GATT_DB_NO_AUXILLARY_PROPERTY[](#_CPPv4NUt1_929GATT_DB_NO_AUXILLARY_PROPERTYE "永久链接至目标")
    :   No Auxillary Property

    enumerator GATT_DB_FIXED_LENGTH_PROPERTY[](#_CPPv4NUt1_929GATT_DB_FIXED_LENGTH_PROPERTYE "永久链接至目标")
    :   Characteristic Value is Fixed Length

    enumerator GATT_DB_AUTHORIZATION_PROPERTY[](#_CPPv4NUt1_930GATT_DB_AUTHORIZATION_PROPERTYE "永久链接至目标")

    enumerator GATT_DB_PEER_SPECIFIC_VAL_PROPERTY[](#_CPPv4NUt1_934GATT_DB_PEER_SPECIFIC_VAL_PROPERTYE "永久链接至目标")

    enumerator GATT_DB_CONST_ATTR_VAL_PROPERTY[](#_CPPv4NUt1_931GATT_DB_CONST_ATTR_VAL_PROPERTYE "永久链接至目标")

enum [anonymous][](#_CPPv4Ut2_10 "永久链接至目标")
:   GATT Characteristic and Descriptor permissions.


    *Values:*

    enumerator GATT_DB_PERM_NONE[](#_CPPv4NUt2_1017GATT_DB_PERM_NONEE "永久链接至目标")

    enumerator GATT_DB_PERM_READ[](#_CPPv4NUt2_1017GATT_DB_PERM_READE "永久链接至目标")

    enumerator GATT_DB_PERM_READ_ENCRYPTED[](#_CPPv4NUt2_1027GATT_DB_PERM_READ_ENCRYPTEDE "永久链接至目标")

    enumerator GATT_DB_PERM_READ_ENCRYPTED_MITM[](#_CPPv4NUt2_1032GATT_DB_PERM_READ_ENCRYPTED_MITME "永久链接至目标")

    enumerator GATT_DB_PERM_WRITE[](#_CPPv4NUt2_1018GATT_DB_PERM_WRITEE "永久链接至目标")

    enumerator GATT_DB_PERM_WRITE_ENCRYPTED[](#_CPPv4NUt2_1028GATT_DB_PERM_WRITE_ENCRYPTEDE "永久链接至目标")

    enumerator GATT_DB_PERM_WRITE_ENCRYPTED_MIMT[](#_CPPv4NUt2_1033GATT_DB_PERM_WRITE_ENCRYPTED_MIMTE "永久链接至目标")

    enumerator GATT_DB_PERM_WRITE_SIGNED[](#_CPPv4NUt2_1025GATT_DB_PERM_WRITE_SIGNEDE "永久链接至目标")

    enumerator GATT_DB_PERM_WRITE_SIGNED_MITM[](#_CPPv4NUt2_1030GATT_DB_PERM_WRITE_SIGNED_MITME "永久链接至目标")

enum [anonymous][](#_CPPv4Ut2_11 "永久链接至目标")
:   *Values:*

    enumerator GATT_DB_SER_SECURITY_LEVEL0[](#_CPPv4NUt2_1127GATT_DB_SER_SECURITY_LEVEL0E "永久链接至目标")
    :   Security related - combination of Level, Mode and Encryption Key Size (if applicable) describes complete security needsService employs Level 0

    enumerator GATT_DB_SER_SECURITY_LEVEL1[](#_CPPv4NUt2_1127GATT_DB_SER_SECURITY_LEVEL1E "永久链接至目标")
    :   Service employs Level 1

    enumerator GATT_DB_SER_SECURITY_LEVEL2[](#_CPPv4NUt2_1127GATT_DB_SER_SECURITY_LEVEL2E "永久链接至目标")
    :   Service employs Level 2

    enumerator GATT_DB_SER_SECURITY_LEVEL3[](#_CPPv4NUt2_1127GATT_DB_SER_SECURITY_LEVEL3E "永久链接至目标")
    :   Service employs Level 3

    enumerator GATT_DB_SER_SECURITY_MODE1[](#_CPPv4NUt2_1126GATT_DB_SER_SECURITY_MODE1E "永久链接至目标")
    :   Service employs Mode 1

    enumerator GATT_DB_SER_SECURITY_MODE2[](#_CPPv4NUt2_1126GATT_DB_SER_SECURITY_MODE2E "永久链接至目标")
    :   Service employs Mode 2

    enumerator GATT_DB_SER_MULTIPLE_CLIENTS_SUPPORT[](#_CPPv4NUt2_1136GATT_DB_SER_MULTIPLE_CLIENTS_SUPPORTE "永久链接至目标")
    :   ignore_this Unused right now

    enumerator GATT_DB_SER_SECONDARY_SERVICE_PROPERTY[](#_CPPv4NUt2_1138GATT_DB_SER_SECONDARY_SERVICE_PROPERTYE "永久链接至目标")
    :   Service is a Secondary Service. If this not used, Service is by default considered to be Primary

    enumerator GATT_DB_SER_128_BIT_UUID_FORMAT[](#_CPPv4NUt2_1131GATT_DB_SER_128_BIT_UUID_FORMATE "永久链接至目标")
    :   Service UUID is 128-bit

    enumerator GATT_DB_SER_NO_SECURITY_PROPERTY[](#_CPPv4NUt2_1132GATT_DB_SER_NO_SECURITY_PROPERTYE "永久链接至目标")
    :   Set this property to relax all Security on the Service

    enumerator GATT_DB_SER_ENC_KEY_SIZE_DONT_CARE[](#_CPPv4NUt2_1134GATT_DB_SER_ENC_KEY_SIZE_DONT_CAREE "永久链接至目标")
    :   This is employed to describe Service is not rigid on any Encryption Key Size. Any Size used by other Services or on the whole by the device will do

    enumerator GATT_DB_SER_ENCRYPT_KEY_SIZE_7[](#_CPPv4NUt2_1130GATT_DB_SER_ENCRYPT_KEY_SIZE_7E "永久链接至目标")
    :   Encyrption Key Size 7 Needed for the Service

    enumerator GATT_DB_SER_ENCRYPT_KEY_SIZE_8[](#_CPPv4NUt2_1130GATT_DB_SER_ENCRYPT_KEY_SIZE_8E "永久链接至目标")
    :   Encyrption Key Size 8 Needed for the Service

    enumerator GATT_DB_SER_ENCRYPT_KEY_SIZE_9[](#_CPPv4NUt2_1130GATT_DB_SER_ENCRYPT_KEY_SIZE_9E "永久链接至目标")
    :   Encyrption Key Size 9 Needed for the Service

    enumerator GATT_DB_SER_ENCRYPT_KEY_SIZE_10[](#_CPPv4NUt2_1131GATT_DB_SER_ENCRYPT_KEY_SIZE_10E "永久链接至目标")
    :   Encyrption Key Size 10 Needed for the Service

    enumerator GATT_DB_SER_ENCRYPT_KEY_SIZE_11[](#_CPPv4NUt2_1131GATT_DB_SER_ENCRYPT_KEY_SIZE_11E "永久链接至目标")
    :   Encyrption Key Size 11 Needed for the Service

    enumerator GATT_DB_SER_ENCRYPT_KEY_SIZE_12[](#_CPPv4NUt2_1131GATT_DB_SER_ENCRYPT_KEY_SIZE_12E "永久链接至目标")
    :   Encryption Key Size 12 Needed for the Service

    enumerator GATT_DB_SER_ENCRYPT_KEY_SIZE_13[](#_CPPv4NUt2_1131GATT_DB_SER_ENCRYPT_KEY_SIZE_13E "永久链接至目标")
    :   Encryption Key Size 13 Needed for the Service

    enumerator GATT_DB_SER_ENCRYPT_KEY_SIZE_14[](#_CPPv4NUt2_1131GATT_DB_SER_ENCRYPT_KEY_SIZE_14E "永久链接至目标")
    :   Encryption Key Size 14 Needed for the Service

    enumerator GATT_DB_SER_ENCRYPT_KEY_SIZE_15[](#_CPPv4NUt2_1131GATT_DB_SER_ENCRYPT_KEY_SIZE_15E "永久链接至目标")
    :   Encryption Key Size 15 Needed for the Service

    enumerator GATT_DB_SER_ENCRYPT_KEY_SIZE_16[](#_CPPv4NUt2_1131GATT_DB_SER_ENCRYPT_KEY_SIZE_16E "永久链接至目标")
    :   Encryption Key Size 16 Needed for the Service

enum ble_event_enum_t[](#_CPPv416ble_event_enum_t "永久链接至目标")
:   *Values:*

    enumerator BK_DM_BLE_EVENT_STACK_OK[](#_CPPv4N16ble_event_enum_t24BK_DM_BLE_EVENT_STACK_OKE "永久链接至目标")
    :   ble stack init ok, param null

    enumerator BK_DM_BLE_EVENT_REPORT_ADV[](#_CPPv4N16ble_event_enum_t26BK_DM_BLE_EVENT_REPORT_ADVE "永久链接至目标")
    :   scan peer adv report, param ble_adv_report_t

    enumerator BK_DM_BLE_EVENT_MTU_CHANGE[](#_CPPv4N16ble_event_enum_t26BK_DM_BLE_EVENT_MTU_CHANGEE "永久链接至目标")
    :   mtu change event, param [ble_mtu_change_t](ble.html#structble__mtu__change__t "ble.html#structble__mtu__change__t")

    enumerator BK_DM_BLE_EVENT_CONNECT[](#_CPPv4N16ble_event_enum_t23BK_DM_BLE_EVENT_CONNECTE "永久链接至目标")
    :   recv connnect event, param [ble_conn_att_t](#structble__conn__att__t "#structble__conn__att__t")

    enumerator BK_DM_BLE_EVENT_DISCONNECT[](#_CPPv4N16ble_event_enum_t26BK_DM_BLE_EVENT_DISCONNECTE "永久链接至目标")
    :   recv disconnect event, param [ble_conn_att_t](#structble__conn__att__t "#structble__conn__att__t")

    enumerator BK_DM_BLE_EVENT_CREATE_DB[](#_CPPv4N16ble_event_enum_t25BK_DM_BLE_EVENT_CREATE_DBE "永久链接至目标")
    :   create db event, param [ble_create_db_t](ble.html#structble__create__db__t "ble.html#structble__create__db__t"), param null

    enumerator BK_DM_BLE_EVENT_TX_DONE[](#_CPPv4N16ble_event_enum_t23BK_DM_BLE_EVENT_TX_DONEE "永久链接至目标")
    :   tx complete event, param [ble_att_tx_compl_t](#structble__att__tx__compl__t "#structble__att__tx__compl__t")

    enumerator BK_DM_BLE_EVENT_READ_PHY[](#_CPPv4N16ble_event_enum_t24BK_DM_BLE_EVENT_READ_PHYE "永久链接至目标")
    :   get current conn phy result, param [ble_read_phy_t](ble.html#structble__read__phy__t "ble.html#structble__read__phy__t")

    enumerator BK_DM_BLE_EVENT_CONN_UPDATA[](#_CPPv4N16ble_event_enum_t27BK_DM_BLE_EVENT_CONN_UPDATAE "永久链接至目标")
    :   recv ble conn update event result, param [ble_conn_update_param_compl_ind_t](#structble__conn__update__param__compl__ind__t "#structble__conn__update__param__compl__ind__t")

    enumerator BK_DM_BLE_EVENT_DISCOVERY_PRIMARY_SERVICE[](#_CPPv4N16ble_event_enum_t41BK_DM_BLE_EVENT_DISCOVERY_PRIMARY_SERVICEE "永久链接至目标")
    :   discover peer primary service result, param ble_discovery_primary_service_t

    enumerator BK_DM_BLE_EVENT_DISCOVERY_CHAR[](#_CPPv4N16ble_event_enum_t30BK_DM_BLE_EVENT_DISCOVERY_CHARE "永久链接至目标")
    :   discover peer characteristic result, param ble_discovery_char_t

    enumerator BK_DM_BLE_EVENT_RECV_NOTIFY[](#_CPPv4N16ble_event_enum_t27BK_DM_BLE_EVENT_RECV_NOTIFYE "永久链接至目标")
    :   recv gatt client notify, param [ble_att_notify_t](#structble__att__notify__t "#structble__att__notify__t")

    enumerator BK_DM_BLE_EVENT_ATT_READ_RESPONSE[](#_CPPv4N16ble_event_enum_t33BK_DM_BLE_EVENT_ATT_READ_RESPONSEE "永久链接至目标")
    :   recv gatt read response, param [ble_att_rw_t](#structble__att__rw__t "#structble__att__rw__t")

    enumerator BK_DM_BLE_EVENT_CONN_UPD_PAR_ASK[](#_CPPv4N16ble_event_enum_t32BK_DM_BLE_EVENT_CONN_UPD_PAR_ASKE "永久链接至目标")
    :   recv ble connection param update req, param [ble_conn_update_param_ind_t](#structble__conn__update__param__ind__t "#structble__conn__update__param__ind__t")

    enumerator BK_DM_BLE_EVENT_DEINIT_STACK_OK[](#_CPPv4N16ble_event_enum_t31BK_DM_BLE_EVENT_DEINIT_STACK_OKE "永久链接至目标")
    :   ble stack deinit ok, param null

enum advertise_filter_policy[](#_CPPv423advertise_filter_policy "永久链接至目标")
:   use in [bk_ble_set_advertising_params](#group__bk__dm__ble__api__v1_1gac82851a90130a907f6a3f58863aae7d5 "#group__bk__dm__ble__api__v1_1gac82851a90130a907f6a3f58863aae7d5")


    *Values:*

    enumerator ADV_FILTER_POLICY_ALLOW_SCAN_ANY_CONNECT_ANY[](#_CPPv4N23advertise_filter_policy44ADV_FILTER_POLICY_ALLOW_SCAN_ANY_CONNECT_ANYE "永久链接至目标")
    :   both scan and connect

    enumerator ADV_FILTER_POLICY_ALLOW_SCAN_WLST_CONNECT_ANY[](#_CPPv4N23advertise_filter_policy45ADV_FILTER_POLICY_ALLOW_SCAN_WLST_CONNECT_ANYE "永久链接至目标")
    :   scan only in white list, connect any

    enumerator ADV_FILTER_POLICY_ALLOW_SCAN_ANY_CONNECT_WLIT[](#_CPPv4N23advertise_filter_policy45ADV_FILTER_POLICY_ALLOW_SCAN_ANY_CONNECT_WLITE "永久链接至目标")
    :   scan any, connect only in white list

    enumerator ADV_FILTER_POLICY_ALLOW_SCAN_WLIT_CONNECT_WLIT[](#_CPPv4N23advertise_filter_policy46ADV_FILTER_POLICY_ALLOW_SCAN_WLIT_CONNECT_WLITE "永久链接至目标")
    :   both scan connect only in white list

enum advertise_legacy_type[](#_CPPv421advertise_legacy_type "永久链接至目标")
:   use in [bk_ble_set_advertising_params](#group__bk__dm__ble__api__v1_1gac82851a90130a907f6a3f58863aae7d5 "#group__bk__dm__ble__api__v1_1gac82851a90130a907f6a3f58863aae7d5")


    *Values:*

    enumerator ADV_LEGACY_TYPE_ADV_IND[](#_CPPv4N21advertise_legacy_type23ADV_LEGACY_TYPE_ADV_INDE "永久链接至目标")
    :   adv that can be scan and connect

    enumerator ADV_LEGACY_TYPE_ADV_DIRECT_IND_HIGH[](#_CPPv4N21advertise_legacy_type35ADV_LEGACY_TYPE_ADV_DIRECT_IND_HIGHE "永久链接至目标")
    :   adv that can be connect by special device(white list). This send adv more frequently.

    enumerator ADV_LEGACY_TYPE_ADV_SCAN_IND[](#_CPPv4N21advertise_legacy_type28ADV_LEGACY_TYPE_ADV_SCAN_INDE "永久链接至目标")
    :   adv that can be scan

    enumerator ADV_LEGACY_TYPE_ADV_NON_IND[](#_CPPv4N21advertise_legacy_type27ADV_LEGACY_TYPE_ADV_NON_INDE "永久链接至目标")
    :   adv that can’t be scan and connect

    enumerator ADV_LEGACY_TYPE_ADV_DIRECT_IND_LOW[](#_CPPv4N21advertise_legacy_type34ADV_LEGACY_TYPE_ADV_DIRECT_IND_LOWE "永久链接至目标")
    :   adv that can be connect by special device(white list). This send adv more few.
