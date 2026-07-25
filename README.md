# RayJason Skills

**English** | [简体中文](README.zh-CN.md)

An open-source collection of Agent Skills for production-grade software delivery.

## Skills

| Skill | Display name | Purpose | Status |
| --- | --- | --- | --- |
| [`harness-agents-md`](harness-agents-md/) | Harness AGENTS.md | Govern global and project-level `AGENTS.md` files with executable, verifiable, and maintainable rules | Available |

When adding a skill, add a row to this table and place a directory with the same
name at the repository root.

## Harness AGENTS.md

`harness-agents-md` provides an engineering-oriented way to maintain personal,
global, and project-level agent rules for Codex, Claude Code, CodeBuddy,
WorkBuddy, and other agent hosts. It covers:

- host capability detection and graceful degradation;
- auditing global and project-level rule chains, recommending appropriate
  layers, and correcting scope;
- global high-cohesion, low-coupling, and 350-line-per-file defaults while
  respecting existing user constraints;
- main branch protection, README/CONTRIBUTING conventions, and
  single-responsibility branch strategies;
- module boundaries and coordinator/executor responsibilities;
- a default maximum of five subagents, single ownership per file/module, and
  sequential execution for overlapping tasks;
- evidence-based validation, release, and downstream handoff;
- documentation lifecycles that avoid unnecessary process bloat;
- discovery of existing tasks and roadmaps, with optional project progress
  document management;
- avoiding worktrees unless necessary, with an automated and safety-tested
  cleanup workflow;
- optional scheduled audits after governance is established.

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

The contract tests validate discovery metadata, on-demand reference routing, and
behavioral scenario fixtures. See
[`evals/README.md`](harness-agents-md/evals/README.md) for cross-host model
evaluations.

The worktree cleanup script only previews changes by default. Before using
`--apply`, inspect the resolved repository, worktree, branch, and target
reference.

## License

MIT
