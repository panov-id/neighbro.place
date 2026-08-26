# Screen 7 — Conversations

## Purpose

The section holding everything to do with talking: offers waiting for an answer, and open conversations. **Edit of 2026-08-26:** this used to hold chats only, and matches appeared nowhere — even though the inbox collects them first (`xor.ad/docs/chat_EN.md` §8.12).

## Screen elements

- **Two tabs: "Offers" and "Conversations".** The first carries a counter of those waiting for an answer.
- A list: one entry per offer or per conversation. A conversation's entry carries **the name, a fragment of the last line, and what is left of your own timer** (settled 2026-08-26): the timer matters more than an unread count, because a conversation dies of silence and that is the only thing requiring action.
- Tap to go inside.

## Logic

- The tabs live **inside the section**, not in the bottom navigation: that has exactly four items (`Feed` / `Chats` / `Say` / `Me`), and a fifth does not fit a narrow screen (`xor.ad/docs/chat_EN.md` §9).
- An **offer** is a match waiting on acceptance — yours, theirs, or both. It disappears when either of the two phrases expires.
- A **conversation** enters the list once both have accepted, and lives until silence eats it — each side by their own count (`00-mechanics_EN.md` §2).
- A new offer or a new conversation adds an entry without replacing the earlier ones.

## Open questions

- ~~What an entry shows~~ — settled 2026-08-26 (above). There is no unread counter: it would mean the node knows who opened a conversation and when.
- ~~Sorting~~ — **by the time of the last line** (settled 2026-08-26): the list answers the question "where are people talking right now".
- ~~The counter on the offers tab~~ — it counts offers **waiting for your answer** and clears as they are answered, not by visiting the tab (settled 2026-08-26). Otherwise one visits, does not answer, and the offer quietly expires with the phrases.
