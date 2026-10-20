---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/driver/drv_bk24.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="drv-bk24"></a>

# DRV\_BK24

<a id="drv-bk24-api-status"></a>

## DRV\_BK24 API Status

| API |
| --- |
| [`drv_bk24_enable_pipe()`](#_CPPv420drv_bk24_enable_pipe7uint8_tb "drv_bk24_enable_pipe") |
| [`drv_bk24_config_TRX_channel()`](#_CPPv427drv_bk24_config_TRX_channel7uint8_t "drv_bk24_config_TRX_channel") |
| [`drv_bk24_tx_payload()`](#_CPPv419drv_bk24_tx_payloadP7uint8_t8uint16_t "drv_bk24_tx_payload") |
| [`drv_bk24_w_ack_payload()`](#_CPPv422drv_bk24_w_ack_payload7uint8_tP7uint8_t8uint16_t "drv_bk24_w_ack_payload") |
| [`drv_bk24_tx_payload_noack()`](#_CPPv425drv_bk24_tx_payload_noackP7uint8_t8uint16_t "drv_bk24_tx_payload_noack") |
| [`drv_bk24_switch_to_TX_mode()`](#_CPPv426drv_bk24_switch_to_TX_modev "drv_bk24_switch_to_TX_mode") |
| [`drv_bk24_switch_to_RX_mode()`](#_CPPv426drv_bk24_switch_to_RX_modev "drv_bk24_switch_to_RX_mode") |
| [`drv_bk24_init()`](#_CPPv413drv_bk24_init11bk24_isr_cb "drv_bk24_init") |
| [`drv_bk24_get_max_rx_width()`](#_CPPv425drv_bk24_get_max_rx_widthv "drv_bk24_get_max_rx_width") |
| [`drv_bk24_config_ARC()`](#_CPPv419drv_bk24_config_ARC7uint8_t "drv_bk24_config_ARC") |
| [`drv_bk24_enable_CE()`](#_CPPv418drv_bk24_enable_CEv "drv_bk24_enable_CE") |
| [`drv_bk24_disable_CE()`](#_CPPv419drv_bk24_disable_CEv "drv_bk24_disable_CE") |
| [`drv_bk24_flush_tx()`](#_CPPv417drv_bk24_flush_txv "drv_bk24_flush_tx") |
| [`drv_bk24_flush_rx()`](#_CPPv417drv_bk24_flush_rxv "drv_bk24_flush_rx") |
| [`drv_bk24_enable_long_packet_mode()`](#_CPPv432drv_bk24_enable_long_packet_modev "drv_bk24_enable_long_packet_mode") |
| [`drv_bk24_disable_long_packet_mode()`](#_CPPv433drv_bk24_disable_long_packet_modev "drv_bk24_disable_long_packet_mode") |
| [`drv_bk24_set_tx_clk()`](#_CPPv419drv_bk24_set_tx_clk8uint32_t8uint16_t "drv_bk24_set_tx_clk") |
| [`drv_bk24_set_rx_clk()`](#_CPPv419drv_bk24_set_rx_clk8uint32_t8uint16_t "drv_bk24_set_rx_clk") |
| [`drv_bk24_set_trx_bt_timer_en()`](#_CPPv428drv_bk24_set_trx_bt_timer_enb "drv_bk24_set_trx_bt_timer_en") |
| [`drv_bk24_switch_to_idle_mode()`](#_CPPv428drv_bk24_switch_to_idle_modev "drv_bk24_switch_to_idle_mode") |
| [`drv_bk24_pwr_up()`](#_CPPv415drv_bk24_pwr_upv "drv_bk24_pwr_up") |
| [`drv_bk24_pwr_down()`](#_CPPv417drv_bk24_pwr_downv "drv_bk24_pwr_down") |

<a id="drv-bk24-api-reference"></a>

## DRV\_BK24 API Reference

<a id="header-file"></a>

### Header File

- [driver/bk24/drv\_bk24.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/driver/bk24/drv_bk24.h)

<a id="functions"></a>

### Functions

<a id="_CPPv420drv_bk24_enable_pipe7uint8_tb"></a>

<a id="_CPPv320drv_bk24_enable_pipe7uint8_tb"></a> <a id="_CPPv220drv_bk24_enable_pipe7uint8_tb"></a> <a id="drv_bk24_enable_pipe__uint8_t.b"></a> <a id="drv__bk24_8h_1ad814cff19ca2745989dee8be83c6cd78"></a> void drv\_bk24\_enable\_pipe(uint8\_t pipe\_num, bool enable)

<a id="_CPPv427drv_bk24_config_TRX_channel7uint8_t"></a>

<a id="_CPPv327drv_bk24_config_TRX_channel7uint8_t"></a> <a id="_CPPv227drv_bk24_config_TRX_channel7uint8_t"></a> <a id="drv_bk24_config_TRX_channel__uint8_t"></a> <a id="drv__bk24_8h_1afc695392a2b3abafa4ee04daad823fb8"></a> void drv\_bk24\_config\_TRX\_channel(uint8\_t rf\_chan)

<a id="_CPPv419drv_bk24_tx_payloadP7uint8_t8uint16_t"></a>

<a id="_CPPv319drv_bk24_tx_payloadP7uint8_t8uint16_t"></a> <a id="_CPPv219drv_bk24_tx_payloadP7uint8_t8uint16_t"></a> <a id="drv_bk24_tx_payload__uint8_tP.uint16_t"></a> <a id="drv__bk24_8h_1a6d4041108dea17b6c2deb639eaee4c8d"></a> void drv\_bk24\_tx\_payload(uint8\_t \*p\_data, uint16\_t length)

<a id="_CPPv422drv_bk24_w_ack_payload7uint8_tP7uint8_t8uint16_t"></a>

<a id="_CPPv322drv_bk24_w_ack_payload7uint8_tP7uint8_t8uint16_t"></a> <a id="_CPPv222drv_bk24_w_ack_payload7uint8_tP7uint8_t8uint16_t"></a> <a id="drv_bk24_w_ack_payload__uint8_t.uint8_tP.uint16_t"></a> <a id="drv__bk24_8h_1a3b933db1bac0979f2f1d2d44e1d3bf73"></a> void drv\_bk24\_w\_ack\_payload(uint8\_t pipe\_num, uint8\_t \*p\_data, uint16\_t length)

<a id="_CPPv425drv_bk24_tx_payload_noackP7uint8_t8uint16_t"></a>

<a id="_CPPv325drv_bk24_tx_payload_noackP7uint8_t8uint16_t"></a> <a id="_CPPv225drv_bk24_tx_payload_noackP7uint8_t8uint16_t"></a> <a id="drv_bk24_tx_payload_noack__uint8_tP.uint16_t"></a> <a id="drv__bk24_8h_1a1cdb3953751bf78ab79391cffcce8682"></a> void drv\_bk24\_tx\_payload\_noack(uint8\_t \*p\_data, uint16\_t length)

<a id="_CPPv426drv_bk24_switch_to_TX_modev"></a>

<a id="_CPPv326drv_bk24_switch_to_TX_modev"></a> <a id="_CPPv226drv_bk24_switch_to_TX_modev"></a> <a id="drv_bk24_switch_to_TX_mode__void"></a> <a id="drv__bk24_8h_1aac5c4f4363b832426a814fd6568be438"></a> void drv\_bk24\_switch\_to\_TX\_mode(void)

<a id="_CPPv426drv_bk24_switch_to_RX_modev"></a>

<a id="_CPPv326drv_bk24_switch_to_RX_modev"></a> <a id="_CPPv226drv_bk24_switch_to_RX_modev"></a> <a id="drv_bk24_switch_to_RX_mode__void"></a> <a id="drv__bk24_8h_1aac5ca7c0d94ca077e24391f19fe9aa08"></a> void drv\_bk24\_switch\_to\_RX\_mode(void)

<a id="_CPPv413drv_bk24_init11bk24_isr_cb"></a>

<a id="_CPPv313drv_bk24_init11bk24_isr_cb"></a> <a id="_CPPv213drv_bk24_init11bk24_isr_cb"></a> <a id="drv_bk24_init__bk24_isr_cb"></a> <a id="drv__bk24_8h_1a7048cefc176a0f37e8757b0f0272b1e9"></a> void drv\_bk24\_init([bk24\_isr\_cb](#_CPPv411bk24_isr_cb "bk24_isr_cb") isr\_cb)

<a id="_CPPv425drv_bk24_get_max_rx_widthv"></a>

<a id="_CPPv325drv_bk24_get_max_rx_widthv"></a> <a id="_CPPv225drv_bk24_get_max_rx_widthv"></a> <a id="drv_bk24_get_max_rx_width__void"></a> <a id="drv__bk24_8h_1a1987e2447abec23e4ac3c6c66c1d267b"></a> uint16\_t drv\_bk24\_get\_max\_rx\_width(void)

<a id="_CPPv419drv_bk24_config_ARC7uint8_t"></a>

<a id="_CPPv319drv_bk24_config_ARC7uint8_t"></a> <a id="_CPPv219drv_bk24_config_ARC7uint8_t"></a> <a id="drv_bk24_config_ARC__uint8_t"></a> <a id="drv__bk24_8h_1a02c4089322550c8b89eb4f099875c9ab"></a> void drv\_bk24\_config\_ARC(uint8\_t arc)

<a id="_CPPv418drv_bk24_enable_CEv"></a>

<a id="_CPPv318drv_bk24_enable_CEv"></a> <a id="_CPPv218drv_bk24_enable_CEv"></a> <a id="drv_bk24_enable_CE__void"></a> <a id="drv__bk24_8h_1ab4086876e0086d2c0cc4e210ce23f0da"></a> void drv\_bk24\_enable\_CE(void)

<a id="_CPPv419drv_bk24_disable_CEv"></a>

<a id="_CPPv319drv_bk24_disable_CEv"></a> <a id="_CPPv219drv_bk24_disable_CEv"></a> <a id="drv_bk24_disable_CE__void"></a> <a id="drv__bk24_8h_1a168f8e251d8e611e878d227701dd05c4"></a> void drv\_bk24\_disable\_CE(void)

<a id="_CPPv417drv_bk24_flush_txv"></a>

<a id="_CPPv317drv_bk24_flush_txv"></a> <a id="_CPPv217drv_bk24_flush_txv"></a> <a id="drv_bk24_flush_tx__void"></a> <a id="drv__bk24_8h_1ac21a7b0b27f8aa0de03078aa3a730c3c"></a> void drv\_bk24\_flush\_tx(void)

<a id="_CPPv417drv_bk24_flush_rxv"></a>

<a id="_CPPv317drv_bk24_flush_rxv"></a> <a id="_CPPv217drv_bk24_flush_rxv"></a> <a id="drv_bk24_flush_rx__void"></a> <a id="drv__bk24_8h_1aa45c8bac696933dc5285154aa76cb4ef"></a> void drv\_bk24\_flush\_rx(void)

<a id="_CPPv432drv_bk24_enable_long_packet_modev"></a>

<a id="_CPPv332drv_bk24_enable_long_packet_modev"></a> <a id="_CPPv232drv_bk24_enable_long_packet_modev"></a> <a id="drv_bk24_enable_long_packet_mode__void"></a> <a id="drv__bk24_8h_1aed79eefad11ee119fc934299efcf2812"></a> void drv\_bk24\_enable\_long\_packet\_mode(void)

<a id="_CPPv433drv_bk24_disable_long_packet_modev"></a>

<a id="_CPPv333drv_bk24_disable_long_packet_modev"></a> <a id="_CPPv233drv_bk24_disable_long_packet_modev"></a> <a id="drv_bk24_disable_long_packet_mode__void"></a> <a id="drv__bk24_8h_1aa651978cd215feadab9e550fff4723da"></a> void drv\_bk24\_disable\_long\_packet\_mode(void)

<a id="_CPPv419drv_bk24_set_tx_clk8uint32_t8uint16_t"></a>

<a id="_CPPv319drv_bk24_set_tx_clk8uint32_t8uint16_t"></a> <a id="_CPPv219drv_bk24_set_tx_clk8uint32_t8uint16_t"></a> <a id="drv_bk24_set_tx_clk__uint32_t.uint16_t"></a> <a id="drv__bk24_8h_1a4682fcdbbd25ff2df0493b28e57e3165"></a> void drv\_bk24\_set\_tx\_clk(uint32\_t clk\_hst, uint16\_t fine\_cnt)

<a id="_CPPv419drv_bk24_set_rx_clk8uint32_t8uint16_t"></a>

<a id="_CPPv319drv_bk24_set_rx_clk8uint32_t8uint16_t"></a> <a id="_CPPv219drv_bk24_set_rx_clk8uint32_t8uint16_t"></a> <a id="drv_bk24_set_rx_clk__uint32_t.uint16_t"></a> <a id="drv__bk24_8h_1af3feb9c0b6de34dd336196e21e3c59be"></a> void drv\_bk24\_set\_rx\_clk(uint32\_t clk\_hst, uint16\_t fine\_cnt)

<a id="_CPPv428drv_bk24_set_trx_bt_timer_enb"></a>

<a id="_CPPv328drv_bk24_set_trx_bt_timer_enb"></a> <a id="_CPPv228drv_bk24_set_trx_bt_timer_enb"></a> <a id="drv_bk24_set_trx_bt_timer_en__b"></a> <a id="drv__bk24_8h_1a1cb05ff87efc1795c8ec2c7ace5d23a1"></a> void drv\_bk24\_set\_trx\_bt\_timer\_en(bool enable)

<a id="_CPPv428drv_bk24_switch_to_idle_modev"></a>

<a id="_CPPv328drv_bk24_switch_to_idle_modev"></a> <a id="_CPPv228drv_bk24_switch_to_idle_modev"></a> <a id="drv_bk24_switch_to_idle_mode__void"></a> <a id="drv__bk24_8h_1a02c49fa92329f0c21a4d4281b0a9209f"></a> void drv\_bk24\_switch\_to\_idle\_mode(void)

<a id="_CPPv415drv_bk24_pwr_upv"></a>

<a id="_CPPv315drv_bk24_pwr_upv"></a> <a id="_CPPv215drv_bk24_pwr_upv"></a> <a id="drv_bk24_pwr_up__void"></a> <a id="drv__bk24_8h_1af989027925c608796512ecb0ec8b2f6b"></a> void drv\_bk24\_pwr\_up(void)

<a id="_CPPv417drv_bk24_pwr_downv"></a>

<a id="_CPPv317drv_bk24_pwr_downv"></a> <a id="_CPPv217drv_bk24_pwr_downv"></a> <a id="drv_bk24_pwr_down__void"></a> <a id="drv__bk24_8h_1ae3dc4d057864e6ff6b2d158a02f552ce"></a> void drv\_bk24\_pwr\_down(void)

<a id="macros"></a>

### Macros

<a id="c.BK24_DR_ISR"></a>

<a id="drv__bk24_8h_1a13f4eb2ed124c708558aa6e0886e1e10"></a> BK24\_DR\_ISR

<a id="c.BK24_TS_ISR"></a>

<a id="drv__bk24_8h_1a7497183c56ec5f946f1f1da9502656af"></a> BK24\_TS\_ISR

<a id="c.BK24_RET_MAX"></a>

<a id="drv__bk24_8h_1acb21759c4a9acef01a87acccbf6aaa39"></a> BK24\_RET\_MAX

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv411bk24_isr_cb"></a>

<a id="_CPPv311bk24_isr_cb"></a> <a id="_CPPv211bk24_isr_cb"></a> <a id="bk24_isr_cb"></a> <a id="drv__bk24_8h_1a899dee933f71058cff586a15108ff87d"></a> typedef void (\*bk24\_isr\_cb)(uint8\_t isr\_type, uint8\_t \*p\_data, uint32\_t length)
