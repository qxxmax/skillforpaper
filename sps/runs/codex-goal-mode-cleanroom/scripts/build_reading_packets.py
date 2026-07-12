#!/usr/bin/env python3
"""Extract current PDFs and build page-anchored reading packets."""

from __future__ import annotations

import csv
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT_DIR = ROOT / "sources/text"
PACKET_DIR = ROOT / "sources/packets"
TEXT_DIR.mkdir(exist_ok=True); PACKET_DIR.mkdir(exist_ok=True)

PATTERNS = {
    "problem": ["challenge", "difficult", "inefficient", "critical slowing", "topological freezing", "intractable", "problem", "bottleneck", "suffer"],
    "method": ["we propose", "we introduce", "our method", "algorithm", "framework", "sampler", "correction", "metropolis", "architecture"],
    "result": ["we show", "we demonstrate", "we find", "results show", "outperform", "agrees", "improve", "achieve", "reproduce"],
    "limitation": ["limitation", "future work", "remain", "however", "does not", "not yet", "restricted", "only", "further work", "open question"],
}


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def sentences(page: str) -> list[str]:
    page = re.sub(r"(?<=[A-Za-z])-\s+(?=[A-Za-z])", "", page)
    return [clean(item) for item in re.split(r"(?<=[.!?])\s+", clean(page)) if 45 <= len(clean(item)) <= 800]


def choose(pages: list[str], dimension: str) -> tuple[int, str, int]:
    candidates = []
    for page_no, page in enumerate(pages, 1):
        for sentence in sentences(page):
            lower = sentence.lower()
            score = sum(3 if " " in pattern else 1 for pattern in PATTERNS[dimension] if pattern in lower)
            if dimension == "problem" and page_no <= 4: score += 2
            if dimension == "method" and page_no <= max(8, len(pages)//2): score += 1
            if dimension in {"result", "limitation"} and page_no >= max(2, len(pages)//2): score += 2
            if score:
                candidates.append((score, -len(sentence), page_no, sentence))
    if not candidates:
        return 0, "not automatically located; manual reading required", 0
    score, _, page_no, sentence = max(candidates)
    return page_no, sentence, score


def main() -> None:
    status = {row["arxiv_id"]: row for row in csv.DictReader((ROOT / "fulltext_download_status.csv").open(encoding="utf-8")) if row["status"] == "verified_pdf"}
    selected = list(csv.DictReader((ROOT / "selected_fulltexts.csv").open(encoding="utf-8")))
    rows = []
    combined = ["# Current-Run Reading Packets", ""]
    for item in selected:
        arxiv_id = item["arxiv_id"]
        if arxiv_id not in status:
            continue
        pdf = ROOT / status[arxiv_id]["pdf_path"]
        text_path = TEXT_DIR / f"{arxiv_id}.txt"
        subprocess.run(["pdftotext", "-layout", str(pdf), str(text_path)], check=True)
        pages = text_path.read_text(encoding="utf-8", errors="replace").split("\f")
        record = {
            "paper_id": f"P_{arxiv_id.replace('.', '_')}", "arxiv_id": arxiv_id,
            "title": item["title"], "authors": item["authors"], "year": item["year"],
            "selection_reason": item["selection_reason"], "facets": item["facets"],
            "pdf_path": status[arxiv_id]["pdf_path"], "pages": status[arxiv_id]["pages"],
        }
        for dimension in PATTERNS:
            page_no, excerpt, score = choose(pages, dimension)
            record[f"{dimension}_page_candidate"] = page_no
            record[f"{dimension}_excerpt_candidate"] = excerpt
            record[f"{dimension}_locator_score"] = score
        rows.append(record)
        packet = [f"# {item['title']}", "", f"- arXiv: {arxiv_id}", f"- selected by: {item['selection_reason']}", f"- PDF pages: {status[arxiv_id]['pages']}", ""]
        for dimension in PATTERNS:
            packet.extend([f"## {dimension.title()} candidate", "", f"PDF p.{record[f'{dimension}_page_candidate']}: {record[f'{dimension}_excerpt_candidate']}", ""])
        content = "\n".join(packet)
        (PACKET_DIR / f"{arxiv_id}.md").write_text(content + "\n", encoding="utf-8")
        combined.extend(packet + ["---", ""])
    with (ROOT / "reading_packet_index.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0])); writer.writeheader(); writer.writerows(rows)
    (ROOT / "reading_packets.md").write_text("\n".join(combined), encoding="utf-8")
    print(f"packets={len(rows)} pages={sum(int(row['pages']) for row in rows)}")


if __name__ == "__main__":
    main()
