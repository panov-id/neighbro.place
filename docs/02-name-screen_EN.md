# Screen 2 — Name

## Purpose

The second registration step, right after picking a birth year on the loading screen — entering a display name.

## Screen elements

- A free-form display name input — optional, can be left blank.
- A "next" button — icon only, no text label (same as screen 1).

## Logic

- The name is optional: the field can be left empty and the user can still proceed.
- Tapping the button moves straight to the feed.
- There is no separate geolocation screen: detecting position and setting the radius happen inside the feed itself, not as a separate onboarding step.

## Next step

→ [Screen 3 — Feed](./03-feed-screen_EN.md)

## Open questions

- The name field's placeholder text is not defined yet.
- A name length limit is not defined yet.
