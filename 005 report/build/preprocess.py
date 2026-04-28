"""Preprosesserer rapport.md før pandoc-bygging.

Konverterer HTML-figurblokker (`<div align="center"><img ...><p ...>...</p></div>`)
til Markdown image-syntaks `![figurtekst](sti){width=NN%}`, slik at pandoc kan
embeddre figurene som faktiske bilder i LaTeX/PDF-output.

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


def to_markdown_image(match: re.Match[str]) -> str:
    src, _alt, width, caption = match.groups()
    return f"![{caption}]({src}){{width={width}%}}"


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 1

    src_path = pathlib.Path(argv[1])
    dst_path = pathlib.Path(argv[2])

    text = src_path.read_text(encoding="utf-8")
    new_text, count = FIGUR_BLOCK.subn(to_markdown_image, text)

    dst_path.write_text(new_text, encoding="utf-8")
    print(f"Konverterte {count} HTML-figurblokker → markdown image-syntaks")
    print(f"Skrev {dst_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
