---
type: question_bank
topic: agent
source_type: xiaolinnote
status: reviewed
updated: 2026-06-12
tags:
  - xiaolinnote
  - interview
  - agent
---

# 小林面试题 - Agent

> 说明：本文件由 `tools/build_xiaolinnote_interview_cards.py` 从 `xiaolinnote-ai-qa.jsonl` 生成，属于外部资料整理层，未合并进手工精选题库。

## 1. 什么是 Agent？与大模型有什么本质不同？

- 来源：[https://xiaolinnote.com/ai/agent/1_whatisagent.html](https://xiaolinnote.com/ai/agent/1_whatisagent.html)
- 本地原文：`interview-agent/sources/xiaolinnote/agent/1_whatisagent.md`

### 考点

- Agent loop、自主规划、状态/记忆、工具执行、可靠性边界
- 普通大模型的局限性
- Agent 特别在哪？
- 为什么 Agent 现在才爆发？
- Agent 生态的最新趋势

### 核心理解

我理解 Agent 本质上是一个能自主完成目标的 AI 系统，跟传统 AI 最核心的区别在于「自主性」和「能行动」。
![[Pasted image 20260616215859.png]]
![[Pasted image 20260616215915.png]]
### 面试回答

我理解 Agent 本质上是一个能自主完成目标的 AI 系统，跟传统 AI 最核心的区别在于「自主性」和「能行动」。

传统 AI 是你问一个问题它回答一个问题，每次都是独立的，被动响应；而 Agent 有自己的规划能力，你给它一个复杂目标，它会自己把任务拆成多步，通过调工具、访问记忆、感知环境来一步步执行，直到完成。

它不只是输出文字，而是真的能做事。

### 工程例子

可以结合一个 Coding Agent 或运营助手来讲：用户给出目标后，系统先规划步骤，再调用搜索、文件、代码执行或 API 工具，每一步观察结果都会写回状态，并决定下一步继续、重试还是停止。

### 容易踩坑

- 回顾开头的对话，踩了三个典型的雷。
- 第一个雷是把 Agent 等同于「插件」或「工具调用」，这是最常见的误区，工具调用只是 Agent 能力的一部分，不是 Agent 本身。
- 第二个雷是停在「能调工具」这一层，没有点出自主性，Agent 的关键不是「有工具」，而是「自己决定用不用、什么时候用、用哪个」。

### 追问

1. 这个能力和普通 LLM / workflow / tool calling 的边界在哪里？
2. 如果 Agent 中途跑偏或工具失败，你会怎么恢复？
3. 生产环境里你会记录哪些 trace 来定位问题？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 2. Agent 的基本架构由哪些核心组件构成？

- 来源：[https://xiaolinnote.com/ai/agent/2_components.html](https://xiaolinnote.com/ai/agent/2_components.html)
- 本地原文：`interview-agent/sources/xiaolinnote/agent/2_components.md`

### 考点

- Agent loop、自主规划、状态/记忆、工具执行、可靠性边界
- LLM 核心
- 工具系统
- 记忆系统
- 规划模块

### 核心理解

我理解 Agent 的基本架构有四个核心组件：LLM、工具、记忆、规划模块。

### 面试回答

我理解 Agent 的基本架构有四个核心组件：LLM、工具、记忆、规划模块。

LLM 是整个系统的大脑，负责理解任务和做决策；工具让 Agent 能跟外部世界交互，搜索、执行代码、调 API 都靠它；记忆让 Agent 在任务执行过程中保持状态，不会「失忆」；规划模块负责把复杂目标拆解成可执行的步骤。

这四个组合在一起，才让 Agent 具备了自主完成任务的能力。

### 工程例子

可以结合一个 Coding Agent 或运营助手来讲：用户给出目标后，系统先规划步骤，再调用搜索、文件、代码执行或 API 工具，每一步观察结果都会写回状态，并决定下一步继续、重试还是停止。

### 容易踩坑

- 开头对话里踩了三个雷，面试时都要注意避开。
- 第一个雷是漏掉组件，很多人只说 LLM 和工具两个，把记忆和规划模块忘了，但这两个恰恰是让 Agent 能跑复杂任务的关键。
- 第二个雷是对记忆的理解太浅，「记忆就是上下文」这个回答不完整，正确的说法是记忆分两层：短期记忆放在 context window 里，存当前任务的中间状态；长期记忆用向量数据库实现，能跨任务保存用户偏好和历史，两者机制和用途完全不同。

### 追问

1. 这个能力和普通 LLM / workflow / tool calling 的边界在哪里？
2. 如果 Agent 中途跑偏或工具失败，你会怎么恢复？
3. 生产环境里你会记录哪些 trace 来定位问题？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 3. Workflow，Agent，Tools 这三个的概念和区别介绍一下？

- 来源：[https://xiaolinnote.com/ai/agent/3_workflow_tools.html](https://xiaolinnote.com/ai/agent/3_workflow_tools.html)
- 本地原文：`interview-agent/sources/xiaolinnote/agent/3_workflow_tools.md`

### 考点

- Agent loop、自主规划、状态/记忆、工具执行、可靠性边界
- 第一层：Tools，最小的能力积木
- 第二层：Agent，拿着工具自己做决定的人
- 第三层：Workflow，把所有人组织起来的总指挥
- 三者怎么组合？Agentic Workflow 才是生产主流

### 核心理解

我理解这三个概念是粒度从小到大的三层结构。

### 面试回答

我理解这三个概念是粒度从小到大的三层结构。

Tools 是最小的能力单元，就是封装好的可调用函数，比如搜索、执行代码、发邮件，它只负责「执行」，本身没有任何决策能力。

Agent 是一个完整的决策系统，内部用 LLM 做大脑，自己判断什么时候调哪个 Tool、要不要继续、什么时候结束，是主动的。

Workflow 是更上层的编排框架，把 Agent、LLM、Tools 组织成一条确定性流程，每个节点做什么、按什么顺序流转都是开发者事先写死的。

三者最核心的区别就一句话：Tools 不做决策只执行，Agent 自己做决策，Workflow 是开发者替所有节点把决策提前写好。

### 工程例子

可以结合一个 Coding Agent 或运营助手来讲：用户给出目标后，系统先规划步骤，再调用搜索、文件、代码执行或 API 工具，每一步观察结果都会写回状态，并决定下一步继续、重试还是停止。

### 容易踩坑

- 开头对话里最典型的误区是把 Workflow 理解成「多个 Agent 串联」，这个说法不对，Workflow 的节点可以是任意的 LLM 调用、Tools 或 Agent，关键不是节点类型，而是控制流由谁掌握——Workflow 是开发者在代码里写死的 if/else，Agent 是 LLM 动态决定的。
- 把 Agent 简化成普通工具调用，忽略自主规划和执行闭环。
- 只讲概念，不讲状态、记忆、终止条件和失败恢复。

### 追问

1. 这个能力和普通 LLM / workflow / tool calling 的边界在哪里？
2. 如果 Agent 中途跑偏或工具失败，你会怎么恢复？
3. 生产环境里你会记录哪些 trace 来定位问题？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 4. 了解哪些其他的 Agent 设计范式？Agent 和 Workflow的区别是什么？

- 来源：[https://xiaolinnote.com/ai/agent/4_patterns.html](https://xiaolinnote.com/ai/agent/4_patterns.html)
- 本地原文：`interview-agent/sources/xiaolinnote/agent/4_patterns.md`

### 考点

- Agent loop、自主规划、状态/记忆、工具执行、可靠性边界
- Workflow 和 Agent 的区别
- Agent 三种设计范式

### 核心理解

我理解 Agent 和 Workflow 最核心的区别是「谁来决定下一步」。Workflow 是我提前把流程写死的，每一步怎么走都是固定的，确定性高、好控制；Agent 是让 LLM 自己决定下一步做什么，灵活但不可控。

### 面试回答

我理解 Agent 和 Workflow 最核心的区别是「谁来决定下一步」。Workflow 是我提前把流程写死的，每一步怎么走都是固定的，确定性高、好控制；Agent 是让 LLM 自己决定下一步做什么，灵活但不可控。

常见的设计范式除了纯 Agent 之外，还有 ReAct、Plan-and-Execute、Reflection 这几种。

我在实际工程里用得最多的反而是把两者混用，固定流程的部分用 Workflow，需要灵活决策的节点嵌入 Agent 能力，这样既保住了整体可控，又有局部的灵活性。

### 工程例子

可以结合一个 Coding Agent 或运营助手来讲：用户给出目标后，系统先规划步骤，再调用搜索、文件、代码执行或 API 工具，每一步观察结果都会写回状态，并决定下一步继续、重试还是停止。

### 容易踩坑

- 开头对话里踩了三个雷，要重点记住。
- 第一个雷是设计范式不熟，ReAct 是最常见的，但 Plan-and-Execute（把规划和执行解耦）和 Reflection（执行后加自我评估环节）也是必须说出来的，三个范式各有适用场景。
- 第二个雷是把 Reflection 当调试手段，它是正式的运行时机制，内嵌在 Agent 的执行流程里，代价是增加 token 消耗和延迟，这个取舍在面试里经常被追问。

### 追问

1. 这个能力和普通 LLM / workflow / tool calling 的边界在哪里？
2. 如果 Agent 中途跑偏或工具失败，你会怎么恢复？
3. 生产环境里你会记录哪些 trace 来定位问题？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 5. Agent 推理模式有哪些？ReAct 是啥？具体是怎么实现的？

- 来源：[https://xiaolinnote.com/ai/agent/5_react.html](https://xiaolinnote.com/ai/agent/5_react.html)
- 本地原文：`interview-agent/sources/xiaolinnote/agent/5_react.md`

### 考点

- Agent loop、自主规划、状态/记忆、工具执行、可靠性边界
- 什么是推理模式？
- CoT是什么？
- ReAct 是什么？
- Plan-and-Execute：先规划再执行

### 核心理解

Agent 的推理模式我用过几种。

### 面试回答

Agent 的推理模式我用过几种。

最基础的是直接输出答案，没有中间推理；CoT 是让 LLM 先把推理过程写出来再给答案，准确率更高；ReAct 是在 CoT 基础上加了「行动」，让 LLM 交替输出思考和工具调用，每次行动后再根据结果继续思考，形成一个循环。

我觉得 ReAct 是目前 Agent 用得最广的模式，因为它推理过程可见，又能动态利用外部工具，两个优点都有。

### 工程例子

可以结合一个 Coding Agent 或运营助手来讲：用户给出目标后，系统先规划步骤，再调用搜索、文件、代码执行或 API 工具，每一步观察结果都会写回状态，并决定下一步继续、重试还是停止。

### 容易踩坑

- 回答 ReAct 相关问题，最容易踩的坑就是开头说的那个误区：以为模型自己在「循环」。
- 把 Agent 简化成普通工具调用，忽略自主规划和执行闭环。
- 只讲概念，不讲状态、记忆、终止条件和失败恢复。

### 追问

1. 这个能力和普通 LLM / workflow / tool calling 的边界在哪里？
2. 如果 Agent 中途跑偏或工具失败，你会怎么恢复？
3. 生产环境里你会记录哪些 trace 来定位问题？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 6. ReAct、Plan-and-Execute、Reflection 三种范式有什么核心区别？实际项目中该如何选型？

- 来源：[https://xiaolinnote.com/ai/agent/6_three_patterns.html](https://xiaolinnote.com/ai/agent/6_three_patterns.html)
- 本地原文：`interview-agent/sources/xiaolinnote/agent/6_three_patterns.md`

### 考点

- Agent loop、自主规划、状态/记忆、工具执行、可靠性边界
- 一、基础款：ReAct 单步迭代范式
- 二、复杂任务款：Plan-and-Execute 规划执行范式
- 三、质量增强款：Reflection 反思迭代范式
- 进阶：动态 Replan 和 Reflexion

### 核心理解

我理解这三者是 Agent 开发里最主流的三种设计范式，核心区别在于「决策和执行的关系」。

### 面试回答

我理解这三者是 Agent 开发里最主流的三种设计范式，核心区别在于「决策和执行的关系」。

ReAct 是边想边干，走一步看一步，单步迭代实时调整，灵活度最高；Plan-and-Execute 是先想全再干，先定完整计划再分步执行，适合长流程复杂任务，不容易跑偏；Reflection 不是独立的完整流程，而是给前两者加的「检查修正 buff」，用来提升输出质量。

实际选型就看三个维度：任务复杂度、流程确定性、输出质量要求，新手入门首选 ReAct，复杂任务用 Plan-and-Execute，高要求场景再加 Reflection。

### 工程例子

可以结合一个 Coding Agent 或运营助手来讲：用户给出目标后，系统先规划步骤，再调用搜索、文件、代码执行或 API 工具，每一步观察结果都会写回状态，并决定下一步继续、重试还是停止。

### 容易踩坑

- 把 Agent 简化成普通工具调用，忽略自主规划和执行闭环。
- 只讲概念，不讲状态、记忆、终止条件和失败恢复。

### 追问

1. 这个能力和普通 LLM / workflow / tool calling 的边界在哪里？
2. 如果 Agent 中途跑偏或工具失败，你会怎么恢复？
3. 生产环境里你会记录哪些 trace 来定位问题？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 7. 复杂任务怎么做的任务拆分？为什么要拆分？效果如何提升？

- 来源：[https://xiaolinnote.com/ai/agent/7_tasksplit.html](https://xiaolinnote.com/ai/agent/7_tasksplit.html)
- 本地原文：`interview-agent/sources/xiaolinnote/agent/7_tasksplit.md`

### 考点

- Agent loop、自主规划、状态/记忆、工具执行、可靠性边界
- 为什么任务要拆分？
- 任务拆分两种思路
- 自适应拆分：做不好就继续拆
- 执行中的 Replan 机制

### 核心理解

我理解任务拆分的原因是 LLM 一次性处理太复杂的任务很容易出错，把大任务拆成小步骤，每步聚焦一件事，准确率会明显提升。

### 面试回答

我理解任务拆分的原因是 LLM 一次性处理太复杂的任务很容易出错，把大任务拆成小步骤，每步聚焦一件事，准确率会明显提升。

拆分方式主要有两种：一种是静态拆分，提前把步骤写死；另一种是动态拆分，让 LLM 自己根据目标规划步骤，更灵活但也更难控制。

拆完之后步骤之间可能有依赖关系，我的经验是把能并行的步骤并发跑，端到端延迟可以降很多，有时能降 40% 到 60%。

### 工程例子

可以结合一个 Coding Agent 或运营助手来讲：用户给出目标后，系统先规划步骤，再调用搜索、文件、代码执行或 API 工具，每一步观察结果都会写回状态，并决定下一步继续、重试还是停止。

### 容易踩坑

- 把 Agent 简化成普通工具调用，忽略自主规划和执行闭环。
- 只讲概念，不讲状态、记忆、终止条件和失败恢复。

### 追问

1. 这个能力和普通 LLM / workflow / tool calling 的边界在哪里？
2. 如果 Agent 中途跑偏或工具失败，你会怎么恢复？
3. 生产环境里你会记录哪些 trace 来定位问题？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 8. 请你介绍一下 AI Agent 的记忆机制，并说明在实际开发中应该如何设计记忆模块？

- 来源：[https://xiaolinnote.com/ai/agent/8_memory.html](https://xiaolinnote.com/ai/agent/8_memory.html)
- 本地原文：`interview-agent/sources/xiaolinnote/agent/8_memory.md`

### 考点

- Agent loop、自主规划、状态/记忆、工具执行、可靠性边界
- 没有记忆的 Agent 有多不好用
- 四种记忆类型（从最短暂到最持久）
- 实际设计记忆模块的三个核心问题
- Context Window 管理：短期记忆的「工作台」不够大怎么办

### 核心理解

Agent 需要记忆才能在多步任务中保持状态、跨任务积累知识。

### 面试回答

Agent 需要记忆才能在多步任务中保持状态、跨任务积累知识。

记忆机制分四层：感知记忆（当前输入的原始内容）、短期记忆（context window 里的对话历史）、长期记忆（存在外部数据库、语义检索召回）、实体记忆（结构化提取的关键事实）。

实际设计时要解决三个核心问题：存什么、怎么存、什么时候取出来用，根据信息类型选合适的存储方式，再搭配主动检索和按需检索两种策略使用。

### 工程例子

可以结合一个 Coding Agent 或运营助手来讲：用户给出目标后，系统先规划步骤，再调用搜索、文件、代码执行或 API 工具，每一步观察结果都会写回状态，并决定下一步继续、重试还是停止。

### 容易踩坑

- 把 Agent 简化成普通工具调用，忽略自主规划和执行闭环。
- 只讲概念，不讲状态、记忆、终止条件和失败恢复。

### 追问

1. 这个能力和普通 LLM / workflow / tool calling 的边界在哪里？
2. 如果 Agent 中途跑偏或工具失败，你会怎么恢复？
3. 生产环境里你会记录哪些 trace 来定位问题？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 9. Agent 的长短期记忆系统怎么做的？记忆是怎么存的？粒度是多少？怎么用的？

- 来源：[https://xiaolinnote.com/ai/agent/9_memory_storage.html](https://xiaolinnote.com/ai/agent/9_memory_storage.html)
- 本地原文：`interview-agent/sources/xiaolinnote/agent/9_memory_storage.md`

### 考点

- Agent loop、自主规划、状态/记忆、工具执行、可靠性边界
- 短期记忆
- 长期记忆

### 核心理解

我理解记忆系统分两层。

### 面试回答

我理解记忆系统分两层。

短期记忆就是 context window 里的对话历史，存当前任务的中间状态，任务结束就清掉；长期记忆用向量数据库存，把信息 embedding 后写入，用的时候做语义检索拿回来注入 prompt。

粒度上我通常按「一次完整交互」或「一个关键事件」为单位存，太细碎检索噪音大，太粗糙又丢失细节，这个需要根据业务实际调整。

### 工程例子

可以结合一个 Coding Agent 或运营助手来讲：用户给出目标后，系统先规划步骤，再调用搜索、文件、代码执行或 API 工具，每一步观察结果都会写回状态，并决定下一步继续、重试还是停止。

### 容易踩坑

- 这道题最容易踩的雷有三个，对照开头的对话回想一下。
- 第一个雷是把长期记忆说成「存数据库靠关键词搜索」，这暴露了不了解向量检索，长期记忆的核心是 Embedding + 向量数据库，靠语义相似度而不是字符串匹配来检索，这一点一定要说清楚。
- 第二个雷是以为粒度越细越好，实际上粒度太细会导致记忆碎片化，检索时拿到不完整的信息，合理粒度是「一次完整交互」或「一个独立知识点」。

### 追问

1. 这个能力和普通 LLM / workflow / tool calling 的边界在哪里？
2. 如果 Agent 中途跑偏或工具失败，你会怎么恢复？
3. 生产环境里你会记录哪些 trace 来定位问题？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 10. 什么是 Multi-Agent？

- 来源：[https://xiaolinnote.com/ai/agent/10_multiagent.html](https://xiaolinnote.com/ai/agent/10_multiagent.html)
- 本地原文：`interview-agent/sources/xiaolinnote/agent/10_multiagent.md`

### 考点

- Agent loop、自主规划、状态/记忆、工具执行、可靠性边界
- Multi-Agent 核心思路

### 核心理解

多智能体系统（Multi-Agent）就是多个 Agent 协作完成任务，每个 Agent 各有分工，有的负责搜索、有的负责写代码、有的负责做评审。

### 面试回答

多智能体系统（Multi-Agent）就是多个 Agent 协作完成任务，每个 Agent 各有分工，有的负责搜索、有的负责写代码、有的负责做评审。

我理解单个 Agent 主要受两个限制：一是 context 窗口大小，复杂任务信息量一多就撑爆了；二是单点能力，什么都让一个 Agent 做，每件事都是泛才。

Multi-Agent 通过专业分工和并行执行，能处理更复杂、更长流程的任务，这是我在实际项目里选择多智能体方案的核心原因。

### 工程例子

可以结合一个 Coding Agent 或运营助手来讲：用户给出目标后，系统先规划步骤，再调用搜索、文件、代码执行或 API 工具，每一步观察结果都会写回状态，并决定下一步继续、重试还是停止。

### 容易踩坑

- 把 Agent 简化成普通工具调用，忽略自主规划和执行闭环。
- 只讲概念，不讲状态、记忆、终止条件和失败恢复。

### 追问

1. 这个能力和普通 LLM / workflow / tool calling 的边界在哪里？
2. 如果 Agent 中途跑偏或工具失败，你会怎么恢复？
3. 生产环境里你会记录哪些 trace 来定位问题？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 11. 说说 Single-Agent 和 Multi-Agent 的设计方案？

- 来源：[https://xiaolinnote.com/ai/agent/11_single_multi.html](https://xiaolinnote.com/ai/agent/11_single_multi.html)
- 本地原文：`interview-agent/sources/xiaolinnote/agent/11_single_multi.md`

### 考点

- Agent loop、自主规划、状态/记忆、工具执行、可靠性边界
- Single-Agent
- Multi-Agent 的中心化方案
- 去中心化方案：为什么「听起来更灵活」却很少在工程上用
- 怎么做选型决策？

### 核心理解

Single-Agent 适合任务流程清晰、复杂度适中的场景，实现简单、好维护；Multi-Agent 适合需要专业分工、任务量大或者需要并行执行的复杂场景。

### 面试回答

Single-Agent 适合任务流程清晰、复杂度适中的场景，实现简单、好维护；Multi-Agent 适合需要专业分工、任务量大或者需要并行执行的复杂场景。

Multi-Agent 架构上主要有两种拓扑：中心化的 Orchestrator 模式，由一个主 Agent 统一调度各个 Worker；去中心化的 Peer-to-Peer 模式，Agent 之间直接通信。

我在工程里用中心化用得更多，因为好控制、好调试，出问题链路清晰。

### 工程例子

可以结合一个 Coding Agent 或运营助手来讲：用户给出目标后，系统先规划步骤，再调用搜索、文件、代码执行或 API 工具，每一步观察结果都会写回状态，并决定下一步继续、重试还是停止。

### 容易踩坑

- 这道题最容易犯的错误有三个，对应开头对话里踩的三个雷。
- 把 Agent 简化成普通工具调用，忽略自主规划和执行闭环。
- 只讲概念，不讲状态、记忆、终止条件和失败恢复。

### 追问

1. 这个能力和普通 LLM / workflow / tool calling 的边界在哪里？
2. 如果 Agent 中途跑偏或工具失败，你会怎么恢复？
3. 生产环境里你会记录哪些 trace 来定位问题？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 12. Agent 记忆压缩通常有哪些方法？

- 来源：[https://xiaolinnote.com/ai/agent/12_memcompress.html](https://xiaolinnote.com/ai/agent/12_memcompress.html)
- 本地原文：`interview-agent/sources/xiaolinnote/agent/12_memcompress.md`

### 考点

- Agent loop、自主规划、状态/记忆、工具执行、可靠性边界
- 第一种方法：滑动窗口，最简单的方案，也是最粗糙的
- 第二种方法：摘要压缩，丢之前先提炼一遍
- 第三种方法：重要性过滤，按价值筛选，不按时间筛选
- 第四种方法：结构化抽取，换一种载体存信息

### 核心理解

记忆压缩常见有四种方法：摘要压缩、滑动窗口、重要性过滤、结构化抽取。

### 面试回答

记忆压缩常见有四种方法：摘要压缩、滑动窗口、重要性过滤、结构化抽取。

摘要压缩是把长对话总结成简短摘要；滑动窗口是只保留最近 N 轮对话；重要性过滤是打分筛选，只留重要内容；结构化抽取是把关键信息抽成结构化数据存起来。

我在实际项目里最常用的是摘要压缩和滑动窗口，而且经常组合用，滑动窗口丢弃前先做一次摘要，尽量不丢重要信息。

### 工程例子

可以结合一个 Coding Agent 或运营助手来讲：用户给出目标后，系统先规划步骤，再调用搜索、文件、代码执行或 API 工具，每一步观察结果都会写回状态，并决定下一步继续、重试还是停止。

### 容易踩坑

- 把 Agent 简化成普通工具调用，忽略自主规划和执行闭环。
- 只讲概念，不讲状态、记忆、终止条件和失败恢复。

### 追问

1. 这个能力和普通 LLM / workflow / tool calling 的边界在哪里？
2. 如果 Agent 中途跑偏或工具失败，你会怎么恢复？
3. 生产环境里你会记录哪些 trace 来定位问题？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 13. 在工程实践中，为什么有时候选择「手搓」Agent，而不是直接用成熟框架？

- 来源：[https://xiaolinnote.com/ai/agent/13_handcode.html](https://xiaolinnote.com/ai/agent/13_handcode.html)
- 本地原文：`interview-agent/sources/xiaolinnote/agent/13_handcode.md`

### 考点

- Agent loop、自主规划、状态/记忆、工具执行、可靠性边界
- 痛点在什么时候开始出现？
- 手搓的本质优势：完全掌控
- 同一个需求，框架写 vs 手搓写，差别在哪？
- 什么时候用框架，什么时候手搓？

### 核心理解

我的感受是框架用起来快，但有几个实际痛点。

### 面试回答

我的感受是框架用起来快，但有几个实际痛点。

第一是抽象层太多，调试的时候不知道哪步出了问题，得一层层往下扒；第二是版本升级经常有破坏性变更，线上稳定性难保证；第三是框架的通用设计往往和具体业务需求有偏差，定制起来反而更费劲。

手搓的代码完全在自己掌控之内，可观测性好、出问题好排查，也更方便做性能优化。所以我现在的策略是核心逻辑手写，只在边缘功能上用框架的工具。

### 工程例子

可以结合一个 Coding Agent 或运营助手来讲：用户给出目标后，系统先规划步骤，再调用搜索、文件、代码执行或 API 工具，每一步观察结果都会写回状态，并决定下一步继续、重试还是停止。

### 容易踩坑

- 回顾开头的对话，踩雷的地方其实很典型：只说「框架好用、效率高」，没有说清楚框架在什么阶段开始出问题、以及为什么手搓能解决这些问题。
- 把 Agent 简化成普通工具调用，忽略自主规划和执行闭环。
- 只讲概念，不讲状态、记忆、终止条件和失败恢复。

### 追问

1. 这个能力和普通 LLM / workflow / tool calling 的边界在哪里？
2. 如果 Agent 中途跑偏或工具失败，你会怎么恢复？
3. 生产环境里你会记录哪些 trace 来定位问题？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 14. 如何赋予 LLM 规划能力？

- 来源：[https://xiaolinnote.com/ai/agent/14_planning.html](https://xiaolinnote.com/ai/agent/14_planning.html)
- 本地原文：`interview-agent/sources/xiaolinnote/agent/14_planning.md`

### 考点

- Agent loop、自主规划、状态/记忆、工具执行、可靠性边界
- CoT：最简单的激活方式，加一句话就够了
- ToT：从「一条链」到「一棵树」，解决走错方向的问题
- GoT：从「树」到「图」，解决推理结果不能复用的问题
- 三者的演进关系

### 核心理解

给 LLM 加规划能力主要靠这几种思路。

### 面试回答

给 LLM 加规划能力主要靠这几种思路。

CoT 是让 LLM 把推理步骤写出来，线性地一步步推导到答案；

ToT 是让它同时探索多条推理路径，选最优的继续深入；

GoT 是图结构推理，推理节点可以复用和合并，适合更复杂的任务。

工程上我用 CoT 最多，因为实现成本最低，就是改个 prompt；ToT 效果更好但调用次数多，成本大概是 3 到 5 倍；GoT 目前还比较学术，生产环境我没见过有人真正落地用的。

### 工程例子

可以结合一个 Coding Agent 或运营助手来讲：用户给出目标后，系统先规划步骤，再调用搜索、文件、代码执行或 API 工具，每一步观察结果都会写回状态，并决定下一步继续、重试还是停止。

### 容易踩坑

- 回顾开头踩的雷，第一个最典型：把「CoT 就是规划能力」画等号，这是这道题最常见的误区。规划能力是个方向，CoT 只是最基础的一种实现手段。
- 把 Agent 简化成普通工具调用，忽略自主规划和执行闭环。
- 只讲概念，不讲状态、记忆、终止条件和失败恢复。

### 追问

1. 这个能力和普通 LLM / workflow / tool calling 的边界在哪里？
2. 如果 Agent 中途跑偏或工具失败，你会怎么恢复？
3. 生产环境里你会记录哪些 trace 来定位问题？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 15. 讲讲 Agent 的反思机制？为什么要用反思？具体怎么实现？

- 来源：[https://xiaolinnote.com/ai/agent/15_reflection.html](https://xiaolinnote.com/ai/agent/15_reflection.html)
- 本地原文：`interview-agent/sources/xiaolinnote/agent/15_reflection.md`

### 考点

- Agent loop、自主规划、状态/记忆、工具执行、可靠性边界
- 核心循环：生成 -> 评估 -> 改进
- 两个粒度：步骤级 vs 任务级
- 多 Agent 互评：为什么「他人审视」比「自我检查」更好
- 进阶：Reflexion 和 LATS，把反思做得更深

### 核心理解

反思机制我的理解是：让 Agent 在完成一个步骤或整个任务后，自我评估输出质量，判断有没有问题，不达标就重试或调整策略。

### 面试回答

反思机制我的理解是：让 Agent 在完成一个步骤或整个任务后，自我评估输出质量，判断有没有问题，不达标就重试或调整策略。

用反思的原因是 LLM 第一次输出不一定是最优的，加一轮自我检查能显著提升质量，相当于人写完东西自己再看一遍。

代价是多至少一次 LLM 调用，token 消耗和延迟都会增加，所以我在工程里通常只在质量要求高的关键节点启用反思，不是每步都做。

### 工程例子

可以结合一个 Coding Agent 或运营助手来讲：用户给出目标后，系统先规划步骤，再调用搜索、文件、代码执行或 API 工具，每一步观察结果都会写回状态，并决定下一步继续、重试还是停止。

### 容易踩坑

- 回顾开头踩的雷，把反思说成「不满意就重新生成」是最常见的误区，这说明没有理解反思机制的核心：它是「生成 -> 评估 -> 改进」的有结构的闭环，不是随机重试。
- 把 Agent 简化成普通工具调用，忽略自主规划和执行闭环。
- 只讲概念，不讲状态、记忆、终止条件和失败恢复。

### 追问

1. 这个能力和普通 LLM / workflow / tool calling 的边界在哪里？
2. 如果 Agent 中途跑偏或工具失败，你会怎么恢复？
3. 生产环境里你会记录哪些 trace 来定位问题？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 16. 如何设计多 Agent 的协作与动态切换机制？

- 来源：[https://xiaolinnote.com/ai/agent/16_collab.html](https://xiaolinnote.com/ai/agent/16_collab.html)
- 本地原文：`interview-agent/sources/xiaolinnote/agent/16_collab.md`

### 考点

- Agent loop、自主规划、状态/记忆、工具执行、可靠性边界
- 先说协作：Agent 之间怎么传递信息
- 状态管理：多 Agent 共享状态的设计要点
- 再说切换：Orchestrator 怎么决定叫谁
- Handoff 模式：Agent 之间的「接力棒」

### 核心理解

协作靠两件事：消息传递和共享状态。消息传递是 Agent 完成自己的工作后把结果发出去，下一个 Agent 取用；共享状态是所有 Agent 共同读写一个状态对象，记录任务进展和中间结果。

### 面试回答

协作靠两件事：消息传递和共享状态。消息传递是 Agent 完成自己的工作后把结果发出去，下一个 Agent 取用；共享状态是所有 Agent 共同读写一个状态对象，记录任务进展和中间结果。

动态切换靠 Orchestrator 来做，有两种方式：一种是静态路由，提前写好规则「任务类型 A 就找 Agent X」；另一种是让 LLM 动态决策，根据当前情况实时判断该把任务交给谁。

我的实践是两种混用，主流程用静态路由保证稳定，边缘情况才交给 LLM 动态判断。

### 工程例子

可以结合一个 Coding Agent 或运营助手来讲：用户给出目标后，系统先规划步骤，再调用搜索、文件、代码执行或 API 工具，每一步观察结果都会写回状态，并决定下一步继续、重试还是停止。

### 容易踩坑

- 回顾开头踩的雷，把协作说成「流水线传结果」，把切换说成「全靠 LLM 动态决策」，都是停留在表面没有说到设计取舍。
- 把 Agent 简化成普通工具调用，忽略自主规划和执行闭环。
- 只讲概念，不讲状态、记忆、终止条件和失败恢复。

### 追问

1. 这个能力和普通 LLM / workflow / tool calling 的边界在哪里？
2. 如果 Agent 中途跑偏或工具失败，你会怎么恢复？
3. 生产环境里你会记录哪些 trace 来定位问题？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 17. Agent 面试题介绍

- 来源：[https://xiaolinnote.com/ai/agent/agent_info.html](https://xiaolinnote.com/ai/agent/agent_info.html)
- 本地原文：`interview-agent/sources/xiaolinnote/agent/agent_info.md`

### 考点

- Agent loop、自主规划、状态/记忆、工具执行、可靠性边界
- 题目目录

### 核心理解

---
type: source_note
source_type: xiaolinnote
topic: agent
status: raw
source_url: https://xiaolinnote.com/ai/agent/agent_info.html
title: "Agent 面试题介绍"
content_hash: e6d33159599b5266cbf040a17ac65318a43034e31b003ae0962604816dfe8e8a
updated: 2026-06-12T11:49:14+00:00
tags:
  - xiaolinnote
  - agent
  - interview
---

### 面试回答

---
type: source_note
source_type: xiaolinnote
topic: agent
status: raw
source_url: https://xiaolinnote.com/ai/agent/agent_info.html
title: "Agent 面试题介绍"
content_hash: e6d33159599b5266cbf040a17ac65318a43034e31b003ae0962604816dfe8e8a
updated: 2026-06-12T11:49:14+00:00
tags:
  - xiaolinnote
  - agent
  - interview
---

大家好，我是小林。

Agent 这个方向现在有多火不用我多说了吧，基本上只要面的是 AI 工程相关的岗位，Agent 就是绕不过去的必考题。但说实话，我看了不少同学的面经分享，发现很多人答 Agent 的题目都有一个通病：听起来好像说得都对，但面试官一追问就露馅了，因为只记住了概念，没有真的搞懂背后的原理和工程取舍。

### 工程例子

可以结合一个 Coding Agent 或运营助手来讲：用户给出目标后，系统先规划步骤，再调用搜索、文件、代码执行或 API 工具，每一步观察结果都会写回状态，并决定下一步继续、重试还是停止。

### 容易踩坑

- 把 Agent 简化成普通工具调用，忽略自主规划和执行闭环。
- 只讲概念，不讲状态、记忆、终止条件和失败恢复。

### 追问

1. 这个能力和普通 LLM / workflow / tool calling 的边界在哪里？
2. 如果 Agent 中途跑偏或工具失败，你会怎么恢复？
3. 生产环境里你会记录哪些 trace 来定位问题？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。
