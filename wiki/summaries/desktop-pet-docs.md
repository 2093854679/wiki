# 桌面宠物项目文档合集

> **Source:** doc/02-19 multiple files
> **TLDR:** 智能桌面萌宠（Desktop Pet）项目的完整开发文档——涵盖 SD 卡 BMP 读取、WiFi 配网、GIF 播放、固件体积对比、UI 设计、宠物交互、养成系统、Web 服务、MCP 集成、闹钟/充电动画等 18 个子系统。

## 各模块要点

### 显示与资源
- **SD 卡 BMP 读取**（doc/02）：FatFs 挂载 SD→LVGL BMP 解码→`lv_img_set_src("S:/path.bmp")`
- **GIF 播放**（doc/04）：`pet_page` 从 SD 卡播放 GIF 动画；使用 LVGL GIF 解码库
- **Emoji 心情切换**（doc/07）：根据养成数据（心情值）动态切换对应 GIF 表情
- **充电动画**（doc/17）：充电状态触发专属动画和指示灯效果

### 网络与通信
- **WiFi 配网**（doc/03）：手动输入 SSID/密码的 WiFi 连接界面；T9 按钮矩阵键盘实现
- **任务拓扑**（doc/19）：12 类 FreeRTOS 任务优先级分配——audio_input(P6)→audio_output(P5)→display(P4)→ui_tick(P2)→http_server(P1)；消息队列和事件驱动的任务间通信
- **局域网网页服务**（doc/10）：`esp_http_server` 在 80 端口提供宠物状态页面 + `/api/pet_state` JSON + `/api/action` 交互接口

### 宠物交互系统
- **戳脸/摸头**（doc/08）：电容触摸传感器检测→触发 `pet_on_pat()`/`pet_on_poke()`→MCP 工具调用→云端语音互动
- **养成系统**（doc/09）：Tamagotchi 养成模型——stage（陌生/熟悉/亲密）、intimacy（亲密度 0-100）、mood（心情）、age_days（相识天数）；每日互动有递减收益机制
- **宠物商店**（doc/11/doc/12）：PetShop 商店 UI 页面；返回按钮防误触设计

### MCP 集成
- **设备状态获取**（doc/13）：MCP 工具 `self.pet.get_state`→返回 stage/intimacy/mood→AI 根据状态选择回应风格
- **Bemfa 台灯控制**（doc/14）：MCP 协议集成第三方 IoT 平台（Bemfa）控制台灯开关和亮度

### 系统与工具
- **固件体积对比**（doc/05）：V2 固件约 6.5MB（比 V1 大约因 LVGL 显示层/GIF 解码/更多板级代码和依赖）；assets.bin 中的资源不占 app 体积
- **闹钟移植**（doc/16）：闹钟响铃功能从参考代码移植到桌宠平台
- **语音代码路线**（doc/18）：语音相关代码的学习路线和源码导航
- **Git 同步**（doc/15）：分支管理、冲突处理和协同开发记录
- **clangd 配置**（doc/clangd）：WSL+Cursor 环境配置 clangd 实现 C/C++ 右键跳转到定义

## Related Concepts

- [[custom-board-guide]] — 自定义开发板
- [[mcp-protocol]] — MCP 协议
- [[websocket-protocol]] — WebSocket 通信
- [[xiaozhi-ai-framework]] — 小智AI 框架
- [[watch-rtos-architecture]] — RTOS 任务架构参考
