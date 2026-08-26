# Screen 18 — A game inside a conversation

## Purpose

A shared board for two inside a conversation: dominoes, draughts, chess. The screen was created on 2026-08-26: the spec describes the game in §6 and puts a 🎲 button in the chat header, while no storefront had a screen for it.

**There are deliberately no rules.** The engine draws the board and lets pieces be moved freely; how to play is for the two to agree. It is a way to start talking rather than a contest, so there is no score, no winner and no move validation here.

## How it opens

- The **🎲 "suggest a game"** button in the conversation header → pick a board → an offer goes to the other person → they accept, and the board opens for both.
- Changing the game uses the same offer. A refusal breaks nothing: the conversation carries on in words.
- The board lives inside the conversation and **disappears with it** — the silence timer runs out, or the conversation is ended by hand, and the board is gone.

## Screen elements

- The board and the pieces; dragging is available to **both, at any moment**.
- A highlight on the piece the other person is dragging right now, so the two do not tug at one piece blindly.
- A **"take turns"** toggle — by agreement of both (settled 2026-08-26).
- A way back to the messages without closing the board.

## Logic

- **A move pushes the conversation's timer.** Activity is any shared action, not only text: the game exists precisely so that one can be silent in words (`xor.ad/docs/chat_EN.md` §8.10).
- **Turn-taking is an agreement, not a rule.** Both switch it on if it suits them, and off the same way. Wiring turns into the engine is not allowed: the whole point is the absence of rules.
- **The board state is encrypted with the same key as the messages** and is never written to the database — it is in transit, like the messages themselves (`xor.ad/docs/chat_EN.md` §8.13).
- Synchronisation goes over the same socket as the replies.

## The set of games and how it works

A game here is described by **a field and a set of pieces**, not by its name: one engine drives every board (`xor.ad/docs/chat_EN.md` §6). Hence the order of things: a new game is a row in a table, not a new screen.

| Class | Games | What it adds |
|---|---|---|
| Grid board | draughts, chess, giveaway, corners, big-board noughts and crosses | nothing beyond the four operations |
| Free table | dominoes | nothing |
| Grid of points | dots | drawing along edges |
| Deck and hand | durak, poker, uno | shuffling, a private hand, a discard pile |
| Dice | backgammon | a roll |
| Physics | flick-draughts | a flick with rebounds |
| Text | hangman | entering a word |

The four operations on a piece — **take, place, rotate, flip** — cover the first three classes entirely: rotation is for dominoes, flipping for a crowned draught.

**What has to be said to the person on the screen itself:**

- **In cards, uno and backgammon the node shuffles and rolls, and it sees the layout.** This is the one place in the product where the node knows contents: it does not read messages or a board without randomness, but it does read a deck it deals itself. Fair randomness works no other way: if somebody's phone shuffles, that phone sees the others' cards.
- **Your own hand is visible only to you**; everyone else sees backs.
- **A word guessed in hangman goes through the queue**, like a phrase: another person will see it. Refused — guess another.
- **Zooming on a large board is fine.** Go and backgammon do not fit a phone without it, and that is the price of the game rather than a fault.

## Open questions

- The set of boards at launch: dominoes, draughts and chess, or starting with one.
- What happens to the board if one of the two loses connection mid-move.
- Whether an undo is needed at all, given there are no rules and so no "wrong" moves.
