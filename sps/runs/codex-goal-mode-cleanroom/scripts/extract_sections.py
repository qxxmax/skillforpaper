#!/usr/bin/env python3
"""Extract longer abstract/method/result/conclusion sections for manual review."""

from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "sources/packets/sections"
OUT.mkdir(parents=True, exist_ok=True)

HEADINGS = {
    "method": [r"method(?:s|ology)?", r"algorithm", r"framework", r"approach", r"model"],
    "result": [r"results?", r"experiments?", r"numerical", r"evaluation"],
    "conclusion": [r"conclusions?", r"summary(?: and outlook)?", r"discussion(?: and outlook)?", r"limitations?", r"outlook"],
}


def clean(text: str) -> str:
    text = re.sub(r"(?<=[A-Za-z])-\s+(?=[A-Za-z])", "", text)
    return re.sub(r"\s+", " ", text).strip()


def page_for_offset(pages: list[str], offset: int) -> int:
    count = 0
    for page_no, page in enumerate(pages, 1):
        count += len(page) + 1
        if offset < count:
            return page_no
    return len(pages)


def section(full: str, pages: list[str], patterns: list[str], last: bool = False) -> tuple[int, str]:
    heading = r"(?im)^\s*(?:\d+(?:\.\d+)*\s+)?(?:" + "|".join(patterns) + r")\b[^\n]{0,100}$"
    matches = list(re.finditer(heading, full))
    if not matches:
        return 0, "section heading not located"
    match = matches[-1] if last else matches[0]
    start = match.start()
    excerpt = clean(full[start:start + 3500])
    return page_for_offset(pages, start), excerpt


def abstract(full: str, pages: list[str]) -> tuple[int, str]:
    match = re.search(r"(?is)\babstract\b\s*[:.-]?\s*(.{200,4000}?)(?=\n\s*(?:1\s+)?introduction\b)", full)
    if match:
        return page_for_offset(pages, match.start(1)), clean(match.group(1))[:3000]
    return 1, clean(" ".join(pages[:2]))[:3000]


def main() -> None:
    selected = list(csv.DictReader((ROOT / "selected_fulltexts.csv").open(encoding="utf-8")))
    rows = []
    combined = ["# Section Extracts For Manual Review", ""]
    for item in selected:
        arxiv_id = item["arxiv_id"]
        text_path = ROOT / "sources/text" / f"{arxiv_id}.txt"
        pages = text_path.read_text(encoding="utf-8", errors="replace").split("\f")
        full = "\f".join(pages)
        a_page, a_text = abstract(full, pages)
        m_page, m_text = section(full, pages, HEADINGS["method"])
        r_page, r_text = section(full, pages, HEADINGS["result"])
        c_page, c_text = section(full, pages, HEADINGS["conclusion"], last=True)
        row = {
            "arxiv_id": arxiv_id, "title": item["title"],
            "abstract_page": a_page, "abstract_extract": a_text,
            "method_page": m_page, "method_extract": m_text,
            "result_page": r_page, "result_extract": r_text,
            "conclusion_page": c_page, "conclusion_extract": c_text,
        }
        rows.append(row)
        packet = [
            f"# {item['title']}", "", f"- arXiv: {arxiv_id}", "",
            f"## Abstract (PDF p.{a_page})", "", a_text, "",
            f"## Method-section extract (PDF p.{m_page})", "", m_text, "",
            f"## Result-section extract (PDF p.{r_page})", "", r_text, "",
            f"## Conclusion/limitation extract (PDF p.{c_page})", "", c_text, "",
        ]
        text = "\n".join(packet)
        (OUT / f"{arxiv_id}.md").write_text(text + "\n", encoding="utf-8")
        combined.extend(packet + ["---", ""])
    with (ROOT / "section_extract_index.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0])); writer.writeheader(); writer.writerows(rows)
    (ROOT / "section_extracts.md").write_text("\n".join(combined), encoding="utf-8")
    print(f"section_packets={len(rows)}")


if __name__ == "__main__":
    main()
