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

Kjør fra `005 report/`:

```bash
python3 build/preprocess.py rapport.md build/rapport_pdf.md
pandoc build/rapport_pdf.md -o rapport.pdf \
  --pdf-engine=lualatex --resource-path=. \
  -V geometry:a4paper -V geometry:margin=2.5cm -V lang=nb-NO -V fontsize=11pt \
  --columns=120 \
  --include-in-header=build/header.tex \
  --lua-filter=build/tables.lua
```

Resultatet legges som `rapport.pdf` i `005 report/`.

## Hva hver fil gjør

| Fil | Rolle |
|:---|:---|
| [preprocess.py](preprocess.py) | Konverterer HTML-figurblokker (`<div align="center"><img …></div>`) til Markdown image-syntaks. Pandoc embeddrer ikke HTML `<img>` i LaTeX-flyten, så preprosessering er nødvendig for at figurer skal vises. |
| [header.tex](header.tex) | LaTeX-preamble: tabellinnstillinger, `microtype`, `pdflscape`, makroene `\splitcode` og `\splitword` (basert på `seqsplit`), og Unicode-mapping for ☐ ☒ − via `newunicodechar`. |
| [tables.lua](tables.lua) | Pandoc Lua-filter. Setter alle kolonnebredder til `1/n` (tvinger linjebryting), wrapper inline-kode i `\splitcode{}` globalt, og inne i tabeller wrapper også lange ubrudte ord (> 14 tegn) i `\splitword{}`. Tabeller med ≥ 8 kolonner roteres til landskap. |
| `rapport_pdf.md` | Mellomprodukt fra `preprocess.py`. Ignorert i git. |

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
- **`\splitword` for lange ord i tabeller**: Klassenavn som
  `LinearRegression` står i markdown uten backticks og fanges derfor
  ikke av Code-filteret. Inne i tabeller får alle Str-elementer > 14
  tegn brytbar form via `\splitword`, slik at også CamelCase-strenger
  brytes mellom tegn ved behov. Terskelen 14 sparer typiske norske
  ord fra unødvendig kunstig bryting.
- **Landskap for ≥ 8 kolonner**: Tabell 7.2 har 8 kolonner. Selv med
  liten skrift blir den trang i portrettformat, så `pdflscape` roterer
  hele siden — leseren kan rotere skjermen eller skrive ut liggende.
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
