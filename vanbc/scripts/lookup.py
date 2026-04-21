#!/usr/bin/env python3
"""VBBL citation → (volume, PDF page) resolver.

The VBBL 2025 is split across two PDFs:
  Volume 1 — assets/vbbl_2025_vol1.pdf  (Book I General, all Parts except Part 9)
  Volume 2 — assets/vbbl_2025_vol2.pdf  (Part 9 Housing and Small Buildings)

This script resolves a citation to the correct volume and page, prints the
result, and — with --extract — pulls the extracted text for quick skimming.
Always read the PDF (not --extract output) when giving a user an authoritative
answer; text extraction can lose tables and layout.

Usage:
    python3 scripts/lookup.py 3.2.2.47
    python3 scripts/lookup.py 9.8.4.1                 # routes to Volume 2
    python3 scripts/lookup.py "Part 9"
    python3 scripts/lookup.py "Sentence 9.8.4.2.(1)"  # falls back to containing Article
    python3 scripts/lookup.py --search "spatial separation"
    python3 scripts/lookup.py --extract 3.2.2.47
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
CITATIONS = SKILL_DIR / "references" / "citations.json"
INDEX = SKILL_DIR / "references" / "index.json"
VOLUME_PDFS = {
    1: SKILL_DIR / "assets" / "vbbl_2025_vol1.pdf",
    2: SKILL_DIR / "assets" / "vbbl_2025_vol2.pdf",
}


def normalize(cite: str) -> str:
    """Normalize a user-provided citation.

    Architects write citations many ways: "3.2.2.47", "3.2.2.47.", "3.2.2.47(3)",
    "3.2.2.47.(3)", "Sentence 3.2.2.47.(3)". Normalize to the internal form
    used by the index: "3.2.2.47" or "3.2.2.47.(3)".
    """
    s = cite.strip()
    m = re.match(r"^Part\s+(\d+)\b", s, flags=re.I)
    if m:
        return f"Part {m.group(1)}"
    s = re.sub(r"^(Section|Sentence|Article|Subsection)\s+", "", s, flags=re.I)
    s = re.sub(r"\s+", "", s)
    m = re.match(r"^(\d+(?:\.\d+){1,3})\.?(\(\d+\))?$", s)
    if m:
        base = m.group(1)
        sent = m.group(2) or ""
        if sent:
            return f"{base}.{sent}"
        return base
    return s


def _broader_levels(cite: str) -> list[tuple[str, str]]:
    """Yield progressively broader containing citations to try as fallbacks.

    Examples:
      "9.8.4.2.(1)" → [("9.8.4.2", "sentence ... lives in Article ..."),
                       ("9.8.4",   "sentence ... lives in Subsection ..."),
                       ("9.8",     "sentence ... lives in Section ...")]
      "3.2.2.47"    → [("3.2.2",   "Article ... lives in Subsection ..."),
                       ("3.2",     "Article ... lives in Section ...")]
    """
    m = re.match(r"^(\d+\.\d+\.\d+\.\d+)\.\(\d+\)$", cite)
    if m:
        article = m.group(1)
        subsection = article.rsplit(".", 1)[0]
        section = subsection.rsplit(".", 1)[0]
        return [
            (article, "sentence {cite} lives in Article {broader}"),
            (subsection, "sentence {cite} lives in Subsection {broader}"),
            (section, "sentence {cite} lives in Section {broader}"),
        ]
    m = re.match(r"^\d+\.\d+\.\d+\.\d+$", cite)
    if m:
        subsection = cite.rsplit(".", 1)[0]
        section = subsection.rsplit(".", 1)[0]
        return [
            (subsection, "Article {cite} lives in Subsection {broader}"),
            (section, "Article {cite} lives in Section {broader}"),
        ]
    m = re.match(r"^\d+\.\d+\.\d+$", cite)
    if m:
        section = cite.rsplit(".", 1)[0]
        return [(section, "Subsection {cite} lives in Section {broader}")]
    return []


def find_exact(cite: str, cites: dict, alternates: dict) -> list[dict]:
    hits = []
    if cite in cites:
        e = cites[cite]
        hits.append({"citation": cite, "volume": e["volume"], "page": e["page"], "source": "primary"})
    for alt in alternates.get(cite, []):
        hits.append({
            "citation": cite,
            "volume": alt["volume"],
            "page": alt["page"],
            "title": alt["title"],
            "source": "alternate",
        })
    return hits


def find_partial(cite: str, rows: list[dict]) -> list[dict]:
    """Partial-prefix match: "9.8.4" matches all sub-entries under 9.8.4."""
    return [r for r in rows if r["citation"] and r["citation"].startswith(cite)]


def search_titles(query: str, rows: list[dict], limit: int = 25) -> list[dict]:
    q = query.lower()
    return [r for r in rows if q in r["title"].lower()][:limit]


def extract_text(volume: int, page_num: int, context_pages: int = 1) -> str:
    try:
        from pypdf import PdfReader
    except ImportError:
        return "(pypdf not installed; cannot extract text)"
    pdf = VOLUME_PDFS[volume]
    reader = PdfReader(str(pdf))
    start = max(0, page_num - 1)
    end = min(len(reader.pages), page_num + context_pages)
    chunks = []
    for i in range(start, end):
        chunks.append(f"--- Volume {volume}, Page {i+1} ---\n{reader.pages[i].extract_text() or ''}")
    return "\n\n".join(chunks)


def format_hit(h: dict) -> str:
    label = h.get("title", h["citation"])
    extra = f" — {h['note']}" if h.get("note") else ""
    pdf_name = VOLUME_PDFS[h["volume"]].name
    return (
        f"{h['citation']}  →  Volume {h['volume']} ({pdf_name}), p.{h['page']}  "
        f"({h['source']}: {label}){extra}"
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("citation", nargs="?", help="Citation like 3.2.2.47, 9.8.4.1, or 'Part 9'")
    ap.add_argument("--search", metavar="QUERY", help="Substring search over outline titles")
    ap.add_argument("--extract", action="store_true", help="Also print extracted text from the PDF page")
    ap.add_argument("--json", action="store_true", help="Emit JSON result")
    ap.add_argument("--volume", type=int, choices=[1, 2], help="Restrict results to one volume")
    args = ap.parse_args()

    if not (args.citation or args.search):
        ap.print_help()
        return 2

    data = json.loads(CITATIONS.read_text())
    rows = json.loads(INDEX.read_text())
    cites = data["citations"]
    alternates = data["alternates"]

    if args.search:
        hits = search_titles(args.search, rows)
        if args.volume:
            hits = [h for h in hits if h["volume"] == args.volume]
        if args.json:
            print(json.dumps(hits, indent=2))
        else:
            if not hits:
                print(f"No outline entries match: {args.search!r}", file=sys.stderr)
                return 1
            for r in hits:
                c = f"[{r['citation']}] " if r["citation"] else ""
                print(f"v{r['volume']} p.{r['page']:>4}  {c}{r['title']}")
        return 0

    cite = normalize(args.citation)
    hits = find_exact(cite, cites, alternates)
    # Cascade: if nothing matched, try the containing level. VBBL outlines
    # frequently stop at Subsection, so sentences and Articles both fall back.
    if not hits:
        for broader, note_fmt in _broader_levels(cite):
            hits = find_exact(broader, cites, alternates)
            if hits:
                for h in hits:
                    h["note"] = note_fmt.format(cite=cite, broader=broader)
                break
    if args.volume:
        hits = [h for h in hits if h["volume"] == args.volume]
    if not hits:
        partial = find_partial(cite, rows)
        if args.volume:
            partial = [r for r in partial if r["volume"] == args.volume]
        if partial:
            if args.json:
                print(json.dumps(partial, indent=2))
            else:
                print(f"No exact match for {cite!r}. Partial matches (prefix):")
                for r in partial[:25]:
                    print(f"  v{r['volume']} p.{r['page']:>4}  [{r['citation']}] {r['title']}")
            return 0
        print(f"No match for citation {cite!r}. Try --search instead.", file=sys.stderr)
        return 1

    if args.json and not args.extract:
        print(json.dumps(hits, indent=2))
        return 0

    for h in hits:
        print(format_hit(h))
        if args.extract:
            print()
            print(extract_text(h["volume"], h["page"], context_pages=1))
            print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
