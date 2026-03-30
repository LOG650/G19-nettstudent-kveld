# Lineær regresjon (WBS 4.1)

## Datagrunnlag

- Input features: `06_datasplitt/X_train.csv`
- Input target: `06_datasplitt/y_train.csv`
- Antall treningsrader: 6682
- Antall features: 67

## Modellvalg

- Benchmark-modellen er `LinearRegression` fra `scikit-learn`.
- Modellen er kjørt med `fit_intercept=True` uten skalering eller regularisering.
- Feature-settet er identisk med den one-hot-kodede modellmatrisen fra WBS 3.3.

## Produserte artefakter

- `model_lineaer_regresjon.joblib`
- `tab_lr_modelloversikt.csv`
- `tab_lr_koeffisienter.csv`
- `lineaer_regresjon.md`

## Første observasjoner

- Modellens intercept er `-3193.551902`.
- De fem største koeffisientene målt i absoluttverdi er:
- `Region_North` (negativ, |koeff| = 277.199368)
- `Discount` (negativ, |koeff| = 166.350024)
- `City_Dindigul` (negativ, |koeff| = 86.223061)
- `Region_South` (positiv, |koeff| = 84.226765)
- `Region_East` (positiv, |koeff| = 65.651701)

## Avgrensning

- WBS 4.1 dokumenterer kun implementering og trening av lineær regresjon på treningsdata.
- Evaluering på 2025-testsettet samt `RMSE`, `MAPE`, prognoser og modellsammenligning er utsatt til senere WBS-steg.
- Koeffisientene må tolkes varsomt fordi dagens dummykoding kan gi multikollinearitet i lineær regresjon.
