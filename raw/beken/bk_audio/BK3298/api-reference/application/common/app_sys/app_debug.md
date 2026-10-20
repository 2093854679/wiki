---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/common/app_sys/app_debug.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="debug-application-functions"></a>

# Debug Application Functions

<a id="app-debug-api-brief"></a>

## APP\_DEBUG API Brief

| Application | Brief |
| --- | --- |
| [`beken_dbg_uart_rx()`](#_CPPv417beken_dbg_uart_rxP7uint8_t8uint16_tP7uint8_tP8uint16_t "beken_dbg_uart_rx") | beken debug cmd hander function |
| [`_bk_uart_hci_ctrl_2_uart()`](#_CPPv424_bk_uart_hci_ctrl_2_uartP7uint8_t8uint16_t "_bk_uart_hci_ctrl_2_uart") | beken\_dbg\_hci\_evt\_process brief description |
| [`_bk_uart_send_cmd_2_ctrl()`](#_CPPv424_bk_uart_send_cmd_2_ctrlv "_bk_uart_send_cmd_2_ctrl") | send dbg data to controller |

<a id="app-debug-api-reference"></a>

## APP\_DEBUG API Reference

<a id="header-file"></a>

### Header File

- [common/app\_sys/app\_debug.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/common/app_sys/app_debug.h)

<a id="functions"></a>

### Functions

<a id="_CPPv417beken_dbg_uart_rxP7uint8_t8uint16_tP7uint8_tP8uint16_t"></a>

<a id="_CPPv317beken_dbg_uart_rxP7uint8_t8uint16_tP7uint8_tP8uint16_t"></a> <a id="_CPPv217beken_dbg_uart_rxP7uint8_t8uint16_tP7uint8_tP8uint16_t"></a> <a id="beken_dbg_uart_rx__uint8_tP.uint16_t.uint8_tP.uint16_tP"></a> <a id="app__debug_8h_1a99b285fc09389b51b24d2bc0ac97af74"></a> bool beken\_dbg\_uart\_rx(uint8\_t \*p\_in\_buffer, uint16\_t in\_length, uint8\_t \*p\_out\_buffer, uint16\_t \*p\_out\_length)
:   beken debug cmd hander function

    handler uart recvice private command and data, then output mapping data or event

    参数:
    :   - **p\_in\_buffer** – **\[in\]** pointer for input buffer data
        - **in\_length** – **\[in\]** input buffer data length
        - **p\_out\_buffer** – **\[out\]** pointer for output buffer data
        - **p\_out\_length** – **\[out\]** output buffer data length

    返回值:
    :   - **TRUE** – will send data or event
        - **FALSE** – will not send data or event

    返回:
    :   result

<a id="_CPPv424_bk_uart_hci_ctrl_2_uartP7uint8_t8uint16_t"></a>

<a id="_CPPv324_bk_uart_hci_ctrl_2_uartP7uint8_t8uint16_t"></a> <a id="_CPPv224_bk_uart_hci_ctrl_2_uartP7uint8_t8uint16_t"></a> <a id="_bk_uart_hci_ctrl_2_uart__uint8_tP.uint16_t"></a> <a id="app__debug_8h_1a498fb4f740eb38c63c2ca49aa98e7420"></a> void \_bk\_uart\_hci\_ctrl\_2\_uart(uint8\_t \*p\_event, uint16\_t len)
:   beken\_dbg\_hci\_evt\_process brief description

    handle hci event and process mapping new command or data

    参数:
    :   - **p\_event** – **\[in\]** hci event data
        - **len** – **\[in\]** hci evnet data len

    返回:
    :   N/A

<a id="_CPPv424_bk_uart_send_cmd_2_ctrlv"></a>

<a id="_CPPv324_bk_uart_send_cmd_2_ctrlv"></a> <a id="_CPPv224_bk_uart_send_cmd_2_ctrlv"></a> <a id="_bk_uart_send_cmd_2_ctrl__void"></a> <a id="app__debug_8h_1ace4268142e6e1d542e181a67023af3e0"></a> void \_bk\_uart\_send\_cmd\_2\_ctrl(void)
:   send dbg data to controller

    pop pending data from dbg queue and send it to controller

    返回:
    :   N/A

<a id="macros"></a>

### Macros

<a id="c.BEKEN_OCF"></a>

<a id="app__debug_8h_1a81f59d4cf0cd98e1a6600b7a26537db5"></a> BEKEN\_OCF

<a id="c.DBG_TX_FIFO_THRD"></a>

<a id="app__debug_8h_1af3fc73146dc6828aa0f9ddb9dde9a873"></a> DBG\_TX\_FIFO\_THRD

<a id="c.HCI_EVENT_HEAD_LENGTH"></a>

<a id="app__debug_8h_1a33537e91324ecce9b9fd7f8129e40ce0"></a> HCI\_EVENT\_HEAD\_LENGTH

<a id="c.HCI_COMMAND_HEAD_LENGTH"></a>

<a id="app__debug_8h_1af7e6bb7e50d01fd70c10c1491b060973"></a> HCI\_COMMAND\_HEAD\_LENGTH

<a id="c.BEKEN_UART_LINK_CHECK"></a>

<a id="app__debug_8h_1aa4a64ae617a701d457874a1d7ff8fbd0"></a> BEKEN\_UART\_LINK\_CHECK
:   return 0x04 0x0e 0x04 0x01 0xe0 0xfc 0x00

<a id="c.BEKEN_UART_REGISTER_WRITE_CMD"></a>

<a id="app__debug_8h_1ace6de6907d17c2f9b45e627add57d6f8"></a> BEKEN\_UART\_REGISTER\_WRITE\_CMD
:   Write certain reg

<a id="c.BEKEN_UART_REGISTER_CONTINUOUS_WRITE_CMD"></a>

<a id="app__debug_8h_1a1f0db924e127d56e1f5c5cd5dc7dae31"></a> BEKEN\_UART\_REGISTER\_CONTINUOUS\_WRITE\_CMD
:   write reg continuous

<a id="c.BEKEN_UART_REGISTER_READ_CMD"></a>

<a id="app__debug_8h_1a7aa8114e592a4afb83c4522ddbcba53b"></a> BEKEN\_UART\_REGISTER\_READ\_CMD
:   read certain reg value

<a id="c.BEKEN_READ_MEM_INFO"></a>

<a id="app__debug_8h_1abc6202b0a632606196e2da6018ee958c"></a> BEKEN\_READ\_MEM\_INFO
:   read heap info

<a id="c.BEKEN_SHOW_BT_MNG_INFO"></a>

<a id="app__debug_8h_1ac64f7483187e415fba67977e6cd36658"></a> BEKEN\_SHOW\_BT\_MNG\_INFO
:   print bt app mng entity state

<a id="c.BEKEN_SHOW_BT_CTRL_INFO"></a>

<a id="app__debug_8h_1a2293b3ea3a466450ec0c3067e06de5e5"></a> BEKEN\_SHOW\_BT\_CTRL\_INFO
:   print bt controller hci\&con info

<a id="c.BEKEN_SHOW_STACK_CMD"></a>

<a id="app__debug_8h_1a8898cf3a2db0462451d49b9510bf4a29"></a> BEKEN\_SHOW\_STACK\_CMD

<a id="c.BEKEN_DISABLE_PRINT"></a>

<a id="app__debug_8h_1aa5ecb83dd2b8e234e35947992fe55115"></a> BEKEN\_DISABLE\_PRINT
:   disable uart print,compatible with 3288/3296

<a id="c.BEKEN_APP_DBG_ANC"></a>

<a id="app__debug_8h_1af2d1ce97ef97c4b1899622e58ae8e9eb"></a> BEKEN\_APP\_DBG\_ANC
:   send anc command to app\_anc

<a id="c.BKKEN_SADC_DUMP"></a>

<a id="app__debug_8h_1a82a2aa3d958be474249d6424faf331ec"></a> BKKEN\_SADC\_DUMP
:   dump sadc data

<a id="c.BEKEN_DUMP_ENV_CMD"></a>

<a id="app__debug_8h_1ab026bc306f766f70fb73a338b2acf667"></a> BEKEN\_DUMP\_ENV\_CMD
:   dump env cfg

<a id="c.BEKEN_PRINT_LINK_KEY"></a>

<a id="app__debug_8h_1a8e1b88b58067ee46e9e76eb3f4625d73"></a> BEKEN\_PRINT\_LINK\_KEY

<a id="c.BEKEN_TRANSPARENT_HCI_CMD"></a>

<a id="app__debug_8h_1ad5b42f423bb5afe61909beb4c089eb56"></a> BEKEN\_TRANSPARENT\_HCI\_CMD
:   Transparent hci cmd to controller

<a id="c.BEKEN_SHOW_RW_KE_UESED"></a>

<a id="app__debug_8h_1ab3970749860d8f68c7c17f0fb1745796"></a> BEKEN\_SHOW\_RW\_KE\_UESED

<a id="c.BEKEN_LED_EQ_BUTTON"></a>

<a id="app__debug_8h_1a2f572db0ec6fa163be41d00f9eb12215"></a> BEKEN\_LED\_EQ\_BUTTON
:   set adc eq data and respone result by anc serivce using spp

<a id="c.BEKEN_APP_DBG_AEC"></a>

<a id="app__debug_8h_1a121cfce24aa4d632af0c83587c8e5559"></a> BEKEN\_APP\_DBG\_AEC
:   send aec command to app\_aec

<a id="c.BEKEN_SYS_SELEEP_TEST"></a>

<a id="app__debug_8h_1a469fdffd6515e782aba2969a3c70a928"></a> BEKEN\_SYS\_SELEEP\_TEST
:   let system into sleep mode

<a id="c.BEKEN_SYS_DEEP_SELEEP_TEST"></a>

<a id="app__debug_8h_1ac342180dbfd383e528a472ecec535a2e"></a> BEKEN\_SYS\_DEEP\_SELEEP\_TEST
:   let system into deepsleep mode

<a id="c.BEKEN_SYS_SHUTDOWQM_TEST"></a>

<a id="app__debug_8h_1a7f3bdbe36ae2bc7b48d3ba9040634a95"></a> BEKEN\_SYS\_SHUTDOWQM\_TEST
:   let system shutdown

<a id="c.BEKEN_SYS_PTS_TEST"></a>

<a id="app__debug_8h_1a6fa4878e1fc281001fd03d3a838cca33"></a> BEKEN\_SYS\_PTS\_TEST
:   for pts test

<a id="c.BEKEN_SYS_MIC_TEST"></a>

<a id="app__debug_8h_1abfcad8b85b8d79cdd917ec803ab60242"></a> BEKEN\_SYS\_MIC\_TEST
:   for mic test

<a id="c.BEKEN_APP_DBG_CMD"></a>

<a id="app__debug_8h_1ab884dca492d20f38ba766471d5333c7a"></a> BEKEN\_APP\_DBG\_CMD

<a id="c.OWNER_DEBUG_CMD"></a>

<a id="app__debug_8h_1ab63fc6b29aca9e24c063164dc0824cb2"></a> OWNER\_DEBUG\_CMD
:   debug cmd used to verify something right

<a id="c.BEKEN_DUT_MODE_ENABLE"></a>

<a id="app__debug_8h_1abf49fe85ba1df4b0f3f764ae873aea19"></a> BEKEN\_DUT\_MODE\_ENABLE
:   Enter Dut mode

<a id="c.BEKEN_NON_SIG_TEST_PARAM"></a>

<a id="app__debug_8h_1ad08c3da71b85c5c59650089b7b394b45"></a> BEKEN\_NON\_SIG\_TEST\_PARAM
:   RF Direct Test mode,BT Packet type Burst

<a id="c.BEKEN_READ_NON_SIG_RESULT"></a>

<a id="app__debug_8h_1a09e0173700de28b195db5fe1e1cf47ea"></a> BEKEN\_READ\_NON\_SIG\_RESULT
:   RF Direct Test mode,read test result

<a id="c.BEKEN_CLEAR_NON_SIG_RESULT"></a>

<a id="app__debug_8h_1aa118cfe1f5df749fcc946469d3948f71"></a> BEKEN\_CLEAR\_NON\_SIG\_RESULT
:   RF Direct Test mode,read test result

<a id="c.BEKEN_FCC_PARAM"></a>

<a id="app__debug_8h_1a042ceee7bc7ec129860433c48fcd761c"></a> BEKEN\_FCC\_PARAM
:   Fcc test,Ex:continue CW,EDR/BR-PN9 TX

<a id="c.BEKEN_RF_PWRUP_ADJ"></a>

<a id="app__debug_8h_1aad282c83dad29303735bed3b25fee19f"></a> BEKEN\_RF\_PWRUP\_ADJ
:   3298 RF PWR UP ADJ

<a id="c.BEKEN_CAPTURE_ADC_DATA"></a>

<a id="app__debug_8h_1a6d88fa0bd687defb51d81cbd0d1a4edf"></a> BEKEN\_CAPTURE\_ADC\_DATA
:   3298 capture adc data

<a id="c.BEKEN_CMD_DUMP_MEM"></a>

<a id="app__debug_8h_1aa4c631943c2f626296ee925733bd8c89"></a> BEKEN\_CMD\_DUMP\_MEM

<a id="c.BEKEN_CMD_READ_MEM"></a>

<a id="app__debug_8h_1ab8341d3cd55c61bafdd4ff1f00f0aedc"></a> BEKEN\_CMD\_READ\_MEM

<a id="c.BEKEN_CMD_LOG_FLUSH"></a>

<a id="app__debug_8h_1a83700950872f566d77d73eeeccec0f34"></a> BEKEN\_CMD\_LOG\_FLUSH

<a id="c.BEKEN_CMD_SWITCH_UART_TO_SWD"></a>

<a id="app__debug_8h_1a15f2975e6ac242259b165198ba59e514"></a> BEKEN\_CMD\_SWITCH\_UART\_TO\_SWD

<a id="c.BEKEN_CMD_SYS_RESET"></a>

<a id="app__debug_8h_1a7478ecf391a9eb7723e30c53d95456fb"></a> BEKEN\_CMD\_SYS\_RESET

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv412bt_test_mode"></a>

<a id="_CPPv312bt_test_mode"></a> <a id="_CPPv212bt_test_mode"></a> <a id="app__debug_8h_1a90affff9b5250b95905bafc390d45c62"></a> enum bt\_test\_mode
:   Bluetooth management mode definition.

    *Values:*

    <a id="_CPPv4N12bt_test_mode19BT_TEST_MODE_NORMALE"></a>

    <a id="_CPPv3N12bt_test_mode19BT_TEST_MODE_NORMALE"></a> <a id="_CPPv2N12bt_test_mode19BT_TEST_MODE_NORMALE"></a> <a id="app__debug_8h_1a90affff9b5250b95905bafc390d45c62af2852a39222d31c81a98da65786766a0"></a> enumerator BT\_TEST\_MODE\_NORMAL
    :   Bluetooth normal work mode

    <a id="_CPPv4N12bt_test_mode21BT_TEST_MODE_SIG_TESTE"></a>

    <a id="_CPPv3N12bt_test_mode21BT_TEST_MODE_SIG_TESTE"></a> <a id="_CPPv2N12bt_test_mode21BT_TEST_MODE_SIG_TESTE"></a> <a id="app__debug_8h_1a90affff9b5250b95905bafc390d45c62aad21dab11fd58ba6156b601eb161ad82"></a> enumerator BT\_TEST\_MODE\_SIG\_TEST
    :   Bluetooth sinal test mode

    <a id="_CPPv4N12bt_test_mode25BT_TEST_MODE_NON_SIG_TESTE"></a>

    <a id="_CPPv3N12bt_test_mode25BT_TEST_MODE_NON_SIG_TESTE"></a> <a id="_CPPv2N12bt_test_mode25BT_TEST_MODE_NON_SIG_TESTE"></a> <a id="app__debug_8h_1a90affff9b5250b95905bafc390d45c62a299d49287913f12f209962a318fd0c67"></a> enumerator BT\_TEST\_MODE\_NON\_SIG\_TEST
    :   Bluetooth non-signal test mode

    <a id="_CPPv4N12bt_test_mode21BT_TEST_MODE_FCC_TESTE"></a>

    <a id="_CPPv3N12bt_test_mode21BT_TEST_MODE_FCC_TESTE"></a> <a id="_CPPv2N12bt_test_mode21BT_TEST_MODE_FCC_TESTE"></a> <a id="app__debug_8h_1a90affff9b5250b95905bafc390d45c62a1f573b48842801d690248bf1d9c7ff76"></a> enumerator BT\_TEST\_MODE\_FCC\_TEST
    :   Bluetooth FCC test mode

    <a id="_CPPv4N12bt_test_mode16BT_TEST_MODE_BQBE"></a>

    <a id="_CPPv3N12bt_test_mode16BT_TEST_MODE_BQBE"></a> <a id="_CPPv2N12bt_test_mode16BT_TEST_MODE_BQBE"></a> <a id="app__debug_8h_1a90affff9b5250b95905bafc390d45c62a9641832bc70e936545500fad72db5db9"></a> enumerator BT\_TEST\_MODE\_BQB
    :   Bluetooth Qualified Body test mode
