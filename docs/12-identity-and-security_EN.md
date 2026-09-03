# Screen 12 — Identity and security

> Number 12 was taken again on 2026-08-28. The former screen 12 (the social link
> field) was dropped on 2026-08-26 along with links themselves; the number came
> free and is reused — renumbering twenty screens for the sake of an empty number
> costs more than saying this in a line.

## Purpose

Everything irreversible a person can do to their identity. Moved off screen 10 by
a **decision of 2026-08-28**: four actions, none of which can be undone, sat one
scroll away from the theme switch. A separate screen is not decoration but
**distance**: you have to mean to get here.

## Screen elements

- **Move to another device** — a nine-character code (screen 13).
- **Change the PIN.** The PIN locks the disk, not the identity, and a PIN someone
  has seen cannot be changed any other way except by moving to another device.
  Changing it re-encrypts the local database and takes a new share from the node
  (`xor.ad/docs/chat_EN.md` §8.2).
- **Reissue the paper code — only on presenting the current one.** Otherwise
  whoever took the identity would write themselves a new one first and lock the
  owner out forever: the insurance would vanish exactly when it is needed. The
  previous code is dead afterwards.
- **What is stored on this device** (added 2026-08-28): the size of the local
  database, the **list of saved offers** (added 2026-08-29 — the only thing that
  outlives 4:20, so it is named here explicitly) and an **"erase conversation
  history"** button. The product promises a
  great deal about storage — and this is the only place where the promise can be
  seen and handled. Erasing is irreversible and takes only the history: the
  identity, the phrases and the open conversations remain, but the earlier
  conversations inside them go silent, as after a move.
- **Start over** — a new identity in place of this one. Before the button, the
  cost is counted **on the spot**: live phrases, open conversations, waiting
  offers. On its own line: that the paper code becomes useless, because the
  identity it brings back will no longer exist.

## Logic

- **Nothing on this screen can be undone**, and that is said out loud in the
  heading rather than implied by layout.
- **The cost is shown as numbers before the press, not as words after** — the same
  rule as on the step-away screen (screen 20).
- **Changing the PIN and reissuing the code do not touch the identity**: the
  `identity_id` is the same and the chats are in place. What changes is keys, not
  the person.
- **"Start over" is a new identity**, not a cleaned-up old one: the previous one is
  closed, and nothing brings it back, not even the paper code.

## Open questions

- ~~How the screen opens from the settings~~ — **as an item in the settings list**
  (decided 2026-09-02), by the general rule for entrances: a screen is opened from the
  place that makes you want it, and identity and security is wanted in settings.
  What that item looks like is not drawn. Formerly: a list item or a line at the bottom —
  is not drawn.
- ~~Whether to show the local database's size exactly or as a band~~ — **exactly, in
  megabytes** (decided 2026-09-03). The bands in the feed are not there for looks: an
  exact count by radius is an instrument for working out where an author stands. Here
  there is nothing and nobody to work out: a person is looking at **their own** device
  and their own conversations, and the only question they are answering is "is this
  worth the room on my phone". A band of "a little / noticeable" does not answer it.
  Formerly: exactly (in megabytes) or as a band,
  like the feed's density, is undecided. An exact number here is not an
  instrument, but a third digit is of no use either.
