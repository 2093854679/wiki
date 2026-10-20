---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_bluelink/bk7258/zh_CN/v2.0.1/projects/wearable/storage.html
sdk_family: bk_bluelink
chip: BK7258
processor: ''
sdk_version: v2.0.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="bluetooth-storage"></a>

# bluetooth\_storage 使用说明

bluetooth\_storage 模块为用户提供了一套管理蓝牙数据存储(包括 LinkKey, address, bonded device info 等信息) 的API

<a id="api-reference"></a>

## API Reference

<a id="header-file"></a>

### Header File

- [bluetooth\_storage.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/bluetooth_storage.h)

<a id="functions"></a>

### Functions

<a id="_CPPv422bluetooth_storage_initv"></a>

<a id="_CPPv322bluetooth_storage_initv"></a> <a id="_CPPv222bluetooth_storage_initv"></a> <a id="bluetooth_storage_init__void"></a> <a id="bluetooth__storage_8h_1a926b0de69de14d5b18027e8405c56cb5"></a> int32\_t bluetooth\_storage\_init(void)
:   Initialize the Bluetooth storage module.

    返回
    :   - int32\_t: 0 on success, other values on failure.

<a id="_CPPv424bluetooth_storage_deinitv"></a>

<a id="_CPPv324bluetooth_storage_deinitv"></a> <a id="_CPPv224bluetooth_storage_deinitv"></a> <a id="bluetooth_storage_deinit__void"></a> <a id="bluetooth__storage_8h_1afd6ca3cbd1c58320001ac7e26669aecf"></a> int32\_t bluetooth\_storage\_deinit(void)
:   Deinitialize the Bluetooth storage module.

    返回
    :   - int32\_t: 0 on success, other values on failure.

<a id="_CPPv441bluetooth_storage_find_linkkey_info_indexP7uint8_tP7uint8_t"></a>

<a id="_CPPv341bluetooth_storage_find_linkkey_info_indexP7uint8_tP7uint8_t"></a> <a id="_CPPv241bluetooth_storage_find_linkkey_info_indexP7uint8_tP7uint8_t"></a> <a id="bluetooth_storage_find_linkkey_info_index__uint8_tP.uint8_tP"></a> <a id="bluetooth__storage_8h_1a7ab9ceb25c342f8466e802bcd5dfe491"></a> int32\_t bluetooth\_storage\_find\_linkkey\_info\_index(uint8\_t \*addr, uint8\_t \*key)
:   Find the index of link key information based on the device address.

    参数
    :   - **addr** – Pointer to the device address.
        - **key** – **\[out\]** Pointer to the link key.

    返回
    :   - int32\_t: Index of the link key information if found, negative value if not found.

<a id="_CPPv435bluetooth_storage_save_linkkey_infoP7uint8_tP7uint8_t"></a>

<a id="_CPPv335bluetooth_storage_save_linkkey_infoP7uint8_tP7uint8_t"></a> <a id="_CPPv235bluetooth_storage_save_linkkey_infoP7uint8_tP7uint8_t"></a> <a id="bluetooth_storage_save_linkkey_info__uint8_tP.uint8_tP"></a> <a id="bluetooth__storage_8h_1a736be064ec8268fb0decb265dc750fde"></a> int32\_t bluetooth\_storage\_save\_linkkey\_info(uint8\_t \*addr, uint8\_t \*key)
:   Save link key information.

    参数
    :   - **addr** – Pointer to the device address.
        - **key** – Pointer to the link key.

    返回
    :   - int32\_t: 0 on success, other values on failure.

<a id="_CPPv434bluetooth_storage_del_linkkey_infoP7uint8_t"></a>

<a id="_CPPv334bluetooth_storage_del_linkkey_infoP7uint8_t"></a> <a id="_CPPv234bluetooth_storage_del_linkkey_infoP7uint8_t"></a> <a id="bluetooth_storage_del_linkkey_info__uint8_tP"></a> <a id="bluetooth__storage_8h_1a66882d56122bb72403571e7153b3b3e3"></a> int32\_t bluetooth\_storage\_del\_linkkey\_info(uint8\_t \*addr)
:   Delete link key information based on the device address.

    参数
    :   **addr** – Pointer to the device address.

    返回
    :   - int32\_t: 0 on success, other values on failure.

<a id="_CPPv434bluetooth_storage_update_to_newestP7uint8_t"></a>

