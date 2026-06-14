#!/usr/bin/env python3
"""Fetch xiaolinnote.com AI interview pages into local interview-agent data.

The script intentionally uses only requests plus the Python standard library so
it can run in this vault without adding dependencies.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin, urlparse
from urllib.robotparser import RobotFileParser
from xml.etree import ElementTree

import requests


BASE_URL = "https://xiaolinnote.com"
SITEMAP_URL = f"{BASE_URL}/sitemap.xml"
ROBOTS_URL = f"{BASE_URL}/robots.txt"
USER_AGENT = "AgentVaultXiaolinFetcher/1.0 (+local knowledge base)"
VALID_SECTIONS = {"agent", "rag", "tools", "llm", "langchain"}

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = ROOT / "interview-agent" / "sources" / "xiaolinnote"
DATASET_PATH = ROOT / "interview-agent" / "datasets" / "xiaolinnote-ai-qa.jsonl"
MANIFEST_PATH = ROOT / "interview-agent" / "datasets" / "xiaolinnote-ai-manifest.json"


@dataclass
class MarkdownPage:
    title: str = ""
    lines: list[str] = field(default_factory=list)
    headings: list[str] = field(default_factory=list)

    @property
    def markdown(self) -> str:
        cleaned: list[str] = []
        blank = False
        for raw in self.lines:
            line = raw.rstrip()
            if not line:
                if not blank:
                    cleaned.append("")
                blank = True
                continue
            cleaned.append(line)
            blank = False
        return "\n".join(cleaned).strip() + "\n"


class MainContentParser(HTMLParser):
    """Small HTML-to-Markdown parser tuned for VuePress pages."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_main = False
        self.skip_depth = 0
        self.current_tag: str | None = None
        self.current_text: list[str] = []
        self.href: str | None = None
        self.list_depth = 0
        self.in_pre = False
        self.page = MarkdownPage()
        self._seen_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {k: v or "" for k, v in attrs}
        if tag == "main" and attrs_dict.get("id") == "main-content":
            self.in_main = True
            return
        if not self.in_main:
            return

        if self.skip_depth:
            self.skip_depth += 1
            return

        if tag in {"script", "style"}:
            self.skip_depth = 1
            return

        if tag in {"h1", "h2", "h3", "h4", "p", "li"}:
            self._flush_text()
            self.current_tag = tag
            self.current_text = []
        elif tag == "br":
            self.current_text.append("\n")
        elif tag == "a":
            self.href = attrs_dict.get("href")
        elif tag == "ul" or tag == "ol":
            self.list_depth += 1
        elif tag == "pre":
            self._flush_text()
            self.in_pre = True
            self.current_tag = "pre"
            self.current_text = []
        elif tag == "code" and not self.in_pre:
            self.current_text.append("`")
        elif tag == "img":
            src = attrs_dict.get("src")
            alt = attrs_dict.get("alt", "")
            if src:
                self._flush_text()
                self._add_line(f"![{alt}]({urljoin(BASE_URL, src)})")

    def handle_endtag(self, tag: str) -> None:
        if not self.in_main:
            return
        if self.skip_depth:
            self.skip_depth -= 1
            return

        if tag == "code" and not self.in_pre:
            self.current_text.append("`")
        elif tag == "a":
            self.href = None
        elif tag in {"h1", "h2", "h3", "h4", "p", "li", "pre"}:
            self._flush_text()
            if tag == "pre":
                self.in_pre = False
        elif tag == "ul" or tag == "ol":
            self.list_depth = max(0, self.list_depth - 1)

        if tag == "main":
            self.in_main = False

    def handle_data(self, data: str) -> None:
        if not self.in_main or self.skip_depth:
            return
        if self.current_tag:
            self.current_text.append(data)

    def _flush_text(self) -> None:
        if not self.current_tag:
            return
        text = self._normalize_text("".join(self.current_text), preserve=self.in_pre)
        tag = self.current_tag
        self.current_tag = None
        self.current_text = []
        if not text:
            return

        if tag == "h1":
            if self._seen_title:
                self._add_line(f"# {text}")
            else:
                self.page.title = text
                self.page.headings.append(text)
                self._seen_title = True
        elif tag in {"h2", "h3", "h4"}:
            level = {"h2": "##", "h3": "###", "h4": "####"}[tag]
            self.page.headings.append(text)
            self._add_line(f"{level} {text}")
        elif tag == "li":
            indent = "  " * max(0, self.list_depth - 1)
            self._add_line(f"{indent}- {text}")
        elif tag == "pre":
            self._add_line("```")
            self.page.lines.extend(text.rstrip("\n").splitlines())
            self._add_line("```")
        else:
            self._add_line(text)

    def _add_line(self, line: str) -> None:
        if self.page.lines and self.page.lines[-1] != "":
            self.page.lines.append("")
        self.page.lines.append(line)

    @staticmethod
    def _normalize_text(text: str, preserve: bool = False) -> str:
        if preserve:
            return text.strip("\n")
        text = html.unescape(text)
        text = text.replace("\xa0", " ")
        text = re.sub(r"\s+", " ", text)
        return text.strip()


