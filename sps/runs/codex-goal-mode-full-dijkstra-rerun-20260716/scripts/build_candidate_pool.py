#!/usr/bin/env python3
"""Apply explicit C0-C2 screening to fresh arXiv route results."""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT_ID = "2606.13790"
ROOT_TITLE = "stochastic path sampler for lattice field theory"

DOMAIN_TERMS = (
    "lattice field theory", "lattice gauge", "lattice phi", "lattice φ",
    "lattice scalar", "boltzmann distribution", "hep-lat", "ising model",
    "phi4", "φ4",
)
METHOD_TERMS = (
    "sampling", "sampler", "monte carlo", "mcmc", "normalizing flow",
    "generative", "diffusion", "importance sampling", "reweight",
    "metropolis", "langevin",
)
MECHANISM_TERMS = (
    "path space", "path-space", "stochastic control", "schrödinger",
    "schrodinger", "nonequilibrium", "non-equilibrium", "jarzynski",
    "entropy production", "reverse sde", "trajectory",
)
EVALUATION_TERMS = (
    "critical slowing", "autocorrelation", "acceptance", "effective sample",
    "exact", "bias", "variance", "hmc", "hybrid monte carlo",
)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def normalise(value: str) -> str:
    return re.sub(r"\s+", " ", value.lower()).strip()


def matched_terms(text: str, terms: tuple[str, ...]) -> list[str]:
    return [term for term in terms if term in text]


