---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/controller-guide/api-reference/bluetooth/ble_api.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="api"></a>

# 蓝牙API

蓝牙API提供低功耗蓝牙(BLE)通信和管理接口。

<a id="header-file"></a>

## Header File

- [bluetooth/bk\_ble.h](https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_ble.h)

<a id="functions"></a>

## Functions

<a id="_CPPv416bk_ble_create_dbP13bk_ble_db_cfg"></a>

<a id="_CPPv316bk_ble_create_dbP13bk_ble_db_cfg"></a> <a id="_CPPv216bk_ble_create_dbP13bk_ble_db_cfg"></a> <a id="bk_ble_create_db__bk_ble_db_cfgP"></a> <a id="group__bk__ble__api__v1_1ga48fc31375113253658e599d347a37878"></a> ble\_err\_t bk\_ble\_create\_db(struct bk\_ble\_db\_cfg \*ble\_db\_cfg)
:   Register a gatt service.

    User example: First we must build test\_service\_db test\_service\_db is a database for att, which used in ble discovery. reading writing and other operation is used on a att database.

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

    TEST\_IDX\_SVC is nessecery, is declare a primary att service. The macro define is:

    ```
    #define DECL_PRIMARY_SERVICE_128     {0x00,0x28,0}
    ```

    which is an UUID say it is a “primary service” BK\_BLE\_PERM\_SET(RD, ENABLE) means it can be read, and must be read, so it can be discove by peer master.

    TEST\_IDX\_CHAR\_DECL declare a characteristic as a element in service, it must be BK\_BLE\_PERM\_SET(RD, ENABLE)

    ```
    #define DECL_CHARACTERISTIC_128      {0x03,0x28,0}
    ```

    show it’s a “characteristic”

    BK\_BLE\_PERM\_SET(RD, ENABLE) means it can be read, and must be read, so it can be discove by peer master.

    TEST\_IDX\_CHAR\_VALUE is the real value of TEST\_IDX\_CHAR\_DECL, {0x34, 0x12, 0} means it’s type is 0x1234, you can determine by you self BK\_BLE\_PERM\_SET(NTF, ENABLE) means it cant notify peer, such as value change. For exzample, BLE mouse report pos by “notify” peer. BK\_BLE\_PERM\_SET(RI, ENABLE) means if peer read this att record, it will enable notification. BK\_BLE\_PERM\_SET(UUID\_LEN, UUID\_16) means the first elem’s max len of TEST\_IDX\_CHAR\_VALUE.

    TEST\_IDX\_CHAR\_DESC is a Client Characteristic Configuration Descriptor for TEST\_IDX\_CHAR\_VALUE, it used by peer master as know as a client. As common usage, it config TEST\_IDX\_CHAR\_VALUE indication or notification. Peer can write this att handle to triggle it. Must be BK\_BLE\_PERM\_SET(RD, ENABLE) \| BK\_BLE\_PERM\_SET(WRITE\_REQ, ENABLE)

    Now, you have a basic database for peer, in this case, peer write TEST\_IDX\_CHAR\_DESC or read TEST\_IDX\_CHAR\_VALUE to enable notification, and then we notify peer by TEST\_IDX\_CHAR\_VALUE

    Secondlly, we build ble\_db\_cfg

    ```
    struct bk_ble_db_cfg ble_db_cfg;

    ble_db_cfg.att_db = (ble_attm_desc_t *)test_service_db;
    ble_db_cfg.att_db_nb = TEST_IDX_NB;
    ble_db_cfg.prf_task_id = g_test_prf_task_id;
    ble_db_cfg.start_hdl = 0;
    ble_db_cfg.svc_perm = BK_BLE_PERM_SET(SVC_UUID_LEN, UUID_16);
    ```

    prf\_task\_id is app handle. If you have multi att service, used prf\_task\_id to distinguish it. svc\_perm show TEST\_IDX\_SVC UUID type’s len.

    参数
    :   **\-** – ble\_db\_cfg: service param

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv420bk_ble_set_notice_cb15ble_notice_cb_t"></a>

<a id="_CPPv320bk_ble_set_notice_cb15ble_notice_cb_t"></a> <a id="_CPPv220bk_ble_set_notice_cb15ble_notice_cb_t"></a> <a id="bk_ble_set_notice_cb__ble_notice_cb_t"></a> <a id="group__bk__ble__api__v1_1gaf161dd87d3a0fcc95e6cee58e4d18f0a"></a> void bk\_ble\_set\_notice\_cb(ble\_notice\_cb\_t func)
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
    :   1\. you must regist it, otherwise you cant get any event !

    **Attention**
    :   2\. you must regist it before bk\_ble\_create\_db, otherwise you cant get BLE\_5\_CREATE\_DB event

    参数
    :   **\-** – func: event callback

    返回
    :   - void

<a id="_CPPv424bk_ble_appm_get_dev_nameP7uint8_t8uint32_t"></a>

<a id="_CPPv324bk_ble_appm_get_dev_nameP7uint8_t8uint32_t"></a> <a id="_CPPv224bk_ble_appm_get_dev_nameP7uint8_t8uint32_t"></a> <a id="bk_ble_appm_get_dev_name__uint8_tP.uint32_t"></a> <a id="group__bk__ble__api__v1_1ga448a1a40bc38145553a43edcd3e481aa"></a> uint8\_t bk\_ble\_appm\_get\_dev\_name(uint8\_t \*name, uint32\_t buf\_len)
:   Get device name.

    参数
    :   **\-** – name: store the device name

        - buf\_len: the length of buf to store the device name

    返回
    :   - length: the length of device name

<a id="_CPPv424bk_ble_appm_set_dev_name7uint8_tP7uint8_t"></a>

<a id="_CPPv324bk_ble_appm_set_dev_name7uint8_tP7uint8_t"></a> <a id="_CPPv224bk_ble_appm_set_dev_name7uint8_tP7uint8_t"></a> <a id="bk_ble_appm_set_dev_name__uint8_t.uint8_tP"></a> <a id="group__bk__ble__api__v1_1gaf5cb0e30cb1ebd5711a12a9ca2346505"></a> uint8\_t bk\_ble\_appm\_set\_dev\_name(uint8\_t len, uint8\_t \*name)
:   Set device name.

    参数
    :   **\-** – len: the length of device name

        - name: the device name to be set

    返回
    :   - length: the length of device name

<a id="_CPPv425bk_ble_create_advertising7uint8_tP15ble_adv_param_t12ble_cmd_cb_t"></a>

<a id="_CPPv325bk_ble_create_advertising7uint8_tP15ble_adv_param_t12ble_cmd_cb_t"></a> <a id="_CPPv225bk_ble_create_advertising7uint8_tP15ble_adv_param_t12ble_cmd_cb_t"></a> <a id="bk_ble_create_advertising__uint8_t.ble_adv_param_tP.ble_cmd_cb_t"></a> <a id="group__bk__ble__api__v1_1gac697edafd3d29640923bfb753f3043c2"></a> ble\_err\_t bk\_ble\_create\_advertising(uint8\_t actv\_idx, ble\_adv\_param\_t \*adv\_param, ble\_cmd\_cb\_t callback)
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
    :   **\-** – actv\_idx: the index of activity

        - adv\_param: the advertising parameter
        - callback: register a callback for this action, ble\_cmd\_t: BLE\_CREATE\_ADV

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv424bk_ble_start_advertising7uint8_t6uint1612ble_cmd_cb_t"></a>

<a id="_CPPv324bk_ble_start_advertising7uint8_t6uint1612ble_cmd_cb_t"></a> <a id="_CPPv224bk_ble_start_advertising7uint8_t6uint1612ble_cmd_cb_t"></a> <a id="bk_ble_start_advertising__uint8_t.uint16.ble_cmd_cb_t"></a> <a id="group__bk__ble__api__v1_1ga91507146a662c6c47a76f52916accdd1"></a> ble\_err\_t bk\_ble\_start\_advertising(uint8\_t actv\_idx, uint16 duration, ble\_cmd\_cb\_t callback)
:   Start a ble advertising.

    **Attention**
    :   1.you must wait callback status, 0 mean success.

    **Attention**
    :   2.must used after bk\_ble\_create\_advertising

    参数
    :   **\-** – actv\_idx: the index of activity

        - duration: Advertising duration (in unit of 10ms). 0 means that advertising continues
        - callback: register a callback for this action, ble\_cmd\_t: BLE\_START\_ADV

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv423bk_ble_stop_advertising7uint8_t12ble_cmd_cb_t"></a>

<a id="_CPPv323bk_ble_stop_advertising7uint8_t12ble_cmd_cb_t"></a> <a id="_CPPv223bk_ble_stop_advertising7uint8_t12ble_cmd_cb_t"></a> <a id="bk_ble_stop_advertising__uint8_t.ble_cmd_cb_t"></a> <a id="group__bk__ble__api__v1_1ga8c6b7d094110e544c24e45ed5aff9fc5"></a> ble\_err\_t bk\_ble\_stop\_advertising(uint8\_t actv\_idx, ble\_cmd\_cb\_t callback)
:   Stop the advertising that has been started.

    **Attention**
    :   1.you must wait callback status, 0 mean success.

    **Attention**
    :   2.must used after bk\_ble\_start\_advertising

    参数
    :   **\-** – actv\_idx: the index of activity

        - callback: register a callback for this action, ble\_cmd\_t: BLE\_STOP\_ADV

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv425bk_ble_delete_advertising7uint8_t12ble_cmd_cb_t"></a>

