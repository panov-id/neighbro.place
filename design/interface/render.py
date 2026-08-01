# The screens of neighbro.place, drawn — both themes, at ×2.
#
# One definition per screen, rendered into design/interface/ beside this file:
#
#     python3 design/interface/render.py
#
# Each sheet carries the screen twice: once on the dark ground, which is the
# default, and once on the light. Not the same drawing re-coloured — the screen is
# a function of its face and is asked again with the light one, because a colour
# written inline does not answer to a class.
#
# The face carries geometry as well as colour, and that is the point: these two
# products are not one product in two palettes. Radius, border weight, whether a
# surface throws a hard offset shadow, whether a bubble clips one corner, whether
# a key is round or square, whether what is chosen is washed or ringed — all of it
# is read off ../../landing/index.html and lives in BRAND.
#
# A sheet carries the drawing and nothing else. What a screen leaves undecided is a
# question about the product; it belongs in ../../docs/, where it is maintained.
#
# THE BROTHER HAS A COPY OF THIS FILE. sosed.place/design/interface/render.py carries the same
# script with its own face and its own screens. The two products share a family
# and not a codebase, so the copies are expected to diverge — but if you change
# the shape of a screen here and the brother should follow, that is a second
# edit, by hand, and nothing will remind you.

import os

OUT = os.path.dirname(os.path.abspath(__file__))

BRAND = dict(
    key="neighbro",
    title="neighbro", dot="●",
    bg="#0c0b09", panel="#14120e", panel2="#26221a", border="#3a331f",
    fg="#ede8dd", muted="#8a8172", muted2="#928979",
    accent="#c6a24e", accent_text="#c6a24e", ink="#1a1509",
    warn="#c6a24e", err="#ff8a80",
    brow="#c6a24e",
    places=["KREUZBERG", "NEUKÖLLN", "MITTE", "PRENZLAUER BERG", "WEDDING"],
    here="kreuzberg",
    # Printed matter on a board: right angles, a hard offset shadow that is the
    # distance to the paper, and a ring rather than a wash. The outgoing bubble's
    # shadow mirrors — it always falls away from whoever is speaking.
    radius=0, bw=2, depth=4, tail=0, avatar="square", pick="ring",
    phone_r=(42, 30),
)

# The light half of each face. Read off the same landing/index.html: sosed puts
# it in :root[data-theme="light"], neighbro in [data-mode="light"]. The accent is
# NOT here — it arrives from the other axis and is identical in both themes, which
# is why an accent eyebrow that passes on a dark ground fails on a light one.
LIGHT = {
    "neighbro": dict(bg="#e9e6dd", panel="#f4f1e8", panel2="#ded9cc", border="#1e1b14",
                     fg="#181510", muted="#5f5a4e", muted2="#5c5749",
                     # gold is 1.94:1 as a word here — the worst number in either
                     # storefront — so it may only be a fill
                     brow="#5c5749", warn="#735b25", accent_text="#735b25"),
}

def lit(b):
    """The same face, in the light theme."""
    return dict(b, **LIGHT[b["key"]])

def L(brand, ru, en):
    """A string with a face. Not a translation table — the two products speak
    differently, and a screen that says the same thing twice is one product."""
    return ru if brand["key"] == "sosed" else en

# ────────────────────────────────────────────────────────────────── primitives ──
def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))

def text(x, y, s, cls="body", style="", size=None, anchor=None):
    a = f' text-anchor="{anchor}"' if anchor else ""
    z = f' font-size="{size}"' if size else ""
    st = f' style="{style}"' if style else ""
    return f'<text x="{x}" y="{y}" class="{cls}"{z}{st}{a}>{esc(s)}</text>'

def rect(x, y, w, h, fill, stroke=None, r=0, opacity=None, sw=1):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    o = f' opacity="{opacity}"' if opacity is not None else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"{s}{o}/>'

def circle(cx, cy, r, fill="none", stroke=None, opacity=None, width=1):
    s = f' stroke="{stroke}" stroke-width="{width}"' if stroke else ""
    o = f' opacity="{opacity}"' if opacity is not None else ""
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"{s}{o}/>'

def line(x1, y1, x2, y2, stroke, w=1, cap=None):
    c = f' stroke-linecap="{cap}"' if cap else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{w}"{c}/>'

def g(tx, ty, body, opacity=None):
    o = f' opacity="{opacity}"' if opacity is not None else ""
    inner = "\n".join("      " + b for b in body)
    return f'    <g transform="translate({tx},{ty})"{o}>\n{inner}\n    </g>'

def plate(b, x, y, w, h, fill=None, stroke=None, r=None, shadow=None):
    """A surface in the brand's own geometry. neighbro throws a hard offset shadow
    because its landing does — eleven of them — and rounds nothing; sosed rounds 16
    and casts nothing, because its depth is ambient light and a drawing cannot
    show that honestly at this size."""
    r = b["radius"] if r is None else r
    out = []
    off = b["depth"] if shadow is None else shadow
    if off:
        out.append(rect(x + abs(off), y + abs(off), w, h, b["border"], None, r) if off > 0
                   else rect(x + off, y - off, w, h, b["border"], None, r))
    out.append(rect(x, y, w, h, fill or b["panel"], stroke or b["border"], r, sw=b["bw"]))
    return out

# ─────────────────────────────────────────────────────────── screen furniture ──
# The two products are not one product in two palettes. neighbro's own prototype
# (prototype/neighbro-app-proto.html) already decided its shape: a bottom bar of
# four, a hard accent shadow on a message that just arrived, a timer in the
# accent, three columns that collapse into rails, and a one-card-at-a-time viewer
# with skip and join. So neighbro gets that, and sosed gets what its landing
# argues for instead: one column, no bar, a round accent button floating over the
# feed, and a rule down the left edge of what is new.

def filter_icon(b, x, y):
    return [rect(x, y, 44, 44, b["panel2"], b["border"], 12),
            line(x + 13, y + 16, x + 31, y + 16, b["accent"], 2, "round"),
            line(x + 16, y + 22, x + 28, y + 22, b["accent"], 2, "round"),
            line(x + 19, y + 28, x + 25, y + 28, b["accent"], 2, "round")]

def header(b, title, sub, icon=True):
    """sosed: the district, set large, and the filter. neighbro: a working top
    bar — where you are, how many are near, and who you are."""
    if b["key"] == "sosed":
        out = [text(20, 64, title, "disp", size=20), text(20, 84, sub, "mono")]
        if icon:
            out += filter_icon(b, 310, 46)
        out.append(line(0, 104, 374, 104, b["border"]))
        return out
    if not icon:
        return [text(24, 64, "‹", "disp", f'fill:{b["accent_text"]}', 22),
                text(48, 60, title, "small", "font-weight:700"),
                text(48, 78, sub, "timer"),
                rect(310, 46, 44, 44, b["panel2"], b["border"], 0, sw=b["bw"]),
                text(332, 74, "···", "disp", f'fill:{b["muted2"]}', 16, "middle"),
                line(0, 104, 374, 104, b["border"])]
    out = [rect(16, 44, 128, 30, b["panel2"], b["border"], 15),
           f'<path d="M32 52 q6 0 6 6 q0 5 -6 10 q-6 -5 -6 -10 q0 -6 6 -6 z" fill="none" '
           f'stroke="{b["accent"]}" stroke-width="2"/>',
           text(46, 64, sub, "mono"),
           circle(166, 59, 4, b["accent"]),
           text(178, 63, title, "small"),
           rect(258, 44, 100, 30, b["panel2"], b["border"], 15),
           circle(276, 59, 7, "none", b["muted2"]),
           text(292, 63, L(b, "Вы", "You"), "small"),
           line(0, 96, 374, 96, b["border"])]
    return out

def card(b, y, brow, lines, meta, plus=True, w=342, x=16, fresh=False, fade=False):
    """A message. Fresh means it has just arrived: neighbro says so with the accent
    in the shadow, sosed with a rule down the left. Fade is neighbro's alone — the
    plate at the bottom of the feed is literally going, which is the one property
    of this product that a drawing can state without a word."""
    h = 40 + 20 * len(lines) + (18 if meta else 0)
    out = []
    if b["depth"]:
        off = b["depth"]
        out.append(rect(x + off, y + off, w, h, b["accent"] if fresh else b["border"], None, b["radius"]))
    out.append(rect(x, y, w, h, b["panel"], b["border"], b["radius"], sw=b["bw"]))
    if fresh and not b["depth"]:
        out.append(rect(x, y + 12, 3, h - 24, b["accent"], None, 2))
    tx = x + (24 if fresh and not b["depth"] else 16)
    out.append(text(tx, y + 24, brow, "brow"))
    for i, ln in enumerate(lines):
        out.append(text(tx, y + 48 + 20 * i, ln, "msg"))
    if meta:
        out.append(text(tx, y + 48 + 20 * len(lines) + 2, meta,
                        "timer" if fresh and b["depth"] else "mono"))
    if plus:
        if b["avatar"] == "round":
            out += [circle(x + w - 26, y + 26, 16, "none", b["border"])]
        else:
            out += [rect(x + w - 42, y + 10, 32, 32, "none", b["border"], 0, sw=b["bw"])]
        out.append(text(x + w - 26, y + 32, "+", "disp", f'fill:{b["accent_text"]}', 16, "middle"))
    if fade:
        out = [f'<g opacity="0.35">'] + ["  " + o for o in out] + ["</g>"]
    return out, h

