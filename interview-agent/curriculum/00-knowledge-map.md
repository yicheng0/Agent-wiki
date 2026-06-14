---
type: curriculum
topic: agent-interview
status: curated
updated: 2026-06-12
tags:
  - agent
  - interview
  - curriculum
---

# Agent 面试能力地图

## 1. Agent 基础

核心问题：

- 什么是 Agent？和普通 chatbot 有什么区别？
- Agent loop 由哪些步骤组成？
- 如何设计终止条件和失败恢复？

强回答要点：

- Agent 是围绕目标循环观察、决策、行动、更新状态的系统。
- 关键组件包括模型、上下文构造、状态、工具、记忆、控制流、终止条件和观测日志。
- 生产系统通常是 LLM + deterministic workflow 的混合，而不是完全让模型自由行动。

## 2. Tool / Function Calling

核心问题：

- tool calling 解决什么问题？
- 如何保证工具调用安全可靠？
- 模型生成的参数能不能直接信任？

强回答要点：

- 工具调用把模型意图转成结构化 API 调用。
- 必须有 schema、参数校验、权限边界、超时、重试、幂等、审计日志。
- 模型输出不可信，工具执行层要做确定性验证。

## 3. RAG

核心问题：

- RAG 的完整流程是什么？
- chunking、embedding、rerank 怎么选？
- 答案不准时如何定位 retrieval 还是 generation 问题？

强回答要点：

- RAG 流程包括 ingest、clean、chunk、embed、index、retrieve、rerank、context build、generate、verify。
- RAG 重点不是“塞更多上下文”，而是提高召回质量、上下文相关性和答案忠实度。
- 需要同时评估 retrieval recall、answer faithfulness、latency、cost。

## 4. Memory 和 State

核心问题：

- state 和 memory 有什么区别？
- 哪些内容不应该写入长期记忆？
- 如何避免 stale memory 和 prompt injection？

强回答要点：

- state 是当前任务上下文，memory 是跨任务复用的信息。
- 需要明确写入策略、读取策略、过期策略、用户可见性和删除能力。
- 来自网页、文档、工具返回的内容不能直接写入高权限记忆。

## 5. Planning 和 Orchestration

核心问题：

- 什么时候用 planner-executor？
- 什么时候用多 Agent？
- 哪些逻辑应该规则写死？

强回答要点：

- 稳定业务流程优先用确定性 workflow。
- 开放式、模糊、多步骤任务可以用 LLM planning。
- 多 Agent 适合职责清晰、上下文隔离、可并行的任务，不适合为了“看起来高级”而拆。

## 6. Evaluation 和 Observability

核心问题：

- 怎么评估一个 Agent 是否好用？
- 怎么评估长任务 trajectory？
- 模型升级导致行为回归怎么办？

强回答要点：

- 不只看最终答案，也要看路径、工具调用、错误恢复、成本和延迟。
- 需要离线 eval set、线上 traces、用户反馈、回归测试。
- 保存 prompt、model、tool args、tool output、latency、token、错误类型。

## 7. Safety 和 Security

核心问题：

- 如何防御 prompt injection？
- 如何处理敏感或不可逆操作？
- 如何设计最小权限？

强回答要点：

- 模型输出和外部内容都按不可信处理。
- 数据和指令要分离，工具层做权限控制。
- 高风险操作必须确认、审计、可回滚。

## 8. Coding 和工程实现

核心问题：

- 如何设计 Agent 后端 API？
- 如何实现工具注册和调用？
- 如何测试工具失败、超时、重试？

强回答要点：

- 接口要显式表达 session、state、tool call、trace 和权限。
- 工具层需要可测试的 mock/fixture。
- 关键路径要有单元测试、回归任务和集成测试。
