#!/usr/bin/env python3
"""Fetch developer interview experiences from xiaozhao.bitejiuyeke.com."""

from __future__ import annotations

import argparse
import hashlib
import hmac
import html
import json
import random
import re
import string
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import requests


BASE_URL = "https://xiaozhao.bitejiuyeke.com"
LIST_URL = f"{BASE_URL}/friend/article/semiLogin/hot/list"
DETAIL_URL = f"{BASE_URL}/friend/article/semiLogin/detail"
SECRET = "09247ec02edce69f6a2d"
SECRET_ID = "BIT_AZ0tHd"
USER_AGENT = "AgentVaultBitejiuyekeFetcher/1.0 (+local knowledge base)"

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "interview-agent" / "sources" / "bitejiuyeke"
DATASET_PATH = ROOT / "interview-agent" / "datasets" / "bitejiuyeke-interviews.jsonl"
MANIFEST_PATH = ROOT / "interview-agent" / "datasets" / "bitejiuyeke-interviews-manifest.json"
QUESTION_BANK_PATH = ROOT / "interview-agent" / "question-bank" / "bitejiuyeke-interviews.md"


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
    args = parse_args(argv or sys.argv[1:])
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})

    if args.dry_run:
        rows = fetch_list_page(session, 1, args.page_size, args.job_type)
        for row in rows[: args.limit or len(rows)]:
            print(f"{row.get('topicId')} {row.get('title')}")
        return 0

    manifest = load_json(MANIFEST_PATH, {"source": BASE_URL, "pages": {}})
    records = load_existing_records()
    seen_ids = set(records)
    stats = {"created": 0, "updated": 0, "unchanged": 0, "failed": 0}
    fetched = 0

    for page_num in range(1, args.max_pages + 1):
        rows = fetch_list_page(session, page_num, args.page_size, args.job_type)
        if not rows:
            break
        for row in rows:
            topic_id = str(row.get("topicId") or "")
            if not topic_id:
                continue
            if args.limit is not None and fetched >= args.limit:
                break
            try:
                detail = fetch_detail(session, topic_id)
                record = normalize_record(detail)
                if not record:
                    continue
                digest = content_hash(record)
                old = manifest.get("pages", {}).get(topic_id)
                source_path = source_path_for(record)
                existed = source_path.exists() or topic_id in seen_ids
                if old and old.get("content_hash") == digest and not args.force:
                    stats["unchanged"] += 1
                else:
                    source_path.parent.mkdir(parents=True, exist_ok=True)
                    source_path.write_text(render_source_markdown(record, digest), encoding="utf-8", newline="\n")
                    record.update(
                        {
                            "id": f"bitejiuyeke-{topic_id}",
                            "source_url": f"{BASE_URL}/bbs/detail/{topic_id}/0",
                            "source_markdown": str(source_path.relative_to(ROOT)).replace("\\", "/"),
                            "content_hash": digest,
                            "updated_at": now_iso(),
                        }
                    )
                    records[topic_id] = record
                    manifest.setdefault("pages", {})[topic_id] = {
                        "title": record["title"],
                        "company": record["company"],
                        "post": record["post"],
                        "job_type": record["job_type"],
                        "source_markdown": record["source_markdown"],
                        "content_hash": digest,
                        "updated_at": now_iso(),
                    }
                    stats["updated" if existed else "created"] += 1
                fetched += 1
                print(f"[page {page_num}] {topic_id} {record['title']}")
            except Exception as exc:  # noqa: BLE001
                stats["failed"] += 1
                print(f"failed topic {topic_id}: {exc}", file=sys.stderr)
            if args.delay > 0:
                time.sleep(args.delay)
        if args.limit is not None and fetched >= args.limit:
            break

    write_records(records)
    write_json(MANIFEST_PATH, manifest)
    write_question_bank(records)
    print(
        "Done: "
        f"created={stats['created']} updated={stats['updated']} "
        f"unchanged={stats['unchanged']} failed={stats['failed']} total_records={len(records)}"
    )
    return 1 if stats["failed"] else 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch bitejiuyeke developer interview experiences.")
    parser.add_argument("--limit", type=int, help="Maximum detail pages to fetch.")
    parser.add_argument("--max-pages", type=int, default=20, help="Maximum list pages to scan.")
    parser.add_argument("--page-size", type=int, default=20, help="List page size.")
    parser.add_argument("--job-type", default="0", help="Job type filter; 0 means all.")
    parser.add_argument("--delay", type=float, default=0.5, help="Delay between detail requests.")
    parser.add_argument("--force", action="store_true", help="Rewrite existing records even if unchanged.")
    parser.add_argument("--dry-run", action="store_true", help="Print first page list entries without writing.")
    return parser.parse_args(argv)


