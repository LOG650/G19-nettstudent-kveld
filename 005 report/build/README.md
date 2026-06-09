# Bygging av rapport.pdf

Denne mappen inneholder byggskript og LaTeX-konfig for å konvertere
[../rapport.md](../rapport.md) til PDF.

## Forutsetninger

- `pandoc` (testet med 3.1.3)
- `lualatex` (TeX Live)
- `python3`

Apt-pakker:

```text
texlive-luatex texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended
```

`texlive-latex-extra` brukes for `seqsplit` og `newunicodechar`.

## Bygg PDF

Bygget er todelt: pandoc genererer en `.tex`, et etterbehandlingssteg
(`postprocess.py`) låser figurplassering og gjør tabeller om til ikke-brytbare,
radstrekede `tabular`-er, og til slutt kompilerer `lualatex`.

Kjør fra `005 report/` (eksempel for `rapport_final.md` i `014 fase 4 - report/`):

```bash
# 1) Preprosesser Markdown (figurer, HTML-tabeller, captions, display-ligninger)
python3 build/preprocess.py "../014 fase 4 - report/rapport_final.md" build/rapport_final_pdf.md

# 2) Pandoc → LaTeX (.tex, ikke PDF)
pandoc build/rapport_final_pdf.md -o build/rapport_final.tex --standalone \
  --pdf-engine=lualatex --resource-path=. \
  -V geometry:a4paper -V geometry:margin=2.5cm -V lang=nb-NO -V fontsize=11pt \
  --columns=120 \
  --include-in-header=build/header.tex \
  --lua-filter=build/tables.lua

# 3) Etterbehandle LaTeX: figure[H] + longtable → ikke-brytbar tabular m/ radlinjer
python3 build/postprocess.py build/rapport_final.tex

# 4) Kompiler (to passeringer) fra 005 report/ så bildestiene løses
lualatex -interaction=nonstopmode build/rapport_final.tex
lualatex -interaction=nonstopmode build/rapport_final.tex
mv rapport_final.pdf "../014 fase 4 - report/rapport_final.pdf"
```

`lualatex` kjøres fra `005 report/` slik at `extracted_images/…` og
`../006 analysis/…` løses, og legger `rapport_final.pdf` i arbeidskatalogen før den
flyttes til rapportmappa.

## Hva hver fil gjør

| Fil | Rolle |
|:---|:---|
| [preprocess.py](preprocess.py) | Kjøres på Markdown før pandoc. (1) HTML-figurblokker (`<div align="center"><img …></div>`) → Markdown image-syntaks. (2) HTML-tabeller med hierarkiske overskrifter (`<div …><table>…</table></div>`) → rå LaTeX-longtable via `pandoc -f html` + `tables.lua` (minipage-wrappere fjernes så `\multicolumn`-headere ikke sprenger sidebredden). (3) HTML-tabellbildetekster → pandoc-native caption (`: Tabell X.Y …`). (4) Frittstående display-ligninger (`$$ … \tag{3.x}$$`) → `equation`-miljø (så `\tag` virker i LaTeX). |
| [postprocess.py](postprocess.py) | Kjøres på den genererte `.tex` etter pandoc. (1) `\begin{figure}` → `\begin{figure}[H]` slik at figurene står i kilderekkefølge i stedet for å flyte. (2) Hver `longtable` → ikke-brytbar, sentrert `tabular` (splittes aldri) med `\midrule` mellom hver datarad (vannrette radlinjer); hierarkiske overskrifter og kolonnebredder beholdes. |
| [header.tex](header.tex) | LaTeX-preamble: `float` (for `[H]`), `multirow`, tabellinnstillinger, `microtype`, captionsetup (sentrert liten italic uten "Figur N:" / "Tabell N:" auto-prefiks), `pdflscape`, makroene `\splitcode` og `\splitword` (basert på `seqsplit`), og Unicode-mapping for ☐ ☒ − via `newunicodechar`. |
| [tables.lua](tables.lua) | Pandoc Lua-filter. Setter alle kolonnebredder til `1/n` (tvinger linjebryting), wrapper inline-kode i `\splitcode{}` globalt, og inne i tabellens body (ikke head/foot) wrapper også lange ord uten naturlige bryte-punkter i `\splitword{}`. Tabeller med ≥ 10 kolonner roteres til landskap. |
| `rapport_*_pdf.md`, `rapport_final.tex` | Mellomprodukter fra preprocess/pandoc. Ignorert i git. |

