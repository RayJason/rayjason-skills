#!/usr/bin/env python3

import json
import re
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parent.parent
SKILL_FILE = SKILL_ROOT / "SKILL.md"
SCENARIOS_FILE = SKILL_ROOT / "evals" / "scenarios.json"
REFERENCE_PATTERN = re.compile(r"references/[a-z0-9-]+\.md")


def fail(message: str) -> None:
    raise SystemExit(f"skill contract failed: {message}")


def load_description(text: str) -> str:
    match = re.search(r'^description:\s*"([^"]+)"$', text, re.MULTILINE)
    if not match:
        fail("frontmatter description must be a quoted single line")
    return match.group(1)


def validate_scenarios(skill_text: str) -> None:
    payload = json.loads(SCENARIOS_FILE.read_text())
    scenarios = payload.get("scenarios", [])
    if len(scenarios) < 6:
        fail("provide at least six representative scenarios")

    trigger_values = {scenario.get("expected_trigger") for scenario in scenarios}
    if trigger_values != {True, False}:
        fail("cover both trigger and no-trigger behavior")

    ids = [scenario.get("id") for scenario in scenarios]
    if len(ids) != len(set(ids)) or any(not scenario_id for scenario_id in ids):
        fail("scenario ids must be present and unique")

    for scenario in scenarios:
        for field in ("prompt", "expected_references", "critical_boundaries"):
            if field not in scenario:
                fail(f"{scenario['id']} is missing {field}")
        if not scenario["expected_trigger"] and scenario["expected_references"]:
            fail(f"{scenario['id']} loads references without triggering")
        for relative_path in scenario["expected_references"]:
            if not (SKILL_ROOT / relative_path).is_file():
                fail(f"{scenario['id']} references missing file {relative_path}")
            if relative_path not in skill_text:
                fail(f"SKILL.md does not route to {relative_path}")


def main() -> None:
    skill_text = SKILL_FILE.read_text()
    description = load_description(skill_text)
    lowered = description.lower()
    if "not for" not in lowered:
        fail("description must state a no-trigger boundary")
    if not any(term in lowered for term in ("complex", "long-running", "risky")):
        fail("description must state a positive trigger")

    body = skill_text.split("---", 2)[-1]
    if len(body.splitlines()) > 100:
        fail("SKILL.md body must stay at or below 100 lines")
    if re.search(r"^Read `references/[^`]+`\.$", body, re.MULTILINE):
        fail("reference loading must be conditional, not unconditional")

    mentioned = set(REFERENCE_PATTERN.findall(body))
    available = {
        str(path.relative_to(SKILL_ROOT))
        for path in (SKILL_ROOT / "references").glob("*.md")
    }
    if mentioned != available:
        fail(
            "route table must mention every reference exactly by path "
            f"(mentioned={sorted(mentioned)}, available={sorted(available)})"
        )

    validate_scenarios(skill_text)
    print("skill contract tests passed")


if __name__ == "__main__":
    main()
