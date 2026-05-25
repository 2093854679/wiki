# I2C[](#i2c "永久链接至标题")

[[English]](../../../../en/v1.5/api-reference/peripheral/bk_i2c.html "../../../../en/v1.5/api-reference/peripheral/bk_i2c.html")


## I2C API Status[](#i2c-api-status "永久链接至标题")

| API | BK7256 | BK7256_cp1 |
| --- | --- | --- |
| [`bk_i2c_driver_init()`](#_CPPv418bk_i2c_driver_initv "bk_i2c_driver_init") | Y | Y |
| [`bk_i2c_driver_deinit()`](#_CPPv420bk_i2c_driver_deinitv "bk_i2c_driver_deinit") | Y | Y |
| [`bk_i2c_init()`](#_CPPv411bk_i2c_init8i2c_id_tPK12i2c_config_t "bk_i2c_init") | Y | Y |
| [`bk_i2c_deinit()`](#_CPPv413bk_i2c_deinit8i2c_id_t "bk_i2c_deinit") | Y | Y |
| [`bk_i2c_master_write()`](#_CPPv419bk_i2c_master_write8i2c_id_t8uint32_tPK7uint8_t8uint32_t8uint32_t "bk_i2c_master_write") | Y | Y |
| [`bk_i2c_master_read()`](#_CPPv418bk_i2c_master_read8i2c_id_t8uint32_tP7uint8_t8uint32_t8uint32_t "bk_i2c_master_read") | Y | Y |
| [`bk_i2c_slave_write()`](#_CPPv418bk_i2c_slave_write8i2c_id_tPK7uint8_t8uint32_t8uint32_t "bk_i2c_slave_write") | Y | Y |
| [`bk_i2c_slave_read()`](#_CPPv417bk_i2c_slave_read8i2c_id_tP7uint8_t8uint32_t8uint32_t "bk_i2c_slave_read") | Y | Y |
| [`bk_i2c_memory_write()`](#_CPPv419bk_i2c_memory_write8i2c_id_tPK15i2c_mem_param_t "bk_i2c_memory_write") | Y | Y |
| [`bk_i2c_memory_read()`](#_CPPv418bk_i2c_memory_read8i2c_id_tPK15i2c_mem_param_t "bk_i2c_memory_read") | Y | Y |


## I2C UNIT Number[](#i2c-unit-number "永久链接至标题")

| Capability | BK7256 | BK7256_cp1 |
| --- | --- | --- |
| UNIT Number | 3 | 3 |


## I2C Pin and GPIO Map[](#i2c-pin-and-gpio-map "永久链接至标题")

| SPI Pin | BK7256 | BK7256_cp1 |
| --- | --- | --- |
| I2C0 SCL | 20 | 20 |
| I2C0 SDA | 21 | 21 |
| I2C1 SCL | 42 | 42 |
| I2C1 SDA | 43 | 43 |
| I2C2 SCL | 0 | 0 |
| I2C2 SDA | 1 | 1 |


## I2C API Reference[](#i2c-api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [i2c.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/i2c.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/i2c.h")


### Functions[](#functions "永久链接至标题")

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_i2c_driver_init(void)[](#_CPPv418bk_i2c_driver_initv "永久链接至目标")
:   Init the I2C driver.

    This API init the resoure common:


    - Init I2C driver control memory


    **Attention**
    :   1. This API should be called before any other I2C APIs.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_i2c_driver_deinit(void)[](#_CPPv420bk_i2c_driver_deinitv "永久链接至目标")
:   Deinit the I2C driver.

    This API free all resource related to I2C and disable I2C.

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_i2c_init([i2c_id_t](#_CPPv48i2c_id_t "i2c_id_t") id, const [i2c_config_t](#_CPPv412i2c_config_t "i2c_config_t") *cfg)[](#_CPPv411bk_i2c_init8i2c_id_tPK12i2c_config_t "永久链接至目标")
:   Init the I2C id.

    This API init the I2C id:


    - Power up the I2C id

    - Configure the I2C id clock

    - Map the I2C id to dedicated GPIO port

    - Set the I2C parameters

    - Start the I2C id


    **Attention**
    :   Multifunction GPIO initialization affects other functions

    参数
    :   - **id** – I2C id

        - **config** – I2C parameter settings

    返回
    :   - BK_OK: succeed

        - BK_ERR_NULL_PARAM: I2C config paramter is NULL

        - BK_ERR_I2C_NOT_INIT: I2C driver not init

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_i2c_deinit([i2c_id_t](#_CPPv48i2c_id_t "i2c_id_t") id)[](#_CPPv413bk_i2c_deinit8i2c_id_t "永久链接至目标")
:   Deinit the I2C id.

    This API deinit the I2C id:


    - Stop the I2C id

    - Disable the I2C id interrupt

    - Power down the I2C id

    参数
    :   **id** – I2C id

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_i2c_master_write([i2c_id_t](#_CPPv48i2c_id_t "i2c_id_t") id, uint32_t dev_addr, const uint8_t *data, uint32_t size, uint32_t timeout_ms)[](#_CPPv419bk_i2c_master_write8i2c_id_t8uint32_tPK7uint8_t8uint32_t8uint32_t "永久链接至目标")
:   Write data to the I2C port from a given buffer and length, It shall only be called in I2C master mode.

    参数
    :   - **id** – I2C id

        - **dev_addr** – slave device address

        - **data** – pointer to the buffer

        - **size** – data length to write

        - **timeout_ms** – timeout ms

    返回
    :   - BK_OK: succeed

        - BK_ERR_I2C_NOT_INIT: I2C driver not init

        - BK_ERR_I2C_INVALID_ID: I2C id number is invalid

        - BK_ERR_I2C_ID_NOT_INIT: I2C id not init

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_i2c_master_read([i2c_id_t](#_CPPv48i2c_id_t "i2c_id_t") id, uint32_t dev_addr, uint8_t *data, uint32_t size, uint32_t timeout_ms)[](#_CPPv418bk_i2c_master_read8i2c_id_t8uint32_tP7uint8_t8uint32_t8uint32_t "永久链接至目标")
:   I2C read data from I2C buffer, It shall only be called in I2C master mode.

    参数
    :   - **id** – I2C id

        - **dev_addr** – slave device address

        - **data** – pointer to the buffer

        - **size** – data length to read

        - **timeout_ms** – timeout ms

    返回
    :   - BK_OK: succeed

        - BK_ERR_I2C_NOT_INIT: I2C driver not init

        - BK_ERR_I2C_INVALID_ID: I2C id number is invalid

        - BK_ERR_I2C_ID_NOT_INIT: I2C id not init

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_i2c_slave_write([i2c_id_t](#_CPPv48i2c_id_t "i2c_id_t") id, const uint8_t *data, uint32_t size, uint32_t timeout_ms)[](#_CPPv418bk_i2c_slave_write8i2c_id_tPK7uint8_t8uint32_t8uint32_t "永久链接至目标")
:   Write data to the I2C port from a given buffer and length, It shall only be called in I2C slave mode.

    参数
    :   - **id** – I2C id

        - **data** – pointer to the buffer

        - **size** – data length to write

        - **timeout_ms** – timeout ms

    返回
    :   - BK_OK: succeed

        - BK_ERR_I2C_NOT_INIT: I2C driver not init

        - BK_ERR_I2C_INVALID_ID: I2C id number is invalid

        - BK_ERR_I2C_ID_NOT_INIT: I2C id not init

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_i2c_slave_read([i2c_id_t](#_CPPv48i2c_id_t "i2c_id_t") id, uint8_t *data, uint32_t size, uint32_t timeout_ms)[](#_CPPv417bk_i2c_slave_read8i2c_id_tP7uint8_t8uint32_t8uint32_t "永久链接至目标")
:   I2C read data from I2C buffer, It shall only be called in I2C slave mode.

    参数
    :   - **id** – I2C id

        - **dev_addr** – slave device address

        - **data** – pointer to the buffer

        - **size** – data length to read

        - **timeout_ms** – timeout ms

    返回
    :   - BK_OK: succeed

        - BK_ERR_I2C_NOT_INIT: I2C driver not init

        - BK_ERR_I2C_INVALID_ID: I2C id number is invalid

        - BK_ERR_I2C_ID_NOT_INIT: I2C id not init

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_i2c_memory_write([i2c_id_t](#_CPPv48i2c_id_t "i2c_id_t") id, const [i2c_mem_param_t](#_CPPv415i2c_mem_param_t "i2c_mem_param_t") *mem_param)[](#_CPPv419bk_i2c_memory_write8i2c_id_tPK15i2c_mem_param_t "永久链接至目标")
:   Write data to the specific memory address from a given buffer and length, It shall only be called in I2C master mode.

    参数
    :   - **id** – I2C id

        - **mem_param** – memory parameter

    返回
    :   - BK_OK: succeed

        - BK_ERR_NULL_PARAM: I2C mem_param is NULL

        - BK_ERR_I2C_NOT_INIT: I2C driver not init

        - BK_ERR_I2C_INVALID_ID: I2C id number is invalid

        - BK_ERR_I2C_ID_NOT_INIT: I2C id not init

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_i2c_memory_read([i2c_id_t](#_CPPv48i2c_id_t "i2c_id_t") id, const [i2c_mem_param_t](#_CPPv415i2c_mem_param_t "i2c_mem_param_t") *mem_param)[](#_CPPv418bk_i2c_memory_read8i2c_id_tPK15i2c_mem_param_t "永久链接至目标")
:   I2C read data from I2C specific memory address, It shall only be called in I2C master mode.

    参数
    :   - **id** – I2C id

        - **mem_param** – memory parameter

    返回
    :   - BK_OK: succeed

        - BK_ERR_NULL_PARAM: I2C mem_param is NULL

        - BK_ERR_I2C_NOT_INIT: I2C driver not init

        - BK_ERR_I2C_INVALID_ID: I2C id number is invalid

        - BK_ERR_I2C_ID_NOT_INIT: I2C id not init

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_i2c_set_baud_rate([i2c_id_t](#_CPPv48i2c_id_t "i2c_id_t") id, uint32_t baud_rate)[](#_CPPv420bk_i2c_set_baud_rate8i2c_id_t8uint32_t "永久链接至目标")
:   I2C set baud rate.

    参数
    :   - **id** – I2C id

        - **baud_rate** – baud rate

    返回
    :   - BK_OK: succeed

        - BK_ERR_I2C_NOT_INIT: I2C driver not init

        - BK_ERR_I2C_INVALID_ID: I2C id number is invalid

        - BK_ERR_I2C_ID_NOT_INIT: I2C id not init

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_i2c_set_slave_address([i2c_id_t](#_CPPv48i2c_id_t "i2c_id_t") id, uint16_t slave_addr)[](#_CPPv424bk_i2c_set_slave_address8i2c_id_t8uint16_t "永久链接至目标")
:   Set slave address when current role is i2c slave.

    参数
    :   - **id** – I2C id

        - **slave_addr** – slave address

    返回
    :   - BK_OK: succeed

        - BK_ERR_I2C_NOT_INIT: I2C driver not init

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_i2c_enable_interrupt([i2c_id_t](#_CPPv48i2c_id_t "i2c_id_t") id)[](#_CPPv423bk_i2c_enable_interrupt8i2c_id_t "永久链接至目标")
:   Enable I2C interrupt.

    参数
    :   **id** – I2C id

    返回
    :   - BK_OK: succeed

        - others: other errors.

[bk_err_t](../system/os.html#_CPPv48bk_err_t "bk_err_t") bk_i2c_disable_interrupt([i2c_id_t](#_CPPv48i2c_id_t "i2c_id_t") id)[](#_CPPv424bk_i2c_disable_interrupt8i2c_id_t "永久链接至目标")
:   Disable I2C interrupt.

    参数
    :   **id** – I2C id

    返回
    :   - BK_OK: succeed

        - others: other errors.

bool bk_i2c_is_bus_busy([i2c_id_t](#_CPPv48i2c_id_t "i2c_id_t") id)[](#_CPPv418bk_i2c_is_bus_busy8i2c_id_t "永久链接至目标")
:   Check if I2C is busy.

    参数
    :   **id** – I2C id

    返回
    :   true: busy, false: not busy

uint32_t bk_i2c_get_cur_action([i2c_id_t](#_CPPv48i2c_id_t "i2c_id_t") id)[](#_CPPv421bk_i2c_get_cur_action8i2c_id_t "永久链接至目标")
:   Get i2c current action, such as start,stop,send write_addr.

    参数
    :   **id** – I2C id

    返回
    :   i2c action

void bk_i2c_timer_callback(int id, void *myTimer)[](#_CPPv421bk_i2c_timer_callbackiPv "永久链接至目标")
:   bk_i2c_timer_callback

    This API set timer call back

    返回

uint8_t bk_i2c_get_busstate(int id)[](#_CPPv419bk_i2c_get_busstatei "永久链接至目标")
:   bk_i2c_get_busstate

    This API get bus status idle or busy

    返回
    :   - 1: idle

        - 0: busy.

uint8_t bk_i2c_get_transstate(int id)[](#_CPPv421bk_i2c_get_transstatei "永久链接至目标")
:   bk_i2c_get_transstate

    This API get bus status idle or busy

    返回
    :   - 1: ok

        - 0: fail.


## I2C API Typedefs[](#i2c-api-typedefs "永久链接至标题")


### Header File[](#id1 "永久链接至标题")


- [i2c_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/i2c_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/i2c_types.h")


### Structures[](#structures "永久链接至标题")

struct i2c_mem_param_t[](#_CPPv415i2c_mem_param_t "永久链接至目标")
:   Public Members

    uint32_t dev_addr[](#_CPPv4N15i2c_mem_param_t8dev_addrE "永久链接至目标")
    :   I2C slave device address

    uint32_t mem_addr[](#_CPPv4N15i2c_mem_param_t8mem_addrE "永久链接至目标")
    :   I2C slave device memerory address

    [i2c_mem_addr_size_t](#_CPPv419i2c_mem_addr_size_t "i2c_mem_addr_size_t") mem_addr_size[](#_CPPv4N15i2c_mem_param_t13mem_addr_sizeE "永久链接至目标")
    :   I2C slave device memerory address size

    uint8_t *data[](#_CPPv4N15i2c_mem_param_t4dataE "永久链接至目标")
    :   I2C data pointer

    uint32_t data_size[](#_CPPv4N15i2c_mem_param_t9data_sizeE "永久链接至目标")
    :   I2C data size

    uint32_t timeout_ms[](#_CPPv4N15i2c_mem_param_t10timeout_msE "永久链接至目标")
    :   I2C timeout ms


### Macros[](#macros "永久链接至标题")

BK_ERR_I2C_NOT_INIT[](#c.BK_ERR_I2C_NOT_INIT "永久链接至目标")
:   I2C driver not init

BK_ERR_I2C_ID_NOT_INIT[](#c.BK_ERR_I2C_ID_NOT_INIT "永久链接至目标")
:   I2C id not init

BK_ERR_I2C_SM_BUS_BUSY[](#c.BK_ERR_I2C_SM_BUS_BUSY "永久链接至目标")
:   I2C bus busy

BK_ERR_I2C_ACK_TIMEOUT[](#c.BK_ERR_I2C_ACK_TIMEOUT "永久链接至目标")
:   I2C receive ack timeout

BK_ERR_I2C_CHECK_DEFCONFIG[](#c.BK_ERR_I2C_CHECK_DEFCONFIG "永久链接至目标")
:   I2C please check defconfig

BK_ERR_I2C_SCL_TIMEOUT[](#c.BK_ERR_I2C_SCL_TIMEOUT "永久链接至目标")
:   I2C SCL timeout


### Type Definitions[](#type-definitions "永久链接至标题")

typedef void (*i2c_isr_t)([i2c_id_t](#_CPPv48i2c_id_t "i2c_id_t") id, void *param)[](#_CPPv49i2c_isr_t "永久链接至目标")
:   i2c interrupt service routine


### Enumerations[](#enumerations "永久链接至标题")

enum i2c_work_mode_t[](#_CPPv415i2c_work_mode_t "永久链接至目标")
:   *Values:*

    enumerator I2C_MASTER_WRITE[](#_CPPv4N15i2c_work_mode_t16I2C_MASTER_WRITEE "永久链接至目标")
    :   I2C master write

    enumerator I2C_MASTER_READ[](#_CPPv4N15i2c_work_mode_t15I2C_MASTER_READE "永久链接至目标")
    :   I2C master read

    enumerator I2C_SLAVE_WRITE[](#_CPPv4N15i2c_work_mode_t15I2C_SLAVE_WRITEE "永久链接至目标")
    :   I2C slave write

    enumerator I2C_SLAVE_READ[](#_CPPv4N15i2c_work_mode_t14I2C_SLAVE_READE "永久链接至目标")
    :   I2C slave read


### Header File[](#id2 "永久链接至标题")


- [hal/hal_i2c_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/hal/hal_i2c_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/hal/hal_i2c_types.h")


### Structures[](#id3 "永久链接至标题")

struct i2c_config_t[](#_CPPv412i2c_config_t "永久链接至目标")
:   Public Members

    uint32_t baud_rate[](#_CPPv4N12i2c_config_t9baud_rateE "永久链接至目标")
    :   i2c clock rate

    [i2c_addr_mode_t](#_CPPv415i2c_addr_mode_t "i2c_addr_mode_t") addr_mode[](#_CPPv4N12i2c_config_t9addr_modeE "永久链接至目标")
    :   i2c address mode

    uint16_t slave_addr[](#_CPPv4N12i2c_config_t10slave_addrE "永久链接至目标")
    :   i2c address for slave mode


### Macros[](#id4 "永久链接至标题")

I2C_BAUD_RATE_50KHZ[](#c.I2C_BAUD_RATE_50KHZ "永久链接至目标")

I2C_BAUD_RATE_100KHZ[](#c.I2C_BAUD_RATE_100KHZ "永久链接至目标")

I2C_BAUD_RATE_200KHZ[](#c.I2C_BAUD_RATE_200KHZ "永久链接至目标")

I2C_BAUD_RATE_400KHZ[](#c.I2C_BAUD_RATE_400KHZ "永久链接至目标")

I2C_DEFAULT_BAUD_RATE[](#c.I2C_DEFAULT_BAUD_RATE "永久链接至目标")


### Type Definitions[](#id5 "永久链接至标题")

typedef uint8_t i2c_unit_t[](#_CPPv410i2c_unit_t "永久链接至目标")
:   i2c uint id


### Enumerations[](#id6 "永久链接至标题")

enum i2c_id_t[](#_CPPv48i2c_id_t "永久链接至目标")
:   *Values:*

    enumerator I2C_ID_0[](#_CPPv4N8i2c_id_t8I2C_ID_0E "永久链接至目标")
    :   i2c id 0

    enumerator I2C_ID_MAX[](#_CPPv4N8i2c_id_t10I2C_ID_MAXE "永久链接至目标")
    :   i2c id max

enum i2c_addr_mode_t[](#_CPPv415i2c_addr_mode_t "永久链接至目标")
:   *Values:*

    enumerator I2C_ADDR_MODE_7BIT[](#_CPPv4N15i2c_addr_mode_t18I2C_ADDR_MODE_7BITE "永久链接至目标")
    :   i2c address mode 7bit

    enumerator I2C_ADDR_MODE_10BIT[](#_CPPv4N15i2c_addr_mode_t19I2C_ADDR_MODE_10BITE "永久链接至目标")
    :   i2c address mode 10bit

enum i2c_fifo_int_level_t[](#_CPPv420i2c_fifo_int_level_t "永久链接至目标")
:   *Values:*

    enumerator I2C_FIFO_INT_LEVEL_1[](#_CPPv4N20i2c_fifo_int_level_t20I2C_FIFO_INT_LEVEL_1E "永久链接至目标")
    :   i2c fifo int level 1

    enumerator I2C_FIFO_INT_LEVEL_4[](#_CPPv4N20i2c_fifo_int_level_t20I2C_FIFO_INT_LEVEL_4E "永久链接至目标")
    :   i2c fifo int level 4

    enumerator I2C_FIFO_INT_LEVEL_8[](#_CPPv4N20i2c_fifo_int_level_t20I2C_FIFO_INT_LEVEL_8E "永久链接至目标")
    :   i2c fifo int level 8

    enumerator I2C_FIFO_INT_LEVEL_12[](#_CPPv4N20i2c_fifo_int_level_t21I2C_FIFO_INT_LEVEL_12E "永久链接至目标")
    :   i2c fifo int level 12

enum i2c_mem_addr_size_t[](#_CPPv419i2c_mem_addr_size_t "永久链接至目标")
:   *Values:*

    enumerator I2C_MEM_ADDR_SIZE_8BIT[](#_CPPv4N19i2c_mem_addr_size_t22I2C_MEM_ADDR_SIZE_8BITE "永久链接至目标")
    :   i2c memory address size 8bit

    enumerator I2C_MEM_ADDR_SIZE_16BIT[](#_CPPv4N19i2c_mem_addr_size_t23I2C_MEM_ADDR_SIZE_16BITE "永久链接至目标")
    :   i2c memory address size 16bit
