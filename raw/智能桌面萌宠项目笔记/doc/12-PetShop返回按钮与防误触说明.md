## Desktop-pet V2 商店返回按钮与宠物页防误触说明

本文档说明在 `desktop-pet` V2 工程中，围绕 **Pet Shop 商店页返回按钮** 与 **宠物首页戳脸防误触** 所做的补充改动，便于后续维护和联调。

- 工程根：`xiaozhi-esp32-main-v2/xiaozhi-esp32`
- 主要代码：
  - 商店页 UI：`main/boards/desktop-pet/ui/ui_shop.cc`
  - 商店/宠物页手势：`main/boards/desktop-pet/ui/action.cc`
  - 宠物首页：`main/boards/desktop-pet/ui/ui_pet.cc`, `ui_pet.h`
  - 图片资源：`main/boards/desktop-pet/ui/images/ui_image_return.c`, `images.h`

---

## 1. 商店页右下角返回按钮

### 1.1 需求与行为

- 在商店页右下角增加一个 **55×55 返回图标按钮**；
- 位置与食物按钮网格对齐，放在 **第二行第三列**（右下角）；
- 点击后返回宠物首页（`SCREEN_ID_PET_PAGE`），动画方向为 **自下而上切回**；
- 保留原有“下滑返回宠物页”的手势，不做改动。

### 1.2 图标资源定义

- 文件：`main/boards/desktop-pet/ui/images/ui_image_return.c`
- 类型：`lv_image_dsc_t`，尺寸 **55×55**，RGB565：
  - `.header.w = 55`
  - `.header.h = 55`
- 在 `images.h` 中增加声明，供 UI 引用：

```c
extern const lv_image_dsc_t ui_image_return;          // 商店返回按钮 55x55
```

### 1.3 商店页 UI 中创建返回按钮

- 文件：`ui_shop.cc`，函数：`create_screen_shop_page()`
- 原有食物按钮布局：
  - 屏幕尺寸：`280×240`
  - 按钮尺寸：
    - `SHOP_ITEM_W 55`
    - `SHOP_ITEM_H 75`
    - `SHOP_BTN_W 55`
    - `SHOP_BTN_H 55`
  - 网格坐标：`SHOP_ITEM_POS[5]`：
    - 第 1 行：`(29,55)`、`(113,55)`、`(197,55)`
    - 第 2 行：`(29,145)`、`(113,145)`

- 新增返回按钮容器（直接使用 `obj` 作为父）：
  - 尺寸：`SHOP_BTN_W × SHOP_BTN_H`（55×55）
  - 位置：
    - `x = SHOP_ITEM_POS[2].x`（与第 1 行第 3 个食物对齐列）
    - `y = SHOP_ITEM_POS[3].y`（与第 2 行第 1 个食物对齐行）
  - 样式：背景全透明、无边框、无阴影，仅展示图标：
    - `bg_opa = 0`
    - `border_width = 0`
    - `shadow_width = 0`

- 在按钮中创建图标：
  - 使用 `lv_img_create(btn)`；
  - `lv_obj_center(img);`
  - `lv_image_set_src(img, &ui_image_return);`

### 1.4 返回逻辑：点击返回宠物页

- 在 `ui_shop.cc` 中新增点击回调：

```c
static void shop_back_clicked(lv_event_t *e) {
    (void)e;
    loadScreenAnim(SCREEN_ID_PET_PAGE, LV_SCR_LOAD_ANIM_MOVE_BOTTOM, 200);
}
```

- 在创建返回按钮时，绑定事件：

```c
lv_obj_add_event_cb(btn, shop_back_clicked, LV_EVENT_CLICKED, nullptr);
```

- 这样用户可以：
  - 上滑从宠物页进入商店；
  - 在商店页通过 **下滑手势** 或 **点击右下角返回图标** 回到宠物首页。

---

## 2. 宠物首页“戳脸”防误触改动

### 2.1 问题背景

- 宠物首页根对象 `objects.main` 同时绑定了：
  - 手势事件：`LV_EVENT_GESTURE` → `action_main_gesture`
  - 短点击事件：`LV_EVENT_SHORT_CLICKED` → `poke_face_cb`（“戳你小脸”）
- 在实际设备上，从宠物页滑动切换到其他页面（商店页 / 养成状态页 / 左右 app 页）时：
  - LVGL 在识别滑动手势后，有时还会额外触发一次短点击事件；
  - 导致刚滑走页面，就立即触发了一次“戳你小脸”的上云交互，体验上属于误触。

### 2.2 设计思路

核心思路：在“从宠物页导航到其他页面”的手势发生时，记录一个 **最近导航时间戳**；  
在戳脸回调中，如果当前时间与最近导航时间相差小于某个门限（例如 300ms），**直接忽略这次点击**。

这样可以保留原有“短按戳脸”交互，同时过滤掉“刚刚滑动切页引起的残余点击”。

