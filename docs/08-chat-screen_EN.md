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
- Every sent message goes through the same AI check as feed messages (see the Moderation section), but without the captcha/rate limit — those apply only to publishing in the feed (see screen 4).
- History is stored on-device in IndexedDB, encrypted with the Web Crypto API before being written (see the Privacy section in the README) — not in some separate "secure" browser storage, which doesn't exist.

## Open questions

- What "for as long as the chat stays open" means exactly — whether there's a way to close/delete the chat manually, and what happens to the history then.
- Read receipts/delivery status indicators are not defined yet.
