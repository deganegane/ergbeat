#!/usr/bin/env python3
"""Build the ErgBeat website pages from one template and one text file per language.

    pip install jinja2
    python3 tools/site/build.py

Writes index.html (English) and <code>/index.html for every other language at the repository
root. The output is plain static HTML for GitHub Pages; commit it together with the sources.
Texts live in tools/site/i18n/<code>.json. Strings may contain simple HTML (<b>, <em>, <a>).
"""
import json
import pathlib

from jinja2 import Environment, FileSystemLoader, StrictUndefined

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
BASE = "https://deganegane.github.io/ergbeat/"
TESTER_URL = "https://play.google.com/apps/testing/com.kriative.ergbeat"
EMAIL = "jaan.dsgn@gmail.com"

# Same order as the language list in the app. "path" is relative to the site root.
LANGS = [
    {"code": "en", "html": "en", "og": "en_US", "short": "EN", "name": "English", "path": ""},
    {"code": "hr", "html": "hr", "og": "hr_HR", "short": "HR", "name": "Hrvatski", "path": "hr/"},
    {"code": "de", "html": "de", "og": "de_DE", "short": "DE", "name": "Deutsch", "path": "de/"},
    {"code": "es", "html": "es", "og": "es_ES", "short": "ES", "name": "Español", "path": "es/"},
    {"code": "fr", "html": "fr", "og": "fr_FR", "short": "FR", "name": "Français", "path": "fr/"},
    {"code": "it", "html": "it", "og": "it_IT", "short": "IT", "name": "Italiano", "path": "it/"},
    {"code": "pt", "html": "pt-BR", "og": "pt_BR", "short": "PT", "name": "Português (Brasil)", "path": "pt/"},
    {"code": "pl", "html": "pl", "og": "pl_PL", "short": "PL", "name": "Polski", "path": "pl/"},
    {"code": "nl", "html": "nl", "og": "nl_NL", "short": "NL", "name": "Nederlands", "path": "nl/"},
]

# Screenshots exist in English and Croatian; other languages use the English ones.
IMAGES = {
    "en": {"live": "live-en.webp", "landscape": "landscape-en.webp", "progress": "progress-en.webp",
           "trio": ["workouts-en.webp", "program-en.webp", "editor-en.webp"]},
    "hr": {"live": "live-hr.webp", "landscape": "landscape-en.webp", "progress": "progress-hr.webp",
           "trio": ["workouts-hr.webp", "program-hr.webp", "editor-hr.webp"]},
}

# The privacy policy has English and Croatian versions on one page.
PRIVACY = {"hr": "privacy.html#hr"}


def main():
    env = Environment(loader=FileSystemLoader(HERE), undefined=StrictUndefined,
                      autoescape=False, keep_trailing_newline=True)
    tpl = env.get_template("template.html.j2")
    en_keys = set(json.loads((HERE / "i18n" / "en.json").read_text("utf-8")))
    for lang in LANGS:
        t = json.loads((HERE / "i18n" / f"{lang['code']}.json").read_text("utf-8"))
        missing = en_keys - set(t)
        if missing:
            raise SystemExit(f"{lang['code']}.json is missing: {', '.join(sorted(missing))}")
        depth = lang["path"].count("/")
        html = tpl.render(
            t=t, lang=lang, langs=LANGS, root="../" * depth, base=BASE,
            img=IMAGES.get(lang["code"], IMAGES["en"]),
            og_image="og-hr.png" if lang["code"] == "hr" else "og-en.png",
            privacy_href=PRIVACY.get(lang["code"], "privacy.html"),
            tester_url=TESTER_URL, email=EMAIL,
        )
        out = ROOT / lang["path"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, "utf-8")
        print(f"{lang['code']}: {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