def field(b, y, placeholder, w=342, x=16):
    return [rect(x, y, w, 44, b["panel2"], b["border"], b["radius"] or 0, sw=b["bw"]),
            text(x + 16, y + 28, placeholder, "small", f'fill:{b["muted2"]}')]

def button(b, y, label, w=342, x=16, filled=True):
    out = []
    if b["depth"]:
        out.append(rect(x + b["depth"], y + b["depth"], w, 44, b["border"], None, b["radius"]))
    if filled:
        out += [rect(x, y, w, 44, b["accent"], None, b["radius"]),
                text(x + w / 2, y + 28, label, "small",
                     f'fill:{b["ink"]};font-weight:700', anchor="middle")]
    else:
        out += [rect(x, y, w, 44, b["panel"], b["border"], b["radius"], sw=b["bw"]),
                text(x + w / 2, y + 28, label, "small", anchor="middle")]
    return out

def slider(b, y, frac, w=326, x=24):
    r = 2 if b["radius"] else 0
    return [rect(x, y + 8, w, 4, b["panel2"], None, r),
            rect(x, y + 8, int(w * frac), 4, b["accent"], None, r),
            circle(x + int(w * frac), y + 10, 11, b["accent"]) if b["avatar"] == "round"
            else rect(x + int(w * frac) - 9, y + 1, 18, 18, b["accent"], None, 0)]

def bubble(b, y, side, lines, meta, w=300):
    """The one place the two products are furthest apart. sosed clips a single
    corner to 5px — a tail made by subtraction. neighbro squares everything and
    mirrors the shadow: it falls to the right of what came in and to the left of
    what went out, so the shadow always points away from whoever spoke."""
    x = 16 if side == "in" else 374 - 16 - w
    h = 26 + 20 * len(lines) + (18 if meta else 0)
    fill = b["panel2"] if side == "in" else b["accent"]
    ink = "" if side == "in" else f'fill:{b["ink"]}'
    out = []
    if b["depth"]:
        off = b["depth"] - 1
        sx = x + off if side == "in" else x - off
        out.append(rect(sx, y + off, w, h, b["border"], None, 0))
    if b["tail"]:
        r, tail = b["radius"], b["tail"]
        # Every corner is r except one, which tightens to `tail` — the bottom
        # corner on the speaker's side, exactly as the landing does it with
        # border-bottom-*-radius. All four corners are drawn: leaving the last one
        # to `z` closed it with a straight line, and the missing arc read as a cut
        # in the wrong corner.
        if side == "out":
            d = (f'M{x + r} {y} h{w - 2 * r} a{r} {r} 0 0 1 {r} {r} '
                 f'v{h - r - tail} a{tail} {tail} 0 0 1 -{tail} {tail} '
                 f'h-{w - r - tail} a{r} {r} 0 0 1 -{r} -{r} '
                 f'v-{h - 2 * r} a{r} {r} 0 0 1 {r} -{r} z')
        else:
            d = (f'M{x + r} {y} h{w - 2 * r} a{r} {r} 0 0 1 {r} {r} '
                 f'v{h - 2 * r} a{r} {r} 0 0 1 -{r} {r} '
                 f'h-{w - r - tail} a{tail} {tail} 0 0 1 -{tail} -{tail} '
                 f'v-{h - r - tail} a{r} {r} 0 0 1 {r} -{r} z')
        stroke = f' stroke="{b["border"]}" stroke-width="{b["bw"]}"' if side == "in" else ""
        out.append(f'<path d="{d}" fill="{fill}"{stroke}/>')
    else:
        out.append(rect(x, y, w, h, fill, b["border"] if side == "in" else b["accent"],
                        b["radius"], sw=b["bw"]))
    for i, ln in enumerate(lines):
        out.append(text(x + 16, y + 26 + 20 * i, ln, "msg", ink))
    if meta:
        out.append(text(x + 16, y + 26 + 20 * len(lines) + 2, meta, "mono", ink))
    return out, h

def matched_note(b, y, quote):
    """sosed alone: the message the two of them both liked, quoted inside a dashed
    accent frame at the head of the chat. Screen 6 asks for exactly this — "show
    which message matched" — and nothing else on the page is dashed, so it reads
    as a footnote rather than as a control."""
    h = 78
    return [f'<rect x="16" y="{y}" width="342" height="{h}" rx="{b["radius"]}" fill="none" '
            f'stroke="{b["accent"]}" stroke-width="{b["bw"]}" stroke-dasharray="6 5"/>',
            text(36, y + 26, L(b, "ПОЧЕМУ СОВПАЛО", "WHY YOU MATCHED"), "brow",
                 f'fill:{b["accent_text"]}'),
            text(36, y + 54, quote, "msg")], h

def sheet(b, y, title, sub, children):
    """A modal sheet, drawn over whatever it covers rather than over nothing —
    and at the height it was asked for. Without the translate it was drawn from
    the top of the screen and sat on the header; the overlap measurement caught
    it on two sheets before anyone looked."""
    h = 828 - y
    out = [f'<path d="M0 40 A35 35 0 0 1 35 5 L339 5 A35 35 0 0 1 374 40 L374 {h} L0 {h} Z" '
           f'fill="{b["panel"]}" stroke="{b["border"]}" stroke-width="1"/>',
           rect(163, 18, 48, 4, b["border"], None, 2),
           text(24, 58, title, "disp", size=18)]
    if sub:
        out.append(text(24, 82, sub, "mono"))
    inner = "\n".join("  " + s for s in out + children)
    return [f'<g transform="translate(0,{y})">\n{inner}\n</g>']

def nav(b, on="feed"):
    """neighbro carries a bar of four; sosed carries one round button and nothing
    else, because its landing puts the whole product behind a single 'say it'."""
    if b["key"] == "sosed":
        return [circle(316, 756, 30, b["accent"]),
                text(316, 766, "+", "disp", f'fill:{b["ink"]}', 26, "middle"),
                text(316, 806, L(b, "сказать", "say"), "mono", anchor="middle")]
    items = [("feed", L(b, "Лента", "Feed")), ("chats", L(b, "Беседы", "Chats")),
             ("say", L(b, "Сказать", "Say")), ("me", L(b, "Я", "Me"))]
    out = [line(0, 742, 374, 742, b["border"])]
    for i, (key, label) in enumerate(items):
        cx = 47 + i * 93
        chosen = key == on
        if key == "say":
            out += [circle(cx, 776, 20, b["accent"]),
                    text(cx, 784, "+", "disp", f'fill:{b["ink"]}', 20, "middle")]
        else:
            out += [rect(cx - 11, 766, 22, 3, b["accent"] if chosen else b["muted2"], None, 1),
                    rect(cx - 11, 773, 15, 3, b["accent"] if chosen else b["muted2"], None, 1)]
        out.append(text(cx, 806, label, "mono",
                        f'fill:{b["accent_text"]}' if chosen else "", anchor="middle"))
    return out

def phone(b, x, y, label, body, dim_backdrop=None):
    """A phone at its true geometry: 390 by 844, screen inset by 8, radius 46/35."""
    inner = [rect(0, 0, 374, 828, b["bg"], None, b["phone_r"][1])]
    if dim_backdrop:
        inner += ['<g opacity="0.45">'] + ["  " + d for d in dim_backdrop] + ["</g>"]
        inner.append(rect(0, 0, 374, 828, b["bg"], None, b["phone_r"][1], 0.62))
    inner += body
    frame, screen = b["phone_r"]
    # The screen clips, the way a screen does. Without it a card swiped off the
    # edge was drawn over the sheet's own background, outside the phone entirely —
    # which the column measurement caught and the eye would have read as a bug in
    # the drawing rather than as the gesture it is.
    phone.n = getattr(phone, "n", 0) + 1
    cid = f"screen{phone.n}"
    return "\n".join([
        f'  <g transform="translate({x},{y})">',
        f'    {text(0, 0, label, "brow")}',
        f'    {rect(0, 14, 390, 844, b["panel"], b["border"], frame, sw=b["bw"])}',
        f'    <clipPath id="{cid}"><rect x="8" y="22" width="374" height="828" rx="{screen}"/></clipPath>',
        f'    <g clip-path="url(#{cid})">',
        g(8, 22, inner),
        "    </g>",
        "  </g>",
    ])

# ───────────────────────────────────────────────────────────────── the sheet ──
# Drawn at ×2. The geometry stays in the product's own units — a phone is 390 by
# 844 here, and every measurement on the sheet is in those units — but width and
# height are doubled against the viewBox, so the browser paints it twice the size.
# A 10px caption arrives at 20px and can be read without leaning in, and nothing
# in the layout had to be re-tuned to get there.
SCALE = 2

