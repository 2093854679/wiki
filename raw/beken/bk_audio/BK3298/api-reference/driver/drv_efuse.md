---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/driver/drv_efuse.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="drv-efuse"></a>

# DRV\_EFUSE

<a id="drv-efuse-api-status"></a>

## DRV\_EFUSE API Status

| API |
| --- |
| [`drv_efuse_init()`](#_CPPv414drv_efuse_initv "drv_efuse_init") |
| [`drv_efuse_deinit()`](#_CPPv416drv_efuse_deinitv "drv_efuse_deinit") |
| [`drv_efuse_write_byte()`](#_CPPv420drv_efuse_write_byte7uint8_t7uint8_t "drv_efuse_write_byte") |
| [`drv_efuse_read_byte()`](#_CPPv419drv_efuse_read_byte7uint8_tP7uint8_t "drv_efuse_read_byte") |

<a id="drv-efuse-api-reference"></a>

## DRV\_EFUSE API Reference

<a id="header-file"></a>

### Header File

- [driver/efuse/drv\_efuse.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/driver/efuse/drv_efuse.h)

<a id="functions"></a>

### Functions

<a id="_CPPv414drv_efuse_initv"></a>

<a id="_CPPv314drv_efuse_initv"></a> <a id="_CPPv214drv_efuse_initv"></a> <a id="drv_efuse_init__void"></a> <a id="drv__efuse_8h_1aa421a439f488bd9231e7141a2dc10e7f"></a> int32\_t drv\_efuse\_init(void)
:   Init the EFUSE driver.

    This API init the resoure common:

    - Init EFUSE driver control memory

      This API should be called before any other EFUSE APIs.

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv416drv_efuse_deinitv"></a>

<a id="_CPPv316drv_efuse_deinitv"></a> <a id="_CPPv216drv_efuse_deinitv"></a> <a id="drv_efuse_deinit__void"></a> <a id="drv__efuse_8h_1a74375dc3efd2858a7cfba6ebf08808a6"></a> int32\_t drv\_efuse\_deinit(void)
:   Deinit the EFUSE driver.

    This API free all resource related to EFUSE and disable EFUSE.

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv420drv_efuse_write_byte7uint8_t7uint8_t"></a>

<a id="_CPPv320drv_efuse_write_byte7uint8_t7uint8_t"></a> <a id="_CPPv220drv_efuse_write_byte7uint8_t7uint8_t"></a> <a id="drv_efuse_write_byte__uint8_t.uint8_t"></a> <a id="drv__efuse_8h_1a59633cb5cdea32c74f480f6e828e63ff"></a> int32\_t drv\_efuse\_write\_byte(uint8\_t addr, uint8\_t data)
:   Efuse write operation.

    参数:
    :   - **addr** – **\[in\]** efuse write addres
        - **data** – **\[in\]** efuse write data

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv419drv_efuse_read_byte7uint8_tP7uint8_t"></a>

<a id="_CPPv319drv_efuse_read_byte7uint8_tP7uint8_t"></a> <a id="_CPPv219drv_efuse_read_byte7uint8_tP7uint8_t"></a> <a id="drv_efuse_read_byte__uint8_t.uint8_tP"></a> <a id="drv__efuse_8h_1a89820f3a0d4fd4c2ba0c870704031bcf"></a> int32\_t drv\_efuse\_read\_byte(uint8\_t addr, uint8\_t \*data)
:   Efuse read operation.

    参数:
    :   - **addr** – **\[in\]** read address
        - **data** – **\[out\]** pointer to accept value of efuse read data

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result
