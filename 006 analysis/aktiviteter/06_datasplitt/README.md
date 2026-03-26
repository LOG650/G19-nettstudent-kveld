# 06 Datasplitt (WBS 3.3)

Denne aktiviteten bygger direkte på `05_feature_engineering` og lager modellklare trenings- og testfiler.

## Kjøring

Kjør fra roten av `006 analysis`:

```bash
uv run python aktiviteter/06_datasplitt/start_wbs_3_3.py
```

## Filer i mappen

- `start_wbs_3_3.py`: Leser `dataset_feature_engineered.csv`, splitter tidsbasert og lager encoded modellmatriser.
- `X_train.csv`: Treningsfeatures etter encoding.
- `X_test.csv`: Testfeatures etter encoding.
- `y_train.csv`: Treningsmål (`Sales`).
- `y_test.csv`: Testmål (`Sales`).
- `tab_split_oversikt.csv`: Oppsummering av radantall per år og delsett.
- `datasplitt.md`: Kort oppsummering av splitten og modellforberedelsen.

## Datakilde

- `006 analysis/aktiviteter/05_feature_engineering/dataset_feature_engineered.csv`

## Viktige valg

- `06_datasplitt` leser kun outputen fra WBS 3.2.
- `Order Date` brukes ikke som modellinput i `X_train` og `X_test`.
- Kategoriske kolonner one-hot-encodes i dette steget.

## Splittregel

- Trening: `2022`, `2023`, `2024`
- Test: `2025`
