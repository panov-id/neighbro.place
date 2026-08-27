# Screen 9 — My Messages

## Purpose

Everything a person has put into the feed and that is still alive: **phrases, offers and tables** (settled 2026-08-27). The screen used to describe phrases only — while a private person's offer is the same phrase with a discount, and there was nowhere to take it down except by finding yourself in the feed; a table appeared nowhere at all.

## Screen elements

- **A separate block on top** — the phrase being checked or waiting for its name to be accepted, with the reason for the wait (settled 2026-08-26). It takes no slot, but a person has to see that their text did not vanish, and understand why a second one cannot be sent.
- **A rejected phrase sits in the same block on top**, with the reason and the text at hand: fix it and send again (screen 4 promises this but does not say where; here, settled 2026-08-27).
- A list of what is published and not yet gone, each marked by type: phrase, offer, table.
- A countdown timer to disappearance and a manual delete button on each entry.
- A phrase and an offer carry their **like count** (settled 2026-08-27).
- A table carries the number of people sitting and a "return" button (screen 19).
- The remaining posting quota (how many of the 5 phrases are still available).

## Logic

- A message can be deleted manually at any point before its timer runs out.
- A manually deleted message disappears from the feed immediately.
- The timer and remaining quota are the same values that apply in the feed and at posting time (see screens 3 and 4, and the Moderation section).
- **The author sees the like count exactly as everyone else does.** `like_count` is a public field of the feed response (`xor.ad/docs/chat_EN.md` §8.4), and hiding it from the author would mean the node answering differently about one phrase depending on who asks. For the author it is the only sign that a phrase touched anybody: **who liked it is never disclosed to anyone**, and a like without a match stays a number. The cost is named: a number on your own is a metric, and people chase metrics; at least this one cannot grow forever, because a phrase lives 4:20.
- **Taking a phrase down frees the slot but not the ceiling.** Eight publications per 64 minutes count whether you took the phrase down or it expired (`00-mechanics_EN.md` §3): the ceiling exists precisely against taking phrases down in a loop to free a slot. So "3 of 5 free" and a refusal to publish can meet on one screen, and that is not a fault.
- **An offer occupies no slot** — offers have a quota of their own (screen 17). Nor does a table: it lives on its own span from the last move.
- **Stepping away deletes phrases along with their likes** (screen 20): coming back, a person finds this screen empty and five slots free.

## Open questions

- ~~Whether manual deletion restores the quota~~ — the slot frees that instant (`00-mechanics_EN.md` §3).
- How this screen is opened from the main interface (an icon in the feed, a separate menu item) is not defined yet.
- What "delete" means for a table with people sitting at it — closing it for everyone or simply leaving — is undecided. For a phrase and an offer deletion is unambiguous; for a table it is not.
