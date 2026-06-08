# Evaluating time series forecasting models: an empirical study on performance estimation methods – Cerqueira, Torgo & Mozetič Sammendrag

## APA 7-referanse

Cerqueira, V., Torgo, L., & Mozetič, I. (2020). Evaluating time series forecasting models: an empirical study on performance estimation methods. *Machine Learning*, 109(11), 1997–2028. https://doi.org/10.1007/s10994-020-05910-7

## Metadata

- **Hentet dato:** 8. juni 2026
- **Kilde:** Machine Learning, Springer (fagfellevurdert tidsskrift)
- **Type:** Empirisk metodestudie
- **DOI/URL:** https://doi.org/10.1007/s10994-020-05910-7

---

## Sammendrag

Studien undersøker hvordan man best estimerer ytelsen til prognosemodeller for tidsrekker, altså hvilke valideringsstrategier som gir et realistisk bilde av hvordan en modell vil prestere på framtidige data. Forfatterne sammenligner en rekke metoder for ytelsesestimering, inkludert out-of-sample-holdout, prequential (utvidende vindu) og ulike varianter av kryssvalidering.

### Hovedpoeng relevant for prosjektet

- **Tidsrekkefølgen må respekteres.** Valideringsstrategier som ignorerer den tidsmessige strukturen (f.eks. tilfeldig kryssvalidering) kan gi for optimistiske og misvisende ytelsesestimater fordi framtidig informasjon lekker inn i treningen.
- **Out-of-sample og prequential anbefales.** Metoder som holder testperioden strengt etter treningsperioden gir mer pålitelige estimater for reell prognoseytelse framover i tid.
- **Datalekkasje er en sentral feilkilde.** Studien dokumenterer empirisk hvorfor tidsbasert evaluering er nødvendig.

### Relevans for rapporten

Kilden forankrer prosjektets metodevalg om **tidsbasert oppsplitting** (2022–2024 trening, 2025 test) og bruken av 2024 som adskilt valideringsår, framfor tilfeldig oppsplitting. Den begrunner faglig hvorfor dette valget hindrer datalekkasje og gir et realistisk bilde av prognosekvaliteten (kap. 3.4 og 5).

---

## Stikkord / Keywords

- Performance estimation
- Time series cross-validation
- Out-of-sample evaluation
- Prequential / rolling-origin
- Data leakage
- Time-based split
- Forecast evaluation