def classes(b, prefix=""):
    sel = f".{prefix} " if prefix else ""
    return f'''    {sel}.disp  {{ font-weight: 800; letter-spacing: -0.03em; fill: {b["fg"]}; }}
    {sel}.body  {{ font-size: 13px; font-weight: 500; fill: {b["fg"]}; }}
    {sel}.msg   {{ font-size: 14px; font-weight: 500; fill: {b["fg"]}; }}
    {sel}.small {{ font-size: 11px; font-weight: 500; fill: {b["fg"]}; }}
    {sel}.muted {{ font-size: 12px; font-weight: 500; fill: {b["muted2"]}; }}
    {sel}.mono  {{ font-family: ui-monospace, SF Mono, Menlo, Consolas, monospace;
             font-size: 10px; fill: {b["muted2"]}; }}
    {sel}.brow  {{ font-family: ui-monospace, SF Mono, Menlo, Consolas, monospace;
             font-size: 10px; letter-spacing: 2.2px; fill: {b["brow"]}; font-weight: 600; }}
    {sel}.warn  {{ font-size: 11px; font-weight: 600; fill: {b["warn"]}; }}
    {sel}.timer {{ font-family: ui-monospace, SF Mono, Menlo, Consolas, monospace;
             font-size: 10px; letter-spacing: 1.4px; fill: {b["brow"]}; font-weight: 600; }}'''

def sheet_svg(b, number, name, lede, phones, phones_light, height):
    W = 1440
    light = lit(b)
    parts = []
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W * SCALE}" '
                 f'height="{height * SCALE}" viewBox="0 0 {W} {height}" '
                 f'font-family="Golos Text, system-ui, sans-serif">')
    parts.append(f'  <title>{esc(b["title"])} — {L(b, "экран", "screen")} {number}, {esc(name)}</title>')
    parts.append(f'  <desc>{esc(lede)} Обе темы. Нарисовано по ../../docs/{b["doc"]}; '
                 f'цвета сняты с landing/index.html.</desc>')
    parts.append(f'''  <style>
    @import url("../../landing/fonts.css");
    /* Colour lives in style, never in a fill attribute: a class outranks the
       attribute, so a per-element fill="…" is thrown away and the label is
       painted in the class colour on top of its own ground. */
{classes(b)}
    /* The same drawing again, on the light ground. Only the values differ — the
       geometry, the wording and the layout are one thing drawn twice. */
{classes(light, "on-light")}
  </style>''')
    parts.append(f'  {rect(0, 0, W, height, b["bg"])}')

    parts.append(g(48, 40, [
        rect(0, 0, 1344, 104, b["accent"], None, 16),
        text(28, 46, f'{L(b, "Экран", "Screen")} {number}. {name}', "disp", f'fill:{b["ink"]}', 30),
        text(28, 74, lede, "body", f'fill:{b["ink"]}'),
        text(1316, 46, f'design/interface/{number:02d}-{b["slug"]}.svg', "mono",
             f'fill:{b["ink"]}', anchor="end"),
        text(1316, 74, f'×2 · обе темы · ../../docs/{b["doc"]}', "mono", f'fill:{b["ink"]}', anchor="end"),
    ]))

    row = 184
    for theme, face, cls, shots in (
            (L(b, "ТЁМНАЯ · ПО УМОЛЧАНИЮ", "DARK · THE DEFAULT"), b, "", phones),
            (L(b, "СВЕТЛАЯ", "LIGHT"), light, "on-light", phones_light)):
        parts.append(g(48, row, [
            text(0, 16, theme, "disp", size=19),
            line(0, 26, 1344, 26, face["border"] if cls else b["border"]),
        ]))
        if cls:
            parts.append(f'  <rect x="0" y="{row + 44}" width="{W}" height="946" fill="{face["bg"]}"/>')
        inner = []
        for i, (label, body, backdrop) in enumerate(shots):
            inner.append(phone(face, 48 + i * 477, row + 72, label, body, backdrop))
        block = "\n".join(inner)
        parts.append(f'  <g class="{cls}">\n{block}\n  </g>' if cls else block)
        row += 1010

    # No panel of open questions here any more. What a screen leaves undecided is
    # a question about the product, and it belongs in ../../docs/ where it is
    # maintained — printed on the drawing it turned every sheet into an argument
    # with itself. A drawing carries the drawing.
    foot = row + 24
    parts.append(g(48, foot, [
        rect(0, -8, 1344, 36, b["panel2"], b["border"], b["radius"], sw=b["bw"]),
        text(24, 16, f'Цвета — landing/index.html, шрифт — landing/fonts.css. '
                     f'Брат: {"neighbro.place" if b["key"] == "sosed" else "sosed.place"}'
                     f'/design/interface/', "mono"),
    ]))
    parts.append("</svg>")
    return "\n".join(p for p in parts if p)

# ════════════════════════════════════════════════════════════════ the screens ══
# One definition per screen, rendered twice. Content comes from ../../docs/; the
# "Открытые вопросы" of each document become the panel at the bottom, so a
# drawing never quietly settles something the description left open.

def s01(b):
    icons = []
    for i, (cx, cy, r) in enumerate([(90, 150, 22), (180, 110, 16), (270, 160, 20),
                                     (130, 220, 14), (240, 235, 18)]):
        icons += [circle(cx, cy, r, b["panel2"], b["border"]),
                  circle(cx, cy, r - 8, b["accent"], None, 0.5 if i % 2 else 0.8)]
    body = [
        text(187, 30, "9:41", "mono", anchor="middle"),
        *icons,
        text(187, 300, L(b, "рядом сейчас", "nearby right now"), "brow", anchor="middle"),
        text(187, 340, "128", "disp", size=34, anchor="middle"),
        text(187, 366, L(b, "сообщений за час · 41", "messages in the last hour · 41"),
             "mono", anchor="middle"),
        text(187, 440, L(b, "ГОД РОЖДЕНИЯ", "YEAR OF BIRTH"), "brow", anchor="middle"),
        *[text(187, 480 + i * 34, y, "muted" if i != 1 else "disp",
               size=None if i != 1 else 30, anchor="middle")
          for i, y in enumerate(["1996", "1997", "1998"])],
        line(90, 496, 284, 496, b["border"]),
        line(90, 560, 284, 560, b["border"]),
        circle(187, 720, 32, b["accent"]),
        text(187, 730, "→", "disp", f'fill:{b["ink"]}', 24, "middle"),
    ]
    return ("загрузка и год рождения" if b["key"] == "sosed" else "loading, and a year of birth",
            L(b, "Загрузочная анимация и первый шаг регистрации на одном экране. Живые цифры площадки — не украшение, а то, что видно, пока идёт загрузка.",
              "The loading animation and the first step of signing up on one screen. The live numbers are not decoration — they are what there is to look at while it loads."),
            [(L(b, "ЗАСТАВКА", "SPLASH"), body, None)],
            [L(b, "Два вопроса описание оставляет открытыми.",
               "Two questions the description leaves open."),
             L(b, "Набор иконок для анимации не определён — здесь кружки как место, которое они займут.",
               "The icon set for the animation is undecided — the circles here are the space it will take."),
             L(b, "Иконка кнопки «вперёд» не определена. Нарисована стрелка как самый нейтральный знак.",
               "The forward button's icon is undecided. An arrow is drawn as the most neutral mark there is.")])

def s02(b):
    body = [
        text(187, 30, "9:41", "mono", anchor="middle"),
        text(24, 120, L(b, "КАК ВАС ЗВАТЬ", "WHAT TO CALL YOU"), "brow"),
        text(24, 168, L(b, "Имя", "Your name"), "disp", size=28),
        text(24, 200, L(b, "Необязательно. Можно оставить пустым.",
                        "Optional. You may leave it empty."), "muted"),
        *field(b, 240, L(b, "как вас зовут…", "your name…"), 342, 16),
        circle(187, 720, 32, b["accent"]),
        text(187, 730, "→", "disp", f'fill:{b["ink"]}', 24, "middle"),
    ]
    return (L(b, "имя", "the name"),
            L(b, "Второй и последний шаг регистрации. Поле необязательное — кнопка работает и с пустым.",
              "The second and last step. The field is optional, and the button works with it empty."),
            [(L(b, "ИМЯ", "NAME"), body, None)],
            [L(b, "Два вопроса описание оставляет открытыми.",
               "Two questions the description leaves open."),
             L(b, "Плейсхолдер поля не определён — здесь стоит пример.",
               "The field's placeholder is undecided — an example stands here."),
             L(b, "Ограничение длины имени не определено.",
               "The name's length limit is undecided.")])

