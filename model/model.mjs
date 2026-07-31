#!/usr/bin/env node
/*
 * Antipode Motor Co. — unit economics, sensitivity and break-even model
 *
 * Run:  node model/model.mjs            (prints report to stdout)
 *       node model/model.mjs --write    (also writes model/output.md)
 *
 * Every input below is an ASSUMPTION unless its `src` says otherwise.
 * The two source business plans are cited as PLAN-A (atelier plan) and
 * PLAN-B (investor-grade plan). Nothing here is a forecast.
 *
 * Design note: this model exists to test three load-bearing assumptions that
 * the source plans asserted but never stress-tested — build hours, the labour
 * rate charged by the workshop, and Luxury Car Tax. Each one on its own can
 * move the venture from viable to loss-making.
 */

const A = (v, src) => ({ v, src });

// ---------------------------------------------------------------------------
// Inputs
// ---------------------------------------------------------------------------

const price = A(975_000, 'PLAN-A recommended launch commission, ex-donor, ex-GST');

const donor = {
  low: A(90_000, 'PLAN-A range low'),
  avg: A(114_000, 'PLAN-B: AutoMarkets AU G-body index average, 93 results'),
  high: A(130_000, 'PLAN-A range high'),
};

// COGS lines excluding build labour (labour is computed from hours x rate)
const cogsExLabour = {
  'Engine rebuild and upgrade': A(75_000, 'PLAN-A assumption'),
  'Body and paint (outsourced)': A(55_000, 'PLAN-A assumption'),
  'Trim and interior (outsourced)': A(50_000, 'PLAN-A assumption'),
  'Suspension, brakes, wheels': A(45_000, 'PLAN-A assumption'),
  'Parts, consumables, misc': A(35_000, 'PLAN-A assumption'),
  'Certification and engineering': A(15_000, 'PLAN-A assumption'),
};

// The two assumptions that decide the whole business case.
const hours = {
  planA: A(3_000, 'PLAN-A assumption: "less than Theon because steel body, not full carbon"'),
  theon: A(6_000, 'PLAN-A cites Adam Hawley (Top Gear/Motoring Research 2026): ~6,000 man-hours'),
};

const labourRate = {
  internalCost: A(120, 'PLAN-A internal blended cost rate'),
  shopLow: A(160, 'PLAN-B: specialist Porsche shop rates run A$160-250/hr'),
  shopHigh: A(250, 'PLAN-B: upper end of specialist Porsche shop rates'),
};

// Annual fixed cost, built from lines rather than guessed as a round number.
// "Lean" assumes European Galleria's existing service business continues to
// carry the workshop's own rent, lifts, tooling and base staff.
const fixedLean = {
  'Brand, web, render suite, content (year 1)': A(120_000, 'assumption'),
  'PR programme (Baden Bower, valued in-kind)': A(60_000, 'assumption; in-kind per PLAN-A'),
  'Design authority (contracted)': A(80_000, 'assumption; PLAN-A names this as a gap'),
  'VSCCS certifier retainer': A(24_000, 'assumption'),
  'Motor-trade and WIP insurance': A(45_000, 'assumption; PLAN-A risk register item'),
  'Legal, IP, accounting, ATO ruling': A(55_000, 'assumption'),
  'Admin, CRM, offshore support (BruntWork)': A(60_000, 'assumption'),
};

const addPanelPaintLead = A(140_000, 'assumption: fully loaded panel/paint lead');
const addSecondTech = A(115_000, 'PLAN-B: fully loaded master technician A$105-115k');

// Luxury Car Tax. Rate and threshold are legislated, not assumptions.
// Whether a re-manufactured classic falls in scope is the open question and
// is precisely what the ATO private ruling must settle.
const LCT = {
  rate: 0.33,
  threshold: 80_567,
  src: 'PLAN-B: 33% above A$80,567 GST-inclusive, 2025-26 general threshold',
};
const GST = 0.10;

