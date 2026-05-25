## 目标

把 `startnorva` 的 `app1_page`（时钟页）背景从固件内置的 `img_picture`，改为 **从 SD 卡读取** `clock/1.bmp` 并在 LVGL 上显示。

已知条件：
- SD 卡已通过 `esp_vfs_fat_sdmmc_mount()` 挂载到 `"/sdcard"`。
- BMP 图片为 **16 位**（RGB565）。

---

## 实现原理（一句话）

**启用 LVGL 的 FatFS 文件系统驱动 + BMP 解码器**，然后在 SD 挂载成功后调用 `lv_img_set_src()` 把图片源切到 SD 卡路径（`S:0:/clock/1.bmp`）。

---

## 1）menuconfig 改了什么（必须）

路径：`Component config -> LVGL configuration -> 3rd Party Libraries`

### 打开 BMP 解码器

- `[ * ] BMP decoder library`

作用：让 LVGL 能识别并解码 `.bmp` 文件（否则只能当普通文件读，不能显示）。

### 打开 FatFS 文件系统接口

- `[ * ] File system on top of FatFS`
- `Set an upper cased letter ...` 设为 **83**（ASCII 的 `'S'`）
- `cache` 保持 `0`（可选优化项，先不需要）

作用：让 LVGL 可以通过 `S:...` 这种“盘符路径”打开文件；盘符用 `S` 只是约定，便于识别（不必须是 S）。

> 备注：BMP 图片建议使用 16/24/32 bpp（本次为 16 位 RGB565）。

---

## 2）代码改了什么（按文件列出）

### A. `main/boards/startnorva/ui/screens.h`

给 `objects_t` 增加一个指针字段，用来保存“时钟页背景的 lv_img 对象”：

- 新增：`lv_obj_t *app1_bg_img;`

目的：后续 SD 挂载成功后，需要拿到这个对象，才能对它 `lv_img_set_src()` 改成 SD 图片。

### B. `main/boards/startnorva/ui/screens.c`

在 `create_screen_app1_page()` 创建背景图时，把背景 `lv_img` 对象保存到 `objects.app1_bg_img`：

- 新增：`objects.app1_bg_img = obj;`
- 保留：`lv_img_set_src(obj, &img_picture);`

为什么保留 `img_picture`？

- **启动时序原因**：`ui_init()` 会先跑，`sd_card_init()` 后跑。启动早期 SD 可能还没挂载成功。
- 先用内置图兜底，等 SD 挂载后再切换成 SD BMP；如果 SD 失败也不会空白。

### C. `main/boards/startnorva/sd_card.cc`

在 `sd_card_init()` 挂载成功后切换背景到 SD BMP：

- 在 `sd_card_mounted = true;` 后增加：
  - `lvgl_port_lock(0);`
  - `lv_img_set_src(objects.app1_bg_img, "S:0:/clock/1.bmp");`
  - `lvgl_port_unlock();`
  - 日志：`Clock background switched ...`

关键点：使用路径 **`S:0:/clock/1.bmp`**

- LVGL 的 FatFS 驱动会先解析掉盘符字母（`S`），再把后面的 path 交给 FatFs。
- 这样传给 FatFs 的实际路径是：`0:/clock/1.bmp`（明确卷号 0），避免依赖“当前盘”。

---

## 3）遇到的报错与解决方案

### 报错 1：`lv_fs_fatfs.c: fatal error: ff.h: No such file or directory`

现象：

- 启用 `LV_USE_FS_FATFS` 后，LVGL 会编译 `lv_fs_fatfs.c`，它 `#include "ff.h"`。
- 但编译命令里没有 fatfs 的 include 目录，导致找不到 `ff.h`。

原因：

- `managed_components/lvgl__lvgl` 在 ESP-IDF 的 `idf_component_register(...)` 中未声明对 `fatfs` 的依赖（`REQUIRES`）。
- 所以即使工程里有 `fatfs` 组件，`lvgl__lvgl` 组件本身也拿不到 `ff.h` 的头文件路径。

解决：

- 修改 `managed_components/lvgl__lvgl/env_support/cmake/esp.cmake`
- 强制把 `fatfs` 加到 `REQUIRES` 里（同时保留 `esp_timer`）：
  - `REQUIRES esp_timer fatfs`

注意：

- 改完依赖后，建议 **删除 `build/` 目录重新生成**（让 CMake 重新计算组件依赖），再 `idf.py build`。

### 报错 2：链接错误 `undefined reference to f_chdrive`

现象：

- 最初尝试在挂载成功后调用 `f_chdrive("0:")`，链接阶段报 `undefined reference to f_chdrive`。

原因：

- ESP-IDF 的 FatFs 配置/裁剪选项不同，有些环境不提供 `f_chdrive()` 符号（被裁剪或未启用相关 API）。

解决（最终采用）：

- **不再调用 `f_chdrive()`**
- 直接把卷号写进 FatFs 路径：`0:/clock/1.bmp`
- 因为 LVGL 会剥离 `S`，所以写成：`S:0:/clock/1.bmp`

---

## 4）最终使用方式/验证方法

### SD 卡文件位置

- SD 卡里放：`/clock/1.bmp`

### 运行时行为

- 启动时：先显示内置背景 `img_picture`
- SD 挂载成功后：自动切换到 SD 背景 BMP

### 串口日志关键字（排查用）

- `Initializing SD card`
- `Filesystem mounted`
- `Clock background switched to SD: S:0:/clock/1.bmp`

如果没切换成功：

- 先确认 SD 挂载成功（否则不会切）
- 确认 BMP 为 16/24/32 bpp，且文件名后缀 `.bmp`
- 确认 `objects.app1_bg_img` 非空（screens 初始化要先跑完）
