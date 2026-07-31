# Strategy decision: reconciling the two business plans

Status: recommended, not yet ratified by the founders.
Date: 31 July 2026.
Supersedes nothing. Read with `model/output.md` open.

## The apparent conflict

Two plans were commissioned and they appear to recommend opposite things.

**Plan A** (*Business Plan: An Ultra-Luxury Porsche 911 Restomod Atelier for Australia*) says build the cars. Launch as Antipode Motor Co., G-body donors, A$975,000 ex-donor, out of Luigi Pacelli's Artarmon workshop, two cars in year one, roughly 35% gross margin, a 50/50 joint venture.

**Plan B** (*The Australian Porsche Restomod Opportunity*) says do not build the cars. Its executive summary opens with "The recommended entry is NOT a car-building atelier." It recommends a capital-light demand-generation, donor-sourcing and advisory business, A$300k to A$750k of working capital instead of A$3m to A$6m, first revenue in 90 to 180 days instead of two to three years.

Taken at face value these are irreconcilable, and the natural instinct is to pick one. That instinct is wrong, and it took running the numbers to see why.

## Why it is a false conflict

Read past each plan's headline to its exit condition and they describe the same gate from opposite sides.

Plan A, Recommendation 1: "Proceed, but stage the commitment... do not commit to a five- or six-car ramp until build one is delivered and certified and at least one paid foundation commission is banked."

Plan B, closing benchmark: "if, and only if, the business demonstrates a repeatable pipeline of ten-plus committed seven-figure buyers a year AND secures an experienced build partner willing to take the manufacturing and ACL risk, then an equity stake in that partner's atelier becomes worth considering."

Both say: prove demand with real money before committing capital to manufacturing. They differ only on what you do while you wait, and on how much of the atelier you eventually own. Plan A treats the waiting period as brand-building. Plan B treats it as a business in its own right that earns revenue.

Plan B is right about that, and it costs nothing to accept. The advisory and donor-brokerage lines are not an alternative strategy, they are how you fund the wait and, more importantly, how you generate the evidence that decides the build question. A donor desk talking to twenty air-cooled buyers a quarter is a demand-sensing instrument that no amount of PR spend replicates.

So the decision is not "atelier or advisory." It is a sequence with a hard gate in the middle.

## What the model changed

I rebuilt Plan A's unit economics as a runnable model (`model/model.mjs`) and stress-tested the assumptions it labelled as assumptions. Three of them are load-bearing, and Plan A's own recommendations quietly break two of them.

### 1. The labour rate contradicts the services agreement

Plan A prices build labour at 3,000 hours by A$120/hr, an "internal blended rate," giving A$360,000 and a 34.9% gross margin. Plan A Recommendation 4 then says European Galleria must be paid "a market labour rate for build hours" under "a separate arm's-length services agreement," so that Luigi is not "effectively diluted twice (equity plus donated labour)."

Both cannot hold. A$120/hr is a cost-of-employment rate. Plan B records specialist Porsche shop rates at A$160 to A$250/hr, which is what an arm's-length agreement would actually charge. Substituting the market rate:

| Labour basis | Rate | Gross profit per car | Margin | Year 1 result on 2 cars |
|---|---|---|---|---|
| Internal cost (Plan A as written) | A$120/hr | A$340,000 | 34.9% | +A$236,000 |
| Market shop rate, low | A$160/hr | A$220,000 | 22.6% | -A$4,000 |
| Market shop rate, high | A$250/hr | -A$50,000 | -5.1% | -A$544,000 |

At the low end of a genuine arm's-length rate, year one breaks exactly even and then loses money in year two. At the high end each car loses money before overhead. The entire difference between a healthy business and a failing one is a single negotiated number that Plan A treats as two independent decisions in two different sections.

This is the most important finding in the reconciliation. The equity split and the services agreement rate have to be negotiated together, as one trade, because they are the same economic quantity. Luigi can take value as equity or as hourly rate. He cannot take it twice, and the venture cannot afford to pretend the choice does not exist.

### 2. Build hours are half the only published benchmark

Plan A assumes 3,000 build hours, reasoning that a steel body with a subtle widebody should take less than Theon's ~6,000 hours for a full carbon car. That is a plausible direction of travel. It is also a 50% cut to the only published figure in the segment, applied to a first-ever build by a team that has never done a full restomod, with no paint or trim capability in-house yet.

At Theon's 6,000 hours, even at the internal A$120/hr rate, COGS reaches A$995,000 against a A$975,000 price. Every car loses A$20,000 before overhead. Holding a 35% margin at those hours needs a price of A$1,530,769, which is above Wiedergeboren and approaching Zeigler/Bailey. The positioning wedge the whole plan rests on disappears.

The sensitivity grid in `model/output.md` section 4 makes the safe zone plain: hours at or below roughly 3,500, and labour at or near internal cost. Outside that corner the business does not work at A$975,000. Note that a first build almost always overruns, so 3,000 is the number to *achieve*, not the number to plan cash against.

### 3. Luxury Car Tax is a position-killer, not a cost line

Both plans flag LCT and both defer it to an ATO private ruling. Neither calculated it. It is worth calculating, because the answer is large.

