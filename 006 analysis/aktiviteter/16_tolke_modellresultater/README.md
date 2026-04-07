# 16 Tolke modellresultater (WBS 6.1)

Denne aktiviteten tolker modellresultatene fra WBS 5.2, 5.3 og 5.4 ved å kombinere månedsbias, segmenterte metrikker og de viktigste variabelsignalene fra den anbefalte modellen.

## Kjøring

Kjør fra roten av `006 analysis`:

```bash
UV_CACHE_DIR=/tmp/uv-cache uv run python aktiviteter/16_tolke_modellresultater/start_wbs_6_1.py
```

## Filer i mappen

- `start_wbs_6_1.py`: Leser 5.x-artefakter, validerer input og skriver tolkningstabeller og markdown-oppsummering.
- `tab_bias_maaned_modell.csv`: Månedlig bias per modell, sammen med månedlige `RMSE`-/`MAPE`-verdier og modellvinnere.
- `tab_segmentdefinisjoner.csv`: Dokumenterer segmentene som brukes i 6.1.
- `tab_segmentmetrikk_modell.csv`: Segmentert `RMSE` og `MAPE` per modellspor.
- `tab_segmentvinnere_tolkning.csv`: Oppsummerer vinner på `RMSE` og `MAPE` per segment.
- `modelltolkning.md`: Kort norsk oppsummering av månedsmønstre, metrikk-sprik og kobling til viktige variabler.

## Datakilder

- `006 analysis/aktiviteter/12_prognoser_2025/tab_prognoser_2025_maaned.csv`
- `006 analysis/aktiviteter/13_rmse_og_mape/tab_prognosefeil_2025_detalj.csv`
- `006 analysis/aktiviteter/13_rmse_og_mape/tab_rmse_mape_maaned.csv`
- `006 analysis/aktiviteter/14_sammenligne_modellresultater/tab_modellsammenligning_oversikt.csv`
- `006 analysis/aktiviteter/14_sammenligne_modellresultater/tab_maanedlige_modellvinnere.csv`
- `006 analysis/aktiviteter/15_viktige_variabler/tab_viktige_variabler_oversikt.csv`

## Viktige valg

- WBS 6.1 trener ikke modeller på nytt og lager ikke nye prognoser.
- `tuned RF` brukes som hovedmodell fordi den er anbefalt i WBS 5.3.
- Segmentene er låst til `quarter`, `discount_band`, `Region` og `sales_band`.
- `sales_band` er en tolkingsdimensjon basert på tertiler av `Sales_faktisk` i 2025-testsettet og brukes kun for å forstå metrikk-sprik.
- Aktiviteten beskriver observerte mønstre og kobler dem til signalene fra WBS 5.4, men går ikke inn i kausal analyse, generell modellkritikk eller praktiske anbefalinger.

## Neste steg

- Diskutere styrker og svakheter i WBS 6.2.
- Vurdere praktisk nytte i WBS 6.3.
- Bygge videre rapportkapitlene i WBS 7.x.
