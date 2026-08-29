#!/usr/bin/env python3
"""Hold the documents' own dates against the documents' own bytes.

A person accepts a contract with a checkbox, and what gets recorded next to the
identity has to answer one question later: *which text did they accept?* Until
2026-08-29 the answer was a "Last updated" line — a date a human types. It fails
in the way hand-kept identifiers always fail, and it had already failed here:
the community guidelines were edited on 2026-08-27 and went on announcing
13 August for two weeks. Nothing was red, because nothing was looking.

So the revision of a document is a **date plus the sha256 of its bytes**, and
this holds the pair against a baseline that only changes by decision:

  * bytes changed, date did not  → the header lies about a text that moved;
  * date changed, bytes did not  → a revision nobody made was announced;
  * both changed                 → not a lie, but the baseline is stale: run
                                   --update, look at the diff, commit it. That
                                   commit *is* the decision that a new revision
                                   exists, made in one place instead of being
                                   discovered by whoever gets sued.

Only the three English originals are hashed. The clause inside every translated
document says the English version governs, so the English text is what was
accepted; a fixed typo in one of seventeen translations must not send everybody
back to a consent screen.

    check-legal-revisions.py [--root DIR] [--update] [--self-test]

Exits non-zero on any mismatch. --self-test breaks the thing this guards, in
both directions, and asserts it goes red — a check whose failure was never seen
is decoration.
"""

import argparse
import datetime
import hashlib
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

# The three documents a person accepts, and what a change to each one costs.
# "required": the identity must accept again before it can publish or open a
# chat — these two are the contract itself. "silent": the accepted revision is
# re-recorded and screen 15 marks it, with nothing blocked — the guidelines
# describe what the product already enforces, and stopping a conversation to
# announce a reworded sentence trains people to click through consent screens.
DOCUMENTS = {
    "terms": ("terms_EN.md", "required"),
    "privacy": ("privacy_EN.md", "required"),
    "guidelines": ("community-guidelines_EN.md", "silent"),
}

MONTHS = {m: i for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july",
     "august", "september", "october", "november", "december"], start=1)}

DATE_LINE = re.compile(r"Last updated:\s*(\d{1,2})\s+([A-Za-z]+)\s+(\d{4})")


def read_document(path):
    """The date the document declares and the digest of everything else.

    The date line lives inside the file, so hashing the file whole would make
    every date edit a text edit and the two could never be told apart — the
    first version of this check had a branch that could not be reached. So the
    digest is taken with the date line blanked out: it is the *substance*, and
    the date is the other half of the pair. A date moved on its own then shows
    up as exactly what it is, and a substance moved on its own does too.
    """
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    found = DATE_LINE.search(text[:2000])
    if not found:
        raise SystemExit(f"нет строки «Last updated» в {path} — редакцию не из чего вывести")
    day, month, year = found.groups()
    if month.lower() not in MONTHS:
        raise SystemExit(f"неизвестный месяц «{month}» в {path}")
    date = datetime.date(int(year), MONTHS[month.lower()], int(day))
    body = DATE_LINE.sub("Last updated: —", text, count=1)
    return date.isoformat(), hashlib.sha256(body.encode("utf-8")).hexdigest()


def translation_dates(legal_dir, day, year):
    """Every language version of a document declares one date, or none of them do.

    The translations are not hashed — the clause inside each says the English
    version governs — but they carry their own "last updated" line, and on
    2026-08-29 all twenty-five of them still said 13 August while the original
    had moved to the 27th. A reader is told the date of the text in front of
    them, so that date has to be the document's date.

    Month names are not checked: seventeen languages decline them differently
    and a table of that would rot faster than it would catch anything. The day
    and the year are digits everywhere, including the two languages that write
    the year first, and they are what drifts.
    """
    problems = []
    for path in sorted(legal_dir.glob("community-guidelines_*.md")):
        if path.name.endswith("_EN.md"):
            continue
        head = path.read_text(encoding="utf-8").splitlines()[:10]
        line = next((l for l in head if year in re.findall(r"\d+", l)), None)
        if line is None:
            problems.append(f"{path.name}: нет строки с датой в первых десяти строках")
            continue
        numbers = sorted(re.findall(r"\d+", line))
        if numbers != sorted([day, year]):
            problems.append(
                f"{path.name}: дата «{line.strip()[:60]}» расходится с оригиналом "
                f"({day}.{year}) — перевод датирует себя не тем днём")
    return problems


def collect(legal_dir):
    current = {}
    for key, (filename, reaccept) in DOCUMENTS.items():
        path = legal_dir / filename
        if not path.is_file():
            raise SystemExit(f"нет документа {path}")
        date, digest = read_document(path)
        current[key] = {"date": date, "sha256": digest, "reaccept": reaccept}
    return current


def compare(baseline, current):
    """Every way the pair (date, bytes) can disagree with what was decided."""
    problems = []
    stale = []
    for key, now in current.items():
        was = baseline.get(key)
        if was is None:
            stale.append(f"{key}: документа нет в базовой записи — редакция ещё не решена")
            continue
        date_moved = was["date"] != now["date"]
        text_moved = was["sha256"] != now["sha256"]
        if text_moved and not date_moved:
            problems.append(
                f"{key}: текст изменился, а дата в шапке осталась {now['date']} — "
                f"документ датирует себя неверно, и принятая редакция указывает не на тот текст\n"
                f"    было  {was['sha256'][:16]}…\n"
                f"    стало {now['sha256'][:16]}…")
        elif date_moved and not text_moved:
            problems.append(
                f"{key}: дата стала {now['date']} (была {was['date']}), а текст не менялся — "
                f"объявлена редакция, которой никто не делал")
        elif date_moved and text_moved:
            stale.append(f"{key}: {was['date']} → {now['date']}, текст изменился — новая редакция")
        if was.get("reaccept") != now["reaccept"]:
            problems.append(
                f"{key}: политика повторного принятия в базовой записи "
                f"«{was.get('reaccept')}», а в проверке «{now['reaccept']}»")
    for key in baseline:
        if key not in current:
            problems.append(f"{key}: есть в базовой записи, но такого документа нет")
    return problems, stale


