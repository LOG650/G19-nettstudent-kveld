# Praktisk nytte (WBS 6.3)

## Hva WBS 6.3 gjør

- Aktiviteten oversetter eksisterende modellfunn fra WBS 5.3, 5.4, 6.1 og 6.2 til praktisk beslutningsstøtte for Dagligvare.
- WBS 6.3 trener ikke modeller på nytt, lager ikke nye prognoser og beregner ikke nye evalueringsmetrikker.
- Leveransen er semi-kvantitativ: den bruker eksisterende nøkkeltall og segmentmønstre til å si hvordan modellene kan brukes, men uten kroner, lageroptimalisering eller bemanningsalgoritmer.

## Praktisk nytte per beslutningsområde

- **Innkjøp og lager:** `tuned RF` er standardvalget når nivåtreff prioriteres, fordi Samlet RMSE=578.259649, 11/12 vinnermåneder på RMSE og 13/14 vinnersegmenter på RMSE.
- **Kampanje og rabatt:** `tuned RF` brukes som hovedmodell, men prosentfeilen må kontrolleres særskilt, fordi Discount er toppsignal i 5.4 (11.4781 %), tuned RF vinner RMSE ved høy rabatt, mens baseline RF vinner MAPE i segmentet.
- **Bemanning og ressursplanlegging:** `tuned RF` kan støtte aggregert kapasitetsplanlegging, fordi Tuned RF vinner RMSE i alle fire kvartaler og 11/12 måneder, mens benchmark lineær er best i segmentet hoyt salg.
- **Ledelsesrapportering:** `tuned RF` bør være hovedprognosen i rapportering oppover, mens `benchmark lineær` brukes som forklaringsstøtte, fordi Tuned RF er rang 1 på både RMSE og MAPE samlet, mens benchmark lineær har tolkbarhet_niva=høy.

## Anbefalt bruk av modellene

- `tuned RF` bør være standardprognose i Dagligvare når absolutte avvik og stabilitet gjennom året er viktigst.
- `baseline RF` beholdes som kontrollmodell når prosentfeil i høyrabatt-situasjoner er særlig viktig å følge opp.
- `benchmark lineær` bør brukes når forklaringsbehovet er viktigere enn maksimal prognosepresisjon. I denne situasjonen anbefales `Bruk tuned RF for selve prognosetallet, men benchmark lineær for å forklare retningen i sentrale signaler uten å hevde kausalitet.`
- Ved svært høyt salgsnivå bør tuned RF sammenlignes med benchmark lineær før prognosen brukes som grunnlag for mer pressede planbeslutninger.

## Viktige forbehold

- WBS 6.3 vurderer praktisk nytte innenfor prosjektets faktiske scope og er ikke en operativ beslutningsmodell for lager eller bemanning.
- Rabatt- og regionsignaler er prediktive og ikke kausale, så de kan ikke brukes som bevis for hvorfor salget endrer seg.
- Generaliserbarheten er fortsatt begrenset til ett datasett og én simulert virksomhet, slik WBS 6.2 allerede har dokumentert.

## Produserte artefakter

- `tab_beslutningsmatrise_6_3.csv`
- `tab_bruksregler_6_3.csv`
- `praktisk_nytte.md`

## Avgrensning mot videre rapportarbeid

- WBS 6.3 dokumenterer hvordan dagens modellfunn kan brukes i praksis for Dagligvare.
- Full rapportferdigstilling, mer helhetlig konklusjon og videre strukturarbeid ligger fortsatt i WBS 7.x og 8.x.
