---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/common/app_ble/app_mcp_ce.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="media-control-client-application-handle-functions"></a>

# Media Control Client Application Handle Functions

<a id="app-mcp-ce-api-brief"></a>

## APP\_MCP\_CE API Brief

| Application | Brief |
| --- | --- |
| [`app_mcp_ce_init()`](#_CPPv415app_mcp_ce_initv "app_mcp_ce_init") | Initialize BLE Media Control Profile (MCP) |
| [`app_mcp_ce_media_state_is_playing()`](#_CPPv433app_mcp_ce_media_state_is_playingv "app_mcp_ce_media_state_is_playing") | BLE Media Control state is playing |
| [`app_mcp_ce_media_state_is_seeking()`](#_CPPv433app_mcp_ce_media_state_is_seekingv "app_mcp_ce_media_state_is_seeking") | BLE Media Control state is seeking |
| [`app_mcp_is_mcp_active()`](#_CPPv421app_mcp_is_mcp_activev "app_mcp_is_mcp_active") | BLE Media Control Profile (MCP) is active |
| [`app_mcp_audio_media_control()`](#_CPPv427app_mcp_audio_media_control7uint8_t "app_mcp_audio_media_control") | Perform BLE media control operation |

<a id="app-mcp-ce-api-reference"></a>

## APP\_MCP\_CE API Reference

<a id="header-file"></a>

### Header File

- [common/app\_ble/app\_mcp\_ce.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/common/app_ble/app_mcp_ce.h)

<a id="functions"></a>

### Functions

<a id="_CPPv415app_mcp_ce_initv"></a>

<a id="_CPPv315app_mcp_ce_initv"></a> <a id="_CPPv215app_mcp_ce_initv"></a> <a id="app_mcp_ce_init__void"></a> <a id="app__mcp__ce_8h_1a914f6487820fcd007071f05f1eebd8b2"></a> void app\_mcp\_ce\_init(void)
:   Initialize BLE Media Control Profile (MCP).

    Initialize and mount the BLE Media Control Profile (MCP).

    返回:
    :   N/A

<a id="_CPPv433app_mcp_ce_media_state_is_playingv"></a>

<a id="_CPPv333app_mcp_ce_media_state_is_playingv"></a> <a id="_CPPv233app_mcp_ce_media_state_is_playingv"></a> <a id="app_mcp_ce_media_state_is_playing__void"></a> <a id="app__mcp__ce_8h_1a374ac4f3a58a668efb56633d2e1e52e0"></a> uint8\_t app\_mcp\_ce\_media\_state\_is\_playing(void)
:   BLE Media Control state is playing.

    Verify if the BLE Media Control state is playing.

    返回值:
    :   - **true** – playing
        - **false** – not playing

    返回:
    :   playing status

<a id="_CPPv433app_mcp_ce_media_state_is_seekingv"></a>

<a id="_CPPv333app_mcp_ce_media_state_is_seekingv"></a> <a id="_CPPv233app_mcp_ce_media_state_is_seekingv"></a> <a id="app_mcp_ce_media_state_is_seeking__void"></a> <a id="app__mcp__ce_8h_1acada35571f0dd926bd1c2888968ae7fe"></a> uint8\_t app\_mcp\_ce\_media\_state\_is\_seeking(void)
:   BLE Media Control state is seeking.

    Verify if the BLE Media Control state is seeking.

    返回值:
    :   - **true** – seeking
        - **false** – not seeking

    返回:
    :   seeking status

<a id="_CPPv421app_mcp_is_mcp_activev"></a>

<a id="_CPPv321app_mcp_is_mcp_activev"></a> <a id="_CPPv221app_mcp_is_mcp_activev"></a> <a id="app_mcp_is_mcp_active__void"></a> <a id="app__mcp__ce_8h_1ac3e350fc248f79eb828bf9714df452e6"></a> uint8\_t app\_mcp\_is\_mcp\_active(void)
:   BLE Media Control Profile (MCP) is active.

    Verify if the BLE Media Control Profile is active.

    返回值:
    :   - **true** – active
        - **false** – inactive

    返回:
    :   active status

<a id="_CPPv427app_mcp_audio_media_control7uint8_t"></a>

<a id="_CPPv327app_mcp_audio_media_control7uint8_t"></a> <a id="_CPPv227app_mcp_audio_media_control7uint8_t"></a> <a id="app_mcp_audio_media_control__uint8_t"></a> <a id="app__mcp__ce_8h_1a960a53de6f4bc4b236fa3e51421176c0"></a> [btif\_ret\_t](../../../btif/btif_type.md#_CPPv410btif_ret_t "btif_ret_t") app\_mcp\_audio\_media\_control(uint8\_t opcode)
:   Perform BLE media control operation.

    Manage mobile phone media behavior.

    参数:
    :   **opcode** – **\[in\]** Media Control Opcode 0x01 play 0x02 pause 0x03 fast rewind 0x04 fast forward 0x05 stop 0x30 previous track 0x31 next track

    返回值:
    :   - **0** – success
        - **other** – fail

    返回:
    :   result
