# ADR-0006: One published commission, not a tier ladder

Date: 31 July 2026. Status: proposed. **Supersedes ADR-0005.**

## Context

ADR-0005 concluded two published tiers, Foundation A$975,000 and Signature
A$1,150,000, after modelling showed the proposed A$850,000 entry tier sat A$10,000
under Theon Design and was the most fragile of the three on labour rate.

Master plan v4 (`reference/plan-v4-master.md` section 6.3) reaches a different
conclusion from a brand direction rather than a margin one: **there are no
client-facing tiers and no published price grid.** Client-facing language is a
single numbered one-off commission. Internally the atelier runs three costed build
stacks (A Foundation, B Grande Traversée, C Signature) with full bills of material,
and those stay internal.

The v4 critique (`reference/plan-v4-directives.md`, item 8) is explicit: "kill tier
names + price grids from client-facing framing — internal cost stacks only;
client-facing = named one-off commissions in a registry."

## Decision

Publish one commission price and keep the ladder internal.

| Published | |
|---|---|
| Foundation commission | From A$975,000, ex-donor |
| Founders series | First three at A$895,000, ex-donor |
| All in, with a donor sourced by us | A$1.07m to A$1.11m |
| Ownership programme | A$18,000 a year |
| Beyond the foundation | Quoted privately, per commission |

Internal Stack A/B/C economics are unchanged and still drive the model. ADR-0005's
arithmetic is not withdrawn: the A$850,000 tier is still rejected, and the
A$1,150,000 figure survives as Stack B's internal guide price.

## Rationale

The two positions are not really in conflict. ADR-0005 asked which prices make
money. v4 asks how many prices a buyer should see. The answer to the first is
unchanged; the answer to the second is one.

A grid invites shopping. Three columns with prices under them turns a conversation
about a car into a comparison between products, and the whole point of the brand
direction (`docs/09-brand-direction.md`) is to avoid comparison, because comparison
is a fight this house loses on paper against Theon. A single figure plus "quoted
privately, per commission" keeps the sale where it belongs.

Publishing something rather than nothing is still right. At this price point a
buyer who cannot find any indication of cost assumes it is either unserious or
outside their range, and a figure filters enquiries before they reach a founder.

## Consequences

The Signature figure disappears from public view but stays in the model as Stack B.
Mix shift toward it from Year 3 still drives the five-year projection.

**The founders-series row is a commercial choice, not a brand one.** v4 frames
A$895,000 as the fallback if the demand-evidence gate fails (3+ letters of intent
before A$975,000 holds). Publishing it now presents it as a launch offer instead,
which is defensible as scarcity and is the more honest position while no letters of
intent exist. If the founders would rather hold at A$975,000, deleting one row in
`web/index.html` reverts it.

Both figures remain contingent on ADR-0003 (labour rate) and ADR-0004 (LCT). An
adverse LCT ruling implies a reprice to roughly A$1.3m, which is a demand question
before it is a pricing one.