<a id="_CPPv334bluetooth_storage_update_to_newestP7uint8_t"></a> <a id="_CPPv234bluetooth_storage_update_to_newestP7uint8_t"></a> <a id="bluetooth_storage_update_to_newest__uint8_tP"></a> <a id="bluetooth__storage_8h_1a8490d47c804e6c4640c6a10f5786b0ed"></a> int32\_t bluetooth\_storage\_update\_to\_newest(uint8\_t \*addr)
:   Update the link key information to the latest based on the device address.

    参数
    :   **addr** – Pointer to the device address.

    返回
    :   - int32\_t: 0 on success, other values on failure.

<a id="_CPPv441bluetooth_storage_get_newest_linkkey_infoP7uint8_tP7uint8_t"></a>

<a id="_CPPv341bluetooth_storage_get_newest_linkkey_infoP7uint8_tP7uint8_t"></a> <a id="_CPPv241bluetooth_storage_get_newest_linkkey_infoP7uint8_tP7uint8_t"></a> <a id="bluetooth_storage_get_newest_linkkey_info__uint8_tP.uint8_tP"></a> <a id="bluetooth__storage_8h_1af84a1446c9624c8792cb056edc8b66ca"></a> int32\_t bluetooth\_storage\_get\_newest\_linkkey\_info(uint8\_t \*addr, uint8\_t \*key)
:   Get the latest link key information.

    参数
    :   - **addr** – Pointer to store the device address.
        - **key** – **\[out\]** Pointer to store the link key.

    返回
    :   - int32\_t: 0 on success, other values on failure.

<a id="_CPPv436bluetooth_storage_clean_linkkey_infov"></a>

<a id="_CPPv336bluetooth_storage_clean_linkkey_infov"></a> <a id="_CPPv236bluetooth_storage_clean_linkkey_infov"></a> <a id="bluetooth_storage_clean_linkkey_info__void"></a> <a id="bluetooth__storage_8h_1ab5408f1f2cc4e72662038a959adf0ee1"></a> int32\_t bluetooth\_storage\_clean\_linkkey\_info(void)
:   Clear all link key information.

    返回
    :   - int32\_t: 0 on success, other values on failure.

<a id="_CPPv431bluetooth_storage_sync_to_flashv"></a>

<a id="_CPPv331bluetooth_storage_sync_to_flashv"></a> <a id="_CPPv231bluetooth_storage_sync_to_flashv"></a> <a id="bluetooth_storage_sync_to_flash__void"></a> <a id="bluetooth__storage_8h_1a69c05551ca0d8abc3bac14e7171403ee"></a> int32\_t bluetooth\_storage\_sync\_to\_flash(void)
:   Synchronize the storage data to the flash memory.

    返回
    :   - int32\_t: 0 on success, other values on failure.

<a id="_CPPv431bluetooth_storage_linkkey_debugv"></a>

<a id="_CPPv331bluetooth_storage_linkkey_debugv"></a> <a id="_CPPv231bluetooth_storage_linkkey_debugv"></a> <a id="bluetooth_storage_linkkey_debug__void"></a> <a id="bluetooth__storage_8h_1a0242a93b90209a965df9acfe78fff57e"></a> int32\_t bluetooth\_storage\_linkkey\_debug(void)
:   Debug the link key information.

    返回
    :   - int32\_t: 0 on success, other values on failure.

<a id="_CPPv437bluetooth_storage_find_volume_by_addrP7uint8_tP7uint8_t"></a>

<a id="_CPPv337bluetooth_storage_find_volume_by_addrP7uint8_tP7uint8_t"></a> <a id="_CPPv237bluetooth_storage_find_volume_by_addrP7uint8_tP7uint8_t"></a> <a id="bluetooth_storage_find_volume_by_addr__uint8_tP.uint8_tP"></a> <a id="bluetooth__storage_8h_1a28114ec9374058244fe95ce9b7d4255e"></a> int32\_t bluetooth\_storage\_find\_volume\_by\_addr(uint8\_t \*addr, uint8\_t \*volume)
:   Find the A2DP volume value based on the device address.

    参数
    :   - **addr** – Pointer to the device address.
        - **volume** – **\[out\]** Pointer to store the A2DP volume value.

    返回
    :   - int32\_t: 0 on success, other values on failure.

<a id="_CPPv429bluetooth_storage_save_volumeP7uint8_t7uint8_t"></a>

<a id="_CPPv329bluetooth_storage_save_volumeP7uint8_t7uint8_t"></a> <a id="_CPPv229bluetooth_storage_save_volumeP7uint8_t7uint8_t"></a> <a id="bluetooth_storage_save_volume__uint8_tP.uint8_t"></a> <a id="bluetooth__storage_8h_1acdab3d866ceb33478fa256a9415e70e4"></a> int32\_t bluetooth\_storage\_save\_volume(uint8\_t \*addr, uint8\_t volume)
:   Save the A2DP volume value based on the device address.

    参数
    :   - **addr** – Pointer to the device address.
        - **volume** – A2DP volume value to be saved.

    返回
    :   - int32\_t: 0 on success, other values on failure.

