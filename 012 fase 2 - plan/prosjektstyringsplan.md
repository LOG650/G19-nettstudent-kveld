# Prosjektstyringsplan

## for Daglivare  

2026-03-10

**Utarbeidet av:**  
Erik Brendehaug  
Joseph James  
Pål Rånes  
Marthe Slåtta Bjerke

**Autorisert av:**  
Bård Inge Peterson (BIP)

## Innhold

- [Prosjektstyringsplan](#prosjektstyringsplan)
  - [for Daglivare](#for-daglivare)
  - [Innhold](#innhold)
  - [Sammendrag](#sammendrag)
    - [Behov](#behov)
  - [Omfang](#omfang)
    - [Mål](#mål)
    - [Krav](#krav)
    - [Løsning](#løsning)
    - [Arbeidsnedbrytningsstruktur](#arbeidsnedbrytningsstruktur)
    - [Omfangsverifikasjon](#omfangsverifikasjon)
  - [Fremdrift](#fremdrift)
    - [Avhengighetsdiagram (AOA)](#avhengighetsdiagram-aoa)
    - [Gantt-plan](#gantt-plan)
    - [Kritisk linje](#kritisk-linje)
    - [Milepæler](#milepæler)
  - [Risiko](#risiko)
    - [Prosess for risikostyring](#prosess-for-risikostyring)
    - [Risikoregister](#risikoregister)
  - [Interessenter](#interessenter)
  - [Ressurser](#ressurser)
    - [Prosjektteam](#prosjektteam)
  - [Kommunikasjon](#kommunikasjon)
  - [Kvalitet](#kvalitet)
    - [Fagfellevurderinger](#fagfellevurderinger)
      - [Uformelle fagfellevurderinger](#uformelle-fagfellevurderinger)
      - [Formelle fagfellevurderinger](#formelle-fagfellevurderinger)
  - [Anskaffelser](#anskaffelser)
    - [Oversikt over anskaffelser](#oversikt-over-anskaffelser)
      - [Datasett](#datasett)
      - [Programvare for dataanalyse](#programvare-for-dataanalyse)
      - [Utviklingsmiljø](#utviklingsmiljø)
      - [Kunstig intelligens-verktøy](#kunstig-intelligens-verktøy)
      - [Versjonskontroll og samarbeid](#versjonskontroll-og-samarbeid)
      - [Dokumentasjon og rapportskriving](#dokumentasjon-og-rapportskriving)
      - [Anskaffelsesstrategi](#anskaffelsesstrategi)
      - [Leverandører og teknologiplattformer](#leverandører-og-teknologiplattformer)
      - [Risiko knyttet til anskaffelser](#risiko-knyttet-til-anskaffelser)
  - [Endringskontrollprosess](#endringskontrollprosess)
    - [Prosess for håndtering av endringer](#prosess-for-håndtering-av-endringer)
    - [Formål med endringskontroll](#formål-med-endringskontroll)
  - [Vedlegg](#vedlegg)
    - [Vedlegg A – Krav](#vedlegg-a--krav)
    - [Vedlegg B – WBS og PlantUML-kode](#vedlegg-b--wbs-og-plantuml-kode)
      - [Løsning plantUML-kode](#løsning-plantuml-kode)
      - [WBS-illustrasjon](#wbs-illustrasjon)
      - [WBS-PlantUML-kode](#wbs-plantuml-kode)
    - [Vedlegg C – Format for prosjektets saksliste](#vedlegg-c--format-for-prosjektets-saksliste)

## Sammendrag

Dette dokumentet utgjør prosjektstyringsplanen for Daglivare-prosjektet. Det dokumenterer planbaselines for omfang, fremdrift, budsjett og risiko, og gir tilleggsinformasjon for å støtte prosjektleder og team i vellykket gjennomføring.

Dette er et levende dokument, og skal oppdateres av prosjektleder ved behov gjennom prosjektets løpetid.

### Behov

Dette prosjektet svarer på behovet for mer presise etterspørselsprognoser i dagligvarehandel, slik at virksomheten kan ta bedre beslutninger knyttet til innkjøp, kampanjer og ressursplanlegging. Mer treffsikre prognoser kan bidra til redusert svinn, færre utsolgte varer og mer effektiv drift.  

## Omfang

Denne seksjonen beskriver prosjektomfanget for Daglivare, inkludert prosjektmål, forutsetninger, begrensninger, krav og arbeidsnedbrytningsstruktur som definerer alle leveranser som skal produseres i prosjektgjennomføring og avslutning. Den beskriver også prosessen som skal brukes for omfangsverifikasjon.

All planlegging av prosjektets fremdriftsplan, budsjett og risiko som beskrives i resten av dette dokumentet, er basert på denne omfangsdefinisjonen.

Aktuell status for omfangsfremdrift skal rapporteres hver måned til sponsor, kunde og andre relevante interessenter i den månedlige prosjektgjennomgangen beskrevet i seksjon 9 – Kommunikasjon.

Endringer i prosjektomfanget etter at denne planen er godkjent og etablert som baseline må gjennom den formelle endringskontrollprosessen beskrevet i seksjon 12 – Endringskontrollprosess.

### Mål

Prosjektmålet er å utvikle og evaluere prediksjonsmodeller (multippel lineær regresjon og Random Forest Regressor) for å forutsi salg i 2025 for en simulert dagligvarekjede, samt identifisere hvilke faktorer som påvirker salget mest.

Prosjektets forutsetninger er:

- Det benyttes et eksisterende datasett fra Kaggle som representerer historiske salgsdata for en dagligvarebutikk.  
- Datasettet antas å være tilstrekkelig representativt for å simulere en virkelig dagligvarekjede.  
- Historiske data fra perioden 2022–2024 brukes som treningsgrunnlag, og 2025 brukes som testperiode.  
- Det forutsettes at sentrale forklaringsvariabler som sesong, rabatt, region og produktkategori er inkludert og har tilstrekkelig datakvalitet.  
- Det antas at etterspørselsmønstre fra tidligere år er relevante for å predikere fremtidig salg.

Prosjektets begrensninger er:

- Analysen fokuserer på prediksjon og ikke på kausal sammenheng mellom variabler.  
- Lageroptimalisering og operative beslutningsmodeller inngår ikke i prosjektet.  
- Eksterne makroøkonomiske faktorer (inflasjon, rente, konjunkturer osv.) inkluderes ikke i modellen.  
- Prosjektet er avgrenset til én simulert virksomhet og ett datasett.  
- Modellene som vurderes er begrenset til multippel lineær regresjon og Random Forest Regressor.

### Krav

Daglivare sine prosjektkrav gir den omfangsdetaljen som trengs for å realisere prosjektmålet. Kravene beskriver hva prosjektet må oppfylle for å nå målet, ikke hvordan det skal gjøres. «Hvordan» vil bli definert under prosjektgjennomføringen etter hvert som detaljerte krav og designleveranser utvikles.

Krav er identifisert innen områdene; funksjonalitet, kapasitet, informasjonssikkerhet og dokumentasjon.

En fullstendig kravliste finnes i vedlegg A, sammen med kravets eier og foreløpig kobling (traceability) til leveranser og testtilfeller. Dette vil bli raffinert etter hvert som design- og testplanleggingen utvikles under gjennomføringen.

Kravene ble innhentet og etablert som baseline av Daglivare sine forretningsanalytikere, basert på tidligere erfaring fra lignende prosjekter, omfattende intervjuer med kundens brukergrupper, og forskning på relevante standarder. Kravene har vært gjennom flere runder med gjennomgang for å sikre at de er komplette, konsistente og testbare, og er signert av de respektive eierne.

For dette prosjektet innebærer det blant annet at:

- Løsningen skal kunne generere salgsprognoser for 2025 basert på historiske data fra 2022–2024.  
- Det skal utvikles og evalueres minst to modeller (multippel lineær regresjon og Random Forest Regressor).  
- Modellenes ytelse skal måles og dokumenteres ved bruk av MAPE og RMSE.  
- Løsningen skal identifisere og rangere hvilke variabler som har størst påvirkning på salget.  
- Datagrunnlaget skal være strukturert, kvalitetssikret og dokumentert.  
- Resultater, metodevalg og modellforutsetninger skal dokumenteres slik at analysen kan etterprøves.  
- Prosjektet skal gjennomføres innenfor avtalte tids- og ressursrammer.

### Løsning

Løsningen som skal utvikles for å oppfylle prosjektmålet er en dataanalyse- og maskinlæringsbasert prognosemodell som kan forutsi dagligvaresalg for 2025 basert på historiske salgsdata. Løsningen vil bestå av en prosess for datainnsamling, datarensing og feature engineering, etterfulgt av utvikling og trening av to prediksjonsmodeller: multippel lineær regresjon og Random Forest Regressor. Modellene vil trenes på historiske data fra 2022–2024 og brukes til å generere prognoser for 2025\.

Videre vil løsningen inkludere evaluering av modellene ved hjelp av målemetoder som MAPE (Mean Absolute Percentage Error) og RMSE (Root Mean Square Error), samt analyse av hvilke variabler som har størst påvirkning på salget, for eksempel sesong, rabatt, region og produktkategori. Resultatene vil bli presentert gjennom visualiseringer og dokumentasjon som gjør det mulig å sammenligne modellene og vurdere hvilken modell som gir best prognoseytelse.

Et overordnet diagram er gitt nedenfor (se Vedlegg B for PlantUML-kode).

![Overordnet diagram for løsningen](./images/LOG650_Løsning.png)

### Arbeidsnedbrytningsstruktur

Daglivare sin arbeidsnedbrytningsstruktur (WBS) utgjør den formelle baselinen for hele prosjektets omfang. Prosjektleder og delprosjektledere gjennomførte flere planleggingsiterasjoner for å utarbeide WBS. WBS dokumenterer alle prosjektleveranser og fanger opp alt arbeid som skal utføres i prosjektet.

WBS er vist nedenfor (se Vedlegg B for PlantUML-kode).

![WBS-diagram for prosjektet](./images/LOG650_WBS.png)

Leveransene i arbeidsnedbrytningsstrukturen kan også finnes som flytskjema over rekkefølgen de utføres i, i seksjon 3.1 – Avhengighetsdiagram, og som planlagt over kalenderen i seksjon 3.2 – Gantt-plan.

### Omfangsverifikasjon

Alt arbeid som leveres inn i sluttproduktet skal verifiseres både av prosjekteamene som har produsert leveransene, og gjennom uavhengig verifikasjon fra QA-organisasjonen, for å sikre at leveransene er i samsvar med alle krav og er egnet for formålet – dvs. i stand til fullt ut å dekke behovet de var ment å tilfredsstille.

Før hver leveranse ferdigstilles skal prosjekteamene først verifisere eget arbeid for å sikre at det er feilfritt og oppfyller alle prosjektkrav, før det sendes videre til QA for verifikasjon. Leveranse-eierne skal ikke basere seg på QA-prosessen for å finne avvik og feil.

Kvalitetssikring (QA) skal deretter gjennomføre formell verifikasjon for å bekrefte at prosjektleveransene er korrekt bygget og konfigurert. Eventuelle avvik eller mangler skal dokumenteres, og korrigerende tiltak skal defineres av leveranse-eier. Korrigeringene skal gjennomføres så raskt som rimelig av leveranse-eierne, og deretter re-verifiseres av QA. En leveranse skal ikke passere verifikasjon før QA-organisasjonen formelt bekrefter at alle avvik er håndtert og at arbeidet er klart til å gå videre til neste steg.

Verifikasjoner kan gjennomføres gjennom inspeksjoner, demonstrasjoner, analyser eller tester, avhengig av hva som er hensiktsmessig. Verifikasjoner skal gjennomføres gjennom hele prosjektet etter hvert som enkeltdeler, utkast, versjoner, inkrementer eller sprinter ferdigstilles, for å avdekke avvik og muliggjøre korrigering lenge før endelig leveranse etableres som baseline.

Der det er mulig skal scenario-basert verifikasjon benyttes, der verifikasjonen gjennomføres i konteksten av et eksempel på faktisk bruk av leveransen. Dette gir mest mulig realistisk verifikasjon av at leveransen oppfyller kravene, og gjør det samtidig tydelig at arbeidet er egnet for formålet. De fremtidige forretningsprosessene (to-be) som utvikles som del av prosjektets første steg, vil være grunnlaget for disse scenarioene der det er relevant.

Der det er relevant skal terskler for avvik og feil etableres for å tillate at mindre avvik kan korrigeres i støtte-/driftsfasen, samtidig som arbeidet kan gå videre til neste steg. Når denne tilnærmingen vurderes som hensiktsmessig, skal QA samarbeide med prosjektgruppen og kunde-/brukergrupper for å etablere kriterier etter følgende struktur:

- Det må være null kategori 1-saker – som påvirker kjernefunksjonalitet.  
- Det må være færre enn N (f.eks. 3\) kategori 2-saker – der det finnes en workaround som er akseptabel for kunderepresentanten inntil saken er rettet innen rimelig tid.  
- Det må være færre enn M (f.eks. 5\) kategori 3-saker – mindre brukervennlighetsavvik som ikke hindrer bruk, og som kunderepresentanten godtar kan håndteres i støtte/driftsfasen eller i neste prosjektfase.

Der tersklene over vurderes som nyttige for vurdering av leveranser, skal de avtales og dokumenteres under testplanleggingen før leveransetesting starter.

## Fremdrift

Prosjektet har fulgt en strukturert fremgang fra den startsfasen, der problemstillingen rundt salgsprediksjon ved bruk av lineær regresjon og Random Forest ble definert, deretter fulgt av en grundig planleggingsgjennomgang som etablerte metodisk rammeverk og styringsverktøy som WBS og Gantt-plan. I gjennomføringsfasen blir Kaggle-datasettet transformert gjennom datarensing og variabelutvikling, etterfulgt av modelltrening og evaluering med presisjonsmålene MAPE og RMSE. Prosjektet ferdigstilles i avslutningsfasen, hvor kvalitetssikring av metode, teori og analyse danner grunnlaget for en helhetlig drøfting av funnene og markerer fullføringen av samtlige milepæler i forskningsprosjektet.

### Avhengighetsdiagram (AOA)

For å strukturere prosjektets logiske rekkefølge av hovedaktiviteter er det utarbeidet et AOA‑basert avhengighetsdiagram. Diagrammet beskriver alle aktiviteter (A–I) med tilhørende varigheter og nødvendige forutgående oppgaver, og gir dermed et tydelig bilde av prosjektets prosessflyt. Prosessen starter med problemdefinisjon og prosjektplanlegging (A), før den går videre til datainnsamling (B), dataforståelse (C) og datapreprosessering (D). Deretter følger feature engineering (E), modellbygging (F) og analyse/evaluering (G), før prosjektet avsluttes med rapportskriving (H) og endelig konklusjon og presentasjon (I). Denne strukturen synliggjør den sekvensielle avhengigheten mellom aktivitetene og danner grunnlaget for både Gantt‑planen og identifikasjonen av prosjektets kritiske linje.

| Kode | Hovedaktivitet | Varighet (d) | Forutgående |
| :---- | :---- | :---- | :---- |
| A | Problemdefinisjon & prosjektplan | 10 | Start |
| B | Datainnsamling & dokumentasjon | 2 | A |
| C | Dataforståelse & variabelanalyse | 3 | B |
| D | Datapreprosessering | 2 | C |
| E | Feature engineering | 1 | D |
| F | Modellbygging & trening | 8 | E |
| G | Analyse & evaluering | 11 | F |
| H | Rapportskriving | 31 | G |
| I | Konklusjon & presentasjon | 16 | H |

### Gantt-plan

![Gantt-plan for prosjektfremdrift](./images/LOG650_Gantt.png)

### Kritisk linje

Kritisk linje i prosjektet går gjennom alle hovedaktivitetene: A → B → C → D → E → F→ G → H → I. Dette innebærer at både datainnsamling, databehandling, modellbygging, analyse og rapportarbeid må gjennomføres uten forsinkelser. Enhver forsinkelse i disse aktivitetene vil påvirke prosjektets totale tidsplan.

### Milepæler

Milepælene i prosjektet fungerer som sentrale kontrollpunkter som markerer ferdigstillelsen av viktige leveranser i prosjektets ulike faser. De er tidsfestet i tråd med prosjektets fremdriftsplan og legger til rette for strukturert oppfølging av fremdriften.

M1 innebærer godkjenning av prosjektforslaget i februar, etterfulgt av M2 i mars hvor datagrunnlaget klargjøres. M3, satt til 10\. mars, omfatter testing av modellen, mens M4 den 20\. april markerer ferdigstillelse av modelloptimaliseringen. Videre representerer M5 den 27\. april innlevering av hovedutkastet til rapporten, før prosjektet avsluttes med M6 den 31\. mai med innlevering av endelig rapport.

Bruken av milepæler bidrar dermed til en strukturert prosjektgjennomføring med tydelige leveranser og klare tidsrammer.

| Milepæl | Beskrivelse | Planlagt dato (Antatt) |
| :---- | :---- | :---- |
| M1 | Prosjektforslag godkjent | februar |
| M2 | Datagrunnlag klargjort | 10\. mars |
| M3 | Testing av modellene | 23\. mars |
| M4 | Modelloptimalisering ferdig | 22\. april |
| M5 | Hovedutkast av rapport | 8.april |
| M6 | Endelig rapport levert | 19\. mai |

## Risiko

Notat: Knyttet til feilmarginer (feil med modell etc.) siden budsjett ikke er en del av dette prosjektet.

Denne seksjonen beskriver risikostyringsprosessen for Dagligvare-prosjektet og gir en kopi av risikoregisteret som baseline.

### Prosess for risikostyring

Risikoregisteret og tilhørende risikobudsjett ble utarbeidet av prosjektleder og prosjektledere for delområder, og forbedret iterativt gjennom planleggingsfasen. Risikoer ble identifisert ved å gå gjennom alle punkter i vår standard risikosjekkliste, ved å se på risikoplanlegging og erfaringer fra tidligere lignende prosjekter, samt ved konsultasjon med prosjektgruppen. Risikoene ble kvantifisert, tiltak ble utarbeidet for å unngå eller redusere risikoene så langt som mulig, beredskapsplaner ble utarbeidet for å håndtere hendelsen dersom risikoen likevel inntraff, og et endelig kvantifisert risikobudsjett ble etablert som baseline.

Sannsynlighet og tidsestimater for risikoene ble utviklet av prosjektgruppen basert på tidligere erfaring og ved bruk av Delphi-estimering. Kostnadsestimatene ble utviklet gjennom en kostnadskonsekvensanalyse som funksjon av estimert forsinkelsestid, og med hensyn til andre relevante kostnader.

Prosjektleder for Daglivare-prosjektet har ansvar for forvaltning av risikobudsjettet og for at prosjektet gjennomføres med ønsket resultat. Eiership til enkeltstående risikoer er lagt til det nivået som er nærmest og best i stand til å håndtere risikoen. Risikoregisteret skal gjennomgås ved slutten av hvert ukentlige statusmøte. Risikoutløsere skal overvåkes av risiko-eierne, og tiltak skal iverksettes proaktivt for å unngå eller redusere risiko der det er mulig. Risikotiltaksplaner skal revideres og forbedres gjennom hele prosjektet ved behov. Midler skal tas fra risikobudsjettet for å finansiere proaktive tiltak som gir størst mulig risikoreduksjon så tidlig som mulig. Dersom det blir tydelig at en risiko ikke kan unngås, skal beredskapsplanene aktiveres.

Prosjektleder er autorisert signeringsmyndighet for uttak fra risikobudsjettet i kroner. For å hente midler fra budsjettet skal prosjektleder sende inn et begrunnelsesskjema for uttak til Dagligvare-prosjektet sin økonomikontroller, der status for den planlagte risikoen som midlene brukes til dokumenteres fullt ut, eller hvorfor midlene trengs for en uforutsett risiko, hvilke alternativer til uttak fra risikobudsjettet som er vurdert og funnet uegnet, samt begrunnelse for beløpet som tas ut. Beløp som overstiger 10 % av opprinnelig risikobudsjett-baseline krever i tillegg godkjenning fra finansdirektør (VP Finance).

Risikotidsbufferen er planlagt i henhold til prinsippene for Critical Chain Management, som én samlet buffer før den kritiske kundehendelsen hvis planlagte dato skal beskyttes mest. Denne hendelsen ble identifisert som rett før oppstart av pilotutrulling av den første produksjonslinjen.

Aktuell status for risikobudsjettet skal rapporteres hver måned til sponsor, kunde og andre relevante interessenter i den månedlige prosjektgjennomgangen beskrevet i seksjon 9 – Kommunikasjon.

Eventuelle økninger i risikobudsjettet etter at denne planen er godkjent og etablert som baseline må gå gjennom den formelle endringskontrollprosessen beskrevet i seksjon 12 – Endringskontrollprosess.

### Risikoregister

Dagligvare-prosjektet sitt risikoregister, som viser kjente prosjektrisikoer, estimerte konsekvenser for tid og kostnad, eier, utløsere, tiltak og beredskapsplan, finnes på de følgende sidene.

| ID | Risiko | Sannsynlighet | Konsekvens | Eier | Utløser | Tiltak | Beredskapsplan |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| R1 | Datasettet inneholder manglende eller inkonsistente data | Middels | Forsinkelse i analyse og modellutvikling | Dataansvarlig | Mange manglende verdier eller feil i datasettet | Gjennomføre datarensing og datavalidering tidlig | Bruke alternative variabler eller redusere datasettet |
| R2 | Modellene gir lav prediksjonsnøyaktighet | Middels | Resultatene blir mindre nyttige | Kvalitetsleder | Høy RMSE eller MAPE i evalueringen | Justere hyperparametere og teste flere features | Velge den modellen som gir best resultat selv om forbedringen er liten |
| R3 | Manglende erfaring med verktøy eller metoder | Lav–Middels | Forsinket fremdrift | Prosjektleder | Problemer med implementering av modellene | Sette av tid til læring og testing | Søke hjelp fra dokumentasjon eller veileder |
| R4 | Tidsmangel mot slutten av prosjektet | Middels | Redusert kvalitet på rapport og analyse | Prosjektleder | Milepæler ikke nådd til planlagt tid | Følge prosjektplan og fremdriftsmøter | Prioritere kjerneoppgaver og redusere mindre viktige analyser |
| R5 | Teknisk feil i programvare eller miljø | Lav | Midlertidig stopp i arbeidet | Teknisk ansvarlig | Feil i Python-miljø eller bibliotek | Bruke versjonskontroll og dokumentere miljø | Reinstallere miljø eller bruke alternativ maskin |

## Interessenter

For å sikre at alle interessenter forstår fremdriften og verdien av maskinlæringsmodellene, følger vi denne planen:Interne møter: Fokus på teknisk utvikling, feilsøking i datasettet (2022-2024) og koding av Linear Regression vs. Random Forest.  

**Teknisk til forretning:**  
Vi skal ikke bare rapportere at $RMSE$ har sunket. Vi skal forklare at en reduksjon i RMSE på 15 % betyr at vi kan treffe bedre på bestilling av ferskvarer, noe som reduserer svinn i simulerte butikker.

**Visualisering:**  
Vi bruker enkle grafer som sammenligner faktiske salgsdata mot modellens prediksjoner for 2025, slik at avviket (prognosefeilen) blir visuelt tydelig for ikke-teknikere.

| Interessent | Rolle | Behov/Forventning | Prioritet |
| :---- | :---- | :---- | :---- |
| **Bård Inge P. (BIP)** | Prosjektsponsor | At prosjektet leverer akademisk verdi og overholder tidsfrister. | Høy |
| **Kategorisjefer** | Bruker (Simulert) | Trenger nøyaktige prognoser for å unngå "out-of-stock" eller svinn. | Høy |
| **Logistikkdirektør** | Beslutningstaker | Ønsker å redusere totalkostnader gjennom bedre treffsikkerhet. | Middels |
| **Butikksjefer** | Sluttbruker | Enkel oversikt over forventet salg for å planlegge bemanning. | Lav |
| **Prosjektteamet** | Gjennomførere | God arbeidsflyt, tydelig ansvarsfordeling og teknisk mestring. | Høy |

## Ressurser

Denne seksjonen beskriver prosjektteamet, gir en ressursbelastning over tid, og beskriver planene for håndtering av kritiske ressurser som kreves for å gjennomføre Daglivare-prosjektet.

### Prosjektteam

Prosjektteamet som skal gjennomføre Daglivare-prosjektet er vist i organisasjonskartet og tabellen nedenfor.

På grunn av den kritiske betydningen nøyaktige etterspørselsprognoser har for dagligvarekjeden, er teamet satt sammen av medlemmer med komplementær kompetanse innen logistikk og maskinlæring. Teamet fungerer som en matriseorganisasjon der hver deltaker har et spesifikt fagansvar (f.eks. modellutvikling eller kvalitetssikring), men rapporterer til prosjektleder for den totale gjennomføringen.

For å sikre fremdrift i henhold til Gantt-planen, er alle teammedlemmer allokert til sine respektive oppgaver i periodene de trengs. Leveransene som hvert medlem er ansvarlig for, er spesifisert i tabellen under og samsvarer med ansvarsfordelingen i WBS-ordlisten.

Roller og ansvar for prosjektsponsor, prosjektleder og delprosjektledere er beskrevet i tabellen nedenfor.

| Name | Role | Responsibilities |
| :---- | :---- | :---- |
| Bård Inge P. | Prosjektsponsor | Godkjenning av prosjektplanen, omfang, fremdriftsplan, budsjett og risikobudsjett. Godkjenning av endringer i planens baseline når prosjektet er i gang. Lede de månedlige prosjektgjennomgangene. Sikre fortsatt støtte i virksomheten. Løse saker som prosjektleder ikke kan løse. |
| Erik Brendehaug | Prosjektleder | Lead Data Scientist & Modellansvarlig (Lineær Regresjon). Ansvarlig for datavasking og klargjøring av Kaggle-datasettet (2022-2024). Utvikler benchmark-modellen (Lineær Regresjon). • Lede prosjektet for å oppnå best mulig måloppnåelse mht. omfang, fremdrift, budsjett og risiko. • Lede delprosjektlederne. • Sikre at prosjektresultatet er egnet for formålet og fullt ut oppfyller interessentenes forventninger. • Formell statusrapportering av prosjektets fremdrift én gang per måned. • Gjennomføre de månedlige prosjektgjennomgangene og presentere prosjektstatus for |
| Joseph James | Modellansvarlig / Teknisk ansvarlig | Fremdriftsplanlegger & Modellansvarlig (Random Forest).Implementering av Random Forest Regressor. Sikre at tidsseriedataene håndteres riktig i trenings og testfasen. |
| Pål Rånes | Kvalitetsleder | Kvalitetsansvarlig & Logistikkanalytiker (Evaluering av MAPE/RMSE). Definere og beregne feilmarginer (RMSE/MAPE). Kontrollere at modellene ikke er "overfitted" og at resultatene er logistikkfaglig logiske. |
| Marthe S.Bjerke | Prosjektstyring | Ressurs og kommunikasjonsleder & Interessentkontakt.Koordinering av gruppen, dokumentasjon av fremdrift og oversettelse av tekniske resultater til rapporter for interessenter.  Ivareta sponsor og nøkkelinteressenter. Lede det ukentlige saksstatusmøtet. |

## Kommunikasjon

Denne seksjonen beskriver planlagt formell kommunikasjon etter hvert som Daglivare-prosjektet gjennomføres. Formell prosjektkommunikasjon skal sikre at alle teammedlemmer er samkjørte på de tekniske modellene, og at sponsor (BIP) holdes oppdatert på fremdriften mot 2025-prognosen.  
For å sikre fremdrift i henhold til Gantt-planen, er alle teammedlemmer allokert til sine respektive oppgaver i periodene de trengs. Leveransene som hvert medlem er ansvarlig for, er spesifisert i tabellen under og samsvarer med ansvarsfordelingen i WBS-ordlisten.

Prosjektteamet i Daglivare-prosjektet er vist i organisasjonskartet og tabellen nedenfor.

| Kommunikasjonsform | Formål | Møteleder/ansvar | Deltakere | Hovedfokus | Tid |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Ukentlige saksstatusmøter | Sikre at teamet er samkjørt på tekniske aktiviteter og fremdrift i modelleringen | Erik Brendehaug | Hele prosjektteamet | Gjennomgang av ukesoppgaver (f.eks. vasking av historiske data 2022–2024) Tekniske hindringer i koding av Linear Regression og Random Forest Oppdatering av prosjektets saksliste (Issue Log) | Hver mandag morgen kl. 09:00. Varighet inntil  én time. |
| Månedlige prosjektgjennomganger | Formålet med de månedlige gjennomgangene er å presentere status for sponsor (BIP) og eventuelle andre interessenter. Her oversettes tekniske beregninger til logistikkfaglig verdi. | Bård Inge P. (sponsor) | Hele prosjektteamet | Teknisk til Forretning**:** Vi forklarer hvordan endringer i RMSE/MAPE påvirker simulert lagerstyring (f.eks. "Modellen har nå 10% lavere feilmargin, som reduserer risiko for svinn"). Visualisering: Presentasjon av grafer som viser faktiske salgsdata mot modellens prediksjoner for 2025\. | Holdes kl.13:00 den første tirsdagen i hver måned i styrerommet Varighet: Inntil én time |
| Møter i endringskontrollstyret (CCB) | Formålet med CCB er å håndtere endringer som påvirker prosjektets omfang eller metodikk etter at baselinen er satt. | Pål Rånes | Hele prosjekt-teamet | Dersom vi for eksempel oppdager at Kaggle-datasettet mangler kritiske variabler for 2025-prognosen, må en endring i metodikk. | Ved behov |
| Annen kommunikasjon (Prosjektverktøy) | Effektiv daglig koordinering og trygg deling av kode og dokumentasjon | Joseph James | Hele prosjektteamet | Samhandlingsplattform**:** Teams for daglig koordinering av koding og skriving. Versjonskontroll**:**  GitHub for deling av Python-scripts og dokumentasjon, slik at alle alltid jobber på nyeste versjon av modellene. | kontinuerlig |

## Kvalitet  

Denne seksjonen beskriver tilnærmingen til kvalitetsstyring gjennom hele prosjektet. Kvaliteten på prosjektets leveranser er avgjørende for at analysen, modellene og rapporten skal være faglig solide og pålitelige. Prosjektgruppen vil derfor følge etablerte prinsipper for kvalitetsstyring gjennom hele prosjektperioden.

Kvalitet sikres gjennom god planlegging, strukturert arbeid, kontinuerlig evaluering av analyser og gjennomganger av arbeidet underveis i prosjektet.

Følgende fire kvalitetsprinsipper ligger til grunn for prosjektet:  

**1\.**   **Planlegging**

Kvalitet skal planlegges inn i prosjektet fra starten av. Dette innebærer tydelig definisjon av prosjektets mål, metode, datagrunnlag og analyseprosess. Selv om arbeidet kontrolleres og testes underveis, skal kvalitet først og fremst bygges inn i arbeidet gjennom gode arbeidsrutiner, tydelig dokumentasjon og strukturert utvikling av analyser og modeller.

 **2\.**   **Gevinst**

 God kvalitet i analyse og modellutvikling reduserer risikoen for feil og gir mer pålitelige resultater. Dette bidrar til bedre forståelse av problemstillingen og mer troverdige konklusjoner i prosjektet. Høy kvalitet i arbeidet kan også bidra til bedre innsikt i hvilke faktorer som påvirker etterspørselen etter dagligvarer.

 **3\.**   **Kontinuerlig forbedring**

 Prosjektgruppen vil evaluere arbeidet løpende gjennom prosjektperioden. Erfaringer fra analyser, modelltesting og diskusjoner i gruppen brukes til å forbedre arbeidet og justere metoder ved behov. Eventuelle utfordringer eller feil identifiseres tidlig slik at de kan korrigeres før prosjektets leveranser ferdigstilles.

**4\.**   **Egnet for formålet**

 Alle prosjektleveranser skal være egnet for formålet. Dette innebærer at analysene, modellene og rapporten skal bidra til å besvare prosjektets problemstilling på en tydelig og faglig korrekt måte. Resultatene skal være forståelige, etterprøvbare og basert på korrekt databehandling og analyse.

Alle prosjektmedlemmer skal bruke beste praksis innen dataanalyse, programmering og prosjektarbeid. Fagfellevurderinger og brukerreviews er derfor inkludert som viktige metoder for å sikre kvalitet i prosjektets leveranser.

### Fagfellevurderinger

Fagfellevurderinger er en viktig metode for å sikre at prosjektets leveranser holder høy kvalitet og oppfyller prosjektets mål. Gjennom fagfellevurderinger blir arbeidet gjennomgått av andre medlemmer i prosjektgruppen for å identifisere feil, forbedringsmuligheter og metodiske svakheter.

Det finnes to typer fagfellevurderinger: uformelle fagfellevurderinger og formelle fagfellevurderinger.  

#### Uformelle fagfellevurderinger

I dette prosjektet vil det hovedsakelig gjennomføres uformelle fagfellevurderinger. Disse vurderingene har mindre administrasjon enn formelle vurderinger, men gir likevel viktig kvalitetssikring av arbeidet.

Prosessen for uformelle fagfellevurderinger gjennomføres på følgende måte:

1\. Ansvarlig for en leveranse skal sørge for at arbeidet gjennomgås av minst ett eller to andre gruppemedlemmer før leveransen ferdigstilles.

2\. Ved større arbeidspakker kan det gjennomføres flere fagfellevurderinger underveis i utviklingsprosessen for å sikre at arbeidet holder riktig kvalitet.

3\. Fagfellene vurderer analyser, kode, metodevalg og resultater, og gir tilbakemeldinger på forbedringsmuligheter.

4\. Leveranse-eier samler inn kommentarer og vurderer hvilke forbedringer som bør implementeres i arbeidet.

5\. Kommentarene brukes til å forbedre leveransen før den inkluderes i den endelige rapporten.

Denne prosessen bidrar til å oppdage feil tidlig, forbedre kvaliteten på analysen og sikre at prosjektets resultater er faglig solide.

#### Formelle fagfellevurderinger

Formelle fagfellevurderinger benyttes vanligvis i prosjekter der leveranser har helse-, sikkerhets- eller juridisk betydning. Slike vurderinger innebærer mer strukturert dokumentasjon og administrasjon.

Siden dette prosjektet er et studentprosjekt innen dataanalyse og ikke omfatter leveranser med helse-, sikkerhets- eller juridisk sensitivitet, vil det normalt ikke være behov for formelle fagfellevurderinger. Kvalitetssikringen vil derfor hovedsakelig skje gjennom de uformelle fagfellevurderingene i prosjektgruppen.

## Anskaffelser

Denne seksjonen beskriver tilnærmingen til anskaffelser i prosjektet, inkludert hvilke digitale ressurser, verktøy og teknologier som benyttes for å gjennomføre prosjektet. Anskaffelser i dette prosjektet omfatter hovedsakelig programvare, datasett og utviklingsverktøy som brukes til dataanalyse, modellutvikling og samarbeid i prosjektgruppen.

Siden prosjektet er et analyse- og studentprosjekt innen maskinlæring og dataanalyse, vil de fleste ressursene som benyttes være digitale verktøy og åpne plattformer. Prosjektet baserer seg i stor grad på open-source teknologi og tilgjengelige nettbaserte tjenester, noe som reduserer kostnader og gjør prosjektet enklere å gjennomføre.

### Oversikt over anskaffelser

Prosjektet krever tilgang til følgende hovedressurser:

#### Datasett

Prosjektet benytter datasettet Supermart Grocery Sales – Retail Analytics Dataset, som er hentet fra plattformen Kaggle. Dette datasettet inneholder historiske salgsdata fra en dagligvarekjede og inkluderer informasjon om blant annet produkter, regioner, rabatter og salgstidspunkt.

Datasettet brukes som grunnlag for utvikling av maskinlæringsmodeller som skal predikere fremtidig etterspørsel etter dagligvarer. Datasettet er offentlig tilgjengelig og kan lastes ned gratis fra Kaggle, noe som gjør anskaffelsesprosessen enkel og kostnadseffektiv.

#### Programvare for dataanalyse

For å utvikle og teste maskinlæringsmodellene vil prosjektet benytte programmeringsspråket Python, som er et av de mest brukte språkene innen dataanalyse og maskinlæring.

Følgende Python-biblioteker vil bli brukt i prosjektet:

- Pandas for databehandling og analyse  
- NumPy for numeriske beregninger  
- Scikit-learn for implementering av maskinlæringsmodeller  
- Matplotlib og Seaborn for datavisualisering

Disse bibliotekene er open-source og kan installeres gratis via Python-pakkebehandlere.

#### Utviklingsmiljø

Prosjektet vil benytte Visual Studio Code (VS Code) som utviklingsmiljø for programmering, analyse og modellutvikling. VS Code gir et fleksibelt og kraftig miljø for programvareutvikling og støtter integrasjon med ulike verktøy for dataanalyse og versjonskontroll.

Utviklingsmiljøet gjør det mulig for prosjektgruppen å skrive, teste og kjøre kode på en strukturert måte. VS Code støtter også utvidelser som gjør det enklere å arbeide med Python og maskinlæringsprosjekter.

#### Kunstig intelligens-verktøy

I prosjektet vil det også benyttes kunstig intelligens-verktøy for å støtte utviklingsprosessen. Et eksempel på dette er Gemini CLI, som kan brukes i Visual Studio Code for å støtte programmering, kodeanalyse og problemløsning.

Kunstig intelligens kan bidra til:

- generering og forbedring av kode  
- feilsøking og debugging  
- forslag til optimalisering av algoritmer  
- støtte til dokumentasjon av kode og analyser

Bruken av slike verktøy kan bidra til mer effektiv utvikling og bedre kvalitet på prosjektets tekniske løsninger.

#### Versjonskontroll og samarbeid

Prosjektet vil bruke GitHub som plattform for versjonskontroll og samarbeid mellom gruppemedlemmene. GitHub gjør det mulig å lagre kode, analysere endringer i prosjektet og samarbeide effektivt om utviklingen.

Følgende funksjoner i GitHub vil bli brukt:

- lagring av prosjektkode i et repository  
- versjonskontroll av kode og dokumenter  
- samarbeid gjennom pull requests og commits  
- sikker lagring av prosjektets utviklingshistorikk

Ved å bruke GitHub kan prosjektgruppen sikre at alle endringer i prosjektet blir dokumentert og at arbeidet kan spores over tid.

#### Dokumentasjon og rapportskriving

For dokumentasjon og rapportskriving vil prosjektgruppen bruke tekstbehandlingsverktøy for å utvikle prosjektets rapport og prosjektstyringsplan. I tillegg vil visualiseringer og grafer fra analyseverktøyene bli inkludert i rapporten for å presentere resultater på en tydelig måte.

God dokumentasjon er viktig for å sikre transparens i prosjektet og gjøre det mulig for andre å forstå og eventuelt reprodusere analysen.

#### Anskaffelsesstrategi

Prosjektets anskaffelsesstrategi er basert på bruk av tilgjengelige og kostnadsfrie digitale ressurser. Ved å bruke open-source programvare og åpne datasett kan prosjektet gjennomføres uten direkte økonomiske kostnader.

Denne strategien gir flere fordeler:

- redusert økonomisk risiko  
- enkel tilgang til nødvendige verktøy  
- fleksibilitet i valg av analysemetoder  
- mulighet for etterprøvbarhet og reproduksjon av analysen

Alle verktøy og ressurser som benyttes i prosjektet vil bli dokumentert tydelig i rapporten.

#### Leverandører og teknologiplattformer

Prosjektets digitale ressurser leveres gjennom følgende plattformer:

- Kaggle – leverandør av datasett  
- GitHub – plattform for versjonskontroll og samarbeid  
- Visual Studio Code – utviklingsmiljø  
- Python og open-source biblioteker – analyseverktøy  
- Gemini CLI – kunstig intelligens-verktøy for programmeringsstøtte

Disse plattformene er bredt brukt innen forskning og programvareutvikling og anses som stabile og pålitelige teknologier.

#### Risiko knyttet til anskaffelser

Selv om prosjektet hovedsakelig bruker gratis og åpne ressurser, finnes det noen potensielle risikoer knyttet til anskaffelser og teknologibruk.

Mulige utfordringer kan være:  

- tekniske problemer med installasjon av programvare  
- kompatibilitetsproblemer mellom ulike verktøy  
- begrensninger i datasettets kvalitet eller struktur

For å redusere disse risikoene vil prosjektgruppen teste datasettet og analyseverktøyene tidlig i prosjektperioden. Eventuelle problemer kan dermed identifiseres og håndteres før hovedanalysen starter.

Gjennom denne tilnærmingen sikrer prosjektet at alle nødvendige ressurser er tilgjengelige og at analysearbeidet kan gjennomføres på en strukturert, effektiv og faglig forsvarlig måte.

## Endringskontrollprosess

Denne seksjonen beskriver hvordan foreslåtte endringer i prosjektet skal håndteres på en strukturert og kontrollert måte. Formålet med endringskontrollprosessen er å sikre at alle endringer blir vurdert grundig før de eventuelt implementeres, slik at konsekvenser for prosjektets omfang, fremdrift, kvalitet og risiko blir tatt hensyn til.

Når prosjektplanen er godkjent av sponsor, vil den fungere som prosjektets baseline. Alle endringer i prosjektets omfang, tidsplan, metodevalg eller leveranser må derfor vurderes gjennom en strukturert endringskontrollprosess før de kan gjennomføres.

Endringer kan for eksempel oppstå dersom:

·        nye krav eller analyser ønskes inkludert

·        det oppdages problemer i datasettet eller modellen

·        prosjektets tidsplan må justeres

·        metoder eller teknologier må endres

Gjennom en tydelig endringskontrollprosess kan prosjektgruppen sikre at endringer ikke skaper unødvendige problemer eller påvirker prosjektets mål negativt.

### Prosess for håndtering av endringer

Endringer i prosjektet håndteres gjennom følgende steg:

**1\. Registrering av endringsforslag**  
 Alle foreslåtte endringer skal først dokumenteres. Dette kan gjøres gjennom et enkelt endringsskjema eller ved å registrere endringen i prosjektets endringslogg. Endringen skal beskrive hva som ønskes endret, hvorfor endringen foreslås, og hvilke deler av prosjektet som kan bli påvirket.

**2\. Foreløpig vurdering av endringen**  
 Prosjektleder og prosjektgruppen vurderer om endringen er nødvendig og om den bør analyseres videre. I denne vurderingen ser man på om endringen kan påvirke prosjektets mål, fremdrift eller ressursbruk.

**3\. Analyse av konsekvenser**  
 Dersom endringen vurderes som relevant, gjennomføres en analyse av hvilke konsekvenser endringen kan få for prosjektet. Dette kan inkludere vurdering av påvirkning på:

·        prosjektets omfang

·        tidsplan og fremdrift

·        arbeidsoppgaver i prosjektet

·        risiko og kvalitet

Ved behov kan prosjektets planer oppdateres for å vise hvordan endringen vil påvirke prosjektet.

**4\. Beslutning om endringen**  
 Etter at konsekvensene er analysert, tas en beslutning om endringen skal godkjennes eller ikke. Mindre endringer kan besluttes av prosjektleder i samarbeid med prosjektgruppen. Større endringer som påvirker prosjektets mål eller fremdrift kan kreve godkjenning fra faglærer eller prosjektsponsor.

**5\. Implementering av endringen**  
 Dersom endringen godkjennes, oppdateres prosjektets dokumentasjon og planer. Dette kan inkludere oppdatering av prosjektplan, analyser, kode eller rapportstruktur.

**6\. Dokumentasjon av beslutningen**  
 Alle endringer og beslutninger skal dokumenteres i prosjektets endringslogg. Dette sikrer sporbarhet og gjør det mulig å se hvilke endringer som er gjort i prosjektet og hvorfor.

### Formål med endringskontroll

Endringskontrollprosessen bidrar til å sikre at prosjektet gjennomføres på en strukturert måte og at eventuelle endringer håndteres på en kontrollert måte. Dette reduserer risikoen for misforståelser, forsinkelser eller uplanlagte konsekvenser i prosjektet.

Ved å dokumentere og evaluere endringer systematisk kan prosjektgruppen opprettholde kontroll over prosjektets fremdrift og sikre at prosjektets mål fortsatt oppnås.

## Vedlegg

### Vedlegg A – Krav

Dette vedlegget gir en oversikt over prosjektkravene for \[ABC\], inkludert unik identifikator, type, eier av hvert krav og foreløpig sporbarhet til leveranser og testtilfeller som skal oppfylle kravene.

Sporbarheten mellom krav og leveranser vil bli raffinert til et mer detaljert nivå etter hvert som design utvikles under gjennomføringen. Tildelingen av testprosedyrer er for øyeblikket på prosedyrenivå, og vil bli raffinert til enkeltstående testtilfeller etter hvert som testdokumentasjonen utvikles.

| ID | Type | Requirement | Owner | Leveranse | Test Case |
| :---- | :---- | :---- | :---- | :---- | :---- |

### Vedlegg B – WBS og PlantUML-kode

#### Løsning plantUML-kode

```plantUML
@startuml
title Overordnet løsningsdiagram – Dagligvare prognoseprosjekt

rectangle "Historiske salgsdata\n(2022–2024)" as Data

rectangle "Datapreprosessering\n- Rensing\n- Feature engineering\n- Datasplitt (train/test)" as Prep

rectangle "Lineær regresjon\n(modell 1)" as LR
rectangle "Random Forest Regressor\n(modell 2)" as RF

rectangle "Evaluering\nMAPE\nRMSE" as Eval

rectangle "Resultater\n- Prognose for 2025\n- Viktige påvirkningsfaktorer\n- Visualiseringer" as Result

Data --> Prep
Prep --> LR
Prep --> RF
LR --> Eval
RF --> Eval
Eval --> Result

@enduml
```

#### WBS-illustrasjon

![WBS-illustrasjon i vedlegg B](images/LOG650_WBS.png)

#### WBS-PlantUML-kode

```plantUML
@startwbs
* Dagligvare Prognoseprosjekt

** 1. Prosjektplanlegging
*** 1.1 Definere problemstilling og prosjektmål
*** 1.2 Lage prosjektplan og rollefordeling

** 2. Datainnsamling og forståelse
*** 2.1 Finne og laste ned datasett
*** 2.2 Utforske datastruktur og variabler
*** 2.3 Identifisere relevante variabler
*** 2.4 Dokumentere datasett

** 3. Datapreprosessering
*** 3.1 Rense data
*** 3.2 Feature engineering
*** 3.3 Splitte trenings- og testdata
*** 3.4 Eksplorativ analyse og visualisering

** 4. Modellutvikling
*** 4.1 Implementere lineær regresjon
*** 4.2 Implementere Random Forest Regressor
*** 4.3 Trene modellene
*** 4.4 Justere modellparametere

** 5. Modelltesting og evaluering
*** 5.1 Generere prognoser for 2025
*** 5.2 Beregne RMSE og MAPE
*** 5.3 Sammenligne modellresultater
*** 5.4 Analysere viktige variabler

** 6. Resultatanalyse
*** 6.1 Tolke modellresultater
*** 6.2 Diskutere styrker og svakheter
*** 6.3 Vurdere praktisk nytte

** 7. Rapport og dokumentasjon
*** 7.1 Skrive rapportkapitler og dokumentasjon
**** 7.1.1 Skrive grunninnledning, problemstilling, avgrensinger og antagelser
**** 7.1.2 Litteratur og teori
**** 7.1.3 Casebeskrivelse
**** 7.1.4 Metode og data
**** 7.1.5 Modellering, analyse og resultat
**** 7.1.6 Diskusjon, konklusjon, sammendrag, abstract og bibliografi
**** 7.1.7 Ferdigstille innledning etter at øvrig rapportskriving er gjort
*** 7.2 Lage og integrere figurer, tabeller og visualiseringer
**** 7.2.1 Velge rapportfigurer og tabeller
**** 7.2.2 Lage case- og datakapitlets figurer og tabeller
**** 7.2.3 Lage analyse-, resultat- og diskusjonsfigurer og tabeller
**** 7.2.4 Sette inn, nummerere og formatere figurer og tabeller i rapporten
*** 7.3 Kvalitetssikre og låse førsteutkast
**** 7.3.1 Struktur- og kravsjekk av rapportutkast
**** 7.3.2 Konsistenssjekk mot analyseartefakter
**** 7.3.3 Språkvask, henvisninger og låsing av førsteutkast

** 8. Ferdigstillelse
*** 8.1 Revisjon av rapport
*** 8.2 Skrive endelig konklusjon
*** 8.3 Forberede presentasjon
*** 8.4 Presentasjon / prosjektslutt

@endwbs
```

### Vedlegg C – Format for prosjektets saksliste

For enkel referanse gir dette vedlegget en kopi av formatet for Prosjektets saksliste (Saker List) som brukes til koordinering av det ukentlige saksstatusmøtet beskrevet i seksjon 9.1 – Ukentlige saksstatusmøter. Sakslisten skal spore sakens navn, status, ansvarlig og forventet dato for løsning for hver sak. Dette Microsoft Word-tabellformatet kan enkelt sorteres med kommandoen Layout / Sort etter at nye punkter er lagt til eller oppdatert, slik at sakene kan settes i ønsket rekkefølge etter Ansvarlig / Frist eller Frist / Ansvarlig.

**Prosjekt ABC \- Saksliste**

| Issue | Status | Lead | Due |
| :---- | :---- | :---- | :---- |
| Plassmangel | Ombygging av møterom 5 til arbeidsområde med skrivebord. | Andersen | 2050-01-15 |

**Bruk:**

- Legg til rader for nye elementer etter behov, og samle deretter sammen etter Lead eller Forfallsdato med menyelementet Tabell / Sorter.  
- Skriv inn datoer i formatet ÅÅÅÅ-MM-DD slik at Layout / Sorter-kommandoen fungerer konsekvent.
