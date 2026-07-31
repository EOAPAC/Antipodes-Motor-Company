#!/usr/bin/env python3
"""Generate the Journal listing and article pages.

    python3 web/build-journal.py

Writes web/journal/index.html plus one page per article. Five pages share one
template, so the copy lives here and the design system cannot drift between them:
change the shell once and every page follows.

Every factual claim in the copy traces to reference/plan-v4-master.md. Section
references are noted against each article in ARTICLES below so they can be checked
rather than trusted.

CRO structure, applied to every article:
  - Standfirst carries the promise. It decides whether the piece gets read.
  - Reading time set, so the commitment is known before it is made.
  - Subheads work as a skim path on their own.
  - One facts panel, so a skimmer gets the numbers without the prose.
  - One soft mid-article prompt, as an aside rather than a banner.
  - Closing block states the price, the next step, and what happens after it,
    because the unknown next step is what stops enquiries.
  - Two related articles, to give the reader somewhere to go that is not "back".
"""

from __future__ import annotations

import html
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / "journal"

SITE = "Antipode Motor Co."
DISCLAIMER = (
    "Antipode Motor Co. is an independent restorer and is not affiliated with, "
    "endorsed by, or connected to Dr. Ing. h.c. F. Porsche AG. &quot;Porsche,&quot; "
    "&quot;911&quot; and &quot;Carrera&quot; are trademarks of Porsche AG, used "
    "here for descriptive purposes only. All commissions are undertaken at the "
    "direction of our clients. Imagery shown is illustrative of commission "
    "direction; no completed Antipode commission has yet been delivered. Prices "
    "are in Australian dollars, exclude GST and the donor car unless stated."
)

NAV = """    <nav class="nav-solid" aria-label="Primary">
      <a class="wordmark" href="{root}">Antipode Motor Co.</a>
      <details class="menu">
        <summary>Menu</summary>
        <ul>
          <li><a href="{root}#philosophy">Philosophy</a></li>
          <li><a href="{root}#car">The Car</a></li>
          <li><a href="{root}#build">The Build</a></li>
          <li><a href="{root}#places">The Places</a></li>
          <li><a href="{journal}">Journal</a></li>
          <li><a href="{root}#commission">Commission</a></li>
        </ul>
      </details>
    </nav>"""