<a id="_CPPv325bk_ble_delete_advertising7uint8_t12ble_cmd_cb_t"></a> <a id="_CPPv225bk_ble_delete_advertising7uint8_t12ble_cmd_cb_t"></a> <a id="bk_ble_delete_advertising__uint8_t.ble_cmd_cb_t"></a> <a id="group__bk__ble__api__v1_1ga7ae152d6b52f7d01ecc975ad51cb42d3"></a> ble\_err\_t bk\_ble\_delete\_advertising(uint8\_t actv\_idx, ble\_cmd\_cb\_t callback)
:   Delete the advertising that has been created.

    **Attention**
    :   1.you must wait callback status, 0 mean success.

    **Attention**
    :   2.must used after bk\_ble\_create\_advertising

    参数
    :   **\-** – actv\_idx: the index of activity

        - callback: register a callback for this action, ble\_cmd\_t: BLE\_DELETE\_ADV

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv419bk_ble_set_adv_data7uint8_tP7uint8_t7uint8_t12ble_cmd_cb_t"></a>

<a id="_CPPv319bk_ble_set_adv_data7uint8_tP7uint8_t7uint8_t12ble_cmd_cb_t"></a> <a id="_CPPv219bk_ble_set_adv_data7uint8_tP7uint8_t7uint8_t12ble_cmd_cb_t"></a> <a id="bk_ble_set_adv_data__uint8_t.uint8_tP.uint8_t.ble_cmd_cb_t"></a> <a id="group__bk__ble__api__v1_1ga2702094390c495f1392f444cdb56fa74"></a> ble\_err\_t bk\_ble\_set\_adv\_data(uint8\_t actv\_idx, uint8\_t \*adv\_buff, uint8\_t adv\_len, ble\_cmd\_cb\_t callback)
:   Set the advertising data.

    User example:

    ```
    const uint8_t adv_data[] = {0x02, 0x01, 0x06, 0x0A, 0x09, 0x37 0x32, 0x33, 0x31, 0x4e, 0x5f, 0x42, 0x4c, 0x45};
    bk_ble_set_adv_data(actv_idx, adv_data, sizeof(adv_data), ble_at_cmd_cb);
    ```

    **Attention**
    :   1.you must wait callback status, 0 mean success.

    **Attention**
    :   2.must used after bk\_ble\_create\_advertising

    参数
    :   **\-** – actv\_idx: the index of activity

        - adv\_buff: advertising data
        - adv\_len: the length of advertising data
        - callback: register a callback for this action, ble\_cmd\_t: BLE\_SET\_ADV\_DATA

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv424bk_ble_set_scan_rsp_data7uint8_tP7uint8_t7uint8_t12ble_cmd_cb_t"></a>

<a id="_CPPv324bk_ble_set_scan_rsp_data7uint8_tP7uint8_t7uint8_t12ble_cmd_cb_t"></a> <a id="_CPPv224bk_ble_set_scan_rsp_data7uint8_tP7uint8_t7uint8_t12ble_cmd_cb_t"></a> <a id="bk_ble_set_scan_rsp_data__uint8_t.uint8_tP.uint8_t.ble_cmd_cb_t"></a> <a id="group__bk__ble__api__v1_1gaf5cdf9f084cb3d354708814e98b7ee89"></a> ble\_err\_t bk\_ble\_set\_scan\_rsp\_data(uint8\_t actv\_idx, uint8\_t \*scan\_buff, uint8\_t scan\_len, ble\_cmd\_cb\_t callback)
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
    :   3.must used after bk\_ble\_create\_advertising

    参数
    :   **\-** – actv\_idx: the index of activity

        - scan\_buff: scan response data
        - scan\_len: the length of scan response data
        - callback: register a callback for this action, ble\_cmd\_t: BLE\_SET\_RSP\_DATA

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv423bk_ble_set_per_adv_data7uint8_tP7uint8_t7uint8_t12ble_cmd_cb_t"></a>

<a id="_CPPv323bk_ble_set_per_adv_data7uint8_tP7uint8_t7uint8_t12ble_cmd_cb_t"></a> <a id="_CPPv223bk_ble_set_per_adv_data7uint8_tP7uint8_t7uint8_t12ble_cmd_cb_t"></a> <a id="bk_ble_set_per_adv_data__uint8_t.uint8_tP.uint8_t.ble_cmd_cb_t"></a> <a id="group__bk__ble__api__v1_1ga383697ec5d75e11dc41c229a226d37fb"></a> ble\_err\_t bk\_ble\_set\_per\_adv\_data(uint8\_t actv\_idx, uint8\_t \*per\_adv\_buff, uint8\_t per\_adv\_len, ble\_cmd\_cb\_t callback)
:   Set the periodic advertising data.

    User example:

    ```
    const uint8_t adv_data[] = {0x02, 0x01, 0x06, 0x0A, 0x09, 0x37 0x32, 0x33, 0x31, 0x4e, 0x5f, 0x42, 0x4c, 0x45};
    bk_ble_set_per_adv_data(actv_idx, adv_data, sizeof(adv_data), ble_at_cmd_cb);
    ```

    **Attention**
    :   1.you must wait callback status, 0 mean success.

    **Attention**
    :   2.must used after bk\_ble\_create\_advertising

    参数
    :   **\-** – actv\_idx: the index of activity

        - per\_adv\_buff: periodic advertising data
        - per\_adv\_len: the length of periodic advertising data
        - callback: register a callback for this action, ble\_cmd\_t: BLE\_SET\_ADV\_DATA????

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv426bk_ble_set_adv_random_addr7uint8_tP7uint8_t12ble_cmd_cb_t"></a>

<a id="_CPPv326bk_ble_set_adv_random_addr7uint8_tP7uint8_t12ble_cmd_cb_t"></a> <a id="_CPPv226bk_ble_set_adv_random_addr7uint8_tP7uint8_t12ble_cmd_cb_t"></a> <a id="bk_ble_set_adv_random_addr__uint8_t.uint8_tP.ble_cmd_cb_t"></a> <a id="group__bk__ble__api__v1_1gaafc68ebc3bb23987096b8fdd99cc7fa2"></a> ble\_err\_t bk\_ble\_set\_adv\_random\_addr(uint8\_t actv\_idx, uint8\_t \*addr, ble\_cmd\_cb\_t callback)
:   Set the adv random addr.

    **Attention**
    :   1.you must wait callback status, 0 mean success.

    **Attention**
    :   2.must used after bk\_ble\_create\_advertising

    参数
    :   **\-** – actv\_idx: the index of activity

        - addr: random address
        - callback: register a callback for this action, ble\_cmd\_t: BLE\_SET\_ADV\_RANDOM\_ADDR

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv415bk_ble_read_phy7uint8_t"></a>

<a id="_CPPv315bk_ble_read_phy7uint8_t"></a> <a id="_CPPv215bk_ble_read_phy7uint8_t"></a> <a id="bk_ble_read_phy__uint8_t"></a> <a id="group__bk__ble__api__v1_1ga8e69af76e3ebefb0d346ca9255442d7b"></a> ble\_err\_t bk\_ble\_read\_phy(uint8\_t conn\_idx)
:   Read the phy of connection device.

    User example:

    ```
    bk_ble_read_phy(conn_idx);
    ```

    **Attention**
    :   1.must used after after connected

    参数
    :   **\-** – conn\_idx: the index of connection device

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv414bk_ble_set_phy7uint8_tP13ble_set_phy_t"></a>

<a id="_CPPv314bk_ble_set_phy7uint8_tP13ble_set_phy_t"></a> <a id="_CPPv214bk_ble_set_phy7uint8_tP13ble_set_phy_t"></a> <a id="bk_ble_set_phy__uint8_t.ble_set_phy_tP"></a> <a id="group__bk__ble__api__v1_1ga7bb8bab27172087eb7d85c3f453446a0"></a> ble\_err\_t bk\_ble\_set\_phy(uint8\_t conn\_idx, ble\_set\_phy\_t \*phy\_info)
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
    :   **\-** – conn\_idx: the index of connection device

        - phy\_info: phy parameters

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv419bk_ble_update_param7uint8_tP16ble_conn_param_t"></a>

<a id="_CPPv319bk_ble_update_param7uint8_tP16ble_conn_param_t"></a> <a id="_CPPv219bk_ble_update_param7uint8_tP16ble_conn_param_t"></a> <a id="bk_ble_update_param__uint8_t.ble_conn_param_tP"></a> <a id="group__bk__ble__api__v1_1ga2d069f95de976e5df02b8e6f77a011d6"></a> ble\_err\_t bk\_ble\_update\_param(uint8\_t conn\_idx, ble\_conn\_param\_t \*conn\_param)
:   Update connection parameters.

    **Attention**
    :   1.must used after connected

    参数
    :   **\-** – conn\_idx: the index of connection

        - conn\_param: connection parameters

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv417bk_ble_disconnect7uint8_t"></a>

<a id="_CPPv317bk_ble_disconnect7uint8_t"></a> <a id="_CPPv217bk_ble_disconnect7uint8_t"></a> <a id="bk_ble_disconnect__uint8_t"></a> <a id="group__bk__ble__api__v1_1gae0c8cf210cb4de1c5bb7ab84d3e604f6"></a> ble\_err\_t bk\_ble\_disconnect(uint8\_t conn\_idx)
:   Disconnect a ble connection.

    **Attention**
    :   1.must used after connected

    参数
    :   **\-** – conn\_idx: the index of connection

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv422bk_ble_gatt_mtu_change7uint8_t"></a>

