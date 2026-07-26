# Verification and handoffs

Verification is an evidence chain, not a worker's confidence statement.

## Acceptance evidence

For each material criterion, record:

```md
- Criterion:
- Source of truth:
- Check or command:
- Environment:
- Observed result:
- Status: passed | failed | skipped | blocked
```

Required criteria with `failed`, `skipped`, or `blocked` status prevent a
verified-complete claim. Explain the impact and the next safe action.

## Minimum final review

- Inspect the final diff and preserve unrelated changes.
- Confirm repository status and commit scope when Git is available.
- Run the smallest checks that exercise the real changed path.
- Record command or check identity, environment, exit status, and meaningful
  observed output.
- Verify schema and migrations against executed order or a disposable instance.
- Verify generated artifacts from the generation pipeline.
- Verify published packages in the registry and consumer install path.
- Verify deployed behavior at the real endpoint after authorized deployment.

Do not substitute a filename, mock, stale document, or implementation diff for
runtime or delivery evidence.

For delegated verification and release gates, apply `MA-VERIFY` and
`MA-RELEASE` from `multi-agent-workflow.md`. Static checks may support the
evidence chain but are not tests.

## Upstream and downstream handoff

Separate these states:

1. implemented locally;
2. committed;
3. released or deployed;
4. available to consumers;
5. adopted and smoke-tested downstream.

Report the highest state actually evidenced. Include immutable version or commit
identity, compatibility impact, migration, consumer validation, and rollback.

For package publication, record the frozen candidate identity and verify the
consumer path outside the source workspace.

## Final report

List passed evidence, required checks not passed, external side effects,
migrations, known risks, and follow-up owner. Never describe a simulation,
fallback, or unavailable integration as the real capability.
