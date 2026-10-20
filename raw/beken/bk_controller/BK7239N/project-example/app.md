---
type: official-document
source_url: https://docs.bekencorp.com/arminodoc/bk_controller/bk7239n/zh_CN/v2.1.1/project-example/app.html
sdk_family: bk_controller
chip: BK7239N
processor: ''
sdk_version: v2.1.1
language: zh_CN
fetched_at: '2026-10-20T16:59:36.586772+00:00'
mirror_status: current
---

<a id="app"></a>

# APP

:

<a id="id1"></a>

## 工程概述

- 工程路径: `projects/app`
- 适用芯片: BK7239N
- 功能定位: 提供最基础的应用入口模板,便于二次开发快速集成自定义业务逻辑。

<a id="id2"></a>

## 编译命令

- `make bk7239` (不同芯片替换对应目标)。

<a id="id3"></a>

## 开发建议

- 在 `user_app_main` 中创建任务或初始化外设时,建议按需启用 CLI 与日志,便于调试。
- 如需自定义分区或外设初始化,可在 `config` 目录中扩展配置。

## 模块导航

- [简介](../introduction.md)
- [快速入门](../get-started.md)
- [硬件开发指南](../hw-reference.md)
- [Controller软件开发指南](../controller-guide.md)
- [主控平台软件开发指南](../host-guide.md)
- [工程与示例](../project-example.md)
- [wifi-controller](wifi_controller.md)
- [wifi-controller-4wire](wifi_controller_4wire.md)
- [蓝牙工程](bluetooth.md)
- [开发工具介绍](../dev-tool.md)
- [调测指导](../debug-guide.md)
- [产测指导](../production-test-guide.md)
- [常见问题解答](../faq.md)
