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
2. When a global `AGENTS.md` or equivalent exists, use it as the primary source
   of truth for drafting style and user defaults. Preserve its language, tone,
   terminology, thresholds, and intent unless the user explicitly requests a
   change or translation.
3. Change only the scope the user requested. A project-only request may read
   global instructions as a baseline but must not rewrite them.
4. Every added rule must be traceable to the user's request, an existing global
   rule, or a verified repository fact needed for the requested scope.
   References and examples are aids, not policy sources. Do not add generic best
   practices, workflow machinery, schedules, or progress tracking unasked.
5. Prefer the smallest useful delta. Merge duplicates and remove stale text
   when requested; if no change is justified, say so. Keep the result concise.

## Workflow

1. Resolve the requested action and target. If the user did not explicitly ask
   to create, review, reorganize, or optimize `AGENTS.md` or agent instructions,
   stop using this skill.
2. Read the discovered global source first, then the applicable project chain
   and target file. Report a missing or inaccessible global source; never
   replace it silently with bundled guidance.
3. Audit only the requested concerns. Distinguish inherited global preferences
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

When creating a file from scratch, `assets/AGENTS.example.md` is a
structure-only fallback. It never overrides the discovered global source and
must not be copied as a policy checklist.
