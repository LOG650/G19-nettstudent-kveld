# Datasplitt (WBS 3.3)

## Kort oppsummering

- Treningsår: 2022, 2023, 2024
- Testår: 2025
- Antall treningsrader: 6682
- Antall testrader: 3312
- Antall encoded feature-kolonner: 67

## Viktige valg

- Datasplitt bygger direkte på `dataset_feature_engineered.csv` fra WBS 3.2.
- `Order Date` brukes til sporbarhet i input, men fjernes fra modellmatrisene.
- Kategoriske features one-hot-encodes i dette steget slik at modelleringen kan bruke filene direkte.
