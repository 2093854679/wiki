## Desktop-pet V2 商店页面（Pet Shop）UI 说明

本文档说明在 `desktop-pet` V2 工程中新增的 **商店页面（Pet Shop）** 的交互入口与 UI 结构，便于后续继续实现“投喂/购买”等业务逻辑。

适用目录：

- 工程根：`xiaozhi-esp32-main-v2/xiaozhi-esp32`
- 相关代码路径：
  - 商店页 UI：`main/boards/desktop-pet/ui/ui_shop.cc`, `ui_shop.h`
  - 入口/返回手势：`main/boards/desktop-pet/ui/action.cc`
  - 屏幕注册：`main/boards/desktop-pet/ui/screens.c`, `screens.h`
  - 食物图标资源：`main/boards/desktop-pet/ui/images/ui_image_shop_*.c`
  - 即时购买/投喂逻辑：当前内置在 `main/boards/desktop-pet/ui/ui_shop.cc`（后续可再抽模块）

---

## 1. 交互概览（入口 / 返回）

### 1.1 从宠物页进入商店页

- 触发位置：宠物页（`objects.main`）手势回调 `action_main_gesture`
- 触发动作：**上滑进入商店页**
- 代码：`main/boards/desktop-pet/ui/action.cc`
  - `vect.y < -SWIPE` 时执行：
    - `loadScreenAnim(SCREEN_ID_SHOP_PAGE, LV_SCR_LOAD_ANIM_MOVE_TOP, ANIMATION_DURATION_MS);`

### 1.2 从商店页返回宠物页

- 触发位置：商店页（`objects.shop_page`）手势回调 `action_shop_gesture`
- 触发动作：**下滑返回宠物页**
- 代码：`main/boards/desktop-pet/ui/action.cc`
  - `vect.y > SWIPE` 时执行：
    - `loadScreenAnim(SCREEN_ID_PET_PAGE, LV_SCR_LOAD_ANIM_MOVE_BOTTOM, ANIMATION_DURATION_MS);`

> 说明：原“养成状态页”仍保留在宠物页的下滑入口（`vect.y > SWIPE` → `action_pet_status_enter(nullptr)`），商店页与养成状态页互不影响。

---

## 2. 屏幕注册（create/tick）

- `objects_t` 增加字段：`lv_obj_t *shop_page;`
  - 文件：`main/boards/desktop-pet/ui/screens.h`
- `create_screens()` 中创建商店页：
  - 文件：`main/boards/desktop-pet/ui/screens.c`
  - 调用：`create_screen_shop_page();`
- `tick_screen_funcs[]` 中注册商店 tick：
  - 文件：`main/boards/desktop-pet/ui/screens.c`
  - 增加：`tick_screen_shop_page`

---

## 2.1 切屏与 tick 的约束（重要）

当前工程（非 EEZ 分支）`ui_tick()` 的行为是：

- 只会执行 `tick_screen(currentScreen)`（即只 tick “当前 screen 索引”）

因此如果仅使用 `lv_screen_load_anim(objects.xxx_page, ...)` 直接切换显示对象，但 **不更新 `currentScreen`**，会导致：

- 屏幕虽然显示切过去了，但 `tick_screen_xxx()` **不会被调用**
- 依赖 tick 的 UI 刷新（例如商店金币刷新）会出现“进入页面显示为 0、点一下才刷新”等问题

为避免踩坑，页面切换统一使用新增接口：

- `loadScreenAnim(SCREEN_ID_XXX, anim, ANIMATION_DURATION_MS)`

该接口会同步更新 `currentScreen`，保证 `ui_tick()` 会 tick 到当前显示页面。

相关实现：

- 接口声明：`main/boards/desktop-pet/ui/ui.h`
- 接口实现：`main/boards/desktop-pet/ui/ui.c`
- 统一改造切屏调用点：`main/boards/desktop-pet/ui/action.cc`

---

## 3. UI 结构（标题栏 + 商品卡片）

商店页整体尺寸为 **280×240**，深色背景。

### 3.1 标题栏（Header）

- 容器：`header`
  - 位置：`(0,0)`
  - 尺寸：`280×36`
  - 背景色：`0x222222`
  - 无边框、无阴影、无内边距
