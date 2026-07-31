#!/usr/bin/env python3
"""The Commission page: the full published price ladder.

Imported by build-pages.py, which injects the shared head/nav/footer/form so
there is exactly one copy of the page shell.

The plan (reference/plan-v4-master.md section 5.6, rule 4) states that "no pricing
is ever published" and keeps the Stack A/B/C ladder internal. The founder has
overruled that: the full ladder is client-facing here, including the option items
the plan withheld. Recorded in decisions/ADR-0007.

Every figure traces to plan-v4 section 6.3 (the three stacks and the four option
lines), section 9.5 (the A$100,000 deposit and the five phases) and section 7.6
(the five build gates and the validation programme).
"""

from __future__ import annotations

# --- Data ------------------------------------------------------------------

LADDER = [
    {
        "name": "Foundation",
        "price": "A$975,000",
        "sub": "The commission most owners take",
        "engine": "3.4&ndash;3.6L rebuilt flat-six, ~210&ndash;235 kW",
        "includes": [
            "Full bare-metal restoration of the original shell, on its original VIN",
            "Every known weakness of the car resolved, not inspected and hoped over",
            "Uprated brakes and suspension, tuned for coarse-chip roads",
            "Thermal package and air conditioning engineered for 45&deg;C",
            "Bespoke wiring loom, built for this car",
            "Bespoke leather and wool interior, specified in person",
            "Full NSW VSCCS certification, registered and road-legal",
            "1,500 km validation programme, with the results published",
            "Hardbound Build Book and registry entry",
        ],
    },
    {
        "name": "Grande Travers&eacute;e",
        "price": "A$1,150,000",
        "sub": "For people who actually cross the continent",
        "engine": "3.8L+ engine programme, ~240&ndash;260 kW",
        "includes": [
            "Everything in the Foundation commission",
            "Larger-capacity engine programme with individual throttle bodies",
            "Motorsport-derived suspension, valved for long-distance compliance",
            "Long-range fuel system",
            "Underbody protection for unsealed sections",
        ],
    },
    {
        "name": "Signature",
        "price": "From A$1,600,000",
        "sub": "One car, no constraints",
        "engine": "Individually dyno-mapped, to your brief",
        "includes": [
            "Everything in the Grande Travers&eacute;e commission",
            "Bespoke bodywork developed for your car alone",
            "Individually dyno-mapped engine, with the sheet published",
            "Unlimited design consultation with the design authority",
            "Delivered personally by a founder, anywhere",
            "Export homologation and left-hand-drive conversion included",
        ],
    },
]

OPTIONS = [
    (
        "Left-hand-drive conversion",
        "A$85,000&ndash;120,000",
        "Integrated at teardown only, never retro-fitted. Required for most export markets.",
    ),
    (
        "GCC thermal package",
        "A$45,000&ndash;60,000",
        "Uprated cooling stack, oversized oil circuits, desert filtration, extreme-duty HVAC.",
    ),
    (
        "Export compliance and logistics",
        "A$25,000&ndash;40,000",
        "Homologation paperwork, freight, marine insurance and customs brokerage.",
    ),
    (
        "Ownership programme",
        "A$18,000 a year",
        "Annual service and agreed-value revaluation, registry privileges, owners' events.",
    ),
]

PAYMENTS = [
    ("A$100,000", "On signing the commission agreement"),
    ("30%", "On the shell gate, after teardown and rust rectification"),
    ("25%", "On the painted-body gate"),
    ("25%", "On the trimmed gate, interior complete"),
    ("Balance", "On certification and delivery"),
]

