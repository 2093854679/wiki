---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7235/zh_CN/v1.5/api-reference/multi_media/bk_video_transfer.html
sdk_family: bk_idk
chip: BK7235
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="video-transfer-apis"></a>

# VIDEO\_TRANSFER APIs

重要

The VIDEO\_TRANSFER API v1.0 is the lastest stable VIDEO\_TRANSFER APIs. All new applications should use VIDEO\_TRANSFER API v1.0.

<a id="video-transfer-api-categories"></a>

## VIDEO\_TRANSFER API Categories

Most of VIDEO\_TRANSFER APIs can be categoried as:

> - VIDEO\_TRANSFER APIs
>
>   The common APIs are prefixed with bk\_video, e.g. bk\_video\_transfer\_init() etc.

VIDEO\_TRANSFER APIs:
:   - [`bk_video_transfer_init()`](#_CPPv422bk_video_transfer_initP13video_setup_t "bk_video_transfer_init") \- init video transfer
    - [`bk_video_transfer_deinit()`](#_CPPv424bk_video_transfer_deinitv "bk_video_transfer_deinit") \- deinit video transfer
    - `bk_video_send_msg()` \- send msg deal video data
    - [`bk_video_buffer_open()`](#_CPPv420bk_video_buffer_openP21media_camera_device_t "bk_video_buffer_open") \- open video buff
    - [`bk_video_buffer_close()`](#_CPPv421bk_video_buffer_closev "bk_video_buffer_close") \- close video buff
    - [`bk_video_buffer_read_frame()`](#_CPPv426bk_video_buffer_read_frameP7uint8_t8uint32_tPi8uint32_t "bk_video_buffer_read_frame") \- read fix length video data

<a id="api-reference"></a>

## API Reference

<a id="header-file"></a>

### Header File

- [video\_transfer.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/video_transfer.h)

<a id="functions"></a>

### Functions

<a id="_CPPv422bk_video_transfer_initP13video_setup_t"></a>

<a id="_CPPv322bk_video_transfer_initP13video_setup_t"></a> <a id="_CPPv222bk_video_transfer_initP13video_setup_t"></a> <a id="bk_video_transfer_init__video_setup_tP"></a> <a id="video__transfer_8h_1a67e8135e788c42d3ada1bb38c200e9be"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_video\_transfer\_init([video\_setup\_t](#_CPPv413video_setup_t "video_setup_t") \*setup\_cfg)
:   video transfer init

    This API will create video thread, init msg queue, and excute camera init

    参数
    :   **setup\_cfg** – configure of the video transfer include packet process, method of transfer, etc.

    返回
    :   - kNoErr: succeed
        - others: other errors.

<a id="_CPPv424bk_video_transfer_deinitv"></a>

<a id="_CPPv324bk_video_transfer_deinitv"></a> <a id="_CPPv224bk_video_transfer_deinitv"></a> <a id="bk_video_transfer_deinit__void"></a> <a id="video__transfer_8h_1aaca404f9de25371ccf3c5f44d983825a"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_video\_transfer\_deinit(void)
:   video transfer deinit

    This API will quit video thread, and free all reasource

    返回
    :   - kNoErr: succeed
        - others: other errors.

<a id="_CPPv420bk_video_buffer_openP21media_camera_device_t"></a>

<a id="_CPPv320bk_video_buffer_openP21media_camera_device_t"></a> <a id="_CPPv220bk_video_buffer_openP21media_camera_device_t"></a> <a id="bk_video_buffer_open__media_camera_device_tP"></a> <a id="video__transfer_8h_1acce7bd91c24b0b5e8229905a9cccf03f"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_video\_buffer\_open(media\_camera\_device\_t \*device)
:   set video transfer param

    This API will open video tranfer data\_buffer, and star transfer

    **Attention**
    :   1\. when call this function, the video date will transfer to wifi(UDP/others)

    参数
    :   **device** – referenc type : meida\_camera\_device\_t

    返回
    :   - kNoErr: succeed
        - others: other errors.

<a id="_CPPv421bk_video_buffer_closev"></a>

<a id="_CPPv321bk_video_buffer_closev"></a> <a id="_CPPv221bk_video_buffer_closev"></a> <a id="bk_video_buffer_close__void"></a> <a id="video__transfer_8h_1a191e7bb0fa2a132dbd7252dd888dcc18"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_video\_buffer\_close(void)
:   set video buffer close

    This API will deinit video tranfer, stop transfer video data

    返回
    :   - kNoErr: succeed
        - others: other errors.

<a id="_CPPv426bk_video_buffer_read_frameP7uint8_t8uint32_tPi8uint32_t"></a>

<a id="_CPPv326bk_video_buffer_read_frameP7uint8_t8uint32_tPi8uint32_t"></a> <a id="_CPPv226bk_video_buffer_read_frameP7uint8_t8uint32_tPi8uint32_t"></a> <a id="bk_video_buffer_read_frame__uint8_tP.uint32_t.iP.uint32_t"></a> <a id="video__transfer_8h_1a0ac3d648986acb9e1533e443f3f24a86"></a> uint32\_t bk\_video\_buffer\_read\_frame(uint8\_t \*buf, uint32\_t buf\_len, int \*err\_code, uint32\_t timeout)
:   read video buffer frame

    This API will malloc a data\_buffer, and save video data to this buffer

    参数
    :   - **buf** – malloc buf pointer
        - **buf\_len** – buf length
        - **err\_code** –

          - 0: success
          - 1: param error
          - 2: buffer full
          - 3: frame data err
          - 4: timeout
          - 5: unknow err
        - **timeout** – read frame data timeout

    返回
    :   - 0: failed
        - other: frame\_length.

<a id="_CPPv422bk_video_transfer_stopv"></a>

<a id="_CPPv322bk_video_transfer_stopv"></a> <a id="_CPPv222bk_video_transfer_stopv"></a> <a id="bk_video_transfer_stop__void"></a> <a id="video__transfer_8h_1a039c083ef5feb0fa4a99c9f64391dfde"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_video\_transfer\_stop(void)
:   read video buffer frame

    This API will stop camera, but not free malloc memory for transfer

    返回
    :   - kNoErr: succeed
        - others: other errors.

<a id="_CPPv423bk_video_transfer_startv"></a>

<a id="_CPPv323bk_video_transfer_startv"></a> <a id="_CPPv223bk_video_transfer_startv"></a> <a id="bk_video_transfer_start__void"></a> <a id="video__transfer_8h_1a2f5849b7dfbd7a97eae9213c1f07cc71"></a> [bk\_err\_t](../system/os.md#_CPPv48bk_err_t "bk_err_t") bk\_video\_transfer\_start(void)
:   read video buffer frame

    This API will start camera after stopping camera

    1\. this function must called after bk\_video\_transfer\_stop

    返回
    :   - kNoErr: succeed
        - others: other errors.

<a id="api-typedefs"></a>

## API Typedefs

<a id="id1"></a>

### Header File

- [video\_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/video_types.h)

<a id="structures"></a>

### Structures

<a id="_CPPv414video_config_t"></a>

<a id="_CPPv314video_config_t"></a> <a id="_CPPv214video_config_t"></a> <a id="video_config_t"></a> <a id="structvideo__config__t"></a> struct video\_config\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N14video_config_t5rxbufE"></a>

    <a id="_CPPv3N14video_config_t5rxbufE"></a> <a id="_CPPv2N14video_config_t5rxbufE"></a> <a id="video_config_t::rxbuf__uint8_tP"></a> <a id="structvideo__config__t_1ad1666245a39492c87094c9e29f84157e"></a> uint8\_t \*rxbuf
    :   the buffer save camera data

    <a id="_CPPv4N14video_config_t17node_full_handlerE"></a>

    <a id="_CPPv3N14video_config_t17node_full_handlerE"></a> <a id="_CPPv2N14video_config_t17node_full_handlerE"></a> <a id="structvideo__config__t_1a28c88230508236ad30de070d45ebcae6"></a> void (\*node\_full\_handler)(void \*curptr, uint32\_t newlen, uint32\_t is\_eof, uint32\_t frame\_len)
    :   node full handler

        This is a transfer camera data to uplayer api, when transfer node\_len jpeg data finish , this function will be called

        Param curptr
        :   the start address of transfer data.

        Param newlen
        :   the transfer data length

        Param is\_eof
        :   0/1: whether this packet data is the last packet of this frame, will called in jpeg\_end\_frame isr

        Param frame\_len
        :   the complete jpeg frame size, if is\_eof\=1, the frame\_len is the true value of jpeg frame size, is\_eof\=0, the frame\_len\=0, in other words, only when transfer really frame\_len at the last packet in jpeg\_end\_frame isr

    <a id="_CPPv4N14video_config_t16data_end_handlerE"></a>

    <a id="_CPPv3N14video_config_t16data_end_handlerE"></a> <a id="_CPPv2N14video_config_t16data_end_handlerE"></a> <a id="structvideo__config__t_1a21dec7a319c2ce19375af31b0e1ca5b7"></a> void (\*data\_end\_handler)(void)
    :   brief data\_end\_handler

        This api use to inforamte video transfer thread to deal transfer camera data

    <a id="_CPPv4N14video_config_t6deviceE"></a>

    <a id="_CPPv3N14video_config_t6deviceE"></a> <a id="_CPPv2N14video_config_t6deviceE"></a> <a id="video_config_t::device__media_camera_device_tP"></a> <a id="structvideo__config__t_1a0390ae89850ac0f16cce1793a2aa2f8f"></a> media\_camera\_device\_t \*device
    :   config of camera

    <a id="_CPPv4N14video_config_t9rxbuf_lenE"></a>

    <a id="_CPPv3N14video_config_t9rxbuf_lenE"></a> <a id="_CPPv2N14video_config_t9rxbuf_lenE"></a> <a id="video_config_t::rxbuf_len__uint16_t"></a> <a id="structvideo__config__t_1ae543771c52ce19ece11aab8e9a8cbb3d"></a> uint16\_t rxbuf\_len
    :   The length of receiving camera data buff

    <a id="_CPPv4N14video_config_t11rx_read_lenE"></a>

    <a id="_CPPv3N14video_config_t11rx_read_lenE"></a> <a id="_CPPv2N14video_config_t11rx_read_lenE"></a> <a id="video_config_t::rx_read_len__uint16_t"></a> <a id="structvideo__config__t_1a102a7a272188fb8e7df9d5661bce62e4"></a> uint16\_t rx\_read\_len
    :   manage the node\_full\_handler callback function input params

    <a id="_CPPv4N14video_config_t8node_lenE"></a>

    <a id="_CPPv3N14video_config_t8node_lenE"></a> <a id="_CPPv2N14video_config_t8node_lenE"></a> <a id="video_config_t::node_len__uint32_t"></a> <a id="structvideo__config__t_1a299d0f13050f1326d77581150a1a0eeb"></a> uint32\_t node\_len
    :   video transfer network comunication protocol length a time

<a id="_CPPv414video_packet_t"></a>

<a id="_CPPv314video_packet_t"></a> <a id="_CPPv214video_packet_t"></a> <a id="video_packet_t"></a> <a id="structvideo__packet__t"></a> struct video\_packet\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N14video_packet_t6ptklenE"></a>

    <a id="_CPPv3N14video_packet_t6ptklenE"></a> <a id="_CPPv2N14video_packet_t6ptklenE"></a> <a id="video_packet_t::ptklen__uint32_t"></a> <a id="structvideo__packet__t_1a1affd3d1fc8c3763de1659a92ee4406c"></a> uint32\_t ptklen
    :   The current packet length

    <a id="_CPPv4N14video_packet_t8frame_idE"></a>

    <a id="_CPPv3N14video_packet_t8frame_idE"></a> <a id="_CPPv2N14video_packet_t8frame_idE"></a> <a id="video_packet_t::frame_id__uint32_t"></a> <a id="structvideo__packet__t_1a8325a551a2bfcd160a268864512df925"></a> uint32\_t frame\_id
    :   The current packet frame id

    <a id="_CPPv4N14video_packet_t6is_eofE"></a>

    <a id="_CPPv3N14video_packet_t6is_eofE"></a> <a id="_CPPv2N14video_packet_t6is_eofE"></a> <a id="video_packet_t::is_eof__uint32_t"></a> <a id="structvideo__packet__t_1a0481a04a936d0d5eaf28e2a0fedc53ce"></a> uint32\_t is\_eof
    :   The current packet is the last packet

    <a id="_CPPv4N14video_packet_t9frame_lenE"></a>

    <a id="_CPPv3N14video_packet_t9frame_lenE"></a> <a id="_CPPv2N14video_packet_t9frame_lenE"></a> <a id="video_packet_t::frame_len__uint32_t"></a> <a id="structvideo__packet__t_1ac9a326ec979611fa7cf8d798084a65bc"></a> uint32\_t frame\_len
    :   The frame length

<a id="_CPPv413video_setup_t"></a>

<a id="_CPPv313video_setup_t"></a> <a id="_CPPv213video_setup_t"></a> <a id="video_setup_t"></a> <a id="structvideo__setup__t"></a> struct video\_setup\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N13video_setup_t6deviceE"></a>

    <a id="_CPPv3N13video_setup_t6deviceE"></a> <a id="_CPPv2N13video_setup_t6deviceE"></a> <a id="video_setup_t::device__media_camera_device_tP"></a> <a id="structvideo__setup__t_1aa79f644fa00351232ac1969de29a70eb"></a> media\_camera\_device\_t \*device
    :   config of camera

    <a id="_CPPv4N13video_setup_t9open_typeE"></a>

    <a id="_CPPv3N13video_setup_t9open_typeE"></a> <a id="_CPPv2N13video_setup_t9open_typeE"></a> <a id="video_setup_t::open_type__uint16_t"></a> <a id="structvideo__setup__t_1af7b5e04758eaf5528888376ea772c5fe"></a> uint16\_t open\_type
    :   video transfer network comunication protocol type, video\_open\_type\_t

    <a id="_CPPv4N13video_setup_t9send_typeE"></a>

    <a id="_CPPv3N13video_setup_t9send_typeE"></a> <a id="_CPPv2N13video_setup_t9send_typeE"></a> <a id="video_setup_t::send_type__uint16_t"></a> <a id="structvideo__setup__t_1a9eb5ad6aeb12d3662dc6b301b602cdf8"></a> uint16\_t send\_type
    :   video transfer network comunication protocol type, video\_send\_type\_t

    <a id="_CPPv4N13video_setup_t9send_funcE"></a>

    <a id="_CPPv3N13video_setup_t9send_funcE"></a> <a id="_CPPv2N13video_setup_t9send_funcE"></a> <a id="video_setup_t::send_func__video_transfer_send_func"></a> <a id="structvideo__setup__t_1a5effdd21872505fe393d9e0c371918ee"></a> [video\_transfer\_send\_func](#_CPPv424video_transfer_send_func "video_transfer_send_func") send\_func
    :   function ptr for send to uplayer

    <a id="_CPPv4N13video_setup_t8start_cbE"></a>

    <a id="_CPPv3N13video_setup_t8start_cbE"></a> <a id="_CPPv2N13video_setup_t8start_cbE"></a> <a id="video_setup_t::start_cb__video_transfer_start_cb"></a> <a id="structvideo__setup__t_1af4b58699c9dea80c40f6cb0b00f7711a"></a> [video\_transfer\_start\_cb](#_CPPv423video_transfer_start_cb "video_transfer_start_cb") start\_cb
    :   function ptr for start to send to uplayer

    <a id="_CPPv4N13video_setup_t6end_cbE"></a>

    <a id="_CPPv3N13video_setup_t6end_cbE"></a> <a id="_CPPv2N13video_setup_t6end_cbE"></a> <a id="video_setup_t::end_cb__video_transfer_start_cb"></a> <a id="structvideo__setup__t_1a425b8b424cb01e5d45b907a9bf4fee67"></a> [video\_transfer\_start\_cb](#_CPPv423video_transfer_start_cb "video_transfer_start_cb") end\_cb
    :   function ptr for end to send to uplayer

    <a id="_CPPv4N13video_setup_t15pkt_header_sizeE"></a>

    <a id="_CPPv3N13video_setup_t15pkt_header_sizeE"></a> <a id="_CPPv2N13video_setup_t15pkt_header_sizeE"></a> <a id="video_setup_t::pkt_header_size__uint32_t"></a> <a id="structvideo__setup__t_1a61d2490cab60556ec579a5076b4a2d89"></a> uint32\_t pkt\_header\_size
    :   packet header size

    <a id="_CPPv4N13video_setup_t14add_pkt_headerE"></a>

    <a id="_CPPv3N13video_setup_t14add_pkt_headerE"></a> <a id="_CPPv2N13video_setup_t14add_pkt_headerE"></a> <a id="video_setup_t::add_pkt_header__tvideo_add_pkt_header"></a> <a id="structvideo__setup__t_1a6641459769d29306e2cc3e5f3d54608f"></a> [tvideo\_add\_pkt\_header](#_CPPv421tvideo_add_pkt_header "tvideo_add_pkt_header") add\_pkt\_header
    :   function ptr for add packet header

<a id="_CPPv414video_header_t"></a>

<a id="_CPPv314video_header_t"></a> <a id="_CPPv214video_header_t"></a> <a id="video_header_t"></a> <a id="structvideo__header__t"></a> struct video\_header\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N14video_header_t2idE"></a>

    <a id="_CPPv3N14video_header_t2idE"></a> <a id="_CPPv2N14video_header_t2idE"></a> <a id="video_header_t::id__uint8_t"></a> <a id="structvideo__header__t_1a738317dc825280489efd2663455786ae"></a> uint8\_t id
    :   the frame id

    <a id="_CPPv4N14video_header_t6is_eofE"></a>

    <a id="_CPPv3N14video_header_t6is_eofE"></a> <a id="_CPPv2N14video_header_t6is_eofE"></a> <a id="video_header_t::is_eof__uint8_t"></a> <a id="structvideo__header__t_1ab10a5515aab616730677558cf909781e"></a> uint8\_t is\_eof
    :   the flag of end frame, 1 for end

    <a id="_CPPv4N14video_header_t7pkt_cntE"></a>

    <a id="_CPPv3N14video_header_t7pkt_cntE"></a> <a id="_CPPv2N14video_header_t7pkt_cntE"></a> <a id="video_header_t::pkt_cnt__uint8_t"></a> <a id="structvideo__header__t_1a7cb80e10f6002cac1e46313fa4a6c35b"></a> uint8\_t pkt\_cnt
    :   the packet count of one frame

    <a id="_CPPv4N14video_header_t7pkt_seqE"></a>

    <a id="_CPPv3N14video_header_t7pkt_seqE"></a> <a id="_CPPv2N14video_header_t7pkt_seqE"></a> <a id="video_header_t::pkt_seq__uint8_t"></a> <a id="structvideo__header__t_1a6a6e8998c05ccf0201a5254c22eaf9e6"></a> uint8\_t pkt\_seq
    :   the packet header’s count of one frame

<a id="_CPPv412video_buff_t"></a>

<a id="_CPPv312video_buff_t"></a> <a id="_CPPv212video_buff_t"></a> <a id="video_buff_t"></a> <a id="structvideo__buff__t"></a> struct video\_buff\_t
:   <a id="breathe-section-title-public-members"></a>

    Public Members

    <a id="_CPPv4N12video_buff_t16aready_semaphoreE"></a>

    <a id="_CPPv3N12video_buff_t16aready_semaphoreE"></a> <a id="_CPPv2N12video_buff_t16aready_semaphoreE"></a> <a id="video_buff_t::aready_semaphore__beken_semaphore_t"></a> <a id="structvideo__buff__t_1ac1065c8ee32ea569532ac58834fe85fd"></a> [beken\_semaphore\_t](../system/os.md#_CPPv417beken_semaphore_t "beken_semaphore_t") aready\_semaphore
    :   the video data receive complete

    <a id="_CPPv4N12video_buff_t8buf_baseE"></a>

    <a id="_CPPv3N12video_buff_t8buf_baseE"></a> <a id="_CPPv2N12video_buff_t8buf_baseE"></a> <a id="video_buff_t::buf_base__uint8_tP"></a> <a id="structvideo__buff__t_1ae29f24a392af14aac82020ec90b2c427"></a> uint8\_t \*buf\_base
    :   the receive video data, malloc by user

    <a id="_CPPv4N12video_buff_t7buf_lenE"></a>

    <a id="_CPPv3N12video_buff_t7buf_lenE"></a> <a id="_CPPv2N12video_buff_t7buf_lenE"></a> <a id="video_buff_t::buf_len__uint32_t"></a> <a id="structvideo__buff__t_1a1e6392561fdc81874e6fed87a730fc10"></a> uint32\_t buf\_len
    :   video buff length, malloc by user

    <a id="_CPPv4N12video_buff_t8frame_idE"></a>

    <a id="_CPPv3N12video_buff_t8frame_idE"></a> <a id="_CPPv2N12video_buff_t8frame_idE"></a> <a id="video_buff_t::frame_id__uint32_t"></a> <a id="structvideo__buff__t_1ac6dad06bbbc71a6e95fcfe44df4d0eaf"></a> uint32\_t frame\_id
    :   frame id

    <a id="_CPPv4N12video_buff_t13frame_pkt_cntE"></a>

    <a id="_CPPv3N12video_buff_t13frame_pkt_cntE"></a> <a id="_CPPv2N12video_buff_t13frame_pkt_cntE"></a> <a id="video_buff_t::frame_pkt_cnt__uint32_t"></a> <a id="structvideo__buff__t_1aff0dcdba376b28e36243a0b2f082189d"></a> uint32\_t frame\_pkt\_cnt
    :   the packet count of one frame

    <a id="_CPPv4N12video_buff_t7buf_ptrE"></a>

    <a id="_CPPv3N12video_buff_t7buf_ptrE"></a> <a id="_CPPv2N12video_buff_t7buf_ptrE"></a> <a id="video_buff_t::buf_ptr__uint8_tP"></a> <a id="structvideo__buff__t_1a2724d181fcbc75098157b84426e575da"></a> uint8\_t \*buf\_ptr
    :   recoder the buff ptr of every time receive video packte

    <a id="_CPPv4N12video_buff_t9frame_lenE"></a>

    <a id="_CPPv3N12video_buff_t9frame_lenE"></a> <a id="_CPPv2N12video_buff_t9frame_lenE"></a> <a id="video_buff_t::frame_len__uint32_t"></a> <a id="structvideo__buff__t_1a222586380b62227b13f031415b6bd964"></a> uint32\_t frame\_len
    :   the length of receive one frame

    <a id="_CPPv4N12video_buff_t9start_bufE"></a>

    <a id="_CPPv3N12video_buff_t9start_bufE"></a> <a id="_CPPv2N12video_buff_t9start_bufE"></a> <a id="video_buff_t::start_buf__uint32_t"></a> <a id="structvideo__buff__t_1a58e6e2470127c05e6a1fff37f81f4b7d"></a> uint32\_t start\_buf
    :   video buff receive state

<a id="type-definitions"></a>

### Type Definitions

<a id="_CPPv421tvideo_add_pkt_header"></a>

<a id="_CPPv321tvideo_add_pkt_header"></a> <a id="_CPPv221tvideo_add_pkt_header"></a> <a id="tvideo_add_pkt_header"></a> <a id="video__types_8h_1a457e9895e9d8e015edf3c87b4cb43858"></a> typedef void (\*tvideo\_add\_pkt\_header)([video\_packet\_t](#_CPPv414video_packet_t "video_packet_t") \*param)

<a id="_CPPv424video_transfer_send_func"></a>

<a id="_CPPv324video_transfer_send_func"></a> <a id="_CPPv224video_transfer_send_func"></a> <a id="video_transfer_send_func"></a> <a id="video__types_8h_1ad22377fec76a5c6dda30baddf0784a9c"></a> typedef int (\*video\_transfer\_send\_func)(uint8\_t \*data, uint32\_t len)

<a id="_CPPv423video_transfer_start_cb"></a>

<a id="_CPPv323video_transfer_start_cb"></a> <a id="_CPPv223video_transfer_start_cb"></a> <a id="video_transfer_start_cb"></a> <a id="video__types_8h_1ac43b20c12ba6f312e614379d553ed21d"></a> typedef void (\*video\_transfer\_start\_cb)(void)

<a id="_CPPv421video_transfer_end_cb"></a>

<a id="_CPPv321video_transfer_end_cb"></a> <a id="_CPPv221video_transfer_end_cb"></a> <a id="video_transfer_end_cb"></a> <a id="video__types_8h_1a5b2fedb5d4e13a029694444fe8c3b5a9"></a> typedef void (\*video\_transfer\_end\_cb)(void)

<a id="enumerations"></a>

### Enumerations

<a id="_CPPv417video_open_type_t"></a>

<a id="_CPPv317video_open_type_t"></a> <a id="_CPPv217video_open_type_t"></a> <a id="video__types_8h_1a1b404a2ca8d76c788f7d996944184b8f"></a> enum video\_open\_type\_t
:   video sample module protocol type

    *Values:*

    <a id="_CPPv4N17video_open_type_t16TVIDEO_OPEN_NONEE"></a>

    <a id="_CPPv3N17video_open_type_t16TVIDEO_OPEN_NONEE"></a> <a id="_CPPv2N17video_open_type_t16TVIDEO_OPEN_NONEE"></a> <a id="video__types_8h_1a1b404a2ca8d76c788f7d996944184b8faff9df1f8ad36095b09db1f0526a74c51"></a> enumerator TVIDEO\_OPEN\_NONE
    :   not sample module

    <a id="_CPPv4N17video_open_type_t16TVIDEO_OPEN_SCCBE"></a>

    <a id="_CPPv3N17video_open_type_t16TVIDEO_OPEN_SCCBE"></a> <a id="_CPPv2N17video_open_type_t16TVIDEO_OPEN_SCCBE"></a> <a id="video__types_8h_1a1b404a2ca8d76c788f7d996944184b8fa66502be5eb2747bdaa915376c2e64e6e"></a> enumerator TVIDEO\_OPEN\_SCCB
    :   sample module follow sccb protocol

    <a id="_CPPv4N17video_open_type_t18TVIDEO_OPEN_SPIDMAE"></a>

    <a id="_CPPv3N17video_open_type_t18TVIDEO_OPEN_SPIDMAE"></a> <a id="_CPPv2N17video_open_type_t18TVIDEO_OPEN_SPIDMAE"></a> <a id="video__types_8h_1a1b404a2ca8d76c788f7d996944184b8fadd8b073e476e3f686d11f905e46d1d37"></a> enumerator TVIDEO\_OPEN\_SPIDMA
    :   sample module follow spidma protocol

<a id="_CPPv417video_send_type_t"></a>

<a id="_CPPv317video_send_type_t"></a> <a id="_CPPv217video_send_type_t"></a> <a id="video__types_8h_1a6dae25f27bc2b2912cc7a839c8dbf8c3"></a> enum video\_send\_type\_t
:   video transfer network comunication protocol type

    *Values:*

    <a id="_CPPv4N17video_send_type_t15TVIDEO_SND_NONEE"></a>

    <a id="_CPPv3N17video_send_type_t15TVIDEO_SND_NONEE"></a> <a id="_CPPv2N17video_send_type_t15TVIDEO_SND_NONEE"></a> <a id="video__types_8h_1a6dae25f27bc2b2912cc7a839c8dbf8c3aba95d6e87da3dee8fa23e16f7c9b4459"></a> enumerator TVIDEO\_SND\_NONE
    :   not transfer

    <a id="_CPPv4N17video_send_type_t14TVIDEO_SND_UDPE"></a>

    <a id="_CPPv3N17video_send_type_t14TVIDEO_SND_UDPE"></a> <a id="_CPPv2N17video_send_type_t14TVIDEO_SND_UDPE"></a> <a id="video__types_8h_1a6dae25f27bc2b2912cc7a839c8dbf8c3aaedc3e3e5e5ff3f9f01e576d3e0806ea"></a> enumerator TVIDEO\_SND\_UDP
    :   follow udp protocol

    <a id="_CPPv4N17video_send_type_t14TVIDEO_SND_TCPE"></a>

    <a id="_CPPv3N17video_send_type_t14TVIDEO_SND_TCPE"></a> <a id="_CPPv2N17video_send_type_t14TVIDEO_SND_TCPE"></a> <a id="video__types_8h_1a6dae25f27bc2b2912cc7a839c8dbf8c3a720729ed1b18eaeefff9086fc8289dea"></a> enumerator TVIDEO\_SND\_TCP
    :   follow tcp protocol

    <a id="_CPPv4N17video_send_type_t15TVIDEO_SND_INTFE"></a>

    <a id="_CPPv3N17video_send_type_t15TVIDEO_SND_INTFE"></a> <a id="_CPPv2N17video_send_type_t15TVIDEO_SND_INTFE"></a> <a id="video__types_8h_1a6dae25f27bc2b2912cc7a839c8dbf8c3ae5b80fdcd6c8a31ee2cd9f3d3dc1d5f4"></a> enumerator TVIDEO\_SND\_INTF
    :   transfer to inter frame

    <a id="_CPPv4N17video_send_type_t17TVIDEO_SND_BUFFERE"></a>

    <a id="_CPPv3N17video_send_type_t17TVIDEO_SND_BUFFERE"></a> <a id="_CPPv2N17video_send_type_t17TVIDEO_SND_BUFFERE"></a> <a id="video__types_8h_1a6dae25f27bc2b2912cc7a839c8dbf8c3ae8adeb63d426eca6c2dfd07d4429abff"></a> enumerator TVIDEO\_SND\_BUFFER
    :   transfer to buffer

<a id="_CPPv418video_buff_state_t"></a>

<a id="_CPPv318video_buff_state_t"></a> <a id="_CPPv218video_buff_state_t"></a> <a id="video__types_8h_1ad9f39e526151fee7648e61d2809ddcc5"></a> enum video\_buff\_state\_t
:   *Values:*

    <a id="_CPPv4N18video_buff_state_t12BUF_STA_INITE"></a>

    <a id="_CPPv3N18video_buff_state_t12BUF_STA_INITE"></a> <a id="_CPPv2N18video_buff_state_t12BUF_STA_INITE"></a> <a id="video__types_8h_1ad9f39e526151fee7648e61d2809ddcc5a293d626ba5afc1fb9be2cadee817f084"></a> enumerator BUF\_STA\_INIT
    :   video buff init

    <a id="_CPPv4N18video_buff_state_t12BUF_STA_COPYE"></a>

    <a id="_CPPv3N18video_buff_state_t12BUF_STA_COPYE"></a> <a id="_CPPv2N18video_buff_state_t12BUF_STA_COPYE"></a> <a id="video__types_8h_1ad9f39e526151fee7648e61d2809ddcc5afd234540a4e4b9d8095f0a5393546f8a"></a> enumerator BUF\_STA\_COPY
    :   video buff begin copy

    <a id="_CPPv4N18video_buff_state_t11BUF_STA_GETE"></a>

    <a id="_CPPv3N18video_buff_state_t11BUF_STA_GETE"></a> <a id="_CPPv2N18video_buff_state_t11BUF_STA_GETE"></a> <a id="video__types_8h_1ad9f39e526151fee7648e61d2809ddcc5a4fa4e801b6833d4f04319ef983eebde1"></a> enumerator BUF\_STA\_GET
    :   video frame get

    <a id="_CPPv4N18video_buff_state_t12BUF_STA_FULLE"></a>

    <a id="_CPPv3N18video_buff_state_t12BUF_STA_FULLE"></a> <a id="_CPPv2N18video_buff_state_t12BUF_STA_FULLE"></a> <a id="video__types_8h_1ad9f39e526151fee7648e61d2809ddcc5a960ee822ae337854ba0880d9ec1ebb9a"></a> enumerator BUF\_STA\_FULL
    :   video buff full

    <a id="_CPPv4N18video_buff_state_t14BUF_STA_DEINITE"></a>

    <a id="_CPPv3N18video_buff_state_t14BUF_STA_DEINITE"></a> <a id="_CPPv2N18video_buff_state_t14BUF_STA_DEINITE"></a> <a id="video__types_8h_1ad9f39e526151fee7648e61d2809ddcc5a05f752bd0c365b84c38d81d27f2cf0b8"></a> enumerator BUF\_STA\_DEINIT
    :   video buff deinit

    <a id="_CPPv4N18video_buff_state_t11BUF_STA_ERRE"></a>

    <a id="_CPPv3N18video_buff_state_t11BUF_STA_ERRE"></a> <a id="_CPPv2N18video_buff_state_t11BUF_STA_ERRE"></a> <a id="video__types_8h_1ad9f39e526151fee7648e61d2809ddcc5a68cbf21d6af72408d120c28fd55a303b"></a> enumerator BUF\_STA\_ERR
    :   other error
