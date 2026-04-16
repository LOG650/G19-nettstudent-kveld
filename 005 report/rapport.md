# Tittel (norsk og/eller engelsk) <!-- omit in toc -->

![Bilde 1](extracted_images/image_0.png)

Forfatter(e):

Totalt antall sider inkludert forsiden:

Molde, Innleveringsdato:

![Bilde 2](extracted_images/image_1.png)

---

## Obligatorisk egenerklæring/gruppeerklæring <!-- omit in toc -->

Den enkelte student er selv ansvarlig for å sette seg inn i hva som er lovlige hjelpemidler, retningslinjer for bruk av disse og regler om kildebruk.

Du/dere fyller ut erklæringen ved å klikke i ruten til høyre for den enkelte del 1–6:

<!-- markdownlint-disable MD033 -->
| Nr. | Erklæring | Avkryssing |
| --- | --- | --- |
| 1 | Jeg/vi erklærer at min/vår besvarelse er mitt/vårt eget arbeid. | ☐ |
| 2 | Jeg/vi erklærer videre at denne besvarelsen:<br>- ikke har vært brukt til annen eksamen<br>- ikke refererer til andres arbeid uten at det er oppgitt<br>- ikke refererer til eget tidligere arbeid uten at det er oppgitt<br>- har alle referanser oppgitt<br>- ikke er kopi eller duplikat | ☐ |
| 3 | Brudd på ovennevnte er fusk og kan medføre annullering. | ☐ |
| 4 | Oppgaven kan bli plagiatkontrollert i URKUND. | ☐ |
| 5 | Høgskolen vil behandle mistanke om fusk etter retningslinjene. | ☐ |
| 6 | Jeg/vi har satt oss inn i reglene for kildebruk. | ☐ |
<!-- markdownlint-enable MD033 -->
---

## Personvern <!-- omit in toc -->

### Personopplysningsloven <!-- omit in toc -->

| Spørsmål                          | Ja | Nei |
| --------------------------------- | -- | --- |
| Har oppgaven vært vurdert av NSD? | ☐  | ☐   |

- Hvis ja:  
  Referansenummer:

- Hvis nei:  
Jeg/vi erklærer at oppgaven ikke omfattes av Personopplysningsloven  ☐

---

### Helseforskningsloven <!-- omit in toc -->

| Spørsmål                                  | Ja | Nei |
| ----------------------------------------- | -- | --- |
| Har oppgaven vært til behandling hos REK? | ☐  | ☐   |

- Hvis ja:  
  Referansenummer:

---

## Publiseringsavtale <!-- omit in toc -->

| Felt        | Verdi |
| ----------- | ----- |
| Studiepoeng |       |
| Veileder    |       |

### Fullmakt til elektronisk publisering <!-- omit in toc -->

| Spørsmål                                                | Ja | Nei |
| ------------------------------------------------------- | -- | --- |
| Gjøre oppgaven tilgjengelig for elektronisk publisering | ☐  | ☐   |

| Spørsmål                              | Ja | Nei |
| ------------------------------------- | -- | --- |
| Er oppgaven båndlagt (konfidensiell)? | ☐  | ☐   |

- Hvis ja:

| Spørsmål                                 | Ja | Nei |
| ---------------------------------------- | -- | --- |
| Kan publiseres etter båndleggingsperiode | ☐  | ☐   |

Dato:

---

## Antall ord <!-- omit in toc -->

Marker denne setningen og skriv inn antall ord dersom nødvendig.

## Forfattererklæring <!-- omit in toc -->

Marker denne setningen og skriv inn forfattererklæring dersom nødvendig.

---

## Sammendrag <!-- omit in toc -->

## Abstract <!-- omit in toc -->

---

## Innhold <!-- omit in toc -->

