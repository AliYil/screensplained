#!/usr/bin/env bash
# The Turkey test (Jeff Moser, 2008), on today's languages: the default case functions on a Linux computer set to
# Turkish (tr_TR.UTF-8) against the same computer set to US English (en_US.UTF-8).
# Usage: bash analysis/run.sh   ->  results/results.json, results/results.txt
set -euo pipefail
cd "$(dirname "$0")"
export DOTNET_CLI_TELEMETRY_OPTOUT=1 DOTNET_NOLOGO=1
(cd java && javac -d . T.java)
(cd c && gcc -O0 -o t t.c)
(cd go && go build -o t .)
(cd cs && dotnet build -c Release -o out >/dev/null)
out=()
for loc in tr_TR.UTF-8 en_US.UTF-8; do
  export LANG=$loc LC_ALL=$loc
  out+=("$(java -cp java T)" "$(cs/out/tt)" "$(c/t)" "$(go/t)" "$(python3 -I t.py)" "$(node t.js)" "$(bash t.sh)")
done
printf '%s\n' "${out[@]}" | python3 -I summarize.py | tee ../results/results.txt
rm -rf cs/obj cs/bin cs/out java/T.class c/t go/t
