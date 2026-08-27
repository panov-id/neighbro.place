# Screen 13 — Moving the identity

## Purpose

Move the identity to another device. The screen was rewritten on 2026-08-26: it used to hold a list of one identity's devices and a way to connect a second. There are no parallel devices — **an identity has exactly one live session** (`00-mechanics_EN.md` §1), and what remains is a move, not a fleet.

## Screen elements

- A "move to another device" button — shows **nine characters** in large type, in groups of three: `K7Q - M3F - 2X9`.
- The invite's lifetime: two minutes, after which the code stops working.
- On the new device, a field where those characters are typed by hand.
- A line saying this device will go still once the move is done.

## Logic

- The invite is **single-use** and lives **two minutes**; entry may be wrong **five times** before it burns (`xor.ad/docs/chat_EN.md` §8.2).
- **No link and no QR code — amended 2026-08-27.** A QR and a link with the key in the fragment after `#` used to stand here, and the reasoning about the fragment was sound: browsers do not send it to a server. But that construction is gone. §8.2 of the spec says it outright: "**moving an identity is a code, not a link**… the pairing lives entirely inside the clients, no separate page exists for it and no separate domain is registered." The QR existed for the sake of a long link — and left with it (`xor.ad/docs/depth-client_EN.md` §5.4).
- **Nine characters, Crockford base32** without `I`, `L`, `O`, `U`: they get confused with one and zero. Case does not matter, the dashes need not be typed.
- **The key does not pass through us here either:** stretching the code yields two halves — one by which the node **finds** the invitation, the other that **unwraps** the envelope, and the second never leaves for the server. The node sees a `lookup_id` and two opaque envelopes (§8.2).
- The new device asks for **its own PIN**: the vault share belongs to a device, not to an identity.
- Once the move happens, **the previous device goes still immediately**: its signature is no longer accepted and it receives no new messages, not even in open conversations.
- **The disk is not wiped.** The local database stays encrypted, and if the identity is brought back the conversations come back with it.
- **On the new device the conversations are the same and the history is empty**: the messages are not in the node's database, so there is nothing to download. Older conversations stay silent there until the chat key is reissued (`xor.ad/docs/chat_EN.md` §8.13).
- **Confirmation on the old device is mandatory.** Before the identity leaves, it shows three lines — what the new device called itself, the same network or a different one, when — and waits for "it's me". Without it no move happens (§14 of the spec). Honestly about the limit: if somebody was talked into pressing, this will not save them; the step gives a pause and a fact.
- There is no grace period: leaving, you close the door at once. The insurance against theft is **the paper code issued at registration (screen 2)**. This used to point at screen 11, which does not exist: the code moved to registration on 2026-08-26 and the reference stayed behind.

## What has to be said to the person

> The identity will move to another device. Here it will go still: new messages stop arriving, and the conversations stay on disk encrypted, returning if you bring the identity back.

> On the new device the conversations will be the same but empty: it has no history and nowhere to get one.

## Open questions

- Two minutes was taken as reasonable but never tried on real people: is it enough to walk to the second device.
- What to do if a move is started and abandoned: the invite burns by itself, but the "moving" state on the screen is not described.
- How the three confirmation lines ("called itself", "network", "when") are shown, and how "network" differs visually from the rest, is not drawn. The network is a hint here, not a verdict, and it must not look like one.
