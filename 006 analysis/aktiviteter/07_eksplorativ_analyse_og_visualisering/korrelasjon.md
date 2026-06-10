# Korrelasjonsanalyse av numeriske variabler (Figur 8.3)

## Datagrunnlag

- Input: `06_datasplitt/X_train.csv` + `06_datasplitt/y_train.csv` (treningsdata 2022–2024)
- Antall observasjoner: 6682
- Variabler (9): `Sales`, `Discount`, `year`, `quarter`, `month`, `weekofyear`, `dayofweek`, `dayofmonth`, `is_weekend`
- One-hot-kodede kategorier er holdt utenfor (binære variabler gir misvisende Pearson-korrelasjon).

## Hovedfunn

- Salget har tilnærmet null lineær korrelasjon med samtlige numeriske prediktorer. Sterkeste (i tallverdi) er `Discount` (-0.02), svakeste er `year` (0.00); ingen overstiger 0.02 i tallverdi.
- Blant prediktorene er kalendervariablene sterkt innbyrdes korrelert, sterkest `month` mot `weekofyear` (0.98). Dette er en mekanisk multikollinearitet fordi `quarter`, `month` og `weekofyear` koder samme kalender på ulik oppløsning.

## Betydning for tolkningen (jf. §9.3)

- Den nær fraværende lineære koblingen mellom de numeriske prediktorene og salget understøtter at en stor andel av variasjonen er irreduserbart støygulv som ingen modellklasse kan forklare bort med de tilgjengelige variablene.
- At ingen enkelt numerisk variabel bærer en sterk bivariat sammenheng med salget, er konsistent med at modellene møter det samme feilgulvet og dermed lander tett på hverandre på de samlede metrikkene.
- Den sterke innbyrdes korrelasjonen mellom kalendervariablene er en multikollinearitet som svekker tolkbarheten av enkeltkoeffisienter i den lineære modellen (jf. forutsetningene i kap. 3.1 og begrensningene i §9.5), men som angår variabler som uansett bærer lite salgssignal her.
