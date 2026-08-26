# Screen 16 — Stickers (Beyond the Alpha)

## Purpose

Decorative stickers for messages/chat (see the README's "Beyond the alpha" section). Not part of day0/the alpha.

## Logic

- The sticker catalog is fixed: populated and edited from the admin panel (see `xor.ad/docs/panel_EN.md`), images live in Bunny object storage.
- Stickers are free: the product has no payments and no internal balance. A user picks a sticker from the catalog and uses it in a message/chat.
- Regular messages stay text-only — a sticker is a separate, decorative entity, not a free-form image attachment.

## Open questions

- Where in the app the sticker catalog is opened from is not defined yet.
- ~~How many stickers per message~~ — **one, and instead of text** (settled 2026-08-26): a sticker is a reply of its own, not a decoration on a phrase.
