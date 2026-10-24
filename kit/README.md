# ErgBeat – paket za web stranicu

Sve što treba za izradu prave web stranice za ErgBeat, na jednom mjestu. Napravljeno 24. 10. 2026.
(aplikacija 0.61). Slike su prave snimke aplikacije: osam tjedana simuliranog treninga kroz pravi
engine aplikacije (`StoreShotsTest` u repozitoriju `deganegane/echo-erg`).

## Cilj

Jednostavna, brza stranica koja objašnjava što ErgBeat radi i vodi na Google Play. Do izlaska
na Play (nakon zatvorenog testiranja) može služiti i za skupljanje testera.

- **Publika:** ljudi koji kod kuće ili u CrossFit boxu treniraju na veslačkom ergometru (Concept2,
  Rogue Echo i drugi FTMS veslači), često s Garmin satom.
- **Ton:** kratko, konkretno, bez marketinških superlativa. Aplikacija je alat, ne lifestyle.
- **Glavna poruka:** veslaj po planu, uz pacer koji se vidi s druge strane sobe; tvoji podaci ostaju
  na tvom mobitelu.

## Tehnički okvir (obavezno)

- **Hosting:** GitHub Pages iz ovog repozitorija (`deganegane/ergbeat`, grana `main`, korijen).
  Adresa: https://deganegane.github.io/ergbeat/
- **`/privacy.html` mora ostati na istoj adresi.** Ta je adresa upisana u Google Play Console
  (App content → Privacy policy) i u trgovini. Sadržaj mora odgovarati `PRIVACY.md` u
  `deganegane/echo-erg` (EN pa HR, odvojeno s `---`). Trenutnu stranicu radi
  `tools/site/build.py` u tom repozitoriju; nova stranica može preuzeti izgled, ali ne smije
  promijeniti tekst bez promjene u `PRIVACY.md`.
- **Bez praćenja:** nema analitike, kolačića, trackera ni vanjskih zahtjeva (fontovi su lokalni u
  `kit/fonts/`, nema Google Fontsa ni CDN-a). Stranica obećava privatnost, pa mora i sama biti
  takva.
- **Statično:** čisti HTML i CSS (malo JS-a po potrebi), bez build koraka. `.nojekyll` ostaje.
- **Jezici:** engleski (zadano, `/`) i hrvatski (`/hr/`). Aplikacija ima 9 jezika; ostali mogu doći
  kasnije.
- **Mobilni prvo**, svijetla i tamna tema (`prefers-color-scheme`), pristupačnost (alt tekstovi,
  kontrast, fokus).
- **Slike:** ovdje su PNG originali; za stranicu ih pretvoriti u WebP/AVIF i smanjiti
  (npr. 600–800 px širine za telefone).

## Dizajn

Isti jezik kao aplikacija i Play stranica: tamni grafit s volt-zelenim naglaskom.

| Uloga | Boja |
|---|---|
| Pozadina (tamna) | `#121316`, gradijent junaka `#2E3034 → #1A1B1E → #121316` |
| Površine (tamna) | `#1E2022`, `#282A2D`, rub `#42474E` |
| Tekst (tamna) | `#E2E2E6`, sekundarni `#C2C7CF` / `#B8BDC5` |
| **Volt (naglasak)** | `#B5E52D` (na tamnom), `#BDEE36` gumbi na svijetlom, tekst na svijetlom `#557A00` |
| Pozadina (svijetla) | `#F9F9FC`, tekst `#1A1C1E`, sekundarni `#42474E` |
| U zoni / prejako / prelagano | `#3DDC84` / `#FF6B5C` / `#5CA8FF` |
| Vati (snaga) | `#B79CFF` |

- **Font:** Space Grotesk (Regular, Medium, Bold) u `kit/fonts/` kao WOFF2, licenca OFL (`OFL.txt`
  mora ići uz fontove).
- **Ikona:** `brand/icon-rounded.svg` (zaobljena), `brand/icon-square.svg` (puna, za favicon i
  maske), `brand/mark.svg` (samo motiv, prozirna pozadina), PNG `icon-512.png`.
- **Uzor stila:** `screenshots/store/` (natpis iznad telefona) i `brand/feature-graphic-*.png`.
- Telefoni bez tuđeg okvira uređaja: tamni zaobljeni okvir kao na Play snimkama.

## Predložene sekcije

1. **Junak:** ikona + „ErgBeat”, naslov, podnaslov, gumb **Get it on Google Play** (do izlaska:
   „Postani tester”), snimka live ekrana.
2. **Kako radi:** spoji veslač → odaberi trening → veslaj prema paceru.
3. **Live ekran:** pacer u obliku luka, zone tempa, duh najboljeg treninga, glas i metronom;
   uspravno i položeno (`screenshots/landscape/`).
4. **Treninzi i programi:** 21 trening, četiri programa, editor.
5. **Napredak:** tjedni cilj, rekordi, procjena 2k, grafovi.
6. **Garmin:** besplatna Connect IQ aplikacija, popis satova.
7. **Sprave:** FTMS veslači, Concept2 PM5, pulsometri.
8. **Privatnost:** bez računa, bez oglasa, bez praćenja; link na pravila.
9. **Besplatno i Pro:** usporedba, cijene.
10. **FAQ.**
11. **Podnožje:** podrška, pravila privatnosti, izjava o neovisnosti.

