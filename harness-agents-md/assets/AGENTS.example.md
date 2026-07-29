# Engineering defaults

- Inspect repository state and applicable instructions before editing. Stay
  within the requested scope and never overwrite unrelated user changes.
- Keep each change and commit cohesive. Follow the repository's actual branch
  and validation rules; use a worktree only when requested or genuinely needed.
- Resolve exact targets before destructive actions and obtain missing authority.

# Delegation

- Delegate only independent, non-conflicting workstreams. The coordinator owns
  decomposition, file and module ownership, integration, final review, and
  validation.
- Choose agents from the real work; do not create fixed roles mechanically.
- Never assign concurrent agents to the same file or module. Give shared state
  one owner or serialize overlapping work.
- Workers run the smallest targeted check for their slice. The coordinator
  reviews the combined diff and runs focused final validation.
