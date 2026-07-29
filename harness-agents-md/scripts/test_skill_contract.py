#!/usr/bin/env python3

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILL_FILE = ROOT / "SKILL.md"
FALLBACK_FILE = ROOT / "assets" / "AGENTS.example.md"
SCENARIOS_FILE = ROOT / "evals" / "scenarios.json"
EXPECTED_FILES = {
    "SKILL.md",
    "assets/AGENTS.example.md",
    "evals/README.md",
    "evals/scenarios.json",
    "scripts/test_skill_contract.py",
}
ACTION = re.compile(r"\b(create|review|reorganize|optimize)\b", re.IGNORECASE)
TARGET = re.compile(r"\bAGENTS\.md\b|\bagent instructions?\b", re.IGNORECASE)
GIT_NO_TRIGGER_IDS = {
    "ordinary-rebase",
    "ordinary-fast-forward",
    "ordinary-merge",
    "mention-agents-while-rebasing",
}


def fail(message: str) -> None:
    raise SystemExit(f"skill contract failed: {message}")


def normalized(text: str) -> str:
    return re.sub(r"\s+", " ", text).lower()


def validate_package() -> None:
    observed = {
        str(path.relative_to(ROOT))
        for path in ROOT.rglob("*")
        if path.is_file()
    }
    if observed != EXPECTED_FILES:
        fail(
            "package must stay minimal "
            f"(expected={sorted(EXPECTED_FILES)}, observed={sorted(observed)})"
        )


def validate_skill() -> None:
    text = SKILL_FILE.read_text()
    match = re.search(r'^description:\s*"([^"]+)"$', text, re.MULTILINE)
    if not match:
        fail("frontmatter description must be a quoted single line")
    description = match.group(1).lower()
    for term in (
        "explicit user requests",
        "create",
        "review",
        "reorganize",
        "optimize",
        "agents.md",
        "agent instructions",
        "only",
    ):
        if term not in description:
            fail(f"description is missing {term!r}")
    for term in (
        "git",
        "rebase",
        "merge",
        "release",
        "implementation",
        "engineering",
        "worktree",
        "multi-agent",
    ):
        if term in description:
            fail(f"description contains unrelated retrieval term {term!r}")

    body = text.split("---", 2)[-1]
    if len(body.splitlines()) > 40:
        fail("SKILL.md body must stay at or below 40 lines")
    compact = normalized(body)
    for phrase in (
        "ordinary git, release, implementation, and coding work is out of scope",
        "use it as the exact baseline",
        "preserve its language, terminology, thresholds, and intent",
        "do not mix in the packaged fallback",
        "use `assets/agents.example.md` as the engineering fallback and continue",
        "a project-only request",
        "does not authorize editing the global file",
        "change only the requested instruction scope",
        "do not invent generic workflows",
        "make the smallest useful change",
    ):
        if phrase not in compact:
            fail(f"SKILL.md is missing {phrase!r}")
    if "references/" in body:
        fail("SKILL.md must remain self-contained")


def validate_fallback() -> None:
    text = FALLBACK_FILE.read_text()
    if len(text.splitlines()) > 24:
        fail("engineering fallback must stay at or below 24 lines")
    compact = normalized(text)
    for phrase in (
        "never overwrite unrelated user changes",
        "keep each change and commit cohesive",
        "follow the repository's actual branch and validation rules",
        "delegate only independent, non-conflicting workstreams",
        "the coordinator owns decomposition, file and module ownership, "
        "integration, final review, and validation",
        "do not create fixed roles mechanically",
        "never assign concurrent agents to the same file or module",
        "one owner or serialize overlapping work",
        "workers run the smallest targeted check",
        "coordinator reviews the combined diff and runs focused final validation",
    ):
        if phrase not in compact:
            fail(f"fallback is missing {phrase!r}")
    for term in (
        "release matrix",
        "migration",
        "rollback",
        "roadmap",
        "schedule",
        "three review",
        "five or fewer",
    ):
        if term in compact:
            fail(f"fallback contains process machinery {term!r}")


def validate_scenarios() -> None:
    payload = json.loads(SCENARIOS_FILE.read_text())
    if payload.get("version", 0) < 4:
        fail("scenario corpus is stale")
    scenarios = payload.get("scenarios", [])
    ids = [scenario.get("id") for scenario in scenarios]
    if len(scenarios) < 9 or len(ids) != len(set(ids)) or any(not item for item in ids):
        fail("scenarios must be representative and uniquely identified")
    if {scenario.get("expected_trigger") for scenario in scenarios} != {True, False}:
        fail("scenarios must cover trigger and no-trigger behavior")

    for scenario in scenarios:
        for field in ("prompt", "expected_trigger", "critical_boundaries"):
            if field not in scenario:
                fail(f"{scenario.get('id')} is missing {field}")
        if scenario["expected_trigger"]:
            if not ACTION.search(scenario["prompt"]) or not TARGET.search(
                scenario["prompt"]
            ):
                fail(f"{scenario['id']} lacks an explicit action and target")
        elif scenario.get("expected_fallback"):
            fail(f"{scenario['id']} selects fallback without triggering")

    by_id = {scenario["id"]: scenario for scenario in scenarios}
    if not GIT_NO_TRIGGER_IDS.issubset(by_id):
        fail("ordinary Git no-trigger scenarios are missing")
    if any(by_id[item]["expected_trigger"] for item in GIT_NO_TRIGGER_IDS):
        fail("ordinary Git requests must not trigger")

    fallback = by_id.get("create-from-missing-global")
    if fallback is None or fallback.get("expected_fallback") != (
        "assets/AGENTS.example.md"
    ):
        fail("missing-global scenario must select the packaged fallback")
    boundaries = {
        boundary
        for scenario in scenarios
        for boundary in scenario["critical_boundaries"]
    }
    for boundary in (
        "present global source is the exact baseline",
        "preserve source language and thresholds",
        "select fallback and continue",
        "safe change preservation",
        "independent non-conflicting delegation",
        "coordinator owns integration and final validation",
        "exclusive file and module ownership",
        "focused worker checks",
        "no fixed agent roles",
    ):
        if boundary not in boundaries:
            fail(f"scenario coverage is missing {boundary!r}")


def main() -> None:
    validate_package()
    validate_skill()
    validate_fallback()
    validate_scenarios()
    print("skill contract tests passed")


if __name__ == "__main__":
    main()
