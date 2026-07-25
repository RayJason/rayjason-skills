# Agent-instruction guidance

## Two governance levels

Audit both levels before proposing changes:

- Global or user guidance holds personal defaults shared across repositories:
  communication style, general Git preferences, approval boundaries, recurring
  workflow expectations, and pointers to reusable skills.
- Project guidance holds repository facts: build and test commands,
  architecture, module ownership, generated files, documentation routes, local
  size limits, release gates, and team conventions.

Report the current state before editing. For each loaded source, show its scope,
path, precedence, notable rules, conflicts, and recommendation. Then ask whether
to change the global level, project level, both, or neither.

Discover instruction files through safe host-aware checks. Do not ask the user
whether an `AGENTS.md` exists when the filesystem and host rules can answer it.
If a level has no instruction file, report it as missing and recommend whether
creating one would add durable value.

Do not move repository-specific commands into global guidance or personal
preferences into a shared repository without explicit user intent. Do not paste
tool inventories, skill summaries, chat history, or other host-injected context
into `AGENTS.md`.

## One policy, thin adapters

Prefer one repository-owned policy source, commonly `AGENTS.md`, plus the
smallest host adapter needed to load it. Do not maintain full copies of the same
rules in `AGENTS.md`, `CLAUDE.md`, and `CODEBUDDY.md`; they will drift.

Before relying on an adapter, verify the current host loaded it. Host behavior
changes over time.

## Good durable instructions

Include facts an agent cannot safely infer:

- supported build, test, and formatting commands;
- repository boundaries and source-of-truth locations;
- package-manager and commit expectations;
- generated or managed files that must not be edited directly;
- permission and release gates;
- routing links to module-specific architecture or operations documents;
- repeated project-specific mistakes to avoid.

Exclude:

- temporary task status;
- secrets or private credentials;
- long tutorials and historical narratives;
- generic engineering advice the agent already knows;
- commands that trigger destructive or external actions without confirmation.

## Scope and precedence

- Inspect the host's global instruction entrypoint and the complete applicable
  project chain before judging either file in isolation.
- Put repository-wide rules at the root.
- Put module-specific rules near the module only when the host supports nested
  instruction discovery; otherwise link them from the root policy.
- State which file is canonical when multiple host files exist.
- Treat personal or machine-local instruction files as non-portable.
- Resolve contradictions using the host's authority order; do not pick the most
  convenient rule.

## Portable example

For project guidance, start from `assets/AGENTS.example.md`. For Claude Code, use
`assets/CLAUDE.example.md` as an import adapter. For CodeBuddy, use
`assets/CODEBUDDY.example.md` only when a host-specific file is needed.

After setup, ask the active agent to list the project instructions it loaded and
compare the response with the intended policy.
