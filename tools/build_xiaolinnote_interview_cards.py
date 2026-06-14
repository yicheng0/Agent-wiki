#!/usr/bin/env python3
"""Build formatted interview-card markdown files from xiaolinnote JSONL data."""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATASET_PATH = ROOT / "interview-agent" / "datasets" / "xiaolinnote-ai-qa.jsonl"
OUTPUT_ROOT = ROOT / "interview-agent" / "question-bank" / "xiaolinnote"

TOPIC_NAMES = {
    "agent": "Agent",
    "rag": "RAG",
    "tools": "Tool Calling / MCP / Skills",
    "llm": "LLM 基础与工程",
    "langchain": "LangChain",
}

TOPIC_INTENTS = {
    "agent": "Agent loop、自主规划、状态/记忆、工具执行、可靠性边界",
    "rag": "检索增强生成、文档处理、召回质量、重排、评估与排错",
    "tools": "Function Calling、工具协议、权限边界、参数校验、工具生态",
    "llm": "大模型基础、训练/推理、模型选型、部署优化和评估",
    "langchain": "框架抽象、链式编排、组件边界和工程取舍",
}

ENGINEERING_EXAMPLES = {
    "agent": "可以结合一个 Coding Agent 或运营助手来讲：用户给出目标后，系统先规划步骤，再调用搜索、文件、代码执行或 API 工具，每一步观察结果都会写回状态，并决定下一步继续、重试还是停止。",
    "rag": "可以结合企业知识库问答来讲：离线阶段清洗文档、切块、向量化并写入索引；在线阶段先检索和重排，再把高相关片段交给模型回答，并记录检索结果、引用和失败样例用于评估。",
    "tools": "可以结合一个能查订单、发邮件或调用内部 API 的 Agent 来讲：模型只负责决定调用哪个工具和参数，真正执行由后端工具层完成，并通过 schema 校验、权限、超时、重试和审计保证可靠性。",
    "llm": "可以结合一个 LLM 应用上线流程来讲：根据任务选择模型和推理参数，设计 prompt 或微调方案，做离线评估和线上监控，并持续关注成本、延迟、稳定性和安全边界。",
    "langchain": "可以结合 RAG 或 Agent 原型来讲：用框架快速组合 loader、retriever、prompt、model 和 tool，但生产落地时要明确哪些抽象保留，哪些链路需要自己控制和观测。",
}

FOLLOWUPS = {
    "agent": [
        "这个能力和普通 LLM / workflow / tool calling 的边界在哪里？",
        "如果 Agent 中途跑偏或工具失败，你会怎么恢复？",
        "生产环境里你会记录哪些 trace 来定位问题？",
    ],
    "rag": [
        "如果答案不准，你怎么判断是 retrieval 问题还是 generation 问题？",
        "chunking、embedding、rerank 分别会怎样影响最终效果？",
        "你会如何设计 RAG 的 eval set 和线上监控指标？",
    ],
    "tools": [
        "模型生成的 tool arguments 能不能直接信任？为什么？",
        "哪些工具调用必须做人工确认或权限隔离？",
        "工具 API 超时、失败或重复执行时，你怎么保证可靠性？",
    ],
    "llm": [
        "这个机制会如何影响成本、延迟或质量？",
        "如果模型升级导致效果回归，你怎么发现和处理？",
        "哪些指标能证明你的方案真的更好？",
    ],
    "langchain": [
        "什么时候用框架抽象，什么时候自己写编排？",
        "框架封装会给调试和观测带来什么问题？",
        "如果要上生产，你会补哪些可靠性设计？",
    ],
}


def main() -> int:
    if not DATASET_PATH.exists():
        print(f"Missing dataset: {DATASET_PATH}", file=sys.stderr)
        return 1

    records = load_records(DATASET_PATH)
    by_topic: dict[str, list[dict]] = defaultdict(list)
    for record in records:
        by_topic[record["topic"]].append(record)

    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    for topic, topic_records in sorted(by_topic.items()):
        topic_records.sort(key=sort_key)
        write_topic_file(topic, topic_records)
    write_index(by_topic)
    print(f"Built {sum(len(v) for v in by_topic.values())} cards in {OUTPUT_ROOT}")
    return 0


def load_records(path: Path) -> list[dict]:
    records = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                records.append(json.loads(line))
    return records


def sort_key(record: dict) -> tuple[int, str]:
    slug = Path(record["source_url"]).stem
    match = re.match(r"(\d+)", slug)
    number = int(match.group(1)) if match else 9999
    return number, slug


def write_topic_file(topic: str, records: list[dict]) -> None:
    title = TOPIC_NAMES.get(topic, topic)
    lines = [
        "---",
        "type: question_bank",
        f"topic: {topic}",
        "source_type: xiaolinnote",
        "status: reviewed",
        f"updated: {today()}",
        "tags:",
        "  - xiaolinnote",
        "  - interview",
        f"  - {topic}",
        "---",
        "",
        f"# 小林面试题 - {title}",
        "",
        "> 说明：本文件由 `tools/build_xiaolinnote_interview_cards.py` 从 `xiaolinnote-ai-qa.jsonl` 生成，属于外部资料整理层，未合并进手工精选题库。",
        "",
    ]
    for index, record in enumerate(records, start=1):
        lines.extend(render_card(index, record))
    (OUTPUT_ROOT / f"{topic}.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")


