# Emoji 心情 GIF 动态切换

## 目标

当 LLM 返回 emotion 字段时，pet 页面自动切换到对应的 GIF 动画。例如 LLM 返回 `"emotion": "happy"`，pet 页面就从当前 GIF 切换到 `/sdcard/gif/happy.gif` 播放。如果文件不存在，回退到 `love.gif`。

---

## 背景：LLM Emotion 消息格式

服务端返回的 JSON：

```json
{
    "type": "llm",
    "text": "😊",
    "emotion": "happy"
}
```

`emotion` 字段是一个英文字符串，对应 21 种心情之一。`text` 是 Emoji 字符（TTS 不朗读），客户端根据 `emotion` 来驱动 UI。

---

## 整体数据流

```
服务端 JSON
  │
  ▼
application.cc  ─── 解析 "llm" 类型消息，提取 emotion 字段
  │
  │  display->SetEmotion("happy")
  ▼
CJ_display.cc::SetEmotion()
  │
  ├── ① 更新聊天状态栏的 Emoji label（🙂）
  │
  └── ② pet_page_set_emotion("happy")  ← 新增
        │
        ▼
      ui_pet.cc::pet_page_set_emotion()
        │
        ├── emotion_to_filename("happy")  → "happy.gif"
        ├── 拼接路径 → "/sdcard/gif/happy.gif"
        ├── file_exists() 检查文件是否存在
        │     ├── 存在 → 使用该路径
        │     └── 不存在 → 回退到 "/sdcard/gif/love.gif"
        │
        └── pet_page_switch_gif("/sdcard/gif/happy.gif")
              │
              ├── 释放旧 GIF 解码器和内存数据
              ├── 从 SD 卡读新 GIF 到内存
              ├── 创建新解码器
              └── 恢复 lv_timer 播放
```

---

## 涉及文件

| 文件 | 改动说明 |
|---|---|
| `main/boards/desktop-pet/ui/ui_pet.h` | 新增 `pet_page_set_emotion()` 接口声明 |
| `main/boards/desktop-pet/ui/ui_pet.cc` | 实现 emotion→GIF 映射、文件存在性检查、回退逻辑 |
| `main/boards/desktop-pet/CJ_display.cc` | `SetEmotion()` 中新增调用 `pet_page_set_emotion()` |
| `sd/gif/*.gif` | SD 卡上的 21 个表情 GIF 文件 |

---

## 代码详解

### 1. 入口：`application.cc` 分发 emotion

```cpp
// application.cc（已有代码，不需要修改）
} else if (strcmp(type->valuestring, "llm") == 0) {
    auto emotion = cJSON_GetObjectItem(root, "emotion");
    if (cJSON_IsString(emotion)) {
        Schedule([display, emotion_str = std::string(emotion->valuestring)]() {
            display->SetEmotion(emotion_str.c_str());
        });
    }
}
```

**解读**：
- 收到 WebSocket 消息后，`cJSON` 解析 JSON
- 如果 `type == "llm"` 且存在 `emotion` 字段，就调度到主线程执行 `display->SetEmotion()`
- `Schedule()` 确保在 LVGL 线程安全的上下文中执行

### 2. `CJDisplay::SetEmotion()` — 双重更新

```cpp
// CJ_display.cc
void CJDisplay::SetEmotion(const char* emotion) {
    // ... 查表找到对应 Emoji 图标 ...

    DisplayLockGuard lock(this);  // 获取 LVGL 锁

    // ① 更新聊天状态栏的 Emoji label
    lv_obj_set_style_text_font(emotion_label_, emoji_font_, 0);
    lv_label_set_text(emotion_label_, it->icon);  // 如 "🙂"

    // ② 同步切换 pet 页面的 GIF 动画（新增）
    pet_page_set_emotion(emotion);
}
```

**解读**：
- `DisplayLockGuard` 是 RAII 风格的 LVGL 锁，构造时 `lock`，析构时 `unlock`
- 先更新聊天栏 emoji（原有功能），再切换 pet 页 GIF（新增功能）
- 两步操作在同一把锁内完成，保证线程安全

### 3. `emotion_to_filename()` — 名称映射

```cpp
// ui_pet.cc
static const char *emotion_to_filename(const char *emotion) {
    if (!emotion || !emotion[0]) return "neutral.gif";

    struct Map { const char *emotion; const char *filename; };
    static const Map special[] = {
        { "loving",  "love.gif" },
        { "kissy",   "kiss.gif" },
    };
    for (const auto &m : special) {
        if (strcmp(emotion, m.emotion) == 0) return m.filename;
    }

    static char buf[48];
    snprintf(buf, sizeof(buf), "%s.gif", emotion);
    return buf;
}
```

