# 10 Felles treningsoppsummering (WBS 4.3)

Denne aktiviteten verifiserer at lineær regresjon fra WBS 4.1 og Random Forest Regressor fra WBS 4.2 bygger på samme treningsgrunnlag, og samler de viktigste modellinterne signalene i felles artefakter.

## Kjøring

Kjør fra roten av `006 analysis`:

```bash
UV_CACHE_DIR=/tmp/uv-cache uv run python aktiviteter/10_felles_treningsoppsummering/start_wbs_4_3.py
```

## Filer i mappen

- `start_wbs_4_3.py`: Leser modellartefakter fra WBS 4.1 og 4.2, verifiserer felles inputgrunnlag og skriver samlefiler.
- `tab_modelltrening_oversikt.csv`: Felles oversikt over modellene, treningsgrunnlaget og om lokale modellfiler finnes.
- `tab_modellsignaler_oversikt.csv`: Samler de fem sterkeste signalene per modell i én tabell.
- `modelltrening_verifisering.md`: Kort norsk oppsummering av hva WBS 4.3 verifiserer og hva aktiviteten ikke omfatter.

## Datakilder

- `006 analysis/aktiviteter/08_lineaer_regresjon/tab_lr_modelloversikt.csv`
- `006 analysis/aktiviteter/08_lineaer_regresjon/tab_lr_koeffisienter.csv`
- `006 analysis/aktiviteter/09_random_forest_regressor/tab_rf_modelloversikt.csv`
- `006 analysis/aktiviteter/09_random_forest_regressor/tab_rf_feature_importance.csv`

## Viktige valg

- WBS 4.3 trener ikke modellene på nytt; selve treningen er allerede gjennomført i WBS 4.1 og WBS 4.2.
- Aktiviteten feiler eksplisitt hvis modellene ikke peker til samme feature-matrise, target-fil, radantall, feature-antall og target-kolonne.
- `.joblib`-filene er valgfrie i dette steget og brukes bare som lokal tilleggsinformasjon hvis de finnes.
- Omtolkningen av WBS 4.3 fra ny trening til felles verifisering og oppsummering er dokumentert i `012 fase 2 - plan/endringslogg.md`.

## Neste steg

- Justere modellparametere i WBS 4.4 ved behov.
- Generere prognoser og beregne evalueringsmål i WBS 5.x.
- Tolke modellresultater og begrensninger i WBS 6.1 og 6.2.