<a id="_CPPv322bk_ble_gatt_mtu_change7uint8_t"></a> <a id="_CPPv222bk_ble_gatt_mtu_change7uint8_t"></a> <a id="bk_ble_gatt_mtu_change__uint8_t"></a> <a id="group__bk__ble__api__v1_1gad3315e1cae014584e043e51f17cf0f03"></a> ble\_err\_t bk\_ble\_gatt\_mtu\_change(uint8\_t conn\_idx)
:   Exchange MTU.

    **Attention**
    :   1.must used after connected

    参数
    :   **\-** – conn\_idx: the index of connection

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv418bk_ble_set_max_mtu8uint16_t"></a>

<a id="_CPPv318bk_ble_set_max_mtu8uint16_t"></a> <a id="_CPPv218bk_ble_set_max_mtu8uint16_t"></a> <a id="bk_ble_set_max_mtu__uint16_t"></a> <a id="group__bk__ble__api__v1_1gad3584b9ef0305ac4f8c15520d7302045"></a> ble\_err\_t bk\_ble\_set\_max\_mtu(uint16\_t max\_mtu)
:   Set maximal Exchange MTU.

    **Attention**
    :   1.must used before connected

    参数
    :   **\-** – max\_mtu: the value to set

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv421bk_ble_create_scaning7uint8_tP16ble_scan_param_t12ble_cmd_cb_t"></a>

<a id="_CPPv321bk_ble_create_scaning7uint8_tP16ble_scan_param_t12ble_cmd_cb_t"></a> <a id="_CPPv221bk_ble_create_scaning7uint8_tP16ble_scan_param_t12ble_cmd_cb_t"></a> <a id="bk_ble_create_scaning__uint8_t.ble_scan_param_tP.ble_cmd_cb_t"></a> <a id="group__bk__ble__api__v1_1ga0543b2a2e91eb632db83762d976ec616"></a> ble\_err\_t bk\_ble\_create\_scaning(uint8\_t actv\_idx, ble\_scan\_param\_t \*scan\_param, ble\_cmd\_cb\_t callback)
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
    :   **\-** – actv\_idx: the index of activity

        - scan\_param: the scan parameter
        - callback: register a callback for this action, ble\_cmd\_t: BLE\_CREATE\_SCAN

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv420bk_ble_start_scaning7uint8_t12ble_cmd_cb_t"></a>

<a id="_CPPv320bk_ble_start_scaning7uint8_t12ble_cmd_cb_t"></a> <a id="_CPPv220bk_ble_start_scaning7uint8_t12ble_cmd_cb_t"></a> <a id="bk_ble_start_scaning__uint8_t.ble_cmd_cb_t"></a> <a id="group__bk__ble__api__v1_1ga6ab237005c5a40cda9f44fa9776c1ce2"></a> ble\_err\_t bk\_ble\_start\_scaning(uint8\_t actv\_idx, ble\_cmd\_cb\_t callback)
:   Start a ble scan.

    **Attention**
    :   1.you must wait callback status, 0 mean success.

    **Attention**
    :   2.must used after bk\_ble\_create\_scaning

    **Attention**
    :   3.adv will report in ble\_notice\_cb\_t as BLE\_5\_REPORT\_ADV

    参数
    :   **\-** – actv\_idx: the index of activity

        - callback: register a callback for this action, ble\_cmd\_t: BLE\_START\_SCAN

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv423bk_ble_start_scaning_ex7uint8_t7uint8_t8uint16_t8uint16_t12ble_cmd_cb_t"></a>

<a id="_CPPv323bk_ble_start_scaning_ex7uint8_t7uint8_t8uint16_t8uint16_t12ble_cmd_cb_t"></a> <a id="_CPPv223bk_ble_start_scaning_ex7uint8_t7uint8_t8uint16_t8uint16_t12ble_cmd_cb_t"></a> <a id="bk_ble_start_scaning_ex__uint8_t.uint8_t.uint16_t.uint16_t.ble_cmd_cb_t"></a> <a id="group__bk__ble__api__v1_1gac42673372c1fce4d583e03135f099627"></a> ble\_err\_t bk\_ble\_start\_scaning\_ex(uint8\_t actv\_idx, uint8\_t filt\_duplicate, uint16\_t duration, uint16\_t period, ble\_cmd\_cb\_t callback)

<a id="_CPPv419bk_ble_stop_scaning7uint8_t12ble_cmd_cb_t"></a>

<a id="_CPPv319bk_ble_stop_scaning7uint8_t12ble_cmd_cb_t"></a> <a id="_CPPv219bk_ble_stop_scaning7uint8_t12ble_cmd_cb_t"></a> <a id="bk_ble_stop_scaning__uint8_t.ble_cmd_cb_t"></a> <a id="group__bk__ble__api__v1_1ga72336462591df1db0904e1a799eb7502"></a> ble\_err\_t bk\_ble\_stop\_scaning(uint8\_t actv\_idx, ble\_cmd\_cb\_t callback)
:   Stop the scan that has been started.

    **Attention**
    :   1.you must wait callback status, 0 mean success.

    **Attention**
    :   2.must used after bk\_ble\_start\_scaning

    参数
    :   **\-** – actv\_idx: the index of activity

        - callback: register a callback for this action, ble\_cmd\_t: BLE\_STOP\_SCAN

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv421bk_ble_delete_scaning7uint8_t12ble_cmd_cb_t"></a>

<a id="_CPPv321bk_ble_delete_scaning7uint8_t12ble_cmd_cb_t"></a> <a id="_CPPv221bk_ble_delete_scaning7uint8_t12ble_cmd_cb_t"></a> <a id="bk_ble_delete_scaning__uint8_t.ble_cmd_cb_t"></a> <a id="group__bk__ble__api__v1_1gad109f017d81f4712a6c934bf17bb3d51"></a> ble\_err\_t bk\_ble\_delete\_scaning(uint8\_t actv\_idx, ble\_cmd\_cb\_t callback)
:   Delete the scan that has been created.

    **Attention**
    :   1.you must wait callback status, 0 mean success.

    **Attention**
    :   2.must used after bk\_ble\_create\_scaning

    参数
    :   **\-** – actv\_idx: the index of activity

        - callback: register a callback for this action, ble\_cmd\_t: BLE\_DELETE\_SCAN

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv418bk_ble_create_init7uint8_tP16ble_conn_param_t12ble_cmd_cb_t"></a>

<a id="_CPPv318bk_ble_create_init7uint8_tP16ble_conn_param_t12ble_cmd_cb_t"></a> <a id="_CPPv218bk_ble_create_init7uint8_tP16ble_conn_param_t12ble_cmd_cb_t"></a> <a id="bk_ble_create_init__uint8_t.ble_conn_param_tP.ble_cmd_cb_t"></a> <a id="group__bk__ble__api__v1_1ga1b4daf940ba925f1023604f1f78a69e5"></a> ble\_err\_t bk\_ble\_create\_init(uint8\_t con\_idx, ble\_conn\_param\_t \*conn\_param, ble\_cmd\_cb\_t callback)
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
    :   **\-** – con\_idx: the index of connection

        - conn\_param: the connection parameter
        - callback: register a callback for this action, ble\_cmd\_t: BLE\_INIT\_CREATE

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv422bk_ble_init_start_conn7uint8_t12ble_cmd_cb_t"></a>

<a id="_CPPv322bk_ble_init_start_conn7uint8_t12ble_cmd_cb_t"></a> <a id="_CPPv222bk_ble_init_start_conn7uint8_t12ble_cmd_cb_t"></a> <a id="bk_ble_init_start_conn__uint8_t.ble_cmd_cb_t"></a> <a id="group__bk__ble__api__v1_1ga57dd321d593ba5ddeb24f821dc34bb96"></a> ble\_err\_t bk\_ble\_init\_start\_conn(uint8\_t con\_idx, ble\_cmd\_cb\_t callback)
:   Initiate a connection.

    **Attention**
    :   1.you must wait callback status, 0 mean success.

    **Attention**
    :   2.must used after bk\_ble\_create\_init

    **Attention**
    :   3.when connect result, will recv BLE\_5\_INIT\_CONNECT\_EVENT in ble\_notice\_cb\_t

    参数
    :   **\-** – con\_idx: the index of connection

        - callback: register a callback for this action, ble\_cmd\_t: BLE\_INIT\_START\_CONN

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv421bk_ble_init_stop_conn7uint8_t12ble_cmd_cb_t"></a>

<a id="_CPPv321bk_ble_init_stop_conn7uint8_t12ble_cmd_cb_t"></a> <a id="_CPPv221bk_ble_init_stop_conn7uint8_t12ble_cmd_cb_t"></a> <a id="bk_ble_init_stop_conn__uint8_t.ble_cmd_cb_t"></a> <a id="group__bk__ble__api__v1_1ga6c383277ac66a267565a8759a1fb37f3"></a> ble\_err\_t bk\_ble\_init\_stop\_conn(uint8\_t con\_idx, ble\_cmd\_cb\_t callback)
:   Stop a connection.

    **Attention**
    :   1.you must wait callback status, 0 mean success.

    **Attention**
    :   2.must used after bk\_ble\_init\_start\_conn

    参数
    :   **\-** – con\_idx: the index of connection

        - callback: register a callback for this action, ble\_cmd\_t: BLE\_INIT\_STOP\_CONN

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv432bk_ble_init_set_connect_dev_addr7uint8_tP9bd_addr_t7uint8_t"></a>

