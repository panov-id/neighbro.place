# Screen 9 — My Messages

## Purpose

Everything a person has put into the feed and that is still alive: **phrases, offers and tables** (settled 2026-08-27). The screen used to describe phrases only — while a private person's offer is the same phrase with a discount, and there was nowhere to take it down except by finding yourself in the feed; a table appeared nowhere at all.

## Screen elements

- **A separate block on top** — the phrase being checked or waiting for its name to be accepted, with the reason for the wait (settled 2026-08-26). It takes no slot, but a person has to see that their text did not vanish, and understand why a second one cannot be sent.
- **A rejected phrase sits in the same block on top**, with the reason and the text at hand: fix it and send again (screen 4 promises this but does not say where; here, settled 2026-08-27).
- **A restricted phrase sits in the same block, and it is a different thing from a rejected one (added 2026-09-04).** A rejected phrase was never published; a restricted one stood in the feed and was taken down. So this is not "fix it and send again" but the full Article 17 statement of reasons: what happened, why, whether automation was involved, the grounds, and what to do next (`xor.ad/docs/refusal-wordings_EN.md` §6).

  **It is shown here because there is nowhere else.** The author usually has no email — an identity is a key pair and we do not ask for electronic contact — and Art. 17(2) requires no letter in that case. The spec requires more (`xor.ad/docs/dsa/SPEC_EN.md` §7): silent removal contradicts the "a refusal is explained" principle, so the statement waits in the app and is shown at the next sign-in with that identity.

  **It lives on the device, and it cannot live anywhere else — recorded 2026-09-04 after the review panel.** The node does not keep it: a rejected `feed_messages` row is deleted and the reason goes to the author (`xor.ad/docs/chat_EN.md` §13). So the block on top can only be assembled from local storage, and it now has its own row in the table in §9. Until this edit the screen promised to show something nobody stored: close the tab as the verdict lands, and there is nothing to show.
- A list of what is published and not yet gone, each marked by type: phrase, offer, table.
- A countdown timer to disappearance and a manual delete button on each entry.
- A phrase and an offer carry their **like count** (settled 2026-08-27).
- A table carries the number of people sitting, a "return" button and a **"get up"** button (decided 2026-08-28: the table stays alive).
- **A "say it again" button** on an expiring or expired phrase (added 2026-08-28): it opens the composer with the same text. The price is named: this is a direct path to repeating the same thing forever, and the only thing holding it is the ceiling of four publications an hour.
- The remaining posting quota (how many of the 4 phrases are still available).

## Logic

- A message can be deleted manually at any point before its timer runs out.
- A manually deleted message disappears from the feed immediately.
- The timer and remaining quota are the same values that apply in the feed and at posting time (see screens 3 and 4, and the Moderation section).
- **The author sees the like count exactly as everyone else does.** `like_count` is a public field of the feed response (`xor.ad/docs/chat_EN.md` §8.4), and hiding it from the author would mean the node answering differently about one phrase depending on who asks. For the author it is the only sign that a phrase touched anybody: **who liked it is never disclosed to anyone**, and a like without a match stays a number. The cost is named: a number on your own is a metric, and people chase metrics; at least this one cannot grow forever, because a phrase lives 4:20.
- **Taking a phrase down frees the slot but not the ceiling.** Four publications per hour count whether you took the phrase down or it expired (`00-mechanics_EN.md` §3): the ceiling exists precisely against taking phrases down in a loop to free a slot. So "3 of 4 free" and a refusal to publish can meet on one screen, and that is not a fault.
- **An offer occupies no slot** — offers have a quota of their own (screen 17). Nor does a table: it lives on its own span from the last move.
- **Stepping away deletes phrases along with their likes** (screen 20): coming back, a person finds this screen empty and four slots free.

## Open questions

- ~~Whether manual deletion restores the quota~~ — the slot frees that instant (`00-mechanics_EN.md` §3).
- ~~How this screen is opened from the main interface~~ — **from the feed, where the need arises** (decided 2026-09-02). People look for their own phrases where they see them; there will be no "me" section listing screens — every screen is entered from the place that makes you want it.
- ~~What "delete" means for a table~~ — **you get up and the table lives on** (decided 2026-08-28). The same as stepping away: nobody owns a table, and one person leaving does not take the game from the others. So the table's button is labelled differently from a phrase's: "get up", not "delete".
