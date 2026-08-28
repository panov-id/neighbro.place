# Screen 6 — Match

## Purpose

What happens on a mutual like and how a conversation opens. **Edit of 2026-08-26:** this used to say the chat opens at once; by the spec a match is an offer to talk that both must accept (`xor.ad/docs/chat_EN.md` §8.5).

## Logic

- **A match is not a chat.** A mutual like opens a card: on it are **both phrases** that caused it, and a "talk" button. The conversation appears when both have pressed.
- **What else is on the card (written down 2026-08-27).** The other phrase's mode (`alone` / `company` / `party`), the peer's **name and age**, and the timer `match expires · Nh Nm`. The name and age are not decoration here: the feed carries neither and never will, and this is the **first place** where the other person becomes somebody in particular (`xor.ad/docs/chat_EN.md` §8.11). Disclosure is stepwise and irreversible — which is why "talk" stays a deliberate press rather than automation.
- **This same screen carries the only warning about what a person is stepping into:**

  > This chat is not checked. Nobody reads what you write here — not us, not a filter.
  > It is encrypted on your devices: our server carries it and cannot read it.
  > If someone behaves badly, block them and report them, attaching a copy from your own device.

  This is **not** a second consent or a checkbox: "talk" stays the single press. The text sits here because this is the last moment at which nothing has been opened (§8.5).
- **There is no conversation span on this screen** — it is chosen inside the conversation itself, one per person (screen 8, settled 2026-08-27). It used to stand here beside the notice; it was removed because asking for a decision before a person has seen who they are talking to is asking them to decide without grounds.
- **While only one has pressed**, that one sees only that **there is no answer yet** — neither whether the other has accepted, nor whether they opened the card at all (confirmed 2026-08-27; the mechanics still listed this as an open question, and it is now closed in both places). The reason is the one behind having no "last seen" and no "read": it is a fact about someone else's action, and it presses. "Saw it and said nothing" reads as a refusal, though the person may simply have closed the app.
  The cost is accepted and named: the wait is blind, right up to the match expiring.
- **A "not now" button — added 2026-08-28.** Declining was possible only by staying silent until the match expired, which made doing nothing the only way to say no. The card now carries two buttons: "talk" and "not now".
  **The refusal is not visible to the other person — a consequence rather than a separate decision.** The product never reports someone else's action (above in this same section), and an offer vanishing early would be exactly such a report: "saw it and refused" reads harder than "did not answer". So "not now" removes the card **for whoever refused**, and the other person waits until expiry as they would have anyway. The price is accepted: they wait for nothing, knowing no more than before.
  **The refusal is final for this match.** There is no changing your mind: the card is gone and the like that created it is spent. A new match needs a new phrase.
- **Both phrases are shown with their own remainders — added 2026-08-28.** Each phrase has its own span and the match dies with the first of them; a single shared timer never said **which one** was ending. Two numbers on the card are more honest than one.
- **An offer lives exactly as long as both phrases live.** Either expires and the match goes with it: the meeting of moods was what tied the two together.
- **A match counts only while both have live phrases**, which is why only someone with a phrase of their own in the feed can like (`00-mechanics_EN.md` §11).
- **Likes after a match.** If a matched person likes another of the other's phrases, no new match appears: the like shows up in the open conversation as a line saying which phrase was liked.
- **A match from an offer is one-sided** (`xor.ad/docs/chat-flows_EN.md`, flow 10). A like on a phrase with a discount creates a match at once, without waiting for one back: otherwise, to collect the stools somebody is giving away, you would have to wait for them to like something of yours. From there it is the same machinery — the card, the notice, the double consent — and **the offer's author may decline**.
- **While a name stands rejected by moderation, no match opens** (§8.2). A name is visible to a stranger only from a match, so the match is the last point at which a rejected one can still be kept out of sight. The phrase itself lives on: it passed on its own merits.

## Next step

→ [Screen 7 — Conversations](./07-chat-list_EN.md): the match waits for an answer on the "Offers" tab.
→ [Screen 8 — Conversation](./08-chat-screen_EN.md): once both have pressed.

## Open questions

- ~~The form of the card~~ — settled 2026-08-26: **your phrase on top, theirs beneath**, one under the other like the start of a conversation, with the button below. Side by side at 375px, two phrases of 128 characters become two narrow strips.
- The format of the like line inside a conversation (text, a card of the phrase, an icon) is undefined.
- ~~What the first to accept sees~~ — **only "no answer yet"** (2026-08-27). The item was listed as open in `00-mechanics_EN.md` §11 and as settled here at the same time; it is now settled the same way in both.
