---
name: harness-agents-md
description: "Explicit user requests to create, review, reorganize, or optimize AGENTS.md or agent instructions only."
---

# Harness AGENTS.md

Use this skill only for the explicit instruction-editing requests named above.
Ordinary Git, release, implementation, and coding work is out of scope.

## Choose the baseline

1. Discover the active global instruction source. In Codex, resolve the active
   Codex home and use the first non-empty `AGENTS.override.md` or `AGENTS.md`.
   On other hosts, use the documented global source; do not guess.
2. If a global source exists, use it as the exact baseline. Preserve its
   language, terminology, thresholds, and intent unless the user asks to change
   them. Do not mix in the packaged fallback.
3. If the global source is confirmed missing, use
   `assets/AGENTS.example.md` as the engineering fallback and continue. State
   that the fallback was used. An inaccessible source is not confirmed missing.
4. Read the target and applicable project instructions. A project-only request
   may inherit global guidance but does not authorize editing the global file.

## Make the smallest useful change

- Change only the requested instruction scope.
- Add a rule only when it comes from the request, the selected baseline, or a
  verified repository fact.
- Do not invent generic workflows, release checklists, trackers, schedules, or
  host-specific machinery.
- Preserve compatible wording, merge duplicates, and say when no change is
  justified.
- Inspect the final diff and report the selected baseline, changed scope, and
  validation performed.
