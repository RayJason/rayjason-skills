# Worktrees and dependency handoffs

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
