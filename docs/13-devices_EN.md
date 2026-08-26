# Screen 13 — Moving the identity

## Purpose

Move the identity to another device. The screen was rewritten on 2026-08-26: it used to hold a list of one identity's devices and a way to connect a second. There are no parallel devices — **an identity has exactly one live session** (`00-mechanics_EN.md` §1), and what remains is a move, not a fleet.

## Screen elements

- A "move to another device" button — shows a QR code with a link beneath it, for when there is no camera.
- The invite's lifetime: two minutes, after which the code stops working.
- A line saying this device will go still once the move is done.

## Logic

- The invite is **single-use** and lives **two minutes**; entry may be wrong **five times** before it burns (`xor.ad/docs/chat_EN.md` §8.2).
- The key material sits **in the fragment of the link**, after the `#`. Browsers do not send that to a server — not in the request, not in the referrer, not in the logs. The key passes from device to device around us.
- The new device asks for **its own PIN**: the vault share belongs to a device, not to an identity.
- Once the move happens, **the previous device goes still immediately**: its signature is no longer accepted and it receives no new messages, not even in open conversations.
- **The disk is not wiped.** The local database stays encrypted, and if the identity is brought back the conversations come back with it.
- **On the new device the conversations are the same and the history is empty**: the messages are not in the node's database, so there is nothing to download. Older conversations stay silent there until the chat key is reissued (`xor.ad/docs/chat_EN.md` §8.13).
- There is no grace period: leaving, you close the door at once. The insurance against theft is the paper code (screen 11).

## What has to be said to the person

> The identity will move to another device. Here it will go still: new messages stop arriving, and the conversations stay on disk encrypted, returning if you bring the identity back.

> On the new device the conversations will be the same but empty: it has no history and nowhere to get one.

## Open questions

- Two minutes was taken as reasonable but never tried on real people: is it enough to walk to the second device.
- What to do if a move is started and abandoned: the invite burns by itself, but the "moving" state on the screen is not described.
