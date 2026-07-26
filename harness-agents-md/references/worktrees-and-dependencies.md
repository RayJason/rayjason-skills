# Worktrees and dependency handoffs

## Worktree decision

Do not create a worktree by default. Extra checkouts consume disk, duplicate
build artifacts and dependencies, and can increase operational cleanup.

Prefer:

1. one owner per file and module;
2. parallel work only for non-overlapping scopes; and
3. sequential execution when scopes overlap.

Use a worktree only when the user requests it or the task genuinely needs
separate Git state, branch isolation, or a disposable experiment that cannot be
handled safely in the current checkout. Check available disk and expected build
cost first. A worktree never authorizes two agents to modify the same file or
module concurrently.

Apply `MA-OWNER` from `multi-agent-workflow.md` before parallel worktree
dispatch.

## Branch workflow

Resolve the actual default branch and inspect hosting-provider branch
protection or rulesets plus repository guidance such as `README`,
`CONTRIBUTING`, `AGENTS.md`, CI, and release docs.

When protection or repository policy requires branch-based delivery:

- create a new task-specific branch before editing;
- keep one cohesive purpose per branch;
- keep commits within that branch aligned to the same purpose;
- never commit directly to the protected default branch;
- use the repository's required review and integration path.

Do not infer that a branch is required only because the default branch is named
`main` or `master`. If no rule requires it, follow the user's selected workflow.

## Worktree lifecycle

1. Confirm the repository policy permits a worktree and branch.
2. Assign exclusive file ownership or an independent module.
3. Implement, verify, and commit a cohesive slice.
4. Integrate into the intended target ref.
5. Confirm the worktree commit is an ancestor of that target ref.
6. Confirm the secondary worktree is clean and registered to this repository.
7. Preview `scripts/cleanup_worktree.sh`.
8. Re-run with `--apply` after checking the resolved paths and refs.
9. Report removed worktree, deleted branch, and remaining worktrees.

Never force-remove a dirty, locked, primary, unregistered, or unmerged
worktree. Never infer a destructive target from an unresolved variable or glob.

## Cleanup helper

```bash
# Preview only
scripts/cleanup_worktree.sh <worktree-path> [temporary-branch] [target-ref]

# Apply the previewed cleanup
scripts/cleanup_worktree.sh --apply <worktree-path> [temporary-branch] [target-ref]
```

`target-ref` defaults to the current `HEAD`. Run the helper from the repository
that owns the worktree.

## Upstream change handoff

An upstream update is incomplete until downstream users can adopt it safely.
Provide:

- released version or immutable commit identity;
- breaking and behavioral change summary;
- affected consumers and compatibility window;
- migrations for data, configuration, API, or filesystem changes;
- step-by-step upgrade and validation;
- rollback procedure;
- owner and status of downstream adoption.

Do not describe unpublished code as an available dependency. Downstream projects
should consume the migration package instead of reverse-engineering a diff.
