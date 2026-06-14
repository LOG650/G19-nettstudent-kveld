"""Etterbehandler den pandoc-genererte LaTeX-filen før lualatex.

Gjør to ting:

1. **Figurer i original plassering.** Bytter hver `\\begin{figure}` til
   `\\begin{figure}[H]` (krever float-pakken, lastet i header.tex). Da står
   figuren nøyaktig der den ligger i Markdown-kilden i stedet for å flyte til
   topp/bunn av siden.

2. **Tabeller som ikke splittes + radlinjer.** Pandoc lager `longtable` for alle
   tabeller, og longtable brytes over sideskift. Hver longtable konverteres til en
   ikke-brytbar, sentrert `tabular` (én uadskillelig boks – splittes aldri, flyttes
   som helhet til neste side ved plassmangel), og det legges en vannrett linje
   (`\\midrule`) mellom hver datarad. Hierarkiske overskrifter (multirow/multicolumn)
   og kolonnebredder beholdes uendret; ingen loddrette linjer.

Bruk:
    python3 build/postprocess.py build/rapport_final.tex
"""

from __future__ import annotations

import pathlib
import re
import sys

# \begin{figure} (med eller uten [..]-plassering) → \begin{figure}[H]
FIGURE = re.compile(r"\\begin\{figure\}(?:\[[^\]]*\])?")

# Hele longtable-blokken. Kolonnespec ligger mellom {@{} … @{}} og kan inneholde
# nøstede klammer (\real{..}, p{..}), derfor matcher vi fram til den avsluttende
# @{} eksplisitt.
LONGTABLE = re.compile(
    r"\\begin\{longtable\}\[\]\{(@\{\}.*?@\{\})\}\n(.*?)\\end\{longtable\}",
    re.DOTALL,
)


# Tabeller som er trange og bryter for mye i ordene med standard \small får
# ett hakk mindre skrift (\footnotesize). Identifiseres på captionteksten.
SMALLER_TABLES = ("Tabell 6.1", "Tabell 6.2", "Tabell 9.1")


def convert_table(match: re.Match[str]) -> str:
    colspec, body = match.group(1), match.group(2)

    # Trekk ut en eventuell pandoc-caption (Markdown-tabeller har den; de
    # HTML-genererte hierarkiske tabellene har ingen – de har caption som egen
    # linje rett etter blokken).
    caption = None
    cap_m = re.search(r"\\caption\{(.*?)\}\\tabularnewline\n?", body, re.DOTALL)
    if cap_m:
        caption = cap_m.group(1).strip()
        body = body[: cap_m.start()] + body[cap_m.end():]

    size = "\\small"
    if caption and any(caption.startswith(t) for t in SMALLER_TABLES):
        size = "\\footnotesize"

    # Fjern longtable-maskineriet.
    body = re.sub(r"\\endfirsthead.*?\\endhead", "", body, flags=re.DOTALL)  # duplisert header
    body = body.replace("\\endhead", "")                                     # caption-løs variant
    body = re.sub(r"\\bottomrule\\noalign\{\}\s*\\endlastfoot", "", body)     # longtable-fot
    body = body.replace("\\noalign{}", "")

    # Del header fra data ved den (eneste gjenværende) \midrule.
    if "\\midrule" in body:
        head, data = body.split("\\midrule", 1)
    else:
        head, data = body, ""
    head = head.strip()

    # Legg en linje mellom hver datarad; \bottomrule helt til slutt.
    rows = [r.strip() for r in re.split(r"\\\\", data) if r.strip()]
    data_tex = ""
    for i, row in enumerate(rows):
        data_tex += row + " \\\\\n"
        data_tex += "\\bottomrule\n" if i == len(rows) - 1 else "\\midrule\n"

    out = (
        "\\begin{center}\n" + size + "\n"
        "\\begin{tabular}{" + colspec + "}\n"
        + head + "\n\\midrule\n"
        + data_tex
        + "\\end{tabular}\n\\end{center}\n"
    )
    if caption:
        out += "\n\\begin{center}{\\small\\itshape " + caption + "}\\end{center}\n"
    return out


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 1

    path = pathlib.Path(argv[1])
    tex = path.read_text(encoding="utf-8")
    tex, n_fig = FIGURE.subn(lambda m: "\\begin{figure}[H]", tex)
    tex, n_tab = LONGTABLE.subn(convert_table, tex)
    path.write_text(tex, encoding="utf-8")
    print(f"Satte [H] på {n_fig} figurer")
    print(f"Konverterte {n_tab} longtable → ikke-brytbar tabular med radlinjer")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
