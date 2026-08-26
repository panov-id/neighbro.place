# Screen 6 — Match

## Purpose

What happens on a mutual like and how a conversation opens. **Edit of 2026-08-26:** this used to say the chat opens at once; by the spec a match is an offer to talk that both must accept (`xor.ad/docs/chat_EN.md` §8.5).

## Logic

- **A match is not a chat.** A mutual like opens a card: on it are **both phrases** that caused it, and a "talk" button. The conversation appears when both have pressed.
- **While only one has pressed**, that one sees only that **there is no answer yet** — not whether the other has already accepted (settled 2026-08-26): that would be a fact about someone else's action and a nudge, and the product gives neither anywhere else — no "last seen", no "read".
- **An offer lives exactly as long as both phrases live.** Either expires and the match goes with it: the meeting of moods was what tied the two together.
- **A match counts only while both have live phrases**, which is why only someone with a phrase of their own in the feed can like (`00-mechanics_EN.md` §11).
- **Likes after a match.** If a matched person likes another of the other's phrases, no new match appears: the like shows up in the open conversation as a line saying which phrase was liked.

## Next step

→ [Screen 8 — Conversation](./08-chat-screen_EN.md)

## Open questions

- ~~The form of the card~~ — settled 2026-08-26: **your phrase on top, theirs beneath**, one under the other like the start of a conversation, with the button below. Side by side at 375px, two phrases of 128 characters become two narrow strips.
- The format of the like line inside a conversation (text, a card of the phrase, an icon) is undefined.
