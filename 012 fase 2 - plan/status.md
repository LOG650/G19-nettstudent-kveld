# Statusliste

Oppdatert: 2026-06-08 (WBS 8.1 påbegynt – veiledertilbakemelding på rapporten innarbeidet i ny revisjon `rapport_final.md`)

Denne statuslisten er generert med utgangspunkt i [prosjektstyringsplan.md](/home/erikb/himolde/log650/G19-nettstudent-kveld/012 fase 2 - plan/prosjektstyringsplan.md) og tilgjengelige prosjektartefakter i repoet. Punkter er merket som `verifisert` når de kan knyttes til eksisterende filer eller mappestruktur. Øvrige punkter er vurdert som planstatus per dato og må bekreftes av prosjektgruppen. Omtolkningen av WBS 4.3 er dokumentert i [endringslogg.md](endringslogg.md).

## Overordnet status

- [x] Prosjektstyringsplan er etablert og datert 2026-03-10. `verifisert`
- [x] Prosjektforslag finnes i fase 1. `verifisert`
- [x] Datasett er tilgjengelig i prosjektmappen. `verifisert`
- [x] Analysearbeid i egen `006 analysis`-mappe er etablert med felles Python/uv-oppsett. `verifisert`
- [x] Statusgrunnlaget for modellutvikling, prognoseleveranse, evalueringsmetrikker, modellsammenligning, analyse av viktige variabler, tolkning av modellresultatene, diskusjon av styrker og svakheter og praktisk nytte er nå dokumentert gjennom feature engineering, datasplitt, eksplorativ analyse, lineær regresjon i WBS 4.1, Random Forest i WBS 4.2, et lett felles verifiseringssteg i WBS 4.3, parameterjustering av Random Forest i WBS 4.4, genererte 2025-prognoser i WBS 5.1, beregnede 2025-`RMSE`/`MAPE` i WBS 5.2, sammenligning av modellresultatene i WBS 5.3, variabelanalyse i WBS 5.4, tolkning i WBS 6.1, diskusjon i WBS 6.2 og praktisk nytte i WBS 6.3. Rapportarbeidet er per 2026-04-24 også helhetlig fullført i WBS 7.1–7.3, og førsteutkastet er låst. `verifisert`

## Status per hovedaktivitet

- [x] A: Problemdefinisjon og prosjektplan er gjennomført eller langt på vei ferdigstilt, siden prosjektforslag og prosjektstyringsplan foreligger. `verifisert delvis gjennom artefakter`
- [x] B: Datainnsamling og dokumentasjon ser ut til å være påbegynt eller gjennomført, siden datasettet finnes i prosjektet. `verifisert delvis gjennom artefakter`
- [x] C: Dataforståelse, variabelanalyse og datasettdokumentasjon er dokumentert for WBS 2.2-2.4 i analyseområdet. `verifisert`
- [x] D: Datapreprosessering og eksplorativ analyse er dokumentert for WBS 3.1-3.4 i analyseområdet. `verifisert`
- [x] E: Feature engineering er dokumentert i analyseområdet med eget feature-datasett og dokumenterte featurevalg. `verifisert`
- [x] F: Modellbygging er dokumentert med lineær regresjon i WBS 4.1, Random Forest i WBS 4.2, et felles verifiserings- og oppsummeringssteg i WBS 4.3 og parameterjustering av Random Forest i WBS 4.4. Lineær regresjon står fortsatt som fast benchmark, mens tuned Random Forest er etablert som videre operativ modell. Selve planendringene for 4.3 og 4.4 er dokumentert i `endringslogg.md`. `verifisert`
- [x] G: Prognoser for 2025, `RMSE`/`MAPE`, modellsammenligning, analyse av viktige variabler, tolkning av modellmønstre, diskusjon av styrker og svakheter og praktisk nytte er nå dokumentert i WBS 5.1, 5.2, 5.3, 5.4, 6.1, 6.2 og 6.3 for lineær regresjon, Random Forest-baseline og tuned Random Forest. `tuned RF` fremstår samlet som anbefalt modell på 2025-data, vinner `RMSE` i de fleste måneder og segmenter, og er nå oversatt til praktisk beslutningsstøtte for innkjøp, lager, kampanjevurdering, ressursplanlegging og ledelsesrapportering. `verifisert`
- [x] H: Rapportskriving er helhetlig fullført: WBS 7.1.1–7.1.7, hele WBS 7.2-blokken (7.2.1 utvalg, 7.2.2 case/data, 7.2.3 analyse/resultat/diskusjon og 7.2.4 innsetting) og hele WBS 7.3-blokken (7.3.1 struktur- og kravsjekk, 7.3.2 konsistenssjekk og 7.3.3 språkvask og låsing) er dokumentert og lukket. Rapporten inneholder Sammendrag, Abstract, ferdigstilt innledning (inkl. §1.2 Delproblemer), problemstilling, avgrensinger, antagelser, litteratur, teori, casebeskrivelse, metode og data (Tabell 5.1–5.4 og Figur 5.1–5.2), modellering (Tabell 6.1–6.2), analyse (Tabell 7.1–7.2, Figur 7.1–7.2), resultat (Tabell 8.1–8.4, Figur 8.1–8.3), diskusjon (9.1–9.5 med Tabell 9.1–9.3), konklusjon, bibliografi og vedlegg (Tabell 12.1). Førsteutkastet er låst per 2026-04-24. `verifisert`
- [ ] I: Konklusjon og presentasjon er ikke startet som egen avslutningsfase, selv om rapporten nå har en ferdigskrevet konklusjon i WBS 7.1.6. `delvis verifisert`

