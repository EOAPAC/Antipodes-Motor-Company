# Brand direction

Adopted 31 July 2026. Supersedes the art direction in `docs/04-brand-clearance.md`
section "Visual identity". Name clearance in that document still stands unchanged.

## What changed, and why it matters

The scoping work built the first site to Plan A's specification: charcoal ground,
bone text, ochre-red accent, technical spec tables, a five-stage commissioning
process, a full enquiry form. That page reads as a well-made product page.

The direction now adopted is different in kind, not degree. Paper ground, ink
text, one ochre rule. No specification tables. No prices. No form. The car is
never described by capacity or output. The subject is the road, and the car is how
you meet it.

That is a real strategic choice and worth naming, because it changes what the
brand competes on. A spec sheet invites comparison, and comparison is a fight
Antipode loses on paper: Theon delivers a full carbon-bodied car over roughly
6,000 hours for about A$860,000 ex-GST. Removing the spec sheet removes the
comparison and moves the sale onto ground where a Sydney workshop with a named
builder and an open door is genuinely stronger. Restraint here is commercial, not
only aesthetic.

The cost is that a buyer who wants numbers has to ask. At this price point, having
to ask is not a barrier. It is the beginning of the conversation the process is
built around.

## Voice

Declarative and unhurried. Short lines with deliberate breaks, closer to set verse
than to marketing copy. Present tense. First person plural, sparingly.

The copy earns its restraint by being specific about experience rather than
specification: "the cool metal of a gear lever", "the weave of a seat insert",
"roads that continue after the map becomes less certain". Concrete sensory detail
in place of adjectives about quality.

Never: "bespoke" as a modifier on its own, "passion", "DNA", "iconic",
"uncompromising", "the pinnacle of". Never a superlative about the car. Never a
number that invites a comparison.

Tagline, retained: **Engineered for the other side of the world.**
Headline: **Cars for roads that are worth the drive.**

## Palette

| Token | Hex | Use |
|---|---|---|
| Ink | `#1c1a17` | Body text, closing section ground |
| Paper | `#f4f1ea` | Primary ground |
| Stone | `#e7e1d4` | Alternate section ground |
| Ochre | `#a5713d` | The single rule, pillar labels, process numerals |
| Eucalyptus | `#31473b` | Held in reserve, currently unused |

Serif throughout for reading. Grotesque for labels, navigation and numerals only.
System font stacks, no webfonts, so there is no external request and no layout
shift. Implemented in `web/styles.css`.

## Structure

Nine movements, in this order. The rhythm alternates copy and image deliberately;
do not add a section without deciding what it displaces.

1. Hero. Tagline as eyebrow, headline, one sentence, one call to action.
2. Philosophy. "The road is part of the design."
3. Full-bleed plate. No copy.
4. Three pillars: Distance, Feel, Belonging.
5. The car. "A familiar shape. A different sense of place." Two images, three
   qualitative statements (Air-Cooled, One Owner, Made to Go).
6. Places. Four-image gallery with place-and-time captions.
7. Details. "The parts you remember." Two images.
8. Commission. Five named stages, no durations, no prices.
9. Closing. "Begin with a road."

The three statements in movement 5 replace what would ordinarily be a spec band.
They are the load-bearing choice in the whole page: qualitative where a spec band
would be quantitative.

## The pillars

**Distance.** Early departures, changing weather, roads that continue past the
map. This carries the biome-specific engineering argument without engineering
language.

**Feel.** Steering weight, the sound behind you, the click of a switch. This is
where the air-cooled manual case gets made, sensorily rather than technically.

**Belonging.** Each commission shaped around its owner, finished to belong to a
particular life and place. This carries the one-owner, one-point-of-view model.

## Rules that survive from the earlier direction

Unchanged and not negotiable, per `docs/03-regulatory-and-tax.md` section 6:

- Never market or invoice "a Porsche." The page refers to "an air-cooled 911"
  twice; the word "Porsche" appears only in the trademark notice.
- No Porsche crest, script or typography, in imagery or type.
- The non-affiliation disclaimer appears in the footer of every page, with the
  client-direction wording. The supplied direction omitted it; it has been added.
- Concept imagery is labelled as such until a car is delivered.

## Open

- **The wordmark.** Set in the grotesque with wide tracking, which is a holding
  position rather than a designed mark. A real wordmark is outstanding.
- **The engine render.** Movement 7 calls for an engine detail and none exists.
  See `web/ASSET-CLEARANCE.md`.
- **Photography.** Every image is a concept render. The direction depends on
  photography that looks unposed and specific to place, so the first real shoot
  matters more than usual.
- **Where price appears at all.** Nowhere on the site is the right answer for
  launch. The two-tier ladder in `decisions/ADR-0005` still governs what is quoted
  in a conversation.
