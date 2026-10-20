---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/component/bk_button.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bk-button"></a>

# BK\_BUTTON

<a id="bk-button-api-status"></a>

## BK\_BUTTON API Status

| API |
| --- |
| [`bk_button_open()`](#_CPPv414bk_button_open24button_detected_callback "bk_button_open") |
| [`bk_button_close()`](#_CPPv415bk_button_closev "bk_button_close") |
| [`bk_button_set_parameter()`](#_CPPv423bk_button_set_parameterPK14button_param_t "bk_button_set_parameter") |
| [`bk_button_register_gpio()`](#_CPPv423bk_button_register_gpio8uint32_t19button_gpio_value_e "bk_button_register_gpio") |
| [`bk_button_unregister_gpio()`](#_CPPv425bk_button_unregister_gpio8uint32_t "bk_button_unregister_gpio") |

<a id="bk-button-api-reference"></a>

## BK\_BUTTON API Reference

<a id="header-file"></a>

### Header File

- [component/button/bk\_button.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/component/button/bk_button.h)

<a id="functions"></a>

### Functions

<a id="_CPPv414bk_button_open24button_detected_callback"></a>

<a id="_CPPv314bk_button_open24button_detected_callback"></a> <a id="_CPPv214bk_button_open24button_detected_callback"></a> <a id="bk_button_open__button_detected_callback"></a> <a id="bk__button_8h_1a2a8fa16b67684fef162bceeb18a7a2bd"></a> int8\_t bk\_button\_open([button\_detected\_callback](#_CPPv424button_detected_callback "button_detected_callback") cb)

<a id="_CPPv415bk_button_closev"></a>

<a id="_CPPv315bk_button_closev"></a> <a id="_CPPv215bk_button_closev"></a> <a id="bk_button_close__void"></a> <a id="bk__button_8h_1a3a09f95ab0e3e32d3c7c9449bf5c2c34"></a> int8\_t bk\_button\_close(void)

<a id="_CPPv423bk_button_set_parameterPK14button_param_t"></a>

<a id="_CPPv323bk_button_set_parameterPK14button_param_t"></a> <a id="_CPPv223bk_button_set_parameterPK14button_param_t"></a> <a id="bk_button_set_parameter__button_param_tCP"></a> <a id="bk__button_8h_1a4a49624b841c840598c049ea14b44fce"></a> void bk\_button\_set\_parameter(const [button\_param\_t](#_CPPv414button_param_t "button_param_t") \*p\_button\_param)

<a id="_CPPv423bk_button_register_gpio8uint32_t19button_gpio_value_e"></a>

<a id="_CPPv323bk_button_register_gpio8uint32_t19button_gpio_value_e"></a> <a id="_CPPv223bk_button_register_gpio8uint32_t19button_gpio_value_e"></a> <a id="bk_button_register_gpio__uint32_t.button_gpio_value_e"></a> <a id="bk__button_8h_1a78490b23323f7cfc9b65a8f45664fc25"></a> void bk\_button\_register\_gpio(uint32\_t gpio\_bitmap, [button\_gpio\_value\_e](#_CPPv419button_gpio_value_e "button_gpio_value_e") press\_value)

<a id="_CPPv425bk_button_unregister_gpio8uint32_t"></a>

<a id="_CPPv325bk_button_unregister_gpio8uint32_t"></a> <a id="_CPPv225bk_button_unregister_gpio8uint32_t"></a> <a id="bk_button_unregister_gpio__uint32_t"></a> <a id="bk__button_8h_1a47615aa9d35d4de7f6af94194bd081b4"></a> void bk\_button\_unregister\_gpio(uint32\_t gpio\_bitmap)

<a id="structures"></a>

### Structures

<a id="_CPPv414button_param_t"></a>

<a id="_CPPv314button_param_t"></a> <a id="_CPPv214button_param_t"></a> <a id="button_param_t"></a> <a id="structbutton__param__t"></a> struct button\_param\_t

<a id="_CPPv417button_gpio_cfg_t"></a>

<a id="_CPPv317button_gpio_cfg_t"></a> <a id="_CPPv217button_gpio_cfg_t"></a> <a id="button_gpio_cfg_t"></a> <a id="structbutton__gpio__cfg__t"></a> struct button\_gpio\_cfg\_t

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv424button_detected_callback"></a>

<a id="_CPPv324button_detected_callback"></a> <a id="_CPPv224button_detected_callback"></a> <a id="button_detected_callback"></a> <a id="bk__button_8h_1a93f5852ce0b92689706860a5cf405b98"></a> typedef void (\*button\_detected\_callback)(uint32\_t gpio\_pin\_id, uint8\_t button\_action)

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv419button_gpio_value_e"></a>

<a id="_CPPv319button_gpio_value_e"></a> <a id="_CPPv219button_gpio_value_e"></a> <a id="bk__button_8h_1ab7fccc12ea4cb78fa2d0e672968ff4d9"></a> enum button\_gpio\_value\_e
:   *Values:*

    <a id="_CPPv4N19button_gpio_value_e19BUTTON_GPIO_VAL_LOWE"></a>

    <a id="_CPPv3N19button_gpio_value_e19BUTTON_GPIO_VAL_LOWE"></a> <a id="_CPPv2N19button_gpio_value_e19BUTTON_GPIO_VAL_LOWE"></a> <a id="bk__button_8h_1ab7fccc12ea4cb78fa2d0e672968ff4d9a0a3b2e65b517f9c7fb9b9b408b70b564"></a> enumerator BUTTON\_GPIO\_VAL\_LOW

    <a id="_CPPv4N19button_gpio_value_e20BUTTON_GPIO_VAL_HIGHE"></a>

    <a id="_CPPv3N19button_gpio_value_e20BUTTON_GPIO_VAL_HIGHE"></a> <a id="_CPPv2N19button_gpio_value_e20BUTTON_GPIO_VAL_HIGHE"></a> <a id="bk__button_8h_1ab7fccc12ea4cb78fa2d0e672968ff4d9ac09bb1db05a383ba6e6d8a1208cfeb4b"></a> enumerator BUTTON\_GPIO\_VAL\_HIGH

<a id="_CPPv415button_action_e"></a>

<a id="_CPPv315button_action_e"></a> <a id="_CPPv215button_action_e"></a> <a id="bk__button_8h_1a3861e377ca9e0b7fdc9238c8eee9ea84"></a> enum button\_action\_e
:   *Values:*

    <a id="_CPPv4N15button_action_e18BUTTON_ACTION_NONEE"></a>

    <a id="_CPPv3N15button_action_e18BUTTON_ACTION_NONEE"></a> <a id="_CPPv2N15button_action_e18BUTTON_ACTION_NONEE"></a> <a id="bk__button_8h_1a3861e377ca9e0b7fdc9238c8eee9ea84aae4107e5c0e74c6846c04452443c8bf2"></a> enumerator BUTTON\_ACTION\_NONE

    <a id="_CPPv4N15button_action_e18BUTTON_ACTION_DOWNE"></a>

    <a id="_CPPv3N15button_action_e18BUTTON_ACTION_DOWNE"></a> <a id="_CPPv2N15button_action_e18BUTTON_ACTION_DOWNE"></a> <a id="bk__button_8h_1a3861e377ca9e0b7fdc9238c8eee9ea84a1b883586e1e9dc40875de16b1ca3ca18"></a> enumerator BUTTON\_ACTION\_DOWN

    <a id="_CPPv4N15button_action_e24BUTTON_ACTION_FIRST_DOWNE"></a>

    <a id="_CPPv3N15button_action_e24BUTTON_ACTION_FIRST_DOWNE"></a> <a id="_CPPv2N15button_action_e24BUTTON_ACTION_FIRST_DOWNE"></a> <a id="bk__button_8h_1a3861e377ca9e0b7fdc9238c8eee9ea84ab31a77d52aeeccef30ed3862c677c5d7"></a> enumerator BUTTON\_ACTION\_FIRST\_DOWN

    <a id="_CPPv4N15button_action_e28BUTTON_ACTION_CONTINUED_DOWNE"></a>

    <a id="_CPPv3N15button_action_e28BUTTON_ACTION_CONTINUED_DOWNE"></a> <a id="_CPPv2N15button_action_e28BUTTON_ACTION_CONTINUED_DOWNE"></a> <a id="bk__button_8h_1a3861e377ca9e0b7fdc9238c8eee9ea84a8ae37041afb00e28932e646535d89dc2"></a> enumerator BUTTON\_ACTION\_CONTINUED\_DOWN

    <a id="_CPPv4N15button_action_e16BUTTON_ACTION_UPE"></a>

    <a id="_CPPv3N15button_action_e16BUTTON_ACTION_UPE"></a> <a id="_CPPv2N15button_action_e16BUTTON_ACTION_UPE"></a> <a id="bk__button_8h_1a3861e377ca9e0b7fdc9238c8eee9ea84a9c2e68a11cf07abd5bdebd8be7baa8d7"></a> enumerator BUTTON\_ACTION\_UP

    <a id="_CPPv4N15button_action_e25BUTTON_ACTION_UP_AFTER_LPE"></a>

    <a id="_CPPv3N15button_action_e25BUTTON_ACTION_UP_AFTER_LPE"></a> <a id="_CPPv2N15button_action_e25BUTTON_ACTION_UP_AFTER_LPE"></a> <a id="bk__button_8h_1a3861e377ca9e0b7fdc9238c8eee9ea84a4f492b516958e1b447306ef20c5f9ba0"></a> enumerator BUTTON\_ACTION\_UP\_AFTER\_LP

    <a id="_CPPv4N15button_action_e19BUTTON_ACTION_CLICKE"></a>

    <a id="_CPPv3N15button_action_e19BUTTON_ACTION_CLICKE"></a> <a id="_CPPv2N15button_action_e19BUTTON_ACTION_CLICKE"></a> <a id="bk__button_8h_1a3861e377ca9e0b7fdc9238c8eee9ea84a16b66b48092f4259360c7bb20784fb38"></a> enumerator BUTTON\_ACTION\_CLICK

    <a id="_CPPv4N15button_action_e21BUTTON_ACTION_2_CLICKE"></a>

    <a id="_CPPv3N15button_action_e21BUTTON_ACTION_2_CLICKE"></a> <a id="_CPPv2N15button_action_e21BUTTON_ACTION_2_CLICKE"></a> <a id="bk__button_8h_1a3861e377ca9e0b7fdc9238c8eee9ea84a8f415d11ad465ceea72a7fee36837af4"></a> enumerator BUTTON\_ACTION\_2\_CLICK

    <a id="_CPPv4N15button_action_e21BUTTON_ACTION_3_CLICKE"></a>

    <a id="_CPPv3N15button_action_e21BUTTON_ACTION_3_CLICKE"></a> <a id="_CPPv2N15button_action_e21BUTTON_ACTION_3_CLICKE"></a> <a id="bk__button_8h_1a3861e377ca9e0b7fdc9238c8eee9ea84a08b29e4f9691543a9d2ed02fda5a8821"></a> enumerator BUTTON\_ACTION\_3\_CLICK

    <a id="_CPPv4N15button_action_e21BUTTON_ACTION_4_CLICKE"></a>

    <a id="_CPPv3N15button_action_e21BUTTON_ACTION_4_CLICKE"></a> <a id="_CPPv2N15button_action_e21BUTTON_ACTION_4_CLICKE"></a> <a id="bk__button_8h_1a3861e377ca9e0b7fdc9238c8eee9ea84afdb8e172df2f52d1273074e2e412ee2d"></a> enumerator BUTTON\_ACTION\_4\_CLICK

    <a id="_CPPv4N15button_action_e21BUTTON_ACTION_5_CLICKE"></a>

    <a id="_CPPv3N15button_action_e21BUTTON_ACTION_5_CLICKE"></a> <a id="_CPPv2N15button_action_e21BUTTON_ACTION_5_CLICKE"></a> <a id="bk__button_8h_1a3861e377ca9e0b7fdc9238c8eee9ea84af96f9155adaa8817b8f698550733a8c3"></a> enumerator BUTTON\_ACTION\_5\_CLICK

    <a id="_CPPv4N15button_action_e21BUTTON_ACTION_6_CLICKE"></a>

    <a id="_CPPv3N15button_action_e21BUTTON_ACTION_6_CLICKE"></a> <a id="_CPPv2N15button_action_e21BUTTON_ACTION_6_CLICKE"></a> <a id="bk__button_8h_1a3861e377ca9e0b7fdc9238c8eee9ea84a3796706b1c06c946e499393b59ad93aa"></a> enumerator BUTTON\_ACTION\_6\_CLICK

    <a id="_CPPv4N15button_action_e21BUTTON_ACTION_7_CLICKE"></a>

    <a id="_CPPv3N15button_action_e21BUTTON_ACTION_7_CLICKE"></a> <a id="_CPPv2N15button_action_e21BUTTON_ACTION_7_CLICKE"></a> <a id="bk__button_8h_1a3861e377ca9e0b7fdc9238c8eee9ea84ab6b42428dbcded45384dbe85e79b3a5d"></a> enumerator BUTTON\_ACTION\_7\_CLICK

    <a id="_CPPv4N15button_action_e21BUTTON_ACTION_8_CLICKE"></a>

    <a id="_CPPv3N15button_action_e21BUTTON_ACTION_8_CLICKE"></a> <a id="_CPPv2N15button_action_e21BUTTON_ACTION_8_CLICKE"></a> <a id="bk__button_8h_1a3861e377ca9e0b7fdc9238c8eee9ea84a9002f837b6ecc32c4a5a34d20ba6f45f"></a> enumerator BUTTON\_ACTION\_8\_CLICK

    <a id="_CPPv4N15button_action_e16BUTTON_ACTION_LPE"></a>

    <a id="_CPPv3N15button_action_e16BUTTON_ACTION_LPE"></a> <a id="_CPPv2N15button_action_e16BUTTON_ACTION_LPE"></a> <a id="bk__button_8h_1a3861e377ca9e0b7fdc9238c8eee9ea84a0b36c7a21a431f51c69753ce5e36d7c5"></a> enumerator BUTTON\_ACTION\_LP

    <a id="_CPPv4N15button_action_e19BUTTON_ACTION_LP_UPE"></a>

    <a id="_CPPv3N15button_action_e19BUTTON_ACTION_LP_UPE"></a> <a id="_CPPv2N15button_action_e19BUTTON_ACTION_LP_UPE"></a> <a id="bk__button_8h_1a3861e377ca9e0b7fdc9238c8eee9ea84a7f88f0e700923e36ec52aacb7dbbc153"></a> enumerator BUTTON\_ACTION\_LP\_UP

    <a id="_CPPv4N15button_action_e17BUTTON_ACTION_LLPE"></a>

    <a id="_CPPv3N15button_action_e17BUTTON_ACTION_LLPE"></a> <a id="_CPPv2N15button_action_e17BUTTON_ACTION_LLPE"></a> <a id="bk__button_8h_1a3861e377ca9e0b7fdc9238c8eee9ea84a2b1b08b97d6c5074ffc7909918904a3e"></a> enumerator BUTTON\_ACTION\_LLP

    <a id="_CPPv4N15button_action_e20BUTTON_ACTION_REPEATE"></a>

    <a id="_CPPv3N15button_action_e20BUTTON_ACTION_REPEATE"></a> <a id="_CPPv2N15button_action_e20BUTTON_ACTION_REPEATE"></a> <a id="bk__button_8h_1a3861e377ca9e0b7fdc9238c8eee9ea84ae99b7db7b2f6f1de514501d7c8f730c2"></a> enumerator BUTTON\_ACTION\_REPEAT

    <a id="_CPPv4N15button_action_e24BUTTON_ACTION_GROUP_DOWNE"></a>

    <a id="_CPPv3N15button_action_e24BUTTON_ACTION_GROUP_DOWNE"></a> <a id="_CPPv2N15button_action_e24BUTTON_ACTION_GROUP_DOWNE"></a> <a id="bk__button_8h_1a3861e377ca9e0b7fdc9238c8eee9ea84a110ff1a66e7ff5425d74ed2386fe967d"></a> enumerator BUTTON\_ACTION\_GROUP\_DOWN

    <a id="_CPPv4N15button_action_e26BUTTON_ACTION_GROUP_REPEATE"></a>

    <a id="_CPPv3N15button_action_e26BUTTON_ACTION_GROUP_REPEATE"></a> <a id="_CPPv2N15button_action_e26BUTTON_ACTION_GROUP_REPEATE"></a> <a id="bk__button_8h_1a3861e377ca9e0b7fdc9238c8eee9ea84a342e2212d7df8e354dad690279ef30a1"></a> enumerator BUTTON\_ACTION\_GROUP\_REPEAT

    <a id="_CPPv4N15button_action_e17BUTTON_ACTION_NUME"></a>

    <a id="_CPPv3N15button_action_e17BUTTON_ACTION_NUME"></a> <a id="_CPPv2N15button_action_e17BUTTON_ACTION_NUME"></a> <a id="bk__button_8h_1a3861e377ca9e0b7fdc9238c8eee9ea84a065ac3084762abc1d947346c1245e9fd"></a> enumerator BUTTON\_ACTION\_NUM