## Milepælstatus mot plan

- [x] M1: Prosjektforslag godkjent, planlagt i februar. Prosjektforslag finnes i repoet. `verifisert delvis gjennom artefakt`
- [x] M2: Datagrunnlag klargjort, planlagt 10. mars. Datasett finnes, men graden av klargjøring bør bekreftes. `delvis verifisert`
- [x] M3: Testing av modellene, planlagt 23. mars. Prognoser for 2025, evalueringsmetrikker (`RMSE`/`MAPE`) og formell modellsammenligning er dokumentert per 2026-04-07. `verifisert forsinket`
- [x] M4: Modelloptimalisering ferdig, planlagt 22. april. WBS 4.4 dokumenterer parameterjustering av Random Forest med 2024 som intern validering. `verifisert 2026-04-02`
- [x] M5: Hovedutkast av rapport, planlagt 8. april. Førsteutkastet av rapporten er låst 2026-04-24 etter at WBS 7.3.3 språkvask ble lukket. M5 regnes som nådd, men forsinket med 16 dager mot opprinnelig plandato. Eksplisitt forsinkelsesnotat mot KR-007 er overført til WBS 8.1. `verifisert forsinket`
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
- [x] WBS 7.3.1: Gjennomføre struktur- og kravsjekk av rapportutkastet. `fullført 2026-04-21`
  - Reviewen er dokumentert i [reviews/7_3_1_struktur_og_kravsjekk-CLAUDE.md](reviews/7_3_1_struktur_og_kravsjekk-CLAUDE.md) og bekrefter at rapporten følger CLAUDE.md § Rapportstruktur og § Rapportsjekkliste og at alle baselinekrav KR-001 til KR-006 er dekket.
  - F1 fra helhetsreview av 7.2 ble lukket som første delsteg: kap. 7 linje 459 endret fra «(jf. Tabell 8.2)» til «(jf. Tabell 7.1)» og linje 496 fra «(jf. Tabell 8.4)» til «(jf. Tabell 7.2)». Henvisningene til Tabell 8.1 og Tabell 8.3 beholdt siden disse peker på aggregert ytelse og feature importance uten lokal motpart.
  - V1 (Høy) lukket: Tittelsiden i [rapport.md](../005%20report/rapport.md) linje 1–93 er fylt ut med tittel, forfattere, studiepoeng (15), veileder (BIP), egenerklæringer, personvern og helseforskningsloven (ikke omfattet), publisering (Ja) og båndlegging (Nei). Innleveringsdato, sidetall og dato står som tydelige TODO-markører og fylles ut nærmere innlevering.
  - V2 (Middels) lukket: Tabell 5.x renummerert 5.2→5.1, 5.3→5.2, 5.4→5.3, 5.5→5.4 i rapport.md. Sporbarhet i [rapport_fig_tab_utvalg.md](rapport_fig_tab_utvalg.md) og [rapport_7_2_2_artefakter.md](rapport_7_2_2_artefakter.md) oppdatert tilsvarende.
  - V3 (Middels) lukket: TOC utvidet med §§ 3.1–3.4.
  - V4 (Middels) lukket: §§ 1.1–1.4 endret fra `##` (H2) til `###` (H3).
  - Gjenstående åpne punkter (overført til senere aktiviteter): F1 (liten «f» i «figur 4.3» linje 306) og F2 (manglende introduksjonssetning for Tabell 12.1) til WBS 7.3.3 språkvask. F3 (ikke-fagfellevurderte kilder) og KR-007-forsinkelsesnotat til WBS 8.1. Antall ord beregnet til ca. 5 300 for hovedtekst kap. 1–10.
