# Turkey test, Python: str.lower() / str.upper(), after locale.setlocale(LC_ALL, "").
import json, locale, platform
loc = locale.setlocale(locale.LC_ALL, "")
print(json.dumps({"lang": "Python", "version": platform.python_version(), "locale": loc, "api": "str.lower() / str.upper()",
                  "lower_TITLE": "TITLE".lower(), "upper_title": "title".upper(), "FILE_equals_file": "FILE".lower() == "file"}, ensure_ascii=False))
