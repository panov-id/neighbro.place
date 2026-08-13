#!/usr/bin/env python3
"""Check that the landing deploy hands no secret to python on a command line.

    python3 deploy/test-no-secrets-in-argv.py

An argument is visible in `ps` to every local account for the life of the call,
and is the first thing to end up in a traceback. The Bunny key therefore travels
through the environment, as HEADERS_JSON beside it always did — and moving it is
the kind of change that quietly shifts an argument index, which no syntax check
would catch.

So the embedded block is executed with urlopen replaced by something that raises:
everything up to the first request — which is all the argument handling — really
runs, and nothing leaves the machine.
"""

import os
import pathlib
import re
import sys
import urllib.request

DEPLOY = pathlib.Path(__file__).parent
SCRIPT = DEPLOY / "deploy-landing.sh"
SECRETS = r"BUNNY_API_KEY|BUNNY_STORAGE_API_KEY|GITHUB_TOKEN|TOKEN"
HEREDOC = re.compile(r"<<'(PY|PYEOF)'\n(.*?)\n(PY|PYEOF)\n", re.S)

failed = 0


def check(name, condition, detail=""):
    global failed
    if condition:
        print(f"  ok   {name}")
    else:
        failed += 1
        print(f"  FAIL {name} — {detail}")


class Blocked(Exception):
    pass


def blocked(*_args, **_kwargs):
    raise Blocked("the network is not available to this check")


text = SCRIPT.read_text(encoding="utf-8")

offenders = [
    f"{SCRIPT.name}:{number}"
    for number, line in enumerate(text.splitlines(), 1)
    if "python3 -" in line and re.search(rf'"\${{?({SECRETS})}}?"', line)
]
check("no secret is passed on a command line", not offenders, ", ".join(offenders))

blocks = [body for _, body, _ in HEREDOC.findall(text) if "urllib" in body]
check("the edge block was found", bool(blocks))

if blocks:
    saved_argv, saved_environment = sys.argv, dict(os.environ)
    saved_urlopen = urllib.request.urlopen
    sys.argv = ["-", "42"]
    os.environ.update({
        "BUNNY_API_KEY": "k",
        "HEADERS_JSON": '{"headers":[{"name":"X-Test","value":"1"}],"counted":{"pages":1}}',
    })
    urllib.request.urlopen = blocked
    try:
        exec(compile(blocks[-1], SCRIPT.name, "exec"), {"__name__": "__main__"})
        check("it parses its arguments", True)
    except (Blocked, SystemExit):
        check("it parses its arguments", True)
    except Exception as error:  # noqa: BLE001
        check("it parses its arguments", False, f"{type(error).__name__}: {error}")
    finally:
        sys.argv = saved_argv
        os.environ.clear()
        os.environ.update(saved_environment)
        urllib.request.urlopen = saved_urlopen

print()
if failed:
    print(f"FAILED: {failed}")
    sys.exit(1)
print("deploy-landing: no secret on a command line, and it still parses")
