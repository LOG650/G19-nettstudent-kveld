# Analyse av viktige variabler (WBS 5.4)

## Hva WBS 5.4 gjør

- Aktiviteten identifiserer og rangerer viktige variabler med utgangspunkt i eksisterende modellartefakter fra WBS 4.x og den anbefalte modellen fra WBS 5.3.
- `tuned RF` brukes som hovedkilde fordi modellen er markert som `anbefalt` i WBS 5.3.
- `baseline RF` brukes som stabilitetskontroll for Random Forest-signaler, mens lineær regresjon brukes som støttespor for fortegn og relativ plassering på overlappende variabler.

## Prioritert variabelliste

- WBS 5.4 rangerer disse variablene høyest i `tuned RF`: `Discount`, `dayofmonth`, `weekofyear`, `month`, `dayofweek`, `year`, `quarter`, `Region_East`, `Region_West`, `Region_Central`.
- Topp 3 i `tuned RF` er `Discount` (11.4781 %), `dayofmonth` (11.3529 %) og `weekofyear` (10.4042 %).
- Gruppeoppsummeringen viser at `kalender` dominerer topp 10 med `6` variabler og `41.9826 %` samlet importance.
- `pris/kampanje` bidrar med én variabel (`Discount`) og `11.4781 %`, mens `region` bidrar med `3` variabler og `5.7830 %`.

## RF-stabilitet mot baseline

- `baseline RF` og `tuned RF` deler `9` av `11` features i unionen av topp 10-signalene.
- Kun i `tuned RF`-topp 10: `quarter`.
- Kun i `baseline RF`-topp 10: `Region_South`.
- Toppsignal i `baseline RF`: `Discount` (12.3926 %).
- Toppsignal i `tuned RF`: `Discount` (11.4781 %).

## Lineær regresjon som støttespor

- Toppsignal i lineær regresjon er `Region_North` med `negativ` fortegn og `|koeff|=277.199368`.
- `Discount` er høyt prioritert i både lineær regresjon og begge Random Forest-varianter, og lineær regresjon gir her et negativt fortegn.
- `Region_East`, `Region_West` og `Region_Central` ligger høyt i `tuned RF` og har også positive koeffisienter i lineær regresjon.
- Flere kalendervariabler ligger svært høyt i `tuned RF`, men lavere i lineær regresjon. Dette dokumenteres som modellforskjell, ikke som årsaksforklaring.

## Produserte artefakter

- `tab_rf_tuned_feature_importance.csv`
- `tab_toppsignaler_per_modell.csv`
- `tab_rf_stabilitet_topp10.csv`
- `tab_viktige_variabler_oversikt.csv`
- `tab_variabelgrupper_tuned_top10.csv`
- `variabelanalyse.md`

## Avgrensning mot senere WBS-steg

- WBS 5.4 identifiserer og rangerer viktige variabler, men gjør ikke kausal analyse, SHAP, residualdiagnostikk eller full diskusjon av modellstyrker og svakheter.
- Dypere faglig tolkning, diskusjon og praktisk vurdering ligger fortsatt i WBS 6.1, 6.2 og 6.3.
