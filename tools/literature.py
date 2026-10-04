#!/usr/bin/env python3
"""Literature discovery pipeline for the self research repository.

Uses public scholarly APIs to discover, merge, rank, and expand candidate works.
No third-party Python packages are required.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

USER_AGENT = "self-literature/0.1 (+https://github.com/RinoPaw/self)"
OPENALEX = "https://api.openalex.org"
S2 = "https://api.semanticscholar.org/graph/v1"
CROSSREF = "https://api.crossref.org"


def request_json(url: str, *, headers: dict[str, str] | None = None) -> Any:
    merged = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    if headers:
        merged.update(headers)
    req = urllib.request.Request(url, headers=merged)
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code} for {url}\n{body[:500]}") from exc


def clean_doi(value: str | None) -> str | None:
    if not value:
        return None
    value = value.strip()
    for prefix in ("https://doi.org/", "http://doi.org/", "doi:"):
        if value.lower().startswith(prefix):
            value = value[len(prefix):]
            break
    return value.lower() or None


def openalex_id(value: str | None) -> str | None:
    if not value:
        return None
    return value.rsplit("/", 1)[-1]


def reconstruct_abstract(index: dict[str, list[int]] | None) -> str | None:
    if not index:
        return None
    positions: list[tuple[int, str]] = []
    for token, offsets in index.items():
        positions.extend((offset, token) for offset in offsets)
    positions.sort()
    return " ".join(token for _, token in positions)


def oa_location_url(location: dict[str, Any] | None) -> str | None:
    if not location:
        return None
    return location.get("pdf_url") or location.get("landing_page_url")


def normalize_openalex(work: dict[str, Any], rank: int) -> dict[str, Any]:
    primary = work.get("primary_location") or {}
    source = primary.get("source") or {}
    best_oa = work.get("best_oa_location") or {}
    return {
        "title": work.get("title") or work.get("display_name"),
        "authors": [
            ((a.get("author") or {}).get("display_name"))
            for a in (work.get("authorships") or [])
            if (a.get("author") or {}).get("display_name")
        ],
        "year": work.get("publication_year"),
        "doi": clean_doi(work.get("doi")),
        "venue": source.get("display_name"),
        "type": work.get("type"),
        "abstract": reconstruct_abstract(work.get("abstract_inverted_index")),
        "citation_count": work.get("cited_by_count") or 0,
        "reference_count": len(work.get("referenced_works") or []),
        "open_access_url": oa_location_url(best_oa),
        "url": primary.get("landing_page_url") or work.get("doi") or work.get("id"),
        "ids": {"openalex": openalex_id(work.get("id"))},
        "sources": ["openalex"],
        "source_ranks": {"openalex": rank},
    }


def s2_headers() -> dict[str, str]:
    key = os.getenv("SEMANTIC_SCHOLAR_API_KEY")
    return {"x-api-key": key} if key else {}


def normalize_s2(work: dict[str, Any], rank: int, source_name: str = "semantic_scholar") -> dict[str, Any]:
    ext = work.get("externalIds") or {}
    oa = work.get("openAccessPdf") or {}
    publication_types = work.get("publicationTypes") or []
    return {
        "title": work.get("title"),
        "authors": [a.get("name") for a in (work.get("authors") or []) if a.get("name")],
        "year": work.get("year"),
        "doi": clean_doi(ext.get("DOI")),
        "venue": work.get("venue"),
        "type": ", ".join(publication_types) if publication_types else None,
        "abstract": work.get("abstract"),
        "citation_count": work.get("citationCount") or 0,
        "reference_count": work.get("referenceCount") or 0,
        "open_access_url": oa.get("url"),
        "url": work.get("url"),
        "ids": {
            "semantic_scholar": work.get("paperId"),
            **({"arxiv": ext.get("ArXiv")} if ext.get("ArXiv") else {}),
        },
        "sources": [source_name],
        "source_ranks": {source_name: rank},
    }


def crossref_date(item: dict[str, Any]) -> int | None:
    for field in ("published-print", "published-online", "published", "issued"):
        parts = ((item.get(field) or {}).get("date-parts") or [])
        if parts and parts[0]:
            return parts[0][0]
    return None


def normalize_crossref(item: dict[str, Any], rank: int) -> dict[str, Any]:
    title = (item.get("title") or [None])[0]
    venue = (item.get("container-title") or [None])[0]
    authors = []
    for author in item.get("author") or []:
        name = " ".join(x for x in (author.get("given"), author.get("family")) if x)
        if name:
            authors.append(name)
    return {
        "title": title,
        "authors": authors,
        "year": crossref_date(item),
        "doi": clean_doi(item.get("DOI")),
        "venue": venue,
        "type": item.get("type"),
        "abstract": None,
        "citation_count": item.get("is-referenced-by-count") or 0,
        "reference_count": len(item.get("reference") or []),
        "open_access_url": None,
        "url": item.get("URL"),
        "ids": {"crossref": clean_doi(item.get("DOI"))},
        "sources": ["crossref"],
        "source_ranks": {"crossref": rank},
    }


def search_openalex(query: str, limit: int, semantic: bool) -> list[dict[str, Any]]:
    parameter = "search.semantic" if semantic else "search"
    params = {
        parameter: query,
        "per_page": str(min(limit, 50 if semantic else 100)),
        "select": ",".join([
            "id", "doi", "title", "authorships", "publication_year",
            "cited_by_count", "primary_location", "best_oa_location",
            "open_access", "type", "referenced_works", "abstract_inverted_index",
        ]),
    }
    key = os.getenv("OPENALEX_API_KEY")
    if key:
        params["api_key"] = key
    data = request_json(f"{OPENALEX}/works?{urllib.parse.urlencode(params)}")
    return [normalize_openalex(w, i) for i, w in enumerate(data.get("results") or [])]


def search_s2(query: str, limit: int) -> list[dict[str, Any]]:
    fields = ",".join([
        "paperId", "title", "abstract", "authors", "year", "citationCount",
        "referenceCount", "externalIds", "url", "venue", "publicationTypes",
        "openAccessPdf",
    ])
    params = {"query": query, "limit": str(min(limit, 100)), "fields": fields}
    data = request_json(
        f"{S2}/paper/search?{urllib.parse.urlencode(params)}",
        headers=s2_headers(),
    )
    return [normalize_s2(w, i) for i, w in enumerate(data.get("data") or [])]


def search_crossref(query: str, limit: int) -> list[dict[str, Any]]:
    params = {"query.bibliographic": query, "rows": str(min(limit, 100))}
    mailto = os.getenv("CROSSREF_MAILTO")
    if mailto:
        params["mailto"] = mailto
    data = request_json(f"{CROSSREF}/works?{urllib.parse.urlencode(params)}")
    items = ((data.get("message") or {}).get("items") or [])
    return [normalize_crossref(w, i) for i, w in enumerate(items)]


def normalize_title(title: str | None) -> str:
    if not title:
        return ""
    return "".join(ch.lower() for ch in title if ch.isalnum())


def record_key(record: dict[str, Any]) -> str:
    if record.get("doi"):
        return f"doi:{record['doi']}"
    s2 = (record.get("ids") or {}).get("semantic_scholar")
    if s2:
        return f"s2:{s2}"
    oa = (record.get("ids") or {}).get("openalex")
    if oa:
        return f"oa:{oa}"
    return f"title:{normalize_title(record.get('title'))}"


def merge_one(base: dict[str, Any], incoming: dict[str, Any]) -> None:
    for field in ("title", "year", "doi", "venue", "type", "abstract", "open_access_url", "url"):
        if not base.get(field) and incoming.get(field):
            base[field] = incoming[field]
    if len(incoming.get("authors") or []) > len(base.get("authors") or []):
        base["authors"] = incoming["authors"]
    base["citation_count"] = max(base.get("citation_count") or 0, incoming.get("citation_count") or 0)
    base["reference_count"] = max(base.get("reference_count") or 0, incoming.get("reference_count") or 0)
    base.setdefault("ids", {}).update({k: v for k, v in (incoming.get("ids") or {}).items() if v})
    base["sources"] = sorted(set((base.get("sources") or []) + (incoming.get("sources") or [])))
    base.setdefault("source_ranks", {}).update(incoming.get("source_ranks") or {})


def dedupe(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_key: dict[str, dict[str, Any]] = {}
    title_keys: dict[str, str] = {}
    for record in records:
        key = record_key(record)
        normalized_title = normalize_title(record.get("title"))
        existing_key = key if key in by_key else title_keys.get(normalized_title)
        if existing_key:
            merge_one(by_key[existing_key], record)
            if key != existing_key and key.startswith("doi:"):
                by_key[key] = by_key.pop(existing_key)
                existing_key = key
            title_keys[normalized_title] = existing_key
        else:
            by_key[key] = record
            if normalized_title:
                title_keys[normalized_title] = key
    return list(by_key.values())


def triage_score(record: dict[str, Any]) -> float:
    """Transparent discovery score, not a claim of philosophical quality."""
    score = 0.0
    sources = record.get("sources") or []
    score += min(len(sources), 3) * 6
    citations = record.get("citation_count") or 0
    score += min(math.log10(citations + 1) * 9, 30)
    if record.get("doi"):
        score += 7
    if record.get("venue"):
        score += 4
    if record.get("year"):
        score += 2
    if record.get("open_access_url"):
        score += 3
    ranks = record.get("source_ranks") or {}
    if ranks:
        best = min(ranks.values())
        score += 18 / (1 + best / 4)
    return round(score, 2)


def rank_records(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    for record in records:
        record["triage_score"] = triage_score(record)
    return sorted(records, key=lambda r: r["triage_score"], reverse=True)


def combined_search(query: str, limit: int, semantic: bool, sources: set[str]) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    failures: list[str] = []
    jobs = []
    if "openalex" in sources:
        jobs.append(("OpenAlex", lambda: search_openalex(query, limit, semantic)))
    if "s2" in sources:
        jobs.append(("Semantic Scholar", lambda: search_s2(query, limit)))
    if "crossref" in sources:
        jobs.append(("Crossref", lambda: search_crossref(query, limit)))

    for name, job in jobs:
        try:
            records.extend(job())
        except Exception as exc:
            failures.append(f"{name}: {exc}")

    if failures:
        print("Warnings:", file=sys.stderr)
        for failure in failures:
            print(f"  - {failure}", file=sys.stderr)

    return rank_records(dedupe(records))


S2_FIELDS = ",".join([
    "paperId", "title", "abstract", "authors", "year", "citationCount",
    "referenceCount", "externalIds", "url", "venue", "publicationTypes",
    "openAccessPdf",
])


def s2_match(title: str) -> dict[str, Any]:
    params = {"query": title, "fields": S2_FIELDS}
    return request_json(
        f"{S2}/paper/search/match?{urllib.parse.urlencode(params)}",
        headers=s2_headers(),
    )


def expand_s2(title: str, direction: str, limit: int) -> list[dict[str, Any]]:
    matched = s2_match(title)
    paper_id = matched.get("paperId")
    if not paper_id:
        raise RuntimeError(f"Semantic Scholar could not match: {title}")
    endpoint = "citations" if direction == "citations" else "references"
    params = {"limit": str(min(limit, 1000)), "fields": S2_FIELDS}
    data = request_json(
        f"{S2}/paper/{urllib.parse.quote(paper_id)}/{endpoint}?{urllib.parse.urlencode(params)}",
        headers=s2_headers(),
    )
    node = "citingPaper" if direction == "citations" else "citedPaper"
    records = []
    for i, edge in enumerate(data.get("data") or []):
        paper = edge.get(node)
        if paper and paper.get("title"):
            records.append(normalize_s2(paper, i, f"s2_{direction}"))
    return rank_records(dedupe(records))


def write_output(records: list[dict[str, Any]], output: str | None, query: str) -> None:
    payload = {
        "query": query,
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "count": len(records),
        "records": records,
    }
    text = json.dumps(payload, ensure_ascii=False, indent=2)
    if not output:
        print(text)
        return
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text + "\n", encoding="utf-8")
    print(f"Wrote {len(records)} records to {path}")


def render_markdown(records: list[dict[str, Any]], query: str, output: str) -> None:
    lines = [f"# Candidate literature: {query}", "", "> Generated discovery list. Triage score is only a prioritization aid.", ""]
    for i, record in enumerate(records, 1):
        authors = ", ".join(record.get("authors") or [])
        meta = " · ".join(str(x) for x in (authors, record.get("year"), record.get("venue")) if x)
        lines.extend([
            f"## {i}. {record.get('title') or '(untitled)'}",
            "",
            meta,
            "",
            f"- triage score: {record.get('triage_score')}",
            f"- citations: {record.get('citation_count', 0)}",
            f"- DOI: {record.get('doi') or '—'}",
            f"- sources: {', '.join(record.get('sources') or [])}",
            f"- OA/full text: {record.get('open_access_url') or '—'}",
            f"- landing page: {record.get('url') or '—'}",
            "",
        ])
    path = Path(output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote Markdown shortlist to {path}")


def parse_sources(value: str) -> set[str]:
    aliases = {"semantic_scholar": "s2", "semanticscholar": "s2"}
    result = set()
    for item in value.split(","):
        item = aliases.get(item.strip().lower(), item.strip().lower())
        if item:
            result.add(item)
    allowed = {"openalex", "s2", "crossref"}
    unknown = result - allowed
    if unknown:
        raise argparse.ArgumentTypeError(f"unknown sources: {', '.join(sorted(unknown))}")
    return result


def cmd_search(args: argparse.Namespace) -> None:
    records = combined_search(args.query, args.limit, args.semantic, args.sources)
    write_output(records, args.output, args.query)
    if args.markdown:
        render_markdown(records, args.query, args.markdown)


def cmd_expand(args: argparse.Namespace) -> None:
    records = expand_s2(args.title, args.direction, args.limit)
    label = f"{args.direction} of {args.title}"
    write_output(records, args.output, label)
    if args.markdown:
        render_markdown(records, label, args.markdown)


def cmd_batch(args: argparse.Namespace) -> None:
    config = json.loads(Path(args.config).read_text(encoding="utf-8"))
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for entry in config.get("queries") or []:
        name = entry["name"]
        query = entry["query"]
        semantic = bool(entry.get("semantic", False))
        limit = int(entry.get("limit", args.limit))
        sources = parse_sources(",".join(entry.get("sources") or ["openalex", "s2", "crossref"]))
        print(f"[{name}] {query}", file=sys.stderr)
        records = combined_search(query, limit, semantic, sources)
        write_output(records, str(out_dir / f"{name}.json"), query)
        render_markdown(records[: args.markdown_limit], query, str(out_dir / f"{name}.md"))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Discover and expand literature for self.")
    sub = parser.add_subparsers(dest="command", required=True)

    search = sub.add_parser("search", help="Search multiple scholarly indexes and merge results.")
    search.add_argument("query")
    search.add_argument("--limit", type=int, default=20, help="Results requested from each source.")
    search.add_argument("--semantic", action="store_true", help="Use OpenAlex semantic search.")
    search.add_argument("--sources", type=parse_sources, default={"openalex", "s2", "crossref"})
    search.add_argument("-o", "--output")
    search.add_argument("--markdown")
    search.set_defaults(func=cmd_search)

    expand = sub.add_parser("expand", help="Expand a seed paper through Semantic Scholar's citation graph.")
    expand.add_argument("title", help="Seed paper title; closest title match is used.")
    expand.add_argument("--direction", choices=("citations", "references"), default="citations")
    expand.add_argument("--limit", type=int, default=50)
    expand.add_argument("-o", "--output")
    expand.add_argument("--markdown")
    expand.set_defaults(func=cmd_expand)

    batch = sub.add_parser("batch", help="Run the curated query set.")
    batch.add_argument("--config", default="literature/queries.json")
    batch.add_argument("--output-dir", default="literature/candidates")
    batch.add_argument("--limit", type=int, default=20)
    batch.add_argument("--markdown-limit", type=int, default=20)
    batch.set_defaults(func=cmd_batch)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
