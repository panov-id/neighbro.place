# Screen 8 — Chat

## Purpose

The private conversation screen between two matched users.

## Screen elements

- The conversation's message feed — short back-and-forth messages.
- Notifications about new likes between these two users appear right in this feed (see screen 6).
- A message input and send control.

## Logic

- The conversation history exists only for these two participants — nowhere else.
- Unlike feed messages, the conversation doesn't disappear after 4 hours 20 minutes — it lives longer, for as long as the chat stays open.
- A chat is not moderated. Neither toxicity nor explicitness: its text goes to neither Perspective nor a language model and never leaves the pair of devices. Only what is published to the feed is checked (see `00-mechanics_EN.md`, §5).
- A conversation is encrypted **on the devices**: the key is derived by the two of them and never reaches the server, which carries ciphertext (see `xor.ad/docs/chat_EN.md` §8.13). So a chat is not merely unread — there is nothing to read it with.
- History is stored on-device in IndexedDB, encrypted with the Web Crypto API before being written (see the Privacy section in the README) — not in some separate "secure" browser storage, which doesn't exist.

## Open questions

- What "for as long as the chat stays open" means exactly — whether there's a way to close/delete the chat manually, and what happens to the history then.
- Read receipts/delivery status indicators are not defined yet.
