# RayJason Skills

[English](README.md) | **简体中文**

面向工程化软件交付的开源 Agent Skills 集合。

## Skills

| Skill | 展示名 | 用途 | 状态 |
| --- | --- | --- | --- |
| [`harness-agents-md`](harness-agents-md/) | 驾驭 AGENTS.md | 忠实创建、审查、重组或优化全局与项目级 Agent 指令 | 可用 |

新增 Skill 时，在表格中增加一行，并在仓库根目录放置同名 Skill 目录。

## 驾驭 AGENTS.md

`harness-agents-md` 是一个用于维护个人全局与项目级 Agent 指令的小型工程辅助
Skill。它：

- 仅在用户明确要求创建、审查、重组或优化 `AGENTS.md` / Agent 指令时触发；
- 全局指令存在时忠实沿用；
- 全局指令缺失时使用简洁的内置工程 fallback；
- 只做用户要求、所选基准和已验证仓库事实支持的最小改动。

普通 Git、rebase、merge、release、实现和编码请求不会触发此 Skill。

包内刻意不再提供 release 流程、worktree 工具、进度追踪、Schedule 工作流或
宿主专用 reference 库；能力足够的模型不需要 Skill 重复约束这些内容。

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

## Develop

通过 SSH 克隆仓库：

```bash
git clone git@github.com:RayJason/rayjason-skills.git
```

## Validate

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py harness-agents-md
python3 harness-agents-md/scripts/test_skill_contract.py
```

契约测试会验证精简后的包结构、窄触发元数据、已有全局指令忠实性、缺失
全局指令时的 fallback，以及 trigger/no-trigger 行为场景。跨宿主模型评估参见
[`evals/README.md`](harness-agents-md/evals/README.md)。

## License

MIT
