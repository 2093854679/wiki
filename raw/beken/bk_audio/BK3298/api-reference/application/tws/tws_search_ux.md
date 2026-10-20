---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/tws/tws_search_ux.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="tws-search-ux-functions"></a>

# TWS Search UX Functions

<a id="tws-search-ux-api-brief"></a>

## TWS\_SEARCH\_UX API Brief

| Application | Brief |
| --- | --- |
| [`tws_search_connect_start()`](#_CPPv424tws_search_connect_startv "tws_search_connect_start") | Start searching for and connecting TWS earbud |
| [`tws_search_init()`](#_CPPv415tws_search_initv "tws_search_init") | Initialize search |
| [`tws_search_is_running()`](#_CPPv421tws_search_is_runningv "tws_search_is_running") | Check that the TWS earbud search is running |

<a id="tws-search-ux-api-reference"></a>

## TWS\_SEARCH\_UX API Reference

<a id="header-file"></a>

### Header File

- [tws/tws\_ux/inc/tws\_search\_ux.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/tws/tws_ux/inc/tws_search_ux.h)

<a id="functions"></a>

### Functions

<a id="_CPPv424tws_search_connect_startv"></a>

<a id="_CPPv324tws_search_connect_startv"></a> <a id="_CPPv224tws_search_connect_startv"></a> <a id="tws_search_connect_start__void"></a> <a id="tws__search__ux_8h_1a98863db4e5b75f81183e0bf7de9250e3"></a> void tws\_search\_connect\_start(void)
:   Start searching for and connecting TWS earbud.

    Start searching for and connecting another paired TWS earbud.

    返回:
    :   N/A

<a id="_CPPv415tws_search_initv"></a>

<a id="_CPPv315tws_search_initv"></a> <a id="_CPPv215tws_search_initv"></a> <a id="tws_search_init__void"></a> <a id="tws__search__ux_8h_1a183533f4eef3323c2c858c32c2bc40ed"></a> void tws\_search\_init(void)
:   Initialize search.

    Register a search handler for HCI events

    返回:
    :   N/A

<a id="_CPPv421tws_search_is_runningv"></a>

<a id="_CPPv321tws_search_is_runningv"></a> <a id="_CPPv221tws_search_is_runningv"></a> <a id="tws_search_is_running__void"></a> <a id="tws__search__ux_8h_1a26af3ba902ce982c0fc9fc1bd7cc3985"></a> bool tws\_search\_is\_running(void)
:   Check that the TWS earbud search is running.

    Check that the another paired TWS earbud search is running

    返回值:
    :   - **true** – running
        - **false** – not runing **TWS\_SEARCH\_UX\_H** EOF

    返回:
    :   result