### 2.3 对外接口：标记导航事件

- 文件：`ui_pet.h`
- 新增接口声明：

```c
// 从宠物首页通过手势导航到其他页面时调用，用于避免误触戳脸
void pet_page_mark_navigate(void);
```

### 2.4 宠物页内部实现与防抖逻辑

- 文件：`ui_pet.cc`

1. 新增状态与参数：

```c
static uint32_t s_last_poke_ms = 0;
static constexpr uint32_t kPokeCooldownMs = 1000;
static uint32_t s_last_nav_ms  = 0;
static constexpr uint32_t kNavIgnoreMs = 300;
```

2. 实现导航标记函数：

```c
void pet_page_mark_navigate(void) {
    s_last_nav_ms = lv_tick_get();
}
```

3. 在戳脸回调中增加“导航后忽略窗口”判断：

```c
static void poke_face_cb(lv_event_t *e) {
    (void)e;
    uint32_t now = lv_tick_get();
    // 刚刚发生过导航手势，忽略这次点击，避免“滑动到其他页面”被当成戳脸
    if (now - s_last_nav_ms < kNavIgnoreMs) return;
    if (now - s_last_poke_ms < kPokeCooldownMs) return;
    s_last_poke_ms = now;

    ESP_LOGI(TAG, ">>> 戳你小脸 → TriggerPetInteraction");
    pet_on_poke();
    Application::GetInstance().TriggerPetInteraction("戳你小脸");
}
```

> 说明：  
> - `kNavIgnoreMs` 当前为 300ms，可根据后续测试情况微调；  
> - 不影响原有 1 秒冷却时间（`kPokeCooldownMs`），两者叠加生效。

### 2.5 手势导航中调用标记函数

- 文件：`action.cc`
- 引入头文件：

```c
#include "ui_pet.h"
```

- 在 `action_main_gesture(lv_event_t * e)` 中，对所有“从宠物页离开”的手势，调用 `pet_page_mark_navigate()`：

1. 左滑进入 `APP1`：

```c
if (vect.x < -SWIPE) {
    pet_page_mark_navigate();
    loadScreenAnim(SCREEN_ID_APP1_PAGE, LV_SCR_LOAD_ANIM_MOVE_LEFT, ANIMATION_DURATION_MS);
}
```

2. 右滑进入 `APP3`：

```c
if (vect.x > SWIPE) {
    pet_page_mark_navigate();
    loadScreenAnim(SCREEN_ID_APP3_PAGE, LV_SCR_LOAD_ANIM_MOVE_RIGHT, ANIMATION_DURATION_MS);
}
```

3. 下滑进入养成状态页：

```c
if (vect.y > SWIPE) {
    pet_page_mark_navigate();
    action_pet_status_enter(nullptr);
}
```

4. 上滑进入商店页：

```c
if (vect.y < -SWIPE) {
    pet_page_mark_navigate();
    lvgl_port_lock(0);
    loadScreenAnim(SCREEN_ID_SHOP_PAGE, LV_SCR_LOAD_ANIM_MOVE_TOP, ANIMATION_DURATION_MS);
    ui_refresh_gold();
    lvgl_port_unlock();
}
```

### 2.6 行为验证预期

- 滑动从宠物页切换到任意其他页面（商店页 / 养成状态页 / 左右 app 页）时：
  - 不再出现“刚切走页面就立即触发戳脸”的误触行为；
- 正常在宠物页短按屏幕：
  - 仍会触发“戳你小脸”上云交互，冷却时间维持为 1 秒；
- 若将来更换面板或调整屏幕采样参数，只需根据实际体验微调 `kNavIgnoreMs` 即可。

---

## 3. 回归测试建议

1. **商店返回按钮**
   - 从宠物页上滑进入商店；
   - 校验右下角返回图标是否正确显示、大小为 55×55，与食物按钮对齐；
   - 点击图标，确认以 `MOVE_BOTTOM` 动画返回宠物页；
   - 保证下滑手势仍可正常返回。

2. **戳脸防误触**
   - 在宠物页连续上下左右滑动，频繁切换页面，观察日志与实际行为：
     - 不应再出现“误触戳脸”；
   - 在宠物页正常短按测试戳脸：
     - 首次点击立刻触发“戳你小脸”；
     - 1 秒内多次点击只算一次（原有冷却逻辑保持生效）。

---

## 4. Web 控制面板（LAN WebServer）改动说明

### 4.1 概览

- 文件：`main/boards/desktop-pet/web_server.cc`
- 访问入口：设备连上 Wi-Fi 后，在日志中会打印 `Web server → http://<ip>/`，浏览器访问即可。
- 页面功能：
  - 显示宠物状态：阶段（陌生/熟悉/亲密）、亲密度、心情、金币、RAM 占用、相识天数；
  - 通过按钮进行互动：摸头、戳脸、喂零食（苹果/香蕉/薯片/蜂蜜/草莓）、重置养成数据；
  - 显示 Web 接口的简单性能统计（调用次数 / 最近耗时 / 峰值耗时）。

