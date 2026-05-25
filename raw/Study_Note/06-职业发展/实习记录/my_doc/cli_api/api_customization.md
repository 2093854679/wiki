# customization工程常用API速查

本笔记整理了projects/customization工程下各子工程的常用API，便于开发和调试。

---

## 典型子工程（如 config_ab）

- **编译命令**（以config_ab为例）：`make bk7236 PROJECT=customization/config_ab`
- **命令名**：无专用CLI命令（app_main.c为主循环模板，未注册cli命令）
- **说明**：各子工程为定制化配置相关功能演示，适合集成分区表、Flash配置等，便于自定义开发。

---

## 常用API速查

### 1. 系统与任务
- `bk_init()` —— 初始化系统
- `rtos_set_user_app_entry(beken_thread_function_t entry)` —— 设置用户主入口
- `rtos_create_thread()` —— 创建RTOS线程
- `rtos_delay_milliseconds(ms)` —— 线程延时

### 2. Flash分区相关
- `bk_flash_partitions` —— Flash分区表（见vendor_flash.c）
- `bk_partition_user_t` —— 分区枚举类型

### 3. 其它常用API
- 具体API请参考各子工程头文件和官方文档，如定制化配置、分区管理等。

---

> 说明：
> - 该工程为定制化配置相关演示，无CLI命令，API以系统初始化和分区/配置相关为主。
> - 具体API参数和用法请参考头文件和官方文档。
> - 如需补充其它API，请告知具体需求。
