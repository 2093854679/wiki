# peri_verification工程常用API速查

本笔记整理了projects/peri_verification工程下各子工程的常用API，便于开发和调试。

---

## main 子工程

- **编译命令**：`make bk7236 PROJECT=peri_verification/main`
- **命令名**：无专用CLI命令（peri_verification_main.c仅初始化CLI，未注册自定义命令）
- **说明**：该子工程为外设功能验证相关演示，适合集成外设驱动、功能测试等，便于自定义开发。

---

## 常用API速查

### 1. 系统与任务
- `bk_init()` —— 初始化系统
- `rtos_set_user_app_entry(beken_thread_function_t entry)` —— 设置用户主入口
- `rtos_create_thread()` —— 创建RTOS线程
- `rtos_delay_milliseconds(ms)` —— 线程延时

### 2. CLI与外设相关
- `bk_cli_init()` —— 初始化命令行（可集成外设相关CLI命令）
- 具体外设API请参考各外设驱动头文件和官方文档，如timer、uart、gpio等。

---

> 说明：
> - 该工程为外设功能验证相关演示，无自定义CLI命令，API以系统初始化和外设相关为主。
> - 具体API参数和用法请参考头文件和官方文档。
> - 如需补充其它API，请告知具体需求。
