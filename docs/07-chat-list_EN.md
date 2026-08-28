# Screen 7 — Conversations

## Purpose

The section holding everything to do with talking: offers waiting for an answer, and open conversations. **Edit of 2026-08-26:** this used to hold chats only, and matches appeared nowhere — even though the inbox collects them first (`xor.ad/docs/chat_EN.md` §8.12).

## Screen elements

- **Two tabs: "Offers" and "Conversations".** The counter is **on the first one only** (settled 2026-08-27), and it counts offers waiting for your answer. There is no number on "Conversations": an offer has a hard deadline and somebody else waiting, while a conversation is your own — when to return to it is not the product's call. The cost is named: someone dropping in for a minute will not learn that a conversation opened somewhere, and it may fade before they do.
- A list: one entry per offer or per conversation. A conversation's entry carries **the name, a fragment of the last line, and what is left of your own timer** (settled 2026-08-26): the timer matters more than an unread count, because a conversation dies of silence and that is the only thing requiring action.
- **A "waiting for your reply" mark** on a conversation row when the last line is theirs (added 2026-08-28). This is not a report of someone else's action: the line is already on your device, and the mark is computed there.
- **A dot on the "Conversations" tab** when a new conversation has opened since you last looked (added 2026-08-28). Not a counter and not "unread": **which conversations you have already seen is remembered by the device**, and the node neither knows nor will know about your visits. The price is accepted: the dot clears when you open the tab rather than when you read anything — and that is all it can do.
- Tap to go inside.

## Logic

- The tabs live **inside the section**, not in the bottom navigation: that has exactly four items (`Feed` / `Chats` / `Say` / `Me`), and a fifth does not fit a narrow screen (`xor.ad/docs/chat_EN.md` §9).
- An **offer** is a match waiting on acceptance — yours, theirs, or both. It disappears when either of the two phrases expires.
- A **conversation** enters the list once both have accepted, and lives until silence eats it — each side by their own count (`00-mechanics_EN.md` §2).
- **A conversation that ended for the other side stays in the list, marked "ended" — settled 2026-08-27.** It lives until **your** span: the history reads, the input is closed, and neither side can write. The mark is mandatory, on the same grounds that gave §5 its headstone: a silent "I cannot write here" is indistinguishable from a fault. The cost is accepted — a row for a conversation that no longer exists sits in the list for a while; but learning it ended only by opening it is worse than seeing it at once.
- **Fading shows in the row itself**: through the last quarter of your own span the row is shown fading. There is no separate "Fading" section and will not be — a conversation would move between sections on a timer, disappearing from view exactly when there is least time left (§3 of the spec).
- **After "not now" the entry disappears, but for a few seconds a line stays at the bottom: "declined · undo"** (decided 2026-08-28, screen 6). The refusal is recorded **at once**, not when those seconds run out: otherwise closing the app would leave the offer hanging for whoever refused. The undo is a request of its own, possible while the line is visible and while the match is still alive; after that the refusal is final.
- A new offer or a new conversation adds an entry without replacing the earlier ones.
- **A table does not land here**, because it is not a conversation: it lives by the rules of the feed, and speech at it is public and moderated (screen 19). So that one can get back to it, **while you are sitting at a table the feed header carries a line "you are at a table — return"** (settled 2026-08-27). The cost is named plainly: narrow the viewing circle or leave the radius and the line stays while the table itself is no longer in the feed — the line still takes you back, but finding the table again is impossible.

## Open questions

- ~~What an entry shows~~ — settled 2026-08-26 (above). There is no unread counter: it would mean the node knows who opened a conversation and when.
- ~~Sorting~~ — **by the time of the last line** (settled 2026-08-26): the list answers the question "where are people talking right now".
- ~~The counter on the offers tab~~ — it counts offers **waiting for your answer** and clears as they are answered, not by visiting the tab (settled 2026-08-26). Otherwise one visits, does not answer, and the offer quietly expires with the phrases.
- ~~A counter on the conversations tab~~ — **there is none** (2026-08-27).
- How exactly the fading row and the "ended" row are shown — by colour, by a label, or both — is not drawn.
