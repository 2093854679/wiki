---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7235/zh_CN/v1.5/api-reference/peripheral/bk_efuse.html
sdk_family: bk_idk
chip: BK7235
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="efuse"></a>

# EFUSE

<a id="efuse-api-status"></a>

## EFUSE API Status

| API | BK7235A | BK7235B | BK7235 |
| --- | --- | --- | --- |
| [`bk_efuse_driver_init()`](#_CPPv420bk_efuse_driver_initv "bk_efuse_driver_init") | Y | Y | Y |
| [`bk_efuse_driver_deinit()`](#_CPPv422bk_efuse_driver_deinitv "bk_efuse_driver_deinit") | Y | Y | Y |
| `bk_efuse_write()` | Y | Y | Y |
| `bk_efuse_read()` | Y | Y | Y |

<a id="efuse-api-reference"></a>

## Efuse API Reference

<a id="header-file"></a>

### Header File

- [efuse.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/efuse.h)

<a id="functions"></a>

### Functions

<a id="_CPPv420bk_efuse_driver_initv"></a>

<a id="_CPPv320bk_efuse_driver_initv"></a> <a id="_CPPv220bk_efuse_driver_initv"></a> <a id="bk_efuse_driver_init__void"></a> <a id="group__bk__api__efuse_1gaca4213e74a531c83a14ec2290a8a29d5"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_efuse\_driver\_init(void)
:   Init the EFUSE driver.

    This API init the resoure common:

    - Init EFUSE driver control memory

    **Attention**
    :   1\. This API should be called before any other EFUSE APIs.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv422bk_efuse_driver_deinitv"></a>

<a id="_CPPv322bk_efuse_driver_deinitv"></a> <a id="_CPPv222bk_efuse_driver_deinitv"></a> <a id="bk_efuse_driver_deinit__void"></a> <a id="group__bk__api__efuse_1gae5d373abe937e574ca3ae5ee17538ccd"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_efuse\_driver\_deinit(void)
:   Deinit the EFUSE driver.

    This API free all resource related to EFUSE and disable EFUSE.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv419bk_efuse_write_byte7uint8_t7uint8_t"></a>

<a id="_CPPv319bk_efuse_write_byte7uint8_t7uint8_t"></a> <a id="_CPPv219bk_efuse_write_byte7uint8_t7uint8_t"></a> <a id="bk_efuse_write_byte__uint8_t.uint8_t"></a> <a id="group__bk__api__efuse_1gad3755868c50c91559d775b6f49879183"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_efuse\_write\_byte(uint8\_t addr, uint8\_t data)
:   Efuse write operation.

    参数
    :   - **addr** – efuse write address
        - **data** – efuse write data

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_EFUSE\_DRIVER\_NOT\_INIT: EFUSE driver not init
        - BK\_ERR\_EFUSE\_ADDR\_OUT\_OF\_RANGE: EFUSE address is out of range
        - BK\_ERR\_EFUSE\_CANNOT\_WRTIE: EFUSE cannot write, cannot change bit from 1 to 0
        - BK\_ERR\_EFUSE\_WRTIE\_NOT\_EQUAL: EFUSE data read is not equal to the data written
        - others: other errors.

<a id="_CPPv418bk_efuse_read_byte7uint8_tP7uint8_t"></a>

<a id="_CPPv318bk_efuse_read_byte7uint8_tP7uint8_t"></a> <a id="_CPPv218bk_efuse_read_byte7uint8_tP7uint8_t"></a> <a id="bk_efuse_read_byte__uint8_t.uint8_tP"></a> <a id="group__bk__api__efuse_1ga1d4dfa52478e2cdedc3ae5f9a467c0d3"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_efuse\_read\_byte(uint8\_t addr, uint8\_t \*data)
:   Efuse read operation.

    参数
    :   - **addr** – read address
        - **data** – pointer to accept value of efuse read data

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_EFUSE\_DRIVER\_NOT\_INIT: EFUSE driver not init
        - BK\_ERR\_EFUSE\_ADDR\_OUT\_OF\_RANGE: EFUSE address is out of range
        - others: other errors.

<a id="efuse-api-typedefs"></a>

## Efuse API Typedefs

<a id="id1"></a>

### Header File

- [efuse\_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/efuse_types.h)

<a id="id2"></a>

### Header File

- [hal/hal\_efuse\_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/hal/hal_efuse_types.h)

<a id="macros"></a>

### Macros

<a id="c.BK_ERR_EFUSE_DRIVER_NOT_INIT"></a>

<a id="group__bk__api__efuse__defs_1ga76f876fae3d7a12a8eca49ba84faa85c"></a> BK\_ERR\_EFUSE\_DRIVER\_NOT\_INIT
:   EFUSE driver not init

<a id="c.BK_ERR_EFUSE_ADDR_OUT_OF_RANGE"></a>

<a id="group__bk__api__efuse__defs_1ga9e5dbc9c4de3ddeec48409259aa09d67"></a> BK\_ERR\_EFUSE\_ADDR\_OUT\_OF\_RANGE
:   EFUSE address is out of range

<a id="c.BK_ERR_EFUSE_CANNOT_WRTIE"></a>

<a id="group__bk__api__efuse__defs_1ga7a3950f4bb11971ca1a7a0fc7d2becf1"></a> BK\_ERR\_EFUSE\_CANNOT\_WRTIE
:   EFUSE cannot write, cannot change bit from 1 to 0

<a id="c.BK_ERR_EFUSE_WRTIE_NOT_EQUAL"></a>

<a id="group__bk__api__efuse__defs_1gaede874f0c778d95a182b935756d59108"></a> BK\_ERR\_EFUSE\_WRTIE\_NOT\_EQUAL
:   EFUSE data read is not equal to the data written

<a id="c.BK_ERR_EFUSE_READ_FAIL"></a>

<a id="group__bk__api__efuse__defs_1gabdeda2eeb6c85149121c1898567d1730"></a> BK\_ERR\_EFUSE\_READ\_FAIL
:   EFUSE data read fail

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv412efuse_unit_t"></a>

<a id="_CPPv312efuse_unit_t"></a> <a id="_CPPv212efuse_unit_t"></a> <a id="efuse_unit_t"></a> <a id="group__bk__api__efuse__defs_1ga2cd5c530432bebdc339e0d9446002563"></a> typedef uint8\_t efuse\_unit\_t
:   efuse uint id
