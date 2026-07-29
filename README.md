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

`harness-agents-md` is a small engineering aid for personal, global, and
project agent instructions. It:

- activates only for an explicit request to create, review, reorganize, or
  optimize `AGENTS.md` or agent instructions;
- follows the active global source faithfully when it exists;
- uses a concise packaged fallback when it does not; and
- makes the smallest change supported by the request, selected baseline, and
  verified repository facts.

Ordinary Git, rebase, merge, release, implementation, and coding requests do
not trigger this skill.

The package deliberately contains no release playbook, worktree utility,
tracking system, schedule workflow, or host-specific reference library. Capable
models do not need those policies duplicated in this skill.

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

## Develop

Clone the repository over SSH:

```bash
git clone git@github.com:RayJason/rayjason-skills.git
```

## Validate

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py harness-agents-md
python3 harness-agents-md/scripts/test_skill_contract.py
```

The contract tests validate the deliberately small package, narrow activation,
present-global fidelity, missing-global fallback, and trigger/no-trigger
scenarios. See
[`evals/README.md`](harness-agents-md/evals/README.md) for cross-host model
evaluations.

## License

MIT
