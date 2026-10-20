---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/controller-guide/peripheral_guide/wdg.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="wdg"></a>

# WDG 驱动

<a id="id1"></a>

## 概述

WDG（Watchdog）看门狗是一种硬件定时器，用于监控系统运行状态，防止系统死锁或异常。当系统在预定时间内没有喂狗时，看门狗会自动复位系统，确保系统可靠性。

<a id="id2"></a>

## 功能描述

- **定时监控**：支持定时监控系统运行状态
- **自动复位**：支持超时自动复位系统
- **启动停止**：支持看门狗的启动和停止控制
- **喂狗功能**：支持定期喂狗防止复位
- **时间管理**：支持喂狗时间设置和获取
- **状态查询**：支持看门狗状态查询
- **低功耗**：支持低功耗模式下的看门狗管理

<a id="id3"></a>

## 开发指引

1. **初始化流程**
   \- 调用 bk\_wdt\_driver\_init() 初始化看门狗驱动
   \- 设置看门狗超时时间
   \- 调用 bk\_wdt\_start() 启动看门狗
   \- 在应用中定期调用 bk\_wdt\_feed() 喂狗
2. **基本使用**
   \- 使用 bk\_wdt\_start() 启动看门狗
   \- 使用 bk\_wdt\_feed() 定期喂狗
   \- 使用 bk\_wdt\_stop() 停止看门狗
   \- 使用 bk\_wdt\_set\_feed\_time() 设置喂狗时间
3. **时间管理**
   \- 使用 bk\_wdt\_get\_feed\_time() 获取当前喂狗时间
   \- 使用 bk\_wdt\_set\_feed\_time() 设置新的喂狗时间
   \- 根据应用需求调整喂狗间隔
4. **状态监控**
   \- 使用 bk\_wdt\_driver\_inited() 检查驱动状态
   \- 监控看门狗运行状态
   \- 处理看门狗复位事件

<a id="id4"></a>

## 注意事项

- 确保在调用其他 WDT API 前先调用 bk\_wdt\_driver\_init()
- 喂狗时间必须小于看门狗超时时间
- 不要在中断服务函数中喂狗
- 注意看门狗复位的副作用
- 低功耗模式下看门狗可能被关闭，需要重新初始化
- 系统复位后看门狗状态会重置

<a id="api"></a>

## API 说明

主要 API 函数：

- bk\_wdt\_driver\_init() \- 初始化看门狗驱动
- bk\_wdt\_driver\_deinit() \- 反初始化看门狗驱动
- bk\_wdt\_start() \- 启动看门狗
- bk\_wdt\_stop() \- 停止看门狗
- bk\_wdt\_feed() \- 喂狗
- bk\_wdt\_get\_feed\_time() \- 获取喂狗时间
- bk\_wdt\_set\_feed\_time() \- 设置喂狗时间
- bk\_wdt\_driver\_inited() \- 检查驱动是否初始化

<a id="id5"></a>

## 示例代码

基本使用示例：

```
#include <driver/wdt.h>

void wdt_example(void)
{
    // 初始化看门狗驱动
    bk_wdt_driver_init();

    // 启动看门狗，超时时间 5 秒
    bk_wdt_start(5000);

    // 在主循环中定期喂狗
    while (1) {
        // 执行应用逻辑
        // ...

        // 喂狗
        bk_wdt_feed();

        // 延时
        rtos_delay_milliseconds(1000);
    }
}
```

时间管理示例：

```
void wdt_time_management_example(void)
{
    // 启动看门狗
    bk_wdt_start(10000);  // 10 秒超时

    // 设置喂狗时间为 5 秒
    bk_wdt_set_feed_time(5000);

    // 获取当前喂狗时间
    uint32_t feed_time = bk_wdt_get_feed_time();
    printf("Feed time: %d ms\n", feed_time);

    // 定期喂狗
    while (1) {
        // 执行应用逻辑
        // ...

        // 喂狗
        bk_wdt_feed();

        // 延时
        rtos_delay_milliseconds(2000);
    }
}
```

状态检查示例：

```
void wdt_status_example(void)
{
    // 检查驱动是否初始化
    if (bk_wdt_driver_inited()) {
        printf("WDT driver initialized\n");
    }

    // 启动看门狗
    bk_wdt_start(8000);

    // 设置喂狗时间
    bk_wdt_set_feed_time(3000);

    // 获取喂狗时间
    uint32_t feed_time = bk_wdt_get_feed_time();
    printf("Current feed time: %d ms\n", feed_time);
}
```

任务管理示例：

```
static void wdt_task(void *arg)
{
    while (1) {
        // 喂狗
        bk_wdt_feed();

        // 延时 1 秒
        rtos_delay_milliseconds(1000);
    }
}

void wdt_task_example(void)
{
    // 初始化看门狗驱动
    bk_wdt_driver_init();

    // 启动看门狗
    bk_wdt_start(3000);

    // 创建喂狗任务
    rtos_create_thread(NULL, 5, "wdt", wdt_task, 1024, NULL);
}
```

<a id="id6"></a>

## 常见问题

- **系统频繁复位**：检查喂狗时间设置、喂狗频率
- **看门狗不工作**：确认驱动初始化、启动状态
- **喂狗失败**：检查 API 调用顺序、参数设置
- **时间设置错误**：确认喂狗时间小于超时时间

<a id="id7"></a>

## 实战示例

1. 系统任务统一定期喂狗

```
static void wdt_task(void *arg) {
    while (1) {
        bk_wdt_feed();
        rtos_delay_milliseconds(1000);
    }
}
bk_wdt_driver_init();
bk_wdt_start(3000);
rtos_create_thread(NULL, 5, "wdt", wdt_task, 1024, NULL);
```

<a id="id8"></a>

## 常见错误码说明

- BK\_ERR\_WDT\_DRIVER\_NOT\_INIT：未初始化驱动即调用接口
- BK\_ERR\_WDT\_INVALID\_PERIOD：启动超时时间非法