# --- Articles ---------------------------------------------------------------
# facts: (label, value). body: list of (kind, content).
ARTICLES = [
    {
        "no": "01",
        "tag": "Place",
        "slug": "why-australia-changes-an-air-cooled-911",
        "title": "Why Australia changes an air-cooled 911",
        "nav_title": "Why Australia changes an air-cooled 911",
        "read": "6 min read",
        "sources": "plan-v4 §5.3, §5.4, §7.6",
        "meta_title": "Why Australia Changes an Air-Cooled 911 | Antipode Journal",
        "meta_desc": (
            "The 911 was built for autobahns, not for heat soak, dust and coarse "
            "chip. What this continent asks of a car, and the 1,500 km protocol "
            "every commission passes."
        ),
        "standfirst": (
            "Salt air, heat soak, coarse chip and distance. The 911 was engineered "
            "for autobahns and alpine passes, and Australia is neither. This is what "
            "that difference costs, and how we prove we have paid it."
        ),
        "image": ("outback-basalt-front", "A dark green Antipode commission on an inland dirt road in late afternoon light.", "Inland / Late Afternoon"),
        "facts_title": "The validation protocol",
        "facts": [
            ("Validation distance per car", "1,500 km"),
            ("Heat-soak and hot-restart testing", "42&deg;C"),
            ("Air conditioning engineered to", "45&deg;C"),
            ("Single endurance day", "1,200 km"),
            ("Results published per car", "Every car"),
        ],
        "body": [
            ("p", "A car designed in Stuttgart is designed against a set of assumptions. Ambient temperatures that rarely trouble a cooling system. Fuel of a known quality, never far away. Roads with a fine-graded surface, resurfaced on a schedule. Distances measured in the low hundreds of kilometres, between towns."),
            ("p", "Every one of those assumptions changes here. Not a little, and not occasionally."),
            ("h2", "What actually breaks"),
            ("p", "Heat is first, and it is not the ambient temperature that does the damage. It is heat soak: the engine bay temperature after the car stops, when airflow ends and the oil is still carrying the last hour into the metal around it. An air-cooled engine has no radiator to hide behind. What it has is airflow, oil volume and the discipline of the person who specified them."),
            ("p", "Dust is second, and it is more insidious because it is cumulative. Unsealed roads put fine particulate against every seal on the car at once. A door seal that is merely adequate in Europe becomes an ingress path here, and dust in a cabin is not a comfort problem. It is an interior that ages a decade in a season."),
            ("p", "Coarse-chip surfacing is third. Most Australian country roads are sealed with a chip size that transmits directly into the cabin as noise and harshness. It also works fasteners loose and finds every panel resonance a car has. A suspension tuned on European tarmac is not wrong here so much as irrelevant."),
            ("pull", "Would this component endure a 1,200 kilometre day on coarse chip at 42 degrees? If we cannot answer yes, it does not go on the car."),
            ("h2", "The internal test"),
            ("p", "We apply one question to every specification decision, and we apply it before cost. Would this component endure a 1,200 kilometre day on coarse chip at 42 degrees? Cooling, fuelling, sealing, paint and trim are all chosen against that question rather than against a catalogue."),
            ("p", "It is a deliberately blunt instrument. Its value is that it cannot be argued with halfway: a part either survives the day or it does not, and a component that only survives it in a mild summer has failed."),
            ("h2", "Why we publish the results"),
            ("p", "Claims about engineering are cheap, and every atelier makes them. So instead of describing our standard, we run a written protocol on every car and publish what it returned."),
            ("h3", "What each car is put through"),
            ("ul", [
                "Heat-soak and hot-restart testing at 42&deg;C, with full thermal logging rather than a single gauge reading.",
                "A dust-seal test on unsealed roads, inspected afterwards for ingress at every seal.",
                "A coarse-chip ride route, with noise and harshness measured rather than described.",
                "A 1,200 kilometre endurance day, completed in one day because that is how these cars are actually used.",
                "Dyno certification and an oil-consumption baseline, so future wear has something to be measured against.",
                "Ultraviolet and heat ageing checks on every cabin material, against a written materials protocol.",
            ]),
            ("facts", None),
            ("p", "Fifteen hundred kilometres is not a long distance for a finished car. It is long enough to find the things that only appear when a car is hot, dirty and tired, which is the state most interesting failures occur in."),
            ("aside", ("If you are weighing a commission, the validation record is the part worth reading before the brochure.", "Talk to us about a commission", "#")),
            ("h2", "What this is not"),
            ("p", "It is not a claim that the car becomes an off-road vehicle. The specification stays period-correct, and the silhouette does not change. Underbody protection and a thermal package are not styling decisions and they are not visible."),
            ("p", "It is also not a case for more technology. There are no touchscreens and no drive modes. The steering stays hydraulic and the throttle stays a cable, because the feel those systems produce is the reason to own the car at all. Engineering for this continent means the car survives the continent, not that it insulates you from it."),
            ("h2", "The point of all of it"),
            ("p", "A car that has been validated this way is not a more exciting car on a Sunday morning. It is a car you will take further, more often, with less thought about whether you should. That is the only measure of the work that matters, and it is the reason the protocol exists."),
        ],
        "close_h": "Every commission is validated, and the record travels with the car.",
        "close_p": "The results of all six tests are bound into the Build Book delivered with your car, alongside the certification file and the dyno sheets. Ask to see a validation record before you commit to anything.",
    },
    {
        "no": "02",
        "tag": "The Car",
        "slug": "the-g-body-that-learned-to-travel",
        "title": "The G-body: the shape that learned to travel",
        "nav_title": "The G-body: the shape that learned to travel",
        "read": "7 min read",
        "sources": "plan-v4 §3.4, §6.1, §6.2, §7.6",
        "meta_title": "The G-Body 911: Why 1979 to 1985 | Antipode Journal",
        "meta_desc": (
            "Galvanised steel, honest supply and a known list of weaknesses. Why the "
            "1979 to 1985 911 is the right foundation for a car meant to be driven, "
            "and what we change."
        ),
        "standfirst": (
            "Everyone else builds on the 964. We build on the car before it, for "
            "three reasons: the shell is galvanised, the supply is honest, and every "
            "weakness it has is already known and already solved."
        ),
        "image": ("workshop-bone-rear-v2", "Rear three-quarter of a bone Antipode commission at rest in the workshop, carbon ducktail and bronze wheels.", "Commission at rest, Artarmon"),
        "facts_title": "Donor economics, Australian market",
        "facts": [
            ("3.2 Carreras built", "~74,000"),
            ("911 SCs built", "~60,000"),
            ("G-body, Australian average", "~A$114,000"),
            ("964, Australian average", "~A$175,875"),
            ("Our donor window", "1979&ndash;1985"),
        ],
        "body": [
            ("p", "The fashionable donor for a reimagined 911 is the 964. It is the car the best-known houses use, and there are good reasons for that: later engineering, a stiffer shell, more modern brakes."),
            ("p", "We build on the car before it. Not because it is cheaper, though it is, but because for a car that is meant to be driven a long way in a hard climate it is the better foundation. Three reasons, in order of importance."),
            ("h2", "One: the shell is galvanised"),
            ("p", "From the mid-1970s the 911 body shell was hot-dip galvanised. For a car that will live in salt air, be driven on unsealed roads and spend forty more years outdoors, that is the single most consequential fact about it."),
            ("p", "A restoration is only as durable as what it is built on. Paint, trim and mechanicals can all be renewed. A shell that has begun to go cannot be, not honestly, and not at a price anyone should pay. Starting with galvanised steel means the work we do has somewhere permanent to sit."),
            ("h2", "Two: the supply is honest"),
            ("p", "Roughly 74,000 3.2 Carreras and 60,000 SCs were built. That depth matters in a way that is easy to underrate: it means we can reject cars."),
            ("p", "A thin donor market forces compromise. When there are only a handful of candidates, a car with marginal rust becomes tempting, and rectification beyond a certain threshold destroys the economics of the whole build. With a deep market we hold a quality floor instead, and walk away."),
            ("facts", None),
            ("p", "The price difference is real but it is not the argument. It matters because every dollar not spent on the donor is available for engineering and craftsmanship, which is what a client is actually paying for."),
            ("aside", ("Bringing your own car, or want us to find one? Both work, and about sixty per cent of commissions start with a car the client already owns.", "Read how we assess a donor", "a-car-begins-before-the-workshop")),
            ("h2", "Three: the weaknesses are known"),
            ("p", "This is the part that reassures engineers and unsettles everyone else, so it is worth saying plainly. The G-body has a specific, finite, well-documented list of weak points. All of them have known fixes, most of them from the factory itself."),
            ("p", "A known problem with a known solution is not a risk. It is a line item."),
            ("h3", "What we change, and why"),
            ("ul", [
                "<strong>Timing-chain tensioners.</strong> Pre-1984 cars use a non-pressure-fed design that is the engine's best-known failure point. Replaced with the factory's own pressure-fed Carrera-style tensioner and oil feed.",
                "<strong>The CIS airbox.</strong> A backfire can split it. A pop-off valve resolves it permanently.",
                "<strong>The clutch centre.</strong> The original rubber-centred design perishes. Replaced with a sprung centre.",
                "<strong>Dilavar head studs.</strong> They fatigue on high-mileage engines. Replaced during the rebuild, not inspected and hoped over.",
                "<strong>The 915 gearbox.</strong> Notchy synchros are characteristic rather than faulty, and a full rebuild transforms the shift without changing the character.",
                "<strong>Oil lines.</strong> Forty-year-old lines are replaced entirely. All of them.",
            ]),
            ("p", "Our donor window is 1979 to 1985, and the gearbox is part of the reason. It keeps the car in the classic silhouette, before the later transmission, in the period with the widest supply."),
            ("h2", "What we do not do"),
            ("p", "We do not chase peak power. Output lands between 210 and 260 kW, specified for mid-range torque rather than a headline figure, because mid-range is what a long drive on an open road actually uses."),
            ("pull", "There is a capacity arms race in this segment. We are not in it. Taste, provenance, drivability and story are the axes worth competing on."),
            ("p", "The bodywork follows the same logic. Arches are flared 25 to 40 millimetres, which is enough for the wheel and tyre the car needs and not a millimetre more. Panel gaps are held to 3.5 millimetres plus or minus 0.5, measured and recorded rather than eyeballed."),
            ("h2", "The result"),
            ("p", "A car that looks like the one you remember, because it is. It simply stops doing the specific things that made the original frustrating, and it does so in a way that a future owner can verify, line by line, from the record."),
        ],
        "close_h": "The foundation matters more than the specification.",
        "close_p": "Every commission starts with the same conversation about the donor, before a single decision about colour or cabin. It is the least glamorous hour of the process and the one that determines everything after it.",
    },
    {
        "no": "03",
        "tag": "Materials",
        "slug": "six-materials-that-improve-with-miles",
        "title": "Six materials that improve with miles",
        "nav_title": "Six materials that improve with miles",
        "read": "5 min read",
        "sources": "plan-v4 §5.4, §5.5, §6.2, §7.6",
        "meta_title": "Six Materials That Improve With Miles | Antipode Journal",
        "meta_desc": (
            "Leather, wool, brass, aluminium, paint and time. Choosing materials that "
            "age into a car rather than away from it, and the protocol that proves "
            "they will."
        ),
        "standfirst": (
            "Most interiors are specified to look best on the day they are handed "
            "over. We specify for the ten-thousandth kilometre instead, which turns "
            "out to be a different set of materials entirely."
        ),
        "image": ("interior-tan", "Cabin of an Antipode commission in saddle leather with houndstooth seat inserts and machined metal.", "Saddle leather, houndstooth, machined metal"),
        "facts_title": "How materials are chosen",
        "facts": [
            ("Ultraviolet and heat ageing", "Written protocol"),
            ("Materials checked on every car", "At validation"),
            ("Trim hides archived per car", "Yes"),
            ("Paint film thickness", "Logged per panel"),
            ("Specification repeated", "Never"),
        ],
        "body": [
            ("p", "There is a particular disappointment that comes about two years into owning a beautifully finished car. Nothing has broken. It simply does not look the way it did, and every individual thing that has changed is too small to complain about."),
            ("p", "That outcome is a specification decision, made years earlier by someone optimising for the handover rather than for the decade after it. It is avoidable."),
            ("h2", "The test we use"),
            ("p", "A material earns a place in the cabin if it will look better in five years than a cheaper version of itself looks new. Six pass that test consistently."),
            ("h3", "Leather"),
            ("p", "Not all of it, and not the kind specified for showroom uniformity. A heavily pigmented hide holds its finish exactly until it does not, and then it cracks. A more lightly finished hide marks in the first month, which is the moment most owners find alarming, and then spends the next decade developing a patina that cannot be bought. The first month is the price of the next ten years."),
            ("h3", "Wool"),
            ("p", "Wool seat inserts, usually houndstooth, are not nostalgia. Wool breathes in a way leather cannot, which matters in a car with a black roof and a 42 degree afternoon. It also wears rather than degrading: the surface softens where you sit and stays intact."),
            ("h3", "Brass"),
            ("p", "Used sparingly, on the things a hand actually touches. Brass takes on the oils of the person using it and darkens unevenly, most where it is touched most. A gear knob that records how the car has been used is a better object than one that stays factory-new."),
            ("h3", "Aluminium"),
            ("p", "Machined and left largely alone. An anodised finish is a coating, and coatings fail. Bare machined aluminium develops a soft grey bloom and is still the same metal underneath. It can be brought back with a cloth in a way a failed coating never can."),
            ("h3", "Paint"),
            ("p", "Chosen to live outdoors, which rules out a surprising number of otherwise beautiful finishes. Film thickness is measured and recorded panel by panel, because thickness determines how many times the paint can be corrected across its life. A car that cannot be polished again in fifteen years has been finished badly, however good it looks now."),
            ("h3", "Time"),
            ("p", "The sixth material, and the only one we cannot buy. Every choice above is a bet that the car will be driven. A cabin specified this way looks its worst in a garage and its best after a long trip, which is precisely the incentive we want to create."),
            ("facts", None),
            ("h2", "How we know, rather than hope"),
            ("p", "Every material in the cabin is checked against a written ultraviolet and heat ageing protocol, and those checks are part of the validation run on every car rather than a one-off qualification done years ago on a sample."),
            ("pull", "We archive the hides. Every commission's leather, carpet and material off-cuts are kept, so a repair in year twelve is invisible instead of approximate."),
            ("p", "That archive is the part owners tend not to expect. A damaged seat bolster eight years from now is repaired from the same hide, from the same batch, rather than from the closest match available. The difference between those two outcomes is the difference between a repair and a compromise."),
            ("aside", ("Specification happens in person, with the actual hides and paint samples on the table.", "Ask about the design session", "#")),
            ("h2", "One consequence worth naming"),
            ("p", "No two commissions share a specification, so none of this is a menu. The materials above are how we choose, not what you get. What you get is arrived at across a series of conversations, then recorded in the registry so it is never repeated for anyone else."),
        ],
        "close_h": "A cabin that is worth the first year is easy. The tenth is the work.",
        "close_p": "The design session happens with physical samples in Artarmon or wherever you are, and nothing is locked until you have handled the materials. It is the part of the process owners tell us they enjoyed most.",
    },
    {
        "no": "04",
        "tag": "Process",
        "slug": "a-car-begins-before-the-workshop",
        "title": "A car begins before the workshop",
        "nav_title": "A car begins before the workshop",
        "read": "6 min read",
        "sources": "plan-v4 §7.5, §7.6, §8.1",
        "meta_title": "How We Assess a Donor 911 | Antipode Journal",
        "meta_desc": (
            "A 140-point checklist, a certifier who signs before money moves, and a "
            "rust threshold we will not cross. What we look for in a donor, and what "
            "we walk away from."
        ),
        "standfirst": (
            "The most consequential decision in a commission is made before anyone "
            "picks up a tool, and it is the one clients are least prepared for: which "
            "car do we start with, and which do we refuse?"
        ),
        "image": ("workshop-lift-grey", "A finished grey Antipode commission raised on a workshop lift, with the bare shell of the next car behind it.", "Two commissions, eighteen months apart"),
        "facts_title": "Donor assessment",
        "facts": [
            ("Suitability checklist", "140 points"),
            ("Certifier signs pre-purchase", "Every car"),
            ("Independent inspections per purchase", "3&ndash;4"),
            ("Commissions using a client's own car", "~60%"),
            ("Donor on our balance sheet", "Never"),
        ],
        "body": [
            ("p", "A restoration is a bet on a shell. Everything else in the build is within our control: hours, suppliers, standards, sequence. The one variable we cannot fully know at the start is the condition of the car underneath the paint, and it is the variable most capable of destroying the economics of the whole project."),
            ("p", "So we spend disproportionate effort on the hour before the purchase."),
            ("h2", "The 140-point assessment"),
            ("p", "Every candidate car, whether we found it or you already own it, goes through the same checklist. It covers chassis-number provenance, a full rust map, accident history, matching numbers where they are relevant to value, the integrity of the original galvanising, and the quality of any previous repair."),
            ("p", "The last of those is the one that catches people out. A car that has been repaired badly is often a worse starting point than a car that has never been touched, because the previous work has to be undone before ours can begin, and undoing it is not billed as progress."),
            ("h2", "The certifier signs before the money moves"),
            ("p", "This is the step almost nobody takes, and it is the one we would keep if we could only keep one."),
            ("p", "The licensed certifier who will eventually have to approve the finished car countersigns the donor's pre-purchase inspection. Certification risk is surfaced while the car still belongs to somebody else."),
            ("pull", "Discovering a compliance problem at the end of an eighteen-month build is not a setback. It is a different, much worse project."),
            ("p", "We budget three to four paid inspections per purchase because the alternative is worse. An inspection costs several hundred dollars. Being wrong about a shell costs a year."),
            ("facts", None),
            ("h2", "The threshold we will not cross"),
            ("p", "There is a point on the rust map beyond which we decline the car, regardless of price, regardless of how well it presents, and regardless of how much the client wants that particular example."),
            ("p", "Holding that line is only possible because the G-body was built in numbers. With roughly 134,000 suitable cars produced, we can say no and find another. It is the practical benefit of an unfashionable donor choice, and it is why we made it."),
            ("aside", ("Wondering whether the car in your garage is a candidate? That assessment is the first conversation, not the last.", "Have a car assessed", "#")),
            ("h2", "Two ways in"),
            ("p", "About sixty per cent of commissions start with a car the client already owns. We assess it, tell you plainly what it is, and either proceed or explain exactly why not."),
            ("p", "The rest we source. We sweep the Australian, United States and Japanese markets against your brief, shortlist with inspection reports, and negotiate. The car is bought with your funds held in escrow and the title passes directly to you."),
            ("h3", "Why the donor never sits on our balance sheet"),
            ("p", "It is a hard rule, and it protects you rather than us. An atelier holding stock has an incentive to place the car it owns. An atelier acting as your purchasing agent has an incentive to find the right one. The structure decides which of those you are dealing with, so we fixed the structure."),
            ("p", "Our fee for the search is deliberately modest. The concierge exists to control donor quality and keep the pipeline moving, not to earn margin on a car."),
            ("h2", "What comes back to you"),
            ("p", "Where the original engine block is sound it is rebuilt rather than replaced. Any numbered component that does come off the car is crated, documented and returned to you with the finished commission."),
            ("p", "That is not sentiment. It preserves the option of reversion and it protects matching-numbers value for whoever owns the car after you, which is a real number on a real invoice one day."),
            ("h2", "The unglamorous conclusion"),
            ("p", "None of this is the part of the process anyone photographs. It is a checklist, some inspection invoices and a difficult conversation about a car somebody has already fallen for. It is also the reason the eighteen months that follow go the way they are supposed to."),
        ],
        "close_h": "Start with the car, not the colour.",
        "close_p": "The first conversation is about the donor and nothing else: what you have, or what we should look for. It costs you nothing and it is the point at which most surprises get removed from the project.",
    },
]

