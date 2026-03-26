# 05 Feature engineering (WBS 3.2)

Denne aktiviteten bygger direkte på `04_dataprosessering` og produserer et feature-engineered datasett som senere skal brukes i WBS 3.3 datasplitt.

## Kjøring

Kjør fra roten av `006 analysis`:

```bash
uv run python aktiviteter/05_feature_engineering/start_wbs_3_2.py
```

## Filer i mappen

- `start_wbs_3_2.py`: Leser remappet `dataset_renset.csv`, lager tidsfeatures og ekskluderer uegnede kolonner.
- `dataset_feature_engineered.csv`: Samlet feature-datasett med target, direkte features, tidsfeatures og `Order Date` for sporbarhet.
- `tab_featurevalg.csv`: Dokumentasjon av hvilke kolonner som ble beholdt, transformert og ekskludert.
- `feature_engineering.md`: Kort oppsummering av viktige featurevalg.

## Datakilde

- `006 analysis/aktiviteter/04_dataprosessering/dataset_renset.csv`

## Viktige valg

- `Profit` ekskluderes som potensiell lekkasje.
- `State` ekskluderes fordi kolonnen er konstant.
- `Order ID` og `Customer Name` ekskluderes fordi de ikke er egnede modellfeatures.
- `Order Date` beholdes i output for sporbarhet og tidsbasert splitt.

## Neste steg

- Bruke `dataset_feature_engineered.csv` som eneste operative input i WBS 3.3 datasplitt.
