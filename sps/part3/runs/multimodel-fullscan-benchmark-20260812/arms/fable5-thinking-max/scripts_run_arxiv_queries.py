#!/usr/bin/env python3
"""R0002 lexical route: run planned arXiv API queries Q001-Q009 (1 web call each)."""
import time, urllib.parse, urllib.request, re, html, json, sys

QUERIES = {
 "Q001": 'all:"normalizing flow" AND all:"lattice field theory"',
 "Q002": 'all:"flow-based sampling" AND all:"lattice"',
 "Q003": 'all:"stochastic normalizing flows"',
 "Q004": 'all:"annealed importance sampling" AND all:"normalizing flow"',
 "Q005": 'all:"Boltzmann generator"',
 "Q006": 'all:"unnormalized" AND all:"neural" AND all:"sampler"',
 "Q007": 'all:"diffusion model" AND all:"lattice gauge theory"',
 "Q008": 'all:"trivializing" AND all:"lattice"',
 "Q009": 'all:"Jarzynski" AND all:"lattice"',
}

def parse(atom):
    out = []
    for entry in re.findall(r"<entry>(.*?)</entry>", atom, re.S):
        def g(tag):
            m = re.search(rf"<{tag}>(.*?)</{tag}>", entry, re.S)
            return html.unescape(re.sub(r"\s+", " ", m.group(1))).strip() if m else ""
        aid = g("id").split("/abs/")[-1]
        out.append({"id": aid, "title": g("title"), "published": g("published")[:10],
                    "authors": re.findall(r"<name>(.*?)</name>", entry)[:3]})
    return out

results = {}
for qid, q in QUERIES.items():
    url = ("http://export.arxiv.org/api/query?search_query=" + urllib.parse.quote(q)
           + "&start=0&max_results=30&sortBy=relevance")
    try:
        with urllib.request.urlopen(url, timeout=45) as r:
            atom = r.read().decode("utf-8", "replace")
        m = re.search(r"totalResults[^>]*>(\d+)", atom)
        total = int(m.group(1)) if m else -1
        entries = parse(atom)
        results[qid] = {"query": q, "totalResults": total, "returned": len(entries),
                        "entries": entries, "status": "ok"}
        print(f"{qid}: total={total} returned={len(entries)}")
    except Exception as e:
        results[qid] = {"query": q, "status": f"FAILED: {e}"}
        print(f"{qid}: FAILED {e}")
    time.sleep(3)

json.dump(results, open("r0002_arxiv_results.json", "w"), indent=1)
print("saved r0002_arxiv_results.json")
