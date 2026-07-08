# NEIGHBRO — промпты для ИИ-фонов (Lexica Art / Midjourney / SDXL)

Промпты генерируют **только фон**. Текст, лого и заголовок накладывает кодовый
генератор (`template.html` → `render.mjs`), поэтому центр и верх кадра держи
спокойными, оставляй свободное место. Текст в самом промпте рисовать **не** проси —
модели пишут его криво.

## Направление бренда (вставляй как преамбулу стиля, если инструмент позволяет)
Тёплый тёмный минимализм, настроение «камерный speakeasy», тихо и премиально,
редакционно, спокойно. Тёплый near-black фон (#0c0b09), тёплый кремовый свет, один
приглушённо-золотой акцент (#c6a24e). Анти-соцсеть: без толп, без логотипов, без UI.
Мягко, камерно, архитектурно. Зерно и глубина вместо насыщенности.

## Соотношения сторон под цели
- Ultrawide 34": `--ar 21:9`
- Десктоп: `--ar 16:9`
- Мобилка / Сторис: `--ar 9:16` (Midjourney); в Lexica — самый вытянутый портрет
- Квадратный пост: `--ar 1:1`
- OG / hero-баннер: `--ar 16:9` или `1.91:1`

Хвост качества для Midjourney: `--style raw --v 6 --q 2`. Для Lexica добавь
`highly detailed, cinematic lighting, 8k` и выбери модель SDXL/Flux.

---

## Варианты палитры
Меняй слово-акцент под темы лендинга:
gold `muted gold #c6a24e` · crimson `deep crimson red #e0342b` ·
teal `deep teal green #1fb39a` · azure `soft azure blue #3d84d6` ·
violet `muted violet #9b5de5`. Фон для тёмных — тёплый near-black, для светлых —
тёплый кремовый (#e9e6dd).

> Ниже промпты на английском (модели понимают его точнее), с русской пометкой темы.

---

## 1 — Двор в сумерках (флагман, тёмный)
> A quiet residential courtyard at blue hour, warm glowing windows scattered across
> dark building facades, seen from a distance, cinematic depth of field, soft bokeh
> of golden window light, near-black warm-brown atmosphere, muted gold highlights,
> minimal, moody, intimate, film grain, negative space in the sky, no people, no
> text, editorial photography --ar 21:9 --style raw

## 2 — Район с высоты ночью
> Abstract aerial view of a small neighborhood at night, softly glowing golden
> streetlights forming a gentle constellation, dark warm ground, out-of-focus,
> minimal, calm, lots of negative space, muted gold on near-black, cinematic,
> subtle grain, no text --ar 16:9

## 3 — Два окна, одна улица (близость)
> Two warmly lit apartment windows facing each other across a narrow dark street at
> dusk, cozy golden interior light, minimal, tender, cinematic, shallow focus,
> near-black warm palette, muted gold glow, film grain, no people visible, no text
> --ar 9:16

## 4 — Абстрактное золотое поле света
> Minimal abstract background, soft flowing bands of muted gold light dissolving into
> near-black warm-brown darkness, gentle gradient, faint grain, calm, premium,
> spacious, cinematic, no objects, no text --ar 21:9

## 5 — Контурная карта квартала
> Elegant topographic contour lines of a city district, thin muted-gold lines on a
> near-black warm ground, minimal cartographic art, precise, quiet, spacious, a
> single soft glow, no labels, no text --ar 16:9

## 6 — Дверной проём с тёплым светом
> A single dark doorway spilling a warm golden light onto a quiet cobblestone street
> at night, minimal, cinematic, intimate, deep shadows, muted gold accent,
> near-black warm atmosphere, film grain, no people, no text --ar 9:16

## 7 — Крыша-терраса, час вина (моменты)
> A softly lit rooftop terrace at dusk, two empty chairs and a small table, warm
> golden string lights bokeh, city silhouette far below, calm and intimate,
> cinematic, near-black warm palette, muted gold, shallow depth, film grain, no
> people, no text --ar 21:9

## 8 — Исчезновение / эфемерность (концепт Fade)
> Abstract minimal composition of soft dissolving particles of warm golden light
> drifting and fading into dark warm-brown void, sense of impermanence, calm,
> premium, cinematic, fine grain, lots of negative space, no text --ar 16:9

## 9 — Светлая тема / бетон
> Minimal warm off-white concrete texture (#e9e6dd), soft daylight, a single muted
> gold geometric arc, calm, editorial, spacious, subtle grain, architectural, no
> text --ar 21:9

## 10 — Сетка окон, утро (светлый)
> Facade of warm cream apartment building in soft morning light, orderly grid of
> windows, minimal, calm, editorial architectural photography, muted gold reflection
> in one window, warm off-white palette, spacious, no people, no text --ar 16:9

---

## Советы
- Для мобилки бери **портретные кропы** — генерь 9:16, верхняя треть оверлея ляжет
  над сюжетом.
- Если Lexica подрисовывает текст — добавь негативы: `no text, no watermark, no
  letters, no signage, no UI`.
- Сохраняй удачные кадры в `wallpapers/art/<стиль-или-тема>/<имя>.jpg`; генератор
  подхватит их при `style=art` и флаге `--art <путь>`.
