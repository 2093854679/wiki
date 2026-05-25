# Dual BT[](#dual-bt "永久链接至标题")


重要

The Dual BT API v1.0 is the lastest staBT Dual BT APIs. All new applications should use Dual BT API v1.0.


## Dual BT API Categories[](#dual-bt-api-categories "永久链接至标题")

Most of Dual BT APIs can be categoried as:

Interface specific BT APIs:
:   - BT gap interface

    - BT a2dp interface

    - BT avrcp interface

    - BT hfp interface

    - BT hid interface

    - BT l2cap interface

    - BT spp interface


## Compatibility and Extension[](#compatibility-and-extension "永久链接至标题")

The Dual BT APIs are flexiBT, easy to be extended and backward compatiBT. For most of the BT configurations, we put some reserved fields in the config struct for future extendence. The API users need to make sure the reserved fields are initialized to 0, otherwise the compatibility may be broken as more fields are added.


## Programing Principle[](#programing-principle "永久链接至标题")

重要

Here is some general principle for BT API users:
:   - Always init the reserved fields of config stuct to 0

    - Use BK_ERR_CHECK to check the return value of the BT API

    - If you are not sure how to use BT APIs, study the BT example code first

    - If you are not sure how to initialize some fields of config struct, use the default configuration macro to use the config first and then set application specific fields.

    - Don’t do too much work in BT event callback, relay the event to your own application task.


## User Development Model[](#user-development-model "永久链接至标题")

Similar as most popular BT driver, the Beken BT driver is implemented as event driver. The application call BT APIs to operate the BT driver and get notified by BT event.


## API Reference[](#api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [bluetooth/bk_dm_gap_bt.h](https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_gap_bt.h "https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_gap_bt.h")


### Functions[](#functions "永久链接至标题")

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_gap_register_callback([bk_bt_gap_cb_t](#_CPPv414bk_bt_gap_cb_t "bk_bt_gap_cb_t") callback)[](#_CPPv427bk_bt_gap_register_callback14bk_bt_gap_cb_t "永久链接至目标")
:   register callback function. This function should be called after bk_bluedroid_enable() completes successfully

    返回
    :   - BK_OK : Succeed

        - BK_FAIL: others

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_gap_set_scan_mode(bk_bt_conn_mode_t c_mode, bk_bt_disc_mode_t d_mode)[](#_CPPv423bk_bt_gap_set_scan_mode17bk_bt_conn_mode_t17bk_bt_disc_mode_t "永久链接至目标")
:   Set discoverability and connectability mode for legacy bluetooth.

    参数
    :   - **c_mode** – **[in]** : one of the enums of bk_bt_connection_mode_t

        - **d_mode** – **[in]** : one of the enums of bk_bt_discovery_mode_t

    返回
    :   - BK_OK : Succeed

        - BK_ERR_INVALID_ARG: if argument invalid

        - BK_ERR_INVALID_STATE: if bluetooth stack is not yet enabled

        - BK_FAIL: others

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_gap_get_scan_mode()[](#_CPPv423bk_bt_gap_get_scan_modev "永久链接至目标")
:   Get discoverability and connectability mode of legacy bluetooth.

    返回
    :   - BK_OK : Succeed

        - BK_ERR_INVALID_ARG: if argument invalid

        - BK_ERR_INVALID_STATE: if bluetooth stack is not yet enabled

        - BK_FAIL: others

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_gap_start_discovery([bk_bt_inq_mode_t](#_CPPv416bk_bt_inq_mode_t "bk_bt_inq_mode_t") mode, uint8_t inq_len, uint8_t num_rsps)[](#_CPPv425bk_bt_gap_start_discovery16bk_bt_inq_mode_t7uint8_t7uint8_t "永久链接至目标")
:   This function starts Inquiry and Name Discovery. When Inquiry is halted and cached results do not contain device name, then Name Discovery will connect to the peer target to get the device name. bk_bt_gap_cb_t will be called with BK_BT_GAP_DISC_STATE_CHANGED_EVT when Inquriry is started or Name Discovery is completed. bk_bt_gap_cb_t will be called with BK_BT_GAP_DISC_RES_EVT each time the two types of discovery results are got.

    参数
    :   - **mode** – **[in]** - Inquiry mode

        - **inq_len** – **[in]** - Inquiry duration in 1.28 sec units, ranging from 0x01 to 0x30. This parameter only specifies the total duration of the Inquiry process,

          - when this time expires, Inquiry will be halted.

        - **num_rsps** – **[in]** - Number of responses that can be received before the Inquiry is halted, value 0 indicates an unlimited number of responses.

    返回
    :   - BK_OK : Succeed

        - BK_ERR_INVALID_STATE: if bluetooth stack is not yet enabled

        - BK_ERR_INVALID_ARG: if invalid parameters are provided

        - BK_FAIL: others

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_gap_cancel_discovery(void)[](#_CPPv426bk_bt_gap_cancel_discoveryv "永久链接至目标")
:   Cancel Inquiry and Name Discovery. bk_bt_gap_cb_t will be called with BK_BT_GAP_DISC_STATE_CHANGED_EVT if Inquiry or Name Discovery is cancelled by calling this function.

    返回
    :   - BK_OK : Succeed

        - BK_ERR_INVALID_STATE: if bluetooth stack is not yet enabled

        - BK_FAIL: others

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_gap_get_remote_services([bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") remote_bda)[](#_CPPv429bk_bt_gap_get_remote_services12bk_bd_addr_t "永久链接至目标")
:   Start SDP to get remote services. bk_bt_gap_cb_t will be called with BK_BT_GAP_RMT_SRVCS_EVT after service discovery ends.

    返回
    :   - BK_OK : Succeed

        - BK_ERR_INVALID_STATE: if bluetooth stack is not yet enabled

        - BK_FAIL: others

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_gap_get_remote_service_record([bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") remote_bda, [bk_bt_uuid_t](dual_ble.md#_CPPv412bk_bt_uuid_t "bk_bt_uuid_t") *uuid)[](#_CPPv435bk_bt_gap_get_remote_service_record12bk_bd_addr_tP12bk_bt_uuid_t "永久链接至目标")
:   Start SDP to look up the service matching uuid on the remote device.

    ```
                 bk_bt_gap_cb_t will be called with BK_BT_GAP_RMT_SRVC_REC_EVT after service discovery ends
    ```

    返回
    :   - BK_OK : Succeed

        - BK_ERR_INVALID_STATE: if bluetooth stack is not yet enabled

        - BK_FAIL: others

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_gap_config_eir_data([bk_bt_eir_data_t](#_CPPv416bk_bt_eir_data_t "bk_bt_eir_data_t") *eir_data)[](#_CPPv425bk_bt_gap_config_eir_dataP16bk_bt_eir_data_t "永久链接至目标")
:   This function is called to config EIR data.

    ```
                 bk_bt_gap_cb_t will be called with BK_BT_GAP_CONFIG_EIR_DATA_EVT after config EIR ends.
    ```

    参数
    :   **eir_data** – **[in]** - pointer of EIR data content

    返回
    :   - BK_OK : Succeed

        - BK_ERR_INVALID_STATE: if bluetooth stack is not yet enabled

        - BK_ERR_INVALID_ARG: if param is invalid

        - BK_FAIL: others

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_gap_set_cod([bk_bt_cod_t](#_CPPv411bk_bt_cod_t "bk_bt_cod_t") cod, [bk_bt_cod_mode_t](#_CPPv416bk_bt_cod_mode_t "bk_bt_cod_mode_t") mode)[](#_CPPv417bk_bt_gap_set_cod11bk_bt_cod_t16bk_bt_cod_mode_t "永久链接至目标")
:   This function is called to set class of device. The structure bk_bt_gap_cb_t will be called with BK_BT_GAP_SET_COD_EVT after set COD ends. Some profile have special restrictions on class of device, changes may cause these profile do not work.

    参数
    :   - **cod** – **[in]** - class of device

        - **mode** – **[in]** - setting mode

    返回
    :   - BK_OK : Succeed

        - BK_ERR_INVALID_STATE: if bluetooth stack is not yet enabled

        - BK_ERR_INVALID_ARG: if param is invalid

        - BK_FAIL: others

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_gap_read_rssi_delta([bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") remote_addr)[](#_CPPv425bk_bt_gap_read_rssi_delta12bk_bd_addr_t "永久链接至目标")
:   This function is called to read RSSI delta by address after connected. The RSSI value returned by BK_BT_GAP_READ_RSSI_DELTA_EVT.

    参数
    :   **remote_addr** – **[in]** - remote device address, corrbkonding to a certain connection handle

    返回
    :   - BK_OK : Succeed

        - BK_FAIL: others

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_gap_remove_bond_device([bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr)[](#_CPPv428bk_bt_gap_remove_bond_device12bk_bd_addr_t "永久链接至目标")
:   Removes a device from the security database list of peer device.

    参数
    :   **bd_addr** – **[in]** : BD address of the peer device

    返回
    :   - BK_OK : success


        - BK_FAIL : failed

int bk_bt_gap_get_bond_device_num(void)[](#_CPPv429bk_bt_gap_get_bond_device_numv "永久链接至目标")
:   Get the device number from the security database list of peer device. It will return the device bonded number immediately.

    返回
    :   - >= 0 : bonded devices number


        - BK_FAIL : failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_gap_get_bond_device_list(int *dev_num, [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") *dev_list)[](#_CPPv430bk_bt_gap_get_bond_device_listPiP12bk_bd_addr_t "永久链接至目标")
:   Get the device from the security database list of peer device. It will return the device bonded information immediately.

    参数
    :   - **dev_num** – **[inout]** Indicate the dev_list array(buffer) size as input. If dev_num is large enough, it means the actual number as output. Suggest that dev_num value equal to [bk_ble_get_bond_device_num()](dual_ble.md#group__dm__gap__defines__v1_1ga197bcd6bbaf7eabfddabce66be9fad92 "dual_ble.md#group__dm__gap__defines__v1_1ga197bcd6bbaf7eabfddabce66be9fad92").

        - **dev_list** – **[out]** an array(buffer) of `bk_bd_addr_t` type. Use for storing the bonded devices address. The dev_list should be allocated by who call this API.

    返回
    :   - BK_OK : Succeed

        - BK_ERR_INVALID_STATE: if bluetooth stack is not yet enabled

        - BK_FAIL: others

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_gap_set_pin([bk_bt_pin_type_t](#_CPPv416bk_bt_pin_type_t "bk_bt_pin_type_t") pin_type, uint8_t pin_code_len, [bk_bt_pin_code_t](#_CPPv416bk_bt_pin_code_t "bk_bt_pin_code_t") pin_code)[](#_CPPv417bk_bt_gap_set_pin16bk_bt_pin_type_t7uint8_t16bk_bt_pin_code_t "永久链接至目标")
:   Set pin type and default pin code for legacy pairing.

    参数
    :   - **pin_type** – **[in]** Use variable or fixed pin. If pin_type is BK_BT_PIN_TYPE_VARIABLE, pin_code and pin_code_len will be ignored, and BK_BT_GAP_PIN_REQ_EVT will come when control requests for pin code. Else, will use fixed pin code and not callback to users.

        - **pin_code_len** – **[in]** Length of pin_code

        - **pin_code** – **[in]** Pin_code

    返回
    :   - BK_OK : success


        - BK_ERR_INVALID_STATE: if bluetooth stack is not yet enabled

        - other : failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_gap_pin_reply([bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr, bool accept, uint8_t pin_code_len, [bk_bt_pin_code_t](#_CPPv416bk_bt_pin_code_t "bk_bt_pin_code_t") pin_code)[](#_CPPv419bk_bt_gap_pin_reply12bk_bd_addr_tb7uint8_t16bk_bt_pin_code_t "永久链接至目标")
:   Reply the pin_code to the peer device for legacy pairing when BK_BT_GAP_PIN_REQ_EVT is coming.

    参数
    :   - **bd_addr** – **[in]** BD address of the peer

        - **accept** – **[in]** Pin_code reply successful or declined.

        - **pin_code_len** – **[in]** Length of pin_code

        - **pin_code** – **[in]** Pin_code

    返回
    :   - BK_OK : success


        - BK_ERR_INVALID_STATE: if bluetooth stack is not yet enabled

        - other : failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_gap_set_security_param([bk_bt_sp_param_t](#_CPPv416bk_bt_sp_param_t "bk_bt_sp_param_t") param_type, void *value, uint8_t len)[](#_CPPv428bk_bt_gap_set_security_param16bk_bt_sp_param_tPv7uint8_t "永久链接至目标")
:   Set a GAP security parameter value. Overrides the default value.

    参数
    :   - **param_type** – **[in]** : the type of the param which is to be set

        - **value** – **[in]** : the param value

        - **len** – **[in]** : the length of the param value

    返回
    :   - BK_OK : success


        - BK_ERR_INVALID_STATE: if bluetooth stack is not yet enabled

        - other : failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_gap_ssp_passkey_reply([bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr, bool accept, uint32_t passkey)[](#_CPPv427bk_bt_gap_ssp_passkey_reply12bk_bd_addr_tb8uint32_t "永久链接至目标")
:   Reply the key value to the peer device in the legacy connection stage.

    参数
    :   - **bd_addr** – **[in]** : BD address of the peer

        - **accept** – **[in]** : passkey entry successful or declined.

        - **passkey** – **[in]** : passkey value, must be a 6 digit number, can be lead by 0.

    返回
    :   - BK_OK : success


        - BK_ERR_INVALID_STATE: if bluetooth stack is not yet enabled

        - other : failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_gap_ssp_confirm_reply([bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr, bool accept)[](#_CPPv427bk_bt_gap_ssp_confirm_reply12bk_bd_addr_tb "永久链接至目标")
:   Reply the confirm value to the peer device in the legacy connection stage.

    参数
    :   - **bd_addr** – **[in]** : BD address of the peer device

        - **accept** – **[in]** : numbers to compare are the same or different

    返回
    :   - BK_OK : success


        - BK_ERR_INVALID_STATE: if bluetooth stack is not yet enabled

        - other : failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_gap_set_afh_channels([bk_bt_gap_afh_channels](#_CPPv422bk_bt_gap_afh_channels "bk_bt_gap_afh_channels") channels)[](#_CPPv426bk_bt_gap_set_afh_channels22bk_bt_gap_afh_channels "永久链接至目标")
:   Set the AFH channels.

    参数
    :   **channels** – **[in]** : The n th such field (in the range 0 to 78) contains the value for channel n : 0 means channel n is bad. 1 means channel n is unknown. The most significant bit is reserved and shall be set to 0. At least 20 channels shall be marked as unknown.

    返回
    :   - BK_OK : success


        - BK_ERR_INVALID_STATE: if bluetooth stack is not yet enabled

        - other : failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_gap_read_remote_name([bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") remote_bda)[](#_CPPv426bk_bt_gap_read_remote_name12bk_bd_addr_t "永久链接至目标")
:   Read the remote device name.

    参数
    :   **remote_bda** – **[in]** The remote device’s address

    返回
    :   - BK_OK : success


        - BK_ERR_INVALID_STATE: if bluetooth stack is not yet enabled

        - other : failed

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_gap_connect([bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") addr, uint8_t allow_role_switch)[](#_CPPv417bk_bt_gap_connect12bk_bd_addr_t7uint8_t "永久链接至目标")
:   Connect the remote device.

    参数
    :   - **addr** – **[in]** The remote device’s address

        - **allow_role_switch** – **[in]** Allow the role switch

    返回
    :   - BK_OK : success


        - BK_ERR_INVALID_STATE: if bluetooth stack is not yet enabled

        - other : failed

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_gap_disconnect([bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") addr, uint8_t reason)[](#_CPPv420bk_bt_gap_disconnect12bk_bd_addr_t7uint8_t "永久链接至目标")
:   Disconnect the remote device.

    参数
    :   - **addr** – **[in]** The remote device’s address

        - **reason** – **[in]** The disconnect reason

    返回
    :   - BK_OK : success


        - BK_ERR_INVALID_STATE: if bluetooth stack is not yet enabled

        - other : failed

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_gap_create_conn_cancel(uint8_t *addr)[](#_CPPv428bk_bt_gap_create_conn_cancelP7uint8_t "永久链接至目标")
:   This API can be used to request cancellation of the ongoing connection creation process.

    参数
    :   **addr** – **[in]** The remote device’s address

    返回
    :   ```

                     - BK_ERR_BT_SUCCESS: cancel request is sent to lower layer successfully

                     - others: fail
        ```

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_gap_set_page_timeout(uint16_t timeout)[](#_CPPv426bk_bt_gap_set_page_timeout8uint16_t "永久链接至目标")
:   This api can be used to set the value for the Page_Timeout configuration parameter.

    参数
    :   **timeout** – **[in]** Page Timeout measured in number of Baseband slots, unit of 0.625ms

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_gap_set_page_scan_activity(uint16_t interval, uint16_t window)[](#_CPPv432bk_bt_gap_set_page_scan_activity8uint16_t8uint16_t "永久链接至目标")
:   This api can be used to set the value for the Page_Scan_Interval and Page_Scan_Window configuration parameters.

    参数
    :   - **interval** – **[in]** defines the amount of time between consecutive page scans, unit of 0.625ms,(Range: 0x0012 to 0x1000, only even values are valid)

        - **window** – **[in]** defines the amount of time for the duration of the page scan, unit of 0.625ms,(Range: 0x0011 to 0x1000, can only be less than or equal to the Page_Scan_Interval)

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_gap_authentication_request(uint8_t *addr)[](#_CPPv432bk_bt_gap_authentication_requestP7uint8_t "永久链接至目标")
:   This api can be used to start authentication request.

    参数
    :   **addr** – **[in]** The remote device’s address

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_gap_set_auto_sniff_policy([bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") remote_bda, uint32_t sec, [bk_bt_gap_sniff_config](#_CPPv422bk_bt_gap_sniff_config "bk_bt_gap_sniff_config") *config)[](#_CPPv431bk_bt_gap_set_auto_sniff_policy12bk_bd_addr_t8uint32_tP22bk_bt_gap_sniff_config "永久链接至目标")
:   Set auto enter sniff policy. bk_bt_gap_cb_t will be called with BK_BT_GAP_SET_AUTO_SNIFF_CMPL_EVT after service discovery ends.

    参数
    :   - **remote_bda** – **[in]** The remote device’s address

        - **sec** – **[in]** How long time (second) enter sniff once no ACL data send or recv. When equal 0, will disable auto enter sniff.

        - **config** – **[in]** Sniff config. when is NULL, last config will be: max_interval: 500 msec min interval: 250 msec attempt: 5 msec timeout: 1.25 msec

    返回
    :   - BK_OK : Succeed

        - BK_FAIL: others


### Header File[](#id1 "永久链接至标题")


- [bluetooth/bk_dm_a2dp.h](https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_a2dp.h "https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_a2dp.h")


### Functions[](#id2 "永久链接至标题")

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_a2dp_register_callback([bk_bt_a2dp_cb_t](#_CPPv415bk_bt_a2dp_cb_t "bk_bt_a2dp_cb_t") callback)[](#_CPPv428bk_bt_a2dp_register_callback15bk_bt_a2dp_cb_t "永久链接至目标")
:   Register application callback function to A2DP module. used by both A2DP source and sink.

    参数
    :   **callback** – **[in]** A2DP event callback function

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_a2dp_source_init(void)[](#_CPPv422bk_bt_a2dp_source_initv "永久链接至目标")
:   Initialize the bluetooth A2DP source module. A2DP can work independently.


    **Attention**
    :   sink/source must init only one.

    返回
    :   - BK_ERR_BT_SUCCESS: if the initialization request is sent to lower layer successfully

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_a2dp_source_deinit(void)[](#_CPPv424bk_bt_a2dp_source_deinitv "永久链接至目标")
:   De-initialize for A2DP source module. This function should be called only after bk_bt_a2dp_source_init() completes successfully, and BK_A2DP_PROF_STATE_EVT will reported to APP layer.

    返回
    :   - BK_ERR_BT_SUCCESS: if the initialization request is sent to lower layer successfully

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_a2dp_source_register_data_callback([bk_a2dp_source_data_cb_t](#_CPPv424bk_a2dp_source_data_cb_t "bk_a2dp_source_data_cb_t") callback)[](#_CPPv437bk_a2dp_source_register_data_callback24bk_a2dp_source_data_cb_t "永久链接至目标")
:   Register A2DP source data input function. For now, the input should be PCM data stream.

    参数
    :   **callback** – **[in]** A2DP source data callback function

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_a2dp_source_set_pcm_data_format(uint32_t sample_rate, uint8_t bit_depth, uint8_t channel_count)[](#_CPPv434bk_a2dp_source_set_pcm_data_format8uint32_t7uint8_t7uint8_t "永久链接至目标")
:   set a2dp source data format

    参数
    :   - **sample_rate** – **[in]** pcm data sample rate, such as 8000 16000 32000 44100 48000.

        - **bit_depth** – **[in]** : pcm data bit depth, now support 16 bits only.

        - **channel_count** – **[in]** : pcm data channel count, support 1 or 2 now.

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_a2dp_source_register_pcm_encode_callback([bk_a2dp_source_pcm_encode_cb_t](#_CPPv430bk_a2dp_source_pcm_encode_cb_t "bk_a2dp_source_pcm_encode_cb_t") cb)[](#_CPPv443bk_a2dp_source_register_pcm_encode_callback30bk_a2dp_source_pcm_encode_cb_t "永久链接至目标")
:   register pcm encode callback.

    参数
    :   **cb** – **[in]** callback.

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_a2dp_source_register_pcm_resample_callback([bk_a2dp_source_pcm_resample_cb_t](#_CPPv432bk_a2dp_source_pcm_resample_cb_t "bk_a2dp_source_pcm_resample_cb_t") cb)[](#_CPPv445bk_a2dp_source_register_pcm_resample_callback32bk_a2dp_source_pcm_resample_cb_t "永久链接至目标")
:   register pcm resample callback, will be used if input pcm is not match a2dp negotiation, see BK_A2DP_AUDIO_SOURCE_CFG_EVT.

    参数
    :   **cb** – **[in]** callback.

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_a2dp_source_connect(uint8_t *addr)[](#_CPPv425bk_bt_a2dp_source_connectP7uint8_t "永久链接至目标")
:   Connect to remote A2DP sink device. This API must be called after bk_bt_a2dp_source_init()

    参数
    :   **addr** – **[in]** remote bluetooth device address

    返回
    :   - BK_ERR_BT_SUCCESS: connect request is sent to lower layer successfully

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_a2dp_source_disconnect(uint8_t *addr)[](#_CPPv428bk_bt_a2dp_source_disconnectP7uint8_t "永久链接至目标")
:   Disconnect from the remote A2DP sink device. This API must be called after bk_bt_a2dp_source_init()

    参数
    :   **addr** – **[in]** remote bluetooth device address

    返回
    :   ```

                     - BK_ERR_BT_SUCCESS: connect request is sent to lower layer successfully

                     - others: fail
        ```

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_a2dp_media_ctrl([bk_a2dp_media_ctrl_t](#_CPPv420bk_a2dp_media_ctrl_t "bk_a2dp_media_ctrl_t") ctrl)[](#_CPPv418bk_a2dp_media_ctrl20bk_a2dp_media_ctrl_t "永久链接至目标")
:   Media control commands. This API can be used for both A2DP sink and must be called after bk_bt_a2dp_source_init()


    **Attention**
    :   this function only used for a2dp source

    参数
    :   **ctrl** – **[in]** control commands for A2DP action

    返回
    :   - BK_ERR_BT_SUCCESS: control command is sent to lower layer successfully

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_a2dp_sink_init(uint8_t aac_supported)[](#_CPPv420bk_bt_a2dp_sink_init7uint8_t "永久链接至目标")
:   Initialize the bluetooth A2DP sink module.

    参数
    :   **aac_supported** – **[in]** 1 means aac is supported, 0 means aac is not supported.

    返回
    :   - BK_ERR_BT_SUCCESS: the initialization request is successfully

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_a2dp_sink_deinit(void)[](#_CPPv422bk_bt_a2dp_sink_deinitv "永久链接至目标")
:   De-initialize for A2DP sink module. This function should be called only after bk_bt_a2dp_sink_init() completes successfully, and BK_A2DP_PROF_STATE_EVT will reported to APP layer.

    返回
    :   - BK_ERR_BT_SUCCESS: the deinitialization request is successfully

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_a2dp_sink_register_data_callback([bk_bt_sink_data_cb_t](#_CPPv420bk_bt_sink_data_cb_t "bk_bt_sink_data_cb_t") callback)[](#_CPPv438bk_bt_a2dp_sink_register_data_callback20bk_bt_sink_data_cb_t "永久链接至目标")
:   Register A2DP sink data output function;.

    参数
    :   **callback** – **[in]** A2DP sink data callback function

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_a2dp_sink_connect(uint8_t *remote_bda)[](#_CPPv423bk_bt_a2dp_sink_connectP7uint8_t "永久链接至目标")
:   Connect to remote bluetooth A2DP source device. This API must be called after bk_bt_a2dp_sink_init().

    参数
    :   **remote_bda** – **[in]** remote bluetooth device address

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_a2dp_sink_disconnect(uint8_t *remote_bda)[](#_CPPv426bk_bt_a2dp_sink_disconnectP7uint8_t "永久链接至目标")
:   Disconnect from the remote A2DP source device. This API must be called after bk_bt_a2dp_sink_init().

    参数
    :   **remote_bda** – **[in]** remote bluetooth device address

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_a2dp_sink_set_delay_value(uint16_t delay_value)[](#_CPPv431bk_bt_a2dp_sink_set_delay_value8uint16_t "永久链接至目标")
:   Set delay reporting value.This API must be called after bk_bt_a2dp_sink_init().

    参数
    :   **delay_value** – **[in]** reporting value is in 1/10 millisecond

    返回
    :   - BK_ERR_BT_SUCCESS: delay value is sent to lower layer successfully

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_a2dp_sink_get_delay_value(void)[](#_CPPv431bk_bt_a2dp_sink_get_delay_valuev "永久链接至目标")
:   Get delay reporting value. This API must be called after bk_bt_a2dp_sink_init().

    返回
    :   - BK_ERR_BT_SUCCESS: if the request is sent successfully

        - others: fail


### Header File[](#id3 "永久链接至标题")


- [bluetooth/bk_dm_avrcp.h](https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_avrcp.h "https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_avrcp.h")


### Functions[](#id4 "永久链接至标题")

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_avrcp_ct_init(void)[](#_CPPv419bk_bt_avrcp_ct_initv "永久链接至目标")
:   Initialize the bluetooth AVRCP controller module.

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_avrcp_ct_deinit(void)[](#_CPPv421bk_bt_avrcp_ct_deinitv "永久链接至目标")
:   Deinitialize the bluetooth AVRCP controller module.

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_avrcp_ct_register_callback([bk_avrcp_ct_cb_t](#_CPPv416bk_avrcp_ct_cb_t "bk_avrcp_ct_cb_t") callback)[](#_CPPv432bk_bt_avrcp_ct_register_callback16bk_avrcp_ct_cb_t "永久链接至目标")
:   Register application callbacks to AVRCP module.

    参数
    :   **callback** – **[in]** AVRCP controller callback function

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_avrcp_ct_send_get_rn_capabilities_cmd(uint8_t *remote_bda)[](#_CPPv443bk_bt_avrcp_ct_send_get_rn_capabilities_cmdP7uint8_t "永久链接至目标")
:   Send GetCapabilities PDU to AVRCP target to retrieve remote device’s supported notification event_ids. This function should be called after BK_AVRCP_CT_CONNECTION_STATE_EVT is received and AVRCP connection is established.

    参数
    :   **remote_bda** – **[in]** remote bluetooth device address

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_avrcp_ct_send_register_notification_cmd(uint8_t *remote_bda, uint8_t event_id, uint32_t event_parameter)[](#_CPPv445bk_bt_avrcp_ct_send_register_notification_cmdP7uint8_t7uint8_t8uint32_t "永久链接至目标")
:   Send register notification command to AVRCP target. This function should be called after BK_AVRCP_CT_CONNECTION_STATE_EVT is received and AVRCP connection is established.

    参数
    :   - **remote_bda** – **[in]** remote bluetooth device address

        - **event_id** – **[in]** : id of events, e.g. BK_AVRCP_RN_PLAY_STATUS_CHANGE, BK_AVRCP_RN_TRACK_CHANGE, etc.

        - **event_parameter** – **[in]** : playback interval for BK_AVRCP_RN_PLAY_POS_CHANGED in second; For other events , value of this parameter is ignored.

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_avrcp_ct_send_passthrough_cmd(uint8_t *remote_bda, uint8_t key_code, uint8_t key_state)[](#_CPPv435bk_bt_avrcp_ct_send_passthrough_cmdP7uint8_t7uint8_t7uint8_t "永久链接至目标")
:   Send passthrough command to AVRCP target. This function should be called after BK_AVRCP_CT_CONNECTION_STATE_EVT is received and AVRCP connection is established.

    参数
    :   - **remote_bda** – **[in]** remote bluetooth device address.

        - **key_code** – **[in]** : passthrough command code, e.g. BK_AVRCP_PT_CMD_PLAY, BK_AVRCP_PT_CMD_STOP, etc.

        - **key_state** – **[in]** : passthrough command key state, BK_AVRCP_PT_CMD_STATE_PRESSED or BK_AVRCP_PT_CMD_STATE_RELEASED

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_avrcp_ct_send_absolute_volume_cmd(uint8_t *remote_bda, uint8_t volume)[](#_CPPv439bk_bt_avrcp_ct_send_absolute_volume_cmdP7uint8_t7uint8_t "永久链接至目标")
:   Send set absolute volume command to AVRCP target. This function should be called after BK_AVRCP_CT_CONNECTION_STATE_EVT is received and AVRCP connection is established.

    参数
    :   - **remote_bda** – **[in]** remote bluetooth device address.

        - **volume** – **[in]** : volume, 0 to 0x7f, means 0% to 100%

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_avrcp_ct_send_set_player_app_setting_cmd(uint8_t *remote_bda, uint8_t attr_id, uint8_t value_id)[](#_CPPv446bk_bt_avrcp_ct_send_set_player_app_setting_cmdP7uint8_t7uint8_t7uint8_t "永久链接至目标")
:   Send player application settings command to AVRCP target. This function should be called after BK_AVRCP_CT_CONNECTION_STATE_EVT is received and AVRCP connection is established.

    参数
    :   - **remote_bda** – **[in]** remote bluetooth device address.

        - **attr_id** – **[in]** : player application setting attribute IDs from one of bk_avrcp_ps_attr_ids_t

        - **value_id** – **[in]** : attribute value defined for the specific player application setting attribute

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_avrcp_ct_send_get_elem_attribute_cmd(uint8_t *remote_bda, uint32_t media_attr_id_mask)[](#_CPPv442bk_bt_avrcp_ct_send_get_elem_attribute_cmdP7uint8_t8uint32_t "永久链接至目标")
:   Send get media attr command to AVRCP target. This function should be called after BK_AVRCP_CT_CONNECTION_STATE_EVT is received and AVRCP connection is established.

    参数
    :   - **remote_bda** – **[in]** remote bluetooth device address.

        - **media_attr_id_mask** – **[in]** : mask of bk_avrcp_media_attr_id_t, such as (1 << BK_AVRCP_MEDIA_ATTR_ID_TITLE) | (1 << BK_AVRCP_MEDIA_ATTR_ID_ARTIST).

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_avrcp_tg_init(void)[](#_CPPv419bk_bt_avrcp_tg_initv "永久链接至目标")
:   Initialize the bluetooth AVRCP target module.

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_avrcp_tg_deinit(void)[](#_CPPv421bk_bt_avrcp_tg_deinitv "永久链接至目标")
:   Deinitialize the bluetooth AVRCP target module.

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_avrcp_tg_register_callback([bk_avrcp_tg_cb_t](#_CPPv416bk_avrcp_tg_cb_t "bk_avrcp_tg_cb_t") callback)[](#_CPPv432bk_bt_avrcp_tg_register_callback16bk_avrcp_tg_cb_t "永久链接至目标")
:   Register application callbacks to AVRCP target module.

    参数
    :   **callback** – **[in]** AVRCP target callback function

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_avrcp_tg_get_rn_evt_cap([bk_avrcp_rn_cap_api_method_t](#_CPPv428bk_avrcp_rn_cap_api_method_t "bk_avrcp_rn_cap_api_method_t") cap, [bk_avrcp_rn_evt_cap_mask_t](#_CPPv426bk_avrcp_rn_evt_cap_mask_t "bk_avrcp_rn_evt_cap_mask_t") *evt_set)[](#_CPPv429bk_bt_avrcp_tg_get_rn_evt_cap28bk_avrcp_rn_cap_api_method_tP26bk_avrcp_rn_evt_cap_mask_t "永久链接至目标")
:   Get the requested event notification capabilies on local AVRC target. The capability is returned in a bit mask representation in evt_set. This function should be called after bk_avrcp_tg_init().

    For capability type “BK_AVRCP_RN_CAP_API_METHOD_ALLOWED, the retrieved event set is constant and it covers all of the notification events that can possibly be supported with current implementation.

    For capability type BK_AVRCP_RN_CAP_API_METHOD_CURRENT_ENABLE, the event set covers the notification events selected to be supported under current configuration, The configuration can be changed using bk_avrcp_tg_set_rn_evt_cap().

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_avrcp_tg_set_rn_evt_cap(const [bk_avrcp_rn_evt_cap_mask_t](#_CPPv426bk_avrcp_rn_evt_cap_mask_t "bk_avrcp_rn_evt_cap_mask_t") *evt_set)[](#_CPPv429bk_bt_avrcp_tg_set_rn_evt_capPK26bk_avrcp_rn_evt_cap_mask_t "永久链接至目标")
:   Set the event notification capabilities on local AVRCP target. The capability is given in a bit mask representation in evt_set and must be a subset of allowed event IDs with current implementation. This function should be called after bk_avrcp_tg_init().

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

bool bk_bt_avrcp_rn_evt_bit_mask_operation([bk_avrcp_bit_mask_op_t](#_CPPv422bk_avrcp_bit_mask_op_t "bk_avrcp_bit_mask_op_t") op, [bk_avrcp_rn_evt_cap_mask_t](#_CPPv426bk_avrcp_rn_evt_cap_mask_t "bk_avrcp_rn_evt_cap_mask_t") *events, [bk_avrcp_rn_event_ids_t](#_CPPv423bk_avrcp_rn_event_ids_t "bk_avrcp_rn_event_ids_t") event_id)[](#_CPPv437bk_bt_avrcp_rn_evt_bit_mask_operation22bk_avrcp_bit_mask_op_tP26bk_avrcp_rn_evt_cap_mask_t23bk_avrcp_rn_event_ids_t "永久链接至目标")
:   Operate on the type [bk_avrcp_rn_evt_cap_mask_t](#structbk__avrcp__rn__evt__cap__mask__t "#structbk__avrcp__rn__evt__cap__mask__t") with regard to a specific event.

    For operation BK_AVRCP_BIT_MASK_OP_TEST, return true if the corresponding bit is set, otherwise false.

    参数
    :   - **op** – **[in]** operation requested on the bit mask field

        - **events** – **[in]** pointer to event notification capability bit mask structure

        - **event_id** – **[in]** notification event code

    返回
    :   For operation BK_AVRCP_BIT_MASK_OP_SET or BK_AVRCP_BIT_MASK_OP_CLEAR, return true for a successful operation, otherwise return false.

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_avrcp_tg_send_rn_rsp(uint8_t *addr, [bk_avrcp_rn_event_ids_t](#_CPPv423bk_avrcp_rn_event_ids_t "bk_avrcp_rn_event_ids_t") event_id, [bk_avrcp_rn_rsp_t](#_CPPv417bk_avrcp_rn_rsp_t "bk_avrcp_rn_rsp_t") rsp, [bk_avrcp_rn_param_t](#_CPPv419bk_avrcp_rn_param_t "bk_avrcp_rn_param_t") *param)[](#_CPPv426bk_bt_avrcp_tg_send_rn_rspP7uint8_t23bk_avrcp_rn_event_ids_t17bk_avrcp_rn_rsp_tP19bk_avrcp_rn_param_t "永久链接至目标")
:   Send RegisterNotification Response to remote AVRCP controller. Local event notification capability can be set using bk_avrcp_tg_set_rn_evt_cap(), in a bit mask representation in evt_set. This function should be called after bk_avrcp_tg_init().

    参数
    :   - **addr** – **[in]** peer addr

        - **event_id** – **[in]** notification event ID that remote AVRCP CT registers

        - **rsp** – **[in]** notification response code

        - **param** – **[in]** parameters included in the specific notification

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_avrcp_tg_get_psth_cmd_filter([bk_avrcp_psth_filter_t](#_CPPv422bk_avrcp_psth_filter_t "bk_avrcp_psth_filter_t") filter, [bk_avrcp_psth_bit_mask_t](#_CPPv424bk_avrcp_psth_bit_mask_t "bk_avrcp_psth_bit_mask_t") *cmd_set)[](#_CPPv434bk_bt_avrcp_tg_get_psth_cmd_filter22bk_avrcp_psth_filter_tP24bk_avrcp_psth_bit_mask_t "永久链接至目标")
:   Get the current filter of remote passthrough commands on AVRC target. Filter is given by filter type and bit mask for the passthrough commands. This function should be called after [bk_bt_avrcp_tg_init()](#group__dm__avrcp_1ga0f43a498c80b739f64c0bd8e8750e851 "#group__dm__avrcp_1ga0f43a498c80b739f64c0bd8e8750e851"). For filter type BK_AVRCP_PSTH_FILTER_METHOD_ALLOWED, the retrieved command set is constant and it covers all of the passthrough commands that can possibly be supported. For filter type BK_AVRCP_PSTH_FILTER_METHOD_CURRENT_ENABLE, the retrieved command set covers the passthrough commands selected to be supported according to current configuration. The configuration can be changed using [bk_bt_avrcp_tg_set_psth_cmd_filter()](#group__dm__avrcp_1ga4f02fd8c38fd08c72e06a633cfdca1ad "#group__dm__avrcp_1ga4f02fd8c38fd08c72e06a633cfdca1ad").

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_avrcp_tg_set_psth_cmd_filter([bk_avrcp_psth_filter_t](#_CPPv422bk_avrcp_psth_filter_t "bk_avrcp_psth_filter_t") filter, const [bk_avrcp_psth_bit_mask_t](#_CPPv424bk_avrcp_psth_bit_mask_t "bk_avrcp_psth_bit_mask_t") *cmd_set)[](#_CPPv434bk_bt_avrcp_tg_set_psth_cmd_filter22bk_avrcp_psth_filter_tPK24bk_avrcp_psth_bit_mask_t "永久链接至目标")
:   Set the filter of remote passthrough commands on AVRC target. Filter is given by filter type and bit mask for the passthrough commands. This function should be called after [bk_bt_avrcp_tg_init()](#group__dm__avrcp_1ga0f43a498c80b739f64c0bd8e8750e851 "#group__dm__avrcp_1ga0f43a498c80b739f64c0bd8e8750e851").

    If filter type is BK_AVRCP_PSTH_FILTER_METHOD_ALLOWED, the passthrough commands which are set “1” as given in cmd_set will generate BK_AVRCP_CT_PASSTHROUGH_RSP_EVT callback event and are auto-accepted in the protocol stack, other commands are replied with response type “NOT IMPLEMENTED” (8). The set of supported commands should be a subset of allowed command set. The allowed command set can be retrieved using [bk_bt_avrcp_tg_get_psth_cmd_filter()](#group__dm__avrcp_1ga0b28fe5943a876887a6175eb3fe8b747 "#group__dm__avrcp_1ga0b28fe5943a876887a6175eb3fe8b747") with filter type “BK_AVRCP_PSTH_FILTER_METHOD_CURRENT_ENABLE”.

    Filter type “BK_AVRCP_PSTH_FILTER_METHOD_ALLOWED” does not apply to this function.

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

bool bk_bt_avrcp_psth_bit_mask_operation([bk_avrcp_bit_mask_op_t](#_CPPv422bk_avrcp_bit_mask_op_t "bk_avrcp_bit_mask_op_t") op, [bk_avrcp_psth_bit_mask_t](#_CPPv424bk_avrcp_psth_bit_mask_t "bk_avrcp_psth_bit_mask_t") *psth, [bk_avrcp_pt_cmd_t](#_CPPv417bk_avrcp_pt_cmd_t "bk_avrcp_pt_cmd_t") cmd)[](#_CPPv435bk_bt_avrcp_psth_bit_mask_operation22bk_avrcp_bit_mask_op_tP24bk_avrcp_psth_bit_mask_t17bk_avrcp_pt_cmd_t "永久链接至目标")
:   Operate on the type [bk_avrcp_psth_bit_mask_t](#structbk__avrcp__psth__bit__mask__t "#structbk__avrcp__psth__bit__mask__t") with regard to a specific PASSTHROUGH command.

    参数
    :   - **op** – **[in]** operation requested on the bit mask field

        - **psth** – **[in]** pointer to passthrough command bit mask structure

        - **cmd** – **[in]** passthrough command code

    返回
    :   For operation BK_AVRCP_BIT_MASK_OP_SET or BK_AVRCP_BIT_MASK_OP_CLEAR, return true for a successful operation, otherwise return false. For operation BK_AVRCP_BIT_MASK_OP_TEST, return true if the corresponding bit is set, otherwise false.

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_avrcp_connect(uint8_t *remote_bda)[](#_CPPv419bk_bt_avrcp_connectP7uint8_t "永久链接至目标")
:   Connect to remote bluetooth AVRCP. This API must be called after [bk_bt_avrcp_ct_init()](#group__dm__avrcp_1ga05f83b873d0086a261259a7523ea3e0f "#group__dm__avrcp_1ga05f83b873d0086a261259a7523ea3e0f") or bk_bt_avrcp_tg_init.

    参数
    :   **remote_bda** – **[in]** remote bluetooth device address

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail


### Header File[](#id5 "永久链接至标题")


- [bluetooth/bk_dm_hfp.h](https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_hfp.h "https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_hfp.h")


### Functions[](#id6 "永久链接至标题")

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_hf_client_register_callback([bk_bt_hf_client_cb_t](#_CPPv420bk_bt_hf_client_cb_t "bk_bt_hf_client_cb_t") callback)[](#_CPPv433bk_bt_hf_client_register_callback20bk_bt_hf_client_cb_t "永久链接至目标")
:   Register application callback function to HFP client module.

    参数
    :   **callback** – **[in]** HFP client event callback function

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_hf_client_init(uint8_t msbc_supported)[](#_CPPv420bk_bt_hf_client_init7uint8_t "永久链接至目标")
:   Initialize the bluetooth HFP client module.

    参数
    :   **msbc_supported** – **[in]** 1 means msbc is supported, 0 means msbc is not supported.

    返回
    :   - BK_ERR_BT_SUCCESS: the initialization request is successfully

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_hf_client_deinit(void)[](#_CPPv422bk_bt_hf_client_deinitv "永久链接至目标")
:   De-initialize for HFP client module.

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_hf_client_register_data_callback([bk_bt_hf_client_data_cb_t](#_CPPv425bk_bt_hf_client_data_cb_t "bk_bt_hf_client_data_cb_t") callback)[](#_CPPv438bk_bt_hf_client_register_data_callback25bk_bt_hf_client_data_cb_t "永久链接至目标")
:   Register HFP client data input function;.

    参数
    :   **callback** – **[in]** HFP client incoming data callback function

    返回
    :   - BK_ERR_BT_SUCCESS: the initialization request is successfully

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_hf_client_voice_out_write(uint8_t *remote_bda, uint8_t *buf, uint16_t len)[](#_CPPv431bk_bt_hf_client_voice_out_writeP7uint8_tP7uint8_t8uint16_t "永久链接至目标")
:   Send voice data to HFP AG;.

    参数
    :   - **remote_bda** – **[in]** remote bluetooth device address

        - **buf** – **[in]** : pointer to the data

        - **len** – **[in]** : size(in bytes) in buf

    返回
    :   - BK_ERR_BT_SUCCESS: the initialization request is successfully

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_hf_client_connect(uint8_t *remote_bda)[](#_CPPv423bk_bt_hf_client_connectP7uint8_t "永久链接至目标")
:   Establish a Service Level Connection to remote bluetooth HFP audio gateway(AG) device. This function must be called after bk_bt_hf_client_init().

    参数
    :   **remote_bda** – **[in]** remote bluetooth device address

    返回
    :   - BK_ERR_BT_SUCCESS: connect request is sent to lower layer

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_hf_client_disconnect(uint8_t *remote_bda)[](#_CPPv426bk_bt_hf_client_disconnectP7uint8_t "永久链接至目标")
:   Disconnect from the remote HFP audio gateway. This function must be called after bk_bt_hf_client_init().

    参数
    :   **remote_bda** – **[in]** remote bluetooth device address

    返回
    :   - BK_ERR_BT_SUCCESS: connect request is sent to lower layer

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_hf_client_connect_audio(uint8_t *remote_bda)[](#_CPPv429bk_bt_hf_client_connect_audioP7uint8_t "永久链接至目标")
:   Create audio connection with remote HFP AG. As a precondition to use this API, Service Level Connection shall exist with AG.

    参数
    :   **remote_bda** – **[in]** remote bluetooth device address

    返回
    :   - BK_ERR_BT_SUCCESS: connect request is sent to lower layer

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_hf_client_disconnect_audio(uint8_t *remote_bda)[](#_CPPv432bk_bt_hf_client_disconnect_audioP7uint8_t "永久链接至目标")
:   Release the established audio connection with remote HFP AG. As a precondition to use this API, Service Level Connection shall exist with AG.

    参数
    :   **remote_bda** – **[in]** remote bluetooth device address

    返回
    :   - BK_ERR_BT_SUCCESS: disconnect request is sent to lower layer

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_hf_client_start_voice_recognition(uint8_t *remote_bda)[](#_CPPv439bk_bt_hf_client_start_voice_recognitionP7uint8_t "永久链接至目标")
:   Enable voice recognition in the AG. As a precondition to use this API, Service Level Connection shall exist with AG.

    参数
    :   **remote_bda** – **[in]** remote bluetooth device address

    返回
    :   - BK_ERR_BT_SUCCESS: request is sent to lower layer

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_hf_client_stop_voice_recognition(uint8_t *remote_bda)[](#_CPPv438bk_bt_hf_client_stop_voice_recognitionP7uint8_t "永久链接至目标")
:   Disable voice recognition in the AG. As a precondition to use this API, Service Level Connection shall exist with AG.

    参数
    :   **remote_bda** – **[in]** remote bluetooth device address

    返回
    :   - BK_ERR_BT_SUCCESS: request is sent to lower layer

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_hf_client_volume_update(uint8_t *remote_bda, [bk_hf_volume_control_target_t](#_CPPv429bk_hf_volume_control_target_t "bk_hf_volume_control_target_t") type, uint8_t volume)[](#_CPPv429bk_bt_hf_client_volume_updateP7uint8_t29bk_hf_volume_control_target_t7uint8_t "永久链接至目标")
:   Volume synchronization with AG. As a precondition to use this API, Service Level Connection shall exist with AG.

    参数
    :   - **remote_bda** – **[in]** remote bluetooth device address

        - **type** – **[in]** volume control target, speaker or microphone

        - **volume** – **[in]** gain of the speaker of microphone, ranges 0 to 15

    返回
    :   - BK_ERR_BT_SUCCESS: request is sent to lower layer

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_hf_client_dial(uint8_t *remote_bda, const char *number)[](#_CPPv420bk_bt_hf_client_dialP7uint8_tPKc "永久链接至目标")
:   Place a call with a specified number, if number is NULL, last called number is called. As a precondition to use this API, Service Level Connection shall exist with AG.

    参数
    :   - **remote_bda** – **[in]** remote bluetooth device address

        - **number** – **[in]** number string of the call. If NULL, the last number is called(aka re-dial)

    返回
    :   - BK_ERR_BT_SUCCESS: request is sent to lower layer

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_hf_client_dial_memory(uint8_t *remote_bda, int location)[](#_CPPv427bk_bt_hf_client_dial_memoryP7uint8_ti "永久链接至目标")
:   Place a call with number specified by location(speed dial). As a precondition to use this API, Service Level Connection shall exist with AG.

    参数
    :   - **remote_bda** – **[in]** remote bluetooth device address

        - **location** – **[in]** location of the number in the memory

    返回
    :   - BK_ERR_BT_SUCCESS: request is sent to lower layer

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_hf_client_send_chld_cmd(uint8_t *remote_bda, [bk_hf_chld_type_t](#_CPPv417bk_hf_chld_type_t "bk_hf_chld_type_t") chld)[](#_CPPv429bk_bt_hf_client_send_chld_cmdP7uint8_t17bk_hf_chld_type_t "永久链接至目标")
:   Send call hold and multiparty commands(Use AT+CHLD). As a precondition to use this API, Service Level Connection shall exist with AG.

    参数
    :   - **remote_bda** – **[in]** remote bluetooth device address

        - **chld** – **[in]** AT+CHLD call hold and multiparty handling AT command.

    返回
    :   - BK_ERR_BT_SUCCESS: request is sent to lower layer

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_hf_client_send_btrh_cmd(uint8_t *remote_bda, [bk_hf_btrh_cmd_t](#_CPPv416bk_hf_btrh_cmd_t "bk_hf_btrh_cmd_t") btrh)[](#_CPPv429bk_bt_hf_client_send_btrh_cmdP7uint8_t16bk_hf_btrh_cmd_t "永久链接至目标")
:   Send response and hold action command(Send AT+BTRH command) As a precondition to use this API, Service Level Connection shall exist with AG.

    参数
    :   - **remote_bda** – **[in]** remote bluetooth device address

        - **btrh** – **[in]** response and hold action to send

    返回
    :   - BK_ERR_BT_SUCCESS: request is sent to lower layer

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_hf_client_answer_call(uint8_t *remote_bda)[](#_CPPv427bk_bt_hf_client_answer_callP7uint8_t "永久链接至目标")
:   Answer an incoming call(send ATA command). As a precondition to use this API, Service Level Connection shall exist with AG.

    参数
    :   **remote_bda** – **[in]** remote bluetooth device address

    返回
    :   - BK_ERR_BT_SUCCESS: request is sent to lower layer

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_hf_client_reject_call(uint8_t *remote_bda)[](#_CPPv427bk_bt_hf_client_reject_callP7uint8_t "永久链接至目标")
:   Reject an incoming call(send AT+CHUP command). As a precondition to use this API, Service Level Connection shall exist with AG.

    参数
    :   **remote_bda** – **[in]** remote bluetooth device address

    返回
    :   - BK_ERR_BT_SUCCESS: request is sent to lower layer

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_hf_client_query_current_calls(uint8_t *remote_bda)[](#_CPPv435bk_bt_hf_client_query_current_callsP7uint8_t "永久链接至目标")
:   Query list of current calls in AG(send AT+CLCC command). As a precondition to use this API, Service Level Connection shall exist with AG.

    参数
    :   **remote_bda** – **[in]** remote bluetooth device address

    返回
    :   - BK_ERR_BT_SUCCESS: request is sent to lower layer

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_hf_client_query_current_operator_name(uint8_t *remote_bda)[](#_CPPv443bk_bt_hf_client_query_current_operator_nameP7uint8_t "永久链接至目标")
:   Query the name of currently selected network operator in AG(use AT+COPS commands). As a precondition to use this API, Service Level Connection shall exist with AG.

    参数
    :   **remote_bda** – **[in]** remote bluetooth device address

    返回
    :   - BK_ERR_BT_SUCCESS: request is sent to lower layer

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_hf_client_retrieve_subscriber_info(uint8_t *remote_bda)[](#_CPPv440bk_bt_hf_client_retrieve_subscriber_infoP7uint8_t "永久链接至目标")
:   Get subscriber information number from AG(send AT+CNUM command) As a precondition to use this API, Service Level Connection shall exist with AG.

    参数
    :   **remote_bda** – **[in]** remote bluetooth device address

    返回
    :   - BK_ERR_BT_SUCCESS: request is sent to lower layer

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_hf_client_send_dtmf(uint8_t *remote_bda, const char *code)[](#_CPPv425bk_bt_hf_client_send_dtmfP7uint8_tPKc "永久链接至目标")
:   Transmit DTMF codes during an ongoing call(use AT+VTS commands) As a precondition to use this API, Service Level Connection shall exist with AG.

    参数
    :   - **remote_bda** – **[in]** remote bluetooth device address

        - **code** – **[in]** string of the dtmf code

    返回
    :   - BK_ERR_BT_SUCCESS: request is sent to lower layer

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_hf_client_request_last_voice_tag_number(uint8_t *remote_bda)[](#_CPPv445bk_bt_hf_client_request_last_voice_tag_numberP7uint8_t "永久链接至目标")
:   Request a phone number from AG corresponding to last voice tag recorded (send AT+BINP command). As a precondition to use this API, Service Level Connection shall exist with AG.

    参数
    :   **remote_bda** – **[in]** remote bluetooth device address

    返回
    :   - BK_ERR_BT_SUCCESS: request is sent to lower layer

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_hf_client_send_nrec(uint8_t *remote_bda)[](#_CPPv425bk_bt_hf_client_send_nrecP7uint8_t "永久链接至目标")
:   Disable echo cancellation and noise reduction in the AG (use AT+NREC=0 command). As a precondition to use this API, Service Level Connection shall exist with AG.

    参数
    :   **remote_bda** – **[in]** remote bluetooth device address

    返回
    :   - BK_ERR_BT_SUCCESS: request is sent to lower layer

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_hf_client_redial(uint8_t *remote_bda)[](#_CPPv422bk_bt_hf_client_redialP7uint8_t "永久链接至目标")
:   This API allows user to redial the last number dialed (use AT+BLDN command). As a precondition to use this API, Service Level Connection shall exist with AG.

    参数
    :   **remote_bda** – **[in]** remote bluetooth device address

    返回
    :   - BK_ERR_BT_SUCCESS: request is sent to lower layer

        - others: fail

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_hf_client_send_custom_cmd(uint8_t *remote_bda, const char *atcmd)[](#_CPPv431bk_bt_hf_client_send_custom_cmdP7uint8_tPKc "永久链接至目标")
:   This API allows user to send custom AT Command. As a precondition to use this API, Service Level Connection shall exist with AG.

    参数
    :   - **remote_bda** – **[in]** remote bluetooth device address

        - **atcmd** – **[in]** string of the custom atcmd.

    返回
    :   - BK_ERR_BT_SUCCESS: request is sent to lower layer

        - others: fail


### Header File[](#id7 "永久链接至标题")


- [bluetooth/bk_dm_hidd.h](https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_hidd.h "https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_hidd.h")


### Functions[](#id8 "永久链接至标题")

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_hid_device_register_callback([bk_hd_cb_t](#_CPPv410bk_hd_cb_t "bk_hd_cb_t") callback)[](#_CPPv434bk_bt_hid_device_register_callback10bk_hd_cb_t "永久链接至目标")
:   This function is called to init callbacks with HID device module.

    参数
    :   **callback** – **[in]** pointer to the init callback function.

    返回
    :   - BK_OK: success

        - other: failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_hid_device_init(void)[](#_CPPv421bk_bt_hid_device_initv "永久链接至目标")
:   Initializes HIDD interface. This function should be called after bk_bluedroid_init() and bk_bluedroid_enable() success, and should be called after bk_bt_hid_device_register_callback. When the operation is complete, the callback function will be called with BK_HIDD_INIT_EVT.

    返回
    :   - BK_OK: success

        - other: failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_hid_device_deinit(void)[](#_CPPv423bk_bt_hid_device_deinitv "永久链接至目标")
:   De-initializes HIDD interface. This function should be called after bk_bluedroid_init() and bk_bluedroid_enable() success, and should be called after bk_bt_hid_device_init(). When the operation is complete, the callback function will be called with BK_HIDD_DEINIT_EVT.

    返回
    :   - BK_OK: success

        - other: failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_hid_device_register_app([bk_hidd_app_param_t](#_CPPv419bk_hidd_app_param_t "bk_hidd_app_param_t") *app_param)[](#_CPPv429bk_bt_hid_device_register_appP19bk_hidd_app_param_t "永久链接至目标")
:   Registers HIDD parameters with SDP and sets l2cap Quality of Service. This function should be called after [bk_bluetooth_init()](dual_ble.md#group__dm__bluetooth_1ga577c57a04b4b4589adfb5736442015a2 "dual_ble.md#group__dm__bluetooth_1ga577c57a04b4b4589adfb5736442015a2") success, and should be called after bk_bt_hid_device_init(). When the operation is complete, the callback function will be called with BK_HIDD_REGISTER_APP_EVT.

    参数
    :   **app_param** – **[in]** HIDD parameters

    返回
    :   - BK_OK: success

        - other: failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_hid_device_unregister_app(void)[](#_CPPv431bk_bt_hid_device_unregister_appv "永久链接至目标")
:   Removes HIDD parameters from SDP and resets l2cap Quality of Service. This function should be called after [bk_bluetooth_init()](dual_ble.md#group__dm__bluetooth_1ga577c57a04b4b4589adfb5736442015a2 "dual_ble.md#group__dm__bluetooth_1ga577c57a04b4b4589adfb5736442015a2") success, and should be called after bk_bt_hid_device_init(). When the operation is complete, the callback function will be called with BK_HIDD_UNREGISTER_APP_EVT.

    返回
    :   - BK_OK: success

        - other: failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_hid_device_connect([bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr)[](#_CPPv424bk_bt_hid_device_connect12bk_bd_addr_t "永久链接至目标")
:   Connects to the peer HID Host with virtual cable. This function should be called after [bk_bluetooth_init()](dual_ble.md#group__dm__bluetooth_1ga577c57a04b4b4589adfb5736442015a2 "dual_ble.md#group__dm__bluetooth_1ga577c57a04b4b4589adfb5736442015a2") success, and should be called after bk_bt_hid_device_init(). When the operation is complete, the callback function will be called with BK_HIDD_OPEN_EVT.

    参数
    :   **bd_addr** – **[in]** Remote host bluetooth device address.

    返回
    :   - BK_OK: success

        - other: failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_hid_device_disconnect(void)[](#_CPPv427bk_bt_hid_device_disconnectv "永久链接至目标")
:   Disconnects from the currently connected HID Host. This function should be called after [bk_bluetooth_init()](dual_ble.md#group__dm__bluetooth_1ga577c57a04b4b4589adfb5736442015a2 "dual_ble.md#group__dm__bluetooth_1ga577c57a04b4b4589adfb5736442015a2") success, and should be called after bk_bt_hid_device_init(). When the operation is complete, the callback function will be called with BK_HIDD_CLOSE_EVT.

    备注

    The disconnect operation will not remove the virtually cabled device. If the connect request from the different HID Host, it will reject the request.

    返回
    :   - BK_OK: success

        - other: failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_hid_device_send_report(uint16_t len, uint8_t *data)[](#_CPPv428bk_bt_hid_device_send_report8uint16_tP7uint8_t "永久链接至目标")
:   Sends HID report to the currently connected HID Host. This function should be called after [bk_bluetooth_init()](dual_ble.md#group__dm__bluetooth_1ga577c57a04b4b4589adfb5736442015a2 "dual_ble.md#group__dm__bluetooth_1ga577c57a04b4b4589adfb5736442015a2") success, and should be called after bk_bt_hid_device_init(). When the operation is complete, the callback function will be called with BK_HIDD_SEND_REPORT_EVT.

    参数
    :   - **len** – **[in]** length of report

        - **data** – **[in]** report data

    返回
    :   - BK_OK: success

        - other: failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_hid_device_send_response(uint8_t message_type, uint8_t res_status, uint16_t len, uint8_t *data)[](#_CPPv430bk_bt_hid_device_send_response7uint8_t7uint8_t8uint16_tP7uint8_t "永久链接至目标")
:   Sends HID Handshake with error info for invalid set_report to the currently connected HID Host. This function should be called after [bk_bluetooth_init()](dual_ble.md#group__dm__bluetooth_1ga577c57a04b4b4589adfb5736442015a2 "dual_ble.md#group__dm__bluetooth_1ga577c57a04b4b4589adfb5736442015a2") success, and should be called after bk_bt_hid_device_init(). When the operation is complete, the callback function will be called with BK_HIDD_REPORT_ERR_EVT.

    参数
    :   - **message_type** – **[in]** type of hid message

        - **res_status** – **[in]** response status

        - **len** – **[in]** response data len

        - **data** – **[in]** response data

    返回
    :   - BK_OK: success

        - other: failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_hid_device_virtual_cable_unplug(void)[](#_CPPv437bk_bt_hid_device_virtual_cable_unplugv "永久链接至目标")
:   Remove the virtually cabled device. This function should be called after [bk_bluetooth_init()](dual_ble.md#group__dm__bluetooth_1ga577c57a04b4b4589adfb5736442015a2 "dual_ble.md#group__dm__bluetooth_1ga577c57a04b4b4589adfb5736442015a2") success, and should be called after bk_bt_hid_device_init(). When the operation is complete, the callback function will be called with BK_HIDD_VC_UNPLUG_EVT.

    备注

    If the connection exists, then HID Device will send a `VIRTUAL_CABLE_UNPLUG` control command to the peer HID Host, and the connection will be destroyed. If the connection does not exist, then HID Device will only unplug on it’s single side. Once the unplug operation is success, the related pairing and bonding information will be removed, then the HID Device can accept connection request from the different HID Host,

    返回
    :   - BK_OK: success


        - other: failed


### Unions[](#unions "永久链接至标题")

union bk_hidd_cb_param_t[](#_CPPv418bk_hidd_cb_param_t "永久链接至目标")
:   *#include <bk_dm_hidd.h>*

    HID device callback parameters union.

    Public Members

    struct [bk_hidd_cb_param_t](#_CPPv418bk_hidd_cb_param_t "bk_hidd_cb_param_t")::[hidd_init_evt_param](#_CPPv4N18bk_hidd_cb_param_t19hidd_init_evt_paramE "bk_hidd_cb_param_t::hidd_init_evt_param") init[](#_CPPv4N18bk_hidd_cb_param_t4initE "永久链接至目标")
    :   HIDD callback param of BK_HIDD_INIT_EVT

    struct [bk_hidd_cb_param_t](#_CPPv418bk_hidd_cb_param_t "bk_hidd_cb_param_t")::[hidd_deinit_evt_param](#_CPPv4N18bk_hidd_cb_param_t21hidd_deinit_evt_paramE "bk_hidd_cb_param_t::hidd_deinit_evt_param") deinit[](#_CPPv4N18bk_hidd_cb_param_t6deinitE "永久链接至目标")
    :   HIDD callback param of BK_HIDD_DEINIT_EVT

    struct [bk_hidd_cb_param_t](#_CPPv418bk_hidd_cb_param_t "bk_hidd_cb_param_t")::[hidd_register_app_evt_param](#_CPPv4N18bk_hidd_cb_param_t27hidd_register_app_evt_paramE "bk_hidd_cb_param_t::hidd_register_app_evt_param") register_app[](#_CPPv4N18bk_hidd_cb_param_t12register_appE "永久链接至目标")
    :   HIDD callback param of BK_HIDD_REGISTER_APP_EVT

    struct [bk_hidd_cb_param_t](#_CPPv418bk_hidd_cb_param_t "bk_hidd_cb_param_t")::[hidd_unregister_app_evt_param](#_CPPv4N18bk_hidd_cb_param_t29hidd_unregister_app_evt_paramE "bk_hidd_cb_param_t::hidd_unregister_app_evt_param") unregister_app[](#_CPPv4N18bk_hidd_cb_param_t14unregister_appE "永久链接至目标")
    :   HIDD callback param of BK_HIDD_UNREGISTER_APP_EVT

    struct [bk_hidd_cb_param_t](#_CPPv418bk_hidd_cb_param_t "bk_hidd_cb_param_t")::[hidd_open_evt_param](#_CPPv4N18bk_hidd_cb_param_t19hidd_open_evt_paramE "bk_hidd_cb_param_t::hidd_open_evt_param") open[](#_CPPv4N18bk_hidd_cb_param_t4openE "永久链接至目标")
    :   HIDD callback param of BK_HIDD_OPEN_EVT

    struct [bk_hidd_cb_param_t](#_CPPv418bk_hidd_cb_param_t "bk_hidd_cb_param_t")::[hidd_close_evt_param](#_CPPv4N18bk_hidd_cb_param_t20hidd_close_evt_paramE "bk_hidd_cb_param_t::hidd_close_evt_param") close[](#_CPPv4N18bk_hidd_cb_param_t5closeE "永久链接至目标")
    :   HIDD callback param of BK_HIDD_CLOSE_EVT

    struct [bk_hidd_cb_param_t](#_CPPv418bk_hidd_cb_param_t "bk_hidd_cb_param_t")::[hidd_send_report_evt_param](#_CPPv4N18bk_hidd_cb_param_t26hidd_send_report_evt_paramE "bk_hidd_cb_param_t::hidd_send_report_evt_param") send_report[](#_CPPv4N18bk_hidd_cb_param_t11send_reportE "永久链接至目标")
    :   HIDD callback param of BK_HIDD_SEND_REPORT_EVT

    struct [bk_hidd_cb_param_t](#_CPPv418bk_hidd_cb_param_t "bk_hidd_cb_param_t")::[hidd_report_err_evt_param](#_CPPv4N18bk_hidd_cb_param_t25hidd_report_err_evt_paramE "bk_hidd_cb_param_t::hidd_report_err_evt_param") report_err[](#_CPPv4N18bk_hidd_cb_param_t10report_errE "永久链接至目标")
    :   HIDD callback param of BK_HIDD_REPORT_ERR_EVT

    struct [bk_hidd_cb_param_t](#_CPPv418bk_hidd_cb_param_t "bk_hidd_cb_param_t")::[hidd_get_report_evt_param](#_CPPv4N18bk_hidd_cb_param_t25hidd_get_report_evt_paramE "bk_hidd_cb_param_t::hidd_get_report_evt_param") get_report[](#_CPPv4N18bk_hidd_cb_param_t10get_reportE "永久链接至目标")
    :   HIDD callback param of BK_HIDD_GET_REPORT_EVT

    struct [bk_hidd_cb_param_t](#_CPPv418bk_hidd_cb_param_t "bk_hidd_cb_param_t")::[hidd_set_report_evt_param](#_CPPv4N18bk_hidd_cb_param_t25hidd_set_report_evt_paramE "bk_hidd_cb_param_t::hidd_set_report_evt_param") set_report[](#_CPPv4N18bk_hidd_cb_param_t10set_reportE "永久链接至目标")
    :   HIDD callback param of BK_HIDD_SET_REPORT_EVT

    struct [bk_hidd_cb_param_t](#_CPPv418bk_hidd_cb_param_t "bk_hidd_cb_param_t")::[hidd_set_protocol_evt_param](#_CPPv4N18bk_hidd_cb_param_t27hidd_set_protocol_evt_paramE "bk_hidd_cb_param_t::hidd_set_protocol_evt_param") set_protocol[](#_CPPv4N18bk_hidd_cb_param_t12set_protocolE "永久链接至目标")
    :   HIDD callback param of BK_HIDD_SET_PROTOCOL_EVT

    struct [bk_hidd_cb_param_t](#_CPPv418bk_hidd_cb_param_t "bk_hidd_cb_param_t")::[hidd_get_protocol_evt_param](#_CPPv4N18bk_hidd_cb_param_t27hidd_get_protocol_evt_paramE "bk_hidd_cb_param_t::hidd_get_protocol_evt_param") get_protocol[](#_CPPv4N18bk_hidd_cb_param_t12get_protocolE "永久链接至目标")
    :   HIDD callback param of BK_HIDD_GET_PROTOCOL_EVT

    struct [bk_hidd_cb_param_t](#_CPPv418bk_hidd_cb_param_t "bk_hidd_cb_param_t")::[hidd_get_idle_evt_param](#_CPPv4N18bk_hidd_cb_param_t23hidd_get_idle_evt_paramE "bk_hidd_cb_param_t::hidd_get_idle_evt_param") get_idle[](#_CPPv4N18bk_hidd_cb_param_t8get_idleE "永久链接至目标")
    :   HIDD callback param of BK_HIDD_GET_IDLE_EVT

    struct [bk_hidd_cb_param_t](#_CPPv418bk_hidd_cb_param_t "bk_hidd_cb_param_t")::[hidd_set_idle_evt_param](#_CPPv4N18bk_hidd_cb_param_t23hidd_set_idle_evt_paramE "bk_hidd_cb_param_t::hidd_set_idle_evt_param") set_idle[](#_CPPv4N18bk_hidd_cb_param_t8set_idleE "永久链接至目标")
    :   HIDD callback param of BK_HIDD_SET_IDLE_EVT

    struct [bk_hidd_cb_param_t](#_CPPv418bk_hidd_cb_param_t "bk_hidd_cb_param_t")::[hidd_intr_data_evt_param](#_CPPv4N18bk_hidd_cb_param_t24hidd_intr_data_evt_paramE "bk_hidd_cb_param_t::hidd_intr_data_evt_param") intr_data[](#_CPPv4N18bk_hidd_cb_param_t9intr_dataE "永久链接至目标")
    :   HIDD callback param of BK_HIDD_INTR_DATA_EVT

    struct [bk_hidd_cb_param_t](#_CPPv418bk_hidd_cb_param_t "bk_hidd_cb_param_t")::[hidd_ctrl_op_evt_param](#_CPPv4N18bk_hidd_cb_param_t22hidd_ctrl_op_evt_paramE "bk_hidd_cb_param_t::hidd_ctrl_op_evt_param") ctrl_op[](#_CPPv4N18bk_hidd_cb_param_t7ctrl_opE "永久链接至目标")
    :   HIDD callback param of BK_HIDD_INTR_DATA_EVT

    struct [bk_hidd_cb_param_t](#_CPPv418bk_hidd_cb_param_t "bk_hidd_cb_param_t")::[hidd_vc_unplug_param](#_CPPv4N18bk_hidd_cb_param_t20hidd_vc_unplug_paramE "bk_hidd_cb_param_t::hidd_vc_unplug_param") vc_unplug[](#_CPPv4N18bk_hidd_cb_param_t9vc_unplugE "永久链接至目标")
    :   HIDD callback param of BK_HIDD_VC_UNPLUG_EVT

    struct hidd_close_evt_param[](#_CPPv4N18bk_hidd_cb_param_t20hidd_close_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidd.h>*

        BK_HIDD_CLOSE_EVT.

        Public Members

        [bk_hidd_status_t](#_CPPv416bk_hidd_status_t "bk_hidd_status_t") status[](#_CPPv4N18bk_hidd_cb_param_t20hidd_close_evt_param6statusE "永久链接至目标")
        :   operation status

        [bk_hidd_connection_state_t](#_CPPv426bk_hidd_connection_state_t "bk_hidd_connection_state_t") conn_status[](#_CPPv4N18bk_hidd_cb_param_t20hidd_close_evt_param11conn_statusE "永久链接至目标")
        :   connection status

    struct hidd_ctrl_op_evt_param[](#_CPPv4N18bk_hidd_cb_param_t22hidd_ctrl_op_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidd.h>*

        BK_HIDD_CTRL_OP_EVT.

        Public Members

        [bk_hidd_message_type_t](#_CPPv422bk_hidd_message_type_t "bk_hidd_message_type_t") message_type[](#_CPPv4N18bk_hidd_cb_param_t22hidd_ctrl_op_evt_param12message_typeE "永久链接至目标")
        :   message type

        [bk_hidd_ctrl_op_t](#_CPPv417bk_hidd_ctrl_op_t "bk_hidd_ctrl_op_t") op[](#_CPPv4N18bk_hidd_cb_param_t22hidd_ctrl_op_evt_param2opE "永久链接至目标")
        :   ctral operation

    struct hidd_deinit_evt_param[](#_CPPv4N18bk_hidd_cb_param_t21hidd_deinit_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidd.h>*

        BK_HIDD_DEINIT_EVT.

        Public Members

        [bk_hidd_status_t](#_CPPv416bk_hidd_status_t "bk_hidd_status_t") status[](#_CPPv4N18bk_hidd_cb_param_t21hidd_deinit_evt_param6statusE "永久链接至目标")
        :   operation status

    struct hidd_get_idle_evt_param[](#_CPPv4N18bk_hidd_cb_param_t23hidd_get_idle_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidd.h>*

        BK_HIDD_GET_IDLE_EVT.

        Public Members

        [bk_hidd_message_type_t](#_CPPv422bk_hidd_message_type_t "bk_hidd_message_type_t") message_type[](#_CPPv4N18bk_hidd_cb_param_t23hidd_get_idle_evt_param12message_typeE "永久链接至目标")
        :   message type

    struct hidd_get_protocol_evt_param[](#_CPPv4N18bk_hidd_cb_param_t27hidd_get_protocol_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidd.h>*

        BK_HIDD_GET_PROTOCOL_EVT.

        Public Members

        [bk_hidd_message_type_t](#_CPPv422bk_hidd_message_type_t "bk_hidd_message_type_t") message_type[](#_CPPv4N18bk_hidd_cb_param_t27hidd_get_protocol_evt_param12message_typeE "永久链接至目标")
        :   message type

    struct hidd_get_report_evt_param[](#_CPPv4N18bk_hidd_cb_param_t25hidd_get_report_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidd.h>*

        BK_HIDD_GET_REPORT_EVT.

        Public Members

        [bk_hidd_message_type_t](#_CPPv422bk_hidd_message_type_t "bk_hidd_message_type_t") message_type[](#_CPPv4N18bk_hidd_cb_param_t25hidd_get_report_evt_param12message_typeE "永久链接至目标")
        :   message type

        [bk_hidd_report_type_t](#_CPPv421bk_hidd_report_type_t "bk_hidd_report_type_t") report_type[](#_CPPv4N18bk_hidd_cb_param_t25hidd_get_report_evt_param11report_typeE "永久链接至目标")
        :   report type

        uint8_t report_id[](#_CPPv4N18bk_hidd_cb_param_t25hidd_get_report_evt_param9report_idE "永久链接至目标")
        :   report id

        uint16_t buffer_size[](#_CPPv4N18bk_hidd_cb_param_t25hidd_get_report_evt_param11buffer_sizeE "永久链接至目标")
        :   buffer size

    struct hidd_init_evt_param[](#_CPPv4N18bk_hidd_cb_param_t19hidd_init_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidd.h>*

        BK_HIDD_INIT_EVT.

        Public Members

        [bk_hidd_status_t](#_CPPv416bk_hidd_status_t "bk_hidd_status_t") status[](#_CPPv4N18bk_hidd_cb_param_t19hidd_init_evt_param6statusE "永久链接至目标")
        :   operation status

    struct hidd_intr_data_evt_param[](#_CPPv4N18bk_hidd_cb_param_t24hidd_intr_data_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidd.h>*

        BK_HIDD_INTR_DATA_EVT.

        Public Members

        [bk_hidd_message_type_t](#_CPPv422bk_hidd_message_type_t "bk_hidd_message_type_t") message_type[](#_CPPv4N18bk_hidd_cb_param_t24hidd_intr_data_evt_param12message_typeE "永久链接至目标")
        :   message type

        [bk_hidd_report_type_t](#_CPPv421bk_hidd_report_type_t "bk_hidd_report_type_t") report_type[](#_CPPv4N18bk_hidd_cb_param_t24hidd_intr_data_evt_param11report_typeE "永久链接至目标")
        :   report type

        uint8_t report_id[](#_CPPv4N18bk_hidd_cb_param_t24hidd_intr_data_evt_param9report_idE "永久链接至目标")
        :   interrupt channel report id

        uint16_t len[](#_CPPv4N18bk_hidd_cb_param_t24hidd_intr_data_evt_param3lenE "永久链接至目标")
        :   interrupt channel report data length

        uint8_t *data[](#_CPPv4N18bk_hidd_cb_param_t24hidd_intr_data_evt_param4dataE "永久链接至目标")
        :   interrupt channel report data pointer

    struct hidd_open_evt_param[](#_CPPv4N18bk_hidd_cb_param_t19hidd_open_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidd.h>*

        BK_HIDD_OPEN_EVT.

        Public Members

        [bk_hidd_status_t](#_CPPv416bk_hidd_status_t "bk_hidd_status_t") status[](#_CPPv4N18bk_hidd_cb_param_t19hidd_open_evt_param6statusE "永久链接至目标")
        :   operation status

        [bk_hidd_connection_state_t](#_CPPv426bk_hidd_connection_state_t "bk_hidd_connection_state_t") conn_status[](#_CPPv4N18bk_hidd_cb_param_t19hidd_open_evt_param11conn_statusE "永久链接至目标")
        :   connection status

        [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr[](#_CPPv4N18bk_hidd_cb_param_t19hidd_open_evt_param7bd_addrE "永久链接至目标")
        :   host address

    struct hidd_register_app_evt_param[](#_CPPv4N18bk_hidd_cb_param_t27hidd_register_app_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidd.h>*

        BK_HIDD_REGISTER_APP_EVT.

        Public Members

        [bk_hidd_status_t](#_CPPv416bk_hidd_status_t "bk_hidd_status_t") status[](#_CPPv4N18bk_hidd_cb_param_t27hidd_register_app_evt_param6statusE "永久链接至目标")
        :   operation status

        bool in_use[](#_CPPv4N18bk_hidd_cb_param_t27hidd_register_app_evt_param6in_useE "永久链接至目标")
        :   indicate whether use virtual cable plug host address

        [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr[](#_CPPv4N18bk_hidd_cb_param_t27hidd_register_app_evt_param7bd_addrE "永久链接至目标")
        :   host address

    struct hidd_report_err_evt_param[](#_CPPv4N18bk_hidd_cb_param_t25hidd_report_err_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidd.h>*

        BK_HIDD_REPORT_ERR_EVT.

        Public Members

        [bk_hidd_status_t](#_CPPv416bk_hidd_status_t "bk_hidd_status_t") status[](#_CPPv4N18bk_hidd_cb_param_t25hidd_report_err_evt_param6statusE "永久链接至目标")
        :   operation status

        uint8_t reason[](#_CPPv4N18bk_hidd_cb_param_t25hidd_report_err_evt_param6reasonE "永久链接至目标")
        :   lower layer failed reason(ref hiddefs.h)

    struct hidd_send_report_evt_param[](#_CPPv4N18bk_hidd_cb_param_t26hidd_send_report_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidd.h>*

        BK_HIDD_SEND_REPORT_EVT.

        Public Members

        [bk_hidd_status_t](#_CPPv416bk_hidd_status_t "bk_hidd_status_t") status[](#_CPPv4N18bk_hidd_cb_param_t26hidd_send_report_evt_param6statusE "永久链接至目标")
        :   operation status

        uint8_t report_id[](#_CPPv4N18bk_hidd_cb_param_t26hidd_send_report_evt_param9report_idE "永久链接至目标")
        :   report id

    struct hidd_set_idle_evt_param[](#_CPPv4N18bk_hidd_cb_param_t23hidd_set_idle_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidd.h>*

        BK_HIDD_SET_IDLE_EVT.

        Public Members

        [bk_hidd_message_type_t](#_CPPv422bk_hidd_message_type_t "bk_hidd_message_type_t") message_type[](#_CPPv4N18bk_hidd_cb_param_t23hidd_set_idle_evt_param12message_typeE "永久链接至目标")
        :   message type

        uint8_t idle[](#_CPPv4N18bk_hidd_cb_param_t23hidd_set_idle_evt_param4idleE "永久链接至目标")
        :   idle rate

    struct hidd_set_protocol_evt_param[](#_CPPv4N18bk_hidd_cb_param_t27hidd_set_protocol_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidd.h>*

        BK_HIDD_SET_PROTOCOL_EVT.

        Public Members

        [bk_hidd_protocol_mode_t](#_CPPv423bk_hidd_protocol_mode_t "bk_hidd_protocol_mode_t") protocol_mode[](#_CPPv4N18bk_hidd_cb_param_t27hidd_set_protocol_evt_param13protocol_modeE "永久链接至目标")
        :   protocol mode

    struct hidd_set_report_evt_param[](#_CPPv4N18bk_hidd_cb_param_t25hidd_set_report_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidd.h>*

        BK_HIDD_SET_REPORT_EVT.

        Public Members

        [bk_hidd_message_type_t](#_CPPv422bk_hidd_message_type_t "bk_hidd_message_type_t") message_type[](#_CPPv4N18bk_hidd_cb_param_t25hidd_set_report_evt_param12message_typeE "永久链接至目标")
        :   message type

        [bk_hidd_report_type_t](#_CPPv421bk_hidd_report_type_t "bk_hidd_report_type_t") report_type[](#_CPPv4N18bk_hidd_cb_param_t25hidd_set_report_evt_param11report_typeE "永久链接至目标")
        :   report type

        uint8_t report_id[](#_CPPv4N18bk_hidd_cb_param_t25hidd_set_report_evt_param9report_idE "永久链接至目标")
        :   report id

        uint16_t len[](#_CPPv4N18bk_hidd_cb_param_t25hidd_set_report_evt_param3lenE "永久链接至目标")
        :   set_report data length

        uint8_t *data[](#_CPPv4N18bk_hidd_cb_param_t25hidd_set_report_evt_param4dataE "永久链接至目标")
        :   set_report data pointer

    struct hidd_unregister_app_evt_param[](#_CPPv4N18bk_hidd_cb_param_t29hidd_unregister_app_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidd.h>*

        BK_HIDD_UNREGISTER_APP_EVT.

        Public Members

        [bk_hidd_status_t](#_CPPv416bk_hidd_status_t "bk_hidd_status_t") status[](#_CPPv4N18bk_hidd_cb_param_t29hidd_unregister_app_evt_param6statusE "永久链接至目标")
        :   operation status

    struct hidd_vc_unplug_param[](#_CPPv4N18bk_hidd_cb_param_t20hidd_vc_unplug_paramE "永久链接至目标")
    :   *#include <bk_dm_hidd.h>*

        BK_HIDD_VC_UNPLUG_EVT.

        Public Members

        [bk_hidd_status_t](#_CPPv416bk_hidd_status_t "bk_hidd_status_t") status[](#_CPPv4N18bk_hidd_cb_param_t20hidd_vc_unplug_param6statusE "永久链接至目标")
        :   operation status

        [bk_hidd_connection_state_t](#_CPPv426bk_hidd_connection_state_t "bk_hidd_connection_state_t") conn_status[](#_CPPv4N18bk_hidd_cb_param_t20hidd_vc_unplug_param11conn_statusE "永久链接至目标")
        :   connection status


### Structures[](#structures "永久链接至标题")

struct bk_hidd_app_param_t[](#_CPPv419bk_hidd_app_param_t "永久链接至目标")
:   HID device characteristics for SDP server.

    Public Members

    char *name[](#_CPPv4N19bk_hidd_app_param_t4nameE "永久链接至目标")
    :   service name

    char *description[](#_CPPv4N19bk_hidd_app_param_t11descriptionE "永久链接至目标")
    :   service description

    char *provider[](#_CPPv4N19bk_hidd_app_param_t8providerE "永久链接至目标")
    :   provider name

    uint8_t *subclass[](#_CPPv4N19bk_hidd_app_param_t8subclassE "永久链接至目标")
    :   HID device subclass

    uint8_t *desc_list[](#_CPPv4N19bk_hidd_app_param_t9desc_listE "永久链接至目标")
    :   HID descriptor list

    int desc_list_len[](#_CPPv4N19bk_hidd_app_param_t13desc_list_lenE "永久链接至目标")
    :   size in bytes of HID descriptor list

struct bk_hidd_qos_param_t[](#_CPPv419bk_hidd_qos_param_t "永久链接至目标")
:   HIDD Quality of Service parameters negotiated over L2CAP.

    Public Members

    uint8_t service_type[](#_CPPv4N19bk_hidd_qos_param_t12service_typeE "永久链接至目标")
    :   the level of service, 0 indicates no traffic

    uint32_t token_rate[](#_CPPv4N19bk_hidd_qos_param_t10token_rateE "永久链接至目标")
    :   token rate in bytes per second, 0 indicates “don’t care”

    uint32_t token_bucket_size[](#_CPPv4N19bk_hidd_qos_param_t17token_bucket_sizeE "永久链接至目标")
    :   limit on the burstness of the application data

    uint32_t peak_bandwidth[](#_CPPv4N19bk_hidd_qos_param_t14peak_bandwidthE "永久链接至目标")
    :   bytes per second, value 0 indicates “don’t care”

    uint32_t access_latency[](#_CPPv4N19bk_hidd_qos_param_t14access_latencyE "永久链接至目标")
    :   maximum acceptable delay in microseconds

    uint32_t delay_variation[](#_CPPv4N19bk_hidd_qos_param_t15delay_variationE "永久链接至目标")
    :   the difference in microseconds between the max and min delay


### Macros[](#macros "永久链接至标题")

BK_HID_CLASS_UNKNOWN[](#c.BK_HID_CLASS_UNKNOWN "永久链接至目标")
:   subclass of hid device

    unknown HID device subclass

BK_HID_CLASS_JOS[](#c.BK_HID_CLASS_JOS "永久链接至目标")
:   joystick

BK_HID_CLASS_GPD[](#c.BK_HID_CLASS_GPD "永久链接至目标")
:   game pad

BK_HID_CLASS_RMC[](#c.BK_HID_CLASS_RMC "永久链接至目标")
:   remote control

BK_HID_CLASS_SED[](#c.BK_HID_CLASS_SED "永久链接至目标")
:   sensing device

BK_HID_CLASS_DGT[](#c.BK_HID_CLASS_DGT "永久链接至目标")
:   digitizer tablet

BK_HID_CLASS_CDR[](#c.BK_HID_CLASS_CDR "永久链接至目标")
:   card reader

BK_HID_CLASS_KBD[](#c.BK_HID_CLASS_KBD "永久链接至目标")
:   keyboard

BK_HID_CLASS_MIC[](#c.BK_HID_CLASS_MIC "永久链接至目标")
:   pointing device

BK_HID_CLASS_COM[](#c.BK_HID_CLASS_COM "永久链接至目标")
:   combo keyboard/pointing


### Type Definitions[](#type-definitions "永久链接至标题")

typedef void (*bk_hd_cb_t)([bk_hidd_cb_event_t](#_CPPv418bk_hidd_cb_event_t "bk_hidd_cb_event_t") event, [bk_hidd_cb_param_t](#_CPPv418bk_hidd_cb_param_t "bk_hidd_cb_param_t") *param)[](#_CPPv410bk_hd_cb_t "永久链接至目标")
:   HID device callback function type.

    Param event
    :   Event type

    Param param
    :   Point to callback parameter, currently is union type


### Enumerations[](#enumerations "永久链接至标题")

enum bk_hidd_handshake_error_t[](#_CPPv425bk_hidd_handshake_error_t "永久链接至目标")
:   HIDD handshake result code.


    *Values:*

    enumerator BK_HID_PAR_HANDSHAKE_RSP_SUCCESS[](#_CPPv4N25bk_hidd_handshake_error_t32BK_HID_PAR_HANDSHAKE_RSP_SUCCESSE "永久链接至目标")
    :   successful

    enumerator BK_HID_PAR_HANDSHAKE_RSP_NOT_READY[](#_CPPv4N25bk_hidd_handshake_error_t34BK_HID_PAR_HANDSHAKE_RSP_NOT_READYE "永久链接至目标")
    :   not ready, device is too busy to accept data

    enumerator BK_HID_PAR_HANDSHAKE_RSP_ERR_INVALID_REP_ID[](#_CPPv4N25bk_hidd_handshake_error_t43BK_HID_PAR_HANDSHAKE_RSP_ERR_INVALID_REP_IDE "永久链接至目标")
    :   invalid report ID

    enumerator BK_HID_PAR_HANDSHAKE_RSP_ERR_UNSUPPORTED_REQ[](#_CPPv4N25bk_hidd_handshake_error_t44BK_HID_PAR_HANDSHAKE_RSP_ERR_UNSUPPORTED_REQE "永久链接至目标")
    :   device does not support the request

    enumerator BK_HID_PAR_HANDSHAKE_RSP_ERR_INVALID_PARAM[](#_CPPv4N25bk_hidd_handshake_error_t42BK_HID_PAR_HANDSHAKE_RSP_ERR_INVALID_PARAME "永久链接至目标")
    :   parameter value is out of range or inappropriate

    enumerator BK_HID_PAR_HANDSHAKE_RSP_ERR_UNKNOWN[](#_CPPv4N25bk_hidd_handshake_error_t36BK_HID_PAR_HANDSHAKE_RSP_ERR_UNKNOWNE "永久链接至目标")
    :   device could not identify the error condition

    enumerator BK_HID_PAR_HANDSHAKE_RSP_ERR_FATAL[](#_CPPv4N25bk_hidd_handshake_error_t34BK_HID_PAR_HANDSHAKE_RSP_ERR_FATALE "永久链接至目标")
    :   restart is essential to resume functionality

enum bk_hidd_message_type_t[](#_CPPv422bk_hidd_message_type_t "永久链接至目标")
:   HIDD message types.


    *Values:*

    enumerator BK_HIDD_MESSAGE_TYPE_HANDSHAKE[](#_CPPv4N22bk_hidd_message_type_t30BK_HIDD_MESSAGE_TYPE_HANDSHAKEE "永久链接至目标")
    :   handshake type

    enumerator BK_HIDD_MESSAGE_TYPE_HID_CONTROL[](#_CPPv4N22bk_hidd_message_type_t32BK_HIDD_MESSAGE_TYPE_HID_CONTROLE "永久链接至目标")
    :   hid control type

    enumerator BK_HIDD_MESSAGE_TYPE_GET_REPORT[](#_CPPv4N22bk_hidd_message_type_t31BK_HIDD_MESSAGE_TYPE_GET_REPORTE "永久链接至目标")
    :   get report

    enumerator BK_HIDD_MESSAGE_TYPE_SET_REPORT[](#_CPPv4N22bk_hidd_message_type_t31BK_HIDD_MESSAGE_TYPE_SET_REPORTE "永久链接至目标")
    :   set report

    enumerator BK_HIDD_MESSAGE_TYPE_GET_PROTOCOL[](#_CPPv4N22bk_hidd_message_type_t33BK_HIDD_MESSAGE_TYPE_GET_PROTOCOLE "永久链接至目标")
    :   get protocol

    enumerator BK_HIDD_MESSAGE_TYPE_SET_PROTOCOL[](#_CPPv4N22bk_hidd_message_type_t33BK_HIDD_MESSAGE_TYPE_SET_PROTOCOLE "永久链接至目标")
    :   set protocol

    enumerator BK_HIDD_MESSAGE_TYPE_GET_IDLE[](#_CPPv4N22bk_hidd_message_type_t29BK_HIDD_MESSAGE_TYPE_GET_IDLEE "永久链接至目标")
    :   get idle [DEPRECATED]

    enumerator BK_HIDD_MESSAGE_TYPE_SET_IDLE[](#_CPPv4N22bk_hidd_message_type_t29BK_HIDD_MESSAGE_TYPE_SET_IDLEE "永久链接至目标")
    :   set idle [DEPRECATED]

    enumerator BK_HIDD_MESSAGE_TYPE_DATA[](#_CPPv4N22bk_hidd_message_type_t25BK_HIDD_MESSAGE_TYPE_DATAE "永久链接至目标")
    :   data intr

enum bk_hidd_report_type_t[](#_CPPv421bk_hidd_report_type_t "永久链接至目标")
:   HIDD report types.


    *Values:*

    enumerator BK_HIDD_REPORT_TYPE_RESERVED[](#_CPPv4N21bk_hidd_report_type_t28BK_HIDD_REPORT_TYPE_RESERVEDE "永久链接至目标")
    :   reserved

    enumerator BK_HIDD_REPORT_TYPE_INPUT[](#_CPPv4N21bk_hidd_report_type_t25BK_HIDD_REPORT_TYPE_INPUTE "永久链接至目标")
    :   input report

    enumerator BK_HIDD_REPORT_TYPE_OUTPUT[](#_CPPv4N21bk_hidd_report_type_t26BK_HIDD_REPORT_TYPE_OUTPUTE "永久链接至目标")
    :   output report

    enumerator BK_HIDD_REPORT_TYPE_FEATURE[](#_CPPv4N21bk_hidd_report_type_t27BK_HIDD_REPORT_TYPE_FEATUREE "永久链接至目标")
    :   feature report

enum bk_hidd_ctrl_op_t[](#_CPPv417bk_hidd_ctrl_op_t "永久链接至目标")
:   HIDD control operation.


    *Values:*

    enumerator BK_HIDD_CTRL_OP_NOP[](#_CPPv4N17bk_hidd_ctrl_op_t19BK_HIDD_CTRL_OP_NOPE "永久链接至目标")
    :   no operation

    enumerator BK_HIDD_CTRL_OP_HARD_RESET[](#_CPPv4N17bk_hidd_ctrl_op_t26BK_HIDD_CTRL_OP_HARD_RESETE "永久链接至目标")
    :   hadr reset

    enumerator BK_HIDD_CTRL_OP_SOFT_RESET[](#_CPPv4N17bk_hidd_ctrl_op_t26BK_HIDD_CTRL_OP_SOFT_RESETE "永久链接至目标")
    :   soft reset

    enumerator BK_HIDD_CTRL_OP_SUSPEND[](#_CPPv4N17bk_hidd_ctrl_op_t23BK_HIDD_CTRL_OP_SUSPENDE "永久链接至目标")
    :   suspend

    enumerator BK_HIDD_CTRL_OP_EXIT_SUSPEND[](#_CPPv4N17bk_hidd_ctrl_op_t28BK_HIDD_CTRL_OP_EXIT_SUSPENDE "永久链接至目标")
    :   exit suspend

enum bk_hidd_connection_state_t[](#_CPPv426bk_hidd_connection_state_t "永久链接至目标")
:   HIDD connection state.


    *Values:*

    enumerator BK_HIDD_CONN_STATE_CONNECTED[](#_CPPv4N26bk_hidd_connection_state_t28BK_HIDD_CONN_STATE_CONNECTEDE "永久链接至目标")
    :   HID connection established

    enumerator BK_HIDD_CONN_STATE_CONNECTING[](#_CPPv4N26bk_hidd_connection_state_t29BK_HIDD_CONN_STATE_CONNECTINGE "永久链接至目标")
    :   connection to remote Bluetooth device

    enumerator BK_HIDD_CONN_STATE_DISCONNECTED[](#_CPPv4N26bk_hidd_connection_state_t31BK_HIDD_CONN_STATE_DISCONNECTEDE "永久链接至目标")
    :   connection released

    enumerator BK_HIDD_CONN_STATE_DISCONNECTING[](#_CPPv4N26bk_hidd_connection_state_t32BK_HIDD_CONN_STATE_DISCONNECTINGE "永久链接至目标")
    :   disconnecting to remote Bluetooth device

    enumerator BK_HIDD_CONN_STATE_UNKNOWN[](#_CPPv4N26bk_hidd_connection_state_t26BK_HIDD_CONN_STATE_UNKNOWNE "永久链接至目标")
    :   unknown connection state

enum bk_hidd_protocol_mode_t[](#_CPPv423bk_hidd_protocol_mode_t "永久链接至目标")
:   HID device protocol modes.


    *Values:*

    enumerator BK_HIDD_REPORT_MODE[](#_CPPv4N23bk_hidd_protocol_mode_t19BK_HIDD_REPORT_MODEE "永久链接至目标")
    :   Report Protocol Mode

    enumerator BK_HIDD_BOOT_MODE[](#_CPPv4N23bk_hidd_protocol_mode_t17BK_HIDD_BOOT_MODEE "永久链接至目标")
    :   Boot Protocol Mode

    enumerator BK_HIDD_UNSUPPORTED_MODE[](#_CPPv4N23bk_hidd_protocol_mode_t24BK_HIDD_UNSUPPORTED_MODEE "永久链接至目标")
    :   unsupported

enum bk_hidd_boot_report_id_t[](#_CPPv424bk_hidd_boot_report_id_t "永久链接至目标")
:   HID Boot Protocol report IDs.


    *Values:*

    enumerator BK_HIDD_BOOT_REPORT_ID_KEYBOARD[](#_CPPv4N24bk_hidd_boot_report_id_t31BK_HIDD_BOOT_REPORT_ID_KEYBOARDE "永久链接至目标")
    :   report ID of Boot Protocol keyboard report

    enumerator BK_HIDD_BOOT_REPORT_ID_MOUSE[](#_CPPv4N24bk_hidd_boot_report_id_t28BK_HIDD_BOOT_REPORT_ID_MOUSEE "永久链接至目标")
    :   report ID of Boot Protocol mouse report

enum [anonymous][](#_CPPv4Ut2_19 "永久链接至目标")
:   HID Boot Protocol report size including report ID.


    *Values:*

    enumerator BK_HIDD_BOOT_REPORT_SIZE_KEYBOARD[](#_CPPv4NUt2_1933BK_HIDD_BOOT_REPORT_SIZE_KEYBOARDE "永久链接至目标")
    :   report size of Boot Protocol keyboard report

    enumerator BK_HIDD_BOOT_REPORT_SIZE_MOUSE[](#_CPPv4NUt2_1930BK_HIDD_BOOT_REPORT_SIZE_MOUSEE "永久链接至目标")
    :   report size of Boot Protocol mouse report

enum bk_hidd_cb_event_t[](#_CPPv418bk_hidd_cb_event_t "永久链接至目标")
:   HID device callback function events.


    *Values:*

    enumerator BK_HIDD_INIT_EVT[](#_CPPv4N18bk_hidd_cb_event_t16BK_HIDD_INIT_EVTE "永久链接至目标")
    :   When HID device is initialized, the event comes

    enumerator BK_HIDD_DEINIT_EVT[](#_CPPv4N18bk_hidd_cb_event_t18BK_HIDD_DEINIT_EVTE "永久链接至目标")
    :   When HID device is deinitialized, the event comes

    enumerator BK_HIDD_REGISTER_APP_EVT[](#_CPPv4N18bk_hidd_cb_event_t24BK_HIDD_REGISTER_APP_EVTE "永久链接至目标")
    :   When HID device application registered, the event comes

    enumerator BK_HIDD_UNREGISTER_APP_EVT[](#_CPPv4N18bk_hidd_cb_event_t26BK_HIDD_UNREGISTER_APP_EVTE "永久链接至目标")
    :   When HID device application unregistered, the event comes

    enumerator BK_HIDD_OPEN_EVT[](#_CPPv4N18bk_hidd_cb_event_t16BK_HIDD_OPEN_EVTE "永久链接至目标")
    :   When HID device connection to host opened, the event comes

    enumerator BK_HIDD_CLOSE_EVT[](#_CPPv4N18bk_hidd_cb_event_t17BK_HIDD_CLOSE_EVTE "永久链接至目标")
    :   When HID device connection to host closed, the event comes

    enumerator BK_HIDD_SEND_REPORT_EVT[](#_CPPv4N18bk_hidd_cb_event_t23BK_HIDD_SEND_REPORT_EVTE "永久链接至目标")
    :   When HID device send report to lower layer, the event comes

    enumerator BK_HIDD_REPORT_ERR_EVT[](#_CPPv4N18bk_hidd_cb_event_t22BK_HIDD_REPORT_ERR_EVTE "永久链接至目标")
    :   When HID device report handshanke error to lower layer, the event comes

    enumerator BK_HIDD_GET_REPORT_EVT[](#_CPPv4N18bk_hidd_cb_event_t22BK_HIDD_GET_REPORT_EVTE "永久链接至目标")
    :   When HID device receives GET_REPORT request from host, the event comes

    enumerator BK_HIDD_SET_REPORT_EVT[](#_CPPv4N18bk_hidd_cb_event_t22BK_HIDD_SET_REPORT_EVTE "永久链接至目标")
    :   When HID device receives SET_REPORT request from host, the event comes

    enumerator BK_HIDD_GET_PROTOCOL_EVT[](#_CPPv4N18bk_hidd_cb_event_t24BK_HIDD_GET_PROTOCOL_EVTE "永久链接至目标")
    :   When HID device receives GET_PROTOCOL request from host, the event comes

    enumerator BK_HIDD_SET_PROTOCOL_EVT[](#_CPPv4N18bk_hidd_cb_event_t24BK_HIDD_SET_PROTOCOL_EVTE "永久链接至目标")
    :   When HID device receives SET_PROTOCOL request from host, the event comes

    enumerator BK_HIDD_GET_IDLE_EVT[](#_CPPv4N18bk_hidd_cb_event_t20BK_HIDD_GET_IDLE_EVTE "永久链接至目标")
    :   When HID device receives GET_IDLE request from host, the event comes

    enumerator BK_HIDD_SET_IDLE_EVT[](#_CPPv4N18bk_hidd_cb_event_t20BK_HIDD_SET_IDLE_EVTE "永久链接至目标")
    :   When HID device receives SET_IDLE request from host, the event comes

    enumerator BK_HIDD_INTR_DATA_EVT[](#_CPPv4N18bk_hidd_cb_event_t21BK_HIDD_INTR_DATA_EVTE "永久链接至目标")
    :   When HID device receives DATA from host on intr, the event comes

    enumerator BK_HIDD_CONTROL_EVT[](#_CPPv4N18bk_hidd_cb_event_t19BK_HIDD_CONTROL_EVTE "永久链接至目标")
    :   When HID device receives HID_CONTROL from host, the event comes

    enumerator BK_HIDD_VC_UNPLUG_EVT[](#_CPPv4N18bk_hidd_cb_event_t21BK_HIDD_VC_UNPLUG_EVTE "永久链接至目标")
    :   When HID device initiates Virtual Cable Unplug, the event comes

    enumerator BK_HIDD_API_ERR_EVT[](#_CPPv4N18bk_hidd_cb_event_t19BK_HIDD_API_ERR_EVTE "永久链接至目标")
    :   When HID device has API error, the event comes

enum bk_hidd_status_t[](#_CPPv416bk_hidd_status_t "永久链接至目标")
:   *Values:*

    enumerator BK_HIDD_SUCCESS[](#_CPPv4N16bk_hidd_status_t15BK_HIDD_SUCCESSE "永久链接至目标")

    enumerator BK_HIDD_ERROR[](#_CPPv4N16bk_hidd_status_t13BK_HIDD_ERRORE "永久链接至目标")
    :   general BK HD error

    enumerator BK_HIDD_NO_RES[](#_CPPv4N16bk_hidd_status_t14BK_HIDD_NO_RESE "永久链接至目标")
    :   out of system resources

    enumerator BK_HIDD_BUSY[](#_CPPv4N16bk_hidd_status_t12BK_HIDD_BUSYE "永久链接至目标")
    :   Temporarily can not handle this request.

    enumerator BK_HIDD_NO_DATA[](#_CPPv4N16bk_hidd_status_t15BK_HIDD_NO_DATAE "永久链接至目标")
    :   No data.

    enumerator BK_HIDD_NEED_INIT[](#_CPPv4N16bk_hidd_status_t17BK_HIDD_NEED_INITE "永久链接至目标")
    :   HIDD module shall init first

    enumerator BK_HIDD_NEED_DEINIT[](#_CPPv4N16bk_hidd_status_t19BK_HIDD_NEED_DEINITE "永久链接至目标")
    :   HIDD module shall deinit first

    enumerator BK_HIDD_NEED_REG[](#_CPPv4N16bk_hidd_status_t16BK_HIDD_NEED_REGE "永久链接至目标")
    :   HIDD module shall register first

    enumerator BK_HIDD_NEED_DEREG[](#_CPPv4N16bk_hidd_status_t18BK_HIDD_NEED_DEREGE "永久链接至目标")
    :   HIDD module shall deregister first

    enumerator BK_HIDD_NO_CONNECTION[](#_CPPv4N16bk_hidd_status_t21BK_HIDD_NO_CONNECTIONE "永久链接至目标")
    :   connection may have been closed

    enumerator BK_HIDD_NO_ACL_LINK[](#_CPPv4N16bk_hidd_status_t19BK_HIDD_NO_ACL_LINKE "永久链接至目标")
    :   Baseband acl link not exist

    enumerator BK_HIDD_FAIL[](#_CPPv4N16bk_hidd_status_t12BK_HIDD_FAILE "永久链接至目标")
    :   HIDD Fail


### Header File[](#id9 "永久链接至标题")


- [bluetooth/bk_dm_hidh.h](https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_hidh.h "https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_hidh.h")


### Functions[](#id10 "永久链接至标题")

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_hid_host_register_callback([bk_hh_cb_t](#_CPPv410bk_hh_cb_t "bk_hh_cb_t") callback)[](#_CPPv432bk_bt_hid_host_register_callback10bk_hh_cb_t "永久链接至目标")
:   This function is called to init callbacks with HID host module.

    参数
    :   **callback** – **[in]** pointer to the init callback function.

    返回
    :   - BK_OK: success

        - other: failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_hid_host_init(void)[](#_CPPv419bk_bt_hid_host_initv "永久链接至目标")
:   This function initializes HID host. This function should be called after [bk_bluetooth_init()](dual_ble.md#group__dm__bluetooth_1ga577c57a04b4b4589adfb5736442015a2 "dual_ble.md#group__dm__bluetooth_1ga577c57a04b4b4589adfb5736442015a2") success, and should be called after bk_bt_hid_host_register_callback(). When the operation is complete the callback function will be called with BK_HIDH_INIT_EVT.

    返回
    :   - BK_OK: success

        - other: failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_hid_host_deinit(void)[](#_CPPv421bk_bt_hid_host_deinitv "永久链接至目标")
:   Closes the interface. This function should be called after [bk_bluetooth_init()](dual_ble.md#group__dm__bluetooth_1ga577c57a04b4b4589adfb5736442015a2 "dual_ble.md#group__dm__bluetooth_1ga577c57a04b4b4589adfb5736442015a2") success, and should be called after bk_bt_hid_host_init(). When the operation is complete the callback function will be called with BK_HIDH_DEINIT_EVT.

    返回
    :   - BK_OK: success


        - other: failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_hid_host_connect([bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr)[](#_CPPv422bk_bt_hid_host_connect12bk_bd_addr_t "永久链接至目标")
:   Connect to HID device. When the operation is complete the callback function will be called with BK_HIDH_OPEN_EVT.

    参数
    :   **bd_addr** – **[in]** Remote device bluetooth device address.

    返回
    :   - BK_OK: success


        - other: failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_hid_host_disconnect([bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr)[](#_CPPv425bk_bt_hid_host_disconnect12bk_bd_addr_t "永久链接至目标")
:   Disconnect from HID device. When the operation is complete the callback function will be called with BK_HIDH_CLOSE_EVT.

    参数
    :   **bd_addr** – **[in]** Remote device bluetooth device address.

    返回
    :   - BK_OK: success


        - other: failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_hid_host_virtual_cable_unplug([bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr)[](#_CPPv435bk_bt_hid_host_virtual_cable_unplug12bk_bd_addr_t "永久链接至目标")
:   Virtual UnPlug (VUP) the specified HID device. When the operation is complete the callback function will be called with BK_HIDH_VC_UNPLUG_EVT.

    参数
    :   **bd_addr** – **[in]** Remote device bluetooth device address.

    返回
    :   - BK_OK: success


        - other: failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_hid_host_set_info([bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr, [bk_hidh_hid_info_t](#_CPPv418bk_hidh_hid_info_t "bk_hidh_hid_info_t") *hid_info)[](#_CPPv423bk_bt_hid_host_set_info12bk_bd_addr_tP18bk_hidh_hid_info_t "永久链接至目标")
:   Set the HID device descriptor for the specified HID device. When the operation is complete the callback function will be called with BK_HIDH_SET_INFO_EVT.

    参数
    :   - **bd_addr** – **[in]** Remote device bluetooth device address.

        - **hid_info** – **[in]** HID device descriptor structure.

    返回
    :   - BK_OK: success


        - other: failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_hid_host_get_protocol([bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr)[](#_CPPv427bk_bt_hid_host_get_protocol12bk_bd_addr_t "永久链接至目标")
:   Get the HID proto mode. When the operation is complete the callback function will be called with BK_HIDH_GET_PROTO_EVT.

    参数
    :   **bd_addr** – **[in]** Remote device bluetooth device address.

    返回
    :   - BK_OK: success

        - other: failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_hid_host_set_protocol([bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr, [bk_hidh_protocol_mode_t](#_CPPv423bk_hidh_protocol_mode_t "bk_hidh_protocol_mode_t") protocol_mode)[](#_CPPv427bk_bt_hid_host_set_protocol12bk_bd_addr_t23bk_hidh_protocol_mode_t "永久链接至目标")
:   Set the HID proto mode. When the operation is complete the callback function will be called with BK_HIDH_SET_PROTO_EVT.

    参数
    :   - **bd_addr** – **[in]** Remote device bluetooth device address.

        - **protocol_mode** – **[in]** Protocol mode type.

    返回
    :   - BK_OK: success

        - other: failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_hid_host_get_report([bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr, [bk_hidh_report_type_t](#_CPPv421bk_hidh_report_type_t "bk_hidh_report_type_t") report_type, uint8_t report_id, int buffer_size)[](#_CPPv425bk_bt_hid_host_get_report12bk_bd_addr_t21bk_hidh_report_type_t7uint8_ti "永久链接至目标")
:   Send a GET_REPORT to HID device. When the operation is complete the callback function will be called with BK_HIDH_GET_RPT_EVT.

    参数
    :   - **bd_addr** – **[in]** Remote device bluetooth device address.

        - **report_type** – **[in]** Report type

        - **report_id** – **[in]** Report id

        - **buffer_size** – **[in]** Buffer size

    返回
    :   - BK_OK: success


        - other: failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_hid_host_set_report([bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr, [bk_hidh_report_type_t](#_CPPv421bk_hidh_report_type_t "bk_hidh_report_type_t") report_type, uint8_t *report, size_t len)[](#_CPPv425bk_bt_hid_host_set_report12bk_bd_addr_t21bk_hidh_report_type_tP7uint8_t6size_t "永久链接至目标")
:   Send a SET_REPORT to HID device. When the operation is complete the callback function will be called with BK_HIDH_SET_RPT_EVT.

    参数
    :   - **bd_addr** – **[in]** Remote device bluetooth device address.

        - **report_type** – **[in]** Report type

        - **report** – **[in]** Report data pointer

        - **len** – **[in]** Report data length

    返回
    :   - BK_OK: success


        - other: failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_hid_host_send_data([bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr, uint8_t *data, size_t len)[](#_CPPv424bk_bt_hid_host_send_data12bk_bd_addr_tP7uint8_t6size_t "永久链接至目标")
:   Send data to HID device. When the operation is complete the callback function will be called with BK_HIDH_DATA_EVT.

    参数
    :   - **bd_addr** – **[in]** Remote device bluetooth device address.

        - **data** – **[in]** Data pointer

        - **len** – **[in]** Data length

    返回
    :   - BK_OK: success


        - other: failed

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_hid_host_sdp_dscp([bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr)[](#_CPPv423bk_bt_hid_host_sdp_dscp12bk_bd_addr_t "永久链接至目标")
:   Start SDP. When the operation is complete the callback function will be called with BK_HIDH_SDP_DSCP_EVT.

    参数
    :   **bd_addr** – **[in]** Remote device bluetooth device address.

    返回
    :   - BK_OK: success


        - other: failed


### Unions[](#id11 "永久链接至标题")

union bk_hidh_cb_param_t[](#_CPPv418bk_hidh_cb_param_t "永久链接至目标")
:   *#include <bk_dm_hidh.h>*

    HID host callback parameters union.

    Public Members

    struct [bk_hidh_cb_param_t](#_CPPv418bk_hidh_cb_param_t "bk_hidh_cb_param_t")::[hidh_init_evt_param](#_CPPv4N18bk_hidh_cb_param_t19hidh_init_evt_paramE "bk_hidh_cb_param_t::hidh_init_evt_param") init[](#_CPPv4N18bk_hidh_cb_param_t4initE "永久链接至目标")
    :   HIDH callback param of BK_HIDH_INIT_EVT

    struct [bk_hidh_cb_param_t](#_CPPv418bk_hidh_cb_param_t "bk_hidh_cb_param_t")::[hidh_uninit_evt_param](#_CPPv4N18bk_hidh_cb_param_t21hidh_uninit_evt_paramE "bk_hidh_cb_param_t::hidh_uninit_evt_param") deinit[](#_CPPv4N18bk_hidh_cb_param_t6deinitE "永久链接至目标")
    :   HIDH callback param of BK_HIDH_DEINIT_EVT

    struct [bk_hidh_cb_param_t](#_CPPv418bk_hidh_cb_param_t "bk_hidh_cb_param_t")::[hidh_open_evt_param](#_CPPv4N18bk_hidh_cb_param_t19hidh_open_evt_paramE "bk_hidh_cb_param_t::hidh_open_evt_param") open[](#_CPPv4N18bk_hidh_cb_param_t4openE "永久链接至目标")
    :   HIDH callback param of BK_HIDH_OPEN_EVT

    struct [bk_hidh_cb_param_t](#_CPPv418bk_hidh_cb_param_t "bk_hidh_cb_param_t")::[hidh_close_evt_param](#_CPPv4N18bk_hidh_cb_param_t20hidh_close_evt_paramE "bk_hidh_cb_param_t::hidh_close_evt_param") close[](#_CPPv4N18bk_hidh_cb_param_t5closeE "永久链接至目标")
    :   HIDH callback param of BK_HIDH_CLOSE_EVT

    struct [bk_hidh_cb_param_t](#_CPPv418bk_hidh_cb_param_t "bk_hidh_cb_param_t")::[hidh_unplug_evt_param](#_CPPv4N18bk_hidh_cb_param_t21hidh_unplug_evt_paramE "bk_hidh_cb_param_t::hidh_unplug_evt_param") unplug[](#_CPPv4N18bk_hidh_cb_param_t6unplugE "永久链接至目标")
    :   HIDH callback param of BK_HIDH_VC_UNPLUG_EVT

    struct [bk_hidh_cb_param_t](#_CPPv418bk_hidh_cb_param_t "bk_hidh_cb_param_t")::[hidh_get_proto_evt_param](#_CPPv4N18bk_hidh_cb_param_t24hidh_get_proto_evt_paramE "bk_hidh_cb_param_t::hidh_get_proto_evt_param") get_proto[](#_CPPv4N18bk_hidh_cb_param_t9get_protoE "永久链接至目标")
    :   HIDH callback param of BK_HIDH_GET_PROTO_EVT

    struct [bk_hidh_cb_param_t](#_CPPv418bk_hidh_cb_param_t "bk_hidh_cb_param_t")::[hidh_set_proto_evt_param](#_CPPv4N18bk_hidh_cb_param_t24hidh_set_proto_evt_paramE "bk_hidh_cb_param_t::hidh_set_proto_evt_param") set_proto[](#_CPPv4N18bk_hidh_cb_param_t9set_protoE "永久链接至目标")
    :   HIDH callback param of BK_HIDH_SET_PROTO_EVT

    struct [bk_hidh_cb_param_t](#_CPPv418bk_hidh_cb_param_t "bk_hidh_cb_param_t")::[hidh_get_rpt_evt_param](#_CPPv4N18bk_hidh_cb_param_t22hidh_get_rpt_evt_paramE "bk_hidh_cb_param_t::hidh_get_rpt_evt_param") get_rpt[](#_CPPv4N18bk_hidh_cb_param_t7get_rptE "永久链接至目标")
    :   HIDH callback param of BK_HIDH_GET_RPT_EVT

    struct [bk_hidh_cb_param_t](#_CPPv418bk_hidh_cb_param_t "bk_hidh_cb_param_t")::[hidh_set_rpt_evt_param](#_CPPv4N18bk_hidh_cb_param_t22hidh_set_rpt_evt_paramE "bk_hidh_cb_param_t::hidh_set_rpt_evt_param") set_rpt[](#_CPPv4N18bk_hidh_cb_param_t7set_rptE "永久链接至目标")
    :   HIDH callback param of BK_HIDH_SET_RPT_EVT

    struct [bk_hidh_cb_param_t](#_CPPv418bk_hidh_cb_param_t "bk_hidh_cb_param_t")::[hidh_send_data_evt_param](#_CPPv4N18bk_hidh_cb_param_t24hidh_send_data_evt_paramE "bk_hidh_cb_param_t::hidh_send_data_evt_param") send_data[](#_CPPv4N18bk_hidh_cb_param_t9send_dataE "永久链接至目标")
    :   HIDH callback param of BK_HIDH_DATA_EVT

    struct [bk_hidh_cb_param_t](#_CPPv418bk_hidh_cb_param_t "bk_hidh_cb_param_t")::[hidh_data_ind_evt_param](#_CPPv4N18bk_hidh_cb_param_t23hidh_data_ind_evt_paramE "bk_hidh_cb_param_t::hidh_data_ind_evt_param") data_ind[](#_CPPv4N18bk_hidh_cb_param_t8data_indE "永久链接至目标")
    :   HIDH callback param of BK_HIDH_DATA_IND_EVT

    struct [bk_hidh_cb_param_t](#_CPPv418bk_hidh_cb_param_t "bk_hidh_cb_param_t")::[hidh_add_dev_evt_param](#_CPPv4N18bk_hidh_cb_param_t22hidh_add_dev_evt_paramE "bk_hidh_cb_param_t::hidh_add_dev_evt_param") add_dev[](#_CPPv4N18bk_hidh_cb_param_t7add_devE "永久链接至目标")
    :   HIDH callback param of BK_HIDH_ADD_DEV_EVT

    struct [bk_hidh_cb_param_t](#_CPPv418bk_hidh_cb_param_t "bk_hidh_cb_param_t")::[hidh_rmv_dev_evt_param](#_CPPv4N18bk_hidh_cb_param_t22hidh_rmv_dev_evt_paramE "bk_hidh_cb_param_t::hidh_rmv_dev_evt_param") rmv_dev[](#_CPPv4N18bk_hidh_cb_param_t7rmv_devE "永久链接至目标")
    :   HIDH callback param of BK_HIDH_RMV_DEV_EVT

    struct [bk_hidh_cb_param_t](#_CPPv418bk_hidh_cb_param_t "bk_hidh_cb_param_t")::[hidh_get_dscp_evt_param](#_CPPv4N18bk_hidh_cb_param_t23hidh_get_dscp_evt_paramE "bk_hidh_cb_param_t::hidh_get_dscp_evt_param") sdp_dscp[](#_CPPv4N18bk_hidh_cb_param_t8sdp_dscpE "永久链接至目标")
    :   HIDH callback param of BK_HIDH_GET_DSCP_EVT

    struct [bk_hidh_cb_param_t](#_CPPv418bk_hidh_cb_param_t "bk_hidh_cb_param_t")::[hidh_set_info_evt_param](#_CPPv4N18bk_hidh_cb_param_t23hidh_set_info_evt_paramE "bk_hidh_cb_param_t::hidh_set_info_evt_param") set_info[](#_CPPv4N18bk_hidh_cb_param_t8set_infoE "永久链接至目标")
    :   HIDH callback param of BK_HIDH_SET_INFO_EVT

    struct hidh_add_dev_evt_param[](#_CPPv4N18bk_hidh_cb_param_t22hidh_add_dev_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidh.h>*

        BK_HIDH_ADD_DEV_EVT.

        Public Members

        [bk_hidh_status_t](#_CPPv416bk_hidh_status_t "bk_hidh_status_t") status[](#_CPPv4N18bk_hidh_cb_param_t22hidh_add_dev_evt_param6statusE "永久链接至目标")
        :   operation status

        uint8_t handle[](#_CPPv4N18bk_hidh_cb_param_t22hidh_add_dev_evt_param6handleE "永久链接至目标")
        :   device handle

        [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr[](#_CPPv4N18bk_hidh_cb_param_t22hidh_add_dev_evt_param7bd_addrE "永久链接至目标")
        :   device address

    struct hidh_close_evt_param[](#_CPPv4N18bk_hidh_cb_param_t20hidh_close_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidh.h>*

        BK_HIDH_CLOSE_EVT.

        Public Members

        [bk_hidh_status_t](#_CPPv416bk_hidh_status_t "bk_hidh_status_t") status[](#_CPPv4N18bk_hidh_cb_param_t20hidh_close_evt_param6statusE "永久链接至目标")
        :   operation status

        [bk_hidh_connection_state_t](#_CPPv426bk_hidh_connection_state_t "bk_hidh_connection_state_t") conn_status[](#_CPPv4N18bk_hidh_cb_param_t20hidh_close_evt_param11conn_statusE "永久链接至目标")
        :   connection status

        uint8_t handle[](#_CPPv4N18bk_hidh_cb_param_t20hidh_close_evt_param6handleE "永久链接至目标")
        :   device handle

    struct hidh_data_ind_evt_param[](#_CPPv4N18bk_hidh_cb_param_t23hidh_data_ind_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidh.h>*

        BK_HIDH_DATA_IND_EVT.

        Public Members

        [bk_hidh_status_t](#_CPPv416bk_hidh_status_t "bk_hidh_status_t") status[](#_CPPv4N18bk_hidh_cb_param_t23hidh_data_ind_evt_param6statusE "永久链接至目标")
        :   operation status

        uint8_t handle[](#_CPPv4N18bk_hidh_cb_param_t23hidh_data_ind_evt_param6handleE "永久链接至目标")
        :   device handle

        [bk_hidh_protocol_mode_t](#_CPPv423bk_hidh_protocol_mode_t "bk_hidh_protocol_mode_t") proto_mode[](#_CPPv4N18bk_hidh_cb_param_t23hidh_data_ind_evt_param10proto_modeE "永久链接至目标")
        :   protocol mode

        uint16_t len[](#_CPPv4N18bk_hidh_cb_param_t23hidh_data_ind_evt_param3lenE "永久链接至目标")
        :   data length

        uint8_t *data[](#_CPPv4N18bk_hidh_cb_param_t23hidh_data_ind_evt_param4dataE "永久链接至目标")
        :   data pointer

        uint8_t report_type[](#_CPPv4N18bk_hidh_cb_param_t23hidh_data_ind_evt_param11report_typeE "永久链接至目标")
        :   report type

    struct hidh_get_dscp_evt_param[](#_CPPv4N18bk_hidh_cb_param_t23hidh_get_dscp_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidh.h>*

        BK_HIDH_SDP_DSCP_EVT.

        Public Members

        [bk_hidh_status_t](#_CPPv416bk_hidh_status_t "bk_hidh_status_t") status[](#_CPPv4N18bk_hidh_cb_param_t23hidh_get_dscp_evt_param6statusE "永久链接至目标")
        :   operation status

        uint8_t sub_class[](#_CPPv4N18bk_hidh_cb_param_t23hidh_get_dscp_evt_param9sub_classE "永久链接至目标")
        :   HIDDeviceSubclass

        uint8_t reconn_init[](#_CPPv4N18bk_hidh_cb_param_t23hidh_get_dscp_evt_param11reconn_initE "永久链接至目标")
        :   HIDReconnectInitiate

        uint8_t normal_conn[](#_CPPv4N18bk_hidh_cb_param_t23hidh_get_dscp_evt_param11normal_connE "永久链接至目标")
        :   HIDNormallyConnectable

        uint16_t ssr_max_latency[](#_CPPv4N18bk_hidh_cb_param_t23hidh_get_dscp_evt_param15ssr_max_latencyE "永久链接至目标")
        :   SSR max latency in slots

        uint16_t ssr_min_tout[](#_CPPv4N18bk_hidh_cb_param_t23hidh_get_dscp_evt_param12ssr_min_toutE "永久链接至目标")
        :   SSR min timeout in slots

        uint8_t ctry_code[](#_CPPv4N18bk_hidh_cb_param_t23hidh_get_dscp_evt_param9ctry_codeE "永久链接至目标")
        :   Country Code

        uint16_t parse_version[](#_CPPv4N18bk_hidh_cb_param_t23hidh_get_dscp_evt_param13parse_versionE "永久链接至目标")
        :   Parse Version

        uint8_t virtual_cable[](#_CPPv4N18bk_hidh_cb_param_t23hidh_get_dscp_evt_param13virtual_cableE "永久链接至目标")
        :   Virtual Cable

        uint8_t boot_device[](#_CPPv4N18bk_hidh_cb_param_t23hidh_get_dscp_evt_param11boot_deviceE "永久链接至目标")
        :   Boot device

        uint8_t remote_wake[](#_CPPv4N18bk_hidh_cb_param_t23hidh_get_dscp_evt_param11remote_wakeE "永久链接至目标")
        :   HIDRemoteWake

        uint8_t battery_power[](#_CPPv4N18bk_hidh_cb_param_t23hidh_get_dscp_evt_param13battery_powerE "永久链接至目标")
        :   HIDBatteryPower

        uint16_t vendor_id[](#_CPPv4N18bk_hidh_cb_param_t23hidh_get_dscp_evt_param9vendor_idE "永久链接至目标")
        :   Device Vendor ID

        uint16_t product_id[](#_CPPv4N18bk_hidh_cb_param_t23hidh_get_dscp_evt_param10product_idE "永久链接至目标")
        :   Device Product ID

        uint16_t device_version[](#_CPPv4N18bk_hidh_cb_param_t23hidh_get_dscp_evt_param14device_versionE "永久链接至目标")
        :   Device Version

        uint16_t dl_len[](#_CPPv4N18bk_hidh_cb_param_t23hidh_get_dscp_evt_param6dl_lenE "永久链接至目标")
        :   Device descriptor length

        uint8_t *dsc_list[](#_CPPv4N18bk_hidh_cb_param_t23hidh_get_dscp_evt_param8dsc_listE "永久链接至目标")
        :   Device descriptor pointer

        uint8_t dsc_type[](#_CPPv4N18bk_hidh_cb_param_t23hidh_get_dscp_evt_param8dsc_typeE "永久链接至目标")
        :   Device ClassDescriptor type

    struct hidh_get_proto_evt_param[](#_CPPv4N18bk_hidh_cb_param_t24hidh_get_proto_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidh.h>*

        BK_HIDH_GET_PROTO_EVT.

        Public Members

        [bk_hidh_status_t](#_CPPv416bk_hidh_status_t "bk_hidh_status_t") status[](#_CPPv4N18bk_hidh_cb_param_t24hidh_get_proto_evt_param6statusE "永久链接至目标")
        :   operation status

        uint8_t handle[](#_CPPv4N18bk_hidh_cb_param_t24hidh_get_proto_evt_param6handleE "永久链接至目标")
        :   device handle

        [bk_hidh_protocol_mode_t](#_CPPv423bk_hidh_protocol_mode_t "bk_hidh_protocol_mode_t") proto_mode[](#_CPPv4N18bk_hidh_cb_param_t24hidh_get_proto_evt_param10proto_modeE "永久链接至目标")
        :   protocol mode

    struct hidh_get_rpt_evt_param[](#_CPPv4N18bk_hidh_cb_param_t22hidh_get_rpt_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidh.h>*

        BK_HIDH_GET_RPT_EVT.

        Public Members

        [bk_hidh_status_t](#_CPPv416bk_hidh_status_t "bk_hidh_status_t") status[](#_CPPv4N18bk_hidh_cb_param_t22hidh_get_rpt_evt_param6statusE "永久链接至目标")
        :   operation status

        uint8_t handle[](#_CPPv4N18bk_hidh_cb_param_t22hidh_get_rpt_evt_param6handleE "永久链接至目标")
        :   device handle

        uint16_t len[](#_CPPv4N18bk_hidh_cb_param_t22hidh_get_rpt_evt_param3lenE "永久链接至目标")
        :   data length

        uint8_t *data[](#_CPPv4N18bk_hidh_cb_param_t22hidh_get_rpt_evt_param4dataE "永久链接至目标")
        :   data pointer

    struct hidh_init_evt_param[](#_CPPv4N18bk_hidh_cb_param_t19hidh_init_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidh.h>*

        BK_HIDH_INIT_EVT.

        Public Members

        [bk_hidh_status_t](#_CPPv416bk_hidh_status_t "bk_hidh_status_t") status[](#_CPPv4N18bk_hidh_cb_param_t19hidh_init_evt_param6statusE "永久链接至目标")
        :   status

    struct hidh_open_evt_param[](#_CPPv4N18bk_hidh_cb_param_t19hidh_open_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidh.h>*

        BK_HIDH_OPEN_EVT.

        Public Members

        [bk_hidh_status_t](#_CPPv416bk_hidh_status_t "bk_hidh_status_t") status[](#_CPPv4N18bk_hidh_cb_param_t19hidh_open_evt_param6statusE "永久链接至目标")
        :   operation status

        [bk_hidh_connection_state_t](#_CPPv426bk_hidh_connection_state_t "bk_hidh_connection_state_t") conn_status[](#_CPPv4N18bk_hidh_cb_param_t19hidh_open_evt_param11conn_statusE "永久链接至目标")
        :   connection status

        bool is_orig[](#_CPPv4N18bk_hidh_cb_param_t19hidh_open_evt_param7is_origE "永久链接至目标")
        :   indicate if host intiate the connection

        uint8_t handle[](#_CPPv4N18bk_hidh_cb_param_t19hidh_open_evt_param6handleE "永久链接至目标")
        :   device handle

        [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr[](#_CPPv4N18bk_hidh_cb_param_t19hidh_open_evt_param7bd_addrE "永久链接至目标")
        :   device address

    struct hidh_rmv_dev_evt_param[](#_CPPv4N18bk_hidh_cb_param_t22hidh_rmv_dev_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidh.h>*

        BK_HIDH_RMV_DEV_EVT.

        Public Members

        [bk_hidh_status_t](#_CPPv416bk_hidh_status_t "bk_hidh_status_t") status[](#_CPPv4N18bk_hidh_cb_param_t22hidh_rmv_dev_evt_param6statusE "永久链接至目标")
        :   operation status

        uint8_t handle[](#_CPPv4N18bk_hidh_cb_param_t22hidh_rmv_dev_evt_param6handleE "永久链接至目标")
        :   device handle

        [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr[](#_CPPv4N18bk_hidh_cb_param_t22hidh_rmv_dev_evt_param7bd_addrE "永久链接至目标")
        :   device address

    struct hidh_send_data_evt_param[](#_CPPv4N18bk_hidh_cb_param_t24hidh_send_data_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidh.h>*

        BK_HIDH_DATA_EVT.

        Public Members

        [bk_hidh_status_t](#_CPPv416bk_hidh_status_t "bk_hidh_status_t") status[](#_CPPv4N18bk_hidh_cb_param_t24hidh_send_data_evt_param6statusE "永久链接至目标")
        :   operation status

        uint8_t handle[](#_CPPv4N18bk_hidh_cb_param_t24hidh_send_data_evt_param6handleE "永久链接至目标")
        :   device handle

        uint8_t reason[](#_CPPv4N18bk_hidh_cb_param_t24hidh_send_data_evt_param6reasonE "永久链接至目标")
        :   lower layer failed reason

    struct hidh_set_info_evt_param[](#_CPPv4N18bk_hidh_cb_param_t23hidh_set_info_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidh.h>*

        BK_HIDH_SET_INFO_EVT.

        Public Members

        [bk_hidh_status_t](#_CPPv416bk_hidh_status_t "bk_hidh_status_t") status[](#_CPPv4N18bk_hidh_cb_param_t23hidh_set_info_evt_param6statusE "永久链接至目标")
        :   operation status

        uint8_t handle[](#_CPPv4N18bk_hidh_cb_param_t23hidh_set_info_evt_param6handleE "永久链接至目标")
        :   device handle

        [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr[](#_CPPv4N18bk_hidh_cb_param_t23hidh_set_info_evt_param7bd_addrE "永久链接至目标")
        :   device address

    struct hidh_set_proto_evt_param[](#_CPPv4N18bk_hidh_cb_param_t24hidh_set_proto_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidh.h>*

        BK_HIDH_SET_PROTO_EVT.

        Public Members

        [bk_hidh_status_t](#_CPPv416bk_hidh_status_t "bk_hidh_status_t") status[](#_CPPv4N18bk_hidh_cb_param_t24hidh_set_proto_evt_param6statusE "永久链接至目标")
        :   operation status

        uint8_t handle[](#_CPPv4N18bk_hidh_cb_param_t24hidh_set_proto_evt_param6handleE "永久链接至目标")
        :   device handle

    struct hidh_set_rpt_evt_param[](#_CPPv4N18bk_hidh_cb_param_t22hidh_set_rpt_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidh.h>*

        BK_HIDH_SET_RPT_EVT.

        Public Members

        [bk_hidh_status_t](#_CPPv416bk_hidh_status_t "bk_hidh_status_t") status[](#_CPPv4N18bk_hidh_cb_param_t22hidh_set_rpt_evt_param6statusE "永久链接至目标")
        :   operation status

        uint8_t handle[](#_CPPv4N18bk_hidh_cb_param_t22hidh_set_rpt_evt_param6handleE "永久链接至目标")
        :   device handle

    struct hidh_uninit_evt_param[](#_CPPv4N18bk_hidh_cb_param_t21hidh_uninit_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidh.h>*

        BK_HIDH_DEINIT_EVT.

        Public Members

        [bk_hidh_status_t](#_CPPv416bk_hidh_status_t "bk_hidh_status_t") status[](#_CPPv4N18bk_hidh_cb_param_t21hidh_uninit_evt_param6statusE "永久链接至目标")
        :   status

    struct hidh_unplug_evt_param[](#_CPPv4N18bk_hidh_cb_param_t21hidh_unplug_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_hidh.h>*

        BK_HIDH_VC_UNPLUG_EVT.

        Public Members

        [bk_hidh_status_t](#_CPPv416bk_hidh_status_t "bk_hidh_status_t") status[](#_CPPv4N18bk_hidh_cb_param_t21hidh_unplug_evt_param6statusE "永久链接至目标")
        :   operation status

        [bk_hidh_connection_state_t](#_CPPv426bk_hidh_connection_state_t "bk_hidh_connection_state_t") conn_status[](#_CPPv4N18bk_hidh_cb_param_t21hidh_unplug_evt_param11conn_statusE "永久链接至目标")
        :   connection status

        uint8_t handle[](#_CPPv4N18bk_hidh_cb_param_t21hidh_unplug_evt_param6handleE "永久链接至目标")
        :   device handle


### Structures[](#id12 "永久链接至标题")

struct bk_hidh_hid_info_t[](#_CPPv418bk_hidh_hid_info_t "永久链接至目标")
:   HID device information from HID Device Service Record and Device ID Service Record.

    Public Members

    int attr_mask[](#_CPPv4N18bk_hidh_hid_info_t9attr_maskE "永久链接至目标")
    :   device attribute bit mask, refer to bk_hidh_dev_attr_t

    int dl_len[](#_CPPv4N18bk_hidh_hid_info_t6dl_lenE "永久链接至目标")
    :   SDP attrbutes of HID devices: HID device descriptor length

    uint8_t *dsc_list[](#_CPPv4N18bk_hidh_hid_info_t8dsc_listE "永久链接至目标")
    :   SDP attrbutes of HID devices: HID device descriptor definition


### Macros[](#id13 "永久链接至标题")

BTHH_MAX_DSC_LEN[](#c.BTHH_MAX_DSC_LEN "永久链接至目标")
:   maximum size of HID Device report descriptor


### Type Definitions[](#id14 "永久链接至标题")

typedef void (*bk_hh_cb_t)([bk_hidh_cb_event_t](#_CPPv418bk_hidh_cb_event_t "bk_hidh_cb_event_t") event, [bk_hidh_cb_param_t](#_CPPv418bk_hidh_cb_param_t "bk_hidh_cb_param_t") *param)[](#_CPPv410bk_hh_cb_t "永久链接至目标")
:   HID host callback function type.

    Param event
    :   Event type

    Param param
    :   Point to callback parameter, currently is union type


### Enumerations[](#id15 "永久链接至标题")

enum bk_hidh_connection_state_t[](#_CPPv426bk_hidh_connection_state_t "永久链接至目标")
:   HID host connection state.


    *Values:*

    enumerator BK_HIDH_CONN_STATE_CONNECTED[](#_CPPv4N26bk_hidh_connection_state_t28BK_HIDH_CONN_STATE_CONNECTEDE "永久链接至目标")
    :   connected state

    enumerator BK_HIDH_CONN_STATE_CONNECTING[](#_CPPv4N26bk_hidh_connection_state_t29BK_HIDH_CONN_STATE_CONNECTINGE "永久链接至目标")
    :   connecting state

    enumerator BK_HIDH_CONN_STATE_DISCONNECTED[](#_CPPv4N26bk_hidh_connection_state_t31BK_HIDH_CONN_STATE_DISCONNECTEDE "永久链接至目标")
    :   disconnected state

    enumerator BK_HIDH_CONN_STATE_DISCONNECTING[](#_CPPv4N26bk_hidh_connection_state_t32BK_HIDH_CONN_STATE_DISCONNECTINGE "永久链接至目标")
    :   disconnecting state

    enumerator BK_HIDH_CONN_STATE_UNKNOWN[](#_CPPv4N26bk_hidh_connection_state_t26BK_HIDH_CONN_STATE_UNKNOWNE "永久链接至目标")
    :   unknown state (initial state)

enum bk_hidh_status_t[](#_CPPv416bk_hidh_status_t "永久链接至目标")
:   HID handshake error code and vendor-defined result code.


    *Values:*

    enumerator BK_HIDH_OK[](#_CPPv4N16bk_hidh_status_t10BK_HIDH_OKE "永久链接至目标")
    :   successful

    enumerator BK_HIDH_HS_HID_NOT_READY[](#_CPPv4N16bk_hidh_status_t24BK_HIDH_HS_HID_NOT_READYE "永久链接至目标")
    :   handshake error: device not ready

    enumerator BK_HIDH_HS_INVALID_RPT_ID[](#_CPPv4N16bk_hidh_status_t25BK_HIDH_HS_INVALID_RPT_IDE "永久链接至目标")
    :   handshake error: invalid report ID

    enumerator BK_HIDH_HS_TRANS_NOT_SPT[](#_CPPv4N16bk_hidh_status_t24BK_HIDH_HS_TRANS_NOT_SPTE "永久链接至目标")
    :   handshake error: HID device does not support the request

    enumerator BK_HIDH_HS_INVALID_PARAM[](#_CPPv4N16bk_hidh_status_t24BK_HIDH_HS_INVALID_PARAME "永久链接至目标")
    :   handshake error: parameter value does not meet the expected criteria of called function or API

    enumerator BK_HIDH_HS_ERROR[](#_CPPv4N16bk_hidh_status_t16BK_HIDH_HS_ERRORE "永久链接至目标")
    :   handshake error: HID device could not identify the error condition

    enumerator BK_HIDH_ERR[](#_CPPv4N16bk_hidh_status_t11BK_HIDH_ERRE "永久链接至目标")
    :   general BK HID Host error

    enumerator BK_HIDH_ERR_SDP[](#_CPPv4N16bk_hidh_status_t15BK_HIDH_ERR_SDPE "永久链接至目标")
    :   SDP error

    enumerator BK_HIDH_ERR_PROTO[](#_CPPv4N16bk_hidh_status_t17BK_HIDH_ERR_PROTOE "永久链接至目标")
    :   SET_PROTOCOL error, only used in BK_HIDH_OPEN_EVT callback

    enumerator BK_HIDH_ERR_DB_FULL[](#_CPPv4N16bk_hidh_status_t19BK_HIDH_ERR_DB_FULLE "永久链接至目标")
    :   device database full, used in BK_HIDH_OPEN_EVT/BK_HIDH_ADD_DEV_EVT

    enumerator BK_HIDH_ERR_TOD_UNSPT[](#_CPPv4N16bk_hidh_status_t21BK_HIDH_ERR_TOD_UNSPTE "永久链接至目标")
    :   type of device not supported

    enumerator BK_HIDH_ERR_NO_RES[](#_CPPv4N16bk_hidh_status_t18BK_HIDH_ERR_NO_RESE "永久链接至目标")
    :   out of system resources

    enumerator BK_HIDH_ERR_AUTH_FAILED[](#_CPPv4N16bk_hidh_status_t23BK_HIDH_ERR_AUTH_FAILEDE "永久链接至目标")
    :   authentication fail

    enumerator BK_HIDH_ERR_HDL[](#_CPPv4N16bk_hidh_status_t15BK_HIDH_ERR_HDLE "永久链接至目标")
    :   connection handle error

    enumerator BK_HIDH_ERR_SEC[](#_CPPv4N16bk_hidh_status_t15BK_HIDH_ERR_SECE "永久链接至目标")
    :   encryption error

    enumerator BK_HIDH_BUSY[](#_CPPv4N16bk_hidh_status_t12BK_HIDH_BUSYE "永久链接至目标")
    :   vendor-defined: temporarily can not handle this request

    enumerator BK_HIDH_NO_DATA[](#_CPPv4N16bk_hidh_status_t15BK_HIDH_NO_DATAE "永久链接至目标")
    :   vendor-defined: no data.

    enumerator BK_HIDH_NEED_INIT[](#_CPPv4N16bk_hidh_status_t17BK_HIDH_NEED_INITE "永久链接至目标")
    :   vendor-defined: HIDH module shall initialize first

    enumerator BK_HIDH_NEED_DEINIT[](#_CPPv4N16bk_hidh_status_t19BK_HIDH_NEED_DEINITE "永久链接至目标")
    :   vendor-defined: HIDH module shall de-deinitialize first

    enumerator BK_HIDH_NO_CONNECTION[](#_CPPv4N16bk_hidh_status_t21BK_HIDH_NO_CONNECTIONE "永久链接至目标")
    :   vendor-defined: connection may have been closed

    enumerator BK_HIDH_NO_ACL_LINK[](#_CPPv4N16bk_hidh_status_t19BK_HIDH_NO_ACL_LINKE "永久链接至目标")
    :   vendor-defined: Baseband acl link not exist

enum bk_hidh_protocol_mode_t[](#_CPPv423bk_hidh_protocol_mode_t "永久链接至目标")
:   HID host protocol modes.


    *Values:*

    enumerator BK_HIDH_BOOT_MODE[](#_CPPv4N23bk_hidh_protocol_mode_t17BK_HIDH_BOOT_MODEE "永久链接至目标")
    :   boot protocol mode

    enumerator BK_HIDH_REPORT_MODE[](#_CPPv4N23bk_hidh_protocol_mode_t19BK_HIDH_REPORT_MODEE "永久链接至目标")
    :   report protocol mode

    enumerator BK_HIDH_UNSUPPORTED_MODE[](#_CPPv4N23bk_hidh_protocol_mode_t24BK_HIDH_UNSUPPORTED_MODEE "永久链接至目标")
    :   unsupported protocol mode

enum bk_hidh_report_type_t[](#_CPPv421bk_hidh_report_type_t "永久链接至目标")
:   HID host report types.


    *Values:*

    enumerator BK_HIDH_REPORT_TYPE_OTHER[](#_CPPv4N21bk_hidh_report_type_t25BK_HIDH_REPORT_TYPE_OTHERE "永久链接至目标")
    :   unsupported report type

    enumerator BK_HIDH_REPORT_TYPE_INPUT[](#_CPPv4N21bk_hidh_report_type_t25BK_HIDH_REPORT_TYPE_INPUTE "永久链接至目标")
    :   input report type

    enumerator BK_HIDH_REPORT_TYPE_OUTPUT[](#_CPPv4N21bk_hidh_report_type_t26BK_HIDH_REPORT_TYPE_OUTPUTE "永久链接至目标")
    :   output report type

    enumerator BK_HIDH_REPORT_TYPE_FEATURE[](#_CPPv4N21bk_hidh_report_type_t27BK_HIDH_REPORT_TYPE_FEATUREE "永久链接至目标")
    :   feature report type

enum bk_hidh_cb_event_t[](#_CPPv418bk_hidh_cb_event_t "永久链接至目标")
:   HID host callback function events.


    *Values:*

    enumerator BK_HIDH_INIT_EVT[](#_CPPv4N18bk_hidh_cb_event_t16BK_HIDH_INIT_EVTE "永久链接至目标")
    :   when HID host is initialized, the event comes

    enumerator BK_HIDH_DEINIT_EVT[](#_CPPv4N18bk_hidh_cb_event_t18BK_HIDH_DEINIT_EVTE "永久链接至目标")
    :   when HID host is deinitialized, the event comes

    enumerator BK_HIDH_OPEN_EVT[](#_CPPv4N18bk_hidh_cb_event_t16BK_HIDH_OPEN_EVTE "永久链接至目标")
    :   when HID host connection opened, the event comes

    enumerator BK_HIDH_CLOSE_EVT[](#_CPPv4N18bk_hidh_cb_event_t17BK_HIDH_CLOSE_EVTE "永久链接至目标")
    :   when HID host connection closed, the event comes

    enumerator BK_HIDH_GET_RPT_EVT[](#_CPPv4N18bk_hidh_cb_event_t19BK_HIDH_GET_RPT_EVTE "永久链接至目标")
    :   when Get_Report command is called, the event comes

    enumerator BK_HIDH_SET_RPT_EVT[](#_CPPv4N18bk_hidh_cb_event_t19BK_HIDH_SET_RPT_EVTE "永久链接至目标")
    :   when Set_Report command is called, the event comes

    enumerator BK_HIDH_GET_PROTO_EVT[](#_CPPv4N18bk_hidh_cb_event_t21BK_HIDH_GET_PROTO_EVTE "永久链接至目标")
    :   when Get_Protocol command is called, the event comes

    enumerator BK_HIDH_SET_PROTO_EVT[](#_CPPv4N18bk_hidh_cb_event_t21BK_HIDH_SET_PROTO_EVTE "永久链接至目标")
    :   when Set_Protocol command is called, the event comes

    enumerator BK_HIDH_SDP_DSCP_EVT[](#_CPPv4N18bk_hidh_cb_event_t20BK_HIDH_SDP_DSCP_EVTE "永久链接至目标")
    :   when HIDH is connected, the event comes

    enumerator BK_HIDH_ADD_DEV_EVT[](#_CPPv4N18bk_hidh_cb_event_t19BK_HIDH_ADD_DEV_EVTE "永久链接至目标")
    :   when a device is added, the event comes

    enumerator BK_HIDH_RMV_DEV_EVT[](#_CPPv4N18bk_hidh_cb_event_t19BK_HIDH_RMV_DEV_EVTE "永久链接至目标")
    :   when a device is removed, the event comes

    enumerator BK_HIDH_VC_UNPLUG_EVT[](#_CPPv4N18bk_hidh_cb_event_t21BK_HIDH_VC_UNPLUG_EVTE "永久链接至目标")
    :   when virtually unplugged, the event comes

    enumerator BK_HIDH_DATA_EVT[](#_CPPv4N18bk_hidh_cb_event_t16BK_HIDH_DATA_EVTE "永久链接至目标")
    :   when send data on interrupt channel, the event comes

    enumerator BK_HIDH_DATA_IND_EVT[](#_CPPv4N18bk_hidh_cb_event_t20BK_HIDH_DATA_IND_EVTE "永久链接至目标")
    :   when receive data on interrupt channel, the event comes

    enumerator BK_HIDH_SET_INFO_EVT[](#_CPPv4N18bk_hidh_cb_event_t20BK_HIDH_SET_INFO_EVTE "永久链接至目标")
    :   when set the HID device descriptor, the event comes

enum bk_hidh_dev_attr_t[](#_CPPv418bk_hidh_dev_attr_t "永久链接至目标")
:   HID device information from HID Device Service Record and Device ID Service Record.


    *Values:*

    enumerator BK_HIDH_DEV_ATTR_VIRTUAL_CABLE[](#_CPPv4N18bk_hidh_dev_attr_t30BK_HIDH_DEV_ATTR_VIRTUAL_CABLEE "永久链接至目标")
    :   whether Virtual Cables is supported

    enumerator BK_HIDH_DEV_ATTR_RECONNECT_INITIATE[](#_CPPv4N18bk_hidh_dev_attr_t35BK_HIDH_DEV_ATTR_RECONNECT_INITIATEE "永久链接至目标")
    :   whether the HID device inititates the reconnection process

    enumerator BK_HIDH_DEV_ATTR_BATTERY_DEVICE[](#_CPPv4N18bk_hidh_dev_attr_t31BK_HIDH_DEV_ATTR_BATTERY_DEVICEE "永久链接至目标")
    :   whether Battery-powered device

    enumerator BK_HIDH_DEV_ATTR_REMOTE_WAKE[](#_CPPv4N18bk_hidh_dev_attr_t28BK_HIDH_DEV_ATTR_REMOTE_WAKEE "永久链接至目标")
    :   whether wake-up signal to host supported

    enumerator BK_HIDH_DEV_ATTR_NORMALLY_CONNECTABLE[](#_CPPv4N18bk_hidh_dev_attr_t37BK_HIDH_DEV_ATTR_NORMALLY_CONNECTABLEE "永久链接至目标")
    :   whether device is in Page Scan mode when there is no active connection

    enumerator BK_HIDH_DEV_ATTR_BOOT_DEVICE[](#_CPPv4N18bk_hidh_dev_attr_t28BK_HIDH_DEV_ATTR_BOOT_DEVICEE "永久链接至目标")
    :   whether Boot Protocol mode supported

enum bk_hidh_dev_app_id_t[](#_CPPv420bk_hidh_dev_app_id_t "永久链接至目标")
:   application ID(non-zero) for each type of device


    *Values:*

    enumerator BK_HIDH_APP_ID_MOUSE[](#_CPPv4N20bk_hidh_dev_app_id_t20BK_HIDH_APP_ID_MOUSEE "永久链接至目标")
    :   pointing device

    enumerator BK_HIDH_APP_ID_KEYBOARD[](#_CPPv4N20bk_hidh_dev_app_id_t23BK_HIDH_APP_ID_KEYBOARDE "永久链接至目标")
    :   keyboard

    enumerator BK_HIDH_APP_ID_REMOTE_CONTROL[](#_CPPv4N20bk_hidh_dev_app_id_t29BK_HIDH_APP_ID_REMOTE_CONTROLE "永久链接至目标")
    :   remote control

    enumerator BK_HIDH_APP_ID_JOYSTICK[](#_CPPv4N20bk_hidh_dev_app_id_t23BK_HIDH_APP_ID_JOYSTICKE "永久链接至目标")
    :   joystick

    enumerator BK_HIDH_APP_ID_GAMEPAD[](#_CPPv4N20bk_hidh_dev_app_id_t22BK_HIDH_APP_ID_GAMEPADE "永久链接至目标")
    :   gamepad


### Header File[](#id16 "永久链接至标题")


- [bluetooth/bk_dm_l2cap.h](https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_l2cap.h "https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_l2cap.h")


### Functions[](#id17 "永久链接至标题")

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_l2cap_register_callback([bk_bt_l2cap_cb_t](#_CPPv416bk_bt_l2cap_cb_t "bk_bt_l2cap_cb_t") callback)[](#_CPPv429bk_bt_l2cap_register_callback16bk_bt_l2cap_cb_t "永久链接至目标")
:   This function is called to init callbacks with L2CAP module.

    参数
    :   **callback** – **[in]** pointer to the init callback function.

    返回
    :   - BT_OK: success

        - other: failed

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_l2cap_init(void)[](#_CPPv416bk_bt_l2cap_initv "永久链接至目标")
:   This function is called to init L2CAP module. When the operation is completed, the callback function will be called with BK_BT_L2CAP_INIT_EVT. This function should be called after bk_bluedroid_enable() completes successfully.

    返回
    :   - BT_OK: success

        - other: failed

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_l2cap_deinit(void)[](#_CPPv418bk_bt_l2cap_deinitv "永久链接至目标")
:   This function is called to uninit l2cap module. The operation will close all active L2CAP connection first, then the callback function will be called with BK_BT_L2CAP_CLOSE_EVT, and the number of BK_BT_L2CAP_CLOSE_EVT is equal to the number of connection. When the operation is completed, the callback function will be called with BK_BT_L2CAP_UNINIT_EVT. This function should be called after bk_bt_l2cap_init() completes successfully.

    返回
    :   - BT_OK: success

        - other: failed

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_l2cap_connect([bk_bt_l2cap_cntl_flags_t](#_CPPv424bk_bt_l2cap_cntl_flags_t "bk_bt_l2cap_cntl_flags_t") cntl_flag, uint16_t remote_psm, [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") peer_bd_addr)[](#_CPPv419bk_bt_l2cap_connect24bk_bt_l2cap_cntl_flags_t8uint16_t12bk_bd_addr_t "永久链接至目标")
:   This function makes an L2CAP connection to a remote BD Address. When the connection is initiated or failed to initiate, the callback is called with BK_BT_L2CAP_CL_INIT_EVT. When the connection is established or failed, the callback is called with BK_BT_L2CAP_OPEN_EVT. This function must be called after bk_bt_l2cap_init() successful and before bk_bt_l2cap_deinit().

    参数
    :   - **cntl_flag** – **[in]** Lower 16-bit security settings mask.

        - **remote_psm** – **[in]** Remote device bluetooth Profile PSM.

        - **peer_bd_addr** – **[in]** Remote device bluetooth device address.

    返回
    :   - BT_OK: success

        - other: failed

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_l2cap_start_srv([bk_bt_l2cap_cntl_flags_t](#_CPPv424bk_bt_l2cap_cntl_flags_t "bk_bt_l2cap_cntl_flags_t") cntl_flag, uint16_t local_psm)[](#_CPPv421bk_bt_l2cap_start_srv24bk_bt_l2cap_cntl_flags_t8uint16_t "永久链接至目标")
:   This function create a L2CAP server and starts listening for an L2CAP connection request from a remote Bluetooth device. When the server is started successfully, the callback is called with BK_BT_L2CAP_START_EVT. When the connection is established, the callback is called with BK_BT_L2CAP_OPEN_EVT. This function must be called after bk_bt_l2cap_init() successful and before bk_bt_l2cap_deinit().

    参数
    :   - **cntl_flag** – **[in]** Lower 16-bit security settings mask.

        - **local_psm** – **[in]** Dynamic PSM.

    返回
    :   - BT_OK: success

        - other: failed

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_l2cap_stop_all_srv(void)[](#_CPPv424bk_bt_l2cap_stop_all_srvv "永久链接至目标")
:   This function stops all L2CAP servers. The operation will close all active L2CAP connection first, then the callback function will be called with BK_BT_L2CAP_CLOSE_EVT, and the number of BK_BT_L2CAP_CLOSE_EVT is equal to the number of connection. When the operation is completed, the callback is called with BK_BT_L2CAP_SRV_STOP_EVT. This function must be called after bk_bt_l2cap_init() successful and before bk_bt_l2cap_deinit().

    返回
    :   - BT_OK: success

        - other: failed

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_bt_l2cap_stop_srv(uint16_t local_psm)[](#_CPPv420bk_bt_l2cap_stop_srv8uint16_t "永久链接至目标")
:   This function stops a specific L2CAP server. The operation will close all active L2CAP connection first on the specific L2CAP server, then the callback function will be called with BK_BT_L2CAP_CLOSE_EVT, and the number of BK_BT_L2CAP_CLOSE_EVT is equal to the number of connection. When the operation is completed, the callback is called with BK_BT_L2CAP_SRV_STOP_EVT. This function must be called after bk_bt_l2cap_init() successful and before bk_bt_l2cap_deinit().

    参数
    :   **local_psm** – **[in]** Dynamic PSM.

    返回
    :   - BT_OK: success

        - other: failed

int bk_bt_l2cap_read(int fd, void *data, uint16_t size)[](#_CPPv416bk_bt_l2cap_readiPv8uint16_t "永久链接至目标")

int bk_bt_l2cap_write(int fd, const void *data, uint16_t size)[](#_CPPv417bk_bt_l2cap_writeiPKv8uint16_t "永久链接至目标")

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_l2cap_close(int fd)[](#_CPPv417bk_bt_l2cap_closei "永久链接至目标")

[bk_err_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk_bt_l2cap_set_data_callback([bk_bt_l2cap_data_cb_t](#_CPPv421bk_bt_l2cap_data_cb_t "bk_bt_l2cap_data_cb_t") callback)[](#_CPPv429bk_bt_l2cap_set_data_callback21bk_bt_l2cap_data_cb_t "永久链接至目标")


### Unions[](#id18 "永久链接至标题")

union bk_bt_l2cap_cb_param_t[](#_CPPv422bk_bt_l2cap_cb_param_t "永久链接至目标")
:   *#include <bk_dm_l2cap.h>*

    L2CAP callback parameters union.

    Public Members

    struct [bk_bt_l2cap_cb_param_t](#_CPPv422bk_bt_l2cap_cb_param_t "bk_bt_l2cap_cb_param_t")::[l2cap_init_evt_param](#_CPPv4N22bk_bt_l2cap_cb_param_t20l2cap_init_evt_paramE "bk_bt_l2cap_cb_param_t::l2cap_init_evt_param") init[](#_CPPv4N22bk_bt_l2cap_cb_param_t4initE "永久链接至目标")
    :   L2CAP callback param of BK_BT_L2CAP_INIT_EVT

    struct [bk_bt_l2cap_cb_param_t](#_CPPv422bk_bt_l2cap_cb_param_t "bk_bt_l2cap_cb_param_t")::[l2cap_uninit_evt_param](#_CPPv4N22bk_bt_l2cap_cb_param_t22l2cap_uninit_evt_paramE "bk_bt_l2cap_cb_param_t::l2cap_uninit_evt_param") uninit[](#_CPPv4N22bk_bt_l2cap_cb_param_t6uninitE "永久链接至目标")
    :   L2CAP callback param of BK_BT_L2CAP_UNINIT_EVT

    struct [bk_bt_l2cap_cb_param_t](#_CPPv422bk_bt_l2cap_cb_param_t "bk_bt_l2cap_cb_param_t")::[l2cap_open_evt_param](#_CPPv4N22bk_bt_l2cap_cb_param_t20l2cap_open_evt_paramE "bk_bt_l2cap_cb_param_t::l2cap_open_evt_param") open[](#_CPPv4N22bk_bt_l2cap_cb_param_t4openE "永久链接至目标")
    :   L2CAP callback param of BK_BT_L2CAP_OPEN_EVT

    struct [bk_bt_l2cap_cb_param_t](#_CPPv422bk_bt_l2cap_cb_param_t "bk_bt_l2cap_cb_param_t")::[l2cap_close_evt_param](#_CPPv4N22bk_bt_l2cap_cb_param_t21l2cap_close_evt_paramE "bk_bt_l2cap_cb_param_t::l2cap_close_evt_param") close[](#_CPPv4N22bk_bt_l2cap_cb_param_t5closeE "永久链接至目标")
    :   L2CAP callback param of BK_BT_L2CAP_CLOSE_EVT

    struct [bk_bt_l2cap_cb_param_t](#_CPPv422bk_bt_l2cap_cb_param_t "bk_bt_l2cap_cb_param_t")::[l2cap_start_evt_param](#_CPPv4N22bk_bt_l2cap_cb_param_t21l2cap_start_evt_paramE "bk_bt_l2cap_cb_param_t::l2cap_start_evt_param") start[](#_CPPv4N22bk_bt_l2cap_cb_param_t5startE "永久链接至目标")
    :   L2CAP callback param of BK_BT_L2CAP_START_EVT

    struct [bk_bt_l2cap_cb_param_t](#_CPPv422bk_bt_l2cap_cb_param_t "bk_bt_l2cap_cb_param_t")::[l2cap_cl_init_evt_param](#_CPPv4N22bk_bt_l2cap_cb_param_t23l2cap_cl_init_evt_paramE "bk_bt_l2cap_cb_param_t::l2cap_cl_init_evt_param") cl_init[](#_CPPv4N22bk_bt_l2cap_cb_param_t7cl_initE "永久链接至目标")
    :   L2CAP callback param of BK_BT_L2CAP_CL_INIT_EVT

    struct [bk_bt_l2cap_cb_param_t](#_CPPv422bk_bt_l2cap_cb_param_t "bk_bt_l2cap_cb_param_t")::[l2cap_srv_stop_evt_param](#_CPPv4N22bk_bt_l2cap_cb_param_t24l2cap_srv_stop_evt_paramE "bk_bt_l2cap_cb_param_t::l2cap_srv_stop_evt_param") srv_stop[](#_CPPv4N22bk_bt_l2cap_cb_param_t8srv_stopE "永久链接至目标")
    :   L2CAP callback param of BK_BT_L2CAP_SRV_STOP_EVT

    struct l2cap_cl_init_evt_param[](#_CPPv4N22bk_bt_l2cap_cb_param_t23l2cap_cl_init_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_l2cap.h>*

        BK_BT_L2CAP_CL_INIT_EVT.

        Public Members

        [bk_bt_l2cap_status_t](#_CPPv420bk_bt_l2cap_status_t "bk_bt_l2cap_status_t") status[](#_CPPv4N22bk_bt_l2cap_cb_param_t23l2cap_cl_init_evt_param6statusE "永久链接至目标")
        :   status

        uint32_t handle[](#_CPPv4N22bk_bt_l2cap_cb_param_t23l2cap_cl_init_evt_param6handleE "永久链接至目标")
        :   The connection handle

        uint8_t sec_id[](#_CPPv4N22bk_bt_l2cap_cb_param_t23l2cap_cl_init_evt_param6sec_idE "永久链接至目标")
        :   security ID used by this server

    struct l2cap_close_evt_param[](#_CPPv4N22bk_bt_l2cap_cb_param_t21l2cap_close_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_l2cap.h>*

        BK_BT_L2CAP_CLOSE_EVT.

        Public Members

        [bk_bt_l2cap_status_t](#_CPPv420bk_bt_l2cap_status_t "bk_bt_l2cap_status_t") status[](#_CPPv4N22bk_bt_l2cap_cb_param_t21l2cap_close_evt_param6statusE "永久链接至目标")
        :   status

        uint32_t handle[](#_CPPv4N22bk_bt_l2cap_cb_param_t21l2cap_close_evt_param6handleE "永久链接至目标")
        :   The connection handle

        bool async[](#_CPPv4N22bk_bt_l2cap_cb_param_t21l2cap_close_evt_param5asyncE "永久链接至目标")
        :   FALSE, if local initiates disconnect

        int fd[](#_CPPv4N22bk_bt_l2cap_cb_param_t21l2cap_close_evt_param2fdE "永久链接至目标")
        :   File descriptor, lcid

    struct l2cap_init_evt_param[](#_CPPv4N22bk_bt_l2cap_cb_param_t20l2cap_init_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_l2cap.h>*

        BK_BT_L2CAP_INIT_EVT.

        Public Members

        [bk_bt_l2cap_status_t](#_CPPv420bk_bt_l2cap_status_t "bk_bt_l2cap_status_t") status[](#_CPPv4N22bk_bt_l2cap_cb_param_t20l2cap_init_evt_param6statusE "永久链接至目标")
        :   status

    struct l2cap_open_evt_param[](#_CPPv4N22bk_bt_l2cap_cb_param_t20l2cap_open_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_l2cap.h>*

        BK_BT_L2CAP_OPEN_EVT.

        Public Members

        [bk_bt_l2cap_status_t](#_CPPv420bk_bt_l2cap_status_t "bk_bt_l2cap_status_t") status[](#_CPPv4N22bk_bt_l2cap_cb_param_t20l2cap_open_evt_param6statusE "永久链接至目标")
        :   status

        uint32_t handle[](#_CPPv4N22bk_bt_l2cap_cb_param_t20l2cap_open_evt_param6handleE "永久链接至目标")
        :   The connection handle

        int fd[](#_CPPv4N22bk_bt_l2cap_cb_param_t20l2cap_open_evt_param2fdE "永久链接至目标")
        :   File descriptor, lcid

        [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") rem_bda[](#_CPPv4N22bk_bt_l2cap_cb_param_t20l2cap_open_evt_param7rem_bdaE "永久链接至目标")
        :   The peer address

        int32_t tx_mtu[](#_CPPv4N22bk_bt_l2cap_cb_param_t20l2cap_open_evt_param6tx_mtuE "永久链接至目标")
        :   The transmit MTU

    struct l2cap_srv_stop_evt_param[](#_CPPv4N22bk_bt_l2cap_cb_param_t24l2cap_srv_stop_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_l2cap.h>*

        BK_BT_L2CAP_SRV_STOP_EVT.

        Public Members

        [bk_bt_l2cap_status_t](#_CPPv420bk_bt_l2cap_status_t "bk_bt_l2cap_status_t") status[](#_CPPv4N22bk_bt_l2cap_cb_param_t24l2cap_srv_stop_evt_param6statusE "永久链接至目标")
        :   status

        uint16_t psm[](#_CPPv4N22bk_bt_l2cap_cb_param_t24l2cap_srv_stop_evt_param3psmE "永久链接至目标")
        :   local psm

    struct l2cap_start_evt_param[](#_CPPv4N22bk_bt_l2cap_cb_param_t21l2cap_start_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_l2cap.h>*

        BK_BT_L2CAP_START_EVT.

        Public Members

        [bk_bt_l2cap_status_t](#_CPPv420bk_bt_l2cap_status_t "bk_bt_l2cap_status_t") status[](#_CPPv4N22bk_bt_l2cap_cb_param_t21l2cap_start_evt_param6statusE "永久链接至目标")
        :   status

        uint32_t handle[](#_CPPv4N22bk_bt_l2cap_cb_param_t21l2cap_start_evt_param6handleE "永久链接至目标")
        :   The connection handle

        uint8_t sec_id[](#_CPPv4N22bk_bt_l2cap_cb_param_t21l2cap_start_evt_param6sec_idE "永久链接至目标")
        :   security ID used by this server

    struct l2cap_uninit_evt_param[](#_CPPv4N22bk_bt_l2cap_cb_param_t22l2cap_uninit_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_l2cap.h>*

        BK_BT_L2CAP_UNINIT_EVT.

        Public Members

        [bk_bt_l2cap_status_t](#_CPPv420bk_bt_l2cap_status_t "bk_bt_l2cap_status_t") status[](#_CPPv4N22bk_bt_l2cap_cb_param_t22l2cap_uninit_evt_param6statusE "永久链接至目标")
        :   status


### Macros[](#id19 "永久链接至标题")

BK_BT_L2CAP_SEC_NONE[](#c.BK_BT_L2CAP_SEC_NONE "永久链接至目标")
:   Security Setting Mask. Use these three mask mode:

    1. BK_BT_L2CAP_SEC_NONE
    2. BK_BT_L2CAP_SEC_AUTHENTICATE
    3. (BK_BT_L2CAP_SEC_ENCRYPT|BK_BT_L2CAP_SEC_AUTHENTICATE) No security

BK_BT_L2CAP_SEC_AUTHORIZE[](#c.BK_BT_L2CAP_SEC_AUTHORIZE "永久链接至目标")
:   Authorization required

BK_BT_L2CAP_SEC_AUTHENTICATE[](#c.BK_BT_L2CAP_SEC_AUTHENTICATE "永久链接至目标")
:   Authentication required

BK_BT_L2CAP_SEC_ENCRYPT[](#c.BK_BT_L2CAP_SEC_ENCRYPT "永久链接至目标")
:   Encryption required


### Type Definitions[](#id20 "永久链接至标题")

typedef uint32_t bk_bt_l2cap_cntl_flags_t[](#_CPPv424bk_bt_l2cap_cntl_flags_t "永久链接至目标")

typedef void (*bk_bt_l2cap_cb_t)([bk_bt_l2cap_cb_event_t](#_CPPv422bk_bt_l2cap_cb_event_t "bk_bt_l2cap_cb_event_t") event, [bk_bt_l2cap_cb_param_t](#_CPPv422bk_bt_l2cap_cb_param_t "bk_bt_l2cap_cb_param_t") *param)[](#_CPPv416bk_bt_l2cap_cb_t "永久链接至目标")
:   L2CAP callback function type.

    Param event
    :   Event type

    Param param
    :   Point to callback parameter, currently is union type

typedef void (*bk_bt_l2cap_data_cb_t)(int fd, void *data, uint16_t size)[](#_CPPv421bk_bt_l2cap_data_cb_t "永久链接至目标")
:   L2CAP callback function type.

    Param fd
    :   File descriptor.

    Param data
    :   pointer to data.

    Param len
    :   data length


### Enumerations[](#id21 "永久链接至标题")

enum bk_bt_l2cap_status_t[](#_CPPv420bk_bt_l2cap_status_t "永久链接至目标")
:   L2CAP operation success and failure codes.


    *Values:*

    enumerator BK_BT_L2CAP_SUCCESS[](#_CPPv4N20bk_bt_l2cap_status_t19BK_BT_L2CAP_SUCCESSE "永久链接至目标")
    :   Successful operation.

    enumerator BK_BT_L2CAP_FAILURE[](#_CPPv4N20bk_bt_l2cap_status_t19BK_BT_L2CAP_FAILUREE "永久链接至目标")
    :   Generic failure.

    enumerator BK_BT_L2CAP_BUSY[](#_CPPv4N20bk_bt_l2cap_status_t16BK_BT_L2CAP_BUSYE "永久链接至目标")
    :   Temporarily can not handle this request.

    enumerator BK_BT_L2CAP_NO_RESOURCE[](#_CPPv4N20bk_bt_l2cap_status_t23BK_BT_L2CAP_NO_RESOURCEE "永久链接至目标")
    :   No more resource

    enumerator BK_BT_L2CAP_NEED_INIT[](#_CPPv4N20bk_bt_l2cap_status_t21BK_BT_L2CAP_NEED_INITE "永久链接至目标")
    :   L2CAP module shall init first

    enumerator BK_BT_L2CAP_NEED_DEINIT[](#_CPPv4N20bk_bt_l2cap_status_t23BK_BT_L2CAP_NEED_DEINITE "永久链接至目标")
    :   L2CAP module shall deinit first

    enumerator BK_BT_L2CAP_NO_CONNECTION[](#_CPPv4N20bk_bt_l2cap_status_t25BK_BT_L2CAP_NO_CONNECTIONE "永久链接至目标")
    :   Connection may have been closed

    enumerator BK_BT_L2CAP_NO_SERVER[](#_CPPv4N20bk_bt_l2cap_status_t21BK_BT_L2CAP_NO_SERVERE "永久链接至目标")
    :   No server

enum bk_bt_l2cap_cb_event_t[](#_CPPv422bk_bt_l2cap_cb_event_t "永久链接至目标")
:   L2CAP callback function events.


    *Values:*

    enumerator BK_BT_L2CAP_INIT_EVT[](#_CPPv4N22bk_bt_l2cap_cb_event_t20BK_BT_L2CAP_INIT_EVTE "永久链接至目标")
    :   When L2CAP is initialized, the event comes

    enumerator BK_BT_L2CAP_UNINIT_EVT[](#_CPPv4N22bk_bt_l2cap_cb_event_t22BK_BT_L2CAP_UNINIT_EVTE "永久链接至目标")
    :   When L2CAP is deinitialized, the event comes

    enumerator BK_BT_L2CAP_OPEN_EVT[](#_CPPv4N22bk_bt_l2cap_cb_event_t20BK_BT_L2CAP_OPEN_EVTE "永久链接至目标")
    :   When L2CAP Client connection open, the event comes

    enumerator BK_BT_L2CAP_CLOSE_EVT[](#_CPPv4N22bk_bt_l2cap_cb_event_t21BK_BT_L2CAP_CLOSE_EVTE "永久链接至目标")
    :   When L2CAP connection closed, the event comes

    enumerator BK_BT_L2CAP_START_EVT[](#_CPPv4N22bk_bt_l2cap_cb_event_t21BK_BT_L2CAP_START_EVTE "永久链接至目标")
    :   When L2CAP server started, the event comes

    enumerator BK_BT_L2CAP_CL_INIT_EVT[](#_CPPv4N22bk_bt_l2cap_cb_event_t23BK_BT_L2CAP_CL_INIT_EVTE "永久链接至目标")
    :   When L2CAP client initiated a connection, the event comes

    enumerator BK_BT_L2CAP_SRV_STOP_EVT[](#_CPPv4N22bk_bt_l2cap_cb_event_t24BK_BT_L2CAP_SRV_STOP_EVTE "永久链接至目标")
    :   When L2CAP server stopped, the event comes


### Header File[](#id22 "永久链接至标题")


- [bluetooth/bk_dm_spp.h](https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_spp.h "https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_spp.h")


### Functions[](#id23 "永久链接至标题")

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_spp_register_callback([bk_spp_cb_t](#_CPPv411bk_spp_cb_t "bk_spp_cb_t") callback)[](#_CPPv424bk_spp_register_callback11bk_spp_cb_t "永久链接至目标")
:   This function is called to init callbacks with SPP module.

    参数
    :   **callback** – **[in]** pointer to the init callback function.

    返回
    :   - BK_OK: success

        - other: failed

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_spp_init()[](#_CPPv411bk_spp_initv "永久链接至目标")
:   This function is called to init SPP module. When the operation is completed, the callback function will be called with BK_SPP_INIT_EVT. This function should be called after bk_bluedroid_enable() completes successfully.

    返回
    :   - BK_OK: success

        - other: failed

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_spp_deinit(void)[](#_CPPv413bk_spp_deinitv "永久链接至目标")
:   This function is called to uninit SPP module. The operation will close all active SPP connection first, then the callback function will be called with BK_SPP_CLOSE_EVT, and the number of BK_SPP_CLOSE_EVT is equal to the number of connection. When the operation is completed, the callback function will be called with BK_SPP_UNINIT_EVT. This function should be called after bk_spp_init()/bk_spp_enhanced_init() completes successfully.

    返回
    :   - BK_OK: success

        - other: failed

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_spp_start_discovery([bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bd_addr)[](#_CPPv422bk_spp_start_discovery12bk_bd_addr_t "永久链接至目标")
:   This function is called to performs service discovery for the services provided by the given peer device. When the operation is completed, the callback function will be called with BK_SPP_DISCOVERY_COMP_EVT. This function must be called after bk_spp_init()/bk_spp_enhanced_init() successful and before bk_spp_deinit().

    参数
    :   **bd_addr** – **[in]** Remote device bluetooth device address.

    返回
    :   - BK_OK: success

        - other: failed

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_spp_connect([bk_spp_role_t](#_CPPv413bk_spp_role_t "bk_spp_role_t") role, uint8_t remote_scn, uint8_t *peer_bd_addr)[](#_CPPv414bk_spp_connect13bk_spp_role_t7uint8_tP7uint8_t "永久链接至目标")
:   This function makes an SPP connection to a remote BD Address. When the connection is initiated or failed to initiate, the callback is called with BK_SPP_CL_INIT_EVT. When the connection is established or failed, the callback is called with BK_SPP_OPEN_EVT. This function must be called after bk_spp_init()/bk_spp_enhanced_init() successful and before bk_spp_deinit().

    参数
    :   - **role** – **[in]** Master or slave.

        - **remote_scn** – **[in]** Remote device bluetooth device SCN.

        - **peer_bd_addr** – **[in]** Remote device bluetooth device address.

    返回
    :   - BK_OK: success

        - other: failed

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_spp_disconnect(uint32_t handle)[](#_CPPv417bk_spp_disconnect8uint32_t "永久链接至目标")
:   This function closes an SPP connection. When the operation is completed, the callback function will be called with BK_SPP_CLOSE_EVT. This function must be called after bk_spp_init()/bk_spp_enhanced_init() successful and before bk_spp_deinit().

    参数
    :   **handle** – **[in]** The connection handle.

    返回
    :   - BK_OK: success

        - other: failed

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_spp_start_srv([bk_spp_role_t](#_CPPv413bk_spp_role_t "bk_spp_role_t") role, uint8_t local_scn, const char *name)[](#_CPPv416bk_spp_start_srv13bk_spp_role_t7uint8_tPKc "永久链接至目标")
:   This function create a SPP server and starts listening for an SPP connection request from a remote Bluetooth device. When the server is started successfully, the callback is called with BK_SPP_START_EVT. When the connection is established, the callback is called with BK_SPP_SRV_OPEN_EVT. This function must be called after bk_spp_init()/bk_spp_enhanced_init() successful and before bk_spp_deinit().

    参数
    :   - **role** – **[in]** Master or slave.

        - **local_scn** – **[in]** The specific channel you want to get. If channel is 0, means get any channel.

        - **name** – **[in]** Server’s name.

    返回
    :   - BK_OK: success

        - other: failed

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_spp_stop_srv(void)[](#_CPPv415bk_spp_stop_srvv "永久链接至目标")
:   This function stops all SPP servers. The operation will close all active SPP connection first, then the callback function will be called with BK_SPP_CLOSE_EVT, and the number of BK_SPP_CLOSE_EVT is equal to the number of connection. When the operation is completed, the callback is called with BK_SPP_SRV_STOP_EVT. This function must be called after bk_spp_init()/bk_spp_enhanced_init() successful and before bk_spp_deinit().

    返回
    :   - BK_OK: success

        - other: failed

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_spp_stop_srv_scn(uint8_t scn)[](#_CPPv419bk_spp_stop_srv_scn7uint8_t "永久链接至目标")
:   This function stops a specific SPP server. The operation will close all active SPP connection first on the specific SPP server, then the callback function will be called with BK_SPP_CLOSE_EVT, and the number of BK_SPP_CLOSE_EVT is equal to the number of connection. When the operation is completed, the callback is called with BK_SPP_SRV_STOP_EVT. This function must be called after bk_spp_init()/bk_spp_enhanced_init() successful and before bk_spp_deinit().

    参数
    :   **scn** – **[in]** Server channel number.

    返回
    :   - BK_OK: success

        - other: failed

[bt_err_t](dual_ble.md#_CPPv48bt_err_t "bt_err_t") bk_spp_write(uint32_t handle, int len, uint8_t *p_data)[](#_CPPv412bk_spp_write8uint32_tiP7uint8_t "永久链接至目标")
:   This function is used to write data, only for BK_SPP_MODE_CB. When this function need to be called repeatedly, it is strongly recommended to call this function again after the previous event BK_SPP_WRITE_EVT is received and the parameter ‘cong’ is equal to false. If the previous event BK_SPP_WRITE_EVT with parameter ‘cong’ is equal to true, the function can only be called again when the event BK_SPP_CONG_EVT with parameter ‘cong’ equal to false is received. This function must be called after an connection between initiator and acceptor has been established.

    参数
    :   - **handle** – **[in]** The connection handle.

        - **len** – **[in]** The length of the data written.

        - **p_data** – **[in]** The data written.

    返回
    :   - BK_OK: success

        - other: failed


### Unions[](#id24 "永久链接至标题")

union bk_spp_cb_param_t[](#_CPPv417bk_spp_cb_param_t "永久链接至目标")
:   *#include <bk_dm_spp.h>*

    SPP callback parameters union.

    Public Members

    struct [bk_spp_cb_param_t](#_CPPv417bk_spp_cb_param_t "bk_spp_cb_param_t")::[spp_init_evt_param](#_CPPv4N17bk_spp_cb_param_t18spp_init_evt_paramE "bk_spp_cb_param_t::spp_init_evt_param") init[](#_CPPv4N17bk_spp_cb_param_t4initE "永久链接至目标")
    :   SPP callback param of SPP_INIT_EVT

    struct [bk_spp_cb_param_t](#_CPPv417bk_spp_cb_param_t "bk_spp_cb_param_t")::[spp_uninit_evt_param](#_CPPv4N17bk_spp_cb_param_t20spp_uninit_evt_paramE "bk_spp_cb_param_t::spp_uninit_evt_param") uninit[](#_CPPv4N17bk_spp_cb_param_t6uninitE "永久链接至目标")
    :   SPP callback param of SPP_UNINIT_EVT

    struct [bk_spp_cb_param_t](#_CPPv417bk_spp_cb_param_t "bk_spp_cb_param_t")::[spp_discovery_comp_evt_param](#_CPPv4N17bk_spp_cb_param_t28spp_discovery_comp_evt_paramE "bk_spp_cb_param_t::spp_discovery_comp_evt_param") disc_comp[](#_CPPv4N17bk_spp_cb_param_t9disc_compE "永久链接至目标")
    :   SPP callback param of SPP_DISCOVERY_COMP_EVT

    struct [bk_spp_cb_param_t](#_CPPv417bk_spp_cb_param_t "bk_spp_cb_param_t")::[spp_open_evt_param](#_CPPv4N17bk_spp_cb_param_t18spp_open_evt_paramE "bk_spp_cb_param_t::spp_open_evt_param") open[](#_CPPv4N17bk_spp_cb_param_t4openE "永久链接至目标")
    :   SPP callback param of BK_SPP_OPEN_EVT

    struct [bk_spp_cb_param_t](#_CPPv417bk_spp_cb_param_t "bk_spp_cb_param_t")::[spp_srv_open_evt_param](#_CPPv4N17bk_spp_cb_param_t22spp_srv_open_evt_paramE "bk_spp_cb_param_t::spp_srv_open_evt_param") srv_open[](#_CPPv4N17bk_spp_cb_param_t8srv_openE "永久链接至目标")
    :   SPP callback param of BK_SPP_SRV_OPEN_EVT

    struct [bk_spp_cb_param_t](#_CPPv417bk_spp_cb_param_t "bk_spp_cb_param_t")::[spp_close_evt_param](#_CPPv4N17bk_spp_cb_param_t19spp_close_evt_paramE "bk_spp_cb_param_t::spp_close_evt_param") close[](#_CPPv4N17bk_spp_cb_param_t5closeE "永久链接至目标")
    :   SPP callback param of BK_SPP_CLOSE_EVT

    struct [bk_spp_cb_param_t](#_CPPv417bk_spp_cb_param_t "bk_spp_cb_param_t")::[spp_start_evt_param](#_CPPv4N17bk_spp_cb_param_t19spp_start_evt_paramE "bk_spp_cb_param_t::spp_start_evt_param") start[](#_CPPv4N17bk_spp_cb_param_t5startE "永久链接至目标")
    :   SPP callback param of BK_SPP_START_EVT

    struct [bk_spp_cb_param_t](#_CPPv417bk_spp_cb_param_t "bk_spp_cb_param_t")::[spp_srv_stop_evt_param](#_CPPv4N17bk_spp_cb_param_t22spp_srv_stop_evt_paramE "bk_spp_cb_param_t::spp_srv_stop_evt_param") srv_stop[](#_CPPv4N17bk_spp_cb_param_t8srv_stopE "永久链接至目标")
    :   SPP callback param of BK_SPP_SRV_STOP_EVT

    struct [bk_spp_cb_param_t](#_CPPv417bk_spp_cb_param_t "bk_spp_cb_param_t")::[spp_cl_init_evt_param](#_CPPv4N17bk_spp_cb_param_t21spp_cl_init_evt_paramE "bk_spp_cb_param_t::spp_cl_init_evt_param") cl_init[](#_CPPv4N17bk_spp_cb_param_t7cl_initE "永久链接至目标")
    :   SPP callback param of BK_SPP_CL_INIT_EVT

    struct [bk_spp_cb_param_t](#_CPPv417bk_spp_cb_param_t "bk_spp_cb_param_t")::[spp_write_evt_param](#_CPPv4N17bk_spp_cb_param_t19spp_write_evt_paramE "bk_spp_cb_param_t::spp_write_evt_param") write[](#_CPPv4N17bk_spp_cb_param_t5writeE "永久链接至目标")
    :   SPP callback param of BK_SPP_WRITE_EVT

    struct [bk_spp_cb_param_t](#_CPPv417bk_spp_cb_param_t "bk_spp_cb_param_t")::[spp_data_ind_evt_param](#_CPPv4N17bk_spp_cb_param_t22spp_data_ind_evt_paramE "bk_spp_cb_param_t::spp_data_ind_evt_param") data_ind[](#_CPPv4N17bk_spp_cb_param_t8data_indE "永久链接至目标")
    :   SPP callback param of BK_SPP_DATA_IND_EVT

    struct spp_cl_init_evt_param[](#_CPPv4N17bk_spp_cb_param_t21spp_cl_init_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_spp.h>*

        BK_SPP_CL_INIT_EVT.

        Public Members

        [bk_spp_status_t](#_CPPv415bk_spp_status_t "bk_spp_status_t") status[](#_CPPv4N17bk_spp_cb_param_t21spp_cl_init_evt_param6statusE "永久链接至目标")
        :   status

        uint32_t handle[](#_CPPv4N17bk_spp_cb_param_t21spp_cl_init_evt_param6handleE "永久链接至目标")
        :   The connection handle

    struct spp_close_evt_param[](#_CPPv4N17bk_spp_cb_param_t19spp_close_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_spp.h>*

        BK_SPP_CLOSE_EVT.

        Public Members

        [bk_spp_status_t](#_CPPv415bk_spp_status_t "bk_spp_status_t") status[](#_CPPv4N17bk_spp_cb_param_t19spp_close_evt_param6statusE "永久链接至目标")
        :   status

        uint32_t handle[](#_CPPv4N17bk_spp_cb_param_t19spp_close_evt_param6handleE "永久链接至目标")
        :   The connection handle

    struct spp_data_ind_evt_param[](#_CPPv4N17bk_spp_cb_param_t22spp_data_ind_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_spp.h>*

        BK_SPP_DATA_IND_EVT.

        Public Members

        [bk_spp_status_t](#_CPPv415bk_spp_status_t "bk_spp_status_t") status[](#_CPPv4N17bk_spp_cb_param_t22spp_data_ind_evt_param6statusE "永久链接至目标")
        :   status

        uint32_t handle[](#_CPPv4N17bk_spp_cb_param_t22spp_data_ind_evt_param6handleE "永久链接至目标")
        :   The connection handle

        uint16_t len[](#_CPPv4N17bk_spp_cb_param_t22spp_data_ind_evt_param3lenE "永久链接至目标")
        :   The length of data

        uint8_t *data[](#_CPPv4N17bk_spp_cb_param_t22spp_data_ind_evt_param4dataE "永久链接至目标")
        :   The data received

    struct spp_discovery_comp_evt_param[](#_CPPv4N17bk_spp_cb_param_t28spp_discovery_comp_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_spp.h>*

        SPP_DISCOVERY_COMP_EVT.

        Public Members

        [bk_spp_status_t](#_CPPv415bk_spp_status_t "bk_spp_status_t") status[](#_CPPv4N17bk_spp_cb_param_t28spp_discovery_comp_evt_param6statusE "永久链接至目标")
        :   status

        uint8_t scn_num[](#_CPPv4N17bk_spp_cb_param_t28spp_discovery_comp_evt_param7scn_numE "永久链接至目标")
        :   The num of scn_num

        uint8_t scn[BK_SPP_MAX_SCN][](#_CPPv4N17bk_spp_cb_param_t28spp_discovery_comp_evt_param3scnE "永久链接至目标")
        :   channel #

        const char *service_name[BK_SPP_MAX_SCN][](#_CPPv4N17bk_spp_cb_param_t28spp_discovery_comp_evt_param12service_nameE "永久链接至目标")
        :   service_name

    struct spp_init_evt_param[](#_CPPv4N17bk_spp_cb_param_t18spp_init_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_spp.h>*

        SPP_INIT_EVT.

        Public Members

        [bk_spp_status_t](#_CPPv415bk_spp_status_t "bk_spp_status_t") status[](#_CPPv4N17bk_spp_cb_param_t18spp_init_evt_param6statusE "永久链接至目标")
        :   status

    struct spp_open_evt_param[](#_CPPv4N17bk_spp_cb_param_t18spp_open_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_spp.h>*

        BK_SPP_OPEN_EVT.

        Public Members

        [bk_spp_status_t](#_CPPv415bk_spp_status_t "bk_spp_status_t") status[](#_CPPv4N17bk_spp_cb_param_t18spp_open_evt_param6statusE "永久链接至目标")
        :   status

        uint32_t handle[](#_CPPv4N17bk_spp_cb_param_t18spp_open_evt_param6handleE "永久链接至目标")
        :   The connection handle

        [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") rem_bda[](#_CPPv4N17bk_spp_cb_param_t18spp_open_evt_param7rem_bdaE "永久链接至目标")
        :   The peer address

    struct spp_srv_open_evt_param[](#_CPPv4N17bk_spp_cb_param_t22spp_srv_open_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_spp.h>*

        BK_SPP_SRV_OPEN_EVT.

        Public Members

        [bk_spp_status_t](#_CPPv415bk_spp_status_t "bk_spp_status_t") status[](#_CPPv4N17bk_spp_cb_param_t22spp_srv_open_evt_param6statusE "永久链接至目标")
        :   status

        uint32_t handle[](#_CPPv4N17bk_spp_cb_param_t22spp_srv_open_evt_param6handleE "永久链接至目标")
        :   The connection handle

        [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") rem_bda[](#_CPPv4N17bk_spp_cb_param_t22spp_srv_open_evt_param7rem_bdaE "永久链接至目标")
        :   The peer address

    struct spp_srv_stop_evt_param[](#_CPPv4N17bk_spp_cb_param_t22spp_srv_stop_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_spp.h>*

        BK_SPP_SRV_STOP_EVT.

        Public Members

        [bk_spp_status_t](#_CPPv415bk_spp_status_t "bk_spp_status_t") status[](#_CPPv4N17bk_spp_cb_param_t22spp_srv_stop_evt_param6statusE "永久链接至目标")
        :   status

        uint8_t scn[](#_CPPv4N17bk_spp_cb_param_t22spp_srv_stop_evt_param3scnE "永久链接至目标")
        :   Server channel number

    struct spp_start_evt_param[](#_CPPv4N17bk_spp_cb_param_t19spp_start_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_spp.h>*

        BK_SPP_START_EVT.

        Public Members

        [bk_spp_status_t](#_CPPv415bk_spp_status_t "bk_spp_status_t") status[](#_CPPv4N17bk_spp_cb_param_t19spp_start_evt_param6statusE "永久链接至目标")
        :   status

        uint32_t handle[](#_CPPv4N17bk_spp_cb_param_t19spp_start_evt_param6handleE "永久链接至目标")
        :   The connection handle

        uint8_t scn[](#_CPPv4N17bk_spp_cb_param_t19spp_start_evt_param3scnE "永久链接至目标")
        :   Server channel number

    struct spp_uninit_evt_param[](#_CPPv4N17bk_spp_cb_param_t20spp_uninit_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_spp.h>*

        SPP_UNINIT_EVT.

        Public Members

        [bk_spp_status_t](#_CPPv415bk_spp_status_t "bk_spp_status_t") status[](#_CPPv4N17bk_spp_cb_param_t20spp_uninit_evt_param6statusE "永久链接至目标")
        :   status

    struct spp_write_evt_param[](#_CPPv4N17bk_spp_cb_param_t19spp_write_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_spp.h>*

        BK_SPP_WRITE_EVT.

        Public Members

        [bk_spp_status_t](#_CPPv415bk_spp_status_t "bk_spp_status_t") status[](#_CPPv4N17bk_spp_cb_param_t19spp_write_evt_param6statusE "永久链接至目标")
        :   status

        uint32_t handle[](#_CPPv4N17bk_spp_cb_param_t19spp_write_evt_param6handleE "永久链接至目标")
        :   The connection handle

        uint16_t len[](#_CPPv4N17bk_spp_cb_param_t19spp_write_evt_param3lenE "永久链接至目标")
        :   The length of the data written.


### Macros[](#id25 "永久链接至标题")

BK_SPP_MAX_SCN[](#c.BK_SPP_MAX_SCN "永久链接至目标")
:   SPP max SCN

BK_SPP_MIN_TX_BUFFER_SIZE[](#c.BK_SPP_MIN_TX_BUFFER_SIZE "永久链接至目标")
:   SPP min tx buffer

BK_SPP_MAX_TX_BUFFER_SIZE[](#c.BK_SPP_MAX_TX_BUFFER_SIZE "永久链接至目标")
:   SPP max tx buffer size


### Type Definitions[](#id26 "永久链接至标题")

typedef void (*bk_spp_cb_t)([bk_spp_cb_event_t](#_CPPv417bk_spp_cb_event_t "bk_spp_cb_event_t") event, [bk_spp_cb_param_t](#_CPPv417bk_spp_cb_param_t "bk_spp_cb_param_t") *param)[](#_CPPv411bk_spp_cb_t "永久链接至目标")
:   SPP callback function type. When handle BK_SPP_DATA_IND_EVT, it is strongly recommended to cache incoming data, and process them in other lower priority application task rather than in this callback directly.

    Param event
    :   Event type

    Param param
    :   Point to callback parameter, currently is union type


### Enumerations[](#id27 "永久链接至标题")

enum bk_spp_status_t[](#_CPPv415bk_spp_status_t "永久链接至目标")
:   *Values:*

    enumerator BK_SPP_SUCCESS[](#_CPPv4N15bk_spp_status_t14BK_SPP_SUCCESSE "永久链接至目标")
    :   Successful operation.

    enumerator BK_SPP_FAILURE[](#_CPPv4N15bk_spp_status_t14BK_SPP_FAILUREE "永久链接至目标")
    :   Generic failure.

    enumerator BK_SPP_BUSY[](#_CPPv4N15bk_spp_status_t11BK_SPP_BUSYE "永久链接至目标")
    :   Temporarily can not handle this request.

    enumerator BK_SPP_NO_DATA[](#_CPPv4N15bk_spp_status_t14BK_SPP_NO_DATAE "永久链接至目标")
    :   No data

    enumerator BK_SPP_NO_RESOURCE[](#_CPPv4N15bk_spp_status_t18BK_SPP_NO_RESOURCEE "永久链接至目标")
    :   No more resource

    enumerator BK_SPP_NEED_INIT[](#_CPPv4N15bk_spp_status_t16BK_SPP_NEED_INITE "永久链接至目标")
    :   SPP module shall init first

    enumerator BK_SPP_NEED_DEINIT[](#_CPPv4N15bk_spp_status_t18BK_SPP_NEED_DEINITE "永久链接至目标")
    :   SPP module shall deinit first

    enumerator BK_SPP_NO_CONNECTION[](#_CPPv4N15bk_spp_status_t20BK_SPP_NO_CONNECTIONE "永久链接至目标")
    :   Connection may have been closed

    enumerator BK_SPP_NO_SERVER[](#_CPPv4N15bk_spp_status_t16BK_SPP_NO_SERVERE "永久链接至目标")
    :   No SPP server

enum bk_spp_role_t[](#_CPPv413bk_spp_role_t "永久链接至目标")
:   *Values:*

    enumerator BK_SPP_ROLE_MASTER[](#_CPPv4N13bk_spp_role_t18BK_SPP_ROLE_MASTERE "永久链接至目标")
    :   Role: master

    enumerator BK_SPP_ROLE_SLAVE[](#_CPPv4N13bk_spp_role_t17BK_SPP_ROLE_SLAVEE "永久链接至目标")
    :   Role: slave

enum bk_spp_cb_event_t[](#_CPPv417bk_spp_cb_event_t "永久链接至目标")
:   SPP callback function events.


    *Values:*

    enumerator BK_SPP_INIT_EVT[](#_CPPv4N17bk_spp_cb_event_t15BK_SPP_INIT_EVTE "永久链接至目标")
    :   When SPP is initialized, the event comes

    enumerator BK_SPP_UNINIT_EVT[](#_CPPv4N17bk_spp_cb_event_t17BK_SPP_UNINIT_EVTE "永久链接至目标")
    :   When SPP is deinitialized, the event comes

    enumerator BK_SPP_DISCOVERY_COMP_EVT[](#_CPPv4N17bk_spp_cb_event_t25BK_SPP_DISCOVERY_COMP_EVTE "永久链接至目标")
    :   When SDP discovery complete, the event comes

    enumerator BK_SPP_OPEN_EVT[](#_CPPv4N17bk_spp_cb_event_t15BK_SPP_OPEN_EVTE "永久链接至目标")
    :   When SPP Client connection open, the event comes

    enumerator BK_SPP_CLOSE_EVT[](#_CPPv4N17bk_spp_cb_event_t16BK_SPP_CLOSE_EVTE "永久链接至目标")
    :   When SPP connection closed, the event comes

    enumerator BK_SPP_START_EVT[](#_CPPv4N17bk_spp_cb_event_t16BK_SPP_START_EVTE "永久链接至目标")
    :   When SPP server started, the event comes

    enumerator BK_SPP_CL_INIT_EVT[](#_CPPv4N17bk_spp_cb_event_t18BK_SPP_CL_INIT_EVTE "永久链接至目标")
    :   When SPP client initiated a connection, the event comes

    enumerator BK_SPP_DATA_IND_EVT[](#_CPPv4N17bk_spp_cb_event_t19BK_SPP_DATA_IND_EVTE "永久链接至目标")
    :   When SPP connection received data, the event comes, only for BK_SPP_MODE_CB

    enumerator BK_SPP_WRITE_EVT[](#_CPPv4N17bk_spp_cb_event_t16BK_SPP_WRITE_EVTE "永久链接至目标")
    :   When SPP write operation completes, the event comes, only for BK_SPP_MODE_CB

    enumerator BK_SPP_SRV_OPEN_EVT[](#_CPPv4N17bk_spp_cb_event_t19BK_SPP_SRV_OPEN_EVTE "永久链接至目标")
    :   When SPP Server connection open, the event comes

    enumerator BK_SPP_SRV_STOP_EVT[](#_CPPv4N17bk_spp_cb_event_t19BK_SPP_SRV_STOP_EVTE "永久链接至目标")
    :   When SPP server stopped, the event comes


## API Typedefs[](#api-typedefs "永久链接至标题")


### Header File[](#id28 "永久链接至标题")


- [bluetooth/bk_dm_a2dp_types.h](https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_a2dp_types.h "https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_a2dp_types.h")


### Unions[](#id29 "永久链接至标题")

union bk_a2dp_cb_param_t[](#_CPPv418bk_a2dp_cb_param_t "永久链接至目标")
:   *#include <bk_dm_a2dp_types.h>*

    A2DP state callback parameters.

    Public Members

    struct [bk_a2dp_cb_param_t](#_CPPv418bk_a2dp_cb_param_t "bk_a2dp_cb_param_t")::[a2dp_conn_state_param](#_CPPv4N18bk_a2dp_cb_param_t21a2dp_conn_state_paramE "bk_a2dp_cb_param_t::a2dp_conn_state_param") conn_state[](#_CPPv4N18bk_a2dp_cb_param_t10conn_stateE "永久链接至目标")
    :   A2DP connection status

    struct [bk_a2dp_cb_param_t](#_CPPv418bk_a2dp_cb_param_t "bk_a2dp_cb_param_t")::[a2dp_audio_state_param](#_CPPv4N18bk_a2dp_cb_param_t22a2dp_audio_state_paramE "bk_a2dp_cb_param_t::a2dp_audio_state_param") audio_state[](#_CPPv4N18bk_a2dp_cb_param_t11audio_stateE "永久链接至目标")
    :   audio stream playing state

    struct [bk_a2dp_cb_param_t](#_CPPv418bk_a2dp_cb_param_t "bk_a2dp_cb_param_t")::[a2dp_audio_cfg_param](#_CPPv4N18bk_a2dp_cb_param_t20a2dp_audio_cfg_paramE "bk_a2dp_cb_param_t::a2dp_audio_cfg_param") audio_cfg[](#_CPPv4N18bk_a2dp_cb_param_t9audio_cfgE "永久链接至目标")
    :   media codec configuration information

    struct [bk_a2dp_cb_param_t](#_CPPv418bk_a2dp_cb_param_t "bk_a2dp_cb_param_t")::[a2dp_audio_source_cfg_param](#_CPPv4N18bk_a2dp_cb_param_t27a2dp_audio_source_cfg_paramE "bk_a2dp_cb_param_t::a2dp_audio_source_cfg_param") audio_source_cfg[](#_CPPv4N18bk_a2dp_cb_param_t16audio_source_cfgE "永久链接至目标")
    :   media codec configuration information

    struct [bk_a2dp_cb_param_t](#_CPPv418bk_a2dp_cb_param_t "bk_a2dp_cb_param_t")::[media_ctrl_stat_param](#_CPPv4N18bk_a2dp_cb_param_t21media_ctrl_stat_paramE "bk_a2dp_cb_param_t::media_ctrl_stat_param") media_ctrl_stat[](#_CPPv4N18bk_a2dp_cb_param_t15media_ctrl_statE "永久链接至目标")
    :   status in acknowledgement to media control commands

    struct [bk_a2dp_cb_param_t](#_CPPv418bk_a2dp_cb_param_t "bk_a2dp_cb_param_t")::[a2dp_prof_stat_param](#_CPPv4N18bk_a2dp_cb_param_t20a2dp_prof_stat_paramE "bk_a2dp_cb_param_t::a2dp_prof_stat_param") a2dp_prof_stat[](#_CPPv4N18bk_a2dp_cb_param_t14a2dp_prof_statE "永久链接至目标")
    :   status to indicate a2dp prof init or deinit

    struct [bk_a2dp_cb_param_t](#_CPPv418bk_a2dp_cb_param_t "bk_a2dp_cb_param_t")::[a2dp_set_stat_param](#_CPPv4N18bk_a2dp_cb_param_t19a2dp_set_stat_paramE "bk_a2dp_cb_param_t::a2dp_set_stat_param") a2dp_set_delay_value_stat[](#_CPPv4N18bk_a2dp_cb_param_t25a2dp_set_delay_value_statE "永久链接至目标")
    :   A2DP sink set delay report value status

    struct [bk_a2dp_cb_param_t](#_CPPv418bk_a2dp_cb_param_t "bk_a2dp_cb_param_t")::[a2dp_get_stat_param](#_CPPv4N18bk_a2dp_cb_param_t19a2dp_get_stat_paramE "bk_a2dp_cb_param_t::a2dp_get_stat_param") a2dp_get_delay_value_stat[](#_CPPv4N18bk_a2dp_cb_param_t25a2dp_get_delay_value_statE "永久链接至目标")
    :   A2DP sink get delay report value status

    struct a2dp_audio_cfg_param[](#_CPPv4N18bk_a2dp_cb_param_t20a2dp_audio_cfg_paramE "永久链接至目标")
    :   *#include <bk_dm_a2dp_types.h>*

        BK_A2DP_AUDIO_CFG_EVT.

        Public Members

        uint8_t remote_bda[6][](#_CPPv4N18bk_a2dp_cb_param_t20a2dp_audio_cfg_param10remote_bdaE "永久链接至目标")
        :   remote bluetooth device address

        [bk_a2dp_mcc_t](#_CPPv413bk_a2dp_mcc_t "bk_a2dp_mcc_t") mcc[](#_CPPv4N18bk_a2dp_cb_param_t20a2dp_audio_cfg_param3mccE "永久链接至目标")
        :   A2DP media codec capability information

    struct a2dp_audio_source_cfg_param[](#_CPPv4N18bk_a2dp_cb_param_t27a2dp_audio_source_cfg_paramE "永久链接至目标")
    :   *#include <bk_dm_a2dp_types.h>*

        BK_A2DP_AUDIO_SOURCE_CFG_EVT.

        Public Members

        uint8_t remote_bda[6][](#_CPPv4N18bk_a2dp_cb_param_t27a2dp_audio_source_cfg_param10remote_bdaE "永久链接至目标")
        :   remote bluetooth device address

        uint16_t mtu[](#_CPPv4N18bk_a2dp_cb_param_t27a2dp_audio_source_cfg_param3mtuE "永久链接至目标")

        [bk_a2dp_mcc_t](#_CPPv413bk_a2dp_mcc_t "bk_a2dp_mcc_t") mcc[](#_CPPv4N18bk_a2dp_cb_param_t27a2dp_audio_source_cfg_param3mccE "永久链接至目标")
        :   max payload len, only used in source A2DP media codec capability information

    struct a2dp_audio_state_param[](#_CPPv4N18bk_a2dp_cb_param_t22a2dp_audio_state_paramE "永久链接至目标")
    :   *#include <bk_dm_a2dp_types.h>*

        BK_A2DP_AUDIO_STATE_EVT.

        Public Members

        [bk_a2dp_audio_state_t](#_CPPv421bk_a2dp_audio_state_t "bk_a2dp_audio_state_t") state[](#_CPPv4N18bk_a2dp_cb_param_t22a2dp_audio_state_param5stateE "永久链接至目标")
        :   one of the values from bk_a2dp_audio_state_t

        uint8_t remote_bda[6][](#_CPPv4N18bk_a2dp_cb_param_t22a2dp_audio_state_param10remote_bdaE "永久链接至目标")
        :   remote bluetooth device address

    struct a2dp_conn_state_param[](#_CPPv4N18bk_a2dp_cb_param_t21a2dp_conn_state_paramE "永久链接至目标")
    :   *#include <bk_dm_a2dp_types.h>*

        BK_A2DP_CONNECTION_STATE_EVT.

        Public Members

        [bk_a2dp_connection_state_t](#_CPPv426bk_a2dp_connection_state_t "bk_a2dp_connection_state_t") state[](#_CPPv4N18bk_a2dp_cb_param_t21a2dp_conn_state_param5stateE "永久链接至目标")
        :   one of values from bk_a2dp_connection_state_t

        uint8_t remote_bda[6][](#_CPPv4N18bk_a2dp_cb_param_t21a2dp_conn_state_param10remote_bdaE "永久链接至目标")
        :   remote bluetooth device address

        [bk_a2dp_disc_rsn_t](#_CPPv418bk_a2dp_disc_rsn_t "bk_a2dp_disc_rsn_t") disc_rsn[](#_CPPv4N18bk_a2dp_cb_param_t21a2dp_conn_state_param8disc_rsnE "永久链接至目标")
        :   reason of disconnection for “DISCONNECTED”

    struct a2dp_get_stat_param[](#_CPPv4N18bk_a2dp_cb_param_t19a2dp_get_stat_paramE "永久链接至目标")
    :   *#include <bk_dm_a2dp_types.h>*

        BK_A2DP_SNK_GET_DELAY_VALUE_EVT.

        Public Members

        uint16_t delay_value[](#_CPPv4N18bk_a2dp_cb_param_t19a2dp_get_stat_param11delay_valueE "永久链接至目标")
        :   delay report value

    struct a2dp_prof_stat_param[](#_CPPv4N18bk_a2dp_cb_param_t20a2dp_prof_stat_paramE "永久链接至目标")
    :   *#include <bk_dm_a2dp_types.h>*

        BK_A2DP_PROF_STATE_EVT.

        Public Members

        uint8_t action[](#_CPPv4N18bk_a2dp_cb_param_t20a2dp_prof_stat_param6actionE "永久链接至目标")

        uint8_t role[](#_CPPv4N18bk_a2dp_cb_param_t20a2dp_prof_stat_param4roleE "永久链接至目标")
        :   0 means init, 1 means deinit

        uint8_t status[](#_CPPv4N18bk_a2dp_cb_param_t20a2dp_prof_stat_param6statusE "永久链接至目标")
        :   0 means source, 1 means sink

        uint8_t reason[](#_CPPv4N18bk_a2dp_cb_param_t20a2dp_prof_stat_param6reasonE "永久链接至目标")
        :   0 means success, other means fail

    struct a2dp_set_stat_param[](#_CPPv4N18bk_a2dp_cb_param_t19a2dp_set_stat_paramE "永久链接至目标")
    :   *#include <bk_dm_a2dp_types.h>*

        BK_A2DP_SNK_SET_DELAY_VALUE_EVT.

        Public Members

        [bk_a2dp_set_delay_value_state_t](#_CPPv431bk_a2dp_set_delay_value_state_t "bk_a2dp_set_delay_value_state_t") set_state[](#_CPPv4N18bk_a2dp_cb_param_t19a2dp_set_stat_param9set_stateE "永久链接至目标")
        :   a2dp profile state param

        uint16_t delay_value[](#_CPPv4N18bk_a2dp_cb_param_t19a2dp_set_stat_param11delay_valueE "永久链接至目标")
        :   delay report value

    struct media_ctrl_stat_param[](#_CPPv4N18bk_a2dp_cb_param_t21media_ctrl_stat_paramE "永久链接至目标")
    :   *#include <bk_dm_a2dp_types.h>*

        BK_A2DP_MEDIA_CTRL_ACK_EVT.

        Public Members

        [bk_a2dp_media_ctrl_t](#_CPPv420bk_a2dp_media_ctrl_t "bk_a2dp_media_ctrl_t") cmd[](#_CPPv4N18bk_a2dp_cb_param_t21media_ctrl_stat_param3cmdE "永久链接至目标")
        :   media control commands to acknowledge

        [bk_a2dp_media_ctrl_ack_t](#_CPPv424bk_a2dp_media_ctrl_ack_t "bk_a2dp_media_ctrl_ack_t") status[](#_CPPv4N18bk_a2dp_cb_param_t21media_ctrl_stat_param6statusE "永久链接至目标")
        :   acknowledgement to media control commands


### Structures[](#id30 "永久链接至标题")

struct bk_a2dp_mcc_t[](#_CPPv413bk_a2dp_mcc_t "永久链接至目标")
:   A2DP media codec capabilities union.

    Public Members

    uint8_t type[](#_CPPv4N13bk_a2dp_mcc_t4typeE "永久链接至目标")
    :   A2DP media codec type

    struct [bk_a2dp_mcc_t](#_CPPv413bk_a2dp_mcc_t "bk_a2dp_mcc_t")::[anonymous]::[anonymous] sbc_codec[](#_CPPv4N13bk_a2dp_mcc_t9sbc_codecE "永久链接至目标")
    :   SBC codec capabilities.

    struct [bk_a2dp_mcc_t](#_CPPv413bk_a2dp_mcc_t "bk_a2dp_mcc_t")::[anonymous]::[anonymous] aac_codec[](#_CPPv4N13bk_a2dp_mcc_t9aac_codecE "永久链接至目标")
    :   MPEG-2, 4 AAC codec capabilities.

    union [bk_a2dp_mcc_t](#_CPPv413bk_a2dp_mcc_t "bk_a2dp_mcc_t")::[anonymous] cie[](#_CPPv4N13bk_a2dp_mcc_t3cieE "永久链接至目标")
    :   A2DP codec information element


### Type Definitions[](#id31 "永久链接至标题")

typedef void (*bk_bt_a2dp_cb_t)([bk_a2dp_cb_event_t](#_CPPv418bk_a2dp_cb_event_t "bk_a2dp_cb_event_t") event, [bk_a2dp_cb_param_t](#_CPPv418bk_a2dp_cb_param_t "bk_a2dp_cb_param_t") *param)[](#_CPPv415bk_bt_a2dp_cb_t "永久链接至目标")
:   A2DP profile callback function type.

    Param event
    :   : Event type

    Param param
    :   : Pointer to callback parameter

typedef void (*bk_bt_sink_data_cb_t)(const uint8_t *buf, uint16_t len)[](#_CPPv420bk_bt_sink_data_cb_t "永久链接至目标")
:   A2DP sink data callback function.

    Param buf
    :   **[in]** : pointer to the data received from A2DP source device

    Param len
    :   **[in]** : size(in bytes) in buf

typedef int32_t (*bk_a2dp_source_data_cb_t)(uint8_t *buf, int32_t len)[](#_CPPv424bk_a2dp_source_data_cb_t "永久链接至目标")
:   A2DP source data read callback function.

    Param buf
    :   **[in]** : buffer to be filled with PCM data stream from higher layer

    Param len
    :   **[in]** : size(in bytes) of data block to be copied to buf. -1 is an indication to user that data buffer shall be flushed

    Return
    :   size of bytes read successfully, if the argument len is -1, this value is ignored.

typedef int32_t (*bk_a2dp_source_pcm_resample_cb_t)(uint8_t *in_addr, uint32_t *in_len, uint8_t *out_addr, uint32_t *out_len)[](#_CPPv432bk_a2dp_source_pcm_resample_cb_t "永久链接至目标")
:   pcm resample callback function

    Param in_addr
    :   **[in]** : input buff before resample (in bytes).

    Param [in|out]
    :   in_len : input buff len (in bytes). When call done, it should change to how many bytes had processed.

    Param out_addr
    :   **[in]** : input buff after resample (in bytes).

    Param [in|out]
    :   out_len : out buff len (in bytes). When call done, it should change to how many bytes had outputed.

    Return
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail, bluetooth will ignore the data.

typedef int32_t (*bk_a2dp_source_pcm_encode_cb_t)(uint8_t type, uint8_t *in_addr, uint32_t *in_len, uint8_t *out_addr, uint32_t *out_len)[](#_CPPv430bk_a2dp_source_pcm_encode_cb_t "永久链接至目标")
:   pcm encode callback function

    Param type
    :   **[in]** : encode type, 0 means sbc.

    Param in_addr
    :   **[in]** : input buff before encode (in bytes).

    Param [in|out]
    :   in_len : input buff len (in bytes). When call done, it should change to how many bytes had processed.

    Param out_addr
    :   **[in]** : input buff after encode (in bytes).

    Param [in|out]
    :   out_len : out buff len (in bytes). When call done, it should change to how many bytes had outputed.

    Return
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail, bluetooth will ignore the data.


### Enumerations[](#id32 "永久链接至标题")

enum bk_a2dp_cb_event_t[](#_CPPv418bk_a2dp_cb_event_t "永久链接至目标")
:   A2DP callback events.


    *Values:*

    enumerator BK_A2DP_CONNECTION_STATE_EVT[](#_CPPv4N18bk_a2dp_cb_event_t28BK_A2DP_CONNECTION_STATE_EVTE "永久链接至目标")
    :   connection state changed event

    enumerator BK_A2DP_AUDIO_STATE_EVT[](#_CPPv4N18bk_a2dp_cb_event_t23BK_A2DP_AUDIO_STATE_EVTE "永久链接至目标")
    :   audio stream transmission state changed event

    enumerator BK_A2DP_AUDIO_CFG_EVT[](#_CPPv4N18bk_a2dp_cb_event_t21BK_A2DP_AUDIO_CFG_EVTE "永久链接至目标")
    :   audio codec is configured, only used for A2DP SINK

    enumerator BK_A2DP_AUDIO_SOURCE_CFG_EVT[](#_CPPv4N18bk_a2dp_cb_event_t28BK_A2DP_AUDIO_SOURCE_CFG_EVTE "永久链接至目标")
    :   audio codec is configured, only used for A2DP SOURCE

    enumerator BK_A2DP_MEDIA_CTRL_ACK_EVT[](#_CPPv4N18bk_a2dp_cb_event_t26BK_A2DP_MEDIA_CTRL_ACK_EVTE "永久链接至目标")
    :   acknowledge event in response to media control commands

    enumerator BK_A2DP_PROF_STATE_EVT[](#_CPPv4N18bk_a2dp_cb_event_t22BK_A2DP_PROF_STATE_EVTE "永久链接至目标")
    :   indicate a2dp init&deinit complete

    enumerator BK_A2DP_SNK_SET_DELAY_VALUE_EVT[](#_CPPv4N18bk_a2dp_cb_event_t31BK_A2DP_SNK_SET_DELAY_VALUE_EVTE "永久链接至目标")
    :   indicate a2dp sink set delay report value complete, only used for A2DP SINK

    enumerator BK_A2DP_SNK_GET_DELAY_VALUE_EVT[](#_CPPv4N18bk_a2dp_cb_event_t31BK_A2DP_SNK_GET_DELAY_VALUE_EVTE "永久链接至目标")
    :   indicate a2dp sink get delay report value complete, only used for A2DP SINK

enum bk_a2dp_connection_state_t[](#_CPPv426bk_a2dp_connection_state_t "永久链接至目标")
:   Bluetooth A2DP connection states.


    *Values:*

    enumerator BK_A2DP_CONNECTION_STATE_DISCONNECTED[](#_CPPv4N26bk_a2dp_connection_state_t37BK_A2DP_CONNECTION_STATE_DISCONNECTEDE "永久链接至目标")
    :   connection released

    enumerator BK_A2DP_CONNECTION_STATE_CONNECTING[](#_CPPv4N26bk_a2dp_connection_state_t35BK_A2DP_CONNECTION_STATE_CONNECTINGE "永久链接至目标")
    :   connecting remote device

    enumerator BK_A2DP_CONNECTION_STATE_CONNECTED[](#_CPPv4N26bk_a2dp_connection_state_t34BK_A2DP_CONNECTION_STATE_CONNECTEDE "永久链接至目标")
    :   connection established

    enumerator BK_A2DP_CONNECTION_STATE_DISCONNECTING[](#_CPPv4N26bk_a2dp_connection_state_t38BK_A2DP_CONNECTION_STATE_DISCONNECTINGE "永久链接至目标")
    :   disconnecting remote device

enum bk_a2dp_disc_rsn_t[](#_CPPv418bk_a2dp_disc_rsn_t "永久链接至目标")
:   Bluetooth A2DP disconnection reason.


    *Values:*

    enumerator BK_A2DP_DISC_RSN_NORMAL[](#_CPPv4N18bk_a2dp_disc_rsn_t23BK_A2DP_DISC_RSN_NORMALE "永久链接至目标")
    :   Finished disconnection that is initiated by local or remote device

    enumerator BK_A2DP_DISC_RSN_ABNORMAL[](#_CPPv4N18bk_a2dp_disc_rsn_t25BK_A2DP_DISC_RSN_ABNORMALE "永久链接至目标")
    :   Abnormal disconnection caused by signal loss

enum bk_a2dp_audio_state_t[](#_CPPv421bk_a2dp_audio_state_t "永久链接至目标")
:   Bluetooth A2DP datapath states.


    *Values:*

    enumerator BK_A2DP_AUDIO_STATE_SUSPEND[](#_CPPv4N21bk_a2dp_audio_state_t27BK_A2DP_AUDIO_STATE_SUSPENDE "永久链接至目标")
    :   audio stream datapath suspend

    enumerator BK_A2DP_AUDIO_STATE_STARTED[](#_CPPv4N21bk_a2dp_audio_state_t27BK_A2DP_AUDIO_STATE_STARTEDE "永久链接至目标")
    :   audio stream datapath started

enum bk_a2dp_media_ctrl_t[](#_CPPv420bk_a2dp_media_ctrl_t "永久链接至目标")
:   A2DP media control commands.


    *Values:*

    enumerator BK_A2DP_MEDIA_CTRL_START[](#_CPPv4N20bk_a2dp_media_ctrl_t24BK_A2DP_MEDIA_CTRL_STARTE "永久链接至目标")
    :   command to set up media transmission channel

    enumerator BK_A2DP_MEDIA_CTRL_SUSPEND[](#_CPPv4N20bk_a2dp_media_ctrl_t26BK_A2DP_MEDIA_CTRL_SUSPENDE "永久链接至目标")
    :   command to suspend media transmission

enum bk_a2dp_media_ctrl_ack_t[](#_CPPv424bk_a2dp_media_ctrl_ack_t "永久链接至目标")
:   A2DP media control command acknowledgement code.


    *Values:*

    enumerator BK_A2DP_MEDIA_CTRL_ACK_SUCCESS[](#_CPPv4N24bk_a2dp_media_ctrl_ack_t30BK_A2DP_MEDIA_CTRL_ACK_SUCCESSE "永久链接至目标")
    :   media control command is acknowledged with success

    enumerator BK_A2DP_MEDIA_CTRL_ACK_FAILURE[](#_CPPv4N24bk_a2dp_media_ctrl_ack_t30BK_A2DP_MEDIA_CTRL_ACK_FAILUREE "永久链接至目标")
    :   media control command is acknowledged with failure

    enumerator BK_A2DP_MEDIA_CTRL_ACK_BUSY[](#_CPPv4N24bk_a2dp_media_ctrl_ack_t27BK_A2DP_MEDIA_CTRL_ACK_BUSYE "永久链接至目标")
    :   media control command is rejected, as previous command is not yet acknowledged

enum bk_a2dp_set_delay_value_state_t[](#_CPPv431bk_a2dp_set_delay_value_state_t "永久链接至目标")
:   Bluetooth A2DP set delay report value states.


    *Values:*

    enumerator BK_A2DP_SET_SUCCESS[](#_CPPv4N31bk_a2dp_set_delay_value_state_t19BK_A2DP_SET_SUCCESSE "永久链接至目标")
    :   A2DP profile set delay report value successful

    enumerator BK_A2DP_SET_FAIL[](#_CPPv4N31bk_a2dp_set_delay_value_state_t16BK_A2DP_SET_FAILE "永久链接至目标")
    :   A2DP profile set delay report value failed


### Header File[](#id33 "永久链接至标题")


- [bluetooth/bk_dm_avrcp_types.h](https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_avrcp_types.h "https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_avrcp_types.h")


### Unions[](#id34 "永久链接至标题")

union bk_avrcp_rn_param_t[](#_CPPv419bk_avrcp_rn_param_t "永久链接至目标")
:   *#include <bk_dm_avrcp_types.h>*

    AVRCP notification parameters.

    Public Members

    uint8_t volume[](#_CPPv4N19bk_avrcp_rn_param_t6volumeE "永久链接至目标")
    :   response data for BK_AVRCP_RN_VOLUME_CHANGE, ranges 0..127

    [bk_avrcp_playback_stat_t](#_CPPv424bk_avrcp_playback_stat_t "bk_avrcp_playback_stat_t") playback[](#_CPPv4N19bk_avrcp_rn_param_t8playbackE "永久链接至目标")
    :   response data for BK_AVRCP_RN_PLAY_STATUS_CHANGE

    uint8_t elm_id[8][](#_CPPv4N19bk_avrcp_rn_param_t6elm_idE "永久链接至目标")
    :   response data for BK_AVRCP_RN_TRACK_CHANGE

    uint32_t play_pos[](#_CPPv4N19bk_avrcp_rn_param_t8play_posE "永久链接至目标")
    :   response data for BK_AVRCP_RN_PLAY_POS_CHANGED, in millisecond

    [bk_avrcp_batt_stat_t](#_CPPv420bk_avrcp_batt_stat_t "bk_avrcp_batt_stat_t") batt[](#_CPPv4N19bk_avrcp_rn_param_t4battE "永久链接至目标")
    :   response data for BK_AVRCP_RN_BATTERY_STATUS_CHANGE

    uint16_t player_id[](#_CPPv4N19bk_avrcp_rn_param_t9player_idE "永久链接至目标")

    uint16_t uid[](#_CPPv4N19bk_avrcp_rn_param_t3uidE "永久链接至目标")

    struct [bk_avrcp_rn_param_t](#_CPPv419bk_avrcp_rn_param_t "bk_avrcp_rn_param_t")::[anonymous] [anonymous][](#_CPPv4N19bk_avrcp_rn_param_tUt2_12E "永久链接至目标")

    uint16_t uid_counter[](#_CPPv4N19bk_avrcp_rn_param_t11uid_counterE "永久链接至目标")
    :   response data for BK_AVRCP_RN_UIDS_CHANGE

    uint8_t system_status[](#_CPPv4N19bk_avrcp_rn_param_t13system_statusE "永久链接至目标")
    :   response data for BK_AVRCP_RN_SYSTEM_STATUS_CHANGE

    uint8_t player_app_set_count[](#_CPPv4N19bk_avrcp_rn_param_t20player_app_set_countE "永久链接至目标")

    uint8_t attr_id[](#_CPPv4N19bk_avrcp_rn_param_t7attr_idE "永久链接至目标")

    uint8_t value_id[](#_CPPv4N19bk_avrcp_rn_param_t8value_idE "永久链接至目标")

    struct [bk_avrcp_rn_param_t](#_CPPv419bk_avrcp_rn_param_t "bk_avrcp_rn_param_t")::[anonymous]::[anonymous] player_app_set_array[[BK_AVRCP_PS_MAX_ATTR](#_CPPv4N22bk_avrcp_ps_attr_ids_t20BK_AVRCP_PS_MAX_ATTRE "BK_AVRCP_PS_MAX_ATTR")][](#_CPPv4N19bk_avrcp_rn_param_t20player_app_set_arrayE "永久链接至目标")

    struct [bk_avrcp_rn_param_t](#_CPPv419bk_avrcp_rn_param_t "bk_avrcp_rn_param_t")::[anonymous] [anonymous][](#_CPPv4N19bk_avrcp_rn_param_tUt2_14E "永久链接至目标")

union bk_avrcp_ct_cb_param_t[](#_CPPv422bk_avrcp_ct_cb_param_t "永久链接至目标")
:   *#include <bk_dm_avrcp_types.h>*

    AVRCP controller callback parameters.

    Public Members

    struct [bk_avrcp_ct_cb_param_t](#_CPPv422bk_avrcp_ct_cb_param_t "bk_avrcp_ct_cb_param_t")::[avrcp_ct_conn_state_param](#_CPPv4N22bk_avrcp_ct_cb_param_t25avrcp_ct_conn_state_paramE "bk_avrcp_ct_cb_param_t::avrcp_ct_conn_state_param") conn_state[](#_CPPv4N22bk_avrcp_ct_cb_param_t10conn_stateE "永久链接至目标")
    :   AVRCP connection status

    struct [bk_avrcp_ct_cb_param_t](#_CPPv422bk_avrcp_ct_cb_param_t "bk_avrcp_ct_cb_param_t")::[avrcp_ct_psth_rsp_param](#_CPPv4N22bk_avrcp_ct_cb_param_t23avrcp_ct_psth_rsp_paramE "bk_avrcp_ct_cb_param_t::avrcp_ct_psth_rsp_param") psth_rsp[](#_CPPv4N22bk_avrcp_ct_cb_param_t8psth_rspE "永久链接至目标")
    :   passthrough command response

    struct [bk_avrcp_ct_cb_param_t](#_CPPv422bk_avrcp_ct_cb_param_t "bk_avrcp_ct_cb_param_t")::[avrcp_ct_change_notify_param](#_CPPv4N22bk_avrcp_ct_cb_param_t28avrcp_ct_change_notify_paramE "bk_avrcp_ct_cb_param_t::avrcp_ct_change_notify_param") change_ntf[](#_CPPv4N22bk_avrcp_ct_cb_param_t10change_ntfE "永久链接至目标")
    :   notifications

    struct [bk_avrcp_ct_cb_param_t](#_CPPv422bk_avrcp_ct_cb_param_t "bk_avrcp_ct_cb_param_t")::[avrcp_ct_get_rn_caps_rsp_param](#_CPPv4N22bk_avrcp_ct_cb_param_t30avrcp_ct_get_rn_caps_rsp_paramE "bk_avrcp_ct_cb_param_t::avrcp_ct_get_rn_caps_rsp_param") get_rn_caps_rsp[](#_CPPv4N22bk_avrcp_ct_cb_param_t15get_rn_caps_rspE "永久链接至目标")
    :   get supported event capabilities response from AVRCP target

    struct [bk_avrcp_ct_cb_param_t](#_CPPv422bk_avrcp_ct_cb_param_t "bk_avrcp_ct_cb_param_t")::[avrcp_ct_set_volume_rsp_param](#_CPPv4N22bk_avrcp_ct_cb_param_t29avrcp_ct_set_volume_rsp_paramE "bk_avrcp_ct_cb_param_t::avrcp_ct_set_volume_rsp_param") set_volume_rsp[](#_CPPv4N22bk_avrcp_ct_cb_param_t14set_volume_rspE "永久链接至目标")
    :   set absolute volume response event

    struct [bk_avrcp_ct_cb_param_t](#_CPPv422bk_avrcp_ct_cb_param_t "bk_avrcp_ct_cb_param_t")::[avrcp_ct_set_player_app_setting_rsp_param](#_CPPv4N22bk_avrcp_ct_cb_param_t41avrcp_ct_set_player_app_setting_rsp_paramE "bk_avrcp_ct_cb_param_t::avrcp_ct_set_player_app_setting_rsp_param") set_player_app_setting_rsp[](#_CPPv4N22bk_avrcp_ct_cb_param_t26set_player_app_setting_rspE "永久链接至目标")
    :   set player app setting response event

    struct [bk_avrcp_ct_cb_param_t](#_CPPv422bk_avrcp_ct_cb_param_t "bk_avrcp_ct_cb_param_t")::[avrcp_ct_elem_attr_rsp_param](#_CPPv4N22bk_avrcp_ct_cb_param_t28avrcp_ct_elem_attr_rsp_paramE "bk_avrcp_ct_cb_param_t::avrcp_ct_elem_attr_rsp_param") elem_attr_rsp[](#_CPPv4N22bk_avrcp_ct_cb_param_t13elem_attr_rspE "永久链接至目标")
    :   metadata attributes response

    struct avrcp_ct_change_notify_param[](#_CPPv4N22bk_avrcp_ct_cb_param_t28avrcp_ct_change_notify_paramE "永久链接至目标")
    :   *#include <bk_dm_avrcp_types.h>*

        BK_AVRCP_CT_CHANGE_NOTIFY_EVT.

        Public Members

        uint8_t event_id[](#_CPPv4N22bk_avrcp_ct_cb_param_t28avrcp_ct_change_notify_param8event_idE "永久链接至目标")
        :   id of AVRCP event notification

        [bk_avrcp_rn_param_t](#_CPPv419bk_avrcp_rn_param_t "bk_avrcp_rn_param_t") event_parameter[](#_CPPv4N22bk_avrcp_ct_cb_param_t28avrcp_ct_change_notify_param15event_parameterE "永久链接至目标")
        :   event notification parameter

        uint8_t remote_bda[6][](#_CPPv4N22bk_avrcp_ct_cb_param_t28avrcp_ct_change_notify_param10remote_bdaE "永久链接至目标")
        :   remote bluetooth device address

    struct avrcp_ct_conn_state_param[](#_CPPv4N22bk_avrcp_ct_cb_param_t25avrcp_ct_conn_state_paramE "永久链接至目标")
    :   *#include <bk_dm_avrcp_types.h>*

        BK_AVRCP_CT_CONNECTION_STATE_EVT.

        Public Members

        uint8_t connected[](#_CPPv4N22bk_avrcp_ct_cb_param_t25avrcp_ct_conn_state_param9connectedE "永久链接至目标")
        :   whether AVRCP connection is set up

        uint8_t remote_bda[6][](#_CPPv4N22bk_avrcp_ct_cb_param_t25avrcp_ct_conn_state_param10remote_bdaE "永久链接至目标")
        :   remote bluetooth device address

    struct avrcp_ct_elem_attr_rsp_param[](#_CPPv4N22bk_avrcp_ct_cb_param_t28avrcp_ct_elem_attr_rsp_paramE "永久链接至目标")
    :   *#include <bk_dm_avrcp_types.h>*

        BK_AVRCP_CT_GET_ELEM_ATTR_RSP_EVT.

        Public Members

        uint8_t status[](#_CPPv4N22bk_avrcp_ct_cb_param_t28avrcp_ct_elem_attr_rsp_param6statusE "永久链接至目标")

        uint8_t attr_count[](#_CPPv4N22bk_avrcp_ct_cb_param_t28avrcp_ct_elem_attr_rsp_param10attr_countE "永久链接至目标")
        :   0 means success

        uint32_t attr_id[](#_CPPv4N22bk_avrcp_ct_cb_param_t28avrcp_ct_elem_attr_rsp_param7attr_idE "永久链接至目标")
        :   elem attribute id, see bk_avrcp_media_attr_id_t

        uint16_t attr_text_charset[](#_CPPv4N22bk_avrcp_ct_cb_param_t28avrcp_ct_elem_attr_rsp_param17attr_text_charsetE "永久链接至目标")

        uint32_t attr_length[](#_CPPv4N22bk_avrcp_ct_cb_param_t28avrcp_ct_elem_attr_rsp_param11attr_lengthE "永久链接至目标")
        :   attr text charset, see [http://www.iana.org/assignments/character-sets](http://www.iana.org/assignments/character-sets "http://www.iana.org/assignments/character-sets")

            attribute character length

        uint8_t *attr_text[](#_CPPv4N22bk_avrcp_ct_cb_param_t28avrcp_ct_elem_attr_rsp_param9attr_textE "永久链接至目标")
        :   attribute itself

        struct [bk_avrcp_ct_cb_param_t](#_CPPv422bk_avrcp_ct_cb_param_t "bk_avrcp_ct_cb_param_t")::[avrcp_ct_elem_attr_rsp_param](#_CPPv4N22bk_avrcp_ct_cb_param_t28avrcp_ct_elem_attr_rsp_paramE "bk_avrcp_ct_cb_param_t::avrcp_ct_elem_attr_rsp_param")::[anonymous] *attr_array[](#_CPPv4N22bk_avrcp_ct_cb_param_t28avrcp_ct_elem_attr_rsp_param10attr_arrayE "永久链接至目标")
        :   attr_array count

        uint8_t remote_bda[6][](#_CPPv4N22bk_avrcp_ct_cb_param_t28avrcp_ct_elem_attr_rsp_param10remote_bdaE "永久链接至目标")
        :   elem array

            remote bluetooth device address

    struct avrcp_ct_get_rn_caps_rsp_param[](#_CPPv4N22bk_avrcp_ct_cb_param_t30avrcp_ct_get_rn_caps_rsp_paramE "永久链接至目标")
    :   *#include <bk_dm_avrcp_types.h>*

        BK_AVRCP_CT_GET_RN_CAPABILITIES_RSP_EVT.

        Public Members

        uint8_t cap_count[](#_CPPv4N22bk_avrcp_ct_cb_param_t30avrcp_ct_get_rn_caps_rsp_param9cap_countE "永久链接至目标")
        :   number of items provided in event or company_id according to cap_id used

        [bk_avrcp_rn_evt_cap_mask_t](#_CPPv426bk_avrcp_rn_evt_cap_mask_t "bk_avrcp_rn_evt_cap_mask_t") evt_set[](#_CPPv4N22bk_avrcp_ct_cb_param_t30avrcp_ct_get_rn_caps_rsp_param7evt_setE "永久链接至目标")
        :   supported event_ids represented in bit-mask

        uint8_t remote_bda[6][](#_CPPv4N22bk_avrcp_ct_cb_param_t30avrcp_ct_get_rn_caps_rsp_param10remote_bdaE "永久链接至目标")
        :   remote bluetooth device address

    struct avrcp_ct_psth_rsp_param[](#_CPPv4N22bk_avrcp_ct_cb_param_t23avrcp_ct_psth_rsp_paramE "永久链接至目标")
    :   *#include <bk_dm_avrcp_types.h>*

        BK_AVRCP_CT_PASSTHROUGH_RSP_EVT.

        Public Members

        uint8_t tl[](#_CPPv4N22bk_avrcp_ct_cb_param_t23avrcp_ct_psth_rsp_param2tlE "永久链接至目标")
        :   transaction label, 0 to 15

        uint8_t key_code[](#_CPPv4N22bk_avrcp_ct_cb_param_t23avrcp_ct_psth_rsp_param8key_codeE "永久链接至目标")
        :   passthrough command code, see bk_avrcp_pt_cmd_t

        uint8_t key_state[](#_CPPv4N22bk_avrcp_ct_cb_param_t23avrcp_ct_psth_rsp_param9key_stateE "永久链接至目标")
        :   0 for PRESSED, 1 for RELEASED

        [bk_avrcp_rsp_t](#_CPPv414bk_avrcp_rsp_t "bk_avrcp_rsp_t") rsp_code[](#_CPPv4N22bk_avrcp_ct_cb_param_t23avrcp_ct_psth_rsp_param8rsp_codeE "永久链接至目标")
        :   response code

        uint8_t remote_bda[6][](#_CPPv4N22bk_avrcp_ct_cb_param_t23avrcp_ct_psth_rsp_param10remote_bdaE "永久链接至目标")
        :   remote bluetooth device address

    struct avrcp_ct_set_player_app_setting_rsp_param[](#_CPPv4N22bk_avrcp_ct_cb_param_t41avrcp_ct_set_player_app_setting_rsp_paramE "永久链接至目标")
    :   *#include <bk_dm_avrcp_types.h>*

        BK_AVRCP_CT_SET_PLAYER_APP_SETTING_RSP_EVT.

        Public Members

        uint8_t status[](#_CPPv4N22bk_avrcp_ct_cb_param_t41avrcp_ct_set_player_app_setting_rsp_param6statusE "永久链接至目标")

        uint8_t remote_bda[6][](#_CPPv4N22bk_avrcp_ct_cb_param_t41avrcp_ct_set_player_app_setting_rsp_param10remote_bdaE "永久链接至目标")
        :   0 means success

            remote bluetooth device address

    struct avrcp_ct_set_volume_rsp_param[](#_CPPv4N22bk_avrcp_ct_cb_param_t29avrcp_ct_set_volume_rsp_paramE "永久链接至目标")
    :   *#include <bk_dm_avrcp_types.h>*

        BK_AVRCP_CT_SET_ABSOLUTE_VOLUME_RSP_EVT.

        Public Members

        uint8_t status[](#_CPPv4N22bk_avrcp_ct_cb_param_t29avrcp_ct_set_volume_rsp_param6statusE "永久链接至目标")

        uint8_t volume[](#_CPPv4N22bk_avrcp_ct_cb_param_t29avrcp_ct_set_volume_rsp_param6volumeE "永久链接至目标")
        :   0 means success

            the volume which has actually been set, range is 0 to 0x7f, means 0% to 100%

        uint8_t remote_bda[6][](#_CPPv4N22bk_avrcp_ct_cb_param_t29avrcp_ct_set_volume_rsp_param10remote_bdaE "永久链接至目标")
        :   remote bluetooth device address

union bk_avrcp_tg_cb_param_t[](#_CPPv422bk_avrcp_tg_cb_param_t "永久链接至目标")
:   *#include <bk_dm_avrcp_types.h>*

    AVRC target callback parameters.

    Public Members

    struct [bk_avrcp_tg_cb_param_t](#_CPPv422bk_avrcp_tg_cb_param_t "bk_avrcp_tg_cb_param_t")::[avrcp_tg_conn_stat_param](#_CPPv4N22bk_avrcp_tg_cb_param_t24avrcp_tg_conn_stat_paramE "bk_avrcp_tg_cb_param_t::avrcp_tg_conn_stat_param") conn_stat[](#_CPPv4N22bk_avrcp_tg_cb_param_t9conn_statE "永久链接至目标")
    :   AVRC connection status

    struct [bk_avrcp_tg_cb_param_t](#_CPPv422bk_avrcp_tg_cb_param_t "bk_avrcp_tg_cb_param_t")::[avrcp_tg_psth_cmd_param](#_CPPv4N22bk_avrcp_tg_cb_param_t23avrcp_tg_psth_cmd_paramE "bk_avrcp_tg_cb_param_t::avrcp_tg_psth_cmd_param") psth_cmd[](#_CPPv4N22bk_avrcp_tg_cb_param_t8psth_cmdE "永久链接至目标")
    :   passthrough command

    struct [bk_avrcp_tg_cb_param_t](#_CPPv422bk_avrcp_tg_cb_param_t "bk_avrcp_tg_cb_param_t")::[avrcp_tg_set_abs_vol_param](#_CPPv4N22bk_avrcp_tg_cb_param_t26avrcp_tg_set_abs_vol_paramE "bk_avrcp_tg_cb_param_t::avrcp_tg_set_abs_vol_param") set_abs_vol[](#_CPPv4N22bk_avrcp_tg_cb_param_t11set_abs_volE "永久链接至目标")
    :   set absolute volume command targeted on audio sink

    struct [bk_avrcp_tg_cb_param_t](#_CPPv422bk_avrcp_tg_cb_param_t "bk_avrcp_tg_cb_param_t")::[avrcp_tg_reg_ntf_param](#_CPPv4N22bk_avrcp_tg_cb_param_t22avrcp_tg_reg_ntf_paramE "bk_avrcp_tg_cb_param_t::avrcp_tg_reg_ntf_param") reg_ntf[](#_CPPv4N22bk_avrcp_tg_cb_param_t7reg_ntfE "永久链接至目标")
    :   register notification

    struct avrcp_tg_conn_stat_param[](#_CPPv4N22bk_avrcp_tg_cb_param_t24avrcp_tg_conn_stat_paramE "永久链接至目标")
    :   *#include <bk_dm_avrcp_types.h>*

        BK_AVRCP_TG_CONNECTION_STATE_EVT.

        Public Members

        bool connected[](#_CPPv4N22bk_avrcp_tg_cb_param_t24avrcp_tg_conn_stat_param9connectedE "永久链接至目标")
        :   whether AVRC connection is set up

        uint8_t remote_bda[6][](#_CPPv4N22bk_avrcp_tg_cb_param_t24avrcp_tg_conn_stat_param10remote_bdaE "永久链接至目标")
        :   remote bluetooth device address

    struct avrcp_tg_psth_cmd_param[](#_CPPv4N22bk_avrcp_tg_cb_param_t23avrcp_tg_psth_cmd_paramE "永久链接至目标")
    :   *#include <bk_dm_avrcp_types.h>*

        BK_AVRCP_TG_PASSTHROUGH_CMD_EVT.

        Public Members

        uint8_t key_code[](#_CPPv4N22bk_avrcp_tg_cb_param_t23avrcp_tg_psth_cmd_param8key_codeE "永久链接至目标")
        :   passthrough command code

        uint8_t key_state[](#_CPPv4N22bk_avrcp_tg_cb_param_t23avrcp_tg_psth_cmd_param9key_stateE "永久链接至目标")
        :   0 for PRESSED, 1 for RELEASED

        uint8_t remote_bda[6][](#_CPPv4N22bk_avrcp_tg_cb_param_t23avrcp_tg_psth_cmd_param10remote_bdaE "永久链接至目标")
        :   remote bluetooth device address

    struct avrcp_tg_reg_ntf_param[](#_CPPv4N22bk_avrcp_tg_cb_param_t22avrcp_tg_reg_ntf_paramE "永久链接至目标")
    :   *#include <bk_dm_avrcp_types.h>*

        BK_AVRCP_TG_REGISTER_NOTIFICATION_EVT.

        Public Members

        uint8_t event_id[](#_CPPv4N22bk_avrcp_tg_cb_param_t22avrcp_tg_reg_ntf_param8event_idE "永久链接至目标")
        :   event id of bk_avrcp_rn_event_ids_t

        uint32_t event_parameter[](#_CPPv4N22bk_avrcp_tg_cb_param_t22avrcp_tg_reg_ntf_param15event_parameterE "永久链接至目标")
        :   event notification parameter, used with BK_AVRCP_RN_PLAY_POS_CHANGED only now, means timer in second

        uint8_t remote_bda[6][](#_CPPv4N22bk_avrcp_tg_cb_param_t22avrcp_tg_reg_ntf_param10remote_bdaE "永久链接至目标")
        :   remote bluetooth device address

    struct avrcp_tg_set_abs_vol_param[](#_CPPv4N22bk_avrcp_tg_cb_param_t26avrcp_tg_set_abs_vol_paramE "永久链接至目标")
    :   *#include <bk_dm_avrcp_types.h>*

        BK_AVRCP_TG_SET_ABSOLUTE_VOLUME_CMD_EVT.

        Public Members

        uint8_t volume[](#_CPPv4N22bk_avrcp_tg_cb_param_t26avrcp_tg_set_abs_vol_param6volumeE "永久链接至目标")
        :   volume ranges from 0 to 127

        uint8_t remote_bda[6][](#_CPPv4N22bk_avrcp_tg_cb_param_t26avrcp_tg_set_abs_vol_param10remote_bdaE "永久链接至目标")
        :   remote bluetooth device address


### Structures[](#id35 "永久链接至标题")

struct bk_avrcp_rn_evt_cap_mask_t[](#_CPPv426bk_avrcp_rn_evt_cap_mask_t "永久链接至目标")
:   AVRCP target notification event capability bit mask.

    Public Members

    uint16_t bits[](#_CPPv4N26bk_avrcp_rn_evt_cap_mask_t4bitsE "永久链接至目标")
    :   bit mask representation of supported event_ids

struct bk_avrcp_psth_bit_mask_t[](#_CPPv424bk_avrcp_psth_bit_mask_t "永久链接至目标")
:   AVRC passthrough command bit mask.

    Public Members

    uint16_t bits[8][](#_CPPv4N24bk_avrcp_psth_bit_mask_t4bitsE "永久链接至目标")
    :   bit mask representation of PASSTHROUGH commands


### Type Definitions[](#id36 "永久链接至标题")

typedef void (*bk_avrcp_ct_cb_t)([bk_avrcp_ct_cb_event_t](#_CPPv422bk_avrcp_ct_cb_event_t "bk_avrcp_ct_cb_event_t") event, [bk_avrcp_ct_cb_param_t](#_CPPv422bk_avrcp_ct_cb_param_t "bk_avrcp_ct_cb_param_t") *param)[](#_CPPv416bk_avrcp_ct_cb_t "永久链接至目标")
:   AVRCP controller callback function type.

    Param event
    :   : Event type

    Param param
    :   : Pointer to callback parameter union

typedef void (*bk_avrcp_tg_cb_t)([bk_avrcp_tg_cb_event_t](#_CPPv422bk_avrcp_tg_cb_event_t "bk_avrcp_tg_cb_event_t") event, [bk_avrcp_tg_cb_param_t](#_CPPv422bk_avrcp_tg_cb_param_t "bk_avrcp_tg_cb_param_t") *param)[](#_CPPv416bk_avrcp_tg_cb_t "永久链接至目标")
:   AVRCP target callback function type.

    Param event
    :   : Event type

    Param param
    :   : Pointer to callback parameter union


### Enumerations[](#id37 "永久链接至标题")

enum bk_avrcp_rn_event_ids_t[](#_CPPv423bk_avrcp_rn_event_ids_t "永久链接至目标")
:   AVRCP event notification ids.


    *Values:*

    enumerator BK_AVRCP_RN_PLAY_STATUS_CHANGE[](#_CPPv4N23bk_avrcp_rn_event_ids_t30BK_AVRCP_RN_PLAY_STATUS_CHANGEE "永久链接至目标")
    :   track status change, eg. from playing to paused

    enumerator BK_AVRCP_RN_TRACK_CHANGE[](#_CPPv4N23bk_avrcp_rn_event_ids_t24BK_AVRCP_RN_TRACK_CHANGEE "永久链接至目标")
    :   new track is loaded

    enumerator BK_AVRCP_RN_TRACK_REACHED_END[](#_CPPv4N23bk_avrcp_rn_event_ids_t29BK_AVRCP_RN_TRACK_REACHED_ENDE "永久链接至目标")
    :   current track reached end

    enumerator BK_AVRCP_RN_TRACK_REACHED_START[](#_CPPv4N23bk_avrcp_rn_event_ids_t31BK_AVRCP_RN_TRACK_REACHED_STARTE "永久链接至目标")
    :   current track reached start position

    enumerator BK_AVRCP_RN_PLAY_POS_CHANGED[](#_CPPv4N23bk_avrcp_rn_event_ids_t28BK_AVRCP_RN_PLAY_POS_CHANGEDE "永久链接至目标")
    :   track playing position changed

    enumerator BK_AVRCP_RN_BATTERY_STATUS_CHANGE[](#_CPPv4N23bk_avrcp_rn_event_ids_t33BK_AVRCP_RN_BATTERY_STATUS_CHANGEE "永久链接至目标")
    :   battery status changed

    enumerator BK_AVRCP_RN_SYSTEM_STATUS_CHANGE[](#_CPPv4N23bk_avrcp_rn_event_ids_t32BK_AVRCP_RN_SYSTEM_STATUS_CHANGEE "永久链接至目标")
    :   system status changed

    enumerator BK_AVRCP_RN_APP_SETTING_CHANGE[](#_CPPv4N23bk_avrcp_rn_event_ids_t30BK_AVRCP_RN_APP_SETTING_CHANGEE "永久链接至目标")
    :   application settings changed

    enumerator BK_AVRCP_RN_NOW_PLAYING_CHANGE[](#_CPPv4N23bk_avrcp_rn_event_ids_t30BK_AVRCP_RN_NOW_PLAYING_CHANGEE "永久链接至目标")
    :   now playing content changed

    enumerator BK_AVRCP_RN_AVAILABLE_PLAYERS_CHANGE[](#_CPPv4N23bk_avrcp_rn_event_ids_t36BK_AVRCP_RN_AVAILABLE_PLAYERS_CHANGEE "永久链接至目标")
    :   available players changed

    enumerator BK_AVRCP_RN_ADDRESSED_PLAYER_CHANGE[](#_CPPv4N23bk_avrcp_rn_event_ids_t35BK_AVRCP_RN_ADDRESSED_PLAYER_CHANGEE "永久链接至目标")
    :   the addressed player changed

    enumerator BK_AVRCP_RN_UIDS_CHANGE[](#_CPPv4N23bk_avrcp_rn_event_ids_t23BK_AVRCP_RN_UIDS_CHANGEE "永久链接至目标")
    :   UIDs changed

    enumerator BK_AVRCP_RN_VOLUME_CHANGE[](#_CPPv4N23bk_avrcp_rn_event_ids_t25BK_AVRCP_RN_VOLUME_CHANGEE "永久链接至目标")
    :   volume changed locally on TG

    enumerator BK_AVRCP_RN_MAX_EVT[](#_CPPv4N23bk_avrcp_rn_event_ids_t19BK_AVRCP_RN_MAX_EVTE "永久链接至目标")

enum bk_avrcp_ct_cb_event_t[](#_CPPv422bk_avrcp_ct_cb_event_t "永久链接至目标")
:   AVRCP Controller callback events.


    *Values:*

    enumerator BK_AVRCP_CT_CONNECTION_STATE_EVT[](#_CPPv4N22bk_avrcp_ct_cb_event_t32BK_AVRCP_CT_CONNECTION_STATE_EVTE "永久链接至目标")
    :   connection state changed event

    enumerator BK_AVRCP_CT_PASSTHROUGH_RSP_EVT[](#_CPPv4N22bk_avrcp_ct_cb_event_t31BK_AVRCP_CT_PASSTHROUGH_RSP_EVTE "永久链接至目标")
    :   passthrough response event

    enumerator BK_AVRCP_CT_GET_ELEM_ATTR_RSP_EVT[](#_CPPv4N22bk_avrcp_ct_cb_event_t33BK_AVRCP_CT_GET_ELEM_ATTR_RSP_EVTE "永久链接至目标")
    :   get elem attr response event

    enumerator BK_AVRCP_CT_PLAY_STATUS_RSP_EVT[](#_CPPv4N22bk_avrcp_ct_cb_event_t31BK_AVRCP_CT_PLAY_STATUS_RSP_EVTE "永久链接至目标")
    :   play status response event

    enumerator BK_AVRCP_CT_CHANGE_NOTIFY_EVT[](#_CPPv4N22bk_avrcp_ct_cb_event_t29BK_AVRCP_CT_CHANGE_NOTIFY_EVTE "永久链接至目标")
    :   notification event

    enumerator BK_AVRCP_CT_REMOTE_FEATURES_EVT[](#_CPPv4N22bk_avrcp_ct_cb_event_t31BK_AVRCP_CT_REMOTE_FEATURES_EVTE "永久链接至目标")
    :   feature of remote device indication event

    enumerator BK_AVRCP_CT_GET_RN_CAPABILITIES_RSP_EVT[](#_CPPv4N22bk_avrcp_ct_cb_event_t39BK_AVRCP_CT_GET_RN_CAPABILITIES_RSP_EVTE "永久链接至目标")
    :   supported notification events capability of peer device

    enumerator BK_AVRCP_CT_SET_ABSOLUTE_VOLUME_RSP_EVT[](#_CPPv4N22bk_avrcp_ct_cb_event_t39BK_AVRCP_CT_SET_ABSOLUTE_VOLUME_RSP_EVTE "永久链接至目标")
    :   set absolute volume response event

    enumerator BK_AVRCP_CT_SET_PLAYER_APP_SETTING_RSP_EVT[](#_CPPv4N22bk_avrcp_ct_cb_event_t42BK_AVRCP_CT_SET_PLAYER_APP_SETTING_RSP_EVTE "永久链接至目标")

enum bk_avrcp_rsp_t[](#_CPPv414bk_avrcp_rsp_t "永久链接至目标")
:   AVCTP response codes.


    *Values:*

    enumerator BK_AVRCP_RSP_NOT_IMPL[](#_CPPv4N14bk_avrcp_rsp_t21BK_AVRCP_RSP_NOT_IMPLE "永久链接至目标")
    :   not implemented

    enumerator BK_AVRCP_RSP_ACCEPT[](#_CPPv4N14bk_avrcp_rsp_t19BK_AVRCP_RSP_ACCEPTE "永久链接至目标")
    :   accept

    enumerator BK_AVRCP_RSP_REJECT[](#_CPPv4N14bk_avrcp_rsp_t19BK_AVRCP_RSP_REJECTE "永久链接至目标")
    :   reject

    enumerator BK_AVRCP_RSP_IN_TRANS[](#_CPPv4N14bk_avrcp_rsp_t21BK_AVRCP_RSP_IN_TRANSE "永久链接至目标")
    :   in transition

    enumerator BK_AVRCP_RSP_IMPL_STBL[](#_CPPv4N14bk_avrcp_rsp_t22BK_AVRCP_RSP_IMPL_STBLE "永久链接至目标")
    :   implemented/stable

    enumerator BK_AVRCP_RSP_CHANGED[](#_CPPv4N14bk_avrcp_rsp_t20BK_AVRCP_RSP_CHANGEDE "永久链接至目标")
    :   changed

    enumerator BK_AVRCP_RSP_INTERIM[](#_CPPv4N14bk_avrcp_rsp_t20BK_AVRCP_RSP_INTERIME "永久链接至目标")
    :   interim

enum bk_avrcp_batt_stat_t[](#_CPPv420bk_avrcp_batt_stat_t "永久链接至目标")
:   AVRCP battery status.


    *Values:*

    enumerator BK_AVRCP_BATT_NORMAL[](#_CPPv4N20bk_avrcp_batt_stat_t20BK_AVRCP_BATT_NORMALE "永久链接至目标")
    :   normal state

    enumerator BK_AVRCP_BATT_WARNING[](#_CPPv4N20bk_avrcp_batt_stat_t21BK_AVRCP_BATT_WARNINGE "永久链接至目标")
    :   unable to operate soon

    enumerator BK_AVRCP_BATT_CRITICAL[](#_CPPv4N20bk_avrcp_batt_stat_t22BK_AVRCP_BATT_CRITICALE "永久链接至目标")
    :   cannot operate any more

    enumerator BK_AVRCP_BATT_EXTERNAL[](#_CPPv4N20bk_avrcp_batt_stat_t22BK_AVRCP_BATT_EXTERNALE "永久链接至目标")
    :   plugged to external power supply

    enumerator BK_AVRCP_BATT_FULL_CHARGE[](#_CPPv4N20bk_avrcp_batt_stat_t25BK_AVRCP_BATT_FULL_CHARGEE "永久链接至目标")
    :   when completely charged from external power supply

enum bk_avrcp_playback_stat_t[](#_CPPv424bk_avrcp_playback_stat_t "永久链接至目标")
:   AVRCP current status of playback.


    *Values:*

    enumerator BK_AVRCP_PLAYBACK_STOPPED[](#_CPPv4N24bk_avrcp_playback_stat_t25BK_AVRCP_PLAYBACK_STOPPEDE "永久链接至目标")
    :   stopped

    enumerator BK_AVRCP_PLAYBACK_PLAYING[](#_CPPv4N24bk_avrcp_playback_stat_t25BK_AVRCP_PLAYBACK_PLAYINGE "永久链接至目标")
    :   playing

    enumerator BK_AVRCP_PLAYBACK_PAUSED[](#_CPPv4N24bk_avrcp_playback_stat_t24BK_AVRCP_PLAYBACK_PAUSEDE "永久链接至目标")
    :   paused

    enumerator BK_AVRCP_PLAYBACK_FWD_SEEK[](#_CPPv4N24bk_avrcp_playback_stat_t26BK_AVRCP_PLAYBACK_FWD_SEEKE "永久链接至目标")
    :   forward seek

    enumerator BK_AVRCP_PLAYBACK_REV_SEEK[](#_CPPv4N24bk_avrcp_playback_stat_t26BK_AVRCP_PLAYBACK_REV_SEEKE "永久链接至目标")
    :   reverse seek

    enumerator BK_AVRCP_PLAYBACK_ERROR[](#_CPPv4N24bk_avrcp_playback_stat_t23BK_AVRCP_PLAYBACK_ERRORE "永久链接至目标")
    :   error

enum bk_avrcp_pt_cmd_t[](#_CPPv417bk_avrcp_pt_cmd_t "永久链接至目标")
:   AVRCP passthrough command code.


    *Values:*

    enumerator BK_AVRCP_PT_CMD_SELECT[](#_CPPv4N17bk_avrcp_pt_cmd_t22BK_AVRCP_PT_CMD_SELECTE "永久链接至目标")
    :   select

    enumerator BK_AVRCP_PT_CMD_UP[](#_CPPv4N17bk_avrcp_pt_cmd_t18BK_AVRCP_PT_CMD_UPE "永久链接至目标")
    :   up

    enumerator BK_AVRCP_PT_CMD_DOWN[](#_CPPv4N17bk_avrcp_pt_cmd_t20BK_AVRCP_PT_CMD_DOWNE "永久链接至目标")
    :   down

    enumerator BK_AVRCP_PT_CMD_LEFT[](#_CPPv4N17bk_avrcp_pt_cmd_t20BK_AVRCP_PT_CMD_LEFTE "永久链接至目标")
    :   left

    enumerator BK_AVRCP_PT_CMD_RIGHT[](#_CPPv4N17bk_avrcp_pt_cmd_t21BK_AVRCP_PT_CMD_RIGHTE "永久链接至目标")
    :   right

    enumerator BK_AVRCP_PT_CMD_RIGHT_UP[](#_CPPv4N17bk_avrcp_pt_cmd_t24BK_AVRCP_PT_CMD_RIGHT_UPE "永久链接至目标")
    :   right-up

    enumerator BK_AVRCP_PT_CMD_RIGHT_DOWN[](#_CPPv4N17bk_avrcp_pt_cmd_t26BK_AVRCP_PT_CMD_RIGHT_DOWNE "永久链接至目标")
    :   right-down

    enumerator BK_AVRCP_PT_CMD_LEFT_UP[](#_CPPv4N17bk_avrcp_pt_cmd_t23BK_AVRCP_PT_CMD_LEFT_UPE "永久链接至目标")
    :   left-up

    enumerator BK_AVRCP_PT_CMD_LEFT_DOWN[](#_CPPv4N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_LEFT_DOWNE "永久链接至目标")
    :   left-down

    enumerator BK_AVRCP_PT_CMD_ROOT_MENU[](#_CPPv4N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_ROOT_MENUE "永久链接至目标")
    :   root menu

    enumerator BK_AVRCP_PT_CMD_SETUP_MENU[](#_CPPv4N17bk_avrcp_pt_cmd_t26BK_AVRCP_PT_CMD_SETUP_MENUE "永久链接至目标")
    :   setup menu

    enumerator BK_AVRCP_PT_CMD_CONT_MENU[](#_CPPv4N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_CONT_MENUE "永久链接至目标")
    :   contents menu

    enumerator BK_AVRCP_PT_CMD_FAV_MENU[](#_CPPv4N17bk_avrcp_pt_cmd_t24BK_AVRCP_PT_CMD_FAV_MENUE "永久链接至目标")
    :   favorite menu

    enumerator BK_AVRCP_PT_CMD_EXIT[](#_CPPv4N17bk_avrcp_pt_cmd_t20BK_AVRCP_PT_CMD_EXITE "永久链接至目标")
    :   exit

    enumerator BK_AVRCP_PT_CMD_0[](#_CPPv4N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_0E "永久链接至目标")
    :   0

    enumerator BK_AVRCP_PT_CMD_1[](#_CPPv4N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_1E "永久链接至目标")
    :   1

    enumerator BK_AVRCP_PT_CMD_2[](#_CPPv4N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_2E "永久链接至目标")
    :   2

    enumerator BK_AVRCP_PT_CMD_3[](#_CPPv4N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_3E "永久链接至目标")
    :   3

    enumerator BK_AVRCP_PT_CMD_4[](#_CPPv4N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_4E "永久链接至目标")
    :   4

    enumerator BK_AVRCP_PT_CMD_5[](#_CPPv4N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_5E "永久链接至目标")
    :   5

    enumerator BK_AVRCP_PT_CMD_6[](#_CPPv4N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_6E "永久链接至目标")
    :   6

    enumerator BK_AVRCP_PT_CMD_7[](#_CPPv4N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_7E "永久链接至目标")
    :   7

    enumerator BK_AVRCP_PT_CMD_8[](#_CPPv4N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_8E "永久链接至目标")
    :   8

    enumerator BK_AVRCP_PT_CMD_9[](#_CPPv4N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_9E "永久链接至目标")
    :   9

    enumerator BK_AVRCP_PT_CMD_DOT[](#_CPPv4N17bk_avrcp_pt_cmd_t19BK_AVRCP_PT_CMD_DOTE "永久链接至目标")
    :   dot

    enumerator BK_AVRCP_PT_CMD_ENTER[](#_CPPv4N17bk_avrcp_pt_cmd_t21BK_AVRCP_PT_CMD_ENTERE "永久链接至目标")
    :   enter

    enumerator BK_AVRCP_PT_CMD_CLEAR[](#_CPPv4N17bk_avrcp_pt_cmd_t21BK_AVRCP_PT_CMD_CLEARE "永久链接至目标")
    :   clear

    enumerator BK_AVRCP_PT_CMD_CHAN_UP[](#_CPPv4N17bk_avrcp_pt_cmd_t23BK_AVRCP_PT_CMD_CHAN_UPE "永久链接至目标")
    :   channel up

    enumerator BK_AVRCP_PT_CMD_CHAN_DOWN[](#_CPPv4N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_CHAN_DOWNE "永久链接至目标")
    :   channel down

    enumerator BK_AVRCP_PT_CMD_PREV_CHAN[](#_CPPv4N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_PREV_CHANE "永久链接至目标")
    :   previous channel

    enumerator BK_AVRCP_PT_CMD_SOUND_SEL[](#_CPPv4N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_SOUND_SELE "永久链接至目标")
    :   sound select

    enumerator BK_AVRCP_PT_CMD_INPUT_SEL[](#_CPPv4N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_INPUT_SELE "永久链接至目标")
    :   input select

    enumerator BK_AVRCP_PT_CMD_DISP_INFO[](#_CPPv4N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_DISP_INFOE "永久链接至目标")
    :   display information

    enumerator BK_AVRCP_PT_CMD_HELP[](#_CPPv4N17bk_avrcp_pt_cmd_t20BK_AVRCP_PT_CMD_HELPE "永久链接至目标")
    :   help

    enumerator BK_AVRCP_PT_CMD_PAGE_UP[](#_CPPv4N17bk_avrcp_pt_cmd_t23BK_AVRCP_PT_CMD_PAGE_UPE "永久链接至目标")
    :   page up

    enumerator BK_AVRCP_PT_CMD_PAGE_DOWN[](#_CPPv4N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_PAGE_DOWNE "永久链接至目标")
    :   page down

    enumerator BK_AVRCP_PT_CMD_POWER[](#_CPPv4N17bk_avrcp_pt_cmd_t21BK_AVRCP_PT_CMD_POWERE "永久链接至目标")
    :   power

    enumerator BK_AVRCP_PT_CMD_VOL_UP[](#_CPPv4N17bk_avrcp_pt_cmd_t22BK_AVRCP_PT_CMD_VOL_UPE "永久链接至目标")
    :   volume up

    enumerator BK_AVRCP_PT_CMD_VOL_DOWN[](#_CPPv4N17bk_avrcp_pt_cmd_t24BK_AVRCP_PT_CMD_VOL_DOWNE "永久链接至目标")
    :   volume down

    enumerator BK_AVRCP_PT_CMD_MUTE[](#_CPPv4N17bk_avrcp_pt_cmd_t20BK_AVRCP_PT_CMD_MUTEE "永久链接至目标")
    :   mute

    enumerator BK_AVRCP_PT_CMD_PLAY[](#_CPPv4N17bk_avrcp_pt_cmd_t20BK_AVRCP_PT_CMD_PLAYE "永久链接至目标")
    :   play

    enumerator BK_AVRCP_PT_CMD_STOP[](#_CPPv4N17bk_avrcp_pt_cmd_t20BK_AVRCP_PT_CMD_STOPE "永久链接至目标")
    :   stop

    enumerator BK_AVRCP_PT_CMD_PAUSE[](#_CPPv4N17bk_avrcp_pt_cmd_t21BK_AVRCP_PT_CMD_PAUSEE "永久链接至目标")
    :   pause

    enumerator BK_AVRCP_PT_CMD_RECORD[](#_CPPv4N17bk_avrcp_pt_cmd_t22BK_AVRCP_PT_CMD_RECORDE "永久链接至目标")
    :   record

    enumerator BK_AVRCP_PT_CMD_REWIND[](#_CPPv4N17bk_avrcp_pt_cmd_t22BK_AVRCP_PT_CMD_REWINDE "永久链接至目标")
    :   rewind

    enumerator BK_AVRCP_PT_CMD_FAST_FORWARD[](#_CPPv4N17bk_avrcp_pt_cmd_t28BK_AVRCP_PT_CMD_FAST_FORWARDE "永久链接至目标")
    :   fast forward

    enumerator BK_AVRCP_PT_CMD_EJECT[](#_CPPv4N17bk_avrcp_pt_cmd_t21BK_AVRCP_PT_CMD_EJECTE "永久链接至目标")
    :   eject

    enumerator BK_AVRCP_PT_CMD_FORWARD[](#_CPPv4N17bk_avrcp_pt_cmd_t23BK_AVRCP_PT_CMD_FORWARDE "永久链接至目标")
    :   forward

    enumerator BK_AVRCP_PT_CMD_BACKWARD[](#_CPPv4N17bk_avrcp_pt_cmd_t24BK_AVRCP_PT_CMD_BACKWARDE "永久链接至目标")
    :   backward

    enumerator BK_AVRCP_PT_CMD_ANGLE[](#_CPPv4N17bk_avrcp_pt_cmd_t21BK_AVRCP_PT_CMD_ANGLEE "永久链接至目标")
    :   angle

    enumerator BK_AVRCP_PT_CMD_SUBPICT[](#_CPPv4N17bk_avrcp_pt_cmd_t23BK_AVRCP_PT_CMD_SUBPICTE "永久链接至目标")
    :   subpicture

    enumerator BK_AVRCP_PT_CMD_F1[](#_CPPv4N17bk_avrcp_pt_cmd_t18BK_AVRCP_PT_CMD_F1E "永久链接至目标")
    :   F1

    enumerator BK_AVRCP_PT_CMD_F2[](#_CPPv4N17bk_avrcp_pt_cmd_t18BK_AVRCP_PT_CMD_F2E "永久链接至目标")
    :   F2

    enumerator BK_AVRCP_PT_CMD_F3[](#_CPPv4N17bk_avrcp_pt_cmd_t18BK_AVRCP_PT_CMD_F3E "永久链接至目标")
    :   F3

    enumerator BK_AVRCP_PT_CMD_F4[](#_CPPv4N17bk_avrcp_pt_cmd_t18BK_AVRCP_PT_CMD_F4E "永久链接至目标")
    :   F4

    enumerator BK_AVRCP_PT_CMD_F5[](#_CPPv4N17bk_avrcp_pt_cmd_t18BK_AVRCP_PT_CMD_F5E "永久链接至目标")
    :   F5

    enumerator BK_AVRCP_PT_CMD_VENDOR[](#_CPPv4N17bk_avrcp_pt_cmd_t22BK_AVRCP_PT_CMD_VENDORE "永久链接至目标")
    :   vendor unique

enum bk_avrcp_pt_cmd_state_t[](#_CPPv423bk_avrcp_pt_cmd_state_t "永久链接至目标")
:   AVRCP passthrough command state.


    *Values:*

    enumerator BK_AVRCP_PT_CMD_STATE_PRESSED[](#_CPPv4N23bk_avrcp_pt_cmd_state_t29BK_AVRCP_PT_CMD_STATE_PRESSEDE "永久链接至目标")
    :   key pressed

    enumerator BK_AVRCP_PT_CMD_STATE_RELEASED[](#_CPPv4N23bk_avrcp_pt_cmd_state_t30BK_AVRCP_PT_CMD_STATE_RELEASEDE "永久链接至目标")
    :   key released

enum bk_avrcp_media_attr_id_t[](#_CPPv424bk_avrcp_media_attr_id_t "永久链接至目标")
:   AVRC media attribute id.


    *Values:*

    enumerator BK_AVRCP_MEDIA_ATTR_ID_TITLE[](#_CPPv4N24bk_avrcp_media_attr_id_t28BK_AVRCP_MEDIA_ATTR_ID_TITLEE "永久链接至目标")
    :   title of the playing track

    enumerator BK_AVRCP_MEDIA_ATTR_ID_ARTIST[](#_CPPv4N24bk_avrcp_media_attr_id_t29BK_AVRCP_MEDIA_ATTR_ID_ARTISTE "永久链接至目标")
    :   track artist

    enumerator BK_AVRCP_MEDIA_ATTR_ID_ALBUM[](#_CPPv4N24bk_avrcp_media_attr_id_t28BK_AVRCP_MEDIA_ATTR_ID_ALBUME "永久链接至目标")
    :   album name

    enumerator BK_AVRCP_MEDIA_ATTR_ID_TRACK_NUM[](#_CPPv4N24bk_avrcp_media_attr_id_t32BK_AVRCP_MEDIA_ATTR_ID_TRACK_NUME "永久链接至目标")
    :   track position on the album

    enumerator BK_AVRCP_MEDIA_ATTR_ID_NUM_TRACKS[](#_CPPv4N24bk_avrcp_media_attr_id_t33BK_AVRCP_MEDIA_ATTR_ID_NUM_TRACKSE "永久链接至目标")
    :   number of tracks on the album

    enumerator BK_AVRCP_MEDIA_ATTR_ID_GENRE[](#_CPPv4N24bk_avrcp_media_attr_id_t28BK_AVRCP_MEDIA_ATTR_ID_GENREE "永久链接至目标")
    :   track genre

    enumerator BK_AVRCP_MEDIA_ATTR_ID_PLAYING_TIME[](#_CPPv4N24bk_avrcp_media_attr_id_t35BK_AVRCP_MEDIA_ATTR_ID_PLAYING_TIMEE "永久链接至目标")
    :   total album playing time in miliseconds

    enumerator BK_AVRCP_MEDIA_ATTR_ID_DEFAULT_COVER_ART[](#_CPPv4N24bk_avrcp_media_attr_id_t40BK_AVRCP_MEDIA_ATTR_ID_DEFAULT_COVER_ARTE "永久链接至目标")

enum bk_avrcp_ps_attr_ids_t[](#_CPPv422bk_avrcp_ps_attr_ids_t "永久链接至目标")
:   AVRC player setting ids.


    *Values:*

    enumerator BK_AVRCP_PS_EQUALIZER[](#_CPPv4N22bk_avrcp_ps_attr_ids_t21BK_AVRCP_PS_EQUALIZERE "永久链接至目标")
    :   equalizer, on or off

    enumerator BK_AVRCP_PS_REPEAT_MODE[](#_CPPv4N22bk_avrcp_ps_attr_ids_t23BK_AVRCP_PS_REPEAT_MODEE "永久链接至目标")
    :   repeat mode

    enumerator BK_AVRCP_PS_SHUFFLE_MODE[](#_CPPv4N22bk_avrcp_ps_attr_ids_t24BK_AVRCP_PS_SHUFFLE_MODEE "永久链接至目标")
    :   shuffle mode

    enumerator BK_AVRCP_PS_SCAN_MODE[](#_CPPv4N22bk_avrcp_ps_attr_ids_t21BK_AVRCP_PS_SCAN_MODEE "永久链接至目标")
    :   scan mode on or off

    enumerator BK_AVRCP_PS_MAX_ATTR[](#_CPPv4N22bk_avrcp_ps_attr_ids_t20BK_AVRCP_PS_MAX_ATTRE "永久链接至目标")

enum bk_avrcp_rn_rsp_t[](#_CPPv417bk_avrcp_rn_rsp_t "永久链接至目标")
:   AVRC notification response type.


    *Values:*

    enumerator BK_AVRCP_RN_RSP_INTERIM[](#_CPPv4N17bk_avrcp_rn_rsp_t23BK_AVRCP_RN_RSP_INTERIME "永久链接至目标")
    :   initial response to RegisterNotification, should be sent T_mtp(1000ms) from receiving the command

    enumerator BK_AVRCP_RN_RSP_CHANGED[](#_CPPv4N17bk_avrcp_rn_rsp_t23BK_AVRCP_RN_RSP_CHANGEDE "永久链接至目标")
    :   final response to RegisterNotification command

enum bk_avrcp_rn_cap_api_method_t[](#_CPPv428bk_avrcp_rn_cap_api_method_t "永久链接至目标")
:   AVRC target notification event notification capability.


    *Values:*

    enumerator BK_AVRCP_RN_CAP_API_METHOD_ALLOWED[](#_CPPv4N28bk_avrcp_rn_cap_api_method_t34BK_AVRCP_RN_CAP_API_METHOD_ALLOWEDE "永久链接至目标")
    :   all of the notification events that can possibly be supported, immutable

    enumerator BK_AVRCP_RN_CAP_API_METHOD_CURRENT_ENABLE[](#_CPPv4N28bk_avrcp_rn_cap_api_method_t41BK_AVRCP_RN_CAP_API_METHOD_CURRENT_ENABLEE "永久链接至目标")
    :   notification events selectively supported according to the current configuration

    enumerator BK_AVRCP_RN_CAP_API_METHOD_MAX[](#_CPPv4N28bk_avrcp_rn_cap_api_method_t30BK_AVRCP_RN_CAP_API_METHOD_MAXE "永久链接至目标")

enum bk_avrcp_psth_filter_t[](#_CPPv422bk_avrcp_psth_filter_t "永久链接至目标")
:   AVRC passthrough command filter.


    *Values:*

    enumerator BK_AVRCP_PSTH_FILTER_METHOD_ALLOWED[](#_CPPv4N22bk_avrcp_psth_filter_t35BK_AVRCP_PSTH_FILTER_METHOD_ALLOWEDE "永久链接至目标")
    :   all of the PASSTHROUGH commands that can possibly be used, immutable

    enumerator BK_AVRCP_PSTH_FILTER_METHOD_CURRENT_ENABLE[](#_CPPv4N22bk_avrcp_psth_filter_t42BK_AVRCP_PSTH_FILTER_METHOD_CURRENT_ENABLEE "永久链接至目标")
    :   PASSTHROUGH commands selectively supported according to the current configuration

    enumerator BK_AVRCP_PSTH_FILTER_METHOD_MAX[](#_CPPv4N22bk_avrcp_psth_filter_t31BK_AVRCP_PSTH_FILTER_METHOD_MAXE "永久链接至目标")

enum bk_avrcp_bit_mask_op_t[](#_CPPv422bk_avrcp_bit_mask_op_t "永久链接至目标")
:   *Values:*

    enumerator BK_AVRCP_BIT_MASK_OP_TEST[](#_CPPv4N22bk_avrcp_bit_mask_op_t25BK_AVRCP_BIT_MASK_OP_TESTE "永久链接至目标")
    :   operation code to test a specific bit

    enumerator BK_AVRCP_BIT_MASK_OP_SET[](#_CPPv4N22bk_avrcp_bit_mask_op_t24BK_AVRCP_BIT_MASK_OP_SETE "永久链接至目标")
    :   operation code to set a specific bit

    enumerator BK_AVRCP_BIT_MASK_OP_CLEAR[](#_CPPv4N22bk_avrcp_bit_mask_op_t26BK_AVRCP_BIT_MASK_OP_CLEARE "永久链接至目标")
    :   operation code to clear a specific bit

enum bk_avrcp_tg_cb_event_t[](#_CPPv422bk_avrcp_tg_cb_event_t "永久链接至目标")
:   AVRC Target callback events.


    *Values:*

    enumerator BK_AVRCP_TG_CONNECTION_STATE_EVT[](#_CPPv4N22bk_avrcp_tg_cb_event_t32BK_AVRCP_TG_CONNECTION_STATE_EVTE "永久链接至目标")
    :   connection state changed event

    enumerator BK_AVRCP_TG_PASSTHROUGH_CMD_EVT[](#_CPPv4N22bk_avrcp_tg_cb_event_t31BK_AVRCP_TG_PASSTHROUGH_CMD_EVTE "永久链接至目标")
    :   passthrough command event

    enumerator BK_AVRCP_TG_SET_ABSOLUTE_VOLUME_CMD_EVT[](#_CPPv4N22bk_avrcp_tg_cb_event_t39BK_AVRCP_TG_SET_ABSOLUTE_VOLUME_CMD_EVTE "永久链接至目标")
    :   set absolute volume command from remote device

    enumerator BK_AVRCP_TG_REGISTER_NOTIFICATION_EVT[](#_CPPv4N22bk_avrcp_tg_cb_event_t37BK_AVRCP_TG_REGISTER_NOTIFICATION_EVTE "永久链接至目标")
    :   register notification event


### Header File[](#id38 "永久链接至标题")


- [bluetooth/bk_dm_hfp_types.h](https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_hfp_types.h "https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_hfp_types.h")


### Structures[](#id39 "永久链接至标题")

struct bk_hf_client_cb_param_t[](#_CPPv423bk_hf_client_cb_param_t "永久链接至目标")
:   HFP client callback parameters.

    Public Members

    uint8_t remote_bda[6][](#_CPPv4N23bk_hf_client_cb_param_t10remote_bdaE "永久链接至目标")
    :   remote bluetooth device address

    [bk_hf_client_connection_state_t](#_CPPv431bk_hf_client_connection_state_t "bk_hf_client_connection_state_t") state[](#_CPPv4N23bk_hf_client_cb_param_t5stateE "永久链接至目标")
    :   HF connection state

    uint32_t peer_feat[](#_CPPv4N23bk_hf_client_cb_param_t9peer_featE "永久链接至目标")
    :   AG supported features

    uint32_t chld_feat[](#_CPPv4N23bk_hf_client_cb_param_t9chld_featE "永久链接至目标")
    :   AG supported features on call hold and multiparty services

    struct [bk_hf_client_cb_param_t](#_CPPv423bk_hf_client_cb_param_t "bk_hf_client_cb_param_t")::[anonymous]::hf_client_conn_stat_param conn_state[](#_CPPv4N23bk_hf_client_cb_param_t10conn_stateE "永久链接至目标")
    :   HF callback param of BK_HF_CLIENT_CONNECTION_STATE_EVT

    [bk_hf_client_audio_state_t](#_CPPv426bk_hf_client_audio_state_t "bk_hf_client_audio_state_t") state
    :   audio connection state

    [bk_hf_codec_type_t](#_CPPv418bk_hf_codec_type_t "bk_hf_codec_type_t") codec_type[](#_CPPv4N23bk_hf_client_cb_param_t10codec_typeE "永久链接至目标")
    :   cvsd or msbc

    struct [bk_hf_client_cb_param_t](#_CPPv423bk_hf_client_cb_param_t "bk_hf_client_cb_param_t")::[anonymous]::hf_client_audio_stat_param audio_state[](#_CPPv4N23bk_hf_client_cb_param_t11audio_stateE "永久链接至目标")
    :   HF callback param of BK_HF_CLIENT_AUDIO_STATE_EVT

    [bk_hf_vr_state_t](#_CPPv416bk_hf_vr_state_t "bk_hf_vr_state_t") value[](#_CPPv4N23bk_hf_client_cb_param_t5valueE "永久链接至目标")
    :   voice recognition state

    struct [bk_hf_client_cb_param_t](#_CPPv423bk_hf_client_cb_param_t "bk_hf_client_cb_param_t")::[anonymous]::hf_client_bvra_param bvra[](#_CPPv4N23bk_hf_client_cb_param_t4bvraE "永久链接至目标")
    :   HF callback param of BK_HF_CLIENT_BVRA_EVT

    [bk_hf_call_status_t](#_CPPv419bk_hf_call_status_t "bk_hf_call_status_t") status[](#_CPPv4N23bk_hf_client_cb_param_t6statusE "永久链接至目标")
    :   call status indicator

    struct [bk_hf_client_cb_param_t](#_CPPv423bk_hf_client_cb_param_t "bk_hf_client_cb_param_t")::[anonymous]::hf_client_call_ind_param call[](#_CPPv4N23bk_hf_client_cb_param_t4callE "永久链接至目标")
    :   HF callback param of BK_HF_CLIENT_CIND_CALL_EVT

    [bk_hf_call_setup_status_t](#_CPPv425bk_hf_call_setup_status_t "bk_hf_call_setup_status_t") status
    :   call setup status indicator

    struct [bk_hf_client_cb_param_t](#_CPPv423bk_hf_client_cb_param_t "bk_hf_client_cb_param_t")::[anonymous]::hf_client_call_setup_ind_param call_setup[](#_CPPv4N23bk_hf_client_cb_param_t10call_setupE "永久链接至目标")
    :   HF callback param of BK_HF_CLIENT_BVRA_EVT

    [bk_hf_call_held_status_t](#_CPPv424bk_hf_call_held_status_t "bk_hf_call_held_status_t") status
    :   bluetooth proprietary call hold status indicator

    struct [bk_hf_client_cb_param_t](#_CPPv423bk_hf_client_cb_param_t "bk_hf_client_cb_param_t")::[anonymous]::hf_client_call_held_ind_param call_held[](#_CPPv4N23bk_hf_client_cb_param_t9call_heldE "永久链接至目标")
    :   HF callback param of BK_HF_CLIENT_CIND_CALL_HELD_EVT

    [bk_hf_network_state_t](#_CPPv421bk_hf_network_state_t "bk_hf_network_state_t") status
    :   service availability status

    struct [bk_hf_client_cb_param_t](#_CPPv423bk_hf_client_cb_param_t "bk_hf_client_cb_param_t")::[anonymous]::hf_client_service_availability_param service_availability[](#_CPPv4N23bk_hf_client_cb_param_t20service_availabilityE "永久链接至目标")
    :   HF callback param of BK_HF_CLIENT_CIND_SERVICE_AVAILABILITY_EVT

    int value
    :   signal strength value, ranges from 0 to 5

        battery charge value, ranges from 0 to 5

    struct [bk_hf_client_cb_param_t](#_CPPv423bk_hf_client_cb_param_t "bk_hf_client_cb_param_t")::[anonymous]::hf_client_signal_strength_ind_param signal_strength[](#_CPPv4N23bk_hf_client_cb_param_t15signal_strengthE "永久链接至目标")
    :   HF callback param of BK_HF_CLIENT_CIND_SIGNAL_STRENGTH_EVT

    [bk_hf_roaming_status_t](#_CPPv422bk_hf_roaming_status_t "bk_hf_roaming_status_t") status
    :   roaming status

    struct [bk_hf_client_cb_param_t](#_CPPv423bk_hf_client_cb_param_t "bk_hf_client_cb_param_t")::[anonymous]::hf_client_network_roaming_param roaming[](#_CPPv4N23bk_hf_client_cb_param_t7roamingE "永久链接至目标")
    :   HF callback param of BK_HF_CLIENT_CIND_ROAMING_STATUS_EVT

    struct [bk_hf_client_cb_param_t](#_CPPv423bk_hf_client_cb_param_t "bk_hf_client_cb_param_t")::[anonymous]::hf_client_battery_level_ind_param battery_level[](#_CPPv4N23bk_hf_client_cb_param_t13battery_levelE "永久链接至目标")
    :   HF callback param of BK_HF_CLIENT_CIND_BATTERY_LEVEL_EVT

    const char *name[](#_CPPv4N23bk_hf_client_cb_param_t4nameE "永久链接至目标")
    :   name of the network operator

        name string of the call

        name string of waiting call

    struct [bk_hf_client_cb_param_t](#_CPPv423bk_hf_client_cb_param_t "bk_hf_client_cb_param_t")::[anonymous]::hf_client_current_operator_param cops[](#_CPPv4N23bk_hf_client_cb_param_t4copsE "永久链接至目标")
    :   HF callback param of BK_HF_CLIENT_COPS_CURRENT_OPERATOR_EVT

    [bk_hf_btrh_status_t](#_CPPv419bk_hf_btrh_status_t "bk_hf_btrh_status_t") status
    :   call hold and response status result code

    struct [bk_hf_client_cb_param_t](#_CPPv423bk_hf_client_cb_param_t "bk_hf_client_cb_param_t")::[anonymous]::hf_client_btrh_param btrh[](#_CPPv4N23bk_hf_client_cb_param_t4btrhE "永久链接至目标")
    :   HF callback param of BK_HF_CLIENT_BRTH_EVT

    const char *number[](#_CPPv4N23bk_hf_client_cb_param_t6numberE "永久链接至目标")
    :   phone number string of call

        phone number string of waiting call

        phone number string

        phone number corresponding to the last voice tag in the HF

    struct [bk_hf_client_cb_param_t](#_CPPv423bk_hf_client_cb_param_t "bk_hf_client_cb_param_t")::[anonymous]::hf_client_clip_param clip[](#_CPPv4N23bk_hf_client_cb_param_t4clipE "永久链接至目标")
    :   HF callback param of BK_HF_CLIENT_CLIP_EVT

    struct [bk_hf_client_cb_param_t](#_CPPv423bk_hf_client_cb_param_t "bk_hf_client_cb_param_t")::[anonymous]::hf_client_ccwa_param ccwa[](#_CPPv4N23bk_hf_client_cb_param_t4ccwaE "永久链接至目标")
    :   HF callback param of BK_HF_CLIENT_BVRA_EVT

    int idx[](#_CPPv4N23bk_hf_client_cb_param_t3idxE "永久链接至目标")
    :   numbering(starting with 1) of the call

    [bk_hf_current_call_direction_t](#_CPPv430bk_hf_current_call_direction_t "bk_hf_current_call_direction_t") dir[](#_CPPv4N23bk_hf_client_cb_param_t3dirE "永久链接至目标")
    :   direction of the call

    [bk_hf_current_call_status_t](#_CPPv427bk_hf_current_call_status_t "bk_hf_current_call_status_t") status
    :   status of the call

    [bk_hf_current_call_mpty_type_t](#_CPPv430bk_hf_current_call_mpty_type_t "bk_hf_current_call_mpty_type_t") mpty[](#_CPPv4N23bk_hf_client_cb_param_t4mptyE "永久链接至目标")
    :   multi-party flag

    char *number
    :   phone number(optional)

    struct [bk_hf_client_cb_param_t](#_CPPv423bk_hf_client_cb_param_t "bk_hf_client_cb_param_t")::[anonymous]::hf_client_clcc_param clcc[](#_CPPv4N23bk_hf_client_cb_param_t4clccE "永久链接至目标")
    :   HF callback param of BK_HF_CLIENT_CLCC_EVT

    [bk_hf_volume_control_target_t](#_CPPv429bk_hf_volume_control_target_t "bk_hf_volume_control_target_t") type[](#_CPPv4N23bk_hf_client_cb_param_t4typeE "永久链接至目标")
    :   volume control target, speaker or microphone

    int volume[](#_CPPv4N23bk_hf_client_cb_param_t6volumeE "永久链接至目标")
    :   gain, ranges from 0 to 15

    struct [bk_hf_client_cb_param_t](#_CPPv423bk_hf_client_cb_param_t "bk_hf_client_cb_param_t")::[anonymous]::hf_client_volume_control_param volume_control[](#_CPPv4N23bk_hf_client_cb_param_t14volume_controlE "永久链接至目标")
    :   HF callback param of BK_HF_CLIENT_VOLUME_CONTROL_EVT

    [bk_hf_at_response_code_t](#_CPPv424bk_hf_at_response_code_t "bk_hf_at_response_code_t") code[](#_CPPv4N23bk_hf_client_cb_param_t4codeE "永久链接至目标")
    :   AT response code

    [bk_hf_cme_err_t](#_CPPv415bk_hf_cme_err_t "bk_hf_cme_err_t") cme[](#_CPPv4N23bk_hf_client_cb_param_t3cmeE "永久链接至目标")
    :   Extended Audio Gateway Error Result Code

    struct [bk_hf_client_cb_param_t](#_CPPv423bk_hf_client_cb_param_t "bk_hf_client_cb_param_t")::[anonymous]::hf_client_at_response_param at_response[](#_CPPv4N23bk_hf_client_cb_param_t11at_responseE "永久链接至目标")
    :   HF callback param of BK_HF_CLIENT_AT_RESPONSE_EVT

    [bk_hf_subscriber_service_type_t](#_CPPv431bk_hf_subscriber_service_type_t "bk_hf_subscriber_service_type_t") type
    :   service type that the phone number relates to

    struct [bk_hf_client_cb_param_t](#_CPPv423bk_hf_client_cb_param_t "bk_hf_client_cb_param_t")::[anonymous]::hf_client_cnum_param cnum[](#_CPPv4N23bk_hf_client_cb_param_t4cnumE "永久链接至目标")
    :   HF callback param of BK_HF_CLIENT_CNUM_EVT

    [bk_hf_client_in_band_ring_state_t](#_CPPv433bk_hf_client_in_band_ring_state_t "bk_hf_client_in_band_ring_state_t") state
    :   setting state of in-band ring tone

    struct [bk_hf_client_cb_param_t](#_CPPv423bk_hf_client_cb_param_t "bk_hf_client_cb_param_t")::[anonymous]::hf_client_bsirparam bsir[](#_CPPv4N23bk_hf_client_cb_param_t4bsirE "永久链接至目标")
    :   HF callback param of BK_HF_CLIENT_BSIR_EVT

    struct [bk_hf_client_cb_param_t](#_CPPv423bk_hf_client_cb_param_t "bk_hf_client_cb_param_t")::[anonymous]::hf_client_binp_param binp[](#_CPPv4N23bk_hf_client_cb_param_t4binpE "永久链接至目标")
    :   HF callback param of BK_HF_CLIENT_BINP_EVT

    const char *data[](#_CPPv4N23bk_hf_client_cb_param_t4dataE "永久链接至目标")
    :   unknown data

    uint16_t data_len[](#_CPPv4N23bk_hf_client_cb_param_t8data_lenE "永久链接至目标")
    :   the length of unknown data

    struct [bk_hf_client_cb_param_t](#_CPPv423bk_hf_client_cb_param_t "bk_hf_client_cb_param_t")::[anonymous]::hf_client_unknown_data_param unknown_data[](#_CPPv4N23bk_hf_client_cb_param_t12unknown_dataE "永久链接至目标")
    :   HF callback param of BK_HF_CLIENT_UNKNOWN_DATA_IND_EVT


### Macros[](#id40 "永久链接至标题")

BK_HF_CLIENT_PEER_FEAT_3WAY[](#c.BK_HF_CLIENT_PEER_FEAT_3WAY "永久链接至目标")

BK_HF_CLIENT_PEER_FEAT_ECNR[](#c.BK_HF_CLIENT_PEER_FEAT_ECNR "永久链接至目标")

BK_HF_CLIENT_PEER_FEAT_VREC[](#c.BK_HF_CLIENT_PEER_FEAT_VREC "永久链接至目标")

BK_HF_CLIENT_PEER_FEAT_INBAND[](#c.BK_HF_CLIENT_PEER_FEAT_INBAND "永久链接至目标")

BK_HF_CLIENT_PEER_FEAT_VTAG[](#c.BK_HF_CLIENT_PEER_FEAT_VTAG "永久链接至目标")

BK_HF_CLIENT_PEER_FEAT_REJECT[](#c.BK_HF_CLIENT_PEER_FEAT_REJECT "永久链接至目标")

BK_HF_CLIENT_PEER_FEAT_ECS[](#c.BK_HF_CLIENT_PEER_FEAT_ECS "永久链接至目标")

BK_HF_CLIENT_PEER_FEAT_ECC[](#c.BK_HF_CLIENT_PEER_FEAT_ECC "永久链接至目标")

BK_HF_CLIENT_PEER_FEAT_EXTERR[](#c.BK_HF_CLIENT_PEER_FEAT_EXTERR "永久链接至目标")

BK_HF_CLIENT_PEER_FEAT_CODEC[](#c.BK_HF_CLIENT_PEER_FEAT_CODEC "永久链接至目标")

BK_HF_CLIENT_PEER_FEAT_HF_IND[](#c.BK_HF_CLIENT_PEER_FEAT_HF_IND "永久链接至目标")

BK_HF_CLIENT_PEER_FEAT_ESCO_S4[](#c.BK_HF_CLIENT_PEER_FEAT_ESCO_S4 "永久链接至目标")

BK_HF_CLIENT_CHLD_FEAT_REL[](#c.BK_HF_CLIENT_CHLD_FEAT_REL "永久链接至目标")

BK_HF_CLIENT_CHLD_FEAT_REL_ACC[](#c.BK_HF_CLIENT_CHLD_FEAT_REL_ACC "永久链接至目标")

BK_HF_CLIENT_CHLD_FEAT_REL_X[](#c.BK_HF_CLIENT_CHLD_FEAT_REL_X "永久链接至目标")

BK_HF_CLIENT_CHLD_FEAT_HOLD_ACC[](#c.BK_HF_CLIENT_CHLD_FEAT_HOLD_ACC "永久链接至目标")

BK_HF_CLIENT_CHLD_FEAT_PRIV_X[](#c.BK_HF_CLIENT_CHLD_FEAT_PRIV_X "永久链接至目标")

BK_HF_CLIENT_CHLD_FEAT_MERGE[](#c.BK_HF_CLIENT_CHLD_FEAT_MERGE "永久链接至目标")

BK_HF_CLIENT_CHLD_FEAT_MERGE_DETACH[](#c.BK_HF_CLIENT_CHLD_FEAT_MERGE_DETACH "永久链接至目标")


### Type Definitions[](#id41 "永久链接至标题")

typedef void (*bk_bt_hf_client_cb_t)([bk_hf_client_cb_event_t](#_CPPv423bk_hf_client_cb_event_t "bk_hf_client_cb_event_t") event, [bk_hf_client_cb_param_t](#_CPPv423bk_hf_client_cb_param_t "bk_hf_client_cb_param_t") *param)[](#_CPPv420bk_bt_hf_client_cb_t "永久链接至目标")
:   HFP client callback function type.

    Param event
    :   : Event type

    Param param
    :   : Pointer to callback parameter

typedef void (*bk_bt_hf_client_data_cb_t)(const uint8_t *buf, uint16_t len)[](#_CPPv425bk_bt_hf_client_data_cb_t "永久链接至目标")
:   HFP client incoming data callback function.

    Param buf
    :   **[in]** : pointer to the data(payload of HCI synchronous data packet) received from HFP AG device

    Param len
    :   **[in]** : size(in bytes) in buf


### Enumerations[](#id42 "永久链接至标题")

enum bk_hf_client_connection_state_t[](#_CPPv431bk_hf_client_connection_state_t "永久链接至目标")
:   Bluetooth HFP RFCOMM connection and service level connection status.


    *Values:*

    enumerator BK_HF_CLIENT_CONNECTION_STATE_DISCONNECTED[](#_CPPv4N31bk_hf_client_connection_state_t42BK_HF_CLIENT_CONNECTION_STATE_DISCONNECTEDE "永久链接至目标")
    :   RFCOMM data link channel released

    enumerator BK_HF_CLIENT_CONNECTION_STATE_CONNECTING[](#_CPPv4N31bk_hf_client_connection_state_t40BK_HF_CLIENT_CONNECTION_STATE_CONNECTINGE "永久链接至目标")
    :   connecting remote device on the RFCOMM data link

    enumerator BK_HF_CLIENT_CONNECTION_STATE_CONNECTED[](#_CPPv4N31bk_hf_client_connection_state_t39BK_HF_CLIENT_CONNECTION_STATE_CONNECTEDE "永久链接至目标")
    :   RFCOMM connection established

    enumerator BK_HF_CLIENT_CONNECTION_STATE_SLC_CONNECTED[](#_CPPv4N31bk_hf_client_connection_state_t43BK_HF_CLIENT_CONNECTION_STATE_SLC_CONNECTEDE "永久链接至目标")
    :   service level connection established

    enumerator BK_HF_CLIENT_CONNECTION_STATE_DISCONNECTING[](#_CPPv4N31bk_hf_client_connection_state_t43BK_HF_CLIENT_CONNECTION_STATE_DISCONNECTINGE "永久链接至目标")
    :   disconnecting with remote device on the RFCOMM dat link

enum bk_hf_client_audio_state_t[](#_CPPv426bk_hf_client_audio_state_t "永久链接至目标")
:   Bluetooth HFP audio connection status.


    *Values:*

    enumerator BK_HF_CLIENT_AUDIO_STATE_DISCONNECTED[](#_CPPv4N26bk_hf_client_audio_state_t37BK_HF_CLIENT_AUDIO_STATE_DISCONNECTEDE "永久链接至目标")
    :   audio connection released

    enumerator BK_HF_CLIENT_AUDIO_STATE_CONNECTING[](#_CPPv4N26bk_hf_client_audio_state_t35BK_HF_CLIENT_AUDIO_STATE_CONNECTINGE "永久链接至目标")
    :   audio connection has been initiated

    enumerator BK_HF_CLIENT_AUDIO_STATE_CONNECTED[](#_CPPv4N26bk_hf_client_audio_state_t34BK_HF_CLIENT_AUDIO_STATE_CONNECTEDE "永久链接至目标")
    :   audio connection is established

enum bk_hf_client_cb_event_t[](#_CPPv423bk_hf_client_cb_event_t "永久链接至目标")
:   HF CLIENT callback events.


    *Values:*

    enumerator BK_HF_CLIENT_CONNECTION_STATE_EVT[](#_CPPv4N23bk_hf_client_cb_event_t33BK_HF_CLIENT_CONNECTION_STATE_EVTE "永久链接至目标")
    :   connection state changed event

    enumerator BK_HF_CLIENT_AUDIO_STATE_EVT[](#_CPPv4N23bk_hf_client_cb_event_t28BK_HF_CLIENT_AUDIO_STATE_EVTE "永久链接至目标")
    :   audio connection state change event

    enumerator BK_HF_CLIENT_BVRA_EVT[](#_CPPv4N23bk_hf_client_cb_event_t21BK_HF_CLIENT_BVRA_EVTE "永久链接至目标")
    :   voice recognition state change event

    enumerator BK_HF_CLIENT_CIND_CALL_EVT[](#_CPPv4N23bk_hf_client_cb_event_t26BK_HF_CLIENT_CIND_CALL_EVTE "永久链接至目标")
    :   call indication

    enumerator BK_HF_CLIENT_CIND_CALL_SETUP_EVT[](#_CPPv4N23bk_hf_client_cb_event_t32BK_HF_CLIENT_CIND_CALL_SETUP_EVTE "永久链接至目标")
    :   call setup indication

    enumerator BK_HF_CLIENT_CIND_CALL_HELD_EVT[](#_CPPv4N23bk_hf_client_cb_event_t31BK_HF_CLIENT_CIND_CALL_HELD_EVTE "永久链接至目标")
    :   call held indication

    enumerator BK_HF_CLIENT_CIND_SERVICE_AVAILABILITY_EVT[](#_CPPv4N23bk_hf_client_cb_event_t42BK_HF_CLIENT_CIND_SERVICE_AVAILABILITY_EVTE "永久链接至目标")
    :   network service availability indication

    enumerator BK_HF_CLIENT_CIND_SIGNAL_STRENGTH_EVT[](#_CPPv4N23bk_hf_client_cb_event_t37BK_HF_CLIENT_CIND_SIGNAL_STRENGTH_EVTE "永久链接至目标")
    :   signal strength indication

    enumerator BK_HF_CLIENT_CIND_ROAMING_STATUS_EVT[](#_CPPv4N23bk_hf_client_cb_event_t36BK_HF_CLIENT_CIND_ROAMING_STATUS_EVTE "永久链接至目标")
    :   roaming status indication

    enumerator BK_HF_CLIENT_CIND_BATTERY_LEVEL_EVT[](#_CPPv4N23bk_hf_client_cb_event_t35BK_HF_CLIENT_CIND_BATTERY_LEVEL_EVTE "永久链接至目标")
    :   battery level indication

    enumerator BK_HF_CLIENT_COPS_CURRENT_OPERATOR_EVT[](#_CPPv4N23bk_hf_client_cb_event_t38BK_HF_CLIENT_COPS_CURRENT_OPERATOR_EVTE "永久链接至目标")
    :   current operator information

    enumerator BK_HF_CLIENT_BTRH_EVT[](#_CPPv4N23bk_hf_client_cb_event_t21BK_HF_CLIENT_BTRH_EVTE "永久链接至目标")
    :   call response and hold event

    enumerator BK_HF_CLIENT_CLIP_EVT[](#_CPPv4N23bk_hf_client_cb_event_t21BK_HF_CLIENT_CLIP_EVTE "永久链接至目标")
    :   Calling Line Identification notification

    enumerator BK_HF_CLIENT_CCWA_EVT[](#_CPPv4N23bk_hf_client_cb_event_t21BK_HF_CLIENT_CCWA_EVTE "永久链接至目标")
    :   call waiting notification

    enumerator BK_HF_CLIENT_CLCC_EVT[](#_CPPv4N23bk_hf_client_cb_event_t21BK_HF_CLIENT_CLCC_EVTE "永久链接至目标")
    :   list of current calls notification

    enumerator BK_HF_CLIENT_VOLUME_CONTROL_EVT[](#_CPPv4N23bk_hf_client_cb_event_t31BK_HF_CLIENT_VOLUME_CONTROL_EVTE "永久链接至目标")
    :   audio volume control command from AG, provided by +VGM or +VGS message

    enumerator BK_HF_CLIENT_AT_RESPONSE_EVT[](#_CPPv4N23bk_hf_client_cb_event_t28BK_HF_CLIENT_AT_RESPONSE_EVTE "永久链接至目标")
    :   AT command response event

    enumerator BK_HF_CLIENT_CNUM_EVT[](#_CPPv4N23bk_hf_client_cb_event_t21BK_HF_CLIENT_CNUM_EVTE "永久链接至目标")
    :   subscriber information response from AG

    enumerator BK_HF_CLIENT_BSIR_EVT[](#_CPPv4N23bk_hf_client_cb_event_t21BK_HF_CLIENT_BSIR_EVTE "永久链接至目标")
    :   setting of in-band ring tone

    enumerator BK_HF_CLIENT_BINP_EVT[](#_CPPv4N23bk_hf_client_cb_event_t21BK_HF_CLIENT_BINP_EVTE "永久链接至目标")
    :   requested number of last voice tag from AG

    enumerator BK_HF_CLIENT_RING_IND_EVT[](#_CPPv4N23bk_hf_client_cb_event_t25BK_HF_CLIENT_RING_IND_EVTE "永久链接至目标")
    :   ring indication event

    enumerator BK_HF_CLIENT_UNKNOWN_DATA_IND_EVT[](#_CPPv4N23bk_hf_client_cb_event_t33BK_HF_CLIENT_UNKNOWN_DATA_IND_EVTE "永久链接至目标")
    :   unknown data from AG

enum bk_hf_codec_type_t[](#_CPPv418bk_hf_codec_type_t "永久链接至目标")
:   Codec Type.


    *Values:*

    enumerator CODEC_VOICE_CVSD[](#_CPPv4N18bk_hf_codec_type_t16CODEC_VOICE_CVSDE "永久链接至目标")
    :   cvsd

    enumerator CODEC_VOICE_MSBC[](#_CPPv4N18bk_hf_codec_type_t16CODEC_VOICE_MSBCE "永久链接至目标")
    :   msbc

enum bk_hf_vr_state_t[](#_CPPv416bk_hf_vr_state_t "永久链接至目标")
:   voice recognition state


    *Values:*

    enumerator BK_HF_VR_STATE_DISABLED[](#_CPPv4N16bk_hf_vr_state_t23BK_HF_VR_STATE_DISABLEDE "永久链接至目标")
    :   voice recognition disabled

    enumerator BK_HF_VR_STATE_ENABLED[](#_CPPv4N16bk_hf_vr_state_t22BK_HF_VR_STATE_ENABLEDE "永久链接至目标")
    :   voice recognition enabled

enum bk_hf_call_status_t[](#_CPPv419bk_hf_call_status_t "永久链接至目标")
:   +CIND call status indicator values


    *Values:*

    enumerator BK_HF_CALL_STATUS_NO_CALLS[](#_CPPv4N19bk_hf_call_status_t26BK_HF_CALL_STATUS_NO_CALLSE "永久链接至目标")
    :   no call in progress

    enumerator BK_HF_CALL_STATUS_CALL_IN_PROGRESS[](#_CPPv4N19bk_hf_call_status_t34BK_HF_CALL_STATUS_CALL_IN_PROGRESSE "永久链接至目标")
    :   call is present(active or held)

enum bk_hf_call_setup_status_t[](#_CPPv425bk_hf_call_setup_status_t "永久链接至目标")
:   +CIND call setup status indicator values


    *Values:*

    enumerator BK_HF_CALL_SETUP_STATUS_IDLE[](#_CPPv4N25bk_hf_call_setup_status_t28BK_HF_CALL_SETUP_STATUS_IDLEE "永久链接至目标")
    :   no call setup in progress

    enumerator BK_HF_CALL_SETUP_STATUS_INCOMING[](#_CPPv4N25bk_hf_call_setup_status_t32BK_HF_CALL_SETUP_STATUS_INCOMINGE "永久链接至目标")
    :   incoming call setup in progress

    enumerator BK_HF_CALL_SETUP_STATUS_OUTGOING_DIALING[](#_CPPv4N25bk_hf_call_setup_status_t40BK_HF_CALL_SETUP_STATUS_OUTGOING_DIALINGE "永久链接至目标")
    :   outgoing call setup in dialing state

    enumerator BK_HF_CALL_SETUP_STATUS_OUTGOING_ALERTING[](#_CPPv4N25bk_hf_call_setup_status_t41BK_HF_CALL_SETUP_STATUS_OUTGOING_ALERTINGE "永久链接至目标")
    :   outgoing call setup in alerting state

enum bk_hf_call_held_status_t[](#_CPPv424bk_hf_call_held_status_t "永久链接至目标")
:   +CIND call held indicator values


    *Values:*

    enumerator BK_HF_CALL_HELD_STATUS_NONE[](#_CPPv4N24bk_hf_call_held_status_t27BK_HF_CALL_HELD_STATUS_NONEE "永久链接至目标")
    :   no calls held

    enumerator BK_HF_CALL_HELD_STATUS_HELD_AND_ACTIVE[](#_CPPv4N24bk_hf_call_held_status_t38BK_HF_CALL_HELD_STATUS_HELD_AND_ACTIVEE "永久链接至目标")
    :   both active and held call

    enumerator BK_HF_CALL_HELD_STATUS_HELD[](#_CPPv4N24bk_hf_call_held_status_t27BK_HF_CALL_HELD_STATUS_HELDE "永久链接至目标")
    :   call on hold, no active call

enum bk_hf_network_state_t[](#_CPPv421bk_hf_network_state_t "永久链接至目标")
:   +CIND network service availability status


    *Values:*

    enumerator BK_HF_NETWORK_STATE_NOT_AVAILABLE[](#_CPPv4N21bk_hf_network_state_t33BK_HF_NETWORK_STATE_NOT_AVAILABLEE "永久链接至目标")

    enumerator BK_HF_NETWORK_STATE_AVAILABLE[](#_CPPv4N21bk_hf_network_state_t29BK_HF_NETWORK_STATE_AVAILABLEE "永久链接至目标")

enum bk_hf_roaming_status_t[](#_CPPv422bk_hf_roaming_status_t "永久链接至目标")
:   +CIND roaming status indicator values


    *Values:*

    enumerator BK_HF_ROAMING_STATUS_INACTIVE[](#_CPPv4N22bk_hf_roaming_status_t29BK_HF_ROAMING_STATUS_INACTIVEE "永久链接至目标")
    :   roaming is not active

    enumerator BK_HF_ROAMING_STATUS_ACTIVE[](#_CPPv4N22bk_hf_roaming_status_t27BK_HF_ROAMING_STATUS_ACTIVEE "永久链接至目标")
    :   a roaming is active

enum bk_hf_btrh_status_t[](#_CPPv419bk_hf_btrh_status_t "永久链接至目标")
:   +BTRH response and hold result code


    *Values:*

    enumerator BK_HF_BTRH_STATUS_HELD[](#_CPPv4N19bk_hf_btrh_status_t22BK_HF_BTRH_STATUS_HELDE "永久链接至目标")
    :   incoming call is put on held in AG

    enumerator BK_HF_BTRH_STATUS_ACCEPTED[](#_CPPv4N19bk_hf_btrh_status_t26BK_HF_BTRH_STATUS_ACCEPTEDE "永久链接至目标")
    :   held incoming call is accepted in AG

    enumerator BK_HF_BTRH_STATUS_REJECTED[](#_CPPv4N19bk_hf_btrh_status_t26BK_HF_BTRH_STATUS_REJECTEDE "永久链接至目标")
    :   held incoming call is rejected in AG

enum bk_hf_current_call_status_t[](#_CPPv427bk_hf_current_call_status_t "永久链接至目标")
:   +CLCC status of the call


    *Values:*

    enumerator BK_HF_CURRENT_CALL_STATUS_ACTIVE[](#_CPPv4N27bk_hf_current_call_status_t32BK_HF_CURRENT_CALL_STATUS_ACTIVEE "永久链接至目标")
    :   active

    enumerator BK_HF_CURRENT_CALL_STATUS_HELD[](#_CPPv4N27bk_hf_current_call_status_t30BK_HF_CURRENT_CALL_STATUS_HELDE "永久链接至目标")
    :   held

    enumerator BK_HF_CURRENT_CALL_STATUS_DIALING[](#_CPPv4N27bk_hf_current_call_status_t33BK_HF_CURRENT_CALL_STATUS_DIALINGE "永久链接至目标")
    :   dialing (outgoing calls only)

    enumerator BK_HF_CURRENT_CALL_STATUS_ALERTING[](#_CPPv4N27bk_hf_current_call_status_t34BK_HF_CURRENT_CALL_STATUS_ALERTINGE "永久链接至目标")
    :   alerting (outgoing calls only)

    enumerator BK_HF_CURRENT_CALL_STATUS_INCOMING[](#_CPPv4N27bk_hf_current_call_status_t34BK_HF_CURRENT_CALL_STATUS_INCOMINGE "永久链接至目标")
    :   incoming (incoming calls only)

    enumerator BK_HF_CURRENT_CALL_STATUS_WAITING[](#_CPPv4N27bk_hf_current_call_status_t33BK_HF_CURRENT_CALL_STATUS_WAITINGE "永久链接至目标")
    :   waiting (incoming calls only)

    enumerator BK_HF_CURRENT_CALL_STATUS_HELD_BY_RBK_HOLD[](#_CPPv4N27bk_hf_current_call_status_t42BK_HF_CURRENT_CALL_STATUS_HELD_BY_RBK_HOLDE "永久链接至目标")
    :   call held by response and hold

enum bk_hf_current_call_direction_t[](#_CPPv430bk_hf_current_call_direction_t "永久链接至目标")
:   +CLCC direction of the call


    *Values:*

    enumerator BK_HF_CURRENT_CALL_DIRECTION_OUTGOING[](#_CPPv4N30bk_hf_current_call_direction_t37BK_HF_CURRENT_CALL_DIRECTION_OUTGOINGE "永久链接至目标")
    :   outgoing

    enumerator BK_HF_CURRENT_CALL_DIRECTION_INCOMING[](#_CPPv4N30bk_hf_current_call_direction_t37BK_HF_CURRENT_CALL_DIRECTION_INCOMINGE "永久链接至目标")
    :   incoming

enum bk_hf_current_call_mpty_type_t[](#_CPPv430bk_hf_current_call_mpty_type_t "永久链接至目标")
:   +CLCC multi-party call flag


    *Values:*

    enumerator BK_HF_CURRENT_CALL_MPTY_TYPE_SINGLE[](#_CPPv4N30bk_hf_current_call_mpty_type_t35BK_HF_CURRENT_CALL_MPTY_TYPE_SINGLEE "永久链接至目标")
    :   not a member of a multi-party call

    enumerator BK_HF_CURRENT_CALL_MPTY_TYPE_MULTI[](#_CPPv4N30bk_hf_current_call_mpty_type_t34BK_HF_CURRENT_CALL_MPTY_TYPE_MULTIE "永久链接至目标")
    :   member of a multi-party call

enum bk_hf_volume_control_target_t[](#_CPPv429bk_hf_volume_control_target_t "永久链接至目标")
:   Bluetooth HFP audio volume control target.


    *Values:*

    enumerator BK_HF_VOLUME_CONTROL_TARGET_SPK[](#_CPPv4N29bk_hf_volume_control_target_t31BK_HF_VOLUME_CONTROL_TARGET_SPKE "永久链接至目标")
    :   speaker

    enumerator BK_HF_VOLUME_CONTROL_TARGET_MIC[](#_CPPv4N29bk_hf_volume_control_target_t31BK_HF_VOLUME_CONTROL_TARGET_MICE "永久链接至目标")
    :   microphone

enum bk_hf_chld_type_t[](#_CPPv417bk_hf_chld_type_t "永久链接至目标")
:   AT+CHLD command values.


    *Values:*

    enumerator BK_HF_CHLD_TYPE_REL[](#_CPPv4N17bk_hf_chld_type_t19BK_HF_CHLD_TYPE_RELE "永久链接至目标")
    :   <0>, Terminate all held or set UDUB(“busy”) to a waiting call

    enumerator BK_HF_CHLD_TYPE_REL_ACC[](#_CPPv4N17bk_hf_chld_type_t23BK_HF_CHLD_TYPE_REL_ACCE "永久链接至目标")
    :   <1>, Terminate all active calls and accepts a waiting/held call

    enumerator BK_HF_CHLD_TYPE_HOLD_ACC[](#_CPPv4N17bk_hf_chld_type_t24BK_HF_CHLD_TYPE_HOLD_ACCE "永久链接至目标")
    :   <2>, Hold all active calls and accepts a waiting/held call

    enumerator BK_HF_CHLD_TYPE_MERGE[](#_CPPv4N17bk_hf_chld_type_t21BK_HF_CHLD_TYPE_MERGEE "永久链接至目标")
    :   <3>, Add all held calls to a conference

    enumerator BK_HF_CHLD_TYPE_MERGE_DETACH[](#_CPPv4N17bk_hf_chld_type_t28BK_HF_CHLD_TYPE_MERGE_DETACHE "永久链接至目标")
    :   <4>, connect the two calls and disconnects the subscriber from both calls

enum bk_hf_btrh_cmd_t[](#_CPPv416bk_hf_btrh_cmd_t "永久链接至目标")
:   AT+BTRH response and hold action code.


    *Values:*

    enumerator BK_HF_BTRH_CMD_HOLD[](#_CPPv4N16bk_hf_btrh_cmd_t19BK_HF_BTRH_CMD_HOLDE "永久链接至目标")
    :   put the incoming call on hold

    enumerator BK_HF_BTRH_CMD_ACCEPT[](#_CPPv4N16bk_hf_btrh_cmd_t21BK_HF_BTRH_CMD_ACCEPTE "永久链接至目标")
    :   accept a held incoming call

    enumerator BK_HF_BTRH_CMD_REJECT[](#_CPPv4N16bk_hf_btrh_cmd_t21BK_HF_BTRH_CMD_REJECTE "永久链接至目标")
    :   reject a held incoming call

enum bk_hf_at_response_code_t[](#_CPPv424bk_hf_at_response_code_t "永久链接至目标")
:   *Values:*

    enumerator BK_HF_AT_RESPONSE_CODE_OK[](#_CPPv4N24bk_hf_at_response_code_t25BK_HF_AT_RESPONSE_CODE_OKE "永久链接至目标")
    :   acknowledges execution of a command line

    enumerator BK_HF_AT_RESPONSE_CODE_ERR[](#_CPPv4N24bk_hf_at_response_code_t26BK_HF_AT_RESPONSE_CODE_ERRE "永久链接至目标")
    :   command not accepted

    enumerator BK_HF_AT_RESPONSE_CODE_NO_CARRIER[](#_CPPv4N24bk_hf_at_response_code_t33BK_HF_AT_RESPONSE_CODE_NO_CARRIERE "永久链接至目标")
    :   connection terminated

    enumerator BK_HF_AT_RESPONSE_CODE_BUSY[](#_CPPv4N24bk_hf_at_response_code_t27BK_HF_AT_RESPONSE_CODE_BUSYE "永久链接至目标")
    :   busy signal detected

    enumerator BK_HF_AT_RESPONSE_CODE_NO_ANSWER[](#_CPPv4N24bk_hf_at_response_code_t32BK_HF_AT_RESPONSE_CODE_NO_ANSWERE "永久链接至目标")
    :   connection completion timeout

    enumerator BK_HF_AT_RESPONSE_CODE_DELAYED[](#_CPPv4N24bk_hf_at_response_code_t30BK_HF_AT_RESPONSE_CODE_DELAYEDE "永久链接至目标")
    :   delayed

    enumerator BK_HF_AT_RESPONSE_CODE_BLACKLISTED[](#_CPPv4N24bk_hf_at_response_code_t34BK_HF_AT_RESPONSE_CODE_BLACKLISTEDE "永久链接至目标")
    :   blacklisted

    enumerator BK_HF_AT_RESPONSE_CODE_CME[](#_CPPv4N24bk_hf_at_response_code_t26BK_HF_AT_RESPONSE_CODE_CMEE "永久链接至目标")
    :   CME error

enum bk_hf_at_response_t[](#_CPPv419bk_hf_at_response_t "永久链接至目标")
:   *Values:*

    enumerator BK_HF_AT_RESPONSE_ERROR[](#_CPPv4N19bk_hf_at_response_t23BK_HF_AT_RESPONSE_ERRORE "永久链接至目标")

    enumerator BK_HF_AT_RESPONSE_OK[](#_CPPv4N19bk_hf_at_response_t20BK_HF_AT_RESPONSE_OKE "永久链接至目标")

enum bk_hf_cme_err_t[](#_CPPv415bk_hf_cme_err_t "永久链接至目标")
:   Extended Audio Gateway Error Result Code Response.


    *Values:*

    enumerator BK_HF_CME_AG_FAILURE[](#_CPPv4N15bk_hf_cme_err_t20BK_HF_CME_AG_FAILUREE "永久链接至目标")
    :   ag failure

    enumerator BK_HF_CME_NO_CONNECTION_TO_PHONE[](#_CPPv4N15bk_hf_cme_err_t32BK_HF_CME_NO_CONNECTION_TO_PHONEE "永久链接至目标")
    :   no connection to phone

    enumerator BK_HF_CME_OPERATION_NOT_ALLOWED[](#_CPPv4N15bk_hf_cme_err_t31BK_HF_CME_OPERATION_NOT_ALLOWEDE "永久链接至目标")
    :   operation not allowed

    enumerator BK_HF_CME_OPERATION_NOT_SUPPORTED[](#_CPPv4N15bk_hf_cme_err_t33BK_HF_CME_OPERATION_NOT_SUPPORTEDE "永久链接至目标")
    :   operation not supported

    enumerator BK_HF_CME_PH_SIM_PIN_REQUIRED[](#_CPPv4N15bk_hf_cme_err_t29BK_HF_CME_PH_SIM_PIN_REQUIREDE "永久链接至目标")
    :   PH-SIM PIN Required

    enumerator BK_HF_CME_SIM_NOT_INSERTED[](#_CPPv4N15bk_hf_cme_err_t26BK_HF_CME_SIM_NOT_INSERTEDE "永久链接至目标")
    :   SIM not inserted

    enumerator BK_HF_CME_SIM_PIN_REQUIRED[](#_CPPv4N15bk_hf_cme_err_t26BK_HF_CME_SIM_PIN_REQUIREDE "永久链接至目标")
    :   SIM PIN required

    enumerator BK_HF_CME_SIM_PUK_REQUIRED[](#_CPPv4N15bk_hf_cme_err_t26BK_HF_CME_SIM_PUK_REQUIREDE "永久链接至目标")
    :   SIM PUK required

    enumerator BK_HF_CME_SIM_FAILURE[](#_CPPv4N15bk_hf_cme_err_t21BK_HF_CME_SIM_FAILUREE "永久链接至目标")
    :   SIM failure

    enumerator BK_HF_CME_SIM_BUSY[](#_CPPv4N15bk_hf_cme_err_t18BK_HF_CME_SIM_BUSYE "永久链接至目标")
    :   SIM busy

    enumerator BK_HF_CME_INCORRECT_PASSWORD[](#_CPPv4N15bk_hf_cme_err_t28BK_HF_CME_INCORRECT_PASSWORDE "永久链接至目标")
    :   incorrect password

    enumerator BK_HF_CME_SIM_PIN2_REQUIRED[](#_CPPv4N15bk_hf_cme_err_t27BK_HF_CME_SIM_PIN2_REQUIREDE "永久链接至目标")
    :   SIM PIN2 required

    enumerator BK_HF_CME_SIM_PUK2_REQUIRED[](#_CPPv4N15bk_hf_cme_err_t27BK_HF_CME_SIM_PUK2_REQUIREDE "永久链接至目标")
    :   SIM PUK2 required

    enumerator BK_HF_CME_MEMORY_FULL[](#_CPPv4N15bk_hf_cme_err_t21BK_HF_CME_MEMORY_FULLE "永久链接至目标")
    :   memory full

    enumerator BK_HF_CME_INVALID_INDEX[](#_CPPv4N15bk_hf_cme_err_t23BK_HF_CME_INVALID_INDEXE "永久链接至目标")
    :   invalid index

    enumerator BK_HF_CME_MEMORY_FAILURE[](#_CPPv4N15bk_hf_cme_err_t24BK_HF_CME_MEMORY_FAILUREE "永久链接至目标")
    :   memory failure

    enumerator BK_HF_CME_TEXT_STRING_TOO_LONG[](#_CPPv4N15bk_hf_cme_err_t30BK_HF_CME_TEXT_STRING_TOO_LONGE "永久链接至目标")
    :   test string too long

    enumerator BK_HF_CME_INVALID_CHARACTERS_IN_TEXT_STRING[](#_CPPv4N15bk_hf_cme_err_t43BK_HF_CME_INVALID_CHARACTERS_IN_TEXT_STRINGE "永久链接至目标")
    :   invalid characters in text string

    enumerator BK_HF_CME_DIAL_STRING_TOO_LONG[](#_CPPv4N15bk_hf_cme_err_t30BK_HF_CME_DIAL_STRING_TOO_LONGE "永久链接至目标")
    :   dial string too long

    enumerator BK_HF_CME_INVALID_CHARACTERS_IN_DIAL_STRING[](#_CPPv4N15bk_hf_cme_err_t43BK_HF_CME_INVALID_CHARACTERS_IN_DIAL_STRINGE "永久链接至目标")
    :   invalid characters in dial string

    enumerator BK_HF_CME_NO_NETWORK_SERVICE[](#_CPPv4N15bk_hf_cme_err_t28BK_HF_CME_NO_NETWORK_SERVICEE "永久链接至目标")
    :   no network service

    enumerator BK_HF_CME_NETWORK_TIMEOUT[](#_CPPv4N15bk_hf_cme_err_t25BK_HF_CME_NETWORK_TIMEOUTE "永久链接至目标")
    :   network timeout

    enumerator BK_HF_CME_NETWORK_NOT_ALLOWED[](#_CPPv4N15bk_hf_cme_err_t29BK_HF_CME_NETWORK_NOT_ALLOWEDE "永久链接至目标")
    :   network not allowed &#8212;emergency calls only

enum bk_hf_subscriber_service_type_t[](#_CPPv431bk_hf_subscriber_service_type_t "永久链接至目标")
:   +CNUM service type of the phone number


    *Values:*

    enumerator BK_HF_SUBSCRIBER_SERVICE_TYPE_UNKNOWN[](#_CPPv4N31bk_hf_subscriber_service_type_t37BK_HF_SUBSCRIBER_SERVICE_TYPE_UNKNOWNE "永久链接至目标")
    :   unknown

    enumerator BK_HF_SUBSCRIBER_SERVICE_TYPE_VOICE[](#_CPPv4N31bk_hf_subscriber_service_type_t35BK_HF_SUBSCRIBER_SERVICE_TYPE_VOICEE "永久链接至目标")
    :   voice service

    enumerator BK_HF_SUBSCRIBER_SERVICE_TYPE_FAX[](#_CPPv4N31bk_hf_subscriber_service_type_t33BK_HF_SUBSCRIBER_SERVICE_TYPE_FAXE "永久链接至目标")
    :   fax service

enum bk_hf_client_in_band_ring_state_t[](#_CPPv433bk_hf_client_in_band_ring_state_t "永久链接至目标")
:   in-band ring tone state


    *Values:*

    enumerator BK_HF_CLIENT_IN_BAND_RINGTONE_NOT_PROVIDED[](#_CPPv4N33bk_hf_client_in_band_ring_state_t42BK_HF_CLIENT_IN_BAND_RINGTONE_NOT_PROVIDEDE "永久链接至目标")

    enumerator BK_HF_CLIENT_IN_BAND_RINGTONE_PROVIDED[](#_CPPv4N33bk_hf_client_in_band_ring_state_t38BK_HF_CLIENT_IN_BAND_RINGTONE_PROVIDEDE "永久链接至目标")


### Header File[](#id43 "永久链接至标题")


- [bluetooth/bk_dm_gap_bt_types.h](https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_gap_bt_types.h "https://github.com/bekencorp/armino/blob/main/components/bluetooth/bk_dm_gap_bt_types.h")


### Unions[](#id44 "永久链接至标题")

union bk_bt_cod_t[](#_CPPv411bk_bt_cod_t "永久链接至目标")
:   *#include <bk_dm_gap_bt_types.h>*

    Class of device.

    Public Members

    struct [bk_bt_cod_t](#_CPPv411bk_bt_cod_t "bk_bt_cod_t")::[class_of_device](#_CPPv4N11bk_bt_cod_t15class_of_deviceE "bk_bt_cod_t::class_of_device") cod_t[](#_CPPv4N11bk_bt_cod_t5cod_tE "永久链接至目标")

    uint32_t cod[](#_CPPv4N11bk_bt_cod_t3codE "永久链接至目标")

    struct class_of_device[](#_CPPv4N11bk_bt_cod_t15class_of_deviceE "永久链接至目标")
    :   Public Members

        uint32_t reserved_2[](#_CPPv4N11bk_bt_cod_t15class_of_device10reserved_2E "永久链接至目标")
        :   undefined

        uint32_t minor[](#_CPPv4N11bk_bt_cod_t15class_of_device5minorE "永久链接至目标")
        :   minor class

        uint32_t major[](#_CPPv4N11bk_bt_cod_t15class_of_device5majorE "永久链接至目标")
        :   major class

        uint32_t service[](#_CPPv4N11bk_bt_cod_t15class_of_device7serviceE "永久链接至目标")
        :   service class

        uint32_t reserved_8[](#_CPPv4N11bk_bt_cod_t15class_of_device10reserved_8E "永久链接至目标")
        :   undefined

union bk_bt_gap_cb_param_t[](#_CPPv420bk_bt_gap_cb_param_t "永久链接至目标")
:   *#include <bk_dm_gap_bt_types.h>*

    GAP state callback parameters.

    Public Members

    struct [bk_bt_gap_cb_param_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[disc_res_param](#_CPPv4N20bk_bt_gap_cb_param_t14disc_res_paramE "bk_bt_gap_cb_param_t::disc_res_param") disc_res[](#_CPPv4N20bk_bt_gap_cb_param_t8disc_resE "永久链接至目标")
    :   discovery result parameter struct

    struct [bk_bt_gap_cb_param_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[disc_state_changed_param](#_CPPv4N20bk_bt_gap_cb_param_t24disc_state_changed_paramE "bk_bt_gap_cb_param_t::disc_state_changed_param") disc_st_chg[](#_CPPv4N20bk_bt_gap_cb_param_t11disc_st_chgE "永久链接至目标")
    :   discovery state changed parameter struct

    struct [bk_bt_gap_cb_param_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[rmt_srvcs_param](#_CPPv4N20bk_bt_gap_cb_param_t15rmt_srvcs_paramE "bk_bt_gap_cb_param_t::rmt_srvcs_param") rmt_srvcs[](#_CPPv4N20bk_bt_gap_cb_param_t9rmt_srvcsE "永久链接至目标")
    :   services of remote device parameter struct

    struct [bk_bt_gap_cb_param_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[rmt_srvc_rec_param](#_CPPv4N20bk_bt_gap_cb_param_t18rmt_srvc_rec_paramE "bk_bt_gap_cb_param_t::rmt_srvc_rec_param") rmt_srvc_rec[](#_CPPv4N20bk_bt_gap_cb_param_t12rmt_srvc_recE "永久链接至目标")
    :   specific service record from remote device parameter struct

    struct [bk_bt_gap_cb_param_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[read_rssi_delta_param](#_CPPv4N20bk_bt_gap_cb_param_t21read_rssi_delta_paramE "bk_bt_gap_cb_param_t::read_rssi_delta_param") read_rssi_delta[](#_CPPv4N20bk_bt_gap_cb_param_t15read_rssi_deltaE "永久链接至目标")
    :   read rssi parameter struct

    struct [bk_bt_gap_cb_param_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[config_eir_data_param](#_CPPv4N20bk_bt_gap_cb_param_t21config_eir_data_paramE "bk_bt_gap_cb_param_t::config_eir_data_param") config_eir_data[](#_CPPv4N20bk_bt_gap_cb_param_t15config_eir_dataE "永久链接至目标")
    :   config EIR data

    struct [bk_bt_gap_cb_param_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[auth_cmpl_param](#_CPPv4N20bk_bt_gap_cb_param_t15auth_cmpl_paramE "bk_bt_gap_cb_param_t::auth_cmpl_param") auth_cmpl[](#_CPPv4N20bk_bt_gap_cb_param_t9auth_cmplE "永久链接至目标")
    :   authentication complete parameter struct

    struct [bk_bt_gap_cb_param_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[pin_req_param](#_CPPv4N20bk_bt_gap_cb_param_t13pin_req_paramE "bk_bt_gap_cb_param_t::pin_req_param") pin_req[](#_CPPv4N20bk_bt_gap_cb_param_t7pin_reqE "永久链接至目标")
    :   pin request parameter struct

    struct [bk_bt_gap_cb_param_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[cfm_req_param](#_CPPv4N20bk_bt_gap_cb_param_t13cfm_req_paramE "bk_bt_gap_cb_param_t::cfm_req_param") cfm_req[](#_CPPv4N20bk_bt_gap_cb_param_t7cfm_reqE "永久链接至目标")
    :   confirm request parameter struct

    struct [bk_bt_gap_cb_param_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[key_notif_param](#_CPPv4N20bk_bt_gap_cb_param_t15key_notif_paramE "bk_bt_gap_cb_param_t::key_notif_param") key_notif[](#_CPPv4N20bk_bt_gap_cb_param_t9key_notifE "永久链接至目标")
    :   passkey notif parameter struct

    struct [bk_bt_gap_cb_param_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[key_req_param](#_CPPv4N20bk_bt_gap_cb_param_t13key_req_paramE "bk_bt_gap_cb_param_t::key_req_param") key_req[](#_CPPv4N20bk_bt_gap_cb_param_t7key_reqE "永久链接至目标")
    :   passkey request parameter struct

    struct [bk_bt_gap_cb_param_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[set_afh_channels_param](#_CPPv4N20bk_bt_gap_cb_param_t22set_afh_channels_paramE "bk_bt_gap_cb_param_t::set_afh_channels_param") set_afh_channels[](#_CPPv4N20bk_bt_gap_cb_param_t16set_afh_channelsE "永久链接至目标")
    :   set AFH channel parameter struct

    struct [bk_bt_gap_cb_param_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[read_rmt_name_param](#_CPPv4N20bk_bt_gap_cb_param_t19read_rmt_name_paramE "bk_bt_gap_cb_param_t::read_rmt_name_param") read_rmt_name[](#_CPPv4N20bk_bt_gap_cb_param_t13read_rmt_nameE "永久链接至目标")
    :   read Remote Name parameter struct

    struct [bk_bt_gap_cb_param_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[mode_chg_param](#_CPPv4N20bk_bt_gap_cb_param_t14mode_chg_paramE "bk_bt_gap_cb_param_t::mode_chg_param") mode_chg[](#_CPPv4N20bk_bt_gap_cb_param_t8mode_chgE "永久链接至目标")
    :   mode change event parameter struct

    struct [bk_bt_gap_cb_param_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[bt_remove_bond_dev_cmpl_evt_param](#_CPPv4N20bk_bt_gap_cb_param_t33bt_remove_bond_dev_cmpl_evt_paramE "bk_bt_gap_cb_param_t::bt_remove_bond_dev_cmpl_evt_param") remove_bond_dev_cmpl[](#_CPPv4N20bk_bt_gap_cb_param_t20remove_bond_dev_cmplE "永久链接至目标")
    :   Event parameter of BK_BT_GAP_REMOVE_BOND_DEV_COMPLETE_EVT

    struct [bk_bt_gap_cb_param_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[qos_cmpl_param](#_CPPv4N20bk_bt_gap_cb_param_t14qos_cmpl_paramE "bk_bt_gap_cb_param_t::qos_cmpl_param") qos_cmpl[](#_CPPv4N20bk_bt_gap_cb_param_t8qos_cmplE "永久链接至目标")
    :   QoS complete parameter struct

    struct [bk_bt_gap_cb_param_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[acl_conn_cmpl_stat_param](#_CPPv4N20bk_bt_gap_cb_param_t24acl_conn_cmpl_stat_paramE "bk_bt_gap_cb_param_t::acl_conn_cmpl_stat_param") acl_conn_cmpl_stat[](#_CPPv4N20bk_bt_gap_cb_param_t18acl_conn_cmpl_statE "永久链接至目标")
    :   ACL connection complete status parameter struct

    struct [bk_bt_gap_cb_param_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[acl_disconn_cmpl_stat_param](#_CPPv4N20bk_bt_gap_cb_param_t27acl_disconn_cmpl_stat_paramE "bk_bt_gap_cb_param_t::acl_disconn_cmpl_stat_param") acl_disconn_cmpl_stat[](#_CPPv4N20bk_bt_gap_cb_param_t21acl_disconn_cmpl_statE "永久链接至目标")
    :   ACL disconnection complete status parameter struct

    struct [bk_bt_gap_cb_param_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[link_key_notif_param](#_CPPv4N20bk_bt_gap_cb_param_t20link_key_notif_paramE "bk_bt_gap_cb_param_t::link_key_notif_param") link_key_notif[](#_CPPv4N20bk_bt_gap_cb_param_t14link_key_notifE "永久链接至目标")
    :   link key notif parameter struct

    struct [bk_bt_gap_cb_param_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[link_key_req_param](#_CPPv4N20bk_bt_gap_cb_param_t18link_key_req_paramE "bk_bt_gap_cb_param_t::link_key_req_param") link_key_req[](#_CPPv4N20bk_bt_gap_cb_param_t12link_key_reqE "永久链接至目标")
    :   link key request parameter struct

    struct [bk_bt_gap_cb_param_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[auto_sniff_cmpl_param](#_CPPv4N20bk_bt_gap_cb_param_t21auto_sniff_cmpl_paramE "bk_bt_gap_cb_param_t::auto_sniff_cmpl_param") auto_sniff_cmpl[](#_CPPv4N20bk_bt_gap_cb_param_t15auto_sniff_cmplE "永久链接至目标")

    struct acl_conn_cmpl_stat_param[](#_CPPv4N20bk_bt_gap_cb_param_t24acl_conn_cmpl_stat_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_bt_types.h>*

        BK_BT_GAP_ACL_CONN_CMPL_STAT_EVT.

        Public Members

        [bk_bt_status_t](dual_ble.md#_CPPv414bk_bt_status_t "bk_bt_status_t") stat[](#_CPPv4N20bk_bt_gap_cb_param_t24acl_conn_cmpl_stat_param4statE "永久链接至目标")
        :   ACL connection status

        uint16_t handle[](#_CPPv4N20bk_bt_gap_cb_param_t24acl_conn_cmpl_stat_param6handleE "永久链接至目标")
        :   ACL connection handle

        [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bda[](#_CPPv4N20bk_bt_gap_cb_param_t24acl_conn_cmpl_stat_param3bdaE "永久链接至目标")
        :   remote bluetooth device address

        uint32_t cod[](#_CPPv4N20bk_bt_gap_cb_param_t24acl_conn_cmpl_stat_param3codE "永久链接至目标")
        :   Class of Device for remote bluetooth device, it is only valid when paged by remote bluetooth device

    struct acl_disconn_cmpl_stat_param[](#_CPPv4N20bk_bt_gap_cb_param_t27acl_disconn_cmpl_stat_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_bt_types.h>*

        BK_BT_GAP_ACL_DISCONN_CMPL_STAT_EVT.

        Public Members

        [bk_bt_status_t](dual_ble.md#_CPPv414bk_bt_status_t "bk_bt_status_t") reason[](#_CPPv4N20bk_bt_gap_cb_param_t27acl_disconn_cmpl_stat_param6reasonE "永久链接至目标")
        :   ACL disconnection reason

        uint16_t handle[](#_CPPv4N20bk_bt_gap_cb_param_t27acl_disconn_cmpl_stat_param6handleE "永久链接至目标")
        :   ACL connection handle

        [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bda[](#_CPPv4N20bk_bt_gap_cb_param_t27acl_disconn_cmpl_stat_param3bdaE "永久链接至目标")
        :   remote bluetooth device address

    struct auth_cmpl_param[](#_CPPv4N20bk_bt_gap_cb_param_t15auth_cmpl_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_bt_types.h>*

        BK_BT_GAP_AUTH_CMPL_EVT.

        Public Members

        [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bda[](#_CPPv4N20bk_bt_gap_cb_param_t15auth_cmpl_param3bdaE "永久链接至目标")
        :   remote bluetooth device address

        [bk_bt_status_t](dual_ble.md#_CPPv414bk_bt_status_t "bk_bt_status_t") stat[](#_CPPv4N20bk_bt_gap_cb_param_t15auth_cmpl_param4statE "永久链接至目标")
        :   authentication complete status

    struct auto_sniff_cmpl_param[](#_CPPv4N20bk_bt_gap_cb_param_t21auto_sniff_cmpl_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_bt_types.h>*

        BK_BT_GAP_SET_AUTO_SNIFF_CMPL_EVT.

        Public Members

        [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bda[](#_CPPv4N20bk_bt_gap_cb_param_t21auto_sniff_cmpl_param3bdaE "永久链接至目标")

        [bk_bt_status_t](dual_ble.md#_CPPv414bk_bt_status_t "bk_bt_status_t") result[](#_CPPv4N20bk_bt_gap_cb_param_t21auto_sniff_cmpl_param6resultE "永久链接至目标")
        :   peer addr

    struct bt_remove_bond_dev_cmpl_evt_param[](#_CPPv4N20bk_bt_gap_cb_param_t33bt_remove_bond_dev_cmpl_evt_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_bt_types.h>*

        BK_BT_GAP_REMOVE_BOND_DEV_COMPLETE_EVT.

        Public Members

        [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bda[](#_CPPv4N20bk_bt_gap_cb_param_t33bt_remove_bond_dev_cmpl_evt_param3bdaE "永久链接至目标")
        :   remote bluetooth device address

        [bk_bt_status_t](dual_ble.md#_CPPv414bk_bt_status_t "bk_bt_status_t") status[](#_CPPv4N20bk_bt_gap_cb_param_t33bt_remove_bond_dev_cmpl_evt_param6statusE "永久链接至目标")
        :   Indicate the remove bond device operation success status

    struct cfm_req_param[](#_CPPv4N20bk_bt_gap_cb_param_t13cfm_req_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_bt_types.h>*

        BK_BT_GAP_CFM_REQ_EVT.

        Public Members

        [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bda[](#_CPPv4N20bk_bt_gap_cb_param_t13cfm_req_param3bdaE "永久链接至目标")
        :   remote bluetooth device address

        uint32_t num_val[](#_CPPv4N20bk_bt_gap_cb_param_t13cfm_req_param7num_valE "永久链接至目标")
        :   the numeric value for comparison.

    struct config_eir_data_param[](#_CPPv4N20bk_bt_gap_cb_param_t21config_eir_data_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_bt_types.h>*

        BK_BT_GAP_CONFIG_EIR_DATA_EVT *.

        Public Members

        [bk_bt_status_t](dual_ble.md#_CPPv414bk_bt_status_t "bk_bt_status_t") stat[](#_CPPv4N20bk_bt_gap_cb_param_t21config_eir_data_param4statE "永久链接至目标")
        :   config EIR status: BK_BT_STATUS_SUCCESS: config success BK_BT_STATUS_EIR_TOO_LARGE: the EIR data is more than 240B. The EIR may not contain the whole data. others: failed

        uint8_t eir_type_num[](#_CPPv4N20bk_bt_gap_cb_param_t21config_eir_data_param12eir_type_numE "永久链接至目标")
        :   the number of EIR types in EIR type

        [bk_bt_eir_type_t](#_CPPv416bk_bt_eir_type_t "bk_bt_eir_type_t") eir_type[BK_BT_EIR_TYPE_MAX_NUM][](#_CPPv4N20bk_bt_gap_cb_param_t21config_eir_data_param8eir_typeE "永久链接至目标")
        :   EIR types in EIR type

    struct disc_res_param[](#_CPPv4N20bk_bt_gap_cb_param_t14disc_res_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_bt_types.h>*

        BK_BT_GAP_DISC_RES_EVT.

        Public Members

        [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bda[](#_CPPv4N20bk_bt_gap_cb_param_t14disc_res_param3bdaE "永久链接至目标")
        :   remote bluetooth device address

        int num_prop[](#_CPPv4N20bk_bt_gap_cb_param_t14disc_res_param8num_propE "永久链接至目标")
        :   number of properties got

        [bk_bt_gap_dev_prop_t](#_CPPv420bk_bt_gap_dev_prop_t "bk_bt_gap_dev_prop_t") *prop[](#_CPPv4N20bk_bt_gap_cb_param_t14disc_res_param4propE "永久链接至目标")
        :   properties discovered from the new device

    struct disc_state_changed_param[](#_CPPv4N20bk_bt_gap_cb_param_t24disc_state_changed_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_bt_types.h>*

        BK_BT_GAP_DISC_STATE_CHANGED_EVT.

        Public Members

        [bk_bt_gap_discovery_state_t](#_CPPv427bk_bt_gap_discovery_state_t "bk_bt_gap_discovery_state_t") state[](#_CPPv4N20bk_bt_gap_cb_param_t24disc_state_changed_param5stateE "永久链接至目标")
        :   discovery state

    struct key_notif_param[](#_CPPv4N20bk_bt_gap_cb_param_t15key_notif_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_bt_types.h>*

        BK_BT_GAP_KEY_NOTIF_EVT.

        Public Members

        [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bda[](#_CPPv4N20bk_bt_gap_cb_param_t15key_notif_param3bdaE "永久链接至目标")
        :   remote bluetooth device address

        uint32_t passkey[](#_CPPv4N20bk_bt_gap_cb_param_t15key_notif_param7passkeyE "永久链接至目标")
        :   the numeric value for passkey entry.

    struct key_req_param[](#_CPPv4N20bk_bt_gap_cb_param_t13key_req_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_bt_types.h>*

        BK_BT_GAP_KEY_REQ_EVT.

        Public Members

        [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bda[](#_CPPv4N20bk_bt_gap_cb_param_t13key_req_param3bdaE "永久链接至目标")
        :   remote bluetooth device address

    struct link_key_notif_param[](#_CPPv4N20bk_bt_gap_cb_param_t20link_key_notif_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_bt_types.h>*

        BK_BT_GAP_LINK_KEY_NOTIF_EVT.

        Public Members

        [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bda[](#_CPPv4N20bk_bt_gap_cb_param_t20link_key_notif_param3bdaE "永久链接至目标")
        :   remote bluetooth device address

        uint8_t link_key[16][](#_CPPv4N20bk_bt_gap_cb_param_t20link_key_notif_param8link_keyE "永久链接至目标")
        :   Link Key for the associated bda.

    struct link_key_req_param[](#_CPPv4N20bk_bt_gap_cb_param_t18link_key_req_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_bt_types.h>*

        BK_BT_GAP_LINK_KEY_REQ_EVT.

        Public Members

        [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bda[](#_CPPv4N20bk_bt_gap_cb_param_t18link_key_req_param3bdaE "永久链接至目标")
        :   remote bluetooth device address

    struct mode_chg_param[](#_CPPv4N20bk_bt_gap_cb_param_t14mode_chg_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_bt_types.h>*

        BK_BT_GAP_MODE_CHG_EVT.

        Public Members

        [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bda[](#_CPPv4N20bk_bt_gap_cb_param_t14mode_chg_param3bdaE "永久链接至目标")
        :   remote bluetooth device address

        [bk_bt_pm_mode_t](#_CPPv415bk_bt_pm_mode_t "bk_bt_pm_mode_t") mode[](#_CPPv4N20bk_bt_gap_cb_param_t14mode_chg_param4modeE "永久链接至目标")
        :   PM mode

    struct pin_req_param[](#_CPPv4N20bk_bt_gap_cb_param_t13pin_req_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_bt_types.h>*

        BK_BT_GAP_PIN_REQ_EVT.

        Public Members

        [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bda[](#_CPPv4N20bk_bt_gap_cb_param_t13pin_req_param3bdaE "永久链接至目标")
        :   remote bluetooth device address

        bool min_16_digit[](#_CPPv4N20bk_bt_gap_cb_param_t13pin_req_param12min_16_digitE "永久链接至目标")
        :   TRUE if the pin returned must be at least 16 digits

    struct qos_cmpl_param[](#_CPPv4N20bk_bt_gap_cb_param_t14qos_cmpl_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_bt_types.h>*

        BK_BT_GAP_QOS_CMPL_EVT.

        Public Members

        [bk_bt_status_t](dual_ble.md#_CPPv414bk_bt_status_t "bk_bt_status_t") stat[](#_CPPv4N20bk_bt_gap_cb_param_t14qos_cmpl_param4statE "永久链接至目标")
        :   QoS status

        [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bda[](#_CPPv4N20bk_bt_gap_cb_param_t14qos_cmpl_param3bdaE "永久链接至目标")
        :   remote bluetooth device address

        uint32_t t_poll[](#_CPPv4N20bk_bt_gap_cb_param_t14qos_cmpl_param6t_pollE "永久链接至目标")
        :   poll interval, the maximum time between transmissions which from the master to a particular slave on the ACL logical transport. unit is 0.625ms.

    struct read_rmt_name_param[](#_CPPv4N20bk_bt_gap_cb_param_t19read_rmt_name_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_bt_types.h>*

        BK_BT_GAP_READ_REMOTE_NAME_EVT.

        Public Members

        [bk_bt_status_t](dual_ble.md#_CPPv414bk_bt_status_t "bk_bt_status_t") stat[](#_CPPv4N20bk_bt_gap_cb_param_t19read_rmt_name_param4statE "永久链接至目标")
        :   read Remote Name status

        uint8_t rmt_name[BK_BT_GAP_MAX_BDNAME_LEN + 1][](#_CPPv4N20bk_bt_gap_cb_param_t19read_rmt_name_param8rmt_nameE "永久链接至目标")
        :   Remote device name

        [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bda[](#_CPPv4N20bk_bt_gap_cb_param_t19read_rmt_name_param3bdaE "永久链接至目标")
        :   remote bluetooth device address

    struct read_rssi_delta_param[](#_CPPv4N20bk_bt_gap_cb_param_t21read_rssi_delta_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_bt_types.h>*

        BK_BT_GAP_READ_RSSI_DELTA_EVT *.

        Public Members

        [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bda[](#_CPPv4N20bk_bt_gap_cb_param_t21read_rssi_delta_param3bdaE "永久链接至目标")
        :   remote bluetooth device address

        [bk_bt_status_t](dual_ble.md#_CPPv414bk_bt_status_t "bk_bt_status_t") stat[](#_CPPv4N20bk_bt_gap_cb_param_t21read_rssi_delta_param4statE "永久链接至目标")
        :   read rssi status

        int8_t rssi_delta[](#_CPPv4N20bk_bt_gap_cb_param_t21read_rssi_delta_param10rssi_deltaE "永久链接至目标")
        :   rssi delta value range -128 ~127, The value zero indicates that the RSSI is inside the Golden Receive Power Range, the Golden Receive Power Range is from BK_BT_GAP_RSSI_LOW_THRLD to BK_BT_GAP_RSSI_HIGH_THRLD

    struct rmt_srvc_rec_param[](#_CPPv4N20bk_bt_gap_cb_param_t18rmt_srvc_rec_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_bt_types.h>*

        BK_BT_GAP_RMT_SRVC_REC_EVT.

        Public Members

        [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bda[](#_CPPv4N20bk_bt_gap_cb_param_t18rmt_srvc_rec_param3bdaE "永久链接至目标")
        :   remote bluetooth device address

        [bk_bt_status_t](dual_ble.md#_CPPv414bk_bt_status_t "bk_bt_status_t") stat[](#_CPPv4N20bk_bt_gap_cb_param_t18rmt_srvc_rec_param4statE "永久链接至目标")
        :   service search status

    struct rmt_srvcs_param[](#_CPPv4N20bk_bt_gap_cb_param_t15rmt_srvcs_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_bt_types.h>*

        BK_BT_GAP_RMT_SRVCS_EVT.

        Public Members

        [bk_bd_addr_t](dual_ble.md#_CPPv412bk_bd_addr_t "bk_bd_addr_t") bda[](#_CPPv4N20bk_bt_gap_cb_param_t15rmt_srvcs_param3bdaE "永久链接至目标")
        :   remote bluetooth device address

        [bk_bt_status_t](dual_ble.md#_CPPv414bk_bt_status_t "bk_bt_status_t") stat[](#_CPPv4N20bk_bt_gap_cb_param_t15rmt_srvcs_param4statE "永久链接至目标")
        :   service search status

        int num_uuids[](#_CPPv4N20bk_bt_gap_cb_param_t15rmt_srvcs_param9num_uuidsE "永久链接至目标")
        :   number of UUID in uuid_list

        [bk_bt_uuid_t](dual_ble.md#_CPPv412bk_bt_uuid_t "bk_bt_uuid_t") *uuid_list[](#_CPPv4N20bk_bt_gap_cb_param_t15rmt_srvcs_param9uuid_listE "永久链接至目标")
        :   list of service UUIDs of remote device

    struct set_afh_channels_param[](#_CPPv4N20bk_bt_gap_cb_param_t22set_afh_channels_paramE "永久链接至目标")
    :   *#include <bk_dm_gap_bt_types.h>*

        BK_BT_GAP_SET_AFH_CHANNELS_EVT.

        Public Members

        [bk_bt_status_t](dual_ble.md#_CPPv414bk_bt_status_t "bk_bt_status_t") stat[](#_CPPv4N20bk_bt_gap_cb_param_t22set_afh_channels_param4statE "永久链接至目标")
        :   set AFH channel status


### Structures[](#id45 "永久链接至标题")

struct bk_bt_gap_dev_prop_t[](#_CPPv420bk_bt_gap_dev_prop_t "永久链接至目标")
:   Bluetooth Device Property Descriptor.

    Public Members

    [bk_bt_gap_dev_prop_type_t](#_CPPv425bk_bt_gap_dev_prop_type_t "bk_bt_gap_dev_prop_type_t") type[](#_CPPv4N20bk_bt_gap_dev_prop_t4typeE "永久链接至目标")
    :   Device property type

    int len[](#_CPPv4N20bk_bt_gap_dev_prop_t3lenE "永久链接至目标")
    :   Device property value length

    void *val[](#_CPPv4N20bk_bt_gap_dev_prop_t3valE "永久链接至目标")
    :   Device property value

struct bk_bt_eir_data_t[](#_CPPv416bk_bt_eir_data_t "永久链接至目标")
:   EIR data content, according to “Supplement to the Bluetooth Core Specification”.

    Public Members

    bool fec_required[](#_CPPv4N16bk_bt_eir_data_t12fec_requiredE "永久链接至目标")
    :   FEC is required or not, true by default

    bool include_txpower[](#_CPPv4N16bk_bt_eir_data_t15include_txpowerE "永久链接至目标")
    :   EIR data include TX power, false by default

    bool include_uuid[](#_CPPv4N16bk_bt_eir_data_t12include_uuidE "永久链接至目标")
    :   EIR data include UUID, false by default

    uint8_t flag[](#_CPPv4N16bk_bt_eir_data_t4flagE "永久链接至目标")
    :   EIR flags, see BK_BT_EIR_FLAG for details, EIR will not include flag if it is 0, 0 by default

    uint16_t manufacturer_len[](#_CPPv4N16bk_bt_eir_data_t16manufacturer_lenE "永久链接至目标")
    :   Manufacturer data length, 0 by default

    uint8_t *p_manufacturer_data[](#_CPPv4N16bk_bt_eir_data_t19p_manufacturer_dataE "永久链接至目标")
    :   Manufacturer data point

    uint16_t url_len[](#_CPPv4N16bk_bt_eir_data_t7url_lenE "永久链接至目标")
    :   URL length, 0 by default

    uint8_t *p_url[](#_CPPv4N16bk_bt_eir_data_t5p_urlE "永久链接至目标")
    :   URL point

struct bk_bt_gap_sniff_config[](#_CPPv422bk_bt_gap_sniff_config "永久链接至目标")
:   bt sniff config

    Public Members

    uint16_t sniff_min_interval[](#_CPPv4N22bk_bt_gap_sniff_config18sniff_min_intervalE "永久链接至目标")
    :   unit 0.625ms, range: 1.25ms ~ 40.9s

    uint16_t sniff_attempt[](#_CPPv4N22bk_bt_gap_sniff_config13sniff_attemptE "永久链接至目标")
    :   unit 0.625ms, range: 1.25ms ~ 40.9s

    uint16_t sniff_timeout[](#_CPPv4N22bk_bt_gap_sniff_config13sniff_timeoutE "永久链接至目标")
    :   unit 1.25ms, range: 1.25ms ~ 40.9s


### Macros[](#id46 "永久链接至标题")

BK_BT_GAP_RSSI_HIGH_THRLD[](#c.BK_BT_GAP_RSSI_HIGH_THRLD "永久链接至目标")
:   RSSI threshold.

    High RSSI threshold

BK_BT_GAP_RSSI_LOW_THRLD[](#c.BK_BT_GAP_RSSI_LOW_THRLD "永久链接至目标")
:   Low RSSI threshold

BK_BT_GAP_AFH_CHANNELS_LEN[](#c.BK_BT_GAP_AFH_CHANNELS_LEN "永久链接至目标")

BK_BT_GAP_MAX_BDNAME_LEN[](#c.BK_BT_GAP_MAX_BDNAME_LEN "永久链接至目标")
:   Maximum bytes of Bluetooth device name.

BK_BT_GAP_EIR_DATA_LEN[](#c.BK_BT_GAP_EIR_DATA_LEN "永久链接至目标")
:   Maximum size of EIR Significant part.

BK_BT_EIR_TYPE_FLAGS[](#c.BK_BT_EIR_TYPE_FLAGS "永久链接至目标")
:   Extended Inquiry Response data type.

    Flag with information such as BR/EDR and LE support

BK_BT_EIR_TYPE_INCMPL_16BITS_UUID[](#c.BK_BT_EIR_TYPE_INCMPL_16BITS_UUID "永久链接至目标")
:   Incomplete list of 16-bit service UUIDs

BK_BT_EIR_TYPE_CMPL_16BITS_UUID[](#c.BK_BT_EIR_TYPE_CMPL_16BITS_UUID "永久链接至目标")
:   Complete list of 16-bit service UUIDs

BK_BT_EIR_TYPE_INCMPL_32BITS_UUID[](#c.BK_BT_EIR_TYPE_INCMPL_32BITS_UUID "永久链接至目标")
:   Incomplete list of 32-bit service UUIDs

BK_BT_EIR_TYPE_CMPL_32BITS_UUID[](#c.BK_BT_EIR_TYPE_CMPL_32BITS_UUID "永久链接至目标")
:   Complete list of 32-bit service UUIDs

BK_BT_EIR_TYPE_INCMPL_128BITS_UUID[](#c.BK_BT_EIR_TYPE_INCMPL_128BITS_UUID "永久链接至目标")
:   Incomplete list of 128-bit service UUIDs

BK_BT_EIR_TYPE_CMPL_128BITS_UUID[](#c.BK_BT_EIR_TYPE_CMPL_128BITS_UUID "永久链接至目标")
:   Complete list of 128-bit service UUIDs

BK_BT_EIR_TYPE_SHORT_LOCAL_NAME[](#c.BK_BT_EIR_TYPE_SHORT_LOCAL_NAME "永久链接至目标")
:   Shortened Local Name

BK_BT_EIR_TYPE_CMPL_LOCAL_NAME[](#c.BK_BT_EIR_TYPE_CMPL_LOCAL_NAME "永久链接至目标")
:   Complete Local Name

BK_BT_EIR_TYPE_TX_POWER_LEVEL[](#c.BK_BT_EIR_TYPE_TX_POWER_LEVEL "永久链接至目标")
:   Tx power level, value is 1 octet ranging from -127 to 127, unit is dBm

BK_BT_EIR_TYPE_URL[](#c.BK_BT_EIR_TYPE_URL "永久链接至目标")
:   Uniform resource identifier

BK_BT_EIR_TYPE_MANU_SPECIFIC[](#c.BK_BT_EIR_TYPE_MANU_SPECIFIC "永久链接至目标")
:   Manufacturer specific data

BK_BT_EIR_TYPE_MAX_NUM[](#c.BK_BT_EIR_TYPE_MAX_NUM "永久链接至目标")
:   MAX number of EIR type

BK_BT_EIR_FLAG_LIMIT_DISC[](#c.BK_BT_EIR_FLAG_LIMIT_DISC "永久链接至目标")

BK_BT_EIR_FLAG_GEN_DISC[](#c.BK_BT_EIR_FLAG_GEN_DISC "永久链接至目标")

BK_BT_EIR_FLAG_BREDR_NOT_SPT[](#c.BK_BT_EIR_FLAG_BREDR_NOT_SPT "永久链接至目标")

BK_BT_EIR_FLAG_DMT_CONTROLLER_SPT[](#c.BK_BT_EIR_FLAG_DMT_CONTROLLER_SPT "永久链接至目标")

BK_BT_EIR_FLAG_DMT_HOST_SPT[](#c.BK_BT_EIR_FLAG_DMT_HOST_SPT "永久链接至目标")

BK_BT_EIR_MAX_LEN[](#c.BK_BT_EIR_MAX_LEN "永久链接至目标")

BK_BT_PIN_CODE_LEN[](#c.BK_BT_PIN_CODE_LEN "永久链接至目标")
:   Max pin code length

BK_BT_IO_CAP_OUT[](#c.BK_BT_IO_CAP_OUT "永久链接至目标")
:   IO Capability Constants DisplayOnly

BK_BT_IO_CAP_IO[](#c.BK_BT_IO_CAP_IO "永久链接至目标")
:   DisplayYesNo

BK_BT_IO_CAP_IN[](#c.BK_BT_IO_CAP_IN "永久链接至目标")
:   KeyboardOnly

BK_BT_IO_CAP_NONE[](#c.BK_BT_IO_CAP_NONE "永久链接至目标")
:   NoInputNoOutput

BK_BT_PM_MD_ACTIVE[](#c.BK_BT_PM_MD_ACTIVE "永久链接至目标")
:   Active mode

BK_BT_PM_MD_HOLD[](#c.BK_BT_PM_MD_HOLD "永久链接至目标")
:   Hold mode

BK_BT_PM_MD_SNIFF[](#c.BK_BT_PM_MD_SNIFF "永久链接至目标")
:   Sniff mode

BK_BT_PM_MD_PARK[](#c.BK_BT_PM_MD_PARK "永久链接至目标")
:   Park state

BK_BT_COD_SRVC_BIT_MASK[](#c.BK_BT_COD_SRVC_BIT_MASK "永久链接至目标")
:   Bits of major service class field.

    Major service bit mask

BK_BT_COD_SRVC_BIT_OFFSET[](#c.BK_BT_COD_SRVC_BIT_OFFSET "永久链接至目标")
:   Major service bit offset

BK_BT_COD_MAJOR_DEV_BIT_MASK[](#c.BK_BT_COD_MAJOR_DEV_BIT_MASK "永久链接至目标")
:   Bits of major device class field.

    Major device bit mask

BK_BT_COD_MAJOR_DEV_BIT_OFFSET[](#c.BK_BT_COD_MAJOR_DEV_BIT_OFFSET "永久链接至目标")
:   Major device bit offset

BK_BT_COD_MINOR_DEV_BIT_MASK[](#c.BK_BT_COD_MINOR_DEV_BIT_MASK "永久链接至目标")
:   Bits of minor device class field.

    Minor device bit mask

BK_BT_COD_MINOR_DEV_BIT_OFFSET[](#c.BK_BT_COD_MINOR_DEV_BIT_OFFSET "永久链接至目标")
:   Minor device bit offset

BK_BT_COD_FORMAT_TYPE_BIT_MASK[](#c.BK_BT_COD_FORMAT_TYPE_BIT_MASK "永久链接至目标")
:   Bits of format type.

    Format type bit mask

BK_BT_COD_FORMAT_TYPE_BIT_OFFSET[](#c.BK_BT_COD_FORMAT_TYPE_BIT_OFFSET "永久链接至目标")
:   Format type bit offset

BK_BT_COD_FORMAT_TYPE_1[](#c.BK_BT_COD_FORMAT_TYPE_1 "永久链接至目标")
:   Class of device format type 1.

BK_BT_GAP_MIN_INQ_LEN[](#c.BK_BT_GAP_MIN_INQ_LEN "永久链接至目标")
:   Minimum and Maximum inquiry length Minimum inquiry duration, unit is 1.28s

BK_BT_GAP_MAX_INQ_LEN[](#c.BK_BT_GAP_MAX_INQ_LEN "永久链接至目标")
:   Maximum inquiry duration, unit is 1.28s


### Type Definitions[](#id47 "永久链接至标题")

typedef uint8_t bk_bt_gap_afh_channels[BK_BT_GAP_AFH_CHANNELS_LEN][](#_CPPv422bk_bt_gap_afh_channels "永久链接至目标")

typedef uint8_t bk_bt_eir_type_t[](#_CPPv416bk_bt_eir_type_t "永久链接至目标")

typedef uint8_t bk_bt_pin_code_t[BK_BT_PIN_CODE_LEN][](#_CPPv416bk_bt_pin_code_t "永久链接至目标")
:   Pin Code (upto 128 bits) MSB is 0

typedef uint8_t bk_bt_io_cap_t[](#_CPPv414bk_bt_io_cap_t "永久链接至目标")
:   Combination of the IO Capability

typedef uint8_t bk_bt_pm_mode_t[](#_CPPv415bk_bt_pm_mode_t "永久链接至目标")

typedef void (*bk_bt_gap_cb_t)([bk_gap_bt_cb_event_t](#_CPPv420bk_gap_bt_cb_event_t "bk_gap_bt_cb_event_t") event, [bk_bt_gap_cb_param_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t") *param)[](#_CPPv414bk_bt_gap_cb_t "永久链接至目标")
:   bluetooth GAP callback function type

    Param event
    :   : Event type

    Param param
    :   : Pointer to callback parameter


### Enumerations[](#id48 "永久链接至标题")

enum bk_bt_cod_mode_t[](#_CPPv416bk_bt_cod_mode_t "永久链接至目标")
:   class of device settings


    *Values:*

    enumerator BK_BT_SET_COD_MAJOR_MINOR[](#_CPPv4N16bk_bt_cod_mode_t25BK_BT_SET_COD_MAJOR_MINORE "永久链接至目标")
    :   overwrite major, minor class

    enumerator BK_BT_SET_COD_SERVICE_CLASS[](#_CPPv4N16bk_bt_cod_mode_t27BK_BT_SET_COD_SERVICE_CLASSE "永久链接至目标")
    :   set the bits in the input, the current bit will remain

    enumerator BK_BT_CLR_COD_SERVICE_CLASS[](#_CPPv4N16bk_bt_cod_mode_t27BK_BT_CLR_COD_SERVICE_CLASSE "永久链接至目标")
    :   clear the bits in the input, others will remain

    enumerator BK_BT_SET_COD_ALL[](#_CPPv4N16bk_bt_cod_mode_t17BK_BT_SET_COD_ALLE "永久链接至目标")
    :   overwrite major, minor, set the bits in service class

    enumerator BK_BT_INIT_COD[](#_CPPv4N16bk_bt_cod_mode_t14BK_BT_INIT_CODE "永久链接至目标")
    :   overwrite major, minor, and service class

enum bk_bt_gap_dev_prop_type_t[](#_CPPv425bk_bt_gap_dev_prop_type_t "永久链接至目标")
:   Bluetooth Device Property type.


    *Values:*

    enumerator BK_BT_GAP_DEV_PROP_BDNAME[](#_CPPv4N25bk_bt_gap_dev_prop_type_t25BK_BT_GAP_DEV_PROP_BDNAMEE "永久链接至目标")
    :   Bluetooth device name, value type is int8_t []

    enumerator BK_BT_GAP_DEV_PROP_COD[](#_CPPv4N25bk_bt_gap_dev_prop_type_t22BK_BT_GAP_DEV_PROP_CODE "永久链接至目标")
    :   Class of Device, value type is uint32_t

    enumerator BK_BT_GAP_DEV_PROP_RSSI[](#_CPPv4N25bk_bt_gap_dev_prop_type_t23BK_BT_GAP_DEV_PROP_RSSIE "永久链接至目标")
    :   Received Signal strength Indication, value type is int8_t, ranging from -128 to 127

    enumerator BK_BT_GAP_DEV_PROP_EIR[](#_CPPv4N25bk_bt_gap_dev_prop_type_t22BK_BT_GAP_DEV_PROP_EIRE "永久链接至目标")
    :   Extended Inquiry Response, value type is uint8_t []

enum bk_bt_cod_srvc_t[](#_CPPv416bk_bt_cod_srvc_t "永久链接至目标")
:   Major service class field of Class of Device, mutiple bits can be set.


    *Values:*

    enumerator BK_BT_COD_SRVC_NONE[](#_CPPv4N16bk_bt_cod_srvc_t19BK_BT_COD_SRVC_NONEE "永久链接至目标")
    :   None indicates an invalid value

    enumerator BK_BT_COD_SRVC_LMTD_DISCOVER[](#_CPPv4N16bk_bt_cod_srvc_t28BK_BT_COD_SRVC_LMTD_DISCOVERE "永久链接至目标")
    :   Limited Discoverable Mode

    enumerator BK_BT_COD_SRVC_POSITIONING[](#_CPPv4N16bk_bt_cod_srvc_t26BK_BT_COD_SRVC_POSITIONINGE "永久链接至目标")
    :   Positioning (Location identification)

    enumerator BK_BT_COD_SRVC_NETWORKING[](#_CPPv4N16bk_bt_cod_srvc_t25BK_BT_COD_SRVC_NETWORKINGE "永久链接至目标")
    :   Networking, e.g. LAN, Ad hoc

    enumerator BK_BT_COD_SRVC_RENDERING[](#_CPPv4N16bk_bt_cod_srvc_t24BK_BT_COD_SRVC_RENDERINGE "永久链接至目标")
    :   Rendering, e.g. Printing, Speakers

    enumerator BK_BT_COD_SRVC_CAPTURING[](#_CPPv4N16bk_bt_cod_srvc_t24BK_BT_COD_SRVC_CAPTURINGE "永久链接至目标")
    :   Capturing, e.g. Scanner, Microphone

    enumerator BK_BT_COD_SRVC_OBJ_TRANSFER[](#_CPPv4N16bk_bt_cod_srvc_t27BK_BT_COD_SRVC_OBJ_TRANSFERE "永久链接至目标")
    :   Object Transfer, e.g. v-Inbox, v-Folder

    enumerator BK_BT_COD_SRVC_AUDIO[](#_CPPv4N16bk_bt_cod_srvc_t20BK_BT_COD_SRVC_AUDIOE "永久链接至目标")
    :   Audio, e.g. Speaker, Microphone, Headset service

    enumerator BK_BT_COD_SRVC_TELEPHONY[](#_CPPv4N16bk_bt_cod_srvc_t24BK_BT_COD_SRVC_TELEPHONYE "永久链接至目标")
    :   Telephony, e.g. Cordless telephony, Modem, Headset service

    enumerator BK_BT_COD_SRVC_INFORMATION[](#_CPPv4N16bk_bt_cod_srvc_t26BK_BT_COD_SRVC_INFORMATIONE "永久链接至目标")
    :   Information, e.g., WEB-server, WAP-server

enum bk_bt_pin_type_t[](#_CPPv416bk_bt_pin_type_t "永久链接至目标")
:   *Values:*

    enumerator BK_BT_PIN_TYPE_VARIABLE[](#_CPPv4N16bk_bt_pin_type_t23BK_BT_PIN_TYPE_VARIABLEE "永久链接至目标")
    :   Refer to BTM_PIN_TYPE_VARIABLE

    enumerator BK_BT_PIN_TYPE_FIXED[](#_CPPv4N16bk_bt_pin_type_t20BK_BT_PIN_TYPE_FIXEDE "永久链接至目标")
    :   Refer to BTM_PIN_TYPE_FIXED

enum bk_bt_sp_param_t[](#_CPPv416bk_bt_sp_param_t "永久链接至目标")
:   *Values:*

    enumerator BK_BT_SP_IOCAP_MODE[](#_CPPv4N16bk_bt_sp_param_t19BK_BT_SP_IOCAP_MODEE "永久链接至目标")
    :   Set IO mode

enum bk_bt_cod_major_dev_t[](#_CPPv421bk_bt_cod_major_dev_t "永久链接至目标")
:   Major device class field of Class of Device.


    *Values:*

    enumerator BK_BT_COD_MAJOR_DEV_MISC[](#_CPPv4N21bk_bt_cod_major_dev_t24BK_BT_COD_MAJOR_DEV_MISCE "永久链接至目标")
    :   Miscellaneous

    enumerator BK_BT_COD_MAJOR_DEV_COMPUTER[](#_CPPv4N21bk_bt_cod_major_dev_t28BK_BT_COD_MAJOR_DEV_COMPUTERE "永久链接至目标")
    :   Computer

    enumerator BK_BT_COD_MAJOR_DEV_PHONE[](#_CPPv4N21bk_bt_cod_major_dev_t25BK_BT_COD_MAJOR_DEV_PHONEE "永久链接至目标")
    :   Phone(cellular, cordless, pay phone, modem

    enumerator BK_BT_COD_MAJOR_DEV_LAN_NAP[](#_CPPv4N21bk_bt_cod_major_dev_t27BK_BT_COD_MAJOR_DEV_LAN_NAPE "永久链接至目标")
    :   LAN, Network Access Point

    enumerator BK_BT_COD_MAJOR_DEV_AV[](#_CPPv4N21bk_bt_cod_major_dev_t22BK_BT_COD_MAJOR_DEV_AVE "永久链接至目标")
    :   Audio/Video(headset, speaker, stereo, video display, VCR

    enumerator BK_BT_COD_MAJOR_DEV_PERIPHERAL[](#_CPPv4N21bk_bt_cod_major_dev_t30BK_BT_COD_MAJOR_DEV_PERIPHERALE "永久链接至目标")
    :   Peripheral(mouse, joystick, keyboard)

    enumerator BK_BT_COD_MAJOR_DEV_IMAGING[](#_CPPv4N21bk_bt_cod_major_dev_t27BK_BT_COD_MAJOR_DEV_IMAGINGE "永久链接至目标")
    :   Imaging(printer, scanner, camera, display

    enumerator BK_BT_COD_MAJOR_DEV_WEARABLE[](#_CPPv4N21bk_bt_cod_major_dev_t28BK_BT_COD_MAJOR_DEV_WEARABLEE "永久链接至目标")
    :   Wearable

    enumerator BK_BT_COD_MAJOR_DEV_TOY[](#_CPPv4N21bk_bt_cod_major_dev_t23BK_BT_COD_MAJOR_DEV_TOYE "永久链接至目标")
    :   Toy

    enumerator BK_BT_COD_MAJOR_DEV_HEALTH[](#_CPPv4N21bk_bt_cod_major_dev_t26BK_BT_COD_MAJOR_DEV_HEALTHE "永久链接至目标")
    :   Health

    enumerator BK_BT_COD_MAJOR_DEV_UNCATEGORIZED[](#_CPPv4N21bk_bt_cod_major_dev_t33BK_BT_COD_MAJOR_DEV_UNCATEGORIZEDE "永久链接至目标")
    :   Uncategorized: device not specified

enum bk_bt_gap_discovery_state_t[](#_CPPv427bk_bt_gap_discovery_state_t "永久链接至目标")
:   Bluetooth Device Discovery state


    *Values:*

    enumerator BK_BT_GAP_DISCOVERY_STOPPED[](#_CPPv4N27bk_bt_gap_discovery_state_t27BK_BT_GAP_DISCOVERY_STOPPEDE "永久链接至目标")
    :   Device discovery stopped

    enumerator BK_BT_GAP_DISCOVERY_STARTED[](#_CPPv4N27bk_bt_gap_discovery_state_t27BK_BT_GAP_DISCOVERY_STARTEDE "永久链接至目标")
    :   Device discovery started

enum bk_gap_bt_cb_event_t[](#_CPPv420bk_gap_bt_cb_event_t "永久链接至目标")
:   BT GAP callback events.


    *Values:*

    enumerator BK_BT_GAP_DISC_RES_EVT[](#_CPPv4N20bk_gap_bt_cb_event_t22BK_BT_GAP_DISC_RES_EVTE "永久链接至目标")
    :   Device discovery result event

    enumerator BK_BT_GAP_DISC_STATE_CHANGED_EVT[](#_CPPv4N20bk_gap_bt_cb_event_t32BK_BT_GAP_DISC_STATE_CHANGED_EVTE "永久链接至目标")
    :   Discovery state changed event

    enumerator BK_BT_GAP_RMT_SRVCS_EVT[](#_CPPv4N20bk_gap_bt_cb_event_t23BK_BT_GAP_RMT_SRVCS_EVTE "永久链接至目标")
    :   Get remote services event

    enumerator BK_BT_GAP_RMT_SRVC_REC_EVT[](#_CPPv4N20bk_gap_bt_cb_event_t26BK_BT_GAP_RMT_SRVC_REC_EVTE "永久链接至目标")
    :   Get remote service record event

    enumerator BK_BT_GAP_AUTH_CMPL_EVT[](#_CPPv4N20bk_gap_bt_cb_event_t23BK_BT_GAP_AUTH_CMPL_EVTE "永久链接至目标")
    :   Authentication complete event

    enumerator BK_BT_GAP_PIN_REQ_EVT[](#_CPPv4N20bk_gap_bt_cb_event_t21BK_BT_GAP_PIN_REQ_EVTE "永久链接至目标")
    :   Legacy Pairing Pin code request

    enumerator BK_BT_GAP_CFM_REQ_EVT[](#_CPPv4N20bk_gap_bt_cb_event_t21BK_BT_GAP_CFM_REQ_EVTE "永久链接至目标")
    :   Security Simple Pairing User Confirmation request.

    enumerator BK_BT_GAP_KEY_NOTIF_EVT[](#_CPPv4N20bk_gap_bt_cb_event_t23BK_BT_GAP_KEY_NOTIF_EVTE "永久链接至目标")
    :   Security Simple Pairing Passkey Notification

    enumerator BK_BT_GAP_KEY_REQ_EVT[](#_CPPv4N20bk_gap_bt_cb_event_t21BK_BT_GAP_KEY_REQ_EVTE "永久链接至目标")
    :   Security Simple Pairing Passkey request

    enumerator BK_BT_GAP_READ_RSSI_DELTA_EVT[](#_CPPv4N20bk_gap_bt_cb_event_t29BK_BT_GAP_READ_RSSI_DELTA_EVTE "永久链接至目标")
    :   Read rssi event

    enumerator BK_BT_GAP_CONFIG_EIR_DATA_EVT[](#_CPPv4N20bk_gap_bt_cb_event_t29BK_BT_GAP_CONFIG_EIR_DATA_EVTE "永久链接至目标")
    :   Config EIR data event

    enumerator BK_BT_GAP_SET_AFH_CHANNELS_EVT[](#_CPPv4N20bk_gap_bt_cb_event_t30BK_BT_GAP_SET_AFH_CHANNELS_EVTE "永久链接至目标")
    :   Set AFH channels event

    enumerator BK_BT_GAP_READ_REMOTE_NAME_EVT[](#_CPPv4N20bk_gap_bt_cb_event_t30BK_BT_GAP_READ_REMOTE_NAME_EVTE "永久链接至目标")
    :   Read Remote Name event

    enumerator BK_BT_GAP_MODE_CHG_EVT[](#_CPPv4N20bk_gap_bt_cb_event_t22BK_BT_GAP_MODE_CHG_EVTE "永久链接至目标")

    enumerator BK_BT_GAP_REMOVE_BOND_DEV_COMPLETE_EVT[](#_CPPv4N20bk_gap_bt_cb_event_t38BK_BT_GAP_REMOVE_BOND_DEV_COMPLETE_EVTE "永久链接至目标")
    :   remove bond device complete event

    enumerator BK_BT_GAP_QOS_CMPL_EVT[](#_CPPv4N20bk_gap_bt_cb_event_t22BK_BT_GAP_QOS_CMPL_EVTE "永久链接至目标")
    :   QOS complete event

    enumerator BK_BT_GAP_ACL_CONN_CMPL_STAT_EVT[](#_CPPv4N20bk_gap_bt_cb_event_t32BK_BT_GAP_ACL_CONN_CMPL_STAT_EVTE "永久链接至目标")
    :   ACL connection complete status event

    enumerator BK_BT_GAP_ACL_DISCONN_CMPL_STAT_EVT[](#_CPPv4N20bk_gap_bt_cb_event_t35BK_BT_GAP_ACL_DISCONN_CMPL_STAT_EVTE "永久链接至目标")
    :   ACL disconnection complete status event

    enumerator BK_BT_GAP_LINK_KEY_NOTIF_EVT[](#_CPPv4N20bk_gap_bt_cb_event_t28BK_BT_GAP_LINK_KEY_NOTIF_EVTE "永久链接至目标")
    :   Link Key Notification

    enumerator BK_BT_GAP_LINK_KEY_REQ_EVT[](#_CPPv4N20bk_gap_bt_cb_event_t26BK_BT_GAP_LINK_KEY_REQ_EVTE "永久链接至目标")
    :   Link Key request

    enumerator BK_BT_GAP_SET_AUTO_SNIFF_CMPL_EVT[](#_CPPv4N20bk_gap_bt_cb_event_t33BK_BT_GAP_SET_AUTO_SNIFF_CMPL_EVTE "永久链接至目标")

    enumerator BK_BT_GAP_EVT_MAX[](#_CPPv4N20bk_gap_bt_cb_event_t17BK_BT_GAP_EVT_MAXE "永久链接至目标")
    :   set auto entry sniff req completed event

enum bk_bt_inq_mode_t[](#_CPPv416bk_bt_inq_mode_t "永久链接至目标")
:   Inquiry Mode


    *Values:*

    enumerator BK_BT_INQ_MODE_GENERAL_INQUIRY[](#_CPPv4N16bk_bt_inq_mode_t30BK_BT_INQ_MODE_GENERAL_INQUIRYE "永久链接至目标")
    :   General inquiry mode

    enumerator BK_BT_INQ_MODE_LIMITED_INQUIRY[](#_CPPv4N16bk_bt_inq_mode_t30BK_BT_INQ_MODE_LIMITED_INQUIRYE "永久链接至目标")
    :   Limited inquiry mode


## Reference link[](#reference-link "永久链接至标题")

> [API Reference :](../bluetooth.md "../../api-reference/bluetooth/index.md") Introduced the Bluetooth API interface
