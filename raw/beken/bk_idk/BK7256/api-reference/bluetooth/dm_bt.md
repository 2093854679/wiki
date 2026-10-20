---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/api-reference/bluetooth/dm_bt.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="dm-bt-apis"></a>

# DM BT APIs

重要

The DM BT API v1.0 is the lastest stable DM BT APIs. All new applications should use DM BT API v1.0.

<a id="dm-bt-api-categories"></a>

## DM BT API Categories

Most of DM BT APIs can be categoried as:

Interface specific DM BT APIs:
:   - BT common interface
    - BT A2DP Sink interface

<a id="application-example"></a>

## Application Example

Check [projects/lvgl/soundbar](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/examples/projects/lvgl/soundbar) folder, which contains the following application:

- There is a A2DP sink client demo. This demo can be discovered and connected by A2DP source device and receive the audio stream from remote device

<a id="api-reference"></a>

## API Reference

<a id="header-file"></a>

### Header File

- [dm\_bt.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/dm_bt.h)

<a id="functions"></a>

### Functions

<a id="_CPPv428bk_bt_gap_set_event_callback13bt_event_cb_t"></a>

<a id="_CPPv328bk_bt_gap_set_event_callback13bt_event_cb_t"></a> <a id="_CPPv228bk_bt_gap_set_event_callback13bt_event_cb_t"></a> <a id="bk_bt_gap_set_event_callback__bt_event_cb_t"></a> <a id="dm__bt_8h_1a5cb90344ff2803bb3a623a5630e98242"></a> bt\_err\_t bk\_bt\_gap\_set\_event\_callback([bt\_event\_cb\_t](#_CPPv413bt_event_cb_t "bt_event_cb_t") func)
:   sets BT event callback function

    参数
    :   **func** – **\[in\]** : callback

    返回
    :   - BK\_ERR\_BT\_SUCCESS : Succeed
        - BK\_ERR\_BT\_FAIL: others

<a id="_CPPv423bk_bt_gap_linkkey_reply7uint8_tP23bk_bt_linkkey_storage_t"></a>

<a id="_CPPv323bk_bt_gap_linkkey_reply7uint8_tP23bk_bt_linkkey_storage_t"></a> <a id="_CPPv223bk_bt_gap_linkkey_reply7uint8_tP23bk_bt_linkkey_storage_t"></a> <a id="bk_bt_gap_linkkey_reply__uint8_t.bk_bt_linkkey_storage_tP"></a> <a id="dm__bt_8h_1aa4bfe6237c79b4fc52f329ce72cdb575"></a> bt\_err\_t bk\_bt\_gap\_linkkey\_reply(uint8\_t is\_exist, [bk\_bt\_linkkey\_storage\_t](#_CPPv423bk_bt_linkkey_storage_t "bk_bt_linkkey_storage_t") \*key)
:   send linkkey when peer need authentication

    **Attention**
    :   key-\>addr must be valued

    参数
    :   - **is\_exist** – **\[in\]** : if linkkey exist. If no exist, peer may trigger pair procedure
        - **key** – **\[in\]** : linkkey,

    返回
    :   - BK\_ERR\_BT\_SUCCESS : Succeed
        - BK\_ERR\_BT\_FAIL: others

<a id="_CPPv424bk_bt_gap_set_visibility17bk_bt_conn_mode_t17bk_bt_disc_mode_t"></a>

<a id="_CPPv324bk_bt_gap_set_visibility17bk_bt_conn_mode_t17bk_bt_disc_mode_t"></a> <a id="_CPPv224bk_bt_gap_set_visibility17bk_bt_conn_mode_t17bk_bt_disc_mode_t"></a> <a id="bk_bt_gap_set_visibility__bk_bt_conn_mode_t.bk_bt_disc_mode_t"></a> <a id="dm__bt_8h_1af17b9dcfb59c2ea64334dc1ca9af5d48"></a> bt\_err\_t bk\_bt\_gap\_set\_visibility([bk\_bt\_conn\_mode\_t](#_CPPv417bk_bt_conn_mode_t "bk_bt_conn_mode_t") conn\_mode, [bk\_bt\_disc\_mode\_t](#_CPPv417bk_bt_disc_mode_t "bk_bt_disc_mode_t") disc\_mode)
:   sets the Bluetooth connectable, discoverable

    参数
    :   - **conn\_mode** – **\[in\]** : one of the enums of bk\_bt\_conn\_mode\_t
        - **disc\_mode** – **\[in\]** : one of the enums of bk\_bt\_disc\_mode\_t

    返回
    :   - BK\_ERR\_BT\_SUCCESS : Succeed
        - BK\_ERR\_BT\_FAIL: others

<a id="_CPPv426bk_bt_gap_set_device_class8uint32_t"></a>

<a id="_CPPv326bk_bt_gap_set_device_class8uint32_t"></a> <a id="_CPPv226bk_bt_gap_set_device_class8uint32_t"></a> <a id="bk_bt_gap_set_device_class__uint32_t"></a> <a id="dm__bt_8h_1aea5c03047d4834982cc5f0af62dad00d"></a> bt\_err\_t bk\_bt\_gap\_set\_device\_class(uint32\_t cod)
:   set the class of device

    参见

    enum common\_cod\_t)

    参数
    :   **cod, :** – **\[in\]** Class of Device for the device(

    返回
    :   - BK\_ERR\_BT\_SUCCESS: succeed
        - others: fail

<a id="_CPPv424bk_bt_gap_set_local_nameP7uint8_t7uint8_t"></a>

<a id="_CPPv324bk_bt_gap_set_local_nameP7uint8_t7uint8_t"></a> <a id="_CPPv224bk_bt_gap_set_local_nameP7uint8_t7uint8_t"></a> <a id="bk_bt_gap_set_local_name__uint8_tP.uint8_t"></a> <a id="dm__bt_8h_1a06eeb3be49561eba06a6280073bbe950"></a> bt\_err\_t bk\_bt\_gap\_set\_local\_name(uint8\_t \*name, uint8\_t len)
:   set the local name

    参数
    :   - **name, :** – **\[in\]** pointer of name
        - **len, :** – **\[in\]** the length of name

    返回
    :   - BK\_ERR\_BT\_SUCCESS: succeed
        - others: fail

<a id="_CPPv425bk_bt_gap_start_discovery16bk_bt_inq_mode_t7uint8_t7uint8_t"></a>

<a id="_CPPv325bk_bt_gap_start_discovery16bk_bt_inq_mode_t7uint8_t7uint8_t"></a> <a id="_CPPv225bk_bt_gap_start_discovery16bk_bt_inq_mode_t7uint8_t7uint8_t"></a> <a id="bk_bt_gap_start_discovery__bk_bt_inq_mode_t.uint8_t.uint8_t"></a> <a id="dm__bt_8h_1aff1490fa21c1e5551887955d290a1d5f"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_bt\_gap\_start\_discovery([bk\_bt\_inq\_mode\_t](#_CPPv416bk_bt_inq_mode_t "bk_bt_inq_mode_t") mode, uint8\_t inq\_len, uint8\_t num\_rsps)
:   This function starts Inquiry and Name Discovery. This function should be called after esp\_bluedroid\_enable() completes successfully. When Inquiry is halted and cached results do not contain device name, then Name Discovery will connect to the peer target to get the device name. bk\_bt\_gap\_cb\_t will be called with BK\_DM\_BT\_GAP\_DISC\_STATE\_CHANGED\_EVT when Inquiry is started or Name Discovery is completed. bk\_bt\_gap\_cb\_t will be called with BK\_DM\_BT\_GAP\_DISC\_RES\_EVT each time the two types of discovery results are got.

    参数
    :   - **mode** – **\[in\]** \- Inquiry mode
        - **inq\_len** – **\[in\]** \- Inquiry duration in 1.28 sec units, ranging from 0x01 to 0x30. This parameter only specifies the total duration of the Inquiry process,

          - when this time expires, Inquiry will be halted.
        - **num\_rsps** – **\[in\]** \- Number of responses that can be received before the Inquiry is halted, value 0 indicates an unlimited number of responses.

    返回
    :   - BK\_ERR\_BT\_SUCCESS : Succeed
        - others: fail

<a id="_CPPv426bk_bt_gap_cancel_discoveryv"></a>

<a id="_CPPv326bk_bt_gap_cancel_discoveryv"></a> <a id="_CPPv226bk_bt_gap_cancel_discoveryv"></a> <a id="bk_bt_gap_cancel_discovery__void"></a> <a id="dm__bt_8h_1a73bf522072defaf438f88965f202d817"></a> bt\_err\_t bk\_bt\_gap\_cancel\_discovery(void)
:   Cancel Inquiry and Name Discovery. This function should be called after esp\_bluedroid\_enable() completes successfully. bt\_event\_cb\_t will be called with BK\_DM\_BT\_GAP\_DISC\_STATE\_CHANGED\_EVT if Inquiry or Name Discovery is cancelled by calling this function.

    返回
    :   - BK\_ERR\_BT\_SUCCESS : Succeed
        - others: fail

<a id="_CPPv420bk_bt_a2dp_sink_init7uint8_t"></a>

<a id="_CPPv320bk_bt_a2dp_sink_init7uint8_t"></a> <a id="_CPPv220bk_bt_a2dp_sink_init7uint8_t"></a> <a id="bk_bt_a2dp_sink_init__uint8_t"></a> <a id="dm__bt_8h_1a134d9baea04522503520ffc4de2893f2"></a> bt\_err\_t bk\_bt\_a2dp\_sink\_init(uint8\_t aac\_supported)
:   Initialize the bluetooth A2DP sink module.

    **Attention**
    :   sink/source must init only one.

    参数
    :   **aac\_supported, :** – **\[in\]** 1 means aac is supported, 0 means aac is not supported.

    返回
    :   - BK\_ERR\_BT\_SUCCESS: the initialization request is successfully
        - others: fail

<a id="_CPPv422bk_bt_a2dp_sink_deinitv"></a>

<a id="_CPPv322bk_bt_a2dp_sink_deinitv"></a> <a id="_CPPv222bk_bt_a2dp_sink_deinitv"></a> <a id="bk_bt_a2dp_sink_deinit__void"></a> <a id="dm__bt_8h_1afc63639812513bb4a51a2d5416a1ad94"></a> bt\_err\_t bk\_bt\_a2dp\_sink\_deinit(void)
:   Deinitialize the bluetooth A2DP sink module.

    **Attention**
    :   sink/source must inited before.

    返回
    :   - BK\_ERR\_BT\_SUCCESS: the deinitialization request is successfully
        - others: fail

<a id="_CPPv428bk_bt_a2dp_register_callback15bk_bt_a2dp_cb_t"></a>

<a id="_CPPv328bk_bt_a2dp_register_callback15bk_bt_a2dp_cb_t"></a> <a id="_CPPv228bk_bt_a2dp_register_callback15bk_bt_a2dp_cb_t"></a> <a id="bk_bt_a2dp_register_callback__bk_bt_a2dp_cb_t"></a> <a id="dm__bt_8h_1a1c2962b8533cc17858582860fec74759"></a> bt\_err\_t bk\_bt\_a2dp\_register\_callback([bk\_bt\_a2dp\_cb\_t](#_CPPv415bk_bt_a2dp_cb_t "bk_bt_a2dp_cb_t") callback)
:   Register application callback function to A2DP module. used by both A2DP source and sink.

    **Attention**
    :   this function must call after sink or source init

    参数
    :   **callback, :** – **\[in\]** A2DP event callback function

    返回
    :   - BK\_ERR\_BT\_SUCCESS: success
        - others: fail

<a id="_CPPv438bk_bt_a2dp_sink_register_data_callback20bk_bt_sink_data_cb_t"></a>

<a id="_CPPv338bk_bt_a2dp_sink_register_data_callback20bk_bt_sink_data_cb_t"></a> <a id="_CPPv238bk_bt_a2dp_sink_register_data_callback20bk_bt_sink_data_cb_t"></a> <a id="bk_bt_a2dp_sink_register_data_callback__bk_bt_sink_data_cb_t"></a> <a id="dm__bt_8h_1adc785ae3d034f31e3036fa1abc201ce0"></a> bt\_err\_t bk\_bt\_a2dp\_sink\_register\_data\_callback([bk\_bt\_sink\_data\_cb\_t](#_CPPv420bk_bt_sink_data_cb_t "bk_bt_sink_data_cb_t") callback)
:   Register A2DP sink data output function;.

    参数
    :   **callback, :** – **\[in\]** A2DP sink data callback function

    返回
    :   - BK\_ERR\_BT\_SUCCESS: success
        - others: fail

<a id="_CPPv423bk_bt_a2dp_sink_connectP7uint8_t"></a>

<a id="_CPPv323bk_bt_a2dp_sink_connectP7uint8_t"></a> <a id="_CPPv223bk_bt_a2dp_sink_connectP7uint8_t"></a> <a id="bk_bt_a2dp_sink_connect__uint8_tP"></a> <a id="dm__bt_8h_1ad106a063945ecfc816f659dc756026dc"></a> bt\_err\_t bk\_bt\_a2dp\_sink\_connect(uint8\_t \*remote\_bda)
:   Connect to remote bluetooth A2DP source device. This API must be called after bk\_bt\_a2dp\_sink\_init().

    参数
    :   **remote\_bda, :** – **\[in\]** remote bluetooth device address

    返回
    :   - BK\_ERR\_BT\_SUCCESS: success
        - others: fail

<a id="_CPPv426bk_bt_a2dp_sink_disconnectP7uint8_t"></a>

<a id="_CPPv326bk_bt_a2dp_sink_disconnectP7uint8_t"></a> <a id="_CPPv226bk_bt_a2dp_sink_disconnectP7uint8_t"></a> <a id="bk_bt_a2dp_sink_disconnect__uint8_tP"></a> <a id="dm__bt_8h_1a51a2a5f7bcded1a05d573e4e499d5a3d"></a> bt\_err\_t bk\_bt\_a2dp\_sink\_disconnect(uint8\_t \*remote\_bda)
:   Disconnect from the remote A2DP source device. This API must be called after bk\_bt\_a2dp\_sink\_init().

    参数
    :   **remote\_bda, :** – **\[in\]** remote bluetooth device address

    返回
    :   - BK\_ERR\_BT\_SUCCESS: success
        - others: fail

<a id="_CPPv419bk_bt_avrcp_ct_initv"></a>

<a id="_CPPv319bk_bt_avrcp_ct_initv"></a> <a id="_CPPv219bk_bt_avrcp_ct_initv"></a> <a id="bk_bt_avrcp_ct_init__void"></a> <a id="dm__bt_8h_1a05f83b873d0086a261259a7523ea3e0f"></a> bt\_err\_t bk\_bt\_avrcp\_ct\_init(void)
:   Initialize the bluetooth AVRCP controller module.

    返回
    :   - BK\_ERR\_BT\_SUCCESS: success
        - others: fail

<a id="_CPPv421bk_bt_avrcp_ct_deinitv"></a>

<a id="_CPPv321bk_bt_avrcp_ct_deinitv"></a> <a id="_CPPv221bk_bt_avrcp_ct_deinitv"></a> <a id="bk_bt_avrcp_ct_deinit__void"></a> <a id="dm__bt_8h_1a9dcc948eeb6ada4e51a9f97499006377"></a> bt\_err\_t bk\_bt\_avrcp\_ct\_deinit(void)
:   Deinitialize the bluetooth AVRCP controller module.

    返回
    :   - BK\_ERR\_BT\_SUCCESS: success
        - others: fail

<a id="_CPPv432bk_bt_avrcp_ct_register_callback16bk_avrcp_ct_cb_t"></a>

<a id="_CPPv332bk_bt_avrcp_ct_register_callback16bk_avrcp_ct_cb_t"></a> <a id="_CPPv232bk_bt_avrcp_ct_register_callback16bk_avrcp_ct_cb_t"></a> <a id="bk_bt_avrcp_ct_register_callback__bk_avrcp_ct_cb_t"></a> <a id="dm__bt_8h_1a98b9a3d45af6f021d08b8a4634fcbe96"></a> bt\_err\_t bk\_bt\_avrcp\_ct\_register\_callback([bk\_avrcp\_ct\_cb\_t](#_CPPv416bk_avrcp_ct_cb_t "bk_avrcp_ct_cb_t") callback)
:   Register application callbacks to AVRCP module.

    参数
    :   **callback, :** – **\[in\]** AVRCP controller callback function

    返回
    :   - BK\_ERR\_BT\_SUCCESS: success
        - others: fail

<a id="_CPPv443bk_bt_avrcp_ct_send_get_rn_capabilities_cmdP7uint8_t"></a>

<a id="_CPPv343bk_bt_avrcp_ct_send_get_rn_capabilities_cmdP7uint8_t"></a> <a id="_CPPv243bk_bt_avrcp_ct_send_get_rn_capabilities_cmdP7uint8_t"></a> <a id="bk_bt_avrcp_ct_send_get_rn_capabilities_cmd__uint8_tP"></a> <a id="dm__bt_8h_1aa0ae75204679264e619ecde057ab5ef8"></a> bt\_err\_t bk\_bt\_avrcp\_ct\_send\_get\_rn\_capabilities\_cmd(uint8\_t \*remote\_bda)
:   Send GetCapabilities PDU to AVRCP target to retrieve remote device’s supported notification event\_ids. This function should be called after BK\_AVRCP\_CT\_CONNECTION\_STATE\_EVT is received and AVRCP connection is established.

    参数
    :   **remote\_bda, :** – **\[in\]** remote bluetooth device address

    返回
    :   - BK\_ERR\_BT\_SUCCESS: success
        - others: fail

<a id="_CPPv439bk_bt_ct_send_register_notification_cmdP7uint8_t7uint8_t8uint32_t"></a>

<a id="_CPPv339bk_bt_ct_send_register_notification_cmdP7uint8_t7uint8_t8uint32_t"></a> <a id="_CPPv239bk_bt_ct_send_register_notification_cmdP7uint8_t7uint8_t8uint32_t"></a> <a id="bk_bt_ct_send_register_notification_cmd__uint8_tP.uint8_t.uint32_t"></a> <a id="dm__bt_8h_1a09f768a8a1a0da6fa7c8fbed0fad30df"></a> bt\_err\_t bk\_bt\_ct\_send\_register\_notification\_cmd(uint8\_t \*remote\_bda, uint8\_t event\_id, uint32\_t event\_parameter)
:   Send register notification command to AVRCP target. This function should be called after BK\_AVRCP\_CT\_CONNECTION\_STATE\_EVT is received and AVRCP connection is established.

    参数
    :   - **remote\_bda, :** – **\[in\]** remote bluetooth device address
        - **event\_id** – **\[in\]** : id of events, e.g. BK\_AVRCP\_RN\_PLAY\_STATUS\_CHANGE, BK\_AVRCP\_RN\_TRACK\_CHANGE, etc.
        - **event\_parameter** – **\[in\]** : playback interval for BK\_AVRCP\_RN\_PLAY\_POS\_CHANGED; For other events , value of this parameter is ignored.

    返回
    :   - BK\_ERR\_BT\_SUCCESS: success
        - others: fail

<a id="_CPPv435bk_bt_avrcp_ct_send_passthrough_cmdP7uint8_t7uint8_t7uint8_t"></a>

<a id="_CPPv335bk_bt_avrcp_ct_send_passthrough_cmdP7uint8_t7uint8_t7uint8_t"></a> <a id="_CPPv235bk_bt_avrcp_ct_send_passthrough_cmdP7uint8_t7uint8_t7uint8_t"></a> <a id="bk_bt_avrcp_ct_send_passthrough_cmd__uint8_tP.uint8_t.uint8_t"></a> <a id="dm__bt_8h_1a1ae2337d958b6b0a4f5dc6722af52d67"></a> bt\_err\_t bk\_bt\_avrcp\_ct\_send\_passthrough\_cmd(uint8\_t \*remote\_bda, uint8\_t key\_code, uint8\_t key\_state)
:   Send passthrough command to AVRCP target. This function should be called after BK\_AVRCP\_CT\_CONNECTION\_STATE\_EVT is received and AVRCP connection is established.

    参数
    :   - **remote\_bda, :** – **\[in\]** remote bluetooth device address.
        - **key\_code** – **\[in\]** : passthrough command code, e.g. BK\_AVRCP\_PT\_CMD\_PLAY, BK\_AVRCP\_PT\_CMD\_STOP, etc.
        - **key\_state** – **\[in\]** : passthrough command key state, BK\_AVRCP\_PT\_CMD\_STATE\_PRESSED or BK\_AVRCP\_PT\_CMD\_STATE\_RELEASED

    返回
    :   - BK\_ERR\_BT\_SUCCESS: success
        - others: fail

<a id="_CPPv419bk_bt_avrcp_tg_initv"></a>

<a id="_CPPv319bk_bt_avrcp_tg_initv"></a> <a id="_CPPv219bk_bt_avrcp_tg_initv"></a> <a id="bk_bt_avrcp_tg_init__void"></a> <a id="dm__bt_8h_1a0f43a498c80b739f64c0bd8e8750e851"></a> bt\_err\_t bk\_bt\_avrcp\_tg\_init(void)
:   Initialize the bluetooth AVRCP target module.

    返回
    :   - BK\_ERR\_BT\_SUCCESS: success
        - others: fail

<a id="_CPPv421bk_bt_avrcp_tg_deinitv"></a>

<a id="_CPPv321bk_bt_avrcp_tg_deinitv"></a> <a id="_CPPv221bk_bt_avrcp_tg_deinitv"></a> <a id="bk_bt_avrcp_tg_deinit__void"></a> <a id="dm__bt_8h_1a9c881603be5f4304f893e200ecae26fc"></a> bt\_err\_t bk\_bt\_avrcp\_tg\_deinit(void)
:   Deinitialize the bluetooth AVRCP target module.

    返回
    :   - BK\_ERR\_BT\_SUCCESS: success
        - others: fail

<a id="_CPPv432bk_bt_avrcp_tg_register_callback16bk_avrcp_tg_cb_t"></a>

<a id="_CPPv332bk_bt_avrcp_tg_register_callback16bk_avrcp_tg_cb_t"></a> <a id="_CPPv232bk_bt_avrcp_tg_register_callback16bk_avrcp_tg_cb_t"></a> <a id="bk_bt_avrcp_tg_register_callback__bk_avrcp_tg_cb_t"></a> <a id="dm__bt_8h_1a6562799ebf8b35345a221329cc9c722a"></a> bt\_err\_t bk\_bt\_avrcp\_tg\_register\_callback([bk\_avrcp\_tg\_cb\_t](#_CPPv416bk_avrcp_tg_cb_t "bk_avrcp_tg_cb_t") callback)
:   Register application callbacks to AVRCP target module.

    参数
    :   **callback, :** – **\[in\]** AVRCP target callback function

    返回
    :   - BK\_ERR\_BT\_SUCCESS: success
        - others: fail

<a id="_CPPv429bk_bt_avrcp_tg_get_rn_evt_cap28bk_avrcp_rn_cap_api_method_tP26bk_avrcp_rn_evt_cap_mask_t"></a>

<a id="_CPPv329bk_bt_avrcp_tg_get_rn_evt_cap28bk_avrcp_rn_cap_api_method_tP26bk_avrcp_rn_evt_cap_mask_t"></a> <a id="_CPPv229bk_bt_avrcp_tg_get_rn_evt_cap28bk_avrcp_rn_cap_api_method_tP26bk_avrcp_rn_evt_cap_mask_t"></a> <a id="bk_bt_avrcp_tg_get_rn_evt_cap__bk_avrcp_rn_cap_api_method_t.bk_avrcp_rn_evt_cap_mask_tP"></a> <a id="dm__bt_8h_1acb418fcfaaf7860d121af48e889eb728"></a> bt\_err\_t bk\_bt\_avrcp\_tg\_get\_rn\_evt\_cap([bk\_avrcp\_rn\_cap\_api\_method\_t](#_CPPv428bk_avrcp_rn_cap_api_method_t "bk_avrcp_rn_cap_api_method_t") cap, [bk\_avrcp\_rn\_evt\_cap\_mask\_t](#_CPPv426bk_avrcp_rn_evt_cap_mask_t "bk_avrcp_rn_evt_cap_mask_t") \*evt\_set)
:   Get the requested event notification capabilies on local AVRC target. The capability is returned in a bit mask representation in evt\_set. This function should be called after bk\_avrcp\_tg\_init().

    ```
                 For capability type "BK_AVRCP_RN_CAP_API_METHOD_ALLOWED, the retrieved event set is constant and
                 it covers all of the notification events that can possibly be supported with current
                 implementation.

                 For capability type BK_AVRCP_RN_CAP_API_METHOD_CURRENT_ENABLE, the event set covers the notification
                 events selected to be supported under current configuration, The configuration can be
                 changed using bk_avrcp_tg_set_rn_evt_cap().
    ```

    返回
    :   - BK\_ERR\_BT\_SUCCESS: success
        - others: fail

<a id="_CPPv429bk_bt_avrcp_tg_set_rn_evt_capPK26bk_avrcp_rn_evt_cap_mask_t"></a>

<a id="_CPPv329bk_bt_avrcp_tg_set_rn_evt_capPK26bk_avrcp_rn_evt_cap_mask_t"></a> <a id="_CPPv229bk_bt_avrcp_tg_set_rn_evt_capPK26bk_avrcp_rn_evt_cap_mask_t"></a> <a id="bk_bt_avrcp_tg_set_rn_evt_cap__bk_avrcp_rn_evt_cap_mask_tCP"></a> <a id="dm__bt_8h_1a3dac5bddfe848d8b63e1597dc36e5999"></a> bt\_err\_t bk\_bt\_avrcp\_tg\_set\_rn\_evt\_cap(const [bk\_avrcp\_rn\_evt\_cap\_mask\_t](#_CPPv426bk_avrcp_rn_evt_cap_mask_t "bk_avrcp_rn_evt_cap_mask_t") \*evt\_set)
:   Set the event notification capabilities on local AVRCP target. The capability is given in a bit mask representation in evt\_set and must be a subset of allowed event IDs with current implementation. This function should be called after bk\_avrcp\_tg\_init().

    返回
    :   - BK\_ERR\_BT\_SUCCESS: success
        - others: fail

<a id="_CPPv426bk_bt_avrcp_tg_send_rn_rspP7uint8_t23bk_avrcp_rn_event_ids_t17bk_avrcp_rn_rsp_tP19bk_avrcp_rn_param_t"></a>

<a id="_CPPv326bk_bt_avrcp_tg_send_rn_rspP7uint8_t23bk_avrcp_rn_event_ids_t17bk_avrcp_rn_rsp_tP19bk_avrcp_rn_param_t"></a> <a id="_CPPv226bk_bt_avrcp_tg_send_rn_rspP7uint8_t23bk_avrcp_rn_event_ids_t17bk_avrcp_rn_rsp_tP19bk_avrcp_rn_param_t"></a> <a id="bk_bt_avrcp_tg_send_rn_rsp__uint8_tP.bk_avrcp_rn_event_ids_t.bk_avrcp_rn_rsp_t.bk_avrcp_rn_param_tP"></a> <a id="dm__bt_8h_1a3afd14e8c63ae716f354592835a6228b"></a> bt\_err\_t bk\_bt\_avrcp\_tg\_send\_rn\_rsp(uint8\_t \*addr, [bk\_avrcp\_rn\_event\_ids\_t](#_CPPv423bk_avrcp_rn_event_ids_t "bk_avrcp_rn_event_ids_t") event\_id, [bk\_avrcp\_rn\_rsp\_t](#_CPPv417bk_avrcp_rn_rsp_t "bk_avrcp_rn_rsp_t") rsp, [bk\_avrcp\_rn\_param\_t](#_CPPv419bk_avrcp_rn_param_t "bk_avrcp_rn_param_t") \*param)
:   Send RegisterNotification Response to remote AVRCP controller. Local event notification capability can be set using bk\_avrcp\_tg\_set\_rn\_evt\_cap(), in a bit mask representation in evt\_set. This function should be called after bk\_avrcp\_tg\_init().

    参数
    :   - **addr, :** – **\[in\]** peer addr
        - **event\_id, :** – **\[in\]** notification event ID that remote AVRCP CT registers
        - **rsp, :** – **\[in\]** notification response code
        - **param, :** – **\[in\]** parameters included in the specific notification

    返回
    :   - BK\_ERR\_BT\_SUCCESS: success
        - others: fail

<a id="_CPPv419bk_bt_avrcp_connectP7uint8_t"></a>

<a id="_CPPv319bk_bt_avrcp_connectP7uint8_t"></a> <a id="_CPPv219bk_bt_avrcp_connectP7uint8_t"></a> <a id="bk_bt_avrcp_connect__uint8_tP"></a> <a id="dm__bt_8h_1a172ff876d50e0f2d040b944845dfd44b"></a> bt\_err\_t bk\_bt\_avrcp\_connect(uint8\_t \*remote\_bda)
:   Connect to remote bluetooth AVRCP. This API must be called after bk\_bt\_avrcp\_ct\_init() or bk\_bt\_avrcp\_tg\_init.

    参数
    :   **remote\_bda, :** – **\[in\]** remote bluetooth device address

    返回
    :   - BK\_ERR\_BT\_SUCCESS: success
        - others: fail

<a id="_CPPv422bk_bt_a2dp_source_initv"></a>

<a id="_CPPv322bk_bt_a2dp_source_initv"></a> <a id="_CPPv222bk_bt_a2dp_source_initv"></a> <a id="bk_bt_a2dp_source_init__void"></a> <a id="dm__bt_8h_1a5e5d4bd49e552ccad922d201f6740c3f"></a> bt\_err\_t bk\_bt\_a2dp\_source\_init(void)
:   Initialize the bluetooth A2DP source module. A2DP can work independently.

    **Attention**
    :   sink/source must init only one.

    返回
    :   - BK\_ERR\_BT\_SUCCESS: if the initialization request is sent to lower layer successfully
        - others: fail

<a id="_CPPv437bk_a2dp_source_register_data_callback24bk_a2dp_source_data_cb_t"></a>

<a id="_CPPv337bk_a2dp_source_register_data_callback24bk_a2dp_source_data_cb_t"></a> <a id="_CPPv237bk_a2dp_source_register_data_callback24bk_a2dp_source_data_cb_t"></a> <a id="bk_a2dp_source_register_data_callback__bk_a2dp_source_data_cb_t"></a> <a id="dm__bt_8h_1a5797967a04d798b032ef028f7e15e730"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_a2dp\_source\_register\_data\_callback([bk\_a2dp\_source\_data\_cb\_t](#_CPPv424bk_a2dp_source_data_cb_t "bk_a2dp_source_data_cb_t") callback)
:   Register A2DP source data input function. For now, the input should be PCM data stream.

    参数
    :   **callback, :** – **\[in\]** A2DP source data callback function

    返回
    :   - BK\_ERR\_BT\_SUCCESS: success
        - others: fail

<a id="_CPPv434bk_a2dp_source_set_pcm_data_format8uint32_t7uint8_t7uint8_t"></a>

<a id="_CPPv334bk_a2dp_source_set_pcm_data_format8uint32_t7uint8_t7uint8_t"></a> <a id="_CPPv234bk_a2dp_source_set_pcm_data_format8uint32_t7uint8_t7uint8_t"></a> <a id="bk_a2dp_source_set_pcm_data_format__uint32_t.uint8_t.uint8_t"></a> <a id="dm__bt_8h_1a88444f5e7568e61c7f6b59840061a67d"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_a2dp\_source\_set\_pcm\_data\_format(uint32\_t sample\_rate, uint8\_t bit\_depth, uint8\_t channel\_count)
:   set a2dp source data format

    参数
    :   - **sample\_rate, :** – **\[in\]** pcm data sample rate, such as 8000 16000 32000 44100 48000\.
        - **bit\_depth** – **\[in\]** : pcm data bit depth, now support 16 bits only.
        - **channel\_count** – **\[in\]** : pcm data channel count, support 1 or 2 now.

    返回
    :   - BK\_ERR\_BT\_SUCCESS: success
        - others: fail

<a id="_CPPv425bk_bt_a2dp_source_connectP7uint8_t"></a>

<a id="_CPPv325bk_bt_a2dp_source_connectP7uint8_t"></a> <a id="_CPPv225bk_bt_a2dp_source_connectP7uint8_t"></a> <a id="bk_bt_a2dp_source_connect__uint8_tP"></a> <a id="dm__bt_8h_1a8b47cde7b1cc5b9baa48c93841c03dd5"></a> bt\_err\_t bk\_bt\_a2dp\_source\_connect(uint8\_t \*addr)
:   Connect to remote A2DP sink device. This API must be called after bk\_bt\_a2dp\_source\_init()

    参数
    :   **addr, :** – **\[in\]** remote bluetooth device address

    返回
    :   - BK\_ERR\_BT\_SUCCESS: connect request is sent to lower layer successfully
        - others: fail

<a id="_CPPv428bk_bt_a2dp_source_disconnectP7uint8_t"></a>

<a id="_CPPv328bk_bt_a2dp_source_disconnectP7uint8_t"></a> <a id="_CPPv228bk_bt_a2dp_source_disconnectP7uint8_t"></a> <a id="bk_bt_a2dp_source_disconnect__uint8_tP"></a> <a id="dm__bt_8h_1a55b454c848c5ae66dbabf98e63c2c966"></a> bt\_err\_t bk\_bt\_a2dp\_source\_disconnect(uint8\_t \*addr)
:   Disconnect from the remote A2DP sink device. This API must be called after bk\_bt\_a2dp\_source\_init()

    参数
    :   **addr, :** – **\[in\]** remote bluetooth device address

    返回
    :   ```
                     - BK_ERR_BT_SUCCESS: connect request is sent to lower layer successfully
                     - others: fail
        ```

<a id="_CPPv418bk_a2dp_media_ctrl20bk_a2dp_media_ctrl_t"></a>

<a id="_CPPv318bk_a2dp_media_ctrl20bk_a2dp_media_ctrl_t"></a> <a id="_CPPv218bk_a2dp_media_ctrl20bk_a2dp_media_ctrl_t"></a> <a id="bk_a2dp_media_ctrl__bk_a2dp_media_ctrl_t"></a> <a id="dm__bt_8h_1a359bea2bba78df5a7a86e19ce45cf922"></a> bt\_err\_t bk\_a2dp\_media\_ctrl([bk\_a2dp\_media\_ctrl\_t](#_CPPv420bk_a2dp_media_ctrl_t "bk_a2dp_media_ctrl_t") ctrl)
:   Media control commands. This API can be used for both A2DP sink and must be called after bk\_bt\_a2dp\_source\_init()

    **Attention**
    :   this function only used for a2dp source

    参数
    :   **ctrl, :** – **\[in\]** control commands for A2DP action

    返回
    :   - BK\_ERR\_BT\_SUCCESS: control command is sent to lower layer successfully
        - others: fail

<a id="_CPPv414bk_bt_spp_init24bt_spp_event_notify_cb_t"></a>

<a id="_CPPv314bk_bt_spp_init24bt_spp_event_notify_cb_t"></a> <a id="_CPPv214bk_bt_spp_init24bt_spp_event_notify_cb_t"></a> <a id="bk_bt_spp_init__bt_spp_event_notify_cb_t"></a> <a id="dm__bt_8h_1a65dc004ec72d12de838e8a5b4113bd4a"></a> bt\_err\_t bk\_bt\_spp\_init([bt\_spp\_event\_notify\_cb\_t](#_CPPv424bt_spp_event_notify_cb_t "bt_spp_event_notify_cb_t") bt\_spp\_event\_notify\_cb)
:   Initialize the bluetooth SPP module.

    **Attention**
    :   this function only used for SPP

    参数
    :   **bt\_spp\_event\_notify\_cb, :** – **\[in\]** SPP event callback function

    返回
    :   - BK\_ERR\_BT\_SUCCESS: control command is sent to lower layer successfully
        - others: fail

<a id="_CPPv415bk_bt_spp_startP8uint32_tP7uint8_tP8uint32_t"></a>

<a id="_CPPv315bk_bt_spp_startP8uint32_tP7uint8_tP8uint32_t"></a> <a id="_CPPv215bk_bt_spp_startP8uint32_tP7uint8_tP8uint32_t"></a> <a id="bk_bt_spp_start__uint32_tP.uint8_tP.uint32_tP"></a> <a id="dm__bt_8h_1a0749a14a9e2c4fb519ed13abc5663209"></a> bt\_err\_t bk\_bt\_spp\_start(uint32\_t \*spp\_handle, uint8\_t \*local\_server\_channel, uint32\_t \*spp\_record\_handle)
:   Start the bluetooth SPP server.

    **Attention**
    :   this function only used for SPP

    参数
    :   - **spp\_handle, :** – **\[out\]** the handle of the server.
        - **local\_server\_channel, :** – **\[out\]** the server channle.
        - **spp\_record\_handle, :** – **\[out\]** the db record handle

    返回
    :   - BK\_ERR\_BT\_SUCCESS: control command is sent to lower layer successfully
        - others: fail

<a id="_CPPv412bk_bt_spp_tx8uint32_tPc8uint16_t"></a>

<a id="_CPPv312bk_bt_spp_tx8uint32_tPc8uint16_t"></a> <a id="_CPPv212bk_bt_spp_tx8uint32_tPc8uint16_t"></a> <a id="bk_bt_spp_tx__uint32_t.cP.uint16_t"></a> <a id="dm__bt_8h_1abb8460888bddfcfdd81852118f1f2a01"></a> bt\_err\_t bk\_bt\_spp\_tx(uint32\_t spp\_handle, char \*data, uint16\_t len)
:   send spp data.

    **Attention**
    :   this function only used for SPP

    参数
    :   - **spp\_handle, :** – **\[in\]** the handle of the server.
        - **data, :** – **\[in\]** the data buffer addr.
        - **len, :** – **\[in\]** the data len.

    返回
    :   - BK\_ERR\_BT\_SUCCESS: control command is sent to lower layer successfully
        - others: fail

<a id="_CPPv421bk_bt_disconnect_linkP7uint8_t"></a>

<a id="_CPPv321bk_bt_disconnect_linkP7uint8_t"></a> <a id="_CPPv221bk_bt_disconnect_linkP7uint8_t"></a> <a id="bk_bt_disconnect_link__uint8_tP"></a> <a id="dm__bt_8h_1a391a43c9dd274b807a1f3a11b854c758"></a> bt\_err\_t bk\_bt\_disconnect\_link(uint8\_t \*addr)
:   This API can be used to disconnect the acl link.

    参数
    :   **addr, :** – **\[in\]** remote bluetooth device address

    返回
    :   ```
                     - BK_ERR_BT_SUCCESS: disconnect request is sent to lower layer successfully
                     - others: fail
        ```

<a id="_CPPv430bk_bt_create_connection_cancelP7uint8_t"></a>

<a id="_CPPv330bk_bt_create_connection_cancelP7uint8_t"></a> <a id="_CPPv230bk_bt_create_connection_cancelP7uint8_t"></a> <a id="bk_bt_create_connection_cancel__uint8_tP"></a> <a id="dm__bt_8h_1afe3b0a14ebc873a70836c80d9bce4b63"></a> bt\_err\_t bk\_bt\_create\_connection\_cancel(uint8\_t \*addr)
:   This API can be used to request cancellation of the ongoing connection creation process.

    参数
    :   **addr, :** – **\[in\]** remote bluetooth device address

    返回
    :   ```
                     - BK_ERR_BT_SUCCESS: cancel request is sent to lower layer successfully
                     - others: fail
        ```

<a id="_CPPv422bk_bt_set_page_timeout8uint16_t"></a>

<a id="_CPPv322bk_bt_set_page_timeout8uint16_t"></a> <a id="_CPPv222bk_bt_set_page_timeout8uint16_t"></a> <a id="bk_bt_set_page_timeout__uint16_t"></a> <a id="dm__bt_8h_1ab67c1e5e225e92fd0da1d7ced098d925"></a> bt\_err\_t bk\_bt\_set\_page\_timeout(uint16\_t timeout)
:   This api can be used to set the value for the Page\_Timeout configuration parameter.

    参数
    :   **timeout, :** – **\[in\]** Page Timeout measured in number of Baseband slots, unit of 0.625ms

    返回
    :   - BK\_ERR\_BT\_SUCCESS: success
        - others: fail

<a id="_CPPv428bk_bt_set_page_scan_activity8uint16_t8uint16_t"></a>

<a id="_CPPv328bk_bt_set_page_scan_activity8uint16_t8uint16_t"></a> <a id="_CPPv228bk_bt_set_page_scan_activity8uint16_t8uint16_t"></a> <a id="bk_bt_set_page_scan_activity__uint16_t.uint16_t"></a> <a id="dm__bt_8h_1a61fd60fce137f2e434eca7828424fa3e"></a> bt\_err\_t bk\_bt\_set\_page\_scan\_activity(uint16\_t interval, uint16\_t window)
:   This api can be used to set the value for the Page\_Scan\_Interval and Page\_Scan\_Window configuration parameters.

    参数
    :   - **interval, :** – **\[in\]** defines the amount of time between consecutive page scans, unit of 0.625ms,(Range: 0x0012 to 0x1000, only even values are valid)
        - **window, :** – **\[in\]** defines the amount of time for the duration of the page scan, unit of 0.625ms,(Range: 0x0011 to 0x1000, can only be less than or equal to the Page\_Scan\_Interval)

    返回
    :   - BK\_ERR\_BT\_SUCCESS: success
        - others: fail

<a id="api-typedefs"></a>

## API Typedefs

<a id="id1"></a>

### Header File

- [dm\_bt\_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/dm_bt_types.h)

<a id="unions"></a>

### Unions

<a id="_CPPv418bk_a2dp_cb_param_t"></a>

<a id="_CPPv318bk_a2dp_cb_param_t"></a> <a id="_CPPv218bk_a2dp_cb_param_t"></a> <a id="unionbk__a2dp__cb__param__t"></a> union bk\_a2dp\_cb\_param\_t
:   *#include \<dm\_bt\_types.h\>*

    A2DP state callback parameters.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18bk_a2dp_cb_param_t10conn_stateE"></a>

    <a id="_CPPv3N18bk_a2dp_cb_param_t10conn_stateE"></a> <a id="_CPPv2N18bk_a2dp_cb_param_t10conn_stateE"></a> <a id="bk_a2dp_cb_param_t::conn_state__bk_a2dp_cb_param_t::a2dp_conn_state_param"></a> <a id="unionbk__a2dp__cb__param__t_1a16c782ba2326da954640398a042ce485"></a> struct [bk\_a2dp\_cb\_param\_t](#_CPPv418bk_a2dp_cb_param_t "bk_a2dp_cb_param_t")::[a2dp\_conn\_state\_param](#_CPPv4N18bk_a2dp_cb_param_t21a2dp_conn_state_paramE "bk_a2dp_cb_param_t::a2dp_conn_state_param") conn\_state
    :   A2DP connection status

    <a id="_CPPv4N18bk_a2dp_cb_param_t11audio_stateE"></a>

    <a id="_CPPv3N18bk_a2dp_cb_param_t11audio_stateE"></a> <a id="_CPPv2N18bk_a2dp_cb_param_t11audio_stateE"></a> <a id="bk_a2dp_cb_param_t::audio_state__bk_a2dp_cb_param_t::a2dp_audio_state_param"></a> <a id="unionbk__a2dp__cb__param__t_1a2020711d73b2f367fd4c807b2fe48f55"></a> struct [bk\_a2dp\_cb\_param\_t](#_CPPv418bk_a2dp_cb_param_t "bk_a2dp_cb_param_t")::[a2dp\_audio\_state\_param](#_CPPv4N18bk_a2dp_cb_param_t22a2dp_audio_state_paramE "bk_a2dp_cb_param_t::a2dp_audio_state_param") audio\_state
    :   audio stream playing state

    <a id="_CPPv4N18bk_a2dp_cb_param_t9audio_cfgE"></a>

    <a id="_CPPv3N18bk_a2dp_cb_param_t9audio_cfgE"></a> <a id="_CPPv2N18bk_a2dp_cb_param_t9audio_cfgE"></a> <a id="bk_a2dp_cb_param_t::audio_cfg__bk_a2dp_cb_param_t::a2dp_audio_cfg_param"></a> <a id="unionbk__a2dp__cb__param__t_1a1ff6b0ca0d0e8e0280f7e86362059bb0"></a> struct [bk\_a2dp\_cb\_param\_t](#_CPPv418bk_a2dp_cb_param_t "bk_a2dp_cb_param_t")::[a2dp\_audio\_cfg\_param](#_CPPv4N18bk_a2dp_cb_param_t20a2dp_audio_cfg_paramE "bk_a2dp_cb_param_t::a2dp_audio_cfg_param") audio\_cfg
    :   media codec configuration information

    <a id="_CPPv4N18bk_a2dp_cb_param_t16audio_source_cfgE"></a>

    <a id="_CPPv3N18bk_a2dp_cb_param_t16audio_source_cfgE"></a> <a id="_CPPv2N18bk_a2dp_cb_param_t16audio_source_cfgE"></a> <a id="bk_a2dp_cb_param_t::audio_source_cfg__bk_a2dp_cb_param_t::a2dp_audio_source_cfg_param"></a> <a id="unionbk__a2dp__cb__param__t_1a51a83355971116d59fb96d73f60ae423"></a> struct [bk\_a2dp\_cb\_param\_t](#_CPPv418bk_a2dp_cb_param_t "bk_a2dp_cb_param_t")::[a2dp\_audio\_source\_cfg\_param](#_CPPv4N18bk_a2dp_cb_param_t27a2dp_audio_source_cfg_paramE "bk_a2dp_cb_param_t::a2dp_audio_source_cfg_param") audio\_source\_cfg
    :   media codec configuration information

    <a id="_CPPv4N18bk_a2dp_cb_param_t20a2dp_audio_cfg_paramE"></a>

    <a id="_CPPv3N18bk_a2dp_cb_param_t20a2dp_audio_cfg_paramE"></a> <a id="_CPPv2N18bk_a2dp_cb_param_t20a2dp_audio_cfg_paramE"></a> <a id="bk_a2dp_cb_param_t::a2dp_audio_cfg_param"></a> <a id="structbk__a2dp__cb__param__t_1_1a2dp__audio__cfg__param"></a> struct a2dp\_audio\_cfg\_param
    :   *#include \<dm\_bt\_types.h\>*

        BK\_A2DP\_AUDIO\_CFG\_EVT.

        <a id="breathe-section-title-public-members"></a>

        Public Members

        <a id="_CPPv4N18bk_a2dp_cb_param_t20a2dp_audio_cfg_param10remote_bdaE"></a>

        <a id="_CPPv3N18bk_a2dp_cb_param_t20a2dp_audio_cfg_param10remote_bdaE"></a> <a id="_CPPv2N18bk_a2dp_cb_param_t20a2dp_audio_cfg_param10remote_bdaE"></a> <a id="bk_a2dp_cb_param_t::a2dp_audio_cfg_param::remote_bda__uint8_tA"></a> <a id="structbk__a2dp__cb__param__t_1_1a2dp__audio__cfg__param_1aa0c9625de8ba349940820e1be91c0cce"></a> uint8\_t remote\_bda\[6\]
        :   remote bluetooth device address

        <a id="_CPPv4N18bk_a2dp_cb_param_t20a2dp_audio_cfg_param3mccE"></a>

        <a id="_CPPv3N18bk_a2dp_cb_param_t20a2dp_audio_cfg_param3mccE"></a> <a id="_CPPv2N18bk_a2dp_cb_param_t20a2dp_audio_cfg_param3mccE"></a> <a id="bk_a2dp_cb_param_t::a2dp_audio_cfg_param::mcc__bk_a2dp_mcc_t"></a> <a id="structbk__a2dp__cb__param__t_1_1a2dp__audio__cfg__param_1a1a646edf4611532b93d132cd2cbd53cf"></a> [bk\_a2dp\_mcc\_t](#_CPPv413bk_a2dp_mcc_t "bk_a2dp_mcc_t") mcc
        :   A2DP media codec capability information

    <a id="_CPPv4N18bk_a2dp_cb_param_t27a2dp_audio_source_cfg_paramE"></a>

    <a id="_CPPv3N18bk_a2dp_cb_param_t27a2dp_audio_source_cfg_paramE"></a> <a id="_CPPv2N18bk_a2dp_cb_param_t27a2dp_audio_source_cfg_paramE"></a> <a id="bk_a2dp_cb_param_t::a2dp_audio_source_cfg_param"></a> <a id="structbk__a2dp__cb__param__t_1_1a2dp__audio__source__cfg__param"></a> struct a2dp\_audio\_source\_cfg\_param
    :   *#include \<dm\_bt\_types.h\>*

        BK\_A2DP\_AUDIO\_SOURCE\_CFG\_EVT.

        <a id="breathe-section-title-public-members"></a>

        Public Members

        <a id="_CPPv4N18bk_a2dp_cb_param_t27a2dp_audio_source_cfg_param10remote_bdaE"></a>

        <a id="_CPPv3N18bk_a2dp_cb_param_t27a2dp_audio_source_cfg_param10remote_bdaE"></a> <a id="_CPPv2N18bk_a2dp_cb_param_t27a2dp_audio_source_cfg_param10remote_bdaE"></a> <a id="bk_a2dp_cb_param_t::a2dp_audio_source_cfg_param::remote_bda__uint8_tA"></a> <a id="structbk__a2dp__cb__param__t_1_1a2dp__audio__source__cfg__param_1a3928cdb23d078ac355385c0cb58dff5e"></a> uint8\_t remote\_bda\[6\]
        :   remote bluetooth device address

        <a id="_CPPv4N18bk_a2dp_cb_param_t27a2dp_audio_source_cfg_param3mtuE"></a>

        <a id="_CPPv3N18bk_a2dp_cb_param_t27a2dp_audio_source_cfg_param3mtuE"></a> <a id="_CPPv2N18bk_a2dp_cb_param_t27a2dp_audio_source_cfg_param3mtuE"></a> <a id="bk_a2dp_cb_param_t::a2dp_audio_source_cfg_param::mtu__uint16_t"></a> <a id="structbk__a2dp__cb__param__t_1_1a2dp__audio__source__cfg__param_1a39527dc5bf6a842b889fb0491c13c85b"></a> uint16\_t mtu

        <a id="_CPPv4N18bk_a2dp_cb_param_t27a2dp_audio_source_cfg_param3mccE"></a>

        <a id="_CPPv3N18bk_a2dp_cb_param_t27a2dp_audio_source_cfg_param3mccE"></a> <a id="_CPPv2N18bk_a2dp_cb_param_t27a2dp_audio_source_cfg_param3mccE"></a> <a id="bk_a2dp_cb_param_t::a2dp_audio_source_cfg_param::mcc__bk_a2dp_mcc_t"></a> <a id="structbk__a2dp__cb__param__t_1_1a2dp__audio__source__cfg__param_1a36630858c8456d7e08c186e4163960b1"></a> [bk\_a2dp\_mcc\_t](#_CPPv413bk_a2dp_mcc_t "bk_a2dp_mcc_t") mcc
        :   max payload len, only used in source A2DP media codec capability information

    <a id="_CPPv4N18bk_a2dp_cb_param_t22a2dp_audio_state_paramE"></a>

    <a id="_CPPv3N18bk_a2dp_cb_param_t22a2dp_audio_state_paramE"></a> <a id="_CPPv2N18bk_a2dp_cb_param_t22a2dp_audio_state_paramE"></a> <a id="bk_a2dp_cb_param_t::a2dp_audio_state_param"></a> <a id="structbk__a2dp__cb__param__t_1_1a2dp__audio__state__param"></a> struct a2dp\_audio\_state\_param
    :   *#include \<dm\_bt\_types.h\>*

        BK\_A2DP\_AUDIO\_STATE\_EVT.

        <a id="breathe-section-title-public-members"></a>

        Public Members

        <a id="_CPPv4N18bk_a2dp_cb_param_t22a2dp_audio_state_param5stateE"></a>

        <a id="_CPPv3N18bk_a2dp_cb_param_t22a2dp_audio_state_param5stateE"></a> <a id="_CPPv2N18bk_a2dp_cb_param_t22a2dp_audio_state_param5stateE"></a> <a id="bk_a2dp_cb_param_t::a2dp_audio_state_param::state__bk_a2dp_audio_state_t"></a> <a id="structbk__a2dp__cb__param__t_1_1a2dp__audio__state__param_1a7ab7aafdd602e75670bf9f0ef57a14df"></a> [bk\_a2dp\_audio\_state\_t](#_CPPv421bk_a2dp_audio_state_t "bk_a2dp_audio_state_t") state
        :   one of the values from bk\_a2dp\_audio\_state\_t

        <a id="_CPPv4N18bk_a2dp_cb_param_t22a2dp_audio_state_param10remote_bdaE"></a>

        <a id="_CPPv3N18bk_a2dp_cb_param_t22a2dp_audio_state_param10remote_bdaE"></a> <a id="_CPPv2N18bk_a2dp_cb_param_t22a2dp_audio_state_param10remote_bdaE"></a> <a id="bk_a2dp_cb_param_t::a2dp_audio_state_param::remote_bda__uint8_tA"></a> <a id="structbk__a2dp__cb__param__t_1_1a2dp__audio__state__param_1a8be843fa2c8a4c0bc15dd52dd863f1e3"></a> uint8\_t remote\_bda\[6\]
        :   remote bluetooth device address

    <a id="_CPPv4N18bk_a2dp_cb_param_t21a2dp_conn_state_paramE"></a>

    <a id="_CPPv3N18bk_a2dp_cb_param_t21a2dp_conn_state_paramE"></a> <a id="_CPPv2N18bk_a2dp_cb_param_t21a2dp_conn_state_paramE"></a> <a id="bk_a2dp_cb_param_t::a2dp_conn_state_param"></a> <a id="structbk__a2dp__cb__param__t_1_1a2dp__conn__state__param"></a> struct a2dp\_conn\_state\_param
    :   *#include \<dm\_bt\_types.h\>*

        BK\_A2DP\_CONNECTION\_STATE\_EVT.

        <a id="breathe-section-title-public-members"></a>

        Public Members

        <a id="_CPPv4N18bk_a2dp_cb_param_t21a2dp_conn_state_param5stateE"></a>

        <a id="_CPPv3N18bk_a2dp_cb_param_t21a2dp_conn_state_param5stateE"></a> <a id="_CPPv2N18bk_a2dp_cb_param_t21a2dp_conn_state_param5stateE"></a> <a id="bk_a2dp_cb_param_t::a2dp_conn_state_param::state__bk_a2dp_connection_state_t"></a> <a id="structbk__a2dp__cb__param__t_1_1a2dp__conn__state__param_1aa4846a9dc530ecdf62dac92c79983a78"></a> [bk\_a2dp\_connection\_state\_t](#_CPPv426bk_a2dp_connection_state_t "bk_a2dp_connection_state_t") state
        :   one of values from bk\_a2dp\_connection\_state\_t

        <a id="_CPPv4N18bk_a2dp_cb_param_t21a2dp_conn_state_param10remote_bdaE"></a>

        <a id="_CPPv3N18bk_a2dp_cb_param_t21a2dp_conn_state_param10remote_bdaE"></a> <a id="_CPPv2N18bk_a2dp_cb_param_t21a2dp_conn_state_param10remote_bdaE"></a> <a id="bk_a2dp_cb_param_t::a2dp_conn_state_param::remote_bda__uint8_tA"></a> <a id="structbk__a2dp__cb__param__t_1_1a2dp__conn__state__param_1a70409b003ec97252a423100a1faad791"></a> uint8\_t remote\_bda\[6\]
        :   remote bluetooth device address

        <a id="_CPPv4N18bk_a2dp_cb_param_t21a2dp_conn_state_param8disc_rsnE"></a>

        <a id="_CPPv3N18bk_a2dp_cb_param_t21a2dp_conn_state_param8disc_rsnE"></a> <a id="_CPPv2N18bk_a2dp_cb_param_t21a2dp_conn_state_param8disc_rsnE"></a> <a id="bk_a2dp_cb_param_t::a2dp_conn_state_param::disc_rsn__bk_a2dp_disc_rsn_t"></a> <a id="structbk__a2dp__cb__param__t_1_1a2dp__conn__state__param_1a301a64c4c1e86c2d1e638147eba2f909"></a> [bk\_a2dp\_disc\_rsn\_t](#_CPPv418bk_a2dp_disc_rsn_t "bk_a2dp_disc_rsn_t") disc\_rsn
        :   reason of disconnection for “DISCONNECTED”

<a id="_CPPv420bk_bt_gap_cb_param_t"></a>

<a id="_CPPv320bk_bt_gap_cb_param_t"></a> <a id="_CPPv220bk_bt_gap_cb_param_t"></a> <a id="unionbk__bt__gap__cb__param__t"></a> union bk\_bt\_gap\_cb\_param\_t
:   *#include \<dm\_bt\_types.h\>*

    GAP state callback parameters.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N20bk_bt_gap_cb_param_t8disc_resE"></a>

    <a id="_CPPv3N20bk_bt_gap_cb_param_t8disc_resE"></a> <a id="_CPPv2N20bk_bt_gap_cb_param_t8disc_resE"></a> <a id="bk_bt_gap_cb_param_t::disc_res__bk_bt_gap_cb_param_t::disc_res_param"></a> <a id="unionbk__bt__gap__cb__param__t_1a01f576443a7972242435a20f48107154"></a> struct [bk\_bt\_gap\_cb\_param\_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[disc\_res\_param](#_CPPv4N20bk_bt_gap_cb_param_t14disc_res_paramE "bk_bt_gap_cb_param_t::disc_res_param") disc\_res
    :   discovery result parameter struct

    <a id="_CPPv4N20bk_bt_gap_cb_param_t11disc_st_chgE"></a>

    <a id="_CPPv3N20bk_bt_gap_cb_param_t11disc_st_chgE"></a> <a id="_CPPv2N20bk_bt_gap_cb_param_t11disc_st_chgE"></a> <a id="bk_bt_gap_cb_param_t::disc_st_chg__bk_bt_gap_cb_param_t::disc_state_changed_param"></a> <a id="unionbk__bt__gap__cb__param__t_1a29a0230a6be4978cbc4e8e91993efebe"></a> struct [bk\_bt\_gap\_cb\_param\_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[disc\_state\_changed\_param](#_CPPv4N20bk_bt_gap_cb_param_t24disc_state_changed_paramE "bk_bt_gap_cb_param_t::disc_state_changed_param") disc\_st\_chg
    :   discovery state changed parameter struct

    <a id="_CPPv4N20bk_bt_gap_cb_param_t9auth_cmplE"></a>

    <a id="_CPPv3N20bk_bt_gap_cb_param_t9auth_cmplE"></a> <a id="_CPPv2N20bk_bt_gap_cb_param_t9auth_cmplE"></a> <a id="bk_bt_gap_cb_param_t::auth_cmpl__bk_bt_gap_cb_param_t::auth_cmpl_param"></a> <a id="unionbk__bt__gap__cb__param__t_1a9ec741deb4537d4c650862d15456f6ba"></a> struct [bk\_bt\_gap\_cb\_param\_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[auth\_cmpl\_param](#_CPPv4N20bk_bt_gap_cb_param_t15auth_cmpl_paramE "bk_bt_gap_cb_param_t::auth_cmpl_param") auth\_cmpl
    :   authentication complete parameter struct

    <a id="_CPPv4N20bk_bt_gap_cb_param_t18acl_conn_cmpl_statE"></a>

    <a id="_CPPv3N20bk_bt_gap_cb_param_t18acl_conn_cmpl_statE"></a> <a id="_CPPv2N20bk_bt_gap_cb_param_t18acl_conn_cmpl_statE"></a> <a id="bk_bt_gap_cb_param_t::acl_conn_cmpl_stat__bk_bt_gap_cb_param_t::acl_conn_cmpl_stat_param"></a> <a id="unionbk__bt__gap__cb__param__t_1ac3d5eed3d50f91f181c7034e5bdcd52f"></a> struct [bk\_bt\_gap\_cb\_param\_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[acl\_conn\_cmpl\_stat\_param](#_CPPv4N20bk_bt_gap_cb_param_t24acl_conn_cmpl_stat_paramE "bk_bt_gap_cb_param_t::acl_conn_cmpl_stat_param") acl\_conn\_cmpl\_stat
    :   ACL connection complete status parameter struct

    <a id="_CPPv4N20bk_bt_gap_cb_param_t21acl_disconn_cmpl_statE"></a>

    <a id="_CPPv3N20bk_bt_gap_cb_param_t21acl_disconn_cmpl_statE"></a> <a id="_CPPv2N20bk_bt_gap_cb_param_t21acl_disconn_cmpl_statE"></a> <a id="bk_bt_gap_cb_param_t::acl_disconn_cmpl_stat__bk_bt_gap_cb_param_t::acl_disconn_cmpl_stat_param"></a> <a id="unionbk__bt__gap__cb__param__t_1a4008c16b5c8d2e50fd476e269cd92f73"></a> struct [bk\_bt\_gap\_cb\_param\_t](#_CPPv420bk_bt_gap_cb_param_t "bk_bt_gap_cb_param_t")::[acl\_disconn\_cmpl\_stat\_param](#_CPPv4N20bk_bt_gap_cb_param_t27acl_disconn_cmpl_stat_paramE "bk_bt_gap_cb_param_t::acl_disconn_cmpl_stat_param") acl\_disconn\_cmpl\_stat
    :   ACL disconnection complete status parameter struct

    <a id="_CPPv4N20bk_bt_gap_cb_param_t24acl_conn_cmpl_stat_paramE"></a>

    <a id="_CPPv3N20bk_bt_gap_cb_param_t24acl_conn_cmpl_stat_paramE"></a> <a id="_CPPv2N20bk_bt_gap_cb_param_t24acl_conn_cmpl_stat_paramE"></a> <a id="bk_bt_gap_cb_param_t::acl_conn_cmpl_stat_param"></a> <a id="structbk__bt__gap__cb__param__t_1_1acl__conn__cmpl__stat__param"></a> struct acl\_conn\_cmpl\_stat\_param
    :   *#include \<dm\_bt\_types.h\>*

        BK\_DM\_GAP\_ACL\_CONN\_CMPL\_STAT\_EVT.

        <a id="breathe-section-title-public-members"></a>

        Public Members

        <a id="_CPPv4N20bk_bt_gap_cb_param_t24acl_conn_cmpl_stat_param4statE"></a>

        <a id="_CPPv3N20bk_bt_gap_cb_param_t24acl_conn_cmpl_stat_param4statE"></a> <a id="_CPPv2N20bk_bt_gap_cb_param_t24acl_conn_cmpl_stat_param4statE"></a> <a id="bk_bt_gap_cb_param_t::acl_conn_cmpl_stat_param::stat__uint8_t"></a> <a id="structbk__bt__gap__cb__param__t_1_1acl__conn__cmpl__stat__param_1ab592460a481e584b6d93fcab5e8d7836"></a> uint8\_t stat
        :   ACL connection status

        <a id="_CPPv4N20bk_bt_gap_cb_param_t24acl_conn_cmpl_stat_param3bdaE"></a>

        <a id="_CPPv3N20bk_bt_gap_cb_param_t24acl_conn_cmpl_stat_param3bdaE"></a> <a id="_CPPv2N20bk_bt_gap_cb_param_t24acl_conn_cmpl_stat_param3bdaE"></a> <a id="bk_bt_gap_cb_param_t::acl_conn_cmpl_stat_param::bda__uint8_tA"></a> <a id="structbk__bt__gap__cb__param__t_1_1acl__conn__cmpl__stat__param_1adf4bfa692508c224616a7f32e4e03ddb"></a> uint8\_t bda\[6\]
        :   remote bluetooth device address

    <a id="_CPPv4N20bk_bt_gap_cb_param_t27acl_disconn_cmpl_stat_paramE"></a>

    <a id="_CPPv3N20bk_bt_gap_cb_param_t27acl_disconn_cmpl_stat_paramE"></a> <a id="_CPPv2N20bk_bt_gap_cb_param_t27acl_disconn_cmpl_stat_paramE"></a> <a id="bk_bt_gap_cb_param_t::acl_disconn_cmpl_stat_param"></a> <a id="structbk__bt__gap__cb__param__t_1_1acl__disconn__cmpl__stat__param"></a> struct acl\_disconn\_cmpl\_stat\_param
    :   *#include \<dm\_bt\_types.h\>*

        BK\_DM\_BT\_GAP\_ACL\_DISCONN\_CMPL\_STAT\_EVT.

        <a id="breathe-section-title-public-members"></a>

        Public Members

        <a id="_CPPv4N20bk_bt_gap_cb_param_t27acl_disconn_cmpl_stat_param6reasonE"></a>

        <a id="_CPPv3N20bk_bt_gap_cb_param_t27acl_disconn_cmpl_stat_param6reasonE"></a> <a id="_CPPv2N20bk_bt_gap_cb_param_t27acl_disconn_cmpl_stat_param6reasonE"></a> <a id="bk_bt_gap_cb_param_t::acl_disconn_cmpl_stat_param::reason__uint8_t"></a> <a id="structbk__bt__gap__cb__param__t_1_1acl__disconn__cmpl__stat__param_1a896b1d607838aff47b18771b97452fcb"></a> uint8\_t reason
        :   ACL disconnection reason

        <a id="_CPPv4N20bk_bt_gap_cb_param_t27acl_disconn_cmpl_stat_param3bdaE"></a>

        <a id="_CPPv3N20bk_bt_gap_cb_param_t27acl_disconn_cmpl_stat_param3bdaE"></a> <a id="_CPPv2N20bk_bt_gap_cb_param_t27acl_disconn_cmpl_stat_param3bdaE"></a> <a id="bk_bt_gap_cb_param_t::acl_disconn_cmpl_stat_param::bda__uint8_tA"></a> <a id="structbk__bt__gap__cb__param__t_1_1acl__disconn__cmpl__stat__param_1abe54c281310ac4f2dfe025fafa320a9d"></a> uint8\_t bda\[6\]
        :   remote bluetooth device address

    <a id="_CPPv4N20bk_bt_gap_cb_param_t15auth_cmpl_paramE"></a>

    <a id="_CPPv3N20bk_bt_gap_cb_param_t15auth_cmpl_paramE"></a> <a id="_CPPv2N20bk_bt_gap_cb_param_t15auth_cmpl_paramE"></a> <a id="bk_bt_gap_cb_param_t::auth_cmpl_param"></a> <a id="structbk__bt__gap__cb__param__t_1_1auth__cmpl__param"></a> struct auth\_cmpl\_param
    :   *#include \<dm\_bt\_types.h\>*

        BK\_DM\_BT\_GAP\_AUTH\_CMPL\_EVT.

        <a id="breathe-section-title-public-members"></a>

        Public Members

        <a id="_CPPv4N20bk_bt_gap_cb_param_t15auth_cmpl_param3bdaE"></a>

        <a id="_CPPv3N20bk_bt_gap_cb_param_t15auth_cmpl_param3bdaE"></a> <a id="_CPPv2N20bk_bt_gap_cb_param_t15auth_cmpl_param3bdaE"></a> <a id="bk_bt_gap_cb_param_t::auth_cmpl_param::bda__uint8_tA"></a> <a id="structbk__bt__gap__cb__param__t_1_1auth__cmpl__param_1a44f9d33a1d94fc9f3106ff4705f360b8"></a> uint8\_t bda\[6\]
        :   remote bluetooth device address

        <a id="_CPPv4N20bk_bt_gap_cb_param_t15auth_cmpl_param4statE"></a>

        <a id="_CPPv3N20bk_bt_gap_cb_param_t15auth_cmpl_param4statE"></a> <a id="_CPPv2N20bk_bt_gap_cb_param_t15auth_cmpl_param4statE"></a> <a id="bk_bt_gap_cb_param_t::auth_cmpl_param::stat__uint8_t"></a> <a id="structbk__bt__gap__cb__param__t_1_1auth__cmpl__param_1a5aeccaf745a90831dbcc08948c68429a"></a> uint8\_t stat
        :   authentication complete status

    <a id="_CPPv4N20bk_bt_gap_cb_param_t14disc_res_paramE"></a>

    <a id="_CPPv3N20bk_bt_gap_cb_param_t14disc_res_paramE"></a> <a id="_CPPv2N20bk_bt_gap_cb_param_t14disc_res_paramE"></a> <a id="bk_bt_gap_cb_param_t::disc_res_param"></a> <a id="structbk__bt__gap__cb__param__t_1_1disc__res__param"></a> struct disc\_res\_param
    :   *#include \<dm\_bt\_types.h\>*

        BK\_DM\_BT\_GAP\_DISC\_RES\_EVT.

        <a id="breathe-section-title-public-members"></a>

        Public Members

        <a id="_CPPv4N20bk_bt_gap_cb_param_t14disc_res_param3bdaE"></a>

        <a id="_CPPv3N20bk_bt_gap_cb_param_t14disc_res_param3bdaE"></a> <a id="_CPPv2N20bk_bt_gap_cb_param_t14disc_res_param3bdaE"></a> <a id="bk_bt_gap_cb_param_t::disc_res_param::bda__uint8_tA"></a> <a id="structbk__bt__gap__cb__param__t_1_1disc__res__param_1a2efb2f4dfe8259ad1ef3ed571b2f36ac"></a> uint8\_t bda\[6\]
        :   remote bluetooth device address

        <a id="_CPPv4N20bk_bt_gap_cb_param_t14disc_res_param8num_propE"></a>

        <a id="_CPPv3N20bk_bt_gap_cb_param_t14disc_res_param8num_propE"></a> <a id="_CPPv2N20bk_bt_gap_cb_param_t14disc_res_param8num_propE"></a> <a id="bk_bt_gap_cb_param_t::disc_res_param::num_prop__i"></a> <a id="structbk__bt__gap__cb__param__t_1_1disc__res__param_1a50b5b3077c9c262b97fdbdf095a332a5"></a> int num\_prop
        :   number of properties got

        <a id="_CPPv4N20bk_bt_gap_cb_param_t14disc_res_param4propE"></a>

        <a id="_CPPv3N20bk_bt_gap_cb_param_t14disc_res_param4propE"></a> <a id="_CPPv2N20bk_bt_gap_cb_param_t14disc_res_param4propE"></a> <a id="bk_bt_gap_cb_param_t::disc_res_param::prop__bk_bt_gap_dev_prop_tP"></a> <a id="structbk__bt__gap__cb__param__t_1_1disc__res__param_1a21eb68cf60ef9504bf48f0606d975f4b"></a> [bk\_bt\_gap\_dev\_prop\_t](#_CPPv420bk_bt_gap_dev_prop_t "bk_bt_gap_dev_prop_t") \*prop
        :   properties discovered from the new device

    <a id="_CPPv4N20bk_bt_gap_cb_param_t24disc_state_changed_paramE"></a>

    <a id="_CPPv3N20bk_bt_gap_cb_param_t24disc_state_changed_paramE"></a> <a id="_CPPv2N20bk_bt_gap_cb_param_t24disc_state_changed_paramE"></a> <a id="bk_bt_gap_cb_param_t::disc_state_changed_param"></a> <a id="structbk__bt__gap__cb__param__t_1_1disc__state__changed__param"></a> struct disc\_state\_changed\_param
    :   *#include \<dm\_bt\_types.h\>*

        BK\_DM\_BT\_GAP\_DISC\_STATE\_CHANGED\_EVT.

        <a id="breathe-section-title-public-members"></a>

        Public Members

        <a id="_CPPv4N20bk_bt_gap_cb_param_t24disc_state_changed_param5stateE"></a>

        <a id="_CPPv3N20bk_bt_gap_cb_param_t24disc_state_changed_param5stateE"></a> <a id="_CPPv2N20bk_bt_gap_cb_param_t24disc_state_changed_param5stateE"></a> <a id="bk_bt_gap_cb_param_t::disc_state_changed_param::state__bk_bt_gap_discovery_state_t"></a> <a id="structbk__bt__gap__cb__param__t_1_1disc__state__changed__param_1a146672efae0c5979201e731c19bb71fa"></a> [bk\_bt\_gap\_discovery\_state\_t](#_CPPv427bk_bt_gap_discovery_state_t "bk_bt_gap_discovery_state_t") state
        :   discovery state

<a id="_CPPv419bk_avrcp_rn_param_t"></a>

<a id="_CPPv319bk_avrcp_rn_param_t"></a> <a id="_CPPv219bk_avrcp_rn_param_t"></a> <a id="unionbk__avrcp__rn__param__t"></a> union bk\_avrcp\_rn\_param\_t
:   *#include \<dm\_bt\_types.h\>*

    AVRCP notification parameters.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N19bk_avrcp_rn_param_t6volumeE"></a>

    <a id="_CPPv3N19bk_avrcp_rn_param_t6volumeE"></a> <a id="_CPPv2N19bk_avrcp_rn_param_t6volumeE"></a> <a id="bk_avrcp_rn_param_t::volume__uint8_t"></a> <a id="unionbk__avrcp__rn__param__t_1aad10cabcea6d19cc18d1d226a4db3fb9"></a> uint8\_t volume
    :   response data for BK\_AVRCP\_RN\_VOLUME\_CHANGE, ranges 0..127

    <a id="_CPPv4N19bk_avrcp_rn_param_t8playbackE"></a>

    <a id="_CPPv3N19bk_avrcp_rn_param_t8playbackE"></a> <a id="_CPPv2N19bk_avrcp_rn_param_t8playbackE"></a> <a id="bk_avrcp_rn_param_t::playback__bk_avrcp_playback_stat_t"></a> <a id="unionbk__avrcp__rn__param__t_1ae7b00714f8a3d6aa3ee7b32fc1155b1e"></a> [bk\_avrcp\_playback\_stat\_t](#_CPPv424bk_avrcp_playback_stat_t "bk_avrcp_playback_stat_t") playback
    :   response data for BK\_AVRCP\_RN\_PLAY\_STATUS\_CHANGE

    <a id="_CPPv4N19bk_avrcp_rn_param_t6elm_idE"></a>

    <a id="_CPPv3N19bk_avrcp_rn_param_t6elm_idE"></a> <a id="_CPPv2N19bk_avrcp_rn_param_t6elm_idE"></a> <a id="bk_avrcp_rn_param_t::elm_id__uint8_tA"></a> <a id="unionbk__avrcp__rn__param__t_1aef9eadb982a1cf6354167335869d5e85"></a> uint8\_t elm\_id\[8\]
    :   response data for BK\_AVRCP\_RN\_TRACK\_CHANGE

    <a id="_CPPv4N19bk_avrcp_rn_param_t8play_posE"></a>

    <a id="_CPPv3N19bk_avrcp_rn_param_t8play_posE"></a> <a id="_CPPv2N19bk_avrcp_rn_param_t8play_posE"></a> <a id="bk_avrcp_rn_param_t::play_pos__uint32_t"></a> <a id="unionbk__avrcp__rn__param__t_1af8b376bc0ae407121833019e05294b7b"></a> uint32\_t play\_pos
    :   response data for BK\_AVRCP\_RN\_PLAY\_POS\_CHANGED, in millisecond

    <a id="_CPPv4N19bk_avrcp_rn_param_t4battE"></a>

    <a id="_CPPv3N19bk_avrcp_rn_param_t4battE"></a> <a id="_CPPv2N19bk_avrcp_rn_param_t4battE"></a> <a id="bk_avrcp_rn_param_t::batt__bk_avrcp_batt_stat_t"></a> <a id="unionbk__avrcp__rn__param__t_1a6d28dbfa8d62a053ecc15210af137d33"></a> [bk\_avrcp\_batt\_stat\_t](#_CPPv420bk_avrcp_batt_stat_t "bk_avrcp_batt_stat_t") batt
    :   response data for BK\_AVRCP\_RN\_BATTERY\_STATUS\_CHANGE

<a id="_CPPv422bk_avrcp_ct_cb_param_t"></a>

<a id="_CPPv322bk_avrcp_ct_cb_param_t"></a> <a id="_CPPv222bk_avrcp_ct_cb_param_t"></a> <a id="unionbk__avrcp__ct__cb__param__t"></a> union bk\_avrcp\_ct\_cb\_param\_t
:   *#include \<dm\_bt\_types.h\>*

    AVRCP controller callback parameters.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N22bk_avrcp_ct_cb_param_t10conn_stateE"></a>

    <a id="_CPPv3N22bk_avrcp_ct_cb_param_t10conn_stateE"></a> <a id="_CPPv2N22bk_avrcp_ct_cb_param_t10conn_stateE"></a> <a id="bk_avrcp_ct_cb_param_t::conn_state__bk_avrcp_ct_cb_param_t::avrcp_ct_conn_state_param"></a> <a id="unionbk__avrcp__ct__cb__param__t_1a4cf74d1bfcf687bfcd407ba87cfc81d7"></a> struct [bk\_avrcp\_ct\_cb\_param\_t](#_CPPv422bk_avrcp_ct_cb_param_t "bk_avrcp_ct_cb_param_t")::[avrcp\_ct\_conn\_state\_param](#_CPPv4N22bk_avrcp_ct_cb_param_t25avrcp_ct_conn_state_paramE "bk_avrcp_ct_cb_param_t::avrcp_ct_conn_state_param") conn\_state
    :   AVRCP connection status

    <a id="_CPPv4N22bk_avrcp_ct_cb_param_t10change_ntfE"></a>

    <a id="_CPPv3N22bk_avrcp_ct_cb_param_t10change_ntfE"></a> <a id="_CPPv2N22bk_avrcp_ct_cb_param_t10change_ntfE"></a> <a id="bk_avrcp_ct_cb_param_t::change_ntf__bk_avrcp_ct_cb_param_t::avrcp_ct_change_notify_param"></a> <a id="unionbk__avrcp__ct__cb__param__t_1a5217e66ff2c00216f85e5a5819a58920"></a> struct [bk\_avrcp\_ct\_cb\_param\_t](#_CPPv422bk_avrcp_ct_cb_param_t "bk_avrcp_ct_cb_param_t")::[avrcp\_ct\_change\_notify\_param](#_CPPv4N22bk_avrcp_ct_cb_param_t28avrcp_ct_change_notify_paramE "bk_avrcp_ct_cb_param_t::avrcp_ct_change_notify_param") change\_ntf
    :   notifications

    <a id="_CPPv4N22bk_avrcp_ct_cb_param_t15get_rn_caps_rspE"></a>

    <a id="_CPPv3N22bk_avrcp_ct_cb_param_t15get_rn_caps_rspE"></a> <a id="_CPPv2N22bk_avrcp_ct_cb_param_t15get_rn_caps_rspE"></a> <a id="bk_avrcp_ct_cb_param_t::get_rn_caps_rsp__bk_avrcp_ct_cb_param_t::avrcp_ct_get_rn_caps_rsp_param"></a> <a id="unionbk__avrcp__ct__cb__param__t_1a2ee389945eceb4d381a2df5c1402cc92"></a> struct [bk\_avrcp\_ct\_cb\_param\_t](#_CPPv422bk_avrcp_ct_cb_param_t "bk_avrcp_ct_cb_param_t")::[avrcp\_ct\_get\_rn\_caps\_rsp\_param](#_CPPv4N22bk_avrcp_ct_cb_param_t30avrcp_ct_get_rn_caps_rsp_paramE "bk_avrcp_ct_cb_param_t::avrcp_ct_get_rn_caps_rsp_param") get\_rn\_caps\_rsp
    :   get supported event capabilities response from AVRCP target

    <a id="_CPPv4N22bk_avrcp_ct_cb_param_t28avrcp_ct_change_notify_paramE"></a>

    <a id="_CPPv3N22bk_avrcp_ct_cb_param_t28avrcp_ct_change_notify_paramE"></a> <a id="_CPPv2N22bk_avrcp_ct_cb_param_t28avrcp_ct_change_notify_paramE"></a> <a id="bk_avrcp_ct_cb_param_t::avrcp_ct_change_notify_param"></a> <a id="structbk__avrcp__ct__cb__param__t_1_1avrcp__ct__change__notify__param"></a> struct avrcp\_ct\_change\_notify\_param
    :   *#include \<dm\_bt\_types.h\>*

        BK\_AVRCP\_CT\_CHANGE\_NOTIFY\_EVT.

        <a id="breathe-section-title-public-members"></a>

        Public Members

        <a id="_CPPv4N22bk_avrcp_ct_cb_param_t28avrcp_ct_change_notify_param8event_idE"></a>

        <a id="_CPPv3N22bk_avrcp_ct_cb_param_t28avrcp_ct_change_notify_param8event_idE"></a> <a id="_CPPv2N22bk_avrcp_ct_cb_param_t28avrcp_ct_change_notify_param8event_idE"></a> <a id="bk_avrcp_ct_cb_param_t::avrcp_ct_change_notify_param::event_id__uint8_t"></a> <a id="structbk__avrcp__ct__cb__param__t_1_1avrcp__ct__change__notify__param_1ac3a48adacda8524e79ec653cba884d18"></a> uint8\_t event\_id
        :   id of AVRCP event notification

        <a id="_CPPv4N22bk_avrcp_ct_cb_param_t28avrcp_ct_change_notify_param15event_parameterE"></a>

        <a id="_CPPv3N22bk_avrcp_ct_cb_param_t28avrcp_ct_change_notify_param15event_parameterE"></a> <a id="_CPPv2N22bk_avrcp_ct_cb_param_t28avrcp_ct_change_notify_param15event_parameterE"></a> <a id="bk_avrcp_ct_cb_param_t::avrcp_ct_change_notify_param::event_parameter__bk_avrcp_rn_param_t"></a> <a id="structbk__avrcp__ct__cb__param__t_1_1avrcp__ct__change__notify__param_1a44e3794d1abdf36dcf1944a01eeaaec4"></a> [bk\_avrcp\_rn\_param\_t](#_CPPv419bk_avrcp_rn_param_t "bk_avrcp_rn_param_t") event\_parameter
        :   event notification parameter

    <a id="_CPPv4N22bk_avrcp_ct_cb_param_t25avrcp_ct_conn_state_paramE"></a>

    <a id="_CPPv3N22bk_avrcp_ct_cb_param_t25avrcp_ct_conn_state_paramE"></a> <a id="_CPPv2N22bk_avrcp_ct_cb_param_t25avrcp_ct_conn_state_paramE"></a> <a id="bk_avrcp_ct_cb_param_t::avrcp_ct_conn_state_param"></a> <a id="structbk__avrcp__ct__cb__param__t_1_1avrcp__ct__conn__state__param"></a> struct avrcp\_ct\_conn\_state\_param
    :   *#include \<dm\_bt\_types.h\>*

        BK\_AVRCP\_CT\_CONNECTION\_STATE\_EVT.

        <a id="breathe-section-title-public-members"></a>

        Public Members

        <a id="_CPPv4N22bk_avrcp_ct_cb_param_t25avrcp_ct_conn_state_param9connectedE"></a>

        <a id="_CPPv3N22bk_avrcp_ct_cb_param_t25avrcp_ct_conn_state_param9connectedE"></a> <a id="_CPPv2N22bk_avrcp_ct_cb_param_t25avrcp_ct_conn_state_param9connectedE"></a> <a id="bk_avrcp_ct_cb_param_t::avrcp_ct_conn_state_param::connected__uint8_t"></a> <a id="structbk__avrcp__ct__cb__param__t_1_1avrcp__ct__conn__state__param_1adb9662c9502b9ee1c51cce04ba7ac395"></a> uint8\_t connected
        :   whether AVRCP connection is set up

        <a id="_CPPv4N22bk_avrcp_ct_cb_param_t25avrcp_ct_conn_state_param10remote_bdaE"></a>

        <a id="_CPPv3N22bk_avrcp_ct_cb_param_t25avrcp_ct_conn_state_param10remote_bdaE"></a> <a id="_CPPv2N22bk_avrcp_ct_cb_param_t25avrcp_ct_conn_state_param10remote_bdaE"></a> <a id="bk_avrcp_ct_cb_param_t::avrcp_ct_conn_state_param::remote_bda__uint8_tA"></a> <a id="structbk__avrcp__ct__cb__param__t_1_1avrcp__ct__conn__state__param_1a312d5ae30306f05976c0832351b2f503"></a> uint8\_t remote\_bda\[6\]
        :   remote bluetooth device address

    <a id="_CPPv4N22bk_avrcp_ct_cb_param_t30avrcp_ct_get_rn_caps_rsp_paramE"></a>

    <a id="_CPPv3N22bk_avrcp_ct_cb_param_t30avrcp_ct_get_rn_caps_rsp_paramE"></a> <a id="_CPPv2N22bk_avrcp_ct_cb_param_t30avrcp_ct_get_rn_caps_rsp_paramE"></a> <a id="bk_avrcp_ct_cb_param_t::avrcp_ct_get_rn_caps_rsp_param"></a> <a id="structbk__avrcp__ct__cb__param__t_1_1avrcp__ct__get__rn__caps__rsp__param"></a> struct avrcp\_ct\_get\_rn\_caps\_rsp\_param
    :   *#include \<dm\_bt\_types.h\>*

        BK\_AVRCP\_CT\_GET\_RN\_CAPABILITIES\_RSP\_EVT.

        <a id="breathe-section-title-public-members"></a>

        Public Members

        <a id="_CPPv4N22bk_avrcp_ct_cb_param_t30avrcp_ct_get_rn_caps_rsp_param9cap_countE"></a>

        <a id="_CPPv3N22bk_avrcp_ct_cb_param_t30avrcp_ct_get_rn_caps_rsp_param9cap_countE"></a> <a id="_CPPv2N22bk_avrcp_ct_cb_param_t30avrcp_ct_get_rn_caps_rsp_param9cap_countE"></a> <a id="bk_avrcp_ct_cb_param_t::avrcp_ct_get_rn_caps_rsp_param::cap_count__uint8_t"></a> <a id="structbk__avrcp__ct__cb__param__t_1_1avrcp__ct__get__rn__caps__rsp__param_1a6d84914e2210ab596344beaf041eecf5"></a> uint8\_t cap\_count
        :   number of items provided in event or company\_id according to cap\_id used

        <a id="_CPPv4N22bk_avrcp_ct_cb_param_t30avrcp_ct_get_rn_caps_rsp_param7evt_setE"></a>

        <a id="_CPPv3N22bk_avrcp_ct_cb_param_t30avrcp_ct_get_rn_caps_rsp_param7evt_setE"></a> <a id="_CPPv2N22bk_avrcp_ct_cb_param_t30avrcp_ct_get_rn_caps_rsp_param7evt_setE"></a> <a id="bk_avrcp_ct_cb_param_t::avrcp_ct_get_rn_caps_rsp_param::evt_set__bk_avrcp_rn_evt_cap_mask_t"></a> <a id="structbk__avrcp__ct__cb__param__t_1_1avrcp__ct__get__rn__caps__rsp__param_1a89f8787a21020c51a64e47940924404d"></a> [bk\_avrcp\_rn\_evt\_cap\_mask\_t](#_CPPv426bk_avrcp_rn_evt_cap_mask_t "bk_avrcp_rn_evt_cap_mask_t") evt\_set
        :   supported event\_ids represented in bit-mask

<a id="_CPPv422bk_avrcp_tg_cb_param_t"></a>

<a id="_CPPv322bk_avrcp_tg_cb_param_t"></a> <a id="_CPPv222bk_avrcp_tg_cb_param_t"></a> <a id="unionbk__avrcp__tg__cb__param__t"></a> union bk\_avrcp\_tg\_cb\_param\_t
:   *#include \<dm\_bt\_types.h\>*

    AVRC target callback parameters.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N22bk_avrcp_tg_cb_param_t9conn_statE"></a>

    <a id="_CPPv3N22bk_avrcp_tg_cb_param_t9conn_statE"></a> <a id="_CPPv2N22bk_avrcp_tg_cb_param_t9conn_statE"></a> <a id="bk_avrcp_tg_cb_param_t::conn_stat__bk_avrcp_tg_cb_param_t::avrcp_tg_conn_stat_param"></a> <a id="unionbk__avrcp__tg__cb__param__t_1aa5453a83cc8fc4d947f2f60146766152"></a> struct [bk\_avrcp\_tg\_cb\_param\_t](#_CPPv422bk_avrcp_tg_cb_param_t "bk_avrcp_tg_cb_param_t")::[avrcp\_tg\_conn\_stat\_param](#_CPPv4N22bk_avrcp_tg_cb_param_t24avrcp_tg_conn_stat_paramE "bk_avrcp_tg_cb_param_t::avrcp_tg_conn_stat_param") conn\_stat
    :   AVRC connection status

    <a id="_CPPv4N22bk_avrcp_tg_cb_param_t8psth_cmdE"></a>

    <a id="_CPPv3N22bk_avrcp_tg_cb_param_t8psth_cmdE"></a> <a id="_CPPv2N22bk_avrcp_tg_cb_param_t8psth_cmdE"></a> <a id="bk_avrcp_tg_cb_param_t::psth_cmd__bk_avrcp_tg_cb_param_t::avrcp_tg_psth_cmd_param"></a> <a id="unionbk__avrcp__tg__cb__param__t_1a45d755cd37cd20a002a4880498eec526"></a> struct [bk\_avrcp\_tg\_cb\_param\_t](#_CPPv422bk_avrcp_tg_cb_param_t "bk_avrcp_tg_cb_param_t")::[avrcp\_tg\_psth\_cmd\_param](#_CPPv4N22bk_avrcp_tg_cb_param_t23avrcp_tg_psth_cmd_paramE "bk_avrcp_tg_cb_param_t::avrcp_tg_psth_cmd_param") psth\_cmd
    :   passthrough command

    <a id="_CPPv4N22bk_avrcp_tg_cb_param_t11set_abs_volE"></a>

    <a id="_CPPv3N22bk_avrcp_tg_cb_param_t11set_abs_volE"></a> <a id="_CPPv2N22bk_avrcp_tg_cb_param_t11set_abs_volE"></a> <a id="bk_avrcp_tg_cb_param_t::set_abs_vol__bk_avrcp_tg_cb_param_t::avrcp_tg_set_abs_vol_param"></a> <a id="unionbk__avrcp__tg__cb__param__t_1a43700eb18454e3f04c25d7ab2b9e7cfa"></a> struct [bk\_avrcp\_tg\_cb\_param\_t](#_CPPv422bk_avrcp_tg_cb_param_t "bk_avrcp_tg_cb_param_t")::[avrcp\_tg\_set\_abs\_vol\_param](#_CPPv4N22bk_avrcp_tg_cb_param_t26avrcp_tg_set_abs_vol_paramE "bk_avrcp_tg_cb_param_t::avrcp_tg_set_abs_vol_param") set\_abs\_vol
    :   set absolute volume command targeted on audio sink

    <a id="_CPPv4N22bk_avrcp_tg_cb_param_t7reg_ntfE"></a>

    <a id="_CPPv3N22bk_avrcp_tg_cb_param_t7reg_ntfE"></a> <a id="_CPPv2N22bk_avrcp_tg_cb_param_t7reg_ntfE"></a> <a id="bk_avrcp_tg_cb_param_t::reg_ntf__bk_avrcp_tg_cb_param_t::avrcp_tg_reg_ntf_param"></a> <a id="unionbk__avrcp__tg__cb__param__t_1a72caf15abf2a8589dc94cf15b3acefe5"></a> struct [bk\_avrcp\_tg\_cb\_param\_t](#_CPPv422bk_avrcp_tg_cb_param_t "bk_avrcp_tg_cb_param_t")::[avrcp\_tg\_reg\_ntf\_param](#_CPPv4N22bk_avrcp_tg_cb_param_t22avrcp_tg_reg_ntf_paramE "bk_avrcp_tg_cb_param_t::avrcp_tg_reg_ntf_param") reg\_ntf
    :   register notification

    <a id="_CPPv4N22bk_avrcp_tg_cb_param_t24avrcp_tg_conn_stat_paramE"></a>

    <a id="_CPPv3N22bk_avrcp_tg_cb_param_t24avrcp_tg_conn_stat_paramE"></a> <a id="_CPPv2N22bk_avrcp_tg_cb_param_t24avrcp_tg_conn_stat_paramE"></a> <a id="bk_avrcp_tg_cb_param_t::avrcp_tg_conn_stat_param"></a> <a id="structbk__avrcp__tg__cb__param__t_1_1avrcp__tg__conn__stat__param"></a> struct avrcp\_tg\_conn\_stat\_param
    :   *#include \<dm\_bt\_types.h\>*

        BK\_AVRCP\_TG\_CONNECTION\_STATE\_EVT.

        <a id="breathe-section-title-public-members"></a>

        Public Members

        <a id="_CPPv4N22bk_avrcp_tg_cb_param_t24avrcp_tg_conn_stat_param9connectedE"></a>

        <a id="_CPPv3N22bk_avrcp_tg_cb_param_t24avrcp_tg_conn_stat_param9connectedE"></a> <a id="_CPPv2N22bk_avrcp_tg_cb_param_t24avrcp_tg_conn_stat_param9connectedE"></a> <a id="bk_avrcp_tg_cb_param_t::avrcp_tg_conn_stat_param::connected__b"></a> <a id="structbk__avrcp__tg__cb__param__t_1_1avrcp__tg__conn__stat__param_1ac84d5807f7b1ba792c87556b5370507d"></a> bool connected
        :   whether AVRC connection is set up

        <a id="_CPPv4N22bk_avrcp_tg_cb_param_t24avrcp_tg_conn_stat_param10remote_bdaE"></a>

        <a id="_CPPv3N22bk_avrcp_tg_cb_param_t24avrcp_tg_conn_stat_param10remote_bdaE"></a> <a id="_CPPv2N22bk_avrcp_tg_cb_param_t24avrcp_tg_conn_stat_param10remote_bdaE"></a> <a id="bk_avrcp_tg_cb_param_t::avrcp_tg_conn_stat_param::remote_bda__uint8_tA"></a> <a id="structbk__avrcp__tg__cb__param__t_1_1avrcp__tg__conn__stat__param_1acef3a6e6f8fc22a3dd3b88b845ee01a0"></a> uint8\_t remote\_bda\[6\]
        :   remote bluetooth device address

    <a id="_CPPv4N22bk_avrcp_tg_cb_param_t23avrcp_tg_psth_cmd_paramE"></a>

    <a id="_CPPv3N22bk_avrcp_tg_cb_param_t23avrcp_tg_psth_cmd_paramE"></a> <a id="_CPPv2N22bk_avrcp_tg_cb_param_t23avrcp_tg_psth_cmd_paramE"></a> <a id="bk_avrcp_tg_cb_param_t::avrcp_tg_psth_cmd_param"></a> <a id="structbk__avrcp__tg__cb__param__t_1_1avrcp__tg__psth__cmd__param"></a> struct avrcp\_tg\_psth\_cmd\_param
    :   *#include \<dm\_bt\_types.h\>*

        BK\_AVRCP\_TG\_PASSTHROUGH\_CMD\_EVT.

        <a id="breathe-section-title-public-members"></a>

        Public Members

        <a id="_CPPv4N22bk_avrcp_tg_cb_param_t23avrcp_tg_psth_cmd_param8key_codeE"></a>

        <a id="_CPPv3N22bk_avrcp_tg_cb_param_t23avrcp_tg_psth_cmd_param8key_codeE"></a> <a id="_CPPv2N22bk_avrcp_tg_cb_param_t23avrcp_tg_psth_cmd_param8key_codeE"></a> <a id="bk_avrcp_tg_cb_param_t::avrcp_tg_psth_cmd_param::key_code__uint8_t"></a> <a id="structbk__avrcp__tg__cb__param__t_1_1avrcp__tg__psth__cmd__param_1a387319421a90bf98eea484594c490e54"></a> uint8\_t key\_code
        :   passthrough command code

        <a id="_CPPv4N22bk_avrcp_tg_cb_param_t23avrcp_tg_psth_cmd_param9key_stateE"></a>

        <a id="_CPPv3N22bk_avrcp_tg_cb_param_t23avrcp_tg_psth_cmd_param9key_stateE"></a> <a id="_CPPv2N22bk_avrcp_tg_cb_param_t23avrcp_tg_psth_cmd_param9key_stateE"></a> <a id="bk_avrcp_tg_cb_param_t::avrcp_tg_psth_cmd_param::key_state__uint8_t"></a> <a id="structbk__avrcp__tg__cb__param__t_1_1avrcp__tg__psth__cmd__param_1acfab04bc1065dc93ec9f4d33752731b8"></a> uint8\_t key\_state
        :   0 for PRESSED, 1 for RELEASED

    <a id="_CPPv4N22bk_avrcp_tg_cb_param_t22avrcp_tg_reg_ntf_paramE"></a>

    <a id="_CPPv3N22bk_avrcp_tg_cb_param_t22avrcp_tg_reg_ntf_paramE"></a> <a id="_CPPv2N22bk_avrcp_tg_cb_param_t22avrcp_tg_reg_ntf_paramE"></a> <a id="bk_avrcp_tg_cb_param_t::avrcp_tg_reg_ntf_param"></a> <a id="structbk__avrcp__tg__cb__param__t_1_1avrcp__tg__reg__ntf__param"></a> struct avrcp\_tg\_reg\_ntf\_param
    :   *#include \<dm\_bt\_types.h\>*

        BK\_AVRCP\_TG\_REGISTER\_NOTIFICATION\_EVT.

        <a id="breathe-section-title-public-members"></a>

        Public Members

        <a id="_CPPv4N22bk_avrcp_tg_cb_param_t22avrcp_tg_reg_ntf_param8event_idE"></a>

        <a id="_CPPv3N22bk_avrcp_tg_cb_param_t22avrcp_tg_reg_ntf_param8event_idE"></a> <a id="_CPPv2N22bk_avrcp_tg_cb_param_t22avrcp_tg_reg_ntf_param8event_idE"></a> <a id="bk_avrcp_tg_cb_param_t::avrcp_tg_reg_ntf_param::event_id__uint8_t"></a> <a id="structbk__avrcp__tg__cb__param__t_1_1avrcp__tg__reg__ntf__param_1af9cd66a648f1f24fde04bf838a4eebcf"></a> uint8\_t event\_id
        :   event id of bk\_avrcp\_rn\_event\_ids\_t

        <a id="_CPPv4N22bk_avrcp_tg_cb_param_t22avrcp_tg_reg_ntf_param15event_parameterE"></a>

        <a id="_CPPv3N22bk_avrcp_tg_cb_param_t22avrcp_tg_reg_ntf_param15event_parameterE"></a> <a id="_CPPv2N22bk_avrcp_tg_cb_param_t22avrcp_tg_reg_ntf_param15event_parameterE"></a> <a id="bk_avrcp_tg_cb_param_t::avrcp_tg_reg_ntf_param::event_parameter__uint32_t"></a> <a id="structbk__avrcp__tg__cb__param__t_1_1avrcp__tg__reg__ntf__param_1a6a33d7382147277e732e92b26f14fa68"></a> uint32\_t event\_parameter
        :   event notification parameter, used with BK\_AVRCP\_RN\_PLAY\_POS\_CHANGED only now

    <a id="_CPPv4N22bk_avrcp_tg_cb_param_t26avrcp_tg_set_abs_vol_paramE"></a>

    <a id="_CPPv3N22bk_avrcp_tg_cb_param_t26avrcp_tg_set_abs_vol_paramE"></a> <a id="_CPPv2N22bk_avrcp_tg_cb_param_t26avrcp_tg_set_abs_vol_paramE"></a> <a id="bk_avrcp_tg_cb_param_t::avrcp_tg_set_abs_vol_param"></a> <a id="structbk__avrcp__tg__cb__param__t_1_1avrcp__tg__set__abs__vol__param"></a> struct avrcp\_tg\_set\_abs\_vol\_param
    :   *#include \<dm\_bt\_types.h\>*

        BK\_AVRCP\_TG\_SET\_ABSOLUTE\_VOLUME\_CMD\_EVT.

        <a id="breathe-section-title-public-members"></a>

        Public Members

        <a id="_CPPv4N22bk_avrcp_tg_cb_param_t26avrcp_tg_set_abs_vol_param6volumeE"></a>

        <a id="_CPPv3N22bk_avrcp_tg_cb_param_t26avrcp_tg_set_abs_vol_param6volumeE"></a> <a id="_CPPv2N22bk_avrcp_tg_cb_param_t26avrcp_tg_set_abs_vol_param6volumeE"></a> <a id="bk_avrcp_tg_cb_param_t::avrcp_tg_set_abs_vol_param::volume__uint8_t"></a> <a id="structbk__avrcp__tg__cb__param__t_1_1avrcp__tg__set__abs__vol__param_1a1a9133b3ba615d4c3d5f0abdace3414b"></a> uint8\_t volume
        :   volume ranges from 0 to 127

<a id="structures"></a>

### Structures

<a id="_CPPv413bk_a2dp_mcc_t"></a>

<a id="_CPPv313bk_a2dp_mcc_t"></a> <a id="_CPPv213bk_a2dp_mcc_t"></a> <a id="bk_a2dp_mcc_t"></a> <a id="structbk__a2dp__mcc__t"></a> struct bk\_a2dp\_mcc\_t
:   A2DP media codec capabilities union.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N13bk_a2dp_mcc_t4typeE"></a>

    <a id="_CPPv3N13bk_a2dp_mcc_t4typeE"></a> <a id="_CPPv2N13bk_a2dp_mcc_t4typeE"></a> <a id="bk_a2dp_mcc_t::type__uint8_t"></a> <a id="structbk__a2dp__mcc__t_1a9406441c4b52916460ad405d08591466"></a> uint8\_t type
    :   A2DP media codec type

    <a id="_CPPv4N13bk_a2dp_mcc_t9sbc_codecE"></a>

    <a id="_CPPv3N13bk_a2dp_mcc_t9sbc_codecE"></a> <a id="_CPPv2N13bk_a2dp_mcc_t9sbc_codecE"></a> <a id="structbk__a2dp__mcc__t_1a83788749c841daba906717c5bac65547"></a> struct [bk\_a2dp\_mcc\_t](#_CPPv413bk_a2dp_mcc_t "bk_a2dp_mcc_t")::\[anonymous\]::\[anonymous\] sbc\_codec
    :   SBC codec capabilities.

    <a id="_CPPv4N13bk_a2dp_mcc_t9aac_codecE"></a>

    <a id="_CPPv3N13bk_a2dp_mcc_t9aac_codecE"></a> <a id="_CPPv2N13bk_a2dp_mcc_t9aac_codecE"></a> <a id="structbk__a2dp__mcc__t_1af91e53de3f120b9ee7da187a0fd1614e"></a> struct [bk\_a2dp\_mcc\_t](#_CPPv413bk_a2dp_mcc_t "bk_a2dp_mcc_t")::\[anonymous\]::\[anonymous\] aac\_codec
    :   MPEG-2, 4 AAC codec capabilities.

    <a id="_CPPv4N13bk_a2dp_mcc_t3cieE"></a>

    <a id="_CPPv3N13bk_a2dp_mcc_t3cieE"></a> <a id="_CPPv2N13bk_a2dp_mcc_t3cieE"></a> <a id="structbk__a2dp__mcc__t_1a3cc8ec043b21b8b467e0c1cf5098af6c"></a> union [bk\_a2dp\_mcc\_t](#_CPPv413bk_a2dp_mcc_t "bk_a2dp_mcc_t")::\[anonymous\] cie
    :   A2DP codec information element

<a id="_CPPv420bk_bt_gap_dev_prop_t"></a>

<a id="_CPPv320bk_bt_gap_dev_prop_t"></a> <a id="_CPPv220bk_bt_gap_dev_prop_t"></a> <a id="bk_bt_gap_dev_prop_t"></a> <a id="structbk__bt__gap__dev__prop__t"></a> struct bk\_bt\_gap\_dev\_prop\_t
:   Bluetooth Device Property Descriptor.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N20bk_bt_gap_dev_prop_t4typeE"></a>

    <a id="_CPPv3N20bk_bt_gap_dev_prop_t4typeE"></a> <a id="_CPPv2N20bk_bt_gap_dev_prop_t4typeE"></a> <a id="bk_bt_gap_dev_prop_t::type__bk_bt_gap_dev_prop_type_t"></a> <a id="structbk__bt__gap__dev__prop__t_1adc72458129c42384e54f9bce641e43ad"></a> [bk\_bt\_gap\_dev\_prop\_type\_t](#_CPPv425bk_bt_gap_dev_prop_type_t "bk_bt_gap_dev_prop_type_t") type
    :   Device property type

    <a id="_CPPv4N20bk_bt_gap_dev_prop_t3lenE"></a>

    <a id="_CPPv3N20bk_bt_gap_dev_prop_t3lenE"></a> <a id="_CPPv2N20bk_bt_gap_dev_prop_t3lenE"></a> <a id="bk_bt_gap_dev_prop_t::len__i"></a> <a id="structbk__bt__gap__dev__prop__t_1a4f43534037f62e6189e62cfc82cf698f"></a> int len
    :   Device property value length

    <a id="_CPPv4N20bk_bt_gap_dev_prop_t3valE"></a>

    <a id="_CPPv3N20bk_bt_gap_dev_prop_t3valE"></a> <a id="_CPPv2N20bk_bt_gap_dev_prop_t3valE"></a> <a id="bk_bt_gap_dev_prop_t::val__voidP"></a> <a id="structbk__bt__gap__dev__prop__t_1ae8e405f45c7eaa46469fed9c3539253e"></a> void \*val
    :   Device property value

<a id="_CPPv423bk_bt_linkkey_storage_t"></a>

<a id="_CPPv323bk_bt_linkkey_storage_t"></a> <a id="_CPPv223bk_bt_linkkey_storage_t"></a> <a id="bk_bt_linkkey_storage_t"></a> <a id="structbk__bt__linkkey__storage__t"></a> struct bk\_bt\_linkkey\_storage\_t
:   bt link key storage

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N23bk_bt_linkkey_storage_t4sizeE"></a>

    <a id="_CPPv3N23bk_bt_linkkey_storage_t4sizeE"></a> <a id="_CPPv2N23bk_bt_linkkey_storage_t4sizeE"></a> <a id="bk_bt_linkkey_storage_t::size__uint16_t"></a> <a id="structbk__bt__linkkey__storage__t_1a4542bd9ea086a1b8744fe133cce57cce"></a> uint16\_t size
    :   this struct size

    <a id="_CPPv4N23bk_bt_linkkey_storage_t4addrE"></a>

    <a id="_CPPv3N23bk_bt_linkkey_storage_t4addrE"></a> <a id="_CPPv2N23bk_bt_linkkey_storage_t4addrE"></a> <a id="bk_bt_linkkey_storage_t::addr__uint8_tA"></a> <a id="structbk__bt__linkkey__storage__t_1a39b79bd1ac279579e1304c43e302541c"></a> uint8\_t addr\[6\]
    :   bt addr

    <a id="_CPPv4N23bk_bt_linkkey_storage_t8link_keyE"></a>

    <a id="_CPPv3N23bk_bt_linkkey_storage_t8link_keyE"></a> <a id="_CPPv2N23bk_bt_linkkey_storage_t8link_keyE"></a> <a id="bk_bt_linkkey_storage_t::link_key__uint8_tA"></a> <a id="structbk__bt__linkkey__storage__t_1a266975b9b33f91f055463023c1dd9c5d"></a> uint8\_t link\_key\[16\]
    :   bt link key

<a id="_CPPv426bk_avrcp_rn_evt_cap_mask_t"></a>

<a id="_CPPv326bk_avrcp_rn_evt_cap_mask_t"></a> <a id="_CPPv226bk_avrcp_rn_evt_cap_mask_t"></a> <a id="bk_avrcp_rn_evt_cap_mask_t"></a> <a id="structbk__avrcp__rn__evt__cap__mask__t"></a> struct bk\_avrcp\_rn\_evt\_cap\_mask\_t
:   AVRCP target notification event capability bit mask.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N26bk_avrcp_rn_evt_cap_mask_t4bitsE"></a>

    <a id="_CPPv3N26bk_avrcp_rn_evt_cap_mask_t4bitsE"></a> <a id="_CPPv2N26bk_avrcp_rn_evt_cap_mask_t4bitsE"></a> <a id="bk_avrcp_rn_evt_cap_mask_t::bits__uint16_t"></a> <a id="structbk__avrcp__rn__evt__cap__mask__t_1a46db406a60787f02436984c9224487e4"></a> uint16\_t bits
    :   bit mask representation of supported event\_ids

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv424bk_a2dp_source_data_cb_t"></a>

<a id="_CPPv324bk_a2dp_source_data_cb_t"></a> <a id="_CPPv224bk_a2dp_source_data_cb_t"></a> <a id="bk_a2dp_source_data_cb_t"></a> <a id="dm__bt__types_8h_1a92c15470f898f899b0bd00fb513ad1ca"></a> typedef int32\_t (\*bk\_a2dp\_source\_data\_cb\_t)(uint8\_t \*buf, int32\_t len)
:   A2DP source data read callback function.

    Param buf
    :   **\[in\]** : buffer to be filled with PCM data stream from higher layer

    Param len
    :   **\[in\]** : size(in bytes) of data block to be copied to buf. -1 is an indication to user that data buffer shall be flushed

    Return
    :   size of bytes read successfully, if the argument len is -1, this value is ignored.

<a id="_CPPv415bk_bt_a2dp_cb_t"></a>

<a id="_CPPv315bk_bt_a2dp_cb_t"></a> <a id="_CPPv215bk_bt_a2dp_cb_t"></a> <a id="bk_bt_a2dp_cb_t"></a> <a id="dm__bt__types_8h_1a85cc16b7d95afe687543b8975858a0a4"></a> typedef void (\*bk\_bt\_a2dp\_cb\_t)([bk\_a2dp\_cb\_event\_t](#_CPPv418bk_a2dp_cb_event_t "bk_a2dp_cb_event_t") event, [bk\_a2dp\_cb\_param\_t](#_CPPv418bk_a2dp_cb_param_t "bk_a2dp_cb_param_t") \*param)
:   A2DP profile callback function type.

    Param event
    :   : Event type

    Param param
    :   : Pointer to callback parameter

<a id="_CPPv420bk_bt_sink_data_cb_t"></a>

<a id="_CPPv320bk_bt_sink_data_cb_t"></a> <a id="_CPPv220bk_bt_sink_data_cb_t"></a> <a id="bk_bt_sink_data_cb_t"></a> <a id="dm__bt__types_8h_1a9c2f236503e71453bac690930291cb45"></a> typedef void (\*bk\_bt\_sink\_data\_cb\_t)(const uint8\_t \*buf, uint16\_t len)
:   A2DP sink data callback function.

    Param buf
    :   **\[in\]** : pointer to the data received from A2DP source device

    Param len
    :   **\[in\]** : size(in bytes) in buf

<a id="_CPPv416bk_avrcp_ct_cb_t"></a>

<a id="_CPPv316bk_avrcp_ct_cb_t"></a> <a id="_CPPv216bk_avrcp_ct_cb_t"></a> <a id="bk_avrcp_ct_cb_t"></a> <a id="dm__bt__types_8h_1a4b4e398990f29e83bb5d49ca2d385475"></a> typedef void (\*bk\_avrcp\_ct\_cb\_t)([bk\_avrcp\_ct\_cb\_event\_t](#_CPPv422bk_avrcp_ct_cb_event_t "bk_avrcp_ct_cb_event_t") event, [bk\_avrcp\_ct\_cb\_param\_t](#_CPPv422bk_avrcp_ct_cb_param_t "bk_avrcp_ct_cb_param_t") \*param)
:   AVRCP controller callback function type.

    Param event
    :   : Event type

    Param param
    :   : Pointer to callback parameter union

<a id="_CPPv416bk_avrcp_tg_cb_t"></a>

<a id="_CPPv316bk_avrcp_tg_cb_t"></a> <a id="_CPPv216bk_avrcp_tg_cb_t"></a> <a id="bk_avrcp_tg_cb_t"></a> <a id="dm__bt__types_8h_1acbed5d4f2b3eccf63f928843c08c4db3"></a> typedef void (\*bk\_avrcp\_tg\_cb\_t)([bk\_avrcp\_tg\_cb\_event\_t](#_CPPv422bk_avrcp_tg_cb_event_t "bk_avrcp_tg_cb_event_t") event, [bk\_avrcp\_tg\_cb\_param\_t](#_CPPv422bk_avrcp_tg_cb_param_t "bk_avrcp_tg_cb_param_t") \*param)
:   AVRCP target callback function type.

    Param event
    :   : Event type

    Param param
    :   : Pointer to callback parameter union

<a id="_CPPv413bt_event_cb_t"></a>

<a id="_CPPv313bt_event_cb_t"></a> <a id="_CPPv213bt_event_cb_t"></a> <a id="bt_event_cb_t"></a> <a id="dm__bt__types_8h_1a03af9490ac8050aea0fb19a9eef39c00"></a> typedef uint32\_t (\*bt\_event\_cb\_t)([bt\_event\_enum\_t](#_CPPv415bt_event_enum_t "bt_event_enum_t") event, void \*param)
:   for async dm\_bt api event.

    bt event report.

    Param event, :
    :   event id. see bt\_event\_enum\_t

        - param: param

<a id="_CPPv424bt_spp_event_notify_cb_t"></a>

<a id="_CPPv324bt_spp_event_notify_cb_t"></a> <a id="_CPPv224bt_spp_event_notify_cb_t"></a> <a id="bt_spp_event_notify_cb_t"></a> <a id="dm__bt__types_8h_1a0c272582293c9ab2df0c56a3f5786ba4"></a> typedef uint16\_t (\*bt\_spp\_event\_notify\_cb\_t)(uint32\_t spp\_handle, uint8\_t spp\_event, uint16\_t status, void \*data, uint16\_t data\_length)
:   Application should register a callback through the API bk\_bt\_spp\_init.

    Param spp\_handle, :
    :   **\[in\]** Handle associates a SPP connection to a remote SPP device.

    Param spp\_event, :
    :   **\[in\]** Event indicated to application by bk\_spp\_cb\_event\_t.

    Param status, :
    :   **\[in\]** The status of the event.

    Param data, :
    :   **\[in\]** Pointer to the array containing the parameters associated with the event.

    Param data\_length, :
    :   **\[in\]** Length of the parameters associated with the event.

    Return
    :   0x00.

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv417bk_bt_conn_mode_t"></a>

<a id="_CPPv317bk_bt_conn_mode_t"></a> <a id="_CPPv217bk_bt_conn_mode_t"></a> <a id="dm__bt__types_8h_1a3fa3a6a98d6cf16673943c4f9f926e5a"></a> enum bk\_bt\_conn\_mode\_t
:   Discoverability and Connectability mode.

    *Values:*

    <a id="_CPPv4N17bk_bt_conn_mode_t21BK_BT_NON_CONNECTABLEE"></a>

    <a id="_CPPv3N17bk_bt_conn_mode_t21BK_BT_NON_CONNECTABLEE"></a> <a id="_CPPv2N17bk_bt_conn_mode_t21BK_BT_NON_CONNECTABLEE"></a> <a id="dm__bt__types_8h_1a3fa3a6a98d6cf16673943c4f9f926e5aadd0ef00016a0a0166e304055d8d4e4c5"></a> enumerator BK\_BT\_NON\_CONNECTABLE
    :   Non-connectable

    <a id="_CPPv4N17bk_bt_conn_mode_t17BK_BT_CONNECTABLEE"></a>

    <a id="_CPPv3N17bk_bt_conn_mode_t17BK_BT_CONNECTABLEE"></a> <a id="_CPPv2N17bk_bt_conn_mode_t17BK_BT_CONNECTABLEE"></a> <a id="dm__bt__types_8h_1a3fa3a6a98d6cf16673943c4f9f926e5aa31ec1ce972adfbf94bc4b1334dbccc8e"></a> enumerator BK\_BT\_CONNECTABLE
    :   Connectable

<a id="_CPPv417bk_bt_disc_mode_t"></a>

<a id="_CPPv317bk_bt_disc_mode_t"></a> <a id="_CPPv217bk_bt_disc_mode_t"></a> <a id="dm__bt__types_8h_1ac04c470895faddd677e699715a2b56d1"></a> enum bk\_bt\_disc\_mode\_t
:   *Values:*

    <a id="_CPPv4N17bk_bt_disc_mode_t22BK_BT_NON_DISCOVERABLEE"></a>

    <a id="_CPPv3N17bk_bt_disc_mode_t22BK_BT_NON_DISCOVERABLEE"></a> <a id="_CPPv2N17bk_bt_disc_mode_t22BK_BT_NON_DISCOVERABLEE"></a> <a id="dm__bt__types_8h_1ac04c470895faddd677e699715a2b56d1a977a2b191c5036b8fd034d84507bb991"></a> enumerator BK\_BT\_NON\_DISCOVERABLE
    :   Non-discoverable

    <a id="_CPPv4N17bk_bt_disc_mode_t18BK_BT_DISCOVERABLEE"></a>

    <a id="_CPPv3N17bk_bt_disc_mode_t18BK_BT_DISCOVERABLEE"></a> <a id="_CPPv2N17bk_bt_disc_mode_t18BK_BT_DISCOVERABLEE"></a> <a id="dm__bt__types_8h_1ac04c470895faddd677e699715a2b56d1ac7ad891c3fb9aaa3d528b77efce3d1ba"></a> enumerator BK\_BT\_DISCOVERABLE
    :   Discoverable

<a id="_CPPv412common_cod_t"></a>

<a id="_CPPv312common_cod_t"></a> <a id="_CPPv212common_cod_t"></a> <a id="dm__bt__types_8h_1ab4918e797f42831f18f1437a61bc99cf"></a> enum common\_cod\_t
:   *Values:*

    <a id="_CPPv4N12common_cod_t9COD_PHONEE"></a>

    <a id="_CPPv3N12common_cod_t9COD_PHONEE"></a> <a id="_CPPv2N12common_cod_t9COD_PHONEE"></a> <a id="dm__bt__types_8h_1ab4918e797f42831f18f1437a61bc99cfae78d990e53a650fccbd6a25af9c262b2"></a> enumerator COD\_PHONE

    <a id="_CPPv4N12common_cod_t12COD_SOUNDBARE"></a>

    <a id="_CPPv3N12common_cod_t12COD_SOUNDBARE"></a> <a id="_CPPv2N12common_cod_t12COD_SOUNDBARE"></a> <a id="dm__bt__types_8h_1ab4918e797f42831f18f1437a61bc99cfa35f5fdf7c8b5e9b521d2f2ea2fc4f0fd"></a> enumerator COD\_SOUNDBAR

    <a id="_CPPv4N12common_cod_t11COD_HEADSETE"></a>

    <a id="_CPPv3N12common_cod_t11COD_HEADSETE"></a> <a id="_CPPv2N12common_cod_t11COD_HEADSETE"></a> <a id="dm__bt__types_8h_1ab4918e797f42831f18f1437a61bc99cfa11312a7611013bbeee6f6eb49075eedc"></a> enumerator COD\_HEADSET

<a id="_CPPv416bk_bt_inq_mode_t"></a>

<a id="_CPPv316bk_bt_inq_mode_t"></a> <a id="_CPPv216bk_bt_inq_mode_t"></a> <a id="dm__bt__types_8h_1a2e7658e3d81463f492ad78aa98c88a9c"></a> enum bk\_bt\_inq\_mode\_t
:   Inquiry Mode

    *Values:*

    <a id="_CPPv4N16bk_bt_inq_mode_t30BK_BT_INQ_MODE_GENERAL_INQUIRYE"></a>

    <a id="_CPPv3N16bk_bt_inq_mode_t30BK_BT_INQ_MODE_GENERAL_INQUIRYE"></a> <a id="_CPPv2N16bk_bt_inq_mode_t30BK_BT_INQ_MODE_GENERAL_INQUIRYE"></a> <a id="dm__bt__types_8h_1a2e7658e3d81463f492ad78aa98c88a9cad2e2f0eb73a57ae43836c867bd6e43aa"></a> enumerator BK\_BT\_INQ\_MODE\_GENERAL\_INQUIRY
    :   General inquiry mode

<a id="_CPPv418bk_a2dp_cb_event_t"></a>

<a id="_CPPv318bk_a2dp_cb_event_t"></a> <a id="_CPPv218bk_a2dp_cb_event_t"></a> <a id="dm__bt__types_8h_1aad6d91713de35db7ded8c9ae80d6ece5"></a> enum bk\_a2dp\_cb\_event\_t
:   A2DP callback events.

    *Values:*

    <a id="_CPPv4N18bk_a2dp_cb_event_t28BK_A2DP_CONNECTION_STATE_EVTE"></a>

    <a id="_CPPv3N18bk_a2dp_cb_event_t28BK_A2DP_CONNECTION_STATE_EVTE"></a> <a id="_CPPv2N18bk_a2dp_cb_event_t28BK_A2DP_CONNECTION_STATE_EVTE"></a> <a id="dm__bt__types_8h_1aad6d91713de35db7ded8c9ae80d6ece5a7a1d3d85c10a4f9d30dfd041c75bcfb6"></a> enumerator BK\_A2DP\_CONNECTION\_STATE\_EVT
    :   connection state changed event

    <a id="_CPPv4N18bk_a2dp_cb_event_t23BK_A2DP_AUDIO_STATE_EVTE"></a>

    <a id="_CPPv3N18bk_a2dp_cb_event_t23BK_A2DP_AUDIO_STATE_EVTE"></a> <a id="_CPPv2N18bk_a2dp_cb_event_t23BK_A2DP_AUDIO_STATE_EVTE"></a> <a id="dm__bt__types_8h_1aad6d91713de35db7ded8c9ae80d6ece5af6523df086d14460fba99ab956af78e1"></a> enumerator BK\_A2DP\_AUDIO\_STATE\_EVT
    :   audio stream transmission state changed event

    <a id="_CPPv4N18bk_a2dp_cb_event_t21BK_A2DP_AUDIO_CFG_EVTE"></a>

    <a id="_CPPv3N18bk_a2dp_cb_event_t21BK_A2DP_AUDIO_CFG_EVTE"></a> <a id="_CPPv2N18bk_a2dp_cb_event_t21BK_A2DP_AUDIO_CFG_EVTE"></a> <a id="dm__bt__types_8h_1aad6d91713de35db7ded8c9ae80d6ece5adc22beb367229db519c745378fb54620"></a> enumerator BK\_A2DP\_AUDIO\_CFG\_EVT
    :   audio codec is configured, only used for A2DP SINK

    <a id="_CPPv4N18bk_a2dp_cb_event_t28BK_A2DP_AUDIO_SOURCE_CFG_EVTE"></a>

    <a id="_CPPv3N18bk_a2dp_cb_event_t28BK_A2DP_AUDIO_SOURCE_CFG_EVTE"></a> <a id="_CPPv2N18bk_a2dp_cb_event_t28BK_A2DP_AUDIO_SOURCE_CFG_EVTE"></a> <a id="dm__bt__types_8h_1aad6d91713de35db7ded8c9ae80d6ece5ae02351051f042929063dab02f5927495"></a> enumerator BK\_A2DP\_AUDIO\_SOURCE\_CFG\_EVT
    :   audio codec is configured, only used for A2DP SOURCE

<a id="_CPPv426bk_a2dp_connection_state_t"></a>

<a id="_CPPv326bk_a2dp_connection_state_t"></a> <a id="_CPPv226bk_a2dp_connection_state_t"></a> <a id="dm__bt__types_8h_1a07aa05dfec96703c88d5b46f90c85e02"></a> enum bk\_a2dp\_connection\_state\_t
:   Bluetooth A2DP connection states.

    *Values:*

    <a id="_CPPv4N26bk_a2dp_connection_state_t37BK_A2DP_CONNECTION_STATE_DISCONNECTEDE"></a>

    <a id="_CPPv3N26bk_a2dp_connection_state_t37BK_A2DP_CONNECTION_STATE_DISCONNECTEDE"></a> <a id="_CPPv2N26bk_a2dp_connection_state_t37BK_A2DP_CONNECTION_STATE_DISCONNECTEDE"></a> <a id="dm__bt__types_8h_1a07aa05dfec96703c88d5b46f90c85e02a0f84e234849ba7263315fb0ad354863e"></a> enumerator BK\_A2DP\_CONNECTION\_STATE\_DISCONNECTED
    :   connection released

    <a id="_CPPv4N26bk_a2dp_connection_state_t35BK_A2DP_CONNECTION_STATE_CONNECTINGE"></a>

    <a id="_CPPv3N26bk_a2dp_connection_state_t35BK_A2DP_CONNECTION_STATE_CONNECTINGE"></a> <a id="_CPPv2N26bk_a2dp_connection_state_t35BK_A2DP_CONNECTION_STATE_CONNECTINGE"></a> <a id="dm__bt__types_8h_1a07aa05dfec96703c88d5b46f90c85e02a3eb1763d554e2ff3cca384ef8ad3e394"></a> enumerator BK\_A2DP\_CONNECTION\_STATE\_CONNECTING
    :   connecting remote device

    <a id="_CPPv4N26bk_a2dp_connection_state_t34BK_A2DP_CONNECTION_STATE_CONNECTEDE"></a>

    <a id="_CPPv3N26bk_a2dp_connection_state_t34BK_A2DP_CONNECTION_STATE_CONNECTEDE"></a> <a id="_CPPv2N26bk_a2dp_connection_state_t34BK_A2DP_CONNECTION_STATE_CONNECTEDE"></a> <a id="dm__bt__types_8h_1a07aa05dfec96703c88d5b46f90c85e02a85653f02b0ba148acc4079adb870ea41"></a> enumerator BK\_A2DP\_CONNECTION\_STATE\_CONNECTED
    :   connection established

    <a id="_CPPv4N26bk_a2dp_connection_state_t38BK_A2DP_CONNECTION_STATE_DISCONNECTINGE"></a>

    <a id="_CPPv3N26bk_a2dp_connection_state_t38BK_A2DP_CONNECTION_STATE_DISCONNECTINGE"></a> <a id="_CPPv2N26bk_a2dp_connection_state_t38BK_A2DP_CONNECTION_STATE_DISCONNECTINGE"></a> <a id="dm__bt__types_8h_1a07aa05dfec96703c88d5b46f90c85e02a5c735cf637c42e198faca3974dfb04fd"></a> enumerator BK\_A2DP\_CONNECTION\_STATE\_DISCONNECTING
    :   disconnecting remote device

<a id="_CPPv418bk_a2dp_disc_rsn_t"></a>

<a id="_CPPv318bk_a2dp_disc_rsn_t"></a> <a id="_CPPv218bk_a2dp_disc_rsn_t"></a> <a id="dm__bt__types_8h_1a2b167fd4415b0e4ab99fad3586c06410"></a> enum bk\_a2dp\_disc\_rsn\_t
:   Bluetooth A2DP disconnection reason.

    *Values:*

    <a id="_CPPv4N18bk_a2dp_disc_rsn_t23BK_A2DP_DISC_RSN_NORMALE"></a>

    <a id="_CPPv3N18bk_a2dp_disc_rsn_t23BK_A2DP_DISC_RSN_NORMALE"></a> <a id="_CPPv2N18bk_a2dp_disc_rsn_t23BK_A2DP_DISC_RSN_NORMALE"></a> <a id="dm__bt__types_8h_1a2b167fd4415b0e4ab99fad3586c06410abeaca5cdf4537dca09f7d7a6bee703b7"></a> enumerator BK\_A2DP\_DISC\_RSN\_NORMAL
    :   Finished disconnection that is initiated by local or remote device

    <a id="_CPPv4N18bk_a2dp_disc_rsn_t25BK_A2DP_DISC_RSN_ABNORMALE"></a>

    <a id="_CPPv3N18bk_a2dp_disc_rsn_t25BK_A2DP_DISC_RSN_ABNORMALE"></a> <a id="_CPPv2N18bk_a2dp_disc_rsn_t25BK_A2DP_DISC_RSN_ABNORMALE"></a> <a id="dm__bt__types_8h_1a2b167fd4415b0e4ab99fad3586c06410a51cb601a97f5dd44da47cfd6c3cb10a0"></a> enumerator BK\_A2DP\_DISC\_RSN\_ABNORMAL
    :   Abnormal disconnection caused by signal loss

<a id="_CPPv421bk_a2dp_audio_state_t"></a>

<a id="_CPPv321bk_a2dp_audio_state_t"></a> <a id="_CPPv221bk_a2dp_audio_state_t"></a> <a id="dm__bt__types_8h_1a9b80ac80a02e3dfcd5c339fb6e84e9f8"></a> enum bk\_a2dp\_audio\_state\_t
:   Bluetooth A2DP datapath states.

    *Values:*

    <a id="_CPPv4N21bk_a2dp_audio_state_t27BK_A2DP_AUDIO_STATE_SUSPENDE"></a>

    <a id="_CPPv3N21bk_a2dp_audio_state_t27BK_A2DP_AUDIO_STATE_SUSPENDE"></a> <a id="_CPPv2N21bk_a2dp_audio_state_t27BK_A2DP_AUDIO_STATE_SUSPENDE"></a> <a id="dm__bt__types_8h_1a9b80ac80a02e3dfcd5c339fb6e84e9f8adb948f8e8c46906aeb09f8fc6b4d1fba"></a> enumerator BK\_A2DP\_AUDIO\_STATE\_SUSPEND
    :   audio stream datapath suspend

    <a id="_CPPv4N21bk_a2dp_audio_state_t27BK_A2DP_AUDIO_STATE_STARTEDE"></a>

    <a id="_CPPv3N21bk_a2dp_audio_state_t27BK_A2DP_AUDIO_STATE_STARTEDE"></a> <a id="_CPPv2N21bk_a2dp_audio_state_t27BK_A2DP_AUDIO_STATE_STARTEDE"></a> <a id="dm__bt__types_8h_1a9b80ac80a02e3dfcd5c339fb6e84e9f8ad92853a9eb4330bbd809c1d8538ede7d"></a> enumerator BK\_A2DP\_AUDIO\_STATE\_STARTED
    :   audio stream datapath started

<a id="_CPPv420bk_a2dp_media_ctrl_t"></a>

<a id="_CPPv320bk_a2dp_media_ctrl_t"></a> <a id="_CPPv220bk_a2dp_media_ctrl_t"></a> <a id="dm__bt__types_8h_1a026216b39590cf9e5ad2fa2fca7efba0"></a> enum bk\_a2dp\_media\_ctrl\_t
:   A2DP media control commands.

    *Values:*

    <a id="_CPPv4N20bk_a2dp_media_ctrl_t24BK_A2DP_MEDIA_CTRL_STARTE"></a>

    <a id="_CPPv3N20bk_a2dp_media_ctrl_t24BK_A2DP_MEDIA_CTRL_STARTE"></a> <a id="_CPPv2N20bk_a2dp_media_ctrl_t24BK_A2DP_MEDIA_CTRL_STARTE"></a> <a id="dm__bt__types_8h_1a026216b39590cf9e5ad2fa2fca7efba0aae8b47cb2a00913e68839b6625c2aacb"></a> enumerator BK\_A2DP\_MEDIA\_CTRL\_START
    :   command to set up media transmission channel

    <a id="_CPPv4N20bk_a2dp_media_ctrl_t26BK_A2DP_MEDIA_CTRL_SUSPENDE"></a>

    <a id="_CPPv3N20bk_a2dp_media_ctrl_t26BK_A2DP_MEDIA_CTRL_SUSPENDE"></a> <a id="_CPPv2N20bk_a2dp_media_ctrl_t26BK_A2DP_MEDIA_CTRL_SUSPENDE"></a> <a id="dm__bt__types_8h_1a026216b39590cf9e5ad2fa2fca7efba0abdce24104465a27adde46d8839e3b9ff"></a> enumerator BK\_A2DP\_MEDIA\_CTRL\_SUSPEND
    :   command to suspend media transmission

<a id="_CPPv425bk_bt_gap_dev_prop_type_t"></a>

<a id="_CPPv325bk_bt_gap_dev_prop_type_t"></a> <a id="_CPPv225bk_bt_gap_dev_prop_type_t"></a> <a id="dm__bt__types_8h_1aa1f2be74afec624071fbb72432cd84ef"></a> enum bk\_bt\_gap\_dev\_prop\_type\_t
:   Bluetooth Device Property type.

    *Values:*

    <a id="_CPPv4N25bk_bt_gap_dev_prop_type_t25BK_BT_GAP_DEV_PROP_BDNAMEE"></a>

    <a id="_CPPv3N25bk_bt_gap_dev_prop_type_t25BK_BT_GAP_DEV_PROP_BDNAMEE"></a> <a id="_CPPv2N25bk_bt_gap_dev_prop_type_t25BK_BT_GAP_DEV_PROP_BDNAMEE"></a> <a id="dm__bt__types_8h_1aa1f2be74afec624071fbb72432cd84efa54380bccd6bf635f57babcbeab79393f"></a> enumerator BK\_BT\_GAP\_DEV\_PROP\_BDNAME
    :   Bluetooth device name, value type is int8\_t \[\]

    <a id="_CPPv4N25bk_bt_gap_dev_prop_type_t22BK_BT_GAP_DEV_PROP_CODE"></a>

    <a id="_CPPv3N25bk_bt_gap_dev_prop_type_t22BK_BT_GAP_DEV_PROP_CODE"></a> <a id="_CPPv2N25bk_bt_gap_dev_prop_type_t22BK_BT_GAP_DEV_PROP_CODE"></a> <a id="dm__bt__types_8h_1aa1f2be74afec624071fbb72432cd84efa237d38b182c93027245632e27949054e"></a> enumerator BK\_BT\_GAP\_DEV\_PROP\_COD
    :   Class of Device, value type is uint32\_t

    <a id="_CPPv4N25bk_bt_gap_dev_prop_type_t23BK_BT_GAP_DEV_PROP_RSSIE"></a>

    <a id="_CPPv3N25bk_bt_gap_dev_prop_type_t23BK_BT_GAP_DEV_PROP_RSSIE"></a> <a id="_CPPv2N25bk_bt_gap_dev_prop_type_t23BK_BT_GAP_DEV_PROP_RSSIE"></a> <a id="dm__bt__types_8h_1aa1f2be74afec624071fbb72432cd84efac624e42fd0288b4fe4f00d3923ebd2f5"></a> enumerator BK\_BT\_GAP\_DEV\_PROP\_RSSI
    :   Received Signal strength Indication, value type is int8\_t, ranging from -128 to 127

    <a id="_CPPv4N25bk_bt_gap_dev_prop_type_t22BK_BT_GAP_DEV_PROP_EIRE"></a>

    <a id="_CPPv3N25bk_bt_gap_dev_prop_type_t22BK_BT_GAP_DEV_PROP_EIRE"></a> <a id="_CPPv2N25bk_bt_gap_dev_prop_type_t22BK_BT_GAP_DEV_PROP_EIRE"></a> <a id="dm__bt__types_8h_1aa1f2be74afec624071fbb72432cd84efaf8606e7599357787ed8134caf745caf2"></a> enumerator BK\_BT\_GAP\_DEV\_PROP\_EIR
    :   Extended Inquiry Response, value type is uint8\_t \[\]

<a id="_CPPv427bk_bt_gap_discovery_state_t"></a>

<a id="_CPPv327bk_bt_gap_discovery_state_t"></a> <a id="_CPPv227bk_bt_gap_discovery_state_t"></a> <a id="dm__bt__types_8h_1a82dc83758cd68660838658f23941afce"></a> enum bk\_bt\_gap\_discovery\_state\_t
:   Bluetooth Device Discovery state

    *Values:*

    <a id="_CPPv4N27bk_bt_gap_discovery_state_t27BK_BT_GAP_DISCOVERY_STOPPEDE"></a>

    <a id="_CPPv3N27bk_bt_gap_discovery_state_t27BK_BT_GAP_DISCOVERY_STOPPEDE"></a> <a id="_CPPv2N27bk_bt_gap_discovery_state_t27BK_BT_GAP_DISCOVERY_STOPPEDE"></a> <a id="dm__bt__types_8h_1a82dc83758cd68660838658f23941afcea724fb584c16f2ccecb97ce45c6f46067"></a> enumerator BK\_BT\_GAP\_DISCOVERY\_STOPPED
    :   Device discovery stopped

    <a id="_CPPv4N27bk_bt_gap_discovery_state_t27BK_BT_GAP_DISCOVERY_STARTEDE"></a>

    <a id="_CPPv3N27bk_bt_gap_discovery_state_t27BK_BT_GAP_DISCOVERY_STARTEDE"></a> <a id="_CPPv2N27bk_bt_gap_discovery_state_t27BK_BT_GAP_DISCOVERY_STARTEDE"></a> <a id="dm__bt__types_8h_1a82dc83758cd68660838658f23941afcea79522f6dfdba2ff8a8f061848582ed2b"></a> enumerator BK\_BT\_GAP\_DISCOVERY\_STARTED
    :   Device discovery started

<a id="_CPPv415bt_event_enum_t"></a>

<a id="_CPPv315bt_event_enum_t"></a> <a id="_CPPv215bt_event_enum_t"></a> <a id="dm__bt__types_8h_1a1e245f2a4d7d5cfa573f37ca214df074"></a> enum bt\_event\_enum\_t
:   *Values:*

    <a id="_CPPv4N15bt_event_enum_t23BK_DM_BT_EVENT_STACK_OKE"></a>

    <a id="_CPPv3N15bt_event_enum_t23BK_DM_BT_EVENT_STACK_OKE"></a> <a id="_CPPv2N15bt_event_enum_t23BK_DM_BT_EVENT_STACK_OKE"></a> <a id="dm__bt__types_8h_1a1e245f2a4d7d5cfa573f37ca214df074a240c857dbc827244e7a230ca661dd8b8"></a> enumerator BK\_DM\_BT\_EVENT\_STACK\_OK
    :   bt stack init ok, param NULL

    <a id="_CPPv4N15bt_event_enum_t29BK_DM_BT_EVENT_INQUIRY_RESULTE"></a>

    <a id="_CPPv3N15bt_event_enum_t29BK_DM_BT_EVENT_INQUIRY_RESULTE"></a> <a id="_CPPv2N15bt_event_enum_t29BK_DM_BT_EVENT_INQUIRY_RESULTE"></a> <a id="dm__bt__types_8h_1a1e245f2a4d7d5cfa573f37ca214df074a00f64493441f9fa8cab85397d6c63355"></a> enumerator BK\_DM\_BT\_EVENT\_INQUIRY\_RESULT
    :   inquiry result, not used now

    <a id="_CPPv4N15bt_event_enum_t25BK_DM_BT_EVENT_DISCONNECTE"></a>

    <a id="_CPPv3N15bt_event_enum_t25BK_DM_BT_EVENT_DISCONNECTE"></a> <a id="_CPPv2N15bt_event_enum_t25BK_DM_BT_EVENT_DISCONNECTE"></a> <a id="dm__bt__types_8h_1a1e245f2a4d7d5cfa573f37ca214df074a00b371859b1dbff8948cc36b7fefa90d"></a> enumerator BK\_DM\_BT\_EVENT\_DISCONNECT
    :   disconnect completed, param addr

    <a id="_CPPv4N15bt_event_enum_t34BK_DM_BT_EVENT_CONNECTION_COMPLETEE"></a>

    <a id="_CPPv3N15bt_event_enum_t34BK_DM_BT_EVENT_CONNECTION_COMPLETEE"></a> <a id="_CPPv2N15bt_event_enum_t34BK_DM_BT_EVENT_CONNECTION_COMPLETEE"></a> <a id="dm__bt__types_8h_1a1e245f2a4d7d5cfa573f37ca214df074a320f89330c3955cc33404c071deeac8a"></a> enumerator BK\_DM\_BT\_EVENT\_CONNECTION\_COMPLETE
    :   connection completed, param addr

    <a id="_CPPv4N15bt_event_enum_t29BK_DM_BT_EVENT_LINKKEY_NOTIFYE"></a>

    <a id="_CPPv3N15bt_event_enum_t29BK_DM_BT_EVENT_LINKKEY_NOTIFYE"></a> <a id="_CPPv2N15bt_event_enum_t29BK_DM_BT_EVENT_LINKKEY_NOTIFYE"></a> <a id="dm__bt__types_8h_1a1e245f2a4d7d5cfa573f37ca214df074a0515e9dadf6a3e5e050ed48e4d8d17eb"></a> enumerator BK\_DM\_BT\_EVENT\_LINKKEY\_NOTIFY
    :   recv cb when pair success and get link key, param [bk\_bt\_linkkey\_storage\_t](#structbk__bt__linkkey__storage__t)

    <a id="_CPPv4N15bt_event_enum_t26BK_DM_BT_EVENT_LINKKEY_REQE"></a>

    <a id="_CPPv3N15bt_event_enum_t26BK_DM_BT_EVENT_LINKKEY_REQE"></a> <a id="_CPPv2N15bt_event_enum_t26BK_DM_BT_EVENT_LINKKEY_REQE"></a> <a id="dm__bt__types_8h_1a1e245f2a4d7d5cfa573f37ca214df074ad22a3500fc103266e735625adc097311"></a> enumerator BK\_DM\_BT\_EVENT\_LINKKEY\_REQ
    :   recv cb when peer need user to input link key, param [bd\_addr\_t](ble.md#structbd__addr__t)

        Device discovery result event, param [bk\_bt\_gap\_cb\_param\_t](#unionbk__bt__gap__cb__param__t)

    <a id="_CPPv4N15bt_event_enum_t25BK_DM_BT_GAP_DISC_RES_EVTE"></a>

    <a id="_CPPv3N15bt_event_enum_t25BK_DM_BT_GAP_DISC_RES_EVTE"></a> <a id="_CPPv2N15bt_event_enum_t25BK_DM_BT_GAP_DISC_RES_EVTE"></a> <a id="dm__bt__types_8h_1a1e245f2a4d7d5cfa573f37ca214df074aaca739721db63dc55504fda81bbbf972"></a> enumerator BK\_DM\_BT\_GAP\_DISC\_RES\_EVT
    :   Discovery state changed event, param [bk\_bt\_gap\_cb\_param\_t](#unionbk__bt__gap__cb__param__t)

    <a id="_CPPv4N15bt_event_enum_t35BK_DM_BT_GAP_DISC_STATE_CHANGED_EVTE"></a>

    <a id="_CPPv3N15bt_event_enum_t35BK_DM_BT_GAP_DISC_STATE_CHANGED_EVTE"></a> <a id="_CPPv2N15bt_event_enum_t35BK_DM_BT_GAP_DISC_STATE_CHANGED_EVTE"></a> <a id="dm__bt__types_8h_1a1e245f2a4d7d5cfa573f37ca214df074a1326f37e7e7f331acf28934c63202797"></a> enumerator BK\_DM\_BT\_GAP\_DISC\_STATE\_CHANGED\_EVT
    :   Authentication complete event, param [bk\_bt\_gap\_cb\_param\_t](#unionbk__bt__gap__cb__param__t)

    <a id="_CPPv4N15bt_event_enum_t26BK_DM_BT_GAP_AUTH_CMPL_EVTE"></a>

    <a id="_CPPv3N15bt_event_enum_t26BK_DM_BT_GAP_AUTH_CMPL_EVTE"></a> <a id="_CPPv2N15bt_event_enum_t26BK_DM_BT_GAP_AUTH_CMPL_EVTE"></a> <a id="dm__bt__types_8h_1a1e245f2a4d7d5cfa573f37ca214df074a5ba84f7f73fb80d3773606e6296563b2"></a> enumerator BK\_DM\_BT\_GAP\_AUTH\_CMPL\_EVT

<a id="_CPPv423bk_avrcp_rn_event_ids_t"></a>

<a id="_CPPv323bk_avrcp_rn_event_ids_t"></a> <a id="_CPPv223bk_avrcp_rn_event_ids_t"></a> <a id="dm__bt__types_8h_1a9f610ed41121b22c7e0da73deaacc2b4"></a> enum bk\_avrcp\_rn\_event\_ids\_t
:   AVRCP event notification ids.

    *Values:*

    <a id="_CPPv4N23bk_avrcp_rn_event_ids_t30BK_AVRCP_RN_PLAY_STATUS_CHANGEE"></a>

    <a id="_CPPv3N23bk_avrcp_rn_event_ids_t30BK_AVRCP_RN_PLAY_STATUS_CHANGEE"></a> <a id="_CPPv2N23bk_avrcp_rn_event_ids_t30BK_AVRCP_RN_PLAY_STATUS_CHANGEE"></a> <a id="dm__bt__types_8h_1a9f610ed41121b22c7e0da73deaacc2b4a51f37ad1a62b2ba8ea12d7df77d9e3eb"></a> enumerator BK\_AVRCP\_RN\_PLAY\_STATUS\_CHANGE
    :   track status change, eg. from playing to paused

    <a id="_CPPv4N23bk_avrcp_rn_event_ids_t24BK_AVRCP_RN_TRACK_CHANGEE"></a>

    <a id="_CPPv3N23bk_avrcp_rn_event_ids_t24BK_AVRCP_RN_TRACK_CHANGEE"></a> <a id="_CPPv2N23bk_avrcp_rn_event_ids_t24BK_AVRCP_RN_TRACK_CHANGEE"></a> <a id="dm__bt__types_8h_1a9f610ed41121b22c7e0da73deaacc2b4af5c4c294a36b5f0fdfa5c4a57f95fb80"></a> enumerator BK\_AVRCP\_RN\_TRACK\_CHANGE
    :   new track is loaded

    <a id="_CPPv4N23bk_avrcp_rn_event_ids_t29BK_AVRCP_RN_TRACK_REACHED_ENDE"></a>

    <a id="_CPPv3N23bk_avrcp_rn_event_ids_t29BK_AVRCP_RN_TRACK_REACHED_ENDE"></a> <a id="_CPPv2N23bk_avrcp_rn_event_ids_t29BK_AVRCP_RN_TRACK_REACHED_ENDE"></a> <a id="dm__bt__types_8h_1a9f610ed41121b22c7e0da73deaacc2b4a91a2f67514018f1ea2718d7dca3d2ea9"></a> enumerator BK\_AVRCP\_RN\_TRACK\_REACHED\_END
    :   current track reached end

    <a id="_CPPv4N23bk_avrcp_rn_event_ids_t31BK_AVRCP_RN_TRACK_REACHED_STARTE"></a>

    <a id="_CPPv3N23bk_avrcp_rn_event_ids_t31BK_AVRCP_RN_TRACK_REACHED_STARTE"></a> <a id="_CPPv2N23bk_avrcp_rn_event_ids_t31BK_AVRCP_RN_TRACK_REACHED_STARTE"></a> <a id="dm__bt__types_8h_1a9f610ed41121b22c7e0da73deaacc2b4aac65c06ee15b66ce751c9950c4c41efa"></a> enumerator BK\_AVRCP\_RN\_TRACK\_REACHED\_START
    :   current track reached start position

    <a id="_CPPv4N23bk_avrcp_rn_event_ids_t28BK_AVRCP_RN_PLAY_POS_CHANGEDE"></a>

    <a id="_CPPv3N23bk_avrcp_rn_event_ids_t28BK_AVRCP_RN_PLAY_POS_CHANGEDE"></a> <a id="_CPPv2N23bk_avrcp_rn_event_ids_t28BK_AVRCP_RN_PLAY_POS_CHANGEDE"></a> <a id="dm__bt__types_8h_1a9f610ed41121b22c7e0da73deaacc2b4acb9e5ef96254c6e27917a2f3559d4be1"></a> enumerator BK\_AVRCP\_RN\_PLAY\_POS\_CHANGED
    :   track playing position changed

    <a id="_CPPv4N23bk_avrcp_rn_event_ids_t33BK_AVRCP_RN_BATTERY_STATUS_CHANGEE"></a>

    <a id="_CPPv3N23bk_avrcp_rn_event_ids_t33BK_AVRCP_RN_BATTERY_STATUS_CHANGEE"></a> <a id="_CPPv2N23bk_avrcp_rn_event_ids_t33BK_AVRCP_RN_BATTERY_STATUS_CHANGEE"></a> <a id="dm__bt__types_8h_1a9f610ed41121b22c7e0da73deaacc2b4a5be43be4bec709e872b886404895a14c"></a> enumerator BK\_AVRCP\_RN\_BATTERY\_STATUS\_CHANGE
    :   battery status changed

    <a id="_CPPv4N23bk_avrcp_rn_event_ids_t32BK_AVRCP_RN_SYSTEM_STATUS_CHANGEE"></a>

    <a id="_CPPv3N23bk_avrcp_rn_event_ids_t32BK_AVRCP_RN_SYSTEM_STATUS_CHANGEE"></a> <a id="_CPPv2N23bk_avrcp_rn_event_ids_t32BK_AVRCP_RN_SYSTEM_STATUS_CHANGEE"></a> <a id="dm__bt__types_8h_1a9f610ed41121b22c7e0da73deaacc2b4ade1b694f4b8c319cbdd42c3ed166185a"></a> enumerator BK\_AVRCP\_RN\_SYSTEM\_STATUS\_CHANGE
    :   system status changed

    <a id="_CPPv4N23bk_avrcp_rn_event_ids_t30BK_AVRCP_RN_APP_SETTING_CHANGEE"></a>

    <a id="_CPPv3N23bk_avrcp_rn_event_ids_t30BK_AVRCP_RN_APP_SETTING_CHANGEE"></a> <a id="_CPPv2N23bk_avrcp_rn_event_ids_t30BK_AVRCP_RN_APP_SETTING_CHANGEE"></a> <a id="dm__bt__types_8h_1a9f610ed41121b22c7e0da73deaacc2b4a4faa93ed22abf30fce5f16f58a44431a"></a> enumerator BK\_AVRCP\_RN\_APP\_SETTING\_CHANGE
    :   application settings changed

    <a id="_CPPv4N23bk_avrcp_rn_event_ids_t30BK_AVRCP_RN_NOW_PLAYING_CHANGEE"></a>

    <a id="_CPPv3N23bk_avrcp_rn_event_ids_t30BK_AVRCP_RN_NOW_PLAYING_CHANGEE"></a> <a id="_CPPv2N23bk_avrcp_rn_event_ids_t30BK_AVRCP_RN_NOW_PLAYING_CHANGEE"></a> <a id="dm__bt__types_8h_1a9f610ed41121b22c7e0da73deaacc2b4a9419cbd82937f75444a01273cb2a9384"></a> enumerator BK\_AVRCP\_RN\_NOW\_PLAYING\_CHANGE
    :   now playing content changed

    <a id="_CPPv4N23bk_avrcp_rn_event_ids_t36BK_AVRCP_RN_AVAILABLE_PLAYERS_CHANGEE"></a>

    <a id="_CPPv3N23bk_avrcp_rn_event_ids_t36BK_AVRCP_RN_AVAILABLE_PLAYERS_CHANGEE"></a> <a id="_CPPv2N23bk_avrcp_rn_event_ids_t36BK_AVRCP_RN_AVAILABLE_PLAYERS_CHANGEE"></a> <a id="dm__bt__types_8h_1a9f610ed41121b22c7e0da73deaacc2b4a4a742e54dea35f71c6b537c55a3dc852"></a> enumerator BK\_AVRCP\_RN\_AVAILABLE\_PLAYERS\_CHANGE
    :   available players changed

    <a id="_CPPv4N23bk_avrcp_rn_event_ids_t35BK_AVRCP_RN_ADDRESSED_PLAYER_CHANGEE"></a>

    <a id="_CPPv3N23bk_avrcp_rn_event_ids_t35BK_AVRCP_RN_ADDRESSED_PLAYER_CHANGEE"></a> <a id="_CPPv2N23bk_avrcp_rn_event_ids_t35BK_AVRCP_RN_ADDRESSED_PLAYER_CHANGEE"></a> <a id="dm__bt__types_8h_1a9f610ed41121b22c7e0da73deaacc2b4a89629d4ce833c585823025488f873c90"></a> enumerator BK\_AVRCP\_RN\_ADDRESSED\_PLAYER\_CHANGE
    :   the addressed player changed

    <a id="_CPPv4N23bk_avrcp_rn_event_ids_t23BK_AVRCP_RN_UIDS_CHANGEE"></a>

    <a id="_CPPv3N23bk_avrcp_rn_event_ids_t23BK_AVRCP_RN_UIDS_CHANGEE"></a> <a id="_CPPv2N23bk_avrcp_rn_event_ids_t23BK_AVRCP_RN_UIDS_CHANGEE"></a> <a id="dm__bt__types_8h_1a9f610ed41121b22c7e0da73deaacc2b4aeafaeabcffea53bf2bec660722d074f6"></a> enumerator BK\_AVRCP\_RN\_UIDS\_CHANGE
    :   UIDs changed

    <a id="_CPPv4N23bk_avrcp_rn_event_ids_t25BK_AVRCP_RN_VOLUME_CHANGEE"></a>

    <a id="_CPPv3N23bk_avrcp_rn_event_ids_t25BK_AVRCP_RN_VOLUME_CHANGEE"></a> <a id="_CPPv2N23bk_avrcp_rn_event_ids_t25BK_AVRCP_RN_VOLUME_CHANGEE"></a> <a id="dm__bt__types_8h_1a9f610ed41121b22c7e0da73deaacc2b4acb9a2787129aadd5ed1259142fd9cf65"></a> enumerator BK\_AVRCP\_RN\_VOLUME\_CHANGE
    :   volume changed locally on TG

    <a id="_CPPv4N23bk_avrcp_rn_event_ids_t19BK_AVRCP_RN_MAX_EVTE"></a>

    <a id="_CPPv3N23bk_avrcp_rn_event_ids_t19BK_AVRCP_RN_MAX_EVTE"></a> <a id="_CPPv2N23bk_avrcp_rn_event_ids_t19BK_AVRCP_RN_MAX_EVTE"></a> <a id="dm__bt__types_8h_1a9f610ed41121b22c7e0da73deaacc2b4a2691df6d71f300710e13340695e9a767"></a> enumerator BK\_AVRCP\_RN\_MAX\_EVT

<a id="_CPPv422bk_avrcp_ct_cb_event_t"></a>

<a id="_CPPv322bk_avrcp_ct_cb_event_t"></a> <a id="_CPPv222bk_avrcp_ct_cb_event_t"></a> <a id="dm__bt__types_8h_1aa33191d1e57e846ceaf0e8abdaa8d1c0"></a> enum bk\_avrcp\_ct\_cb\_event\_t
:   AVRCP Controller callback events.

    *Values:*

    <a id="_CPPv4N22bk_avrcp_ct_cb_event_t32BK_AVRCP_CT_CONNECTION_STATE_EVTE"></a>

    <a id="_CPPv3N22bk_avrcp_ct_cb_event_t32BK_AVRCP_CT_CONNECTION_STATE_EVTE"></a> <a id="_CPPv2N22bk_avrcp_ct_cb_event_t32BK_AVRCP_CT_CONNECTION_STATE_EVTE"></a> <a id="dm__bt__types_8h_1aa33191d1e57e846ceaf0e8abdaa8d1c0aa87a8c91b50434976ef87e7be6459442"></a> enumerator BK\_AVRCP\_CT\_CONNECTION\_STATE\_EVT
    :   connection state changed event

    <a id="_CPPv4N22bk_avrcp_ct_cb_event_t31BK_AVRCP_CT_PASSTHROUGH_RSP_EVTE"></a>

    <a id="_CPPv3N22bk_avrcp_ct_cb_event_t31BK_AVRCP_CT_PASSTHROUGH_RSP_EVTE"></a> <a id="_CPPv2N22bk_avrcp_ct_cb_event_t31BK_AVRCP_CT_PASSTHROUGH_RSP_EVTE"></a> <a id="dm__bt__types_8h_1aa33191d1e57e846ceaf0e8abdaa8d1c0acb65eb943853e69dd3bad1ea71b21a00"></a> enumerator BK\_AVRCP\_CT\_PASSTHROUGH\_RSP\_EVT
    :   passthrough response event

    <a id="_CPPv4N22bk_avrcp_ct_cb_event_t28BK_AVRCP_CT_METADATA_RSP_EVTE"></a>

    <a id="_CPPv3N22bk_avrcp_ct_cb_event_t28BK_AVRCP_CT_METADATA_RSP_EVTE"></a> <a id="_CPPv2N22bk_avrcp_ct_cb_event_t28BK_AVRCP_CT_METADATA_RSP_EVTE"></a> <a id="dm__bt__types_8h_1aa33191d1e57e846ceaf0e8abdaa8d1c0acbe8b309d23d3a7dcbcd932edecd662e"></a> enumerator BK\_AVRCP\_CT\_METADATA\_RSP\_EVT
    :   metadata response event

    <a id="_CPPv4N22bk_avrcp_ct_cb_event_t31BK_AVRCP_CT_PLAY_STATUS_RSP_EVTE"></a>

    <a id="_CPPv3N22bk_avrcp_ct_cb_event_t31BK_AVRCP_CT_PLAY_STATUS_RSP_EVTE"></a> <a id="_CPPv2N22bk_avrcp_ct_cb_event_t31BK_AVRCP_CT_PLAY_STATUS_RSP_EVTE"></a> <a id="dm__bt__types_8h_1aa33191d1e57e846ceaf0e8abdaa8d1c0a77db166c0c5c467e4ce28c30621d384b"></a> enumerator BK\_AVRCP\_CT\_PLAY\_STATUS\_RSP\_EVT
    :   play status response event

    <a id="_CPPv4N22bk_avrcp_ct_cb_event_t29BK_AVRCP_CT_CHANGE_NOTIFY_EVTE"></a>

    <a id="_CPPv3N22bk_avrcp_ct_cb_event_t29BK_AVRCP_CT_CHANGE_NOTIFY_EVTE"></a> <a id="_CPPv2N22bk_avrcp_ct_cb_event_t29BK_AVRCP_CT_CHANGE_NOTIFY_EVTE"></a> <a id="dm__bt__types_8h_1aa33191d1e57e846ceaf0e8abdaa8d1c0a430f301f662eac93af1d5e05cd3fb4fc"></a> enumerator BK\_AVRCP\_CT\_CHANGE\_NOTIFY\_EVT
    :   notification event

    <a id="_CPPv4N22bk_avrcp_ct_cb_event_t31BK_AVRCP_CT_REMOTE_FEATURES_EVTE"></a>

    <a id="_CPPv3N22bk_avrcp_ct_cb_event_t31BK_AVRCP_CT_REMOTE_FEATURES_EVTE"></a> <a id="_CPPv2N22bk_avrcp_ct_cb_event_t31BK_AVRCP_CT_REMOTE_FEATURES_EVTE"></a> <a id="dm__bt__types_8h_1aa33191d1e57e846ceaf0e8abdaa8d1c0a60b68e2be5db5827becc9cd05d5136e8"></a> enumerator BK\_AVRCP\_CT\_REMOTE\_FEATURES\_EVT
    :   feature of remote device indication event

    <a id="_CPPv4N22bk_avrcp_ct_cb_event_t39BK_AVRCP_CT_GET_RN_CAPABILITIES_RSP_EVTE"></a>

    <a id="_CPPv3N22bk_avrcp_ct_cb_event_t39BK_AVRCP_CT_GET_RN_CAPABILITIES_RSP_EVTE"></a> <a id="_CPPv2N22bk_avrcp_ct_cb_event_t39BK_AVRCP_CT_GET_RN_CAPABILITIES_RSP_EVTE"></a> <a id="dm__bt__types_8h_1aa33191d1e57e846ceaf0e8abdaa8d1c0aa07f2f7c12781a476755a5897ec47757"></a> enumerator BK\_AVRCP\_CT\_GET\_RN\_CAPABILITIES\_RSP\_EVT
    :   supported notification events capability of peer device

    <a id="_CPPv4N22bk_avrcp_ct_cb_event_t39BK_AVRCP_CT_SET_ABSOLUTE_VOLUME_RSP_EVTE"></a>

    <a id="_CPPv3N22bk_avrcp_ct_cb_event_t39BK_AVRCP_CT_SET_ABSOLUTE_VOLUME_RSP_EVTE"></a> <a id="_CPPv2N22bk_avrcp_ct_cb_event_t39BK_AVRCP_CT_SET_ABSOLUTE_VOLUME_RSP_EVTE"></a> <a id="dm__bt__types_8h_1aa33191d1e57e846ceaf0e8abdaa8d1c0a99c8d02106c1e97b1e77f922b8a25406"></a> enumerator BK\_AVRCP\_CT\_SET\_ABSOLUTE\_VOLUME\_RSP\_EVT
    :   set absolute volume response event

<a id="_CPPv420bk_avrcp_batt_stat_t"></a>

<a id="_CPPv320bk_avrcp_batt_stat_t"></a> <a id="_CPPv220bk_avrcp_batt_stat_t"></a> <a id="dm__bt__types_8h_1a797447618ccc72cadc5acd07b04ce3dd"></a> enum bk\_avrcp\_batt\_stat\_t
:   AVRCP battery status.

    *Values:*

    <a id="_CPPv4N20bk_avrcp_batt_stat_t20BK_AVRCP_BATT_NORMALE"></a>

    <a id="_CPPv3N20bk_avrcp_batt_stat_t20BK_AVRCP_BATT_NORMALE"></a> <a id="_CPPv2N20bk_avrcp_batt_stat_t20BK_AVRCP_BATT_NORMALE"></a> <a id="dm__bt__types_8h_1a797447618ccc72cadc5acd07b04ce3dda253093c24586cbc2909e6dc774169bc8"></a> enumerator BK\_AVRCP\_BATT\_NORMAL
    :   normal state

    <a id="_CPPv4N20bk_avrcp_batt_stat_t21BK_AVRCP_BATT_WARNINGE"></a>

    <a id="_CPPv3N20bk_avrcp_batt_stat_t21BK_AVRCP_BATT_WARNINGE"></a> <a id="_CPPv2N20bk_avrcp_batt_stat_t21BK_AVRCP_BATT_WARNINGE"></a> <a id="dm__bt__types_8h_1a797447618ccc72cadc5acd07b04ce3ddaf7804f0a0b252ecfd3bf4e8c2d70beea"></a> enumerator BK\_AVRCP\_BATT\_WARNING
    :   unable to operate soon

    <a id="_CPPv4N20bk_avrcp_batt_stat_t22BK_AVRCP_BATT_CRITICALE"></a>

    <a id="_CPPv3N20bk_avrcp_batt_stat_t22BK_AVRCP_BATT_CRITICALE"></a> <a id="_CPPv2N20bk_avrcp_batt_stat_t22BK_AVRCP_BATT_CRITICALE"></a> <a id="dm__bt__types_8h_1a797447618ccc72cadc5acd07b04ce3dda342eae6c11af9d6aaded9566c5208782"></a> enumerator BK\_AVRCP\_BATT\_CRITICAL
    :   cannot operate any more

    <a id="_CPPv4N20bk_avrcp_batt_stat_t22BK_AVRCP_BATT_EXTERNALE"></a>

    <a id="_CPPv3N20bk_avrcp_batt_stat_t22BK_AVRCP_BATT_EXTERNALE"></a> <a id="_CPPv2N20bk_avrcp_batt_stat_t22BK_AVRCP_BATT_EXTERNALE"></a> <a id="dm__bt__types_8h_1a797447618ccc72cadc5acd07b04ce3dda7475438d3c30f276b125ead80f1817d4"></a> enumerator BK\_AVRCP\_BATT\_EXTERNAL
    :   plugged to external power supply

    <a id="_CPPv4N20bk_avrcp_batt_stat_t25BK_AVRCP_BATT_FULL_CHARGEE"></a>

    <a id="_CPPv3N20bk_avrcp_batt_stat_t25BK_AVRCP_BATT_FULL_CHARGEE"></a> <a id="_CPPv2N20bk_avrcp_batt_stat_t25BK_AVRCP_BATT_FULL_CHARGEE"></a> <a id="dm__bt__types_8h_1a797447618ccc72cadc5acd07b04ce3ddaabc59922d547b80f715dc265e6f82a17"></a> enumerator BK\_AVRCP\_BATT\_FULL\_CHARGE
    :   when completely charged from external power supply

<a id="_CPPv424bk_avrcp_playback_stat_t"></a>

<a id="_CPPv324bk_avrcp_playback_stat_t"></a> <a id="_CPPv224bk_avrcp_playback_stat_t"></a> <a id="dm__bt__types_8h_1a4f81825b1f00405e5a5694dea91b975c"></a> enum bk\_avrcp\_playback\_stat\_t
:   AVRCP current status of playback.

    *Values:*

    <a id="_CPPv4N24bk_avrcp_playback_stat_t25BK_AVRCP_PLAYBACK_STOPPEDE"></a>

    <a id="_CPPv3N24bk_avrcp_playback_stat_t25BK_AVRCP_PLAYBACK_STOPPEDE"></a> <a id="_CPPv2N24bk_avrcp_playback_stat_t25BK_AVRCP_PLAYBACK_STOPPEDE"></a> <a id="dm__bt__types_8h_1a4f81825b1f00405e5a5694dea91b975caea0a025a267b0b1a603f5da2891db30b"></a> enumerator BK\_AVRCP\_PLAYBACK\_STOPPED
    :   stopped

    <a id="_CPPv4N24bk_avrcp_playback_stat_t25BK_AVRCP_PLAYBACK_PLAYINGE"></a>

    <a id="_CPPv3N24bk_avrcp_playback_stat_t25BK_AVRCP_PLAYBACK_PLAYINGE"></a> <a id="_CPPv2N24bk_avrcp_playback_stat_t25BK_AVRCP_PLAYBACK_PLAYINGE"></a> <a id="dm__bt__types_8h_1a4f81825b1f00405e5a5694dea91b975ca72fc96ef5eb98035a6d4604e169426a5"></a> enumerator BK\_AVRCP\_PLAYBACK\_PLAYING
    :   playing

    <a id="_CPPv4N24bk_avrcp_playback_stat_t24BK_AVRCP_PLAYBACK_PAUSEDE"></a>

    <a id="_CPPv3N24bk_avrcp_playback_stat_t24BK_AVRCP_PLAYBACK_PAUSEDE"></a> <a id="_CPPv2N24bk_avrcp_playback_stat_t24BK_AVRCP_PLAYBACK_PAUSEDE"></a> <a id="dm__bt__types_8h_1a4f81825b1f00405e5a5694dea91b975ca8b7da446d4ee4a61c7ffaa144c378e69"></a> enumerator BK\_AVRCP\_PLAYBACK\_PAUSED
    :   paused

    <a id="_CPPv4N24bk_avrcp_playback_stat_t26BK_AVRCP_PLAYBACK_FWD_SEEKE"></a>

    <a id="_CPPv3N24bk_avrcp_playback_stat_t26BK_AVRCP_PLAYBACK_FWD_SEEKE"></a> <a id="_CPPv2N24bk_avrcp_playback_stat_t26BK_AVRCP_PLAYBACK_FWD_SEEKE"></a> <a id="dm__bt__types_8h_1a4f81825b1f00405e5a5694dea91b975ca76c71c7aefeb9835aa79d354324b6175"></a> enumerator BK\_AVRCP\_PLAYBACK\_FWD\_SEEK
    :   forward seek

    <a id="_CPPv4N24bk_avrcp_playback_stat_t26BK_AVRCP_PLAYBACK_REV_SEEKE"></a>

    <a id="_CPPv3N24bk_avrcp_playback_stat_t26BK_AVRCP_PLAYBACK_REV_SEEKE"></a> <a id="_CPPv2N24bk_avrcp_playback_stat_t26BK_AVRCP_PLAYBACK_REV_SEEKE"></a> <a id="dm__bt__types_8h_1a4f81825b1f00405e5a5694dea91b975caa17fdc49adf06050ea078ab34458c66e"></a> enumerator BK\_AVRCP\_PLAYBACK\_REV\_SEEK
    :   reverse seek

    <a id="_CPPv4N24bk_avrcp_playback_stat_t23BK_AVRCP_PLAYBACK_ERRORE"></a>

    <a id="_CPPv3N24bk_avrcp_playback_stat_t23BK_AVRCP_PLAYBACK_ERRORE"></a> <a id="_CPPv2N24bk_avrcp_playback_stat_t23BK_AVRCP_PLAYBACK_ERRORE"></a> <a id="dm__bt__types_8h_1a4f81825b1f00405e5a5694dea91b975ca033f405d46b82f5e5d49c2c6f41ff20c"></a> enumerator BK\_AVRCP\_PLAYBACK\_ERROR
    :   error

<a id="_CPPv417bk_avrcp_pt_cmd_t"></a>

<a id="_CPPv317bk_avrcp_pt_cmd_t"></a> <a id="_CPPv217bk_avrcp_pt_cmd_t"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701"></a> enum bk\_avrcp\_pt\_cmd\_t
:   AVRCP passthrough command code.

    *Values:*

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t22BK_AVRCP_PT_CMD_SELECTE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t22BK_AVRCP_PT_CMD_SELECTE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t22BK_AVRCP_PT_CMD_SELECTE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a84bd40bb4a123d498aa57489acff71b5"></a> enumerator BK\_AVRCP\_PT\_CMD\_SELECT
    :   select

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t18BK_AVRCP_PT_CMD_UPE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t18BK_AVRCP_PT_CMD_UPE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t18BK_AVRCP_PT_CMD_UPE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a3146314ce4fff6c9247abb7f7000a7a9"></a> enumerator BK\_AVRCP\_PT\_CMD\_UP
    :   up

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t20BK_AVRCP_PT_CMD_DOWNE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t20BK_AVRCP_PT_CMD_DOWNE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t20BK_AVRCP_PT_CMD_DOWNE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701af5a04527adce945c2dff044e2e518413"></a> enumerator BK\_AVRCP\_PT\_CMD\_DOWN
    :   down

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t20BK_AVRCP_PT_CMD_LEFTE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t20BK_AVRCP_PT_CMD_LEFTE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t20BK_AVRCP_PT_CMD_LEFTE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a0dca3356100bda0daaa116e4b7bcd19a"></a> enumerator BK\_AVRCP\_PT\_CMD\_LEFT
    :   left

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t21BK_AVRCP_PT_CMD_RIGHTE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t21BK_AVRCP_PT_CMD_RIGHTE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t21BK_AVRCP_PT_CMD_RIGHTE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701aafe5a1447b374ddd1bb6aec86d057217"></a> enumerator BK\_AVRCP\_PT\_CMD\_RIGHT
    :   right

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t24BK_AVRCP_PT_CMD_RIGHT_UPE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t24BK_AVRCP_PT_CMD_RIGHT_UPE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t24BK_AVRCP_PT_CMD_RIGHT_UPE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701ad957ab2f3bbd5d406f1ddea0a3e10f21"></a> enumerator BK\_AVRCP\_PT\_CMD\_RIGHT\_UP
    :   right-up

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t26BK_AVRCP_PT_CMD_RIGHT_DOWNE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t26BK_AVRCP_PT_CMD_RIGHT_DOWNE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t26BK_AVRCP_PT_CMD_RIGHT_DOWNE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a50937cac078d4e3b9cd02129e8b0c2b9"></a> enumerator BK\_AVRCP\_PT\_CMD\_RIGHT\_DOWN
    :   right-down

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t23BK_AVRCP_PT_CMD_LEFT_UPE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t23BK_AVRCP_PT_CMD_LEFT_UPE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t23BK_AVRCP_PT_CMD_LEFT_UPE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a8bbcb7b3797bec056d418161801023bd"></a> enumerator BK\_AVRCP\_PT\_CMD\_LEFT\_UP
    :   left-up

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_LEFT_DOWNE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_LEFT_DOWNE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_LEFT_DOWNE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a0154b4ad991696b29d4178b250f545f3"></a> enumerator BK\_AVRCP\_PT\_CMD\_LEFT\_DOWN
    :   left-down

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_ROOT_MENUE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_ROOT_MENUE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_ROOT_MENUE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701af83ce89a77c8763127f8c0c8e15a8dd5"></a> enumerator BK\_AVRCP\_PT\_CMD\_ROOT\_MENU
    :   root menu

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t26BK_AVRCP_PT_CMD_SETUP_MENUE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t26BK_AVRCP_PT_CMD_SETUP_MENUE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t26BK_AVRCP_PT_CMD_SETUP_MENUE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701ac5ee19d87dd5adadeda96b9e86673d1a"></a> enumerator BK\_AVRCP\_PT\_CMD\_SETUP\_MENU
    :   setup menu

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_CONT_MENUE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_CONT_MENUE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_CONT_MENUE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a7001b5ed6defcba0e7d73c18c50a746c"></a> enumerator BK\_AVRCP\_PT\_CMD\_CONT\_MENU
    :   contents menu

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t24BK_AVRCP_PT_CMD_FAV_MENUE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t24BK_AVRCP_PT_CMD_FAV_MENUE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t24BK_AVRCP_PT_CMD_FAV_MENUE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a8865092bf33f48f8d2d3f551a07c7f01"></a> enumerator BK\_AVRCP\_PT\_CMD\_FAV\_MENU
    :   favorite menu

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t20BK_AVRCP_PT_CMD_EXITE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t20BK_AVRCP_PT_CMD_EXITE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t20BK_AVRCP_PT_CMD_EXITE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701aab48a86dff326d5d39f24c6c833ec286"></a> enumerator BK\_AVRCP\_PT\_CMD\_EXIT
    :   exit

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_0E"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_0E"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_0E"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701aad4f990b86227490bac3c71191a3aca7"></a> enumerator BK\_AVRCP\_PT\_CMD\_0
    :   0

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_1E"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_1E"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_1E"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701ab7868003d706a323c6d68d5acfed5a8c"></a> enumerator BK\_AVRCP\_PT\_CMD\_1
    :   1

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_2E"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_2E"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_2E"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a033b5186f3e1ed6b75bd90b10afe4a88"></a> enumerator BK\_AVRCP\_PT\_CMD\_2
    :   2

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_3E"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_3E"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_3E"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a185b0d5e57cfbcb49b4a7e624d0676fc"></a> enumerator BK\_AVRCP\_PT\_CMD\_3
    :   3

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_4E"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_4E"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_4E"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701ad885fcf8d2f8ea242e87d0fbad1fce5f"></a> enumerator BK\_AVRCP\_PT\_CMD\_4
    :   4

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_5E"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_5E"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_5E"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a39485cc3bca8d3d72c58450a2b420d4f"></a> enumerator BK\_AVRCP\_PT\_CMD\_5
    :   5

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_6E"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_6E"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_6E"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a151fb9c4fa0a23eafc3fa5044e6645ed"></a> enumerator BK\_AVRCP\_PT\_CMD\_6
    :   6

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_7E"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_7E"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_7E"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701af2054c7e21d07fb5d59c1c8b7d007cd4"></a> enumerator BK\_AVRCP\_PT\_CMD\_7
    :   7

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_8E"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_8E"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_8E"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a70f4f117693c49ddf4132c197ca30d83"></a> enumerator BK\_AVRCP\_PT\_CMD\_8
    :   8

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_9E"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_9E"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t17BK_AVRCP_PT_CMD_9E"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a47ea1b5f1334bb5495730cc2fd1d6399"></a> enumerator BK\_AVRCP\_PT\_CMD\_9
    :   9

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t19BK_AVRCP_PT_CMD_DOTE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t19BK_AVRCP_PT_CMD_DOTE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t19BK_AVRCP_PT_CMD_DOTE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a13a2751cd92dde88045f8fc09df8351f"></a> enumerator BK\_AVRCP\_PT\_CMD\_DOT
    :   dot

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t21BK_AVRCP_PT_CMD_ENTERE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t21BK_AVRCP_PT_CMD_ENTERE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t21BK_AVRCP_PT_CMD_ENTERE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a349a86cb9d0efa0f7c690d55a23b910d"></a> enumerator BK\_AVRCP\_PT\_CMD\_ENTER
    :   enter

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t21BK_AVRCP_PT_CMD_CLEARE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t21BK_AVRCP_PT_CMD_CLEARE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t21BK_AVRCP_PT_CMD_CLEARE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701ab8729b06212e30e4ad33eca88be3fc60"></a> enumerator BK\_AVRCP\_PT\_CMD\_CLEAR
    :   clear

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t23BK_AVRCP_PT_CMD_CHAN_UPE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t23BK_AVRCP_PT_CMD_CHAN_UPE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t23BK_AVRCP_PT_CMD_CHAN_UPE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a5c2ffd072684bdc40299ba16f0f9b861"></a> enumerator BK\_AVRCP\_PT\_CMD\_CHAN\_UP
    :   channel up

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_CHAN_DOWNE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_CHAN_DOWNE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_CHAN_DOWNE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a7497d7e0375648637a6ba5e4ff62cf46"></a> enumerator BK\_AVRCP\_PT\_CMD\_CHAN\_DOWN
    :   channel down

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_PREV_CHANE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_PREV_CHANE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_PREV_CHANE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701af8b9f935fb7c9b22bf5a8c362fc2468f"></a> enumerator BK\_AVRCP\_PT\_CMD\_PREV\_CHAN
    :   previous channel

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_SOUND_SELE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_SOUND_SELE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_SOUND_SELE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701adba3442b8c38eeeed58da19c0ffcf61f"></a> enumerator BK\_AVRCP\_PT\_CMD\_SOUND\_SEL
    :   sound select

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_INPUT_SELE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_INPUT_SELE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_INPUT_SELE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a70ea29cb1a105c2f69e4ea6694da2d56"></a> enumerator BK\_AVRCP\_PT\_CMD\_INPUT\_SEL
    :   input select

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_DISP_INFOE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_DISP_INFOE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_DISP_INFOE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a2b95d281c0cf36d53e1a4183ec7388dc"></a> enumerator BK\_AVRCP\_PT\_CMD\_DISP\_INFO
    :   display information

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t20BK_AVRCP_PT_CMD_HELPE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t20BK_AVRCP_PT_CMD_HELPE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t20BK_AVRCP_PT_CMD_HELPE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a2cf3a272caa073447fc8712608efb837"></a> enumerator BK\_AVRCP\_PT\_CMD\_HELP
    :   help

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t23BK_AVRCP_PT_CMD_PAGE_UPE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t23BK_AVRCP_PT_CMD_PAGE_UPE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t23BK_AVRCP_PT_CMD_PAGE_UPE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701ad2645a23031264ed5c3ba10eb00f4604"></a> enumerator BK\_AVRCP\_PT\_CMD\_PAGE\_UP
    :   page up

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_PAGE_DOWNE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_PAGE_DOWNE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t25BK_AVRCP_PT_CMD_PAGE_DOWNE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a55a3318f848ca012897d6e76ab3b370c"></a> enumerator BK\_AVRCP\_PT\_CMD\_PAGE\_DOWN
    :   page down

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t21BK_AVRCP_PT_CMD_POWERE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t21BK_AVRCP_PT_CMD_POWERE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t21BK_AVRCP_PT_CMD_POWERE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701ab247eb05286afec0482665a6c7f0a91f"></a> enumerator BK\_AVRCP\_PT\_CMD\_POWER
    :   power

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t22BK_AVRCP_PT_CMD_VOL_UPE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t22BK_AVRCP_PT_CMD_VOL_UPE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t22BK_AVRCP_PT_CMD_VOL_UPE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a5654e9e729e66bd3c2d0e27eca7bc963"></a> enumerator BK\_AVRCP\_PT\_CMD\_VOL\_UP
    :   volume up

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t24BK_AVRCP_PT_CMD_VOL_DOWNE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t24BK_AVRCP_PT_CMD_VOL_DOWNE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t24BK_AVRCP_PT_CMD_VOL_DOWNE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a712afd017c4246b7052778de7d5f61b0"></a> enumerator BK\_AVRCP\_PT\_CMD\_VOL\_DOWN
    :   volume down

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t20BK_AVRCP_PT_CMD_MUTEE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t20BK_AVRCP_PT_CMD_MUTEE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t20BK_AVRCP_PT_CMD_MUTEE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a871707c5039cb6a245547ff4db7c2f87"></a> enumerator BK\_AVRCP\_PT\_CMD\_MUTE
    :   mute

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t20BK_AVRCP_PT_CMD_PLAYE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t20BK_AVRCP_PT_CMD_PLAYE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t20BK_AVRCP_PT_CMD_PLAYE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a06f284a1284901c5312256de851d6625"></a> enumerator BK\_AVRCP\_PT\_CMD\_PLAY
    :   play

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t20BK_AVRCP_PT_CMD_STOPE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t20BK_AVRCP_PT_CMD_STOPE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t20BK_AVRCP_PT_CMD_STOPE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a0fa51cd5a691df1607ef76476d2286ba"></a> enumerator BK\_AVRCP\_PT\_CMD\_STOP
    :   stop

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t21BK_AVRCP_PT_CMD_PAUSEE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t21BK_AVRCP_PT_CMD_PAUSEE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t21BK_AVRCP_PT_CMD_PAUSEE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a89cefcd216afa2ebf0efb58fc7369c2a"></a> enumerator BK\_AVRCP\_PT\_CMD\_PAUSE
    :   pause

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t22BK_AVRCP_PT_CMD_RECORDE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t22BK_AVRCP_PT_CMD_RECORDE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t22BK_AVRCP_PT_CMD_RECORDE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a437138a84b3bebc750e456ee2c581c78"></a> enumerator BK\_AVRCP\_PT\_CMD\_RECORD
    :   record

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t22BK_AVRCP_PT_CMD_REWINDE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t22BK_AVRCP_PT_CMD_REWINDE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t22BK_AVRCP_PT_CMD_REWINDE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a62dfaa4d5b05cbf0057737db6c5f90ab"></a> enumerator BK\_AVRCP\_PT\_CMD\_REWIND
    :   rewind

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t28BK_AVRCP_PT_CMD_FAST_FORWARDE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t28BK_AVRCP_PT_CMD_FAST_FORWARDE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t28BK_AVRCP_PT_CMD_FAST_FORWARDE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701ab2e59598f6fbf72fb874d6e77c4ef5b7"></a> enumerator BK\_AVRCP\_PT\_CMD\_FAST\_FORWARD
    :   fast forward

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t21BK_AVRCP_PT_CMD_EJECTE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t21BK_AVRCP_PT_CMD_EJECTE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t21BK_AVRCP_PT_CMD_EJECTE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a3819f5026b92ab980a1ccd3a4ef6e8de"></a> enumerator BK\_AVRCP\_PT\_CMD\_EJECT
    :   eject

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t23BK_AVRCP_PT_CMD_FORWARDE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t23BK_AVRCP_PT_CMD_FORWARDE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t23BK_AVRCP_PT_CMD_FORWARDE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a03a3364e715c7b50de594a2e18841bfd"></a> enumerator BK\_AVRCP\_PT\_CMD\_FORWARD
    :   forward

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t24BK_AVRCP_PT_CMD_BACKWARDE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t24BK_AVRCP_PT_CMD_BACKWARDE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t24BK_AVRCP_PT_CMD_BACKWARDE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a51dbedcf7abe4898f0b092d3bc9946d4"></a> enumerator BK\_AVRCP\_PT\_CMD\_BACKWARD
    :   backward

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t21BK_AVRCP_PT_CMD_ANGLEE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t21BK_AVRCP_PT_CMD_ANGLEE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t21BK_AVRCP_PT_CMD_ANGLEE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a2bc359a7fb33172fdaf9bdd287a5b0f9"></a> enumerator BK\_AVRCP\_PT\_CMD\_ANGLE
    :   angle

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t23BK_AVRCP_PT_CMD_SUBPICTE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t23BK_AVRCP_PT_CMD_SUBPICTE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t23BK_AVRCP_PT_CMD_SUBPICTE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a79a9940b3ff2277c6b5f9de4aab51dfd"></a> enumerator BK\_AVRCP\_PT\_CMD\_SUBPICT
    :   subpicture

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t18BK_AVRCP_PT_CMD_F1E"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t18BK_AVRCP_PT_CMD_F1E"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t18BK_AVRCP_PT_CMD_F1E"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701ac2acfbe7b471e25ab3b61b6b472deb29"></a> enumerator BK\_AVRCP\_PT\_CMD\_F1
    :   F1

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t18BK_AVRCP_PT_CMD_F2E"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t18BK_AVRCP_PT_CMD_F2E"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t18BK_AVRCP_PT_CMD_F2E"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a69244e76bc7df5da599d774796b3ba35"></a> enumerator BK\_AVRCP\_PT\_CMD\_F2
    :   F2

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t18BK_AVRCP_PT_CMD_F3E"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t18BK_AVRCP_PT_CMD_F3E"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t18BK_AVRCP_PT_CMD_F3E"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a6bc408b354e1b82ca21ac9732a540d38"></a> enumerator BK\_AVRCP\_PT\_CMD\_F3
    :   F3

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t18BK_AVRCP_PT_CMD_F4E"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t18BK_AVRCP_PT_CMD_F4E"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t18BK_AVRCP_PT_CMD_F4E"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701a9df2a81304fa45d4364bbb1ac24624d3"></a> enumerator BK\_AVRCP\_PT\_CMD\_F4
    :   F4

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t18BK_AVRCP_PT_CMD_F5E"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t18BK_AVRCP_PT_CMD_F5E"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t18BK_AVRCP_PT_CMD_F5E"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701acdbe88ffc728ec79cf2adbe4076706ae"></a> enumerator BK\_AVRCP\_PT\_CMD\_F5
    :   F5

    <a id="_CPPv4N17bk_avrcp_pt_cmd_t22BK_AVRCP_PT_CMD_VENDORE"></a>

    <a id="_CPPv3N17bk_avrcp_pt_cmd_t22BK_AVRCP_PT_CMD_VENDORE"></a> <a id="_CPPv2N17bk_avrcp_pt_cmd_t22BK_AVRCP_PT_CMD_VENDORE"></a> <a id="dm__bt__types_8h_1ae780de89845d9801b3ec7fd06bc5d701ab10e5cbf2f3e313508f9376638d838c4"></a> enumerator BK\_AVRCP\_PT\_CMD\_VENDOR
    :   vendor unique

<a id="_CPPv423bk_avrcp_pt_cmd_state_t"></a>

<a id="_CPPv323bk_avrcp_pt_cmd_state_t"></a> <a id="_CPPv223bk_avrcp_pt_cmd_state_t"></a> <a id="dm__bt__types_8h_1ab0f385b4e01d0e06e8692d98d163729a"></a> enum bk\_avrcp\_pt\_cmd\_state\_t
:   AVRCP passthrough command state.

    *Values:*

    <a id="_CPPv4N23bk_avrcp_pt_cmd_state_t29BK_AVRCP_PT_CMD_STATE_PRESSEDE"></a>

    <a id="_CPPv3N23bk_avrcp_pt_cmd_state_t29BK_AVRCP_PT_CMD_STATE_PRESSEDE"></a> <a id="_CPPv2N23bk_avrcp_pt_cmd_state_t29BK_AVRCP_PT_CMD_STATE_PRESSEDE"></a> <a id="dm__bt__types_8h_1ab0f385b4e01d0e06e8692d98d163729aa7a75b1f2754e0f7f98837b8ac4f50efe"></a> enumerator BK\_AVRCP\_PT\_CMD\_STATE\_PRESSED
    :   key pressed

    <a id="_CPPv4N23bk_avrcp_pt_cmd_state_t30BK_AVRCP_PT_CMD_STATE_RELEASEDE"></a>

    <a id="_CPPv3N23bk_avrcp_pt_cmd_state_t30BK_AVRCP_PT_CMD_STATE_RELEASEDE"></a> <a id="_CPPv2N23bk_avrcp_pt_cmd_state_t30BK_AVRCP_PT_CMD_STATE_RELEASEDE"></a> <a id="dm__bt__types_8h_1ab0f385b4e01d0e06e8692d98d163729aa8172ad7165b28713f66a1ddab8ef336b"></a> enumerator BK\_AVRCP\_PT\_CMD\_STATE\_RELEASED
    :   key released

<a id="_CPPv417bk_avrcp_rn_rsp_t"></a>

<a id="_CPPv317bk_avrcp_rn_rsp_t"></a> <a id="_CPPv217bk_avrcp_rn_rsp_t"></a> <a id="dm__bt__types_8h_1ab7c0f64f7d22a9a5fafaa97504ff506f"></a> enum bk\_avrcp\_rn\_rsp\_t
:   AVRC notification response type.

    *Values:*

    <a id="_CPPv4N17bk_avrcp_rn_rsp_t23BK_AVRCP_RN_RSP_INTERIME"></a>

    <a id="_CPPv3N17bk_avrcp_rn_rsp_t23BK_AVRCP_RN_RSP_INTERIME"></a> <a id="_CPPv2N17bk_avrcp_rn_rsp_t23BK_AVRCP_RN_RSP_INTERIME"></a> <a id="dm__bt__types_8h_1ab7c0f64f7d22a9a5fafaa97504ff506faf1dcfc252d41628de9a97e371d5cc98c"></a> enumerator BK\_AVRCP\_RN\_RSP\_INTERIM
    :   initial response to RegisterNotification, should be sent T\_mtp(1000ms) from receiving the command

    <a id="_CPPv4N17bk_avrcp_rn_rsp_t23BK_AVRCP_RN_RSP_CHANGEDE"></a>

    <a id="_CPPv3N17bk_avrcp_rn_rsp_t23BK_AVRCP_RN_RSP_CHANGEDE"></a> <a id="_CPPv2N17bk_avrcp_rn_rsp_t23BK_AVRCP_RN_RSP_CHANGEDE"></a> <a id="dm__bt__types_8h_1ab7c0f64f7d22a9a5fafaa97504ff506fade53ae52535d1f417ab7bddb737b9105"></a> enumerator BK\_AVRCP\_RN\_RSP\_CHANGED
    :   final response to RegisterNotification command

<a id="_CPPv428bk_avrcp_rn_cap_api_method_t"></a>

<a id="_CPPv328bk_avrcp_rn_cap_api_method_t"></a> <a id="_CPPv228bk_avrcp_rn_cap_api_method_t"></a> <a id="dm__bt__types_8h_1aa3ecceff152dd8c74f3557f0adb1b920"></a> enum bk\_avrcp\_rn\_cap\_api\_method\_t
:   AVRC target notification event notification capability.

    *Values:*

    <a id="_CPPv4N28bk_avrcp_rn_cap_api_method_t34BK_AVRCP_RN_CAP_API_METHOD_ALLOWEDE"></a>

    <a id="_CPPv3N28bk_avrcp_rn_cap_api_method_t34BK_AVRCP_RN_CAP_API_METHOD_ALLOWEDE"></a> <a id="_CPPv2N28bk_avrcp_rn_cap_api_method_t34BK_AVRCP_RN_CAP_API_METHOD_ALLOWEDE"></a> <a id="dm__bt__types_8h_1aa3ecceff152dd8c74f3557f0adb1b920a2316f7e38e5c29879fda3f80bf4de736"></a> enumerator BK\_AVRCP\_RN\_CAP\_API\_METHOD\_ALLOWED
    :   all of the notification events that can possibly be supported, immutable

    <a id="_CPPv4N28bk_avrcp_rn_cap_api_method_t41BK_AVRCP_RN_CAP_API_METHOD_CURRENT_ENABLEE"></a>

    <a id="_CPPv3N28bk_avrcp_rn_cap_api_method_t41BK_AVRCP_RN_CAP_API_METHOD_CURRENT_ENABLEE"></a> <a id="_CPPv2N28bk_avrcp_rn_cap_api_method_t41BK_AVRCP_RN_CAP_API_METHOD_CURRENT_ENABLEE"></a> <a id="dm__bt__types_8h_1aa3ecceff152dd8c74f3557f0adb1b920a484109cf5cecbf3f4b5bd075fddbddb2"></a> enumerator BK\_AVRCP\_RN\_CAP\_API\_METHOD\_CURRENT\_ENABLE
    :   notification events selectively supported according to the current configuration

    <a id="_CPPv4N28bk_avrcp_rn_cap_api_method_t30BK_AVRCP_RN_CAP_API_METHOD_MAXE"></a>

    <a id="_CPPv3N28bk_avrcp_rn_cap_api_method_t30BK_AVRCP_RN_CAP_API_METHOD_MAXE"></a> <a id="_CPPv2N28bk_avrcp_rn_cap_api_method_t30BK_AVRCP_RN_CAP_API_METHOD_MAXE"></a> <a id="dm__bt__types_8h_1aa3ecceff152dd8c74f3557f0adb1b920ac9c9146dd1915fb28eea587b348a8d0e"></a> enumerator BK\_AVRCP\_RN\_CAP\_API\_METHOD\_MAX

<a id="_CPPv422bk_avrcp_tg_cb_event_t"></a>

<a id="_CPPv322bk_avrcp_tg_cb_event_t"></a> <a id="_CPPv222bk_avrcp_tg_cb_event_t"></a> <a id="dm__bt__types_8h_1a2160c8551d6b6e170804ad1c5519af3f"></a> enum bk\_avrcp\_tg\_cb\_event\_t
:   AVRC Target callback events.

    *Values:*

    <a id="_CPPv4N22bk_avrcp_tg_cb_event_t32BK_AVRCP_TG_CONNECTION_STATE_EVTE"></a>

    <a id="_CPPv3N22bk_avrcp_tg_cb_event_t32BK_AVRCP_TG_CONNECTION_STATE_EVTE"></a> <a id="_CPPv2N22bk_avrcp_tg_cb_event_t32BK_AVRCP_TG_CONNECTION_STATE_EVTE"></a> <a id="dm__bt__types_8h_1a2160c8551d6b6e170804ad1c5519af3fa4be15d462ea5dd7ac237cbae299aff94"></a> enumerator BK\_AVRCP\_TG\_CONNECTION\_STATE\_EVT
    :   connection state changed event

    <a id="_CPPv4N22bk_avrcp_tg_cb_event_t31BK_AVRCP_TG_PASSTHROUGH_CMD_EVTE"></a>

    <a id="_CPPv3N22bk_avrcp_tg_cb_event_t31BK_AVRCP_TG_PASSTHROUGH_CMD_EVTE"></a> <a id="_CPPv2N22bk_avrcp_tg_cb_event_t31BK_AVRCP_TG_PASSTHROUGH_CMD_EVTE"></a> <a id="dm__bt__types_8h_1a2160c8551d6b6e170804ad1c5519af3fa4bdd7e7400a67c99d665a8948b9780d1"></a> enumerator BK\_AVRCP\_TG\_PASSTHROUGH\_CMD\_EVT
    :   passthrough command event

    <a id="_CPPv4N22bk_avrcp_tg_cb_event_t39BK_AVRCP_TG_SET_ABSOLUTE_VOLUME_CMD_EVTE"></a>

    <a id="_CPPv3N22bk_avrcp_tg_cb_event_t39BK_AVRCP_TG_SET_ABSOLUTE_VOLUME_CMD_EVTE"></a> <a id="_CPPv2N22bk_avrcp_tg_cb_event_t39BK_AVRCP_TG_SET_ABSOLUTE_VOLUME_CMD_EVTE"></a> <a id="dm__bt__types_8h_1a2160c8551d6b6e170804ad1c5519af3fa1ad017746605324004027f2bdf7bc816"></a> enumerator BK\_AVRCP\_TG\_SET\_ABSOLUTE\_VOLUME\_CMD\_EVT
    :   set absolute volume command from remote device

    <a id="_CPPv4N22bk_avrcp_tg_cb_event_t37BK_AVRCP_TG_REGISTER_NOTIFICATION_EVTE"></a>

    <a id="_CPPv3N22bk_avrcp_tg_cb_event_t37BK_AVRCP_TG_REGISTER_NOTIFICATION_EVTE"></a> <a id="_CPPv2N22bk_avrcp_tg_cb_event_t37BK_AVRCP_TG_REGISTER_NOTIFICATION_EVTE"></a> <a id="dm__bt__types_8h_1a2160c8551d6b6e170804ad1c5519af3fa4f23fb048f10f19a725f01987ea278a3"></a> enumerator BK\_AVRCP\_TG\_REGISTER\_NOTIFICATION\_EVT
    :   register notification event

<a id="_CPPv417bk_spp_cb_event_t"></a>

<a id="_CPPv317bk_spp_cb_event_t"></a> <a id="_CPPv217bk_spp_cb_event_t"></a> <a id="dm__bt__types_8h_1a7aa13b1881d3faf735781da65d4f884d"></a> enum bk\_spp\_cb\_event\_t
:   SPP Callback Event Types.

    *Values:*

    <a id="_CPPv4N17bk_spp_cb_event_t15BK_SPP_NO_EVENTE"></a>

    <a id="_CPPv3N17bk_spp_cb_event_t15BK_SPP_NO_EVENTE"></a> <a id="_CPPv2N17bk_spp_cb_event_t15BK_SPP_NO_EVENTE"></a> <a id="dm__bt__types_8h_1a7aa13b1881d3faf735781da65d4f884da52f323ef77e785bb72018a75aaa99ce6"></a> enumerator BK\_SPP\_NO\_EVENT
    :   spp no event

    <a id="_CPPv4N17bk_spp_cb_event_t18BK_SPP_CONNECT_CNFE"></a>

    <a id="_CPPv3N17bk_spp_cb_event_t18BK_SPP_CONNECT_CNFE"></a> <a id="_CPPv2N17bk_spp_cb_event_t18BK_SPP_CONNECT_CNFE"></a> <a id="dm__bt__types_8h_1a7aa13b1881d3faf735781da65d4f884dadd11057b4c7f2e632df0ecd4e275ef38"></a> enumerator BK\_SPP\_CONNECT\_CNF
    :   spp connect confirm event

    <a id="_CPPv4N17bk_spp_cb_event_t18BK_SPP_CONNECT_INDE"></a>

    <a id="_CPPv3N17bk_spp_cb_event_t18BK_SPP_CONNECT_INDE"></a> <a id="_CPPv2N17bk_spp_cb_event_t18BK_SPP_CONNECT_INDE"></a> <a id="dm__bt__types_8h_1a7aa13b1881d3faf735781da65d4f884dafc63e14ba935c36517218cc199045dc3"></a> enumerator BK\_SPP\_CONNECT\_IND
    :   spp connect request ind event

    <a id="_CPPv4N17bk_spp_cb_event_t21BK_SPP_DISCONNECT_CNFE"></a>

    <a id="_CPPv3N17bk_spp_cb_event_t21BK_SPP_DISCONNECT_CNFE"></a> <a id="_CPPv2N17bk_spp_cb_event_t21BK_SPP_DISCONNECT_CNFE"></a> <a id="dm__bt__types_8h_1a7aa13b1881d3faf735781da65d4f884da5cf0c3d9f8f4850b018ee969299a63c4"></a> enumerator BK\_SPP\_DISCONNECT\_CNF
    :   spp disconnect confirm event

    <a id="_CPPv4N17bk_spp_cb_event_t21BK_SPP_DISCONNECT_INDE"></a>

    <a id="_CPPv3N17bk_spp_cb_event_t21BK_SPP_DISCONNECT_INDE"></a> <a id="_CPPv2N17bk_spp_cb_event_t21BK_SPP_DISCONNECT_INDE"></a> <a id="dm__bt__types_8h_1a7aa13b1881d3faf735781da65d4f884da6b1babe99e893034efa9460f1b2c2e8a"></a> enumerator BK\_SPP\_DISCONNECT\_IND
    :   spp disconnect request ind event

    <a id="_CPPv4N17bk_spp_cb_event_t15BK_SPP_STOP_CNFE"></a>

    <a id="_CPPv3N17bk_spp_cb_event_t15BK_SPP_STOP_CNFE"></a> <a id="_CPPv2N17bk_spp_cb_event_t15BK_SPP_STOP_CNFE"></a> <a id="dm__bt__types_8h_1a7aa13b1881d3faf735781da65d4f884daee777cbb8fc2ea6aad3be8e60a89dc12"></a> enumerator BK\_SPP\_STOP\_CNF
    :   spp server stop confirm event

    <a id="_CPPv4N17bk_spp_cb_event_t15BK_SPP_SEND_CNFE"></a>

    <a id="_CPPv3N17bk_spp_cb_event_t15BK_SPP_SEND_CNFE"></a> <a id="_CPPv2N17bk_spp_cb_event_t15BK_SPP_SEND_CNFE"></a> <a id="dm__bt__types_8h_1a7aa13b1881d3faf735781da65d4f884da862cd93f15d84ef87bde5e42cacb1bc9"></a> enumerator BK\_SPP\_SEND\_CNF
    :   spp send data confirm event

    <a id="_CPPv4N17bk_spp_cb_event_t21BK_SPP_RECVD_DATA_INDE"></a>

    <a id="_CPPv3N17bk_spp_cb_event_t21BK_SPP_RECVD_DATA_INDE"></a> <a id="_CPPv2N17bk_spp_cb_event_t21BK_SPP_RECVD_DATA_INDE"></a> <a id="dm__bt__types_8h_1a7aa13b1881d3faf735781da65d4f884da06f544a69c159fd389b38bd8b29ee9fe"></a> enumerator BK\_SPP\_RECVD\_DATA\_IND
    :   spp receive data ind event
