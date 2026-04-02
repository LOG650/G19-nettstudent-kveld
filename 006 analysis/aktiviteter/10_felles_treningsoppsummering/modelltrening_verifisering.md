# Felles treningsoppsummering (WBS 4.3)

## Hva WBS 4.3 gjør

- WBS 4.1 gjennomførte selve treningen av lineær regresjon.
- WBS 4.2 gjennomførte selve treningen av Random Forest Regressor.
- WBS 4.3 trener ikke modellene på nytt, men verifiserer at de bygger på samme treningsgrunnlag og samler de viktigste modellinterne signalene.

## Verifisert felles treningsgrunnlag

- Input features: `06_datasplitt/X_train.csv`
- Input target: `06_datasplitt/y_train.csv`
- Antall treningsrader: 6682
- Antall features: 67
- Target-kolonne: `Sales`

## Produserte artefakter

- `tab_modelltrening_oversikt.csv`
- `tab_modellsignaler_oversikt.csv`
- `modelltrening_verifisering.md`

## Lokal modellfilstatus

- `LinearRegression` lokal modellfil funnet: ja
- `RandomForestRegressor` lokal modellfil funnet: ja

## Utdrag av samlede modellsignaler

- De fem sterkeste signalene per modell er samlet i `tab_modellsignaler_oversikt.csv`.
- `LinearRegression` rang 1: `Region_North` (abs_koeffisient = 277.199368), fortegn: negativ
- `LinearRegression` rang 2: `Discount` (abs_koeffisient = 166.350024), fortegn: negativ
- `LinearRegression` rang 3: `City_Dindigul` (abs_koeffisient = 86.223061), fortegn: negativ
- `RandomForestRegressor` rang 1: `Discount` (importance = 0.123926)
- `RandomForestRegressor` rang 2: `dayofmonth` (importance = 0.122360)
- `RandomForestRegressor` rang 3: `weekofyear` (importance = 0.086338)

## Avgrensning

- Aktiviteten produserer ikke nye prediksjoner, residualfiler, treningsmetrikker, testmetrikker, `RMSE`, `MAPE`, prognoser eller figurer.
- Videre evaluering og modellvurdering er utsatt til WBS 5.x og WBS 6.1.
