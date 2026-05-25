# WiFi 配网功能文档

## 功能概述

在 **desktop-pet** 板型的第三屏（`app3_page`）进入手动输入 SSID/密码的 WiFi 配网界面，支持 T9 多字母按键输入。

- **屏幕物理分辨率**: 240×280  
- **UI 坐标系**: 280×240（横向布局）  
- **入口**: `app3_page` 的 WiFi 图标  
- **输入方式**: T9 按钮矩阵键盘（同键循环选字母）  
- **主实现**: `main/boards/desktop-pet/ui/ui_wifi.cc`（页面创建 + 全部事件）；声明在 `main/boards/desktop-pet/ui/ui_wifi.h`。`screens.c` 仅在 `create_screens()` 里调用 `create_screen_wifi_page()`。

---

## 代码位置

### 1. UI 界面定义

**文件**: `main/boards/desktop-pet/ui/screens.h`

```c
typedef struct _objects_t {
    lv_obj_t *main;
    lv_obj_t *app1_page;
    lv_obj_t *app2_page;
    lv_obj_t *app3_page;
    lv_obj_t *app3_gmae;
    lv_obj_t *wifi_page;
    lv_obj_t *shop_page;
    /* ... 其它页面控件 ... */
    lv_obj_t *wifi_title_label;
    lv_obj_t *wifi_back_btn;
    lv_obj_t *wifi_ssid_ta;
    lv_obj_t *wifi_pwd_ta;
    lv_obj_t *wifi_connect_btn;
    lv_obj_t *wifi_disconnect_btn;
    lv_obj_t *wifi_status_label;
    lv_obj_t *wifi_kb;              /* T9：lv_buttonmatrix */
} objects_t;

enum ScreensEnum {
    SCREEN_ID_PET_PAGE = 1,
    SCREEN_ID_APP1_PAGE = 2,
    SCREEN_ID_APP2_PAGE = 3,
    SCREEN_ID_APP3_PAGE = 4,
    SCREEN_ID_APP3_GMAE = 5,
    SCREEN_ID_WIFI_PAGE = 6,
    SCREEN_ID_SHOP_PAGE = 7,
};
```

`create_screen_wifi_page` / `tick_screen_wifi_page` 的声明已迁至 **`ui_wifi.h`**（本文件内为注释说明）。

---

### 2. UI 界面实现

**注册**: `main/boards/desktop-pet/ui/screens.c` — `create_screens()` 末尾调用 `create_screen_wifi_page();`。

**实现文件**: `main/boards/desktop-pet/ui/ui_wifi.cc`  
**函数**: `create_screen_wifi_page()`

**界面布局**:
```
+---------------------------+
| [<] WiFi      (标题栏)     |
|---------------------------|
| SSID: [输入框 200×28]      |
| PWD:  [输入框 200×28]      |
| [ON] [OFF]  (连接/断开)    |
| Status: Ready             |
| [T9 键盘 280×118]          |
+---------------------------+
```

**关键组件（与代码一致）**:
- **根页面**: 280×240，黑底；手势 `action_wifi_back`；点击页面 `action_wifi_page_clicked` 用于隐藏键盘。
- **标题栏**: 高度 **36px**，背景 `#222222`（`0x222222`）。
- **返回按钮**: `<`，约 40×18，`action_wifi_back`。
- **ON 按钮**: 背景 `#2a82e4`，100×36，(20,144)，`LV_EVENT_PRESSED` → `action_wifi_connect`。
- **OFF 按钮**: 背景 `#ff5555`，100×36，(160,144)，`action_wifi_disconnect`。
- **T9**: `lv_buttonmatrix_create`，280×118，(0,122)，初始 `LV_OBJ_FLAG_HIDDEN`，映射见下文。

**页面根对象与标题栏（节选）**:
```cpp
void create_screen_wifi_page() {
    lv_obj_t *obj = lv_obj_create(0);
    objects.wifi_page = obj;
    lv_obj_set_pos(obj, 0, 0);
    lv_obj_set_size(obj, 280, 240);
    lv_obj_add_event_cb(obj, action_wifi_back, LV_EVENT_GESTURE, (void *)0);
    lv_obj_add_event_cb(obj, action_wifi_page_clicked, LV_EVENT_CLICKED, (void *)0);
    lv_obj_set_style_bg_color(obj, lv_color_hex(0xff000000), LV_PART_MAIN | LV_STATE_DEFAULT);
    // ... 标题栏 36px #222222、SSID/PWD textarea、ON/OFF、状态标签 ...
#if LV_USE_BUTTONMATRIX
    static const char *wifi_t9_map_lower_static[] = {
        "1.@-", "2abc", "3def", "\n",
        "4ghi", "5jkl", "6mno", "\n",
        "7pqrs", "8tuv", "9wxyz", "\n",
        "^", "0 _", "DEL", ""
    };
    lv_obj_t *obj = lv_buttonmatrix_create(parent_obj);
    objects.wifi_kb = obj;
    lv_buttonmatrix_set_map(obj, wifi_t9_map_lower_static);
    lv_obj_set_size(obj, 280, 118);
    lv_obj_set_pos(obj, 0, 122);
    lv_obj_add_event_cb(obj, action_wifi_keypad, LV_EVENT_VALUE_CHANGED, (void *)0);
    lv_obj_add_flag(obj, LV_OBJ_FLAG_HIDDEN);
#endif
}
```

