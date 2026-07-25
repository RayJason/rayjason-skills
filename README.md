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

## Install

Install `agent-repo-steward` globally for Codex with the open Agent Skills CLI:

```bash
bunx skills add RayJason/rayjason-skills \
  --skill agent-repo-steward \
  --global \
  --agent codex \
  --yes
```

`npx skills` can be used in place of `bunx skills`. Remove `--global` to
install into the current project, or select another supported host:

```bash
bunx skills add RayJason/rayjason-skills \
  --skill agent-repo-steward \
  --global \
  --agent claude-code \
  --yes
```

Update an installed copy with:

```bash
bunx skills update agent-repo-steward --global --yes
```

WorkBuddy users can import the local skill package from the Skills interface.

Host behavior changes over time. See
[`agent-compatibility.md`](agent-repo-steward/references/agent-compatibility.md)
before relying on automatic instruction loading.

## Develop

Clone the source repository over SSH:

```bash
git clone git@github.com:RayJason/rayjason-skills.git
```

## Validate

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py agent-repo-steward
python3 agent-repo-steward/scripts/test_skill_contract.py
bash -n agent-repo-steward/scripts/*.sh
agent-repo-steward/scripts/test_cleanup_worktree.sh
```

The contract test validates discovery metadata, conditional reference routing,
and the behavior-scenario corpus. See
[`evals/README.md`](agent-repo-steward/evals/README.md) for cross-host model
evaluation.

The cleanup helper is preview-only by default. Review its resolved repository,
worktree, branch, and target ref before using `--apply`.

## License

MIT
