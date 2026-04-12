# 18 Vurdere praktisk nytte (WBS 6.3)

Denne aktiviteten oversetter eksisterende modellfunn fra WBS 5.3, 5.4, 6.1 og 6.2 til praktisk beslutningsstøtte for Dagligvare, uten ny modelltrening, nye prognoser eller operative optimeringsmodeller.

## Kjøring

Kjør fra roten av `006 analysis`:

```bash
UV_CACHE_DIR=/tmp/uv-cache uv run python aktiviteter/18_vurdere_praktisk_nytte/start_wbs_6_3.py
```

## Filer i mappen

- `start_wbs_6_3.py`: Leser tidligere artefakter, validerer kildene og skriver beslutningsmatrise, bruksregler og markdown-oppsummering.
- `tab_beslutningsmatrise_6_3.csv`: Semi-kvantitativ vurdering av praktisk nytte per beslutningsområde.
- `tab_bruksregler_6_3.csv`: Konkrete bruksregler for standard planlegging, rabattfølsomme situasjoner, høyt salgsnivå og forklaringsbehov.
- `praktisk_nytte.md`: Kort norsk oppsummering av hvordan modellfunnene kan brukes i praksis innenfor prosjektets scope.

## Datakilder

- `006 analysis/aktiviteter/14_sammenligne_modellresultater/tab_modellsammenligning_oversikt.csv`
- `006 analysis/aktiviteter/14_sammenligne_modellresultater/tab_modellvinner_telling.csv`
- `006 analysis/aktiviteter/15_viktige_variabler/tab_viktige_variabler_oversikt.csv`
- `006 analysis/aktiviteter/16_tolke_modellresultater/tab_segmentvinnere_tolkning.csv`
- `006 analysis/aktiviteter/17_styrker_og_svakheter/tab_modellprofil_6_2.csv`
- `006 analysis/aktiviteter/17_styrker_og_svakheter/styrker_og_svakheter.md`
- `012 fase 2 - plan/core.json`

## Viktige valg

- WBS 6.3 trener ikke modeller på nytt og beregner ikke nye prognosemetrikker.
- `tuned RF` behandles som standardmodell fordi WBS 5.3 allerede har pekt den ut som samlet anbefalt modell.
- Aktiviteten er semi-kvantitativ: den bruker eksisterende tall som `RMSE`, `MAPE`, vinneropptellinger og segmentmønstre, men innfører ikke kroner, lageroptimalisering eller bemanningsalgoritmer.
- `benchmark lineær` brukes som forklaringsstøtte der tolkbarhet er viktig, mens `baseline RF` brukes som ekstra prosentfeil-kontroll i høyrabatt-situasjoner.
- Praktisk nytte vurderes bare innenfor prosjektets faktiske scope for Dagligvare og skal ikke leses som kausal eller allmenn forretningssannhet.

## Neste steg

- Bygge videre rapportkapitlene i WBS 7.x med mer fullstendig case-, metode-, resultat- og konklusjonstekst.
- Rydde eventuelle gjenværende navneavvik i rapport og planfiler dersom de berørte filene senere åpnes for videre redigering.