// ---------------------------------------------------------------------------
// Core functions
// ---------------------------------------------------------------------------

const sum = (obj) => Object.values(obj).reduce((t, x) => t + x.v, 0);

/** LCT payable on a supply, given an ex-GST price.
 *  ATO formula: (LCT value - threshold) x 10/11 x 33%, where LCT value is the
 *  GST-inclusive price excluding LCT itself. Note 10/11 x 0.33 = 0.30 exactly. */
function lctPayable(exGstPrice, { rate = LCT.rate, threshold = LCT.threshold } = {}) {
  const lctValue = exGstPrice * (1 + GST);
  if (lctValue <= threshold) return 0;
  return (lctValue - threshold) * (10 / 11) * rate;
}

/** Ex-GST price that holds the buyer's all-in cost at `target` when LCT applies.
 *  Solves: 1.1P + 0.3(1.1P - threshold) = target */
function priceAbsorbingLct(target, { rate = LCT.rate, threshold = LCT.threshold } = {}) {
  const k = (10 / 11) * rate; // 0.30
  return (target + k * threshold) / ((1 + GST) * (1 + k));
}

function unitEconomics({ buildHours, rate, commission = price.v }) {
  const labour = buildHours * rate;
  const cogs = sum(cogsExLabour) + labour;
  const gross = commission - cogs;
  return {
    commission,
    buildHours,
    rate,
    labour,
    cogs,
    gross,
    margin: gross / commission,
  };
}

function breakEven(grossPerCar, fixedAnnual) {
  if (grossPerCar <= 0) return Infinity;
  return fixedAnnual / grossPerCar;
}

// ---------------------------------------------------------------------------
// Formatting
// ---------------------------------------------------------------------------

const money = (n) =>
  (n < 0 ? '-' : '') +
  'A$' +
  Math.abs(Math.round(n)).toLocaleString('en-AU');
const pct = (n) => (n * 100).toFixed(1) + '%';
const out = [];
const w = (s = '') => out.push(s);
const table = (headers, rows) => {
  w('| ' + headers.join(' | ') + ' |');
  w('|' + headers.map(() => '---').join('|') + '|');
  rows.forEach((r) => w('| ' + r.join(' | ') + ' |'));
  w();
};

// ---------------------------------------------------------------------------
// Report
// ---------------------------------------------------------------------------

w('# Antipode Motor Co. — model output');
w();
w('Generated by `model/model.mjs`. Do not edit this file by hand; edit the model and re-run.');
w();
w('Every figure is a planning assumption unless the basis column says otherwise.');
w('The model exists to test assumptions, not to forecast.');
w();

// --- 1. Cost stack -----------------------------------------------------------
w('## 1. Cost stack, excluding build labour');
w();
table(
  ['Line', 'Amount', 'Basis'],
  Object.entries(cogsExLabour).map(([k, a]) => [k, money(a.v), a.src])
);
w(`Subtotal excluding labour and donor: **${money(sum(cogsExLabour))}**`);
w();
w(`Donor car is excluded from the commission price and bought with buyer funds: ${money(donor.low.v)} to ${money(donor.high.v)}, AU G-body index average ${money(donor.avg.v)}.`);
w();

// --- 2. The three scenarios that matter --------------------------------------
w('## 2. Unit economics under the load-bearing assumptions');
w();
w("PLAN-A's headline (~35% gross margin) holds only in the first row. The other rows change nothing except two inputs that neither plan validated.");
w();

const scenarios = [
  { name: 'A. PLAN-A as written', h: hours.planA.v, r: labourRate.internalCost.v },
  { name: 'B. PLAN-A hours, workshop billed at market shop rate (low)', h: hours.planA.v, r: labourRate.shopLow.v },
  { name: 'C. PLAN-A hours, workshop billed at market shop rate (high)', h: hours.planA.v, r: labourRate.shopHigh.v },
  { name: 'D. Theon-equivalent hours, internal cost rate', h: hours.theon.v, r: labourRate.internalCost.v },
  { name: 'E. Theon-equivalent hours, market shop rate (low)', h: hours.theon.v, r: labourRate.shopLow.v },
];

