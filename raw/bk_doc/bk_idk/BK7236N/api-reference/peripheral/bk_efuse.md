# EFUSE[](#efuse "永久链接至标题")


## EFUSE API Status[](#efuse-api-status "永久链接至标题")

| API | BK7236N |
| --- | --- |
| [`bk_efuse_driver_init()`](#_CPPv420bk_efuse_driver_initv "bk_efuse_driver_init") | Y |
| [`bk_efuse_driver_deinit()`](#_CPPv422bk_efuse_driver_deinitv "bk_efuse_driver_deinit") | Y |
| `bk_efuse_write()` | Y |
| `bk_efuse_read()` | Y |


## Efuse API Reference[](#efuse-api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [efuse.h](https://github.com/bekencorp/armino/blob/main/components/efuse.h "https://github.com/bekencorp/armino/blob/main/components/efuse.h")


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
:   Efuse write operation @Notice: Each efuse address area has specific usage, please apply the area from PM before write data to the efuse address.

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


- [efuse_types.h](https://github.com/bekencorp/armino/blob/main/components/efuse_types.h "https://github.com/bekencorp/armino/blob/main/components/efuse_types.h")


### Header File[](#id2 "永久链接至标题")


- [hal/hal_efuse_types.h](https://github.com/bekencorp/armino/blob/main/components/hal/hal_efuse_types.h "https://github.com/bekencorp/armino/blob/main/components/hal/hal_efuse_types.h")


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

EFUSE_ADDR_BYTE0[](#c.EFUSE_ADDR_BYTE0 "永久链接至目标")
:   efuse address defines @Notice: Each efuse address area has specific usage, please apply the area from PM before write data to the efuse address.

EFUSE_ADDR_BYTE1[](#c.EFUSE_ADDR_BYTE1 "永久链接至目标")

EFUSE_ADDR_BYTE2[](#c.EFUSE_ADDR_BYTE2 "永久链接至目标")

EFUSE_ADDR_BYTE3[](#c.EFUSE_ADDR_BYTE3 "永久链接至目标")

EFUSE_ADDR_BYTE4[](#c.EFUSE_ADDR_BYTE4 "永久链接至目标")

EFUSE_ADDR_BYTE5[](#c.EFUSE_ADDR_BYTE5 "永久链接至目标")

EFUSE_ADDR_BYTE6[](#c.EFUSE_ADDR_BYTE6 "永久链接至目标")

EFUSE_ADDR_BYTE7[](#c.EFUSE_ADDR_BYTE7 "永久链接至目标")

EFUSE_ADDR_BYTE8[](#c.EFUSE_ADDR_BYTE8 "永久链接至目标")

EFUSE_ADDR_BYTE9[](#c.EFUSE_ADDR_BYTE9 "永久链接至目标")

EFUSE_ADDR_BYTE10[](#c.EFUSE_ADDR_BYTE10 "永久链接至目标")

EFUSE_ADDR_BYTE11[](#c.EFUSE_ADDR_BYTE11 "永久链接至目标")

EFUSE_ADDR_BYTE12[](#c.EFUSE_ADDR_BYTE12 "永久链接至目标")

EFUSE_ADDR_BYTE13[](#c.EFUSE_ADDR_BYTE13 "永久链接至目标")

EFUSE_ADDR_BYTE14[](#c.EFUSE_ADDR_BYTE14 "永久链接至目标")

EFUSE_ADDR_BYTE15[](#c.EFUSE_ADDR_BYTE15 "永久链接至目标")

EFUSE_ADDR_BYTE16[](#c.EFUSE_ADDR_BYTE16 "永久链接至目标")

EFUSE_ADDR_BYTE17[](#c.EFUSE_ADDR_BYTE17 "永久链接至目标")

EFUSE_ADDR_BYTE18[](#c.EFUSE_ADDR_BYTE18 "永久链接至目标")

EFUSE_ADDR_BYTE19[](#c.EFUSE_ADDR_BYTE19 "永久链接至目标")

EFUSE_ADDR_BYTE20[](#c.EFUSE_ADDR_BYTE20 "永久链接至目标")

EFUSE_ADDR_BYTE21[](#c.EFUSE_ADDR_BYTE21 "永久链接至目标")

EFUSE_ADDR_BYTE22[](#c.EFUSE_ADDR_BYTE22 "永久链接至目标")

EFUSE_ADDR_BYTE23[](#c.EFUSE_ADDR_BYTE23 "永久链接至目标")

EFUSE_ADDR_BYTE24[](#c.EFUSE_ADDR_BYTE24 "永久链接至目标")

EFUSE_ADDR_BYTE25[](#c.EFUSE_ADDR_BYTE25 "永久链接至目标")

EFUSE_ADDR_BYTE26[](#c.EFUSE_ADDR_BYTE26 "永久链接至目标")

EFUSE_ADDR_BYTE27[](#c.EFUSE_ADDR_BYTE27 "永久链接至目标")

EFUSE_ADDR_BYTE28[](#c.EFUSE_ADDR_BYTE28 "永久链接至目标")

EFUSE_ADDR_BYTE29[](#c.EFUSE_ADDR_BYTE29 "永久链接至目标")

EFUSE_ADDR_BYTE30[](#c.EFUSE_ADDR_BYTE30 "永久链接至目标")

EFUSE_ADDR_BYTE31[](#c.EFUSE_ADDR_BYTE31 "永久链接至目标")

EFUSE_DEVICE_ID_BYTE_NUM[](#c.EFUSE_DEVICE_ID_BYTE_NUM "永久链接至目标")
:   efuse device id defines the device id stores in efuse address byte 0x18 ~ 0x1c the efuse device id is set via ate cmds

EFUSE_DEVICE_ID_SN_MINIMUM[](#c.EFUSE_DEVICE_ID_SN_MINIMUM "永久链接至目标")

EFUSE_DEVICE_ID_SN_MAXIMUM[](#c.EFUSE_DEVICE_ID_SN_MAXIMUM "永久链接至目标")

EFUSE_WAFER_ID_MINIMUM[](#c.EFUSE_WAFER_ID_MINIMUM "永久链接至目标")

EFUSE_WAFER_ID_MAXIMUM[](#c.EFUSE_WAFER_ID_MAXIMUM "永久链接至目标")


### Type Definitions[](#type-definitions "永久链接至标题")

typedef uint8_t efuse_unit_t[](#_CPPv412efuse_unit_t "永久链接至目标")
:   efuse uint id