- [x] WBS 7.3.2: Gjennomføre konsistenssjekk mot analyseartefakter. `fullført 2026-04-21`
  - Reviewen er dokumentert i [reviews/7_3_2_konsistenssjekk-CLAUDE.md](reviews/7_3_2_konsistenssjekk-CLAUDE.md) og bekrefter at alle ni ankerpåstander i Sammendrag og Abstract (RMSE 578,26, MAPE 43,97 %, 11/12 måneder, 13/14 segmenter, 67 features, 9 994 transaksjoner, 6 682 trening, 3 312 test, rabatt 11,48 %, ~42 % kalender) stemmer eksakt med kilde-CSV.
  - Alle 16 innholdstabeller (5.1–12.1) og 10 figurer (4.1–8.3) er verifisert mot artefaktkildene innenfor ±0,005-toleranse. Vedleggsreferansene A1–A7 peker til eksisterende CSV-filer, og A1-radantallet «3 312 rader» stemmer.
  - Ingen svakheter (V) ble funnet. Tre lave forbedringsforslag overføres til WBS 7.3.3 språkvask: F1 (tvetydig formulering om 42 % kalenderandel i Sammendrag og Abstract), F2 (Tabell 5.1 anbefaling `inkluder` for `State` motsier brødtekst og Tabell 5.2 som ekskluderer den konstante kolonnen), F3 (tvetydig MAPE-referanse 89,39 % i § 7 linje 502).
- [x] WBS 7.3.3: Gjennomføre språkvask, rette henvisninger og låse førsteutkastet. `fullført 2026-04-24`
  - Reviewen er dokumentert i [reviews/7_3_3_sprakvask-CLAUDE.md](reviews/7_3_3_sprakvask-CLAUDE.md) og bekrefter at alle fem overførte F-punkter er lukket med seks målrettede tekstendringer i [rapport.md](../005%20report/rapport.md).
  - F1 fra 7.3.1 lukket: linje 312 endret «figur 4.3» → «Figur 4.3».
  - F2 fra 7.3.1 lukket: ny introsetning `Tabell 12.1 lister vedleggene A1–A7 med innhold og tilhørende kildefil under \`006 analysis/\`.` innsatt før Tabell 12.1.
  - F1 fra 7.3.2 lukket: Sammendrag (linje 105) og Abstract (linje 113) omformulert slik at «om lag 42 %» entydig gjelder kalendervariablene alene.
  - F2 fra 7.3.2 lukket: Tabell 5.1 `State`-rad endret fra `inkluder / Kategorisk variabel med håndterbar kardinalitet.` til `ekskluder / Kolonnen er konstant i datasettet og gir ingen forklaringskraft.`, i samsvar med Tabell 5.2 og brødtekst § 5.2.
  - F3 fra 7.3.2 lukket: § 7 linje 502 korrigert fra «MAPE der ligger på 89,39 %» til «tuned Random Forest-MAPE i samme segment ligger på 90,27 %». 89,39 % var faktisk baseline RFs MAPE; 90,27 % er tuned RFs verdi verifisert mot [tab_segmentmetrikk_modell.csv](../006%20analysis/aktiviteter/16_tolke_modellresultater/tab_segmentmetrikk_modell.csv).
  - Overført til WBS 8.1: synkronisering av [tab_relevante_variabler.csv](../006%20analysis/aktiviteter/02_identifisere_relevante_variabler/tab_relevante_variabler.csv) slik at `State = ekskluder` (analyseartefakt-opprydding, ikke språkvask).
  - Førsteutkastet av rapporten er låst per 2026-04-24. Videre revisjon håndteres i WBS 8.1.

