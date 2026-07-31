# The site

Static homepage. No build step, no framework, no external requests. Open
`index.html` or serve the directory:

```sh
python3 -m http.server -d web 8000
```

## Before it goes live

**Read `ASSET-CLEARANCE.md` first.** Every render carries Porsche badging and is
not publishable as supplied. `<meta name="robots" content="noindex, nofollow">` is
set for that reason. Remove it only once that register is signed off.

Also outstanding:

- The enquiry form has `action="#"`. Wire it to the CRM endpoint, and add
  server-side validation and a spam control before launch.
- `commissions@antipodemotor.com` is a placeholder pending domain clearance
  (`docs/04-brand-clearance.md`, item C6).
- Stage labels in the commissioning section are generic ("Stage one"). Replace with
  real durations once build duration is settled.

## Structure

Eight sections, following the content specification in
`reference/plan-a-atelier.md`: hero, the car, philosophy, the build journey,
specifications, commissioning, founders, enquiry. Copy is taken from that
specification close to verbatim, with two deliberate changes:

- **ADR wording corrected.** A third concept claimed "fully ADR-compliant". A
  modified production vehicle is certified under the NSW VSCCS against the ADRs
  applicable to its original date of manufacture. The blanket claim describes the
  ICV path and would be a misrepresentation. See `docs/08-concept-review.md`.
- **A concept-render notice added.** No completed car exists. Every figure is
  captioned "concept render" and the enquiry section says so plainly.

## Deployment

Deployed to Vercel as a static site. `vercel.json` at the repo root sets
`outputDirectory: web`, so there is no build step, and adds an `X-Robots-Tag:
noindex, nofollow` response header.

That header matters and is not redundant with the `<meta name="robots">` tag: the
meta tag only covers the HTML document, while six of the ten renders still carry
Porsche badging and would otherwise be directly indexable as image URLs. **Remove
both the header and the meta tag together, once `ASSET-CLEARANCE.md` is signed
off.**

## Accessibility and mobile

Audited with a scripted pass over computed styles at 390px, 768px and 1440px.
Current state: no contrast failures, nothing below 12px, no touch target under
44x44, no horizontal overflow at any width.

Three things worth not regressing:

**Mobile navigation exists.** It previously did not: below 46rem the inline links
were `display: none`, leaving a nine-section scroll page with no way to navigate.
It is now a `<details>` disclosure, which gives a real menu with no JavaScript,
keyboard support and correct expanded state for free. Menu items are 48px tall.

**There are two ochres, and only one is for text.** `--ochre` (#a5713d) fails AA
as type at 3.7:1. `--ochre-ink` (#855426) is the same hue carried darker, measured
5.46:1 on paper and 4.92:1 on stone, and it carries the pillar labels and process
numerals. `--ochre` draws rules and graphic marks only, which are exempt. Do not
set type in `--ochre`.

**Gallery captions carry their own scrim.** They sit on photography, so contrast
cannot be guaranteed by the palette. Each has a translucent ink background rather
than relying on a text shadow over an unknown image.

## Design

Art direction per `docs/04-brand-clearance.md`: charcoal `#14150F` ground, bone
`#EDE7D8` text, a single ochre-red `#B24A24` accent, one transitional serif for
headlines and one grotesque for body. Font stacks only, no webfonts, so there is
no external request and no layout shift.

Two things worth not breaking:

**The hero eyebrow is bone, not ochre.** Over the sunset photograph the ochre
accent drops below usable contrast. `.hero .eyebrow` overrides it with a shadow.
Any new section that sits over bright photography needs the same treatment.

**The scroll reveal fails open.** `.reveal` is added by JavaScript, anything near
the viewport is revealed on the first frame, and a 2.5 second timer reveals
everything regardless. Content is never hidden unless it can certainly be shown
again. Without JS, or under `prefers-reduced-motion`, nothing is ever hidden. Keep
that guarantee: an earlier version hid everything below the fold when the observer
did not fire.

## Images

`build-images.py` generates two widths (1600 and 900) of WebP and JPEG from the
masters in `assets/renders/`, and crops 7% off the bottom to remove the
"AI 生成" watermark. Cropping does not remove Porsche badging; that needs
retouching.

```sh
python3 web/build-images.py    # needs Pillow
```

Every `<img>` carries explicit `width`/`height` and `srcset`/`sizes`. **If the
crop or the source dimensions change, update those attributes**, or the page will
shift as images load. The script prints a reminder.

Initial load is about 126 kB (HTML, CSS, hero). Below-fold images are lazy.
