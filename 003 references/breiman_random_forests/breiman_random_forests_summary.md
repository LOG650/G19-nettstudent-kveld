# Random Forests – Breiman Sammendrag

## APA 7-referanse

Breiman, L. (2001). Random forests. *Machine Learning*, 45(1), 5–32. https://doi.org/10.1023/A:1010933404324

## Metadata

- **Hentet dato:** 8. juni 2026
- **Kilde:** Machine Learning, Springer (fagfellevurdert tidsskrift)
- **Type:** Grunnleggende metodeartikkel (seminalverk)
- **DOI/URL:** https://doi.org/10.1023/A:1010933404324

---

## Sammendrag

Dette er originalartikkelen som introduserer **Random Forests**. Breiman definerer en random forest som et ensemble av beslutningstrær der hvert tre trenes på et bootstrap-utvalg av dataene, og der det ved hver splitt kun vurderes et tilfeldig subsett av variablene. Den endelige prediksjonen er et gjennomsnitt (regresjon) eller flertallsvotering (klassifikasjon) over trærne.

### Hovedpoeng relevant for prosjektet

- **To kilder til tilfeldighet.** Kombinasjonen av bootstrap-aggregering (bagging) og tilfeldig variabeluttrekk per splitt gjør trærne mindre korrelerte, noe som reduserer variansen i ensemblet uten å øke biasen tilsvarende.
- **Generaliseringsfeil og robusthet.** Breiman viser at generaliseringsfeilen konvergerer når antall trær øker, slik at modellen ikke overtilpasser ved flere trær. Feilen avhenger av styrken til enkelttrærne og korrelasjonen mellom dem.
- **Out-of-bag (OOB).** Observasjonene som ikke inngår i et tres bootstrap-utvalg, kan brukes som et innebygd, forventningsrett estimat på prediksjonsfeilen uten et separat valideringssett.
- **Variabelviktighet (feature importance).** Artikkelen introduserer mål for hvor mye hver variabel bidrar til prediksjonen, som er grunnlaget for feature importance-rangeringene som brukes i rapporten.

### Relevans for rapporten

Kilden er det teoretiske fundamentet for kapittel 3.2 (Random Forest Regressor): bagging, variabeltilfeldighet, bias–varians-avveiingen, OOB-validering og feature importance. Den forankrer hvorfor Random Forest er robust mot overfitting og hvorfor gjennomsnitting av avkorrelerte trær reduserer varians.

---

## Stikkord / Keywords

- Random forest
- Bootstrap aggregation (bagging)
- Feature randomness
- Out-of-bag (OOB) error
- Variable importance
- Generalization error
- Ensemble learning
- Bias–variance
