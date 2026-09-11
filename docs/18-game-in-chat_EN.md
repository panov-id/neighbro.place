# Screen 18 — A game inside a conversation

## Purpose

A shared board for two inside a conversation — **a field and a set of pieces**, not a list of names (amended 2026-08-27: the heading still carried "dominoes, draughts, chess", although the decision of 2026-08-26 describes a game by primitives, and the classes already stand below). The screen was created on 2026-08-26: the spec describes the game in §6 and puts a 🎲 button in the chat header, while no storefront had a screen for it.

**There are minimal rules — decided 2026-09-09, overriding the earlier "deliberately no rules".** One argument: watching the rules by hand is work, and putting it on somebody who came to play is wrong. A game stays a way to start talking rather than a contest, but the product helps run it.

**The scope of the rules differs by class of board.** Where a rule is cheap and unambiguous the engine checks everything (dominoes: a tile may only join a matching end); where it is expensive it checks only turn order, the end of a round and the score (chess, the flick game). The full breakdown by class is in `xor.ad/docs/chat_EN.md` §6.
**The price is named: the behaviour is uneven.** In dominoes the engine stops your hand, in chess it says nothing, and there is no guessing that in advance. Even behaviour would cost a chess engine inside every board — exactly what was walked away from on 2026-08-26.

**A "see the basic rules" button** opens over the board and says: what we are playing, what the product checks, what is left to agreement. Without it the rules would be a guessing game.

**A score is kept and lives as long as the conversation does.** It accumulates between games: five games played, 3:2 is shown. It goes out with the conversation. Nothing outlives that: no history of wins, no mark on an identity.

## How it opens

- The **🎲 "suggest a game"** button in the conversation header → pick a board → an offer goes to the other person → they accept, and the board opens for both.
- Changing the game uses the same offer. A refusal breaks nothing: the conversation carries on in words.
- **The board does not go out by itself — decided 2026-08-29.** A game has ended (by agreement, since there are no rules) — the board stays. There is no "the engine decided the game was finished" here and there cannot be: it knows no rules, so it cannot know the end.
  **In a pair the board stays up even after a refusal to play again — clarified 2026-09-09.** It lives inside the conversation and goes out with it, not with the outcome of a game. This used to say "if everyone declines, the board closes", which in a pair meant one "not again" took the board away from both.
- **"Play again" asks what to play — the same game or another (2026-09-09).** These used to be two buttons, "play again" and "suggest another game", doing the same thing in the same second. Now there is one, and the same game comes first in the choice.
  **There are three ways to answer:** agree, finish, or **propose your own** — another board instead of the one named. A counter-proposal passes the ball back, and the exchange runs as long as it needs to: this is a conversation about what to play, not a vote. "Finish" stands apart from "propose your own" on purpose — otherwise declining one game would be indistinguishable from declining to play at all.
- **"Resign" and "offer a draw" are statements, not verdicts (2026-09-09).** The engine knows no rules, so it can neither award a win nor check a draw. "I resign" is a unilateral announcement and the game is over for the people; "draw" is a proposal accepted by agreement. **No result is recorded anywhere:** no score, no history of games, no mark on an identity — none of those exist by construction, and adding them for two buttons would be adding a competition where the game exists as an excuse to start talking.
- **In a pair, one person leaving ends the game — decided 2026-08-29.** There is nobody to wait for in a pair: the other participant is gone. At a table it is the opposite — the one who remains **waits for someone to sit down** (screen 19: a table with one person seated is a normal state).
- The board lives inside the conversation and **goes out for both at the first death** (amended 2026-08-27): spans are now each person's own, and the board leaves with the conversation — no longer because its key went out: since 2026-09-09 it does not sit under that key, but because the conversation's span ran out as soon as it goes out for either side (`xor.ad/docs/chat_EN.md` §8.13). There is nothing to wait for: neither side can write or move any more anyway.

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
- **The play is visible in the conversation — decided 2026-09-09.** Every move
  becomes a line: "Anya placed a tile on e4", "Petya flicked". These words used to
  exist for the screen reader only (2026-08-29) — now everybody sees them. The
  argument: the position changes silently, and an opponent's move is
  indistinguishable from a slip; and the vocabulary of coordinates per class of
  board is already written, so there is nothing to invent twice.
  **In a pair this is a system line in the conversation, and it is not encrypted**,
  unlike the messages beside it: it is part of the game state. The difference has to
  be said to the person plainly — your words are closed, your moves are not.
- **Moves and board state are not encrypted — decided 2026-09-09.** Only whoever sees the board can check the rules, so the board, and only the board, is outside end-to-end encryption. **The messages are encrypted as before** (`xor.ad/docs/chat_EN.md` §8.13): the node knows what you are playing and how, and does not know what you are saying. Saying so on the screen is required — next to what is already written about shuffling a deck, which the node saw anyway.
- **In a pair the state sits in a game cache — rewritten 2026-09-10:** the node judges as the game goes, and it needs the position to do so; this used to read "never written to the database", and a node restart lost the game. The price is named plainly: the position, whose turn and the score sit on the node unencrypted while the conversation lives. There are no replies in the cache. At a table it is the other way round — everything is public there, and the state sits in the database beside the table (screen 19).
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
- ~~What happens to the board on a lost connection~~ — **whoever returns takes the state from the peer** (settled 2026-08-27): the node carries and, since 2026-09-10, holds the position in a game cache. This used to read "there is no board in the database and there will not be" and "if both drop at once, the game is lost for good": with the cache it is not lost, and whoever returns takes the position from the node.
- ~~Whether an undo is needed at all~~ — **there is one, but as a request rather than a button (decided 2026-08-29).** "Put it back" sends a proposal to the others; once **everyone** agrees, the board steps back once. There is no unilateral undo for the same reason there is no turn order and no table owner: nobody holds power over a shared board.
  **The engine keeps exactly one previous snapshot**, not a history: it sits in the node's memory and is not encrypted — like the board itself since 2026-09-09; it does not reach the game cache, which holds the current position alone. Two steps back are impossible, and that is not an omission.
  **At a table everyone playing agrees** (screen 19; clarified 2026-09-09 — there are spectators at a table from that day, and they are not in the game); the more people, the more expensive an undo — a price accepted, because a cheap undo in company is precisely how somebody else's game gets spoiled.
