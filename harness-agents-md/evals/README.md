# Behavior contract

`scenarios.json` covers the skill's small public contract:

- explicit create, review, reorganize, and optimize requests trigger;
- ordinary Git, release, implementation, and multi-agent work does not;
- a present global source is followed faithfully;
- a missing global source selects the packaged engineering fallback; and
- the fallback preserves unrelated work and keeps delegation boundaries short.

Run:

```bash
python3 scripts/test_skill_contract.py
```

The deterministic test validates metadata, the entrypoint, package size, the
fallback, and scenario coverage. It does not claim that a model followed the
skill; use the scenarios for host/model behavior checks when discovery changes.