def load_baseline(path):
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))["documents"]


def write_baseline(path, current):
    path.write_text(json.dumps(
        {"documents": current}, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8")


def run(root, update):
    legal_dir = root / "landing" / "legal"
    baseline_path = root / "deploy" / "legal-revisions.json"
    current = collect(legal_dir)
    baseline = load_baseline(baseline_path)
    problems, stale = compare(baseline, current)
    guide_date = datetime.date.fromisoformat(current["guidelines"]["date"])
    problems += translation_dates(legal_dir, str(guide_date.day), str(guide_date.year))

    if problems:
        print("редакции документов не сходятся с их текстами:", file=sys.stderr)
        for line in problems:
            print(f"  ✗ {line}", file=sys.stderr)
        if not update:
            print("\n  дата в шапке правится вместе с текстом; после — "
                  "check-legal-revisions.py --update", file=sys.stderr)
            return 1

    if stale:
        for line in stale:
            print(f"  · {line}", file=sys.stderr)
        if not update:
            print("\nбазовая запись отстала. Посмотрите изменения глазами и, если это "
                  "действительно новая редакция:\n  check-legal-revisions.py --update",
                  file=sys.stderr)
            return 1

    if update:
        write_baseline(baseline_path, current)
        print(f"базовая запись обновлена: {baseline_path}")
        return 0

    for key, now in sorted(current.items()):
        print(f"  {key:<11} {now['date']}  {now['sha256'][:16]}…  {now['reaccept']}")
    translations = len(list(legal_dir.glob("community-guidelines_*.md"))) - 1
    print(f"проверено документов: {len(current)} — дата и текст сходятся у всех; "
          f"и {translations} переводов правил датируют себя днём оригинала")
    return 0


def self_test(root):
    """Break it in both directions and watch it go red, then watch it go green."""
    def probe(label, mutate):
        with tempfile.TemporaryDirectory() as tmp:
            copy = pathlib.Path(tmp) / "repo"
            copy.mkdir()
            for part in ("landing/legal", "deploy"):
                target = copy / part
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copytree(root / part, target)
            mutate(copy)
            done = subprocess.run(
                [sys.executable, str(pathlib.Path(__file__).resolve()),
                 "--root", str(copy)],
                capture_output=True, text=True)
            return label, done.returncode, (done.stdout + done.stderr).strip()

    def edit_text(copy):
        path = copy / "landing/legal/terms_EN.md"
        path.write_text(path.read_text(encoding="utf-8") + "\nOne more sentence.\n",
                        encoding="utf-8")

    def edit_date(copy):
        path = copy / "landing/legal/privacy_EN.md"
        text = path.read_text(encoding="utf-8")
        path.write_text(DATE_LINE.sub("Last updated: 1 January 2030", text, count=1),
                        encoding="utf-8")

    def edit_translation_date(copy):
        path = copy / "landing/legal/community-guidelines_RU.md"
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        for i, line in enumerate(lines[:10]):
            if "2026" in line:
                lines[i] = line.replace("27", "13")
                break
        path.write_text("".join(lines), encoding="utf-8")

    def edit_both(copy):
        edit_text(copy)
        path = copy / "landing/legal/terms_EN.md"
        path.write_text(DATE_LINE.sub("Last updated: 1 January 2030",
                                      path.read_text(encoding="utf-8"), count=1),
                        encoding="utf-8")

    cases = [
        ("текст изменился, дата стоит", edit_text, 1),
        ("дата уехала, текст стоит", edit_date, 1),
        ("уехало и то и другое — новая редакция, база отстала", edit_both, 1),
        ("перевод отстал от оригинала на день", edit_translation_date, 1),
        ("ничего не трогали", lambda copy: None, 0),
    ]
    failures = 0
    for label, mutate, expected in cases:
        name, code, output = probe(label, mutate)
        ok = code == expected
        failures += 0 if ok else 1
        print(f"  {'✓' if ok else '✗'} {name}: код {code}, ожидали {expected}")
        if not ok:
            print("      " + output.replace("\n", "\n      "))
        elif expected == 1:
            said = next((l for l in output.splitlines()
                         if l.strip().startswith(("✗", "·"))), "")
            print(f"      {said.strip()}")
    if failures:
        print(f"самопроверка провалена: {failures}", file=sys.stderr)
        return 1
    print("самопроверка пройдена: подсадка ловится в обе стороны, чистое дерево зелёное")
    return 0


def main():
    parser = argparse.ArgumentParser(add_help=True, description=__doc__)
    parser.add_argument("--root", default=None,
                        help="корень витрины (по умолчанию — родитель каталога скрипта)")
    parser.add_argument("--update", action="store_true",
                        help="записать текущие дату и хэш как решённую редакцию")
    parser.add_argument("--self-test", action="store_true",
                        help="сломать проверяемое и убедиться, что проверка краснеет")
    args = parser.parse_args()
    root = pathlib.Path(args.root).resolve() if args.root \
        else pathlib.Path(__file__).resolve().parent.parent
    if args.self_test:
        return self_test(root)
    return run(root, args.update)


if __name__ == "__main__":
    sys.exit(main())
