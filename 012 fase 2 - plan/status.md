# Statusliste

Oppdatert: 2026-04-21 (F1 fra helhetsreview av 7.2 adressert: tabellhenvisninger i kap. 7 oppdatert til lokale Tabell 7.1/7.2)

Denne statuslisten er generert med utgangspunkt i [prosjektstyringsplan.md](/home/erikb/himolde/log650/G19-nettstudent-kveld/012 fase 2 - plan/prosjektstyringsplan.md) og tilgjengelige prosjektartefakter i repoet. Punkter er merket som `verifisert` når de kan knyttes til eksisterende filer eller mappestruktur. Øvrige punkter er vurdert som planstatus per dato og må bekreftes av prosjektgruppen. Omtolkningen av WBS 4.3 er dokumentert i [endringslogg.md](endringslogg.md).

## Overordnet status

- [x] Prosjektstyringsplan er etablert og datert 2026-03-10. `verifisert`
- [x] Prosjektforslag finnes i fase 1. `verifisert`
- [x] Datasett er tilgjengelig i prosjektmappen. `verifisert`
- [x] Analysearbeid i egen `006 analysis`-mappe er etablert med felles Python/uv-oppsett. `verifisert`
- [x] Statusgrunnlaget for modellutvikling, prognoseleveranse, evalueringsmetrikker, modellsammenligning, analyse av viktige variabler, tolkning av modellresultatene, diskusjon av styrker og svakheter og praktisk nytte er nå dokumentert gjennom feature engineering, datasplitt, eksplorativ analyse, lineær regresjon i WBS 4.1, Random Forest i WBS 4.2, et lett felles verifiseringssteg i WBS 4.3, parameterjustering av Random Forest i WBS 4.4, genererte 2025-prognoser i WBS 5.1, beregnede 2025-`RMSE`/`MAPE` i WBS 5.2, sammenligning av modellresultatene i WBS 5.3, variabelanalyse i WBS 5.4, tolkning i WBS 6.1, diskusjon i WBS 6.2 og praktisk nytte i WBS 6.3, men større deler av rapportarbeidet mangler fortsatt. `verifisert`

## Status per hovedaktivitet

- [x] A: Problemdefinisjon og prosjektplan er gjennomført eller langt på vei ferdigstilt, siden prosjektforslag og prosjektstyringsplan foreligger. `verifisert delvis gjennom artefakter`
- [x] B: Datainnsamling og dokumentasjon ser ut til å være påbegynt eller gjennomført, siden datasettet finnes i prosjektet. `verifisert delvis gjennom artefakter`
- [x] C: Dataforståelse, variabelanalyse og datasettdokumentasjon er dokumentert for WBS 2.2-2.4 i analyseområdet. `verifisert`
- [x] D: Datapreprosessering og eksplorativ analyse er dokumentert for WBS 3.1-3.4 i analyseområdet. `verifisert`
- [x] E: Feature engineering er dokumentert i analyseområdet med eget feature-datasett og dokumenterte featurevalg. `verifisert`
- [x] F: Modellbygging er dokumentert med lineær regresjon i WBS 4.1, Random Forest i WBS 4.2, et felles verifiserings- og oppsummeringssteg i WBS 4.3 og parameterjustering av Random Forest i WBS 4.4. Lineær regresjon står fortsatt som fast benchmark, mens tuned Random Forest er etablert som videre operativ modell. Selve planendringene for 4.3 og 4.4 er dokumentert i `endringslogg.md`. `verifisert`
- [x] G: Prognoser for 2025, `RMSE`/`MAPE`, modellsammenligning, analyse av viktige variabler, tolkning av modellmønstre, diskusjon av styrker og svakheter og praktisk nytte er nå dokumentert i WBS 5.1, 5.2, 5.3, 5.4, 6.1, 6.2 og 6.3 for lineær regresjon, Random Forest-baseline og tuned Random Forest. `tuned RF` fremstår samlet som anbefalt modell på 2025-data, vinner `RMSE` i de fleste måneder og segmenter, og er nå oversatt til praktisk beslutningsstøtte for innkjøp, lager, kampanjevurdering, ressursplanlegging og ledelsesrapportering. `verifisert`
- [ ] H: Rapportskriving er langt på vei fullført: WBS 7.1.1–7.1.7 og hele WBS 7.2-blokken (7.2.1 utvalg, 7.2.2 case/data, 7.2.3 analyse/resultat/diskusjon og 7.2.4 innsetting) er dokumentert. Rapporten inneholder nå Sammendrag, Abstract, ferdigstilt innledning (inkl. ny §1.2 Delproblemer), problemstilling, avgrensinger, antagelser, litteratur, teori, casebeskrivelse, metode og data (med Tabell 5.2–5.5 og Figur 5.1–5.2), modellering (Tabell 6.1–6.2), analyse (Tabell 7.1–7.2, Figur 7.1–7.2), resultat (Tabell 8.1–8.4, Figur 8.1–8.3), diskusjon (9.1–9.5 med Tabell 9.1–9.3), konklusjon, bibliografi og vedlegg (Tabell 12.1). Rapportfasen er brutt ned i WBS 7.1.1–7.3.3, og gjenstående aktiviteter er 7.3.1 struktur- og kravsjekk, 7.3.2 konsistenssjekk og 7.3.3 språkvask og låsing av førsteutkastet. `delvis verifisert`
- [ ] I: Konklusjon og presentasjon er ikke startet som egen avslutningsfase, selv om rapporten nå har en ferdigskrevet konklusjon i WBS 7.1.6. `delvis verifisert`