def render_card(index: int, record: dict) -> list[str]:
    topic = record["topic"]
    question = clean_question(record["question"])
    headings = useful_headings(record.get("headings", []))
    summary = strip_noise(record.get("answer_summary", ""))
    core = first_paragraph(summary)
    answer = summary or "这道题需要结合来源原文进一步整理。"
    pitfalls = pitfalls_from_summary(record.get("interview_summary", ""), topic)
    source_markdown = record.get("source_markdown", "")
    source_url = record.get("source_url", "")

    lines = [
        f"## {index}. {question}",
        "",
        f"- 来源：[{source_url}]({source_url})",
        f"- 本地原文：`{source_markdown}`",
        "",
        "### 考点",
        "",
        f"- {TOPIC_INTENTS.get(topic, '核心概念、工程边界和面试表达')}",
    ]
    for heading in headings[:4]:
        lines.append(f"- {heading}")

    lines.extend(
        [
            "",
            "### 核心理解",
            "",
            core or answer,
            "",
            "### 面试回答",
            "",
            answer,
            "",
            "### 工程例子",
            "",
            ENGINEERING_EXAMPLES.get(topic, "结合一个真实 LLM 应用来讲清楚输入、处理链路、失败恢复、评估和上线约束。"),
            "",
            "### 容易踩坑",
            "",
        ]
    )
    for item in pitfalls:
        lines.append(f"- {item}")

    lines.extend(["", "### 追问", ""])
    for i, question_text in enumerate(FOLLOWUPS.get(topic, FOLLOWUPS["llm"]), start=1):
        lines.append(f"{i}. {question_text}")

    lines.extend(
        [
            "",
            "### 评分提示",
            "",
            "- 3 分：能说清基本定义和主要流程，有一个简单例子。",
            "- 5 分：能主动讲清工程边界、失败场景、评估指标、成本/延迟/安全等 tradeoff。",
            "",
        ]
    )
    return lines


def write_index(by_topic: dict[str, list[dict]]) -> None:
    lines = [
        "---",
        "type: question_bank_index",
        "source_type: xiaolinnote",
        "status: reviewed",
        f"updated: {today()}",
        "tags:",
        "  - xiaolinnote",
        "  - interview",
        "---",
        "",
        "# 小林 AI 面试题整理索引",
        "",
        "这些文件由抓取数据自动排版生成，适合面试 Agent 检索和出题。手工精选仍放在上一级题库文件中。",
        "",
        "| 主题 | 数量 | 文件 |",
        "| --- | ---: | --- |",
    ]
    for topic, records in sorted(by_topic.items()):
        lines.append(f"| {TOPIC_NAMES.get(topic, topic)} | {len(records)} | [{topic}.md]({topic}.md) |")
    lines.extend(
        [
            "",
            "## 数据来源",
            "",
            "- 原始 JSONL：`interview-agent/datasets/xiaolinnote-ai-qa.jsonl`",
            "- 原文 Markdown：`interview-agent/sources/xiaolinnote/`",
            "- 生成脚本：`tools/build_xiaolinnote_interview_cards.py`",
        ]
    )
    (OUTPUT_ROOT / "README.md").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")


def clean_question(question: str) -> str:
    return re.sub(r"^\d+\.\s*", "", question).strip()


def useful_headings(headings: list[str]) -> list[str]:
    ignored = {"💡 简要回答", "📝 详细解析", "🎯 面试总结"}
    result = []
    for heading in headings[1:]:
        heading = heading.strip()
        if not heading or heading in ignored:
            continue
        if heading not in result:
            result.append(heading)
    return result


def first_paragraph(text: str) -> str:
    for paragraph in re.split(r"\n\s*\n", text.strip()):
        paragraph = paragraph.strip()
        if paragraph:
            return paragraph
    return ""


def strip_noise(text: str) -> str:
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)
    text = re.sub(r"对了，AI Agent的面试题会在[\s\S]*$", "", text)
    return text.strip()


def pitfalls_from_summary(summary: str, topic: str) -> list[str]:
    summary = strip_noise(summary)
    items: list[str] = []
    for paragraph in re.split(r"\n\s*\n", summary):
        paragraph = paragraph.strip()
        if not paragraph:
            continue
        if "雷" in paragraph or "误区" in paragraph or "注意" in paragraph:
            items.append(paragraph)
        if len(items) >= 3:
            break
    defaults = {
        "agent": ["把 Agent 简化成普通工具调用，忽略自主规划和执行闭环。", "只讲概念，不讲状态、记忆、终止条件和失败恢复。"],
        "rag": ["把 RAG 简化成向量搜索，忽略生成、重排、引用和评估。", "答案不准时只改 prompt，不先检查检索结果和 trace。"],
        "tools": ["信任模型生成的工具参数，缺少 schema 校验和权限边界。", "忽略工具失败、超时、重试、幂等和审计。"],
        "llm": ["只背术语，不讲它对质量、成本、延迟和上线风险的影响。", "混淆训练、推理、微调、对齐和评估等相近概念。"],
        "langchain": ["只讲框架用法，不讲抽象边界、调试和生产可靠性。"],
    }
    for item in defaults.get(topic, defaults["llm"]):
        if len(items) >= 3:
            break
        items.append(item)
    return items[:3]


def today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


if __name__ == "__main__":
    raise SystemExit(main())
