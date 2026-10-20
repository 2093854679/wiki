---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/api-reference/bluetooth/dm_ble.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="dm-ble-apis"></a>

# DM BLE APIs

重要

The DM BLE API v1.0 is the lastest stable DM BLE APIs. All new applications should use DM BLE API v1.0.

<a id="dm-ble-api-categories"></a>

## DM BLE API Categories

Most of DM BLE APIs can be categoried as:

Interface specific DM BLE APIs:
:   - BLE common interface
    - BLE scan interface
    - BLE ADV interface
    - BLE connect interface

<a id="compitability-and-extension"></a>

## Compitability and Extension

The DM BLE APIs are flexible, easy to be extended and backward compatible. For most of the BLE configurations, we put some reserved fields in the config struct for future extendence. The API users need to make sure the reserved fields are initialized to 0, otherwise the compatibility may be broken as more fields are added.

<a id="programing-principle"></a>

## Programing Principle

重要

Here is some general principle for DM BLE API users:
:   - Always init the reserved fields of config stuct to 0
    - Use BK\_ERR\_CHECK to check the return value of the DM BLE API
    - If you are not sure how to use DM BLE APIs, study the BLE example code first
    - If you are not sure how to initialize some fields of config struct, use the default configuration macro to use the config first and then set application specific fields.
    - Don’t do too much work in BLE event callback, relay the event to your own application task.

<a id="user-development-model"></a>

## User Development Model

Similar as most popular BLE driver, the Beken BLE driver is implemented as event driver. The application call DM BLE APIs to operate the BLE driver and get notified by BLE event.

<a id="user-guide"></a>

## User Guide

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
    ble\_adv\_parameter\_t tmp\_param;

    memset(\&tmp\_param, 0, sizeof(tmp\_param));

    tmp\_param.adv\_intv\_max \= 160;
    tmp\_param.adv\_intv\_min \= 120;
    tmp\_param.adv\_type \= ADV\_LEGACY\_TYPE\_ADV\_IND;
    tmp\_param.chnl\_map \= ADV\_ALL\_CHNLS;
    tmp\_param.filter\_policy \= ADV\_FILTER\_POLICY\_ALLOW\_SCAN\_ANY\_CONNECT\_ANY;
    tmp\_param.own\_addr\_type \= 0;
    tmp\_param.peer\_addr\_type \= 0;

    const uint8\_t adv\_data\[\] \= {0x02, 0x01, 0x06, 0x0f, 0x08, 0x53, 0x6d, 0x61, 0x72, 0x74, 0x2d, 0x44, 0x6f, 0x6f, 0x72, 0x62, 0x65, 0x6c, 0x6c};

    //wait for ble\_at\_cmd\_cb
    retval \= bk\_ble\_set\_advertising\_data(adv\_len, adv\_data, ble\_at\_cmd\_cb);
    if (retval !\= BK\_ERR\_BLE\_SUCCESS)
    {

    }

    retval \= bk\_ble\_set\_advertising\_enable(1, ble\_at\_cmd\_cb);
    //wait for ble\_at\_cmd\_cb
    if (retval !\= BK\_ERR\_BLE\_SUCCESS)
    {

    }

<a id="api-reference"></a>

## API Reference

<a id="header-file"></a>

### Header File

- [dm\_ble.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/dm_ble.h)

<a id="functions"></a>

### Functions

<a id="_CPPv425bk_ble_set_event_callback14ble_event_cb_t"></a>

