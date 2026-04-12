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

- [Innledning](#innledning)
- [Problemstilling](#problemstilling)
- [Delproblemer (valgfri)](#delproblemer-valgfri)
- [Avgrensinger](#avgrensinger)
- [Antagelser](#antagelser)
- [Litteratur](#litteratur)
- [Teori](#teori)
- [Casebeskrivelse](#casebeskrivelse)
- [Metode og data](#metode-og-data)
  - [Metode](#metode)
  - [Data](#data)
- [Modellering](#modellering)
- [Analyse](#analyse)
- [Resultat](#resultat)
- [Diskusjon](#diskusjon)
- [Konklusjon](#konklusjon)
- [Bibliografi](#bibliografi)
- [Vedlegg](#vedlegg)

---

## Innledning

(tekst beholdt, lett ryddet til markdown)

Introduksjonen bør ikke være for lang (1–4 sider)...

**Svar på spørsmål:**

- Hvilket tema handler oppgaven om?
- Hvorfor er tema aktuelt?
- Hva har blitt gjort tidligere?
- Hva er problemstillingen?
- Hvilke avgrensninger gjøres?

---

## Problemstilling

Problemstillingen skal være et *hvordan* eller *hvorfor*-spørsmål.

Viktige krav:

- Vær spesifikk
- Vær presis
- Ikke svar på noe utenfor problemstillingen

---

## Delproblemer (valgfri)

Del opp problemstillingen ved behov.

---

## Avgrensinger

Forklar hva som ikke inkluderes og hvorfor.

---

## Antagelser

Presiser forutsetninger for analysen.

---

## Litteratur

Diskuter relevante bidrag (siste 5 år).
Unngå synsing – referer alltid.

---

## Teori

Beskriv teoretisk grunnlag og tidligere forskning.

---

## Casebeskrivelse

Beskriv case/bedrift og relevant kontekst.

---

## Metode og data

### Metode

Analyseopplegget bygger på en trinnvis prosess der datasettet først ble renset, remappet til prosjektperioden 2022-2025, feature-engineered og splittet i treningsdata (2022-2024) og testdata (2025). Denne arbeidsflyten er dokumentert i analyseområdet og danner grunnlaget for modellutviklingen.

Som første modellsteg er lineær regresjon implementert som benchmark-modell på den one-hot-kodede modellmatrisen fra WBS 3.3. Random Forest Regressor er deretter implementert på samme treningsgrunnlag som alternativ modell med eksplisitte baseline-parametre. Etter at begge modellene var etablert, ble WBS 4.3 brukt til å verifisere at modellene bygger på samme treningsgrunnlag og til å samle sentrale modellinterne signaler før videre evaluering. I WBS 4.4 ble Random Forest-parametere deretter justert ved å trene på 2022-2023 og validere på 2024, slik at den valgte tuned-modellen kan tas videre til prognoser uten å bruke 2025-data i tuning. I WBS 5.1 er det generert prognoser for hele 2025 for lineær regresjon, Random Forest-baseline og tuned Random Forest, både på radnivå og som månedlig oppsummering. I WBS 5.2 er `RMSE` og `MAPE` deretter beregnet både samlet for hele 2025 og per måned med utgangspunkt i prognosene fra WBS 5.1. I WBS 5.3 er modellene sammenlignet med samlet 2025-`RMSE` som hovedregel og samlet `MAPE` som sekundær regel, der tuned Random Forest fremstår som samlet beste modell, samtidig som månedsnivået viser at metrikkene ikke alltid peker på samme vinner. I WBS 5.4 brukes denne anbefalte modellen som hovedgrunnlag for å rangere viktige variabler, med baseline-RF som stabilitetskontroll og lineær regresjon som støttespor for fortegn. I WBS 6.1 tolkes deretter modellresultatene videre ved å koble månedsbias og segmenterte `RMSE`-/`MAPE`-mønstre til kvartal, rabatt, region og salgsnivå. I WBS 6.2 diskuteres deretter modellstyrker, modellsvakheter og metodebegrensninger med eksplisitt skille mellom pålitelighet i dette oppsettet og generaliserbarhet utover caset.

Beskriv:

- Forskningsdesign
- Datainnsamling
- Analysemetoder

### Data

Beskriv:

- Datakilder
- Innsamling
- Utvalg

---

## Modellering

WBS 4.1 etablerer lineær regresjon som prosjektets benchmark-modell ved å trene `LinearRegression` på `X_train.csv` og `y_train.csv` fra datasplitten. WBS 4.2 etablerer `RandomForestRegressor` på samme treningsmatrise og dokumenterer sentrale parameterverdier og foreløpige feature importance-signaler. WBS 4.3 samler og verifiserer at begge modellene bygger på samme treningsgrunnlag før videre evaluering. WBS 4.4 tuner deretter Random Forest videre med 2024 som intern valideringsperiode, mens lineær regresjon beholdes uendret som benchmark. WBS 5.1 genererer deretter 2025-prognoser for benchmark-modellen, Random Forest-baseline og tuned Random Forest som grunnlag for senere metrikkberegning og sammenligning. WBS 5.4 bygger videre på disse artefaktene ved å hente ut feature importance for den tunede modellen og rangere viktige variabler uten å trene modellene på nytt.

---

## Analyse

WBS 6.1 viser at tuned Random Forest er den mest stabile modellen på `RMSE` gjennom året og på tvers av kvartaler, rabattnivåer og regioner, men at `MAPE` oftere skifter vinner mellom modellene. Dette er særlig tydelig i segmentene for høy rabatt, vestlig region og høyt salgsnivå, der prosentfeil og absoluttfeil peker i ulik retning.

Tolkningen knytter disse mønstrene til variabelsignalene fra WBS 5.4: `Discount`, `quarter` og flere regionsignaler ligger høyt i den anbefalte modellen, og de samme dimensjonene forklarer mye av variasjonen i segmenterte metrikker. Salgsnivå brukes her som et avledet tolkningssegment for å forstå hvorfor en modell kan være best på absolutt feil uten å være best på prosentfeil.

---

## Resultat

Det foreligger nå en første evalueringsleveranse i form av prognosefiler for 2025, beregnede `RMSE`-/`MAPE`-tabeller, en eksplisitt modellsammenligning for tre modellspor, en første rangering av viktige variabler, en første tolkning av modellmønstrene, en første diskusjon av styrker og svakheter og en første vurdering av praktisk nytte. Samlet for hele 2025 er tuned Random Forest best på både `RMSE` og `MAPE`, men månedsnivået viser at vinnermodellen varierer med valgt metrikk i store deler av året. Variabelanalysen peker samtidig på `Discount` og flere kalendervariabler som de tydeligste signalene i den anbefalte modellen, mens regionsignalene `Region_East`, `Region_West` og `Region_Central` også ligger høyt. WBS 6.1 viser videre at tuned Random Forest følger salgsnivå best på `RMSE` i lavt og middels salg, mens benchmark lineær er marginalt best i det høyeste salgssegmentet. WBS 6.2 viser i tillegg at modellvalget er robust på absoluttfeil innenfor dette prosjektoppsettet, men at generaliserbarheten er mer begrenset enn påliteligheten. WBS 6.3 oversetter disse funnene videre til praktisk beslutningsstøtte for Dagligvare innen innkjøp og lager, kampanje og rabatt, bemanning og ressursplanlegging og ledelsesrapportering.

Presenter funn:

- Tabeller
- Figurer
- Forklarende tekst

---

## Diskusjon

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

## Konklusjon

Analysen viser at tuned Random Forest er det beste samlede modellvalget for å predikere salg i 2025 i dette caset, mens `Discount`, kalendervariabler og regionsignaler fremstår som de viktigste prediktive faktorene. I praksis kan Dagligvare bruke tuned Random Forest som standardprognose for innkjøp, lager og overordnet ressursplanlegging, mens benchmark lineær brukes som forklaringsstøtte og rabatt- eller toppbelastningssituasjoner kontrolleres særskilt.

---

## Bibliografi

## Vedlegg
