---
type: question_bank
topic: agent-engineer
status: curated
updated: 2026-06-12
tags:
  - agent
  - rag
  - tool-calling
  - interview
---

# Agent 工程师核心题库


### 1. 什么是 AI Agent？它和普通 Chatbot 有什么区别？

考点：Agent loop、工具调用、状态管理、任务完成判断。

追问：

- Agent 的终止条件怎么设计？
- 自主性越高一定越好吗？
- 你会如何限制 Agent 的行动范围？

### 2. Function calling / tool calling 的作用是什么？

考点：结构化输出、API 调用、可靠性和安全。

追问：

- 模型生成的 tool arguments 能直接用吗？
- 工具调用失败如何恢复？
- 为什么要考虑幂等性？

### 3. RAG 的基本流程是什么？

考点：索引、检索、重排、上下文构造、答案验证。

追问：

- 为什么需要 rerank？
- chunk size 怎么选？
- 答案不准时你先排查哪里？

### 4. Agent 的 memory 应该怎么设计？

考点：state vs memory、长期记忆、隐私、安全、过期。

追问：

- 哪些内容不应该写入 memory？
- 用户要求删除记忆怎么办？
- 如何避免错误记忆影响后续任务？

## Intermediate

### 5. 如何设计一个能操作 GitHub Issues 的 Coding Agent？

考点：权限、工具、状态流、审计、human-in-the-loop。

优秀回答结构：

1. 明确可执行动作：读 issue、检索代码、开分支、改代码、跑测试、创建 PR。
2. 工具注册和权限隔离：读操作默认允许，写操作需要范围限制或确认。
3. 任务状态：issue -> plan -> patch -> test -> summary。
4. 失败恢复：测试失败、冲突、工具超时、权限不足。
5. 观测：保存 trace、diff、测试结果、token 和耗时。

### 6. RAG 系统答案不准，你怎么定位问题？

考点：retrieval/generation 分层排查。

优秀回答结构：

1. 固定问题和期望答案，复现失败。
2. 看检索结果是否包含答案。
3. 如果没有，查 chunking、metadata、embedding、召回参数、索引新鲜度。
4. 如果有但没答对，查 prompt、上下文排序、模型能力、引用约束。
5. 加入回归 eval，防止同类问题反复出现。

### 7. 什么时候用多 Agent，什么时候不用？

考点：任务拆分、上下文隔离、协作成本。

追问：

- 多 Agent 最大的问题是什么？
- 你如何设计 handoff？
- 如何评估多 Agent 是否真的提升效果？

## Advanced

### 8. 设计一个生产级 Agent 平台，需要哪些核心模块？

考点：平台架构、工具生态、权限、评估、观测、成本。

优秀回答结构：

1. 接入层：API、用户 session、鉴权。
2. 编排层：workflow、agent loop、router、planner。
3. 模型层：model router、prompt/template、structured output。
4. 工具层：tool registry、schema、permission、sandbox。
5. 状态和记忆：state store、memory store、检索。
6. 观测评估：trace、eval、feedback、cost/latency。
7. 安全治理：审批、审计、敏感操作拦截。

### 9. 如何防御来自网页或文档的 prompt injection？

考点：信任边界、数据/指令分离、工具权限。

追问：

- RAG 文档中写着“忽略系统指令”怎么办？
- 搜索结果要求你泄露 API key 怎么办？
- 哪些防线应该放在模型外？

### 10. 如果模型升级导致 Agent 行为回归，你怎么发现和处理？

考点：eval、灰度、回滚、trace diff。

追问：

- 你的 eval set 怎么构造？
- 如何比较两个模型的 trajectory？
- 如何决定是否上线新模型？
