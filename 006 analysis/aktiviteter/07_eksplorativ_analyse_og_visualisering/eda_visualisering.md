# Eksplorativ analyse og visualisering (WBS 3.4)

## Datagrunnlag

- Input: `05_feature_engineering/dataset_feature_engineered.csv`
- Trening: 2022-2024
- Test: 2025
- Antall observasjoner: 9994

## Hovedfunn

- Gjennomsnittlig salg er stabilt mellom trening og test, med `1493.49` i trening og `1502.87` i test.
- Det høyeste gjennomsnittlige månedsnivået ligger i `okt`, mens `jun` ligger lavest.
- Kategorien `Eggs, Meat & Fish` har høyest gjennomsnittlig salgsnivå i datasettet.
- Regionen `South` ligger høyest blant regionene med meningsfullt observasjonsvolum.
- `Region = North` er svært sparsom med bare `1` observasjon og må tolkes varsomt i modellarbeidet.

## Betydning for neste steg

- Tidsmønsteret bør testes både i lineær regresjon og Random Forest gjennom de etablerte tidsfeature-kolonnene.
- Kategori- og regionsignalene støtter at de kategoriske variablene bør beholdes i modellgrunnlaget.
- Stabilt gjennomsnitt mellom trening og test tyder på at tidsbasert holdout er brukbar for videre modelltesting.
