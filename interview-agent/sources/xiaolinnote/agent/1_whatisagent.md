---
type: source_note
source_type: xiaolinnote
topic: agent
status: raw
source_url: https://xiaolinnote.com/ai/agent/1_whatisagent.html
title: "1. 什么是 Agent？与大模型有什么本质不同？"
content_hash: 01363de86dd0fcb7aaf2300b2aa1c925b5ba2b03e8a309d943424719600c5f6e
updated: 2026-06-12T11:48:29+00:00
tags:
  - xiaolinnote
  - agent
  - interview
---

# 1. 什么是 Agent？与大模型有什么本质不同？


##  简要回答

我理解 Agent 本质上是一个能自主完成目标的 AI 系统，跟传统 AI 最核心的区别在于「自主性」和「能行动」。

Agentt本质上是一个围绕目标运行的系统，而不只是一次输入输出的模型调用。它通常会在多步执行中基于当前观察结果动态决定下一步动作，并通过工具或外部环境持续推进任务完成。

和普通chatbot相比，Agent具有规划能力，给它一个复杂目标，会把任务拆分成多步，通过调工具、访问记忆、感知环境一步一步完成指定的任务；和workflow相比，Agent的关键差异在于运行时有更高的决策自由度，而不是所有步骤都预先写死。

在工程上，我会把Agentt看成由目标、策略/规划、工具、状态/记忆、控制约束和校验机制组成。是否应该用Aget,要看任务路径是否不确定、是否需要多轮环境交互，以及引入自治后能否接受成本、延迟和风险。


Agent 就完全不一样了。它有一个核心的运作闭环：感知 -> 规划 -> 行动 -> 再感知。

![](https://cdn.xiaolincoding.com//picgo/4a13bf9723d1882518cb6716bfad078d.png)


一个生产级别的agent应该有的最小框架：
Goal/Task 、 Policy/Planner 、 Tools/Environment 、 State/Memory、 Guardrails/Governance、 Evaluator/Verifier


![](https://cdn.xiaolincoding.com//picgo/image-20260305202625429.png?image_process=watermark,text_eGlhb2xpbm5vdGUuY29tQOWwj-ael-mdouivleeslOiusA,g_south,size_35,type_aHloZWk,color_304ffe)

第一件：工具调用（Tool Use），这是让 Agent 从「说话」变成「做事」的关键。Agent 能调用外部工具，比如搜索引擎、代码执行器、数据库、API 等等。不过这里有一个容易误解的地方：不是模型自己执行，而是模型「告诉你该调什么」，你的代码去真正执行，结果再反馈给模型。模型始终只是大脑，不是手脚。


![](https://cdn.xiaolincoding.com//picgo/45666d3465d37176337f3c11313c524c.png)



![](https://cdn.xiaolincoding.com//picgo/76ca50010773832fc1bdf95dabe799ac.png)

第二件：记忆机制。传统 LLM 每次对话都是「失忆」的，除非你手动传上下文，不然它完全不记得上一次说了什么。而 Agent 系统通常会设计短期记忆和长期记忆两层。短期记忆就是当前任务执行过程中的中间状态，比如第一步搜索到了什么、第二步计算结果是多少，这些都存在上下文里，保证 Agent 不会做到一半忘了前面发生了什么。长期记忆则是跨任务的，比如用户的偏好、历史操作记录，通常用向量数据库来存储，需要的时候做语义检索拿回来。有了这两层记忆，Agent 在执行复杂任务时才能保持连贯性，不会走着走着忘了目标是什么。


第三件：多步推理和自我纠错。这一点经常被忽略，但其实是 Agent 区别于简单自动化脚本的关键。

Agent 在执行过程中如果某一步失败了，它不会直接崩掉，而是能感知到失败、分析原因、换一种方式重试。比如用关键词 A 搜索没找到有用信息，它会自己换关键词 B 再搜一次；调用某个 API 报错了，它会看报错信息然后调整参数重新调用。



![](https://cdn.xiaolincoding.com//picgo/2dacd3923d9a43e0d405660c3b13bc57.png)




回顾开头的对话，踩了三个典型的雷。

第一个雷是把 Agent 等同于「插件」或「工具调用」，这是最常见的误区，工具调用只是 Agent 能力的一部分，不是 Agent 本身。

第二个雷是停在「能调工具」这一层，没有点出自主性，Agent 的关键不是「有工具」，而是「自己决定用不用、什么时候用、用哪个」。

第三个雷是忽略了执行闭环，感知 -> 规划 -> 行动 -> 再感知这个循环才是 Agent 区别于普通 LLM 的核心机制。

面试时答这道题，一定要点出三件事：一是 Agent 有自主规划能力，给它一个复杂目标它能自己拆解成多步；二是它能行动，通过工具调用跟外部世界真实交互；三是它有闭环，每步的结果会反馈回来指导下一步，而不是一次性生成完就结束。另外还要提一句容易混的点：模型本身只是「大脑」，工具的真正执行是你的代码，模型只负责决策。



