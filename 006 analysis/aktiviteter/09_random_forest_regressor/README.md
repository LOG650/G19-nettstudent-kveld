# 09 Random Forest Regressor (WBS 4.2)

Denne aktiviteten implementerer benchmark-varianten av `RandomForestRegressor` med utgangspunkt i treningsmatrisen fra WBS 3.3.

## Kjøring

Kjør fra roten av `006 analysis`:

```bash
UV_CACHE_DIR=/tmp/uv-cache uv run python aktiviteter/09_random_forest_regressor/start_wbs_4_2.py
```

## Filer i mappen

- `start_wbs_4_2.py`: Leser modellmatrise fra WBS 3.3, trener `RandomForestRegressor` og skriver modellartefakter.
- `model_random_forest_regressor.joblib`: Serialisert Random Forest-modell for videre bruk.
- `tab_rf_modelloversikt.csv`: Kort oppsummering av input, sentrale parameterverdier og treningstid.
- `tab_rf_feature_importance.csv`: Feature importance-tabell rangert etter importance.
- `random_forest_regressor.md`: Kort norsk oppsummering av modellvalget og avgrensningen mot senere WBS-steg.

## Datakilde

- `006 analysis/aktiviteter/06_datasplitt/X_train.csv`
- `006 analysis/aktiviteter/06_datasplitt/y_train.csv`

## Viktige valg

- WBS 4.2 bruker `RandomForestRegressor(n_estimators=200, random_state=42, n_jobs=-1)` som enkel baseline.
- Øvrige parametre beholdes på `scikit-learn`-default for installert versjon.
- `feature_importances_` dokumenteres som et foreløpig modellinternt signal, ikke som endelig variabelrangering.
- Aktiviteten produserer ikke testprediksjoner, `RMSE`, `MAPE`, prognosefiler eller modellsammenligning.

## Neste steg

- Samle modelltrening og videre verifisering i WBS 4.3.
- Beregne prognoser og evalueringsmål i WBS 5.x.
- Tolke og sammenligne variabelsignaler senere i WBS 5.4 og 6.1.
