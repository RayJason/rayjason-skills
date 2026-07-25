# Architecture and scope review

Before approving an agent plan, review:

1. Requirement, non-goals, and observable acceptance criteria.
2. Owning module, layer, and source of truth.
3. Public contracts and dependency direction.
4. Allowed and forbidden paths.
5. Cross-module, data, security, and operational side effects.
6. Test strategy against the real changed path.
7. Compatibility, migration, release, and rollback.
8. Long-term maintenance cost and ownership.

Prefer modules with stable public interfaces and private internal
implementations. Do not bypass an ownership boundary just because a direct edit
is faster.

A scoped task should declare:

```md
- Goal:
- Non-goals:
- Acceptance criteria:
- Owning module:
- Allowed paths:
- Forbidden paths:
- Public interfaces used or changed:
- Upstream dependencies:
- Downstream consumers:
- External or data side effects:
- Required approvals:
- Validation:
- Migration and rollback:
```

If the current repository state contradicts the proposed architecture, stop and
surface the evidence. Do not make the plan appear valid by editing unrelated
modules or documentation.
