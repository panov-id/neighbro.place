# Screen 5 — Feed Message Actions

## Purpose

The set of actions available on a message card in the feed: like, report, block.

## Message card elements

- A like icon — visible right on the card, outside any menu.
- A hidden menu — holds report and block, triggered by an additional action (not shown directly on the card).

## Logic

- **Like.** If the like is mutual (both sides liked each other), a private chat opens between them.
- **Report.** Reduces the message author's posting quota.
- **Block.** Reduces the message author's posting quota and additionally hides that message from the feed personally for the blocker — the message stays visible to everyone else.

## Open questions

- Whether reporting also hides the message personally for the reporter (like blocking does), or only affects the author's quota.
- The exact way to trigger the hidden menu (long-press, a "..." button, a swipe) is not defined yet.
- How much reporting/blocking reduces the quota by is not defined yet.
