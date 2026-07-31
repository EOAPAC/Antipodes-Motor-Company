# Render asset clearance register

Reviewed 31 July 2026. Eleven masters, all eleven in use across `index.html`.

**Six are clear. Five are not.** Improved from four-of-ten last pass: two badged
masters were retired because clean equivalents arrived, and two new clean renders
came in, one of which closes a gap that had been open since the first review.

Indexing is not gated on this register, by decision, so the site is live and
indexable while the remaining work is outstanding. The Open Graph share image uses
a cleared render, since it is the single most widely distributed asset on the site.

## Why this matters

The Singer dispute turned on presentation, not engineering. Porsche Cars North
America, with Porsche AG, sued Singer Vehicle Design in February 2024 alleging
unauthorised use of the 911 name, **the crest, the stylised logo** and the 911
trade dress. It moved once Singer changed how it presented the cars.

Our standing rule: no Porsche crest, no Porsche script, no Porsche typography,
anywhere. Five renders currently break it.

## Cleared

| Asset | Where used | Status |
|---|---|---|
| `clifftop-basalt-front.png` | Hero, and the share image | **Clear.** No crest, blank plate, no watermark |
| `forest-bone-headon.png` | Full-bleed plate | **Clear.** No crest, blank plate. Retains the LED halo headlights noted below |
| `coast-midnight-motion.png` | Gallery, "Coastal Road / Dusk" | **Clear.** No crest, blank plate |
| `interior-tan.png` | The Car, cabin | **Clear.** Plain leather wheel boss. Faint mark at the very bottom edge, cropped 4.5% in the derivative |
| `workshop-bone-rear-v2.png` | The Car, rear three-quarter | **Clear, and new.** Blank rear panel, blank plate, carbon ducktail. Replaces a master that carried "Carrera 3.2" and "NULLARBOR" |
| `engine-itb.png` | The Details, engine | **Clear, and new.** Individual throttle bodies, carbon plenum, braided lines. No badging or script anywhere in the bay |

## Not cleared

| Asset | Where used | Porsche IP present | Also |
|---|---|---|---|
| `outback-ochre-rear-v2.png` | Gallery, "The Long Way Home" | **"PORSCHE" script across the rear panel; "Carrera 3.2" on the engine lid** | Two word marks, the worst of the set. QLD plate "82·GIB" |
| `workshop-lift-grey.png` | The Build | **Crest on the bonnet, and a second crest on the wall art behind** | Otherwise the strongest process image in the library: a finished car on the lift with the bare shell of the next one behind it. Worth retouching rather than dropping |
| `outback-basalt-front.png` | Gallery, "Inland / Late Afternoon" | **Crest on bonnet** | 930-style flares, beyond the specified 25 to 40 mm |
| `forest-bone-front.png` | Gallery, "Wet Forest / First Light" | **Crest on bonnet** | NSW plate "PRS·11B" reads as a Porsche 911 reference. LED halo headlights |
| `interior-cognac.png` | The Details, cabin | **Crest on the steering wheel boss** | Otherwise closest to the original brief |

Four of the eleven carried an "AI 生成" watermark and are cropped 7% or 4.5% at
the bottom in the derivative. **The masters still carry it**, so never publish
from a master. The four newest renders arrived clean and are not cropped.

## Retired this pass

| Asset | Why |
|---|---|
| `workshop-bone-rear.png` | Carried "Carrera 3.2" and "NULLARBOR". Superseded by the clean `workshop-bone-rear-v2` |
| `coast-dusk-motion.png` | Carried a bonnet crest and a "NULLARBOR" plate, and was a near-duplicate of the clean `coast-midnight-motion` |

Retiring beats retouching where a clean equivalent already exists. Both were
deleted rather than left in the library to be picked up by mistake.

## Automated patching was tried and rejected

Removing the badges programmatically was tried first, before spending money on
retouching: feathered patches sampled from adjacent paint for the crests,
horizontal samples from the reflector band for the word marks, and per-row median
fills for the plates. Coordinates were measured off grid overlays, so alignment
was not the limiting factor.

It does not work. The crests leave visible smears, the plates stay legible under
the fill, and the wheel boss and the bone rear panel come out looking damaged
rather than clean. On a seven-figure car a bad retouch is worse than a visible
badge, because it reads as carelessness about the object itself.

**The evidence now points somewhere better.** Every render that has arrived clean
arrived clean straight from generation. Regenerating the five remaining
compositions is cheaper and better than retouching them, and the engine and rear
renders are proof it works. Try that before commissioning inpainting.

## Required work

1. **Remove every crest and word mark** on the five above: bonnet crests, the
   steering-wheel crest, the wall art in the workshop shot, and the "PORSCHE" and
   "Carrera 3.2" scripts. Replacement is bare paint, not a substitute badge.
2. **Re-plate.** Remove "PRS·11B" and "82·GIB". Blank plates, as the clean set
   already does.
3. **Reconsider the LED halo headlights** in both forest renders, including the
   cleared `forest-bone-headon`. They read modern and they fight the
   period-correct positioning.
4. **Settle the widebody, then make the set consistent.** Several renders show
   flares closer to a 930 Turbo than the specified subtle 25 to 40 mm. The set
   does not yet depict one coherent car, which undercuts the
   single-design-authority principle in `docs/01-scope.md`. A design problem
   before it is a retouching problem.
5. ~~**Produce the missing engine render.**~~ **Done.** `engine-itb.png` closes
   this. The Details section now carries a real engine image rather than a
   substitute driving shot, which matters because the copy in that section talks
   about "the rise in engine note".
6. **Regenerate derivatives** after retouching: `python3 web/build-images.py`.
   Remove each retouched file's entry from `CROP_BOTTOM` in that script, since the
   crop only exists to hide the watermark.
7. **Keep the "illustrative of commission direction" wording** until a real car
   exists. Presenting a render as a photograph of a delivered car would be a
   misrepresentation under the Australian Consumer Law, separately from the
   trademark question.

## Already handled in the markup

- Non-affiliation disclaimer in the footer, with the client-direction wording that
  resolved the Singer dispute, an explicit statement that no completed commission
  has been delivered, and a pricing basis note.
- No render is described as "a Porsche" in alt text or copy. The page refers to
  "an air-cooled 911" twice and to "an Antipode commission" throughout. The word
  "Porsche" appears only in the trademark notice.
- The Open Graph share image is built from `clifftop-basalt-front`, a cleared
  render, by `web/build-og.py`.
- All images local, all with explicit dimensions and `srcset`.

## Sign-off

- [ ] Five uncleared renders retouched or regenerated, items 1 to 4 addressed, derivatives rebuilt
- [ ] Full set reviewed by the trademark adviser engaged under `docs/06-90-day-plan.md` item 1.3
