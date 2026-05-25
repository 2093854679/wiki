## Desktop-pet V2 设置页面（音量 & 亮度）设计说明

本文档说明在 `desktop-pet` V2 工程中新增的 **设置页面（Setting）** 的设计与实现，便于后续 review 与维护。

适用目录：

- 工程根：`xiaozhi-esp32-main-v2/xiaozhi-esp32`
- 相关代码路径：
  - 设置页 UI 与逻辑：`main/boards/desktop-pet/ui/ui_setting.cc`, `ui_setting.h`
  - 主屏创建与入口：`main/boards/desktop-pet/ui/screens.c`
  - 图片资源：`main/boards/desktop-pet/ui/images/ui_image_volume.c`, `ui_image_light.c`, `ui_image_seting.c`

---

## 1. 目标与交互概览

- 在 `desktop-pet` V2 上增加一个 **设置页面**，用于调节：
  - **音量**：映射到底层 `AudioCodec::SetOutputVolume(int volume)`；
  - **亮度**：映射到底层 `Backlight::SetBrightness(uint8_t brightness, bool permanent)`。
- 入口方式：
  - 从 `app3_page` 点击设置图标（`img_seting`）进入设置页；
  - 设置页顶部有返回按钮 `<` 与右滑手势，返回 `app3_page`；
  - 整体交互风格对齐 WiFi 配网页（`ui_wifi.cc`）。

用户视角流程：

1. 在第三页（`app3_page`）上点击设置图标；
2. 进入 Setting 页面，顶部显示 “Setting”，中间两行分别为「音量」和「亮度」；
3. 左侧为图标，中间为滑块，右侧/下方为当前数值文本（如 `音量: 70`、`亮度: 80`）；
4. 拖动滑块实时改变音量和屏幕亮度；
5. 点击左上角 `<` 或右滑，返回 `app3_page`。

---

## 2. 代码结构总览

### 2.1 头文件：`ui_setting.h`

定义了设置页面的对外接口：

- `void create_screen_setting();`
- `void tick_screen_setting();`（当前为空实现，预留扩展）
- `void action_setting_enter(lv_event_t *e);`  —— 从 `app3_page` 进入设置页
- `void action_setting_back(lv_event_t *e);`   —— 从设置页返回 `app3_page`

> 说明：所有接口都只依赖 `lvgl.h`，与 WiFi 页的 `ui_wifi.h` 风格一致。

### 2.2 主实现文件：`ui_setting.cc`

职责：

- 创建 Setting 页面 UI 结构（背景、顶部栏、两条设置项）；
- 处理进入/返回事件；
- 根据滑块值调用底层 Board 的音量与背光接口；
- 保持与 WiFi 页一致的线程安全策略（`lvgl_port_lock/unlock`）。

设置页面本身 **不修改** 全局 `objects_t` 结构，而是通过一组静态指针管理自己的控件：

- `static lv_obj_t *setting_page;`
- `static lv_obj_t *setting_slider_volume;`
- `static lv_obj_t *setting_slider_light;`
- `static lv_obj_t *setting_label_volume;`
- `static lv_obj_t *setting_label_light;`

### 2.3 主屏入口文件：`screens.c`

当前版本中，`screens.c` 只负责：

- 创建 `app3_page`、WiFi 页等主屏；
- 在 `app3_page` 中挂 WiFi 图标，对应 `action_wifi_enter`。

> 设置图标入口目前根据需求可以选择是否挂在 `app3_page` 上：  
> - 若挂载：参考 WiFi 图标的方式新增 `img_seting` + `action_setting_enter`；  
> - 若不挂载：可从其他触发点调用 `action_setting_enter`。

---

## 3. Setting 页面 UI 设计细节

### 3.1 顶部栏（对齐 WiFi）

- 使用一个高度约 `26px` 的容器作为顶部栏：
  - 背景颜色：`0xff1b1b1b`（深灰）；
  - 无边框，左右有内边距；
  - 与 WiFi 页顶部栏风格保持一致。
- 左侧返回按钮：
  - `lv_btn` + `<` 文本；
  - 点击事件：`LV_EVENT_CLICKED` 绑定 `action_setting_back`。
- 中央标题：
  - `lv_label`，文本 `"Setting"`（如需中文可改为 `"设置"`）；
  - 字体与颜色对齐 WiFi 页（`lv_font_montserrat_14`，白色）。

