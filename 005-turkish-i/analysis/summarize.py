# Collects run.sh's JSON lines into ../results/results.json and prints a table (results/results.txt).
import datetime, json, sys

rows = [json.loads(l) for l in sys.stdin if l.strip()]
json.dump({"run": datetime.date.today().isoformat(), "machine": "Linux (Arch), glibc locales tr_TR.UTF-8 and en_US.UTF-8",
           "results": rows}, open("../results/results.json", "w"), ensure_ascii=False, indent=1)
w = max(len(r["lang"]) for r in rows)
for r in rows:
    same = str(r["FILE_equals_file"]).lower()
    print(f'{r["lang"]:<{w}}  {r["locale"]:<12}  TITLE -> {r["lower_TITLE"]:<6}  title -> {r["upper_title"]:<6}  FILE = file: {same:<5}  {r["version"]}')