- 标题文字：
  - 文本：`Pet Shop`
  - 对齐：水平/垂直居中
  - 颜色：白色
  - 字体：若启用 `LV_FONT_MONTSERRAT_18` 则使用 `lv_font_montserrat_18`
- 分割线（标题下方）：
  - 位置：`(0,36)`
  - 尺寸：`280×1`
  - 颜色：`0x555555`

### 3.2 右上角金币余额（gold_box）

标题栏右侧显示金币余额，结构如下：

- `gold_box`：放在 `header` 内部，右对齐、垂直居中，距离右边距 **20px**
  - `gold_icon`：当前使用 `$`（ASCII，保证字库可显示）
  - `gold_label`：显示数字余额（颜色 `0xFFD700`）

金币刷新函数：

- `ui_refresh_gold()`：从 `pet_get_data()->gold` 读取余额并刷新 `gold_label`

### 3.2 商品卡片（container + btn + price）

每个商品为一个容器 `container(55×75)`，内部结构：

- `btn(55×55)`：放食物图标，仍使用 `lv_btn`
- `price label(55×20)`：显示价格文字，位于按钮下方 \(y = 55 + 3\)，居中，金色 `0xFFD700`

> 注意：`💰` 等 emoji 往往不在当前字体字库中，实际显示可能为空白/方块，因此价格前缀改为 ASCII 字符（例如 `$`）以保证必定可见。

---

## 4. 布局坐标（容器坐标）

商品保持 **3 + 2** 排列，并将第二排**左对齐第一排**：

- 第 1 行（3 个）：`(29,55)`、`(113,55)`、`(197,55)`
- 第 2 行（2 个）：`(29,140)`、`(113,140)`

对应图片资源与价格（示例）：

| food_id | 图标资源 | 价格 |
|---:|---|---:|
| 0 | `ui_image_shop_apple` | 50 |
| 1 | `ui_image_shop_banana` | 30 |
| 2 | `ui_image_shop_chips` | 80 |
| 3 | `ui_image_shop_honey` | 70 |
| 4 | `ui_image_shop_strawberry` | 60 |

---

## 5. 点击交互（即时购买 + 立即投喂 + 返回宠物页）

- 控件：仍为 `lv_btn`
- 事件：`LV_EVENT_CLICKED`
- 回调函数：`shop_food_clicked`
- `user_data`：传递 `food_id`（0~4）
- 点击流程：
  - 根据 `food_id` 取价格
  - 判断金币是否足够
    - 足够：扣金币 → `pet_feed(food_id)` → 触发上云文本 → 刷新金币 UI → 打印成功日志 → **自动切回宠物主页面**
    - 不足：不扣钱 → toast 提示“金币不足” → 打印失败日志

```c
FoodId id = ...
bool ok = shop_buy_and_feed(id);
if (ok) {
    ui_refresh_gold();
    ui_show_toast("购买成功");
    ESP_LOGI(TAG, "buy success id=%d", (int)id);
    // 购买成功后直接返回宠物主页面
    loadScreenAnim(SCREEN_ID_PET_PAGE, LV_SCR_LOAD_ANIM_MOVE_BOTTOM, 200);
} else {
    ui_show_toast("金币不足");
    ESP_LOGW(TAG, "not enough gold id=%d", (int)id);
}
```

### 5.1 预留函数（当前为空实现/日志代替）

- `ui_show_toast(const char *msg)`：暂用日志代替，不改动现有 UI 结构
- `mcp_send_feed_event(int food_id)`：预留 MCP hook，先不实现

---

## 6. 宠物数据与投喂接口（基础依赖）

为支持商店扣金币，本次在宠物数据结构中新增字段：

- `PetData.gold`：金币余额（NVS key：`gold`，默认值调试阶段为 `9999`，正式可调整为较小值）

相关接口（文件：`main/boards/desktop-pet/pet_tamagotchi.h/.cc`）：

- `const PetData* pet_get_data(void);`
- `PetData* pet_get_data_mutable(void);`
- `void pet_feed(FoodId id);`：投喂后更新宠物状态（当前为最小实现：心情+3、亲密+1，并保存）


---

## 7. 金币获取规则（不限每日上限）

金币完全由本地“养成行为”产生，目前 **不设每日上限**，但每次奖励额度较大，便于玩家频繁购买零食。

