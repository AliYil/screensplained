# 002 · Turkey Designed a Keyboard for Turkish. QWERTY Won Anyway.

Data, code and sources for the Screensplained video about the Turkish **F keyboard** (1955) and why most people in Turkey type on **Turkish Q** instead.

▶️ **Watch the video:** https://www.youtube.com/watch?v=VMBXn1zRJk4

## What we measured

We took **26,227,575 letters** of Turkish text and asked: *if a touch typist typed all of it, how would the work be spread over the keyboard on Turkish Q and on Turkish F?*

| Measure | Turkish Q | Turkish F |
|---|---:|---:|
| Letters typed on the **8 resting keys** (where the fingers rest) | 33.0% | **51.3%** |
| Letters typed on the whole middle row | 44.1% | 58.4% |
| Letters on the top row / bottom row | 37.4% / 18.5% | 30.7% / 10.9% |
| Letters typed by the **pinkies** (left + right) | 27.2% (13.2 + 14.0) | **9.2%** (3.7 + 5.5) |
| Consecutive letter pairs *inside words* that **switch hands** | 48.8% | **79.0%** |
| Pairs typed by the same finger (different keys) | 8.8% | 5.9% |
| Same-hand jumps between top and bottom row | 8.7% | 1.6% |
| **Left / right hand** share of letters | 47.4% / 52.6% | **49.0% / 51.0%** |
| Finger travel, simple there-and-back model (metres per 1,000 letters) | 29.1 | 20.9 |

**One word as an example: *kelime* ("word").** On F all six letters sit on resting keys and the hands alternate on every letter (5 of 5 switches). On Q, four of the six letters need a reach, and the hands switch 3 times out of 5.

**The 49 / 51 split** is explained step by step, letter by letter, in [`hand-balance-49-51.md`](hand-balance-49-51.md).

All numbers: [`results/layout-stats.json`](results/layout-stats.json) (`metrics.trq` = Q, `metrics.trf` = F; per-letter frequencies in `letter_freq_pct`; per-key shares in `layouts`).

## What these numbers do and don't show

- They measure **where the letters are**, under standard touch-typing finger assignments. They are **not** a typing-speed, accuracy or comfort test, and they say nothing about how fast real people type on either layout.
- **Letters only**: spaces, digits, punctuation, Shift, Enter and corrections are not counted. "Pinkies type 27%" means 27% of the *letter* keystrokes.
- They describe **this text sample** (news, Wikipedia, websites, 2019–2022). Other kinds of text give somewhat different numbers; for example, the ranking of dotted *i* as the 3rd most common letter is specific to this sample.
- "Switch hands" counts consecutive letters **within words** only, not across spaces or punctuation.
- The model is for physical keyboards and touch typing, not phones.
- The 49 / 51 match holds **after rounding to one decimal place** (unrounded: 49.001% / 50.998%).

## Method

