---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/common/app_env/app_env.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="enviorment-application-functions"></a>

# Enviorment Application Functions

<a id="app-env-api-brief"></a>

## APP\_ENV API Brief

| Application | Brief |
| --- | --- |
| [`app_env_get_ptr()`](#_CPPv415app_env_get_ptrv "app_env_get_ptr") | application: get app\_env variable address |
| [`app_env_get_pin_num()`](#_CPPv419app_env_get_pin_num8uint32_t "app_env_get_pin_num") | application: get GPIO pin number member from app\_env variable |
| [`app_env_get_pin_enable()`](#_CPPv422app_env_get_pin_enable8uint32_t "app_env_get_pin_enable") | application : get GPIO pin enable member from app\_env variable |
| [`app_env_get_pin_valid_level()`](#_CPPv427app_env_get_pin_valid_level8uint32_t "app_env_get_pin_valid_level") | application: get GPIO pin valid\_level member from app\_env variable |
| [`app_env_check_bt_mode()`](#_CPPv421app_env_check_bt_mode9bt_mode_t "app_env_check_bt_mode") | application: check toolkit bt mode feature setting |
| [`app_env_check_feature_flag()`](#_CPPv426app_env_check_feature_flag19app_env_feat_flag_t "app_env_check_feature_flag") | application: Check the features set by toolkit. |
| [`app_env_check_bat_display()`](#_CPPv425app_env_check_bat_displayv "app_env_check_bat_display") | application: Check the battery level display setting of bt\_flag set by toolkit. |
| [`app_env_get_dev_bt_name()`](#_CPPv423app_env_get_dev_bt_namev "app_env_get_dev_bt_name") | application: get bluetooth device name from app\_env variable |
| [`app_env_get_dev_bt_addr()`](#_CPPv423app_env_get_dev_bt_addrv "app_env_get_dev_bt_addr") | application: get bluetooth address from app\_env variable |
| [`app_env_get_tws_addr()`](#_CPPv420app_env_get_tws_addrv "app_env_get_tws_addr") | application: get tws bluetooth address from env\_data |
| [`app_env_get_dev_ble_addr()`](#_CPPv424app_env_get_dev_ble_addrv "app_env_get_dev_ble_addr") | application: get tws bluetooth address from env\_data |
| [`app_env_get_tx_pwr_lvl()`](#_CPPv422app_env_get_tx_pwr_lvlv "app_env_get_tx_pwr_lvl") | application: get RF tx power level from app\_env variable of Toolkit setting |
| [`app_env_get_connect_profile()`](#_CPPv427app_env_get_connect_profilev "app_env_get_connect_profile") | application: get support profile info from app\_env variable of Toolkit setting |
| [`app_env_get_mos_soft_power_flag()`](#_CPPv431app_env_get_mos_soft_power_flagv "app_env_get_mos_soft_power_flag") | application: get power key type from app\_env variable of Toolkit setting |
| [`app_env_get_sw_pwr_on_key_time()`](#_CPPv430app_env_get_sw_pwr_on_key_timev "app_env_get_sw_pwr_on_key_time") | application: get software power on key time length from app\_env variable of Toolkit setting |
| [`app_env_get_enter_pairing_key_time()`](#_CPPv434app_env_get_enter_pairing_key_timev "app_env_get_enter_pairing_key_time") | application: get enter pairing key time length from app\_env variable of Toolkit setting |
| [`app_env_data_find_bt_dev_record()`](#_CPPv431app_env_data_find_bt_dev_recordPK14btif_bd_addr_tPP18btif_bt_dev_info_t "app_env_data_find_bt_dev_record") | application: get bluetooth data record include bluetooth addrss,link key …,@btif\_bt\_dev\_info\_t |
| [`app_env_data_print_bt_record()`](#_CPPv428app_env_data_print_bt_recordv "app_env_data_print_bt_record") | application: output bluetooth data record data to uart,@btif\_bt\_dev\_info\_t |
| [`app_env_data_get_bt_conn_lk()`](#_CPPv427app_env_data_get_bt_conn_lkP14btif_bd_addr_tP9btif_lk_t "app_env_data_get_bt_conn_lk") | application: get link key by bluetooth address |
| [`app_env_data_add_bt_conn_lk()`](#_CPPv427app_env_data_add_bt_conn_lkP14btif_bd_addr_tP9btif_lk_t18if_link_key_type_t "app_env_data_add_bt_conn_lk") | application: add link key by bluetooth address to bt record |
| [`app_env_data_get_bt_last_two_record()`](#_CPPv435app_env_data_get_bt_last_two_recordP18btif_bt_dev_info_tP18btif_bt_dev_info_t "app_env_data_get_bt_last_two_record") | application: get bluetooth data record\[0\] and recode\[1\] include bluetooth addrss,link key …,@btif\_bt\_dev\_info\_t |
| [`app_env_data_find_ble_dev_record()`](#_CPPv432app_env_data_find_ble_dev_recordPK14btif_bd_addr_tPP19btif_ble_dev_info_t "app_env_data_find_ble_dev_record") | app\_env\_data\_find\_ble\_dev\_record brief description |
| [`app_env_data_add_or_update_ble_record()`](#_CPPv437app_env_data_add_or_update_ble_recordPK19btif_ble_dev_info_t "app_env_data_add_or_update_ble_record") | app\_env\_data\_add\_or\_update\_ble\_record brief description |
| [`app_env_data_flush()`](#_CPPv418app_env_data_flushv "app_env_data_flush") | app\_env\_data\_flush brief description |
| [`app_env_init()`](#_CPPv412app_env_initv "app_env_init") | app\_env\_init brief description |
| [`app_env_deinit()`](#_CPPv414app_env_deinitv "app_env_deinit") | app\_env\_deinit brief description |
| [`app_env_register_lk_handle()`](#_CPPv426app_env_register_lk_handlev "app_env_register_lk_handle") | app\_env\_register\_lk\_handle brief description |
| [`app_env_register_le_lk_handle()`](#_CPPv429app_env_register_le_lk_handlev "app_env_register_le_lk_handle") | app\_env\_register\_le\_lk\_handle brief description |
| [`app_env_save_charger_info()`](#_CPPv425app_env_save_charger_infoP14charger_info_t "app_env_save_charger_info") | app\_env\_save\_charger\_info brief description |
| [`app_env_reset_charger_info()`](#_CPPv426app_env_reset_charger_infov "app_env_reset_charger_info") | app\_env\_reset\_charger\_info brief description |
| [`app_get_ble_flag()`](#_CPPv416app_get_ble_flagv "app_get_ble_flag") | app\_get\_ble\_flag brief description |
| [`app_env_ble_init()`](#_CPPv416app_env_ble_initv "app_env_ble_init") | app\_env\_ble\_init brief description |
| [`app_get_ble_adv_interval()`](#_CPPv424app_get_ble_adv_intervalv "app_get_ble_adv_interval") | app\_get\_ble\_adv\_interval brief description |
| [`app_get_ble_conn_update_delay_time()`](#_CPPv434app_get_ble_conn_update_delay_timev "app_get_ble_conn_update_delay_time") | app\_get\_ble\_conn\_update\_delay\_time brief description |
| [`app_env_get_dev_ble_name()`](#_CPPv424app_env_get_dev_ble_namev "app_env_get_dev_ble_name") | app\_env\_get\_dev\_ble\_name brief description |
| [`app_env_get_dev_ble_name_len()`](#_CPPv428app_env_get_dev_ble_name_lenv "app_env_get_dev_ble_name_len") | app\_env\_get\_dev\_ble\_name\_len brief description |
| [`app_get_ble_conn_interval_min()`](#_CPPv429app_get_ble_conn_interval_minv "app_get_ble_conn_interval_min") | app\_get\_ble\_conn\_interval\_min brief description |
| [`app_get_ble_conn_interval_max()`](#_CPPv429app_get_ble_conn_interval_maxv "app_get_ble_conn_interval_max") | app\_get\_ble\_conn\_interval\_max brief description |
| [`app_env_get_dev_csip_sirk()`](#_CPPv425app_env_get_dev_csip_sirkv "app_env_get_dev_csip_sirk") | app\_env\_get\_dev\_csip\_sirk brief description |
| [`get_pref_max_transport_latency()`](#_CPPv430get_pref_max_transport_latencyv "get_pref_max_transport_latency") | get\_pref\_max\_transport\_latency brief description |
| [`get_pref_presentation_delay_min()`](#_CPPv431get_pref_presentation_delay_minv "get_pref_presentation_delay_min") | get\_pref\_presentation\_delay\_min brief description |
| [`get_pref_presentation_delay_max()`](#_CPPv431get_pref_presentation_delay_maxv "get_pref_presentation_delay_max") | get\_pref\_presentation\_delay\_max brief description |
| [`get_supp_presentation_delay_max()`](#_CPPv431get_supp_presentation_delay_maxv "get_supp_presentation_delay_max") | get\_supp\_presentation\_delay\_max brief description |
| [`get_supp_presentation_delay_min()`](#_CPPv431get_supp_presentation_delay_minv "get_supp_presentation_delay_min") | get\_supp\_presentation\_delay\_min brief description |
| [`app_env_data_reset()`](#_CPPv418app_env_data_resetv "app_env_data_reset") | app\_env\_data\_reset brief description |
| [`app_env_cfg_is_tws_left()`](#_CPPv423app_env_cfg_is_tws_leftv "app_env_cfg_is_tws_left") | app\_env\_cfg\_is\_tws\_left brief description |
| [`app_env_cfg_is_tws_right_en()`](#_CPPv427app_env_cfg_is_tws_right_env "app_env_cfg_is_tws_right_en") | app\_env\_cfg\_is\_tws\_right\_en brief description |
| [`app_env_get_sleep_en()`](#_CPPv420app_env_get_sleep_env "app_env_get_sleep_en") | app\_env\_get\_sleep\_en brief description |
| [`app_env_save_assert_info()`](#_CPPv424app_env_save_assert_infoPKc8uint16_t8uint32_t8uint32_t8uint32_tP13asssert_ctx_t "app_env_save_assert_info") | app\_env\_save\_assert\_info brief description |
| [`app_env_reset_assert_info()`](#_CPPv425app_env_reset_assert_infov "app_env_reset_assert_info") | app\_env\_reset\_assert\_info brief description |
| [`app_env_get_log_level()`](#_CPPv421app_env_get_log_levelv "app_env_get_log_level") | app\_env\_get\_log\_level brief description |
| [`app_env_set_tws_addr()`](#_CPPv420app_env_set_tws_addrP7uint8_t "app_env_set_tws_addr") | app\_env\_set\_tws\_addr brief description |
| [`app_env_set_dev_bt_name()`](#_CPPv423app_env_set_dev_bt_nameP7uint8_t7uint8_t "app_env_set_dev_bt_name") | app\_env\_set\_dev\_bt\_name brief description |
| [`app_env_set_bt_calib_result()`](#_CPPv427app_env_set_bt_calib_result7uint8_t "app_env_set_bt_calib_result") | app\_env\_set\_bt\_calib\_result brief description |
| [`app_env_get_bt_calib_result()`](#_CPPv427app_env_get_bt_calib_resultv "app_env_get_bt_calib_result") | app\_env\_get\_bt\_calib\_result brief description |
| [`app_env_data_get_bt_record_ptr()`](#_CPPv430app_env_data_get_bt_record_ptrP14btif_bd_addr_tPP18btif_bt_dev_info_t "app_env_data_get_bt_record_ptr") | app\_env\_data\_get\_bt\_record\_ptr brief description |
| [`app_env_cfg_is_free_pairing_enable()`](#_CPPv434app_env_cfg_is_free_pairing_enablev "app_env_cfg_is_free_pairing_enable") | app\_env\_cfg\_is\_free\_pairing\_enable brief description |
| [`app_env_cfg_is_power_on_reconnect_en()`](#_CPPv436app_env_cfg_is_power_on_reconnect_env "app_env_cfg_is_power_on_reconnect_en") | app\_env\_cfg\_is\_power\_on\_reconnect\_en brief description |
| [`app_env_cfg_get_le_addr_type()`](#_CPPv428app_env_cfg_get_le_addr_typev "app_env_cfg_get_le_addr_type") | app\_env\_cfg\_get\_le\_addr\_type brief description |

<a id="app-env-api-reference"></a>

## APP\_ENV API Reference

<a id="header-file"></a>

### Header File

- [common/app\_env/app\_env.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/common/app_env/app_env.h)

<a id="functions"></a>

### Functions

<a id="_CPPv415app_env_get_ptrv"></a>

<a id="_CPPv315app_env_get_ptrv"></a> <a id="_CPPv215app_env_get_ptrv"></a> <a id="app_env_get_ptr__void"></a> <a id="app__env_8h_1a4b03e9941af237dcf5055348f52eccf3"></a> [app\_env\_t](#_CPPv49app_env_t "app_env_t") \*app\_env\_get\_ptr(void)
:   application: get app\_env variable address

    返回:
    :   app\_env\_t\* [app\_env\_t](#structapp__env__t) type pointer

<a id="_CPPv419app_env_get_pin_num8uint32_t"></a>

<a id="_CPPv319app_env_get_pin_num8uint32_t"></a> <a id="_CPPv219app_env_get_pin_num8uint32_t"></a> <a id="app_env_get_pin_num__uint32_t"></a> <a id="app__env_8h_1ae7a9142ce29767b9f43362a0fe173e23"></a> uint32\_t app\_env\_get\_pin\_num(uint32\_t pin\_type)
:   application: get GPIO pin number member from app\_env variable

    参数:
    :   **pin\_type** – **\[in\]** type of pin(example PIN\_pwrBtn power button),gpio special usage

    返回:
    :   pin number

<a id="_CPPv422app_env_get_pin_enable8uint32_t"></a>

<a id="_CPPv322app_env_get_pin_enable8uint32_t"></a> <a id="_CPPv222app_env_get_pin_enable8uint32_t"></a> <a id="app_env_get_pin_enable__uint32_t"></a> <a id="app__env_8h_1ae4240446ae03dff6907b2d34aea7e6d4"></a> uint32\_t app\_env\_get\_pin\_enable(uint32\_t pin\_type)
:   application : get GPIO pin enable member from app\_env variable

    参数:
    :   **pin\_type** – **\[in\]** type of pin(example PIN\_pwrBtn power button),gpio special usage

    返回值:
    :   - **true** – enable
        - **false** – disable

    返回:
    :   pin enable or not

<a id="_CPPv427app_env_get_pin_valid_level8uint32_t"></a>

<a id="_CPPv327app_env_get_pin_valid_level8uint32_t"></a> <a id="_CPPv227app_env_get_pin_valid_level8uint32_t"></a> <a id="app_env_get_pin_valid_level__uint32_t"></a> <a id="app__env_8h_1ab18e907829a2c2ac60dbadff8570aba3"></a> uint32\_t app\_env\_get\_pin\_valid\_level(uint32\_t pin\_type)
:   application: get GPIO pin valid\_level member from app\_env variable

    参数:
    :   **pin\_type** – **\[in\]** type of pin(example PIN\_pwrBtn power button),gpio special usage

    返回值:
    :   - **high** – active
        - **low** – active

    返回:
    :   pin valid level

<a id="_CPPv421app_env_check_bt_mode9bt_mode_t"></a>

<a id="_CPPv321app_env_check_bt_mode9bt_mode_t"></a> <a id="_CPPv221app_env_check_bt_mode9bt_mode_t"></a> <a id="app_env_check_bt_mode__bt_mode_t"></a> <a id="app__env_8h_1a6f4731d0033ea998f47ac258c1edc53d"></a> uint32\_t app\_env\_check\_bt\_mode([bt\_mode\_t](#_CPPv49bt_mode_t "bt_mode_t") bt\_mode)
:   application: check toolkit bt mode feature setting

    参数:
    :   **bt\_mode** – **\[in\]** bluetooth link mode example(BT\_MODE\_1V2(one\_bring\_two),BT\_MODE\_1V1(one\_bring\_one))

    返回值:
    :   - **true** – is match input parameter
        - **false** – is not match input parameter

    返回:
    :   true or false

<a id="_CPPv426app_env_check_feature_flag19app_env_feat_flag_t"></a>

<a id="_CPPv326app_env_check_feature_flag19app_env_feat_flag_t"></a> <a id="_CPPv226app_env_check_feature_flag19app_env_feat_flag_t"></a> <a id="app_env_check_feature_flag__app_env_feat_flag_t"></a> <a id="app__env_8h_1aba2ad10af1e9c7d7dfb762433de9af83"></a> uint32\_t app\_env\_check\_feature\_flag([app\_env\_feat\_flag\_t](#_CPPv419app_env_feat_flag_t "app_env_feat_flag_t") flag)
:   application: Check the features set by toolkit.

    参数:
    :   **flag** – **\[in\]** is bit define variable detail,[app\_env\_feat\_flag\_t](#app__env_8h_1a39c7637219281ce19649e317f9709efd)

    返回值:
    :   - **true** – is match input parameter
        - **false** – is not match input parameter

    返回:
    :   true or false

<a id="_CPPv425app_env_check_bat_displayv"></a>

<a id="_CPPv325app_env_check_bat_displayv"></a> <a id="_CPPv225app_env_check_bat_displayv"></a> <a id="app_env_check_bat_display__void"></a> <a id="app__env_8h_1a171302231e65a65fe0402eec55ce7d71"></a> uint32\_t app\_env\_check\_bat\_display(void)
:   application: Check the battery level display setting of bt\_flag set by toolkit.

    返回值:
    :   - **true** – enable battery display
        - **false** – disable battery display

    返回:
    :   true or false

<a id="_CPPv423app_env_get_dev_bt_namev"></a>

<a id="_CPPv323app_env_get_dev_bt_namev"></a> <a id="_CPPv223app_env_get_dev_bt_namev"></a> <a id="app_env_get_dev_bt_name__void"></a> <a id="app__env_8h_1a5d34330b5eaca1c5f439ffaa91035de0"></a> char \*app\_env\_get\_dev\_bt\_name(void)
:   application: get bluetooth device name from app\_env variable

    返回:
    :   bluetooth device name character pointer variable

<a id="_CPPv423app_env_get_dev_bt_addrv"></a>

<a id="_CPPv323app_env_get_dev_bt_addrv"></a> <a id="_CPPv223app_env_get_dev_bt_addrv"></a> <a id="app_env_get_dev_bt_addr__void"></a> <a id="app__env_8h_1a6e6b81879f4480e58e2e308b674c39a1"></a> [btif\_bd\_addr\_t](../../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") app\_env\_get\_dev\_bt\_addr(void)
:   application: get bluetooth address from app\_env variable

    返回:
    :   bluetooth address(six bytes array)

<a id="_CPPv420app_env_get_tws_addrv"></a>

<a id="_CPPv320app_env_get_tws_addrv"></a> <a id="_CPPv220app_env_get_tws_addrv"></a> <a id="app_env_get_tws_addr__void"></a> <a id="app__env_8h_1a192be7bf39ab83b834f30c94c0c11386"></a> [btif\_bd\_addr\_t](../../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") app\_env\_get\_tws\_addr(void)
:   application: get tws bluetooth address from env\_data

    返回:
    :   bluetooth address(six bytes array)

<a id="_CPPv424app_env_get_dev_ble_addrv"></a>

<a id="_CPPv324app_env_get_dev_ble_addrv"></a> <a id="_CPPv224app_env_get_dev_ble_addrv"></a> <a id="app_env_get_dev_ble_addr__void"></a> <a id="app__env_8h_1a0a3c9f13205a01ff2043c72bcce5014b"></a> [btif\_bd\_addr\_t](../../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") app\_env\_get\_dev\_ble\_addr(void)
:   application: get tws bluetooth address from env\_data

    返回:
    :   bluetooth address(six bytes array)

<a id="_CPPv422app_env_get_tx_pwr_lvlv"></a>

<a id="_CPPv322app_env_get_tx_pwr_lvlv"></a> <a id="_CPPv222app_env_get_tx_pwr_lvlv"></a> <a id="app_env_get_tx_pwr_lvl__void"></a> <a id="app__env_8h_1a89803641022fe9ac960d90aab7ab09f0"></a> uint16\_t app\_env\_get\_tx\_pwr\_lvl(void)
:   application: get RF tx power level from app\_env variable of Toolkit setting

    返回:
    :   bluetooth address(six bytes array)

<a id="_CPPv427app_env_get_connect_profilev"></a>

<a id="_CPPv327app_env_get_connect_profilev"></a> <a id="_CPPv227app_env_get_connect_profilev"></a> <a id="app_env_get_connect_profile__void"></a> <a id="app__env_8h_1a92e72332fdcb129758b01474215aef9d"></a> uint32\_t app\_env\_get\_connect\_profile(void)
:   application: get support profile info from app\_env variable of Toolkit setting

    返回:
    :   connect\_profile [btif\_profile\_bitmap\_t](../../../btif/btif_type.md#btif__type_8h_1a7686100aea963f3a607732b92b69deb0)

<a id="_CPPv431app_env_get_mos_soft_power_flagv"></a>

<a id="_CPPv331app_env_get_mos_soft_power_flagv"></a> <a id="_CPPv231app_env_get_mos_soft_power_flagv"></a> <a id="app_env_get_mos_soft_power_flag__void"></a> <a id="app__env_8h_1a9cd467d6e7d3fd4d8c17bd66a8173914"></a> uint32\_t app\_env\_get\_mos\_soft\_power\_flag(void)
:   application: get power key type from app\_env variable of Toolkit setting

    返回:
    :   poweron\_mode power\_key\_type\_t

<a id="_CPPv430app_env_get_sw_pwr_on_key_timev"></a>

<a id="_CPPv330app_env_get_sw_pwr_on_key_timev"></a> <a id="_CPPv230app_env_get_sw_pwr_on_key_timev"></a> <a id="app_env_get_sw_pwr_on_key_time__void"></a> <a id="app__env_8h_1a910732ffcfcb118da4db001c783c76a4"></a> uint32\_t app\_env\_get\_sw\_pwr\_on\_key\_time(void)
:   application: get software power on key time length from app\_env variable of Toolkit setting

    返回:
    :   software power on key time unit(10ms)

<a id="_CPPv434app_env_get_enter_pairing_key_timev"></a>

<a id="_CPPv334app_env_get_enter_pairing_key_timev"></a> <a id="_CPPv234app_env_get_enter_pairing_key_timev"></a> <a id="app_env_get_enter_pairing_key_time__void"></a> <a id="app__env_8h_1ad0e43ea689dd47d8757b1cf83a109e72"></a> uint32\_t app\_env\_get\_enter\_pairing\_key\_time(void)
:   application: get enter pairing key time length from app\_env variable of Toolkit setting

    返回:
    :   software enter pairing key time unit(10ms)

<a id="_CPPv431app_env_data_find_bt_dev_recordPK14btif_bd_addr_tPP18btif_bt_dev_info_t"></a>

<a id="_CPPv331app_env_data_find_bt_dev_recordPK14btif_bd_addr_tPP18btif_bt_dev_info_t"></a> <a id="_CPPv231app_env_data_find_bt_dev_recordPK14btif_bd_addr_tPP18btif_bt_dev_info_t"></a> <a id="app_env_data_find_bt_dev_record__btif_bd_addr_tCP.btif_bt_dev_info_tPP"></a> <a id="app__env_8h_1a01b719b752527b94e9a9d02179d5ea64"></a> int32\_t app\_env\_data\_find\_bt\_dev\_record(const [btif\_bd\_addr\_t](../../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_bd\_addr, [btif\_bt\_dev\_info\_t](../../../btif/btif_type.md#_CPPv418btif_bt_dev_info_t "btif_bt_dev_info_t") \*\*p\_bt\_record)
:   application: get bluetooth data record include bluetooth addrss,link key …,@btif\_bt\_dev\_info\_t

    参数:
    :   **p\_bd\_addr** – **\[in\]** input bluetooth address(like mobile bluetooth address)

    Param :

<a id="_CPPv428app_env_data_print_bt_recordv"></a>

<a id="_CPPv328app_env_data_print_bt_recordv"></a> <a id="_CPPv228app_env_data_print_bt_recordv"></a> <a id="app_env_data_print_bt_record__void"></a> <a id="app__env_8h_1ad59fd102f0fc1b4ffb32909ec33a2256"></a> void app\_env\_data\_print\_bt\_record(void)
:   application: output bluetooth data record data to uart,@btif\_bt\_dev\_info\_t

    返回:
    :   N/A

<a id="_CPPv427app_env_data_get_bt_conn_lkP14btif_bd_addr_tP9btif_lk_t"></a>

<a id="_CPPv327app_env_data_get_bt_conn_lkP14btif_bd_addr_tP9btif_lk_t"></a> <a id="_CPPv227app_env_data_get_bt_conn_lkP14btif_bd_addr_tP9btif_lk_t"></a> <a id="app_env_data_get_bt_conn_lk__btif_bd_addr_tP.btif_lk_tP"></a> <a id="app__env_8h_1ae149e1be4d77fa91710dca4245d270e3"></a> int32\_t app\_env\_data\_get\_bt\_conn\_lk([btif\_bd\_addr\_t](../../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr, [btif\_lk\_t](../../../btif/btif_type.md#_CPPv49btif_lk_t "btif_lk_t") \*p\_lk)
:   application: get link key by bluetooth address

    参数:
    :   - **\*p\_addr** – **\[in\]** bluetooth address(Normally, the input address is the Bluetooth address of the mobile phone.),[btif\_bd\_addr\_t](../../../btif/btif_type.md#structbtif__bd__addr__t)
        - **\*p\_lk** – **\[out\]** bluetooth link key,@btif\_lk\_t

    返回值:
    :   - **BK\_RET\_OK** – found bluetooth link key from record
        - **BK\_RET\_FAIL** – found bluetooth link key from record

    返回:
    :   status

<a id="_CPPv427app_env_data_add_bt_conn_lkP14btif_bd_addr_tP9btif_lk_t18if_link_key_type_t"></a>

<a id="_CPPv327app_env_data_add_bt_conn_lkP14btif_bd_addr_tP9btif_lk_t18if_link_key_type_t"></a> <a id="_CPPv227app_env_data_add_bt_conn_lkP14btif_bd_addr_tP9btif_lk_t18if_link_key_type_t"></a> <a id="app_env_data_add_bt_conn_lk__btif_bd_addr_tP.btif_lk_tP.if_link_key_type_t"></a> <a id="app__env_8h_1ad76299f115afe582222ad66f006fafa4"></a> int32\_t app\_env\_data\_add\_bt\_conn\_lk([btif\_bd\_addr\_t](../../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_addr, [btif\_lk\_t](../../../btif/btif_type.md#_CPPv49btif_lk_t "btif_lk_t") \*p\_lk, [if\_link\_key\_type\_t](../../../btif/btif_type.md#_CPPv418if_link_key_type_t "if_link_key_type_t") lk\_type)
:   application: add link key by bluetooth address to bt record

    参数:
    :   - **\*p\_addr** – **\[in\]** bluetooth address(Normally, the input address is the Bluetooth address of the mobile phone.),[btif\_bd\_addr\_t](../../../btif/btif_type.md#structbtif__bd__addr__t)
        - **\*p\_lk** – **\[in\]** bluetooth link key,@btif\_lk\_t
        - **lk\_type** – **\[in\]** bluetooth link key type,@if\_link\_key\_type\_t

    返回值:
    :   - **BK\_RET\_OK** – add bluetooth link key to record
        - **BK\_RET\_FAIL** – add bluetooth link key to record

    返回:
    :   status

<a id="_CPPv435app_env_data_get_bt_last_two_recordP18btif_bt_dev_info_tP18btif_bt_dev_info_t"></a>

<a id="_CPPv335app_env_data_get_bt_last_two_recordP18btif_bt_dev_info_tP18btif_bt_dev_info_t"></a> <a id="_CPPv235app_env_data_get_bt_last_two_recordP18btif_bt_dev_info_tP18btif_bt_dev_info_t"></a> <a id="app_env_data_get_bt_last_two_record__btif_bt_dev_info_tP.btif_bt_dev_info_tP"></a> <a id="app__env_8h_1abbb9f7916c972d9567b6f3684657ae08"></a> uint8\_t app\_env\_data\_get\_bt\_last\_two\_record([btif\_bt\_dev\_info\_t](../../../btif/btif_type.md#_CPPv418btif_bt_dev_info_t "btif_bt_dev_info_t") \*p\_bt\_record1, [btif\_bt\_dev\_info\_t](../../../btif/btif_type.md#_CPPv418btif_bt_dev_info_t "btif_bt_dev_info_t") \*p\_bt\_record2)
:   application: get bluetooth data record\[0\] and recode\[1\] include bluetooth addrss,link key …,@btif\_bt\_dev\_info\_t

    参数:
    :   - **\*p\_addr** – **\[out\]** bluetooth address(Normally, the input address is the Bluetooth address of the mobile phone.),[btif\_bd\_addr\_t](../../../btif/btif_type.md#structbtif__bd__addr__t)
        - **\*p\_lk** – **\[out\]** bluetooth link key,@btif\_lk\_t
        - **lk\_type** – **\[in\]** bluetooth link key type,@if\_link\_key\_type\_t

    返回值:
    :   - **0** – no record
        - **1** – 1 record
        - **2** – 2 records

    返回:
    :   number of record

<a id="_CPPv432app_env_data_find_ble_dev_recordPK14btif_bd_addr_tPP19btif_ble_dev_info_t"></a>

<a id="_CPPv332app_env_data_find_ble_dev_recordPK14btif_bd_addr_tPP19btif_ble_dev_info_t"></a> <a id="_CPPv232app_env_data_find_ble_dev_recordPK14btif_bd_addr_tPP19btif_ble_dev_info_t"></a> <a id="app_env_data_find_ble_dev_record__btif_bd_addr_tCP.btif_ble_dev_info_tPP"></a> <a id="app__env_8h_1a1ea50896fcfbe6347b134a53b59e4d8f"></a> int32\_t app\_env\_data\_find\_ble\_dev\_record(const [btif\_bd\_addr\_t](../../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_bd\_addr, [btif\_ble\_dev\_info\_t](../../../btif/btif_type.md#_CPPv419btif_ble_dev_info_t "btif_ble_dev_info_t") \*\*p\_ble\_record)
:   app\_env\_data\_find\_ble\_dev\_record brief description

    find BLE device information by specified MAC address

    参数:
    :   - **p\_bd\_addr** – **\[in\]** MAC address
        - **p\_ble\_record** – **\[out\]** BLE device information

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv437app_env_data_add_or_update_ble_recordPK19btif_ble_dev_info_t"></a>

<a id="_CPPv337app_env_data_add_or_update_ble_recordPK19btif_ble_dev_info_t"></a> <a id="_CPPv237app_env_data_add_or_update_ble_recordPK19btif_ble_dev_info_t"></a> <a id="app_env_data_add_or_update_ble_record__btif_ble_dev_info_tCP"></a> <a id="app__env_8h_1a33ba284fde8a4fc765807c4d3bc29e4c"></a> int32\_t app\_env\_data\_add\_or\_update\_ble\_record(const [btif\_ble\_dev\_info\_t](../../../btif/btif_type.md#_CPPv419btif_ble_dev_info_t "btif_ble_dev_info_t") \*p\_ble\_record)
:   app\_env\_data\_add\_or\_update\_ble\_record brief description

    add or update BLE device information

    参数:
    :   **p\_ble\_record** –

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result

<a id="_CPPv418app_env_data_flushv"></a>

<a id="_CPPv318app_env_data_flushv"></a> <a id="_CPPv218app_env_data_flushv"></a> <a id="app_env_data_flush__void"></a> <a id="app__env_8h_1ac6a8b513b59afe963b8ed9ff69aee86e"></a> void app\_env\_data\_flush(void)
:   app\_env\_data\_flush brief description

    store system environment information to flash if needed

    返回:
    :   N/A

<a id="_CPPv412app_env_initv"></a>

<a id="_CPPv312app_env_initv"></a> <a id="_CPPv212app_env_initv"></a> <a id="app_env_init__void"></a> <a id="app__env_8h_1a4ff0bdff941429918c804e01bd7a13f9"></a> void app\_env\_init(void)
:   app\_env\_init brief description

    load system environment information and configre data from flash

    返回:
    :   N/A

<a id="_CPPv414app_env_deinitv"></a>

<a id="_CPPv314app_env_deinitv"></a> <a id="_CPPv214app_env_deinitv"></a> <a id="app_env_deinit__void"></a> <a id="app__env_8h_1a5a2ec694145f8c3c863b7c9283c748d4"></a> void app\_env\_deinit(void)
:   app\_env\_deinit brief description

    store load system environment information and configre data to flash if needed and release allocated data buffer for them

    返回:
    :   N/A

<a id="_CPPv426app_env_register_lk_handlev"></a>

<a id="_CPPv326app_env_register_lk_handlev"></a> <a id="_CPPv226app_env_register_lk_handlev"></a> <a id="app_env_register_lk_handle__void"></a> <a id="app__env_8h_1afb92053143f2c70357710fabb9ad6a76"></a> void app\_env\_register\_lk\_handle(void)
:   app\_env\_register\_lk\_handle brief description

    register BT link key relevant operation callback function to HCI

    返回:
    :   N/A

<a id="_CPPv429app_env_register_le_lk_handlev"></a>

<a id="_CPPv329app_env_register_le_lk_handlev"></a> <a id="_CPPv229app_env_register_le_lk_handlev"></a> <a id="app_env_register_le_lk_handle__void"></a> <a id="app__env_8h_1a4407ea5b36e12a6fc71cfd885da3ce0c"></a> void app\_env\_register\_le\_lk\_handle(void)
:   app\_env\_register\_le\_lk\_handle brief description

    register BLE link key relevant operation callback function to HCI

    返回:
    :   N/A

<a id="_CPPv425app_env_save_charger_infoP14charger_info_t"></a>

<a id="_CPPv325app_env_save_charger_infoP14charger_info_t"></a> <a id="_CPPv225app_env_save_charger_infoP14charger_info_t"></a> <a id="app_env_save_charger_info__charger_info_tP"></a> <a id="app__env_8h_1a0ebe3cefa30b85ac55118f95416e878d"></a> void app\_env\_save\_charger\_info([charger\_info\_t](#_CPPv414charger_info_t "charger_info_t") \*p\_change\_info)
:   app\_env\_save\_charger\_info brief description

    save charger information to system environment information

    参数:
    :   **p\_change\_info** – **\[in\]** change information for charger relevant data

    返回:
    :   N/A

<a id="_CPPv426app_env_reset_charger_infov"></a>

<a id="_CPPv326app_env_reset_charger_infov"></a> <a id="_CPPv226app_env_reset_charger_infov"></a> <a id="app_env_reset_charger_info__void"></a> <a id="app__env_8h_1a026a33e00ec73016b33501d9804f51da"></a> void app\_env\_reset\_charger\_info(void)
:   app\_env\_reset\_charger\_info brief description

    reset charger information

    返回:
    :   N/A

<a id="_CPPv416app_get_ble_flagv"></a>

<a id="_CPPv316app_get_ble_flagv"></a> <a id="_CPPv216app_get_ble_flagv"></a> <a id="app_get_ble_flag__void"></a> <a id="app__env_8h_1a4544640b645aebe3681289a374f65117"></a> uint16\_t app\_get\_ble\_flag(void)
:   app\_get\_ble\_flag brief description

    return BLE environment setting

    返回:
    :   BLE environment setting @app\_env\_le\_flag\_t

<a id="_CPPv416app_env_ble_initv"></a>

<a id="_CPPv316app_env_ble_initv"></a> <a id="_CPPv216app_env_ble_initv"></a> <a id="app_env_ble_init__void"></a> <a id="app__env_8h_1ae8f958f2b2510d599f17241eefe2958a"></a> void app\_env\_ble\_init(void)
:   app\_env\_ble\_init brief description

    initialize BLE relevant setting and send to HCI

    返回:
    :   N/A

<a id="_CPPv424app_get_ble_adv_intervalv"></a>

<a id="_CPPv324app_get_ble_adv_intervalv"></a> <a id="_CPPv224app_get_ble_adv_intervalv"></a> <a id="app_get_ble_adv_interval__void"></a> <a id="app__env_8h_1a28ce8736cd0805a8cce4b7bcc0181330"></a> uint16\_t app\_get\_ble\_adv\_interval(void)
:   app\_get\_ble\_adv\_interval brief description

    return BLE advertising interval

    返回值:
    :   - **DEFAULT\_ADV\_INT** – default interval
        - **other** – setting interval

    返回:
    :   interval

<a id="_CPPv434app_get_ble_conn_update_delay_timev"></a>

<a id="_CPPv334app_get_ble_conn_update_delay_timev"></a> <a id="_CPPv234app_get_ble_conn_update_delay_timev"></a> <a id="app_get_ble_conn_update_delay_time__void"></a> <a id="app__env_8h_1ace490b9dfce2357a2693e4724d6cb205"></a> uint16\_t app\_get\_ble\_conn\_update\_delay\_time(void)
:   app\_get\_ble\_conn\_update\_delay\_time brief description

    return connection update delay time

    返回值:
    :   - **DEFAULT\_CON\_UPDATE\_DELAY** – default value
        - **other** – setting value

    返回:
    :   delay time

<a id="_CPPv424app_env_get_dev_ble_namev"></a>

<a id="_CPPv324app_env_get_dev_ble_namev"></a> <a id="_CPPv224app_env_get_dev_ble_namev"></a> <a id="app_env_get_dev_ble_name__void"></a> <a id="app__env_8h_1ac7c4918df0065d1b3863e65c2d64fa72"></a> char \*app\_env\_get\_dev\_ble\_name(void)
:   app\_env\_get\_dev\_ble\_name brief description

    return BLE local name

    返回:
    :   pointer for BLE name data buffer

<a id="_CPPv428app_env_get_dev_ble_name_lenv"></a>

<a id="_CPPv328app_env_get_dev_ble_name_lenv"></a> <a id="_CPPv228app_env_get_dev_ble_name_lenv"></a> <a id="app_env_get_dev_ble_name_len__void"></a> <a id="app__env_8h_1aa9e345d787afcffbddf34dfbe9f872ea"></a> uint8\_t app\_env\_get\_dev\_ble\_name\_len(void)
:   app\_env\_get\_dev\_ble\_name\_len brief description

    return BLE local name length

    返回:
    :   length value

<a id="_CPPv429app_get_ble_conn_interval_minv"></a>

<a id="_CPPv329app_get_ble_conn_interval_minv"></a> <a id="_CPPv229app_get_ble_conn_interval_minv"></a> <a id="app_get_ble_conn_interval_min__void"></a> <a id="app__env_8h_1a595d00ed8f91694a1c5402a567892cb1"></a> uint16\_t app\_get\_ble\_conn\_interval\_min(void)
:   app\_get\_ble\_conn\_interval\_min brief description

    return min value of BLE connection interval

    返回值:
    :   - **DEFAULT\_CON\_UPDATE\_INTV** – default value
        - **other** – setting value

    返回:
    :   interval value

<a id="_CPPv429app_get_ble_conn_interval_maxv"></a>

<a id="_CPPv329app_get_ble_conn_interval_maxv"></a> <a id="_CPPv229app_get_ble_conn_interval_maxv"></a> <a id="app_get_ble_conn_interval_max__void"></a> <a id="app__env_8h_1aeaf5f773b77300cb87824d8d77963168"></a> uint16\_t app\_get\_ble\_conn\_interval\_max(void)
:   app\_get\_ble\_conn\_interval\_max brief description

    return max value of BLE connection interval

    返回值:
    :   - **DEFAULT\_CON\_UPDATE\_INTV** – default value
        - **other** – setting value

    返回:
    :   interval value

<a id="_CPPv425app_env_get_dev_csip_sirkv"></a>

<a id="_CPPv325app_env_get_dev_csip_sirkv"></a> <a id="_CPPv225app_env_get_dev_csip_sirkv"></a> <a id="app_env_get_dev_csip_sirk__void"></a> <a id="app__env_8h_1a16c6420cbfe27af7db3f7909db229c51"></a> uint8\_t \*app\_env\_get\_dev\_csip\_sirk(void)
:   app\_env\_get\_dev\_csip\_sirk brief description

    return csip sirk data

    返回值:
    :   - **NULL** – no enable LE audio
        - **other** – csip sirk data buffer

    返回:
    :   address

<a id="_CPPv430get_pref_max_transport_latencyv"></a>

<a id="_CPPv330get_pref_max_transport_latencyv"></a> <a id="_CPPv230get_pref_max_transport_latencyv"></a> <a id="get_pref_max_transport_latency__void"></a> <a id="app__env_8h_1a7f1b1e047767f756073249c5a8f87297"></a> uint16\_t get\_pref\_max\_transport\_latency(void)
:   get\_pref\_max\_transport\_latency brief description

    return max value of transport latency

    返回值:
    :   - **APPL\_GA\_PREF\_MAX\_TRANS\_LATENCY** – defalut value
        - **other** – setting value

    返回:
    :   latency value

<a id="_CPPv431get_pref_presentation_delay_minv"></a>

<a id="_CPPv331get_pref_presentation_delay_minv"></a> <a id="_CPPv231get_pref_presentation_delay_minv"></a> <a id="get_pref_presentation_delay_min__void"></a> <a id="app__env_8h_1a8bf38989eb106839e01f085cebce5d35"></a> uint32\_t get\_pref\_presentation\_delay\_min(void)
:   get\_pref\_presentation\_delay\_min brief description

    return min value of presentation delay

    返回值:
    :   - **APPL\_GA\_PREF\_PRESENTATION\_DELAY\_MIN** – default value
        - **other** – setting value

    返回:
    :   delay value

<a id="_CPPv431get_pref_presentation_delay_maxv"></a>

<a id="_CPPv331get_pref_presentation_delay_maxv"></a> <a id="_CPPv231get_pref_presentation_delay_maxv"></a> <a id="get_pref_presentation_delay_max__void"></a> <a id="app__env_8h_1a227ac3b7b46e249700ac566f4ee5d7ce"></a> uint32\_t get\_pref\_presentation\_delay\_max(void)
:   get\_pref\_presentation\_delay\_max brief description

    return max value of presentation delay

    返回值:
    :   - **APPL\_GA\_PREF\_PRESENTATION\_DELAY\_MAX** – default value
        - **other** – setting value

    返回:
    :   delay value

<a id="_CPPv431get_supp_presentation_delay_maxv"></a>

<a id="_CPPv331get_supp_presentation_delay_maxv"></a> <a id="_CPPv231get_supp_presentation_delay_maxv"></a> <a id="get_supp_presentation_delay_max__void"></a> <a id="app__env_8h_1a3b446ef266bfeedc705804ee3d8ee18e"></a> uint32\_t get\_supp\_presentation\_delay\_max(void)
:   get\_supp\_presentation\_delay\_max brief description

    return max value of supported delay

    返回值:
    :   - **APPL\_GA\_PREF\_PRESENTATION\_DELAY\_MAX** – default value
        - **other** – setting value

    返回:
    :   delay value

<a id="_CPPv431get_supp_presentation_delay_minv"></a>

<a id="_CPPv331get_supp_presentation_delay_minv"></a> <a id="_CPPv231get_supp_presentation_delay_minv"></a> <a id="get_supp_presentation_delay_min__void"></a> <a id="app__env_8h_1a890496a4358d7ffda978edd1c9626d7e"></a> uint32\_t get\_supp\_presentation\_delay\_min(void)
:   get\_supp\_presentation\_delay\_min brief description

    return min value of supported delay

    返回值:
    :   - **APPL\_GA\_PREF\_PRESENTATION\_DELAY\_MIN** – default value
        - **other** – setting value

    返回:
    :   delay value

<a id="_CPPv418app_env_data_resetv"></a>

<a id="_CPPv318app_env_data_resetv"></a> <a id="_CPPv218app_env_data_resetv"></a> <a id="app_env_data_reset__void"></a> <a id="app__env_8h_1a4f0b8aeec5eaabd83f72dd4f72d3ab7d"></a> void app\_env\_data\_reset(void)
:   app\_env\_data\_reset brief description

    reset system environment information, will call function app\_env\_data\_flush to write back to flash.

    返回:
    :   N/A

<a id="_CPPv423app_env_cfg_is_tws_leftv"></a>

<a id="_CPPv323app_env_cfg_is_tws_leftv"></a> <a id="_CPPv223app_env_cfg_is_tws_leftv"></a> <a id="app_env_cfg_is_tws_left__void"></a> <a id="app__env_8h_1ac51a5d3990ce2f77c033146937ec059b"></a> bool app\_env\_cfg\_is\_tws\_left(void)
:   app\_env\_cfg\_is\_tws\_left brief description

    return TWS position set by toolkit @APP\_ENV\_FEATURE\_FLAG\_TWS\_L

    返回值:
    :   - **true** – left
        - **false** – right

    返回:
    :   bool

<a id="_CPPv427app_env_cfg_is_tws_right_env"></a>

<a id="_CPPv327app_env_cfg_is_tws_right_env"></a> <a id="_CPPv227app_env_cfg_is_tws_right_env"></a> <a id="app_env_cfg_is_tws_right_en__void"></a> <a id="app__env_8h_1aef6055ce3ad9923747409ffb9b0db5b3"></a> bool app\_env\_cfg\_is\_tws\_right\_en(void)
:   app\_env\_cfg\_is\_tws\_right\_en brief description

    return enble or not function which distinguish TWS right size or left size setting by toolkit @APP\_ENV\_FEATURE\_FLAG\_TWS\_L\_R\_DIF\_EN

    返回值:
    :   **true** – enable

    返回:
    :   bool

    返回:
    :   false disalbe

<a id="_CPPv420app_env_get_sleep_env"></a>

<a id="_CPPv320app_env_get_sleep_env"></a> <a id="_CPPv220app_env_get_sleep_env"></a> <a id="app_env_get_sleep_en__void"></a> <a id="app__env_8h_1a55a5f8c521f474020ec2feb70530a64f"></a> bool app\_env\_get\_sleep\_en(void)
:   app\_env\_get\_sleep\_en brief description

    return sleep enable or not setting by toolkit @APP\_ENV\_FEATURE\_FLAG\_SLEEP\_ENABLE

    返回值:
    :   - **true** – enable
        - **false** – disable

    返回:
    :   bool

<a id="_CPPv424app_env_save_assert_infoPKc8uint16_t8uint32_t8uint32_t8uint32_tP13asssert_ctx_t"></a>

<a id="_CPPv324app_env_save_assert_infoPKc8uint16_t8uint32_t8uint32_t8uint32_tP13asssert_ctx_t"></a> <a id="_CPPv224app_env_save_assert_infoPKc8uint16_t8uint32_t8uint32_t8uint32_tP13asssert_ctx_t"></a> <a id="app_env_save_assert_info__cCP.uint16_t.uint32_t.uint32_t.uint32_t.asssert_ctx_tP"></a> <a id="app__env_8h_1a7e6f9ef961f90bcb15ba94fcce3005d9"></a> void app\_env\_save\_assert\_info(const char \*p\_func, uint16\_t line, uint32\_t para\_0, uint32\_t para\_1, uint32\_t lr, asssert\_ctx\_t \*p\_ctx)
:   app\_env\_save\_assert\_info brief description

    save assert dump information

    参数:
    :   - **p\_func** – **\[in\]** function name data buffer
        - **line** – **\[in\]** line number
        - **para\_0** – **\[in\]** parameter 1
        - **para\_1** – **\[in\]** parameter 2
        - **lr** – **\[in\]** link register
        - **p\_ctx** – **\[in\]** MCU register data struct

    返回:
    :   N/A

<a id="_CPPv425app_env_reset_assert_infov"></a>

<a id="_CPPv325app_env_reset_assert_infov"></a> <a id="_CPPv225app_env_reset_assert_infov"></a> <a id="app_env_reset_assert_info__void"></a> <a id="app__env_8h_1a3253e0b6a30ecb2ffc2cd497c2c353eb"></a> void app\_env\_reset\_assert\_info(void)
:   app\_env\_reset\_assert\_info brief description

    reset assert dump information

    返回:
    :   N/A

<a id="_CPPv421app_env_get_log_levelv"></a>

<a id="_CPPv321app_env_get_log_levelv"></a> <a id="_CPPv221app_env_get_log_levelv"></a> <a id="app_env_get_log_level__void"></a> <a id="app__env_8h_1a0b8c508357754c1eacc2ce8ece862352"></a> uint8\_t app\_env\_get\_log\_level(void)
:   app\_env\_get\_log\_level brief description

    return log level setting from environment

    返回:
    :   log level

<a id="_CPPv420app_env_set_tws_addrP7uint8_t"></a>

<a id="_CPPv320app_env_set_tws_addrP7uint8_t"></a> <a id="_CPPv220app_env_set_tws_addrP7uint8_t"></a> <a id="app_env_set_tws_addr__uint8_tP"></a> <a id="app__env_8h_1a7833ee557168d31e11eab4c275f03e66"></a> void app\_env\_set\_tws\_addr(uint8\_t \*p\_bd\_addr)
:   app\_env\_set\_tws\_addr brief description

    update tws addr

    返回:
    :   none

<a id="_CPPv423app_env_set_dev_bt_nameP7uint8_t7uint8_t"></a>

<a id="_CPPv323app_env_set_dev_bt_nameP7uint8_t7uint8_t"></a> <a id="_CPPv223app_env_set_dev_bt_nameP7uint8_t7uint8_t"></a> <a id="app_env_set_dev_bt_name__uint8_tP.uint8_t"></a> <a id="app__env_8h_1a3d19ba28ac6981be8afb9ee82d46e7e3"></a> void app\_env\_set\_dev\_bt\_name(uint8\_t \*p\_name, uint8\_t name\_len)
:   app\_env\_set\_dev\_bt\_name brief description

    update bt name

    返回:
    :   none

<a id="_CPPv427app_env_set_bt_calib_result7uint8_t"></a>

<a id="_CPPv327app_env_set_bt_calib_result7uint8_t"></a> <a id="_CPPv227app_env_set_bt_calib_result7uint8_t"></a> <a id="app_env_set_bt_calib_result__uint8_t"></a> <a id="app__env_8h_1a517c573aee7256929c1cadde595b796a"></a> void app\_env\_set\_bt\_calib\_result(uint8\_t calib\_result)
:   app\_env\_set\_bt\_calib\_result brief description

    update bt calib result

    返回:
    :   none

<a id="_CPPv427app_env_get_bt_calib_resultv"></a>

<a id="_CPPv327app_env_get_bt_calib_resultv"></a> <a id="_CPPv227app_env_get_bt_calib_resultv"></a> <a id="app_env_get_bt_calib_result__void"></a> <a id="app__env_8h_1a912553e92941ed5540f25242b39c82a9"></a> uint8\_t app\_env\_get\_bt\_calib\_result(void)
:   app\_env\_get\_bt\_calib\_result brief description

    update bt calib result

    返回:
    :   return bt calib result

<a id="_CPPv430app_env_data_get_bt_record_ptrP14btif_bd_addr_tPP18btif_bt_dev_info_t"></a>

<a id="_CPPv330app_env_data_get_bt_record_ptrP14btif_bd_addr_tPP18btif_bt_dev_info_t"></a> <a id="_CPPv230app_env_data_get_bt_record_ptrP14btif_bd_addr_tPP18btif_bt_dev_info_t"></a> <a id="app_env_data_get_bt_record_ptr__btif_bd_addr_tP.btif_bt_dev_info_tPP"></a> <a id="app__env_8h_1a1f72c5d37dd8101737b2fbedf13c417f"></a> [btif\_ret\_t](../../../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") app\_env\_data\_get\_bt\_record\_ptr([btif\_bd\_addr\_t](../../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") \*p\_bd\_addr, [btif\_bt\_dev\_info\_t](../../../btif/btif_type.md#_CPPv418btif_bt_dev_info_t "btif_bt_dev_info_t") \*\*p\_dev\_record)
:   app\_env\_data\_get\_bt\_record\_ptr brief description

    get dev info

    返回:
    :   return get record dev info

<a id="_CPPv434app_env_cfg_is_free_pairing_enablev"></a>

<a id="_CPPv334app_env_cfg_is_free_pairing_enablev"></a> <a id="_CPPv234app_env_cfg_is_free_pairing_enablev"></a> <a id="app_env_cfg_is_free_pairing_enable__void"></a> <a id="app__env_8h_1a92528fb077d69707a8029ca49ca5eed0"></a> bool app\_env\_cfg\_is\_free\_pairing\_enable(void)
:   app\_env\_cfg\_is\_free\_pairing\_enable brief description

    return is free pairing enable

    返回:
    :   return get record dev info

<a id="_CPPv436app_env_cfg_is_power_on_reconnect_env"></a>

<a id="_CPPv336app_env_cfg_is_power_on_reconnect_env"></a> <a id="_CPPv236app_env_cfg_is_power_on_reconnect_env"></a> <a id="app_env_cfg_is_power_on_reconnect_en__void"></a> <a id="app__env_8h_1a5ef905d3786b6fb6a7c4592f198dff8a"></a> bool app\_env\_cfg\_is\_power\_on\_reconnect\_en(void)
:   app\_env\_cfg\_is\_power\_on\_reconnect\_en brief description

    return true is power on reconnect enable

    返回:
    :   return get record dev info

<a id="_CPPv428app_env_cfg_get_le_addr_typev"></a>

<a id="_CPPv328app_env_cfg_get_le_addr_typev"></a> <a id="_CPPv228app_env_cfg_get_le_addr_typev"></a> <a id="app_env_cfg_get_le_addr_type__void"></a> <a id="app__env_8h_1aeb6e9c454e9d2becefee2fef9971023e"></a> uint8\_t app\_env\_cfg\_get\_le\_addr\_type(void)
:   app\_env\_cfg\_get\_le\_addr\_type brief description

    return le addr type

    返回:
    :   return get record dev info

<a id="structures"></a>

### Structures

<a id="_CPPv417app_env_pin_set_t"></a>

<a id="_CPPv317app_env_pin_set_t"></a> <a id="_CPPv217app_env_pin_set_t"></a> <a id="app_env_pin_set_t"></a> <a id="structapp__env__pin__set__t"></a> struct app\_env\_pin\_set\_t
:   GPIO special useage setting struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N17app_env_pin_set_t8gpio_idxE"></a>

    <a id="_CPPv3N17app_env_pin_set_t8gpio_idxE"></a> <a id="_CPPv2N17app_env_pin_set_t8gpio_idxE"></a> <a id="app_env_pin_set_t::gpio_idx__uint8_t"></a> <a id="structapp__env__pin__set__t_1a0aabdde4c6a657e7c0c2b63e7a2706b0"></a> uint8\_t gpio\_idx
    :   GPIO index

    <a id="_CPPv4N17app_env_pin_set_t11valid_levelE"></a>

    <a id="_CPPv3N17app_env_pin_set_t11valid_levelE"></a> <a id="_CPPv2N17app_env_pin_set_t11valid_levelE"></a> <a id="app_env_pin_set_t::valid_level__uint8_t"></a> <a id="structapp__env__pin__set__t_1a202b0ff22e6ce5d613f43ac89b18c950"></a> uint8\_t valid\_level
    :   low active or high active

    <a id="_CPPv4N17app_env_pin_set_t10pin_enableE"></a>

    <a id="_CPPv3N17app_env_pin_set_t10pin_enableE"></a> <a id="_CPPv2N17app_env_pin_set_t10pin_enableE"></a> <a id="app_env_pin_set_t::pin_enable__uint8_t"></a> <a id="structapp__env__pin__set__t_1a4b209d55afca35fe5145d69a930cde52"></a> uint8\_t pin\_enable
    :   pin enable or not

<a id="_CPPv414app_sys_para_t"></a>

<a id="_CPPv314app_sys_para_t"></a> <a id="_CPPv214app_sys_para_t"></a> <a id="app_sys_para_t"></a> <a id="structapp__sys__para__t"></a> struct app\_sys\_para\_t
:   system parameter setting data struct definition

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N14app_sys_para_t19mos_soft_power_flagE"></a>

    <a id="_CPPv3N14app_sys_para_t19mos_soft_power_flagE"></a> <a id="_CPPv2N14app_sys_para_t19mos_soft_power_flagE"></a> <a id="app_sys_para_t::mos_soft_power_flag__uint8_t"></a> <a id="structapp__sys__para__t_1a98d0292f2081d4b2f48063131cfcd53d"></a> uint8\_t mos\_soft\_power\_flag
    :   toolkit \- sys param \- power on/off setting(see @power\_key\_type\_t)

    <a id="_CPPv4N14app_sys_para_t15charger_currentE"></a>

    <a id="_CPPv3N14app_sys_para_t15charger_currentE"></a> <a id="_CPPv2N14app_sys_para_t15charger_currentE"></a> <a id="app_sys_para_t::charger_current__uint8_t"></a> <a id="structapp__sys__para__t_1a6b6b873b32da742c3be63985345a59db"></a> uint8\_t charger\_current
    :   toolkit \- feature \- value setting \- charging current(see@app\_env\_charging\_current\_t)

    <a id="_CPPv4N14app_sys_para_t14pop_icon_indexE"></a>

    <a id="_CPPv3N14app_sys_para_t14pop_icon_indexE"></a> <a id="_CPPv2N14app_sys_para_t14pop_icon_indexE"></a> <a id="app_sys_para_t::pop_icon_index__uint8_t"></a> <a id="structapp__sys__para__t_1a5297e5b96eae71d6dc25a4727afc58ef"></a> uint8\_t pop\_icon\_index
    :   toolkit \- feature \- value setting \- Pop-Up prompt icon

    <a id="_CPPv4N14app_sys_para_t11system_flagE"></a>

    <a id="_CPPv3N14app_sys_para_t11system_flagE"></a> <a id="_CPPv2N14app_sys_para_t11system_flagE"></a> <a id="app_sys_para_t::system_flag__app_env_sys_flag_t"></a> <a id="structapp__sys__para__t_1a9b003cbbbc3181d4087cf8f777216ff7"></a> [app\_env\_sys\_flag\_t](#_CPPv418app_env_sys_flag_t "app_env_sys_flag_t") system\_flag
    :   system environment setting

    <a id="_CPPv4N14app_sys_para_t4pinsE"></a>

    <a id="_CPPv3N14app_sys_para_t4pinsE"></a> <a id="_CPPv2N14app_sys_para_t4pinsE"></a> <a id="app_sys_para_t::pins__app_env_pin_set_tA"></a> <a id="structapp__sys__para__t_1a7bd98f718cfc3f9ab7684763f185dcf6"></a> [app\_env\_pin\_set\_t](#_CPPv417app_env_pin_set_t "app_env_pin_set_t") pins\[PIN\_MAX\]
    :   GPIO special usage setting

    <a id="_CPPv4N14app_sys_para_t8vol_a2dpE"></a>

    <a id="_CPPv3N14app_sys_para_t8vol_a2dpE"></a> <a id="_CPPv2N14app_sys_para_t8vol_a2dpE"></a> <a id="app_sys_para_t::vol_a2dp__uint8_t"></a> <a id="structapp__sys__para__t_1ac7b8cb72ed4be1c3f611f00ad5a9f72b"></a> uint8\_t vol\_a2dp
    :   toolkit \- audio base setting \- A2DP default volume

    <a id="_CPPv4N14app_sys_para_t7vol_hfpE"></a>

    <a id="_CPPv3N14app_sys_para_t7vol_hfpE"></a> <a id="_CPPv2N14app_sys_para_t7vol_hfpE"></a> <a id="app_sys_para_t::vol_hfp__uint8_t"></a> <a id="structapp__sys__para__t_1a5c3d4b998f61e4b53542c8da343a2d61"></a> uint8\_t vol\_hfp
    :   toolkit \- audio base setting \- HFP default volume

    <a id="_CPPv4N14app_sys_para_t8vol_waveE"></a>

    <a id="_CPPv3N14app_sys_para_t8vol_waveE"></a> <a id="_CPPv2N14app_sys_para_t8vol_waveE"></a> <a id="app_sys_para_t::vol_wave__uint8_t"></a> <a id="structapp__sys__para__t_1ab65bbf48eb551cbe6d2deaabaea0a9fb"></a> uint8\_t vol\_wave
    :   toolkit \- audio base setting \- hint default volume

    <a id="_CPPv4N14app_sys_para_t7vol_micE"></a>

    <a id="_CPPv3N14app_sys_para_t7vol_micE"></a> <a id="_CPPv2N14app_sys_para_t7vol_micE"></a> <a id="app_sys_para_t::vol_mic__app_env_mic_ana_gain_t"></a> <a id="structapp__sys__para__t_1a6f3438b0a5bbb75b885a1d8c7dc37ec7"></a> [app\_env\_mic\_ana\_gain\_t](#_CPPv422app_env_mic_ana_gain_t "app_env_mic_ana_gain_t") vol\_mic
    :   toolkit \- audio base setting \- MIC analog gain

    <a id="_CPPv4N14app_sys_para_t11lp_intervalE"></a>

    <a id="_CPPv3N14app_sys_para_t11lp_intervalE"></a> <a id="_CPPv2N14app_sys_para_t11lp_intervalE"></a> <a id="app_sys_para_t::lp_interval__uint32_t"></a> <a id="structapp__sys__para__t_1a0278382a44a627b62c57bb81ea69f41d"></a> uint32\_t lp\_interval
    :   toolkit \- sys param \- low battery setting \- detect interval

    <a id="_CPPv4N14app_sys_para_t12lp_thresholdE"></a>

    <a id="_CPPv3N14app_sys_para_t12lp_thresholdE"></a> <a id="_CPPv2N14app_sys_para_t12lp_thresholdE"></a> <a id="app_sys_para_t::lp_threshold__uint16_t"></a> <a id="structapp__sys__para__t_1a669703dd9f304947885baed012ec9136"></a> uint16\_t lp\_threshold
    :   toolkit \- sys param \- low battery setting \- warning threshold \= (2600 \+ lp\_threshold)/100

    <a id="_CPPv4N14app_sys_para_t15lp_pd_thresholdE"></a>

    <a id="_CPPv3N14app_sys_para_t15lp_pd_thresholdE"></a> <a id="_CPPv2N14app_sys_para_t15lp_pd_thresholdE"></a> <a id="app_sys_para_t::lp_pd_threshold__uint16_t"></a> <a id="structapp__sys__para__t_1a925c75ece193c7fa96f6e15e874c73b7"></a> uint16\_t lp\_pd\_threshold
    :   toolkit \- sys param \- low battery setting \- power down threshold \= (2600 \+ lp\_pd\_threshold)/100

    <a id="_CPPv4N14app_sys_para_t10lp_channelE"></a>

    <a id="_CPPv3N14app_sys_para_t10lp_channelE"></a> <a id="_CPPv2N14app_sys_para_t10lp_channelE"></a> <a id="app_sys_para_t::lp_channel__uint8_t"></a> <a id="structapp__sys__para__t_1abfaa93e0ad1f7f1f06f21ade213b234a"></a> uint8\_t lp\_channel
    :   toolkit \- sys param \- low battery setting \- channel see@ SADC\_CHANNEL

    <a id="_CPPv4N14app_sys_para_t10frq_offsetE"></a>

    <a id="_CPPv3N14app_sys_para_t10frq_offsetE"></a> <a id="_CPPv2N14app_sys_para_t10frq_offsetE"></a> <a id="app_sys_para_t::frq_offset__uint8_t"></a> <a id="structapp__sys__para__t_1a434c77c27c3874be9a4b8140377ff709"></a> uint8\_t frq\_offset
    :   toolkit \- feature \- rf function/freq offset \- trimmer capacitor

    <a id="_CPPv4N14app_sys_para_t13sleep_timeoutE"></a>

    <a id="_CPPv3N14app_sys_para_t13sleep_timeoutE"></a> <a id="_CPPv2N14app_sys_para_t13sleep_timeoutE"></a> <a id="app_sys_para_t::sleep_timeout__uint16_t"></a> <a id="structapp__sys__para__t_1ae0aa4e36b992d449d9ecf2c6b0abcd24"></a> uint16\_t sleep\_timeout
    :   toolkit \- sys param \- timeout setting \- Sleep timeout \= sleep\_timeout \* 10 ms

    <a id="_CPPv4N14app_sys_para_t19non_conn_pd_timeoutE"></a>

    <a id="_CPPv3N14app_sys_para_t19non_conn_pd_timeoutE"></a> <a id="_CPPv2N14app_sys_para_t19non_conn_pd_timeoutE"></a> <a id="app_sys_para_t::non_conn_pd_timeout__int32_t"></a> <a id="structapp__sys__para__t_1a663d46c62c371cf0eb60e77badac0ff2"></a> int32\_t non\_conn\_pd\_timeout
    :   toolkit \- sys param \- timeout setting \- Non-connect timeoutt enter power down \= non\_conn\_pd\_timeout \* 10 ms

    <a id="_CPPv4N14app_sys_para_t16pause_pd_timeoutE"></a>

    <a id="_CPPv3N14app_sys_para_t16pause_pd_timeoutE"></a> <a id="_CPPv2N14app_sys_para_t16pause_pd_timeoutE"></a> <a id="app_sys_para_t::pause_pd_timeout__int32_t"></a> <a id="structapp__sys__para__t_1a3cb08e6eef078b52e8fc6c36328871f9"></a> int32\_t pause\_pd\_timeout
    :   toolkit \- sys param \- timeout setting \- Power down when pause timeout \= pause\_pd\_timeout \* 10 ms

    <a id="_CPPv4N14app_sys_para_t12hfp_mic_chanE"></a>

    <a id="_CPPv3N14app_sys_para_t12hfp_mic_chanE"></a> <a id="_CPPv2N14app_sys_para_t12hfp_mic_chanE"></a> <a id="app_sys_para_t::hfp_mic_chan__uint8_t"></a> <a id="structapp__sys__para__t_1a80fc39e3c0d0951454b31e2ba58c24a2"></a> uint8\_t hfp\_mic\_chan
    :   toolkit \- audio base setting \- HFP MIC channel

    <a id="_CPPv4N14app_sys_para_t11tt_mic_chanE"></a>

    <a id="_CPPv3N14app_sys_para_t11tt_mic_chanE"></a> <a id="_CPPv2N14app_sys_para_t11tt_mic_chanE"></a> <a id="app_sys_para_t::tt_mic_chan__uint8_t"></a> <a id="structapp__sys__para__t_1a48ab53330462c1a4903a8f0988475111"></a> uint8\_t tt\_mic\_chan
    :   toolkit \- audio base setting \- TT MIC channel

    <a id="_CPPv4N14app_sys_para_t12anc_mic_chanE"></a>

    <a id="_CPPv3N14app_sys_para_t12anc_mic_chanE"></a> <a id="_CPPv2N14app_sys_para_t12anc_mic_chanE"></a> <a id="app_sys_para_t::anc_mic_chan__uint8_t"></a> <a id="structapp__sys__para__t_1a8f7cbf532a95d4cbe8b82d257fb345df"></a> uint8\_t anc\_mic\_chan
    :   toolkit \- audio base setting \- ANC MIC channel

    <a id="_CPPv4N14app_sys_para_t18charger_vol_offsetE"></a>

    <a id="_CPPv3N14app_sys_para_t18charger_vol_offsetE"></a> <a id="_CPPv2N14app_sys_para_t18charger_vol_offsetE"></a> <a id="app_sys_para_t::charger_vol_offset__uint8_t"></a> <a id="structapp__sys__para__t_1a020d0d235c74cce5b67eb25f7cea0877"></a> uint8\_t charger\_vol\_offset
    :   toolkit \- feature \- value setting \- charging voltage compensation

    <a id="_CPPv4N14app_sys_para_t9touch_crgE"></a>

    <a id="_CPPv3N14app_sys_para_t9touch_crgE"></a> <a id="_CPPv2N14app_sys_para_t9touch_crgE"></a> <a id="app_sys_para_t::touch_crg__uint8_tA"></a> <a id="structapp__sys__para__t_1ab63d3a8b62ce005040e8ff504a22b368"></a> uint8\_t touch\_crg\[4\]
    :   toolkit \- button \- touch configure setting

    <a id="_CPPv4N14app_sys_para_t9log_levelE"></a>

    <a id="_CPPv3N14app_sys_para_t9log_levelE"></a> <a id="_CPPv2N14app_sys_para_t9log_levelE"></a> <a id="app_sys_para_t::log_level__uint8_t"></a> <a id="structapp__sys__para__t_1ac69b59eddca5fcfa93935b6fb570ae10"></a> uint8\_t log\_level
    :   toolkit \- log level

    <a id="_CPPv4N14app_sys_para_t9vdda_clibE"></a>

    <a id="_CPPv3N14app_sys_para_t9vdda_clibE"></a> <a id="_CPPv2N14app_sys_para_t9vdda_clibE"></a> <a id="app_sys_para_t::vdda_clib__uint8_t"></a> <a id="structapp__sys__para__t_1a172a712b2562c58a7921357bde2c840f"></a> uint8\_t vdda\_clib
    :   toolkit \- feature \- value setting \- VDDA calibration value

    <a id="_CPPv4N14app_sys_para_t9reserved2E"></a>

    <a id="_CPPv3N14app_sys_para_t9reserved2E"></a> <a id="_CPPv2N14app_sys_para_t9reserved2E"></a> <a id="app_sys_para_t::reserved2__uint8_tA"></a> <a id="structapp__sys__para__t_1a73e5eeb5e306b296fea2794901c3c549"></a> uint8\_t reserved2\[10\]
    :   not used

<a id="_CPPv413app_bt_para_t"></a>

<a id="_CPPv313app_bt_para_t"></a> <a id="_CPPv213app_bt_para_t"></a> <a id="app_bt_para_t"></a> <a id="structapp__bt__para__t"></a> struct app\_bt\_para\_t
:   BT parameter data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N13app_bt_para_t7bt_flagE"></a>

    <a id="_CPPv3N13app_bt_para_t7bt_flagE"></a> <a id="_CPPv2N13app_bt_para_t7bt_flagE"></a> <a id="app_bt_para_t::bt_flag__app_env_bt_flag_t"></a> <a id="structapp__bt__para__t_1ab827134a2e3638d0a4b80d624461b796"></a> [app\_env\_bt\_flag\_t](#_CPPv417app_env_bt_flag_t "app_env_bt_flag_t") bt\_flag
    :   BT environment setting

    <a id="_CPPv4N13app_bt_para_t8dev_nameE"></a>

    <a id="_CPPv3N13app_bt_para_t8dev_nameE"></a> <a id="_CPPv2N13app_bt_para_t8dev_nameE"></a> <a id="app_bt_para_t::dev_name__uint8_tA"></a> <a id="structapp__bt__para__t_1a23faa16437ac9210eca6e249a2c403f2"></a> uint8\_t dev\_name\[APP\_ENV\_CFG\_NAME\_LEN\_MAX\]
    :   toolkit \- sys param \- basic param \- BT name

    <a id="_CPPv4N13app_bt_para_t7dev_pinE"></a>

    <a id="_CPPv3N13app_bt_para_t7dev_pinE"></a> <a id="_CPPv2N13app_bt_para_t7dev_pinE"></a> <a id="app_bt_para_t::dev_pin__uint8_tA"></a> <a id="structapp__bt__para__t_1a1e6b35adc25bfd9c1e5e919eb2940f08"></a> uint8\_t dev\_pin\[16\]
    :   toolkit \- sys param \- basic param \- default PIN

    <a id="_CPPv4N13app_bt_para_t8dev_addrE"></a>

    <a id="_CPPv3N13app_bt_para_t8dev_addrE"></a> <a id="_CPPv2N13app_bt_para_t8dev_addrE"></a> <a id="app_bt_para_t::dev_addr__btif_bd_addr_t"></a> <a id="structapp__bt__para__t_1a1f034ef9856baa1d2519e8d2b09b6237"></a> [btif\_bd\_addr\_t](../../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") dev\_addr
    :   toolkit \- sys param \- basic param \- BT address

    <a id="_CPPv4N13app_bt_para_t7dev_codE"></a>

    <a id="_CPPv3N13app_bt_para_t7dev_codE"></a> <a id="_CPPv2N13app_bt_para_t7dev_codE"></a> <a id="app_bt_para_t::dev_cod__app_env_dev_cod_t"></a> <a id="structapp__bt__para__t_1a5a3a29a0a106fe08e79241bd69f00bd1"></a> [app\_env\_dev\_cod\_t](#_CPPv417app_env_dev_cod_t "app_env_dev_cod_t") dev\_cod
    :   toolkit \- sys param \- basic param \- device type

    <a id="_CPPv4N13app_bt_para_t13reconn_actionE"></a>

    <a id="_CPPv3N13app_bt_para_t13reconn_actionE"></a> <a id="_CPPv2N13app_bt_para_t13reconn_actionE"></a> <a id="app_bt_para_t::reconn_action__app_env_reconn_action_t"></a> <a id="structapp__bt__para__t_1aad0bfcc1765577cde3cd58c089909d6f"></a> [app\_env\_reconn\_action\_t](#_CPPv423app_env_reconn_action_t "app_env_reconn_action_t") reconn\_action
    :   toolkit \- sys param \- reconnect \- connect action

    <a id="_CPPv4N13app_bt_para_t12reconn_startE"></a>

    <a id="_CPPv3N13app_bt_para_t12reconn_startE"></a> <a id="_CPPv2N13app_bt_para_t12reconn_startE"></a> <a id="app_bt_para_t::reconn_start__int32_t"></a> <a id="structapp__bt__para__t_1a8c757dc8436b51002da3a36bff288d3a"></a> int32\_t reconn\_start
    :   toolkit \- sys param \- reconnect \- start time

    <a id="_CPPv4N13app_bt_para_t21reconn_retry_intervalE"></a>

    <a id="_CPPv3N13app_bt_para_t21reconn_retry_intervalE"></a> <a id="_CPPv2N13app_bt_para_t21reconn_retry_intervalE"></a> <a id="app_bt_para_t::reconn_retry_interval__int32_t"></a> <a id="structapp__bt__para__t_1ae44080a95907c913ded8a8deed13a091"></a> int32\_t reconn\_retry\_interval
    :   toolkit \- sys param \- reconnect \- reconnect interval(val \>\= 4s unit:ms)

    <a id="_CPPv4N13app_bt_para_t18reconn_retry_countE"></a>

    <a id="_CPPv3N13app_bt_para_t18reconn_retry_countE"></a> <a id="_CPPv2N13app_bt_para_t18reconn_retry_countE"></a> <a id="app_bt_para_t::reconn_retry_count__int8_t"></a> <a id="structapp__bt__para__t_1a9a2fde0a4c28d6eec1f4dba9771273d3"></a> int8\_t reconn\_retry\_count
    :   toolkit \- sys param \- reconnect \- reconnect count

    <a id="_CPPv4N13app_bt_para_t20poweron_reconn_countE"></a>

    <a id="_CPPv3N13app_bt_para_t20poweron_reconn_countE"></a> <a id="_CPPv2N13app_bt_para_t20poweron_reconn_countE"></a> <a id="app_bt_para_t::poweron_reconn_count__int8_t"></a> <a id="structapp__bt__para__t_1a18e7cdd0aa850c298c5a8447f2476371"></a> int8\_t poweron\_reconn\_count
    :   toolkit \- sys param \- poweron reconnect \- reconnect count

    <a id="_CPPv4N13app_bt_para_t23poweron_reconn_intervalE"></a>

    <a id="_CPPv3N13app_bt_para_t23poweron_reconn_intervalE"></a> <a id="_CPPv2N13app_bt_para_t23poweron_reconn_intervalE"></a> <a id="app_bt_para_t::poweron_reconn_interval__uint16_t"></a> <a id="structapp__bt__para__t_1aa7269973d3a9f94f1e47b337f6a761eb"></a> uint16\_t poweron\_reconn\_interval
    :   toolkit \- sys param \- poweron reconnect \- reconnect interval(val \>\= 4s unit:ms)

    <a id="_CPPv4N13app_bt_para_t12pair_timeoutE"></a>

    <a id="_CPPv3N13app_bt_para_t12pair_timeoutE"></a> <a id="_CPPv2N13app_bt_para_t12pair_timeoutE"></a> <a id="app_bt_para_t::pair_timeout__int16_t"></a> <a id="structapp__bt__para__t_1ae98e9ca7ded36c5d257082f78239effc"></a> int16\_t pair\_timeout
    :   toolkit \- sys param \- paring timeout(unit:s)

    <a id="_CPPv4N13app_bt_para_t12auto_pd_condE"></a>

    <a id="_CPPv3N13app_bt_para_t12auto_pd_condE"></a> <a id="_CPPv2N13app_bt_para_t12auto_pd_condE"></a> <a id="app_bt_para_t::auto_pd_cond__app_env_auto_pd_cond_t"></a> <a id="structapp__bt__para__t_1aac621cba597a6e70eb6bae90b8a3e071"></a> [app\_env\_auto\_pd\_cond\_t](#_CPPv422app_env_auto_pd_cond_t "app_env_auto_pd_cond_t") auto\_pd\_cond
    :   toolkit \- sys param \- other -auto power off condition

    <a id="_CPPv4N13app_bt_para_t14disconn_actionE"></a>

    <a id="_CPPv3N13app_bt_para_t14disconn_actionE"></a> <a id="_CPPv2N13app_bt_para_t14disconn_actionE"></a> <a id="app_bt_para_t::disconn_action__uint8_t"></a> <a id="structapp__bt__para__t_1a131aa3c6e7549e1d13c2a439f4bababd"></a> uint8\_t disconn\_action
    :   toolkit \- sys param \- other -disconnect action

<a id="_CPPv414app_ble_para_t"></a>

<a id="_CPPv314app_ble_para_t"></a> <a id="_CPPv214app_ble_para_t"></a> <a id="app_ble_para_t"></a> <a id="structapp__ble__para__t"></a> struct app\_ble\_para\_t
:   BLE parameter data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N14app_ble_para_t8ble_flagE"></a>

    <a id="_CPPv3N14app_ble_para_t8ble_flagE"></a> <a id="_CPPv2N14app_ble_para_t8ble_flagE"></a> <a id="app_ble_para_t::ble_flag__app_env_le_flag_t"></a> <a id="structapp__ble__para__t_1ac55827239d882df42ebcdf3db9908758"></a> [app\_env\_le\_flag\_t](#_CPPv417app_env_le_flag_t "app_env_le_flag_t") ble\_flag
    :   BLE environment setting

    <a id="_CPPv4N14app_ble_para_t11public_addrE"></a>

    <a id="_CPPv3N14app_ble_para_t11public_addrE"></a> <a id="_CPPv2N14app_ble_para_t11public_addrE"></a> <a id="app_ble_para_t::public_addr__btif_bd_addr_t"></a> <a id="structapp__ble__para__t_1a1fa5d35a86fc43197cd349e027183c66"></a> [btif\_bd\_addr\_t](../../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") public\_addr
    :   toolkit \- sys param \- BLE setting \- ble public address

    <a id="_CPPv4N14app_ble_para_t11static_addrE"></a>

    <a id="_CPPv3N14app_ble_para_t11static_addrE"></a> <a id="_CPPv2N14app_ble_para_t11static_addrE"></a> <a id="app_ble_para_t::static_addr__btif_bd_addr_t"></a> <a id="structapp__ble__para__t_1aa1644deb2252fb08c81f5d7ad43f1613"></a> [btif\_bd\_addr\_t](../../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") static\_addr
    :   toolkit \- sys param \- BLE setting \- ble static address

    <a id="_CPPv4N14app_ble_para_t8dev_nameE"></a>

    <a id="_CPPv3N14app_ble_para_t8dev_nameE"></a> <a id="_CPPv2N14app_ble_para_t8dev_nameE"></a> <a id="app_ble_para_t::dev_name__cA"></a> <a id="structapp__ble__para__t_1a48538ba705e6a758ed227b4e3cfd4d30"></a> char dev\_name\[APP\_ENV\_CFG\_NAME\_LEN\_MAX\]
    :   toolkit \- sys param \- BLE setting \- ble name

    <a id="_CPPv4N14app_ble_para_t12adv_intervalE"></a>

    <a id="_CPPv3N14app_ble_para_t12adv_intervalE"></a> <a id="_CPPv2N14app_ble_para_t12adv_intervalE"></a> <a id="app_ble_para_t::adv_interval__uint16_t"></a> <a id="structapp__ble__para__t_1ab4e8d7355bb7b178b087aa1963f2762d"></a> uint16\_t adv\_interval
    :   toolkit \- sys param \- BLE setting \- adv interval(adv\_interval \* 1.25ms)

    <a id="_CPPv4N14app_ble_para_t22conn_update_delay_timeE"></a>

    <a id="_CPPv3N14app_ble_para_t22conn_update_delay_timeE"></a> <a id="_CPPv2N14app_ble_para_t22conn_update_delay_timeE"></a> <a id="app_ble_para_t::conn_update_delay_time__uint16_t"></a> <a id="structapp__ble__para__t_1a10063c1d79840788c7a0d02cfd1285f3"></a> uint16\_t conn\_update\_delay\_time
    :   toolkit \- sys param \- BLE setting \- connection update delay time (unit:s)

    <a id="_CPPv4N14app_ble_para_t17conn_interval_minE"></a>

    <a id="_CPPv3N14app_ble_para_t17conn_interval_minE"></a> <a id="_CPPv2N14app_ble_para_t17conn_interval_minE"></a> <a id="app_ble_para_t::conn_interval_min__uint16_t"></a> <a id="structapp__ble__para__t_1a772025327a33d0b806084eff8eb19fc5"></a> uint16\_t conn\_interval\_min
    :   toolkit \- sys param \- BLE setting \- MIN connect interval(conn\_interval\_min \* 1.25ms)

    <a id="_CPPv4N14app_ble_para_t17conn_interval_maxE"></a>

    <a id="_CPPv3N14app_ble_para_t17conn_interval_maxE"></a> <a id="_CPPv2N14app_ble_para_t17conn_interval_maxE"></a> <a id="app_ble_para_t::conn_interval_max__uint16_t"></a> <a id="structapp__ble__para__t_1aea0a144a6029beb7923d2643396d703c"></a> uint16\_t conn\_interval\_max
    :   toolkit \- sys param \- BLE setting \- MAX connect interval(conn\_interval\_max \* 1.25ms)

    <a id="_CPPv4N14app_ble_para_t12csip_pt_sirkE"></a>

    <a id="_CPPv3N14app_ble_para_t12csip_pt_sirkE"></a> <a id="_CPPv2N14app_ble_para_t12csip_pt_sirkE"></a> <a id="app_ble_para_t::csip_pt_sirk__uint8_tA"></a> <a id="structapp__ble__para__t_1a76d75c93647a748e8c3c3566381cb5a7"></a> uint8\_t csip\_pt\_sirk\[16\]
    :   toolkit \- sys param \- BLE setting \- CSIP SIRK

    <a id="_CPPv4N14app_ble_para_t26pref_max_transport_latencyE"></a>

    <a id="_CPPv3N14app_ble_para_t26pref_max_transport_latencyE"></a> <a id="_CPPv2N14app_ble_para_t26pref_max_transport_latencyE"></a> <a id="app_ble_para_t::pref_max_transport_latency__uint16_t"></a> <a id="structapp__ble__para__t_1aa7cdfde663071880a48ff84dbd4a8d2e"></a> uint16\_t pref\_max\_transport\_latency
    :   toolkit \- sys param \- BLE setting \- max tranport lantency

    <a id="_CPPv4N14app_ble_para_t27pref_presentation_delay_minE"></a>

    <a id="_CPPv3N14app_ble_para_t27pref_presentation_delay_minE"></a> <a id="_CPPv2N14app_ble_para_t27pref_presentation_delay_minE"></a> <a id="app_ble_para_t::pref_presentation_delay_min__uint32_t"></a> <a id="structapp__ble__para__t_1a691e594aae0fd1bd958eada6706fce44"></a> uint32\_t pref\_presentation\_delay\_min
    :   toolkit \- sys param \- BLE setting \- pref pd min

    <a id="_CPPv4N14app_ble_para_t27pref_presentation_delay_maxE"></a>

    <a id="_CPPv3N14app_ble_para_t27pref_presentation_delay_maxE"></a> <a id="_CPPv2N14app_ble_para_t27pref_presentation_delay_maxE"></a> <a id="app_ble_para_t::pref_presentation_delay_max__uint32_t"></a> <a id="structapp__ble__para__t_1a4e47ab10b7510bf6132c1aa3a9bd8509"></a> uint32\_t pref\_presentation\_delay\_max
    :   toolkit \- sys param \- BLE setting \- pref pd max

    <a id="_CPPv4N14app_ble_para_t27supp_presentation_delay_minE"></a>

    <a id="_CPPv3N14app_ble_para_t27supp_presentation_delay_minE"></a> <a id="_CPPv2N14app_ble_para_t27supp_presentation_delay_minE"></a> <a id="app_ble_para_t::supp_presentation_delay_min__uint32_t"></a> <a id="structapp__ble__para__t_1aa0038d133f960c0d31448f79956a234d"></a> uint32\_t supp\_presentation\_delay\_min
    :   toolkit \- sys param \- BLE setting \- support pd min

    <a id="_CPPv4N14app_ble_para_t27supp_presentation_delay_maxE"></a>

    <a id="_CPPv3N14app_ble_para_t27supp_presentation_delay_maxE"></a> <a id="_CPPv2N14app_ble_para_t27supp_presentation_delay_maxE"></a> <a id="app_ble_para_t::supp_presentation_delay_max__uint32_t"></a> <a id="structapp__ble__para__t_1a8ad6f86da47ab4743c58c485f52c14e2"></a> uint32\_t supp\_presentation\_delay\_max
    :   toolkit \- sys param \- BLE setting \- support pd max

    <a id="_CPPv4N14app_ble_para_t8reservedE"></a>

    <a id="_CPPv3N14app_ble_para_t8reservedE"></a> <a id="_CPPv2N14app_ble_para_t8reservedE"></a> <a id="app_ble_para_t::reserved__uint8_tA"></a> <a id="structapp__ble__para__t_1ad06b71379944375652a7e2165ad6fe59"></a> uint8\_t reserved\[19\]
    :   not used

<a id="_CPPv413app_eq_para_t"></a>

<a id="_CPPv313app_eq_para_t"></a> <a id="_CPPv213app_eq_para_t"></a> <a id="app_eq_para_t"></a> <a id="structapp__eq__para__t"></a> struct app\_eq\_para\_t
:   EQ parameter data strcut definition.

<a id="_CPPv412app_aud_eq_t"></a>

<a id="_CPPv312app_aud_eq_t"></a> <a id="_CPPv212app_aud_eq_t"></a> <a id="app_aud_eq_t"></a> <a id="structapp__aud__eq__t"></a> struct app\_aud\_eq\_t
:   EQ setting data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N12app_aud_eq_t9eq_enableE"></a>

    <a id="_CPPv3N12app_aud_eq_t9eq_enableE"></a> <a id="_CPPv2N12app_aud_eq_t9eq_enableE"></a> <a id="app_aud_eq_t::eq_enable__uint16_t"></a> <a id="structapp__aud__eq__t_1a0809689e54555ccf98742c8089bf6535"></a> uint16\_t eq\_enable
    :   toolkit \- audio eq \- 16 order(bitmap), bit0-\>eq\_para\[0\]

    <a id="_CPPv4N12app_aud_eq_t7eq_gainE"></a>

    <a id="_CPPv3N12app_aud_eq_t7eq_gainE"></a> <a id="_CPPv2N12app_aud_eq_t7eq_gainE"></a> <a id="app_aud_eq_t::eq_gain__int16_t"></a> <a id="structapp__aud__eq__t_1a1563aa19ae1898aa04414d744d08a932"></a> int16\_t eq\_gain
    :   toolkit \- audio eq \- total gain

<a id="_CPPv413app_hfp_cfg_t"></a>

<a id="_CPPv313app_hfp_cfg_t"></a> <a id="_CPPv213app_hfp_cfg_t"></a> <a id="app_hfp_cfg_t"></a> <a id="structapp__hfp__cfg__t"></a> struct app\_hfp\_cfg\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N13app_hfp_cfg_t7parasetE"></a>

    <a id="_CPPv3N13app_hfp_cfg_t7parasetE"></a> <a id="_CPPv2N13app_hfp_cfg_t7parasetE"></a> <a id="app_hfp_cfg_t::paraset__uint8_t"></a> <a id="structapp__hfp__cfg__t_1a2375119de54baf5de282a01a75cce800"></a> uint8\_t paraset
    :   toolkit \- call setting \- aec/ns enable \- use default(0 or 1\)

    <a id="_CPPv4N13app_hfp_cfg_t8ns_levelE"></a>

    <a id="_CPPv3N13app_hfp_cfg_t8ns_levelE"></a> <a id="_CPPv2N13app_hfp_cfg_t8ns_levelE"></a> <a id="app_hfp_cfg_t::ns_level__uint8_t"></a> <a id="structapp__hfp__cfg__t_1a604398c92c77dc7afb82b72038558722"></a> uint8\_t ns\_level
    :   toolkit \- call setting \- aec/ns enable \- noise reduction lecel (0\~3)

    <a id="_CPPv4N13app_hfp_cfg_t8out_gainE"></a>

    <a id="_CPPv3N13app_hfp_cfg_t8out_gainE"></a> <a id="_CPPv2N13app_hfp_cfg_t8out_gainE"></a> <a id="app_hfp_cfg_t::out_gain__uint8_t"></a> <a id="structapp__hfp__cfg__t_1abec953c67c18f93b3b4bb60871a686aa"></a> uint8\_t out\_gain
    :   toolkit \- call setting \- aec/ns enable \- output gain (0 \~ 30\)

    <a id="_CPPv4N13app_hfp_cfg_t8ec_levelE"></a>

    <a id="_CPPv3N13app_hfp_cfg_t8ec_levelE"></a> <a id="_CPPv2N13app_hfp_cfg_t8ec_levelE"></a> <a id="app_hfp_cfg_t::ec_level__uint8_t"></a> <a id="structapp__hfp__cfg__t_1a6030d22ea2502047fe0d09886ee19047"></a> uint8\_t ec\_level
    :   toolkit \- call setting \- aec/ns enable \- aec level (0 \~ 30\)

    <a id="_CPPv4N13app_hfp_cfg_t8d2a_loopE"></a>

    <a id="_CPPv3N13app_hfp_cfg_t8d2a_loopE"></a> <a id="_CPPv2N13app_hfp_cfg_t8d2a_loopE"></a> <a id="app_hfp_cfg_t::d2a_loop__uint8_t"></a> <a id="structapp__hfp__cfg__t_1adbe5e445160a300dbc039ad6a3f4c52d"></a> uint8\_t d2a\_loop
    :   toolkit \- call setting \- boolean for enale DAC ADC loop

    <a id="_CPPv4N13app_hfp_cfg_t4minGE"></a>

    <a id="_CPPv3N13app_hfp_cfg_t4minGE"></a> <a id="_CPPv2N13app_hfp_cfg_t4minGE"></a> <a id="app_hfp_cfg_t::minG__uint8_t"></a> <a id="structapp__hfp__cfg__t_1abe5f8dac611095fe59337805b91b007f"></a> uint8\_t minG
    :   toolkit \- call setting \- MIC gain

    <a id="_CPPv4N13app_hfp_cfg_t4distE"></a>

    <a id="_CPPv3N13app_hfp_cfg_t4distE"></a> <a id="_CPPv2N13app_hfp_cfg_t4distE"></a> <a id="app_hfp_cfg_t::dist__uint8_t"></a> <a id="structapp__hfp__cfg__t_1a81515097d5f34e339e2130a3d2d1b8b6"></a> uint8\_t dist
    :   toolkit \- call setting \- distance between two MIC

    <a id="_CPPv4N13app_hfp_cfg_t7dualmicE"></a>

    <a id="_CPPv3N13app_hfp_cfg_t7dualmicE"></a> <a id="_CPPv2N13app_hfp_cfg_t7dualmicE"></a> <a id="app_hfp_cfg_t::dualmic__uint8_t"></a> <a id="structapp__hfp__cfg__t_1a9281e31ec9b432bf2777a21c7d90625a"></a> uint8\_t dualmic
    :   toolkit \- call setting \- boolean for enale daul MIC setting

    <a id="_CPPv4N13app_hfp_cfg_t7mainmicE"></a>

    <a id="_CPPv3N13app_hfp_cfg_t7mainmicE"></a> <a id="_CPPv2N13app_hfp_cfg_t7mainmicE"></a> <a id="app_hfp_cfg_t::mainmic__uint8_t"></a> <a id="structapp__hfp__cfg__t_1ac469dcdd6cfc3762339f970395864ac6"></a> uint8\_t mainmic
    :   toolkit \- call setting \- main MIC index

    <a id="_CPPv4N13app_hfp_cfg_t9eq_enableE"></a>

    <a id="_CPPv3N13app_hfp_cfg_t9eq_enableE"></a> <a id="_CPPv2N13app_hfp_cfg_t9eq_enableE"></a> <a id="app_hfp_cfg_t::eq_enable__uint8_t"></a> <a id="structapp__hfp__cfg__t_1a77c43ea7eca5414b6f6fd73343f18b92"></a> uint8\_t eq\_enable
    :   toolkit \- call setting \- EQ enable or not

    <a id="_CPPv4N13app_hfp_cfg_t10tlv_eq_addE"></a>

    <a id="_CPPv3N13app_hfp_cfg_t10tlv_eq_addE"></a> <a id="_CPPv2N13app_hfp_cfg_t10tlv_eq_addE"></a> <a id="app_hfp_cfg_t::tlv_eq_add__uint32_t"></a> <a id="structapp__hfp__cfg__t_1a8233288620bb7824ab4dacd2e3ec2a17"></a> uint32\_t tlv\_eq\_add
    :   toolkit \- call setting \- flash address for calling EQ setting

    <a id="_CPPv4N13app_hfp_cfg_t8reservedE"></a>

    <a id="_CPPv3N13app_hfp_cfg_t8reservedE"></a> <a id="_CPPv2N13app_hfp_cfg_t8reservedE"></a> <a id="app_hfp_cfg_t::reserved__uint8_tA"></a> <a id="structapp__hfp__cfg__t_1aae4b9ff47e70a9b555f174fd2138c418"></a> uint8\_t reserved\[158\]
    :   not used

<a id="_CPPv414app_drc_para_t"></a>

<a id="_CPPv314app_drc_para_t"></a> <a id="_CPPv214app_drc_para_t"></a> <a id="app_drc_para_t"></a> <a id="structapp__drc__para__t"></a> struct app\_drc\_para\_t
:   DRC parameter setting definition LCI.

<a id="_CPPv414app_vol_info_t"></a>

<a id="_CPPv314app_vol_info_t"></a> <a id="_CPPv214app_vol_info_t"></a> <a id="app_vol_info_t"></a> <a id="structapp__vol__info__t"></a> struct app\_vol\_info\_t
:   volume gain setting data struct definition

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N14app_vol_info_t8dig_gainE"></a>

    <a id="_CPPv3N14app_vol_info_t8dig_gainE"></a> <a id="_CPPv2N14app_vol_info_t8dig_gainE"></a> <a id="app_vol_info_t::dig_gain__uint32_t"></a> <a id="structapp__vol__info__t_1aa200a25293927610f8fea870753524ac"></a> uint32\_t dig\_gain
    :   digital gian

    <a id="_CPPv4N14app_vol_info_t8ana_gainE"></a>

    <a id="_CPPv3N14app_vol_info_t8ana_gainE"></a> <a id="_CPPv2N14app_vol_info_t8ana_gainE"></a> <a id="app_vol_info_t::ana_gain__uint32_t"></a> <a id="structapp__vol__info__t_1a5f0e3f6f73be39dcea2253e3be2ef819"></a> uint32\_t ana\_gain
    :   analog gain

<a id="_CPPv412app_volume_t"></a>

<a id="_CPPv312app_volume_t"></a> <a id="_CPPv212app_volume_t"></a> <a id="app_volume_t"></a> <a id="structapp__volume__t"></a> struct app\_volume\_t
:   volume level setting data struct definition

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N12app_volume_t3volE"></a>

    <a id="_CPPv3N12app_volume_t3volE"></a> <a id="_CPPv2N12app_volume_t3volE"></a> <a id="app_volume_t::vol__app_vol_info_tA"></a> <a id="structapp__volume__t_1ab925707eac8c8837f13205e369040837"></a> [app\_vol\_info\_t](#_CPPv414app_vol_info_t "app_vol_info_t") vol\[APP\_ENV\_VOL\_LEVEL\_CNT\_MAX\]
    :   gain setting array for volume level

<a id="_CPPv411app_rfpwr_t"></a>

<a id="_CPPv311app_rfpwr_t"></a> <a id="_CPPv211app_rfpwr_t"></a> <a id="app_rfpwr_t"></a> <a id="structapp__rfpwr__t"></a> struct app\_rfpwr\_t
:   RF power adjust data strcut definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N11app_rfpwr_t7big_adjE"></a>

    <a id="_CPPv3N11app_rfpwr_t7big_adjE"></a> <a id="_CPPv2N11app_rfpwr_t7big_adjE"></a> <a id="app_rfpwr_t::big_adj__uint8_t"></a> <a id="structapp__rfpwr__t_1a8c973b0427b3fbdfb9258599ec806125"></a> uint8\_t big\_adj
    :   xvr\_0x24{bit10:bit7}

<a id="_CPPv417app_bat_display_t"></a>

<a id="_CPPv317app_bat_display_t"></a> <a id="_CPPv217app_bat_display_t"></a> <a id="app_bat_display_t"></a> <a id="structapp__bat__display__t"></a> struct app\_bat\_display\_t
:   battery level data struct definition

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N17app_bat_display_t9bat_levelE"></a>

    <a id="_CPPv3N17app_bat_display_t9bat_levelE"></a> <a id="_CPPv2N17app_bat_display_t9bat_levelE"></a> <a id="app_bat_display_t::bat_level__uint16_tA"></a> <a id="structapp__bat__display__t_1a4b23d697728ceedb7dccf56ef65c7dea"></a> uint16\_t bat\_level\[10\]
    :   battery voltage

<a id="_CPPv416app_saradc_vol_t"></a>

<a id="_CPPv316app_saradc_vol_t"></a> <a id="_CPPv216app_saradc_vol_t"></a> <a id="app_saradc_vol_t"></a> <a id="structapp__saradc__vol__t"></a> struct app\_saradc\_vol\_t
:   SAR ADC setting data struct definition.

<a id="_CPPv416app_sw_feature_t"></a>

<a id="_CPPv316app_sw_feature_t"></a> <a id="_CPPv216app_sw_feature_t"></a> <a id="app_sw_feature_t"></a> <a id="structapp__sw__feature__t"></a> struct app\_sw\_feature\_t
:   software features data struct definition

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N16app_sw_feature_t12feature_flagE"></a>

    <a id="_CPPv3N16app_sw_feature_t12feature_flagE"></a> <a id="_CPPv2N16app_sw_feature_t12feature_flagE"></a> <a id="app_sw_feature_t::feature_flag__app_env_feat_flag_t"></a> <a id="structapp__sw__feature__t_1a10b7bf840551b91387660976163fba1a"></a> [app\_env\_feat\_flag\_t](#_CPPv419app_env_feat_flag_t "app_env_feat_flag_t") feature\_flag
    :   features setting

    <a id="_CPPv4N16app_sw_feature_t14charge_timeoutE"></a>

    <a id="_CPPv3N16app_sw_feature_t14charge_timeoutE"></a> <a id="_CPPv2N16app_sw_feature_t14charge_timeoutE"></a> <a id="app_sw_feature_t::charge_timeout__int32_t"></a> <a id="structapp__sw__feature__t_1ab940e4ee38db18f38320f3cb6c6b5f30"></a> int32\_t charge\_timeout
    :   Not used

    <a id="_CPPv4N16app_sw_feature_t7bt_modeE"></a>

    <a id="_CPPv3N16app_sw_feature_t7bt_modeE"></a> <a id="_CPPv2N16app_sw_feature_t7bt_modeE"></a> <a id="app_sw_feature_t::bt_mode__bt_mode_t"></a> <a id="structapp__sw__feature__t_1aa284544406636f347961b513d911b882"></a> [bt\_mode\_t](#_CPPv49bt_mode_t "bt_mode_t") bt\_mode
    :   toolkit \- feature \- 1V2(default 1V1, tws isnot config in the toolkit)

    <a id="_CPPv4N16app_sw_feature_t17a2dp_vol_gain_cfgE"></a>

    <a id="_CPPv3N16app_sw_feature_t17a2dp_vol_gain_cfgE"></a> <a id="_CPPv2N16app_sw_feature_t17a2dp_vol_gain_cfgE"></a> <a id="app_sw_feature_t::a2dp_vol_gain_cfg__app_volume_t"></a> <a id="structapp__sw__feature__t_1aac6b8d1b595ec455a1c269c16e00b0b7"></a> [app\_volume\_t](#_CPPv412app_volume_t "app_volume_t") a2dp\_vol\_gain\_cfg
    :   toolkit \- audio base setting \- a2dp vol gain config table

    <a id="_CPPv4N16app_sw_feature_t16hfp_vol_gain_cfgE"></a>

    <a id="_CPPv3N16app_sw_feature_t16hfp_vol_gain_cfgE"></a> <a id="_CPPv2N16app_sw_feature_t16hfp_vol_gain_cfgE"></a> <a id="app_sw_feature_t::hfp_vol_gain_cfg__app_volume_t"></a> <a id="structapp__sw__feature__t_1ad76fbee187479ef560c6363d44521b1f"></a> [app\_volume\_t](#_CPPv412app_volume_t "app_volume_t") hfp\_vol\_gain\_cfg
    :   toolkit \- audio base setting \- hfp vol gain config table

    <a id="_CPPv4N16app_sw_feature_t19linein_vol_gain_cfgE"></a>

    <a id="_CPPv3N16app_sw_feature_t19linein_vol_gain_cfgE"></a> <a id="_CPPv2N16app_sw_feature_t19linein_vol_gain_cfgE"></a> <a id="app_sw_feature_t::linein_vol_gain_cfg__app_volume_t"></a> <a id="structapp__sw__feature__t_1a2824c894ce220f704214a7867f2995fb"></a> [app\_volume\_t](#_CPPv412app_volume_t "app_volume_t") linein\_vol\_gain\_cfg
    :   toolkit \- audio base setting \- linein vol gain config table

    <a id="_CPPv4N16app_sw_feature_t11vol_mic_digE"></a>

    <a id="_CPPv3N16app_sw_feature_t11vol_mic_digE"></a> <a id="_CPPv2N16app_sw_feature_t11vol_mic_digE"></a> <a id="app_sw_feature_t::vol_mic_dig__uint8_t"></a> <a id="structapp__sw__feature__t_1aa3781a32d7b13f4366a6a95b3ba3e85f"></a> uint8\_t vol\_mic\_dig
    :   toolkit \- audio HFP \- MIC digital gain

    <a id="_CPPv4N16app_sw_feature_t11vol_mic_anaE"></a>

    <a id="_CPPv3N16app_sw_feature_t11vol_mic_anaE"></a> <a id="_CPPv2N16app_sw_feature_t11vol_mic_anaE"></a> <a id="app_sw_feature_t::vol_mic_ana__app_env_mic_ana_gain_t"></a> <a id="structapp__sw__feature__t_1ab850a5a0dbfeedd6ae10467be36840e3"></a> [app\_env\_mic\_ana\_gain\_t](#_CPPv422app_env_mic_ana_gain_t "app_env_mic_ana_gain_t") vol\_mic\_ana
    :   toolkit \- audio HFP \- MIC analog gain

    <a id="_CPPv4N16app_sw_feature_t14vol_linein_digE"></a>

    <a id="_CPPv3N16app_sw_feature_t14vol_linein_digE"></a> <a id="_CPPv2N16app_sw_feature_t14vol_linein_digE"></a> <a id="app_sw_feature_t::vol_linein_dig__uint8_t"></a> <a id="structapp__sw__feature__t_1a593ea016c30762a4810880c3a7b0f4da"></a> uint8\_t vol\_linein\_dig
    :   toolkit \- audio base setting \- Linein digital gain

    <a id="_CPPv4N16app_sw_feature_t14vol_linein_anaE"></a>

    <a id="_CPPv3N16app_sw_feature_t14vol_linein_anaE"></a> <a id="_CPPv2N16app_sw_feature_t14vol_linein_anaE"></a> <a id="app_sw_feature_t::vol_linein_ana__uint8_t"></a> <a id="structapp__sw__feature__t_1ad6e6f11061ce7d7f44f845516392bfc4"></a> uint8\_t vol\_linein\_ana
    :   toolkit \- audio base setting \- Linein analog gain

    <a id="_CPPv4N16app_sw_feature_t18pa_mute_delay_timeE"></a>

    <a id="_CPPv3N16app_sw_feature_t18pa_mute_delay_timeE"></a> <a id="_CPPv2N16app_sw_feature_t18pa_mute_delay_timeE"></a> <a id="app_sw_feature_t::pa_mute_delay_time__uint8_t"></a> <a id="structapp__sw__feature__t_1a021e9b00795461f94d168af3064cf5aa"></a> uint8\_t pa\_mute\_delay\_time
    :   toolkit \- feature \- PA Mute setting \- delay

    <a id="_CPPv4N16app_sw_feature_t20pa_unmute_delay_timeE"></a>

    <a id="_CPPv3N16app_sw_feature_t20pa_unmute_delay_timeE"></a> <a id="_CPPv2N16app_sw_feature_t20pa_unmute_delay_timeE"></a> <a id="app_sw_feature_t::pa_unmute_delay_time__uint8_t"></a> <a id="structapp__sw__feature__t_1ad85a01b57a7aea1c70e11a2117e581c7"></a> uint8\_t pa\_unmute\_delay\_time
    :   toolkit \- feature \- PA Mute setting \- UN-delay

    <a id="_CPPv4N16app_sw_feature_t18sw_pwr_on_key_timeE"></a>

    <a id="_CPPv3N16app_sw_feature_t18sw_pwr_on_key_timeE"></a> <a id="_CPPv2N16app_sw_feature_t18sw_pwr_on_key_timeE"></a> <a id="app_sw_feature_t::sw_pwr_on_key_time__uint16_t"></a> <a id="structapp__sw__feature__t_1a8338bf0f3c694bb268c8541cc336f7ff"></a> uint16\_t sw\_pwr\_on\_key\_time
    :   toolkit \- sys pram- power on/off setting \- soft-poweron time

    <a id="_CPPv4N16app_sw_feature_t19sw_pwr_off_key_timeE"></a>

    <a id="_CPPv3N16app_sw_feature_t19sw_pwr_off_key_timeE"></a> <a id="_CPPv2N16app_sw_feature_t19sw_pwr_off_key_timeE"></a> <a id="app_sw_feature_t::sw_pwr_off_key_time__uint16_t"></a> <a id="structapp__sw__feature__t_1a01d8f8453753b4341c50d0047c4f90f2"></a> uint16\_t sw\_pwr\_off\_key\_time
    :   Not used

    <a id="_CPPv4N16app_sw_feature_t22enter_pairing_key_timeE"></a>

    <a id="_CPPv3N16app_sw_feature_t22enter_pairing_key_timeE"></a> <a id="_CPPv2N16app_sw_feature_t22enter_pairing_key_timeE"></a> <a id="app_sw_feature_t::enter_pairing_key_time__uint16_t"></a> <a id="structapp__sw__feature__t_1a68e2fe005c275a0bf21c88c62a77108f"></a> uint16\_t enter\_pairing\_key\_time
    :   toolkit \- sys pram- power on/off setting \- enter paring time(unit:10ms)

    <a id="_CPPv4N16app_sw_feature_t11a2dp_rf_pwrE"></a>

    <a id="_CPPv3N16app_sw_feature_t11a2dp_rf_pwrE"></a> <a id="_CPPv2N16app_sw_feature_t11a2dp_rf_pwrE"></a> <a id="app_sw_feature_t::a2dp_rf_pwr__app_rfpwr_t"></a> <a id="structapp__sw__feature__t_1a4dffe6388c65092a0467ab63f02b9b4e"></a> [app\_rfpwr\_t](#_CPPv411app_rfpwr_t "app_rfpwr_t") a2dp\_rf\_pwr
    :   toolkit \- feature \- rf function/freq offset \- a2dp mode

    <a id="_CPPv4N16app_sw_feature_t10hfp_rf_pwrE"></a>

    <a id="_CPPv3N16app_sw_feature_t10hfp_rf_pwrE"></a> <a id="_CPPv2N16app_sw_feature_t10hfp_rf_pwrE"></a> <a id="app_sw_feature_t::hfp_rf_pwr__app_rfpwr_t"></a> <a id="structapp__sw__feature__t_1adae900aae0f58a30b839891c1213f899"></a> [app\_rfpwr\_t](#_CPPv411app_rfpwr_t "app_rfpwr_t") hfp\_rf\_pwr
    :   toolkit \- feature \- rf function/freq offset \- hfp mode

    <a id="_CPPv4N16app_sw_feature_t17bat_display_levelE"></a>

    <a id="_CPPv3N16app_sw_feature_t17bat_display_levelE"></a> <a id="_CPPv2N16app_sw_feature_t17bat_display_levelE"></a> <a id="app_sw_feature_t::bat_display_level__app_bat_display_t"></a> <a id="structapp__sw__feature__t_1aaa08acbd114bec4d4fbefaf9870c2f9c"></a> [app\_bat\_display\_t](#_CPPv417app_bat_display_t "app_bat_display_t") bat\_display\_level
    :   toolkit \- feature \- battery level display setting \- battery percent-value pair table

    <a id="_CPPv4N16app_sw_feature_t14tester_bt_addrE"></a>

    <a id="_CPPv3N16app_sw_feature_t14tester_bt_addrE"></a> <a id="_CPPv2N16app_sw_feature_t14tester_bt_addrE"></a> <a id="app_sw_feature_t::tester_bt_addr__btif_bd_addr_t"></a> <a id="structapp__sw__feature__t_1a1135ca37561850c7295c0caf10c1becc"></a> [btif\_bd\_addr\_t](../../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") tester\_bt\_addr
    :   Not used

    <a id="_CPPv4N16app_sw_feature_t7dig_volE"></a>

    <a id="_CPPv3N16app_sw_feature_t7dig_volE"></a> <a id="_CPPv2N16app_sw_feature_t7dig_volE"></a> <a id="app_sw_feature_t::dig_vol__app_env_dig_vol_t"></a> <a id="structapp__sw__feature__t_1a7849e88346d7509bbe55fb5835ea075c"></a> [app\_env\_dig\_vol\_t](#_CPPv417app_env_dig_vol_t "app_env_dig_vol_t") dig\_vol
    :   toolkit \- feature \- value setting \- digital voltage

    <a id="_CPPv4N16app_sw_feature_t7ana_volE"></a>

    <a id="_CPPv3N16app_sw_feature_t7ana_volE"></a> <a id="_CPPv2N16app_sw_feature_t7ana_volE"></a> <a id="app_sw_feature_t::ana_vol__app_env_ana_vol_t"></a> <a id="structapp__sw__feature__t_1a6deb872795748d2b652fbf6bbc51792f"></a> [app\_env\_ana\_vol\_t](#_CPPv417app_env_ana_vol_t "app_env_ana_vol_t") ana\_vol
    :   toolkit \- feature \- value setting \- analog voltage

    <a id="_CPPv4N16app_sw_feature_t7tws_eirE"></a>

    <a id="_CPPv3N16app_sw_feature_t7tws_eirE"></a> <a id="_CPPv2N16app_sw_feature_t7tws_eirE"></a> <a id="app_sw_feature_t::tws_eir__uint8_t"></a> <a id="structapp__sw__feature__t_1a977ecbd3253973bf4d16e0ecf71bf5da"></a> uint8\_t tws\_eir
    :   toolkit \- feature \- value setting \- tws earphone icon

    <a id="_CPPv4N16app_sw_feature_t10saradc_volE"></a>

    <a id="_CPPv3N16app_sw_feature_t10saradc_volE"></a> <a id="_CPPv2N16app_sw_feature_t10saradc_volE"></a> <a id="app_sw_feature_t::saradc_vol__app_saradc_vol_t"></a> <a id="structapp__sw__feature__t_1a2ba38d1d8ff40464063e946716cbc56f"></a> [app\_saradc\_vol\_t](#_CPPv416app_saradc_vol_t "app_saradc_vol_t") saradc\_vol
    :   toolkit \- button train

    <a id="_CPPv4N16app_sw_feature_t14audio_eq_indexE"></a>

    <a id="_CPPv3N16app_sw_feature_t14audio_eq_indexE"></a> <a id="_CPPv2N16app_sw_feature_t14audio_eq_indexE"></a> <a id="app_sw_feature_t::audio_eq_index__uint8_t"></a> <a id="structapp__sw__feature__t_1abcf6ed170970eee7926a82a3da005ef4"></a> uint8\_t audio\_eq\_index
    :   toolkit \- audio eq \- EQ enable \- index

<a id="_CPPv417_app_hints_info_s"></a>

<a id="_CPPv317_app_hints_info_s"></a> <a id="_CPPv217_app_hints_info_s"></a> <a id="_app_hints_info_s"></a> <a id="struct__app__hints__info__s"></a> struct \_app\_hints\_info\_s
:   hints information data struct definition

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N17_app_hints_info_s10page_indexE"></a>

    <a id="_CPPv3N17_app_hints_info_s10page_indexE"></a> <a id="_CPPv2N17_app_hints_info_s10page_indexE"></a> <a id="_app_hints_info_s::page_index__uint16_t"></a> <a id="struct__app__hints__info__s_1a75c1334221784e76eb5b5069ac12c03d"></a> uint16\_t page\_index
    :   page index for hints data in flash

<a id="_CPPv413app_env_cfg_t"></a>

<a id="_CPPv313app_env_cfg_t"></a> <a id="_CPPv213app_env_cfg_t"></a> <a id="app_env_cfg_t"></a> <a id="structapp__env__cfg__t"></a> struct app\_env\_cfg\_t
:   system environment configure data struct definition

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N13app_env_cfg_t10valid_flagE"></a>

    <a id="_CPPv3N13app_env_cfg_t10valid_flagE"></a> <a id="_CPPv2N13app_env_cfg_t10valid_flagE"></a> <a id="app_env_cfg_t::valid_flag__int8_t"></a> <a id="structapp__env__cfg__t_1ae1bac861a23f01f36282f38ab7868f7f"></a> int8\_t valid\_flag
    :   flag for valid or not

    <a id="_CPPv4N13app_env_cfg_t11system_paraE"></a>

    <a id="_CPPv3N13app_env_cfg_t11system_paraE"></a> <a id="_CPPv2N13app_env_cfg_t11system_paraE"></a> <a id="app_env_cfg_t::system_para__app_sys_para_t"></a> <a id="structapp__env__cfg__t_1a2ac7843251eb1ae1130b7a0b509a9c77"></a> [app\_sys\_para\_t](#_CPPv414app_sys_para_t "app_sys_para_t") system\_para
    :   system parameter settings

    <a id="_CPPv4N13app_env_cfg_t7bt_paraE"></a>

    <a id="_CPPv3N13app_env_cfg_t7bt_paraE"></a> <a id="_CPPv2N13app_env_cfg_t7bt_paraE"></a> <a id="app_env_cfg_t::bt_para__app_bt_para_t"></a> <a id="structapp__env__cfg__t_1a98804dc8f5165a78096a01c7a5e03d30"></a> [app\_bt\_para\_t](#_CPPv413app_bt_para_t "app_bt_para_t") bt\_para
    :   BT parameter settings

    <a id="_CPPv4N13app_env_cfg_t8ble_paraE"></a>

    <a id="_CPPv3N13app_env_cfg_t8ble_paraE"></a> <a id="_CPPv2N13app_env_cfg_t8ble_paraE"></a> <a id="app_env_cfg_t::ble_para__app_ble_para_t"></a> <a id="structapp__env__cfg__t_1a86477b872d02e74fd2267f292d66be1e"></a> [app\_ble\_para\_t](#_CPPv414app_ble_para_t "app_ble_para_t") ble\_para
    :   BLE parameter settings

    <a id="_CPPv4N13app_env_cfg_t13wave_lang_selE"></a>

    <a id="_CPPv3N13app_env_cfg_t13wave_lang_selE"></a> <a id="_CPPv2N13app_env_cfg_t13wave_lang_selE"></a> <a id="app_env_cfg_t::wave_lang_sel__uint8_t"></a> <a id="structapp__env__cfg__t_1ad13369ff8d85b5b806337bbcb5efec5e"></a> uint8\_t wave\_lang\_sel
    :   using language for hints

    <a id="_CPPv4N13app_env_cfg_t7led_mapE"></a>

    <a id="_CPPv3N13app_env_cfg_t7led_mapE"></a> <a id="_CPPv2N13app_env_cfg_t7led_mapE"></a> <a id="app_env_cfg_t::led_map__uint8_tA"></a> <a id="structapp__env__cfg__t_1a143f81e37a2107c02cb912cca8be892e"></a> uint8\_t led\_map\[LED\_NUM\]
    :   GPIO index for LED

    <a id="_CPPv4N13app_env_cfg_t8led_infoE"></a>

    <a id="_CPPv3N13app_env_cfg_t8led_infoE"></a> <a id="_CPPv2N13app_env_cfg_t8led_infoE"></a> <a id="app_env_cfg_t::led_info__app_led_info_tA"></a> <a id="structapp__env__cfg__t_1a5300f102ec6db4140783bcca832a9786"></a> [app\_led\_info\_t](../app_component/app_led.md#_CPPv414app_led_info_t "app_led_info_t") led\_info\[LED\_EVENT\_NUM\]
    :   LED event behavior setting

    <a id="_CPPv4N13app_env_cfg_t11button_paraE"></a>

    <a id="_CPPv3N13app_env_cfg_t11button_paraE"></a> <a id="_CPPv2N13app_env_cfg_t11button_paraE"></a> <a id="app_env_cfg_t::button_para__app_button_para_t"></a> <a id="structapp__env__cfg__t_1a0d7945d0ba20be30cd6d4b2e81ca8516"></a> [app\_button\_para\_t](../app_component/app_button.md#_CPPv417app_button_para_t "app_button_para_t") button\_para
    :   button trigger threshold setting

    <a id="_CPPv4N13app_env_cfg_t11button_codeE"></a>

    <a id="_CPPv3N13app_env_cfg_t11button_codeE"></a> <a id="_CPPv2N13app_env_cfg_t11button_codeE"></a> <a id="app_env_cfg_t::button_code__uint64_tA"></a> <a id="structapp__env__cfg__t_1a5d5812f1c41cb94de5ee5b1588698a36"></a> uint64\_t button\_code\[[BUTTON\_BT\_END](../app_component/app_button.md#_CPPv4NUt1_413BUTTON_BT_ENDE "[anonymous]::BUTTON_BT_END")\]
    :   button trigger condition setting

    <a id="_CPPv4N13app_env_cfg_t6aud_eqE"></a>

    <a id="_CPPv3N13app_env_cfg_t6aud_eqE"></a> <a id="_CPPv2N13app_env_cfg_t6aud_eqE"></a> <a id="app_env_cfg_t::aud_eq__app_aud_eq_tA"></a> <a id="structapp__env__cfg__t_1a24859816e24aef4e546c9bf307ec5830"></a> [app\_aud\_eq\_t](#_CPPv412app_aud_eq_t "app_aud_eq_t") aud\_eq\[APP\_ENV\_AUDIOEQ\_DEF\_CNT\]
    :   EQ settings

    <a id="_CPPv4N13app_env_cfg_t7hfp_cfgE"></a>

    <a id="_CPPv3N13app_env_cfg_t7hfp_cfgE"></a> <a id="_CPPv2N13app_env_cfg_t7hfp_cfgE"></a> <a id="app_env_cfg_t::hfp_cfg__app_hfp_cfg_t"></a> <a id="structapp__env__cfg__t_1a3f202f8463b166cfbf3d0508bb9a890a"></a> [app\_hfp\_cfg\_t](#_CPPv413app_hfp_cfg_t "app_hfp_cfg_t") hfp\_cfg
    :   call relevant configure setting

    <a id="_CPPv4N13app_env_cfg_t3drcE"></a>

    <a id="_CPPv3N13app_env_cfg_t3drcE"></a> <a id="_CPPv2N13app_env_cfg_t3drcE"></a> <a id="app_env_cfg_t::drc__app_drc_para_t"></a> <a id="structapp__env__cfg__t_1a9287c205369e51035ea7608e8cb7fa9e"></a> [app\_drc\_para\_t](#_CPPv414app_drc_para_t "app_drc_para_t") drc
    :   DRC relevant configure setting

    <a id="_CPPv4N13app_env_cfg_t7featureE"></a>

    <a id="_CPPv3N13app_env_cfg_t7featureE"></a> <a id="_CPPv2N13app_env_cfg_t7featureE"></a> <a id="app_env_cfg_t::feature__app_sw_feature_t"></a> <a id="structapp__env__cfg__t_1a006f4304fe4a03f616d1305bf35e0c86"></a> [app\_sw\_feature\_t](#_CPPv416app_sw_feature_t "app_sw_feature_t") feature
    :   software features setting

    <a id="_CPPv4N13app_env_cfg_t10hints_infoE"></a>

    <a id="_CPPv3N13app_env_cfg_t10hints_infoE"></a> <a id="_CPPv2N13app_env_cfg_t10hints_infoE"></a> <a id="app_env_cfg_t::hints_info__app_hints_info_tAA"></a> <a id="structapp__env__cfg__t_1a22699b0634e8c79137e0623f52fa65e7"></a> [app\_hints\_info\_t](#_CPPv416app_hints_info_t "app_hints_info_t") hints\_info\[APP\_HINTS\_LANGS\_CNT\_MAX\]\[[WAVE\_END](#_CPPv4N15WAVE_EVENT_LIST8WAVE_ENDE "WAVE_END") \- 1\]
    :   hints information

<a id="_CPPv418app_env_data_hdr_t"></a>

<a id="_CPPv318app_env_data_hdr_t"></a> <a id="_CPPv218app_env_data_hdr_t"></a> <a id="app_env_data_hdr_t"></a> <a id="structapp__env__data__hdr__t"></a> struct app\_env\_data\_hdr\_t
:   environment header data struct definition

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18app_env_data_hdr_t5magicE"></a>

    <a id="_CPPv3N18app_env_data_hdr_t5magicE"></a> <a id="_CPPv2N18app_env_data_hdr_t5magicE"></a> <a id="app_env_data_hdr_t::magic__uint32_t"></a> <a id="structapp__env__data__hdr__t_1af17d77f1e47c90d88d83a691da378faf"></a> uint32\_t magic
    :   magic words

    <a id="_CPPv4N18app_env_data_hdr_t5crc32E"></a>

    <a id="_CPPv3N18app_env_data_hdr_t5crc32E"></a> <a id="_CPPv2N18app_env_data_hdr_t5crc32E"></a> <a id="app_env_data_hdr_t::crc32__uint32_t"></a> <a id="structapp__env__data__hdr__t_1a3ba360f3dd9deb012fd018bcef2fe849"></a> uint32\_t crc32
    :   CRC value

    <a id="_CPPv4N18app_env_data_hdr_t7versionE"></a>

    <a id="_CPPv3N18app_env_data_hdr_t7versionE"></a> <a id="_CPPv2N18app_env_data_hdr_t7versionE"></a> <a id="app_env_data_hdr_t::version__uint32_t"></a> <a id="structapp__env__data__hdr__t_1a8b5d3edb118d33c2c1594c450d8f4f70"></a> uint32\_t version
    :   version value

    <a id="_CPPv4N18app_env_data_hdr_t8data_lenE"></a>

    <a id="_CPPv3N18app_env_data_hdr_t8data_lenE"></a> <a id="_CPPv2N18app_env_data_hdr_t8data_lenE"></a> <a id="app_env_data_hdr_t::data_len__uint32_t"></a> <a id="structapp__env__data__hdr__t_1abcb7cbad8bb1ff5a74ec2938a7fc6054"></a> uint32\_t data\_len
    :   data length

<a id="_CPPv423app_env_data_sys_info_t"></a>

<a id="_CPPv323app_env_data_sys_info_t"></a> <a id="_CPPv223app_env_data_sys_info_t"></a> <a id="app_env_data_sys_info_t"></a> <a id="structapp__env__data__sys__info__t"></a> struct app\_env\_data\_sys\_info\_t
:   sysyem environment information data struct definition

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N23app_env_data_sys_info_t8lang_selE"></a>

    <a id="_CPPv3N23app_env_data_sys_info_t8lang_selE"></a> <a id="_CPPv2N23app_env_data_sys_info_t8lang_selE"></a> <a id="app_env_data_sys_info_t::lang_sel__uint8_t"></a> <a id="structapp__env__data__sys__info__t_1a03e3cd193f6aeeeff67c9f1d968a6955"></a> uint8\_t lang\_sel
    :   using language

    <a id="_CPPv4N23app_env_data_sys_info_t11eq_lang_selE"></a>

    <a id="_CPPv3N23app_env_data_sys_info_t11eq_lang_selE"></a> <a id="_CPPv2N23app_env_data_sys_info_t11eq_lang_selE"></a> <a id="app_env_data_sys_info_t::eq_lang_sel__uint8_t"></a> <a id="structapp__env__data__sys__info__t_1ac0697697f50391a42cfc210a09908ddb"></a> uint8\_t eq\_lang\_sel
    :   EQ using language

    <a id="_CPPv4N23app_env_data_sys_info_t8reservedE"></a>

    <a id="_CPPv3N23app_env_data_sys_info_t8reservedE"></a> <a id="_CPPv2N23app_env_data_sys_info_t8reservedE"></a> <a id="app_env_data_sys_info_t::reserved__uint8_tA"></a> <a id="structapp__env__data__sys__info__t_1add76c9647536d5bbd3283ca9b8c2e62f"></a> uint8\_t reserved\[15\]
    :   not used

<a id="_CPPv423app_env_data_tws_info_t"></a>

<a id="_CPPv323app_env_data_tws_info_t"></a> <a id="_CPPv223app_env_data_tws_info_t"></a> <a id="app_env_data_tws_info_t"></a> <a id="structapp__env__data__tws__info__t"></a> struct app\_env\_data\_tws\_info\_t
:   TWS environment information data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N23app_env_data_tws_info_t8tws_addrE"></a>

    <a id="_CPPv3N23app_env_data_tws_info_t8tws_addrE"></a> <a id="_CPPv2N23app_env_data_tws_info_t8tws_addrE"></a> <a id="app_env_data_tws_info_t::tws_addr__btif_bd_addr_t"></a> <a id="structapp__env__data__tws__info__t_1a8ecba6f746c68605e69c15e4cffbc133"></a> [btif\_bd\_addr\_t](../../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") tws\_addr
    :   TWS MAC address

    <a id="_CPPv4N23app_env_data_tws_info_t8lk_vaildE"></a>

    <a id="_CPPv3N23app_env_data_tws_info_t8lk_vaildE"></a> <a id="_CPPv2N23app_env_data_tws_info_t8lk_vaildE"></a> <a id="app_env_data_tws_info_t::lk_vaild__uint8_t"></a> <a id="structapp__env__data__tws__info__t_1a2e4b55fc45cf84ce83bf5fe4e1a839cb"></a> uint8\_t lk\_vaild
    :   flag for link key valid or not

    <a id="_CPPv4N23app_env_data_tws_info_t2lkE"></a>

    <a id="_CPPv3N23app_env_data_tws_info_t2lkE"></a> <a id="_CPPv2N23app_env_data_tws_info_t2lkE"></a> <a id="app_env_data_tws_info_t::lk__btif_lk_t"></a> <a id="structapp__env__data__tws__info__t_1a80f2ba05c5f7b8cd3a3e0ebbd68cd8c9"></a> [btif\_lk\_t](../../../btif/btif_type.md#_CPPv49btif_lk_t "btif_lk_t") lk
    :   data buffer for link key value

    <a id="_CPPv4N23app_env_data_tws_info_t8reservedE"></a>

    <a id="_CPPv3N23app_env_data_tws_info_t8reservedE"></a> <a id="_CPPv2N23app_env_data_tws_info_t8reservedE"></a> <a id="app_env_data_tws_info_t::reserved__uint8_tA"></a> <a id="structapp__env__data__tws__info__t_1a53f99f3927cccd7844eb55bd6cc5a1e3"></a> uint8\_t reserved\[16\]
    :   not used

    <a id="_CPPv4N23app_env_data_tws_info_t7ear_posE"></a>

    <a id="_CPPv3N23app_env_data_tws_info_t7ear_posE"></a> <a id="_CPPv2N23app_env_data_tws_info_t7ear_posE"></a> <a id="app_env_data_tws_info_t::ear_pos__uint8_t"></a> <a id="structapp__env__data__tws__info__t_1a33c75a33eb6b19cdeee27deb95b9efdf"></a> uint8\_t ear\_pos
    :   TWS right size or left size @left\_right\_t

<a id="_CPPv424app_env_data_bt_record_t"></a>

<a id="_CPPv324app_env_data_bt_record_t"></a> <a id="_CPPv224app_env_data_bt_record_t"></a> <a id="app_env_data_bt_record_t"></a> <a id="structapp__env__data__bt__record__t"></a> struct app\_env\_data\_bt\_record\_t
:   BT record informaiton data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N24app_env_data_bt_record_t12record_countE"></a>

    <a id="_CPPv3N24app_env_data_bt_record_t12record_countE"></a> <a id="_CPPv2N24app_env_data_bt_record_t12record_countE"></a> <a id="app_env_data_bt_record_t::record_count__uint32_t"></a> <a id="structapp__env__data__bt__record__t_1a7837acce5e47b71c84c6e3bcabe396ee"></a> uint32\_t record\_count
    :   reoced count

    <a id="_CPPv4N24app_env_data_bt_record_t6recordE"></a>

    <a id="_CPPv3N24app_env_data_bt_record_t6recordE"></a> <a id="_CPPv2N24app_env_data_bt_record_t6recordE"></a> <a id="app_env_data_bt_record_t::record__btif_bt_dev_info_tA"></a> <a id="structapp__env__data__bt__record__t_1ab38a2d4f1e6c75c277f5fd1c89692330"></a> [btif\_bt\_dev\_info\_t](../../../btif/btif_type.md#_CPPv418btif_bt_dev_info_t "btif_bt_dev_info_t") record\[APP\_ENV\_DATA\_BT\_RECORD\_COUNT\_MAX\]
    :   remote BT device information data

<a id="_CPPv425app_env_data_ble_record_t"></a>

<a id="_CPPv325app_env_data_ble_record_t"></a> <a id="_CPPv225app_env_data_ble_record_t"></a> <a id="app_env_data_ble_record_t"></a> <a id="structapp__env__data__ble__record__t"></a> struct app\_env\_data\_ble\_record\_t
:   BLE record informaiton data struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N25app_env_data_ble_record_t12record_countE"></a>

    <a id="_CPPv3N25app_env_data_ble_record_t12record_countE"></a> <a id="_CPPv2N25app_env_data_ble_record_t12record_countE"></a> <a id="app_env_data_ble_record_t::record_count__uint32_t"></a> <a id="structapp__env__data__ble__record__t_1ac4e71480008b1c338b002898428e01d3"></a> uint32\_t record\_count
    :   reoced count

    <a id="_CPPv4N25app_env_data_ble_record_t6recordE"></a>

    <a id="_CPPv3N25app_env_data_ble_record_t6recordE"></a> <a id="_CPPv2N25app_env_data_ble_record_t6recordE"></a> <a id="app_env_data_ble_record_t::record__btif_ble_dev_info_tA"></a> <a id="structapp__env__data__ble__record__t_1a1c0bf821ea22343aafaefa8ba7787001"></a> [btif\_ble\_dev\_info\_t](../../../btif/btif_type.md#_CPPv419btif_ble_dev_info_t "btif_ble_dev_info_t") record\[APP\_ENV\_DATA\_BLE\_RECORD\_COUNT\_MAX\]
    :   remote BT device information data

<a id="_CPPv413assert_info_t"></a>

<a id="_CPPv313assert_info_t"></a> <a id="_CPPv213assert_info_t"></a> <a id="assert_info_t"></a> <a id="structassert__info__t"></a> struct assert\_info\_t
:   assert information data struct

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N13assert_info_t12assert_validE"></a>

    <a id="_CPPv3N13assert_info_t12assert_validE"></a> <a id="_CPPv2N13assert_info_t12assert_validE"></a> <a id="assert_info_t::assert_valid__b"></a> <a id="structassert__info__t_1af60e84d26d8b9dde236d90a7f0e7239d"></a> bool assert\_valid
    :   flag for assert dump data valid or not

    <a id="_CPPv4N13assert_info_t11assert_funcE"></a>

    <a id="_CPPv3N13assert_info_t11assert_funcE"></a> <a id="_CPPv2N13assert_info_t11assert_funcE"></a> <a id="assert_info_t::assert_func__cA"></a> <a id="structassert__info__t_1ac8a272631c0842836be25a2ab8a7d2f6"></a> char assert\_func\[APP\_ENV\_ASSERT\_FILE\_LEN\_MAX\]
    :   function name

    <a id="_CPPv4N13assert_info_t11assert_lineE"></a>

    <a id="_CPPv3N13assert_info_t11assert_lineE"></a> <a id="_CPPv2N13assert_info_t11assert_lineE"></a> <a id="assert_info_t::assert_line__uint16_t"></a> <a id="structassert__info__t_1a2e1c239ebb2cb4494603a8f3ec12c557"></a> uint16\_t assert\_line
    :   line number

    <a id="_CPPv4N13assert_info_t7param_1E"></a>

    <a id="_CPPv3N13assert_info_t7param_1E"></a> <a id="_CPPv2N13assert_info_t7param_1E"></a> <a id="assert_info_t::param_1__uint32_t"></a> <a id="structassert__info__t_1a0c55127f12f618b5d40c61893a9795f3"></a> uint32\_t param\_1
    :   parameter 1

    <a id="_CPPv4N13assert_info_t7param_2E"></a>

    <a id="_CPPv3N13assert_info_t7param_2E"></a> <a id="_CPPv2N13assert_info_t7param_2E"></a> <a id="assert_info_t::param_2__uint32_t"></a> <a id="structassert__info__t_1ab5646c911e8e33df0eccc89063d94cb4"></a> uint32\_t param\_2
    :   parameter 2

    <a id="_CPPv4N13assert_info_t9assert_lrE"></a>

    <a id="_CPPv3N13assert_info_t9assert_lrE"></a> <a id="_CPPv2N13assert_info_t9assert_lrE"></a> <a id="assert_info_t::assert_lr__uint32_t"></a> <a id="structassert__info__t_1a4503a9272c003704d018bc480403fe59"></a> uint32\_t assert\_lr
    :   link register

    <a id="_CPPv4N13assert_info_t3ctxE"></a>

    <a id="_CPPv3N13assert_info_t3ctxE"></a> <a id="_CPPv2N13assert_info_t3ctxE"></a> <a id="assert_info_t::ctx__asssert_ctx_t"></a> <a id="structassert__info__t_1abc723bb9f6929deac18d5ac0970b5539"></a> asssert\_ctx\_t ctx
    :   register data struct

<a id="_CPPv414charger_info_t"></a>

<a id="_CPPv314charger_info_t"></a> <a id="_CPPv214charger_info_t"></a> <a id="charger_info_t"></a> <a id="structcharger__info__t"></a> struct charger\_info\_t
:   charger relevant information data struct definition

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N14charger_info_t18charger_info_validE"></a>

    <a id="_CPPv3N14charger_info_t18charger_info_validE"></a> <a id="_CPPv2N14charger_info_t18charger_info_validE"></a> <a id="charger_info_t::charger_info_valid__b"></a> <a id="structcharger__info__t_1ae90a6f5fe09ec872415fa9dd5c534370"></a> bool charger\_info\_valid
    :   flag for information valid or not

    <a id="_CPPv4N14charger_info_t15usb_level_stateE"></a>

    <a id="_CPPv3N14charger_info_t15usb_level_stateE"></a> <a id="_CPPv2N14charger_info_t15usb_level_stateE"></a> <a id="charger_info_t::usb_level_state__uint8_t"></a> <a id="structcharger__info__t_1a45f91a09c99b497546340685b10772be"></a> uint8\_t usb\_level\_state
    :   usb level @drv\_pmu\_usb\_voltage\_e

    <a id="_CPPv4N14charger_info_t7pd_typeE"></a>

    <a id="_CPPv3N14charger_info_t7pd_typeE"></a> <a id="_CPPv2N14charger_info_t7pd_typeE"></a> <a id="charger_info_t::pd_type__uint8_t"></a> <a id="structcharger__info__t_1ab88b50f9aa178f9f267d77de836a02e4"></a> uint8\_t pd\_type
    :   power down type index

    <a id="_CPPv4N14charger_info_t15current_voltageE"></a>

    <a id="_CPPv3N14charger_info_t15current_voltageE"></a> <a id="_CPPv2N14charger_info_t15current_voltageE"></a> <a id="charger_info_t::current_voltage__uint16_t"></a> <a id="structcharger__info__t_1a7e4a453114c35d429004a94db0c94420"></a> uint16\_t current\_voltage
    :   current voltage

<a id="_CPPv414app_env_data_t"></a>

<a id="_CPPv314app_env_data_t"></a> <a id="_CPPv214app_env_data_t"></a> <a id="app_env_data_t"></a> <a id="structapp__env__data__t"></a> struct app\_env\_data\_t
:   system environment information data struct definition

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N14app_env_data_t8data_hdrE"></a>

    <a id="_CPPv3N14app_env_data_t8data_hdrE"></a> <a id="_CPPv2N14app_env_data_t8data_hdrE"></a> <a id="app_env_data_t::data_hdr__app_env_data_hdr_t"></a> <a id="structapp__env__data__t_1acd71a4e9d57484d3a6716ec54efd880f"></a> [app\_env\_data\_hdr\_t](#_CPPv418app_env_data_hdr_t "app_env_data_hdr_t") data\_hdr
    :   environment header data

    <a id="_CPPv4N14app_env_data_t8sys_infoE"></a>

    <a id="_CPPv3N14app_env_data_t8sys_infoE"></a> <a id="_CPPv2N14app_env_data_t8sys_infoE"></a> <a id="app_env_data_t::sys_info__app_env_data_sys_info_t"></a> <a id="structapp__env__data__t_1adec8f1030db2a8f975631d4472b19768"></a> [app\_env\_data\_sys\_info\_t](#_CPPv423app_env_data_sys_info_t "app_env_data_sys_info_t") sys\_info
    :   sysyem environment information

    <a id="_CPPv4N14app_env_data_t8tws_infoE"></a>

    <a id="_CPPv3N14app_env_data_t8tws_infoE"></a> <a id="_CPPv2N14app_env_data_t8tws_infoE"></a> <a id="app_env_data_t::tws_info__app_env_data_tws_info_t"></a> <a id="structapp__env__data__t_1a7b7d6acdf050300926b6cc0e45e14080"></a> [app\_env\_data\_tws\_info\_t](#_CPPv423app_env_data_tws_info_t "app_env_data_tws_info_t") tws\_info
    :   TWS environment information

    <a id="_CPPv4N14app_env_data_t9bt_recordE"></a>

    <a id="_CPPv3N14app_env_data_t9bt_recordE"></a> <a id="_CPPv2N14app_env_data_t9bt_recordE"></a> <a id="app_env_data_t::bt_record__app_env_data_bt_record_t"></a> <a id="structapp__env__data__t_1a083b8a10eee3a6c96947433f466627b7"></a> [app\_env\_data\_bt\_record\_t](#_CPPv424app_env_data_bt_record_t "app_env_data_bt_record_t") bt\_record
    :   BT record informaiton

    <a id="_CPPv4N14app_env_data_t10ble_recordE"></a>

    <a id="_CPPv3N14app_env_data_t10ble_recordE"></a> <a id="_CPPv2N14app_env_data_t10ble_recordE"></a> <a id="app_env_data_t::ble_record__app_env_data_ble_record_t"></a> <a id="structapp__env__data__t_1a3eadfa5f778b7a3274a0ffb0bdf6b052"></a> [app\_env\_data\_ble\_record\_t](#_CPPv425app_env_data_ble_record_t "app_env_data_ble_record_t") ble\_record
    :   BLE record informaiton

    <a id="_CPPv4N14app_env_data_t11assert_infoE"></a>

    <a id="_CPPv3N14app_env_data_t11assert_infoE"></a> <a id="_CPPv2N14app_env_data_t11assert_infoE"></a> <a id="app_env_data_t::assert_info__assert_info_t"></a> <a id="structapp__env__data__t_1ad8215a829f0a3e437091ef1126ae3467"></a> [assert\_info\_t](#_CPPv413assert_info_t "assert_info_t") assert\_info
    :   assert information

    <a id="_CPPv4N14app_env_data_t12charger_infoE"></a>

    <a id="_CPPv3N14app_env_data_t12charger_infoE"></a> <a id="_CPPv2N14app_env_data_t12charger_infoE"></a> <a id="app_env_data_t::charger_info__charger_info_t"></a> <a id="structapp__env__data__t_1ae4839ee97f0219ec629c6ac394cfebb6"></a> [charger\_info\_t](#_CPPv414charger_info_t "charger_info_t") charger\_info
    :   charger information

<a id="_CPPv49app_env_t"></a>

<a id="_CPPv39app_env_t"></a> <a id="_CPPv29app_env_t"></a> <a id="app_env_t"></a> <a id="structapp__env__t"></a> struct app\_env\_t
:   system environment information and configre data struct definition

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N9app_env_t8env_dataE"></a>

    <a id="_CPPv3N9app_env_t8env_dataE"></a> <a id="_CPPv2N9app_env_t8env_dataE"></a> <a id="app_env_t::env_data__app_env_data_t"></a> <a id="structapp__env__t_1a0b8b07811485b9783c5cfa13a9e436ef"></a> [app\_env\_data\_t](#_CPPv414app_env_data_t "app_env_data_t") env\_data
    :   system environment information data

    <a id="_CPPv4N9app_env_t7env_cfgE"></a>

    <a id="_CPPv3N9app_env_t7env_cfgE"></a> <a id="_CPPv2N9app_env_t7env_cfgE"></a> <a id="app_env_t::env_cfg__app_env_cfg_t"></a> <a id="structapp__env__t_1ae3fb728da1ca4892276a0ace71d7f463"></a> [app\_env\_cfg\_t](#_CPPv413app_env_cfg_t "app_env_cfg_t") env\_cfg
    :   system environment configure data

<a id="macros"></a>

### Macros

<a id="c.APP_ENV_ASSERT_FILE_LEN_MAX"></a>

<a id="app__env_8h_1ac59f1f63e0f31f4eb0b37321b1779a32"></a> APP\_ENV\_ASSERT\_FILE\_LEN\_MAX

<a id="c.APP_ENV_DATA_BT_RECORD_COUNT_MAX"></a>

<a id="app__env_8h_1a1b0e62f44f73dc04ac369ed0ace47172"></a> APP\_ENV\_DATA\_BT\_RECORD\_COUNT\_MAX

<a id="c.APP_ENV_DATA_BLE_RECORD_COUNT_MAX"></a>

<a id="app__env_8h_1a1cb2a5b161dbc71af49dcd29a2f4172c"></a> APP\_ENV\_DATA\_BLE\_RECORD\_COUNT\_MAX

<a id="c.APP_ENV_CFG_NAME_LEN_MAX"></a>

<a id="app__env_8h_1aea444e3266192283fb7fe51ec5941074"></a> APP\_ENV\_CFG\_NAME\_LEN\_MAX

<a id="c.APP_ENV_VOL_LEVEL_CNT_MAX"></a>

<a id="app__env_8h_1a4880f57d2cb510eb5ed2b3af94c9c5a8"></a> APP\_ENV\_VOL\_LEVEL\_CNT\_MAX

<a id="c.APP_HINTS_LANGS_CNT_MAX"></a>

<a id="app__env_8h_1a53bda1dcc55bf082e352a9996e447cbc"></a> APP\_HINTS\_LANGS\_CNT\_MAX

<a id="c.APP_ENV_AUDIOEQ_DEF_CNT"></a>

<a id="app__env_8h_1a8763287d84236a313140cdb97d78d805"></a> APP\_ENV\_AUDIOEQ\_DEF\_CNT

<a id="c.APP_ENV_CFG_AT_FLASH_ADDR"></a>

<a id="app__env_8h_1a5190f17274e5f90eb6a0b43258ef3dd0"></a> APP\_ENV\_CFG\_AT\_FLASH\_ADDR

<a id="c.APP_ENV_DATA_AT_FLASH_ADDR"></a>

<a id="app__env_8h_1aac429f94d864e694c2b4a20e73bbe9cc"></a> APP\_ENV\_DATA\_AT\_FLASH\_ADDR

<a id="c.APP_ENV_CALI_AT_FLASH_ADDR"></a>

<a id="app__env_8h_1a0c6c8c79c351fd458560a87254a037ab"></a> APP\_ENV\_CALI\_AT\_FLASH\_ADDR

<a id="c.APP_ENV_END_AT_FLASH_ADDR"></a>

<a id="app__env_8h_1a1b2dab84be910e39c939e150019c67c8"></a> APP\_ENV\_END\_AT\_FLASH\_ADDR

<a id="c.BT_MODE_1V1"></a>

<a id="app__env_8h_1a334aab7043a2f1c0a85261301a12bf32"></a> BT\_MODE\_1V1

<a id="c.BT_MODE_1V2"></a>

<a id="app__env_8h_1afc840a0301a914aaa38813aa5793a8a5"></a> BT\_MODE\_1V2

<a id="c.BT_MODE_TWS"></a>

<a id="app__env_8h_1adae94f6f071b1d646908c1d9911b334e"></a> BT\_MODE\_TWS

<a id="c.BT_MODE"></a>

<a id="app__env_8h_1a303782a453ab4f77117ae0e7ca8ea133"></a> BT\_MODE

<a id="c.APP_ENV_SYS_FLAG_UARTDBG"></a>

<a id="app__env_8h_1ab4cd58f0db5ee8f5602c1eea3b1e2176"></a> APP\_ENV\_SYS\_FLAG\_UARTDBG
:   toolkit \- feature \- debug setting

<a id="c.APP_ENV_SYS_FLAG_IIC"></a>

<a id="app__env_8h_1abebef7cc667e40951c1040065f0d2fbf"></a> APP\_ENV\_SYS\_FLAG\_IIC

<a id="c.APP_ENV_SYS_FLAG_A2DP_SRC"></a>

<a id="app__env_8h_1a0af1fe075f68d4110eb3855d011248ba"></a> APP\_ENV\_SYS\_FLAG\_A2DP\_SRC
:   toolkit \- feature \- A2DP SRC

<a id="c.APP_ENV_SYS_FLAG_AGHFP"></a>

<a id="app__env_8h_1a7cbe19fd10b2790aefe84a55f795f287"></a> APP\_ENV\_SYS\_FLAG\_AGHFP
:   toolkit \- feature \- HFP AG

<a id="c.APP_ENV_SYS_FLAG_DAC_DIFFER"></a>

<a id="app__env_8h_1a989d8f0400cec8b182df06ef04b74a56"></a> APP\_ENV\_SYS\_FLAG\_DAC\_DIFFER
:   toolkit \- audio base setting \- audio output(0: Single-Ended 1:Differential)

<a id="c.APP_ENV_SYS_FLAG_L_is_LplusR"></a>

<a id="app__env_8h_1ad4e7c92b71ed7c78f642ef9d20145f22"></a> APP\_ENV\_SYS\_FLAG\_L\_is\_LplusR
:   toolkit \- feature \- Audio\=L\+R

<a id="c.APP_ENV_SYS_FLAG_LED_REVERSE"></a>

<a id="app__env_8h_1a4b2dc119e57686c81e043e8956201658"></a> APP\_ENV\_SYS\_FLAG\_LED\_REVERSE
:   toolkit \- LED \- output reverse

<a id="c.APP_ENV_SYS_FLAG_SD_DETECT_ENA"></a>

<a id="app__env_8h_1a9267819781b2b79b6edbffbbe3d74e89"></a> APP\_ENV\_SYS\_FLAG\_SD\_DETECT\_ENA
:   toolkit \- feature \- SD card detect enable

<a id="c.APP_ENV_SYS_FLAG_AD_LINEIN_ENA"></a>

<a id="app__env_8h_1a2ff22958e39096a5fdd9444bc459a2b6"></a> APP\_ENV\_SYS\_FLAG\_AD\_LINEIN\_ENA
:   toolkit \- feature \- line in detect enable

<a id="c.APP_ENV_SYS_FLAG_USB_ENA"></a>

<a id="app__env_8h_1ad5ef98308e451e136121f43091c1a1f8"></a> APP\_ENV\_SYS\_FLAG\_USB\_ENA
:   toolkit \- feature \- USB enable

<a id="c.APP_ENV_SYS_FLAG_MIC_BIAS"></a>

<a id="app__env_8h_1a12af45dac04a0c03bce6a7b7eda585a5"></a> APP\_ENV\_SYS\_FLAG\_MIC\_BIAS
:   toolket \- audio base setting \- Mic bias vol 0:1.8V 1:2.1V 2:2.4V 3:2.6V

<a id="c.APP_ENV_SYS_FLAG_DEFAULT"></a>

<a id="app__env_8h_1a466de1dc98a1b833d8d11e67e6bba213"></a> APP\_ENV\_SYS\_FLAG\_DEFAULT

<a id="c.APP_ENV_BT_FLAG_A2DP"></a>

<a id="app__env_8h_1ab146e682b6b97425826aef3e5e62a948"></a> APP\_ENV\_BT\_FLAG\_A2DP
:   toolkit \- feature \- enable \- A2DP enable

<a id="c.APP_ENV_BT_FLAG_HFP"></a>

<a id="app__env_8h_1a8f9610ae4178be51a6bc0f133dce4840"></a> APP\_ENV\_BT\_FLAG\_HFP
:   toolkit \- feature \- enable \- HFP enable

<a id="c.APP_ENV_BT_FLAG_PBAP"></a>

<a id="app__env_8h_1a69eb1d0493b42a23b692d27f857d48aa"></a> APP\_ENV\_BT\_FLAG\_PBAP
:   toolkit \- feature \- enable \- PBAP enable

<a id="c.APP_ENV_BT_FLAG_AUTO_CONN"></a>

<a id="app__env_8h_1a8db907f888c2724769caec63b768136a"></a> APP\_ENV\_BT\_FLAG\_AUTO\_CONN
:   toolkit \- sys param \- power on reconnect \- enable

<a id="c.APP_ENV_BT_FLAG_RECOV"></a>

<a id="app__env_8h_1aebf0a21feee845b0de3971750f37dbc6"></a> APP\_ENV\_BT\_FLAG\_RECOV
:   toolkit \- sys param \- reconnect \- enable

<a id="c.APP_ENV_BT_FLAG_ADDR_POLL"></a>

<a id="app__env_8h_1a008057b72a4033a74d4353634ff45a02"></a> APP\_ENV\_BT\_FLAG\_ADDR\_POLL
:   toolkit \- sys param \- power on reconnect \- reconnect addr poll

<a id="c.APP_ENV_BT_FLAG_ADDR_AUDIO_DIAL"></a>

<a id="app__env_8h_1a1e809618682d215bb48c4c70e542d2eb"></a> APP\_ENV\_BT\_FLAG\_ADDR\_AUDIO\_DIAL
:   toolkit \- feature \- enable \- dial audio report

<a id="c.APP_ENV_BT_FLAG_AUTO_CONN_PERIOD"></a>

<a id="app__env_8h_1a956565dfe5a0657c1508612a4787728e"></a> APP\_ENV\_BT\_FLAG\_AUTO\_CONN\_PERIOD
:   toolkit \- sys param \- power on reconnect \- Periodic reconnect

<a id="c.APP_ENV_BT_FLAG_APP_BAT_DISPLAY"></a>

<a id="app__env_8h_1a63eb5bd19233c829f4874a2e968e042d"></a> APP\_ENV\_BT\_FLAG\_APP\_BAT\_DISPLAY
:   toolkit \- feature \- battery level display setting

<a id="c.APP_ENV_BT_FLAG_DEFAULT"></a>

<a id="app__env_8h_1a5498644d3c7c23c8535e0b9ef70771d5"></a> APP\_ENV\_BT\_FLAG\_DEFAULT

<a id="c.APP_ENV_FEATURE_FLAG_INQUIRY_ALWAYS"></a>

<a id="app__env_8h_1a7a22b7d68224a6f66978c250cdb73cf3"></a> APP\_ENV\_FEATURE\_FLAG\_INQUIRY\_ALWAYS
:   toolkit \- feature \- enable \- power on start both-scan

<a id="c.APP_ENV_FEATURE_FLAG_DIG_BUCK_ENABLE"></a>

<a id="app__env_8h_1a9b47a45b07ccad0df9e5a38328883b82"></a> APP\_ENV\_FEATURE\_FLAG\_DIG\_BUCK\_ENABLE
:   toolkit \- feature \- value setting \- digital buck val enable

<a id="c.APP_ENV_FEATURE_FLAG_ANA_BUCK_ENABLE"></a>

<a id="app__env_8h_1a99ddcaa84e361718604c63792d8767d9"></a> APP\_ENV\_FEATURE\_FLAG\_ANA\_BUCK\_ENABLE
:   toolkit \- feature \- value setting \- analog buck val enable

<a id="c.APP_ENV_FEATURE_FLAG_CHARGEING_LOW_I_Vusb"></a>

<a id="app__env_8h_1af2b433ef691357783ec2baf36461ac49"></a> APP\_ENV\_FEATURE\_FLAG\_CHARGEING\_LOW\_I\_Vusb
:   toolkit \- feature \- enable \- charging enter deep sleep

<a id="c.APP_ENV_FEATURE_FLAG_FREE_CONN"></a>

<a id="app__env_8h_1a4d77536d8e24cee6e8a00e06a62cd1b2"></a> APP\_ENV\_FEATURE\_FLAG\_FREE\_CONN
:   toolkit \- feature \- enable \- free paring

<a id="c.APP_ENV_FEATURE_FLAG_CHARGE_MODE_PWR_DOWN"></a>

<a id="app__env_8h_1a35c1f59d367a175b18166063ff4245ce"></a> APP\_ENV\_FEATURE\_FLAG\_CHARGE\_MODE\_PWR\_DOWN
:   toolkit \- feature \- enable \- power off when charging

<a id="c.APP_ENV_FEATURE_FLAG_MIC_SINGLE_ENABLE"></a>

<a id="app__env_8h_1aeebcdc52bc66b9f75f39ab0d270cc141"></a> APP\_ENV\_FEATURE\_FLAG\_MIC\_SINGLE\_ENABLE
:   toolket \- audio base setting \- mic input(1: Single-Ended 0:Differential)

<a id="c.APP_ENV_FEATURE_FLAG_DAC_DC_COMPENSATION"></a>

<a id="app__env_8h_1ae5af5bf7b68a5beb6d4e7e53c7a214c6"></a> APP\_ENV\_FEATURE\_FLAG\_DAC\_DC\_COMPENSATION
:   toolket \- audio base setting \- mic input

<a id="c.APP_ENV_FEATURE_FLAG_KEY_LOW_ACTIVE"></a>

<a id="app__env_8h_1afffc6e80d4d1f561056ef27152b9d402"></a> APP\_ENV\_FEATURE\_FLAG\_KEY\_LOW\_ACTIVE

<a id="c.APP_ENV_FEATURE_FLAG_DISABLE_IOS_INCOMING_RING"></a>

<a id="app__env_8h_1a734593e8c4948e7edfe78f26da10992a"></a> APP\_ENV\_FEATURE\_FLAG\_DISABLE\_IOS\_INCOMING\_RING
:   toolkit \- feature \- enable \- disable in-band ring

<a id="c.APP_ENV_FEATURE_FLAG_VOLUME_RESTORE"></a>

<a id="app__env_8h_1a76e1e1f6fee40f4decb420463984e803"></a> APP\_ENV\_FEATURE\_FLAG\_VOLUME\_RESTORE
:   Not used

<a id="c.APP_ENV_FEATURE_FLAG_VOLUME_SYNC"></a>

<a id="app__env_8h_1ac5ecb98a02bb6e57b1340bf68c3897f7"></a> APP\_ENV\_FEATURE\_FLAG\_VOLUME\_SYNC
:   toolkit \- feature \- enable \- volume sync

<a id="c.APP_ENV_FEATURE_FLAG_PAIRING_AFTER_PWR_ON"></a>

<a id="app__env_8h_1a1262508354780a4fd76b5dae37e65c90"></a> APP\_ENV\_FEATURE\_FLAG\_PAIRING\_AFTER\_PWR\_ON
:   toolkit \- sys param \- power on/off setting \- Long press enter paring mode

<a id="c.APP_ENV_FEATURE_FLAG_SPP_PROFILE"></a>

<a id="app__env_8h_1a36b9c51b80902c080edf1888ef9e7c80"></a> APP\_ENV\_FEATURE\_FLAG\_SPP\_PROFILE
:   toolkit \- feature \- enable \- SPP

<a id="c.APP_ENV_FEATURE_FLAG_HID_PROFILE"></a>

<a id="app__env_8h_1afbe2b9bc0ca8e32568567d07dd3120ca"></a> APP\_ENV\_FEATURE\_FLAG\_HID\_PROFILE
:   toolkit \- feature \- enable \- HID

<a id="c.APP_ENV_FEATURE_FLAG_AEC_ENABLE"></a>

<a id="app__env_8h_1aa7eb68e90b49da1b8aa4821611fb8981"></a> APP\_ENV\_FEATURE\_FLAG\_AEC\_ENABLE
:   toolkit \- call setting \- aec test \- enable

<a id="c.APP_ENV_FEATURE_FLAG_TWS_L_R_PWR_DOWN"></a>

<a id="app__env_8h_1a9f526ebc5ceca67cffee5db2aba798ca"></a> APP\_ENV\_FEATURE\_FLAG\_TWS\_L\_R\_PWR\_DOWN
:   toolkit \- feature \- enable \- power down when left \& right key sync-press

<a id="c.APP_ENV_FEATURE_FLAG_AAC_ENABLE"></a>

<a id="app__env_8h_1a338b7f4176d5ace97403b88184e3d9ec"></a> APP\_ENV\_FEATURE\_FLAG\_AAC\_ENABLE
:   toolkit \- feature \- enable \- AAC Enable

<a id="c.APP_ENV_FEATURE_FLAG_SLEEP_ENABLE"></a>

<a id="app__env_8h_1a080d00c8790b0569cb1c962ccda10c3d"></a> APP\_ENV\_FEATURE\_FLAG\_SLEEP\_ENABLE
:   toolkit \- feature \- enable \- sleep

<a id="c.APP_ENV_FEATURE_FLAG_FAST_MUTE"></a>

<a id="app__env_8h_1a8a3c3c7cc23b690ab91b71c49fa300d8"></a> APP\_ENV\_FEATURE\_FLAG\_FAST\_MUTE
:   toolkit \- feature \- enable \- auto mute in BT\_mode

<a id="c.APP_ENV_FEATURE_FLAG_TWS_L_R_DIF_EN"></a>

<a id="app__env_8h_1aa54ccfd445c6cea5db6830d2dc9b581d"></a> APP\_ENV\_FEATURE\_FLAG\_TWS\_L\_R\_DIF\_EN
:   toolkit \- feature \- value\_setting \- Distinguish between left and ring earsids.

<a id="c.APP_ENV_FEATURE_FLAG_TWS_L"></a>

<a id="app__env_8h_1a8fea559b3a35fb87103d58983c443ba8"></a> APP\_ENV\_FEATURE\_FLAG\_TWS\_L
:   toolkit \- feature \- value\_setting \- 1: left side 0: right side

<a id="c.APP_ENV_FEATURE_FLAG_POP_EN"></a>

<a id="app__env_8h_1a8731f3b9b8f6b6e874821f71891d97f2"></a> APP\_ENV\_FEATURE\_FLAG\_POP\_EN
:   toolkit \- feature \- enable \- Pop-up prompt

<a id="c.APP_ENV_FEATURE_FLAG_MAX_BITPOOL"></a>

<a id="app__env_8h_1af6cf1f527dd145e41227230542afba06"></a> APP\_ENV\_FEATURE\_FLAG\_MAX\_BITPOOL
:   toolkit \- feature \- enable \- high fidelity

<a id="c.APP_ENV_FEATURE_FLAG_UPDATE_BT_NAME"></a>

<a id="app__env_8h_1a92e4ab5efec61e32f47102941047e22f"></a> APP\_ENV\_FEATURE\_FLAG\_UPDATE\_BT\_NAME
:   toolkit \- feature \- enable \- Update BT name

<a id="c.APP_ENV_FEATURE_FLAG_TESTER"></a>

<a id="app__env_8h_1ab3ff8bdcbfdf7e8ec4351ba993c924ac"></a> APP\_ENV\_FEATURE\_FLAG\_TESTER
:   toolkit \- feature \- enable \- product test(5V communicat)

<a id="c.APP_ENV_FEATURE_FLAG_ANA_LOW_VOLT"></a>

<a id="app__env_8h_1ad7c0d7cc045ed64023f8e051f54e73a2"></a> APP\_ENV\_FEATURE\_FLAG\_ANA\_LOW\_VOLT
:   toolkit \- feature \- value setting \- analog buck val setting(1: 1.6V 0:1.8V)

<a id="c.APP_ENV_FEATURE_FLAG_CHARGER_HIGH_VOLTAGE"></a>

<a id="app__env_8h_1a84addd8fd3d1e98c14761185a23626ae"></a> APP\_ENV\_FEATURE\_FLAG\_CHARGER\_HIGH\_VOLTAGE
:   toolkit \- feature \- enable \- charging to high val(4.35V)

<a id="c.APP_ENV_DEATURE_FLAG_DEFAULT"></a>

<a id="app__env_8h_1a58f9124e900548809099029f9f9e32c3"></a> APP\_ENV\_DEATURE\_FLAG\_DEFAULT

<a id="c.APP_ENV_LE_FLAG_LE_ENABLE"></a>

<a id="app__env_8h_1a1370d565e6126813a806a6665ca203d2"></a> APP\_ENV\_LE\_FLAG\_LE\_ENABLE
:   toolkit \- sys param \- BLE seting \- ble enable

<a id="c.APP_ENV_LE_FLAG_ADDR_NAME_CONFIG_ENABLE"></a>

<a id="app__env_8h_1ab74e7aaa3c03980e015e5b06a73cd2df"></a> APP\_ENV\_LE\_FLAG\_ADDR\_NAME\_CONFIG\_ENABLE
:   toolkit \- sys param \- BLE setting \- le address \& name config

<a id="c.APP_ENV_LE_FLAG_ADV_CONFIG_ENABLE"></a>

<a id="app__env_8h_1ae7d15e0a0f08a36e10cbc80e02b31eb4"></a> APP\_ENV\_LE\_FLAG\_ADV\_CONFIG\_ENABLE
:   toolkit \- sys param \- BLE setting \- BLE ADV setting

<a id="c.APP_ENV_LE_FLAG_UPDATE_CONFIG_ENABLE"></a>

<a id="app__env_8h_1a94aaf8f13fe2724a0e202afe89de5df6"></a> APP\_ENV\_LE\_FLAG\_UPDATE\_CONFIG\_ENABLE
:   toolkit \- sys param \- BLE setting \- BLE update connect para setting

<a id="c.APP_ENV_LE_FLAG_LE_AUDIO_ENABLE"></a>

<a id="app__env_8h_1a1b5478181570a1e6dcf895d8a60302fe"></a> APP\_ENV\_LE\_FLAG\_LE\_AUDIO\_ENABLE
:   toolkit \- sys param \- BLE setting \- LE Audio

<a id="c.APP_ENV_LE_FLAG_MAX_TRAN_LATENCY_ENABLE"></a>

<a id="app__env_8h_1aed721bd79c9db13f4e08beaea93bc9d5"></a> APP\_ENV\_LE\_FLAG\_MAX\_TRAN\_LATENCY\_ENABLE
:   toolkit \- sys param \- BLE setting \- MaxTransLatency

<a id="c.APP_ENV_LE_FLAG_PREF_PRESENTATION_DELAY_ENABLE"></a>

<a id="app__env_8h_1a7329d3113a28b4a6c3c8eccd9813d6f3"></a> APP\_ENV\_LE\_FLAG\_PREF\_PRESENTATION\_DELAY\_ENABLE
:   toolkit \- sys param \- BLE setting \- Pref Delay

<a id="c.APP_ENV_LE_FLAG_SUPP_PRESENTATION_DELAY_ENABLE"></a>

<a id="app__env_8h_1aa1d7b32d61ba8b206f5e5cd0d1c85aff"></a> APP\_ENV\_LE\_FLAG\_SUPP\_PRESENTATION\_DELAY\_ENABLE
:   toolkit \- sys param \- BLE setting \- Supp Delay

<a id="c.APP_ENV_MIC_ANA_GAIN_9P5_DB"></a>

<a id="app__env_8h_1ab0cf89ff0e68a1f79d0cfc8438d66f2b"></a> APP\_ENV\_MIC\_ANA\_GAIN\_9P5\_DB

<a id="c.APP_ENV_MIC_ANA_GAIN_11P3_DB"></a>

<a id="app__env_8h_1aaf92c885f7762d9c4db9c8daf53247ec"></a> APP\_ENV\_MIC\_ANA\_GAIN\_11P3\_DB

<a id="c.APP_ENV_MIC_ANA_GAIN_13P1_DB"></a>

<a id="app__env_8h_1a0fecb9c06b5a1602931af8c10e260bfd"></a> APP\_ENV\_MIC\_ANA\_GAIN\_13P1\_DB

<a id="c.APP_ENV_MIC_ANA_GAIN_14P9_DB"></a>

<a id="app__env_8h_1aa744f2ce629826406e980d207be265ba"></a> APP\_ENV\_MIC\_ANA\_GAIN\_14P9\_DB

<a id="c.APP_ENV_MIC_ANA_GAIN_16P7_DB"></a>

<a id="app__env_8h_1ac46c173e54da84284ab5e69c7161c227"></a> APP\_ENV\_MIC\_ANA\_GAIN\_16P7\_DB

<a id="c.APP_ENV_MIC_ANA_GAIN_18P5_DB"></a>

<a id="app__env_8h_1a25080c8ab4bd58620653b13fc9da7481"></a> APP\_ENV\_MIC\_ANA\_GAIN\_18P5\_DB

<a id="c.APP_ENV_MIC_ANA_GAIN_20P3_DB"></a>

<a id="app__env_8h_1aed4183ead8b12eaf8335dd5216066be0"></a> APP\_ENV\_MIC\_ANA\_GAIN\_20P3\_DB

<a id="c.APP_ENV_MIC_ANA_GAIN_22P2_DB"></a>

<a id="app__env_8h_1ac980d05f308b6630e70af31ae7fa5b9a"></a> APP\_ENV\_MIC\_ANA\_GAIN\_22P2\_DB

<a id="c.APP_ENV_MIC_ANA_GAIN_24P0_DB"></a>

<a id="app__env_8h_1a149a370271df9554388178effa9af9f9"></a> APP\_ENV\_MIC\_ANA\_GAIN\_24P0\_DB

<a id="c.APP_ENV_MIC_ANA_GAIN_25P8_DB"></a>

<a id="app__env_8h_1a6c9c2a6734d2b59173df7d9bcba426d7"></a> APP\_ENV\_MIC\_ANA\_GAIN\_25P8\_DB

<a id="c.APP_ENV_MIC_ANA_GAIN_27P6_DB"></a>

<a id="app__env_8h_1a37224a057e43522a181133a4aaba827e"></a> APP\_ENV\_MIC\_ANA\_GAIN\_27P6\_DB

<a id="c.APP_ENV_MIC_ANA_GAIN_29P4_DB"></a>

<a id="app__env_8h_1aa6dfcfa0eb7e0c590f60b4b00a0dc057"></a> APP\_ENV\_MIC\_ANA\_GAIN\_29P4\_DB

<a id="c.APP_ENV_MIC_ANA_GAIN_31P2_DB"></a>

<a id="app__env_8h_1a67165c0a8a8e9a5b8890fb44278b21ed"></a> APP\_ENV\_MIC\_ANA\_GAIN\_31P2\_DB

<a id="c.APP_ENV_MIC_ANA_GAIN_33P0_DB"></a>

<a id="app__env_8h_1a4f74c71e4e74a314716d94b3cdba2ffc"></a> APP\_ENV\_MIC\_ANA\_GAIN\_33P0\_DB

<a id="c.APP_ENV_DEV_COD_WEAR_HEADSET"></a>

<a id="app__env_8h_1ad05f804bf60a913502f50d005251ae10"></a> APP\_ENV\_DEV\_COD\_WEAR\_HEADSET

<a id="c.APP_ENV_DEV_COD_HANDSFREE"></a>

<a id="app__env_8h_1a39f572a7ea03d22b68d5cce8d7ca8c9d"></a> APP\_ENV\_DEV\_COD\_HANDSFREE

<a id="c.APP_ENV_DEV_COD_LOUD_SPEAKER"></a>

<a id="app__env_8h_1ad3971a97fc7b45013f3755d57da43d95"></a> APP\_ENV\_DEV\_COD\_LOUD\_SPEAKER

<a id="c.APP_ENV_DEV_COD_HEAD_PHONES"></a>

<a id="app__env_8h_1a1c1b33d7816cdd751dc19f33c8a6342b"></a> APP\_ENV\_DEV\_COD\_HEAD\_PHONES

<a id="c.APP_ENV_DEV_COD_PORT_AUDIO"></a>

<a id="app__env_8h_1a5a84efa00de30940d5e147d60578bc31"></a> APP\_ENV\_DEV\_COD\_PORT\_AUDIO

<a id="c.APP_ENV_DEV_COD_CAR_AUDIO"></a>

<a id="app__env_8h_1a4b7c70ddd57f45124a1036863ccf0a85"></a> APP\_ENV\_DEV\_COD\_CAR\_AUDIO

<a id="c.APP_ENV_RECONN_ACTION_ENTER_PAIRING"></a>

<a id="app__env_8h_1a75525f8cbe42e10d9751c5ba5b7106c0"></a> APP\_ENV\_RECONN\_ACTION\_ENTER\_PAIRING

<a id="c.APP_ENV_RECONN_ACTION_RECONN"></a>

<a id="app__env_8h_1a5d636121fe5467a4468fa9ddc9a39850"></a> APP\_ENV\_RECONN\_ACTION\_RECONN

<a id="c.APP_ENV_BT_AUTO_PD_COND_NOCONN"></a>

<a id="app__env_8h_1a969bc2dc67614ca62c76c8ccae4164cf"></a> APP\_ENV\_BT\_AUTO\_PD\_COND\_NOCONN

<a id="c.APP_ENV_BT_AUTO_PD_COND_PAUSE_TO"></a>

<a id="app__env_8h_1ada331286473de85259c44564f0bf10f4"></a> APP\_ENV\_BT\_AUTO\_PD\_COND\_PAUSE\_TO

<a id="c.APP_ENV_DISCONN_ACTION_W4_PARING"></a>

<a id="app__env_8h_1a29653b711416c8081bab94173349efba"></a> APP\_ENV\_DISCONN\_ACTION\_W4\_PARING

<a id="c.APP_ENV_DISCONN_ACTION_POWERON_RECONN"></a>

<a id="app__env_8h_1a1f14e8e06220f609e329a3ed55e9aca1"></a> APP\_ENV\_DISCONN\_ACTION\_POWERON\_RECONN

<a id="c.APP_ENV_ANA_VOL_1P55"></a>

<a id="app__env_8h_1a815834db6e7300191f0ee4f84ff044d9"></a> APP\_ENV\_ANA\_VOL\_1P55

<a id="c.APP_ENV_ANA_VOL_1P50"></a>

<a id="app__env_8h_1a99db2c684843cba7661fa371a2ce0712"></a> APP\_ENV\_ANA\_VOL\_1P50

<a id="c.APP_ENV_ANA_VOL_1P45"></a>

<a id="app__env_8h_1a0dde97f9418ac30c12cfc6e5f67e3b10"></a> APP\_ENV\_ANA\_VOL\_1P45

<a id="c.APP_ENV_ANA_VOL_1P40"></a>

<a id="app__env_8h_1a21bb5f91aebbf51ccd5bf2e67e9ba6f3"></a> APP\_ENV\_ANA\_VOL\_1P40

<a id="c.APP_ENV_ANA_VOL_1P35"></a>

<a id="app__env_8h_1afbac8726f52e31df267ebd3f62ad9b68"></a> APP\_ENV\_ANA\_VOL\_1P35

<a id="c.APP_ENV_ANA_VOL_1P30"></a>

<a id="app__env_8h_1af487a0a9f861c988e402e6aec87ca8f1"></a> APP\_ENV\_ANA\_VOL\_1P30

<a id="c.APP_ENV_ANA_VOL_1P25"></a>

<a id="app__env_8h_1adbb4a9f6799be98d234d5d22fe7efaa6"></a> APP\_ENV\_ANA\_VOL\_1P25

<a id="c.APP_ENV_ANA_VOL_1P20"></a>

<a id="app__env_8h_1a4d0fa5e98f55cd30dd591176fc81ba52"></a> APP\_ENV\_ANA\_VOL\_1P20

<a id="c.APP_ENV_DIG_VOL_0P60"></a>

<a id="app__env_8h_1ad70bd8ef3e1b54d09357635dc5c8fc05"></a> APP\_ENV\_DIG\_VOL\_0P60

<a id="c.APP_ENV_DIG_VOL_0P65"></a>

<a id="app__env_8h_1afdb5037e1f7bfcaa088424ed9354cab6"></a> APP\_ENV\_DIG\_VOL\_0P65

<a id="c.APP_ENV_DIG_VOL_0P70"></a>

<a id="app__env_8h_1acb3bb834ba91cb2a639499a932ddf814"></a> APP\_ENV\_DIG\_VOL\_0P70

<a id="c.APP_ENV_DIG_VOL_0P75"></a>

<a id="app__env_8h_1a7d5e6305d038f5f5209957cc84d91732"></a> APP\_ENV\_DIG\_VOL\_0P75

<a id="c.APP_ENV_DIG_VOL_0P80"></a>

<a id="app__env_8h_1a73d3aa5936887d76d151167d0a9b0a7d"></a> APP\_ENV\_DIG\_VOL\_0P80

<a id="c.APP_ENV_DIG_VOL_0P85"></a>

<a id="app__env_8h_1a3145f0310386dbb703d280dd0f28062c"></a> APP\_ENV\_DIG\_VOL\_0P85

<a id="c.APP_ENV_DIG_VOL_0P90"></a>

<a id="app__env_8h_1a0682d57cecc89c46eb63ae9f33477d04"></a> APP\_ENV\_DIG\_VOL\_0P90

<a id="c.APP_ENV_DIG_VOL_0P95"></a>

<a id="app__env_8h_1a818f94d012b49a84846826f388bb804f"></a> APP\_ENV\_DIG\_VOL\_0P95

<a id="c.APP_ENC_DRC_ENABLE_ENDRC"></a>

<a id="app__env_8h_1ab80e11816b73ec1680c9622002de1bb4"></a> APP\_ENC\_DRC\_ENABLE\_ENDRC

<a id="c.DEFAULT_BLE_ENABLE"></a>

<a id="app__env_8h_1a069b1bef0293d611bf355662eae6b436"></a> DEFAULT\_BLE\_ENABLE

<a id="c.DEFAULT_ADV_INT"></a>

<a id="app__env_8h_1a7fa0a99e768eab500cc3de175b759f2b"></a> DEFAULT\_ADV\_INT

<a id="c.DEFAULT_CON_UPDATE_INTV"></a>

<a id="app__env_8h_1a68f77c90a210aaf29c6ba20c5c170e28"></a> DEFAULT\_CON\_UPDATE\_INTV

<a id="c.DEFAULT_CON_UPDATE_DELAY"></a>

<a id="app__env_8h_1a8adb2191a506c2c7f7ac732f460fad08"></a> DEFAULT\_CON\_UPDATE\_DELAY

<a id="c.APPL_GA_PREF_MAX_TRANS_LATENCY"></a>

<a id="app__env_8h_1a6b344b94cce283d2a72137b909797dcd"></a> APPL\_GA\_PREF\_MAX\_TRANS\_LATENCY

<a id="c.APPL_GA_PREF_PRESENTATION_DELAY_MIN"></a>

<a id="app__env_8h_1adfe3ab4cba141123b0e760fe1b43a40d"></a> APPL\_GA\_PREF\_PRESENTATION\_DELAY\_MIN

<a id="c.APPL_GA_PREF_PRESENTATION_DELAY_MAX"></a>

<a id="app__env_8h_1a47d929a5201dc48f794cce35d418b8e2"></a> APPL\_GA\_PREF\_PRESENTATION\_DELAY\_MAX

<a id="c.APPL_GA_SUPP_PRESENTATION_DELAY_MIN"></a>

<a id="app__env_8h_1a7e2ab77e5ad58425048d07353631215e"></a> APPL\_GA\_SUPP\_PRESENTATION\_DELAY\_MIN

<a id="c.APPL_GA_SUPP_PRESENTATION_DELAY_MAX"></a>

<a id="app__env_8h_1a3848c074a4929b6a983cc00ed663d519"></a> APPL\_GA\_SUPP\_PRESENTATION\_DELAY\_MAX

<a id="c.APP_ENV_EQ_SR_16000"></a>

<a id="app__env_8h_1a741f3cddb409577eb951bbad12805996"></a> APP\_ENV\_EQ\_SR\_16000

<a id="c.APP_ENV_EQ_SR_44100"></a>

<a id="app__env_8h_1aed3f0676fb42bd1650848bc88a12c542"></a> APP\_ENV\_EQ\_SR\_44100

<a id="c.APP_ENV_EQ_SR_48000"></a>

<a id="app__env_8h_1a0d07cd6a8f09d4a1216a25b12f5b9f96"></a> APP\_ENV\_EQ\_SR\_48000

<a id="c.APP_ENV_EQ_TYPE_AUDIO"></a>

<a id="app__env_8h_1a8ac216856bccd4b5011ebf447f1d0bcd"></a> APP\_ENV\_EQ\_TYPE\_AUDIO

<a id="c.APP_ENV_EQ_TYPE_SPK"></a>

<a id="app__env_8h_1a96535c5a73088d00b3c440dad98a4dc5"></a> APP\_ENV\_EQ\_TYPE\_SPK

<a id="c.APP_ENV_EQ_TYPE_MIC"></a>

<a id="app__env_8h_1a9396eeb081e588243d23a947cedac781"></a> APP\_ENV\_EQ\_TYPE\_MIC

<a id="c.APP_ENV_EQ_EFFECT_CUSTOM"></a>

<a id="app__env_8h_1a1e8921eda76cd9f398afb000694ae126"></a> APP\_ENV\_EQ\_EFFECT\_CUSTOM

<a id="c.APP_ENV_EQ_EFFECT_FLAT"></a>

<a id="app__env_8h_1aa0b6157d56bb75b9487f3d8cac67c2dd"></a> APP\_ENV\_EQ\_EFFECT\_FLAT

<a id="c.APP_ENV_EQ_EFFECT_BOOST"></a>

<a id="app__env_8h_1aac1468855b2c1e5bc502b670aefc214c"></a> APP\_ENV\_EQ\_EFFECT\_BOOST

<a id="c.APP_ENV_EQ_EFFECT_TREBLE"></a>

<a id="app__env_8h_1a3471b90af3db23b1000785e53596fa0a"></a> APP\_ENV\_EQ\_EFFECT\_TREBLE

<a id="c.APP_ENV_EQ_EFFECT_POP"></a>

<a id="app__env_8h_1a711488f91c6f4c40961500802e448e4c"></a> APP\_ENV\_EQ\_EFFECT\_POP

<a id="c.APP_ENV_EQ_EFFECT_ROCK"></a>

<a id="app__env_8h_1a5e4ad435365f949faa62bac04e31a274"></a> APP\_ENV\_EQ\_EFFECT\_ROCK

<a id="c.APP_ENV_EQ_EFFECT_CLASSIC"></a>

<a id="app__env_8h_1a163707c7f9ad75ff7841141b1c6622e8"></a> APP\_ENV\_EQ\_EFFECT\_CLASSIC

<a id="c.APP_ENV_EQ_EFFECT_JAZZ"></a>

<a id="app__env_8h_1aa6bb756bdb8525224a4c161105b0937e"></a> APP\_ENV\_EQ\_EFFECT\_JAZZ

<a id="c.APP_ENV_EQ_EFFECT_DANCE"></a>

<a id="app__env_8h_1a376f4ade4b0802f69bf384890b3a7d6e"></a> APP\_ENV\_EQ\_EFFECT\_DANCE

<a id="c.APP_ENV_EQ_EFFECT_RANDB"></a>

<a id="app__env_8h_1a2f07df9d4bba0c35f0c2e3dee34f0fe6"></a> APP\_ENV\_EQ\_EFFECT\_RANDB

<a id="c.APP_ENV_EQ_FILTER_PKF"></a>

<a id="app__env_8h_1ac76c268dcbfc4fb32273e570079401d7"></a> APP\_ENV\_EQ\_FILTER\_PKF

<a id="c.APP_ENV_EQ_FILTER_LSF"></a>

<a id="app__env_8h_1a2cae3ef481113cea3fb7d160d681d3cc"></a> APP\_ENV\_EQ\_FILTER\_LSF

<a id="c.APP_ENV_EQ_FILTER_HSF"></a>

<a id="app__env_8h_1a0efee562282697f09c56181f5ab19f6a"></a> APP\_ENV\_EQ\_FILTER\_HSF

<a id="c.APP_ENV_EQ_FILTER_LPF"></a>

<a id="app__env_8h_1ad43eb44c8dca93b1aa537ce6cde52439"></a> APP\_ENV\_EQ\_FILTER\_LPF

<a id="c.APP_ENV_EQ_FILTER_HPF"></a>

<a id="app__env_8h_1aab079df85cd9b907b15bc1701fefa52b"></a> APP\_ENV\_EQ\_FILTER\_HPF

<a id="c.APP_ENV_EQ_FILTER_BPF"></a>

<a id="app__env_8h_1a2d28a0003c1072e9be7e332065317f3f"></a> APP\_ENV\_EQ\_FILTER\_BPF

<a id="c.APP_ENV_EQ_FILTER_NTF"></a>

<a id="app__env_8h_1a4428d49d341321e4b096faa6a4d936f5"></a> APP\_ENV\_EQ\_FILTER\_NTF

<a id="c.APP_ENV_EQ_FILTER_APF"></a>

<a id="app__env_8h_1ac0b0914bb081230e738c3cf136491bf9"></a> APP\_ENV\_EQ\_FILTER\_APF

<a id="c.APP_ENV_HINT_CODEC_INTER_FLASH_WAV"></a>

<a id="app__env_8h_1a59b0100287f597ebe71818f03e4eb02f"></a> APP\_ENV\_HINT\_CODEC\_INTER\_FLASH\_WAV

<a id="c.APP_ENV_HINT_CODEC_INTER_FLASH_SBC"></a>

<a id="app__env_8h_1ac0b6c2faa5b8e6b6520fc85110d25301"></a> APP\_ENV\_HINT\_CODEC\_INTER\_FLASH\_SBC

<a id="c.APP_ENV_HINT_CODEC_INTER_FLASH_AMR"></a>

<a id="app__env_8h_1ae2d49156854ea254ca0fbbffa67bf4b3"></a> APP\_ENV\_HINT\_CODEC\_INTER\_FLASH\_AMR

<a id="c.APP_ENV_HINT_CODEC_EXT_FLASH_WAV"></a>

<a id="app__env_8h_1a8e187f4fa71f5604e4fe964374423148"></a> APP\_ENV\_HINT\_CODEC\_EXT\_FLASH\_WAV

<a id="c.APP_ENV_HINT_CODEC_EXT_FLASH_SBC"></a>

<a id="app__env_8h_1a836d3562140a8efd20b1641b0a228917"></a> APP\_ENV\_HINT\_CODEC\_EXT\_FLASH\_SBC

<a id="c.APP_ENV_HINT_CODEC_EXT_FLASH_AMR"></a>

<a id="app__env_8h_1a0865937634d5554ad9cc44298d21e954"></a> APP\_ENV\_HINT\_CODEC\_EXT\_FLASH\_AMR

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv49bt_mode_t"></a>

<a id="_CPPv39bt_mode_t"></a> <a id="_CPPv29bt_mode_t"></a> <a id="bt_mode_t"></a> <a id="app__env_8h_1aad20a10431bbf48eef853f65af8ca3fb"></a> typedef uint16\_t bt\_mode\_t
:   BT mode value definition.

<a id="_CPPv418app_env_sys_flag_t"></a>

<a id="_CPPv318app_env_sys_flag_t"></a> <a id="_CPPv218app_env_sys_flag_t"></a> <a id="app_env_sys_flag_t"></a> <a id="app__env_8h_1a1c76d112595e4ec68abbb0f65a82b0a3"></a> typedef uint32\_t app\_env\_sys\_flag\_t
:   system environment bitmap definition

<a id="_CPPv417app_env_bt_flag_t"></a>

<a id="_CPPv317app_env_bt_flag_t"></a> <a id="_CPPv217app_env_bt_flag_t"></a> <a id="app_env_bt_flag_t"></a> <a id="app__env_8h_1a100df2ec6cc802a667e381fde10bc2b0"></a> typedef uint32\_t app\_env\_bt\_flag\_t
:   bluetooth environment bitmap definition

<a id="_CPPv419app_env_feat_flag_t"></a>

<a id="_CPPv319app_env_feat_flag_t"></a> <a id="_CPPv219app_env_feat_flag_t"></a> <a id="app_env_feat_flag_t"></a> <a id="app__env_8h_1a39c7637219281ce19649e317f9709efd"></a> typedef uint32\_t app\_env\_feat\_flag\_t
:   feature environment bitmap definition

<a id="_CPPv417app_env_le_flag_t"></a>

<a id="_CPPv317app_env_le_flag_t"></a> <a id="_CPPv217app_env_le_flag_t"></a> <a id="app_env_le_flag_t"></a> <a id="app__env_8h_1a1a64dd93751320a3c68bc6fd706ea194"></a> typedef uint16\_t app\_env\_le\_flag\_t
:   BLE environment bitmap definition.

<a id="_CPPv422app_env_mic_ana_gain_t"></a>

<a id="_CPPv322app_env_mic_ana_gain_t"></a> <a id="_CPPv222app_env_mic_ana_gain_t"></a> <a id="app_env_mic_ana_gain_t"></a> <a id="app__env_8h_1a4d768882a1dddda47ab8f13b52dacb4f"></a> typedef uint8\_t app\_env\_mic\_ana\_gain\_t
:   MIC analog gain setting index defintion.

<a id="_CPPv417app_env_dev_cod_t"></a>

<a id="_CPPv317app_env_dev_cod_t"></a> <a id="_CPPv217app_env_dev_cod_t"></a> <a id="app_env_dev_cod_t"></a> <a id="app__env_8h_1acc92416dc54aed3b07901c3f7411d78b"></a> typedef uint8\_t app\_env\_dev\_cod\_t
:   class of device index definition

<a id="_CPPv423app_env_reconn_action_t"></a>

<a id="_CPPv323app_env_reconn_action_t"></a> <a id="_CPPv223app_env_reconn_action_t"></a> <a id="app_env_reconn_action_t"></a> <a id="app__env_8h_1abdaf99511d496119eaaabfce384684e4"></a> typedef int8\_t app\_env\_reconn\_action\_t
:   bluetooth re-connection action definition

<a id="_CPPv422app_env_auto_pd_cond_t"></a>

<a id="_CPPv322app_env_auto_pd_cond_t"></a> <a id="_CPPv222app_env_auto_pd_cond_t"></a> <a id="app_env_auto_pd_cond_t"></a> <a id="app__env_8h_1a241ce13b9475b23bb1e86924f48cffd9"></a> typedef uint8\_t app\_env\_auto\_pd\_cond\_t
:   auto power down condtion setting index definition

<a id="_CPPv424app_env_disconn_action_t"></a>

<a id="_CPPv324app_env_disconn_action_t"></a> <a id="_CPPv224app_env_disconn_action_t"></a> <a id="app_env_disconn_action_t"></a> <a id="app__env_8h_1a5028a3262c2235a5dab0df6cab9f6957"></a> typedef uint8\_t app\_env\_disconn\_action\_t
:   action after disconnecting with remote device index definition

<a id="_CPPv417app_env_ana_vol_t"></a>

<a id="_CPPv317app_env_ana_vol_t"></a> <a id="_CPPv217app_env_ana_vol_t"></a> <a id="app_env_ana_vol_t"></a> <a id="app__env_8h_1ab3efba55343f4aa1f3542048bc8f3997"></a> typedef uint8\_t app\_env\_ana\_vol\_t
:   environment analog voltage index definition

<a id="_CPPv417app_env_dig_vol_t"></a>

<a id="_CPPv317app_env_dig_vol_t"></a> <a id="_CPPv217app_env_dig_vol_t"></a> <a id="app_env_dig_vol_t"></a> <a id="app__env_8h_1a061b703e30a4facb7a8d90cfd447767b"></a> typedef uint8\_t app\_env\_dig\_vol\_t
:   environment digital voltage index definition

<a id="_CPPv415app_env_eq_sr_t"></a>

<a id="_CPPv315app_env_eq_sr_t"></a> <a id="_CPPv215app_env_eq_sr_t"></a> <a id="app_env_eq_sr_t"></a> <a id="app__env_8h_1ada0a97f67790fa32377cd1ce01a1c2a8"></a> typedef uint8\_t app\_env\_eq\_sr\_t
:   EQ simping rate index defintion.

<a id="_CPPv417app_env_eq_type_t"></a>

<a id="_CPPv317app_env_eq_type_t"></a> <a id="_CPPv217app_env_eq_type_t"></a> <a id="app_env_eq_type_t"></a> <a id="app__env_8h_1ac19d1dcee6af7e6e5790446d938f32a6"></a> typedef uint8\_t app\_env\_eq\_type\_t
:   EQ type index definition.

<a id="_CPPv419app_env_eq_effect_t"></a>

<a id="_CPPv319app_env_eq_effect_t"></a> <a id="_CPPv219app_env_eq_effect_t"></a> <a id="app_env_eq_effect_t"></a> <a id="app__env_8h_1a55c675de2c3400b66272ea3e0a8ae3b8"></a> typedef uint8\_t app\_env\_eq\_effect\_t
:   EQ default effect configured index definition.

<a id="_CPPv419app_env_eq_filter_t"></a>

<a id="_CPPv319app_env_eq_filter_t"></a> <a id="_CPPv219app_env_eq_filter_t"></a> <a id="app_env_eq_filter_t"></a> <a id="app__env_8h_1a1813dfaafbf95cbdde2b34e191373cb8"></a> typedef uint8\_t app\_env\_eq\_filter\_t
:   EQ filter type index definition.

<a id="_CPPv420app_env_hint_codec_t"></a>

<a id="_CPPv320app_env_hint_codec_t"></a> <a id="_CPPv220app_env_hint_codec_t"></a> <a id="app_env_hint_codec_t"></a> <a id="app__env_8h_1affc05f2bc3a4afb4e865f11ad0d037b0"></a> typedef uint8\_t app\_env\_hint\_codec\_t
:   hints codec type index definition

<a id="_CPPv416app_hints_info_t"></a>

<a id="_CPPv316app_hints_info_t"></a> <a id="_CPPv216app_hints_info_t"></a> <a id="app_hints_info_t"></a> <a id="app__env_8h_1a6a77f84bf567f832eb71573f35b8fb66"></a> typedef struct [\_app\_hints\_info\_s](#_CPPv417_app_hints_info_s "_app_hints_info_s") app\_hints\_info\_t
:   hints information data struct definition

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv426app_env_charging_current_t"></a>

<a id="_CPPv326app_env_charging_current_t"></a> <a id="_CPPv226app_env_charging_current_t"></a> <a id="app__env_8h_1a1dd879e99738420342b4ca96376dd186"></a> enum app\_env\_charging\_current\_t
:   charging current index defintion

    *Values:*

    <a id="_CPPv4N26app_env_charging_current_t18CHARGING_CURR_20MAE"></a>

    <a id="_CPPv3N26app_env_charging_current_t18CHARGING_CURR_20MAE"></a> <a id="_CPPv2N26app_env_charging_current_t18CHARGING_CURR_20MAE"></a> <a id="app__env_8h_1a1dd879e99738420342b4ca96376dd186a1147634625e0b6d1c31b7c9e9acf2140"></a> enumerator CHARGING\_CURR\_20MA

    <a id="_CPPv4N26app_env_charging_current_t18CHARGING_CURR_30MAE"></a>

    <a id="_CPPv3N26app_env_charging_current_t18CHARGING_CURR_30MAE"></a> <a id="_CPPv2N26app_env_charging_current_t18CHARGING_CURR_30MAE"></a> <a id="app__env_8h_1a1dd879e99738420342b4ca96376dd186a3627ce7d248720a2aa1a1f8fc11d2ffe"></a> enumerator CHARGING\_CURR\_30MA

    <a id="_CPPv4N26app_env_charging_current_t18CHARGING_CURR_40MAE"></a>

    <a id="_CPPv3N26app_env_charging_current_t18CHARGING_CURR_40MAE"></a> <a id="_CPPv2N26app_env_charging_current_t18CHARGING_CURR_40MAE"></a> <a id="app__env_8h_1a1dd879e99738420342b4ca96376dd186aceda86fbada661869fa469635c4cc456"></a> enumerator CHARGING\_CURR\_40MA

    <a id="_CPPv4N26app_env_charging_current_t18CHARGING_CURR_50MAE"></a>

    <a id="_CPPv3N26app_env_charging_current_t18CHARGING_CURR_50MAE"></a> <a id="_CPPv2N26app_env_charging_current_t18CHARGING_CURR_50MAE"></a> <a id="app__env_8h_1a1dd879e99738420342b4ca96376dd186adca82c9f5cd8e0b70a6ce866c5b0aa40"></a> enumerator CHARGING\_CURR\_50MA

    <a id="_CPPv4N26app_env_charging_current_t18CHARGING_CURR_60MAE"></a>

    <a id="_CPPv3N26app_env_charging_current_t18CHARGING_CURR_60MAE"></a> <a id="_CPPv2N26app_env_charging_current_t18CHARGING_CURR_60MAE"></a> <a id="app__env_8h_1a1dd879e99738420342b4ca96376dd186ad43c4d4ec397bbcd1c353f9652d3ee12"></a> enumerator CHARGING\_CURR\_60MA

    <a id="_CPPv4N26app_env_charging_current_t18CHARGING_CURR_70MAE"></a>

    <a id="_CPPv3N26app_env_charging_current_t18CHARGING_CURR_70MAE"></a> <a id="_CPPv2N26app_env_charging_current_t18CHARGING_CURR_70MAE"></a> <a id="app__env_8h_1a1dd879e99738420342b4ca96376dd186add1d39654b75e25c9a197ae1f0a42768"></a> enumerator CHARGING\_CURR\_70MA

    <a id="_CPPv4N26app_env_charging_current_t18CHARGING_CURR_80MAE"></a>

    <a id="_CPPv3N26app_env_charging_current_t18CHARGING_CURR_80MAE"></a> <a id="_CPPv2N26app_env_charging_current_t18CHARGING_CURR_80MAE"></a> <a id="app__env_8h_1a1dd879e99738420342b4ca96376dd186a137b59f17710d4833cb25e9b9b1045ef"></a> enumerator CHARGING\_CURR\_80MA

    <a id="_CPPv4N26app_env_charging_current_t18CHARGING_CURR_90MAE"></a>

    <a id="_CPPv3N26app_env_charging_current_t18CHARGING_CURR_90MAE"></a> <a id="_CPPv2N26app_env_charging_current_t18CHARGING_CURR_90MAE"></a> <a id="app__env_8h_1a1dd879e99738420342b4ca96376dd186aa9019d7bfcd66e12fe65d1d003347e55"></a> enumerator CHARGING\_CURR\_90MA

    <a id="_CPPv4N26app_env_charging_current_t19CHARGING_CURR_100MAE"></a>

    <a id="_CPPv3N26app_env_charging_current_t19CHARGING_CURR_100MAE"></a> <a id="_CPPv2N26app_env_charging_current_t19CHARGING_CURR_100MAE"></a> <a id="app__env_8h_1a1dd879e99738420342b4ca96376dd186a044fde7aa7e8eff000f90c80bb69d95b"></a> enumerator CHARGING\_CURR\_100MA

    <a id="_CPPv4N26app_env_charging_current_t19CHARGING_CURR_110MAE"></a>

    <a id="_CPPv3N26app_env_charging_current_t19CHARGING_CURR_110MAE"></a> <a id="_CPPv2N26app_env_charging_current_t19CHARGING_CURR_110MAE"></a> <a id="app__env_8h_1a1dd879e99738420342b4ca96376dd186a0e5579ded0d5d660461a9393674c8f19"></a> enumerator CHARGING\_CURR\_110MA

<a id="_CPPv415WAVE_EVENT_LIST"></a>

<a id="_CPPv315WAVE_EVENT_LIST"></a> <a id="_CPPv215WAVE_EVENT_LIST"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086c"></a> enum WAVE\_EVENT\_LIST
:   hints event type index definition

    *Values:*

    <a id="_CPPv4N15WAVE_EVENT_LIST12WAVE_INVALIDE"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST12WAVE_INVALIDE"></a> <a id="_CPPv2N15WAVE_EVENT_LIST12WAVE_INVALIDE"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086ca120f57595b2409c560964ac485865a3b"></a> enumerator WAVE\_INVALID

    <a id="_CPPv4N15WAVE_EVENT_LIST13WAVE_POWER_ONE"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST13WAVE_POWER_ONE"></a> <a id="_CPPv2N15WAVE_EVENT_LIST13WAVE_POWER_ONE"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086caa6e9548d751796d5065c40377a12f4f6"></a> enumerator WAVE\_POWER\_ON

    <a id="_CPPv4N15WAVE_EVENT_LIST14WAVE_CONNECTEDE"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST14WAVE_CONNECTEDE"></a> <a id="_CPPv2N15WAVE_EVENT_LIST14WAVE_CONNECTEDE"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086ca7969b5f5e51019705a8500965a8786f2"></a> enumerator WAVE\_CONNECTED

    <a id="_CPPv4N15WAVE_EVENT_LIST17WAVE_DISCONNECTEDE"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST17WAVE_DISCONNECTEDE"></a> <a id="_CPPv2N15WAVE_EVENT_LIST17WAVE_DISCONNECTEDE"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086ca27a212b5987e92c8391a2d4467c61289"></a> enumerator WAVE\_DISCONNECTED

    <a id="_CPPv4N15WAVE_EVENT_LIST14WAVE_POWER_OFFE"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST14WAVE_POWER_OFFE"></a> <a id="_CPPv2N15WAVE_EVENT_LIST14WAVE_POWER_OFFE"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086ca0694d9c0c3e51a6b935ef764e3e2751f"></a> enumerator WAVE\_POWER\_OFF

    <a id="_CPPv4N15WAVE_EVENT_LIST18WAVE_ENTER_PAIRINGE"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST18WAVE_ENTER_PAIRINGE"></a> <a id="_CPPv2N15WAVE_EVENT_LIST18WAVE_ENTER_PAIRINGE"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086ca1e7bd66400cae04fd2a4cd2714372533"></a> enumerator WAVE\_ENTER\_PAIRING

    <a id="_CPPv4N15WAVE_EVENT_LIST16WAVE_LOW_BATTERYE"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST16WAVE_LOW_BATTERYE"></a> <a id="_CPPv2N15WAVE_EVENT_LIST16WAVE_LOW_BATTERYE"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086ca3b60bfbd50b7962cb595f16de17f8bf8"></a> enumerator WAVE\_LOW\_BATTERY

    <a id="_CPPv4N15WAVE_EVENT_LIST13WAVE_HFP_RINGE"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST13WAVE_HFP_RINGE"></a> <a id="_CPPv2N15WAVE_EVENT_LIST13WAVE_HFP_RINGE"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086ca7bc0fc56d32de88fc15be96304a6000e"></a> enumerator WAVE\_HFP\_RING

    <a id="_CPPv4N15WAVE_EVENT_LIST12WAVE_HFP_ACKE"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST12WAVE_HFP_ACKE"></a> <a id="_CPPv2N15WAVE_EVENT_LIST12WAVE_HFP_ACKE"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086cad036f4229804c0d1a2a71afd7a89f0ea"></a> enumerator WAVE\_HFP\_ACK

    <a id="_CPPv4N15WAVE_EVENT_LIST14WAVE_HF_REJECTE"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST14WAVE_HF_REJECTE"></a> <a id="_CPPv2N15WAVE_EVENT_LIST14WAVE_HF_REJECTE"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086ca558cf372d8c0d0d77ea31ae075f4db25"></a> enumerator WAVE\_HF\_REJECT

    <a id="_CPPv4N15WAVE_EVENT_LIST14WAVE_HF_CANCELE"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST14WAVE_HF_CANCELE"></a> <a id="_CPPv2N15WAVE_EVENT_LIST14WAVE_HF_CANCELE"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086cae7b73e1939a2d6e0ba7e27a67a194ee2"></a> enumerator WAVE\_HF\_CANCEL

    <a id="_CPPv4N15WAVE_EVENT_LIST18WAVE_HF_VOICE_DIALE"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST18WAVE_HF_VOICE_DIALE"></a> <a id="_CPPv2N15WAVE_EVENT_LIST18WAVE_HF_VOICE_DIALE"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086caa5c98c079dc88ad2d5a02c680e918d0d"></a> enumerator WAVE\_HF\_VOICE\_DIAL

    <a id="_CPPv4N15WAVE_EVENT_LIST13WAVE_MUTE_MICE"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST13WAVE_MUTE_MICE"></a> <a id="_CPPv2N15WAVE_EVENT_LIST13WAVE_MUTE_MICE"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086cac8162a33d0de36c70f3cc6c5041d7376"></a> enumerator WAVE\_MUTE\_MIC

    <a id="_CPPv4N15WAVE_EVENT_LIST15WAVE_UNMUTE_MICE"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST15WAVE_UNMUTE_MICE"></a> <a id="_CPPv2N15WAVE_EVENT_LIST15WAVE_UNMUTE_MICE"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086cad09a7233167b2bc65a6485222fe3abd5"></a> enumerator WAVE\_UNMUTE\_MIC

    <a id="_CPPv4N15WAVE_EVENT_LIST12WAVE_VOL_MAXE"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST12WAVE_VOL_MAXE"></a> <a id="_CPPv2N15WAVE_EVENT_LIST12WAVE_VOL_MAXE"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086ca55950003d3b0dec6cc890267f71ac6a2"></a> enumerator WAVE\_VOL\_MAX

    <a id="_CPPv4N15WAVE_EVENT_LIST12WAVE_VOL_MINE"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST12WAVE_VOL_MINE"></a> <a id="_CPPv2N15WAVE_EVENT_LIST12WAVE_VOL_MINE"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086caa7d1c240cdd674f3b7671f1a87590f23"></a> enumerator WAVE\_VOL\_MIN

    <a id="_CPPv4N15WAVE_EVENT_LIST23WAVE_HF_TRANSFER_TOGGLEE"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST23WAVE_HF_TRANSFER_TOGGLEE"></a> <a id="_CPPv2N15WAVE_EVENT_LIST23WAVE_HF_TRANSFER_TOGGLEE"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086cabff4477b5f9ccb0bee0edf00a5326c93"></a> enumerator WAVE\_HF\_TRANSFER\_TOGGLE

    <a id="_CPPv4N15WAVE_EVENT_LIST14WAVE_HF_REDIALE"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST14WAVE_HF_REDIALE"></a> <a id="_CPPv2N15WAVE_EVENT_LIST14WAVE_HF_REDIALE"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086ca5227df2993efae564b4f1439d622d9b6"></a> enumerator WAVE\_HF\_REDIAL

    <a id="_CPPv4N15WAVE_EVENT_LIST17WAVE_CLEAR_MEMORYE"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST17WAVE_CLEAR_MEMORYE"></a> <a id="_CPPv2N15WAVE_EVENT_LIST17WAVE_CLEAR_MEMORYE"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086ca7a2585e50a6a83f6a280f199865d025a"></a> enumerator WAVE\_CLEAR\_MEMORY

    <a id="_CPPv4N15WAVE_EVENT_LIST15WAVE_VOICE_NUM0E"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST15WAVE_VOICE_NUM0E"></a> <a id="_CPPv2N15WAVE_EVENT_LIST15WAVE_VOICE_NUM0E"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086ca452390ad1749b34385b8197570ff5349"></a> enumerator WAVE\_VOICE\_NUM0

    <a id="_CPPv4N15WAVE_EVENT_LIST15WAVE_VOICE_NUM1E"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST15WAVE_VOICE_NUM1E"></a> <a id="_CPPv2N15WAVE_EVENT_LIST15WAVE_VOICE_NUM1E"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086ca5059fce13172965f9eedffae316af33e"></a> enumerator WAVE\_VOICE\_NUM1

    <a id="_CPPv4N15WAVE_EVENT_LIST15WAVE_VOICE_NUM2E"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST15WAVE_VOICE_NUM2E"></a> <a id="_CPPv2N15WAVE_EVENT_LIST15WAVE_VOICE_NUM2E"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086ca969d3e1c39e7cf4d7bf4ad30722016c5"></a> enumerator WAVE\_VOICE\_NUM2

    <a id="_CPPv4N15WAVE_EVENT_LIST15WAVE_VOICE_NUM3E"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST15WAVE_VOICE_NUM3E"></a> <a id="_CPPv2N15WAVE_EVENT_LIST15WAVE_VOICE_NUM3E"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086caf1c2cc9b1b4753f946b3174cd337415b"></a> enumerator WAVE\_VOICE\_NUM3

    <a id="_CPPv4N15WAVE_EVENT_LIST15WAVE_VOICE_NUM4E"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST15WAVE_VOICE_NUM4E"></a> <a id="_CPPv2N15WAVE_EVENT_LIST15WAVE_VOICE_NUM4E"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086ca8a9b42e803bfe1a53a89a035f4bdd3dd"></a> enumerator WAVE\_VOICE\_NUM4

    <a id="_CPPv4N15WAVE_EVENT_LIST15WAVE_VOICE_NUM5E"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST15WAVE_VOICE_NUM5E"></a> <a id="_CPPv2N15WAVE_EVENT_LIST15WAVE_VOICE_NUM5E"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086ca52846c84b55047c2d91dc52a854a5149"></a> enumerator WAVE\_VOICE\_NUM5

    <a id="_CPPv4N15WAVE_EVENT_LIST15WAVE_VOICE_NUM6E"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST15WAVE_VOICE_NUM6E"></a> <a id="_CPPv2N15WAVE_EVENT_LIST15WAVE_VOICE_NUM6E"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086ca7b0e555fe1c7aa84a529428f42cb28ec"></a> enumerator WAVE\_VOICE\_NUM6

    <a id="_CPPv4N15WAVE_EVENT_LIST15WAVE_VOICE_NUM7E"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST15WAVE_VOICE_NUM7E"></a> <a id="_CPPv2N15WAVE_EVENT_LIST15WAVE_VOICE_NUM7E"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086ca779fdc0cb10b374948a49182eb360fa3"></a> enumerator WAVE\_VOICE\_NUM7

    <a id="_CPPv4N15WAVE_EVENT_LIST15WAVE_VOICE_NUM8E"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST15WAVE_VOICE_NUM8E"></a> <a id="_CPPv2N15WAVE_EVENT_LIST15WAVE_VOICE_NUM8E"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086ca218afaa30dbcda16c8558db4fff077de"></a> enumerator WAVE\_VOICE\_NUM8

    <a id="_CPPv4N15WAVE_EVENT_LIST15WAVE_VOICE_NUM9E"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST15WAVE_VOICE_NUM9E"></a> <a id="_CPPv2N15WAVE_EVENT_LIST15WAVE_VOICE_NUM9E"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086cad7acae1dd15e5d4abab2f9c747bb6db2"></a> enumerator WAVE\_VOICE\_NUM9

    <a id="_CPPv4N15WAVE_EVENT_LIST12WAVE_BT_MODEE"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST12WAVE_BT_MODEE"></a> <a id="_CPPv2N15WAVE_EVENT_LIST12WAVE_BT_MODEE"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086ca69c0f9c0b1212f11c995441f04edf01c"></a> enumerator WAVE\_BT\_MODE

    <a id="_CPPv4N15WAVE_EVENT_LIST15WAVE_UDISK_MODEE"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST15WAVE_UDISK_MODEE"></a> <a id="_CPPv2N15WAVE_EVENT_LIST15WAVE_UDISK_MODEE"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086ca899d4deb8628a8a24cb36f4079948944"></a> enumerator WAVE\_UDISK\_MODE

    <a id="_CPPv4N15WAVE_EVENT_LIST12WAVE_FM_MODEE"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST12WAVE_FM_MODEE"></a> <a id="_CPPv2N15WAVE_EVENT_LIST12WAVE_FM_MODEE"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086ca1bc4202c17bd3de09b80489ed2e35acf"></a> enumerator WAVE\_FM\_MODE

    <a id="_CPPv4N15WAVE_EVENT_LIST16WAVE_LINEIN_MODEE"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST16WAVE_LINEIN_MODEE"></a> <a id="_CPPv2N15WAVE_EVENT_LIST16WAVE_LINEIN_MODEE"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086ca99b37e528628c8d44992e545184fb8cd"></a> enumerator WAVE\_LINEIN\_MODE

    <a id="_CPPv4N15WAVE_EVENT_LIST16WAVE_SDCARD_MODEE"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST16WAVE_SDCARD_MODEE"></a> <a id="_CPPv2N15WAVE_EVENT_LIST16WAVE_SDCARD_MODEE"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086cafd920dd23515b0391e0a05f3a5070030"></a> enumerator WAVE\_SDCARD\_MODE

    <a id="_CPPv4N15WAVE_EVENT_LIST14WAVE_RESERVED1E"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST14WAVE_RESERVED1E"></a> <a id="_CPPv2N15WAVE_EVENT_LIST14WAVE_RESERVED1E"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086caf70cf2aadf76c97a63ef8a7cd03cb145"></a> enumerator WAVE\_RESERVED1

    <a id="_CPPv4N15WAVE_EVENT_LIST14WAVE_RESERVED2E"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST14WAVE_RESERVED2E"></a> <a id="_CPPv2N15WAVE_EVENT_LIST14WAVE_RESERVED2E"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086cabec2e5c40e671e4040e0ac346526cb5a"></a> enumerator WAVE\_RESERVED2

    <a id="_CPPv4N15WAVE_EVENT_LIST14WAVE_RESERVED3E"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST14WAVE_RESERVED3E"></a> <a id="_CPPv2N15WAVE_EVENT_LIST14WAVE_RESERVED3E"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086caa53710f3757ed81fe9f21db44892a171"></a> enumerator WAVE\_RESERVED3

    <a id="_CPPv4N15WAVE_EVENT_LIST14WAVE_RESERVED4E"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST14WAVE_RESERVED4E"></a> <a id="_CPPv2N15WAVE_EVENT_LIST14WAVE_RESERVED4E"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086ca36cd48254f2acb0151b62b1f8e14b9be"></a> enumerator WAVE\_RESERVED4

    <a id="_CPPv4N15WAVE_EVENT_LIST14WAVE_RESERVED5E"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST14WAVE_RESERVED5E"></a> <a id="_CPPv2N15WAVE_EVENT_LIST14WAVE_RESERVED5E"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086caed0df0ae89de04828735d2f96499a007"></a> enumerator WAVE\_RESERVED5

    <a id="_CPPv4N15WAVE_EVENT_LIST14WAVE_RESERVED6E"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST14WAVE_RESERVED6E"></a> <a id="_CPPv2N15WAVE_EVENT_LIST14WAVE_RESERVED6E"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086cae1c80e6a57a1ff05eb10224bab93d380"></a> enumerator WAVE\_RESERVED6

    <a id="_CPPv4N15WAVE_EVENT_LIST14WAVE_RESERVED7E"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST14WAVE_RESERVED7E"></a> <a id="_CPPv2N15WAVE_EVENT_LIST14WAVE_RESERVED7E"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086ca95caddd4ad9ce2cdaa92bf919f8908fe"></a> enumerator WAVE\_RESERVED7

    <a id="_CPPv4N15WAVE_EVENT_LIST14WAVE_RESERVED8E"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST14WAVE_RESERVED8E"></a> <a id="_CPPv2N15WAVE_EVENT_LIST14WAVE_RESERVED8E"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086ca4761a83d6a2c38fa480c5c3e684a8343"></a> enumerator WAVE\_RESERVED8

    <a id="_CPPv4N15WAVE_EVENT_LIST14WAVE_RESERVED9E"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST14WAVE_RESERVED9E"></a> <a id="_CPPv2N15WAVE_EVENT_LIST14WAVE_RESERVED9E"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086caf5e8f65968d7d9a0fad0825ccea89221"></a> enumerator WAVE\_RESERVED9

    <a id="_CPPv4N15WAVE_EVENT_LIST8WAVE_ENDE"></a>

    <a id="_CPPv3N15WAVE_EVENT_LIST8WAVE_ENDE"></a> <a id="_CPPv2N15WAVE_EVENT_LIST8WAVE_ENDE"></a> <a id="app__env_8h_1a5043db45534b90d0323376092a32086ca99fea36a1eb93227919156e7be722555"></a> enumerator WAVE\_END

<a id="_CPPv414WAVE_TYPE_LIST"></a>

<a id="_CPPv314WAVE_TYPE_LIST"></a> <a id="_CPPv214WAVE_TYPE_LIST"></a> <a id="app__env_8h_1a11d52bdff153b2056aeef244de05c6d6"></a> enum WAVE\_TYPE\_LIST
:   hints codec type index definition

    *Values:*

    <a id="_CPPv4N14WAVE_TYPE_LIST15INTER_FLASH_WAVE"></a>

    <a id="_CPPv3N14WAVE_TYPE_LIST15INTER_FLASH_WAVE"></a> <a id="_CPPv2N14WAVE_TYPE_LIST15INTER_FLASH_WAVE"></a> <a id="app__env_8h_1a11d52bdff153b2056aeef244de05c6d6a4892dacb2dc5ea5965e763e0afbe5f7c"></a> enumerator INTER\_FLASH\_WAV

    <a id="_CPPv4N14WAVE_TYPE_LIST15INTER_FLASH_SBCE"></a>

    <a id="_CPPv3N14WAVE_TYPE_LIST15INTER_FLASH_SBCE"></a> <a id="_CPPv2N14WAVE_TYPE_LIST15INTER_FLASH_SBCE"></a> <a id="app__env_8h_1a11d52bdff153b2056aeef244de05c6d6a39b2ee963a6d1964eaf6e06e4eb4c0c4"></a> enumerator INTER\_FLASH\_SBC

    <a id="_CPPv4N14WAVE_TYPE_LIST15INTER_FLASH_AMRE"></a>

    <a id="_CPPv3N14WAVE_TYPE_LIST15INTER_FLASH_AMRE"></a> <a id="_CPPv2N14WAVE_TYPE_LIST15INTER_FLASH_AMRE"></a> <a id="app__env_8h_1a11d52bdff153b2056aeef244de05c6d6a29f4e1d9c6e48b35288f55aae1d62212"></a> enumerator INTER\_FLASH\_AMR

    <a id="_CPPv4N14WAVE_TYPE_LIST13EXT_FLASH_WAVE"></a>

    <a id="_CPPv3N14WAVE_TYPE_LIST13EXT_FLASH_WAVE"></a> <a id="_CPPv2N14WAVE_TYPE_LIST13EXT_FLASH_WAVE"></a> <a id="app__env_8h_1a11d52bdff153b2056aeef244de05c6d6a3f42ed6b6692a42ede2e7d9acb27c86e"></a> enumerator EXT\_FLASH\_WAV

    <a id="_CPPv4N14WAVE_TYPE_LIST13EXT_FLASH_SBCE"></a>

    <a id="_CPPv3N14WAVE_TYPE_LIST13EXT_FLASH_SBCE"></a> <a id="_CPPv2N14WAVE_TYPE_LIST13EXT_FLASH_SBCE"></a> <a id="app__env_8h_1a11d52bdff153b2056aeef244de05c6d6a56372923f9b04a467102d33e96d86bee"></a> enumerator EXT\_FLASH\_SBC

    <a id="_CPPv4N14WAVE_TYPE_LIST13EXT_FLASH_AMRE"></a>

    <a id="_CPPv3N14WAVE_TYPE_LIST13EXT_FLASH_AMRE"></a> <a id="_CPPv2N14WAVE_TYPE_LIST13EXT_FLASH_AMRE"></a> <a id="app__env_8h_1a11d52bdff153b2056aeef244de05c6d6a9c6baee6f74128e181cea4845d9cdea4"></a> enumerator EXT\_FLASH\_AMR

    <a id="_CPPv4N14WAVE_TYPE_LIST15INTER_SOFT_WAVEE"></a>

    <a id="_CPPv3N14WAVE_TYPE_LIST15INTER_SOFT_WAVEE"></a> <a id="_CPPv2N14WAVE_TYPE_LIST15INTER_SOFT_WAVEE"></a> <a id="app__env_8h_1a11d52bdff153b2056aeef244de05c6d6a3ae3993988efd3cc3c46c6048f886e72"></a> enumerator INTER\_SOFT\_WAVE

<a id="_CPPv418WAVE_BITPOOL_INDEX"></a>

<a id="_CPPv318WAVE_BITPOOL_INDEX"></a> <a id="_CPPv218WAVE_BITPOOL_INDEX"></a> <a id="app__env_8h_1a77afd959aacfc11e0e331d9519d25a4e"></a> enum WAVE\_BITPOOL\_INDEX
:   hints bitpool index definition

    *Values:*

    <a id="_CPPv4N18WAVE_BITPOOL_INDEX9WAVE_NONEE"></a>

    <a id="_CPPv3N18WAVE_BITPOOL_INDEX9WAVE_NONEE"></a> <a id="_CPPv2N18WAVE_BITPOOL_INDEX9WAVE_NONEE"></a> <a id="app__env_8h_1a77afd959aacfc11e0e331d9519d25a4eaa3f62a5e55c9b392ee4b3fc460080789"></a> enumerator WAVE\_NONE

    <a id="_CPPv4N18WAVE_BITPOOL_INDEX7_80_512E"></a>

    <a id="_CPPv3N18WAVE_BITPOOL_INDEX7_80_512E"></a> <a id="_CPPv2N18WAVE_BITPOOL_INDEX7_80_512E"></a> <a id="app__env_8h_1a77afd959aacfc11e0e331d9519d25a4eadf1b1fe7733c38204c08b25bf254757b"></a> enumerator \_80\_512

    <a id="_CPPv4N18WAVE_BITPOOL_INDEX7_96_512E"></a>

    <a id="_CPPv3N18WAVE_BITPOOL_INDEX7_96_512E"></a> <a id="_CPPv2N18WAVE_BITPOOL_INDEX7_96_512E"></a> <a id="app__env_8h_1a77afd959aacfc11e0e331d9519d25a4eadd578f9a3fd6b705901942601dbb914c"></a> enumerator \_96\_512

    <a id="_CPPv4N18WAVE_BITPOOL_INDEX8_112_512E"></a>

    <a id="_CPPv3N18WAVE_BITPOOL_INDEX8_112_512E"></a> <a id="_CPPv2N18WAVE_BITPOOL_INDEX8_112_512E"></a> <a id="app__env_8h_1a77afd959aacfc11e0e331d9519d25a4ea10c11c5decb9decb3ead28da71b9e8d7"></a> enumerator \_112\_512

    <a id="_CPPv4N18WAVE_BITPOOL_INDEX8_128_512E"></a>

    <a id="_CPPv3N18WAVE_BITPOOL_INDEX8_128_512E"></a> <a id="_CPPv2N18WAVE_BITPOOL_INDEX8_128_512E"></a> <a id="app__env_8h_1a77afd959aacfc11e0e331d9519d25a4eab62329a4e61d4bfe08a0e0fc467d73fc"></a> enumerator \_128\_512
