# Screen 10 — Settings

## Purpose

The screen behind the **"Me"** item in the bottom navigation. It is also screen 9: what is alive on top (your own phrases, offers and tables with their timers), settings and everything a person can change about themselves below (settled 2026-08-27).

They were not split for a simple reason: the bottom navigation has exactly four items, and a fifth does not fit 375px (`xor.ad/docs/chat_EN.md` §9). The cost is accepted and named: the screen is heterogeneous — urgent above, rare and partly irreversible below — so the dangerous part is separated and labelled.

## Screen elements

**About you:**

- **Name.** Changes only on a clean slate — while there is no live phrase and no open conversation; an accepted name is frozen, a rejected one is always editable (§8.2). A new one goes through the same moderation queue as a phrase.
- **Age.** Upward only, and the 20 → 21 step is **irreversible**: the warning comes before saving, not after. Once a year the app asks again, "still 38?" — silence changes nothing.
- **Feed languages** — up to three, taken from the browser by default, edited here (`00-mechanics_EN.md` §8). The feed header only clears the filter with a tap; the list itself lives here.

**The app:**

- A theme switch: light, dark, or as in the system.
- Contrast — **three steps**: normal, raised, maximum (settled 2026-08-26).
- **The default silence span applies to new conversations only** (decided 2026-08-28): it does not touch those already open. The price is named — a person changes the default and does not see why the current conversation still runs on the old one — but the opposite would mean one tap in the settings killing a conversation with an hour left in it.
- **Step away** — 20 minutes, an hour, or until morning (screen 20). From here, because there is nowhere else.
- **A default zone and mode for new phrases** (added 2026-08-28): the composer opens with them, and changing them per phrase is no longer required. The price is named: privacy stops being a decision made for **each** phrase, while different phrases often want different things — so the default is visible in the composer and editable right there.
- **Hidden phrases** — a list with a way back (added 2026-08-28, screen 5). Short-lived by construction: a hidden phrase disappears with its own span, like any other.

**Identity and security — a screen of its own (decided 2026-08-28):**

- An **"Identity and security"** item leads to screen 12: moving the device,
  changing the PIN, reissuing the paper code, what is stored on the device,
  starting over. All of them are irreversible, and they used to sit one scroll
  away from the theme switch — a separate screen works here as distance rather
  than decoration.

## Logic

- Theme and contrast apply immediately, no confirmation needed.
- **The theme lives in two places and is one state:** the house mark in the header flips it with a tap, here it is an explicit choice of three (`xor.ad/docs/chat_EN.md` §11). Two controls, one value; they must not drift apart.
- **The social link field is gone — edit of 2026-08-26.** There are no links in the product, neither in the feed nor in a conversation: they are stripped, and the one place a link lives is a neighbourhood offer (`00-mechanics_EN.md` §5). The field was a leftover of screen 12, dropped along with it.
- There is no sexual-content setting here, because there is nothing to switch on: such content is rejected before publication for everyone alike.
- **Links to the three legal documents** — terms, privacy, community rules (screen 15). Here, because this is the only place a person comes back to them after registration.
- **The irreversible is kept apart from the reversible.** Theme and contrast apply at once and undo with a tap; an age raised, a code re-issued and "start over" undo with nothing. So they sit in a separate block rather than in one list with the theme.

## Open questions

- ~~The contrast slider's range and step~~ — there is no slider: three steps, each checked by arithmetic against 4.5:1, as in the panel. A continuous control inevitably has positions below the threshold, and accessibility stops being a guarantee.
- The silence timer defaults to an hour; whether it can be set here for all future conversations or only inside a conversation is undecided.
- How exactly the "Identity" block is set apart — by a heading, by colour, or on a screen of its own — is not drawn; all that is settled is that it is set apart (2026-08-27).
