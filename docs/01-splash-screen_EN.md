# Screen 1 — Splash

## Purpose

The first screen a person sees on opening neighbro.place. A splash and nothing else: the animation, the live numbers and one way onward. There is no registration here — **edit of 2026-08-26**: age moved to screen 2, where name, age, PIN and the paper code are asked in a single step, as in flow 1 of the spec (`xor.ad/docs/chat-flows_EN.md`) and in the terminal client. The faces must not diverge in the order of their steps: the core is one, and a splash is no place for a registration field.

## Visual

An animation themed around neighbourliness, friendship and shared activities — simple icons appearing and disappearing in a loop. The style follows the platform's Soviet-flavoured visual identity. Alongside it a live infographic shows real numbers from the platform: how many people are online nearby, how many messages in the last hour.

## Screen elements

- Icon animation themed around neighbourliness, friendship and shared activities.
- Live platform activity numbers, beside the icons.
- A "next" button — icon only, no text label.

## Logic

- Nothing is asked and nothing is required: the screen is passed with one tap.
- `prefers-reduced-motion` turns off the animation and the fades — the rule is shared (`00-mechanics_EN.md` §4).
- An empty place does not lie: with nobody nearby the numbers show **zero** — and beside it an invitation to be the first, not an apology (settled 2026-08-26). Substituting "‹1", or platform-wide numbers instead of nearby ones, is not allowed: a person expecting neighbours would get an empty feed.

## Next step

→ [Screen 2 — About you](./02-name-screen_EN.md)

## Open questions

- The exact set of icons for the animation is not defined yet.
- The exact icon for the "next" button is not defined yet.
