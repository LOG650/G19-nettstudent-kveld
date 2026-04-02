# 12 Prognoser 2025 (WBS 5.1)

Denne aktiviteten genererer prognoser for 2025 for tre modellspor: lineær regresjon, Random Forest-baseline og tuned Random Forest.

## Kjøring

Kjør fra roten av `006 analysis`:

```bash
UV_CACHE_DIR=/tmp/uv-cache uv run python aktiviteter/12_prognoser_2025/start_wbs_5_1.py
```

## Filer i mappen

- `start_wbs_5_1.py`: Leser testdata for 2025, henter eller regenererer modellene og skriver radvise og månedlige prognosefiler.
- `tab_prognoser_2025_detalj.csv`: Samlet radnivåtabell med faktisk salg og prognoser for alle tre modellspor.
- `tab_prognoser_2025_maaned.csv`: Månedlig oppsummering av faktisk salg og prognosesummer for 2025.
- `tab_prognosemodeller_oversikt.csv`: Kort oversikt over hvilke modellspor som er brukt og om modeller ble autogenerert i 5.1.
- `prognoser_2025.md`: Norsk oppsummering av datagrunnlag, modellspor og avgrensning mot 5.2 og 5.3.

## Datakilder

- `006 analysis/aktiviteter/06_datasplitt/X_test.csv`
- `006 analysis/aktiviteter/06_datasplitt/y_test.csv`
- `006 analysis/aktiviteter/06_datasplitt/X_train.csv`
- `006 analysis/aktiviteter/06_datasplitt/y_train.csv`
- `006 analysis/aktiviteter/05_feature_engineering/dataset_feature_engineered.csv`

## Viktige valg

- Aktiviteten lager prognoser for alle tre modellspor i én samlet leveranse.
- Faktisk `Sales` for 2025 tas med for sporbarhet, men uten residualer eller evalueringsmetrikker.
- Hvis en lokal `.joblib` mangler, regenereres modellen i memory fra dokumenterte parameter- eller modellvalg uten å skrive ny modellfil.
- Tuned Random Forest fra WBS 4.4 er standardmodellen videre i Random Forest-sporet.

## Neste steg

- Beregne `RMSE` og `MAPE` i WBS 5.2.
- Sammenligne modellresultater i WBS 5.3.
- Analysere viktige variabler videre i WBS 5.4.
