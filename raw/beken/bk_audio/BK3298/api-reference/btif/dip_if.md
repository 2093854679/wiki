---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_audio/bk3298/zh_CN/latest/api-reference/btif/dip_if.html
sdk_family: bk_audio
chip: BK3298
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="dip-interface-functions"></a>

# DIP Interface Functions

<a id="dip-if-api-reference"></a>

## DIP\_IF API Reference

<a id="header-file"></a>

### Header File

- [btif/inc/dip\_if.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/btif/inc/dip_if.h)

<a id="structures"></a>

### Structures

<a id="_CPPv422btif_dip_inquiry_pkt_t"></a>

<a id="_CPPv322btif_dip_inquiry_pkt_t"></a> <a id="_CPPv222btif_dip_inquiry_pkt_t"></a> <a id="btif_dip_inquiry_pkt_t"></a> <a id="structbtif__dip__inquiry__pkt__t"></a> struct btif\_dip\_inquiry\_pkt\_t
:   DIP inquiry packet struct definition.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N22btif_dip_inquiry_pkt_t4addrE"></a>

    <a id="_CPPv3N22btif_dip_inquiry_pkt_t4addrE"></a> <a id="_CPPv2N22btif_dip_inquiry_pkt_t4addrE"></a> <a id="btif_dip_inquiry_pkt_t::addr__btif_bd_addr_t"></a> <a id="structbtif__dip__inquiry__pkt__t_1af76d127c6033abdaf460170872e18ba3"></a> [btif\_bd\_addr\_t](btif_type.md#_CPPv414btif_bd_addr_t "btif_bd_addr_t") addr
    :   remote BT MAC address

    <a id="_CPPv4N22btif_dip_inquiry_pkt_t6statusE"></a>

    <a id="_CPPv3N22btif_dip_inquiry_pkt_t6statusE"></a> <a id="_CPPv2N22btif_dip_inquiry_pkt_t6statusE"></a> <a id="btif_dip_inquiry_pkt_t::status__uint8_t"></a> <a id="structbtif__dip__inquiry__pkt__t_1a0bbf65a9e2cf235f60f57895ca0fa88c"></a> uint8\_t status
    :   status @btif\_ret\_t

    <a id="_CPPv4N22btif_dip_inquiry_pkt_t8dev_infoE"></a>

    <a id="_CPPv3N22btif_dip_inquiry_pkt_t8dev_infoE"></a> <a id="_CPPv2N22btif_dip_inquiry_pkt_t8dev_infoE"></a> <a id="btif_dip_inquiry_pkt_t::dev_info__btif_dip_dev_info_t"></a> <a id="structbtif__dip__inquiry__pkt__t_1a2e167508fa0dc8e45366ea765a8de9a4"></a> [btif\_dip\_dev\_info\_t](btif_type.md#_CPPv419btif_dip_dev_info_t "btif_dip_dev_info_t") dev\_info
    :   remote device information

<a id="_CPPv423btif_dip_evt_register_t"></a>

<a id="_CPPv323btif_dip_evt_register_t"></a> <a id="_CPPv223btif_dip_evt_register_t"></a> <a id="btif_dip_evt_register_t"></a> <a id="structbtif__dip__evt__register__t"></a> struct btif\_dip\_evt\_register\_t
:   callback struct definition

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N23btif_dip_evt_register_t9dlst_nodeE"></a>

    <a id="_CPPv3N23btif_dip_evt_register_t9dlst_nodeE"></a> <a id="_CPPv2N23btif_dip_evt_register_t9dlst_nodeE"></a> <a id="btif_dip_evt_register_t::dlst_node__dl_list_t"></a> <a id="structbtif__dip__evt__register__t_1ae4ec6610290905f4b0cdd59cbbfd2567"></a> dl\_list\_t dlst\_node
    :   node for application handler will be linked to orthers

    <a id="_CPPv4N23btif_dip_evt_register_t10cb_handlerE"></a>

    <a id="_CPPv3N23btif_dip_evt_register_t10cb_handlerE"></a> <a id="_CPPv2N23btif_dip_evt_register_t10cb_handlerE"></a> <a id="btif_dip_evt_register_t::cb_handler__dip_if_evt_cb_pfn"></a> <a id="structbtif__dip__evt__register__t_1ab290366d4d71502d098baba1e41757c6"></a> [dip\_if\_evt\_cb\_pfn](#_CPPv417dip_if_evt_cb_pfn "dip_if_evt_cb_pfn") cb\_handler
    :   function pointer for callback function

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv417dip_if_evt_cb_pfn"></a>

<a id="_CPPv317dip_if_evt_cb_pfn"></a> <a id="_CPPv217dip_if_evt_cb_pfn"></a> <a id="dip_if_evt_cb_pfn"></a> <a id="dip__if_8h_1a1d24c06a6fae0e52594d36cb4d97ed61"></a> typedef void (\*dip\_if\_evt\_cb\_pfn)([btif\_dip\_inquiry\_pkt\_t](#_CPPv422btif_dip_inquiry_pkt_t "btif_dip_inquiry_pkt_t") \*p\_pkt)
