---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/common/app_ota/app_ota_diff.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="over-the-air-diff-application-functions"></a>

# Over-the-air Diff Application Functions

<a id="app-ota-diff-api-brief"></a>

## APP\_OTA\_DIFF API Brief

| Application | Brief |
| --- | --- |
| [`app_apply_ota_diff_patch()`](#_CPPv424app_apply_ota_diff_patchP11buff_info_tP11buff_info_tP11buff_info_tb "app_apply_ota_diff_patch") | generate OTA patch bin |
| [`app_ota_diff_test()`](#_CPPv417app_ota_diff_testv "app_ota_diff_test") | generate OTA diff bin file |

<a id="app-ota-diff-api-reference"></a>

## APP\_OTA\_DIFF API Reference

<a id="header-file"></a>

### Header File

- [common/app\_ota/app\_ota\_diff.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/common/app_ota/app_ota_diff.h)

<a id="functions"></a>

### Functions

<a id="_CPPv416app_gen_ota_diffP11buff_info_tP11buff_info_tP11buff_info_tb"></a>

<a id="_CPPv316app_gen_ota_diffP11buff_info_tP11buff_info_tP11buff_info_tb"></a> <a id="_CPPv216app_gen_ota_diffP11buff_info_tP11buff_info_tP11buff_info_tb"></a> <a id="app_gen_ota_diff__buff_info_tP.buff_info_tP.buff_info_tP.b"></a> <a id="app__ota__diff_8h_1a10266c6f1bbae56bd4cd677dd4e3f794"></a> uint8\_t app\_gen\_ota\_diff([buff\_info\_t](#_CPPv411buff_info_t "buff_info_t") \*p\_old\_info, [buff\_info\_t](#_CPPv411buff_info_t "buff_info_t") \*p\_new\_info, [buff\_info\_t](#_CPPv411buff_info_t "buff_info_t") \*p\_diff\_info, bool compress)
:   generate OTA diff data

    generate diff data between old OTA bin and new OTA bin

    参数:
    :   - **p\_old\_info** – **\[in\]** pointer to the old OTA bin buffer data
        - **p\_new\_info** – **\[in\]** pointer to the new OTA bin buffer data
        - **p\_diff\_info** – **\[out\]** pointer to the diff data buffer data
        - **compress** – **\[in\]** execute compress or not

    返回值:
    :   **0** – always return 0

    返回:
    :   result

<a id="_CPPv424app_apply_ota_diff_patchP11buff_info_tP11buff_info_tP11buff_info_tb"></a>

<a id="_CPPv324app_apply_ota_diff_patchP11buff_info_tP11buff_info_tP11buff_info_tb"></a> <a id="_CPPv224app_apply_ota_diff_patchP11buff_info_tP11buff_info_tP11buff_info_tb"></a> <a id="app_apply_ota_diff_patch__buff_info_tP.buff_info_tP.buff_info_tP.b"></a> <a id="app__ota__diff_8h_1a4e8a622fae7cdb10285e972171bae837"></a> uint8\_t app\_apply\_ota\_diff\_patch([buff\_info\_t](#_CPPv411buff_info_t "buff_info_t") \*p\_old\_info, [buff\_info\_t](#_CPPv411buff_info_t "buff_info_t") \*p\_diff\_info, [buff\_info\_t](#_CPPv411buff_info_t "buff_info_t") \*p\_new\_info, bool decompress)
:   generate OTA patch bin

    genereate OTA patch bin from the OTA old bin and diff data

    参数:
    :   - **p\_old\_info** – **\[in\]** pointer to the old OTA bin buffer data
        - **p\_diff\_info** – **\[in\]** pointer to the diff buffer data
        - **p\_new\_info** – **\[out\]** pointer to the new OTA bin buffer data
        - **decompress** – **\[in\]** execute decompress or not cc

    返回值:
    :   **0** – always return 0

    返回:
    :   result

<a id="_CPPv417app_ota_diff_testv"></a>

<a id="_CPPv317app_ota_diff_testv"></a> <a id="_CPPv217app_ota_diff_testv"></a> <a id="app_ota_diff_test__void"></a> <a id="app__ota__diff_8h_1a482899c311aeb4e052e3653d882a9b45"></a> void app\_ota\_diff\_test(void)
:   generate OTA diff bin file

    use bsdiff to generate OTA bin file

    返回:
    :   N/A

<a id="structures"></a>

### Structures

<a id="_CPPv411buff_info_t"></a>

<a id="_CPPv311buff_info_t"></a> <a id="_CPPv211buff_info_t"></a> <a id="buff_info_t"></a> <a id="structbuff__info__t"></a> struct buff\_info\_t
:   OTA bin data struct definition.