const runs = scenarios.map((s) => ({ ...s, e: unitEconomics({ buildHours: s.h, rate: s.r }) }));

table(
  ['Scenario', 'Hours', 'Rate/hr', 'Labour', 'Total COGS', 'Gross profit', 'Gross margin'],
  runs.map((s) => [
    s.name,
    s.h.toLocaleString('en-AU'),
    money(s.r),
    money(s.e.labour),
    money(s.e.cogs),
    money(s.e.gross),
    pct(s.e.margin),
  ])
);

const scenA = runs[0].e;
const scenD = runs[3].e;
w(`Scenario D is the one to sit with. At Theon's published ~6,000 hours, total COGS of ${money(scenD.cogs)} exceeds the ${money(price.v)} commission price, so every car loses ${money(-scenD.gross)} before a dollar of overhead. The price that would restore a 35% margin at those hours is ${money(scenD.cogs / 0.65)}, which is above Wiedergeboren (A$1.265m) and close to Zeigler/Bailey (A$1.6m). The positioning wedge PLAN-A is built on disappears.`);
w();

// --- 3. Competitive ladder, reconciled ---------------------------------------
w('## 3. Competitive price ladder, reconciled to a common tax basis');
w();
w("Both source plans record Wiedergeboren's price as either A$1.265m or \"A$1.15m plus GST\" and treat these as inconsistent reporting. They are the same price: 1,150,000 x 1.1 = 1,265,000 exactly. One figure is ex-GST, the other GST-inclusive. Comparing Antipode's ex-GST commission against a rival's GST-inclusive price overstates the wedge, so the ladder below states both.");
w();
const ladderComp = [
  { name: 'Theon Design (UK)', exGst: 860_000, note: 'GBP 430k ex-VAT at 2.00; excludes shipping and AU taxes on landing' },
  { name: 'Antipode (proposed)', exGst: price.v, note: 'Recommended launch commission' },
  { name: 'Wiedergeboren (AU)', exGst: 1_150_000, note: 'Reported as A$1.15m + GST, equivalently A$1.265m inc GST' },
  { name: 'Zeigler/Bailey Z/B 4.4 (AU)', exGst: 1_600_000, note: 'Ex-donor, GST basis not stated. Publishes 300kW/500Nm from 4.4L; original floor replaced, ICV path' },
];
table(
  ['House', 'Ex-GST', 'Inc-GST', 'vs Antipode ex-GST', 'Note'],
  ladderComp.map((c) => [
    c.name,
    money(c.exGst),
    money(c.exGst * (1 + GST)),
    c.exGst === price.v ? '—' : pct(c.exGst / price.v - 1),
    c.note,
  ])
);
const wieder = ladderComp.find((c) => c.name.startsWith('Wieder'));
const antipodeAllInWithLct = price.v * (1 + GST) + lctPayable(price.v);
w(`On a like-for-like ex-GST basis Antipode undercuts Wiedergeboren by ${money(wieder.exGst - price.v)}, or ${pct(1 - price.v / wieder.exGst)} below it, rather than the ~A$290k implied by comparing against the GST-inclusive figure. That is still a real wedge, but it is thinner than PLAN-A assumes, and it is the wedge that an adverse LCT ruling erases: at ${money(antipodeAllInWithLct)} all-in, Antipode would sit ${pct(antipodeAllInWithLct / (wieder.exGst * (1 + GST)) - 1)} above Wiedergeboren instead of below it.`);
w();
w('Theon sits below both Australian houses on price while delivering a full carbon body over 6,000 hours. Any Australian house pricing above Theon is selling locality, certification and access to the builder, not a cost advantage. That is a defensible pitch, and it is worth being clear internally that it is the actual pitch.');
w();

