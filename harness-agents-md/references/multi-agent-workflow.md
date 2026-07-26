# Bounded multi-agent control

Coordinator and worker are task roles, not a required team shape. One agent may
perform both roles sequentially when delegation is unavailable or coordination
would cost more than it saves.

## Why the loop needs bounds

A roughly 17-hour engineering run with 85 commits and 190 changed files showed
that more workers were not the limiting factor. Repeated full checks, unbounded
review loops, overlapping ownership, shared WIP, candidate drift, and polluted
consumer checks consumed the expected parallel gain.

Treat coordination and verification as finite shared budgets. Control a few
observable states—workstream independence, owner, evidence level, review round,
and candidate identity—instead of adding a rule for every past failure.

## Core control policies

### MA-DELEGATE — Delegate only independent work

- **Trigger:** Two or more workstreams can progress without shared writes,
  mutable state, or an unresolved interface.
- **Control:** Define acceptance criteria and dependencies first. Choose agent
  count and roles from the independent workstreams; keep concurrent subagents at
  five or fewer by default and verify resources before exceeding that limit.
- **Stop or override:** Keep work with the coordinator when it is small,
  sequential, discovery-heavy, or concentrated in one module. Never create a
  fixed implementer/reviewer/release trio mechanically.

### MA-OWNER — Keep one concurrent owner

- **Trigger:** Before dispatch and whenever a workstream changes scope.
- **Control:** Assign one concurrent owner per file, module, and shared mutable
  state. Record dependencies, forbidden paths, integration order, and local
  evidence. A worktree provides Git isolation, not logical independence.
- **Stop or override:** Stop and serialize when ownership overlaps, shared WIP
  makes attribution ambiguous, or an interface is not stable. End completed
  workers promptly.

### MA-VERIFY — Match evidence to integration level

- **Trigger:** A worker finishes its slice or the coordinator completes a
  cohesive module integration.
- **Control:** A worker runs only the smallest targeted behavior or red-to-green
  check for its change. It does not run the full repository test suite, build,
  E2E, generated-project matrix, database matrix, or release gate. After
  integration, the coordinator runs one focused module validation. Formatting,
  linting, and typechecking are static checks, not tests; do not rerun tests
  after every small commit.
- **Stop or override:** TDD, bug reproduction, and high-risk regressions may
  justify additional targeted worker checks. If the integrated path changes,
  invalidate affected evidence; full repository gates remain coordinator-owned.

### MA-REVIEW — Bound feedback rounds

- **Trigger:** All workstreams for one cohesive module are integrated.
- **Control:** Integrate contracts and foundations before dependents, generated
  outputs, consumers, documentation, and release metadata. The coordinator
  performs one consolidated review, returns findings together, and re-reviews
  only affected paths. Allow at most three review-to-fix rounds.
- **Stop or override:** After round three, preserve remaining evidence and ask
  the user to choose scope reduction, risk acceptance, or redesign. Do not keep
  an audit-to-fix loop open indefinitely.

### MA-RELEASE — Freeze identity before the full gate

- **Trigger:** An actual, authorized release is ready for final verification.
- **Control:** Freeze candidate SHA and managed-file layout, build one exact
  artifact, and carry it through CI evidence, historical upgrades, and
  publication. Run the full test/build/release matrix once at this point. Smoke
  test the published artifact from a non-workspace directory and verify declared
  version, resolved version, integrity, and commit SHA without workspace or
  cache substitution.
- **Stop or override:** Any code, layout, lockfile, or artifact change
  invalidates downstream evidence and requires a new candidate. Repeat the full
  gate only when the user requests it or a high-risk failure invalidates prior
  evidence. Publication, deployment, and external changes still require their
  own authority.

## Operating record

Use one compact owner matrix:

| Workstream | Owner | Scope | Dependencies/shared state | Worker evidence | Integration order | State |
| --- | --- | --- | --- | --- | --- | --- |
| Example | agent-a | `packages/example/**` | stable public API; root lockfile forbidden | targeted unit check | after API owner | active |

The coordinator owns the goal, matrix, shared state, integration, consolidated
review, module validation, and release gate. A worker owns only its assigned
scope, targeted evidence, and early reporting of dependency or authority drift.

Each delegation and completion record should contain:

```md
- Goal and acceptance criteria:
- Owner, allowed scope, and forbidden shared state:
- Inputs, dependencies, and integration position:
- Smallest worker-local evidence:
- Approval and commit boundaries:
- Outcome, blocked evidence, risks, and commit:
```

Inspect worker diffs and observed evidence before accepting the result.
