---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/controller-guide/peripheral_guide/efuse.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="efuse"></a>

# efuse 驱动

<a id="id1"></a>

## 概述

efuse（Electrically Fusable）电熔丝是一种一次可编程存储器，用于存储芯片的唯一标识、配置参数、密钥等关键信息。BK7239N 内置 efuse 存储器，提供安全可靠的数据存储解决方案。

<a id="id2"></a>

## 功能描述

- **一次可编程**：efuse 只能从 0 编程为 1，不能从 1 变为 0
- **永久存储**：数据一旦写入，永久保存，断电不丢失
- **安全存储**：适合存储密钥、证书等敏感信息
- **唯一标识**：支持芯片唯一标识存储
- **配置参数**：支持系统配置参数存储
- **地址管理**：支持灵活的地址空间管理
- **数据验证**：支持写入数据验证
- **低功耗**：支持低功耗模式下的数据保持

<a id="id3"></a>

## 开发指引

1. **初始化流程**
   \- 调用 bk\_efuse\_driver\_init() 初始化 efuse 驱动
   \- 确认要写入的地址区域可用
   \- 准备要写入的数据
2. **基本使用**
   \- 使用 bk\_efuse\_write\_byte() 写入单字节数据
   \- 使用 bk\_efuse\_read\_byte() 读取单字节数据
   \- 注意 efuse 只能从 0 编程为 1
3. **地址管理**
   \- 确认地址范围在有效范围内
   \- 避免重复写入同一地址
   \- 注意地址区域的用途限制
4. **数据验证**
   \- 写入后立即读取验证
   \- 检查数据是否正确写入
   \- 处理写入失败的情况

<a id="id4"></a>

## 注意事项

- 确保在调用其他 efuse API 前先调用 bk\_efuse\_driver\_init()
- efuse 只能从 0 编程为 1，不能从 1 变为 0
- 写入操作不可逆，请谨慎操作
- 地址范围需要确认在有效范围内
- 写入前需要向 PM 申请地址区域
- 注意 efuse 的寿命限制

<a id="api"></a>

## API 说明

主要 API 函数：

- bk\_efuse\_driver\_init() \- 初始化 efuse 驱动
- bk\_efuse\_driver\_deinit() \- 反初始化 efuse 驱动
- bk\_efuse\_write\_byte() \- 写入单字节数据
- bk\_efuse\_read\_byte() \- 读取单字节数据

<a id="id5"></a>

## 示例代码

基本使用示例：

```
#include <driver/efuse.h>

void efuse_example(void)
{
    // 初始化 efuse 驱动
    bk_efuse_driver_init();

    // 写入数据到 efuse
    uint8_t write_data = 0xAA;
    bk_err_t ret = bk_efuse_write_byte(0x10, write_data);
    if (ret != BK_OK) {
        printf("efuse write failed: %d\n", ret);
        return;
    }

    // 读取数据验证
    uint8_t read_data;
    ret = bk_efuse_read_byte(0x10, &read_data);
    if (ret == BK_OK) {
        printf("efuse read: 0x%02X\n", read_data);
    }
}
```

批量读写示例：

```
void efuse_batch_example(void)
{
    uint8_t write_data[] = {0x01, 0x02, 0x03, 0x04};
    uint8_t read_data[4];

    // 批量写入
    for (int i = 0; i < 4; i++) {
        bk_err_t ret = bk_efuse_write_byte(0x20 + i, write_data[i]);
        if (ret != BK_OK) {
            printf("Write failed at address 0x%02X\n", 0x20 + i);
            return;
        }
    }

    // 批量读取验证
    for (int i = 0; i < 4; i++) {
        bk_err_t ret = bk_efuse_read_byte(0x20 + i, &read_data[i]);
        if (ret == BK_OK) {
            printf("Address 0x%02X: 0x%02X\n", 0x20 + i, read_data[i]);
        }
    }
}
```

安全存储示例：

```
void efuse_secure_storage_example(void)
{
    // 存储密钥
    uint8_t key[] = {0x12, 0x34, 0x56, 0x78, 0x9A, 0xBC, 0xDE, 0xF0};
    uint8_t key_addr = 0x30;

    // 写入密钥
    for (int i = 0; i < 8; i++) {
        bk_err_t ret = bk_efuse_write_byte(key_addr + i, key[i]);
        if (ret != BK_OK) {
            printf("Key write failed at index %d\n", i);
            return;
        }
    }

    // 验证密钥
    uint8_t verify_key[8];
    for (int i = 0; i < 8; i++) {
        bk_efuse_read_byte(key_addr + i, &verify_key[i]);
    }

    // 比较密钥
    bool key_match = true;
    for (int i = 0; i < 8; i++) {
        if (key[i] != verify_key[i]) {
            key_match = false;
            break;
        }
    }

    printf("Key verification: %s\n", key_match ? "PASS" : "FAIL");
}
```

配置参数存储示例：

```
void efuse_config_example(void)
{
    // 存储配置参数
    struct {
        uint8_t device_id;
        uint8_t version;
        uint8_t features;
        uint8_t reserved;
    } config = {
        .device_id = 0x01,
        .version = 0x02,
        .features = 0x03,
        .reserved = 0x00
    };

    uint8_t config_addr = 0x40;

    // 写入配置
    bk_efuse_write_byte(config_addr, config.device_id);
    bk_efuse_write_byte(config_addr + 1, config.version);
    bk_efuse_write_byte(config_addr + 2, config.features);
    bk_efuse_write_byte(config_addr + 3, config.reserved);

    // 读取配置
    uint8_t read_config[4];
    for (int i = 0; i < 4; i++) {
        bk_efuse_read_byte(config_addr + i, &read_config[i]);
    }

    printf("Device ID: 0x%02X\n", read_config[0]);
    printf("Version: 0x%02X\n", read_config[1]);
    printf("Features: 0x%02X\n", read_config[2]);
}
```

<a id="id6"></a>

## 常见问题

- **写入失败**：检查地址范围、数据格式、efuse 状态
- **读取错误**：确认地址有效性、驱动初始化状态
- **数据不匹配**：检查写入操作是否成功、地址是否正确
- **地址冲突**：确认地址区域使用情况、避免重复写入

<a id="id7"></a>

## 实战示例

1. 存储芯片唯一标识

```
void efuse_chip_id_example(void)
{
    uint8_t chip_id[4] = {0x12, 0x34, 0x56, 0x78};
    uint8_t id_addr = 0x00;

    // 写入芯片ID
    for (int i = 0; i < 4; i++) {
        bk_efuse_write_byte(id_addr + i, chip_id[i]);
    }

    // 读取验证
    uint8_t read_id[4];
    for (int i = 0; i < 4; i++) {
        bk_efuse_read_byte(id_addr + i, &read_id[i]);
    }
}
```

<a id="id8"></a>

## 常见错误码说明

- BK\_ERR\_EFUSE\_DRIVER\_NOT\_INIT：未调用 bk\_efuse\_driver\_init()
- BK\_ERR\_EFUSE\_ADDR\_OUT\_OF\_RANGE：efuse 地址超出范围
- BK\_ERR\_EFUSE\_CANNOT\_WRTIE：efuse 无法写入，不能将位从 1 变为 0
- BK\_ERR\_EFUSE\_WRTIE\_NOT\_EQUAL：efuse 读取数据与写入数据不相等
