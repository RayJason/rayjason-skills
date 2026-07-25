# Documentation lifecycle

Update documentation when behavior, operations, contracts, or project direction
changed. Avoid documentation churn for trivial implementation details.

## Active task state

First inspect the repository and connected project tools for existing progress
management, including task files, roadmap documents, documentation indexes,
issues, milestones, and project boards. Report what exists, what is current,
and what overlaps.

Then ask whether the user wants project progress managed through documentation.
If yes, reuse the existing source of truth. If none exists, offer a minimal
choice of location and fields; do not create `tasks.md`, a roadmap, or another
tracker until the user chooses one.

In the selected tracker, keep:

- work in progress and near-term planned work;
- active blockers and owners;
- explicit next actions;
- acceptance and verification state.

Move completed or stale items to an archive, issue tracker, release note, or
history section when they remain useful. Do not silently erase audit-relevant
decisions.

## Roadmap and milestones

Update only when completion changes delivery status, order, scope, or strategy.
Separate committed milestones from ideas and explicitly label uncertainty.

## Durable technical documentation

After a complex feature, cover the applicable parts:

- goal and non-goals;
- architecture and module ownership;
- data and control flow;
- public interfaces and compatibility;
- security, permissions, and sensitive-data handling;
- decisions and tradeoffs;
- operations, observability, and troubleshooting;
- migration and rollback;
- known risks.

Document the final implementation and real operating path. Mark proposed,
simulated, unreleased, or unavailable behavior explicitly.

## Synchronization check

A task is synchronized only when relevant code, tests, schema, configuration,
generated artifacts, and project documents agree. Record skipped documentation
when no durable artifact changed.

## Scheduled governance

After a successful one-time governance pass, ask whether the user wants
recurring governance for:

- global instructions and installed skills;
- project `AGENTS.md` and host adapters such as `CLAUDE.md`;
- both scopes; or
- neither.

Do not create a schedule from silence or a generic interest in automation.
Confirm cadence, target projects, execution surface, local versus isolated
worktree behavior, permissions, and whether runs only report or may apply
changes. Default to a weekly, report-only audit. Test the prompt manually and
review early runs before allowing edits. Deleting or replacing skills and
editing shared rules always require the authority selected by the user.
