# VIDEO_TRANSFER APIs[](#video-transfer-apis "永久链接至标题")


重要

The VIDEO_TRANSFER API v1.0 is the lastest stable VIDEO_TRANSFER APIs. All new applications should use VIDEO_TRANSFER API v1.0.


## VIDEO_TRANSFER API Categories[](#video-transfer-api-categories "永久链接至标题")

Most of VIDEO_TRANSFER APIs can be categoried as:

> - VIDEO_TRANSFER APIs
>
>   The common APIs are prefixed with bk_video, e.g. bk_video_transfer_init() etc.

VIDEO_TRANSFER APIs:
:   - [`bk_video_transfer_init()`](#_CPPv422bk_video_transfer_initP13video_setup_t "bk_video_transfer_init") - init video transfer

    - [`bk_video_transfer_deinit()`](#_CPPv424bk_video_transfer_deinitv "bk_video_transfer_deinit") - deinit video transfer

    - [`bk_video_buffer_open()`](#_CPPv420bk_video_buffer_openP21media_camera_device_t "bk_video_buffer_open") - open video buff

    - [`bk_video_buffer_close()`](#_CPPv421bk_video_buffer_closev "bk_video_buffer_close") - close video buff

    - [`bk_video_buffer_read_frame()`](#_CPPv426bk_video_buffer_read_frameP7uint8_t8uint32_tPi8uint32_t "bk_video_buffer_read_frame") - read fix length video data


## API Reference[](#api-reference "永久链接至标题")


### Header File[](#header-file "永久链接至标题")


- [video_transfer.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/video_transfer.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/video_transfer.h")


### Functions[](#functions "永久链接至标题")

bk_err_t bk_video_transfer_init([video_setup_t](#_CPPv413video_setup_t "video_setup_t") *setup_cfg)[](#_CPPv422bk_video_transfer_initP13video_setup_t "永久链接至目标")
:   video transfer init

    This API will create video thread, init msg queue, and excute camera init

    参数
    :   **setup_cfg** – configure of the video transfer include packet process, method of transfer, etc.

    返回
    :   - kNoErr: succeed

        - others: other errors.

bk_err_t bk_video_transfer_deinit(void)[](#_CPPv424bk_video_transfer_deinitv "永久链接至目标")
:   video transfer deinit

    This API will quit video thread, and free all reasource

    返回
    :   - kNoErr: succeed

        - others: other errors.

bk_err_t bk_video_buffer_open(media_camera_device_t *device)[](#_CPPv420bk_video_buffer_openP21media_camera_device_t "永久链接至目标")
:   set video transfer param

    This API will open video tranfer data_buffer, and star transfer


    **Attention**
    :   1. when call this function, the video date will transfer to wifi(UDP/others)

    参数
    :   **device** – referenc type : meida_camera_device_t

    返回
    :   - kNoErr: succeed

        - others: other errors.

bk_err_t bk_video_buffer_close(void)[](#_CPPv421bk_video_buffer_closev "永久链接至目标")
:   set video buffer close

    This API will deinit video tranfer, stop transfer video data

    返回
    :   - kNoErr: succeed

        - others: other errors.

uint32_t bk_video_buffer_read_frame(uint8_t *buf, uint32_t buf_len, int *err_code, uint32_t timeout)[](#_CPPv426bk_video_buffer_read_frameP7uint8_t8uint32_tPi8uint32_t "永久链接至目标")
:   read video buffer frame

    This API will malloc a data_buffer, and save video data to this buffer

    参数
    :   - **buf** – malloc buf pointer

        - **buf_len** – buf length

        - **err_code** –

          - 0: success

          - 1: param error

          - 2: buffer full

          - 3: frame data err

          - 4: timeout

          - 5: unknow err

        - **timeout** – read frame data timeout

    返回
    :   - 0: failed

        - other: frame_length.

bk_err_t bk_video_transfer_stop(void)[](#_CPPv422bk_video_transfer_stopv "永久链接至目标")
:   read video buffer frame

    This API will stop camera, but not free malloc memory for transfer

    返回
    :   - kNoErr: succeed

        - others: other errors.

bk_err_t bk_video_transfer_start(void)[](#_CPPv423bk_video_transfer_startv "永久链接至目标")
:   read video buffer frame

    This API will start camera after stopping camera

    @attation 1. this function must called after bk_video_transfer_stop

    返回
    :   - kNoErr: succeed

        - others: other errors.


## API Typedefs[](#api-typedefs "永久链接至标题")


### Header File[](#id1 "永久链接至标题")


- [video_types.h](http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/video_types.h "http://192.168.0.46/gerrit/plugins/gitiles/iot/wcn/projects/+/refs/heads/armino_main/components/video_types.h")


### Structures[](#structures "永久链接至标题")

struct video_config_t[](#_CPPv414video_config_t "永久链接至目标")
:   Public Members

    uint8_t *rxbuf[](#_CPPv4N14video_config_t5rxbufE "永久链接至目标")
    :   the buffer save camera data

    void (*node_full_handler)(void *curptr, uint32_t newlen, uint32_t is_eof, uint32_t frame_len)[](#_CPPv4N14video_config_t17node_full_handlerE "永久链接至目标")
    :   node full handler

        This is a transfer camera data to uplayer api, when transfer node_len jpeg data finish , this function will be called

        Param curptr
        :   the start address of transfer data.

        Param newlen
        :   the transfer data length

        Param is_eof
        :   0/1: whether this packet data is the last packet of this frame, will called in jpeg_end_frame isr

        Param frame_len
        :   the complete jpeg frame size, if is_eof=1, the frame_len is the true value of jpeg frame size, is_eof=0, the frame_len=0, in other words, only when transfer really frame_len at the last packet in jpeg_end_frame isr

    void (*data_end_handler)(void)[](#_CPPv4N14video_config_t16data_end_handlerE "永久链接至目标")
    :   brief data_end_handler

        This api use to inforamte video transfer thread to deal transfer camera data

    media_camera_device_t *device[](#_CPPv4N14video_config_t6deviceE "永久链接至目标")
    :   config of camera

    uint16_t rxbuf_len[](#_CPPv4N14video_config_t9rxbuf_lenE "永久链接至目标")
    :   The length of receiving camera data buff

    uint16_t rx_read_len[](#_CPPv4N14video_config_t11rx_read_lenE "永久链接至目标")
    :   manage the node_full_handler callback function input params

    uint32_t node_len[](#_CPPv4N14video_config_t8node_lenE "永久链接至目标")
    :   video transfer network comunication protocol length a time

struct video_packet_t[](#_CPPv414video_packet_t "永久链接至目标")
:   Public Members

    uint32_t ptklen[](#_CPPv4N14video_packet_t6ptklenE "永久链接至目标")
    :   The current packet length

    uint32_t frame_id[](#_CPPv4N14video_packet_t8frame_idE "永久链接至目标")
    :   The current packet frame id

    uint32_t is_eof[](#_CPPv4N14video_packet_t6is_eofE "永久链接至目标")
    :   The current packet is the last packet

    uint32_t frame_len[](#_CPPv4N14video_packet_t9frame_lenE "永久链接至目标")
    :   The frame length

struct video_setup_t[](#_CPPv413video_setup_t "永久链接至目标")
:   Public Members

    media_camera_device_t *device[](#_CPPv4N13video_setup_t6deviceE "永久链接至目标")
    :   config of camera

    uint16_t open_type[](#_CPPv4N13video_setup_t9open_typeE "永久链接至目标")
    :   video transfer network comunication protocol type, video_open_type_t

    uint16_t send_type[](#_CPPv4N13video_setup_t9send_typeE "永久链接至目标")
    :   video transfer network comunication protocol type, video_send_type_t

    uint16_t pkt_header_size[](#_CPPv4N13video_setup_t15pkt_header_sizeE "永久链接至目标")
    :   packet header size

    uint16_t pkt_size[](#_CPPv4N13video_setup_t8pkt_sizeE "永久链接至目标")
    :   packet size

    [video_transfer_send_func](#_CPPv424video_transfer_send_func "video_transfer_send_func") send_func[](#_CPPv4N13video_setup_t9send_funcE "永久链接至目标")
    :   function ptr for send to uplayer

    [video_transfer_start_cb](#_CPPv423video_transfer_start_cb "video_transfer_start_cb") start_cb[](#_CPPv4N13video_setup_t8start_cbE "永久链接至目标")
    :   function ptr for start to send to uplayer

    [video_transfer_start_cb](#_CPPv423video_transfer_start_cb "video_transfer_start_cb") end_cb[](#_CPPv4N13video_setup_t6end_cbE "永久链接至目标")
    :   function ptr for end to send to uplayer

    [tvideo_add_pkt_header](#_CPPv421tvideo_add_pkt_header "tvideo_add_pkt_header") add_pkt_header[](#_CPPv4N13video_setup_t14add_pkt_headerE "永久链接至目标")
    :   function ptr for add packet header

struct video_header_t[](#_CPPv414video_header_t "永久链接至目标")
:   Public Members

    uint8_t id[](#_CPPv4N14video_header_t2idE "永久链接至目标")
    :   the frame id

    uint8_t is_eof[](#_CPPv4N14video_header_t6is_eofE "永久链接至目标")
    :   the flag of end frame, 1 for end

    uint8_t pkt_cnt[](#_CPPv4N14video_header_t7pkt_cntE "永久链接至目标")
    :   the packet index of one frame

    uint8_t pkt_seq[](#_CPPv4N14video_header_t7pkt_seqE "永久链接至目标")
    :   the total packets of one frame

struct video_buff_t[](#_CPPv412video_buff_t "永久链接至目标")
:   Public Members

    beken_semaphore_t aready_semaphore[](#_CPPv4N12video_buff_t16aready_semaphoreE "永久链接至目标")
    :   the video data receive complete

    uint8_t *buf_base[](#_CPPv4N12video_buff_t8buf_baseE "永久链接至目标")
    :   the receive video data, malloc by user

    uint32_t buf_len[](#_CPPv4N12video_buff_t7buf_lenE "永久链接至目标")
    :   video buff length, malloc by user

    uint32_t frame_id[](#_CPPv4N12video_buff_t8frame_idE "永久链接至目标")
    :   frame id

    uint32_t frame_pkt_cnt[](#_CPPv4N12video_buff_t13frame_pkt_cntE "永久链接至目标")
    :   the packet count of one frame

    uint8_t *buf_ptr[](#_CPPv4N12video_buff_t7buf_ptrE "永久链接至目标")
    :   recoder the buff ptr of every time receive video packte

    uint32_t frame_len[](#_CPPv4N12video_buff_t9frame_lenE "永久链接至目标")
    :   the length of receive one frame

    uint32_t start_buf[](#_CPPv4N12video_buff_t9start_bufE "永久链接至目标")
    :   video buff receive state


### Macros[](#macros "永久链接至标题")

VIDEO_UDP_TRAN_LEN[](#c.VIDEO_UDP_TRAN_LEN "永久链接至目标")

VIDEO_TCP_TRAN_LEN[](#c.VIDEO_TCP_TRAN_LEN "永久链接至目标")

TRAN_MAX_RETRY_TIME[](#c.TRAN_MAX_RETRY_TIME "永久链接至目标")

TRAN_RETRY_DELAY_TIME[](#c.TRAN_RETRY_DELAY_TIME "永久链接至目标")


### Type Definitions[](#type-definitions "永久链接至标题")

typedef void (*tvideo_add_pkt_header)([video_packet_t](#_CPPv414video_packet_t "video_packet_t") *param)[](#_CPPv421tvideo_add_pkt_header "永久链接至目标")

typedef int (*video_transfer_send_func)(uint8_t *data, uint32_t len)[](#_CPPv424video_transfer_send_func "永久链接至目标")

typedef void (*video_transfer_start_cb)(void)[](#_CPPv423video_transfer_start_cb "永久链接至目标")

typedef void (*video_transfer_end_cb)(void)[](#_CPPv421video_transfer_end_cb "永久链接至目标")


### Enumerations[](#enumerations "永久链接至标题")

enum video_open_type_t[](#_CPPv417video_open_type_t "永久链接至目标")
:   video sample module protocol type


    *Values:*

    enumerator TVIDEO_OPEN_NONE[](#_CPPv4N17video_open_type_t16TVIDEO_OPEN_NONEE "永久链接至目标")
    :   not sample module

    enumerator TVIDEO_OPEN_SCCB[](#_CPPv4N17video_open_type_t16TVIDEO_OPEN_SCCBE "永久链接至目标")
    :   sample module follow sccb protocol

    enumerator TVIDEO_OPEN_SPIDMA[](#_CPPv4N17video_open_type_t18TVIDEO_OPEN_SPIDMAE "永久链接至目标")
    :   sample module follow spidma protocol

    enumerator TVIDEO_OPEN_RTSP[](#_CPPv4N17video_open_type_t16TVIDEO_OPEN_RTSPE "永久链接至目标")
    :   sample module follow rtsp protocol

enum video_send_type_t[](#_CPPv417video_send_type_t "永久链接至目标")
:   video transfer network comunication protocol type


    *Values:*

    enumerator TVIDEO_SND_NONE[](#_CPPv4N17video_send_type_t15TVIDEO_SND_NONEE "永久链接至目标")
    :   not transfer

    enumerator TVIDEO_SND_UDP[](#_CPPv4N17video_send_type_t14TVIDEO_SND_UDPE "永久链接至目标")
    :   follow udp protocol

    enumerator TVIDEO_SND_TCP[](#_CPPv4N17video_send_type_t14TVIDEO_SND_TCPE "永久链接至目标")
    :   follow tcp protocol

    enumerator TVIDEO_SND_INTF[](#_CPPv4N17video_send_type_t15TVIDEO_SND_INTFE "永久链接至目标")
    :   transfer to inter frame

    enumerator TVIDEO_SND_BUFFER[](#_CPPv4N17video_send_type_t17TVIDEO_SND_BUFFERE "永久链接至目标")
    :   transfer to buffer

enum video_buff_state_t[](#_CPPv418video_buff_state_t "永久链接至目标")
:   *Values:*

    enumerator BUF_STA_INIT[](#_CPPv4N18video_buff_state_t12BUF_STA_INITE "永久链接至目标")
    :   video buff init

    enumerator BUF_STA_COPY[](#_CPPv4N18video_buff_state_t12BUF_STA_COPYE "永久链接至目标")
    :   video buff begin copy

    enumerator BUF_STA_GET[](#_CPPv4N18video_buff_state_t11BUF_STA_GETE "永久链接至目标")
    :   video frame get

    enumerator BUF_STA_FULL[](#_CPPv4N18video_buff_state_t12BUF_STA_FULLE "永久链接至目标")
    :   video buff full

    enumerator BUF_STA_DEINIT[](#_CPPv4N18video_buff_state_t14BUF_STA_DEINITE "永久链接至目标")
    :   video buff deinit

    enumerator BUF_STA_ERR[](#_CPPv4N18video_buff_state_t11BUF_STA_ERRE "永久链接至目标")
    :   other error
