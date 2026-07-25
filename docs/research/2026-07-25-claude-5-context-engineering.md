# Claude 5 上下文工程文章：对 `agent-repo-steward` 的借鉴

研究日期：2026-07-25

研究对象：

- X 原文：<https://x.com/trq212/article/2080710971228918066>
- Anthropic 官方转载：<https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models>
- 当前仓库：`agent-repo-steward/`

## 结论

值得借鉴，但不应把“删掉 80%”当作目标。

本仓库已经做对了文章最重要的一件事：`SKILL.md` 负责路由，详细内容拆到
`references/`，可靠操作放进脚本并配测试。这正是渐进披露和“用接口代替冗长示例”。

当前最值得补的不是继续拆 Markdown，而是：

1. 给 skill 建立行为评测，先证明精简不会降低安全性和交付质量；
2. 把 frontmatter 的 `description` 从功能摘要改成明确的触发条件；
3. 收窄 “Apply this workflow to any coding agent” 的适用范围，避免普通编码任务也加载整套治理流程；
4. 在评测证明有收益后，再把独立触发的“验证交付”和“worktree 清理”做成可组合的专用 skill。

安全、权限、发布边界不能因为模型能力增强而删除；自动记忆也不能替代版本库中的团队规则。

## 文章的核心论点

文章将新版模型的上下文工程变化归纳为六组迁移：

| 过去的做法 | 新建议 | 实际含义 |
| --- | --- | --- |
| 给大量绝对规则 | 让模型在边界内判断 | 删除会与用户意图、代码风格冲突的通用禁令，保留真正重要的边界 |
| 给很多工具调用示例 | 设计清晰接口 | 用参数、枚举、状态约束和返回值表达可用空间 |
| 所有说明预先加载 | 渐进披露 | 只在需要时加载 skill、reference 和延迟工具定义 |
| 在多处重复同一规则 | 简化工具描述 | 每条规则尽量只有一个权威位置 |
| 把经验持续写进 `CLAUDE.md` | 使用自动记忆 | 团队规则与模型自行积累的本机经验分开 |
| 只给简单 Markdown 规格 | 提供高保真参考物 | 测试、代码、HTML 原型和 rubric 都可以成为可验证的规格 |

作者进一步建议：

- `CLAUDE.md` 保持轻量，重点记录模型无法从仓库推断的 gotcha；
- skill 应是轻量入口，承载团队或产品特有的观点与知识；
- 长 skill 拆成按需加载的文件树；
- 精简必须依赖评测，而不是凭感觉删字。

## 事实核验与证据强度

### 1. “系统提示删掉 80%，编码评测没有可测损失”

这是 Anthropic 对 Claude Code 内部实践的第一方陈述，X 原文也已在 Claude 官方博客
发布。它可以证明 Anthropic 报告了这个结果，但官方没有公开这里使用的完整提示、
评测集、分模型结果或置信区间，因此无法在本仓库独立复现。

结论：把它视为“应该尝试评测驱动的精简”，不能把 80% 视为通用目标。

来源：

- <https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models>
- <https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents>

### 2. 渐进披露是 Agent Skills 的正式加载模型

Claude Platform 文档把 skill 加载分成元数据、触发后加载 `SKILL.md`、按需访问资源三个
层次；Claude Code 文档也说明 skill 一旦加载，其正文会在后续轮次持续占用上下文，
因此正文应保持精简，详细参考和模板应放在 supporting files。

结论：文章的建议不是单纯风格偏好，而是与产品加载机制一致。

来源：

- <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview>
- <https://code.claude.com/docs/en/slash-commands>
- <https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>

### 3. `description` 是触发接口，不只是给人看的摘要

Anthropic 总结内部数百个 skill 时明确指出，模型在启动时扫描每个 skill 的
`description` 来决定是否加载，因此 description 应写“何时使用”；同一文章还指出，
最好的 skill 通常落在一个清晰类别中，跨多个类别的 skill 更容易让模型困惑。

结论：这是当前仓库最直接、改动最小的改进点。

来源：

- <https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills>

### 4. 自动记忆存在，但与项目指令不是替代关系

Claude Code 文档说明：

- `CLAUDE.md` 由团队维护，用于项目规则、工作流和架构；
- auto memory 由 Claude 自行维护，用于它发现的命令、调试经验和偏好；
- auto memory 是本机、按仓库存储的，不随版本库跨机器共享；
- 多步流程应移到 skill 或路径作用域规则，`CLAUDE.md` 应具体、简洁、无冲突。

