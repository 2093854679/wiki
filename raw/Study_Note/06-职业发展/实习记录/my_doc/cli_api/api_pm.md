# pm工程常用API速查

本笔记整理了projects/pm工程下各子工程的常用API，便于开发和调试。

---

## lv 子工程

- **编译命令**：`make bk7236 PROJECT=pm/lv`
- **命令名**：无专用CLI命令（lv_main.c为主循环模板，未注册cli命令）
- **说明**：该子工程为低功耗/电源管理相关功能演示，适合集成PM、LVGL等功能，便于自定义开发。

---

## 常用API速查

### 1. 系统与任务
- `bk_init()` —— 初始化系统
- `rtos_set_user_app_entry(beken_thread_function_t entry)` —— 设置用户主入口
- `rtos_create_thread()` —— 创建RTOS线程
- `rtos_delay_milliseconds(ms)` —— 线程延时

### 2. 电源管理相关
- 具体API请参考PM模块头文件和官方文档，如低功耗模式切换、唤醒源配置等。

---

> 说明：
> - 该工程为低功耗/电源管理相关演示，无CLI命令，API以系统初始化和PM相关为主。
> - 具体API参数和用法请参考头文件和官方文档。
> - 如需补充其它API，请告知具体需求。
