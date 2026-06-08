# Another look at measures of forecast accuracy – Hyndman & Koehler Sammendrag

## APA 7-referanse

Hyndman, R. J., & Koehler, A. B. (2006). Another look at measures of forecast accuracy. *International Journal of Forecasting*, 22(4), 679–688. https://doi.org/10.1016/j.ijforecast.2006.03.001

## Metadata

- **Hentet dato:** 8. juni 2026
- **Kilde:** International Journal of Forecasting (fagfellevurdert tidsskrift)
- **Type:** Metodeartikkel
- **DOI/URL:** https://doi.org/10.1016/j.ijforecast.2006.03.001

---

## Sammendrag

Artikkelen er en sentral og mye sitert gjennomgang av mål for prognosenøyaktighet. Forfatterne klassifiserer de vanligste feilmålene, drøfter deres egenskaper og svakheter, og foreslår skalerte feilmål som et mer robust alternativ.

### Hovedpoeng relevant for prosjektet

- **Ulike feilmål vektlegger feil ulikt.** Absolutte mål (som RMSE) og prosentbaserte mål (som MAPE) måler forskjellige aspekter ved prognosefeilen, og de kan peke på ulike modeller som best.
- **MAPE er ustabil ved lave verdier.** Prosentbaserte mål blir ustabile eller udefinerte når de faktiske verdiene er nær null, fordi man deler på en liten (eller null) nevner. De er også asymmetriske.
- **Skalerte feilmål.** Forfatterne introduserer skalerte feilmål (MASE) som er godt definert uavhengig av skala og volum, og som senere er tatt i bruk i bl.a. M-konkurransene.

### Relevans for rapporten

Kilden er det vitenskapelige grunnlaget for kapittel 3.3 (Evalueringsmetrikker): hvorfor RMSE og MAPE vektlegger feil ulikt, og hvorfor MAPE er ustabil ved lave salgsvolum. Den erstatter tidligere oppslagsverk (GeeksforGeeks) som kilde til metrikkenes egenskaper, og underbygger rapportens valg av RMSE som primær metrikk.

---

## Stikkord / Keywords

- Forecast accuracy
- RMSE
- MAPE
- Scaled errors (MASE)
- Percentage errors
- Low-volume instability
- Forecast evaluation
