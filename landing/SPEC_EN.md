# Spec — neighbro.place Landing Page (Waitlist)

## Purpose

A single-page pre-launch teaser — testing demand via conversion into a waitlist (see `xor.ad/docs/marketing-plan_EN.md`). Not a full site, not the app.

## Section structure

1. **Headline + pitch + waitlist form** — already implemented (`index.html`): name, one-line pitch, email field, send button, a note about premium early-user status.
2. **How it works** — feature block(s), short and simple:
   - Write a short message — people nearby see it.
   - A like matches — a private chat opens.
   - The message disappears on its own after a few hours — nothing piles up.
3. **Waitlist form again** (at the bottom of the page) — the same form as in the header, for anyone who scrolls all the way down.

## Tone and style

Copy and visual tone follow neighbro.place's European-flavored identity (see the README's "The faces" section). The structure and the set of features in block 2 are shared with sosed.place — the difference is only in language and tone, not in which features are covered.

## Technical constraints

- Static, no build step — a single HTML file with inline styles, as it is now.
- The waitlist form keeps submitting email to the relay backend (`POST /waitlist`, see the existing `index.html`); block 2 is purely informational, no logic of its own.

## Open questions

- Exact copy for the "how it works" block hasn't been written yet.
- Illustrations/icons for the feature block are not defined yet (see also the open question about icons in `docs/01-splash-screen_EN.md`).
- Whether footer links to the legal documents (`legal/`) are needed at the teaser stage, or can wait for the full site — not decided.
