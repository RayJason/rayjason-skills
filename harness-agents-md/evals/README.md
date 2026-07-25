# Behavior evaluations

`scenarios.json` is the host-neutral behavior corpus for
`harness-agents-md`. It covers:

- positive, negative, and ambiguous discovery cases;
- the references expected after discovery;
- safety and evidence boundaries that must remain observable.

## Deterministic contract check

Run:

```bash
python3 scripts/test_skill_contract.py
```

from the skill directory, or use the repository-root command in the main
`README.md`.

The check validates the public package contract:

- discovery metadata has positive and negative boundaries;
- the entrypoint stays lean and uses conditional reference routing;
- every routed reference exists;
- the scenario corpus covers both trigger and no-trigger behavior.

It does not claim that a model followed the skill.

## Host behavior run

For each supported host and model:

1. Start a clean session with the skill installed.
2. Submit each scenario's `prompt` without naming the skill.
3. Record whether the skill triggered.
4. Record which reference files were loaded.
5. Compare the response and proposed actions with `critical_boundaries`.
6. Repeat after changing discovery metadata or the entrypoint.

An optimization is acceptable only when discovery and boundary results are
equivalent or better across the supported host/model set. Report unsupported
inspection facilities instead of guessing which context loaded.
