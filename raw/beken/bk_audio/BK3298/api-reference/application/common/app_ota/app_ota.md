---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/common/app_ota/app_ota.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="over-the-air-application-functions"></a>

# Over-the-air Application Functions

<a id="app-ota-api-brief"></a>

## APP\_OTA API Brief

| Application | Brief |
| --- | --- |
| [`app_ota_init()`](#_CPPv412app_ota_initv "app_ota_init") | OTA service initialization |
| [`app_ota_notify_slave_result_handle()`](#_CPPv434app_ota_notify_slave_result_handlePK7uint8_t8uint16_t "app_ota_notify_slave_result_handle") | master handle slave OTA result |
| [`app_ota_is_running()`](#_CPPv418app_ota_is_runningv "app_ota_is_running") | check OTA service status |

<a id="app-ota-api-reference"></a>

## APP\_OTA API Reference

<a id="header-file"></a>

### Header File

- [common/app\_ota/app\_ota.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/common/app_ota/app_ota.h)

<a id="functions"></a>

### Functions

<a id="_CPPv412app_ota_initv"></a>

<a id="_CPPv312app_ota_initv"></a> <a id="_CPPv212app_ota_initv"></a> <a id="app_ota_init__void"></a> <a id="app__ota_8h_1a90b56f7f40fd7082942b3ce23558ff56"></a> void app\_ota\_init(void)
:   OTA service initialization.

    initile OTA relatived setting and hook up bluetooth service

    返回:
    :   N/A

<a id="_CPPv434app_ota_notify_slave_result_handlePK7uint8_t8uint16_t"></a>

<a id="_CPPv334app_ota_notify_slave_result_handlePK7uint8_t8uint16_t"></a> <a id="_CPPv234app_ota_notify_slave_result_handlePK7uint8_t8uint16_t"></a> <a id="app_ota_notify_slave_result_handle__uint8_tCP.uint16_t"></a> <a id="app__ota_8h_1ad2f6e43e11c7c73f7b1fd4797f561b0b"></a> void app\_ota\_notify\_slave\_result\_handle(const uint8\_t \*p\_data, uint16\_t length)
:   master handle slave OTA result

    master handle OTA result send from slave, used to confirm the upgrade process and result

    参数:
    :   - **p\_data** – **\[in\]** [ota\_notify\_result\_t](#structota__notify__result__t) data send from slave
        - **length** – **\[in\]** data length

    返回:
    :   N/A

<a id="_CPPv418app_ota_is_runningv"></a>

<a id="_CPPv318app_ota_is_runningv"></a> <a id="_CPPv218app_ota_is_runningv"></a> <a id="app_ota_is_running__void"></a> <a id="app__ota_8h_1a0c3174158e5096f638b72c2370fce6b1"></a> bool app\_ota\_is\_running(void)
:   check OTA service status

    check OTA service connect or disconnet

    返回值:
    :   - **TRUE** – connect
        - **FALSE** – disconnet

    返回:
    :   result

<a id="structures"></a>

### Structures

<a id="_CPPv419ota_notify_result_t"></a>

<a id="_CPPv319ota_notify_result_t"></a> <a id="_CPPv219ota_notify_result_t"></a> <a id="ota_notify_result_t"></a> <a id="structota__notify__result__t"></a> struct ota\_notify\_result\_t
:   slave OTA notify result struct definition

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N19ota_notify_result_t8cmd_codeE"></a>

    <a id="_CPPv3N19ota_notify_result_t8cmd_codeE"></a> <a id="_CPPv2N19ota_notify_result_t8cmd_codeE"></a> <a id="ota_notify_result_t::cmd_code__uint16_t"></a> <a id="structota__notify__result__t_1a530bf610c2ca632b742c4f478fb7daea"></a> uint16\_t cmd\_code
    :   slave OTA notfiy result cmd index

    <a id="_CPPv4N19ota_notify_result_t9ready_seqE"></a>

    <a id="_CPPv3N19ota_notify_result_t9ready_seqE"></a> <a id="_CPPv2N19ota_notify_result_t9ready_seqE"></a> <a id="ota_notify_result_t::ready_seq__uint8_t"></a> <a id="structota__notify__result__t_1a21f94374087b336b92e47f4fa57f37d3"></a> uint8\_t ready\_seq
    :   slave OTA write flash index

    <a id="_CPPv4N19ota_notify_result_t4typeE"></a>

    <a id="_CPPv3N19ota_notify_result_t4typeE"></a> <a id="_CPPv2N19ota_notify_result_t4typeE"></a> <a id="ota_notify_result_t::type__uint8_t"></a> <a id="structota__notify__result__t_1aee69296e41b7835d827c9b73df725e8e"></a> uint8\_t type
    :   slave OTA notify type, 0:OTA\_TYPE\_CHECKSUM 1:OTA\_TYPE\_FINAL\_RESULT

    <a id="_CPPv4N19ota_notify_result_t6resultE"></a>

    <a id="_CPPv3N19ota_notify_result_t6resultE"></a> <a id="_CPPv2N19ota_notify_result_t6resultE"></a> <a id="ota_notify_result_t::result__uint8_t"></a> <a id="structota__notify__result__t_1ac5f03fb04388f7ad1ccabd74b0492ece"></a> uint8\_t result
    :   slave OTA notify result

<a id="macros"></a>

### Macros

<a id="c.OTA_TYPE_CHECKSUM"></a>

<a id="app__ota_8h_1a03aeb148d686b2ab496f66844d01b915"></a> OTA\_TYPE\_CHECKSUM
:   slave OTA notify for notify master checksum

<a id="c.OTA_TYPE_FINAL_RESULT"></a>

<a id="app__ota_8h_1a977186aea35875b7fe9ca7205296f4bb"></a> OTA\_TYPE\_FINAL\_RESULT
:   slave OTA notify for notify master final result
