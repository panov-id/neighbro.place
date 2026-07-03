# Screen 10 — Settings

## Purpose

The app's settings screen, opened via an icon in the feed header.

## Screen elements

- A theme switch: light/dark.
- A contrast slider.
- Social link management: a single plain input field for a freeform link the user can share in chat — no platform picker, no presets (Telegram/Instagram etc. aren't broken out as separate options).
- A "show messages with sexual subtext" item — leads to a separate consent screen (see screen 11).

## Logic

- Theme and contrast apply immediately, no confirmation needed.
- The attached social link is used on the "share link" screen in chat (see separate screen).
- Access to NSFW content is only enabled through the separate consent screen — from settings this is a proactive hand-off, not a one-tap toggle.

## Open questions

- The contrast slider's range and step are not defined yet.
- The social link field's format/validation is not defined yet — per the README, nothing is validated and the platform list isn't restricted.
