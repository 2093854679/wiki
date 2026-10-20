---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/common/app_audio/app_anc.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="anc-application-functions"></a>

# ANC Application Functions

<a id="app-anc-api-brief"></a>

## APP\_ANC API Brief

| Application | Brief |
| --- | --- |
| [`app_anc_get_version()`](#_CPPv419app_anc_get_versionv "app_anc_get_version") | get anc version |
| [`anc_anc_get_verstr()`](#_CPPv418anc_anc_get_verstrv "anc_anc_get_verstr") | get anc version string |
| [`app_anc_deinit()`](#_CPPv414app_anc_deinitv "app_anc_deinit") | turn off anc operate |
| [`app_anc_init()`](#_CPPv412app_anc_init7uint8_t "app_anc_init") | turn on anc operate and initialize |
| [`app_anc_cmd_handler()`](#_CPPv419app_anc_cmd_handlerPvP7uint8_tP8uint16_t "app_anc_cmd_handler") | handle anc command |
| [`app_anc_is_open()`](#_CPPv415app_anc_is_openv "app_anc_is_open") | Enquiry anc is Enable or not |
| [`app_anc_reopen()`](#_CPPv414app_anc_reopen7uint8_t "app_anc_reopen") | re-open anc function |
| [`app_anc_reset_audio()`](#_CPPv419app_anc_reset_audiov "app_anc_reset_audio") | reset g\_audio\_env |
| [`app_anc_fade_in()`](#_CPPv415app_anc_fade_in7uint8_t "app_anc_fade_in") | setting fade in of p\_path\_ctrl variables |
| [`app_anc_fade_out()`](#_CPPv416app_anc_fade_out7uint8_t "app_anc_fade_out") | setting fade out of p\_path\_ctrl variables |
| [`app_audio_anc_ctrl_noise_cancel()`](#_CPPv431app_audio_anc_ctrl_noise_cancelv "app_audio_anc_ctrl_noise_cancel") | turn on anc function |
| [`app_audio_anc_ctrl_off()`](#_CPPv422app_audio_anc_ctrl_offv "app_audio_anc_ctrl_off") | turn off anc function |
| [`app_anc_path_fade_in()`](#_CPPv420app_anc_path_fade_in8uint32_t "app_anc_path_fade_in") | setting multi-path to fade in |
| [`app_anc_cache_reset()`](#_CPPv419app_anc_cache_resetv "app_anc_cache_reset") | reset ec cache ram and reset anc digital gain |
| [`app_anc_get_current_gain()`](#_CPPv424app_anc_get_current_gain7uint8_t "app_anc_get_current_gain") | get digital gain from specify voice path |
| [`app_anc_button_ctrl()`](#_CPPv419app_anc_button_ctrlv "app_anc_button_ctrl") | anc button control |
| [`app_anc_reset_coef_by_path()`](#_CPPv426app_anc_reset_coef_by_path8uint32_t "app_anc_reset_coef_by_path") | app\_anc\_reset\_coef\_by\_path |
| [`app_anc_rx_ctrl_handle()`](#_CPPv422app_anc_rx_ctrl_handlePK7uint8_t8uint16_t "app_anc_rx_ctrl_handle") | handle TWS\_ANC\_CTRL private command |

<a id="app-anc-api-reference"></a>

## APP\_ANC API Reference

<a id="header-file"></a>

### Header File

- [common/app\_audio/app\_anc.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/common/app_audio/app_anc.h)

<a id="functions"></a>

### Functions

<a id="_CPPv419app_anc_get_versionv"></a>

<a id="_CPPv319app_anc_get_versionv"></a> <a id="_CPPv219app_anc_get_versionv"></a> <a id="app_anc_get_version__void"></a> <a id="app__anc_8h_1a662d15001957421801f3f216d0ff4857"></a> uint32\_t app\_anc\_get\_version(void)
:   get anc version

    返回:
    :   anc version

<a id="_CPPv418anc_anc_get_verstrv"></a>

<a id="_CPPv318anc_anc_get_verstrv"></a> <a id="_CPPv218anc_anc_get_verstrv"></a> <a id="anc_anc_get_verstr__void"></a> <a id="app__anc_8h_1aa3a51d4fae2a800d422123c7bd78bda5"></a> uint8\_t \*anc\_anc\_get\_verstr(void)
:   get anc version string

    返回:
    :   anc version string

<a id="_CPPv414app_anc_deinitv"></a>

<a id="_CPPv314app_anc_deinitv"></a> <a id="_CPPv214app_anc_deinitv"></a> <a id="app_anc_deinit__void"></a> <a id="app__anc_8h_1a9254df9eba1e76f730b35b9be7ea9117"></a> int32\_t app\_anc\_deinit(void)
:   turn off anc operate

    返回:
    :   status

<a id="_CPPv412app_anc_init7uint8_t"></a>

<a id="_CPPv312app_anc_init7uint8_t"></a> <a id="_CPPv212app_anc_init7uint8_t"></a> <a id="app_anc_init__uint8_t"></a> <a id="app__anc_8h_1abf98e9713b85c1cb244b1ab8657d1d9e"></a> int32\_t app\_anc\_init(uint8\_t anc\_mode)
:   turn on anc operate and initialize

    返回:
    :   status

<a id="_CPPv419app_anc_cmd_handlerPvP7uint8_tP8uint16_t"></a>

<a id="_CPPv319app_anc_cmd_handlerPvP7uint8_tP8uint16_t"></a> <a id="_CPPv219app_anc_cmd_handlerPvP7uint8_tP8uint16_t"></a> <a id="app_anc_cmd_handler__voidP.uint8_tP.uint16_tP"></a> <a id="app__anc_8h_1a31781707e33a462633b8476bdd44d9fb"></a> int app\_anc\_cmd\_handler(void \*pd, uint8\_t \*p\_out\_buffer, uint16\_t \*p\_out\_length)
:   handle anc command

    参数:
    :   - **\*pd** – **\[in\]** anc command(etc ANC\_CMD\_RESET\_TO\_DB…)
        - **\*p\_out\_buffer** – **\[out\]** process result to get
        - **\*p\_out\_length** – **\[out\]** process result length to get

    返回:
    :   status

<a id="_CPPv415app_anc_is_openv"></a>

<a id="_CPPv315app_anc_is_openv"></a> <a id="_CPPv215app_anc_is_openv"></a> <a id="app_anc_is_open__void"></a> <a id="app__anc_8h_1a56fa629b01033628216379318e46b730"></a> bool app\_anc\_is\_open(void)
:   Enquiry anc is Enable or not.

    返回值:
    :   - **true** – is open
        - **false** – not open

    返回:
    :   status

<a id="_CPPv414app_anc_reopen7uint8_t"></a>

<a id="_CPPv314app_anc_reopen7uint8_t"></a> <a id="_CPPv214app_anc_reopen7uint8_t"></a> <a id="app_anc_reopen__uint8_t"></a> <a id="app__anc_8h_1a1a166ef87a4d9a4576e1462c4b742ae7"></a> void app\_anc\_reopen(uint8\_t type)
:   re-open anc function

    参数:
    :   **type** – **\[in\]** Controls to be turned on or off dac(etc ANC\_REOPEN\_ON\_START,ANC\_REOPEN\_ON\_STOP)

    返回:
    :   N/A

<a id="_CPPv419app_anc_reset_audiov"></a>

<a id="_CPPv319app_anc_reset_audiov"></a> <a id="_CPPv219app_anc_reset_audiov"></a> <a id="app_anc_reset_audio__void"></a> <a id="app__anc_8h_1a05b49c185b65dce84f11b62e93a25cf9"></a> void app\_anc\_reset\_audio(void)
:   reset g\_audio\_env

    返回:
    :   N/A

<a id="_CPPv415app_anc_fade_in7uint8_t"></a>

<a id="_CPPv315app_anc_fade_in7uint8_t"></a> <a id="_CPPv215app_anc_fade_in7uint8_t"></a> <a id="app_anc_fade_in__uint8_t"></a> <a id="app__anc_8h_1a1ac3eb06d5f06c2bb22a1d6528f5efc3"></a> void app\_anc\_fade\_in(uint8\_t path)
:   setting fade in of p\_path\_ctrl variables

    参数:
    :   **path** – **\[in\]** ANC path(etc:ANC\_PATH\_FF\_L,ANC\_PATH\_TS\_L…)

    返回:
    :   N/A

<a id="_CPPv416app_anc_fade_out7uint8_t"></a>

<a id="_CPPv316app_anc_fade_out7uint8_t"></a> <a id="_CPPv216app_anc_fade_out7uint8_t"></a> <a id="app_anc_fade_out__uint8_t"></a> <a id="app__anc_8h_1aeac2785ab7efcc33d0ff39e7d5165ed6"></a> void app\_anc\_fade\_out(uint8\_t path)
:   setting fade out of p\_path\_ctrl variables

    参数:
    :   **path** – **\[in\]** ANC path(etc:ANC\_PATH\_FF\_L,ANC\_PATH\_TS\_L…)

    返回:
    :   N/A

<a id="_CPPv431app_audio_anc_ctrl_noise_cancelv"></a>

<a id="_CPPv331app_audio_anc_ctrl_noise_cancelv"></a> <a id="_CPPv231app_audio_anc_ctrl_noise_cancelv"></a> <a id="app_audio_anc_ctrl_noise_cancel__void"></a> <a id="app__anc_8h_1a8327d0e0347145746ac4f2d4833a8fab"></a> void app\_audio\_anc\_ctrl\_noise\_cancel(void)
:   turn on anc function

    返回:
    :   N/A

<a id="_CPPv422app_audio_anc_ctrl_offv"></a>

<a id="_CPPv322app_audio_anc_ctrl_offv"></a> <a id="_CPPv222app_audio_anc_ctrl_offv"></a> <a id="app_audio_anc_ctrl_off__void"></a> <a id="app__anc_8h_1acff2ddfcb8b7fa6c8d87f7f2e6396a21"></a> void app\_audio\_anc\_ctrl\_off(void)
:   turn off anc function

    返回:
    :   N/A

<a id="_CPPv420app_anc_path_fade_in8uint32_t"></a>

<a id="_CPPv320app_anc_path_fade_in8uint32_t"></a> <a id="_CPPv220app_anc_path_fade_in8uint32_t"></a> <a id="app_anc_path_fade_in__uint32_t"></a> <a id="app__anc_8h_1a9099a2ccb9d20024d610f477f3811d4a"></a> void app\_anc\_path\_fade\_in(uint32\_t paths)
:   setting multi-path to fade in

    参数:
    :   **paths** – **\[in\]** voice paths AUDIO\_ANC\_PATH

    返回:
    :   N/A

<a id="_CPPv419app_anc_cache_resetv"></a>

<a id="_CPPv319app_anc_cache_resetv"></a> <a id="_CPPv219app_anc_cache_resetv"></a> <a id="app_anc_cache_reset__void"></a> <a id="app__anc_8h_1af59d94a1596186bd87710f7305baec36"></a> void app\_anc\_cache\_reset(void)
:   reset ec cache ram and reset anc digital gain

    返回:
    :   N/A

<a id="_CPPv424app_anc_get_current_gain7uint8_t"></a>

<a id="_CPPv324app_anc_get_current_gain7uint8_t"></a> <a id="_CPPv224app_anc_get_current_gain7uint8_t"></a> <a id="app_anc_get_current_gain__uint8_t"></a> <a id="app__anc_8h_1ae006e63aedb1d68f79476c24c4fa41eb"></a> uint32\_t app\_anc\_get\_current\_gain(uint8\_t path)
:   get digital gain from specify voice path

    参数:
    :   **path** – **\[in\]** voice path (etc: ANC\_PATH\_FF\_L,ANC\_PATH\_TS\_L,ANC\_PATH\_FB\_L…)

    返回:
    :   N/A

<a id="_CPPv419app_anc_button_ctrlv"></a>

<a id="_CPPv319app_anc_button_ctrlv"></a> <a id="_CPPv219app_anc_button_ctrlv"></a> <a id="app_anc_button_ctrl__void"></a> <a id="app__anc_8h_1ad743d5ee241ad2d6b195e70eb2a2f73f"></a> void app\_anc\_button\_ctrl(void)
:   anc button control

    Param :

<a id="_CPPv426app_anc_reset_coef_by_path8uint32_t"></a>

<a id="_CPPv326app_anc_reset_coef_by_path8uint32_t"></a> <a id="_CPPv226app_anc_reset_coef_by_path8uint32_t"></a> <a id="app_anc_reset_coef_by_path__uint32_t"></a> <a id="app__anc_8h_1a13008a15abb572b94ead9ec50002dee0"></a> void app\_anc\_reset\_coef\_by\_path(uint32\_t path)
:   app\_anc\_reset\_coef\_by\_path

    Param :

<a id="_CPPv422app_anc_rx_ctrl_handlePK7uint8_t8uint16_t"></a>

<a id="_CPPv322app_anc_rx_ctrl_handlePK7uint8_t8uint16_t"></a> <a id="_CPPv222app_anc_rx_ctrl_handlePK7uint8_t8uint16_t"></a> <a id="app_anc_rx_ctrl_handle__uint8_tCP.uint16_t"></a> <a id="app__anc_8h_1a851fe5cea5afed96da69cb424c0f2332"></a> void app\_anc\_rx\_ctrl\_handle(const uint8\_t \*p\_data, uint16\_t length)
:   handle TWS\_ANC\_CTRL private command

    参数:
    :   - **p\_data** – **\[in\]** command packet payload
        - **length** – **\[in\]** payload length

    返回:
    :   N/A

<a id="_CPPv415app_anc_sub_fsm13anc_subtype_t"></a>

<a id="_CPPv315app_anc_sub_fsm13anc_subtype_t"></a> <a id="_CPPv215app_anc_sub_fsm13anc_subtype_t"></a> <a id="app_anc_sub_fsm__anc_subtype_t"></a> <a id="app__anc_8h_1a5aa8f26a3eba01acc95c16bdeb810c63"></a> void app\_anc\_sub\_fsm([anc\_subtype\_t](#_CPPv413anc_subtype_t "anc_subtype_t") sub\_type\_cb)

<a id="unions"></a>

### Unions

<a id="_CPPv411variant32_t"></a>

<a id="_CPPv311variant32_t"></a> <a id="_CPPv211variant32_t"></a> <a id="unionvariant32__t"></a> union variant32\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N11variant32_t2i8E"></a>

    <a id="_CPPv3N11variant32_t2i8E"></a> <a id="_CPPv2N11variant32_t2i8E"></a> <a id="variant32_t::i8__int8_tA"></a> <a id="unionvariant32__t_1a3a6dde0935f847deba9c9c84520810ef"></a> int8\_t i8\[4\]

    <a id="_CPPv4N11variant32_t2u8E"></a>

    <a id="_CPPv3N11variant32_t2u8E"></a> <a id="_CPPv2N11variant32_t2u8E"></a> <a id="variant32_t::u8__uint8_tA"></a> <a id="unionvariant32__t_1ac54c1d1b5557ef7356e274ecc876182d"></a> uint8\_t u8\[4\]

    <a id="_CPPv4N11variant32_t3i16E"></a>

    <a id="_CPPv3N11variant32_t3i16E"></a> <a id="_CPPv2N11variant32_t3i16E"></a> <a id="variant32_t::i16__int16_tA"></a> <a id="unionvariant32__t_1aeb9fa0298432807402cb1455629a9333"></a> int16\_t i16\[2\]

    <a id="_CPPv4N11variant32_t3u16E"></a>

    <a id="_CPPv3N11variant32_t3u16E"></a> <a id="_CPPv2N11variant32_t3u16E"></a> <a id="variant32_t::u16__uint16_tA"></a> <a id="unionvariant32__t_1ac0cdb261a5632a3889f3e2df8d1ccc52"></a> uint16\_t u16\[2\]

    <a id="_CPPv4N11variant32_t3i32E"></a>

    <a id="_CPPv3N11variant32_t3i32E"></a> <a id="_CPPv2N11variant32_t3i32E"></a> <a id="variant32_t::i32__int32_t"></a> <a id="unionvariant32__t_1a1a9c398ec7d47b06ed42dc5e570f6dc4"></a> int32\_t i32

    <a id="_CPPv4N11variant32_t3u32E"></a>

    <a id="_CPPv3N11variant32_t3u32E"></a> <a id="_CPPv2N11variant32_t3u32E"></a> <a id="variant32_t::u32__uint32_t"></a> <a id="unionvariant32__t_1a63906e3328828d05fe50c5f4890df693"></a> uint32\_t u32

    <a id="_CPPv4N11variant32_t3f32E"></a>

    <a id="_CPPv3N11variant32_t3f32E"></a> <a id="_CPPv2N11variant32_t3f32E"></a> <a id="variant32_t::f32__float"></a> <a id="unionvariant32__t_1a5de29e0496848c64e50e0be10e6fafea"></a> float f32

<a id="structures"></a>

### Structures

<a id="_CPPv420biquad_filter_coef_t"></a>

<a id="_CPPv320biquad_filter_coef_t"></a> <a id="_CPPv220biquad_filter_coef_t"></a> <a id="biquad_filter_coef_t"></a> <a id="structbiquad__filter__coef__t"></a> struct biquad\_filter\_coef\_t

<a id="_CPPv410anc_para_t"></a>

<a id="_CPPv310anc_para_t"></a> <a id="_CPPv210anc_para_t"></a> <a id="anc_para_t"></a> <a id="structanc__para__t"></a> struct anc\_para\_t

<a id="_CPPv413anc_spp_cmd_t"></a>

<a id="_CPPv313anc_spp_cmd_t"></a> <a id="_CPPv213anc_spp_cmd_t"></a> <a id="anc_spp_cmd_t"></a> <a id="structanc__spp__cmd__t"></a> struct anc\_spp\_cmd\_t

<a id="_CPPv420anc_spp_filter_cmd_t"></a>

<a id="_CPPv320anc_spp_filter_cmd_t"></a> <a id="_CPPv220anc_spp_filter_cmd_t"></a> <a id="anc_spp_filter_cmd_t"></a> <a id="structanc__spp__filter__cmd__t"></a> struct anc\_spp\_filter\_cmd\_t

<a id="_CPPv416audio_anc_ctrl_t"></a>

<a id="_CPPv316audio_anc_ctrl_t"></a> <a id="_CPPv216audio_anc_ctrl_t"></a> <a id="audio_anc_ctrl_t"></a> <a id="structaudio__anc__ctrl__t"></a> struct audio\_anc\_ctrl\_t

<a id="macros"></a>

### Macros

<a id="c.ADC_ANA_STABLE_TIME_MS"></a>

<a id="app__anc_8h_1a46f9b9c52501d0fcd67210ad532d8019"></a> ADC\_ANA\_STABLE\_TIME\_MS

<a id="c.FADE_INOUT_TO_US"></a>

<a id="app__anc_8h_1a727fb7a0ac3a433ca01b0bf2b2d84b5f"></a> FADE\_INOUT\_TO\_US

<a id="c.NUM_0x9e8b3713"></a>

<a id="app__anc_8h_1a75852c544b8e7be5cf9de65ddc0ad751"></a> NUM\_0x9e8b3713

<a id="c.NUM_DEADBEAF"></a>

<a id="app__anc_8h_1a5943595fc4a9407e94052f5bc28a6fd3"></a> NUM\_DEADBEAF

<a id="c.ANC_DEF_FS"></a>

<a id="app__anc_8h_1a406785d1b01392945977762f8771926e"></a> ANC\_DEF\_FS

<a id="c.ANC_LSHIFTER_DEF_BITS"></a>

<a id="app__anc_8h_1a5169c9c8368808e213a059d7a2744462"></a> ANC\_LSHIFTER\_DEF\_BITS

<a id="c.ANC_OFF"></a>

<a id="app__anc_8h_1a3614e24cbe57b58aec6524846b966fb5"></a> ANC\_OFF

<a id="c.ANC_NOISE_CANCEL"></a>

<a id="app__anc_8h_1a1f432ae79ecf507cf9317ede338a1224"></a> ANC\_NOISE\_CANCEL

<a id="c.ANC_TRANSPANT"></a>

<a id="app__anc_8h_1a6706b9fc243df62549ae7964958ca80e"></a> ANC\_TRANSPANT

<a id="c.ANC_SUBTYPE_IDLE"></a>

<a id="app__anc_8h_1ab7bc57812464f23135f8d1e5c7ca7f28"></a> ANC\_SUBTYPE\_IDLE

<a id="c.ANC_SUBTYPE_W4_NOISE_CANCEL_HINT_DONE"></a>

<a id="app__anc_8h_1aa8214490babf86616f9fc4bd59959271"></a> ANC\_SUBTYPE\_W4\_NOISE\_CANCEL\_HINT\_DONE

<a id="c.ANC_SUBTYPE_W4_NOISE_CANCEL_DONE"></a>

<a id="app__anc_8h_1a54d9b897b2b8b60497345e7e228f972d"></a> ANC\_SUBTYPE\_W4\_NOISE\_CANCEL\_DONE

<a id="c.ANC_SUBTYPE_W4_TRANSPRANT_ANCOFF_DONE"></a>

<a id="app__anc_8h_1a73889aa66db6529d9ce70e04dc7a674c"></a> ANC\_SUBTYPE\_W4\_TRANSPRANT\_ANCOFF\_DONE

<a id="c.ANC_SUBTYPE_W4_TRANSPRANT_HINT_DONE"></a>

<a id="app__anc_8h_1a0a9d8b9dfd1c0b756599397740a17856"></a> ANC\_SUBTYPE\_W4\_TRANSPRANT\_HINT\_DONE

<a id="c.ANC_SUBTYPE_W4_TRANSPRANT_DONE"></a>

<a id="app__anc_8h_1a675de73dfc6fd3b59ef82555dd7a0328"></a> ANC\_SUBTYPE\_W4\_TRANSPRANT\_DONE

<a id="c.ANC_SUBTYPE_W4_ANC_OFF_DONE"></a>

<a id="app__anc_8h_1a5c2800055c2e067ebff688b4a41af6a5"></a> ANC\_SUBTYPE\_W4\_ANC\_OFF\_DONE

<a id="c.ANC_SUBTYPE_W4_ANC_OFF_HINT_DONE"></a>

<a id="app__anc_8h_1a41446f99dbc2fc36915da1e4ea20b846"></a> ANC\_SUBTYPE\_W4\_ANC\_OFF\_HINT\_DONE

<a id="c.CHECK_PATH_10X"></a>

<a id="app__anc_8h_1a9fa34d1f0172a6bcbd97bbb7b3ae3a6d"></a> CHECK\_PATH\_10X(path)

<a id="c.CHECK_PATH_8X"></a>

<a id="app__anc_8h_1acc0cff43643df4e0544fb12af087125b"></a> CHECK\_PATH\_8X(path)

<a id="c.SPP_CMD_SYNCWORD"></a>

<a id="app__anc_8h_1abb7d5c439c83080d475f1a438956e08f"></a> SPP\_CMD\_SYNCWORD

<a id="c.SPP_RSP_SYNCWORD"></a>

<a id="app__anc_8h_1a89d7b743c3fd8c7fa2e2c2a9544ec4ce"></a> SPP\_RSP\_SYNCWORD

<a id="c.SPP_TEST_CMD_LEN"></a>

<a id="app__anc_8h_1af389d7e842493c88c38e555808d38d3b"></a> SPP\_TEST\_CMD\_LEN

<a id="c.SPP_RSP_FORMAT_1"></a>

<a id="app__anc_8h_1ab065e924159e5b1de8469b336a237754"></a> SPP\_RSP\_FORMAT\_1

<a id="c.SPP_RSP_FORMAT_2"></a>

<a id="app__anc_8h_1a8bf92b7073f7d08b8d9068e284e6cba7"></a> SPP\_RSP\_FORMAT\_2

<a id="c.SPP_FILTER_CMD_LEN"></a>

<a id="app__anc_8h_1a4e5144993955ed2597dd82beeaba9f72"></a> SPP\_FILTER\_CMD\_LEN

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv410anc_type_t"></a>

<a id="_CPPv310anc_type_t"></a> <a id="_CPPv210anc_type_t"></a> <a id="anc_type_t"></a> <a id="app__anc_8h_1a93978716b13b85520525166401e24f04"></a> typedef uint8\_t anc\_type\_t

<a id="_CPPv413anc_subtype_t"></a>

<a id="_CPPv313anc_subtype_t"></a> <a id="_CPPv213anc_subtype_t"></a> <a id="anc_subtype_t"></a> <a id="app__anc_8h_1a6ba8498c47ceaf015ef385bb8cd20168"></a> typedef uint8\_t anc\_subtype\_t

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv4Ut1_0"></a>

<a id="_CPPv3Ut1_0"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55b"></a> enum \[anonymous\]
:   *Values:*

    <a id="_CPPv4NUt1_022ANC_CMD_ENTER_TESTMODEE"></a>

    <a id="_CPPv3NUt1_022ANC_CMD_ENTER_TESTMODEE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba4e90a21bf30d8a94e8674dee3d803c64"></a> enumerator ANC\_CMD\_ENTER\_TESTMODE

    <a id="_CPPv4NUt1_022ANC_CMD_MASTER_IS_LEFTE"></a>

    <a id="_CPPv3NUt1_022ANC_CMD_MASTER_IS_LEFTE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55baf50ca1ded3a1bb44928d37accc3ffe38"></a> enumerator ANC\_CMD\_MASTER\_IS\_LEFT

    <a id="_CPPv4NUt1_015ANC_CMD_ANC_OFFE"></a>

    <a id="_CPPv3NUt1_015ANC_CMD_ANC_OFFE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba55627983385e55dbde79fdc5b62c697b"></a> enumerator ANC\_CMD\_ANC\_OFF

    <a id="_CPPv4NUt1_014ANC_CMD_ANC_ONE"></a>

    <a id="_CPPv3NUt1_014ANC_CMD_ANC_ONE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba805e81ec4d1ca2617556bbb43f072828"></a> enumerator ANC\_CMD\_ANC\_ON

    <a id="_CPPv4NUt1_016ANC_CMD_SET_GAINE"></a>

    <a id="_CPPv3NUt1_016ANC_CMD_SET_GAINE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba107a573f344e82394a0b416d04348c8f"></a> enumerator ANC\_CMD\_SET\_GAIN

    <a id="_CPPv4NUt1_018ANC_CMD_WRITE_GAINE"></a>

    <a id="_CPPv3NUt1_018ANC_CMD_WRITE_GAINE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba05e29c505c0663194cec6abcbccfef48"></a> enumerator ANC\_CMD\_WRITE\_GAIN

    <a id="_CPPv4NUt1_017ANC_CMD_READ_GAINE"></a>

    <a id="_CPPv3NUt1_017ANC_CMD_READ_GAINE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba88bbb3c7c3b7ce3d47cbc85205fef703"></a> enumerator ANC\_CMD\_READ\_GAIN

    <a id="_CPPv4NUt1_027ANC_CMD_ANC_WHITE_NOISE_OUTE"></a>

    <a id="_CPPv3NUt1_027ANC_CMD_ANC_WHITE_NOISE_OUTE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba945ae3d903d69f98ae413edafe7a8593"></a> enumerator ANC\_CMD\_ANC\_WHITE\_NOISE\_OUT

    <a id="_CPPv4NUt1_021ANC_CMD_ANC_PULSE_OUTE"></a>

    <a id="_CPPv3NUt1_021ANC_CMD_ANC_PULSE_OUTE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba395ce46086205d15a7aee9319576f595"></a> enumerator ANC\_CMD\_ANC\_PULSE\_OUT

    <a id="_CPPv4NUt1_021ANC_CMD_FILTER_UPDATEE"></a>

    <a id="_CPPv3NUt1_021ANC_CMD_FILTER_UPDATEE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55bac158ef0553c8e27daaa0589c9d26dfd6"></a> enumerator ANC\_CMD\_FILTER\_UPDATE

    <a id="_CPPv4NUt1_020ANC_CMD_FILTER_WRITEE"></a>

    <a id="_CPPv3NUt1_020ANC_CMD_FILTER_WRITEE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55baeedd67b55092fd0da629db7fc305e3b8"></a> enumerator ANC\_CMD\_FILTER\_WRITE

    <a id="_CPPv4NUt1_020ANC_CMD_TRANSPARENCYE"></a>

    <a id="_CPPv3NUt1_020ANC_CMD_TRANSPARENCYE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba86999af3de1093cd42b1ed67d83cac73"></a> enumerator ANC\_CMD\_TRANSPARENCY

    <a id="_CPPv4NUt1_019ANC_CMD_MASTER_PLUSE"></a>

    <a id="_CPPv3NUt1_019ANC_CMD_MASTER_PLUSE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba7a5c22a5f2c6a0bfdd5d38c5d89e4b19"></a> enumerator ANC\_CMD\_MASTER\_PLUS

    <a id="_CPPv4NUt1_020ANC_CMD_MASTER_MINUSE"></a>

    <a id="_CPPv3NUt1_020ANC_CMD_MASTER_MINUSE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba957a8f6152fb606d3224d8763addaddc"></a> enumerator ANC\_CMD\_MASTER\_MINUS

    <a id="_CPPv4NUt1_018ANC_CMD_SLAVE_PLUSE"></a>

    <a id="_CPPv3NUt1_018ANC_CMD_SLAVE_PLUSE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba2f685070b696d4bf49e3d58cd094476e"></a> enumerator ANC\_CMD\_SLAVE\_PLUS

    <a id="_CPPv4NUt1_019ANC_CMD_SLAVE_MINUSE"></a>

    <a id="_CPPv3NUt1_019ANC_CMD_SLAVE_MINUSE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55bab4577df7e2f44d6bc1225e7423385eff"></a> enumerator ANC\_CMD\_SLAVE\_MINUS

    <a id="_CPPv4NUt1_019ANC_CMD_MASTER_SAVEE"></a>

    <a id="_CPPv3NUt1_019ANC_CMD_MASTER_SAVEE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55bacaf7eb7695d183a0cf70588d4c3570b6"></a> enumerator ANC\_CMD\_MASTER\_SAVE

    <a id="_CPPv4NUt1_018ANC_CMD_SLAVE_SAVEE"></a>

    <a id="_CPPv3NUt1_018ANC_CMD_SLAVE_SAVEE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba1443b6c1b53e25054a6b49f094b5aff5"></a> enumerator ANC\_CMD\_SLAVE\_SAVE

    <a id="_CPPv4NUt1_022ANC_CMD_SLAVE_SET_GAINE"></a>

    <a id="_CPPv3NUt1_022ANC_CMD_SLAVE_SET_GAINE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba3de9ff0081f5874f01d1530a1a4bac7a"></a> enumerator ANC\_CMD\_SLAVE\_SET\_GAIN

    <a id="_CPPv4NUt1_023ANC_CMD_MASTER_SET_GAINE"></a>

    <a id="_CPPv3NUt1_023ANC_CMD_MASTER_SET_GAINE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55baf0737f5f45a107a8c49a71b6621c2c5a"></a> enumerator ANC\_CMD\_MASTER\_SET\_GAIN

    <a id="_CPPv4NUt1_019ANC_CMD_RESET_TO_DBE"></a>

    <a id="_CPPv3NUt1_019ANC_CMD_RESET_TO_DBE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55baccee594ea8f63162cc208015d8aa0a03"></a> enumerator ANC\_CMD\_RESET\_TO\_DB

    <a id="_CPPv4NUt1_020ANC_CMD_CTRL_LIMITERE"></a>

    <a id="_CPPv3NUt1_020ANC_CMD_CTRL_LIMITERE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba507cf526059df1bcf8578b52b5b2a0e9"></a> enumerator ANC\_CMD\_CTRL\_LIMITER

    <a id="_CPPv4NUt1_021ANC_CMD_STATUS_SWITCHE"></a>

    <a id="_CPPv3NUt1_021ANC_CMD_STATUS_SWITCHE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55bab7f97ffffd117ccde2cd839a2889be53"></a> enumerator ANC\_CMD\_STATUS\_SWITCH

    <a id="_CPPv4NUt1_021ANC_CMD_PATH_CFG_READE"></a>

    <a id="_CPPv3NUt1_021ANC_CMD_PATH_CFG_READE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba3bffda32e26a8e0ca054a5b009101334"></a> enumerator ANC\_CMD\_PATH\_CFG\_READ

    <a id="_CPPv4NUt1_016ANC_CMD_CTRL_I2SE"></a>

    <a id="_CPPv3NUt1_016ANC_CMD_CTRL_I2SE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55baab3c01f56c3a8f7a87cdb273673e2378"></a> enumerator ANC\_CMD\_CTRL\_I2S

    <a id="_CPPv4NUt1_025ANC_CMD_CTRL_ANA_GAIN_SETE"></a>

    <a id="_CPPv3NUt1_025ANC_CMD_CTRL_ANA_GAIN_SETE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55bab7895feeadfc2f32e4d3fee9dd1c97a1"></a> enumerator ANC\_CMD\_CTRL\_ANA\_GAIN\_SET

    <a id="_CPPv4NUt1_022ANC_CMD_MATCH_GAIN_UPDE"></a>

    <a id="_CPPv3NUt1_022ANC_CMD_MATCH_GAIN_UPDE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55bae2cc8ff6174fb96347ffa9e25ea17e2f"></a> enumerator ANC\_CMD\_MATCH\_GAIN\_UPD

    <a id="_CPPv4NUt1_016ANC_CMD_GAIN_UPDE"></a>

    <a id="_CPPv3NUt1_016ANC_CMD_GAIN_UPDE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55baf80f7dd29df2438e9301f1303d03869c"></a> enumerator ANC\_CMD\_GAIN\_UPD

    <a id="_CPPv4NUt1_020ANC_CMD_FLT_COEF_UPDE"></a>

    <a id="_CPPv3NUt1_020ANC_CMD_FLT_COEF_UPDE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba3e6d949e8640a293d133648bcea964ed"></a> enumerator ANC\_CMD\_FLT\_COEF\_UPD

    <a id="_CPPv4NUt1_019ANC_CMD_CTRL_BYPASSE"></a>

    <a id="_CPPv3NUt1_019ANC_CMD_CTRL_BYPASSE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba7b81a189a7681bf325f8b6dce33d5f47"></a> enumerator ANC\_CMD\_CTRL\_BYPASS

    <a id="_CPPv4NUt1_018ANC_CMD_CTRL_CLEARE"></a>

    <a id="_CPPv3NUt1_018ANC_CMD_CTRL_CLEARE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba0b3ea5ece375be391d190439f677c0d4"></a> enumerator ANC\_CMD\_CTRL\_CLEAR

    <a id="_CPPv4NUt1_021ANC_CMD_RESET_TO_NONEE"></a>

    <a id="_CPPv3NUt1_021ANC_CMD_RESET_TO_NONEE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55bad6700d779f672e8b894bd239036b6d1a"></a> enumerator ANC\_CMD\_RESET\_TO\_NONE

    <a id="_CPPv4NUt1_022ANC_CMD_DBGAIN_INVERSEE"></a>

    <a id="_CPPv3NUt1_022ANC_CMD_DBGAIN_INVERSEE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba9f32708faaca62686f9254c1eb80e34e"></a> enumerator ANC\_CMD\_DBGAIN\_INVERSE

    <a id="_CPPv4NUt1_018ANC_CMD_ANC_ON_OFFE"></a>

    <a id="_CPPv3NUt1_018ANC_CMD_ANC_ON_OFFE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba9880a9d4a6b4d094c93cc86c3167df20"></a> enumerator ANC\_CMD\_ANC\_ON\_OFF

    <a id="_CPPv4NUt1_028ANC_CMD_FILTER_BYPASS_ON_OFFE"></a>

    <a id="_CPPv3NUt1_028ANC_CMD_FILTER_BYPASS_ON_OFFE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55bae2c4179efc0c4f21925e6d98675bd03b"></a> enumerator ANC\_CMD\_FILTER\_BYPASS\_ON\_OFF

    <a id="_CPPv4NUt1_021ANC_CMD_DBGAIN_UPDATEE"></a>

    <a id="_CPPv3NUt1_021ANC_CMD_DBGAIN_UPDATEE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55bafe4a782f63341a8b21b5e9240235b7e9"></a> enumerator ANC\_CMD\_DBGAIN\_UPDATE

    <a id="_CPPv4NUt1_020ANC_CMD_DBGAIN_WRITEE"></a>

    <a id="_CPPv3NUt1_020ANC_CMD_DBGAIN_WRITEE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba006d4f712bf53b58080d62a7454f1a73"></a> enumerator ANC\_CMD\_DBGAIN\_WRITE

    <a id="_CPPv4NUt1_019ANC_CMD_DBGAIN_READE"></a>

    <a id="_CPPv3NUt1_019ANC_CMD_DBGAIN_READE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba7fbab96b86dd9bbcab3b2e513234eef3"></a> enumerator ANC\_CMD\_DBGAIN\_READ

    <a id="_CPPv4NUt1_019ANC_CMD_STATUS_SYNCE"></a>

    <a id="_CPPv3NUt1_019ANC_CMD_STATUS_SYNCE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba0f7a38165c3d1fb5570f5dd3093693bf"></a> enumerator ANC\_CMD\_STATUS\_SYNC

    <a id="_CPPv4NUt1_022ANC_CMD_FILTER_REVERSEE"></a>

    <a id="_CPPv3NUt1_022ANC_CMD_FILTER_REVERSEE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba0afe9e0ac2a7485832fd64d5145ecfc5"></a> enumerator ANC\_CMD\_FILTER\_REVERSE

    <a id="_CPPv4NUt1_022ANC_CMD_ENHANCED_TS_ENE"></a>

    <a id="_CPPv3NUt1_022ANC_CMD_ENHANCED_TS_ENE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba599a90f58329d853538f9b00f5ac770d"></a> enumerator ANC\_CMD\_ENHANCED\_TS\_EN

    <a id="_CPPv4NUt1_016ANC_CMD_ANC_MODEE"></a>

    <a id="_CPPv3NUt1_016ANC_CMD_ANC_MODEE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba87757d1f02706821b141171e0e88e2ec"></a> enumerator ANC\_CMD\_ANC\_MODE

    <a id="_CPPv4NUt1_017ANC_CMD_PATH_CTRLE"></a>

    <a id="_CPPv3NUt1_017ANC_CMD_PATH_CTRLE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba8a9e0030eda106920f92f51d3667a756"></a> enumerator ANC\_CMD\_PATH\_CTRL

    <a id="_CPPv4NUt1_029ANC_CMD_STORE_ALL_MATCH_PARAME"></a>

    <a id="_CPPv3NUt1_029ANC_CMD_STORE_ALL_MATCH_PARAME"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55baef9b3e87365b572020e63b968c5aad9a"></a> enumerator ANC\_CMD\_STORE\_ALL\_MATCH\_PARAM

    <a id="_CPPv4NUt1_030ANC_CMD_STORE_ALL_DESIGN_PARAME"></a>

    <a id="_CPPv3NUt1_030ANC_CMD_STORE_ALL_DESIGN_PARAME"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba721f45755b1b1d496f4305e57d0739a1"></a> enumerator ANC\_CMD\_STORE\_ALL\_DESIGN\_PARAM

    <a id="_CPPv4NUt1_021ANC_CMD_LIMITER_THRESE"></a>

    <a id="_CPPv3NUt1_021ANC_CMD_LIMITER_THRESE"></a> <a id="app__anc_8h_1a06fc87d81c62e9abb8790b6e5713c55ba026def337e1ac82838267adb7feca41f"></a> enumerator ANC\_CMD\_LIMITER\_THRES

<a id="_CPPv4Ut1_1"></a>

<a id="_CPPv3Ut1_1"></a> <a id="app__anc_8h_1adf764cbdea00d65edcd07bb9953ad2b7"></a> enum \[anonymous\]
:   *Values:*

    <a id="_CPPv4NUt1_119ANC_HFP_CMD_ANC_OFFE"></a>

    <a id="_CPPv3NUt1_119ANC_HFP_CMD_ANC_OFFE"></a> <a id="app__anc_8h_1adf764cbdea00d65edcd07bb9953ad2b7ad12a92228a4a85a67d4ef7c1d3d919c4"></a> enumerator ANC\_HFP\_CMD\_ANC\_OFF

    <a id="_CPPv4NUt1_118ANC_HFP_CMD_ANC_ONE"></a>

    <a id="_CPPv3NUt1_118ANC_HFP_CMD_ANC_ONE"></a> <a id="app__anc_8h_1adf764cbdea00d65edcd07bb9953ad2b7a4144668dbf23a24ec3f2fa589c110090"></a> enumerator ANC\_HFP\_CMD\_ANC\_ON

    <a id="_CPPv4NUt1_120ANC_HFP_CMD_SET_GAINE"></a>

    <a id="_CPPv3NUt1_120ANC_HFP_CMD_SET_GAINE"></a> <a id="app__anc_8h_1adf764cbdea00d65edcd07bb9953ad2b7a17eace0d96153861f90d217ffa2e9520"></a> enumerator ANC\_HFP\_CMD\_SET\_GAIN

    <a id="_CPPv4NUt1_122ANC_HFP_CMD_WRITE_GAINE"></a>

    <a id="_CPPv3NUt1_122ANC_HFP_CMD_WRITE_GAINE"></a> <a id="app__anc_8h_1adf764cbdea00d65edcd07bb9953ad2b7a101a08f60c8d02b2b4d1f90d1c7cff02"></a> enumerator ANC\_HFP\_CMD\_WRITE\_GAIN

    <a id="_CPPv4NUt1_121ANC_HFP_CMD_READ_GAINE"></a>

    <a id="_CPPv3NUt1_121ANC_HFP_CMD_READ_GAINE"></a> <a id="app__anc_8h_1adf764cbdea00d65edcd07bb9953ad2b7a741aaa436f5f02316ec54e50d8fd4be7"></a> enumerator ANC\_HFP\_CMD\_READ\_GAIN

    <a id="_CPPv4NUt1_111ANC_HFP_RSPE"></a>

    <a id="_CPPv3NUt1_111ANC_HFP_RSPE"></a> <a id="app__anc_8h_1adf764cbdea00d65edcd07bb9953ad2b7a88ed3a66445ca301947dc19fe5da3ef1"></a> enumerator ANC\_HFP\_RSP

    <a id="_CPPv4NUt1_124ANC_HFP_CMD_TRANSPARENCYE"></a>

    <a id="_CPPv3NUt1_124ANC_HFP_CMD_TRANSPARENCYE"></a> <a id="app__anc_8h_1adf764cbdea00d65edcd07bb9953ad2b7ac6faf61377da9b14dbece759bf76ad14"></a> enumerator ANC\_HFP\_CMD\_TRANSPARENCY

    <a id="_CPPv4NUt1_116ANC_HFP_CMD_PLUSE"></a>

    <a id="_CPPv3NUt1_116ANC_HFP_CMD_PLUSE"></a> <a id="app__anc_8h_1adf764cbdea00d65edcd07bb9953ad2b7a4432074ba10acd3acc3515d71eef75ee"></a> enumerator ANC\_HFP\_CMD\_PLUS

    <a id="_CPPv4NUt1_117ANC_HFP_CMD_MINUSE"></a>

    <a id="_CPPv3NUt1_117ANC_HFP_CMD_MINUSE"></a> <a id="app__anc_8h_1adf764cbdea00d65edcd07bb9953ad2b7a03051510b5676a13d65d208ef490dc19"></a> enumerator ANC\_HFP\_CMD\_MINUS

    <a id="_CPPv4NUt1_116ANC_HFP_CMD_SAVEE"></a>

    <a id="_CPPv3NUt1_116ANC_HFP_CMD_SAVEE"></a> <a id="app__anc_8h_1adf764cbdea00d65edcd07bb9953ad2b7a8a731d198425ab6f2f5cc82fc7d228a1"></a> enumerator ANC\_HFP\_CMD\_SAVE

    <a id="_CPPv4NUt1_125ANC_HFP_CMD_SET_GAIN_TESTE"></a>

    <a id="_CPPv3NUt1_125ANC_HFP_CMD_SET_GAIN_TESTE"></a> <a id="app__anc_8h_1adf764cbdea00d65edcd07bb9953ad2b7a3c9f7a44e6d7833fcfdc3d4c291feb04"></a> enumerator ANC\_HFP\_CMD\_SET\_GAIN\_TEST

    <a id="_CPPv4NUt1_131ANC_HFP_CMD_ANC_WHITE_NOISE_OUTE"></a>

    <a id="_CPPv3NUt1_131ANC_HFP_CMD_ANC_WHITE_NOISE_OUTE"></a> <a id="app__anc_8h_1adf764cbdea00d65edcd07bb9953ad2b7af222354887891fa406cd310960b15e44"></a> enumerator ANC\_HFP\_CMD\_ANC\_WHITE\_NOISE\_OUT

    <a id="_CPPv4NUt1_125ANC_HFP_CMD_ANC_PULSE_OUTE"></a>

    <a id="_CPPv3NUt1_125ANC_HFP_CMD_ANC_PULSE_OUTE"></a> <a id="app__anc_8h_1adf764cbdea00d65edcd07bb9953ad2b7a1ce566013e442306581ebd97a7d88a9f"></a> enumerator ANC\_HFP\_CMD\_ANC\_PULSE\_OUT

    <a id="_CPPv4NUt1_124ANC_HFP_CMD_FILTER_WRITEE"></a>

    <a id="_CPPv3NUt1_124ANC_HFP_CMD_FILTER_WRITEE"></a> <a id="app__anc_8h_1adf764cbdea00d65edcd07bb9953ad2b7a2932511f2f710b92092b75f24e15f4b0"></a> enumerator ANC\_HFP\_CMD\_FILTER\_WRITE

    <a id="_CPPv4NUt1_125ANC_HFP_CMD_FILTER_UPDATEE"></a>

    <a id="_CPPv3NUt1_125ANC_HFP_CMD_FILTER_UPDATEE"></a> <a id="app__anc_8h_1adf764cbdea00d65edcd07bb9953ad2b7a480aae6e9165529d03e6087efc145496"></a> enumerator ANC\_HFP\_CMD\_FILTER\_UPDATE

<a id="_CPPv411eq_filter_e"></a>

<a id="_CPPv311eq_filter_e"></a> <a id="_CPPv211eq_filter_e"></a> <a id="app__anc_8h_1a87a7a36fbb96cd39edbd0fea5daf1522"></a> enum eq\_filter\_e
:   *Values:*

    <a id="_CPPv4N11eq_filter_e21EQ_FILTER_TYPE_UNKNOWE"></a>

    <a id="_CPPv3N11eq_filter_e21EQ_FILTER_TYPE_UNKNOWE"></a> <a id="_CPPv2N11eq_filter_e21EQ_FILTER_TYPE_UNKNOWE"></a> <a id="app__anc_8h_1a87a7a36fbb96cd39edbd0fea5daf1522a328e9e78fa9f1a627133dcfe06c1cc1f"></a> enumerator EQ\_FILTER\_TYPE\_UNKNOW

    <a id="_CPPv4N11eq_filter_e22EQ_FILTER_TYPE_PEAKINGE"></a>

    <a id="_CPPv3N11eq_filter_e22EQ_FILTER_TYPE_PEAKINGE"></a> <a id="_CPPv2N11eq_filter_e22EQ_FILTER_TYPE_PEAKINGE"></a> <a id="app__anc_8h_1a87a7a36fbb96cd39edbd0fea5daf1522a58aae6197b6bb565633b9138f0781ff2"></a> enumerator EQ\_FILTER\_TYPE\_PEAKING

    <a id="_CPPv4N11eq_filter_e24EQ_FILTER_TYPE_LOW_SHELFE"></a>

    <a id="_CPPv3N11eq_filter_e24EQ_FILTER_TYPE_LOW_SHELFE"></a> <a id="_CPPv2N11eq_filter_e24EQ_FILTER_TYPE_LOW_SHELFE"></a> <a id="app__anc_8h_1a87a7a36fbb96cd39edbd0fea5daf1522abd05a5d610e30ebadb3c712e2bbb360d"></a> enumerator EQ\_FILTER\_TYPE\_LOW\_SHELF

    <a id="_CPPv4N11eq_filter_e25EQ_FILTER_TYPE_HIGH_SHELFE"></a>

    <a id="_CPPv3N11eq_filter_e25EQ_FILTER_TYPE_HIGH_SHELFE"></a> <a id="_CPPv2N11eq_filter_e25EQ_FILTER_TYPE_HIGH_SHELFE"></a> <a id="app__anc_8h_1a87a7a36fbb96cd39edbd0fea5daf1522ad5f294e9cc5a50b14d7735aa6e1c4132"></a> enumerator EQ\_FILTER\_TYPE\_HIGH\_SHELF

    <a id="_CPPv4N11eq_filter_e23EQ_FILTER_TYPE_LOW_PASSE"></a>

    <a id="_CPPv3N11eq_filter_e23EQ_FILTER_TYPE_LOW_PASSE"></a> <a id="_CPPv2N11eq_filter_e23EQ_FILTER_TYPE_LOW_PASSE"></a> <a id="app__anc_8h_1a87a7a36fbb96cd39edbd0fea5daf1522a2d4cae803a7769b674832f431398bc86"></a> enumerator EQ\_FILTER\_TYPE\_LOW\_PASS

    <a id="_CPPv4N11eq_filter_e24EQ_FILTER_TYPE_HIGH_PASSE"></a>

    <a id="_CPPv3N11eq_filter_e24EQ_FILTER_TYPE_HIGH_PASSE"></a> <a id="_CPPv2N11eq_filter_e24EQ_FILTER_TYPE_HIGH_PASSE"></a> <a id="app__anc_8h_1a87a7a36fbb96cd39edbd0fea5daf1522a63f84fb690000f8e82924b10f07a86ed"></a> enumerator EQ\_FILTER\_TYPE\_HIGH\_PASS

    <a id="_CPPv4N11eq_filter_e24EQ_FILTER_TYPE_BAND_PASSE"></a>

    <a id="_CPPv3N11eq_filter_e24EQ_FILTER_TYPE_BAND_PASSE"></a> <a id="_CPPv2N11eq_filter_e24EQ_FILTER_TYPE_BAND_PASSE"></a> <a id="app__anc_8h_1a87a7a36fbb96cd39edbd0fea5daf1522a8885e1fc15bef7ccc72540838a3fde89"></a> enumerator EQ\_FILTER\_TYPE\_BAND\_PASS

    <a id="_CPPv4N11eq_filter_e20EQ_FILTER_TYPE_NOTCHE"></a>

    <a id="_CPPv3N11eq_filter_e20EQ_FILTER_TYPE_NOTCHE"></a> <a id="_CPPv2N11eq_filter_e20EQ_FILTER_TYPE_NOTCHE"></a> <a id="app__anc_8h_1a87a7a36fbb96cd39edbd0fea5daf1522a7bba2ea18957d08bb1e29187981b1bdc"></a> enumerator EQ\_FILTER\_TYPE\_NOTCH

    <a id="_CPPv4N11eq_filter_e23EQ_FILTER_TYPE_ALL_PASSE"></a>

    <a id="_CPPv3N11eq_filter_e23EQ_FILTER_TYPE_ALL_PASSE"></a> <a id="_CPPv2N11eq_filter_e23EQ_FILTER_TYPE_ALL_PASSE"></a> <a id="app__anc_8h_1a87a7a36fbb96cd39edbd0fea5daf1522afae98e25a13d67b805859ac1d5d3ef9e"></a> enumerator EQ\_FILTER\_TYPE\_ALL\_PASS

<a id="_CPPv4Ut1_2"></a>

<a id="_CPPv3Ut1_2"></a> <a id="app__anc_8h_1a99fb83031ce9923c84392b4e92f956b5"></a> enum \[anonymous\]
:   *Values:*

    <a id="_CPPv4NUt1_213ANC_PATH_FF_LE"></a>

    <a id="_CPPv3NUt1_213ANC_PATH_FF_LE"></a> <a id="app__anc_8h_1a99fb83031ce9923c84392b4e92f956b5aa018c1045701bbdcd6059e5c90b961e5"></a> enumerator ANC\_PATH\_FF\_L

    <a id="_CPPv4NUt1_213ANC_PATH_TS_LE"></a>

    <a id="_CPPv3NUt1_213ANC_PATH_TS_LE"></a> <a id="app__anc_8h_1a99fb83031ce9923c84392b4e92f956b5ad3730ee6a53b3d5e51fc0d8c4efbbd99"></a> enumerator ANC\_PATH\_TS\_L

    <a id="_CPPv4NUt1_213ANC_PATH_FB_LE"></a>

    <a id="_CPPv3NUt1_213ANC_PATH_FB_LE"></a> <a id="app__anc_8h_1a99fb83031ce9923c84392b4e92f956b5ac6e96c668a4c660c40c478f7bec15203"></a> enumerator ANC\_PATH\_FB\_L

    <a id="_CPPv4NUt1_213ANC_PATH_EC_LE"></a>

    <a id="_CPPv3NUt1_213ANC_PATH_EC_LE"></a> <a id="app__anc_8h_1a99fb83031ce9923c84392b4e92f956b5a817b6d6007d05972ebacff17ac1fcac2"></a> enumerator ANC\_PATH\_EC\_L

    <a id="_CPPv4NUt1_213ANC_PATH_TF_LE"></a>

    <a id="_CPPv3NUt1_213ANC_PATH_TF_LE"></a> <a id="app__anc_8h_1a99fb83031ce9923c84392b4e92f956b5a32fce53decefd0c5a24c5f6e0ec110e7"></a> enumerator ANC\_PATH\_TF\_L

    <a id="_CPPv4NUt1_213ANC_PATH_TE_LE"></a>

    <a id="_CPPv3NUt1_213ANC_PATH_TE_LE"></a> <a id="app__anc_8h_1a99fb83031ce9923c84392b4e92f956b5a96a09896b8c5642de4302d2c02c8dfd9"></a> enumerator ANC\_PATH\_TE\_L

    <a id="_CPPv4NUt1_213ANC_PATH_FF_RE"></a>

    <a id="_CPPv3NUt1_213ANC_PATH_FF_RE"></a> <a id="app__anc_8h_1a99fb83031ce9923c84392b4e92f956b5aebd4945f0c8da65f905b623538e4ff24"></a> enumerator ANC\_PATH\_FF\_R

    <a id="_CPPv4NUt1_213ANC_PATH_TS_RE"></a>

    <a id="_CPPv3NUt1_213ANC_PATH_TS_RE"></a> <a id="app__anc_8h_1a99fb83031ce9923c84392b4e92f956b5a07195a97eea54ec675c8a5a342925145"></a> enumerator ANC\_PATH\_TS\_R

    <a id="_CPPv4NUt1_213ANC_PATH_FB_RE"></a>

    <a id="_CPPv3NUt1_213ANC_PATH_FB_RE"></a> <a id="app__anc_8h_1a99fb83031ce9923c84392b4e92f956b5a8227bc4294c5b29ee2a0616402d4eed5"></a> enumerator ANC\_PATH\_FB\_R

    <a id="_CPPv4NUt1_213ANC_PATH_EC_RE"></a>

    <a id="_CPPv3NUt1_213ANC_PATH_EC_RE"></a> <a id="app__anc_8h_1a99fb83031ce9923c84392b4e92f956b5a7743e1239b1604f3330616ef9b6a6a05"></a> enumerator ANC\_PATH\_EC\_R

    <a id="_CPPv4NUt1_213ANC_PATH_TF_RE"></a>

    <a id="_CPPv3NUt1_213ANC_PATH_TF_RE"></a> <a id="app__anc_8h_1a99fb83031ce9923c84392b4e92f956b5a9582387f00dad45264522d2fa1abfb34"></a> enumerator ANC\_PATH\_TF\_R

    <a id="_CPPv4NUt1_213ANC_PATH_TE_RE"></a>

    <a id="_CPPv3NUt1_213ANC_PATH_TE_RE"></a> <a id="app__anc_8h_1a99fb83031ce9923c84392b4e92f956b5a9c6d7bd6578d00501faf826c7423faa2"></a> enumerator ANC\_PATH\_TE\_R

    <a id="_CPPv4NUt1_214ANC_PATH_COUNTE"></a>

    <a id="_CPPv3NUt1_214ANC_PATH_COUNTE"></a> <a id="app__anc_8h_1a99fb83031ce9923c84392b4e92f956b5a1bacea68dd4dc8868983806eeaf5b7bb"></a> enumerator ANC\_PATH\_COUNT

<a id="_CPPv4Ut1_3"></a>

<a id="_CPPv3Ut1_3"></a> <a id="app__anc_8h_1abc6126af1d45847bc59afa0aa3216b04"></a> enum \[anonymous\]
:   *Values:*

    <a id="_CPPv4NUt1_319ANC_REOPEN_ON_STARTE"></a>

    <a id="_CPPv3NUt1_319ANC_REOPEN_ON_STARTE"></a> <a id="app__anc_8h_1abc6126af1d45847bc59afa0aa3216b04a32cf0aa67b54b2db62e64254575392ae"></a> enumerator ANC\_REOPEN\_ON\_START

    <a id="_CPPv4NUt1_318ANC_REOPEN_ON_STOPE"></a>

    <a id="_CPPv3NUt1_318ANC_REOPEN_ON_STOPE"></a> <a id="app__anc_8h_1abc6126af1d45847bc59afa0aa3216b04ad875908cae9394cd571edf1044f4a3d6"></a> enumerator ANC\_REOPEN\_ON\_STOP
