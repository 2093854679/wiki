---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/application/common/app_audio/app_audio_sync.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="audio-sync-application-functions"></a>

# AUDIO Sync Application Functions

<a id="app-audio-sync-api-brief"></a>

## APP\_AUDIO\_SYNC API Brief

| Application | Brief |
| --- | --- |
| [`app_audio_sync_init()`](#_CPPv419app_audio_sync_initv "app_audio_sync_init") | audio sync initialize function |
| [`app_audio_sync_reg_init()`](#_CPPv423app_audio_sync_reg_initv "app_audio_sync_reg_init") | register audio sync callback function |
| [`app_audio_sync_env_reset()`](#_CPPv424app_audio_sync_env_resetv "app_audio_sync_env_reset") | reset sync environment variable |
| [`app_audio_sync_set_trigger()`](#_CPPv426app_audio_sync_set_triggerP8bt_clk_t "app_audio_sync_set_trigger") | set audio sync trigger time |
| [`app_audio_sync_get_retrigger_time()`](#_CPPv433app_audio_sync_get_retrigger_timeP8uint32_t "app_audio_sync_get_retrigger_time") | get audio sync re-trigger time |
| [`app_audio_sync_update_retrigger_time()`](#_CPPv436app_audio_sync_update_retrigger_timeP8bt_clk_tb "app_audio_sync_update_retrigger_time") | update re-trigger time |
| [`app_music_audio_sync_start()`](#_CPPv426app_music_audio_sync_start8uint32_t "app_music_audio_sync_start") | music audio sync start(only call by BTIF\_TWS\_ROLE\_MASTER) |
| [`app_audio_sync_tws_join_start()`](#_CPPv429app_audio_sync_tws_join_startv "app_audio_sync_tws_join_start") | If condition satisfaction, BTIF\_TWS\_ROLE\_MASTER will send TWS\_SET\_TRIGGER private command to BTIF\_TWS\_ROLE\_SLAVE |
| [`app_audio_sync_slave_req_join()`](#_CPPv429app_audio_sync_slave_req_joinv "app_audio_sync_slave_req_join") | BTIF\_TWS\_ROLE\_SLAVE request to join sync stream link |
| [`app_audio_sync_tws_join_reselect_para()`](#_CPPv437app_audio_sync_tws_join_reselect_para8uint16_t "app_audio_sync_tws_join_reselect_para") | re-select join parameter |
| [`app_audio_sync_tws_rejoin_handle()`](#_CPPv432app_audio_sync_tws_rejoin_handlePK7uint8_t8uint16_t "app_audio_sync_tws_rejoin_handle") | synchronisation tws re-join handler function |
| [`app_audio_sync_tws_a2dp_sch_handle()`](#_CPPv434app_audio_sync_tws_a2dp_sch_handlePK7uint8_t8uint16_t "app_audio_sync_tws_a2dp_sch_handle") | TWS\_SET\_A2DP\_SCH private command handler function |
| [`app_audio_sync_tws_send_resync_time()`](#_CPPv435app_audio_sync_tws_send_resync_time8uint32_t8bt_clk_t "app_audio_sync_tws_send_resync_time") | Send TWS\_SET\_RETRIGGER command |
| [`app_audio_sync_tws_resync_time_handle()`](#_CPPv437app_audio_sync_tws_resync_time_handlePK7uint8_t8uint16_t "app_audio_sync_tws_resync_time_handle") | TWS\_SET\_RETRIGGER command handler function |
| [`app_audio_sync_tws_playback_info_handle()`](#_CPPv439app_audio_sync_tws_playback_info_handlePK7uint8_t8uint16_t "app_audio_sync_tws_playback_info_handle") | TWS\_PLAYBACK\_INFO command handler function |
| [`app_audio_sync_tws_set_trigger_time_handle()`](#_CPPv442app_audio_sync_tws_set_trigger_time_handlePK7uint8_t8uint16_t "app_audio_sync_tws_set_trigger_time_handle") | TWS\_SET\_TRIGGER command handler function(BTIF\_TWS\_ROLE\_SLAVE role only used) |
| [`app_audio_sync_local_media_trigger_handle()`](#_CPPv441app_audio_sync_local_media_trigger_handlePK7uint8_t8uint16_t "app_audio_sync_local_media_trigger_handle") | TWS\_LOCAL\_MEDIA\_TRIGGER command handler function |
| [`app_audio_sync_local_media_start()`](#_CPPv432app_audio_sync_local_media_start7uint8_t8uint32_t7uint8_t "app_audio_sync_local_media_start") | application for play local hint music |
| [`app_audio_sync_cal_diff()`](#_CPPv423app_audio_sync_cal_diff7int32_t "app_audio_sync_cal_diff") | application for calulate frame-diffrence value |
| [`app_audio_sync_join_diff_handle()`](#_CPPv431app_audio_sync_join_diff_handlePK7uint8_t8uint16_t "app_audio_sync_join_diff_handle") | handle for receive frame-diffrence value |

<a id="app-audio-sync-api-reference"></a>

## APP\_AUDIO\_SYNC API Reference

<a id="header-file"></a>

### Header File

- [common/app\_audio/app\_audio\_sync.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/common/app_audio/app_audio_sync.h)

<a id="functions"></a>

### Functions

<a id="_CPPv419app_audio_sync_initv"></a>

<a id="_CPPv319app_audio_sync_initv"></a> <a id="_CPPv219app_audio_sync_initv"></a> <a id="app_audio_sync_init__void"></a> <a id="app__audio__sync_8h_1a8dac97a9294b5b6f0256b34bc22c73a0"></a> void app\_audio\_sync\_init(void)
:   audio sync initialize function

    register app\_audio\_sync\_if\_hci\_event\_handler to gap\_env.li\_evt\_cb

    返回:
    :   N/A

<a id="_CPPv423app_audio_sync_reg_initv"></a>

<a id="_CPPv323app_audio_sync_reg_initv"></a> <a id="_CPPv223app_audio_sync_reg_initv"></a> <a id="app_audio_sync_reg_init__void"></a> <a id="app__audio__sync_8h_1a39b47efb0466713687abe35b09938c7b"></a> void app\_audio\_sync\_reg\_init(void)
:   register audio sync callback function

    register user\_callback and dma\_info\_cb into \_async\_isr\_handle and setting AUDIO\_SYNC\_CTRL1\_SYNC\_A2DP\_CNT of REG\_AUDIO\_SYNC\_CTRL1 register and setting AUDIO\_SYNC\_CTRL1\_SYNC\_CALL\_CNT of REG\_AUDIO\_SYNC\_CTRL1 register register \_async\_isr\_handle callback into g\_isr\_usr\_table

    返回:
    :   N/A

<a id="_CPPv424app_audio_sync_env_resetv"></a>

<a id="_CPPv324app_audio_sync_env_resetv"></a> <a id="_CPPv224app_audio_sync_env_resetv"></a> <a id="app_audio_sync_env_reset__void"></a> <a id="app__audio__sync_8h_1a0e57125fd356c7a06fc3d267ec290120"></a> void app\_audio\_sync\_env\_reset(void)
:   reset sync environment variable

    include async\_clk\_info.async\_dma\_info,async\_clk\_info.dma\_info,async\_clk\_info.fine\_tune\_info

    返回:
    :   N/A

<a id="_CPPv426app_audio_sync_set_triggerP8bt_clk_t"></a>

<a id="_CPPv326app_audio_sync_set_triggerP8bt_clk_t"></a> <a id="_CPPv226app_audio_sync_set_triggerP8bt_clk_t"></a> <a id="app_audio_sync_set_trigger__bt_clk_tP"></a> <a id="app__audio__sync_8h_1a71c542a5ad281707193835a1ae89f278"></a> void app\_audio\_sync\_set\_trigger(bt\_clk\_t \*p\_trigger\_clk)
:   set audio sync trigger time

    When trigger time happen,TWS\_MASTER and TWS\_SLAVE DAC and DMA will start work

    参数:
    :   **\*p\_trigger\_clk** – **\[in\]** trigger clock value this value is piconet clock

    返回:
    :   N/A

<a id="_CPPv433app_audio_sync_get_retrigger_timeP8uint32_t"></a>

<a id="_CPPv333app_audio_sync_get_retrigger_timeP8uint32_t"></a> <a id="_CPPv233app_audio_sync_get_retrigger_timeP8uint32_t"></a> <a id="app_audio_sync_get_retrigger_time__uint32_tP"></a> <a id="app__audio__sync_8h_1a07d9950a9946bf9ec64044b0e37ca5a2"></a> bt\_clk\_t app\_audio\_sync\_get\_retrigger\_time(uint32\_t \*p\_pac\_seq)
:   get audio sync re-trigger time

    get currently piconet clock time

    参数:
    :   **\[in/out\]** – \*p\_pac\_seq input last packet sequence number and add RETRIGGER\_DISCARD\_PAC to overwrite this variable

    返回:
    :   clock current piconet clock time

<a id="_CPPv436app_audio_sync_update_retrigger_timeP8bt_clk_tb"></a>

<a id="_CPPv336app_audio_sync_update_retrigger_timeP8bt_clk_tb"></a> <a id="_CPPv236app_audio_sync_update_retrigger_timeP8bt_clk_tb"></a> <a id="app_audio_sync_update_retrigger_time__bt_clk_tP.b"></a> <a id="app__audio__sync_8h_1a48a4a9f0b930c336e599039212c6935b"></a> void app\_audio\_sync\_update\_retrigger\_time(bt\_clk\_t \*p\_resync\_clk, bool is\_resync)
:   update re-trigger time

    normal PLAY\_START case ,resync\_clk is a future time must bigger then current clock

    参数:
    :   - **\*p\_resync\_clk** – **\[out\]** get resync\_clk
        - **is\_resync** – **\[in\]** true mean is resync,false not resync

    返回:
    :   N/A

<a id="_CPPv426app_music_audio_sync_start8uint32_t"></a>

<a id="_CPPv326app_music_audio_sync_start8uint32_t"></a> <a id="_CPPv226app_music_audio_sync_start8uint32_t"></a> <a id="app_music_audio_sync_start__uint32_t"></a> <a id="app__audio__sync_8h_1a4af7272fd5a5f9152aa6a6f8d082fdad"></a> void app\_music\_audio\_sync\_start(uint32\_t trigger\_delta\_time)
:   music audio sync start(only call by BTIF\_TWS\_ROLE\_MASTER)

    this function will send private command TWS\_SET\_TRIGGER with trigger time info to BTIF\_TWS\_ROLE\_SLAVE trigger time \= current clock\+trigger\_delta\_time(ms)\* 1000 / 3125 \* 10

    参数:
    :   **trigger\_delta\_time** – **\[in\]** must more than 150ms audio data,current use [TRIGGER\_CLK\_DELTA\_TIME(260ms)](#app__audio__sync_8h_1a5ee6bcfc9c2f24c72d71057cdde121f4)

    返回:
    :   N/A

<a id="_CPPv429app_audio_sync_tws_join_startv"></a>

<a id="_CPPv329app_audio_sync_tws_join_startv"></a> <a id="_CPPv229app_audio_sync_tws_join_startv"></a> <a id="app_audio_sync_tws_join_start__void"></a> <a id="app__audio__sync_8h_1abd9ebd53ccc5b8a2c79c00218c818c62"></a> bool app\_audio\_sync\_tws\_join\_start(void)
:   If condition satisfaction, BTIF\_TWS\_ROLE\_MASTER will send TWS\_SET\_TRIGGER private command to BTIF\_TWS\_ROLE\_SLAVE.

    normal case: phone is playing music before profile sync done need execute audio\_join procedure

    返回:
    :   star join status true: satisfy condition and sent TWS\_SET\_TRIGGER private command to BTIF\_TWS\_ROLE\_SLAVE false : not satisfy condition

<a id="_CPPv429app_audio_sync_slave_req_joinv"></a>

<a id="_CPPv329app_audio_sync_slave_req_joinv"></a> <a id="_CPPv229app_audio_sync_slave_req_joinv"></a> <a id="app_audio_sync_slave_req_join__void"></a> <a id="app__audio__sync_8h_1ab6a4852e33f6b8f2d80b34c83f23c8b7"></a> void app\_audio\_sync\_slave\_req\_join(void)
:   BTIF\_TWS\_ROLE\_SLAVE request to join sync stream link.

    condition : When BTIF\_TWS\_ROLE\_SLAVE receive async\_ctrl.type is PLAY\_START and current\_clk.half\_slot\_clk \+ RETRIGGER\_BUFF\_TIME is bigger then async\_ctrl.clk.half\_slot\_clk will call this function to send TWS\_AUDIO\_REJOIN private command to BTIF\_TWS\_ROLE\_MASTER. BTIF\_TWS\_ROLE\_MASTER received TWS\_AUDIO\_REJOIN will trigger app\_audio\_sync\_tws\_join\_start function

    返回:
    :   N/A

<a id="_CPPv437app_audio_sync_tws_join_reselect_para8uint16_t"></a>

<a id="_CPPv337app_audio_sync_tws_join_reselect_para8uint16_t"></a> <a id="_CPPv237app_audio_sync_tws_join_reselect_para8uint16_t"></a> <a id="app_audio_sync_tws_join_reselect_para__uint16_t"></a> <a id="app__audio__sync_8h_1aed7a1ff389f8f245bd409487d891b081"></a> void app\_audio\_sync\_tws\_join\_reselect\_para(uint16\_t packet\_seq)
:   re-select join parameter

    When the packet sequence number of the received packet exceeds the packet sequence number of the scheduled synchronisation packet , you need to re-select the packet sequence number of the synchronisation packet.

    参数:
    :   **packet\_seq** – **\[in\]** packet sequence number of the scheduled synchronisation packet(async\_ctrl.pac\_seq)

    返回:
    :   N/A

<a id="_CPPv432app_audio_sync_tws_rejoin_handlePK7uint8_t8uint16_t"></a>

<a id="_CPPv332app_audio_sync_tws_rejoin_handlePK7uint8_t8uint16_t"></a> <a id="_CPPv232app_audio_sync_tws_rejoin_handlePK7uint8_t8uint16_t"></a> <a id="app_audio_sync_tws_rejoin_handle__uint8_tCP.uint16_t"></a> <a id="app__audio__sync_8h_1ad336cf1dd8b957bfc9134fbfa72275c1"></a> void app\_audio\_sync\_tws\_rejoin\_handle(const uint8\_t \*p\_data, uint16\_t length)
:   synchronisation tws re-join handler function

    BTIF\_TWS\_ROLE\_MASTER received TWS\_AUDIO\_REJOIN private command then trigger this function and run app\_audio\_sync\_tws\_start\_join\_procedure function

    参数:
    :   - **\*p\_data** – **\[in\]** TWS\_AUDIO\_REJOIN command packet
        - **length** – **\[in\]** TWS\_AUDIO\_REJOIN command packet length

    返回:
    :   N/A

<a id="_CPPv434app_audio_sync_tws_a2dp_sch_handlePK7uint8_t8uint16_t"></a>

<a id="_CPPv334app_audio_sync_tws_a2dp_sch_handlePK7uint8_t8uint16_t"></a> <a id="_CPPv234app_audio_sync_tws_a2dp_sch_handlePK7uint8_t8uint16_t"></a> <a id="app_audio_sync_tws_a2dp_sch_handle__uint8_tCP.uint16_t"></a> <a id="app__audio__sync_8h_1ad34d128b76428208c35565b70a52cc88"></a> void app\_audio\_sync\_tws\_a2dp\_sch\_handle(const uint8\_t \*p\_data, uint16\_t length)
:   TWS\_SET\_A2DP\_SCH private command handler function.

    received from BTIF\_TWS\_ROLE\_SLAVE TWS\_SET\_A2DP\_SCH private command will trigger this function BTIF\_TWS\_ROLE\_MASTER will send HCI\_VS\_SET\_LINK\_PROFILE\_CMD\_OPCODE command to controller for change specific mobile link TDD schedule

    参数:
    :   - **\*p\_data** – **\[in\]** TWS\_SET\_A2DP\_SCH command packet
        - **length** – **\[in\]** TWS\_SET\_A2DP\_SCH command packet length

    返回:
    :   N/A

<a id="_CPPv435app_audio_sync_tws_send_resync_time8uint32_t8bt_clk_t"></a>

<a id="_CPPv335app_audio_sync_tws_send_resync_time8uint32_t8bt_clk_t"></a> <a id="_CPPv235app_audio_sync_tws_send_resync_time8uint32_t8bt_clk_t"></a> <a id="app_audio_sync_tws_send_resync_time__uint32_t.bt_clk_t"></a> <a id="app__audio__sync_8h_1aae4fc09d56d77b78c3457622d6af6fc1"></a> void app\_audio\_sync\_tws\_send\_resync\_time(uint32\_t pac\_seq, bt\_clk\_t resync\_clk)
:   Send TWS\_SET\_RETRIGGER command.

    This function no used

    Param :

<a id="_CPPv437app_audio_sync_tws_resync_time_handlePK7uint8_t8uint16_t"></a>

<a id="_CPPv337app_audio_sync_tws_resync_time_handlePK7uint8_t8uint16_t"></a> <a id="_CPPv237app_audio_sync_tws_resync_time_handlePK7uint8_t8uint16_t"></a> <a id="app_audio_sync_tws_resync_time_handle__uint8_tCP.uint16_t"></a> <a id="app__audio__sync_8h_1ae84470ed996c3fa9f653fa42b042d3b5"></a> void app\_audio\_sync\_tws\_resync\_time\_handle(const uint8\_t \*p\_data, uint16\_t length)
:   TWS\_SET\_RETRIGGER command handler function.

    received TWS\_SET\_RETRIGGER command (This function no used)

    参数:
    :   - **\*p\_data** – **\[in\]** TWS\_SET\_RETRIGGER command packet
        - **length** – **\[in\]** TWS\_SET\_RETRIGGER command packet length

    返回:
    :   N/A

<a id="_CPPv439app_audio_sync_tws_playback_info_handlePK7uint8_t8uint16_t"></a>

<a id="_CPPv339app_audio_sync_tws_playback_info_handlePK7uint8_t8uint16_t"></a> <a id="_CPPv239app_audio_sync_tws_playback_info_handlePK7uint8_t8uint16_t"></a> <a id="app_audio_sync_tws_playback_info_handle__uint8_tCP.uint16_t"></a> <a id="app__audio__sync_8h_1aead32e6a7d0fe312e8f13f16664a83da"></a> void app\_audio\_sync\_tws\_playback\_info\_handle(const uint8\_t \*p\_data, uint16\_t length)
:   TWS\_PLAYBACK\_INFO command handler function.

    received TWS\_PLAYBACK\_INFO command(This function no used)

    参数:
    :   - **\*p\_data** – **\[in\]** TWS\_PLAYBACK\_INFO command packet
        - **length** – **\[in\]** TWS\_PLAYBACK\_INFO command packet length

    返回:
    :   N/A

<a id="_CPPv442app_audio_sync_tws_set_trigger_time_handlePK7uint8_t8uint16_t"></a>

<a id="_CPPv342app_audio_sync_tws_set_trigger_time_handlePK7uint8_t8uint16_t"></a> <a id="_CPPv242app_audio_sync_tws_set_trigger_time_handlePK7uint8_t8uint16_t"></a> <a id="app_audio_sync_tws_set_trigger_time_handle__uint8_tCP.uint16_t"></a> <a id="app__audio__sync_8h_1a28c2984074c7fe573a7e8f55b02bee91"></a> void app\_audio\_sync\_tws\_set\_trigger\_time\_handle(const uint8\_t \*p\_data, uint16\_t length)
:   TWS\_SET\_TRIGGER command handler function(BTIF\_TWS\_ROLE\_SLAVE role only used)

    received TWS\_SET\_TRIGGER command and update async\_clk\_info\[ASYNC\_MUSIC\_PATH\] parameter and DMA info initialize

    参数:
    :   - **\*p\_data** – **\[in\]** TWS\_SET\_TRIGGER command packet
        - **length** – **\[in\]** TWS\_SET\_TRIGGER command packet length

    返回:
    :   N/A

<a id="_CPPv441app_audio_sync_local_media_trigger_handlePK7uint8_t8uint16_t"></a>

<a id="_CPPv341app_audio_sync_local_media_trigger_handlePK7uint8_t8uint16_t"></a> <a id="_CPPv241app_audio_sync_local_media_trigger_handlePK7uint8_t8uint16_t"></a> <a id="app_audio_sync_local_media_trigger_handle__uint8_tCP.uint16_t"></a> <a id="app__audio__sync_8h_1a97d525846018684f7a53d86db9a72486"></a> void app\_audio\_sync\_local\_media\_trigger\_handle(const uint8\_t \*p\_data, uint16\_t length)
:   TWS\_LOCAL\_MEDIA\_TRIGGER command handler function.

    received TWS\_LOCAL\_MEDIA\_TRIGGER command and set local trigger time to play hint music

    参数:
    :   - **\*p\_data** – **\[in\]** TWS\_LOCAL\_MEDIA\_TRIGGER command packet
        - **length** – **\[in\]** TWS\_LOCAL\_MEDIA\_TRIGGER command packet length

    返回:
    :   N/A

<a id="_CPPv432app_audio_sync_local_media_start7uint8_t8uint32_t7uint8_t"></a>

<a id="_CPPv332app_audio_sync_local_media_start7uint8_t8uint32_t7uint8_t"></a> <a id="_CPPv232app_audio_sync_local_media_start7uint8_t8uint32_t7uint8_t"></a> <a id="app_audio_sync_local_media_start__uint8_t.uint32_t.uint8_t"></a> <a id="app__audio__sync_8h_1af716f0b10230873928223190fd1aee2d"></a> void app\_audio\_sync\_local\_media\_start(uint8\_t async\_path, uint32\_t trigger\_delta\_time, uint8\_t hint\_id)
:   application for play local hint music

    参数:
    :   - **async\_path** – **\[in\]** Asynchronisation path this variable must use ASYNC\_LOCAL\_MEDIA\_PATH
        - **trigger\_delta\_time** – **\[in\]** must used TRIGGER\_CLK\_DELTA\_TIME
        - **hint\_id** – **\[in\]** hint music id number

    返回:
    :   N/A

<a id="_CPPv432app_audio_sync_dac_isr_info_init12async_path_t8uint32_t"></a>

<a id="_CPPv332app_audio_sync_dac_isr_info_init12async_path_t8uint32_t"></a> <a id="_CPPv232app_audio_sync_dac_isr_info_init12async_path_t8uint32_t"></a> <a id="app_audio_sync_dac_isr_info_init__async_path_t.uint32_t"></a> <a id="app__audio__sync_8h_1ad807435805d4995f91dda932dfc893ff"></a> void app\_audio\_sync\_dac\_isr\_info\_init(async\_path\_t async\_path, uint32\_t init\_cnt)
:   init dac isr information

    init dac isr information

    参数:
    :   - **async\_path** – **\[in\]** Asynchronisation path
        - **init\_cnt** – **\[in\]** dac isr init count

    返回:
    :   N/A

<a id="_CPPv423app_audio_sync_cal_diff7int32_t"></a>

<a id="_CPPv323app_audio_sync_cal_diff7int32_t"></a> <a id="_CPPv223app_audio_sync_cal_diff7int32_t"></a> <a id="app_audio_sync_cal_diff__int32_t"></a> <a id="app__audio__sync_8h_1a5202bd79ce6d0fff9931ce47a81c94f2"></a> void app\_audio\_sync\_cal\_diff(int32\_t diff)
:   application for calulate frame-diffrence value

    参数:
    :   **diff** – **\[in\]** dufault diffrence value

    返回:
    :   N/A

<a id="_CPPv431app_audio_sync_join_diff_handlePK7uint8_t8uint16_t"></a>

<a id="_CPPv331app_audio_sync_join_diff_handlePK7uint8_t8uint16_t"></a> <a id="_CPPv231app_audio_sync_join_diff_handlePK7uint8_t8uint16_t"></a> <a id="app_audio_sync_join_diff_handle__uint8_tCP.uint16_t"></a> <a id="app__audio__sync_8h_1a3e031d42aef5cf68964526fa50fca9a6"></a> void app\_audio\_sync\_join\_diff\_handle(const uint8\_t \*p\_data, uint16\_t length)
:   handle for receive frame-diffrence value

    参数:
    :   - **p\_data** – **\[in\]** the pointer of join diff sturct
        - **p\_data** – **\[in\]** the length of join diff struct

    返回:
    :   N/A

<a id="structures"></a>

### Structures

<a id="_CPPv416fine_tune_info_t"></a>

<a id="_CPPv316fine_tune_info_t"></a> <a id="_CPPv216fine_tune_info_t"></a> <a id="fine_tune_info_t"></a> <a id="structfine__tune__info__t"></a> struct fine\_tune\_info\_t

<a id="_CPPv418trigger_pkt_into_t"></a>

<a id="_CPPv318trigger_pkt_into_t"></a> <a id="_CPPv218trigger_pkt_into_t"></a> <a id="trigger_pkt_into_t"></a> <a id="structtrigger__pkt__into__t"></a> struct trigger\_pkt\_into\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18trigger_pkt_into_t11trigger_clkE"></a>

    <a id="_CPPv3N18trigger_pkt_into_t11trigger_clkE"></a> <a id="_CPPv2N18trigger_pkt_into_t11trigger_clkE"></a> <a id="trigger_pkt_into_t::trigger_clk__bt_clk_t"></a> <a id="structtrigger__pkt__into__t_1a13ab14ed0bec40a07d79ab734336be94"></a> bt\_clk\_t trigger\_clk
    :   trigger clock base on piconet clock

    <a id="_CPPv4N18trigger_pkt_into_t10packet_seqE"></a>

    <a id="_CPPv3N18trigger_pkt_into_t10packet_seqE"></a> <a id="_CPPv2N18trigger_pkt_into_t10packet_seqE"></a> <a id="trigger_pkt_into_t::packet_seq__uint32_t"></a> <a id="structtrigger__pkt__into__t_1ab741a6ccb5653515c0e8593f2a7c5898"></a> uint32\_t packet\_seq
    :   packet sequence number

    <a id="_CPPv4N18trigger_pkt_into_t9frame_seqE"></a>

    <a id="_CPPv3N18trigger_pkt_into_t9frame_seqE"></a> <a id="_CPPv2N18trigger_pkt_into_t9frame_seqE"></a> <a id="trigger_pkt_into_t::frame_seq__uint32_t"></a> <a id="structtrigger__pkt__into__t_1ae492345b0b75c2e199b37a654c0d7b50"></a> uint32\_t frame\_seq
    :   frame sequence number

    <a id="_CPPv4N18trigger_pkt_into_t7dma_cntE"></a>

    <a id="_CPPv3N18trigger_pkt_into_t7dma_cntE"></a> <a id="_CPPv2N18trigger_pkt_into_t7dma_cntE"></a> <a id="trigger_pkt_into_t::dma_cnt__uint32_t"></a> <a id="structtrigger__pkt__into__t_1a9c144a4ca29a1f5d49d1a2559a227732"></a> uint32\_t dma\_cnt
    :   dma isr count

    <a id="_CPPv4N18trigger_pkt_into_t7log_idxE"></a>

    <a id="_CPPv3N18trigger_pkt_into_t7log_idxE"></a> <a id="_CPPv2N18trigger_pkt_into_t7log_idxE"></a> <a id="trigger_pkt_into_t::log_idx__uint32_t"></a> <a id="structtrigger__pkt__into__t_1a48f785a23c17385117f0fd245c0eb321"></a> uint32\_t log\_idx
    :   log index

<a id="_CPPv414trigger_info_t"></a>

<a id="_CPPv314trigger_info_t"></a> <a id="_CPPv214trigger_info_t"></a> <a id="trigger_info_t"></a> <a id="structtrigger__info__t"></a> struct trigger\_info\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N14trigger_info_t8cmd_codeE"></a>

    <a id="_CPPv3N14trigger_info_t8cmd_codeE"></a> <a id="_CPPv2N14trigger_info_t8cmd_codeE"></a> <a id="trigger_info_t::cmd_code__uint16_t"></a> <a id="structtrigger__info__t_1aab2f2a64b006268c02b2676477b1a31d"></a> uint16\_t cmd\_code
    :   private command code example (TWS\_SET\_TRIGGER)

    <a id="_CPPv4N14trigger_info_t10async_pathE"></a>

    <a id="_CPPv3N14trigger_info_t10async_pathE"></a> <a id="_CPPv2N14trigger_info_t10async_pathE"></a> <a id="trigger_info_t::async_path__async_path_t"></a> <a id="structtrigger__info__t_1a205eabe499cd5c755a73358cbb39623f"></a> async\_path\_t async\_path
    :   Asynchronous path example(ASYNC\_MUSIC\_PATH)

    <a id="_CPPv4N14trigger_info_t14master_startedE"></a>

    <a id="_CPPv3N14trigger_info_t14master_startedE"></a> <a id="_CPPv2N14trigger_info_t14master_startedE"></a> <a id="trigger_info_t::master_started__b"></a> <a id="structtrigger__info__t_1a1ffc97f3d25e9e93f55e04fd1e6c2712"></a> bool master\_started
    :   master started or not

    <a id="_CPPv4N14trigger_info_t17trig_pkt_info_cntE"></a>

    <a id="_CPPv3N14trigger_info_t17trig_pkt_info_cntE"></a> <a id="_CPPv2N14trigger_info_t17trig_pkt_info_cntE"></a> <a id="trigger_info_t::trig_pkt_info_cnt__uint8_t"></a> <a id="structtrigger__info__t_1a16e6fea82aab8a1f6e7c4684bfee61f5"></a> uint8\_t trig\_pkt\_info\_cnt
    :   trigger packet info count

    <a id="_CPPv4N14trigger_info_t11mobile_addrE"></a>

    <a id="_CPPv3N14trigger_info_t11mobile_addrE"></a> <a id="_CPPv2N14trigger_info_t11mobile_addrE"></a> <a id="trigger_info_t::mobile_addr__uint8_tA"></a> <a id="structtrigger__info__t_1a7f98ac297088c92d293156fa7a9c0d53"></a> uint8\_t mobile\_addr\[6\]
    :   mobile address

    <a id="_CPPv4N14trigger_info_t9start_seqE"></a>

    <a id="_CPPv3N14trigger_info_t9start_seqE"></a> <a id="_CPPv2N14trigger_info_t9start_seqE"></a> <a id="trigger_info_t::start_seq__uint32_t"></a> <a id="structtrigger__info__t_1ab59f8a343eddeea0107490c7d4472e1d"></a> uint32\_t start\_seq
    :   start sequence number

    <a id="_CPPv4N14trigger_info_t16trigger_pkt_infoE"></a>

    <a id="_CPPv3N14trigger_info_t16trigger_pkt_infoE"></a> <a id="_CPPv2N14trigger_info_t16trigger_pkt_infoE"></a> <a id="trigger_info_t::trigger_pkt_info__trigger_pkt_into_tA"></a> <a id="structtrigger__info__t_1a37d244124fadf2fb54d3ff2920888c30"></a> [trigger\_pkt\_into\_t](#_CPPv418trigger_pkt_into_t "trigger_pkt_into_t") trigger\_pkt\_info\[ASYNC\_TRIGGER\_INFO\_MAX\]
    :   trigger packet info array

<a id="_CPPv416async_clk_info_t"></a>

<a id="_CPPv316async_clk_info_t"></a> <a id="_CPPv216async_clk_info_t"></a> <a id="async_clk_info_t"></a> <a id="structasync__clk__info__t"></a> struct async\_clk\_info\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N16async_clk_info_t13master_na_clkE"></a>

    <a id="_CPPv3N16async_clk_info_t13master_na_clkE"></a> <a id="_CPPv2N16async_clk_info_t13master_na_clkE"></a> <a id="async_clk_info_t::master_na_clk__bt_clk_t"></a> <a id="structasync__clk__info__t_1a39ecf6214ee8a3d0512fe516cddc4b46"></a> bt\_clk\_t master\_na\_clk
    :   master native clock

    <a id="_CPPv4N16async_clk_info_t14master_clk_offE"></a>

    <a id="_CPPv3N16async_clk_info_t14master_clk_offE"></a> <a id="_CPPv2N16async_clk_info_t14master_clk_offE"></a> <a id="async_clk_info_t::master_clk_off__clkoff_info_t"></a> <a id="structasync__clk__info__t_1a33fcd75ebeab68f71f827a0aff92a375"></a> clkoff\_info\_t master\_clk\_off
    :   master clock offset

    <a id="_CPPv4N16async_clk_info_t18master_trigger_clkE"></a>

    <a id="_CPPv3N16async_clk_info_t18master_trigger_clkE"></a> <a id="_CPPv2N16async_clk_info_t18master_trigger_clkE"></a> <a id="async_clk_info_t::master_trigger_clk__trigger_info_t"></a> <a id="structasync__clk__info__t_1aa0c87fc6ced8d16481e4e193ee88b1e8"></a> [trigger\_info\_t](#_CPPv414trigger_info_t "trigger_info_t") master\_trigger\_clk
    :   master trigger info

    <a id="_CPPv4N16async_clk_info_t12slave_na_clkE"></a>

    <a id="_CPPv3N16async_clk_info_t12slave_na_clkE"></a> <a id="_CPPv2N16async_clk_info_t12slave_na_clkE"></a> <a id="async_clk_info_t::slave_na_clk__bt_clk_t"></a> <a id="structasync__clk__info__t_1a2f6aed57e88955b39fe9ab29737538f7"></a> bt\_clk\_t slave\_na\_clk
    :   slave native clock

    <a id="_CPPv4N16async_clk_info_t13slave_clk_offE"></a>

    <a id="_CPPv3N16async_clk_info_t13slave_clk_offE"></a> <a id="_CPPv2N16async_clk_info_t13slave_clk_offE"></a> <a id="async_clk_info_t::slave_clk_off__clkoff_info_t"></a> <a id="structasync__clk__info__t_1a89ec0b601e103813629a3c949c204ab6"></a> clkoff\_info\_t slave\_clk\_off
    :   slave clock offset

    <a id="_CPPv4N16async_clk_info_t22slave_recv_trigger_clkE"></a>

    <a id="_CPPv3N16async_clk_info_t22slave_recv_trigger_clkE"></a> <a id="_CPPv2N16async_clk_info_t22slave_recv_trigger_clkE"></a> <a id="async_clk_info_t::slave_recv_trigger_clk__trigger_info_t"></a> <a id="structasync__clk__info__t_1abca2d78bad206ccaec93b497fdb12efa"></a> [trigger\_info\_t](#_CPPv414trigger_info_t "trigger_info_t") slave\_recv\_trigger\_clk
    :   get from master TWS\_SET\_TRIGGER private cmd master\_trigger\_clk

    <a id="_CPPv4N16async_clk_info_t16hint_trigger_cntE"></a>

    <a id="_CPPv3N16async_clk_info_t16hint_trigger_cntE"></a> <a id="_CPPv2N16async_clk_info_t16hint_trigger_cntE"></a> <a id="async_clk_info_t::hint_trigger_cnt__uint32_t"></a> <a id="structasync__clk__info__t_1a89dba669a5c414406b9fcb064ecdfeb6"></a> uint32\_t hint\_trigger\_cnt
    :   hint music trigger count

    <a id="_CPPv4N16async_clk_info_t17music_trigger_cntE"></a>

    <a id="_CPPv3N16async_clk_info_t17music_trigger_cntE"></a> <a id="_CPPv2N16async_clk_info_t17music_trigger_cntE"></a> <a id="async_clk_info_t::music_trigger_cnt__uint32_t"></a> <a id="structasync__clk__info__t_1a13c73aced579b65a79ec8a0b5e818f81"></a> uint32\_t music\_trigger\_cnt
    :   music trigger count

    <a id="_CPPv4N16async_clk_info_t16call_trigger_cntE"></a>

    <a id="_CPPv3N16async_clk_info_t16call_trigger_cntE"></a> <a id="_CPPv2N16async_clk_info_t16call_trigger_cntE"></a> <a id="async_clk_info_t::call_trigger_cnt__uint32_t"></a> <a id="structasync__clk__info__t_1ab6b4b037dcdbe9fea0310dbcf152af2e"></a> uint32\_t call\_trigger\_cnt
    :   call trigger count

    <a id="_CPPv4N16async_clk_info_t15mic_trigger_cntE"></a>

    <a id="_CPPv3N16async_clk_info_t15mic_trigger_cntE"></a> <a id="_CPPv2N16async_clk_info_t15mic_trigger_cntE"></a> <a id="async_clk_info_t::mic_trigger_cnt__uint32_t"></a> <a id="structasync__clk__info__t_1aa49aa619029ec639d6619fb2c46382a3"></a> uint32\_t mic\_trigger\_cnt
    :   microphone trigger count

    <a id="_CPPv4N16async_clk_info_t14async_dma_infoE"></a>

    <a id="_CPPv3N16async_clk_info_t14async_dma_infoE"></a> <a id="_CPPv2N16async_clk_info_t14async_dma_infoE"></a> <a id="async_clk_info_t::async_dma_info__async_dma_info_tA"></a> <a id="structasync__clk__info__t_1a94ba8cafc1d769afe55ebecad48f1886"></a> async\_dma\_info\_t async\_dma\_info\[ASYNC\_TRIGGER\_INFO\_MAX\]
    :   async dma info array

    <a id="_CPPv4N16async_clk_info_t12dma_info_idxE"></a>

    <a id="_CPPv3N16async_clk_info_t12dma_info_idxE"></a> <a id="_CPPv2N16async_clk_info_t12dma_info_idxE"></a> <a id="async_clk_info_t::dma_info_idx__uint32_t"></a> <a id="structasync__clk__info__t_1aa0f240559bd045397d9c082139483dde"></a> uint32\_t dma\_info\_idx
    :   dma info index

    <a id="_CPPv4N16async_clk_info_t13fine_tune_idxE"></a>

    <a id="_CPPv3N16async_clk_info_t13fine_tune_idxE"></a> <a id="_CPPv2N16async_clk_info_t13fine_tune_idxE"></a> <a id="async_clk_info_t::fine_tune_idx__uint32_t"></a> <a id="structasync__clk__info__t_1a6457f71371dec8f34bbd4a4755e07323"></a> uint32\_t fine\_tune\_idx
    :   fine tune index

    <a id="_CPPv4N16async_clk_info_t8dma_infoE"></a>

    <a id="_CPPv3N16async_clk_info_t8dma_infoE"></a> <a id="_CPPv2N16async_clk_info_t8dma_infoE"></a> <a id="async_clk_info_t::dma_info__async_dma_info_tA"></a> <a id="structasync__clk__info__t_1ad3f99d192dd7de4118b031cd9d026cc6"></a> async\_dma\_info\_t dma\_info\[ASYNC\_DMA\_INFO\_MAX\]
    :   dma info array

    <a id="_CPPv4N16async_clk_info_t14fine_tune_infoE"></a>

    <a id="_CPPv3N16async_clk_info_t14fine_tune_infoE"></a> <a id="_CPPv2N16async_clk_info_t14fine_tune_infoE"></a> <a id="async_clk_info_t::fine_tune_info__fine_tune_info_tA"></a> <a id="structasync__clk__info__t_1ac907ee8746891a0186e68ef174fe3bb2"></a> [fine\_tune\_info\_t](#_CPPv416fine_tune_info_t "fine_tune_info_t") fine\_tune\_info\[ASYNC\_FINE\_TUNE\_MAX\]
    :   fine tune info array

<a id="_CPPv416async_pid_ctrl_t"></a>

<a id="_CPPv316async_pid_ctrl_t"></a> <a id="_CPPv216async_pid_ctrl_t"></a> <a id="async_pid_ctrl_t"></a> <a id="structasync__pid__ctrl__t"></a> struct async\_pid\_ctrl\_t

<a id="_CPPv415playback_unit_t"></a>

<a id="_CPPv315playback_unit_t"></a> <a id="_CPPv215playback_unit_t"></a> <a id="playback_unit_t"></a> <a id="structplayback__unit__t"></a> struct playback\_unit\_t

<a id="_CPPv415playback_into_t"></a>

<a id="_CPPv315playback_into_t"></a> <a id="_CPPv215playback_into_t"></a> <a id="playback_into_t"></a> <a id="structplayback__into__t"></a> struct playback\_into\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N15playback_into_t8cmd_codeE"></a>

    <a id="_CPPv3N15playback_into_t8cmd_codeE"></a> <a id="_CPPv2N15playback_into_t8cmd_codeE"></a> <a id="playback_into_t::cmd_code__uint16_t"></a> <a id="structplayback__into__t_1a7a5d99f0a82a9a5bbb5000822f0216d2"></a> uint16\_t cmd\_code
    :   private command code example (TWS\_PLAYBACK\_INFO)

<a id="_CPPv413resync_info_t"></a>

<a id="_CPPv313resync_info_t"></a> <a id="_CPPv213resync_info_t"></a> <a id="resync_info_t"></a> <a id="structresync__info__t"></a> struct resync\_info\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N13resync_info_t8cmd_codeE"></a>

    <a id="_CPPv3N13resync_info_t8cmd_codeE"></a> <a id="_CPPv2N13resync_info_t8cmd_codeE"></a> <a id="resync_info_t::cmd_code__uint16_t"></a> <a id="structresync__info__t_1a592494acb86c6641e36d2d0deedecbe9"></a> uint16\_t cmd\_code
    :   private command code example (TWS\_SET\_RETRIGGER)

    <a id="_CPPv4N13resync_info_t10packet_seqE"></a>

    <a id="_CPPv3N13resync_info_t10packet_seqE"></a> <a id="_CPPv2N13resync_info_t10packet_seqE"></a> <a id="resync_info_t::packet_seq__uint32_t"></a> <a id="structresync__info__t_1ad84090909727d7a6c845dab61642dc16"></a> uint32\_t packet\_seq
    :   packet sequence number

    <a id="_CPPv4N13resync_info_t10resync_clkE"></a>

    <a id="_CPPv3N13resync_info_t10resync_clkE"></a> <a id="_CPPv2N13resync_info_t10resync_clkE"></a> <a id="resync_info_t::resync_clk__bt_clk_t"></a> <a id="structresync__info__t_1ab726b17f06d64140274a5f1a77035d7a"></a> bt\_clk\_t resync\_clk
    :   resync clock

<a id="_CPPv415retrigger_req_t"></a>

<a id="_CPPv315retrigger_req_t"></a> <a id="_CPPv215retrigger_req_t"></a> <a id="retrigger_req_t"></a> <a id="structretrigger__req__t"></a> struct retrigger\_req\_t

<a id="_CPPv413a2dp_sch_en_t"></a>

<a id="_CPPv313a2dp_sch_en_t"></a> <a id="_CPPv213a2dp_sch_en_t"></a> <a id="a2dp_sch_en_t"></a> <a id="structa2dp__sch__en__t"></a> struct a2dp\_sch\_en\_t
:   re-trigger request type not used

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N13a2dp_sch_en_t8cmd_codeE"></a>

    <a id="_CPPv3N13a2dp_sch_en_t8cmd_codeE"></a> <a id="_CPPv2N13a2dp_sch_en_t8cmd_codeE"></a> <a id="a2dp_sch_en_t::cmd_code__uint16_t"></a> <a id="structa2dp__sch__en__t_1af3084e8fcd4d7447f4781d35d1871026"></a> uint16\_t cmd\_code
    :   private command code example (TWS\_SET\_A2DP\_SCH)

    <a id="_CPPv4N13a2dp_sch_en_t4addrE"></a>

    <a id="_CPPv3N13a2dp_sch_en_t4addrE"></a> <a id="_CPPv2N13a2dp_sch_en_t4addrE"></a> <a id="a2dp_sch_en_t::addr__btif_bd_addr_t"></a> <a id="structa2dp__sch__en__t_1a8863e2640a6737c287838e8ba8e67b37"></a> [btif\_bd\_addr\_t](../../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr
    :   bluetooth address

    <a id="_CPPv4N13a2dp_sch_en_t11a2dp_enableE"></a>

    <a id="_CPPv3N13a2dp_sch_en_t11a2dp_enableE"></a> <a id="_CPPv2N13a2dp_sch_en_t11a2dp_enableE"></a> <a id="a2dp_sch_en_t::a2dp_enable__b"></a> <a id="structa2dp__sch__en__t_1ac18e35306ee5450ca7b73eed2cd1afd7"></a> bool a2dp\_enable
    :   get from master TWS\_SET\_A2DP\_SCH private command

<a id="_CPPv418audio_rejoin_req_t"></a>

<a id="_CPPv318audio_rejoin_req_t"></a> <a id="_CPPv218audio_rejoin_req_t"></a> <a id="audio_rejoin_req_t"></a> <a id="structaudio__rejoin__req__t"></a> struct audio\_rejoin\_req\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N18audio_rejoin_req_t8cmd_codeE"></a>

    <a id="_CPPv3N18audio_rejoin_req_t8cmd_codeE"></a> <a id="_CPPv2N18audio_rejoin_req_t8cmd_codeE"></a> <a id="audio_rejoin_req_t::cmd_code__uint16_t"></a> <a id="structaudio__rejoin__req__t_1ac091c1cff61ed7425abe2e0736423c8c"></a> uint16\_t cmd\_code
    :   private command code example (TWS\_AUDIO\_REJOIN)

    <a id="_CPPv4N18audio_rejoin_req_t4addrE"></a>

    <a id="_CPPv3N18audio_rejoin_req_t4addrE"></a> <a id="_CPPv2N18audio_rejoin_req_t4addrE"></a> <a id="audio_rejoin_req_t::addr__btif_bd_addr_t"></a> <a id="structaudio__rejoin__req__t_1ab6af933884042856dc68b72991fe0e4a"></a> [btif\_bd\_addr\_t](../../../btif/btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr
    :   bluetooth address

<a id="_CPPv417audio_join_diff_t"></a>

<a id="_CPPv317audio_join_diff_t"></a> <a id="_CPPv217audio_join_diff_t"></a> <a id="audio_join_diff_t"></a> <a id="structaudio__join__diff__t"></a> struct audio\_join\_diff\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N17audio_join_diff_t8cmd_codeE"></a>

    <a id="_CPPv3N17audio_join_diff_t8cmd_codeE"></a> <a id="_CPPv2N17audio_join_diff_t8cmd_codeE"></a> <a id="audio_join_diff_t::cmd_code__uint16_t"></a> <a id="structaudio__join__diff__t_1aaa79aa8ef2d106dcb70809e19f7e440d"></a> uint16\_t cmd\_code
    :   private command code example (TWS\_AUDIO\_JOIN\_DIFF)

    <a id="_CPPv4N17audio_join_diff_t10frame_diffE"></a>

    <a id="_CPPv3N17audio_join_diff_t10frame_diffE"></a> <a id="_CPPv2N17audio_join_diff_t10frame_diffE"></a> <a id="audio_join_diff_t::frame_diff__int32_t"></a> <a id="structaudio__join__diff__t_1a5a436da933cbed5d8b4345ee32c253c7"></a> int32\_t frame\_diff
    :   frame diffrence value

    <a id="_CPPv4N17audio_join_diff_t9frame_cntE"></a>

    <a id="_CPPv3N17audio_join_diff_t9frame_cntE"></a> <a id="_CPPv2N17audio_join_diff_t9frame_cntE"></a> <a id="audio_join_diff_t::frame_cnt__uint32_t"></a> <a id="structaudio__join__diff__t_1afc1b0aba7547e919259575524ef3a560"></a> uint32\_t frame\_cnt
    :   self-arraged frame counter

<a id="_CPPv412lm_trigger_t"></a>

<a id="_CPPv312lm_trigger_t"></a> <a id="_CPPv212lm_trigger_t"></a> <a id="lm_trigger_t"></a> <a id="structlm__trigger__t"></a> struct lm\_trigger\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N12lm_trigger_t8cmd_codeE"></a>

    <a id="_CPPv3N12lm_trigger_t8cmd_codeE"></a> <a id="_CPPv2N12lm_trigger_t8cmd_codeE"></a> <a id="lm_trigger_t::cmd_code__uint16_t"></a> <a id="structlm__trigger__t_1a2a52074e77417be3f74bb90ef566e0f5"></a> uint16\_t cmd\_code
    :   private command code example (TWS\_LOCAL\_MEDIA\_TRIGGER)

    <a id="_CPPv4N12lm_trigger_t10async_pathE"></a>

    <a id="_CPPv3N12lm_trigger_t10async_pathE"></a> <a id="_CPPv2N12lm_trigger_t10async_pathE"></a> <a id="lm_trigger_t::async_path__uint8_t"></a> <a id="structlm__trigger__t_1aa649f9db37eb82c042486787d41f95b2"></a> uint8\_t async\_path
    :   async path

    <a id="_CPPv4N12lm_trigger_t11trigger_clkE"></a>

    <a id="_CPPv3N12lm_trigger_t11trigger_clkE"></a> <a id="_CPPv2N12lm_trigger_t11trigger_clkE"></a> <a id="lm_trigger_t::trigger_clk__bt_clk_t"></a> <a id="structlm__trigger__t_1aa7c292f7627675c039009a82e99ce248"></a> bt\_clk\_t trigger\_clk
    :   trigger clock

    <a id="_CPPv4N12lm_trigger_t7hint_idE"></a>

    <a id="_CPPv3N12lm_trigger_t7hint_idE"></a> <a id="_CPPv2N12lm_trigger_t7hint_idE"></a> <a id="lm_trigger_t::hint_id__uint8_t"></a> <a id="structlm__trigger__t_1a7bcbb04ef635c73cb04796590785a313"></a> uint8\_t hint\_id
    :   hint music id

<a id="macros"></a>

### Macros

<a id="c.TRIGGER_CLK_DELTA_TIME"></a>

<a id="app__audio__sync_8h_1a5ee6bcfc9c2f24c72d71057cdde121f4"></a> TRIGGER\_CLK\_DELTA\_TIME
:   unit : ms

<a id="c.TRIGGER_CLK_SBC_DELTA_TIME"></a>

<a id="app__audio__sync_8h_1a903936e6ff0dc94f4fbf131c58f7062e"></a> TRIGGER\_CLK\_SBC\_DELTA\_TIME
:   unit : ms

<a id="c.TRIGGER_CLK_TWS_HINTS_DELTA_TIME"></a>

<a id="app__audio__sync_8h_1abc324d5ee1f55f69c7881a557f549282"></a> TRIGGER\_CLK\_TWS\_HINTS\_DELTA\_TIME
:   unit : ms

<a id="c.TRIGGER_CLK_CONNECT_HINTS_DELTA_TIME"></a>

<a id="app__audio__sync_8h_1a3d247393a19816736983cf654cc5c183"></a> TRIGGER\_CLK\_CONNECT\_HINTS\_DELTA\_TIME
:   unit : ms

<a id="c.TRIGGER_CLK_HINTS_DELTA_TIME"></a>

<a id="app__audio__sync_8h_1a24ccce351881f1adbcc3ca489c09e8c1"></a> TRIGGER\_CLK\_HINTS\_DELTA\_TIME
:   unit : ms

<a id="c.ASYNC_TRIGGER_INFO_MAX"></a>

<a id="app__audio__sync_8h_1a13069aceee252e6f9a23f000bc21e895"></a> ASYNC\_TRIGGER\_INFO\_MAX

<a id="c.RETRIGGER_DISCARD_PAC"></a>

<a id="app__audio__sync_8h_1a46d05ea81dc65df113ac64f27d868333"></a> RETRIGGER\_DISCARD\_PAC
:   packet num

<a id="c.JOIN_PACKET_DIFF_LIMIT_MIN"></a>

<a id="app__audio__sync_8h_1a8a113c68f11d624b5c7013db8888710d"></a> JOIN\_PACKET\_DIFF\_LIMIT\_MIN
:   packet num

<a id="c.RETRIGGER_BUFF_TIME"></a>

<a id="app__audio__sync_8h_1a310589f00619ae2162072bad7474f47b"></a> RETRIGGER\_BUFF\_TIME
:   half slots(96\*0.3125 \= 30ms)

<a id="c.RETRIGGER_DELTA_HS"></a>

<a id="app__audio__sync_8h_1a289e93b4c84ae9f96d2ce16ed17503e1"></a> RETRIGGER\_DELTA\_HS
:   half slots(32\*0.3125 \= 10ms)

<a id="c.RESYNC_RETRIGGER_BUFF_TIME"></a>

<a id="app__audio__sync_8h_1a067f52ddf89b133a3180fe5618baa16b"></a> RESYNC\_RETRIGGER\_BUFF\_TIME
:   half slots(192\*0.3125 \= 60ms)

<a id="c.RESYNC_RETRIGGER_DELTA_HS"></a>

<a id="app__audio__sync_8h_1a4478bdba5374b8f77200fb1103e54725"></a> RESYNC\_RETRIGGER\_DELTA\_HS
:   half slots(6\*0.3125 \= 1.875ms)

<a id="c.INVALID_CLK_HS"></a>

<a id="app__audio__sync_8h_1adf9239dd65d790dad3b9bf95853cf4b3"></a> INVALID\_CLK\_HS

<a id="c.ASYNC_DAC_ISR_INTERVAL"></a>

<a id="app__audio__sync_8h_1a4463a8ca16fea393c71ac4cb3b18bf05"></a> ASYNC\_DAC\_ISR\_INTERVAL

<a id="c.ASYNC_FINE_TUNE_LIMIT"></a>

<a id="app__audio__sync_8h_1af6ec5c4dc37d1b08b757733f59d865d0"></a> ASYNC\_FINE\_TUNE\_LIMIT
:   half us

<a id="c.APLL_FINE_TUNE_COEF"></a>

<a id="app__audio__sync_8h_1a235a9dcddd0295afa299ae6d6c2604c3"></a> APLL\_FINE\_TUNE\_COEF

<a id="c.PLAYBACK_INFO_TIMEOUT"></a>

<a id="app__audio__sync_8h_1a7727eff5d5bc08c24c7d73b68aedfc6b"></a> PLAYBACK\_INFO\_TIMEOUT
:   ms record 400ms history

<a id="c.ASYNC_DMA_INFO_MAX"></a>

<a id="app__audio__sync_8h_1a248ea3e32cc6810f2413c1c1a2338a30"></a> ASYNC\_DMA\_INFO\_MAX

<a id="c.ASYNC_FINE_TUNE_MAX"></a>

<a id="app__audio__sync_8h_1afc8a31119e6c0698922faab12577151a"></a> ASYNC\_FINE\_TUNE\_MAX

<a id="c.ASYNC_DIFF_HUS_MAX"></a>

<a id="app__audio__sync_8h_1a64d5c675baf6d13c2948524a0e5d8685"></a> ASYNC\_DIFF\_HUS\_MAX

<a id="c.JOIN_TRIGGER_DELTA_TIME"></a>

<a id="app__audio__sync_8h_1a54bd4bd484b2be328029ff6f8f400cb3"></a> JOIN\_TRIGGER\_DELTA\_TIME
:   not used

<a id="c.AUDIO_ISR_CNT_CYCLE"></a>

<a id="app__audio__sync_8h_1a02187b2aac1fbd223b62452bcb5f4da5"></a> AUDIO\_ISR\_CNT\_CYCLE

<a id="c.AUDIO_ISR_SAMPLES_PER_ISR"></a>

<a id="app__audio__sync_8h_1a7a2fc402d988cb9e65c55ee7ab7cf21c"></a> AUDIO\_ISR\_SAMPLES\_PER\_ISR

<a id="c.AUDIO_DIFF_MASK"></a>

<a id="app__audio__sync_8h_1a1ef7ac93a415df64eab091a7e773c834"></a> AUDIO\_DIFF\_MASK

<a id="c.AUDIO_DIFF_INTER"></a>

<a id="app__audio__sync_8h_1aed3f1d2decdb5d5b0c532353028c84ce"></a> AUDIO\_DIFF\_INTER

<a id="c.AUDIO_SUB"></a>

<a id="app__audio__sync_8h_1a44d57e90d6b126e610d69458642c6f86"></a> AUDIO\_SUB(a, b)
