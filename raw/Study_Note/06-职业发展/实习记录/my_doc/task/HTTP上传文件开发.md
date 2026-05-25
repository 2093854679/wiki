# HTTP上传文件开发

## 任务目标
- 使用文件系统Littlefs，将文件上传到http服务器。

## 参考例程
- projects/examples/peripherals（文件系统、HTTP相关）

## 开发计划
- [ ] 方案设计与流程图
- [ ] Littlefs文件系统操作
- [ ] HTTP上传流程实现
- [ ] 大文件与断点续传测试（如有需求）

## 问题记录
-

## 代码区
```c
// 代码片段可在此补充
```

---

## Littlefs与HTTP文件上传实现细节

### 1. Littlefs文件系统操作

```c
#include "lfs.h"
lfs_t lfs;
lfs_file_t file;

// 挂载文件系统
lfs_mount(&lfs, &cfg);

// 写文件
lfs_file_open(&lfs, &file, "test.txt", LFS_O_WRONLY | LFS_O_CREAT);
lfs_file_write(&lfs, &file, "hello", 5);
lfs_file_close(&lfs, &file);

// 读文件
lfs_file_open(&lfs, &file, "test.txt", LFS_O_RDONLY);
char buf[16];
lfs_file_read(&lfs, &file, buf, sizeof(buf));
lfs_file_close(&lfs, &file);
```

---

### 2. HTTP文件上传流程

- 推荐用lwIP httpd或第三方HTTP库实现文件上传接口。
- 典型流程：网页表单POST文件到设备，设备解析HTTP body并写入Littlefs。

```c
// HTTP POST回调伪代码
void httpd_post_receive_data(void *connection, struct pbuf *p) {
    // 假设p->payload为文件内容
    lfs_file_open(&lfs, &file, "upload.bin", LFS_O_WRONLY | LFS_O_CREAT);
    lfs_file_write(&lfs, &file, p->payload, p->len);
    lfs_file_close(&lfs, &file);
}
```

---

### 3. 网页上传表单示例

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>文件上传</title>
</head>
<body>
    <h2>上传文件到设备</h2>
    <form action="/upload" method="post" enctype="multipart/form-data">
        选择文件: <input type="file" name="file"><br>
        <input type="submit" value="上传">
    </form>
</body>
</html>
```

- 用户通过网页选择文件并上传，设备端解析HTTP POST数据并保存到Littlefs。

---

### 4. 关键点说明
- **大文件处理**：建议分块写入，防止内存溢出。
- **文件名安全**：校验文件名，防止路径遍历攻击。
- **上传进度**：可在网页端显示进度条，提升用户体验。

---

### 5. 参考资料
- [Littlefs官方文档](https://github.com/littlefs-project/littlefs)
- [lwIP httpd官方文档](https://www.nongnu.org/lwip/2_1_x/group__httpd.html)
- BK7236 SDK文件系统与HTTP例程
