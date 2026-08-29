# Screen 17 — Offer

## Purpose

A neighbourhood offer — a post with a mandatory discount, and the only form of advertising in the product. The screen was created on 2026-08-26: the mechanics referred to offers (`00-mechanics_EN.md` §3, §5) while no storefront had a screen for them. The full mechanics live in `xor.ad/docs/offers/SPEC_EN.md`; here is only what a person sees.

**There is no money here.** Placement is free, the platform takes neither payment nor barter and is not a party to the deal: the contract is between the person and the venue.

## The card in the feed

- An offer stands among ordinary phrases and is **marked as an offer** — otherwise advertising would pass itself off as a neighbour.
- The discount is **mandatory** and visible on the card; conditions are a separate line, and empty means "no conditions".
- **The discount's term is mandatory and sits on the card — decided 2026-08-29:** the date and time until which it holds (`discount_until`, ≤90 days). It is **not** the card's lifetime: the card leaves the feed after 4:20 like any phrase, while the discount lives until its own hour. Without this field a saved card could not honestly say whether it still holds, and "while stocks last" in the conditions covered supplies but never time.
- A venue additionally gets: its name, a promo code and an external link. A private author gets neither link nor promo code.
- The button differs: a venue's card carries **"Save"**, a private author's carries a **like**, and it leads to a conversation at once.
- **An offer can be liked without a live phrase of your own — settled 2026-08-27.** An ordinary like requires the liker to have a live phrase (`00-mechanics_EN.md` §11): otherwise no match could ever come of it, since a match counts only while both phrases are alive. On an offer the match is one-sided and the argument does not hold — and the rule without this proviso would cancel the mechanism itself: to collect stools somebody is giving away you would first have to write something of your own. The proviso is written into the spec as well (`xor.ad/docs/chat_EN.md` §8.4).
- **The language filter does not hide an offer** (`00-mechanics_EN.md` §8): the Greek bakery across the road is just as useful to a Russian-speaking neighbour. It is the only exception to the language filter.
- The link opens through our own redirect, which can be switched off; a warning about leaving the site is shown first.

## Creating one

- A **venue** signs in by email — a separate account, not a device identity. Every location is verified by **an envelope with a code sent to its physical address**: that is the one thing making abuse expensive.
- A **private author** sets nothing up: their offer is an ordinary phrase with a non-empty discount, and they have no right to a link or a promo code. **It is entered in the composer** (screen 4): a collapsed "I'm offering a discount" line under the text, holding the value and the conditions. Until 2026-08-27 this path was promised here but there was nowhere to type the discount — the columns lived in the schema with no interface to them.
- An offer is published straight to the feed and goes through the same moderation queue as a phrase (`00-mechanics_EN.md` §5).
- **There is deliberately no auto-repeat and no scheduling.** Showing it again is done by hand, with a button.

## Logic

- **An offer takes no ordinary quota slot** (`00-mechanics_EN.md` §3): offers have their own limits — a share of the feed and a rate limit per venue. The baker stays a neighbour with their own five phrases.
- **Age bands do not apply to venue offers — settled 2026-08-27.** A band separates teenagers and adults **in conversation**, and a coffee shop is not somebody to talk to: a venue has no age and no like, and no conversation is born from its card. The cost is named plainly: a teenager sees the whole commercial feed of the district, including what must not be sold to them — and what protects here is not the band but the moderation queue's stop categories, which publish such things to nobody.
- **A private person's offer disappears when they step away**, like any phrase of theirs (screen 20): "step away" deletes phrases along with their likes, and a private offer is a phrase with a non-empty discount.
- **Reports hide an offer automatically**, and a pattern of them moves the venue to `suspended`.
- **The save counter is not shown to the venue** — with free placement it is an unverifiable number, and promising it would be dishonest.
- **The click count, however, is shown, and that is not a contradiction (recorded 2026-08-29).** The screen named only what is withheld and stayed silent about the other half. The difference is what we know for certain: a click goes through our own redirect, so the number is ours and verifiable; a save sits on the device and nothing about it ever leaves. Only the **count** is kept — not who went, not when, not from which address (`xor.ad/docs/offers/SPEC_EN.md` §6.2).
- **A saved offer outlives the feed — decided 2026-08-29.** The card leaves after 4:20, while the saved one stays on the device with its discount, promo code, address and a mark saying **"no longer in the feed"**; past `discount_until` it says **"the term has passed"** and greys out rather than vanishing: a person has to understand why they were refused, not guess where it went.
  **The price is named:** this is the **first place in the product where content outlives 4:20**. So the list of saved offers is named on screen 12 among what is stored on the device, and it is erased along with the history.
  **The legal side is unsettled and moved to the roadmap** (`xor.ad/docs/roadmap_EN.md` §2): what binds a business on an expired saved card, and what to do with the copy of an offer taken down on a report.

## Open questions

- ~~What marks an offer~~ — **the word "offer" and the size of the discount**, right on the card (settled 2026-08-26). A border or a background is not distinguishable in every theme, and a venue icon reads as a neighbour's avatar — advertising disguised as a person.
- ~~Where the saved offers live~~ — **a local list on the device, and nothing about it ever leaves** (`xor.ad/docs/offers/SPEC_EN.md`; the screen kept this open although the spec answered it). What is undrawn is the button's state after the press, and the list itself.
- The creation screen for a venue is not drawn: the fields are known from the spec, the look is not.
