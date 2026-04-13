# Random Forest – IBM Sammendrag

## APA 7-referanse

IBM. (u.å.). *What is random forest?*. Hentet 13. april 2026 fra https://www.ibm.com/think/topics/random-forest

## Metadata

- **Hentet dato:** 13. april 2026
- **Kilde:** IBM Think Topics
- **Forfatter(e):** Eda Kavlakoglu (IBM Research)
- **URL:** https://www.ibm.com/think/topics/random-forest

---

## Sammendrag

**Random Forest** er en populær maskinlæringsalgoritme som kombinerer utlatet fra flere beslutningstrær for å nå et enkelt resultat. Algoritmen ble patentet av Leo Breiman og Adele Cutler, og har blitt mye brukt på grunn av sin fleksibilitet og enkel bruk. Den håndterer både klassifikasjon og regresjonsoppgaver.

### Grunnleggende komponenter

**Beslutningstrær** danner grunnlaget for Random Forest. Beslutningstrær starter med et grunnleggende spørsmål og stiller en serie oppfølgingsspørsmål for å bestemme et svar. Disse spørsmålene utgjør beslutningsnodene i treet, som fungerer som splittkriteria for dataene. Algoritmen søker etter de beste splittingene ved bruk av metrikkene Gini-urenhet, informasjonsgevinst eller gjennomsnittlig kvadratfeil (MSE). 

**Ensemble-metoder** kombinerer prediksjoner fra flere klassifikatorer. Random Forest er basert på *bagging* (bootstrap aggregation), der data samplet med erstatning, og hver modell blir trent uavhengig.

### Random Forest-algoritmen

Random Forest utvider bagging ved å kombinere både bagging og *feature randomness*. Dette kalles også "random subspace method" og genererer et tilfeldig delsett av features, som sikrer lav korrelasjon mellom beslutningstrær. En nøkkeldifferens fra enkle beslutningstrær er at Random Forest bare velger en delmengde av features ved hver splitting, i stedet for å vurdere alle mulige splits.

### Hvordan den fungerer

Algoritmen har tre hovedhyperparametre:
- Antall trær
- Nodnummer
- Antall samplende features

Hvert tre bygges fra en bootstrap-sample (data samplet med erstatning). En tredjedel av data settes til side som test-data (out-of-bag eller OOB-sample). For regresjonsoppgaver blir prediksjoner fra alle trær gjennomsnittliggjort; for klassifikasjonsoppgaver brukes flertallsvotering.

### Fordeler

- **Reduserer overfitting:** Kombinasjonen av ukorrelerte trær reduserer overordnet varians og prediksjonfeil
- **Fleksibel:** Fungerer for både klassifikasjon og regresjon, håndterer manglende data godt
- **Feature importance:** Gir lett identifikasjon av hvilke variabler som er viktigst for prediksjoner

### Begrensninger

- **Beregningsintensiv:** Krever betydelig tid når antallet trær er stort
- **Ressurskrevende:** Større datasett krever mer minnekapasitet
- **Kompleks tolking:** Vanskeligere å tolke enn enkle beslutningstrær

### Praktiske anvendelser

Random Forest brukes i finans (kredittrisiko, svindeldeteksjon), helsevesen (genekspresjon, biomarkørdeteksjon) og e-handel (anbefalinger).

---

## Stikkord / Keywords

- Ensemble learning
- Bootstrap aggregation (bagging)
- Feature randomness
- Decision trees
- Out-of-bag (OOB) sampling
- Gini impurity
- Feature importance
- Mean decrease in impurity (MDI)
- Classification and regression
- Overfitting reduction
