# bin & map文件分析

> **Source:** [02-bin&map文件的分析.md](../../../raw/Study_Note/02-嵌入式开发/MCU基础/02-bin&map文件的分析.md)
> **TLDR:** 编译产出的.bin和.map文件解读方法——通过map文件分析代码/数据/符号的空间分布，定位内存溢出和优化目标。

## Key Points

- **.map文件**（链接器生成）：包含Section信息（各段地址和大小）和Symbol信息（每个函数/变量的地址和大小）；是分析内存占用的第一手资料
- **.bin文件**：纯二进制机器码，不含地址信息；直接烧录到Flash起始地址执行
- **.hex文件**（Intel HEX）：带地址和校验的ASCII格式；比bin大但包含更多元信息
- **.elf/.axf文件**：完整可执行文件格式，包含调试信息和符号表；可用`readelf`/`objdump`工具分析
- **map文件分析技巧**：①查找`.text`/`.data`/`.bss`/`.heap`/`.stack`段大小 ②按大小排序符号表定位大对象 ③检查是否有意外引入的库函数 ④验证链接脚本与实际分布是否一致
- **常见问题定位**：RAM溢出（.data + .bss + heap + stack > RAM总大小）、Flash溢出（.text + .rodata > Flash大小）

## Related Concepts

- [[c-compilation-pipeline]] — 编译链接全流程
- [[mcu-startup-flow]] — MCU启动阶段的内存初始化
- [[lr-er-load-execute-regions]] — 加载区与执行区
