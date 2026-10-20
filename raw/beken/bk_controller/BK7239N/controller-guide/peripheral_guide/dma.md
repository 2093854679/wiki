---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/controller-guide/peripheral_guide/dma.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="dma"></a>

# DMA 驱动

<a id="id1"></a>

## 概述

DMA（Direct Memory Access）直接内存访问是一种硬件机制，允许外设直接与内存进行数据传输，无需CPU干预。BK7239N 支持多个 DMA 通道，提供高效的数据传输解决方案，减少 CPU 负载，提高系统性能。

<a id="id2"></a>

## 功能描述

- **多通道支持**：支持多个 DMA 通道同时工作
- **内存到内存**：支持内存到内存的数据传输
- **外设到内存**：支持外设到内存的数据传输
- **内存到外设**：支持内存到外设的数据传输
- **中断支持**：支持传输完成中断
- **通道管理**：支持 DMA 通道的分配和释放
- **传输配置**：支持灵活的传输参数配置
- **状态监控**：支持传输状态查询
- **低功耗**：支持低功耗模式下的 DMA 管理

<a id="id3"></a>

## 开发指引

1. **初始化流程**
   \- 调用 bk\_dma\_driver\_init() 初始化 DMA 驱动
   \- 使用 bk\_dma\_alloc() 分配 DMA 通道
   \- 配置传输参数（源地址、目标地址、传输长度等）
   \- 根据需要配置中断
2. **基本使用**
   \- 使用 bk\_dma\_set\_src\_addr() 设置源地址
   \- 使用 bk\_dma\_set\_dest\_addr() 设置目标地址
   \- 使用 bk\_dma\_set\_transfer\_len() 设置传输长度
   \- 使用 bk\_dma\_start() 启动传输
3. **通道管理**
   \- 使用 bk\_dma\_alloc() 分配通道
   \- 使用 bk\_dma\_free() 释放通道
   \- 使用 bk\_dma\_get\_remain\_len() 查询剩余传输长度
4. **中断处理**
   \- 注册传输完成中断回调
   \- 在中断中处理传输状态
   \- 根据需要启用/禁用中断

<a id="id4"></a>

## 注意事项

- 确保在调用其他 DMA API 前先调用 bk\_dma\_driver\_init()
- DMA 通道分配需要在任务上下文中进行
- 传输地址需要确保内存对齐
- 使用中断模式时注意中断优先级设置
- 注意 DMA 传输的缓存一致性
- 低功耗模式下 DMA 可能被关闭，需要重新初始化

<a id="api"></a>

## API 说明

主要 API 函数：

- bk\_dma\_driver\_init() \- 初始化 DMA 驱动
- bk\_dma\_driver\_deinit() \- 反初始化 DMA 驱动
- bk\_dma\_alloc() \- 分配 DMA 通道
- bk\_dma\_free() \- 释放 DMA 通道
- bk\_dma\_set\_src\_addr() \- 设置源地址
- bk\_dma\_set\_dest\_addr() \- 设置目标地址
- bk\_dma\_set\_transfer\_len() \- 设置传输长度
- bk\_dma\_start() \- 启动 DMA 传输
- bk\_dma\_stop() \- 停止 DMA 传输
- bk\_dma\_get\_remain\_len() \- 获取剩余传输长度
- bk\_dma\_register\_isr() \- 注册中断服务函数
- bk\_dma\_unregister\_isr() \- 注销中断服务函数
- bk\_dma\_enable\_interrupt() \- 启用中断
- bk\_dma\_disable\_interrupt() \- 禁用中断
- bk\_dma\_clear\_interrupt() \- 清除中断标志
- bk\_dma\_get\_status() \- 获取 DMA 状态
- bk\_dma\_wait\_finish() \- 等待传输完成

<a id="id5"></a>

## 示例代码

基本使用示例：

```
#include <driver/dma.h>

void dma_example(void)
{
    // 初始化 DMA 驱动
    bk_dma_driver_init();

    // 分配 DMA 通道
    dma_id_t dma_chan = bk_dma_alloc(0x1000);  // 用户ID
    if (dma_chan >= DMA_ID_MAX) {
        printf("DMA channel allocation failed\n");
        return;
    }

    // 准备数据
    uint8_t src_data[1024];
    uint8_t dst_data[1024];
    for (int i = 0; i < 1024; i++) {
        src_data[i] = i & 0xFF;
    }

    // 配置 DMA 传输
    bk_dma_set_src_addr(dma_chan, (uint32_t)src_data);
    bk_dma_set_dest_addr(dma_chan, (uint32_t)dst_data);
    bk_dma_set_transfer_len(dma_chan, 1024);

    // 启动传输
    bk_dma_start(dma_chan);

    // 等待传输完成
    bk_dma_wait_finish(dma_chan);

    // 释放通道
    bk_dma_free(0x1000, dma_chan);
}
```

