# Workflow — Part 11 Existing Buildings (Alternative Compliance, Heritage, Upgrades)

**When to use this guide:** renovations, additions, change-of-use, conversions, heritage buildings, upgrade triggers, or questions framed as "do I have to bring the whole building up to the new code?"

Part 11 lives in **Volume 1** (Vol 1 p.834–892). It is one of the VBBL's most Vancouver-specific parts and one of the most cited in practice — most projects in Vancouver touch an existing building.

## Part 11 section map

| Section | Topic | Vol 1 p. |
|---|---|---|
| **11.1** | General | 834 |
| **11.2** | Alternative Compliance Measures for the Conversion of Existing Buildings | 837 |
| **11.3** | Alternative Compliance Measures for Existing Conditions to Assist Renovation | 843 |
| **11.4** | Alternative Compliance Measures for Heritage Buildings | 857 |
| **11.5** | Upgrade Mechanism | 864 |
| **Notes to Part 11** | Appendix notes / explanatory material | 872 |

## Core concept: three alternative-compliance regimes

Part 11 is organized around three distinct regimes — make sure you know which one applies:

1. **Section 11.2 — Conversions.** Change of use or occupancy in an existing building (e.g. a house converted to a community care facility, office to residential). Named article to know: **11.2.2.** Conversion of an Existing Residential Building Containing Not More Than Two Principal Dwelling Units into a Community Care Facility, Group Residence or Daycare Facility for Children (Vol 1 p.837).
2. **Section 11.3 — Renovations.** Alterations to existing buildings where strict code compliance would be impractical — provides alternatives to the new-construction requirements. Includes 11.3.8 Alternatives for Accessibility (Vol 1 p.856).
3. **Section 11.4 — Heritage buildings.** Additional alternative compliance measures for buildings with heritage designation. Significant overlap with 11.3, but heritage projects get extra latitude.

## The Upgrade Mechanism (Section 11.5)

**Section 11.5 Upgrade Mechanism** (Vol 1 p.864) is how the City determines what code upgrades are triggered by proposed work. This is the "do I have to do X because I'm doing Y?" framework. Read this Section carefully — the thresholds for triggering seismic upgrades, accessibility upgrades, fire-safety upgrades, and energy upgrades all live here.

## Common question shapes

- **"I'm doing a $X renovation — what do I have to bring up to code?"** — Read Section 11.5 first to identify which upgrade thresholds the work crosses, then apply the alternative-compliance measures in 11.3 (or 11.4 for heritage) to the triggered upgrades.
- **"Can I convert this duplex to a daycare?"** — Start with **11.2.2** (Vol 1 p.837).
- **"The building is heritage — do I still have to meet accessibility?"** — **11.4** (Vol 1 p.857) has the heritage alternative compliance; **11.3.8** (Vol 1 p.856) has accessibility alternatives applicable more broadly.
- **"I'm adding a secondary suite to an existing house."** — Part 9 provides the new-work rules; Part 11 (especially 11.3) provides the alternative compliance that lets existing conditions stay. Both apply.

## Interaction with other parts

- **Part 3, Part 9** — provide the target (new-construction) requirements. Part 11 is the exemption / alternative-path framework layered on top.
- **Part 10 (Energy)** — renovations don't always trigger full Part 10 compliance. Check 11.5 for the energy-upgrade threshold and 11.3 for the alternative compliance measures.
- **Part 4 (Structural)** — seismic upgrade triggers live in 11.5. Structural scope beyond that goes to Part 4 and the structural engineer of record.
- **Division C (Administration)** — permit process for alterations and changes of use lives in Division C Part 1 (Vol 1 p.971+).

## Vancouver-specific notes

- **Heritage designation** in Vancouver comes through the Heritage Register and specific designations — the VBBL defers to those determinations. Whether a building qualifies for 11.4 measures depends on its heritage status.
- The City publishes bulletins clarifying how 11.5's upgrade mechanism is applied in practice — for close calls (e.g. "is my renovation big enough to trigger a seismic upgrade?"), recommend the user request a pre-application review with the City.
- **Change of occupancy across Groups A/B** — always requires careful Part 11 analysis because the new occupancy may force construction-type, exits, accessibility, and energy upgrades. Expect this to be an AHJ conversation, not a prescriptive lookup.

## Pull the authoritative text

```
python3 scripts/lookup.py 11.1                   # General (Vol 1 p.834)
python3 scripts/lookup.py 11.2                   # Conversions (Vol 1 p.837)
python3 scripts/lookup.py 11.3                   # Renovations alternative compliance (Vol 1 p.843)
python3 scripts/lookup.py 11.4                   # Heritage (Vol 1 p.857)
python3 scripts/lookup.py 11.5                   # Upgrade mechanism (Vol 1 p.864)
python3 scripts/lookup.py --search "heritage"
python3 scripts/lookup.py --search "alteration"
```

Always end with: *"Part 11 determinations almost always involve interpretation — the City of Vancouver's Chief Building Official has significant discretion here. Get a pre-application meeting and a code consultant's written scope before committing to an alternative compliance approach."*
