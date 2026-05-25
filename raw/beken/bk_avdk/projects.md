# 参考工程[](#id1 "永久链接至标题")



- [蓝牙(Bluetooth)工程](bluetooth/index.md "bluetooth/index.md")

  - [中控(Central)](bluetooth/central/index.md "bluetooth/central/index.md")

    - [1 功能概述](bluetooth/central/index.md#id1 "bluetooth/central/index.md#id1")

      - [1.1 软件规格](bluetooth/central/index.md#id2 "bluetooth/central/index.md#id2")

      - [1.2 代码路径及编译命令](bluetooth/central/index.md#id3 "bluetooth/central/index.md#id3")

    - [2 cmd命令简介](bluetooth/central/index.md#cmd "bluetooth/central/index.md#cmd")

      - [2.1 a2dp source](bluetooth/central/index.md#a2dp-source "bluetooth/central/index.md#a2dp-source")

      - [2.2 ble gatt](bluetooth/central/index.md#ble-gatt "bluetooth/central/index.md#ble-gatt")

    - [3 a2dp source 测试](bluetooth/central/index.md#id4 "bluetooth/central/index.md#id4")

      - [3.1 测试过程](bluetooth/central/index.md#id5 "bluetooth/central/index.md#id5")

      - [3.2 兼容性说明](bluetooth/central/index.md#id6 "bluetooth/central/index.md#id6")

      - [3.3 其他注意事项](bluetooth/central/index.md#id7 "bluetooth/central/index.md#id7")

    - [4 ble gatt 测试](bluetooth/central/index.md#id8 "bluetooth/central/index.md#id8")

      - [4.1 单板作为client与手机连接测试](bluetooth/central/index.md#client "bluetooth/central/index.md#client")

      - [4.2 双板对测](bluetooth/central/index.md#id9 "bluetooth/central/index.md#id9")

    - [5 结构图](bluetooth/central/index.md#id10 "bluetooth/central/index.md#id10")

      - [5.1 运行时](bluetooth/central/index.md#id11 "bluetooth/central/index.md#id11")

      - [5.2 流程图](bluetooth/central/index.md#id12 "bluetooth/central/index.md#id12")

    - [6 重要流程说明](bluetooth/central/index.md#id13 "bluetooth/central/index.md#id13")

      - [6.1 连接音响](bluetooth/central/index.md#id14 "bluetooth/central/index.md#id14")

      - [6.2 mp3解码](bluetooth/central/index.md#mp3 "bluetooth/central/index.md#mp3")

      - [6.3 host a2dp 取数回调(pcm)](bluetooth/central/index.md#host-a2dp-pcm "bluetooth/central/index.md#host-a2dp-pcm")

      - [6.3 host a2dp 重采样回调](bluetooth/central/index.md#host-a2dp "bluetooth/central/index.md#host-a2dp")

      - [6.4 host a2dp sbc编码回调](bluetooth/central/index.md#host-a2dp-sbc "bluetooth/central/index.md#host-a2dp-sbc")

      - [6.5 ble gap初始化](bluetooth/central/index.md#ble-gap "bluetooth/central/index.md#ble-gap")

      - [6.6 ble gatts初始化](bluetooth/central/index.md#ble-gatts "bluetooth/central/index.md#ble-gatts")

      - [6.7 ble gattc初始化](bluetooth/central/index.md#ble-gattc "bluetooth/central/index.md#ble-gattc")

      - [6.8 ble gattc 连接](bluetooth/central/index.md#id15 "bluetooth/central/index.md#id15")

    - [7 常见问题FAQ](bluetooth/central/index.md#faq "bluetooth/central/index.md#faq")

      - [7.1 ble连接、断连evt是怎样的顺序？](bluetooth/central/index.md#bleevt "bluetooth/central/index.md#bleevt")

      - [7.2 蓝牙多模(bt/ble)链接的有哪些库？](bluetooth/central/index.md#bt-ble "bluetooth/central/index.md#bt-ble")

      - [7.3 对于一个已存在的ble链路，有没有handle之类的以便于控制？](bluetooth/central/index.md#ble-handle "bluetooth/central/index.md#ble-handle")

      - [7.4 如何创建gatts db，如何将其和attribute handle对应起来？](bluetooth/central/index.md#gatts-db-attribute-handle "bluetooth/central/index.md#gatts-db-attribute-handle")

      - [7.5 bk_ble_gap_register_callback能不能复用，比如多个profile都想收到evt？](bluetooth/central/index.md#bk-ble-gap-register-callback-profileevt "bluetooth/central/index.md#bk-ble-gap-register-callback-profileevt")

      - [7.6 attribute handle的evt能不能分别给到各个profile？](bluetooth/central/index.md#attribute-handleevtprofile "bluetooth/central/index.md#attribute-handleevtprofile")

      - [7.7 各个profile能否收到gatts的evt？](bluetooth/central/index.md#profilegattsevt "bluetooth/central/index.md#profilegattsevt")

      - [7.8 配对相关的evt有哪些流程？](bluetooth/central/index.md#evt "bluetooth/central/index.md#evt")

      - [7.9 app应该存储key吗？](bluetooth/central/index.md#appkey "bluetooth/central/index.md#appkey")

      - [7.10 绑定(bond)和解绑流程？](bluetooth/central/index.md#bond "bluetooth/central/index.md#bond")

      - [7.11 绑定相关还有哪些注意事项？](bluetooth/central/index.md#id16 "bluetooth/central/index.md#id16")

      - [7.12 如何修改ble地址？](bluetooth/central/index.md#ble "bluetooth/central/index.md#ble")

      - [7.13 bt、ble public addr能否不一样？](bluetooth/central/index.md#btble-public-addr "bluetooth/central/index.md#btble-public-addr")

      - [7.14 rpa是什么意思？](bluetooth/central/index.md#rpa "bluetooth/central/index.md#rpa")

      - [7.15 ble如何使用rpa？](bluetooth/central/index.md#blerpa "bluetooth/central/index.md#blerpa")

      - [7.16 ble如果配对使用，推荐用哪种地址？](bluetooth/central/index.md#id17 "bluetooth/central/index.md#id17")

  - [耳机(Headset)](bluetooth/headset/index.md "bluetooth/headset/index.md")

    - [1. 功能概述](bluetooth/headset/index.md#id1 "bluetooth/headset/index.md#id1")

      - [1.1 软件规格](bluetooth/headset/index.md#id2 "bluetooth/headset/index.md#id2")

      - [1.2 代码路径及编译命令](bluetooth/headset/index.md#id3 "bluetooth/headset/index.md#id3")

    - [2. cmd命令简介](bluetooth/headset/index.md#cmd "bluetooth/headset/index.md#cmd")

      - [2.1 a2dp/avrcp](bluetooth/headset/index.md#a2dp-avrcp "bluetooth/headset/index.md#a2dp-avrcp")

    - [3. 框架图](bluetooth/headset/index.md#id4 "bluetooth/headset/index.md#id4")

      - [3.1 软件模块架构图](bluetooth/headset/index.md#id5 "bluetooth/headset/index.md#id5")

      - [3.2 流程图](bluetooth/headset/index.md#id6 "bluetooth/headset/index.md#id6")

    - [4. 配置](bluetooth/headset/index.md#id7 "bluetooth/headset/index.md#id7")

      - [4.1 demo开启配置](bluetooth/headset/index.md#demo "bluetooth/headset/index.md#demo")

      - [4.2 codec方式配置](bluetooth/headset/index.md#codec "bluetooth/headset/index.md#codec")

        - [4.2.1 A2DP](bluetooth/headset/index.md#a2dp "bluetooth/headset/index.md#a2dp")

        - [4.2.1 HFP](bluetooth/headset/index.md#hfp "bluetooth/headset/index.md#hfp")

    - [5. 代码讲解](bluetooth/headset/index.md#id8 "bluetooth/headset/index.md#id8")

      - [5.1 A2DP demo](bluetooth/headset/index.md#a2dp-demo "bluetooth/headset/index.md#a2dp-demo")

        - [5.1.1 获得蓝牙上报的音乐数据](bluetooth/headset/index.md#id9 "bluetooth/headset/index.md#id9")

        - [5.1.2 把音乐数据按帧暂存ring buffer](bluetooth/headset/index.md#ring-buffer "bluetooth/headset/index.md#ring-buffer")

        - [5.1.3 解码音乐数据](bluetooth/headset/index.md#id10 "bluetooth/headset/index.md#id10")

      - [5.2 HFP demo](bluetooth/headset/index.md#hfp-demo "bluetooth/headset/index.md#hfp-demo")

        - [5.2.1 获得蓝牙上报的语音数据](bluetooth/headset/index.md#id11 "bluetooth/headset/index.md#id11")

        - [5.2.2 解码语音数据](bluetooth/headset/index.md#id12 "bluetooth/headset/index.md#id12")

        - [5.2.3 播放语音数据](bluetooth/headset/index.md#id13 "bluetooth/headset/index.md#id13")

        - [5.2.4 获取上行MIC数据](bluetooth/headset/index.md#mic "bluetooth/headset/index.md#mic")

- [多媒体工程(Multi-media)工程](media/index.md "media/index.md")

  - [doorbell](media/doorbell/index.md "media/doorbell/index.md")

    - [1. 简介](media/doorbell/index.md#id1 "media/doorbell/index.md#id1")

      - [1.1 规格](media/doorbell/index.md#id2 "media/doorbell/index.md#id2")

      - [1.2 路径](media/doorbell/index.md#id3 "media/doorbell/index.md#id3")

    - [2. 框架图](media/doorbell/index.md#id4 "media/doorbell/index.md#id4")

      - [2.1 软件模块架构图](media/doorbell/index.md#id5 "media/doorbell/index.md#id5")

      - [2.2 代码模块关系图](media/doorbell/index.md#id6 "media/doorbell/index.md#id6")

    - [3. 配置](media/doorbell/index.md#id7 "media/doorbell/index.md#id7")

      - [3.1 蓝牙与多媒体内存复用](media/doorbell/index.md#id8 "media/doorbell/index.md#id8")

        - [3.1.1 卸载蓝牙](media/doorbell/index.md#id9 "media/doorbell/index.md#id9")

        - [3.1.2 初始化蓝牙](media/doorbell/index.md#id10 "media/doorbell/index.md#id10")

      - [3.2 硬件解码内存配置说明](media/doorbell/index.md#id11 "media/doorbell/index.md#id11")

    - [4. 演示说明](media/doorbell/index.md#id12 "media/doorbell/index.md#id12")

    - [5. 代码讲解](media/doorbell/index.md#id13 "media/doorbell/index.md#id13")

      - [5.1 UVC摄像头](media/doorbell/index.md#uvc "media/doorbell/index.md#uvc")

        - [5.1.1 打开UVC](media/doorbell/index.md#id15 "media/doorbell/index.md#id15")

        - [5.1.2 获取一张图像](media/doorbell/index.md#id18 "media/doorbell/index.md#id18")

        - [5.1.3 关闭UVC](media/doorbell/index.md#id21 "media/doorbell/index.md#id21")

      - [5.2 LCD显示](media/doorbell/index.md#lcd "media/doorbell/index.md#lcd")

        - [5.2.1 打开LCD](media/doorbell/index.md#id25 "media/doorbell/index.md#id25")

        - [5.2.2 关闭LCD](media/doorbell/index.md#id28 "media/doorbell/index.md#id28")

        - [5.2.3 OSD显示](media/doorbell/index.md#osd "media/doorbell/index.md#osd")

      - [5.3 Audio](media/doorbell/index.md#audio "media/doorbell/index.md#audio")

        - [5.3.1 打开UAC，板载MIC/SPEAKER](media/doorbell/index.md#uac-mic-speaker "media/doorbell/index.md#uac-mic-speaker")

        - [5.3.2 获取上行MIC数据](media/doorbell/index.md#mic "media/doorbell/index.md#mic")

        - [5.3.3 播放下行SPEAKER数据](media/doorbell/index.md#speaker "media/doorbell/index.md#speaker")

        - [5.3.4 AEC/降噪处理](media/doorbell/index.md#aec "media/doorbell/index.md#aec")

        - [5.3.7 关闭UAC，板载MIC/SPEAKER](media/doorbell/index.md#id33 "media/doorbell/index.md#id33")

      - [5.4 H264编解码](media/doorbell/index.md#h264 "media/doorbell/index.md#h264")

      - [5.5 WIFI传输](media/doorbell/index.md#wifi "media/doorbell/index.md#wifi")

        - [5.5.1 设置WIFI网络数据传输回调](media/doorbell/index.md#id35 "media/doorbell/index.md#id35")

        - [5.5.1 获取H264图像数据](media/doorbell/index.md#id36 "media/doorbell/index.md#id36")

        - [5.5.2 打开图像数据图传](media/doorbell/index.md#id37 "media/doorbell/index.md#id37")

        - [5.5.2 关闭图像数据图传](media/doorbell/index.md#id38 "media/doorbell/index.md#id38")

  - [doorbell_8M](media/doorbell_8M/index.md "media/doorbell_8M/index.md")

    - [1. 简介](media/doorbell_8M/index.md#id1 "media/doorbell_8M/index.md#id1")

      - [1.1 规格](media/doorbell_8M/index.md#id2 "media/doorbell_8M/index.md#id2")

      - [1.2 路径](media/doorbell_8M/index.md#id4 "media/doorbell_8M/index.md#id4")

    - [2. 框架图](media/doorbell_8M/index.md#id5 "media/doorbell_8M/index.md#id5")

    - [3. 配置](media/doorbell_8M/index.md#id7 "media/doorbell_8M/index.md#id7")

      - [3.1 区别](media/doorbell_8M/index.md#id9 "media/doorbell_8M/index.md#id9")

    - [4. 演示说明](media/doorbell_8M/index.md#id10 "media/doorbell_8M/index.md#id10")

    - [5. 代码讲解](media/doorbell_8M/index.md#id11 "media/doorbell_8M/index.md#id11")

  - [doorbell_720p](media/doorbell_720p/index.md "media/doorbell_720p/index.md")

    - [1. 简介](media/doorbell_720p/index.md#id1 "media/doorbell_720p/index.md#id1")

      - [1.1 规格](media/doorbell_720p/index.md#id2 "media/doorbell_720p/index.md#id2")

      - [1.2 路径](media/doorbell_720p/index.md#id4 "media/doorbell_720p/index.md#id4")

    - [2. 框架图](media/doorbell_720p/index.md#id5 "media/doorbell_720p/index.md#id5")

    - [3. 配置](media/doorbell_720p/index.md#id7 "media/doorbell_720p/index.md#id7")

      - [3.1 区别](media/doorbell_720p/index.md#id9 "media/doorbell_720p/index.md#id9")

    - [4. 演示说明](media/doorbell_720p/index.md#id10 "media/doorbell_720p/index.md#id10")

    - [5. 代码讲解](media/doorbell_720p/index.md#id11 "media/doorbell_720p/index.md#id11")

  - [doorviewer](media/doorviewer/index.md "media/doorviewer/index.md")

    - [1. 简介](media/doorviewer/index.md#id1 "media/doorviewer/index.md#id1")

      - [1.1 规格](media/doorviewer/index.md#id2 "media/doorviewer/index.md#id2")

      - [1.2 路径](media/doorviewer/index.md#id3 "media/doorviewer/index.md#id3")

    - [2. 框架图](media/doorviewer/index.md#id4 "media/doorviewer/index.md#id4")

      - [2.1 软件模块架构图](media/doorviewer/index.md#id5 "media/doorviewer/index.md#id5")

      - [2.2 代码模块关系图](media/doorviewer/index.md#id6 "media/doorviewer/index.md#id6")

    - [3. 配置](media/doorviewer/index.md#id7 "media/doorviewer/index.md#id7")

      - [3.1 蓝牙与多媒体内存复用](media/doorviewer/index.md#id8 "media/doorviewer/index.md#id8")

        - [3.1.1 卸载蓝牙](media/doorviewer/index.md#id9 "media/doorviewer/index.md#id9")

        - [3.1.2 初始化蓝牙](media/doorviewer/index.md#id10 "media/doorviewer/index.md#id10")

    - [4. 演示说明](media/doorviewer/index.md#id11 "media/doorviewer/index.md#id11")

    - [5. 代码讲解](media/doorviewer/index.md#id12 "media/doorviewer/index.md#id12")

      - [5.1 摄像头](media/doorviewer/index.md#id13 "media/doorviewer/index.md#id13")

        - [5.1.1 打开摄像头](media/doorviewer/index.md#id15 "media/doorviewer/index.md#id15")

        - [5.1.2 获取一张图像](media/doorviewer/index.md#id18 "media/doorviewer/index.md#id18")

        - [5.1.2 关闭摄像头](media/doorviewer/index.md#id21 "media/doorviewer/index.md#id21")

      - [5.2 LCD显示](media/doorviewer/index.md#lcd "media/doorviewer/index.md#lcd")

        - [5.2.1 打开LCD](media/doorviewer/index.md#id25 "media/doorviewer/index.md#id25")

        - [5.2.2 关闭LCD](media/doorviewer/index.md#id28 "media/doorviewer/index.md#id28")

        - [5.2.3 OSD显示](media/doorviewer/index.md#osd "media/doorviewer/index.md#osd")

      - [5.4 H264编解码](media/doorviewer/index.md#h264 "media/doorviewer/index.md#h264")

      - [5.5 WIFI传输](media/doorviewer/index.md#wifi "media/doorviewer/index.md#wifi")

  - [doorviewer_8M](media/doorviewer_8M/index.md "media/doorviewer_8M/index.md")

    - [1. 简介](media/doorviewer_8M/index.md#id1 "media/doorviewer_8M/index.md#id1")

      - [1.1 规格](media/doorviewer_8M/index.md#id2 "media/doorviewer_8M/index.md#id2")

      - [1.2 路径](media/doorviewer_8M/index.md#id3 "media/doorviewer_8M/index.md#id3")

    - [2. 框架图](media/doorviewer_8M/index.md#id4 "media/doorviewer_8M/index.md#id4")

    - [3. 配置](media/doorviewer_8M/index.md#id6 "media/doorviewer_8M/index.md#id6")

      - [3.1 区别](media/doorviewer_8M/index.md#id8 "media/doorviewer_8M/index.md#id8")

    - [4. 演示说明](media/doorviewer_8M/index.md#id9 "media/doorviewer_8M/index.md#id9")

    - [5. 代码讲解](media/doorviewer_8M/index.md#id10 "media/doorviewer_8M/index.md#id10")

  - [av_client](media/av_client/index.md "media/av_client/index.md")

    - [1 功能概述](media/av_client/index.md#id1 "media/av_client/index.md#id1")

      - [1.1 规格](media/av_client/index.md#id2 "media/av_client/index.md#id2")

      - [1.2 路径](media/av_client/index.md#id3 "media/av_client/index.md#id3")

    - [2. 框架图](media/av_client/index.md#id4 "media/av_client/index.md#id4")

      - [2.1 软件模块架构图](media/av_client/index.md#id5 "media/av_client/index.md#id5")

      - [2.2 代码模块关系图](media/av_client/index.md#id6 "media/av_client/index.md#id6")

    - [3. 配置](media/av_client/index.md#id7 "media/av_client/index.md#id7")

      - [3.1 图像传输方式配置](media/av_client/index.md#id8 "media/av_client/index.md#id8")

    - [4. 演示说明](media/av_client/index.md#id9 "media/av_client/index.md#id9")

    - [5. 代码讲解](media/av_client/index.md#id10 "media/av_client/index.md#id10")

      - [5.1 UVC摄像头](media/av_client/index.md#uvc "media/av_client/index.md#uvc")

        - [5.1.1 打开UVC](media/av_client/index.md#id12 "media/av_client/index.md#id12")

      - [5.2 LCD显示](media/av_client/index.md#lcd "media/av_client/index.md#lcd")

        - [5.2.1 打开LCD](media/av_client/index.md#id16 "media/av_client/index.md#id16")

      - [5.3 Audio](media/av_client/index.md#audio "media/av_client/index.md#audio")

        - [5.3.1 打开UAC，板载MIC/SPEAKER](media/av_client/index.md#uac-mic-speaker "media/av_client/index.md#uac-mic-speaker")

        - [5.3.2 获取上行MIC数据](media/av_client/index.md#mic "media/av_client/index.md#mic")

        - [5.3.3 播放下行SPEAKER数据](media/av_client/index.md#speaker "media/av_client/index.md#speaker")

  - [av_server](media/av_server/index.md "media/av_server/index.md")

    - [1 功能概述](media/av_server/index.md#id1 "media/av_server/index.md#id1")

      - [1.1 规格](media/av_server/index.md#id2 "media/av_server/index.md#id2")

      - [1.2 路径](media/av_server/index.md#id3 "media/av_server/index.md#id3")

    - [2. 框架图](media/av_server/index.md#id4 "media/av_server/index.md#id4")

      - [2.1 软件模块架构图](media/av_server/index.md#id5 "media/av_server/index.md#id5")

      - [2.2 代码模块关系图](media/av_server/index.md#id6 "media/av_server/index.md#id6")

    - [3. 配置](media/av_server/index.md#id7 "media/av_server/index.md#id7")

      - [3.1 图像传输方式配置](media/av_server/index.md#id8 "media/av_server/index.md#id8")

    - [4. 演示说明](media/av_server/index.md#id9 "media/av_server/index.md#id9")

    - [5. 代码讲解](media/av_server/index.md#id10 "media/av_server/index.md#id10")

      - [5.1 LCD显示](media/av_server/index.md#lcd "media/av_server/index.md#lcd")

        - [5.1.1 打开LCD](media/av_server/index.md#id12 "media/av_server/index.md#id12")

      - [5.2 Audio](media/av_server/index.md#audio "media/av_server/index.md#audio")

        - [5.2.1 打开UAC，板载MIC/SPEAKER](media/av_server/index.md#uac-mic-speaker "media/av_server/index.md#uac-mic-speaker")

        - [5.2.2 获取上行MIC数据](media/av_server/index.md#mic "media/av_server/index.md#mic")

        - [5.2.3 播放下行SPEAKER数据](media/av_server/index.md#speaker "media/av_server/index.md#speaker")

  - [audio_record_to_sdcard](media/audio_record_to_sdcard/index.md "media/audio_record_to_sdcard/index.md")

    - [1. 简介](media/audio_record_to_sdcard/index.md#id1 "media/audio_record_to_sdcard/index.md#id1")

      - [1.1 规格](media/audio_record_to_sdcard/index.md#id2 "media/audio_record_to_sdcard/index.md#id2")

      - [1.2 路径](media/audio_record_to_sdcard/index.md#id3 "media/audio_record_to_sdcard/index.md#id3")

    - [2. 框架图](media/audio_record_to_sdcard/index.md#id4 "media/audio_record_to_sdcard/index.md#id4")

      - [2.1 软件模块架构图](media/audio_record_to_sdcard/index.md#id5 "media/audio_record_to_sdcard/index.md#id5")

      - [2.2 代码模块关系图](media/audio_record_to_sdcard/index.md#id6 "media/audio_record_to_sdcard/index.md#id6")

    - [3. 演示说明](media/audio_record_to_sdcard/index.md#id7 "media/audio_record_to_sdcard/index.md#id7")

    - [4. 代码讲解](media/audio_record_to_sdcard/index.md#id8 "media/audio_record_to_sdcard/index.md#id8")

      - [4.1 启动录音](media/audio_record_to_sdcard/index.md#id9 "media/audio_record_to_sdcard/index.md#id9")

      - [4.2 停止录音](media/audio_record_to_sdcard/index.md#id10 "media/audio_record_to_sdcard/index.md#id10")

  - [audio_play_sdcard_mp3_music](media/audio_play_sdcard_mp3_music/index.md "media/audio_play_sdcard_mp3_music/index.md")

    - [1. 简介](media/audio_play_sdcard_mp3_music/index.md#id1 "media/audio_play_sdcard_mp3_music/index.md#id1")

      - [1.1 规格](media/audio_play_sdcard_mp3_music/index.md#id2 "media/audio_play_sdcard_mp3_music/index.md#id2")

      - [1.2 路径](media/audio_play_sdcard_mp3_music/index.md#id3 "media/audio_play_sdcard_mp3_music/index.md#id3")

    - [2. 框架图](media/audio_play_sdcard_mp3_music/index.md#id4 "media/audio_play_sdcard_mp3_music/index.md#id4")

      - [2.1 软件模块架构图](media/audio_play_sdcard_mp3_music/index.md#id5 "media/audio_play_sdcard_mp3_music/index.md#id5")

      - [2.2 代码模块关系图](media/audio_play_sdcard_mp3_music/index.md#id6 "media/audio_play_sdcard_mp3_music/index.md#id6")

    - [3. 演示说明](media/audio_play_sdcard_mp3_music/index.md#id7 "media/audio_play_sdcard_mp3_music/index.md#id7")

    - [4. 代码讲解](media/audio_play_sdcard_mp3_music/index.md#id8 "media/audio_play_sdcard_mp3_music/index.md#id8")

      - [4.1 启动播放](media/audio_play_sdcard_mp3_music/index.md#id9 "media/audio_play_sdcard_mp3_music/index.md#id9")

      - [4.2 停止播放](media/audio_play_sdcard_mp3_music/index.md#id10 "media/audio_play_sdcard_mp3_music/index.md#id10")

- [图形界面(LVGL)工程](lvgl/index.md "lvgl/index.md")

  - [86box](lvgl/86box/index.md "lvgl/86box/index.md")

    - [1. 简介](lvgl/86box/index.md#id2 "lvgl/86box/index.md#id2")

      - [1.1 规格](lvgl/86box/index.md#id3 "lvgl/86box/index.md#id3")

      - [1.2 路径](lvgl/86box/index.md#id4 "lvgl/86box/index.md#id4")

    - [2. 框架图](lvgl/86box/index.md#id5 "lvgl/86box/index.md#id5")

      - [2.1 软件模块架构图](lvgl/86box/index.md#id6 "lvgl/86box/index.md#id6")

      - [2.2 代码模块关系图](lvgl/86box/index.md#id8 "lvgl/86box/index.md#id8")

    - [3. 演示说明](lvgl/86box/index.md#id9 "lvgl/86box/index.md#id9")

  - [86box_smart_panel](lvgl/86box_smart_panel/index.md "lvgl/86box_smart_panel/index.md")

    - [1. 简介](lvgl/86box_smart_panel/index.md#id2 "lvgl/86box_smart_panel/index.md#id2")

      - [1.1 规格](lvgl/86box_smart_panel/index.md#id4 "lvgl/86box_smart_panel/index.md#id4")

      - [1.2 路径](lvgl/86box_smart_panel/index.md#id5 "lvgl/86box_smart_panel/index.md#id5")

    - [2. 框架图](lvgl/86box_smart_panel/index.md#id6 "lvgl/86box_smart_panel/index.md#id6")

      - [2.1 软件模块架构图](lvgl/86box_smart_panel/index.md#id7 "lvgl/86box_smart_panel/index.md#id7")

      - [2.2 代码模块关系图](lvgl/86box_smart_panel/index.md#id9 "lvgl/86box_smart_panel/index.md#id9")

    - [3. 演示说明](lvgl/86box_smart_panel/index.md#id10 "lvgl/86box_smart_panel/index.md#id10")

  - [benchmark](lvgl/benchmark/index.md "lvgl/benchmark/index.md")

    - [1. 简介](lvgl/benchmark/index.md#id1 "lvgl/benchmark/index.md#id1")

      - [1.1 规格](lvgl/benchmark/index.md#id2 "lvgl/benchmark/index.md#id2")

      - [1.2 路径](lvgl/benchmark/index.md#id3 "lvgl/benchmark/index.md#id3")

    - [2. 框架图](lvgl/benchmark/index.md#id4 "lvgl/benchmark/index.md#id4")

      - [2.1 软件模块架构图](lvgl/benchmark/index.md#id5 "lvgl/benchmark/index.md#id5")

      - [2.2 代码模块关系图](lvgl/benchmark/index.md#id7 "lvgl/benchmark/index.md#id7")

    - [3. 演示说明](lvgl/benchmark/index.md#id8 "lvgl/benchmark/index.md#id8")

  - [camera](lvgl/camera/index.md "lvgl/camera/index.md")

    - [1. 简介](lvgl/camera/index.md#id1 "lvgl/camera/index.md#id1")

      - [1.1 规格](lvgl/camera/index.md#id2 "lvgl/camera/index.md#id2")

      - [1.2 路径](lvgl/camera/index.md#id3 "lvgl/camera/index.md#id3")

    - [2. 框架图](lvgl/camera/index.md#id4 "lvgl/camera/index.md#id4")

      - [2.1 软件模块架构图](lvgl/camera/index.md#id5 "lvgl/camera/index.md#id5")

      - [2.2 代码模块关系图](lvgl/camera/index.md#id7 "lvgl/camera/index.md#id7")

    - [3. 演示说明](lvgl/camera/index.md#id8 "lvgl/camera/index.md#id8")

    - [4. 代码讲解](lvgl/camera/index.md#id9 "lvgl/camera/index.md#id9")

  - [keypad_encoder](lvgl/keypad_encoder/index.md "lvgl/keypad_encoder/index.md")

    - [1. 简介](lvgl/keypad_encoder/index.md#id1 "lvgl/keypad_encoder/index.md#id1")

      - [1.1 规格](lvgl/keypad_encoder/index.md#id2 "lvgl/keypad_encoder/index.md#id2")

      - [1.2 路径](lvgl/keypad_encoder/index.md#id3 "lvgl/keypad_encoder/index.md#id3")

    - [2. 框架图](lvgl/keypad_encoder/index.md#id4 "lvgl/keypad_encoder/index.md#id4")

      - [2.1 软件模块架构图](lvgl/keypad_encoder/index.md#id5 "lvgl/keypad_encoder/index.md#id5")

      - [2.2 代码模块关系图](lvgl/keypad_encoder/index.md#id7 "lvgl/keypad_encoder/index.md#id7")

    - [3. 演示说明](lvgl/keypad_encoder/index.md#id8 "lvgl/keypad_encoder/index.md#id8")

  - [meter](lvgl/meter/index.md "lvgl/meter/index.md")

    - [1. 简介](lvgl/meter/index.md#id1 "lvgl/meter/index.md#id1")

      - [1.1 规格](lvgl/meter/index.md#id2 "lvgl/meter/index.md#id2")

      - [1.2 路径](lvgl/meter/index.md#id3 "lvgl/meter/index.md#id3")

    - [2. 框架图](lvgl/meter/index.md#id4 "lvgl/meter/index.md#id4")

      - [2.1 软件模块架构图](lvgl/meter/index.md#id5 "lvgl/meter/index.md#id5")

      - [2.2 代码模块关系图](lvgl/meter/index.md#id7 "lvgl/meter/index.md#id7")

    - [3. 演示说明](lvgl/meter/index.md#id8 "lvgl/meter/index.md#id8")

  - [meter_rgb_16M](lvgl/meter_rgb_16M/index.md "lvgl/meter_rgb_16M/index.md")

    - [1. 简介](lvgl/meter_rgb_16M/index.md#id1 "lvgl/meter_rgb_16M/index.md#id1")

      - [1.1 规格](lvgl/meter_rgb_16M/index.md#id2 "lvgl/meter_rgb_16M/index.md#id2")

      - [1.2 路径](lvgl/meter_rgb_16M/index.md#id3 "lvgl/meter_rgb_16M/index.md#id3")

    - [2. 框架图](lvgl/meter_rgb_16M/index.md#id4 "lvgl/meter_rgb_16M/index.md#id4")

      - [2.1 软件模块架构图](lvgl/meter_rgb_16M/index.md#id5 "lvgl/meter_rgb_16M/index.md#id5")

      - [2.2 代码模块关系图](lvgl/meter_rgb_16M/index.md#id7 "lvgl/meter_rgb_16M/index.md#id7")

    - [3. 演示说明](lvgl/meter_rgb_16M/index.md#id8 "lvgl/meter_rgb_16M/index.md#id8")

  - [meter_spi](lvgl/meter_spi/index.md "lvgl/meter_spi/index.md")

    - [1. 简介](lvgl/meter_spi/index.md#id1 "lvgl/meter_spi/index.md#id1")

      - [1.1 规格](lvgl/meter_spi/index.md#id2 "lvgl/meter_spi/index.md#id2")

      - [1.2 路径](lvgl/meter_spi/index.md#id3 "lvgl/meter_spi/index.md#id3")

    - [2. 框架图](lvgl/meter_spi/index.md#id4 "lvgl/meter_spi/index.md#id4")

      - [2.1 软件模块架构图](lvgl/meter_spi/index.md#id5 "lvgl/meter_spi/index.md#id5")

      - [2.2 代码模块关系图](lvgl/meter_spi/index.md#id7 "lvgl/meter_spi/index.md#id7")

    - [3. 演示说明](lvgl/meter_spi/index.md#id8 "lvgl/meter_spi/index.md#id8")

  - [music](lvgl/music/index.md "lvgl/music/index.md")

    - [1. 简介](lvgl/music/index.md#id1 "lvgl/music/index.md#id1")

      - [1.1 规格](lvgl/music/index.md#id2 "lvgl/music/index.md#id2")

      - [1.2 路径](lvgl/music/index.md#id3 "lvgl/music/index.md#id3")

    - [2. 框架图](lvgl/music/index.md#id4 "lvgl/music/index.md#id4")

      - [2.1 软件模块架构图](lvgl/music/index.md#id5 "lvgl/music/index.md#id5")

      - [2.2 代码模块关系图](lvgl/music/index.md#id7 "lvgl/music/index.md#id7")

    - [3. 演示说明](lvgl/music/index.md#id8 "lvgl/music/index.md#id8")

  - [stress](lvgl/stress/index.md "lvgl/stress/index.md")

    - [1. 简介](lvgl/stress/index.md#id1 "lvgl/stress/index.md#id1")

      - [1.1 规格](lvgl/stress/index.md#id2 "lvgl/stress/index.md#id2")

      - [1.2 路径](lvgl/stress/index.md#id3 "lvgl/stress/index.md#id3")

    - [2. 框架图](lvgl/stress/index.md#id4 "lvgl/stress/index.md#id4")

      - [2.1 软件模块架构图](lvgl/stress/index.md#id5 "lvgl/stress/index.md#id5")

      - [2.2 代码模块关系图](lvgl/stress/index.md#id7 "lvgl/stress/index.md#id7")

    - [3. 演示说明](lvgl/stress/index.md#id8 "lvgl/stress/index.md#id8")

  - [widgets](lvgl/widgets/index.md "lvgl/widgets/index.md")

    - [1. 简介](lvgl/widgets/index.md#id1 "lvgl/widgets/index.md#id1")

      - [1.1 规格](lvgl/widgets/index.md#id2 "lvgl/widgets/index.md#id2")

      - [1.2 路径](lvgl/widgets/index.md#id3 "lvgl/widgets/index.md#id3")

    - [2. 框架图](lvgl/widgets/index.md#id4 "lvgl/widgets/index.md#id4")

      - [2.1 软件模块架构图](lvgl/widgets/index.md#id5 "lvgl/widgets/index.md#id5")

      - [2.2 代码模块关系图](lvgl/widgets/index.md#id7 "lvgl/widgets/index.md#id7")

    - [3. 演示说明](lvgl/widgets/index.md#id8 "lvgl/widgets/index.md#id8")

- [第三方工程](thirdparty/index.md "thirdparty/index.md")

  - [华镇语音识别(wanson-asr)工程](thirdparty/wanson_asr/index.md "thirdparty/wanson_asr/index.md")

    - [1. 简介](thirdparty/wanson_asr/index.md#id2 "thirdparty/wanson_asr/index.md#id2")

      - [1.1 规格](thirdparty/wanson_asr/index.md#id3 "thirdparty/wanson_asr/index.md#id3")

      - [1.2 路径](thirdparty/wanson_asr/index.md#id4 "thirdparty/wanson_asr/index.md#id4")

    - [2. 框架图](thirdparty/wanson_asr/index.md#id5 "thirdparty/wanson_asr/index.md#id5")

      - [2.1 软件模块架构图](thirdparty/wanson_asr/index.md#id6 "thirdparty/wanson_asr/index.md#id6")

      - [2.2 代码模块关系图](thirdparty/wanson_asr/index.md#id7 "thirdparty/wanson_asr/index.md#id7")

    - [3. 配置](thirdparty/wanson_asr/index.md#id8 "thirdparty/wanson_asr/index.md#id8")

    - [4. 演示说明](thirdparty/wanson_asr/index.md#id9 "thirdparty/wanson_asr/index.md#id9")

    - [5. 代码讲解](thirdparty/wanson_asr/index.md#id10 "thirdparty/wanson_asr/index.md#id10")

      - [5.1 mic采样](thirdparty/wanson_asr/index.md#mic "thirdparty/wanson_asr/index.md#mic")

        - [5.1.1 打开mic采样](thirdparty/wanson_asr/index.md#id11 "thirdparty/wanson_asr/index.md#id11")

        - [5.1.2 关闭mic采样](thirdparty/wanson_asr/index.md#id12 "thirdparty/wanson_asr/index.md#id12")

      - [5.2 wanson语音识别](thirdparty/wanson_asr/index.md#wanson "thirdparty/wanson_asr/index.md#wanson")

        - [5.2.1 初始化语音识别](thirdparty/wanson_asr/index.md#id13 "thirdparty/wanson_asr/index.md#id13")

        - [5.2.2 退出语音识别](thirdparty/wanson_asr/index.md#id14 "thirdparty/wanson_asr/index.md#id14")

        - [5.2.3 启动语音识别](thirdparty/wanson_asr/index.md#id15 "thirdparty/wanson_asr/index.md#id15")

        - [5.2.4 停止语音识别](thirdparty/wanson_asr/index.md#id16 "thirdparty/wanson_asr/index.md#id16")

      - [5.3 语音识别task识别流程](thirdparty/wanson_asr/index.md#task "thirdparty/wanson_asr/index.md#task")

    - [6. 上海华镇电子科技有限公司](thirdparty/wanson_asr/index.md#id17 "thirdparty/wanson_asr/index.md#id17")

  - [UVC尚云门锁(doorbell_cs2)工程](thirdparty/doorbell_cs2/index.md "thirdparty/doorbell_cs2/index.md")

    - [1. 简介](thirdparty/doorbell_cs2/index.md#id1 "thirdparty/doorbell_cs2/index.md#id1")

      - [1.1 规格](thirdparty/doorbell_cs2/index.md#id2 "thirdparty/doorbell_cs2/index.md#id2")

      - [1.2 路径](thirdparty/doorbell_cs2/index.md#id4 "thirdparty/doorbell_cs2/index.md#id4")

    - [2. 框架图](thirdparty/doorbell_cs2/index.md#id5 "thirdparty/doorbell_cs2/index.md#id5")

    - [3. 配置](thirdparty/doorbell_cs2/index.md#id7 "thirdparty/doorbell_cs2/index.md#id7")

      - [3.1 区别](thirdparty/doorbell_cs2/index.md#id9 "thirdparty/doorbell_cs2/index.md#id9")

    - [4. 演示说明](thirdparty/doorbell_cs2/index.md#id10 "thirdparty/doorbell_cs2/index.md#id10")

    - [5. 代码讲解](thirdparty/doorbell_cs2/index.md#id11 "thirdparty/doorbell_cs2/index.md#id11")

  - [UVC尚云门锁(doorbell_cs2_4M)工程](thirdparty/doorbell_cs2_4M/index.md "thirdparty/doorbell_cs2_4M/index.md")

    - [1. 简介](thirdparty/doorbell_cs2_4M/index.md#id1 "thirdparty/doorbell_cs2_4M/index.md#id1")

      - [1.1 规格](thirdparty/doorbell_cs2_4M/index.md#id2 "thirdparty/doorbell_cs2_4M/index.md#id2")

      - [1.2 路径](thirdparty/doorbell_cs2_4M/index.md#id3 "thirdparty/doorbell_cs2_4M/index.md#id3")

    - [2. 框架图](thirdparty/doorbell_cs2_4M/index.md#id4 "thirdparty/doorbell_cs2_4M/index.md#id4")

    - [3. 配置](thirdparty/doorbell_cs2_4M/index.md#id6 "thirdparty/doorbell_cs2_4M/index.md#id6")

      - [3.1 区别](thirdparty/doorbell_cs2_4M/index.md#id8 "thirdparty/doorbell_cs2_4M/index.md#id8")

    - [4. 演示说明](thirdparty/doorbell_cs2_4M/index.md#id9 "thirdparty/doorbell_cs2_4M/index.md#id9")

    - [5. 代码讲解](thirdparty/doorbell_cs2_4M/index.md#id10 "thirdparty/doorbell_cs2_4M/index.md#id10")

    - [6. 移植说明](thirdparty/doorbell_cs2_4M/index.md#id12 "thirdparty/doorbell_cs2_4M/index.md#id12")

      - [步骤1：](thirdparty/doorbell_cs2_4M/index.md#id13 "thirdparty/doorbell_cs2_4M/index.md#id13")

      - [步骤2：](thirdparty/doorbell_cs2_4M/index.md#id14 "thirdparty/doorbell_cs2_4M/index.md#id14")

    - [7. Q&A](thirdparty/doorbell_cs2_4M/index.md#q-a "thirdparty/doorbell_cs2_4M/index.md#q-a")

      - [Q: psram内存分配如何调整？](thirdparty/doorbell_cs2_4M/index.md#q-psram "thirdparty/doorbell_cs2_4M/index.md#q-psram")

      - [Q: 融合buffer踩内存问题](thirdparty/doorbell_cs2_4M/index.md#q-buffer "thirdparty/doorbell_cs2_4M/index.md#q-buffer")

  - [UVC尚云门锁(doorbell_cs2_ab_4M)工程](thirdparty/doorbell_cs2_ab_4M/index.md "thirdparty/doorbell_cs2_ab_4M/index.md")

    - [1. 简介](thirdparty/doorbell_cs2_ab_4M/index.md#id1 "thirdparty/doorbell_cs2_ab_4M/index.md#id1")

      - [1.1 规格](thirdparty/doorbell_cs2_ab_4M/index.md#id2 "thirdparty/doorbell_cs2_ab_4M/index.md#id2")

      - [1.2 路径](thirdparty/doorbell_cs2_ab_4M/index.md#id3 "thirdparty/doorbell_cs2_ab_4M/index.md#id3")

    - [2. 框架图](thirdparty/doorbell_cs2_ab_4M/index.md#id4 "thirdparty/doorbell_cs2_ab_4M/index.md#id4")

    - [3. 配置](thirdparty/doorbell_cs2_ab_4M/index.md#id6 "thirdparty/doorbell_cs2_ab_4M/index.md#id6")

      - [3.1 区别](thirdparty/doorbell_cs2_ab_4M/index.md#id8 "thirdparty/doorbell_cs2_ab_4M/index.md#id8")

    - [4. 演示说明](thirdparty/doorbell_cs2_ab_4M/index.md#id9 "thirdparty/doorbell_cs2_ab_4M/index.md#id9")

    - [5. 代码讲解](thirdparty/doorbell_cs2_ab_4M/index.md#id10 "thirdparty/doorbell_cs2_ab_4M/index.md#id10")

    - [6. 移植说明](thirdparty/doorbell_cs2_ab_4M/index.md#id12 "thirdparty/doorbell_cs2_ab_4M/index.md#id12")

      - [步骤1：](thirdparty/doorbell_cs2_ab_4M/index.md#id13 "thirdparty/doorbell_cs2_ab_4M/index.md#id13")

      - [步骤2：](thirdparty/doorbell_cs2_ab_4M/index.md#id14 "thirdparty/doorbell_cs2_ab_4M/index.md#id14")

  - [UVC尚云门锁(doorbell_cs2_8M)工程](thirdparty/doorbell_cs2_8M/index.md "thirdparty/doorbell_cs2_8M/index.md")

    - [1. 简介](thirdparty/doorbell_cs2_8M/index.md#id1 "thirdparty/doorbell_cs2_8M/index.md#id1")

      - [1.1 规格](thirdparty/doorbell_cs2_8M/index.md#id2 "thirdparty/doorbell_cs2_8M/index.md#id2")

      - [1.2 路径](thirdparty/doorbell_cs2_8M/index.md#id4 "thirdparty/doorbell_cs2_8M/index.md#id4")

    - [2. 框架图](thirdparty/doorbell_cs2_8M/index.md#id5 "thirdparty/doorbell_cs2_8M/index.md#id5")

    - [3. 配置](thirdparty/doorbell_cs2_8M/index.md#id7 "thirdparty/doorbell_cs2_8M/index.md#id7")

      - [3.1 区别](thirdparty/doorbell_cs2_8M/index.md#id9 "thirdparty/doorbell_cs2_8M/index.md#id9")

    - [4. 演示说明](thirdparty/doorbell_cs2_8M/index.md#id10 "thirdparty/doorbell_cs2_8M/index.md#id10")

    - [5. 代码讲解](thirdparty/doorbell_cs2_8M/index.md#id11 "thirdparty/doorbell_cs2_8M/index.md#id11")

  - [UVC尚云门锁(doorbell_cs2_720p)工程](thirdparty/doorbell_cs2_720p/index.md "thirdparty/doorbell_cs2_720p/index.md")

    - [1. 简介](thirdparty/doorbell_cs2_720p/index.md#id1 "thirdparty/doorbell_cs2_720p/index.md#id1")

      - [1.1 规格](thirdparty/doorbell_cs2_720p/index.md#id2 "thirdparty/doorbell_cs2_720p/index.md#id2")

      - [1.2 路径](thirdparty/doorbell_cs2_720p/index.md#id4 "thirdparty/doorbell_cs2_720p/index.md#id4")

    - [2. 框架图](thirdparty/doorbell_cs2_720p/index.md#id5 "thirdparty/doorbell_cs2_720p/index.md#id5")

    - [3. 配置](thirdparty/doorbell_cs2_720p/index.md#id7 "thirdparty/doorbell_cs2_720p/index.md#id7")

      - [3.1 区别](thirdparty/doorbell_cs2_720p/index.md#id9 "thirdparty/doorbell_cs2_720p/index.md#id9")

    - [4. 演示说明](thirdparty/doorbell_cs2_720p/index.md#id10 "thirdparty/doorbell_cs2_720p/index.md#id10")

    - [5. 代码讲解](thirdparty/doorbell_cs2_720p/index.md#id11 "thirdparty/doorbell_cs2_720p/index.md#id11")

- [Wi-Fi 工程](wifi/index.md "wifi/index.md")

  - [BK-RLK 多媒体(Multi-media)工程](projects/wifi/bk_rlk_media.md "wifi/bk_rlk_media.md")

    - [1 功能概述](wifi/bk_rlk_media.md#id1 "wifi/bk_rlk_media.md#id1")

    - [2 Demo 说明](wifi/bk_rlk_media.md#demo "wifi/bk_rlk_media.md#demo")

    - [3 环境搭建](wifi/bk_rlk_media.md#id2 "wifi/bk_rlk_media.md#id2")

    - [4 代码路径](wifi/bk_rlk_media.md#id3 "wifi/bk_rlk_media.md#id3")

    - [5 参考链接](wifi/bk_rlk_media.md#id4 "wifi/bk_rlk_media.md#id4")

- [外设应用工程](peripheral/index.md "peripheral/index.md")

  - [dvp](peripheral/dvp/index.md "peripheral/dvp/index.md")

    - [1. 简介](peripheral/dvp/index.md#id1 "peripheral/dvp/index.md#id1")

      - [1.1 规格](peripheral/dvp/index.md#id2 "peripheral/dvp/index.md#id2")

      - [1.2 路径](peripheral/dvp/index.md#id4 "peripheral/dvp/index.md#id4")

    - [2. 框架图](peripheral/dvp/index.md#id5 "peripheral/dvp/index.md#id5")

    - [3. 配置](peripheral/dvp/index.md#id7 "peripheral/dvp/index.md#id7")

      - [3.1 蓝牙与多媒体内存复用](peripheral/dvp/index.md#id8 "peripheral/dvp/index.md#id8")

        - [3.1.1 卸载蓝牙](peripheral/dvp/index.md#id9 "peripheral/dvp/index.md#id9")

        - [3.1.2 初始化蓝牙](peripheral/dvp/index.md#id10 "peripheral/dvp/index.md#id10")

      - [3.2 区别](peripheral/dvp/index.md#id11 "peripheral/dvp/index.md#id11")

    - [4. 演示说明](peripheral/dvp/index.md#id12 "peripheral/dvp/index.md#id12")

    - [5. 代码讲解](peripheral/dvp/index.md#id13 "peripheral/dvp/index.md#id13")

    - [6. 新增适配](peripheral/dvp/index.md#id15 "peripheral/dvp/index.md#id15")

  - [uvc](peripheral/uvc/index.md "peripheral/uvc/index.md")

    - [1. 简介](peripheral/uvc/index.md#id1 "peripheral/uvc/index.md#id1")

      - [1.1 规格](peripheral/uvc/index.md#id2 "peripheral/uvc/index.md#id2")

      - [1.2 路径](peripheral/uvc/index.md#id4 "peripheral/uvc/index.md#id4")

    - [2. 框架图](peripheral/uvc/index.md#id5 "peripheral/uvc/index.md#id5")

    - [3. 配置](peripheral/uvc/index.md#id7 "peripheral/uvc/index.md#id7")

      - [3.1 蓝牙与多媒体内存复用](peripheral/uvc/index.md#id8 "peripheral/uvc/index.md#id8")

        - [3.1.1 卸载蓝牙](peripheral/uvc/index.md#id9 "peripheral/uvc/index.md#id9")

        - [3.1.2 初始化蓝牙](peripheral/uvc/index.md#id10 "peripheral/uvc/index.md#id10")

      - [3.2 区别](peripheral/uvc/index.md#id11 "peripheral/uvc/index.md#id11")

    - [4. 演示说明](peripheral/uvc/index.md#id12 "peripheral/uvc/index.md#id12")

    - [5. 代码讲解](peripheral/uvc/index.md#id13 "peripheral/uvc/index.md#id13")

  - [slcd](peripheral/slcd/index.md "peripheral/slcd/index.md")

    - [1 功能概述](peripheral/slcd/index.md#id1 "peripheral/slcd/index.md#id1")

    - [2 代码路径](peripheral/slcd/index.md#id2 "peripheral/slcd/index.md#id2")

    - [3 编译命令](peripheral/slcd/index.md#id3 "peripheral/slcd/index.md#id3")

    - [4 演示介绍](peripheral/slcd/index.md#id4 "peripheral/slcd/index.md#id4")

  - [lcd_qspi](peripheral/lcd_qspi/index.md "peripheral/lcd_qspi/index.md")

    - [1 功能概述](peripheral/lcd_qspi/index.md#id1 "peripheral/lcd_qspi/index.md#id1")

    - [2 代码路径](peripheral/lcd_qspi/index.md#id2 "peripheral/lcd_qspi/index.md#id2")

    - [3 编译命令](peripheral/lcd_qspi/index.md#id3 "peripheral/lcd_qspi/index.md#id3")

    - [4 演示介绍](peripheral/lcd_qspi/index.md#id4 "peripheral/lcd_qspi/index.md#id4")

  - [lcd_spi](peripheral/lcd_spi/index.md "peripheral/lcd_spi/index.md")

    - [1 功能概述](peripheral/lcd_spi/index.md#id1 "peripheral/lcd_spi/index.md#id1")

    - [2 代码路径](peripheral/lcd_spi/index.md#id2 "peripheral/lcd_spi/index.md#id2")

    - [3 编译命令](peripheral/lcd_spi/index.md#id3 "peripheral/lcd_spi/index.md#id3")

    - [4 演示介绍](peripheral/lcd_spi/index.md#id4 "peripheral/lcd_spi/index.md#id4")

  - [lcd_rgb565](peripheral/lcd_rgb565/index.md "peripheral/lcd_rgb565/index.md")

    - [1 功能概述](peripheral/lcd_rgb565/index.md#id1 "peripheral/lcd_rgb565/index.md#id1")

    - [2 代码路径](peripheral/lcd_rgb565/index.md#id2 "peripheral/lcd_rgb565/index.md#id2")

    - [3.代码讲解](peripheral/lcd_rgb565/index.md#id3 "peripheral/lcd_rgb565/index.md#id3")

      - [RGB565 LCD 工程的配置步骤如下：](peripheral/lcd_rgb565/index.md#id4 "peripheral/lcd_rgb565/index.md#id4")

  - [lcd_rgb888](peripheral/lcd_rgb888/index.md "peripheral/lcd_rgb888/index.md")

    - [1 功能概述](peripheral/lcd_rgb888/index.md#id1 "peripheral/lcd_rgb888/index.md#id1")

    - [2 代码路径](peripheral/lcd_rgb888/index.md#id2 "peripheral/lcd_rgb888/index.md#id2")

    - [3.代码讲解](peripheral/lcd_rgb888/index.md#id3 "peripheral/lcd_rgb888/index.md#id3")

      - [RGB888 LCD 工程的配置步骤如下：](peripheral/lcd_rgb888/index.md#id4 "peripheral/lcd_rgb888/index.md#id4")

  - [lcd_rgb666](peripheral/lcd_rgb666/index.md "peripheral/lcd_rgb666/index.md")

    - [1 功能概述](peripheral/lcd_rgb666/index.md#id1 "peripheral/lcd_rgb666/index.md#id1")

    - [2 代码路径](peripheral/lcd_rgb666/index.md#id2 "peripheral/lcd_rgb666/index.md#id2")

    - [3.代码讲解](peripheral/lcd_rgb666/index.md#id3 "peripheral/lcd_rgb666/index.md#id3")

      - [RGB666 LCD 工程的配置步骤如下：](peripheral/lcd_rgb666/index.md#id4 "peripheral/lcd_rgb666/index.md#id4")

  - [lcd_8080](peripheral/lcd_8080/index.md "peripheral/lcd_8080/index.md")

    - [1 功能概述](peripheral/lcd_8080/index.md#id1 "peripheral/lcd_8080/index.md#id1")

    - [2 代码路径](peripheral/lcd_8080/index.md#id2 "peripheral/lcd_8080/index.md#id2")

    - [3.代码讲解](peripheral/lcd_8080/index.md#id3 "peripheral/lcd_8080/index.md#id3")

      - [LCD MCU 工程的配置步骤如下：](peripheral/lcd_8080/index.md#lcd-mcu "peripheral/lcd_8080/index.md#lcd-mcu")

## 模块导航

- [bluetooth](projects/bluetooth.md)
- [lvgl](projects/lvgl.md)
- [media](projects/media.md)
- [peripheral](projects/peripheral.md)
- [thirdparty](projects/thirdparty.md)
- [wifi](projects/wifi.md)

