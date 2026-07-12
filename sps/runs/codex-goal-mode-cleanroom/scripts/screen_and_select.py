#!/usr/bin/env python3
"""Deduplicate current query results, score relevance, and select full texts."""

from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROOT_AUTHORS = {"shiyang chen", "moxian qian", "gert aarts", "biagio lucini", "kai zhou"}
DOMAIN_STEMS = {"lattice", "field", "sampl", "flow", "diffusion", "gauge", "monte", "markov", "path", "thermodynamic", "boltzmann", "phi", "scalar", "topolog", "stochastic"}
STRONG_DOMAIN_PHRASES = {
    "lattice field", "lattice gauge", "lattice qcd", "phi 4", "scalar field",
    "gauge theory", "boltzmann distribution", "unnormalized distribution",
    "unnormalized target", "markov chain monte carlo", "path integral sampler",
    "stochastic normalizing flow",
}
ROOT_METHOD_PHRASES = {
    "path integral sampler", "denoising diffusion sampler",
    "non equilibrium transport sampler", "controlled monte carlo diffusion",
    "stochastic normalizing flow", "continuous normalizing flow",
}
METHOD_QUOTAS = {
    "path_space": 4, "stochastic_flow": 3, "flow": 4, "diffusion": 4,
    "gauge": 4, "fermion": 2, "failure": 3, "scaling": 2,
}
FACET_QUOTAS = {
    "lineage": 5, "mechanism": 3, "objective": 3, "correction": 4,
    "failure": 4, "adjacent_method": 5, "extension": 4, "evaluation": 3,
    "author": 2,
}


def norm(text: str) -> str:
    text = text.lower().replace("ϕ", "phi").replace("φ", "phi")
    return re.sub(r"[^a-z0-9]+", " ", text).strip()


def key(row: dict[str, str]) -> str:
    if row["arxiv_id"]:
        return "arxiv:" + row["arxiv_id"]
    if row["doi"]:
        return "doi:" + row["doi"].lower()
    return "title:" + norm(row["title"])


