"""Compare keyboard layouts on real text: rows, hands, fingers, alternation, travel.

Layouts are taken from xkb (/usr/share/X11/xkb/symbols/tr, us). Geometry: ISO
staggered rows, 1 key unit = 19.05 mm. Standard touch-typing finger assignment.
"""
import collections, math, re, sys, json

ROWS = {  # letters per physical key, row name -> list of 12 keys (AD/AC) or 10 (AB)
    "trq": {
        "AD": list("qwertyuıopğü"),
        "AC": list("asdfghjklşi") + [","],
        "AB": list("zxcvbnmöç."),
    },
    "trf": {
        "AD": list("fgğıodrnhpqw"),
        "AC": list("uieaütkmlyşx"),
        "AB": list("jövcçzsb.,"),
    },
    "us": {
        "AD": list("qwertyuiop[]"),
        "AC": list("asdfghjkl;'") + ["\\"],
        "AB": list("zxcvbnm,./"),
    },
    "dvorak": {
        "AD": list("',.pyfgcrl/="),
        "AC": list("aoeuidhtns-") + ["\\"],
        "AB": list(";qjkxbmwvz"),
    },
}
ROW_Y = {"AD": 0.0, "AC": 1.0, "AB": 2.0}
ROW_X0 = {"AD": 1.5, "AC": 1.75, "AB": 2.25}  # left edge of first key, in key units
# finger by column index (0-based) for AD/AC rows; AB uses same columns
FINGER = {0: "LP", 1: "LR", 2: "LM", 3: "LI", 4: "LI", 5: "RI", 6: "RI", 7: "RM", 8: "RR", 9: "RP", 10: "RP", 11: "RP"}
HOME_COL = {"LP": 0, "LR": 1, "LM": 2, "LI": 3, "RI": 6, "RM": 7, "RR": 8, "RP": 9}
MM = 19.05


def keypos(row, col):
    return (ROW_X0[row] + col + 0.5, ROW_Y[row])


def build(layout):
    m = {}
    for row, keys in ROWS[layout].items():
        for col, ch in enumerate(keys):
            f = FINGER[col]
            m[ch] = dict(row=row, col=col, finger=f, hand=f[0], pos=keypos(row, col))
    return m


def home_pos(f):
    return keypos("AC", HOME_COL[f])


def tr_lower(s):
    return s.replace("I", "ı").replace("İ", "i").lower()


def letters_tr(text):
    text = tr_lower(text)
    text = text.replace("â", "a").replace("î", "i").replace("û", "u")
    return text


TR_ALPHA = set("abcçdefgğhıijklmnoöprsştuüvyzqwx")
EN_ALPHA = set("abcdefghijklmnopqrstuvwxyz")


def words(text, alpha):
    return re.findall("[" + "".join(sorted(alpha)) + "]+", text)


def analyze(ws, layout):
    if not isinstance(ws, collections.Counter):
        ws = collections.Counter(ws)
    m = build(layout)
    n = 0
    rows = collections.Counter()
    fingers = collections.Counter()
    hands = collections.Counter()
    homekeys = 0
    dist = 0.0
    bigrams = alt = sfb = samekey = 0
    rowjump = 0
    for w, c in ws.items():
        prev = None
        for ch in w:
            k = m[ch]
            n += c
            rows[k["row"]] += c
            fingers[k["finger"]] += c
            hands[k["hand"]] += c
            if k["row"] == "AC" and k["col"] == HOME_COL[k["finger"]]:
                homekeys += c
            hx, hy = home_pos(k["finger"])
            dist += c * 2 * math.hypot(k["pos"][0] - hx, k["pos"][1] - hy)
            if prev is not None:
                bigrams += c
                if prev["hand"] != k["hand"]:
                    alt += c
                elif prev["finger"] == k["finger"]:
                    if prev is k:
                        samekey += c
                    else:
                        sfb += c
                if prev["hand"] == k["hand"] and {prev["row"], k["row"]} == {"AD", "AB"}:
                    rowjump += c
            prev = k
    pct = lambda x, d: round(100.0 * x / d, 1)
    return dict(
        letters=n,
        top=pct(rows["AD"], n), home_row=pct(rows["AC"], n), bottom=pct(rows["AB"], n),
        home_keys=pct(homekeys, n),
        left=pct(hands["L"], n), right=pct(hands["R"], n),
        fingers={f: pct(fingers[f], n) for f in ["LP", "LR", "LM", "LI", "RI", "RM", "RR", "RP"]},
        alternation=pct(alt, bigrams), same_finger=pct(sfb, bigrams), same_key=pct(samekey, bigrams),
        row_jumps=pct(rowjump, bigrams),
        travel_m_per_1000=round(dist * MM / 1000.0 * 1000 / n, 2),  # metres per 1000 letters
    )


if __name__ == "__main__":
    lang = sys.argv[1]
    files = sys.argv[2:]
    parts = []
    for f in files:
        with open(f, encoding="utf-8") as fh:
            for line in fh:
                parts.append(line.split("\t", 1)[-1])
    text = "".join(parts)
    if lang == "tr":
        ws = words(letters_tr(text), TR_ALPHA)
        out = {lay: analyze(ws, lay) for lay in ["trq", "trf"]}
    else:
        ws = words(text.lower(), EN_ALPHA)
        out = {lay: analyze(ws, lay) for lay in ["us", "dvorak"]}
    print(json.dumps(out, ensure_ascii=False, indent=1))
