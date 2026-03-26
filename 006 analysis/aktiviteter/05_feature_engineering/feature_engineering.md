# Feature engineering (WBS 3.2)

## Kort oppsummering

- Antall observasjoner: 9994
- Periode i arbeidsgrunnlaget: 2022-01-02 til 2025-12-30
- Target: `Sales`
- Direkte features: `Discount, Category, Sub Category, City, Region`
- Utledede tidsfeatures: `year`, `month`, `quarter`, `weekofyear`, `dayofweek`, `dayofmonth`, `is_weekend`

## Viktige valg

- `Profit` er ekskludert som potensiell lekkasjevariabel.
- `State` er ekskludert fordi kolonnen er konstant.
- `Order ID` og `Customer Name` er ekskludert for å unngå overtilpasning.
- `Order Date` beholdes i feature-datasettet for sporbarhet og brukes videre i WBS 3.3 datasplitt.

## Videre bruk

- `dataset_feature_engineered.csv` er eneste operative input til WBS 3.3.