**T9 键盘布局**（小写 / 大写两套 map，见 `wifi_t9_map_lower` / `wifi_t9_map_upper`）:
```
[1.@-] [2abc] [3def]
[4ghi] [5jkl] [6mno]
[7pqrs] [8tuv] [9wxyz]
[^]    [0 _]  [DEL]
```
- **^**: 大小写切换，并切换 `lv_buttonmatrix` 的 map（小写标签 ↔ 大写标签）。
- **0 _**: 数字与空格（字符集在 `wifi_t9_letters_for_key` 中解析）。
- **DEL**: 删除。

---

### 3. 事件处理声明

**文件**: `main/boards/desktop-pet/ui/ui_wifi.h`（`actions.h` 中 WiFi 相关已移除，见该文件注释）

```c
void create_screen_wifi_page();
void tick_screen_wifi_page();

void action_wifi_enter(lv_event_t * e);
void action_wifi_page_clicked(lv_event_t * e);
void action_wifi_back(lv_event_t * e);
void action_wifi_focus_ssid(lv_event_t * e);
void action_wifi_focus_pwd(lv_event_t * e);
void action_wifi_connect(lv_event_t * e);
void action_wifi_disconnect(lv_event_t * e);
void action_wifi_keypad(lv_event_t * e);
```
（源文件中含 Doxygen 注释，此处为便于阅读的精简列表。）

---

### 4. 事件实现（`ui_wifi.cc`）

#### 4.1 进入 WiFi 页面

```cpp
void action_wifi_enter(lv_event_t * e)
{
    ESP_LOGI(TAG, "action_wifi_enter called");
    lvgl_port_lock(0);
    wifi_hide_keyboard();
    wifi_active_ta = nullptr;
    wifi_t9_commit_pending();
    wifi_keypad_uppercase = false;
    lv_screen_load_anim(objects.wifi_page, LV_SCR_LOAD_ANIM_NONE, ANIMATION_DURATION_MS, 0, false);
    lvgl_port_unlock();

    auto &wifi_manager = WifiManager::GetInstance();
    if (wifi_manager.IsConnected()) {
        char status[48];
        snprintf(status, sizeof(status), "Connected %s", wifi_manager.GetSsid().c_str());
        wifi_update_status(status);
    } else {
        wifi_update_status("Ready");
    }
}
```

#### 4.2 返回上一页

```cpp
void action_wifi_back(lv_event_t * e)
{
    ESP_LOGI(TAG, "action_wifi_back called");
    lv_event_code_t code = lv_event_get_code(e);

    if (code == LV_EVENT_GESTURE) {
        lv_indev_t * indev = lv_indev_get_act();
        if (indev) {
            lv_point_t vect;
            lv_indev_get_vect(indev, &vect);
            if (vect.x < SWIPE) {
                return;
            }
        }
    }

    lvgl_port_lock(0);
    wifi_hide_keyboard();
    wifi_active_ta = nullptr;
    wifi_t9_commit_pending();
    wifi_keypad_uppercase = false;

    if (wifi_t9_timer) {
        lv_timer_del(wifi_t9_timer);
        wifi_t9_timer = nullptr;
        ESP_LOGI(TAG, "T9 timer deleted to save resources");
    }

    lv_screen_load_anim(objects.app3_page, LV_SCR_LOAD_ANIM_NONE, ANIMATION_DURATION_MS, 0, false);
    lvgl_port_unlock();
}
```

**返回方式**: 左上角 `<` 点击；**右滑**手势（`vect.x >= SWIPE`，`SWIPE` 为 20）。

#### 4.3 连接 WiFi — 校验与起任务

