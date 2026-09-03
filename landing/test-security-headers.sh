#!/usr/bin/env bash
# Exercise landing/security-headers.mjs against fixture markup. No network.
#
#     bash landing/test-security-headers.sh
#
# This script decides what the landing is allowed to do in production, and it is
# the only place that decides it: the header lives at the CDN edge, so no local
# server sends it and no browser check runs before a deploy. A wrong hash is a
# page that silently does nothing in production and works everywhere else.
#
# The panel's builder has the same shape and its own copy of this
# (xor.ad/deploy/test_panel_security_headers.sh). The two differ where the two
# faces differ, and the differences are what most of the cases below are about.
set -uo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BUILDER="${BUILDER_UNDER_TEST:-$ROOT/landing/security-headers.mjs}"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

failed=0

pass() { echo "  ok   $1"; }
fail() { echo "  FAIL $1 — $2"; failed=$((failed + 1)); }

# A landing in miniature: an inline script, a structured-data block that is data
# rather than code, an external script, an inline stylesheet and a style
# attribute — all five shapes the builder has to tell apart.
mkdir -p "$WORK/stage/ru"
printf '%s' '<!doctype html><html><head><base href="/">
<style>body{margin:0}</style>
<script type="application/ld+json">{"@type":"WebSite"}</script>
<script src="/config.js"></script>
<script>window.lang="en"</script>
</head><body><p style="color:red">x</p></body></html>' > "$WORK/stage/index.html"
printf '%s' '<!doctype html><html><body><p style="color:red">x</p><script>window.lang="ru"</script></body></html>' \
  > "$WORK/stage/ru/index.html"

build() { # build <relay> [analytics id] [report host]
  RELAY_API_URL="$1" ANALYTICS_ID="${2:-}" RELAY_REPORT_URL="${3:-}" \
    node "$BUILDER" "$WORK/stage" 2>&1
}

# --- the value of the relay address ------------------------------------------

for bad_value in "https://relay.example/v1" "not a url" "https://relay.example ; script-src *"; do
  output="$(build "$bad_value")"
  status=$?
  label="refuses relay value '$bad_value'"
  if [ $status -eq 0 ]; then
    fail "$label" "exited 0"
  elif ! printf '%s' "$output" | grep -qi 'not a usable CSP source'; then
    fail "$label" "message does not explain: $output"
  else
    pass "$label"
  fi
done

# Unlike the panel, an empty value is legal here: a stand without a relay is a
# stand, not a mistake. What it must not do is invent an endpoint.
output="$(build "")"
if [ $? -ne 0 ]; then
  fail "an empty relay is allowed" "$output"
else
  printf '%s' "$output" > "$WORK/norelay.json"
  python3 - "$WORK/norelay.json" <<'PY'
import json, sys
data = json.load(open(sys.argv[1]))
headers = {h["name"]: h["value"] for h in data["headers"]}
csp = headers["Content-Security-Policy"]
failed = 0
def check(name, condition, detail=""):
    global failed
    if condition:
        print(f"  ok   {name}")
    else:
        failed += 1
        print(f"  FAIL {name} — {detail}")
check("an empty relay is allowed", True)
check("no report directives without a relay",
      "report-uri" not in csp and "report-to" not in csp, csp)
check("no Reporting-Endpoints without a relay",
      "Reporting-Endpoints" not in headers, str(list(headers)))
check("connect-src is just 'self'", "connect-src 'self';" in csp + ";", csp)
sys.exit(1 if failed else 0)
PY
  [ $? -eq 0 ] || failed=$((failed + 1))
fi

output="$(build "https://relay.example/")"
if [ $? -ne 0 ]; then
  fail "a trailing slash is accepted" "$output"
else
  pass "a trailing slash is accepted"
fi

# --- the address an Article 16 notice is sent to ------------------------------
#
# It is a host of its own: the api host sits behind a WAF that blocks a report
# quoting the attack it reports. The deploy has been passing RELAY_REPORT_URL
# since the intake moved, while the policy was built from RELAY_API_URL alone —
# so connect-src refused the very request the move existed to allow, and the
# notifier saw nothing. These cases hold the two halves: the value is validated
# like the api one, and it reaches connect-src.

for bad_report in "https://report.example/v1" "not a url"; do
  output="$(build "https://relay.example" "" "$bad_report")"
  status=$?
  label="refuses report value '$bad_report'"
  if [ $status -eq 0 ]; then
    fail "$label" "exited 0"
  elif ! printf '%s' "$output" | grep -qi 'RELAY_REPORT_URL is not a usable CSP source'; then
    fail "$label" "message does not name the variable: $output"
  else
    pass "$label"
  fi
done

output="$(build "https://relay.example" "" "https://report.example")"
if [ $? -ne 0 ]; then
  fail "a report host builds" "$output"
else
  printf '%s' "$output" > "$WORK/report.json"
  python3 - "$WORK/report.json" <<'PY2'
import json, sys
data = json.load(open(sys.argv[1]))
headers = {h["name"]: h["value"] for h in data["headers"]}
csp = headers["Content-Security-Policy"]
connect = [d for d in csp.split(";") if d.strip().startswith("connect-src")][0]
failed = 0
def check(name, condition, detail=""):
    global failed
    if condition:
        print(f"  ok   {name}")
    else:
        failed += 1
        print(f"  FAIL {name} — {detail}")
