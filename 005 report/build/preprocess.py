"""Preprosesserer rapport.md før pandoc-bygging.

Gjør tre konverteringer:

1. HTML-figurblokker (`<div align="center"><img ...><p ...>...</p></div>`)
   blir til Markdown image-syntaks `![figurtekst](sti){width=NN%}`. Pandoc
   embeddrer ikke HTML `<img>` i LaTeX-flyten, så preprosessering er
   nødvendig for at figurer skal vises.

2. HTML-tabeller (`<div align="center" ...><table>…</table></div>`) med
   hierarkiske kolonneoverskrifter (colspan/rowspan) som ikke kan uttrykkes
   i Markdown-tabeller. Pandocs Markdown-leser slipper rå HTML-tabeller når
   målet er LaTeX, så hver tabell konverteres separat via `pandoc -f html
   -t latex` (med samme `tables.lua`-filter som hovedbygget) til en ekte
   longtable med `\\multirow`/`\\multicolumn`. En eventuell etterfølgende
   bildetekst limes inn som sentrert liten italic linje under tabellen.

3. HTML-tabellbildetekster (`<p align="center"><small><i>Tabell X.Y …</i></small></p>`)
   for vanlige Markdown-tabeller blir til pandoc-native caption-syntaks
   (`: Tabell X.Y …`). Pandoc genererer da en ekte longtable-caption, og
   header.tex' captionsetup styler den som sentrert, liten og italic uten
   «Tabell N:» auto-prefiks.

Bruk:
    python3 build/preprocess.py rapport.md build/rapport_pdf.md
"""

from __future__ import annotations

import pathlib
import re
import subprocess
import sys

LUA_FILTER = str(pathlib.Path(__file__).resolve().parent / "tables.lua")

TABELL_DIV = re.compile(
    r'<div align="center"[^>]*>\s*\n'
    r'\s*(<table>.*?</table>)\s*\n'
    r'\s*</div>'
    r'(?:\s*\n\s*<p align="center"><small><i>(Tabell[^<]+)</i></small></p>)?',
    re.DOTALL,
)

FIGUR_BLOCK = re.compile(
    r'<div align="center">\s*\n'
    r'\s*<img\s+src="([^"]+)"\s+alt="([^"]*)"\s+width="(\d+)%">\s*\n'
    r'\s*<p align="center"><small><i>([^<]+)</i></small></p>\s*\n'
    r'\s*</div>',
    re.MULTILINE,
)

TABELL_CAPTION = re.compile(
    r'<p align="center"><small><i>(Tabell [^<]+)</i></small></p>',
)


def to_markdown_image(match: re.Match[str]) -> str:
    src, _alt, width, caption = match.groups()
    return f"![{caption}]({src}){{width={width}%}}"


def to_pandoc_caption(match: re.Match[str]) -> str:
    caption = match.group(1).strip()
    return f": {caption}"


def _escape_latex(text: str) -> str:
    for char, repl in (("&", r"\&"), ("%", r"\%"), ("#", r"\#"), ("_", r"\_")):
        text = text.replace(char, repl)
    return text


def to_latex_table(match: re.Match[str]) -> str:
    """Konverter én HTML-tabell til rå LaTeX-longtable via pandoc.

    Beholder hierarkiske overskrifter (colspan/rowspan → multicolumn/multirow)
    og kjører `tables.lua` slik at kolonnene får lik bredde (linjebryting) og
    brede tabeller roteres til landskap, akkurat som hovedbygget.
    """
    inner_html, caption = match.group(1), match.group(2)
    result = subprocess.run(
        ["pandoc", "-f", "html", "-t", "latex", "--columns=120",
         f"--lua-filter={LUA_FILTER}"],
        input=inner_html, capture_output=True, text=True, check=True,
    )
    latex = result.stdout.strip()
    out = f"\n{latex}\n"
    if caption:
        cap = _escape_latex(caption.strip())
        out += f"\n\\begin{{center}}\n{{\\small\\itshape {cap}}}\n\\end{{center}}\n"
    return out


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 1

    src_path = pathlib.Path(argv[1])
    dst_path = pathlib.Path(argv[2])

    text = src_path.read_text(encoding="utf-8")
    text, html_tab_count = TABELL_DIV.subn(to_latex_table, text)
    text, fig_count = FIGUR_BLOCK.subn(to_markdown_image, text)
    text, tab_count = TABELL_CAPTION.subn(to_pandoc_caption, text)

    dst_path.write_text(text, encoding="utf-8")
    print(f"Konverterte {html_tab_count} HTML-tabeller → rå LaTeX-longtable")
    print(f"Konverterte {fig_count} HTML-figurblokker → markdown image-syntaks")
    print(f"Konverterte {tab_count} HTML-tabellbildetekster → pandoc-caption")
    print(f"Skrev {dst_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