<a id="_CPPv332bk_ble_init_set_connect_dev_addr7uint8_tP9bd_addr_t7uint8_t"></a> <a id="_CPPv232bk_ble_init_set_connect_dev_addr7uint8_tP9bd_addr_t7uint8_t"></a> <a id="bk_ble_init_set_connect_dev_addr__uint8_t.bd_addr_tP.uint8_t"></a> <a id="group__bk__ble__api__v1_1ga5effaee518f4279b18480590f11492b2"></a> ble\_err\_t bk\_ble\_init\_set\_connect\_dev\_addr(uint8\_t connidx, bd\_addr\_t \*bdaddr, uint8\_t addr\_type)
:   Set the address of the device to be connected.

    **Attention**
    :   1.you must wait callback status, 0 mean success.

    **Attention**
    :   2.must used after bk\_ble\_create\_init

    **Attention**
    :   3.addr\_type must right, if wrong, cant connect

    参数
    :   **\-** – connidx: the index of connection

        - bdaddr: the address of the device to be connected
        - addr\_type: the address type of the device to be connected, 0: public 1: random

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv427bk_ble_create_periodic_sync7uint8_t12ble_cmd_cb_t"></a>

<a id="_CPPv327bk_ble_create_periodic_sync7uint8_t12ble_cmd_cb_t"></a> <a id="_CPPv227bk_ble_create_periodic_sync7uint8_t12ble_cmd_cb_t"></a> <a id="bk_ble_create_periodic_sync__uint8_t.ble_cmd_cb_t"></a> <a id="group__bk__ble__api__v1_1gae223c377f88d86cfd2c00924308a884b"></a> ble\_err\_t bk\_ble\_create\_periodic\_sync(uint8\_t actv\_idx, ble\_cmd\_cb\_t callback)

<a id="_CPPv426bk_ble_start_periodic_sync7uint8_tP20ble_periodic_param_t12ble_cmd_cb_t"></a>

<a id="_CPPv326bk_ble_start_periodic_sync7uint8_tP20ble_periodic_param_t12ble_cmd_cb_t"></a> <a id="_CPPv226bk_ble_start_periodic_sync7uint8_tP20ble_periodic_param_t12ble_cmd_cb_t"></a> <a id="bk_ble_start_periodic_sync__uint8_t.ble_periodic_param_tP.ble_cmd_cb_t"></a> <a id="group__bk__ble__api__v1_1ga6fc9e9c9de75337df138562176fa7ebf"></a> ble\_err\_t bk\_ble\_start\_periodic\_sync(uint8\_t actv\_idx, ble\_periodic\_param\_t \*param, ble\_cmd\_cb\_t callback)

<a id="_CPPv425bk_ble_stop_periodic_sync7uint8_t12ble_cmd_cb_t"></a>

<a id="_CPPv325bk_ble_stop_periodic_sync7uint8_t12ble_cmd_cb_t"></a> <a id="_CPPv225bk_ble_stop_periodic_sync7uint8_t12ble_cmd_cb_t"></a> <a id="bk_ble_stop_periodic_sync__uint8_t.ble_cmd_cb_t"></a> <a id="group__bk__ble__api__v1_1gaa96fa107f270ed0d7ada77fea3100dfa"></a> ble\_err\_t bk\_ble\_stop\_periodic\_sync(uint8\_t actv\_idx, ble\_cmd\_cb\_t callback)

<a id="_CPPv427bk_ble_delete_periodic_sync7uint8_t12ble_cmd_cb_t"></a>

<a id="_CPPv327bk_ble_delete_periodic_sync7uint8_t12ble_cmd_cb_t"></a> <a id="_CPPv227bk_ble_delete_periodic_sync7uint8_t12ble_cmd_cb_t"></a> <a id="bk_ble_delete_periodic_sync__uint8_t.ble_cmd_cb_t"></a> <a id="group__bk__ble__api__v1_1gabed96772625693380d83c81d4b704933"></a> ble\_err\_t bk\_ble\_delete\_periodic\_sync(uint8\_t actv\_idx, ble\_cmd\_cb\_t callback)

<a id="_CPPv431bk_ble_get_idle_actv_idx_handlev"></a>

<a id="_CPPv331bk_ble_get_idle_actv_idx_handlev"></a> <a id="_CPPv231bk_ble_get_idle_actv_idx_handlev"></a> <a id="bk_ble_get_idle_actv_idx_handle__void"></a> <a id="group__bk__ble__api__v1_1ga59256bec7de3df45f39570d5ef69d082"></a> uint8\_t bk\_ble\_get\_idle\_actv\_idx\_handle(void)
:   Get an idle activity.

    返回
    :   - xx: the idle activity’s index

<a id="_CPPv429bk_ble_get_max_actv_idx_countv"></a>

<a id="_CPPv329bk_ble_get_max_actv_idx_countv"></a> <a id="_CPPv229bk_ble_get_max_actv_idx_countv"></a> <a id="bk_ble_get_max_actv_idx_count__void"></a> <a id="group__bk__ble__api__v1_1gada33374d8018856640754918b9297e1d"></a> uint8\_t bk\_ble\_get\_max\_actv\_idx\_count(void)
:   Get the maximum count of activities.

    返回
    :   - xx: the maximum count of activities

<a id="_CPPv429bk_ble_get_max_conn_idx_countv"></a>

<a id="_CPPv329bk_ble_get_max_conn_idx_countv"></a> <a id="_CPPv229bk_ble_get_max_conn_idx_countv"></a> <a id="bk_ble_get_max_conn_idx_count__void"></a> <a id="group__bk__ble__api__v1_1ga5974f690de4bd01eba232d898fc21173"></a> uint8\_t bk\_ble\_get\_max\_conn\_idx\_count(void)
:   Get the maximum count of supported connections.

    返回
    :   - xx: the maximum count of supported connections

<a id="_CPPv431bk_ble_get_idle_conn_idx_handlev"></a>

<a id="_CPPv331bk_ble_get_idle_conn_idx_handlev"></a> <a id="_CPPv231bk_ble_get_idle_conn_idx_handlev"></a> <a id="bk_ble_get_idle_conn_idx_handle__void"></a> <a id="group__bk__ble__api__v1_1ga127748f4f5b2d17a8326ac63af539254"></a> uint8\_t bk\_ble\_get\_idle\_conn\_idx\_handle(void)
:   Get an idle connection activity.

    返回
    :   - xx: the idle connection activity’s index

<a id="_CPPv430bk_ble_find_conn_idx_from_addrP9bd_addr_t"></a>

<a id="_CPPv330bk_ble_find_conn_idx_from_addrP9bd_addr_t"></a> <a id="_CPPv230bk_ble_find_conn_idx_from_addrP9bd_addr_t"></a> <a id="bk_ble_find_conn_idx_from_addr__bd_addr_tP"></a> <a id="group__bk__ble__api__v1_1gacaf401abda1e95bf14f3e7b4b14e9d31"></a> uint8\_t bk\_ble\_find\_conn\_idx\_from\_addr(bd\_addr\_t \*connt\_addr)
:   Find the specific connection activity by address.

    参数
    :   **\-** – connt\_addr: the address of the connected device

    返回
    :   - xx: the index of the connection activity meeting the address

<a id="_CPPv424bk_ble_get_connect_stateP9bd_addr_t"></a>

<a id="_CPPv324bk_ble_get_connect_stateP9bd_addr_t"></a> <a id="_CPPv224bk_ble_get_connect_stateP9bd_addr_t"></a> <a id="bk_ble_get_connect_state__bd_addr_tP"></a> <a id="group__bk__ble__api__v1_1ga3048473f9c8c4c226eeb664e7e53a430"></a> uint8\_t bk\_ble\_get\_connect\_state(bd\_addr\_t \*connt\_addr)
:   Get the connection state of the specific device.

    参数
    :   **\-** – connt\_addr: the device’s address

    返回
    :   - 1: this device is connected
        - 0: this device is disconnected

<a id="_CPPv414bk_ble_get_macP7uint8_t"></a>

<a id="_CPPv314bk_ble_get_macP7uint8_t"></a> <a id="_CPPv214bk_ble_get_macP7uint8_t"></a> <a id="bk_ble_get_mac__uint8_tP"></a> <a id="group__bk__ble__api__v1_1ga7473327e2502d76d164da8dffd05c58c"></a> ble\_err\_t bk\_ble\_get\_mac(uint8\_t \*mac)
:   get ble mac addr,this api is deprecated,please use bk\_bluetooth\_get\_address

    **Attention**
    :   1\. return mac is 6 bytes.

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv422bk_ble_send_noti_value7uint8_t8uint32_tP7uint8_t8uint16_t8uint16_t"></a>

<a id="_CPPv322bk_ble_send_noti_value7uint8_t8uint32_tP7uint8_t8uint16_t8uint16_t"></a> <a id="_CPPv222bk_ble_send_noti_value7uint8_t8uint32_tP7uint8_t8uint16_t8uint16_t"></a> <a id="bk_ble_send_noti_value__uint8_t.uint32_t.uint8_tP.uint16_t.uint16_t"></a> <a id="group__bk__ble__api__v1_1ga743b3b5e1a8789a83099ab260115a6c7"></a> ble\_err\_t bk\_ble\_send\_noti\_value(uint8\_t con\_idx, uint32\_t len, uint8\_t \*buf, uint16\_t prf\_id, uint16\_t att\_idx)
:   As slaver, send a notification of an attribute’s value.

    参数
    :   **\-** – con\_idx: the index of connection

        - len: the length of attribute’s value
        - buf: attribute’s value
        - prf\_id: The id of the profile
        - att\_idx: The index of the attribute

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv421bk_ble_send_ind_value7uint8_t8uint32_tP7uint8_t8uint16_t8uint16_t"></a>

