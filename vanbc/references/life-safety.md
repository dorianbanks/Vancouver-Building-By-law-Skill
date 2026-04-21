# Workflow — Fire & Life Safety / Egress (VBBL)

**When to use this guide:** questions about occupant load, travel distance, exits, fire separations, fire-resistance ratings, sprinkler trade-offs, corridor widths, dead-end limits, stair pressurization.

Most life-safety provisions live in **Vol 1, Part 3**:
- Subsection 3.1.7. Fire-Resistance Ratings (Vol 1 p.151)
- Subsection 3.1.8. Fire Separations and Closures (Vol 1 p.151)
- Subsection 3.1.17. Occupant Load (Vol 1 p.171)
- Subsection 3.2.3. Spatial Separation and Exposure Protection (Vol 1 p.213)
- Subsection 3.2.4. Fire Alarm and Detection Systems (Vol 1 p.228)
- Subsection 3.2.5. Provisions for Firefighting (Vol 1 p.241)
- Section 3.3. Safety within Floor Areas (Vol 1 p.262)
- Section 3.4. Exits (Vol 1 p.289)

Part 9 mirrors a simpler version in Vol 2 Section 9.9 (egress) and Section 9.10 (fire protection).

## Occupant load (Subsection 3.1.17.)

Occupant load drives exit sizing, number of exits, and plumbing fixture count. Occupant load per m² varies by use — see Subsection 3.1.17 at Vol 1 p.171, and the accompanying Table within that Subsection.

Order-of-magnitude figures (always verify against the actual Table):

| Use | Typical load |
|---|---|
| Assembly, fixed seats | 1 / seat |
| Assembly, standing / dining | ~0.75–1.2 m² / person |
| Classroom | ~1.85 m² / person |
| Office | ~9.3 m² / person |
| Mercantile, ground floor | ~3.7 m² / person |
| Residential | 2 persons per sleeping room |
| Industrial storage | ~28 m² / person (higher density for manufacturing) |

## Exits — number and width (Section 3.4)

Section 3.4 Exits starts at Vol 1 p.289.

- **Minimum two exits** from a floor area in nearly all cases.
- **Remoteness** — exits must be spaced to meet the diagonal test.
- **Exit width** — based on occupant load and whether the building is sprinklered; sprinklered buildings use reduced width factors.
- **Exit stairs** — minimum dimensions and a rated fire separation from the rest of the building.

## Travel distance

Travel distance limits live within Section 3.4 (Vol 1 p.289+). The 2025 VBBL outline doesn't bookmark "travel distance" as a separate heading, so read through Section 3.4 for the applicable Subsection. Sprinklering generally extends the allowed distance materially.

## Dead-end corridors

Dead-end limits apply in public corridors serving more than one suite. Live in Section 3.3 Safety within Floor Areas (Vol 1 p.262). Sprinklered buildings get more permissive limits.

## Fire separations, firewalls, closures

| Concept | Where | What it does |
|---|---|---|
| **Fire separation** | 3.1.8 (Vol 1 p.151); Part 9: 9.10.9 (Vol 2 p.51) | Assembly that resists the passage of flame; may or may not have a fire-resistance rating |
| **Fire-resistance rating** | 3.1.7 (Vol 1 p.151); Part 9: 9.10.3 (Vol 2 p.47) | Time rating (45 min, 1 h, 2 h, etc.) from a standard test |
| **Firewall** | 3.1.10 (Vol 1 p.162); Part 9: 9.10.11 (Vol 2 p.58) | Separates "buildings" from a code standpoint — continuous, structurally independent |
| **Closure** | 3.1.8 (Vol 1 p.151); Part 9: 9.10.13 (Vol 2 p.59) | Doors, dampers, shutters in fire separations — rated closures |
| **Penetrations** | 3.1.9 (Vol 1 p.159) | Firestopping at service penetrations |

**Appendix D** (Vol 1 p.923+) has fire-performance rating tables, assembly lists, and background on rating derivation.

## Spatial separation and exposing building face

- **Part 3**: Subsection 3.2.3 (Vol 1 p.213).
- **Part 9**: 9.10.14 (between buildings — Vol 2 p.61) and 9.10.15 (between houses — Vol 2 p.67).

Drives limiting distance, percent glazing permitted, fire-resistance rating of exterior wall, combustibility of cladding. Read the Subsection thoroughly — the sprinklered vs unsprinklered tables are pivotal.

## Fire alarms and detection

- **Part 3**: Subsection 3.2.4 (Vol 1 p.228).
- **Part 9**: 9.10.18 (Vol 2 p.74) for alarm and detection, 9.10.19 (Vol 2 p.76) for smoke alarms.
- High buildings carry additional voice-communication requirements — Subsection 3.2.6 (Vol 1 p.250).

## Sprinklers — trade-offs

Sprinklering unlocks trade-offs throughout the code:

- Increased building area and height allowances (Subsection 3.2.2, Vol 1 p.177+).
- Reduced fire-resistance ratings in some assemblies.
- Longer travel distance (Section 3.4).
- Larger dead-end corridors (Section 3.3).
- Reduced spatial-separation glazing restrictions (3.2.3).
- Required in almost all EMTC buildings and most Group C buildings over 3 storeys.

System requirements and NFPA references live in Subsection 3.2.5 (Vol 1 p.241).

## Accessibility interacts with life safety

Section 3.8 Accessibility (Vol 1 p.327). Relevant to egress:

- Accessible means of egress
- Areas of refuge
- Wheelchair-accessible washrooms, doors, routes
- **3.8.5 Adaptable Dwelling Units** (Vol 1 p.347) — Vancouver-specific strengthened provisions.

## Pull the authoritative text

```
python3 scripts/lookup.py 3.1.17                 # Occupant load (Vol 1 p.171)
python3 scripts/lookup.py 3.4                    # Exits (Vol 1 p.289)
python3 scripts/lookup.py 3.2.3                  # Spatial separation (Vol 1 p.213)
python3 scripts/lookup.py 3.2.5                  # Sprinklers / firefighting (Vol 1 p.241)
python3 scripts/lookup.py 9.10.15                # Spatial separation between houses (Vol 2 p.67)
python3 scripts/lookup.py --search "fire alarm"
```

Always end with: *"Life-safety calculations (occupant load, exit width, travel distance) should be confirmed by a code consultant and reviewed by the City of Vancouver. Prescriptive values in this guide are for orientation only — always read the current article."*