CLOSE_PRICE = (
    "Commissions from <b>A$975,000</b>, excluding the donor car. "
    "The first three are offered as a founders series at <b>A$895,000</b>."
)
CLOSE_FINE = (
    "A commissioning deposit follows the first conversation, not the enquiry. "
    "Nothing is payable to talk to us."
)


def esc(t: str) -> str:
    return t


def render_body(blocks, art, others) -> str:
    parts = []
    for kind, content in blocks:
        if kind == "p":
            parts.append(f"          <p>{content}</p>")
        elif kind == "h2":
            parts.append(f"          <h2>{content}</h2>")
        elif kind == "h3":
            parts.append(f"          <h3>{content}</h3>")
        elif kind == "pull":
            parts.append(f'          <blockquote class="pull">{content}</blockquote>')
        elif kind == "ul":
            items = "\n".join(f"            <li>{i}</li>" for i in content)
            parts.append(f"          <ul>\n{items}\n          </ul>")
        elif kind == "facts":
            rows = "\n".join(
                f"              <div><dt>{lab}</dt><dd>{val}</dd></div>"
                for lab, val in art["facts"]
            )
            parts.append(
                f'          <aside class="facts">\n'
                f'            <p class="facts-title">{art["facts_title"]}</p>\n'
                f"            <dl>\n{rows}\n            </dl>\n"
                f"          </aside>"
            )
        elif kind == "aside":
            text, link_label, target = content
            href = "../#enquire" if target == "#" else f"{target}"
            parts.append(
                f'          <aside class="aside-cta">\n'
                f"            <p>{text} <a href=\"{href}\">{link_label}</a></p>\n"
                f"          </aside>"
            )
    return "\n".join(parts)


