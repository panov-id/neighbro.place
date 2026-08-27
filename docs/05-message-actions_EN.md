# Screen 5 — Feed Message Actions

## Purpose

The set of actions available on a message card in the feed: like, hide, block, report.

## Message card elements

- A like icon — visible right on the card, outside any menu.
- A **"…"** button on the card — opens three actions (settled 2026-08-26: long-press is unobvious and does not work with a mouse, a swipe fights the scroll). They run from the quietest to the loudest: **hide the phrase**, **block the person**, **report**.

## Logic

- **A like is available only if you have a live phrase of your own in the feed** (`00-mechanics_EN.md` §11). Otherwise the button is inactive and says why: a match counts only while both phrases are alive, so a like without one of your own would go nowhere.
- **A mutual like opens not a chat but an offer to talk**, accepted by both (screen 6).
- **Hide the phrase.** The quietest action: the phrase disappears from your feed and from nowhere else. The author learns nothing, their feed does not change, the like counter is untouched, and nothing goes into the moderation queue. It is a viewer's filter, not a sanction (`xor.ad/docs/chat_EN.md` §8.9). The action returned to this screen on 2026-08-27: the spec knew about it from the start and kept a `hidden_messages` table for it, but it had no interface — a person who simply did not want to see something was left with reporting, that is, sending a neighbour into the moderation queue for not being to their taste.
- **Block.** Hides that author's messages from you and separates the two of you: the check is symmetric, so they stop seeing yours as well. It also **puts out a pending match** and **closes a shared chat** if there was one (§8.9, flow 16). **It does not lower the author's ceiling — settled 2026-08-26:** cutting someone's quota with one tap would let a single person quietly narrow another's voice.
- **Report.** Immediately removes the message from your feed and adds one to that message's counter; when the counter reaches the threshold — a share of the audience, not a number — the message goes for everyone. **It does not touch the author's quota.**

  **The notifier does not pick a category — amended 2026-08-27, reversing the list of 2026-08-26.** "Rudeness, dangerous, explicit, spam" used to stand here, and it contradicted the legal spec (`xor.ad/docs/dsa/SPEC_EN.md` §3), which says plainly: any list would be incomplete, and a wrongly chosen category obstructs the review more than its absence does. This is not settled by taste: a report is an Article 16 notice, and the rules for accepting such notices live in the legal document.

  **A justification in the person's own words is mandatory.** Without it the form does not send: an empty notice creates no "actual knowledge" under Article 16(3) and gives nothing to work from. The cost is named: reporting takes a second longer than tapping a button.

## Open questions

- ~~Whether a report hides the message personally~~ — it does, immediately (`00-mechanics_EN.md` §5).
- ~~How much a report or a block lowers the quota~~ — neither lowers it at all (2026-08-26).
- ~~What an inactive like looks like~~ — settled 2026-08-26: the icon is **visible but muted**; pressing it gives the line "to like, say something yourself" and a way into the composer. Hiding it is not allowed: a person would never learn that likes exist, nor why they should publish.
- ~~The report's category~~ — **there is none; a free-text justification instead** (2026-08-27, per the legal spec).
- How hiding differs from reporting, for a person seeing both items side by side, is not put into words on the screen. The difference is real and material: hiding goes nowhere, a report goes to a moderator.