结论：本仓库可以继续建议使用 auto memory，但不能把权威治理策略搬出版本库。

来源：

- <https://code.claude.com/docs/en/memory>

### 5. `/doctor` 是 Claude Code 专用、并且行为随版本演进

7 月 24 日官方文章称 `/doctor` 已可帮助精简 skill 和 `CLAUDE.md`。现有配置调试文档
仍主要将它描述为安装、配置、schema、MCP 和上下文使用诊断工具。这更像是刚发布的
能力或文档尚未完全同步，不应假设所有 Claude Code 版本都有同样行为，更不能扩展为
Codex、CodeBuddy 或 WorkBuddy 的通用能力。

来源：

- <https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models>
- <https://code.claude.com/docs/en/debug-your-config>
- <https://code.claude.com/docs/en/changelog>

### 6. 精简前需要 skill 行为评测

Anthropic 的企业 Skills 指南建议每个 skill 至少提供 3–5 个代表查询，覆盖应触发、
不应触发和模糊边界，并在实际使用的不同模型上测试。其 agent eval 指南也强调，
没有评测时容易在修一个失败的同时制造另一个失败。

结论：本仓库当前只有格式、shell 语法和 cleanup 脚本测试；这些能验证包与代码，
不能证明模型是否在正确场景触发 skill、是否选择了正确 reference、是否仍守住安全边界。

来源：

- <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise>
- <https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents>

## 对当前仓库的评估

### 已经值得保留的设计

1. **渐进披露已经成形**

   `agent-repo-steward/SKILL.md` 为 148 行，八份主题 reference 分别处理 host 兼容、
   项目指令、安全、架构、协作、文档、worktree、验证交付。详细内容不是全部堆在入口。

2. **代码承担了确定性工作**

   `scripts/cleanup_worktree.sh` 用明确参数表达目标，默认只预览，必须显式传
   `--apply` 才执行；`test_cleanup_worktree.sh` 覆盖已合并、未合并、脏 worktree 和
   primary worktree 等边界。这比让模型每次临时重写清理命令可靠。

3. **安全边界与自然语言建议分层**

   skill 已明确说明 Markdown 不是强制执行边界，必须依赖 sandbox、权限、hook、CI 和
   branch protection。这与 Claude Code 官方文档对 `CLAUDE.md` 与 permissions/hooks
   的区分一致。

4. **跨 host 适配器足够薄**

   `CLAUDE.example.md` 和 `CODEBUDDY.example.md` 指向同一个 `AGENTS.md` 权威来源，
   没有复制整套规则，降低了漂移风险。

5. **内容具有明确观点**

   “真实运行路径优先于文件名或模拟证据”“不要把已实现写成已发布”“worker 声明不是
   验证”等内容是本 skill 的核心判断，不是模型从任意代码库都能可靠推断的常识。

### 当前主要差距

1. **触发面过宽**

   frontmatter description 目前是能力清单：
   “scope, delegation, safety, verification, documentation, dependency handoffs,
   and worktree hygiene”，没有说明何时应该、何时不应该触发。

   正文第一句 “Apply this workflow to any coding agent” 也容易把复杂治理流程应用到
   一行修复或只读解释任务。

2. **一个 skill 横跨过多独立任务**

   它同时承担指令治理、架构评审、多 agent 协作、文档生命周期、worktree 操作和发布
   验证。它们在复杂项目治理中有关联，但“安全清理一个 worktree”和“审查发布证据”
   本身有独立触发条件。

3. **入口与 reference 仍有重复**

   `SKILL.md` 对 scope、worker、文档、worktree、验证分别列出较完整规则，reference
   再次展开同一主题。入口应该保留跨主题不变量和路由条件，具体清单尽量只存在于一个
   权威文件。

4. **缺少行为评测**

   当前校验能证明 Markdown 结构有效、脚本语法正确、清理保护生效；不能回答：

   - 普通小修是否错误触发整套治理；
   - 发布任务是否一定加载 verification reference；
   - 未授权生产操作是否被识别并暂停；
   - 非 Claude host 是否会误用 `/doctor`、auto memory 等 Claude 专属机制；
   - 精简前后在不同模型上的结果是否等价。