def related_cards(art) -> str:
    others = [a for a in ARTICLES if a["slug"] != art["slug"]][:2]
    cards = []
    for o in others:
        cards.append(
            f'            <a class="j-card" href="{o["slug"]}">\n'
            f'              <p class="j-no">No. {o["no"]}</p>\n'
            f'              <h3>{o["title"]}</h3>\n'
            f'              <p>{o["meta_desc"].split(".")[0]}.</p>\n'
            f'              <p class="j-more">Read this</p>\n'
            f"            </a>"
        )
    return "\n".join(cards)


def picture(stem, alt, cls="", width=1600, height=900, prefix="../", lazy=True):
    load = ' loading="lazy"' if lazy else ' fetchpriority="high"'
    c = f' class="{cls}"' if cls else ""
    return (
        f"          <picture>\n"
        f"            <source\n"
        f'              type="image/webp"\n'
        f'              srcset="{prefix}assets/img/{stem}@900.webp 900w, {prefix}assets/img/{stem}.webp 1600w"\n'
        f'              sizes="(max-width: 1200px) 100vw, 1200px"\n'
        f"            />\n"
        f"            <img\n"
        f'              src="{prefix}assets/img/{stem}.jpg"\n'
        f'              srcset="{prefix}assets/img/{stem}@900.jpg 900w, {prefix}assets/img/{stem}.jpg 1600w"\n'
        f'              sizes="(max-width: 1200px) 100vw, 1200px"\n'
        f'              alt="{alt}"\n'
        f'              width="{width}"\n'
        f'              height="{height}"{c}{load}\n'
        f'              decoding="async"\n'
        f"            />\n"
        f"          </picture>"
    )