- [1 Innledning](#1-innledning)
  - [1.1 Problemstilling](#11-problemstilling)
  - [1.3 Avgrensinger](#13-avgrensinger)
  - [1.4 Antagelser](#14-antagelser)
- [2 Litteratur](#2-litteratur)
- [3 Teori](#3-teori)
- [4 Casebeskrivelse](#4-casebeskrivelse)
  - [4.1 Dagligvare og beslutningssituasjonen](#41-dagligvare-og-beslutningssituasjonen)
  - [4.2 Historisk salgsutvikling](#42-historisk-salgsutvikling)
  - [4.3 Sesongmønster i salget](#43-sesongmønster-i-salget)
  - [4.4 Utfordringer dårlige prognoser medfører i bedriften](#44-utfordringer-dårlige-prognoser-medfører-i-bedriften)
- [5 Metode og data](#5-metode-og-data)
  - [5.1 Metode](#51-metode)
  - [5.2 Data](#52-data)
- [6 Modellering](#6-modellering)
- [7 Analyse](#7-analyse)
- [8 Resultat](#8-resultat)
- [9 Diskusjon](#9-diskusjon)
- [10 Konklusjon](#10-konklusjon)
- [11 Bibliografi](#11-bibliografi)
- [12 Vedlegg](#12-vedlegg)

---

## 1 Innledning

Dagligvarehandel er preget av høy variabilitet i etterspørsel. Salget svinger med sesong, kampanjer, rabatter og regionale forhold, og konsekvensene av dårlige prognoser er direkte synlige i driften: for høye bestillinger fører til svinn og bundet kapital, mens for lave bestillinger gir utsolgte varer og tapte inntekter. Behovet for mer presise etterspørselsprognoser er derfor sentralt for virksomheter som ønsker å ta bedre beslutninger knyttet til innkjøp, lager, kampanjer og ressursplanlegging.

Maskinlæringsbaserte modeller som Random Forest Regressor gir nye muligheter for å fange opp komplekse mønstre i historiske salgsdata sammenlignet med tradisjonelle lineære tilnærminger. I dette prosjektet analyseres et datasett som simulerer en dagligvarekjede med 9 994 daglige salgsrader over perioden 2022–2025, med mål om å utvikle og evaluere prognosemodeller for salg i 2025.

Rapporten er strukturert slik at casebeskrivelsen presenterer bedriften og det historiske salget i kapittel 4, metode og datagrunnlag beskrives i kapittel 5, modellvalg og spesifikasjon i kapittel 6, analyse og resultater i kapittel 7–8, og diskusjon og konklusjon i kapittel 9–10.

## 1.1 Problemstilling

Hvordan kan multippel lineær regresjon og Random Forest Regressor brukes til å forutsi salg for 2025 for en simulert dagligvarekjede, og hvilke faktorer påvirker salget mest?

## 1.3 Avgrensinger

Analysen er avgrenset på følgende punkter:

1. **Prediksjon, ikke kausal analyse.** Prosjektet undersøker hvilke variabler som predikerer salget best, ikke hvorfor salget endrer seg. Kausale slutninger forutsetter eksperimentelt design og ligger utenfor prosjektets rammer.
2. **Ingen lageroptimalisering.** Rapporten dokumenterer ikke lageroptimalisering. Det krever kostnads- og volumparametere som ikke inngår i datasettet.
3. **Ingen makroøkonomiske faktorer.** Eksterne variabler som inflasjon, rente og konjunkturer er ikke inkludert. Datasettet gir ikke grunnlag for dette, og inkludering av slike variabler ville kreve egne datakilder.
4. **Én simulert virksomhet og ett datasett.** Analysen begrenses til det tilgjengelige datasettet. Generalisering til andre virksomheter eller bransjer forutsetter eget datagrunnlag og ny validering.
5. **To modelltyper.** Modellvalget er begrenset til multippel lineær regresjon og Random Forest Regressor, i tråd med prosjektets faglige rammer og tilgjengelig treningsgrunnlag.

## 1.4 Antagelser

Analysen bygger på følgende eksplisitte antagelser:

1. **Representativitet.** Datasettet antas representativt for en realistisk dagligvarekjede med tanke på sesongmønstre, rabattbruk, regionfordeling og produktkategorier. *Konsekvens:* Funnene er gyldige innenfor dette caset, men ikke nødvendigvis overførbare til andre virksomheter eller reelle kjeder.
2. **Tidsmessig relevans.** Historiske mønstre fra 2022–2024 antas relevante for å predikere 2025. *Konsekvens:* Strukturelle brudd som betydelige prissjokk, atferdsendringer eller endringer i sortiment vil svekke prediksjonens gyldighet.
3. **Tilstrekkelig datakvalitet.** Datasettet antas å inneholde tilstrekkelig variasjon i nøkkeldimensjonene sesong, rabatt, region og produktkategori til å trene modellene. *Konsekvens:* Simulerte data kan undervurdere virkelig støy og sjeldne hendelser, noe som kan gi mer optimistiske målinger enn hva som er realistisk i produksjon.
4. **Testsett som fremtidig periode.** 2025-dataene er holdt helt utenfor trening og brukes som testperiode. *Konsekvens:* Evalueringen gir et realistisk bilde av prognosekvalitet under antakelsen om at 2025 ligner de foregående årene i mønster og struktur.

---

## 2 Litteratur

I salgsprognose og etterspørselspredikering er to metodetradisjoner spesielt relevante: klassisk statistisk regresjon og ensemble-basert maskinlæring. Begge er godt dokumenterte tilnærminger til prediktiv modellering i handels- og forretningskontekster.

Multippel lineær regresjon er en veletablert statistisk metode for å predikere en kontinuerlig utfallsvariabel fra flere forklaringsvariabler. IBM (u.å.-a) framhever at metoden er godt egnet for å avdekke mønstre i salgs- og innkjøpsdata og hjelpe ledere med å forutsi etterspørselsperioder for produkter. GeeksforGeeks (2026a) understreker at lineær regresjon er effektiv beregningskostnadsvis og gir et solid utgangspunkt for modellsammenlikning. Et fellestrekk i litteraturen er at metoden krever at flere antagelser er oppfylt: residualene skal følge normalfordelingen, variansen skal være konstant over alle prediktornivåer (homoskedastisitet), og det skal ikke være perfekt multikollinearitet mellom forklaringsvariablene (IBM, u.å.-a; GeeksforGeeks, 2026a). Brudd på disse antagelsene svekker tolkningsvaliditeten, men ikke nødvendigvis prediksjonskraften.

Random Forest representerer en nyere og mer fleksibel tilnærming. IBM (u.å.-b) og GeeksforGeeks (2026b) beskriver begge at algoritmen er en ensemble-metode som kombinerer prediksjoner fra flere uavhengige beslutningstrær og dermed reduserer variansen i prediksjoner sammenlignet med et enkelt tre. IBM (u.å.-b) framhever at Random Forest gir lett identifikasjon av hvilke variabler som er viktigst for prediksjonen gjennom feature importance-rangeringer, og at metoden er robust mot overfitting og håndterer manglende data godt. GeeksforGeeks (2026b) presiserer at algoritmen ikke krever normalisering og er fleksibel for både klassifikasjon og regresjon.

Litteraturen gir ikke ett entydig svar på hvilken modell som er best for salgsprognose — det avhenger av datastruktur, evalueringsmål og krav til tolkbarhet. Begge metodene er vanlige valg, og valget av evalueringsmetrikk påvirker konklusjonen. RMSE og MAPE er anerkjente metrikker for å sammenligne prognosemodeller, men de vektlegger henholdsvis absolutt og relativ feil ulikt (GeeksforGeeks, 2026a). At de to metrikkene ikke alltid peker på samme vinner, er en kjent utfordring i praktisk prognosearbeid.

De tilgjengelige kildene for dette prosjektet er webbaserte oppslagsverk fra IBM Think Topics og GeeksforGeeks, ikke fagfellevurderte vitenskapelige artikler. Kildene gir likevel faglig solide introduksjoner til de valgte metodene og tilstrekkelig grunnlag for metodevalgene i dette prosjektet. Supplering med fagfellevurderte studier — for eksempel om maskinlæring for etterspørselspredikering i dagligvarehandel — bør vurderes dersom kravene til akademisk dybde øker.

---

## 3 Teori

### 3.1 Multippel lineær regresjon

Multippel lineær regresjon er en supervisert læringsmetode som modellerer forholdet mellom en avhengig variabel og to eller flere uavhengige forklaringsvariabler. Modellen uttrykkes som:

$\hat{y} = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_n x_n$

der $\hat{y}$ er predikert verdi, $\beta_0$ er konstantleddet og $\beta_1, \ldots, \beta_n$ er regresjonskoeffisientene som uttrykker endringen i $\hat{y}$ per enhet endring i den tilhørende forklaringsvariabelen, alt annet likt (GeeksforGeeks, 2026a).

Koeffisientene estimeres med **Ordinary Least Squares (OLS)**, som minimerer summen av kvadrerte residualer:

$\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$

For at estimatene skal være gyldige krever metoden at fem antagelser er oppfylt (IBM, u.å.-a; GeeksforGeeks, 2026a): (1) linearitet mellom avhengig og uavhengige variabler, (2) uavhengige residualer, (3) homoskedastisitet — konstant varians i residualene på tvers av alle prediktornivåer, (4) normalfordelte residualer, og (5) ingen perfekt **multikollinearitet** mellom forklaringsvariablene. Multikollinearitet er særlig relevant i dette prosjektet fordi one-hot-kodede dummyvariabler kan skape høy innbyrdes korrelasjon og gjøre tolkning av enkeltkoeffisienter usikker.

Lineær regresjon brukes her som benchmarkmodell. Dens styrke er tolkbarhet — koeffisientene gir direkte innsikt i retning og størrelse av variabeleffekter. Dens begrensning er at den forutsetter et lineært mønster i dataene.

### 3.2 Random Forest Regressor

Random Forest er en ensemble-metode basert på et sett med beslutningstrær som samlet gir mer stabile prediksjoner enn ett enkelt tre (IBM, u.å.-b). Algoritmen hviler på to grunnprinsipper:

**Bootstrap aggregation (bagging):** Hvert tre trenes på et tilfeldig utvalg med tilbakelegging fra treningsdataene. Dermed ser hvert tre en litt annerledes versjon av datasettet, og trærne korrelerer mindre med hverandre (GeeksforGeeks, 2026b).

**Feature randomness:** Ved hver splittingsbeslutning i et tre velges kun et tilfeldig subsett av features til vurdering — ikke alle tilgjengelige variabler. Dette reduserer korrelasjon mellom trærne ytterligere og gjør ensemblet mer robust mot overfitting (IBM, u.å.-b).

For regresjonsoppgaver er den endelige prediksjonen gjennomsnittet av alle trærnes individuelle prediksjoner. Dette reduserer overordnet varians og demper effekten av støy i enkelttrær.

**Feature importance** beregnes som gjennomsnittlig reduksjon i MSE (Mean Decrease in Impurity) på tvers av alle trær og splittinger for en gitt variabel. En variabel som konsekvent reduserer prediksjonsfeilen i mange trær, rangeres høyt (IBM, u.å.-b).

Modellens oppførsel styres av hyperparametere som `n_estimators` (antall trær), `max_depth` (maksimal dybde per tre), `min_samples_leaf` (minste antall observasjoner i et løvnode) og `max_features` (antall features vurdert per split). Disse tilpasses gjennom hyperparametertuning mot et valideringssett.

### 3.3 Evalueringsmetrikker

To metrikker brukes for å evaluere prognosemodellene i dette prosjektet.

**RMSE (Root Mean Squared Error)** måler den gjennomsnittlige størrelsen på prediksjonsfeilen i samme enhet som utfallsvariabelen:

$\text{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}$

Kvadreringen medfører at store avvik vektes tyngre enn små. RMSE brukes som primær metrikk i dette prosjektet fordi absolutt presisjon — å treffe riktig salgsvolum — er det mest relevante kravet for innkjøp og lagerstyring.

**MAPE (Mean Absolute Percentage Error)** måler det gjennomsnittlige prosentvise avviket:

$\text{MAPE} = \frac{1}{n}\sum_{i=1}^{n}\left|\frac{y_i - \hat{y}_i}{y_i}\right| \times 100$

MAPE er skalanøytral og enklere å kommunisere, men er ustabil når faktiske verdier er nær null (divisjon mot null). Metrikken brukes som sekundær metrikk.

Når RMSE og MAPE peker på ulike vinnere, skyldes det at en modell kan ha lavt absolutt avvik på store volumer (lavt RMSE) uten å treffe proporsjonalt godt på små volumer (høy MAPE). Begge metrikkene er derfor nødvendige for å forstå modelloppførselen på tvers av ulike salgsnivåer (GeeksforGeeks, 2026a).

### 3.4 Feature engineering og dataoppsett

**Feature engineering** er prosessen med å utlede nye variabler fra rådata for å gjøre mønstre tilgjengelige for modellene. I dette prosjektet er kalendervariablene `year`, `month`, `quarter`, `weekofyear`, `dayofweek`, `dayofmonth` og `is_weekend` avledet fra den opprinnelige datovariabelen. Disse variablene fanger opp sesong-, uke- og kvartalsmønstre som ikke direkte kan leses fra en rådate (GeeksforGeeks, 2026a).

**One-hot encoding** konverterer kategoriske variabler — som Region, Category og Sub-Category — til binære dummyvariabler. For lineær regresjon er dette nødvendig fordi modellen krever numerisk input. Random Forest bruker her samme kodede matrise for konsistens i sammenligning (IBM, u.å.-a).

**Data leakage** oppstår når variabler som ikke ville vært tilgjengelige på prediksjonstidspunktet inkluderes i modellen. I dette prosjektet er `Profit` ekskludert fordi den kun er kjent etter at salget er gjennomført.

**Tidsbasert oppsplitting** er valgt fremfor tilfeldig oppsplitting. Treningsdata er 2022–2024 og testdata er 2025. Tilfeldig oppsplitting ville tillate fremtidige observasjoner å inngå i treningen, noe som gir kunstig god ytelse og ikke reflekterer reell prediksjon fremover i tid. I WBS 4.4 brukes 2024 i tillegg som intern valideringsperiode for hyperparametertuning av Random Forest, mens lineær regresjon beholdes med det fulle treningsgrunnlaget.

---

## 4 Casebeskrivelse

### 4.1 Dagligvare og beslutningssituasjonen

Dagligvare er en simulert dagligvarekjede som opererer på tvers av fem regioner: West, East, Central, South og North. Kjeden fører syv produktkategorier – Snacks, Eggs/Meat/Fish, Fruits & Veggies, Bakery, Beverages, Food Grains og Oil & Masala – fordelt på 23 subkategorier. Datasettet som danner analysegrunnlaget inneholder 9 994 daglige salgstransaksjoner fra perioden 2022–2025, fordelt på 24 byer.

Dagligvares operative planlegging er avhengig av pålitelige etterspørselsprognoser. Salget varierer med sesong, rabatter og regionale forhold, og konsekvensene av dårlige prognoser er direkte synlige i driften: for høye bestillinger gir svinn og bundet kapital, mens for lave bestillinger fører til utsolgte varer og tapte inntekter. Behovet for mer presise prognoser er dermed sentralt for innkjøp, lager, kampanjevurdering og ressursplanlegging.

Figur 4.1 viser gjennomsnittlig salgsnivå per produktkategori. Eggs, Meat & Fish skiller seg ut med det høyeste gjennomsnittlige salgsnivået i datasettet.

<div align="center">
  <img src="../006 analysis/aktiviteter/07_eksplorativ_analyse_og_visualisering/fig_sales_per_category.png" alt="Gjennomsnittlig salgsnivå per produktkategori" width="80%">
  <p align="center"><small><i>Figur 4.1 Gjennomsnittlig salgsnivå per produktkategori.</i></small></p>
</div>

### 4.2 Historisk salgsutvikling

Gjennomsnittlig daglig salg for hele perioden 2022–2025 er 1 497 med et spenn fra 500 til 2 500 og standardavvik på 578. Salgsnivået er stabilt over tid: gjennomsnittsnivået i treningsperioden 2022–2024 er 1 493, mot 1 503 i testperioden 2025. Ingen tydelig veksttrend er synlig i perioden – nivået holder seg relativt konstant med lokal variabilitet.

Figur 4.2 viser salgsforløpet over tid med trenings- og testperioden markert.

<div align="center">
  <img src="../006 analysis/aktiviteter/07_eksplorativ_analyse_og_visualisering/fig_sales_over_tid_train_test.png" alt="Salgsutvikling over tid, trening og test" width="80%">
  <p align="center"><small><i>Figur 4.2 Daglig salg over perioden 2022–2025, med treningsperiode (2022–2024) og testperiode (2025) vist.</i></small></p>
</div>

### 4.3 Sesongmønster i salget

Månedsmønsteret viser at oktober er måneden med det høyeste gjennomsnittlige salgsnivået, mens juni er den svakeste måneden. Mønsteret er konsistent mellom trenings- og testperioden, noe som tyder på et stabilt sesongmønster i datasettet. Fjerde kvartal fremstår samlet som den sterkeste perioden, mens andre og tredje kvartal er relativt svakere.

Figur 4.3 viser gjennomsnittlig salg per måned for henholdsvis trenings- og testperioden.

<div align="center">
  <img src="../006 analysis/aktiviteter/07_eksplorativ_analyse_og_visualisering/fig_sales_per_month_split.png" alt="Gjennomsnittlig salg per måned" width="80%">
  <p align="center"><small><i>Figur 4.3 Gjennomsnittlig daglig salg per måned for treningsperioden (2022–2024) og testperioden (2025).</i></small></p>
</div>

### 4.4 Utfordringer dårlige prognoser medfører i bedriften

For Dagligvare forsterkes planleggingsrisikoen av et sortiment som spenner fra ferske varer med kort holdbarhet til tørrvarer med lengre holdbarhetsperiode. Overskuddsbestillinger fører til direkte svinn og bundet kapital – konsekvenser som er særlig kostbare i kategorier som Eggs, Meat & Fish og Fruits & Veggies. Underestimering gir tomme hyller, tapte inntekter og risiko for å svekke kundelojaliteten.

Sesongvariasjonen i figur 4.3 viser at salget svinger markant gjennom året – med topp i oktober og bunnpunkt i juni. Kombinert med rabattavhengighet gjør dette at enkle tommelfingerregler for innkjøp gir dårlige resultater i perioder med høy kampanjeaktivitet eller sesongtopper.

Nøyaktige etterspørselsprognoser for 2025 kan gi Dagligvare et bedre grunnlag for innkjøpsplanlegging og lagerstyring, støtte vurderingen av kampanjeeffekter og bidra til mer presis ressursplanlegging i perioder med høy og lav etterspørsel.

---

## 5 Metode og data

### 5.1 Metode

Prosjektet er en kvantitativ, prediktiv studie der historiske salgsdata fra én simulert dagligvarekjede brukes til å bygge og evaluere prognosemodeller. Datagrunnlaget er ikke samlet inn, men stilt til disposisjon som en del av prosjektets faglige rammer. Problemstillingen besvares gjennom en trinnvis analytisk prosess: datasettet ble renset og gjort klart for modellering, deretter ble relevante variabler valgt og nye kalendervariabler utledet, og til slutt ble datasettet delt i en treningsperiode og en testperiode basert på tid.

Lineær regresjon ble valgt som benchmark-modell fordi metoden er tolkbar og gir et stabilt sammenligningsgrunnlag. Random Forest Regressor ble valgt som alternativmodell fordi den kan fange opp ikke-lineære mønstre og gir en naturlig rangering av variablenes prediksjonsverdi. Random Forest ble i tillegg tunet ved å trene på 2022–2023 og validere på 2024, slik at hyperparametere ble valgt uten å bruke testdataene. Alle tre modellspor – lineær regresjon, Random Forest baseline og tuned Random Forest – ble evaluert på 2025-data.

Evalueringen benytter RMSE som primær metrikk fordi absolutt presisjon er mest relevant for innkjøp og lagerstyring, og MAPE som sekundær metrikk for å gi et relativt bilde av prognosefeilen (se kap. 3.3). Modellene sammenlignes samlet for hele 2025 og per måned, og resultatene tolkes videre etter kvartal, rabattnivå, region og salgsnivå for å gi praktisk beslutningsstøtte til Dagligvare.

### 5.2 Data

Datagrunnlaget er filen `Dagligvare_Dataset.csv`, som inneholder 9 994 daglige salgstransaksjoner fra en simulert dagligvarekjede. Rådata dekker opprinnelig perioden 2015–2018 og er remappet med en syvårig kalenderforskyvning til prosjektperioden 2022–2025. Datasettet har 11 råkolonner og ingen manglende verdier eller dubletter. To ulike datoformater i kildedata – 4 042 rader med `dd-mm-yyyy` og 5 952 rader med `mm/dd/yyyy` – ble standardisert til ISO-format under rensingen.

Målvariabelen er `Sales` (heltall, spenn 500–2 500). Forklaringsvariablene som inngår i modellene er `Discount` (desimaltall, 0,10–0,35) og de kategoriske variablene `Category`, `Sub Category`, `City` og `Region`. Fra `Order Date` er det i tillegg utledet sju kalendervariabler: `year`, `month`, `quarter`, `weekofyear`, `dayofweek`, `dayofmonth` og `is_weekend`. Fire variabler ble ekskludert: `Profit` fordi den er en lekkasjevariabel som kun er kjent etter gjennomført salg, `State` fordi kolonnen er konstant i datasettet, og `Order ID` og `Customer Name` fordi de ikke har generaliserbar prediksjonsverdi. Kategoriske variabler ble one-hot-encoded til binære dummyvariabler, slik at den endelige modellmatrisen inneholder 67 features.

Fordelingen av kategoriske variabler viser at West-regionen utgjør 32 % av observasjonene, East 28 %, Central 23 % og South 16 %. North-regionen er representert med bare én observasjon og benyttes ikke som separat analysesegment. Produktkategoriene er jevnt fordelt med mellom 14 og 15 % av observasjonene hver, noe som betyr at ingen enkelt kategori dominerer datasettet.

Datasettet er delt tidsmessig slik at treningsdata dekker 2022–2024 og testdata dekker 2025. Tilfeldig splitt ble ikke brukt, fordi det ville tillate fremtidige observasjoner å inngå i treningen og dermed gi kunstig god ytelse. Det gjennomsnittlige salgsnivået er stabilt mellom periodene (1 493 i treningsdata og 1 503 i testdata), noe som styrker antakelsen om at historiske mønstre er overførbare til 2025. Tabell 5.1 viser fordelingen mellom trenings- og testdata.

| Delmengde | År | Antall rader | Andel |
| --- | --- | --- | --- |
| Treningsdata | 2022–2024 | 6 682 | ~67 % |
| Testdata | 2025 | 3 312 | ~33 % |

<p align="center"><small><i>Tabell 5.1 Fordeling av trenings- og testdata etter tidsmessig splitt.</i></small></p>

---

## 6 Modellering

Prosjektet evaluerer tre modellspor for å predikere daglig salg i 2025. Benchmark-modellen er en multippel lineær regresjon som gir et tolkbart sammenligningsgrunnlag. Random Forest inngår i to varianter: en baseline med standardparametere som viser hva en utuned ensemble-modell leverer på det samme datagrunnlaget, og en tuned variant der hyperparametere er valgt gjennom et strukturert søk. Sammenstillingen gir både et grunnlag for å måle gevinsten av tuning og et tolkbart referansepunkt som er robust mot overfitting.

Den multiple lineære regresjonen trenes som `LinearRegression` med `fit_intercept=True` og uten regularisering eller skalering. Modellen estimeres med OLS (se kap. 3.1) på 6 682 rader og 67 features – det vil si alle kalendervariabler, `Discount` og de one-hot-kodede kategoriske variablene. Estimert konstantledd er $-3193{,}55$. Modellen er tolkbar gjennom sine koeffisienter, men forutsetter at salget kan beskrives som en lineær kombinasjon av forklaringsvariablene, og den har ingen mekanisme for å fange opp interaksjoner eller ikke-lineære effekter utover de som eksplisitt er kodet inn.

Random Forest Regressor trenes på samme treningsmatrise. Baselinen bruker standardkonfigurasjonen `n_estimators=200`, `max_depth=None`, `min_samples_leaf=1`, `max_features=1.0` (dvs. at alle 67 features vurderes ved hver split), `bootstrap=True` og `random_state=42`, jf. bagging og feature randomness i kap. 3.2. Den tunede varianten bygger på et rutenettsøk der hver kandidat trenes på 2022–2023 (4 095 rader) og valideres på 2024 (2 587 rader). 2025-data inngår ikke i modellutvelgelsen – denne tidsmessige isolasjonen forhindrer datalekkasje mellom tuning og evaluering (jf. kap. 3.4 og 5.2). Vinnerkonfigurasjonen ble `n_estimators=400`, `max_depth=10`, `min_samples_leaf=4` og `max_features='sqrt'` (som gir $\lfloor\sqrt{67}\rfloor = 8$ features per split), valgt med validerings-RMSE som primærkriterium. Vinnerkandidaten oppnådde validerings-RMSE $577{,}27$ og validerings-MAPE $43{,}56\%$, mot baseline-kandidatens $590{,}30$ og $44{,}22\%$ på samme valideringssett. Den tunede modellen retrenes deretter på hele treningsperioden (2022–2024) før evaluering på 2025. Alle tre modellene genererer prognoser på testperioden 2025 (3 312 rader), og det er disse prognosene som danner grunnlaget for analyse og resultat i de neste kapitlene.

---

## 7 Analyse

Samlet for 2025 leverer den tunede Random Forest-modellen både lavest RMSE og lavest MAPE (jf. Tabell 8.1), marginalt foran benchmark lineær og tydeligere foran baseline Random Forest. Gapet mellom modellene er lite i absolutt forstand – tuned Random Forest forbedrer RMSE med omtrent $11$ enheter sammenlignet med baseline Random Forest og $2$ enheter sammenlignet med benchmark lineær. Tuningeffekten tolkes som en kombinasjon av dybdebegrensningen (`max_depth=10`) og redusert `max_features`, som demper variansen i de enkelte trærne og gir mer stabile ensemble-prediksjoner på nye data (jf. kap. 3.2).

Månedsnivået nyanserer bildet vesentlig (jf. Tabell 8.2). Tuned Random Forest vinner RMSE i 11 av 12 måneder, men vinner MAPE i bare 3 måneder. Baseline Random Forest vinner ikke en eneste måned på RMSE, men vinner MAPE i 6 av 12 måneder. RMSE og MAPE peker på samme vinner bare i juli og september. Mønsteret kan forklares med at absolutt feil og prosentfeil vekter observasjoner ulikt: RMSE straffer store avvik hardt og favoriserer dermed modellen som er mest treffsikker på de største salgsmålene, mens MAPE er mer sensitiv i måneder med mange lavvolumrader der små avvik gir utslag i høye prosenttall.

Bias-analysen av den tunede modellen viser et systematisk sesongavvik. August og september er underestimerte med henholdsvis $-5{,}22\%$ ($-20\,548$ salgsenheter) og $-2{,}77\%$ ($-16\,334$ salgsenheter), mens november og desember er lett overestimerte med $+1{,}05\%$ og $+2{,}36\%$. En mulig forklaring er at kalenderfeaturene ikke fullt ut fanger en høstoppgang som skiller seg fra tidligere år – antakelsen er at treningsperioden (2022–2024) inneholder en annen august–september-profil enn 2025, og at modellen dermed glatter ut det virkelige nivået i disse månedene. Mønsteret er konsistent på tvers av alle tre modellsporene og peker på en begrensning i det tilgjengelige sesongsignalet, ikke bare på den tunede modellen.

Segmentanalysen (jf. Tabell 8.4) forsterker forskjellen mellom de to metrikkene. Tuned Random Forest vinner RMSE i alle fire kvartaler, alle tre rabattband og alle fire regioner, men må vike for benchmark lineær og baseline Random Forest i flere av MAPE-segmentene – særlig i høyrabattsegmentet, vest-regionen og lavvolumssegmentet. I segmentet «høyt salg» er benchmark lineær best på begge metrikker (RMSE $699{,}10$, MAPE $30{,}31\%$), mens tuned Random Forest likevel gir lavest RMSE i segmentet «lavt salg» til tross for at MAPE der ligger på $89{,}39\%$.

Feature importance (jf. Tabell 8.3) støtter tolkningen av hvilke dimensjoner som driver variasjonen: kalendervariablene utgjør samlet $\sim 42\%$ av importance i topp 10, `Discount` er sterkeste enkeltvariabel med $11{,}48\%$, og regionvariablene bidrar med $\sim 5{,}8\%$. Den lineære modellen gir negativt fortegn på `Discount` (koeffisient $-166{,}35$), mens Random Forest rangerer samme variabel øverst. Forskjellen tolkes som et mulig tegn på en ikke-lineær eller interaktiv sammenheng mellom rabatt og salg som en lineær spesifikasjon ikke klarer å fange opp.

---

## 8 Resultat

Tabell 8.1 oppsummerer den samlede ytelsen på 2025 for de tre modellsporene. Tuned Random Forest har lavest RMSE og MAPE, mens baseline Random Forest er svakest på RMSE og benchmark lineær er svakest på MAPE.

| Modell | RMSE | MAPE |
| --- | --- | --- |
| Benchmark lineær | 580,39 | 44,18 % |
| Baseline Random Forest | 589,28 | 44,12 % |
| Tuned Random Forest | 578,26 | 43,97 % |

<p align="center"><small><i>Tabell 8.1 Samlet prognoseytelse på 2025 (3 312 observasjoner).</i></small></p>

Tabell 8.2 viser hvor mange av de tolv månedene i 2025 hver modell vinner på henholdsvis RMSE og MAPE.

| Modell | RMSE-vinner (av 12) | MAPE-vinner (av 12) |
| --- | --- | --- |
| Benchmark lineær | 1 | 3 |
| Baseline Random Forest | 0 | 6 |
| Tuned Random Forest | 11 | 3 |

<p align="center"><small><i>Tabell 8.2 Månedlig vinnertelling per metrikk i 2025.</i></small></p>

Tabell 8.3 viser de ti variablene med høyest feature importance i den tunede Random Forest-modellen, gruppert etter variabelgruppe.

| Rang | Variabel | Gruppe | Importance |
| --- | --- | --- | --- |
| 1 | Discount | Pris/kampanje | 11,48 % |
| 2 | dayofmonth | Kalender | 11,35 % |
| 3 | weekofyear | Kalender | 10,40 % |
| 4 | month | Kalender | 6,74 % |
| 5 | dayofweek | Kalender | 6,52 % |
| 6 | year | Kalender | 4,02 % |
| 7 | quarter | Kalender | 2,95 % |
| 8 | Region_East | Region | 2,04 % |
| 9 | Region_West | Region | 1,91 % |
| 10 | Region_Central | Region | 1,84 % |

<p align="center"><small><i>Tabell 8.3 Topp 10 feature importance for tuned Random Forest.</i></small></p>

Tabell 8.4 oppsummerer vinnermodellen per segment på RMSE og MAPE, fordelt på kvartal, rabattband, region og salgsnivå.

| Segmentdimensjon | Verdi | RMSE-vinner | MAPE-vinner |
| --- | --- | --- | --- |
| Kvartal | Q1 | Tuned RF | Benchmark lineær |
| Kvartal | Q2 | Tuned RF | Baseline RF |
| Kvartal | Q3 | Tuned RF | Tuned RF |
| Kvartal | Q4 | Tuned RF | Benchmark lineær |
| Rabatt | Lav | Tuned RF | Tuned RF |
| Rabatt | Middels | Tuned RF | Tuned RF |
| Rabatt | Høy | Tuned RF | Baseline RF |
| Region | Central | Tuned RF | Benchmark lineær |
| Region | East | Tuned RF | Tuned RF |
| Region | South | Tuned RF | Tuned RF |
| Region | West | Tuned RF | Baseline RF |
| Salgsnivå | Lavt salg | Tuned RF | Baseline RF |
| Salgsnivå | Middels salg | Tuned RF | Tuned RF |
| Salgsnivå | Høyt salg | Benchmark lineær | Benchmark lineær |

<p align="center"><small><i>Tabell 8.4 Vinnermodell per segment på RMSE og MAPE.</i></small></p>

---

## 9 Diskusjon

WBS 6.2 viser at tuned Random Forest er det mest robuste modellvalget når absolutte prognoseavvik prioriteres. Modellen er best samlet i 2025 og vinner `RMSE` i `11` av `12` måneder og `13` av `14` tolkingssegmenter. Samtidig har benchmark lineær høyere tolkbarhet og er fortsatt konkurransedyktig i enkelte segmenter, særlig på prosentfeil og i det høyeste salgssegmentet. Baseline Random Forest er svakest samlet, men har lokal styrke på `MAPE` og fungerer derfor som et nyttig sammenligningspunkt for å synliggjøre gevinsten av tuning.

Påliteligheten i funnene styrkes av et renset og sporbart datagrunnlag med `9994` rader, `0` manglende verdier, `0` dubletter og et tydelig tidsdelt trenings- og testoppsett. Generaliserbarheten er likevel begrenset fordi analysen bygger på én simulert virksomhet, ett datasett, et smalt modellomfang og ingen eksterne makroøkonomiske faktorer. I tillegg er analysen prediktiv og ikke kausal, slik at variabelsignalene bør brukes som prognosestøtte og ikke som bevis for årsakssammenhenger.

### Praktisk nytte for innkjøp og lager

For Dagligvare er den tydeligste praktiske nytten knyttet til innkjøp og overordnet lagerplanlegging. Når absolutte prognoseavvik prioriteres, fremstår tuned Random Forest som det mest relevante standardvalget fordi modellen er best samlet på `RMSE`, vinner `11` av `12` måneder på `RMSE` og `13` av `14` tolkingssegmenter. Det betyr ikke at rapporten dokumenterer lageroptimalisering, men at modellen gir det sterkeste grunnlaget i dette prosjektet for å treffe bedre på totalnivå i planlagte bestillinger og dermed redusere risikoen for for lave eller for høye volumanslag.

### Praktisk nytte for kampanje og rabatt

Kampanje- og rabattvurderinger krever mer varsom bruk. Variabelanalysen viser at `Discount` er det sterkeste signalet i den anbefalte modellen, og WBS 6.1 viser samtidig at prosentfeilen varierer mer enn absoluttfeilen i rabattutsatte segmenter. Det gjør tuned Random Forest relevant som hovedmodell også her, men med en ekstra kontroll mot `MAPE`, særlig i segmentet med høy rabatt der baseline Random Forest er best på prosentfeil. Praktisk betyr dette at Dagligvare kan bruke tuned Random Forest til hovedprognosen i kampanjeperioder, men bør tolke prosentavvik særskilt før tallene brukes direkte som støtte for rabattnære beslutninger.

### Praktisk nytte for bemanning og ressursplanlegging

Funnene har også nytte for aggregert bemannings- og ressursplanlegging fordi tuned Random Forest viser sterk stabilitet på `RMSE` både per måned og på tvers av kvartaler. Dette gir et mer robust bilde av forventet aktivitetsnivå gjennom året enn de svakere modellsporene. Samtidig viser tolkingssegmentene at benchmark lineær er best i segmentet for høyt salgsnivå, så toppbelastning bør behandles mer varsomt enn normal drift. Praktisk sett kan modellen derfor støtte overordnet kapasitetsplanlegging, men ikke leses som en ferdig løsning for butikkbemanning eller skiftoptimalisering.

### Ledelsesrapportering og forbehold

I ledelsesrapportering bør tuned Random Forest være hovedmodellen fordi den er best samlet på både `RMSE` og `MAPE`, mens benchmark lineær brukes som forklaringsstøtte når retningen i sentrale signaler må kommuniseres enkelt. Dette kan gjøre tekniske modellfunn mer forståelige for interessenter som er opptatt av innkjøp, kampanjer og ressursplanlegging. Samtidig må slike forklaringer holdes innenfor prosjektets avgrensning: analysen er prediktiv, ikke kausal, og verken rabatt-, region- eller kalendersignalene kan brukes som bevis for hvorfor salget endrer seg.

---

## 10 Konklusjon

Analysen viser at tuned Random Forest er det beste samlede modellvalget for å predikere salg i 2025 i dette caset, mens `Discount`, kalendervariabler og regionsignaler fremstår som de viktigste prediktive faktorene. I praksis kan Dagligvare bruke tuned Random Forest som standardprognose for innkjøp, lager og overordnet ressursplanlegging, mens benchmark lineær brukes som forklaringsstøtte og rabatt- eller toppbelastningssituasjoner kontrolleres særskilt.

---

## 11 Bibliografi

GeeksforGeeks. (2026a, 6. april). *Linear Regression in Machine Learning*. Hentet 13. april 2026 fra <https://www.geeksforgeeks.org/machine-learning/ml-linear-regression/>

GeeksforGeeks. (2026b, 6. april). *Random Forest Algorithm in Machine Learning*. Hentet 13. april 2026 fra <https://www.geeksforgeeks.org/machine-learning/random-forest-algorithm-in-machine-learning/>

IBM. (u.å.-a). *What is linear regression?*. Hentet 13. april 2026 fra <https://www.ibm.com/think/topics/linear-regression>

IBM. (u.å.-b). *What is random forest?*. Hentet 13. april 2026 fra <https://www.ibm.com/think/topics/random-forest>

## 12 Vedlegg
