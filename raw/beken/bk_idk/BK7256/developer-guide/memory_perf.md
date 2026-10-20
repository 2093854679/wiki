---
type: official-document
source_url: https://docs.bekencorp.com/armino/bk7256/zh_CN/v1.5/developer-guide/memory_perf/index.html
sdk_family: bk_idk
chip: BK7256
processor: ''
sdk_version: v1.5
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="id1"></a>

# 内存与性能

<a id="id2"></a>

# 1、内存概述

> BK7256芯片整体有4\*128K sram，双核各有独立的32k dtcm和32k itcm，8M PSRAM

<a id="psram"></a>

# 2、PSRAM概述

> > BK7256芯片有8M PSRAM，当前默认将最后1M(0x60700000\~0x60800000)用作堆内存使用，可通过宏 `CONFIG_PSRAM_HEAP_BASE` 和 `CONFIG_PSRAM_HEAP_SIZE` 进行配置来扩大堆内存，这两个宏的设置值以十进制为单位。
>
> - 功能开关CONFIG\_PSRAM\_AS\_SYS\_MEMORY依赖CONFIG\_PSRAM和CONFIG\_FREERTOS\_V10
> - 内存接口psram\_malloc和psram\_free
> - BK7256芯片PSRAM只支持4字节对齐访问，必须按照WORD操作PSRAM申请内存并保证4字节对齐
>
>   ```
>   #include <os/mem.h>
>
>   #define os_write_word(addr,val)                 *((volatile uint32_t *)(addr)) = val
>   #define os_read_word(addr,val)                  val = *((volatile uint32_t *)(addr))
>   #define os_get_word(addr)                       *((volatile uint32_t *)(addr))
>
>   void os_memcpy_word(uint32_t *out, const uint32_t *in, uint32_t n);
>   void os_memset_word(uint32_t *b, int32_t c, uint32_t n);
>   ```
> - 此外，由于BK7256芯片PSRAM必须4字节对齐访问，在对PSRAM内存进行写入时，需要注意访问的地址必须四字节对齐，且为了满足一些需要对PSRAM内存进行1字节或者2字节写入的需求，故而封装了以下四个函数供使用，这些函数都无需使用者考虑地址是否对齐，代码路径为：`.\include\driver\psram.h`，具体分别是
>
>   ```
>   static inline void bk_psram_byte_write(unsigned char *addr, unsigned char value);        //PSRAM 1字节数据写入
>   static inline void bk_psram_half_word_write(unsigned short *dst, unsigned short value);  //PSRAM 2字节数据写入
>   static inline void bk_psram_word_write(unsigned int *src, unsigned int value);           //PSRAM 4字节数据写入
>   static inline void bk_psram_word_memcpy(void *dst_t, void *src_t, unsigned int length);  //PSRAM 内存拷贝
>   ```
> - BK7256芯片低压功能PARAM会下电，退出低压模式时必须使用void bk\_psram\_heap\_init(void)接口重新初始化PSRAM Heap内存，
>   并且之前通过psram\_malloc申请的内存，不能再使用。

<a id="id3"></a>

# 3\. PSRAM 划分

> > BK7256芯片有8M PSRAM，前7M主要用于Camera数据采集、LCD图像显示；
>
> - 800\*600分辨率
>
>   ```
>   yuv图片存储地址范围，0x60000000-0x603BFFFF，共4帧，
>       显示占用1帧，pingpang buffer占用1帧，jpeg解码占用1帧，旋转占用1帧；
>   jpeg图片存储地址范围0x603C0000-0x60488000，共4帧，
>       camera采集占用1帧，jpeg解码占用1帧，图传使用时占用1帧，存图使用时占用1帧；
>   ```
> - 1280\*720分辨率
>
>   ```
>   yuv图片存储地址范围，0x60000000-0x6056FFFF，共3帧，
>       显示占用1帧，pingpang buffer占用1帧，jpeg解码占用1帧；
>   jpeg图片存储地址范围，0x60570000-0x60637FFF，共4帧，
>       camera采集占用1帧，jpeg解码占用1帧，图传使用时占用1帧，存图使用时占用1帧；
>   ```
> - LVGL画图
>
>   ```
>   LVGL画图起始地址：0x60500000 (可配置)
>   ```