## Milepælstatus mot plan

- [x] M1: Prosjektforslag godkjent, planlagt i februar. Prosjektforslag finnes i repoet. `verifisert delvis gjennom artefakt`
- [x] M2: Datagrunnlag klargjort, planlagt 10. mars. Datasett finnes, men graden av klargjøring bør bekreftes. `delvis verifisert`
- [x] M3: Testing av modellene, planlagt 23. mars. Prognoser for 2025, evalueringsmetrikker (`RMSE`/`MAPE`) og formell modellsammenligning er dokumentert per 2026-04-07. `verifisert forsinket`
- [x] M4: Modelloptimalisering ferdig, planlagt 22. april. WBS 4.4 dokumenterer parameterjustering av Random Forest med 2024 som intern validering. `verifisert 2026-04-02`
- [ ] M5: Hovedutkast av rapport, planlagt 8. april. Rapporten er utvidet med praktisk nytte og en kort konklusjonssetning, men hovedutkastet er fortsatt ikke ferdig per 2026-04-12. `forsinket`
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
- [x] Dokumentasjon for WBS 5.2 (beregne RMSE og MAPE) er etablert med samlet metrikktabell, månedlig metrikktabell, detaljert feilgrunnlag og markdown-oppsummering. `fullført 2026-04-07`
- [x] Dokumentasjon for WBS 5.3 (sammenligne modellresultater) er etablert med samlet sammenligningstabell, månedlige modellvinnere, vinnertelling og markdown-oppsummering med `tuned RF` som samlet anbefalt modell. `fullført 2026-04-07`
- [x] Dokumentasjon for WBS 5.4 (analysere viktige variabler) er etablert med tuned-RF feature importance, toppsignaler per modell, RF-stabilitetstabell, prioritert variabeloversikt og markdown-oppsummering. `fullført 2026-04-07`
- [x] Dokumentasjon for WBS 6.1 (tolke modellresultater) er etablert med månedlig bias per modell, segmentdefinisjoner, segmenterte metrikktabeller, segmentvinnere og markdown-oppsummering som kobler mønstrene til WBS 5.4. `fullført 2026-04-07`
- [x] Dokumentasjon for WBS 6.2 (diskutere styrker og svakheter) er etablert med modellprofiler, sporbare diskusjonspunkter, metodebegrensninger og markdown-oppsummering som skiller mellom pålitelighet og generaliserbarhet. `fullført 2026-04-07`
- [x] Dokumentasjon for WBS 6.3 (vurdere praktisk nytte) er etablert med beslutningsmatrise, bruksregler og markdown-oppsummering som oversetter modellfunnene til beslutningsstøtte for Dagligvare. `fullført 2026-04-12`
- [x] Planendringen for WBS 4.3 er dokumentert i egen endringslogg med begrunnelse og konsekvens for videre arbeid. `fullført 2026-04-02`
- [x] Avgrensningen av WBS 4.4 til tuning av Random Forest er dokumentert i egen endringslogg med begrunnelse og konsekvens for videre arbeid. `fullført 2026-04-02`
- [x] Fullføre sporbar modelltesting og modellsammenligning gjennom WBS 5.2 og WBS 5.3. `fullført 2026-04-07`
- [x] Bruke renset datasett som grunnlag for datasplitt og videre feature engineering. `fullført 2026-03-26`
- [x] Starte løpende rapportskriving parallelt med analysearbeidet, i tråd med arbeidsreglene i prosjektet. `påbegynt 2026-03-30, utvidet 2026-04-02 med modellnotater for WBS 4.1, 4.2, 4.3, 4.4 og 5.1, utvidet 2026-04-07 med korte notater for WBS 5.2, 5.3, 5.4, 6.1 og 6.2, utvidet 2026-04-12 med praktisk nytte i WBS 6.3 og en kort konklusjonssetning, utvidet 2026-04-16 med reorganisert diskusjon (9.1–9.5), utvidet konklusjon, Sammendrag og Abstract for WBS 7.1.6, ferdigstilt 2026-04-16 med kalibrert innledning og ny §1.2 Delproblemer for WBS 7.1.7, og utvidet 2026-04-19 med låst figur-/tabellutvalg for WBS 7.2.1`
- [ ] Oppdatere denne statuslisten etter ukentlige statusmøter og ved milepæler.

