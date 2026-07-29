# RayJason Skills

[English](README.md) | **简体中文**

面向工程化软件交付的开源 Agent Skills 集合。

## Skills

| Skill | 展示名 | 用途 | 状态 |
| --- | --- | --- | --- |
| [`harness-agents-md`](harness-agents-md/) | 驾驭 AGENTS.md | 忠实创建、审查、重组或优化全局与项目级 Agent 指令 | 可用 |

新增 Skill 时，在表格中增加一行，并在仓库根目录放置同名 Skill 目录。

## 驾驭 AGENTS.md

`harness-agents-md` 面向 Codex、Claude Code、CodeBuddy、WorkBuddy
及其他 Agent 宿主，维护个人全局与项目级 Agent 指令。它：

- 仅在用户明确要求创建、审查、重组或优化 `AGENTS.md` / Agent 指令时触发；
- 发现当前机器实际生效的全局指令；存在时将其作为完全忠实的主要基准；
- 全局指令缺失时选择简洁的内置工程基准，其中包含 Git/变更安全、仅委派独立
  workstream、排他所有权，以及协调者负责集成和最终验证；
- 保留源文件语言、术语、阈值和用户已有选择；
- 只添加可追溯到用户要求、所选基准或已验证仓库事实的规则；
- 优先做简洁的最小改动，而不是生成通用政策。

普通 Git、rebase、merge、release、实现和编码请求不会触发此 Skill。

## Install

使用开源 Agent Skills CLI 为 Codex 全局安装：

```bash
npx skills add RayJason/rayjason-skills --skill harness-agents-md --global
```

- 可用 `bunx skills` 替代 `npx skills`。
- 去掉 `--global` 可安装到当前项目。

更新已安装版本：

```bash
npx skills update harness-agents-md --global --yes
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

契约测试会验证窄触发元数据、已有全局指令忠实性、缺失全局指令时的内置
fallback、按需 reference 路由和 trigger/no-trigger 行为场景。跨宿主模型评估参见
[`evals/README.md`](harness-agents-md/evals/README.md)。

worktree 清理脚本默认只预览。使用 `--apply` 前应检查解析出的仓库、worktree、
分支和目标引用。

## License

MIT
