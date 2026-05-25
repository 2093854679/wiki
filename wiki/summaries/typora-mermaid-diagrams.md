# Typora画图（Mermaid）

> **Source:** [使用 Typora 画图.md](../../raw/Study_Note/05-工具与技巧/Typora使用/使用 Typora 画图（类图、流程图、时序图）.md)
> **TLDR:** Typora通过Mermaid代码块支持流程图、时序图、类图、状态图、甘特图和饼图，渲染后可直接导出为图片或PDF。

## Key Points

- **流程图（graph）**：`graph TD/LR`定义方向；`A[矩形]-->B(圆角矩形)-->C{菱形条件}`；支持多种节点形状和连线样式
- **时序图（sequenceDiagram）**：`A->>B: message`同步调用；`A-->>B: message`异步返回；`Note left/right of`添加注释；`loop`/`alt`/`opt`控制结构
- **类图（classDiagram）**：类定义含属性和方法；`<|--`继承、`*--`组合、`o--`聚合关系
- **状态图（stateDiagram）**：`[*]-->State1`起始；`State1-->State2: event`转换；`[*]`结束状态
- **甘特图（gantt）**：任务计划和时间线可视化；`section`分组、`done/crit/active`状态标记
- **导出**：Typora支持导出为HTML/PDF/图片格式

## Related Concepts

- [[cmake-build-system]] — 工具链