check("the report host is in connect-src", "https://report.example" in connect, connect)
check("the api host is still in connect-src", "https://relay.example" in connect, connect)
# csp-report goes to the api host, not the report one: it is a browser report,
# not an Article 16 notice, and nothing about it is quoted from an attack.
check("csp reporting still points at the api host",
      headers.get("Reporting-Endpoints", "").count("https://relay.example/csp-report") == 1,
      headers.get("Reporting-Endpoints", ""))
sys.exit(1 if failed else 0)
PY2
  [ $? -eq 0 ] || failed=$((failed + 1))
fi

# No report host is legal and means the page falls back to the api one.
output="$(build "https://relay.example")"
if [ $? -ne 0 ]; then
  fail "an empty report host is allowed" "$output"
else
  if printf '%s' "$output" | grep -q 'report.example'; then
    fail "an empty report host is allowed" "invented an endpoint"
  else
    pass "an empty report host is allowed"
  fi
fi

# --- what the policy says, with a relay and no analytics ---------------------

GOOD="$(build "https://relay.example")"
if [ $? -ne 0 ]; then
  echo "  FAIL a valid origin builds — $GOOD"
  echo "FAILED: 1"
  exit 1
fi
pass "a valid origin builds"

printf '%s' "$GOOD" > "$WORK/good.json"
python3 - "$WORK/good.json" <<'PY'
import json, sys

data = json.load(open(sys.argv[1]))
headers = {h["name"]: h["value"] for h in data["headers"]}
csp = headers["Content-Security-Policy"]
counted = data["counted"]
failed = 0

def check(name, condition, detail=""):
    global failed
    if condition:
        print(f"  ok   {name}")
    else:
        failed += 1
        print(f"  FAIL {name} — {detail}")

expected = [
    "Content-Security-Policy", "Reporting-Endpoints", "Strict-Transport-Security",
    "X-Content-Type-Options", "Referrer-Policy", "X-Frame-Options", "Permissions-Policy",
]
check("seven headers, in order",
      [h["name"] for h in data["headers"]] == expected,
      str([h["name"] for h in data["headers"]]))
check("report-uri names the relay",
      "report-uri https://relay.example/csp-report" in csp, csp)
check("report-to names the group", "report-to csp" in csp, csp)
check("the group is defined",
      headers["Reporting-Endpoints"] == 'csp="https://relay.example/csp-report"',
      headers["Reporting-Endpoints"])

# Both pages are counted, not only the source one: the per-language copies are
# generated before this runs, and a hash missing for /ru/ is a dead page in one
# language and a working one in every other.
check("every generated page is read", counted["pages"] == 2, str(counted))

# ld+json is data. Browsers never execute it and CSP never blocks it, so hashing
# it would add a hash that can never match.
check("two inline scripts, the ld+json block excluded",
      counted["inline_scripts"] == 2, str(counted))
check("the external script is not hashed", "config.js" not in csp, csp)
check("the inline stylesheet is counted", counted["inline_styles"] == 1, str(counted))
# The same attribute on two pages is one hash, not two.
check("identical style attributes collapse to one",
      counted["style_attributes"] == 1, str(counted))

# Unlike the panel, the landings do carry style attributes, and a hash does not
# apply to an attribute without this.
check("'unsafe-hashes' is present, because attributes are",
      "style-src 'self' 'unsafe-hashes' 'sha256-" in csp, csp)

# base-uri 'self' rather than 'none': <base href="/"> is load-bearing for the
# per-language folders, and 'none' blocked our own tag. This is the one that
# broke the home page once.
check("base-uri is 'self'", "base-uri 'self'" in csp, csp)

check("nothing of Google's without an analytics id",
      "google" not in csp, csp)

sys.exit(1 if failed else 0)
PY
[ $? -eq 0 ] || failed=$((failed + 1))

# --- with analytics ----------------------------------------------------------

WITH_GA="$(build "https://relay.example" "G-TEST")"
if [ $? -ne 0 ]; then
  fail "analytics builds" "$WITH_GA"
else
  printf '%s' "$WITH_GA" > "$WORK/ga.json"
  python3 - "$WORK/ga.json" <<'PY'
import json, sys
data = json.load(open(sys.argv[1]))
csp = {h["name"]: h["value"] for h in data["headers"]}["Content-Security-Policy"]
failed = 0
def check(name, condition, detail=""):
    global failed
    if condition:
        print(f"  ok   {name}")
    else:
        failed += 1
        print(f"  FAIL {name} — {detail}")
check("the tag manager is allowed to load",
      "https://www.googletagmanager.com" in csp, csp)
check("analytics may be talked to",
      "https://www.google-analytics.com" in csp, csp)
check("analytics is recorded as on", data["counted"]["analytics"] is True,
      str(data["counted"]))
sys.exit(1 if failed else 0)
PY
  [ $? -eq 0 ] || failed=$((failed + 1))
fi

echo
if [ "$failed" -ne 0 ]; then
  echo "FAILED: $failed"
  exit 1
fi
echo "security-headers: every case passed"
