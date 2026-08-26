# Screen 15 — Legal Documents

## Purpose

Access to the Terms of Service, Privacy Policy, and Community Guidelines.

## Screen elements

- Links to three documents: Terms of Service, Privacy Policy, Community Guidelines.

## Logic

- The documents are short and simple, not exhaustive legal boilerplate.
- Content mirrors the rules already described in the README (Moderation, Privacy sections), rather than introducing new ones.
- The texts live in `landing/legal/`, where the documents page serves them from: `terms_EN.md`, `privacy_EN.md`, `community-guidelines_*.md`. English, one authoritative version. The root `legal/` holds pointers only.

## Open questions

- Exactly where this screen is opened from (settings, footer, a separate registration step) is not defined yet.
- ~~Whether explicit agreement is required at registration~~ — **yes, a separate checkbox** on screen 2 (settled 2026-08-26). It is a contract, and the accepted revision is recorded with the identity; a line saying "by pressing, you accept" is weaker as evidence.