# Ordered by what actually stops an enquiry, not by what is easiest to answer.
FAQ = [
    (
        "Does the price include the car it is built from?",
        "No, and that is deliberate. The donor is bought in your name with your funds "
        "held in escrow and the title passes directly to you, so it never sits on our "
        "balance sheet. Budget A$90,000 to A$130,000. All in, a Foundation commission "
        "with a donor we source lands between A$1.07m and A$1.11m.",
    ),
    (
        "How long does it take?",
        "Twelve to eighteen months from the commission agreement, in five stages with a "
        "signed gate at the end of each. Most of that is not assembly. It is the "
        "fabrication and engineering months, and the validation programme at the end.",
    ),
    (
        "When do I pay, and what is at risk?",
        "A A$100,000 commissioning deposit on signing, then staged against milestones "
        "you sign off in the workshop. Never ahead of the work. Nothing is payable to "
        "have a conversation, and an enquiry commits you to nothing.",
    ),
    (
        "Can I use the 911 I already own?",
        "Usually, and about sixty per cent of commissions start that way. We assess it "
        "against a 140-point checklist first, and the licensed certifier countersigns "
        "the inspection before anyone commits money. If the shell is beyond our rust "
        "threshold we will say so, and we will not build on it.",
    ),
    (
        "Is it road-legal, and can I insure and resell it?",
        "Yes. Every car is certified under the NSW Vehicle Safety Compliance "
        "Certification Scheme by a licensed certifier, on its original shell and VIN. "
        "The certification file, dyno sheets and validation record are bound into the "
        "Build Book, which is what an insurer or a future buyer actually wants to see.",
    ),
    (
        "How is this different from the other Australian houses?",
        "On one point that matters more than any other at this price: we keep the "
        "original galvanised floor and the original VIN. Some houses cut the floor "
        "out and fit an entirely new tub. That is a legitimate engineering choice "
        "and it buys rigidity, but it is also a heavier regulatory path, because a "
        "car built that way can be treated as an Individually Constructed Vehicle "
        "and issued a new VIN. Yours is certified under the NSW scheme as your car, "
        "modified, on the identity it left the factory with. That is what an insurer "
        "underwrites and what a future buyer's inspector looks for.",
    ),
    (
        "Are you chasing the biggest engine number?",
        "No, and you should know that before you compare spec sheets. There is an "
        "Australian car at this money with a 4.4-litre and 300kW, and we are not "
        "trying to beat it. Our engines are built for a 1,200 kilometre day at "
        "42 degrees on coarse chip, which is a different brief from a peak figure, "
        "and the validation record we publish is where that shows up. If the "
        "headline number is what you are buying, we are honestly not the right "
        "house.",
    ),
    (
        "What happens if something goes wrong after delivery?",
        "We rectify it. Australian Consumer Law guarantees cannot be contracted out of "
        "and we do not try to. Beyond that we run a service-campaign policy: if a fault "
        "turns out to be systemic across the registry, every affected car is corrected "
        "without argument.",
    ),
    (
        "Why build on a G-body rather than a 964?",
        "The shell is galvanised, the supply is deep enough that we can reject cars "
        "instead of compromising, and every weakness it has is documented with a known "
        "fix. The long answer is in the Journal.",
    ),
    (
        "Is the founders-series price real?",
        "Yes, for the first three commissions only, at Foundation specification. It is "
        "A$895,000 rather than A$975,000, and it reflects the part those cars play in "
        "establishing the process.",
    ),
]

ALL_IN_LOW = "A$1.07m"
ALL_IN_HIGH = "A$1.11m"


# --- Rendering -------------------------------------------------------------


def _tiers() -> str:
    out = []
    for i, t in enumerate(LADDER):
        items = "\n".join(f"              <li>{x}</li>" for x in t["includes"])
        featured = " tier--featured" if i == 0 else ""
        badge = (
            '\n            <p class="tier-badge">Most commissioned</p>'
            if i == 0
            else ""
        )
        out.append(
            f'          <article class="tier{featured}">{badge}\n'
            f'            <h2 class="tier-name">{t["name"]}</h2>\n'
            f'            <p class="tier-price">{t["price"]}</p>\n'
            f'            <p class="tier-sub">{t["sub"]}</p>\n'
            f'            <p class="tier-engine">{t["engine"]}</p>\n'
            f'            <ul class="tier-list">\n{items}\n            </ul>\n'
            f'            <p class="tier-foot">Excludes the donor car and GST.</p>\n'
            f'            <a class="btn btn-dark tier-cta" href="#enquire">Enquire about this</a>\n'
            f"          </article>"
        )
    return "\n".join(out)


