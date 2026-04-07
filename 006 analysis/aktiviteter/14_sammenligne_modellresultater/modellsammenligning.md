# Sammenligning av modellresultater (WBS 5.3)

## Hva WBS 5.3 gjør

- Aktiviteten sammenligner modellresultatene fra WBS 5.2 uten å trene modeller på nytt eller beregne nye prognoser.
- Samlet `RMSE` for hele 2025 brukes som hovedregel, mens samlet `MAPE` brukes som sekundær regel ved lik `RMSE`.
- Månedlige vinnere brukes som støtteforklaring for å vise hvor stabil modellen er gjennom året.

## Samlet anbefaling

- WBS 5.3 anbefaler `tuned RF` som samlet modell for videre analyse, fordi modellen er best på total `RMSE` og samtidig også best på total `MAPE`.
- Rang 1 samlet: `tuned RF` (`RMSE=578.259649`, `MAPE=43.9706 %`)
- Rang 2 samlet: `benchmark lineær` (`RMSE=580.394322`, `MAPE=44.1840 %`)
- Rang 3 samlet: `baseline RF` (`RMSE=589.284744`, `MAPE=44.1162 %`)

## Viktigste deltaer

- `tuned RF` mot `benchmark lineær`: `delta RMSE=-2.134673` og `delta MAPE=-0.2134` prosentpoeng.
- `baseline RF` mot `benchmark lineær`: `delta RMSE=8.890422` og `delta MAPE=-0.0678` prosentpoeng.
- `tuned RF` mot `baseline RF`: `delta RMSE=-11.025095` og `delta MAPE=-0.1456` prosentpoeng.

## Månedsbilde

- Samme vinner på `RMSE` og `MAPE` forekommer i `2` av `12` måneder.
- Måneder med metrikk-sprik: `2025-01`, `2025-02`, `2025-03`, `2025-04`, `2025-05`, `2025-06`, `2025-08`, `2025-10`, `2025-11`, `2025-12`.

### Vinnermåneder per metrikk

- `RMSE`: `benchmark lineær` vinner `1` måneder.
- `RMSE`: `baseline RF` vinner `0` måneder.
- `RMSE`: `tuned RF` vinner `11` måneder.
- `MAPE`: `benchmark lineær` vinner `3` måneder.
- `MAPE`: `baseline RF` vinner `6` måneder.
- `MAPE`: `tuned RF` vinner `3` måneder.

## Produserte artefakter

- `tab_modellsammenligning_oversikt.csv`
- `tab_maanedlige_modellvinnere.csv`
- `tab_modellvinner_telling.csv`
- `modellsammenligning.md`

## Avgrensning mot senere WBS-steg

- WBS 5.3 sammenligner modeller, men går ikke inn i variabeltolkning, residualdiagnostikk eller årsaksforklaring.
- WBS 5.4 og WBS 6.x tar videre arbeid med viktige variabler, faglig tolkning og diskusjon.
