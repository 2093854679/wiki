---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/common/app_component/app_dlp.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="dlp-application-functions"></a>

# DLP Application Functions

<a id="app-dlp-api-brief"></a>

## APP\_DLP API Brief

| Application | Brief |
| --- | --- |
| [`app_dlp_init()`](#_CPPv412app_dlp_initv "app_dlp_init") | initialise DLP application |
| [`app_dlp_deinit()`](#_CPPv414app_dlp_deinitv "app_dlp_deinit") | deinit DLP application |

<a id="app-charger-api-reference"></a>

## APP\_CHARGER API Reference

<a id="header-file"></a>

### Header File

- [common/app\_component/app\_dlp.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/common/app_component/app_dlp.h)

<a id="functions"></a>

### Functions

<a id="_CPPv412app_dlp_initv"></a>

<a id="_CPPv312app_dlp_initv"></a> <a id="_CPPv212app_dlp_initv"></a> <a id="app_dlp_init__void"></a> <a id="app__dlp_8h_1aefcd69b07999c850bcae5ad21e9e1257"></a> int32\_t app\_dlp\_init(void)
:   initialise DLP application.

    initialise DLP, open and start waiting data

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv414app_dlp_deinitv"></a>

<a id="_CPPv314app_dlp_deinitv"></a> <a id="_CPPv214app_dlp_deinitv"></a> <a id="app_dlp_deinit__void"></a> <a id="app__dlp_8h_1a0c7622e378b760b1dc2cdccb5974c5e5"></a> int32\_t app\_dlp\_deinit(void)
:   deinit DLP application.

    deinitialize DLP, stop waiting and close it

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result
