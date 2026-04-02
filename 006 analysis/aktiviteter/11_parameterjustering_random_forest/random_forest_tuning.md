# Random Forest tuning (WBS 4.4)

## Avgrensning og formål

- WBS 4.4 justerer kun parametere for `RandomForestRegressor`.
- Lineær regresjon beholdes uendret som fast benchmark fra WBS 4.1.
- WBS 4.4 bruker ikke 2025-data i tuning eller modellvalg.

## Valideringsoppsett

- Søketrening: `2022, 2023`
- Valideringsår: `2024`
- Antall kandidater testet: 36
- Valg av vinner gjøres på lavest `RMSE` på valideringsåret, med `MAPE` som sekundær metrikk ved likt resultat.

## Vinnerkonfigurasjon

- `n_estimators=400`
- `max_depth=10`
- `min_samples_leaf=4`
- `max_features=sqrt`
- Validerings-`RMSE`: `577.267750`
- Validerings-`MAPE`: `43.5554 %`
- Baseline endret: `ja`
- Retrening på hele 2022-2024 tok `0.509763` sekunder.

## Toppkandidater

- Rang 1: `rf_tune_30` med `RMSE=577.267750` og `MAPE=43.5554 %`
- Rang 2: `rf_tune_28` med `RMSE=577.286036` og `MAPE=43.5662 %`
- Rang 3: `rf_tune_10` med `RMSE=577.364009` og `MAPE=43.5837 %`
- Rang 4: `rf_tune_26` med `RMSE=577.649975` og `MAPE=43.6020 %`
- Rang 5: `rf_tune_12` med `RMSE=577.805328` og `MAPE=43.6084 %`

## Produserte artefakter

- `model_random_forest_tuned.joblib`
- `tab_rf_tuning_kandidater.csv`
- `tab_rf_tuning_vinner.csv`
- `tab_rf_tuned_modelloversikt.csv`
- `random_forest_tuning.md`

## Avgrensning mot senere WBS-steg

- Tuningen er gjort mot 2024 som intern validering, mens 2025 fortsatt er reservert for videre prognoser og evaluering i WBS 5.x.
- Aktiviteten produserer ikke prognosefiler for 2025 og beregner ikke endelige test-`RMSE` eller test-`MAPE`.
- Baseline-artefaktene i `09_random_forest_regressor` er bevart uendret som sammenligningspunkt.
