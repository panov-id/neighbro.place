# Screen 21 — Console

## Purpose

The place where a person sees **what the product just did and what did not work**.
Introduced 2026-09-09. Before it, the only answer to "why did it not send" was
silence: the phrase did not appear, the table was not put up, the application did
not go — and there was nothing to tell "the network dropped" from "you were
refused", in the web or in the terminal.

One screen for both faces of the client: the storefront web app and the terminal
client `depth` (`xor.ad/docs/depth-client_EN.md`). In a terminal this is the
native shape anyway — there the console is the window — while in the web it is a
separate panel that is opened rather than kept open.

## What goes into it

- **Your own actions**: "put up a table", "applied to play", "application
  refused", "sent a phrase", "left the table". The line appears when the action
  happened, and describes it in the product's words rather than the code's.
- **Errors that concern the person**: no connection, refused by quota, refused by
  age, phrase too long, the table no longer exists.
- **A timestamp** on every line, from the device's clock.

## What is not in it — decided, not forgotten (2026-09-09)

No network detail and nothing the node answered with: **no node addresses, no
headers, no request identifiers, no `lookup_id`, no socket tickets**
(`xor.ad/docs/chat_EN.md` §7 and §8.2).

The argument is not tidiness but what people do with a screenshot of a console:
they send it to support (screen 14) and post it publicly asking "what does this
mean". Everything that reaches the console must be treated as published. A request
id would tie a person's session to records on the node; a socket ticket is access;
a `lookup_id` is an identity. None of them belongs in a line a person will forward
to a stranger.

The price is stated plainly: **a network failure cannot be diagnosed from the
console**. The node's logs and the `x-request-id` in its answers are there for
that — but they belong to an operator, not to a person, and that separation is
deliberate.

## Logic

- **The console stores nothing on disk.** It lives in the memory of the tab or the
  process and disappears with it, like everything else on the device
  (`00-mechanics_EN.md` §9). No copy goes to the node: what the platform needs,
  the platform already writes in its own logs.
- **No more than two hundred lines**, then the oldest are dropped. A console is
  "what just happened", not a journal.
- **An open console changes no behaviour** and is not a developer mode: it enables
  no hidden actions and shows nothing belonging to anybody else.

## Open questions

- How the console is opened in the web — a gesture, a menu item or an address —
  is not decided.
- Whether there should be a "copy everything" button: it helps support and it also
  turns "look" into "forward", and people forward without reading.
