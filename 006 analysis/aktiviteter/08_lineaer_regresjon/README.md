# 08 Lineær regresjon (WBS 4.1)

Denne aktiviteten implementerer benchmark-modellen for lineær regresjon med utgangspunkt i treningsmatrisen fra WBS 3.3.

## Kjøring

Kjør fra roten av `006 analysis`:

```bash
UV_CACHE_DIR=/tmp/uv-cache uv run python aktiviteter/08_lineaer_regresjon/start_wbs_4_1.py
```

## Filer i mappen

- `start_wbs_4_1.py`: Leser modellmatrise fra WBS 3.3, trener `LinearRegression` og skriver modellartefakter.
- `model_lineaer_regresjon.joblib`: Serialisert benchmark-modell for videre bruk.
- `tab_lr_modelloversikt.csv`: Kort oppsummering av input, modellvalg og intercept.
- `tab_lr_koeffisienter.csv`: Koeffisienttabell rangert etter absolutt verdi.
- `lineaer_regresjon.md`: Kort norsk oppsummering av modellvalget og avgrensningen mot senere WBS-steg.

## Datakilde

- `006 analysis/aktiviteter/06_datasplitt/X_train.csv`
- `006 analysis/aktiviteter/06_datasplitt/y_train.csv`

## Viktige valg

- WBS 4.1 bruker `LinearRegression(fit_intercept=True)` som benchmark-modell.
- Aktiviteten bruker dagens one-hot-kodede feature-sett uten skalering og uten regularisering.
- Koeffisientene må tolkes varsomt fordi dummykoding uten referansekategori kan gi multikollinearitet.
- Aktiviteten produserer ikke testprediksjoner, `RMSE`, `MAPE` eller modellsammenligning.

## Neste steg

- Implementere Random Forest separat i WBS 4.2.
- Samle modelltrening og videre verifisering i WBS 4.3.
- Beregne prognoser og evalueringsmål i WBS 5.x.
