# RayJason Skills

面向工程化软件交付的开源 Agent Skills 集合。

## Skills

| Skill | 展示名 | 用途 | 状态 |
| --- | --- | --- | --- |
| [`harness-agents-md`](harness-agents-md/) | 驾驭AGENTS.md | 分层治理全局与项目级 `AGENTS.md`，让规则可执行、可验证、可维护 | 可用 |

新增 Skill 时，在表格中增加一行，并在仓库根目录放置同名 Skill 目录。

## 驾驭 AGENTS.md

`harness-agents-md` 面向 Codex、Claude Code、CodeBuddy、WorkBuddy
及其他 Agent 宿主，工程化维护个人全局与项目代理规则。它覆盖：

- 宿主能力识别与降级；
- 全局与项目级规则链盘点、分层建议和作用域纠错；
- 指令优先级、权限和提示词注入边界；
- 模块边界与协调者/执行者分工；
- 基于证据的验证、发布与上下游交接；
- 避免形式化文档膨胀的文档生命周期；
- 带自动安全测试的 Git worktree 清理。
- 完成治理后可选的 Schedule 周期审计。

## Install

使用开源 Agent Skills CLI 为 Codex 全局安装：

```bash
bunx skills add RayJason/rayjason-skills \
  --skill harness-agents-md \
  --global \
  --agent codex \
  --yes
```

可以用 `npx skills` 替代 `bunx skills`。去掉 `--global` 可安装到当前项目；
也可以选择其他支持的 Agent：

```bash
bunx skills add RayJason/rayjason-skills \
  --skill harness-agents-md \
  --global \
  --agent claude-code \
  --yes
```

更新已安装版本：

```bash
bunx skills update harness-agents-md --global --yes
```

WorkBuddy 用户可以从 Skills 界面导入本地 Skill 包。

宿主行为可能变化。依赖自动加载指令前，请查看
[`agent-compatibility.md`](harness-agents-md/references/agent-compatibility.md)。

## Develop

通过 SSH 克隆仓库：

```bash
git clone git@github.com:RayJason/rayjason-skills.git
```

## Validate

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py harness-agents-md
python3 harness-agents-md/scripts/test_skill_contract.py
bash -n harness-agents-md/scripts/*.sh
harness-agents-md/scripts/test_cleanup_worktree.sh
```

契约测试会验证发现元数据、按需 reference 路由和行为场景语料。跨宿主模型评估
参见 [`evals/README.md`](harness-agents-md/evals/README.md)。

worktree 清理脚本默认只预览。使用 `--apply` 前应检查解析出的仓库、worktree、
分支和目标引用。

## License

MIT
