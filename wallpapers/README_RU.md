# NEIGHBRO — генератор обоев и баннеров

Система собирает обои и баннеры в фирменном стиле NEIGHBRO из матрицы
**темы × режимы × языки × стили фона × наполнение × форматы**. Всё рисуется кодом
(SVG/CSS) на фирменных шрифтах и цветах лендинга; фон-арт от ИИ подставляется
опционально.

## Что внутри
- `catalog.mjs` — единый источник: темы, палитры, копирайт (6 языков), форматы, стили.
- `template.html` — рендер-страница: рисует один макет, шрифты берёт из `../landing/fonts/`.
- `render.mjs` — Puppeteer: обходит матрицу и пишет PNG + галерею `output/index.html`.
- `ai-prompts/PROMPTS_RU.md` / `PROMPTS_EN.md` — промпты для Lexica / Midjourney под фон.
- `docker/` — образ с Chromium и скрипт запуска (на хост ничего не ставится).

## Оси матрицы
- **Темы:** gold (по умолчанию), crimson, teal, azure, violet
- **Режимы:** dark, light
- **Языки:** en, ru, fr, de, es, el
- **Стили фона:** plain, glow, mesh, grid, rings, contour, houses, steps, art (ИИ)
- **Наполнение:** `mark` (только лого), `brand` (лого + строка), `full` (+ заголовок)
- **Форматы:** ultrawide 3440×1440, desktop 1080p/1440p/4K, iPhone 1179×2556,
  Android 1080×2340, stories 1080×1920, post 1080×1080, OG 1200×630, hero 1920×1080

## Запуск
```bash
# Полный дефолтный набор (5 тем × 2 режима × 8 стилей × все форматы, en)
./docker/run.sh

# Точечно
./docker/run.sh --formats ultrawide,mobileIPhone --themes gold,teal \
  --modes dark --styles glow,mesh,rings --content full --langs en,ru

# С ИИ-фоном
./docker/run.sh --formats ultrawide --styles art --art art/twilight.jpg
```
Результат — в `output/<категория>/...png`, обзор — `output/index.html`.

Флаги: `--formats --themes --modes --langs --styles --content --art --out --limit`
(значения через запятую, `all` = все). Без флагов — курируемый дефолт.

## Быстрый предпросмотр без Docker
Открой `template.html?spec=<base64 JSON>` в браузере, где JSON — например
`{"format":"ultrawide","theme":"gold","mode":"dark","lang":"en","style":"glow","content":"full"}`.

## ИИ-фоны (гибрид)
1. Прогони промпты из `ai-prompts/PROMPTS_RU.md` в Lexica под нужный aspect ratio.
2. Сохрани удачные кадры в `art/…jpg`.
3. Запусти со `--styles art --art art/твой.jpg` — код наложит лого/текст/скрим сверху.

## Будущие итерации
Новый язык/тема/формат/стиль — добавь в `catalog.mjs`, перезапусти `run.sh`.
Скрипт идемпотентен и перерисовывает всё заново.
