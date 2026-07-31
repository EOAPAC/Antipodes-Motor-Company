# Review: the "Hinterland Ateliers / Nullarbor" concept

A third concept arrived alongside the two business plans: a built landing page
branded **Hinterland Ateliers**, selling **The Nullarbor Commission**, plus six
renders. Source preserved at `reference/kimi-hinterland-concept.html`; the renders
are the masters in `web/assets/renders/`.

It is a good piece of work and it contains one commercial idea worth more than
anything in either business plan. It also contains two claims that would create
real liability if published. Both are worth being precise about.

## What to adopt

**1. Price tiers instead of a single price.** This is the genuinely new idea. Both
business plans assume one commission price. A ladder widens a thin buyer pool,
which is the venture's largest structural risk (R9), and it costs nothing to try
because the tiers differ by specification rather than by discount.

I modelled it (`model/output.md` section 10) and the answer is two tiers, not
three:

| Tier | Price ex-GST | Hours | Margin at cost rate | Verdict |
|---|---|---|---|---|
| Heritage | A$850,000 | 2,400 | 37.3% | **Drop.** Margin is fine, positioning is not |
| Signature | A$1,150,000 | 3,000 | 44.8% | **Adopt** |
| Export | A$1,600,000 | 3,800 | 48.4% | **Defer.** Out of Phase 0 scope |

The Heritage tier is the interesting rejection. Its margin is healthy at 37.3%,
because the lighter specification saves 600 hours, so this is not a margin
objection. It fails on two other counts. It is the most fragile tier under the
unresolved labour-rate question, falling to 26.0% at a market shop rate. And at
A$850,000 it sits A$10,000 below Theon Design, which delivers a full
carbon-bodied car over roughly 6,000 hours for about A$860,000 ex-GST. Inviting
that comparison is inviting a loss.

Recommended ladder: **Foundation A$975,000** and **Signature A$1,150,000**, both
at or just above the 35% constraint, A$175,000 apart, neither undercutting Theon.

**2. Name the car, not just the house.** Plan A's naming study rejected
"Nullarbor" as a house name for being an unregistrable place name. As a *model*
name it is excellent, and the objection largely falls away, because the
distinctive registrable mark is the house name carrying it. This is how the
segment works: Gunther Werks sells the Turbo, Singer sells the DLS. Adopt the
pattern. Antipode is the house; the first car can be the Nullarbor.

**3. Time-phased commissioning timeline.** Kimi's journey uses real durations
("Weeks 1–2", "Months 5–14") rather than Plan A's unnumbered five steps. Concrete
beats abstract for a buyer committing to eighteen months. Adopted structurally in
`web/index.html`, with stage labels pending the build-duration decision.

**4. The spec band.** Five or six numeric tiles as a scannable block. Adopted.

**5. Weekly workshop access, as a specific promise.** Plan A says owners may
visit; Kimi commits to weekly access and a direct line to the builder. The
specific version is more persuasive and more ownable. Worth committing to, once
capacity is understood (R8).

**6. "The anti-garage queen."** A sharp three-word statement of the whole
positioning. Better than anything in Plan A's copy deck.

## What to reject

**1. "Fully ADR-compliant" and "full ADR certification."** This is the most
serious problem in the concept, and it is repeated three times. It is not how the
regime works. A modified production vehicle retaining its original floor pan and
VIN is certified under the NSW VSCCS against the Australian Design Rules
**applicable to its original date of manufacture**, by a licensed certifier within
their licensed modification codes. A blanket claim of ADR compliance describes the
Individually Constructed Vehicle path that a competitor took, and which
`docs/03-regulatory-and-tax.md` rules out absolutely.

Publishing it would be a misrepresentation about the goods, which is a distinct
and easier breach of the Australian Consumer Law than any quality failure. Correct
wording, used in `web/index.html`: "Certified under the NSW Vehicle Safety
Compliance Certification Scheme by a licensed certifier, with the original shell
and VIN retained."

**2. No non-affiliation disclaimer, anywhere.** The footer reads "Concept
renderings shown · © 2026" and nothing else. Given that the Singer dispute turned
on website wording, this is the single most consequential omission. The verbatim
disclaimer, including the client-direction language, is now in the site footer.

**3. Six to ten cars a year.** At 3,000 hours a car this is 18,000 to 30,000 build
hours, which is roughly nine to fifteen full-time technicians on builds alone, in
a workshop whose base business is servicing and engine rebuilds. Plan A says two
cars in year one and flags the capacity conflict as a high risk; my own reading
(`docs/02-strategy-decision.md`) is that even two is optimistic and one is the
better proving programme. Six to ten is not a near-term number.

**4. A 4.0-litre, ~340 hp engine as the signature specification.** Getting 4.0
litres out of a 3.2 Carrera block is a substantial engine programme, well beyond
the A$75,000 rebuild-and-upgrade line in the model, and Wiedergeboren reached a
comparable output by sourcing a 964 3.8 rather than building up a G-body engine.
Kimi's own Heritage tier gets this right at "3.4L, ~280 hp", which sits inside
Plan A's 210 to 260 kW envelope. Either specify 3.4 to 3.6 litres, or re-cost the
engine line properly. Do not publish 4.0L until it is quoted.

**5. The light "paper" palette.** Kimi used a parchment ground (`#f4f1ea`) with
ink text and a soft ochre. Plan A specifies the inverse: charcoal `#14150F`, bone
`#EDE7D8`, one ochre-red accent `#B24A24`. The dark treatment is the agreed art
direction, it suits the photography, and it separates us from the light editorial
look most restomod houses already use. Built dark.

**6. The Export tier's LHD conversion.** Converting to left-hand drive on a car
whose value rests partly on originality is a significant engineering and
positioning decision, not a line item. Combined with GCC thermal packages and
managed homologation, this is a second business. Out of scope per
`docs/01-scope.md`, revisit in year two.

## Render assets

All six renders are strong photographically and close to Plan A's art-direction
brief. None is publishable as supplied: every one carries Porsche IP, either the
crest or the "PORSCHE" / "Carrera" word marks, which is exactly the category
Porsche AG has already litigated. Full per-asset register and the retouching
required in **`web/ASSET-CLEARANCE.md`**.

Three of the six also show flares closer to a 930 Turbo than the specified subtle
25 to 40 mm, so the set does not currently depict one coherent car. That is a
design-authority problem (R6) before it is a retouching problem.

## Net effect on the scoping

- `model/model.mjs` gains section 10, the tier-ladder analysis.
- Recommended pricing moves from one price to two: A$975,000 and A$1,150,000.
- `docs/07-open-questions.md` gains Q17 (tier ladder) and Q18 (engine capacity).
- The site is built dark, to Plan A's palette, with the ADR wording corrected and
  the disclaimer restored.
- The model-naming pattern is adopted: Antipode the house, Nullarbor the car.
