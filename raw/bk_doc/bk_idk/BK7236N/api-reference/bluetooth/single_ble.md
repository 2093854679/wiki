# Single BLE APIs[](#single-ble-apis "永久链接至标题")


重要

The Single BLE API v1.0 is the lastest stable Single BLE APIs. All new applications should use Single BLE API v1.0.


## Single BLE API Categories[](#single-ble-api-categories "永久链接至标题")

Most of Single BLE APIs can be categoried as:

Interface specific Single BLE APIs:
:   - BLE common interface

    - BLE scan interface

    - BLE ADV interface

    - BLE connect interface


## Compatibility and Extension[](#compatibility-and-extension "永久链接至标题")

The Single BLE APIs are flexible, easy to be extended and backward compatible. For most of the Single BLE configurations, we put some reserved fields in the config struct for future extendence. The API users need to make sure the reserved fields are initialized to 0, otherwise the compatibility may be broken as more fields are added.


## Programing Principle[](#programing-principle "永久链接至标题")

重要

Here is some general principle for Single BLE API users:
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
    #define DECL_PRIMARY_SERVICE_128     {0x00,0x28,0,0,0,0,0,0,0,0,0,0,0,0,0,0}
    #define DECL_CHARACTERISTIC_128      {0x03,0x28,0,0,0,0,0,0,0,0,0,0,0,0,0,0}
    #define DESC_CLIENT_CHAR_CFG_128     {0x02,0x29,0,0,0,0,0,0,0,0,0,0,0,0,0,0}

    //database index:
    enum {
            TEST_IDX_SVC,
            TEST_IDX_CHAR_DECL,
            TEST_IDX_CHAR_VALUE,
            TEST_IDX_CHAR_DESC,

            TEST_IDX_NB,
    };
    //database build by some att records.
    ble_attm_desc_t test_service_db[TEST_IDX_NB] = {
       //  Service Declaration
       [TEST_IDX_SVC]              = {DECL_PRIMARY_SERVICE_128, BK_BLE_PERM_SET(RD, ENABLE), 0, 0},
       // Characteristic declare
       [TEST_IDX_CHAR_DECL]    = {DECL_CHARACTERISTIC_128,  BK_BLE_PERM_SET(RD, ENABLE), 0, 0},
       // Characteristic Value
       [TEST_IDX_CHAR_VALUE]   = {{0x34, 0x12, 0},     BK_BLE_PERM_SET(NTF, ENABLE), BK_BLE_PERM_SET(RI, ENABLE) | BK_BLE_PERM_SET(UUID_LEN, UUID_16), 128},
       //Client Characteristic Configuration Descriptor
       [TEST_IDX_CHAR_DESC] = {DESC_CLIENT_CHAR_CFG_128, BK_BLE_PERM_SET(RD, ENABLE) | BK_BLE_PERM_SET(WRITE_REQ, ENABLE), 0, 0},
    };

    struct bk_ble_db_cfg ble_db_cfg;
    const uint16_t service_uuid = 0xffff;

    ble_db_cfg.att_db = (ble_attm_desc_t *)test_service_db;
    ble_db_cfg.att_db_nb = TEST_IDX_NB;
    ble_db_cfg.prf_task_id = g_test_prf_task_id;
    ble_db_cfg.start_hdl = 0;
    ble_db_cfg.svc_perm = BK_BLE_PERM_SET(SVC_UUID_LEN, UUID_16);
os_memcpy(&(ble_db_cfg.uuid[0]), &service_uuid, 2);

    bk_ble_set_notice_cb(ble_at_notice_cb);
    bk_ble_create_db(&ble_db_cfg);

    void ble_at_notice_cb(ble_notice_t notice, void *param)
    {
            switch (notice) {

            case BLE_5_WRITE_EVENT: {

                    if (w_req->prf_id == g_test_prf_task_id)
                    {
                            switch(w_req->att_idx)
                            {
                            case TEST_IDX_CHAR_DECL:
                                    break;
                            case TEST_IDX_CHAR_VALUE:
                                    break;
                            case TEST_IDX_CHAR_DESC:
                                    //when peer enable notification, we create time and notify peer, such as
                                    //write_buffer = (uint8_t *)os_malloc(s_test_data_len);
                                    //bk_ble_send_noti_value(s_test_data_len, write_buffer, g_test_prf_task_id, TEST_IDX_CHAR_VALUE);
                                    break;

                            default:
                                    break;
                            }
                    }
                    break;
            }
            case BLE_5_CREATE_DB:
            //bk_ble_create_db success here
            break;
            }
    }

```


- start adv


```
ble_adv_param_t adv_param;

adv_param.own_addr_type = 0;//BLE_STATIC_ADDR
adv_param.adv_type = 0; //ADV_IND
adv_param.chnl_map = 7;
adv_param.adv_prop = 3;
adv_param.adv_intv_min = 0x120; //min
adv_param.adv_intv_max = 0x160; //max
adv_param.prim_phy = 1;// 1M
adv_param.second_phy = 1;// 1M
actv_idx = bk_ble_get_idle_actv_idx_handle();
if (actv_idx != UNKNOW_ACT_IDX) {
        bk_ble_create_advertising(actv_idx, &adv_param, ble_at_cmd_cb);
}

//wait for ble_at_cmd_cb

const uint8_t adv_data[] = {0x02, 0x01, 0x06, 0x0A, 0x09, 0x37 0x32, 0x33, 0x31, 0x4e, 0x5f, 0x42, 0x4c, 0x45};
bk_ble_set_adv_data(actv_idx, adv_data, sizeof(adv_data), ble_at_cmd_cb);

//wait for ble_at_cmd_cb

const uint8_t scan_data[] = {0x02, 0x01, 0x06, 0x0A, 0x09, 0x37 0x32, 0x33, 0x31, 0x4e, 0x5f, 0x42, 0x4c, 0x45};
bk_ble_set_scan_rsp_data(actv_idx, scan_data, sizeof(scan_data), ble_at_cmd_cb);

//wait for ble_at_cmd_cb

bk_ble_start_advertising(actv_idx, 0, ble_at_cmd_cb);

```


- start scan


```
ble_scan_param_t scan_param;

scan_param.own_addr_type = 0;//BLE_STATIC_ADDR
scan_param.scan_phy = 5;
scan_param.scan_intv = 0x64; //interval
scan_param.scan_wd = 0x1e; //windows
actv_idx = bk_ble_get_idle_actv_idx_handle();
bk_ble_create_scaning(actv_idx, &scan_param, ble_at_cmd);

//wait for ble_at_cmd_cb
bk_ble_start_scaning(actv_idx, ble_at_cmd);

```


- start a connect


```
ble_conn_param_t conn_param;
conn_param.intv_min = 0x40; //interval
conn_param.intv_max = 0x40; //interval
conn_param.con_latency = 0;
conn_param.sup_to = 0x200;//supervision timeout
conn_param.init_phys = 1;// 1M
con_idx = bk_ble_get_idle_conn_idx_handle();
bk_ble_create_init(con_idx, &conn_param, ble_at_cmd);
//wait for ble_at_cmd_cb
bk_ble_init_set_connect_dev_addr(con_idx, bt_mac, 1);
bk_ble_init_start_conn(con_idx, ble_at_cmd)

