# 04 Dataprosessering (WBS 3.1)

Denne aktiviteten renser og standardiserer datasettet før videre datasplitt, feature engineering og modellering.

## Kjøring

Kjør fra roten av `006 analysis`:

```bash
uv run python aktiviteter/04_dataprosessering/start_wbs_3_1.py
```

## Filer i mappen

- `start_wbs_3_1.py`: Leser rådata, standardiserer tekstfelt, tolker datoer og lager renset datasett.
- `dataset_renset.csv`: Renset datasett sortert etter dato, med `Order Date` lagret i ISO-format.
- `tab_renselogg.csv`: Kort logg over hva som ble kontrollert og eventuelt fjernet.
- `tab_datakvalitet_etter_rens.csv`: Kolonneprofil etter rens.
- `dataprosessering.md`: Kort oppsummering som kan brukes videre i rapport og statusarbeid.

## Datakilde

- `004 data/Dagligvare_Dataset.csv`

## Viktig antagelse

- Datoverdier med `-` tolkes som `dd-mm-yyyy`.
- Datoverdier med `/` tolkes som `mm/dd/yyyy`.

## Neste steg

- Bruke `dataset_renset.csv` som grunnlag for datasplitt.
- Starte feature engineering på standardiserte dato- og kategorivariabler.
