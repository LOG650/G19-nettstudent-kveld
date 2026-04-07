# 13 RMSE og MAPE (WBS 5.2)

Denne aktiviteten beregner `RMSE` og `MAPE` for de tre modellsporene fra WBS 5.1 og dokumenterer resultatene både samlet for hele 2025, per måned og som detaljert feilgrunnlag.

## Kjøring

Kjør fra roten av `006 analysis`:

```bash
UV_CACHE_DIR=/tmp/uv-cache uv run python aktiviteter/13_rmse_og_mape/start_wbs_5_2.py
```

## Filer i mappen

- `start_wbs_5_2.py`: Leser prognosetabellene fra WBS 5.1, validerer input og skriver metrikktabeller og detaljert feilgrunnlag.
- `tab_rmse_mape_oversikt.csv`: Samlet `RMSE` og `MAPE` for hele 2025 per modellspor.
- `tab_rmse_mape_maaned.csv`: Månedlig `RMSE` og `MAPE` i long-format per modellspor.
- `tab_prognosefeil_2025_detalj.csv`: Radnivåtabell som bygger videre på WBS 5.1 med feil, absoluttfeil og `APE` per modellspor.
- `rmse_mape.md`: Norsk oppsummering av datagrunnlag, metrikkdefinisjon og totalresultater for 2025.

## Datakilder

- `006 analysis/aktiviteter/12_prognoser_2025/tab_prognoser_2025_detalj.csv`
- `006 analysis/aktiviteter/12_prognoser_2025/tab_prognosemodeller_oversikt.csv`

## Viktige valg

- WBS 5.2 bruker WBS 5.1 som eneste sannhetskilde for 2025-prognosene og trener ikke modellene på nytt.
- `RMSE` beregnes med `root_mean_squared_error`, og `MAPE` beregnes med `mean_absolute_percentage_error * 100`.
- Modellrekkefølgen beholdes fra WBS 5.1 for å sikre sporbarhet mellom prognoser, metrikker og senere sammenligning.
- Detaljert feilgrunnlag lagres som `prognose - faktisk`, absoluttfeil og `APE` i prosent for hvert modellspor.

## Neste steg

- Sammenligne modellresultater i WBS 5.3.
- Analysere viktige variabler videre i WBS 5.4.
- Tolke og diskutere modellprestasjonene videre i WBS 6.1 og 6.2.
