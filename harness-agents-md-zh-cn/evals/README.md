# 行为契约

`scenarios.json` 覆盖本 Skill 的精简公开契约：

- 明确的创建、审查、重组和优化请求会触发；
- 普通 Git、发布、实现和多 Agent 工作不会触发；
- 存在全局指令时忠实沿用；
- 缺失全局指令时选择内置工程 fallback；
- fallback 保留无关修改，并维持简短的委派边界。

运行：

```bash
python3 scripts/test_skill_contract.py
```

确定性测试检查元数据、入口、包大小、fallback 和场景覆盖。它不能证明模型一定
遵循了 Skill；发现逻辑变化时，应使用这些场景执行宿主/模型行为检查。
