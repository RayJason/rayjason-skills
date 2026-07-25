---
name: harness-agents-md
description: "工程化创建、审计和优化全局与项目级 AGENTS.md，覆盖作用域、协作、Git、验证与交付；不用于普通代码修改或只读问答。"
---

# 驾驭 AGENTS.md

分析全局与项目级现有的 `AGENTS.md` 文件，整理零散、冲突、不可执行、过时的约定。先读取真实环境和仓库，再给方案；不套用通用模板。

## 安装

```bash
npx skills add RayJason/rayjason-skills --skill harness-agents-md --global
```

- 可用 `bunx skills` 替代 `npx skills`
- 去掉 `--global` 可安装到当前项目。

## 使用方法

在目标仓库中对 Agent 说：
```text
请使用 harness-agents-md，分析全局与项目级 AGENTS.md 文件，给出建议，等我选择治理范围后再修改并验证。
```

## 工作流

1. 识别宿主能力、全局指令入口、项目根目录、嵌套规则、权限和作用域；自行判断各层文件是否存在，不要求用户说明。
2. 分别读取全局层与从项目根到当前目录的规则链；确认实际加载顺序。
3. 先报告两层现状、冲突、重复、缺失和错放规则，再分别给出建议。
4. 让用户选择只改全局、只改项目、两者都改或暂不修改。
5. 经授权后更新并验证；保留无关用户改动，区分实现、提交与发布。

## 按需加载

- 安装或适配宿主：
  `references/agent-compatibility.md` 和 `references/agents-guidance.md`.
- 指令优先级、审批、敏感数据或风险副作用：
  `references/security-and-approvals.md`.
- 架构边界或跨模块方案：
  `references/architecture-and-scope.md`.
- 多 Agent 分工：
  `references/multi-agent-workflow.md`.
- 任务状态、路线图或长期文档：
  `references/documentation-lifecycle.md`.
- worktree 或依赖交接：
  `references/worktrees-and-dependencies.md`.
- 运行、发布、部署、迁移或采用证据：
  `references/verification-and-handoffs.md`.

只加载本次需要的资料。缺少多 Agent、worktree 或自动化能力时顺序执行，
不得模拟。破坏性、生产、发布、凭证和外部数据操作必须有明确授权。

清理 worktree 时使用 `scripts/cleanup_worktree.sh`；默认只预览，传 `--apply`
前检查仓库、分支、干净状态和祖先关系。完成时报告结果、变更范围、验证证据、
跳过项、风险和 commit。

## 周期治理

完成一次治理后，必须询问用户是否设置 Schedule，选项包括：治理全局指令与
已安装 Skills、治理项目级 `AGENTS.md`/宿主适配文件、两者都治理或暂不设置。
仅在用户明确同意后创建；先确认周期、项目范围、运行位置和权限，并手动测试
任务提示词。默认建议每周、只审计并报告建议；自动改文件或清理 Skill 需要
单独授权。Git 项目需要写入时优先使用隔离 worktree。
