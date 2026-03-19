# 01 Dataforståelse og variabler (WBS 2.2)

Denne aktiviteten kartlegger datastruktur og variabler i datasettet.

## Kjøring

Kjør fra roten av `006 analysis`:

```bash
uv run python aktiviteter/01_dataforstaelse_og_variabler/start_wbs_2_2.py
```

## Filer i mappen

- `start_wbs_2_2.py`: Leser datasettet og lager første oversikter.
- `tab_dataset_oversikt.csv`: Kolonnenavn, datatype, manglende verdier og antall unike verdier.
- `tab_manglende_verdier.csv`: Rangert oversikt over manglende verdier per kolonne.
- `fig_datatype_fordeling.png`: Figur som viser fordeling av datatyper i datasettet.

## Datakilde

- `004 data/Dagligvare_Dataset.csv`

## Neste steg

- Kvalitetssjekk av nøkkelvariabler for prognose.
- Velge hvilke variabler som tas videre til WBS 2.3.
