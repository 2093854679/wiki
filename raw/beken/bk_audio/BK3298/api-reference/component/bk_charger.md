---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/component/bk_charger.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bk-charger"></a>

# BK\_CHARGER

<a id="bk-charger-api-status"></a>

## BK\_CHARGER API Status

| API |
| --- |
| [`bk_charger_init()`](#_CPPv415bk_charger_initv "bk_charger_init") |
| [`bk_charger_deinit()`](#_CPPv417bk_charger_deinitv "bk_charger_deinit") |
| [`bk_charger_reg_callback()`](#_CPPv423bk_charger_reg_callback18pfunc_charger_cb_t "bk_charger_reg_callback") |
| [`bk_charger_get_current_state()`](#_CPPv428bk_charger_get_current_statev "bk_charger_get_current_state") |
| [`bk_charger_enable()`](#_CPPv417bk_charger_enableb "bk_charger_enable") |

<a id="bk-charger-api-reference"></a>

## BK\_CHARGER API Reference

<a id="header-file"></a>

### Header File

- [component/charger/bk\_charger.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/component/charger/bk_charger.h)

<a id="functions"></a>

### Functions

<a id="_CPPv415bk_charger_initv"></a>

<a id="_CPPv315bk_charger_initv"></a> <a id="_CPPv215bk_charger_initv"></a> <a id="bk_charger_init__void"></a> <a id="bk__charger_8h_1acfad08b338d5440cc4829602c051af2f"></a> int32\_t bk\_charger\_init(void)
:   initialise charger.

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv417bk_charger_deinitv"></a>

<a id="_CPPv317bk_charger_deinitv"></a> <a id="_CPPv217bk_charger_deinitv"></a> <a id="bk_charger_deinit__void"></a> <a id="bk__charger_8h_1a4c8acc1d712e081c14293b8daea686ea"></a> int32\_t bk\_charger\_deinit(void)
:   deinitialise charger.

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv423bk_charger_reg_callback18pfunc_charger_cb_t"></a>

<a id="_CPPv323bk_charger_reg_callback18pfunc_charger_cb_t"></a> <a id="_CPPv223bk_charger_reg_callback18pfunc_charger_cb_t"></a> <a id="bk_charger_reg_callback__pfunc_charger_cb_t"></a> <a id="bk__charger_8h_1a5f06c2451e1bd8e8547cbc0509a22f36"></a> int32\_t bk\_charger\_reg\_callback([pfunc\_charger\_cb\_t](#_CPPv418pfunc_charger_cb_t "pfunc_charger_cb_t") pfn\_state\_change\_cb)
:   register callback for charger state changed.

    参数:
    :   **pfn\_state\_change\_cb** – **\[in\]** 状态变化的callback函数

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv428bk_charger_get_current_statev"></a>

<a id="_CPPv328bk_charger_get_current_statev"></a> <a id="_CPPv228bk_charger_get_current_statev"></a> <a id="bk_charger_get_current_state__void"></a> <a id="bk__charger_8h_1ab04a867ba4294c0c1cc5ffc1decbfc6b"></a> [bk\_chg\_state\_e](#_CPPv414bk_chg_state_e "bk_chg_state_e") bk\_charger\_get\_current\_state(void)
:   get current charger state.

    返回:
    :   state see [bk\_chg\_state\_e](#bk__charger_8h_1a4e3863d8d482d7b7a20fbf23eb6bf2f7)

<a id="_CPPv417bk_charger_enableb"></a>

<a id="_CPPv317bk_charger_enableb"></a> <a id="_CPPv217bk_charger_enableb"></a> <a id="bk_charger_enable__b"></a> <a id="bk__charger_8h_1a7b764ad982c32fcf58e9588f732a9f3b"></a> int32\_t bk\_charger\_enable(bool enable\_charger)
:   enable/disable charger

    参数:
    :   **enable\_charger** – **\[in\]** true: enable charger false: disable charger

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv414bk_chg_state_e"></a>

<a id="_CPPv314bk_chg_state_e"></a> <a id="_CPPv214bk_chg_state_e"></a> <a id="bk_chg_state_e"></a> <a id="bk__charger_8h_1a4e3863d8d482d7b7a20fbf23eb6bf2f7"></a> typedef enum [\_bk\_chg\_state\_e](#_CPPv415_bk_chg_state_e "_bk_chg_state_e") bk\_chg\_state\_e
:   充电状态的变化

<a id="_CPPv418pfunc_charger_cb_t"></a>

<a id="_CPPv318pfunc_charger_cb_t"></a> <a id="_CPPv218pfunc_charger_cb_t"></a> <a id="pfunc_charger_cb_t"></a> <a id="bk__charger_8h_1a12d864407f442541cf8b5c71bc9715ad"></a> typedef void (\*pfunc\_charger\_cb\_t)([bk\_chg\_state\_e](#_CPPv414bk_chg_state_e "bk_chg_state_e") e\_from, [bk\_chg\_state\_e](#_CPPv414bk_chg_state_e "bk_chg_state_e") e\_to)
:   charger state changed callback

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv415_bk_chg_state_e"></a>

<a id="_CPPv315_bk_chg_state_e"></a> <a id="_CPPv215_bk_chg_state_e"></a> <a id="bk__charger_8h_1af9e81f80fa9146472716eff002ee05f5"></a> enum \_bk\_chg\_state\_e
:   充电状态的变化

    *Values:*

    <a id="_CPPv4N15_bk_chg_state_e15BK_CHARGER_noneE"></a>

    <a id="_CPPv3N15_bk_chg_state_e15BK_CHARGER_noneE"></a> <a id="_CPPv2N15_bk_chg_state_e15BK_CHARGER_noneE"></a> <a id="bk__charger_8h_1af9e81f80fa9146472716eff002ee05f5a259e634e0342ecc719c6eb2763fd98df"></a> enumerator BK\_CHARGER\_none

    <a id="_CPPv4N15_bk_chg_state_e18BK_CHARGER_plug_inE"></a>

    <a id="_CPPv3N15_bk_chg_state_e18BK_CHARGER_plug_inE"></a> <a id="_CPPv2N15_bk_chg_state_e18BK_CHARGER_plug_inE"></a> <a id="bk__charger_8h_1af9e81f80fa9146472716eff002ee05f5a0814f5d0f18a6d570449fd85493cd17c"></a> enumerator BK\_CHARGER\_plug\_in

    <a id="_CPPv4N15_bk_chg_state_e19BK_CHARGER_plug_outE"></a>

    <a id="_CPPv3N15_bk_chg_state_e19BK_CHARGER_plug_outE"></a> <a id="_CPPv2N15_bk_chg_state_e19BK_CHARGER_plug_outE"></a> <a id="bk__charger_8h_1af9e81f80fa9146472716eff002ee05f5ad36b85d33c219cee014e1716a74a8d03"></a> enumerator BK\_CHARGER\_plug\_out

    <a id="_CPPv4N15_bk_chg_state_e17BK_CHARGER_finishE"></a>

    <a id="_CPPv3N15_bk_chg_state_e17BK_CHARGER_finishE"></a> <a id="_CPPv2N15_bk_chg_state_e17BK_CHARGER_finishE"></a> <a id="bk__charger_8h_1af9e81f80fa9146472716eff002ee05f5a60be6e15b96765526882279378799051"></a> enumerator BK\_CHARGER\_finish

    <a id="_CPPv4N15_bk_chg_state_e17BK_CHARGER_ccfastE"></a>

    <a id="_CPPv3N15_bk_chg_state_e17BK_CHARGER_ccfastE"></a> <a id="_CPPv2N15_bk_chg_state_e17BK_CHARGER_ccfastE"></a> <a id="bk__charger_8h_1af9e81f80fa9146472716eff002ee05f5a4e848d255169eb13123f5803dec19e27"></a> enumerator BK\_CHARGER\_ccfast

    <a id="_CPPv4N15_bk_chg_state_e13BK_CHARGER_cvE"></a>

    <a id="_CPPv3N15_bk_chg_state_e13BK_CHARGER_cvE"></a> <a id="_CPPv2N15_bk_chg_state_e13BK_CHARGER_cvE"></a> <a id="bk__charger_8h_1af9e81f80fa9146472716eff002ee05f5a33eb17b8fc5ae151de29a673c17256f8"></a> enumerator BK\_CHARGER\_cv

    <a id="_CPPv4N15_bk_chg_state_e18BK_CHARGER_trickleE"></a>

    <a id="_CPPv3N15_bk_chg_state_e18BK_CHARGER_trickleE"></a> <a id="_CPPv2N15_bk_chg_state_e18BK_CHARGER_trickleE"></a> <a id="bk__charger_8h_1af9e81f80fa9146472716eff002ee05f5aa070f0e353cdb0adbe7b2e9939ffb34d"></a> enumerator BK\_CHARGER\_trickle

    <a id="_CPPv4N15_bk_chg_state_e16BK_CHARGER_rechgE"></a>

    <a id="_CPPv3N15_bk_chg_state_e16BK_CHARGER_rechgE"></a> <a id="_CPPv2N15_bk_chg_state_e16BK_CHARGER_rechgE"></a> <a id="bk__charger_8h_1af9e81f80fa9146472716eff002ee05f5ad916905ff81ac3cb989131155430ba76"></a> enumerator BK\_CHARGER\_rechg
