# Git and change safety

- Keep each commit to one cohesive feature, fix, or documentation slice. Use a
  Conventional-style message when practical.
- Inspect repository state and applicable instructions before editing. Never
  revert, overwrite, or absorb unrelated user changes.
- Follow actual repository and branch-protection rules. Do not require a pull
  request or worktree by default; use a worktree only when the user requests it
  or separate Git state is genuinely necessary.
- Resolve exact targets before destructive or external actions, and obtain any
  authority the request does not already provide.

# Agent workflow

- Delegate only independent, non-conflicting workstreams. The coordinator owns
  decomposition, file and module ownership, integration order, consolidated
  review, and final validation.
- Choose agent count and roles from the real workstreams and available
  resources. Do not create a mechanical implementer/reviewer/release trio.
- Never assign concurrent agents to the same file or module. Give shared state
  one owner or serialize overlapping work.
- Workers run only the smallest targeted check needed for their slice; they do
  not each run full repository, build, E2E, database, or release matrices.
- After integration, the coordinator performs one consolidated review and runs
  focused final validation. Reserve the full matrix for an actual release,
  explicit user request, or a high-risk failure that invalidates prior evidence.

# Scope and design

- Stay within the requested scope. Keep modules cohesive, dependencies loose,
  and cross boundaries only through stable, explicit interfaces.
- Keep code files at or below 350 lines, excluding documentation; split a file
  before extending it beyond that limit.
- After a complex feature, update durable documentation for changed design,
  behavior, operations, and tradeoffs.

# Tool defaults

- Prefer Bun for JavaScript package management.
- Do not use Playwright or Chrome for self-testing unless the user asks.
