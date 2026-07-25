# Documentation lifecycle

Update documentation when behavior, operations, contracts, or project direction
changed. Avoid documentation churn for trivial implementation details.

## Active task state

Use the repository's existing tracker. Keep:

- work in progress and near-term planned work;
- active blockers and owners;
- explicit next actions;
- acceptance and verification state.

Move completed or stale items to an archive, issue tracker, release note, or
history section when they remain useful. Do not silently erase audit-relevant
decisions. Do not invent `tasks.md` when the repository uses another system.

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
