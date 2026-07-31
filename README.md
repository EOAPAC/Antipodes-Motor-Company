# Antipode Motor Co.

Scoping repository for a proposed Australian house building bespoke Porsche 911
restomods on 1979 to 1985 galvanised G-body donors, out of Luigi Pacelli's
Artarmon workshop in Sydney.

**Status: scoping. No entity exists, no name is cleared, no car is committed.**
Everything here is deliberately reversible.

## Start here

| If you want | Read |
|---|---|
| The strategy, and why the two business plans only appear to conflict | `docs/02-strategy-decision.md` |
| What we are building, in phases, with gates | `docs/01-scope.md` |
| The numbers, and the three assumptions that decide everything | `model/output.md` |
| What could kill it | `docs/05-risk-register.md` |
| What to do in the next 90 days | `docs/06-90-day-plan.md` |
| What is still unanswered | `docs/07-open-questions.md` |
| The adopted brand direction and voice | `docs/09-brand-direction.md` |
| Which renders can be published, and which cannot | `web/ASSET-CLEARANCE.md` |

## The three findings that matter

Two business plans were commissioned. Neither stress-tested its own assumptions.
Rebuilding the unit economics as a runnable model surfaced three things, each of
which on its own moves the venture from a 35% gross margin business to a
loss-making one.

**1. The plan contradicts itself on labour.** Plan A costs build labour at
A$120/hr internal cost, then separately recommends paying the workshop "a market
labour rate" under an arm's-length services agreement. Market rates for
specialist Porsche work are A$160 to A$250/hr. At A$160 year one breaks even at
minus A$4,000. At A$250 every car loses money before overhead. The equity split
and the hourly rate are the same economic quantity and must be negotiated
together. See `decisions/ADR-0003`.

**2. Build hours are assumed at half the only published benchmark.** Plan A
assumes 3,000 hours against Theon Design's published ~6,000. At 6,000 hours,
COGS reaches A$995,000 against a A$975,000 price. Restoring a 35% margin would
need A$1,530,769, above Wiedergeboren and near Zeigler/Bailey, which erases the
entire pricing wedge. This one cannot be answered without building a car, which
is why car one is scoped as an instrumented prototype.

**3. Luxury Car Tax is A$297,580 a car, and nobody had calculated it.** Both
plans flag LCT and defer it. Passing it on puts the buyer 8.3% *above*
Wiedergeboren, inverting the pricing strategy. Absorbing it cuts the margin from
34.9% to 17.2%. It is answerable now, for the cost of a private ruling, before
anyone buys a donor. See `decisions/ADR-0004`.

Two of the three are closeable in Phase 0 without touching a car. That is the
whole argument for the sequencing in `docs/02-strategy-decision.md`.

## Two smaller corrections to the source plans

**The Wiedergeboren price wedge is smaller than either plan thinks.** Both record
its price as either A$1.265m or "A$1.15m plus GST" and treat that as inconsistent
reporting. It is one price on two tax bases: 1,150,000 × 1.1 = 1,265,000 exactly.
Like-for-like ex-GST, Antipode undercuts by A$175,000 (15.2%), not the ~A$290,000
implied. Still a real wedge, thinner than assumed, and exactly what an adverse LCT
ruling consumes.

**Plan A has no Australian Consumer Law position.** Consumer guarantees cannot be
contracted out of, and a major failure gives the buyer choice of repair,
replacement or refund on a hand-built A$975,000 car. Plan B raises it; Plan A's
eleven-row risk register omits it entirely. Now risk R4.

## Repository map

```
docs/
  01-scope.md               Phases, gates, workstreams, what is out of scope
  02-strategy-decision.md   Reconciliation of the two plans. The core document
  03-regulatory-and-tax.md  NSW VSCCS, ICV, LCT, imports, ACL, Porsche trademark
  04-brand-clearance.md     Name clearance checklist, decision rule, visual identity
  05-risk-register.md       20 risks, merged, with owners and gate blockers
  06-90-day-plan.md         Dated to 29 October 2026, three blocks
  07-open-questions.md      19 open items, flagged by which gate they block
  08-concept-review.md      Review of a third concept: what to adopt and reject
  09-brand-direction.md     Adopted creative direction, voice, palette, structure
decisions/
  ADR-0001  Staged commitment: atelier as destination, advisory as the path
  ADR-0002  G-body donor choice
  ADR-0003  Equity split and labour rate settled together   [blocks Gate 1]
  ADR-0004  ATO private ruling on LCT                        [blocks Gate 1]
  ADR-0005  Two commission tiers, not one and not three
model/
  model.mjs                 Runnable model. Ten sections, every input sourced
  output.md                 Generated report, committed so it is reviewable
  README.md                 How to run and extend it
web/
  index.html                Brand site, cinematic editorial direction
  styles.css                Paper / ink / ochre, no dependencies
  build-images.py           Regenerates web derivatives from the masters
  ASSET-CLEARANCE.md        Per-render trademark status. Read before launch
  assets/renders/           Ten masters: four cleared, six awaiting retouching
  assets/img/               Generated WebP and JPEG, two widths
reference/
  plan-a-atelier.md         Source plan, verbatim
  plan-b-investor-grade.md  Source plan, verbatim
  plan-v3-master.md         Master plan v3, verbatim (truncated at s3.5)
  kimi-hinterland-concept.html      Third concept, verbatim
  kimi-hinterland-concept-v2.html   Third concept, second pass, verbatim
```

## Running things

```sh
node model/model.mjs              # print the model report
node model/model.mjs --write      # also regenerate model/output.md

python3 -m http.server -d web 8000   # preview the site at localhost:8000
python3 web/build-images.py          # rebuild image derivatives (needs Pillow)
```

The model has no dependencies. `web/build-images.py` needs Pillow.

## Ground rules that are not up for debate

Three operating rules are settled and should not be relitigated:

1. **Never replace the tub.** Retain, repair and seam-strengthen the original
   galvanised shell and its VIN. Replacing it risks Individually Constructed
   Vehicle reclassification and destroys the "restored, not built from scratch"
   story. `docs/03-regulatory-and-tax.md` section 2.
2. **Never market or invoice "a Porsche."** Always "a Porsche 911 reimagined by
   Antipode", with the non-affiliation disclaimer on every page and document, no
   crest, no script, and client-directed framing throughout. Section 6.
3. **No public use of the name until it clears class 12 and class 37.** Fallback
   to Verrada is pre-agreed rather than reopened under pressure.
   `docs/04-brand-clearance.md`.

## A note on the numbers

Most figures in the model are planning assumptions, and each is labelled with its
basis. They are there to be replaced with real quotes during the 90-day plan, not
to be quoted as forecasts. Where a figure could not be verified, the documents say
so rather than filling the gap.
