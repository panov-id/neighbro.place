# Screen 6 — Match

## Purpose

What happens on a mutual like and how a conversation opens. **Edit of 2026-08-26:** this used to say the chat opens at once; by the spec a match is an offer to talk that both must accept (`xor.ad/docs/chat_EN.md` §8.5).

## Logic

- **A match is not a chat.** A mutual like opens a card: on it are **both phrases** that caused it, and a "talk" button. The conversation appears when both have pressed.
- **While only one has pressed**, that one sees there is no answer yet and the other sees an offer. When the other person was last online is not shown: that is about them, not about the conversation.
- **An offer lives exactly as long as both phrases live.** Either expires and the match goes with it: the meeting of moods was what tied the two together.
- **A match counts only while both have live phrases**, which is why only someone with a phrase of their own in the feed can like (`00-mechanics_EN.md` §6).
- **Likes after a match.** If a matched person likes another of the other's phrases, no new match appears: the like shows up in the open conversation as a line saying which phrase was liked.

## Next step

→ [Screen 8 — Conversation](./08-chat-screen_EN.md)

## Open questions

- The visual form of the match card is undefined: the two phrases side by side, one under the other, or yours and theirs styled differently.
- The format of the like line inside a conversation (text, a card of the phrase, an icon) is undefined.
- Whether the card shows that the other has already accepted, or only that there is no answer yet, is undefined.
