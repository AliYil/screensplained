# How we got 49.0% / 51.0% (the F keyboard's left/right hand split)

In video 002 (at about 6:21) the narration says:

> Yener said his keyboard was designed to split the work between the hands: forty-nine percent left, fifty-one right. Seven decades later, on modern Turkish text, I got forty-nine point zero, and fifty-one point zero.

This document explains where the two numbers come from, how they were calculated, and what they do and don't mean.

## The short version

1. We took **26,227,575 letters** of Turkish text from three public corpora (news, Wikipedia, websites; 2019–2022).
2. We counted how often each of the 32 letters appears.
3. For each letter we looked up **which hand types it** on the Turkish F keyboard, using the standard touch-typing finger assignment.
4. We added up the shares per hand: **left 49.001%, right 50.998%**. Rounded to one decimal place, that is **49.0% / 51.0%**.

So it isn't a typing test. It answers this question: *if a touch typist typed this text on F, what share of the letter keystrokes would each hand make?*

## 1. The "49 / 51" target

The target comes from later accounts of how Yener and the 1955 committee designed the layout, e.g. the Tiro / Intersteno history ([link](https://tiro.intersteno.org/2021/12/the-f-keyboard-the-history-and-contemporary-use-of-the-turkish-standard-keyboard-layout/)). We did not find a document from 1955 itself that states it, which is why the narration says "Yener *said* his keyboard was designed to…" and not "in 1955 he promised…". (This wording came out of an independent fact-check of the script.)

## 2. The text

| Corpus (Leipzig Corpora Collection) | What it is |
|---|---|
| `tur_news_2022_100K` | 100,000 sentences of Turkish news, 2022 |
| `tur_wikipedia_2021_100K` | 100,000 sentences of Turkish Wikipedia, 2021 |
| `tur-tr_web_2019_100K` | 100,000 sentences of Turkish websites, 2019 |

The three are pooled into one body of text. Together they give **26,227,575 letters**.

## 3. Cleaning the text (letters only)

Done by [`analysis/layouts.py`](analysis/layouts.py) (`letters_tr` and `words`):

- **Turkish-aware lowercase:** `I → ı` and `İ → i` first, then lowercase everything. A plain lowercase would turn `I` into `i` and mix up the two Turkish i's.
- **Circumflexes folded:** `â → a`, `î → i`, `û → u` (they are typed with the same keys).
- **Only the 32 letters are kept:** the 29 Turkish letters plus q, w, x (they appear in names and loanwords).
- **Everything else is ignored:** spaces, digits, punctuation, Shift, Enter, Backspace. So the result is about **letter keystrokes**, not every key press.

## 4. Which hand types each letter

The F and Q layouts are read from the Linux keyboard definitions (`xkeyboard-config`, file `/usr/share/X11/xkb/symbols/tr`; "f" variant = F, basic = Q). Each key is given to a finger by the **standard touch-typing assignment**: on each row, the first five letter keys belong to the left hand and the rest to the right.

On F that gives this split:

| Hand | Letters on F |
|---|---|
| **Left** (15 letters) | all 8 vowels **A E I İ O Ö U Ü**, plus F G Ğ J V C Ç |
| **Right** (17 letters) | B D H K L M N P Q R S Ş T W X Y Z |

Every vowel being on the left is the design idea the video describes ("every vowel under the left hand").

## 5. Adding it up

Each letter's share of the 26.2 million letters, grouped by hand:

**F keyboard, left hand: 49.001%**

| Letter | Share of all letters | Key (row, finger) |
|---|---:|---|
| A | 11.822% | home, left index |
| E | 9.594% | home, left middle |
| İ / i | 8.758% | home, left ring |
| I / ı | 4.596% | top, left index |
| U | 3.027% | home, left pinky |
| O | 2.541% | top, left index |
| Ü | 1.795% | home, left index |
| G | 1.241% | top, left ring |
| V | 1.177% | bottom, left middle |
| Ç | 1.025% | bottom, left index |
| Ğ | 0.976% | top, left middle |
| C | 0.974% | bottom, left index |
| Ö | 0.789% | bottom, left ring |
| F | 0.577% | top, left pinky |
| J | 0.109% | bottom, left pinky |
| **Total** | **49.001%** | |

**F keyboard, right hand: 50.998%**

| Letter | Share of all letters | Key (row, finger) |
|---|---:|---|
| N | 7.435% | top, right middle |
| R | 7.039% | top, right index |
| L | 7.025% | home, right ring |
| K | 4.484% | home, right index |
| D | 4.275% | top, right index |
| T | 3.837% | home, right index |
| M | 3.524% | home, right middle |
| S | 3.256% | bottom, right index |
| Y | 3.016% | home, right pinky |
| B | 2.182% | bottom, right middle |
| Ş | 1.490% | home, right pinky |
| Z | 1.384% | bottom, right index |
| H | 1.047% | top, right ring |
| P | 0.945% | top, right pinky |
| W | 0.041% | top, right pinky |
| X | 0.014% | home, right pinky |
| Q | 0.004% | top, right pinky |
| **Total** | **50.998%** | |

The two totals add up to 99.999% instead of 100%, because each letter's share is stored rounded to three decimals.

**Result: left 49.001%, right 50.998% → 49.0% / 51.0%.**

## 6. For comparison: Turkish Q

The same text on Turkish Q gives **left 47.4%, right 52.6%** (47.417% / 52.582%). Q leans more on the right hand, mainly because the Turkish letters ı, Ğ, Ü, Ş, İ, Ö and Ç all sit on the right side (the "parked on the right edge" letters from the video).

<details>
<summary>Q per-letter tables</summary>

**Q keyboard, left hand: 47.417%**

| Letter | Share of all letters | Key (row, finger) |
|---|---:|---|
| A | 11.822% | home, left pinky |
| E | 9.594% | top, left middle |
| R | 7.039% | top, left index |
| D | 4.275% | home, left middle |
| T | 3.837% | top, left index |
| S | 3.256% | home, left ring |
| B | 2.182% | bottom, left index |
| Z | 1.384% | bottom, left pinky |
| G | 1.241% | home, left index |
| V | 1.177% | bottom, left index |
| C | 0.974% | bottom, left middle |
| F | 0.577% | home, left index |
| W | 0.041% | top, left ring |
| X | 0.014% | bottom, left ring |
| Q | 0.004% | top, left pinky |
| **Total** | **47.417%** | |

**Q keyboard, right hand: 52.582%**

| Letter | Share of all letters | Key (row, finger) |
|---|---:|---|
| İ / i | 8.758% | home, right pinky |
| N | 7.435% | bottom, right index |
| L | 7.025% | home, right ring |
| I / ı | 4.596% | top, right middle |
| K | 4.484% | home, right middle |
| M | 3.524% | bottom, right index |
| U | 3.027% | top, right index |
| Y | 3.016% | top, right index |
| O | 2.541% | top, right ring |
| Ü | 1.795% | top, right pinky |
| Ş | 1.490% | home, right pinky |
| H | 1.047% | home, right index |
| Ç | 1.025% | bottom, right ring |
| Ğ | 0.976% | top, right pinky |
| P | 0.945% | top, right pinky |
| Ö | 0.789% | bottom, right middle |
| J | 0.109% | home, right index |
| **Total** | **52.582%** | |

</details>

## 7. What these numbers do and don't show

- **They describe this text sample.** Another mix of texts (chat messages, novels, code) would give slightly different shares.
- **"Exactly" isn't justified.** The split matches 49 / 51 **after rounding to one decimal place**. Unrounded it is 49.001% / 50.998%, as close as you can reasonably get, but not exact.
- **"Seven decades later"** refers to the analysis year (2026) vs. 1955. The texts themselves are from 2019–2022.
- **It measures key placement, not typing speed.** It assumes standard touch-typing fingering and says nothing about how fast or accurately people actually type on either layout.
- **Letters only:** spaces, numbers, punctuation and modifier keys are not counted.
- **Phones:** the model is for physical touch typing and doesn't apply to phone keyboards.

## 8. Checking it yourself

- **Code:** [`analysis/layouts.py`](analysis/layouts.py) (the layout model and all metrics) and [`analysis/freq.py`](analysis/freq.py) (per-letter frequencies and key positions).
- **Saved results:** [`results/layout-stats.json`](results/layout-stats.json): `metrics.trf.left` / `.right` = 49.0 / 51.0, plus every letter's frequency in `letter_freq_pct`.
- **Re-running:** see [Rerun it](README.md#rerun-it). The raw corpus files are not included in this repository.
- **Independent check:** an independent fact-check recomputed the split from the saved letter frequencies and the xkb layout, and got the same 49.001% / 50.998%.
