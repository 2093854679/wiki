# C语言命名规范

> **Source:** [02-C语言命名规范.md](../../raw/Study_Note/02-编程语言/C语言/02-C语言命名规范.md)
> **TLDR:** C语言项目命名规范总览——变量、函数、类型、宏、文件的命名规则与最佳实践，强调代码可读性和一致性。

## Key Points

- 变量名使用小写+下划线（snake_case），如 `timer_count`、`buffer_size`
- 函数名使用小写+下划线，动词开头，如 `get_temperature()`、`set_baud_rate()`
- 类型名（`typedef`/`struct`/`enum`）使用小写+下划线+`_t`后缀，如 `timer_config_t`、`status_t`
- 宏定义全大写+下划线，如 `MAX_BUFFER_SIZE`、`GPIO_PIN_13`
- 全局变量加`g_`前缀，静态变量加`s_`前缀
- 指针变量加`p_`前缀（可选），如 `p_buffer`
- 文件名全小写+下划线，模块名与功能对应

## Main Arguments

统一的命名规范是代码可读性和可维护性的基础。在嵌入式C项目中，遵循一致的命名约定能显著减少团队协作中的理解成本，降低因命名混淆导致的bug。

## Related Concepts

- [[c-language-basics]] — C语言基础语法
- [[embedded-coding-standards]] — 嵌入式编码规范
