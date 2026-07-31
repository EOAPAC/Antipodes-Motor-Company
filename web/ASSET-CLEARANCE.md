# Render asset clearance register

Reviewed 31 July 2026. Ten renders in use across `index.html`.

**Four are clear. Six are not.** The page stays `noindex` until every row below
is cleared. Read this before the site goes public, before any render goes into a
PR wave, and before anything is posted to social.

## Why this matters

The Singer dispute turned on presentation, not engineering. Porsche Cars North
America, with Porsche AG, sued Singer Vehicle Design in February 2024 alleging
unauthorised use of the 911 name, **the crest, the stylised logo** and the 911
trade dress. It moved once Singer changed how it presented the cars.

Our standing rule: no Porsche crest, no Porsche script, no Porsche typography,
anywhere. Six renders currently break it.

## Cleared

The v4 set arrived crest-free, plate-free and watermark-free. This is what the
brief asked for and these four can be published once the trademark adviser signs
off the set as a whole.

| Asset | Where used | Status |
|---|---|---|
| `clifftop-basalt-front.png` | Hero | **Clear.** No crest, blank plate, no watermark |
| `forest-bone-headon.png` | Full-bleed plate | **Clear.** No crest, blank plate. Retains the LED halo headlights noted below |
| `coast-midnight-motion.png` | Gallery, "Coastal Road / Dusk" | **Clear.** No crest, blank plate |
| `interior-tan.png` | The car, cabin | **Clear.** Plain leather wheel boss, no crest. Faint watermark at the very bottom edge, cropped 4.5% in the derivative |

## Not cleared

| Asset | Where used | Porsche IP present | Also |
|---|---|---|---|
| `outback-ochre-rear-v2.png` | Gallery, "The Long Way Home" | **"PORSCHE" script across the rear panel; "Carrera 3.2" on the engine lid** | Revised version: watermark gone, badging unchanged. Two word marks, the worst of the set. QLD plate "82·GIB" |
| `workshop-bone-rear.png` | The car, rear three-quarter | **"Carrera 3.2" script on the rear panel** | "NULLARBOR" lettering on the engine lid, a name from a superseded concept |
| `outback-basalt-front.png` | Gallery, "The Interior / Late Afternoon" | **Crest on bonnet** | 930-style flares, beyond the specified 25 to 40 mm |
| `forest-bone-front.png` | Gallery, "Wet Forest / First Light" | **Crest on bonnet** | NSW plate "PRS·11B" reads as a Porsche 911 reference. LED halo headlights |
| `interior-cognac.png` | Details, cabin | **Crest on the steering wheel boss** | Otherwise closest to the original brief |
| `coast-dusk-motion.png` | Details, at speed | **Crest on bonnet** | Front plate reads "NULLARBOR" |

All six carried an "AI 生成" watermark. Derivatives crop 7% off the bottom to
remove it. **The masters still carry it**, so never publish from a master.

## Required work

1. **Remove every crest and word mark** on the six above: bonnet crests, the
   steering-wheel crest, and the "PORSCHE", "Carrera" and "Carrera 3.2" scripts.
   Replacement is bare paint, not a substitute badge.
2. **Re-plate.** Remove "NULLARBOR" and "PRS·11B". Blank plates, as the v4 set
   already does.
3. **Reconsider the LED halo headlights** in both forest renders, including the
   cleared `forest-bone-headon`. They read modern, they fight the period-correct
   positioning, and headlight treatment is worth being conservative about.
4. **Settle the widebody, then make the set consistent.** Several renders show
   flares closer to a 930 Turbo than the specified subtle 25 to 40 mm. The set
   does not yet depict one coherent car, which undercuts the single-design-authority
   principle in `docs/01-scope.md`. This is a design problem before it is a
   retouching problem.
5. **Produce the missing engine render.** The supplied direction called for an
   engine detail in the "parts you remember" section, and no engine render exists
   in the set. That slot currently holds a driving shot instead. The copy talks
   about "the rise in engine note", so the image belongs.
6. **Regenerate derivatives** after retouching: `python3 web/build-images.py`.
   Remove each retouched file's entry from `CROP_BOTTOM` in that script, since the
   crop only exists to hide the watermark.
7. **Keep the "concept visualisations" wording** until a real car exists.
   Presenting a render as a photograph of a delivered car would be a
   misrepresentation under the Australian Consumer Law, separately from the
   trademark question.

## Already handled in the markup

- Non-affiliation disclaimer in the footer, verbatim from
  `docs/03-regulatory-and-tax.md`, including the client-direction wording that
  resolved the Singer dispute, and an explicit statement that no completed
  commission has been delivered. The supplied direction had no disclaimer at all.
- No render is described as "a Porsche" in alt text or copy. The page refers to
  "an air-cooled 911" twice and to "an Antipode commission" throughout. The word
  "Porsche" appears only in the trademark notice.
- `<meta name="robots" content="noindex, nofollow">`. **Remove only after this
  register closes.**
- All images local. The supplied file pointed at upload-bucket S3 URLs, which
  would have broken as soon as those expired.

## Sign-off

- [ ] Six uncleared renders retouched, items 1 to 5 addressed, derivatives rebuilt
- [ ] Full set reviewed by the trademark adviser engaged under `docs/06-90-day-plan.md` item 1.3
