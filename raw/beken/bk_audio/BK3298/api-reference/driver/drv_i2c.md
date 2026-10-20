---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/driver/drv_i2c.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="drv-i2c"></a>

# DRV\_I2C

<a id="drv-i2c-api-status"></a>

## DRV\_I2C API Status

| API |
| --- |
| [`drv_i2c_init()`](#_CPPv412drv_i2c_init8uint32_t8uint16_t8uint32_t "drv_i2c_init") |
| [`drv_i2c_deinit()`](#_CPPv414drv_i2c_deinit8uint32_t "drv_i2c_deinit") |
| [`drv_i2c_master_trx()`](#_CPPv418drv_i2c_master_trx8uint32_tP7uint8_t8uint16_t8uint16_tb14pfunc_i2c_cb_tPv "drv_i2c_master_trx") |
| [`drv_i2c_slave_rx()`](#_CPPv416drv_i2c_slave_rx8uint32_tP7uint8_t8uint16_t14pfunc_i2c_cb_tPv "drv_i2c_slave_rx") |
| [`drv_i2c_slave_tx()`](#_CPPv416drv_i2c_slave_tx8uint32_tP7uint8_t8uint16_t14pfunc_i2c_cb_tPv "drv_i2c_slave_tx") |

<a id="drv-i2c-unit-number"></a>

## DRV\_I2C UNIT Number

| Capability | Number |
| --- | --- |
| UNIT Number | 2 |

<a id="drv-i2c-pin-and-gpio-map"></a>

## DRV\_I2C Pin and GPIO Map

| SPI Pin | Number |
| --- | --- |
| I2C0 SCK | 0 |
| I2C0 SDA | 1 |
| I2C1 SCK | 7 |
| I2C1 SDA | 8 |

<a id="drv-i2c-api-reference"></a>

## DRV\_I2C API Reference

<a id="header-file"></a>

### Header File

- [driver/i2c/drv\_i2c.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/driver/i2c/drv_i2c.h)

<a id="functions"></a>

### Functions

<a id="_CPPv412drv_i2c_init8uint32_t8uint16_t8uint32_t"></a>

<a id="_CPPv312drv_i2c_init8uint32_t8uint16_t8uint32_t"></a> <a id="_CPPv212drv_i2c_init8uint32_t8uint16_t8uint32_t"></a> <a id="drv_i2c_init__uint32_t.uint16_t.uint32_t"></a> <a id="drv__i2c_8h_1a4a7209c1d2a1a9583006a6c4f3ae0e34"></a> uint32\_t drv\_i2c\_init(uint32\_t dev\_index, uint16\_t slv\_addr\_7bit, uint32\_t work\_clk\_hz)
:   init a I2C device.

    初始化I2C设备. 由于我们的I2C同时支持master和slave角色，所以如果期望切换角色或者 切换不同的工作clock，或者slv\_addr有变动的时候，就需要再次调用该函数

    参数:
    :   - **dev\_index** – **\[in\]** device index, from 0(the first device), \< [I2C\_DEVICE\_NUM](#drv__i2c_8h_1a039d14c826b8b95ba0d9ceeeb21c4220)
        - **slv\_addr\_7bit** – **\[in\]** for master: it is equal zero for slave: it’s own address, only high 7 bit in the first byte from master 不包括第一个byte的最低位的读写位，如果是10bit地址，也是纯地址部分
        - **work\_clk\_hz** – **\[in\]** work clock in HZ

    返回值:
    :   - **0** – fail
        - **other** – success

    返回:
    :   device instance

<a id="_CPPv414drv_i2c_deinit8uint32_t"></a>

<a id="_CPPv314drv_i2c_deinit8uint32_t"></a> <a id="_CPPv214drv_i2c_deinit8uint32_t"></a> <a id="drv_i2c_deinit__uint32_t"></a> <a id="drv__i2c_8h_1acb645a09299ea29a2d8efd537c27c9f6"></a> int32\_t drv\_i2c\_deinit(uint32\_t dev\_instance)
:   deinit a I2C device.

    反初始化I2C设备。是 [drv\_i2c\_init()](#drv__i2c_8h_1a4a7209c1d2a1a9583006a6c4f3ae0e34)的反向操作。两次调用 [drv\_i2c\_init()](#drv__i2c_8h_1a4a7209c1d2a1a9583006a6c4f3ae0e34)之间需要 调用一次 [drv\_i2c\_deinit()](#drv__i2c_8h_1acb645a09299ea29a2d8efd537c27c9f6)

    参数:
    :   **dev\_instance** – **\[in\]** return value of [drv\_i2c\_init()](#drv__i2c_8h_1a4a7209c1d2a1a9583006a6c4f3ae0e34)

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv418drv_i2c_master_trx8uint32_tP7uint8_t8uint16_t8uint16_tb14pfunc_i2c_cb_tPv"></a>

<a id="_CPPv318drv_i2c_master_trx8uint32_tP7uint8_t8uint16_t8uint16_tb14pfunc_i2c_cb_tPv"></a> <a id="_CPPv218drv_i2c_master_trx8uint32_tP7uint8_t8uint16_t8uint16_tb14pfunc_i2c_cb_tPv"></a> <a id="drv_i2c_master_trx__uint32_t.uint8_tP.uint16_t.uint16_t.b.pfunc_i2c_cb_t.voidP"></a> <a id="drv__i2c_8h_1ad66bb41f58fdf9f4c8cd8b307e72f498"></a> int32\_t drv\_i2c\_master\_trx(uint32\_t dev\_instance, uint8\_t \*pu1\_buf, uint16\_t tx\_size, uint16\_t rx\_size, bool gen\_stop, [pfunc\_i2c\_cb\_t](#_CPPv414pfunc_i2c_cb_t "pfunc_i2c_cb_t") pfn\_cb, void \*pv\_arg)
:   master tx and rx data on I2C bus.

    master发起tx和rx的动作，也可以只进行tx的动作。pu1\_buf 的第一个byte是寻址信息 该函数是一个异步函数，完成RX的动作后会调用回调函数 pfn\_cb 进行通知

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_i2c\_init()](#drv__i2c_8h_1a4a7209c1d2a1a9583006a6c4f3ae0e34)
        - **pu1\_buf** – **\[in\]** tx/rx buffer pointer, buffer size is tx\_size\+rx\_size
        - **tx\_size** – **\[in\]** buffer tx size in byte, slave address is in this feild
        - **rx\_size** – **\[in\]** buffer rx size in byte, 0 if you want to rx nothing
        - **gen\_stop** – **\[in\]** true: send stop when transfer finish false: do not send stop
        - **pfn\_cb** – **\[in\]** finish callback
        - **pv\_arg** – **\[in\]** argument for rx finish callback

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv416drv_i2c_slave_rx8uint32_tP7uint8_t8uint16_t14pfunc_i2c_cb_tPv"></a>

<a id="_CPPv316drv_i2c_slave_rx8uint32_tP7uint8_t8uint16_t14pfunc_i2c_cb_tPv"></a> <a id="_CPPv216drv_i2c_slave_rx8uint32_tP7uint8_t8uint16_t14pfunc_i2c_cb_tPv"></a> <a id="drv_i2c_slave_rx__uint32_t.uint8_tP.uint16_t.pfunc_i2c_cb_t.voidP"></a> <a id="drv__i2c_8h_1a70646d5a292b85f36c0797a8a59faecf"></a> int32\_t drv\_i2c\_slave\_rx(uint32\_t dev\_instance, uint8\_t \*pu1\_buf, uint16\_t rx\_size, [pfunc\_i2c\_cb\_t](#_CPPv414pfunc_i2c_cb_t "pfunc_i2c_cb_t") pfn\_cb, void \*pv\_arg)
:   slave rx data on I2C bus.

    slave RX data, pu1\_buf的数据不包括slave address部分 该函数是一个异步函数，完成RX的动作后会调用回调函数 pfn\_cb 进行通知

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_i2c\_init()](#drv__i2c_8h_1a4a7209c1d2a1a9583006a6c4f3ae0e34)
        - **pu1\_buf** – **\[in\]** rx buffer pointer
        - **rx\_size** – **\[in\]** rx buffer size in byte
        - **pfn\_cb** – **\[in\]** rx finish callback
        - **pv\_arg** – **\[in\]** argument for rx finish callback

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="_CPPv416drv_i2c_slave_tx8uint32_tP7uint8_t8uint16_t14pfunc_i2c_cb_tPv"></a>

<a id="_CPPv316drv_i2c_slave_tx8uint32_tP7uint8_t8uint16_t14pfunc_i2c_cb_tPv"></a> <a id="_CPPv216drv_i2c_slave_tx8uint32_tP7uint8_t8uint16_t14pfunc_i2c_cb_tPv"></a> <a id="drv_i2c_slave_tx__uint32_t.uint8_tP.uint16_t.pfunc_i2c_cb_t.voidP"></a> <a id="drv__i2c_8h_1a0938f8b815c2dae4738ee9278ec775b9"></a> int32\_t drv\_i2c\_slave\_tx(uint32\_t dev\_instance, uint8\_t \*pu1\_buf, uint16\_t tx\_size, [pfunc\_i2c\_cb\_t](#_CPPv414pfunc_i2c_cb_t "pfunc_i2c_cb_t") pfn\_cb, void \*pv\_arg)
:   slave tx data on I2C bus.

    slave TX data, pu1\_buf的数据不包括address byte 该函数是一个异步函数，完成TX的动作后会调用回调函数 pfn\_cb 进行通知

    参数:
    :   - **dev\_instance** – **\[in\]** return value of [drv\_i2c\_init()](#drv__i2c_8h_1a4a7209c1d2a1a9583006a6c4f3ae0e34)
        - **pu1\_buf** – **\[in\]** tx buffer pointer
        - **tx\_size** – **\[in\]** tx buffer size in byte
        - **pfn\_cb** – **\[in\]** tx finish callback
        - **pv\_arg** – **\[in\]** argument for tx finish callback

    返回值:
    :   - **0** – success \[BK\_RET\_OK\]
        - **other** – fail

    返回:
    :   result

<a id="macros"></a>

### Macros

<a id="c.I2C_DEVICE_NUM"></a>

<a id="drv__i2c_8h_1a039d14c826b8b95ba0d9ceeeb21c4220"></a> I2C\_DEVICE\_NUM
:   I2C device number.

<a id="c.I2C_RW_FLAG_INDICATOR_WRITE"></a>

<a id="drv__i2c_8h_1abda68b9a38d6b55968a7e48a2bbb15b6"></a> I2C\_RW\_FLAG\_INDICATOR\_WRITE

<a id="c.I2C_RW_FLAG_INDICATOR_READ"></a>

<a id="drv__i2c_8h_1a230373f8eb58a3e116819db649a8f3c6"></a> I2C\_RW\_FLAG\_INDICATOR\_READ

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv414drv_i2c_role_e"></a>

<a id="_CPPv314drv_i2c_role_e"></a> <a id="_CPPv214drv_i2c_role_e"></a> <a id="drv_i2c_role_e"></a> <a id="drv__i2c_8h_1a7da2244160e5628a4d35eb3839604ed2"></a> typedef enum [\_drv\_i2c\_role\_e](#_CPPv415_drv_i2c_role_e "_drv_i2c_role_e") drv\_i2c\_role\_e
:   driver I2C work role

<a id="_CPPv414pfunc_i2c_cb_t"></a>

<a id="_CPPv314pfunc_i2c_cb_t"></a> <a id="_CPPv214pfunc_i2c_cb_t"></a> <a id="pfunc_i2c_cb_t"></a> <a id="drv__i2c_8h_1a0d814f0ac81078b71d27cbf0c4a5376a"></a> typedef void (\*pfunc\_i2c\_cb\_t)(uint32\_t dev\_instance, int32\_t err\_code, void \*pv\_arg)
:   driver I2C callback for tx or rx, it means no error when err\_code\=\=0

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv415_drv_i2c_role_e"></a>

<a id="_CPPv315_drv_i2c_role_e"></a> <a id="_CPPv215_drv_i2c_role_e"></a> <a id="drv__i2c_8h_1a53e2bfec99c29e5add78a782336f8f9e"></a> enum \_drv\_i2c\_role\_e
:   driver I2C work role

    *Values:*

    <a id="_CPPv4N15_drv_i2c_role_e14DRV_I2C_MASTERE"></a>

    <a id="_CPPv3N15_drv_i2c_role_e14DRV_I2C_MASTERE"></a> <a id="_CPPv2N15_drv_i2c_role_e14DRV_I2C_MASTERE"></a> <a id="drv__i2c_8h_1a53e2bfec99c29e5add78a782336f8f9ea8ccf11e752c75f13208cb8f51b099719"></a> enumerator DRV\_I2C\_MASTER

    <a id="_CPPv4N15_drv_i2c_role_e13DRV_I2C_SLAVEE"></a>

    <a id="_CPPv3N15_drv_i2c_role_e13DRV_I2C_SLAVEE"></a> <a id="_CPPv2N15_drv_i2c_role_e13DRV_I2C_SLAVEE"></a> <a id="drv__i2c_8h_1a53e2bfec99c29e5add78a782336f8f9ea8d1c42fd17c986685fb2017959c935ac"></a> enumerator DRV\_I2C\_SLAVE
