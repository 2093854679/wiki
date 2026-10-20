---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/tws/tws_config.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="tws-configuration-functions"></a>

# TWS Configuration Functions

<a id="tws-config-api-brief"></a>

## TWS\_CONFIG API Brief

| Application | Brief |
| --- | --- |
| [`tws_config_initialise()`](#_CPPv421tws_config_initialise14btif_bd_addr_t14btif_bd_addr_t12left_right_t "tws_config_initialise") | Initialize TWS configuration |
| [`tws_config_is_tws_addr()`](#_CPPv422tws_config_is_tws_addr14btif_bd_addr_t "tws_config_is_tws_addr") | Check that address is TWS address |
| [`tws_config_get_left_right()`](#_CPPv425tws_config_get_left_rightv "tws_config_get_left_right") | Get earbud position |
| [`tws_config_get_tws_addr()`](#_CPPv423tws_config_get_tws_addrv "tws_config_get_tws_addr") | Get TWS address |
| [`tws_config_get_paring_timeout_ms()`](#_CPPv432tws_config_get_paring_timeout_msv "tws_config_get_paring_timeout_ms") | Get TWS pairing timeout |
| [`tws_config_is_enable_one_bring_two()`](#_CPPv434tws_config_is_enable_one_bring_twov "tws_config_is_enable_one_bring_two") | Check that the one bring two mode is enabled |
| [`tws_config_is_enable_discon_enter_pair()`](#_CPPv438tws_config_is_enable_discon_enter_pairv "tws_config_is_enable_discon_enter_pair") | Check that the disconnect mobile enter pair is enabled |
| [`tws_config_set_tws_addr()`](#_CPPv423tws_config_set_tws_addr14btif_bd_addr_t "tws_config_set_tws_addr") | Set TWS address |
| [`tws_config_is_search_ux_enable()`](#_CPPv430tws_config_is_search_ux_enablev "tws_config_is_search_ux_enable") | Check that TWS earbud search is enabled. |
| [`tws_config_get_reconn_param()`](#_CPPv427tws_config_get_reconn_paramv "tws_config_get_reconn_param") | Get reconnect parameters |
| [`tws_config_is_valid_tws_addr()`](#_CPPv428tws_config_is_valid_tws_addrv "tws_config_is_valid_tws_addr") | Check that the TWS address is valid |
| [`tws_config_enable_search_UX()`](#_CPPv427tws_config_enable_search_UXv "tws_config_enable_search_UX") | Enable TWS earbud search |
| [`tws_config_disable_search_UX()`](#_CPPv428tws_config_disable_search_UXv "tws_config_disable_search_UX") | Disable TWS earbud search |
| [`tws_config_set_left_right()`](#_CPPv425tws_config_set_left_right7uint8_t "tws_config_set_left_right") | Set earbud position |

<a id="tws-config-api-reference"></a>

## TWS\_CONFIG API Reference

<a id="header-file"></a>

### Header File

- [tws/tws\_ux/inc/tws\_config.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/tws/tws_ux/inc/tws_config.h)

<a id="functions"></a>

### Functions

<a id="_CPPv421tws_config_initialise14btif_bd_addr_t14btif_bd_addr_t12left_right_t"></a>

<a id="_CPPv321tws_config_initialise14btif_bd_addr_t14btif_bd_addr_t12left_right_t"></a> <a id="_CPPv221tws_config_initialise14btif_bd_addr_t14btif_bd_addr_t12left_right_t"></a> <a id="tws_config_initialise__btif_bd_addr_t.btif_bd_addr_t.left_right_t"></a> <a id="tws__config_8h_1aa1338a3537f70d2f80865fccc082af20"></a> void tws\_config\_initialise([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") local\_addr, [btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") tws\_addr, [left\_right\_t](#_CPPv412left_right_t "left_right_t") left\_right)
:   Initialize TWS configuration.

    Initialize TWS configuration and send TWS initialization command to the controller.

    参数:
    :   - **local\_addr** – **\[in\]** Local address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t).
        - **tws\_addr** – **\[in\]** TWS address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t).
        - **left\_right** – **\[in\]** TWS earbud position of type left\_right\_t.

    返回:
    :   N/A

<a id="_CPPv422tws_config_is_tws_addr14btif_bd_addr_t"></a>

<a id="_CPPv322tws_config_is_tws_addr14btif_bd_addr_t"></a> <a id="_CPPv222tws_config_is_tws_addr14btif_bd_addr_t"></a> <a id="tws_config_is_tws_addr__btif_bd_addr_t"></a> <a id="tws__config_8h_1ac878894d8f45c0638247a9cb05b73018"></a> bool tws\_config\_is\_tws\_addr([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr)
:   Check that address is TWS address.

    Check that the address \[addr\] is the TWS address in the configuration.

    参数:
    :   **addr** – **\[in\]** address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)

    返回值:
    :   - **true** – is the TWS address
        - **false** – unknown address

    返回:
    :   result

<a id="_CPPv425tws_config_get_left_rightv"></a>

<a id="_CPPv325tws_config_get_left_rightv"></a> <a id="_CPPv225tws_config_get_left_rightv"></a> <a id="tws_config_get_left_right__void"></a> <a id="tws__config_8h_1a23cfec2ff492bc49db2c825311a51705"></a> [left\_right\_t](#_CPPv412left_right_t "left_right_t") tws\_config\_get\_left\_right(void)
:   Get earbud position.

    Get the earbud position in the configuration.

    返回:
    :   earbud position of type left\_right\_t

<a id="_CPPv423tws_config_get_tws_addrv"></a>

<a id="_CPPv323tws_config_get_tws_addrv"></a> <a id="_CPPv223tws_config_get_tws_addrv"></a> <a id="tws_config_get_tws_addr__void"></a> <a id="tws__config_8h_1a1cabc9c1102f86a1f848f4c016575271"></a> [btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") tws\_config\_get\_tws\_addr(void)
:   Get TWS address.

    Get the TWS address in the configuration.

    返回:
    :   TWS address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)

<a id="_CPPv432tws_config_get_paring_timeout_msv"></a>

<a id="_CPPv332tws_config_get_paring_timeout_msv"></a> <a id="_CPPv232tws_config_get_paring_timeout_msv"></a> <a id="tws_config_get_paring_timeout_ms__void"></a> <a id="tws__config_8h_1a74ef2e04afd09705db8399873df74e3f"></a> uint32\_t tws\_config\_get\_paring\_timeout\_ms(void)
:   Get TWS pairing timeout.

    Get the TWS pairing timeout in the configuration.

    返回:
    :   TWS pairing timeout (ms)

<a id="_CPPv434tws_config_is_enable_one_bring_twov"></a>

<a id="_CPPv334tws_config_is_enable_one_bring_twov"></a> <a id="_CPPv234tws_config_is_enable_one_bring_twov"></a> <a id="tws_config_is_enable_one_bring_two__void"></a> <a id="tws__config_8h_1aee9e61055abfa39c9b01b34f09dec4f5"></a> bool tws\_config\_is\_enable\_one\_bring\_two(void)
:   Check that the one bring two mode is enabled.

    Check that the one bring two mode is enabled in the configuration.

    返回值:
    :   - **true** – enable
        - **false** – disable

    返回:
    :   result

<a id="_CPPv438tws_config_is_enable_discon_enter_pairv"></a>

<a id="_CPPv338tws_config_is_enable_discon_enter_pairv"></a> <a id="_CPPv238tws_config_is_enable_discon_enter_pairv"></a> <a id="tws_config_is_enable_discon_enter_pair__void"></a> <a id="tws__config_8h_1ae51e15b1a3f9a5728679e335d5c61792"></a> bool tws\_config\_is\_enable\_discon\_enter\_pair(void)
:   Check that the disconnect mobile enter pair is enabled.

    Check that the disconnect mobile enter pair is enabled in the configuration.

    返回值:
    :   - **true** – enable
        - **false** – disable

    返回:
    :   result

<a id="_CPPv423tws_config_set_tws_addr14btif_bd_addr_t"></a>

<a id="_CPPv323tws_config_set_tws_addr14btif_bd_addr_t"></a> <a id="_CPPv223tws_config_set_tws_addr14btif_bd_addr_t"></a> <a id="tws_config_set_tws_addr__btif_bd_addr_t"></a> <a id="tws__config_8h_1adf6459141c7c1a279adde25295c5679a"></a> void tws\_config\_set\_tws\_addr([btif\_bd\_addr\_t](../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") tws\_addr)
:   Set TWS address.

    Set the TWS address in the configuration.

    参数:
    :   **tws\_addr** – **\[in\]** TWS address of type [btif\_bd\_addr\_t](../../btif/btif_type.md#structbtif__bd__addr__t)

    返回:
    :   N/A

<a id="_CPPv430tws_config_is_search_ux_enablev"></a>

<a id="_CPPv330tws_config_is_search_ux_enablev"></a> <a id="_CPPv230tws_config_is_search_ux_enablev"></a> <a id="tws_config_is_search_ux_enable__void"></a> <a id="tws__config_8h_1a21467b398a3de88aa80d8cda45f0a8e7"></a> bool tws\_config\_is\_search\_ux\_enable(void)
:   Check that TWS earbud search is enabled.

    Check that another paired TWS earbud search is enabled in the configuration.

    返回值:
    :   - **true** – enable
        - **false** – disable

    返回:
    :   result

<a id="_CPPv427tws_config_get_reconn_paramv"></a>

<a id="_CPPv327tws_config_get_reconn_paramv"></a> <a id="_CPPv227tws_config_get_reconn_paramv"></a> <a id="tws_config_get_reconn_param__void"></a> <a id="tws__config_8h_1a814a0b6341015d18b6192cdd9fea37e9"></a> [tws\_reconn\_cfg\_t](#_CPPv416tws_reconn_cfg_t "tws_reconn_cfg_t") \*tws\_config\_get\_reconn\_param(void)
:   Get reconnect parameters.

    Get reconnect parameters in the configuration.

    返回:
    :   pointer to reconnect parameters of type [tws\_reconn\_cfg\_t](#structtws__reconn__cfg__t)

<a id="_CPPv428tws_config_is_valid_tws_addrv"></a>

<a id="_CPPv328tws_config_is_valid_tws_addrv"></a> <a id="_CPPv228tws_config_is_valid_tws_addrv"></a> <a id="tws_config_is_valid_tws_addr__void"></a> <a id="tws__config_8h_1a3678612c5dbb8b6f81bc5510a0e95cd3"></a> bool tws\_config\_is\_valid\_tws\_addr(void)
:   Check that the TWS address is valid.

    Check that the TWS address is valid in the configuration.

    返回值:
    :   - **true** – valid
        - **false** – invalid

    返回:
    :   result

<a id="_CPPv427tws_config_enable_search_UXv"></a>

<a id="_CPPv327tws_config_enable_search_UXv"></a> <a id="_CPPv227tws_config_enable_search_UXv"></a> <a id="tws_config_enable_search_UX__void"></a> <a id="tws__config_8h_1a6b80144328dc1ecc880050a1fe197c37"></a> void tws\_config\_enable\_search\_UX(void)
:   Enable TWS earbud search.

    Enable search for another paired TWS earbud in the configuration.

    返回:
    :   N/A

<a id="_CPPv428tws_config_disable_search_UXv"></a>

<a id="_CPPv328tws_config_disable_search_UXv"></a> <a id="_CPPv228tws_config_disable_search_UXv"></a> <a id="tws_config_disable_search_UX__void"></a> <a id="tws__config_8h_1ab83219fc068e835fdbbb6f30d531ee24"></a> void tws\_config\_disable\_search\_UX(void)
:   Disable TWS earbud search.

    Disable search for another paired TWS earbud in the configuration.

    返回:
    :   N/A

<a id="_CPPv425tws_config_set_left_right7uint8_t"></a>

<a id="_CPPv325tws_config_set_left_right7uint8_t"></a> <a id="_CPPv225tws_config_set_left_right7uint8_t"></a> <a id="tws_config_set_left_right__uint8_t"></a> <a id="tws__config_8h_1aad9c119ef537a65ba634f604ebcc9088"></a> void tws\_config\_set\_left\_right(uint8\_t left\_right)
:   Set earbud position.

    Set the earbud position in the configuration.

    参数:
    :   **left\_right** – **\[in\]** earbud position of type left\_right\_t

    返回:
    :   N/A **TWS\_CONFIG\_H** EOF

<a id="structures"></a>

### Structures

<a id="_CPPv416tws_reconn_cfg_t"></a>

<a id="_CPPv316tws_reconn_cfg_t"></a> <a id="_CPPv216tws_reconn_cfg_t"></a> <a id="tws_reconn_cfg_t"></a> <a id="structtws__reconn__cfg__t"></a> struct tws\_reconn\_cfg\_t
:   TWS reconnection configuration structure definition.

<a id="_CPPv412tws_config_t"></a>

<a id="_CPPv312tws_config_t"></a> <a id="_CPPv212tws_config_t"></a> <a id="tws_config_t"></a> <a id="structtws__config__t"></a> struct tws\_config\_t
:   TWS configuration structure definition.

<a id="macros"></a>

### Macros

<a id="c.TWS_MOBILE_LINK_SUPPORTED"></a>

<a id="tws__config_8h_1a069b7e1f0daf65279a7efe0ae34a69b9"></a> TWS\_MOBILE\_LINK\_SUPPORTED
:   Number of TWS linked mobile phones supported

<a id="c.CTO_MAX_RETRY"></a>

<a id="tws__config_8h_1a4633db9a4b630c04ffc7ed93091c136a"></a> CTO\_MAX\_RETRY
:   Maximum number of reconnections

<a id="c.CTO_INTERVAL_MS"></a>

<a id="tws__config_8h_1a850508f2efe409c3df1ea6e6e8b8a5ee"></a> CTO\_INTERVAL\_MS
:   Reconnect interval (ms)

<a id="c.TWS_PARING_TIMEOUT_MS"></a>

<a id="tws__config_8h_1a4b4eb6f5bdeeb93d8b63ff277e8f3934"></a> TWS\_PARING\_TIMEOUT\_MS
:   TWS paring timeout (ms)

<a id="c.LEFT_POS"></a>

<a id="tws__config_8h_1a38bbfd048900bcc7cd00c91863bd961c"></a> LEFT\_POS
:   left position

<a id="c.RIGHT_POS"></a>

<a id="tws__config_8h_1a936d83a70aab624ae410c5e0ecf3c3a9"></a> RIGHT\_POS
:   right position

<a id="c.UNKNOWN_POS"></a>

<a id="tws__config_8h_1a7b497e8c05226b11bf56976988b42760"></a> UNKNOWN\_POS
:   unknown position

<a id="c.PAIRING_TWS_DISCONNECT_SET"></a>

<a id="tws__config_8h_1ac33c5257e7f4c9b24cabd35b0fd621d0"></a> PAIRING\_TWS\_DISCONNECT\_SET

<a id="c.PAIRING_TWS_CONNECTED_L_SET"></a>

<a id="tws__config_8h_1af4dc7a0d401d14f3a27912c98c00d412"></a> PAIRING\_TWS\_CONNECTED\_L\_SET

<a id="c.PAIRING_TWS_CONNECTED_R_SET"></a>

<a id="tws__config_8h_1a91e4801d0b231ff61e0379093dcb85c7"></a> PAIRING\_TWS\_CONNECTED\_R\_SET

<a id="c.NORMAL_TWS_CONNECTED_L_SET"></a>

<a id="tws__config_8h_1a14680c6978350fd0f6f1c43a70afd714"></a> NORMAL\_TWS\_CONNECTED\_L\_SET

<a id="c.NORMAL_TWS_CONNECTED_R_SET"></a>

<a id="tws__config_8h_1a3eada31c850c0ec52b5c53e03c27e7a2"></a> NORMAL\_TWS\_CONNECTED\_R\_SET

<a id="c.NORMAL_TWS_DISCONNECTED_L_SET"></a>

<a id="tws__config_8h_1ad15058118a26981a256f274fc6070271"></a> NORMAL\_TWS\_DISCONNECTED\_L\_SET

<a id="c.NORMAL_TWS_DISCONNECTED_R_SET"></a>

<a id="tws__config_8h_1a22b97cc7e4218f6f27d8fdabb74ed451"></a> NORMAL\_TWS\_DISCONNECTED\_R\_SET

<a id="c.BOX_CLOSED_SET"></a>

<a id="tws__config_8h_1a6d485ecb9f9789dbcef6e59b20523b1e"></a> BOX\_CLOSED\_SET

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv412left_right_t"></a>

<a id="_CPPv312left_right_t"></a> <a id="_CPPv212left_right_t"></a> <a id="left_right_t"></a> <a id="tws__config_8h_1a09e7bab3730cb6f3ed4a02ef9e28d673"></a> typedef uint8\_t left\_right\_t
:   TWS earbud position type definition.
