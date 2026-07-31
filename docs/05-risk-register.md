# Risk register

Merged from both source plans, with the model's findings added and owners assigned. Severity is judged on impact to the venture, not likelihood alone. Reviewed at each gate.

| ID | Risk | Severity | Owner | Mitigation | Status |
|---|---|---|---|---|---|
| R1 | Services-agreement labour rate set at market shop rate rather than internal cost, halving or eliminating margin | **Critical** | Jeremy + Luigi | Negotiate the equity split and the hourly rate as one trade in a single term sheet. Model both before signing (`model/output.md` s2) | Open, blocks Gate 1 |
| R2 | Build hours land near Theon's 6,000 rather than the assumed 3,000, making every car loss-making at A$975k | **Critical** | Luigi | Time car one by stage. Treat 3,000 as a target, not a cash-flow assumption. Do not price car two until car one's hours are known | Open, cannot close before Phase 2 |
| R3 | LCT applies to a re-manufactured classic: A$297,580 a car | **Critical** | Jeremy | ATO private binding ruling in Phase 0. Explicit contingency in the commissioning agreement until it lands | Open, blocks Gate 1 |
| R4 | Australian Consumer Law guarantee exposure. A major failure gives the buyer choice of repair, replacement or refund, and cannot be contracted out | High | Jeremy | Specific advice on which entity supplies the vehicle. Warranty reserve once estimable. No attempt to disclaim | Open. Absent from Plan A entirely |
| R5 | Key-person dependence on Luigi | High | Both | Founder vesting over four years, documented build processes, second senior technician trained early, key-person insurance, buy-sell provisions | Open |
| R6 | Capability gaps: paint, panel, trim, carbon, and no single design authority | High | Luigi | Contract specialists under Antipode quality control. Three written quotes each. Engage a design authority so cars share a signature | Open, blocks Gate 1 |
| R7 | No engineering signatory secured | High | Jeremy | VSCCS certifier on retainer before build one, licence confirmed across every modification code the build needs | Open, blocks Gate 1 |
| R8 | Capacity conflict between restomod builds and the existing service business | High | Luigi | Ring-fenced build bays and hours, separate scheduling board, separate P&Ls. Consider one car in year one rather than two | Open |
| R9 | Thin domestic buyer pool. Realistically low tens of buyers a year, against two local incumbents each targeting ten cars plus Singer via Zagame | High | Jeremy | Gate the build on a real cleared deposit. Donor desk and advisory as demand-sensing. Two-tier ladder to widen the funnel without discounting (`decisions/ADR-0005`). Export optionality from year two | Open, blocks Gate 1 |
| R10 | ICV reclassification if the tub is replaced | Medium-High | Luigi | Absolute rule: retain, repair and seam-strengthen the original shell and VIN | Controlled by process |
| R11 | Insurance gap on work-in-progress. Peak WIP approaches A$1m of customer-funded asset the atelier does not own | Medium-High | Jeremy | Specialist motor-trade broker, goods-in-custody and WIP cover sized to peak across all cars in build simultaneously. In place before the first client car arrives | Open |
| R12 | Porsche AG trademark or trade dress action | Medium | Jeremy | "Reimagined by Antipode" only. Persistent disclaimers. No crest, script or typography. Client-directed framing. Class 12 and 37 clearance before launch | Controlled by process, see `docs/03-regulatory-and-tax.md` s6 |
| R13 | Brand name collision. "Antipode" is uncleared in class 12 and 37, with a known luxury-superyacht overlap | Medium | Jeremy | Run the clearance in `docs/04-brand-clearance.md` before any public use. Pre-agreed fallback to Verrada | Open, blocks launch |
| R14 | Outsourced paint and trim exceed the modelled A$105,000 combined | Medium | Luigi | Three written quotes per discipline before Gate 1 | Open, blocks Gate 1 |
| R15 | European Galleria entity, ABN and workshop scope unconfirmed. The two plans use different trading names for Luigi's business | Medium | Luigi | Confirm the correct legal entity and ABN before any contract or public reference | Open, blocks Gate 1 |
| R16 | Deposit and cash-flow mismatch across a 12 to 18 month build | Medium | Jeremy | Milestone progress payments per `model/output.md` s7. Buyer funds the donor. Atelier never finances WIP from its own balance sheet | Controlled by structure |
| R17 | Donor prices run above A$130,000 | Medium | Jeremy | Shift to buyer-supplied donors. Current AU G-body index averages A$114k with a 12-month trend down 19%, so this is presently benign | Monitored |
| R18 | 50/50 deadlock paralyses decisions | Medium | Both | Pre-agreed tie-break: independent chair's casting vote on defined reserved matters, or a buy-sell shotgun clause | Open |
| R19 | Macro or wealth downturn cuts discretionary spend | Medium | Jeremy | Variable cost base. Advisory and donor brokerage are more resilient than new commissions and can carry the business through | Structural |
| R20 | Self-commissioned awards read as self-commissioned to a small connected buyer community | Low-Medium | Jeremy | Lead credibility with the car, named technicians and the build journal rather than a purchased award. See `docs/02-strategy-decision.md` | Open, judgement call |

## The three that matter

R1, R2 and R3 decide whether this is a 35% gross margin business or a loss-making one. Everything else is manageable. Two of the three (R1 and R3) are closeable in Phase 0 without touching a car, which is the strongest argument for the sequencing in `docs/02-strategy-decision.md`. R2 cannot be closed without building, which is why car one is scoped as an instrumented prototype rather than simply the first sale.

## Removed from the source registers

Plan B's risk "builder relationship falls through or is exclusive to a rival" does not apply, since Luigi is a founder rather than a counterparty. Plan B's "search or digital demand thinner than hoped" is retained implicitly in R9 rather than as its own line: the point stands that this is a relationship-led market and digital is a capture layer only, but it is a channel-mix observation rather than a venture risk.
