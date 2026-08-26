# Screen 3 — Feed

## Purpose

The app's main screen. Short messages from people nearby, newest at the bottom like a chat, not a stacked timeline. The AI detects each message's language; by default about 95% of what's visible is in the user's language and 5% is in other languages spoken in the region (both shares configurable via environment variable).

## Screen elements

- The message feed.
- A filter icon — opens a panel with the age and radius filters.

## Filter panel (opened via the icon)

- **Age filter** — a range slider **inside your own age band**. The band is computed by the node from the number given on screen 2: up to 20 it is ±2 years, from 21 it starts two years below and runs upward with no ceiling, and the rule is symmetric — a pair sees each other only if each falls inside the other's band (`xor.ad/docs/chat_EN.md` §8.2). Narrowing is free; widening past the band is not.
  **The bounds are not labelled with numbers — settled 2026-08-26.** The handle simply stops: a stated bound would point out where the wall is and what number to claim in order to get past it. The stop is drawn to read as the end of the scale, not as a frozen interface.
  **For an adult the right end is "no limit", not a number.** The band has no ceiling, and an invented one such as 65+ would cut off older neighbours for no reason.
  **When the band has shifted** — the person got older and the saved filter was clamped into the new one — a single line says so on their next visit. Changing someone's feed in silence is not allowed.
- **Radius filter** — a slider on a map: a circle over the map that the slider stretches. **3 km by default, from 500 m to 25 km** (settled 2026-08-26). Three kilometres is a whole district: the feed is full from the first day, and a person does not hit emptiness before understanding why they came.
- **Mode filter** — three toggles: **alone / company / party** (settled 2026-08-26). Every phrase carries a mode (`mode` in `xor.ad/docs/chat_EN.md` §8.3) and until now it was only displayed. Without the filter, someone looking for company reads a feed of solitary phrases, and a party drowns among short lines.

## Logic

- Both filters are part of the feed's interface, not a separate onboarding step.
- Geolocation is detected automatically on first opening the feed; the user can also set it manually via the same circle on the map.

## Open questions

- Default radius values (min/max/starting) are not defined yet.
- The exact filter icon is not defined yet.
- The posting screen/mechanic ("add" button) is not described yet — will be a separate step.
