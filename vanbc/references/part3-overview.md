# Workflow — Part 3 (Fire Protection, Occupant Safety and Accessibility)

**When to use this guide:** the user is working on a building that falls under Part 3 — anything that isn't Part 9 — and asks about construction type, fire separations, egress, sprinklers, mass timber, or high-building provisions.

Part 3 is the largest and most-cited part of the VBBL for architects working on commercial, institutional, and mid/high-rise residential projects. It lives in **Volume 1, Division B** (Vol 1 p.124–512).

## Part 3 vs Part 9 — which applies?

Read **Division A, Article 1.3.3.3.** (Application of Division B) — `python3 scripts/lookup.py 1.3.3`.

Part 9 applies only if **all** of the following are true:
- Building ≤ 3 storeys in building height, **and**
- Building area ≤ 600 m², **and**
- Major occupancies limited to Group C, D, E, F-2, or F-3, **and**
- Not a post-disaster building, not a high building.

Anything outside those limits goes to Part 3. When in doubt, Part 3 applies.

## Part 3 map (Vol 1)

| Section | Topic | Vol 1 p. |
|---|---|---|
| **3.1** | General (combustible/non-combustible/EMTC construction, fire-resistance ratings, fire separations, interior finish, occupant load) | 124 |
| **3.2** | Building fire safety (size & construction by occupancy, spatial separation, alarm, firefighting, high buildings, lighting) | 174 |
| **3.3** | Safety within floor areas (suite separations, corridors, egress within suites) | 262 |
| **3.4** | Exits (number, width, separation, travel distance, stair dimensions) | 289 |
| **3.5** | Vertical transportation | 311 |
| **3.6** | Service facilities | 313 |
| **3.7** | Health requirements (washrooms, etc.) | 322 |
| **3.8** | Accessibility (including **3.8.5 Adaptable Dwelling Units** at Vol 1 p.347) | 327 |
| **3.9** | Self-service storage buildings | 349 |
| **3.10** | Objectives and Functional Statements | 351 |

## Core decision: construction type matrix (Subsection 3.2.2)

Subsection **3.2.2. Building Size and Construction Relative to Occupancy** (Vol 1 p.177) is the heart of Part 3. For each combination of **major occupancy + number of storeys + building area + sprinklered/unsprinklered**, the code specifies:

- **Combustible** / **non-combustible** / **encapsulated mass timber (EMTC)** construction permitted
- **Fire-resistance ratings** of floor assemblies, mezzanines, roof assemblies, loadbearing supports
- **Sprinklering** requirement (often makes the difference between a trade-up and a trade-down)

The VBBL 2025 outline bookmarks 3.2.2 at the Subsection level — the individual occupancy Articles (3.2.2.x) live on the pages following p.177. Use `lookup.py 3.2.2` to jump there, then read 20–40 pages forward to find the Article for your occupancy and sprinklering status.

## Encapsulated Mass Timber Construction (EMTC)

VBBL 2025 recognizes EMTC as a distinct construction type — see **Subsection 3.1.6. Encapsulated Mass Timber Construction** (Vol 1 p.143). Key constraints live in 3.1.6 (encapsulation ratings, exposed mass timber limits) and the per-occupancy articles in 3.2.2.

`python3 scripts/lookup.py 3.1.6` and `python3 scripts/lookup.py --search "mass timber"`.

## Spatial separation and exposing building face

**Subsection 3.2.3. Spatial Separation and Exposure Protection** (Vol 1 p.213). Drives **limiting distance**, **percent glazing permitted**, **fire-resistance rating of exterior wall**, **combustibility of cladding**. Read the full Subsection — the sprinklered vs unsprinklered tables are pivotal.

## Exits (Section 3.4)

**Section 3.4. Exits** starts at Vol 1 p.289. You'll reach for this for:
- Minimum number of exits from a floor area
- Remoteness (diagonal rule)
- Exit width based on occupant load and sprinklering
- Travel distance limits by occupancy and sprinklering
- Exit stair dimensions and fire separation

## High buildings (Subsection 3.2.6)

**Subsection 3.2.6. Additional Requirements for High Buildings** (Vol 1 p.250). Triggered by height / storey-count thresholds. Triggers: mechanical smoke control, emergency power, voice communication, firefighter elevators, two-way communication, enhanced fire-fighting access.

## Post-disaster building

Defined in Division A, Section 1.4 (Vol 1 p.31). Drives seismic importance category, redundancy, sometimes construction type. Cross-reference Part 4 (Structural) — Section 4.1 starts at Vol 1 p.513.

## Vancouver-specific notes

- **Accessibility is in Section 3.8** — Vancouver has layered provisions here, including **3.8.5 Adaptable Dwelling Units** (Vol 1 p.347). The City's adaptable/visitable unit requirements are stricter than the BCBC in some respects — read the PDF, don't pattern-match from BCBC memory.
- **Self-service storage** has its own Section 3.9 (Vol 1 p.349).
- **Appendix D (Vol 1 p.923+)** contains fire-performance ratings and assembly lists — `python3 scripts/lookup.py --search "Appendix D"` or jump directly to Vol 1 p.923.

## Pull the authoritative text

```
python3 scripts/lookup.py 3.1.6                  # EMTC
python3 scripts/lookup.py 3.2.2                  # building size/construction by occupancy (Vol 1 p.177)
python3 scripts/lookup.py 3.2.3                  # spatial separation
python3 scripts/lookup.py 3.2.6                  # high buildings
python3 scripts/lookup.py 3.4                    # exits
python3 scripts/lookup.py 3.8                    # accessibility
python3 scripts/lookup.py --search "firewall"
```

Always end with: *"Construction type and life-safety decisions should be confirmed with a code consultant and the City of Vancouver. The 2025 VBBL revised several thresholds (EMTC, energy, accessibility) — verify against the current article, not memory."*