### 7.1 每日登录 / 新的一天奖励

- 触发位置：`pet_tamagotchi.cc::check_new_day()` 在检测到新日期时。
- 行为：
  - `age_days++`、`daily_intimacy` 重置；
  - 心情回归中值；
  - **金币：`s_data.gold += 100;`**
- 日志：`new day: age=... daily_int reset, gold=...`

### 7.2 互动奖励：摸头 / 戳脸 / 对话

所有奖励都在 `pet_tamagotchi.cc` 的对应接口中累加：

- `void pet_on_pat(void);`（摸头）
  - 亲密度递减收益 +2 心情（原有逻辑）；
  - **金币：`s_data.gold += 5;`**
  - 日志：`on_pat ... gold=...`
- `void pet_on_poke(void);`（戳脸）
  - 心情 +1（原有逻辑）；
  - **金币：`s_data.gold += 2;`**
  - 日志：`on_poke → mood=... gold=...`
- `void pet_on_chat(void);`（一轮对话完成）
  - 亲密度递减收益 +1 心情（原有逻辑）；
  - **金币：`s_data.gold += 15;`**
  - 日志：`on_chat ... gold=...`

### 7.3 阶段提升成就奖励

在 `try_promote()` 中，当亲密度达到上限并升阶段时，追加一次性金币奖励：

- 陌生 → 熟悉（`PET_STAGE_FAMILIAR`）：**金币 +200**
- 熟悉 → 亲密（`PET_STAGE_INTIMATE`）：**金币 +400**
- 日志：`stage up! → X, gold=...`

> 说明：以上规则叠加后，正常互动几分钟就能获得数百金币，结合当前食物价格（30~120）可以较为频繁地购买零食。


---

## 8. 购买投喂上云触发（对齐摸头 / 戳脸）

商店购买成功后，会像“摸头/戳脸”一样，将**动作文本**发送到云端，用于触发 LLM 行为。

### 8.1 现有链路回顾（摸头 / 戳脸）

- 摸头：`main/boards/desktop-pet/touch.cc`
  - `pet_on_pat();`
  - `Application::GetInstance().TriggerPetInteraction("摸头");`
- 戳脸：`main/boards/desktop-pet/ui/ui_pet.cc`
  - `pet_on_poke();`
  - `Application::GetInstance().TriggerPetInteraction("戳脸");`
- 上云实现：`main/application.cc` 中：
  - `Application::TriggerPetInteraction(const std::string& text)` 在 Idle 状态下会：\n
    - 打开音频通道\n
    - 在 Listening 状态通过 `protocol_->SendWakeWordDetected(text)` 把 `text` 发送到云端

### 8.2 商店购买触发规则

- 触发位置：`main/boards/desktop-pet/ui/ui_shop.cc` 中 `shop_buy_and_feed(FoodId id)` 的成功分支
- 条件：
  - 金币足够 → 扣除金币 → `pet_feed(id)` → **先切到 Idle，再触发上云文本**
  - 金币不足 / 非法 id → 不触发上云
- 文本映射（与食物一一对应）：
  - `FOOD_APPLE`      → `"投喂苹果"`
  - `FOOD_BANANA`     → `"投喂香蕉"`
  - `FOOD_CHIPS`      → `"投喂薯片"`
  - `FOOD_HONEY`      → `"投喂蜂蜜"`
  - `FOOD_STRAWBERRY` → `"投喂草莓"`

实现要点（当前版本）：购买成功后**直接切到 Idle 并立即触发一次上云交互**，不再使用 pending 文本或定时器重试。

```c
// 一次点击只购买一次；购买成功后直接切到 Idle 并触发一次上云交互
static void trigger_cloud_feed_once_click(const char *text) {
    if (!text || !text[0]) return;
    auto &app = Application::GetInstance();
    app.SetDeviceState(kDeviceStateIdle);
    app.TriggerPetInteraction(text);
}

// shop_buy_and_feed(FoodId id) 成功分支中：
trigger_cloud_feed_once_click(food_to_cloud_text(id));
```

这样云端能像识别“摸头”“戳脸”一样识别“投喂草莓”“投喂苹果”等动作；一次点击即完成购买并触发一次“投喂XXX”对话。


