# Web stranica: izvor

Stranice (`index.html` i `<jezik>/index.html`) nastaju iz jednog predloška i jedne datoteke s
tekstovima po jeziku. Gotove stranice su obični statični HTML za GitHub Pages i idu u repozitorij.

- `template.html.j2` – izgled stranice
- `i18n/<jezik>.json` – tekstovi; `en.json` je izvor, ostali moraju imati iste ključeve
- `build.py` – izrada svih stranica
- stil: `assets/site.css`, slike `assets/img/`, fontovi `assets/fonts/`

Nakon promjene teksta ili predloška:

    pip install jinja2
    python3 tools/site/build.py

Ne uređuj generirane `index.html` datoteke ručno. Snimke ekrana postoje za engleski i hrvatski;
ostali jezici koriste engleske (`IMAGES` u `build.py`).
