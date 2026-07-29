---
name: harness-agents-md
description: "Explicit user requests to create, review, reorganize, or optimize AGENTS.md or agent instructions only."
---

# Harness AGENTS.md

Edit or audit agent instructions with the smallest faithful change. Installing
this skill must not affect ordinary repository work.

## Fidelity contract

1. Discover the active host's global instruction source before drafting. For
   Codex discovery and precedence, load `references/agent-compatibility.md`.
2. When a global `AGENTS.md` or equivalent exists, use it as the exact primary
   source of truth for drafting style and user defaults. Preserve its language,
   tone, terminology, thresholds, and intent unless the user explicitly
   requests a change or translation. Do not merge packaged defaults into it.
3. When no global source exists, select `assets/AGENTS.example.md` as the
   packaged engineering fallback baseline and continue the requested work.
   State that fallback was used. Adapt it only for the requested scope and
   verified repository facts; do not present it as the user's existing policy.
4. Change only the scope the user requested. A project-only request may read
   global instructions as a baseline but must not rewrite them.
5. Every added rule must be traceable to the user's request, a present global
   rule, the selected missing-global fallback, or a verified repository fact
   needed for the requested scope. Other references are aids, not policy
   sources. Do not add unrelated workflow machinery, schedules, or progress
   tracking unasked.
6. Prefer the smallest useful delta. Merge duplicates and remove stale text
   when requested; if no change is justified, say so. Keep the result concise.

## Workflow

1. Resolve the requested action and target. If the user did not explicitly ask
   to create, review, reorganize, or optimize `AGENTS.md` or agent instructions,
   stop using this skill.
2. Inspect the global location first. Read the active global source when
   present; when confirmed missing, load the packaged fallback. If discovery is
   inaccessible rather than missing, disclose that uncertainty.
3. Read the applicable project chain and target file. Audit only the requested
   concerns. Distinguish inherited global preferences or fallback defaults
   from verified project-specific exceptions and host-specific adapters.
4. Apply the authorized edit or give the requested review. Ask a question only
   when unresolved scope would materially change the result.
5. Inspect the final diff, validate instruction loading when practical, and
   report changed scope plus skipped checks.

## Conditional references

Load only what the explicit instruction-editing request needs:

- Host discovery, precedence, or adapters:
  `references/agent-compatibility.md` and
  `references/agents-guidance.md`.
- Architecture or module-boundary instructions:
  `references/architecture-and-scope.md`.
- Documentation-lifecycle instructions:
  `references/documentation-lifecycle.md`.
- Multi-agent instruction sections:
  `references/multi-agent-workflow.md`.
- Branch, worktree, or dependency-handoff instruction sections:
  `references/worktrees-and-dependencies.md`.
- Verification, release, migration, or handoff instruction sections:
  `references/verification-and-handoffs.md`.

`assets/AGENTS.example.md` is used only when global instructions are confirmed
missing. It is the packaged engineering default in that case, never an override
or supplement for a present global source.