<a id="_CPPv321bk_ble_send_ind_value7uint8_t8uint32_tP7uint8_t8uint16_t8uint16_t"></a> <a id="_CPPv221bk_ble_send_ind_value7uint8_t8uint32_tP7uint8_t8uint16_t8uint16_t"></a> <a id="bk_ble_send_ind_value__uint8_t.uint32_t.uint8_tP.uint16_t.uint16_t"></a> <a id="group__bk__ble__api__v1_1ga1762c826416150f03376d283904c27a0"></a> ble\_err\_t bk\_ble\_send\_ind\_value(uint8\_t con\_idx, uint32\_t len, uint8\_t \*buf, uint16\_t prf\_id, uint16\_t att\_idx)
:   As slaver, send an indication of an attribute’s value.

    参数
    :   **\-** – con\_idx: the index of connection

        - len: the length of attribute’s value
        - buf: attribute’s value
        - prf\_id: The id of the profile
        - att\_idx: The index of the attribute

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv428bk_ble_reg_hci_recv_callback18ble_hci_to_host_cb18ble_hci_to_host_cb"></a>

<a id="_CPPv328bk_ble_reg_hci_recv_callback18ble_hci_to_host_cb18ble_hci_to_host_cb"></a> <a id="_CPPv228bk_ble_reg_hci_recv_callback18ble_hci_to_host_cb18ble_hci_to_host_cb"></a> <a id="bk_ble_reg_hci_recv_callback__ble_hci_to_host_cb.ble_hci_to_host_cb"></a> <a id="group__bk__ble__api__v1_1ga0f4a056d95139bcd0ab6e1da8c58c0a2"></a> ble\_err\_t bk\_ble\_reg\_hci\_recv\_callback(ble\_hci\_to\_host\_cb evt\_cb, ble\_hci\_to\_host\_cb acl\_cb)
:   reg hci recv callback

    **Attention**
    :   1\. you must call this after recv BLE\_5\_STACK\_OK evt !

    参数
    :   **\-** – evt\_cb: evt callback function

        - acl\_cb: acl callback function

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv424bk_ble_hci_to_controller7uint8_tP7uint8_t8uint16_t"></a>

<a id="_CPPv324bk_ble_hci_to_controller7uint8_tP7uint8_t8uint16_t"></a> <a id="_CPPv224bk_ble_hci_to_controller7uint8_tP7uint8_t8uint16_t"></a> <a id="bk_ble_hci_to_controller__uint8_t.uint8_tP.uint16_t"></a> <a id="group__bk__ble__api__v1_1ga3ec321524722d7477284ca9058c2140f"></a> ble\_err\_t bk\_ble\_hci\_to\_controller(uint8\_t type, uint8\_t \*buf, uint16\_t len)
:   send hci to controller.

    **Attention**
    :   1\. you must call this after bk\_ble\_reg\_hci\_recv\_callback !

    参数
    :   **\-** – type: see BK\_BLE\_HCI\_TYPE.

        - buf: payload
        - len: buf’s len

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed

<a id="_CPPv428bk_ble_hci_cmd_to_controllerP7uint8_t8uint16_t"></a>

<a id="_CPPv328bk_ble_hci_cmd_to_controllerP7uint8_t8uint16_t"></a> <a id="_CPPv228bk_ble_hci_cmd_to_controllerP7uint8_t8uint16_t"></a> <a id="bk_ble_hci_cmd_to_controller__uint8_tP.uint16_t"></a> <a id="group__bk__ble__api__v1_1ga1ef1a5b9e5879e45c132c00113c80210"></a> ble\_err\_t bk\_ble\_hci\_cmd\_to\_controller(uint8\_t \*buf, uint16\_t len)
:   send hci cmd to controller.

    **Attention**
    :   1\. you must call this after bk\_ble\_reg\_hci\_recv\_callback !

    参数
    :   **\-** – buf: payload

        - len: buf’s len

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed

<a id="_CPPv428bk_ble_hci_acl_to_controllerP7uint8_t8uint16_t"></a>

<a id="_CPPv328bk_ble_hci_acl_to_controllerP7uint8_t8uint16_t"></a> <a id="_CPPv228bk_ble_hci_acl_to_controllerP7uint8_t8uint16_t"></a> <a id="bk_ble_hci_acl_to_controller__uint8_tP.uint16_t"></a> <a id="group__bk__ble__api__v1_1ga42c06f4782cd0f9269ef723299c5656e"></a> ble\_err\_t bk\_ble\_hci\_acl\_to\_controller(uint8\_t \*buf, uint16\_t len)
:   send hci acl to controller.

    **Attention**
    :   1\. you must call this after bk\_ble\_reg\_hci\_recv\_callback !

    参数
    :   **\-** – buf: payload

        - len: buf’s len

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed

<a id="_CPPv425bk_ble_if_support_centralP7uint8_t"></a>

<a id="_CPPv325bk_ble_if_support_centralP7uint8_t"></a> <a id="_CPPv225bk_ble_if_support_centralP7uint8_t"></a> <a id="bk_ble_if_support_central__uint8_tP"></a> <a id="group__bk__ble__api__v1_1gab48622b9f97434399b0057e2d7fa7a4d"></a> uint8\_t bk\_ble\_if\_support\_central(uint8\_t \*count)

<a id="_CPPv432bk_ble_get_controller_stack_typev"></a>

<a id="_CPPv332bk_ble_get_controller_stack_typev"></a> <a id="_CPPv232bk_ble_get_controller_stack_typev"></a> <a id="bk_ble_get_controller_stack_type__void"></a> <a id="group__bk__ble__api__v1_1gad34af9c7166e9e393789e03c8c06a23f"></a> BK\_BLE\_CONTROLLER\_STACK\_TYPE bk\_ble\_get\_controller\_stack\_type(void)

<a id="_CPPv426bk_ble_get_host_stack_typev"></a>

<a id="_CPPv326bk_ble_get_host_stack_typev"></a> <a id="_CPPv226bk_ble_get_host_stack_typev"></a> <a id="bk_ble_get_host_stack_type__void"></a> <a id="group__bk__ble__api__v1_1gaaf9743eb06680f2d5fba04e6c2b526d0"></a> BK\_BLE\_HOST\_STACK\_TYPE bk\_ble\_get\_host\_stack\_type(void)

<a id="_CPPv420bk_ble_get_env_statev"></a>

<a id="_CPPv320bk_ble_get_env_statev"></a> <a id="_CPPv220bk_ble_get_env_statev"></a> <a id="bk_ble_get_env_state__void"></a> <a id="group__bk__ble__api__v1_1ga3a4ee0a3aaf16dac82123483730cdedb"></a> uint8\_t bk\_ble\_get\_env\_state(void)

<a id="_CPPv439bk_ble_register_app_sdp_charac_callback23app_sdp_charac_callback"></a>

<a id="_CPPv339bk_ble_register_app_sdp_charac_callback23app_sdp_charac_callback"></a> <a id="_CPPv239bk_ble_register_app_sdp_charac_callback23app_sdp_charac_callback"></a> <a id="bk_ble_register_app_sdp_charac_callback__app_sdp_charac_callback"></a> <a id="group__bk__ble__api__v1_1gae17451331278acf39079608c0f31cf9d"></a> void bk\_ble\_register\_app\_sdp\_charac\_callback(app\_sdp\_charac\_callback cb)

<a id="_CPPv439bk_ble_register_app_sdp_common_callback21app_sdp_comm_callback"></a>

<a id="_CPPv339bk_ble_register_app_sdp_common_callback21app_sdp_comm_callback"></a> <a id="_CPPv239bk_ble_register_app_sdp_common_callback21app_sdp_comm_callback"></a> <a id="bk_ble_register_app_sdp_common_callback__app_sdp_comm_callback"></a> <a id="group__bk__ble__api__v1_1ga1c7f8f3a73702fe8ecc729d960e08274"></a> void bk\_ble\_register\_app\_sdp\_common\_callback(app\_sdp\_comm\_callback cb)

<a id="_CPPv421bk_ble_gatt_write_ccc7uint8_t8uint16_t8uint16_t"></a>

<a id="_CPPv321bk_ble_gatt_write_ccc7uint8_t8uint16_t8uint16_t"></a> <a id="_CPPv221bk_ble_gatt_write_ccc7uint8_t8uint16_t8uint16_t"></a> <a id="bk_ble_gatt_write_ccc__uint8_t.uint16_t.uint16_t"></a> <a id="group__bk__ble__api__v1_1ga7eef50132e596d6d6e46cd48d44afbf4"></a> uint8\_t bk\_ble\_gatt\_write\_ccc(uint8\_t con\_idx, uint16\_t ccc\_handle, uint16\_t ccc\_value)
:   As master, enable notification or indication.

    参数
    :   **\-** – con\_idx: the index of connection

        - ccc\_handle: the handle of Client Characteristic Configuration descriptor
        - ccc\_value: descriptor value, 0x01 means notification ,0x02 means indication

    返回
    :   - 0: succeed
        - others: errors.

<a id="_CPPv423bk_ble_gatt_write_value7uint8_t8uint16_t8uint16_tP7uint8_t"></a>

