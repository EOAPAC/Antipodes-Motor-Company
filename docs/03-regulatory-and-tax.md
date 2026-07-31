# Regulatory, tax and IP

Jurisdiction: New South Wales, with federal overlay. Not legal or tax advice. Every item below needs a named professional to sign off before it is relied on.

## 1. Vehicle certification in NSW

Significantly modified vehicles in NSW are certified under the Vehicle Safety Compliance Certification Scheme (VSCCS) by a certifier licensed by Transport for NSW, against VSB14 and the National Code of Practice, using the modification codes in Vehicle Standards Information sheet 6.

The build touches engine, brakes, suspension, body and seats/belts. Each of those falls under a different licensed modification code, and a certifier is only authorised within the sub-categories on their own licence. One certifier may not cover the whole build.

Operating rules:

- Engage a certifier on retainer before build one starts, not at the end. Retrofitting evidence for work already closed up is how certification fails.
- Confirm in writing which modification codes their licence covers, and identify a second certifier for any gap.
- Photograph and document every stage as it happens. Staged inspection evidence is a build-process requirement, not paperwork.
- Certification cost is modelled at A$15,000. That is an assumption and needs a quote (W3).

Plan B makes a point worth carrying: compliance is administered state by state and the states do not align. Any future interstate sale needs its own compliance path (VASS in Victoria, for example). Phase 0 assumes NSW registration only.

## 2. Individually Constructed Vehicle risk

If the original tub is replaced rather than repaired, the car risks being treated as an Individually Constructed Vehicle. That is a materially heavier path: compliance with the ADRs applicable to its date of manufacture, a new VIN issued by a signatory, no use of structural components carrying an existing vehicle identifier, and in some states a cap on how many ICV VINs one person can obtain in twelve months.

**The rule is absolute: retain, repair and seam-strengthen the original galvanised G-body shell and its VIN. Never replace the tub.**

This is not only a compliance choice. It protects vehicle identity, resale integrity, and the "restored, not built from scratch" story that the brand rests on. Zeigler/Bailey cut the original floor out and accepted the ICV path; their co-founder is on record that the regulations were harder than the engine. Antipode should not follow them there.

## 3. Luxury Car Tax

**Status: unresolved. This is the largest single financial variable in the venture and it must be settled before the first invoice.**

LCT is 33% on the GST-inclusive value above the threshold (A$80,567 general, 2025-26). The formula is:

```
LCT = (LCT value − threshold) × 10/11 × 33%
```

where LCT value is the GST-inclusive price excluding LCT itself. Note that 10/11 × 33% = 0.30 exactly, so the calculation simplifies to 30% of the excess over the threshold.

LCT generally applies only to cars imported or sold within two years of manufacture, which is why a genuinely old car is normally outside it. The unresolved question is whether re-manufacturing resets the date of manufacture for LCT purposes. Neither source plan could verify the current position.

On a A$975,000 ex-GST commission the exposure is **A$297,580**, and the consequences are set out in `model/output.md` section 6. In short: passing it on lifts the buyer's cost to A$1,370,080, which is above Wiedergeboren and inverts the pricing position; absorbing it drops the margin from 34.9% to 17.2%.

Actions:
1. Lodge an ATO private binding ruling request on the LCT treatment of a re-manufactured G-body restomod. Do this in Phase 0. It is the cheapest large risk reduction available.
2. Confirm the current-year threshold. The A$80,567 figure is the 2025-26 general threshold and the model is labelled accordingly; a sale in FY2026-27 uses that year's threshold, which is not in either source document.
3. Until the ruling lands, price with the contingency explicit in the commissioning agreement rather than absorbed silently. A A$300,000 contingency is too large to carry as goodwill.
4. Confirm GST registration and that the commissioning agreement states clearly whether quoted prices are inclusive or exclusive of GST and LCT. The Wiedergeboren price confusion (see `docs/02-strategy-decision.md` section 4) is exactly the ambiguity to avoid in our own paperwork.

## 4. Import pathways

