# Git版本控制

> **Source:** [Git.md](../../../raw/Study_Note/05-工具与技巧/Git使用/Git.md)
> **TLDR:** Git常用工作流和命令速查——仓库管理、分支操作、提交规范、合并与变基、日志查看、暂存与重置、标签管理。

## Key Points

- **工作流**：Working Directory → Staging Area(`git add`) → Local Repo(`git commit`) → Remote Repo(`git push`)
- **分支管理**：`git branch`/`git checkout -b`创建切换；`feature`/`fix`/`release`分支策略；`git merge`合并，`git rebase`变基
- **提交规范**：`<type>: <subject>`格式（feat/fix/docs/style/refactor/test/chore）；语义清晰、原子化提交
- **常用操作**：`git log --oneline --graph`可视化历史；`git stash`暂存工作区；`git reset`/`git revert`回退；`git diff`比较差异
- **冲突解决**：手动编辑冲突标记→`git add`标记解决→`git commit`完成合并
- **实用技巧**：`.gitignore`忽略文件；`git tag`标记版本；`git cherry-pick`精选提交

## Related Concepts

- [[cmake-build-system]] — 构建系统配合
