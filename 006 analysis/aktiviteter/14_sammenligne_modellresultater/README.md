# 14 Sammenligne modellresultater (WBS 5.3)

Denne aktiviteten sammenligner modellresultatene fra WBS 5.2 og peker ut en samlet anbefalt modell for videre analyse.

## Kjøring

Kjør fra roten av `006 analysis`:

```bash
UV_CACHE_DIR=/tmp/uv-cache uv run python aktiviteter/14_sammenligne_modellresultater/start_wbs_5_3.py
```

## Filer i mappen

- `start_wbs_5_3.py`: Leser metrikktabellene fra WBS 5.2, validerer input og skriver sammenligningsartefakter.
- `tab_modellsammenligning_oversikt.csv`: Samlet rangering, deltaer og vurdering for hver modell.
- `tab_maanedlige_modellvinnere.csv`: Månedlig vinner på `RMSE` og `MAPE`, samt markering av om metrikkene peker på samme modell.
- `tab_modellvinner_telling.csv`: Oppsummerer hvor mange måneder hver modell vinner per metrikk.
- `modellsammenligning.md`: Norsk oppsummering av sammenligningsregel, totalrangering og viktigste metrikkavvik.

## Datakilder

- `006 analysis/aktiviteter/13_rmse_og_mape/tab_rmse_mape_oversikt.csv`
- `006 analysis/aktiviteter/13_rmse_og_mape/tab_rmse_mape_maaned.csv`

## Viktige valg

- WBS 5.3 bruker samlet `RMSE` for hele 2025 som hovedregel for anbefalt modell.
- Samlet `MAPE` brukes som sekundær regel ved lik `RMSE`, og månedlige `RMSE`-seire brukes som neste tie-break.
- Modellrekkefølgen beholdes som `benchmark lineær`, `baseline RF`, `tuned RF`.
- Aktiviteten dokumenterer metrikk-sprik mellom måneder, men går ikke inn i variabeltolkning eller årsaksforklaring.

## Neste steg

- Analysere viktige variabler i WBS 5.4.
- Tolke modellresultater videre i WBS 6.1.
- Diskutere styrker, svakheter og praktisk nytte i WBS 6.2 og WBS 6.3.
