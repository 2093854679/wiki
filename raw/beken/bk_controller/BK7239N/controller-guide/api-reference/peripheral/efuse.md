---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/controller-guide/api-reference/peripheral/efuse.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="efuse-api"></a>

# efuse API

efuse (Electrically Fusable) 电熔丝API接口。

<a id="header-file"></a>

## Header File

- [efuse.h](https://github.com/bekencorp/armino/blob/main/components/efuse.h)

<a id="functions"></a>

## Functions

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
:   Efuse write operation @Notice: Each efuse address area has specific usage, please apply the area from PM before write data to the efuse address.

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
