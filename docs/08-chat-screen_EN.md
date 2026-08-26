# Screen 8 — Conversation

## Purpose

A private conversation between two people, opened after both accepted the match (screen 6).

## Screen elements

- The line of replies — short messages back and forth.
- Lines about new likes between these two — right in the conversation (screen 6).
- An input with a **256 character** counter.
- The silence-timer control in the header — 10 minutes, 30 minutes, an hour, or "while we're talking".
- What is left of your own timer: how long the conversation lives if you stay quiet.

## Logic

- **The reply limit is 256 characters and it comes from the server** (`max_message_length`), not baked into the client. The counter is the client's; the node is what refuses.
  The second limit, **2048 bytes of ciphertext** (`max_ciphertext_bytes`), is not shown to the person: with an honest 256 characters it is unreachable — even a string of nothing but emoji comes to 1404 bytes, and hitting 2048 takes 378 characters. It guards against a forged client, not against a real conversation.
- **Two statuses: delivered and error.** "✓" means the node passed it on; an error gives a line with a retry rather than vanishing quietly. **There is no "read"** and will not be: the node has no business knowing who opened a conversation and when.
- **The silence timer is chosen here**, not when accepting the match, and can be changed at any moment. An hour by default. Each side has their own count and cannot see the other's (`00-mechanics_EN.md` §2).
- **Expiry is announced in advance**: in its last minutes the conversation is shown fading. When it has ended for the other person, one line says so — otherwise an expired timer is indistinguishable from being snubbed.
- **An expired conversation disappears for both**; whoever had it on screen keeps a headstone reading "the conversation has ended" until they touch it, and it does not return to the list.
- **Conversations are not moderated** — neither for rudeness nor for explicitness: they never leave the pair of devices. Only what is published to the feed is checked (`00-mechanics_EN.md` §5).
- **There are no links in a conversation** — they are stripped, as in the feed; the one place a link lives is a neighbourhood offer (`00-mechanics_EN.md` §5).
- **Encryption happens on the devices**: the key is derived by the two of them and the node carries ciphertext (`xor.ad/docs/chat_EN.md` §8.13). A conversation is not merely unchecked — there is nothing to read it with.
- **History sits on the device** in IndexedDB, encrypted with the vault key made of the PIN and the node's share. It exists neither with us nor on another device.

## Open questions

- Whether a conversation can be closed by hand before it expires, and what happens to the history then.
- How many minutes before the end the fading starts — shared with the feed phrase, and undefined (`00-mechanics_EN.md` §2).
