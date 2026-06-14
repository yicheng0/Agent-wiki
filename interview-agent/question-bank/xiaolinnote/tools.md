---
type: question_bank
topic: tools
source_type: xiaolinnote
status: reviewed
updated: 2026-06-12
tags:
  - xiaolinnote
  - interview
  - tools
---

# 小林面试题 - Tool Calling / MCP / Skills

> 说明：本文件由 `tools/build_xiaolinnote_interview_cards.py` 从 `xiaolinnote-ai-qa.jsonl` 生成，属于外部资料整理层，未合并进手工精选题库。

## 1. 什么是 Function Calling ？原理是什么？

- 来源：[https://xiaolinnote.com/ai/tools/1_function_calling.html](https://xiaolinnote.com/ai/tools/1_function_calling.html)
- 本地原文：`interview-agent/sources/xiaolinnote/tools/1_function_calling.md`

### 考点

- Function Calling、工具协议、权限边界、参数校验、工具生态
- 背景，Function Calling 解决了什么问题
- 三个角色，把 Function Calling 理解成一场任务委托
- 工具定义，schema 的每个字段都有含义
- 完整的调用流程，两轮对话加中间执行

### 核心理解

Function Calling 我的理解是这样一套机制：开发者用 JSON schema 把工具描述好传给模型，模型判断需要调工具的时候不输出自然语言，而是直接输出一段结构化的 tool_calls JSON，告诉你「我要调哪个函数、参数是什么」，你的代码拿到这段 JSON 去真正执行，把结果塞回对话，模型再生成最终答案。

### 面试回答

Function Calling 我的理解是这样一套机制：开发者用 JSON schema 把工具描述好传给模型，模型判断需要调工具的时候不输出自然语言，而是直接输出一段结构化的 tool_calls JSON，告诉你「我要调哪个函数、参数是什么」，你的代码拿到这段 JSON 去真正执行，把结果塞回对话，模型再生成最终答案。

整个流程本质上是两轮对话：第一轮模型说「我需要调这个工具」，你去执行，第二轮模型拿到执行结果说「答案是这个」。

我觉得最核心的设计是，模型全程只做决策，执行的事情一律由宿主代码完成，职责分得很清楚。

### 工程例子

可以结合一个能查订单、发邮件或调用内部 API 的 Agent 来讲：模型只负责决定调用哪个工具和参数，真正执行由后端工具层完成，并通过 schema 校验、权限、超时、重试和审计保证可靠性。

### 容易踩坑

- 回头看开头的面试对话，踩的雷其实很典型。
- 第一个误区是以为模型能「自己」去访问网络、执行代码，这是对 Function Calling 最常见的误解。面试时一定要强调：模型全程只负责决策，输出结构化的 JSON 调用请求，真正执行工具的是你的宿主程序代码，这个职责分工是整个机制的核心设计。
- 第二个误区是把 Function Calling 和之前靠解析自然语言调工具的「土办法」搞混了，Function Calling 的关键改进就是模型直接输出结构化 JSON 而非自然语言，让工具调用有了统一标准。

### 追问

1. 模型生成的 tool arguments 能不能直接信任？为什么？
2. 哪些工具调用必须做人工确认或权限隔离？
3. 工具 API 超时、失败或重复执行时，你怎么保证可靠性？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 2. LLM 是如何学会调用外部工具的？

- 来源：[https://xiaolinnote.com/ai/tools/2_llm_tool_learning.html](https://xiaolinnote.com/ai/tools/2_llm_tool_learning.html)
- 本地原文：`interview-agent/sources/xiaolinnote/tools/2_llm_tool_learning.md`

### 考点

- Function Calling、工具协议、权限边界、参数校验、工具生态
- 原始 LLM 的世界，为什么不会调工具
- 第一阶段：SFT，让模型「见过」工具调用
- SFT 的短板，会了，但不知道「该不该调」
- 第二阶段：RLHF，用反馈建立边界感

### 核心理解

这道题我分两块来讲：模型怎么被训练出工具调用能力，以及训练好之后运行时是怎么工作的。

### 面试回答

这道题我分两块来讲：模型怎么被训练出工具调用能力，以及训练好之后运行时是怎么工作的。

训练层面靠两个阶段：

- SFT（监督微调，Supervised Fine-Tuning）：给模型喂大量「工具调用示范对话」，让它通过模仿学会「看到工具描述 -> 判断要不要调 -> 输出结构化 JSON 请求」这整套流程；

- RLHF（基于人类反馈的强化学习，Reinforcement Learning from Human Feedback）：收集人类对「哪种回答更好」的判断，训练一个打分器，再用这个分数反复调整模型，让它学会什么时候不应该调工具。

运行层面，每次请求时，你的应用代码把工具描述（叫 schema，可以理解为工具的说明书）传给模型，模型如果判断需要工具，就输出一段结构化的 `tool_calls` JSON；你的代码拿到这段 JSON 去真正执行，把结果塞回对话，模型再给出最终答案。

有一点非常关键：模型全程只是在「下指令」，真正执行工具的是你的代码，不是模型本身。这套「模型决策、代码执行」的运行时机制，就是我们常说的 Function Calling。

### 工程例子

可以结合一个能查订单、发邮件或调用内部 API 的 Agent 来讲：模型只负责决定调用哪个工具和参数，真正执行由后端工具层完成，并通过 schema 校验、权限、超时、重试和审计保证可靠性。

### 容易踩坑

- 回顾开头的面试对话，第一个雷是以为模型参数量够大就自然会调工具，这是把「语言涌现能力」和「工具调用能力」搞混了。工具调用需要输出结构化 JSON，这不是预训练能学到的，必须经过专项训练。
- 第二个雷是只知道 SFT 而忽略了 RLHF，SFT 解决「会不会调」，RLHF 解决「该不该调」，两个阶段缺一不可。
- 信任模型生成的工具参数，缺少 schema 校验和权限边界。

### 追问

1. 模型生成的 tool arguments 能不能直接信任？为什么？
2. 哪些工具调用必须做人工确认或权限隔离？
3. 工具 API 超时、失败或重复执行时，你怎么保证可靠性？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 3. 大模型的 Function Call 能力是怎么训练出来的？

- 来源：[https://xiaolinnote.com/ai/tools/3_fc_training.html](https://xiaolinnote.com/ai/tools/3_fc_training.html)
- 本地原文：`interview-agent/sources/xiaolinnote/tools/3_fc_training.md`

### 考点

- Function Calling、工具协议、权限边界、参数校验、工具生态
- 阶段一：SFT，让模型「学会怎么调」
- 训练数据需要覆盖哪些场景
- 训练数据从哪来
- 阶段二：RLHF，对齐「该不该调」的边界感

### 核心理解

Function Call 的能力主要靠两个训练阶段来培养，这两个阶段解决的是不同的问题。

### 面试回答

Function Call 的能力主要靠两个训练阶段来培养，这两个阶段解决的是不同的问题。

第一个是 SFT，就是给模型喂大量「包含工具调用的完整对话样本」，每条样本覆盖工具定义、用户问题、模型应该输出的结构化 JSON 调用、工具执行结果、最终答案，让模型通过模仿学会整套流程。但光有 SFT 不够，模型可能学得过激，遇到什么问题都想调工具。

第二个阶段是 RLHF，通过人类标注「哪种回答更好」来训练奖励模型，再用强化学习调整主模型，让它学会「能直接回答的就直接回答，需要实时数据才去调工具」这个边界感。

一句话总结：SFT 教会怎么调，RLHF 教会什么时候调。

### 工程例子

可以结合一个能查订单、发邮件或调用内部 API 的 Agent 来讲：模型只负责决定调用哪个工具和参数，真正执行由后端工具层完成，并通过 schema 校验、权限、超时、重试和审计保证可靠性。

### 容易踩坑

- 回看开头踩的雷，第一个误区是以为预训练就能学会 Function Call，实际上预训练只学了「预测下一个 token」，模型最多会描述意图，不会输出结构化 JSON，这必须靠 SFT 专项训练。第二个误区是以为训练数据只覆盖单工具调用就够了，实际上多工具并行、调用失败重试、不需要工具直接回答、多轮对话中的调用，这些场景都必须覆盖，缺哪个就在哪个场景翻车。
- 训练数据来源也要提到：人工标注质量高但成本高用于种子数据，模型自动生成（Self-Instruct / Distillation）成本低量大但要注意幻觉传递的风险。
- 信任模型生成的工具参数，缺少 schema 校验和权限边界。

### 追问

1. 模型生成的 tool arguments 能不能直接信任？为什么？
2. 哪些工具调用必须做人工确认或权限隔离？
3. 工具 API 超时、失败或重复执行时，你怎么保证可靠性？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 4. 什么是 MCP（模型上下文协议）？讲讲它的核心内容？

- 来源：[https://xiaolinnote.com/ai/tools/4_what_is_mcp.html](https://xiaolinnote.com/ai/tools/4_what_is_mcp.html)
- 本地原文：`interview-agent/sources/xiaolinnote/tools/4_what_is_mcp.md`

### 考点

- Function Calling、工具协议、权限边界、参数校验、工具生态
- 没有 MCP 之前，接工具有多麻烦
- MCP 的核心思路，定一套行业标准接口
- MCP 的 Client-Server 架构
- 三类核心能力，Tools、Resources、Prompts

### 核心理解

MCP 是 Anthropic 在 2024 年底推出的开放协议，我理解它主要解决的是「模型接工具太碎片化」的问题。

### 面试回答

MCP 是 Anthropic 在 2024 年底推出的开放协议，我理解它主要解决的是「模型接工具太碎片化」的问题。

在 MCP 出现之前，每接一个新工具都要单独写集成代码、处理认证、适配格式，而且这套代码和具体模型强绑定，换个模型就得重写，非常繁琐。

MCP 的思路是把这件事标准化：工具提供方按协议实现一个 Server，任何支持 MCP 的 AI 客户端就能直接接进来，一次实现到处复用。

协议定义了三类能力：Tools 用于执行有副作用的操作，Resources 是只读数据，Prompts 是提示词模板，底层通信用 JSON-RPC 2.0。

我把它理解成给「AI 接工具」这件事定了一套行业标准。

### 工程例子

可以结合一个能查订单、发邮件或调用内部 API 的 Agent 来讲：模型只负责决定调用哪个工具和参数，真正执行由后端工具层完成，并通过 schema 校验、权限、超时、重试和审计保证可靠性。

### 容易踩坑

- 回看开头的面试对话，最典型的误区就是把 MCP 和 Function Calling 搞混了。Function Calling 解决的是「模型怎么输出结构化的工具调用请求」，而 MCP 解决的是「工具怎么标准化接入、一次实现到处复用」，两者是不同层面的东西。另一个常见错误是以为 MCP 是 Anthropic 专属的，实际上它是开放协议，任何支持 MCP 的客户端都能接入。
- 信任模型生成的工具参数，缺少 schema 校验和权限边界。
- 忽略工具失败、超时、重试、幂等和审计。

### 追问

1. 模型生成的 tool arguments 能不能直接信任？为什么？
2. 哪些工具调用必须做人工确认或权限隔离？
3. 工具 API 超时、失败或重复执行时，你怎么保证可靠性？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 5. MCP 由哪几部分组成？

- 来源：[https://xiaolinnote.com/ai/tools/5_mcp_components.html](https://xiaolinnote.com/ai/tools/5_mcp_components.html)
- 本地原文：`interview-agent/sources/xiaolinnote/tools/5_mcp_components.md`

### 考点

- Function Calling、工具协议、权限边界、参数校验、工具生态
- 先建立整体感：三层来看就清楚了
- 第一层：角色架构，Host / Client / Server
- 第二层：能力类型，Tools / Resources / Prompts
- 第三层：传输协议，JSON-RPC 2.0 + 传输方式

### 核心理解

MCP 由三层组成，可以从角色、能力、协议三个维度来理解。

### 面试回答

MCP 由三层组成，可以从角色、能力、协议三个维度来理解。

角色层有三个：Host 是 AI 应用本身（比如 Claude Desktop），Client 是 Host 里负责和 Server 通信的模块，Server 是工具提供方实现的独立进程，一个 Host 可以同时连多个 Server。

能力层定义了 Server 能暴露三类东西：Tools 是有副作用的操作（比如创建文件、调 API），Resources 是只读数据（比如读取文档内容），Prompts 是预定义的提示词模板。

协议层是底层通信：消息格式统一用 JSON-RPC 2.0，传输方式支持 stdio（本地子进程通信）和 Streamable HTTP（远程 HTTP 连接）两种，早期的 HTTP+SSE 双端点方案在 2025 年 3 月的规范更新里被标记为 deprecated。

这三层合在一起，就是 MCP 的完整组成。

### 工程例子

可以结合一个能查订单、发邮件或调用内部 API 的 Agent 来讲：模型只负责决定调用哪个工具和参数，真正执行由后端工具层完成，并通过 schema 校验、权限、超时、重试和审计保证可靠性。

### 容易踩坑

- 回到开头踩的雷，最大的问题是把 MCP 简单理解成「Client + Server」的二元结构，忽略了 Host 这个角色。
- 第二个容易踩的雷是把 Server 暴露的能力全归为「工具」。Tools、Resources、Prompts 三者职责分明，Tools 有副作用、改变外部状态，Resources 是只读数据、没有副作用，Prompts 是提示词模板。面试时说清楚三者的区别，尤其是 Tools 和 Resources 的本质差异（有无副作用），会让面试官觉得你真正理解了 MCP 的设计意图，而不是只停留在表面。
- 信任模型生成的工具参数，缺少 schema 校验和权限边界。

### 追问

1. 模型生成的 tool arguments 能不能直接信任？为什么？
2. 哪些工具调用必须做人工确认或权限隔离？
3. 工具 API 超时、失败或重复执行时，你怎么保证可靠性？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 6. MCP 和 Function Calling 有什么区别？有没有实际跑过 MCP？

- 来源：[https://xiaolinnote.com/ai/tools/6_mcp_vs_fc.html](https://xiaolinnote.com/ai/tools/6_mcp_vs_fc.html)
- 本地原文：`interview-agent/sources/xiaolinnote/tools/6_mcp_vs_fc.md`

### 考点

- Function Calling、工具协议、权限边界、参数校验、工具生态
- Function Calling 有了，为什么还需要 MCP？
- Function Calling 解决的是「一次调用」的格式问题
- Function Calling 的痛点，每次都是一次性的
- MCP 解决的是「工具生态」的问题

### 核心理解

我理解这两者不是竞争关系，解决的不是同一层面的问题。

### 面试回答

我理解这两者不是竞争关系，解决的不是同一层面的问题。

Function Calling 是「调用语言」，定义的是模型怎么表达「我要调哪个函数、参数是什么」；MCP 是「工具生态协议」，定义的是工具怎么标准化打包、注册和被 AI 客户端发现。

MCP 底层其实还是用 Function Calling 来触发工具调用，只是在它之上加了一套工具管理框架，让工具实现一次、到处复用。

打个比方：Function Calling 像 HTTP 请求格式，MCP 像 REST API 的设计规范加服务注册发现机制，两者是不同层次的东西。

关于实际跑过的经验，我用 Claude Desktop 配过文件系统和 GitHub 的 MCP Server，在配置文件里加几行就能用，Claude 会自动发现工具，完全不用写对接代码。

### 工程例子

可以结合一个能查订单、发邮件或调用内部 API 的 Agent 来讲：模型只负责决定调用哪个工具和参数，真正执行由后端工具层完成，并通过 schema 校验、权限、超时、重试和审计保证可靠性。

### 容易踩坑

- 回到开头的面试对话，最大的雷就是把 MCP 当成 Function Calling 的「替代品」或「升级版」，这是很多人的第一反应，但完全搞反了两者的关系。
- 如果能再补充实际跑过 MCP 的经验就更好了，比如在 Claude Desktop 里配置过哪些 MCP Server、接入流程是什么样的，这些实操细节能让面试官看到你不是只背概念。要避免的误区是：不要说 MCP 就是「换了个写法的 Function Calling」，也不要说两者是竞争关系，它们是上下层的配合关系。
- 信任模型生成的工具参数，缺少 schema 校验和权限边界。

### 追问

1. 模型生成的 tool arguments 能不能直接信任？为什么？
2. 哪些工具调用必须做人工确认或权限隔离？
3. 工具 API 超时、失败或重复执行时，你怎么保证可靠性？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 7. Function Calling 也属于工具调用，请问什么场景下使用 Function Calling，什么场景下使用 MCP？

- 来源：[https://xiaolinnote.com/ai/tools/7_fc_vs_mcp_usage.html](https://xiaolinnote.com/ai/tools/7_fc_vs_mcp_usage.html)
- 本地原文：`interview-agent/sources/xiaolinnote/tools/7_fc_vs_mcp_usage.md`

### 考点

- Function Calling、工具协议、权限边界、参数校验、工具生态
- 先建立一个直觉：内嵌 vs 独立
- Function Calling 的适用场景
- MCP 的适用场景
- 一个实用的判断方法

### 核心理解

如果只是给单个应用接一两个工具、场景临时、不需要复用，Function Calling 就够了，简单直接，不需要引入额外的进程和配置。

### 面试回答

如果只是给单个应用接一两个工具、场景临时、不需要复用，Function Calling 就够了，简单直接，不需要引入额外的进程和配置。

但只要工具需要跨项目或跨团队复用、或者数量多了管理麻烦、或者社区已经有现成的 MCP Server 可以直接配置，MCP 就值得上了。

判断的核心问题只有一个：这个工具会不会在这个应用之外被用到？会的话，把它封装成 MCP Server 是更长远的选择。

此外，做 Agent 系统的话更应该选 MCP，工具来源多、数量大，手写 Function Calling 的维护成本会让代码变得难以管理。

### 工程例子

可以结合一个能查订单、发邮件或调用内部 API 的 Agent 来讲：模型只负责决定调用哪个工具和参数，真正执行由后端工具层完成，并通过 schema 校验、权限、超时、重试和审计保证可靠性。

### 容易踩坑

- 回到开头的面试对话，最典型的误区就是用单一维度来做选型判断，比如只看项目规模或只看工具数量。
- 另一个容易踩的雷是只说「什么时候用 MCP」而忽略了 Function Calling 的适用场景。快速原型、工具只为单一应用服务、需要精细控制执行逻辑、部署环境受限这四种场景，Function Calling 反而是更好的选择。面试官想听到的是你能根据具体场景做出合理取舍，而不是一刀切地倾向某一个方案。
- 信任模型生成的工具参数，缺少 schema 校验和权限边界。

### 追问

1. 模型生成的 tool arguments 能不能直接信任？为什么？
2. 哪些工具调用必须做人工确认或权限隔离？
3. 工具 API 超时、失败或重复执行时，你怎么保证可靠性？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 8. 为什么有些特定的推理模型不支持 MCP 协议？

- 来源：[https://xiaolinnote.com/ai/tools/8_reasoning_no_mcp.html](https://xiaolinnote.com/ai/tools/8_reasoning_no_mcp.html)
- 本地原文：`interview-agent/sources/xiaolinnote/tools/8_reasoning_no_mcp.md`

### 考点

- Function Calling、工具协议、权限边界、参数校验、工具生态
- 先弄清楚推理模型是什么
- 工具调用的本质是「中途暂停」
- 直觉类比，写推理过程中途被打断
- 「那保存状态再恢复不就行了？」

### 核心理解

我理解根本原因是两者的生成范式有冲突。

### 面试回答

我理解根本原因是两者的生成范式有冲突。

推理模型在给出答案之前，会先跑一段完整的「思维链」，这个 thinking 过程是一次性连续生成的，不能中途打断。但工具调用天然是多轮交互：模型输出调用请求、暂停等工具执行、拿到结果再继续生成，这两种模式没法兼容。你没法在思考链跑到一半的时候暂停去等工具结果，否则之前的推理上下文全断了。

而 MCP 底层就是靠 Function Calling 驱动的，推理模型连 Function Calling 都支持不好，MCP 自然也用不了。

当然这个问题不是无解的，后来 o3 和 Claude Extended Thinking 都找到了折中方案，比如让工具调用发生在思考阶段结束之后，保证思考过程还是一次性完整生成的。

### 工程例子

可以结合一个能查订单、发邮件或调用内部 API 的 Agent 来讲：模型只负责决定调用哪个工具和参数，真正执行由后端工具层完成，并通过 schema 校验、权限、超时、重试和审计保证可靠性。

### 容易踩坑

- 回到开头的面试对话，最常见的误区有两个：一是以为不支持 MCP 只是「还没适配」，把结构性的技术冲突当成了工程进度问题；二是把原因归结为上下文窗口不够大，没有抓到真正的矛盾点。
- 信任模型生成的工具参数，缺少 schema 校验和权限边界。
- 忽略工具失败、超时、重试、幂等和审计。

### 追问

1. 模型生成的 tool arguments 能不能直接信任？为什么？
2. 哪些工具调用必须做人工确认或权限隔离？
3. 工具 API 超时、失败或重复执行时，你怎么保证可靠性？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 9. Skill 是什么？

- 来源：[https://xiaolinnote.com/ai/tools/9_skill.html](https://xiaolinnote.com/ai/tools/9_skill.html)
- 本地原文：`interview-agent/sources/xiaolinnote/tools/9_skill.md`

### 考点

- Function Calling、工具协议、权限边界、参数校验、工具生态
- 为什么需要 Skill？从「重复贴 prompt」的痛点说起
- Skill 的结构长什么样
- 渐进式加载：Skill 最聪明的设计
- Skill 和 Tool、Prompt 分别是什么关系

### 核心理解

Agent Skill 是把「指令、脚本、模板」一体化打包成可复用能力包的机制，关键在于三件事：Agent 能自动发现它、按需加载它、在需要时调用里面的脚本和资源。它不只是「存 prompt」，而是一份 Agent 能自己翻阅的「操作手册 + 工具箱」。每个 Skill 是一个文件夹，里面有一份 SKILL.md 指令文件，还可以带上脚本、模板、参考文档这些资源。

### 面试回答

Agent Skill 是把「指令、脚本、模板」一体化打包成可复用能力包的机制，关键在于三件事：Agent 能自动发现它、按需加载它、在需要时调用里面的脚本和资源。它不只是「存 prompt」，而是一份 Agent 能自己翻阅的「操作手册 + 工具箱」。每个 Skill 是一个文件夹，里面有一份 SKILL.md 指令文件，还可以带上脚本、模板、参考文档这些资源。

它和普通 prompt 最大的区别是：Skill 能被 Agent 自动发现和按需加载，不用你每次手动输入；和 MCP 工具的区别是：MCP 给 Agent 提供外部工具和数据的访问能力，而 Skill 教 Agent 拿到这些工具和数据之后该怎么用。

Anthropic 在 2025 年 10 月推出了 Agent Skills，同年 12 月把规范作为开放标准发布出来，允许其他 Agent 平台按照这套格式来兼容 Skills 生态。

### 工程例子

可以结合一个能查订单、发邮件或调用内部 API 的 Agent 来讲：模型只负责决定调用哪个工具和参数，真正执行由后端工具层完成，并通过 schema 校验、权限、超时、重试和审计保证可靠性。

### 容易踩坑

- 回到开头踩的雷，最常见的误区就是把 Skill 等同于「保存好的 prompt」。面试回答这道题，第一个要说清楚的是 Skill 的本质：它不是一段 prompt，而是一个包含指令、脚本、模板的可复用能力模块，Agent 可以自动发现和按需加载。
- 信任模型生成的工具参数，缺少 schema 校验和权限边界。
- 忽略工具失败、超时、重试、幂等和审计。

### 追问

1. 模型生成的 tool arguments 能不能直接信任？为什么？
2. 哪些工具调用必须做人工确认或权限隔离？
3. 工具 API 超时、失败或重复执行时，你怎么保证可靠性？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 10. MCP 和 Agent Skill 的区别是什么？

- 来源：[https://xiaolinnote.com/ai/tools/10_mcp_vs_skill.html](https://xiaolinnote.com/ai/tools/10_mcp_vs_skill.html)
- 本地原文：`interview-agent/sources/xiaolinnote/tools/10_mcp_vs_skill.md`

### 考点

- Function Calling、工具协议、权限边界、参数校验、工具生态
- 从定位说起：两者解决的不是同一个问题
- MCP：让 Agent 有「手」
- Skill：给 Agent 一份「操作手册」
- 两者怎么配合工作

### 核心理解

MCP 和 Agent Skill 不是同类概念，不是竞争关系，而是互补的。

### 面试回答

MCP 和 Agent Skill 不是同类概念，不是竞争关系，而是互补的。

MCP 解决的是「Agent 怎么获得外部能力」，它把数据库、API、文件系统这些外部工具标准化封装成服务，Agent 通过 MCP 就能查数据、调接口、读写文件。

Skill 解决的是「Agent 拿到这些能力之后，该按什么步骤、什么标准来完成任务」，它把完成某类工作的知识和流程打包成可复用的模块。

简单记：MCP 是给 Agent 配的电脑和软件，Skill 是给 Agent 发的操作手册和 SOP。在实际系统里，两者经常同时工作，Skill 定义流程，流程中调用 MCP 提供的工具。

### 工程例子

可以结合一个能查订单、发邮件或调用内部 API 的 Agent 来讲：模型只负责决定调用哪个工具和参数，真正执行由后端工具层完成，并通过 schema 校验、权限、超时、重试和审计保证可靠性。

### 容易踩坑

- 回到开头对话踩的雷，最大的误区就是把 MCP 和 Skill 当成同类概念来对比。面试回答这道题，第一个必须说清楚的是两者的定位差异：MCP 提供工具和数据的访问能力，解决的是「Agent 怎么做事」；Skill 提供完成任务的知识和流程，解决的是「Agent 该怎么做事」。一个是能力，一个是知识。
- 信任模型生成的工具参数，缺少 schema 校验和权限边界。
- 忽略工具失败、超时、重试、幂等和审计。

### 追问

1. 模型生成的 tool arguments 能不能直接信任？为什么？
2. 哪些工具调用必须做人工确认或权限隔离？
3. 工具 API 超时、失败或重复执行时，你怎么保证可靠性？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 11. Function Calling、Skill、MCP 这三个有什么区别？

- 来源：[https://xiaolinnote.com/ai/tools/11_fc_skill_mcp.html](https://xiaolinnote.com/ai/tools/11_fc_skill_mcp.html)
- 本地原文：`interview-agent/sources/xiaolinnote/tools/11_fc_skill_mcp.md`

### 考点

- Function Calling、工具协议、权限边界、参数校验、工具生态
- 为什么会有三个概念
- 从「谁和谁通信」来看三者位置
- 三者的层级依赖关系
- 用一个完整故事串联三者

### 核心理解

这三个概念在不同层次工作，不是竞争关系。

### 面试回答

这三个概念在不同层次工作，不是竞争关系。

Function Calling 是最底层的调用协议，解决的是「模型怎么调函数」，模型输出结构化 JSON 告诉程序该调哪个函数、传什么参数。

MCP 在 Function Calling 之上做工具标准化，解决的是「工具怎么暴露给模型」，把数据库、API 这些外部能力封装成标准化服务，一次实现到处复用。

Agent Skill 在最上层做知识和流程的封装，解决的是「拿到工具之后按什么流程完成任务」，把执行步骤、标准、脚本、模板打包成可复用模块。

简单记就是：Function Calling 是语言，MCP 是工具箱，Skill 是操作手册。

### 工程例子

可以结合一个能查订单、发邮件或调用内部 API 的 Agent 来讲：模型只负责决定调用哪个工具和参数，真正执行由后端工具层完成，并通过 schema 校验、权限、超时、重试和审计保证可靠性。

### 容易踩坑

- 回到开头对话踩的雷，最大的误区就是把 Function Calling、MCP、Skill 当成三个平行的竞争方案。面试回答这道题，第一个必须说清楚的是三者的层级关系：Function Calling 是最底层的调用协议，解决的是「模型怎么触发函数调用」；MCP 在 Function Calling 之上，解决的是「工具怎么标准化封装和发现」；Skill 在最上层，解决的是「拿到工具后按什么流程完成任务」。三层从下到上，各司其职。
- 信任模型生成的工具参数，缺少 schema 校验和权限边界。
- 忽略工具失败、超时、重试、幂等和审计。

### 追问

1. 模型生成的 tool arguments 能不能直接信任？为什么？
2. 哪些工具调用必须做人工确认或权限隔离？
3. 工具 API 超时、失败或重复执行时，你怎么保证可靠性？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 12. 什么是 A2A 协议？它和 MCP 协议的区别是什么？

- 来源：[https://xiaolinnote.com/ai/tools/12_a2a_protocol.html](https://xiaolinnote.com/ai/tools/12_a2a_protocol.html)
- 本地原文：`interview-agent/sources/xiaolinnote/tools/12_a2a_protocol.md`

### 考点

- Function Calling、工具协议、权限边界、参数校验、工具生态
- 为什么单个 Agent 不够用，上下文和专业边界
- 多 Agent 的基础问题，Agent 之间怎么互相认识？
- Task，A2A 里的一等公民
- A2A 的架构本质，Agent 的微服务化

### 核心理解

A2A 是 Google 发布的开放协议，专门解决多个 AI Agent 之间怎么互相通信协作的问题。

### 面试回答

A2A 是 Google 发布的开放协议，专门解决多个 AI Agent 之间怎么互相通信协作的问题。

我理解它和 MCP 的区别是这样的：MCP 解决的是「单个 Agent 怎么连工具和数据」，A2A 解决的是「多个 Agent 之间怎么分工协作」。

一个 Agent 通过 A2A 可以把子任务委托给另一个专业 Agent，接收方按自己的 Skill 声明承接，支持异步长任务和流式推送结果。

两者是互补的，不冲突：MCP 向下连工具，A2A 向上连 Agent，在复杂的多 Agent 系统里这两个通常都要用到。

### 工程例子

可以结合一个能查订单、发邮件或调用内部 API 的 Agent 来讲：模型只负责决定调用哪个工具和参数，真正执行由后端工具层完成，并通过 schema 校验、权限、超时、重试和审计保证可靠性。

### 容易踩坑

- 回到开头的面试对话，最大的雷是把 A2A 当成 MCP 的「竞品」或「替代方案」，这说明没搞清楚两者面向的对象完全不同。
- 信任模型生成的工具参数，缺少 schema 校验和权限边界。
- 忽略工具失败、超时、重试、幂等和审计。

### 追问

1. 模型生成的 tool arguments 能不能直接信任？为什么？
2. 哪些工具调用必须做人工确认或权限隔离？
3. 工具 API 超时、失败或重复执行时，你怎么保证可靠性？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 13. MCP 协议通常采用什么通信方式？

- 来源：[https://xiaolinnote.com/ai/tools/13_mcp_transport.html](https://xiaolinnote.com/ai/tools/13_mcp_transport.html)
- 本地原文：`interview-agent/sources/xiaolinnote/tools/13_mcp_transport.md`

### 考点

- Function Calling、工具协议、权限边界、参数校验、工具生态
- MCP 的消息格式：JSON-RPC 2.0
- 传输方式一：stdio（标准输入输出）
- 传输方式二：Streamable HTTP（当前标准的远程传输）
- 为什么 SSE 被弃用了

### 核心理解

MCP 支持两种主要的传输方式，分别适用于不同场景。

### 面试回答

MCP 支持两种主要的传输方式，分别适用于不同场景。

本地场景用 stdio，Client 把 Server 作为子进程启动，通过标准输入输出通信，延迟极低，不用开端口，也没有网络安全问题，我用 Claude Desktop 接本地工具走的就是这种方式。

远程场景现在推荐用 Streamable HTTP，Server 作为独立的 HTTP 服务部署，多个 Client 可以共享同一个 Server，适合团队统一管理工具服务。

MCP 早期版本（2024-11-05 规范）的远程传输是「HTTP + SSE」双端点方案，2025 年 3 月的规范更新里被标记为 deprecated（保留向后兼容但不推荐新项目使用），Streamable HTTP 成为了推荐的远程传输方式。

不管哪种传输方式，底层消息格式都统一用 JSON-RPC 2.0，传输方式只影响「怎么传」，消息协议本身不变。

### 工程例子

可以结合一个能查订单、发邮件或调用内部 API 的 Agent 来讲：模型只负责决定调用哪个工具和参数，真正执行由后端工具层完成，并通过 schema 校验、权限、超时、重试和审计保证可靠性。

### 容易踩坑

- 回到开头踩的雷，最常见的误区就是想当然地以为 MCP 用 WebSocket 或者 HTTP REST 接口。
- 信任模型生成的工具参数，缺少 schema 校验和权限边界。
- 忽略工具失败、超时、重试、幂等和审计。

### 追问

1. 模型生成的 tool arguments 能不能直接信任？为什么？
2. 哪些工具调用必须做人工确认或权限隔离？
3. 工具 API 超时、失败或重复执行时，你怎么保证可靠性？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 14. 说说 WebSocket 和 SSE 通信的区别及局限性？

- 来源：[https://xiaolinnote.com/ai/tools/14_sse_vs_websocket.html](https://xiaolinnote.com/ai/tools/14_sse_vs_websocket.html)
- 本地原文：`interview-agent/sources/xiaolinnote/tools/14_sse_vs_websocket.md`

### 考点

- Function Calling、工具协议、权限边界、参数校验、工具生态
- 先从 HTTP 的本质说起
- SSE：用普通 HTTP「撑开」一条单向水管
- WebSocket：从 HTTP 升级成真正的双向信道
- SSE 的局限：不只是「单向」那么简单

### 核心理解

我觉得最核心的区别是通信方向：SSE 是服务端单向推，客户端只能接收，想发消息只能另起一个 HTTP 请求；WebSocket 是全双工，双方都可以随时主动发消息。

### 面试回答

我觉得最核心的区别是通信方向：SSE 是服务端单向推，客户端只能接收，想发消息只能另起一个 HTTP 请求；WebSocket 是全双工，双方都可以随时主动发消息。

对于 LLM 流式输出这种「模型一直在推 token、用户只是看」的场景，SSE 完全够用，而且轻量、HTTP 原生支持、运维简单，OpenAI 和 Anthropic 的 API 用的都是 SSE。

WebSocket 的复杂性只有在真正需要双向实时交互的时候才值得引入，比如用户要在模型说话过程中随时打断。

两者各有局限：SSE 在 HTTP/1.1 下有连接数上限，只支持文本传输；WebSocket 有状态、横向扩展麻烦，还容易被企业代理或防火墙拦掉。大多数 LLM 文字对话产品用 SSE 就够了。

### 工程例子

可以结合一个能查订单、发邮件或调用内部 API 的 Agent 来讲：模型只负责决定调用哪个工具和参数，真正执行由后端工具层完成，并通过 schema 校验、权限、超时、重试和审计保证可靠性。

### 容易踩坑

- 回到开头踩的雷，最大的误区是觉得「WebSocket 功能更强大所以更好」，或者把 SSE 当成 WebSocket 的简化版。
- 信任模型生成的工具参数，缺少 schema 校验和权限边界。
- 忽略工具失败、超时、重试、幂等和审计。

### 追问

1. 模型生成的 tool arguments 能不能直接信任？为什么？
2. 哪些工具调用必须做人工确认或权限隔离？
3. 工具 API 超时、失败或重复执行时，你怎么保证可靠性？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 15. 为什么要用 WebRTC 协议？它和 WebSocket（WS）在 AI 对话流中的核心差异是什么？

- 来源：[https://xiaolinnote.com/ai/tools/15_webrtc_vs_ws.html](https://xiaolinnote.com/ai/tools/15_webrtc_vs_ws.html)
- 本地原文：`interview-agent/sources/xiaolinnote/tools/15_webrtc_vs_ws.md`

### 考点

- Function Calling、工具协议、权限边界、参数校验、工具生态
- WebRTC 的根本：选择 UDP，主动放弃可靠性
- WebRTC 不是单一协议，而是一套协议组合
- SDP 信令：WebRTC 握手的「协商书」
- NAT 穿透：ICE/STUN/TURN 解决的问题

### 核心理解

我理解核心原因是 WebSocket 基于 TCP，而 TCP 的可靠性设计在实时语音场景里反而是负担。

### 面试回答

我理解核心原因是 WebSocket 基于 TCP，而 TCP 的可靠性设计在实时语音场景里反而是负担。

语音可以容忍丢包，但绝对不容忍延迟；一旦网络抖动丢了包，TCP 强制等重传，后续所有音频都得跟着等，延迟一堆积通话就卡。

WebRTC 走的是 UDP，丢包了不等重传，直接用插值算法填补，用一点点音质损失换来稳定的低延迟，延迟能控制在 50 到 150 毫秒。

另外 WebRTC 还内置了回声消除、噪声抑制、自适应码率这些语音处理能力，这些用 WebSocket 都得自己实现。

所以 OpenAI Realtime API 这类实时语音产品选 WebRTC，就是因为 TCP 根本撑不住语音场景的延迟要求。

### 工程例子

可以结合一个能查订单、发邮件或调用内部 API 的 Agent 来讲：模型只负责决定调用哪个工具和参数，真正执行由后端工具层完成，并通过 schema 校验、权限、超时、重试和审计保证可靠性。

### 容易踩坑

- 回到开头踩的雷，最大的误区是觉得 WebSocket 和 WebRTC「都能传语音，差别不大」。
- 信任模型生成的工具参数，缺少 schema 校验和权限边界。
- 忽略工具失败、超时、重试、幂等和审计。

### 追问

1. 模型生成的 tool arguments 能不能直接信任？为什么？
2. 哪些工具调用必须做人工确认或权限隔离？
3. 工具 API 超时、失败或重复执行时，你怎么保证可靠性？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 16. 有没有用过大模型的网关框架？网关层解决了什么问题？

- 来源：[https://xiaolinnote.com/ai/tools/16_llm_gateway.html](https://xiaolinnote.com/ai/tools/16_llm_gateway.html)
- 本地原文：`interview-agent/sources/xiaolinnote/tools/16_llm_gateway.md`

### 考点

- Function Calling、工具协议、权限边界、参数校验、工具生态
- 先建立直觉：网关是什么，放在哪
- 没有网关时的痛点
- 多模型统一接口：换模型对业务代码隐形
- 负载均衡和故障转移：可靠性兜底

### 核心理解

我用过 LiteLLM，它是目前最活跃的开源 LLM 网关。我理解网关本质上是架在应用和模型 API 之间的中间层，主要解决几个实际问题。

### 面试回答

我用过 LiteLLM，它是目前最活跃的开源 LLM 网关。我理解网关本质上是架在应用和模型 API 之间的中间层，主要解决几个实际问题。

第一是多模型统一接口，业务代码只调一个地方，想换模型只改网关配置，不用动应用代码；第二是 API Key 集中管理，不用每个服务都存一份，降低泄漏风险。

第三是限流和配额，可以给不同团队分别设 token 预算，防止某个团队把整个公司的额度用光；第四是成本追踪，所有请求的 token 用量都在网关记录，方便统计哪个服务最烧钱。

还有一个我觉得挺实用的能力是语义缓存，两个用户问了语义相近的问题，直接命中缓存返回上次的结果，根本不打底层模型，省钱还降延迟。

### 工程例子

可以结合一个能查订单、发邮件或调用内部 API 的 Agent 来讲：模型只负责决定调用哪个工具和参数，真正执行由后端工具层完成，并通过 schema 校验、权限、超时、重试和审计保证可靠性。

### 容易踩坑

- 回到开头对话踩的雷，最常见的误区就是把 LLM 网关等同于普通的负载均衡器或反向代理。面试回答这道题，首先要说清楚网关的定位：它是架在应用和模型 API 之间的中间层，集中拦截和处理所有出入流量，所以能在这个位置统一做很多事情。
- 要避免的误区：不要只说负载均衡和统一接口，这两个普通 API 网关也能做。面试官想听的是你对 LLM 场景特有问题的理解，比如 token 配额管理、语义缓存、prompt 安全过滤这些只有 LLM 网关才需要的能力。如果用过具体框架（比如 LiteLLM、One API），能结合实际使用经验来说会更有说服力。
- 信任模型生成的工具参数，缺少 schema 校验和权限边界。

### 追问

1. 模型生成的 tool arguments 能不能直接信任？为什么？
2. 哪些工具调用必须做人工确认或权限隔离？
3. 工具 API 超时、失败或重复执行时，你怎么保证可靠性？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。

## 17. LLM工具调用面试题介绍

- 来源：[https://xiaolinnote.com/ai/tools/tools_info.html](https://xiaolinnote.com/ai/tools/tools_info.html)
- 本地原文：`interview-agent/sources/xiaolinnote/tools/tools_info.md`

### 考点

- Function Calling、工具协议、权限边界、参数校验、工具生态
- 题目目录

### 核心理解

---
type: source_note
source_type: xiaolinnote
topic: tools
status: raw
source_url: https://xiaolinnote.com/ai/tools/tools_info.html
title: "LLM工具调用面试题介绍"
content_hash: bde8d26c6e4853315245b2c2555f65021b338902df8dc6dfa36971bfab6ad097
updated: 2026-06-12T11:49:52+00:00
tags:
  - xiaolinnote
  - tools
  - interview
---

### 面试回答

---
type: source_note
source_type: xiaolinnote
topic: tools
status: raw
source_url: https://xiaolinnote.com/ai/tools/tools_info.html
title: "LLM工具调用面试题介绍"
content_hash: bde8d26c6e4853315245b2c2555f65021b338902df8dc6dfa36971bfab6ad097
updated: 2026-06-12T11:49:52+00:00
tags:
  - xiaolinnote
  - tools
  - interview
---

大家好，我是小林。

做 AI 应用，光让大模型能聊天是远远不够的，你得让它能「干活」，能查数据库、能调 API、能操作文件，这些能力的背后就是工具调用。Function Calling、MCP、A2A 这些概念现在面试里问得越来越多，但我发现很多同学对它们的理解还停留在「都是调工具的」这个层面，一追问就分不清谁是谁了，更别说解释它们之间的层级关系了。

### 工程例子

可以结合一个能查订单、发邮件或调用内部 API 的 Agent 来讲：模型只负责决定调用哪个工具和参数，真正执行由后端工具层完成，并通过 schema 校验、权限、超时、重试和审计保证可靠性。

### 容易踩坑

- 信任模型生成的工具参数，缺少 schema 校验和权限边界。
- 忽略工具失败、超时、重试、幂等和审计。

### 追问

1. 模型生成的 tool arguments 能不能直接信任？为什么？
2. 哪些工具调用必须做人工确认或权限隔离？
3. 工具 API 超时、失败或重复执行时，你怎么保证可靠性？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。
