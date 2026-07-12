#!/usr/bin/env python3
"""Derive bibliography, grounded terms, and query routes from the root source."""

from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / "sources/root/source/main_1b.tex"
BIB = ROOT / "sources/root/source/reference_1b.bib"
PDF_TEXT = ROOT / "sources/root/2606.13790.txt"


def strip_tex_comments(text: str) -> str:
    return "\n".join(re.split(r"(?<!\\)%", line, maxsplit=1)[0] for line in text.splitlines())


def bib_entries(text: str) -> dict[str, str]:
    entries: dict[str, str] = {}
    for match in re.finditer(r"@(\w+)\s*\{\s*([^,]+),", text, re.I):
        start, depth, i = match.start(), 1, match.end()
        while i < len(text) and depth:
            depth += (text[i] == "{") - (text[i] == "}")
            i += 1
        entries[match.group(2).strip()] = text[start:i]
    return entries


def field(entry: str, name: str) -> str:
    match = re.search(rf"\b{name}\s*=\s*", entry, re.I)
    if not match:
        return ""
    i = match.end()
    if entry[i] == "{":
        depth, j = 1, i + 1
        while j < len(entry) and depth:
            depth += (entry[j] == "{") - (entry[j] == "}")
            j += 1
        value = entry[i + 1:j - 1]
    elif entry[i] == '"':
        j = i + 1
        while j < len(entry) and entry[j] != '"':
            j += 1
        value = entry[i + 1:j]
    else:
        j = entry.find(",", i)
        value = entry[i:j if j >= 0 else len(entry)]
    value = re.sub(r"\\[a-zA-Z]+\s*", "", value)
    return re.sub(r"[{}\s]+", " ", value).strip()


def arxiv_id(entry: str) -> str:
    for value in (field(entry, "eprint"), field(entry, "url"), entry):
        match = re.search(r"(?<!\d)(\d{4}\.\d{4,5})(?:v\d+)?", value)
        if match:
            return match.group(1)
    return ""


def citation_order(tex: str) -> list[tuple[str, int, str]]:
    seen: set[str] = set()
    result = []
    for line_no, line in enumerate(tex.splitlines(), 1):
        for match in re.finditer(r"\\cite\s*\{([^}]+)\}", line):
            for key in re.split(r"\s*,\s*", match.group(1)):
                if key and key not in seen:
                    seen.add(key)
                    result.append((key, line_no, re.sub(r"\s+", " ", line).strip()))
    return result


def page_anchor(pages: list[str], phrase: str) -> tuple[int, str]:
    needle = re.sub(r"[^a-z0-9]+", " ", phrase.lower()).strip()
    for page_no, page in enumerate(pages, 1):
        dehyphenated = re.sub(r"(?<=[A-Za-z])-\s+(?=[A-Za-z])", "", page)
        normalized = re.sub(r"[^a-z0-9]+", " ", dehyphenated.lower())
        position = normalized.find(needle)
        if position >= 0:
            # Use the first nearby source sentence as a compact audit anchor.
            sentences = re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", dehyphenated))
            for sentence in sentences:
                if needle in re.sub(r"[^a-z0-9]+", " ", sentence.lower()):
                    return page_no, sentence[:360]
            return page_no, phrase
    raise ValueError(f"Phrase not found in root PDF text: {phrase}")


