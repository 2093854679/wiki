# 代码风格指南（clang-format）

> **Source:** [code_style.md](../../../raw/智能桌面萌宠项目笔记/code_style.md)
> **TLDR:** 项目使用 clang-format + Google C++ 风格统一代码格式，4 空格缩进、100 字符行宽、Attach 大括号风格；VSCode/CLion 均可集成。

## Key Points

- `.clang-format` 基于 Google C++ 风格，做自定义调整
- 安装：`winget install LLVM`（Windows）、`apt install clang-format`（Linux）、`brew install clang-format`（macOS）
- 格式化整个项目：`find main -iname *.h -o -iname *.cc | xargs clang-format -i`
- IDE 集成：VSCode 安装 C/C++ 扩展启用 `C_Cpp.formatting: clang-format`；CLion 设置 Formatter 为 clang-format
- 代码块可用 `// clang-format off/on` 临时关闭格式化

## Related Concepts

- [[cursor-embedded-rules]] — Cursor 嵌入式编码规则
- [[c-naming-conventions]] — C 语言命名规范
