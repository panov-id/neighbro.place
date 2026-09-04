# Screen 11 — Empty and Edge States

> This was screen 13 until 2026-08-27. Number 13 was held by two screens at once — this one and moving the identity — while eleven stood empty: screen 11 was dropped along with moving the paper code to registration, screen 12 along with the social link field. Referring to "screen 13" had become ambiguous, and numbering exists precisely for references.

## Purpose

Interface states for missing data or reached limits, rather than the normal usage flow.

**Every edge state of the product is gathered here — decided 2026-08-29.** There used to be four, while those added over the week lived each on its own screen. The price of gathering them is named: some states are described here and where they happen — so here the line is short and carries a pointer, and the mechanic lives on its own screen. Empty screens are the ones most often left undrawn, and a place where they are all visible at once is worth that price.

## States

- **Quota exhausted.** All four slots hold live phrases (`00-mechanics_EN.md` §3). Posting is unavailable until one expires or is taken down by hand on screen 9.
- **The first phrase is waiting on its name.** Until the queue accepts the name, the phrase has not reached the feed and a second cannot be sent. A state of its own, separate from an exhausted quota: no slot is taken, but the button is inactive (edit of 2026-08-26).
- **No one nearby.** No live phrases within the selected radius (screen 3). The screen does not leave the person in a void: a line says it is quiet nearby and offers to widen the circle — **with the step of how many phrases would then appear**: "a few", "about a dozen", "dozens" (settled 2026-08-26, the steps are in `00-mechanics_EN.md` §4). There is no exact number here for the same reason there is none on the handle itself: a counter tied to a radius is a measuring instrument, and an exact figure lets one work out the ring holding a single particular phrase. The circle does not grow by itself: otherwise a person sees people ten kilometres away and takes them for neighbours.
- **A first visit with no phrase of your own (added 2026-08-29).** The feed is full but liking is impossible: a match counts only while both sides have a live phrase. This is a state of its own because until now it lived as a single dimmed icon on a card — a person saw an inactive button and did not understand that the product was waiting for their first word. A line explains it and leads to the composer (screen 5).
- **The queue has stalled (added 2026-08-29).** Moderation is answering more slowly than usual, or not at all. The phrase stays dimmed for its author and a second one cannot be sent — the same as waiting for a name, but the reason differs and so must the wording: not "checking" but "the check is taking longer". How many seconds separate the two is undecided (`xor.ad/docs/refusal-wordings_EN.md`).
- **A support answer is waiting (added 2026-08-29).** A mark on the support button rather than in the inbox: the platform's voice does not mix with conversations between people (screen 14).
- **No network (added 2026-09-02).** A line of its own rather than a mention
  inside the neighbouring state: the person has no connection, and it is fixed
  on their side — flight mode, a tunnel, data run out. The tone differs from the
  one below accordingly: not "we could not do it". What was typed is kept, the
  feed shows the last thing it managed to receive, and says that it is stale.
- **Waiting for the first answer (added 2026-09-02).** Neither emptiness nor an
  error: the request went out, the answer has not arrived. A skeleton of cards
  instead of an empty screen — otherwise a first visit to a quiet
  neighbourhood is indistinguishable from an app that does not work, and those
  are exactly the two seconds in which a person decides whether the product
  keeps its place on the phone.
- **The node is unreachable (added 2026-08-29).** Separate from "no network": there the person has no connection, here we are not answering. The difference is not cosmetic — in the second case it is our fault, and the tone differs: "we could not do it", not "there is no connection". What was typed is kept either way.
- **A moderation refusal** — the phrase did not pass, the class of reason is named, the text stays at hand (screen 4, wordings in `xor.ad/docs/refusal-wordings_EN.md`).
- **A published phrase of yours was restricted** — the Article 17 statement of reasons is shown in the app at the next sign-in, because the author usually has no email (screen 9; added 2026-09-04).
- **The fifth refusal in a row** — fifteen minutes without posting; the feed, likes and conversations keep working, and the refusal says so.
- **A conversation ended for the other person** — a gravestone on the open screen, a marked row in the list (screens 7 and 8).
- **The other person stepped away** — a line saying "away" instead of the input field, with no span (screen 8).
- **The identity moved to another device** — the node closed the socket with `4002`, the conversation closes, reconnecting is pointless (screen 8; added 2026-09-04).
- **The app is out of date** — the node does not support this version, code `4004`, no reconnection is attempted (screen 8; added 2026-09-04).
- **A table outside your bands** — there is no state and there will not be: someone outside the bands is not shown the table at all, because a greyed-out card would itself report who is sitting where (screen 19).
- **Geolocation does not exist as a state — edit of 2026-08-28.** Permission is never requested, so "no access" is not an edge case but the norm: the point is worked out from the time zone, the address and the language, labelled as approximate, the circle is wider, and everything is refined by hand on the diagram (`00-mechanics_EN.md` §4).

