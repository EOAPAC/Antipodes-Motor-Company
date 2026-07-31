# Render asset clearance register

Status: **none of the six renders is cleared for publication.** The site markup is
finished; the imagery is not. Read this before the site goes public, before any
render goes into a PR wave, and before anything is posted to social.

Reviewed 31 July 2026 against the trademark rules in
`docs/03-regulatory-and-tax.md` section 6.

## Why this matters

The Singer matter turned on website wording and presentation, not on how the cars
were built. Porsche Cars North America, with Porsche AG, sued Singer Vehicle
Design in February 2024 alleging unauthorised use of the 911 name, **the crest,
the stylised logo** and the 911 trade dress. The dispute moved once Singer
changed how it presented the cars.

Our own rule, already written down, is: no Porsche crest, no Porsche script, no
Porsche typography, anywhere. Every render currently in `web/assets/renders/`
breaks that rule. Publishing them as supplied would hand Porsche AG the easiest
possible complaint, in the exact category it has already litigated.

## Per-asset findings

Masters live in `web/assets/renders/*.png`. Web derivatives in
`web/assets/img/` are generated from them by `web/build-images.py`.

| Asset | Where used | Porsche IP present | Other issues |
|---|---|---|---|
| `coast-dusk-motion.png` | Hero | **Crest on bonnet** | Front plate reads "NULLARBOR", a name from a different concept (see `docs/08-concept-review.md`). Wide arches and whale tail read closer to a 930 Turbo than the specified subtle widebody |
| `outback-ochre-rear.png` | The car | **"PORSCHE" script across the rear reflector panel; "Carrera" script on the engine lid** | Worst offender of the six. Two separate word marks |
| `outback-basalt-front.png` | Full-bleed plate | **Crest on bonnet** | 930-style flares and front spoiler, beyond the specified 25 to 40 mm flare |
| `workshop-bone-rear.png` | The build | **"Carrera 3.2" script on the rear panel** | "NULLARBOR" lettering on the engine lid, wrong brand |
| `interior-cognac.png` | Specifications | **Crest on the steering wheel boss** | Otherwise the closest to the brief. Cognac leather, houndstooth centres, five dials, no screens |
| `forest-bone-front.png` | Who builds it | **Crest on bonnet** | Modern LED halo headlights, which contradict the period-correct silhouette and drift toward current-model design cues. NSW plate "PRS·11B" reads as a Porsche 911 reference and should be changed |

All six also carried an "AI 生成" (AI-generated) watermark in the lower left.
The web derivatives crop the bottom 7% to remove it. **The masters still carry
it**, so do not publish from the masters.

## Required work before publication

1. **Remove every crest and every word mark.** Retouch the bonnet crests, the
   steering-wheel crest, and the "PORSCHE", "Carrera" and "Carrera 3.2" scripts.
   Where a badge sits on a painted panel, the replacement is bare paint, not a
   substitute badge.
2. **Apply the Antipode identity instead**, in the discreet way the brand calls
   for. A small rear wordmark, as the source concept did with "NULLARBOR"
   lettering, is the right restraint. Get the placement approved once and apply it
   consistently.
3. **Re-plate the cars.** Remove "NULLARBOR" and "PRS·11B". Use neutral plates or
   none.
4. **Reconsider the LED halo headlights** in `forest-bone-front.png`. They read
   modern, they fight the period-correct positioning, and headlight design is
   exactly the sort of cue worth being conservative about.
5. **Decide on the widebody**, then make the renders consistent with it. Three of
   the six show flares closer to a 930 Turbo than the specified subtle 25 to
   40 mm. Right now the set does not depict one coherent car, which undercuts the
   single-design-authority principle in `docs/01-scope.md`.
6. **Regenerate the derivatives** from the cleared masters:
   `python3 web/build-images.py`.
7. **Keep the "concept render" captions** until a real car exists. They are on
   every figure now and they should stay there. Renders presented as photographs
   of a delivered car would be a misrepresentation under the Australian Consumer
   Law, quite apart from the trademark question.

## What is already handled in the markup

- The non-affiliation disclaimer is in the footer, verbatim from
  `docs/03-regulatory-and-tax.md`, including the client-direction wording that
  resolved the Singer dispute.
- No render is described as "a Porsche" in alt text. The approved descriptor,
  "a Porsche 911 reimagined by Antipode", is used once in the hero copy and once
  in alt text; elsewhere the car is "an Antipode car".
- Every figure carries a "concept render" caption.
- A visible notice states that no completed car has been delivered.
- `<meta name="robots" content="noindex, nofollow">` is set, so the page cannot
  be indexed while the imagery is uncleared. **Remove that tag only after this
  register is closed out.**

## Sign-off

Do not publish until both boxes are ticked.

- [ ] Retouching complete, every item above addressed, derivatives regenerated
- [ ] Reviewed by the trademark adviser engaged under `docs/06-90-day-plan.md` item 1.3