def s04(b):
    body = [
        text(187, 30, "9:41", "mono", anchor="middle"),
        *header(b, L(b, "сказать", "say it"), L(b, "видно тем, кто рядом", "seen by whoever is near"), False),
        rect(16, 130, 342, 128, b["panel2"], b["border"], 16),
        text(32, 160, L(b, "Во дворе поставили стол для", "Someone put a ping-pong table"), "msg"),
        text(32, 180, L(b, "пинг-понга. Ракетки у консьержа.", "in the yard. Bats are with the porter."), "msg"),
        text(32, 244, "64 / 128", "mono"),
        text(24, 296, L(b, "СКОЛЬКО ВАС", "HOW MANY OF YOU"), "brow"),
        *[(rect(24 + i * 58, 312, 46, 38, b["accent"] if i == 0 else b["panel2"],
                None if i == 0 else b["border"], 12)) for i in range(5)],
        *[text(47 + i * 58, 337, s, "small",
               f'fill:{b["ink"]};font-weight:700' if i == 0 else "", anchor="middle")
          for i, s in enumerate(["1", "2", "3", "4", "5+"])],
        text(24, 400, L(b, "РАЗМЫТИЕ МЕСТА", "BLUR THE PLACE"), "brow"),
        text(24, 428, L(b, "около 300 м", "about 300 m"), "msg"),
        *slider(b, 446, 0.34),
        *button(b, 700, L(b, "Отправить", "Send")),
    ]
    return (L(b, "публикация сообщения", "writing a message"),
            L(b, "128 символов, сколько вас, и радиус размытия места. Картинок нет — они бывают только у продвигаемого сообщения.",
              "128 characters, how many of you, and how much to blur the place. No pictures — those belong to promoted messages only."),
            [(L(b, "НАПИСАТЬ", "COMPOSE"), body, None)],
            [L(b, "Три вопроса описание оставляет открытыми.",
               "Three questions the description leaves open."),
             L(b, "Осталось ли отдельное поле города и страны, или его заменил слайдер размытия.",
               "Whether a separate city and country field survives, or the blur slider replaced it."),
             L(b, "Умолчания и границы слайдера размытия не определены. 300 м на чертеже — пример.",
               "The blur slider's default and bounds are undecided. The 300 m here is an example."),
             L(b, "Вид кнопки отправки не определён — здесь она текстовая.",
               "The send button's form is undecided — here it carries a word.")])

def s03b(b):
    """The feed again, in each product's own shape: this is where the two stop
    being one drawing in two palettes."""
    lines = L(b, [["Кофейня на углу поставила", "пианино. Играет кто хочет."],
                  ["Кто-то потерял синий шарф"],
                  ["Кто-нибудь ещё слышал этот", "оркестр во дворе в семь утра?"]],
              [["The corner café put a piano", "outside. Anyone may play."],
               ["Blue scarf left by the canal"],
               ["Anyone else hear that brass", "band in the yard at seven?"]])
    body = [text(187, 30, "9:41", "mono", anchor="middle"),
            *header(b, L(b, "рядом", "34 nearby"), f'{b["here"]} · 1.2 {L(b, "км", "km")}')]
    y = 130 if b["key"] == "sosed" else 122
    for i, ls in enumerate(lines):
        part, h = card(b, y, f'{b["places"][i]} · {27 + i * 2}',
                       ls, L(b, "14:32", "14:32 · 2H 40M LEFT") if i == 2 else "08:12",
                       plus=True, fresh=(i == 2))
        body += part
        y += h + 16
    if b["depth"]:
        # the plate that is on its way out, shown going rather than described
        part, _ = card(b, y, f'{b["places"][3]} · 22',
                       L(b, ["уже почти растаяло"], ["almost gone now"]), "04:12",
                       plus=False, fade=True)
        body += part
    body += nav(b)
    if b["key"] == "sosed":
        body += [text(16, 700, L(b, "новое отчёркнуто слева — тихо, без движения", ""), "mono")]
    else:
        body += [text(16, 700, L(b, "", "what just arrived throws a hard shadow"), "mono")]
    viewer = [
        text(187, 30, "9:41", "mono", anchor="middle"),
        text(24, 66, L(b, "3 / 34", "3 / 34"), "mono"),
        text(350, 68, "✕", "disp", f'fill:{b["muted2"]}', 16, "end"),
        rect(24, 150, 326, 320, b["panel"], b["border"], 16),
        text(48, 190, f'{b["places"][2]} · 24', "brow"),
        *[text(48, 240 + i * 26, s, "msg", size=17) for i, s in enumerate(
            L(b, ["Кто со мной за утренним", "эспрессо перед работой?"],
              ["Anyone up for a morning", "espresso before work?"]))],
        text(48, 330, L(b, "нас двое · 400 м", "two of us · 400 m"), "mono"),
        text(48, 430, L(b, "СВЕЖЕЕ", "FRESH · 4H 02M"), "timer"),
        text(187, 520, L(b, "влево — мимо · вправо — я с вами",
                         "swipe left to skip · swipe right to join"), "mono", anchor="middle"),
        *button(b, 700, L(b, "Мимо", "Skip"), 150, 24, filled=False),
        *button(b, 700, L(b, "Я с вами", "I'm in"), 150, 200),
    ]
    phones = [(L(b, "ЛЕНТА", "FEED"), body, None)]
    if b["key"] == "neighbro":
        phones.append((L(b, "ПРОСМОТРЩИК", "ONE AT A TIME"), viewer, None))
    return (L(b, "лента: своя форма", "the feed, in its own shape"),
            L(b, "Один столбец, круглая кнопка поверх него и черта у нового. Ни нижней панели, ни режима по одной карточке — у соседа их нет.",
              "A bar of four, a hard accent shadow on what just arrived, and a one-at-a-time mode with skip and join — taken from this product's own prototype."),
            phones,
            [L(b, "Это дополнение к экрану 3, а не замена.",
               "This is an addition to screen 3, not a replacement."),
             L(b, "Здесь показано, чем форма соседа отличается от формы брата: столбец, круглая кнопка, отчёркнутое новое.",
               "It shows what this product's shape is: the bar, the shadow on the fresh card, the viewer."),
             L(b, "Режим по одной карточке и вкладки «беседы/запросы» есть только у брата — они из его прототипа.",
               "The viewer and the chats/requests tabs come from prototype/neighbro-app-proto.html.")])

def s05(b):
    lines1 = L(b, ["Кто-нибудь ещё слышал этот", "оркестр во дворе в семь утра?"],
               ["Anyone else hear that brass", "band in the yard at seven?"])
    c1, h1 = card(b, 150, f'{b["places"][1]} · 29', lines1, "14:32", plus=False)
    body = [
        text(187, 30, "9:41", "mono", anchor="middle"),
        *header(b, L(b, "рядом", "nearby"), f'{b["here"]} · 1.2 {L(b, "км", "km")}'),
        *c1,
        circle(316, 176, 16, "none", b["border"]),
        f'<path d="M310 176 a5 5 0 0 1 6 -3 a5 5 0 0 1 6 3 q0 6 -6 9 q-6 -3 -6 -9 z" fill="{b["accent"]}"/>',
        text(316, 236, "···", "disp", f'fill:{b["muted2"]}', 16, "middle"),
    ]
    menu = [
        text(24, 126, L(b, "Пожаловаться", "Report"), "msg"),
        line(24, 174, 350, 174, b["border"]),
        text(24, 210, L(b, "Заблокировать", "Block"), "msg"),
        line(24, 276, 350, 276, b["border"]),
        text(24, 312, L(b, "Отмена", "Cancel"), "msg", f'fill:{b["muted2"]}'),
    ]
    backdrop = [text(187, 30, "9:41", "mono", anchor="middle"),
                *header(b, L(b, "рядом", "nearby"), f'{b["here"]} · 1.2 {L(b, "км", "km")}'),
                *card(b, 150, f'{b["places"][1]} · 29', lines1, "14:32", plus=False)[0]]
    return (L(b, "действия с сообщением", "what you can do to a message"),
            L(b, "Лайк виден сразу. Жалоба и блокировка спрятаны — их не предлагают, к ним приходят.",
              "The like is in the open. Report and block are hidden — they are not offered, they are reached for."),
            [(L(b, "КАРТОЧКА", "THE CARD"), body, None),
             (L(b, "СКРЫТОЕ МЕНЮ", "THE HIDDEN MENU"),
              sheet(b, 480, L(b, "Сообщение", "This message"), None, menu), backdrop)],
            [L(b, "Три вопроса описание оставляет открытыми.",
               "Three questions the description leaves open."),
             L(b, "Прячет ли жалоба сообщение лично для пожаловавшегося, как это делает блокировка.",
               "Whether a report also hides the message for the person who reported it, the way blocking does."),
             L(b, "Способ вызова скрытого меню не определён: долгое нажатие, кнопка «···» или свайп.",
               "How the hidden menu is summoned is undecided: a long press, a «···» button or a swipe."),
             L(b, "Насколько жалоба и блокировка снижают квоту — не определено.",
               "How far a report or a block lowers the quota is undecided.")])

