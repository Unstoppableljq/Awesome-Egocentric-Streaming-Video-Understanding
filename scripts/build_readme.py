#!/usr/bin/env python3
"""Validate the curated registry and render README paper sections. Stdlib only."""

import argparse
import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "papers.json"
README = ROOT / "README.md"
START = "<!-- PAPERS:START -->"
END = "<!-- PAPERS:END -->"
LAST_PASS = "2026-10-27"
TOPICS = [
    "Online Perception & Understanding",
    "Continuous Memory & Long-Horizon Reasoning",
    "Personalized & User-Centric Understanding",
    "Streaming Audio-Visual Understanding",
    "Proactive Assistance & Situated Interaction",
    "Anticipation, Planning & Embodied Reasoning",
]
BLURBS = {
    "Online Perception & Understanding": "What is unfolding now, using only the observation available at this moment?",
    "Continuous Memory & Long-Horizon Reasoning": "What happened, what changed, and which past state is still valid?",
    "Personalized & User-Centric Understanding": "What should be remembered because it matters to this wearer, not to a generic user?",
    "Streaming Audio-Visual Understanding": "Which observed entity or event does an utterance refer to?",
    "Proactive Assistance & Situated Interaction": "Should the assistant stay silent, answer, or intervene now?",
    "Anticipation, Planning & Embodied Reasoning": "What happens next, and which action or correction is appropriate?",
}
TIERS = {"Core", "Related"}
REQUIRED = {
    "id", "title", "year", "date", "short_name", "tier", "primary_topic", "kind",
    "viewpoint", "protocol", "interaction", "memory_horizon", "audio_role", "venue",
    "paper_url", "code_url", "project_url", "dataset_url", "why_it_matters",
    "verification_note",
}
DATE_RE = re.compile(r"\d{4}/\d{2}")


def verify_url(url, where, optional=False):
    if optional and not url:
        return
    parts = urlparse(url)
    if parts.scheme not in {"https", "http"} or not parts.netloc:
        raise ValueError(f"Invalid URL for {where}: {url!r}")


def validate(items):
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
        if not DATE_RE.fullmatch(item["date"]):
            raise ValueError(f"date must be YYYY/MM: {item['id']}")
        year_text, month_text = item["date"].split("/")
        if int(year_text) != item["year"] or not 1 <= int(month_text) <= 12:
            raise ValueError(f"date does not match year: {item['id']}")
        if item["tier"] not in TIERS:
            raise ValueError(f"Invalid tier: {item['id']}")
        if item["primary_topic"] not in TOPICS:
            raise ValueError(f"Invalid topic: {item['id']}")
        for field in ("title", "short_name", "venue", "why_it_matters"):
            if not str(item[field]).strip():
                raise ValueError(f"{field} must be nonempty: {item['id']}")
        verify_url(item["paper_url"], f"{item['id']}.paper_url")
        for field in ("code_url", "project_url", "dataset_url"):
            verify_url(item[field], f"{item['id']}.{field}", optional=True)
        if item["paper_url"] in papers:
            raise ValueError(f"Duplicate paper URL: {item['paper_url']}")
        papers.add(item["paper_url"])


def cell(text):
    """Make a simple inline Markdown table cell safe."""
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def resources(item):
    grouped = []
    index = {}
    for label, key in (("Code", "code_url"), ("Project", "project_url"), ("Data", "dataset_url")):
        url = item.get(key) or ""
        if not url or url == item["paper_url"]:
            continue
        if url in index:
            grouped[index[url]][1].append(label)
            continue
        index[url] = len(grouped)
        grouped.append([url, [label]])
    if not grouped:
        return "—"
    return " · ".join(f"[{' / '.join(labels)}]({url})" for url, labels in grouped)


def paper_rows(matches):
    lines = [
        "| Paper | Work | Date | Venue | Streaming evidence | Method / Key Contribution | Resources |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
    ]
    ordered = sorted(matches, key=lambda x: x["title"].casefold())
    ordered.sort(key=lambda x: x["date"], reverse=True)
    for item in ordered:
        lines.append("| " + " | ".join((
            f"[{cell(item['title'])}]({item['paper_url']})",
            cell(item["short_name"]),
            cell(item["date"]),
            cell(item["venue"]),
            cell(item["protocol"]),
            cell(item["why_it_matters"]),
            resources(item),
        )) + " |")
    return lines


def render(items):
    core = sum(i["tier"] == "Core" for i in items)
    related = sum(i["tier"] == "Related" for i in items)
    lines = [
        f"_Curated entries: **{len(items)}** · Core: **{core}** · Related: **{related}**. Literature pass: **{LAST_PASS}**. Streaming labels follow author-described evidence and are not an independent latency audit. A missing code, project, or data link means **not recorded**._",
        "",
        "Interaction type, memory horizon, and audio role stay in [`data/papers.json`](data/papers.json) so this table can stay readable.",
        "",
    ]
    for tier in ("Core", "Related"):
        lines.extend([f"### {tier} papers", ""])
        if tier == "Core":
            lines.extend([
                "First-person visual input, an author-described online or causal protocol, and an understanding, memory, reasoning, or interaction task.",
                "",
            ])
        else:
            lines.extend([
                "These papers inform the research agenda, but first-person capture and a causal streaming protocol are not both established.",
                "",
            ])
        tier_items = [i for i in items if i["tier"] == tier]
        if not tier_items and tier == "Related":
            lines.extend(["_None yet._", ""])
            continue
        for topic in TOPICS:
            matches = [i for i in tier_items if i["primary_topic"] == topic]
            if not matches and tier == "Related":
                continue
            lines.extend([
                f"#### {topic}",
                "",
                f"*{BLURBS[topic]}*",
                "",
            ])
            if not matches:
                lines.extend(["_No curated core entry yet._", ""])
                continue
            lines.extend(paper_rows(matches))
            lines.extend(["", ""])
    lines.extend([
        "### Release index",
        "",
        "Same entries, newest submission month first. Question is the single primary category, not an exhaustive tag set.",
        "",
        "| Date | Paper | Work | Tier | Question | Venue |",
        "| :--- | :--- | :--- | :--- | :--- | :--- |",
    ])
    ordered = sorted(items, key=lambda x: x["title"].casefold())
    ordered.sort(key=lambda x: x["date"], reverse=True)
    for item in ordered:
        lines.append("| " + " | ".join((
            cell(item["date"]),
            f"[{cell(item['title'])}]({item['paper_url']})",
            cell(item["short_name"]),
            cell(item["tier"]),
            cell(item["primary_topic"]),
            cell(item["venue"]),
        )) + " |")
    lines.append("")
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
