---
type: concept
aliases:
  - 嵌入式编码规范
  - C 命名规范
  - 工程规范
---

# 嵌入式编码规范

> **TLDR:** 嵌入式编码规范的核心是可读、可测、可追踪和可维护，覆盖命名、格式、模块边界、错误处理、日志、提交和文档。

## 适用问题

- C 文件、函数、变量、宏和类型怎么命名？
- CMake、Kconfig、组件目录如何保持一致？
- AI 生成代码如何避免风格漂移？
- 项目文档、commit 和分支策略怎么配合开发流程？

## 核心关系

- [[c-naming-conventions]] 是 C 命名规范入口。
- [[cursor-embedded-rules]] 是 AI 辅助编码规则入口。
- [[cmake-build-system]] 是构建规范入口。
- [[embedded-registration-patterns]] 和 [[embedded-software-design-patterns]] 约束模块边界。
- [[huang-learning-log]] 和 [[internship-plan]] 包含实习阶段的工程规范。

## 规范优先级

- 接口稳定性优先于局部写法偏好。
- 命名表达语义，不只表达类型。
- 错误路径和日志要能支持现场定位。
- 自动格式化解决格式问题，人负责架构和边界。

## Related

- [[c-language-core-system]]
- [[embedded-software-design-patterns]]
- [[cmake-build-system]]
