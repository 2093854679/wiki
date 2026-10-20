---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/controller-guide/peripheral_guide/i2c.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="i2c"></a>

# I2C 驱动

<a id="id1"></a>

## 概述

I2C（Inter-Integrated Circuit）是一种两线制串行通信协议，广泛用于微控制器与各种外设之间的低速数据传输。BK7239N 支持多个 I2C 通道，提供灵活的主从通信解决方案。

<a id="id2"></a>

## 功能描述

- **多通道支持**：支持多个 I2C 通道同时工作
- **主从模式**：支持 I2C 主机和从机模式
- **时钟配置**：支持多种时钟频率设置
- **地址配置**：支持 7 位和 10 位设备地址
- **中断支持**：支持传输完成、错误等中断
- **超时机制**：支持传输超时检测
- **状态查询**：支持总线状态和传输状态查询
- **内存读写**：支持 I2C 内存设备读写
- **低功耗**：支持低功耗模式，节省功耗

<a id="id3"></a>

## 开发指引

1. **初始化流程**
   \- 调用 bk\_i2c\_driver\_init() 初始化 I2C 驱动
   \- 配置 I2C 参数（时钟频率、模式等）
   \- 调用 bk\_i2c\_init() 初始化具体 I2C 通道
   \- 根据需要配置中断
2. **主机模式使用**
   \- 使用 bk\_i2c\_master\_write() 向从设备写入数据
   \- 使用 bk\_i2c\_master\_read() 从从设备读取数据
   \- 使用 bk\_i2c\_master\_mem\_write() 和 bk\_i2c\_master\_mem\_read() 进行内存读写
3. **从机模式使用**
   \- 使用 bk\_i2c\_slave\_write() 向主机发送数据
   \- 使用 bk\_i2c\_slave\_read() 从主机接收数据
   \- 设置从机地址和中断处理
4. **错误处理**
   \- 检查传输状态和错误码
   \- 使用超时机制防止死锁
   \- 处理总线错误和仲裁丢失

<a id="id4"></a>

## 注意事项

- 确保在调用其他 I2C API 前先调用 bk\_i2c\_driver\_init()
- 时钟频率设置需要与从设备兼容
- 设备地址设置需要与硬件连接匹配
- 使用中断模式时注意中断优先级设置
- 注意 I2C 信号线的电气特性和上拉电阻
- 低功耗模式下 I2C 可能被关闭，需要重新初始化
- 多设备共享总线时注意地址冲突

<a id="api"></a>

## API 说明

主要 API 函数：

- bk\_i2c\_driver\_init() \- 初始化 I2C 驱动
- bk\_i2c\_driver\_deinit() \- 反初始化 I2C 驱动
- bk\_i2c\_init() \- 初始化 I2C 通道
- bk\_i2c\_deinit() \- 反初始化 I2C 通道
- bk\_i2c\_master\_write() \- 主机写入数据
- bk\_i2c\_master\_read() \- 主机读取数据
- bk\_i2c\_master\_mem\_write() \- 主机写入内存
- bk\_i2c\_master\_mem\_read() \- 主机读取内存
- bk\_i2c\_slave\_write() \- 从机写入数据
- bk\_i2c\_slave\_read() \- 从机读取数据
- bk\_i2c\_set\_baud\_rate() \- 设置波特率
- bk\_i2c\_set\_slave\_addr() \- 设置从机地址
- bk\_i2c\_enable\_interrupt() \- 启用中断
- bk\_i2c\_disable\_interrupt() \- 禁用中断
- bk\_i2c\_is\_bus\_busy() \- 检查总线忙状态
- bk\_i2c\_get\_current\_action() \- 获取当前操作
- bk\_i2c\_get\_bus\_state() \- 获取总线状态
- bk\_i2c\_get\_transaction\_state() \- 获取传输状态

<a id="id5"></a>

## 示例代码

基本使用示例：

