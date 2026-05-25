# app工程CLI命令与常用API速查

本笔记整理了projects/app工程main目录中注册的CLI命令，以及常用API，便于开发和调试。

---

## app 工程
- **编译命令**：`make bk7236 PROJECT=app`
- **命令名**：无专用CLI命令（app_main.c为主循环模板，未注册cli命令）
- **说明**：该工程为通用应用主入口模板，适合集成多任务、shell、外设等功能，便于自定义开发。

---

## 常用API速查

### 1. 系统与任务
- `bk_init()` —— 初始化系统
- `rtos_set_user_app_entry(beken_thread_function_t entry)` —— 设置用户主入口
- `bk_cli_init()` —— 初始化命令行（如需集成CLI）
- `rtos_create_thread()` —— 创建RTOS线程
- `rtos_delay_milliseconds(ms)` —— 线程延时

### 2. Flash分区相关
- `bk_flash_partitions` —— Flash分区表（见vendor_flash.c）
- `bk_partition_user_t` —— 分区枚举类型

### 3. 其它常用API
- `bk_set_jtag_mode(cpu_id, group_id)` —— 设置JTAG模式
- `bk_set_printf_sync(true/false)` —— 设置printf同步
- `shell_set_log_level(level)` —— 设置shell日志等级

### 4. 常用结构体与类型
- `bk_logic_partition_t` —— Flash分区结构体
- `bk_partition_user_t` —— 分区枚举

---

> 说明：
> - 该工程为通用应用模板，CLI命令和API可根据实际需求扩展。
> - 具体API参数和用法请参考头文件和官方文档。
> - 如需补充其它CLI命令或API，请告知具体需求。
