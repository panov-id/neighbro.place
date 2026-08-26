# Screen 2 — About you

## Purpose

The one step of signing up: name, age and PIN. It ends here — the feed comes next. **Edit of 2026-08-26:** the birth year used to be asked on the splash, the name was optional, and there was no PIN at all.

## Screen elements

- A name field — **required**.
- Age — the birth year, year only, no day or month.
- A six-digit PIN, entered twice.
- **The paper recovery code**: sixteen characters in groups, shown once, with a confirmation — type two of the groups back.
- A line saying the identity lives on this device, and what brings it back.
- A "next" button — icon only, no text label (same as screen 1).

## Logic

- **The name is required.** It is published text: the other person sees it on the match card and in the chat, so it goes through the same moderation queue as a phrase — but **at the first publication**, not here: until then it is visible to nobody (`00-mechanics_EN.md` §5).
- **Age is asked before the feed**, because the feed itself depends on it: it is cut by age bands, and without the number there is nothing to assemble it from.
- **The PIN is required and asked here.** It locks an open tab and takes part in encrypting everything on disk. It cannot be deferred: the terminal client writes its key file immediately (`00-mechanics_EN.md` §1).
- **The paper code is issued here — settled 2026-08-26** (overriding the move to the first chat of 2026-08-18). The reason is not that there is something to lose before the chat, but that the cost of being wrong is asymmetric: a screen that fails to convince mends itself — the person returns a day later; a device lost without a code never comes back.
- **The code is shown once and confirmed by typing two groups.** Without the confirmation the "next" button stays inactive: "next" gets pressed unread, and recovery cannot ask afterwards.
- After the button, straight to the feed. There is no separate geolocation screen: position and radius live inside the feed.
- Signing up completes on this step: the keys are born on the device, the node mints an identifier and keeps only the public half of the key.

## What has to be said to the person

On the screen itself, not in small print:

> **Write this code down on paper.** It is the only way to bring your identity back. We have no email and no password — lose the device or clear the site's data, and there is nothing to restore you with, and we cannot look the code up: we do not have it. It will not be shown a second time.

A separate line about the conversations, because the code does not bring those back:

> The identity comes back with the code. The conversations do not: they exist neither with us nor anywhere else.

## Next step

→ [Screen 3 — Feed](./03-feed-screen_EN.md)

## Open questions

- The name field's placeholder is not defined yet.
- A name length limit is not defined yet.
- Whether the warning is shown only here or stays reachable in settings.
- The format of the code — which characters, grouped how — comes from the spec but is not fixed on the screen.
- What happens if the person closes the tab between seeing the code and confirming it.