def signed_headers(params: dict | None = None, data: dict | None = None, method: str = "get") -> dict:
    params = params or {}
    data = data or {}
    nonce = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
    timestamp = str(int(time.time() * 1000))
    headers = {
        "bit-secretId": SECRET_ID,
        "bit-nonce": nonce,
        "bit-timestamp": timestamp,
        "User-Agent": USER_AGENT,
        "Content-Type": "application/json;charset=utf-8",
    }
    if method == "get":
        values = {**params, **headers}
    else:
        body = json.dumps(data, ensure_ascii=False, separators=(",", ":")) if data else ""
        values = {"bodyStr": body, **headers}
    payload = "".join(str(values[key]) for key in sorted(values)) + SECRET
    headers["bit-sign"] = hmac.new(SECRET.encode(), payload.encode(), hashlib.sha256).hexdigest().upper()
    return headers


def fetch_list_page(session: requests.Session, page_num: int, page_size: int, job_type: str) -> list[dict]:
    params = {
        "pageNum": page_num,
        "pageSize": page_size,
        "topicType": 0,
        "sectionId": "0",
        "sectionUnionId": "0",
        "title": "",
        "schoolId": "",
        "companyId": "",
        "postId": "",
        "sortType": "1",
        "jobType": job_type,
    }
    response = session.get(LIST_URL, params=params, headers=signed_headers(params), timeout=30)
    response.raise_for_status()
    payload = response.json()
    return payload.get("rows") or []


def fetch_detail(session: requests.Session, topic_id: str) -> dict:
    params = {"topicId": topic_id}
    response = session.get(DETAIL_URL, params=params, headers=signed_headers(params), timeout=30)
    response.raise_for_status()
    payload = response.json()
    if payload.get("code") != 200:
        raise RuntimeError(payload)
    return payload.get("data") or {}


def normalize_record(detail: dict) -> dict | None:
    topic_id = str(detail.get("topicId") or "")
    title = clean_text(detail.get("title") or "")
    content = html_to_markdown(detail.get("content") or detail.get("briefContent") or "")
    if not topic_id or not title or not content:
        return None
    return {
        "topic_id": topic_id,
        "title": title,
        "company": clean_text(detail.get("companyName") or ""),
        "post": clean_text(detail.get("postName") or ""),
        "stage": clean_text(detail.get("stage") or ""),
        "job_type": detail.get("jobType"),
        "section": clean_text(detail.get("sectionTypeName") or "#面经"),
        "author": clean_text(detail.get("publishName") or ""),
        "create_time": clean_text(detail.get("createTime") or ""),
        "view_count": detail.get("viewCount") or 0,
        "like_count": detail.get("likeCount") or 0,
        "collect_count": detail.get("collectCount") or 0,
        "comment_count": detail.get("commentCount") or 0,
        "content": content,
        "questions": extract_questions(content),
        "tags": infer_tags(title, content, detail),
    }


