# Statusliste

Oppdatert: 2026-03-26

Denne statuslisten er generert med utgangspunkt i [prosjektstyringsplan.md](/home/erikb/himolde/log650/G19-nettstudent-kveld/012 fase 2 - plan/prosjektstyringsplan.md) og tilgjengelige prosjektartefakter i repoet. Punkter er merket som `verifisert` når de kan knyttes til eksisterende filer eller mappestruktur. Øvrige punkter er vurdert som planstatus per dato og må bekreftes av prosjektgruppen.

## Overordnet status

- [x] Prosjektstyringsplan er etablert og datert 2026-03-10. `verifisert`
- [x] Prosjektforslag finnes i fase 1. `verifisert`
- [x] Datasett er tilgjengelig i prosjektmappen. `verifisert`
- [x] Analysearbeid i egen `006 analysis`-mappe er etablert med felles Python/uv-oppsett. `verifisert`
- [ ] Statusgrunnlaget for modellutvikling er delvis dokumentert gjennom feature engineering og datasplitt, men evaluering og rapportarbeid er ikke dokumentert i repoet ennå. `delvis verifisert`

## Status per hovedaktivitet

- [x] A: Problemdefinisjon og prosjektplan er gjennomført eller langt på vei ferdigstilt, siden prosjektforslag og prosjektstyringsplan foreligger. `verifisert delvis gjennom artefakter`
- [x] B: Datainnsamling og dokumentasjon ser ut til å være påbegynt eller gjennomført, siden datasettet finnes i prosjektet. `verifisert delvis gjennom artefakter`
- [x] C: Dataforståelse, variabelanalyse og datasettdokumentasjon er dokumentert for WBS 2.2-2.4 i analyseområdet. `verifisert`
- [x] D: Datapreprosessering er dokumentert for WBS 3.1-3.3, mens eksplorativ analyse og visualisering fortsatt gjenstår. `verifisert delvis gjennom artefakter`
- [x] E: Feature engineering er dokumentert i analyseområdet med eget feature-datasett og dokumenterte featurevalg. `verifisert`
- [ ] F: Modellbygging og trening er ikke dokumentert i repoet ennå. `må bekreftes`
- [ ] G: Analyse og evaluering er ikke dokumentert i repoet ennå. `må bekreftes`
- [ ] H: Rapportskriving er ikke dokumentert i rapportmappen ennå utover tidligere faseleveranser. `må bekreftes`
- [ ] I: Konklusjon og presentasjon er ikke startet ifølge planlagt rekkefølge. `antatt`

## Milepælstatus mot plan

- [x] M1: Prosjektforslag godkjent, planlagt i februar. Prosjektforslag finnes i repoet. `verifisert delvis gjennom artefakt`
- [x] M2: Datagrunnlag klargjort, planlagt 10. mars. Datasett finnes, men graden av klargjøring bør bekreftes. `delvis verifisert`
- [ ] M3: Testing av modellene, planlagt 23. mars. Ikke dokumentert som fullført per 2026-03-19. `forventet neste milepæl`
- [ ] M4: Modelloptimalisering ferdig, planlagt 22. april. `ikke startet / ikke bekreftet`
- [ ] M5: Hovedutkast av rapport, planlagt 8. april. `ikke startet / ikke bekreftet`
- [ ] M6: Endelig rapport levert, planlagt 19. mai. `ikke startet / ikke bekreftet`

## Risiko- og oppfølgingspunkter

- [x] Bekrefte om datasettet er renset og grunnleggende validert, siden dette er en sentral risiko i planen. `fullført 2026-03-26`
- [x] Opprette eller dokumentere analysearbeid i strukturert analysemiljø, slik planen og arbeidsreglene legger opp til. `fullført 2026-03-19`
- [x] Dokumentasjon for WBS 2.2 (utforske datastruktur og variabler) er etablert med skript, tabeller og figur. `fullført 2026-03-19`
- [x] Dokumentasjon for WBS 2.3 (identifisere relevante variabler) er etablert med skript, tabeller og figur. `fullført 2026-03-19`
- [x] Dokumentasjon for WBS 2.4 (dokumentere datasett) er etablert med tabellprofil og markdown-oppsummering. `fullført 2026-03-19`
- [x] Dokumentasjon for WBS 3.1 (rense data) er etablert med skript, renselogg, kolonneprofil og renset datasett. `fullført 2026-03-26`
- [x] Dokumentasjon for WBS 3.2 (feature engineering) er etablert med feature-datasett, featurevalg og markdown-oppsummering. `fullført 2026-03-26`
- [x] Dokumentasjon for WBS 3.3 (splitte trenings- og testdata) er etablert med train/test-filer og splittrapport som bygger på WBS 3.2. `fullført 2026-03-26`
- [ ] Dokumentere status for lineær regresjon og Random Forest separat.
- [ ] Etablere sporbar status for MAPE, RMSE og modelltesting før milepæl M3.
- [x] Bruke renset datasett som grunnlag for datasplitt og videre feature engineering. `fullført 2026-03-26`
- [ ] Starte løpende rapportskriving parallelt med analysearbeidet, i tråd med arbeidsreglene i prosjektet.
- [ ] Oppdatere denne statuslisten etter ukentlige statusmøter og ved milepæler.

## Anbefalt kort prosjektstatus

Prosjektet fremstår per 2026-03-26 som værende ferdig med planfasen, med dataforståelse, datasettdokumentasjon, remappet datarensing, feature engineering og datasplitt dokumentert i analyseområdet. Neste kritiske behov er å bygge og trene de planlagte modellene, slik at videre status kan følges opp med faktiske modellresultater og ikke bare klargjort datagrunnlag.
