"""Preprosesserer rapport.md før pandoc-bygging.

Gjør to konverteringer:

1. HTML-figurblokker (`<div align="center"><img ...><p ...>...</p></div>`)
   blir til Markdown image-syntaks `![figurtekst](sti){width=NN%}`. Pandoc
   embeddrer ikke HTML `<img>` i LaTeX-flyten, så preprosessering er
   nødvendig for at figurer skal vises.

2. HTML-tabellbildetekster (`<p align="center"><small><i>Tabell X.Y …</i></small></p>`)
   blir til pandoc-native caption-syntaks (`: Tabell X.Y …`). Pandoc
   genererer da en ekte longtable-caption, og header.tex' captionsetup
   styler den som sentrert, liten og italic uten «Tabell N:» auto-prefiks.

Bruk:
    python3 build/preprocess.py rapport.md build/rapport_pdf.md
"""

from __future__ import annotations

import pathlib
import re
import sys

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


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 1

    src_path = pathlib.Path(argv[1])
    dst_path = pathlib.Path(argv[2])

    text = src_path.read_text(encoding="utf-8")
    text, fig_count = FIGUR_BLOCK.subn(to_markdown_image, text)
    text, tab_count = TABELL_CAPTION.subn(to_pandoc_caption, text)

    dst_path.write_text(text, encoding="utf-8")
    print(f"Konverterte {fig_count} HTML-figurblokker → markdown image-syntaks")
    print(f"Konverterte {tab_count} HTML-tabellbildetekster → pandoc-caption")
    print(f"Skrev {dst_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
