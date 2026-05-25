# pet_page 播放 SD 卡 GIF 说明

## 目标

在 `desktop-pet` 板子的宠物首页（`pet_page`）中，循环播放放在 SD 卡根目录的 `neutral.gif`，并支持运行时切换不同表情 GIF。

---

## 涉及文件

| 文件 | 改动说明 |
|---|---|
| `main/boards/desktop-pet/ui/ui_pet.cc` | GIF 播放器完整实现 |
| `main/boards/desktop-pet/ui/ui_pet.h` | 新增 `pet_page_load_gif()` / `pet_page_switch_gif()` 接口声明 |
| `main/boards/desktop-pet/sd_card.cc` | SD 挂载成功后主动触发 GIF 加载；禁用自动格式化 |
| `managed_components/lvgl__lvgl/env_support/cmake/esp.cmake` | 补全 `fatfs` 组件依赖 |
| `sdkconfig`（menuconfig） | 开启 LVGL FatFS 文件系统，盘符设为 `S` |

---

## 名词说明

### VFS（Virtual File System，虚拟文件系统）

ESP-IDF 提供的抽象层，让代码用标准 C 接口（`fopen/fread/fclose`）访问不同存储介质，不需要关心底层是 SD 卡、Flash 还是其他设备。

```
你的代码
  fopen("/sdcard/neutral.gif")
       ↓
   VFS 层（ESP-IDF）        ← 根据路径前缀 "/sdcard" 找到对应驱动
       ↓
   FatFS 驱动               ← 实际操作 SD 卡硬件
```

SD 卡挂载时指定了挂载点 `/sdcard`，所以 SD 根目录的文件在 VFS 里都是 `/sdcard/文件名`。

### LVGL FatFS（`S:0:/...` 路径）

LVGL 自己的文件系统抽象，供 LVGL 内部（图片解码器、字体加载等）使用。路径格式为 `盘符:卷号:/文件名`。两者底层都走同一个 SD 卡，只是入口不同。

| | VFS（`/sdcard/...`） | LVGL FatFS（`S:0:/...`） |
|---|---|---|
| 接口 | 标准 C `fopen/fread` | LVGL 专有 `lv_fs_open` |
| 谁管 | ESP-IDF | LVGL |
| 用途 | 通用文件读写 | 供 LVGL 内部使用 |

---

## 实现原理

### 1. 为什么用 VFS 读到内存再解码（不用 `gd_open_gif_file`）

`gifdec` 支持两种打开方式：

- `gd_open_gif_file(path)`：通过 LVGL FatFS 打开，**每次 `gd_get_frame()` 都要对 SD 卡执行 seek + read**，帧率越高越卡
- `gd_open_gif_data(data)`：从内存 buffer 解码，**零 SD IO**，帧切换完全在内存里完成

因此采用的方案是：

```
一次性 fopen("/sdcard/neutral.gif")
  → fread 整个文件到 lv_malloc 分配的 PSRAM
  → fclose（文件关闭，SD IO 结束）
  → gd_open_gif_data(内存指针)
  → 之后每帧解码全走内存，不再碰 SD 卡
```

ESP32-S3 有 8MB PSRAM，普通表情 GIF（100KB～600KB）完全放得下。

### 2. 内存分配与释放

`lv_malloc` / `lv_free` 是 LVGL 封装的内存管理接口，在 ESP32-S3 上会优先从 PSRAM 分配。

- **VFS（`fopen/fread`）**：负责从 SD 卡读数据，本身不分配缓冲区
- **`lv_malloc`**：负责分配存放 GIF 数据的内存缓冲区
- **`lv_free`**：释放 `lv_malloc` 分配的那块内存

```cpp
// lv_malloc 分配 PSRAM ← 对应 lv_free 释放
s_gif.file_data = (uint8_t *)lv_malloc(sz);

// fread 把 SD 数据读进这块内存 ← VFS 只读，不分配
fread(s_gif.file_data, 1, sz, f);
fclose(f);  // 文件关闭，内存里的数据仍然存在

// 解码器从内存读帧（不再访问 SD 卡）
gd_open_gif_data(s_gif.file_data);
```

### 3. lv_timer 驱动播放

创建一个 `lv_timer`，初始间隔 100ms，加载成功后动态调整为当前帧的实际延时：

```cpp
// 每帧后更新 timer 间隔（GIF 允许逐帧指定不同延时）
uint32_t period = gif->gce.delay * 10;  // 1/100s → ms
lv_timer_set_period(timer, period);
```

`loop_count = 0` 表示 gifdec 在动画结尾自动 seek 回 `anim_start` 无限循环。

### 4. 切页面时暂停 timer

监听 LVGL 的屏幕事件，离开 `pet_page` 时暂停 timer，回来时恢复，避免在其他页面白白消耗 CPU：

```cpp
lv_obj_add_event_cb(obj, screen_event_cb, LV_EVENT_SCREEN_UNLOADED, nullptr); // 离开时暂停
lv_obj_add_event_cb(obj, screen_event_cb, LV_EVENT_SCREEN_LOADED,   nullptr); // 回来时恢复
lv_obj_add_event_cb(obj, screen_event_cb, LV_EVENT_DELETE,          nullptr); // 销毁时释放资源
```

### 5. LVGL FatFS 配置（仍需开启）

虽然播放时用 VFS 不走 LVGL FatFS，但工程其他模块（BMP 背景图等）仍依赖该配置，需要在 **menuconfig** 里开启：

```
Component config → LVGL configuration → 3rd Party Libraries
  [*] File system on top of FatFS
      Set an upper cased letter ... → 83   (ASCII 'S')
```

