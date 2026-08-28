# Screen 4 — Composing

## Purpose

The screen from which anything at all appears in the feed. Opened by the "Say" button in the bottom navigation.

**Two tabs: "phrase" and "table" (settled 2026-08-27).** Until this decision there was nowhere to set a table up: screen 19 described in detail how to **sit down** at somebody's table, who removes whom and how the bands are checked — and the person who sets one up existed on no screen at all. You can only sit down at what somebody has put there, and that somebody did not exist.

## Tab "phrase"

- Text input — up to 128 characters. The limit is enforced **by the node** (`CHECK (char_length(text) BETWEEN 1 AND 128)` in `xor.ad/docs/chat_EN.md` §8.3), not by this field alone: the client is open, and a check living in it alone is a hint to the author rather than a rule of the system.
- **Mode — three buttons: alone / company / party** (edit of 2026-08-26). A selector of numbers, "1, 2, 3 … N", used to stand here, but the node stores exactly the mode (`mode` = `alone | company | party`), and that is what the match card shows. An exact headcount changes nothing and adds a detail about the company that the product does not need.
- **A place can be named in words, and the point travels there (decided 2026-08-28).** A "district or city" field beside the diagram: type "Kolonaki" and the circle moves, the radius stays. It is the reverse path to what the diagram already shows as a caption, and without it the point is dragged blind: there are no streets.
  **The search runs on the device, not with us.** The list of places — districts and cities, not addresses — is delivered to the client together with the area and searched locally. So no record of "what place a person searched for" appears with us or with a third party: there is nobody to search with. This retires the earlier wording "there is no geocoding" — geocoding exists, it just lives entirely in the person's hands.
  **The price is named:** the list has to be compiled and kept small enough to hand over whole, which makes it coarse — districts and cities, no streets and no houses. "Number 14 on the embankment" cannot be found with this field, and that is not an omission.
- **The zone is a diagram with a draggable point (decided 2026-08-28)**, the same instrument as the viewing radius in the feed: the circle moves and stretches, with the place named in words and the distance from your approximate point beside it. There is no map here, as in every face (§4 of the mechanics). The zone slider ties the phrase not to a point but to an area around it. **300 m by default, from 100 m to 10 km** (the ceiling was reconciled with the spec on 2026-08-26: this said 2 km while `xor.ad/docs/chat_EN.md` §8.3 computes the coarse bounding box from a 10 km maximum — they must not diverge, and 10 was chosen). Three hundred metres hide the doorway while leaving the block recognisable. It is a privacy setting rather than a visibility one: who sees it is decided by the reader's radius, and the zone need only overlap their circle.
  **The price of the upper end is stated plainly:** a 10 km zone overlaps almost every other circle in a city, so a blur cranked to the maximum buys not silence but the opposite — almost everyone sees the phrase, they simply cannot tell where it came from. What privacy trades for here is vagueness, not invisibility.
- **A discount is an optional field (settled 2026-08-27).** Under the text, a collapsed line "I'm offering a discount"; expanded, two fields: the value as free text ("−20%", "1+1", "second coffee free") and the conditions ("first ten", "while stocks last"). Filled in, the phrase becomes a **private person's offer**, and a like on it creates a match immediately, without waiting for one back (`xor.ad/docs/offers/SPEC_EN.md`).

  There is no separate entity here and there will not be: a private offer is the same feed record with a non-empty discount, and the whole machinery of a post — geo, lifetime, like, match, chat — comes to it for free. The columns existed in the schema (`discount_value`, `conditions`) and screen 17 promised them, but there was nowhere to type them.

  A private person gets no link and no promo code — those belong to venues, and the way in there is different: email, an account, an envelope with a code to a physical address.
- **The quota remainder next to the button** (added 2026-08-28): "third of five". Until now a person learned about the limit only when refused — and the limit is hard, and this is the screen that runs into it.
- **A preview of the card** (added 2026-08-28): how the phrase will look in a neighbour's feed, with its mode label and the discount if there is one. It matters most at the first publication: until then a person has not seen a single card of someone else's from this side.
- The send button.

## Tab "table"

- Pick a game — from the same classes as in a conversation (screen 18): grid board, free table, deck and hand, dice, physics, text.
- The same blur slider: a table has a zone, and it is seen by those whose viewing circle crosses it.
- A "set it up" button.
- From there the table lives by the rules of screen 19: anyone within the radius may sit down, bands are checked each with each, the majority removes a sitter, and whoever set it up **does not become its owner** — nobody holds sole power over a table, its founder included.

## Logic

- Text is required; mode and blur radius are settings on the post.
- **Links are stripped, and the person is told so** (`00-mechanics_EN.md` §5). There are no links in the feed or in a conversation; the only place a link lives is a venue's offer. Stripping them silently would read as broken input, so the line is mandatory.
- **Publishing has two ceilings, and this is where a person meets them:** no more than **five live phrases** at once and no more than **eight in 64 minutes**. The first is about space in the neighbours' feed, the second is against someone taking their phrase down in a loop to free a slot. An offer occupies no slot; it has a quota of its own (screen 17).
- The message is text-only — no image attachment. An image is only possible on a boosted/promoted message (see the README's "Beyond the alpha" — balance and boosting section).
- On send the message goes into the **moderation queue** rather than being checked on the spot: the node accepts the phrase at once, the composer closes, and it appears **to its author** muted and labelled as being checked. It is not in anyone else's feed yet. The verdict arrives later — a 2.8 second median, a maximum near 12 (`00-mechanics_EN.md` §5). Passed, it becomes ordinary; refused, it turns into an explanation with a cause, and the text stays at hand to be fixed and sent again.
- **A person's very first phrase waits on the name as well**: the name goes into the same queue, and the phrase reaches the feed only when both are accepted. If the name is refused the phrase lies waiting until it is fixed; its 4:20 counts from publication, so waiting costs it no life. While the first one waits, a second cannot be sent.
- Sending also runs through a per-address rate limit on the node — **alongside the per-identity ceilings, not instead of them** (`xor.ad/docs/chat_EN.md` §8.3: "both limits live on the node and are tied to the identity, not the address"). It applies only to publishing in the feed, not to sending messages in a conversation. There is no external captcha.

## Open questions

- The send button's form (icon vs. text) is not defined yet.
- How switching between the "phrase" and "table" tabs looks — a toggle, segments or two buttons — is not drawn.
- ~~What happens to a half-set-up table if the person leaves the screen~~ — **the draft stays, decided 2026-08-28**, and the rule is one for both tabs. What was typed lives **on the device**, in the same encrypted storage as conversations (§9 of the mechanics), and disappears with it: on moving an identity, on recovery, and when the share burns. A draft never reaches the node — otherwise unchecked text would sit with us, which the whole construction avoids.
- How the quota remainder is shown — a number, dots or a line — is not drawn.
