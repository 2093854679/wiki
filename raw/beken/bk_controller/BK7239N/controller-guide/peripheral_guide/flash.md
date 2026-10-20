---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/controller-guide/peripheral_guide/flash.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="flash"></a>

# FLASH 驱动

<a id="id1"></a>

## 概述

FLASH 存储器是 BK7239N 系统的重要组成部分，用于存储程序代码、配置数据和用户数据。FLASH 驱动提供了对 FLASH 存储器的完整访问接口，支持读写、擦除、保护等操作。

<a id="id2"></a>

## 功能描述

- **初始化管理**：支持 FLASH 驱动初始化和反初始化
- **并发保护**：支持多任务环境下的并发访问保护
- **线制模式**：支持单线、双线、四线等不同线制模式
- **ID 识别**：支持 FLASH 器件 ID 读取和识别
- **时钟配置**：支持 DPLL 和 DCO 时钟源配置
- **写保护**：支持写使能/禁用和多种保护类型
- **状态管理**：支持状态寄存器读写和状态查询
- **擦除操作**：支持扇区擦除和块擦除
- **读写操作**：支持字节、字、多字节读写
- **低功耗管理**：支持深度睡眠和唤醒
- **电源管理**：支持电源保存和恢复回调
- **时钟切换**：支持运行时时钟源切换
- **忙状态检测**：支持 FLASH 忙状态检测

<a id="id3"></a>

## 开发指引

1. **初始化流程**
   \- 调用 bk\_flash\_driver\_init() 初始化 FLASH 驱动
   \- 配置 FLASH 线制模式
   \- 设置时钟源和频率
   \- 根据需要配置写保护
2. **基本使用**
   \- 使用 bk\_flash\_read\_bytes() 读取数据
   \- 使用 bk\_flash\_write\_bytes() 写入数据
   \- 使用 bk\_flash\_erase\_sector() 擦除扇区
   \- 使用 bk\_flash\_erase\_block() 擦除块
3. **并发保护**
   \- 在多任务环境中使用 bk\_flash\_lock() 和 bk\_flash\_unlock()
   \- 确保 FLASH 操作的原子性
   \- 避免并发访问冲突
4. **低功耗管理**
   \- 使用 bk\_flash\_deep\_sleep\_entry() 进入深度睡眠
   \- 使用 bk\_flash\_deep\_sleep\_exit() 退出深度睡眠
   \- 配置电源保存和恢复回调

<a id="id4"></a>

## 注意事项

- 确保在调用其他 FLASH API 前先调用 bk\_flash\_driver\_init()
- 擦除操作会清除整个扇区或块的数据
- 写入操作前需要先擦除对应区域
- 注意 FLASH 的寿命限制和擦除次数
- 使用并发保护机制避免数据损坏
- 低功耗模式下 FLASH 可能被关闭，需要重新初始化

<a id="api"></a>

## API 说明

主要 API 函数：