<a id="_CPPv323bk_ble_gatt_write_value7uint8_t8uint16_t8uint16_tP7uint8_t"></a> <a id="_CPPv223bk_ble_gatt_write_value7uint8_t8uint16_t8uint16_tP7uint8_t"></a> <a id="bk_ble_gatt_write_value__uint8_t.uint16_t.uint16_t.uint8_tP"></a> <a id="group__bk__ble__api__v1_1ga5d8594b965d7972b27469437d1fafb54"></a> ble\_err\_t bk\_ble\_gatt\_write\_value(uint8\_t con\_idx, uint16\_t att\_handle, uint16\_t len, uint8\_t \*data)
:   As master, write attribute value.

    参数
    :   **\-** – con\_idx: the index of connection

        - att\_handle: the handle of attribute value
        - data: value data
        - len: the length of attribute value

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: fail

<a id="_CPPv426bk_ble_read_response_value7uint8_t8uint32_tP7uint8_t8uint16_t8uint16_t"></a>

<a id="_CPPv326bk_ble_read_response_value7uint8_t8uint32_tP7uint8_t8uint16_t8uint16_t"></a> <a id="_CPPv226bk_ble_read_response_value7uint8_t8uint32_tP7uint8_t8uint16_t8uint16_t"></a> <a id="bk_ble_read_response_value__uint8_t.uint32_t.uint8_tP.uint16_t.uint16_t"></a> <a id="group__bk__ble__api__v1_1ga891545eb2345032de540840166c483a8"></a> ble\_err\_t bk\_ble\_read\_response\_value(uint8\_t con\_idx, uint32\_t len, uint8\_t \*buf, uint16\_t prf\_id, uint16\_t att\_idx)
:   As slaver, send response value.

    参数
    :   **\-** – con\_idx: the idx of app connections

        - len: the length of attribute’s value
        - buf: attribute’s value
        - prf\_id: The id of the profile
        - att\_idx: The index of the attribute

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: fail

<a id="_CPPv425bk_ble_sec_send_auth_mode7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t"></a>

<a id="_CPPv325bk_ble_sec_send_auth_mode7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t"></a> <a id="_CPPv225bk_ble_sec_send_auth_mode7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t"></a> <a id="bk_ble_sec_send_auth_mode__uint8_t.uint8_t.uint8_t.uint8_t.uint8_t"></a> <a id="group__bk__ble__api__v1_1ga3b406cbb6440cbff728fb52de36f91e6"></a> ble\_err\_t bk\_ble\_sec\_send\_auth\_mode(uint8\_t con\_idx, uint8\_t mode, uint8\_t iocap, uint8\_t sec\_req, uint8\_t oob)
:   As master, configure attribute value.

    参数
    :   **\-** – con\_idx: the index of connection

        - mode: authentication features
        - iocap: IO Capability Values
        - sec\_req: Security Defines
        - oob: OOB Data Present Flag Values

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: fail

<a id="_CPPv429bk_ble_sec_send_auth_mode_ext7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t"></a>

<a id="_CPPv329bk_ble_sec_send_auth_mode_ext7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t"></a> <a id="_CPPv229bk_ble_sec_send_auth_mode_ext7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t"></a> <a id="bk_ble_sec_send_auth_mode_ext__uint8_t.uint8_t.uint8_t.uint8_t.uint8_t.uint8_t.uint8_t"></a> <a id="group__bk__ble__api__v1_1ga2e5becd15200d2f15376b7f58754963b"></a> ble\_err\_t bk\_ble\_sec\_send\_auth\_mode\_ext(uint8\_t con\_idx, uint8\_t mode, uint8\_t iocap, uint8\_t sec\_req, uint8\_t oob, uint8\_t initiator\_key\_distr, uint8\_t responder\_key\_distr)
:   As master, configure auth mode param.

    参数
    :   **\-** – con\_idx: the index of connection

        - mode: authentication features
        - iocap: IO Capability Values
        - sec\_req: Security Defines
        - oob: OOB Data Present Flag Values
        - initiator\_key\_distr: init key distr, see gap\_key\_distr
        - responder\_key\_distr: resp key distr, see gap\_key\_distr

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: fail

<a id="_CPPv411bk_ble_initv"></a>

<a id="_CPPv311bk_ble_initv"></a> <a id="_CPPv211bk_ble_initv"></a> <a id="bk_ble_init__void"></a> <a id="group__bk__ble__api__v1_1ga6e2fb78d12d18f8adfa8221a4dc9d4b4"></a> ble\_err\_t bk\_ble\_init(void)
:   ble init function,this api is deprecated,please use bk\_bluetooth\_init.

    Param

<a id="_CPPv413bk_ble_deinitv"></a>

<a id="_CPPv313bk_ble_deinitv"></a> <a id="_CPPv213bk_ble_deinitv"></a> <a id="bk_ble_deinit__void"></a> <a id="group__bk__ble__api__v1_1gaf520ce1148fdad9b4f3eb3841ef07091"></a> ble\_err\_t bk\_ble\_deinit(void)
:   ble deinit function,this api is deprecated,please use bk\_bluetooth\_deinit.

    Param

<a id="_CPPv421bk_ble_delete_serviceP13bk_ble_db_cfg"></a>

<a id="_CPPv321bk_ble_delete_serviceP13bk_ble_db_cfg"></a> <a id="_CPPv221bk_ble_delete_serviceP13bk_ble_db_cfg"></a> <a id="bk_ble_delete_service__bk_ble_db_cfgP"></a> <a id="group__bk__ble__api__v1_1gad0471e4a212ec50d89da0237ca07c3fe"></a> ble\_err\_t bk\_ble\_delete\_service(struct bk\_ble\_db\_cfg \*ble\_db\_cfg)
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
    :   **\-** – ble\_db\_cfg: service param

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv415bk_ble_att_read7uint8_t8uint16_t"></a>

<a id="_CPPv315bk_ble_att_read7uint8_t8uint16_t"></a> <a id="_CPPv215bk_ble_att_read7uint8_t8uint16_t"></a> <a id="bk_ble_att_read__uint8_t.uint16_t"></a> <a id="group__bk__ble__api__v1_1ga2dff3792fbbce670c5eb9bab35a8a68f"></a> ble\_err\_t bk\_ble\_att\_read(uint8\_t con\_idx, uint16\_t att\_handle)
:   As master, read attribute value, the result is reported in the callback registered through bk\_ble\_register\_app\_sdp\_charac\_callback.

    参数
    :   **\-** – con\_idx: the index of connection

        - att\_handle: the handle of attribute value

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: fail

<a id="_CPPv418bk_ble_create_bond7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t"></a>

<a id="_CPPv318bk_ble_create_bond7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t"></a> <a id="_CPPv218bk_ble_create_bond7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t"></a> <a id="bk_ble_create_bond__uint8_t.uint8_t.uint8_t.uint8_t.uint8_t"></a> <a id="group__bk__ble__api__v1_1gac786e0c3ad011349f19ccfc337037ce9"></a> ble\_err\_t bk\_ble\_create\_bond(uint8\_t con\_idx, uint8\_t auth, uint8\_t iocap, uint8\_t sec\_req, uint8\_t oob)
:   start authentication the link

    **Attention**
    :   if the link has not been bonded, it will trigger pairing, otherwise it will trigger the link encryption.

    参数
    :   **\-** – con\_idx: the index of connection

        - auth: authentication features(see enum gap\_auth)
        - iocap: IO Capability Values(see enum bk\_ble\_gap\_io\_cap)
        - sec\_req: Security Defines(see enum gap\_sec\_req)
        - oob: OOB Data Present Flag Values(see enum gap\_oob)

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: fail

<a id="_CPPv422bk_ble_create_bond_ext7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t"></a>

<a id="_CPPv322bk_ble_create_bond_ext7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t"></a> <a id="_CPPv222bk_ble_create_bond_ext7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t7uint8_t"></a> <a id="bk_ble_create_bond_ext__uint8_t.uint8_t.uint8_t.uint8_t.uint8_t.uint8_t.uint8_t"></a> <a id="group__bk__ble__api__v1_1ga2427a2bc27b9a7472534821dd603cf34"></a> ble\_err\_t bk\_ble\_create\_bond\_ext(uint8\_t con\_idx, uint8\_t auth, uint8\_t iocap, uint8\_t sec\_req, uint8\_t oob, uint8\_t initiator\_key\_distr, uint8\_t responder\_key\_distr)
:   create bond

    **Attention**
    :   if the link has not been bonded, it will trigger pairing, otherwise it will trigger the link encryption.

    参数
    :   **\-** – con\_idx: the index of connection

        - auth: authentication features(see enum gap\_auth)
        - iocap: IO Capability Values(see enum bk\_ble\_gap\_io\_cap)
        - sec\_req: Security Defines(see enum gap\_sec\_req)
        - oob: OOB Data Present Flag Values(see enum gap\_oob)
        - initiator\_key\_distr: init key distr, see gap\_key\_distr
        - responder\_key\_distr: resp key distr, see gap\_key\_distr

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: fail

<a id="_CPPv419bk_ble_passkey_send7uint8_t7uint8_t8uint32_t"></a>

<a id="_CPPv319bk_ble_passkey_send7uint8_t7uint8_t8uint32_t"></a> <a id="_CPPv219bk_ble_passkey_send7uint8_t7uint8_t8uint32_t"></a> <a id="bk_ble_passkey_send__uint8_t.uint8_t.uint32_t"></a> <a id="group__bk__ble__api__v1_1gad3908431a386c015571bc53cdcc53b8d"></a> ble\_err\_t bk\_ble\_passkey\_send(uint8\_t con\_idx, uint8\_t accept, uint32\_t passkey)
:   send passkey when pairing

    参数
    :   **\-** – con\_idx: the index of connection

        - accept: accept pair
        - passkey: the num that peer need to input or local need to input

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: fail

