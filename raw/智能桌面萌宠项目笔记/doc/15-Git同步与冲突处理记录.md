## Git 同步与冲突处理记录（xiaozhi-esp32-main-v2）

本文件记录本次在 `xiaozhi-esp32-main-v2/xiaozhi-esp32` 仓库中遇到的 Git 同步问题和解决过程，方便以后遇到类似情况时快速处理。

---

### 1. 情况一：`git push` 被拒绝（non-fast-forward）

**报错示例：**

```text
git push
To gitee.com:hghhhh/xiaozhi_v2.git
 ! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'gitee.com:hghhhh/xiaozhi_v2.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
```

**原因：**

- 远端 `origin/main` 上已经有新的提交，本地 `main` 也有新的提交，两边历史不在同一条线上，直接 `push` 会覆盖远端，所以被拒绝。

**解决步骤：**

1. **先把本地改动保存好**（二选一）：
   - 直接提交：

     ```bash
     git add .
     git commit -m "你的提交说明"
     ```

   - 或者暂存：

     ```bash
     git stash
     ```

2. **拉取远端并 rebase：**

   ```bash
   git pull --rebase origin main
   ```

3. 若无冲突，执行：

   ```bash
   git push
   ```

---

### 2. 情况二：`git pull` 需要指定 merge / rebase 策略

**报错示例：**

```text
git pull
hint: You have divergent branches and need to specify how to reconcile them.
...
fatal: Need to specify how to reconcile divergent branches.
```

**含义：**

- 本地和远端已经“各自多出提交”（divergent branches），Git 需要你明确：**拉取时是用 merge 还是 rebase**。

**处理方式：**

- 不改全局配置的情况下，直接在命令行带上参数，例如：

  ```bash
  git pull --rebase origin main       # 使用 rebase（本次采用）
  # 或
  git pull --no-rebase origin main    # 使用 merge
  ```

---

### 3. 情况三：`git pull --rebase` 提示有未暂存改动

**报错示例：**

```text
git pull --rebase origin main
error: cannot pull with rebase: You have unstaged changes.
error: please commit or stash them.
```

**解决方法：**

1. 确认当前改动（`git status`）。
2. 要么提交，要么暂存：

   ```bash
   git add .
   git commit -m "save work before rebase"
   # 或
   git stash
   ```

3. 再执行：

   ```bash
   git pull --rebase origin main
   ```

---

### 4. 情况四：rebase 过程中二进制 GIF 资源冲突（add/add）

**报错示例：**

```text
warning: Cannot merge binary files: sd/xiaoxiong/winking.gif (HEAD vs. 4192f3c (fix:fix git err))
...
CONFLICT (add/add): Merge conflict in sd/xiaoxiong/angry.gif
...
error: could not apply 4192f3c... fix:fix git err
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
```

**原因：**

- 同一个 GIF 文件在本地和远端都以“新增文件”的形式存在（`add/add`），Git 无法自动决定保哪一边。

**选择：**

- **保留本地 GIF**（本次采用）：

  ```bash
  git checkout --ours sd/xiaoxiong/*.gif
  git add sd/xiaoxiong/*.gif
  git rebase --continue
  ```

- **保留远端 GIF**（如确实远端才是最新）：

  ```bash
  git checkout --theirs sd/xiaoxiong/*.gif
  git add sd/xiaoxiong/*.gif
  git rebase --continue
  ```

如果 rebase 过程中有更多冲突，重复“解决冲突 → `git add` → `git rebase --continue`”的循环，直到完成。

若过程中出错想回到 rebase 前的状态，可以使用：

```bash
git rebase --abort
```

---

### 5. 情况五：rebase 进入编辑提交信息（nano）

在执行 `git rebase --continue` 时，Git 会打开编辑器（当前为 `nano`）让你编辑提交信息，例如：

```text
fix:fix git err

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
...
Save modified buffer?  Y Yes  N No  ^C Cancel
```

**操作步骤（nano）：**

1. 修改第一行提交说明（可选），例如保持 `fix:fix git err`。
2. 按 `Ctrl + O`（字母 O） → 回车（确认写入 `COMMIT_EDITMSG`）。
3. 按 `Ctrl + X` 退出 nano。
4. 若 nano 再询问 `Save modified buffer?`，选择：
   - 按 `Y`（Yes）保存并退出。

完成后 rebase 会继续执行，回到 shell 后若无错误，说明该步已完成，可继续 `git push`。

---

### 6. 最终状态检查

完成 rebase 和 push 后，建议执行：

```bash
git status
git log --oneline --decorate --graph --max-count=10
```

预期结果：

- `git status` 显示：

  ```text
  On branch main
  Your branch is up to date with 'origin/main'.
  nothing to commit, working tree clean
  ```

- `git log` 中可以看到远端提交（例如 `86cb126 add :add so`）在历史中，本地新提交（集成 Bemfa、商店 UI 等）也已经在它之后，并且远端和本地指向同一个 HEAD。 

