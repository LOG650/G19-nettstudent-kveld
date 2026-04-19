# Endringslogg

## 2026-04-19 - WBS 7.2.1 valgte maksimalt figur-/tabellutvalg

- Hva ble endret: Utvalget i `rapport_fig_tab_utvalg.md` omfatter 12 figurer (5 beholdt inkl. 2 forsidebilder, 2 kopieres inn fra eksisterende analyse-PNG, 5 nye plott) og 15 innholdstabeller (5 beholdt fra dagens rapport, 10 nye som produseres i 7.2.2 og 7.2.3), samt 7 vedleggsreferanser (A1–A7) til stort datamateriale. Etter reviewen er figurene i kap. 8 omnummerert slik at tekstrekkefølgen matcher nummereringen (Figur 8.1 = samlet RMSE/MAPE, Figur 8.2 = feature importance topp 10, Figur 8.3 = variabelgrupper), og salgsfordelingen mellom trening og test er flyttet fra kap. 4 (tidligere Figur 4.4) til kap. 5.2 som Figur 5.2.
- Hvorfor: Analysen har produsert 4 figurer og 57 CSV-tabeller i 18 aktivitetsmapper, mens rapporten per 7.1.7 bare inneholdt 5 figurer og 4 innholdstabeller. Prosjektgruppen valgte maksimalt utvalg for å utnytte analysegrunnlaget, styrke rapportens akademiske verdi og oppfylle lærerens anbefaling om en god andel egenproduserte figurer. Omnummereringen og flyttingen ble gjort for å oppfylle lærerens formkrav om at «figurer og tabeller nummereres separat og i den rekkefølgen de omtales» og for å plassere salgsfordelingsfiguren i det kapitlet som faglig hører hjemme.
- Konsekvens for videre arbeid: WBS 7.2.2 får to kopieringsoppdrag (`fig_datatype_fordeling.png` som Figur 5.1 og `fig_sales_fordeling_train_test.png` som Figur 5.2) og tre nye tabellutdrag i kap. 5 (5.2, 5.3, 5.4). WBS 7.2.3 får fem nye plotteblokker fordelt på `start_wbs_5_2.py` i aktivitet 13 (Figur 7.2 og 8.1), `start_wbs_5_4.py` i aktivitet 15 (Figur 8.2 og 8.3) og `start_wbs_6_1.py` i aktivitet 16 (Figur 7.1), samt sju nye tabellutdrag i kap. 6, 7 og 9. Gantt-vinduet for 7.2-blokken (2026-04-15 til 2026-04-20) må forskyves når 7.2.4 er lukket, siden omfanget er større enn det Gantt forutsatte. `Prosjekt Gantt v2.mpp` og bildene i `images/` regenereres ikke i denne endringen.
- Hvem/beslutningsgrunnlag: Endringen ble gjort i arbeidsøkten 2026-04-19 etter at 7.2.1 ble lukket og reviewen identifiserte behovet for tidlig endringslogg-oppføring (F2), samt tre svakheter (V1 rekkefølgebrudd i kap. 8, V2 feil plassering av salgsfordelingsfigur, V3 uspesifisert plassering for Tabell 7.2) og tre forbedringsforslag (F1 URL-koding av lenker, F3 sorteringskriterium i Tabell 6.2, og F2 selv) som alle ble rettet samme dag.

## 2026-04-13 - Selskapsnavn rettet fra «PowerHorse» til «Dagligvare»

- Hva ble endret: Navnet «PowerHorse» er erstattet med «Dagligvare» i `rapport.md` (kap. 4.1 overskrift, brødtekst og kap. 4.4), og AGENTS.md linje 36 (`4.1 PowerHorse og beslutningssituasjonen`) er identifisert som en mal-rest som ikke reflekterer prosjektets faktiske case.
- Hvorfor: Caset i dette prosjektet gjelder en simulert dagligvarekjede kalt «Dagligvare», ikke «PowerHorse». «PowerHorse» stammer fra rapportmalen i AGENTS.md og ble ved en feil brukt som selskapsnavn da casebeskrivelsen ble skrevet i WBS 7.1.3.
- Konsekvens for videre arbeid: Bruk alltid «Dagligvare» som selskapsnavn i rapport, planfiler og analyse. Seksjonsoverskriften «4.1 PowerHorse og beslutningssituasjonen» i AGENTS.md er en mal-plassholder og skal leses som «4.1 Dagligvare og beslutningssituasjonen» i det faktiske prosjektet.
- Hvem/beslutningsgrunnlag: Rettet i arbeidsøkten 2026-04-13 etter at feilen ble oppdaget under gjennomgang av rapport.md.

