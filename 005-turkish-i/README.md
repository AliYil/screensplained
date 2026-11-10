# 005 · This Turkish Letter Keeps Breaking the World's Software

Data, code and sources for the Screensplained video about the **Turkish I problem**: Turkish has a dotted İ and a dotless ı, and code that follows Turkish rules turns `TITLE` into `tıtle`.

▶️ **Watch the video:** https://www.youtube.com/watch?v=Ke-_V_XT5i4

## The Turkey test, 2026

Jeff Moser's "Turkey test" (2008) asks whether code still works on a computer set to Turkish. We ran its best-known part, the Turkish I, on seven languages' basic case functions: the ones a programmer reaches for first, without naming a language or locale.

**Run on 2026-10-26** on one Linux machine (Arch, glibc 2.44), once with `LANG=LC_ALL=tr_TR.UTF-8` and once with `en_US.UTF-8` as the control. **Re-run on 2026-11-10** with the same 14 results (Python 3.14.9 and Node 26.13.0 by then). The video shows the 2026-10-26 run.

| Language | Version | Function tested | `TITLE` → | `title` → | `FILE` = `file`? |
|---|---|---|---|---|---|
| Java | OpenJDK 17.0.21 | `toLowerCase()`, `toUpperCase()`, `.equals` after lowercasing | **tıtle** | **TİTLE** | **no** |
| C# | .NET 10.0.13 | `ToLower()`, `ToUpper()`, `string.Compare(a, b, ignoreCase: true)` | **tıtle** | **TİTLE** | **no** |
| C | glibc 2.44 | `tolower()`, `toupper()` byte by byte, `strcasecmp()` | **tItle** | **TiTLE** | **no** |
| Bash | 5.3.20 | `${var,,}`, `${var^^}` | **tıtle** | **TİTLE** | **no** |
| Python | 3.14.8 | `str.lower()`, `str.upper()` | title | TITLE | yes |
| JavaScript | Node 26.12.1 | `toLowerCase()`, `toUpperCase()` | title | TITLE | yes |
| Go | 1.27.3 | `strings.ToLower`, `strings.ToUpper`, `strings.EqualFold` | title | TITLE | yes |

With `en_US.UTF-8`, all seven give `title`, `TITLE` and "yes".

All results: [`results/results.json`](results/results.json) (and the plain table [`results/results.txt`](results/results.txt)).

## What these results do and don't show

On a computer set to Turkish, Java's and C#'s default case functions and Bash follow Turkish rules, and so do C's once a program switches to the computer's language (`setlocale`). So a program that compares English words by changing their case stops finding them. Python's, JavaScript's and Go's use the same rules everywhere. This compares the selected functions, not whole languages: every one of these languages also has the other kind.

