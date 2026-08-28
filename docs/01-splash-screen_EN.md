# Screen 1 — Splash

## Purpose

The first screen a person sees on opening neighbro.place. A splash and nothing else: the animation and one way onward. There is no registration here — **edit of 2026-08-26**: age moved to screen 2, where name, age, PIN and the paper code are asked in a single step, as in flow 1 of the spec (`xor.ad/docs/chat-flows_EN.md`) and in the terminal client. The faces must not diverge in the order of their steps: the core is one, and a splash is no place for a registration field.

## Visual

An animation themed around neighbourliness, friendship and shared activities — simple icons appearing and disappearing in a loop. The style follows the platform's Soviet-flavoured visual identity. There is nothing else on the screen.

## Screen elements

- Icon animation themed around neighbourliness, friendship and shared activities — **the main thing on the screen**.
- **One line saying what this is** (added 2026-08-28): that neighbours nearby are
  talking and that what is said disappears. Without numbers — those are forbidden
  here by a separate decision — but with words: nobody should go through
  registration without understanding where they have arrived.
- **Two ways in** (added 2026-08-28): "create an identity" and, quieter and
  smaller, "I already have one". The second leads to a choice: a code from another
  device (screen 13) or the paper recovery code.
- A "next" button — icon only, no text label.

## Logic

- Nothing is asked and nothing is required: the screen is passed with one tap.
- **The second way in closes a gap between the faces — decided 2026-08-28.** In the
  terminal the first screen offers three paths: create an identity, move one here,
  raise one from the paper code. On the web the splash offered one — "next", that
  is, registration. Someone who has an identity and a new device went nowhere: the
  paper code is issued on screen 2 and there was no place to use it. The core is
  one, and the faces have no right to differ on which entrances exist.
- **The application's splash and the landing's splash are different, by design**
  (decided 2026-08-28). The landing speaks to a passer-by; the application's splash
  is the threshold of a home, separating a storefront full of text from a place
  where everything disappears. The price is accepted: someone arriving from the
  landing sees two animations in a row.
- **The screen's job is to show the character of the place** (decided 2026-08-28),
  so the animation stays the content rather than the background: the line and the
  two entrances sit at the bottom and do not compete with it. Language and rules
  are **not** added here — they belong on screen 2, where a person has already
  stopped to read.
- `prefers-reduced-motion` turns off the animation and the fades — the rule is shared (`00-mechanics_EN.md` §4).
- **There are no live numbers on the splash — settled 2026-08-26, retiring them together with the zero rule.** "How many people are online nearby, how many messages in the last hour" used to stand here, and it is gone for two reasons, either of which would be enough on its own.

  First: "people online" reports somebody else's presence, and the spec (`xor.ad/docs/chat_EN.md` §8.2) calls `stepped_away` the **only** exception to "we do not report anyone's presence". We are not opening a second one — least of all on a storefront anyone can see.

  Second: an exact figure tied to the surroundings is a measuring instrument (§4 of the mechanics). That is why the radius handle returns a step and computes on release; on the splash it would be handed to **an anonymous visitor, with no identity and no signature**, and from an approximate point at that. Opening the page through a VPN in another city to take a density reading of somebody's district must not be easier than creating an identity.

  The price is named: the splash loses its only argument that there is life here, and a person registers without knowing whether they will find neighbours. That is accepted deliberately — an empty feed after registration is better than a rule that grew a second exception.

## Next step

→ [Screen 2 — About you](./02-name-screen_EN.md)

## Open questions

- The exact set of icons for the animation is not defined yet.
- The exact icon for the "next" button is not defined yet.