<a id="structures"></a>

### Structures

<a id="_CPPv430bt_user_storage_elem_linkkey_t"></a>

<a id="_CPPv330bt_user_storage_elem_linkkey_t"></a> <a id="_CPPv230bt_user_storage_elem_linkkey_t"></a> <a id="bt_user_storage_elem_linkkey_t"></a> <a id="structbt__user__storage__elem__linkkey__t"></a> struct bt\_user\_storage\_elem\_linkkey\_t
:   Define the structure of link key elements for Bluetooth user storage. Use the packed attribute to ensure byte \- compact arrangement.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N30bt_user_storage_elem_linkkey_t4addrE"></a>

    <a id="_CPPv3N30bt_user_storage_elem_linkkey_t4addrE"></a> <a id="_CPPv2N30bt_user_storage_elem_linkkey_t4addrE"></a> <a id="bt_user_storage_elem_linkkey_t::addr__uint8_tA"></a> <a id="structbt__user__storage__elem__linkkey__t_1afc05b07b54e70cc296a4c8f4d69cd0da"></a> uint8\_t addr\[6\]
    :   Device address, with a length of 6 bytes.

    <a id="_CPPv4N30bt_user_storage_elem_linkkey_t8link_keyE"></a>

    <a id="_CPPv3N30bt_user_storage_elem_linkkey_t8link_keyE"></a> <a id="_CPPv2N30bt_user_storage_elem_linkkey_t8link_keyE"></a> <a id="bt_user_storage_elem_linkkey_t::link_key__uint8_tA"></a> <a id="structbt__user__storage__elem__linkkey__t_1a5ae8670af65940ab5b8721bca1aed948"></a> uint8\_t link\_key\[16\]
    :   Link key, with a length of 16 bytes.

    <a id="_CPPv4N30bt_user_storage_elem_linkkey_t11a2dp_volumeE"></a>

    <a id="_CPPv3N30bt_user_storage_elem_linkkey_t11a2dp_volumeE"></a> <a id="_CPPv2N30bt_user_storage_elem_linkkey_t11a2dp_volumeE"></a> <a id="bt_user_storage_elem_linkkey_t::a2dp_volume__uint8_t"></a> <a id="structbt__user__storage__elem__linkkey__t_1ab3c0a838702c1f73b8725083af31bc46"></a> uint8\_t a2dp\_volume
    :   A2DP volume value.

<a id="_CPPv417bt_user_storage_t"></a>

<a id="_CPPv317bt_user_storage_t"></a> <a id="_CPPv217bt_user_storage_t"></a> <a id="bt_user_storage_t"></a> <a id="structbt__user__storage__t"></a> struct bt\_user\_storage\_t
:   Define the structure of Bluetooth user storage. Use the packed attribute to ensure byte \- compact arrangement.

    <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N17bt_user_storage_t7linkkeyE"></a>

    <a id="_CPPv3N17bt_user_storage_t7linkkeyE"></a> <a id="_CPPv2N17bt_user_storage_t7linkkeyE"></a> <a id="bt_user_storage_t::linkkey__bt_user_storage_elem_linkkey_tA"></a> <a id="structbt__user__storage__t_1abb3340c34ac2b1e3398a4ff4509f448b"></a> [bt\_user\_storage\_elem\_linkkey\_t](#_CPPv430bt_user_storage_elem_linkkey_t "bt_user_storage_elem_linkkey_t") linkkey\[BT\_LINKKEY\_MAX\_SAVE\_COUNT\]
    :   Array to store link key information, with a quantity of BT\_LINKKEY\_MAX\_SAVE\_COUNT.

<a id="macros"></a>

### Macros

<a id="c.BT_STORAGE_KEY"></a>

<a id="bluetooth__storage_8h_1adae9eded8ad79b9d8b4b75d53861b628"></a> BT\_STORAGE\_KEY
:   Define the key name for Bluetooth user information storage.

<a id="c.BT_LINKKEY_MAX_SAVE_COUNT"></a>

<a id="bluetooth__storage_8h_1ac484124b075d2d971d0784b3e21bac0a"></a> BT\_LINKKEY\_MAX\_SAVE\_COUNT
:   Define the maximum number of link keys that can be saved.