## WBS 8.1 – Revisjon etter veiledertilbakemelding

- [x] Veiledertilbakemelding på `014 fase 4 - report/rapport_post_review.md` innarbeidet i ny revisjon [rapport_final.md](../014%20fase%204%20-%20report/rapport_final.md). Kildefilen `rapport_post_review.md` er bevart uendret. `fullført 2026-06-08`
  - Kapittel 7 og 8 byttet plass: ny rekkefølge er `7 Resultat` og `8 Analyse`. Alle tabeller/figurer er renummerert (Tabell 7.1–7.4, Figur 7.1–7.3 i resultatkapitlet; Tabell 8.1–8.2, Figur 8.1–8.2 i analysekapitlet) og alle kryssreferanser, innholdsfortegnelse og CLAUDE.md-strukturlisten er oppdatert.
  - All omtale av caset/datasettet som «simulert» er fjernet fullstendig (16 norske + 2 engelske forekomster, inkl. tittel, sammendrag, abstract, etikkavsnitt og konklusjon). `grep -i simuler` = 0 treff.
  - Tabell 9.3 (metodiske begrensninger) er gjort om til løpende tekst i § 9.5.
  - De brede tabellene er konvertert til HTML med mindre font (`font-size:0.8em`); Tabell 8.1, 8.2 og 9.1 har i tillegg hierarkiske kolonneoverskrifter (modell → RMSE/MAPE).
  - Kapittel 3 (Teori) er styrket med konsekvenser av forutsetningsbrudd (3.1), bias–varians-avveiing og out-of-bag-validering (3.2) og skalerte feilmål (3.3).
  - Litteratur (kap. 2) og bibliografi (kap. 11) er utvidet med fire verifiserte fagfellevurderte kilder fra Google Scholar/CrossRef: Fildes et al. (2022), Makridakis et al. (2022), Mitra et al. (2022) og Ulrich et al. (2021). Dette lukker WBS 8.1-punkt (c) om fagfellevurderte supplerende kilder.
  - Figur 4.1 beholdt i § 4.1 etter avklaring (veileders «flytte figur 4.1?» besvart med nei).
- [ ] Gjenstående WBS 8.1-punkter: (a) synkronisering av `tab_relevante_variabler.csv` (`State = ekskluder`) og (b) eksplisitt dokumentasjon av M5-forsinkelsen mot KR-007.

## Anbefalt kort prosjektstatus

Prosjektet fremstår per 2026-04-24 som værende ferdig med all analyse (WBS 2.x–6.x), hele rapportskrivingen i WBS 7.1, hele figur-/tabellblokken WBS 7.2 og hele kvalitetssikringsblokken WBS 7.3 (7.3.1 struktur- og kravsjekk, 7.3.2 konsistenssjekk mot analyseartefakter og nå 7.3.3 språkvask). [rapport.md](../005%20report/rapport.md) inneholder 10 nummererte innholdsfigurer (Figur 4.1–4.3, 5.1–5.2, 7.1–7.2, 8.1–8.3) og 16 innholdstabeller (Tabell 5.1–5.4, 6.1–6.2, 7.1–7.2, 8.1–8.4, 9.1–9.3, 12.1) og vedleggsreferanser A1–A7. Språkvasken i 7.3.3 har lukket alle fem overførte F-punkter med seks målrettede tekstendringer, inkludert én faktuell korreksjon der tuned RFs MAPE i segmentet «lavt salg» er satt til 90,27 % (tidligere feilattribuert baseline RFs 89,39 %). Førsteutkastet av rapporten er dermed låst. Overført til WBS 8.1 revisjon: (a) synkronisering av [tab_relevante_variabler.csv](../006%20analysis/aktiviteter/02_identifisere_relevante_variabler/tab_relevante_variabler.csv) slik at `State = ekskluder` for full sporbarhet; (b) eksplisitt dokumentasjon av M5-forsinkelsen; (c) vurdering av fagfellevurderte supplerende kilder. Neste milepæl er M6 2026-05-19 (endelig rapport levert).
