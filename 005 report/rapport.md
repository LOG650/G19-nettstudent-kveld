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

Som første modellsteg er lineær regresjon implementert som benchmark-modell på den one-hot-kodede modellmatrisen fra WBS 3.3. Random Forest Regressor er deretter implementert på samme treningsgrunnlag som alternativ modell med eksplisitte baseline-parametre. Etter at begge modellene var etablert, ble WBS 4.3 brukt til å verifisere at modellene bygger på samme treningsgrunnlag og til å samle sentrale modellinterne signaler før videre evaluering. I WBS 4.4 ble Random Forest-parametere deretter justert ved å trene på 2022-2023 og validere på 2024, slik at den valgte tuned-modellen kan tas videre til prognoser uten å bruke 2025-data i tuning. I WBS 5.1 er det generert prognoser for hele 2025 for lineær regresjon, Random Forest-baseline og tuned Random Forest, både på radnivå og som månedlig oppsummering. I WBS 5.2 er `RMSE` og `MAPE` deretter beregnet både samlet for hele 2025 og per måned med utgangspunkt i prognosene fra WBS 5.1. I WBS 5.3 er modellene sammenlignet med samlet 2025-`RMSE` som hovedregel og samlet `MAPE` som sekundær regel, der tuned Random Forest fremstår som samlet beste modell, samtidig som månedsnivået viser at metrikkene ikke alltid peker på samme vinner. I WBS 5.4 brukes denne anbefalte modellen som hovedgrunnlag for å rangere viktige variabler, med baseline-RF som stabilitetskontroll og lineær regresjon som støttespor for fortegn. Videre faglig tolkning av forskjellene gjennomføres i senere aktiviteter.

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

Velg metode:

- Kvalitativ
- Kvantitativ
- Dokumentanalyse

---

## Resultat

Det foreligger nå en første evalueringsleveranse i form av prognosefiler for 2025, beregnede `RMSE`-/`MAPE`-tabeller, en eksplisitt modellsammenligning for tre modellspor og en første rangering av viktige variabler. Samlet for hele 2025 er tuned Random Forest best på både `RMSE` og `MAPE`, men månedsnivået viser at vinnermodellen varierer med valgt metrikk i store deler av året. Variabelanalysen peker samtidig på `Discount` og flere kalendervariabler som de tydeligste signalene i den anbefalte modellen, mens regionsignalene `Region_East`, `Region_West` og `Region_Central` også ligger høyt. Nærmere tolkning av hva dette betyr for caset er fortsatt utsatt til senere aktiviteter.

Presenter funn:

- Tabeller
- Figurer
- Forklarende tekst

---

## Diskusjon

Diskuter:

- Resultater
- Metode
- Pålitelighet
- Generaliserbarhet

---

## Konklusjon

Oppsummer hovedfunn i lys av problemstilling.

---

## Bibliografi

## Vedlegg
