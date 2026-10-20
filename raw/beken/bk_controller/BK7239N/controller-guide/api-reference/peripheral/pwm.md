---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/controller-guide/api-reference/peripheral/pwm.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="pwm-api"></a>

# PWM API

PWM (Pulse Width Modulation) 脉宽调制API接口。

<a id="header-file"></a>

## Header File

- [pwm.h](https://github.com/bekencorp/armino/blob/main/components/pwm.h)

<a id="functions"></a>

## Functions

<a id="_CPPv418bk_pwm_driver_initv"></a>

<a id="_CPPv318bk_pwm_driver_initv"></a> <a id="_CPPv218bk_pwm_driver_initv"></a> <a id="bk_pwm_driver_init__void"></a> <a id="group__bk__api__pwm_1gadb3ef9a0e49ce3d96b68298f66803993"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pwm\_driver\_init(void)
:   Init the PWM driver.

    This API init the resoure common to all PWM channels:

    - Init PWM driver control memory
    - Configure PWM common clock to 26M

    This API should be called before any other PWM APIs.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv420bk_pwm_driver_deinitv"></a>

<a id="_CPPv320bk_pwm_driver_deinitv"></a> <a id="_CPPv220bk_pwm_driver_deinitv"></a> <a id="bk_pwm_driver_deinit__void"></a> <a id="group__bk__api__pwm_1ga06b5d6366210b50610c2f6d30e208d71"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pwm\_driver\_deinit(void)
:   Deinit the PWM driver.

    This API free all resource related to PWM and power down all PWM channels.

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv411bk_pwm_init10pwm_chan_tPK17pwm_init_config_t"></a>

<a id="_CPPv311bk_pwm_init10pwm_chan_tPK17pwm_init_config_t"></a> <a id="_CPPv211bk_pwm_init10pwm_chan_tPK17pwm_init_config_t"></a> <a id="bk_pwm_init__pwm_chan_t.pwm_init_config_tCP"></a> <a id="group__bk__api__pwm_1ga914e2099ce92d433b1a6c76ade4d0f5a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pwm\_init(pwm\_chan\_t chan, const pwm\_init\_config\_t \*config)
:   Init the PWM channel.

    This API init the PWM channel:

    - Power up the PWM channel
    - Configure the PWM channel clock to 26M
    - Map the PWM channel to dedicated GPIO port
    - Set the period and duty cycle.

    For duty/cycle relationship, refer to [bk\_pwm\_set\_period\_duty()](#group__bk__api__pwm_1ga45326f56e267f9deb61f8b45c459b44a)

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_PWM\_NOT\_INIT: PWM driver not init
        - BK\_ERR\_NULL\_PARAM: config is NULL
        - BK\_ERR\_PWM\_CHAN\_ID: invalid PWM channel
        - BK\_ERR\_PWM\_PERIOD\_DUTY: PWM duty/period relationship is invalid
        - others: other errors.

<a id="_CPPv413bk_pwm_deinit10pwm_chan_t"></a>

<a id="_CPPv313bk_pwm_deinit10pwm_chan_t"></a> <a id="_CPPv213bk_pwm_deinit10pwm_chan_t"></a> <a id="bk_pwm_deinit__pwm_chan_t"></a> <a id="group__bk__api__pwm_1ga2becd6367591a52bb4938b9297a116ef"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pwm\_deinit(pwm\_chan\_t chan)
:   Deinit a PWM channel.

    This API deinit the PWM channel:

    - Stop the PWM channel
    - Reset all configuration of PWM channel to default value
    - Power down the PWM channel

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv412bk_pwm_start10pwm_chan_t"></a>

<a id="_CPPv312bk_pwm_start10pwm_chan_t"></a> <a id="_CPPv212bk_pwm_start10pwm_chan_t"></a> <a id="bk_pwm_start__pwm_chan_t"></a> <a id="group__bk__api__pwm_1gad7adc69069f8645766d1056d7ff2f919"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pwm\_start(pwm\_chan\_t chan)
:   Stop a PWM channel.

    This API init the resoure common to all PWM channels:

    - Init PWM driver control memory
    - Configure PWM common clock to 26M

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv411bk_pwm_stop10pwm_chan_t"></a>

<a id="_CPPv311bk_pwm_stop10pwm_chan_t"></a> <a id="_CPPv211bk_pwm_stop10pwm_chan_t"></a> <a id="bk_pwm_stop__pwm_chan_t"></a> <a id="group__bk__api__pwm_1gad88155b2ed4b16afc638696ee389c995"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pwm\_stop(pwm\_chan\_t chan)
:   Stop a PWM channel.

    This API init the resoure common to all PWM channels:

    - Init PWM driver control memory
    - Configure PWM common clock to 26M

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv422bk_pwm_set_period_duty10pwm_chan_tP24pwm_period_duty_config_t"></a>

<a id="_CPPv322bk_pwm_set_period_duty10pwm_chan_tP24pwm_period_duty_config_t"></a> <a id="_CPPv222bk_pwm_set_period_duty10pwm_chan_tP24pwm_period_duty_config_t"></a> <a id="bk_pwm_set_period_duty__pwm_chan_t.pwm_period_duty_config_tP"></a> <a id="group__bk__api__pwm_1ga45326f56e267f9deb61f8b45c459b44a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pwm\_set\_period\_duty(pwm\_chan\_t chan, pwm\_period\_duty\_config\_t \*config)
:   Configure the PWM period and duty cycle.

    This API is used to configure the period and duty time. The unit is cycle of PWM channel clock, since the PWM channel clock is default to 26M, the unit is 1/26M (1/26 000 000\) seconds.

    The beken chip supports up to 3 duties, the exact duty numbers depends on the target type.

    EXample1 \- the simplest case::

    ```
    Clock cycle = 1/26M
    Initial signal is High
    duty_cycle = D1 = 3
    duty2_cycle = 0
    duty3_cycle = 0
    period_cycle = 3 + 2 = 5

                      |<-C->|
                       __    __    __    __    __    __    __    __    __    __    __    __
    Clock Signal:   __|  |__|  |__|  |__|  |__|  |__|  |__|  |__|  |__|  |__|  |__|  |__|  |__
                      __________________             _________________             ___________
    PWM Signal:    __|                  |___________|                 |___________|

    Duty1:           |<------- D1 ----->|

    Period:          |<---------- Period1 --------->|<------ Period2 ------------>|
    ```

    Example2 \- 3 duty with initial signal high::

    ```
    Clock cycle = 1/26M
    Duty_cycle = D1 = 1
    Duty2_cycle = D2 = 2
    Duty3_cycle = D3 = 3
    period_cycle = D1 + D2 + D3 = 6

                      |<-C->|
                       __    __    __    __    __    __    __    __    __    __    __    __    __
    Clock Signal:   __|  |__|  |__|  |__|  |__|  |__|  |__|  |__|  |__|  |__|  |__|  |__|  |__|
                      ______             _________________ _____             _________________
    PWM Signal:    __|      |___________|                 |     |___________|                 |__

    Duty1:           |<-D1->|<----D2--->|<------D3------->|

    Period:          |<--------------- Period1 ---------->|<------------ Period2 ------------>|
    ```

    Example3 \- 3 duty with initial signal low::

    ```
    Clock cycle = 1/26M
    Duty_cycle = D1 = 1
    Duty2_cycle = D2 = 2
    Duty3_cycle = D3 = 3
    period_cycle = D1 + D2 + D3 = 6

                      |<-C->|
                       __    __    __    __    __    __    __    __    __    __    __    __    __
    Clock Signal:   __|  |__|  |__|  |__|  |__|  |__|  |__|  |__|  |__|  |__|  |__|  |__|  |__|
                    __       ___________                         ___________
    PWM Signal:       |_____|           |_________________|_____|           |_________________|__

    Duty1:           |<-D1->|<----D2--->|<------D3------->|

    Period:          |<--------------- Period1 ---------->|<------------ Period2 -------------|
    ```

    Example4 \- 3 duty with initial signal low and period \> (D1 \+ D2 \+ D3)::

    ```
    Clock cycle = 1/26M
    Duty_cycle = D1 = 1
    Duty2_cycle = D2 = 2
    Duty3_cycle = D3 = 3
    period_cycle = D1 + D2 + D3 + 1 = 7

                      |<-C->|
                       __    __    __    __    __    __    __    __    __    __    __    __    __
    Clock Signal:   __|  |__|  |__|  |__|  |__|  |__|  |__|  |__|  |__|  |__|  |__|  |__|  |__|
                    __       ___________                   _____       ___________
    PWM Signal:       |_____|           |_________________|     |_____|           |______________

    Duty1:           |<-D1->|<----D2--->|<------D3------->|

    Period:          |<--------------- Period ----------------->|
    ```

    **Attention**
    :   1\. The period should great or equal to (D1 \+ D2 \+ D3)

    **Attention**
    :   2\. If the duty Dx is 0, then Dx\+1 to D3 should also be 0\. If D1 is 0, it indicates the duty ratio is 0% and the signal is always low.

    **Attention**
    :   3\. If D1 equals period, it indicates the duty ratio is 100% and the signal is always high.

    **Attention**
    :   4\. The signal strengh between two successive duties is opposite, e.g. if signal of D1 is high, then signal of D2 is low.

    **Attention**
    :   5\. The initial signal is the signal strengh of D1 if D1 is not 0\.

    **Attention**
    :   6\. The duty/period configuration is very flexible, different configurations may have same result.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NULL\_PARAM: config is NULL
        - BK\_ERR\_PWM\_CHAN\_NOT\_INIT: PWM channel not init
        - BK\_ERR\_PWM\_CHAN\_ID: invalid PWM channel
        - BK\_ERR\_PWM\_PERIOD\_DUTY: PWM duty/period relationship is invalid
        - others: other errors.

<a id="_CPPv426bk_pwm_set_init_signal_low10pwm_chan_t"></a>

<a id="_CPPv326bk_pwm_set_init_signal_low10pwm_chan_t"></a> <a id="_CPPv226bk_pwm_set_init_signal_low10pwm_chan_t"></a> <a id="bk_pwm_set_init_signal_low__pwm_chan_t"></a> <a id="group__bk__api__pwm_1ga6210cfbd8239cde480100268d3d6eb2d"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pwm\_set\_init\_signal\_low(pwm\_chan\_t chan)
:   Set the initial signal to low.

    Set the initial signal level of the first duty which is indicated by duty\_cycle.

    **Attention**
    :   The signal will always be high if the duty\_cycle equals period cycle (duty ratio is 100%), regardless whether this API is called or NOT.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_PWM\_CHAN\_NOT\_INIT: PWM channel not init
        - BK\_ERR\_PWM\_CHAN\_ID: invalid PWM channel
        - others: other errors.

<a id="_CPPv427bk_pwm_set_init_signal_high10pwm_chan_t"></a>

<a id="_CPPv327bk_pwm_set_init_signal_high10pwm_chan_t"></a> <a id="_CPPv227bk_pwm_set_init_signal_high10pwm_chan_t"></a> <a id="bk_pwm_set_init_signal_high__pwm_chan_t"></a> <a id="group__bk__api__pwm_1gac1e4ba10c716f1d8bd68cf45bf14170b"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pwm\_set\_init\_signal\_high(pwm\_chan\_t chan)
:   Set the initial signal to high.

    Set the initial signal level of the first duty which is indicated by duty\_cycle.

    **Attention**
    :   The signal will always be low if the duty\_cycle is 0 (duty ratio is 0%), regardless whether this API is called or NOT.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_PWM\_CHAN\_NOT\_INIT: PWM channel not init
        - BK\_ERR\_PWM\_CHAN\_ID: invalid PWM channel
        - others: other errors.

<a id="_CPPv419bk_pwm_register_isr10pwm_chan_t9pwm_isr_t"></a>

<a id="_CPPv319bk_pwm_register_isr10pwm_chan_t9pwm_isr_t"></a> <a id="_CPPv219bk_pwm_register_isr10pwm_chan_t9pwm_isr_t"></a> <a id="bk_pwm_register_isr__pwm_chan_t.pwm_isr_t"></a> <a id="group__bk__api__pwm_1gad668632575533971376f69f2babbf5c2"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pwm\_register\_isr(pwm\_chan\_t chan, pwm\_isr\_t isr)
:   Register the interrupt service routine for PWM channel.

    **Attention**
    :   1\. Both [bk\_pwm\_capture\_init()](#group__bk__api__pwm_1gab70684dbb531cabcd790bcf5cfe6d074) and this API can set the ISR, the one called later makes sense.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_PWM\_NOT\_INIT: PWM driver not init
        - BK\_ERR\_PWM\_CHAN\_ID: invalid PWM channel
        - others: other errors.

<a id="_CPPv423bk_pwm_enable_interrupt10pwm_chan_t"></a>

<a id="_CPPv323bk_pwm_enable_interrupt10pwm_chan_t"></a> <a id="_CPPv223bk_pwm_enable_interrupt10pwm_chan_t"></a> <a id="bk_pwm_enable_interrupt__pwm_chan_t"></a> <a id="group__bk__api__pwm_1ga2b5f618eada64568c0855e6236e91a40"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pwm\_enable\_interrupt(pwm\_chan\_t chan)
:   Enable interrupt of PWM channel.

    The PWM channel interrupt is disabled by default when starting the channel by [bk\_pwm\_start()](#group__bk__api__pwm_1gad7adc69069f8645766d1056d7ff2f919) or [bk\_pwm\_group\_start()](#group__bk__api__pwm_1gaf87327843711c56cab915f02b42a602a), while it’s enabled by default when starting the channel by [bk\_pwm\_capture\_start()](#group__bk__api__pwm_1gaa8d1d9cee6831f6f03360a2fa3d3915a).

    This API is designed mainly for debug purpose, we can use it to enable the interrupt of any PWM channel, regardless of whether the channel is started by [bk\_pwm\_start()](#group__bk__api__pwm_1gad7adc69069f8645766d1056d7ff2f919) or [bk\_pwm\_group\_start()](#group__bk__api__pwm_1gaf87327843711c56cab915f02b42a602a) or [bk\_pwm\_capture\_start()](#group__bk__api__pwm_1gaa8d1d9cee6831f6f03360a2fa3d3915a).

    The [bk\_pwm\_stop()](#group__bk__api__pwm_1gad88155b2ed4b16afc638696ee389c995) and [bk\_pwm\_group\_stop()](#group__bk__api__pwm_1gae78db60193a534fa44665e4397c4d3c9) also disable the interrupt, but the [bk\_pwm\_start()](#group__bk__api__pwm_1gad7adc69069f8645766d1056d7ff2f919) and bk\_pwm\_group\_start will not enable the interrupt. So if the channel interrupt is enabled, and then stop and start the channel, we need to call this API to re-enable the interrupt.

    **Attention**
    :   1\. The interrupt can be enabled only after PWM channel is started by [bk\_pwm\_start()](#group__bk__api__pwm_1gad7adc69069f8645766d1056d7ff2f919).

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_PWM\_NOT\_INIT: PWM driver not init
        - BK\_ERR\_PWM\_CHAN\_ID: invalid PWM channel
        - BK\_ERR\_PWM\_CHAN\_NOT\_START: PWM channel is not started
        - others: other errors.

<a id="_CPPv424bk_pwm_disable_interrupt10pwm_chan_t"></a>

<a id="_CPPv324bk_pwm_disable_interrupt10pwm_chan_t"></a> <a id="_CPPv224bk_pwm_disable_interrupt10pwm_chan_t"></a> <a id="bk_pwm_disable_interrupt__pwm_chan_t"></a> <a id="group__bk__api__pwm_1gab330fccd473ffc2b1431e06c6179127e"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pwm\_disable\_interrupt(pwm\_chan\_t chan)
:   Disable interrupt of PWM channel.

    Stop the interrupt of any PWM channel, regardless whether the channel is in PWM mode, or PWM capture mode, or PWM group mode.

    **Attention**
    :   1\. [bk\_pwm\_capture\_start()](#group__bk__api__pwm_1gaa8d1d9cee6831f6f03360a2fa3d3915a) will enable the interrupt anyway, so if we want to disable the interrupt of PWM capture channel, we need to call this API anytime [bk\_pwm\_capture\_start()](#group__bk__api__pwm_1gaa8d1d9cee6831f6f03360a2fa3d3915a) is called.

    参数
    :   **chan** – the channel ID

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_PWM\_NOT\_INIT: PWM driver not init
        - BK\_ERR\_PWM\_CHAN\_ID: invalid PWM channel
        - others: other errors.

<a id="_CPPv417bk_pwm_group_initPK23pwm_group_init_config_tP11pwm_group_t"></a>

<a id="_CPPv317bk_pwm_group_initPK23pwm_group_init_config_tP11pwm_group_t"></a> <a id="_CPPv217bk_pwm_group_initPK23pwm_group_init_config_tP11pwm_group_t"></a> <a id="bk_pwm_group_init__pwm_group_init_config_tCP.pwm_group_tP"></a> <a id="group__bk__api__pwm_1gab3f68971d07e8e7f589b57f1eda510e7"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pwm\_group\_init(const pwm\_group\_init\_config\_t \*config, pwm\_group\_t \*group)
:   Init the PWM group.

    This API init the PWM group. The PWM group is a channel pair that has following attributes:

    - The period is same
    - The initial signal level is opposite
    - Start and stop at the same time

    Below is a picture to demonstrate the relationship between duty and period::

    ```
                 |<------------------------ period_cycle ---------------------------->|
                 |<--chan1_duty_cycle -->|<- D1 --|<--- chan2_duty_cycle --->|<- D2 ->|
                  _______________________
     channe1 1   |                       |____________________________________________|
                                                   __________________________
     channel 2   |________________________________|                          |________|
    ```

    The D1/D2 indicates the dead time cycle, it’s calculated based on following formula: D1 \= D2 \= (period \- chan1\_duty\_cycle \- chan2\_duty\_cycle)/2

    **Attention**
    :   1\. This API doesn’t check whether the PWM channel is already used in other mode. e.g. If the API doesn’t returns error if config-\>chan1 is already used in capture mode, the application need to make sure the channel configured in the group is not used for other purpose.

    **Attention**
    :   2\. The chan2\_duty\_cycle is actually the 2nd signal wave for channel 2, as depicted in above picture.

    **Attention**
    :   3\. This API supports to group any two available channel into a PWM group, however, we recommend to group 0/1, 2/3, 4/5 into a group, because hardware can support these group directly and we can start the channels in the group at exactly same time.

    **Attention**
    :   4\. The chan1\_duty\_cycle and chan2\_duty\_cycle should be great than 0\.

    参数
    :   - **config** – configuration of PWM group
        - **group** – store the group ID if the API is succeed.

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_PWM\_NOT\_INIT: PWM driver not init
        - BK\_ERR\_NULL\_PARAM: config or group is NULL
        - BK\_ERR\_PWM\_CHAN\_ID: channel 1 or 2 in the group is invalid
        - BK\_ERR\_PWM\_GROUP\_SAME\_CHAN: channel 1 and 2 are same
        - BK\_ERR\_PWM\_GROUP\_EXIST: a group with channel 1 and 2 is already exists
        - BK\_ERR\_PWM\_GROUP\_CHAN\_USED: a existing group has a channel equals to channel 1 or 2
        - BK\_ERR\_PWM\_GROUP\_DUTY: period cycle \< (chan1\_duty\_cycle \+ chan2\_duty\_cycle)
        - BK\_ERR\_PWM\_PERIOD\_DUTY: PWM duty/period relationship is invalid
        - others: other errors.

<a id="_CPPv419bk_pwm_group_deinit11pwm_group_t"></a>

<a id="_CPPv319bk_pwm_group_deinit11pwm_group_t"></a> <a id="_CPPv219bk_pwm_group_deinit11pwm_group_t"></a> <a id="bk_pwm_group_deinit__pwm_group_t"></a> <a id="group__bk__api__pwm_1gaa774c10fdd0ae71899c60f91e71f6b54"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pwm\_group\_deinit(pwm\_group\_t group)
:   Deinit a PWM group.

    This API stops and powers down channels in a PWM group.

    **Attention**
    :   This API returns BK\_OK directly if the group doesn’t exist.

    参数
    :   **group** – the group ID returned bk [bk\_pwm\_group\_init()](#group__bk__api__pwm_1gab3f68971d07e8e7f589b57f1eda510e7)

    返回
    :   - BK\_OK: succeed
        - others: other errors.

<a id="_CPPv423bk_pwm_group_set_config11pwm_group_tPK18pwm_group_config_t"></a>

<a id="_CPPv323bk_pwm_group_set_config11pwm_group_tPK18pwm_group_config_t"></a> <a id="_CPPv223bk_pwm_group_set_config11pwm_group_tPK18pwm_group_config_t"></a> <a id="bk_pwm_group_set_config__pwm_group_t.pwm_group_config_tCP"></a> <a id="group__bk__api__pwm_1ga19fda5d66250886025881f6dd020c94c"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pwm\_group\_set\_config(pwm\_group\_t group, const pwm\_group\_config\_t \*config)
:   Configure the PWM group.

    Configure the duty and period of a PWM group, for duty/period relationship refer to [bk\_pwm\_group\_init()](#group__bk__api__pwm_1gab3f68971d07e8e7f589b57f1eda510e7).

    **Attention**
    :   The configuration can’t take effect until the current period is ended

    参数
    :   - **group** – the group ID to be configured
        - **config** – configuration of PWM group

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_NULL\_PARAM: config or group is NULL
        - BK\_ERR\_PWM\_GROUP\_NOT\_EXIST: the group doesn’t exist
        - BK\_ERR\_PWM\_GROUP\_DUTY: period cycle \< (chan1\_duty\_cycle \+ chan2\_duty\_cycle)
        - BK\_ERR\_PWM\_PERIOD\_DUTY: PWM duty/period relationship is invalid
        - others: other errors.

<a id="_CPPv418bk_pwm_group_start11pwm_group_t"></a>

<a id="_CPPv318bk_pwm_group_start11pwm_group_t"></a> <a id="_CPPv218bk_pwm_group_start11pwm_group_t"></a> <a id="bk_pwm_group_start__pwm_group_t"></a> <a id="group__bk__api__pwm_1gaf87327843711c56cab915f02b42a602a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pwm\_group\_start(pwm\_group\_t group)
:   Start the PWM group.

    参数
    :   **group** – the group ID to be started

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_PWM\_GROUP\_NOT\_EXIST: the group doesn’t exist
        - others: other errors.

<a id="_CPPv417bk_pwm_group_stop11pwm_group_t"></a>

<a id="_CPPv317bk_pwm_group_stop11pwm_group_t"></a> <a id="_CPPv217bk_pwm_group_stop11pwm_group_t"></a> <a id="bk_pwm_group_stop__pwm_group_t"></a> <a id="group__bk__api__pwm_1gae78db60193a534fa44665e4397c4d3c9"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pwm\_group\_stop(pwm\_group\_t group)
:   Stop the PWM group.

    参数
    :   **group** – the group ID to be stopped

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_PWM\_GROUP\_NOT\_EXIST: the group doesn’t exist
        - others: other errors.

<a id="_CPPv419bk_pwm_capture_init10pwm_chan_tPK25pwm_capture_init_config_t"></a>

<a id="_CPPv319bk_pwm_capture_init10pwm_chan_tPK25pwm_capture_init_config_t"></a> <a id="_CPPv219bk_pwm_capture_init10pwm_chan_tPK25pwm_capture_init_config_t"></a> <a id="bk_pwm_capture_init__pwm_chan_t.pwm_capture_init_config_tCP"></a> <a id="group__bk__api__pwm_1gab70684dbb531cabcd790bcf5cfe6d074"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pwm\_capture\_init(pwm\_chan\_t chan, const pwm\_capture\_init\_config\_t \*config)
:   Init the PWM capture.

    The PWM capture can calculate the cycles between two different edges, currently we support following mode:

    1. PWM\_CAPTURE\_POS \- calcualte cycles between two pos-edge, the interrupt trigger in post edge
    2. PWM\_CAPTURE\_NEG \- calcualte cycles between two neg-edge, the interrupt trigger in neg edge
    3. PWM\_CAPTURE\_EDGE \- calculate cycles between two edge (pos or neg), the interrupt trigger in post or neg edge.

    Example 1 \- init the capture in PWM\_CAPTURE\_POS mode::

    ```
                    |<------ C1 ---->|<------- C2 ------->|
                     ______           ___________          ________________            _
     PWM input     _|      |_________|           |________|                |__________|

     Capture value                   |    C1              |             C2            |
    ```

    参数
    :   - **chan** – the capture channel
        - **config** – the configuration of capture

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_PWM\_NOT\_INIT: PWM driver not init
        - BK\_ERR\_NULL\_PARAM: config is NULL
        - BK\_ERR\_PWM\_CHAN\_ID: invalid channel
        - BK\_ERR\_PWM\_CAPTURE\_EDGE: capture edge is invalid or not supported.
        - others: other errors.

<a id="_CPPv421bk_pwm_capture_deinit10pwm_chan_t"></a>

<a id="_CPPv321bk_pwm_capture_deinit10pwm_chan_t"></a> <a id="_CPPv221bk_pwm_capture_deinit10pwm_chan_t"></a> <a id="bk_pwm_capture_deinit__pwm_chan_t"></a> <a id="group__bk__api__pwm_1gacc5c6613d4e8f1fea9f3e4a557b220a9"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pwm\_capture\_deinit(pwm\_chan\_t chan)
:   Deinit the PWM capture.

    参数
    :   **chan** – the capture channel

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_PWM\_NOT\_INIT: PWM driver not init
        - BK\_ERR\_PWM\_CHAN\_ID: invalid channel
        - others: other errors.

<a id="_CPPv420bk_pwm_capture_start10pwm_chan_t"></a>

<a id="_CPPv320bk_pwm_capture_start10pwm_chan_t"></a> <a id="_CPPv220bk_pwm_capture_start10pwm_chan_t"></a> <a id="bk_pwm_capture_start__pwm_chan_t"></a> <a id="group__bk__api__pwm_1gaa8d1d9cee6831f6f03360a2fa3d3915a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pwm\_capture\_start(pwm\_chan\_t chan)
:   Start the PWM capture.

    参数
    :   **chan** – channel to be started

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_PWM\_NOT\_INIT: PWM driver not init
        - BK\_ERR\_PWM\_CHAN\_ID: invalid PWM channel
        - others: other errors.

<a id="_CPPv419bk_pwm_capture_stop10pwm_chan_t"></a>

<a id="_CPPv319bk_pwm_capture_stop10pwm_chan_t"></a> <a id="_CPPv219bk_pwm_capture_stop10pwm_chan_t"></a> <a id="bk_pwm_capture_stop__pwm_chan_t"></a> <a id="group__bk__api__pwm_1ga24d919012ae64d84daf61063aa8eff05"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pwm\_capture\_stop(pwm\_chan\_t chan)
:   Stop the PWM capture.

    参数
    :   **chan** – channel to be stopped

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_PWM\_NOT\_INIT: PWM driver not init
        - BK\_ERR\_PWM\_CHAN\_ID: invalid PWM channel
        - others: other errors.

<a id="_CPPv424bk_pwm_capture_get_value10pwm_chan_t"></a>

<a id="_CPPv324bk_pwm_capture_get_value10pwm_chan_t"></a> <a id="_CPPv224bk_pwm_capture_get_value10pwm_chan_t"></a> <a id="bk_pwm_capture_get_value__pwm_chan_t"></a> <a id="group__bk__api__pwm_1ga22fa4105ec2ca1e86c7e041327d418a2"></a> uint32\_t bk\_pwm\_capture\_get\_value(pwm\_chan\_t chan)
:   Get the capture value.

    **Attention**
    :   The caller need to make sure the parameter chan is correct!

    参数
    :   **chan** – PWM channel

    返回
    :   capture value

<a id="_CPPv436bk_pwm_capture_get_period_duty_cycle10pwm_chan_t8uint32_t"></a>

<a id="_CPPv336bk_pwm_capture_get_period_duty_cycle10pwm_chan_t8uint32_t"></a> <a id="_CPPv236bk_pwm_capture_get_period_duty_cycle10pwm_chan_t8uint32_t"></a> <a id="bk_pwm_capture_get_period_duty_cycle__pwm_chan_t.uint32_t"></a> <a id="group__bk__api__pwm_1gaae0e6d04a844d9ef917e605184006760"></a> uint32\_t bk\_pwm\_capture\_get\_period\_duty\_cycle(pwm\_chan\_t chan, uint32\_t timeout\_ms)
:   Get the capture period and duty cycle.

    **Attention**
    :   The caller need to make sure the parameter chan is correct!

    参数
    :   - **chan** – PWM channel
        - **timeout\_ms** – timeout ms

    返回
    :   period and duty cycle

<a id="_CPPv421bk_pwm_set_mode_timer10pwm_chan_t"></a>

<a id="_CPPv321bk_pwm_set_mode_timer10pwm_chan_t"></a> <a id="_CPPv221bk_pwm_set_mode_timer10pwm_chan_t"></a> <a id="bk_pwm_set_mode_timer__pwm_chan_t"></a> <a id="group__bk__api__pwm_1gaa2eb2adac89054fe6518549ce66095af"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_pwm\_set\_mode\_timer(pwm\_chan\_t chan)
:   Set pwm channel as timer mode.

    **Attention**
    :   The caller need to make sure the parameter chan is correct!

    参数
    :   **chan** – PWM channel

    返回
    :   - BK\_OK: succeed
        - BK\_ERR\_PWM\_CHAN\_ID: invalid PWM channel
        - others: other errors.
