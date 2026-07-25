# Coordinator and worker workflow

These are roles, not product-specific features. One agent may perform both roles
sequentially when the host cannot delegate.

## Coordinator

The coordinator:

- owns the overall goal and acceptance criteria;
- decomposes work into bounded, independently verifiable slices;
- identifies dependencies, file ownership, and shared-state conflicts;
- assigns work only when delegation reduces risk or latency;
- maintains integration and progress state;
- reviews diffs and verification evidence before acceptance;
- integrates changes and updates durable project state.

## Worker

A worker:

- stays within assigned paths and authority;
- preserves unrelated user changes;
- reports assumptions, discovered conflicts, and scope gaps;
- does not publish, deploy, delete, or expand scope without authority;
- verifies the assigned slice;
- commits only when the coordinator or repository policy requires it;
- returns a concise completion report.

## Delegation packet

```md
- Goal and acceptance criteria:
- Allowed paths:
- Forbidden paths:
- Inputs and dependencies:
- Expected output:
- Required verification:
- Approval boundaries:
- Commit expectation:
```

## Completion report

```md
- Outcome:
- Changed files:
- Verification passed:
- Verification skipped or blocked:
- External effects:
- Risks and follow-up:
- Commit:
```

Parallelize only independent scopes. Assign one integration owner for shared
interfaces, schema, lockfiles, generated artifacts, and documentation indexes.
Never accept a worker's statement as evidence without inspecting the result.
