#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "$0")" && pwd -P)"
cleanup_script="$script_dir/cleanup_worktree.sh"
test_root="$(mktemp -d)"

cleanup() {
  chmod -R u+w "$test_root" 2>/dev/null || true
  rm -rf "$test_root"
}
trap cleanup EXIT

repository="$test_root/repository"
merged_worktree="$test_root/merged-worktree"
unmerged_worktree="$test_root/unmerged-worktree"
dirty_worktree="$test_root/dirty-worktree"

git init -q -b main "$repository"
git -C "$repository" config user.name "Skill Test"
git -C "$repository" config user.email "skill-test@example.invalid"
printf 'base\n' >"$repository/state.txt"
git -C "$repository" add state.txt
git -C "$repository" commit -q -m "base"

git -C "$repository" worktree add -q -b merged-slice "$merged_worktree"
printf 'merged\n' >>"$merged_worktree/state.txt"
git -C "$merged_worktree" add state.txt
git -C "$merged_worktree" commit -q -m "merged slice"
git -C "$repository" merge -q --ff-only merged-slice

preview="$(
  cd "$repository"
  "$cleanup_script" "$merged_worktree" merged-slice main
)"
case "$preview" in
  *"Preview only."*) ;;
  *)
    echo "Preview marker missing." >&2
    exit 1
    ;;
esac
test -d "$merged_worktree"

(
  cd "$repository"
  "$cleanup_script" --apply "$merged_worktree" merged-slice main >/dev/null
)
test ! -e "$merged_worktree"
if git -C "$repository" show-ref --verify --quiet refs/heads/merged-slice; then
  echo "Merged branch was not deleted." >&2
  exit 1
fi

git -C "$repository" worktree add -q -b unmerged-slice "$unmerged_worktree"
printf 'unmerged\n' >>"$unmerged_worktree/state.txt"
git -C "$unmerged_worktree" add state.txt
git -C "$unmerged_worktree" commit -q -m "unmerged slice"

if (
  cd "$repository"
  "$cleanup_script" --apply "$unmerged_worktree" unmerged-slice main
) >/dev/null 2>&1; then
  echo "Unmerged worktree cleanup should have failed." >&2
  exit 1
fi
test -d "$unmerged_worktree"

git -C "$repository" worktree add -q -b dirty-slice "$dirty_worktree" main
printf 'untracked\n' >"$dirty_worktree/untracked.txt"
if (
  cd "$repository"
  "$cleanup_script" --apply "$dirty_worktree" dirty-slice main
) >/dev/null 2>&1; then
  echo "Dirty worktree cleanup should have failed." >&2
  exit 1
fi
test -d "$dirty_worktree"

if (
  cd "$repository"
  "$cleanup_script" --apply "$repository" "" main
) >/dev/null 2>&1; then
  echo "Primary worktree cleanup should have failed." >&2
  exit 1
fi

echo "cleanup_worktree tests passed"
