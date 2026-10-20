---
type: summary
source_root: beken
sdk_family: bk_toolkit
chip: null
sdk_version:
  IoTApp: v2.0.1
  IDE: v2.0.1
  MeshApp: latest
  RFTest: latest
  UIDesigner: latest
  AudioDebugTool: latest
  BKFIL: latest
processor: null
---

# BK 开发与生产工具导航

> **TLDR:** BK ToolKit 是多个独立工具的文档集合，应按固件烧录、射频测试、音频调参、界面设计、开发环境或手机控制分别进入，不能把工具目录的 `latest` 当作统一 SDK 版本。
> **Source:** [BKFIL](../../../raw/beken/bk_toolkit/bkfil/index.md)、[RF Test](../../../raw/beken/bk_toolkit/rf-test/index.md)、[音频调试](../../../raw/beken/bk_toolkit/audiodebugtool/index.md)、[字体融合工具](../../../raw/beken/bk_toolkit/uidesigner/index.md)、[LVGL UI Designer](../../../raw/beken/bk_toolkit/lvgluidesigner/index.md)、[IDE](../../../raw/beken/bk_toolkit/ide/index.md)、[IoT App](../../../raw/beken/bk_toolkit/iotapp/index.md)、[Mesh App](../../../raw/beken/bk_toolkit/meshapp/index.md)

## 按任务选择

- **烧录与生产。** BKFIL 的导航覆盖下载安装、快速开始、功能、外置 Flash、工厂模式和发布日志；RF Test 的导航覆盖测试站点、频率/功率校准与 TX 验证。[BKFIL](../../../raw/beken/bk_toolkit/bkfil/index.md)／[RF Test](../../../raw/beken/bk_toolkit/rf-test/index.md)
- **音频参数。** AudioDebugTool 明确用于可视化配置音频算法参数，提供 EQ、基础配置、AEC、芯片选择、串口与导出入口。[音频调试](../../../raw/beken/bk_toolkit/audiodebugtool/index.md)
- **界面设计。** UIDesigner 是字体融合工具，文档含文字/图片控件及代码导出；LVGL UI Designer 另提供拖拽组件、实时预览、样式与项目管理，两者是独立产品入口。[UIDesigner](../../../raw/beken/bk_toolkit/uidesigner/index.md)／[LVGL 工具](../../../raw/beken/bk_toolkit/lvgluidesigner/index.md)
- **开发及控制。** IDE 文档面向 VSCode Beken Extension；IoTApp 对应 ARMINO Smart SDK 文档；Mesh App 另涵盖节点、群组与拓扑管理。[IDE](../../../raw/beken/bk_toolkit/ide/index.md)／[IoTApp](../../../raw/beken/bk_toolkit/iotapp/index.md)／[Mesh App](../../../raw/beken/bk_toolkit/meshapp/index.md)

## 适用范围

这是工具路由页，未给所有工具指定统一芯片或 AP/CP。IoTApp、IDE 官网入口路径为 v2.0.1，部分工具路径为 `latest`，LVGL 工具入口未声明固定版本；实际软件版本以对应发布日志和安装包为准。

## Related

- [[bk-armino-framework]]
- [[bk-mesh-overview]]
- [[bk-ai-solution-overview]]
- [[custom-board-guide]]