def main() -> None:
    results = list(csv.DictReader((ROOT / "route_results.csv").open(encoding="utf-8")))
    web_seed = ROOT / "web_seed_candidates.csv"
    if web_seed.exists():
        results.extend(csv.DictReader(web_seed.open(encoding="utf-8")))
    terms = list(csv.DictReader((ROOT / "keyword_ledger.csv").open(encoding="utf-8")))
    grounded_phrases = [norm(row["term"]) for row in terms if len(norm(row["term"]).split()) >= 2]
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in results:
        if norm(row["title"]):
            grouped[key(row)].append(row)

    candidates = []
    for candidate_id, rows in sorted(grouped.items()):
        best = max(rows, key=lambda row: (bool(row["abstract"]), bool(row["arxiv_id"]), -int(row["rank"] or 999)))
        combined = norm(best["title"] + " " + best["abstract"])
        title_norm = norm(best["title"])
        facets = sorted({row["facet"] for row in rows})
        families = sorted({row["family"] for row in rows})
        authors_norm = {norm(name) for name in re.split(r";| and ", best["authors"]) if norm(name)}
        phrase_hits = [phrase for phrase in grounded_phrases if phrase in combined]
        domain_hits = sorted({stem for stem in DOMAIN_STEMS if any(token.startswith(stem) for token in combined.split())})
        strong_domain_hits = sorted({phrase for phrase in STRONG_DOMAIN_PHRASES if phrase in combined})
        root_method_hits = sorted({phrase for phrase in ROOT_METHOD_PHRASES if phrase in combined})
        score = min(8, len(phrase_hits))
        score += min(5, len(domain_hits))
        if "backward" in families:
            score += 5
        if authors_norm & ROOT_AUTHORS:
            score += 4
        if any(family in families for family in ["author", "adjacent", "adversarial", "extension", "closure"]):
            score += 2
        if best["arxiv_id"]:
            score += 2
        if best["arxiv_id"] == "2606.13790":
            score += 100
        if "backward" in families and root_method_hits:
            score += 3
        if not any(stem in domain_hits for stem in ["lattice", "field", "sampl", "flow", "diffusion", "gauge", "path"]):
            score -= 6
        if not strong_domain_hits and "backward" not in families and not (authors_norm & ROOT_AUTHORS):
            score -= 8
        decision = "include" if score >= 9 else "monitor" if score >= 6 else "exclude"
        groups = []
        if any(phrase in combined for phrase in ["path integral sampler", "denoising diffusion sampler", "transport sampler", "stochastic control", "controlled monte carlo diffusion"]): groups.append("path_space")
        if "stochastic normalizing flow" in combined: groups.append("stochastic_flow")
        if "flow" in combined or "normalizing flow" in combined: groups.append("flow")
        if "diffusion" in combined or "score based" in combined: groups.append("diffusion")
        if "gauge" in combined or "topolog" in combined: groups.append("gauge")
        if any(term in combined for term in ["fermion", "schwinger", "qcd", "pseudofermion"]): groups.append("fermion")
        if any(term in combined for term in ["mode collapse", "topological freezing", "critical slowing"]): groups.append("failure")
        if any(term in combined for term in ["scaling", "scalable", "larger lattice", "volume transfer"]): groups.append("scaling")
        reason = f"score={score}; phrase_hits={len(phrase_hits)}; strong_domain={';'.join(strong_domain_hits)}; root_methods={';'.join(root_method_hits)}; domain={';'.join(domain_hits[:8])}; routes={';'.join(families)}"
        candidates.append({
            "candidate_id": candidate_id, "title": best["title"], "authors": best["authors"],
            "year": best["year"], "doi": best["doi"], "arxiv_id": best["arxiv_id"],
            "primary_url": best["primary_url"], "facets": ";".join(facets),
            "families": ";".join(families), "method_groups": ";".join(sorted(set(groups))), "query_ids": ";".join(sorted({r["query_id"] for r in rows})),
            "route_occurrences": len(rows), "score": score, "decision": decision,
            "screen_reason": reason, "provenance": ";".join(sorted({r["provenance"] for r in rows})),
        })
    candidates.sort(key=lambda row: (-int(row["score"]), -int(row["route_occurrences"]), row["title"]))
    with (ROOT / "candidate_screening_table.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(candidates[0])); writer.writeheader(); writer.writerows(candidates)

    eligible = [row for row in candidates if row["decision"] == "include" and row["arxiv_id"]]
    selected: list[dict[str, str]] = []
    selected_ids: set[str] = set()
    def choose(row: dict[str, str], reason: str) -> None:
        if row["arxiv_id"] in selected_ids:
            return
        selected_ids.add(row["arxiv_id"])
        selected.append({**row, "selection_reason": reason, "pdf_url": f"https://arxiv.org/pdf/{row['arxiv_id']}"})

    root_rows = [row for row in eligible if row["arxiv_id"] == "2606.13790"]
    if not root_rows:
        raise SystemExit("Root paper missing from current candidate pool")
    choose(root_rows[0], "root")
    for group, quota in METHOD_QUOTAS.items():
        group_rows = [row for row in eligible if group in row["method_groups"].split(";")]
        for row in group_rows[:quota]:
            choose(row, f"method_quota:{group}")
    for facet, quota in FACET_QUOTAS.items():
        facet_rows = [row for row in eligible if facet in row["facets"].split(";")]
        for row in facet_rows[:quota]:
            choose(row, f"facet_quota:{facet}")
    for row in eligible:
        if len(selected) >= 30:
            break
        choose(row, "global_score_fill")
    if len(selected) < 24:
        raise SystemExit(f"Only {len(selected)} eligible arXiv full texts; required 24")
    fields = list(selected[0])
    with (ROOT / "selected_fulltexts.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields); writer.writeheader(); writer.writerows(selected)
    print(f"raw={len(results)} deduplicated={len(candidates)} include={sum(r['decision']=='include' for r in candidates)} monitor={sum(r['decision']=='monitor' for r in candidates)} selected={len(selected)}")


if __name__ == "__main__":
    main()