```cpp
void action_wifi_connect(lv_event_t * e)
{
    ESP_LOGI(TAG, "action_wifi_connect called");
    if (!objects.wifi_ssid_ta || !objects.wifi_pwd_ta) {
        wifi_update_status("Failed");
        return;
    }

    const char *ssid = lv_textarea_get_text(objects.wifi_ssid_ta);
    const char *password = lv_textarea_get_text(objects.wifi_pwd_ta);

    if (!ssid || ssid[0] == '\0') {
        wifi_update_status("SSID empty");
        return;
    }
    size_t ssid_len = strlen(ssid);
    if (ssid_len > 32) {
        wifi_update_status("SSID too long");
        return;
    }
    if (password && password[0] != '\0') {
        size_t pwd_len = strlen(password);
        if (pwd_len < 8) {
            wifi_update_status("Password too short");
            return;
        }
        if (pwd_len > 63) {
            wifi_update_status("Password too long");
            return;
        }
    }

    wifi_update_status("Connecting...");
    wifi_hide_keyboard();
    wifi_active_ta = nullptr;
    wifi_t9_commit_pending();

    if (wifi_connect_task_handle) {
        vTaskDelete(wifi_connect_task_handle);
        wifi_connect_task_handle = nullptr;
    }

    auto *params = new WifiConnectParams();
    strncpy(params->ssid, ssid, sizeof(params->ssid) - 1);
    params->ssid[sizeof(params->ssid) - 1] = '\0';
    if (password) {
        strncpy(params->password, password, sizeof(params->password) - 1);
        params->password[sizeof(params->password) - 1] = '\0';
    } else {
        params->password[0] = '\0';
    }
    BaseType_t ret = xTaskCreate(
        wifi_connect_task,
        "wifi_connect_task",
        2048,
        params,
        3,
        &wifi_connect_task_handle);
    if (ret != pdPASS) {
        delete params;
        wifi_connect_task_handle = nullptr;
        wifi_update_status("Failed");
    }
}
```

#### 4.4 连接任务（V2：`WifiManager` + `SsidManager::AddSsid`）

```cpp
static void wifi_connect_task(void *arg) {
    WifiConnectParams *params = static_cast<WifiConnectParams *>(arg);
    auto &wifi_manager = WifiManager::GetInstance();
    auto &ssid_manager = SsidManager::GetInstance();

    if (wifi_manager.IsConnected()) {
        esp_wifi_disconnect();
        vTaskDelay(pdMS_TO_TICKS(100));
    }
    if (wifi_manager.IsConfigMode()) {
        wifi_manager.StopConfigAp();
    }
    wifi_manager.StopStation();
    vTaskDelay(pdMS_TO_TICKS(500));

    ssid_manager.Clear();

    wifi_config_t empty_config = {};
    memset(&empty_config, 0, sizeof(wifi_config_t));
    esp_wifi_set_config(WIFI_IF_STA, &empty_config);

    ssid_manager.AddSsid(std::string(params->ssid), std::string(params->password));

    wifi_manager.StartStation();
    vTaskDelay(pdMS_TO_TICKS(200));

    int waited_ms = 0;
    while (waited_ms < 30000 && !wifi_manager.IsConnected()) {
        vTaskDelay(pdMS_TO_TICKS(200));
        waited_ms += 200;
    }

    if (wifi_manager.IsConnected()) {
        const std::string& connected_ssid = wifi_manager.GetSsid();
        char status[48];
        snprintf(status, sizeof(status), "Connected %s", connected_ssid.c_str());
        wifi_update_status(status);
    } else {
        wifi_update_status("Failed: Timeout");
    }

    wifi_connect_task_handle = nullptr;
    delete params;
    vTaskDelete(nullptr);
}
```

**说明**: 工程内**无** `WaitForConnected()`，用 **30s 内轮询 `IsConnected()`** 代替。

#### 4.5 断开 WiFi

**注意**: 当前断开任务**不**调用 `SsidManager::Clear()`，NVS 中已存凭证可能仍在；仅 `StopStation` + 清除 STA `wifi_config`。

```cpp
void action_wifi_disconnect(lv_event_t * e)
{
    (void)e;
    ESP_LOGI(TAG, "action_wifi_disconnect called");

    wifi_hide_keyboard();
    wifi_active_ta = nullptr;
    wifi_t9_commit_pending();

    if (wifi_connect_task_handle) {
        vTaskDelete(wifi_connect_task_handle);
        wifi_connect_task_handle = nullptr;
    }

    if (wifi_disconnect_task_handle) {
        wifi_update_status("Disconnecting...");
        return;
    }

    wifi_update_status("Disconnecting...");
    BaseType_t ret = xTaskCreate(wifi_disconnect_task, "wifi_disc", 2048, nullptr, 3, &wifi_disconnect_task_handle);
    if (ret != pdPASS) {
        wifi_disconnect_task_handle = nullptr;
        wifi_update_status("Failed");
    }
}
```