- **A document changed while the person was away — state added 2026-08-29.**
  The feed reads as usual; at the first attempt to publish or open a chat the
  node answers `legal_reacceptance_required` (`xor.ad/docs/protocol_EN.md` §6),
  and the person lands on a screen listing the documents that changed, with one
  checkbox. Reading is left alone **deliberately**: someone who came to read a
  reply should get the reply, not a legal text. The guidelines never come here —
  their new revision is recorded silently (screen 15).

## Wordings

**Written 2026-09-03, before the drawing — and that is a decision.** A mockup
with "Lorem ipsum" lies about the layout: a long line breaks it exactly where
nobody expected, a short one leaves a hole. Below is what a person reads; the
look stays open.

One voice for all of them: say what happened and what to do next. No apologising
twice, no explaining how the system is built, no "oops".

| State | Heading | Line under it | Action |
|---|---|---|---|
| Quota spent | That is all for now | Your four phrases are still alive. When one frees up, you can speak again. | My messages |
| Tab locked | Enter your PIN | Six digits and you are back. | — |
| Locked, fewer than four attempts left | Enter your PIN | 3 attempts left. After that the correspondence on this device is gone — neither we nor you will be able to bring it back. | — |
| First phrase waiting for a name | Looking at your name | Once the name is accepted, the phrase goes out to the neighbours. | — |
| Nobody nearby | Quiet around here | Nobody in your circle is talking right now. A wider circle, more voices. | Widen the circle |
| First visit with no phrase of your own | Say something first | A like opens a conversation only when both of you have a live phrase. | Write one |
| The queue is stuck | The check is running late | The phrase is not lost, it is waiting its turn. | — |
| A support reply is waiting | You have a reply | The support reply is in the support section. | Open |
| No network | No connection | The internet seems to be gone. What you typed is here, the feed is what made it through. | Retry |
| Waiting for the first answer | — | (a skeleton of cards, no text) | — |
| The node is unreachable | This one is on us | We are not answering — that is our side. What you typed is here. | Retry |
| Moderation refusal | This will not go out | *(the class of reason — `xor.ad/docs/refusal-wordings_EN.md`)* | Edit |
| Fifth refusal in a row | Fifteen minutes off | The feed, likes and conversations all work — only new phrases are paused. | — |
| The conversation ended for the other person | The conversation ended | There is nothing here any more. | Close |
| The other person stepped away | Stepped away | — | — |
| The identity moved to another device | Your identity is not here any more | You moved it to another device. It no longer works on this one, and the correspondence stays here. | — |
| The app is out of date | Time to update | This version no longer talks to the node. Reload the page and everything is where you left it. | Reload |
| A published phrase was restricted | Your phrase was hidden | What happened, why, who decided and what to do next — all of it here. | Read |
| A document changed | Something changed | Read what is different and accept it — writing does not work until you do. | Read |

Three lines are deliberately empty. "Stepped away" has no second line because we
do not know when they are back and will not invent it. "Waiting for the first
answer" has no text at all: the skeleton already says a load is running, and a
caption under it turns a second of waiting into an event. The moderation refusal
has a shared heading, while the reason arrives from the node — one per class.

## Open questions

- ~~Exact copy for each state~~ — **written 2026-09-03, the "Wordings" section above**. What stays open is the **visual**: how these lines sit on the screen, with or without an icon, where the action goes.
- ~~Whether the quota recovers over time~~ — **there are two counts and they differ** (decided 2026-08-29). A slot frees **only** when a phrase disappears: it expired or was taken down. The "four per hour" ceiling is a sliding window and releases by itself. So a person can see a free slot and still be refused, and the other way round; a refusal must name which of the two is holding them (`xor.ad/docs/refusal-wordings_EN.md`).
- ~~Behaviour when geolocation access is denied~~ — settled 2026-08-26 (above).
