# CMake构建系统

> **Source:** [CMake.md](../../raw/Study_Note/05-工具与技巧/CMake/CMake.md)
> **TLDR:** CMake跨平台构建系统教程——从基础的`CMakeLists.txt`编写，到库的创建和链接、接口需求传递、条件编译和安装导出。

## Key Points

- **基础命令**：`cmake_minimum_required(VERSION x.x)`、`project(Name)`、`add_executable(target src.c)`；`set(VAR value)`设置变量
- **版本和配置**：`configure_file()`将CMake变量替换到头文件模板；`target_include_directories()`控制头文件搜索路径
- **库创建**：`add_library(libname STATIC/SHARED src.c)`；`target_link_libraries(target PRIVATE/PUBLIC/INTERFACE lib)`
- **依赖传递**：PRIVATE（仅自己用）、PUBLIC（自己和依赖者都用）、INTERFACE（仅依赖者用）
- **条件编译**：`option(VAR "desc" ON/OFF)`、`if(DEFINED VAR)`、`target_compile_definitions()`
- **安装**：`install(TARGETS ...)`、`install(EXPORT ...)`；`find_package()` 查找已安装包
- **构建目录**：推荐`build/`目录隔离构建产物，`cmake .. && make`

## Related Concepts

- [[c-compilation-pipeline]] — 编译链接流程
- [[embedded-coding-standards]] — Cursor规则中的CMake规范
