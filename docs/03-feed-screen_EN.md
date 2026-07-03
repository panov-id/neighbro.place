# Screen 3 — Feed

## Purpose

The app's main screen. Short messages from people nearby, newest at the bottom like a chat, not a stacked timeline. The AI detects each message's language; by default about 95% of what's visible is in the user's language and 5% is in other languages spoken in the region (both shares configurable via environment variable).

## Screen elements

- The message feed.
- A filter icon — opens a panel with the age and radius filters.

## Filter panel (opened via the icon)

- **Age filter** — a range slider. For 18+, it's a smooth slider across any range; people under 18 are never shown, regardless of the setting. For under 18, the slider is available too, but with a narrow maximum that never reveals adults.
- **Radius filter** — a slider on a map: a map with a visual radius circle over it, the slider grows or shrinks the circle.

## Logic

- Both filters are part of the feed's interface, not a separate onboarding step.
- Geolocation is detected automatically on first opening the feed; the user can also set it manually via the same circle on the map.

## Open questions

- Default radius values (min/max/starting) are not defined yet.
- The exact filter icon is not defined yet.
- The posting screen/mechanic ("add" button) is not described yet — will be a separate step.
