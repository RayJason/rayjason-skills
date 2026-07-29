# Behavior evaluations

`scenarios.json` is the host-neutral behavior corpus for
`harness-agents-md`. It covers:

- explicit requests to create, review, reorganize, or optimize `AGENTS.md` and
  agent instructions;
- ordinary Git, release, worktree, implementation, and multi-agent requests
  that must not trigger the skill;
- global-instruction discovery, source-language preservation, minimal edits,
  and prohibition of unsolicited rules;
- exact fidelity when a global source exists versus selection of the packaged
  engineering fallback when it is confirmed missing;
- fallback coverage for Git/change safety, independent delegation, exclusive
  ownership, worker-local checks, and coordinator-owned integration and final
  validation;
- conditional reference routing after a valid trigger.

## Deterministic contract check

Run:

```bash
python3 scripts/test_skill_contract.py
```

from the skill directory, or use the repository-root command in the main
`README.md`.

The check validates the public package contract:

- discovery metadata requires an explicit instruction-editing request and
  excludes ordinary Git and coding work;
- every positive scenario names both an allowed action and an instruction
  target;
- Git/rebase/merge/fast-forward regression scenarios remain no-trigger cases;
- the entrypoint preserves a present global source without mixing in packaged
  defaults;
- a missing global source selects the operational engineering fallback instead
  of stopping at a report;
- the fallback keeps the intended Git, scope, and subagent collaboration rules
  without mechanical agent roles;
- routed references and the five stable multi-agent policy IDs remain valid.

It does not claim that a model followed the skill.

## Host behavior run

For each supported host and model:

1. Start a clean session with the skill installed.
2. Submit each scenario's `prompt` without naming the skill.
3. Record whether the skill triggered.
4. For valid triggers, record which references loaded and compare the response
   with `critical_boundaries`.
5. Repeat after changing discovery metadata or the entrypoint.

An optimization is acceptable only when explicit instruction-editing requests
still trigger, ordinary repository work does not, and fidelity boundaries are
equivalent or better. A confirmed missing global source must select the
packaged fallback; an inaccessible source must be reported as uncertain rather
than guessed.
