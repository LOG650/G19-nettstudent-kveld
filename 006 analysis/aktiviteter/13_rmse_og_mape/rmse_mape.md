# RMSE og MAPE for 2025 (WBS 5.2)

## Hva WBS 5.2 gjør

- Aktiviteten beregner test-`RMSE` og test-`MAPE` for de tre modellsporene fra WBS 5.1.
- Resultatene dokumenteres både samlet for hele 2025, per måned og som detaljert feilgrunnlag på radnivå.
- WBS 5.2 rangerer ikke modellene; selve sammenligningen og tolkningen er utsatt til WBS 5.3.

## Datagrunnlag

- Input detaljtabell: `12_prognoser_2025/tab_prognoser_2025_detalj.csv`
- Input modelloversikt: `12_prognoser_2025/tab_prognosemodeller_oversikt.csv`
- Antall 2025-observasjoner: 3312
- Månedlig dekning: `2025-01` til `2025-12`

## Metrikkdefinisjon

- `RMSE` beregnes som `root_mean_squared_error(faktisk, prognose)`.
- `MAPE` beregnes som `mean_absolute_percentage_error(faktisk, prognose) * 100` og rapporteres i prosent.

## Samlede 2025-resultater

- `benchmark lineær`: `RMSE=580.394322` og `MAPE=44.1840 %`
- `baseline RF`: `RMSE=589.284744` og `MAPE=44.1162 %`
- `tuned RF`: `RMSE=578.259649` og `MAPE=43.9706 %`

## Produserte artefakter

- `tab_rmse_mape_oversikt.csv`
- `tab_rmse_mape_maaned.csv`
- `tab_prognosefeil_2025_detalj.csv`
- `rmse_mape.md`

## Avgrensning mot senere WBS-steg

- WBS 5.2 gjør ikke modellrangering, anbefaling, figurer eller tolkning av hvorfor en modell gjør det bedre enn en annen.
- WBS 5.3 bruker metrikktabellene og feilgrunnlaget fra WBS 5.2 som input til selve sammenligningen av modellresultater.