def head(title, desc, og_title, og_desc, prefix="../", canonical="") -> str:
    return f"""    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{title}</title>
    <meta name="description" content="{desc}" />
    <link rel="canonical" href="{canonical}" />
    <meta name="theme-color" content="#edeee8" />

    <meta property="og:type" content="article" />
    <meta property="og:site_name" content="{SITE}" />
    <meta property="og:locale" content="en_AU" />
    <meta property="og:title" content="{og_title}" />
    <meta property="og:description" content="{og_desc}" />
    <meta property="og:image" content="/assets/og/antipode-og.jpg" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{og_title}" />
    <meta name="twitter:description" content="{og_desc}" />
    <meta name="twitter:image" content="/assets/og/antipode-og.jpg" />
    <link
      rel="icon"
      href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%231c1a17'/%3E%3Ccircle cx='16' cy='16' r='7' fill='none' stroke='%23a5713d' stroke-width='2.5'/%3E%3Ccircle cx='16' cy='16' r='2' fill='%23f4f1ea'/%3E%3C/svg%3E"
    />
    <link rel="stylesheet" href="{prefix}styles.css" />"""


def footer() -> str:
    return f"""    <footer>
      <div class="footer-top">
        <span>Antipode Motor Co. &middot; Sydney, Australia</span>
        <span>&copy; 2026</span>
      </div>
      <p class="disclaimer">{DISCLAIMER}</p>
    </footer>"""


