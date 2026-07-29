# Agent-instruction guidance

## Primary-source fidelity

Discover and read the active global instruction source before drafting. When it
exists, it is the primary source of truth for the user's defaults and for the
language, tone, terminology, and level of detail used in proposed instructions.

Do not translate an English global file into Chinese, or any other language,
unless the user asks. Preserve explicit thresholds and workflow choices. Do not
replace them with values from this skill, its references, or its examples.

Every proposed addition needs one of these sources:

- an explicit requirement in the user's request;
- a rule already present in the discovered global instructions; or
- a verified repository fact necessary for the requested project scope.

If none applies, omit the rule. Generic model advice and bundled examples are
not evidence. Prefer a short file over a comprehensive-looking policy.

## Scope and precedence

- Global guidance holds personal defaults shared across repositories.
- Project guidance holds repository facts and intentional project-specific
  overrides.
- More specific project instructions may override inherited defaults according
  to the host's precedence rules.

Read the complete applicable chain before judging a target in isolation. Honor
the target the user named. A project-only request may use global instructions
as a read-only baseline; it does not authorize changing the global file or
duplicating inherited global rules into the project file.

Report missing or inaccessible sources instead of silently substituting a
template. Ask about scope only when the request is genuinely ambiguous and the
answer would materially change the edit.

## Minimal edits

- Preserve compatible existing wording instead of rewriting for style alone.
- Merge semantic duplicates without weakening stricter thresholds.
- Add repository commands, boundaries, generated-file rules, or release gates
  only when they are verified and relevant to the requested change.
- Exclude temporary task state, secrets, host-injected tool inventories, chat
  history, tutorials, and generic engineering advice.
- Do not introduce branches, worktrees, subagents, schedules, trackers, or
  documentation processes merely because a reference discusses them.
- If the current instructions already satisfy the request, recommend no change.

## Thin adapters and examples

Prefer one canonical policy source plus the smallest host adapter required to
load it. Verify the host actually loads the adapter before relying on it.

`assets/AGENTS.example.md` is structure-only and may be used only when the
requested target does not exist. Copy neither its placeholders nor unrelated
reference rules into the result. Match the discovered global language and keep
only sections supported by the user's request or verified repository facts.
