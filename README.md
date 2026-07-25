# RayJason Skills

Open-source Agent Skills for practical software delivery.

## Agent Repo Steward

`agent-repo-steward` keeps long-running, AI-assisted repositories governable
across Codex, Claude Code, CodeBuddy, WorkBuddy, and other Agent hosts.

It covers:

- host capability detection and graceful fallback;
- instruction authority, permission, and prompt-injection boundaries;
- scoped architecture and coordinator/worker ownership;
- evidence-based verification and upstream/downstream handoffs;
- documentation lifecycle without ceremonial file churn;
- guarded Git worktree cleanup with automated safety tests.

The skill package is in [`agent-repo-steward`](agent-repo-steward/).

## Clone

Use the SSH remote:

```bash
git clone git@github.com:RayJason/rayjason-skills.git
```

## Install

Copy or symlink the `agent-repo-steward` directory into the skill directory
supported by your Agent host:

- Codex project: `.agents/skills/agent-repo-steward/`
- Claude Code project: `.claude/skills/agent-repo-steward/`
- CodeBuddy project: `.codebuddy/skills/agent-repo-steward/`
- WorkBuddy: import the local skill package from the Skills interface

Host behavior changes over time. See
[`agent-compatibility.md`](agent-repo-steward/references/agent-compatibility.md)
before relying on automatic instruction loading.

## Validate

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py agent-repo-steward
bash -n agent-repo-steward/scripts/*.sh
agent-repo-steward/scripts/test_cleanup_worktree.sh
```

The cleanup helper is preview-only by default. Review its resolved repository,
worktree, branch, and target ref before using `--apply`.

## License

MIT
