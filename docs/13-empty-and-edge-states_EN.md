# Screen 13 — Empty and Edge States

## Purpose

Interface states for missing data or reached limits, rather than the normal usage flow.

## States

- **Quota exhausted.** The user tries to post, but the 5-post limit (see the Moderation section) is used up. Posting is unavailable until the quota recovers.
- **No one nearby.** No active messages exist within the selected radius (see screen 3) — the feed is empty.
- **No geolocation access.** The user hasn't granted permission for automatic position detection (see screen 3) — a way to set location manually is needed.

## Open questions

- Exact copy and visuals for each state are not defined yet.
- Whether the quota recovers automatically over time, or only as old messages expire, is not defined yet.
- Follow-up behavior when geolocation access is denied (re-prompt, manual entry only) is not defined yet.