### 4.2 状态总览 UI 设计

- 顶部标题：`🐻 桌面宠物 · LAN 控制面板`。
- 样式：暗色玻璃拟态 + 渐变背景，统一在内联 CSS 中。
- 状态总览卡片内容：
  - 第一行：三个阶段圆点（陌生 / 熟悉 / 亲密），与设备端宠物状态页视觉统一。
  - 第二行：四个圆环仪表（使用 `conic-gradient` 绘制）：
    - **金币**：使用 `gold` 值，圆环显示 0–9999 的百分比，内圈数字显示当前金币数；
    - **亲密度**：使用 `intimacy`（0–100），内圈显示百分比；
    - **心情**：使用 `mood`（0–100），内圈显示百分比，说明标签显示“心情 · 开心/平静/低落”；
    - **RAM 占用**：使用 `heap_total` / `heap_free`，只显示百分比圆环，去掉具体 KB 文本。
  - 底部：`相识 X 天`，与设备端宠物状态页保持一致。

### 4.3 互动控制区布局

- 互动卡片标题：**互动控制**。
- 第一行（3 个按钮）：
  - `🤚 摸头` → 调用 `/api/action?type=pat`，内部执行 `pet_on_pat()` + `TriggerPetInteraction("轻摸你头")`；
  - `👉 戳脸` → 调用 `/api/action?type=poke`，内部执行 `pet_on_poke()` + `TriggerPetInteraction("戳你小脸")`；
  - `♻️ 重置` → 调用 `/api/action?type=reset`，内部执行 `pet_reset()`。
  - 使用 `btn-row btn-row-triple` + CSS Grid 保证一行恰好 3 个按钮。
- 第二行（零食按钮，一行最多 3 个，自动换行）：
  - `🍎 苹果 · 50💰` → `feed_apple`
  - `🍌 香蕉 · 30💰` → `feed_banana`
  - `🍟 薯片 · 80💰` → `feed_chips`
  - `🍓 草莓 · 60💰` → `feed_strawberry`
  - `🍯 蜂蜜 · 70💰` → `feed_honey`（价格由原来的 120 降为 70，UI 与后端一致）
- Web 性能卡片放在最底部，展示 `/api/pet_state` 和 `/api/action` 的调用次数、最近耗时和最大耗时，用于调试。

### 4.4 Web API 行为与限制

- **宠物状态接口**：`GET /api/pet_state`
  - 返回 JSON，包括：
    - `stage` / `stage_id`、`intimacy` / `daily_intimacy` / `intimacy_max`；
    - `mood` / `mood_text`、`age_days`、`gold`；
    - `heap_free` / `heap_total` / `heap_used_pct`；
    - `http_perf`：Web 性能统计字段（调用次数、最近耗时、峰值耗时，单位 µs）。
- **动作接口**：`POST /api/action?type=...`
  - `pat` / `poke`：与设备 UI 上的摸头/戳脸逻辑一致，会走触摸/戳脸的本地逻辑和云端交互。
  - `feed_xxx`：调用 `web_shop_buy_and_feed()`，共用与商店页一致的价格和逻辑：
    - 会检查金币是否足够，不够时不扣费；
    - 成功后调用 `pet_feed(id)`，并注入对应的“投喂xxx”交互文本。
  - `reset`：调用 `pet_reset()` 重置养成数据。

### 4.5 Web 投喂前强制回到空闲状态

- 为了避免在设备当前处于“连接中 / 说话 / 聆听”状态时从 Web 再触发一轮投喂导致状态机混乱，在 `web_shop_buy_and_feed()` 中增加了：

```c++
auto &app = Application::GetInstance();
app.SetDeviceState(kDeviceStateIdle);
app.TriggerPetInteraction(text);
```

- 含义：
  - 通过 Web 发起的投喂动作，会先把设备状态切回 `kDeviceStateIdle`，再发起一次“投喂xxx”的交互；
  - 这样可以保证云端对话和本地状态机的起点一致，减少“上一轮还在说话/听着”的残留影响。

### 4.6 金币与亲密度规则补充

- 金币：
  - 总数上限为 **9999**，在 `clamp_data()` 中统一截断（所有来源的金币加成都生效）；
  - Web 页面金币圆环使用 0–9999 映射到 0–100%。
- 亲密度：
  - 0–100，满 100 后触发阶段提升，亲密度归零；
  - 每日上限 `DAILY_INTIMACY_CAP = 20` 仍然生效，只对通过 `compute_gain()` 的亲密来源（摸头 / 完整对话）有效；
  - `pet_feed` 当前仍是额外亲密来源，不计入每日上限（后续如需一致，可改为也走 `compute_gain()`）。


