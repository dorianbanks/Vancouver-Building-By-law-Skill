#!/usr/bin/env python3
"""Derive compact navigation files from references/index.json.

Two-volume aware: each entry is tagged with its source volume so the generated
map/tables/figures files tell Claude which PDF to read.

Outputs:
  references/map.md         — Parts, Sections, Subsections only (context-friendly)
  references/tables.md      — every numbered Table with volume + page number
  references/figures.md     — every numbered Figure with volume + page number
  references/definitions.md — Part 1.4 defined terms list with volume + page numbers
"""
from __future__ import annotations

import json
import re
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
INDEX = SKILL_DIR / "references" / "index.json"
MAP_MD = SKILL_DIR / "references" / "map.md"
TABLES_MD = SKILL_DIR / "references" / "tables.md"
FIGURES_MD = SKILL_DIR / "references" / "figures.md"
DEFINITIONS_MD = SKILL_DIR / "references" / "definitions.md"

TABLE_RE = re.compile(r"\bTable\s+(?P<cite>[A-Z]?-?\d+\.\d+\.\d+\.\d+\.?(?:\(\d+\))?)[.\s]", re.I)
FIGURE_RE = re.compile(r"\bFigure\s+(?P<cite>[A-Z]?-?\d+\.\d+\.\d+\.\d+\.?(?:\(\d+\))?)", re.I)
SECTION_RE = re.compile(r"^(Section\s+)?(\d+\.\d+\.)\s+")
SUBSECTION_RE = re.compile(r"^(\d+\.\d+\.\d+\.)\s+")
PART_RE = re.compile(r"^Part\s+(\d+)\b", re.I)
DIVISION_RE = re.compile(r"^(BOOK\s+I+\s+\(GENERAL\)\s*-\s*)?Division\s+([ABC])\b", re.I)
BOOK_RE = re.compile(r"^BOOK\s+([IVX]+)", re.I)


def load_rows() -> list[dict]:
    return json.loads(INDEX.read_text())


def vol_page(r: dict) -> str:
    return f"v{r['volume']} p.{r['page']}"


def build_map(rows: list[dict]) -> str:
    lines = [
        "# VBBL 2025 — Structural Map",
        "",
        "High-level navigation: Books, Divisions, Parts, Sections, and Subsections.",
        "For articles and sentences, see `index.md` or run `scripts/lookup.py <citation>`.",
        "",
        "Volumes:",
        "- `v1` → `assets/vbbl_2025_vol1.pdf` (Book I, Divisions A/B/C — all Parts except Part 9)",
        "- `v2` → `assets/vbbl_2025_vol2.pdf` (Part 9 — Housing and Small Buildings)",
        "",
    ]
    current_volume = None
    for r in rows:
        if r["volume"] != current_volume:
            current_volume = r["volume"]
            label = "Volume 1 (General)" if current_volume == 1 else "Volume 2 (Part 9)"
            lines.append(f"\n# ═══ {label} ═══\n")
        t = r["title"].strip()
        vp = vol_page(r)
        if BOOK_RE.match(t):
            lines.append(f"\n## {t}  _({vp})_\n")
        elif DIVISION_RE.match(t):
            lines.append(f"\n## {t}  _({vp})_\n")
        elif PART_RE.match(t):
            lines.append(f"\n### {t}  _({vp})_\n")
        elif SECTION_RE.match(t):
            lines.append(f"- **{t}**  _({vp})_")
        elif SUBSECTION_RE.match(t):
            lines.append(f"  - {t}  _({vp})_")
    return "\n".join(lines) + "\n"


def build_tables(rows: list[dict]) -> str:
    lines = [
        "# VBBL 2025 — Table Index",
        "",
        "Every titled Table in the code with its volume + page number.",
        "Tables carry a lot of the code's decision-making weight (occupancy, construction",
        "type, spatial separation, fire-resistance ratings). Read the PDF page for the",
        "authoritative text.",
        "",
    ]
    seen = set()
    for r in rows:
        t = r["title"].strip()
        m = TABLE_RE.search(t)
        if not m:
            continue
        cite = m.group("cite").rstrip(".")
        key = (cite, t, r["volume"])
        if key in seen:
            continue
        seen.add(key)
        lines.append(f"- **Table {cite}** — {t}  _({vol_page(r)})_")
    return "\n".join(lines) + "\n"


def build_figures(rows: list[dict]) -> str:
    lines = [
        "# VBBL 2025 — Figure Index",
        "",
        "Every titled Figure in the code with its volume + page number.",
        "",
    ]
    seen = set()
    for r in rows:
        t = r["title"].strip()
        m = FIGURE_RE.search(t)
        if not m:
            continue
        cite = m.group("cite").rstrip(".")
        key = (cite, t, r["volume"])
        if key in seen:
            continue
        seen.add(key)
        lines.append(f"- **Figure {cite}** — {t}  _({vol_page(r)})_")
    return "\n".join(lines) + "\n"


def build_definitions(rows: list[dict]) -> str:
    """Extract defined-term bookmarks. VBBL puts defined terms under
    Division A Article 1.4.1. (Definitions of Words and Phrases)."""
    lines = [
        "# VBBL 2025 — Defined Terms",
        "",
        "Defined terms live in **Division A, Section 1.4 Terms and Abbreviations**,",
        "specifically Subsection 1.4.1. Definitions of Words and Phrases, starting",
        "at Vol 1 p.31. Notes to Part 1 (Vol 1 p.50+) expand on individual terms.",
        "Read the PDF page for the authoritative definition.",
        "",
        "## Outline hits",
        "",
    ]
    for r in rows:
        t = r["title"].strip()
        if r["volume"] != 1:
            continue
        # Match any 1.4 / 1.4.1 / 1.4.1.x style reference under Division A.
        if (t.startswith("1.4.") or "Terms and Abbreviations" in t
                or "Definitions of Words and Phrases" in t):
            lines.append(f"- **{t}**  _({vol_page(r)})_")
    return "\n".join(lines) + "\n"


def main() -> int:
    rows = load_rows()
    MAP_MD.write_text(build_map(rows))
    TABLES_MD.write_text(build_tables(rows))
    FIGURES_MD.write_text(build_figures(rows))
    DEFINITIONS_MD.write_text(build_definitions(rows))
    print("Wrote:")
    for p in (MAP_MD, TABLES_MD, FIGURES_MD, DEFINITIONS_MD):
        print(f"  {p.relative_to(SKILL_DIR)} ({p.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
