#!/usr/bin/env python3
"""Validate provenance and relation contracts for literature-search artifacts."""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path


KEYWORD_FIELDS = {
    "TermID", "CanonicalTerm", "OriginalPhrase", "Axis", "Synonyms",
    "Acronyms", "BroaderTerm", "NeighborTerms", "NegativeMeanings",
    "SourcePaperID", "SourceSection", "SourceAnchor", "ProvenanceType",
    "Confidence", "Status",
}
QUERY_FIELDS = {
    "QueryID", "Round", "RouteFamily", "AxisCombination", "QueryString",
    "DomainLock", "NegativeTerms", "SourceTermIDs", "TargetSource",
    "ExpectedFacet", "Status",
}
RELATION_FIELDS = {
    "EdgeID", "SourceID", "TargetID", "EdgeType", "DirectlyCited",
    "EvidenceID", "RelationBasis", "Confidence", "HumanReviewStatus",
    "PublicGraphStatus",
}

ALLOWED_AXES = {
    "problem", "method", "learned_object", "correction_validation",
    "domain_benchmark", "limitation_direction",
}
ALLOWED_EDGES = {
    "direct_citation", "forward_citation", "method_precedent",
    "method_extension", "baseline_comparison", "same_author_context",
    "shared_benchmark", "conceptual_neighbor",
    "external_historical_relation",
}
DOMAIN_LOCK_OPTIONAL = {"identifier", "author", "venue", "backward_citation", "forward_citation"}


def load_csv(path: Path, required: set[str], label: str) -> tuple[list[dict[str, str]], list[str]]:
    errors: list[str] = []
    if not path.exists():
        return [], [f"{label}: missing file {path}"]
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fields = set(reader.fieldnames or [])
        missing = sorted(required - fields)
        if missing:
            errors.append(f"{label}: missing columns {missing}")
        rows = list(reader)
    return rows, errors


def split_ids(value: str) -> list[str]:
    return [item.strip() for item in re.split(r"[;,|]", value) if item.strip()]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--keyword-ledger", type=Path, required=True)
    parser.add_argument("--query-matrix", type=Path, required=True)
    parser.add_argument("--relation-ledger", type=Path, required=True)
    parser.add_argument("--json-output", type=Path)
    args = parser.parse_args()

    keywords, errors = load_csv(args.keyword_ledger, KEYWORD_FIELDS, "keyword ledger")
    queries, query_errors = load_csv(args.query_matrix, QUERY_FIELDS, "query matrix")
    relations, relation_errors = load_csv(args.relation_ledger, RELATION_FIELDS, "relation ledger")
    errors.extend(query_errors)
    errors.extend(relation_errors)
    warnings: list[str] = []

    term_ids = {row.get("TermID", "").strip() for row in keywords if row.get("TermID", "").strip()}
    if len(term_ids) != len([row for row in keywords if row.get("TermID", "").strip()]):
        errors.append("keyword ledger: duplicate TermID")

    for index, row in enumerate(keywords, start=2):
        axis_values = set(split_ids(row.get("Axis", "")))
        if not axis_values:
            errors.append(f"keyword row {index}: missing Axis")
        unknown_axes = axis_values - ALLOWED_AXES
        if unknown_axes:
            errors.append(f"keyword row {index}: unknown axes {sorted(unknown_axes)}")
        if not row.get("CanonicalTerm", "").strip():
            errors.append(f"keyword row {index}: missing CanonicalTerm")
        provenance = row.get("ProvenanceType", "").strip()
        if provenance != "hypothesis_term" and not row.get("SourceAnchor", "").strip():
            errors.append(f"keyword row {index}: sourced term lacks SourceAnchor")
        if provenance == "hypothesis_term" and row.get("Status", "").strip() not in {"candidate", "hold"}:
            errors.append(f"keyword row {index}: hypothesis term must remain candidate/hold")

    for index, row in enumerate(queries, start=2):
        query = row.get("QueryString", "").strip()
        route = row.get("RouteFamily", "").strip()
        if not query:
            errors.append(f"query row {index}: missing QueryString")
        compact = re.sub(r"[^A-Za-z0-9]", "", query)
        if compact.isupper() and len(compact) <= 10:
            errors.append(f"query row {index}: acronym-only query is forbidden")
        if route not in DOMAIN_LOCK_OPTIONAL and not row.get("DomainLock", "").strip():
            errors.append(f"query row {index}: route {route!r} requires DomainLock")
        unknown_terms = set(split_ids(row.get("SourceTermIDs", ""))) - term_ids
        if unknown_terms:
            errors.append(f"query row {index}: unknown SourceTermIDs {sorted(unknown_terms)}")

    edge_ids: set[str] = set()
    for index, row in enumerate(relations, start=2):
        edge_id = row.get("EdgeID", "").strip()
        if edge_id in edge_ids:
            errors.append(f"relation row {index}: duplicate EdgeID {edge_id}")
        edge_ids.add(edge_id)
        edge_type = row.get("EdgeType", "").strip()
        if edge_type not in ALLOWED_EDGES:
            errors.append(f"relation row {index}: unknown EdgeType {edge_type!r}")
        if not row.get("EvidenceID", "").strip():
            errors.append(f"relation row {index}: missing EvidenceID")
        if not row.get("RelationBasis", "").strip():
            errors.append(f"relation row {index}: missing RelationBasis")
        direct = row.get("DirectlyCited", "").strip().lower()
        if edge_type == "direct_citation" and direct != "yes":
            errors.append(f"relation row {index}: direct_citation requires DirectlyCited=yes")
        if (
            direct == "yes"
            and edge_type != "direct_citation"
            and row.get("PublicGraphStatus", "").strip() == "show"
        ):
            warnings.append(f"relation row {index}: DirectlyCited=yes with EdgeType={edge_type}")
        if row.get("PublicGraphStatus", "").strip() == "show" and row.get("HumanReviewStatus", "").strip() != "reviewed":
            errors.append(f"relation row {index}: public edge must be human reviewed")

    result = {
        "status": "PASS" if not errors else "FAIL",
        "counts": {"keywords": len(keywords), "queries": len(queries), "relations": len(relations)},
        "errors": errors,
        "warnings": warnings,
    }
    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
