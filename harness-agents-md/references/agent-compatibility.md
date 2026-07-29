# Agent compatibility

Keep governance concepts portable. Instruction filenames, skill installation,
delegation, permission models, and automation are host adapters.

## Codex

- Resolve the active Codex home from host configuration or environment instead
  of assuming a path from another machine. In that directory, inspect
  `AGENTS.override.md` and `AGENTS.md`; the first non-empty file in that order
  is the active global source.
- Read that file before drafting. Treat it as the primary source of truth for
  user defaults and output language. If the home or file is inaccessible,
  report that limitation instead of substituting the installed skill, an
  example, or remembered content.
- Project instructions: from the project root to the current directory, read at
  most one applicable instruction file per directory. More specific files
  appear later and take precedence.
- Codex normally builds this instruction chain once per run. After changing an
  instruction file, verify the loaded sources in a new session.
- Report the resolved global source and applicable project chain before
  proposing edits. Keep personal defaults global and repository facts in the
  project.
- Repository skill package: `.agents/skills/harness-agents-md/SKILL.md`
  when the current Codex host supports repository-local skills.
- User installation commonly uses the Codex-configured skills directory; verify
  it in the active host rather than assuming a machine path.
- Use Codex plans, subagents, worktrees, approvals, and automations only when
  those capabilities are present in the current session.

## Claude Code

- Repository instructions: `CLAUDE.md`.
- Repository skill package: `.claude/skills/harness-agents-md/SKILL.md`;
  user package: `~/.claude/skills/harness-agents-md/SKILL.md`.
- To share a canonical `AGENTS.md`, use the thin adapter in
  `assets/CLAUDE.example.md`; Claude Code supports `@AGENTS.md` imports.
- Larger Claude-only rules may use `.claude/rules/`; keep portable policy out of
  host-specific duplicates.
- Confirm loaded sources with Claude Code's current memory or instruction
  inspection facility.

## Tencent CodeBuddy

- Repository instructions: `CODEBUDDY.md`.
- Repository skill package: `.codebuddy/skills/harness-agents-md/SKILL.md`;
  user package: `~/.codebuddy/skills/harness-agents-md/SKILL.md`.
- Current CodeBuddy IDE documentation says a root `AGENTS.md` is loaded when
  `CODEBUDDY.md` is absent. If both are needed, keep `AGENTS.md` canonical and
  use `assets/CODEBUDDY.example.md` as a pointer.
- Project-specific subagents and settings are host features, not requirements of
  this governance skill.

## Tencent WorkBuddy

- Install the skill through WorkBuddy's local skill-package import or supported
  skill marketplace flow.
- Select the repository as the task workspace and keep the package self-contained.
- Do not invent a project-instruction filename or local install path when the
  current WorkBuddy documentation or UI does not expose one.
- WorkBuddy may run multiple tasks, but task isolation is not proof of Git or
  file isolation. Confirm workspace paths and ownership before parallel edits.

## Other agents

1. Discover the host's documented instruction entrypoint.
2. Determine whether it reads `AGENTS.md` directly or needs a thin adapter.
3. Verify how skills are discovered and whether local scripts require approval.
4. Inventory delegation, isolation, permission, and automation capabilities.
5. Use the portable workflow and downgrade unsupported mechanics.

## Drift rule

Host behavior changes. Verify adapter claims against current official
documentation before installing globally or relying on automatic instruction
loading.

Official references checked on 2026-07-26:

- Codex AGENTS.md:
  <https://developers.openai.com/codex/guides/agents-md>
- Codex scheduled tasks:
  <https://developers.openai.com/codex/app/automations>
- Claude Code memory: <https://code.claude.com/docs/en/memory>
- Claude Code skills: <https://code.claude.com/docs/en/skills>
- CodeBuddy rules: <https://www.workbuddy.cn/docs/ide/User-guide/Rules>
- CodeBuddy skills: <https://www.workbuddy.ai/docs/cli/skills>
- WorkBuddy skills:
  <https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market>
