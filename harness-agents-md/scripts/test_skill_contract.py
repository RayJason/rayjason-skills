#!/usr/bin/env python3

import json
import re
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parent.parent
SKILL_FILE = SKILL_ROOT / "SKILL.md"
SCENARIOS_FILE = SKILL_ROOT / "evals" / "scenarios.json"
WORKFLOW_FILE = SKILL_ROOT / "references" / "multi-agent-workflow.md"
REFERENCE_PATTERN = re.compile(r"references/[a-z0-9-]+\.md")
POLICY_SECTION_PATTERN = re.compile(
    r"^### (MA-[A-Z]+)\b[^\n]*\n(?P<body>.*?)(?=^### |^## |\Z)",
    re.MULTILINE | re.DOTALL,
)
REQUIRED_MULTI_AGENT_POLICIES = {
    "MA-DELEGATE",
    "MA-OWNER",
    "MA-VERIFY",
    "MA-REVIEW",
    "MA-RELEASE",
}
REQUIRED_POLICY_FIELDS = (
    "**Trigger:**",
    "**Control:**",
    "**Stop or override:**",
)


def fail(message: str) -> None:
    raise SystemExit(f"skill contract failed: {message}")


def load_description(text: str) -> str:
    match = re.search(r'^description:\s*"([^"]+)"$', text, re.MULTILINE)
    if not match:
        fail("frontmatter description must be a quoted single line")
    return match.group(1)


def validate_scenarios(skill_text: str) -> list[dict]:
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
        policies = scenario.get("expected_policies", [])
        if not isinstance(policies, list):
            fail(f"{scenario['id']} expected_policies must be a list")
        if len(policies) != len(set(policies)):
            fail(f"{scenario['id']} has duplicate expected_policies")
        if not scenario["expected_trigger"] and scenario["expected_references"]:
            fail(f"{scenario['id']} loads references without triggering")
        if policies and "references/multi-agent-workflow.md" not in scenario[
            "expected_references"
        ]:
            fail(f"{scenario['id']} expects policies without workflow reference")
        for relative_path in scenario["expected_references"]:
            if not (SKILL_ROOT / relative_path).is_file():
                fail(f"{scenario['id']} references missing file {relative_path}")
            if relative_path not in skill_text:
                fail(f"SKILL.md does not route to {relative_path}")

    return scenarios


def validate_multi_agent_contract(scenarios: list[dict]) -> None:
    sections = list(POLICY_SECTION_PATTERN.finditer(WORKFLOW_FILE.read_text()))
    policy_ids = [section.group(1) for section in sections]
    if len(policy_ids) != len(set(policy_ids)):
        fail("multi-agent workflow has duplicate policy ids")

    defined = set(policy_ids)
    if defined != REQUIRED_MULTI_AGENT_POLICIES:
        fail(
            "multi-agent workflow policy ids differ "
            f"(defined={sorted(defined)}, required="
            f"{sorted(REQUIRED_MULTI_AGENT_POLICIES)})"
        )

    for section in sections:
        missing_fields = [
            field
            for field in REQUIRED_POLICY_FIELDS
            if not re.search(
                rf"^- {re.escape(field)}[ \t]+\S",
                section.group("body"),
                re.MULTILINE,
            )
        ]
        if missing_fields:
            fail(f"{section.group(1)} has empty or missing fields {missing_fields}")

    observed_policies = {
        policy
        for scenario in scenarios
        for policy in scenario.get("expected_policies", [])
    }
    unknown_policies = observed_policies - REQUIRED_MULTI_AGENT_POLICIES
    if unknown_policies:
        fail(
            "multi-agent scenarios use unknown policies "
            f"{sorted(unknown_policies)}"
        )
    missing_coverage = REQUIRED_MULTI_AGENT_POLICIES - observed_policies
    if missing_coverage:
        fail(
            "multi-agent scenarios are missing policy coverage "
            f"{sorted(missing_coverage)}"
        )


def main() -> None:
    skill_text = SKILL_FILE.read_text()
    description = load_description(skill_text)
    lowered = description.lower()
    if not any(term in lowered for term in ("not for", "不用于", "不适用于")):
        fail("description must state a no-trigger boundary")
    if not any(
        term in lowered
        for term in (
            "complex",
            "long-running",
            "risky",
            "复杂",
            "长期",
            "高风险",
            "工程化",
        )
    ):
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

    scenarios = validate_scenarios(skill_text)
    validate_multi_agent_contract(scenarios)
    print("skill contract tests passed")


if __name__ == "__main__":
    main()
