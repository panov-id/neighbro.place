# Screen 11 — Empty and Edge States

> This was screen 13 until 2026-08-27. Number 13 was held by two screens at once — this one and moving the identity — while eleven stood empty: screen 11 was dropped along with moving the paper code to registration, screen 12 along with the social link field. Referring to "screen 13" had become ambiguous, and numbering exists precisely for references.

## Purpose

Interface states for missing data or reached limits, rather than the normal usage flow.

## States

- **Quota exhausted.** All five slots hold live phrases (`00-mechanics_EN.md` §3). Posting is unavailable until one expires or is taken down by hand on screen 9.
- **The first phrase is waiting on its name.** Until the queue accepts the name, the phrase has not reached the feed and a second cannot be sent. A state of its own, separate from an exhausted quota: no slot is taken, but the button is inactive (edit of 2026-08-26).
- **No one nearby.** No live phrases within the selected radius (screen 3). The screen does not leave the person in a void: a line says it is quiet nearby and offers to widen the circle — **with the step of how many phrases would then appear**: "a few", "about a dozen", "dozens" (settled 2026-08-26, the steps are in `00-mechanics_EN.md` §4). There is no exact number here for the same reason there is none on the handle itself: a counter tied to a radius is a measuring instrument, and an exact figure lets one work out the ring holding a single particular phrase. The circle does not grow by itself: otherwise a person sees people ten kilometres away and takes them for neighbours.
- **No geolocation access.** A refusal breaks nothing: the approximate point stays — worked out from the time zone, the address and the language — labelled as approximate, with a wider default circle (`00-mechanics_EN.md` §4). Plus a point placed by hand on the map. Permission is not asked again: browsers mute repeat requests themselves, and the approximate point is enough (settled 2026-08-26).

## Open questions

- Exact copy and visuals for each state are not defined yet.
- Whether the quota recovers automatically over time, or only as old messages expire, is not defined yet.
- ~~Behaviour when geolocation access is denied~~ — settled 2026-08-26 (above).
