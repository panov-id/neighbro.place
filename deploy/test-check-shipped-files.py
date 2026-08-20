#!/usr/bin/env python3
"""What the manifest guard does with a storefront it was not told about.

    python3 deploy/test-check-shipped-files.py

The guard was written because five of our own check scripts answered 200 on the
production storefront for months: the landing directory ships whole and there
was no list to hold it against. It shipped without a test of its own, which
means the first thing that would ever exercise it is a deploy — the same mistake
the landing's CI was created to stop.

What is worth pinning is the distinction it exists for: a file nobody allowed
stops the deploy, and a rule that matches nothing does not. The first is an
undecided publication; the second is only a list going stale, and a deploy that
refused there would break on a legitimate build — dev has no sitemap.xml, prod
does.
"""

import pathlib
import subprocess
import sys
import tempfile

GUARD = pathlib.Path(__file__).with_name("check-shipped-files.py")
REAL_MANIFEST = pathlib.Path(__file__).with_name("landing-shipped.manifest")

failed = 0


def check(name, condition, detail=""):
    global failed
    if condition:
        print(f"  ok   {name}")
    else:
        failed += 1
        print(f"  FAIL {name} — {detail}")


def run(files, manifest_text):
    """Build a staging copy and a manifest, then ask the guard about them."""
    with tempfile.TemporaryDirectory() as work:
        root = pathlib.Path(work)
        stage = root / "stage"
        stage.mkdir()
        for name in files:
            path = stage / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("x", encoding="utf-8")
        manifest = root / "manifest"
        manifest.write_text(manifest_text, encoding="utf-8")
        done = subprocess.run(
            [sys.executable, str(GUARD), str(stage), str(manifest)],
            capture_output=True, text=True,
        )
        return done.returncode, done.stdout, done.stderr


MANIFEST = """
# the pages themselves
index.html
legal.html
*/index.html
# generated at deploy time
config.js
robots.txt
sitemap.xml
sw.js
# typography and pictures
fonts.css
fonts/*.woff2
img/*.jpg
og-image.jpg
legal/*.md
"""

# A storefront as the deploy stages it: pages, the per-language folders that
# build-pages.mjs renders, and the files generated at deploy time.
STAGE = ["index.html", "legal.html", "ru/index.html", "ka/index.html",
         "config.js", "robots.txt", "sitemap.xml", "sw.js",
         "fonts.css", "fonts/inter.woff2", "img/hero.jpg", "og-image.jpg",
         "legal/privacy.md"]

code, out, err = run(STAGE, MANIFEST)
check("a staged storefront that matches the manifest passes", code == 0, f"код {code}: {err}")
check("and it says what it looked at", "файлов 13" in out, out)

# The case the guard was written for, name for name: a check script sitting in
# the landing directory and shipping with everything else.
code, out, err = run(STAGE + ["check-contrast.mjs"], MANIFEST)
check("our own tooling stops the deploy", code == 1, f"код {code}")
check("and it is named", "check-contrast.mjs" in err, err)
check("and the message explains rather than orders",
      "впишите правило" in err and "manifest" in err, err)

code, _, err = run(STAGE + ["test-security-headers.sh"], MANIFEST)
check("a shell script in the landing is a stranger too",
      code == 1 and "test-security-headers.sh" in err, f"код {code}: {err}")

# dev and uat delete sitemap.xml on purpose — indexing is production-only. A
# guard that refused over an unmatched rule would fail every non-production
# deploy.
without_sitemap = [name for name in STAGE if name != "sitemap.xml"]
code, out, err = run(without_sitemap, MANIFEST)
check("a non-production stage without sitemap.xml still passes", code == 0, f"код {code}: {err}")
check("and the unused rule is printed rather than swallowed",
      "правила без совпадений" in out and "sitemap.xml" in out, out)

# A new language folder is the normal way this landing grows, and it must not
# need a manifest edit every time.
code, _, err = run(STAGE + ["hy/index.html"], MANIFEST)
check("a new language folder needs no new rule", code == 0, f"код {code}: {err}")

# But a stray page at the root is not covered by */index.html.
code, _, err = run(STAGE + ["draft.html"], MANIFEST)
check("a page nobody listed is caught",
      code == 1 and "draft.html" in err, f"код {code}: {err}")

code, out, err = run(STAGE, "# only comments\n\n")
check("an empty manifest is refused, not treated as 'all allowed'",
      code != 0 and "пуст" in (out + err), f"код {code}: {out}{err}")

code, out, err = run([], MANIFEST)
check("an empty staging directory is refused",
      code != 0 and "нет файлов" in (out + err), f"код {code}: {out}{err}")

# The manifest that actually ships has to accept a canonical stage, or the cases
# above describe a file nobody uses.
code, out, err = run(STAGE, REAL_MANIFEST.read_text(encoding="utf-8"))
check("the real landing manifest accepts a canonical stage", code == 0, f"код {code}: {err}")

print()
if failed:
    print(f"FAILED: {failed}")
    sys.exit(1)
print("check-shipped-files: every case passed")
