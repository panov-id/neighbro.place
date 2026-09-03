# Screen 18 — A game inside a conversation

## Purpose

A shared board for two inside a conversation — **a field and a set of pieces**, not a list of names (amended 2026-08-27: the heading still carried "dominoes, draughts, chess", although the decision of 2026-08-26 describes a game by primitives, and the classes already stand below). The screen was created on 2026-08-26: the spec describes the game in §6 and puts a 🎲 button in the chat header, while no storefront had a screen for it.

**There are deliberately no rules.** The engine draws the board and lets pieces be moved freely; how to play is for the two to agree. It is a way to start talking rather than a contest, so there is no score, no winner and no move validation here.

## How it opens

- The **🎲 "suggest a game"** button in the conversation header → pick a board → an offer goes to the other person → they accept, and the board opens for both.
- Changing the game uses the same offer. A refusal breaks nothing: the conversation carries on in words.
- **The board does not go out by itself — decided 2026-08-29.** A game has ended (by agreement, since there are no rules) — the board stays, and "play again" becomes a proposal: **whoever agrees, plays**. If everyone declines, the game is over and the board closes. There is no "the engine decided the game was finished" here and there cannot be: it knows no rules, so it cannot know the end.
- **In a pair, one person leaving ends the game — decided 2026-08-29.** There is nobody to wait for in a pair: the other participant is gone. At a table it is the opposite — the one who remains **waits for someone to sit down** (screen 19: a table with one person seated is a normal state).
- The board lives inside the conversation and **goes out for both at the first death** (amended 2026-08-27): spans are now each person's own, and the board leaves with the conversation key as soon as it goes out for either side (`xor.ad/docs/chat_EN.md` §8.13). There is nothing to wait for: neither side can write or move any more anyway.

## Screen elements

- The board and the pieces; dragging is available to **both, at any moment**.
- A highlight on the piece the other person is dragging right now, so the two do not tug at one piece blindly.
- A **"take turns"** toggle — by agreement of both (settled 2026-08-26).
- **Keyboard control — decided 2026-08-29, and the grammar is taken from the terminal.** Until that day the only way to move was dragging, which left the board unusable from a keyboard and unreadable to a screen reader — while `depth` had solved the same problem long ago: `[hjkl] select · [enter] move · [esc] leave`. The web gets the same: arrows select a cell or a piece, Enter takes and puts, two keys rotate and flip. Nothing had to be invented: **the four operations on a piece were the vocabulary already**.
  **The price is accepted:** the web now has two ways to move instead of one — mouse and keys — and both have to be drawn, including the "piece taken by keyboard" state.
- **The other person's move is announced in words — decided 2026-08-29:** "Anya put a piece on e4", "Anya flipped the checker on c3". Not "made a move": to understand that, a screen reader would have to walk the whole board again after every twitch.
  **Each class of board has its own vocabulary of coordinates.** A grid board has cells; a dot grid has edges; a **free table has no coordinates at all**, and there adjacency is announced instead: "placed it against the six". Imposing a grid on dominoes for the sake of narration is not on — it would change the game itself.
  **The limit is named honestly:** in the "physics" class (crokinole-style flicking) a coordinate is meaningless — a flick ends wherever it rolls. The reader gets "Anya flicked", and it is the one class that stays sighted.
- A way back to the messages without closing the board.

## Logic

- **Your own move holds your conversation exactly as your own message does** (settled 2026-08-27). The timer counts from your last action, and a move is an action: the game exists precisely so that one can be silent in words. **Their move does not push your timer** — for the same reason their line does not: whoever is silent is silent.
- Play in silence long enough and the conversation lives for both — each pushes their own timer with their own moves. A spectator who only watches somebody else move loses it exactly as if they had left.
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
- **The "touch target no smaller than 44 px" rule does not extend to a board's cells — decided 2026-08-29.** Two documents disagreed: the screen allowed zoom while `xor.ad/docs/accessibility-and-i18n_EN.md` demanded 44 px of any target. It is resolved in favour of zoom, and the line is drawn by meaning: 44 px is about **controls** — buttons and menus, where a miss takes you somewhere else; a board's cell is a surface a person magnifies themselves, and a miss on it costs one move back. The price is named: this is the first exception in a list that had held without any.

## Open questions

- ~~The set of boards at launch~~ — **all three at once: dominoes, draughts, chess** (decided 2026-09-02). The engine is one and knows no rules, so a third board costs a third set of pieces and a board's markings, not a third engine. The price is named: three times the artwork of starting with one.
- ~~What happens to the board on a lost connection~~ — **whoever returns takes the state from the peer** (settled 2026-08-27), over the same encrypted channel: the node carries but does not store — there is no board in the database and there will not be. The cost is named: if both drop at once, the game is lost for good, with nowhere to restore it from.
- ~~Whether an undo is needed at all~~ — **there is one, but as a request rather than a button (decided 2026-08-29).** "Put it back" sends a proposal to the others; once **everyone** agrees, the board steps back once. There is no unilateral undo for the same reason there is no turn order and no table owner: nobody holds power over a shared board.
  **The engine keeps exactly one previous snapshot**, not a history: it sits in memory, is encrypted under the same key and never reaches the database, like the board itself. Two steps back are impossible, and that is not an omission.
  **At a table everyone seated agrees** (screen 19); the more people, the more expensive an undo — a price accepted, because a cheap undo in company is precisely how somebody else's game gets spoiled.