def s06(b):
    liked = L(b, ["Кто-нибудь ещё слышал этот", "оркестр во дворе в семь утра?"],
              ["Anyone else hear that brass", "band in the yard at seven?"])
    match = [
        text(187, 30, "9:41", "mono", anchor="middle"),
        text(187, 200, L(b, "ВЗАИМНО", "MUTUAL"), "brow", anchor="middle"),
        text(187, 260, L(b, "Совпало", "It matched"), "disp", size=34, anchor="middle"),
        text(187, 300, L(b, "на этом сообщении", "on this message"), "muted", anchor="middle"),
        *card(b, 340, f'{b["places"][1]} · 29', liked, "14:32", plus=False)[0],
        text(187, 500, L(b, "чат уже открыт", "the chat is already open"), "mono", anchor="middle"),
        *button(b, 700, L(b, "Написать", "Say something")),
    ]
    chat = [
        text(187, 30, "9:41", "mono", anchor="middle"),
        *header(b, f'{b["places"][1]} · 29', L(b, "приватно", "private"), False),
        *bubble(b, 140, "in", L(b, ["Слышал. Думал, это у меня в голове."],
                                ["Heard it. Thought it was in my head."]), "14:33")[0],
        *bubble(b, 216, "out", L(b, ["Значит, нас двое."], ["So there are two of us."]),
                L(b, "14:35 · ДОСТАВЛЕНО", "14:35 · DELIVERED"), 260)[0],
        rect(16, 300, 342, 70, b["panel2"], b["border"], 16),
        f'<path d="M32 322 a5 5 0 0 1 6 -3 a5 5 0 0 1 6 3 q0 6 -6 9 q-6 -3 -6 -9 z" fill="{b["accent"]}"/>',
        text(56, 328, L(b, "лайкнули ещё одно ваше сообщение",
                        "another of your messages was liked"), "small"),
        text(32, 354, L(b, "«Продаю велосипед, стоял год на балконе»",
                        "“Selling a bike, a year on the balcony”"), "mono"),
        *field(b, 700, L(b, "написать…", "write…"), 278),
        *(([circle(332, 722, 22, b["accent"])]) if b["avatar"] == "round" else
          [rect(310, 700, 44, 44, b["accent"], None, 0)]),
        text(332, 729, "↑", "disp", f'fill:{b["ink"]}', 20, "middle"),
    ]
    return (L(b, "мэтч и чат", "the match, and the chat"),
            L(b, "Взаимный лайк открывает чат и показывает, на чём именно совпало. Следующий лайк не заводит второй чат.",
              "A mutual like opens the chat and shows what matched. The next like does not start a second one."),
            [(L(b, "МЭТЧ", "MATCH"), match, None),
             (L(b, "ЛАЙК ПОСЛЕ МЭТЧА", "A LIKE AFTER THE MATCH"), chat, None)],
            [L(b, "Два вопроса описание оставляет открытыми.",
               "Two questions the description leaves open."),
             L(b, "Вид анимации мэтча не определён — здесь показано только её содержание.",
               "The match animation's look is undecided — only what it says is drawn here."),
             L(b, "Формат уведомления о лайке внутри чата не определён: текст, карточка или иконка.",
               "The form of the in-chat like notice is undecided: a line, a card or an icon.")])

def s07(b):
    rows = [
        (f'{b["places"][1]} · 29', L(b, "Значит, нас двое.", "So there are two of us."), "14:35", 0),
        (f'{b["places"][2]} · 24', L(b, "Семь подходит. У ворот?", "Seven works. At the gate?"), "12:41", 2),
        (f'{b["places"][0]} · 31', L(b, "Нашёлся, спасибо.", "Found it, thank you."), "11:22", 0),
        (f'{b["places"][3]} · 33', L(b, "Велосипед ещё свободен.", "The bike is still available."),
         L(b, "Пн", "Mon"), 0),
    ]
    body = [text(187, 30, "9:41", "mono", anchor="middle"),
            *header(b, L(b, "беседы", "chats"), L(b, "по одной на мэтч", "one per match"), False)]
    y = 130
    for i, (who, last, when, unread) in enumerate(rows):
        body += [rect(16, y, 342, 72, b["accent"] if i == 0 else b["panel2"],
                      None if i == 0 else b["border"], 16),
                 text(32, y + 28, who, "small",
                      f'fill:{b["ink"]};font-weight:700' if i == 0 else "font-weight:700"),
                 text(32, y + 50, last, "mono", f'fill:{b["ink"]}' if i == 0 else ""),
                 text(342, y + 28, when, "mono", f'fill:{b["ink"]}' if i == 0 else "", anchor="end")]
        if unread:
            body += [circle(334, y + 46, 10, b["accent"]),
                     text(334, y + 50, str(unread), "mono", f'fill:{b["ink"]}', anchor="middle")]
        y += 84
    return (L(b, "список бесед", "the list of chats"),
            L(b, "Появляется, когда мэтчей больше одного. Пока он один — сразу чат.",
              "It appears once there is more than one match. While there is one, there is just the chat."),
            [(L(b, "БЕСЕДЫ", "CHATS"), body, None)],
            [L(b, "Описание не оставило здесь открытых вопросов.",
               "The description leaves nothing open here."),
             L(b, "Список живёт, пока живы сами чаты — время жизни описано на экране 8.",
               "The list lives as long as the chats do — their lifetime is on screen 8.")])

def s08(b):
    body = [text(187, 30, "9:41", "mono", anchor="middle"),
            *header(b, f'{b["places"][1]} · 29', L(b, "приватно", "private"), False)]
    y = 130
    convo = [("in", L(b, ["Слышал. Думал, это у меня в голове."],
                      ["Heard it. Thought it was in my head."]), "14:33", 300),
             ("out", L(b, ["Значит, нас двое."], ["So there are two of us."]),
              L(b, "14:35 · ДОСТАВЛЕНО", "14:35 · DELIVERED"), 240),
             ("in", L(b, ["Каждое утро под одним окном."], ["Same window every morning."]), "14:36", 280),
             ("out", L(b, ["Завтра проверим вместе?"], ["Shall we check together tomorrow?"]),
              L(b, "14:38 · ДОСТАВЛЕНО", "14:38 · DELIVERED"), 260)]
    for side, lines, meta, w in convo:
        part, h = bubble(b, y, side, lines, meta, w)
        body += part
        y += h + 12
    body += [
        *field(b, 700, L(b, "написать…", "write…"), 278),
        *(([circle(332, 722, 22, b["accent"])]) if b["avatar"] == "round" else
          [rect(310, 700, 44, 44, b["accent"], None, 0)]),
        text(332, 729, "↑", "disp", f'fill:{b["ink"]}', 20, "middle"),
    ]
    return (L(b, "беседа", "the chat"),
            L(b, "Приватная переписка двоих. История есть только у них двоих и больше нигде.",
              "Two people's private thread. The history exists for the two of them and nowhere else."),
            [(L(b, "БЕСЕДА", "CHAT"), body, None)],
            [L(b, "Описание не оставило здесь открытых вопросов.",
               "The description leaves nothing open here."),
             L(b, "Хранение названо прямо: IndexedDB на устройстве, шифрование через Web Crypto перед записью.",
               "Storage is named plainly: IndexedDB on the device, encrypted with Web Crypto before it is written."),
             L(b, "«Защищённого» хранилища браузера не существует, и описание это оговаривает.",
               "There is no such thing as a browser's “secure” store, and the description says so.")])

def s09(b):
    body = [text(187, 30, "9:41", "mono", anchor="middle"),
            *header(b, L(b, "мои сообщения", "my messages"),
                    L(b, "квота: 3 из 5", "quota: 3 of 5"), False)]
    y = 130
    mine = [(L(b, ["Во дворе поставили стол", "для пинг-понга."],
               ["Someone put a ping-pong", "table in the yard."]), "3:41"),
            (L(b, ["Кто-нибудь ещё слышал", "оркестр в семь утра?"],
               ["Anyone else hear that", "band at seven?"]), "1:07"),
            (L(b, ["Ищу компанию в бассейн."], ["Looking for a pool buddy."]), "0:12")]
    for lines, left in mine:
        h = 46 + 20 * len(lines) + 18
        body += [rect(16, y, 342, h, b["panel"], b["border"], 16)]
        for i, ln in enumerate(lines):
            body.append(text(32, y + 30 + 20 * i, ln, "msg"))
        body += [text(32, y + 30 + 20 * len(lines) + 4, L(b, f"исчезнет через {left}",
                                                          f"gone in {left}"), "mono"),
                 (circle(332, y + 26, 15, "none", b["border"]) if b["avatar"] == "round"
                  else rect(317, y + 11, 30, 30, "none", b["border"], 0, sw=b["bw"])),
                 text(332, y + 31, "×", "disp", f'fill:{b["muted2"]}', 15, "middle")]
        y += h + 12
    body += [
        rect(16, y + 20, 342, 78, b["panel2"], b["border"], 16),
        text(32, y + 48, L(b, "КВОТА", "QUOTA"), "brow"),
        *[rect(32 + i * 62, y + 62, 46, 8, b["accent"] if i < 3 else b["panel"],
               None if i < 3 else b["border"], 4) for i in range(5)],
        text(32, y + 92, L(b, "три из пяти заняты", "three of five in use"), "mono"),
    ]
    return (L(b, "мои сообщения", "my messages"),
            L(b, "Свои активные сообщения, у каждого таймер и кнопка удаления, и остаток квоты.",
              "Your own live messages, each with its timer and a way to delete it, and what is left of the quota."),
            [(L(b, "МОИ СООБЩЕНИЯ", "MY MESSAGES"), body, None)],
            [L(b, "Описание не оставило здесь открытых вопросов.",
               "The description leaves nothing open here."),
             L(b, "Восстановление квоты со временем описано как открытое на экране 13, а не здесь.",
               "Whether the quota refills with time is left open on screen 13, not here.")])

