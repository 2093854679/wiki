---
type: concept
aliases:
  - HTTP 文件上传任务
  - 嵌入式 HTTP 上传
---

# HTTP 文件上传任务

> **TLDR:** HTTP 文件上传任务把网络服务、表单解析、文件系统和 Flash 存储串起来，核心是流式接收、边界解析、容量检查和错误恢复。

## 关键链路

- HTTP Server 接收 `POST` 请求。
- 解析 `multipart/form-data` 的边界和文件字段。
- 分块写入 LittleFS/Flash，避免一次性占用大内存。
- 上传完成后校验大小、类型和存储结果。

## 易错点

- 一次性缓存整个文件导致内存不足。
- multipart 边界解析不完整。
- 上传中断后残留半文件。
- 文件系统容量、路径和权限没有检查。

## Related

- [[tcp-protocol-basics]]
- [[task-development-records]]
- [[embedded-coding-standards]]
- [[bk-armino-framework]]
