# Screen 11 — Consent to Show NSFW Content

## Purpose

The screen where a user turns on showing messages with sexual subtext (see the "Moderation" section in the README). Opened proactively from Settings (screen 10).

## Screen elements

- The consent agreement text for this option.
- A button to accept the agreement.
- An email input field.
- A confirm/save button.

## Logic

- Without an accepted agreement and a saved email, messages with sexual subtext stay completely invisible (see screen 3, Moderation section).
- The email is stored as given, without email verification.
- After accepting the agreement and saving the email, such messages appear in the feed alongside everything else.

## Open questions

- The exact agreement text is not defined yet.
- Whether the option can be turned back off after enabling it is not defined yet.
