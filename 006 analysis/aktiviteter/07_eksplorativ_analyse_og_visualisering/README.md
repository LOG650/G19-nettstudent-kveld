# 07 Eksplorativ analyse og visualisering (WBS 3.4)

Denne aktiviteten beskriver målvariabelen og viktige mønstre i datasettet før modellbygging.

## Kjøring

Kjør fra roten av `006 analysis`:

```bash
uv run python aktiviteter/07_eksplorativ_analyse_og_visualisering/start_wbs_3_4.py
```

## Filer i mappen

- `start_wbs_3_4.py`: Leser feature-datasettet, lager EDA-tabeller og figurer og skriver en kort markdown-oppsummering.
- `tab_eda_oversikt.csv`: Oppsummering av `Sales` for hele datasettet, per periode og per år.
- `tab_kategorisk_fordeling.csv`: Frekvenstabell for `Category`, `Sub Category`, `City` og `Region`.
- `fig_sales_over_tid_train_test.png`: Månedlig totalsalg med tydelig skille mellom trening og test.
- `fig_sales_fordeling_train_test.png`: Fordeling av `Sales` i trening versus test.
- `fig_sales_per_month_split.png`: Sesongfigur som sammenligner månedsmønster mellom trening og test.
- `fig_sales_per_category.png`: Sammenligning av gjennomsnittlig salg per kategori for trening og test.
- `eda_visualisering.md`: Kort norsk oppsummering av de viktigste funnene.

## Datakilde

- `006 analysis/aktiviteter/05_feature_engineering/dataset_feature_engineered.csv`

## Viktige valg

- Aktiviteten bygger på eksisterende feature engineering og datasplitt uten å skrive tilbake til `05_feature_engineering` eller `06_datasplitt`.
- Trening (`2022-2024`) og test (`2025`) skilles eksplisitt i tabeller og figurer.
- Funnene er deskriptive og modellforberedende, ikke modelltrening.

## Neste steg

- Bruke funnene som grunnlag for lineær regresjon og Random Forest i modellutviklingen.
