# Statusliste

Oppdatert: 2026-04-02

Denne statuslisten er generert med utgangspunkt i [prosjektstyringsplan.md](/home/erikb/himolde/log650/G19-nettstudent-kveld/012 fase 2 - plan/prosjektstyringsplan.md) og tilgjengelige prosjektartefakter i repoet. Punkter er merket som `verifisert` når de kan knyttes til eksisterende filer eller mappestruktur. Øvrige punkter er vurdert som planstatus per dato og må bekreftes av prosjektgruppen. Omtolkningen av WBS 4.3 er dokumentert i [endringslogg.md](endringslogg.md).

## Overordnet status

- [x] Prosjektstyringsplan er etablert og datert 2026-03-10. `verifisert`
- [x] Prosjektforslag finnes i fase 1. `verifisert`
- [x] Datasett er tilgjengelig i prosjektmappen. `verifisert`
- [x] Analysearbeid i egen `006 analysis`-mappe er etablert med felles Python/uv-oppsett. `verifisert`
- [ ] Statusgrunnlaget for modellutvikling og første prognoseleveranse er nå dokumentert gjennom feature engineering, datasplitt, eksplorativ analyse, lineær regresjon i WBS 4.1, Random Forest i WBS 4.2, et lett felles verifiseringssteg i WBS 4.3, parameterjustering av Random Forest i WBS 4.4 og genererte 2025-prognoser i WBS 5.1, men evaluering og større deler av rapportarbeidet mangler fortsatt. `delvis verifisert`

## Status per hovedaktivitet

- [x] A: Problemdefinisjon og prosjektplan er gjennomført eller langt på vei ferdigstilt, siden prosjektforslag og prosjektstyringsplan foreligger. `verifisert delvis gjennom artefakter`
- [x] B: Datainnsamling og dokumentasjon ser ut til å være påbegynt eller gjennomført, siden datasettet finnes i prosjektet. `verifisert delvis gjennom artefakter`
- [x] C: Dataforståelse, variabelanalyse og datasettdokumentasjon er dokumentert for WBS 2.2-2.4 i analyseområdet. `verifisert`
- [x] D: Datapreprosessering og eksplorativ analyse er dokumentert for WBS 3.1-3.4 i analyseområdet. `verifisert`
- [x] E: Feature engineering er dokumentert i analyseområdet med eget feature-datasett og dokumenterte featurevalg. `verifisert`
- [x] F: Modellbygging er dokumentert med lineær regresjon i WBS 4.1, Random Forest i WBS 4.2, et felles verifiserings- og oppsummeringssteg i WBS 4.3 og parameterjustering av Random Forest i WBS 4.4. Lineær regresjon står fortsatt som fast benchmark, mens tuned Random Forest er etablert som videre operativ modell. Selve planendringene for 4.3 og 4.4 er dokumentert i `endringslogg.md`. `verifisert`
- [ ] G: Prognoser for 2025 er nå generert i WBS 5.1 for lineær regresjon, Random Forest-baseline og tuned Random Forest, men `RMSE`, `MAPE` og modellsammenligning er fortsatt ikke dokumentert. `delvis verifisert`
- [ ] H: Rapportskriving er påbegynt med korte metode- og modelleringsnotater om WBS 4.1, 4.2, 4.3, 4.4 og 5.1, men hoveddelen av rapportarbeidet er fortsatt ikke dokumentert i rapportmappen. `delvis verifisert`
- [ ] I: Konklusjon og presentasjon er ikke startet ifølge planlagt rekkefølge. `antatt`

## Milepælstatus mot plan

- [x] M1: Prosjektforslag godkjent, planlagt i februar. Prosjektforslag finnes i repoet. `verifisert delvis gjennom artefakt`
- [x] M2: Datagrunnlag klargjort, planlagt 10. mars. Datasett finnes, men graden av klargjøring bør bekreftes. `delvis verifisert`
- [ ] M3: Testing av modellene, planlagt 23. mars. Prognoser for 2025 er nå generert i WBS 5.1, men evalueringsmetrikker og formell modelltesting gjenstår fortsatt per 2026-04-02. `delvis oppnådd`
- [x] M4: Modelloptimalisering ferdig, planlagt 22. april. WBS 4.4 dokumenterer parameterjustering av Random Forest med 2024 som intern validering. `verifisert 2026-04-02`
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
- [x] Dokumentasjon for WBS 3.4 (eksplorativ analyse og visualisering) er etablert med EDA-tabeller, figurer og markdown-oppsummering. `fullført 2026-03-26`
- [x] Dokumentasjon for WBS 4.1 (implementere lineær regresjon) er etablert med skript, modellfil, modelloversikt, koeffisienttabell og markdown-oppsummering. `fullført 2026-03-30`
- [x] Dokumentasjon for WBS 4.2 (implementere Random Forest Regressor) er etablert med skript, modellfil, modelloversikt, feature importance-tabell og markdown-oppsummering. `fullført 2026-03-30`
- [x] Dokumentasjon for WBS 4.3 (trene modellene) er etablert som et lett felles verifiserings- og oppsummeringssteg med samlefiler for treningsgrunnlag og modellsignaler. `fullført 2026-04-02`
- [x] Dokumentasjon for WBS 4.4 (justere modellparametere) er etablert med kandidatgrid, valideringsmetrikker for 2024, vinneroversikt og retrent tuned Random Forest-modell. `fullført 2026-04-02`
- [x] Dokumentasjon for WBS 5.1 (generere prognoser for 2025) er etablert med radvise prognoser, månedlig oppsummering og tre dokumenterte modellspor for 2025. `fullført 2026-04-02`
- [x] Planendringen for WBS 4.3 er dokumentert i egen endringslogg med begrunnelse og konsekvens for videre arbeid. `fullført 2026-04-02`
- [x] Avgrensningen av WBS 4.4 til tuning av Random Forest er dokumentert i egen endringslogg med begrunnelse og konsekvens for videre arbeid. `fullført 2026-04-02`
- [ ] Etablere sporbar status for MAPE, RMSE og modelltesting før milepæl M3.
- [x] Bruke renset datasett som grunnlag for datasplitt og videre feature engineering. `fullført 2026-03-26`
- [x] Starte løpende rapportskriving parallelt med analysearbeidet, i tråd med arbeidsreglene i prosjektet. `påbegynt 2026-03-30 og utvidet 2026-04-02 med modellnotater for WBS 4.1, 4.2, 4.3, 4.4 og 5.1`
- [ ] Oppdatere denne statuslisten etter ukentlige statusmøter og ved milepæler.

## Anbefalt kort prosjektstatus

Prosjektet fremstår per 2026-04-02 som værende ferdig med planfasen, med dataforståelse, datasettdokumentasjon, remappet datarensing, feature engineering, datasplitt, eksplorativ analyse, lineær regresjon for WBS 4.1, Random Forest for WBS 4.2, felles verifisering av treningsgrunnlaget i WBS 4.3, parameterjustering av Random Forest i WBS 4.4 og genererte 2025-prognoser i WBS 5.1 dokumentert i analyseområdet. Neste kritiske behov er å beregne evalueringsmål og sammenligne modellene på 2025-data, slik at videre status kan følges opp med faktiske modellprestasjoner og ikke bare prognosefiler.
