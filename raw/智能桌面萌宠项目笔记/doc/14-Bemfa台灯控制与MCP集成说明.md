## Bemfa 台灯控制与 MCP 集成说明

本文记录在 `desktop-pet` V2 工程中，如何通过 **巴法云 MQTT** 控制外部台灯，以及如何通过 **MCP 工具与 Web 控制台** 触发这一能力，便于后续扩展到小车底盘等设备。

- **工程根**：`xiaozhi-esp32-main-v2/xiaozhi-esp32`
- 主要相关文件：
  - `main/boards/desktop-pet/mqtt_bemfa.h`
  - `main/boards/desktop-pet/mqtt_bemfa.cc`
  - `main/boards/desktop-pet/web_server.cc`
  - `main/boards/desktop-pet/desktop_pet.cc`

---

### 1. 巴法云 MQTT 封装（`mqtt_bemfa.*`）

**连接参数与默认配置**

- 服务器：`bemfa.com`
- 端口：`9501`（TCP）
- 本地封装常量（`mqtt_bemfa.cc`）：
  - `BEMFA_SERVER`, `BEMFA_PORT`
  - NVS 命名空间：`"bemfa"`
  - NVS 键：
    - `"client_id"`：巴法云私钥 / clientId
    - `"topic"`：用于控制的主题名
  - 默认值（当 NVS 为空时回退）：
    - `BEMFA_DEFAULT_CLIENT_ID = "2e5d411bd3a745c8bd54a48beffab2e3"`
    - `BEMFA_DEFAULT_TOPIC     = "light002"`

**核心接口（`mqtt_bemfa.h`）**

- `bool BemfaMqtt_Start(void);`
  - 从 NVS 读取 `client_id` / `topic`，若为空则使用上述默认值。
  - 通过 `Board::GetInstance().GetNetwork()->CreateMqtt(1)` 创建第 2 路 MQTT 客户端。
  - 调用 `Connect(BEMFA_SERVER, BEMFA_PORT, client_id, client_id, "")` 建立连接。
- `bool BemfaMqtt_Publish(const char* topic, const char* payload);`
  - 若 `topic == nullptr` 或空串，则使用缓存的 `s_topic`（NVS 或默认值）。
  - 通过 `Mqtt::Publish(topic, payload, 0)` 发送文本消息。
- `bool BemfaMqtt_PublishLamp(const char* payload);`
  - 便捷接口，等价于 `BemfaMqtt_Publish(nullptr, payload)`，使用默认主题。
- `bool BemfaMqtt_LampOn(void);`
  - 调用 `BemfaMqtt_PublishLamp("on")`。
- `bool BemfaMqtt_LampOff(void);`
  - 调用 `BemfaMqtt_PublishLamp("off")`。
- `bool BemfaMqtt_IsConnected(void);` / `void BemfaMqtt_Stop(void);`
  - 查询连接状态、断开并释放 `s_bemfa_mqtt`。

> 说明：选择 `CreateMqtt(1)` 是为了不干扰主协议使用的 `CreateMqtt(0)`（与小智云端通信）。

---

### 2. Web 控制台按钮（`web_server.cc`）

在局域网 Web 控制台的「互动控制」卡片中，新增了 **开灯 / 关灯** 两个按钮。

**前端部分**

- 在 HTML 模板中增加一行按钮：
  - `💡 开灯` → `onclick="doAction('lamp_on')"`
  - `🌙 关灯` → `onclick="doAction('lamp_off')"`
- 按钮最终都会调用 `doAction(act)`，即向 `/api/action?type=...` 发送 `POST` 请求。

**后端路由（`action_handler`）**

- 原有分支处理 `pat` / `poke` / `feed_*` / `reset`。
- 新增分支：

  - `type == "lamp_on"`：
    - 若尚未连接：`if (!BemfaMqtt_IsConnected()) BemfaMqtt_Start();`
    - 然后调用 `BemfaMqtt_LampOn();`
    - 记录日志：`web: lamp_on`

  - `type == "lamp_off"`：
    - 若尚未连接：`if (!BemfaMqtt_IsConnected()) BemfaMqtt_Start();`
    - 然后调用 `BemfaMqtt_LampOff();`
    - 记录日志：`web: lamp_off`

这样，在浏览器中打开宠物 Web 控制台，点击对应按钮即可通过巴法云控制外部台灯。

---

### 3. MCP 工具集成（`desktop_pet.cc`）

为方便云端通过 MCP 控制台灯，在 `DesktopPetBoard::InitializeTools()` 中注册了两个新工具：

```cpp
mcp_server.AddTool("self.lamp.on",
    "通过巴法云打开外部台灯。当用户说开灯、打开台灯、把灯打开等类似意图时调用。",
    PropertyList(),
    [](const PropertyList&) -> ReturnValue {
        if (!BemfaMqtt_IsConnected()) {
            BemfaMqtt_Start();
        }
        bool ok = BemfaMqtt_LampOn();
        ESP_LOGI("desktop-pet", "MCP lamp.on via Bemfa: %s", ok ? "ok" : "failed");
        return ok;
    });

mcp_server.AddTool("self.lamp.off",
    "通过巴法云关闭外部台灯。当用户说关灯、关闭台灯、把灯关掉等类似意图时调用。",
    PropertyList(),
    [](const PropertyList&) -> ReturnValue {
        if (!BemfaMqtt_IsConnected()) {
            BemfaMqtt_Start();
        }
        bool ok = BemfaMqtt_LampOff();
        ESP_LOGI("desktop-pet", "MCP lamp.off via Bemfa: %s", ok ? "ok" : "failed");
        return ok;
    });
```

**云端使用建议**

- 工具名：
  - 开灯：`self.lamp.on`
  - 关灯：`self.lamp.off`
- 描述中已经包含典型触发语，如“开灯 / 关灯 / 打开台灯 / 把灯关掉”等，云端可以在 prompt 中引用这些描述进行意图匹配。

---

### 4. 未来扩展：从台灯到小车

当前设计是将 **外部设备抽象成“通过 MQTT 主题控制的实体”**，台灯只是第一个例子：

- 台灯：主题 `light002`，payload 为 `"on"` / `"off"`；
- 小车：可以在巴法云上另建主题（如 `car001/cmd`），payload 约定为 `"forward"` / `"back"` / `"left"` / `"right"` / `"stop"` 等。

迁移步骤：

1. 为小车新增 `BemfaMqtt_PublishCarCmd(const char* cmd)` 等封装。
2. 在 MCP 中注册 `self.car.forward` / `self.car.stop` 等工具，内部调用上述封装。
3. 小车侧 ESP8266/ESP32 固件订阅车的主题，根据指令控制电机。

通过复用现有 `mqtt_bemfa` 封装与 MCP 模式，可以较低成本地把「桌面小熊」扩展为「会动的小车宠物」。 