def s10(b):
    body = [
        text(187, 30, "9:41", "mono", anchor="middle"),
        *header(b, L(b, "настройки", "settings"), L(b, "применяются сразу", "applied at once"), False),
        text(24, 150, L(b, "ТЕМА", "THEME"), "brow"),
        rect(16, 166, 342, 48, b["panel2"], b["border"], 14),
        rect(20, 170, 167, 40, b["accent"], None, 11),
        text(103, 195, L(b, "тёмная", "dark"), "small", f'fill:{b["ink"]};font-weight:700', anchor="middle"),
        text(271, 195, L(b, "светлая", "light"), "small", anchor="middle"),
        text(24, 260, L(b, "КОНТРАСТНОСТЬ", "CONTRAST"), "brow"),
        *slider(b, 278, 0.62),
        text(24, 340, L(b, "ССЫЛКА НА СЕБЯ", "A LINK TO YOU"), "brow"),
        *field(b, 356, "https://", 342, 16),
        text(24, 424, L(b, "одно поле, без выбора площадки", "one field, no platform to pick"), "mono"),
        text(24, 442, L(b, "ею можно поделиться в чате", "it can be shared inside a chat"), "mono"),
        line(16, 490, 358, 490, b["border"]),
        text(24, 528, L(b, "Сообщения с сексуальным подтекстом",
                        "Messages with a sexual undertone"), "msg"),
        text(24, 552, L(b, "выключено — включается на отдельном экране",
                        "off — turned on from a screen of its own"), "mono"),
        text(342, 534, "→", "disp", f'fill:{b["accent_text"]}', 18, "end"),
    ]
    return (L(b, "настройки", "settings"),
            L(b, "Тема, контрастность, одна ссылка на себя — и переход на согласие, а не переключатель.",
              "Theme, contrast, one link to you — and a way through to a consent screen, not a switch."),
            [(L(b, "НАСТРОЙКИ", "SETTINGS"), body, None)],
            [L(b, "Описание не оставило здесь открытых вопросов.",
               "The description leaves nothing open here."),
             L(b, "Площадки не перечисляются: ни Telegram, ни Instagram отдельными пунктами — одно поле произвольной ссылки.",
               "No platforms are listed: no Telegram, no Instagram as separate rows — one field for any link.")])

def s11(b):
    body = [
        text(187, 30, "9:41", "mono", anchor="middle"),
        *header(b, L(b, "согласие", "consent"), L(b, "экран 11", "screen 11"), False),
        rect(16, 130, 342, 250, b["panel2"], b["border"], 16),
        text(32, 158, L(b, "СОГЛАШЕНИЕ", "THE AGREEMENT"), "brow"),
        *[text(32, 186 + i * 20, s, "mono") for i, s in enumerate(L(b, [
            "Включая эту настройку, вы подтверждаете,",
            "что вам есть 18 лет и что вы согласны",
            "видеть сообщения с сексуальным подтекстом.",
            "",
            "Такие сообщения появляются в ленте наравне",
            "с остальными. Выключить можно в любой момент.",
            "",
            "Email сохраняется как есть, без письма",
            "с подтверждением.",
        ], [
            "By turning this on you confirm that you are",
            "eighteen or older and that you agree to see",
            "messages with a sexual undertone.",
            "",
            "They then appear in the feed like any other.",
            "You may turn this off at any time.",
            "",
            "The email is stored as given; no confirmation",
            "letter is sent.",
        ]))],
        rect(16, 404, 24, 24, b["panel2"], b["border"], 6),
        f'<path d="M22 416 l4 5 l8 -10" fill="none" stroke="{b["accent"]}" stroke-width="2" stroke-linecap="round"/>',
        text(52, 421, L(b, "Я прочитал и принимаю", "I have read and accept"), "small"),
        text(24, 470, "EMAIL", "brow"),
        *field(b, 486, "you@example.com", 342, 16),
        *button(b, 700, L(b, "Сохранить", "Save")),
    ]
    return (L(b, "согласие на чувствительное", "consenting to the sensitive"),
            L(b, "Открывается из настроек по своей воле. Без принятого соглашения и email такие сообщения не видны вовсе.",
              "Reached from settings on purpose. Without the agreement and an email those messages are not there at all."),
            [(L(b, "СОГЛАСИЕ", "CONSENT"), body, None)],
            [L(b, "Описание не оставило здесь открытых вопросов.",
               "The description leaves nothing open here."),
             L(b, "Email не проверяется письмом — это записано в описании и нарисовано как есть.",
               "The email is not verified by letter — the description says so and the drawing says it too."),
             L(b, "Текст соглашения на чертеже — рыба; настоящий лежит в legal/.",
               "The agreement's words here stand in for the real ones, which live in legal/.")])

def s12(b):
    menu = [
        text(24, 126, L(b, "Поделиться ссылкой", "Share my link"), "msg"),
        text(24, 150, L(b, "той, что в настройках — разово, в эту беседу",
                        "the one from settings — once, into this chat"), "mono"),
        line(24, 174, 350, 174, b["border"]),
        text(24, 210, L(b, "Пожаловаться", "Report"), "msg"),
        line(24, 234, 350, 234, b["border"]),
        text(24, 270, L(b, "Заблокировать", "Block"), "msg"),
        line(24, 294, 350, 294, b["border"]),
        text(24, 330, L(b, "Отмена", "Cancel"), "msg", f'fill:{b["muted2"]}'),
    ]
    backdrop = [text(187, 30, "9:41", "mono", anchor="middle"),
                *header(b, f'{b["places"][1]} · 29', L(b, "приватно", "private"), False),
                *bubble(b, 140, "in", L(b, ["Скину, где это было."], ["I will send you where."]), "14:40")[0]]
    warn = [
        text(187, 30, "9:41", "mono", anchor="middle"),
        rect(0, 0, 374, 828, b["bg"], None, 35),
        rect(28, 300, 318, 228, b["panel"], b["border"], 16),
        text(48, 340, L(b, "ВНЕШНЯЯ ССЫЛКА", "AN OUTSIDE LINK"), "brow"),
        text(48, 376, L(b, "Вы уходите с sosed.place", "You are leaving neighbro.place"), "msg"),
        text(48, 400, L(b, "на сторонний сайт.", "for a site that is not ours."), "msg"),
        text(48, 430, "example.com/…", "mono"),
        *button(b, 452, L(b, "Перейти", "Go"), 140, 48),
        *button(b, 452, L(b, "Отмена", "Cancel"), 140, 206, filled=False),
    ]
    return (L(b, "ссылка в беседе", "a link inside a chat"),
            L(b, "Своей ссылкой делятся разово и вручную. Чужую открывают только после предупреждения.",
              "You share your link once and by hand. Someone else's opens only after a warning."),
            [(L(b, "СКРЫТОЕ МЕНЮ", "THE HIDDEN MENU"),
              sheet(b, 460, L(b, "Беседа", "This chat"), None, menu), backdrop),
             (L(b, "ПРЕДУПРЕЖДЕНИЕ", "THE WARNING"), warn, None)],
            [L(b, "Описание не оставило здесь открытых вопросов.",
               "The description leaves nothing open here."),
             L(b, "Ссылка простая, без привязки к площадке — то же поле, что на экране 10.",
               "The link is plain, tied to no platform — the same field as on screen 10.")])