## Operativ oppdeling av rapportarbeid (WBS 7.x)

- [x] WBS 7.1.1: Skrive grunninnledning, problemstilling, avgrensinger og antagelser. Denne aktiviteten skal bare etablere en enkel og funksjonell start på rapporten, ikke ferdigstille innledningen. `fullført 2026-04-13`
- [x] WBS 7.1.2: Skrive litteratur og teori. `fullført 2026-04-13`
- [x] WBS 7.1.3: Skrive casebeskrivelse. `fullført 2026-04-13`
- [x] WBS 7.1.4: Skrive metode og data. `fullført 2026-04-13`
- [x] WBS 7.1.5: Skrive modellering, analyse og resultat. `fullført 2026-04-16`
- [x] WBS 7.1.6: Skrive diskusjon, konklusjon, sammendrag, abstract og bibliografi. `fullført 2026-04-16`
- [x] WBS 7.1.7: Ferdigstille innledning etter at øvrig rapportskriving i WBS 7.1 er gjort, slik at innledningen samsvarer med resten av rapporten. `fullført 2026-04-16`
- [x] WBS 7.2.1: Velge hvilke figurer og tabeller som faktisk skal inn i rapporten. Utvalget er dokumentert i [rapport_fig_tab_utvalg.md](rapport_fig_tab_utvalg.md) med 12 figurer, 16 innholdstabeller (15 i kap. 5–9 + Tabell 12.1 i kap. 12) og 7 vedleggsreferanser, og knytter hver artefakt til kilde i `006 analysis/`. `fullført 2026-04-19`
- [x] WBS 7.2.2: Lage case- og datakapitlets figurer og tabeller. Leveransen er dokumentert i [rapport_7_2_2_artefakter.md](rapport_7_2_2_artefakter.md) med Figur 5.1, Figur 5.2 og Tabell 5.2–5.4 klare til innsetting. `fullført 2026-04-19`
- [x] WBS 7.2.3: Lage analyse-, resultat- og diskusjonsfigurer og tabeller. Leveransen er dokumentert i [rapport_7_2_3_artefakter.md](rapport_7_2_3_artefakter.md) med fem nye PNG-er (Figur 7.1, 7.2, 8.1, 8.2, 8.3) og syv nye Markdown-tabeller (Tabell 6.1, 6.2, 7.1, 7.2, 9.1, 9.2, 9.3). `fullført 2026-04-19`
- [x] WBS 7.2.4: Sette inn, nummerere og formatere figurer og tabeller i rapporten. Alle figurer og tabeller er plassert i riktig kapittel i [rapport.md](../005%20report/rapport.md), og renummerering etter helhetsreviewen (Tabell 5.1 → 5.5, Tabell 9.2 ↔ 9.3) sikrer at formkrav 1 oppfylles. `fullført 2026-04-19`
- [ ] WBS 7.3.1: Gjennomføre struktur- og kravsjekk av rapportutkastet.
  - F1 fra helhetsreview av 7.2 er adressert 2026-04-21: henvisningen i kap. 7 linje 459 er endret fra «(jf. Tabell 8.2)» til «(jf. Tabell 7.1)» og linje 496 fra «(jf. Tabell 8.4)» til «(jf. Tabell 7.2)». Henvisningene til Tabell 8.1 (linje 457) og Tabell 8.3 (linje 519) beholdes, siden disse peker på aggregert ytelse og feature importance som ikke har lokale motparter i kap. 7.