```


## API Reference[](#api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [bluetooth/bk_ble.h](https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_ble.h "https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_ble.h")


### Functions[](#functions "永久链接至标题")

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_create_db(struct [bk_ble_db_cfg](#_CPPv413bk_ble_db_cfg "bk_ble_db_cfg") *ble_db_cfg)[](#_CPPv416bk_ble_create_dbP13bk_ble_db_cfg "永久链接至目标")
:   Register a gatt service.

    User example: First we must build test_service_db test_service_db is a database for att, which used in ble discovery. reading writing and other operation is used on a att database.

    ```
    enum {
        TEST_IDX_SVC,
        TEST_IDX_CHAR_DECL,
        TEST_IDX_CHAR_VALUE,
        TEST_IDX_CHAR_DESC,

        TEST_IDX_CHAR_DATALEN_DECL,
        TEST_IDX_CHAR_DATALEN_VALUE,

        TEST_IDX_CHAR_INTER_DECL,
        TEST_IDX_CHAR_INTER_VALUE,

        TEST_IDX_NB,
    };

    //att records database.

    ble_attm_desc_t test_service_db[TEST_IDX_NB] = {
       //  Service Declaration
       [TEST_IDX_SVC]              = {DECL_PRIMARY_SERVICE_128, BK_BLE_PERM_SET(RD, ENABLE), 0, 0},
       // Characteristic declare
       [TEST_IDX_CHAR_DECL]    = {DECL_CHARACTERISTIC_128,  BK_BLE_PERM_SET(RD, ENABLE), 0, 0},
       // Characteristic Value
       [TEST_IDX_CHAR_VALUE]   = {{0x34, 0x12, 0},     BK_BLE_PERM_SET(NTF, ENABLE), BK_BLE_PERM_SET(RI, ENABLE) | BK_BLE_PERM_SET(UUID_LEN, UUID_16), 128},
       //Client Characteristic Configuration Descriptor
       [TEST_IDX_CHAR_DESC] = {DESC_CLIENT_CHAR_CFG_128, BK_BLE_PERM_SET(RD, ENABLE) | BK_BLE_PERM_SET(WRITE_REQ, ENABLE), 0, 0},
    };
    ```

    TEST_IDX_SVC is nessecery, is declare a primary att service. The macro define is:

    ```
    #define DECL_PRIMARY_SERVICE_128     {0x00,0x28,0}
    ```

    which is an UUID say it is a “primary service” [BK_BLE_PERM_SET(RD, ENABLE)](#group__bk__ble__api__v1_1ga12a5ba4c80b8f6fdc20573c242bd0b5b "#group__bk__ble__api__v1_1ga12a5ba4c80b8f6fdc20573c242bd0b5b") means it can be read, and must be read, so it can be discove by peer master.

    TEST_IDX_CHAR_DECL declare a characteristic as a element in service, it must be [BK_BLE_PERM_SET(RD, ENABLE)](#group__bk__ble__api__v1_1ga12a5ba4c80b8f6fdc20573c242bd0b5b "#group__bk__ble__api__v1_1ga12a5ba4c80b8f6fdc20573c242bd0b5b")

    ```
    #define DECL_CHARACTERISTIC_128      {0x03,0x28,0}
    ```

    show it’s a “characteristic”

    [BK_BLE_PERM_SET(RD, ENABLE)](#group__bk__ble__api__v1_1ga12a5ba4c80b8f6fdc20573c242bd0b5b "#group__bk__ble__api__v1_1ga12a5ba4c80b8f6fdc20573c242bd0b5b") means it can be read, and must be read, so it can be discove by peer master.

    TEST_IDX_CHAR_VALUE is the real value of TEST_IDX_CHAR_DECL, {0x34, 0x12, 0} means it’s type is 0x1234, you can determine by you self [BK_BLE_PERM_SET(NTF, ENABLE)](#group__bk__ble__api__v1_1ga12a5ba4c80b8f6fdc20573c242bd0b5b "#group__bk__ble__api__v1_1ga12a5ba4c80b8f6fdc20573c242bd0b5b") means it cant notify peer, such as value change. For exzample, BLE mouse report pos by “notify” peer. [BK_BLE_PERM_SET(RI, ENABLE)](#group__bk__ble__api__v1_1ga12a5ba4c80b8f6fdc20573c242bd0b5b "#group__bk__ble__api__v1_1ga12a5ba4c80b8f6fdc20573c242bd0b5b") means if peer read this att record, it will enable notification. [BK_BLE_PERM_SET(UUID_LEN, UUID_16)](#group__bk__ble__api__v1_1ga12a5ba4c80b8f6fdc20573c242bd0b5b "#group__bk__ble__api__v1_1ga12a5ba4c80b8f6fdc20573c242bd0b5b") means the first elem’s max len of TEST_IDX_CHAR_VALUE.

    TEST_IDX_CHAR_DESC is a Client Characteristic Configuration Descriptor for TEST_IDX_CHAR_VALUE, it used by peer master as know as a client. As common usage, it config TEST_IDX_CHAR_VALUE indication or notification. Peer can write this att handle to triggle it. Must be [BK_BLE_PERM_SET(RD, ENABLE)](#group__bk__ble__api__v1_1ga12a5ba4c80b8f6fdc20573c242bd0b5b "#group__bk__ble__api__v1_1ga12a5ba4c80b8f6fdc20573c242bd0b5b") | [BK_BLE_PERM_SET(WRITE_REQ, ENABLE)](#group__bk__ble__api__v1_1ga12a5ba4c80b8f6fdc20573c242bd0b5b "#group__bk__ble__api__v1_1ga12a5ba4c80b8f6fdc20573c242bd0b5b")

    Now, you have a basic database for peer, in this case, peer write TEST_IDX_CHAR_DESC or read TEST_IDX_CHAR_VALUE to enable notification, and then we notify peer by TEST_IDX_CHAR_VALUE

    Secondlly, we build ble_db_cfg

    ```
    struct bk_ble_db_cfg ble_db_cfg;

    ble_db_cfg.att_db = (ble_attm_desc_t *)test_service_db;
    ble_db_cfg.att_db_nb = TEST_IDX_NB;
    ble_db_cfg.prf_task_id = g_test_prf_task_id;
    ble_db_cfg.start_hdl = 0;
    ble_db_cfg.svc_perm = BK_BLE_PERM_SET(SVC_UUID_LEN, UUID_16);
    ```

    prf_task_id is app handle. If you have multi att service, used prf_task_id to distinguish it. svc_perm show TEST_IDX_SVC UUID type’s len.

    参数
    :   **-** – ble_db_cfg: service param

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

void bk_ble_set_notice_cb([ble_notice_cb_t](#_CPPv415ble_notice_cb_t "ble_notice_cb_t") func)[](#_CPPv420bk_ble_set_notice_cb15ble_notice_cb_t "永久链接至目标")
:   Register ble event notification callback.

    User example:

    ```
       void ble_at_notice_cb(ble_notice_t notice, void *param)
    {
        switch (notice) {

        case BLE_5_WRITE_EVENT: {

            if (w_req->prf_id == g_test_prf_task_id)
            {
                switch(w_req->att_idx)
                {
                case TEST_IDX_CHAR_DECL:
                    break;
                case TEST_IDX_CHAR_VALUE:
                    break;
                case TEST_IDX_CHAR_DESC:
                    //when peer enable notification, we create time and notify peer, such as
                    //write_buffer = (uint8_t *)os_malloc(s_test_data_len);
                    //bk_ble_send_noti_value(s_test_data_len, write_buffer, g_test_prf_task_id, TEST_IDX_CHAR_VALUE);
                    break;

                default:
                    break;
                }
            }
            break;
        }
        case BLE_5_CREATE_DB:
        //bk_ble_create_db success here
        break;
        }
    }

    bk_ble_set_notice_cb(ble_at_notice_cb);
    ```


    **Attention**
    :   1. you must regist it, otherwise you cant get any event !


    **Attention**
    :   2. you must regist it before bk_ble_create_db, otherwise you cant get BLE_5_CREATE_DB event

    参数
    :   **-** – func: event callback

    返回
    :   - void

uint8_t bk_ble_appm_get_dev_name(uint8_t *name, uint32_t buf_len)[](#_CPPv424bk_ble_appm_get_dev_nameP7uint8_t8uint32_t "永久链接至目标")
:   Get device name.

    参数
    :   **-** – name: store the device name


        - buf_len: the length of buf to store the device name

    返回
    :   - length: the length of device name

uint8_t bk_ble_appm_set_dev_name(uint8_t len, uint8_t *name)[](#_CPPv424bk_ble_appm_set_dev_name7uint8_tP7uint8_t "永久链接至目标")
:   Set device name.

    参数
    :   **-** – len: the length of device name


        - name: the device name to be set

    返回
    :   - length: the length of device name

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_create_advertising(uint8_t actv_idx, [ble_adv_param_t](#_CPPv415ble_adv_param_t "ble_adv_param_t") *adv_param, [ble_cmd_cb_t](#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)[](#_CPPv425bk_ble_create_advertising7uint8_tP15ble_adv_param_t12ble_cmd_cb_t "永久链接至目标")
:   Create a ble advertising activity.

    User example:

    ```
    ble_adv_param_t adv_param;

    adv_param.own_addr_type = 0;//BLE_STATIC_ADDR
    adv_param.adv_type = 0; //ADV_IND
    adv_param.chnl_map = 7;
    adv_param.adv_prop = 3;
    adv_param.adv_intv_min = 0x120; //min
    adv_param.adv_intv_max = 0x160; //max
    adv_param.prim_phy = 1;// 1M
    adv_param.second_phy = 1;// 1M
    actv_idx = bk_ble_get_idle_actv_idx_handle();
    if (actv_idx != UNKNOW_ACT_IDX) {
        bk_ble_create_advertising(actv_idx, &adv_param, ble_at_cmd_cb);
    }
    ```


    **Attention**
    :   1.you must wait callback status, 0 mean success.

    参数
    :   **-** – actv_idx: the index of activity


        - adv_param: the advertising parameter

        - callback: register a callback for this action, ble_cmd_t: BLE_CREATE_ADV

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_start_advertising(uint8_t actv_idx, uint16 duration, [ble_cmd_cb_t](#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)[](#_CPPv424bk_ble_start_advertising7uint8_t6uint1612ble_cmd_cb_t "永久链接至目标")
:   Start a ble advertising.


    **Attention**
    :   1.you must wait callback status, 0 mean success.


    **Attention**
    :   2.must used after bk_ble_create_advertising

    参数
    :   **-** – actv_idx: the index of activity


        - duration: Advertising duration (in unit of 10ms). 0 means that advertising continues

        - callback: register a callback for this action, ble_cmd_t: BLE_START_ADV

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_stop_advertising(uint8_t actv_idx, [ble_cmd_cb_t](#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)[](#_CPPv423bk_ble_stop_advertising7uint8_t12ble_cmd_cb_t "永久链接至目标")
:   Stop the advertising that has been started.


    **Attention**
    :   1.you must wait callback status, 0 mean success.


    **Attention**
    :   2.must used after bk_ble_start_advertising

    参数
    :   **-** – actv_idx: the index of activity


        - callback: register a callback for this action, ble_cmd_t: BLE_STOP_ADV

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_delete_advertising(uint8_t actv_idx, [ble_cmd_cb_t](#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)[](#_CPPv425bk_ble_delete_advertising7uint8_t12ble_cmd_cb_t "永久链接至目标")
:   Delete the advertising that has been created.


    **Attention**
    :   1.you must wait callback status, 0 mean success.


    **Attention**
    :   2.must used after bk_ble_create_advertising

    参数
    :   **-** – actv_idx: the index of activity


        - callback: register a callback for this action, ble_cmd_t: BLE_DELETE_ADV

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_set_adv_data(uint8_t actv_idx, uint8_t *adv_buff, uint8_t adv_len, [ble_cmd_cb_t](#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)[](#_CPPv419bk_ble_set_adv_data7uint8_tP7uint8_t7uint8_t12ble_cmd_cb_t "永久链接至目标")
:   Set the advertising data.

    User example:

    ```
    const uint8_t adv_data[] = {0x02, 0x01, 0x06, 0x0A, 0x09, 0x37 0x32, 0x33, 0x31, 0x4e, 0x5f, 0x42, 0x4c, 0x45};
    bk_ble_set_adv_data(actv_idx, adv_data, sizeof(adv_data), ble_at_cmd_cb);
    ```


    **Attention**
    :   1.you must wait callback status, 0 mean success.


    **Attention**
    :   2.must used after bk_ble_create_advertising

    参数
    :   **-** – actv_idx: the index of activity


        - adv_buff: advertising data

        - adv_len: the length of advertising data

        - callback: register a callback for this action, ble_cmd_t: BLE_SET_ADV_DATA

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_set_scan_rsp_data(uint8_t actv_idx, uint8_t *scan_buff, uint8_t scan_len, [ble_cmd_cb_t](#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)[](#_CPPv424bk_ble_set_scan_rsp_data7uint8_tP7uint8_t7uint8_t12ble_cmd_cb_t "永久链接至目标")
:   Set the scan response data.

    User example:

    ```
    const uint8_t scan_data[] = {0x02, 0x01, 0x06, 0x0A, 0x09, 0x37 0x32, 0x33, 0x31, 0x4e, 0x5f, 0x42, 0x4c, 0x45};
    bk_ble_set_scan_rsp_data(actv_idx, scan_data, sizeof(scan_data), ble_at_cmd_cb);
    ```


    **Attention**
    :   1.you must wait callback status, 0 mean success.


    **Attention**
    :   2.scan rsp data similaly to adv data


    **Attention**
    :   3.must used after bk_ble_create_advertising

    参数
    :   **-** – actv_idx: the index of activity


        - scan_buff: scan response data

        - scan_len: the length of scan response data

        - callback: register a callback for this action, ble_cmd_t: BLE_SET_RSP_DATA

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_set_per_adv_data(uint8_t actv_idx, uint8_t *per_adv_buff, uint8_t per_adv_len, [ble_cmd_cb_t](#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)[](#_CPPv423bk_ble_set_per_adv_data7uint8_tP7uint8_t7uint8_t12ble_cmd_cb_t "永久链接至目标")
:   Set the periodic advertising data.

    User example:

    ```
    const uint8_t adv_data[] = {0x02, 0x01, 0x06, 0x0A, 0x09, 0x37 0x32, 0x33, 0x31, 0x4e, 0x5f, 0x42, 0x4c, 0x45};
    bk_ble_set_per_adv_data(actv_idx, adv_data, sizeof(adv_data), ble_at_cmd_cb);
    ```


    **Attention**
    :   1.you must wait callback status, 0 mean success.


    **Attention**
    :   2.must used after bk_ble_create_advertising

    参数
    :   **-** – actv_idx: the index of activity


        - per_adv_buff: periodic advertising data

        - per_adv_len: the length of periodic advertising data

        - callback: register a callback for this action, ble_cmd_t: BLE_SET_ADV_DATA????

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_set_adv_random_addr(uint8_t actv_idx, uint8_t *addr, [ble_cmd_cb_t](#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)[](#_CPPv426bk_ble_set_adv_random_addr7uint8_tP7uint8_t12ble_cmd_cb_t "永久链接至目标")
:   Set the adv random addr.


    **Attention**
    :   1.you must wait callback status, 0 mean success.


    **Attention**
    :   2.must used after bk_ble_create_advertising

    参数
    :   **-** – actv_idx: the index of activity


        - addr: random address

        - callback: register a callback for this action, ble_cmd_t: BLE_SET_ADV_RANDOM_ADDR

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_read_phy(uint8_t conn_idx)[](#_CPPv415bk_ble_read_phy7uint8_t "永久链接至目标")
:   Read the phy of connection device.

    User example:

    ```
    bk_ble_read_phy(conn_idx);
    ```


    **Attention**
    :   1.must used after after connected

    参数
    :   **-** – conn_idx: the index of connection device

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_set_phy(uint8_t conn_idx, [ble_set_phy_t](#_CPPv413ble_set_phy_t "ble_set_phy_t") *phy_info)[](#_CPPv414bk_ble_set_phy7uint8_tP13ble_set_phy_t "永久链接至目标")
:   Set the phy of connection device.

    User example:

    ```
    ble_set_phy_t * phy = {0x04, 0x01, 0x01};
    //set tx phy to s2 coded phy, and set rx phy to 1M phy
    bk_ble_set_phy(1, phy);
    ```


    **Attention**
    :   1.must used after after connected

    参数
    :   **-** – conn_idx: the index of connection device


        - phy_info: phy parameters

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_update_param(uint8_t conn_idx, [ble_conn_param_t](#_CPPv416ble_conn_param_t "ble_conn_param_t") *conn_param)[](#_CPPv419bk_ble_update_param7uint8_tP16ble_conn_param_t "永久链接至目标")
:   Update connection parameters.


    **Attention**
    :   1.must used after connected

    参数
    :   **-** – conn_idx: the index of connection


        - conn_param: connection parameters

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_disconnect(uint8_t conn_idx)[](#_CPPv417bk_ble_disconnect7uint8_t "永久链接至目标")
:   Disconnect a ble connection.


    **Attention**
    :   1.must used after connected

    参数
    :   **-** – conn_idx: the index of connection

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_gatt_mtu_change(uint8_t conn_idx)[](#_CPPv422bk_ble_gatt_mtu_change7uint8_t "永久链接至目标")
:   Exchange MTU.


    **Attention**
    :   1.must used after connected

    参数
    :   **-** – conn_idx: the index of connection

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_set_max_mtu(uint16_t max_mtu)[](#_CPPv418bk_ble_set_max_mtu8uint16_t "永久链接至目标")
:   Set maximal Exchange MTU.


    **Attention**
    :   1.must used before connected

    参数
    :   **-** – max_mtu: the value to set

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_create_scaning(uint8_t actv_idx, [ble_scan_param_t](#_CPPv416ble_scan_param_t "ble_scan_param_t") *scan_param, [ble_cmd_cb_t](#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)[](#_CPPv421bk_ble_create_scaning7uint8_tP16ble_scan_param_t12ble_cmd_cb_t "永久链接至目标")
:   Create a ble scan activity.

    User exzample:

    ```
    ble_scan_param_t scan_param;

    scan_param.own_addr_type = 0;//BLE_STATIC_ADDR
    scan_param.scan_phy = 5;
    scan_param.scan_intv = 0x64; //interval
    scan_param.scan_wd = 0x1e; //windows
    bk_ble_create_scaning(actv_idx, &, ble_at_cmd);
    ```


    **Attention**
    :   1.you must wait callback status, 0 mean success.

    参数
    :   **-** – actv_idx: the index of activity


        - scan_param: the scan parameter

        - callback: register a callback for this action, ble_cmd_t: BLE_CREATE_SCAN

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_start_scaning(uint8_t actv_idx, [ble_cmd_cb_t](#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)[](#_CPPv420bk_ble_start_scaning7uint8_t12ble_cmd_cb_t "永久链接至目标")
:   Start a ble scan.


    **Attention**
    :   1.you must wait callback status, 0 mean success.


    **Attention**
    :   2.must used after bk_ble_create_scaning


    **Attention**
    :   3.adv will report in ble_notice_cb_t as BLE_5_REPORT_ADV

    参数
    :   **-** – actv_idx: the index of activity


        - callback: register a callback for this action, ble_cmd_t: BLE_START_SCAN

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_start_scaning_ex(uint8_t actv_idx, uint8_t filt_duplicate, uint16_t duration, uint16_t period, [ble_cmd_cb_t](#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)[](#_CPPv423bk_ble_start_scaning_ex7uint8_t7uint8_t8uint16_t8uint16_t12ble_cmd_cb_t "永久链接至目标")

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_stop_scaning(uint8_t actv_idx, [ble_cmd_cb_t](#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)[](#_CPPv419bk_ble_stop_scaning7uint8_t12ble_cmd_cb_t "永久链接至目标")
:   Stop the scan that has been started.


    **Attention**
    :   1.you must wait callback status, 0 mean success.


    **Attention**
    :   2.must used after bk_ble_start_scaning

    参数
    :   **-** – actv_idx: the index of activity


        - callback: register a callback for this action, ble_cmd_t: BLE_STOP_SCAN

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_delete_scaning(uint8_t actv_idx, [ble_cmd_cb_t](#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)[](#_CPPv421bk_ble_delete_scaning7uint8_t12ble_cmd_cb_t "永久链接至目标")
:   Delete the scan that has been created.


    **Attention**
    :   1.you must wait callback status, 0 mean success.


    **Attention**
    :   2.must used after bk_ble_create_scaning

    参数
    :   **-** – actv_idx: the index of activity


        - callback: register a callback for this action, ble_cmd_t: BLE_DELETE_SCAN

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_create_init(uint8_t con_idx, [ble_conn_param_t](#_CPPv416ble_conn_param_t "ble_conn_param_t") *conn_param, [ble_cmd_cb_t](#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)[](#_CPPv418bk_ble_create_init7uint8_tP16ble_conn_param_t12ble_cmd_cb_t "永久链接至目标")
:   Create a activity for initiating a connection.

    User example:

    ```
    ble_conn_param_t conn_param;
    conn_param.intv_min = 0x40; //interval
    conn_param.intv_max = 0x40; //interval
    conn_param.con_latency = 0;
    conn_param.sup_to = 0x200;//supervision timeout
    conn_param.init_phys = 1;// 1M
    bk_ble_create_init(con_idx, &conn_param, ble_at_cmd);
    ```


    **Attention**
    :   1.you must wait callback status, 0 mean success.

    参数
    :   **-** – con_idx: the index of connection


        - conn_param: the connection parameter

        - callback: register a callback for this action, ble_cmd_t: BLE_INIT_CREATE

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_init_start_conn(uint8_t con_idx, [ble_cmd_cb_t](#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)[](#_CPPv422bk_ble_init_start_conn7uint8_t12ble_cmd_cb_t "永久链接至目标")
:   Initiate a connection.


    **Attention**
    :   1.you must wait callback status, 0 mean success.


    **Attention**
    :   2.must used after bk_ble_create_init


    **Attention**
    :   3.when connect result, will recv BLE_5_INIT_CONNECT_EVENT in ble_notice_cb_t

    参数
    :   **-** – con_idx: the index of connection


        - callback: register a callback for this action, ble_cmd_t: BLE_INIT_START_CONN

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_init_stop_conn(uint8_t con_idx, [ble_cmd_cb_t](#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)[](#_CPPv421bk_ble_init_stop_conn7uint8_t12ble_cmd_cb_t "永久链接至目标")
:   Stop a connection.


    **Attention**
    :   1.you must wait callback status, 0 mean success.


    **Attention**
    :   2.must used after bk_ble_init_start_conn

    参数
    :   **-** – con_idx: the index of connection


        - callback: register a callback for this action, ble_cmd_t: BLE_INIT_STOP_CONN

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_init_set_connect_dev_addr(uint8_t connidx, [bd_addr_t](#_CPPv49bd_addr_t "bd_addr_t") *bdaddr, uint8_t addr_type)[](#_CPPv432bk_ble_init_set_connect_dev_addr7uint8_tP9bd_addr_t7uint8_t "永久链接至目标")
:   Set the address of the device to be connected.


    **Attention**
    :   1.you must wait callback status, 0 mean success.


    **Attention**
    :   2.must used after bk_ble_create_init


    **Attention**
    :   3.addr_type must right, if wrong, cant connect

    参数
    :   **-** – connidx: the index of connection


        - bdaddr: the address of the device to be connected

        - addr_type: the address type of the device to be connected, 0: public 1: random

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_create_periodic_sync(uint8_t actv_idx, [ble_cmd_cb_t](#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)[](#_CPPv427bk_ble_create_periodic_sync7uint8_t12ble_cmd_cb_t "永久链接至目标")

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_start_periodic_sync(uint8_t actv_idx, [ble_periodic_param_t](#_CPPv420ble_periodic_param_t "ble_periodic_param_t") *param, [ble_cmd_cb_t](#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)[](#_CPPv426bk_ble_start_periodic_sync7uint8_tP20ble_periodic_param_t12ble_cmd_cb_t "永久链接至目标")

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_stop_periodic_sync(uint8_t actv_idx, [ble_cmd_cb_t](#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)[](#_CPPv425bk_ble_stop_periodic_sync7uint8_t12ble_cmd_cb_t "永久链接至目标")

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_delete_periodic_sync(uint8_t actv_idx, [ble_cmd_cb_t](#_CPPv412ble_cmd_cb_t "ble_cmd_cb_t") callback)[](#_CPPv427bk_ble_delete_periodic_sync7uint8_t12ble_cmd_cb_t "永久链接至目标")

uint8_t bk_ble_get_idle_actv_idx_handle(void)[](#_CPPv431bk_ble_get_idle_actv_idx_handlev "永久链接至目标")
:   Get an idle activity.

    返回
    :   - xx: the idle activity’s index

uint8_t bk_ble_get_max_actv_idx_count(void)[](#_CPPv429bk_ble_get_max_actv_idx_countv "永久链接至目标")
:   Get the maximum count of activities.

    返回
    :   - xx: the maximum count of activities

uint8_t bk_ble_get_max_conn_idx_count(void)[](#_CPPv429bk_ble_get_max_conn_idx_countv "永久链接至目标")
:   Get the maximum count of supported connections.

    返回
    :   - xx: the maximum count of supported connections

uint8_t bk_ble_get_idle_conn_idx_handle(void)[](#_CPPv431bk_ble_get_idle_conn_idx_handlev "永久链接至目标")
:   Get an idle connection activity.

    返回
    :   - xx: the idle connection activity’s index

uint8_t bk_ble_find_conn_idx_from_addr([bd_addr_t](#_CPPv49bd_addr_t "bd_addr_t") *connt_addr)[](#_CPPv430bk_ble_find_conn_idx_from_addrP9bd_addr_t "永久链接至目标")
:   Find the specific connection activity by address.

    参数
    :   **-** – connt_addr: the address of the connected device

    返回
    :   - xx: the index of the connection activity meeting the address

uint8_t bk_ble_get_connect_state([bd_addr_t](#_CPPv49bd_addr_t "bd_addr_t") *connt_addr)[](#_CPPv424bk_ble_get_connect_stateP9bd_addr_t "永久链接至目标")
:   Get the connection state of the specific device.

    参数
    :   **-** – connt_addr: the device’s address

    返回
    :   - 1: this device is connected

        - 0: this device is disconnected

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_get_mac(uint8_t *mac)[](#_CPPv414bk_ble_get_macP7uint8_t "永久链接至目标")
:   get ble mac addr,this api is deprecated,please use bk_bluetooth_get_address


    **Attention**
    :   1. return mac is 6 bytes.

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_send_noti_value(uint8_t con_idx, uint32_t len, uint8_t *buf, uint16_t prf_id, uint16_t att_idx)[](#_CPPv422bk_ble_send_noti_value7uint8_t8uint32_tP7uint8_t8uint16_t8uint16_t "永久链接至目标")
:   As slaver, send a notification of an attribute’s value.

    参数
    :   **-** – con_idx: the index of connection


        - len: the length of attribute’s value

        - buf: attribute’s value

        - prf_id: The id of the profile

        - att_idx: The index of the attribute

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_send_ind_value(uint8_t con_idx, uint32_t len, uint8_t *buf, uint16_t prf_id, uint16_t att_idx)[](#_CPPv421bk_ble_send_ind_value7uint8_t8uint32_tP7uint8_t8uint16_t8uint16_t "永久链接至目标")
:   As slaver, send an indication of an attribute’s value.

    参数
    :   **-** – con_idx: the index of connection


        - len: the length of attribute’s value

        - buf: attribute’s value

        - prf_id: The id of the profile

        - att_idx: The index of the attribute

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_reg_hci_recv_callback([ble_hci_to_host_cb](#_CPPv418ble_hci_to_host_cb "ble_hci_to_host_cb") evt_cb, [ble_hci_to_host_cb](#_CPPv418ble_hci_to_host_cb "ble_hci_to_host_cb") acl_cb)[](#_CPPv428bk_ble_reg_hci_recv_callback18ble_hci_to_host_cb18ble_hci_to_host_cb "永久链接至目标")
:   reg hci recv callback


    **Attention**
    :   1. you must call this after recv BLE_5_STACK_OK evt !

    参数
    :   **-** – evt_cb: evt callback function


        - acl_cb: acl callback function

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_hci_to_controller(uint8_t type, uint8_t *buf, uint16_t len)[](#_CPPv424bk_ble_hci_to_controller7uint8_tP7uint8_t8uint16_t "永久链接至目标")
:   send hci to controller.


    **Attention**
    :   1. you must call this after bk_ble_reg_hci_recv_callback !

    参数
    :   **-** – type: see [BK_BLE_HCI_TYPE](#group__bk__ble__api__v1_1ga28e61788890c70b81bec53fc9a5ea22c "#group__bk__ble__api__v1_1ga28e61788890c70b81bec53fc9a5ea22c").


        - buf: payload

        - len: buf’s len

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_hci_cmd_to_controller(uint8_t *buf, uint16_t len)[](#_CPPv428bk_ble_hci_cmd_to_controllerP7uint8_t8uint16_t "永久链接至目标")
:   send hci cmd to controller.


    **Attention**
    :   1. you must call this after bk_ble_reg_hci_recv_callback !

    参数
    :   **-** – buf: payload


        - len: buf’s len

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_hci_acl_to_controller(uint8_t *buf, uint16_t len)[](#_CPPv428bk_ble_hci_acl_to_controllerP7uint8_t8uint16_t "永久链接至目标")
:   send hci acl to controller.


    **Attention**
    :   1. you must call this after bk_ble_reg_hci_recv_callback !

    参数
    :   **-** – buf: payload


        - len: buf’s len

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

uint8_t bk_ble_if_support_central(uint8_t *count)[](#_CPPv425bk_ble_if_support_centralP7uint8_t "永久链接至目标")

[BK_BLE_CONTROLLER_STACK_TYPE](#_CPPv428BK_BLE_CONTROLLER_STACK_TYPE "BK_BLE_CONTROLLER_STACK_TYPE") bk_ble_get_controller_stack_type(void)[](#_CPPv432bk_ble_get_controller_stack_typev "永久链接至目标")

[BK_BLE_HOST_STACK_TYPE](#_CPPv422BK_BLE_HOST_STACK_TYPE "BK_BLE_HOST_STACK_TYPE") bk_ble_get_host_stack_type(void)[](#_CPPv426bk_ble_get_host_stack_typev "永久链接至目标")

uint8_t bk_ble_get_env_state(void)[](#_CPPv420bk_ble_get_env_statev "永久链接至目标")

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_set_task_stack_size(uint16_t size)[](#_CPPv426bk_ble_set_task_stack_size8uint16_t "永久链接至目标")

void bk_ble_register_app_sdp_charac_callback([app_sdp_charac_callback](#_CPPv423app_sdp_charac_callback "app_sdp_charac_callback") cb)[](#_CPPv439bk_ble_register_app_sdp_charac_callback23app_sdp_charac_callback "永久链接至目标")

void bk_ble_register_app_sdp_common_callback([app_sdp_comm_callback](#_CPPv421app_sdp_comm_callback "app_sdp_comm_callback") cb)[](#_CPPv439bk_ble_register_app_sdp_common_callback21app_sdp_comm_callback "永久链接至目标")

uint8_t bk_ble_gatt_write_ccc(uint8_t con_idx, uint16_t ccc_handle, uint16_t ccc_value)[](#_CPPv421bk_ble_gatt_write_ccc7uint8_t8uint16_t8uint16_t "永久链接至目标")
:   As master, enable notification or indication.

    参数
    :   **-** – con_idx: the index of connection


        - ccc_handle: the handle of Client Characteristic Configuration descriptor

        - ccc_value: descriptor value, 0x01 means notification ,0x02 means indication

    返回
    :   - 0: succeed

        - others: errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_gatt_write_value(uint8_t con_idx, uint16_t att_handle, uint16_t len, uint8_t *data)[](#_CPPv423bk_ble_gatt_write_value7uint8_t8uint16_t8uint16_tP7uint8_t "永久链接至目标")
:   As master, write attribute value.

    参数
    :   **-** – con_idx: the index of connection


        - att_handle: the handle of attribute value

        - data: value data

        - len: the length of attribute value

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: fail

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_read_response_value(uint8_t con_idx, uint32_t len, uint8_t *buf, uint16_t prf_id, uint16_t att_idx)[](#_CPPv426bk_ble_read_response_value7uint8_t8uint32_tP7uint8_t8uint16_t8uint16_t "永久链接至目标")
:   As slaver, send response value.

    参数
    :   **-** – con_idx: the idx of app connections


        - len: the length of attribute’s value

        - buf: attribute’s value

        - prf_id: The id of the profile

        - att_idx: The index of the attribute

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: fail

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_sec_send_auth_mode(uint8_t con_idx, uint8_t mode, uint8_t iocap, uint8_t sec_req, uint8_t oob)[](#_CPPv425bk_ble_sec_send_auth_mode7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t "永久链接至目标")
:   As master, configure attribute value.

    参数
    :   **-** – con_idx: the index of connection


        - mode: authentication features

        - iocap: IO Capability Values

        - sec_req: Security Defines

        - oob: OOB Data Present Flag Values

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: fail

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_sec_send_auth_mode_ext(uint8_t con_idx, uint8_t mode, uint8_t iocap, uint8_t sec_req, uint8_t oob, uint8_t initiator_key_distr, uint8_t responder_key_distr)[](#_CPPv429bk_ble_sec_send_auth_mode_ext7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t "永久链接至目标")
:   As master, configure auth mode param.

    参数
    :   **-** – con_idx: the index of connection


        - mode: authentication features

        - iocap: IO Capability Values

        - sec_req: Security Defines

        - oob: OOB Data Present Flag Values

        - initiator_key_distr: init key distr, see gap_key_distr

        - responder_key_distr: resp key distr, see gap_key_distr

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: fail

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_init(void)[](#_CPPv411bk_ble_initv "永久链接至目标")
:   ble init function,this api is deprecated,please use bk_bluetooth_init.

    Param

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_deinit(void)[](#_CPPv413bk_ble_deinitv "永久链接至目标")
:   ble deinit function,this api is deprecated,please use bk_bluetooth_deinit.

    Param

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_delete_service(struct [bk_ble_db_cfg](#_CPPv413bk_ble_db_cfg "bk_ble_db_cfg") *ble_db_cfg)[](#_CPPv421bk_ble_delete_serviceP13bk_ble_db_cfg "永久链接至目标")
:   Unregister a gatt service.

    User example:

    ```
    struct bk_ble_db_cfg ble_db_cfg;
    uint16 service_uuid = 0x1800;

    os_memcpy(&(ble_db_cfg.uuid[0]), &service_uuid, 2);
    ble_db_cfg.svc_perm = BK_BLE_PERM_SET(SVC_UUID_LEN, UUID_16);
    ```


    **Attention**
    :   1.you must set the uuid of service and the len of uuid.

    参数
    :   **-** – ble_db_cfg: service param

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_att_read(uint8_t con_idx, uint16_t att_handle)[](#_CPPv415bk_ble_att_read7uint8_t8uint16_t "永久链接至目标")
:   As master, read attribute value, the result is reported in the callback registered through bk_ble_register_app_sdp_charac_callback.

    参数
    :   **-** – con_idx: the index of connection


        - att_handle: the handle of attribute value

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: fail

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_create_bond(uint8_t con_idx, uint8_t auth, uint8_t iocap, uint8_t sec_req, uint8_t oob)[](#_CPPv418bk_ble_create_bond7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t "永久链接至目标")
:   start authentication the link


    **Attention**
    :   if the link has not been bonded, it will trigger pairing, otherwise it will trigger the link encryption.

    参数
    :   **-** – con_idx: the index of connection


        - auth: authentication features(see enum [gap_auth](#group__bk__ble__api__v1__typedef_1gabddf59399b398b7d0cdb34f77becadb8 "#group__bk__ble__api__v1__typedef_1gabddf59399b398b7d0cdb34f77becadb8"))

        - iocap: IO Capability Values(see enum [bk_ble_gap_io_cap](#group__bk__ble__api__v1__typedef_1ga47c2938c3450762bfc853c0891ce35d4 "#group__bk__ble__api__v1__typedef_1ga47c2938c3450762bfc853c0891ce35d4"))

        - sec_req: Security Defines(see enum [gap_sec_req](#group__bk__ble__api__v1__typedef_1ga5bdf085cbe078d063965de5462611445 "#group__bk__ble__api__v1__typedef_1ga5bdf085cbe078d063965de5462611445"))

        - oob: OOB Data Present Flag Values(see enum [gap_oob](#group__bk__ble__api__v1__typedef_1ga009fe656dba3e223453288e3fc6fa68c "#group__bk__ble__api__v1__typedef_1ga009fe656dba3e223453288e3fc6fa68c"))

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: fail

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_create_bond_ext(uint8_t con_idx, uint8_t auth, uint8_t iocap, uint8_t sec_req, uint8_t oob, uint8_t initiator_key_distr, uint8_t responder_key_distr)[](#_CPPv422bk_ble_create_bond_ext7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t "永久链接至目标")
:   create bond


    **Attention**
    :   if the link has not been bonded, it will trigger pairing, otherwise it will trigger the link encryption.

    参数
    :   **-** – con_idx: the index of connection


        - auth: authentication features(see enum [gap_auth](#group__bk__ble__api__v1__typedef_1gabddf59399b398b7d0cdb34f77becadb8 "#group__bk__ble__api__v1__typedef_1gabddf59399b398b7d0cdb34f77becadb8"))

        - iocap: IO Capability Values(see enum [bk_ble_gap_io_cap](#group__bk__ble__api__v1__typedef_1ga47c2938c3450762bfc853c0891ce35d4 "#group__bk__ble__api__v1__typedef_1ga47c2938c3450762bfc853c0891ce35d4"))

        - sec_req: Security Defines(see enum [gap_sec_req](#group__bk__ble__api__v1__typedef_1ga5bdf085cbe078d063965de5462611445 "#group__bk__ble__api__v1__typedef_1ga5bdf085cbe078d063965de5462611445"))

        - oob: OOB Data Present Flag Values(see enum [gap_oob](#group__bk__ble__api__v1__typedef_1ga009fe656dba3e223453288e3fc6fa68c "#group__bk__ble__api__v1__typedef_1ga009fe656dba3e223453288e3fc6fa68c"))

        - initiator_key_distr: init key distr, see gap_key_distr

        - responder_key_distr: resp key distr, see gap_key_distr

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: fail

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_passkey_send(uint8_t con_idx, uint8_t accept, uint32_t passkey)[](#_CPPv419bk_ble_passkey_send7uint8_t7uint8_t8uint32_t "永久链接至目标")
:   send passkey when pairing

    参数
    :   **-** – con_idx: the index of connection


        - accept: accept pair

        - passkey: the num that peer need to input or local need to input

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: fail

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_number_compare_send(uint8_t con_idx, uint8_t accept)[](#_CPPv426bk_ble_number_compare_send7uint8_t7uint8_t "永久链接至目标")
:   send number compare accept when pairing

    参数
    :   **-** – con_idx: the index of connection


        - accept: accept pair

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: fail

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_read_rssi(uint8_t conn_idx)[](#_CPPv416bk_ble_read_rssi7uint8_t "永久链接至目标")
:   Read the rssi of connection device. The result will report in callback registered through bk_ble_set_notice_cb with evt BLE_5_READ_RSSI_CMPL_EVENT, and param is [ble_read_rssi_rsp_t](#structble__read__rssi__rsp__t "#structble__read__rssi__rsp__t") *.

    User example:

    ```
    bk_ble_read_rssi(conn_idx);
    ```


    **Attention**
    :   1.must used after after connected

    参数
    :   **-** – conn_idx: the index of connection device

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_config_local_appearance(uint16_t appearance)[](#_CPPv430bk_ble_config_local_appearance8uint16_t "永久链接至目标")
:   set local gap appearance

    参数
    :   **appearance** – **[in]** - External appearance value, these values are defined by the Bluetooth SIG, please refer to [https://specificationrefs.bluetooth.com/assigned-values/Appearance%20Values.pdf](https://specificationrefs.bluetooth.com/assigned-values/Appearance%20Values.pdf "https://specificationrefs.bluetooth.com/assigned-values/Appearance%20Values.pdf")

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: other errors.

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_discover_primary_service(uint8_t conn_id, uint16_t sh, uint16_t eh)[](#_CPPv431bk_ble_discover_primary_service7uint8_t8uint16_t8uint16_t "永久链接至目标")
:   Discover peer primary service. The result is report in the callback registered through bk_ble_register_app_sdp_common_callback, and evt is MST_TYPE_DISCOVER_PRI_SERVICE_RSP. When completed, callback will report MST_TYPE_DISCOVER_COMPLETED with [ble_descover_complete_inf](#structble__descover__complete__inf "#structble__descover__complete__inf") and MST_TYPE_DISCOVER_PRI_SERVICE_RSP.

    参数
    :   **-** – sh: att start handle


        - eh: att end handle

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: fail

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_discover_primary_service_by_uuid(uint8_t conn_id, uint16_t sh, uint16_t eh, uint16_t uuid)[](#_CPPv439bk_ble_discover_primary_service_by_uuid7uint8_t8uint16_t8uint16_t8uint16_t "永久链接至目标")
:   Discover peer primary service. The result is report in the callback registered through bk_ble_register_app_sdp_common_callback, and evt is MST_TYPE_DISCOVER_PRI_SERVICE_BY_UUID_RSP. When completed, callback will report MST_TYPE_DISCOVER_COMPLETED with [ble_descover_complete_inf](#structble__descover__complete__inf "#structble__descover__complete__inf") and MST_TYPE_DISCOVER_PRI_SERVICE_BY_UUID_RSP.

    参数
    :   **-** – sh: att start handle


        - eh: att end handle

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_discover_primary_service_by_128uuid(uint8_t conn_id, uint16_t sh, uint16_t eh, uint8_t *uuid)[](#_CPPv442bk_ble_discover_primary_service_by_128uuid7uint8_t8uint16_t8uint16_tP7uint8_t "永久链接至目标")
:   Discover peer primary service. The result is report in the callback registered through bk_ble_register_app_sdp_common_callback, and evt is MST_TYPE_DISCOVER_PRI_SERVICE_BY_128_UUID_RSP. When completed, callback will report MST_TYPE_DISCOVER_COMPLETED with [ble_descover_complete_inf](#structble__descover__complete__inf "#structble__descover__complete__inf") and MST_TYPE_DISCOVER_PRI_SERVICE_BY_128_UUID_RSP. bk_ble_read_rssi(conn_idx);.

    参数
    :   **-** – conn_id: the index of connection


        - sh: att start handle

        - eh: att end handle

        - uuid: uuid that service need to find in 128bits

    返回
    :   - others: fail

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_discover_characteristic(uint8_t conn_id, uint16_t sh, uint16_t eh)[](#_CPPv430bk_ble_discover_characteristic7uint8_t8uint16_t8uint16_t "永久链接至目标")
:   Discover peer characteristic. The result is report in the callback registered through bk_ble_register_app_sdp_common_callback, and evt is MST_TYPE_DISCOVER_CHAR_RSP. When completed, callback will report MST_TYPE_DISCOVER_COMPLETED with [ble_descover_complete_inf](#structble__descover__complete__inf "#structble__descover__complete__inf") and MST_TYPE_DISCOVER_CHAR_RSP.

    参数
    :   **-** – conn_id: the index of connection


        - sh: att start handle

        - eh: att end handle

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: fail

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_discover_characteristic_by_uuid(uint8_t conn_id, uint16_t sh, uint16_t eh, uint16_t uuid)[](#_CPPv438bk_ble_discover_characteristic_by_uuid7uint8_t8uint16_t8uint16_t8uint16_t "永久链接至目标")
:   Discover peer characteristic. The result is report in the callback registered through bk_ble_register_app_sdp_common_callback, and evt is MST_TYPE_DISCOVER_CHAR_BY_UUID_RSP. When completed, callback will report MST_TYPE_DISCOVER_COMPLETED with [ble_descover_complete_inf](#structble__descover__complete__inf "#structble__descover__complete__inf") and MST_TYPE_DISCOVER_CHAR_BY_UUID_RSP.

    参数
    :   **-** – conn_id: the index of connection


        - sh: att start handle

        - eh: att end handle

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: fail

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_discover_characteristic_by_128uuid(uint8_t conn_id, uint16_t sh, uint16_t eh, uint8_t *uuid)[](#_CPPv441bk_ble_discover_characteristic_by_128uuid7uint8_t8uint16_t8uint16_tP7uint8_t "永久链接至目标")
:   Discover peer characteristic. The result is report in the callback registered through bk_ble_register_app_sdp_common_callback, and evt is MST_TYPE_DISCOVER_CHAR_BY_128_UUID_RSP. When completed, callback will report MST_TYPE_DISCOVER_COMPLETED with [ble_descover_complete_inf](#structble__descover__complete__inf "#structble__descover__complete__inf") and MST_TYPE_DISCOVER_CHAR_BY_128_UUID_RSP.

    参数
    :   **-** – conn_id: the index of connection


        - sh: att start handle

        - eh: att end handle

    返回
    :   - others: fail

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_discover_characteristic_descriptor(uint8_t conn_id, uint16_t sh, uint16_t eh)[](#_CPPv441bk_ble_discover_characteristic_descriptor7uint8_t8uint16_t8uint16_t "永久链接至目标")
:   Discover peer characteristic descriptor. The result is report in the callback registered through bk_ble_register_app_sdp_common_callback, and evt is MST_TYPE_DISCOVER_CHAR_DESC. When completed, callback will report MST_TYPE_DISCOVER_COMPLETED with [ble_descover_complete_inf](#structble__descover__complete__inf "#structble__descover__complete__inf") and MST_TYPE_DISCOVER_CHAR_DESC.

    参数
    :   **-** – conn_id: the index of connection


        - sh: att start handle

        - eh: att end handle

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: fail

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_gattc_read(uint8_t con_idx, uint16_t att_handle, uint16_t offset)[](#_CPPv417bk_ble_gattc_read7uint8_t8uint16_t8uint16_t "永久链接至目标")
:   As master, read attribute value, the result is reported in the callback registered through bk_ble_register_app_sdp_charac_callback.

    参数
    :   **-** – con_idx: the index of connection


        - att_handle: the handle of attribute value

        - offset: the offset of attribute value

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: fail

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_gattc_read_by_uuid(uint8_t conn_id, uint16_t sh, uint16_t eh, uint8_t *uuid, uint8_t uuid_len)[](#_CPPv425bk_ble_gattc_read_by_uuid7uint8_t8uint16_t8uint16_tP7uint8_t7uint8_t "永久链接至目标")
:   As master, read attribute value, the result is reported in the callback registered through bk_ble_register_app_sdp_charac_callback.

    参数
    :   **-** – con_idx: the index of connection


        - sh: the start handle of attribute

        - eh: the end handle of attribute

        - uuid: uuid

        - uuid_len: uuid len, may be 2 or 16

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: fail

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_gattc_write(uint8_t con_idx, uint16_t att_handle, uint8_t *data, uint16_t len, uint8_t is_write_cmd)[](#_CPPv418bk_ble_gattc_write7uint8_t8uint16_tP7uint8_t8uint16_t7uint8_t "永久链接至目标")
:   As master, write attribute value.

    参数
    :   **-** – con_idx: the index of connection


        - att_handle: the handle of attribute value

        - data: value data

        - len: the length of attribute value

        - is_write_cmd: when true, will trigger write cmd, otherwise write req.

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: fail

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_clear_white_list(void)[](#_CPPv423bk_ble_clear_white_listv "永久链接至目标")
:   clear the white list.

    Param

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_add_devices_to_while_list([bd_addr_t](#_CPPv49bd_addr_t "bd_addr_t") *addr, uint8_t addr_type)[](#_CPPv432bk_ble_add_devices_to_while_listP9bd_addr_t7uint8_t "永久链接至目标")
:   Add a device to the while list.

    参数
    :   **-** – addr: the address of the device.


        - addr_type: the type of the address, 0 is public address, 1 is random address.

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: fail

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_remove_devices_from_while_list([bd_addr_t](#_CPPv49bd_addr_t "bd_addr_t") *addr, uint8_t addr_type)[](#_CPPv437bk_ble_remove_devices_from_while_listP9bd_addr_t7uint8_t "永久链接至目标")
:   Remove a device from the while list.

    参数
    :   **-** – addr: the address of the device.


        - addr_type: the type of the address, 0 is public address, 1 is random address.

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: fail

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_tx_power_set(float pwr_gain)[](#_CPPv419bk_ble_tx_power_setf "永久链接至目标")
:   Set tx power.

    参数
    :   **-** – pwr_gain: tx power gain

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: fail

[ble_err_t](#_CPPv49ble_err_t "ble_err_t") bk_ble_authorization_reply(uint8_t con_idx, uint16_t prf_id, uint16_t att_idx, uint8_t type, uint8_t accept, uint32_t len, uint8_t *buf)[](#_CPPv426bk_ble_authorization_reply7uint8_t8uint16_t8uint16_t7uint8_t7uint8_t8uint32_tP7uint8_t "永久链接至目标")
:   As slaver, respond to a read/write user authorization request.If the attribute is configured with authorization flag (see enum [bk_ble_authorization_flag](#group__bk__ble__api__v1_1ga9527a3c790b83c4cdc4757218cbf4f18 "#group__bk__ble__api__v1_1ga9527a3c790b83c4cdc4757218cbf4f18")),the BLE_5_AUTHOR_READ_EVENT/BLE_5_AUTHOR_WRITE_EVENT will be reported, then this api can be used to reply.

    参数
    :   **-** – con_idx: the index of connection


        - prf_id: The id of the profile

        - att_idx: The index of the attribute

        - type: 0: read respond ;1: write respond;

        - accept: 1: permit to read/write; 0: reject to read/write

        - len: the length of attribute’s value(valid for read respond)

        - buf: attribute’s value(valid for read respond)

    返回
    :   - BK_ERR_BLE_SUCCESS: succeed

        - others: fail


## API Typedefs[](#api-typedefs "永久链接至标题")


### Header File[](#id1 "永久链接至标题")


- [bluetooth/bk_ble_types.h](https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_ble_types.h "https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_ble_types.h")


### Structures[](#structures "永久链接至标题")

struct ble_sdp_svc_ind[](#_CPPv415ble_sdp_svc_ind "永久链接至目标")
:   Public Members

    uint8_t uuid_len[](#_CPPv4N15ble_sdp_svc_ind8uuid_lenE "永久链接至目标")
    :   Service UUID Length.

    uint8_t uuid[16][](#_CPPv4N15ble_sdp_svc_ind4uuidE "永久链接至目标")
    :   Service UUID.

    uint16_t start_hdl[](#_CPPv4N15ble_sdp_svc_ind9start_hdlE "永久链接至目标")
    :   Service start handle.

    uint16_t end_hdl[](#_CPPv4N15ble_sdp_svc_ind7end_hdlE "永久链接至目标")
    :   Service end handle.

struct ble_sdp_char_inf[](#_CPPv416ble_sdp_char_inf "永久链接至目标")
:   characteristic info

    Public Members

    uint8_t uuid_len[](#_CPPv4N16ble_sdp_char_inf8uuid_lenE "永久链接至目标")
    :   Characteristic UUID Length.

    uint8_t uuid[16][](#_CPPv4N16ble_sdp_char_inf4uuidE "永久链接至目标")
    :   Characteristic UUID.

    uint16_t char_hdl[](#_CPPv4N16ble_sdp_char_inf8char_hdlE "永久链接至目标")
    :   Characteristic handle.

    uint16_t val_hdl[](#_CPPv4N16ble_sdp_char_inf7val_hdlE "永久链接至目标")
    :   Value handle.

    uint8_t prop[](#_CPPv4N16ble_sdp_char_inf4propE "永久链接至目标")
    :   Characteristic properties.

    uint8_t char_ehdl_off[](#_CPPv4N16ble_sdp_char_inf13char_ehdl_offE "永久链接至目标")
    :   End of characteristic offset.

struct ble_sdp_char_desc_inf[](#_CPPv421ble_sdp_char_desc_inf "永久链接至目标")
:   characteristic description

    Public Members

    uint8_t uuid_len[](#_CPPv4N21ble_sdp_char_desc_inf8uuid_lenE "永久链接至目标")
    :   UUID length.

    uint8_t uuid[16][](#_CPPv4N21ble_sdp_char_desc_inf4uuidE "永久链接至目标")
    :   UUID.

    uint16_t desc_hdl[](#_CPPv4N21ble_sdp_char_desc_inf8desc_hdlE "永久链接至目标")
    :   Descriptor handle.

struct ble_descover_complete_inf[](#_CPPv425ble_descover_complete_inf "永久链接至目标")
:   discover completed evt param, see MST_TYPE_DISCOVER_COMPLETED

struct ble_smp_ind_t[](#_CPPv413ble_smp_ind_t "永久链接至目标")

struct ble_attc_wr_rd_op[](#_CPPv417ble_attc_wr_rd_op "永久链接至目标")
:   Public Members

    uint8_t status[](#_CPPv4N17ble_attc_wr_rd_op6statusE "永久链接至目标")
    :   Status of the request.

    uint16_t seq_num[](#_CPPv4N17ble_attc_wr_rd_op7seq_numE "永久链接至目标")
    :   operation sequence number - provided when operation is started

struct ble_attc_event_ind[](#_CPPv418ble_attc_event_ind "永久链接至目标")
:   Public Members

    enum [msg_attc](#_CPPv48msg_attc "msg_attc") type[](#_CPPv4N18ble_attc_event_ind4typeE "永久链接至目标")
    :   Event Type.

    uint16_t start_hdl[](#_CPPv4N18ble_attc_event_ind9start_hdlE "永久链接至目标")
    :   if start_hdl = end_hdl = 0,it is invaild

struct ble_cmd_param_t[](#_CPPv415ble_cmd_param_t "永久链接至目标")
:   Public Members

    uint8_t cmd_idx[](#_CPPv4N15ble_cmd_param_t7cmd_idxE "永久链接至目标")
    :   actv_idx

    [ble_err_t](#_CPPv49ble_err_t "ble_err_t") status[](#_CPPv4N15ble_cmd_param_t6statusE "永久链接至目标")
    :   The status for this command

struct ble_att_info_req_t[](#_CPPv418ble_att_info_req_t "永久链接至目标")
:   Public Members

    uint8_t conn_idx[](#_CPPv4N18ble_att_info_req_t8conn_idxE "永久链接至目标")
    :   The index of the connection

    uint16_t prf_id[](#_CPPv4N18ble_att_info_req_t6prf_idE "永久链接至目标")
    :   The id of the profile

    uint16_t att_idx[](#_CPPv4N18ble_att_info_req_t7att_idxE "永久链接至目标")
    :   The index of the attribute

    uint16_t length[](#_CPPv4N18ble_att_info_req_t6lengthE "永久链接至目标")
    :   The length of the attribute

    uint8_t status[](#_CPPv4N18ble_att_info_req_t6statusE "永久链接至目标")
    :   Use to know if it’s possible to modify the attribute ,can contains authorization or application error code

struct ble_write_req_t[](#_CPPv415ble_write_req_t "永久链接至目标")
:   Public Members

    uint8_t conn_idx[](#_CPPv4N15ble_write_req_t8conn_idxE "永久链接至目标")
    :   The index of the connection

    uint16_t prf_id[](#_CPPv4N15ble_write_req_t6prf_idE "永久链接至目标")
    :   The id of the profile

    uint16_t att_idx[](#_CPPv4N15ble_write_req_t7att_idxE "永久链接至目标")
    :   The index of the attribute

    uint8_t *value[](#_CPPv4N15ble_write_req_t5valueE "永久链接至目标")
    :   The attribute value

    uint16_t len[](#_CPPv4N15ble_write_req_t3lenE "永久链接至目标")
    :   The length of the attribute value

struct ble_read_req_t[](#_CPPv414ble_read_req_t "永久链接至目标")
:   Public Members

    uint8_t conn_idx[](#_CPPv4N14ble_read_req_t8conn_idxE "永久链接至目标")
    :   The index of the connection

    uint16_t prf_id[](#_CPPv4N14ble_read_req_t6prf_idE "永久链接至目标")
    :   The id of the profile

    uint16_t att_idx[](#_CPPv4N14ble_read_req_t7att_idxE "永久链接至目标")
    :   The index of the attribute

    uint8_t *value[](#_CPPv4N14ble_read_req_t5valueE "永久链接至目标")
    :   The attribute value

    uint16_t size[](#_CPPv4N14ble_read_req_t4sizeE "永久链接至目标")
    :   The size of attribute value to read

    uint16_t length[](#_CPPv4N14ble_read_req_t6lengthE "永久链接至目标")
    :   The data length read

struct ble_recv_adv_t[](#_CPPv414ble_recv_adv_t "永久链接至目标")
:   Public Members

    uint8_t actv_idx[](#_CPPv4N14ble_recv_adv_t8actv_idxE "永久链接至目标")
    :   The index of the activity

    uint8_t evt_type[](#_CPPv4N14ble_recv_adv_t8evt_typeE "永久链接至目标")
    :   Event type (see enum [adv_report_info](#group__bk__ble__api__v1__typedef_1ga8648555af760e5e51dcbd0829cb4dd16 "#group__bk__ble__api__v1__typedef_1ga8648555af760e5e51dcbd0829cb4dd16") and see enum [adv_report_type](#group__bk__ble__api__v1__typedef_1ga586827f2b8e2c17b183858febd25a205 "#group__bk__ble__api__v1__typedef_1ga586827f2b8e2c17b183858febd25a205"))

    uint8_t adv_addr_type[](#_CPPv4N14ble_recv_adv_t13adv_addr_typeE "永久链接至目标")
    :   Advertising address type: public/random

    uint8_t adv_addr[6][](#_CPPv4N14ble_recv_adv_t8adv_addrE "永久链接至目标")
    :   Advertising address value

    uint8_t data_len[](#_CPPv4N14ble_recv_adv_t8data_lenE "永久链接至目标")
    :   Data length in advertising packet

    uint8_t *data[](#_CPPv4N14ble_recv_adv_t4dataE "永久链接至目标")
    :   Data of advertising packet

    int8_t rssi[](#_CPPv4N14ble_recv_adv_t4rssiE "永久链接至目标")
    :   RSSI value for advertising packet (in dBm, between -127 and +20 dBm)

struct ble_mtu_change_t[](#_CPPv416ble_mtu_change_t "永久链接至目标")
:   Public Members

    uint8_t conn_idx[](#_CPPv4N16ble_mtu_change_t8conn_idxE "永久链接至目标")
    :   The index of connection

    uint16_t mtu_size[](#_CPPv4N16ble_mtu_change_t8mtu_sizeE "永久链接至目标")
    :   The MTU size to exchange

struct ble_conn_ind_t[](#_CPPv414ble_conn_ind_t "永久链接至目标")
:   Public Members

    uint8_t conn_idx[](#_CPPv4N14ble_conn_ind_t8conn_idxE "永久链接至目标")
    :   The index of connection.

    uint8_t peer_addr_type[](#_CPPv4N14ble_conn_ind_t14peer_addr_typeE "永久链接至目标")
    :   Peer address type.

    uint8_t peer_addr[6][](#_CPPv4N14ble_conn_ind_t9peer_addrE "永久链接至目标")
    :   Peer BT address.

    uint8_t clk_accuracy[](#_CPPv4N14ble_conn_ind_t12clk_accuracyE "永久链接至目标")
    :   Clock accuracy.

    uint16_t con_interval[](#_CPPv4N14ble_conn_ind_t12con_intervalE "永久链接至目标")
    :   Connection interval.

    uint16_t con_latency[](#_CPPv4N14ble_conn_ind_t11con_latencyE "永久链接至目标")
    :   Connection latency.

    uint16_t sup_to[](#_CPPv4N14ble_conn_ind_t6sup_toE "永久链接至目标")
    :   Link supervision timeout.

struct ble_discon_ind_t[](#_CPPv416ble_discon_ind_t "永久链接至目标")
:   Public Members

    uint8_t conn_idx[](#_CPPv4N16ble_discon_ind_t8conn_idxE "永久链接至目标")
    :   The index of connection.

    uint8_t reason[](#_CPPv4N16ble_discon_ind_t6reasonE "永久链接至目标")
    :   Reason of disconnection.

struct ble_create_db_t[](#_CPPv415ble_create_db_t "永久链接至目标")
:   Public Members

    uint8_t status[](#_CPPv4N15ble_create_db_t6statusE "永久链接至目标")
    :   The status for creating db

    uint8_t prf_id[](#_CPPv4N15ble_create_db_t6prf_idE "永久链接至目标")
    :   The id of the profile

struct ble_attm_desc_t[](#_CPPv415ble_attm_desc_t "永久链接至目标")
:   Public Members

    uint8_t uuid[16][](#_CPPv4N15ble_attm_desc_t4uuidE "永久链接至目标")
    :   16 bits UUID LSB First

    uint16_t perm[](#_CPPv4N15ble_attm_desc_t4permE "永久链接至目标")
    :   Attribute Permissions (see enum [bk_ble_perm_mask](#group__bk__ble__api__v1_1gaa529f18ac0ecdf658b9e49c2fffc7f22 "#group__bk__ble__api__v1_1gaa529f18ac0ecdf658b9e49c2fffc7f22"))

    uint16_t ext_perm[](#_CPPv4N15ble_attm_desc_t8ext_permE "永久链接至目标")
    :   Attribute Extended Permissions (see enum [bk_ble_ext_perm_mask](#group__bk__ble__api__v1_1ga3c750771a137d5504854bfcebb6e5235 "#group__bk__ble__api__v1_1ga3c750771a137d5504854bfcebb6e5235"))

    uint16_t max_size[](#_CPPv4N15ble_attm_desc_t8max_sizeE "永久链接至目标")
    :   Attribute Max Size note: for characteristic declaration contains handle offset note: for included service, contains target service handle

    void *p_value_context[](#_CPPv4N15ble_attm_desc_t15p_value_contextE "永久链接至目标")
    :   pointer to value if [BK_BLE_PERM_SET(RI, ENABLE)](#group__bk__ble__api__v1_1ga12a5ba4c80b8f6fdc20573c242bd0b5b "#group__bk__ble__api__v1_1ga12a5ba4c80b8f6fdc20573c242bd0b5b") not set and [BK_BLE_PERM_SET(VALUE_INCL, ENABLE)](#group__bk__ble__api__v1_1ga12a5ba4c80b8f6fdc20573c242bd0b5b "#group__bk__ble__api__v1_1ga12a5ba4c80b8f6fdc20573c242bd0b5b") set

    uint8_t author_flag[](#_CPPv4N15ble_attm_desc_t11author_flagE "永久链接至目标")
    :   read/write Authorization permission flag (see enum [bk_ble_authorization_flag](#group__bk__ble__api__v1_1ga9527a3c790b83c4cdc4757218cbf4f18 "#group__bk__ble__api__v1_1ga9527a3c790b83c4cdc4757218cbf4f18"))

struct bk_ble_db_cfg[](#_CPPv413bk_ble_db_cfg "永久链接至目标")
:   Public Members

    uint8_t uuid[16][](#_CPPv4N13bk_ble_db_cfg4uuidE "永久链接至目标")
    :   Service uuid.

    uint8_t att_db_nb[](#_CPPv4N13bk_ble_db_cfg9att_db_nbE "永久链接至目标")
    :   Number of db.

    uint16_t start_hdl[](#_CPPv4N13bk_ble_db_cfg9start_hdlE "永久链接至目标")
    :   Start handler, 0 means autoalloc.

    [ble_attm_desc_t](#_CPPv415ble_attm_desc_t "ble_attm_desc_t") *att_db[](#_CPPv4N13bk_ble_db_cfg6att_dbE "永久链接至目标")
    :   Attribute database.

    uint8_t svc_perm[](#_CPPv4N13bk_ble_db_cfg8svc_permE "永久链接至目标")
    :   Service config.

struct ble_init_config_t[](#_CPPv417ble_init_config_t "永久链接至目标")

struct bd_addr_t[](#_CPPv49bd_addr_t "永久链接至目标")

struct ble_cmd_cmp_evt_t[](#_CPPv417ble_cmd_cmp_evt_t "永久链接至目标")
:   Public Members

    uint8_t conn_idx[](#_CPPv4N17ble_cmd_cmp_evt_t8conn_idxE "永久链接至目标")
    :   The index of connection.

    uint8_t cmd[](#_CPPv4N17ble_cmd_cmp_evt_t3cmdE "永久链接至目标")
    :   Command operation.

    uint8_t status[](#_CPPv4N17ble_cmd_cmp_evt_t6statusE "永久链接至目标")
    :   Command operation status.

struct ble_read_phy_t[](#_CPPv414ble_read_phy_t "永久链接至目标")
:   Public Members

    uint8_t tx_phy[](#_CPPv4N14ble_read_phy_t6tx_phyE "永久链接至目标")
    :   The transmitter PHY

    uint8_t rx_phy[](#_CPPv4N14ble_read_phy_t6rx_phyE "永久链接至目标")
    :   The receiver PHY

struct ble_set_phy_t[](#_CPPv413ble_set_phy_t "永久链接至目标")
:   Public Members

    uint8_t tx_phy[](#_CPPv4N13ble_set_phy_t6tx_phyE "永久链接至目标")
    :   The transmitter PHY

    uint8_t rx_phy[](#_CPPv4N13ble_set_phy_t6rx_phyE "永久链接至目标")
    :   The receiver PHY

    uint8_t phy_opt[](#_CPPv4N13ble_set_phy_t7phy_optE "永久链接至目标")
    :   PHY options

struct ble_adv_param_t[](#_CPPv415ble_adv_param_t "永久链接至目标")
:   Public Members

    uint8_t own_addr_type[](#_CPPv4N15ble_adv_param_t13own_addr_typeE "永久链接至目标")
    :   Own address type: see enum [ble_own_addr_type](#group__bk__ble__api__v1__typedef_1gaaa7b5c55bc3b207c84e20eca8e0c7223 "#group__bk__ble__api__v1__typedef_1gaaa7b5c55bc3b207c84e20eca8e0c7223").

    uint8_t adv_type[](#_CPPv4N15ble_adv_param_t8adv_typeE "永久链接至目标")
    :   Advertising type (see enum [adv_type](#structble__adv__param__t_1a6e865fec2db0cc0eaee3e477918f1c38 "#structble__adv__param__t_1a6e865fec2db0cc0eaee3e477918f1c38"))

    uint8_t chnl_map[](#_CPPv4N15ble_adv_param_t8chnl_mapE "永久链接至目标")
    :   Bit field indicating the channel mapping (see enum [adv_chnl_map](#group__bk__ble__api__v1__typedef_1ga57c9e3ee8efb2e8c2fcc35e570f8679a "#group__bk__ble__api__v1__typedef_1ga57c9e3ee8efb2e8c2fcc35e570f8679a"))

    uint16_t adv_prop[](#_CPPv4N15ble_adv_param_t8adv_propE "永久链接至目标")
    :   Bit field value provided advertising properties (see enum [adv_prop_bf](#group__bk__ble__api__v1__typedef_1ga6b5140e1b8fe4043c83c62cbdfdd20c3 "#group__bk__ble__api__v1__typedef_1ga6b5140e1b8fe4043c83c62cbdfdd20c3"))

    uint32_t adv_intv_min[](#_CPPv4N15ble_adv_param_t12adv_intv_minE "永久链接至目标")
    :   Minimum advertising interval (in unit of 625us). Must be greater than or equal to 20ms.

    uint32_t adv_intv_max[](#_CPPv4N15ble_adv_param_t12adv_intv_maxE "永久链接至目标")
    :   Maximum advertising interval (in unit of 625us). Must be greater than or equal to 20ms.

    uint8_t prim_phy[](#_CPPv4N15ble_adv_param_t8prim_phyE "永久链接至目标")
    :   Indicate on which PHY primary advertising has to be performed (see enum [phy_type_le](#group__bk__ble__api__v1__typedef_1ga4acd0e053cbeead642d1317913613874 "#group__bk__ble__api__v1__typedef_1ga4acd0e053cbeead642d1317913613874")) Note that LE 2M PHY is not allowed and that legacy advertising only support LE 1M PHY

    uint8_t second_phy[](#_CPPv4N15ble_adv_param_t10second_phyE "永久链接至目标")
    :   Indicate on which PHY secondary advertising has to be performed (see enum [phy_type_le](#group__bk__ble__api__v1__typedef_1ga4acd0e053cbeead642d1317913613874 "#group__bk__ble__api__v1__typedef_1ga4acd0e053cbeead642d1317913613874"))

    uint8_t peer_addr_type[](#_CPPv4N15ble_adv_param_t14peer_addr_typeE "永久链接至目标")
    :   Peer address type: 0=public/1=private random, used for directed adv.

    [bd_addr_t](#_CPPv49bd_addr_t "bd_addr_t") peer_addr[](#_CPPv4N15ble_adv_param_t9peer_addrE "永久链接至目标")
    :   Peer address, used for directed adv.

struct ble_scan_param_t[](#_CPPv416ble_scan_param_t "永久链接至目标")
:   Public Members

    uint8_t own_addr_type[](#_CPPv4N16ble_scan_param_t13own_addr_typeE "永久链接至目标")
    :   Own address type: see enum [ble_own_addr_type](#group__bk__ble__api__v1__typedef_1gaaa7b5c55bc3b207c84e20eca8e0c7223 "#group__bk__ble__api__v1__typedef_1gaaa7b5c55bc3b207c84e20eca8e0c7223").

    uint8_t scan_phy[](#_CPPv4N16ble_scan_param_t8scan_phyE "永久链接至目标")
    :   on which the advertising packets should be received: LE 1M=1 / LE CODED=4 / LE 1M and LE CODED=5

    uint16_t scan_intv[](#_CPPv4N16ble_scan_param_t9scan_intvE "永久链接至目标")
    :   Scan interval (in unit of 625us). Must be greater than or equal to 2.5ms.

    uint16_t scan_wd[](#_CPPv4N16ble_scan_param_t7scan_wdE "永久链接至目标")
    :   Scan window (in unit of 625us). Must be greater than or equal to 2.5ms.

    uint8_t scan_type[](#_CPPv4N16ble_scan_param_t9scan_typeE "永久链接至目标")
    :   Scan type: see enum [ble_scan_type](#group__bk__ble__api__v1__typedef_1ga364631dfaf59ba0e1df8a02a43fa63d6 "#group__bk__ble__api__v1__typedef_1ga364631dfaf59ba0e1df8a02a43fa63d6").

    uint8_t scan_filter[](#_CPPv4N16ble_scan_param_t11scan_filterE "永久链接至目标")
    :   Scan type: see enum [ble_scan_filter_policy](#group__bk__ble__api__v1__typedef_1ga6bbb5b4b01f2f6a60164943eb569795e "#group__bk__ble__api__v1__typedef_1ga6bbb5b4b01f2f6a60164943eb569795e").

struct ble_conn_param_t[](#_CPPv416ble_conn_param_t "永久链接至目标")
:   Public Members

    uint16_t intv_min[](#_CPPv4N16ble_conn_param_t8intv_minE "永久链接至目标")
    :   Connection interval minimum (in unit of 1.25ms). Must be greater than or equal to 7.5ms.

    uint16_t intv_max[](#_CPPv4N16ble_conn_param_t8intv_maxE "永久链接至目标")
    :   Connection interval maximum (in unit of 1.25ms). Must be greater than or equal to 7.5ms.

    uint16_t con_latency[](#_CPPv4N16ble_conn_param_t11con_latencyE "永久链接至目标")
    :   Connection latency. The range is 0x0000 to 0x01F3.

    uint16_t sup_to[](#_CPPv4N16ble_conn_param_t6sup_toE "永久链接至目标")
    :   Link supervision timeout(in unit of 10ms). Must be greater than or equal to 100ms.

    uint8_t init_phys[](#_CPPv4N16ble_conn_param_t9init_physE "永久链接至目标")
    :   on which the advertising packets should be received on the primary advertising physical channel (see enum [phy_type_le](#group__bk__ble__api__v1__typedef_1ga4acd0e053cbeead642d1317913613874 "#group__bk__ble__api__v1__typedef_1ga4acd0e053cbeead642d1317913613874"))

    uint8_t conn_idx[](#_CPPv4N16ble_conn_param_t8conn_idxE "永久链接至目标")
    :   The index of connection.

struct ble_periodic_param_t[](#_CPPv420ble_periodic_param_t "永久链接至目标")
:   Public Members

    uint8_t report_disable[](#_CPPv4N20ble_periodic_param_t14report_disableE "永久链接至目标")
    :   1 to disable periodic advertising report, 0 to enable them by default

    uint8_t adv_sid[](#_CPPv4N20ble_periodic_param_t7adv_sidE "永久链接至目标")
    :   adv sid of advertiser(0x00 to 0x0F)

    [bd_addr_t](#_CPPv49bd_addr_t "bd_addr_t") adv_addr[](#_CPPv4N20ble_periodic_param_t8adv_addrE "永久链接至目标")
    :   Address of advertiser with which synchronization has to be established (used only if use_pal is false)

    uint16_t skip[](#_CPPv4N20ble_periodic_param_t4skipE "永久链接至目标")
    :   Number of periodic advertising that can be skipped after a successful receive. Maximum authorized value is 499

    uint16_t sync_to[](#_CPPv4N20ble_periodic_param_t7sync_toE "永久链接至目标")
    :   Synchronization timeout for the periodic advertising (in unit of 10ms between 100ms and 163.84s)

    uint8_t cte_type[](#_CPPv4N20ble_periodic_param_t8cte_typeE "永久链接至目标")
    :   Type of Constant Tone Extension device should sync on (see enum [ble_sync_cte_type](#group__bk__ble__api__v1__typedef_1ga7249d9eb7c2b2f4a4f56b4c241e6db5f "#group__bk__ble__api__v1__typedef_1ga7249d9eb7c2b2f4a4f56b4c241e6db5f")).

struct ble_conn_update_para_ind_t[](#_CPPv426ble_conn_update_para_ind_t "永久链接至目标")
:   Public Members

    uint8_t conn_idx[](#_CPPv4N26ble_conn_update_para_ind_t8conn_idxE "永久链接至目标")
    :   0:is not agree,1:is agree,0xFF;Let me think about it;other:is agree

    uint16_t ce_len_min[](#_CPPv4N26ble_conn_update_para_ind_t10ce_len_minE "永久链接至目标")
    :   Minimum Connection Event Duration.

    uint16_t ce_len_max[](#_CPPv4N26ble_conn_update_para_ind_t10ce_len_maxE "永久链接至目标")
    :   Maximum Connection Event Duration.

    uint16_t intv_min[](#_CPPv4N26ble_conn_update_para_ind_t8intv_minE "永久链接至目标")
    :   Connection interval minimum.

    uint16_t intv_max[](#_CPPv4N26ble_conn_update_para_ind_t8intv_maxE "永久链接至目标")
    :   Connection interval maximum.

    uint16_t latency[](#_CPPv4N26ble_conn_update_para_ind_t7latencyE "永久链接至目标")
    :   Latency.

    uint16_t time_out[](#_CPPv4N26ble_conn_update_para_ind_t8time_outE "永久链接至目标")
    :   Supervision timeout.

struct mst_comm_updata_para[](#_CPPv420mst_comm_updata_para "永久链接至目标")
:   Public Members

    uint8_t is_agree[](#_CPPv4N20mst_comm_updata_para8is_agreeE "永久链接至目标")
    :   Status of the request.

    uint16_t ce_len_min[](#_CPPv4N20mst_comm_updata_para10ce_len_minE "永久链接至目标")
    :   Minimum Connection Event Duration.

        0:is not agree,1:is agree,0xFF;Let me think about it;other:is agree

    uint16_t ce_len_max[](#_CPPv4N20mst_comm_updata_para10ce_len_maxE "永久链接至目标")
    :   Maximum Connection Event Duration.

    uint16_t intv_min[](#_CPPv4N20mst_comm_updata_para8intv_minE "永久链接至目标")
    :   Connection interval minimum.

    uint16_t intv_max[](#_CPPv4N20mst_comm_updata_para8intv_maxE "永久链接至目标")
    :   Connection interval maximum.

    uint16_t latency[](#_CPPv4N20mst_comm_updata_para7latencyE "永久链接至目标")
    :   Latency.

    uint16_t time_out[](#_CPPv4N20mst_comm_updata_para8time_outE "永久链接至目标")
    :   Supervision timeout.

struct ble_adv_stopped_ind_t[](#_CPPv421ble_adv_stopped_ind_t "永久链接至目标")
:   Public Members

    uint8_t adv_idx[](#_CPPv4N21ble_adv_stopped_ind_t7adv_idxE "永久链接至目标")
    :   The index of adv.

    uint8_t reason[](#_CPPv4N21ble_adv_stopped_ind_t6reasonE "永久链接至目标")
    :   the stopped reason,0:adv is stopped by user stop or link establishment;1:adv is stopped by timeout

struct ble_scan_stopped_ind_t[](#_CPPv422ble_scan_stopped_ind_t "永久链接至目标")
:   Public Members

    uint8_t scan_idx[](#_CPPv4N22ble_scan_stopped_ind_t8scan_idxE "永久链接至目标")
    :   The index of scan.

    uint8_t reason[](#_CPPv4N22ble_scan_stopped_ind_t6reasonE "永久链接至目标")
    :   the stopped reason,0:scan is stopped by user stop;1:scan is stopped by timeout

struct ble_read_rssi_rsp_t[](#_CPPv419ble_read_rssi_rsp_t "永久链接至目标")
:   BLE_5_READ_RSSI_CMPL_EVENT data.

    Public Members

    uint8_t conn_idx[](#_CPPv4N19ble_read_rssi_rsp_t8conn_idxE "永久链接至目标")
    :   The index of connection.

    int8_t rssi[](#_CPPv4N19ble_read_rssi_rsp_t4rssiE "永久链接至目标")
    :   RSSI value.

struct bk_ble_enc_keys_t[](#_CPPv417bk_ble_enc_keys_t "永久链接至目标")
:   BLE encryption keys.

    Public Members

    uint8_t ltk[16][](#_CPPv4N17bk_ble_enc_keys_t3ltkE "永久链接至目标")
    :   The long term key

    uint8_t rand[8][](#_CPPv4N17bk_ble_enc_keys_t4randE "永久链接至目标")
    :   The random number

    uint16_t ediv[](#_CPPv4N17bk_ble_enc_keys_t4edivE "永久链接至目标")
    :   The ediv value

    uint8_t key_size[](#_CPPv4N17bk_ble_enc_keys_t8key_sizeE "永久链接至目标")
    :   The key size(7~16) of the security link

struct bk_ble_irk_info_t[](#_CPPv417bk_ble_irk_info_t "永久链接至目标")
:   BLE irk info.

    Public Members

    uint8_t irk[16][](#_CPPv4N17bk_ble_irk_info_t3irkE "永久链接至目标")
    :   The irk value

    uint8_t addr_type[](#_CPPv4N17bk_ble_irk_info_t9addr_typeE "永久链接至目标")
    :   The address type

    uint8_t id_addr[6][](#_CPPv4N17bk_ble_irk_info_t7id_addrE "永久链接至目标")
    :   The Identity address

struct bk_ble_key_t[](#_CPPv412bk_ble_key_t "永久链接至目标")
:   Public Members

    uint8_t peer_addr_type[](#_CPPv4N12bk_ble_key_t14peer_addr_typeE "永久链接至目标")
    :   Peer address type.

    uint8_t peer_addr[6][](#_CPPv4N12bk_ble_key_t9peer_addrE "永久链接至目标")
    :   Peer address.

    uint8_t auth[](#_CPPv4N12bk_ble_key_t4authE "永久链接至目标")
    :   Authentication level.

    [bk_ble_enc_keys_t](#_CPPv417bk_ble_enc_keys_t "bk_ble_enc_keys_t") penc[](#_CPPv4N12bk_ble_key_t4pencE "永久链接至目标")
    :   received peer encryption key

    [bk_ble_enc_keys_t](#_CPPv417bk_ble_enc_keys_t "bk_ble_enc_keys_t") lenc[](#_CPPv4N12bk_ble_key_t4lencE "永久链接至目标")
    :   local encryption key

    [bk_ble_irk_info_t](#_CPPv417bk_ble_irk_info_t "bk_ble_irk_info_t") pirk[](#_CPPv4N12bk_ble_key_t4pirkE "永久链接至目标")
    :   peer Identity Resolving Key information

struct bk_ble_bond_info_req_t[](#_CPPv422bk_ble_bond_info_req_t "永久链接至目标")
:   Public Members

    uint8_t key_found[](#_CPPv4N22bk_ble_bond_info_req_t9key_foundE "永久链接至目标")
    :   check whether key is found

struct bk_ble_gatt_cmp_evt_t[](#_CPPv421bk_ble_gatt_cmp_evt_t "永久链接至目标")
:   Public Members

    uint8_t operation[](#_CPPv4N21bk_ble_gatt_cmp_evt_t9operationE "永久链接至目标")
    :   GATT request type.

    uint8_t status[](#_CPPv4N21bk_ble_gatt_cmp_evt_t6statusE "永久链接至目标")
    :   Status of the request.

    uint16_t prf_id[](#_CPPv4N21bk_ble_gatt_cmp_evt_t6prf_idE "永久链接至目标")
    :   service id

    uint16_t att_id[](#_CPPv4N21bk_ble_gatt_cmp_evt_t6att_idE "永久链接至目标")
    :   attribute id

    uint8_t conn_idx[](#_CPPv4N21bk_ble_gatt_cmp_evt_t8conn_idxE "永久链接至目标")
    :   connection index

struct nsp24g_access_addr[](#_CPPv418nsp24g_access_addr "永久链接至目标")
:   used for CONFIG_NSP24G

    Public Members

    uint8_t addr[4][](#_CPPv4N18nsp24g_access_addr4addrE "永久链接至目标")
    :   4-byte array access address

struct nsp24g_crc_init[](#_CPPv415nsp24g_crc_init "永久链接至目标")
:   Public Members

    uint8_t crc[3][](#_CPPv4N15nsp24g_crc_init3crcE "永久链接至目标")
    :   3-byte array CRC initial value

struct bk_nsp24g_param_t[](#_CPPv417bk_nsp24g_param_t "永久链接至目标")
:   Public Members

    struct [nsp24g_access_addr](#_CPPv418nsp24g_access_addr "nsp24g_access_addr") aa[](#_CPPv4N17bk_nsp24g_param_t2aaE "永久链接至目标")
    :   Access address.

    struct [nsp24g_crc_init](#_CPPv415nsp24g_crc_init "nsp24g_crc_init") crcinit[](#_CPPv4N17bk_nsp24g_param_t7crcinitE "永久链接至目标")
    :   CRC init.

struct nsp24g_packet_t[](#_CPPv415nsp24g_packet_t "永久链接至目标")
:   Public Members

    [nsp24g_channel_t](#_CPPv416nsp24g_channel_t "nsp24g_channel_t") channel[](#_CPPv4N15nsp24g_packet_t7channelE "永久链接至目标")
    :   nsp24g channel

    uint8_t data[36][](#_CPPv4N15nsp24g_packet_t4dataE "永久链接至目标")
    :   nsp24g packet

    uint8_t size[](#_CPPv4N15nsp24g_packet_t4sizeE "永久链接至目标")
    :   nsp24g packet length


### Macros[](#macros "永久链接至标题")

BK_ERR_BLE_SUCCESS[](#c.BK_ERR_BLE_SUCCESS "永久链接至目标")
:   success

BK_ERR_BLE_FAIL[](#c.BK_ERR_BLE_FAIL "永久链接至目标")
:   fail

BK_ERR_BLE_NO_MEM[](#c.BK_ERR_BLE_NO_MEM "永久链接至目标")
:   no mem

BK_ERR_BLE_PROFILE[](#c.BK_ERR_BLE_PROFILE "永久链接至目标")
:   profile err

BK_ERR_BLE_CREATE_DB[](#c.BK_ERR_BLE_CREATE_DB "永久链接至目标")
:   bk_ble_create_db err

BK_ERR_BLE_CMD_NOT_SUPPORT[](#c.BK_ERR_BLE_CMD_NOT_SUPPORT "永久链接至目标")
:   unknow cmd err

BK_ERR_BLE_UNKNOW_IDX[](#c.BK_ERR_BLE_UNKNOW_IDX "永久链接至目标")
:   index err, suchas conn_ind

BK_ERR_BLE_BLE_STATUS[](#c.BK_ERR_BLE_BLE_STATUS "永久链接至目标")
:   ble status not match

BK_ERR_BLE_ADV_DATA[](#c.BK_ERR_BLE_ADV_DATA "永久链接至目标")
:   adv data err, such as too long

BK_ERR_BLE_CMD_RUN[](#c.BK_ERR_BLE_CMD_RUN "永久链接至目标")
:   cmd run err

BK_ERR_BLE_INIT_CREATE[](#c.BK_ERR_BLE_INIT_CREATE "永久链接至目标")
:   create init err, such as bk_ble_create_init

BK_ERR_BLE_INIT_STATE[](#c.BK_ERR_BLE_INIT_STATE "永久链接至目标")
:   current init status not match

BK_ERR_BLE_ATTC_WRITE[](#c.BK_ERR_BLE_ATTC_WRITE "永久链接至目标")
:   att write err

BK_ERR_BLE_ATTC_WRITE_UNREGISTER[](#c.BK_ERR_BLE_ATTC_WRITE_UNREGISTER "永久链接至目标")
:   att handle is not regist

BK_BLE_MAX_ADV_DATA_LEN[](#c.BK_BLE_MAX_ADV_DATA_LEN "永久链接至目标")
:   max ble adv data len

BK_BLE_GAP_BD_ADDR_LEN[](#c.BK_BLE_GAP_BD_ADDR_LEN "永久链接至目标")
:   BD address length.

BK_BLE_APP_DEVICE_NAME_MAX_LEN[](#c.BK_BLE_APP_DEVICE_NAME_MAX_LEN "永久链接至目标")
:   Maximal length of the Device Name value.

BK_BLE_PERM_SET(access, right)[](#c.BK_BLE_PERM_SET "永久链接至目标")
:   for [ble_attm_desc_t](#structble__attm__desc__t "#structble__attm__desc__t"), build database perm,

BK_BLE_PERM_GET(perm, access)[](#c.BK_BLE_PERM_GET "永久链接至目标")


### Type Definitions[](#type-definitions "永久链接至标题")

typedef [bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") ble_err_t[](#_CPPv49ble_err_t "永久链接至目标")
:   ble api return enum

typedef void (*app_sdp_callback)(unsigned char conidx, uint16_t chars_val_hdl, unsigned char uuid_len, unsigned char *uuid)[](#_CPPv416app_sdp_callback "永久链接至目标")

typedef void (*app_sdp_charac_callback)([CHAR_TYPE](#_CPPv49CHAR_TYPE "CHAR_TYPE") type, uint8 conidx, uint16_t hdl, uint16_t len, uint8 *data)[](#_CPPv423app_sdp_charac_callback "永久链接至目标")

typedef void (*app_sdp_comm_callback)([MASTER_COMMON_TYPE](#_CPPv418MASTER_COMMON_TYPE "MASTER_COMMON_TYPE") type, uint8 conidx, void *param)[](#_CPPv421app_sdp_comm_callback "永久链接至目标")

typedef void (*ble_nsp24g_rx_cb_t)([nsp24g_packet_t](#_CPPv415nsp24g_packet_t "nsp24g_packet_t") *in_rx_data, [nsp24g_packet_t](#_CPPv415nsp24g_packet_t "nsp24g_packet_t") *out_ack_frame)[](#_CPPv418ble_nsp24g_rx_cb_t "永久链接至目标")
:   for nsp24g rx callback.

    备注

    The callback function is within the interrupt handling function.

    Param -
    :   in_rx_data: Input Parameters


        - out_ack_frame: Output Parameters

typedef void (*ble_nsp24g_ack_cb_t)(uint8_t ack_state, [nsp24g_packet_t](#_CPPv415nsp24g_packet_t "nsp24g_packet_t") *ack_frame)[](#_CPPv419ble_nsp24g_ack_cb_t "永久链接至目标")
:   for nsp24g Receive ack callback.

    备注

    The callback function is within the interrupt handling function.

    Param -
    :   ack_state: 1 is receive ack success,0 is timeout


        - ack_frame: if ack_state is 1,ack_frame is valid poniter

typedef void (*ble_cmd_cb_t)([ble_cmd_t](#_CPPv49ble_cmd_t "ble_cmd_t") cmd, [ble_cmd_param_t](#_CPPv415ble_cmd_param_t "ble_cmd_param_t") *param)[](#_CPPv412ble_cmd_cb_t "永久链接至目标")
:   for sync ble api call return

    most ble api have ble_cmd_cb_t param, you must wait is callback.

    Param -
    :   cmd: cmd id.


        - param: param

typedef void (*ble_notice_cb_t)([ble_notice_t](#_CPPv412ble_notice_t "ble_notice_t") notice, void *param)[](#_CPPv415ble_notice_cb_t "永久链接至目标")
:   for async ble api event.

    ble event report.

    Param -
    :   notice: event id.


        - param: param

typedef [ble_err_t](#_CPPv49ble_err_t "ble_err_t") (*ble_hci_to_host_cb)(uint8_t *buf, uint16_t len)[](#_CPPv418ble_hci_to_host_cb "永久链接至目标")
:   for hci callback.

    stack report evt, acl to upper

    Param -
    :   buf: payload


        - len: buf’s len

    Return
    :   - BK_ERR_BLE_SUCCESS: succeed


### Enumerations[](#enumerations "永久链接至标题")

enum BK_BLE_CONTROLLER_STACK_TYPE[](#_CPPv428BK_BLE_CONTROLLER_STACK_TYPE "永久链接至目标")
:   *Values:*

    enumerator BK_BLE_CONTROLLER_STACK_TYPE_BLE_4[](#_CPPv4N28BK_BLE_CONTROLLER_STACK_TYPE34BK_BLE_CONTROLLER_STACK_TYPE_BLE_4E "永久链接至目标")

    enumerator BK_BLE_CONTROLLER_STACK_TYPE_BLE_5_X[](#_CPPv4N28BK_BLE_CONTROLLER_STACK_TYPE36BK_BLE_CONTROLLER_STACK_TYPE_BLE_5_XE "永久链接至目标")

    enumerator BK_BLE_CONTROLLER_STACK_TYPE_BTDM_5_2[](#_CPPv4N28BK_BLE_CONTROLLER_STACK_TYPE37BK_BLE_CONTROLLER_STACK_TYPE_BTDM_5_2E "永久链接至目标")

enum BK_BLE_HOST_STACK_TYPE[](#_CPPv422BK_BLE_HOST_STACK_TYPE "永久链接至目标")
:   *Values:*

    enumerator BK_BLE_HOST_STACK_TYPE_RW_4[](#_CPPv4N22BK_BLE_HOST_STACK_TYPE27BK_BLE_HOST_STACK_TYPE_RW_4E "永久链接至目标")

    enumerator BK_BLE_HOST_STACK_TYPE_RW_5_X[](#_CPPv4N22BK_BLE_HOST_STACK_TYPE29BK_BLE_HOST_STACK_TYPE_RW_5_XE "永久链接至目标")

    enumerator BK_BLE_HOST_STACK_TYPE_RW_5_2[](#_CPPv4N22BK_BLE_HOST_STACK_TYPE29BK_BLE_HOST_STACK_TYPE_RW_5_2E "永久链接至目标")

    enumerator BK_BLE_HOST_STACK_TYPE_ETHERMIND[](#_CPPv4N22BK_BLE_HOST_STACK_TYPE32BK_BLE_HOST_STACK_TYPE_ETHERMINDE "永久链接至目标")

enum BK_BLE_HCI_TYPE[](#_CPPv415BK_BLE_HCI_TYPE "永久链接至目标")
:   hci type enum


    *Values:*

    enumerator BK_BLE_HCI_TYPE_CMD[](#_CPPv4N15BK_BLE_HCI_TYPE19BK_BLE_HCI_TYPE_CMDE "永久链接至目标")

    enumerator BK_BLE_HCI_TYPE_ACL[](#_CPPv4N15BK_BLE_HCI_TYPE19BK_BLE_HCI_TYPE_ACLE "永久链接至目标")

    enumerator BK_BLE_HCI_TYPE_SCO[](#_CPPv4N15BK_BLE_HCI_TYPE19BK_BLE_HCI_TYPE_SCOE "永久链接至目标")

    enumerator BK_BLE_HCI_TYPE_EVT[](#_CPPv4N15BK_BLE_HCI_TYPE19BK_BLE_HCI_TYPE_EVTE "永久链接至目标")

enum ble_actv_state[](#_CPPv414ble_actv_state "永久链接至目标")
:   ble actv type


    *Values:*

    enumerator BLE_ACTV_IDLE[](#_CPPv4N14ble_actv_state13BLE_ACTV_IDLEE "永久链接至目标")

    enumerator BLE_ACTV_ADV_CREATED[](#_CPPv4N14ble_actv_state20BLE_ACTV_ADV_CREATEDE "永久链接至目标")

    enumerator BLE_ACTV_ADV_STARTED[](#_CPPv4N14ble_actv_state20BLE_ACTV_ADV_STARTEDE "永久链接至目标")

    enumerator BLE_ACTV_SCAN_CREATED[](#_CPPv4N14ble_actv_state21BLE_ACTV_SCAN_CREATEDE "永久链接至目标")

    enumerator BLE_ACTV_SCAN_STARTED[](#_CPPv4N14ble_actv_state21BLE_ACTV_SCAN_STARTEDE "永久链接至目标")

    enumerator BLE_ACTV_INIT_CREATED[](#_CPPv4N14ble_actv_state21BLE_ACTV_INIT_CREATEDE "永久链接至目标")

    enumerator BLE_ACTV_PER_SYNC_CREATED[](#_CPPv4N14ble_actv_state25BLE_ACTV_PER_SYNC_CREATEDE "永久链接至目标")

    enumerator BLE_ACTV_PER_SYNC_STARTED[](#_CPPv4N14ble_actv_state25BLE_ACTV_PER_SYNC_STARTEDE "永久链接至目标")

enum bk_ble_perm_mask[](#_CPPv416bk_ble_perm_mask "永久链接至目标")
:   normal perm, for BK_BLE_PERM_SET

    | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 - 6 | 5 - 4 | 3 - 2 | 1 - 0 |
    | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
    | EXT | WS | I | N | WR | WC | RD | B | NP | IP | WP | RP |


    **Attention**
    :   you cant use this direct, use [BK_BLE_PERM_SET(RD, ENABLE)](#group__bk__ble__api__v1_1ga12a5ba4c80b8f6fdc20573c242bd0b5b "#group__bk__ble__api__v1_1ga12a5ba4c80b8f6fdc20573c242bd0b5b") instead

    Bit [0-1] : Read Permission (0 = NO_AUTH, 1 = UNAUTH, 2 = AUTH, 3 = SEC_CON)

    Bit [2-3] : Write Permission (0 = NO_AUTH, 1 = UNAUTH, 2 = AUTH, 3 = SEC_CON)

    Bit [4-5] : Indication Permission (0 = NO_AUTH, 1 = UNAUTH, 2 = AUTH, 3 = SEC_CON)

    Bit [6-7] : Notification Permission (0 = NO_AUTH, 1 = UNAUTH, 2 = AUTH, 3 = SEC_CON)

    Bit [8] : Broadcast permission

    Bit [9] : Read Command accepted

    Bit [10] : Write Command accepted

    Bit [11] : Write Request accepted

    Bit [12] : Send Notification

    Bit [13] : Send Indication

    Bit [14] : Write Signed accepted

    Bit [15] : Extended properties present


    *Values:*

    enumerator BK_BLE_RP_MASK[](#_CPPv4N16bk_ble_perm_mask14BK_BLE_RP_MASKE "永久链接至目标")
    :   Read Permission Mask.

    enumerator BK_BLE_RP_POS[](#_CPPv4N16bk_ble_perm_mask13BK_BLE_RP_POSE "永久链接至目标")

    enumerator BK_BLE_WP_MASK[](#_CPPv4N16bk_ble_perm_mask14BK_BLE_WP_MASKE "永久链接至目标")
    :   Write Permission Mask.

    enumerator BK_BLE_WP_POS[](#_CPPv4N16bk_ble_perm_mask13BK_BLE_WP_POSE "永久链接至目标")

    enumerator BK_BLE_IP_MASK[](#_CPPv4N16bk_ble_perm_mask14BK_BLE_IP_MASKE "永久链接至目标")
    :   Indication Access Mask.

    enumerator BK_BLE_IP_POS[](#_CPPv4N16bk_ble_perm_mask13BK_BLE_IP_POSE "永久链接至目标")

    enumerator BK_BLE_NP_MASK[](#_CPPv4N16bk_ble_perm_mask14BK_BLE_NP_MASKE "永久链接至目标")
    :   Notification Access Mask.

    enumerator BK_BLE_NP_POS[](#_CPPv4N16bk_ble_perm_mask13BK_BLE_NP_POSE "永久链接至目标")

    enumerator BK_BLE_BROADCAST_MASK[](#_CPPv4N16bk_ble_perm_mask21BK_BLE_BROADCAST_MASKE "永久链接至目标")
    :   Broadcast descriptor present.

    enumerator BK_BLE_BROADCAST_POS[](#_CPPv4N16bk_ble_perm_mask20BK_BLE_BROADCAST_POSE "永久链接至目标")

    enumerator BK_BLE_RD_MASK[](#_CPPv4N16bk_ble_perm_mask14BK_BLE_RD_MASKE "永久链接至目标")
    :   Read Access Mask.

    enumerator BK_BLE_RD_POS[](#_CPPv4N16bk_ble_perm_mask13BK_BLE_RD_POSE "永久链接至目标")

    enumerator BK_BLE_WRITE_COMMAND_MASK[](#_CPPv4N16bk_ble_perm_mask25BK_BLE_WRITE_COMMAND_MASKE "永久链接至目标")
    :   Write Command Enabled attribute Mask.

    enumerator BK_BLE_WRITE_COMMAND_POS[](#_CPPv4N16bk_ble_perm_mask24BK_BLE_WRITE_COMMAND_POSE "永久链接至目标")

    enumerator BK_BLE_WRITE_REQ_MASK[](#_CPPv4N16bk_ble_perm_mask21BK_BLE_WRITE_REQ_MASKE "永久链接至目标")
    :   Write Request Enabled attribute Mask.

    enumerator BK_BLE_WRITE_REQ_POS[](#_CPPv4N16bk_ble_perm_mask20BK_BLE_WRITE_REQ_POSE "永久链接至目标")

    enumerator BK_BLE_NTF_MASK[](#_CPPv4N16bk_ble_perm_mask15BK_BLE_NTF_MASKE "永久链接至目标")
    :   Notification Access Mask.

    enumerator BK_BLE_NTF_POS[](#_CPPv4N16bk_ble_perm_mask14BK_BLE_NTF_POSE "永久链接至目标")

    enumerator BK_BLE_IND_MASK[](#_CPPv4N16bk_ble_perm_mask15BK_BLE_IND_MASKE "永久链接至目标")
    :   Indication Access Mask.

    enumerator BK_BLE_IND_POS[](#_CPPv4N16bk_ble_perm_mask14BK_BLE_IND_POSE "永久链接至目标")

    enumerator BK_BLE_WRITE_SIGNED_MASK[](#_CPPv4N16bk_ble_perm_mask24BK_BLE_WRITE_SIGNED_MASKE "永久链接至目标")
    :   Write Signed Enabled attribute Mask.

    enumerator BK_BLE_WRITE_SIGNED_POS[](#_CPPv4N16bk_ble_perm_mask23BK_BLE_WRITE_SIGNED_POSE "永久链接至目标")

    enumerator BK_BLE_EXT_MASK[](#_CPPv4N16bk_ble_perm_mask15BK_BLE_EXT_MASKE "永久链接至目标")
    :   Extended properties descriptor present.

    enumerator BK_BLE_EXT_POS[](#_CPPv4N16bk_ble_perm_mask14BK_BLE_EXT_POSE "永久链接至目标")

enum bk_ble_ext_perm_mask[](#_CPPv420bk_ble_ext_perm_mask "永久链接至目标")
:   Attribute Extended permissions, for BK_BLE_PERM_SET.

    Extended Value permission bit field


    **Attention**
    :   you cant use this direct, use [BK_BLE_PERM_SET(EKS, ENABLE)](#group__bk__ble__api__v1_1ga12a5ba4c80b8f6fdc20573c242bd0b5b "#group__bk__ble__api__v1_1ga12a5ba4c80b8f6fdc20573c242bd0b5b") instead

    | 15 | 14 - 13 | 12 | 11 | 10 - 0 |
    | --- | --- | --- | --- | --- |
    | RI | UUID_LEN | EKS | INCL | Reserved |

    Bit [0-10] : Reserved

    Bit [11] : Attribute Value is included(Value present in Database)

    Bit [12] : Encryption key Size must be 16 bytes

    Bit [13-14]: UUID Length (0 = 16 bits, 1 = 32 bits, 2 = 128 bits, 3 = RFU)

    Bit [15] : Trigger Read Indication (0 = Value present in Database, 1 = Value not present in Database)


    *Values:*

    enumerator BK_BLE_VALUE_INCL_MASK[](#_CPPv4N20bk_ble_ext_perm_mask22BK_BLE_VALUE_INCL_MASKE "永久链接至目标")
    :   Attribute Value is included.

    enumerator BK_BLE_VALUE_INCL_POS[](#_CPPv4N20bk_ble_ext_perm_mask21BK_BLE_VALUE_INCL_POSE "永久链接至目标")

    enumerator BK_BLE_EKS_MASK[](#_CPPv4N20bk_ble_ext_perm_mask15BK_BLE_EKS_MASKE "永久链接至目标")
    :   Check Encryption key size Mask.

    enumerator BK_BLE_EKS_POS[](#_CPPv4N20bk_ble_ext_perm_mask14BK_BLE_EKS_POSE "永久链接至目标")

    enumerator BK_BLE_UUID_LEN_MASK[](#_CPPv4N20bk_ble_ext_perm_mask20BK_BLE_UUID_LEN_MASKE "永久链接至目标")
    :   UUID Length.

    enumerator BK_BLE_UUID_LEN_POS[](#_CPPv4N20bk_ble_ext_perm_mask19BK_BLE_UUID_LEN_POSE "永久链接至目标")

    enumerator BK_BLE_RI_MASK[](#_CPPv4N20bk_ble_ext_perm_mask14BK_BLE_RI_MASKE "永久链接至目标")
    :   Read trigger Indication.

    enumerator BK_BLE_RI_POS[](#_CPPv4N20bk_ble_ext_perm_mask13BK_BLE_RI_POSE "永久链接至目标")

enum bk_ble_svc_perm_mask[](#_CPPv420bk_ble_svc_perm_mask "永久链接至目标")
:   Service permissions, for BK_BLE_PERM_SET.

    | 7 | 6 - 5 | 4 | 3 - 2 | 1 | 0 |
    | --- | --- | --- | --- | --- | --- |
    | SEC | UUID_LEN | DIS | AUTH | EKS | MI |


    **Attention**
    :   you cant use this direct, use [BK_BLE_PERM_SET(SVC_UUID_LEN, UUID_16)](#group__bk__ble__api__v1_1ga12a5ba4c80b8f6fdc20573c242bd0b5b "#group__bk__ble__api__v1_1ga12a5ba4c80b8f6fdc20573c242bd0b5b") instead

    Bit [0] : Task that manage service is multi-instantiated (Connection index is conveyed)

    Bit [1] : Encryption key Size must be 16 bytes

    Bit [2-3]: Service Permission (0 = NO_AUTH, 1 = UNAUTH, 2 = AUTH, 3 = Secure Connect)

    Bit [4] : Disable the service

    Bit [5-6]: UUID Length (0 = 16 bits, 1 = 32 bits, 2 = 128 bits, 3 = RFU)

    Bit [7] : Secondary Service (0 = Primary Service, 1 = Secondary Service)


    *Values:*

    enumerator BK_BLE_SVC_MI_MASK[](#_CPPv4N20bk_ble_svc_perm_mask18BK_BLE_SVC_MI_MASKE "永久链接至目标")
    :   Task that manage service is multi-instantiated.

    enumerator BK_BLE_SVC_MI_POS[](#_CPPv4N20bk_ble_svc_perm_mask17BK_BLE_SVC_MI_POSE "永久链接至目标")

    enumerator BK_BLE_SVC_EKS_MASK[](#_CPPv4N20bk_ble_svc_perm_mask19BK_BLE_SVC_EKS_MASKE "永久链接至目标")
    :   Check Encryption key size for service Access.

    enumerator BK_BLE_SVC_EKS_POS[](#_CPPv4N20bk_ble_svc_perm_mask18BK_BLE_SVC_EKS_POSE "永久链接至目标")

    enumerator BK_BLE_SVC_AUTH_MASK[](#_CPPv4N20bk_ble_svc_perm_mask20BK_BLE_SVC_AUTH_MASKE "永久链接至目标")
    :   Service Permission authentication.

    enumerator BK_BLE_SVC_AUTH_POS[](#_CPPv4N20bk_ble_svc_perm_mask19BK_BLE_SVC_AUTH_POSE "永久链接至目标")

    enumerator BK_BLE_SVC_DIS_MASK[](#_CPPv4N20bk_ble_svc_perm_mask19BK_BLE_SVC_DIS_MASKE "永久链接至目标")
    :   Disable the service.

    enumerator BK_BLE_SVC_DIS_POS[](#_CPPv4N20bk_ble_svc_perm_mask18BK_BLE_SVC_DIS_POSE "永久链接至目标")

    enumerator BK_BLE_SVC_UUID_LEN_MASK[](#_CPPv4N20bk_ble_svc_perm_mask24BK_BLE_SVC_UUID_LEN_MASKE "永久链接至目标")
    :   Service UUID Length.

    enumerator BK_BLE_SVC_UUID_LEN_POS[](#_CPPv4N20bk_ble_svc_perm_mask23BK_BLE_SVC_UUID_LEN_POSE "永久链接至目标")

    enumerator BK_BLE_SVC_SECONDARY_MASK[](#_CPPv4N20bk_ble_svc_perm_mask25BK_BLE_SVC_SECONDARY_MASKE "永久链接至目标")
    :   Service type Secondary.

    enumerator BK_BLE_SVC_SECONDARY_POS[](#_CPPv4N20bk_ble_svc_perm_mask24BK_BLE_SVC_SECONDARY_POSE "永久链接至目标")

enum [anonymous][](#_CPPv4Ut1_0 "永久链接至目标")
:   *Values:*

    enumerator BK_BLE_PERM_RIGHT_DISABLE[](#_CPPv4NUt1_025BK_BLE_PERM_RIGHT_DISABLEE "永久链接至目标")
    :   Disable access.

    enumerator BK_BLE_PERM_RIGHT_ENABLE[](#_CPPv4NUt1_024BK_BLE_PERM_RIGHT_ENABLEE "永久链接至目标")
    :   Enable access.

enum [anonymous][](#_CPPv4Ut1_1 "永久链接至目标")
:   *Values:*

    enumerator BK_BLE_PERM_RIGHT_NO_AUTH[](#_CPPv4NUt1_125BK_BLE_PERM_RIGHT_NO_AUTHE "永久链接至目标")
    :   No Authentication.

    enumerator BK_BLE_PERM_RIGHT_UNAUTH[](#_CPPv4NUt1_124BK_BLE_PERM_RIGHT_UNAUTHE "永久链接至目标")
    :   Access Requires Unauthenticated link.

    enumerator BK_BLE_PERM_RIGHT_AUTH[](#_CPPv4NUt1_122BK_BLE_PERM_RIGHT_AUTHE "永久链接至目标")
    :   Access Requires Authenticated link.

    enumerator BK_BLE_PERM_RIGHT_SEC_CON[](#_CPPv4NUt1_125BK_BLE_PERM_RIGHT_SEC_CONE "永久链接至目标")
    :   Access Requires Secure Connection link.

enum [anonymous][](#_CPPv4Ut1_2 "永久链接至目标")
:   *Values:*

    enumerator BK_BLE_PERM_RIGHT_UUID_16[](#_CPPv4NUt1_225BK_BLE_PERM_RIGHT_UUID_16E "永久链接至目标")
    :   16 bits UUID

    enumerator BK_BLE_PERM_RIGHT_UUID_32[](#_CPPv4NUt1_225BK_BLE_PERM_RIGHT_UUID_32E "永久链接至目标")
    :   32 bits UUID

    enumerator BK_BLE_PERM_RIGHT_UUID_128[](#_CPPv4NUt1_226BK_BLE_PERM_RIGHT_UUID_128E "永久链接至目标")
    :   128 bits UUID

    enumerator BK_BLE_PERM_RIGHT_UUID_RFU[](#_CPPv4NUt1_226BK_BLE_PERM_RIGHT_UUID_RFUE "永久链接至目标")
    :   Invalid.

enum bk_ble_authorization_flag[](#_CPPv425bk_ble_authorization_flag "永久链接至目标")
:   *Values:*

    enumerator BK_GATT_VALUE_READ_AUTHOR_FLAG[](#_CPPv4N25bk_ble_authorization_flag30BK_GATT_VALUE_READ_AUTHOR_FLAGE "永久链接至目标")
    :   read needs to be authorized by user

    enumerator BK_GATT_VALUE_WRITE_AUTHOR_FLAG[](#_CPPv4N25bk_ble_authorization_flag31BK_GATT_VALUE_WRITE_AUTHOR_FLAGE "永久链接至目标")
    :   write needs to be authorized by user

enum ble_cmd_t[](#_CPPv49ble_cmd_t "永久链接至目标")
:   *Values:*

    enumerator BLE_CMD_NONE[](#_CPPv4N9ble_cmd_t12BLE_CMD_NONEE "永久链接至目标")

    enumerator BLE_CREATE_ADV[](#_CPPv4N9ble_cmd_t14BLE_CREATE_ADVE "永久链接至目标")
    :   ADV_CMD:FOR BLE 5.1.

    enumerator BLE_SET_ADV_DATA[](#_CPPv4N9ble_cmd_t16BLE_SET_ADV_DATAE "永久链接至目标")

    enumerator BLE_SET_RSP_DATA[](#_CPPv4N9ble_cmd_t16BLE_SET_RSP_DATAE "永久链接至目标")

    enumerator BLE_START_ADV[](#_CPPv4N9ble_cmd_t13BLE_START_ADVE "永久链接至目标")

    enumerator BLE_STOP_ADV[](#_CPPv4N9ble_cmd_t12BLE_STOP_ADVE "永久链接至目标")

    enumerator BLE_DELETE_ADV[](#_CPPv4N9ble_cmd_t14BLE_DELETE_ADVE "永久链接至目标")

    enumerator BLE_INIT_ADV[](#_CPPv4N9ble_cmd_t12BLE_INIT_ADVE "永久链接至目标")
    :   ADV_CMD:FOR BLE 4.2.

    enumerator BLE_DEINIT_ADV[](#_CPPv4N9ble_cmd_t14BLE_DEINIT_ADVE "永久链接至目标")

    enumerator BLE_CREATE_SCAN[](#_CPPv4N9ble_cmd_t15BLE_CREATE_SCANE "永久链接至目标")
    :   SCAN_CMD:FOR BLE 5.1.

    enumerator BLE_START_SCAN[](#_CPPv4N9ble_cmd_t14BLE_START_SCANE "永久链接至目标")

    enumerator BLE_STOP_SCAN[](#_CPPv4N9ble_cmd_t13BLE_STOP_SCANE "永久链接至目标")

    enumerator BLE_DELETE_SCAN[](#_CPPv4N9ble_cmd_t15BLE_DELETE_SCANE "永久链接至目标")

    enumerator BLE_INIT_SCAN[](#_CPPv4N9ble_cmd_t13BLE_INIT_SCANE "永久链接至目标")
    :   SCAN_CMD:FOR BLE 4.2.

    enumerator BLE_DEINIT_SCAN[](#_CPPv4N9ble_cmd_t15BLE_DEINIT_SCANE "永久链接至目标")

    enumerator BLE_CONN_UPDATE_MTU[](#_CPPv4N9ble_cmd_t19BLE_CONN_UPDATE_MTUE "永久链接至目标")
    :   conn

    enumerator BLE_CONN_UPDATE_PARAM[](#_CPPv4N9ble_cmd_t21BLE_CONN_UPDATE_PARAME "永久链接至目标")

    enumerator BLE_CONN_DIS_CONN[](#_CPPv4N9ble_cmd_t17BLE_CONN_DIS_CONNE "永久链接至目标")

    enumerator BLE_CONN_READ_PHY[](#_CPPv4N9ble_cmd_t17BLE_CONN_READ_PHYE "永久链接至目标")

    enumerator BLE_CONN_SET_PHY[](#_CPPv4N9ble_cmd_t16BLE_CONN_SET_PHYE "永久链接至目标")

    enumerator BLE_CONN_ENCRYPT[](#_CPPv4N9ble_cmd_t16BLE_CONN_ENCRYPTE "永久链接至目标")

    enumerator BLE_INIT_CREATE[](#_CPPv4N9ble_cmd_t15BLE_INIT_CREATEE "永久链接至目标")
    :   init

    enumerator BLE_INIT_START_CONN[](#_CPPv4N9ble_cmd_t19BLE_INIT_START_CONNE "永久链接至目标")

    enumerator BLE_INIT_STOP_CONN[](#_CPPv4N9ble_cmd_t18BLE_INIT_STOP_CONNE "永久链接至目标")

    enumerator BLE_INIT_DIS_CONN[](#_CPPv4N9ble_cmd_t17BLE_INIT_DIS_CONNE "永久链接至目标")

    enumerator BLE_INIT_READ_CHAR[](#_CPPv4N9ble_cmd_t18BLE_INIT_READ_CHARE "永久链接至目标")

    enumerator BLE_INIT_WRITE_CHAR[](#_CPPv4N9ble_cmd_t19BLE_INIT_WRITE_CHARE "永久链接至目标")

    enumerator BLE_SET_MAX_MTU[](#_CPPv4N9ble_cmd_t15BLE_SET_MAX_MTUE "永久链接至目标")
    :   config

    enumerator BLE_CREATE_PERIODIC[](#_CPPv4N9ble_cmd_t19BLE_CREATE_PERIODICE "永久链接至目标")

    enumerator BLE_START_PERIODIC[](#_CPPv4N9ble_cmd_t18BLE_START_PERIODICE "永久链接至目标")

    enumerator BLE_STOP_PERIODIC[](#_CPPv4N9ble_cmd_t17BLE_STOP_PERIODICE "永久链接至目标")

    enumerator BLE_DELETE_PERIODIC[](#_CPPv4N9ble_cmd_t19BLE_DELETE_PERIODICE "永久链接至目标")

    enumerator BLE_SET_LOCAL_NAME[](#_CPPv4N9ble_cmd_t18BLE_SET_LOCAL_NAMEE "永久链接至目标")

    enumerator BLE_GET_LOCAL_NAME[](#_CPPv4N9ble_cmd_t18BLE_GET_LOCAL_NAMEE "永久链接至目标")

    enumerator BLE_READ_LOCAL_ADDR[](#_CPPv4N9ble_cmd_t19BLE_READ_LOCAL_ADDRE "永久链接至目标")

    enumerator BLE_SET_RANDOM_ADDR[](#_CPPv4N9ble_cmd_t19BLE_SET_RANDOM_ADDRE "永久链接至目标")

    enumerator BLE_SET_ADV_RANDOM_ADDR[](#_CPPv4N9ble_cmd_t23BLE_SET_ADV_RANDOM_ADDRE "永久链接至目标")

    enumerator BLE_ADD_WHITE_LIST[](#_CPPv4N9ble_cmd_t18BLE_ADD_WHITE_LISTE "永久链接至目标")

    enumerator BLE_RMV_WHITE_LIST[](#_CPPv4N9ble_cmd_t18BLE_RMV_WHITE_LISTE "永久链接至目标")

    enumerator BLE_CLE_WHITE_LIST[](#_CPPv4N9ble_cmd_t18BLE_CLE_WHITE_LISTE "永久链接至目标")

    enumerator BLE_CMD_MAX[](#_CPPv4N9ble_cmd_t11BLE_CMD_MAXE "永久链接至目标")

enum ble_notice_t[](#_CPPv412ble_notice_t "永久链接至目标")
:   *Values:*

    enumerator BLE_5_STACK_OK[](#_CPPv4N12ble_notice_t14BLE_5_STACK_OKE "永久链接至目标")
    :   ble stack init ok, param null.This event is deprecated,please do not use it.

    enumerator BLE_5_WRITE_EVENT[](#_CPPv4N12ble_notice_t17BLE_5_WRITE_EVENTE "永久链接至目标")
    :   peer write our, param [ble_write_req_t](#structble__write__req__t "#structble__write__req__t")

    enumerator BLE_5_READ_EVENT[](#_CPPv4N12ble_notice_t16BLE_5_READ_EVENTE "永久链接至目标")
    :   peer read our, param [ble_read_req_t](#structble__read__req__t "#structble__read__req__t")

    enumerator BLE_5_REPORT_ADV[](#_CPPv4N12ble_notice_t16BLE_5_REPORT_ADVE "永久链接至目标")
    :   scan peer adv report, param [ble_recv_adv_t](#structble__recv__adv__t "#structble__recv__adv__t")

    enumerator BLE_5_MTU_CHANGE[](#_CPPv4N12ble_notice_t16BLE_5_MTU_CHANGEE "永久链接至目标")
    :   mtu change event, param [ble_mtu_change_t](#structble__mtu__change__t "#structble__mtu__change__t")

    enumerator BLE_5_CONNECT_EVENT[](#_CPPv4N12ble_notice_t19BLE_5_CONNECT_EVENTE "永久链接至目标")
    :   as slaver, recv connnect event, param [ble_conn_ind_t](#structble__conn__ind__t "#structble__conn__ind__t")

    enumerator BLE_5_DISCONNECT_EVENT[](#_CPPv4N12ble_notice_t22BLE_5_DISCONNECT_EVENTE "永久链接至目标")
    :   recv disconnect event, param [ble_discon_ind_t](#structble__discon__ind__t "#structble__discon__ind__t")

    enumerator BLE_5_ATT_INFO_REQ[](#_CPPv4N12ble_notice_t18BLE_5_ATT_INFO_REQE "永久链接至目标")
    :   PREPARE_WRITE_REQ indicate.

    enumerator BLE_5_CREATE_DB[](#_CPPv4N12ble_notice_t15BLE_5_CREATE_DBE "永久链接至目标")
    :   create db event, param [ble_create_db_t](#structble__create__db__t "#structble__create__db__t")

    enumerator BLE_5_TX_DONE[](#_CPPv4N12ble_notice_t13BLE_5_TX_DONEE "永久链接至目标")
    :   tx complete event, param null

    enumerator BLE_5_PAIRING_REQ[](#_CPPv4N12ble_notice_t17BLE_5_PAIRING_REQE "永久链接至目标")
    :   smp report

    enumerator BLE_5_PAIRING_SUCCEED[](#_CPPv4N12ble_notice_t21BLE_5_PAIRING_SUCCEEDE "永久链接至目标")

    enumerator BLE_5_PAIRING_FAILED[](#_CPPv4N12ble_notice_t20BLE_5_PAIRING_FAILEDE "永久链接至目标")

    enumerator BLE_5_PARING_PASSKEY_REQ[](#_CPPv4N12ble_notice_t24BLE_5_PARING_PASSKEY_REQE "永久链接至目标")

    enumerator BLE_5_ENCRYPT_EVENT[](#_CPPv4N12ble_notice_t19BLE_5_ENCRYPT_EVENTE "永久链接至目标")

    enumerator BLE_5_INIT_CONNECT_EVENT[](#_CPPv4N12ble_notice_t24BLE_5_INIT_CONNECT_EVENTE "永久链接至目标")
    :   as master, recv connect event

    enumerator BLE_5_INIT_DISCONNECT_EVENT[](#_CPPv4N12ble_notice_t27BLE_5_INIT_DISCONNECT_EVENTE "永久链接至目标")

    enumerator BLE_5_INIT_CONNECT_FAILED_EVENT[](#_CPPv4N12ble_notice_t31BLE_5_INIT_CONNECT_FAILED_EVENTE "永久链接至目标")

    enumerator BLE_5_SDP_REGISTER_FAILED[](#_CPPv4N12ble_notice_t25BLE_5_SDP_REGISTER_FAILEDE "永久链接至目标")

    enumerator BLE_5_READ_PHY_EVENT[](#_CPPv4N12ble_notice_t20BLE_5_READ_PHY_EVENTE "永久链接至目标")
    :   get current conn phy result, param [ble_read_phy_t](#structble__read__phy__t "#structble__read__phy__t")

    enumerator BLE_5_CONN_UPDATA_EVENT[](#_CPPv4N12ble_notice_t23BLE_5_CONN_UPDATA_EVENTE "永久链接至目标")
    :   recv conn update event, param [ble_conn_param_t](#structble__conn__param__t "#structble__conn__param__t")

    enumerator BLE_5_PERIODIC_SYNC_CMPL_EVENT[](#_CPPv4N12ble_notice_t30BLE_5_PERIODIC_SYNC_CMPL_EVENTE "永久链接至目标")

    enumerator BLE_5_DISCOVERY_PRIMARY_SERVICE_EVENT[](#_CPPv4N12ble_notice_t37BLE_5_DISCOVERY_PRIMARY_SERVICE_EVENTE "永久链接至目标")

    enumerator BLE_5_DISCOVERY_CHAR_EVENT[](#_CPPv4N12ble_notice_t26BLE_5_DISCOVERY_CHAR_EVENTE "永久链接至目标")

    enumerator BLE_5_RECV_NOTIFY_EVENT[](#_CPPv4N12ble_notice_t23BLE_5_RECV_NOTIFY_EVENTE "永久链接至目标")

    enumerator BLE_5_ATT_READ_RESPONSE[](#_CPPv4N12ble_notice_t23BLE_5_ATT_READ_RESPONSEE "永久链接至目标")

    enumerator BLE_5_CONN_UPD_PAR_ASK[](#_CPPv4N12ble_notice_t22BLE_5_CONN_UPD_PAR_ASKE "永久链接至目标")

    enumerator BLE_5_SHUTDOWN_SUCCEED[](#_CPPv4N12ble_notice_t22BLE_5_SHUTDOWN_SUCCEEDE "永久链接至目标")

    enumerator BLE_5_DELETE_SERVICE_DONE[](#_CPPv4N12ble_notice_t25BLE_5_DELETE_SERVICE_DONEE "永久链接至目标")
    :   delete service event

    enumerator BLE_5_GAP_CMD_CMP_EVENT[](#_CPPv4N12ble_notice_t23BLE_5_GAP_CMD_CMP_EVENTE "永久链接至目标")

    enumerator BLE_5_ADV_STOPPED_EVENT[](#_CPPv4N12ble_notice_t23BLE_5_ADV_STOPPED_EVENTE "永久链接至目标")

    enumerator BLE_5_READ_RSSI_CMPL_EVENT[](#_CPPv4N12ble_notice_t26BLE_5_READ_RSSI_CMPL_EVENTE "永久链接至目标")

    enumerator BLE_5_KEY_EVENT[](#_CPPv4N12ble_notice_t15BLE_5_KEY_EVENTE "永久链接至目标")

    enumerator BLE_5_BOND_INFO_REQ_EVENT[](#_CPPv4N12ble_notice_t25BLE_5_BOND_INFO_REQ_EVENTE "永久链接至目标")

    enumerator BLE_5_READ_BLOB_EVENT[](#_CPPv4N12ble_notice_t21BLE_5_READ_BLOB_EVENTE "永久链接至目标")

    enumerator BLE_5_PAIRING_SECURITY_REQ_EVENT[](#_CPPv4N12ble_notice_t32BLE_5_PAIRING_SECURITY_REQ_EVENTE "永久链接至目标")

    enumerator BLE_5_PARING_NUMBER_COMPARE_REQ_EVENT[](#_CPPv4N12ble_notice_t37BLE_5_PARING_NUMBER_COMPARE_REQ_EVENTE "永久链接至目标")

    enumerator BLE_5_SCAN_STOPPED_EVENT[](#_CPPv4N12ble_notice_t24BLE_5_SCAN_STOPPED_EVENTE "永久链接至目标")

    enumerator BLE_5_AUTHOR_WRITE_EVENT[](#_CPPv4N12ble_notice_t24BLE_5_AUTHOR_WRITE_EVENTE "永久链接至目标")
    :   This event corresponds to BLE_5_WRITE_EVENT, and is applicable after configuring the BK_GATT_VALUE_WRITE_AUTHOR_FLAG.

    enumerator BLE_5_AUTHOR_READ_EVENT[](#_CPPv4N12ble_notice_t23BLE_5_AUTHOR_READ_EVENTE "永久链接至目标")
    :   This event corresponds to BLE_5_READ_EVENT, and is applicable after configuring the BK_GATT_VALUE_READ_AUTHOR_FLAG.

enum CHAR_TYPE[](#_CPPv49CHAR_TYPE "永久链接至目标")
:   *Values:*

    enumerator CHARAC_NOTIFY[](#_CPPv4N9CHAR_TYPE13CHARAC_NOTIFYE "永久链接至目标")

    enumerator CHARAC_INDICATE[](#_CPPv4N9CHAR_TYPE15CHARAC_INDICATEE "永久链接至目标")

    enumerator CHARAC_READ[](#_CPPv4N9CHAR_TYPE11CHARAC_READE "永久链接至目标")

    enumerator CHARAC_READ_DONE[](#_CPPv4N9CHAR_TYPE16CHARAC_READ_DONEE "永久链接至目标")

    enumerator CHARAC_WRITE_DONE[](#_CPPv4N9CHAR_TYPE17CHARAC_WRITE_DONEE "永久链接至目标")

enum MASTER_COMMON_TYPE[](#_CPPv418MASTER_COMMON_TYPE "永久链接至目标")
:   *Values:*

    enumerator MST_TYPE_SVR_UUID[](#_CPPv4N18MASTER_COMMON_TYPE17MST_TYPE_SVR_UUIDE "永久链接至目标")

    enumerator MST_TYPE_ATT_UUID[](#_CPPv4N18MASTER_COMMON_TYPE17MST_TYPE_ATT_UUIDE "永久链接至目标")

    enumerator MST_TYPE_ATT_DESC[](#_CPPv4N18MASTER_COMMON_TYPE17MST_TYPE_ATT_DESCE "永久链接至目标")

    enumerator MST_TYPE_SDP_END[](#_CPPv4N18MASTER_COMMON_TYPE16MST_TYPE_SDP_ENDE "永久链接至目标")

    enumerator MST_TYPE_ATTC_SVR_UUID[](#_CPPv4N18MASTER_COMMON_TYPE22MST_TYPE_ATTC_SVR_UUIDE "永久链接至目标")

    enumerator MST_TYPE_ATTC_ATT_UUID[](#_CPPv4N18MASTER_COMMON_TYPE22MST_TYPE_ATTC_ATT_UUIDE "永久链接至目标")
    :   Service the UUID.

    enumerator MST_TYPE_ATTC_ATT_DESC[](#_CPPv4N18MASTER_COMMON_TYPE22MST_TYPE_ATTC_ATT_DESCE "永久链接至目标")
    :   ATT of a service.

    enumerator MST_TYPS_ATTC_PARAM_ERR[](#_CPPv4N18MASTER_COMMON_TYPE23MST_TYPS_ATTC_PARAM_ERRE "永久链接至目标")
    :   ATT DESC of a service.

    enumerator MST_TYPE_ATTC_ERR[](#_CPPv4N18MASTER_COMMON_TYPE17MST_TYPE_ATTC_ERRE "永久链接至目标")
    :   The delivered parameter is abnormal or unknown.

    enumerator MST_TYPE_ATTC_END[](#_CPPv4N18MASTER_COMMON_TYPE17MST_TYPE_ATTC_ENDE "永久链接至目标")
    :   if appm_get_init_attc_info return is ok && ble is disconnect,so update the event

    enumerator MST_TYPE_ATTC_WRITE_RSP[](#_CPPv4N18MASTER_COMMON_TYPE23MST_TYPE_ATTC_WRITE_RSPE "永久链接至目标")
    :   End of the operation.

    enumerator MST_TYPE_ATTC_WRITE_NO_RESPONSE[](#_CPPv4N18MASTER_COMMON_TYPE31MST_TYPE_ATTC_WRITE_NO_RESPONSEE "永久链接至目标")

    enumerator MST_TYPE_ATTC_CHARAC_READ_DONE[](#_CPPv4N18MASTER_COMMON_TYPE30MST_TYPE_ATTC_CHARAC_READ_DONEE "永久链接至目标")

    enumerator MST_TYPE_MTU_EXC[](#_CPPv4N18MASTER_COMMON_TYPE16MST_TYPE_MTU_EXCE "永久链接至目标")

    enumerator MST_TYPE_MTU_EXC_DONE[](#_CPPv4N18MASTER_COMMON_TYPE21MST_TYPE_MTU_EXC_DONEE "永久链接至目标")

    enumerator MST_TYPE_UPP_ASK[](#_CPPv4N18MASTER_COMMON_TYPE16MST_TYPE_UPP_ASKE "永久链接至目标")

    enumerator MST_TYPE_UPDATA_STATUS[](#_CPPv4N18MASTER_COMMON_TYPE22MST_TYPE_UPDATA_STATUSE "永久链接至目标")
    :   Ask if you agree to update the parameter.

    enumerator MST_TYPE_DISCOVER_PRI_SERVICE_RSP[](#_CPPv4N18MASTER_COMMON_TYPE33MST_TYPE_DISCOVER_PRI_SERVICE_RSPE "永久链接至目标")

    enumerator MST_TYPE_DISCOVER_PRI_SERVICE_BY_UUID_RSP[](#_CPPv4N18MASTER_COMMON_TYPE41MST_TYPE_DISCOVER_PRI_SERVICE_BY_UUID_RSPE "永久链接至目标")

    enumerator MST_TYPE_DISCOVER_PRI_SERVICE_BY_128_UUID_RSP[](#_CPPv4N18MASTER_COMMON_TYPE45MST_TYPE_DISCOVER_PRI_SERVICE_BY_128_UUID_RSPE "永久链接至目标")

    enumerator MST_TYPE_DISCOVER_CHAR_RSP[](#_CPPv4N18MASTER_COMMON_TYPE26MST_TYPE_DISCOVER_CHAR_RSPE "永久链接至目标")

    enumerator MST_TYPE_DISCOVER_CHAR_BY_UUID_RSP[](#_CPPv4N18MASTER_COMMON_TYPE34MST_TYPE_DISCOVER_CHAR_BY_UUID_RSPE "永久链接至目标")

    enumerator MST_TYPE_DISCOVER_CHAR_BY_128_UUID_RSP[](#_CPPv4N18MASTER_COMMON_TYPE38MST_TYPE_DISCOVER_CHAR_BY_128_UUID_RSPE "永久链接至目标")

    enumerator MST_TYPE_DISCOVER_CHAR_DESC[](#_CPPv4N18MASTER_COMMON_TYPE27MST_TYPE_DISCOVER_CHAR_DESCE "永久链接至目标")

    enumerator MST_TYPE_DISCOVER_COMPLETED[](#_CPPv4N18MASTER_COMMON_TYPE27MST_TYPE_DISCOVER_COMPLETEDE "永久链接至目标")

enum msg_attc[](#_CPPv48msg_attc "永久链接至目标")
:   *Values:*

    enumerator MST_ATTC_ALL[](#_CPPv4N8msg_attc12MST_ATTC_ALLE "永久链接至目标")

    enumerator MST_ATTC_GET_SVR_UUID_ALL[](#_CPPv4N8msg_attc25MST_ATTC_GET_SVR_UUID_ALLE "永久链接至目标")

    enumerator MST_ATTC_GET_SVR_UUID_BY_SVR_UUID[](#_CPPv4N8msg_attc33MST_ATTC_GET_SVR_UUID_BY_SVR_UUIDE "永久链接至目标")

    enumerator MST_ATTC_GET_ATT_UUID_ALL[](#_CPPv4N8msg_attc25MST_ATTC_GET_ATT_UUID_ALLE "永久链接至目标")

    enumerator MST_ATTC_GET_ATT_DESC_UUID_ALL[](#_CPPv4N8msg_attc30MST_ATTC_GET_ATT_DESC_UUID_ALLE "永久链接至目标")

    enumerator MST_ATTC_SVR_ATT_BY_SVR_UUID[](#_CPPv4N8msg_attc28MST_ATTC_SVR_ATT_BY_SVR_UUIDE "永久链接至目标")

    enumerator MST_ATTC_SVR_ATT_DESC_BY_SVR_UUID[](#_CPPv4N8msg_attc33MST_ATTC_SVR_ATT_DESC_BY_SVR_UUIDE "永久链接至目标")

    enumerator MST_ATTC_SVR_ATT_AND_DESC_BY_SVR_UUID[](#_CPPv4N8msg_attc37MST_ATTC_SVR_ATT_AND_DESC_BY_SVR_UUIDE "永久链接至目标")
    :   Gets all ATT-DESC’s for this SVR-UUID for this connection.

enum adv_report_type[](#_CPPv415adv_report_type "永久链接至目标")
:   *Values:*

    enumerator REPORT_TYPE_ADV_EXT[](#_CPPv4N15adv_report_type19REPORT_TYPE_ADV_EXTE "永久链接至目标")
    :   Extended advertising report.

    enumerator REPORT_TYPE_ADV_LEG[](#_CPPv4N15adv_report_type19REPORT_TYPE_ADV_LEGE "永久链接至目标")
    :   Legacy advertising report.

    enumerator REPORT_TYPE_SCAN_RSP_EXT[](#_CPPv4N15adv_report_type24REPORT_TYPE_SCAN_RSP_EXTE "永久链接至目标")
    :   Extended scan response report.

    enumerator REPORT_TYPE_SCAN_RSP_LEG[](#_CPPv4N15adv_report_type24REPORT_TYPE_SCAN_RSP_LEGE "永久链接至目标")
    :   Legacy scan response report.

    enumerator REPORT_TYPE_PER_ADV[](#_CPPv4N15adv_report_type19REPORT_TYPE_PER_ADVE "永久链接至目标")
    :   Periodic advertising report.

enum adv_report_info[](#_CPPv415adv_report_info "永久链接至目标")
:   *Values:*

    enumerator REPORT_INFO_REPORT_TYPE_MASK[](#_CPPv4N15adv_report_info28REPORT_INFO_REPORT_TYPE_MASKE "永久链接至目标")
    :   Report Type.

    enumerator REPORT_INFO_COMPLETE_BIT[](#_CPPv4N15adv_report_info24REPORT_INFO_COMPLETE_BITE "永久链接至目标")
    :   Report is complete.

    enumerator REPORT_INFO_CONN_ADV_BIT[](#_CPPv4N15adv_report_info24REPORT_INFO_CONN_ADV_BITE "永久链接至目标")
    :   Connectable advertising.

    enumerator REPORT_INFO_SCAN_ADV_BIT[](#_CPPv4N15adv_report_info24REPORT_INFO_SCAN_ADV_BITE "永久链接至目标")
    :   Scannable advertising.

    enumerator REPORT_INFO_DIR_ADV_BIT[](#_CPPv4N15adv_report_info23REPORT_INFO_DIR_ADV_BITE "永久链接至目标")
    :   Directed advertising.

enum adv_type[](#_CPPv48adv_type "永久链接至目标")
:   Type of advertising that can be created.


    *Values:*

    enumerator ADV_TYPE_LEGACY[](#_CPPv4N8adv_type15ADV_TYPE_LEGACYE "永久链接至目标")
    :   Legacy advertising.

    enumerator ADV_TYPE_EXTENDED[](#_CPPv4N8adv_type17ADV_TYPE_EXTENDEDE "永久链接至目标")
    :   Extended advertising.

    enumerator ADV_TYPE_PERIODIC[](#_CPPv4N8adv_type17ADV_TYPE_PERIODICE "永久链接至目标")
    :   Periodic advertising.

enum adv_prop_bf[](#_CPPv411adv_prop_bf "永久链接至目标")
:   Advertising properties bit field bit positions.


    *Values:*

    enumerator ADV_PROP_CONNECTABLE_BIT[](#_CPPv4N11adv_prop_bf24ADV_PROP_CONNECTABLE_BITE "永久链接至目标")
    :   Indicate that advertising is connectable, reception of CONNECT_REQ or AUX_CONNECT_REQ PDUs is accepted. Not applicable for periodic advertising.

    enumerator ADV_PROP_SCANNABLE_BIT[](#_CPPv4N11adv_prop_bf22ADV_PROP_SCANNABLE_BITE "永久链接至目标")
    :   Indicate that advertising is scannable, reception of SCAN_REQ or AUX_SCAN_REQ PDUs is accepted

    enumerator ADV_PROP_DIRECTED_BIT[](#_CPPv4N11adv_prop_bf21ADV_PROP_DIRECTED_BITE "永久链接至目标")
    :   Indicate that advertising targets a specific device. Only apply in following cases:


        - Legacy advertising: if connectable

        - Extended advertising: connectable or (non connectable and non discoverable)

    enumerator ADV_PROP_HDC_BIT[](#_CPPv4N11adv_prop_bf16ADV_PROP_HDC_BITE "永久链接至目标")
    :   Indicate that High Duty Cycle has to be used for advertising on primary channel Apply only if created advertising is not an extended advertising

    enumerator ADV_PROP_PROP_LEGACY_BIT[](#_CPPv4N11adv_prop_bf24ADV_PROP_PROP_LEGACY_BITE "永久链接至目标")
    :   Use legacy advertising PDUs.

    enumerator ADV_PROP_ANONYMOUS_BIT[](#_CPPv4N11adv_prop_bf22ADV_PROP_ANONYMOUS_BITE "永久链接至目标")
    :   Enable anonymous mode. Device address won’t appear in send PDUs Valid only if created advertising is an extended advertising

    enumerator ADV_PROP_TX_PWR_BIT[](#_CPPv4N11adv_prop_bf19ADV_PROP_TX_PWR_BITE "永久链接至目标")
    :   Include TX Power in the extended header of the advertising PDU. Valid only if created advertising is not a legacy advertising

enum adv_chnl_map[](#_CPPv412adv_chnl_map "永久链接至目标")
:   Advertising channels enables.


    *Values:*

    enumerator ADV_CHNL_37[](#_CPPv4N12adv_chnl_map11ADV_CHNL_37E "永久链接至目标")
    :   Byte value for advertising channel map for channel 37 enable.

    enumerator ADV_CHNL_38[](#_CPPv4N12adv_chnl_map11ADV_CHNL_38E "永久链接至目标")
    :   Byte value for advertising channel map for channel 38 enable.

    enumerator ADV_CHNL_39[](#_CPPv4N12adv_chnl_map11ADV_CHNL_39E "永久链接至目标")
    :   Byte value for advertising channel map for channel 39 enable.

    enumerator ADV_ALL_CHNLS[](#_CPPv4N12adv_chnl_map13ADV_ALL_CHNLSE "永久链接至目标")
    :   Byte value for advertising channel map for channel 37, 38 and 39 enable.

enum phy_type_le[](#_CPPv411phy_type_le "永久链接至目标")
:   PHY Type.


    *Values:*

    enumerator PHY_TYPE_LE_1M[](#_CPPv4N11phy_type_le14PHY_TYPE_LE_1ME "永久链接至目标")
    :   LE 1M.

    enumerator PHY_TYPE_LE_2M[](#_CPPv4N11phy_type_le14PHY_TYPE_LE_2ME "永久链接至目标")
    :   LE 2M.

    enumerator PHY_TYPE_LE_CODED[](#_CPPv4N11phy_type_le17PHY_TYPE_LE_CODEDE "永久链接至目标")
    :   LE Coded.

enum initiating_phy_type_le[](#_CPPv422initiating_phy_type_le "永久链接至目标")
:   Initiating PHY Type.


    *Values:*

    enumerator INIT_PHY_TYPE_LE_1M[](#_CPPv4N22initiating_phy_type_le19INIT_PHY_TYPE_LE_1ME "永久链接至目标")
    :   LE 1M.

    enumerator INIT_PHY_TYPE_LE_2M[](#_CPPv4N22initiating_phy_type_le19INIT_PHY_TYPE_LE_2ME "永久链接至目标")
    :   LE 2M.

    enumerator INIT_PHY_TYPE_LE_CODED[](#_CPPv4N22initiating_phy_type_le22INIT_PHY_TYPE_LE_CODEDE "永久链接至目标")
    :   LE Coded.

enum ble_own_addr_type[](#_CPPv417ble_own_addr_type "永久链接至目标")
:   Own addr type.


    *Values:*

    enumerator OWN_ADDR_TYPE_PUBLIC_OR_STATIC_ADDR[](#_CPPv4N17ble_own_addr_type35OWN_ADDR_TYPE_PUBLIC_OR_STATIC_ADDRE "永久链接至目标")
    :   Public or Private Static Address according to device address configuration Attention: Private Static Address is not used now, so set will be public Attention: this enum is derecated, use OWN_ADDR_TYPE_PUBLIC_ADDR instead.

    enumerator OWN_ADDR_TYPE_GEN_RSLV_OR_RANDOM_ADDR[](#_CPPv4N17ble_own_addr_type37OWN_ADDR_TYPE_GEN_RSLV_OR_RANDOM_ADDRE "永久链接至目标")
    :   Generated resolvable private random or random address, will auto refresh periodic Attention: RPA is not used now, so set will be random

    enumerator OWN_ADDR_TYPE_GEN_NON_RSLV_OR_RANDOM_ADDR[](#_CPPv4N17ble_own_addr_type41OWN_ADDR_TYPE_GEN_NON_RSLV_OR_RANDOM_ADDRE "永久链接至目标")
    :   Generated non-resolvable private random or random address, will auto refresh periodic Attention: NRPA is not used now, so set will be random

    enumerator OWN_ADDR_TYPE_PUBLIC_ADDR[](#_CPPv4N17ble_own_addr_type25OWN_ADDR_TYPE_PUBLIC_ADDRE "永久链接至目标")
    :   public addr

    enumerator OWN_ADDR_TYPE_RANDOM_ADDR[](#_CPPv4N17ble_own_addr_type25OWN_ADDR_TYPE_RANDOM_ADDRE "永久链接至目标")
    :   use bk_ble_set_adv_random_addr addr

enum ble_scan_type[](#_CPPv413ble_scan_type "永久链接至目标")
:   Scan type.


    *Values:*

    enumerator PASSIVE_SCANNING[](#_CPPv4N13ble_scan_type16PASSIVE_SCANNINGE "永久链接至目标")
    :   Passive Scanning. No scanning PDUs shall be sent (default)

    enumerator ACTIVE_SCANNING[](#_CPPv4N13ble_scan_type15ACTIVE_SCANNINGE "永久链接至目标")
    :   Active scanning. Scanning PDUs may be sent.

enum ble_scan_filter_policy[](#_CPPv422ble_scan_filter_policy "永久链接至目标")
:   Scan filter policy.


    *Values:*

    enumerator BASIC_UNFILTER_SCAN_POLICY[](#_CPPv4N22ble_scan_filter_policy26BASIC_UNFILTER_SCAN_POLICYE "永久链接至目标")
    :   Basic unfiltered scanning filter policy.

    enumerator BASIC_FILTER_SCAN_POLICY[](#_CPPv4N22ble_scan_filter_policy24BASIC_FILTER_SCAN_POLICYE "永久链接至目标")
    :   Basic filtered scanning filter policy.

    enumerator EXTENED_UNFILER_SCAN_POLICY[](#_CPPv4N22ble_scan_filter_policy27EXTENED_UNFILER_SCAN_POLICYE "永久链接至目标")
    :   Extended unfiltered scanning filter policy.

    enumerator EXTENED_FILER_SCAN_POLICY[](#_CPPv4N22ble_scan_filter_policy25EXTENED_FILER_SCAN_POLICYE "永久链接至目标")
    :   Extended filtered scanning filter policy.

enum ble_sync_cte_type[](#_CPPv417ble_sync_cte_type "永久链接至目标")
:   Constant Tone Extension sync filtering type.


    *Values:*

    enumerator CTE_NO_SYNC_WITH_AOA[](#_CPPv4N17ble_sync_cte_type20CTE_NO_SYNC_WITH_AOAE "永久链接至目标")
    :   Do not sync to packets with an AoA Constant Tone Extension.

    enumerator CTE_NO_SYNC_WITH_AOD_1US_SLOT[](#_CPPv4N17ble_sync_cte_type29CTE_NO_SYNC_WITH_AOD_1US_SLOTE "永久链接至目标")
    :   Do not sync to packets with an AoD Constant Tone Extension with 1 us slots.

    enumerator CTE_NO_SYNC_WITH_AOD_2US_SLOT[](#_CPPv4N17ble_sync_cte_type29CTE_NO_SYNC_WITH_AOD_2US_SLOTE "永久链接至目标")
    :   Do not sync to packets with an AoD Constant Tone Extension with 2 us slots.

    enumerator CTE_NO_SYNC_WITH_TYPE_3[](#_CPPv4N17ble_sync_cte_type23CTE_NO_SYNC_WITH_TYPE_3E "永久链接至目标")
    :   Do not sync to packets with a type 3 Constant Tone Extension (currently reserved for future use)

    enumerator CTE_NO_SYNC_WITHOUT_CTE[](#_CPPv4N17ble_sync_cte_type23CTE_NO_SYNC_WITHOUT_CTEE "永久链接至目标")
    :   Do not sync to packets without a Constant Tone Extension.

enum nsp24g_channel_t[](#_CPPv416nsp24g_channel_t "永久链接至目标")
:   *Values:*

    enumerator NSP24G_2423[](#_CPPv4N16nsp24g_channel_t11NSP24G_2423E "永久链接至目标")

    enumerator NSP24G_2470[](#_CPPv4N16nsp24g_channel_t11NSP24G_2470E "永久链接至目标")

enum gap_auth_mask[](#_CPPv413gap_auth_mask "永久链接至目标")
:   Authentication mask.


    *Values:*

    enumerator GAP_AUTH_NONE[](#_CPPv4N13gap_auth_mask13GAP_AUTH_NONEE "永久链接至目标")
    :   No Flag set.

    enumerator GAP_AUTH_BOND[](#_CPPv4N13gap_auth_mask13GAP_AUTH_BONDE "永久链接至目标")
    :   Bond authentication.

    enumerator GAP_AUTH_MITM[](#_CPPv4N13gap_auth_mask13GAP_AUTH_MITME "永久链接至目标")
    :   Man In the middle protection.

    enumerator GAP_AUTH_SEC_CON[](#_CPPv4N13gap_auth_mask16GAP_AUTH_SEC_CONE "永久链接至目标")
    :   Secure Connection.

    enumerator GAP_AUTH_KEY_NOTIF[](#_CPPv4N13gap_auth_mask18GAP_AUTH_KEY_NOTIFE "永久链接至目标")
    :   Key Notification.

enum gap_auth[](#_CPPv48gap_auth "永久链接至目标")
:   *Values:*

    enumerator GAP_AUTH_REQ_NO_MITM_NO_BOND[](#_CPPv4N8gap_auth28GAP_AUTH_REQ_NO_MITM_NO_BONDE "永久链接至目标")
    :   No MITM No Bonding.

    enumerator GAP_AUTH_REQ_NO_MITM_BOND[](#_CPPv4N8gap_auth25GAP_AUTH_REQ_NO_MITM_BONDE "永久链接至目标")
    :   No MITM Bonding.

    enumerator GAP_AUTH_REQ_MITM_NO_BOND[](#_CPPv4N8gap_auth25GAP_AUTH_REQ_MITM_NO_BONDE "永久链接至目标")
    :   MITM No Bonding.

    enumerator GAP_AUTH_REQ_MITM_BOND[](#_CPPv4N8gap_auth22GAP_AUTH_REQ_MITM_BONDE "永久链接至目标")
    :   MITM and Bonding.

    enumerator GAP_AUTH_REQ_SEC_CON_NO_BOND[](#_CPPv4N8gap_auth28GAP_AUTH_REQ_SEC_CON_NO_BONDE "永久链接至目标")
    :   SEC_CON and No Bonding.

    enumerator GAP_AUTH_REQ_SEC_CON_BOND[](#_CPPv4N8gap_auth25GAP_AUTH_REQ_SEC_CON_BONDE "永久链接至目标")
    :   SEC_CON and Bonding.

    enumerator GAP_AUTH_REQ_LAST[](#_CPPv4N8gap_auth17GAP_AUTH_REQ_LASTE "永久链接至目标")

    enumerator GAP_AUTH_REQ_MASK[](#_CPPv4N8gap_auth17GAP_AUTH_REQ_MASKE "永久链接至目标")
    :   Mask of authentication features without reserved flag.

enum bk_ble_gap_io_cap[](#_CPPv417bk_ble_gap_io_cap "永久链接至目标")
:   IO Capability Values.


    *Values:*

    enumerator BK_BLE_GAP_IO_CAP_DISPLAY_ONLY[](#_CPPv4N17bk_ble_gap_io_cap30BK_BLE_GAP_IO_CAP_DISPLAY_ONLYE "永久链接至目标")
    :   Display Only.

    enumerator BK_BLE_GAP_IO_CAP_DISPLAY_YES_NO[](#_CPPv4N17bk_ble_gap_io_cap32BK_BLE_GAP_IO_CAP_DISPLAY_YES_NOE "永久链接至目标")
    :   Display Yes No.

    enumerator BK_BLE_GAP_IO_CAP_KB_ONLY[](#_CPPv4N17bk_ble_gap_io_cap25BK_BLE_GAP_IO_CAP_KB_ONLYE "永久链接至目标")
    :   Keyboard Only.

    enumerator BK_BLE_GAP_IO_CAP_NO_INPUT_NO_OUTPUT[](#_CPPv4N17bk_ble_gap_io_cap36BK_BLE_GAP_IO_CAP_NO_INPUT_NO_OUTPUTE "永久链接至目标")
    :   No Input No Output.

    enumerator BK_BLE_GAP_IO_CAP_KB_DISPLAY[](#_CPPv4N17bk_ble_gap_io_cap28BK_BLE_GAP_IO_CAP_KB_DISPLAYE "永久链接至目标")
    :   Keyboard Display.

    enumerator BK_BLE_GAP_IO_CAP_LAST[](#_CPPv4N17bk_ble_gap_io_cap22BK_BLE_GAP_IO_CAP_LASTE "永久链接至目标")

enum gap_sec_req[](#_CPPv411gap_sec_req "永久链接至目标")
:   Security Defines.


    *Values:*

    enumerator GAP_NO_SEC[](#_CPPv4N11gap_sec_req10GAP_NO_SECE "永久链接至目标")
    :   No security (no authentication and encryption)

    enumerator GAP_SEC1_NOAUTH_PAIR_ENC[](#_CPPv4N11gap_sec_req24GAP_SEC1_NOAUTH_PAIR_ENCE "永久链接至目标")
    :   Unauthenticated pairing with encryption.

    enumerator GAP_SEC1_AUTH_PAIR_ENC[](#_CPPv4N11gap_sec_req22GAP_SEC1_AUTH_PAIR_ENCE "永久链接至目标")
    :   Authenticated pairing with encryption.

    enumerator GAP_SEC2_NOAUTH_DATA_SGN[](#_CPPv4N11gap_sec_req24GAP_SEC2_NOAUTH_DATA_SGNE "永久链接至目标")
    :   Unauthenticated pairing with data signing.

    enumerator GAP_SEC2_AUTH_DATA_SGN[](#_CPPv4N11gap_sec_req22GAP_SEC2_AUTH_DATA_SGNE "永久链接至目标")
    :   Authentication pairing with data signing.

    enumerator GAP_SEC1_SEC_CON_PAIR_ENC[](#_CPPv4N11gap_sec_req25GAP_SEC1_SEC_CON_PAIR_ENCE "永久链接至目标")
    :   Secure Connection pairing with encryption.

enum gap_oob[](#_CPPv47gap_oob "永久链接至目标")
:   OOB Data Present Flag Values.


    *Values:*

    enumerator GAP_OOB_AUTH_DATA_NOT_PRESENT[](#_CPPv4N7gap_oob29GAP_OOB_AUTH_DATA_NOT_PRESENTE "永久链接至目标")
    :   OOB Data not present.

    enumerator GAP_OOB_AUTH_DATA_PRESENT[](#_CPPv4N7gap_oob25GAP_OOB_AUTH_DATA_PRESENTE "永久链接至目标")
    :   OOB data present.

    enumerator GAP_OOB_AUTH_DATA_LAST[](#_CPPv4N7gap_oob22GAP_OOB_AUTH_DATA_LASTE "永久链接至目标")

enum gap_key_distr[](#_CPPv413gap_key_distr "永久链接至目标")
:   key distr


    *Values:*

    enumerator BK_BLE_GAP_KDIST_NONE[](#_CPPv4N13gap_key_distr21BK_BLE_GAP_KDIST_NONEE "永久链接至目标")
    :   No Keys to distribute.

    enumerator BK_BLE_GAP_KDIST_ENCKEY[](#_CPPv4N13gap_key_distr23BK_BLE_GAP_KDIST_ENCKEYE "永久链接至目标")
    :   Encryption key in distribution.

    enumerator BK_BLE_GAP_KDIST_IDKEY[](#_CPPv4N13gap_key_distr22BK_BLE_GAP_KDIST_IDKEYE "永久链接至目标")
    :   IRK (ID key)in distribution.

    enumerator BK_BLE_GAP_KDIST_SIGNKEY[](#_CPPv4N13gap_key_distr24BK_BLE_GAP_KDIST_SIGNKEYE "永久链接至目标")
    :   CSRK(Signature key) in distribution.

    enumerator BK_BLE_GAP_KDIST_LINKKEY[](#_CPPv4N13gap_key_distr24BK_BLE_GAP_KDIST_LINKKEYE "永久链接至目标")
    :   LTK in distribution.

    enumerator BK_BLE_GAP_KDIST_LAST[](#_CPPv4N13gap_key_distr21BK_BLE_GAP_KDIST_LASTE "永久链接至目标")


## Reference link[](#reference-link "永久链接至标题")

> [API Reference :](../../api-reference/bluetooth/index.md "../../api-reference/bluetooth/index.md") Introduced the Bluetooth API interface
>
> [User and Developer Guide :](../../developer-guide/bluetooth/index.md "../../developer-guide/bluetooth/index.md") Introduced common usage scenarios of Bluetooth
>
> [Samples and Demos:](../../examples/bluetooth/index.md "../../examples/bluetooth/index.md") Introduced the use and operation of Bluetooth samples
