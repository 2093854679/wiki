# EFUSE[](#efuse "永久链接至标题")

[[English]](../../../../en/v1.5/api-reference/peripheral/bk_efuse.html "../../../../en/v1.5/api-reference/peripheral/bk_efuse.html")


## EFUSE API Status[](#efuse-api-status "永久链接至标题")

| API | BK7235A | BK7235B | BK7235 |
| --- | --- | --- | --- |
| [`bk_efuse_driver_init()`](#_CPPv420bk_efuse_driver_initv "bk_efuse_driver_init") | Y | Y | Y |
| [`bk_efuse_driver_deinit()`](#_CPPv422bk_efuse_driver_deinitv "bk_efuse_driver_deinit") | Y | Y | Y |
| `bk_efuse_write()` | Y | Y | Y |
| `bk_efuse_read()` | Y | Y | Y |


## Efuse API Reference[](#efuse-api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [efuse.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/efuse.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/efuse.h")


### Functions[](#functions "永久链接至标题")

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_efuse_driver_init(void)[](#_CPPv420bk_efuse_driver_initv "永久链接至目标")
:   Init the EFUSE driver.

    This API init the resoure common:


    - Init EFUSE driver control memory


    **Attention**
    :   1. This API should be called before any other EFUSE APIs.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_efuse_driver_deinit(void)[](#_CPPv422bk_efuse_driver_deinitv "永久链接至目标")
:   Deinit the EFUSE driver.

    This API free all resource related to EFUSE and disable EFUSE.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_efuse_write_byte(uint8_t addr, uint8_t data)[](#_CPPv419bk_efuse_write_byte7uint8_t7uint8_t "永久链接至目标")
:   Efuse write operation.

    参数
    :   - **addr** – efuse write address

        - **data** – efuse write data

    返回
    :   - BK_OK: succeed

        - BK_ERR_EFUSE_DRIVER_NOT_INIT: EFUSE driver not init

        - BK_ERR_EFUSE_ADDR_OUT_OF_RANGE: EFUSE address is out of range

        - BK_ERR_EFUSE_CANNOT_WRTIE: EFUSE cannot write, cannot change bit from 1 to 0

        - BK_ERR_EFUSE_WRTIE_NOT_EQUAL: EFUSE data read is not equal to the data written

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_efuse_read_byte(uint8_t addr, uint8_t *data)[](#_CPPv418bk_efuse_read_byte7uint8_tP7uint8_t "永久链接至目标")
:   Efuse read operation.

    参数
    :   - **addr** – read address

        - **data** – pointer to accept value of efuse read data

    返回
    :   - BK_OK: succeed

        - BK_ERR_EFUSE_DRIVER_NOT_INIT: EFUSE driver not init

        - BK_ERR_EFUSE_ADDR_OUT_OF_RANGE: EFUSE address is out of range

        - others: other errors.


## Efuse API Typedefs[](#efuse-api-typedefs "永久链接至标题")


### Header File[](#id1 "永久链接至标题")


- [efuse_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/efuse_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/efuse_types.h")


### Header File[](#id2 "永久链接至标题")


- [hal/hal_efuse_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/hal/hal_efuse_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/hal/hal_efuse_types.h")


### Macros[](#macros "永久链接至标题")

BK_ERR_EFUSE_DRIVER_NOT_INIT[](#c.BK_ERR_EFUSE_DRIVER_NOT_INIT "永久链接至目标")
:   EFUSE driver not init

BK_ERR_EFUSE_ADDR_OUT_OF_RANGE[](#c.BK_ERR_EFUSE_ADDR_OUT_OF_RANGE "永久链接至目标")
:   EFUSE address is out of range

BK_ERR_EFUSE_CANNOT_WRTIE[](#c.BK_ERR_EFUSE_CANNOT_WRTIE "永久链接至目标")
:   EFUSE cannot write, cannot change bit from 1 to 0

BK_ERR_EFUSE_WRTIE_NOT_EQUAL[](#c.BK_ERR_EFUSE_WRTIE_NOT_EQUAL "永久链接至目标")
:   EFUSE data read is not equal to the data written

BK_ERR_EFUSE_READ_FAIL[](#c.BK_ERR_EFUSE_READ_FAIL "永久链接至目标")
:   EFUSE data read fail


### Type Definitions[](#type-definitions "永久链接至标题")

typedef uint8_t efuse_unit_t[](#_CPPv412efuse_unit_t "永久链接至目标")
:   efuse uint id