Tekstovi za sve sekcije: `copy/en.md` i `copy/hr.md`.

## Činjenice (provjereno u kodu, 0.61)

- **Naziv:** ErgBeat. Paket na Playu: `com.kriative.ergbeat`.
- **Link na Play** (radi tek kad je aplikacija javna):
  https://play.google.com/store/apps/details?id=com.kriative.ergbeat
- **Prijava za testere** (zatvoreno testiranje, kad bude postavljeno):
  https://play.google.com/apps/testing/com.kriative.ergbeat
- **Podrška:** jaan.dsgn@gmail.com. Druge e-adrese ne objavljivati.
- **Android 8.0+** (minSdk 26).
- **Sprave:** Bluetooth FTMS veslači (testirano na Rogue Echo Roweru); Concept2 PM5 (duljina
  zaveslaja, vršna sila, krivulja sile; podrška napravljena, još nije isprobana na pravom PM5);
  puls s prsnog pojasa ili sa sata koji emitira puls.
- **Garmin (Connect IQ, besplatno):** fēnix 8 (43 mm, 47 mm, Pro 47 mm, Solar 47 mm i 51 mm),
  Forerunner 965, Forerunner 265. Aplikacija još nije objavljena u Connect IQ trgovini.
- **Besplatno:** spajanje sprava, slobodno veslanje, 4 treninga (20 min ravnomjerno, 10 × 1 min,
  4 × 500 m, 2k test), live ekran sa zadanim karticama, pacer, glas i metronom, povijest, tjedni
  cilj i niz, Health Connect, podsjetnici, dijeljenje treninga (link/QR), sigurnosna kopija,
  Garmin sat.
- **Pro:** svih 21 trening, 4 programa (EN: Foundations, Build, Peak, CrossFit Engine; HR: Temelji,
  Izgradnja, Vrhunac, CrossFit kondicija), editor i
  generator intervala, duh, rekordi, napredak i statistika, trening sa snagom (FTP, zone), FIT/CSV
  izvoz (Garmin Connect, Strava, intervals.icu), odabir kartica na live ekranu.
- **Cijene (osnovne, bez PDV-a):** 3,99 €/mjesec, 24,99 €/godina, 49,99 € jednokratno zauvijek.
  Google Play dodaje PDV po zemlji; u Hrvatskoj kupac vidi 4,99 € / 30,99 € / 59,99 €.
  Na stranici je sigurnije pisati „od 3,99 € mjesečno” uz napomenu da točnu cijenu pokazuje
  Google Play, ili cijene izostaviti.
- **Privatnost:** bez računa, oglasa, analitike i trackera; podaci samo na mobitelu; aplikacija ne
  šalje podatke na internet (izvoz, dijeljenje i kopije radi korisnik sam).
- **Jezici aplikacije:** engleski, hrvatski, njemački, španjolski, francuski, talijanski,
  portugalski (Brazil), poljski, nizozemski.
- **Pravno:** ErgBeat nije povezan s tvrtkama Rogue Fitness, Concept2 ni Garmin. Njihova imena se
  smiju spominjati kao opis kompatibilnosti, ali bez njihovih logotipa i bez fotografija njihovih
  proizvoda u prvom planu. Ova izjava ide u podnožje.

## Sadržaj paketa

```
kit/
  README.md                 ovaj opis
  copy/en.md, copy/hr.md    tekstovi za stranicu
  brand/                    ikone (SVG, PNG), feature graphic EN/HR
  fonts/                    Space Grotesk WOFF2 + OFL.txt
  screenshots/
    phone/en-dark/          8 ekrana, 1233×2193 (telefon 9:16), engleski, tamna tema
    phone/hr-dark/          isto na hrvatskom
    phone/en-light/         isto, svijetla tema
    landscape/              live ekran položeno, 2673×1233 (telefon 20:9), tamno i svijetlo
    store/en, store/hr      gotove Play snimke s natpisima, 1080×1920
    watch/                  Garmin ekrani (500×500) i hero slike
    extra/                  ostale snimke, 1233×2673 (20:9): auto pauza, brze postavke, čekanje
                            prvog zaveslaja, preimenovani trening, editor tamno/svijetlo, postavke
```

Ekrani u `phone/*`:

| Datoteka | Što pokazuje |
|---|---|
| `1-live.png` | Live ekran: 5 × 1000 m, treći interval, u zoni, +36 m ispred duha |
| `2-training.png` | Početni ekran: spojen veslač i puls, današnji trening iz programa |
| `2-workouts.png` | Popis teških treninga (intervali, sprintovi, WOD-ovi) |
| `3-program.png` | Program „Izgradnja”: tjedan 1 gotov, sljedeći dan |
| `4-progress.png` | Napredak: tjedni cilj, volumen, procjena 2k |
| `5-history.png` | Povijest: zbroj, osobni rekordi, zadnji trening |
| `6-session.png` | Detalji 2k testa: split, puls, graf |
| `7-editor.png` | Editor: veslanje i wall ball (CrossFit stil) |

## Kako ažurirati slike

Snimke nastaju u CI-u repozitorija `deganegane/echo-erg` pri svakom buildu i završe na grani
`ui-shots` (`store/<jezik>/`). Play snimke s natpisima radi `tools/play_store/make.py`. Za novu
verziju paketa: preuzeti granu `ui-shots` i zamijeniti datoteke ovdje.
