---
type: question_bank
topic: langchain
source_type: xiaolinnote
status: reviewed
updated: 2026-06-12
tags:
  - xiaolinnote
  - interview
  - langchain
---


## 1. LangChain框架面试题介绍

- 来源：[https://xiaolinnote.com/ai/langchain/langchain_info.html](https://xiaolinnote.com/ai/langchain/langchain_info.html)
- 本地原文：`interview-agent/sources/xiaolinnote/langchain/langchain_info.md`

### 考点

- 框架抽象、链式编排、组件边界和工程取舍

### 核心理解

---
type: source_note
source_type: xiaolinnote
topic: langchain
status: raw
source_url: https://xiaolinnote.com/ai/langchain/langchain_info.html
title: "LangChain框架面试题介绍"
content_hash: 20b4bf4ad1ba0fcf3643d60a8141081298f421945b868957cc7a874afaf3dfb6
updated: 2026-06-12T11:49:14+00:00
tags:
  - xiaolinnote
  - langchain
  - interview
---

### 面试回答

---
type: source_note
source_type: xiaolinnote
topic: langchain
status: raw
source_url: https://xiaolinnote.com/ai/langchain/langchain_info.html
title: "LangChain框架面试题介绍"
content_hash: 20b4bf4ad1ba0fcf3643d60a8141081298f421945b868957cc7a874afaf3dfb6
updated: 2026-06-12T11:49:14+00:00
tags:
  - xiaolinnote
  - langchain
  - interview
---


### 工程例子

可以结合 RAG 或 Agent 原型来讲：用框架快速组合 loader、retriever、prompt、model 和 tool，但生产落地时要明确哪些抽象保留，哪些链路需要自己控制和观测。

### 容易踩坑

- 只讲框架用法，不讲抽象边界、调试和生产可靠性。

### 追问

1. 什么时候用框架抽象，什么时候自己写编排？
2. 框架封装会给调试和观测带来什么问题？
3. 如果要上生产，你会补哪些可靠性设计？

### 评分提示

- 3 分：能说清基本定义和主要流程，有一个简单例子。
- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。
