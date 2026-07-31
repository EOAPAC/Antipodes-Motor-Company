# ADR-0004: Obtain an ATO private ruling on LCT before the first invoice

Date: 31 July 2026. Status: proposed. **Blocks Gate 1.**

## Context

Luxury Car Tax is 33% on the GST-inclusive value above the threshold (A$80,567,
2025-26 general), by the formula (LCT value − threshold) × 10/11 × 33%. Note that
10/11 × 33% = 0.30 exactly.

LCT generally applies only to cars imported or sold within two years of
manufacture, which is why an old car is normally outside it. Whether
re-manufacturing resets the date of manufacture is unresolved. Neither business
plan could verify the current position, and neither calculated the exposure.

On a A$975,000 ex-GST commission it is **A$297,580**, and there are only two ways
to handle it:

| | LCT out of scope | LCT in scope, passed on | LCT in scope, absorbed |
|---|---|---|---|
| Buyer pays ex-donor | A$1,072,500 | A$1,370,080 | A$1,072,500 |
| Ex-GST commission | A$975,000 | A$975,000 | A$766,902 |
| Gross margin | 34.9% | 34.9% | 17.2% |

Passing it on puts the buyer 8.3% **above** Wiedergeboren, inverting a pricing
strategy built on sitting below it. Absorbing it halves the margin and lifts
break-even from 1.3 cars a year to 3.4.

## Decision

Lodge an ATO private binding ruling request in Phase 0, before any donor is
bought. Until the ruling lands, state the LCT contingency explicitly in the
commissioning agreement rather than absorbing it silently. Confirm the
current-year threshold, since the modelled figure is the 2025-26 general one.

## Consequences

This is the cheapest large risk reduction available to the venture: the cost of a
ruling against a A$297,580-per-car exposure. It requires no car, no donor and no
commission, so there is no reason to defer it.

If the ruling is adverse, treat it as a genuine stop-and-think rather than a
repricing exercise. Plan A's instruction to "re-price to preserve the ~35% gross
margin" understates it, because the reprice is what destroys the market position.
