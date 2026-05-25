## 目的

记录在 WSL + Cursor 环境下，为本项目配置 clangd，使 C/C++ 能够支持右键「跳转到定义」的步骤。

## 环境说明

- 操作系统：WSL2 / Ubuntu
- 编辑器：Cursor / VS Code 兼容
- 工程根目录：`xiaozhi-esp32`
- 已安装工具：`clangd` 14（`/usr/bin/clangd`）
- 工程已生成 `compile_commands.json`（在工程根目录）
- 工程根已有 `.clangd`：

```text
CompileFlags:
  CompilationDatabase: build
```

## 一、在系统中安装 clangd

如果尚未安装：

```bash
sudo apt update
sudo apt install -y clangd
clangd --version   # 确认有版本号输出
```

本项目中实际输出为：

```text
Ubuntu clangd version 14.0.0-1ubuntu1.1
Features: linux+grpc
Platform: x86_64-pc-linux-gnu
```

## 二、配置工程使用 clangd

### 1. 确认工程根目录

在 Cursor 中 **打开整个工程根目录**：

- 根目录应为：`xiaozhi-esp32`（包含 `main/`, `docs/`, `build/`, `compile_commands.json` 等）
- 不要只单独打开 `main/boards/desktop-pet/` 之类的子目录

### 2. 配置 `.clangd`

工程根目录已经有 `.clangd`，内容为：

```text
CompileFlags:
  CompilationDatabase: build
```

说明 clangd 会在 `build/` 目录下寻找 `compile_commands.json`，与 ESP-IDF 的默认生成路径一致。

如需从工程根目录直接使用根目录下的 `compile_commands.json`，可改为：

```text
CompileFlags:
  CompilationDatabasePath: .
```

> 当前项目已验证使用 `CompilationDatabase: build` 工作正常，无需修改。

### 3. 配置 `.vscode/settings.json`

在工程根目录下创建（或编辑） `.vscode/settings.json`，内容如下：

```json
{
  "clangd.path": "/usr/bin/clangd",
  "clangd.arguments": [
    "--compile-commands-dir=${workspaceFolder}"
  ]
}
```

含义：

- **clangd.path**：显式指定 clangd 可执行文件路径，防止 Cursor/VS Code 在 Windows 路径下找不到。
- **clangd.arguments**：告诉 clangd 编译数据库的位置为当前工作区根目录（`${workspaceFolder}`）。

> 如果将来 `compile_commands.json` 只放在 `build/` 目录下，可以把参数改为 `--compile-commands-dir=${workspaceFolder}/build`。

## 三、编辑器侧操作

### 1. 安装/启用 clangd 扩展

在 Cursor / VS Code 中：

1. 打开 **Extensions**（扩展）视图；
2. 搜索并安装官方 **clangd** 扩展（提供 C/C++ 语言服务器功能）；
3. 如已安装微软 `C/C++` 扩展，建议先禁用它，避免与 clangd 抢占语言服务。

### 2. 重启语言服务器和窗口

在命令面板（`Ctrl+Shift+P`）依次执行：

1. `Clangd: Restart language server`（如果命令存在）；
2. `Developer: Reload Window`（重载窗口）。

等待右下角状态栏中 clangd 初始化和索引完成。

## 四、验证右键跳转

1. 打开 `main/boards/desktop-pet/CJ_display.cc`；
2. 将光标放在以下符号上任意一个，例如：
   - `CJDisplay`
   - `CJ_SpiLcdDisplay`
   - 某个成员函数名
3. 使用以下任一方式：
   - 右键 → **Go to Definition / 跳转到定义**
   - `F12`
   - `Ctrl + 左键`（在符号上）

如果能正确跳转到对应的头文件或实现文件（如 `CJ_display.h`），则说明 clangd 语言服务和编译数据库已正常工作。

## 五、常见问题与排查

- **提示 “The clangd language server is not installed”**
  - 原因：扩展找不到可执行文件；
  - 解决：确认 `/usr/bin/clangd` 存在，并在 `.vscode/settings.json` 中设置 `"clangd.path": "/usr/bin/clangd"`。

- **右键仍然无法跳转，但无报错**
  - 检查当前是否打开工程根目录，而不是子目录；
  - 确认根目录存在 `compile_commands.json` 或 `build/compile_commands.json`；
  - 在命令面板中重新执行 `Clangd: Restart language server` 和 `Developer: Reload Window`。

- **新改动后跳转位置不对或不更新**
  - 重新执行一次项目构建命令（如 `idf.py build`），让 `compile_commands.json` 更新；
  - 重启 clangd 语言服务器。

## 六、小结

本项目启用右键跳转的关键点：

- **系统层面**：安装并确认 `/usr/bin/clangd` 可用；
- **工程层面**：有正确的 `compile_commands.json` 和 `.clangd`；
- **编辑器层面**：在 `.vscode/settings.json` 中配置 `clangd.path` 与 `clangd.arguments`，并安装/启用 clangd 扩展；
- **最后**：重启语言服务器和窗口，验证在 `CJ_display.cc` 等文件中能正常跳转到定义。

