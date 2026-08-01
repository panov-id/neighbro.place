# The app's interface, drawn

Screens 01–17 are described in words in [`../../docs/`](../../docs/). Here they are
drawn.

The sheets are SVG because a drawing should open anywhere, diff line by line, and
be set in the product's own type: every sheet imports
[`../../landing/fonts.css`](../../landing/fonts.css) — the real Golos Text the
landing serves, not a copy of it.

## What is here

| Sheet | What it shows |
|---|---|
| [`foundations.svg`](./foundations.svg) | both themes with their contrast counted, the accents, the type scale, controls, a feed card, chat bubbles |
| [`03-feed.svg`](./03-feed.svg) | the neighbourhood feed: phone at 390×844 and a wide screen in three columns |
| `01`…`17` | the rest of the screens from [`../../docs/`](../../docs/), one sheet each |
| [`03-feed-shape.svg`](./03-feed-shape.svg) | this product's shape: a bar of four, a hard accent shadow on what just arrived, a one-at-a-time viewer |

## Where the shape comes from

From [`../../prototype/neighbro-app-proto.html`](../../prototype/neighbro-app-proto.html),
which already decided how this storefront is put together: a bottom bar of
Feed · Chats · Say · Me, `box-shadow: 5px 5px 0` in the accent on a message that
just arrived, a timer in the accent set uppercase, three columns that collapse
into rails, and a one-card-at-a-time viewer with "Skip" and "I'm in". The palette
and the type come from the landing; the shape comes from the prototype.

## The generator

Sheets `01`…`17` are built by [`render.py`](./render.py) — one definition per
screen, rendered beside itself:

```sh
python3 design/interface/render.py
```

`foundations.svg` and `03-feed.svg` were drawn by hand before the generator and
are not overwritten by it.

**The price, stated plainly.** The brother repository carries a copy of this file
with its own face and its own screens. The two storefronts share a family, not a
codebase, so the copies are expected to diverge — which is fine while the
divergence is deliberate. But if you change a screen's shape here and the brother
should follow, that is a second edit, by hand, and nothing will remind you.

## How to view them

In a browser, but **over a server rather than by double-clicking**: some browsers
refuse `@font-face` over `file://`, and the sheet then arrives in a system font
with every line the wrong width.

```sh
# from the repository root
python3 -m http.server 8080
# then http://localhost:8080/design/interface/foundations.svg
```

## Where the colours come from

From [`../../landing/index.html`](../../landing/index.html) — from what is
deployed, not from memory. The contrast figures are counted from those values.

Noticed while reading them off, and recorded on the sheet:

- The accent is **its own axis** here: `data-theme` with four values, and the gold
  `#c6a24e` is the **absence of the attribute**, not a fifth value. Light and dark
  live on a separate axis, `data-mode`.
- [`../../prototype/neighbro-app-proto.html`](../../prototype/neighbro-app-proto.html)
  disagrees with the landing twice: nine accents instead of four, and Arial Black
  as the display face instead of Golos Text. The sheets follow the landing.
- In the dark theme `--muted` on `--panel-2` measures **4.12:1** against a
  threshold of 4.5 — that is secondary text in nested plates and in incoming chat
  bubbles.
- Gold as text on the light ground measures **1.94:1**. As a fill under dark ink it
  passes comfortably (7.51:1); as a word it does not.

## The brother

The same thing for sosed:
[`sosed.place/design/interface/`](https://github.com/panov-id/sosed.place/tree/main/design/interface).
The same brutalism and the same templates, its own face.