def html_to_markdown(raw: str) -> str:
    text = raw.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)
    text = re.sub(r"</p\s*>", "\n\n", text, flags=re.I)
    text = re.sub(r"<p[^>]*>", "", text, flags=re.I)
    text = re.sub(r"<li[^>]*>", "- ", text, flags=re.I)
    text = re.sub(r"</li\s*>", "\n", text, flags=re.I)
    text = re.sub(r"<h([1-6])[^>]*>", lambda m: "\n" + "#" * int(m.group(1)) + " ", text, flags=re.I)
    text = re.sub(r"</h[1-6]\s*>", "\n\n", text, flags=re.I)
    text = re.sub(r'<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', lambda m: f"[{strip_tags(m.group(2))}]({m.group(1)})", text, flags=re.I | re.S)
    text = strip_tags(text)
    text = html.unescape(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def strip_tags(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text)


def clean_text(text: str) -> str:
    return html.unescape(str(text)).strip()


def extract_questions(content: str) -> list[str]:
    questions: list[str] = []
    for line in content.splitlines():
        raw = line.strip()
        line = raw
        line = re.sub(r"^[-*]\s*", "", line)
        numbered = bool(re.match(r"^\d+[.、]\s*", line))
        line = re.sub(r"^\d+[.、]\s*", "", line)
        if len(line) < 4:
            continue
        if numbered or "？" in line or "?" in line or re.match(r"^(介绍|说说|讲讲|如何|怎么|什么|为什么|有没有|是否)", line):
            questions.append(line)
    deduped: list[str] = []
    for question in questions:
        if question not in deduped:
            deduped.append(question)
    return deduped[:50]


def infer_tags(title: str, content: str, detail: dict) -> list[str]:
    haystack = f"{title}\n{content}"
    tags = ["bitejiuyeke", "interview-experience"]
    post = clean_text(detail.get("postName") or "")
    company = clean_text(detail.get("companyName") or "")
    if company:
        tags.append(company)
    if post:
        tags.append(post)
    keywords = {
        "cpp": ["C++", "右值", "vector", "STL"],
        "backend": ["后端", "Java", "Redis", "MySQL", "TCP", "HTTP", "Linux"],
        "algorithm": ["算法", "LeetCode", "二叉树", "哈希", "排序", "动态规划"],
        "database": ["MySQL", "数据库", "索引", "事务"],
        "cache": ["Redis", "缓存"],
        "network": ["TCP", "HTTP", "网络", "epoll"],
        "os": ["进程", "线程", "操作系统", "Linux"],
    }
    for tag, words in keywords.items():
        if any(word in haystack for word in words):
            tags.append(tag)
    return list(dict.fromkeys(tags))


def content_hash(record: dict) -> str:
    payload = json.dumps(
        {
            "title": record["title"],
            "company": record["company"],
            "post": record["post"],
            "content": record["content"],
        },
        ensure_ascii=False,
        sort_keys=True,
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def source_path_for(record: dict) -> Path:
    company = slugify(record["company"] or "unknown-company")
    slug = slugify(record["title"])
    return SOURCE_ROOT / company / f"{record['topic_id']}-{slug}.md"


def render_source_markdown(record: dict, digest: str) -> str:
    frontmatter = [
        "---",
        "type: interview_experience",
        "source_type: bitejiuyeke",
        "status: raw",
        f"topic_id: {record['topic_id']}",
        f"source_url: {BASE_URL}/bbs/detail/{record['topic_id']}/0",
        f"title: {json.dumps(record['title'], ensure_ascii=False)}",
        f"company: {json.dumps(record['company'], ensure_ascii=False)}",
        f"post: {json.dumps(record['post'], ensure_ascii=False)}",
        f"stage: {json.dumps(record['stage'], ensure_ascii=False)}",
        f"content_hash: {digest}",
        f"updated: {now_iso()}",
        "tags:",
    ]
    frontmatter.extend(f"  - {tag}" for tag in record["tags"])
    frontmatter.append("---")
    meta = [
        f"# {record['title']}",
        "",
        f"> 来源：{BASE_URL}/bbs/detail/{record['topic_id']}/0",
        "",
        f"- 公司：{record['company'] or '未知'}",
        f"- 岗位：{record['post'] or '未知'}",
        f"- 轮次：{record['stage'] or '未知'}",
        f"- 时间：{record['create_time'] or '未知'}",
        "",
        "## 面经原文",
        "",
        record["content"],
    ]
    if record["questions"]:
        meta.extend(["", "## 提取问题", ""])
        meta.extend(f"{idx}. {question}" for idx, question in enumerate(record["questions"], start=1))
    return "\n".join(frontmatter + [""] + meta).rstrip() + "\n"


def write_question_bank(records: dict[str, dict]) -> None:
    ordered = sorted(records.values(), key=lambda r: (r.get("company") or "", r.get("create_time") or "", r["title"]))
    QUESTION_BANK_PATH.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "---",
        "type: question_bank",
        "source_type: bitejiuyeke",
        "status: reviewed",
        f"updated: {datetime.now().strftime('%Y-%m-%d')}",
        "tags:",
        "  - bitejiuyeke",
        "  - interview-experience",
        "---",
        "",
        "# 比特就业课开发面经整理",
        "",
        "> 说明：本文件由 `tools/fetch_bitejiuyeke_interviews.py` 抓取并生成，属于外部面经资料层，适合做项目/八股/算法追问素材。",
        "",
    ]
    for index, record in enumerate(ordered, start=1):
        lines.extend(render_bank_card(index, record))
    QUESTION_BANK_PATH.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")


def render_bank_card(index: int, record: dict) -> list[str]:
    questions = record.get("questions") or []
    lines = [
        f"## {index}. {record['title']}",
        "",
        f"- 公司：{record.get('company') or '未知'}",
        f"- 岗位：{record.get('post') or '未知'}",
        f"- 轮次：{record.get('stage') or '未知'}",
        f"- 来源：[{record['source_url']}]({record['source_url']})",
        f"- 本地原文：`{record['source_markdown']}`",
        "",
        "### 考点",
        "",
    ]
    tags = [tag for tag in record.get("tags", []) if tag not in {"bitejiuyeke", "interview-experience"}]
    if tags:
        lines.extend(f"- {tag}" for tag in tags[:8])
    else:
        lines.append("- 开发基础、项目经历、算法和岗位匹配度")
    lines.extend(["", "### 面试问题摘录", ""])
    if questions:
        lines.extend(f"{idx}. {question}" for idx, question in enumerate(questions[:20], start=1))
    else:
        lines.append("1. 需要从原文继续人工提炼。")
    lines.extend(
        [
            "",
            "### 复盘提示",
            "",
            "- 先按知识点归类：项目、语言基础、数据库、网络、操作系统、算法、场景设计。",
            "- 对每个问题准备 1 分钟版本和 3 分钟深入版本。",
            "- 把不会的问题加入个人错题库，并补一个工程例子。",
            "",
        ]
    )
    return lines


def load_existing_records() -> dict[str, dict]:
    records: dict[str, dict] = {}
    if not DATASET_PATH.exists():
        return records
    for line in DATASET_PATH.read_text(encoding="utf-8").splitlines():
        if line.strip():
            record = json.loads(line)
            records[str(record["topic_id"])] = record
    return records


def write_records(records: dict[str, dict]) -> None:
    DATASET_PATH.parent.mkdir(parents=True, exist_ok=True)
    ordered = sorted(records.values(), key=lambda r: (r.get("company") or "", r.get("create_time") or "", r["title"]))
    with DATASET_PATH.open("w", encoding="utf-8", newline="\n") as handle:
        for record in ordered:
            handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")


def load_json(path: Path, default: dict) -> dict:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data["updated_at"] = now_iso()
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def slugify(text: str) -> str:
    text = re.sub(r"[\\/:*?\"<>|]+", "-", text)
    text = re.sub(r"\s+", "-", text.strip())
    return text[:80] or "untitled"


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


if __name__ == "__main__":
    raise SystemExit(main())
