# Screen 8 — Conversation

## Purpose

A private conversation between two people, opened after both accepted the match (screen 6).

## Screen elements

- The header: the peer's **name and age**, and a **key-comparison mark** beside the name (added 2026-08-28). The mark exists because a guarantee nobody knows about works only on paper — and this one closes the single hole in the encryption: us substituting a key. Tapping the mark or the name opens the **safety code** — a string derived from both identities' long-term keys (`xor.ad/docs/chat_EN.md` §8.13), with an explanation of what it is for.
- The line of replies — short messages back and forth.
- Lines about new likes between these two — right in the conversation (screen 6).
- An input with a **256 character** counter.
- The silence-timer control in the header — 10 minutes, 30 minutes, an hour, or "while we're talking".
- A **🎲 "suggest a game"** button in the header — opens the shared board for two (screen 18).
- An **"end it"** button — closes the conversation for both at once, **with a confirmation** (settled 2026-08-27: "are you sure? the history disappears for both").
- What is left of your own timer: how long the conversation lives if you stay quiet.

## Logic

- **The reply limit is 256 characters and it comes from the server** (`max_message_length`), not baked into the client. The counter is the client's; the node is what refuses.
  The second limit, **2048 bytes of ciphertext** (`max_ciphertext_bytes`), is not shown to the person: with an honest 256 characters it is unreachable — even a string of nothing but emoji comes to 1404 bytes, and hitting 2048 takes 378 characters. It guards against a forged client, not against a real conversation.
- **Two statuses: delivered and error.** "✓" means the node passed it on; an error gives a line with a retry rather than vanishing quietly. **There is no "read"** and will not be: the node has no business knowing who opened a conversation and when.
- **The silence timer is chosen here**, not when accepting the match, and can be changed at any moment. An hour by default. Each side has their own count and cannot see the other's (`00-mechanics_EN.md` §2).
- **Expiry is announced in advance**: in its last minutes the conversation is shown fading. When it has ended for the other person, one line says so — otherwise an expired timer is indistinguishable from being snubbed.
- **An expired conversation disappears for whoever's span ran out — amended 2026-08-27.** It used to say "for both", which held while the span was shared. The span is now each person's own (§5 of the spec), and for the other it stays until their own span, marked "ended" (screen 7). Whoever had it on screen at that moment keeps a headstone reading "the conversation has ended" until they tap it, and it does not return to the list.
- **The conversation key and the game board go out for both at the first death** (§8.13). So neither side can write, even while the other still counts the conversation as alive: they keep their own history — it sits under the vault key, not the conversation key — but not the conversation.
- **"End it" is not the same as expiry.** Silence is not a decision; a button is, and so it works symmetrically: it ends the conversation for both at once. The confirmation is mandatory, because the other side loses its history without having agreed to it.
- **The peer has stepped away** (`00-mechanics_EN.md` §13) — a line saying **"stepped away"** replaces the input, with no time of return and no time of leaving. This is the only place in the whole product where anyone's presence is reported, and it is allowed because the person declared the state themselves rather than the system inferring it.
- **Conversations are not moderated** — neither for rudeness nor for explicitness: they never leave the pair of devices. Only what is published to the feed is checked (`00-mechanics_EN.md` §5).
- **There are no links in a conversation** — they are stripped, as in the feed; the one place a link lives is a neighbourhood offer (`00-mechanics_EN.md` §5).
- **Encryption happens on the devices**: the key is derived by the two of them and the node carries ciphertext (`xor.ad/docs/chat_EN.md` §8.13). A conversation is not merely unchecked — there is nothing to read it with.
- **History sits on the device** in IndexedDB, encrypted with the vault key made of the PIN and the node's share. It exists neither with us nor on another device.
- **A draft reply lives while the conversation is open and never reaches the disk — decided 2026-08-28.** Go out to the list and back, and the text is there; close the app, and it is gone. This **differs** from a phrase's draft (screen 4), which survives leaving the screen and sits in encrypted storage, and the difference is deliberate: publishing is an intention that outlives a screen, while a conversation disappears by itself, and a draft outliving it would outlive the thing that was meant to vanish.

## Open questions

- ~~Whether a conversation can be closed by hand~~ — it can, **for both at once and with a confirmation** (2026-08-26; the confirmation added 2026-08-27): the other person sees the same headstone as on expiry. Staying silent until it expires is a poor only way out of an unpleasant conversation, and a block is too large a step for it. The history on the device goes the same way as on expiry.
- ~~How long before the end the fading starts~~ — **in the last quarter of the span** (settled 2026-08-26). A fraction rather than fixed minutes: for a phrase that is the last hour-odd of 4:20, for an hour-long conversation a quarter of an hour, for a ten-minute one two and a half minutes. Fixed five minutes would put a ten-minute conversation half its life into fading.
