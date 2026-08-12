#!/usr/bin/env python3
"""Run optional literature-retrieval backends and preserve an audit trail.

The runner deliberately stops at metadata candidates. Scientific claims still
require the skill's source-verification and native-reading gates.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


USER_AGENT = "play-the-toy-with-children/1.0 literature-retrieval"
S2_GRAPH = "https://api.semanticscholar.org/graph/v1"
OPENALEX = "https://api.openalex.org"
CROSSREF = "https://api.crossref.org"

CSV_FIELDS = [
    "PaperID", "Title", "Authors", "Year", "Venue", "DOI", "ArxivID",
    "PMID", "PMCID", "OpenAlexID", "SemanticScholarID", "URL", "PDFURL",
    "IsOpenAccess", "CitationCount", "SourceFamilies", "RouteFamilies",
    "QueryIDs", "RoundIDs", "RetrievalTimestamps", "ProvenanceFiles",
    "Status", "Verification", "EvidenceLevel", "Abstract", "Notes",
]

EDGE_FIELDS = [
    "EdgeCandidateID", "SeedIdentifier", "RelatedPaperID",
    "RelatedIdentifier", "Direction", "Backend", "RouteID", "RoundID",
    "ContextAvailable", "ContextLead", "Intent", "IsInfluential",
    "VerificationStatus", "PublicGraphStatus", "EvidenceID", "Notes",
]


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def clean_text(value: Any) -> str:
    if value is None:
        return ""
    return " ".join(str(value).split())


def normalize_doi(value: Any) -> str:
    doi = clean_text(value).lower()
    doi = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", doi)
    doi = re.sub(r"^doi:\s*", "", doi)
    return doi.rstrip(". ")


def normalize_arxiv(value: Any) -> str:
    text = clean_text(value)
    text = re.sub(r"^arxiv:\s*", "", text, flags=re.I)
    match = re.search(r"arxiv\.org/(?:abs|pdf)/([^/?#]+)", text, flags=re.I)
    if match:
        text = match.group(1)
    return re.sub(r"v\d+$", "", text, flags=re.I)


def normalize_title(value: Any) -> str:
    return re.sub(r"[^a-z0-9]+", " ", clean_text(value).lower()).strip()


def author_names(value: Any) -> list[str]:
    if not value:
        return []
    if isinstance(value, str):
        return [clean_text(item) for item in re.split(r"\s*;\s*", value) if clean_text(item)]
    names: list[str] = []
    for item in value if isinstance(value, list) else [value]:
        if isinstance(item, str):
            name = clean_text(item)
        elif isinstance(item, dict):
            author = item.get("author") if isinstance(item.get("author"), dict) else item
            name = clean_text(
                author.get("name")
                or author.get("display_name")
                or " ".join(
                    part for part in [author.get("given", ""), author.get("family", "")] if part
                )
            )
        else:
            name = clean_text(item)
        if name and name not in names:
            names.append(name)
    return names


def first_year(value: Any) -> str:
    if isinstance(value, int):
        return str(value)
    text = clean_text(value)
    match = re.search(r"(?:19|20)\d{2}", text)
    return match.group(0) if match else ""


def first_list_value(value: Any) -> Any:
    if isinstance(value, list):
        return value[0] if value else ""
    return value


def inverted_abstract(index: Any) -> str:
    if not isinstance(index, dict):
        return ""
    positions: dict[int, str] = {}
    for word, locs in index.items():
        if isinstance(locs, list):
            for loc in locs:
                if isinstance(loc, int):
                    positions[loc] = str(word)
    return " ".join(positions[pos] for pos in sorted(positions))


def short_context(value: Any, max_words: int = 20) -> str:
    if isinstance(value, list):
        value = value[0] if value else ""
    words = clean_text(value).split()
    return " ".join(words[:max_words]) + (" ..." if len(words) > max_words else "")


def join_unique(values: Iterable[str]) -> str:
    return "; ".join(sorted({clean_text(v) for v in values if clean_text(v)}))


@dataclass
class Record:
    title: str
    authors: list[str] = field(default_factory=list)
    year: str = ""
    venue: str = ""
    doi: str = ""
    arxiv_id: str = ""
    pmid: str = ""
    pmcid: str = ""
    openalex_id: str = ""
    semantic_id: str = ""
    url: str = ""
    pdf_url: str = ""
    abstract: str = ""
    is_open_access: str = ""
    citation_count: str = ""
    source_families: set[str] = field(default_factory=set)
    route_families: set[str] = field(default_factory=set)
    query_ids: set[str] = field(default_factory=set)
    round_ids: set[str] = field(default_factory=set)
    timestamps: set[str] = field(default_factory=set)
    provenance_files: set[str] = field(default_factory=set)
    source_record_ids: set[str] = field(default_factory=set)
    notes: set[str] = field(default_factory=set)
    merged_count: int = 1
    paper_id: str = ""

    def identity_keys(self) -> list[str]:
        keys = []
        for prefix, value in (
            ("doi", self.doi), ("arxiv", self.arxiv_id), ("pmid", self.pmid),
            ("pmcid", self.pmcid), ("openalex", self.openalex_id),
            ("s2", self.semantic_id),
        ):
            if value:
                keys.append(f"{prefix}:{value.lower()}")
        return keys

    def title_key(self) -> str:
        first_author = normalize_title(self.authors[0]) if self.authors else ""
        return f"{normalize_title(self.title)}|{first_author}|{self.year}"

    def to_row(self) -> dict[str, Any]:
        return {
            "PaperID": self.paper_id,
            "Title": self.title,
            "Authors": "; ".join(self.authors),
            "Year": self.year,
            "Venue": self.venue,
            "DOI": self.doi,
            "ArxivID": self.arxiv_id,
            "PMID": self.pmid,
            "PMCID": self.pmcid,
            "OpenAlexID": self.openalex_id,
            "SemanticScholarID": self.semantic_id,
            "URL": self.url,
            "PDFURL": self.pdf_url,
            "IsOpenAccess": self.is_open_access,
            "CitationCount": self.citation_count,
            "SourceFamilies": join_unique(self.source_families),
            "RouteFamilies": join_unique(self.route_families),
            "QueryIDs": join_unique(self.query_ids),
            "RoundIDs": join_unique(self.round_ids),
            "RetrievalTimestamps": join_unique(self.timestamps),
            "ProvenanceFiles": join_unique(self.provenance_files),
            "Status": "candidate",
            "Verification": "C0",
            "EvidenceLevel": "metadata_only",
            "Abstract": self.abstract,
            "Notes": join_unique(self.notes),
        }


def merge_record(target: Record, incoming: Record) -> None:
    for name in (
        "year", "venue", "doi", "arxiv_id", "pmid", "pmcid",
        "openalex_id", "semantic_id", "url", "pdf_url", "is_open_access",
    ):
        if not getattr(target, name) and getattr(incoming, name):
            setattr(target, name, getattr(incoming, name))
    if len(incoming.title) > len(target.title):
        target.title = incoming.title
    if len(incoming.abstract) > len(target.abstract):
        target.abstract = incoming.abstract
    for author in incoming.authors:
        if author not in target.authors:
            target.authors.append(author)
    try:
        if int(incoming.citation_count or 0) > int(target.citation_count or 0):
            target.citation_count = incoming.citation_count
    except ValueError:
        pass
    for name in (
        "source_families", "route_families", "query_ids", "round_ids",
        "timestamps", "provenance_files", "source_record_ids", "notes",
    ):
        getattr(target, name).update(getattr(incoming, name))
    target.merged_count += incoming.merged_count


def record_from_item(
    item: dict[str, Any], backend: str, route_id: str, query_id: str,
    round_id: str, timestamp: str, provenance: str,
) -> Record | None:
    external = item.get("externalIds") or item.get("external_ids") or {}
    if not isinstance(external, dict):
        external = {}

    title = clean_text(first_list_value(item.get("title") or item.get("display_name")))
    if not title:
        return None

    source = clean_text(item.get("source") or backend)
    paper_id = clean_text(item.get("paper_id") or item.get("paperId") or item.get("id"))
    doi = normalize_doi(item.get("doi") or item.get("DOI") or external.get("DOI"))
    arxiv_id = normalize_arxiv(
        item.get("arxiv_id") or external.get("ArXiv") or external.get("ARXIV") or ""
    )
    if not arxiv_id and source.lower() == "arxiv":
        arxiv_id = normalize_arxiv(paper_id)
    if not arxiv_id:
        arxiv_id = normalize_arxiv(item.get("url") or "") if "arxiv.org" in clean_text(item.get("url")) else ""

    authors_value = item.get("authors") or item.get("authorships") or item.get("author")
    year = first_year(item.get("year") or item.get("publication_year") or item.get("published_date"))
    if not year:
        date_parts = item.get("published", {}).get("date-parts", []) if isinstance(item.get("published"), dict) else []
        if date_parts and date_parts[0]:
            year = first_year(date_parts[0][0])

    primary = item.get("primary_location") if isinstance(item.get("primary_location"), dict) else {}
    primary_source = primary.get("source") if isinstance(primary.get("source"), dict) else {}
    best_oa = item.get("best_oa_location") if isinstance(item.get("best_oa_location"), dict) else {}
    oa = item.get("open_access") if isinstance(item.get("open_access"), dict) else {}
    open_pdf = item.get("openAccessPdf") if isinstance(item.get("openAccessPdf"), dict) else {}
    links = item.get("link") if isinstance(item.get("link"), list) else []

    venue = clean_text(
        item.get("venue")
        or first_list_value(item.get("container-title"))
        or primary_source.get("display_name")
    )
    pdf_url = clean_text(
        item.get("pdf_url")
        or item.get("open_access_url")
        or open_pdf.get("url")
        or best_oa.get("pdf_url")
        or next((link.get("URL") for link in links if isinstance(link, dict) and link.get("URL")), "")
    )
    url = clean_text(item.get("url") or item.get("URL") or item.get("id"))
    abstract = clean_text(item.get("abstract")) or inverted_abstract(item.get("abstract_inverted_index"))
    is_oa_value = item.get("isOpenAccess")
    if is_oa_value is None:
        is_oa_value = oa.get("is_oa")
    if is_oa_value is None and pdf_url:
        is_oa_value = True

    openalex_id = clean_text(item.get("openalex_id"))
    if not openalex_id and "openalex.org/W" in clean_text(item.get("id")):
        openalex_id = clean_text(item.get("id")).rsplit("/", 1)[-1]
    semantic_id = clean_text(item.get("semantic_scholar_id") or item.get("paperId"))
    if backend == "semantic-scholar" and not semantic_id:
        semantic_id = paper_id

    citation_value = item.get("citationCount")
    if citation_value is None:
        citation_value = item.get("cited_by_count")
    if citation_value is None:
        citation_value = item.get("citations")

    record = Record(
        title=title,
        authors=author_names(authors_value),
        year=year,
        venue=venue,
        doi=doi,
        arxiv_id=arxiv_id,
        pmid=clean_text(item.get("pmid") or external.get("PubMed") or external.get("PMID")),
        pmcid=clean_text(item.get("pmcid") or external.get("PubMedCentral") or external.get("PMCID")),
        openalex_id=openalex_id,
        semantic_id=semantic_id,
        url=url,
        pdf_url=pdf_url,
        abstract=abstract,
        is_open_access="yes" if is_oa_value is True else "no" if is_oa_value is False else "unknown",
        citation_count=clean_text(citation_value),
    )
    record.source_families.add(source or backend)
    record.route_families.add(route_id)
    if query_id:
        record.query_ids.add(query_id)
    if round_id:
        record.round_ids.add(round_id)
    record.timestamps.add(timestamp)
    record.provenance_files.add(provenance)
    source_record_id = openalex_id if backend == "openalex" and openalex_id else paper_id
    if source_record_id:
        record.source_record_ids.add(f"{backend}:{source_record_id}")
    return record


def extract_items(payload: Any, backend: str) -> list[dict[str, Any]]:
    if isinstance(payload, list):
        return [item for item in payload if isinstance(item, dict)]
    if not isinstance(payload, dict):
        return []
    for key in ("papers", "related_papers", "recommendedPapers", "results", "data"):
        value = payload.get(key)
        if isinstance(value, list):
            return [item for item in value if isinstance(item, dict)]
    message = payload.get("message")
    if isinstance(message, dict) and isinstance(message.get("items"), list):
        return [item for item in message["items"] if isinstance(item, dict)]
    if backend == "openalex" and payload.get("title"):
        return [payload]
    return []


def deduplicate(records: list[Record]) -> tuple[list[Record], list[dict[str, str]]]:
    canonical: list[Record] = []
    key_to_index: dict[str, int] = {}
    exact_groups: list[dict[str, str]] = []

    for record in records:
        keys = record.identity_keys()
        title_key = record.title_key()
        match_index = next((key_to_index[key] for key in keys if key in key_to_index), None)
        if match_index is None and not keys and title_key in key_to_index:
            match_index = key_to_index[title_key]
        if match_index is None:
            match_index = len(canonical)
            canonical.append(record)
        else:
            merge_record(canonical[match_index], record)
        for key in keys:
            key_to_index[key] = match_index
        if not keys:
            key_to_index[title_key] = match_index

    for index, record in enumerate(canonical, start=1):
        record.paper_id = f"P{index:05d}"
        if record.merged_count > 1:
            exact_groups.append({
                "GroupID": f"DEDUP{len(exact_groups) + 1:04d}",
                "GroupType": "exact_identity_merge",
                "CanonicalPaperID": record.paper_id,
                "MemberCount": str(record.merged_count),
                "Sources": join_unique(record.source_families),
                "Identifiers": join_unique(record.identity_keys()),
                "Decision": "merged",
                "Reason": "shared stable identifier or compatible title-author-year without conflicting identifiers",
            })

    by_title: dict[str, list[Record]] = {}
    for record in canonical:
        by_title.setdefault(normalize_title(record.title), []).append(record)
    for same_title in by_title.values():
        if len(same_title) < 2:
            continue
        identifiers = {tuple(record.identity_keys()) for record in same_title}
        if len(identifiers) < 2:
            continue
        exact_groups.append({
            "GroupID": f"MANIFEST{len(exact_groups) + 1:04d}",
            "GroupType": "possible_manifestation",
            "CanonicalPaperID": join_unique(record.paper_id for record in same_title),
            "MemberCount": str(len(same_title)),
            "Sources": join_unique(source for record in same_title for source in record.source_families),
            "Identifiers": join_unique(key for record in same_title for key in record.identity_keys()),
            "Decision": "manual_review",
            "Reason": "matching normalized title with different stable identifiers; do not collapse preprint and publication automatically",
        })
    return canonical, exact_groups


def sanitized_url(url: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    query = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    safe_query = [(key, "REDACTED" if key.lower() in {"api_key", "key", "token"} else value) for key, value in query]
    return urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, parsed.path, urllib.parse.urlencode(safe_query), parsed.fragment))


def request_json(
    url: str, cache_dir: Path, headers: dict[str, str] | None = None,
    body: dict[str, Any] | None = None, refresh: bool = False,
) -> tuple[Any, str]:
    cache_dir.mkdir(parents=True, exist_ok=True)
    body_bytes = json.dumps(body, sort_keys=True).encode("utf-8") if body is not None else None
    digest = hashlib.sha256(url.encode("utf-8") + (body_bytes or b"")).hexdigest()
    cache_path = cache_dir / f"{digest}.json"
    if cache_path.exists() and not refresh:
        return json.loads(cache_path.read_text(encoding="utf-8")), "cache"

    request_headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    if headers:
        request_headers.update(headers)
    if body_bytes is not None:
        request_headers["Content-Type"] = "application/json"

    last_error: Exception | None = None
    for attempt in range(3):
        try:
            request = urllib.request.Request(url, data=body_bytes, headers=request_headers, method="POST" if body is not None else "GET")
            with urllib.request.urlopen(request, timeout=30) as response:
                payload = json.loads(response.read().decode("utf-8"))
            cache_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            return payload, "fresh"
        except urllib.error.HTTPError as exc:
            last_error = exc
            if exc.code not in {429, 500, 502, 503, 504}:
                break
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            last_error = exc
        if attempt < 2:
            time.sleep(2 ** attempt)
    raise RuntimeError(f"request failed for {sanitized_url(url)}: {last_error}")


def write_raw(output_dir: Path, backend: str, action: str, payload: Any, serial: int) -> Path:
    raw_dir = output_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    path = raw_dir / f"{serial:03d}_{backend}_{action}.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return path


def event_record(
    backend: str, action: str, route_id: str, query_id: str, round_id: str,
    request_value: str, status: str, hits: int, started: float,
    raw_path: str = "", error: str = "",
) -> dict[str, Any]:
    return {
        "timestamp": now_iso(),
        "backend": backend,
        "action": action,
        "route_id": route_id,
        "query_id": query_id,
        "round_id": round_id,
        "request": request_value,
        "status": status,
        "hits": hits,
        "elapsed_seconds": round(time.monotonic() - started, 3),
        "raw_path": raw_path,
        "error": error,
    }


def paper_search_query(args: argparse.Namespace) -> tuple[Any, str]:
    command = shlex.split(args.paper_search_command)
    if not command or shutil.which(command[0]) is None:
        raise RuntimeError(f"paper-search command not found: {args.paper_search_command}")
    command.extend([
        "search", args.query, "-n", str(args.limit), "-s", args.paper_search_sources,
    ])
    result = subprocess.run(command, text=True, capture_output=True, check=False, timeout=180)
    if result.returncode != 0:
        raise RuntimeError((result.stderr or result.stdout).strip())
    start = result.stdout.find("{")
    if start < 0:
        raise RuntimeError("paper-search returned no JSON object")
    return json.loads(result.stdout[start:]), "fresh"


def semantic_search(args: argparse.Namespace, cache_dir: Path) -> tuple[Any, str]:
    params = {
        "query": args.query,
        "limit": str(min(args.limit, 100)),
        "fields": "paperId,title,authors,year,publicationDate,venue,abstract,externalIds,url,citationCount,referenceCount,isOpenAccess,openAccessPdf",
    }
    if args.year_from or args.year_to:
        params["year"] = f"{args.year_from or ''}-{args.year_to or ''}".strip("-")
    headers = {}
    key = os.environ.get(args.semantic_api_key_env, "")
    if key:
        headers["x-api-key"] = key
    url = f"{S2_GRAPH}/paper/search?{urllib.parse.urlencode(params)}"
    return request_json(url, cache_dir, headers=headers, refresh=args.refresh)


def openalex_search(args: argparse.Namespace, cache_dir: Path) -> tuple[Any, str]:
    key = os.environ.get(args.openalex_api_key_env, "")
    if not key:
        raise RuntimeError(f"missing {args.openalex_api_key_env}; current OpenAlex API requires an API key")
    filters = []
    if args.year_from:
        filters.append(f"publication_year:>{args.year_from - 1}")
    if args.year_to:
        filters.append(f"publication_year:<{args.year_to + 1}")
    params = {
        "search": args.query,
        "per_page": str(min(args.limit, 100)),
        "sort": "relevance_score:desc",
        "select": "id,doi,title,authorships,publication_year,publication_date,abstract_inverted_index,cited_by_count,primary_location,best_oa_location,open_access,referenced_works",
        "api_key": key,
    }
    if filters:
        params["filter"] = ",".join(filters)
    url = f"{OPENALEX}/works?{urllib.parse.urlencode(params)}"
    return request_json(url, cache_dir, refresh=args.refresh)


def crossref_search(args: argparse.Namespace, cache_dir: Path) -> tuple[Any, str]:
    params = {
        "query.bibliographic": args.query,
        "rows": str(min(args.limit, 1000)),
        "select": "DOI,title,author,published,URL,container-title,abstract,is-referenced-by-count,type,link",
    }
    filters = []
    if args.year_from:
        filters.append(f"from-pub-date:{args.year_from}-01-01")
    if args.year_to:
        filters.append(f"until-pub-date:{args.year_to}-12-31")
    if filters:
        params["filter"] = ",".join(filters)
    if args.mailto:
        params["mailto"] = args.mailto
    url = f"{CROSSREF}/works?{urllib.parse.urlencode(params)}"
    return request_json(url, cache_dir, refresh=args.refresh)


def semantic_seed(seed: str) -> str:
    value = clean_text(seed)
    if re.match(r"^10\.\d{4,9}/", value, flags=re.I):
        return "DOI:" + value
    if re.match(r"^(?:\d{4}\.\d{4,5}|[a-z-]+/\d{7})v?\d*$", value, flags=re.I):
        return "ARXIV:" + normalize_arxiv(value)
    return value


def semantic_expand(
    args: argparse.Namespace, cache_dir: Path, direction: str,
) -> tuple[Any, str, list[dict[str, Any]]]:
    endpoint = "citations" if direction == "forward" else "references"
    seed = urllib.parse.quote(semantic_seed(args.seed), safe=":/")
    params = {
        "limit": str(min(args.limit, 1000)),
        "fields": "title,authors,year,venue,abstract,externalIds,url,citationCount,isOpenAccess,openAccessPdf,contexts,intents,isInfluential",
    }
    headers = {}
    key = os.environ.get(args.semantic_api_key_env, "")
    if key:
        headers["x-api-key"] = key
    url = f"{S2_GRAPH}/paper/{seed}/{endpoint}?{urllib.parse.urlencode(params)}"
    payload, freshness = request_json(url, cache_dir, headers=headers, refresh=args.refresh)
    paper_key = "citingPaper" if direction == "forward" else "citedPaper"
    papers = []
    edges = []
    for row in payload.get("data", []) if isinstance(payload, dict) else []:
        if not isinstance(row, dict) or not isinstance(row.get(paper_key), dict):
            continue
        paper = dict(row[paper_key])
        papers.append(paper)
        edges.append({
            "related_source_id": clean_text(paper.get("paperId")),
            "direction": direction,
            "context_available": "yes" if row.get("contexts") else "no",
            "context": short_context(row.get("contexts")),
            "intent": join_unique(row.get("intents") or []),
            "is_influential": clean_text(row.get("isInfluential")),
        })
    return {"data": papers}, freshness, edges


def resolve_openalex_seed(args: argparse.Namespace, cache_dir: Path, key: str) -> tuple[dict[str, Any], str]:
    seed = clean_text(args.seed)
    if re.fullmatch(r"W\d+", seed, flags=re.I) or "openalex.org/W" in seed:
        work_id = seed.rsplit("/", 1)[-1].upper()
        url = f"{OPENALEX}/works/{work_id}?{urllib.parse.urlencode({'api_key': key})}"
        payload, freshness = request_json(url, cache_dir, refresh=args.refresh)
        return payload, freshness
    doi = normalize_doi(seed)
    if not doi:
        raise RuntimeError("OpenAlex expansion seed must be a DOI or OpenAlex W identifier")
    params = {
        "filter": f"doi:https://doi.org/{doi}",
        "per_page": "1",
        "select": "id,doi,title,referenced_works",
        "api_key": key,
    }
    url = f"{OPENALEX}/works?{urllib.parse.urlencode(params)}"
    payload, freshness = request_json(url, cache_dir, refresh=args.refresh)
    results = payload.get("results", []) if isinstance(payload, dict) else []
    if not results:
        raise RuntimeError(f"OpenAlex could not resolve seed DOI {doi}")
    return results[0], freshness


def fetch_openalex_ids(
    ids: list[str], args: argparse.Namespace, cache_dir: Path, key: str,
) -> tuple[list[dict[str, Any]], list[str]]:
    records: list[dict[str, Any]] = []
    freshnesses: list[str] = []
    for start in range(0, len(ids), 100):
        chunk = [item.rsplit("/", 1)[-1] for item in ids[start:start + 100]]
        params = {
            "filter": "openalex_id:" + "|".join(chunk),
            "per_page": str(len(chunk)),
            "select": "id,doi,title,authorships,publication_year,publication_date,abstract_inverted_index,cited_by_count,primary_location,best_oa_location,open_access",
            "api_key": key,
        }
        url = f"{OPENALEX}/works?{urllib.parse.urlencode(params)}"
        payload, freshness = request_json(url, cache_dir, refresh=args.refresh)
        freshnesses.append(freshness)
        records.extend(payload.get("results", []) if isinstance(payload, dict) else [])
    return records, freshnesses


def openalex_expand(
    args: argparse.Namespace, cache_dir: Path, direction: str,
) -> tuple[Any, str, list[dict[str, Any]]]:
    key = os.environ.get(args.openalex_api_key_env, "")
    if not key:
        raise RuntimeError(f"missing {args.openalex_api_key_env}; current OpenAlex API requires an API key")
    seed_work, seed_freshness = resolve_openalex_seed(args, cache_dir, key)
    work_id = clean_text(seed_work.get("id")).rsplit("/", 1)[-1]
    if not work_id:
        raise RuntimeError("OpenAlex seed has no work ID")

    if direction == "backward":
        ids = list(seed_work.get("referenced_works") or [])[:args.limit]
        records, freshnesses = fetch_openalex_ids(ids, args, cache_dir, key)
        freshness = "fresh" if "fresh" in [seed_freshness, *freshnesses] else "cache"
    else:
        records = []
        freshnesses = [seed_freshness]
        route_limit = max(1, min(args.limit, 100) // 2)
        for sort in ("cited_by_count:desc", "publication_date:desc"):
            params = {
                "filter": f"cites:{work_id}",
                "per_page": str(route_limit),
                "sort": sort,
                "select": "id,doi,title,authorships,publication_year,publication_date,abstract_inverted_index,cited_by_count,primary_location,best_oa_location,open_access",
                "api_key": key,
            }
            url = f"{OPENALEX}/works?{urllib.parse.urlencode(params)}"
            payload, current = request_json(url, cache_dir, refresh=args.refresh)
            freshnesses.append(current)
            records.extend(payload.get("results", []) if isinstance(payload, dict) else [])
        seen = set()
        records = [record for record in records if not (clean_text(record.get("id")) in seen or seen.add(clean_text(record.get("id"))))]
        records = records[:args.limit]
        freshness = "fresh" if "fresh" in freshnesses else "cache"

    edges = [{
        "related_source_id": clean_text(record.get("id")).rsplit("/", 1)[-1],
        "direction": direction,
        "context_available": "no",
        "context": "",
        "intent": "",
        "is_influential": "",
    } for record in records]
    return {"results": records}, freshness, edges


def make_output(
    output_dir: Path, batches: list[tuple[str, Any, str, str, str, str]],
    events: list[dict[str, Any]], edge_meta: list[dict[str, Any]],
) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    records: list[Record] = []
    for backend, payload, route_id, query_id, round_id, provenance in batches:
        timestamp = next((event["timestamp"] for event in reversed(events) if event["backend"] == backend and event["raw_path"] == provenance), now_iso())
        for item in extract_items(payload, backend):
            record = record_from_item(item, backend, route_id, query_id, round_id, timestamp, provenance)
            if record:
                records.append(record)

    canonical, groups = deduplicate(records)
    key_to_paper: dict[str, str] = {}
    source_to_paper: dict[str, str] = {}
    for record in canonical:
        for key in record.identity_keys():
            key_to_paper[key] = record.paper_id
        for source_id in record.source_record_ids:
            source_to_paper[source_id] = record.paper_id

    with (output_dir / "normalized_candidates.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(record.to_row() for record in canonical)
    with (output_dir / "normalized_candidates.jsonl").open("w", encoding="utf-8") as handle:
        for record in canonical:
            handle.write(json.dumps(record.to_row(), ensure_ascii=False) + "\n")

    group_fields = ["GroupID", "GroupType", "CanonicalPaperID", "MemberCount", "Sources", "Identifiers", "Decision", "Reason"]
    with (output_dir / "dedupe_groups.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=group_fields)
        writer.writeheader()
        writer.writerows(groups)

    edge_rows = []
    for index, edge in enumerate(edge_meta, start=1):
        source_key = f"{edge['backend']}:{edge.get('related_source_id', '')}"
        edge_rows.append({
            "EdgeCandidateID": f"EC{index:05d}",
            "SeedIdentifier": edge.get("seed", ""),
            "RelatedPaperID": source_to_paper.get(source_key, ""),
            "RelatedIdentifier": edge.get("related_source_id", ""),
            "Direction": edge.get("direction", ""),
            "Backend": edge.get("backend", ""),
            "RouteID": edge.get("route_id", ""),
            "RoundID": edge.get("round_id", ""),
            "ContextAvailable": edge.get("context_available", "no"),
            "ContextLead": edge.get("context", ""),
            "Intent": edge.get("intent", ""),
            "IsInfluential": edge.get("is_influential", ""),
            "VerificationStatus": "metadata_only",
            "PublicGraphStatus": "hold",
            "EvidenceID": "",
            "Notes": "check bibliography or original citation context before public direct-citation edge",
        })
    with (output_dir / "citation_edge_candidates.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=EDGE_FIELDS)
        writer.writeheader()
        writer.writerows(edge_rows)

    with (output_dir / "retrieval_events.jsonl").open("w", encoding="utf-8") as handle:
        for event in events:
            handle.write(json.dumps(event, ensure_ascii=False) + "\n")

    summary = {
        "status": "PASS" if canonical and not all(event["status"] == "error" for event in events) else "PARTIAL" if canonical else "FAIL",
        "raw_records": len(records),
        "normalized_candidates": len(canonical),
        "dedupe_groups": len(groups),
        "citation_edge_candidates": len(edge_rows),
        "backend_events": len(events),
        "successful_events": sum(event["status"] in {"fresh", "cache", "ok"} for event in events),
        "blocked_or_failed_events": sum(event["status"] not in {"fresh", "cache", "ok"} for event in events),
        "boundary": "all records remain metadata_only C0 candidates until source and full-text gates pass",
        "generated_at": now_iso(),
    }
    (output_dir / "retrieval_summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    return summary


def run_search(args: argparse.Namespace) -> int:
    output_dir = args.output_dir.resolve()
    cache_dir = (args.cache_dir or output_dir / "cache").resolve()
    events: list[dict[str, Any]] = []
    batches: list[tuple[str, Any, str, str, str, str]] = []
    serial = 0
    runners = {
        "paper-search": lambda: paper_search_query(args),
        "semantic-scholar": lambda: semantic_search(args, cache_dir),
        "openalex": lambda: openalex_search(args, cache_dir),
        "crossref": lambda: crossref_search(args, cache_dir),
    }
    for backend in args.backend:
        started = time.monotonic()
        try:
            payload, status = runners[backend]()
            serial += 1
            raw_path = write_raw(output_dir, backend, "search", payload, serial)
            hits = len(extract_items(payload, backend))
            event = event_record(backend, "search", args.route_id, args.query_id, args.round_id, args.query, status, hits, started, str(raw_path.relative_to(output_dir)))
            events.append(event)
            batches.append((backend, payload, args.route_id, args.query_id, args.round_id, event["raw_path"]))
        except Exception as exc:  # noqa: BLE001
            events.append(event_record(backend, "search", args.route_id, args.query_id, args.round_id, args.query, "error", 0, started, error=str(exc)))
    summary = make_output(output_dir, batches, events, [])
    print(json.dumps(summary, indent=2))
    return 0 if summary["status"] != "FAIL" else 1


def run_expand(args: argparse.Namespace) -> int:
    output_dir = args.output_dir.resolve()
    cache_dir = (args.cache_dir or output_dir / "cache").resolve()
    events: list[dict[str, Any]] = []
    batches: list[tuple[str, Any, str, str, str, str]] = []
    edge_meta: list[dict[str, Any]] = []
    serial = 0
    directions = [args.direction] if args.direction != "both" else ["backward", "forward"]
    for backend in args.backend:
        for direction in directions:
            started = time.monotonic()
            try:
                if backend == "semantic-scholar":
                    payload, status, edges = semantic_expand(args, cache_dir, direction)
                elif backend == "openalex":
                    payload, status, edges = openalex_expand(args, cache_dir, direction)
                else:
                    raise RuntimeError(f"backend {backend} does not provide citation expansion in this runner")
                serial += 1
                raw_path = write_raw(output_dir, backend, f"expand_{direction}", payload, serial)
                hits = len(extract_items(payload, backend))
                event = event_record(backend, f"expand_{direction}", args.route_id, "", args.round_id, args.seed, status, hits, started, str(raw_path.relative_to(output_dir)))
                events.append(event)
                batches.append((backend, payload, args.route_id, "", args.round_id, event["raw_path"]))
                for edge in edges:
                    edge.update({"backend": backend, "seed": args.seed, "route_id": args.route_id, "round_id": args.round_id})
                    edge_meta.append(edge)
            except Exception as exc:  # noqa: BLE001
                events.append(event_record(backend, f"expand_{direction}", args.route_id, "", args.round_id, args.seed, "error", 0, started, error=str(exc)))
    summary = make_output(output_dir, batches, events, edge_meta)
    print(json.dumps(summary, indent=2))
    return 0 if summary["status"] != "FAIL" else 1


def run_ingest(args: argparse.Namespace) -> int:
    output_dir = args.output_dir.resolve()
    events = []
    batches = []
    for index, path in enumerate(args.input, start=1):
        started = time.monotonic()
        payload = json.loads(path.read_text(encoding="utf-8"))
        backend = args.backend_name or "generic"
        hits = len(extract_items(payload, backend))
        provenance = str(path.resolve())
        events.append(event_record(backend, "ingest", args.route_id, args.query_id, args.round_id, provenance, "ok", hits, started, provenance))
        batches.append((backend, payload, args.route_id, args.query_id, args.round_id, provenance))
    summary = make_output(output_dir, batches, events, [])
    print(json.dumps(summary, indent=2))
    return 0 if summary["status"] != "FAIL" else 1


def run_doctor(args: argparse.Namespace) -> int:
    command = shlex.split(args.paper_search_command)
    result = {
        "paper_search": bool(command and shutil.which(command[0])),
        "semantic_scholar": "available_without_key_but_shared_rate_limit" if not os.environ.get(args.semantic_api_key_env) else "key_configured",
        "openalex": "key_configured" if os.environ.get(args.openalex_api_key_env) else "blocked_missing_key",
        "crossref": "available_without_key",
        "semantic_key_env": args.semantic_api_key_env,
        "openalex_key_env": args.openalex_api_key_env,
        "boundary": "readiness does not validate API results or scientific claims",
    }
    print(json.dumps(result, indent=2))
    return 0


def run_self_test() -> int:
    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        payload_a = {
            "papers": [
                {
                    "paper_id": "2606.13790",
                    "title": "Stochastic Path Sampler For Lattice Field Theory",
                    "authors": "Moxian Qian; Example Author",
                    "doi": "",
                    "published_date": "2026-06-16",
                    "url": "https://arxiv.org/abs/2606.13790",
                    "source": "arxiv",
                    "citations": 0,
                },
                {
                    "paper_id": "duplicate",
                    "title": "Stochastic Path Sampler for Lattice Field Theory",
                    "authors": "Moxian Qian; Example Author",
                    "published_date": "2026",
                    "url": "https://arxiv.org/abs/2606.13790v1",
                    "source": "semantic",
                },
            ]
        }
        path = root / "input.json"
        path.write_text(json.dumps(payload_a), encoding="utf-8")
        args = argparse.Namespace(
            input=[path], output_dir=root / "out", backend_name="paper-search",
            route_id="TEST", query_id="QTEST", round_id="RTEST",
        )
        code = run_ingest(args)
        summary = json.loads((root / "out" / "retrieval_summary.json").read_text(encoding="utf-8"))
        rows = list(csv.DictReader((root / "out" / "normalized_candidates.csv").open(encoding="utf-8")))
        errors = []
        if code != 0 or summary["status"] != "PASS":
            errors.append("ingest did not pass")
        if len(rows) != 1:
            errors.append(f"expected one deduplicated row, got {len(rows)}")
        if rows and rows[0]["ArxivID"] != "2606.13790":
            errors.append("arXiv identity normalization failed")
        if rows and rows[0]["Verification"] != "C0":
            errors.append("metadata candidate was promoted unexpectedly")
        edge_payload = {
            "data": [{
                "paperId": "s2-test-id",
                "title": "A Citation Neighbor",
                "authors": [{"name": "Example Author"}],
                "year": 2025,
                "externalIds": {"DOI": "10.1000/test"},
            }]
        }
        edge_event = event_record(
            "semantic-scholar", "expand_forward", "EDGE", "", "REDGE",
            "DOI:10.1000/seed", "ok", 1, time.monotonic(), "synthetic.json",
        )
        make_output(
            root / "edges",
            [("semantic-scholar", edge_payload, "EDGE", "", "REDGE", "synthetic.json")],
            [edge_event],
            [{
                "backend": "semantic-scholar",
                "seed": "DOI:10.1000/seed",
                "related_source_id": "s2-test-id",
                "direction": "forward",
                "route_id": "EDGE",
                "round_id": "REDGE",
                "context_available": "no",
                "context": "",
                "intent": "",
                "is_influential": "",
            }],
        )
        edge_rows = list(csv.DictReader((root / "edges" / "citation_edge_candidates.csv").open(encoding="utf-8")))
        if not edge_rows or edge_rows[0]["RelatedPaperID"] != "P00001":
            errors.append("citation edge did not resolve to normalized PaperID")
        if edge_rows and edge_rows[0]["PublicGraphStatus"] != "hold":
            errors.append("metadata citation edge was exposed publicly")
        if errors:
            print(json.dumps({"status": "FAIL", "errors": errors}, indent=2))
            return 1
    print(json.dumps({"status": "PASS", "checks": 6}, indent=2))
    return 0


def add_common_api_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--cache-dir", type=Path)
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--semantic-api-key-env", default="SEMANTIC_SCHOLAR_API_KEY")
    parser.add_argument("--openalex-api-key-env", default="OPENALEX_API_KEY")
    parser.add_argument("--mailto", default="")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    subparsers = parser.add_subparsers(dest="command")

    doctor = subparsers.add_parser("doctor", help="Report optional backend readiness")
    doctor.add_argument("--paper-search-command", default="paper-search")
    doctor.add_argument("--semantic-api-key-env", default="SEMANTIC_SCHOLAR_API_KEY")
    doctor.add_argument("--openalex-api-key-env", default="OPENALEX_API_KEY")
    doctor.set_defaults(func=run_doctor)

    search = subparsers.add_parser("search", help="Run one or more discovery backends")
    search.add_argument("--query", required=True)
    search.add_argument("--backend", action="append", choices=["paper-search", "semantic-scholar", "openalex", "crossref"], required=True)
    search.add_argument("--limit", type=int, default=20)
    search.add_argument("--year-from", type=int)
    search.add_argument("--year-to", type=int)
    search.add_argument("--route-id", default="CH001")
    search.add_argument("--query-id", default="Q001")
    search.add_argument("--round-id", default="R0001")
    search.add_argument("--output-dir", type=Path, required=True)
    search.add_argument("--paper-search-command", default="paper-search")
    search.add_argument("--paper-search-sources", default="arxiv,semantic,crossref")
    add_common_api_options(search)
    search.set_defaults(func=run_search)

    expand = subparsers.add_parser("expand", help="Run backward/forward citation expansion")
    expand.add_argument("--seed", required=True)
    expand.add_argument("--backend", action="append", choices=["semantic-scholar", "openalex"], required=True)
    expand.add_argument("--direction", choices=["backward", "forward", "both"], default="both")
    expand.add_argument("--limit", type=int, default=50)
    expand.add_argument("--route-id", default="CH002")
    expand.add_argument("--round-id", default="R0002")
    expand.add_argument("--output-dir", type=Path, required=True)
    add_common_api_options(expand)
    expand.set_defaults(func=run_expand)

    ingest = subparsers.add_parser("ingest", help="Normalize saved JSON responses")
    ingest.add_argument("--input", type=Path, action="append", required=True)
    ingest.add_argument("--backend-name", default="generic")
    ingest.add_argument("--route-id", default="IMPORT")
    ingest.add_argument("--query-id", default="")
    ingest.add_argument("--round-id", default="R0000")
    ingest.add_argument("--output-dir", type=Path, required=True)
    ingest.set_defaults(func=run_ingest)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.self_test:
        return run_self_test()
    if not getattr(args, "command", None):
        parser.error("choose a command or use --self-test")
    if hasattr(args, "limit") and args.limit < 1:
        parser.error("--limit must be positive")
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