**解读**：
- 大部分 emotion 直接加 `.gif` 后缀即可（如 `"happy"` → `"happy.gif"`）
- 两个特殊映射：`"loving"` → `"love.gif"`，`"kissy"` → `"kiss.gif"`（因为 GIF 文件名和 emotion 字符串不完全一致）
- 空字符串或 `NULL` 回退到 `"neutral.gif"`
- `static char buf[48]` 是静态缓冲区，避免动态分配，但注意**非线程安全**（在 LVGL 锁内调用所以没问题）

### 4. `file_exists()` — 轻量级文件检查

```cpp
static bool file_exists(const char *path) {
    FILE *f = fopen(path, "rb");
    if (f) { fclose(f); return true; }
    return false;
}
```

**解读**：
- 用标准 C 的 `fopen` 尝试打开文件
- 能打开就说明文件存在，立即 `fclose` 不读任何数据
- 比 `stat()` 更简单，在 ESP-IDF VFS 上兼容性好

### 5. `pet_page_set_emotion()` — 核心入口

```cpp
static constexpr const char *kGifDir     = "/sdcard/gif/";
static constexpr const char *kFallbackGif = "/sdcard/gif/love.gif";

void pet_page_set_emotion(const char *emotion) {
    const char *filename = emotion_to_filename(emotion);

    char path[80];
    snprintf(path, sizeof(path), "%s%s", kGifDir, filename);

    ESP_LOGI(TAG, "emotion=%s → %s", emotion ? emotion : "(null)", path);

    if (!file_exists(path)) {
        ESP_LOGW(TAG, "%s not found, fallback to love.gif", path);
        snprintf(path, sizeof(path), "%s", kFallbackGif);
    }

    pet_page_switch_gif(path);
}
```

**解读**：
1. 调用 `emotion_to_filename()` 得到文件名
2. 拼接完整路径：`/sdcard/gif/` + `happy.gif` = `/sdcard/gif/happy.gif`
3. 检查文件是否存在，不存在则回退到 `/sdcard/gif/love.gif`
4. 调用已有的 `pet_page_switch_gif()` 完成实际切换

### 6. `pet_page_switch_gif()` — 已有的 GIF 切换器

```cpp
void pet_page_switch_gif(const char *vfs_path) {
    // 1. 释放旧解码器
    close_decoder();
    // 2. 释放旧文件内存
    lv_free(s_gif.file_data);
    // 3. 暂停 timer
    lv_timer_pause(s_gif.timer);
    // 4. 从 SD 读新 GIF 到内存 + 创建解码器
    load_file_to_ram(vfs_path) && open_decoder_from_data();
    // 5. 恢复 timer
    lv_timer_resume(s_gif.timer);
}
```

**解读**（简化伪代码）：
- 每次切换都是 **释放旧 → 加载新** 的完整流程
- 内存中始终只保留一份 GIF 数据，不会累积

---

## Emotion → GIF 对照表

| Emotion 字符串 | Emoji | GIF 文件名 | SD 卡路径 |
|---|---|---|---|
| `neutral` | 😶 | `neutral.gif` | `/sdcard/gif/neutral.gif` |
| `happy` | 🙂 | `happy.gif` | `/sdcard/gif/happy.gif` |
| `laughing` | 😆 | `laughing.gif` | `/sdcard/gif/laughing.gif` |
| `funny` | 😂 | `funny.gif` | `/sdcard/gif/funny.gif` |
| `sad` | 😔 | `sad.gif` | `/sdcard/gif/sad.gif` |
| `angry` | 😠 | `angry.gif` | `/sdcard/gif/angry.gif` |
| `crying` | 😭 | `crying.gif` | `/sdcard/gif/crying.gif` |
| `loving` | 😍 | **`love.gif`** | `/sdcard/gif/love.gif` |
| `embarrassed` | 😳 | `embarrassed.gif` | `/sdcard/gif/embarrassed.gif` |
| `surprised` | 😲 | `surprised.gif` | `/sdcard/gif/surprised.gif` |
| `shocked` | 😱 | `shocked.gif` | `/sdcard/gif/shocked.gif` |
| `thinking` | 🤔 | `thinking.gif` | `/sdcard/gif/thinking.gif` |
| `winking` | 😉 | `winking.gif` | `/sdcard/gif/winking.gif` |
| `cool` | 😎 | `cool.gif` | `/sdcard/gif/cool.gif` |
| `relaxed` | 😌 | `relaxed.gif` | `/sdcard/gif/relaxed.gif` |
| `delicious` | 🤤 | `delicious.gif` | `/sdcard/gif/delicious.gif` |
| `kissy` | 😘 | **`kiss.gif`** | `/sdcard/gif/kiss.gif` |
| `confident` | 😏 | `confident.gif` | `/sdcard/gif/confident.gif` |
| `sleepy` | 😴 | `sleepy.gif` | `/sdcard/gif/sleepy.gif` |
| `silly` | 😜 | `silly.gif` | `/sdcard/gif/silly.gif` |
| `confused` | 🙄 | `confused.gif` | `/sdcard/gif/confused.gif` |

