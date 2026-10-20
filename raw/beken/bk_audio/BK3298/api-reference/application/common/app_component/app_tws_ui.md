---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/common/app_component/app_tws_ui.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="tws-user-interface-application-functions"></a>

# TWS User Interface Application Functions

<a id="app-tws-ui-api-brief"></a>

## APP\_TWS\_UI API Brief

| Application | Brief |
| --- | --- |
| [`app_tws_inout_box_manage_init()`](#_CPPv429app_tws_inout_box_manage_initv "app_tws_inout_box_manage_init") | initial detection which whether has been took out of box |

<a id="app-tws-ui-api-reference"></a>

## APP\_TWS\_UI API Reference

<a id="header-file"></a>

### Header File

- [common/app\_component/app\_tws\_ui.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/common/app_component/app_tws_ui.h)

<a id="functions"></a>

### Functions

<a id="_CPPv429app_tws_inout_box_manage_initv"></a>

<a id="_CPPv329app_tws_inout_box_manage_initv"></a> <a id="_CPPv229app_tws_inout_box_manage_initv"></a> <a id="app_tws_inout_box_manage_init__void"></a> <a id="app__tws__ui_8h_1ae59ca12bc2b6548db99ecd4af09e4029"></a> int32\_t app\_tws\_inout\_box\_manage\_init(void)
:   initial detection which whether has been took out of box

    register a callback to pmu module and check vusb to decide whether is out of box status or not

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result