// --- 4. Sensitivity grid -----------------------------------------------------
w('## 4. Gross margin sensitivity: build hours against labour rate');
w();
w(`Commission held at ${money(price.v)} ex-donor. Cells below 20% margin are marked \`!\`; negative margins are marked \`!!\`.`);
w();
const hourGrid = [2500, 3000, 3500, 4000, 5000, 6000];
const rateGrid = [120, 150, 180, 220, 250];
table(
  ['Hours \\ Rate', ...rateGrid.map((r) => money(r) + '/hr')],
  hourGrid.map((h) => [
    h.toLocaleString('en-AU'),
    ...rateGrid.map((r) => {
      const m = unitEconomics({ buildHours: h, rate: r }).margin;
      const flag = m < 0 ? ' !!' : m < 0.2 ? ' !' : '';
      return pct(m) + flag;
    }),
  ])
);
w('Only the top-left corner of that grid supports the business case as written. The plan needs build hours at or below roughly 3,500 and a labour rate at or near internal cost. Both need validating on the first car before volume is committed.');
w();

// --- 5. Fixed cost and break-even -------------------------------------------
w('## 5. Annual fixed cost and break-even volume');
w();
table(
  ['Line', 'Amount', 'Basis'],
  Object.entries(fixedLean).map(([k, a]) => [k, money(a.v), a.src])
);
const leanTotal = sum(fixedLean);
const moderateTotal = leanTotal + addPanelPaintLead.v + addSecondTech.v;
const planBComparator = 450_000 * 6;

w(`**Lean** (service business carries the workshop's own fixed costs): ${money(leanTotal)}`);
w();
w(`**Moderate** (lean plus a panel/paint lead at ${money(addPanelPaintLead.v)} and a second senior technician at ${money(addSecondTech.v)}, both named as required in PLAN-A's risk register): ${money(moderateTotal)}`);
w();
w(`**PLAN-B comparator** (a standalone atelier carrying its own premises and non-billable staff, A$450k/car at 6 cars): ${money(planBComparator)}`);
w();

const fixedLevels = [
  ['Lean', leanTotal],
  ['Moderate', moderateTotal],
  ['PLAN-B standalone atelier', planBComparator],
];

table(
  ['Fixed cost level', 'Annual fixed', ...runs.map((s) => s.name.split('.')[0])],
  fixedLevels.map(([label, f]) => [
    label,
    money(f),
    ...runs.map((s) => {
      const be = breakEven(s.e.gross, f);
      return be === Infinity ? 'never' : be.toFixed(1) + ' cars';
    }),
  ])
);

w(`Read that against PLAN-A's plan of two cars in year one:`);
w();
table(
  ['Scenario', 'Gross profit, 2 cars', 'Less lean fixed', 'Year 1 operating result'],
  runs.map((s) => {
    const g = s.e.gross * 2;
    return [s.name.split('.')[0], money(g), money(leanTotal), money(g - leanTotal)];
  })
);
w(`Scenario A clears lean fixed cost on two cars with ${money(scenA.gross * 2 - leanTotal)} to spare. Scenario B does not: two cars produce a ${money(-(runs[1].e.gross * 2 - leanTotal))} loss. The difference between those two outcomes is nothing but the rate at which European Galleria bills its own hours to the joint venture, which PLAN-A recommendation 3 says must be an arm's-length market rate.`);
w();

