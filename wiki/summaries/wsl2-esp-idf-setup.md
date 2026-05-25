# WSL2 ESP-IDF 开发完整指南

> **Source:** [01-WSL2-ESP-IDF开发完整指南.md](../../raw/智能桌面萌宠项目笔记/doc/01-WSL2-ESP-IDF开发完整指南.md)
> **TLDR:** WSL2 下 ESP-IDF 开发环境的完整搭建指南——从 WSL/Ubuntu 安装、ESP-IDF 克隆与工具链配置、USB 设备映射（usbipd）、到 VS Code/Cursor 集成和编译烧录。

## Key Points

- WSL2 安装：`wsl --install -d Ubuntu`；确保 WSL 版本为 2
- ESP-IDF 安装：克隆仓库→`install.sh` 安装工具链→`. ./export.sh` 激活环境
- USB 设备映射（Windows→WSL2）：安装 usbipd→`usbipd bind -b <BUSID>`→`usbipd attach -w -b <BUSID>`→WSL 中 `ls /dev/ttyUSB*` 确认
- VS Code/Cursor 远程开发：安装 Remote-WSL 扩展→`code .` 打开项目
- 编译烧录：`idf.py set-target esp32s3`→`idf.py build`→`idf.py flash monitor`
- 常见问题：USB 权限（`sudo usermod -a -G dialout $USER`）、端口占用、工具链版本冲突
