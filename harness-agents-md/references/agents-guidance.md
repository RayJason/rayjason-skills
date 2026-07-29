# Agent-instruction guidance

## Baseline selection

Discover and read the active global instruction source before drafting. When it
exists, it is the exact primary source of truth for the user's defaults and for
the language, tone, terminology, and level of detail used in proposed
instructions.

Do not translate an English global file into Chinese, or any other language,
unless the user asks. Preserve explicit thresholds and workflow choices. Do not
replace them with values from this skill, its references, or its examples.

When the global source is confirmed missing, select
`assets/AGENTS.example.md` as the packaged engineering baseline and continue.
Its concise Git, collaboration, scope, and tool rules are intentional defaults
for this missing-global case. State that the fallback was selected so packaged
policy is not mistaken for an existing user file. Do not use it to supplement
or rewrite a present global source.

Every proposed addition needs one of these sources:

- an explicit requirement in the user's request;
- a rule already present in the discovered global instructions; or
- a packaged fallback rule when the global source is confirmed missing; or
- a verified repository fact necessary for the requested project scope.

If none applies, omit the rule. Other generic model advice and reference
checklists are not evidence. Prefer a short file over a
comprehensive-looking policy.

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

Report which source was selected. A confirmed missing global source selects the
packaged fallback; an inaccessible source is not proof that it is missing, so
disclose that uncertainty. Ask about scope only when the request is genuinely
ambiguous and the answer would materially change the edit.

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

## Thin adapters and fallback

Prefer one canonical policy source plus the smallest host adapter required to
load it. Verify the host actually loads the adapter before relying on it.

`assets/AGENTS.example.md` is an operational fallback only for a confirmed
missing global source. Keep its engineering intent and adapt it narrowly to the
requested target and verified repository facts. It never overrides a present
global source.
