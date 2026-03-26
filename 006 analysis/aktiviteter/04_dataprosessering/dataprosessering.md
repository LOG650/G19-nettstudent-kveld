# Dataprosessering (WBS 3.1)

## Kort oppsummering

- Antall observasjoner inn: 9994
- Antall observasjoner ut: 9994
- Opprinnelig periode i kildedata: 2015-01-02 til 2018-12-30
- Remappet prosjektperiode: 2022-01-02 til 2025-12-30
- Rader fjernet på grunn av manglende kritiske felt: 0
- Dubletter fjernet: 0
- Ugyldige datoer etter tolkning: 0

## Tolkningsregler

- Verdier med `-` tolkes som `dd-mm-yyyy`.
- Verdier med `/` tolkes som `mm/dd/yyyy`.
- Etter rens forskyves hele tidsaksen med `7` år for å bruke datasettet som prosjektets 2022-2025-analog.
- Renset datasett lagres med ISO-format `YYYY-MM-DD` i kolonnen `Order Date`.

## Funn i rådata

- Datoer med `dd-mm-yyyy`: 4042
- Datoer med `mm/dd/yyyy`: 5952
- Datoer med annet mønster: 0
- Totalt manglende verdier i rådata: 0
- Eksakte dubletter i rådata: 0

## Merknad for videre modellering

- `State` har bare én unik verdi i datasettet og kan vurderes ekskludert i senere modellering.
- `dataset_renset.csv` er arbeidsgrunnlaget for WBS 3.2 feature engineering.
- WBS 3.3 datasplitt skal bygge på feature-datasettet fra WBS 3.2, ikke direkte på denne fila.