def fetch_text(session: requests.Session, url: str) -> str:
    response = session.get(url, timeout=30)
    response.raise_for_status()
    response.encoding = "utf-8"
    return response.text


def allowed_by_robots(urls: Iterable[str]) -> None:
    parser = RobotFileParser()
    parser.set_url(ROBOTS_URL)
    parser.read()
    blocked = [url for url in urls if not parser.can_fetch(USER_AGENT, url)]
    if blocked:
        raise RuntimeError(f"robots.txt disallows {len(blocked)} target(s), first: {blocked[0]}")


def load_ai_urls(session: requests.Session, sections: set[str] | None = None) -> list[str]:
    xml_text = fetch_text(session, SITEMAP_URL)
    root = ElementTree.fromstring(xml_text)
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls: list[str] = []
    for node in root.findall("sm:url/sm:loc", namespace):
        url = (node.text or "").strip()
        section = infer_topic(url)
        if not section:
            continue
        if sections and section not in sections:
            continue
        urls.append(url)
    return sorted(set(urls), key=url_sort_key)


def infer_topic(url: str) -> str | None:
    path = urlparse(url).path.strip("/")
    parts = path.split("/")
    if len(parts) < 2 or parts[0] != "ai":
        return None
    section = parts[1]
    if section in VALID_SECTIONS and path.endswith(".html"):
        return section
    return None


def url_sort_key(url: str) -> tuple[str, int, str]:
    path = urlparse(url).path
    section = infer_topic(url) or ""
    filename = Path(path).stem
    match = re.match(r"(\d+)", filename)
    number = int(match.group(1)) if match else 9999
    return section, number, filename


def parse_page(html_text: str) -> MarkdownPage:
    parser = MainContentParser()
    parser.feed(html_text)
    parser.close()
    if not parser.page.title:
        title_match = re.search(r"<title>(.*?)</title>", html_text, re.S)
        if title_match:
            parser.page.title = clean_title(html.unescape(title_match.group(1)))
            parser.page.headings.insert(0, parser.page.title)
    return parser.page


def clean_title(title: str) -> str:
    return re.sub(r"\s*\|\s*小林面试笔记\s*$", "", title).strip()


def markdown_with_frontmatter(page: MarkdownPage, url: str, topic: str, content_hash: str) -> str:
    updated_at = now_iso()
    body = page.markdown
    if body.startswith("# "):
        body = "\n".join(body.splitlines()[1:]).strip() + "\n"
    return (
        "---\n"
        "type: source_note\n"
        "source_type: xiaolinnote\n"
        f"topic: {topic}\n"
        "status: raw\n"
        f"source_url: {url}\n"
        f"title: {json.dumps(page.title, ensure_ascii=False)}\n"
        f"content_hash: {content_hash}\n"
        f"updated: {updated_at}\n"
        "tags:\n"
        "  - xiaolinnote\n"
        f"  - {topic}\n"
        "  - interview\n"
        "---\n\n"
        f"# {page.title}\n\n"
        f"> 来源：{url}\n\n"
        f"{body}"
    )


def extract_sections(markdown: str) -> dict[str, str]:
    lines = markdown.splitlines()
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in lines:
        heading = re.match(r"^#{2,4}\s+(.+?)\s*$", line)
        if heading:
            name = strip_emoji(heading.group(1))
            current = classify_heading(name)
            if current:
                sections.setdefault(current, [])
            continue
        if current is not None:
            sections[current].append(line)
    return {key: "\n".join(value).strip() for key, value in sections.items()}


def classify_heading(name: str) -> str | None:
    normalized = re.sub(r"\s+", "", name)
    if "简要回答" in normalized:
        return "answer_summary"
    if "详细解析" in normalized:
        return "answer_outline"
    if "面试总结" in normalized:
        return "interview_summary"
    return None


def strip_emoji(text: str) -> str:
    return re.sub(r"^[^\w\u4e00-\u9fff]+", "", text).strip()


def fallback_summary(markdown: str) -> str:
    paragraphs = []
    for block in re.split(r"\n\s*\n", markdown):
        block = block.strip()
        if not block or block.startswith("#") or block.startswith(">") or block.startswith("!"):
            continue
        if block.startswith("- "):
            continue
        paragraphs.append(block)
        if len(paragraphs) >= 3:
            break
    return "\n\n".join(paragraphs)


def build_record(page: MarkdownPage, markdown: str, url: str, topic: str, content_hash: str, source_path: Path) -> dict:
    sections = extract_sections(markdown)
    answer_summary = sections.get("answer_summary") or fallback_summary(markdown)
    answer_outline = sections.get("answer_outline") or "\n".join(
        heading for heading in page.headings[1:] if heading
    )
    interview_summary = sections.get("interview_summary") or ""
    return {
        "id": make_id(url),
        "topic": topic,
        "source_url": url,
        "title": page.title,
        "question": page.title,
        "answer_summary": answer_summary,
        "answer_outline": split_outline(answer_outline),
        "interview_summary": interview_summary,
        "headings": page.headings,
        "source_markdown": str(source_path.relative_to(ROOT)).replace("\\", "/"),
        "content_hash": content_hash,
        "updated_at": now_iso(),
    }


