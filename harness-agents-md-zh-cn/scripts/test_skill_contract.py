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
ACTION = re.compile(r"创建|审查|重组|优化")
TARGET = re.compile(r"AGENTS\.md|Agent\s*指令|代理指令", re.IGNORECASE)
GIT_NO_TRIGGER_IDS = {
    "ordinary-rebase",
    "ordinary-fast-forward",
    "ordinary-merge",
    "mention-agents-while-rebasing",
}
GIT_PROMPT_TERMS = {
    "ordinary-rebase": ("rebase",),
    "ordinary-fast-forward": ("fast-forward",),
    "ordinary-merge": ("合并",),
    "mention-agents-while-rebasing": ("agents.md", "rebase", "fast-forward"),
}


def fail(message: str) -> None:
    raise SystemExit(f"Skill 契约失败：{message}")


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
            "包必须保持精简 "
            f"(expected={sorted(EXPECTED_FILES)}, observed={sorted(observed)})"
        )


def validate_skill() -> None:
    text = SKILL_FILE.read_text()
    name = re.search(r"^name:\s*(\S+)$", text, re.MULTILINE)
    if not name or name.group(1) != "harness-agents-md-zh-cn":
        fail("frontmatter name 必须匹配中文包标识符")
    match = re.search(r'^description:\s*"([^"]+)"$', text, re.MULTILINE)
    if not match:
        fail("frontmatter description 必须是单行引号字符串")
    description = match.group(1).lower()
    for term in (
        "仅用于用户明确要求",
        "创建",
        "审查",
        "重组",
        "优化",
        "agents.md",
        "agent 指令",
    ):
        if term not in description:
            fail(f"description 缺少 {term!r}")
    for term in (
        "git",
        "rebase",
        "merge",
        "合并",
        "发布",
        "实现",
        "工程",
        "worktree",
        "多 agent",
        "子 agent",
    ):
        if term in description:
            fail(f"description 包含无关检索词 {term!r}")

    body = text.split("---", 2)[-1]
    if len(body.splitlines()) > 40:
        fail("SKILL.md 正文不得超过 40 行")
    compact = normalized(body)
    for phrase in (
        "普通 git、发布、实现和编码 工作不在范围内",
        "将其作为精确基准",
        "保留其语言、 术语、阈值和意图",
        "不要混入内置 fallback",
        "使用 `assets/agents.example.md` 作为工程 fallback 并继续",
        "仅针对项目的请求",
        "不 授权修改全局文件",
        "只修改用户要求的指令范围",
        "不要编造通用工作流",
        "做最小且有用的修改",
    ):
        if phrase not in compact:
            fail(f"SKILL.md 缺少 {phrase!r}")
    if "references/" in body:
        fail("SKILL.md 必须保持自包含")


def validate_fallback() -> None:
    text = FALLBACK_FILE.read_text()
    if len(text.splitlines()) > 24:
        fail("工程 fallback 不得超过 24 行")
    compact = normalized(text)
    for phrase in (
        "绝不覆盖无关的用户修改",
        "每次修改和提交都保持单一内聚",
        "遵循仓库实际的分支和验证规则",
        "只委派相互独立且不冲突的工作流",
        "主 agent（协调者）负责拆分、文件和模块 所有权、集成、最终审查与验证",
        "不要机械设置固定角色",
        "不得让多个 agent 并发修改同一文件或模块",
        "只有一个所有者，否则 顺序执行重叠工作",
        "执行 agent 只运行其工作所需的最小针对性检查",
        "协调者审查合并后的 diff， 并运行聚焦的最终验证",
    ):
        if phrase not in compact:
            fail(f"fallback 缺少 {phrase!r}")
    for term in (
        "发布矩阵",
        "迁移清单",
        "回滚流程",
        "roadmap",
        "schedule",
        "三轮审查",
        "最多五个",
    ):
        if term in compact:
            fail(f"fallback 包含流程机制 {term!r}")


def validate_scenarios() -> None:
    payload = json.loads(SCENARIOS_FILE.read_text())
    if payload.get("skill") != "harness-agents-md-zh-cn":
        fail("场景 skill 标识符错误")
    scenarios = payload.get("scenarios", [])
    ids = [scenario.get("id") for scenario in scenarios]
    if len(scenarios) < 9 or len(ids) != len(set(ids)) or any(not item for item in ids):
        fail("场景必须具有代表性且 ID 唯一")
    if {scenario.get("expected_trigger") for scenario in scenarios} != {True, False}:
        fail("场景必须同时覆盖触发和不触发")

    for scenario in scenarios:
        for field in ("prompt", "expected_trigger", "critical_boundaries"):
            if field not in scenario:
                fail(f"{scenario.get('id')} 缺少 {field}")
        if scenario["expected_trigger"]:
            if not ACTION.search(scenario["prompt"]) or not TARGET.search(
                scenario["prompt"]
            ):
                fail(f"{scenario['id']} 缺少明确动作和指令目标")
        elif scenario.get("expected_fallback"):
            fail(f"{scenario['id']} 在未触发时选择了 fallback")

    by_id = {scenario["id"]: scenario for scenario in scenarios}
    if not GIT_NO_TRIGGER_IDS.issubset(by_id):
        fail("缺少普通 Git 不触发场景")
    if any(by_id[item]["expected_trigger"] for item in GIT_NO_TRIGGER_IDS):
        fail("普通 Git 请求不得触发")
    for scenario_id, terms in GIT_PROMPT_TERMS.items():
        prompt = by_id[scenario_id]["prompt"].lower()
        if any(term not in prompt for term in terms):
            fail(f"{scenario_id} 不再覆盖预期的普通 Git 请求")

    fallback = by_id.get("create-from-missing-global")
    if fallback is None or fallback.get("expected_fallback") != (
        "assets/AGENTS.example.md"
    ):
        fail("缺失全局指令时必须选择内置 fallback")
    boundaries = {
        boundary
        for scenario in scenarios
        for boundary in scenario["critical_boundaries"]
    }
    for boundary in (
        "现有全局指令是精确基准",
        "保留源语言和阈值",
        "选择 fallback 并继续",
        "保护无关修改",
        "只委派独立且不冲突的工作流",
        "协调者负责集成和最终验证",
        "文件和模块排他所有权",
        "执行 Agent 运行最小针对性检查",
        "不机械设置固定角色",
    ):
        if boundary not in boundaries:
            fail(f"场景覆盖缺少 {boundary!r}")


def main() -> None:
    validate_package()
    validate_skill()
    validate_fallback()
    validate_scenarios()
    print("Skill 契约测试通过")


if __name__ == "__main__":
    main()
