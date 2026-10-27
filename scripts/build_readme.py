#!/usr/bin/env python3
"""Validate the curated registry and render README paper sections. Stdlib only."""

import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "papers.json"
README = ROOT / "README.md"
START = "<!-- PAPERS:START -->"
END = "<!-- PAPERS:END -->"
TOPICS = [
    "Online Perception & Understanding",
    "Continuous Memory & Long-Horizon Reasoning",
    "Personalized & User-Centric Understanding",
    "Streaming Audio-Visual Understanding",
    "Proactive Assistance & Situated Interaction",
    "Anticipation, Planning & Embodied Reasoning",
]
TIERS = {"Core", "Related"}
REQUIRED = {
    "id", "title", "year", "tier", "primary_topic", "kind", "viewpoint",
    "protocol", "interaction", "memory_horizon", "audio_role", "paper_url",
    "code_url", "project_url", "why_it_matters", "verification_note",
}


def verify_url(url: str, where: str, optional: bool = False) -> None:
    if optional and not url:
        return
    parts = urlparse(url)
    if parts.scheme not in {"https", "http"} or not parts.netloc:
        raise ValueError(f"Invalid URL for {where}: {url!r}")


def validate(items: list[dict]) -> None:
    if not isinstance(items, list):
        raise ValueError("papers.json must contain a JSON list")
    ids = set()
    papers = set()
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            raise ValueError(f"Entry {index} must be an object")
        missing = REQUIRED - set(item)
        if missing:
            raise ValueError(f"Entry {index} missing keys: {sorted(missing)}")
        if item["id"] in ids:
            raise ValueError(f"Duplicate id: {item['id']}")
        ids.add(item["id"])
        if not isinstance(item["year"], int) or not 1900 <= item["year"] <= 2100:
            raise ValueError(f"Invalid year: {item['id']}")
        if item["tier"] not in TIERS:
            raise ValueError(f"Invalid tier: {item['id']}")
        if item["primary_topic"] not in TOPICS:
            raise ValueError(f"Invalid topic: {item['id']}")
        if not item["title"].strip() or not item["why_it_matters"].strip():
            raise ValueError(f"Title / research motivation must be nonempty: {item['id']}")
        verify_url(item["paper_url"], f"{item['id']}.paper_url")
        for field in ("code_url", "project_url"):
            verify_url(item[field], f"{item['id']}.{field}", optional=True)
        if item["paper_url"] in papers:
            raise ValueError(f"Duplicate paper URL: {item['paper_url']}")
        papers.add(item["paper_url"])


def cell(text: str) -> str:
    """Make a simple inline Markdown table cell safe."""
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def render(items: list[dict]) -> str:
    lines = [
        f"_Seed entries: **{len(items)}** · Core: **{sum(i['tier'] == 'Core' for i in items)}** · Related: **{sum(i['tier'] == 'Related' for i in items)}**. Missing links mean **not recorded**, not necessarily unavailable._",
        "",
    ]
    for tier in ("Core", "Related"):
        lines.extend([f"### {tier} papers", ""])
        if tier == "Related":
            lines.extend(["These papers inform the research agenda but have not yet been confirmed to meet the strict core scope.", ""])
        for topic in TOPICS:
            matches = [i for i in items if i["tier"] == tier and i["primary_topic"] == topic]
            if not matches:
                continue
            lines.extend([
                f"#### {topic}",
                "",
                "| Paper | Type | Streaming evidence | Research motivation | Resources |",
                "| --- | --- | --- | --- | --- |",
            ])
            for item in sorted(matches, key=lambda x: (-x["year"], x["title"].casefold())):
                paper = f"[{cell(item['title'])}]({item['paper_url']}) ({item['year']})"
                links = [f"[Paper]({item['paper_url']})"]
                if item["code_url"]:
                    links.append(f"[Code]({item['code_url']})")
                if item["project_url"]:
                    links.append(f"[Project]({item['project_url']})")
                lines.append("| " + " | ".join((
                    paper,
                    cell(item["kind"]),
                    cell(item["protocol"]),
                    cell(item["why_it_matters"]),
                    " · ".join(links)
                )) + " |")
            lines.extend(["", ""])
        if not any(i["tier"] == tier for i in items):
            lines.extend(["_None yet._", ""])
    return "\n".join(lines).rstrip() + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if README needs regeneration")
    args = parser.parse_args()
    items = json.loads(REGISTRY.read_text(encoding="utf-8"))
    validate(items)
    body = README.read_text(encoding="utf-8")
    if body.count(START) != 1 or body.count(END) != 1:
        raise ValueError("README must contain exactly one pair of paper markers")
    before, after_start = body.split(START, 1)
    _, after = after_start.split(END, 1)
    new_body = before + START + "\n" + render(items) + "\n" + END + after
    if args.check:
        if new_body != body:
            raise SystemExit("README is out of date. Run: python scripts/build_readme.py")
        print(f"PASS: {len(items)} curated entries, README synchronized")
    else:
        README.write_text(new_body, encoding="utf-8")
        print(f"Updated README with {len(items)} curated entries")


if __name__ == "__main__":
    main()