def yes_no(value: bool) -> str:
    return "pass" if value else "fail"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()
    metadata = read_csv(run_dir / "fresh_arxiv_metadata.csv")
    route_results = read_csv(run_dir / "route_results.csv")
    protocol = read_csv(run_dir / "search_protocol.csv")

    hits_by_id: defaultdict[str, list[dict[str, str]]] = defaultdict(list)
    for hit in route_results:
        hits_by_id[hit["arxiv_id"]].append(hit)
    root_hits = [row for row in route_results if row["arxiv_id"] == ROOT_ID]
    identity_rows = []
    for route in ("Q01", "Q02", "P01"):
        relevant = [row for row in root_hits if row["route_id"] == route]
        title_match = bool(relevant and normalise(relevant[0]["title"]) == ROOT_TITLE)
        identity_rows.append({
            "route_id": route,
            "root_identifier_returned": "PASS" if relevant else "FAIL",
            "title_match": "PASS" if title_match else "FAIL",
            "returned_title": relevant[0]["title"] if relevant else "",
            "source_url": relevant[0]["canonical_url"] if relevant else "",
            "raw_file": relevant[0]["raw_file"] if relevant else "",
        })
    write_csv(run_dir / "root_identity_check.csv", identity_rows, [
        "route_id", "root_identifier_returned", "title_match", "returned_title", "source_url", "raw_file",
    ])
    if any(row["root_identifier_returned"] != "PASS" or row["title_match"] != "PASS" for row in identity_rows):
        raise SystemExit("Root identity gate failed")

    screening_rows = []
    raw_rows = []
    for item in metadata:
        arxiv_id = item["arxiv_id"]
        text = normalise(" ".join([
            item["title"], item["abstract"], item["categories"], item["primary_category"],
        ]))
        domain = matched_terms(text, DOMAIN_TERMS)
        method = matched_terms(text, METHOD_TERMS)
        mechanism = matched_terms(text, MECHANISM_TERMS)
        evaluation = matched_terms(text, EVALUATION_TERMS)
        hits = hits_by_id[arxiv_id]
        route_ids = sorted({hit["route_id"] for hit in hits})
        route_ranks = ";".join(
            f"{hit['route_id']}:{hit['rank']}" for hit in sorted(hits, key=lambda row: (row["route_id"], int(row["rank"])))
        )
        route_families = sorted({hit["family"] for hit in hits})
        is_root = arxiv_id == ROOT_ID
        is_direct_probe = any(route.startswith("P") for route in route_ids)
        score = (
            100 if is_root else 0
        ) + 4 * len(domain) + 3 * len(method) + 2 * len(mechanism) + len(evaluation) + min(len(route_ids), 3)
        domain_gate = bool(domain) or item["primary_category"] == "hep-lat"
        method_gate = bool(method)
        c0 = "pass"
        c1 = yes_no(bool(arxiv_id and item["title"] and item["authors"] and item["canonical_url"]))
        c2 = yes_no(len(item["abstract"]) >= 80)
        if is_root:
            decision = "include"
            reason = "root identity passed by identifier and exact-title routes"
        elif c1 != "pass" or c2 != "pass":
            decision = "exclude"
            reason = "metadata or abstract gate failed"
        elif domain_gate and method_gate and score >= 9:
            decision = "include"
            reason = "domain and sampling-method gates passed"
        elif is_direct_probe and method_gate:
            decision = "candidate"
            reason = "identifier probe passed; method adjacency needs full-text review"
        elif method_gate and (mechanism or evaluation) and score >= 7:
            decision = "candidate"
            reason = "general method adjacency; not yet domain-specific evidence"
        else:
            decision = "exclude"
            reason = "did not jointly satisfy domain and sampling-method gates"
        screening_rows.append({
            "candidate_id": f"arxiv:{arxiv_id}",
            "arxiv_id": arxiv_id,
            "title": item["title"],
            "authors": item["authors"],
            "published": item["published"],
            "primary_category": item["primary_category"],
            "route_ids": ";".join(route_ids),
            "route_families": ";".join(route_families),
            "route_ranks": route_ranks,
            "C0_candidate": c0,
            "C1_metadata": c1,
            "C2_abstract": c2,
            "domain_hits": ";".join(domain),
            "method_hits": ";".join(method),
            "mechanism_hits": ";".join(mechanism),
            "evaluation_hits": ";".join(evaluation),
            "screen_score": score,
            "decision": decision,
            "screen_reason": reason,
            "canonical_url": item["canonical_url"],
            "pdf_url": item["pdf_url"],
            "raw_files": item["raw_files"],
        })
        for hit in hits:
            raw_rows.append({
                "candidate_id": f"arxiv:{arxiv_id}",
                "arxiv_id": arxiv_id,
                "route_id": hit["route_id"],
                "round": hit["round"],
                "family": hit["family"],
                "facet": hit["facet"],
                "rank": hit["rank"],
                "title": hit["title"],
                "canonical_url": hit["canonical_url"],
                "raw_file": hit["raw_file"],
            })
    screening_rows.sort(key=lambda row: (
        {"include": 0, "candidate": 1, "exclude": 2}[str(row["decision"])],
        -int(row["screen_score"]),
        str(row["arxiv_id"]),
    ))
    for rank, row in enumerate(screening_rows, 1):
        row["screen_rank"] = rank
    fields = [
        "screen_rank", "candidate_id", "arxiv_id", "title", "authors", "published", "primary_category",
        "route_ids", "route_families", "route_ranks", "C0_candidate", "C1_metadata", "C2_abstract",
        "domain_hits", "method_hits", "mechanism_hits", "evaluation_hits", "screen_score", "decision",
        "screen_reason", "canonical_url", "pdf_url", "raw_files",
    ]
    write_csv(run_dir / "candidate_screening_table.csv", screening_rows, fields)
    write_csv(run_dir / "candidate_pool_raw.csv", raw_rows, [
        "candidate_id", "arxiv_id", "route_id", "round", "family", "facet", "rank", "title", "canonical_url", "raw_file",
    ])

    decision_count = Counter(str(row["decision"]) for row in screening_rows)
    round_counts: dict[str, set[str]] = defaultdict(set)
    for row in raw_rows:
        round_counts[str(row["round"])].add(str(row["arxiv_id"]))
    route_quality = []
    for route in protocol:
        route_rows = [row for row in raw_rows if row["route_id"] == route["query_id"]]
        included = sum(
            1 for row in screening_rows
            if row["decision"] == "include" and route["query_id"] in str(row["route_ids"]).split(";")
        )
        candidates = sum(
            1 for row in screening_rows
            if row["decision"] == "candidate" and route["query_id"] in str(row["route_ids"]).split(";")
        )
        route_quality.append({
            "route_id": route["query_id"], "round": route["round"], "family": route["family"],
            "facet": route["facet"], "query": route["expression"], "raw_hits": len(route_rows),
            "unique_hits": len({row["arxiv_id"] for row in route_rows}), "included": included,
            "candidate_only": candidates,
        })
    write_csv(run_dir / "route_quality_audit.csv", route_quality, [
        "route_id", "round", "family", "facet", "query", "raw_hits", "unique_hits", "included", "candidate_only",
    ])
    lines = [
        "# Candidate Pool",
        "",
        "This pool is derived from the current run's raw arXiv responses. It is not a bibliography.",
        "",
        "## C0-C2 gate",
        "",
        "- C0: a deduplicated arXiv candidate.",
        "- C1: identifier, title, authors, and canonical source URL present.",
        "- C2: abstract is present and long enough for a preliminary relevance screen.",
        f"- records: {len(screening_rows)}",
        f"- include for full-text queue: {decision_count['include']}",
        f"- method-adjacent candidates: {decision_count['candidate']}",
        f"- excluded at C0-C2: {decision_count['exclude']}",
        "",
        "## Boundary",
        "",
        "An include label means only that the paper cleared preliminary identity and",
        "topic gates. It is not a claim about a paper's result. C3/C4 require the current",
        "PDF and an anchored reading record.",
    ]
    (run_dir / "candidate_pool.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    round_lines = [
        "# Round Log",
        "",
        "| round | purpose | unique retrieved records |",
        "|---|---|---:|",
        "| L0 | root identity and exact-title checks | " + str(len(round_counts["L0"])) + " |",
        "| L1 | root terminology, direct hypotheses, and domain methods | " + str(len(round_counts["L1"])) + " |",
        "| L2 | mechanism and adjacent-method expansion | " + str(len(round_counts["L2"])) + " |",
        "| L3 | author and method-precedent expansion | " + str(len(round_counts["L3"])) + " |",
        "| L4 | evaluation, correction, and recent-neighbor expansion | " + str(len(round_counts["L4"])) + " |",
        "",
        "Raw route-by-route yields are in query_yield_log.csv; the C0-C2 decision for",
        "every deduplicated record is in candidate_screening_table.csv.",
    ]
    (run_dir / "round_log.md").write_text("\n".join(round_lines) + "\n", encoding="utf-8")
    route_lines = [
        "# Search Route Log",
        "",
        "The protocol is intentionally wider than the final reading list. This avoids",
        "equating a verbal clue with a settled literature boundary.",
        "",
        "| route | round | family | facet | query |",
        "|---|---|---|---|---|",
    ]
    for route in protocol:
        route_lines.append(
            f"| {route['query_id']} | {route['round']} | {route['family']} | {route['facet']} | {route['expression']} |"
        )
    (run_dir / "search_route_log.md").write_text("\n".join(route_lines) + "\n", encoding="utf-8")
    state = [
        "# Research State",
        "",
        "- topic: SPS / stochastic path sampler for lattice field theory",
        "- intent: cover, with evaluation as a secondary question",
        "- root: arXiv:2606.13790",
        "- stage: C0-C2 complete; C3/C4 reading selection pending",
        f"- raw route records: {len(raw_rows)}",
        f"- deduplicated candidates: {len(screening_rows)}",
        f"- root identity routes passing: {sum(row['root_identifier_returned'] == 'PASS' for row in identity_rows)}/{len(identity_rows)}",
        "- current open question: which methods have a directly sourced relation to SPS, and which are only adjacent?",
    ]
    (run_dir / "research_state.md").write_text("\n".join(state) + "\n", encoding="utf-8")
    print(
        f"records={len(screening_rows)} include={decision_count['include']} "
        f"candidate={decision_count['candidate']} exclude={decision_count['exclude']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
