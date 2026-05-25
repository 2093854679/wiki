# Cursor嵌入式编码规则

> **Source:** [CursorRules/readme.md](../../raw/Study_Note/05-工具与技巧/Cursor/CursorRules/readme.md)
> **TLDR:** Cursor AI辅助嵌入式开发的规则体系——5个专用规则文件覆盖驱动开发、固件开发、编码规范、硬件接口和中断优化，实现AI生成代码的质量控制。

## Key Points

- **规则文件结构**：`.cursor/.rules/`目录下5个规则文件，各司其职；readme.md为总体说明
- **driver_development.md**：驱动开发规则——BSP分层、寄存器操作封装、外设初始化流程
- **firmware_development.md**：固件开发规则——模块化设计、状态机实现、错误处理模式
- **embedded_c_coding_standards.md**：编码规范——命名约定、注释要求、代码结构、静态分析集成
- **hardware_interface_development.md**：硬件接口规则——中断处理、DMA使用、定时器配置、外设抽象
- **interrupt_handling_optimization.md**：中断优化——ISR精简、优先级分配、临界区管理、Deferred Interrupt模式
- **核心价值**：让AI生成符合嵌入式最佳实践的代码，减少手动审查工作量

## Related Concepts

- [[embedded-registration-patterns]] — 设计模式与编码规范配合
- [[c-naming-conventions]] — C语言命名规范
