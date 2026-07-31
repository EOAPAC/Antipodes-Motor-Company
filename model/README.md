# The financial model

`model.mjs` is the unit-economics, sensitivity and break-even model. Plain
JavaScript, no dependencies, Node 18 or later.

```sh
node model/model.mjs           # print the report
node model/model.mjs --write   # also regenerate output.md
```

`output.md` is generated. Do not edit it by hand: change the model and re-run.

## What it is for

It exists to test assumptions, not to forecast. Both source business plans stated
their per-car economics as a single column of figures and labelled them
"ASSUMPTIONS", which is honest but not useful, because it gives no sense of which
assumptions the whole case rests on. The model answers that question.

Three inputs turn out to be load-bearing:

1. **Build hours.** 3,000 assumed against Theon's published ~6,000.
2. **The labour rate** charged by the workshop to the joint venture. A$120/hr
   internal cost against A$160 to A$250/hr market shop rates.
3. **Luxury Car Tax.** In scope or out, worth A$297,580 a car.

Section 4's sensitivity grid is the single most useful output: gross margin across
six hour counts and five labour rates. Only the top-left corner supports the
business case at A$975,000.

## Sections

| # | Section | Answers |
|---|---|---|
| 1 | Cost stack | What the car costs before labour |
| 2 | Unit economics | Five scenarios across the two load-bearing inputs |
| 3 | Competitive ladder | Where we sit, corrected to a common tax basis |
| 4 | Sensitivity grid | Hours against labour rate. The safe zone |
| 5 | Fixed cost and break-even | How many cars a year at three overhead levels |
| 6 | Luxury Car Tax | Pass it on or absorb it, and what each costs |
| 7 | Deposit schedule | Milestone payments, and peak own-cash exposure |
| 8 | Five-year projection | Under both labour-rate scenarios |
| 9 | What has to be true | Six conditions, with status and how to close each |
| 10 | Tier ladder | One price, two or three |

## How inputs are recorded

Every input is wrapped in `A(value, source)` so the basis travels with the number
and prints into the report:

```js
const price = A(975_000, 'PLAN-A recommended launch commission, ex-donor, ex-GST');
```

`PLAN-A` is the atelier business plan, `PLAN-B` the investor-grade plan, both in
`reference/`. Anything marked plainly `assumption` has no external basis and is
first in line to be replaced with a real quote.

Rate and threshold for LCT are legislated, not assumed, and are labelled as such.
The threshold used is the 2025-26 general figure; a sale in a later year uses that
year's threshold (open question Q4).

## Extending it

Two things worth knowing before editing.

**Fixed cost is built from lines, not guessed.** `fixedLean` sums to a real figure
rather than a round number, on the assumption that European Galleria's existing
service business continues to carry the workshop's own rent, lifts, tooling and
base staff. If that assumption changes, this is where it changes.

**The LCT helpers are exact, not approximations.** `lctPayable` implements
(LCT value − threshold) × 10/11 × 33%, where 10/11 × 33% = 0.30 exactly.
`priceAbsorbingLct` inverts it to solve for the ex-GST price that holds a buyer's
all-in cost fixed. If you change the rate, both stay correct.

The deposit schedule self-checks against the commission price and prints a failure
line if it stops reconciling. Keep that behaviour if you change the milestones.

## What it does not model

- A warranty reserve. It follows from the ACL advice, which is open (Q6, Q12).
- The service business's own P&L. Real figures were not available (Q9).
- Donor cost, deliberately: the donor is excluded from the commission price and
  bought with buyer funds.
- Tax on profits, financing costs, or founder drawings. Gross and operating only.
