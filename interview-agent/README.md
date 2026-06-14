# Interview Agent Knowledge Base

这里是给面试 Agent 使用的“精选层”。原始剪藏不直接作为标准答案来源，先在这里被整理成能力地图、题库、评分规则和结构化数据。

## 这个目录解决什么问题

原始学习笔记适合人看，但面试 Agent 需要更稳定的输入：

- 知道一个问题在考什么
- 能给出结构化标准答案
- 能根据用户回答继续追问
- 能用统一 rubric 打分
- 能引用来源，但不被低质量剪藏污染

## 使用顺序

1. `curriculum/00-knowledge-map.md`: 定义 Agent 面试的能力地图。
2. `question-bank/agent-engineer-core.md`: 常规概念题、架构题和工程题。
3. `question-bank/scenario-debugging.md`: 生产事故、故障排查、可靠性场景题。
4. `rubrics/answer-scoring.md`: 评分标准。
5. `datasets/qa-cards.jsonl`: 后续接 RAG 或本地 Agent 时可直接读取的样例。

## 外部题库整理

`question-bank/xiaolinnote/` 保存从小林面试笔记 AI 栏目抓取并排版后的题库，按主题分成 Agent、RAG、Tools、LLM、LangChain。它们是 `reviewed` 外部资料层，适合检索、出题和二次精炼，但不直接等同于手工精选答案。

`question-bank/bitejiuyeke-interviews.md` 保存从比特就业课论坛抓取的开发面经汇总，按公司、岗位、轮次和问题摘录组织。原文保存在 `sources/bitejiuyeke/`，结构化数据保存在 `datasets/bitejiuyeke-interviews.jsonl`。

`question-bank/feishu/` 保存从飞书知识库截图人工整理的 Agent 面试题，按截图章节顺序分类编号。对应的截图摘录保存在 `sources/feishu/`，用于后续补图或核对原文。

相关数据和脚本：

- 原文 Markdown: `sources/xiaolinnote/`
- 结构化 JSONL: `datasets/xiaolinnote-ai-qa.jsonl`
- 抓取脚本: `../tools/fetch_xiaolinnote_ai.py`
- 排版脚本: `../tools/build_xiaolinnote_interview_cards.py`
- 比特就业课抓取脚本: `../tools/fetch_bitejiuyeke_interviews.py`

## 新资料怎么进来

```text
raw article -> source-note -> interview-card -> question-bank -> qa-cards.jsonl
```

不要把所有剪藏都直接进题库。先判断它是否能产生面试价值：

- 是否解释了一个高频概念？
- 是否包含真实工程权衡？
- 是否能转成一道问题？
- 是否能形成追问？
- 是否能帮助评分？

## 推荐的 Agent 行为

面试 Agent 回答时应遵循：

- 中文优先，关键术语保留英文
- 先说考点，再说核心理解
- 必须给工程例子
- 必须指出常见坑
- 每轮最多追问 1-3 个问题
- 评分时使用五维 rubric: 准确性、结构性、工程感、深度、表达
