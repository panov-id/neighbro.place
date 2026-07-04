# Screen 17 — Stickers (Beyond the Alpha)

## Purpose

Decorative stickers for messages/chat, purchased with the internal balance (see the README's "Beyond the alpha" section). Not part of day0/the alpha.

## Logic

- The sticker catalog is fixed: populated and edited from the admin panel (see `xor.ad/docs/panel_EN.md`), images stored via Supabase Storage/imgproxy.
- A user buys a sticker with balance in the app and can use it in a message/chat.
- Regular messages stay text-only — a sticker is a separate, decorative entity, not a free-form image attachment.

## Open questions

- Where in the app the sticker catalog is opened from is not defined yet.
- Sticker prices are not defined yet.
- A cap on the number of stickers per message is not defined yet.