LCT is 33% on the GST-inclusive value above A$80,567 (2025-26 general threshold), by the formula (LCT value − threshold) × 10/11 × 33%. On a A$975,000 ex-GST commission that is **A$297,580**.

There are only two ways to handle it and both hurt:

- **Pass it to the buyer.** Margin is untouched, but the buyer's ex-donor cost rises to A$1,370,080, which is 8.3% *above* Wiedergeboren. The pricing strategy is to sit below Wiedergeboren. Passing the tax on inverts the position.
- **Absorb it.** The buyer stays at A$1,072,500, the ex-GST commission falls to A$766,902, and the margin drops from 34.9% to 17.2%. Break-even rises from 1.3 cars a year to 3.4.

So an adverse ruling either breaks the price position or halves the margin. What makes this the easiest of the three problems is that it is answerable now, for the cost of a private ruling, before anyone spends money on a donor. Plan A's instruction to "price with a contingency until the ruling is in hand" is right, and the contingency is roughly A$300k a car, which is too large to carry quietly.

### 4. The Wiedergeboren price wedge is smaller than either plan thinks

Both plans note Wiedergeboren's price as either A$1.265m or "A$1.15m plus GST" and treat the discrepancy as inconsistent reporting. It is not inconsistent. 1,150,000 × 1.1 = 1,265,000 exactly. These are one price on two tax bases.

That matters because Plan A positions A$975,000 against A$1.265m and reads a ~A$290,000 wedge. On a like-for-like ex-GST basis the wedge is A$175,000, or 15.2%. Still real, still defensible, but thinner than assumed, and it is precisely the margin an adverse LCT ruling consumes.

Worth stating plainly for internal clarity: Theon delivers a full carbon-bodied car over 6,000 hours for about A$860,000 ex-GST, below both Australian houses. No Australian atelier is winning on cost. The pitch is locality, certification, and access to the people building your car. That is a real pitch. It is just not a value pitch, and the copy should not pretend otherwise.

### 5. Plan A has no Australian Consumer Law position

Plan B raises consumer guarantees as a serious tail risk for a builder: acceptable quality and fitness for purpose cannot be contracted out of, and a major failure gives the buyer the choice of repair, replacement or refund. On a hand-built A$975,000 car, "replacement" is not a meaningful remedy and "refund" is close to fatal.

Plan A's eleven-row risk register does not mention the ACL at all. That is the single largest omission across the two documents. It does not change the recommendation, but it belongs in the risk register (it is now item R4 in `docs/05-risk-register.md`) and it needs to shape the build contract, the warranty reserve, and the decision about which entity supplies the vehicle.

## The recommendation

Adopt Plan A's destination and Plan B's sequencing, with three gates. Concretely:

**Phase 0, weeks 1 to 12. Clear the cheap questions.** Trademark clearance, the ATO private ruling, a VSCCS certifier on retainer, written quotes for paint and trim, the entity and the services-agreement rate settled as one negotiation, and the European Galleria entity discrepancy resolved. Brand and website built. Cost is legal, professional and brand spend, not manufacturing. None of this requires a donor car.

**Phase 1, weeks 6 to 26, overlapping. Stand up Plan B's revenue lines.** Donor sourcing and brokerage, and paid advisory. This earns revenue inside the first two quarters, builds the client book, and generates the demand evidence that Gate 1 turns on. Run the launch PR wave here, against renders and the brand rather than a finished car.

**Gate 1: commit to build one.** Requires one signed foundation commission with a cleared A$100,000 deposit (not an expression of interest), a favourable LCT ruling or a priced contingency the founders have explicitly accepted, a certifier engaged, and paint and trim quoted in writing. If Gate 1 does not clear by roughly month 9, the advisory and brokerage business continues and the build decision moves out. That is a real outcome, not a failure.

**Phase 2. Build car one as an instrumented prototype.** Every stage timed against the 3,000-hour assumption. The purpose of car one is as much to produce a validated cost model as a car.

**Gate 2: commit to volume.** Requires car one delivered and certified, actual hours known, and a second paid commission banked. Only then does the five- or six-car ramp get funded.

Both source plans already agree with this. The contribution here is putting numbers on the gates and naming the two assumptions that decide everything.

## What I would push back on

Plan A's two-cars-in-year-one figure is presented as prudence, and it reads that way, but at 3,000 hours a car it implies 6,000 build hours flowing through a workshop whose base business is servicing and engine rebuilds. Plan A identifies the capacity conflict as a high risk and mitigates it with ring-fenced bays and separate scheduling. That is the right mitigation, and it is worth being honest that two cars is not a gentle ramp for a shop this size. One car in year one, done properly and measured, is a better proving programme and produces a far more valuable number at Gate 2.

I would also resist Plan A's instruction to "commission a Global Recognition Award to seed third-party credibility before any product exists." Buyers at this level are a small, connected community, and self-commissioned awards are legible as such. The credibility asset that actually converts is a car and a named technician, and Plan A's own build-journal idea is the stronger play. This is a judgement call and the founders may weigh it differently, but the downside is reputational and hard to reverse.

## Open items this document does not resolve

Carried into `docs/07-open-questions.md`: the equity split cannot be fixed until the services-agreement rate is set; the correct legal entity and ABN for Luigi's workshop is unconfirmed and the two plans use different names for it; and which entity supplies the vehicle for ACL purposes is undecided.
