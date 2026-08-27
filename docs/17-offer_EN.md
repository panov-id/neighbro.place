# Screen 17 — Offer

## Purpose

A neighbourhood offer — a post with a mandatory discount, and the only form of advertising in the product. The screen was created on 2026-08-26: the mechanics referred to offers (`00-mechanics_EN.md` §3, §5) while no storefront had a screen for them. The full mechanics live in `xor.ad/docs/offers/SPEC_EN.md`; here is only what a person sees.

**There is no money here.** Placement is free, the platform takes neither payment nor barter and is not a party to the deal: the contract is between the person and the venue.

## The card in the feed

- An offer stands among ordinary phrases and is **marked as an offer** — otherwise advertising would pass itself off as a neighbour.
- The discount is **mandatory** and visible on the card; conditions are a separate line, and empty means "no conditions".
- A venue additionally gets: its name, a promo code and an external link. A private author gets neither link nor promo code.
- The button differs: a venue's card carries **"Save"**, a private author's carries a **like**, as any phrase does, and a like may lead to a conversation by the usual rules.
- The link opens through our own redirect, which can be switched off; a warning about leaving the site is shown first.

## Creating one

- A **venue** signs in by email — a separate account, not a device identity. Every location is verified by **an envelope with a code sent to its physical address**: that is the one thing making abuse expensive.
- A **private author** sets nothing up: their offer is an ordinary phrase with a non-empty discount, and they have no right to a link or a promo code. **It is entered in the composer** (screen 4): a collapsed "I'm offering a discount" line under the text, holding the value and the conditions. Until 2026-08-27 this path was promised here but there was nowhere to type the discount — the columns lived in the schema with no interface to them.
- An offer is published straight to the feed and goes through the same moderation queue as a phrase (`00-mechanics_EN.md` §5).
- **There is deliberately no auto-repeat and no scheduling.** Showing it again is done by hand, with a button.

## Logic

- **An offer takes no ordinary quota slot** (`00-mechanics_EN.md` §3): offers have their own limits — a share of the feed and a rate limit per venue. The baker stays a neighbour with their own five phrases.
- **Reports hide an offer automatically**, and a pattern of them moves the venue to `suspended`.
- **The save counter is not shown to the venue** — with free placement it is an unverifiable number, and promising it would be dishonest.

## Open questions

- ~~What marks an offer~~ — **the word "offer" and the size of the discount**, right on the card (settled 2026-08-26). A border or a background is not distinguishable in every theme, and a venue icon reads as a neighbour's avatar — advertising disguised as a person.
- What "Save" looks like once pressed, and where saved offers live, is undefined.
- The creation screen for a venue is not drawn: the fields are known from the spec, the look is not.
