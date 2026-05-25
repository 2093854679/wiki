# phy工程常用API速查

本笔记整理了projects/phy工程下各子工程的常用API，便于开发和调试。

---

## cert_test 子工程

- **编译命令**：`make bk7236 PROJECT=phy/cert_test`
- **命令名**：无专用CLI命令（armino_main.c为主循环模板，未注册cli命令）
- **说明**：该子工程为射频/PHY相关功能演示，适合集成射频测试、BLE/BT PHY验证等功能，便于自定义开发。

---

## 常用API速查

### 1. 系统与任务
- `bk_init()` —— 初始化系统
- `rtos_set_user_app_entry(beken_thread_function_t entry)` —— 设置用户主入口
- `rtos_create_thread()` —— 创建RTOS线程
- `rtos_delay_milliseconds(ms)` —— 线程延时

### 2. 射频/PHY相关
- 具体API请参考PHY模块头文件和官方文档，如射频参数配置、PHY测试等。

---

> 说明：
> - 该工程为射频/PHY相关演示，无CLI命令，API以系统初始化和PHY相关为主。
> - 具体API参数和用法请参考头文件和官方文档。
> - 如需补充其它API，请告知具体需求。
