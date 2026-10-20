---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/common/app_component/app_charger.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="charger-application-functions"></a>

# Charger Application Functions

<a id="app-charger-api-brief"></a>

## APP\_CHARGER API Brief

| Application | Brief |
| --- | --- |
| [`app_charger_init()`](#_CPPv416app_charger_initv "app_charger_init") | initialise charger application |
| [`app_charger_deinit()`](#_CPPv418app_charger_deinitv "app_charger_deinit") | deinit charger application. |
| [`app_charger_get_state_tick()`](#_CPPv426app_charger_get_state_tickv "app_charger_get_state_tick") | get current state tick |

<a id="app-charger-api-reference"></a>

## APP\_CHARGER API Reference

<a id="header-file"></a>

### Header File

- [common/app\_component/app\_charger.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/common/app_component/app_charger.h)

<a id="functions"></a>

### Functions

<a id="_CPPv416app_charger_initv"></a>

<a id="_CPPv316app_charger_initv"></a> <a id="_CPPv216app_charger_initv"></a> <a id="app_charger_init__void"></a> <a id="app__charger_8h_1a68d4b392d4f6a35110ac51a541d8ac54"></a> int32\_t app\_charger\_init(void)
:   initialise charger application.

    The behavior of charging after the user calls it is continued to be controlled by it according to , without calling other api operations

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv418app_charger_deinitv"></a>

<a id="_CPPv318app_charger_deinitv"></a> <a id="_CPPv218app_charger_deinitv"></a> <a id="app_charger_deinit__void"></a> <a id="app__charger_8h_1af08c2984f1b233265190d6ce45dc03fa"></a> int32\_t app\_charger\_deinit(void)
:   deinit charger application.

    include unregister charger callback and disable charger

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv426app_charger_get_state_tickv"></a>

<a id="_CPPv326app_charger_get_state_tickv"></a> <a id="_CPPv226app_charger_get_state_tickv"></a> <a id="app_charger_get_state_tick__void"></a> <a id="app__charger_8h_1a698606599b9ef19b070d9b666cf7baa1"></a> uint32\_t app\_charger\_get\_state\_tick(void)
:   get current state tick.

    返回:
    :   state tick

<a id="_CPPv430app_charger_get_charger_statusv"></a>

<a id="_CPPv330app_charger_get_charger_statusv"></a> <a id="_CPPv230app_charger_get_charger_statusv"></a> <a id="app_charger_get_charger_status__void"></a> <a id="app__charger_8h_1af42d43b0a86d03c989b34de71e8a7a5c"></a> bool app\_charger\_get\_charger\_status(void)
:   get current charger status.

    返回值:
    :   - **0** – no charger
        - **1** – chargering

    返回:
    :   charger’status
