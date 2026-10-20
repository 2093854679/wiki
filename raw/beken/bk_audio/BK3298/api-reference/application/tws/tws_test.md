---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/tws/tws_test.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="tws-test-functions"></a>

# TWS Test Functions

<a id="tws-test-api-brief"></a>

## TWS\_TEST API Brief

| Application | Brief |
| --- | --- |
| [`tws_test()`](#_CPPv48tws_test7uint8_t "tws_test") | Send test message to TWS task |
| [`tws_test_handle()`](#_CPPv415tws_test_handleP7uint8_t "tws_test_handle") | Handle test messages in TWS task |

<a id="tws-test-api-reference"></a>

## TWS\_TEST API Reference

<a id="header-file"></a>

### Header File

- [tws/tws\_ux/inc/tws\_test.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/tws/tws_ux/inc/tws_test.h)

<a id="functions"></a>

### Functions

<a id="_CPPv48tws_test7uint8_t"></a>

<a id="_CPPv38tws_test7uint8_t"></a> <a id="_CPPv28tws_test7uint8_t"></a> <a id="tws_test__uint8_t"></a> <a id="tws__test_8h_1ac45aea5a3d828ad1a014780e191a4920"></a> void tws\_test(uint8\_t code)
:   Send test message to TWS task.

    Send the test message of code id \[code\] to the TWS task for testing.

    参数:
    :   **code** – **\[in\]** test code id

    返回:
    :   N/A

<a id="_CPPv415tws_test_handleP7uint8_t"></a>

<a id="_CPPv315tws_test_handleP7uint8_t"></a> <a id="_CPPv215tws_test_handleP7uint8_t"></a> <a id="tws_test_handle__uint8_tP"></a> <a id="tws__test_8h_1a1203848595feaed4f542c5fdba053282"></a> void tws\_test\_handle(uint8\_t \*p\_msg)
:   Handle test messages in TWS task.

    Handle the test messages \[p\_msg\] in TWS task.

    参数:
    :   **p\_msg** – **\[in\]** pointer to test message

    返回:
    :   N/A **TWS\_TEST\_H** EOF

<a id="structures"></a>

### Structures

<a id="_CPPv414tws_test_msg_t"></a>

<a id="_CPPv314tws_test_msg_t"></a> <a id="_CPPv214tws_test_msg_t"></a> <a id="tws_test_msg_t"></a> <a id="structtws__test__msg__t"></a> struct tws\_test\_msg\_t
:   TWS test message structure definition.
