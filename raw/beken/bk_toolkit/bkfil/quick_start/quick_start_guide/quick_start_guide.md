---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_app/bkfil_v4/zh_CN/latest/quick_start/quick_start_guide/quick_start_guide.html
sdk_family: bk_toolkit
chip: ''
processor: ''
sdk_version: latest
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 硬件准备

在开始之前，请确保您已准备好以下硬件：

- 1条 UART 串口线
- 1块 USB转串口底板
- 1片 待下载芯片
- 1台 电脑

备注

- Beken芯片默认是uart0烧录
- 部分开发板如AI开发板，已经板载了USB转串口芯片，无需额外准备串口底板

<a id="id6"></a>
[![../../_images/port_baseboard_1.png](../../../../_assets/55ee3a1afa48b8fa3552-port_baseboard_1.png)](../../../../_assets/55ee3a1afa48b8fa3552-port_baseboard_1.png)


串口底板

<a id="id7"></a>
[![../../_images/port_baseboard_2.png](../../../../_assets/ee98251caee0f94891ac-port_baseboard_2.png)](../../../../_assets/ee98251caee0f94891ac-port_baseboard_2.png)


其他串口底板

<a id="id8"></a>
[![../../_images/port_baseboard_and_target_chip.png](../../../../_assets/19b89b8fa3006504c881-port_baseboard_and_target_chip.png)](../../../../_assets/19b89b8fa3006504c881-port_baseboard_and_target_chip.png)


串口底板和待下载芯片

<a id="id9"></a>
[![../../_images/port_baseboard_and_target_chip_and_pc.png](../../../../_assets/a58aecddc6af38228e04-port_baseboard_and_target_chip_and_pc.png)](../../../../_assets/a58aecddc6af38228e04-port_baseboard_and_target_chip_and_pc.png)


串口底板和待下载芯片和电脑

<a id="id2"></a>

# 软件准备

参考 [下载安装](../../download/download.md)

<a id="id3"></a>

# 烧录

1. 选择串口和波特率

[![../../_images/select_port_and_baud.png](../../../../_assets/66e260752210d6f73dc0-select_port_and_baud.png)](../../../../_assets/66e260752210d6f73dc0-select_port_and_baud.png)

2. 选择bin文件

[![../../_images/select_bin.png](../../../../_assets/3e5c99f3498b3891091a-select_bin.png)](../../../../_assets/3e5c99f3498b3891091a-select_bin.png)

3. 开始烧录

[![../../_images/download_start.png](../../../../_assets/9182c8df9b822bfc22ac-download_start.png)](../../../../_assets/9182c8df9b822bfc22ac-download_start.png)

[![../../_images/download_ing.png](../../../../_assets/a11b1d846aca1ccb08de-download_ing.png)](../../../../_assets/a11b1d846aca1ccb08de-download_ing.png)

4. 烧录完成

[![../../_images/download_success.png](../../../../_assets/1243f5a0f1d26081eb32-download_success.png)](../../../../_assets/1243f5a0f1d26081eb32-download_success.png)

<a id="id4"></a>

# 擦除

警告

擦除操作会清除指定区域内的所有数据，请谨慎操作。

1. 选择串口和波特率
2. 选择要擦除的区域

[![../../_images/erase_type.png](../../../../_assets/e4a971c2d06a5e3bb441-erase_type.png)](../../../../_assets/e4a971c2d06a5e3bb441-erase_type.png)

[![../../_images/erase_custom_area.png](../../../../_assets/135406708da56c265cdc-erase_custom_area.png)](../../../../_assets/135406708da56c265cdc-erase_custom_area.png)

3. 开始擦除

[![../../_images/erase.png](../../../../_assets/729b5360171103141987-erase.png)](../../../../_assets/729b5360171103141987-erase.png)

[![../../_images/erase_ing.png](../../../../_assets/7fa26f36d051f0a46278-erase_ing.png)](../../../../_assets/7fa26f36d051f0a46278-erase_ing.png)

4. 擦除完成

[![../../_images/erase_success.png](../../../../_assets/a7d20fc27a3a5f22c165-erase_success.png)](../../../../_assets/a7d20fc27a3a5f22c165-erase_success.png)

<a id="id5"></a>

# 读取

1. 选择串口和波特率
2. 选择读取区域

[![../../_images/read_type.png](../../../../_assets/819f3be6f68e23140eea-read_type.png)](../../../../_assets/819f3be6f68e23140eea-read_type.png)

[![../../_images/read_area.png](../../../../_assets/3478f93841657400b231-read_area.png)](../../../../_assets/3478f93841657400b231-read_area.png)

3. 开始读取

[![../../_images/read_ing.png](../../../../_assets/9fdb9c9ebb606859775e-read_ing.png)](../../../../_assets/9fdb9c9ebb606859775e-read_ing.png)

4. 读取完成

[![../../_images/read_success.png](../../../../_assets/1702ad321ef7027f4413-read_success.png)](../../../../_assets/1702ad321ef7027f4413-read_success.png)