```cpp
static void wifi_disconnect_task(void* arg) {
    (void)arg;
    auto& wifi_manager = WifiManager::GetInstance();
    wifi_manager.StopStation();

    wifi_config_t empty_config = {};
    memset(&empty_config, 0, sizeof(wifi_config_t));
    esp_wifi_set_config(WIFI_IF_STA, &empty_config);

    wifi_update_status("Disconnected");
    ESP_LOGI(TAG, "WiFi disconnected (saved credentials in NVS kept)");
    wifi_disconnect_task_handle = nullptr;
    vTaskDelete(nullptr);
}
```

#### 4.6 T9 键盘映射与按键处理

**映射（文件顶部静态数组）**:
```cpp
static const char *wifi_t9_map_lower[] = {
    "1.@-", "2abc", "3def", "\n",
    "4ghi", "5jkl", "6mno", "\n",
    "7pqrs", "8tuv", "9wxyz", "\n",
    "^", "0 _", "DEL", ""
};

static const char *wifi_t9_map_upper[] = {
    "1.@-", "2ABC", "3DEF", "\n",
    "4GHI", "5JKL", "6MNO", "\n",
    "7PQRS", "8TUV", "9WXYZ", "\n",
    "^", "0 _", "DEL", ""
};
```

**定时器**: `wifi_t9_reset_timer()` 使用 **800ms** 周期；首次创建 `lv_timer_create(wifi_t9_timer_cb, 800, nullptr)`。

**按键事件**:
```cpp
void action_wifi_keypad(lv_event_t * e)
{
#if LV_USE_BUTTONMATRIX
    if (!wifi_active_ta || !objects.wifi_kb) {
        return;
    }
    uint16_t id = lv_buttonmatrix_get_selected_button(objects.wifi_kb);
    const char *txt = lv_buttonmatrix_get_button_text(objects.wifi_kb, id);
    if (!txt) {
        return;
    }

    if (strcmp(txt, "^") == 0) {
        wifi_keypad_uppercase = !wifi_keypad_uppercase;
        if (wifi_keypad_uppercase) {
            lv_buttonmatrix_set_button_ctrl(objects.wifi_kb, id, LV_BUTTONMATRIX_CTRL_CHECKED);
            lv_buttonmatrix_set_map(objects.wifi_kb, wifi_t9_map_upper);
        } else {
            lv_buttonmatrix_clear_button_ctrl(objects.wifi_kb, id, LV_BUTTONMATRIX_CTRL_CHECKED);
            lv_buttonmatrix_set_map(objects.wifi_kb, wifi_t9_map_lower);
        }
        return;
    }

    if (strcmp(txt, "DEL") == 0) {
        wifi_t9_commit_pending();
        lv_textarea_set_cursor_pos(wifi_active_ta, LV_TEXTAREA_CURSOR_LAST);
        lv_textarea_delete_char(wifi_active_ta);
        return;
    }

    wifi_t9_append_or_cycle(wifi_active_ta, txt);
#else
    (void)e;
#endif
}
```

同键循环、大小写转换在 **`wifi_t9_append_or_cycle`** / **`wifi_t9_letters_for_key`** 中完成；确认 pending 时在 **`wifi_t9_commit_pending()`** 中可自动关闭 Shift 并恢复小写 map。

---

## 依赖的组件

### WiFi（工程内 `wifi_manager.h` / `ssid_manager.h`）

```cpp
auto &wifi = WifiManager::GetInstance();
wifi.IsConnected();
wifi.IsConfigMode();
wifi.StopConfigAp();
wifi.StopStation();
wifi.StartStation();
wifi.GetSsid();

auto &sm = SsidManager::GetInstance();
sm.Clear();
sm.AddSsid(std::string(ssid), std::string(password));
```

### LVGL

**文件**: `sdkconfig.defaults`（或对应 `sdkconfig`）

```
CONFIG_LV_USE_BUTTONMATRIX=y
CONFIG_LV_USE_TEXTAREA=y
```

（若需标准 LVGL 键盘再单独开启；本 UI 使用 buttonmatrix。）

---

## 遇到的问题和解决方案

### 问题1: 键盘不显示

**原因**: 未启用 `BUTTONMATRIX`，或仅在聚焦输入框时 `wifi_show_keyboard()` 才去掉 `HIDDEN`。

**对策**: 确认 `CONFIG_LV_USE_BUTTONMATRIX=y`，且使用 `lv_buttonmatrix_create`。

