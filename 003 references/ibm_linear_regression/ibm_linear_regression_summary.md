# Linear Regression – IBM Sammendrag

## APA 7-referanse

IBM. (u.å.). *What is linear regression?*. Hentet 13. april 2026 fra https://www.ibm.com/think/topics/linear-regression

## Metadata

- **Hentet dato:** 13. april 2026
- **Kilde:** IBM Think Topics
- **URL:** https://www.ibm.com/think/topics/linear-regression

---

## Sammendrag

**Linear Regression** er en fundamental statistisk metode for å predikere verdien av en variabel basert på verdien av en annen variabel. Metoden estimerer koeffisientene til en lineær ligning med én eller flere uavhengige variabler som predikerer verdien av den avhengige variabelen. Linear regression tilpasser en rett linje eller overflate som minimerer differansene mellom predikerte og faktiske utgangsdata.

### Grunnleggende konsept

I linear regression:
- **Avhengig variabel** = variabelen du vil predikere
- **Uavhengig variabel** = variabelen brukt til å predikere

Metoden bruker "least squares"-metoden for å finne den beste tilpassede linjen for et sett med parede data. Linear regression kan implementeres i ulike miljøer: R, MATLAB, Python (Sklearn), Excel og statistisk programvare som IBM SPSS.

### Hvorfor linear regression er viktig

Linear regression-modeller er relativt enkle og gir en lett tolket matematisk formel. Den kan brukes i biologiske, atferds-, miljø- og samfunnsvitenskaper samt business. Siden linear regression er en veletablert statistisk prosedyre, er egenskapene velforstådd og modeller kan trenes raskt.

**Forretningsmessige fordeler:**
- Bedrifter samler store datamengder som linear regression hjelper til med å tolke
- Kan avdekke mønstre i salgs- og innkjøpsdata
- Hjelper ledere forutse etterspørselsperioder for produkter
- Gir basis for bedre beslutningstaking instead for erfaring

### Kritiske antagelser

For vellykket linear regression må flere antagelser oppfylles:

1. **Variabltyper:** Avhengige og uavhengige variabler skal være kvantitative. Kategoriske variabler må rekodes til binære eller kontrastvariabler.

2. **Datakvalitet:** Data skal ikke ha signifikante utliggere.

3. **Linearitet:** Forholdet mellom variabler skal være lineært.

4. **Uavhengighet:** Alle observasjoner skal være uavhengige av hverandre.

5. **Homoskedastisitet:** Variansen av distribusjonen av den avhengige variabelen skal være konstant for alle verdier av den uavhengige variabelen.

6. **Normalfordeling:** Residualene (feilene) skal følge normalfordeling.

### Sjekkliste før implementering

Før du benytter linear regression, sikre at:
- Variabler måles på kontinuerlig nivå (tid, salg, vekt, testskårer)
- Scatterplot viser lineær relasjon mellom variabler
- Observasjoner er uavhengige
- Data inneholder ingen betydelige utliggere
- Homoskedastisitet er oppfylt
- Residualene følger normalfordeling

### Praktiske anvendelser

**Salg og trender:** Predikering av totalt årlig salgs basert på alder, utdanning og erfaring.

**Priselastisitet:** Analyse av hvordan prisendringer påvirker forbruksmønster.

**Risikovurdering:** Forsikringsselskaper bruker modeller for å estimere erstatningskostnader.

**Sports:** Modellering av forholdet mellom vunne kamper og gjennomsnittlige poeng per kamp.

---

## Stikkord / Keywords

- Supervised learning
- Dependent variable
- Independent variable
- Least squares method
- Regression coefficient
- Homoscedasticity
- Normality of residuals
- R² (R-squared)
- Adjusted R²
- Multiple linear regression
- Simple linear regression
- Outliers
- Continuous variables
