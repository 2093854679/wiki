# security工程CLI命令与常用API速查

本笔记整理了projects/security工程下各子工程的CLI命令与常用API，便于开发和调试。

---

## 各子工程
- **secureboot_xip**
- **secureboot_tfm_test**
- **secureboot_overwrite**
- **secureboot_no_tfm**

- **编译命令**（以secureboot_xip为例）：
  `make bk7236 PROJECT=security/secureboot_xip`
- **命令名**：无专用CLI命令（主流程为安全启动演示，未注册cli命令）
- **说明**：各子工程主要演示安全启动、TFM集成、覆盖写保护等功能，适合安全相关开发和测试。

---

## 常用API速查

### 1. 系统与启动
- `bk_init()` —— 初始化系统
- `rtos_set_user_app_entry(beken_thread_function_t entry)` —— 设置用户主入口

### 2. 安全启动相关
- 具体API请参考各子工程的README和官方安全启动文档，常见如Flash分区、TFM集成、启动流程等。

---

> 说明：
> - 该工程为安全启动相关演示，无CLI命令，API以系统初始化和安全相关为主。
> - 具体API参数和用法请参考头文件和官方文档。
> - 如需补充其它CLI命令或API，请告知具体需求。
