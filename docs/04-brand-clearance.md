# Brand name clearance

Primary candidate: **Antipode**, trading as **Antipode Motor Co.**
Pre-agreed fallback: **Verrada**.

Nothing below authorises public use of either name. Clearance is not complete until every row in the checklist has a written result and a trademark attorney has reviewed them.

## Why Antipode

The antipode is the point on the earth diametrically opposite a given point. Australia is close to Germany's antipode, so the word carries the whole thesis without explanation: a Stuttgart icon, re-engineered at the opposite end of the world for the opposite end of the world. It is one distinctive word, it contains no Porsche mark or model designation, and the compound trading name improves both distinctiveness for registration and the odds of getting usable domains.

Naming logic in the reference set falls into three patterns: honorific (Singer honours Norbert Singer, Gunther Werks honours Gunther, variously cited as a NASA engineer or the test driver Gunther Steckonig), founder surname (Tuthill, Kalmar), and evocative heritage (Wiedergeboren, "reborn"). Antipode sits in the third group, which is the right one for a house with no eponymous engineer to honour.

## What has been checked here

Two things, both by web search on 31 July 2026, and neither is a substitute for a register search:

- **No automotive use of "Antipode" found.** A search for Antipode as a car brand, manufacturer or restomod house returned nothing. This is consistent with Plan A's finding.
- **No automotive use of "Verrada" found.** Same method, same result. Verrada remains the cleanest candidate on the automotive axis.

Plan A separately records a luxury-superyacht overlap (vessels named "Antipodean" and "Antipode II"). Marine vessels sit in a different class from land vehicles, so this is unlikely to block a class 12 registration, but it is a reason to have an attorney form a view on coexistence rather than assume.

**Not checked, and not checkable without a human:** the IP Australia register, ASIC business names, domain registration status, and the US register. IP Australia's search is a session-based application and the registrar and RDAP endpoints are unreachable from this environment. These are manual tasks and they are the ones that matter.

## Checklist

Fill in the result and date for every row. Do not proceed to public launch with any row blank.

| # | Check | Where | Search terms | Result | Date |
|---|---|---|---|---|---|
| C1 | Trade mark, class 12 (vehicles) | search.ipaustralia.gov.au | ANTIPODE; ANTIPODE MOTOR; ANTIPODE MOTOR CO | | |
| C2 | Trade mark, class 37 (repair, customisation, maintenance) | search.ipaustralia.gov.au | same three terms | | |
| C3 | Similar-mark search, both classes | search.ipaustralia.gov.au | ANTIPOD*; ANTIPODEAN; phonetic equivalents | | |
| C4 | Business name availability | asic.gov.au business names register | Antipode Motor Co.; Antipode Motor Company | | |
| C5 | Company name availability | ASIC | Antipode Motor Co. Pty Ltd | | |
| C6 | Domain, .com | any registrar WHOIS | antipodemotor.com; antipodemotorco.com; antipode.com | | |
| C7 | Domain, .com.au | auDA registrar, eligibility via the operating ABN | antipodemotor.com.au; antipodemotorco.com.au; antipode.com.au | | |
| C8 | US knock-out search | uspto.gov TESS, classes 12 and 37 | ANTIPODE; ANTIPODE MOTOR | | |
| C9 | Social handles | Instagram, YouTube, X | @antipodemotor; @antipodemotorco | | |
| C10 | Attorney opinion, including the superyacht coexistence question | Trademark attorney | Full report on C1 to C8 | | |

Note on C7: a .com.au domain requires an Australian presence, so the operating ABN must exist first. That sequences after incorporation, which is why `docs/06-90-day-plan.md` puts the .com registration in block 1 and treats .com.au as following the entity.

## Decision rule

Agreed in advance so the exercise is not reopened under pressure:

1. If C1, C2 and C3 come back clear and the attorney is comfortable, adopt Antipode. Register in class 12 and class 37.
2. If class 12 or class 37 is blocked, switch to **Verrada** and run the same checklist against it. Do not invent a third candidate, do not attempt to design around a blocking mark, and do not launch on an uncleared name while an application is pending.
3. If both are blocked, stop and reopen the naming study properly rather than settling on whatever is available.

Register in both classes even if only one is strictly needed. Class 12 covers the vehicles, class 37 covers the restoration and customisation service, and the venture does both.

## Candidates considered and rejected

From Plan A's study, retained so the reasoning is not lost:

| Candidate | Why rejected |
|---|---|
| Sundowner | Sundowner Trailer Corporation makes vehicle trailers. Direct class 12 clash |
| Brumby | Subaru Brumby model name, Brumby Aircraft, Brumby Motors Sydney. Multiple collisions |
| Meridian Autowerke | "Meridian Automotive" is crowded in the US. Dilution risk |
| Ochre, Gibber, Larapinta, Nullarbor, Marra | Uncleared, and either generic words or place names, both of which are harder to register and harder to defend |

Verrada survives as the fallback specifically because it is coined, which makes it the easiest of the set to register and defend, at the cost of carrying no story. That is the right trade for a fallback.

## Usage rules, once cleared

These bind every page, document, invoice, render and social post. They exist because of the Singer matter (see `docs/03-regulatory-and-tax.md` section 6), where website wording was the thing that resolved the dispute.

- The brand is Antipode. Porsche is descriptive context, never the product name.
- Approved descriptor: "a Porsche 911 reimagined by Antipode."
- Never "an Antipode Porsche," never "our Porsche 911," never a bare "Porsche" on an invoice.
- No Porsche crest, no Porsche script, no Porsche typography, anywhere.
- Frame every build as client-directed restoration of the client's car.
- The non-affiliation disclaimer appears on every page, not once in a terms page. Wording is fixed in `docs/03-regulatory-and-tax.md` section 6 and implemented in `web/index.html`.

## Positioning and voice, carried from Plan A

Position: rugged purity, engineered for Australia. The air-cooled 911 was built for autobahns and alpine passes. Australia is neither. Antipode takes the most plentiful and honest of the classic 911s and rebuilds it for 42-degree heat, coarse-chip country roads, dirt driveways and thousand-kilometre weekends.

Three pillars: biome-specific engineering (cooling, fuelling, sealing, paint and trim chosen for Australian conditions); the over-the-shoulder local build (one Sydney workshop, named technicians, a build journal, an open invitation to visit); and compliance as a feature (full VSCCS certification presented as a benefit, a car you can register, insure and resell without anxiety).

Voice: understated, technical, confident. Short sentences. Numbers rather than adjectives. Closer to a watchmaker's dossier than a car advertisement.

Tagline, recommended: **"Engineered for the other side of the world."**
Alternates: "The 911, rebuilt for Australia." / "Rugged purity. Built in Sydney."

## Visual identity

Implemented in `web/styles.css`.

| Token | Hex | Use |
|---|---|---|
| Charcoal | `#14150F` | Background |
| Bone | `#EDE7D8` | Primary text |
| Ochre red | `#B24A24` | Single accent, used sparingly |

One quiet transitional serif for headlines, one clean grotesque for body. Large silent photography, generous negative space, no stock imagery, no sliders, no carousels. Scroll-led editorial pacing.

Palette names for paint, drawn from the Australian environment: Gibber Ochre (burnt red-brown), Nullarbor Bone (warm off-white), Wattle (muted gold-green), Basalt (near-black with green flake), Coastal Storm (deep grey-blue).