<a id="_CPPv426bk_ble_number_compare_send7uint8_t7uint8_t"></a>

<a id="_CPPv326bk_ble_number_compare_send7uint8_t7uint8_t"></a> <a id="_CPPv226bk_ble_number_compare_send7uint8_t7uint8_t"></a> <a id="bk_ble_number_compare_send__uint8_t.uint8_t"></a> <a id="group__bk__ble__api__v1_1ga5d75e7894809d173a6d4c85239735cc5"></a> ble\_err\_t bk\_ble\_number\_compare\_send(uint8\_t con\_idx, uint8\_t accept)
:   send number compare accept when pairing

    参数
    :   **\-** – con\_idx: the index of connection

        - accept: accept pair

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: fail

<a id="_CPPv416bk_ble_read_rssi7uint8_t"></a>

<a id="_CPPv316bk_ble_read_rssi7uint8_t"></a> <a id="_CPPv216bk_ble_read_rssi7uint8_t"></a> <a id="bk_ble_read_rssi__uint8_t"></a> <a id="group__bk__ble__api__v1_1ga826f2819108947636cd1f673a930f85f"></a> ble\_err\_t bk\_ble\_read\_rssi(uint8\_t conn\_idx)
:   Read the rssi of connection device. The result will report in callback registered through bk\_ble\_set\_notice\_cb with evt BLE\_5\_READ\_RSSI\_CMPL\_EVENT, and param is ble\_read\_rssi\_rsp\_t \*.

    User example:

    ```
    bk_ble_read_rssi(conn_idx);
    ```

    **Attention**
    :   1.must used after after connected

    参数
    :   **\-** – conn\_idx: the index of connection device

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv430bk_ble_config_local_appearance8uint16_t"></a>

<a id="_CPPv330bk_ble_config_local_appearance8uint16_t"></a> <a id="_CPPv230bk_ble_config_local_appearance8uint16_t"></a> <a id="bk_ble_config_local_appearance__uint16_t"></a> <a id="group__bk__ble__api__v1_1ga6275e926ec40b18a657121c793306011"></a> ble\_err\_t bk\_ble\_config\_local\_appearance(uint16\_t appearance)
:   set local gap appearance

    参数
    :   **appearance** – **\[in\]** \- External appearance value, these values are defined by the Bluetooth SIG, please refer to <https://specificationrefs.bluetooth.com/assigned-values/Appearance%20Values.pdf>

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: other errors.

<a id="_CPPv431bk_ble_discover_primary_service7uint8_t8uint16_t8uint16_t"></a>

<a id="_CPPv331bk_ble_discover_primary_service7uint8_t8uint16_t8uint16_t"></a> <a id="_CPPv231bk_ble_discover_primary_service7uint8_t8uint16_t8uint16_t"></a> <a id="bk_ble_discover_primary_service__uint8_t.uint16_t.uint16_t"></a> <a id="group__bk__ble__api__v1_1ga6a47d52c21bd14dca65e649a803ada8c"></a> ble\_err\_t bk\_ble\_discover\_primary\_service(uint8\_t conn\_id, uint16\_t sh, uint16\_t eh)
:   Discover peer primary service. The result is report in the callback registered through bk\_ble\_register\_app\_sdp\_common\_callback, and evt is MST\_TYPE\_DISCOVER\_PRI\_SERVICE\_RSP. When completed, callback will report MST\_TYPE\_DISCOVER\_COMPLETED with ble\_descover\_complete\_inf and MST\_TYPE\_DISCOVER\_PRI\_SERVICE\_RSP.

    参数
    :   **\-** – sh: att start handle

        - eh: att end handle

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: fail

<a id="_CPPv439bk_ble_discover_primary_service_by_uuid7uint8_t8uint16_t8uint16_t8uint16_t"></a>

<a id="_CPPv339bk_ble_discover_primary_service_by_uuid7uint8_t8uint16_t8uint16_t8uint16_t"></a> <a id="_CPPv239bk_ble_discover_primary_service_by_uuid7uint8_t8uint16_t8uint16_t8uint16_t"></a> <a id="bk_ble_discover_primary_service_by_uuid__uint8_t.uint16_t.uint16_t.uint16_t"></a> <a id="group__bk__ble__api__v1_1gacd90936a4c76203ced8af706c795f83e"></a> ble\_err\_t bk\_ble\_discover\_primary\_service\_by\_uuid(uint8\_t conn\_id, uint16\_t sh, uint16\_t eh, uint16\_t uuid)
:   Discover peer primary service. The result is report in the callback registered through bk\_ble\_register\_app\_sdp\_common\_callback, and evt is MST\_TYPE\_DISCOVER\_PRI\_SERVICE\_BY\_UUID\_RSP. When completed, callback will report MST\_TYPE\_DISCOVER\_COMPLETED with ble\_descover\_complete\_inf and MST\_TYPE\_DISCOVER\_PRI\_SERVICE\_BY\_UUID\_RSP.

    参数
    :   **\-** – sh: att start handle

        - eh: att end handle

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed

<a id="_CPPv442bk_ble_discover_primary_service_by_128uuid7uint8_t8uint16_t8uint16_tP7uint8_t"></a>

<a id="_CPPv342bk_ble_discover_primary_service_by_128uuid7uint8_t8uint16_t8uint16_tP7uint8_t"></a> <a id="_CPPv242bk_ble_discover_primary_service_by_128uuid7uint8_t8uint16_t8uint16_tP7uint8_t"></a> <a id="bk_ble_discover_primary_service_by_128uuid__uint8_t.uint16_t.uint16_t.uint8_tP"></a> <a id="group__bk__ble__api__v1_1gaa0f48fe52635ed8291f4bb8f20f3c1e8"></a> ble\_err\_t bk\_ble\_discover\_primary\_service\_by\_128uuid(uint8\_t conn\_id, uint16\_t sh, uint16\_t eh, uint8\_t \*uuid)
:   Discover peer primary service. The result is report in the callback registered through bk\_ble\_register\_app\_sdp\_common\_callback, and evt is MST\_TYPE\_DISCOVER\_PRI\_SERVICE\_BY\_128\_UUID\_RSP. When completed, callback will report MST\_TYPE\_DISCOVER\_COMPLETED with ble\_descover\_complete\_inf and MST\_TYPE\_DISCOVER\_PRI\_SERVICE\_BY\_128\_UUID\_RSP. bk\_ble\_read\_rssi(conn\_idx);.

    参数
    :   **\-** – conn\_id: the index of connection

        - sh: att start handle
        - eh: att end handle
        - uuid: uuid that service need to find in 128bits

    返回
    :   - others: fail

<a id="_CPPv430bk_ble_discover_characteristic7uint8_t8uint16_t8uint16_t"></a>

<a id="_CPPv330bk_ble_discover_characteristic7uint8_t8uint16_t8uint16_t"></a> <a id="_CPPv230bk_ble_discover_characteristic7uint8_t8uint16_t8uint16_t"></a> <a id="bk_ble_discover_characteristic__uint8_t.uint16_t.uint16_t"></a> <a id="group__bk__ble__api__v1_1ga114d6592e9c897955970d3f0d01d20f0"></a> ble\_err\_t bk\_ble\_discover\_characteristic(uint8\_t conn\_id, uint16\_t sh, uint16\_t eh)
:   Discover peer characteristic. The result is report in the callback registered through bk\_ble\_register\_app\_sdp\_common\_callback, and evt is MST\_TYPE\_DISCOVER\_CHAR\_RSP. When completed, callback will report MST\_TYPE\_DISCOVER\_COMPLETED with ble\_descover\_complete\_inf and MST\_TYPE\_DISCOVER\_CHAR\_RSP.

    参数
    :   **\-** – conn\_id: the index of connection

        - sh: att start handle
        - eh: att end handle

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: fail

<a id="_CPPv438bk_ble_discover_characteristic_by_uuid7uint8_t8uint16_t8uint16_t8uint16_t"></a>

<a id="_CPPv338bk_ble_discover_characteristic_by_uuid7uint8_t8uint16_t8uint16_t8uint16_t"></a> <a id="_CPPv238bk_ble_discover_characteristic_by_uuid7uint8_t8uint16_t8uint16_t8uint16_t"></a> <a id="bk_ble_discover_characteristic_by_uuid__uint8_t.uint16_t.uint16_t.uint16_t"></a> <a id="group__bk__ble__api__v1_1ga7b09af5e20509e41b42e467af475cd49"></a> ble\_err\_t bk\_ble\_discover\_characteristic\_by\_uuid(uint8\_t conn\_id, uint16\_t sh, uint16\_t eh, uint16\_t uuid)
:   Discover peer characteristic. The result is report in the callback registered through bk\_ble\_register\_app\_sdp\_common\_callback, and evt is MST\_TYPE\_DISCOVER\_CHAR\_BY\_UUID\_RSP. When completed, callback will report MST\_TYPE\_DISCOVER\_COMPLETED with ble\_descover\_complete\_inf and MST\_TYPE\_DISCOVER\_CHAR\_BY\_UUID\_RSP.

    参数
    :   **\-** – conn\_id: the index of connection

        - sh: att start handle
        - eh: att end handle

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: fail

<a id="_CPPv441bk_ble_discover_characteristic_by_128uuid7uint8_t8uint16_t8uint16_tP7uint8_t"></a>

