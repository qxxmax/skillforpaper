#!/usr/bin/env python3
"""Build page-aware full-text reading packets and a PDF inventory."""

from __future__ import annotations

import csv
import hashlib
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PDF_DIR = ROOT / "sources/pdfs"
TEXT_DIR = ROOT / "sources/text"

PATTERNS = {
    "problem": [r"\bintroduction\b", r"\bmotivation\b", r"critical slowing", r"sampling from"],
    "mechanism_or_correction": [r"\bmethod(?:s|ology)?\b", r"\balgorithm\b", r"metropolis", r"importance weight", r"training objective", r"stochastic differential"],
    "result": [r"\bresults?\b", r"\bexperiments?\b", r"numerical results", r"we (?:find|show|demonstrate)"],
    "limitation": [r"\blimitations?\b", r"\bdiscussion\b", r"\bconclusions?\b", r"future work", r"remain(?:s|ing)", r"outside the scope"],
}


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def find_anchor(pages: list[str], patterns: list[str]) -> tuple[int, str, str]:
    for page_no, page in enumerate(pages, 1):
        for pattern in patterns:
            match = re.search(pattern, page, re.I)
            if match:
                start = max(0, match.start() - 180)
                end = min(len(page), match.end() + 620)
                return page_no, match.group(0), normalize(page[start:end])
    return 0, "not found", "No automatic anchor; manual abstract/conclusion review required."


def pdf_pages(path: Path) -> int:
    info = subprocess.check_output(["pdfinfo", str(path)], text=True, errors="replace")
    match = re.search(r"^Pages:\s+(\d+)", info, re.M)
    if not match:
        raise RuntimeError(f"Pages missing from pdfinfo: {path}")
    return int(match.group(1))


def main() -> None:
    inventory = []
    packet_lines = ["# Full-Text Reading Packets", "", "Generated from fresh local PDFs; page numbers are PDF pages.", ""]
    for pdf in sorted(PDF_DIR.glob("*.pdf")):
        paper_id = pdf.stem
        text_path = TEXT_DIR / f"{paper_id}.txt"
        pages = text_path.read_text(encoding="utf-8", errors="replace").split("\f")
        if pages and not pages[-1].strip():
            pages.pop()
        page_count = pdf_pages(pdf)
        digest = hashlib.sha256(pdf.read_bytes()).hexdigest()
        inventory.append({
            "PaperID": paper_id,
            "PDFPath": str(pdf.relative_to(ROOT)),
            "TextPath": str(text_path.relative_to(ROOT)),
            "Pages": page_count,
            "Bytes": pdf.stat().st_size,
            "SHA256": digest,
            "PDFInfoStatus": "readable",
            "ReadingStatus": "four_dimension_packet_built",
        })
        title = normalize(" ".join(pages[0].splitlines()[:12]))[:240]
        packet_lines.extend([f"## {paper_id}", "", f"Title block: {title}", f"Pages: {page_count}", ""])
        for dimension, patterns in PATTERNS.items():
            page_no, anchor, snippet = find_anchor(pages, patterns)
            packet_lines.extend([f"### {dimension}", f"PDF page {page_no}; anchor: `{anchor}`", "", snippet, ""])
    with (ROOT / "pdf_inventory.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(inventory[0]))
        writer.writeheader()
        writer.writerows(inventory)
    (ROOT / "fulltext_reading_packets.md").write_text("\n".join(packet_lines), encoding="utf-8")


if __name__ == "__main__":
    main()