// --- 6. LCT ------------------------------------------------------------------
w('## 6. Luxury Car Tax exposure');
w();
w(`Rate and threshold are legislated (${LCT.src}). Whether a re-manufactured classic is in scope is unresolved in both plans and is the question the ATO private ruling must answer. The arithmetic below shows why it cannot be left open.`);
w();
const lct = lctPayable(price.v);
const buyerNoLct = price.v * (1 + GST);
const buyerWithLct = buyerNoLct + lct;
table(
  ['Measure', 'LCT out of scope', 'LCT in scope'],
  [
    ['Commission price, ex-GST', money(price.v), money(price.v)],
    ['GST', money(price.v * GST), money(price.v * GST)],
    ['LCT', money(0), money(lct)],
    ['**Buyer pays, ex-donor**', `**${money(buyerNoLct)}**`, `**${money(buyerWithLct)}**`],
    ['Gross margin to Antipode', pct(scenA.margin), pct(scenA.margin)],
  ]
);
w(`Passing LCT through costs Antipode no margin, but it lifts the buyer's ex-donor cost to ${money(buyerWithLct)}, above Wiedergeboren's A$1.265m. The entire pricing strategy is to sit below Wiedergeboren, so passing the tax on inverts the position.`);
w();
const absorbed = priceAbsorbingLct(buyerNoLct);
const absorbedEcon = unitEconomics({ buildHours: hours.planA.v, rate: labourRate.internalCost.v, commission: absorbed });
w(`Absorbing it instead, to hold the buyer at ${money(buyerNoLct)}, drops the ex-GST commission to ${money(absorbed)} and the margin from ${pct(scenA.margin)} to ${pct(absorbedEcon.margin)}:`);
w();
table(
  ['Measure', 'Value'],
  [
    ['Ex-GST commission price', money(absorbed)],
    ['Total COGS (scenario A)', money(absorbedEcon.cogs)],
    ['Gross profit per car', money(absorbedEcon.gross)],
    ['Gross margin', pct(absorbedEcon.margin)],
    ['Break-even cars against lean fixed', breakEven(absorbedEcon.gross, leanTotal).toFixed(1)],
  ]
);
w(`So an adverse ruling either breaks the price position or roughly halves the margin. There is no version where it is a minor variable, and it is resolvable for the cost of a private ruling before the first invoice.`);
w();

// --- 7. Deposit schedule -----------------------------------------------------
w('## 7. Deposit and progress payment schedule');
w();
const deposits = [
  ['Commissioning deposit on signing', 100_000],
  ['On teardown (30%)', 292_500],
  ['On body and paint sign-off (25%)', 243_750],
  ['On mechanical and engine assembly (25%)', 243_750],
  ['Balance on certification and delivery', 95_000],
];
let cum = 0;
table(
  ['Milestone', 'Amount', 'Cumulative', '% of price'],
  deposits.map(([label, amt]) => {
    cum += amt;
    return [label, money(amt), money(cum), pct(cum / price.v)];
  })
);
const depTotal = deposits.reduce((t, [, a]) => t + a, 0);
w(
  depTotal === price.v
    ? `Schedule reconciles to the ${money(price.v)} commission price exactly.`
    : `**Schedule does not reconcile.** Sums to ${money(depTotal)} against a ${money(price.v)} price, a ${money(depTotal - price.v)} discrepancy.`
);
w();
w(`Cash position matters more than the total. Antipode holds ${money(deposits[0][1] + deposits[1][1])} before body and paint is committed, and the donor is bought with buyer funds, so peak own-cash exposure stays low. Insurance must still cover full work-in-progress value, because the atelier is holding a customer's asset it did not pay for.`);
w();

// --- 8. Five-year projection -------------------------------------------------
w('## 8. Five-year projection');
w();
w('Volumes and the price ladder are PLAN-A assumptions. Costs are inflated 3% a year. Shown under scenario A and scenario B so the labour-rate question stays visible across the ramp.');
w();
const ladder = [
  { year: 1, cars: 2, price: 975_000 },
  { year: 2, cars: 3, price: 975_000 },
  { year: 3, cars: 4, price: 1_050_000 },
  { year: 4, cars: 5, price: 1_100_000 },
  { year: 5, cars: 6, price: 1_150_000 },
];
const INFL = 0.03;

