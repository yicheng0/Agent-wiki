# Agent Interview Vault

这个仓库正在从“大模型学习资料库”升级为“Agent 岗位面试训练知识库”。目标不是单纯收藏文章，而是把资料整理成面试 Agent 可以直接使用的结构：能讲题、能出题、能追问、能评分、能复盘。

## 当前定位

面向岗位：

- Agent 工程师
- RAG 工程师
- LLM 应用工程师
- AI 全栈工程师
- Coding Agent / AI Coding 方向

核心能力：

- 解释 Agent、RAG、tool calling、memory、evaluation、safety 等高频概念
- 生成初级/中级/高级面试题
- 根据回答进行五维评分
- 围绕项目经历做深挖追问
- 把原始资料沉淀为可检索、可评估的问答卡片

## 目录结构

```text
interview-agent/
  README.md                  面试 Agent 知识库使用说明
  curriculum/                能力地图和学习路径
  question-bank/             题库与场景追问
  rubrics/                   回答评分标准
  templates/                 新增笔记和面试卡片模板
  datasets/                  可供 Agent/RAG 使用的结构化样例数据

01-RAG解决方案/              RAG 学习和面试资料
手撕代码/                    深度学习、NLP、强化学习等手写代码笔记
AI学习资料/                  Agent / Hermes / AI 工具资料
笔记同步助手/                外部文章剪藏和同步资料
```

## 推荐工作流

1. 原始文章继续放到 `笔记同步助手/` 或对应主题目录。
2. 读完后按 `interview-agent/templates/source-note.md` 提炼成结构化资料。
3. 高价值内容再转成 `interview-agent/templates/interview-card.md` 格式。
4. 稳定题目同步到 `interview-agent/question-bank/`。
5. 可直接喂给 Agent/RAG 的样例放到 `interview-agent/datasets/qa-cards.jsonl`。

## 资料状态约定

- `raw`: 原始剪藏，只做存档
- `reviewed`: 已读过，确认有价值
- `curated`: 已提炼成面试知识
- `qa`: 已转成问答卡片
- `gold`: 可作为标准答案来源

## 优先补齐方向

- RAG: chunking、embedding、rerank、评估、排错
- Tool calling: schema、权限、重试、幂等、审计
- Agent loop: planning、state、termination、human-in-the-loop
- Memory: 写入策略、召回策略、隐私和过期
- Evaluation: 轨迹评估、回归测试、线上观测
- Safety: prompt injection、工具边界、敏感操作确认
- Project story: 用 STAR + 工程深度组织个人项目经历

## 使用建议

如果你要模拟面试，可以让 Agent 先读取：

1. `interview-agent/curriculum/00-knowledge-map.md`
2. `interview-agent/rubrics/answer-scoring.md`
3. 对应方向的 `question-bank/*.md`

如果你要把新文章变成题库，先套 `templates/source-note.md`，再提炼成 `templates/interview-card.md`。
