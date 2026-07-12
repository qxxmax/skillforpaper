#!/usr/bin/env python3
"""Reconstruct the live SPS bibliography in first-citation order."""

from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / "sources/root_source/main_1b.tex"
BIB = ROOT / "sources/root_source/reference_1b.bib"
OUT = ROOT / "root_bibliography_screening.csv"


def strip_comments(text: str) -> str:
    lines = []
    for line in text.splitlines():
        match = re.search(r"(?<!\\)%", line)
        lines.append(line[: match.start()] if match else line)
    return "\n".join(lines)


def split_entries(text: str) -> dict[str, str]:
    entries: dict[str, str] = {}
    pos = 0
    while True:
        match = re.search(r"@(\w+)\s*\{\s*([^,]+),", text[pos:], re.I)
        if not match:
            break
        start = pos + match.start()
        body_start = pos + match.end()
        depth = 1
        i = body_start
        while i < len(text) and depth:
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
            i += 1
        entries[match.group(2).strip()] = text[start:i]
        pos = i
    return entries


def field(entry: str, name: str) -> str:
    match = re.search(rf"\b{name}\s*=\s*", entry, re.I)
    if not match:
        return ""
    i = match.end()
    if i >= len(entry):
        return ""
    if entry[i] == "{":
        depth = 1
        j = i + 1
        while j < len(entry) and depth:
            if entry[j] == "{":
                depth += 1
            elif entry[j] == "}":
                depth -= 1
            j += 1
        value = entry[i + 1 : j - 1]
    elif entry[i] == '"':
        j = i + 1
        while j < len(entry) and (entry[j] != '"' or entry[j - 1] == "\\"):
            j += 1
        value = entry[i + 1 : j]
    else:
        j = entry.find(",", i)
        value = entry[i : j if j >= 0 else len(entry)]
    value = re.sub(r"\s+", " ", value).strip()
    return value.replace("{", "").replace("}", "")


def arxiv_id(entry: str) -> str:
    candidates = [field(entry, "eprint"), field(entry, "url")]
    for value in candidates:
        match = re.search(r"(?:arXiv[.:/]?\s*)?(\d{4}\.\d{4,5})(?:v\d+)?", value, re.I)
        if match:
            return match.group(1)
    return ""


def live_citations(tex: str) -> tuple[list[str], dict[str, tuple[int, str]]]:
    order: list[str] = []
    contexts: dict[str, tuple[int, str]] = {}
    seen: set[str] = set()
    lines = tex.splitlines()
    for line_no, line in enumerate(lines, 1):
        for citation in re.finditer(r"\\cite\s*\{([^}]*)\}", line):
            context = re.sub(r"\s+", " ", line).strip()
            for key in re.split(r"\s*,\s*", citation.group(1)):
                if key and key not in seen:
                    seen.add(key)
                    order.append(key)
                    contexts[key] = (line_no, context)
    return order, contexts


def screening(title: str, context: str) -> tuple[str, str, str]:
    combined = f"{title} {context}".lower()
    if "applications range from materials science" in context.lower():
        return "include_context", "cross_domain_entropy_context", "Individually screened cross-domain Clausius/entropy-production context; not a direct sampler or LFT mechanism."
    if any(term in combined for term in ["lattice", "sampl", "diffusion", "flow", "langevin", "monte carlo", "gflownet", "stochastic quant"]):
        facet = "core_sampler_or_lft"
        return "include", facet, "Direct method, lattice-field, stochastic-process, or sampler relevance."
    if any(term in combined for term in ["entropy", "clausius", "thermodynamic", "information", "irreversib", "jarzynski"]):
        facet = "thermodynamic_foundation"
        return "include_context", facet, "Foundational path-entropy, nonequilibrium, or information-theoretic context."
    return "exclude_context", "distant_application", "Cited as a distant application of entropy production; no direct SPS or LFT mechanism."


def main() -> None:
    tex = strip_comments(TEX.read_text(encoding="utf-8"))
    entries = split_entries(BIB.read_text(encoding="utf-8"))
    order, contexts = live_citations(tex)
    if len(order) != 58:
        raise SystemExit(f"Expected 58 live references, found {len(order)}")
    columns = [
        "ref_no", "bibkey", "authors", "year", "title", "venue", "doi", "arxiv_id", "url",
        "citation_line", "root_context", "screening_decision", "facet", "screening_reason",
        "primary_source_status", "full_text_status", "notes",
    ]
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns)
        writer.writeheader()
        for number, key in enumerate(order, 1):
            entry = entries.get(key, "")
            if not entry:
                raise SystemExit(f"Missing BibTeX entry: {key}")
            line_no, context = contexts[key]
            title = field(entry, "title")
            decision, facet, reason = screening(title, context)
            venue = field(entry, "journal") or field(entry, "booktitle") or field(entry, "publisher")
            writer.writerow({
                "ref_no": number,
                "bibkey": key,
                "authors": field(entry, "author"),
                "year": field(entry, "year"),
                "title": title,
                "venue": venue,
                "doi": field(entry, "doi"),
                "arxiv_id": arxiv_id(entry),
                "url": field(entry, "url"),
                "citation_line": line_no,
                "root_context": context,
                "screening_decision": decision,
                "facet": facet,
                "screening_reason": reason,
                "primary_source_status": "metadata_from_root_bib",
                "full_text_status": "not_yet_retrieved",
                "notes": "Freshly reconstructed from live TeX citation order.",
            })


if __name__ == "__main__":
    main()