中断处理示例：

```
static void dma_interrupt_handler(dma_id_t id, void *param)
{
    printf("DMA channel %d transfer complete\n", id);

    // 清除中断标志
    bk_dma_clear_interrupt(id);
}

void dma_interrupt_example(void)
{
    // 分配 DMA 通道
    dma_id_t dma_chan = bk_dma_alloc(0x1001);
    if (dma_chan >= DMA_ID_MAX) {
        return;
    }

    // 注册中断服务函数
    bk_dma_register_isr(dma_chan, dma_interrupt_handler, NULL);

    // 启用中断
    bk_dma_enable_interrupt(dma_chan);

    // 配置并启动传输
    uint8_t src[512], dst[512];
    bk_dma_set_src_addr(dma_chan, (uint32_t)src);
    bk_dma_set_dest_addr(dma_chan, (uint32_t)dst);
    bk_dma_set_transfer_len(dma_chan, 512);
    bk_dma_start(dma_chan);
}
```

外设到内存传输示例：

```
void dma_peripheral_to_memory_example(void)
{
    dma_id_t dma_chan = bk_dma_alloc(0x1002);
    if (dma_chan >= DMA_ID_MAX) {
        return;
    }

    // 配置外设到内存传输
    uint8_t buffer[256];
    bk_dma_set_src_addr(dma_chan, UART0_RX_ADDR);  // 外设地址
    bk_dma_set_dest_addr(dma_chan, (uint32_t)buffer);
    bk_dma_set_transfer_len(dma_chan, 256);

    // 启动传输
    bk_dma_start(dma_chan);

    // 等待传输完成
    while (bk_dma_get_remain_len(dma_chan) > 0) {
        // 等待传输完成
    }

    // 处理接收到的数据
    printf("Received %d bytes\n", 256);

    // 释放通道
    bk_dma_free(0x1002, dma_chan);
}
```

状态监控示例：

```
void dma_status_example(void)
{
    dma_id_t dma_chan = bk_dma_alloc(0x1003);
    if (dma_chan >= DMA_ID_MAX) {
        return;
    }

    // 配置传输
    uint8_t src[1024], dst[1024];
    bk_dma_set_src_addr(dma_chan, (uint32_t)src);
    bk_dma_set_dest_addr(dma_chan, (uint32_t)dst);
    bk_dma_set_transfer_len(dma_chan, 1024);

    // 启动传输
    bk_dma_start(dma_chan);

    // 监控传输状态
    while (1) {
        uint32_t remain_len = bk_dma_get_remain_len(dma_chan);
        dma_status_t status = bk_dma_get_status(dma_chan);

        printf("Remain: %d, Status: %d\n", remain_len, status);

        if (remain_len == 0) {
            printf("Transfer complete\n");
            break;
        }

        rtos_delay_milliseconds(10);
    }

    // 释放通道
    bk_dma_free(0x1003, dma_chan);
}
```

<a id="id6"></a>

## 常见问题

- **通道分配失败**：检查是否有可用通道、用户ID是否正确
- **传输失败**：检查地址对齐、传输长度、源目标地址有效性
- **中断未触发**：确认中断注册和启用，检查中断优先级设置
- **数据不一致**：检查缓存一致性、内存屏障使用

<a id="id7"></a>

## 实战示例

1. 内存到内存高速传输

```
dma_id_t chan = bk_dma_alloc(0x1000);
bk_dma_set_src_addr(chan, (uint32_t)src_buf);
bk_dma_set_dest_addr(chan, (uint32_t)dst_buf);
bk_dma_set_transfer_len(chan, 4096);
bk_dma_start(chan);
bk_dma_wait_finish(chan);
```

<a id="id8"></a>

## 常见错误码说明

- BK\_ERR\_DMA\_NOT\_INIT：未调用 bk\_dma\_driver\_init()
- BK\_ERR\_DMA\_INVALID\_ID：DMA 通道 ID 非法
- BK\_ERR\_DMA\_CHANNEL\_BUSY：DMA 通道忙
- BK\_ERR\_DMA\_TRANSFER\_FAIL：DMA 传输失败
