# ADR-0005: Two commission tiers, not one and not three

Date: 31 July 2026. Status: proposed.

## Context

Both business plans assume a single commission price. A third concept
(`docs/08-concept-review.md`) proposed three: A$850,000 Heritage, A$1.15m
Signature, A$1.6m Export. A ladder addresses the venture's largest structural
risk, a domestic buyer pool in the low tens against two incumbents each targeting
ten cars, by widening the funnel rather than discounting.

Modelled in `model/output.md` section 10, with each tier carrying its own
specification so COGS moves with price.

## Decision

Two tiers: **Foundation A$975,000** and **Signature A$1,150,000**, both ex-donor
and ex-GST.

Drop the A$850,000 entry tier. Defer the Export tier.

## Rationale

The A$850,000 tier is not rejected on margin. At 2,400 hours it returns 37.3% at
the internal cost rate, which clears the constraint. It is rejected because:

- it falls to 26.0% at a market labour rate, the most fragile of the three tiers
  under the unresolved question in ADR-0003; and
- it sits A$10,000 below Theon Design, which delivers a full carbon-bodied car
  over roughly 6,000 hours for about A$860,000 ex-GST. That comparison is
  available to any prospective buyer and we lose it on paper.

Foundation and Signature sit at 34.9% and 37.1%, are A$175,000 apart, and neither
invites the Theon comparison. Foundation is the price already benchmarked against
Wiedergeboren, which on a like-for-like ex-GST basis is A$1,150,000 rather than
the A$1.265m both plans quote (that figure is the same price GST-inclusive).

Export is deferred rather than rejected: LHD conversion, GCC thermal packages and
managed homologation amount to a second business, and it is out of Phase 0 scope.

## Consequences

Neither price is published on the site. Commissions at this level are quoted on
application, and both plans' copy decks agree. The ladder is a sales instrument,
not a price list.

Both figures are contingent on ADR-0003 and ADR-0004. If LCT applies, or the
labour rate lands at market, the ladder is re-derived before it is quoted.