def build_article(art) -> str:
    stem, alt, cap = art["image"]
    ld = {
        "headline": art["title"],
        "description": art["meta_desc"],
    }
    return f"""<!DOCTYPE html>
<!-- Generated by web/build-journal.py. Edit the copy there, not here. -->
<html lang="en-AU">
  <head>
{head(art["meta_title"], art["meta_desc"], art["title"], art["standfirst"], canonical=f'/journal/{art["slug"]}')}

    <script type="application/ld+json">
      {{
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": "{ld["headline"]}",
        "description": "{ld["description"]}",
        "inLanguage": "en-AU",
        "isPartOf": {{ "@type": "Blog", "name": "The Antipode Journal" }},
        "publisher": {{ "@type": "Organization", "name": "{SITE}" }}
      }}
    </script>
  </head>
  <body>
    <a class="skip" href="#article">Skip to content</a>

{NAV.format(root="../", journal="./")}

    <p class="breadcrumb">
      <a href="../">Home</a><span>/</span><a href="./">Journal</a><span>/</span>No.
      {art["no"]}
    </p>

    <article class="article" id="article">
      <div class="article-head">
        <p class="article-meta">
          <span>No. {art["no"]}</span><span class="dot">&middot;</span>
          <span>{art["tag"]}</span><span class="dot">&middot;</span>
          <span class="read">{art["read"]}</span>
        </p>
        <h1>{art["title"]}</h1>
        <p class="standfirst">{art["standfirst"]}</p>
      </div>

      <figure class="article-figure">
{picture(stem, alt, height=900)}
        <figcaption>{cap}</figcaption>
      </figure>

      <div class="article-body">
{render_body(art["body"], art, ARTICLES)}
      </div>

      <div class="article-close">
        <div class="inner">
          <p class="eyebrow-2">Begin a Commission</p>
          <h2>{art["close_h"]}</h2>
          <p>{art["close_p"]}</p>
          <p class="price-line">{CLOSE_PRICE}</p>
          <a class="btn" href="mailto:commissions@antipodemotor.com"
            >Request a Private Conversation</a
          >
          <p class="fineprint">{CLOSE_FINE}</p>
        </div>
      </div>

      <section class="related">
        <div class="related-head">
          <p class="eyebrow-2">Also in the Journal</p>
        </div>
        <div class="wrap-wide">
          <div class="journal-grid">
{related_cards(art)}
          </div>
        </div>
      </section>
    </article>

{footer()}
  </body>
</html>
"""


