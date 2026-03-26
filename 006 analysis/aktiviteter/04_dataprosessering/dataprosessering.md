# Dataprosessering (WBS 3.1)

## Kort oppsummering

- Antall observasjoner inn: 9994
- Antall observasjoner ut: 9994
- Rader fjernet på grunn av manglende kritiske felt: 0
- Dubletter fjernet: 0
- Ugyldige datoer etter tolkning: 0

## Tolkningsregler

- Verdier med `-` tolkes som `dd-mm-yyyy`.
- Verdier med `/` tolkes som `mm/dd/yyyy`.
- Renset datasett lagres med ISO-format `YYYY-MM-DD` i kolonnen `Order Date`.

## Funn i rådata

- Datoer med `dd-mm-yyyy`: 4042
- Datoer med `mm/dd/yyyy`: 5952
- Datoer med annet mønster: 0
- Totalt manglende verdier i rådata: 0
- Eksakte dubletter i rådata: 0

## Merknad for videre modellering

- `State` har bare én unik verdi i datasettet og kan vurderes ekskludert i senere modellering.
- Bruk `dataset_renset.csv` som grunnlag for datasplitt og videre feature engineering.