def split_outline(text: str) -> list[str]:
    items: list[str] = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        line = re.sub(r"^[-*]\s+", "", line)
        items.append(line)
    return items


def make_id(url: str) -> str:
    path = urlparse(url).path.strip("/")
    path = re.sub(r"\.html$", "", path)
    path = path.replace("/", "-")
    return f"xiaolinnote-{path}"


def source_path_for(url: str) -> Path:
    parsed = urlparse(url)
    parts = parsed.path.strip("/").split("/")
    section = parts[1]
    name = parts[-1]
    if name == "index.html":
        name = "_index.html"
    return SOURCE_ROOT / section / f"{Path(name).stem}.md"


def content_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load_manifest() -> dict:
    if not MANIFEST_PATH.exists():
        return {"source": SITEMAP_URL, "pages": {}}
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def write_manifest(manifest: dict) -> None:
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    manifest["updated_at"] = now_iso()
    MANIFEST_PATH.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def load_existing_records() -> dict[str, dict]:
    records: dict[str, dict] = {}
    if not DATASET_PATH.exists():
        return records
    with DATASET_PATH.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            record = json.loads(line)
            records[record["source_url"]] = record
    return records


def write_records(records: dict[str, dict]) -> None:
    DATASET_PATH.parent.mkdir(parents=True, exist_ok=True)
    ordered = sorted(records.values(), key=lambda item: url_sort_key(item["source_url"]))
    with DATASET_PATH.open("w", encoding="utf-8", newline="\n") as handle:
        for record in ordered:
            handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")


def should_skip(url: str, digest: str, manifest: dict, force: bool) -> bool:
    if force:
        return False
    page = manifest.get("pages", {}).get(url)
    return bool(page and page.get("content_hash") == digest)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch xiaolinnote.com AI interview pages.")
    parser.add_argument(
        "--sections",
        nargs="+",
        choices=sorted(VALID_SECTIONS),
        help="Only fetch selected sections, e.g. --sections agent rag",
    )
    parser.add_argument("--limit", type=int, help="Limit number of URLs after filtering.")
    parser.add_argument("--force", action="store_true", help="Refetch and rewrite changed data even if hashes match.")
    parser.add_argument("--dry-run", action="store_true", help="List target URLs without writing files.")
    parser.add_argument("--delay", type=float, default=0.5, help="Delay between page requests in seconds.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})
    sections = set(args.sections) if args.sections else None

    urls = load_ai_urls(session, sections)
    if args.limit is not None:
        urls = urls[: args.limit]
    allowed_by_robots(urls)

    print(f"Found {len(urls)} target page(s).")
    if args.dry_run:
        for url in urls:
            print(url)
        return 0

    manifest = load_manifest()
    records = load_existing_records()
    stats = {"created": 0, "updated": 0, "unchanged": 0, "failed": 0}

    for index, url in enumerate(urls, start=1):
        topic = infer_topic(url)
        if not topic:
            continue
        try:
            html_text = fetch_text(session, url)
            page = parse_page(html_text)
            if not page.title:
                raise ValueError("missing page title")
            digest = content_hash(page.markdown)
            target_path = source_path_for(url)
            existed = target_path.exists() or url in records
            if should_skip(url, digest, manifest, args.force):
                stats["unchanged"] += 1
                print(f"[{index}/{len(urls)}] unchanged {url}")
            else:
                target_path.parent.mkdir(parents=True, exist_ok=True)
                source_md = markdown_with_frontmatter(page, url, topic, digest)
                target_path.write_text(source_md, encoding="utf-8", newline="\n")
                records[url] = build_record(page, source_md, url, topic, digest, target_path)
                manifest.setdefault("pages", {})[url] = {
                    "topic": topic,
                    "source_markdown": str(target_path.relative_to(ROOT)).replace("\\", "/"),
                    "content_hash": digest,
                    "updated_at": now_iso(),
                }
                key = "updated" if existed else "created"
                stats[key] += 1
                print(f"[{index}/{len(urls)}] {key} {url}")
        except Exception as exc:  # noqa: BLE001 - CLI should continue through bad pages.
            stats["failed"] += 1
            print(f"[{index}/{len(urls)}] failed {url}: {exc}", file=sys.stderr)
        if index < len(urls) and args.delay > 0:
            time.sleep(args.delay)

    write_records(records)
    write_manifest(manifest)
    print(
        "Done: "
        f"created={stats['created']} updated={stats['updated']} "
        f"unchanged={stats['unchanged']} failed={stats['failed']}"
    )
    return 1 if stats["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