对应 `sdkconfig`：
```
CONFIG_LV_USE_FS_FATFS=y
CONFIG_LV_FS_FATFS_LETTER=83
CONFIG_LV_FS_FATFS_PATH=""
```

### 6. 补全 CMake 依赖

开启 `LV_USE_FS_FATFS` 后，LVGL 会编译 `lv_fs_fatfs.c`，它 `#include "ff.h"`，但 `lvgl__lvgl` 组件默认未声明对 `fatfs` 的依赖，导致编译报错：

```
lv_fs_fatfs.c: fatal error: ff.h: No such file or directory
```

修复：在 `managed_components/lvgl__lvgl/env_support/cmake/esp.cmake` 里补上 `fatfs`：

```cmake
# 修改前
REQUIRES esp_timer)

# 修改后
REQUIRES esp_timer fatfs)
```

> 修改后建议删除 `build/` 目录重新编译，让 CMake 重新计算组件依赖。

### 7. 初始化时序问题（关键）

`desktop_pet.cc` 的构造顺序是：

```
InitializeDisplay()   ←  内部调用 ui_init() → create_screen_pet_page()
    ↓
sd_card_init()        ←  SD 挂载（此时 UI 已经建完）
```

`create_screen_pet_page()` 被调用时 SD **尚未挂载**，首次 `fopen` 会返回 `errno=2`。

另外，工程里的 `uiTickTask`（`action.cc`）只调用了 `tick_app1()` / `tick_app2()`，**不调用 `ui_tick()`**，所以 `tick_screen_pet_page()` 里的定时重试逻辑永远不会被触发。

**解决方案**：在 `sd_card_init()` 挂载成功后主动调用一次 `pet_page_load_gif()`：

```c
// sd_card.cc
lvgl_port_lock(0);
pet_page_load_gif();    // 直接触发，不依赖 tick 轮询
lvgl_port_unlock();
```

### 8. 防止 SD 被自动格式化

`sd_card.cc` 中 `.format_if_mount_failed` 必须设为 **false**，否则 SD 挂载失败时会自动格式化，清空卡上所有文件：

```c
.format_if_mount_failed = false,  // 禁止自动格式化
```

---

## 公开接口

```c
// ui_pet.h

// SD 挂载成功后调用，加载并播放默认 GIF（/sdcard/neutral.gif）
// 需持有 LVGL 锁
void pet_page_load_gif();

// 切换播放指定 GIF，自动释放旧资源
// vfs_path 为 VFS 路径，如 "/sdcard/happy.gif"
// 需持有 LVGL 锁
void pet_page_switch_gif(const char *vfs_path);
```

### 切换表情示例

```cpp
// 在任意位置切换表情（需持有 LVGL 锁）
lvgl_port_lock(0);
pet_page_switch_gif("/sdcard/happy.gif");
lvgl_port_unlock();
```

SD 卡上准备对应文件即可：

```
SD卡根目录/
├── neutral.gif
├── happy.gif
├── sad.gif
└── angry.gif
```

---

## 内存估算（切换表情时）

每次只有一个 GIF 的数据在内存里，`pet_page_switch_gif` 会先释放旧的再加载新的：

| 项目 | 大小 |
|---|---|
| GIF 文件数据（典型） | 100 KB ～ 600 KB |
| gifdec 解码器（280×240） | ≈ 335 KB（canvas + frame buffer） |
| 合计 | ≈ 500 KB ～ 1 MB |

ESP32-S3 有 8MB PSRAM，远低于上限，不需要担心。

---

## 排查记录

| 现象 | 原因 | 解决 |
|---|---|---|
| 显示 `neutral.gif (SD loading...)` | SD 挂载前 UI 已初始化，tick 又没调，重试永远不触发 | `sd_card_init` 成功后主动调 `pet_page_load_gif()` |
| 显示 `neutral.gif (lvfs=12)` | `LV_FS_RES_UNKNOWN`，FatFS `f_open` 失败 | 降级到 VFS `/sdcard/neutral.gif` |
| 显示 `neutral.gif (lvfs=12 errno=2)` | `errno=2` = `ENOENT`，文件被自动格式化清空 | `format_if_mount_failed = false`，重新拷文件 |
| 编译报 `ff.h: No such file or directory` | `lvgl__lvgl` 组件未声明对 `fatfs` 的 CMake 依赖 | `esp.cmake` 的 `REQUIRES` 加上 `fatfs` |
| GIF 加载成功但画面不动 | cleanup 误删了 `lv_timer`，重试后 timer 消失 | 拆分 cleanup：只有页面销毁才删 timer |
| 动画卡顿 | timer 固定 10ms 空转 + 每帧走 SD IO | 改为内存解码 + timer 间隔跟随帧延时 |
| 切到其他页面仍占 CPU | timer 未暂停 | 监听 `LV_EVENT_SCREEN_UNLOADED` 暂停 timer |

---

## 关键代码位置速查

```
main/boards/desktop-pet/
├── ui/
│   ├── ui_pet.h     # pet_page_load_gif() / pet_page_switch_gif() 声明
│   └── ui_pet.cc    # GIF 播放器完整实现
└── sd_card.cc       # SD 挂载后调用 pet_page_load_gif()

main/display/lvgl_display/gif/
├── gifdec.h         # gd_open_gif_data / gd_get_frame / gd_render_frame
└── gifdec.c         # GIF 解码实现

managed_components/lvgl__lvgl/env_support/cmake/
└── esp.cmake        # REQUIRES esp_timer fatfs（已修改）
```
