---
type: source_note
source_type: feishu_screenshot
status: extracted
topic: agent-definition-boundary
updated: 2026-06-12
tags:
  - agent
  - feishu
  - screenshot
---

# 原始截图摘录 - 01 Agent定义、边界与适用场景

来源截图：`D:/Temp/codex-clipboard-a6c370ca-6d98-46bd-b471-1e5e321b465b.png`

说明：本文件保留截图可见内容的顺序化摘录，供后续和原文核对。不可见或被截断的内容不做原文补全。

## 1. 页面信息

- 标题：01 Agent定义、边界与适用场景
- 修改时间：6月10日修改

## 2. 可见章节顺序

1. 这一题在面试里到底考什么
2. 什么是 Agent：从会回答到会完成任务
3. 什么不算 Agent：边界比定义更重要
4. 为什么 Agent 会火：它到底解决了什么问题
5. Guardrails / Governance
6. Evaluator / Verifier
7. Agent 的自治程度：不要把全自动当成唯一答案
8. Agent 适合什么场景，不适合什么场景
9. 常见误区与纠偏
10. Agent 的最小运行闭环
11. 高频面试题与参考回答
12. 面试速记版
13. 参考资料与延伸阅读

## 3. Agent 定义相关可见要点

1. 围绕目标运行
2. 在执行过程中做决策
3. 借助外部能力推进任务
4. 持续运行直到终止条件满足

可见组件：

1. Goal / Task
2. Policy / Planner
3. Guardrails / Governance
4. Evaluator / Verifier

截图正文中可见定义方向：

> Agent 是一种围绕任务目标运行、能够在执行过程中根据中间观察结果决定后续动作，并借助工具或外部环境持续推进任务完成的系统。

## 4. Agent 边界相关可见要点

1. 普通 chatbot 不一定是 agent
2. 固定流程的 workflow 不一定是 agent
3. 只有 function calling 不足以构成 agent
4. 有记忆不等于 agent

## 5. Agent 适用场景相关可见要点

1. 场景一：任务路径事先不确定
2. 场景二：任务需要多轮环境交互
3. 场景三：任务规模超过单轮上下文

## 6. Agent 自治程度相关可见要点

1. Assisted Agent
2. Semi-Autonomous Agent
3. Autonomous Agent
4. Open-Ended Agent

可见判断：

- Agent 不一定要完全自治。
- 自治是连续谱，不是二元开关。
- 任务可以被拆成阶段，但阶段之间仍需动态协调。
- 只是为了看起来高级，是常见陷阱。

## 7. 常见误区相关可见要点

1. 误区一：用了工具就是 agent
   - 纠偏：工具增强型应用和 agent 的区别在于是否存在目标推进型运行循环，以及是否根据观察持续决策。
2. 误区二：agent 一定比 workflow 高级
3. 误区三：agent 就是把 prompt ...
4. 误区四：只要模型够强，就不...
5. 误区五：agent 的核心是思维链

## 8. 高频面试题可见列表

1. 什么是 Agent？和普通 LLM / chatbot 有什么区别？
2. 带 function calling 的聊天机器人算不算 agent？
3. Workflow 和 Agent 的区别是什么？
4. Agent 一定需要工具吗？
5. 什么时候你不会建议上 Agent？
6. 为什么大家总说 agent 难做？
7. Agent 的核心组件有哪些？
8. Agent 和 RAG 的关系是什么？
9. Agent 和多 agent 是一...（截图截断）
10. 怎样判断一个需求是否...（截图截断）

## 9. 可见参考回答摘录

### 题 2：带 function calling 的聊天机器人算不算 agent？

参考回答：不一定。如果只是一次性选择一个工具然后结束，更像 tool-augmented chatbot；如果系统会根据工具结果持续决策、多步推进任务，那就更接近 agent。

### 题 5：什么时候你不会建议上 Agent？

参考回答：任务路径清晰、规则强、结果必须稳定可控、错误代价高且可通过规则系统解决时，我更倾向于 workflow 或纯程序逻辑。

### 题 6：为什么大家总说 agent 难做？

参考回答：难点不在于让模型想一步，而在于如何在复杂环境里持续正确做事。包括工具可靠性、上下文污染、权限控制、长任务恢复、终止条件、评测与回放等。

### 题 7：Agent 的核心组件有哪些？

参考回答：目标、策略/规划、工具、状态/记忆、控制约束、结果校验。这六块缺一不可，尤其在生产环境里。

### 题 8：Agent 和 RAG 的关系是什么？

可见要点：不是所有任务都值得 agent 化，过度 agent 化是常见反模式。

## 10. 可见参考资料

1. Anthropic, Building effective agents, 2024。适合用来界定 agent 与 workflow 的边界，强调能用简单工作流解决时不要过度 agent 化。
2. Anthropic, Effective context engineering for AI agents, 2025。非常适合补充 agent 不只是 prompt engineering，而是 context engineering 的近年观点。
3. Anthropic, How we built our multi-agent research system, 2025。适合放在多 agent、任务拆解、subagent 协作章节中。
4. OpenAI, A practical guide to building agents, 2025。适合用作工具类型、agent 运行循环、单 agent 优先、多 agent 何时有意义的工程基线。
5. LangChain / LangGraph 官方文档：Workflows and agents、Multi-agent、Human-in-the-loop 等。

