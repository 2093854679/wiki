# properties_libs工程常用API速查

本笔记整理了projects/properties_libs工程下各子工程的常用API，便于开发和调试。

---

## main 子工程

- **编译命令**：`make bk7236 PROJECT=properties_libs/main`
- **命令名**：无专用CLI命令（main.c为空模板，未注册cli命令）
- **说明**：该子工程为属性库相关功能演示，适合集成属性管理、配置存储等功能，便于自定义开发。

---

## 常用API速查

### 1. 系统与任务
- `bk_init()` —— 初始化系统（如有集成）
- `rtos_set_user_app_entry(beken_thread_function_t entry)` —— 设置用户主入口
- `rtos_create_thread()` —— 创建RTOS线程
- `rtos_delay_milliseconds(ms)` —— 线程延时

### 2. 属性库相关
- 具体API请参考属性库相关头文件和官方文档，如属性读写、存储管理等。

---

> 说明：
> - 该工程为属性库相关演示，无CLI命令，API以系统初始化和属性管理相关为主。
> - 具体API参数和用法请参考头文件和官方文档。
> - 如需补充其它API，请告知具体需求。
