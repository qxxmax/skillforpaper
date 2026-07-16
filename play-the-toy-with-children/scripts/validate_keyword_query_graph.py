#!/usr/bin/env python3
"""Validate provenance and relation contracts for literature-search artifacts."""

from __future__ import annotations

import argparse
import csv
import json
import re
import tempfile
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

COMPACT_KEYWORD_FIELDS = {
    "term_id", "term", "normalized_term", "facet", "source", "page",
    "anchor_quote", "status",
}
COMPACT_QUERY_FIELDS = {
    "query_id", "family", "source", "query", "facet", "parent_evidence",
}
COMPACT_RELATION_FIELDS = {
    "edge_id", "source_arxiv_id", "target_arxiv_id", "relation_type",
    "relation_basis", "evidence_id", "confidence", "review_status",
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


def load_csv(
    path: Path,
    profiles: dict[str, set[str]],
    label: str,
) -> tuple[list[dict[str, str]], list[str], str | None]:
    errors: list[str] = []
    if not path.exists():
        return [], [f"{label}: missing file {path}"], None
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fields = set(reader.fieldnames or [])
        rows = list(reader)
    profile = next(
        (name for name, required in profiles.items() if required <= fields),
        None,
    )
    if profile is None:
        summaries = "; ".join(
            f"{name} missing {sorted(required - fields)}"
            for name, required in profiles.items()
        )
        errors.append(f"{label}: no supported schema ({summaries})")
    return rows, errors, profile


def split_ids(value: str) -> list[str]:
    return [item.strip() for item in re.split(r"[;,|]", value) if item.strip()]


def validate_files(
    keyword_path: Path,
    query_path: Path,
    relation_path: Path,
) -> dict[str, object]:
    keywords, errors, keyword_profile = load_csv(
        keyword_path,
        {"canonical": KEYWORD_FIELDS, "compact_v1": COMPACT_KEYWORD_FIELDS},
        "keyword ledger",
    )
    queries, query_errors, query_profile = load_csv(
        query_path,
        {"canonical": QUERY_FIELDS, "compact_v1": COMPACT_QUERY_FIELDS},
        "query matrix",
    )
    relations, relation_errors, relation_profile = load_csv(
        relation_path,
        {"canonical": RELATION_FIELDS, "compact_v1": COMPACT_RELATION_FIELDS},
        "relation ledger",
    )
    errors.extend(query_errors)
    errors.extend(relation_errors)
    warnings: list[str] = []

    if keyword_profile == "canonical":
        term_ids = {
            row.get("TermID", "").strip()
            for row in keywords
            if row.get("TermID", "").strip()
        }
        if len(term_ids) != len(
            [row for row in keywords if row.get("TermID", "").strip()]
        ):
            errors.append("keyword ledger: duplicate TermID")
        for index, row in enumerate(keywords, start=2):
            axis_values = set(split_ids(row.get("Axis", "")))
            if not axis_values:
                errors.append(f"keyword row {index}: missing Axis")
            unknown_axes = axis_values - ALLOWED_AXES
            if unknown_axes:
                errors.append(
                    f"keyword row {index}: unknown axes {sorted(unknown_axes)}"
                )
            if not row.get("CanonicalTerm", "").strip():
                errors.append(f"keyword row {index}: missing CanonicalTerm")
            provenance = row.get("ProvenanceType", "").strip()
            if (
                provenance != "hypothesis_term"
                and not row.get("SourceAnchor", "").strip()
            ):
                errors.append(f"keyword row {index}: sourced term lacks SourceAnchor")
            if (
                provenance == "hypothesis_term"
                and row.get("Status", "").strip() not in {"candidate", "hold"}
            ):
                errors.append(
                    f"keyword row {index}: hypothesis term must remain candidate/hold"
                )
    elif keyword_profile == "compact_v1":
        term_ids = {
            row.get("term_id", "").strip()
            for row in keywords
            if row.get("term_id", "").strip()
        }
        if len(term_ids) != len(
            [row for row in keywords if row.get("term_id", "").strip()]
        ):
            errors.append("keyword ledger: duplicate term_id")
        for index, row in enumerate(keywords, start=2):
            for field in ("term_id", "normalized_term", "facet", "source", "status"):
                if not row.get(field, "").strip():
                    errors.append(f"keyword row {index}: missing {field}")
            if not row.get("anchor_quote", "").strip():
                errors.append(f"keyword row {index}: missing anchor_quote")
    else:
        term_ids = set()

    if query_profile == "canonical":
        query_ids: set[str] = set()
        for index, row in enumerate(queries, start=2):
            query_id = row.get("QueryID", "").strip()
            if not query_id:
                errors.append(f"query row {index}: missing QueryID")
            elif query_id in query_ids:
                errors.append(f"query row {index}: duplicate QueryID {query_id}")
            query_ids.add(query_id)
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
                errors.append(
                    f"query row {index}: unknown SourceTermIDs {sorted(unknown_terms)}"
                )
    elif query_profile == "compact_v1":
        query_ids: set[str] = set()
        for index, row in enumerate(queries, start=2):
            query_id = row.get("query_id", "").strip()
            if not query_id:
                errors.append(f"query row {index}: missing query_id")
            elif query_id in query_ids:
                errors.append(f"query row {index}: duplicate query_id {query_id}")
            query_ids.add(query_id)
            for field in ("family", "source", "query", "facet", "parent_evidence"):
                if not row.get(field, "").strip():
                    errors.append(f"query row {index}: missing {field}")
            compact = re.sub(r"[^A-Za-z0-9]", "", row.get("query", ""))
            if compact.isupper() and len(compact) <= 10:
                errors.append(f"query row {index}: acronym-only query is forbidden")

    edge_ids: set[str] = set()
    if relation_profile == "canonical":
        for index, row in enumerate(relations, start=2):
            edge_id = row.get("EdgeID", "").strip()
            if not edge_id:
                errors.append(f"relation row {index}: missing EdgeID")
            elif edge_id in edge_ids:
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
                errors.append(
                    f"relation row {index}: direct_citation requires DirectlyCited=yes"
                )
            if (
                direct == "yes"
                and edge_type != "direct_citation"
                and row.get("PublicGraphStatus", "").strip() == "show"
            ):
                warnings.append(
                    f"relation row {index}: DirectlyCited=yes with EdgeType={edge_type}"
                )
            if (
                row.get("PublicGraphStatus", "").strip() == "show"
                and row.get("HumanReviewStatus", "").strip() != "reviewed"
            ):
                errors.append(
                    f"relation row {index}: public edge must be human reviewed"
                )
    elif relation_profile == "compact_v1":
        arxiv_pattern = re.compile(r"^\d{4}\.\d{5}$")
        for index, row in enumerate(relations, start=2):
            edge_id = row.get("edge_id", "").strip()
            if not edge_id:
                errors.append(f"relation row {index}: missing edge_id")
            elif edge_id in edge_ids:
                errors.append(f"relation row {index}: duplicate edge_id {edge_id}")
            edge_ids.add(edge_id)
            edge_type = row.get("relation_type", "").strip()
            if edge_type not in ALLOWED_EDGES:
                errors.append(
                    f"relation row {index}: unknown relation_type {edge_type!r}"
                )
            for field in (
                "source_arxiv_id", "target_arxiv_id", "relation_basis",
                "evidence_id", "confidence", "review_status",
            ):
                if not row.get(field, "").strip():
                    errors.append(f"relation row {index}: missing {field}")
            for field in ("source_arxiv_id", "target_arxiv_id"):
                value = row.get(field, "").strip()
                if value and not arxiv_pattern.fullmatch(value):
                    errors.append(
                        f"relation row {index}: invalid {field} {value!r}"
                    )
            if (
                edge_type == "direct_citation"
                and "verified" not in row.get("review_status", "").lower()
            ):
                errors.append(
                    f"relation row {index}: direct citation lacks verified review_status"
                )

    return {
        "status": "PASS" if not errors else "FAIL",
        "counts": {"keywords": len(keywords), "queries": len(queries), "relations": len(relations)},
        "schemas": {
            "keyword_ledger": keyword_profile,
            "query_matrix": query_profile,
            "relation_ledger": relation_profile,
        },
        "errors": errors,
        "warnings": warnings,
    }


def write_one_row(path: Path, fields: set[str], row: dict[str, str]) -> None:
    ordered = sorted(fields)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=ordered)
        writer.writeheader()
        writer.writerow(row)