for (const [label, rate, fixedBase] of [
  ['Scenario A (internal cost rate A$120/hr)', labourRate.internalCost.v, leanTotal],
  ['Scenario B (market shop rate A$160/hr)', labourRate.shopLow.v, leanTotal],
]) {
  w(`### ${label}`);
  w();
  let cumProfit = 0;
  table(
    ['Year', 'Cars', 'Price', 'GP/car', 'Gross profit', 'Fixed cost', 'Operating result', 'Cumulative'],
    ladder.map((y) => {
      const infl = Math.pow(1 + INFL, y.year - 1);
      const e = unitEconomics({ buildHours: hours.planA.v, rate: rate * infl, commission: y.price });
      const inflatedCogs = (sum(cogsExLabour) * infl) + e.labour;
      const gp = y.price - inflatedCogs;
      const grossTotal = gp * y.cars;
      // Fixed cost grows for the panel/paint lead and second tech from year 2.
      const fixed = (y.year === 1 ? fixedBase : fixedBase + addPanelPaintLead.v + addSecondTech.v) * infl;
      const op = grossTotal - fixed;
      cumProfit += op;
      return [
        y.year,
        y.cars,
        money(y.price),
        money(gp),
        money(grossTotal),
        money(fixed),
        money(op),
        money(cumProfit),
      ];
    })
  );
}
w('Scenario B never compounds. Under a market labour rate the price ladder in PLAN-A does not rise fast enough to outrun the cost of the hours, which means the price ladder and the services agreement have to be negotiated as one decision, not two.');
w();

// --- 9. What would have to be true ------------------------------------------
w('## 9. What has to be true for the plan to work');
w();
table(
  ['#', 'Must be true', 'Current status', 'How to close it'],
  [
    ['1', `Build hours land at or under ~3,500 (not Theon's 6,000)`, 'Unvalidated assumption', 'Time the first car properly, by stage, from teardown'],
    ['2', 'Workshop hours charged to the JV at or near internal cost', 'Contradicts PLAN-A rec. 3 (arm\'s-length rate)', 'Settle the services agreement and equity split as one negotiation'],
    ['3', 'LCT out of scope for a re-manufactured classic', 'Unresolved in both plans', 'ATO private binding ruling before the first invoice'],
    ['4', 'Outsourced paint and trim hold at A$105k combined', 'Unvalidated assumption', 'Get three written quotes each'],
    ['5', 'Two foundation commissions inside 6 months of launch PR', 'Unproven demand', 'Waitlist with real A$100k deposits, not expressions of interest'],
    ['6', 'Donor supply at or under A$130k', 'Supported: AU index avg A$114k, trend down 19%', 'Buyer-supplied donors as the fallback'],
  ]
);
w('Items 1, 2 and 3 are the ones that decide whether this is a 35% margin business or a loss-making one. All three are closeable in the first 90 days, and none of them requires building a car to answer, which is the strongest argument for sequencing the cheap answers before the expensive commitment.');
w();

// --- 10. Three-tier ladder --------------------------------------------------
w('## 10. The three-tier commission ladder');
w();
w('A separate concept (see `docs/08-concept-review.md`) proposed three price points instead of one, on the reasoning that a lower entry tier widens a thin buyer pool. Tested here, because it is the one genuinely new commercial idea in that concept and it changes the answer to risk R9.');
w();
w('Each tier carries its own specification, so COGS moves with price. Hours and the non-labour delta are assumptions and are the first thing to replace with real quotes.');
w();

const tiers = [
  {
    name: 'Heritage',
    price: 850_000,
    hours: 2_400,
    cogsDelta: -30_000,
    note: 'Rebuilt 3.4L, standard arches, trim to sample. No widebody, no carbon',
  },
  {
    name: 'Signature',
    price: 1_150_000,
    hours: 3_000,
    cogsDelta: 0,
    note: 'The specified car: subtle widebody, full upgrade menu',
  },
  {
    name: 'Export',
    price: 1_600_000,
    hours: 3_800,
    cogsDelta: 95_000,
    note: 'Adds LHD conversion, homologation and freight. Out of Phase 0 scope',
  },
];