def build_listing() -> str:
    cards = []
    for a in ARTICLES:
        cards.append(
            f'            <a class="j-card" href="{a["slug"]}">\n'
            f'              <p class="j-no">No. {a["no"]}</p>\n'
            f'              <h3>{a["title"]}</h3>\n'
            f'              <p>{a["standfirst"]}</p>\n'
            f'              <p class="j-tag">{a["tag"]} &middot; {a["read"]}</p>\n'
            f'              <p class="j-more">Read this</p>\n'
            f"            </a>"
        )
    cards_html = "\n".join(cards)
    desc = (
        "Engineering essays, validation reports and notes on materials from the "
        "Antipode workshop in Sydney. Four pieces, no advertorial."
    )
    return f"""<!DOCTYPE html>
<!-- Generated by web/build-journal.py. Edit the copy there, not here. -->
<html lang="en-AU">
  <head>
{head("The Journal | Antipode Motor Co.", desc, "The Antipode Journal", desc, prefix="../", canonical="/journal/")}
  </head>
  <body>
    <a class="skip" href="#listing">Skip to content</a>

{NAV.format(root="../", journal="./")}

    <p class="breadcrumb"><a href="../">Home</a><span>/</span>Journal</p>

    <main class="listing" id="listing">
      <div class="listing-head">
        <p class="eyebrow-2">The Journal</p>
        <h1>Notes from the long way home.</h1>
        <p class="standfirst">
          What a continent asks of a car, what we change and why, and what the
          validation actually returned. Written in the workshop, not by an agency.
        </p>
      </div>

      <div class="wrap-wide">
        <div class="journal-grid">
{cards_html}
        </div>
      </div>

      <div class="article-close">
        <div class="inner">
          <p class="eyebrow-2">Begin a Commission</p>
          <h2>Two to six cars a year. The conversation comes first.</h2>
          <p>
            If any of this is the way you think about cars, the next step is a
            conversation about the one you would build. No deposit, no obligation.
          </p>
          <p class="price-line">{CLOSE_PRICE}</p>
          <a class="btn" href="mailto:commissions@antipodemotor.com"
            >Request a Private Conversation</a
          >
          <p class="fineprint">{CLOSE_FINE}</p>
        </div>
      </div>
    </main>

{footer()}
  </body>
</html>
"""


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "index.html").write_text(build_listing())
    print(f"  journal/index.html")
    for art in ARTICLES:
        path = OUT / f'{art["slug"]}.html'
        path.write_text(build_article(art))
        words = sum(
            len(re.sub(r"<[^>]+>", " ", c if isinstance(c, str) else " ".join(
                x if isinstance(x, str) else str(x) for x in (c if isinstance(c, list) else [str(c)])
            )).split())
            for _, c in art["body"] if c
        )
        print(f'  journal/{art["slug"]}.html  ({words} words, {art["sources"]})')
    print(f"\n{len(ARTICLES) + 1} pages written to {OUT.relative_to(HERE.parent)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
