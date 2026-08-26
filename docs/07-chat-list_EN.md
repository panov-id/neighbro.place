# Screen 7 — Conversations

## Purpose

The section holding everything to do with talking: offers waiting for an answer, and open conversations. **Edit of 2026-08-26:** this used to hold chats only, and matches appeared nowhere — even though the inbox collects them first (`xor.ad/docs/chat_EN.md` §8.12).

## Screen elements

- **Two tabs: "Offers" and "Conversations".** The first carries a counter of those waiting for an answer.
- A list: one entry per offer or per conversation.
- Tap to go inside.

## Logic

- The tabs live **inside the section**, not in the bottom navigation: that has exactly four items (`Feed` / `Chats` / `Say` / `Me`), and a fifth does not fit a narrow screen (`xor.ad/docs/chat_EN.md` §9).
- An **offer** is a match waiting on acceptance — yours, theirs, or both. It disappears when either of the two phrases expires.
- A **conversation** enters the list once both have accepted, and lives until silence eats it — each side by their own count (`00-mechanics_EN.md` §2).
- A new offer or a new conversation adds an entry without replacing the earlier ones.

## Open questions

- What an entry shows — a name, a fragment of the last line, an unread counter — is undefined. The other person's name is visible from the match onward, not before.
- Sorting (by time of the last line, by time of the match) is undefined.
- What the counter on the offers tab looks like, and whether it clears itself.