### 问题2: 连接失败后仍连旧 WiFi

**原因**: Station 自动重连 NVS 中旧条目。

**对策**（与当前 `wifi_connect_task` 一致）:
```cpp
wifi_manager.StopStation();
ssid_manager.Clear();
wifi_config_t empty_config = {};
memset(&empty_config, 0, sizeof(wifi_config_t));
esp_wifi_set_config(WIFI_IF_STA, &empty_config);
ssid_manager.AddSsid(new_ssid, new_pwd);
wifi_manager.StartStation();
```

### 问题3: 超时过短

**对策**: 保持 **30s** 轮询；弱网下仍可能 `Failed: Timeout`。

### 问题4: 输入校验

与 `action_wifi_connect` 中一致：SSID 非空且 ≤32；密码为空或长度 8～63。

### 问题5: 资源与内存

- 离开页面删除 **`wifi_t9_timer`**（见 `action_wifi_back`）。
- 连接/断开任务栈 **2048**。
- 状态字符串缓冲 **48** 字节。

### 问题6: 右滑返回

```cpp
if (code == LV_EVENT_GESTURE) {
    lv_indev_get_vect(indev, &vect);
    if (vect.x < SWIPE) {
        return;
    }
}
```

---

## 内存和资源优化总结

| 优化项 | 说明 |
|--------|------|
| 连接任务栈 | `wifi_connect_task` / `wifi_disc` 均为 **2048** |
| 状态缓冲 | `char status[48]` |
| T9 定时器 | 离开 WiFi 页 `lv_timer_del(wifi_t9_timer)` |
| 连接参数 | 堆上 `WifiConnectParams`，任务结束 `delete` |

---

## app3_page 界面（入口）

**文件**: `main/boards/desktop-pet/ui/screens.c` — `create_screen_app3_page()`

```
+---------------------------+
|      [游戏 112,60]         |
|      [WiFi 112,155]        |
| [设置40,155] [聊天190,155] |
+---------------------------+
```

- 黑底；WiFi 图绑定 `action_wifi_enter`（`LV_EVENT_CLICKED`）。

---

## 测试清单

### 基本功能
- [ ] 点击 WiFi 图标进入配网页
- [ ] 聚焦输入框后 T9 显示
- [ ] 同键循环与 800ms 超时提交
- [ ] DEL / `^` 大小写切换

### 连接
- [ ] 正确 SSID/密码可连上
- [ ] 文案：`Connecting...` → `Connected ...` 或 `Failed: Timeout`
- [ ] 超长 SSID / 密码长度错误提示

### 断开
- [ ] OFF 后 STA 停止；**确认 NVS 行为是否符合预期**（当前实现保留 NVS）

### 返回与资源
- [ ] `<` 与右滑返回 `app3_page`
- [ ] 多次进出无异常

---

## 调试日志关键字

```
action_wifi_enter called
action_wifi_back called
action_wifi_connect called
=== Starting WiFi connection task for SSID
Cleared SsidManager
Added ONLY new WiFi
Waiting for connection (30s timeout)
Successfully connected to
Failed to connect
T9 timer deleted to save resources
WiFi disconnected (saved credentials in NVS kept)
SSID empty / SSID too long / Password too short / Password too long
```

---

## 大小写切换（摘要）

- 全局 **`wifi_keypad_uppercase`**；**`^`** 切换 map 与 `LV_BUTTONMATRIX_CTRL_CHECKED`。
- **`wifi_t9_append_or_cycle`** 内对字母使用 `toupper`（当 Shift 开启时）。
- **`wifi_t9_commit_pending()`** 在超时或确认后可将 Shift 复位为小写 map。
- **点击页面背景**: `action_wifi_page_clicked` 仅在 `target == current_target == wifi_page` 时隐藏键盘并提交 pending。

**实现位置**: 均在 **`ui_wifi.cc`**（不再使用单独的 `action.cc` 中的旧实现）。

---

## 后续改进建议

1. WiFi 扫描列表点选 SSID  
2. 密码显示/隐藏切换  
3. 多热点与 RSSI  
4. 若产品要求 OFF 清除 NVS，在 `wifi_disconnect_task` 中增加 `SsidManager::Clear()` 并充分测试  

---

**文档版本**: v1.4  
**最后更新**: 2026-03-29  
**更新说明**: 恢复完整章节结构；**代码块全部改为 `desktop-pet/ui_wifi.cc` + `screens.h` 当前实现**；补充 V2 `WifiManager` / `AddSsid`、断开保留 NVS 的说明。
