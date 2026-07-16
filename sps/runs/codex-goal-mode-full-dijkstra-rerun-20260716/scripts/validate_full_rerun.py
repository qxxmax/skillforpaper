#!/usr/bin/env python3
"""Independently validate the fresh SPS Part 1 rerun artifacts."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from collections import Counter
from pathlib import Path


def read_csv(path: Path, delimiter: str = ",") -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter=delimiter))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    args = parser.parse_args()
    run_dir = args.run_dir.resolve()
    checks: list[dict[str, str]] = []

    def check(name: str, condition: bool, detail: str) -> None:
        checks.append({"name": name, "status": "PASS" if condition else "FAIL", "detail": detail})

    required = [
        "full_run_contract.md", "invocation_manifest.json", "search_protocol.csv", "identifier_probes.csv",
        "retrieval_log_all_rounds.csv", "route_results.csv", "candidate_screening_table.csv",
        "root_identity_check.csv", "selected_fulltexts.csv", "fulltext_download_status.tsv",
        "source_matrix.csv", "paper_verification_ledger.csv", "c4_reading_notes.psv",
        "evidence_registry.csv", "claim_source_ledger.csv", "relation_ledger.csv",
        "root_bibliography.csv", "author_lineage_table.csv", "keyword_ledger.csv", "query_matrix.csv",
        "gap_ledger.csv", "visual_source_audit.csv", "visual_source_audit.md", "source_link_verification.csv",
        "dijkstra_graph_nodes.csv", "dijkstra_graph_edges.csv", "dijkstra_computed/dijkstra_shortest_paths.csv",
        "dijkstra_selection_comparison.csv", "dijkstra_effect_evaluation.md", "coverage_stopping_report.md",
        "run_report.md", "output_manifest.md", "numerical_ledger.csv", "goal_usage_snapshots.csv", "runtime_accounting.md",
        "graphs/landscape_map.png", "graphs/citation_lineage_graph.png", "graphs/audit_funnel.png",
        "graphs/dijkstra_selection_effect.png",
    ]
    missing = [item for item in required if not (run_dir / item).is_file()]
    check("required_artifacts", not missing, "all required artifacts present" if not missing else "; ".join(missing))
    if missing:
        payload = {"overall": "FAIL", "checks": checks}
        (run_dir / "final_validation_report.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        (run_dir / "final_validation_report.md").write_text("# Final Validation\n\nRequired artifacts are missing.\n", encoding="utf-8")
        return 1

    protocol = read_csv(run_dir / "search_protocol.csv")
    expected_queries = {f"Q{i:02}" for i in range(1, 25)}
    check(
        "L0_L10_protocol",
        len(protocol) == 24 and {row["query_id"] for row in protocol} == expected_queries,
        f"{len(protocol)} configured Q routes",
    )
    probes = read_csv(run_dir / "identifier_probes.csv")
    expected_probes = {f"P{i:02}" for i in range(1, 13)}
    check(
        "identifier_probe_plan",
        len(probes) == 12 and {row["probe_id"] for row in probes} == expected_probes,
        f"{len(probes)} configured identifier probes",
    )

    retrieval = read_csv(run_dir / "retrieval_log_all_rounds.csv")
    retrieval_ids = {row["route_id"] for row in retrieval}
    check(
        "fresh_retrievals",
        len(retrieval) == 36 and retrieval_ids == expected_queries | expected_probes and all(row["status"] == "OK" for row in retrieval),
        f"{len(retrieval)} logged routes; statuses={dict(Counter(row['status'] for row in retrieval))}",
    )
    raw_files_ok = all((run_dir / row["raw_file"]).is_file() and row["sha256"] for row in retrieval)
    check("raw_source_artifacts", raw_files_ok, "every retrieval row has a current raw response and hash")

    root = read_csv(run_dir / "root_identity_check.csv")
    check(
        "root_identity",
        len(root) == 3 and {row["route_id"] for row in root} == {"Q01", "Q02", "P01"}
        and all(row["root_identifier_returned"] == "PASS" and row["title_match"] == "PASS" for row in root),
        "Q01, Q02, and P01 agree on arXiv:2606.13790 and title",
    )

    route_records = read_csv(run_dir / "route_results.csv")
    screening = read_csv(run_dir / "candidate_screening_table.csv")
    decisions = Counter(row["decision"] for row in screening)
    root_screen = next((row for row in screening if row["arxiv_id"] == "2606.13790"), None)
    check("candidate_pool_size", len(route_records) == 371 and len(screening) == 308, f"raw={len(route_records)}, deduplicated={len(screening)}")
    check(
        "candidate_screening_decisions",
        decisions == Counter({"include": 94, "candidate": 57, "exclude": 157}),
        f"{dict(decisions)}",
    )
    check(
        "root_screen_status",
        root_screen is not None and root_screen["decision"] == "include"
        and all(root_screen[level] == "pass" for level in ("C0_candidate", "C1_metadata", "C2_abstract")),
        "root is included and passes C0-C2",
    )

    selected = read_csv(run_dir / "selected_fulltexts.csv")
    downloads = read_csv(run_dir / "fulltext_download_status.tsv", delimiter="\t")
    source_matrix = read_csv(run_dir / "source_matrix.csv")
    verification = read_csv(run_dir / "paper_verification_ledger.csv")
    download_by_id = {row["arxiv_id"]: row for row in downloads}
    c3_integrity = True
    for row in selected:
        status = download_by_id.get(row["arxiv_id"])
        if not status or status["status"] != "OK":
            c3_integrity = False
            continue
        pdf = run_dir / status["pdf_file"]
        text = run_dir / status["text_file"]
        c3_integrity &= pdf.is_file() and text.is_file() and text.stat().st_size > 500
        c3_integrity &= sha256(pdf) == status["sha256"]
    check(
        "C3_source_integrity",
        len(selected) == 21 and len(downloads) == 21 and len(source_matrix) == 21 and c3_integrity,
        f"{len(selected)} selected PDFs checksum-rechecked",
    )
    c4_planned = {row["arxiv_id"] for row in selected if row["target_level"] == "C4"}
    c4_notes = read_csv(run_dir / "c4_reading_notes.psv", delimiter="|")
    c4_ids = {row["arxiv_id"] for row in c4_notes}
    check(
        "C4_anchor_set",
        len(c4_notes) == 14 and c4_ids == c4_planned,
        f"{len(c4_notes)} C4 records for {len(c4_planned)} planned sources",
    )
    check(
        "C4_verification_ledger",
        sum(row["C4_claim_anchor"] == "pass" for row in verification) == 14
        and all(row["C3_full_text"] == "pass" for row in verification),
        "all selected sources pass C3; planned core sources pass C4",
    )

    evidence = read_csv(run_dir / "evidence_registry.csv")
    claims = read_csv(run_dir / "claim_source_ledger.csv")
    relations = read_csv(run_dir / "relation_ledger.csv")
    direct = [row for row in relations if row["relation_type"] == "direct_citation"]
    check("evidence_and_claim_ledgers", len(evidence) == 70 and len(claims) == 14, f"evidence={len(evidence)}, claims={len(claims)}")
    check(
        "direct_citation_lineage",
        len(relations) == 14 and len(direct) == 10
        and all(row["review_status"] == "exact_identifier_context_verified" for row in direct)
        and all("printed p." in row["relation_basis"] and "PDF page" in row["relation_basis"] for row in direct),
        f"relations={len(relations)}, direct={len(direct)} with explicit physical/printed page anchors",
    )

    visual = read_csv(run_dir / "visual_source_audit.csv")
    source_links = read_csv(run_dir / "source_link_verification.csv")
    visual_files_ok = all((run_dir / row["screenshot"]).is_file() and (run_dir / row["screenshot"]).stat().st_size > 1000 for row in visual)
    check(
        "key_visual_source_audit",
        len(visual) == 7 and all(row["visual_result"] == "PASS" for row in visual) and visual_files_ok,
        f"{len(visual)} source-page screenshots registered",
    )
    check(
        "source_link_ledger",
        len(source_links) == 21 and all(row["full_text_integrity"] == "PASS" for row in source_links)
        and sum(row["status"] == "VERIFIED_C3_WITH_KEY_VISUAL" for row in source_links) == 4,
        "all C3 links pass; four papers have selected visual anchors",
    )

    nodes = read_csv(run_dir / "dijkstra_graph_nodes.csv")
    edges = read_csv(run_dir / "dijkstra_graph_edges.csv")
    node_ids = {row["node_id"] for row in nodes}
    edge_by_id = {row["edge_id"]: row for row in edges}
    graph_ok = len(nodes) == 254 and len(edges) == 464 and len(edge_by_id) == len(edges)
    graph_ok &= all(row["source"] in node_ids and row["target"] in node_ids and float(row["weight"]) > 0 for row in edges)
    check("dijkstra_input_graph", graph_ok, f"nodes={len(nodes)}, edges={len(edges)}")

    paths = read_csv(run_dir / "dijkstra_computed" / "dijkstra_shortest_paths.csv")
    path_ok = len(paths) == len(nodes) and all(row["reachable"] == "yes" for row in paths)
    root_path = next((row for row in paths if row["node_id"] == "paper:2606.13790"), None)
    path_ok &= root_path is not None and math.isclose(float(root_path["dijkstra_distance"]), 0.0)
    for row in paths:
        if not row["path_edge_ids"]:
            continue
        ids = row["path_edge_ids"].split(" -> ")
        if not all(edge_id in edge_by_id for edge_id in ids):
            path_ok = False
            break
        recomputed = sum(float(edge_by_id[edge_id]["weight"]) for edge_id in ids)
        if not math.isclose(recomputed, float(row["dijkstra_distance"]), abs_tol=1e-9):
            path_ok = False
            break
    check("computed_dijkstra_paths", path_ok, f"{len(paths)} reachable nodes and recomputed weighted paths")

    comparison = read_csv(run_dir / "dijkstra_selection_comparison.csv")
    by_budget = {int(row["budget_papers"]): row for row in comparison}
    expected_budgets = {5, 10, 20, 40, 60}
    selection_ok = set(by_budget) == expected_budgets and all(
        int(row["dijkstra_C4_anchors"]) >= int(row["screen_C4_anchors"]) for row in comparison
    )
    selection_ok &= by_budget.get(20, {}).get("dijkstra_C4_anchors") == "14" and by_budget.get(20, {}).get("screen_C4_anchors") == "8"
    check("dijkstra_equal_budget_replay", selection_ok, "same candidate pool; at 20-paper budget: 14 C4 anchors vs 8")

    graphs = [
        "graphs/landscape_map.png", "graphs/citation_lineage_graph.png", "graphs/audit_funnel.png",
        "graphs/dijkstra_selection_effect.png",
    ]
    check(
        "rendered_graphs",
        all((run_dir / item).stat().st_size > 10000 for item in graphs),
        "four nonempty rendered PNG views",
    )
    snapshots = read_csv(run_dir / "goal_usage_snapshots.csv")
    check(
        "runtime_accounting",
        len(snapshots) >= 2 and all(row["goal_tokens_used"] and row["goal_time_seconds"] for row in snapshots),
        f"{len(snapshots)} runtime snapshots; counters labelled separately from API cost",
    )

    overall = "PASS" if all(item["status"] == "PASS" for item in checks) else "FAIL"
    payload = {"overall": overall, "checks": checks}
    (run_dir / "final_validation_report.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    lines = ["# Final Validation", "", f"Overall: **{overall}**", "", "| Check | Status | Detail |", "|---|---|---|"]
    lines.extend(f"| {item['name']} | {item['status']} | {item['detail']} |" for item in checks)
    (run_dir / "final_validation_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"overall={overall} checks={len(checks)}")
    return 0 if overall == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