def self_test() -> None:
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        canonical_keyword = root / "canonical_keyword.csv"
        canonical_query = root / "canonical_query.csv"
        canonical_relation = root / "canonical_relation.csv"
        write_one_row(
            canonical_keyword,
            KEYWORD_FIELDS,
            {
                "TermID": "T001", "CanonicalTerm": "path sampler",
                "OriginalPhrase": "path sampler", "Axis": "method",
                "SourcePaperID": "P001", "SourceSection": "Sec. 2",
                "SourceAnchor": "p. 5, Eq. (2.2)",
                "ProvenanceType": "source_anchor", "Confidence": "high",
                "Status": "seed",
            },
        )
        write_one_row(
            canonical_query,
            QUERY_FIELDS,
            {
                "QueryID": "Q001", "Round": "R0", "RouteFamily": "lexical",
                "AxisCombination": "problem_x_method",
                "QueryString": "stochastic path sampler",
                "DomainLock": "lattice field theory", "SourceTermIDs": "T001",
                "TargetSource": "arXiv", "ExpectedFacet": "method",
                "Status": "complete",
            },
        )
        write_one_row(
            canonical_relation,
            RELATION_FIELDS,
            {
                "EdgeID": "R001", "SourceID": "P000", "TargetID": "P001",
                "EdgeType": "direct_citation", "DirectlyCited": "yes",
                "EvidenceID": "E0001", "RelationBasis": "p. 2 reference list",
                "Confidence": "high", "HumanReviewStatus": "reviewed",
                "PublicGraphStatus": "show",
            },
        )

        compact_keyword = root / "compact_keyword.csv"
        compact_query = root / "compact_query.csv"
        compact_relation = root / "compact_relation.csv"
        write_one_row(
            compact_keyword,
            COMPACT_KEYWORD_FIELDS,
            {
                "term_id": "K01", "term": "path sampler",
                "normalized_term": "path sampler", "facet": "method",
                "source": "root_pdf", "page": "1",
                "anchor_quote": "source text", "status": "root_grounded",
            },
        )
        write_one_row(
            compact_query,
            COMPACT_QUERY_FIELDS,
            {
                "query_id": "Q01", "family": "root", "source": "arXiv",
                "query": "stochastic path sampler", "facet": "identity",
                "parent_evidence": "root title",
            },
        )
        write_one_row(
            compact_relation,
            COMPACT_RELATION_FIELDS,
            {
                "edge_id": "R0001", "source_arxiv_id": "2111.15141",
                "target_arxiv_id": "2606.13790",
                "relation_type": "direct_citation",
                "relation_basis": "exact identifier in reference list",
                "evidence_id": "CIT-260613790-211115141",
                "confidence": "high",
                "review_status": "exact_identifier_context_verified",
            },
        )

        canonical = validate_files(
            canonical_keyword, canonical_query, canonical_relation
        )
        compact = validate_files(compact_keyword, compact_query, compact_relation)
        invalid = validate_files(compact_keyword, compact_query, root / "missing.csv")
    if (
        canonical["status"] != "PASS"
        or compact["status"] != "PASS"
        or invalid["status"] != "FAIL"
    ):
        raise SystemExit(
            f"self-test failed: canonical={canonical}, compact={compact}, invalid={invalid}"
        )
    print("PASS: keyword/query/graph validator self-test")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--keyword-ledger", type=Path)
    parser.add_argument("--query-matrix", type=Path)
    parser.add_argument("--relation-ledger", type=Path)
    parser.add_argument("--json-output", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return 0
    if not args.keyword_ledger or not args.query_matrix or not args.relation_ledger:
        parser.error(
            "--keyword-ledger, --query-matrix, and --relation-ledger are required"
        )

    result = validate_files(
        args.keyword_ledger,
        args.query_matrix,
        args.relation_ledger,
    )
    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 1 if result["status"] == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())