> 注意加粗的两行：`loving` → `love.gif`，`kissy` → `kiss.gif`，文件名和 emotion 字符串不同。

---

## SD 卡目录结构

```
SD 卡根目录/
└── gif/
    ├── neutral.gif       ← 默认表情（开机加载）
    ├── happy.gif
    ├── sad.gif
    ├── angry.gif
    ├── love.gif          ← 回退表情 + "loving" 对应
    ├── kiss.gif          ← "kissy" 对应
    ├── laughing.gif
    ├── funny.gif
    ├── crying.gif
    ├── embarrassed.gif
    ├── surprised.gif
    ├── shocked.gif
    ├── thinking.gif
    ├── winking.gif
    ├── cool.gif
    ├── relaxed.gif
    ├── delicious.gif
    ├── confident.gif
    ├── sleepy.gif
    ├── silly.gif
    └── confused.gif
```

---

## 关键设计决策

### 为什么用 `file_exists()` 而不是提前加载到内存？

`pet_page_switch_gif()` 内部会先释放旧的 `file_data`，再调用 `load_file_to_ram()` 读取新文件。如果在外面先调用 `load_file_to_ram()` 预检查，数据会被缓存到 `s_gif.file_data`，随后 `pet_page_switch_gif()` 又把它释放掉，造成不必要的 IO 浪费。

所以用一个轻量的 `fopen` + `fclose` 只检查存在性，不读数据。

### 为什么回退到 `love.gif` 而不是 `neutral.gif`？

这是产品设计选择。`neutral` 是默认的平静状态（开机就播放），当 LLM 发来一个未知 emotion 时，说明它在表达某种情绪，用 `love.gif`（喜爱）作为通用的正面情绪回退比冷淡的 `neutral` 更合适。

### `static char buf[48]` 的线程安全问题

`emotion_to_filename()` 内部用了一个 `static` 缓冲区来拼接文件名。这意味着：

- **同一时刻只能有一个调用者**使用返回值
- 当前调用链：`SetEmotion()` → `pet_page_set_emotion()` → `emotion_to_filename()`，全程在 `DisplayLockGuard` 锁内，不会并发，所以是安全的
- 如果未来要在锁外调用，需要改成传入外部缓冲区

---

## 调试技巧

### 查看 emotion 切换日志

```bash
idf.py monitor
```

正常切换时会看到：

```
I (12345) ui_pet: emotion=happy → /sdcard/gif/happy.gif
I (12346) ui_pet: gif loaded to RAM: /sdcard/gif/happy.gif (100689 bytes)
I (12347) ui_pet: gif ready: 280x240
I (12348) ui_pet: switched to: /sdcard/gif/happy.gif
```

文件不存在时的回退：

```
I (12345) ui_pet: emotion=unknown → /sdcard/gif/unknown.gif
W (12346) ui_pet: /sdcard/gif/unknown.gif not found, fallback to love.gif
I (12347) ui_pet: gif loaded to RAM: /sdcard/gif/love.gif (96039 bytes)
```

### 手动测试切换

在代码中临时插入测试代码：

```cpp
// 在 sd_card.cc 的 SD 挂载成功后
lvgl_port_lock(0);
pet_page_set_emotion("happy");    // 测试 happy
// pet_page_set_emotion("loving");   // 测试特殊映射
// pet_page_set_emotion("xxx");      // 测试回退
lvgl_port_unlock();
```

---

## 关键代码位置速查

```
main/boards/desktop-pet/
├── CJ_display.cc       # SetEmotion() — emotion 分发入口
├── CJ_display.h        # CJDisplay 类声明
└── ui/
    ├── ui_pet.h         # pet_page_set_emotion() 声明
    └── ui_pet.cc        # emotion→GIF 映射 + 回退逻辑

sd/gif/                  # SD 卡表情 GIF 文件（烧录到 SD 卡）
    ├── neutral.gif
    ├── happy.gif
    └── ...

main/application.cc      # LLM 消息解析，调用 display->SetEmotion()
```
