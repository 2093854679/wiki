# 嵌入式软件设计模式

> **TLDR:** 嵌入式软件架构中实现低耦合高内聚的三种核心设计模式——模块注册（IoC控制反转，从Switch-Case到链接器静态注册的演进）、接口聚合（硬件抽象层，含函数指针的结构体统一访问入口）和发布/订阅（事件驱动，时空解耦）。

## 一、模块注册机制（控制反转）

贯穿嵌入式架构演进的核心思想：控制权从模块转移到框架。

### 演进路径
```
Switch-Case (强耦合)
  → 列表式 (耦合转移到静态数组)
  → 动态注册 (管理器解耦，init仍需手动调用)
  → 静态注册 (链接器自动汇集，零运行时开销)
  → 发布/订阅 (时空解耦，事件驱动)
```

### 静态注册实现要点
```c
// 1. 链接器脚本中定义专用段
SECTIONS {
    .recipient_section : {
        __recipients_start = .;
        KEEP(*(.recipient_section*))
        __recipients_end = .;
    } > RAM
}

// 2. 注册宏：将实例指针放入特定段
#define REGISTER_RECIPIENT(instance) \
    static const recipient_t* const __ptr_##instance \
    __attribute__((section(".recipient_section"), used)) = &instance

// 3. 使用：模块只需一行
REGISTER_RECIPIENT(grandma_recipient);

// 4. 管理器遍历由链接器自动生成的列表
extern const recipient_t* __recipients_start[];
extern const recipient_t* __recipients_end[];
for (const recipient_t** p = __recipients_start; p < __recipients_end; ++p) {
    // 处理每个已注册模块
}
```

此模式被Linux内核（`__initcall`/`module_init`）和RT-Thread（`INIT_EXPORT`）广泛使用。

## 二、接口聚合（硬件抽象层）

### 设计要点
- 为每类硬件定义接口结构体：包含状态变量 + 函数指针（Init/Enable/Disable/Read/Write）
- 用总结构体聚合所有设备接口形成统一访问入口
- 运行时初始化各设备函数指针

```c
// 单个设备接口
typedef struct {
    uint8_t ConnectionError;
    uint16_t Steps;
    void (*Init)(void);
    void (*WristEnable)(void);
    uint16_t (*GetSteps)(void);
} HW_IMU_InterfaceTypeDef;

// 总接口聚合
HW_InterfaceTypeDef HWInterface = {
    .IMU = { .Init = HW_MPU_Init, .GetSteps = HW_MPU_Get_Steps },
    .LCD = { .SetLight = HW_LCD_Set_Light },
    // ... 所有设备
};
```

### 核心优势
- 解耦：UI/任务层仅面对`HWInterface`，不关心底层实现
- 可替换：换传感器/移植只需替换函数指针
- 可测试：注入虚拟实现（`HW_USE_HARDWARE=0`）进行PC仿真
- 可维护：所有设备接口集中管理，排查问题高效

## 三、发布/订阅（事件驱动）

### 核心概念
- 事件总线（Event Bus）：中介者，解耦发布者和订阅者
- 订阅者向总线注册对某个主题（Topic）的兴趣
- 发布者向总线发布事件，无需知道谁在监听
- 总线负责将事件分发给所有订阅了该主题的订阅者

### 适用场景
- GUI事件处理（按键、触摸、页面切换）
- 物联网多传感器数据融合（各传感器独立发布，中心处理订阅）
- 多任务异步协作（一个任务的通知驱动多个任务的动作）
- 系统模式切换（Active→Idle→Stop，多个模块订阅模式变化事件）

### 与直接函数调用的对比
| 维度 | 直接调用 | 发布/订阅 |
|------|---------|----------|
| 耦合度 | 调用者知道被调用者 | 完全解耦 |
| 扩展性 | 新增接收者需修改代码 | 新增订阅者无需改动 |
| 调用关系 | 1对1 | 1对多、多对多 |
| 时序 | 同步 | 可同步可异步 |
| 调试 | 调用栈清晰 | 事件流追踪复杂 |

## 设计原则

1. **控制反转（IoC）**：模块不再主动调用框架，而是被动注册到框架，由框架统一调用
2. **开放/封闭原则**：对扩展开放（新增模块），对修改封闭（不修改核心代码）
3. **依赖倒置**：高层模块和低层模块都依赖抽象接口，而非具体实现

选择建议：没有最好的架构，只有最合适的。资源极度受限的微型项目可能列表式足够，高性能底层平台适合静态注册，复杂异步系统需要发布/订阅。

## Related

- [[embedded-registration-patterns]] — 模块注册机制的完整演进
- [[ovwatch-code-style]] — OV-Watch硬件抽象层实例
- [[c-function-pointers]] — 函数指针是实现基础
- [[watch-rtos-architecture]] — 发布/订阅在手表中的应用
