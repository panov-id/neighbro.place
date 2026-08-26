# Screen 5 — Feed Message Actions

## Purpose

The set of actions available on a message card in the feed: like, report, block.

## Message card elements

- A like icon — visible right on the card, outside any menu.
- A **"…"** button on the card — opens report and block (settled 2026-08-26: long-press is unobvious and does not work with a mouse, a swipe fights the scroll).

## Logic

- **A like is available only if you have a live phrase of your own in the feed** (`00-mechanics_EN.md` §11). Otherwise the button is inactive and says why: a match counts only while both phrases are alive, so a like without one of your own would go nowhere.
- **A mutual like opens not a chat but an offer to talk**, accepted by both (screen 6).
- **Report.** Immediately removes the message from your feed and adds one to that message's counter; when the counter reaches the threshold — a share of the audience, not a number — the message goes for everyone. **It does not touch the author's quota.** A report names a cause from a short list: rudeness, dangerous, explicit, spam (edit of 2026-08-26).
- **Block.** Hides that author's messages from you and separates the two of you. **It does not lower the author's ceiling — settled 2026-08-26:** cutting someone's quota with one tap would let a single person quietly narrow another's voice.

## Open questions

- ~~Whether a report hides the message personally~~ — it does, immediately (`00-mechanics_EN.md` §5).
- ~~How much a report or a block lowers the quota~~ — neither lowers it at all (2026-08-26).
- ~~What an inactive like looks like~~ — settled 2026-08-26: the icon is **visible but muted**; pressing it gives the line "to like, say something yourself" and a way into the composer. Hiding it is not allowed: a person would never learn that likes exist, nor why they should publish.
