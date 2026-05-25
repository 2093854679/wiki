# 桌面宠物任务拓扑与通信

> **Source:** [19-desktop-pet任务拓扑与通信说明.md](../../raw/智能桌面萌宠项目笔记/doc/19-desktop-pet任务拓扑与通信说明.md)
> **TLDR:** FreeRTOS 12 类任务的优先级拓扑图——音频(P6/P5) > 显示(P4) > 按键/传感器(P3) > UI刷新(P2) > 网络服务(P1)；事件驱动+消息队列的模块间通信架构。

## Key Points

- **任务优先级分配**（0=最低）：
  - audio_input_task（P6）：麦克风采集+Opus编码，最高优先级保证不丢音频
  - audio_output_task（P5）：音频解码+播放，P6输出依赖
  - display_task（P4）：LVGL 渲染+触摸扫描
  - key_sensor_task（P3）：按键+电容触摸+IMU 传感器轮询
  - ui_tick_task（P2）：UI 定时刷新（动画/状态轮询）
  - http_server_task（P1）：局域网宠物网页服务，最低优先级避免干扰实时任务
- **事件驱动架构**：各模块通过事件总线松散耦合；MCP 工具调用→事件发布→订阅模块响应
- **消息队列**：audio_input→audio_processing→audio_output 使用队列传递编码帧
- **MCP 工具集**：`self.pet.get_state`、`self.light.set_rgb`、`self.chassis.go_forward` 等通过 MCP 协议暴露给后台 AI
- **互联互通**：WiFi→WebSocket/MQTT→后台 API→LLM 决策→MCP tools/call→设备执行

## Related Concepts

- [[watch-rtos-architecture]] — OV-Watch RTOS 架构参考
- [[mcp-protocol]] — MCP 工具调用机制
- [[desktop-pet-docs]] — 项目其他文档
