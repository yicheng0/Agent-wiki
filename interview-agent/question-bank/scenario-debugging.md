---
type: question_bank
topic: debugging
status: curated
updated: 2026-06-12
tags:
  - debugging
  - production
  - agent
  - reliability
---

# 场景题和故障排查

## 1. Agent 调错工具了

问题：用户让 Agent 查询订单状态，但 Agent 调用了退款工具，你怎么设计防线？

考点：

- 工具权限分级
- intent 到 tool 的路由校验
- 高风险工具确认
- 参数验证
- trace 和审计

追问：

- 如果模型坚持调用错误工具怎么办？
- 怎么在测试里覆盖这个场景？
- 哪些工具应该永远需要人工确认？

## 2. RAG 检索到了无关文档

问题：用户问产品退款政策，检索结果却是登录问题排查文档，你怎么定位？

考点：

- query rewrite
- chunk granularity
- metadata filter
- hybrid search
- rerank
- eval set

追问：

- 如果向量召回 top10 都不相关，你怎么处理？
- 如果 top10 相关但最终答案错了呢？
- 如何设计自动化评估指标？

## 3. Agent 长任务跑偏

问题：Coding Agent 本来要修一个 bug，结果开始重构无关模块，怎么办？

考点：

- goal boundary
- step limit
- plan review
- diff scope check
- human-in-the-loop

追问：

- 如何判断修改是否越界？
- 如何让 Agent 在每一步重新对齐目标？
- 什么时候应该停止任务并请求用户确认？

## 4. Tool API 间歇性失败

问题：外部工具接口 10% 概率超时，Agent 经常中断，你怎么优化？

考点：

- timeout
- retry/backoff
- idempotency key
- partial result
- fallback
- error summarization

追问：

- 哪些错误可以重试，哪些不该重试？
- 如何避免重复下单或重复发消息？
- 如何把错误返回给模型才有助于恢复？

## 5. Memory 召回了过期信息

问题：Agent 记住了用户以前用旧框架，现在用户项目已经迁移，Agent 还在按旧框架建议，怎么办？

考点：

- memory freshness
- confidence score
- write/read policy
- user visibility
- deletion/update

追问：

- 如何设计记忆过期策略？
- 用户纠正 Agent 后应该写入什么？
- memory 是否应该参与所有任务？
