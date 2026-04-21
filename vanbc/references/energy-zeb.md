# Workflow — Part 10 Energy and Water Efficiency (Zero Emissions Building Plan)

**When to use this guide:** questions about energy performance, EV charging, embodied carbon, low-carbon materials, Zero Emissions Building Plan (ZEB) requirements, or compliance paths for energy efficiency.

Part 10 lives in **Volume 1** (Vol 1 p.805–833). It's one of the most Vancouver-specific parts of the VBBL — the City layers in its Zero Emissions Building Plan targets and low-carbon construction requirements on top of (and often stricter than) the BC Energy Step Code and BCBC Section 9.36/NECB.

## Part 10 section map

| Section | Topic | Vol 1 p. |
|---|---|---|
| **10.1** | General (application, scope, references) | 805 |
| **10.2** | Energy Efficiency | 805 |
| **10.3** | Electric Vehicle Charging | 821 |
| **10.4** | Low Carbon Materials and Construction | 821 |
| **10.5** | Objectives and Functional Statements | 821 |
| **Notes to Part 10** | Appendix notes / explanatory material | 824 |

Read Section 10.1 first to understand application — thresholds, exemptions, and interactions with the ASHRAE, NECB, and Energy Step Code references are all there.

## Vancouver's Zero Emissions Building Plan layering

Three levers work together:

1. **Energy efficiency** (Section 10.2) — thermal energy demand intensity (TEDI), total energy use intensity (TEUI), envelope performance, mechanical efficiency targets. Compliance is often through referenced standards (NECB / ASHRAE / Energy Step Code) with Vancouver-specific tightened targets.
2. **EV charging** (Section 10.3) — readiness rates per parking stall for residential and non-residential, load-management allowances.
3. **Low-carbon materials** (Section 10.4) — embodied-carbon limits or reporting for structural materials, cement/concrete mix requirements.

## Interaction with other parts

- **Part 5 (Environmental Separation)** — Vol 1 p.659+ — handles the envelope performance requirements (thermal, air, moisture) on the physical side; Part 10 sets the *performance target*.
- **Part 6 (HVAC)** — Vol 1 p.709+ — handles mechanical system design; Part 10 sets the *efficiency requirement*.
- **Part 7 (Plumbing)** — Vol 1 p.742+ — handles plumbing fixtures; Part 10 handles water-efficiency targets.
- **Part 9** — for Part-9-eligible buildings, Part 10 applies in addition to Part 9. The old BCBC Section 9.36 / 9.37 energy pattern doesn't exist in the VBBL; Part 10 is the one stop for energy.
- **Part 11 (Existing Buildings)** — Vol 1 p.834+ — has alternative compliance measures for energy retrofits in existing buildings; renovations don't always trigger full Part 10 compliance.

## Common question shapes

- **"What TEDI do I need to hit?"** — Section 10.2, look up the occupancy and building type; the target varies and has a phased implementation schedule. Read the notes at Vol 1 p.824+ for rationale.
- **"How many EV-ready stalls?"** — Section 10.3 (Vol 1 p.821). Residential and non-residential have different rates.
- **"Can I use this concrete mix?"** — Section 10.4 (Vol 1 p.821). Low-carbon materials provisions may require supplementary cementitious materials or cap the global warming potential of the mix.
- **"Does a reno trigger all of Part 10?"** — check Part 11 alternative compliance first (Vol 1 p.834+), then Section 10.1 application.

## Vancouver-specific notes

- The ZEB targets evolve — the VBBL 2025 reflects the current schedule, but check City of Vancouver energy bulletins for updates since publication.
- Modelling and compliance documentation are usually required at permit application; the City may require an energy advisor or mechanical engineer to sign off. Flag this when a user asks "how do I show I comply".
- Some project types (e.g. heritage, small renovations) may have carve-outs — always read 10.1 application first before assuming Part 10 applies in full.

## Pull the authoritative text

```
python3 scripts/lookup.py 10.1                   # General application (Vol 1 p.805)
python3 scripts/lookup.py 10.2                   # Energy Efficiency (Vol 1 p.805)
python3 scripts/lookup.py 10.3                   # EV charging (Vol 1 p.821)
python3 scripts/lookup.py 10.4                   # Low Carbon Materials (Vol 1 p.821)
python3 scripts/lookup.py --search "energy"
```

Always end with: *"Part 10 is actively evolving; confirm current targets, phased dates, and compliance path with the City of Vancouver and your energy modeller or sustainability consultant before finalizing design."*
