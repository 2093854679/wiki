# Git使用指南

## 目录

- [1. Git工作流程与项目开发规范](#1-git工作流程与项目开发规范)
  - [1.1 Git仓库管理](#11-git仓库管理)
  - [1.2 开发工作流程](#12-开发工作流程)
- [2. 重要Git命令](#2-重要git命令)
  - [2.1 基础操作](#21-基础操作)
  - [2.2 提交操作](#22-提交操作)
  - [2.3 合并操作](#23-合并操作)
- [3. 常见问题解决](#3-常见问题解决)
- [4. 代码提交规范](#4-代码提交规范)
- [5. 实用Git技巧](#5-实用git技巧)
  - [5.1 查看文件修改历史](#51-查看文件修改历史)
  - [5.2 撤销操作](#52-撤销操作)
  - [5.3 查看差异](#53-查看差异)
  - [5.4 标签管理](#54-标签管理)
  - [5.5 暂存修改](#55-暂存修改)
- [6. 最佳实践](#6-最佳实践)

## 1. Git工作流程与项目开发规范

### 1.1 Git仓库管理

#### 仓库结构

```
远程仓库：https://gitlab.bekencorp.com/armino/release_sdk_sample/bk_idk/bk_idk_bk7236.git
主分支：release/v2.0.2
个人开发分支：guohang-task（基于主分支创建）
```

#### 分支策略

- **主分支**：`release/v2.0.2` - 稳定版本，只接受通过Merge Request的代码
- **开发分支**：`guohang-task` - 个人功能开发分支
- **功能分支**：`feature/xxx` - 特定功能开发分支（可选）

### 1.2 开发工作流程

#### 1. 初始化本地仓库

```bash
# 克隆远程仓库
git clone https://gitlab.bekencorp.com/armino/release_sdk_sample/bk_idk/bk_idk_bk7236.git
cd bk_idk_bk7236

# 切换到主分支
git checkout release/v2.0.2

# 创建个人开发分支
git checkout -b guohang-task

# 推送个人分支到远程
git push -u origin guohang-task
```

#### 2. 日常开发流程

```bash
# 确保在个人开发分支上
git branch
# 应该显示：* guohang-task

# 开发代码...

# 提交更改
git add .
git commit -m "feat: 添加WiFi扫描线程安全功能"

# 推送到远程个人分支
git push origin guohang-task
```

#### 3. 完成功能开发后合并

```bash
# 1. 确保所有更改已提交并推送
git status
git push origin guohang-task

# 2. 在GitLab上创建Merge Request
# 访问：https://gitlab.bekencorp.com/armino/release_sdk_sample/bk_idk/bk_idk_bk7236
# 点击 "New Merge Request"
# Source branch: guohang-task
# Target branch: release/v2.0.2

# 3. 等待代码审查和合并
```

## 2. 重要Git命令

### 2.1 基础操作

```bash
# 查看状态
git status

# 查看分支
git branch

# 切换分支
git checkout <branch_name>

# 创建并切换分支
git checkout -b <new_branch_name>

# 查看提交历史
git log --oneline
```

### 2.2 提交操作

```bash
# 添加文件到暂存区
git add <file_name>
git add .  # 添加所有更改

# 提交更改
git commit -m "描述性提交信息"

# 推送到远程
git push origin <branch_name>

# 拉取远程更新
git pull origin <branch_name>
```

### 2.3 合并操作

```bash
# 合并主分支到开发分支（保持同步）
git checkout guohang-task
git pull origin release/v2.0.2

# 如果有冲突，解决后提交
git add .
git commit -m "merge: 解决合并冲突"
git push origin guohang-task
```

## 3. 常见问题解决

### 3.1 推送被拒绝

```bash
# 错误：Updates were rejected because the remote contains work that you do not have locally
# 解决：先拉取远程更新
git pull origin <branch_name>
# 如果有冲突，解决后重新推送
git push origin <branch_name>
```

### 3.2 合并无关历史

```bash
# 错误：fatal: refusing to merge unrelated histories
# 解决：允许合并无关历史
git pull origin <branch_name> --allow-unrelated-histories
```

### 3.3 退出合并状态

```bash
# 如果卡在MERGING状态
git merge --abort  # 取消合并
# 或者
git commit  # 完成合并
```

## 4. 代码提交规范

### 4.1 提交信息格式

```bash
# 格式：<type>: <description>
git commit -m "feat: 添加WiFi扫描线程安全功能"
git commit -m "fix: 修复页面自动刷新问题"
git commit -m "docs: 更新API文档"
git commit -m "refactor: 重构HTTP服务器代码"
```

### 4.2 提交类型说明

- `feat`: 新功能
- `fix`: 修复bug
- `docs`: 文档更新
- `style`: 代码格式调整
- `refactor`: 代码重构
- `test`: 测试相关
- `chore`: 构建过程或辅助工具的变动

## 5. 实用Git技巧

### 5.1 查看文件修改历史

```bash
# 查看文件的修改历史
git log --follow <file_name>

# 查看文件的详细修改内容
git log -p <file_name>

# 查看文件的修改统计
git log --stat <file_name>
```

### 5.2 撤销操作

```bash
# 撤销工作区的修改
git checkout -- <file_name>

# 撤销暂存区的修改
git reset HEAD <file_name>

# 撤销最近一次提交（保留修改）
git reset --soft HEAD~1

# 撤销最近一次提交（不保留修改）
git reset --hard HEAD~1
```

### 5.3 查看差异

```bash
# 查看工作区与暂存区的差异
git diff

# 查看暂存区与最新提交的差异
git diff --cached

# 查看工作区与最新提交的差异
git diff HEAD

# 查看两个提交之间的差异
git diff <commit1> <commit2>
```

### 5.4 标签管理

```bash
# 创建标签
git tag -a v1.0.0 -m "版本1.0.0"

# 查看所有标签
git tag

# 推送标签到远程
git push origin v1.0.0

# 推送所有标签
git push origin --tags
```

### 5.5 暂存修改

```bash
# 暂存当前修改
git stash

# 查看暂存列表
git stash list

# 恢复暂存的修改
git stash pop

# 应用暂存的修改（不删除）
git stash apply
```

## 6. 最佳实践

### 6.1 提交频率
- 功能开发完成后及时提交
- 每次提交只包含一个逻辑变更
- 提交信息要清晰明确

### 6.2 分支管理
- 保持主分支的稳定性
- 及时合并主分支的更新
- 功能开发完成后及时合并

### 6.3 代码审查
- 通过Merge Request进行代码审查
- 审查通过后再合并到主分支
- 保持代码质量和一致性