- [ ] WBS 7.3.2: Gjennomføre konsistenssjekk mot analyseartefakter.
- [ ] WBS 7.3.3: Gjennomføre språkvask, rette henvisninger og låse førsteutkastet.

## Anbefalt kort prosjektstatus

Prosjektet fremstår per 2026-04-21 som værende ferdig med all analyse (WBS 2.x–6.x), hele rapportskrivingen i WBS 7.1 og hele figur-/tabellblokken WBS 7.2 (7.2.1 utvalg, 7.2.2 case/data, 7.2.3 analyse/resultat/diskusjon og 7.2.4 innsetting). [rapport.md](../005%20report/rapport.md) inneholder nå 10 nummererte innholdsfigurer (Figur 4.1–4.3, 5.1–5.2, 7.1–7.2, 8.1–8.3), 16 innholdstabeller (Tabell 5.2–5.5, 6.1–6.2, 7.1–7.2, 8.1–8.4, 9.1–9.3, 12.1) og vedleggsreferanser A1–A7. WBS 7.1.1–7.1.7 er fullført: Sammendrag (277 ord), Abstract (298 ord), ferdigstilt innledning med problemstilling og §1.2 Delproblemer, litteratur, teori (3.1–3.4), casebeskrivelse (4.1–4.4), kapittel 5 Metode og data (5.1 Metode og 5.2 Data med Tabell 5.2–5.5), kapittel 6 Modellering med Tabell 6.1–6.2, kapittel 7 Analyse med Tabell 7.1–7.2 og Figur 7.1–7.2, kapittel 8 Resultat med Tabell 8.1–8.4 og Figur 8.1–8.3, kapittel 9 Diskusjon (9.1–9.5) med Tabell 9.1–9.3, kapittel 10 Konklusjon, kapittel 11 Bibliografi og kapittel 12 Vedlegg med Tabell 12.1. Etter helhetsreviewen av 7.2 er Tabell 5.1 renummerert til 5.5 og Tabell 9.2/9.3 byttet slik at nummereringen matcher tekstrekkefølgen (formkrav 1). Som en tidlig del av 7.3.1 er F1 fra helhetsreviewen lukket 2026-04-21: henvisningene i kap. 7 linje 459 og 496 er endret til lokale Tabell 7.1 og Tabell 7.2, mens linje 457 (Tabell 8.1) og linje 519 (Tabell 8.3) beholdes fordi disse peker på aggregert ytelse og feature importance uten lokal motpart. Gjenstående steg er resten av WBS 7.3.1 struktur- og kravsjekk, 7.3.2 konsistenssjekk og 7.3.3 språkvask og låsing av førsteutkastet.
