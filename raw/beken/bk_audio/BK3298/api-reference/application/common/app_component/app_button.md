---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/common/app_component/app_button.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="button-application-functions"></a>

# Button Application Functions

<a id="app-button-api-brief"></a>

## APP\_BUTTON API Brief

| Application | Brief |
| --- | --- |
| [`app_button_register_task_cb_handler()`](#_CPPv435app_button_register_task_cb_handlerv "app_button_register_task_cb_handler") | application for button task callback register in app\_msg\_hdl\_dlst\_hdr queue |
| [`app_button_init()`](#_CPPv415app_button_initv "app_button_init") | application for button initialize |

<a id="app-button-api-reference"></a>

## APP\_BUTTON API Reference

<a id="header-file"></a>

### Header File

- [common/app\_component/app\_button.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/common/app_component/app_button.h)

<a id="functions"></a>

### Functions

<a id="_CPPv435app_button_register_task_cb_handlerv"></a>

<a id="_CPPv335app_button_register_task_cb_handlerv"></a> <a id="_CPPv235app_button_register_task_cb_handlerv"></a> <a id="app_button_register_task_cb_handler__void"></a> <a id="app__button_8h_1a94113eb21d608cdfc150cb9700571bdb"></a> void app\_button\_register\_task\_cb\_handler(void)
:   application for button task callback register in app\_msg\_hdl\_dlst\_hdr queue APP\_TASK will poll this queue and process button message

    返回:
    :   N/A

<a id="_CPPv415app_button_initv"></a>

<a id="_CPPv315app_button_initv"></a> <a id="_CPPv215app_button_initv"></a> <a id="app_button_init__void"></a> <a id="app__button_8h_1a92b6d4d72bd9e2d41b439bfd858b3ec9"></a> void app\_button\_init(void)
:   application for button initialize include load application environment variable into button parameter gpio pin initialize

    返回:
    :   N/A

<a id="unions"></a>

### Unions

<a id="_CPPv417_button_setting_u"></a>

<a id="_CPPv317_button_setting_u"></a> <a id="_CPPv217_button_setting_u"></a> <a id="union__button__setting__u"></a> union \_button\_setting\_u
:   *#include \<app\_button.h\>*

    button setting union variable

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N17_button_setting_u1fE"></a>

    <a id="_CPPv3N17_button_setting_u1fE"></a> <a id="_CPPv2N17_button_setting_u1fE"></a> <a id="_button_setting_u::f___button_setting_u::_button_setting_bitfields_t"></a> <a id="union__button__setting__u_1a561bd8ca764d82032a673274021dedfa"></a> struct [\_button\_setting\_u](#_CPPv417_button_setting_u "_button_setting_u")::[\_button\_setting\_bitfields\_t](#_CPPv4N17_button_setting_u27_button_setting_bitfields_tE "_button_setting_u::_button_setting_bitfields_t") f

    <a id="_CPPv4N17_button_setting_u7settingE"></a>

    <a id="_CPPv3N17_button_setting_u7settingE"></a> <a id="_CPPv2N17_button_setting_u7settingE"></a> <a id="_button_setting_u::setting__uint64_t"></a> <a id="union__button__setting__u_1a6a4c2068f496bd443bb5d443299b6d95"></a> uint64\_t setting

    <a id="_CPPv4N17_button_setting_u27_button_setting_bitfields_tE"></a>

    <a id="_CPPv3N17_button_setting_u27_button_setting_bitfields_tE"></a> <a id="_CPPv2N17_button_setting_u27_button_setting_bitfields_tE"></a> <a id="_button_setting_u::_button_setting_bitfields_t"></a> <a id="struct__button__setting__u_1_1__button__setting__bitfields__t"></a> struct \_button\_setting\_bitfields\_t
    :   <a id="breathe-section-title-public-members"></a>

        Public Members

        <a id="_CPPv4N17_button_setting_u27_button_setting_bitfields_t8gpio_pinE"></a>

        <a id="_CPPv3N17_button_setting_u27_button_setting_bitfields_t8gpio_pinE"></a> <a id="_CPPv2N17_button_setting_u27_button_setting_bitfields_t8gpio_pinE"></a> <a id="_button_setting_u::_button_setting_bitfields_t::gpio_pin__uint64_t"></a> <a id="struct__button__setting__u_1_1__button__setting__bitfields__t_1a1de60d60faa2cb56d270cc24df0e3c54"></a> uint64\_t gpio\_pin
        :   \[0 :39\] gpio pin in the GPIO/ADC/TOUCH mode

        <a id="_CPPv4N17_button_setting_u27_button_setting_bitfields_t11adc_key_cntE"></a>

        <a id="_CPPv3N17_button_setting_u27_button_setting_bitfields_t11adc_key_cntE"></a> <a id="_CPPv2N17_button_setting_u27_button_setting_bitfields_t11adc_key_cntE"></a> <a id="_button_setting_u::_button_setting_bitfields_t::adc_key_cnt__uint64_t"></a> <a id="struct__button__setting__u_1_1__button__setting__bitfields__t_1a79df9b48275342511d9b32ecae29f4ce"></a> uint64\_t adc\_key\_cnt
        :   \[40:43\] adc key count

        <a id="_CPPv4N17_button_setting_u27_button_setting_bitfields_t8reservedE"></a>

        <a id="_CPPv3N17_button_setting_u27_button_setting_bitfields_t8reservedE"></a> <a id="_CPPv2N17_button_setting_u27_button_setting_bitfields_t8reservedE"></a> <a id="_button_setting_u::_button_setting_bitfields_t::reserved__uint64_t"></a> <a id="struct__button__setting__u_1_1__button__setting__bitfields__t_1a7f9cfd8626d72d2acdb52f2d940ece9f"></a> uint64\_t reserved
        :   \[44:44\] NA

        <a id="_CPPv4N17_button_setting_u27_button_setting_bitfields_t8adc_chanE"></a>

        <a id="_CPPv3N17_button_setting_u27_button_setting_bitfields_t8adc_chanE"></a> <a id="_CPPv2N17_button_setting_u27_button_setting_bitfields_t8adc_chanE"></a> <a id="_button_setting_u::_button_setting_bitfields_t::adc_chan__uint64_t"></a> <a id="struct__button__setting__u_1_1__button__setting__bitfields__t_1aa5a4cf4179c5027e8832eab353fb21eb"></a> uint64\_t adc\_chan
        :   \[45:48\] adc channel

        <a id="_CPPv4N17_button_setting_u27_button_setting_bitfields_t11button_modeE"></a>

        <a id="_CPPv3N17_button_setting_u27_button_setting_bitfields_t11button_modeE"></a> <a id="_CPPv2N17_button_setting_u27_button_setting_bitfields_t11button_modeE"></a> <a id="_button_setting_u::_button_setting_bitfields_t::button_mode__uint64_t"></a> <a id="struct__button__setting__u_1_1__button__setting__bitfields__t_1a57d81b898132a3f172b193d7c5ba0f74"></a> uint64\_t button\_mode
        :   \[49:51\] button mode: GPIO/ ADC/ TOUCH

        <a id="_CPPv4N17_button_setting_u27_button_setting_bitfields_t11comb_buttonE"></a>

        <a id="_CPPv3N17_button_setting_u27_button_setting_bitfields_t11comb_buttonE"></a> <a id="_CPPv2N17_button_setting_u27_button_setting_bitfields_t11comb_buttonE"></a> <a id="_button_setting_u::_button_setting_bitfields_t::comb_button__uint64_t"></a> <a id="struct__button__setting__u_1_1__button__setting__bitfields__t_1a277d6b18b6e090bbb013775d638c4100"></a> uint64\_t comb\_button
        :   \[52:53\] Combination button

        <a id="_CPPv4N17_button_setting_u27_button_setting_bitfields_t11button_typeE"></a>

        <a id="_CPPv3N17_button_setting_u27_button_setting_bitfields_t11button_typeE"></a> <a id="_CPPv2N17_button_setting_u27_button_setting_bitfields_t11button_typeE"></a> <a id="_button_setting_u::_button_setting_bitfields_t::button_type__uint64_t"></a> <a id="struct__button__setting__u_1_1__button__setting__bitfields__t_1a4b445397a8fd3c50dd58dd6fc7378a10"></a> uint64\_t button\_type
        :   \[54:56\] button type:a2dp/hfp/twc/all

        <a id="_CPPv4N17_button_setting_u27_button_setting_bitfields_t13button_actionE"></a>

        <a id="_CPPv3N17_button_setting_u27_button_setting_bitfields_t13button_actionE"></a> <a id="_CPPv2N17_button_setting_u27_button_setting_bitfields_t13button_actionE"></a> <a id="_button_setting_u::_button_setting_bitfields_t::button_action__uint64_t"></a> <a id="struct__button__setting__u_1_1__button__setting__bitfields__t_1ac220578aad17a716ebacd34469aa25b9"></a> uint64\_t button\_action
        :   \[57:63\] button action

<a id="structures"></a>

### Structures

<a id="_CPPv418_app_button_para_s"></a>

<a id="_CPPv318_app_button_para_s"></a> <a id="_CPPv218_app_button_para_s"></a> <a id="_app_button_para_s"></a> <a id="struct__app__button__para__s"></a> struct \_app\_button\_para\_s
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18_app_button_para_s5pressE"></a>

    <a id="_CPPv3N18_app_button_para_s5pressE"></a> <a id="_CPPv2N18_app_button_para_s5pressE"></a> <a id="_app_button_para_s::press__uint16_t"></a> <a id="struct__app__button__para__s_1ad5c1165ad39f20a733f95cb23d8e4875"></a> uint16\_t press
    :   short pressed time length unit is millisecond

    <a id="_CPPv4N18_app_button_para_s6repeatE"></a>

    <a id="_CPPv3N18_app_button_para_s6repeatE"></a> <a id="_CPPv2N18_app_button_para_s6repeatE"></a> <a id="_app_button_para_s::repeat__uint16_t"></a> <a id="struct__app__button__para__s_1a273626c52df18d7d69f41cb05452aaf3"></a> uint16\_t repeat
    :   repeat time unit is millisecond

    <a id="_CPPv4N18_app_button_para_s5longpE"></a>

    <a id="_CPPv3N18_app_button_para_s5longpE"></a> <a id="_CPPv2N18_app_button_para_s5longpE"></a> <a id="_app_button_para_s::longp__uint16_t"></a> <a id="struct__app__button__para__s_1a3011c375071fd12864164fe2054fdc9b"></a> uint16\_t longp
    :   long pressed time length unit is millisecond

    <a id="_CPPv4N18_app_button_para_s6vlongpE"></a>

    <a id="_CPPv3N18_app_button_para_s6vlongpE"></a> <a id="_CPPv2N18_app_button_para_s6vlongpE"></a> <a id="_app_button_para_s::vlongp__uint16_t"></a> <a id="struct__app__button__para__s_1a6810bf5fe14bcdbc3bae1504bece7975"></a> uint16\_t vlongp
    :   very long pressed time length unit is millisecond

    <a id="_CPPv4N18_app_button_para_s7doublepE"></a>

    <a id="_CPPv3N18_app_button_para_s7doublepE"></a> <a id="_CPPv2N18_app_button_para_s7doublepE"></a> <a id="_app_button_para_s::doublep__uint16_t"></a> <a id="struct__app__button__para__s_1ab36ec10f8729fb11b1889ef1f01f5fd2"></a> uint16\_t doublep
    :   double click time length unit is millisecond

<a id="macros"></a>

### Macros

<a id="c.BUTTON_CLICK"></a>

<a id="app__button_8h_1a6fdb9ca3747dd2257c6d6e216d9e56e4"></a> BUTTON\_CLICK
:   ```
                              button setting bits mapping **************************************************************
    ```

    \+——————————————————————-\&#8212; ————————————————\&#8212;\+ \| 63 \~ 57 \| 56 \~ 54 \| 53 52 \| 51 \~ 49 \| 48 \~ 45 \| 44 \| 43 \~ 40 \| 39 \~ 0 \| \|———\&#8212;\+————-\&#8212;\+——\&#8212;\+———–\&#8212;\+——–\&#8212;\+-\&#8212;\+———-\&#8212;\+——————————–\&#8212;\| \| btn action \| btn type \| Combo \| Btn Mode \| if(ADC) \| Na \| if(ADC) \| if(GPIO) if(Touch) if(ADC) \| \| clk… \|a2dp/hfp/twc/all\| Button \|gpio/adc/touch\| ADC-CH \| \| adc key num \| gpio-pin Touch pin ADC pin \| \+———————————————————————————————————————-\&#8212;\+ button atcion : bit 63:57 (7bit)

<a id="c.BUTTON_DOUBLE_CLICK"></a>

<a id="app__button_8h_1a8587f5d6619d57d5ed0c36d4eeb33f6a"></a> BUTTON\_DOUBLE\_CLICK

<a id="c.BUTTON_LONG_PRESS_NO_UP"></a>

<a id="app__button_8h_1a822c94fbed18cdbc46fd454d25798911"></a> BUTTON\_LONG\_PRESS\_NO\_UP

<a id="c.BUTTON_WAIT_DOUBLE_CLICK"></a>

<a id="app__button_8h_1af40173d0387f1648aa8835f75ffef2ac"></a> BUTTON\_WAIT\_DOUBLE\_CLICK

<a id="c.BUTTON_CONTINUE"></a>

<a id="app__button_8h_1afac522d228e6cac5e2556642686ca191"></a> BUTTON\_CONTINUE

<a id="c.BUTTON_LONG_LONG_PRESS"></a>

<a id="app__button_8h_1a56aeec236022fe1c16836133548364d9"></a> BUTTON\_LONG\_LONG\_PRESS

<a id="c.BUTTON_LONG_PRESS"></a>

<a id="app__button_8h_1acc7228308bca711ea7b42fcc82dc09ce"></a> BUTTON\_LONG\_PRESS

<a id="c.BUTTON_ACTION_MASK"></a>

<a id="app__button_8h_1aa9b6a0e75bd8fc1d814b1dde8e157f18"></a> BUTTON\_ACTION\_MASK

<a id="c.BUTTON_TYPE_A2DP"></a>

<a id="app__button_8h_1ac12fc99e95f4e2a37bba1ffc5a38f658"></a> BUTTON\_TYPE\_A2DP
:   button type: bit56:54, in which context

<a id="c.BUTTON_TYPE_HFP"></a>

<a id="app__button_8h_1a5d5823b272a9e369520fc45d595e376b"></a> BUTTON\_TYPE\_HFP

<a id="c.BUTTON_TYPE_TWC"></a>

<a id="app__button_8h_1afe44d4995552a5f02ef7926bbda59335"></a> BUTTON\_TYPE\_TWC

<a id="c.BUTTON_TYPE_ALL"></a>

<a id="app__button_8h_1a6af41519d6f59f74274d89e137314d43"></a> BUTTON\_TYPE\_ALL

<a id="c.BUTTON_TYPE_MASK"></a>

<a id="app__button_8h_1aaf91651b0208e9550e8f15a2e0d6bac0"></a> BUTTON\_TYPE\_MASK

<a id="c.BUTTON_MUL_CLICK_MASK"></a>

<a id="app__button_8h_1a8af6995f6933652b4906c043eeab0858"></a> BUTTON\_MUL\_CLICK\_MASK
:   Combination buttons: bit53 \~ bit52

<a id="c.BUTTON_MUL_CLICK_FLAG"></a>

<a id="app__button_8h_1a99626983f9a3ccdd66482bb54d6cb1a5"></a> BUTTON\_MUL\_CLICK\_FLAG

<a id="c.BUTTON_THREE_CLICK_FLAG"></a>

<a id="app__button_8h_1abc14106ea92409b03671b25ce99d3763"></a> BUTTON\_THREE\_CLICK\_FLAG

<a id="c.BUTTON_FOUR_CLICK_FLAG"></a>

<a id="app__button_8h_1a16945ef6aae608795878a5829a27b240"></a> BUTTON\_FOUR\_CLICK\_FLAG

<a id="c.BUTTON_FIVE_CLICK_FLAG"></a>

<a id="app__button_8h_1a914dba2f66722d4d9bfbebfa3fe367d1"></a> BUTTON\_FIVE\_CLICK\_FLAG

<a id="c.BUTTON_SIX_CLICK_FLAG"></a>

<a id="app__button_8h_1aa61cac4b93eec268a67b35bb5211920b"></a> BUTTON\_SIX\_CLICK\_FLAG

<a id="c.BUTTON_SEVEN_CLICK_FLAG"></a>

<a id="app__button_8h_1a97a6dc86bed1d745b7c0645d82f9be82"></a> BUTTON\_SEVEN\_CLICK\_FLAG

<a id="c.BUTTON_EIGHT_CLICK_FLAG"></a>

<a id="app__button_8h_1a3d0c4d15ea758c182a658487a049d462"></a> BUTTON\_EIGHT\_CLICK\_FLAG

<a id="c.BUTTON_MODE_KEY_TYPE_MASK"></a>

<a id="app__button_8h_1a1746e0a3c8e953004950723dc6736b37"></a> BUTTON\_MODE\_KEY\_TYPE\_MASK
:   input key type: bit51:49 \= x X:0 for gpio button X:1 for adc button X:4 for touch button

<a id="c.BUTTON_MODE_KEY_TOUCH_MASK"></a>

<a id="app__button_8h_1ae9ab509c7afc644173173736ed10a96f"></a> BUTTON\_MODE\_KEY\_TOUCH\_MASK

<a id="c.BUTTON_MODE_KEY_ADC_MASK"></a>

<a id="app__button_8h_1a968725bf16c9478c6d85b6dc545bd1b8"></a> BUTTON\_MODE\_KEY\_ADC\_MASK

<a id="c.BUTTON_MAP_EXCLUDE_MASK"></a>

<a id="app__button_8h_1ad850a3934d6a84e62443b7929131da8d"></a> BUTTON\_MAP\_EXCLUDE\_MASK

<a id="c.BUTTON_MAP_MASK"></a>

<a id="app__button_8h_1a9e28cfb8d259b6dc41375172b74e0507"></a> BUTTON\_MAP\_MASK

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv416button_setting_u"></a>

<a id="_CPPv316button_setting_u"></a> <a id="_CPPv216button_setting_u"></a> <a id="button_setting_u"></a> <a id="app__button_8h_1ad9dc9f788819c42817e34a964790094e"></a> typedef union [\_button\_setting\_u](#_CPPv417_button_setting_u "_button_setting_u") button\_setting\_u
:   button setting union variable

<a id="_CPPv417app_button_para_t"></a>

<a id="_CPPv317app_button_para_t"></a> <a id="_CPPv217app_button_para_t"></a> <a id="app_button_para_t"></a> <a id="app__button_8h_1a6fcdf62f118a3a937df01944e4a7d166"></a> typedef struct [\_app\_button\_para\_s](#_CPPv418_app_button_para_s "_app_button_para_s") app\_button\_para\_t

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv4Ut1_4"></a>

<a id="_CPPv3Ut1_4"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06c"></a> enum \[anonymous\]
:   button action

    *Values:*

    <a id="_CPPv4NUt1_414BUTTON_BT_NONEE"></a>

    <a id="_CPPv3NUt1_414BUTTON_BT_NONEE"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06ca77d83be0d7c7642d8e79648f9c6515ea"></a> enumerator BUTTON\_BT\_NONE

    <a id="_CPPv4NUt1_420BUTTON_BT_PLAY_PAUSEE"></a>

    <a id="_CPPv3NUt1_420BUTTON_BT_PLAY_PAUSEE"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06ca7cfb5c053eeafefdbd85c1c35d47dcb3"></a> enumerator BUTTON\_BT\_PLAY\_PAUSE

    <a id="_CPPv4NUt1_414BUTTON_BT_NEXTE"></a>

    <a id="_CPPv3NUt1_414BUTTON_BT_NEXTE"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06cac7fa56121ebb3614086beb8c5dc8124e"></a> enumerator BUTTON\_BT\_NEXT

    <a id="_CPPv4NUt1_414BUTTON_BT_PREVE"></a>

    <a id="_CPPv3NUt1_414BUTTON_BT_PREVE"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06caca278c3e39af4cff32268ca2ec46067a"></a> enumerator BUTTON\_BT\_PREV

    <a id="_CPPv4NUt1_416BUTTON_BT_REWINDE"></a>

    <a id="_CPPv3NUt1_416BUTTON_BT_REWINDE"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06cad08c0972c457f0bca97ccae35b225fb4"></a> enumerator BUTTON\_BT\_REWIND

    <a id="_CPPv4NUt1_417BUTTON_BT_FORWARDE"></a>

    <a id="_CPPv3NUt1_417BUTTON_BT_FORWARDE"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06ca0058d2e53956fd58f0000146e36e286e"></a> enumerator BUTTON\_BT\_FORWARD

    <a id="_CPPv4NUt1_415BUTTON_BT_VOL_PE"></a>

    <a id="_CPPv3NUt1_415BUTTON_BT_VOL_PE"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06cae691495c17eb699c33d27c87d72bbf66"></a> enumerator BUTTON\_BT\_VOL\_P

    <a id="_CPPv4NUt1_415BUTTON_BT_VOL_ME"></a>

    <a id="_CPPv3NUt1_415BUTTON_BT_VOL_ME"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06ca554ea878b8906fe2d17f9f18beb95779"></a> enumerator BUTTON\_BT\_VOL\_M

    <a id="_CPPv4NUt1_418BUTTON_BT_VOL_MUTEE"></a>

    <a id="_CPPv3NUt1_418BUTTON_BT_VOL_MUTEE"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06ca24711038a8a456b2fece82e23d25105a"></a> enumerator BUTTON\_BT\_VOL\_MUTE

    <a id="_CPPv4NUt1_417BUTTON_BT_PAIRINGE"></a>

    <a id="_CPPv3NUt1_417BUTTON_BT_PAIRINGE"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06ca92ec252f864c3efd6314412e3a524dd5"></a> enumerator BUTTON\_BT\_PAIRING

    <a id="_CPPv4NUt1_419BUTTON_BT_POWERDOWNE"></a>

    <a id="_CPPv3NUt1_419BUTTON_BT_POWERDOWNE"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06cae17fba8677047ef2bcceef85dc81edd7"></a> enumerator BUTTON\_BT\_POWERDOWN

    <a id="_CPPv4NUt1_417BUTTON_BT_HFP_ACKE"></a>

    <a id="_CPPv3NUt1_417BUTTON_BT_HFP_ACKE"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06cadea32887d75b995537247dc473ea7f3b"></a> enumerator BUTTON\_BT\_HFP\_ACK

    <a id="_CPPv4NUt1_418BUTTON_BT_HFP_NACKE"></a>

    <a id="_CPPv3NUt1_418BUTTON_BT_HFP_NACKE"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06cac399e6758ce1199e7f3629d8cb784d38"></a> enumerator BUTTON\_BT\_HFP\_NACK

    <a id="_CPPv4NUt1_418BUTTON_BT_HFP_DIALE"></a>

    <a id="_CPPv3NUt1_418BUTTON_BT_HFP_DIALE"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06cae34211e8affe5b1559e93ed364414266"></a> enumerator BUTTON\_BT\_HFP\_DIAL

    <a id="_CPPv4NUt1_415BUTTON_BT_MIC_PE"></a>

    <a id="_CPPv3NUt1_415BUTTON_BT_MIC_PE"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06cab9f175b64e2ec4df47fc9d84ea816103"></a> enumerator BUTTON\_BT\_MIC\_P

    <a id="_CPPv4NUt1_415BUTTON_BT_MIC_ME"></a>

    <a id="_CPPv3NUt1_415BUTTON_BT_MIC_ME"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06caffde8c7b6c57fd12680b18bc1146a2d8"></a> enumerator BUTTON\_BT\_MIC\_M

    <a id="_CPPv4NUt1_418BUTTON_BT_MIC_MUTEE"></a>

    <a id="_CPPv3NUt1_418BUTTON_BT_MIC_MUTEE"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06cac076e5f62fd041757c3d89452a58f910"></a> enumerator BUTTON\_BT\_MIC\_MUTE

    <a id="_CPPv4NUt1_425BUTTON_BT_VOICE_DIAL_INITE"></a>

    <a id="_CPPv3NUt1_425BUTTON_BT_VOICE_DIAL_INITE"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06ca802022482c1cc7b3769e76bd55d4440b"></a> enumerator BUTTON\_BT\_VOICE\_DIAL\_INIT

    <a id="_CPPv4NUt1_425BUTTON_BT_TRANSFER_TOGGLEE"></a>

    <a id="_CPPv3NUt1_425BUTTON_BT_TRANSFER_TOGGLEE"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06cab55649a36c6f189cfe8c7d853d54f9b6"></a> enumerator BUTTON\_BT\_TRANSFER\_TOGGLE

    <a id="_CPPv4NUt1_422BUTTON_BT_CONN_DISCONNE"></a>

    <a id="_CPPv3NUt1_422BUTTON_BT_CONN_DISCONNE"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06cab4c494b12a30caecf37ed58ffe9dd101"></a> enumerator BUTTON\_BT\_CONN\_DISCONN

    <a id="_CPPv4NUt1_419BUTTON_BT_RESERVED4E"></a>

    <a id="_CPPv3NUt1_419BUTTON_BT_RESERVED4E"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06cafa8e32307f2bb488e10d4e134dbd7a7f"></a> enumerator BUTTON\_BT\_RESERVED4

    <a id="_CPPv4NUt1_425BUTTON_BT_RESTORE_FACTORYE"></a>

    <a id="_CPPv3NUt1_425BUTTON_BT_RESTORE_FACTORYE"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06cac01e7c288d3a593544e58e43da79cc95"></a> enumerator BUTTON\_BT\_RESTORE\_FACTORY

    <a id="_CPPv4NUt1_419BUTTON_BT_TEST_MODEE"></a>

    <a id="_CPPv3NUt1_419BUTTON_BT_TEST_MODEE"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06cacaf8446efabc0ee1579528af9b3c9d0e"></a> enumerator BUTTON\_BT\_TEST\_MODE

    <a id="_CPPv4NUt1_426BUTTON_BT_HINT_LANG_CHANGEE"></a>

    <a id="_CPPv3NUt1_426BUTTON_BT_HINT_LANG_CHANGEE"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06ca045b633d88aa71ce9a0a18e054b27afd"></a> enumerator BUTTON\_BT\_HINT\_LANG\_CHANGE

    <a id="_CPPv4NUt1_420BUTTON_BT_ANC_SWITCHE"></a>

    <a id="_CPPv3NUt1_420BUTTON_BT_ANC_SWITCHE"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06ca71426adccd566f8d17fc06844a3617fb"></a> enumerator BUTTON\_BT\_ANC\_SWITCH

    <a id="_CPPv4NUt1_419BUTTON_BT_RECONNECTE"></a>

    <a id="_CPPv3NUt1_419BUTTON_BT_RECONNECTE"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06cae57700130dfdf13b18205db522d04f21"></a> enumerator BUTTON\_BT\_RECONNECT
    :   25

    <a id="_CPPv4NUt1_428BUTTON_BT_AURACAST_SRC_STARTE"></a>

    <a id="_CPPv3NUt1_428BUTTON_BT_AURACAST_SRC_STARTE"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06cadd613a19ddc642483745d6558f38707c"></a> enumerator BUTTON\_BT\_AURACAST\_SRC\_START
    :   26

    <a id="_CPPv4NUt1_426BUTTON_BT_AURACAST_SRC_ENDE"></a>

    <a id="_CPPv3NUt1_426BUTTON_BT_AURACAST_SRC_ENDE"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06ca3c833560fda36d0133e51b3db396dbfe"></a> enumerator BUTTON\_BT\_AURACAST\_SRC\_END
    :   27

    <a id="_CPPv4NUt1_423BUTTON_BT_2PHONES_SWTCHE"></a>

    <a id="_CPPv3NUt1_423BUTTON_BT_2PHONES_SWTCHE"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06cae5d623b8bd349360a178b3c5999c9a8b"></a> enumerator BUTTON\_BT\_2PHONES\_SWTCH
    :   28

    <a id="_CPPv4NUt1_419BUTTON_BT_GAME_MODEE"></a>

    <a id="_CPPv3NUt1_419BUTTON_BT_GAME_MODEE"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06ca2caeed4ade397bc8b50b689a753ca3c1"></a> enumerator BUTTON\_BT\_GAME\_MODE
    :   29

    <a id="_CPPv4NUt1_419BUTTON_BT_RESERVED1E"></a>

    <a id="_CPPv3NUt1_419BUTTON_BT_RESERVED1E"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06ca1e7512e3461914a7124dbb1109417257"></a> enumerator BUTTON\_BT\_RESERVED1
    :   30

    <a id="_CPPv4NUt1_419BUTTON_BT_RESERVED2E"></a>

    <a id="_CPPv3NUt1_419BUTTON_BT_RESERVED2E"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06cac9da5c753e9bb26b971a3574462acdf9"></a> enumerator BUTTON\_BT\_RESERVED2
    :   31

    <a id="_CPPv4NUt1_419BUTTON_BT_RESERVED3E"></a>

    <a id="_CPPv3NUt1_419BUTTON_BT_RESERVED3E"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06ca7a04b38ddde66cab9397d9e5304a39e6"></a> enumerator BUTTON\_BT\_RESERVED3
    :   32

    <a id="_CPPv4NUt1_413BUTTON_BT_ENDE"></a>

    <a id="_CPPv3NUt1_413BUTTON_BT_ENDE"></a> <a id="app__button_8h_1adc29c2ff13d900c2f185ee95427fb06cab81fd5b19bc48cc56d21dd80b4d57d43"></a> enumerator BUTTON\_BT\_END