```
#include <driver/i2c.h>

void i2c_example(void)
{
    i2c_config_t config = {
        .baud_rate = 100000,  // 100kHz
        .mode = I2C_MODE_MASTER
    };

    // 初始化 I2C 驱动
    bk_i2c_driver_init();

    // 初始化 I2C0
    bk_i2c_init(I2C_ID_0, &config);

    // 写入数据到从设备
    uint8_t data[] = {0x01, 0x02, 0x03};
    bk_i2c_master_write(I2C_ID_0, 0x50, data, sizeof(data), 1000);

    // 从从设备读取数据
    uint8_t rx_data[3];
    bk_i2c_master_read(I2C_ID_0, 0x50, rx_data, sizeof(rx_data), 1000);

    printf("I2C Data: %02X %02X %02X\n", rx_data[0], rx_data[1], rx_data[2]);
}
```

内存读写示例：

```
void i2c_memory_example(void)
{
    // 写入内存地址 0x1000
    uint8_t write_data[] = {0xAA, 0xBB, 0xCC};
    bk_i2c_master_mem_write(I2C_ID_0, 0x50, 0x1000, write_data, sizeof(write_data), 1000);

    // 从内存地址 0x1000 读取数据
    uint8_t read_data[3];
    bk_i2c_master_mem_read(I2C_ID_0, 0x50, 0x1000, read_data, sizeof(read_data), 1000);

    printf("Memory Data: %02X %02X %02X\n", read_data[0], read_data[1], read_data[2]);
}
```

从机模式示例：

```
static void i2c_slave_callback(i2c_id_t id, void *param)
{
    uint8_t data[32];
    int len = bk_i2c_slave_read(id, data, sizeof(data));
    if (len > 0) {
        printf("Slave received %d bytes\n", len);
        // 处理接收到的数据
    }
}

void i2c_slave_example(void)
{
    i2c_config_t config = {
        .baud_rate = 100000,
        .mode = I2C_MODE_SLAVE
    };

    // 初始化从机模式
    bk_i2c_init(I2C_ID_0, &config);

    // 设置从机地址
    bk_i2c_set_slave_addr(I2C_ID_0, 0x30);

    // 注册中断回调
    bk_i2c_register_isr(I2C_ID_0, i2c_slave_callback, NULL);
    bk_i2c_enable_interrupt(I2C_ID_0);
}
```

状态检查示例：

```
void i2c_status_example(void)
{
    // 检查总线是否忙
    if (bk_i2c_is_bus_busy(I2C_ID_0)) {
        printf("I2C Bus is busy\n");
        return;
    }

    // 获取当前操作状态
    i2c_action_t action = bk_i2c_get_current_action(I2C_ID_0);
    printf("Current action: %d\n", action);

    // 获取总线状态
    i2c_bus_state_t bus_state = bk_i2c_get_bus_state(I2C_ID_0);
    printf("Bus state: %d\n", bus_state);
}
```

<a id="id6"></a>

## 常见问题

- **通信失败**：检查设备地址、时钟频率、信号线连接
- **总线忙**：等待总线空闲或检查是否有其他设备占用
- **超时错误**：增加超时时间或检查从设备响应
- **地址冲突**：确认设备地址设置正确，避免地址冲突

<a id="id7"></a>

## 实战示例

1. 读取寄存器（带寄存器地址）

```
// 写寄存器地址
uint8_t reg = 0x10;
bk_i2c_master_write(I2C_ID_0, 0x50, &reg, 1, 100);
// 读寄存器数据
uint8_t val = 0;
bk_i2c_master_read(I2C_ID_0, 0x50, &val, 1, 100);
```

<a id="id8"></a>

## 常见错误码说明

- BK\_ERR\_I2C\_NOT\_INIT：未调用 bk\_i2c\_driver\_init()
- BK\_ERR\_I2C\_INVALID\_ID：I2C 通道 ID 非法
- BK\_ERR\_I2C\_ID\_NOT\_INIT：未对通道调用 bk\_i2c\_init()