function tierEcon(t, rate) {
  const labour = t.hours * rate;
  const cogs = sum(cogsExLabour) + t.cogsDelta + labour;
  return { labour, cogs, gross: t.price - cogs, margin: (t.price - cogs) / t.price };
}

for (const [label, rate] of [
  ['At the internal cost rate (A$120/hr)', labourRate.internalCost.v],
  ['At a market shop rate (A$160/hr)', labourRate.shopLow.v],
]) {
  w(`### ${label}`);
  w();
  table(
    ['Tier', 'Price', 'Hours', 'COGS', 'Gross profit', 'Margin', 'Specification'],
    tiers.map((t) => {
      const e = tierEcon(t, rate);
      return [
        t.name,
        money(t.price),
        t.hours.toLocaleString('en-AU'),
        money(e.cogs),
        money(e.gross),
        pct(e.margin) + (e.margin < 0.2 ? ' !' : ''),
        t.note,
      ];
    })
  );
}

const heritage120 = tierEcon(tiers[0], labourRate.internalCost.v);
const heritage160 = tierEcon(tiers[0], labourRate.shopLow.v);
const sig120 = tierEcon(tiers[1], labourRate.internalCost.v);

w(`The entry tier carries its weight on margin and still fails on positioning. At ${money(tiers[0].price)} the Heritage car returns ${pct(heritage120.margin)} at internal cost, which clears the ~35% constraint, because the lighter specification takes ${(tiers[1].hours - tiers[0].hours).toLocaleString('en-AU')} fewer hours. So the objection is not the margin at cost. It is two other things.`);
w();
w(`First, fragility: at a market labour rate the same car falls to ${pct(heritage160.margin)}, the worst of the three tiers, so the entry tier is where the unresolved labour-rate question (R1) bites hardest. Second, and more serious, ${money(tiers[0].price)} lands within ${money(Math.abs(tiers[0].price - 860_000))} of Theon Design, which delivers a full carbon-bodied car over roughly 6,000 hours for about A$860,000 ex-GST. Pricing there invites a direct comparison against a more deeply specified car, and it is a comparison we lose on paper.`);
w();
w(`The Signature tier is the strong one: ${money(sig120.gross)} gross at ${pct(sig120.margin)}, well above the single-price ${money(price.v)} plan, because price rises faster than hours do. Together those two findings point somewhere specific, and away from both source plans as written: two tiers, not three and not one.`);
w();

const twoTier = [
  { name: 'Foundation', price: 975_000, hours: 3_000, cogsDelta: 0 },
  { name: 'Signature', price: 1_150_000, hours: 3_400, cogsDelta: 40_000 },
];
table(
  ['Recommended ladder', 'Price', 'Hours', 'COGS', 'Gross profit', 'Margin'],
  twoTier.map((t) => {
    const e = tierEcon(t, labourRate.internalCost.v);
    return [t.name, money(t.price), t.hours.toLocaleString('en-AU'), money(e.cogs), money(e.gross), pct(e.margin)];
  })
);
w('Both sit at or just above the ~35% constraint, the A$175,000 gap between them is wide enough to mean something to a buyer without inviting a Theon comparison, and the Foundation price is the one already benchmarked against Wiedergeboren. Drop the A$850,000 entry tier, and defer Export until a second market is genuinely in scope.');
w();

const report = out.join('\n');
console.log(report);

if (process.argv.includes('--write')) {
  const { writeFileSync } = await import('node:fs');
  const { fileURLToPath } = await import('node:url');
  const { dirname, join } = await import('node:path');
  const here = dirname(fileURLToPath(import.meta.url));
  writeFileSync(join(here, 'output.md'), report + '\n');
  console.error('\n[written] model/output.md');
}
