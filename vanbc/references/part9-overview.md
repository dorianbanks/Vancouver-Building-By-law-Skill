# Workflow — Part 9 (Housing and Small Buildings)

**When to use this guide:** single-family houses, duplexes, small multi-family, small commercial (≤ 600 m² building area, ≤ 3 storeys). Also secondary suites, laneway houses, and other small infill.

Part 9 lives entirely in **Volume 2** of the VBBL 2025 (Vol 2 p.7–414 for the main text, plus fire/sound tables at Vol 2 p.415+ and span tables at Vol 2 p.522+).

## Scope test (Division A, Article 1.3.3.3.)

Part 9 applies if **all** of the following are true:
- Building ≤ 3 storeys in building height, **and**
- Building area ≤ 600 m², **and**
- Major occupancies limited to Group C (residential), D (business), E (mercantile), or F-2 / F-3 (medium-/low-hazard industrial), **and**
- Not a post-disaster building, not a high building.

If any one fails, Part 3 applies. Watch for:
- **Any Group A or B major occupancy** (including daycare in many cases) → Part 3.
- **Mid-rise mass timber residential** → Part 3 (EMTC lives in Subsection 3.1.6).
- **Mixed occupancies that include F-1** → Part 3.

## Part 9 section map (Vol 2)

| Section | Topic | Vol 2 p. |
|---|---|---|
| **9.1** | General / application | 7 |
| **9.2** | Definitions | 7 |
| **9.3** | Materials, systems and equipment (concrete, lumber, metal) | 7 |
| **9.4** | Structural requirements (loads, deflections, foundations) | 12 |
| **9.5** | Design of areas and spaces (accessible design, ceiling heights, hallways, doorways) | 15 |
| **9.6** | Glass | 18 |
| **9.7** | Windows, doors and skylights | 19 |
| **9.8** | Stairs, ramps, landings, handrails and guards | 23 |
| **9.9** | Means of egress | 34 |
| **9.10** | Fire protection (occupancy, ratings, construction, fire separations, firewalls, spatial separation, smoke alarms, firefighting) | 45 |
| **9.11** | Sound transmission | 81 |
| **9.12** | Excavation | 83 |
| **9.13** | Dampproofing, waterproofing, soil gas control | 85 |
| **9.14** | Drainage | 90 |
| **9.15** | Footings and foundations | 92 |
| **9.16** | Floors-on-ground | 100 |
| **9.17** | Columns | 101 |
| **9.18** | Crawl spaces | 103 |
| **9.19** | Roof spaces | 105 |
| **9.20** | Masonry and ICF walls not in contact with ground | 106 |
| **9.21** | Masonry and concrete chimneys and flues | 119 |
| **9.22** | Fireplaces | 123 |
| **9.23** | Wood-frame construction (bread-and-butter section) | 125 |
| **9.24** | Sheet steel stud wall framing | 175 |
| **9.25** | Heat transfer, air leakage and condensation control | 178 |
| **9.26** | Roofing | 183 |
| **9.27** | Cladding | 193 |
| **9.28** | Stucco | 205 |
| **9.29** | Interior wall and ceiling finishes | 208 |
| **9.30** | Flooring | 214 |
| **9.31** | Plumbing facilities | 216 |
| **9.32** | Ventilation | 218 |
| **9.33** | Heating and air-conditioning | 226 |
| **9.34** | Electrical facilities | 235 |
| **9.35** | Garages and carports | 237 |
| 9.36 | Deleted | — |
| 9.37 | Deleted | — |
| **9.38** | Objectives and Functional Statements | 239 |
| **Fire & Sound Resistance Tables** | Tabulated assemblies for Part 9 use | 415 |
| **Span Tables** | Joist, rafter, beam span tables | 522 |

**Note on 9.36 / 9.37:** These are marked "Deleted" in VBBL 2025 — the BCBC's energy (9.36) and secondary-suite (9.37) sections aren't present here. In the VBBL, **energy and water efficiency live in Part 10** (Vol 1 p.805+), and secondary-suite / laneway-house provisions are handled through Part 9's general dwelling-unit provisions combined with Part 10 energy requirements and Part 11 alternative compliance measures. Always read Part 11 when you're adding or converting a suite in an existing building.

## Common Part 9 question shapes

- **Stair and guard dimensions** — Section 9.8 (Vol 2 p.23–33). Step dimensions at 9.8.4 (Vol 2 p.25). Handrails at 9.8.7 (Vol 2 p.28). Guards at 9.8.8 (Vol 2 p.30).
- **Means of egress** — Section 9.9. Egress from dwelling units at 9.9.9 (Vol 2 p.42). Egress from bedrooms at 9.9.10 (Vol 2 p.43).
- **Smoke alarms and CO alarms** — 9.10.19 (Vol 2 p.76).
- **Spatial separation between buildings / between houses** — 9.10.14 (Vol 2 p.61) and 9.10.15 (Vol 2 p.67).
- **Firewalls between dwelling units** (row housing, secondary suites) — 9.10.11 (Vol 2 p.58).
- **Ceiling heights and room sizes** — Section 9.5 (Vol 2 p.15).
- **Wood-frame prescriptive details** — Section 9.23 (Vol 2 p.125+) and span tables at Vol 2 p.522+.
- **Energy / envelope** — VBBL Part 9 defers to **Part 10 Energy and Water Efficiency** (Vol 1 p.805+). Don't expect a 9.36 energy section.

## Vancouver-specific notes

- **Secondary suites and laneway houses** are common in Vancouver but the VBBL doesn't bookmark them as dedicated sections. Treat the additional suite as a second dwelling unit, apply the fire-separation, egress, ventilation, and smoke-alarm rules in Section 9.10 and Section 9.9, and cross-check against **Part 11** for any existing-building alternative compliance measures (Vol 1 p.834+).
- **Heritage buildings** — if the house has heritage status, Part 11 Section 11.4 (Vol 1 p.857) provides alternative compliance measures.
- **Zoning** (floor area ratio, density, setbacks, permitted uses for laneway/secondary suites) lives in the Zoning and Development By-law, **not** the VBBL. Say so when a user conflates the two.

## Pull the authoritative text

```
python3 scripts/lookup.py 9.8.4                  # Step dimensions (Vol 2)
python3 scripts/lookup.py 9.9.10                 # Egress from bedrooms
python3 scripts/lookup.py 9.10.15                # Spatial separation between houses
python3 scripts/lookup.py 9.10.19                # Smoke alarms
python3 scripts/lookup.py --search "dwelling" --volume 2
```

Always end with: *"Part 9 includes many prescriptive values (stair risers, window sizes, joist spans) that should be confirmed against the current article before construction. The City of Vancouver may add requirements beyond Part 9 through bulletins, Part 10 (energy), or Part 11 (existing/heritage)."*
