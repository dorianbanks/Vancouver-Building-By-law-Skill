#!/usr/bin/env python3
"""Build a citation -> page index from the VBBL PDFs (two-volume set).

The VBBL 2025 is published in two volumes:
  Volume 1 — Book I (General), Divisions A, B, C (all Parts except Part 9)
  Volume 2 — Part 9 Housing and Small Buildings

This script walks the PDF bookmark tree of BOTH volumes and tags every row
with its source volume and page number, so `lookup.py` can route citations
to the right PDF.

Produces three files alongside the skill:
  references/index.json   — machine-readable: {citation, title, page, depth, volume}
  references/index.md     — human-readable: hierarchical TOC with page refs
  references/citations.json — fast path for scripts/lookup.py (citation → {volume, page})

Run once after dropping new VBBL PDFs into assets/.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from pypdf import PdfReader

SKILL_DIR = Path(__file__).resolve().parent.parent
ASSETS = SKILL_DIR / "assets"
VOLUMES = [
    {"volume": 1, "path": ASSETS / "vbbl_2025_vol1.pdf", "label": "Vol 1 (General)"},
    {"volume": 2, "path": ASSETS / "vbbl_2025_vol2.pdf", "label": "Vol 2 (Part 9)"},
]
INDEX_JSON = SKILL_DIR / "references" / "index.json"
INDEX_MD = SKILL_DIR / "references" / "index.md"
CITATIONS_JSON = SKILL_DIR / "references" / "citations.json"

# Matches VBBL citation patterns at the start of a bookmark title:
#   "1.1.1."           (Subsection)
#   "1.1.1.1."         (Article)
#   "1.1.1.1.(3)"      (Sentence)
#   "Section 3.2."     (Section)
#   "Part 3"           (Part)
CITATION_RE = re.compile(
    r"""^\s*(?:
        (?:Section\s+)?(?P<section>\d+\.\d+\.)\s+               |
        (?P<subsection>\d+\.\d+\.\d+\.)\s+                      |
        (?P<article>\d+\.\d+\.\d+\.\d+\.)(?:\((?P<sent>\d+)\))? |
        Part\s+(?P<part>\d+)(?:\b|\s)
    )""",
    re.VERBOSE,
)


def walk(reader: PdfReader, items, depth: int, rows: list, volume: int) -> None:
    for it in items:
        if isinstance(it, list):
            walk(reader, it, depth + 1, rows, volume)
            continue
        try:
            title = (it.title or "").strip()
            page = reader.get_destination_page_number(it) + 1  # 1-indexed
        except Exception:
            continue
        if not title:
            continue
        citation = extract_citation(title)
        rows.append(
            {
                "volume": volume,
                "depth": depth,
                "title": title,
                "page": page,
                "citation": citation,
            }
        )


def extract_citation(title: str) -> str | None:
    m = CITATION_RE.match(title)
    if not m:
        return None
    gd = m.groupdict()
    if gd.get("article"):
        base = gd["article"].rstrip(".")
        return f"{base}.({gd['sent']})" if gd.get("sent") else base
    for key in ("subsection", "section"):
        if gd.get(key):
            return gd[key].rstrip(".")
    if gd.get("part"):
        return f"Part {gd['part']}"
    return None


def to_markdown(rows: list[dict]) -> str:
    lines = [
        "# VBBL 2025 — Citation Index",
        "",
        "Auto-generated from the PDF bookmark trees of both volumes. Pages are 1-indexed.",
        "Volume 1 = `assets/vbbl_2025_vol1.pdf` (Book I, General — Divisions A/B/C, all Parts except Part 9).",
        "Volume 2 = `assets/vbbl_2025_vol2.pdf` (Part 9 — Housing and Small Buildings).",
        "",
        "Use `scripts/lookup.py <citation>` to resolve a citation to volume + page, or read the",
        "PDF directly with the Read tool and the `pages` parameter.",
        "",
    ]
    current_volume = None
    for r in rows:
        if r["volume"] != current_volume:
            current_volume = r["volume"]
            label = "Volume 1 (General)" if current_volume == 1 else "Volume 2 (Part 9)"
            lines.append(f"\n# ═══ {label} ═══\n")
        indent = "  " * min(r["depth"], 6)
        cite = f"**{r['citation']}** — " if r["citation"] else ""
        lines.append(f"{indent}- {cite}{r['title']}  _(v{r['volume']} p.{r['page']})_")
    return "\n".join(lines) + "\n"


def main() -> int:
    rows: list[dict] = []
    total_pages = 0
    for vol in VOLUMES:
        if not vol["path"].exists():
            print(f"PDF not found at {vol['path']}", file=sys.stderr)
            return 1
        reader = PdfReader(str(vol["path"]))
        total_pages += len(reader.pages)
        before = len(rows)
        walk(reader, reader.outline, 0, rows, vol["volume"])
        print(f"  {vol['label']}: {len(reader.pages)} pages, {len(rows) - before} bookmarks indexed")

    INDEX_JSON.write_text(json.dumps(rows, indent=2))
    INDEX_MD.write_text(to_markdown(rows))

    # Fast lookup map. Each citation maps to {volume, page}. Duplicate citations
    # (same number appearing in multiple Divisions) are stored under `_alternates`.
    cites: dict[str, dict] = {}
    alternates: dict[str, list[dict]] = {}
    for r in rows:
        c = r["citation"]
        if not c:
            continue
        entry = {"volume": r["volume"], "page": r["page"]}
        if c not in cites:
            cites[c] = entry
        else:
            alternates.setdefault(c, []).append(
                {"volume": r["volume"], "page": r["page"], "title": r["title"]}
            )
    CITATIONS_JSON.write_text(
        json.dumps({"citations": cites, "alternates": alternates}, indent=2)
    )

    print()
    print(f"Indexed {len(rows)} entries across {total_pages} pages in {len(VOLUMES)} volumes.")
    print(f"Unique citations: {len(cites)} (with {sum(len(v) for v in alternates.values())} alternates)")
    print("Wrote:")
    print(f"  {INDEX_JSON.relative_to(SKILL_DIR)}")
    print(f"  {INDEX_MD.relative_to(SKILL_DIR)}")
    print(f"  {CITATIONS_JSON.relative_to(SKILL_DIR)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
