---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/common/app_audio/app_hints.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="hints-application-functions"></a>

# HINTS Application Functions

<a id="app-hints-api-brief"></a>

## APP\_HINTS API Brief

| Application | Brief |
| --- | --- |
| [`app_hints_deinit()`](#_CPPv416app_hints_deinitb "app_hints_deinit") | de-initialize hints relevant settings |
| [`app_hints_init()`](#_CPPv414app_hints_init7uint8_t "app_hints_init") | initialize hints relevant settings |
| [`app_play_hints_in_audio_task()`](#_CPPv428app_play_hints_in_audio_task7uint8_tPv "app_play_hints_in_audio_task") | start to play hints procedure |
| [`app_hints_process()`](#_CPPv417app_hints_process20audio_trigger_type_t "app_hints_process") | handle audio data of hints |
| [`app_play_hints_wrap()`](#_CPPv419app_play_hints_wrap7uint8_tb "app_play_hints_wrap") | wrapper function for @app\_play\_hints\_in\_audio\_task |
| [`app_peer_play_hints()`](#_CPPv419app_peer_play_hints7uint8_t12async_path_t8bt_clk_t "app_peer_play_hints") | handle peer play hints cmd for @app\_play\_hints\_in\_audio\_task |

<a id="app-hints-api-reference"></a>

## APP\_HINTS API Reference

<a id="header-file"></a>

### Header File

- [common/app\_audio/app\_hints.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/common/app_audio/app_hints.h)

<a id="functions"></a>

### Functions

<a id="_CPPv416app_hints_deinitb"></a>

<a id="_CPPv316app_hints_deinitb"></a> <a id="_CPPv216app_hints_deinitb"></a> <a id="app_hints_deinit__b"></a> <a id="app__hints_8h_1a8bf9d9d2cad4a900f1faf08fb7b4ef3b"></a> void app\_hints\_deinit(bool execute\_pending)
:   de-initialize hints relevant settings

    reset hints relevant settings. If it has pending event, call @app\_play\_hints\_in\_audio\_task to handle pending event

    返回:
    :   N/A

<a id="_CPPv414app_hints_init7uint8_t"></a>

<a id="_CPPv314app_hints_init7uint8_t"></a> <a id="_CPPv214app_hints_init7uint8_t"></a> <a id="app_hints_init__uint8_t"></a> <a id="app__hints_8h_1a339a2bc350e018f7486fb9ce2f567334"></a> void app\_hints\_init(uint8\_t hint\_id)
:   initialize hints relevant settings

    initialize hints relevant settings and audio environment data

    参数:
    :   **hint\_id** – **\[in\]** index of hints behavior @hint\_idx\_t

    返回:
    :   N/A

<a id="_CPPv428app_play_hints_in_audio_task7uint8_tPv"></a>

<a id="_CPPv328app_play_hints_in_audio_task7uint8_tPv"></a> <a id="_CPPv228app_play_hints_in_audio_task7uint8_tPv"></a> <a id="app_play_hints_in_audio_task__uint8_t.voidP"></a> <a id="app__hints_8h_1a3a89bff2997eb937bb5696cbdeec20ac"></a> uint8\_t app\_play\_hints\_in\_audio\_task(uint8\_t hint\_id, void \*p\_trigger\_clk)
:   start to play hints procedure

    If no other hints is being played, start hints procedure. Otherwise, push it into pending queue

    参数:
    :   - **hint\_id** – **\[in\]** index of hints behavior @hint\_idx\_t
        - **p\_trigger\_clk** – **\[in\]** the clock of hints trigger.

    返回值:
    :   **0** – always 0

    返回:
    :   result

<a id="_CPPv417app_hints_process20audio_trigger_type_t"></a>

<a id="_CPPv317app_hints_process20audio_trigger_type_t"></a> <a id="_CPPv217app_hints_process20audio_trigger_type_t"></a> <a id="app_hints_process__audio_trigger_type_t"></a> <a id="app__hints_8h_1a3992a2d1ee07b41a57dce9be05a1fbfd"></a> void app\_hints\_process([audio\_trigger\_type\_t](app_audio.md#_CPPv420audio_trigger_type_t "audio_trigger_type_t") trigger\_type)
:   handle audio data of hints

    process audio data, and fill data into DAC.

    参数:
    :   **trigger\_type** – **\[in\]** audio trigger type @audio\_trigger\_type\_t

    返回:
    :   N/A

<a id="_CPPv419app_play_hints_wrap7uint8_tb"></a>

<a id="_CPPv319app_play_hints_wrap7uint8_tb"></a> <a id="_CPPv219app_play_hints_wrap7uint8_tb"></a> <a id="app_play_hints_wrap__uint8_t.b"></a> <a id="app__hints_8h_1ae10702afb2e7fda9dbd550c8c5423abb"></a> void app\_play\_hints\_wrap(uint8\_t hint\_id, bool tws\_direct\_play)
:   wrapper function for @app\_play\_hints\_in\_audio\_task

    in TWS mode, only one side need precess play hints procedure

    参数:
    :   - **hint\_id** – **\[in\]** index of hints behavior @hint\_idx\_t
        - **tws\_direct\_play** – **\[in\]** In tws mode, the prompt sound is played directed without distingushing between the left and right earbuds.

    返回:
    :   N/A

<a id="_CPPv419app_peer_play_hints7uint8_t12async_path_t8bt_clk_t"></a>

<a id="_CPPv319app_peer_play_hints7uint8_t12async_path_t8bt_clk_t"></a> <a id="_CPPv219app_peer_play_hints7uint8_t12async_path_t8bt_clk_t"></a> <a id="app_peer_play_hints__uint8_t.async_path_t.bt_clk_t"></a> <a id="app__hints_8h_1a5cf732198a174b0f3b78c2e380012983"></a> uint8\_t app\_peer\_play\_hints(uint8\_t hint\_id, async\_path\_t async\_path, bt\_clk\_t trigger\_time)
:   handle peer play hints cmd for @app\_play\_hints\_in\_audio\_task

    in TWS mode, local handle peer play hints cmd

    参数:
    :   **hint\_id** – **\[in\]** index of hints behavior @hint\_idx\_t

    返回:
    :   N/A

<a id="structures"></a>

### Structures

<a id="_CPPv411hints_hdr_t"></a>

<a id="_CPPv311hints_hdr_t"></a> <a id="_CPPv211hints_hdr_t"></a> <a id="hints_hdr_t"></a> <a id="structhints__hdr__t"></a> struct hints\_hdr\_t
:   hints data header struct definition

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N11hints_hdr_t6lengthE"></a>

    <a id="_CPPv3N11hints_hdr_t6lengthE"></a> <a id="_CPPv2N11hints_hdr_t6lengthE"></a> <a id="hints_hdr_t::length__uint32_t"></a> <a id="structhints__hdr__t_1ab5c152be2dfcc708ec13e4b0e9c8bb02"></a> uint32\_t length
    :   length of hints data

    <a id="_CPPv4N11hints_hdr_t10samplerateE"></a>

    <a id="_CPPv3N11hints_hdr_t10samplerateE"></a> <a id="_CPPv2N11hints_hdr_t10samplerateE"></a> <a id="hints_hdr_t::samplerate__uint32_t"></a> <a id="structhints__hdr__t_1aeb22b6058f41345cc147a1f878150885"></a> uint32\_t samplerate
    :   simpling rate of hints dat

    <a id="_CPPv4N11hints_hdr_t10block_sizeE"></a>

    <a id="_CPPv3N11hints_hdr_t10block_sizeE"></a> <a id="_CPPv2N11hints_hdr_t10block_sizeE"></a> <a id="hints_hdr_t::block_size__uint32_t"></a> <a id="structhints__hdr__t_1a8bd186b03c1a5dd6985e4dc1680af0ba"></a> uint32\_t block\_size
    :   block size of hints data

<a id="_CPPv412hints_info_t"></a>

<a id="_CPPv312hints_info_t"></a> <a id="_CPPv212hints_info_t"></a> <a id="hints_info_t"></a> <a id="structhints__info__t"></a> struct hints\_info\_t
:   hints data information struct definition

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N12hints_info_t9hint_typeE"></a>

    <a id="_CPPv3N12hints_info_t9hint_typeE"></a> <a id="_CPPv2N12hints_info_t9hint_typeE"></a> <a id="hints_info_t::hint_type__hints_type_e"></a> <a id="structhints__info__t_1ac914a9671e62910934c79160a018e4e2"></a> [hints\_type\_e](#_CPPv412hints_type_e "hints_type_e") hint\_type
    :   types of hints codec @hints\_type\_e

    <a id="_CPPv4N12hints_info_t10hints_dataE"></a>

    <a id="_CPPv3N12hints_info_t10hints_dataE"></a> <a id="_CPPv2N12hints_info_t10hints_dataE"></a> <a id="hints_info_t::hints_data__uint8_tA"></a> <a id="structhints__info__t_1abc2aca17c3b294060b8ba73ab95a5a65"></a> uint8\_t hints\_data\[HINTS\_DATA\_PAGE\_LEN\]
    :   data array loading from flash

    <a id="_CPPv4N12hints_info_t9hints_hdrE"></a>

    <a id="_CPPv3N12hints_info_t9hints_hdrE"></a> <a id="_CPPv2N12hints_info_t9hints_hdrE"></a> <a id="hints_info_t::hints_hdr__hints_hdr_t"></a> <a id="structhints__info__t_1a76d29acb5be652f6e178b5f65cae13ad"></a> [hints\_hdr\_t](#_CPPv411hints_hdr_t "hints_hdr_t") hints\_hdr
    :   hints data header @hints\_hdr\_t

    <a id="_CPPv4N12hints_info_t16hints_start_addrE"></a>

    <a id="_CPPv3N12hints_info_t16hints_start_addrE"></a> <a id="_CPPv2N12hints_info_t16hints_start_addrE"></a> <a id="hints_info_t::hints_start_addr__uint32_t"></a> <a id="structhints__info__t_1a153afe05a602c8289a374b3b571d255c"></a> uint32\_t hints\_start\_addr
    :   hints data start address from flash

    <a id="_CPPv4N12hints_info_t14hints_end_addrE"></a>

    <a id="_CPPv3N12hints_info_t14hints_end_addrE"></a> <a id="_CPPv2N12hints_info_t14hints_end_addrE"></a> <a id="hints_info_t::hints_end_addr__uint32_t"></a> <a id="structhints__info__t_1a54facd0b0e56572e3c69ce6c694291e5"></a> uint32\_t hints\_end\_addr
    :   hints data end address from flash

<a id="macros"></a>

### Macros

<a id="c.HINTS_DATA_PAGE_LEN"></a>

<a id="app__hints_8h_1a654d4457ddb9db4d21df69e37162f85a"></a> HINTS\_DATA\_PAGE\_LEN

<a id="c.IS_SINGLE_SIDE_HINT"></a>

<a id="app__hints_8h_1a68fde575513dedf8931491ccd200f0ce"></a> IS\_SINGLE\_SIDE\_HINT(hint\_id)

<a id="c.IS_FORCE_SIDE_HINT"></a>

<a id="app__hints_8h_1a15d40eb56d431c5f9c5c4012412b302b"></a> IS\_FORCE\_SIDE\_HINT(hint\_id)

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv410hint_idx_t"></a>

<a id="_CPPv310hint_idx_t"></a> <a id="_CPPv210hint_idx_t"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44"></a> enum hint\_idx\_t
:   index of hints behavior definition

    *Values:*

    <a id="_CPPv4N10hint_idx_t8POWER_ONE"></a>

    <a id="_CPPv3N10hint_idx_t8POWER_ONE"></a> <a id="_CPPv2N10hint_idx_t8POWER_ONE"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44a96d7f5efa52f2ef85f65ec540233b69d"></a> enumerator POWER\_ON

    <a id="_CPPv4N10hint_idx_t14HINT_CONNECTEDE"></a>

    <a id="_CPPv3N10hint_idx_t14HINT_CONNECTEDE"></a> <a id="_CPPv2N10hint_idx_t14HINT_CONNECTEDE"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44a06ece60448ac4ed5f8ab42d3c41e3df0"></a> enumerator HINT\_CONNECTED

    <a id="_CPPv4N10hint_idx_t17HINT_DISCONNECTEDE"></a>

    <a id="_CPPv3N10hint_idx_t17HINT_DISCONNECTEDE"></a> <a id="_CPPv2N10hint_idx_t17HINT_DISCONNECTEDE"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44ac10c8bf79208d464e1ccbecf3c9f31b3"></a> enumerator HINT\_DISCONNECTED

    <a id="_CPPv4N10hint_idx_t9POWER_OFFE"></a>

    <a id="_CPPv3N10hint_idx_t9POWER_OFFE"></a> <a id="_CPPv2N10hint_idx_t9POWER_OFFE"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44a4a0682c6762857d83fd5d8cb36f9c94e"></a> enumerator POWER\_OFF

    <a id="_CPPv4N10hint_idx_t13ENTER_PAIRINGE"></a>

    <a id="_CPPv3N10hint_idx_t13ENTER_PAIRINGE"></a> <a id="_CPPv2N10hint_idx_t13ENTER_PAIRINGE"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44a54f84de0ab435793320a9940949cfa8d"></a> enumerator ENTER\_PAIRING

    <a id="_CPPv4N10hint_idx_t11LOW_BATTERYE"></a>

    <a id="_CPPv3N10hint_idx_t11LOW_BATTERYE"></a> <a id="_CPPv2N10hint_idx_t11LOW_BATTERYE"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44a86fbcd2781d697097cfa2c24cbf3ffce"></a> enumerator LOW\_BATTERY

    <a id="_CPPv4N10hint_idx_t8HFP_RINGE"></a>

    <a id="_CPPv3N10hint_idx_t8HFP_RINGE"></a> <a id="_CPPv2N10hint_idx_t8HFP_RINGE"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44a8b4425f8f61c20f9ba6352c130a17a09"></a> enumerator HFP\_RING

    <a id="_CPPv4N10hint_idx_t7HFP_ACKE"></a>

    <a id="_CPPv3N10hint_idx_t7HFP_ACKE"></a> <a id="_CPPv2N10hint_idx_t7HFP_ACKE"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44acb24663c67f6c71dc50505a4184ccf5c"></a> enumerator HFP\_ACK

    <a id="_CPPv4N10hint_idx_t9HF_REJECTE"></a>

    <a id="_CPPv3N10hint_idx_t9HF_REJECTE"></a> <a id="_CPPv2N10hint_idx_t9HF_REJECTE"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44a1c4734498586fc10db5ade73ebbe36bb"></a> enumerator HF\_REJECT

    <a id="_CPPv4N10hint_idx_t9HF_CANCELE"></a>

    <a id="_CPPv3N10hint_idx_t9HF_CANCELE"></a> <a id="_CPPv2N10hint_idx_t9HF_CANCELE"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44a2dac8aa7e8dae30d98d4bd4d19a09f6e"></a> enumerator HF\_CANCEL

    <a id="_CPPv4N10hint_idx_t13HF_VOICE_DIALE"></a>

    <a id="_CPPv3N10hint_idx_t13HF_VOICE_DIALE"></a> <a id="_CPPv2N10hint_idx_t13HF_VOICE_DIALE"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44aec399912ed793526ef02bac8ce20c561"></a> enumerator HF\_VOICE\_DIAL

    <a id="_CPPv4N10hint_idx_t8MUTE_MICE"></a>

    <a id="_CPPv3N10hint_idx_t8MUTE_MICE"></a> <a id="_CPPv2N10hint_idx_t8MUTE_MICE"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44a66c0e7b6fb6609b3b6c8f08a3e3036a5"></a> enumerator MUTE\_MIC

    <a id="_CPPv4N10hint_idx_t10UNMUTE_MICE"></a>

    <a id="_CPPv3N10hint_idx_t10UNMUTE_MICE"></a> <a id="_CPPv2N10hint_idx_t10UNMUTE_MICE"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44a8ee92aa2a698b80377a2fd777079236c"></a> enumerator UNMUTE\_MIC

    <a id="_CPPv4N10hint_idx_t7VOL_MAXE"></a>

    <a id="_CPPv3N10hint_idx_t7VOL_MAXE"></a> <a id="_CPPv2N10hint_idx_t7VOL_MAXE"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44a6c373808c1f17d966c31656658bbca5d"></a> enumerator VOL\_MAX

    <a id="_CPPv4N10hint_idx_t7VOL_MINE"></a>

    <a id="_CPPv3N10hint_idx_t7VOL_MINE"></a> <a id="_CPPv2N10hint_idx_t7VOL_MINE"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44abf471612c2e14607367c1a81c931a603"></a> enumerator VOL\_MIN

    <a id="_CPPv4N10hint_idx_t18HF_TRANSFER_TOGGLEE"></a>

    <a id="_CPPv3N10hint_idx_t18HF_TRANSFER_TOGGLEE"></a> <a id="_CPPv2N10hint_idx_t18HF_TRANSFER_TOGGLEE"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44ac997bd5660bbf9942e2dc3eda3a7f550"></a> enumerator HF\_TRANSFER\_TOGGLE

    <a id="_CPPv4N10hint_idx_t9HF_REDIALE"></a>

    <a id="_CPPv3N10hint_idx_t9HF_REDIALE"></a> <a id="_CPPv2N10hint_idx_t9HF_REDIALE"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44a8c3efb453e782fd4efe9256532b9f71a"></a> enumerator HF\_REDIAL

    <a id="_CPPv4N10hint_idx_t10RESERVED_1E"></a>

    <a id="_CPPv3N10hint_idx_t10RESERVED_1E"></a> <a id="_CPPv2N10hint_idx_t10RESERVED_1E"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44af428eaa5b11ce9e4813c0dc3eb105ba0"></a> enumerator RESERVED\_1

    <a id="_CPPv4N10hint_idx_t18HINT_TWS_CONNECTEDE"></a>

    <a id="_CPPv3N10hint_idx_t18HINT_TWS_CONNECTEDE"></a> <a id="_CPPv2N10hint_idx_t18HINT_TWS_CONNECTEDE"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44adcbfc162a3495543266afb25f7fb5b73"></a> enumerator HINT\_TWS\_CONNECTED

    <a id="_CPPv4N10hint_idx_t9HINT_SIRIE"></a>

    <a id="_CPPv3N10hint_idx_t9HINT_SIRIE"></a> <a id="_CPPv2N10hint_idx_t9HINT_SIRIE"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44a77b7228e61ac6617b278333382f39158"></a> enumerator HINT\_SIRI

    <a id="_CPPv4N10hint_idx_t15HINT_PREV_TRACKE"></a>

    <a id="_CPPv3N10hint_idx_t15HINT_PREV_TRACKE"></a> <a id="_CPPv2N10hint_idx_t15HINT_PREV_TRACKE"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44ab623b3a8f062f819a2979504b9744caf"></a> enumerator HINT\_PREV\_TRACK

    <a id="_CPPv4N10hint_idx_t15HINT_NEXT_TRACKE"></a>

    <a id="_CPPv3N10hint_idx_t15HINT_NEXT_TRACKE"></a> <a id="_CPPv2N10hint_idx_t15HINT_NEXT_TRACKE"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44af5d7bbe033c71837787dae59def47a77"></a> enumerator HINT\_NEXT\_TRACK

    <a id="_CPPv4N10hint_idx_t14HINT_VOLUME_UPE"></a>

    <a id="_CPPv3N10hint_idx_t14HINT_VOLUME_UPE"></a> <a id="_CPPv2N10hint_idx_t14HINT_VOLUME_UPE"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44a3e8af92cd5f21a97fbfff537ed98b755"></a> enumerator HINT\_VOLUME\_UP

    <a id="_CPPv4N10hint_idx_t16HINT_VOLUME_DOWNE"></a>

    <a id="_CPPv3N10hint_idx_t16HINT_VOLUME_DOWNE"></a> <a id="_CPPv2N10hint_idx_t16HINT_VOLUME_DOWNE"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44a6bd17603e8fd58b883f1a7888fe51a4a"></a> enumerator HINT\_VOLUME\_DOWN

    <a id="_CPPv4N10hint_idx_t12HINT_HUNG_UPE"></a>

    <a id="_CPPv3N10hint_idx_t12HINT_HUNG_UPE"></a> <a id="_CPPv2N10hint_idx_t12HINT_HUNG_UPE"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44a44db72b4e68932ea88eaff25c5927e08"></a> enumerator HINT\_HUNG\_UP

    <a id="_CPPv4N10hint_idx_t11HINT_ANC_ONE"></a>

    <a id="_CPPv3N10hint_idx_t11HINT_ANC_ONE"></a> <a id="_CPPv2N10hint_idx_t11HINT_ANC_ONE"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44a009974304b073ff8c1bebe5769142c6f"></a> enumerator HINT\_ANC\_ON

    <a id="_CPPv4N10hint_idx_t21HINT_ANC_TRANSPANT_ONE"></a>

    <a id="_CPPv3N10hint_idx_t21HINT_ANC_TRANSPANT_ONE"></a> <a id="_CPPv2N10hint_idx_t21HINT_ANC_TRANSPANT_ONE"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44a18d50533ef89d54a5f2752e082897a7a"></a> enumerator HINT\_ANC\_TRANSPANT\_ON

    <a id="_CPPv4N10hint_idx_t12HINT_ANC_OFFE"></a>

    <a id="_CPPv3N10hint_idx_t12HINT_ANC_OFFE"></a> <a id="_CPPv2N10hint_idx_t12HINT_ANC_OFFE"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44a2fa7b00634a6739058e692ef2ce0d33f"></a> enumerator HINT\_ANC\_OFF

    <a id="_CPPv4N10hint_idx_t10RESERVED_2E"></a>

    <a id="_CPPv3N10hint_idx_t10RESERVED_2E"></a> <a id="_CPPv2N10hint_idx_t10RESERVED_2E"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44a59fb8f70e42afe0296673ee6e932ea0b"></a> enumerator RESERVED\_2

    <a id="_CPPv4N10hint_idx_t10RESERVED_3E"></a>

    <a id="_CPPv3N10hint_idx_t10RESERVED_3E"></a> <a id="_CPPv2N10hint_idx_t10RESERVED_3E"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44ab9cd831dfcb1f699d7eaee2c189a327c"></a> enumerator RESERVED\_3

    <a id="_CPPv4N10hint_idx_t10RESERVED_4E"></a>

    <a id="_CPPv3N10hint_idx_t10RESERVED_4E"></a> <a id="_CPPv2N10hint_idx_t10RESERVED_4E"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44a0b01276727338370e9935f8d40136557"></a> enumerator RESERVED\_4

    <a id="_CPPv4N10hint_idx_t10RESERVED_5E"></a>

    <a id="_CPPv3N10hint_idx_t10RESERVED_5E"></a> <a id="_CPPv2N10hint_idx_t10RESERVED_5E"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44a8ce97bdb21a680d9b201670f22c5b660"></a> enumerator RESERVED\_5

    <a id="_CPPv4N10hint_idx_t10RESERVED_6E"></a>

    <a id="_CPPv3N10hint_idx_t10RESERVED_6E"></a> <a id="_CPPv2N10hint_idx_t10RESERVED_6E"></a> <a id="app__hints_8h_1aac6fa777c296cd4da0a7d6b06e059e44a9b582c1e7ecef65ce80aca883453117b"></a> enumerator RESERVED\_6

<a id="_CPPv412hints_type_e"></a>

<a id="_CPPv312hints_type_e"></a> <a id="_CPPv212hints_type_e"></a> <a id="app__hints_8h_1a3fac91c4cb2333d17b08c7e394a33c14"></a> enum hints\_type\_e
:   types of hints codec definition

    *Values:*

    <a id="_CPPv4N12hints_type_e9INTER_WAVE"></a>

    <a id="_CPPv3N12hints_type_e9INTER_WAVE"></a> <a id="_CPPv2N12hints_type_e9INTER_WAVE"></a> <a id="app__hints_8h_1a3fac91c4cb2333d17b08c7e394a33c14a2a1bffb602b6b9d8dc12abeb8a592a10"></a> enumerator INTER\_WAV

    <a id="_CPPv4N12hints_type_e9INTER_SBCE"></a>

    <a id="_CPPv3N12hints_type_e9INTER_SBCE"></a> <a id="_CPPv2N12hints_type_e9INTER_SBCE"></a> <a id="app__hints_8h_1a3fac91c4cb2333d17b08c7e394a33c14a3e2a10cc80c3d46accc00b1404261c05"></a> enumerator INTER\_SBC

    <a id="_CPPv4N12hints_type_e9INTER_MP3E"></a>

    <a id="_CPPv3N12hints_type_e9INTER_MP3E"></a> <a id="_CPPv2N12hints_type_e9INTER_MP3E"></a> <a id="app__hints_8h_1a3fac91c4cb2333d17b08c7e394a33c14a28f7c4f95becc441e975a7a192afdb14"></a> enumerator INTER\_MP3

    <a id="_CPPv4N12hints_type_e7EXT_WAVE"></a>

    <a id="_CPPv3N12hints_type_e7EXT_WAVE"></a> <a id="_CPPv2N12hints_type_e7EXT_WAVE"></a> <a id="app__hints_8h_1a3fac91c4cb2333d17b08c7e394a33c14a8f99a5c6c2b78ff77ca63b269af44f7b"></a> enumerator EXT\_WAV

    <a id="_CPPv4N12hints_type_e7EXT_SBCE"></a>

    <a id="_CPPv3N12hints_type_e7EXT_SBCE"></a> <a id="_CPPv2N12hints_type_e7EXT_SBCE"></a> <a id="app__hints_8h_1a3fac91c4cb2333d17b08c7e394a33c14aa0dc4f77f104aee2dac92a4b2463d86c"></a> enumerator EXT\_SBC
