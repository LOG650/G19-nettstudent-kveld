# Bygging av rapport.pdf

Denne mappen inneholder byggskript og LaTeX-konfig for å konvertere
[../rapport.md](../rapport.md) til PDF.

## Forutsetninger

- `pandoc` (testet med 3.1.3)
- `pdflatex` (TeX Live, `texlive-latex-recommended` + `texlive-fonts-recommended`)
- `python3`

`lualatex` og `xelatex` er **ikke** brukt fordi miljøet mangler full
TeX Live-installasjon for disse motorene. `pdflatex` håndterer norsk
encoding via `inputenc` og spesialtegn (☐ ☒ −) via deklarasjoner i
[header.tex](header.tex).

## Bygg PDF

Kjør fra `005 report/`:

```bash
python3 build/preprocess.py rapport.md build/rapport_pdf.md
pandoc build/rapport_pdf.md -o rapport.pdf \
  --pdf-engine=pdflatex --resource-path=. \
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
| [header.tex](header.tex) | LaTeX-preamble med tabellinnstillinger (`\small` skrift, strammere kolonner), `microtype`, `pdflscape` og Unicode-deklarasjoner for `pifont`-symboler. |
| [tables.lua](tables.lua) | Pandoc Lua-filter. Setter alle kolonnebredder til `1/n` slik at pandoc bruker `p{}`-kolonner som bryter linjer. Tabeller med ≥ 8 kolonner roteres automatisk til landskap. |
| `rapport_pdf.md` | Mellomprodukt fra `preprocess.py`. Ignorert i git. |

## Hvorfor disse valgene

- **Equal-width `p{}`-kolonner**: Markdown-tabeller med uniform `---`
  separator gir pandoc ingen breddeinformasjon, og default `l`/`c`/`r`
  kolonner _bryter ikke_ linjer — de renner ut til høyre og overlapper
  med naboen. Lua-filteret tildeler `1/n` av sidebredden til hver
  kolonne, som tvinger pandoc til å bruke `p{...\textwidth}` med riktig
  linjebryting.
- **Landskap for ≥ 8 kolonner**: Tabell 7.2 har 8 kolonner. Selv med
  liten skrift blir den trang i portrettformat, så `pdflscape` roterer
  hele siden — leseren kan rotere skjermen eller skrive ut liggende.
- **`pifont` for ☐ ☒**: pdflatex støtter ikke disse Unicode-symbolene
  uten ekstra deklarasjon. `pifont` gir LaTeX-glyfer som ligner.
- **Ingen `lualatex`/`xelatex`**: Disse mangler i miljøet (font cache /
  ikke installert). pdflatex med Unicode-mapping er en pragmatisk
  løsning som fungerer her og nå.
