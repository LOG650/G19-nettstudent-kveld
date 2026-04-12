# Endringslogg

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
