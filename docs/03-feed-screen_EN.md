# Screen 3 — Feed

## Purpose

The app's main screen. Short messages from people nearby, newest at the bottom like a chat, not a stacked timeline.

**Three different things live in the feed, and each is labelled:** neighbours' phrases, **offers** (screen 17) and **tables** (screen 19). They run as one stream ordered by time, not on separate shelves. An offer is labelled with the word "offer" and the size of the discount, a table with the name of the game and the number of people sitting at it; offers carry a quota — no more than one commercial card per ten ordinary ones (`xor.ad/docs/chat_EN.md` §8.3). This screen used to describe phrases only, although both of its neighbours in the feed were described on their own screens.

**Your own phrase awaiting review is visible here to you alone** — dimmed, labelled as under review (screen 4). It is in nobody else's feed.

## Screen elements

- The feed: phrases, offers and tables in one stream.
- **A language filter in the header** — up to three languages, cleared with one tap (`00-mechanics_EN.md` §8).
- **A line "you are at a table — return"** in the header while you are sitting at one (settled 2026-08-27). A table does not appear in the conversations list — it lives by the rules of the feed — and without this line somebody who looked away for a minute would lose a game with live people without any notice (screen 7, screen 19).
- A line under the feed: "**N more messages in other languages — show**".
- A filter icon — opens a panel with the age, radius and mode filters.

## Filter panel (opened via the icon)

- **Age filter** — a range slider **inside your own age band**. The band is computed by the node from the number given on screen 2: up to 20 it is ±2 years, from 21 it starts two years below and runs upward with no ceiling, and the rule is symmetric — a pair sees each other only if each falls inside the other's band (`xor.ad/docs/chat_EN.md` §8.2). Narrowing is free; widening past the band is not.
  **The bounds are not labelled with numbers — settled 2026-08-26.** The handle simply stops: a stated bound would point out where the wall is and what number to claim in order to get past it. The stop is drawn to read as the end of the scale, not as a frozen interface.
  **For an adult the right end is "no limit", not a number.** The band has no ceiling, and an invented one such as 65+ would cut off older neighbours for no reason.
  **When the band has shifted** — the person got older and the saved filter was clamped into the new one — a single line says so on their next visit. Changing someone's feed in silence is not allowed.
- **Radius filter** — a slider on a map: a circle over the map that the slider stretches. **3 km by default, from 500 m to 25 km** (settled 2026-08-26). Three kilometres is a whole district: the feed is full from the first day, and a person does not hit emptiness before understanding why they came.
  **Under the circle it says how many are talking in there right now** (settled 2026-08-26). Not an exact number but a step: `nobody here yet` · `a few` · `about a dozen` · `dozens` · `hundreds`. Otherwise the handle is dragged blind — a person does not know whether to pull further, and ends up in emptiness or in somebody else's district.
  **The number arrives when the handle is released**, not under the finger. The reason is not saving requests: a counter tied to a radius is a measuring instrument. Stepping the handle and reading exact numbers, one can build a density map of the surroundings and work out the ring in which a single phrase appeared — going around the very blur its author chose (§4 of the mechanics). Steps, and one request per gesture, make that measurement pointless.
- **Mode filter** — three toggles: **alone / company / party** (settled 2026-08-26). Every phrase carries a mode (`mode` in `xor.ad/docs/chat_EN.md` §8.3) and until now it was only displayed. Without the filter, someone looking for company reads a feed of solitary phrases, and a party drowns among short lines.

## Logic

- The filters are part of the feed's interface, not a separate onboarding step.
- **Language is a filter, not a set of shares (amended 2026-08-26).** What stood here was "about 95% in the user's language, 5% in other languages of the region, both shares configurable via environment variable". That was a [retired] different mechanic from `00-mechanics_EN.md` §8, and it loses for one reason: shares decide for the person silently. A filter is up to three languages, taken from `navigator.languages` by default, edited by hand, cleared with a tap, with the line "N more in other languages" always under the feed. A person always knows the district is livelier than their feed, and never mistakes the filter's silence for the district's.
- **The node detects the language** with a local library, on its own machine: no text leaves in order to be identified. "AI" in the old wording was imprecise — there is no external service here and there will not be.
- **An offer is not hidden by the language filter**: the Greek bakery across the road is just as useful to a Russian-speaking neighbour (§8 of the mechanics).
- **Geolocation is not requested on entry — amended 2026-08-26** (`00-mechanics_EN.md` §4). What stood here — "detected automatically on first opening the feed" — read as a permission prompt. In fact the first point is worked out from indirect signals — time zone, address, language — labelled as approximate, with a wider default circle. The exact position is requested by the person themselves, with the "where am I" button, exactly once: it is never read in the background.

## Open questions

- The exact filter icon is not defined yet.
- How exactly a table and an offer are labelled in the stream — by a word, a frame or an icon — is not drawn; all that is settled is that both are labelled and both run in the common stream (2026-08-26).
- ~~Default radius values~~ — **3 km, from 500 m to 25 km** (settled 2026-08-26, stated above in this same file).
- ~~The posting screen~~ — described separately, screen 4.
