# 加载区LR和执行区ER

> **Source:** [04-加载区LR和执行区ER.md](../../../raw/Study_Note/02-嵌入式开发/MCU基础/04-加载区LR和执行区ER.md)
> **TLDR:** ARM分散加载机制——Load Region（LR，加载域）是程序在ROM中的存储位置，Execute Region（ER，执行域）是运行时在RAM中的执行位置；链接器脚本控制LR到ER的映射和自动搬移。

## Key Points

- **LR（Load Region）**：程序在Flash/ROM中的存放位置；只读数据（`.rodata`/`const`）也在此
- **ER（Execute Region）**：程序在RAM中的执行位置；代码可直接在Flash执行（XIP），但读写数据必须在RAM
- **为什么需要LR→ER搬移**：①Flash速度慢，搬移到RAM加速 ②.data段（已初始化全局变量）必须在RAM中读写 ③Flash不能在写操作期间读取
- **分散加载脚本（.sct/.scf）**：定义LR和ER的映射关系；手动指定各段的加载地址和执行地址
- **RW段搬移**：__main()在调用main()前，按链接器生成的Copy Table自动将RW和ZI数据从LR搬移到对应的ER
- **XIP（eXecute In Place）**：代码直接在Flash中执行（无需搬移到RAM）；节省RAM但速度较慢（需Flash加速器/缓存缓解）
- **链接脚本关键符号**：`Image$$RO$$Base/Limit`、`Image$$RW$$Base/Limit`、`Image$$ZI$$Base/Limit`由链接器自动生成，启动代码引用它们完成数据搬移

## Related Concepts

- [[mcu-startup-flow]] — MCU启动流程
- [[bin-map-analysis]] — map文件分析
- [[c-compilation-pipeline]] — 编译链接流程
