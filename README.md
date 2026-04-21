# Vancouver Building By-law (VBBL 2025) — Claude Skill

A [Claude Skill](https://code.claude.com/docs/en/skills) that turns Claude
into a practitioner-grade reference for the **City of Vancouver Building
By-law, 2025 edition**. It bundles the full two-volume PDF set (Volume 1 —
Book I General, and Volume 2 — Part 9 Housing and Small Buildings), a
page-numbered citation index, and workflow guides for the questions
architects actually ask on Vancouver projects.

**Why a separate by-law?** Vancouver is the only municipality in BC with
authority to enact its own building by-law. Inside city limits, the VBBL
applies — not the BCBC. The two are closely aligned, but Vancouver layers
in the Zero Emissions Building Plan (Part 10), stricter envelope and
accessibility provisions, a heritage-building alternative compliance
mechanism (Part 11), and names the City's Chief Building Official as the
Authority Having Jurisdiction.

---

## What it does

Ask Claude a VBBL question in plain English — or by citation — and the
skill will:

1. **Route** the question to the right workflow guide (occupancy,
   Part 3, Part 9, life safety, Part 10 ZEB, Part 11 heritage).
2. **Resolve** any article you name (e.g. `3.2.2.47`, `10.2.3.1`) to a
   volume + PDF page via the bundled `lookup.py` script.
3. **Read the authoritative text** from the bundled VBBL PDFs — not a
   paraphrase.
4. **Quote and cite** in the standard form: *VBBL 2025, Vol. 1, Division
   B, Sentence 3.2.2.47.(1) (PDF p. 218)*.
5. **Add practitioner context** — VBBL-vs-BCBC deltas, ZEB compliance
   paths, heritage alternative compliance, coordination with the City.
6. **Close with the AHJ disclaimer.** Always. Binding determinations
   belong to the City of Vancouver Chief Building Official, not to
   Claude.

### Triggers on things like

- *"What's the Zero Emissions Building Plan compliance path for a Part 3
  office building?"*
- *"Does VBBL 2025 require adaptable dwelling units in a small apartment?"*
- *"Heritage building — how do I use the Part 11 alternative compliance
  mechanism?"*
- *"Spatial separation for an exposing building face on a Vancouver
  laneway site."*
- *"Part 9 stair dimensions in Vancouver — any deltas from BCBC?"*
- *"Is my project in VBBL or BCBC territory?"*

---

## Install

### Personal use (single machine)

1. Clone this repository.
2. Copy the `vanbc/` folder into your Claude skills directory:

   ```bash
   cp -R vanbc ~/.claude/skills/vanbc
   ```

3. Restart Claude Code. Run `/plugin list` and look for `vanbc`.

### Team / studio use

Every team member clones the repo and copies the `vanbc/` folder into
`~/.claude/skills/vanbc`. Pull to update. For Claude Team/Enterprise
plans with **Organization Settings → Add Skill**, zip the `vanbc/` folder
and upload:

```bash
cd vanbc && zip -r ../vanbc.zip . && cd ..
```

See [INSTALL.md](INSTALL.md) for details, project-scoped installs, and
size-limit workarounds.

---

## How to use it

Once installed, just ask — the skill auto-triggers on Vancouver / VBBL
questions.

```
> Does VBBL 2025 allow a 12-storey EMTC mass-timber building on a
  Broadway Plan site?

> Summarize Part 10 — Zero Emissions Building Plan.

> Stair width minimum for a secondary suite in Vancouver.

> Quote Sentence 3.2.2.47.(1).
```

---

## What's in the skill

```
vanbc/
├── SKILL.md                         # skill definition + operating instructions
├── assets/
│   ├── vbbl_2025_vol1.pdf           # Volume 1: Book I General — all Parts except Part 9
│   └── vbbl_2025_vol2.pdf           # Volume 2: Part 9 Housing and Small Buildings
├── references/
│   ├── index.md / index.json        # page-numbered outline with volume + page
│   ├── map.md                       # top-level structural map
│   ├── citations.json               # citation → {volume, page} lookup
│   ├── tables.md / figures.md       # tables and figures with volume + pages
│   ├── definitions.md               # defined-term index (Division A, Section 1.4)
│   ├── occupancy-classification.md  # workflow: Groups A–F, mixed use
│   ├── part3-overview.md            # workflow: construction type, EMTC, high buildings
│   ├── part9-overview.md            # workflow: houses & small buildings
│   ├── life-safety.md               # workflow: exits, egress, occupant load
│   ├── energy-zeb.md                # workflow: Part 10 Zero Emissions Building Plan
│   └── existing-heritage.md         # workflow: Part 11 alternative compliance
└── scripts/
    ├── lookup.py                    # citation → {volume, page} resolver + search
    ├── build_index.py               # regenerate index from new PDFs
    └── build_map.py                 # regenerate derived navigation files
```

---

## Scope & limits

- **VBBL 2025 only.** For projects outside City of Vancouver limits, use
  the **BCBC** — see the companion
  [British-Columbia-Building-Code-Skill](https://github.com/dorianbanks/British-Columbia-Building-Code-Skill).
- **Book I focus.** The bundled set is Book I (general — fire /
  structural / envelope / accessibility / energy / ZEB). Plumbing
  (Book II) is not included.
- **Not a code consultant.** Binding determinations — especially
  Alternative Solutions, heritage compliance, change-of-use, and
  ambiguous cases — belong to the City of Vancouver Chief Building
  Official and your code consultant.
- **Authoritative text wins.** Always verify by reading the cited PDF
  page before relying on an answer for a permit submission.

---

## Credits

Built by **Dorian Banks**. Released under the MIT License — see
[LICENSE](LICENSE).

The Vancouver Building By-law itself is published by the City of
Vancouver. This repository redistributes the 2025 by-law PDF set for
reference use inside the skill; consult the official source at
[vancouver.ca](https://vancouver.ca/home-property-development/vancouver-building-bylaw.aspx)
for authoritative and current versions.

---

## Disclaimer

This skill is a reference aid for licensed practitioners. It is not legal
advice, not a substitute for a code consultant, and not a substitute for
review by the City of Vancouver Chief Building Official. Always verify
against the official published by-law and confirm with the City before
relying on any output for a permit submission or construction.
