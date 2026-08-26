# Screen 13 — Empty and Edge States

## Purpose

Interface states for missing data or reached limits, rather than the normal usage flow.

## States

- **Quota exhausted.** All five slots hold live phrases (`00-mechanics_EN.md` §3). Posting is unavailable until one expires or is taken down by hand on screen 9.
- **The first phrase is waiting on its name.** Until the queue accepts the name, the phrase has not reached the feed and a second cannot be sent. A state of its own, separate from an exhausted quota: no slot is taken, but the button is inactive (edit of 2026-08-26).
- **No one nearby.** No live phrases within the selected radius (screen 3). The screen does not leave the person in a void: a line says it is quiet nearby and offers to widen the circle — **with the number of phrases that would then appear** (settled 2026-08-26). The circle does not grow by itself: otherwise a person sees people ten kilometres away and takes them for neighbours.
- **No geolocation access.** The user hasn't granted permission for automatic position detection (see screen 3) — a way to set location manually is needed.

## Open questions

- Exact copy and visuals for each state are not defined yet.
- Whether the quota recovers automatically over time, or only as old messages expire, is not defined yet.
- Follow-up behavior when geolocation access is denied (re-prompt, manual entry only) is not defined yet.
