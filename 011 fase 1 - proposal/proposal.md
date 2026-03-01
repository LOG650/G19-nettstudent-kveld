# Proposal LOG650

## Gruppemedlemmer

- Marthe Slåtta Bjerke
- Erik Brendehaug
- Joseph James
- Pål Arne Rånes

## Område

Etterspørselsprognoser

## Bedrift (valgbart)

“Simulerer” en daglivare-butikkjede ved å finne datasett på nettside som for eksempel kaggle.com.

## Problemstilling

Hvordan kan vi bruke lineær regresjon og “Random Forest Regressor” til å forutsi salg i 2025.

Vi ønsker å:

1) Lage modell som predikerer salg basert på historiske data (undersøke om Random Forest gir bedre predikeringsevne).
2) Undersøke hvilke faktorer som påvirker salget mest (sesong, rabatt, region, produktkategori).

## Data

[Supermart Grocery Sales - Retail Analytics Dataset](https://www.kaggle.com/datasets/mohamedharris/supermart-grocery-sales-retail-analytics-dataset)

Kommer til å gjøre en mindre endring der vi flytter opp datoene med (2015->2022, osv.)

(hentet fra kaggle.com)

Tankegangen er at vi bruker data for 2022-24 for å ordne prognose for 2025.

Altså 22-24 blir treningsdata og 25 blir test-data.

## Beslutningsvariabler

Beslutningsvariablene blir prognosene som er regnet ut av modellen.

## Modell

Valget av modell for dette datasettet blir to maskinlæringsmodeller. Vi må da finne ut akkurat hvilken type som passer datasettet best:

- Lineær regresjon (multippel som benchmark)
- Random Forest Regressor (undersøke om denne modellen forbedrer predikeringsevnen)

## Målfunksjon

Minimere prognosefeil uttrykt ved MAPE (Mean Absolute Percentage Error) og RMSE (Root Mean Square Error).

Notat: For eksempel, vi ordner prognose basert på 2022-24 for 2025 og sammenligner med faktisk 2025 salg.

## Avgrensninger

- Fokus på prediksjon, ikke kausal analyse.
- Lageroptimalisering modelleres ikke eksplisitt.
- Eksterne makroøkonomiske variabler inkluderes ikke.
- Analysen begrenses til én simulert virksomhet.