def _options() -> str:
    return "\n".join(
        f"            <div>\n"
        f"              <dt>{name}<span class=\"opt-note\">{note}</span></dt>\n"
        f"              <dd>{price}</dd>\n"
        f"            </div>"
        for name, price, note in OPTIONS
    )


def _payments() -> str:
    return "\n".join(
        f'            <li><span class="pay-amt">{amt}</span>'
        f'<span class="pay-when">{when}</span></li>'
        for amt, when in PAYMENTS
    )


def _faqs() -> str:
    return "\n".join(
        f'          <details class="faq">\n'
        f"            <summary>{q}</summary>\n"
        f'            <div class="faq-body"><p>{a}</p></div>\n'
        f"          </details>"
        for q, a in FAQ
    )


def _faq_schema() -> str:
    entries = []
    for q, a in FAQ:
        entries.append(
            "          {\n"
            '            "@type": "Question",\n'
            f'            "name": "{q}",\n'
            '            "acceptedAnswer": { "@type": "Answer", "text": '
            f'"{a}" }}\n'
            "          }"
        )
    return ",\n".join(entries)


def build(head, nav, footer, form) -> str:
    """head/nav/footer/form are the shared builders from build-pages.py."""
    title = "Commission Pricing, from A$975,000 | Antipode Motor Co."
    desc = (
        "What an air-cooled 911 commission costs, in full: three levels from "
        "A$975,000 to A$1.6m ex-donor, priced options, payment stages and timeline."
    )
    return f"""<!DOCTYPE html>
<!-- Generated by web/build-pages.py. Edit web/pages_commission.py, not here. -->
<html lang="en-AU">
  <head>
{head(title, desc, "What an Antipode commission costs", desc, prefix="../", canonical="/commission/")}

    <script type="application/ld+json">
      {{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
{_faq_schema()}
        ]
      }}
    </script>
  </head>
  <body>
    <a class="skip" href="#pricing">Skip to content</a>

{nav(current="commission")}

    <p class="breadcrumb"><a href="../">Home</a><span>/</span>Commission</p>

    <main id="pricing">
      <div class="listing">
        <div class="listing-head">
          <p class="eyebrow-2">The Commission</p>
          <h1>What a commission costs.</h1>
          <p class="standfirst">
            Three levels, priced openly. Most houses at this level will not tell you
            until you have asked twice, which wastes your time and ours.
          </p>
          <p class="listing-note">
            Every figure excludes GST and the donor car. All in, a Foundation
            commission with a donor we source for you lands between
            <b>{ALL_IN_LOW} and {ALL_IN_HIGH}</b>.
          </p>
        </div>

        <div class="wrap-wide">
          <div class="tiers">
{_tiers()}
          </div>
        </div>

        <p class="keeps-note">
          <b>Every commission keeps the car it started as.</b> We retain, repair
          and seam-strengthen the original galvanised shell and its VIN, and
          certify it under the NSW scheme as your car, modified. We do not cut the
          floor out and fit a new tub, which would put the car on the Individually
          Constructed Vehicle path and a new VIN.
        </p>

        <p class="founders-note">
          <b>Founders series.</b> The first three commissions are
          <b>A$895,000</b> at Foundation specification, in recognition of the part
          they play in establishing the process.
        </p>

        <section class="block">
          <p class="eyebrow-2">Priced options</p>
          <h2>Added at teardown, not afterwards.</h2>
          <p class="block-lede">
            Anything here has to be designed in from the start. That is why they
            are priced separately rather than offered later.
          </p>
          <dl class="terms-dl">
{_options()}
          </dl>
        </section>

        <section class="block">
          <p class="eyebrow-2">Payment</p>
          <h2>Staged against work, never ahead of it.</h2>
          <ol class="pay-steps">
{_payments()}
          </ol>
          <p class="block-note">
            Twelve to eighteen months, five gates. Each one is signed off by you
            in the workshop before the next payment falls due.
          </p>
        </section>

        <section class="block" id="faq">
          <p class="eyebrow-2">Before you ask</p>
          <h2>The questions everyone asks.</h2>
{_faqs()}
        </section>
      </div>

{form()}
    </main>

{footer()}
  </body>
</html>
"""
