# DM BT APIs[](#dm-bt-apis "永久链接至标题")

[[English]](../../../../en/v1.5/api-reference/bluetooth/dm_bt.html "../../../../en/v1.5/api-reference/bluetooth/dm_bt.html")

重要

The DM BT API v1.0 is the lastest stable DM BT APIs. All new applications should use DM BT API v1.0.


## DM BT API Categories[](#dm-bt-api-categories "永久链接至标题")

Most of DM BT APIs can be categoried as:

Interface specific DM BT APIs:
:   - BT common interface

    - BT A2DP Sink interface


## Application Example[](#application-example "永久链接至标题")

Check [projects/lvgl/soundbar](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/projects/lvgl/soundbar "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/projects/lvgl/soundbar") folder, which contains the following application:


- There is a A2DP sink client demo. This demo can be discovered and connected by A2DP source device and receive the audio stream from remote device


## API Reference[](#api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [dm_bt.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/dm_bt.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/dm_bt.h")


### Functions[](#functions "永久链接至标题")

bt_err_t bk_bt_gap_set_event_callback([bt_event_cb_t](#_CPPv413bt_event_cb_t "bt_event_cb_t") func)[](#_CPPv428bk_bt_gap_set_event_callback13bt_event_cb_t "永久链接至目标")
:   sets BT event callback function

    参数
    :   **func** – **[in]** : callback

    返回
    :   - BK_ERR_BT_SUCCESS : Succeed

        - BK_ERR_BT_FAIL: others

bt_err_t bk_bt_gap_linkkey_reply(uint8_t is_exist, [bk_bt_linkkey_storage_t](#_CPPv423bk_bt_linkkey_storage_t "bk_bt_linkkey_storage_t") *key)[](#_CPPv423bk_bt_gap_linkkey_reply7uint8_tP23bk_bt_linkkey_storage_t "永久链接至目标")
:   send linkkey when peer need authentication


    **Attention**
    :   key->addr must be valued

    参数
    :   - **is_exist** – **[in]** : if linkkey exist. If no exist, peer may trigger pair procedure

        - **key** – **[in]** : linkkey,

    返回
    :   - BK_ERR_BT_SUCCESS : Succeed

        - BK_ERR_BT_FAIL: others

bt_err_t bk_bt_gap_set_visibility([bk_bt_conn_mode_t](#_CPPv417bk_bt_conn_mode_t "bk_bt_conn_mode_t") conn_mode, [bk_bt_disc_mode_t](#_CPPv417bk_bt_disc_mode_t "bk_bt_disc_mode_t") disc_mode)[](#_CPPv424bk_bt_gap_set_visibility17bk_bt_conn_mode_t17bk_bt_disc_mode_t "永久链接至目标")
:   sets the Bluetooth connectable, discoverable

    参数
    :   - **conn_mode** – **[in]** : one of the enums of bk_bt_conn_mode_t

        - **disc_mode** – **[in]** : one of the enums of bk_bt_disc_mode_t

    返回
    :   - BK_ERR_BT_SUCCESS : Succeed

        - BK_ERR_BT_FAIL: others

bt_err_t bk_bt_gap_set_device_class(uint32_t cod)[](#_CPPv426bk_bt_gap_set_device_class8uint32_t "永久链接至目标")
:   set the class of device

    参见

    enum common_cod_t)

    参数
    :   **cod, :** – **[in]** Class of Device for the device(

    返回
    :   - BK_ERR_BT_SUCCESS: succeed

        - others: fail

bt_err_t bk_bt_gap_set_local_name(uint8_t *name, uint8_t len)[](#_CPPv424bk_bt_gap_set_local_nameP7uint8_t7uint8_t "永久链接至目标")
:   set the local name

    参数
    :   - **name, :** – **[in]** pointer of name

        - **len, :** – **[in]** the length of name

    返回
    :   - BK_ERR_BT_SUCCESS: succeed

        - others: fail

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_bt_gap_start_discovery([bk_bt_inq_mode_t](#_CPPv416bk_bt_inq_mode_t "bk_bt_inq_mode_t") mode, uint8_t inq_len, uint8_t num_rsps)[](#_CPPv425bk_bt_gap_start_discovery16bk_bt_inq_mode_t7uint8_t7uint8_t "永久链接至目标")
:   This function starts Inquiry and Name Discovery. This function should be called after esp_bluedroid_enable() completes successfully. When Inquiry is halted and cached results do not contain device name, then Name Discovery will connect to the peer target to get the device name. bk_bt_gap_cb_t will be called with BK_DM_BT_GAP_DISC_STATE_CHANGED_EVT when Inquiry is started or Name Discovery is completed. bk_bt_gap_cb_t will be called with BK_DM_BT_GAP_DISC_RES_EVT each time the two types of discovery results are got.

    参数
    :   - **mode** – **[in]** - Inquiry mode

        - **inq_len** – **[in]** - Inquiry duration in 1.28 sec units, ranging from 0x01 to 0x30. This parameter only specifies the total duration of the Inquiry process,

          - when this time expires, Inquiry will be halted.

        - **num_rsps** – **[in]** - Number of responses that can be received before the Inquiry is halted, value 0 indicates an unlimited number of responses.

    返回
    :   - BK_ERR_BT_SUCCESS : Succeed

        - others: fail

bt_err_t bk_bt_gap_cancel_discovery(void)[](#_CPPv426bk_bt_gap_cancel_discoveryv "永久链接至目标")
:   Cancel Inquiry and Name Discovery. This function should be called after esp_bluedroid_enable() completes successfully. bt_event_cb_t will be called with BK_DM_BT_GAP_DISC_STATE_CHANGED_EVT if Inquiry or Name Discovery is cancelled by calling this function.

    返回
    :   - BK_ERR_BT_SUCCESS : Succeed

        - others: fail

bt_err_t bk_bt_a2dp_sink_init(uint8_t aac_supported)[](#_CPPv420bk_bt_a2dp_sink_init7uint8_t "永久链接至目标")
:   Initialize the bluetooth A2DP sink module.


    **Attention**
    :   sink/source must init only one.

    参数
    :   **aac_supported, :** – **[in]** 1 means aac is supported, 0 means aac is not supported.

    返回
    :   - BK_ERR_BT_SUCCESS: the initialization request is successfully

        - others: fail

bt_err_t bk_bt_a2dp_sink_deinit(void)[](#_CPPv422bk_bt_a2dp_sink_deinitv "永久链接至目标")
:   Deinitialize the bluetooth A2DP sink module.


    **Attention**
    :   sink/source must inited before.

    返回
    :   - BK_ERR_BT_SUCCESS: the deinitialization request is successfully

        - others: fail

bt_err_t bk_bt_a2dp_register_callback([bk_bt_a2dp_cb_t](#_CPPv415bk_bt_a2dp_cb_t "bk_bt_a2dp_cb_t") callback)[](#_CPPv428bk_bt_a2dp_register_callback15bk_bt_a2dp_cb_t "永久链接至目标")
:   Register application callback function to A2DP module. used by both A2DP source and sink.


    **Attention**
    :   this function must call after sink or source init

    参数
    :   **callback, :** – **[in]** A2DP event callback function

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

bt_err_t bk_bt_a2dp_sink_register_data_callback([bk_bt_sink_data_cb_t](#_CPPv420bk_bt_sink_data_cb_t "bk_bt_sink_data_cb_t") callback)[](#_CPPv438bk_bt_a2dp_sink_register_data_callback20bk_bt_sink_data_cb_t "永久链接至目标")
:   Register A2DP sink data output function;.

    参数
    :   **callback, :** – **[in]** A2DP sink data callback function

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

bt_err_t bk_bt_a2dp_sink_connect(uint8_t *remote_bda)[](#_CPPv423bk_bt_a2dp_sink_connectP7uint8_t "永久链接至目标")
:   Connect to remote bluetooth A2DP source device. This API must be called after bk_bt_a2dp_sink_init().

    参数
    :   **remote_bda, :** – **[in]** remote bluetooth device address

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

bt_err_t bk_bt_a2dp_sink_disconnect(uint8_t *remote_bda)[](#_CPPv426bk_bt_a2dp_sink_disconnectP7uint8_t "永久链接至目标")
:   Disconnect from the remote A2DP source device. This API must be called after bk_bt_a2dp_sink_init().

    参数
    :   **remote_bda, :** – **[in]** remote bluetooth device address

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

bt_err_t bk_bt_avrcp_ct_init(void)[](#_CPPv419bk_bt_avrcp_ct_initv "永久链接至目标")
:   Initialize the bluetooth AVRCP controller module.

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

bt_err_t bk_bt_avrcp_ct_deinit(void)[](#_CPPv421bk_bt_avrcp_ct_deinitv "永久链接至目标")
:   Deinitialize the bluetooth AVRCP controller module.

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

bt_err_t bk_bt_avrcp_ct_register_callback([bk_avrcp_ct_cb_t](#_CPPv416bk_avrcp_ct_cb_t "bk_avrcp_ct_cb_t") callback)[](#_CPPv432bk_bt_avrcp_ct_register_callback16bk_avrcp_ct_cb_t "永久链接至目标")
:   Register application callbacks to AVRCP module.

    参数
    :   **callback, :** – **[in]** AVRCP controller callback function

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

bt_err_t bk_bt_avrcp_ct_send_get_rn_capabilities_cmd(uint8_t *remote_bda)[](#_CPPv443bk_bt_avrcp_ct_send_get_rn_capabilities_cmdP7uint8_t "永久链接至目标")
:   Send GetCapabilities PDU to AVRCP target to retrieve remote device’s supported notification event_ids. This function should be called after BK_AVRCP_CT_CONNECTION_STATE_EVT is received and AVRCP connection is established.

    参数
    :   **remote_bda, :** – **[in]** remote bluetooth device address

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

bt_err_t bk_bt_ct_send_register_notification_cmd(uint8_t *remote_bda, uint8_t event_id, uint32_t event_parameter)[](#_CPPv439bk_bt_ct_send_register_notification_cmdP7uint8_t7uint8_t8uint32_t "永久链接至目标")
:   Send register notification command to AVRCP target. This function should be called after BK_AVRCP_CT_CONNECTION_STATE_EVT is received and AVRCP connection is established.

    参数
    :   - **remote_bda, :** – **[in]** remote bluetooth device address

        - **event_id** – **[in]** : id of events, e.g. BK_AVRCP_RN_PLAY_STATUS_CHANGE, BK_AVRCP_RN_TRACK_CHANGE, etc.

        - **event_parameter** – **[in]** : playback interval for BK_AVRCP_RN_PLAY_POS_CHANGED; For other events , value of this parameter is ignored.

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

bt_err_t bk_bt_avrcp_ct_send_passthrough_cmd(uint8_t *remote_bda, uint8_t key_code, uint8_t key_state)[](#_CPPv435bk_bt_avrcp_ct_send_passthrough_cmdP7uint8_t7uint8_t7uint8_t "永久链接至目标")
:   Send passthrough command to AVRCP target. This function should be called after BK_AVRCP_CT_CONNECTION_STATE_EVT is received and AVRCP connection is established.

    参数
    :   - **remote_bda, :** – **[in]** remote bluetooth device address.

        - **key_code** – **[in]** : passthrough command code, e.g. BK_AVRCP_PT_CMD_PLAY, BK_AVRCP_PT_CMD_STOP, etc.

        - **key_state** – **[in]** : passthrough command key state, BK_AVRCP_PT_CMD_STATE_PRESSED or BK_AVRCP_PT_CMD_STATE_RELEASED

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

bt_err_t bk_bt_avrcp_tg_init(void)[](#_CPPv419bk_bt_avrcp_tg_initv "永久链接至目标")
:   Initialize the bluetooth AVRCP target module.

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

bt_err_t bk_bt_avrcp_tg_deinit(void)[](#_CPPv421bk_bt_avrcp_tg_deinitv "永久链接至目标")
:   Deinitialize the bluetooth AVRCP target module.

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

bt_err_t bk_bt_avrcp_tg_register_callback([bk_avrcp_tg_cb_t](#_CPPv416bk_avrcp_tg_cb_t "bk_avrcp_tg_cb_t") callback)[](#_CPPv432bk_bt_avrcp_tg_register_callback16bk_avrcp_tg_cb_t "永久链接至目标")
:   Register application callbacks to AVRCP target module.

    参数
    :   **callback, :** – **[in]** AVRCP target callback function

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

bt_err_t bk_bt_avrcp_tg_get_rn_evt_cap([bk_avrcp_rn_cap_api_method_t](#_CPPv428bk_avrcp_rn_cap_api_method_t "bk_avrcp_rn_cap_api_method_t") cap, [bk_avrcp_rn_evt_cap_mask_t](#_CPPv426bk_avrcp_rn_evt_cap_mask_t "bk_avrcp_rn_evt_cap_mask_t") *evt_set)[](#_CPPv429bk_bt_avrcp_tg_get_rn_evt_cap28bk_avrcp_rn_cap_api_method_tP26bk_avrcp_rn_evt_cap_mask_t "永久链接至目标")
:   Get the requested event notification capabilies on local AVRC target. The capability is returned in a bit mask representation in evt_set. This function should be called after bk_avrcp_tg_init().

    ```
                 For capability type "BK_AVRCP_RN_CAP_API_METHOD_ALLOWED, the retrieved event set is constant and
                 it covers all of the notification events that can possibly be supported with current
                 implementation.

                 For capability type BK_AVRCP_RN_CAP_API_METHOD_CURRENT_ENABLE, the event set covers the notification
                 events selected to be supported under current configuration, The configuration can be
                 changed using bk_avrcp_tg_set_rn_evt_cap().
    ```

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

bt_err_t bk_bt_avrcp_tg_set_rn_evt_cap(const [bk_avrcp_rn_evt_cap_mask_t](#_CPPv426bk_avrcp_rn_evt_cap_mask_t "bk_avrcp_rn_evt_cap_mask_t") *evt_set)[](#_CPPv429bk_bt_avrcp_tg_set_rn_evt_capPK26bk_avrcp_rn_evt_cap_mask_t "永久链接至目标")
:   Set the event notification capabilities on local AVRCP target. The capability is given in a bit mask representation in evt_set and must be a subset of allowed event IDs with current implementation. This function should be called after bk_avrcp_tg_init().

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

bt_err_t bk_bt_avrcp_tg_send_rn_rsp(uint8_t *addr, [bk_avrcp_rn_event_ids_t](#_CPPv423bk_avrcp_rn_event_ids_t "bk_avrcp_rn_event_ids_t") event_id, [bk_avrcp_rn_rsp_t](#_CPPv417bk_avrcp_rn_rsp_t "bk_avrcp_rn_rsp_t") rsp, [bk_avrcp_rn_param_t](#_CPPv419bk_avrcp_rn_param_t "bk_avrcp_rn_param_t") *param)[](#_CPPv426bk_bt_avrcp_tg_send_rn_rspP7uint8_t23bk_avrcp_rn_event_ids_t17bk_avrcp_rn_rsp_tP19bk_avrcp_rn_param_t "永久链接至目标")
:   Send RegisterNotification Response to remote AVRCP controller. Local event notification capability can be set using bk_avrcp_tg_set_rn_evt_cap(), in a bit mask representation in evt_set. This function should be called after bk_avrcp_tg_init().

    参数
    :   - **addr, :** – **[in]** peer addr

        - **event_id, :** – **[in]** notification event ID that remote AVRCP CT registers

        - **rsp, :** – **[in]** notification response code

        - **param, :** – **[in]** parameters included in the specific notification

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

bt_err_t bk_bt_avrcp_connect(uint8_t *remote_bda)[](#_CPPv419bk_bt_avrcp_connectP7uint8_t "永久链接至目标")
:   Connect to remote bluetooth AVRCP. This API must be called after bk_bt_avrcp_ct_init() or bk_bt_avrcp_tg_init.

    参数
    :   **remote_bda, :** – **[in]** remote bluetooth device address

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

bt_err_t bk_bt_a2dp_source_init(void)[](#_CPPv422bk_bt_a2dp_source_initv "永久链接至目标")
:   Initialize the bluetooth A2DP source module. A2DP can work independently.


    **Attention**
    :   sink/source must init only one.

    返回
    :   - BK_ERR_BT_SUCCESS: if the initialization request is sent to lower layer successfully

        - others: fail

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_a2dp_source_register_data_callback([bk_a2dp_source_data_cb_t](#_CPPv424bk_a2dp_source_data_cb_t "bk_a2dp_source_data_cb_t") callback)[](#_CPPv437bk_a2dp_source_register_data_callback24bk_a2dp_source_data_cb_t "永久链接至目标")
:   Register A2DP source data input function. For now, the input should be PCM data stream.

    参数
    :   **callback, :** – **[in]** A2DP source data callback function

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_a2dp_source_set_pcm_data_format(uint32_t sample_rate, uint8_t bit_depth, uint8_t channel_count)[](#_CPPv434bk_a2dp_source_set_pcm_data_format8uint32_t7uint8_t7uint8_t "永久链接至目标")
:   set a2dp source data format

    参数
    :   - **sample_rate, :** – **[in]** pcm data sample rate, such as 8000 16000 32000 44100 48000.

        - **bit_depth** – **[in]** : pcm data bit depth, now support 16 bits only.

        - **channel_count** – **[in]** : pcm data channel count, support 1 or 2 now.

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

bt_err_t bk_bt_a2dp_source_connect(uint8_t *addr)[](#_CPPv425bk_bt_a2dp_source_connectP7uint8_t "永久链接至目标")
:   Connect to remote A2DP sink device. This API must be called after bk_bt_a2dp_source_init()

    参数
    :   **addr, :** – **[in]** remote bluetooth device address

    返回
    :   - BK_ERR_BT_SUCCESS: connect request is sent to lower layer successfully

        - others: fail

bt_err_t bk_bt_a2dp_source_disconnect(uint8_t *addr)[](#_CPPv428bk_bt_a2dp_source_disconnectP7uint8_t "永久链接至目标")
:   Disconnect from the remote A2DP sink device. This API must be called after bk_bt_a2dp_source_init()

    参数
    :   **addr, :** – **[in]** remote bluetooth device address

    返回
    :   ```

                     - BK_ERR_BT_SUCCESS: connect request is sent to lower layer successfully

                     - others: fail
        ```

bt_err_t bk_a2dp_media_ctrl([bk_a2dp_media_ctrl_t](#_CPPv420bk_a2dp_media_ctrl_t "bk_a2dp_media_ctrl_t") ctrl)[](#_CPPv418bk_a2dp_media_ctrl20bk_a2dp_media_ctrl_t "永久链接至目标")
:   Media control commands. This API can be used for both A2DP sink and must be called after bk_bt_a2dp_source_init()


    **Attention**
    :   this function only used for a2dp source

    参数
    :   **ctrl, :** – **[in]** control commands for A2DP action

    返回
    :   - BK_ERR_BT_SUCCESS: control command is sent to lower layer successfully

        - others: fail

bt_err_t bk_bt_spp_init([bt_spp_event_notify_cb_t](#_CPPv424bt_spp_event_notify_cb_t "bt_spp_event_notify_cb_t") bt_spp_event_notify_cb)[](#_CPPv414bk_bt_spp_init24bt_spp_event_notify_cb_t "永久链接至目标")
:   Initialize the bluetooth SPP module.


    **Attention**
    :   this function only used for SPP

    参数
    :   **bt_spp_event_notify_cb, :** – **[in]** SPP event callback function

    返回
    :   - BK_ERR_BT_SUCCESS: control command is sent to lower layer successfully

        - others: fail

bt_err_t bk_bt_spp_start(uint32_t *spp_handle, uint8_t *local_server_channel, uint32_t *spp_record_handle)[](#_CPPv415bk_bt_spp_startP8uint32_tP7uint8_tP8uint32_t "永久链接至目标")
:   Start the bluetooth SPP server.


    **Attention**
    :   this function only used for SPP

    参数
    :   - **spp_handle, :** – **[out]** the handle of the server.

        - **local_server_channel, :** – **[out]** the server channle.

        - **spp_record_handle, :** – **[out]** the db record handle

    返回
    :   - BK_ERR_BT_SUCCESS: control command is sent to lower layer successfully

        - others: fail

bt_err_t bk_bt_spp_tx(uint32_t spp_handle, char *data, uint16_t len)[](#_CPPv412bk_bt_spp_tx8uint32_tPc8uint16_t "永久链接至目标")
:   send spp data.


    **Attention**
    :   this function only used for SPP

    参数
    :   - **spp_handle, :** – **[in]** the handle of the server.

        - **data, :** – **[in]** the data buffer addr.

        - **len, :** – **[in]** the data len.

    返回
    :   - BK_ERR_BT_SUCCESS: control command is sent to lower layer successfully

        - others: fail

bt_err_t bk_bt_disconnect_link(uint8_t *addr)[](#_CPPv421bk_bt_disconnect_linkP7uint8_t "永久链接至目标")
:   This API can be used to disconnect the acl link.

    参数
    :   **addr, :** – **[in]** remote bluetooth device address

    返回
    :   ```

                     - BK_ERR_BT_SUCCESS: disconnect request is sent to lower layer successfully

                     - others: fail
        ```

bt_err_t bk_bt_create_connection_cancel(uint8_t *addr)[](#_CPPv430bk_bt_create_connection_cancelP7uint8_t "永久链接至目标")
:   This API can be used to request cancellation of the ongoing connection creation process.

    参数
    :   **addr, :** – **[in]** remote bluetooth device address

    返回
    :   ```

                     - BK_ERR_BT_SUCCESS: cancel request is sent to lower layer successfully

                     - others: fail
        ```

bt_err_t bk_bt_set_page_timeout(uint16_t timeout)[](#_CPPv422bk_bt_set_page_timeout8uint16_t "永久链接至目标")
:   This api can be used to set the value for the Page_Timeout configuration parameter.

    参数
    :   **timeout, :** – **[in]** Page Timeout measured in number of Baseband slots, unit of 0.625ms

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail

bt_err_t bk_bt_set_page_scan_activity(uint16_t interval, uint16_t window)[](#_CPPv428bk_bt_set_page_scan_activity8uint16_t8uint16_t "永久链接至目标")
:   This api can be used to set the value for the Page_Scan_Interval and Page_Scan_Window configuration parameters.

    参数
    :   - **interval, :** – **[in]** defines the amount of time between consecutive page scans, unit of 0.625ms,(Range: 0x0012 to 0x1000, only even values are valid)

        - **window, :** – **[in]** defines the amount of time for the duration of the page scan, unit of 0.625ms,(Range: 0x0011 to 0x1000, can only be less than or equal to the Page_Scan_Interval)

    返回
    :   - BK_ERR_BT_SUCCESS: success

        - others: fail


## API Typedefs[](#api-typedefs "永久链接至标题")


### Header File[](#id1 "永久链接至标题")


- [dm_bt_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/dm_bt_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/dm_bt_types.h")


### Unions[](#unions "永久链接至标题")

union bk_a2dp_cb_param_t[](#_CPPv418bk_a2dp_cb_param_t "永久链接至目标")
:   *#include <dm_bt_types.h>*

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

    struct a2dp_audio_cfg_param[](#_CPPv4N18bk_a2dp_cb_param_t20a2dp_audio_cfg_paramE "永久链接至目标")
    :   *#include <dm_bt_types.h>*

        BK_A2DP_AUDIO_CFG_EVT.

        Public Members

        uint8_t remote_bda[6][](#_CPPv4N18bk_a2dp_cb_param_t20a2dp_audio_cfg_param10remote_bdaE "永久链接至目标")
        :   remote bluetooth device address

        [bk_a2dp_mcc_t](#_CPPv413bk_a2dp_mcc_t "bk_a2dp_mcc_t") mcc[](#_CPPv4N18bk_a2dp_cb_param_t20a2dp_audio_cfg_param3mccE "永久链接至目标")
        :   A2DP media codec capability information

    struct a2dp_audio_source_cfg_param[](#_CPPv4N18bk_a2dp_cb_param_t27a2dp_audio_source_cfg_paramE "永久链接至目标")
    :   *#include <dm_bt_types.h>*

        BK_A2DP_AUDIO_SOURCE_CFG_EVT.

        Public Members

        uint8_t remote_bda[6][](#_CPPv4N18bk_a2dp_cb_param_t27a2dp_audio_source_cfg_param10remote_bdaE "永久链接至目标")
        :   remote bluetooth device address

        uint16_t mtu[](#_CPPv4N18bk_a2dp_cb_param_t27a2dp_audio_source_cfg_param3mtuE "永久链接至目标")

        [bk_a2dp_mcc_t](#_CPPv413bk_a2dp_mcc_t "bk_a2dp_mcc_t") mcc[](#_CPPv4N18bk_a2dp_cb_param_t27a2dp_audio_source_cfg_param3mccE "永久链接至目标")
        :   max payload len, only used in source A2DP media codec capability information

    struct a2dp_audio_state_param[](#_CPPv4N18bk_a2dp_cb_param_t22a2dp_audio_state_paramE "永久链接至目标")
    :   *#include <dm_bt_types.h>*

        BK_A2DP_AUDIO_STATE_EVT.

        Public Members

        [bk_a2dp_audio_state_t](#_CPPv421bk_a2dp_audio_state_t "bk_a2dp_audio_state_t") state[](#_CPPv4N18bk_a2dp_cb_param_t22a2dp_audio_state_param5stateE "永久链接至目标")
        :   one of the values from bk_a2dp_audio_state_t

        uint8_t remote_bda[6][](#_CPPv4N18bk_a2dp_cb_param_t22a2dp_audio_state_param10remote_bdaE "永久链接至目标")
        :   remote bluetooth device address

    struct a2dp_conn_state_param[](#_CPPv4N18bk_a2dp_cb_param_t21a2dp_conn_state_paramE "永久链接至目标")
    :   *#include <dm_bt_types.h>*

        BK_A2DP_CONNECTION_STATE_EVT.

        Public Members

        [bk_a2dp_connection_state_t](#_CPPv426bk_a2dp_connection_state_t "bk_a2dp_connection_state_t") state[](#_CPPv4N18bk_a2dp_cb_param_t21a2dp_conn_state_param5stateE "永久链接至目标")
        :   one of values from bk_a2dp_connection_state_t

        uint8_t remote_bda[6][](#_CPPv4N18bk_a2dp_cb_param_t21a2dp_conn_state_param10remote_bdaE "永久链接至目标")
        :   remote bluetooth device address

        [bk_a2dp_disc_rsn_t](#_CPPv418bk_a2dp_disc_rsn_t "bk_a2dp_disc_rsn_t") disc_rsn[](#_CPPv4N18bk_a2dp_cb_param_t21a2dp_conn_state_param8disc_rsnE "永久链接至目标")
        :   reason of disconnection for “DISCONNECTED”

union bk_bt_gap_cb_param_t[](#_CPPv420bk_bt_gap_cb_param_t "永久链接至目标")
:   *#include <dm_bt_types.h>*

    GAP state callback parameters.

    Public Members

    struct [bk_bt_gap_cb_param_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[disc_res_param](#_CPPv4N20bk_bt_gap_cb_param_t14disc_res_paramE "bk_bt_gap_cb_param_t::disc_res_param") disc_res[](#_CPPv4N20bk_bt_gap_cb_param_t8disc_resE "永久链接至目标")
    :   discovery result parameter struct

    struct [bk_bt_gap_cb_param_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[disc_state_changed_param](#_CPPv4N20bk_bt_gap_cb_param_t24disc_state_changed_paramE "bk_bt_gap_cb_param_t::disc_state_changed_param") disc_st_chg[](#_CPPv4N20bk_bt_gap_cb_param_t11disc_st_chgE "永久链接至目标")
    :   discovery state changed parameter struct

    struct [bk_bt_gap_cb_param_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[auth_cmpl_param](#_CPPv4N20bk_bt_gap_cb_param_t15auth_cmpl_paramE "bk_bt_gap_cb_param_t::auth_cmpl_param") auth_cmpl[](#_CPPv4N20bk_bt_gap_cb_param_t9auth_cmplE "永久链接至目标")
    :   authentication complete parameter struct

    struct [bk_bt_gap_cb_param_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[acl_conn_cmpl_stat_param](#_CPPv4N20bk_bt_gap_cb_param_t24acl_conn_cmpl_stat_paramE "bk_bt_gap_cb_param_t::acl_conn_cmpl_stat_param") acl_conn_cmpl_stat[](#_CPPv4N20bk_bt_gap_cb_param_t18acl_conn_cmpl_statE "永久链接至目标")
    :   ACL connection complete status parameter struct

    struct [bk_bt_gap_cb_param_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[acl_disconn_cmpl_stat_param](#_CPPv4N20bk_bt_gap_cb_param_t27acl_disconn_cmpl_stat_paramE "bk_bt_gap_cb_param_t::acl_disconn_cmpl_stat_param") acl_disconn_cmpl_stat[](#_CPPv4N20bk_bt_gap_cb_param_t21acl_disconn_cmpl_statE "永久链接至目标")
    :   ACL disconnection complete status parameter struct

    struct acl_conn_cmpl_stat_param[](#_CPPv4N20bk_bt_gap_cb_param_t24acl_conn_cmpl_stat_paramE "永久链接至目标")
    :   *#include <dm_bt_types.h>*

        BK_DM_GAP_ACL_CONN_CMPL_STAT_EVT.

        Public Members

        uint8_t stat[](#_CPPv4N20bk_bt_gap_cb_param_t24acl_conn_cmpl_stat_param4statE "永久链接至目标")
        :   ACL connection status

        uint8_t bda[6][](#_CPPv4N20bk_bt_gap_cb_param_t24acl_conn_cmpl_stat_param3bdaE "永久链接至目标")
        :   remote bluetooth device address

    struct acl_disconn_cmpl_stat_param[](#_CPPv4N20bk_bt_gap_cb_param_t27acl_disconn_cmpl_stat_paramE "永久链接至目标")
    :   *#include <dm_bt_types.h>*

        BK_DM_BT_GAP_ACL_DISCONN_CMPL_STAT_EVT.

        Public Members

        uint8_t reason[](#_CPPv4N20bk_bt_gap_cb_param_t27acl_disconn_cmpl_stat_param6reasonE "永久链接至目标")
        :   ACL disconnection reason

        uint8_t bda[6][](#_CPPv4N20bk_bt_gap_cb_param_t27acl_disconn_cmpl_stat_param3bdaE "永久链接至目标")
        :   remote bluetooth device address

    struct auth_cmpl_param[](#_CPPv4N20bk_bt_gap_cb_param_t15auth_cmpl_paramE "永久链接至目标")
    :   *#include <dm_bt_types.h>*

        BK_DM_BT_GAP_AUTH_CMPL_EVT.

        Public Members

        uint8_t bda[6][](#_CPPv4N20bk_bt_gap_cb_param_t15auth_cmpl_param3bdaE "永久链接至目标")
        :   remote bluetooth device address

        uint8_t stat[](#_CPPv4N20bk_bt_gap_cb_param_t15auth_cmpl_param4statE "永久链接至目标")
        :   authentication complete status

    struct disc_res_param[](#_CPPv4N20bk_bt_gap_cb_param_t14disc_res_paramE "永久链接至目标")
    :   *#include <dm_bt_types.h>*

        BK_DM_BT_GAP_DISC_RES_EVT.

        Public Members

        uint8_t bda[6][](#_CPPv4N20bk_bt_gap_cb_param_t14disc_res_param3bdaE "永久链接至目标")
        :   remote bluetooth device address

        int num_prop[](#_CPPv4N20bk_bt_gap_cb_param_t14disc_res_param8num_propE "永久链接至目标")
        :   number of properties got

        [bk_bt_gap_dev_prop_t](#_CPPv420bk_bt_gap_dev_prop_t "bk_bt_gap_dev_prop_t") *prop[](#_CPPv4N20bk_bt_gap_cb_param_t14disc_res_param4propE "永久链接至目标")
        :   properties discovered from the new device

    struct disc_state_changed_param[](#_CPPv4N20bk_bt_gap_cb_param_t24disc_state_changed_paramE "永久链接至目标")
    :   *#include <dm_bt_types.h>*

        BK_DM_BT_GAP_DISC_STATE_CHANGED_EVT.

        Public Members

        [bk_bt_gap_discovery_state_t](#_CPPv427bk_bt_gap_discovery_state_t "bk_bt_gap_discovery_state_t") state[](#_CPPv4N20bk_bt_gap_cb_param_t24disc_state_changed_param5stateE "永久链接至目标")
        :   discovery state

union bk_avrcp_rn_param_t[](#_CPPv419bk_avrcp_rn_param_t "永久链接至目标")
:   *#include <dm_bt_types.h>*

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

union bk_avrcp_ct_cb_param_t[](#_CPPv422bk_avrcp_ct_cb_param_t "永久链接至目标")
:   *#include <dm_bt_types.h>*

    AVRCP controller callback parameters.

    Public Members

    struct [bk_avrcp_ct_cb_param_t](#_CPPv422bk_avrcp_ct_cb_param_t "bk_avrcp_ct_cb_param_t")::[avrcp_ct_conn_state_param](#_CPPv4N22bk_avrcp_ct_cb_param_t25avrcp_ct_conn_state_paramE "bk_avrcp_ct_cb_param_t::avrcp_ct_conn_state_param") conn_state[](#_CPPv4N22bk_avrcp_ct_cb_param_t10conn_stateE "永久链接至目标")
    :   AVRCP connection status

    struct [bk_avrcp_ct_cb_param_t](#_CPPv422bk_avrcp_ct_cb_param_t "bk_avrcp_ct_cb_param_t")::[avrcp_ct_change_notify_param](#_CPPv4N22bk_avrcp_ct_cb_param_t28avrcp_ct_change_notify_paramE "bk_avrcp_ct_cb_param_t::avrcp_ct_change_notify_param") change_ntf[](#_CPPv4N22bk_avrcp_ct_cb_param_t10change_ntfE "永久链接至目标")
    :   notifications

    struct [bk_avrcp_ct_cb_param_t](#_CPPv422bk_avrcp_ct_cb_param_t "bk_avrcp_ct_cb_param_t")::[avrcp_ct_get_rn_caps_rsp_param](#_CPPv4N22bk_avrcp_ct_cb_param_t30avrcp_ct_get_rn_caps_rsp_paramE "bk_avrcp_ct_cb_param_t::avrcp_ct_get_rn_caps_rsp_param") get_rn_caps_rsp[](#_CPPv4N22bk_avrcp_ct_cb_param_t15get_rn_caps_rspE "永久链接至目标")
    :   get supported event capabilities response from AVRCP target

    struct avrcp_ct_change_notify_param[](#_CPPv4N22bk_avrcp_ct_cb_param_t28avrcp_ct_change_notify_paramE "永久链接至目标")
    :   *#include <dm_bt_types.h>*

        BK_AVRCP_CT_CHANGE_NOTIFY_EVT.

        Public Members

        uint8_t event_id[](#_CPPv4N22bk_avrcp_ct_cb_param_t28avrcp_ct_change_notify_param8event_idE "永久链接至目标")
        :   id of AVRCP event notification

        [bk_avrcp_rn_param_t](#_CPPv419bk_avrcp_rn_param_t "bk_avrcp_rn_param_t") event_parameter[](#_CPPv4N22bk_avrcp_ct_cb_param_t28avrcp_ct_change_notify_param15event_parameterE "永久链接至目标")
        :   event notification parameter

    struct avrcp_ct_conn_state_param[](#_CPPv4N22bk_avrcp_ct_cb_param_t25avrcp_ct_conn_state_paramE "永久链接至目标")
    :   *#include <dm_bt_types.h>*

        BK_AVRCP_CT_CONNECTION_STATE_EVT.

        Public Members

        uint8_t connected[](#_CPPv4N22bk_avrcp_ct_cb_param_t25avrcp_ct_conn_state_param9connectedE "永久链接至目标")
        :   whether AVRCP connection is set up

        uint8_t remote_bda[6][](#_CPPv4N22bk_avrcp_ct_cb_param_t25avrcp_ct_conn_state_param10remote_bdaE "永久链接至目标")
        :   remote bluetooth device address

    struct avrcp_ct_get_rn_caps_rsp_param[](#_CPPv4N22bk_avrcp_ct_cb_param_t30avrcp_ct_get_rn_caps_rsp_paramE "永久链接至目标")
    :   *#include <dm_bt_types.h>*

        BK_AVRCP_CT_GET_RN_CAPABILITIES_RSP_EVT.

        Public Members

        uint8_t cap_count[](#_CPPv4N22bk_avrcp_ct_cb_param_t30avrcp_ct_get_rn_caps_rsp_param9cap_countE "永久链接至目标")
        :   number of items provided in event or company_id according to cap_id used

        [bk_avrcp_rn_evt_cap_mask_t](#_CPPv426bk_avrcp_rn_evt_cap_mask_t "bk_avrcp_rn_evt_cap_mask_t") evt_set[](#_CPPv4N22bk_avrcp_ct_cb_param_t30avrcp_ct_get_rn_caps_rsp_param7evt_setE "永久链接至目标")
        :   supported event_ids represented in bit-mask

union bk_avrcp_tg_cb_param_t[](#_CPPv422bk_avrcp_tg_cb_param_t "永久链接至目标")
:   *#include <dm_bt_types.h>*

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
    :   *#include <dm_bt_types.h>*

        BK_AVRCP_TG_CONNECTION_STATE_EVT.

        Public Members

        bool connected[](#_CPPv4N22bk_avrcp_tg_cb_param_t24avrcp_tg_conn_stat_param9connectedE "永久链接至目标")
        :   whether AVRC connection is set up

        uint8_t remote_bda[6][](#_CPPv4N22bk_avrcp_tg_cb_param_t24avrcp_tg_conn_stat_param10remote_bdaE "永久链接至目标")
        :   remote bluetooth device address

    struct avrcp_tg_psth_cmd_param[](#_CPPv4N22bk_avrcp_tg_cb_param_t23avrcp_tg_psth_cmd_paramE "永久链接至目标")
    :   *#include <dm_bt_types.h>*

        BK_AVRCP_TG_PASSTHROUGH_CMD_EVT.

        Public Members

        uint8_t key_code[](#_CPPv4N22bk_avrcp_tg_cb_param_t23avrcp_tg_psth_cmd_param8key_codeE "永久链接至目标")
        :   passthrough command code

        uint8_t key_state[](#_CPPv4N22bk_avrcp_tg_cb_param_t23avrcp_tg_psth_cmd_param9key_stateE "永久链接至目标")
        :   0 for PRESSED, 1 for RELEASED

    struct avrcp_tg_reg_ntf_param[](#_CPPv4N22bk_avrcp_tg_cb_param_t22avrcp_tg_reg_ntf_paramE "永久链接至目标")
    :   *#include <dm_bt_types.h>*

        BK_AVRCP_TG_REGISTER_NOTIFICATION_EVT.

        Public Members

        uint8_t event_id[](#_CPPv4N22bk_avrcp_tg_cb_param_t22avrcp_tg_reg_ntf_param8event_idE "永久链接至目标")
        :   event id of bk_avrcp_rn_event_ids_t

        uint32_t event_parameter[](#_CPPv4N22bk_avrcp_tg_cb_param_t22avrcp_tg_reg_ntf_param15event_parameterE "永久链接至目标")
        :   event notification parameter, used with BK_AVRCP_RN_PLAY_POS_CHANGED only now

    struct avrcp_tg_set_abs_vol_param[](#_CPPv4N22bk_avrcp_tg_cb_param_t26avrcp_tg_set_abs_vol_paramE "永久链接至目标")
    :   *#include <dm_bt_types.h>*

        BK_AVRCP_TG_SET_ABSOLUTE_VOLUME_CMD_EVT.

        Public Members

        uint8_t volume[](#_CPPv4N22bk_avrcp_tg_cb_param_t26avrcp_tg_set_abs_vol_param6volumeE "永久链接至目标")
        :   volume ranges from 0 to 127


### Structures[](#structures "永久链接至标题")

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

struct bk_bt_gap_dev_prop_t[](#_CPPv420bk_bt_gap_dev_prop_t "永久链接至目标")
:   Bluetooth Device Property Descriptor.

    Public Members

    [bk_bt_gap_dev_prop_type_t](#_CPPv425bk_bt_gap_dev_prop_type_t "bk_bt_gap_dev_prop_type_t") type[](#_CPPv4N20bk_bt_gap_dev_prop_t4typeE "永久链接至目标")
    :   Device property type

    int len[](#_CPPv4N20bk_bt_gap_dev_prop_t3lenE "永久链接至目标")
    :   Device property value length

    void *val[](#_CPPv4N20bk_bt_gap_dev_prop_t3valE "永久链接至目标")
    :   Device property value

struct bk_bt_linkkey_storage_t[](#_CPPv423bk_bt_linkkey_storage_t "永久链接至目标")
:   bt link key storage

    Public Members

    uint16_t size[](#_CPPv4N23bk_bt_linkkey_storage_t4sizeE "永久链接至目标")
    :   this struct size

    uint8_t addr[6][](#_CPPv4N23bk_bt_linkkey_storage_t4addrE "永久链接至目标")
    :   bt addr

    uint8_t link_key[16][](#_CPPv4N23bk_bt_linkkey_storage_t8link_keyE "永久链接至目标")
    :   bt link key

struct bk_avrcp_rn_evt_cap_mask_t[](#_CPPv426bk_avrcp_rn_evt_cap_mask_t "永久链接至目标")
:   AVRCP target notification event capability bit mask.

    Public Members

    uint16_t bits[](#_CPPv4N26bk_avrcp_rn_evt_cap_mask_t4bitsE "永久链接至目标")
    :   bit mask representation of supported event_ids


### Type Definitions[](#type-definitions "永久链接至标题")

typedef int32_t (*bk_a2dp_source_data_cb_t)(uint8_t *buf, int32_t len)[](#_CPPv424bk_a2dp_source_data_cb_t "永久链接至目标")
:   A2DP source data read callback function.

    Param buf
    :   **[in]** : buffer to be filled with PCM data stream from higher layer

    Param len
    :   **[in]** : size(in bytes) of data block to be copied to buf. -1 is an indication to user that data buffer shall be flushed

    Return
    :   size of bytes read successfully, if the argument len is -1, this value is ignored.

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

typedef uint32_t (*bt_event_cb_t)([bt_event_enum_t](#_CPPv415bt_event_enum_t "bt_event_enum_t") event, void *param)[](#_CPPv413bt_event_cb_t "永久链接至目标")
:   for async dm_bt api event.

    bt event report.

    Param event, :
    :   event id. see bt_event_enum_t


        - param: param

typedef uint16_t (*bt_spp_event_notify_cb_t)(uint32_t spp_handle, uint8_t spp_event, uint16_t status, void *data, uint16_t data_length)[](#_CPPv424bt_spp_event_notify_cb_t "永久链接至目标")
:   Application should register a callback through the API bk_bt_spp_init.

    Param spp_handle, :
    :   **[in]** Handle associates a SPP connection to a remote SPP device.

    Param spp_event, :
    :   **[in]** Event indicated to application by bk_spp_cb_event_t.

    Param status, :
    :   **[in]** The status of the event.

    Param data, :
    :   **[in]** Pointer to the array containing the parameters associated with the event.

    Param data_length, :
    :   **[in]** Length of the parameters associated with the event.

    Return
    :   0x00.


### Enumerations[](#enumerations "永久链接至标题")

enum bk_bt_conn_mode_t[](#_CPPv417bk_bt_conn_mode_t "永久链接至目标")
:   Discoverability and Connectability mode.


    *Values:*

    enumerator BK_BT_NON_CONNECTABLE[](#_CPPv4N17bk_bt_conn_mode_t21BK_BT_NON_CONNECTABLEE "永久链接至目标")
    :   Non-connectable

    enumerator BK_BT_CONNECTABLE[](#_CPPv4N17bk_bt_conn_mode_t17BK_BT_CONNECTABLEE "永久链接至目标")
    :   Connectable

enum bk_bt_disc_mode_t[](#_CPPv417bk_bt_disc_mode_t "永久链接至目标")
:   *Values:*

    enumerator BK_BT_NON_DISCOVERABLE[](#_CPPv4N17bk_bt_disc_mode_t22BK_BT_NON_DISCOVERABLEE "永久链接至目标")
    :   Non-discoverable

    enumerator BK_BT_DISCOVERABLE[](#_CPPv4N17bk_bt_disc_mode_t18BK_BT_DISCOVERABLEE "永久链接至目标")
    :   Discoverable

enum common_cod_t[](#_CPPv412common_cod_t "永久链接至目标")
:   *Values:*

    enumerator COD_PHONE[](#_CPPv4N12common_cod_t9COD_PHONEE "永久链接至目标")

    enumerator COD_SOUNDBAR[](#_CPPv4N12common_cod_t12COD_SOUNDBARE "永久链接至目标")

    enumerator COD_HEADSET[](#_CPPv4N12common_cod_t11COD_HEADSETE "永久链接至目标")

enum bk_bt_inq_mode_t[](#_CPPv416bk_bt_inq_mode_t "永久链接至目标")
:   Inquiry Mode


    *Values:*

    enumerator BK_BT_INQ_MODE_GENERAL_INQUIRY[](#_CPPv4N16bk_bt_inq_mode_t30BK_BT_INQ_MODE_GENERAL_INQUIRYE "永久链接至目标")
    :   General inquiry mode

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

enum bk_bt_gap_discovery_state_t[](#_CPPv427bk_bt_gap_discovery_state_t "永久链接至目标")
:   Bluetooth Device Discovery state


    *Values:*

    enumerator BK_BT_GAP_DISCOVERY_STOPPED[](#_CPPv4N27bk_bt_gap_discovery_state_t27BK_BT_GAP_DISCOVERY_STOPPEDE "永久链接至目标")
    :   Device discovery stopped

    enumerator BK_BT_GAP_DISCOVERY_STARTED[](#_CPPv4N27bk_bt_gap_discovery_state_t27BK_BT_GAP_DISCOVERY_STARTEDE "永久链接至目标")
    :   Device discovery started

enum bt_event_enum_t[](#_CPPv415bt_event_enum_t "永久链接至目标")
:   *Values:*

    enumerator BK_DM_BT_EVENT_STACK_OK[](#_CPPv4N15bt_event_enum_t23BK_DM_BT_EVENT_STACK_OKE "永久链接至目标")
    :   bt stack init ok, param NULL

    enumerator BK_DM_BT_EVENT_INQUIRY_RESULT[](#_CPPv4N15bt_event_enum_t29BK_DM_BT_EVENT_INQUIRY_RESULTE "永久链接至目标")
    :   inquiry result, not used now

    enumerator BK_DM_BT_EVENT_DISCONNECT[](#_CPPv4N15bt_event_enum_t25BK_DM_BT_EVENT_DISCONNECTE "永久链接至目标")
    :   disconnect completed, param addr

    enumerator BK_DM_BT_EVENT_CONNECTION_COMPLETE[](#_CPPv4N15bt_event_enum_t34BK_DM_BT_EVENT_CONNECTION_COMPLETEE "永久链接至目标")
    :   connection completed, param addr

    enumerator BK_DM_BT_EVENT_LINKKEY_NOTIFY[](#_CPPv4N15bt_event_enum_t29BK_DM_BT_EVENT_LINKKEY_NOTIFYE "永久链接至目标")
    :   recv cb when pair success and get link key, param [bk_bt_linkkey_storage_t](#structbk__bt__linkkey__storage__t "#structbk__bt__linkkey__storage__t")

    enumerator BK_DM_BT_EVENT_LINKKEY_REQ[](#_CPPv4N15bt_event_enum_t26BK_DM_BT_EVENT_LINKKEY_REQE "永久链接至目标")
    :   recv cb when peer need user to input link key, param [bd_addr_t](ble.html#structbd__addr__t "ble.html#structbd__addr__t")

        Device discovery result event, param [bk_bt_gap_cb_param_t](#unionbk__bt__gap__cb__param__t "#unionbk__bt__gap__cb__param__t")

    enumerator BK_DM_BT_GAP_DISC_RES_EVT[](#_CPPv4N15bt_event_enum_t25BK_DM_BT_GAP_DISC_RES_EVTE "永久链接至目标")
    :   Discovery state changed event, param [bk_bt_gap_cb_param_t](#unionbk__bt__gap__cb__param__t "#unionbk__bt__gap__cb__param__t")

    enumerator BK_DM_BT_GAP_DISC_STATE_CHANGED_EVT[](#_CPPv4N15bt_event_enum_t35BK_DM_BT_GAP_DISC_STATE_CHANGED_EVTE "永久链接至目标")
    :   Authentication complete event, param [bk_bt_gap_cb_param_t](#unionbk__bt__gap__cb__param__t "#unionbk__bt__gap__cb__param__t")

    enumerator BK_DM_BT_GAP_AUTH_CMPL_EVT[](#_CPPv4N15bt_event_enum_t26BK_DM_BT_GAP_AUTH_CMPL_EVTE "永久链接至目标")

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

    enumerator BK_AVRCP_CT_METADATA_RSP_EVT[](#_CPPv4N22bk_avrcp_ct_cb_event_t28BK_AVRCP_CT_METADATA_RSP_EVTE "永久链接至目标")
    :   metadata response event

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

enum bk_spp_cb_event_t[](#_CPPv417bk_spp_cb_event_t "永久链接至目标")
:   SPP Callback Event Types.


    *Values:*

    enumerator BK_SPP_NO_EVENT[](#_CPPv4N17bk_spp_cb_event_t15BK_SPP_NO_EVENTE "永久链接至目标")
    :   spp no event

    enumerator BK_SPP_CONNECT_CNF[](#_CPPv4N17bk_spp_cb_event_t18BK_SPP_CONNECT_CNFE "永久链接至目标")
    :   spp connect confirm event

    enumerator BK_SPP_CONNECT_IND[](#_CPPv4N17bk_spp_cb_event_t18BK_SPP_CONNECT_INDE "永久链接至目标")
    :   spp connect request ind event

    enumerator BK_SPP_DISCONNECT_CNF[](#_CPPv4N17bk_spp_cb_event_t21BK_SPP_DISCONNECT_CNFE "永久链接至目标")
    :   spp disconnect confirm event

    enumerator BK_SPP_DISCONNECT_IND[](#_CPPv4N17bk_spp_cb_event_t21BK_SPP_DISCONNECT_INDE "永久链接至目标")
    :   spp disconnect request ind event

    enumerator BK_SPP_STOP_CNF[](#_CPPv4N17bk_spp_cb_event_t15BK_SPP_STOP_CNFE "永久链接至目标")
    :   spp server stop confirm event

    enumerator BK_SPP_SEND_CNF[](#_CPPv4N17bk_spp_cb_event_t15BK_SPP_SEND_CNFE "永久链接至目标")
    :   spp send data confirm event

    enumerator BK_SPP_RECVD_DATA_IND[](#_CPPv4N17bk_spp_cb_event_t21BK_SPP_RECVD_DATA_INDE "永久链接至目标")
    :   spp receive data ind event