### 3.2 内容区域布局

整体背景：

- 根对象 `setting_page` 设置为纯黑背景：`0xff000000`，不透明。

两条设置项（从上到下）：

1. **音量行**
   - 左侧图标：`img_volume`（位于 ~`(18, 60)`）
   - 中间滑块：`setting_slider_volume`
     - 位置约 `(85, 75)`，宽 `181` 像素；
     - 范围 `0–100`，初始值 `50`（进入页面时会同步为当前音量）；
     - 值改变事件：`LV_EVENT_VALUE_CHANGED` → `setting_volume_slider_event_cb`。
   - 文本标签：`setting_label_volume`
     - 位置约 `(85, 100)`；
     - 文本格式：`"音量: 50"`、`"音量: 70"` 等；
     - 字体颜色为白色。

2. **亮度行**
   - 左侧图标：`img_light`（位于 ~`(18, 150)`）
   - 中间滑块：`setting_slider_light`
     - 位置约 `(85, 165)`，宽 `181`；
     - 范围 `0–100`，初始值 `80`（进入页面时会同步为当前亮度）；
     - 值改变事件：`LV_EVENT_VALUE_CHANGED` → `setting_light_slider_event_cb`。
   - 文本标签：`setting_label_light`
     - 位置约 `(85, 190)`；
     - 文本格式：`"亮度: 80"` 等。

### 3.3 手势支持

- 整个 `setting_page` 根对象添加 `LV_EVENT_GESTURE` 事件，回调为 `action_setting_back`；
- 在回调中检测当前输入向量 `vect.x`，若大于设定阈值（`SWIPE`，当前为 `20`），视为右滑并执行返回；
- 小于阈值则忽略，避免误触。

---

## 4. 行为与事件逻辑

### 4.1 进入设置页：`action_setting_enter(lv_event_t *e)`

调用路径示例：

- 从 `app3_page` 的设置图标点击：
  - `lv_obj_add_event_cb(setting_icon, action_setting_enter, LV_EVENT_CLICKED, nullptr);`

实现要点：

1. 在进入逻辑开始处先调用 `create_screen_setting()`，确保页面与控件已经创建（懒加载：仅首次实际创建，其余调用直接 return）；
2. 通过 `Board::GetInstance()` 获取硬件对象：
   - `AudioCodec *codec = board.GetAudioCodec();`
   - `Backlight *backlight = board.GetBacklight();`
3. 读出当前音量与亮度：
   - `volume = codec ? codec->output_volume() : 50;`
   - `brightness = backlight ? backlight->brightness() : 80;`
   - 并限制在 `0–100`。
4. 同步 UI：
   - 若 `setting_slider_volume` 存在，设置范围 `0–100` 与当前值；
   - 若 `setting_slider_light` 存在，同理；
   - 使用 `setting_update_volume_label` / `setting_update_light_label` 更新文本标签。
5. 切换页面：
   - 使用 `lv_screen_load_anim(setting_page, LV_SCR_LOAD_ANIM_NONE, ANIMATION_DURATION_MS, 0, false);` 切换；
   - 全程使用 `lvgl_port_lock(0)` / `lvgl_port_unlock()` 保护。

### 4.2 返回上一页：`action_setting_back(lv_event_t *e)`

触发途径：

- 顶部返回按钮点击：`LV_EVENT_CLICKED`；
- 页面根对象右滑：`LV_EVENT_GESTURE`。

实现逻辑：

1. 若事件类型为 `LV_EVENT_GESTURE`，则通过 `lv_indev_get_vect` 获取滑动向量：
   - 当 `vect.x < SWIPE`（滑动距离不足）时直接返回，不做处理；
   - 否则视为有效右滑。
2. 在 `lvgl_port_lock` / `unlock` 包裹下调用：
   - `lv_screen_load_anim(objects.app3_page, LV_SCR_LOAD_ANIM_NONE, ANIMATION_DURATION_MS, 0, false);`
3. 日志中打点 `action_setting_back called` 以便调试。

### 4.3 滑块事件：`setting_volume_slider_event_cb` / `setting_light_slider_event_cb`

通用流程：

