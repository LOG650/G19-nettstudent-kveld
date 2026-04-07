# Tolkning av modellresultater (WBS 6.1)

## Hva WBS 6.1 gjør

- Aktiviteten tolker observerte modellmønstre på toppen av WBS 5.2, 5.3 og 5.4 uten å trene modeller på nytt eller lage nye prognoser.
- `tuned RF` brukes som hovedmodell fordi den er anbefalt i WBS 5.3.
- Tolkningen er avgrenset til observerte mønstre i månedsbias og segmenterte metrikker. Aktiviteten gjør ikke kausal analyse, diskuterer ikke generelle styrker og svakheter, og gir ikke forretningsanbefalinger.

## Månedsbilde for anbefalt modell

- `tuned RF` vinner `RMSE` i `11` av `12` måneder, men bare `MAPE` i `3` av `12` måneder.
- Størst negativ månedsbias for `tuned RF` er `2025-08` (`bias_sum=-20548.2807`, `bias_pct=-5.2193 %`), etterfulgt av `2025-09` (`bias_sum=-16333.7299`, `bias_pct=-2.7713 %`).
- Størst positiv månedsbias for `tuned RF` er `2025-12` (`bias_sum=11073.8228`, `bias_pct=2.3626 %`).
- Månedsmønsteret viser at modellen følger totalnivået godt i absolutte termer, men at prosentfeilen svinger mer mellom måneder med ulikt salgsnivå.

## Segmenter som forklarer metrikk-sprik

- `quarter`: `tuned RF` vinner `RMSE` i alle fire kvartaler, mens `MAPE` vinnes av `benchmark lineær` i Q1, `baseline RF` i Q2, `tuned RF` i Q3 og `benchmark lineær` i Q4.
- `discount_band`: `tuned RF` vinner både `RMSE` og `MAPE` ved `lav` og `middels` rabatt, mens `MAPE` ved `hoy` rabatt vinnes av `baseline RF`.
- `Region`: `tuned RF` vinner `RMSE` i alle fire regioner, mens `MAPE` vinnes av `benchmark lineær` i `Central`, `tuned RF` i `East`, `tuned RF` i `South` og `baseline RF` i `West`.
- `sales_band`: `RMSE` vinnes av `tuned RF` for `lavt salg`, `tuned RF` for `middels salg` og `benchmark lineær` for `hoyt salg`, mens `MAPE` vinnes av `baseline RF`, `tuned RF` og `benchmark lineær` i de samme segmentene.
- Tertilgrensene for `sales_band` er `1179.0` og `1828.0`, slik at segmentene brukes som ren tolkningsstøtte for å forstå hvorfor absolutt feil og prosentfeil reagerer forskjellig.

## Kobling til viktige variabler fra WBS 5.4

- `Discount` er prioritet `1` i WBS 5.4 og støtter at rabattsegmentene er sentrale for å forklare forskjeller i prosentfeil mellom modellene.
- `quarter` er et toppsignal i `tuned RF` med rang `7` i WBS 5.4 og støtter at kvartalsmønstre brukes som tolkningsakse i 6.1.
- Regionfeature-ene `Region_East`, `Region_West`, `Region_Central` ligger høyt i WBS 5.4 og henger sammen med at MAPE-vinneren varierer mellom `Central`, `East`, `South` og `West`.
- `sales_band` er ikke en modellfeature, men et avledet tolkningssegment som brukes for å forklare hvorfor `RMSE` og `MAPE` ikke alltid peker på samme modell.

## Produserte artefakter

- `tab_bias_maaned_modell.csv`
- `tab_segmentdefinisjoner.csv`
- `tab_segmentmetrikk_modell.csv`
- `tab_segmentvinnere_tolkning.csv`
- `modelltolkning.md`

## Avgrensning mot senere WBS-steg

- WBS 6.1 beskriver observerte mønstre og kobler dem til signalene fra WBS 5.4.
- WBS 6.2 tar videre diskusjon av styrker og svakheter.
- WBS 6.3 tar videre vurdering av praktisk nytte for caset.
