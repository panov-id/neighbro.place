# Screen 10 — Settings

## Purpose

The app's settings screen, opened via an icon in the feed header.

## Screen elements

- A theme switch: light, dark, or as in the system.
- A contrast slider.
- The default silence timer for new conversations.
- Device: moving the identity to another one (screen 13).

## Logic

- Theme and contrast apply immediately, no confirmation needed.
- **The theme lives in two places and is one state:** the house mark in the header flips it with a tap, here it is an explicit choice of three (`xor.ad/docs/chat_EN.md` §11). Two controls, one value; they must not drift apart.
- **The social link field is gone — edit of 2026-08-26.** There are no links in the product, neither in the feed nor in a conversation: they are stripped, and the one place a link lives is a neighbourhood offer (`00-mechanics_EN.md` §5). The field was a leftover of screen 12, dropped along with it.
- There is no sexual-content setting here, because there is nothing to switch on: such content is rejected before publication for everyone alike.

## Open questions

- The contrast slider's range and step are not defined yet.
- The silence timer defaults to an hour; whether it can be set here for all future conversations or only inside a conversation is undecided.
