---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/common/app_component/app_led.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="led-application-functions"></a>

# LED Application Functions

<a id="app-led-api-brief"></a>

## APP\_LED API Brief

| Application | Brief |
| --- | --- |
| [`app_led_init()`](#_CPPv412app_led_initv "app_led_init") | initailize LED config setting |
| [`app_led_uninit()`](#_CPPv414app_led_uninitv "app_led_uninit") | deinitailize LED config setting |
| [`app_led_push_event_action()`](#_CPPv425app_led_push_event_action13APP_LED_EVENT "app_led_push_event_action") | push LED event to app task |
| [`app_led_register_task_cb_handler()`](#_CPPv432app_led_register_task_cb_handlerv "app_led_register_task_cb_handler") | LED event task handler |

<a id="app-led-api-reference"></a>

## APP\_LED API Reference

<a id="header-file"></a>

### Header File

- [common/app\_component/app\_led.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/common/app_component/app_led.h)

<a id="functions"></a>

### Functions

<a id="_CPPv412app_led_initv"></a>

<a id="_CPPv312app_led_initv"></a> <a id="_CPPv212app_led_initv"></a> <a id="app_led_init__void"></a> <a id="app__led_8h_1aa15a7ae3c67b4ade77795b59b9c261ed"></a> void app\_led\_init(void)
:   initailize LED config setting

    initailize and loed LED config setting from env data

    返回:
    :   N/A

<a id="_CPPv414app_led_uninitv"></a>

<a id="_CPPv314app_led_uninitv"></a> <a id="_CPPv214app_led_uninitv"></a> <a id="app_led_uninit__void"></a> <a id="app__led_8h_1a64cf3be7dfd7d4ed72f1a70365b65308"></a> void app\_led\_uninit(void)
:   deinitailize LED config setting

    free LED config setting which has allocated by app\_led\_init

    返回:
    :   N/A

<a id="_CPPv425app_led_push_event_action13APP_LED_EVENT"></a>

<a id="_CPPv325app_led_push_event_action13APP_LED_EVENT"></a> <a id="_CPPv225app_led_push_event_action13APP_LED_EVENT"></a> <a id="app_led_push_event_action__APP_LED_EVENT"></a> <a id="app__led_8h_1a27df6b8784be7e96cfb1aa074e4349eb"></a> void app\_led\_push\_event\_action([APP\_LED\_EVENT](#_CPPv413APP_LED_EVENT "APP_LED_EVENT") event)
:   push LED event to app task

    push LED event to app task, wait app\_task pass it to app\_led\_register\_task\_cb\_handler

    参数:
    :   **event** – **\[in\]** LED event index

    返回:
    :   N/A

<a id="_CPPv432app_led_register_task_cb_handlerv"></a>

<a id="_CPPv332app_led_register_task_cb_handlerv"></a> <a id="_CPPv232app_led_register_task_cb_handlerv"></a> <a id="app_led_register_task_cb_handler__void"></a> <a id="app__led_8h_1a8f9c4ab7e38f04dcd5a98071b84d43bf"></a> void app\_led\_register\_task\_cb\_handler(void)
:   LED event task handler.

    a callback function hook with APP\_TASK, it handle LED action start ot stop

    返回:
    :   N/A

<a id="_CPPv433app_led_set_charger_plugin_statusb"></a>

<a id="_CPPv333app_led_set_charger_plugin_statusb"></a> <a id="_CPPv233app_led_set_charger_plugin_statusb"></a> <a id="app_led_set_charger_plugin_status__b"></a> <a id="app__led_8h_1adad21e8fa9d3fd88554d607cc6fd9aa3"></a> void app\_led\_set\_charger\_plugin\_status(bool plugin)
:   set charger plugin status

    set charger plugin status

    参数:
    :   **plugin** – **\[in\]** charger plugin

    返回:
    :   N/A

<a id="structures"></a>

### Structures

<a id="_CPPv415_app_led_info_t"></a>

<a id="_CPPv315_app_led_info_t"></a> <a id="_CPPv215_app_led_info_t"></a> <a id="_app_led_info_t"></a> <a id="struct__app__led__info__t"></a> struct \_app\_led\_info\_t
:   LED action config struct definiation.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N15_app_led_info_t5indexE"></a>

    <a id="_CPPv3N15_app_led_info_t5indexE"></a> <a id="_CPPv2N15_app_led_info_t5indexE"></a> <a id="_app_led_info_t::index__uint8_t"></a> <a id="struct__app__led__info__t_1ac9f78576cf82c9b54828ec17fa12a51c"></a> uint8\_t index
    :   LED index, LED\_LP \= 0, LED\_0 \= 1, LED\_1 \= 2, LED\_BRATH \= 3

    <a id="_CPPv4N15_app_led_info_t12number_flashE"></a>

    <a id="_CPPv3N15_app_led_info_t12number_flashE"></a> <a id="_CPPv2N15_app_led_info_t12number_flashE"></a> <a id="_app_led_info_t::number_flash__uint16_t"></a> <a id="struct__app__led__info__t_1aa05fd973abd5f20b5a1d8993a8e4d25a"></a> uint16\_t number\_flash
    :   gpio mode is flash times , pwm mode is brighter

    <a id="_CPPv4N15_app_led_info_t10led_ontimeE"></a>

    <a id="_CPPv3N15_app_led_info_t10led_ontimeE"></a> <a id="_CPPv2N15_app_led_info_t10led_ontimeE"></a> <a id="_app_led_info_t::led_ontime__uint16_t"></a> <a id="struct__app__led__info__t_1a7605241b77b452b92c1bccf7141a19ac"></a> uint16\_t led\_ontime
    :   LED on time, (unit: ms)

    <a id="_CPPv4N15_app_led_info_t11led_offtimeE"></a>

    <a id="_CPPv3N15_app_led_info_t11led_offtimeE"></a> <a id="_CPPv2N15_app_led_info_t11led_offtimeE"></a> <a id="_app_led_info_t::led_offtime__uint16_t"></a> <a id="struct__app__led__info__t_1a9d4958cb5c71a7e88e63d6232ba15b40"></a> uint16\_t led\_offtime
    :   LED off time, (unit: ms)

    <a id="_CPPv4N15_app_led_info_t6repeatE"></a>

    <a id="_CPPv3N15_app_led_info_t6repeatE"></a> <a id="_CPPv2N15_app_led_info_t6repeatE"></a> <a id="_app_led_info_t::repeat__uint16_t"></a> <a id="struct__app__led__info__t_1a32efa914c2e54148b8d26719dd5325a8"></a> uint16\_t repeat
    :   LED action repeat times

    <a id="_CPPv4N15_app_led_info_t7timeoutE"></a>

    <a id="_CPPv3N15_app_led_info_t7timeoutE"></a> <a id="_CPPv2N15_app_led_info_t7timeoutE"></a> <a id="_app_led_info_t::timeout__int32_t"></a> <a id="struct__app__led__info__t_1af0ccb386aed40d07a4dbc605679bb0a8"></a> int32\_t timeout
    :   LED action timeout(uint: ms) , 0xFFFF means never timeout, pwm mode is darken

<a id="macros"></a>

### Macros

<a id="c.LED_ON"></a>

<a id="app__led_8h_1af2e697ac60e05813d45ea2c9c9e79c25"></a> LED\_ON

<a id="c.LED_OFF"></a>

<a id="app__led_8h_1a80700bb63bd56ebabbb4728aa433fd29"></a> LED\_OFF

<a id="c.LED_NUM"></a>

<a id="app__led_8h_1a77440c4104ae0a7368936ff87a3d3260"></a> LED\_NUM
:   total numbers of LED

<a id="c.LED_EVENT_NUM"></a>

<a id="app__led_8h_1ac4057922cd4632d3b4304bad6e3b4e0b"></a> LED\_EVENT\_NUM
:   total numbers of LED event

<a id="c.LED0_INDEX"></a>

<a id="app__led_8h_1a00ea1020d32630ee5a4ebc728800d6e8"></a> LED0\_INDEX
:   LED\_0 default GPIO index

<a id="c.LED1_INDEX"></a>

<a id="app__led_8h_1a2274cd3b41e425dbf98c239be1edf882"></a> LED1\_INDEX
:   LED\_1 default GPIO index

<a id="c.LED_BR_INDEX"></a>

<a id="app__led_8h_1a84ab4469f89c1a250cec9dd328a2c75a"></a> LED\_BR\_INDEX
:   LED\_BR default GPIO index

<a id="c.LED_TMR_DUR"></a>

<a id="app__led_8h_1a93298e4849fb13223394768f8b93bb30"></a> LED\_TMR\_DUR
:   LED action event timer unit

<a id="c.LED_INVALID_INDEX"></a>

<a id="app__led_8h_1a5000229b30af4541530f4bce3201c4a1"></a> LED\_INVALID\_INDEX
:   LED invalid config value

<a id="c.LED_DEBUG"></a>

<a id="app__led_8h_1adfac3535a6d4b8cf84ea9b7091ce23a8"></a> LED\_DEBUG
:   LED debug message

<a id="c.LED_PRT"></a>

<a id="app__led_8h_1aab7a6503abfc11aecf9b7d4ad8a27f70"></a> LED\_PRT(...)

<a id="c.LED_ERR"></a>

<a id="app__led_8h_1af4c45933dba8970cba5e32b5fda3d4ea"></a> LED\_ERR(...)

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv412APP_LED_MODE"></a>

<a id="_CPPv312APP_LED_MODE"></a> <a id="_CPPv212APP_LED_MODE"></a> <a id="APP_LED_MODE"></a> <a id="app__led_8h_1a4999ecf24863938ad89445429491928d"></a> typedef uint8\_t APP\_LED\_MODE

<a id="_CPPv413APP_LED_EVENT"></a>

<a id="_CPPv313APP_LED_EVENT"></a> <a id="_CPPv213APP_LED_EVENT"></a> <a id="APP_LED_EVENT"></a> <a id="app__led_8h_1aaa282ebbb7f9cbf2f647c39d8a3194af"></a> typedef uint8\_t APP\_LED\_EVENT

<a id="_CPPv414app_led_info_t"></a>

<a id="_CPPv314app_led_info_t"></a> <a id="_CPPv214app_led_info_t"></a> <a id="app_led_info_t"></a> <a id="app__led_8h_1acc4b85dc2b4e1b7e06b602327c1ee6b4"></a> typedef struct [\_app\_led\_info\_t](#_CPPv415_app_led_info_t "_app_led_info_t") app\_led\_info\_t
:   LED action config struct definiation.

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv4Ut1_5"></a>

<a id="_CPPv3Ut1_5"></a> <a id="app__led_8h_1a61dadd085c1777f559549e05962b2c9e"></a> enum \[anonymous\]
:   led\_gpio index, “LEDIndex” in toolkit This item that is logical led index, containing leds action, will be translated to “LED\_GPIO” in toolkit finally. ex. LEDIndex\=\=LED0, means LED\_GPIO:GPIO\_x toggles repeatedly as event happens. One more case, LEDIndex\=\=BOTH, means LED\_GPIO:LED0 \&\& LED\_GPIO:LED1 both toggle repeatedly. In another view, wo could treat this index as instruction, which instruct the leds how to take action,such as LED0, instructs LED0 flash(blink), Altern does LED0 \&\& LED1 flash alternatively, LED0\_Only does LED0 flah(blink),and LED1 switch off.

    *Values:*

    <a id="_CPPv4NUt1_514LED_INDEX_LED0E"></a>

    <a id="_CPPv3NUt1_514LED_INDEX_LED0E"></a> <a id="app__led_8h_1a61dadd085c1777f559549e05962b2c9ea88a5c01f1ec0fb7aad1b1b26941aa3cd"></a> enumerator LED\_INDEX\_LED0
    :   0, action using LED\_0 and clean others

    <a id="_CPPv4NUt1_514LED_INDEX_LED1E"></a>

    <a id="_CPPv3NUt1_514LED_INDEX_LED1E"></a> <a id="app__led_8h_1a61dadd085c1777f559549e05962b2c9ea9ee173f8c168a2acfb3e6de8b222a2a3"></a> enumerator LED\_INDEX\_LED1
    :   1, action using LED\_1 and clean others

    <a id="_CPPv4NUt1_512LED_INDEX_LPE"></a>

    <a id="_CPPv3NUt1_512LED_INDEX_LPE"></a> <a id="app__led_8h_1a61dadd085c1777f559549e05962b2c9eade5bb9b49404b4d8240dbceed4905090"></a> enumerator LED\_INDEX\_LP
    :   2, action using LED\_LP and clean others

    <a id="_CPPv4NUt1_516LED_INDEX_ALTERNE"></a>

    <a id="_CPPv3NUt1_516LED_INDEX_ALTERNE"></a> <a id="app__led_8h_1a61dadd085c1777f559549e05962b2c9ead6e09c92bffc93a78f762f63e9280c5b"></a> enumerator LED\_INDEX\_ALTERN
    :   3, action using alternatively blinking

    <a id="_CPPv4NUt1_514LED_INDEX_BOTHE"></a>

    <a id="_CPPv3NUt1_514LED_INDEX_BOTHE"></a> <a id="app__led_8h_1a61dadd085c1777f559549e05962b2c9eaee899a640c9648df3f50096ac3305a65"></a> enumerator LED\_INDEX\_BOTH
    :   4, action using synchronously blinking

    <a id="_CPPv4NUt1_519LED_INDEX_LED0_ONLYE"></a>

    <a id="_CPPv3NUt1_519LED_INDEX_LED0_ONLYE"></a> <a id="app__led_8h_1a61dadd085c1777f559549e05962b2c9ea3dd2c2dfaf33f92403c66c3b7a76264c"></a> enumerator LED\_INDEX\_LED0\_ONLY
    :   5, action using LED\_0

    <a id="_CPPv4NUt1_519LED_INDEX_LED1_ONLYE"></a>

    <a id="_CPPv3NUt1_519LED_INDEX_LED1_ONLYE"></a> <a id="app__led_8h_1a61dadd085c1777f559549e05962b2c9ea5befad400d3f8e93c5414c28d57d7631"></a> enumerator LED\_INDEX\_LED1\_ONLY
    :   6, action using LED\_1

    <a id="_CPPv4NUt1_521LED_INDEX_LED_LP_ONLYE"></a>

    <a id="_CPPv3NUt1_521LED_INDEX_LED_LP_ONLYE"></a> <a id="app__led_8h_1a61dadd085c1777f559549e05962b2c9ea75bc1127e8194c692ba7afc084f2aac5"></a> enumerator LED\_INDEX\_LED\_LP\_ONLY
    :   7, action using LED\_LP

    <a id="_CPPv4NUt1_516LED_INDEX_LED_BRE"></a>

    <a id="_CPPv3NUt1_516LED_INDEX_LED_BRE"></a> <a id="app__led_8h_1a61dadd085c1777f559549e05962b2c9ea523262bdbfcdd763eb8b590f87a9332f"></a> enumerator LED\_INDEX\_LED\_BR
    :   8, action using LED pwm mode

    <a id="_CPPv4NUt1_521LED_INDEX_ALL_IN_LED0E"></a>

    <a id="_CPPv3NUt1_521LED_INDEX_ALL_IN_LED0E"></a> <a id="app__led_8h_1a61dadd085c1777f559549e05962b2c9ea428eac3de31f1f470cc956e895211b5c"></a> enumerator LED\_INDEX\_ALL\_IN\_LED0
    :   9, action force using LED\_0 instead of the original setting

    <a id="_CPPv4NUt1_521LED_INDEX_ALL_IN_LED1E"></a>

    <a id="_CPPv3NUt1_521LED_INDEX_ALL_IN_LED1E"></a> <a id="app__led_8h_1a61dadd085c1777f559549e05962b2c9ea29c80475776cf38dbb98fcbfec6bafb5"></a> enumerator LED\_INDEX\_ALL\_IN\_LED1
    :   10, action force using LED\_1 instead of the original setting

    <a id="_CPPv4NUt1_519LED_INDEX_ALL_IN_LPE"></a>

    <a id="_CPPv3NUt1_519LED_INDEX_ALL_IN_LPE"></a> <a id="app__led_8h_1a61dadd085c1777f559549e05962b2c9eacda10cae1cc9157420054c3fa95c7b71"></a> enumerator LED\_INDEX\_ALL\_IN\_LP
    :   11, action force using LED\_LP instead of the original setting

    <a id="_CPPv4NUt1_513LED_INDEX_ENDE"></a>

    <a id="_CPPv3NUt1_513LED_INDEX_ENDE"></a> <a id="app__led_8h_1a61dadd085c1777f559549e05962b2c9ea27f5fd47d9ef79c38178a970ac4b75ce"></a> enumerator LED\_INDEX\_END

<a id="_CPPv4Ut1_6"></a>

<a id="_CPPv3Ut1_6"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635"></a> enum \[anonymous\]
:   LED action event definition.

    *Values:*

    <a id="_CPPv4NUt1_621LED_EVENT_INVALID_LEDE"></a>

    <a id="_CPPv3NUt1_621LED_EVENT_INVALID_LEDE"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635a672f90665ae8b90585a267a49d0acdd6"></a> enumerator LED\_EVENT\_INVALID\_LED

    <a id="_CPPv4NUt1_625LED_EVENT_AUTO_CONNECTIONE"></a>

    <a id="_CPPv3NUt1_625LED_EVENT_AUTO_CONNECTIONE"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635a8720568ceafabe2d9fdf185e71ff04b1"></a> enumerator LED\_EVENT\_AUTO\_CONNECTION

    <a id="_CPPv4NUt1_621LED_EVENT_MATCH_STATEE"></a>

    <a id="_CPPv3NUt1_621LED_EVENT_MATCH_STATEE"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635a46250852128b920940300bf0dfe97e72"></a> enumerator LED\_EVENT\_MATCH\_STATE

    <a id="_CPPv4NUt1_632LED_EVENT_NO_MATCH_NO_CONN_STATEE"></a>

    <a id="_CPPv3NUt1_632LED_EVENT_NO_MATCH_NO_CONN_STATEE"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635a0ce8611dc5b2941052d83a6f858ef425"></a> enumerator LED\_EVENT\_NO\_MATCH\_NO\_CONN\_STATE

    <a id="_CPPv4NUt1_614LED_EVENT_CONNE"></a>

    <a id="_CPPv3NUt1_614LED_EVENT_CONNE"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635a55fa2ab7fcfd1df1748ae75ecaa76d06"></a> enumerator LED\_EVENT\_CONN

    <a id="_CPPv4NUt1_618LED_EVENT_BT_PAUSEE"></a>

    <a id="_CPPv3NUt1_618LED_EVENT_BT_PAUSEE"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635ad52d888946e64d4d0ba6413e85e6f55f"></a> enumerator LED\_EVENT\_BT\_PAUSE

    <a id="_CPPv4NUt1_617LED_EVENT_BT_PLAYE"></a>

    <a id="_CPPv3NUt1_617LED_EVENT_BT_PLAYE"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635a108bdee8ddeab29d3941f5a4b24d8290"></a> enumerator LED\_EVENT\_BT\_PLAY

    <a id="_CPPv4NUt1_626LED_EVENT_INCOMING_RINGINGE"></a>

    <a id="_CPPv3NUt1_626LED_EVENT_INCOMING_RINGINGE"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635aac7b4d4332f760e01ac99192387d39ae"></a> enumerator LED\_EVENT\_INCOMING\_RINGING

    <a id="_CPPv4NUt1_626LED_EVENT_OUTGOING_RINGINGE"></a>

    <a id="_CPPv3NUt1_626LED_EVENT_OUTGOING_RINGINGE"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635aa78dba234386a1134eeea38155cd8d5b"></a> enumerator LED\_EVENT\_OUTGOING\_RINGING

    <a id="_CPPv4NUt1_628LED_EVENT_CALL_ESTABLISHMENTE"></a>

    <a id="_CPPv3NUt1_628LED_EVENT_CALL_ESTABLISHMENTE"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635a7475871575af0f19b1b10dfed52a94d2"></a> enumerator LED\_EVENT\_CALL\_ESTABLISHMENT

    <a id="_CPPv4NUt1_621LED_EVENT_LOW_BATTERYE"></a>

    <a id="_CPPv3NUt1_621LED_EVENT_LOW_BATTERYE"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635a1b753586fa39c20a300d12184b37f015"></a> enumerator LED\_EVENT\_LOW\_BATTERY

    <a id="_CPPv4NUt1_618LED_EVENT_CHARGINGE"></a>

    <a id="_CPPv3NUt1_618LED_EVENT_CHARGINGE"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635a0fc3d23c0a5253efa4dba0f0cece586c"></a> enumerator LED\_EVENT\_CHARGING

    <a id="_CPPv4NUt1_622LED_EVENT_BATTERY_FULLE"></a>

    <a id="_CPPv3NUt1_622LED_EVENT_BATTERY_FULLE"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635a97eb975aa0e8598cba319d0890debb44"></a> enumerator LED\_EVENT\_BATTERY\_FULL

    <a id="_CPPv4NUt1_618LED_EVENT_POWER_ONE"></a>

    <a id="_CPPv3NUt1_618LED_EVENT_POWER_ONE"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635aa95421fd476761c4c02025e7d7cac82a"></a> enumerator LED\_EVENT\_POWER\_ON

    <a id="_CPPv4NUt1_619LED_EVENT_POWER_OFFE"></a>

    <a id="_CPPv3NUt1_619LED_EVENT_POWER_OFFE"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635a9b76240cb326aec4093d956c32ef4791"></a> enumerator LED\_EVENT\_POWER\_OFF

    <a id="_CPPv4NUt1_621LED_EVENT_LINEIN_PLAYE"></a>

    <a id="_CPPv3NUt1_621LED_EVENT_LINEIN_PLAYE"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635ac60583c8539f543ab9f939b979b323af"></a> enumerator LED\_EVENT\_LINEIN\_PLAY

    <a id="_CPPv4NUt1_622LED_EVENT_LINEIN_PAUSEE"></a>

    <a id="_CPPv3NUt1_622LED_EVENT_LINEIN_PAUSEE"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635a0b517cfbd1287ba8ec58443ea6f65f06"></a> enumerator LED\_EVENT\_LINEIN\_PAUSE

    <a id="_CPPv4NUt1_620LED_EVENT_MUSIC_PLAYE"></a>

    <a id="_CPPv3NUt1_620LED_EVENT_MUSIC_PLAYE"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635ac4246ef7bb1e1904e39cbb2f3617b3dc"></a> enumerator LED\_EVENT\_MUSIC\_PLAY

    <a id="_CPPv4NUt1_621LED_EVENT_MUSIC_PAUSEE"></a>

    <a id="_CPPv3NUt1_621LED_EVENT_MUSIC_PAUSEE"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635a9e38f4dfd19c758c797369aa8a904881"></a> enumerator LED\_EVENT\_MUSIC\_PAUSE

    <a id="_CPPv4NUt1_617LED_EVENT_FM_PLAYE"></a>

    <a id="_CPPv3NUt1_617LED_EVENT_FM_PLAYE"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635a66dae1e300d8346175b0cd05a2c40b56"></a> enumerator LED\_EVENT\_FM\_PLAY

    <a id="_CPPv4NUt1_618LED_EVENT_FM_PAUSEE"></a>

    <a id="_CPPv3NUt1_618LED_EVENT_FM_PAUSEE"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635aee8b28fe5d5753445f14800c97ce0552"></a> enumerator LED\_EVENT\_FM\_PAUSE

    <a id="_CPPv4NUt1_617LED_EVENT_FM_SCANE"></a>

    <a id="_CPPv3NUt1_617LED_EVENT_FM_SCANE"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635a4f1890bade47925996b2ba1f9d494327"></a> enumerator LED\_EVENT\_FM\_SCAN

    <a id="_CPPv4NUt1_619LED_EVENT_TEST_MODEE"></a>

    <a id="_CPPv3NUt1_619LED_EVENT_TEST_MODEE"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635a84de2ed4de9d13472a0146efdcb37b8f"></a> enumerator LED\_EVENT\_TEST\_MODE

    <a id="_CPPv4NUt1_626LED_EVENT_STEREO_CONN_MODEE"></a>

    <a id="_CPPv3NUt1_626LED_EVENT_STEREO_CONN_MODEE"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635a7bd606694a30bad1e7418bbf3348f924"></a> enumerator LED\_EVENT\_STEREO\_CONN\_MODE

    <a id="_CPPv4NUt1_627LED_EVENT_STEREO_MATCH_MODEE"></a>

    <a id="_CPPv3NUt1_627LED_EVENT_STEREO_MATCH_MODEE"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635acdf80fca4cd1379b0f49f169ba8e2425"></a> enumerator LED\_EVENT\_STEREO\_MATCH\_MODE

    <a id="_CPPv4NUt1_627LED_EVENT_STEREO_RECON_MODEE"></a>

    <a id="_CPPv3NUt1_627LED_EVENT_STEREO_RECON_MODEE"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635a5e0e7252d55b8f07b6fe3e88517eb38d"></a> enumerator LED\_EVENT\_STEREO\_RECON\_MODE

    <a id="_CPPv4NUt1_619LED_EVENT_RESERVED1E"></a>

    <a id="_CPPv3NUt1_619LED_EVENT_RESERVED1E"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635a9fa3acc18946f00f2e7248ca839683da"></a> enumerator LED\_EVENT\_RESERVED1

    <a id="_CPPv4NUt1_619LED_EVENT_RESERVED2E"></a>

    <a id="_CPPv3NUt1_619LED_EVENT_RESERVED2E"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635af308a533ead20d1e421748cd787a7f4d"></a> enumerator LED\_EVENT\_RESERVED2

    <a id="_CPPv4NUt1_619LED_EVENT_RESERVED3E"></a>

    <a id="_CPPv3NUt1_619LED_EVENT_RESERVED3E"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635a652ceb99d92900eab7c882780aff130e"></a> enumerator LED\_EVENT\_RESERVED3

    <a id="_CPPv4NUt1_613LED_EVENT_ENDE"></a>

    <a id="_CPPv3NUt1_613LED_EVENT_ENDE"></a> <a id="app__led_8h_1a726ca809ffd3d67ab4b8476646f26635a179b2709d1959dc6bf46a1ddb03b1b2b"></a> enumerator LED\_EVENT\_END
