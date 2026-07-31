# Project scope

Date: 31 July 2026. Owner: Jeremy Levitt. Build partner: Luigi Pacelli.

## What this project is

Antipode Motor Co., a proposed Australian house building bespoke Porsche 911 restomods on 1979 to 1985 G-body donors (911 SC and early 3.2 Carrera), operating from Luigi Pacelli's Artarmon workshop in Sydney, with a launch commission price of A$975,000 ex-donor, since revised to a two-tier ladder (see `decisions/ADR-0005`).

The venture is at the scoping stage. No entity exists, no name is cleared, no car is committed. This repository holds the scoping work, the financial model, and the brand and web assets.

## What this project is not, yet

Not a decision to build cars. `docs/02-strategy-decision.md` sets out why the build commitment sits behind a gate, and what has to be true to clear it. Everything in Phase 0 is deliberately reversible.

## Pricing

Recommended: two tiers, both ex-donor and ex-GST. **Foundation A$975,000** and **Signature A$1,150,000**, at 34.9% and 37.1% gross margin respectively. A third concept proposed an A$850,000 entry tier; it is rejected on positioning rather than margin, because it sits A$10,000 below Theon Design's full carbon-bodied car. Reasoning in `decisions/ADR-0005`, arithmetic in `model/output.md` section 10.

Neither figure is published on the site. Commissions at this level are quoted on application.

Both prices are contingent on the labour-rate question (`decisions/ADR-0003`) and the LCT ruling (`decisions/ADR-0004`). If either lands badly, the ladder is re-derived before it is quoted.

## The strategy in one paragraph

Adopt the atelier as the destination and the advisory business as the path. Clear the cheap questions first (trademark, tax ruling, certifier, quotes, entity), stand up donor brokerage and advisory to earn revenue and sense demand, then commit to a single instrumented build only once a paid foundation commission is banked. Ramp to volume only after car one is delivered, certified, and its real hours are known.

## Workstreams

| # | Workstream | Owner | Phase 0 deliverable |
|---|---|---|---|
| W1 | Brand, name and IP clearance | Jeremy | Class 12 and 37 clearance, domains, ASIC name |
| W2 | Entity, equity and services agreement | Both | Term sheet with the labour rate settled |
| W3 | Tax and regulatory | Jeremy + advisers | ATO private ruling lodged, VSCCS certifier retained |
| W4 | Capability gaps (paint, panel, trim, design) | Luigi | Three written quotes per discipline, design authority engaged |
| W5 | Financial model and cost validation | Jeremy | Assumption lines replaced with real quotes |
| W6 | Demand generation and web | Jeremy | Site live, PR wave briefed, waitlist open |
| W7 | Donor desk and advisory | Jeremy | First sourcing mandates, inspection partner signed |
| W8 | Build one | Luigi | Not in Phase 0. Behind Gate 1. |

## Phases and gates

**Phase 0, weeks 1 to 12.** Clearance and foundations. W1 through W6. No manufacturing spend. Nothing here commits the founders to building.

**Phase 1, weeks 6 to 26, overlapping Phase 0.** W7 live, earning revenue. Launch PR against renders and the brand. Waitlist converting to deposits.

**Gate 1, target month 9.** Commit to build one. Requires all four:
1. One signed foundation commission with a cleared A$100,000 deposit.
2. Favourable LCT ruling, or a contingency the founders have explicitly priced and accepted.
3. VSCCS certifier engaged, covering every modification code the build needs.
4. Paint, panel and trim quoted in writing, inside the modelled A$105,000 combined.

**Phase 2.** Build car one as an instrumented prototype. Time every stage against the 3,000-hour assumption. Capture the build journal from day one.

**Gate 2.** Commit to volume. Requires car one delivered and certified, actual hours known and modelled, and a second paid commission banked.

## Definition of done for Phase 0

Phase 0 is complete when every row in `docs/07-open-questions.md` marked "blocks Gate 1" is closed, the model's assumption lines carry real quotes, and the founders have signed a term sheet in which the equity split and the services-agreement labour rate are set together in one document.

## Product definition, carried from Plan A

Donor 1979 to 1985 911 SC or 3.2 Carrera, galvanised G-body shell retained and repaired, never replaced. Rebuilt air-cooled flat-six, 210 to 260 kW, tuned for mid-range torque rather than peak. Pressure-fed timing-chain tensioners replacing the pre-1984 non-pressure-fed design, pop-off valve for the CIS airbox, sprung clutch centre, attention to Dilavar head studs and ageing oil lines. Five-speed 915 manual. Uprated brakes and suspension specified for coarse-chip roads. 17 to 18 inch Fuchs-style forged wheels. Subtle widebody, arches flared 25 to 40 mm. Leather cabin, concealed modern audio, no screens. Full NSW VSCCS certification.

Positioning: engineered for Australian heat, dust and distance rather than European roads. Restraint over aggression. Do not chase Zeigler/Bailey's billet 4.4-litre engine programme.

## Out of scope

- Any second model line or platform (964, 993, Turbo bodies).
- Electric conversions. Plan B notes the segment is growing and that Everrati has proven it, but it splits the brand and the buyer, and the air-cooled purist market is the one being addressed here.
- Export to the United States. Real, and the 25-year exemption covers the donors, but it is a year-two question and adds compliance and logistics load the venture cannot carry in Phase 0.
- Building or leasing a dedicated facility. The whole cost advantage is that the workshop already exists.
- Replacing the tub, seam-welding to a new structure, or anything else that risks Individually Constructed Vehicle reclassification. See `docs/03-regulatory-and-tax.md`.

## Repository map

```
README.md                      Orientation and current status
docs/
  01-scope.md                  This file
  02-strategy-decision.md      Reconciliation of the two source plans
  03-regulatory-and-tax.md     NSW certification, LCT, ICV, imports, ACL, trademark
  04-brand-clearance.md        Name clearance checklist and fallback
  05-risk-register.md          Merged register with owners
  06-90-day-plan.md            Dated plan to 29 October 2026
  07-open-questions.md         Blocker register, gated
  08-concept-review.md         Third concept: what to adopt and what to reject
decisions/
  ADR-0001  Staged commitment (atelier destination, advisory path)
  ADR-0002  G-body donor choice
  ADR-0003  Equity split and labour rate settled together  [blocks Gate 1]
  ADR-0004  ATO private ruling on LCT                       [blocks Gate 1]
  ADR-0005  Two commission tiers, not one and not three
model/
  model.mjs                    Runnable unit economics and sensitivity model
  output.md                    Generated report, committed
  README.md                    How to run and extend it
web/
  index.html                   Homepage, built to Plan A's content spec
  styles.css                   Charcoal / bone / ochre-red, no dependencies
  build-images.py              Regenerates web derivatives from the masters
  ASSET-CLEARANCE.md           Why no render is publishable yet
  README.md
reference/
  plan-a-atelier.md            Source plan, verbatim
  plan-b-investor-grade.md     Source plan, verbatim
  kimi-hinterland-concept.html Third concept, verbatim
```

## Source documents

All three source documents are committed verbatim to `reference/` so that every claim in this repository can be traced. Where they disagree, `docs/02-strategy-decision.md` records which was adopted and why for the two business plans, and `docs/08-concept-review.md` does the same for the third concept.
