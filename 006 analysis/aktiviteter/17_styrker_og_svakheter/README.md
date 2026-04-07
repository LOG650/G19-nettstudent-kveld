# 17 Diskutere styrker og svakheter (WBS 6.2)

Denne aktiviteten diskuterer styrker og svakheter i modellresultatene oppå WBS 5.3, 5.4 og 6.1, uten ny modelltrening, nye prognoser eller nye evalueringsmetrikker.

## Kjøring

Kjør fra roten av `006 analysis`:

```bash
UV_CACHE_DIR=/tmp/uv-cache uv run python aktiviteter/17_styrker_og_svakheter/start_wbs_6_2.py
```

## Filer i mappen

- `start_wbs_6_2.py`: Leser tidligere artefakter, validerer kildene og skriver diskusjonstabeller og markdown-oppsummering.
- `tab_modellprofil_6_2.csv`: Samlet modellprofil med totalmetrikker, vinneropptellinger, tolkbarhetsnivå og hovedstyrke/-svakhet per modell.
- `tab_diskusjonspunkter_oversikt.csv`: Sporbar long-format-tabell med styrker og svakheter på modell- og prosjektnivå.
- `tab_metodebegrensninger_6_2.csv`: Eksplisitt oversikt over metodebegrensninger med konsekvenser for pålitelighet og generaliserbarhet.
- `styrker_og_svakheter.md`: Kort norsk oppsummering av modellstyrker, modellsvakheter og prosjektbegrensninger.

## Datakilder

- `006 analysis/aktiviteter/14_sammenligne_modellresultater/tab_modellsammenligning_oversikt.csv`
- `006 analysis/aktiviteter/14_sammenligne_modellresultater/tab_modellvinner_telling.csv`
- `006 analysis/aktiviteter/15_viktige_variabler/tab_viktige_variabler_oversikt.csv`
- `006 analysis/aktiviteter/16_tolke_modellresultater/tab_segmentvinnere_tolkning.csv`
- `006 analysis/aktiviteter/04_dataprosessering/tab_renselogg.csv`
- `006 analysis/aktiviteter/05_feature_engineering/feature_engineering.md`
- `006 analysis/aktiviteter/06_datasplitt/datasplitt.md`
- `006 analysis/aktiviteter/08_lineaer_regresjon/lineaer_regresjon.md`
- `006 analysis/aktiviteter/11_parameterjustering_random_forest/random_forest_tuning.md`
- `012 fase 2 - plan/prosjektstyringsplan.md`

## Viktige valg

- WBS 6.2 beregner ikke nye prognoser og trener ikke modellene på nytt.
- `tuned RF` behandles som hovedmodell fordi WBS 5.3 allerede har pekt den ut som samlet anbefalt modell.
- Diskusjonen skilles eksplisitt mellom `pålitelighet` i dette prosjektoppsettet og `generaliserbarhet` utover den simulerte virksomheten.
- Hver styrke og svakhet kobles til konkrete artefakter for å holde diskusjonen sporbar.
- Aktiviteten følger faktiske 6.1-data dersom planantagelser og artefakter ikke stemmer helt overens.

## Neste steg

- Vurdere praktisk nytte i WBS 6.3.
- Bygge videre diskusjon, konklusjon og helhetlig rapportstruktur i WBS 7.x.
