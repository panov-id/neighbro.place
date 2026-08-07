# Screen 10 — Settings

## Purpose

The app's settings screen, opened via an icon in the feed header.

## Screen elements

- A theme switch: light/dark.
- A contrast slider.
- Social link management: a single plain input field for a freeform link the user can share in chat — no platform picker, no presets (Telegram/Instagram etc. aren't broken out as separate options).

## Logic

- Theme and contrast apply immediately, no confirmation needed.
- The attached social link is used on the "share link" screen in chat (see separate screen).
- There is no sexual-content setting here, because there is nothing to switch on: such content is rejected before publication for everyone alike.

## Open questions

- The contrast slider's range and step are not defined yet.
- The social link field's format/validation is not defined yet — per the README, nothing is validated and the platform list isn't restricted.