Donors: the rolling 25-year rule covers every 1979 to 1985 car comfortably, with concessional Register of Approved Vehicles entry.

Left-hand-drive donors: cars over 30 years old can generally be registered and used without conversion in most states; those 25 to 30 years old are restricted to personal use unless converted to right-hand drive, and the rules vary by state. Prefer Australian-delivered right-hand-drive shells. They are a smaller slice of world supply but they avoid the conversion question entirely.

Export of finished cars: the United States 25-year exemption covers any pre-2001 car, so a finished G-body Antipode can be sold into the deepest restomod market in the world. Out of scope for Phase 0 (see `docs/01-scope.md`), but it is the reason the donor window matters strategically and not just for supply.

## 5. Australian Consumer Law

Anyone supplying a vehicle in trade or commerce is bound by the consumer guarantees: acceptable quality and fitness for purpose. These cannot be contracted out of. For a major failure the consumer chooses the remedy, which includes replacement or refund.

On a hand-built A$975,000 car, replacement is not a real remedy and a refund would consume roughly three cars' worth of gross profit. Plan A's risk register omits this entirely. It is now risk R4.

Actions:
1. Take specific advice on which entity supplies the vehicle to the buyer, and what that means for guarantee exposure. This is an open question (`docs/07-open-questions.md`, Q6).
2. Carry a warranty reserve in the model once the number can be estimated. It is not currently modelled, and that is a known gap rather than an oversight.
3. Do not attempt to disclaim the guarantees in the commissioning agreement. It does not work, and the attempt itself is a problem under the same Act.
4. Be scrupulous in marketing copy about what the car is and what it is not. Misrepresentation is a separate and easier breach than a quality failure.

## 6. Porsche trademark and trade dress

Porsche AG enforces its marks. Porsche Cars North America, with Porsche AG, sued Singer Vehicle Design on 26 February 2024 in the District of Delaware (No. 1:24-cv-00253) over the DLS and DLS Turbo, alleging unauthorised use of the 911 name, the crest, the stylised logo and the 911 trade dress, plus breach of a 2012 agreement. Plan A records that Porsche withdrew on 22 March 2024 after Singer amended its website to describe builds as done "at the direction of its clients"; Plan B records it as settled on undisclosed terms. Either way the lesson is in the remedy: the wording of the website was the thing that moved.

Operating rules, to be applied to every page, document, invoice and social asset without exception:

- Never market or invoice "a Porsche." Always "a Porsche 911 reimagined by Antipode."
- Keep the Antipode identity dominant in all branding.
- No Porsche crest, no Porsche script, no Porsche typography.
- Frame builds as client-directed restoration of a car the client owns or has commissioned us to source.
- Carry the non-affiliation disclaimer persistently, not once in a terms page.
- Do not copy protected design cues wholesale. A period-correct silhouette on the original shell is restoration; recreating a modern 911's signature elements is a different exposure.

The disclaimer, to be used verbatim:

> Antipode Motor Co. is an independent restorer and is not affiliated with, endorsed by, or connected to Dr. Ing. h.c. F. Porsche AG. "Porsche," "911" and "Carrera" are trademarks of Porsche AG, used here for descriptive purposes only.

This is implemented in the site footer at `web/index.html`.

## 7. Insurance

Not a regulatory requirement but it sits with them, because the exposure is structural. Under the recommended deposit schedule the atelier holds a customer-funded asset it does not own, and peak work-in-progress value approaches A$1m per car.

Brief a specialist motor-trade broker for goods-in-custody and work-in-progress cover sized to peak WIP across all cars in build simultaneously, not per car. Confirm cover is in place before the first client car enters the workshop. Modelled at A$45,000 a year, which is an assumption needing a quote.

## 8. Compliance as a selling point

Plan A's third brand pillar is compliance presented as a feature: a car you can register, insure and resell without anxiety. That is genuinely differentiated against the ICV path a competitor has taken, and it costs nothing extra to say because we are doing the work anyway. It is reflected in the site copy.