- bk\_flash\_driver\_init() \- 初始化 FLASH 驱动
- bk\_flash\_driver\_deinit() \- 反初始化 FLASH 驱动
- bk\_flash\_lock() \- 锁定 FLASH 操作
- bk\_flash\_unlock() \- 解锁 FLASH 操作
- bk\_flash\_set\_line\_mode() \- 设置线制模式
- bk\_flash\_get\_line\_mode() \- 获取线制模式
- bk\_flash\_get\_id() \- 获取 FLASH ID
- bk\_flash\_set\_clock\_dpll() \- 设置 DPLL 时钟
- bk\_flash\_set\_clock\_dco() \- 设置 DCO 时钟
- bk\_flash\_write\_enable() \- 写使能
- bk\_flash\_write\_disable() \- 写禁用
- bk\_flash\_set\_protect\_type() \- 设置保护类型
- bk\_flash\_read\_status\_reg() \- 读取状态寄存器
- bk\_flash\_write\_status\_reg() \- 写入状态寄存器
- bk\_flash\_erase\_sector() \- 擦除扇区
- bk\_flash\_erase\_block() \- 擦除块
- bk\_flash\_deep\_sleep\_entry() \- 进入深度睡眠
- bk\_flash\_deep\_sleep\_exit() \- 退出深度睡眠
- bk\_flash\_write\_bytes() \- 写入字节
- bk\_flash\_read\_bytes() \- 读取字节
- bk\_flash\_write\_word() \- 写入字
- bk\_flash\_read\_word() \- 读取字
- bk\_flash\_driver\_inited() \- 检查驱动是否初始化
- bk\_flash\_get\_total\_size() \- 获取总大小
- bk\_flash\_power\_save\_suspend() \- 电源保存挂起
- bk\_flash\_power\_save\_resume() \- 电源保存恢复
- bk\_flash\_clock\_switch() \- 时钟切换
- bk\_flash\_busy\_wait() \- 忙等待
- bk\_flash\_get\_operate\_status() \- 获取操作状态

<a id="id5"></a>

## 示例代码

基本使用示例：

```
#include <driver/flash.h>

void flash_example(void)
{
    // 初始化 FLASH 驱动
    bk_flash_driver_init();

    // 设置四线模式
    bk_flash_set_line_mode(FLASH_LINE_MODE_4);

    // 读取 FLASH ID
    uint32_t flash_id = bk_flash_get_id();
    printf("Flash ID: 0x%08X\n", flash_id);

    // 读取数据
    uint8_t read_data[256];
    bk_flash_read_bytes(0x1000, read_data, sizeof(read_data));

    // 写入数据
    uint8_t write_data[256];
    for (int i = 0; i < 256; i++) {
        write_data[i] = i & 0xFF;
    }
    bk_flash_write_bytes(0x2000, write_data, sizeof(write_data));
}
```

擦除操作示例：

```
void flash_erase_example(void)
{
    // 锁定 FLASH 操作
    bk_flash_lock();

    // 擦除扇区
    bk_flash_erase_sector(0x1000);

    // 擦除块
    bk_flash_erase_block(0x2000);

    // 解锁 FLASH 操作
    bk_flash_unlock();
}
```

低功耗管理示例：

```
void flash_power_management_example(void)
{
    // 进入深度睡眠
    bk_flash_deep_sleep_entry();

    // 系统进入低功耗模式
    // ...

    // 退出深度睡眠
    bk_flash_deep_sleep_exit();
}
```

状态检查示例：

```
void flash_status_example(void)
{
    // 检查驱动是否初始化
    if (bk_flash_driver_inited()) {
        printf("Flash driver initialized\n");
    }

    // 获取总大小
    uint32_t total_size = bk_flash_get_total_size();
    printf("Flash total size: %d bytes\n", total_size);

    // 读取状态寄存器
    uint16_t status = bk_flash_read_status_reg();
    printf("Flash status: 0x%04X\n", status);

    // 检查操作状态
    flash_operate_status_t op_status = bk_flash_get_operate_status();
    printf("Operate status: %d\n", op_status);
}
```

<a id="id6"></a>

## 常见问题

- **写入失败**：检查写保护状态、擦除状态、地址范围
- **读取错误**：检查地址范围、线制模式、时钟配置
- **擦除失败**：确认扇区/块地址、写保护状态
- **并发冲突**：使用锁机制保护并发访问

<a id="id7"></a>

## 实战示例

1. 读取 Flash ID 与状态寄存器

```
bk_flash_driver_init();
uint32_t id = bk_flash_get_id();
uint16_t sr = bk_flash_read_status_reg();
```

<a id="id8"></a>

## 常见错误码说明

- BK\_ERR\_FLASH\_ADDR\_OUT\_OF\_RANGE：读写/擦除地址越界
- 其他错误：通常与底层 QSPI/SPI 访问失败、保护限制或频率过高有关