## Hvorfor disse valgene

- **Equal-width `p{}`-kolonner**: Markdown-tabeller med uniform `---`
  separator gir pandoc ingen breddeinformasjon, og default `l`/`c`/`r`
  kolonner _bryter ikke_ linjer — innholdet renner ut til høyre og
  overlapper med naboen. Lua-filteret tildeler `1/n` av sidebredden til
  hver kolonne, som tvinger pandoc til å bruke `p{...\textwidth}` med
  riktig linjebryting.
- **`\splitcode` for inline-kode**: Lange identifikatorer som
  `RandomForestRegressor` eller `fit_intercept=True` har ingen
  mellomrom eller bindestreker, så LaTeX kan ikke bryte dem og de
  renner over kolonnegrensen i smale tabellceller. `seqsplit` legger
  inn brytbare punkter mellom hvert tegn, slik at LaTeX kan dele
  tegnsekvensen ved behov uten å påvirke utseendet i andre
  sammenhenger.
- **`\splitword` for lange ord, men bare der det trengs**: Klassenavn
  som `LinearRegression` står i markdown uten backticks og fanges
  derfor ikke av Code-filteret. Inne i tabellens body wrappes alle
  Str-elementer > 14 tegn _uten naturlige bryte-punkter_ i
  `\splitword`. Ord som inneholder `-`, `_`, `.`, `/` eller `=`
  hoppes over, slik at LaTeXs naturlige hyphenation (norsk via babel)
  får håndtere dem. Headers (TableHead) berøres ikke i det hele tatt
  for å unngå at lange overskrifter brytes på rare steder.
- **Caption-styling med `\captionsetup`**: Pandoc auto-nummererer
  figurer som "Figur N:" og tabeller som "Tabell N:" i sin
  `\caption`-rendering. Rapporten bruker manuell nummerering ("Figur
  8.2", "Tabell 9.1") i kryssreferanser, så
  `labelformat=empty` i header.tex fjerner auto-prefiksen og lar
  caption-teksten være som den står i markdown. `font={small,it}` og
  `justification=centering` gir samme visuelle stil som rapportens
  HTML-mønster (sentrert, liten, italic).
- **Landskap for ≥ 10 kolonner**: Tabell 9.1 har 10 kolonner med tre
  lange tekstkolonner (Tolkbarhet/Hovedstyrke/Hovedsvakhet) og
  trenger landskap for å være lesbar. Tabell 6.2 og 7.2 (8 kolonner)
  forblir i portrett. Terskelen er valgt for å fange Tabell 9.1 men
  ikke smale 8-kolonne-tabeller.
- **Unicode-mapping via `newunicodechar`**: Default Latin Modern-fonten
  har ikke ☐ ☒ −. `newunicodechar` mapper kodepunktene direkte til
  `\ding{110}`, `\ding{55}` og `\ensuremath{-}` (fra `pifont`).
- **`lualatex`**: Leser UTF-8 nativt, så norske bokstaver (`æøå`)
  renderer uten ekstra konfig. Gir også bedre typografi via
  `microtype`.

## Ved bytte til pdflatex

Hvis miljøet ikke har `texlive-luatex`, kan oppsettet falles tilbake til
pdflatex ved å bytte `--pdf-engine=lualatex` til
`--pdf-engine=pdflatex`. Da må følgende deklarasjoner legges til
[header.tex](header.tex) for at norske bokstaver skal rendere:

```latex
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
```

`seqsplit` og `newunicodechar` fungerer i begge motorene.