def s13(b):
    def state(title, lines, action):
        out = [text(187, 30, "9:41", "mono", anchor="middle"),
               *header(b, L(b, "рядом", "nearby"), f'{b["here"]} · 1.2 {L(b, "км", "km")}'),
               rect(16, 240, 342, 40 + 20 * len(lines) + 60, "none", b["muted2"], 16)]
        out[-1] = (f'<rect x="16" y="240" width="342" height="{40 + 20 * len(lines) + 60}" rx="16" '
                   f'fill="none" stroke="{b["muted2"]}" stroke-width="2" stroke-dasharray="6 5"/>')
        out.append(text(187, 278, title, "disp", size=18, anchor="middle"))
        for i, ln in enumerate(lines):
            out.append(text(187, 310 + 20 * i, ln, "muted", anchor="middle"))
        out += button(b, 240 + 40 + 20 * len(lines) + 4, action, 220, 74)
        return out
    quota = state(L(b, "Квота исчерпана", "Quota spent"),
                  L(b, ["Пять сообщений уже в ленте.", "Освободится, когда уйдёт старое."],
                    ["Five messages are already out there.", "Room frees as the old ones go."]),
                  L(b, "Мои сообщения", "My messages"))
    empty = state(L(b, "Рядом тихо", "Quiet nearby"),
                  L(b, ["В этом радиусе сейчас никого.", "Попробуйте расширить круг."],
                    ["Nobody within this radius.", "Try widening the circle."]),
                  L(b, "Расширить радиус", "Widen the radius"))
    geo = state(L(b, "Где вы — неизвестно", "We do not know where you are"),
                L(b, ["Доступ к геопозиции не дан.", "Место можно указать вручную."],
                  ["Location access was not given.", "The place can be set by hand."]),
                L(b, "Указать на карте", "Point at the map"))
    return (L(b, "пустые и пограничные состояния", "empty and edge states"),
            L(b, "Три случая, когда показывать нечего. Каждый называет причину и даёт выход.",
              "Three cases where there is nothing to show. Each names the reason and offers a way out."),
            [(L(b, "КВОТА ИСЧЕРПАНА", "QUOTA SPENT"), quota, None),
             (L(b, "НИКОГО РЯДОМ", "NOBODY NEARBY"), empty, None),
             (L(b, "НЕТ ГЕОПОЗИЦИИ", "NO LOCATION"), geo, None)],
            [L(b, "Три вопроса описание оставляет открытыми.",
               "Three questions the description leaves open."),
             L(b, "Точные тексты и вид каждого состояния не определены — здесь они предложены, а не утверждены.",
               "The exact words and look of each state are undecided — these are proposed, not settled."),
             L(b, "Восстанавливается ли квота со временем или только по мере ухода старых сообщений — не определено.",
               "Whether the quota refills with time or only as old messages go is undecided."),
             L(b, "Поведение при отказе в геопозиции не определено: повторный запрос или только ручной ввод.",
               "What happens after location is refused is undecided: ask again, or hand entry only.")])

def s14(b):
    body = [
        text(187, 30, "9:41", "mono", anchor="middle"),
        *header(b, L(b, "поддержка", "support"), L(b, "доступна всегда", "always reachable"), False),
        text(24, 150, L(b, "ЧТО СЛУЧИЛОСЬ", "WHAT HAPPENED"), "brow"),
        rect(16, 166, 342, 180, b["panel2"], b["border"], 16),
        text(32, 196, L(b, "напишите как есть…", "tell it as it is…"), "small", f'fill:{b["muted2"]}'),
        *button(b, 372, L(b, "Отправить", "Send")),
    ]
    return (L(b, "поддержка", "support"),
            L(b, "Поле, кнопка и честное обещание: обращение зафиксируют и уведомят команду. Больше ничего не обещано.",
              "A field, a button and an honest promise: it will be recorded and the team told. Nothing more is promised."),
            [(L(b, "ПОДДЕРЖКА", "SUPPORT"), body, None)],
            [L(b, "Два вопроса описание оставляет открытыми.",
               "Two questions the description leaves open."),
             L(b, "Откуда именно доступна кнопка — шапка ленты, настройки или своя иконка — не определено.",
               "Where the button lives — the feed's header, settings, or an icon of its own — is undecided."),
             L(b, "Получает ли человек подтверждение отправки — не определено. Чертёж его не обещает.",
               "Whether a person gets a confirmation is undecided. The drawing does not promise one.")])

def s15(b):
    docs = L(b, ["Пользовательское соглашение", "Политика конфиденциальности", "Правила сообщества"],
             ["Terms of service", "Privacy policy", "Community guidelines"])
    body = [text(187, 30, "9:41", "mono", anchor="middle"),
            *header(b, L(b, "документы", "documents"), L(b, "коротко и просто", "short and plain"), False)]
    y = 140
    for d in docs:
        body += [rect(16, y, 342, 60, b["panel2"], b["border"], 16),
                 text(32, y + 36, d, "msg"),
                 text(342, y + 37, "→", "disp", f'fill:{b["accent_text"]}', 16, "end")]
        y += 72
    body += [
    ]
    return (L(b, "юридические документы", "the legal documents"),
            L(b, "Три коротких документа. Они пересказывают уже описанные правила, а не вводят новые.",
              "Three short documents. They restate the rules already written down rather than adding any."),
            [(L(b, "ДОКУМЕНТЫ", "DOCUMENTS"), body, None)],
            [L(b, "Два вопроса описание оставляет открытыми.",
               "Two questions the description leaves open."),
             L(b, "Откуда открывается экран — настройки, футер или шаг регистрации — не определено.",
               "Where the screen opens from — settings, a footer, or a step in signing up — is undecided."),
             L(b, "Нужен ли явный чекбокс согласия при регистрации — не определено.",
               "Whether signing up needs an explicit tick is undecided.")])

def s16(b):
    body = [
        text(187, 30, "9:41", "mono", anchor="middle"),
        *header(b, L(b, "пригласить", "invite"), L(b, "за пределами альфы", "beyond the alpha"), False),
        rect(16, 140, 342, 96, b["panel2"], b["border"], 16),
        text(32, 168, L(b, "ВАША ССЫЛКА", "YOUR LINK"), "brow"),
        text(32, 200, L(b, "sosed.place/i/8f4c1a", "neighbro.place/i/8f4c1a"), "msg"),
        *button(b, 256, L(b, "Скопировать", "Copy")),
    ]
    return (L(b, "приглашения", "referrals"),
            L(b, "За пределами альфы. Персональная ссылка; поощрение получают оба — и позвавший, и пришедший.",
              "Beyond the alpha. A personal link; the reward lands on both — the one who invited and the one who came."),
            [(L(b, "ПРИГЛАСИТЬ", "INVITE"), body, None)],
            [L(b, "Четыре вопроса описание оставляет открытыми.",
               "Four questions the description leaves open."),
             L(b, "Размер поощрения не определён.", "The size of the reward is undecided."),
             L(b, "Откуда человек берёт свою ссылку — не определено. Здесь она на своём экране.",
               "Where a person picks up their link is undecided. Here it has a screen."),
             L(b, "Ограничение на число приглашений не определено.",
               "Whether the number of invitations is capped is undecided."),
             L(b, "Момент начисления не определён: сразу при регистрации или по условию.",
               "When the reward lands is undecided: at signup, or on some condition.")])

def s17(b):
    body = [
        text(187, 30, "9:41", "mono", anchor="middle"),
        *header(b, L(b, "стикеры", "stickers"), L(b, "баланс: 40", "balance: 40"), False),
    ]
    for r in range(3):
        for c in range(3):
            x, y = 16 + c * 116, 140 + r * 116
            body += [rect(x, y, 100, 100, b["panel2"], b["border"], 16),
                     circle(x + 50, y + 42, 22, b["accent"], None, 0.25 + 0.12 * ((r + c) % 4)),
                     text(x + 50, y + 86, L(b, f"{4 + r * 3 + c} ⌁", f"{4 + r * 3 + c} ⌁"),
                          "mono", anchor="middle")]
    body += [
        *button(b, 700, L(b, "Купить за 6", "Buy for 6")),
    ]
    return (L(b, "стикеры", "stickers"),
            L(b, "За пределами альфы. Фиксированный каталог из админ-панели, покупка за внутренний баланс.",
              "Beyond the alpha. A fixed catalogue kept from the admin panel, bought with the in-app balance."),
            [(L(b, "КАТАЛОГ", "CATALOGUE"), body, None)],
            [L(b, "Три вопроса описание оставляет открытыми.",
               "Three questions the description leaves open."),
             L(b, "Откуда открывается каталог — не определено.",
               "Where the catalogue opens from is undecided."),
             L(b, "Цены не определены — числа на чертеже условны.",
               "Prices are undecided — the numbers here are stand-ins."),
             L(b, "Сколько стикеров помещается в одно сообщение — не определено.",
               "How many stickers fit in one message is undecided.")])


