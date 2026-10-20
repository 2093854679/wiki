---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/controller-guide/peripheral_guide/sdio.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="sdio"></a>

# SDIO 驱动

<a id="id1"></a>

## 概述

SDIO（Secure Digital Input/Output）是一种高速串行通信接口，主要用于与 SD 卡、WiFi 模块等设备通信。BK7239N 支持 SDIO 主机模式，提供高速数据传输能力。

<a id="id2"></a>

## 功能描述

- **主机模式**：支持 SDIO 主机模式，可控制 SDIO 从设备
- **命令传输**：支持 SDIO 命令的发送和响应接收
- **数据传输**：支持单块和多块数据传输
- **时钟配置**：支持多种时钟频率设置
- **总线宽度**：支持 1 位和 4 位总线宽度
- **中断支持**：支持命令完成、数据传输完成等中断
- **FIFO 支持**：内置 FIFO 缓冲，提高传输效率
- **错误检测**：支持 CRC 校验和错误检测

<a id="id3"></a>

## 开发指引

1. **初始化流程**
   \- 调用 bk\_sdio\_host\_driver\_init() 初始化 SDIO 主机驱动
   \- 配置 SDIO 主机参数（时钟频率、总线宽度等）
   \- 调用 bk\_sdio\_host\_init() 初始化 SDIO 主机
   \- 根据需要配置数据传输参数
2. **基本使用**
   \- 使用 bk\_sdio\_host\_send\_cmd() 发送命令
   \- 使用 bk\_sdio\_host\_wait\_cmd\_rsp() 等待命令响应
   \- 使用 bk\_sdio\_host\_config\_data() 配置数据传输
   \- 使用 bk\_sdio\_host\_wait\_receive\_data() 等待数据接收
3. **数据传输**
   \- 配置数据方向（读/写）
   \- 设置块大小和块数量
   \- 使用 FIFO 进行数据传输
   \- 处理传输完成中断
4. **错误处理**
   \- 检查命令响应状态
   \- 处理数据传输错误
   \- 使用超时机制防止死锁

<a id="id4"></a>

## 注意事项

- 确保在调用其他 SDIO API 前先调用 bk\_sdio\_host\_driver\_init()
- 时钟频率设置需要与从设备兼容
- 总线宽度设置需要与硬件连接匹配
- 使用中断模式时注意中断优先级设置
- 注意 SDIO 信号线的电气特性
- 低功耗模式下 SDIO 可能被关闭，需要重新初始化

<a id="api"></a>

## API 说明

主要 API 函数：

- bk\_sdio\_host\_driver\_init() \- 初始化 SDIO 主机驱动
- bk\_sdio\_host\_driver\_deinit() \- 反初始化 SDIO 主机驱动
- bk\_sdio\_host\_init() \- 初始化 SDIO 主机
- bk\_sdio\_host\_deinit() \- 反初始化 SDIO 主机
- bk\_sdio\_host\_set\_clock\_freq() \- 设置时钟频率
- bk\_sdio\_host\_send\_cmd() \- 发送命令
- bk\_sdio\_host\_wait\_cmd\_rsp() \- 等待命令响应
- bk\_sdio\_host\_config\_data() \- 配置数据传输
- bk\_sdio\_host\_wait\_receive\_data() \- 等待数据接收
- bk\_sdio\_host\_write\_fifo() \- 写入 FIFO
- bk\_sdio\_host\_read\_fifo() \- 读取 FIFO
- bk\_sdio\_host\_read\_blks\_fifo() \- 读取多个块到 FIFO

<a id="id5"></a>

## 示例代码

基本使用示例：

```
#include <driver/sdio_host.h>

void sdio_example(void)
{
    sdio_host_config_t config = {
        .clock_freq = SDIO_HOST_CLOCK_FREQ_25MHZ,
        .bus_width = SDIO_HOST_BUS_WIDTH_4BIT
    };

    // 初始化 SDIO 主机驱动
    bk_sdio_host_driver_init();

    // 初始化 SDIO 主机
    bk_sdio_host_init(&config);

    // 发送命令
    sdio_host_cmd_t cmd = {
        .cmd = 0,  // CMD0
        .arg = 0,
        .flags = SDIO_HOST_CMD_FLAG_NONE
    };
    bk_sdio_host_send_cmd(&cmd);

    // 等待命令响应
    uint32_t response;
    bk_sdio_host_wait_cmd_rsp(&response, 1000);
}
```

数据传输示例：

```
void sdio_data_transfer_example(void)
{
    // 配置数据传输
    sdio_host_data_config_t data_config = {
        .direction = SDIO_HOST_DATA_DIR_READ,
        .blk_cnt = 1,
        .blk_size = 512
    };
    bk_sdio_host_config_data(&data_config);

    // 等待数据接收
    bk_sdio_host_wait_receive_data();

    // 读取数据
    uint8_t buffer[512];
    bk_sdio_host_read_blks_fifo(buffer, 1);

    // 处理接收到的数据
    printf("Received %d bytes\n", 512);
}
```

多块读取示例：

```
void sdio_multi_block_example(void)
{
    // 配置多块读取
    sdio_host_data_config_t data_config = {
        .direction = SDIO_HOST_DATA_DIR_READ,
        .blk_cnt = 4,
        .blk_size = 512
    };
    bk_sdio_host_config_data(&data_config);

    // 等待数据接收
    bk_sdio_host_wait_receive_data();

    // 读取多个块
    uint8_t buffer[2048];  // 4 * 512
    bk_sdio_host_read_blks_fifo(buffer, 4);

    printf("Received %d blocks\n", 4);
}
```

<a id="id6"></a>

## 常见问题

- **命令响应超时**：检查时钟频率设置、信号线连接、从设备状态
- **数据传输失败**：确认总线宽度设置、块大小配置、FIFO 状态
- **CRC 错误**：检查信号完整性、时钟稳定性、电气连接
- **初始化失败**：确认 GPIO 映射、时钟配置、电源状态

<a id="id7"></a>

## 实战示例

1. 读取多个 512B 块

```
sdio_host_config_t cfg = { /* 频率/总线宽度 */ };
bk_sdio_host_driver_init();
bk_sdio_host_init(&cfg);
// 配置数据路径为读，块数=2
sdio_host_data_config_t dc = { /* direction=read, blk_cnt=2, blk_size=512 */ };
bk_sdio_host_config_data(&dc);
// 等待数据并读取
bk_sdio_host_wait_receive_data();
uint8_t buf[1024];
bk_sdio_host_read_blks_fifo(buf, 2);
```

<a id="id8"></a>

## 常见错误码说明

- BK\_ERR\_SDIO\_HOST\_NOT\_INIT：未初始化主机驱动或主机
- BK\_ERR\_SDIO\_HOST\_CMD\_RSP\_TIMEOUT/CRC\_FAIL：命令响应超时/CRC 失败
- BK\_ERR\_SDIO\_HOST\_DATA\_TIMEOUT/CRC\_FAIL：数据阶段超时/CRC 失败