1. `lv_event_get_target(e)` 获取当前 slider 对象；
2. 使用 `lv_slider_get_value(obj)` 取得 `0–100` 的新值；
3. 调设置接口：
   - 音量：`codec->SetOutputVolume(value);`
   - 亮度：`backlight->SetBrightness((uint8_t)value, true);`
4. 更新对应标签文本。

错误处理：

- 若 `Board::GetAudioCodec()` 或 `GetBacklight()` 返回空指针，仅打印 `ESP_LOGW` 警告，不崩溃。

---

## 5. 与 WiFi 界面实现的异同

**相同点：**

- 都是通过单独的 `ui_xxx.cc/h` 管理 UI 与事件逻辑；
- 进入页面前会做状态同步（WiFi 页更新连接状态；Setting 页更新音量和亮度）；
- 切页统一使用 `lv_screen_load_anim(..., ANIMATION_DURATION_MS, ...)`；
- 返回页面支持顶部按钮和右滑手势。

**不同点：**

- WiFi 页的 `objects.wifi_page` 等对象由 `ui_wifi.cc` 直接写入 `objects_t` 中；  
  Setting 页为了不破坏既有布局，**不再往 `objects_t` 加字段**，而是用 `static lv_obj_t*` 指针自管理。
- WiFi 页参加了主屏幕 tick 表 `tick_screen_funcs[]`；  
  Setting 页目前不需要每帧刷新逻辑，因此没有加入 tick 表，完全事件驱动。

---

## 6. 设计决策与坑点记录

### 6.1 不再修改 `objects_t` 结构

曾经的尝试：

- 在 `screens.h` 的 `objects_t` 结构中添加 `setting`、`setting_volume_label` 等字段；
- 同时扩展 `ScreensEnum` 和 `tick_screen_funcs`。

问题：

- 该结构的布局与 EEZ/LVGL Flow 生成的 assets 强相关，随意增加字段会改变 `sizeof(objects)` 与每个对象指针的偏移；
- 导致 WiFi 页面等原有对象指针“错位”，出现点击 WiFi 界面卡死的问题。

最终决策：

- **不再向 `objects_t` 添加 Setting 相关字段**；
- Setting 页使用独立的 `static lv_obj_t*` 管理，避免破坏原有布局；
- 如需在其他模块访问 Setting 控件，可通过新增 API 暴露读写函数，而不是暴露内部指针。

### 6.2 Setting 是否加入 `create_screens()` / tick 表

当前策略：

- `create_screen_setting()` 采用懒加载模式：首次进入时创建；
- `create_screens()` 中不强制调用 `create_screen_setting()`；
- 不加入 `tick_screen_funcs[]`，因为目前没有周期刷新需求。

可选策略：

- 若希望完全对齐 WiFi，可在 `create_screens()` 里增加：
  - `create_screen_setting();`
- 若未来 Setting 页需要周期更新（例如跟随外部状态实时刷新），可以再考虑加入 `tick_screen_funcs[]` 与对应的枚举。

---

## 7. 使用与扩展建议

### 7.1 给 app3 页挂载设置图标（入口）

参考 WiFi 图标，在 `create_screen_app3_page()` 中添加：

```c
// ===== 设置图标 =====
{
    lv_obj_t *obj = lv_image_create(parent_obj);
    lv_obj_set_pos(obj, 40, 155);
    lv_obj_set_size(obj, LV_SIZE_CONTENT, LV_SIZE_CONTENT);
    lv_image_set_src(obj, &img_seting);
    lv_obj_add_flag(obj, LV_OBJ_FLAG_CLICKABLE);
    lv_obj_add_event_cb(obj, action_setting_enter, LV_EVENT_CLICKED, (void *)0);
}
```

之后在设备上测试：

1. 进入 `app3_page`；
2. 点击设置图标，进入 Setting 页面；
3. 调节音量 / 亮度，确认硬件效果与 UI 文本同步；
4. 点击 `<` 或右滑返回 `app3_page`。

### 7.2 未来可选增强

- **设置值持久化**：通过 NVS 存储音量和亮度，下次上电恢复；
- **增加 +/- 精细调节按钮**：在滑块两端增加按钮，以固定步长微调；
- **一键静音 / 熄屏**：增加开关，快速切到 0 音量或最低亮度；
- **多语言支持**：将 `"音量" / "亮度" / "Setting"` 文本抽到语言资源表中。

