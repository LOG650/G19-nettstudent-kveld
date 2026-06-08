# M5 accuracy competition: Results, findings, and conclusions – Makridakis, Spiliotis & Assimakopoulos Sammendrag

## APA 7-referanse

Makridakis, S., Spiliotis, E., & Assimakopoulos, V. (2022). M5 accuracy competition: Results, findings, and conclusions. *International Journal of Forecasting*, 38(4), 1346–1364. https://doi.org/10.1016/j.ijforecast.2021.11.013

## Metadata

- **Hentet dato:** 8. juni 2026
- **Kilde:** International Journal of Forecasting (fagfellevurdert tidsskrift)
- **Type:** Konkurranserapport / empirisk studie
- **DOI/URL:** https://doi.org/10.1016/j.ijforecast.2021.11.013

---

## Sammendrag

Artikkelen oppsummerer resultatene fra M5-konkurransen, den femte i Makridakis-serien av prognosekonkurranser. M5 baserte seg på daglige hierarkiske salgsdata fra varehandel (Walmart), med over 42 000 tidsserier fordelt på produkt, butikk og region, samt eksterne variabler som pris, kampanjer og kalenderhendelser.

### Hovedfunn relevant for prosjektet

- **Tre-baserte ensembler dominerte.** Gradient-boostede tremodeller (særlig LightGBM) slo systematisk både klassiske statistiske metoder (ARIMA, eksponensiell glatting) og rene lineære/benchmark-modeller.
- **Maskinlæring forutsetter rike data.** Gevinsten ved maskinlæring var størst når modellene utnyttet kryss-læring på tvers av serier og rike forklaringsvariabler (pris, kampanje, kalender). Med begrenset feature-engineering var fortrinnet mindre.
- **Eksterne variabler er viktige.** Pris- og kampanjevariabler bidro vesentlig til prognosenøyaktigheten i daglige salgsdata.
- **Skalerte feilmål.** Konkurransen brukte skalerte feilmål (RMSSE/WRMSSE) framfor MAPE, blant annet for å unngå ustabilitet ved lave volum og nullsalg.

### Relevans for rapporten

Kilden støtter teorikapitlets argument om at tre-baserte ensembler kan slå lineære modeller når etterspørselsmønsteret er sammensatt og dataene er rike, men at fortrinnet er kontekstavhengig. Den brukes også til å begrunne svakheten ved MAPE ved lave volum (kap. 3.3).

---

## Stikkord / Keywords

- M5 competition
- Daily retail sales forecasting
- Gradient boosting (LightGBM)
- Hierarchical time series
- Cross-learning
- RMSSE / WRMSSE
- Machine learning vs. statistical methods
