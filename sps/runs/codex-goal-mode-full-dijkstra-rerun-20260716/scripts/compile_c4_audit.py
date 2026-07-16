#!/usr/bin/env python3
"""Compile anchored C4 notes into Part 1 literature-audit artifacts."""

from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


def read_csv(path: Path, delimiter: str = ",") -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter=delimiter))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def surname(name: str) -> str:
    return name.strip().lower().split()[-1] if name.strip() else ""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()
    selected = read_csv(run_dir / "selected_fulltexts.csv")
    selected_by_id = {row["arxiv_id"]: row for row in selected}
    source_rows = read_csv(run_dir / "source_matrix.csv")
    source_by_id = {row["arxiv_id"]: row for row in source_rows}
    notes = read_csv(run_dir / "c4_reading_notes.psv", delimiter="|")
    notes_by_id = {row["arxiv_id"]: row for row in notes}
    expected_c4 = {row["arxiv_id"] for row in selected if row["target_level"] == "C4"}
    if set(notes_by_id) != expected_c4:
        missing = sorted(expected_c4 - set(notes_by_id))
        extra = sorted(set(notes_by_id) - expected_c4)
        raise SystemExit(f"C4 note set mismatch; missing={missing}; extra={extra}")
    required = [
        "problem", "problem_anchor", "method", "method_anchor", "result", "result_anchor",
        "scope_boundary", "scope_anchor", "safe_sentence", "prohibited_sentence",
    ]
    incomplete = [
        note["arxiv_id"] for note in notes
        if any(not note[field].strip() for field in required)
    ]
    if incomplete:
        raise SystemExit(f"C4 notes missing required fields: {incomplete}")

    updated_sources = []
    for row in source_rows:
        updated = dict(row)
        if row["arxiv_id"] in notes_by_id:
            updated["evidence_level"] = "C4_claim_anchored"
        updated_sources.append(updated)
    write_csv(run_dir / "source_matrix.csv", updated_sources, list(source_rows[0]))

    verification = read_csv(run_dir / "paper_verification_ledger.csv")
    updated_verification = []
    for row in verification:
        updated = dict(row)
        if row["arxiv_id"] in notes_by_id:
            updated["C4_claim_anchor"] = "pass"
            updated["review_status"] = "C4_anchored_manual_reading"
        updated_verification.append(updated)
    write_csv(run_dir / "paper_verification_ledger.csv", updated_verification, list(verification[0]))

    evidence_rows = []
    claim_rows = []
    reading_rows = []
    for row in selected:
        arxiv_id = row["arxiv_id"]
        source = source_by_id[arxiv_id]
        note = notes_by_id.get(arxiv_id)
        if note:
            anchor_map = (
                ("identity", "PDF p. 1 title block and current arXiv metadata", row["title"]),
                ("problem", note["problem_anchor"], note["problem"]),
                ("method", note["method_anchor"], note["method"]),
                ("result", note["result_anchor"], note["result"]),
                ("boundary", note["scope_anchor"], note["scope_boundary"]),
            )
            evidence_ids = []
            for suffix, anchor, content in anchor_map:
                evidence_id = f"E-{row['paper_id']}-{suffix[0].upper()}"
                evidence_ids.append(evidence_id)
                evidence_rows.append({
                    "evidence_id": evidence_id,
                    "paper_id": row["paper_id"],
                    "arxiv_id": arxiv_id,
                    "evidence_type": suffix,
                    "source_url": row["canonical_url"],
                    "pdf_path": source["pdf_path"],
                    "anchor": anchor,
                    "supported_content": content,
                    "status": "full_text_manual",
                    "sha256": source["pdf_sha256"],
                })
            claim_rows.append({
                "claim_id": f"C-{row['paper_id']}",
                "arxiv_id": arxiv_id,
                "title": row["title"],
                "claim": note["safe_sentence"],
                "source_anchor": note["result_anchor"],
                "evidence_ids": ";".join(evidence_ids),
                "boundary": note["scope_boundary"],
                "do_not_write": note["prohibited_sentence"],
                "status": "C4_anchored",
            })
            reading_rows.append({
                "paper_id": row["paper_id"],
                "identity_status": "verified",
                "title": row["title"],
                "authors": row["authors"],
                "version_date": row["published"],
                "arxiv_id": arxiv_id + row["version"],
                "canonical_url": row["canonical_url"],
                "pdf_pages": source["pdf_pages"],
                "reading_level": "C4",
                "problem": note["problem"],
                "problem_anchor": note["problem_anchor"],
                "method": note["method"],
                "method_anchor": note["method_anchor"],
                "result": note["result"],
                "result_anchor": note["result_anchor"],
                "scope_boundary": note["scope_boundary"],
                "scope_anchor": note["scope_anchor"],
                "relation_to_root": note["relation_to_root"],
                "relation_anchor": note["relation_anchor"],
                "safe_sentence": note["safe_sentence"],
                "prohibited_sentence": note["prohibited_sentence"],
                "evidence_ids": ";".join(evidence_ids),
                "next_search": note["next_search"],
            })
        else:
            reading_rows.append({
                "paper_id": row["paper_id"],
                "identity_status": "verified",
                "title": row["title"],
                "authors": row["authors"],
                "version_date": row["published"],
                "arxiv_id": arxiv_id + row["version"],
                "canonical_url": row["canonical_url"],
                "pdf_pages": source["pdf_pages"],
                "reading_level": "C3",
                "problem": "Full text was downloaded and extracted but is not used as a C4 claim anchor in this run.",
                "problem_anchor": "",
                "method": "",
                "method_anchor": "",
                "result": "",
                "result_anchor": "",
                "scope_boundary": "C3 source only; no report claim is derived from this record.",
                "scope_anchor": "",
                "relation_to_root": "not_claim_anchored",
                "relation_anchor": "",
                "safe_sentence": "This paper is a full-text contextual source, not a claim anchor in this report.",
                "prohibited_sentence": "Any unanchored technical or performance claim.",
                "evidence_ids": "",
                "next_search": "Upgrade only after a specific current-PDF claim is anchored.",
            })
    evidence_fields = [
        "evidence_id", "paper_id", "arxiv_id", "evidence_type", "source_url", "pdf_path",
        "anchor", "supported_content", "status", "sha256",
    ]
    write_csv(run_dir / "evidence_registry.csv", evidence_rows, evidence_fields)
    write_csv(run_dir / "claim_source_ledger.csv", claim_rows, list(claim_rows[0]))
    write_csv(run_dir / "native_paper_reading_ledger.csv", reading_rows, list(reading_rows[0]))
    write_csv(run_dir / "manual_reading_notes.csv", [
        row for row in reading_rows if row["reading_level"] == "C4"
    ], list(reading_rows[0]))

    # Keep the PDF's physical page number separate from its printed page number.
    direct_specs = [
        ("R001", "1904.12072", "[5]", "printed p. 29 (PDF page 30)"),
        ("R002", "2003.06413", "[8]", "printed p. 30 (PDF page 31)"),
        ("R003", "2512.19575", "[11]", "printed p. 30 (PDF page 31)"),
        ("R004", "2201.08862", "[19]", "printed p. 30 (PDF page 31)"),
        ("R005", "2210.03139", "[20]", "printed p. 30 (PDF page 31)"),
        ("R006", "2309.17082", "[25]", "printed p. 31 (PDF page 32)"),
        ("R007", "2605.11199", "[32]", "printed p. 31 (PDF page 32)"),
        ("R008", "2111.15141", "[33]", "printed p. 31 (PDF page 32)"),
        ("R009", "2302.13834", "[34]", "printed p. 31 (PDF page 32)"),
        ("R010", "2211.01364", "[35]", "printed p. 31 (PDF page 32)"),
    ]
    relation_rows = []
    for edge_id, target, ref_no, page in direct_specs:
        relation_rows.append({
            "edge_id": edge_id,
            "source_arxiv_id": "2606.13790",
            "target_arxiv_id": target,
            "relation_type": "direct_citation",
            "relation_basis": f"Exact title and arXiv identifier in SPS reference {ref_no}, {page}.",
            "evidence_id": f"CIT-{target}",
            "confidence": "high",
            "review_status": "exact_identifier_context_verified",
        })
    adjacent_specs = [
        ("M001", "2310.11979", "nonequilibrium topological-freezing method neighbor"),
        ("M002", "2402.06561", "nonequilibrium topological-freezing evaluation neighbor"),
        ("M003", "2604.10209", "multiscale critical-sampling comparison neighbor"),
        ("M004", "2607.08505", "post-root diffusion and diagnostic neighbor"),
    ]
    for edge_id, target, basis in adjacent_specs:
        relation_rows.append({
            "edge_id": edge_id,
            "source_arxiv_id": "2606.13790",
            "target_arxiv_id": target,
            "relation_type": "method_neighbor",
            "relation_basis": basis + "; not asserted as a direct citation.",
            "evidence_id": "",
            "confidence": "medium",
            "review_status": "non_citation_relation_declared",
        })
    write_csv(run_dir / "relation_ledger.csv", relation_rows, list(relation_rows[0]))
    write_csv(run_dir / "display_relation_ledger.csv", relation_rows, list(relation_rows[0]))
    root_bib = []
    for edge_id, target, ref_no, page in direct_specs:
        paper = selected_by_id[target]
        root_bib.append({
            "ref_no": ref_no.strip("[]"),
            "arxiv_id": target,
            "title": paper["title"],
            "authors": paper["authors"],
            "citation_context": f"SPS reference {ref_no}",
            "anchor": f"Root {page}",
            "source_url": paper["canonical_url"],
        })
    write_csv(run_dir / "root_bibliography.csv", root_bib, list(root_bib[0]))

    root_authors = {surname(author): author.strip() for author in selected_by_id["2606.13790"]["authors"].split(";")}
    author_rows = []
    for paper in selected:
        if paper["arxiv_id"] == "2606.13790":
            continue
        shared = [
            root_authors[surname(author)]
            for author in paper["authors"].split(";")
            if surname(author) in root_authors
        ]
        if shared:
            author_rows.append({
                "root_author": "; ".join(sorted(set(shared))),
                "related_paper_arxiv_id": paper["arxiv_id"],
                "related_paper": paper["title"],
                "relationship": "shared author across current arXiv metadata",
                "source": "fresh_arxiv_metadata.csv",
            })
    write_csv(run_dir / "author_lineage_table.csv", author_rows, list(author_rows[0]))

    keyword_rows = [
        ("K01", "stochastic path sampler", "method identity", "Root PDF p. 1 abstract"),
        ("K02", "unnormalized target", "problem", "Root PDF p. 1 abstract"),
        ("K03", "path-space variational free energy", "objective", "Root PDF p. 1 abstract"),
        ("K04", "entropy production", "objective", "Root PDF p. 1 abstract"),
        ("K05", "extended-space independence Metropolis-Hastings", "correction", "Root PDF pp. 7-8, Sec. 2.4"),
        ("K06", "critical slowing down", "failure mode", "Root PDF p. 1 abstract"),
        ("K07", "stochastic normalizing flow", "method lineage", "Root PDF p. 30, Refs. [19-20]"),
        ("K08", "Jarzynski equality", "method lineage", "Root PDF p. 30, Refs. [19-20]"),
        ("K09", "Schrodinger bridge", "adjacent method", "Root PDF p. 31, Ref. [33]"),
        ("K10", "denoising diffusion sampler", "adjacent method", "Root PDF p. 31, Ref. [34]"),
        ("K11", "observable-level cost", "evaluation gap", "Root PDF p. 21, Sec. 4"),
    ]
    write_csv(run_dir / "keyword_ledger.csv", [
        {"term_id": term_id, "term": term, "facet": facet, "source_anchor": anchor, "status": "root_grounded"}
        for term_id, term, facet, anchor in keyword_rows
    ], ["term_id", "term", "facet", "source_anchor", "status"])
    query_yields = {row["route_id"]: row for row in read_csv(run_dir / "query_yield_log.csv")}
    protocol = read_csv(run_dir / "search_protocol.csv")
    query_rows = [
        {
            "query_id": row["query_id"], "round": row["round"], "family": row["family"],
            "facet": row["facet"], "query": row["expression"], "source": "arXiv API",
            "raw_hits": query_yields[row["query_id"]]["raw_hits"], "status": query_yields[row["query_id"]]["status"],
        }
        for row in protocol
    ]
    write_csv(run_dir / "query_matrix.csv", query_rows, list(query_rows[0]))

    gaps = [
        ("G01", "SPS cost-normalized observable efficiency", "Open", "Root warns autocorrelation units differ and total cost is not matched.", "Run matched schedule and observable-level GPU-hour comparison."),
        ("G02", "SPS scaling beyond reported 2D phi4", "Open", "Root numerical evidence is 2D phi4.", "Test more volumes, dimensions, and model families."),
        ("G03", "Correction versus uncorrected proposal quality", "Partially resolved", "Root uses IMH correction and shows uncorrected proposal diagnostics.", "Report acceptance, weights, and corrected observable errors together."),
        ("G04", "Topological-freezing application", "Open for SPS", "Nearby nonequilibrium CP(N-1) work exists, but no SPS test is claimed here.", "Design an SPS versus nonequilibrium and PTBC comparison."),
        ("G05", "Mechanism of learned SPS paths", "Open", "Operator spectroscopy gives a related diagnostic framework, not an SPS analysis.", "Project trained SPS fields with held-out and negative controls."),
    ]
    write_csv(run_dir / "gap_ledger.csv", [
        {"gap_id": gap_id, "question": question, "status": status, "evidence_boundary": boundary, "next_step": next_step}
        for gap_id, question, status, boundary, next_step in gaps
    ], ["gap_id", "question", "status", "evidence_boundary", "next_step"])
    reviewer_rows = [
        ("Q01", "Is the sampler exact?", "SPS uses extended-space IMH; inspect the correction, not the proposal alone.", "Root PDF pp. 7-8."),
        ("Q02", "Does higher ESS prove physical efficiency?", "No. Observable errors and matched total cost remain a documented gap.", "Root PDF p. 21; G01."),
        ("Q03", "Is a neighboring method a baseline?", "Only when the model, schedule, correction, and cost are matched.", "C4 boundaries in the claim-source ledger."),
        ("Q04", "Which links are citations?", "Only relation_ledger entries labeled direct_citation; method neighbors are declared separately.", "relation_ledger.csv."),
    ]
    write_csv(run_dir / "reviewer_comparison_matrix.csv", [
        {"question_id": qid, "reviewer_question": question, "response_boundary": response, "source": source}
        for qid, question, response, source in reviewer_rows
    ], ["question_id", "reviewer_question", "response_boundary", "source"])

    report_lines = [
        "# SPS Literature Research Report",
        "",
        "## What is confirmed",
        "",
        "- Root identity: Stochastic Path Sampler For Lattice Field Theory, arXiv:2606.13790v1.",
        "- The root's stated mechanism is a learnable forward and backward Langevin path with a path-space objective and extended-space IMH correction.",
        "- The current C4 set separates direct root citations from method neighbors and from a post-root forward neighbor.",
        "",
        "## Coverage",
        "",
        f"- raw arXiv route records: {len(read_csv(run_dir / 'route_results.csv'))}",
        f"- deduplicated candidates: {len(read_csv(run_dir / 'candidate_screening_table.csv'))}",
        f"- current PDFs passing C3: {len(source_rows)}",
        f"- C4 claim anchors: {len(notes)}",
        f"- direct root-citation edges verified: {len(direct_specs)}",
        "",
        "## Boundary",
        "",
        "This report supports paper identity, stated methods, reported results, and explicit",
        "scope limits. It does not turn route distance, a search-hit count, ESS, or a single",
        "autocorrelation number into a universal computational-cost claim.",
    ]
    (run_dir / "literature_research_report.md").write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    matrix_lines = [
        "# Literature Matrix",
        "",
        "| paper | method family | safe conclusion | boundary |",
        "|---|---|---|---|",
    ]
    for claim in claim_rows:
        paper = selected_by_id[claim["arxiv_id"]]
        matrix_lines.append(
            f"| {claim['arxiv_id']} | {paper['cluster']} | {claim['claim']} | {claim['boundary']} |"
        )
    (run_dir / "literature_matrix.md").write_text("\n".join(matrix_lines) + "\n", encoding="utf-8")
    evidence_lines = [
        "# Evidence Registry",
        "",
        "Each entry points to a current downloaded PDF and a short anchor. The content is a",
        "paraphrase for the stated claim, not a replacement for the source.",
        "",
        "| evidence | paper | type | anchor |",
        "|---|---|---|---|",
    ]
    for item in evidence_rows:
        evidence_lines.append(f"| {item['evidence_id']} | {item['arxiv_id']} | {item['evidence_type']} | {item['anchor']} |")
    (run_dir / "evidence_registry.md").write_text("\n".join(evidence_lines) + "\n", encoding="utf-8")
    claim_lines = [
        "# Claim-Source Ledger",
        "",
        "| claim | paper | source anchor | boundary |",
        "|---|---|---|---|",
    ]
    for claim in claim_rows:
        claim_lines.append(f"| {claim['claim']} | {claim['arxiv_id']} | {claim['source_anchor']} | {claim['boundary']} |")
    (run_dir / "claim_source_ledger.md").write_text("\n".join(claim_lines) + "\n", encoding="utf-8")
    state_path = run_dir / "research_state.md"
    state_path.write_text(
        state_path.read_text(encoding="utf-8")
        + f"\n- C3 gate: {len(source_rows)}/{len(source_rows)} selected PDFs passed\n"
        + f"- C4 gate: {len(notes)}/{len(expected_c4)} planned core papers have anchored notes\n"
        + "- next stage: perform L5-L10 expansion from the verified keyword and gap ledgers.\n",
        encoding="utf-8",
    )
    print(f"c4={len(notes)} evidence={len(evidence_rows)} direct_citations={len(direct_specs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
