# 15 Viktige variabler (WBS 5.4)

Denne aktiviteten identifiserer og rangerer de viktigste variablene bak modellresultatene ved å bruke `tuned RF` som hovedkilde, `baseline RF` som stabilitetskontroll og lineær regresjon som støttespor for fortegn.

## Kjøring

Kjør fra roten av `006 analysis`:

```bash
UV_CACHE_DIR=/tmp/uv-cache uv run python aktiviteter/15_viktige_variabler/start_wbs_5_4.py
```

## Filer i mappen

- `start_wbs_5_4.py`: Leser modellartefakter fra WBS 4.x og WBS 5.3, validerer input og skriver tabeller for viktige variabler.
- `tab_rf_tuned_feature_importance.csv`: Full feature importance-tabell for `tuned RF`.
- `tab_toppsignaler_per_modell.csv`: Topp 10 signaler per modellspor i fast modellrekkefølge.
- `tab_rf_stabilitet_topp10.csv`: Sammenligner unionen av topp 10-signalene i `baseline RF` og `tuned RF`.
- `tab_viktige_variabler_oversikt.csv`: Operativ 5.4-prioritering av de viktigste variablene basert på `tuned RF`.
- `tab_variabelgrupper_tuned_top10.csv`: Oppsummerer tuned-RF topp 10 per variabelgruppe.
- `variabelanalyse.md`: Kort norsk oppsummering av prioritering, RF-stabilitet og avgrensning mot senere tolkning.

## Datakilder

- `006 analysis/aktiviteter/14_sammenligne_modellresultater/tab_modellsammenligning_oversikt.csv`
- `006 analysis/aktiviteter/08_lineaer_regresjon/tab_lr_koeffisienter.csv`
- `006 analysis/aktiviteter/09_random_forest_regressor/tab_rf_feature_importance.csv`
- `006 analysis/aktiviteter/11_parameterjustering_random_forest/model_random_forest_tuned.joblib`
- `006 analysis/aktiviteter/06_datasplitt/X_train.csv`

## Viktige valg

- WBS 5.4 trener ikke modeller på nytt og beregner ikke nye prognoser eller metrikker.
- `tuned RF` brukes som primær rangeringskilde fordi modellen er anbefalt i WBS 5.3.
- `baseline RF` brukes kun for å vise hvor stabilt Random Forest-signalbildet er før og etter tuning.
- Lineær regresjon brukes kun som støttespor for fortegn og relativ plassering; koeffisienter sammenlignes ikke direkte med RF-importance.
- Variabler grupperes i `pris/kampanje`, `kalender`, `region`, `by`, `kategori` og `underkategori` for en kort, sporbar oppsummering.

## Neste steg

- Tolke modellresultater og variabelsignaler videre i WBS 6.1.
- Diskutere styrker og svakheter i WBS 6.2.
- Vurdere praktisk nytte for caset i WBS 6.3.
