# 04 Dataprosessering (WBS 3.1)

Denne aktiviteten renser, standardiserer og remapper datasettet til prosjektets arbeidsperiode før videre feature engineering og modellering.

## Kjøring

Kjør fra roten av `006 analysis`:

```bash
uv run python aktiviteter/04_dataprosessering/start_wbs_3_1.py
```

## Filer i mappen

- `start_wbs_3_1.py`: Leser rådata, standardiserer tekstfelt, tolker datoer, forskyver tidsaksen og lager renset datasett.
- `dataset_renset.csv`: Renset datasett sortert etter dato, med `Order Date` lagret i ISO-format og remappet til prosjektperioden 2022-2025.
- `tab_renselogg.csv`: Kort logg over hva som ble kontrollert og eventuelt fjernet.
- `tab_datakvalitet_etter_rens.csv`: Kolonneprofil etter rens.
- `dataprosessering.md`: Kort oppsummering som kan brukes videre i rapport og statusarbeid.

## Datakilde

- `004 data/Dagligvare_Dataset.csv`

## Viktig antagelse

- Datoverdier med `-` tolkes som `dd-mm-yyyy`.
- Datoverdier med `/` tolkes som `mm/dd/yyyy`.
- Den opprinnelige tidsserien forskyves `+7` år, slik at 2015-2018 brukes som prosjektets 2022-2025-analog.

## Neste steg

- Bruke `dataset_renset.csv` som grunnlag for WBS 3.2 feature engineering.
- La WBS 3.3 datasplitt bygge videre på feature-datasettet fra WBS 3.2.