def main() -> None:
    tex = strip_tex_comments(TEX.read_text(encoding="utf-8"))
    entries = bib_entries(BIB.read_text(encoding="utf-8"))
    order = citation_order(tex)
    if not order:
        raise SystemExit("No live citations found")
    refs = []
    for number, (key, line_no, context) in enumerate(order, 1):
        entry = entries.get(key, "")
        if not entry:
            raise SystemExit(f"Missing BibTeX entry for {key}")
        refs.append({
            "ref_no": number, "bibkey": key, "authors": field(entry, "author"),
            "year": field(entry, "year"), "title": field(entry, "title"),
            "venue": field(entry, "journal") or field(entry, "booktitle"),
            "doi": field(entry, "doi"), "arxiv_id": arxiv_id(entry),
            "url": field(entry, "url"), "citation_line": line_no,
            "citation_context": context, "provenance": "current root TeX and BibTeX",
        })
    with (ROOT / "root_bibliography.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(refs[0]))
        writer.writeheader(); writer.writerows(refs)

    pages = PDF_TEXT.read_text(encoding="utf-8", errors="replace").split("\f")
    # These phrases were selected after reading the current root abstract,
    # introduction, contents, and method section. Anchors are recovered from
    # the current PDF rather than copied from an earlier ledger.
    phrases = [
        ("lattice field theory", "domain"),
        ("critical slowing down", "failure"),
        ("topological freezing", "failure"),
        ("unnormalized target distribution", "problem"),
        ("nonequilibrium thermodynamics", "foundation"),
        ("trajectory-level balance", "mechanism"),
        ("forward and backward stochastic dynamics", "mechanism"),
        ("path-space variational free energy", "objective"),
        ("entropy production", "objective"),
        ("Independence Metropolis", "correction"),
        ("stochastic quantization", "lineage"),
        ("normalizing flows", "adjacent_method"),
        ("continuous normalizing flows", "adjacent_method"),
        ("autoregressive networks", "adjacent_method"),
        ("stochastic normalizing flows", "adjacent_method"),
        ("diffusion", "adjacent_method"),
        ("path-space Kullback", "lineage"),
        ("mode collapse", "failure"),
        ("gauge equivariant", "extension"),
        ("training reference data", "boundary"),
        ("acceptance rate and training cost", "evaluation"),
        ("autocorrelation time", "evaluation"),
        ("full support of the target distribution", "boundary"),
        ("free energy density", "observable"),
    ]
    terms = []
    for index, (phrase, facet) in enumerate(phrases, 1):
        page, quote = page_anchor(pages, phrase)
        terms.append({
            "term_id": f"K{index:02d}", "term": phrase,
            "normalized_term": phrase.lower(), "facet": facet,
            "source": "root_pdf", "page": page, "anchor_quote": quote,
            "status": "root_grounded",
        })
    with (ROOT / "keyword_ledger.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(terms[0]))
        writer.writeheader(); writer.writerows(terms)

    authors = ["Shiyang Chen", "Moxian Qian", "Gert Aarts", "Biagio Lucini", "Kai Zhou"]
    routes = []
    def add(family: str, source: str, query: str, facet: str, parent: str) -> None:
        routes.append({"query_id": f"Q{len(routes)+1:02d}", "family": family,
                       "source": source, "query": query, "facet": facet,
                       "parent_evidence": parent})
    add("root", "OpenAlex", '"Stochastic Path Sampler For Lattice Field Theory"', "identity", "root title")
    add("root", "Crossref", '"Stochastic Path Sampler For Lattice Field Theory"', "identity", "root title")
    add("root", "arXiv", 'ti:"Stochastic Path Sampler For Lattice Field Theory"', "identity", "root title")
    add("backward", "root_bibliography", "all live root references", "lineage", "root TeX")
    add("forward", "OpenAlex", "works citing arXiv:2606.13790", "forward", "root arXiv ID")
    for author in authors:
        add("author", "OpenAlex", f'"{author}" lattice sampler', "author", "root title page")
    selected_terms = [row for row in terms if row["facet"] in {"mechanism", "objective", "correction", "failure", "adjacent_method", "extension", "boundary", "evaluation"}]
    for row in selected_terms[:14]:
        add("keyword", "OpenAlex", f'{row["term"]} sampling', row["facet"], row["term_id"])
    for row in selected_terms[4:10]:
        add("keyword", "arXiv", f'all:"{row["term"]}" AND all:"lattice field"', row["facet"], row["term_id"])
    add("adjacent", "OpenAlex", "learned sampler exact correction unnormalized target", "correction", "K10;K04")
    add("adversarial", "OpenAlex", "generative sampler critical slowing mode collapse", "failure", "K02;K18")
    add("extension", "OpenAlex", "gauge equivariant sampler topological freezing", "extension", "K03;K19")
    add("evaluation", "Crossref", "lattice sampler training cost autocorrelation", "evaluation", "K21;K22")
    add("source_link", "Crossref", "2606.13790", "identity", "root arXiv ID")
    add("closure", "OpenAlex", "path space sampler stochastic control diffusion", "lineage", "K07;K17")
    with (ROOT / "query_matrix.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(routes[0]))
        writer.writeheader(); writer.writerows(routes)

    print(f"references={len(refs)} terms={len(terms)} queries={len(routes)}")


if __name__ == "__main__":
    main()
