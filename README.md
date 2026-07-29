# RayJason Skills

**English** | [简体中文](README.zh-CN.md)

An open-source collection of Agent Skills for production-grade software delivery.

## Skills

| Skill | Display name | Purpose | Status |
| --- | --- | --- | --- |
| [`harness-agents-md`](harness-agents-md/) | Harness AGENTS.md | Faithfully create, review, reorganize, or optimize global and project agent instructions | Available |

When adding a skill, add a row to this table and place a directory with the same
name at the repository root.

## Harness AGENTS.md

`harness-agents-md` maintains personal, global, and project agent instructions
for Codex, Claude Code, CodeBuddy, WorkBuddy, and other agent hosts. It:

- activates only for an explicit request to create, review, reorganize, or
  optimize `AGENTS.md` or agent instructions;
- discovers the active machine's global instructions and uses them as the
  primary drafting baseline;
- preserves the source language, terminology, thresholds, and user choices;
- adds only rules traceable to the request, existing global instructions, or
  verified repository facts; and
- prefers a concise delta over generic policy generation.

Ordinary Git, rebase, merge, release, implementation, and coding requests do
not trigger this skill.

## Install

Install globally for Codex with the open-source Agent Skills CLI:

```bash
npx skills add RayJason/rayjason-skills --skill harness-agents-md --global
```

- You can use `bunx skills` instead of `npx skills`.
- Remove `--global` to install into the current project.

Update an installed skill:

```bash
npx skills update harness-agents-md --global --yes
```

WorkBuddy users can import a local skill package from the Skills interface.

Host behavior may change. Before relying on automatic instruction loading, see
[`agent-compatibility.md`](harness-agents-md/references/agent-compatibility.md).

## Develop

Clone the repository over SSH:

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

The contract tests validate narrow discovery metadata, global-instruction
fidelity, on-demand reference routing, and trigger/no-trigger scenario fixtures.
See
[`evals/README.md`](harness-agents-md/evals/README.md) for cross-host model
evaluations.

The worktree cleanup script only previews changes by default. Before using
`--apply`, inspect the resolved repository, worktree, branch, and target
reference.

## License

MIT
