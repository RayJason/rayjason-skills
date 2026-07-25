#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: $0 [--apply] <worktree-path> [temporary-branch] [target-ref]" >&2
}

apply=false
if [ "${1:-}" = "--apply" ]; then
  apply=true
  shift
fi

if [ "$#" -lt 1 ] || [ "$#" -gt 3 ]; then
  usage
  exit 2
fi

worktree_path="$1"
temporary_branch="${2:-}"
target_ref="${3:-HEAD}"

git rev-parse --is-inside-work-tree >/dev/null
repository_root="$(git rev-parse --show-toplevel)"
primary_path="$(cd "$repository_root" && pwd -P)"

if [ ! -d "$worktree_path" ]; then
  echo "Refusing cleanup: path is not a directory: $worktree_path" >&2
  exit 1
fi

resolved_path="$(cd "$worktree_path" && pwd -P)"
if [ "$resolved_path" = "$primary_path" ]; then
  echo "Refusing cleanup: target is the primary worktree: $resolved_path" >&2
  exit 1
fi

if ! git -c core.quotePath=false worktree list --porcelain |
  awk -v target="$resolved_path" '
    index($0, "worktree ") == 1 && substr($0, 10) == target { found = 1 }
    END { exit(found ? 0 : 1) }
  '; then
  echo "Refusing cleanup: path is not a registered worktree of this repository." >&2
  exit 1
fi

if [ -n "$(git -C "$resolved_path" status --porcelain)" ]; then
  echo "Refusing cleanup: worktree has tracked or untracked changes." >&2
  exit 1
fi

if ! target_commit="$(
  git rev-parse --verify --quiet --end-of-options "${target_ref}^{commit}"
)"; then
  echo "Refusing cleanup: target ref does not resolve to a commit: $target_ref" >&2
  exit 1
fi

worktree_commit="$(git -C "$resolved_path" rev-parse HEAD)"
if ! git merge-base --is-ancestor "$worktree_commit" "$target_commit"; then
  echo "Refusing cleanup: worktree HEAD is not contained in $target_ref." >&2
  exit 1
fi

actual_branch="$(git -C "$resolved_path" symbolic-ref --quiet --short HEAD || true)"
if [ -n "$temporary_branch" ]; then
  if ! git check-ref-format "refs/heads/$temporary_branch" >/dev/null; then
    echo "Refusing cleanup: invalid branch name: $temporary_branch" >&2
    exit 1
  fi
  if [ "$actual_branch" != "$temporary_branch" ]; then
    echo "Refusing cleanup: worktree branch is '$actual_branch', not '$temporary_branch'." >&2
    exit 1
  fi
  if ! git show-ref --verify --quiet "refs/heads/$temporary_branch"; then
    echo "Refusing cleanup: local branch not found: $temporary_branch" >&2
    exit 1
  fi
fi

echo "Repository: $primary_path"
echo "Worktree:  $resolved_path"
echo "HEAD:      $worktree_commit"
echo "Target:    $target_ref ($target_commit)"
echo "Branch:    ${actual_branch:-detached}"
if [ -n "$temporary_branch" ]; then
  echo "Delete:    refs/heads/$temporary_branch"
else
  echo "Delete:    no branch requested"
fi

if [ "$apply" != true ]; then
  echo "Preview only. Re-run with --apply to perform this cleanup."
  exit 0
fi

git worktree remove -- "$resolved_path"
git worktree prune

if [ -n "$temporary_branch" ]; then
  git branch -d -- "$temporary_branch"
fi

echo "Cleanup complete. Remaining worktrees:"
git worktree list
