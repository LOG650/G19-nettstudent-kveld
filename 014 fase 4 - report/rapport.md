# Prediksjon av dagligvaresalg for 2025

**Forfattere:** Marthe Slåtta Bjerke, Erik Brendehaug, Joseph James, Pål Arne Rånes  
**Dato:** 19. mars 2026  
**Emne:** LOG650 - Logistikk og Maskinlæring  

---

## Sammendrag

Dette prosjektet undersøker bruken av maskinlæringsmodellene lineær regresjon og Random Forest Regressor for å forutsi salg i en simulert dagligvarekjede for året 2025. Ved å benytte historiske salgsdata fra 2022 til 2024 som treningsgrunnlag, har målet vært å utvikle en modell som minimerer prognosefeil målt ved MAPE og RMSE. Resultatene gir innsikt i hvilke faktorer som påvirker salget mest, herunder sesongvariasjoner, rabatter og produktkategorier, noe som er kritisk for effektiv lagerstyring og beslutningsstøtte.

## Abstract

This project investigates the application of machine learning models, specifically Linear Regression and Random Forest Regressor, to predict sales for a simulated grocery chain in 2025. Using historical sales data from 2022 to 2024 for training, the objective was to develop a model that minimizes prediction error measured by MAPE and RMSE. The findings provide insights into key factors influencing sales, such as seasonality, discounts, and product categories, which are essential for effective inventory management and decision support.

---

## Innhold

- [1 Innledning](#1-innledning)
- [1.1 Problemstilling](#11-problemstilling)
- [1.2 Delproblemer](#12-delproblemer)
- [1.3 Avgrensinger](#13-avgrensinger)
- [1.4 Antagelser](#14-antagelser)
- [2 Litteratur](#2-litteratur)
- [3 Teori](#3-teori)
- [4 Casebeskrivelse](#4-casebeskrivelse)
- [5 Metode og data](#5-metode-og-data)
- [6 Modellering](#6-modellering)
- [11 Bibliografi](#11-bibliografi)
- [12 Vedlegg](#12-vedlegg)

---

## 1 Innledning

Presise etterspørselsprognoser er avgjørende i dagligvarebransjen for å balansere tilgjengelighet mot svinn. Med økende datatilgang og kraftigere analyseverktøy har maskinlæring blitt en sentral metode for å forbedre treffsikkerheten i slike prognoser. Denne rapporten tar for seg en simulert dagligvarekjede og utforsker hvordan avanserte regresjonsmodeller kan benyttes for å planlegge fremtidig salg.

### 1.1 Problemstilling

Hvordan kan vi bruke lineær regresjon og "Random Forest Regressor" til å forutsi salg i 2025 for en simulert dagligvarekjede, og hvilke faktorer har størst påvirkning på modellens nøyaktighet?

### 1.2 Delproblemer

1. Hvordan presterer en Random Forest-modell sammenlignet med en tradisjonell lineær regresjonsmodell målt i MAPE og RMSE?
2. Hvilken betydning har sesong, rabattnivå og produktkategori for salgsprognosene?

### 1.3 Avgrensinger

- Analysen fokuserer utelukkende på salgsprediksjon og ikke på operasjonell lageroptimalisering.
- Eksterne makroøkonomiske faktorer som inflasjon eller renter er ikke inkludert i datagrunnlaget.
- Studien er begrenset til ett spesifikt datasett fra Kaggle.

### 1.4 Antagelser

- Det antas at historiske mønstre fra 2022-2024 er representative for utviklingen i 2025.
- Datasettet fra Kaggle anses å ha tilstrekkelig kvalitet etter gjennomført rensing.

## 4 Casebeskrivelse

Casebedriften er en simulert dagligvarekjede som opererer i et marked preget av høy konkurranse og tynne marginer. For å opprettholde lønnsomhet er bedriften avhengig av å treffe flest mulig av beslutningene sine basert på data fremfor intuisjon.

<div align="center">
  <img src="../012 fase 2 - plan/images/LOG650_Løsning.png" alt="Løsningsdiagram" width="80%">
  <p align="center"><small><i>Figur 4.1 Overordnet løsningsdiagram for prognoseprosjektet.</i></small></p>
</div>

### 4.2 Historisk salgsutvikling

Historiske data viser betydelige svingninger gjennom året, noe som tyder på sterke sesongvariasjoner i enkelte produktgrupper.

## 5 Metode og data

Prosjektet følger en strukturert prosess for dataanalyse, fra innsamling til evaluering.

<div align="center">
  <img src="../012 fase 2 - plan/images/LOG650_WBS.png" alt="WBS" width="80%">
  <p align="center"><small><i>Figur 5.1 Arbeidsnedbrytningsstruktur (WBS) for prosjektgjennomføringen.</i></small></p>
</div>

### 5.2 Data

Datasettet består av salgstransaksjoner med variabler som dato, produktkategori, region og rabatt. For å validere modellene brukes data fra 2022-2024 til trening og 2025 som testsett.

## 6 Modellering

To modeller er valgt for denne studien:
1. **Multippel lineær regresjon:** Fungerer som en benchmark-modell.
2. **Random Forest Regressor:** En ensemble-metode som forventes å håndtere ikke-lineære sammenhenger bedre.

## 12 Vedlegg

Prosjektfremdrift er styrt etter en etablert Gantt-plan.

<div align="center">
  <img src="../012 fase 2 - plan/images/LOG650_Gantt.png" alt="Gantt-plan" width="80%">
  <p align="center"><small><i>Figur 12.1 Gantt-plan som viser prosjektets fremdrift og milepæler.</i></small></p>
</div>