def s_feed_states(b):
    """The feed in the four shapes it actually takes. Nothing here explains the
    product — these are the states a screen has to be drawn in before anyone can
    build it."""
    def frame(rows, tail=None, first=None):
        body = [text(187, 30, "9:41", "mono", anchor="middle"),
                *header(b, L(b, "рядом", "34 nearby"), f'{b["here"]} · 1.2 {L(b, "км", "km")}')]
        if first:
            body.append(first)
        y = 130 if b["key"] == "sosed" else 122
        for i, (place, lines, meta, fresh) in enumerate(rows):
            part, h = card(b, y, place, lines, meta, plus=True, fresh=fresh)
            body += part
            y += h + 16
        if tail:
            body += tail(y)
        body += nav(b)
        return body

    full = frame([
        (f'{b["places"][0]} · 27', L(b, ["Кофейня поставила пианино"], ["The café put a piano out"]), "08:12", False),
        (f'{b["places"][1]} · 31', L(b, ["Кто-то потерял синий шарф"], ["Blue scarf by the canal"]), "11:04", False),
        (f'{b["places"][2]} · 24', L(b, ["Кто со мной за эспрессо?"], ["Anyone up for espresso?"]), "12:20", False),
        (f'{b["places"][3]} · 29', L(b, ["Слышали оркестр в семь?"], ["Heard that band at seven?"]),
         L(b, "14:32", "14:32 · 2H 40M"), True),
    ])

    def skeleton(y):
        out = []
        for i in range(3):
            top = 130 + i * 108
            out += plate(b, 16, top, 342, 92)
            out += [rect(36, top + 24, 120, 8, b["panel2"], None, 4),
                    rect(36, top + 48, 250, 8, b["panel2"], None, 4),
                    rect(36, top + 66, 180, 8, b["panel2"], None, 4)]
        return out
    loading = [text(187, 30, "9:41", "mono", anchor="middle"),
               *header(b, L(b, "рядом", "34 nearby"), f'{b["here"]} · 1.2 {L(b, "км", "km")}'),
               *skeleton(0), *nav(b)]

    empty = [text(187, 30, "9:41", "mono", anchor="middle"),
             *header(b, L(b, "рядом", "0 nearby"), f'{b["here"]} · 1.2 {L(b, "км", "km")}'),
             (f'<rect x="16" y="240" width="342" height="150" rx="{b["radius"]}" fill="none" '
              f'stroke="{b["muted2"]}" stroke-width="{b["bw"]}" stroke-dasharray="6 5"/>'),
             text(187, 292, L(b, "Рядом тихо", "Quiet nearby"), "disp", size=18, anchor="middle"),
             text(187, 324, L(b, "в этом радиусе никого", "nobody within this radius"), "muted", anchor="middle"),
             *button(b, 348, L(b, "Расширить радиус", "Widen the radius"), 220, 74),
             *nav(b)]

    def older(y):
        return [text(187, 128, L(b, "↑ тянуть — показать раньше", "↑ pull for earlier"), "mono", anchor="middle")]
    top = frame([
        (f'{b["places"][0]} · 27', L(b, ["Кофейня поставила пианино"], ["The café put a piano out"]), "08:12", False),
        (f'{b["places"][1]} · 31', L(b, ["Кто-то потерял синий шарф"], ["Blue scarf by the canal"]), "11:04", False),
    ], tail=older)

    return (L(b, "лента: состояния", "the feed, in its states"),
            L(b, "Полная, загрузка, пустая, начало списка. Одна и та же лента в четырёх видах.",
              "Full, loading, empty, at the top of the list. One feed in four shapes."),
            [(L(b, "ПОЛНАЯ", "FULL"), full, None),
             (L(b, "ЗАГРУЗКА", "LOADING"), loading, None),
             (L(b, "ПУСТАЯ", "EMPTY"), empty, None)])


def s_gestures(b):
    """Swipes, drawn as position rather than described. A gesture has a resting
    state, a state part-way, and what it uncovers — and only the middle one is
    worth a sheet."""
    lines = L(b, ["Слышали оркестр во дворе", "в семь утра?"],
              ["Heard that brass band in", "the yard at seven?"])

    swiped = [text(187, 30, "9:41", "mono", anchor="middle"),
              *header(b, L(b, "рядом", "34 nearby"), f'{b["here"]} · 1.2 {L(b, "км", "km")}')]
    # what the card slides off to reveal
    swiped += plate(b, 214, 200, 160, 96, b["accent"], b["accent"])
    swiped += [text(238, 240, L(b, "СКРЫТЬ", "HIDE"), "brow", f'fill:{b["ink"]}'),
               text(238, 268, L(b, "СКРЫТЬ ЕГО", "REPORT"), "brow", f'fill:{b["ink"]}')]
    part, h = card(b, 200, f'{b["places"][1]} · 29', lines, "14:32", plus=False, x=-128)
    swiped += part
    swiped += [text(16, 340, L(b, "карточка уезжает влево, под ней — действия",
                               "the card slides left, the actions are under it"), "mono"),
               *nav(b)]

    holding = [text(187, 30, "9:41", "mono", anchor="middle"),
               *header(b, L(b, "рядом", "34 nearby"), f'{b["here"]} · 1.2 {L(b, "км", "km")}')]
    part, h = card(b, 200, f'{b["places"][1]} · 29', lines, "14:32", plus=False)
    holding += part
    holding += [(f'<rect x="12" y="196" width="350" height="{h + 8}" rx="{b["radius"]}" '
                 f'fill="none" stroke="{b["accent"]}" stroke-width="{b["bw"] + 1}"/>'),
                circle(187, 200 + h + 44, 26, b["accent"], None, 0.25),
                circle(187, 200 + h + 44, 14, b["accent"]),
                text(16, 200 + h + 96, L(b, "долгое нажатие — то же меню, без свайпа",
                                         "a long press opens the same menu"), "mono"),
                *nav(b)]

    if b["key"] == "neighbro":
        viewer = [
            text(187, 30, "9:41", "mono", anchor="middle"),
            text(24, 66, "3 / 34", "mono"),
            text(350, 68, "✕", "disp", f'fill:{b["muted2"]}', 16, "end"),
            *plate(b, 44, 150, 286, 300),
            text(68, 190, f'{b["places"][2]} · 24', "brow"),
            *[text(68, 240 + i * 26, s, "msg", size=17) for i, s in enumerate(
                ["Anyone up for a morning", "espresso before work?"])],
            text(68, 330, "two of us · 400 m", "mono"),
            text(68, 420, "FRESH · 4H 02M", "timer"),
            text(60, 500, "←", "disp", f'fill:{b["muted2"]}', 26),
            text(300, 500, "→", "disp", f'fill:{b["accent_text"]}', 26, "end"),
            text(96, 496, "skip", "mono"),
            text(240, 496, "join", "mono"),
            *button(b, 700, "Skip", 150, 24, filled=False),
            *button(b, 700, "I\u2019m in", 150, 200),
        ]
        third = ("ONE AT A TIME", viewer, None)
    else:
        pull = [text(187, 30, "9:41", "mono", anchor="middle"),
                *header(b, L(b, "рядом", "nearby"), f'{b["here"]} · 1.2 {L(b, "км", "km")}'),
                circle(187, 168, 18, "none", b["accent"], None, 2),
                text(187, 176, "↻", "disp", f'fill:{b["accent_text"]}', 18, "middle"),
                text(187, 214, L(b, "отпустите — обновится", "release to refresh"), "mono", anchor="middle")]
        y = 250
        for i in range(2):
            part, h = card(b, y, f'{b["places"][i]} · {27 + i * 2}',
                           L(b, ["Кофейня поставила пианино"], ["The café put a piano out"]), "08:12")
            pull += part
            y += h + 16
        pull += nav(b)
        third = ("ТЯНУТЬ — ОБНОВИТЬ", pull, None)

    return (L(b, "жесты", "gestures"),
            L(b, "Свайп по карточке, долгое нажатие и то, что тянут сверху. Нарисовано положением, а не стрелками на пустом месте.",
              "A swipe across a card, a long press, and the pull from the top. Drawn as position, not as arrows over nothing."),
            [(L(b, "СВАЙП ВЛЕВО", "SWIPE LEFT"), swiped, None),
             (L(b, "ДОЛГОЕ НАЖАТИЕ", "LONG PRESS"), holding, None),
             third])


SCREENS = [
    (1, "splash", "01-splash-screen_RU.md", s01),
    (2, "name", "02-name-screen_RU.md", s02),
    (4, "composer", "04-post-composer_RU.md", s04),
    (3, "feed-shape", "03-feed-screen_RU.md", s03b),
    (3, "feed-states", "03-feed-screen_RU.md", s_feed_states),
    (18, "gestures", "03-feed-screen_RU.md", s_gestures),
    (5, "message-actions", "05-message-actions_RU.md", s05),
    (6, "match-and-chat", "06-match-and-chat_RU.md", s06),
    (7, "chat-list", "07-chat-list_RU.md", s07),
    (8, "chat-screen", "08-chat-screen_RU.md", s08),
    (9, "my-messages", "09-my-messages_RU.md", s09),
    (10, "settings", "10-settings-screen_RU.md", s10),
    (11, "nsfw-consent", "11-nsfw-consent_RU.md", s11),
    (12, "share-link", "12-share-link-in-chat_RU.md", s12),
    (13, "empty-states", "13-empty-and-edge-states_RU.md", s13),
    (14, "support", "14-support_RU.md", s14),
    (15, "legal", "15-legal-documents_RU.md", s15),
    (16, "referral", "16-referral_RU.md", s16),
    (17, "stickers", "17-stickers_RU.md", s17),
]

if __name__ == "__main__":
    written = 0
    for number, slug, doc, build in SCREENS:
        b = dict(BRAND, slug=slug, doc=doc)
        built = build(b)
        name, lede, phones = built[0], built[1], built[2]
        # the light row is the same screen asked again with the light face
        phones_light = build(dict(lit(b), slug=slug, doc=doc))[2]
        height = 184 + 1010 * 2 + 24 + 60
        with open(os.path.join(OUT, f"{number:02d}-{slug}.svg"), "w") as f:
            f.write(sheet_svg(b, number, name, lede, phones, phones_light, height) + "\n")
        written += 1
    print(f"листов написано: {written} → {OUT}")
