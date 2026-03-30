# Random Forest Regressor (WBS 4.2)

## Datagrunnlag

- Input features: `06_datasplitt/X_train.csv`
- Input target: `06_datasplitt/y_train.csv`
- Antall treningsrader: 6682
- Antall features: 67

## Modellvalg

- Benchmark-varianten er `RandomForestRegressor` fra `scikit-learn`.
- Baseline-parametre er `n_estimators=200`, `random_state=42` og `n_jobs=-1`.
- Øvrige parametre bruker `scikit-learn`-default for installert versjon i analysemiljøet.
- Treningstiden i denne kjøringen var `0.766622` sekunder.

## Produserte artefakter

- `model_random_forest_regressor.joblib`
- `tab_rf_modelloversikt.csv`
- `tab_rf_feature_importance.csv`
- `random_forest_regressor.md`

## Foreløpige feature-signaler

- De fem viktigste feature-signalene i denne baseline-modellen er:
- `Discount` (importance = 0.123926, 12.39 %)
- `dayofmonth` (importance = 0.122360, 12.24 %)
- `weekofyear` (importance = 0.086338, 8.63 %)
- `dayofweek` (importance = 0.063920, 6.39 %)
- `year` (importance = 0.038233, 3.82 %)

## Avgrensning

- WBS 4.2 dokumenterer kun implementering og trening av Random Forest på treningsdata.
- Feature importance-verdiene er foreløpige modellinterne signaler og erstatter ikke senere evaluering og tolkning i WBS 5.4 og 6.1.
- Aktiviteten produserer ikke testprediksjoner, `RMSE`, `MAPE`, prognoser eller modellsammenligning.
