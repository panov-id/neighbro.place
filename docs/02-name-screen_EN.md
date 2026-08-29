# Screen 2 — About you

## Purpose

The one step of signing up: name, age and PIN. It ends here — the feed comes next. **Edit of 2026-08-26:** the birth year used to be asked on the splash, the name was optional, and there was no PIN at all.

## Two steps — decided 2026-08-28

The screen is split in two. The number stays one: renumbering twenty screens for
the sake of one fork costs more than describing it inside.

| Step | What is asked | Why together |
|---|---|---|
| 1. Who you are | name, age, language, acceptance of the terms | these are facts about a person and their consent; a mistake here is harmless, all of it is editable later |
| 2. What brings you back | PIN, paper code | these are keys: the PIN encrypts what is local, the code returns the identity. A mistake here is fixed by nothing |

**The argument for splitting:** one screen carried six elements and two
confirmations in a row — the narrowest place in the product, and the first thing a
person sees. Two steps put the pause exactly where the subject changes: before it
the conversation is about you, after it about how to get you back.

**The faces do not diverge because of this.** In the terminal registration already
goes one question at a time (`depth new`: name, age, PIN, paper code, area), so
the web is not stepping away from §13 but closer to it. The order stays mandatory:
name and age, then the PIN and the exchange with the node for its share, then the
code.

**The price is named:** one more transition, and some people will drop out between
the steps — right at the border where the conversation about losing an identity
begins.

## Screen elements

- A name field — **required**, up to **24 characters**: that is what fits the conversation header and the match card at 375px without an ellipsis. A counter shows what is left; the limit counts graphemes and **the node enforces it** (`xor.ad/docs/chat_EN.md` §8.2), not this field alone.
- Age — **a number of years** (settled 2026-08-26: the same as the node stores in its `age` column; once a year the app asks again, "still 38?"). Next to the field, a line saying **"13 and over"**, said before the input rather than after it.
- A six-digit PIN, entered twice. An obvious one (`000000`, `123456`, one's own birth year) produces the line "this PIN is easy to guess" — and does **not** lock: the button stays live.
- **The paper recovery code**: sixteen characters in **four groups of four**, shown once, with a confirmation — type back **two of the four groups** (the format comes from `xor.ad/docs/chat_EN.md` §8.2: Crockford base32 without `I`, `L`, `O`, `U`, which are confused with one and zero; case does not matter).
- A line saying the identity lives on this device, and what brings it back.
- **Acceptance of the terms and the rules** (added 2026-08-28): a checkbox with
  links that open the documents right here. Without it the "next" button stays
  inactive.
- **A language switcher** (moved here from the splash on 2026-08-28): taken from
  the browser by default, but someone whose phone is in a language they do not read
  has to be able to fix that before typing their own name.
- A "next" button — icon only, no text label (same as screen 1).

## Logic

- **The terms are accepted before the first screen, not after — recorded
  2026-08-28.** The requirement stands in `xor.ad/docs/dsa/SPEC_EN.md` §7.1 and in
  the terminal client ("a face without accepted documents does not work"), and this
  screen had no such element at all: a person registered having accepted nothing.
  The **date and hash** of the accepted text are stored next to the identity —
  a row per each of the three documents in `legal_acceptances` (decided
  2026-08-29, screen 15; the schema is in `xor.ad/docs/migrations-step1_EN.md`) — on a new revision the documents are shown
  again, and "new" is decided by the hash rather than by the memory of whoever
  edited the file.
- **The name is required.** It is published text: the other person sees it on the match card and in the chat, so it goes through the same moderation queue as a phrase — but **at the first publication**, not here: until then it is visible to nobody (`00-mechanics_EN.md` §5).
- **Age is asked before the feed**, because the feed itself depends on it: it is cut by age bands, and without the number there is nothing to assemble it from. What is asked is the number of years, not a date of birth: a full date is more precise than the product needs and works against the minimisation stated in the policy.
- **The PIN is required and asked here.** It locks an open tab and takes part in encrypting everything on disk. It cannot be deferred: the terminal client writes its key file immediately (`00-mechanics_EN.md` §1).
- **An obvious PIN warns rather than forbids — settled 2026-08-26.** A ban would hit exactly the person who barely reached the end of the single registration screen, and the gain is smaller than it looks: a million options are no defence with or without a list — the node's share and the ten-attempt counter are.
- **The lower age bound is said out loud — settled 2026-08-26.** The database carries `CHECK (age >= 13)` — **there is no upper bound, decided 2026-08-28**: age is not capped from above at all, because an invented ceiling would cut off a living person for the sake of catching a typo, and the band's right edge already carries no number ("no limit", screen 3), and until this decision a twelve-year-old got a refusal from the node with not one word about why. The cost is accepted and known: the line does hint which number to type in order to pass — but there is no age verification here at all, the spec calls it self-declaration, and silence would add no check, only take the explanation away from the honest.
- **The paper code is issued here — settled 2026-08-26** (overriding the move to the first chat of 2026-08-18). The reason is not that there is something to lose before the chat, but that the cost of being wrong is asymmetric: a screen that fails to convince mends itself — the person returns a day later; a device lost without a code never comes back.
- **The code is shown once and confirmed by typing two groups.** Without the confirmation the "next" button stays inactive: "next" gets pressed unread, and recovery cannot ask afterwards.
- After the button, straight to the feed. There is no separate geolocation screen: position and radius live inside the feed.
- Signing up completes on this step: the keys are born on the device, the node mints an identifier and keeps only the public half of the key.

- **Agreement with the documents is a separate checkbox**, not a line under the button (settled 2026-08-26). It is the contract everything else rests on, and the accepted revision is recorded with the identity. Links to the three documents sit beside it (screen 15).
- **Breaking off halfway means there is no identity.** Close the tab between seeing the code and confirming it, and signing up is not complete: come back and you start again, with a new code. Otherwise an identity without insurance would exist, and the code cannot be shown twice.

## What has to be said to the person

On the screen itself, not in small print:

> **Write this code down on paper.** It is the only way to bring your identity back. We have no email and no password — lose the device or clear the site's data, and there is nothing to restore you with, and we cannot look the code up: we do not have it. It will not be shown a second time.

A separate line about the conversations, because the code does not bring those back:

> The identity comes back with the code. The conversations do not: they exist neither with us nor anywhere else.

## Next step

→ [Screen 3 — Feed](./03-feed-screen_EN.md)

## Open questions

- The name field's placeholder is not defined yet.
- Whether the warning about losing the identity is shown only here or stays reachable in settings.
- ~~A name length limit~~ — **24 graphemes, refused by the node** (settled 2026-08-26). The item sat here as open while the number stood a paragraph above in this same file; what was missing was the rule on the node, and now it exists.
- ~~The format of the code~~ — **four groups of four, Crockford base32 without `I`, `L`, `O`, `U`**, confirmed with two of the four groups. Not a decision but a transfer from the spec: it was written there and missing here.
- ~~What happens if the person closes the tab between seeing the code and confirming it~~ — the answer stood in this screen's own "Logic": there is no identity, and registration starts again with a new code.