## 2026-04-12 - WBS 7.x delt opp i operative rapportunderaktiviteter

- Hva ble endret: Rapportfasen er delt opp fra grove aktivitetspakker til operative underaktiviteter i `7.1.1-7.3.3`. Endringen er synket i `Prosjekt Gantt v2.csv`, `wbs.json`, `project_model.json`, WBS-vedlegget i `prosjektstyringsplan.md` og `status.md`.
- Hvorfor: Den opprinnelige oppdelingen i `7.1-7.3` var for grov til å gi god styring og sporbarhet mot faktisk arbeid i `rapport.md`. En finere oppdeling gjør det lettere å følge progresjon, fordele arbeid og oppdatere status uten å late som om store deler av rapporten er ferdige.
- Innledningsstrategi: Innledningen er nå bevisst delt i to steg. `7.1.1` brukes til å skrive en grunninnledning med problemretning, problemstilling, avgrensinger og antagelser, mens `7.1.7` brukes til å ferdigstille innledningen etter at øvrig rapportskriving i `7.1` er gjort.
- Konsekvens for videre arbeid: `8.1-8.4` har fått forskjøvede `task_id` til `36-39`, `project_model.json` er oppdatert til nivå-3-WBS og aktivitetstelling `39`, og `status.md` har fått åpne sjekkpunkter for hele den nye rapportstrukturen.
- Avgrensning i denne endringen: `Prosjekt Gantt v2.mpp`, `images/LOG650_Gantt.png` og andre eksporterte planbilder er ikke oppdatert i samme steg, og må eventuelt regenereres manuelt senere.
- Hvem/beslutningsgrunnlag: Endringen ble gjort i arbeidsøkten 2026-04-12 etter vurdering av at rapportarbeidet i praksis følger flere mindre skrive- og kvalitetssikringssteg enn det den opprinnelige 7.x-strukturen fanget opp.

## 2026-04-02 - WBS 4.4 avgrenset til tuning av Random Forest

- Hva ble endret: Aktiviteten `4.4 Justere modellparametere` er gjennomført som parameterjustering av `RandomForestRegressor`, mens lineær regresjon beholdes som uendret benchmark-modell.
- Hvorfor: Lineær regresjon er allerede dokumentert som fast referansemodell, og videre tuning der ville i praksis utvidet modellomfanget mot regulariserte varianter som ikke ligger i prosjektets eksplisitte WBS. Random Forest har samtidig størst realistisk tuningrom innenfor dagens prosjektplan.
- Konsekvens for videre arbeid: Den tunede Random Forest-modellen blir standardmodell for Random Forest-sporet i WBS 5.1, mens baseline-modellen fra WBS 4.2 beholdes som dokumentert sammenligningspunkt. 2025-data er fortsatt urørt og forbeholdt prognoser og evaluering i WBS 5.x.
- Hvem/beslutningsgrunnlag: Endringen ble gjort i arbeidsøkten 2026-04-02 etter gjennomgang av WBS 4.1-4.3, datasplitten i `06_datasplitt` og prosjektets krav om to modeller, evalueringsmål og etterprøvbar dokumentasjon.

## 2026-04-02 - WBS 4.3 omtolket til lett verifiseringssteg

- Hva ble endret: Aktiviteten `4.3 Trene modellene` er gjennomført i repoet som felles verifisering og treningsoppsummering, ikke som en ny full treningsrunde for begge modeller.
- Hvorfor: Selve modelltreningen er allerede dokumentert og utført i WBS 4.1 for lineær regresjon og i WBS 4.2 for Random Forest Regressor. En ny trening i 4.3 ville derfor vært redundant og gitt lite ny sporbar verdi.
- Konsekvens for videre arbeid: WBS 4.3 leverer felles kontroll av treningsgrunnlaget og en samlet oversikt over modellsignaler, mens parameterjustering fortsatt ligger i WBS 4.4 og evaluering ligger i WBS 5.x og WBS 6.1.
- Hvem/beslutningsgrunnlag: Endringen ble gjort i arbeidsøkten 2026-04-02 etter gjennomgang av eksisterende artefakter i `08_lineaer_regresjon` og `09_random_forest_regressor`, samt avklaring om at 4.3 skulle være et lett steg.