<a id="_CPPv325bk_ble_set_event_callback14ble_event_cb_t"></a> <a id="_CPPv225bk_ble_set_event_callback14ble_event_cb_t"></a> <a id="bk_ble_set_event_callback__ble_event_cb_t"></a> <a id="group__bk__dm__ble__api__v1_1ga968bd9be6af1ef18baa218828e734542"></a> void bk\_ble\_set\_event\_callback([ble\_event\_cb\_t](#_CPPv414ble_event_cb_t "ble_event_cb_t") func)
:   Register dm\_ble event notification callback.

    User example:

    ```

    ```

    **Attention**
    :   1\. you must regist it, otherwise you cant get any event !

        2\. you must regist it before bk\_ble\_create\_db, otherwise you cant get BLE\_5\_CREATE\_DB event

    参数
    :   **func, :** – event callback

    返回
    :   - void

<a id="_CPPv429bk_ble_set_advertising_paramsP19ble_adv_parameter_t12ble_cmd_cb_t"></a>

<a id="_CPPv329bk_ble_set_advertising_paramsP19ble_adv_parameter_t12ble_cmd_cb_t"></a> <a id="_CPPv229bk_ble_set_advertising_paramsP19ble_adv_parameter_t12ble_cmd_cb_t"></a> <a id="bk_ble_set_advertising_params__ble_adv_parameter_tP.ble_cmd_cb_t"></a> <a id="group__bk__dm__ble__api__v1_1gac82851a90130a907f6a3f58863aae7d5"></a> [ble\_err\_t](ble.md#_CPPv49ble_err_t "ble_err_t") bk\_ble\_set\_advertising\_params([ble\_adv\_parameter\_t](#_CPPv419ble_adv_parameter_t "ble_adv_parameter_t") \*param, [ble\_cmd\_cb\_t](ble.md#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)
:   Set adv param.

    **Attention**
    :   1.you must wait callback status, 0 mean success.

    参数
    :   - **param, :** – adv param see [ble\_adv\_parameter\_t](#structble__adv__parameter__t)
        - **callback, :** – register a callback for this action, ble\_cmd\_t: BLE\_CREATE\_ADV

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv427bk_ble_set_advertising_data7uint8_tP7uint8_t12ble_cmd_cb_t"></a>

<a id="_CPPv327bk_ble_set_advertising_data7uint8_tP7uint8_t12ble_cmd_cb_t"></a> <a id="_CPPv227bk_ble_set_advertising_data7uint8_tP7uint8_t12ble_cmd_cb_t"></a> <a id="bk_ble_set_advertising_data__uint8_t.uint8_tP.ble_cmd_cb_t"></a> <a id="group__bk__dm__ble__api__v1_1gada68052dae4825cd8d73021f4157389b"></a> [ble\_err\_t](ble.md#_CPPv49ble_err_t "ble_err_t") bk\_ble\_set\_advertising\_data(uint8\_t adv\_len, uint8\_t \*adv\_buff, [ble\_cmd\_cb\_t](ble.md#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)
:   Set adv data.

    **Attention**
    :   1.you must wait callback status, 0 mean success.

    参数
    :   - **adv\_len, :** – adv data len
        - **adv\_buff, :** – adv data
        - **callback, :** – register a callback for this action, ble\_cmd\_t: BLE\_SET\_ADV\_DATA

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv429bk_ble_set_scan_response_data7uint8_tP7uint8_t12ble_cmd_cb_t"></a>

<a id="_CPPv329bk_ble_set_scan_response_data7uint8_tP7uint8_t12ble_cmd_cb_t"></a> <a id="_CPPv229bk_ble_set_scan_response_data7uint8_tP7uint8_t12ble_cmd_cb_t"></a> <a id="bk_ble_set_scan_response_data__uint8_t.uint8_tP.ble_cmd_cb_t"></a> <a id="group__bk__dm__ble__api__v1_1ga71e725c70ab665212c98054b458a2e64"></a> [ble\_err\_t](ble.md#_CPPv49ble_err_t "ble_err_t") bk\_ble\_set\_scan\_response\_data(uint8\_t scan\_response\_data\_length, uint8\_t \*scan\_response\_data, [ble\_cmd\_cb\_t](ble.md#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)
:   Set adv scan response data.

    **Attention**
    :   1.you must wait callback status, 0 mean success.

    参数
    :   - **scan\_response\_data\_length, :** – data len
        - **scan\_response\_data, :** – data
        - **callback, :** – register a callback for this action, ble\_cmd\_t: BLE\_SET\_RSP\_DATA

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv429bk_ble_set_advertising_enable7uint8_t12ble_cmd_cb_t"></a>

<a id="_CPPv329bk_ble_set_advertising_enable7uint8_t12ble_cmd_cb_t"></a> <a id="_CPPv229bk_ble_set_advertising_enable7uint8_t12ble_cmd_cb_t"></a> <a id="bk_ble_set_advertising_enable__uint8_t.ble_cmd_cb_t"></a> <a id="group__bk__dm__ble__api__v1_1gad06f3c8aeb2065001794c9783f1b595a"></a> [ble\_err\_t](ble.md#_CPPv49ble_err_t "ble_err_t") bk\_ble\_set\_advertising\_enable(uint8\_t enable, [ble\_cmd\_cb\_t](ble.md#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)
:   Set enable/disable adv.

    **Attention**
    :   1.you must wait callback status, 0 mean success.

    参数
    :   - **enable, :** – enable or disable
        - **callback, :** – register a callback for this action, ble\_cmd\_t: BLE\_START\_ADV(enable) BLE\_STOP\_ADV(disable)

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv428bk_ble_disconnect_connectionP9bd_addr_t12ble_cmd_cb_t"></a>

<a id="_CPPv328bk_ble_disconnect_connectionP9bd_addr_t12ble_cmd_cb_t"></a> <a id="_CPPv228bk_ble_disconnect_connectionP9bd_addr_t12ble_cmd_cb_t"></a> <a id="bk_ble_disconnect_connection__bd_addr_tP.ble_cmd_cb_t"></a> <a id="group__bk__dm__ble__api__v1_1gaad124e70566b7e2670684befa6771e1a"></a> [ble\_err\_t](ble.md#_CPPv49ble_err_t "ble_err_t") bk\_ble\_disconnect\_connection([bd\_addr\_t](ble.md#_CPPv49bd_addr_t "bd_addr_t") \*addr, [ble\_cmd\_cb\_t](ble.md#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)
:   disconnect ble connection

    **Attention**
    :   1.you must wait callback status, 0 mean success.

    参数
    :   - **addr, :** – peer addr
        - **callback, :** – register a callback for this action, ble\_cmd\_t: BLE\_CONN\_DIS\_CONN

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv426bk_ble_gatt_db_add_serviceP20GATT_DB_SERVICE_INFO8uint16_tP8uint16_t"></a>

<a id="_CPPv326bk_ble_gatt_db_add_serviceP20GATT_DB_SERVICE_INFO8uint16_tP8uint16_t"></a> <a id="_CPPv226bk_ble_gatt_db_add_serviceP20GATT_DB_SERVICE_INFO8uint16_tP8uint16_t"></a> <a id="bk_ble_gatt_db_add_service__GATT_DB_SERVICE_INFOP.uint16_t.uint16_tP"></a> <a id="group__bk__dm__ble__api__v1_1gae22cd028b7b7b834f0136a4b7fac339e"></a> [ble\_err\_t](ble.md#_CPPv49ble_err_t "ble_err_t") bk\_ble\_gatt\_db\_add\_service([GATT\_DB\_SERVICE\_INFO](#_CPPv420GATT_DB_SERVICE_INFO "GATT_DB_SERVICE_INFO") \*service\_info, uint16\_t num\_attr\_handles, uint16\_t \*service\_handle)
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
    :   - **service\_info, :** – service info
        - **num\_attr\_handles, :** – how many attr in this service
        - **service\_handle, :** – **\[out\]** out put a handle to user.

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv433bk_ble_gatt_db_add_characteristic8uint16_tP17GATT_DB_UUID_TYPE8uint16_t8uint16_tP9ATT_VALUEP8uint16_t"></a>

<a id="_CPPv333bk_ble_gatt_db_add_characteristic8uint16_tP17GATT_DB_UUID_TYPE8uint16_t8uint16_tP9ATT_VALUEP8uint16_t"></a> <a id="_CPPv233bk_ble_gatt_db_add_characteristic8uint16_tP17GATT_DB_UUID_TYPE8uint16_t8uint16_tP9ATT_VALUEP8uint16_t"></a> <a id="bk_ble_gatt_db_add_characteristic__uint16_t.GATT_DB_UUID_TYPEP.uint16_t.uint16_t.ATT_VALUEP.uint16_tP"></a> <a id="group__bk__dm__ble__api__v1_1gac69295a0b96f24511a489044d8d7fcc4"></a> [ble\_err\_t](ble.md#_CPPv49ble_err_t "ble_err_t") bk\_ble\_gatt\_db\_add\_characteristic(uint16\_t service\_handle, [GATT\_DB\_UUID\_TYPE](#_CPPv417GATT_DB_UUID_TYPE "GATT_DB_UUID_TYPE") \*char\_uuid, uint16\_t perm, uint16\_t property, [ATT\_VALUE](#_CPPv49ATT_VALUE "ATT_VALUE") \*char\_value, uint16\_t \*char\_handle)
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
    :   - **service\_handle, :** – service handle, get from bk\_ble\_gatt\_db\_add\_service
        - **char\_uuid, :** – characteristic’s uuid, in ATT\_UUID16 or [ATT\_UUID128](#structATT__UUID128), see [GATT\_DB\_UUID\_TYPE](#structGATT__DB__UUID__TYPE)
        - **perm, :** – permission, such as GATT\_DB\_PERM\_READ GATT\_DB\_PERM\_WRITE
        - **property, :** – property, such as [GATT\_DB\_CHAR\_READ\_PROPERTY](#group__gatt__characteristic__properties_1ggab04a0655cd1e3bcac5e8f48c18df1a57a90ebdf42e3bda749182f0229c30c3495) [GATT\_DB\_CHAR\_NOTIFY\_PROPERTY](#group__gatt__characteristic__properties_1ggab04a0655cd1e3bcac5e8f48c18df1a57a4c0b4fe5642fc1602ed91532da1492bb)
        - **char\_value, :** – att data, see [ATT\_VALUE](#structATT__VALUE)
        - **char\_handle, :** – **\[out\]** output a handle

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv444bk_ble_gatt_db_add_characteristic_descriptor8uint16_t8uint16_tP17GATT_DB_UUID_TYPE8uint16_tP9ATT_VALUE"></a>

<a id="_CPPv344bk_ble_gatt_db_add_characteristic_descriptor8uint16_t8uint16_tP17GATT_DB_UUID_TYPE8uint16_tP9ATT_VALUE"></a> <a id="_CPPv244bk_ble_gatt_db_add_characteristic_descriptor8uint16_t8uint16_tP17GATT_DB_UUID_TYPE8uint16_tP9ATT_VALUE"></a> <a id="bk_ble_gatt_db_add_characteristic_descriptor__uint16_t.uint16_t.GATT_DB_UUID_TYPEP.uint16_t.ATT_VALUEP"></a> <a id="group__bk__dm__ble__api__v1_1gaec20ef220605c266e20915555a287b1f"></a> [ble\_err\_t](ble.md#_CPPv49ble_err_t "ble_err_t") bk\_ble\_gatt\_db\_add\_characteristic\_descriptor(uint16\_t service\_handle, uint16\_t char\_handle, [GATT\_DB\_UUID\_TYPE](#_CPPv417GATT_DB_UUID_TYPE "GATT_DB_UUID_TYPE") \*desc\_uuid, uint16\_t perm, [ATT\_VALUE](#_CPPv49ATT_VALUE "ATT_VALUE") \*desc\_value)
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
    :   - **service\_handle, :** – service handle, get from bk\_ble\_gatt\_db\_add\_service
        - **char\_handle, :** – get from bk\_ble\_gatt\_db\_add\_characteristic
        - **desc\_uuid, :** – characteristic’s uuid, in ATT\_UUID16 or [ATT\_UUID128](#structATT__UUID128), see [GATT\_DB\_UUID\_TYPE](#structGATT__DB__UUID__TYPE)
        - **perm, :** – permission, such as GATT\_DB\_PERM\_READ GATT\_DB\_PERM\_WRITE
        - **desc\_value, :** – att data, see [ATT\_VALUE](#structATT__VALUE)

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv428bk_ble_gatt_db_add_completedv"></a>

<a id="_CPPv328bk_ble_gatt_db_add_completedv"></a> <a id="_CPPv228bk_ble_gatt_db_add_completedv"></a> <a id="bk_ble_gatt_db_add_completed__void"></a> <a id="group__bk__dm__ble__api__v1_1gacfd8e251f076e541a5bf7907c62fa07e"></a> [ble\_err\_t](ble.md#_CPPv49ble_err_t "ble_err_t") bk\_ble\_gatt\_db\_add\_completed(void)
:   call when gatt db add completed

    **Attention**
    :   1.you must wait callback status, 0 mean success.

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv427bk_ble_gatt_db_set_callback22ble_gatt_db_callback_t"></a>

<a id="_CPPv327bk_ble_gatt_db_set_callback22ble_gatt_db_callback_t"></a> <a id="_CPPv227bk_ble_gatt_db_set_callback22ble_gatt_db_callback_t"></a> <a id="bk_ble_gatt_db_set_callback__ble_gatt_db_callback_t"></a> <a id="group__bk__dm__ble__api__v1_1gac7d20b5a390d5fdd9a9a1d4205c0b475"></a> [ble\_err\_t](ble.md#_CPPv49ble_err_t "ble_err_t") bk\_ble\_gatt\_db\_set\_callback([ble\_gatt\_db\_callback\_t](#_CPPv422ble_gatt_db_callback_t "ble_gatt_db_callback_t") hndlr\_cb)
:   set callback, when recv write read req

    **Attention**
    :   1.you must wait callback status, 0 mean success.

    参数
    :   **hndlr\_cb, :** – callback, see ble\_gatt\_db\_callback\_t

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv421bk_ble_gatt_read_resp7uint8_tP7uint8_t8uint16_t"></a>

<a id="_CPPv321bk_ble_gatt_read_resp7uint8_tP7uint8_t8uint16_t"></a> <a id="_CPPv221bk_ble_gatt_read_resp7uint8_tP7uint8_t8uint16_t"></a> <a id="bk_ble_gatt_read_resp__uint8_t.uint8_tP.uint16_t"></a> <a id="group__bk__dm__ble__api__v1_1gaf7acd4ec96f2190002687031524f366f"></a> [ble\_err\_t](ble.md#_CPPv49ble_err_t "ble_err_t") bk\_ble\_gatt\_read\_resp(uint8\_t conn\_handle, uint8\_t \*value, uint16\_t length)
:   When recv GATT\_DB\_CHAR\_PEER\_READ\_REQ, async response.

    **Attention**
    :   1.you must wait callback status, 0 mean success.

    参数
    :   - **conn\_handle, :** – connection handle
        - **value, :** – a point to buffer
        - **length, :** – buffer len

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv418bk_ble_send_notify7uint8_t8uint16_t8uint16_tP7uint8_t8uint16_t"></a>

<a id="_CPPv318bk_ble_send_notify7uint8_t8uint16_t8uint16_tP7uint8_t8uint16_t"></a> <a id="_CPPv218bk_ble_send_notify7uint8_t8uint16_t8uint16_tP7uint8_t8uint16_t"></a> <a id="bk_ble_send_notify__uint8_t.uint16_t.uint16_t.uint8_tP.uint16_t"></a> <a id="group__bk__dm__ble__api__v1_1gaff104a99a71a7cdc69010a3260275ed5"></a> [ble\_err\_t](ble.md#_CPPv49ble_err_t "ble_err_t") bk\_ble\_send\_notify(uint8\_t conn\_handle, uint16\_t service\_handle, uint16\_t char\_handle, uint8\_t \*data, uint16\_t len)
:   send notify when recv enable notify

    **Attention**
    :   1.you must wait callback status, 0 mean success.

    参数
    :   - **conn\_handle, :** – connection handle
        - **adv** – service\_handle: from bk\_ble\_gatt\_db\_add\_service
        - **char\_handle, :** – get from bk\_ble\_gatt\_db\_add\_characteristic
        - **data, :** – a point to buffer
        - **len, :** – buffer len

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv424bk_ble_gatt_get_char_valP14GATT_DB_HANDLEP9ATT_VALUE"></a>

<a id="_CPPv324bk_ble_gatt_get_char_valP14GATT_DB_HANDLEP9ATT_VALUE"></a> <a id="_CPPv224bk_ble_gatt_get_char_valP14GATT_DB_HANDLEP9ATT_VALUE"></a> <a id="bk_ble_gatt_get_char_val__GATT_DB_HANDLEP.ATT_VALUEP"></a> <a id="group__bk__dm__ble__api__v1_1ga17173b45b2682f0fde2e18bcd60dc2e3"></a> [ble\_err\_t](ble.md#_CPPv49ble_err_t "ble_err_t") bk\_ble\_gatt\_get\_char\_val([GATT\_DB\_HANDLE](#_CPPv414GATT_DB_HANDLE "GATT_DB_HANDLE") \*handle, [ATT\_VALUE](#_CPPv49ATT_VALUE "ATT_VALUE") \*attr\_value)
:   get db value

    **Attention**
    :   1.you must wait callback status, 0 mean success.

    参数
    :   - **handle, :** – handle
        - **attr\_value, :** – attr

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv422bk_ble_set_random_addrP9bd_addr_t12ble_cmd_cb_t"></a>

<a id="_CPPv322bk_ble_set_random_addrP9bd_addr_t12ble_cmd_cb_t"></a> <a id="_CPPv222bk_ble_set_random_addrP9bd_addr_t12ble_cmd_cb_t"></a> <a id="bk_ble_set_random_addr__bd_addr_tP.ble_cmd_cb_t"></a> <a id="group__bk__dm__ble__api__v1_1gaff6a94e5e18aa9d1d5b0f305872716d0"></a> [ble\_err\_t](ble.md#_CPPv49ble_err_t "ble_err_t") bk\_ble\_set\_random\_addr([bd\_addr\_t](ble.md#_CPPv49bd_addr_t "bd_addr_t") \*addr, [ble\_cmd\_cb\_t](ble.md#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)
:   set random addr

    **Attention**
    :   1.you must wait callback status, 0 mean success.

        2.this api must call after bk\_ble\_set\_advertising\_params now !

    参数
    :   - **addr, :** – addr
        - **callback, :** – register a callback for this action, ble\_cmd\_t: BLE\_SET\_RANDOM\_ADDR

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv431bk_ble_update_connection_paramsP23ble_update_conn_param_t"></a>

<a id="_CPPv331bk_ble_update_connection_paramsP23ble_update_conn_param_t"></a> <a id="_CPPv231bk_ble_update_connection_paramsP23ble_update_conn_param_t"></a> <a id="bk_ble_update_connection_params__ble_update_conn_param_tP"></a> <a id="group__bk__dm__ble__api__v1_1ga0156eeb613b1b5453a117824ece71cf6"></a> [ble\_err\_t](ble.md#_CPPv49ble_err_t "ble_err_t") bk\_ble\_update\_connection\_params([ble\_update\_conn\_param\_t](#_CPPv423ble_update_conn_param_t "ble_update_conn_param_t") \*conn\_param)
:   update connection param, result as BK\_DM\_BLE\_EVENT\_CONN\_UPDATA

    **Attention**
    :   1.you must wait callback status, 0 mean success.

        2.you don’t need to wait BK\_DM\_BLE\_EVENT\_CONN\_UPDATA because it is an aysnc procedure.

    参数
    :   **conn\_param, :** – [ble\_update\_conn\_param\_t](#structble__update__conn__param__t)

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="api-typedefs"></a>

## API Typedefs

<a id="id1"></a>

### Header File

- [dm\_ble\_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/dm_ble_types.h)

<a id="unions"></a>

### Unions

<a id="_CPPv48ATT_UUID"></a>

<a id="_CPPv38ATT_UUID"></a> <a id="_CPPv28ATT_UUID"></a> <a id="unionATT__UUID"></a> union ATT\_UUID
:   *#include \<dm\_ble\_types.h\>*

    att uuid struct

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N8ATT_UUID7uuid_16E"></a>

    <a id="_CPPv3N8ATT_UUID7uuid_16E"></a> <a id="_CPPv2N8ATT_UUID7uuid_16E"></a> <a id="ATT_UUID::uuid_16__ATT_UUID16"></a> <a id="unionATT__UUID_1ae65afca15eb0a51e8dc34fa6092927bd"></a> [ATT\_UUID16](#_CPPv410ATT_UUID16 "ATT_UUID16") uuid\_16

    <a id="_CPPv4N8ATT_UUID8uuid_128E"></a>

    <a id="_CPPv3N8ATT_UUID8uuid_128E"></a> <a id="_CPPv2N8ATT_UUID8uuid_128E"></a> <a id="ATT_UUID::uuid_128__ATT_UUID128"></a> <a id="unionATT__UUID_1a28bb258a788b94cc2f9fb604228e9595"></a> [ATT\_UUID128](#_CPPv411ATT_UUID128 "ATT_UUID128") uuid\_128

<a id="structures"></a>

### Structures

<a id="_CPPv411ATT_UUID128"></a>

<a id="_CPPv311ATT_UUID128"></a> <a id="_CPPv211ATT_UUID128"></a> <a id="ATT_UUID128"></a> <a id="structATT__UUID128"></a> struct ATT\_UUID128
:   Abstracts 128 Bit UUID.

<a id="_CPPv49ATT_VALUE"></a>

<a id="_CPPv39ATT_VALUE"></a> <a id="_CPPv29ATT_VALUE"></a> <a id="ATT_VALUE"></a> <a id="structATT__VALUE"></a> struct ATT\_VALUE
:   att value struct

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N9ATT_VALUE3valE"></a>

    <a id="_CPPv3N9ATT_VALUE3valE"></a> <a id="_CPPv2N9ATT_VALUE3valE"></a> <a id="ATT_VALUE::val__uint8_tP"></a> <a id="structATT__VALUE_1abd410953c1fda35779423d1d93f3da53"></a> uint8\_t \*val
    :   Value to be packed

    <a id="_CPPv4N9ATT_VALUE3lenE"></a>

    <a id="_CPPv3N9ATT_VALUE3lenE"></a> <a id="_CPPv2N9ATT_VALUE3lenE"></a> <a id="ATT_VALUE::len__uint16_t"></a> <a id="structATT__VALUE_1af62ada316b52725c2e924ecf8186f51c"></a> uint16\_t len
    :   Length of Value

    <a id="_CPPv4N9ATT_VALUE10actual_lenE"></a>

    <a id="_CPPv3N9ATT_VALUE10actual_lenE"></a> <a id="_CPPv2N9ATT_VALUE10actual_lenE"></a> <a id="ATT_VALUE::actual_len__uint16_t"></a> <a id="structATT__VALUE_1abea394d7bf395153ea34395d86341207"></a> uint16\_t actual\_len
    :   Out Parameter Indicating Actual Length Packed

<a id="_CPPv421ATT_HANDLE_VALUE_PAIR"></a>

<a id="_CPPv321ATT_HANDLE_VALUE_PAIR"></a> <a id="_CPPv221ATT_HANDLE_VALUE_PAIR"></a> <a id="ATT_HANDLE_VALUE_PAIR"></a> <a id="structATT__HANDLE__VALUE__PAIR"></a> struct ATT\_HANDLE\_VALUE\_PAIR
:   Abstracts Handle Value Pair This is used in multiple PDUs \- see ATT\_WRITE\_REQ\_PARAM, ATT\_WRITE\_CMD\_PARAM etc.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N21ATT_HANDLE_VALUE_PAIR5valueE"></a>

    <a id="_CPPv3N21ATT_HANDLE_VALUE_PAIR5valueE"></a> <a id="_CPPv2N21ATT_HANDLE_VALUE_PAIR5valueE"></a> <a id="ATT_HANDLE_VALUE_PAIR::value__ATT_VALUE"></a> <a id="structATT__HANDLE__VALUE__PAIR_1a9256eb851cc4331a9722d3562a256fac"></a> [ATT\_VALUE](#_CPPv49ATT_VALUE "ATT_VALUE") value
    :   Attribute Value

    <a id="_CPPv4N21ATT_HANDLE_VALUE_PAIR6handleE"></a>

    <a id="_CPPv3N21ATT_HANDLE_VALUE_PAIR6handleE"></a> <a id="_CPPv2N21ATT_HANDLE_VALUE_PAIR6handleE"></a> <a id="ATT_HANDLE_VALUE_PAIR::handle__ATT_ATTR_HANDLE"></a> <a id="structATT__HANDLE__VALUE__PAIR_1a87d7b070ea19db27cb084c298fc77925"></a> [ATT\_ATTR\_HANDLE](#_CPPv415ATT_ATTR_HANDLE "ATT_ATTR_HANDLE") handle
    :   Attribute Handle

<a id="_CPPv410ATT_HANDLE"></a>

<a id="_CPPv310ATT_HANDLE"></a> <a id="_CPPv210ATT_HANDLE"></a> <a id="ATT_HANDLE"></a> <a id="structATT__HANDLE"></a> struct ATT\_HANDLE
:   ATT Handle.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N10ATT_HANDLE9device_idE"></a>

    <a id="_CPPv3N10ATT_HANDLE9device_idE"></a> <a id="_CPPv2N10ATT_HANDLE9device_idE"></a> <a id="ATT_HANDLE::device_id__DEVICE_HANDLE"></a> <a id="structATT__HANDLE_1a2321cd37aeb10e873692851a5ba00cf1"></a> [DEVICE\_HANDLE](#_CPPv413DEVICE_HANDLE "DEVICE_HANDLE") device\_id
    :   Identifies the peer instance

    <a id="_CPPv4N10ATT_HANDLE6att_idE"></a>

    <a id="_CPPv3N10ATT_HANDLE6att_idE"></a> <a id="_CPPv2N10ATT_HANDLE6att_idE"></a> <a id="ATT_HANDLE::att_id__ATT_CON_ID"></a> <a id="structATT__HANDLE_1ac1c0cc77bca9f3ccca85ecee2e50986f"></a> [ATT\_CON\_ID](#_CPPv410ATT_CON_ID "ATT_CON_ID") att\_id
    :   Identifies the ATT Instance

<a id="_CPPv416ATT_HANDLE_RANGE"></a>

<a id="_CPPv316ATT_HANDLE_RANGE"></a> <a id="_CPPv216ATT_HANDLE_RANGE"></a> <a id="ATT_HANDLE_RANGE"></a> <a id="structATT__HANDLE__RANGE"></a> struct ATT\_HANDLE\_RANGE
:   ATT range.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N16ATT_HANDLE_RANGE12start_handleE"></a>

    <a id="_CPPv3N16ATT_HANDLE_RANGE12start_handleE"></a> <a id="_CPPv2N16ATT_HANDLE_RANGE12start_handleE"></a> <a id="ATT_HANDLE_RANGE::start_handle__ATT_ATTR_HANDLE"></a> <a id="structATT__HANDLE__RANGE_1af60067e9dd03e6646db4cf7551e21b6b"></a> [ATT\_ATTR\_HANDLE](#_CPPv415ATT_ATTR_HANDLE "ATT_ATTR_HANDLE") start\_handle
    :   Start Handle

    <a id="_CPPv4N16ATT_HANDLE_RANGE10end_handleE"></a>

    <a id="_CPPv3N16ATT_HANDLE_RANGE10end_handleE"></a> <a id="_CPPv2N16ATT_HANDLE_RANGE10end_handleE"></a> <a id="ATT_HANDLE_RANGE::end_handle__ATT_ATTR_HANDLE"></a> <a id="structATT__HANDLE__RANGE_1a53b0a753e56bf09b6be642e0373d349f"></a> [ATT\_ATTR\_HANDLE](#_CPPv415ATT_ATTR_HANDLE "ATT_ATTR_HANDLE") end\_handle
    :   End Handle

<a id="_CPPv417GATT_DB_UUID_TYPE"></a>

<a id="_CPPv317GATT_DB_UUID_TYPE"></a> <a id="_CPPv217GATT_DB_UUID_TYPE"></a> <a id="GATT_DB_UUID_TYPE"></a> <a id="structGATT__DB__UUID__TYPE"></a> struct GATT\_DB\_UUID\_TYPE
:   gatt db uuid type

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N17GATT_DB_UUID_TYPE11uuid_formatE"></a>

    <a id="_CPPv3N17GATT_DB_UUID_TYPE11uuid_formatE"></a> <a id="_CPPv2N17GATT_DB_UUID_TYPE11uuid_formatE"></a> <a id="GATT_DB_UUID_TYPE::uuid_format__uint8_t"></a> <a id="structGATT__DB__UUID__TYPE_1a40b7eec37fe12e83b776b36d12aa6f49"></a> uint8\_t uuid\_format
    :   Format indicating, 16 bit or 128 bit UUIDs, see ATT\_16\_BIT\_UUID\_FORMAT ATT\_128\_BIT\_UUID\_FORMAT.

    <a id="_CPPv4N17GATT_DB_UUID_TYPE4uuidE"></a>

    <a id="_CPPv3N17GATT_DB_UUID_TYPE4uuidE"></a> <a id="_CPPv2N17GATT_DB_UUID_TYPE4uuidE"></a> <a id="GATT_DB_UUID_TYPE::uuid__ATT_UUID"></a> <a id="structGATT__DB__UUID__TYPE_1a796adea3d7c3b811af2dae09b8ce28eb"></a> [ATT\_UUID](#_CPPv48ATT_UUID "ATT_UUID") uuid
    :   Attribute UUID.

<a id="_CPPv420GATT_DB_SERVICE_INFO"></a>

<a id="_CPPv320GATT_DB_SERVICE_INFO"></a> <a id="_CPPv220GATT_DB_SERVICE_INFO"></a> <a id="GATT_DB_SERVICE_INFO"></a> <a id="structGATT__DB__SERVICE__INFO"></a> struct GATT\_DB\_SERVICE\_INFO
:   used in [bk\_ble\_gatt\_db\_add\_service](#group__bk__dm__ble__api__v1_1gae22cd028b7b7b834f0136a4b7fac339e)

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N20GATT_DB_SERVICE_INFO4uuidE"></a>

    <a id="_CPPv3N20GATT_DB_SERVICE_INFO4uuidE"></a> <a id="_CPPv2N20GATT_DB_SERVICE_INFO4uuidE"></a> <a id="GATT_DB_SERVICE_INFO::uuid__GATT_DB_UUID_TYPE"></a> <a id="structGATT__DB__SERVICE__INFO_1a8a4d517e92635a46f3e361962a4d0631"></a> [GATT\_DB\_UUID\_TYPE](#_CPPv417GATT_DB_UUID_TYPE "GATT_DB_UUID_TYPE") uuid
    :   UUID, see [GATT\_DB\_UUID\_TYPE](#structGATT__DB__UUID__TYPE)

    <a id="_CPPv4N20GATT_DB_SERVICE_INFO10is_primaryE"></a>

    <a id="_CPPv3N20GATT_DB_SERVICE_INFO10is_primaryE"></a> <a id="_CPPv2N20GATT_DB_SERVICE_INFO10is_primaryE"></a> <a id="GATT_DB_SERVICE_INFO::is_primary__uint8_t"></a> <a id="structGATT__DB__SERVICE__INFO_1a37433615364f7eb202bf7af423bd00cb"></a> uint8\_t is\_primary
    :   If this service is primary or not

    <a id="_CPPv4N20GATT_DB_SERVICE_INFO7sec_reqE"></a>

    <a id="_CPPv3N20GATT_DB_SERVICE_INFO7sec_reqE"></a> <a id="_CPPv2N20GATT_DB_SERVICE_INFO7sec_reqE"></a> <a id="GATT_DB_SERVICE_INFO::sec_req__GATT_DB_SERVICE_DESC"></a> <a id="structGATT__DB__SERVICE__INFO_1acee9dc88eeae0b8b633d3beabbeea79e"></a> [GATT\_DB\_SERVICE\_DESC](#_CPPv420GATT_DB_SERVICE_DESC "GATT_DB_SERVICE_DESC") sec\_req
    :   Security Requrirements for the Service Logical OR of desired combinations of

        1. Security Mode
        2. Security Level
        3. Encryption Key Size

        Acceptable values for Security Mode are: [GATT\_DB\_SER\_SECURITY\_MODE1](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da74841772cdaba7022c4c0350846e928c) [GATT\_DB\_SER\_SECURITY\_MODE2](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da7459a951c37cece87b3bf40773884978)

        Acceptable values for Security Level are: [GATT\_DB\_SER\_SECURITY\_LEVEL1](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da97297f1172c56e0335ada7ec9a95523f) [GATT\_DB\_SER\_SECURITY\_LEVEL2](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035daeee0be171bf53f0b5e9394163254b85c) [GATT\_DB\_SER\_SECURITY\_LEVEL3](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da43c32dae35af6c45c3e6e3a9b7b8697a)

        Acceptable values for Encryption Key Size are: [GATT\_DB\_SER\_ENCRYPT\_KEY\_SIZE\_7](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035daf26237278d04eb8e0f0b6d458e4101a8) [GATT\_DB\_SER\_ENCRYPT\_KEY\_SIZE\_8](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da578f242314247aabe4766585b213935d) [GATT\_DB\_SER\_ENCRYPT\_KEY\_SIZE\_9](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da0b721e086f412de7f0b881434193421f) [GATT\_DB\_SER\_ENCRYPT\_KEY\_SIZE\_10](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da0af0e5686c4872b497be8568ec7c8ad7) [GATT\_DB\_SER\_ENCRYPT\_KEY\_SIZE\_11](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da22ae7f4b2be7c145dd54d8f58720041f) [GATT\_DB\_SER\_ENCRYPT\_KEY\_SIZE\_12](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da62c6ca9b86cda66475dc31c721f31ee5) [GATT\_DB\_SER\_ENCRYPT\_KEY\_SIZE\_13](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035dada15fde570ee125f1e273c0e15416ac0) [GATT\_DB\_SER\_ENCRYPT\_KEY\_SIZE\_14](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035daae41a9c45197bf1897c25206b7833552) [GATT\_DB\_SER\_ENCRYPT\_KEY\_SIZE\_15](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da0f7f2aac54861fbefd0054f3ac911fa2) [GATT\_DB\_SER\_ENCRYPT\_KEY\_SIZE\_16](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da15388d866bc04cfba206ce44726d6e0e) When the Service does not mandate any specific Key size [GATT\_DB\_SER\_ENC\_KEY\_SIZE\_DONT\_CARE](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da9d8f85a9e69bab3d04f0c9c035bc20df) shall be used.

        When No Security is mandated for the service Value [GATT\_DB\_SER\_NO\_SECURITY\_PROPERTY](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035dab307287b35dec27c88ec7030aca6fb84) shall be used.

    <a id="_CPPv4N20GATT_DB_SERVICE_INFO8link_reqE"></a>

    <a id="_CPPv3N20GATT_DB_SERVICE_INFO8link_reqE"></a> <a id="_CPPv2N20GATT_DB_SERVICE_INFO8link_reqE"></a> <a id="GATT_DB_SERVICE_INFO::link_req__GATT_DB_SERVICE_DESC"></a> <a id="structGATT__DB__SERVICE__INFO_1a9cc5353f34282f7abe3abf4f0210f990"></a> [GATT\_DB\_SERVICE\_DESC](#_CPPv420GATT_DB_SERVICE_DESC "GATT_DB_SERVICE_DESC") link\_req
    :   Transport Requrirements for the Service. This describes the Transport on which this required to be operational. GATT\_DB\_SER\_SUPPORT\_ANY\_LINK\_TYPE GATT\_DB\_SER\_SUPPORT\_LE\_LINK\_TYPE GATT\_DB\_SER\_SUPPORT\_BR\_LINK\_TYPE

<a id="_CPPv414GATT_DB_HANDLE"></a>

<a id="_CPPv314GATT_DB_HANDLE"></a> <a id="_CPPv214GATT_DB_HANDLE"></a> <a id="GATT_DB_HANDLE"></a> <a id="structGATT__DB__HANDLE"></a> struct GATT\_DB\_HANDLE
:   GATT db handle.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N14GATT_DB_HANDLE9device_idE"></a>

    <a id="_CPPv3N14GATT_DB_HANDLE9device_idE"></a> <a id="_CPPv2N14GATT_DB_HANDLE9device_idE"></a> <a id="GATT_DB_HANDLE::device_id__DEVICE_HANDLE"></a> <a id="structGATT__DB__HANDLE_1a0aa4f35e5832d3dc46c0497b311f941e"></a> [DEVICE\_HANDLE](#_CPPv413DEVICE_HANDLE "DEVICE_HANDLE") device\_id
    :   Identifies the peer accessing the database

    <a id="_CPPv4N14GATT_DB_HANDLE10service_idE"></a>

    <a id="_CPPv3N14GATT_DB_HANDLE10service_idE"></a> <a id="_CPPv2N14GATT_DB_HANDLE10service_idE"></a> <a id="GATT_DB_HANDLE::service_id__uint8_t"></a> <a id="structGATT__DB__HANDLE_1a812de01dfed380722bc52d62a7e42d1f"></a> uint8\_t service\_id
    :   Identifies the Service being Accessed

    <a id="_CPPv4N14GATT_DB_HANDLE7char_idE"></a>

    <a id="_CPPv3N14GATT_DB_HANDLE7char_idE"></a> <a id="_CPPv2N14GATT_DB_HANDLE7char_idE"></a> <a id="GATT_DB_HANDLE::char_id__uint8_t"></a> <a id="structGATT__DB__HANDLE_1aecd20dc0bcc3865994d1e5d685e9cd66"></a> uint8\_t char\_id
    :   Identifies the Characteristic being Accessed

<a id="_CPPv414GATT_DB_PARAMS"></a>

<a id="_CPPv314GATT_DB_PARAMS"></a> <a id="_CPPv214GATT_DB_PARAMS"></a> <a id="GATT_DB_PARAMS"></a> <a id="structGATT__DB__PARAMS"></a> struct GATT\_DB\_PARAMS
:   GATT db param.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N14GATT_DB_PARAMS5valueE"></a>

    <a id="_CPPv3N14GATT_DB_PARAMS5valueE"></a> <a id="_CPPv2N14GATT_DB_PARAMS5valueE"></a> <a id="GATT_DB_PARAMS::value__ATT_VALUE"></a> <a id="structGATT__DB__PARAMS_1a5164929f3be039ddbbbeebca07ff62aa"></a> [ATT\_VALUE](#_CPPv49ATT_VALUE "ATT_VALUE") value
    :   Abstracts Value to get/set the Attribute Value

    <a id="_CPPv4N14GATT_DB_PARAMS6handleE"></a>

    <a id="_CPPv3N14GATT_DB_PARAMS6handleE"></a> <a id="_CPPv2N14GATT_DB_PARAMS6handleE"></a> <a id="GATT_DB_PARAMS::handle__ATT_ATTR_HANDLE"></a> <a id="structGATT__DB__PARAMS_1ac2af73aa086bf9c98333de44fb723911"></a> [ATT\_ATTR\_HANDLE](#_CPPv415ATT_ATTR_HANDLE "ATT_ATTR_HANDLE") handle
    :   Abstracts the handle information

    <a id="_CPPv4N14GATT_DB_PARAMS5db_opE"></a>

    <a id="_CPPv3N14GATT_DB_PARAMS5db_opE"></a> <a id="_CPPv2N14GATT_DB_PARAMS5db_opE"></a> <a id="GATT_DB_PARAMS::db_op__GATT_DB_OPERATION"></a> <a id="structGATT__DB__PARAMS_1a52300bb450939f02fe8303cf86cd2521"></a> [GATT\_DB\_OPERATION](#_CPPv417GATT_DB_OPERATION "GATT_DB_OPERATION") db\_op
    :   Abstracts the Access Operation, such as [GATT\_DB\_CHAR\_PEER\_READ\_REQ](#group__gatt__db__operations_1ggabed82baf7f470b522273a3e37c24c600a61a516866cd39e8f02f29096ae3f191a)

        **Attention**
        :   when recv GATT\_DB\_CHAR\_PEER\_READ\_REQ and you dont want response immediately, return GATT\_DB\_DELAYED\_RESPONSE in ble\_gatt\_db\_callback\_t

<a id="_CPPv418GATT_SERVICE_PARAM"></a>

<a id="_CPPv318GATT_SERVICE_PARAM"></a> <a id="_CPPv218GATT_SERVICE_PARAM"></a> <a id="GATT_SERVICE_PARAM"></a> <a id="structGATT__SERVICE__PARAM"></a> struct GATT\_SERVICE\_PARAM
:   gatt Service param

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18GATT_SERVICE_PARAM4uuidE"></a>

    <a id="_CPPv3N18GATT_SERVICE_PARAM4uuidE"></a> <a id="_CPPv2N18GATT_SERVICE_PARAM4uuidE"></a> <a id="GATT_SERVICE_PARAM::uuid__ATT_UUID"></a> <a id="structGATT__SERVICE__PARAM_1ad6c706a65d5c6b0567d87e334de8c727"></a> [ATT\_UUID](#_CPPv48ATT_UUID "ATT_UUID") uuid
    :   Service UUID

    <a id="_CPPv4N18GATT_SERVICE_PARAM9uuid_typeE"></a>

    <a id="_CPPv3N18GATT_SERVICE_PARAM9uuid_typeE"></a> <a id="_CPPv2N18GATT_SERVICE_PARAM9uuid_typeE"></a> <a id="GATT_SERVICE_PARAM::uuid_type__uint8_t"></a> <a id="structGATT__SERVICE__PARAM_1ad672dc27baa64cf892d08b54f9472957"></a> uint8\_t uuid\_type
    :   Service UUID Type

    <a id="_CPPv4N18GATT_SERVICE_PARAM5rangeE"></a>

    <a id="_CPPv3N18GATT_SERVICE_PARAM5rangeE"></a> <a id="_CPPv2N18GATT_SERVICE_PARAM5rangeE"></a> <a id="GATT_SERVICE_PARAM::range__ATT_HANDLE_RANGE"></a> <a id="structGATT__SERVICE__PARAM_1a89e4efdab5dc9630ac183a7479fe869d"></a> [ATT\_HANDLE\_RANGE](#_CPPv416ATT_HANDLE_RANGE "ATT_HANDLE_RANGE") range
    :   Service Range

<a id="_CPPv420GATT_CHAR_DESC_PARAM"></a>

<a id="_CPPv320GATT_CHAR_DESC_PARAM"></a> <a id="_CPPv220GATT_CHAR_DESC_PARAM"></a> <a id="GATT_CHAR_DESC_PARAM"></a> <a id="structGATT__CHAR__DESC__PARAM"></a> struct GATT\_CHAR\_DESC\_PARAM
:   gatt Characteristic Descriptor Information

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N20GATT_CHAR_DESC_PARAM6handleE"></a>

    <a id="_CPPv3N20GATT_CHAR_DESC_PARAM6handleE"></a> <a id="_CPPv2N20GATT_CHAR_DESC_PARAM6handleE"></a> <a id="GATT_CHAR_DESC_PARAM::handle__ATT_ATTR_HANDLE"></a> <a id="structGATT__CHAR__DESC__PARAM_1adb27267856e966640133f1888b884fd5"></a> [ATT\_ATTR\_HANDLE](#_CPPv415ATT_ATTR_HANDLE "ATT_ATTR_HANDLE") handle
    :   Descriptor handle

    <a id="_CPPv4N20GATT_CHAR_DESC_PARAM4uuidE"></a>

    <a id="_CPPv3N20GATT_CHAR_DESC_PARAM4uuidE"></a> <a id="_CPPv2N20GATT_CHAR_DESC_PARAM4uuidE"></a> <a id="GATT_CHAR_DESC_PARAM::uuid__ATT_UUID"></a> <a id="structGATT__CHAR__DESC__PARAM_1ac25095e0723da29933adc798e7386e80"></a> [ATT\_UUID](#_CPPv48ATT_UUID "ATT_UUID") uuid
    :   Descriptor UUID

    <a id="_CPPv4N20GATT_CHAR_DESC_PARAM9uuid_typeE"></a>

    <a id="_CPPv3N20GATT_CHAR_DESC_PARAM9uuid_typeE"></a> <a id="_CPPv2N20GATT_CHAR_DESC_PARAM9uuid_typeE"></a> <a id="GATT_CHAR_DESC_PARAM::uuid_type__uint8_t"></a> <a id="structGATT__CHAR__DESC__PARAM_1ab97c51d969f08f5df8032c6d9ecd227b"></a> uint8\_t uuid\_type
    :   Descriptor UUID Type

<a id="_CPPv425GATT_CHARACTERISTIC_PARAM"></a>

<a id="_CPPv325GATT_CHARACTERISTIC_PARAM"></a> <a id="_CPPv225GATT_CHARACTERISTIC_PARAM"></a> <a id="GATT_CHARACTERISTIC_PARAM"></a> <a id="structGATT__CHARACTERISTIC__PARAM"></a> struct GATT\_CHARACTERISTIC\_PARAM
:   gatt Characteristic Information

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N25GATT_CHARACTERISTIC_PARAM5rangeE"></a>

    <a id="_CPPv3N25GATT_CHARACTERISTIC_PARAM5rangeE"></a> <a id="_CPPv2N25GATT_CHARACTERISTIC_PARAM5rangeE"></a> <a id="GATT_CHARACTERISTIC_PARAM::range__ATT_HANDLE_RANGE"></a> <a id="structGATT__CHARACTERISTIC__PARAM_1a84a445cf133458947ffcba0f4a61b106"></a> [ATT\_HANDLE\_RANGE](#_CPPv416ATT_HANDLE_RANGE "ATT_HANDLE_RANGE") range
    :   Characteristic Range

    <a id="_CPPv4N25GATT_CHARACTERISTIC_PARAM9cpropertyE"></a>

    <a id="_CPPv3N25GATT_CHARACTERISTIC_PARAM9cpropertyE"></a> <a id="_CPPv2N25GATT_CHARACTERISTIC_PARAM9cpropertyE"></a> <a id="GATT_CHARACTERISTIC_PARAM::cproperty__uint8_t"></a> <a id="structGATT__CHARACTERISTIC__PARAM_1a3636e5decc3ddb0b2be2b05860a8ff82"></a> uint8\_t cproperty
    :   Characteristic Property

    <a id="_CPPv4N25GATT_CHARACTERISTIC_PARAM12value_handleE"></a>

    <a id="_CPPv3N25GATT_CHARACTERISTIC_PARAM12value_handleE"></a> <a id="_CPPv2N25GATT_CHARACTERISTIC_PARAM12value_handleE"></a> <a id="GATT_CHARACTERISTIC_PARAM::value_handle__ATT_ATTR_HANDLE"></a> <a id="structGATT__CHARACTERISTIC__PARAM_1ae3692a967f611624f0d9065486b545dc"></a> [ATT\_ATTR\_HANDLE](#_CPPv415ATT_ATTR_HANDLE "ATT_ATTR_HANDLE") value\_handle
    :   Characteristic Value Handle

    <a id="_CPPv4N25GATT_CHARACTERISTIC_PARAM4uuidE"></a>

    <a id="_CPPv3N25GATT_CHARACTERISTIC_PARAM4uuidE"></a> <a id="_CPPv2N25GATT_CHARACTERISTIC_PARAM4uuidE"></a> <a id="GATT_CHARACTERISTIC_PARAM::uuid__ATT_UUID"></a> <a id="structGATT__CHARACTERISTIC__PARAM_1a4c9483353f52bfa2a33b3f624e18661a"></a> [ATT\_UUID](#_CPPv48ATT_UUID "ATT_UUID") uuid
    :   Characteristic UUID

    <a id="_CPPv4N25GATT_CHARACTERISTIC_PARAM9uuid_typeE"></a>

    <a id="_CPPv3N25GATT_CHARACTERISTIC_PARAM9uuid_typeE"></a> <a id="_CPPv2N25GATT_CHARACTERISTIC_PARAM9uuid_typeE"></a> <a id="GATT_CHARACTERISTIC_PARAM::uuid_type__uint8_t"></a> <a id="structGATT__CHARACTERISTIC__PARAM_1afa895b8e95ebcf8700b3dc28f7214a68"></a> uint8\_t uuid\_type
    :   Characteristic UUID Type

    <a id="_CPPv4N25GATT_CHARACTERISTIC_PARAM10desc_indexE"></a>

    <a id="_CPPv3N25GATT_CHARACTERISTIC_PARAM10desc_indexE"></a> <a id="_CPPv2N25GATT_CHARACTERISTIC_PARAM10desc_indexE"></a> <a id="GATT_CHARACTERISTIC_PARAM::desc_index__uint8_t"></a> <a id="structGATT__CHARACTERISTIC__PARAM_1aa44e6d7a557034a68895a90395fbd337"></a> uint8\_t desc\_index
    :   ATT\_128\_BIT\_UUID\_FORMAT Characteristic desciptor index

    <a id="_CPPv4N25GATT_CHARACTERISTIC_PARAM10val_offsetE"></a>

    <a id="_CPPv3N25GATT_CHARACTERISTIC_PARAM10val_offsetE"></a> <a id="_CPPv2N25GATT_CHARACTERISTIC_PARAM10val_offsetE"></a> <a id="GATT_CHARACTERISTIC_PARAM::val_offset__uint16_t"></a> <a id="structGATT__CHARACTERISTIC__PARAM_1ae4e4605b092dc15e23e6e59de5b8a6c6"></a> uint16\_t val\_offset
    :   Characteristics Value Offset

    <a id="_CPPv4N25GATT_CHARACTERISTIC_PARAM10val_lengthE"></a>

    <a id="_CPPv3N25GATT_CHARACTERISTIC_PARAM10val_lengthE"></a> <a id="_CPPv2N25GATT_CHARACTERISTIC_PARAM10val_lengthE"></a> <a id="GATT_CHARACTERISTIC_PARAM::val_length__uint16_t"></a> <a id="structGATT__CHARACTERISTIC__PARAM_1aa04b3de6879a734e5ed51fd086a045e7"></a> uint16\_t val\_length
    :   Characteristic Value Length

    <a id="_CPPv4N25GATT_CHARACTERISTIC_PARAM10descriptorE"></a>

    <a id="_CPPv3N25GATT_CHARACTERISTIC_PARAM10descriptorE"></a> <a id="_CPPv2N25GATT_CHARACTERISTIC_PARAM10descriptorE"></a> <a id="GATT_CHARACTERISTIC_PARAM::descriptor__GATT_CHAR_DESC_PARAMA"></a> <a id="structGATT__CHARACTERISTIC__PARAM_1a87d5023bd2d4d535b308858f4bf28cd9"></a> [GATT\_CHAR\_DESC\_PARAM](#_CPPv420GATT_CHAR_DESC_PARAM "GATT_CHAR_DESC_PARAM") descriptor\[GATT\_MAX\_CHAR\_DESCRIPTORS\]
    :   Characteristic descriptor array

<a id="_CPPv419ble_adv_parameter_t"></a>

<a id="_CPPv319ble_adv_parameter_t"></a> <a id="_CPPv219ble_adv_parameter_t"></a> <a id="ble_adv_parameter_t"></a> <a id="structble__adv__parameter__t"></a> struct ble\_adv\_parameter\_t
:   use in [bk\_ble\_set\_advertising\_params](#group__bk__dm__ble__api__v1_1gac82851a90130a907f6a3f58863aae7d5)

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N19ble_adv_parameter_t12adv_intv_minE"></a>

    <a id="_CPPv3N19ble_adv_parameter_t12adv_intv_minE"></a> <a id="_CPPv2N19ble_adv_parameter_t12adv_intv_minE"></a> <a id="ble_adv_parameter_t::adv_intv_min__uint32_t"></a> <a id="structble__adv__parameter__t_1afb16c739324130ae40d85e05281d8844"></a> uint32\_t adv\_intv\_min
    :   Minimum advertising interval (in unit of 625us). Must be greater than or equal to 20ms.

    <a id="_CPPv4N19ble_adv_parameter_t12adv_intv_maxE"></a>

    <a id="_CPPv3N19ble_adv_parameter_t12adv_intv_maxE"></a> <a id="_CPPv2N19ble_adv_parameter_t12adv_intv_maxE"></a> <a id="ble_adv_parameter_t::adv_intv_max__uint32_t"></a> <a id="structble__adv__parameter__t_1a386e1d96b8613cb7848c0c07c29c2a0c"></a> uint32\_t adv\_intv\_max
    :   Maximum advertising interval (in unit of 625us). Must be greater than or equal to 20ms.

    <a id="_CPPv4N19ble_adv_parameter_t8adv_typeE"></a>

    <a id="_CPPv3N19ble_adv_parameter_t8adv_typeE"></a> <a id="_CPPv2N19ble_adv_parameter_t8adv_typeE"></a> <a id="ble_adv_parameter_t::adv_type__uint8_t"></a> <a id="structble__adv__parameter__t_1ae2e483415cf2dff457d90f25e90ca24f"></a> uint8\_t adv\_type
    :   Advertising type, see advertise\_legacy\_type.

    <a id="_CPPv4N19ble_adv_parameter_t13own_addr_typeE"></a>

    <a id="_CPPv3N19ble_adv_parameter_t13own_addr_typeE"></a> <a id="_CPPv2N19ble_adv_parameter_t13own_addr_typeE"></a> <a id="ble_adv_parameter_t::own_addr_type__uint8_t"></a> <a id="structble__adv__parameter__t_1a8719465bf000dcfaa78ef1773d5739e2"></a> uint8\_t own\_addr\_type
    :   Own address type: public\=0 / random\=1 / rpa\_or\_pub\=2 / rpa\_or\_rnd\=3.

    <a id="_CPPv4N19ble_adv_parameter_t12peer_addressE"></a>

    <a id="_CPPv3N19ble_adv_parameter_t12peer_addressE"></a> <a id="_CPPv2N19ble_adv_parameter_t12peer_addressE"></a> <a id="ble_adv_parameter_t::peer_address__bd_addr_t"></a> <a id="structble__adv__parameter__t_1a0bd68bd75e9f8ac25e4ec9f5efe958f4"></a> [bd\_addr\_t](ble.md#_CPPv49bd_addr_t "bd_addr_t") peer\_address
    :   Peer address.

    <a id="_CPPv4N19ble_adv_parameter_t14peer_addr_typeE"></a>

    <a id="_CPPv3N19ble_adv_parameter_t14peer_addr_typeE"></a> <a id="_CPPv2N19ble_adv_parameter_t14peer_addr_typeE"></a> <a id="ble_adv_parameter_t::peer_addr_type__uint8_t"></a> <a id="structble__adv__parameter__t_1afe90f9dd01ea24129108709a0502b116"></a> uint8\_t peer\_addr\_type
    :   Peer address type: public or public identity addr \=0 / RDP or random Identity Addr \=1.

    <a id="_CPPv4N19ble_adv_parameter_t8chnl_mapE"></a>

    <a id="_CPPv3N19ble_adv_parameter_t8chnl_mapE"></a> <a id="_CPPv2N19ble_adv_parameter_t8chnl_mapE"></a> <a id="ble_adv_parameter_t::chnl_map__uint8_t"></a> <a id="structble__adv__parameter__t_1a8d926132c769b61460c86b7f46bb66a1"></a> uint8\_t chnl\_map
    :   Bit field indicating the channel mapping (.

        参见

        enum [adv\_chnl\_map](ble.md#group__bk__ble__api__v1__typedef_1ga57c9e3ee8efb2e8c2fcc35e570f8679a))

    <a id="_CPPv4N19ble_adv_parameter_t13filter_policyE"></a>

    <a id="_CPPv3N19ble_adv_parameter_t13filter_policyE"></a> <a id="_CPPv2N19ble_adv_parameter_t13filter_policyE"></a> <a id="ble_adv_parameter_t::filter_policy__uint16_t"></a> <a id="structble__adv__parameter__t_1a51b64fa42430c06a8c0a5cea017ab6a4"></a> uint16\_t filter\_policy
    :   advertising policy see advertise\_filter\_policy

<a id="_CPPv414ble_conn_att_t"></a>

<a id="_CPPv314ble_conn_att_t"></a> <a id="_CPPv214ble_conn_att_t"></a> <a id="ble_conn_att_t"></a> <a id="structble__conn__att__t"></a> struct ble\_conn\_att\_t
:   use in BK\_DM\_BLE\_EVENT\_CONNECT BK\_DM\_BLE\_EVENT\_DISCONNECT

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N14ble_conn_att_t14peer_addr_typeE"></a>

    <a id="_CPPv3N14ble_conn_att_t14peer_addr_typeE"></a> <a id="_CPPv2N14ble_conn_att_t14peer_addr_typeE"></a> <a id="ble_conn_att_t::peer_addr_type__uint8_t"></a> <a id="structble__conn__att__t_1aaeba1b362bc64a20b2269914d32cca82"></a> uint8\_t peer\_addr\_type
    :   Peer address type.

    <a id="_CPPv4N14ble_conn_att_t9peer_addrE"></a>

    <a id="_CPPv3N14ble_conn_att_t9peer_addrE"></a> <a id="_CPPv2N14ble_conn_att_t9peer_addrE"></a> <a id="ble_conn_att_t::peer_addr__uint8_tA"></a> <a id="structble__conn__att__t_1a3a08b29600af98f0380d44e3a2080503"></a> uint8\_t peer\_addr\[6\]
    :   Peer BT address.

<a id="_CPPv418ble_att_tx_compl_t"></a>

<a id="_CPPv318ble_att_tx_compl_t"></a> <a id="_CPPv218ble_att_tx_compl_t"></a> <a id="ble_att_tx_compl_t"></a> <a id="structble__att__tx__compl__t"></a> struct ble\_att\_tx\_compl\_t
:   use in BK\_DM\_BLE\_EVENT\_TX\_DONE

<a id="_CPPv416ble_att_notify_t"></a>

<a id="_CPPv316ble_att_notify_t"></a> <a id="_CPPv216ble_att_notify_t"></a> <a id="ble_att_notify_t"></a> <a id="structble__att__notify__t"></a> struct ble\_att\_notify\_t
:   use in BK\_DM\_BLE\_EVENT\_RECV\_NOTIFY

<a id="_CPPv427ble_conn_update_param_ind_t"></a>

<a id="_CPPv327ble_conn_update_param_ind_t"></a> <a id="_CPPv227ble_conn_update_param_ind_t"></a> <a id="ble_conn_update_param_ind_t"></a> <a id="structble__conn__update__param__ind__t"></a> struct ble\_conn\_update\_param\_ind\_t
:   use in BK\_DM\_BLE\_EVENT\_CONN\_UPD\_PAR\_ASK

<a id="_CPPv433ble_conn_update_param_compl_ind_t"></a>

<a id="_CPPv333ble_conn_update_param_compl_ind_t"></a> <a id="_CPPv233ble_conn_update_param_compl_ind_t"></a> <a id="ble_conn_update_param_compl_ind_t"></a> <a id="structble__conn__update__param__compl__ind__t"></a> struct ble\_conn\_update\_param\_compl\_ind\_t
:   use in BK\_DM\_BLE\_EVENT\_CONN\_UPDATA

<a id="_CPPv423ble_update_conn_param_t"></a>

<a id="_CPPv323ble_update_conn_param_t"></a> <a id="_CPPv223ble_update_conn_param_t"></a> <a id="ble_update_conn_param_t"></a> <a id="structble__update__conn__param__t"></a> struct ble\_update\_conn\_param\_t
:   use when we need to trigger an update

<a id="_CPPv412ble_att_rw_t"></a>

<a id="_CPPv312ble_att_rw_t"></a> <a id="_CPPv212ble_att_rw_t"></a> <a id="ble_att_rw_t"></a> <a id="structble__att__rw__t"></a> struct ble\_att\_rw\_t
:   use in BK\_DM\_BLE\_EVENT\_ATT\_READ\_RESPONSE

<a id="macros"></a>

### Macros

<a id="c._H_GATT_DEFINES_"></a>

<a id="dm__ble__types_8h_1aa1ecaef05c394bc2188ad8f92975b812"></a> \_H\_GATT\_DEFINES\_

<a id="c.ATT_APPL_PROCEDURE_ALREADY_IN_PROGRESS"></a>

<a id="dm__ble__types_8h_1a579e1b41c27122fc1a1cfed521b8a11e"></a> ATT\_APPL\_PROCEDURE\_ALREADY\_IN\_PROGRESS

<a id="c.ATT_APPL_CCD_IMPROPERLY_CONFIGURED"></a>

<a id="dm__ble__types_8h_1acfbc5a4e42f4cc1bdcc89705fe978d68"></a> ATT\_APPL\_CCD\_IMPROPERLY\_CONFIGURED

<a id="c._H_BT_ERROR_"></a>

<a id="dm__ble__types_8h_1a45271ea44b78f80ce8e947d25b39ee24"></a> \_H\_BT\_ERROR\_
:   *H\_GATT\_DEFINES*

<a id="c.GATT_DB_ERR_ID"></a>

<a id="dm__ble__types_8h_1a68670779bbb6b4a9a40611bde9b1db03"></a> GATT\_DB\_ERR\_ID

<a id="c.GATT_DB_DELAYED_RESPONSE"></a>

<a id="dm__ble__types_8h_1ad0896852c67558063b6ebca1d6816071"></a> GATT\_DB\_DELAYED\_RESPONSE
:   Not an error code. More of a status code

<a id="c.GATT_DB_DONOT_RESPOND"></a>

<a id="dm__ble__types_8h_1afb04764fd90a835c602a9b804b43bab5"></a> GATT\_DB\_DONOT\_RESPOND

<a id="c.GATT_DB_ALREADY_RESPONDED"></a>

<a id="dm__ble__types_8h_1a38bf22ff18be506fe9caa524c099f71e"></a> GATT\_DB\_ALREADY\_RESPONDED

<a id="c._H_BT_DEVICE_QUEUE_"></a>

<a id="dm__ble__types_8h_1a0bb5e1510983e7ed45fb55ee663deff1"></a> \_H\_BT\_DEVICE\_QUEUE\_

<a id="c._H_BT_ATT_API_"></a>

<a id="dm__ble__types_8h_1a3e81611a38621674aa4a0c1b925b90fe"></a> \_H\_BT\_ATT\_API\_

<a id="c.ATT_AUTH_SIGNATURE_SIZE"></a>

<a id="dm__ble__types_8h_1a6d1270795072ec17df75cb56d9bc2809"></a> ATT\_AUTH\_SIGNATURE\_SIZE
:   ATT Default MTU ATT Signature Size in Signed Write

<a id="c.ATT_EXECUTE_WRITE_CANCEL_FLAG"></a>

<a id="dm__ble__types_8h_1a5307cf75382e9393a78de8ea1c68abb8"></a> ATT\_EXECUTE\_WRITE\_CANCEL\_FLAG
:   ATT Execute Write Cancel Flag

<a id="c.ATT_EXECUTE_WRITE_EXEC_FLAG"></a>

<a id="dm__ble__types_8h_1ac51c8aafba415820386267f6df1a201b"></a> ATT\_EXECUTE\_WRITE\_EXEC\_FLAG
:   ATT Execute Write Execute Flag

<a id="c.ATT_16_BIT_UUID_FORMAT"></a>

<a id="dm__ble__types_8h_1a266631e29f4b22eb1d9bf35b73f3aa0b"></a> ATT\_16\_BIT\_UUID\_FORMAT
:   ATT Identification for 16-bit UUID Format

<a id="c.ATT_128_BIT_UUID_FORMAT"></a>

<a id="dm__ble__types_8h_1ab18429f6ce331e78607880d828a77d6e"></a> ATT\_128\_BIT\_UUID\_FORMAT
:   ATT Identification for 128-bit UUID Format

<a id="c.ATT_16_BIT_UUID_SIZE"></a>

<a id="dm__ble__types_8h_1a5cd176782299576eedbd2d835070187d"></a> ATT\_16\_BIT\_UUID\_SIZE
:   ATT 16-bit UUID Size

<a id="c.ATT_128_BIT_UUID_SIZE"></a>

<a id="dm__ble__types_8h_1aa617f10fa73d68b8a46fad9eb0f884af"></a> ATT\_128\_BIT\_UUID\_SIZE
:   ATT 128-bit UUID Size

<a id="c.ATT_CON_ID_INIT_VAL"></a>

<a id="dm__ble__types_8h_1aac271d6c538f96c8dc655bbd5de48d68"></a> ATT\_CON\_ID\_INIT\_VAL
:   ATT Connection Instance Initialization Value.

<a id="c.ATT_APPL_CB_INIT_VAL"></a>

<a id="dm__ble__types_8h_1ae53bec19b981d60b450c932f2c6a5d38"></a> ATT\_APPL\_CB\_INIT\_VAL
:   ATT Application Callback Initialization Value.

<a id="c.ATT_INVALID_ATTR_HANDLE_VAL"></a>

<a id="dm__ble__types_8h_1a6511ba0706f11fe964a0897398c3e1af"></a> ATT\_INVALID\_ATTR\_HANDLE\_VAL
:   ATT Invalid Attribute Handle Value

<a id="c.ATT_ATTR_HANDLE_START_RANGE"></a>

<a id="dm__ble__types_8h_1afa30d67be37775e5f97084d7b7935195"></a> ATT\_ATTR\_HANDLE\_START\_RANGE
:   ATT Attribute Handle Start Range

<a id="c.ATT_ATTR_HANDLE_END_RANGE"></a>

<a id="dm__ble__types_8h_1ab663261ce282dadac68e6840884c9716"></a> ATT\_ATTR\_HANDLE\_END\_RANGE
:   ATT Attribute Handle End Range

<a id="c._H_BT_GATT_DB_API_"></a>

<a id="dm__ble__types_8h_1ac9f52679a2b5f00fd5a529a6176f7794"></a> \_H\_BT\_GATT\_DB\_API\_

<a id="c._H_GATT_"></a>

<a id="dm__ble__types_8h_1a8d4d748c677fa3621c505eaa838a3784"></a> \_H\_GATT\_

<a id="c.GATT_MAX_CHAR_DESCRIPTORS"></a>

<a id="dm__ble__types_8h_1aa38498dfee0880682d17621a4ef7c71e"></a> GATT\_MAX\_CHAR\_DESCRIPTORS

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv410API_RESULT"></a>

<a id="_CPPv310API_RESULT"></a> <a id="_CPPv210API_RESULT"></a> <a id="API_RESULT"></a> <a id="dm__ble__types_8h_1a8540c71f87b4954170645aacd3d28eaf"></a> typedef uint16\_t API\_RESULT

<a id="_CPPv413DEVICE_HANDLE"></a>

<a id="_CPPv313DEVICE_HANDLE"></a> <a id="_CPPv213DEVICE_HANDLE"></a> <a id="DEVICE_HANDLE"></a> <a id="dm__ble__types_8h_1ae967fb1c1b9414b3ae621204880ffdb3"></a> typedef uint8\_t DEVICE\_HANDLE

<a id="_CPPv410ATT_CON_ID"></a>

<a id="_CPPv310ATT_CON_ID"></a> <a id="_CPPv210ATT_CON_ID"></a> <a id="ATT_CON_ID"></a> <a id="dm__ble__types_8h_1a5dae14ce83035fa54b8206ae5673d340"></a> typedef uint8\_t ATT\_CON\_ID

<a id="_CPPv415ATT_ATTR_HANDLE"></a>

<a id="_CPPv315ATT_ATTR_HANDLE"></a> <a id="_CPPv215ATT_ATTR_HANDLE"></a> <a id="ATT_ATTR_HANDLE"></a> <a id="dm__ble__types_8h_1a1e23aec8a207eac39ffd27585be679bf"></a> typedef uint16\_t ATT\_ATTR\_HANDLE
:   ble att protocol handle

<a id="_CPPv410ATT_UUID16"></a>

<a id="_CPPv310ATT_UUID16"></a> <a id="_CPPv210ATT_UUID16"></a> <a id="ATT_UUID16"></a> <a id="dm__ble__types_8h_1a2acc0a75998ef992ec7306f1e5ddb2ac"></a> typedef uint16\_t ATT\_UUID16
:   Abstracts 16 Bit UUID

<a id="_CPPv417GATT_DB_OPERATION"></a>

<a id="_CPPv317GATT_DB_OPERATION"></a> <a id="_CPPv217GATT_DB_OPERATION"></a> <a id="GATT_DB_OPERATION"></a> <a id="dm__ble__types_8h_1a99a59c2999b0c1057f2b150ef15447bb"></a> typedef uint8\_t GATT\_DB\_OPERATION
:   such as GATT\_DB\_CHAR\_VALUE\_READ\_REQ

<a id="_CPPv420GATT_DB_SERVICE_DESC"></a>

<a id="_CPPv320GATT_DB_SERVICE_DESC"></a> <a id="_CPPv220GATT_DB_SERVICE_DESC"></a> <a id="GATT_DB_SERVICE_DESC"></a> <a id="dm__ble__types_8h_1aad26f63723135ed89569199b9729c06e"></a> typedef uint32\_t GATT\_DB\_SERVICE\_DESC
:   such as [GATT\_DB\_SER\_NO\_SECURITY\_PROPERTY](#group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035dab307287b35dec27c88ec7030aca6fb84) GATT\_DB\_SER\_SUPPORT\_ANY\_LINK\_TYPE

<a id="_CPPv422ble_gatt_db_callback_t"></a>

<a id="_CPPv322ble_gatt_db_callback_t"></a> <a id="_CPPv222ble_gatt_db_callback_t"></a> <a id="ble_gatt_db_callback_t"></a> <a id="dm__ble__types_8h_1af8a77b6634562ad79c03ea1b02d50d88"></a> typedef [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") (\*ble\_gatt\_db\_callback\_t)(uint8\_t conn\_handle, [GATT\_DB\_HANDLE](#_CPPv414GATT_DB_HANDLE "GATT_DB_HANDLE") \*handle, [GATT\_DB\_PARAMS](#_CPPv414GATT_DB_PARAMS "GATT_DB_PARAMS") \*param)
:   GATT DB callback extension, GATT DB Handler Callback. The GATT DB PL extension calls the registered callback to indicate any ongoing GATT DB Operation. The Upper Layer can implement specific handling for any Characterisitc or Characteritistic Descriptor depending on its requirement.

    Param conn\_handle
    :   **\[in\]** connection handle, see BK\_DM\_BLE\_EVENT\_CONNECT

    Param handle
    :   **\[in\]** Pointer to GATT DB identifier [GATT\_DB\_HANDLE](#structGATT__DB__HANDLE)

    Param param
    :   **\[in\]** Pointer to GATT DB Parameters [GATT\_DB\_PARAMS](#structGATT__DB__PARAMS)

    Return
    :   API\_SUCCESS if ATT/GATT response for the incoming request to be sent from the below layer GATT\_DB\_DELAYED\_RESPONSE if ATT/GATT response will be sent at a later point by the application GATT\_DB\_DONOT\_RESPOND if ATT/GATT response will be sent at a later point by the application GATT\_DB\_ALREADY\_RESPONDED if ATT/GATT response is already sent the application else and Error code describing cause of failure.

<a id="_CPPv414ble_event_cb_t"></a>

<a id="_CPPv314ble_event_cb_t"></a> <a id="_CPPv214ble_event_cb_t"></a> <a id="ble_event_cb_t"></a> <a id="dm__ble__types_8h_1ae05e16ccaad557c4d36fa16115d6b363"></a> typedef uint32\_t (\*ble\_event\_cb\_t)([ble\_event\_enum\_t](#_CPPv416ble_event_enum_t "ble_event_enum_t") event, void \*param)
:   for async dm\_ble api event.

    ble event report.

    Param event, :
    :   event id. see ble\_event\_enum\_t

        - param: param

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv4Ut1_3"></a>

<a id="_CPPv3Ut1_3"></a> <a id="dm__ble__types_8h_1abc6126af1d45847bc59afa0aa3216b04"></a> enum \[anonymous\]
:   GATT Attributes.

    *Values:*

    <a id="_CPPv4NUt1_320GATT_PRIMARY_SERVICEE"></a>

    <a id="_CPPv3NUt1_320GATT_PRIMARY_SERVICEE"></a> <a id="dm__ble__types_8h_1abc6126af1d45847bc59afa0aa3216b04a7f7b0a8b166e6bdb58b27eda08539ba2"></a> enumerator GATT\_PRIMARY\_SERVICE

    <a id="_CPPv4NUt1_322GATT_SECONDARY_SERVICEE"></a>

    <a id="_CPPv3NUt1_322GATT_SECONDARY_SERVICEE"></a> <a id="dm__ble__types_8h_1abc6126af1d45847bc59afa0aa3216b04a628dfffd136296fa182c36c8dbe69012"></a> enumerator GATT\_SECONDARY\_SERVICE

    <a id="_CPPv4NUt1_312GATT_INCLUDEE"></a>

    <a id="_CPPv3NUt1_312GATT_INCLUDEE"></a> <a id="dm__ble__types_8h_1abc6126af1d45847bc59afa0aa3216b04aedbb6a0187e64089344ac0a5f8dfd979"></a> enumerator GATT\_INCLUDE

    <a id="_CPPv4NUt1_319GATT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_319GATT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1abc6126af1d45847bc59afa0aa3216b04ae168b0de149233f1226b0145c7cb6881"></a> enumerator GATT\_CHARACTERISTIC

    <a id="_CPPv4NUt1_324GATT_EXTENDED_PROPERTIESE"></a>

    <a id="_CPPv3NUt1_324GATT_EXTENDED_PROPERTIESE"></a> <a id="dm__ble__types_8h_1abc6126af1d45847bc59afa0aa3216b04a5db9670afadfbbb36f8b91326e724d65"></a> enumerator GATT\_EXTENDED\_PROPERTIES

    <a id="_CPPv4NUt1_321GATT_USER_DESCRIPTIONE"></a>

    <a id="_CPPv3NUt1_321GATT_USER_DESCRIPTIONE"></a> <a id="dm__ble__types_8h_1abc6126af1d45847bc59afa0aa3216b04a3502e168194cc0d2491b294f309e6c47"></a> enumerator GATT\_USER\_DESCRIPTION

    <a id="_CPPv4NUt1_318GATT_CLIENT_CONFIGE"></a>

    <a id="_CPPv3NUt1_318GATT_CLIENT_CONFIGE"></a> <a id="dm__ble__types_8h_1abc6126af1d45847bc59afa0aa3216b04ac12babe25f6d65a037d8212f7fc4662d"></a> enumerator GATT\_CLIENT\_CONFIG

    <a id="_CPPv4NUt1_318GATT_SERVER_CONFIGE"></a>

    <a id="_CPPv3NUt1_318GATT_SERVER_CONFIGE"></a> <a id="dm__ble__types_8h_1abc6126af1d45847bc59afa0aa3216b04aec2a02cf19f82b9043600c417eb94323"></a> enumerator GATT\_SERVER\_CONFIG

    <a id="_CPPv4NUt1_311GATT_FORMATE"></a>

    <a id="_CPPv3NUt1_311GATT_FORMATE"></a> <a id="dm__ble__types_8h_1abc6126af1d45847bc59afa0aa3216b04acdc4dea4c65841ca5f3a7be0c2d2d6ed"></a> enumerator GATT\_FORMAT

    <a id="_CPPv4NUt1_321GATT_AGGREGATE_FORMATE"></a>

    <a id="_CPPv3NUt1_321GATT_AGGREGATE_FORMATE"></a> <a id="dm__ble__types_8h_1abc6126af1d45847bc59afa0aa3216b04a95c1f0118803a453613186da7baabc9a"></a> enumerator GATT\_AGGREGATE\_FORMAT

    <a id="_CPPv4NUt1_316GATT_VALID_RANGEE"></a>

    <a id="_CPPv3NUt1_316GATT_VALID_RANGEE"></a> <a id="dm__ble__types_8h_1abc6126af1d45847bc59afa0aa3216b04a4bd541977350fc73f6e97d03a3c61906"></a> enumerator GATT\_VALID\_RANGE

    <a id="_CPPv4NUt1_324GATT_EXTERNAL_REPORT_REFE"></a>

    <a id="_CPPv3NUt1_324GATT_EXTERNAL_REPORT_REFE"></a> <a id="dm__ble__types_8h_1abc6126af1d45847bc59afa0aa3216b04a4f70a260550a17811349b3ca399cff2d"></a> enumerator GATT\_EXTERNAL\_REPORT\_REF

    <a id="_CPPv4NUt1_329GATT_IP_OP_FEATURE_REPORT_REFE"></a>

    <a id="_CPPv3NUt1_329GATT_IP_OP_FEATURE_REPORT_REFE"></a> <a id="dm__ble__types_8h_1abc6126af1d45847bc59afa0aa3216b04a3b3f2930b4817f75f202d8d083a52e19"></a> enumerator GATT\_IP\_OP\_FEATURE\_REPORT\_REF

<a id="_CPPv4Ut1_4"></a>

<a id="_CPPv3Ut1_4"></a> <a id="dm__ble__types_8h_1adc29c2ff13d900c2f185ee95427fb06c"></a> enum \[anonymous\]
:   GATT Configuration.

    *Values:*

    <a id="_CPPv4NUt1_426GATT_CLI_CNFG_NOTIFICATIONE"></a>

    <a id="_CPPv3NUt1_426GATT_CLI_CNFG_NOTIFICATIONE"></a> <a id="dm__ble__types_8h_1adc29c2ff13d900c2f185ee95427fb06ca625a52e22fffd0aaaf199cc4eadb2723"></a> enumerator GATT\_CLI\_CNFG\_NOTIFICATION
    :   GATT Client Configuration values

    <a id="_CPPv4NUt1_424GATT_CLI_CNFG_INDICATIONE"></a>

    <a id="_CPPv3NUt1_424GATT_CLI_CNFG_INDICATIONE"></a> <a id="dm__ble__types_8h_1adc29c2ff13d900c2f185ee95427fb06cadcf83833fde88106f1202e4e1246c960"></a> enumerator GATT\_CLI\_CNFG\_INDICATION

    <a id="_CPPv4NUt1_421GATT_CLI_CNFG_DEFAULTE"></a>

    <a id="_CPPv3NUt1_421GATT_CLI_CNFG_DEFAULTE"></a> <a id="dm__ble__types_8h_1adc29c2ff13d900c2f185ee95427fb06cad8fc971d39800ec151f172bb6598c1d9"></a> enumerator GATT\_CLI\_CNFG\_DEFAULT

    <a id="_CPPv4NUt1_423GATT_SER_CNFG_BROADCASTE"></a>

    <a id="_CPPv3NUt1_423GATT_SER_CNFG_BROADCASTE"></a> <a id="dm__ble__types_8h_1adc29c2ff13d900c2f185ee95427fb06ca9b274cce82f346e054c8f8aacb2e4852"></a> enumerator GATT\_SER\_CNFG\_BROADCAST
    :   GATT Server Configuration values

    <a id="_CPPv4NUt1_421GATT_SER_CNFG_DEFAULTE"></a>

    <a id="_CPPv3NUt1_421GATT_SER_CNFG_DEFAULTE"></a> <a id="dm__ble__types_8h_1adc29c2ff13d900c2f185ee95427fb06ca8c64d78d85c3670c829b7c7411484858"></a> enumerator GATT\_SER\_CNFG\_DEFAULT

<a id="_CPPv4Ut1_5"></a>

<a id="_CPPv3Ut1_5"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9e"></a> enum \[anonymous\]
:   GATT Services.

    *Values:*

    <a id="_CPPv4NUt1_516GATT_GAP_SERVICEE"></a>

    <a id="_CPPv3NUt1_516GATT_GAP_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9ea3de78b95bdb6b81fc0e03fd822bfd7a4"></a> enumerator GATT\_GAP\_SERVICE

    <a id="_CPPv4NUt1_517GATT_GATT_SERVICEE"></a>

    <a id="_CPPv3NUt1_517GATT_GATT_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9ea6b27df3d24b59542af674698c3bb2a1b"></a> enumerator GATT\_GATT\_SERVICE

    <a id="_CPPv4NUt1_528GATT_IMMEDIATE_ALERT_SERVICEE"></a>

    <a id="_CPPv3NUt1_528GATT_IMMEDIATE_ALERT_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9eaf9056bcbe2759cc56da747d6005d7aad"></a> enumerator GATT\_IMMEDIATE\_ALERT\_SERVICE

    <a id="_CPPv4NUt1_522GATT_LINK_LOSS_SERVICEE"></a>

    <a id="_CPPv3NUt1_522GATT_LINK_LOSS_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9ea296d717a7252093ac369ef0dec0c0873"></a> enumerator GATT\_LINK\_LOSS\_SERVICE

    <a id="_CPPv4NUt1_521GATT_TX_POWER_SERVICEE"></a>

    <a id="_CPPv3NUt1_521GATT_TX_POWER_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9ea921c6adcf3564d771d3c107b5e4d20ac"></a> enumerator GATT\_TX\_POWER\_SERVICE

    <a id="_CPPv4NUt1_525GATT_CURRENT_TIME_SERVICEE"></a>

    <a id="_CPPv3NUt1_525GATT_CURRENT_TIME_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9eaf154420e5817b74f9b021c2b3219bc0e"></a> enumerator GATT\_CURRENT\_TIME\_SERVICE

    <a id="_CPPv4NUt1_528GATT_REF_TIME_UPDATE_SERVICEE"></a>

    <a id="_CPPv3NUt1_528GATT_REF_TIME_UPDATE_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9ea3f096adf8d93cfc690838e8122afcfef"></a> enumerator GATT\_REF\_TIME\_UPDATE\_SERVICE

    <a id="_CPPv4NUt1_528GATT_NEXT_DST_CHANGE_SERVICEE"></a>

    <a id="_CPPv3NUt1_528GATT_NEXT_DST_CHANGE_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9eab76c025604664f72d631c7720535332c"></a> enumerator GATT\_NEXT\_DST\_CHANGE\_SERVICE

    <a id="_CPPv4NUt1_520GATT_GLUCOSE_SERVICEE"></a>

    <a id="_CPPv3NUt1_520GATT_GLUCOSE_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9ea431e17dc864d105c4cfd5abd7c738561"></a> enumerator GATT\_GLUCOSE\_SERVICE

    <a id="_CPPv4NUt1_531GATT_HEALTH_THERMOMETER_SERVICEE"></a>

    <a id="_CPPv3NUt1_531GATT_HEALTH_THERMOMETER_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9eac61e7573caff93fb045b86afc63f68b0"></a> enumerator GATT\_HEALTH\_THERMOMETER\_SERVICE

    <a id="_CPPv4NUt1_524GATT_DEVICE_INFO_SERVICEE"></a>

    <a id="_CPPv3NUt1_524GATT_DEVICE_INFO_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9ea9a48945add7c3f4c579c256e91e967f0"></a> enumerator GATT\_DEVICE\_INFO\_SERVICE

    <a id="_CPPv4NUt1_516GATT_NWA_SERVICEE"></a>

    <a id="_CPPv3NUt1_516GATT_NWA_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9ea3b5045f624d84421a021ea2c31f1b0b7"></a> enumerator GATT\_NWA\_SERVICE

    <a id="_CPPv4NUt1_522GATT_WATCH_DOG_SERVICEE"></a>

    <a id="_CPPv3NUt1_522GATT_WATCH_DOG_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9ea6af37e6c4a0018839d2e6b227ca19ff7"></a> enumerator GATT\_WATCH\_DOG\_SERVICE

    <a id="_CPPv4NUt1_523GATT_HEART_RATE_SERVICEE"></a>

    <a id="_CPPv3NUt1_523GATT_HEART_RATE_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9ea19c9a23374faff3605e287cd3d845b39"></a> enumerator GATT\_HEART\_RATE\_SERVICE

    <a id="_CPPv4NUt1_531GATT_PHONE_ALERT_STATUS_SERVICEE"></a>

    <a id="_CPPv3NUt1_531GATT_PHONE_ALERT_STATUS_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9ea56538d50b5de02423be245767f184007"></a> enumerator GATT\_PHONE\_ALERT\_STATUS\_SERVICE

    <a id="_CPPv4NUt1_520GATT_BATTERY_SERVICEE"></a>

    <a id="_CPPv3NUt1_520GATT_BATTERY_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9ea594e47b9d67881d758bafb116e519b75"></a> enumerator GATT\_BATTERY\_SERVICE

    <a id="_CPPv4NUt1_527GATT_BLOOD_PRESSURE_SERVICEE"></a>

    <a id="_CPPv3NUt1_527GATT_BLOOD_PRESSURE_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9ea77277a759c1e374e7bbb9a9de3444435"></a> enumerator GATT\_BLOOD\_PRESSURE\_SERVICE

    <a id="_CPPv4NUt1_531GATT_ALERT_NOTIFICATION_SERVICEE"></a>

    <a id="_CPPv3NUt1_531GATT_ALERT_NOTIFICATION_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9eacd2e77f51a2b89caa38c7f6347bf0224"></a> enumerator GATT\_ALERT\_NOTIFICATION\_SERVICE

    <a id="_CPPv4NUt1_516GATT_HID_SERVICEE"></a>

    <a id="_CPPv3NUt1_516GATT_HID_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9eaf48f8464f7c8e038568f6266cd0467c2"></a> enumerator GATT\_HID\_SERVICE

    <a id="_CPPv4NUt1_523GATT_SCAN_PARAM_SERVICEE"></a>

    <a id="_CPPv3NUt1_523GATT_SCAN_PARAM_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9ea495f103974fa35973dfd1923898de530"></a> enumerator GATT\_SCAN\_PARAM\_SERVICE

    <a id="_CPPv4NUt1_538GATT_RUNNING_SPEED_AND_CADENCE_SERVICEE"></a>

    <a id="_CPPv3NUt1_538GATT_RUNNING_SPEED_AND_CADENCE_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9ea4c6ce810bc791fccb662aafe0caea73b"></a> enumerator GATT\_RUNNING\_SPEED\_AND\_CADENCE\_SERVICE

    <a id="_CPPv4NUt1_517GATT_AIOS_SERVICEE"></a>

    <a id="_CPPv3NUt1_517GATT_AIOS_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9eab0d9f1b86a1dee6b411912b4beffb235"></a> enumerator GATT\_AIOS\_SERVICE

    <a id="_CPPv4NUt1_538GATT_CYCLING_SPEED_AND_CADENCE_SERVICEE"></a>

    <a id="_CPPv3NUt1_538GATT_CYCLING_SPEED_AND_CADENCE_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9eabb5d1d6b649b1a11932fb6715ecf72f5"></a> enumerator GATT\_CYCLING\_SPEED\_AND\_CADENCE\_SERVICE

    <a id="_CPPv4NUt1_516GATT_CPM_SERVICEE"></a>

    <a id="_CPPv3NUt1_516GATT_CPM_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9ea396a77f300322c4c0373a561b9eb1806"></a> enumerator GATT\_CPM\_SERVICE

    <a id="_CPPv4NUt1_536GATT_LOCATION_AND_NAVIGATION_SERVICEE"></a>

    <a id="_CPPv3NUt1_536GATT_LOCATION_AND_NAVIGATION_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9ea3a6669b26655c308e869a200accc4a8e"></a> enumerator GATT\_LOCATION\_AND\_NAVIGATION\_SERVICE

    <a id="_CPPv4NUt1_534GATT_ENVIRONMENTAL_SENSING_SERVICEE"></a>

    <a id="_CPPv3NUt1_534GATT_ENVIRONMENTAL_SENSING_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9eab6bcde59495ead72b9be84e3671400f5"></a> enumerator GATT\_ENVIRONMENTAL\_SENSING\_SERVICE

    <a id="_CPPv4NUt1_529GATT_BODY_COMPOSITION_SERVICEE"></a>

    <a id="_CPPv3NUt1_529GATT_BODY_COMPOSITION_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9ea9887419030384e6b006a13f1019d9c43"></a> enumerator GATT\_BODY\_COMPOSITION\_SERVICE

    <a id="_CPPv4NUt1_522GATT_USER_DATA_SERVICEE"></a>

    <a id="_CPPv3NUt1_522GATT_USER_DATA_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9eaf4eed8b647ec9fe7522cbc40f224b891"></a> enumerator GATT\_USER\_DATA\_SERVICE

    <a id="_CPPv4NUt1_525GATT_WEIGHT_SCALE_SERVICEE"></a>

    <a id="_CPPv3NUt1_525GATT_WEIGHT_SCALE_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9ea616422db11592b23038f6d10f0e862f8"></a> enumerator GATT\_WEIGHT\_SCALE\_SERVICE

    <a id="_CPPv4NUt1_515GATT_BM_SERVICEE"></a>

    <a id="_CPPv3NUt1_515GATT_BM_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9ea0864179b38f16738acc5bbd7b72c4075"></a> enumerator GATT\_BM\_SERVICE

    <a id="_CPPv4NUt1_516GATT_CGM_SERVICEE"></a>

    <a id="_CPPv3NUt1_516GATT_CGM_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9eaa8ae9293187d31ce73db8e3dbdb96dee"></a> enumerator GATT\_CGM\_SERVICE

    <a id="_CPPv4NUt1_519GATT_INT_PS_SERVICEE"></a>

    <a id="_CPPv3NUt1_519GATT_INT_PS_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9eacc3ae9bf55c9667bd426b71ea177533f"></a> enumerator GATT\_INT\_PS\_SERVICE

    <a id="_CPPv4NUt1_516GATT_IPS_SERVICEE"></a>

    <a id="_CPPv3NUt1_516GATT_IPS_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9ea1e5819a357147fe085709c2e710ddebc"></a> enumerator GATT\_IPS\_SERVICE

    <a id="_CPPv4NUt1_527GATT_PULSE_OXIMETER_SERVICEE"></a>

    <a id="_CPPv3NUt1_527GATT_PULSE_OXIMETER_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9ea7a8ba5a4c18fd6bf89c7055de11e661e"></a> enumerator GATT\_PULSE\_OXIMETER\_SERVICE

    <a id="_CPPv4NUt1_516GATT_HPS_SERVICEE"></a>

    <a id="_CPPv3NUt1_516GATT_HPS_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9eabb9f46c3396a08d159b0afa030028055"></a> enumerator GATT\_HPS\_SERVICE

    <a id="_CPPv4NUt1_516GATT_TDS_SERVICEE"></a>

    <a id="_CPPv3NUt1_516GATT_TDS_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9ea16bf01bbb63052bd0be21abb02b91116"></a> enumerator GATT\_TDS\_SERVICE

    <a id="_CPPv4NUt1_528GATT_OBJECT_TRANSFER_SERVICEE"></a>

    <a id="_CPPv3NUt1_528GATT_OBJECT_TRANSFER_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9ea2393139d81bdf69888135ad83d2c2f86"></a> enumerator GATT\_OBJECT\_TRANSFER\_SERVICE

    <a id="_CPPv4NUt1_517GATT_FTMS_SERVICEE"></a>

    <a id="_CPPv3NUt1_517GATT_FTMS_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9ea270ceb370707a0b75bd7f3a5f200af0a"></a> enumerator GATT\_FTMS\_SERVICE

    <a id="_CPPv4NUt1_516GATT_RCS_SERVICEE"></a>

    <a id="_CPPv3NUt1_516GATT_RCS_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9eac0ea0a13ad599d3fa4c47b61d6d30f8e"></a> enumerator GATT\_RCS\_SERVICE

    <a id="_CPPv4NUt1_529GATT_INSULIN_DELIVERY_SERVICEE"></a>

    <a id="_CPPv3NUt1_529GATT_INSULIN_DELIVERY_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9ea716d25e36be595500e3b49f3010beb6c"></a> enumerator GATT\_INSULIN\_DELIVERY\_SERVICE

    <a id="_CPPv4NUt1_520GATT_FIND_ME_SERVICEE"></a>

    <a id="_CPPv3NUt1_520GATT_FIND_ME_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9ea7843f49c2748e01d3fccabe210efb1fa"></a> enumerator GATT\_FIND\_ME\_SERVICE
    :   Dont find this on .org

    <a id="_CPPv4NUt1_517GATT_TPMS_SERVICEE"></a>

    <a id="_CPPv3NUt1_517GATT_TPMS_SERVICEE"></a> <a id="dm__ble__types_8h_1a61dadd085c1777f559549e05962b2c9eae894752f7b5a0a69a85f3d8059732394"></a> enumerator GATT\_TPMS\_SERVICE
    :   Still not adopted, may need updation

<a id="_CPPv4Ut1_6"></a>

<a id="_CPPv3Ut1_6"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635"></a> enum \[anonymous\]
:   GATT Characteristic.

    *Values:*

    <a id="_CPPv4NUt1_631GATT_DEVICE_NAME_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_631GATT_DEVICE_NAME_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635aa54228583c1ef2c9912e5d60096c4314"></a> enumerator GATT\_DEVICE\_NAME\_CHARACTERISTIC

    <a id="_CPPv4NUt1_630GATT_APPEARANCE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_630GATT_APPEARANCE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a1be1ccc7fcf79fad7fa8c58b77dc748f"></a> enumerator GATT\_APPEARANCE\_CHARACTERISTIC

    <a id="_CPPv4NUt1_639GATT_PERIPHRL_PRIVCY_FLG_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_639GATT_PERIPHRL_PRIVCY_FLG_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ad02143f8a1f0f0f67509f54ecbd80951"></a> enumerator GATT\_PERIPHRL\_PRIVCY\_FLG\_CHARACTERISTIC

    <a id="_CPPv4NUt1_634GATT_RECONNECT_ADDR_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_634GATT_RECONNECT_ADDR_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ad67fd40602fd7a841d6b031b2f327fbf"></a> enumerator GATT\_RECONNECT\_ADDR\_CHARACTERISTIC

    <a id="_CPPv4NUt1_637GATT_PRFRRD_CNXN_PARAM_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_637GATT_PRFRRD_CNXN_PARAM_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a31a5d3ce8aceee16f8b8404e1c4039b4"></a> enumerator GATT\_PRFRRD\_CNXN\_PARAM\_CHARACTERISTIC

    <a id="_CPPv4NUt1_635GATT_SERVICE_CHANGED_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_635GATT_SERVICE_CHANGED_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a3907725caf3c139062239f3ce014fd07"></a> enumerator GATT\_SERVICE\_CHANGED\_CHARACTERISTIC

    <a id="_CPPv4NUt1_631GATT_ALERT_LEVEL_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_631GATT_ALERT_LEVEL_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a60f39290c37e1c14ce31eca6b1301645"></a> enumerator GATT\_ALERT\_LEVEL\_CHARACTERISTIC

    <a id="_CPPv4NUt1_634GATT_TX_POWER_LEVEL_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_634GATT_TX_POWER_LEVEL_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a9f3b82c4d4d93522312b4b772453d061"></a> enumerator GATT\_TX\_POWER\_LEVEL\_CHARACTERISTIC

    <a id="_CPPv4NUt1_629GATT_DATE_TIME_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_629GATT_DATE_TIME_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ae846db575fa9d24e03cfe406e8f22f95"></a> enumerator GATT\_DATE\_TIME\_CHARACTERISTIC

    <a id="_CPPv4NUt1_631GATT_DAY_OF_WEEK_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_631GATT_DAY_OF_WEEK_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a27e64c9e1e8d11745b18ebea22825983"></a> enumerator GATT\_DAY\_OF\_WEEK\_CHARACTERISTIC

    <a id="_CPPv4NUt1_633GATT_DAY_DATE_TIME_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_633GATT_DAY_DATE_TIME_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635abd6dc146881b8d479a4d2fe2b23e2028"></a> enumerator GATT\_DAY\_DATE\_TIME\_CHARACTERISTIC

    <a id="_CPPv4NUt1_634GATT_EXACT_TIME_100_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_634GATT_EXACT_TIME_100_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a085c32196b9b4a9c1824d872f159e9d4"></a> enumerator GATT\_EXACT\_TIME\_100\_CHARACTERISTIC

    <a id="_CPPv4NUt1_634GATT_EXACT_TIME_256_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_634GATT_EXACT_TIME_256_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a9512713de92fb284b86818c54ce28527"></a> enumerator GATT\_EXACT\_TIME\_256\_CHARACTERISTIC

    <a id="_CPPv4NUt1_630GATT_DST_OFFSET_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_630GATT_DST_OFFSET_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a147eb24025e7a73d708356ffafdc440c"></a> enumerator GATT\_DST\_OFFSET\_CHARACTERISTIC

    <a id="_CPPv4NUt1_629GATT_TIME_ZONE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_629GATT_TIME_ZONE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635abb82c748d8c8119bd5fd64a462be14a7"></a> enumerator GATT\_TIME\_ZONE\_CHARACTERISTIC

    <a id="_CPPv4NUt1_635GATT_LOCAL_TIME_INFO_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_635GATT_LOCAL_TIME_INFO_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a6f590bb9456c754b52c6b364047a2b4f"></a> enumerator GATT\_LOCAL\_TIME\_INFO\_CHARACTERISTIC

    <a id="_CPPv4NUt1_633GATT_SEC_TIME_ZONE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_633GATT_SEC_TIME_ZONE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a452faa94d2ed000b9d4b42479aef1f3e"></a> enumerator GATT\_SEC\_TIME\_ZONE\_CHARACTERISTIC

    <a id="_CPPv4NUt1_633GATT_TIME_WITH_DST_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_633GATT_TIME_WITH_DST_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a6ba8d62c1039932c7537d378910192bd"></a> enumerator GATT\_TIME\_WITH\_DST\_CHARACTERISTIC

    <a id="_CPPv4NUt1_633GATT_TIME_ACCURACY_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_633GATT_TIME_ACCURACY_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a1d7dedd6929eb4d9fd49398fdfb4bd15"></a> enumerator GATT\_TIME\_ACCURACY\_CHARACTERISTIC

    <a id="_CPPv4NUt1_631GATT_TIME_SOURCE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_631GATT_TIME_SOURCE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635addbbe52fe4df9a3ea4923a062d83363e"></a> enumerator GATT\_TIME\_SOURCE\_CHARACTERISTIC

    <a id="_CPPv4NUt1_633GATT_REF_TIME_INFO_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_633GATT_REF_TIME_INFO_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635abf0be9bf6412153b7e35516717451197"></a> enumerator GATT\_REF\_TIME\_INFO\_CHARACTERISTIC

    <a id="_CPPv4NUt1_634GATT_TIME_BROADCAST_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_634GATT_TIME_BROADCAST_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a4d2b6945bc17904f0d38eb03ed2f8fb9"></a> enumerator GATT\_TIME\_BROADCAST\_CHARACTERISTIC

    <a id="_CPPv4NUt1_630GATT_TIME_UPDATE_CONTROL_POINTE"></a>

    <a id="_CPPv3NUt1_630GATT_TIME_UPDATE_CONTROL_POINTE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ac18918e127f5cbc48491aa384c1d0e40"></a> enumerator GATT\_TIME\_UPDATE\_CONTROL\_POINT

    <a id="_CPPv4NUt1_637GATT_TIME_UPDATE_STATE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_637GATT_TIME_UPDATE_STATE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a741c822d4a0ee3113ed26d75d0a4d34a"></a> enumerator GATT\_TIME\_UPDATE\_STATE\_CHARACTERISTIC

    <a id="_CPPv4NUt1_634GATT_GLUCOSE_MSRMNT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_634GATT_GLUCOSE_MSRMNT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635af14027483e500c588758dea6c008f310"></a> enumerator GATT\_GLUCOSE\_MSRMNT\_CHARACTERISTIC

    <a id="_CPPv4NUt1_633GATT_BATTERY_LEVEL_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_633GATT_BATTERY_LEVEL_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635acceca790a17d4cee09123ecf96a416d0"></a> enumerator GATT\_BATTERY\_LEVEL\_CHARACTERISTIC

    <a id="_CPPv4NUt1_633GATT_BATTERY_PWR_ST_CHARCTERISTICE"></a>

    <a id="_CPPv3NUt1_633GATT_BATTERY_PWR_ST_CHARCTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a0e4f6f86a8e30fad4b0e9ca7a6d9a176"></a> enumerator GATT\_BATTERY\_PWR\_ST\_CHARCTERISTIC

    <a id="_CPPv4NUt1_636GATT_BATTERY_LEVEL_ST_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_636GATT_BATTERY_LEVEL_ST_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635aa13f2b0353177e701fae99db22288c8d"></a> enumerator GATT\_BATTERY\_LEVEL\_ST\_CHARACTERISTIC

    <a id="_CPPv4NUt1_637GATT_TEMPERATURE_MSMNT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_637GATT_TEMPERATURE_MSMNT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635aa8f3c814bb8449033403055b9b2b285a"></a> enumerator GATT\_TEMPERATURE\_MSMNT\_CHARACTERISTIC

    <a id="_CPPv4NUt1_636GATT_TEMPERATURE_TYPE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_636GATT_TEMPERATURE_TYPE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ad03d9596121fbd2531d4f30429cae446"></a> enumerator GATT\_TEMPERATURE\_TYPE\_CHARACTERISTIC

    <a id="_CPPv4NUt1_637GATT_INTERMEDIATE_TEMP_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_637GATT_INTERMEDIATE_TEMP_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a86da80e4f810523a9d4e0f1237316cd8"></a> enumerator GATT\_INTERMEDIATE\_TEMP\_CHARACTERISTIC

    <a id="_CPPv4NUt1_636GATT_MSMNT_INTERVAL_CHARATACTERISTICE"></a>

    <a id="_CPPv3NUt1_636GATT_MSMNT_INTERVAL_CHARATACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a9e434c5f6230165b37856ae5c461c7af"></a> enumerator GATT\_MSMNT\_INTERVAL\_CHARATACTERISTIC

    <a id="_CPPv4NUt1_637GATT_BOOT_KYBRD_IN_RPT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_637GATT_BOOT_KYBRD_IN_RPT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a1d7ca7ec5fc54881fc51e0a3a66c0c66"></a> enumerator GATT\_BOOT\_KYBRD\_IN\_RPT\_CHARACTERISTIC

    <a id="_CPPv4NUt1_629GATT_SYSTEM_ID_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_629GATT_SYSTEM_ID_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635aa6d45823e4e00ac1c8fc951c2b1198ef"></a> enumerator GATT\_SYSTEM\_ID\_CHARACTERISTIC

    <a id="_CPPv4NUt1_632GATT_MODEL_NUMBER_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_632GATT_MODEL_NUMBER_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a8fe3861f1e1c5e5ea492f30f8c99d5b9"></a> enumerator GATT\_MODEL\_NUMBER\_CHARACTERISTIC

    <a id="_CPPv4NUt1_633GATT_SERIAL_NUMBER_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_633GATT_SERIAL_NUMBER_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a2bfeb8ab2c8f30e1d1bf5163b1e8ad78"></a> enumerator GATT\_SERIAL\_NUMBER\_CHARACTERISTIC

    <a id="_CPPv4NUt1_632GATT_FIRMWARE_REV_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_632GATT_FIRMWARE_REV_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a6ea194209469440a6d34cb04a0f06673"></a> enumerator GATT\_FIRMWARE\_REV\_CHARACTERISTIC

    <a id="_CPPv4NUt1_632GATT_HARDWARE_REV_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_632GATT_HARDWARE_REV_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635adf42129dee24a6c3f71c84ceec0276e2"></a> enumerator GATT\_HARDWARE\_REV\_CHARACTERISTIC

    <a id="_CPPv4NUt1_632GATT_SOFTWARE_REV_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_632GATT_SOFTWARE_REV_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a6e2bd0ae16c859f9939b7e6668350313"></a> enumerator GATT\_SOFTWARE\_REV\_CHARACTERISTIC

    <a id="_CPPv4NUt1_637GATT_MANUFACTURER_NAME_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_637GATT_MANUFACTURER_NAME_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a81e018248f7f4ca1a021d36ebadbb725"></a> enumerator GATT\_MANUFACTURER\_NAME\_CHARACTERISTIC

    <a id="_CPPv4NUt1_633GATT_REG_CERT_DATA_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_633GATT_REG_CERT_DATA_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635af833359a2d2cf95cdabf7584f19d93db"></a> enumerator GATT\_REG\_CERT\_DATA\_CHARACTERISTIC

    <a id="_CPPv4NUt1_632GATT_CURRENT_TIME_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_632GATT_CURRENT_TIME_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a62d06703a7d8969ec6068308b2c2ca7f"></a> enumerator GATT\_CURRENT\_TIME\_CHARACTERISTIC

    <a id="_CPPv4NUt1_632GATT_SCAN_REFRESH_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_632GATT_SCAN_REFRESH_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a372c9354c05b32e9a10f85c9285b1f1f"></a> enumerator GATT\_SCAN\_REFRESH\_CHARACTERISTIC

    <a id="_CPPv4NUt1_633GATT_BOOT_KYBRD_OP_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_633GATT_BOOT_KYBRD_OP_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a9f53da5e8ceb6c66dac99964dec727b1"></a> enumerator GATT\_BOOT\_KYBRD\_OP\_CHARACTERISTIC

    <a id="_CPPv4NUt1_628GATT_MOUSE_IP_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_628GATT_MOUSE_IP_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635aa9d6a93ce292dbf0d6f8a7d89f130f7e"></a> enumerator GATT\_MOUSE\_IP\_CHARACTERISTIC

    <a id="_CPPv4NUt1_632GATT_GL_MSRMT_CTX_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_632GATT_GL_MSRMT_CTX_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a90e8e10618003c55fa89c4a845a5ee9e"></a> enumerator GATT\_GL\_MSRMT\_CTX\_CHARACTERISTIC

    <a id="_CPPv4NUt1_628GATT_BP_MSRMT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_628GATT_BP_MSRMT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a241e9052148b3cfb16a5e62e26b61d81"></a> enumerator GATT\_BP\_MSRMT\_CHARACTERISTIC

    <a id="_CPPv4NUt1_637GATT_INTRMDT_CUFF_PRSR_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_637GATT_INTRMDT_CUFF_PRSR_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a257846d5e00e389d43e25afc2f55fa50"></a> enumerator GATT\_INTRMDT\_CUFF\_PRSR\_CHARACTERISTIC

    <a id="_CPPv4NUt1_628GATT_HR_MSRMT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_628GATT_HR_MSRMT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a4c08078e47e8a5303c5226bf514628fc"></a> enumerator GATT\_HR\_MSRMT\_CHARACTERISTIC

    <a id="_CPPv4NUt1_635GATT_BODY_SENSOR_LOC_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_635GATT_BODY_SENSOR_LOC_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635af9a0ca7482b5a657243b802b96962e72"></a> enumerator GATT\_BODY\_SENSOR\_LOC\_CHARACTERISTIC

    <a id="_CPPv4NUt1_619GATT_HR_CNTRL_POINTE"></a>

    <a id="_CPPv3NUt1_619GATT_HR_CNTRL_POINTE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a2dd6c7010ff8d08f1ebeaae01f130210"></a> enumerator GATT\_HR\_CNTRL\_POINT

    <a id="_CPPv4NUt1_623GATT_NWA_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_623GATT_NWA_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a202b01d3d9a9a522074245479f5553b6"></a> enumerator GATT\_NWA\_CHARACTERISTIC

    <a id="_CPPv4NUt1_632GATT_ALERT_STATUS_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_632GATT_ALERT_STATUS_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635af5261cbd1fb5c4459ac62673d233ac31"></a> enumerator GATT\_ALERT\_STATUS\_CHARACTERISTIC

    <a id="_CPPv4NUt1_640GATT_RINGER_CONTROL_POINT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_640GATT_RINGER_CONTROL_POINT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a33f63c21b6ce3afe7503fffcc8bb8c35"></a> enumerator GATT\_RINGER\_CONTROL\_POINT\_CHARACTERISTIC

    <a id="_CPPv4NUt1_634GATT_RINGER_SETTING_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_634GATT_RINGER_SETTING_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a16565c9398beaf6decf376c8dab92dbf"></a> enumerator GATT\_RINGER\_SETTING\_CHARACTERISTIC

    <a id="_CPPv4NUt1_637GATT_ALERT_ID_BIT_MASK_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_637GATT_ALERT_ID_BIT_MASK_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635addd5df56203030fdfd91014b29cd8fef"></a> enumerator GATT\_ALERT\_ID\_BIT\_MASK\_CHARACTERISTIC

    <a id="_CPPv4NUt1_628GATT_ALERT_ID_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_628GATT_ALERT_ID_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a2ba81a001977b5e809108748205fc716"></a> enumerator GATT\_ALERT\_ID\_CHARACTERISTIC

    <a id="_CPPv4NUt1_628GATT_ALERT_NTF_CONTROL_POINTE"></a>

    <a id="_CPPv3NUt1_628GATT_ALERT_NTF_CONTROL_POINTE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a9988085cd010ce0c3b3d8d3d23531605"></a> enumerator GATT\_ALERT\_NTF\_CONTROL\_POINT

    <a id="_CPPv4NUt1_638GATT_UNREAD_ALRT_STATUS_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_638GATT_UNREAD_ALRT_STATUS_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a897fa776ac6b3a15943cecd13471bf63"></a> enumerator GATT\_UNREAD\_ALRT\_STATUS\_CHARACTERISTIC

    <a id="_CPPv4NUt1_629GATT_NEW_ALERT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_629GATT_NEW_ALERT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635afcb5a43c4cc75b65ba81821034195955"></a> enumerator GATT\_NEW\_ALERT\_CHARACTERISTIC

    <a id="_CPPv4NUt1_640GATT_SPRTD_NEW_ALRT_CTGRY_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_640GATT_SPRTD_NEW_ALRT_CTGRY_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a371f2ca7e6894e47635c2a1ec3695681"></a> enumerator GATT\_SPRTD\_NEW\_ALRT\_CTGRY\_CHARACTERISTIC

    <a id="_CPPv4NUt1_640GATT_SPRT_UNRD_ALRT_CTGRY_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_640GATT_SPRT_UNRD_ALRT_CTGRY_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a697a5006f6cb79fe4a95ea2befc18ae2"></a> enumerator GATT\_SPRT\_UNRD\_ALRT\_CTGRY\_CHARACTERISTIC

    <a id="_CPPv4NUt1_630GATT_BP_FEATURE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_630GATT_BP_FEATURE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a59362ad5e21c5fa198623d1d45a4d9fe"></a> enumerator GATT\_BP\_FEATURE\_CHARACTERISTIC

    <a id="_CPPv4NUt1_628GATT_HID_INFO_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_628GATT_HID_INFO_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a1c15c4d6ef496fb7fa6dd2f0590e0989"></a> enumerator GATT\_HID\_INFO\_CHARACTERISTIC

    <a id="_CPPv4NUt1_631GATT_HID_RPT_MAP_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_631GATT_HID_RPT_MAP_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635accd06e62e400b63057694ed14b62da37"></a> enumerator GATT\_HID\_RPT\_MAP\_CHARACTERISTIC

    <a id="_CPPv4NUt1_626GATT_HID_CP_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_626GATT_HID_CP_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a03e956221c4db2a45eec3cb54bf6c797"></a> enumerator GATT\_HID\_CP\_CHARACTERISTIC

    <a id="_CPPv4NUt1_627GATT_HID_RPT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_627GATT_HID_RPT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ab8ab71125a4759a279714855719de6ad"></a> enumerator GATT\_HID\_RPT\_CHARACTERISTIC

    <a id="_CPPv4NUt1_634GATT_HID_PROTO_MODE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_634GATT_HID_PROTO_MODE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a4aead811c73f2507a1ac4339f021b6a4"></a> enumerator GATT\_HID\_PROTO\_MODE\_CHARACTERISTIC

    <a id="_CPPv4NUt1_631GATT_SCAN_WINDOW_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_631GATT_SCAN_WINDOW_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a080f8b29dcd367b551caf3533a7fb177"></a> enumerator GATT\_SCAN\_WINDOW\_CHARACTERISTIC

    <a id="_CPPv4NUt1_626GATT_PNP_ID_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_626GATT_PNP_ID_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a076f73cd85c635fbfb43a484125ff436"></a> enumerator GATT\_PNP\_ID\_CHARACTERISTIC

    <a id="_CPPv4NUt1_630GATT_GL_FEATURE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_630GATT_GL_FEATURE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635afeea8188d5d406139414265dd437f498"></a> enumerator GATT\_GL\_FEATURE\_CHARACTERISTIC

    <a id="_CPPv4NUt1_624GATT_RACP_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_624GATT_RACP_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ab59babb2886138bbef67e44a05682930"></a> enumerator GATT\_RACP\_CHARACTERISTIC

    <a id="_CPPv4NUt1_629GATT_RSC_MSRMT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_629GATT_RSC_MSRMT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ad436fe8b2192d69963642c865816a95a"></a> enumerator GATT\_RSC\_MSRMT\_CHARACTERISTIC

    <a id="_CPPv4NUt1_631GATT_RSC_FEATURE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_631GATT_RSC_FEATURE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a8af1ec351f6e6aeab89e932e76a37e01"></a> enumerator GATT\_RSC\_FEATURE\_CHARACTERISTIC

    <a id="_CPPv4NUt1_636GATT_SC_CONTROL_POINT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_636GATT_SC_CONTROL_POINT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635af4d4f1f2e58bcfd5f2c5afe4e6c4cbcd"></a> enumerator GATT\_SC\_CONTROL\_POINT\_CHARACTERISTIC

    <a id="_CPPv4NUt1_629GATT_CSC_MSRMT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_629GATT_CSC_MSRMT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635afe0a7accdc76f1bf0b4ae8346e852691"></a> enumerator GATT\_CSC\_MSRMT\_CHARACTERISTIC

    <a id="_CPPv4NUt1_631GATT_CSC_FEATURE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_631GATT_CSC_FEATURE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a5216ba8906b83feec33682f42cf04944"></a> enumerator GATT\_CSC\_FEATURE\_CHARACTERISTIC

    <a id="_CPPv4NUt1_635GATT_SENSOR_LOCATION_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_635GATT_SENSOR_LOCATION_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a886b6579b23ddf90f8e22505e6450872"></a> enumerator GATT\_SENSOR\_LOCATION\_CHARACTERISTIC

    <a id="_CPPv4NUt1_638GATT_POX_SPOT_CHK_MSRMT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_638GATT_POX_SPOT_CHK_MSRMT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a9f4f733cad7de85e9a58589bf2dc119b"></a> enumerator GATT\_POX\_SPOT\_CHK\_MSRMT\_CHARACTERISTIC
    :   Still Not Adopted, may need updation Pulse Oximeter Characteristics defines

    <a id="_CPPv4NUt1_640GATT_POX_CONTINUOUS_MSRMT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_640GATT_POX_CONTINUOUS_MSRMT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a42e314b0e60a3e7049cd9e161879d6a8"></a> enumerator GATT\_POX\_CONTINUOUS\_MSRMT\_CHARACTERISTIC

    <a id="_CPPv4NUt1_639GATT_POX_PULSATILE_EVENT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_639GATT_POX_PULSATILE_EVENT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a38670a90df3ef4de286ad43080522eed"></a> enumerator GATT\_POX\_PULSATILE\_EVENT\_CHARACTERISTIC

    <a id="_CPPv4NUt1_632GATT_POX_FEATURES_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_632GATT_POX_FEATURES_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635aa3bfda2453020423c4425944fd5cfe35"></a> enumerator GATT\_POX\_FEATURES\_CHARACTERISTIC

    <a id="_CPPv4NUt1_637GATT_POX_CONTROL_POINT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_637GATT_POX_CONTROL_POINT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a15e896e588c840c698bac659575cd4cb"></a> enumerator GATT\_POX\_CONTROL\_POINT\_CHARACTERISTIC

    <a id="_CPPv4NUt1_629GATT_CPM_MSRMT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_629GATT_CPM_MSRMT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a78feca8e63bba4653f37e2d3c1b685f8"></a> enumerator GATT\_CPM\_MSRMT\_CHARACTERISTIC
    :   CPM Characteristics Measurments

    <a id="_CPPv4NUt1_630GATT_CPM_VECTOR_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_630GATT_CPM_VECTOR_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635aa4918f4e3a994d4269d0765446d32abf"></a> enumerator GATT\_CPM\_VECTOR\_CHARACTERISTIC

    <a id="_CPPv4NUt1_631GATT_CPM_FEATURE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_631GATT_CPM_FEATURE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635af6949585ff550dc6025c8fe911003e97"></a> enumerator GATT\_CPM\_FEATURE\_CHARACTERISTIC

    <a id="_CPPv4NUt1_633GATT_CPM_CNTRL_PNT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_633GATT_CPM_CNTRL_PNT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ad2388ab6dc1c8286ebe1ef3b71523a26"></a> enumerator GATT\_CPM\_CNTRL\_PNT\_CHARACTERISTIC

    <a id="_CPPv4NUt1_639GATT_CPM_SENSOR_LOCATION_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_639GATT_CPM_SENSOR_LOCATION_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a33e553680222b993798e3adbed899a69"></a> enumerator GATT\_CPM\_SENSOR\_LOCATION\_CHARACTERISTIC

    <a id="_CPPv4NUt1_638GATT_LOCATION_AND_SPEED_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_638GATT_LOCATION_AND_SPEED_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a5cc8a46d7f288659defad1580b44a278"></a> enumerator GATT\_LOCATION\_AND\_SPEED\_CHARACTERISTIC
    :   Location and Navigation Characteristics

    <a id="_CPPv4NUt1_630GATT_NAVIGATION_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_630GATT_NAVIGATION_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a6c2f08532162fe07f19c4e66e544dddf"></a> enumerator GATT\_NAVIGATION\_CHARACTERISTIC

    <a id="_CPPv4NUt1_639GATT_LN_POSITION_QUALITY_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_639GATT_LN_POSITION_QUALITY_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635acf503bc96216731bec46321c30c05927"></a> enumerator GATT\_LN\_POSITION\_QUALITY\_CHARACTERISTIC

    <a id="_CPPv4NUt1_630GATT_LN_FEATURE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_630GATT_LN_FEATURE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635aae3e9b3bc417dd861f8256bf4d358f9d"></a> enumerator GATT\_LN\_FEATURE\_CHARACTERISTIC

    <a id="_CPPv4NUt1_632GATT_LN_CNTRL_PNT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_632GATT_LN_CNTRL_PNT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a86330404f63db52737288d4d3ff1f42c"></a> enumerator GATT\_LN\_CNTRL\_PNT\_CHARACTERISTIC

    <a id="_CPPv4NUt1_629GATT_CGM_MSRMT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_629GATT_CGM_MSRMT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a6e3b3881c74c94a178ad43de08135fa6"></a> enumerator GATT\_CGM\_MSRMT\_CHARACTERISTIC
    :   CGM Characteristics defines

    <a id="_CPPv4NUt1_632GATT_CGM_FEATURES_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_632GATT_CGM_FEATURES_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635af7e0967cef1f898b97cbd5580d2d4cf4"></a> enumerator GATT\_CGM\_FEATURES\_CHARACTERISTIC

    <a id="_CPPv4NUt1_630GATT_CGM_STATUS_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_630GATT_CGM_STATUS_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635abb9c791258c0bf45b776f544e2381801"></a> enumerator GATT\_CGM\_STATUS\_CHARACTERISTIC

    <a id="_CPPv4NUt1_637GATT_CGM_SSN_STRT_TIME_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_637GATT_CGM_SSN_STRT_TIME_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a9474f82fb9dd0580841910854a134e87"></a> enumerator GATT\_CGM\_SSN\_STRT\_TIME\_CHARACTERISTIC

    <a id="_CPPv4NUt1_636GATT_CGM_SSN_RUN_TIME_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_636GATT_CGM_SSN_RUN_TIME_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ae53095b367adc503769e480bc3a9ee03"></a> enumerator GATT\_CGM\_SSN\_RUN\_TIME\_CHARACTERISTIC

    <a id="_CPPv4NUt1_639GATT_CGM_SPECIFIC_OPS_CP_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_639GATT_CGM_SPECIFIC_OPS_CP_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a879fbc8e31efa4e26f806978c2598110"></a> enumerator GATT\_CGM\_SPECIFIC\_OPS\_CP\_CHARACTERISTIC

    <a id="_CPPv4NUt1_637GATT_BATTERY_REMOVABLE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_637GATT_BATTERY_REMOVABLE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635acfc2ecfd7e105a908661ad2a35970a99"></a> enumerator GATT\_BATTERY\_REMOVABLE\_CHARACTERISTIC

    <a id="_CPPv4NUt1_638GATT_BATTERY_SERV_REQRD_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_638GATT_BATTERY_SERV_REQRD_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a48953a80338ff8c1d7ab62b6f2d12895"></a> enumerator GATT\_BATTERY\_SERV\_REQRD\_CHARACTERISTIC

    <a id="_CPPv4NUt1_628GATT_WS_MSRMT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_628GATT_WS_MSRMT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ab83334b2ecc918712d7d7f5abc35f113"></a> enumerator GATT\_WS\_MSRMT\_CHARACTERISTIC
    :   Weight Scale Characteristics define

    <a id="_CPPv4NUt1_630GATT_WS_FEATURE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_630GATT_WS_FEATURE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a952531640a3aeacf19acb4d9b8fb02e1"></a> enumerator GATT\_WS\_FEATURE\_CHARACTERISTIC

    <a id="_CPPv4NUt1_628GATT_BC_MSRMT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_628GATT_BC_MSRMT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a10c5e96b6c5c76a18ddbf9cae4ff8782"></a> enumerator GATT\_BC\_MSRMT\_CHARACTERISTIC
    :   Body Composition Characteristics define

    <a id="_CPPv4NUt1_630GATT_BC_FEATURE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_630GATT_BC_FEATURE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a68d2c642cf57d2e92448ba9dfda73659"></a> enumerator GATT\_BC\_FEATURE\_CHARACTERISTIC

    <a id="_CPPv4NUt1_633GATT_UD_FIRST_NAME_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_633GATT_UD_FIRST_NAME_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a1e06bd32015a8bab14f4b69efa9c5ddb"></a> enumerator GATT\_UD\_FIRST\_NAME\_CHARACTERISTIC
    :   User Name Characterictics define

    <a id="_CPPv4NUt1_632GATT_UD_LAST_NAME_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_632GATT_UD_LAST_NAME_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a98c61d5601de7ba03e4c16ce6144b40c"></a> enumerator GATT\_UD\_LAST\_NAME\_CHARACTERISTIC

    <a id="_CPPv4NUt1_628GATT_UD_EMAIL_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_628GATT_UD_EMAIL_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a8da9a626f15e4103ec2227e6eef920e7"></a> enumerator GATT\_UD\_EMAIL\_CHARACTERISTIC

    <a id="_CPPv4NUt1_626GATT_UD_AGE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_626GATT_UD_AGE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a46eb9a4d541834e2dfc769b2735ffa5a"></a> enumerator GATT\_UD\_AGE\_CHARACTERISTIC

    <a id="_CPPv4NUt1_629GATT_UD_GENDER_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_629GATT_UD_GENDER_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ae908551fdf629e19c8d5ade4543c0015"></a> enumerator GATT\_UD\_GENDER\_CHARACTERISTIC

    <a id="_CPPv4NUt1_634GATT_UD_DB_CHNG_INC_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_634GATT_UD_DB_CHNG_INC_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a217dcef56ce2478cff606ff51c5cf795"></a> enumerator GATT\_UD\_DB\_CHNG\_INC\_CHARACTERISTIC

    <a id="_CPPv4NUt1_626GATT_UD_DOB_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_626GATT_UD_DOB_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a37c024968aa41d98fe816703a53b5a0a"></a> enumerator GATT\_UD\_DOB\_CHARACTERISTIC

    <a id="_CPPv4NUt1_629GATT_UD_WEIGHT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_629GATT_UD_WEIGHT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a0f83d86ca4fb40fde7e582dc634c9e3e"></a> enumerator GATT\_UD\_WEIGHT\_CHARACTERISTIC

    <a id="_CPPv4NUt1_629GATT_UD_HEIGHT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_629GATT_UD_HEIGHT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a151960387bb9a5ef82e9755d699da6e9"></a> enumerator GATT\_UD\_HEIGHT\_CHARACTERISTIC

    <a id="_CPPv4NUt1_629GATT_UD_VO2MAX_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_629GATT_UD_VO2MAX_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635af886e87a31e21349d80700ac47723a6c"></a> enumerator GATT\_UD\_VO2MAX\_CHARACTERISTIC

    <a id="_CPPv4NUt1_628GATT_UD_HRMAX_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_628GATT_UD_HRMAX_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635aacba4c0ed9768170ff3fd62b9950a869"></a> enumerator GATT\_UD\_HRMAX\_CHARACTERISTIC

    <a id="_CPPv4NUt1_626GATT_UD_RHR_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_626GATT_UD_RHR_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a4673c428353e9ff53102742e13d4f777"></a> enumerator GATT\_UD\_RHR\_CHARACTERISTIC

    <a id="_CPPv4NUt1_629GATT_UD_MAXRHR_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_629GATT_UD_MAXRHR_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ad1c39c4d9c09c2c3a9f8e664f708ede8"></a> enumerator GATT\_UD\_MAXRHR\_CHARACTERISTIC

    <a id="_CPPv4NUt1_629GATT_UD_AEROTH_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_629GATT_UD_AEROTH_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a5192119d46688c7f0c38a43c50dd412c"></a> enumerator GATT\_UD\_AEROTH\_CHARACTERISTIC

    <a id="_CPPv4NUt1_629GATT_UD_ANAETH_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_629GATT_UD_ANAETH_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635abca2ac8ce95f95411f1cab2db9611abb"></a> enumerator GATT\_UD\_ANAETH\_CHARACTERISTIC

    <a id="_CPPv4NUt1_632GATT_UD_SPORTTYPE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_632GATT_UD_SPORTTYPE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ad5d014724cb919becef77af4c907929b"></a> enumerator GATT\_UD\_SPORTTYPE\_CHARACTERISTIC

    <a id="_CPPv4NUt1_632GATT_UD_DATETHASS_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_632GATT_UD_DATETHASS_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ad88931dcc9d6450ff8e0a543528ec590"></a> enumerator GATT\_UD\_DATETHASS\_CHARACTERISTIC

    <a id="_CPPv4NUt1_631GATT_UD_WAISTCIR_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_631GATT_UD_WAISTCIR_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635aca839b955866522954bc168e337d536b"></a> enumerator GATT\_UD\_WAISTCIR\_CHARACTERISTIC

    <a id="_CPPv4NUt1_629GATT_UD_HIPCIR_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_629GATT_UD_HIPCIR_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a3a5481ae273cbe9a0d9168ac78dd5fc8"></a> enumerator GATT\_UD\_HIPCIR\_CHARACTERISTIC

    <a id="_CPPv4NUt1_634GATT_UD_FATBURN_LOW_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_634GATT_UD_FATBURN_LOW_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a49290b9e22b1bcd8a6036395a72febbc"></a> enumerator GATT\_UD\_FATBURN\_LOW\_CHARACTERISTIC

    <a id="_CPPv4NUt1_634GATT_UD_FATBURN_UPL_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_634GATT_UD_FATBURN_UPL_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ae2a6b3dc0d682e5035bed8c746f29147"></a> enumerator GATT\_UD\_FATBURN\_UPL\_CHARACTERISTIC

    <a id="_CPPv4NUt1_631GATT_UD_AERO_LOW_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_631GATT_UD_AERO_LOW_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635aff5f07dd987d8d4bfd6f605fb4d1d356"></a> enumerator GATT\_UD\_AERO\_LOW\_CHARACTERISTIC

    <a id="_CPPv4NUt1_631GATT_UD_AERO_UPL_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_631GATT_UD_AERO_UPL_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635aecdde129773d6c3fc5a83c7ec7653374"></a> enumerator GATT\_UD\_AERO\_UPL\_CHARACTERISTIC

    <a id="_CPPv4NUt1_631GATT_UD_ANAE_LOW_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_631GATT_UD_ANAE_LOW_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635aa1bda7257d32eb67e99aad3a1baf0116"></a> enumerator GATT\_UD\_ANAE\_LOW\_CHARACTERISTIC

    <a id="_CPPv4NUt1_631GATT_UD_ANAE_UPL_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_631GATT_UD_ANAE_UPL_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635af7cd0895571a38c3af91e0ef0010d227"></a> enumerator GATT\_UD\_ANAE\_UPL\_CHARACTERISTIC

    <a id="_CPPv4NUt1_635GATT_UD_FIVEZONE_HRL_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_635GATT_UD_FIVEZONE_HRL_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a122ba8b1c79bce3b22712ae0c97fb386"></a> enumerator GATT\_UD\_FIVEZONE\_HRL\_CHARACTERISTIC

    <a id="_CPPv4NUt1_636GATT_UD_THREEZONE_HRL_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_636GATT_UD_THREEZONE_HRL_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635af6fb69def0757ae1b1071f4b61965dc6"></a> enumerator GATT\_UD\_THREEZONE\_HRL\_CHARACTERISTIC

    <a id="_CPPv4NUt1_634GATT_UD_TWOZONE_HRL_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_634GATT_UD_TWOZONE_HRL_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635af1bf0feb7cca0055b2db12a97e6cc129"></a> enumerator GATT\_UD\_TWOZONE\_HRL\_CHARACTERISTIC

    <a id="_CPPv4NUt1_633GATT_UD_USER_INDEX_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_633GATT_UD_USER_INDEX_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a89f19cef3803753bec0af5c4e78fc060"></a> enumerator GATT\_UD\_USER\_INDEX\_CHARACTERISTIC

    <a id="_CPPv4NUt1_637GATT_UD_USER_CNTRL_PNT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_637GATT_UD_USER_CNTRL_PNT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a59f7d0d00ed3662e5cb4d62dc8dc5311"></a> enumerator GATT\_UD\_USER\_CNTRL\_PNT\_CHARACTERISTIC

    <a id="_CPPv4NUt1_631GATT_UD_LANGUAGE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_631GATT_UD_LANGUAGE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ae7ec2ae776aefd950c2bdd7a9a159404"></a> enumerator GATT\_UD\_LANGUAGE\_CHARACTERISTIC

    <a id="_CPPv4NUt1_638GATT_UD_REGISTERED_USER_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_638GATT_UD_REGISTERED_USER_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a22b2ef37fd46ad733c0ab0001f534366"></a> enumerator GATT\_UD\_REGISTERED\_USER\_CHARACTERISTIC

    <a id="_CPPv4NUt1_627GATT_ESS_DVC_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_627GATT_ESS_DVC_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a200f6a2deb004f578caf50b217d76446"></a> enumerator GATT\_ESS\_DVC\_CHARACTERISTIC
    :   Environmental Sensing Characterisitcs define

    <a id="_CPPv4NUt1_628GATT_ESS_TEMP_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_628GATT_ESS_TEMP_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ae0710d11a00fde82a02a11427b16ab27"></a> enumerator GATT\_ESS\_TEMP\_CHARACTERISTIC

    <a id="_CPPv4NUt1_629GATT_ES_MEASURMENT_DESCRIPTORE"></a>

    <a id="_CPPv3NUt1_629GATT_ES_MEASURMENT_DESCRIPTORE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ab2c80ad3794e8786ec1a222a70b776a3"></a> enumerator GATT\_ES\_MEASURMENT\_DESCRIPTOR

    <a id="_CPPv4NUt1_634GATT_ES_TRIGGER_SETTING_DESCRIPTORE"></a>

    <a id="_CPPv3NUt1_634GATT_ES_TRIGGER_SETTING_DESCRIPTORE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a8868a4176e04e849ef99eaebb248d0d4"></a> enumerator GATT\_ES\_TRIGGER\_SETTING\_DESCRIPTOR

    <a id="_CPPv4NUt1_632GATT_ES_CONFIGURATION_DESCRIPTORE"></a>

    <a id="_CPPv3NUt1_632GATT_ES_CONFIGURATION_DESCRIPTORE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635af288e84900ce7bc591f776afb81f7aaf"></a> enumerator GATT\_ES\_CONFIGURATION\_DESCRIPTOR

    <a id="_CPPv4NUt1_630GATT_ES_MEASUREMENT_DESCRIPTORE"></a>

    <a id="_CPPv3NUt1_630GATT_ES_MEASUREMENT_DESCRIPTORE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635aa034387e555d1cf3da4a75bf30763acc"></a> enumerator GATT\_ES\_MEASUREMENT\_DESCRIPTOR

    <a id="_CPPv4NUt1_631GATT_BM_FEATURES_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_631GATT_BM_FEATURES_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a1f240b9ee91c0586695a5710a73f013f"></a> enumerator GATT\_BM\_FEATURES\_CHARACTERISTIC
    :   Bond Management Characteritiscs defines

    <a id="_CPPv4NUt1_632GATT_BM_CNTRL_PNT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_632GATT_BM_CNTRL_PNT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635afcebc7cecdf406dc68032bb9d706899c"></a> enumerator GATT\_BM\_CNTRL\_PNT\_CHARACTERISTIC

    <a id="_CPPv4NUt1_631GATT_AIO_DIGITAL_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_631GATT_AIO_DIGITAL_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a2a7f41b341f54969eb5a95cb52994bb9"></a> enumerator GATT\_AIO\_DIGITAL\_CHARACTERISTIC
    :   Automation IO Service Characteritiscs defines

    <a id="_CPPv4NUt1_630GATT_AIO_ANALOG_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_630GATT_AIO_ANALOG_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a5886a0fa486b4a01bf3d205dd37ae9ac"></a> enumerator GATT\_AIO\_ANALOG\_CHARACTERISTIC

    <a id="_CPPv4NUt1_633GATT_AIO_AGGREGATE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_633GATT_AIO_AGGREGATE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a2246cd8bd7487cce76c6bc980299b7a6"></a> enumerator GATT\_AIO\_AGGREGATE\_CHARACTERISTIC

    <a id="_CPPv4NUt1_640GATT_IP_INDOOR_POS_CONFIG_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_640GATT_IP_INDOOR_POS_CONFIG_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a9e44092b0d5a92b29391b6ec21ef1b9e"></a> enumerator GATT\_IP\_INDOOR\_POS\_CONFIG\_CHARACTERISTIC
    :   Indoor Positioning Characteritiscs defines

    <a id="_CPPv4NUt1_631GATT_IP_LATITUDE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_631GATT_IP_LATITUDE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ad97c987db07ade7f773587f4d28025e9"></a> enumerator GATT\_IP\_LATITUDE\_CHARACTERISTIC

    <a id="_CPPv4NUt1_632GATT_IP_LONGITUDE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_632GATT_IP_LONGITUDE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635afdfbf54b1853ea8388d8329653cb6396"></a> enumerator GATT\_IP\_LONGITUDE\_CHARACTERISTIC

    <a id="_CPPv4NUt1_634GATT_IP_LOCAL_NORTH_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_634GATT_IP_LOCAL_NORTH_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635abbfba03ad8fb07cc8a2a8774648dfe9f"></a> enumerator GATT\_IP\_LOCAL\_NORTH\_CHARACTERISTIC

    <a id="_CPPv4NUt1_633GATT_IP_LOCAL_EAST_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_633GATT_IP_LOCAL_EAST_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ad002e4afc65e14977f98e84323658f79"></a> enumerator GATT\_IP\_LOCAL\_EAST\_CHARACTERISTIC

    <a id="_CPPv4NUt1_632GATT_IP_FLOOR_NUM_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_632GATT_IP_FLOOR_NUM_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ab8b39c9a7a744989379663e49e341abf"></a> enumerator GATT\_IP\_FLOOR\_NUM\_CHARACTERISTIC

    <a id="_CPPv4NUt1_631GATT_IP_ALTITUDE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_631GATT_IP_ALTITUDE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a27d24a87c126608d424f2542c62a3e6c"></a> enumerator GATT\_IP\_ALTITUDE\_CHARACTERISTIC

    <a id="_CPPv4NUt1_634GATT_IP_UNCERTAINTY_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_634GATT_IP_UNCERTAINTY_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a827a00de9c0d902d1416768acbb6ffca"></a> enumerator GATT\_IP\_UNCERTAINTY\_CHARACTERISTIC

    <a id="_CPPv4NUt1_633GATT_IP_LOCAL_NAME_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_633GATT_IP_LOCAL_NAME_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a60467a43285419ac4ea93b667904d485"></a> enumerator GATT\_IP\_LOCAL\_NAME\_CHARACTERISTIC

    <a id="_CPPv4NUt1_631GATT_OTS_FEATURE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_631GATT_OTS_FEATURE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a5c948bb2192c916f34541a99c346cdb5"></a> enumerator GATT\_OTS\_FEATURE\_CHARACTERISTIC
    :   Object Transfer Characteritics defines

    <a id="_CPPv4NUt1_632GATT_OTS_OBJ_NAME_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_632GATT_OTS_OBJ_NAME_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a07ff77692a4e977401ea0bed5fd74392"></a> enumerator GATT\_OTS\_OBJ\_NAME\_CHARACTERISTIC

    <a id="_CPPv4NUt1_632GATT_OTS_OBJ_TYPE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_632GATT_OTS_OBJ_TYPE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a92b19c790c532ac5035fc68cc9dab5a4"></a> enumerator GATT\_OTS\_OBJ\_TYPE\_CHARACTERISTIC

    <a id="_CPPv4NUt1_632GATT_OTS_OBJ_SIZE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_632GATT_OTS_OBJ_SIZE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a36aa611b7438dbde5d4753304255c2fb"></a> enumerator GATT\_OTS\_OBJ\_SIZE\_CHARACTERISTIC

    <a id="_CPPv4NUt1_638GATT_OTS_OBJ_FIRST_CRTD_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_638GATT_OTS_OBJ_FIRST_CRTD_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635aed88433bd66a469e59670c87da26376a"></a> enumerator GATT\_OTS\_OBJ\_FIRST\_CRTD\_CHARACTERISTIC

    <a id="_CPPv4NUt1_638GATT_OTS_OBJ_LAST_MODFD_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_638GATT_OTS_OBJ_LAST_MODFD_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a332dc2bff2d6d950789aa9b2c360b6c5"></a> enumerator GATT\_OTS\_OBJ\_LAST\_MODFD\_CHARACTERISTIC

    <a id="_CPPv4NUt1_630GATT_OTS_OBJ_ID_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_630GATT_OTS_OBJ_ID_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a46514e056e2757f5ddc099fabe6e0018"></a> enumerator GATT\_OTS\_OBJ\_ID\_CHARACTERISTIC

    <a id="_CPPv4NUt1_633GATT_OTS_OBJ_PRPTY_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_633GATT_OTS_OBJ_PRPTY_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a87ee101c9cd058ae887e609b89164568"></a> enumerator GATT\_OTS\_OBJ\_PRPTY\_CHARACTERISTIC

    <a id="_CPPv4NUt1_628GATT_OTS_OACP_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_628GATT_OTS_OACP_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a5dc1dc6359c76103c1189e75b7742c88"></a> enumerator GATT\_OTS\_OACP\_CHARACTERISTIC

    <a id="_CPPv4NUt1_628GATT_OTS_OLCP_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_628GATT_OTS_OLCP_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a3b4f9eb0f587a89eb79c3aa80a9a4544"></a> enumerator GATT\_OTS\_OLCP\_CHARACTERISTIC

    <a id="_CPPv4NUt1_639GATT_OTS_OBJ_LIST_FILTER_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_639GATT_OTS_OBJ_LIST_FILTER_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a1bfe30d3f76fac5f47389d9925d8a0c2"></a> enumerator GATT\_OTS\_OBJ\_LIST\_FILTER\_CHARACTERISTIC

    <a id="_CPPv4NUt1_635GATT_OTS_OBJ_CHANGED_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_635GATT_OTS_OBJ_CHANGED_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a2e18d77580099a633deb8f1a79f0300b"></a> enumerator GATT\_OTS\_OBJ\_CHANGED\_CHARACTERISTIC

    <a id="_CPPv4NUt1_630GATT_OTS_LE_PSM_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_630GATT_OTS_LE_PSM_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635af8ff1b1c9850012ca4f23043d38cd1ca"></a> enumerator GATT\_OTS\_LE\_PSM\_CHARACTERISTIC

    <a id="_CPPv4NUt1_638GATT_OTS_OBJ_LAST_ACCSD_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_638GATT_OTS_OBJ_LAST_ACCSD_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a1030c3249afaf0087e3681ca68c49dda"></a> enumerator GATT\_OTS\_OBJ\_LAST\_ACCSD\_CHARACTERISTIC

    <a id="_CPPv4NUt1_636GATT_OTS_OBJ_CHECKSUM_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_636GATT_OTS_OBJ_CHECKSUM_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ac73c34fefa86fbe2300772eaee0f6a4a"></a> enumerator GATT\_OTS\_OBJ\_CHECKSUM\_CHARACTERISTIC

    <a id="_CPPv4NUt1_637GATT_OTS_OCTECT_OFFSET_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_637GATT_OTS_OCTECT_OFFSET_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635aafc33ccff5f66407385bc384c50a24cf"></a> enumerator GATT\_OTS\_OCTECT\_OFFSET\_CHARACTERISTIC

    <a id="_CPPv4NUt1_637GATT_TPM_TIRE_PRESSURE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_637GATT_TPM_TIRE_PRESSURE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635adb157f45f925cccef2cfe2b214fad9b5"></a> enumerator GATT\_TPM\_TIRE\_PRESSURE\_CHARACTERISTIC
    :   Tire Pressure Monitoring Characteritiscs defines Needs to update the opcode once TPMS spec is adopted

    <a id="_CPPv4NUt1_633GATT_TPM_TIRE_TEMP_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_633GATT_TPM_TIRE_TEMP_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a21e8b42a39535950d15fac16dbbe4fcc"></a> enumerator GATT\_TPM\_TIRE\_TEMP\_CHARACTERISTIC

    <a id="_CPPv4NUt1_639GATT_TPM_PRESSURE_CALIBN_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_639GATT_TPM_PRESSURE_CALIBN_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635aeba17fd7caeea1ce0345c87d63ababd7"></a> enumerator GATT\_TPM\_PRESSURE\_CALIBN\_CHARACTERISTIC

    <a id="_CPPv4NUt1_635GATT_TPM_TEMP_CALIBN_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_635GATT_TPM_TEMP_CALIBN_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635af3234b3bebd8548df8a9f58607add0aa"></a> enumerator GATT\_TPM\_TEMP\_CALIBN\_CHARACTERISTIC

    <a id="_CPPv4NUt1_640GATT_TPM_DISRY_CONN_MGMNT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_640GATT_TPM_DISRY_CONN_MGMNT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a42fd339d2cee1516538a7c997cc64507"></a> enumerator GATT\_TPM\_DISRY\_CONN\_MGMNT\_CHARACTERISTIC

    <a id="_CPPv4NUt1_634GATT_TPM_ADV_PERIOD_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_634GATT_TPM_ADV_PERIOD_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a14fbb70c3f8d360dd0deb70ea1c2b00b"></a> enumerator GATT\_TPM\_ADV\_PERIOD\_CHARACTERISTIC

    <a id="_CPPv4NUt1_636GATT_TD_CONTROL_POINT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_636GATT_TD_CONTROL_POINT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635aa8d5323fb85448e95007a57eb417a891"></a> enumerator GATT\_TD\_CONTROL\_POINT\_CHARACTERISTIC
    :   Transport Discovery Characteristics defines

    <a id="_CPPv4NUt1_627GATT_HPC_URI_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_627GATT_HPC_URI_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a8005fe45849d0c5cc42c4e934427ab34"></a> enumerator GATT\_HPC\_URI\_CHARACTERISTIC
    :   HTTP Proxy Characteristics defines

    <a id="_CPPv4NUt1_636GATT_HPC_HTTP_HEADERS_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_636GATT_HPC_HTTP_HEADERS_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a3ed662e497e461bbba762ff900b6312a"></a> enumerator GATT\_HPC\_HTTP\_HEADERS\_CHARACTERISTIC

    <a id="_CPPv4NUt1_640GATT_HPC_HTTP_ENTITY_BODY_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_640GATT_HPC_HTTP_ENTITY_BODY_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a3405b72ee48dae0286072abe89137e18"></a> enumerator GATT\_HPC\_HTTP\_ENTITY\_BODY\_CHARACTERISTIC

    <a id="_CPPv4NUt1_631GATT_HPC_HTTP_CP_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_631GATT_HPC_HTTP_CP_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a4fe1ce3bd75000c14a826a6b42521e3a"></a> enumerator GATT\_HPC\_HTTP\_CP\_CHARACTERISTIC

    <a id="_CPPv4NUt1_640GATT_HPC_HTTP_STATUS_CODE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_640GATT_HPC_HTTP_STATUS_CODE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a41d70964e85d1f8c6a7d2e3b96a0156c"></a> enumerator GATT\_HPC\_HTTP\_STATUS\_CODE\_CHARACTERISTIC

    <a id="_CPPv4NUt1_638GATT_HPC_HTTPS_SECURITY_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_638GATT_HPC_HTTPS_SECURITY_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a7092f54cea4fadc150a25a5fba1b92fa"></a> enumerator GATT\_HPC\_HTTPS\_SECURITY\_CHARACTERISTIC

    <a id="_CPPv4NUt1_631GATT_FTM_FEATURE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_631GATT_FTM_FEATURE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a7c6745a91fa84e08b66ca22436506fdd"></a> enumerator GATT\_FTM\_FEATURE\_CHARACTERISTIC
    :   Fitness Machine Characteristics defines

    <a id="_CPPv4NUt1_633GATT_FTM_TREADMILL_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_633GATT_FTM_TREADMILL_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635af8ed5003ed69eb42ef4b24267c06f298"></a> enumerator GATT\_FTM\_TREADMILL\_CHARACTERISTIC

    <a id="_CPPv4NUt1_637GATT_FTM_CROSS_TRAINER_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_637GATT_FTM_CROSS_TRAINER_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635af763c50e9c27a8ba849f3e5ba014b5c6"></a> enumerator GATT\_FTM\_CROSS\_TRAINER\_CHARACTERISTIC

    <a id="_CPPv4NUt1_636GATT_FTM_STEP_CLIMBER_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_636GATT_FTM_STEP_CLIMBER_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a38587178d7d10e2041eccd45126476f0"></a> enumerator GATT\_FTM\_STEP\_CLIMBER\_CHARACTERISTIC

    <a id="_CPPv4NUt1_637GATT_FTM_STAIR_CLIMBER_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_637GATT_FTM_STAIR_CLIMBER_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a55540e226baf6fb6c234f68f851ae05b"></a> enumerator GATT\_FTM\_STAIR\_CLIMBER\_CHARACTERISTIC

    <a id="_CPPv4NUt1_634GATT_FTM_ROWER_DATA_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_634GATT_FTM_ROWER_DATA_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635aea7fdb9f43bbde5ae4cbad0a16e9294d"></a> enumerator GATT\_FTM\_ROWER\_DATA\_CHARACTERISTIC

    <a id="_CPPv4NUt1_635GATT_FTM_INDOOR_BIKE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_635GATT_FTM_INDOOR_BIKE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635afa125f86d2d9636ae9efe9f34c5c9562"></a> enumerator GATT\_FTM\_INDOOR\_BIKE\_CHARACTERISTIC

    <a id="_CPPv4NUt1_639GATT_FTM_TRAINING_STATUS_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_639GATT_FTM_TRAINING_STATUS_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a50050e45a33d5665e20b07885582f0f3"></a> enumerator GATT\_FTM\_TRAINING\_STATUS\_CHARACTERISTIC

    <a id="_CPPv4NUt1_639GATT_FTM_SUPPD_SPEED_RNG_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_639GATT_FTM_SUPPD_SPEED_RNG_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ac7f704edd53f5656a4997bbfb936fbb3"></a> enumerator GATT\_FTM\_SUPPD\_SPEED\_RNG\_CHARACTERISTIC

    <a id="_CPPv4NUt1_639GATT_FTM_SUPPD_INCLN_RNG_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_639GATT_FTM_SUPPD_INCLN_RNG_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a0006a296f0e2b11b9a713dc6f631fa91"></a> enumerator GATT\_FTM\_SUPPD\_INCLN\_RNG\_CHARACTERISTIC

    <a id="_CPPv4NUt1_639GATT_FTM_SUPPD_RESIS_RNG_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_639GATT_FTM_SUPPD_RESIS_RNG_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ab7b332d74fc5a7ab1c0aa33bf8567e6e"></a> enumerator GATT\_FTM\_SUPPD\_RESIS\_RNG\_CHARACTERISTIC

    <a id="_CPPv4NUt1_639GATT_FTM_SUPPD_POWER_RNG_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_639GATT_FTM_SUPPD_POWER_RNG_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ac6b1660a37b1daa714f1d99ffc2a8b16"></a> enumerator GATT\_FTM\_SUPPD\_POWER\_RNG\_CHARACTERISTIC

    <a id="_CPPv4NUt1_639GATT_FTM_SUPPD_HRTRE_RNG_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_639GATT_FTM_SUPPD_HRTRE_RNG_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a823ccf4b5e583d63cb0e0324ae530b5a"></a> enumerator GATT\_FTM\_SUPPD\_HRTRE\_RNG\_CHARACTERISTIC

    <a id="_CPPv4NUt1_637GATT_FTM_CONTROL_POINT_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_637GATT_FTM_CONTROL_POINT_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ad308c0340979524b98b9d4954bdab8c4"></a> enumerator GATT\_FTM\_CONTROL\_POINT\_CHARACTERISTIC

    <a id="_CPPv4NUt1_638GATT_FTM_MACHINE_STATUS_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_638GATT_FTM_MACHINE_STATUS_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a284aee79308ceac1a93ffd11c874069f"></a> enumerator GATT\_FTM\_MACHINE\_STATUS\_CHARACTERISTIC

    <a id="_CPPv4NUt1_630GATT_RC_FEATURE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_630GATT_RC_FEATURE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a41201118d676a60a32214cc88f62926d"></a> enumerator GATT\_RC\_FEATURE\_CHARACTERISTIC
    :   Reconnection Configuration Characteristic defines

    <a id="_CPPv4NUt1_630GATT_RC_SETTING_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_630GATT_RC_SETTING_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a9c8c00e9a1bbc43f4d2fd451d2b902f7"></a> enumerator GATT\_RC\_SETTING\_CHARACTERISTIC

    <a id="_CPPv4NUt1_625GATT_RC_CP_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_625GATT_RC_CP_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a12b3db93026e1e35aca7ff4a1062d8d3"></a> enumerator GATT\_RC\_CP\_CHARACTERISTIC

    <a id="_CPPv4NUt1_638GATT_IDD_STATUS_CHANGED_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_638GATT_IDD_STATUS_CHANGED_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635aafc8cbe6d11da792b745b1e8d9944ccf"></a> enumerator GATT\_IDD\_STATUS\_CHANGED\_CHARACTERISTIC
    :   Insulin Delivery Characteristics defines

    <a id="_CPPv4NUt1_630GATT_IDD_STATUS_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_630GATT_IDD_STATUS_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ad0cb0dfbab93d7a6206f482421e32e24"></a> enumerator GATT\_IDD\_STATUS\_CHARACTERISTIC

    <a id="_CPPv4NUt1_636GATT_IDD_ANNUN_STATUS_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_636GATT_IDD_ANNUN_STATUS_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635abd8c76c7c80db288233469a99a659a2c"></a> enumerator GATT\_IDD\_ANNUN\_STATUS\_CHARACTERISTIC

    <a id="_CPPv4NUt1_631GATT_IDD_FEATURE_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_631GATT_IDD_FEATURE_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a76dff03cd76b35a1b9913730d9c8ce98"></a> enumerator GATT\_IDD\_FEATURE\_CHARACTERISTIC

    <a id="_CPPv4NUt1_640GATT_IDD_STATUS_READER_CP_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_640GATT_IDD_STATUS_READER_CP_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635ae814b0c81aae31ed95f6df7768730e29"></a> enumerator GATT\_IDD\_STATUS\_READER\_CP\_CHARACTERISTIC

    <a id="_CPPv4NUt1_634GATT_IDD_COMMAND_CP_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_634GATT_IDD_COMMAND_CP_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a7a159fff393a6c842204f72bbf6b234f"></a> enumerator GATT\_IDD\_COMMAND\_CP\_CHARACTERISTIC

    <a id="_CPPv4NUt1_636GATT_IDD_COMMAND_DATA_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_636GATT_IDD_COMMAND_DATA_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a6684170eef67362a7b7fd6346f83c69a"></a> enumerator GATT\_IDD\_COMMAND\_DATA\_CHARACTERISTIC

    <a id="_CPPv4NUt1_628GATT_IDD_RACP_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_628GATT_IDD_RACP_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a8b013d721a3bc4b7d5353eebb0bd6f27"></a> enumerator GATT\_IDD\_RACP\_CHARACTERISTIC

    <a id="_CPPv4NUt1_636GATT_IDD_HISTORY_DATA_CHARACTERISTICE"></a>

    <a id="_CPPv3NUt1_636GATT_IDD_HISTORY_DATA_CHARACTERISTICE"></a> <a id="dm__ble__types_8h_1a726ca809ffd3d67ab4b8476646f26635a93c0723ab8cf1c86676df983f88025ad"></a> enumerator GATT\_IDD\_HISTORY\_DATA\_CHARACTERISTIC

<a id="_CPPv4Ut1_7"></a>

<a id="_CPPv3Ut1_7"></a> <a id="dm__ble__types_8h_1a0411cd49bb5b71852cecd93bcbf0ca2d"></a> enum \[anonymous\]
:   only use for Operations Notified In Characteristic Callback

    *Values:*

    <a id="_CPPv4NUt1_712GATT_DB_READE"></a>

    <a id="_CPPv3NUt1_712GATT_DB_READE"></a> <a id="dm__ble__types_8h_1a0411cd49bb5b71852cecd93bcbf0ca2da177dc8e5a6d4271b3fe4f8b1c9811871"></a> enumerator GATT\_DB\_READ
    :   Read operation for Attribute

    <a id="_CPPv4NUt1_713GATT_DB_WRITEE"></a>

    <a id="_CPPv3NUt1_713GATT_DB_WRITEE"></a> <a id="dm__ble__types_8h_1a0411cd49bb5b71852cecd93bcbf0ca2da6ffad990a4e9bb5690ac48bb2aaeac0a"></a> enumerator GATT\_DB\_WRITE
    :   Write operation for Attribute

    <a id="_CPPv4NUt1_717GATT_DB_READ_BLOBE"></a>

    <a id="_CPPv3NUt1_717GATT_DB_READ_BLOBE"></a> <a id="dm__ble__types_8h_1a0411cd49bb5b71852cecd93bcbf0ca2da2231e83b150e1c6f351e65fd07270c97"></a> enumerator GATT\_DB\_READ\_BLOB
    :   Read blob operation for Attribute

    <a id="_CPPv4NUt1_725GATT_DB_WRITE_WITHOUT_RSPE"></a>

    <a id="_CPPv3NUt1_725GATT_DB_WRITE_WITHOUT_RSPE"></a> <a id="dm__ble__types_8h_1a0411cd49bb5b71852cecd93bcbf0ca2dafa40e5411e1ccca43b9b667eca5e596c"></a> enumerator GATT\_DB\_WRITE\_WITHOUT\_RSP
    :   Write Without Response operation for Attribute

    <a id="_CPPv4NUt1_720GATT_DB_READ_BY_TYPEE"></a>

    <a id="_CPPv3NUt1_720GATT_DB_READ_BY_TYPEE"></a> <a id="dm__ble__types_8h_1a0411cd49bb5b71852cecd93bcbf0ca2da10146b20f410e63e7a4637099c390208"></a> enumerator GATT\_DB\_READ\_BY\_TYPE
    :   Read by UUID/Type operation for Attribute

    <a id="_CPPv4NUt1_720GATT_DB_SIGNED_WRITEE"></a>

    <a id="_CPPv3NUt1_720GATT_DB_SIGNED_WRITEE"></a> <a id="dm__ble__types_8h_1a0411cd49bb5b71852cecd93bcbf0ca2da8e5f0898bb9831f56a944f7905dae0b4"></a> enumerator GATT\_DB\_SIGNED\_WRITE
    :   Signed Write operation for Attribute

    <a id="_CPPv4NUt1_715GATT_DB_EXECUTEE"></a>

    <a id="_CPPv3NUt1_715GATT_DB_EXECUTEE"></a> <a id="dm__ble__types_8h_1a0411cd49bb5b71852cecd93bcbf0ca2dab839575b3d7d2540a8724670e8aea533"></a> enumerator GATT\_DB\_EXECUTE
    :   Execute Write operation for Attribute

    <a id="_CPPv4NUt1_715GATT_DB_PREPAREE"></a>

    <a id="_CPPv3NUt1_715GATT_DB_PREPAREE"></a> <a id="dm__ble__types_8h_1a0411cd49bb5b71852cecd93bcbf0ca2da248c5f671cb5b41e0e1c9b1c3de30c1d"></a> enumerator GATT\_DB\_PREPARE
    :   Prepare Write operation for Attribute

    <a id="_CPPv4NUt1_714GATT_DB_UPDATEE"></a>

    <a id="_CPPv3NUt1_714GATT_DB_UPDATEE"></a> <a id="dm__ble__types_8h_1a0411cd49bb5b71852cecd93bcbf0ca2daaf750cf55ee2ae464bcef44a94197786"></a> enumerator GATT\_DB\_UPDATE
    :   Local update of a Readable Attribute Value using [GATT\_DB\_HANDLE](#structGATT__DB__HANDLE) instead of Attribute Handle. See BT\_gatt\_db\_set\_char\_val for more details.

    <a id="_CPPv4NUt1_727GATT_DB_128_BIT_UUID_FORMATE"></a>

    <a id="_CPPv3NUt1_727GATT_DB_128_BIT_UUID_FORMATE"></a> <a id="dm__ble__types_8h_1a0411cd49bb5b71852cecd93bcbf0ca2da2c267972442b04a3289e9e462b033b7e"></a> enumerator GATT\_DB\_128\_BIT\_UUID\_FORMAT
    :   128 Bit Attribute UUID

    <a id="_CPPv4NUt1_722GATT_DB_PEER_INITIATEDE"></a>

    <a id="_CPPv3NUt1_722GATT_DB_PEER_INITIATEDE"></a> <a id="dm__ble__types_8h_1a0411cd49bb5b71852cecd93bcbf0ca2da3d35a0baf83fc5079896cac2af193854"></a> enumerator GATT\_DB\_PEER\_INITIATED
    :   Peer initiated operation, needed when Peer is Reading or Writing Values either using GATT Read Procedures for Value and Descriptors.

    <a id="_CPPv4NUt1_725GATT_DB_LOCALLY_INITIATEDE"></a>

    <a id="_CPPv3NUt1_725GATT_DB_LOCALLY_INITIATEDE"></a> <a id="dm__ble__types_8h_1a0411cd49bb5b71852cecd93bcbf0ca2da8040ef7cbb7fb0f1f1d7ed61d4421a8a"></a> enumerator GATT\_DB\_LOCALLY\_INITIATED
    :   Locally initiated operation, needed for local updates based on Attribute Handles. In case [GATT\_DB\_HANDLE](#structGATT__DB__HANDLE) is known, use of access through GATT\_DB\_UPDATE is recommended.

<a id="_CPPv4Ut1_8"></a>

<a id="_CPPv3Ut1_8"></a> <a id="group__gatt__db__operations_1gabed82baf7f470b522273a3e37c24c600"></a> enum \[anonymous\]
:   *Values:*

    <a id="_CPPv4NUt1_827GATT_DB_CHAR_VALUE_READ_REQE"></a>

    <a id="_CPPv3NUt1_827GATT_DB_CHAR_VALUE_READ_REQE"></a> <a id="group__gatt__db__operations_1ggabed82baf7f470b522273a3e37c24c600ac027770cd4c786e6ebf57ccb4b4faf7a"></a> enumerator GATT\_DB\_CHAR\_VALUE\_READ\_REQ
    :   Characteristic Value Local Read Operation

    <a id="_CPPv4NUt1_828GATT_DB_CHAR_VALUE_WRITE_REQE"></a>

    <a id="_CPPv3NUt1_828GATT_DB_CHAR_VALUE_WRITE_REQE"></a> <a id="group__gatt__db__operations_1ggabed82baf7f470b522273a3e37c24c600a4a46bdadeeda0e3cd647988d0541b57e"></a> enumerator GATT\_DB\_CHAR\_VALUE\_WRITE\_REQ
    :   Characteristic Value Local Write Operation

    <a id="_CPPv4NUt1_836GATT_DB_CHAR_VALUE_WRITE_WITHOUT_REQE"></a>

    <a id="_CPPv3NUt1_836GATT_DB_CHAR_VALUE_WRITE_WITHOUT_REQE"></a> <a id="group__gatt__db__operations_1ggabed82baf7f470b522273a3e37c24c600a5ba3ab331e2649568a61b7a56ed59b49"></a> enumerator GATT\_DB\_CHAR\_VALUE\_WRITE\_WITHOUT\_REQ
    :   Characteristic Value Local Write Without Response Operation

    <a id="_CPPv4NUt1_830GATT_DB_CHAR_CLI_CNFG_READ_REQE"></a>

    <a id="_CPPv3NUt1_830GATT_DB_CHAR_CLI_CNFG_READ_REQE"></a> <a id="group__gatt__db__operations_1ggabed82baf7f470b522273a3e37c24c600a94a3b5ca3ae79643a3e941b9a2a4f7df"></a> enumerator GATT\_DB\_CHAR\_CLI\_CNFG\_READ\_REQ
    :   Characteristic Client Configuration Local Read Operation

    <a id="_CPPv4NUt1_831GATT_DB_CHAR_CLI_CNFG_WRITE_REQE"></a>

    <a id="_CPPv3NUt1_831GATT_DB_CHAR_CLI_CNFG_WRITE_REQE"></a> <a id="group__gatt__db__operations_1ggabed82baf7f470b522273a3e37c24c600aeac3d95077c91bc2ce6dbe243a66f21e"></a> enumerator GATT\_DB\_CHAR\_CLI\_CNFG\_WRITE\_REQ
    :   Characteristic Client Configuration Local Write Operation

    <a id="_CPPv4NUt1_830GATT_DB_CHAR_SER_CNFG_READ_REQE"></a>

    <a id="_CPPv3NUt1_830GATT_DB_CHAR_SER_CNFG_READ_REQE"></a> <a id="group__gatt__db__operations_1ggabed82baf7f470b522273a3e37c24c600a0558672c736d515be0463859c3fff3cb"></a> enumerator GATT\_DB\_CHAR\_SER\_CNFG\_READ\_REQ
    :   Characteristic Server Configuration Local Read Operation

    <a id="_CPPv4NUt1_831GATT_DB_CHAR_SER_CNFG_WRITE_REQE"></a>

    <a id="_CPPv3NUt1_831GATT_DB_CHAR_SER_CNFG_WRITE_REQE"></a> <a id="group__gatt__db__operations_1ggabed82baf7f470b522273a3e37c24c600a29df99c82d214064e7e9e036d95ea9a6"></a> enumerator GATT\_DB\_CHAR\_SER\_CNFG\_WRITE\_REQ
    :   Characteristic Server Configuration Local Write Operation

    <a id="_CPPv4NUt1_826GATT_DB_CHAR_PEER_READ_REQE"></a>

    <a id="_CPPv3NUt1_826GATT_DB_CHAR_PEER_READ_REQE"></a> <a id="group__gatt__db__operations_1ggabed82baf7f470b522273a3e37c24c600a61a516866cd39e8f02f29096ae3f191a"></a> enumerator GATT\_DB\_CHAR\_PEER\_READ\_REQ
    :   Characteristic Value Peer Read Operation

    <a id="_CPPv4NUt1_827GATT_DB_CHAR_PEER_WRITE_REQE"></a>

    <a id="_CPPv3NUt1_827GATT_DB_CHAR_PEER_WRITE_REQE"></a> <a id="group__gatt__db__operations_1ggabed82baf7f470b522273a3e37c24c600a3f62c7fb37f67962d4a02e58d7c66858"></a> enumerator GATT\_DB\_CHAR\_PEER\_WRITE\_REQ
    :   Characteristic Value Peer Write Operation

    <a id="_CPPv4NUt1_831GATT_DB_CHAR_PEER_READ_BLOB_REQE"></a>

    <a id="_CPPv3NUt1_831GATT_DB_CHAR_PEER_READ_BLOB_REQE"></a> <a id="group__gatt__db__operations_1ggabed82baf7f470b522273a3e37c24c600a07e16c735e0b8ba96a6a405b4a2ff010"></a> enumerator GATT\_DB\_CHAR\_PEER\_READ\_BLOB\_REQ
    :   Characteristic Value Peer Read Blob Operation

    <a id="_CPPv4NUt1_827GATT_DB_CHAR_PEER_WRITE_CMDE"></a>

    <a id="_CPPv3NUt1_827GATT_DB_CHAR_PEER_WRITE_CMDE"></a> <a id="group__gatt__db__operations_1ggabed82baf7f470b522273a3e37c24c600ae21c8ea3e0f57c82ca813c2c9b22892f"></a> enumerator GATT\_DB\_CHAR\_PEER\_WRITE\_CMD
    :   Characteristic Value Peer Write Command

    <a id="_CPPv4NUt1_834GATT_DB_CHAR_PEER_READ_BY_TYPE_REQE"></a>

    <a id="_CPPv3NUt1_834GATT_DB_CHAR_PEER_READ_BY_TYPE_REQE"></a> <a id="group__gatt__db__operations_1ggabed82baf7f470b522273a3e37c24c600a157df9b48d0f0440d6df7eb08fd89535"></a> enumerator GATT\_DB\_CHAR\_PEER\_READ\_BY\_TYPE\_REQ
    :   Characteristic Value Peer Read by Type Operation

    <a id="_CPPv4NUt1_834GATT_DB_CHAR_PEER_SIGNED_WRITE_CMDE"></a>

    <a id="_CPPv3NUt1_834GATT_DB_CHAR_PEER_SIGNED_WRITE_CMDE"></a> <a id="group__gatt__db__operations_1ggabed82baf7f470b522273a3e37c24c600ad22fd7b3000f0aff9cc24ecac8c3acd9"></a> enumerator GATT\_DB\_CHAR\_PEER\_SIGNED\_WRITE\_CMD
    :   Characteristic Value Peer Signed Write Operation

    <a id="_CPPv4NUt1_835GATT_DB_CHAR_PEER_EXECUTE_WRITE_REQE"></a>

    <a id="_CPPv3NUt1_835GATT_DB_CHAR_PEER_EXECUTE_WRITE_REQE"></a> <a id="group__gatt__db__operations_1ggabed82baf7f470b522273a3e37c24c600ae7306f5ce7871ad40a01161e0781cda8"></a> enumerator GATT\_DB\_CHAR\_PEER\_EXECUTE\_WRITE\_REQ
    :   Characteristic Value Peer Execute Write Req

    <a id="_CPPv4NUt1_835GATT_DB_CHAR_PEER_PREPARE_WRITE_REQE"></a>

    <a id="_CPPv3NUt1_835GATT_DB_CHAR_PEER_PREPARE_WRITE_REQE"></a> <a id="group__gatt__db__operations_1ggabed82baf7f470b522273a3e37c24c600acaba221e072946ac6c171660a75afb31"></a> enumerator GATT\_DB\_CHAR\_PEER\_PREPARE\_WRITE\_REQ
    :   Characteristic Value Peer Prepare Write Req

    <a id="_CPPv4NUt1_835GATT_DB_CHAR_PEER_CLI_CNFG_READ_REQE"></a>

    <a id="_CPPv3NUt1_835GATT_DB_CHAR_PEER_CLI_CNFG_READ_REQE"></a> <a id="group__gatt__db__operations_1ggabed82baf7f470b522273a3e37c24c600afadfa2f22307d21ba16e43c5b7ffff6a"></a> enumerator GATT\_DB\_CHAR\_PEER\_CLI\_CNFG\_READ\_REQ
    :   Characteristic Client Configuration Peer Read Operation

    <a id="_CPPv4NUt1_836GATT_DB_CHAR_PEER_CLI_CNFG_WRITE_REQE"></a>

    <a id="_CPPv3NUt1_836GATT_DB_CHAR_PEER_CLI_CNFG_WRITE_REQE"></a> <a id="group__gatt__db__operations_1ggabed82baf7f470b522273a3e37c24c600acd4748e02d5dd3eb42e03c9271a0eae0"></a> enumerator GATT\_DB\_CHAR\_PEER\_CLI\_CNFG\_WRITE\_REQ
    :   Characteristic Client Configuration Peer Write Operation

    <a id="_CPPv4NUt1_835GATT_DB_CHAR_PEER_SER_CNFG_READ_REQE"></a>

    <a id="_CPPv3NUt1_835GATT_DB_CHAR_PEER_SER_CNFG_READ_REQE"></a> <a id="group__gatt__db__operations_1ggabed82baf7f470b522273a3e37c24c600abb8bee622a7e8ea7e0ede708c170c44d"></a> enumerator GATT\_DB\_CHAR\_PEER\_SER\_CNFG\_READ\_REQ
    :   Characteristic Server Configuration Peer Read Operation

    <a id="_CPPv4NUt1_836GATT_DB_CHAR_PEER_SER_CNFG_WRITE_REQE"></a>

    <a id="_CPPv3NUt1_836GATT_DB_CHAR_PEER_SER_CNFG_WRITE_REQE"></a> <a id="group__gatt__db__operations_1ggabed82baf7f470b522273a3e37c24c600a3cca3d20495a7a0397a8306a09cca5ea"></a> enumerator GATT\_DB\_CHAR\_PEER\_SER\_CNFG\_WRITE\_REQ
    :   Characteristic Server Configuration Peer Write Operation

    <a id="_CPPv4NUt1_835GATT_DB_CHAR_PEER_USR_DESC_READ_REQE"></a>

    <a id="_CPPv3NUt1_835GATT_DB_CHAR_PEER_USR_DESC_READ_REQE"></a> <a id="group__gatt__db__operations_1ggabed82baf7f470b522273a3e37c24c600ae6384aae0267e25604c514ec329d5867"></a> enumerator GATT\_DB\_CHAR\_PEER\_USR\_DESC\_READ\_REQ
    :   Characteristic User Description Peer Read Operation

    <a id="_CPPv4NUt1_836GATT_DB_CHAR_PEER_USR_DESC_WRITE_REQE"></a>

    <a id="_CPPv3NUt1_836GATT_DB_CHAR_PEER_USR_DESC_WRITE_REQE"></a> <a id="group__gatt__db__operations_1ggabed82baf7f470b522273a3e37c24c600af65a6cae8cf8f303dc5462c22dad998d"></a> enumerator GATT\_DB\_CHAR\_PEER\_USR\_DESC\_WRITE\_REQ
    :   Characteristic User Description Peer Write Operation

    <a id="_CPPv4NUt1_835GATT_DB_CHAR_PEER_HLD_DESC_READ_REQE"></a>

    <a id="_CPPv3NUt1_835GATT_DB_CHAR_PEER_HLD_DESC_READ_REQE"></a> <a id="group__gatt__db__operations_1ggabed82baf7f470b522273a3e37c24c600aa1dc669f0cd17430258e4c1d68525e95"></a> enumerator GATT\_DB\_CHAR\_PEER\_HLD\_DESC\_READ\_REQ
    :   Characteristic Higher Layer Defined Descriptor Peer Read Operation

    <a id="_CPPv4NUt1_836GATT_DB_CHAR_PEER_HLD_DESC_WRITE_REQE"></a>

    <a id="_CPPv3NUt1_836GATT_DB_CHAR_PEER_HLD_DESC_WRITE_REQE"></a> <a id="group__gatt__db__operations_1ggabed82baf7f470b522273a3e37c24c600aabf6fa1102926ea5020c052e3b54edd2"></a> enumerator GATT\_DB\_CHAR\_PEER\_HLD\_DESC\_WRITE\_REQ
    :   Characteristic Higher Layer Defined Descriptor Peer Write Operation

<a id="_CPPv4Ut1_9"></a>

<a id="_CPPv3Ut1_9"></a> <a id="group__gatt__characteristic__properties_1gab04a0655cd1e3bcac5e8f48c18df1a57"></a> enum \[anonymous\]
:   *Values:*

    <a id="_CPPv4NUt1_931GATT_DB_CHAR_BROADCAST_PROPERTYE"></a>

    <a id="_CPPv3NUt1_931GATT_DB_CHAR_BROADCAST_PROPERTYE"></a> <a id="group__gatt__characteristic__properties_1ggab04a0655cd1e3bcac5e8f48c18df1a57a48a450bc1c80a98a3720f4bcfb36b227"></a> enumerator GATT\_DB\_CHAR\_BROADCAST\_PROPERTY
    :   Characteristic support Broadcast of its value to the peer. Setting this property automatically includes Characteristic Server Configuration Descriptor to the Characteristic

    <a id="_CPPv4NUt1_926GATT_DB_CHAR_READ_PROPERTYE"></a>

    <a id="_CPPv3NUt1_926GATT_DB_CHAR_READ_PROPERTYE"></a> <a id="group__gatt__characteristic__properties_1ggab04a0655cd1e3bcac5e8f48c18df1a57a90ebdf42e3bda749182f0229c30c3495"></a> enumerator GATT\_DB\_CHAR\_READ\_PROPERTY
    :   Characteristic support Reading its value by peer

    <a id="_CPPv4NUt1_939GATT_DB_CHAR_WRITE_WITHOUT_RSP_PROPERTYE"></a>

    <a id="_CPPv3NUt1_939GATT_DB_CHAR_WRITE_WITHOUT_RSP_PROPERTYE"></a> <a id="group__gatt__characteristic__properties_1ggab04a0655cd1e3bcac5e8f48c18df1a57aa4e6e816857cec76b175b533ff568e01"></a> enumerator GATT\_DB\_CHAR\_WRITE\_WITHOUT\_RSP\_PROPERTY
    :   Characteristic support Writing its value by peer Without Response

    <a id="_CPPv4NUt1_927GATT_DB_CHAR_WRITE_PROPERTYE"></a>

    <a id="_CPPv3NUt1_927GATT_DB_CHAR_WRITE_PROPERTYE"></a> <a id="group__gatt__characteristic__properties_1ggab04a0655cd1e3bcac5e8f48c18df1a57a242aeb495d7cf71704c80e461a6702bb"></a> enumerator GATT\_DB\_CHAR\_WRITE\_PROPERTY
    :   Characteristic supports Writing its value by peer

    <a id="_CPPv4NUt1_928GATT_DB_CHAR_NOTIFY_PROPERTYE"></a>

    <a id="_CPPv3NUt1_928GATT_DB_CHAR_NOTIFY_PROPERTYE"></a> <a id="group__gatt__characteristic__properties_1ggab04a0655cd1e3bcac5e8f48c18df1a57a4c0b4fe5642fc1602ed91532da1492bb"></a> enumerator GATT\_DB\_CHAR\_NOTIFY\_PROPERTY
    :   Characteristic supports Notifying its value to the peer. Setting this property automatically includes Characteristic Server Configuration Descriptor to the Characteristic

    <a id="_CPPv4NUt1_930GATT_DB_CHAR_INDICATE_PROPERTYE"></a>

    <a id="_CPPv3NUt1_930GATT_DB_CHAR_INDICATE_PROPERTYE"></a> <a id="group__gatt__characteristic__properties_1ggab04a0655cd1e3bcac5e8f48c18df1a57a4afe6abe2b4e442c272542879880822a"></a> enumerator GATT\_DB\_CHAR\_INDICATE\_PROPERTY
    :   Characteristic supports Indicating its value to the peer

    <a id="_CPPv4NUt1_934GATT_DB_CHAR_SIGNED_WRITE_PROPERTYE"></a>

    <a id="_CPPv3NUt1_934GATT_DB_CHAR_SIGNED_WRITE_PROPERTYE"></a> <a id="group__gatt__characteristic__properties_1ggab04a0655cd1e3bcac5e8f48c18df1a57ac04f9b662cdba17c2a6f194fcd38f82c"></a> enumerator GATT\_DB\_CHAR\_SIGNED\_WRITE\_PROPERTY
    :   Characteristic supports Signed Write on its value

    <a id="_CPPv4NUt1_934GATT_DB_CHAR_WRIEABLE_AUX_PROPERTYE"></a>

    <a id="_CPPv3NUt1_934GATT_DB_CHAR_WRIEABLE_AUX_PROPERTYE"></a> <a id="group__gatt__characteristic__properties_1ggab04a0655cd1e3bcac5e8f48c18df1a57a9299f2b3eafb4e2c985f8ca2eef02b3c"></a> enumerator GATT\_DB\_CHAR\_WRIEABLE\_AUX\_PROPERTY
    :   Characteristic supports write on its User Description Descriptor

    <a id="_CPPv4NUt1_929GATT_DB_NO_AUXILLARY_PROPERTYE"></a>

    <a id="_CPPv3NUt1_929GATT_DB_NO_AUXILLARY_PROPERTYE"></a> <a id="group__gatt__characteristic__properties_1ggab04a0655cd1e3bcac5e8f48c18df1a57a786205016b07140ac8c136df992d7784"></a> enumerator GATT\_DB\_NO\_AUXILLARY\_PROPERTY
    :   No Auxillary Property

    <a id="_CPPv4NUt1_929GATT_DB_FIXED_LENGTH_PROPERTYE"></a>

    <a id="_CPPv3NUt1_929GATT_DB_FIXED_LENGTH_PROPERTYE"></a> <a id="group__gatt__characteristic__properties_1ggab04a0655cd1e3bcac5e8f48c18df1a57a8e6d57ebe0d2a2eabc0756ffceb777b6"></a> enumerator GATT\_DB\_FIXED\_LENGTH\_PROPERTY
    :   Characteristic Value is Fixed Length

    <a id="_CPPv4NUt1_930GATT_DB_AUTHORIZATION_PROPERTYE"></a>

    <a id="_CPPv3NUt1_930GATT_DB_AUTHORIZATION_PROPERTYE"></a> <a id="group__gatt__characteristic__properties_1ggab04a0655cd1e3bcac5e8f48c18df1a57a7d07489b67f8f3e5d1a829ba937b987a"></a> enumerator GATT\_DB\_AUTHORIZATION\_PROPERTY

    <a id="_CPPv4NUt1_934GATT_DB_PEER_SPECIFIC_VAL_PROPERTYE"></a>

    <a id="_CPPv3NUt1_934GATT_DB_PEER_SPECIFIC_VAL_PROPERTYE"></a> <a id="group__gatt__characteristic__properties_1ggab04a0655cd1e3bcac5e8f48c18df1a57a80805e281fbe68c25c73210098c177be"></a> enumerator GATT\_DB\_PEER\_SPECIFIC\_VAL\_PROPERTY

    <a id="_CPPv4NUt1_931GATT_DB_CONST_ATTR_VAL_PROPERTYE"></a>

    <a id="_CPPv3NUt1_931GATT_DB_CONST_ATTR_VAL_PROPERTYE"></a> <a id="group__gatt__characteristic__properties_1ggab04a0655cd1e3bcac5e8f48c18df1a57ae2168b7b5aa798edd23c4c66177ca3b7"></a> enumerator GATT\_DB\_CONST\_ATTR\_VAL\_PROPERTY

<a id="_CPPv4Ut2_10"></a>

<a id="_CPPv3Ut2_10"></a> <a id="dm__ble__types_8h_1a385c44f6fb256e5716a2302a5b940388"></a> enum \[anonymous\]
:   GATT Characteristic and Descriptor permissions.

    *Values:*

    <a id="_CPPv4NUt2_1017GATT_DB_PERM_NONEE"></a>

    <a id="_CPPv3NUt2_1017GATT_DB_PERM_NONEE"></a> <a id="dm__ble__types_8h_1a385c44f6fb256e5716a2302a5b940388a05eb7e009344dced736ea7e3c4918e55"></a> enumerator GATT\_DB\_PERM\_NONE

    <a id="_CPPv4NUt2_1017GATT_DB_PERM_READE"></a>

    <a id="_CPPv3NUt2_1017GATT_DB_PERM_READE"></a> <a id="dm__ble__types_8h_1a385c44f6fb256e5716a2302a5b940388a75353ce435b038e35ceca420e4e9dee0"></a> enumerator GATT\_DB\_PERM\_READ

    <a id="_CPPv4NUt2_1027GATT_DB_PERM_READ_ENCRYPTEDE"></a>

    <a id="_CPPv3NUt2_1027GATT_DB_PERM_READ_ENCRYPTEDE"></a> <a id="dm__ble__types_8h_1a385c44f6fb256e5716a2302a5b940388a198567c90e37e992215eee017c201cdc"></a> enumerator GATT\_DB\_PERM\_READ\_ENCRYPTED

    <a id="_CPPv4NUt2_1032GATT_DB_PERM_READ_ENCRYPTED_MITME"></a>

    <a id="_CPPv3NUt2_1032GATT_DB_PERM_READ_ENCRYPTED_MITME"></a> <a id="dm__ble__types_8h_1a385c44f6fb256e5716a2302a5b940388ae116897f58be17b5981d70d9d2af9584"></a> enumerator GATT\_DB\_PERM\_READ\_ENCRYPTED\_MITM

    <a id="_CPPv4NUt2_1018GATT_DB_PERM_WRITEE"></a>

    <a id="_CPPv3NUt2_1018GATT_DB_PERM_WRITEE"></a> <a id="dm__ble__types_8h_1a385c44f6fb256e5716a2302a5b940388a5392f1c16e499388fc20a76b448b05a5"></a> enumerator GATT\_DB\_PERM\_WRITE

    <a id="_CPPv4NUt2_1028GATT_DB_PERM_WRITE_ENCRYPTEDE"></a>

    <a id="_CPPv3NUt2_1028GATT_DB_PERM_WRITE_ENCRYPTEDE"></a> <a id="dm__ble__types_8h_1a385c44f6fb256e5716a2302a5b940388a8c250cb92924cbacce29396a73012070"></a> enumerator GATT\_DB\_PERM\_WRITE\_ENCRYPTED

    <a id="_CPPv4NUt2_1033GATT_DB_PERM_WRITE_ENCRYPTED_MIMTE"></a>

    <a id="_CPPv3NUt2_1033GATT_DB_PERM_WRITE_ENCRYPTED_MIMTE"></a> <a id="dm__ble__types_8h_1a385c44f6fb256e5716a2302a5b940388a0a9b935041052392de0e6daee581ad57"></a> enumerator GATT\_DB\_PERM\_WRITE\_ENCRYPTED\_MIMT

    <a id="_CPPv4NUt2_1025GATT_DB_PERM_WRITE_SIGNEDE"></a>

    <a id="_CPPv3NUt2_1025GATT_DB_PERM_WRITE_SIGNEDE"></a> <a id="dm__ble__types_8h_1a385c44f6fb256e5716a2302a5b940388a44d58538f2c20044a9c1e580ae30000f"></a> enumerator GATT\_DB\_PERM\_WRITE\_SIGNED

    <a id="_CPPv4NUt2_1030GATT_DB_PERM_WRITE_SIGNED_MITME"></a>

    <a id="_CPPv3NUt2_1030GATT_DB_PERM_WRITE_SIGNED_MITME"></a> <a id="dm__ble__types_8h_1a385c44f6fb256e5716a2302a5b940388a71a8079bce83ccaceb02fb644ef191db"></a> enumerator GATT\_DB\_PERM\_WRITE\_SIGNED\_MITM

<a id="_CPPv4Ut2_11"></a>

<a id="_CPPv3Ut2_11"></a> <a id="group__gatt__service__properties_1gabc5c98fcc1211af2b80116dd6e0a035d"></a> enum \[anonymous\]
:   *Values:*

    <a id="_CPPv4NUt2_1127GATT_DB_SER_SECURITY_LEVEL0E"></a>

    <a id="_CPPv3NUt2_1127GATT_DB_SER_SECURITY_LEVEL0E"></a> <a id="group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da49e0d81dff13fcb278b8a1b87be39c0b"></a> enumerator GATT\_DB\_SER\_SECURITY\_LEVEL0
    :   Security related \- combination of Level, Mode and Encryption Key Size (if applicable) describes complete security needsService employs Level 0

    <a id="_CPPv4NUt2_1127GATT_DB_SER_SECURITY_LEVEL1E"></a>

    <a id="_CPPv3NUt2_1127GATT_DB_SER_SECURITY_LEVEL1E"></a> <a id="group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da97297f1172c56e0335ada7ec9a95523f"></a> enumerator GATT\_DB\_SER\_SECURITY\_LEVEL1
    :   Service employs Level 1

    <a id="_CPPv4NUt2_1127GATT_DB_SER_SECURITY_LEVEL2E"></a>

    <a id="_CPPv3NUt2_1127GATT_DB_SER_SECURITY_LEVEL2E"></a> <a id="group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035daeee0be171bf53f0b5e9394163254b85c"></a> enumerator GATT\_DB\_SER\_SECURITY\_LEVEL2
    :   Service employs Level 2

    <a id="_CPPv4NUt2_1127GATT_DB_SER_SECURITY_LEVEL3E"></a>

    <a id="_CPPv3NUt2_1127GATT_DB_SER_SECURITY_LEVEL3E"></a> <a id="group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da43c32dae35af6c45c3e6e3a9b7b8697a"></a> enumerator GATT\_DB\_SER\_SECURITY\_LEVEL3
    :   Service employs Level 3

    <a id="_CPPv4NUt2_1126GATT_DB_SER_SECURITY_MODE1E"></a>

    <a id="_CPPv3NUt2_1126GATT_DB_SER_SECURITY_MODE1E"></a> <a id="group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da74841772cdaba7022c4c0350846e928c"></a> enumerator GATT\_DB\_SER\_SECURITY\_MODE1
    :   Service employs Mode 1

    <a id="_CPPv4NUt2_1126GATT_DB_SER_SECURITY_MODE2E"></a>

    <a id="_CPPv3NUt2_1126GATT_DB_SER_SECURITY_MODE2E"></a> <a id="group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da7459a951c37cece87b3bf40773884978"></a> enumerator GATT\_DB\_SER\_SECURITY\_MODE2
    :   Service employs Mode 2

    <a id="_CPPv4NUt2_1136GATT_DB_SER_MULTIPLE_CLIENTS_SUPPORTE"></a>

    <a id="_CPPv3NUt2_1136GATT_DB_SER_MULTIPLE_CLIENTS_SUPPORTE"></a> <a id="group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da2eceaf0561c10556913d30bf1997e1e4"></a> enumerator GATT\_DB\_SER\_MULTIPLE\_CLIENTS\_SUPPORT
    :   ignore\_this Unused right now

    <a id="_CPPv4NUt2_1138GATT_DB_SER_SECONDARY_SERVICE_PROPERTYE"></a>

    <a id="_CPPv3NUt2_1138GATT_DB_SER_SECONDARY_SERVICE_PROPERTYE"></a> <a id="group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da5494a021c096fbbefe964e063515647f"></a> enumerator GATT\_DB\_SER\_SECONDARY\_SERVICE\_PROPERTY
    :   Service is a Secondary Service. If this not used, Service is by default considered to be Primary

    <a id="_CPPv4NUt2_1131GATT_DB_SER_128_BIT_UUID_FORMATE"></a>

    <a id="_CPPv3NUt2_1131GATT_DB_SER_128_BIT_UUID_FORMATE"></a> <a id="group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035dac8f073d85206e84ae8c4528f9515183e"></a> enumerator GATT\_DB\_SER\_128\_BIT\_UUID\_FORMAT
    :   Service UUID is 128-bit

    <a id="_CPPv4NUt2_1132GATT_DB_SER_NO_SECURITY_PROPERTYE"></a>

    <a id="_CPPv3NUt2_1132GATT_DB_SER_NO_SECURITY_PROPERTYE"></a> <a id="group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035dab307287b35dec27c88ec7030aca6fb84"></a> enumerator GATT\_DB\_SER\_NO\_SECURITY\_PROPERTY
    :   Set this property to relax all Security on the Service

    <a id="_CPPv4NUt2_1134GATT_DB_SER_ENC_KEY_SIZE_DONT_CAREE"></a>

    <a id="_CPPv3NUt2_1134GATT_DB_SER_ENC_KEY_SIZE_DONT_CAREE"></a> <a id="group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da9d8f85a9e69bab3d04f0c9c035bc20df"></a> enumerator GATT\_DB\_SER\_ENC\_KEY\_SIZE\_DONT\_CARE
    :   This is employed to describe Service is not rigid on any Encryption Key Size. Any Size used by other Services or on the whole by the device will do

    <a id="_CPPv4NUt2_1130GATT_DB_SER_ENCRYPT_KEY_SIZE_7E"></a>

    <a id="_CPPv3NUt2_1130GATT_DB_SER_ENCRYPT_KEY_SIZE_7E"></a> <a id="group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035daf26237278d04eb8e0f0b6d458e4101a8"></a> enumerator GATT\_DB\_SER\_ENCRYPT\_KEY\_SIZE\_7
    :   Encyrption Key Size 7 Needed for the Service

    <a id="_CPPv4NUt2_1130GATT_DB_SER_ENCRYPT_KEY_SIZE_8E"></a>

    <a id="_CPPv3NUt2_1130GATT_DB_SER_ENCRYPT_KEY_SIZE_8E"></a> <a id="group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da578f242314247aabe4766585b213935d"></a> enumerator GATT\_DB\_SER\_ENCRYPT\_KEY\_SIZE\_8
    :   Encyrption Key Size 8 Needed for the Service

    <a id="_CPPv4NUt2_1130GATT_DB_SER_ENCRYPT_KEY_SIZE_9E"></a>

    <a id="_CPPv3NUt2_1130GATT_DB_SER_ENCRYPT_KEY_SIZE_9E"></a> <a id="group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da0b721e086f412de7f0b881434193421f"></a> enumerator GATT\_DB\_SER\_ENCRYPT\_KEY\_SIZE\_9
    :   Encyrption Key Size 9 Needed for the Service

    <a id="_CPPv4NUt2_1131GATT_DB_SER_ENCRYPT_KEY_SIZE_10E"></a>

    <a id="_CPPv3NUt2_1131GATT_DB_SER_ENCRYPT_KEY_SIZE_10E"></a> <a id="group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da0af0e5686c4872b497be8568ec7c8ad7"></a> enumerator GATT\_DB\_SER\_ENCRYPT\_KEY\_SIZE\_10
    :   Encyrption Key Size 10 Needed for the Service

    <a id="_CPPv4NUt2_1131GATT_DB_SER_ENCRYPT_KEY_SIZE_11E"></a>

    <a id="_CPPv3NUt2_1131GATT_DB_SER_ENCRYPT_KEY_SIZE_11E"></a> <a id="group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da22ae7f4b2be7c145dd54d8f58720041f"></a> enumerator GATT\_DB\_SER\_ENCRYPT\_KEY\_SIZE\_11
    :   Encyrption Key Size 11 Needed for the Service

    <a id="_CPPv4NUt2_1131GATT_DB_SER_ENCRYPT_KEY_SIZE_12E"></a>

    <a id="_CPPv3NUt2_1131GATT_DB_SER_ENCRYPT_KEY_SIZE_12E"></a> <a id="group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da62c6ca9b86cda66475dc31c721f31ee5"></a> enumerator GATT\_DB\_SER\_ENCRYPT\_KEY\_SIZE\_12
    :   Encryption Key Size 12 Needed for the Service

    <a id="_CPPv4NUt2_1131GATT_DB_SER_ENCRYPT_KEY_SIZE_13E"></a>

    <a id="_CPPv3NUt2_1131GATT_DB_SER_ENCRYPT_KEY_SIZE_13E"></a> <a id="group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035dada15fde570ee125f1e273c0e15416ac0"></a> enumerator GATT\_DB\_SER\_ENCRYPT\_KEY\_SIZE\_13
    :   Encryption Key Size 13 Needed for the Service

    <a id="_CPPv4NUt2_1131GATT_DB_SER_ENCRYPT_KEY_SIZE_14E"></a>

    <a id="_CPPv3NUt2_1131GATT_DB_SER_ENCRYPT_KEY_SIZE_14E"></a> <a id="group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035daae41a9c45197bf1897c25206b7833552"></a> enumerator GATT\_DB\_SER\_ENCRYPT\_KEY\_SIZE\_14
    :   Encryption Key Size 14 Needed for the Service

    <a id="_CPPv4NUt2_1131GATT_DB_SER_ENCRYPT_KEY_SIZE_15E"></a>

    <a id="_CPPv3NUt2_1131GATT_DB_SER_ENCRYPT_KEY_SIZE_15E"></a> <a id="group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da0f7f2aac54861fbefd0054f3ac911fa2"></a> enumerator GATT\_DB\_SER\_ENCRYPT\_KEY\_SIZE\_15
    :   Encryption Key Size 15 Needed for the Service

    <a id="_CPPv4NUt2_1131GATT_DB_SER_ENCRYPT_KEY_SIZE_16E"></a>

    <a id="_CPPv3NUt2_1131GATT_DB_SER_ENCRYPT_KEY_SIZE_16E"></a> <a id="group__gatt__service__properties_1ggabc5c98fcc1211af2b80116dd6e0a035da15388d866bc04cfba206ce44726d6e0e"></a> enumerator GATT\_DB\_SER\_ENCRYPT\_KEY\_SIZE\_16
    :   Encryption Key Size 16 Needed for the Service

<a id="_CPPv416ble_event_enum_t"></a>

<a id="_CPPv316ble_event_enum_t"></a> <a id="_CPPv216ble_event_enum_t"></a> <a id="dm__ble__types_8h_1aaf292ba960e9cf141b43e748481c38e9"></a> enum ble\_event\_enum\_t
:   *Values:*

    <a id="_CPPv4N16ble_event_enum_t24BK_DM_BLE_EVENT_STACK_OKE"></a>

    <a id="_CPPv3N16ble_event_enum_t24BK_DM_BLE_EVENT_STACK_OKE"></a> <a id="_CPPv2N16ble_event_enum_t24BK_DM_BLE_EVENT_STACK_OKE"></a> <a id="dm__ble__types_8h_1aaf292ba960e9cf141b43e748481c38e9ac2ffb703bae27522995628a68d7a9880"></a> enumerator BK\_DM\_BLE\_EVENT\_STACK\_OK
    :   ble stack init ok, param null

    <a id="_CPPv4N16ble_event_enum_t26BK_DM_BLE_EVENT_REPORT_ADVE"></a>

    <a id="_CPPv3N16ble_event_enum_t26BK_DM_BLE_EVENT_REPORT_ADVE"></a> <a id="_CPPv2N16ble_event_enum_t26BK_DM_BLE_EVENT_REPORT_ADVE"></a> <a id="dm__ble__types_8h_1aaf292ba960e9cf141b43e748481c38e9ac056b3cdbdc78cbdcfac5762e3b4ebe2"></a> enumerator BK\_DM\_BLE\_EVENT\_REPORT\_ADV
    :   scan peer adv report, param ble\_adv\_report\_t

    <a id="_CPPv4N16ble_event_enum_t26BK_DM_BLE_EVENT_MTU_CHANGEE"></a>

    <a id="_CPPv3N16ble_event_enum_t26BK_DM_BLE_EVENT_MTU_CHANGEE"></a> <a id="_CPPv2N16ble_event_enum_t26BK_DM_BLE_EVENT_MTU_CHANGEE"></a> <a id="dm__ble__types_8h_1aaf292ba960e9cf141b43e748481c38e9a8182fadd1a8aee241bde174b64eb46b1"></a> enumerator BK\_DM\_BLE\_EVENT\_MTU\_CHANGE
    :   mtu change event, param [ble\_mtu\_change\_t](ble.md#structble__mtu__change__t)

    <a id="_CPPv4N16ble_event_enum_t23BK_DM_BLE_EVENT_CONNECTE"></a>

    <a id="_CPPv3N16ble_event_enum_t23BK_DM_BLE_EVENT_CONNECTE"></a> <a id="_CPPv2N16ble_event_enum_t23BK_DM_BLE_EVENT_CONNECTE"></a> <a id="dm__ble__types_8h_1aaf292ba960e9cf141b43e748481c38e9a398c0ba31627b50927eff0227b44df3b"></a> enumerator BK\_DM\_BLE\_EVENT\_CONNECT
    :   recv connnect event, param [ble\_conn\_att\_t](#structble__conn__att__t)

    <a id="_CPPv4N16ble_event_enum_t26BK_DM_BLE_EVENT_DISCONNECTE"></a>

    <a id="_CPPv3N16ble_event_enum_t26BK_DM_BLE_EVENT_DISCONNECTE"></a> <a id="_CPPv2N16ble_event_enum_t26BK_DM_BLE_EVENT_DISCONNECTE"></a> <a id="dm__ble__types_8h_1aaf292ba960e9cf141b43e748481c38e9a7827bbd34505241f49fee9beec2be973"></a> enumerator BK\_DM\_BLE\_EVENT\_DISCONNECT
    :   recv disconnect event, param [ble\_conn\_att\_t](#structble__conn__att__t)

    <a id="_CPPv4N16ble_event_enum_t25BK_DM_BLE_EVENT_CREATE_DBE"></a>

    <a id="_CPPv3N16ble_event_enum_t25BK_DM_BLE_EVENT_CREATE_DBE"></a> <a id="_CPPv2N16ble_event_enum_t25BK_DM_BLE_EVENT_CREATE_DBE"></a> <a id="dm__ble__types_8h_1aaf292ba960e9cf141b43e748481c38e9a35b305a5230fa3a0dd7870d257321d20"></a> enumerator BK\_DM\_BLE\_EVENT\_CREATE\_DB
    :   create db event, param [ble\_create\_db\_t](ble.md#structble__create__db__t), param null

    <a id="_CPPv4N16ble_event_enum_t23BK_DM_BLE_EVENT_TX_DONEE"></a>

    <a id="_CPPv3N16ble_event_enum_t23BK_DM_BLE_EVENT_TX_DONEE"></a> <a id="_CPPv2N16ble_event_enum_t23BK_DM_BLE_EVENT_TX_DONEE"></a> <a id="dm__ble__types_8h_1aaf292ba960e9cf141b43e748481c38e9ae14eaf08462f470f5c45e1031d24486b"></a> enumerator BK\_DM\_BLE\_EVENT\_TX\_DONE
    :   tx complete event, param [ble\_att\_tx\_compl\_t](#structble__att__tx__compl__t)

    <a id="_CPPv4N16ble_event_enum_t24BK_DM_BLE_EVENT_READ_PHYE"></a>

    <a id="_CPPv3N16ble_event_enum_t24BK_DM_BLE_EVENT_READ_PHYE"></a> <a id="_CPPv2N16ble_event_enum_t24BK_DM_BLE_EVENT_READ_PHYE"></a> <a id="dm__ble__types_8h_1aaf292ba960e9cf141b43e748481c38e9a7c600ba2963043dce4b1dcd421345f14"></a> enumerator BK\_DM\_BLE\_EVENT\_READ\_PHY
    :   get current conn phy result, param [ble\_read\_phy\_t](ble.md#structble__read__phy__t)

    <a id="_CPPv4N16ble_event_enum_t27BK_DM_BLE_EVENT_CONN_UPDATAE"></a>

    <a id="_CPPv3N16ble_event_enum_t27BK_DM_BLE_EVENT_CONN_UPDATAE"></a> <a id="_CPPv2N16ble_event_enum_t27BK_DM_BLE_EVENT_CONN_UPDATAE"></a> <a id="dm__ble__types_8h_1aaf292ba960e9cf141b43e748481c38e9afc0193983fbdc04d6b5ecaca86290609"></a> enumerator BK\_DM\_BLE\_EVENT\_CONN\_UPDATA
    :   recv ble conn update event result, param [ble\_conn\_update\_param\_compl\_ind\_t](#structble__conn__update__param__compl__ind__t)

    <a id="_CPPv4N16ble_event_enum_t41BK_DM_BLE_EVENT_DISCOVERY_PRIMARY_SERVICEE"></a>

    <a id="_CPPv3N16ble_event_enum_t41BK_DM_BLE_EVENT_DISCOVERY_PRIMARY_SERVICEE"></a> <a id="_CPPv2N16ble_event_enum_t41BK_DM_BLE_EVENT_DISCOVERY_PRIMARY_SERVICEE"></a> <a id="dm__ble__types_8h_1aaf292ba960e9cf141b43e748481c38e9a11e34ae51d1f07c58ac22105cd2e867b"></a> enumerator BK\_DM\_BLE\_EVENT\_DISCOVERY\_PRIMARY\_SERVICE
    :   discover peer primary service result, param ble\_discovery\_primary\_service\_t

    <a id="_CPPv4N16ble_event_enum_t30BK_DM_BLE_EVENT_DISCOVERY_CHARE"></a>

    <a id="_CPPv3N16ble_event_enum_t30BK_DM_BLE_EVENT_DISCOVERY_CHARE"></a> <a id="_CPPv2N16ble_event_enum_t30BK_DM_BLE_EVENT_DISCOVERY_CHARE"></a> <a id="dm__ble__types_8h_1aaf292ba960e9cf141b43e748481c38e9a3ffcf9da7c93f625aa0420f471a579d1"></a> enumerator BK\_DM\_BLE\_EVENT\_DISCOVERY\_CHAR
    :   discover peer characteristic result, param ble\_discovery\_char\_t

    <a id="_CPPv4N16ble_event_enum_t27BK_DM_BLE_EVENT_RECV_NOTIFYE"></a>

    <a id="_CPPv3N16ble_event_enum_t27BK_DM_BLE_EVENT_RECV_NOTIFYE"></a> <a id="_CPPv2N16ble_event_enum_t27BK_DM_BLE_EVENT_RECV_NOTIFYE"></a> <a id="dm__ble__types_8h_1aaf292ba960e9cf141b43e748481c38e9ac4d5d5576b5674459bbbfd1e2a7e60bb"></a> enumerator BK\_DM\_BLE\_EVENT\_RECV\_NOTIFY
    :   recv gatt client notify, param [ble\_att\_notify\_t](#structble__att__notify__t)

    <a id="_CPPv4N16ble_event_enum_t33BK_DM_BLE_EVENT_ATT_READ_RESPONSEE"></a>

    <a id="_CPPv3N16ble_event_enum_t33BK_DM_BLE_EVENT_ATT_READ_RESPONSEE"></a> <a id="_CPPv2N16ble_event_enum_t33BK_DM_BLE_EVENT_ATT_READ_RESPONSEE"></a> <a id="dm__ble__types_8h_1aaf292ba960e9cf141b43e748481c38e9a4d008ecd5c3cfc972629ced1d1595086"></a> enumerator BK\_DM\_BLE\_EVENT\_ATT\_READ\_RESPONSE
    :   recv gatt read response, param [ble\_att\_rw\_t](#structble__att__rw__t)

    <a id="_CPPv4N16ble_event_enum_t32BK_DM_BLE_EVENT_CONN_UPD_PAR_ASKE"></a>

    <a id="_CPPv3N16ble_event_enum_t32BK_DM_BLE_EVENT_CONN_UPD_PAR_ASKE"></a> <a id="_CPPv2N16ble_event_enum_t32BK_DM_BLE_EVENT_CONN_UPD_PAR_ASKE"></a> <a id="dm__ble__types_8h_1aaf292ba960e9cf141b43e748481c38e9a39274def1a8a0d154baeb18b7e8b9fd8"></a> enumerator BK\_DM\_BLE\_EVENT\_CONN\_UPD\_PAR\_ASK
    :   recv ble connection param update req, param [ble\_conn\_update\_param\_ind\_t](#structble__conn__update__param__ind__t)

    <a id="_CPPv4N16ble_event_enum_t31BK_DM_BLE_EVENT_DEINIT_STACK_OKE"></a>

    <a id="_CPPv3N16ble_event_enum_t31BK_DM_BLE_EVENT_DEINIT_STACK_OKE"></a> <a id="_CPPv2N16ble_event_enum_t31BK_DM_BLE_EVENT_DEINIT_STACK_OKE"></a> <a id="dm__ble__types_8h_1aaf292ba960e9cf141b43e748481c38e9a6bd869cf800811b5f380279edcdf1354"></a> enumerator BK\_DM\_BLE\_EVENT\_DEINIT\_STACK\_OK
    :   ble stack deinit ok, param null

<a id="_CPPv423advertise_filter_policy"></a>

<a id="_CPPv323advertise_filter_policy"></a> <a id="_CPPv223advertise_filter_policy"></a> <a id="dm__ble__types_8h_1a490541eb3c275397966c565e416d00b2"></a> enum advertise\_filter\_policy
:   use in [bk\_ble\_set\_advertising\_params](#group__bk__dm__ble__api__v1_1gac82851a90130a907f6a3f58863aae7d5)

    *Values:*

    <a id="_CPPv4N23advertise_filter_policy44ADV_FILTER_POLICY_ALLOW_SCAN_ANY_CONNECT_ANYE"></a>

    <a id="_CPPv3N23advertise_filter_policy44ADV_FILTER_POLICY_ALLOW_SCAN_ANY_CONNECT_ANYE"></a> <a id="_CPPv2N23advertise_filter_policy44ADV_FILTER_POLICY_ALLOW_SCAN_ANY_CONNECT_ANYE"></a> <a id="dm__ble__types_8h_1a490541eb3c275397966c565e416d00b2a924421068a4d12dfd3ce645a7328de37"></a> enumerator ADV\_FILTER\_POLICY\_ALLOW\_SCAN\_ANY\_CONNECT\_ANY
    :   both scan and connect

    <a id="_CPPv4N23advertise_filter_policy45ADV_FILTER_POLICY_ALLOW_SCAN_WLST_CONNECT_ANYE"></a>

    <a id="_CPPv3N23advertise_filter_policy45ADV_FILTER_POLICY_ALLOW_SCAN_WLST_CONNECT_ANYE"></a> <a id="_CPPv2N23advertise_filter_policy45ADV_FILTER_POLICY_ALLOW_SCAN_WLST_CONNECT_ANYE"></a> <a id="dm__ble__types_8h_1a490541eb3c275397966c565e416d00b2a5102b1cbf2f2114cfd2332c81bcd56df"></a> enumerator ADV\_FILTER\_POLICY\_ALLOW\_SCAN\_WLST\_CONNECT\_ANY
    :   scan only in white list, connect any

    <a id="_CPPv4N23advertise_filter_policy45ADV_FILTER_POLICY_ALLOW_SCAN_ANY_CONNECT_WLITE"></a>

    <a id="_CPPv3N23advertise_filter_policy45ADV_FILTER_POLICY_ALLOW_SCAN_ANY_CONNECT_WLITE"></a> <a id="_CPPv2N23advertise_filter_policy45ADV_FILTER_POLICY_ALLOW_SCAN_ANY_CONNECT_WLITE"></a> <a id="dm__ble__types_8h_1a490541eb3c275397966c565e416d00b2a9fafd30652ad3dfb37fa2db3ae8d1913"></a> enumerator ADV\_FILTER\_POLICY\_ALLOW\_SCAN\_ANY\_CONNECT\_WLIT
    :   scan any, connect only in white list

    <a id="_CPPv4N23advertise_filter_policy46ADV_FILTER_POLICY_ALLOW_SCAN_WLIT_CONNECT_WLITE"></a>

    <a id="_CPPv3N23advertise_filter_policy46ADV_FILTER_POLICY_ALLOW_SCAN_WLIT_CONNECT_WLITE"></a> <a id="_CPPv2N23advertise_filter_policy46ADV_FILTER_POLICY_ALLOW_SCAN_WLIT_CONNECT_WLITE"></a> <a id="dm__ble__types_8h_1a490541eb3c275397966c565e416d00b2ae7f81e19c59e80f2628cd014c604a622"></a> enumerator ADV\_FILTER\_POLICY\_ALLOW\_SCAN\_WLIT\_CONNECT\_WLIT
    :   both scan connect only in white list

<a id="_CPPv421advertise_legacy_type"></a>

<a id="_CPPv321advertise_legacy_type"></a> <a id="_CPPv221advertise_legacy_type"></a> <a id="dm__ble__types_8h_1aa6075df15275412d307ea26ea8e966f0"></a> enum advertise\_legacy\_type
:   use in [bk\_ble\_set\_advertising\_params](#group__bk__dm__ble__api__v1_1gac82851a90130a907f6a3f58863aae7d5)

    *Values:*

    <a id="_CPPv4N21advertise_legacy_type23ADV_LEGACY_TYPE_ADV_INDE"></a>

    <a id="_CPPv3N21advertise_legacy_type23ADV_LEGACY_TYPE_ADV_INDE"></a> <a id="_CPPv2N21advertise_legacy_type23ADV_LEGACY_TYPE_ADV_INDE"></a> <a id="dm__ble__types_8h_1aa6075df15275412d307ea26ea8e966f0ae7e7d126c03c0514d5e2ca7ad7551795"></a> enumerator ADV\_LEGACY\_TYPE\_ADV\_IND
    :   adv that can be scan and connect

    <a id="_CPPv4N21advertise_legacy_type35ADV_LEGACY_TYPE_ADV_DIRECT_IND_HIGHE"></a>

    <a id="_CPPv3N21advertise_legacy_type35ADV_LEGACY_TYPE_ADV_DIRECT_IND_HIGHE"></a> <a id="_CPPv2N21advertise_legacy_type35ADV_LEGACY_TYPE_ADV_DIRECT_IND_HIGHE"></a> <a id="dm__ble__types_8h_1aa6075df15275412d307ea26ea8e966f0a3579fd83f7d6e01cc96bd28b4d7e9372"></a> enumerator ADV\_LEGACY\_TYPE\_ADV\_DIRECT\_IND\_HIGH
    :   adv that can be connect by special device(white list). This send adv more frequently.

    <a id="_CPPv4N21advertise_legacy_type28ADV_LEGACY_TYPE_ADV_SCAN_INDE"></a>

    <a id="_CPPv3N21advertise_legacy_type28ADV_LEGACY_TYPE_ADV_SCAN_INDE"></a> <a id="_CPPv2N21advertise_legacy_type28ADV_LEGACY_TYPE_ADV_SCAN_INDE"></a> <a id="dm__ble__types_8h_1aa6075df15275412d307ea26ea8e966f0a5d3f25f32a8eede79c99fbcff4176020"></a> enumerator ADV\_LEGACY\_TYPE\_ADV\_SCAN\_IND
    :   adv that can be scan

    <a id="_CPPv4N21advertise_legacy_type27ADV_LEGACY_TYPE_ADV_NON_INDE"></a>

    <a id="_CPPv3N21advertise_legacy_type27ADV_LEGACY_TYPE_ADV_NON_INDE"></a> <a id="_CPPv2N21advertise_legacy_type27ADV_LEGACY_TYPE_ADV_NON_INDE"></a> <a id="dm__ble__types_8h_1aa6075df15275412d307ea26ea8e966f0aafcc857e8d768f72654c93e652de986d"></a> enumerator ADV\_LEGACY\_TYPE\_ADV\_NON\_IND
    :   adv that can’t be scan and connect

    <a id="_CPPv4N21advertise_legacy_type34ADV_LEGACY_TYPE_ADV_DIRECT_IND_LOWE"></a>

    <a id="_CPPv3N21advertise_legacy_type34ADV_LEGACY_TYPE_ADV_DIRECT_IND_LOWE"></a> <a id="_CPPv2N21advertise_legacy_type34ADV_LEGACY_TYPE_ADV_DIRECT_IND_LOWE"></a> <a id="dm__ble__types_8h_1aa6075df15275412d307ea26ea8e966f0a33363256428a755f40efaad299e5ee0c"></a> enumerator ADV\_LEGACY\_TYPE\_ADV\_DIRECT\_IND\_LOW
    :   adv that can be connect by special device(white list). This send adv more few.