5. **缺少从真实失败沉淀的显式 gotcha**

   现有内容包含许多正确原则，但未区分“通用预防性规则”和“真实发生过、反复导致失败的
   gotcha”。后者应成为最优先保留的高信号内容。

## 建议的改进顺序

### P0：先建评测基线，再精简

至少建立以下六类场景：

1. 应触发：跨模块、带迁移和发布的复杂改动；
2. 应触发：验证实现、registry、部署和下游采用状态；
3. 应触发：清理 worktree，但目标未合并或仍有未跟踪文件；
4. 不应触发：一行代码修复，仓库已有明确测试命令；
5. 不应触发：只读解释或状态查询；
6. 模糊边界：用户要求并行，但任务共享 schema、lockfile 或文档索引。

每个场景至少评估：

- trigger / no-trigger 是否正确；
- 加载了哪份 reference；
- 是否保持授权、范围和不可逆操作边界；
- 最终声明是否与证据等级一致；
- 是否产生不必要的文档、分支或 worktree。

先记录当前版本结果，再对精简版做同样评测。没有等价或更好的结果，不合并精简。

### P1：重写 discovery 接口

把 description 改成模型可判定的触发条件，例如表达：

- 用于复杂、长期或多 agent 仓库工作的治理与交付；
- 用于指令来源冲突、跨模块范围、危险操作、worktree 生命周期、发布/下游证据；
- 不用于已有明确局部流程的普通小修或只读问答。

正文入口也应从“任何 coding agent 都应用整套流程”改成“根据任务选择适用路由”。

### P1：把 `SKILL.md` 收敛为不变量与路由表

入口建议只保留：

- host 能力与权威来源先确认；
- 不能越权、不能伪造能力或证据；
- 复杂任务明确目标、范围和验收；
- 一个按场景选择 reference 的路由表；
- 最终集成与证据责任。

架构清单、worker 模板、文档同步清单、worktree 步骤、验证证据模板各自只在对应
reference 中维护。

不建议直接追求 80% 缩减；应以评测结果确定能删多少。

### P2：只拆真正独立触发的 skill

在评测显示入口仍容易过度触发后，优先考虑两个独立 skill：

- `verify-and-handoff`：真实运行路径、发布层级、迁移、下游采用和回滚；
- `safe-worktree-cleanup`：调用现有脚本完成预览、检查、执行和结果报告。

`agent-repo-steward` 可以作为复杂治理的协调入口，需要时调用它们。安全/权限边界和
架构范围仍适合保留在核心治理 skill，不宜拆成可被遗漏的可选建议。

### P2：把真实 gotcha 与通用原则分开

为每条新增规则记录它来自哪类重复失败。优先保留：

- 模型无法从仓库推断的约束；
- 曾经重复造成事故或返工的边界；
- host 间真实不兼容；
- 运行、发布、registry、数据库或下游采用中的证据陷阱。

模型本就会做、且没有项目特异性的通用工程建议，应删除或下沉到可选 reference。

## 不建议照搬的部分

1. **不要把 80% 当 KPI。** 这是 Anthropic 在特定内部提示、模型和评测上的结果。
2. **不要删除安全与授权边界。** 文章本身也为高重要性区域保留强约束；本项目还要支持
   不同 host 和模型代际。
3. **不要用 auto memory 替代仓库政策。** 它是 Claude Code 本机经验层，不是团队共享
   的版本化真相。
4. **不要把 `/doctor` 写成跨 host 必备步骤。** 应继续执行当前的能力探测与降级策略。
5. **不要因为文章反对“示例驱动工具”就删除模板和脚本用法。** 当前 assets 是安装产物，
   cleanup 示例也是危险操作的明确接口，不是限制模型探索空间的 few-shot 提示。
6. **不要为了“富参考”强行引入 HTML artifact。** 本项目的高保真参考主要是脚本、测试、
   host 官方文档和可执行验证；HTML 对当前治理 skill 没有天然优势。

## 最终判断

这篇文章支持当前仓库的总体方向，但也暴露了一个关键矛盾：本 skill 一方面倡导渐进披露，
另一方面又试图成为所有 coding agent 的通用治理总入口。

最稳妥的演进不是马上大删，而是：

> 先用触发、边界和结果评测建立基线；再收窄 discovery；随后把入口变成路由器；最后仅把
> 具有独立触发条件的验证和 worktree 流程拆成可组合 skill。

这样可以获得文章所说的上下文效率，同时保留本项目真正有价值的跨 host、安全和证据纪律。
