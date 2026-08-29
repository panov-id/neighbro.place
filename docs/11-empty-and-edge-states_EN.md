# Screen 11 — Empty and Edge States

> This was screen 13 until 2026-08-27. Number 13 was held by two screens at once — this one and moving the identity — while eleven stood empty: screen 11 was dropped along with moving the paper code to registration, screen 12 along with the social link field. Referring to "screen 13" had become ambiguous, and numbering exists precisely for references.

## Purpose

Interface states for missing data or reached limits, rather than the normal usage flow.

**Every edge state of the product is gathered here — decided 2026-08-29.** There used to be four, while those added over the week lived each on its own screen. The price of gathering them is named: some states are described here and where they happen — so here the line is short and carries a pointer, and the mechanic lives on its own screen. Empty screens are the ones most often left undrawn, and a place where they are all visible at once is worth that price.

## States

- **Quota exhausted.** All five slots hold live phrases (`00-mechanics_EN.md` §3). Posting is unavailable until one expires or is taken down by hand on screen 9.
- **The first phrase is waiting on its name.** Until the queue accepts the name, the phrase has not reached the feed and a second cannot be sent. A state of its own, separate from an exhausted quota: no slot is taken, but the button is inactive (edit of 2026-08-26).
- **No one nearby.** No live phrases within the selected radius (screen 3). The screen does not leave the person in a void: a line says it is quiet nearby and offers to widen the circle — **with the step of how many phrases would then appear**: "a few", "about a dozen", "dozens" (settled 2026-08-26, the steps are in `00-mechanics_EN.md` §4). There is no exact number here for the same reason there is none on the handle itself: a counter tied to a radius is a measuring instrument, and an exact figure lets one work out the ring holding a single particular phrase. The circle does not grow by itself: otherwise a person sees people ten kilometres away and takes them for neighbours.
- **A first visit with no phrase of your own (added 2026-08-29).** The feed is full but liking is impossible: a match counts only while both sides have a live phrase. This is a state of its own because until now it lived as a single dimmed icon on a card — a person saw an inactive button and did not understand that the product was waiting for their first word. A line explains it and leads to the composer (screen 5).
- **The queue has stalled (added 2026-08-29).** Moderation is answering more slowly than usual, or not at all. The phrase stays dimmed for its author and a second one cannot be sent — the same as waiting for a name, but the reason differs and so must the wording: not "checking" but "the check is taking longer". How many seconds separate the two is undecided (`xor.ad/docs/refusal-wordings_EN.md`).
- **A support answer is waiting (added 2026-08-29).** A mark on the support button rather than in the inbox: the platform's voice does not mix with conversations between people (screen 14).
- **The node is unreachable (added 2026-08-29).** Separate from "no network": there the person has no connection, here we are not answering. The difference is not cosmetic — in the second case it is our fault, and the tone differs: "we could not do it", not "there is no connection". What was typed is kept either way.
- **A moderation refusal** — the phrase did not pass, the class of reason is named, the text stays at hand (screen 4, wordings in `xor.ad/docs/refusal-wordings_EN.md`).
- **The fifth refusal in a row** — fifteen minutes without posting; the feed, likes and conversations keep working, and the refusal says so.
- **A conversation ended for the other person** — a gravestone on the open screen, a marked row in the list (screens 7 and 8).
- **The other person stepped away** — a line saying "away" instead of the input field, with no span (screen 8).
- **A table outside your bands** — there is no state and there will not be: someone outside the bands is not shown the table at all, because a greyed-out card would itself report who is sitting where (screen 19).
- **Geolocation does not exist as a state — edit of 2026-08-28.** Permission is never requested, so "no access" is not an edge case but the norm: the point is worked out from the time zone, the address and the language, labelled as approximate, the circle is wider, and everything is refined by hand on the diagram (`00-mechanics_EN.md` §4).

## Open questions

- Exact copy and visuals for each state are not defined yet.
- ~~Whether the quota recovers over time~~ — **there are two counts and they differ** (decided 2026-08-29). A slot frees **only** when a phrase disappears: it expired or was taken down. The "four per hour" ceiling is a sliding window and releases by itself. So a person can see a free slot and still be refused, and the other way round; a refusal must name which of the two is holding them (`xor.ad/docs/refusal-wordings_EN.md`).
- ~~Behaviour when geolocation access is denied~~ — settled 2026-08-26 (above).
