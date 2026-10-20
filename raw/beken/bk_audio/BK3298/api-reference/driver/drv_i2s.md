---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/driver/drv_i2s.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="drv-i2s"></a>

# DRV\_I2S

<a id="drv-i2s-api-status"></a>

## DRV\_I2S API Status

| API |
| --- |
| [`i2s_init()`](#_CPPv48i2s_init3I2S8uint32_t8uint32_t8uint32_t8uint32_t "i2s_init") |
| [`i2s_ctrl()`](#_CPPv48i2s_ctrl3I2S8uint32_t8uint32_t "i2s_ctrl") |
| [`i2s_enable()`](#_CPPv410i2s_enable3I2S8uint32_t "i2s_enable") |
| [`i2s_rx_int_enbale()`](#_CPPv417i2s_rx_int_enbale3I2S8uint32_t "i2s_rx_int_enbale") |
| [`i2s_tx_int_enbale()`](#_CPPv417i2s_tx_int_enbale3I2S8uint32_t "i2s_tx_int_enbale") |
| [`i2s_fifo_port_get()`](#_CPPv417i2s_fifo_port_get3I2S8uint32_t "i2s_fifo_port_get") |

<a id="drv-i2c-unit-number"></a>

## DRV\_I2C UNIT Number

| Capability | Number |
| --- | --- |
| UNIT Number | 1 |

<a id="drv-i2s-pin-and-gpio-map"></a>

## DRV\_I2S Pin and GPIO Map

| SPI Pin | Number |
| --- | --- |
| I2S0 BSCK | 13 |
| I2S0 SCLK | 14 |
| I2S0 DIN | 15 |
| I2S0 DOUT | 16 |

<a id="drv-i2s-api-reference"></a>

## DRV\_I2S API Reference

<a id="header-file"></a>

### Header File

- [driver/i2s/drv\_i2s.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/driver/i2s/drv_i2s.h)

<a id="functions"></a>

### Functions

<a id="_CPPv48i2s_init3I2S8uint32_t8uint32_t8uint32_t8uint32_t"></a>

<a id="_CPPv38i2s_init3I2S8uint32_t8uint32_t8uint32_t8uint32_t"></a> <a id="_CPPv28i2s_init3I2S8uint32_t8uint32_t8uint32_t8uint32_t"></a> <a id="i2s_init__I2S.uint32_t.uint32_t.uint32_t.uint32_t"></a> <a id="drv__i2s_8h_1ab911a00315a8254b88d1a2172714c4d2"></a> int32\_t i2s\_init([I2S](#_CPPv43I2S "I2S") i, uint32\_t mode, uint32\_t sample\_rate, uint32\_t sample\_width, uint32\_t sample\_ratio)
:   I2S initialization.

    参见

    I2S\_ROLE

    参数:
    :   - **i** – I2S index
        - **mode** – I2S mode,
        - **sample\_rate** – sampel rate
        - **sample\_width** – sample width
        - **sample\_ratio** – sample ratio

    返回:
    :   error code

<a id="_CPPv48i2s_ctrl3I2S8uint32_t8uint32_t"></a>

<a id="_CPPv38i2s_ctrl3I2S8uint32_t8uint32_t"></a> <a id="_CPPv28i2s_ctrl3I2S8uint32_t8uint32_t"></a> <a id="i2s_ctrl__I2S.uint32_t.uint32_t"></a> <a id="drv__i2s_8h_1a34e36220488ae501fcd85543845ea4b6"></a> int32\_t i2s\_ctrl([I2S](#_CPPv43I2S "I2S") i, uint32\_t cmd, uint32\_t arg)
:   I2S control.

    参见

    I2S\_CTRL\_CMD

    参数:
    :   - **i** – I2S index
        - **cmd** – control command,
        - **arg** – control argument

    返回:
    :   error code

<a id="_CPPv410i2s_enable3I2S8uint32_t"></a>

<a id="_CPPv310i2s_enable3I2S8uint32_t"></a> <a id="_CPPv210i2s_enable3I2S8uint32_t"></a> <a id="i2s_enable__I2S.uint32_t"></a> <a id="drv__i2s_8h_1ae0c46cfcac481956421c8454544c78ec"></a> void i2s\_enable([I2S](#_CPPv43I2S "I2S") i, uint32\_t enable)
:   I2S enable.

    参数:
    :   - **i** – I2S index
        - **enable** – 0:disable, 1:enable

    返回:
    :   NULL

<a id="_CPPv417i2s_rx_int_enbale3I2S8uint32_t"></a>

<a id="_CPPv317i2s_rx_int_enbale3I2S8uint32_t"></a> <a id="_CPPv217i2s_rx_int_enbale3I2S8uint32_t"></a> <a id="i2s_rx_int_enbale__I2S.uint32_t"></a> <a id="drv__i2s_8h_1aabbabe769d29268702d1ce4ca09d349d"></a> void i2s\_rx\_int\_enbale([I2S](#_CPPv43I2S "I2S") i, uint32\_t enable)
:   I2S rx interrupt enable.

    参数:
    :   - **i** – I2S index
        - **enable** – 0:disable, 1:enable

    返回:
    :   NULL

<a id="_CPPv417i2s_tx_int_enbale3I2S8uint32_t"></a>

<a id="_CPPv317i2s_tx_int_enbale3I2S8uint32_t"></a> <a id="_CPPv217i2s_tx_int_enbale3I2S8uint32_t"></a> <a id="i2s_tx_int_enbale__I2S.uint32_t"></a> <a id="drv__i2s_8h_1a66b201beed0890d772b31a1455c68dc2"></a> void i2s\_tx\_int\_enbale([I2S](#_CPPv43I2S "I2S") i, uint32\_t enable)
:   I2S tx interrupt enable.

    参数:
    :   - **i** – I2S index
        - **enable** – 0:disable, 1:enable

    返回:
    :   NULL

<a id="_CPPv417i2s_fifo_port_get3I2S8uint32_t"></a>

<a id="_CPPv317i2s_fifo_port_get3I2S8uint32_t"></a> <a id="_CPPv217i2s_fifo_port_get3I2S8uint32_t"></a> <a id="i2s_fifo_port_get__I2S.uint32_t"></a> <a id="drv__i2s_8h_1a47bbd91863dcc34c133100fc3c18d56f"></a> uint32\_t i2s\_fifo\_port\_get([I2S](#_CPPv43I2S "I2S") i, uint32\_t n)
:   I2S FIFO port address get.

    参数:
    :   - **i** – I2S index
        - **n** – I2S channel index, range form 0 \~ 3

    返回:
    :   I2S FIFO port address

<a id="macros"></a>

### Macros

<a id="c.i2s_master_init"></a>

<a id="drv__i2s_8h_1afa147ac616619dcdad490598c0ad2f06"></a> i2s\_master\_init(i, sample\_rate, sample\_width, sample\_ratio)

<a id="c.i2s_slaver_init"></a>

<a id="drv__i2s_8h_1a2475ba158446d532e5a5264386c4f508"></a> i2s\_slaver\_init(i, sample\_rate, sample\_width, sample\_ratio)

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv43I2S"></a>

<a id="_CPPv33I2S"></a> <a id="_CPPv23I2S"></a> <a id="drv__i2s_8h_1a3743af819ed43a3623342fc7c420fc86"></a> enum I2S
:   I2S definition.

    *Values:*

    <a id="_CPPv4N3I2S4I2S0E"></a>

    <a id="_CPPv3N3I2S4I2S0E"></a> <a id="_CPPv2N3I2S4I2S0E"></a> <a id="drv__i2s_8h_1a3743af819ed43a3623342fc7c420fc86a15ba9b13dc076204628bcd32be35c9ec"></a> enumerator I2S0

    <a id="_CPPv4N3I2S4I2S1E"></a>

    <a id="_CPPv3N3I2S4I2S1E"></a> <a id="_CPPv2N3I2S4I2S1E"></a> <a id="drv__i2s_8h_1a3743af819ed43a3623342fc7c420fc86aa928acaeafa6e2d85eb37143a5265846"></a> enumerator I2S1

    <a id="_CPPv4N3I2S4I2S2E"></a>

    <a id="_CPPv3N3I2S4I2S2E"></a> <a id="_CPPv2N3I2S4I2S2E"></a> <a id="drv__i2s_8h_1a3743af819ed43a3623342fc7c420fc86a30fd7e772d4da12dd92d3261b3272476"></a> enumerator I2S2

    <a id="_CPPv4N3I2S4I2S3E"></a>

    <a id="_CPPv3N3I2S4I2S3E"></a> <a id="_CPPv2N3I2S4I2S3E"></a> <a id="drv__i2s_8h_1a3743af819ed43a3623342fc7c420fc86a7840d13bbfe2a3fc5fc6b59e772063c9"></a> enumerator I2S3

    <a id="_CPPv4N3I2S4I2S4E"></a>

    <a id="_CPPv3N3I2S4I2S4E"></a> <a id="_CPPv2N3I2S4I2S4E"></a> <a id="drv__i2s_8h_1a3743af819ed43a3623342fc7c420fc86ab9c5bfd32b17078f19a42d350c933ad4"></a> enumerator I2S4

<a id="_CPPv48I2S_ROLE"></a>

<a id="_CPPv38I2S_ROLE"></a> <a id="_CPPv28I2S_ROLE"></a> <a id="drv__i2s_8h_1ab2f20612f34fef15b28acb70283cb3c6"></a> enum I2S\_ROLE
:   I2S role definition.

    *Values:*

    <a id="_CPPv4N8I2S_ROLE15I2S_ROLE_MASTERE"></a>

    <a id="_CPPv3N8I2S_ROLE15I2S_ROLE_MASTERE"></a> <a id="_CPPv2N8I2S_ROLE15I2S_ROLE_MASTERE"></a> <a id="drv__i2s_8h_1ab2f20612f34fef15b28acb70283cb3c6a150cd0ed470f1cab13a6c0cacf4a090d"></a> enumerator I2S\_ROLE\_MASTER

    <a id="_CPPv4N8I2S_ROLE14I2S_ROLE_SLAVEE"></a>

    <a id="_CPPv3N8I2S_ROLE14I2S_ROLE_SLAVEE"></a> <a id="_CPPv2N8I2S_ROLE14I2S_ROLE_SLAVEE"></a> <a id="drv__i2s_8h_1ab2f20612f34fef15b28acb70283cb3c6ad1aad5aa5bddd1e447c7775b7ba921dc"></a> enumerator I2S\_ROLE\_SLAVE

<a id="_CPPv48I2S_MODE"></a>

<a id="_CPPv38I2S_MODE"></a> <a id="_CPPv28I2S_MODE"></a> <a id="drv__i2s_8h_1aa6160b1c3f58c0b656ded311c5b38995"></a> enum I2S\_MODE
:   I2S mode definition.

    *Values:*

    <a id="_CPPv4N8I2S_MODE15I2S_MODE_PHILIPE"></a>

    <a id="_CPPv3N8I2S_MODE15I2S_MODE_PHILIPE"></a> <a id="_CPPv2N8I2S_MODE15I2S_MODE_PHILIPE"></a> <a id="drv__i2s_8h_1aa6160b1c3f58c0b656ded311c5b38995a547747b6ceade41a7d2a72045e640243"></a> enumerator I2S\_MODE\_PHILIP

    <a id="_CPPv4N8I2S_MODE23I2S_MODE_LEFT_JUSTIFIEDE"></a>

    <a id="_CPPv3N8I2S_MODE23I2S_MODE_LEFT_JUSTIFIEDE"></a> <a id="_CPPv2N8I2S_MODE23I2S_MODE_LEFT_JUSTIFIEDE"></a> <a id="drv__i2s_8h_1aa6160b1c3f58c0b656ded311c5b38995a32c5f53159a8a7cf45cc8f11a3755185"></a> enumerator I2S\_MODE\_LEFT\_JUSTIFIED

    <a id="_CPPv4N8I2S_MODE24I2S_MODE_RIGHT_JUSTIFIEDE"></a>

    <a id="_CPPv3N8I2S_MODE24I2S_MODE_RIGHT_JUSTIFIEDE"></a> <a id="_CPPv2N8I2S_MODE24I2S_MODE_RIGHT_JUSTIFIEDE"></a> <a id="drv__i2s_8h_1aa6160b1c3f58c0b656ded311c5b38995a4892e1a30ba4ab5cdd5af7454d67fcb3"></a> enumerator I2S\_MODE\_RIGHT\_JUSTIFIED

    <a id="_CPPv4N8I2S_MODE25I2S_MODE_SHORT_FRAME_SYNCE"></a>

    <a id="_CPPv3N8I2S_MODE25I2S_MODE_SHORT_FRAME_SYNCE"></a> <a id="_CPPv2N8I2S_MODE25I2S_MODE_SHORT_FRAME_SYNCE"></a> <a id="drv__i2s_8h_1aa6160b1c3f58c0b656ded311c5b38995a3a562eca7ea03c6c2e55ffce00df2540"></a> enumerator I2S\_MODE\_SHORT\_FRAME\_SYNC

    <a id="_CPPv4N8I2S_MODE24I2S_MODE_LONG_FRAME_SYNCE"></a>

    <a id="_CPPv3N8I2S_MODE24I2S_MODE_LONG_FRAME_SYNCE"></a> <a id="_CPPv2N8I2S_MODE24I2S_MODE_LONG_FRAME_SYNCE"></a> <a id="drv__i2s_8h_1aa6160b1c3f58c0b656ded311c5b38995a5e61487ad9242c7cb54fba47ca7917b4"></a> enumerator I2S\_MODE\_LONG\_FRAME\_SYNC

    <a id="_CPPv4N8I2S_MODE20I2S_MODE_NORMAL_2B_DE"></a>

    <a id="_CPPv3N8I2S_MODE20I2S_MODE_NORMAL_2B_DE"></a> <a id="_CPPv2N8I2S_MODE20I2S_MODE_NORMAL_2B_DE"></a> <a id="drv__i2s_8h_1aa6160b1c3f58c0b656ded311c5b38995a9146adf335c9ffb5e16b4ca91008be73"></a> enumerator I2S\_MODE\_NORMAL\_2B\_D

    <a id="_CPPv4N8I2S_MODE19I2S_MODE_DELAY_2B_DE"></a>

    <a id="_CPPv3N8I2S_MODE19I2S_MODE_DELAY_2B_DE"></a> <a id="_CPPv2N8I2S_MODE19I2S_MODE_DELAY_2B_DE"></a> <a id="drv__i2s_8h_1aa6160b1c3f58c0b656ded311c5b38995a37b5d2c38724c41baa6cbb870dc8b404"></a> enumerator I2S\_MODE\_DELAY\_2B\_D

<a id="_CPPv414I2S_ERROR_CODE"></a>

<a id="_CPPv314I2S_ERROR_CODE"></a> <a id="_CPPv214I2S_ERROR_CODE"></a> <a id="drv__i2s_8h_1acbf8487eaa143dd4681c622870425b66"></a> enum I2S\_ERROR\_CODE
:   I2S error code definition.

    *Values:*

    <a id="_CPPv4N14I2S_ERROR_CODE17I2S_ERROR_CODE_OKE"></a>

    <a id="_CPPv3N14I2S_ERROR_CODE17I2S_ERROR_CODE_OKE"></a> <a id="_CPPv2N14I2S_ERROR_CODE17I2S_ERROR_CODE_OKE"></a> <a id="drv__i2s_8h_1acbf8487eaa143dd4681c622870425b66a0d8b16079ae2e7f4369bd73b9660cdf8"></a> enumerator I2S\_ERROR\_CODE\_OK

    <a id="_CPPv4N14I2S_ERROR_CODE32I2S_ERROR_CODE_INVALID_PARAMETERE"></a>

    <a id="_CPPv3N14I2S_ERROR_CODE32I2S_ERROR_CODE_INVALID_PARAMETERE"></a> <a id="_CPPv2N14I2S_ERROR_CODE32I2S_ERROR_CODE_INVALID_PARAMETERE"></a> <a id="drv__i2s_8h_1acbf8487eaa143dd4681c622870425b66a298dd4af548c4ff37ec32d153bb0f414"></a> enumerator I2S\_ERROR\_CODE\_INVALID\_PARAMETER

<a id="_CPPv412I2S_CTRL_CMD"></a>

<a id="_CPPv312I2S_CTRL_CMD"></a> <a id="_CPPv212I2S_CTRL_CMD"></a> <a id="drv__i2s_8h_1af53471f773ac54f888aeddb9c3980117"></a> enum I2S\_CTRL\_CMD
:   I2S control command definition.

    *Values:*

    <a id="_CPPv4N12I2S_CTRL_CMD26I2S_CTRL_CMD_SET_SMP_RATIOE"></a>

    <a id="_CPPv3N12I2S_CTRL_CMD26I2S_CTRL_CMD_SET_SMP_RATIOE"></a> <a id="_CPPv2N12I2S_CTRL_CMD26I2S_CTRL_CMD_SET_SMP_RATIOE"></a> <a id="drv__i2s_8h_1af53471f773ac54f888aeddb9c3980117accebbafdcf64840615d86da0ac6ad249"></a> enumerator I2S\_CTRL\_CMD\_SET\_SMP\_RATIO

    <a id="_CPPv4N12I2S_CTRL_CMD21I2S_CTRL_CMD_SET_DLENE"></a>

    <a id="_CPPv3N12I2S_CTRL_CMD21I2S_CTRL_CMD_SET_DLENE"></a> <a id="_CPPv2N12I2S_CTRL_CMD21I2S_CTRL_CMD_SET_DLENE"></a> <a id="drv__i2s_8h_1af53471f773ac54f888aeddb9c3980117a7052c0f0b705a009e6db0ae335580926"></a> enumerator I2S\_CTRL\_CMD\_SET\_DLEN

    <a id="_CPPv4N12I2S_CTRL_CMD26I2S_CTRL_CMD_SET_BIT_WIDTHE"></a>

    <a id="_CPPv3N12I2S_CTRL_CMD26I2S_CTRL_CMD_SET_BIT_WIDTHE"></a> <a id="_CPPv2N12I2S_CTRL_CMD26I2S_CTRL_CMD_SET_BIT_WIDTHE"></a> <a id="drv__i2s_8h_1af53471f773ac54f888aeddb9c3980117a5e9c02fbd872ace670d6d7c731519967"></a> enumerator I2S\_CTRL\_CMD\_SET\_BIT\_WIDTH

    <a id="_CPPv4N12I2S_CTRL_CMD21I2S_CTRL_CMD_SET_SLENE"></a>

    <a id="_CPPv3N12I2S_CTRL_CMD21I2S_CTRL_CMD_SET_SLENE"></a> <a id="_CPPv2N12I2S_CTRL_CMD21I2S_CTRL_CMD_SET_SLENE"></a> <a id="drv__i2s_8h_1af53471f773ac54f888aeddb9c3980117a71ea357bce9821aec6a68a4652d4043d"></a> enumerator I2S\_CTRL\_CMD\_SET\_SLEN

    <a id="_CPPv4N12I2S_CTRL_CMD26I2S_CTRL_CMD_SET_LSB_FIRSTE"></a>

    <a id="_CPPv3N12I2S_CTRL_CMD26I2S_CTRL_CMD_SET_LSB_FIRSTE"></a> <a id="_CPPv2N12I2S_CTRL_CMD26I2S_CTRL_CMD_SET_LSB_FIRSTE"></a> <a id="drv__i2s_8h_1af53471f773ac54f888aeddb9c3980117a9c810615d38fbcf645ed2a3fb0ee3458"></a> enumerator I2S\_CTRL\_CMD\_SET\_LSB\_FIRST

    <a id="_CPPv4N12I2S_CTRL_CMD28I2S_CTRL_CMD_SET_BIT_CLK_INVE"></a>

    <a id="_CPPv3N12I2S_CTRL_CMD28I2S_CTRL_CMD_SET_BIT_CLK_INVE"></a> <a id="_CPPv2N12I2S_CTRL_CMD28I2S_CTRL_CMD_SET_BIT_CLK_INVE"></a> <a id="drv__i2s_8h_1af53471f773ac54f888aeddb9c3980117a06296aaf3dd4cfdea937d7019e786ad1"></a> enumerator I2S\_CTRL\_CMD\_SET\_BIT\_CLK\_INV

    <a id="_CPPv4N12I2S_CTRL_CMD27I2S_CTRL_CMD_SET_LR_CLK_INVE"></a>

    <a id="_CPPv3N12I2S_CTRL_CMD27I2S_CTRL_CMD_SET_LR_CLK_INVE"></a> <a id="_CPPv2N12I2S_CTRL_CMD27I2S_CTRL_CMD_SET_LR_CLK_INVE"></a> <a id="drv__i2s_8h_1af53471f773ac54f888aeddb9c3980117a1baff00e1cafb3fa4c421fabba0e9d0f"></a> enumerator I2S\_CTRL\_CMD\_SET\_LR\_CLK\_INV

    <a id="_CPPv4N12I2S_CTRL_CMD21I2S_CTRL_CMD_SET_MODEE"></a>

    <a id="_CPPv3N12I2S_CTRL_CMD21I2S_CTRL_CMD_SET_MODEE"></a> <a id="_CPPv2N12I2S_CTRL_CMD21I2S_CTRL_CMD_SET_MODEE"></a> <a id="drv__i2s_8h_1af53471f773ac54f888aeddb9c3980117a0b115e133459b5fba90b95b79613ca36"></a> enumerator I2S\_CTRL\_CMD\_SET\_MODE

    <a id="_CPPv4N12I2S_CTRL_CMD29I2S_CTRL_CMD_SET_RX_THRESHOLDE"></a>

    <a id="_CPPv3N12I2S_CTRL_CMD29I2S_CTRL_CMD_SET_RX_THRESHOLDE"></a> <a id="_CPPv2N12I2S_CTRL_CMD29I2S_CTRL_CMD_SET_RX_THRESHOLDE"></a> <a id="drv__i2s_8h_1af53471f773ac54f888aeddb9c3980117a24e5eabf596f6b5f463df06f2dc737c7"></a> enumerator I2S\_CTRL\_CMD\_SET\_RX\_THRESHOLD

    <a id="_CPPv4N12I2S_CTRL_CMD29I2S_CTRL_CMD_SET_TX_THRESHOLDE"></a>

    <a id="_CPPv3N12I2S_CTRL_CMD29I2S_CTRL_CMD_SET_TX_THRESHOLDE"></a> <a id="_CPPv2N12I2S_CTRL_CMD29I2S_CTRL_CMD_SET_TX_THRESHOLDE"></a> <a id="drv__i2s_8h_1af53471f773ac54f888aeddb9c3980117adfc2c8c79b402a175cc9d58f74548a1c"></a> enumerator I2S\_CTRL\_CMD\_SET\_TX\_THRESHOLD

    <a id="_CPPv4N12I2S_CTRL_CMD34I2S_CTRL_CMD_SET_DOWN_SAMPLE_RATIOE"></a>

    <a id="_CPPv3N12I2S_CTRL_CMD34I2S_CTRL_CMD_SET_DOWN_SAMPLE_RATIOE"></a> <a id="_CPPv2N12I2S_CTRL_CMD34I2S_CTRL_CMD_SET_DOWN_SAMPLE_RATIOE"></a> <a id="drv__i2s_8h_1af53471f773ac54f888aeddb9c3980117a17acf53f59961719f583a630b3a69495"></a> enumerator I2S\_CTRL\_CMD\_SET\_DOWN\_SAMPLE\_RATIO

    <a id="_CPPv4N12I2S_CTRL_CMD29I2S_CTRL_CMD_SET_BIT_SEQ_MODEE"></a>

    <a id="_CPPv3N12I2S_CTRL_CMD29I2S_CTRL_CMD_SET_BIT_SEQ_MODEE"></a> <a id="_CPPv2N12I2S_CTRL_CMD29I2S_CTRL_CMD_SET_BIT_SEQ_MODEE"></a> <a id="drv__i2s_8h_1af53471f773ac54f888aeddb9c3980117ae436254f15ad602e80d8b53a0a562899"></a> enumerator I2S\_CTRL\_CMD\_SET\_BIT\_SEQ\_MODE

    <a id="_CPPv4N12I2S_CTRL_CMD29I2S_CTRL_CMD_SET_TX_FIFO_MODEE"></a>

    <a id="_CPPv3N12I2S_CTRL_CMD29I2S_CTRL_CMD_SET_TX_FIFO_MODEE"></a> <a id="_CPPv2N12I2S_CTRL_CMD29I2S_CTRL_CMD_SET_TX_FIFO_MODEE"></a> <a id="drv__i2s_8h_1af53471f773ac54f888aeddb9c3980117a2227fda97a31808c80f8987628cc697e"></a> enumerator I2S\_CTRL\_CMD\_SET\_TX\_FIFO\_MODE

    <a id="_CPPv4N12I2S_CTRL_CMD20I2S_CTRL_CMD_RX_TRIGE"></a>

    <a id="_CPPv3N12I2S_CTRL_CMD20I2S_CTRL_CMD_RX_TRIGE"></a> <a id="_CPPv2N12I2S_CTRL_CMD20I2S_CTRL_CMD_RX_TRIGE"></a> <a id="drv__i2s_8h_1af53471f773ac54f888aeddb9c3980117a6eceb7234f3b6b85f6e1d85d0ab684c6"></a> enumerator I2S\_CTRL\_CMD\_RX\_TRIG

    <a id="_CPPv4N12I2S_CTRL_CMD25I2S_CTRL_CMD_LR_COM_STOREE"></a>

    <a id="_CPPv3N12I2S_CTRL_CMD25I2S_CTRL_CMD_LR_COM_STOREE"></a> <a id="_CPPv2N12I2S_CTRL_CMD25I2S_CTRL_CMD_LR_COM_STOREE"></a> <a id="drv__i2s_8h_1af53471f773ac54f888aeddb9c3980117a63cc942e2866a42559e68164ce5c1486"></a> enumerator I2S\_CTRL\_CMD\_LR\_COM\_STORE

    <a id="_CPPv4N12I2S_CTRL_CMD24I2S_CTRL_CMD_PARALLEL_ENE"></a>

    <a id="_CPPv3N12I2S_CTRL_CMD24I2S_CTRL_CMD_PARALLEL_ENE"></a> <a id="_CPPv2N12I2S_CTRL_CMD24I2S_CTRL_CMD_PARALLEL_ENE"></a> <a id="drv__i2s_8h_1af53471f773ac54f888aeddb9c3980117abf6a6a3eaef85c3b064fbc245bfda5d1"></a> enumerator I2S\_CTRL\_CMD\_PARALLEL\_EN