1. **Text:** three corpora from the [Leipzig Corpora Collection](https://wortschatz.uni-leipzig.de/en/download/Turkish): `tur_news_2022_100K`, `tur_wikipedia_2021_100K`, `tur-tr_web_2019_100K`, pooled.
2. **Cleaning:** Turkish-aware lowercasing (`I → ı`, `İ → i`, then lowercase), circumflexes folded (`â/î/û → a/i/u`), only the 29 Turkish letters plus q, w, x kept; words are runs of those letters.
3. **Layouts:** Turkish Q (`basic`) and Turkish F (`f`) from xkeyboard-config `symbols/tr`, the definitions Linux uses.
4. **Geometry and fingers:** ISO staggered rows, 1 key = 19.05 mm; standard touch-typing assignment (on each row the first five letter keys are left-hand, the rest right-hand; index fingers cover two columns, the right pinky the outer columns).
5. **Metrics:** each letter adds to its row, finger and hand; each pair of consecutive letters inside a word counts as alternating (different hands), same-finger, same-key or a top↔bottom jump. "Resting keys" = the 8 home keys under the fingers (not the whole middle row).

**Calibration:** the same code on English news (`eng_news_2020_100K`) gives US QWERTY 33% / Dvorak 70% of letters on the home row, matching the commonly cited figures ([`results/english-calibration.json`](results/english-calibration.json)).

## Rerun it

```bash
# 1. Download and unpack the corpora (https://downloads.wortschatz-leipzig.de/corpora/<name>.tar.gz)
for c in tur_news_2022_100K tur_wikipedia_2021_100K tur-tr_web_2019_100K; do
  curl -LO https://downloads.wortschatz-leipzig.de/corpora/$c.tar.gz && tar xzf $c.tar.gz
done
# 2. Metrics for Q and F (Python 3, no dependencies)
python3 analysis/layouts.py tr */*-sentences.txt
# 3. Letter frequencies and each letter's key on Q and F
python3 analysis/freq.py */*-sentences.txt
```

The corpus files are not included here (they are large and keep their own license).

## Claims in the video and their sources

"As Yener told it" means the story rests on İhsan Sıtkı Yener's own later account; we found no contemporary record for it.

| Claim in the video | Source |
|---|---|
| Paris 1965: a Turkish typist (Ece Özbayrak) becomes world champion; 5,370 keystrokes in 10 minutes | Milliyet, 30 Jul 1965 ([archive](https://www.gastearsivi.com/gazete/milliyet2/1965-07-30/1)); Intersteno eNews 112, pp. 32–33 |
| According to her teacher, the French protested that the keyboard was built for the competition; after 6 hours: "then build your own" | Yener, interview in Hürriyet (2003) (as Yener told it); reproduced in [this paper, PDF p. 13](https://dergipark.org.tr/tr/download/article-file/31298) |
| QWERTY's order was set in America in the 1870s | Sholes & Glidden typewriter, 1874 ([Smithsonian](https://americanhistory.si.edu/collections/object/nmah_850542)) |
| 1955: the government made F the official standard; most people never switched (2021 estimate: 5–10% use F) | [Intersteno Türk, part 2](https://www.interstenoturk.org/f-klavyenin-hikayesi-bolum-2-klavye-inkilabi/); [Tiro / Intersteno (2021)](https://tiro.intersteno.org/2021/12/the-f-keyboard-the-history-and-contemporary-use-of-the-turkish-standard-keyboard-layout/) |
| 1928: Latin alphabet; new letters Ç Ğ Ö Ş Ü and two i's | [TDK](https://tdk.gov.tr/icerik/yazim-kurallari/ses-harf-ve-alfabe/) |
| Manufacturers placed Turkish letters differently; an early standard didn't stick; "maybe 70" layouts | Yener, Hürriyet (2003) (as Yener told it); Intersteno Türk, part 2 |
| 1946: Yener, a young typing teacher in Istanbul; students failed on other layouts; employers called their speeds fake | [Intersteno Türk, part 1](https://www.interstenoturk.org/f-klavyenin-hikayesi-bolum1-turk-milli-klavyesi/); Tiro |
| Early 1950s: meetings with the education minister and the president: "Make a scientific keyboard, and we'll accept it" | Yener, Hürriyet (2003) (as Yener told it) |
| The spelling dictionary: 29,934 words, 183,596 letters counted; doctors and hand X-rays | Intersteno Türk, part 1 |
| A (most common) under the left index finger; J (rarest) bottom-left under the left pinky | xkeyboard-config; our analysis |
| Every vowel on the left hand, only consonants on the right; two American professors checked alternation with − and + | Intersteno Türk, part 2 |
| 20 October 1955: approved unanimously by a government committee | Intersteno Türk, part 2 |
| Typing-school typewriters converted in one semester; from 1963 the customs rule only let in F typewriters | Yener, Hürriyet (2003); [Anadolu Agency (2015)](https://www.aa.com.tr/en/turkey/keyboard-warriors-battle-for-turkish-typists-heats-up/70320) |
| 1948: first national champion Ece Özbayrak, title kept 10+ years; 1957: first world championships | [Intersteno eNews 112](https://www.intersteno.org/docs/enews/enews112.pdf), pp. 32–33; Tiro |
| 2025 online world contest: Turkish typists won all three youth categories in the mother-tongue competition | Intersteno eNews 112, p. 7 |
| All analysis numbers (resting keys, pinkies, alternation, 49 / 51) | This folder |
| Yener's 49 / 51 target | Later accounts, e.g. Tiro (2021) |
| "In 1963, we were not aware of computers…" and "It is like a smoking addiction…" | Anadolu Agency (2015), quoted verbatim |
| 1980s: PCs arrived with American keyboards; 1991: TSE updated F for computers | Tiro |
| Lock-in | Paul David, "Clio and the Economics of QWERTY" (1985); for the counter-argument, Liebowitz & Margolis, "The Fable of the Keys" (1990) |
| 2003: Ministry of Education circular to use F in schools | Circular 2003/20 ([parliamentary record](https://www5.tbmm.gov.tr/tutanaklar/TUTANAK/TBMM/d24/c018/tbmm24018092.pdf)) |
| 2013: public institutions to switch to F by the end of 2017 | Prime Ministry Circular 2013/13, [Official Gazette 28847](https://www.resmigazete.gov.tr/eskiler/2013/12/20131210-9.htm) |
| Feb 2018: an MP: "Right now, we don't know how far the switch has gone" (our translation) | [Habertürk (2018)](https://www.haberturk.com/f-klavye-zorunlu-mu-oldu-turk-icadi-f-klavye-icin-yeni-aciklama-1834059-ekonomi) |
| Court clerks can now take their typing exam on Q | Ministry of Justice recruitment announcements (2023, 2025) |
| Yener died in 2016 | [Anadolu Agency (2016)](https://www.aa.com.tr/tr/gunun-basliklari/f-klavyenin-mucidi-yener-hayatini-kaybetti/639901) |
| F is built into Windows, macOS and Linux | [Microsoft](https://learn.microsoft.com/en-us/globalization/keyboards/kbdtuf), [Apple](https://support.apple.com/en-ae/102743), xkeyboard-config |

### Checked and left out

- "QWERTY was designed to slow typists down": disputed.
- "F is 11% faster than Q": repeated in Turkish sources, but we couldn't find the original study.
- "43 million lira saved per year": sources conflict.

## Corrections

None yet. Before publishing, the script was independently fact-checked; that check led us to attribute the French protest to Yener, date the 5–10% figure to 2021, limit the 2025 results to the mother-tongue competition, and state that the analysis doesn't measure typing speed.
