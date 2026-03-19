# 006 analysis - Python med uv

Dette området bruker ett felles Python-prosjekt med uv for hele analysearbeidet.

## Miljø

- Python: 3.12
- Pakker: pandas, numpy, scikit-learn, matplotlib, seaborn
- Arbeidsform: kun `.py`-skript (ingen notebooks)

## Standardkommandoer

Kjør i denne mappen:

```bash
uv sync
```

Test at avhengigheter virker:

```bash
uv run python -c "import pandas, numpy, sklearn, matplotlib, seaborn; print('ok')"
```

Eksempel på kjøring av et analyseskript:

```bash
uv run python aktiviteter/min_aktivitet/skript.py
```

Legg til ny pakke:

```bash
uv add pakkenavn
```

## Struktur

- Skript, figurer og tabeller skal ligge i samme aktivitetsmappe.
- Bruk prefiks `fig_` for figurer og `tab_` for tabeller.
