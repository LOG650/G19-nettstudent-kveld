# Prognoser for 2025 (WBS 5.1)

## Hva WBS 5.1 gjør

- Aktiviteten genererer 2025-prognoser for lineær regresjon, Random Forest-baseline og tuned Random Forest.
- Tuned Random Forest er standardmodellen videre i Random Forest-sporet, men benchmark- og baseline-sporene beholdes for senere evaluering.
- Faktisk `Sales` for 2025 er med i outputen for sporbarhet, men uten feilkolonner eller evalueringsmetrikker.

## Datagrunnlag

- Antall 2025-observasjoner: 3312
- Antall måneder i oppsummeringen: 12
- Testfeature-matrise: `06_datasplitt/X_test.csv`
- Testtarget: `06_datasplitt/y_test.csv`

## Modellspor brukt i prognosene

- `benchmark lineær`: `LinearRegression` via `prognose_lineaer_regresjon` (lokal modellfil funnet: ja, autogenerert i 5.1: nei)
- `baseline RF`: `RandomForestRegressor` via `prognose_random_forest_baseline` (lokal modellfil funnet: ja, autogenerert i 5.1: nei)
- `tuned RF`: `RandomForestRegressor` via `prognose_random_forest_tuned` (lokal modellfil funnet: ja, autogenerert i 5.1: nei)

## Månedlig dekning

- Første måned i oppsummeringen: `2025-01`
- Siste måned i oppsummeringen: `2025-12`

## Produserte artefakter

- `tab_prognoser_2025_detalj.csv`
- `tab_prognoser_2025_maaned.csv`
- `tab_prognosemodeller_oversikt.csv`
- `prognoser_2025.md`

## Avgrensning mot senere WBS-steg

- WBS 5.1 beregner ikke residualer, `RMSE`, `MAPE` eller modellrangering.
- Selve evalueringen og sammenligningen av modellene er utsatt til WBS 5.2 og WBS 5.3.
