# 11 Parameterjustering Random Forest (WBS 4.4)

Denne aktiviteten justerer parameterne til `RandomForestRegressor` med 2024 som intern valideringsperiode, mens lineær regresjon beholdes som fast benchmark.

## Kjøring

Kjør fra roten av `006 analysis`:

```bash
UV_CACHE_DIR=/tmp/uv-cache uv run python aktiviteter/11_parameterjustering_random_forest/start_wbs_4_4.py
```

## Filer i mappen

- `start_wbs_4_4.py`: Leser `X_train.csv` og `y_train.csv`, tester 36 Random Forest-kandidater og retrener vinneren på hele 2022-2024.
- `model_random_forest_tuned.joblib`: Tunet Random Forest-modell som skal brukes som standard Random Forest-inngang til WBS 5.1.
- `tab_rf_tuning_kandidater.csv`: Samlet oversikt over alle testede kandidater og valideringsmetrikkene deres.
- `tab_rf_tuning_vinner.csv`: Kort oppsummering av valgt konfigurasjon og forbedring mot baseline.
- `tab_rf_tuned_modelloversikt.csv`: Modelloversikt for den retrente tuned-modellen.
- `random_forest_tuning.md`: Norsk oppsummering av valideringsoppsett, vinnerkonfigurasjon og avgrensning mot senere WBS-steg.

## Datakilder

- `006 analysis/aktiviteter/06_datasplitt/X_train.csv`
- `006 analysis/aktiviteter/06_datasplitt/y_train.csv`
- `006 analysis/aktiviteter/09_random_forest_regressor/tab_rf_modelloversikt.csv` brukes som dokumentert baseline-referanse i prosjektet, men overskrives ikke.

## Viktige valg

- WBS 4.4 tuner bare `RandomForestRegressor`; lineær regresjon justeres ikke videre.
- Søketreningen bruker 2022-2023, mens 2024 brukes som valideringsår for modellvalg.
- 2025 brukes ikke i tuning og forblir reservert for videre prognoser og evaluering i WBS 5.x.
- Vinneren velges på lavest validerings-`RMSE`, med `MAPE` som sekundær metrikk ved likt resultat.
- Baseline-artefaktene i `09_random_forest_regressor` beholdes uendret som sammenligningspunkt.

## Neste steg

- Bruke `model_random_forest_tuned.joblib` som standard Random Forest-modell i WBS 5.1.
- Generere prognoser for 2025 i WBS 5.1.
- Beregne `RMSE`, `MAPE` og sammenligne modeller i WBS 5.2 og 5.3.
