# 90-day plan

Dated from 31 July 2026. Merged from both source plans, resequenced so that the questions which can kill the venture are answered before money is committed to anything hard to reverse.

Owners: **J** Jeremy Levitt, **L** Luigi Pacelli, **B** bought in (adviser, certifier, broker, counsel).

## Block 1: weeks 1 to 4, to 28 August 2026. Clear and decide.

The theme is cheap answers to expensive questions. Nothing in this block requires a donor car, a deposit, or a public launch.

| # | Action | Owner | Done when |
|---|---|---|---|
| 1.1 | Run IP Australia searches for "Antipode" and "Antipode Motor" in class 12 and class 37 | J | Written search results filed. See `docs/04-brand-clearance.md` |
| 1.2 | ASIC business-name availability, plus WHOIS on antipodemotor.com, antipodemotor.com.au, antipode.com.au | J | Availability confirmed and names secured, or fallback triggered |
| 1.3 | Knock-out US trademark search, given eventual export intent | J + B | Search report received |
| 1.4 | Lodge the ATO private binding ruling request on LCT treatment of a re-manufactured G-body | J + B | Lodged with the ATO, reference number filed |
| 1.5 | Confirm European Galleria's correct legal entity, ABN and licensed workshop scope | L | Entity and ABN documented. Resolves R15 |
| 1.6 | Pull European Galleria's actual service P&L to set the base-load figures | L | Twelve months of real numbers in the model |
| 1.7 | Model the equity split against the services-agreement labour rate, both together | J | Scenarios run in `model/model.mjs`, outcomes tabled for the term sheet |
| 1.8 | Engage a VSCCS-licensed certifier. Confirm in writing which modification codes their licence covers | J + B | Retainer signed, code coverage confirmed, gaps identified |
| 1.9 | Brief a specialist motor-trade broker on goods-in-custody and WIP cover | J + B | Indicative terms and premium received |
| 1.10 | Commission legal advice on ACL exposure and which entity supplies the vehicle | J + B | Written opinion received. Resolves R4 and Q6 |

Milestone at 28 August: the founders know whether the name is usable, what the tax risk is, and what an arm's-length labour rate does to the margin. All three before a dollar of build spend.

## Block 2: weeks 5 to 8, to 25 September 2026. Structure and quote.

| # | Action | Owner | Done when |
|---|---|---|---|
| 2.1 | Sign the term sheet: new entity, equity split, services-agreement rate, tie-break mechanism, four-year vesting, leaver provisions, in-kind valuation of Baden Bower, BruntWork and GRA services | J + L | Signed. Equity and labour rate in one document, per R1 |
| 2.2 | Incorporate Antipode Motor Co. Pty Ltd, subject to name clearance | J + B | ACN issued, bank account open |
| 2.3 | Three written quotes for body and paint | L | Quotes in hand, compared to the modelled A$55,000 |
| 2.4 | Three written quotes for bespoke trim and interior | L | Quotes in hand, compared to the modelled A$50,000 |
| 2.5 | Interview and engage a design authority so cars share a coherent signature | L + J | Engaged. Resolves half of R6 |
| 2.6 | Interview a panel and paint lead, whether hired or contracted | L | Shortlist and decision on hire versus contract |
| 2.7 | Retouch the six existing renders: remove every Porsche crest and word mark, re-plate, apply the Antipode wordmark, regenerate derivatives | J | Every item in `web/ASSET-CLEARANCE.md` closed and signed off by the trademark adviser |
| 2.8 | Settle the widebody specification, then make the render set depict one coherent car | J + L + design authority | Flares agreed; three renders currently closer to a 930 Turbo brought into line |
| 2.9 | Decide the commission ladder: two tiers or one price | J | Decision recorded against `decisions/ADR-0005`. Resolves Q17 |
| 2.10 | Build and ship the website | J | Live at the cleared domain, enquiry form wired to the CRM, `noindex` removed only after 2.7 closes |
| 2.11 | Source and price two candidate donor 911 SC or 3.2 Carrera cars to validate the donor-cost assumption | J + L | Two real cars inspected and priced |
| 2.12 | Sign an inspection and authentication partner for the donor desk | J | Agreement in place, fee basis agreed |
| 2.13 | Update the model with every real quote received, replacing assumption lines | J | `model/output.md` regenerated, assumption count reduced |

Milestone at 25 September: the entity exists, the capability gaps have prices against them, and the brand is public-ready with cleared imagery.

## Block 3: weeks 9 to 13, to 29 October 2026. Launch and convert.

| # | Action | Owner | Done when |
|---|---|---|---|
| 3.1 | Brief Baden Bower for the launch PR wave, timed to the render reveal, with the non-affiliation line on every placement | J | Wave briefed and scheduled |
| 3.2 | Run the launch wave. Message: Australia has a world-class 911 restomod house, and here is why the G-body is the right donor | J | Placements live |
| 3.3 | Open the commission waitlist with the A$100,000 deposit structure | J | Waitlist live, deposit terms drafted and legally reviewed |
| 3.4 | Activate Porsche Club NSW, concours and track-day presence | J | Attendance calendar set, first event attended |
| 3.5 | Establish presence on Collecting Cars and Shannons, for donors and for visibility | J | Accounts active, first donor tracked |
| 3.6 | Open the donor desk. Take the first two or three sourcing mandates | J | First mandate signed, first fee earned |
| 3.7 | Convert the first paid advisory retainers | J | First retainer invoiced |
| 3.8 | Chase the ATO ruling and record the outcome or expected timing | J | Status known, contingency decision made either way |
| 3.9 | Review Gate 1 against its four criteria | J + L | Written go or no-go decision |

Milestone at 29 October: the business is earning revenue from advisory and brokerage, the brand is public, and the founders have a documented Gate 1 decision.

## What Gate 1 requires

Do not start build one until all four are true:

1. One signed foundation commission with a **cleared** A$100,000 deposit. An expression of interest is not a commission.
2. A favourable LCT ruling, or a contingency the founders have explicitly priced and accepted in writing.
3. A VSCCS certifier engaged, with licence coverage confirmed across every modification code the build needs.
4. Paint, panel and trim quoted in writing, inside the modelled A$105,000 combined.

## Benchmarks that change the plan

- **No foundation commission within six months of the PR wave.** Hold. Do not build speculatively. Keep the advisory and brokerage business running and revisit the build decision at month twelve. Plan A's guidance was to hold volume at two cars and reprice; the sharper version is to hold at zero until a deposit clears.
- **LCT ruled in scope.** Do not simply reprice to preserve the margin. Passing A$297,580 to the buyer puts Antipode above Wiedergeboren and destroys the position. Model both absorb and pass-through, then decide whether the venture still makes sense. This is a genuine stop-and-think, not an adjustment.
- **Arm's-length labour rate above about A$150/hr.** The margin no longer supports two cars against lean fixed cost. Either restructure the equity so Luigi's return comes through ownership rather than hourly rate, or reprice above A$975,000 and give up the Wiedergeboren wedge.
- **Luigi's service business shows strain.** Slow the ramp before quality slips. The service revenue is the base load that carries fixed costs between build milestones, and it is the reason the economics work at low volume at all.
- **Donor prices above A$130,000.** Shift to buyer-supplied donors. Currently benign: the AU G-body index averages A$114,000 with a 12-month trend down 19%.
