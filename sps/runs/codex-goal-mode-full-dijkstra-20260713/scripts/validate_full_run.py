#!/usr/bin/env python3
"""Validate the complete SPS literature run, including Dijkstra invariants."""

from __future__ import annotations

import csv
import hashlib
import heapq
import json
import math
import re
import subprocess
import time
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def rows(name: str) -> list[dict[str, str]]:
    with (ROOT / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def page_count(path: Path) -> int:
    output = subprocess.check_output(["pdfinfo", str(path)], text=True, errors="replace")
    match = re.search(r"^Pages:\s+(\d+)", output, flags=re.MULTILINE)
    if not match:
        raise ValueError(f"Pages missing from {path}")
    return int(match.group(1))


def graph(edges: list[dict[str, str]]) -> dict[str, list[tuple[str, float]]]:
    adjacency: dict[str, list[tuple[str, float]]] = defaultdict(list)
    for edge in edges:
        adjacency[edge["source"]].append((edge["target"], float(edge["weight"])))
    return adjacency


def dijkstra(adjacency: dict[str, list[tuple[str, float]]], root: str) -> dict[str, float]:
    distance = {root: 0.0}
    queue = [(0.0, root)]
    while queue:
        cost, node = heapq.heappop(queue)
        if cost > distance[node] + 1e-12:
            continue
        for target, weight in adjacency.get(node, []):
            proposal = cost + weight
            if proposal + 1e-12 < distance.get(target, math.inf):
                distance[target] = proposal
                heapq.heappush(queue, (proposal, target))
    return distance


def parse_path(value: str) -> list[str]:
    return [part.strip() for part in value.split(" -> ") if part.strip()]


def parse_weights(value: str) -> list[float]:
    return [float(part.strip()) for part in value.split(" + ") if part.strip()]


def validate_paths(
    edge_rows: list[dict[str, str]], path_rows: list[dict[str, str]], root: str,
    distance_field: str, path_field: str, weight_field: str, target_field: str,
) -> list[str]:
    errors = []
    adjacency = graph(edge_rows)
    independent = dijkstra(adjacency, root)
    exact_edges = defaultdict(list)
    for edge in edge_rows:
        exact_edges[(edge["source"], edge["target"])].append(float(edge["weight"]))
    for row in path_rows:
        if row.get("reachable", "yes") != "yes":
            continue
        nodes = parse_path(row[path_field])
        weights = parse_weights(row[weight_field])
        target = target_field.format(value=row[target_field.split("{")[0]]) if "{" in target_field else row[target_field]
        if not nodes or nodes[0] != root:
            errors.append(f"path does not start at root: {row}")
            continue
        if len(nodes) != len(weights) + 1:
            errors.append(f"path/weight length mismatch: {row}")
            continue
        for source, destination, weight in zip(nodes, nodes[1:], weights):
            if not any(abs(candidate - weight) < 1e-8 for candidate in exact_edges[(source, destination)]):
                errors.append(f"missing exact edge {source}->{destination} weight={weight}")
        reported = float(row[distance_field])
        recomputed = sum(weights)
        if abs(reported - recomputed) > 1e-6:
            errors.append(f"reported path cost mismatch for {nodes[-1]}: {reported} vs {recomputed}")
        if abs(reported - independent.get(nodes[-1], math.inf)) > 1e-6:
            errors.append(f"not an independently shortest path for {nodes[-1]}")
    return errors


def check(results: list[dict[str, object]], name: str, passed: bool, detail: str) -> None:
    results.append({"gate": name, "status": "PASS" if passed else "FAIL", "detail": detail})


def main() -> None:
    results: list[dict[str, object]] = []
    selected = rows("selected_fulltexts.csv")
    selected_ids = {row["arxiv_id"] for row in selected}
    notes = rows("manual_reading_notes.csv")
    pdfs = rows("fulltext_download_status.csv")
    sources = rows("source_link_verification.csv")
    evidence = rows("evidence_registry.csv")
    claims = rows("claim_source_ledger.csv")
    numbers = rows("numerical_ledger.csv")
    gaps = rows("gap_ledger.csv")
    relations = rows("relation_ledger.csv")

    check(results, "selected_read_pdf_source_sets", selected_ids == {r["arxiv_id"] for r in notes} == {r["arxiv_id"] for r in pdfs} == {r["arxiv_id"] for r in sources}, f"sets={len(selected_ids)}/{len(notes)}/{len(pdfs)}/{len(sources)}")
    check(results, "fulltext_count", len(selected) == 37, f"count={len(selected)}")
    check(results, "reading_anchors", all(all(row.get(f"{role}_anchor", "").strip() for role in ("problem", "method", "result", "limitation")) for row in notes), "all four anchors present per paper")

    pdf_errors = []
    total_pages = 0
    for row in pdfs:
        path = ROOT / row["pdf_path"]
        if not path.exists() or row["status"] != "verified_pdf":
            pdf_errors.append(f"missing/failed {row['arxiv_id']}")
            continue
        actual_hash = sha256(path)
        actual_pages = page_count(path)
        total_pages += actual_pages
        if actual_hash != row["sha256"] or actual_pages != int(row["pages"]):
            pdf_errors.append(f"hash/page mismatch {row['arxiv_id']}")
    check(results, "pdf_integrity", not pdf_errors, f"pages={total_pages}; errors={pdf_errors}")
    check(results, "source_links", all(row["status"] == "VERIFIED" and row["source_url"].startswith("https://") for row in sources), f"verified={sum(row['status']=='VERIFIED' for row in sources)}")

    evidence_ids = [row["evidence_id"] for row in evidence]
    check(results, "evidence_registry_shape", len(evidence) == 5 * len(selected) and len(set(evidence_ids)) == len(evidence_ids), f"entries={len(evidence)} expected={5*len(selected)}")
    evidence_set = set(evidence_ids)
    claim_refs = [item for row in claims for item in row["evidence_ids"].split(";") if item]
    gap_refs = [item for row in gaps for item in row["evidence_ids"].split(";") if item]
    check(results, "claim_evidence_links", set(claim_refs) <= evidence_set, f"claims={len(claims)} refs={len(claim_refs)}")
    check(results, "gap_evidence_links", set(gap_refs) <= evidence_set, f"gaps={len(gaps)} refs={len(gap_refs)}")
    check(results, "numerical_claims", all(row["arxiv_id"] in selected_ids and row["source_anchor"].strip() and row["boundary"].strip() and row["evidence_id"] in evidence_set for row in numbers), f"numbers={len(numbers)}")

    relation_pairs = {(row["source_arxiv_id"], row["target_arxiv_id"]) for row in relations}
    relation_ok = all(
        row["relation_type"] == "direct_citation"
        and row["source_arxiv_id"] in selected_ids
        and row["target_arxiv_id"] in selected_ids
        and row["relation_basis"].strip()
        and row["evidence_id"].strip()
        for row in relations
    )
    check(results, "direct_citation_relations", relation_ok and len(relation_pairs) == len(relations), f"edges={len(relations)} unique_pairs={len(relation_pairs)}")

    candidate_nodes = rows("dijkstra_candidate_graph_nodes.csv")
    candidate_edges = rows("dijkstra_candidate_graph_edges.csv")
    candidate_paths = rows("dijkstra_candidate_shortest_paths.csv")
    check(results, "candidate_graph_size", len(candidate_nodes) == 3300 and len(candidate_edges) == 8187 and len(candidate_paths) == 593, f"nodes={len(candidate_nodes)} edges={len(candidate_edges)} paths={len(candidate_paths)}")
    candidate_errors = validate_paths(
        candidate_edges, candidate_paths, "paper:arxiv:2606.13790",
        "dijkstra_distance", "path_nodes", "path_edge_weights", "candidate_id",
    )
    candidate_root = next((row for row in candidate_paths if row["candidate_id"] == "arxiv:2606.13790"), None)
    check(results, "candidate_dijkstra_invariants", not candidate_errors and candidate_root is not None and float(candidate_root["dijkstra_distance"]) == 0.0, f"errors={candidate_errors[:5]}")

    verified_nodes = rows("dijkstra_graph_nodes.csv")
    verified_edges = rows("dijkstra_graph_edges.csv")
    verified_paths = rows("dijkstra_shortest_paths.csv")
    check(results, "verified_graph_size", len(verified_nodes) == 164 and len(verified_edges) == 944 and len(verified_paths) == 37, f"nodes={len(verified_nodes)} edges={len(verified_edges)} paths={len(verified_paths)}")
    verified_errors = validate_paths(
        verified_edges, verified_paths, "paper:2606.13790",
        "dijkstra_distance", "path_nodes", "path_weights", "arxiv_id",
    )
    verified_root = next((row for row in verified_paths if row["arxiv_id"] == "2606.13790"), None)
    check(results, "verified_dijkstra_invariants", not verified_errors and verified_root is not None and float(verified_root["dijkstra_distance"]) == 0.0, f"errors={verified_errors[:5]}")
    check(results, "verified_path_semantics", all(row["path_kind"] in {"root", "citation_only", "author_bridge", "method_bridge"} for row in verified_paths), str(dict((kind, sum(row['path_kind']==kind for row in verified_paths)) for kind in {row['path_kind'] for row in verified_paths})))

    selection_rows = rows("dijkstra_selection_comparison.csv")
    baseline = {row["candidate_id"] for row in selection_rows if row["baseline_selected"] == "yes"}
    graph_selected = {row["candidate_id"] for row in selection_rows if row["dijkstra_selected"] == "yes"}
    check(results, "equal_budget_selection_comparison", len(baseline) == len(graph_selected) == 30 and len(baseline & graph_selected) == 20, f"baseline={len(baseline)} dijkstra={len(graph_selected)} overlap={len(baseline & graph_selected)}")

    required = [
        "README.md", "full_run_contract.md", "research_state.md", "round_log.md",
        "candidate_pool.md", "evidence_registry.md", "claim_source_ledger.md",
        "literature_matrix.md", "lineage_snowball_map.md", "gap_ledger.csv",
        "dijkstra_candidate_run_report.md", "dijkstra_run_report.md",
        "dijkstra_effect_evaluation.md", "coverage_stopping_report.md",
        "literature_research_report.md", "output_manifest.md",
        "graphs/landscape_map.png", "graphs/citation_lineage_graph.png",
        "graphs/audit_funnel.png", "graphs/dijkstra_selection_effect.png",
        "sps_literature_audit_full_dijkstra.xlsx",
    ]
    missing = [name for name in required if not (ROOT / name).exists() or (ROOT / name).stat().st_size == 0]
    check(results, "required_artifacts", not missing, f"missing={missing}")
    previews = list((ROOT / "qa_workbook").glob("*.png"))
    check(results, "workbook_visual_qa", len(previews) >= 15 and all(path.stat().st_size > 1000 for path in previews), f"previews={len(previews)}")
    inspect_path = ROOT / "sps_literature_audit_full_dijkstra.xlsx.inspect.ndjson"
    inspect_text = inspect_path.read_text(encoding="utf-8", errors="replace") if inspect_path.exists() else ""
    check(results, "workbook_formula_scan", bool(inspect_text) and not re.search(r"#REF!|#DIV/0!|#VALUE!|#NAME\?|#N/A", inspect_text), "no formula error tokens")

    failures = [row for row in results if row["status"] != "PASS"]
    report = {
        "validated_at_epoch": int(time.time()),
        "status": "PASS" if not failures else "FAIL",
        "counts": {
            "selected_fulltexts": len(selected), "verified_pages": total_pages,
            "evidence_entries": len(evidence), "direct_citation_edges": len(relations),
            "candidate_graph_nodes": len(candidate_nodes), "candidate_graph_edges": len(candidate_edges),
            "verified_graph_nodes": len(verified_nodes), "verified_graph_edges": len(verified_edges),
        },
        "gates": results,
    }
    (ROOT / "final_validation_report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    lines = ["# Final Validation Report", "", f"**Status: {report['status']}**", "", "| Gate | Status | Detail |", "|---|---|---|"]
    for row in results:
        lines.append(f"| {row['gate']} | {row['status']} | {str(row['detail']).replace('|', '/')} |")
    lines.extend(["", "Dijkstra distances are navigation costs. Passing these gates does not convert a path score into scientific evidence."])
    (ROOT / "final_validation_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "gates": len(results), "failures": failures}, indent=2))
    if failures:
        raise SystemExit("Full-run validation failed")


if __name__ == "__main__":
    main()
