# Workflow — Occupancy Classification (VBBL)

**When to use this guide:** the user describes a building or space ("a 1,200 m² daycare", "a warehouse with a small office") and needs the major occupancy group, or they're trying to figure out mixed-use implications.

Authoritative text lives in **Division B, Subsection 3.1.2. Classification of Buildings or Parts of Buildings by Major Occupancy** (Vol 1 p.124) and **Subsection 3.1.3. Multiple Occupancy Requirements** (Vol 1 p.126). Read the PDF. This file is a navigation + mental-model aid, not a substitute.

## The six major occupancy groups

| Group | Title | Typical uses |
|---|---|---|
| **A** | Assembly | Restaurants, theatres, churches, schools, museums, gyms, arenas |
| **B** | Care, treatment, or detention | Hospitals, long-term care, daycare (care), jails, group homes |
| **C** | Residential | Houses, apartments, hotels, dormitories |
| **D** | Business & personal services | Offices, banks, clinics (outpatient), barber shops |
| **E** | Mercantile | Retail stores, shopping centres, markets |
| **F** | Industrial | Factories, warehouses, labs, garages |

Each group has divisions (A-1 through A-4, B-1/B-2/B-3, C, D, E, F-1/F-2/F-3) — the divisions matter a lot, since they drive construction-type requirements and fire load. See **Article 3.1.2.1.** in the PDF.

## Workflow

1. **Start with Article 3.1.2.1.** — `python3 scripts/lookup.py 3.1.2` then read from Vol 1 p.124.
2. **Identify the major occupancy** — the principal use of the building or fire compartment. Don't over-index on ancillary spaces.
3. **Check for multiple major occupancies** — see **Subsection 3.1.3. Multiple Occupancy Requirements** (Vol 1 p.126). This drives whether the building must be separated by fire separations with specific ratings, or designed to the most restrictive occupancy.
4. **Check subsidiary / ancillary uses** — a subsidiary occupancy below certain thresholds does not trigger mixed-use complexity. Read the specific articles in Subsection 3.1.2.
5. **Industrial hazard levels** — F-1 (high-hazard), F-2 (medium-hazard), F-3 (low-hazard). Driven by the flammability / combustibility of contents, not the building type alone.
6. **Care vs assembly nuances** — whether a specific use (daycare, small group home, adult-day-program) is Group A or Group B can flip the whole design. Read the defined terms in Division A, Section 1.4 (Vol 1 p.31) and the classification articles carefully; the City of Vancouver's written interpretations sometimes differ from how other BC jurisdictions read the same text.

## Common traps

- **Daycare classification** — a daycare facility for children has specific classification rules. Don't assume "daycare = Group B"; read the specific article in Subsection 3.1.2 and any related appendix note. Different types of daycare (hours, overnight, children's ages) may land in different groups.
- **Offices inside industrial buildings** — usually subsidiary unless they're large enough to count as a major occupancy on their own.
- **Live/work units** — if a dwelling unit is subsidiary to the business use (or vice versa), check the specific subsidiary-occupancy article.
- **Restaurants** — A-2 typically; but a small café inside a retail store (E) may be subsidiary.
- **Clinics** — outpatient medical is D; treatment with overnight stay is B.
- **Group A or B triggers Part 3 automatically.** If a Group A or B use is added to a building that was previously Part-9-eligible (C/D/E/F-2/F-3 only), the whole building moves to Part 3. Part 9 is not available when any major occupancy is Group A, B, or F-1 (Division A, Article 1.3.3.3.).

## Vancouver-specific notes

- Part 11 (Existing Buildings) has **alternative compliance measures for conversions** — e.g. Article **11.2.2.** governs conversion of a small existing residential building into a Community Care Facility, Group Residence, or Daycare (Vol 1 p.837). If your project is a change-of-use in an existing building, read Part 11 before designing to the new-construction rules.
- The City of Vancouver's Building Review & Permits staff publish written bulletins that clarify their approach to edge cases — those bulletins aren't in this skill, but they're on the City website. Flag to the user when a call looks close.

## Pull the authoritative text

```
python3 scripts/lookup.py 3.1.2                # Subsection: Classification by Major Occupancy (Vol 1 p.124)
python3 scripts/lookup.py 3.1.3                # Subsection: Multiple Occupancy Requirements (Vol 1 p.126)
python3 scripts/lookup.py --search "occupancy" --volume 1
```

Always end with: *"Classification should be confirmed with the City of Vancouver Building Review & Permits and your code consultant before relying on it for a permit submission."*