- **Turkish rules are correct for Turkish text.** Java's and C#'s results aren't bugs in the languages; they are documented (Java's `String.toLowerCase()`: "This method is locale sensitive"). The bugs come from using them on text that isn't Turkish (commands, identifiers, protocol keywords, email addresses). Each of these languages has a locale-free version (`toLowerCase(Locale.ROOT)`, `ToLowerInvariant()`, `StringComparison.OrdinalIgnoreCase`).
- **How each program picks up the locale differs.** Java, .NET, Node and Bash take it from the environment when they start. A C program stays in the neutral "C" locale until it calls `setlocale(LC_ALL, "")`; the C test does that first, as does the Python test (whose `str.lower()` ignores it anyway). So the C row shows a C program that has switched to the computer's language; one that hasn't stays in the "C" locale and gives `title`.
- **C keeps the I:** in a UTF-8 Turkish locale, glibc's one-byte `tolower()` can't return `ı` (two bytes in UTF-8), so it leaves `I` alone (`tItle`), but `strcasecmp()` still says `FILE` and `file` differ. The wide-character functions follow Turkish rules (`towlower(L'I')` = U+0131).
- **One machine, one operating system.** Java and .NET take their default from the system's language on Windows and macOS too; the C and Bash results are glibc's (Linux), and other C libraries may differ.
- **The default functions only.** Every language here can do either kind of case change; the test asks which one you get without asking.
- **Not tested:** PHP (not installed; since PHP 8.2, December 2022, `strtolower()` and `strtoupper()` ignore the locale: RFC "Locale-independent case conversion"), Kotlin (since 1.5, May 2021, `uppercase()`/`lowercase()` ignore it; the old `toUpperCase()` is deprecated).
- **Other surprises, not counted above:** Python's `"İ".lower()` gives two characters (`i` + a combining dot), as Unicode's default rules say. `"mıke".upper() == "mike".upper()` is `True` in Python, the kind of case-mapping collision behind the 2016 GitHub password-reset bug (GitHub hasn't said which function it used). Go's `EqualFold("mıke", "mike")` is `false`.

## Rerun it

Needs a Linux machine with the `tr_TR.UTF-8` and `en_US.UTF-8` locales generated, and Java (JDK), .NET SDK 10, gcc, Go, Python 3 and Node on the path.

```bash
bash analysis/run.sh    # builds each test, runs it under both locales, writes results/
```

## Claims in the video and their sources

"The papers said" means the account comes from Turkish newspaper reports of a prosecutor's indictment; we did not see the indictment itself.

| Claim in the video | Source |
|---|---|
| Programmers call it "the Turkish I problem"; Microsoft calls it "the canonical example" | [Microsoft, "Best practices for comparing strings in .NET"](https://learn.microsoft.com/en-us/dotnet/standard/base-types/best-practices-strings); [Jeff Atwood (2008)](https://blog.codinghorror.com/whats-wrong-with-turkey/) |
| Little boxes where the i's should be in game menus; the game turns menu text into capitals with Turkish rules, and its font has no İ | [Unity forum (2020)](https://discussions.unity.com/threads/lowercase-i-sc-flag-fails-to-render-with-tr-tr-culture.882457/); [a game developer on Steam (2020)](https://steamcommunity.com/app/1173590/discussions/0/2269195350119365224); [player reports on Steam, 2020–2025](https://steamcommunity.com/app/1161580/discussions/1/2974027084073745709). "Almost every Unity game I played" is the narrator's own experience |
| The fix shared on Turkish forums: set the Windows region format to English | The Steam reports above; Turkish forums (Technopat 2022, PC Hocası 2023) |
| 1928: the Latin alphabet, with İ i and I ı as separate letters | [Law No. 1353 and its table of letters](https://www.mevzuat.gov.tr/MevzuatMetin/1.3.1353.pdf) |
| Turkish and Azerbaijani pair I with ı and İ with i | Unicode `SpecialCasing.txt` ("Turkish and Azeri"); Microsoft (above) |
| ASCII, the American code in use since the sixties, has one pair, I and i | ASA X3.4-1963 (capitals only); the 1967 revision added small letters |
| Older Turkish encodings kept I and i and added İ and ı | ISO/IEC 8859-9 (1989); [Unicode FAQ](https://www.unicode.org/faq/casemap_charprop.html) |
| In the nineties, people asked Unicode for two Turkish letters of their own; Unicode said no; today's reason: "intolerably difficult" | [John Cowan's proposal (1997)](https://www.unicode.org/mail-arch/unicode-ml/Archives-Old/UML009/0619.html) and [Mark Davis's reply](https://www.unicode.org/mail-arch/unicode-ml/Archives-Old/UML009/0624.html); [Unicode FAQ](https://www.unicode.org/faq/casemap_charprop.html) |
| Java's manual has used `TITLE` → `tıtle` as a warning since 2006 | [`String.toLowerCase()`, Java SE 21](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html); the Java SE 6 docs as archived on 25 Apr 2006 |
| Google's Android tools flag it | [Android lint, "DefaultLocale"](https://googlesamples.github.io/android-custom-lint-rules/checks/DefaultLocale.md.html) |
| 2002: PHP couldn't find a class called InfoOracle when the program was switched to Turkish; a fix that held came almost ten years later | [PHP bug #18556](https://bugs.php.net/18556) (fixed for PHP 5.5, 2012) |
| 2008: Jeff Moser's "Turkey test"; "If your code properly runs in Turkey, it'll probably work anywhere." | [Moser (2008)](https://www.moserware.com/2008/02/does-your-code-pass-turkey-test.html) |
| 2008: Jeff Atwood, "What's Wrong With Turkey?" | [Atwood (2008)](https://blog.codinghorror.com/whats-wrong-with-turkey/) |
| 2012: a Lucene developer: Turkish IT specialists advise any locale but Turkish | [Uwe Schindler (2012)](https://blog.thetaphi.de/2012/07/default-locales-default-charsets-and.html) |
| 2016: Kotlin's build tools didn't recognise INFO on Turkish computers | [KT-13631](https://youtrack.jetbrains.com/issue/KT-13631); [Kotlin forum (2016)](https://discuss.kotlinlang.org/t/kotlin-build-error/1560) |
| 2022: curl crashed on Red Hat Linux set to Turkish; OpenSSL's CAMELLIA ≠ camellia | [Red Hat Developer (2022)](https://developers.redhat.com/articles/2022/06/15/openssl-30-dealing-turkish-locale-bug) |
| The text-message alphabet had ö and ü but not ı, ğ or ş; messages with them fell back to 70 characters | 3GPP TS 23.038; CR 0017 (CP-080223); [Habertürk (2007)](https://www.haberturk.com/ekonomi/teknoloji/haber/37284-turkce-karakterli-smste-fazla-kontore-son) |
| October 2007: "don't use these letters" when texting; the regulator's announced deadline of July 2008 (in force July 2009) | İHA via memurlar.net (6 Oct 2007); Habertürk (2007); Hürriyet (2009) |
| March 2008: the standard added national alphabets; Turkish is language number one; Spanish with it, Portuguese later that year, ten languages of India in 2009 | [3GPP TS 23.038 / ETSI TS 123 038 V9.1.1](https://www.etsi.org/deliver/etsi_ts/123000_123099/123038/09.01.01_60/ts_123038v090101p.pdf), table of national language identifiers and change history |
| Ankara, 2007: a couple arguing by text; her phone showed his ı's as i's and a word read as an insult; the fight that followed (the papers said) | [Hürriyet (21 Apr 2008)](https://www.hurriyet.com.tr/gundem/kucucuk-bir-nokta-tam-5-kisiyi-yakti-8748359); [Habertürk (21 Apr 2008)](https://www.haberturk.com/yasam/haber/68975-i-harfi-cinayeti). Attributed throughout; the names are left out |
| 2016: GitHub's password reset matched mike@ with mıke@; reported by John Gracey; fixed by checking the address matches the account | [GitHub Bug Bounty, @jagracey](https://bounty.github.com/researchers/jagracey.html) (described there by Nov 2016) |
| 2019: a write-up reached a Django developer; Django fixed the same kind of hole three weeks later | [The write-up (28 Nov 2019)](https://web.archive.org/web/20210114183105/https://eng.getwisdom.io/hacking-github-with-unicode-dotless-i/); [Django security releases (18 Dec 2019, CVE-2019-19844)](https://www.djangoproject.com/weblog/2019/dec/18/security-releases/) |
| Unicode's standard rule for capitals turns ı into I in every language | Unicode `UnicodeData.txt` (U+0131 → U+0049); this folder's test (Python) |
| PostgreSQL's code: Turkish "may do strange things with 'i' and 'I'" | [`scansup.c`](https://github.com/postgres/postgres/blob/master/src/backend/parser/scansup.c) |
| 2021: Kotlin added new case functions and began phasing out the old ones ("Obviously KOTLIN, you would say…") | [Kotlin 1.5.0-RC (2021)](https://blog.jetbrains.com/kotlin/2021/04/kotlin-1-5-0-rc-released/) |
| 2022: PHP's case functions stopped following the computer's language | [PHP RFC, "Locale-independent case conversion"](https://wiki.php.net/rfc/strtolower-ascii) (PHP 8.2) |
| The Turkey test results | This folder |

### Checked and left out

- A 2026 report blaming JavaScript's `toLowerCase()` for a Turkish-I bug: our test shows Node ignores the Turkish locale, so the case stays out.
- "Fixed in PHP 7.2" (a 2018 comment on the PHP bug): the maintainers say 5.5.
- A widely shared English version of the Ankara case with details the Turkish reports don't have: only the Turkish reports are used.

## Corrections

None yet. Before recording, the script was independently fact-checked; that check led us to drop a wrong date for ASCII's small letters (1967, not 1963), say GitHub's hole was *reported* in 2016 and needed an address at the victim's own email service, give July 2008 as the regulator's *announced* deadline, call the Bash shell by name, and attribute the Ankara case to the newspapers throughout.

Found a mistake? [Open an issue](../../../issues).
