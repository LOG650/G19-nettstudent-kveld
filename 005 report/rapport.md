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
  - [4.1 PowerHorse og beslutningssituasjonen](#41-powerhorse-og-beslutningssituasjonen)
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

Diskuter relevante bidrag (siste 5 år).
Unngå synsing – referer alltid.

---

## 3 Teori

Beskriv teoretisk grunnlag og tidligere forskning.

---

## 4 Casebeskrivelse

### 4.1 PowerHorse og beslutningssituasjonen

Beskriv case/bedrift og relevant kontekst.

### 4.2 Historisk salgsutvikling

### 4.3 Sesongmønster i salget

### 4.4 Utfordringer dårlige prognoser medfører i bedriften

---

## 5 Metode og data

### 5.1 Metode

Analyseopplegget bygger på en trinnvis prosess der datasettet først ble renset, remappet til prosjektperioden 2022-2025, feature-engineered og splittet i treningsdata (2022-2024) og testdata (2025). Denne arbeidsflyten er dokumentert i analyseområdet og danner grunnlaget for modellutviklingen.

Som første modellsteg er lineær regresjon implementert som benchmark-modell på den one-hot-kodede modellmatrisen fra WBS 3.3. Random Forest Regressor er deretter implementert på samme treningsgrunnlag som alternativ modell med eksplisitte baseline-parametre. Etter at begge modellene var etablert, ble WBS 4.3 brukt til å verifisere at modellene bygger på samme treningsgrunnlag og til å samle sentrale modellinterne signaler før videre evaluering. I WBS 4.4 ble Random Forest-parametere deretter justert ved å trene på 2022-2023 og validere på 2024, slik at den valgte tuned-modellen kan tas videre til prognoser uten å bruke 2025-data i tuning. I WBS 5.1 er det generert prognoser for hele 2025 for lineær regresjon, Random Forest-baseline og tuned Random Forest, både på radnivå og som månedlig oppsummering. I WBS 5.2 er `RMSE` og `MAPE` deretter beregnet både samlet for hele 2025 og per måned med utgangspunkt i prognosene fra WBS 5.1. I WBS 5.3 er modellene sammenlignet med samlet 2025-`RMSE` som hovedregel og samlet `MAPE` som sekundær regel, der tuned Random Forest fremstår som samlet beste modell, samtidig som månedsnivået viser at metrikkene ikke alltid peker på samme vinner. I WBS 5.4 brukes denne anbefalte modellen som hovedgrunnlag for å rangere viktige variabler, med baseline-RF som stabilitetskontroll og lineær regresjon som støttespor for fortegn. I WBS 6.1 tolkes deretter modellresultatene videre ved å koble månedsbias og segmenterte `RMSE`-/`MAPE`-mønstre til kvartal, rabatt, region og salgsnivå. I WBS 6.2 diskuteres deretter modellstyrker, modellsvakheter og metodebegrensninger med eksplisitt skille mellom pålitelighet i dette oppsettet og generaliserbarhet utover caset.

Beskriv:

- Forskningsdesign
- Datainnsamling
- Analysemetoder

### 5.2 Data

Beskriv:

- Datakilder
- Innsamling
- Utvalg

---

## 6 Modellering

WBS 4.1 etablerer lineær regresjon som prosjektets benchmark-modell ved å trene `LinearRegression` på `X_train.csv` og `y_train.csv` fra datasplitten. WBS 4.2 etablerer `RandomForestRegressor` på samme treningsmatrise og dokumenterer sentrale parameterverdier og foreløpige feature importance-signaler. WBS 4.3 samler og verifiserer at begge modellene bygger på samme treningsgrunnlag før videre evaluering. WBS 4.4 tuner deretter Random Forest videre med 2024 som intern valideringsperiode, mens lineær regresjon beholdes uendret som benchmark. WBS 5.1 genererer deretter 2025-prognoser for benchmark-modellen, Random Forest-baseline og tuned Random Forest som grunnlag for senere metrikkberegning og sammenligning. WBS 5.4 bygger videre på disse artefaktene ved å hente ut feature importance for den tunede modellen og rangere viktige variabler uten å trene modellene på nytt.

---

## 7 Analyse

WBS 6.1 viser at tuned Random Forest er den mest stabile modellen på `RMSE` gjennom året og på tvers av kvartaler, rabattnivåer og regioner, men at `MAPE` oftere skifter vinner mellom modellene. Dette er særlig tydelig i segmentene for høy rabatt, vestlig region og høyt salgsnivå, der prosentfeil og absoluttfeil peker i ulik retning.

Tolkningen knytter disse mønstrene til variabelsignalene fra WBS 5.4: `Discount`, `quarter` og flere regionsignaler ligger høyt i den anbefalte modellen, og de samme dimensjonene forklarer mye av variasjonen i segmenterte metrikker. Salgsnivå brukes her som et avledet tolkningssegment for å forstå hvorfor en modell kan være best på absolutt feil uten å være best på prosentfeil.

---

## 8 Resultat

Det foreligger nå en første evalueringsleveranse i form av prognosefiler for 2025, beregnede `RMSE`-/`MAPE`-tabeller, en eksplisitt modellsammenligning for tre modellspor, en første rangering av viktige variabler, en første tolkning av modellmønstrene, en første diskusjon av styrker og svakheter og en første vurdering av praktisk nytte. Samlet for hele 2025 er tuned Random Forest best på både `RMSE` og `MAPE`, men månedsnivået viser at vinnermodellen varierer med valgt metrikk i store deler av året. Variabelanalysen peker samtidig på `Discount` og flere kalendervariabler som de tydeligste signalene i den anbefalte modellen, mens regionsignalene `Region_East`, `Region_West` og `Region_Central` også ligger høyt. WBS 6.1 viser videre at tuned Random Forest følger salgsnivå best på `RMSE` i lavt og middels salg, mens benchmark lineær er marginalt best i det høyeste salgssegmentet. WBS 6.2 viser i tillegg at modellvalget er robust på absoluttfeil innenfor dette prosjektoppsettet, men at generaliserbarheten er mer begrenset enn påliteligheten. WBS 6.3 oversetter disse funnene videre til praktisk beslutningsstøtte for Dagligvare innen innkjøp og lager, kampanje og rabatt, bemanning og ressursplanlegging og ledelsesrapportering.

Presenter funn:

- Tabeller
- Figurer
- Forklarende tekst

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

## 12 Vedlegg