<a id="_CPPv341bk_ble_discover_characteristic_by_128uuid7uint8_t8uint16_t8uint16_tP7uint8_t"></a> <a id="_CPPv241bk_ble_discover_characteristic_by_128uuid7uint8_t8uint16_t8uint16_tP7uint8_t"></a> <a id="bk_ble_discover_characteristic_by_128uuid__uint8_t.uint16_t.uint16_t.uint8_tP"></a> <a id="group__bk__ble__api__v1_1ga1416ce651a3eb33f5f711facf79deac6"></a> ble\_err\_t bk\_ble\_discover\_characteristic\_by\_128uuid(uint8\_t conn\_id, uint16\_t sh, uint16\_t eh, uint8\_t \*uuid)
:   Discover peer characteristic. The result is report in the callback registered through bk\_ble\_register\_app\_sdp\_common\_callback, and evt is MST\_TYPE\_DISCOVER\_CHAR\_BY\_128\_UUID\_RSP. When completed, callback will report MST\_TYPE\_DISCOVER\_COMPLETED with ble\_descover\_complete\_inf and MST\_TYPE\_DISCOVER\_CHAR\_BY\_128\_UUID\_RSP.

    参数
    :   **\-** – conn\_id: the index of connection

        - sh: att start handle
        - eh: att end handle

    返回
    :   - others: fail

<a id="_CPPv441bk_ble_discover_characteristic_descriptor7uint8_t8uint16_t8uint16_t"></a>

<a id="_CPPv341bk_ble_discover_characteristic_descriptor7uint8_t8uint16_t8uint16_t"></a> <a id="_CPPv241bk_ble_discover_characteristic_descriptor7uint8_t8uint16_t8uint16_t"></a> <a id="bk_ble_discover_characteristic_descriptor__uint8_t.uint16_t.uint16_t"></a> <a id="group__bk__ble__api__v1_1ga70cb2d7506fbf5dc80bbdb66bfdd0919"></a> ble\_err\_t bk\_ble\_discover\_characteristic\_descriptor(uint8\_t conn\_id, uint16\_t sh, uint16\_t eh)
:   Discover peer characteristic descriptor. The result is report in the callback registered through bk\_ble\_register\_app\_sdp\_common\_callback, and evt is MST\_TYPE\_DISCOVER\_CHAR\_DESC. When completed, callback will report MST\_TYPE\_DISCOVER\_COMPLETED with ble\_descover\_complete\_inf and MST\_TYPE\_DISCOVER\_CHAR\_DESC.

    参数
    :   **\-** – conn\_id: the index of connection

        - sh: att start handle
        - eh: att end handle

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: fail

<a id="_CPPv417bk_ble_gattc_read7uint8_t8uint16_t8uint16_t"></a>

<a id="_CPPv317bk_ble_gattc_read7uint8_t8uint16_t8uint16_t"></a> <a id="_CPPv217bk_ble_gattc_read7uint8_t8uint16_t8uint16_t"></a> <a id="bk_ble_gattc_read__uint8_t.uint16_t.uint16_t"></a> <a id="group__bk__ble__api__v1_1ga59559466bbfdc422e1dc9d1a767f8bad"></a> ble\_err\_t bk\_ble\_gattc\_read(uint8\_t con\_idx, uint16\_t att\_handle, uint16\_t offset)
:   As master, read attribute value, the result is reported in the callback registered through bk\_ble\_register\_app\_sdp\_charac\_callback.

    参数
    :   **\-** – con\_idx: the index of connection

        - att\_handle: the handle of attribute value
        - offset: the offset of attribute value

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: fail

<a id="_CPPv425bk_ble_gattc_read_by_uuid7uint8_t8uint16_t8uint16_tP7uint8_t7uint8_t"></a>

<a id="_CPPv325bk_ble_gattc_read_by_uuid7uint8_t8uint16_t8uint16_tP7uint8_t7uint8_t"></a> <a id="_CPPv225bk_ble_gattc_read_by_uuid7uint8_t8uint16_t8uint16_tP7uint8_t7uint8_t"></a> <a id="bk_ble_gattc_read_by_uuid__uint8_t.uint16_t.uint16_t.uint8_tP.uint8_t"></a> <a id="group__bk__ble__api__v1_1ga9cd028a6be13887d30b44d507e70ccf9"></a> ble\_err\_t bk\_ble\_gattc\_read\_by\_uuid(uint8\_t conn\_id, uint16\_t sh, uint16\_t eh, uint8\_t \*uuid, uint8\_t uuid\_len)
:   As master, read attribute value, the result is reported in the callback registered through bk\_ble\_register\_app\_sdp\_charac\_callback.

    参数
    :   **\-** – con\_idx: the index of connection

        - sh: the start handle of attribute
        - eh: the end handle of attribute
        - uuid: uuid
        - uuid\_len: uuid len, may be 2 or 16

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: fail

<a id="_CPPv418bk_ble_gattc_write7uint8_t8uint16_tP7uint8_t8uint16_t7uint8_t"></a>

<a id="_CPPv318bk_ble_gattc_write7uint8_t8uint16_tP7uint8_t8uint16_t7uint8_t"></a> <a id="_CPPv218bk_ble_gattc_write7uint8_t8uint16_tP7uint8_t8uint16_t7uint8_t"></a> <a id="bk_ble_gattc_write__uint8_t.uint16_t.uint8_tP.uint16_t.uint8_t"></a> <a id="group__bk__ble__api__v1_1ga717111fc7918c6d76dda6122a15d76eb"></a> ble\_err\_t bk\_ble\_gattc\_write(uint8\_t con\_idx, uint16\_t att\_handle, uint8\_t \*data, uint16\_t len, uint8\_t is\_write\_cmd)
:   As master, write attribute value.

    参数
    :   **\-** – con\_idx: the index of connection

        - att\_handle: the handle of attribute value
        - data: value data
        - len: the length of attribute value
        - is\_write\_cmd: when true, will trigger write cmd, otherwise write req.

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: fail

<a id="_CPPv423bk_ble_clear_white_listv"></a>

<a id="_CPPv323bk_ble_clear_white_listv"></a> <a id="_CPPv223bk_ble_clear_white_listv"></a> <a id="bk_ble_clear_white_list__void"></a> <a id="group__bk__ble__api__v1_1ga2a023a365afa7b2ad3eb5818540ad18e"></a> ble\_err\_t bk\_ble\_clear\_white\_list(void)
:   clear the white list.

    Param

<a id="_CPPv432bk_ble_add_devices_to_while_listP9bd_addr_t7uint8_t"></a>

<a id="_CPPv332bk_ble_add_devices_to_while_listP9bd_addr_t7uint8_t"></a> <a id="_CPPv232bk_ble_add_devices_to_while_listP9bd_addr_t7uint8_t"></a> <a id="bk_ble_add_devices_to_while_list__bd_addr_tP.uint8_t"></a> <a id="group__bk__ble__api__v1_1ga97257f56c5410ec86f49bb1d521301d1"></a> ble\_err\_t bk\_ble\_add\_devices\_to\_while\_list(bd\_addr\_t \*addr, uint8\_t addr\_type)
:   Add a device to the while list.

    参数
    :   **\-** – addr: the address of the device.

        - addr\_type: the type of the address, 0 is public address, 1 is random address.

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: fail

<a id="_CPPv437bk_ble_remove_devices_from_while_listP9bd_addr_t7uint8_t"></a>

<a id="_CPPv337bk_ble_remove_devices_from_while_listP9bd_addr_t7uint8_t"></a> <a id="_CPPv237bk_ble_remove_devices_from_while_listP9bd_addr_t7uint8_t"></a> <a id="bk_ble_remove_devices_from_while_list__bd_addr_tP.uint8_t"></a> <a id="group__bk__ble__api__v1_1gaad8714efc7d2602444a7fc1edbb8d08e"></a> ble\_err\_t bk\_ble\_remove\_devices\_from\_while\_list(bd\_addr\_t \*addr, uint8\_t addr\_type)
:   Remove a device from the while list.

    参数
    :   **\-** – addr: the address of the device.

        - addr\_type: the type of the address, 0 is public address, 1 is random address.

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: fail

<a id="_CPPv418bk_ble_set_tx_powr7uint8_t"></a>

<a id="_CPPv318bk_ble_set_tx_powr7uint8_t"></a> <a id="_CPPv218bk_ble_set_tx_powr7uint8_t"></a> <a id="bk_ble_set_tx_powr__uint8_t"></a> <a id="group__bk__ble__api__v1_1ga9bef875c2e2c689a02317d14cdcca282"></a> ble\_err\_t bk\_ble\_set\_tx\_powr(uint8\_t pwr\_gain)
:   Set tx power.

    参数
    :   **\-** – pwr\_gain: tx power gain

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: fail

<a id="_CPPv434bk_ble_enable_uart_controller_only7uint8_tP39bluetooth_uart_controller_only_config_t"></a>

<a id="_CPPv334bk_ble_enable_uart_controller_only7uint8_tP39bluetooth_uart_controller_only_config_t"></a> <a id="_CPPv234bk_ble_enable_uart_controller_only7uint8_tP39bluetooth_uart_controller_only_config_t"></a> <a id="bk_ble_enable_uart_controller_only__uint8_t.bluetooth_uart_controller_only_config_tP"></a> <a id="group__bk__ble__api__v1_1ga7a8ca6a8320054cdc03099d0a2c172d2"></a> ble\_err\_t bk\_ble\_enable\_uart\_controller\_only(uint8\_t enable, bluetooth\_uart\_controller\_only\_config\_t \*config)
:   enable controller only by uart.

    参数
    :   **\-** – enable: enable or disable.

        - config: uart config

    返回
    :   - BK\_ERR\_BLE\_SUCCESS: succeed
        - others: fail
