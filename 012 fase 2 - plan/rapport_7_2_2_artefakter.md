# Artefakter fra WBS 7.2.2 – Case- og datakapitlets figurer og tabeller

Opprettet: 2026-04-19 (WBS 7.2.2)

Denne filen er leveransen fra WBS 7.2.2 og inneholder ferdige figur- og tabellblokker for kapittel 4 og kapittel 5 i [rapport.md](../005%20report/rapport.md), klare til innsetting i WBS 7.2.4. Utvalget følger [rapport_fig_tab_utvalg.md](rapport_fig_tab_utvalg.md). Alle artefakter er egenproduserte og skal ikke ha kildehenvisning i figur- eller tabellteksten.

## 1 Status for kapittel 4 – Casebeskrivelse

Figur 4.1, 4.2 og 4.3 ligger allerede i [rapport.md](../005%20report/rapport.md) § 4.1, § 4.2 og § 4.3 med korrekt HTML-mønster, sentrert kursiv figurtekst og relativ sti til PNG-ene under [07_eksplorativ_analyse_og_visualisering](../006%20analysis/aktiviteter/07_eksplorativ_analyse_og_visualisering/). Ingen endringer kreves i 7.2.2. Kapittel 4 har ingen tabeller i utvalget.

| Nr | Kildefil | Tilstand i rapporten |
|---|---|---|
| Figur 4.1 | [fig_sales_per_category.png](../006%20analysis/aktiviteter/07_eksplorativ_analyse_og_visualisering/fig_sales_per_category.png) | På plass i § 4.1 |
| Figur 4.2 | [fig_sales_over_tid_train_test.png](../006%20analysis/aktiviteter/07_eksplorativ_analyse_og_visualisering/fig_sales_over_tid_train_test.png) | På plass i § 4.2 |
| Figur 4.3 | [fig_sales_per_month_split.png](../006%20analysis/aktiviteter/07_eksplorativ_analyse_og_visualisering/fig_sales_per_month_split.png) | På plass i § 4.3 |

## 2 Kapittel 5 – Metode og data

Splittabellen ligger allerede i [rapport.md](../005%20report/rapport.md) § 5.2 og beholdes uendret bortsett fra nummer: etter V1 i helhetsreviewen av 7.2 er den renummerert fra Tabell 5.1 til **Tabell 5.5** slik at tekstrekkefølgen matcher formkrav 1. De fem øvrige artefaktene (Figur 5.1, Figur 5.2, Tabell 5.2, Tabell 5.3 og Tabell 5.4) er nye for rapporten og leveres som ferdige blokker under.

### 2.1 Figur 5.1 – Fordeling av datatyper

Plasseres tidlig i § 5.2 Data, før omtalen av variabelutvalget. HTML-blokk klar for innsetting:

```html
<div align="center">
  <img src="../006 analysis/aktiviteter/01_dataforstaelse_og_variabler/fig_datatype_fordeling.png" alt="Fordeling av datatyper i rådatasettet" width="80%">
  <p align="center"><small><i>Figur 5.1 Fordeling av datatyper i rådatasettet. Fordelingen viser hvor mange kolonner som er numeriske, kategoriske og datobaserte, og underbygger valg av forbehandling og feature engineering.</i></small></p>
</div>
```

### 2.2 Figur 5.2 – Fordeling av daglige salgsverdier

Plasseres i § 5.2 etter Figur 5.1 og før omtalen av datasplitten. HTML-blokk klar for innsetting:

```html
<div align="center">
  <img src="../006 analysis/aktiviteter/07_eksplorativ_analyse_og_visualisering/fig_sales_fordeling_train_test.png" alt="Fordeling av daglige salgsverdier i trenings- og testperioden" width="80%">
  <p align="center"><small><i>Figur 5.2 Fordeling av daglige salgsverdier i trenings- og testperioden. Overlappet i fordelingene tyder på at målvariabelen er stabil mellom periodene.</i></small></p>
</div>
```

### 2.3 Tabell 5.2 – Variabeloversikt

Kilde: [tab_relevante_variabler.csv](../006%20analysis/aktiviteter/02_identifisere_relevante_variabler/tab_relevante_variabler.csv) (11 datarader). Plasseres i § 5.2 etter Figur 5.1 som oversikt over de 11 kolonnene i rådatasettet. Tabellblokk klar for innsetting:

| Variabel | Datatype | Manglende % | Unike | Anbefaling | Begrunnelse |
| --- | --- | --- | --- | --- | --- |
| Sales | int64 | 0,0 | 1 989 | target | Målvariabel for prognose. |
| Category | str | 0,0 | 7 | inkluder | Kategorisk variabel med håndterbar kardinalitet. |
| City | str | 0,0 | 24 | inkluder | Kategorisk variabel med håndterbar kardinalitet. |
| Discount | float64 | 0,0 | 26 | inkluder | Numerisk variabel egner seg direkte for modellering. |
| Region | str | 0,0 | 5 | inkluder | Kategorisk variabel med håndterbar kardinalitet. |
| State | str | 0,0 | 1 | inkluder | Kategorisk variabel med håndterbar kardinalitet. |
| Sub Category | str | 0,0 | 23 | inkluder | Kategorisk variabel med håndterbar kardinalitet. |
| Order Date | str | 0,0 | 1 236 | vurder | Middels/høy kardinalitet, vurder koding og nytte. |
| Profit | float64 | 0,0 | 8 380 | vurder | Kan være informativ, men bør sjekkes for lekkasje før modellering. |
| Customer Name | str | 0,0 | 50 | ekskluder | Navn-kolonne har høy kardinalitet og høy risiko for overtilpasning. |
| Order ID | str | 0,0 | 9 994 | ekskluder | ID-variabel gir vanligvis lite generaliserbar prediksjonsverdi. |

<p align="center"><small><i>Tabell 5.2 Variabeloversikt med datatype, manglende andel og anbefaling for videre bruk.</i></small></p>

*Merk:* Kilden lister 12 rader fordi `Sales` er telt med både som variabel og som målvariabel. Tabellen over gjengir de 11 unike variablene i datasettet; `Sales` står øverst som målvariabel. Full variabelliste ligger i kildefilen.

### 2.4 Tabell 5.3 – Feature engineering-oppsett

Kilde: [tab_featurevalg.csv](../006%20analysis/aktiviteter/05_feature_engineering/tab_featurevalg.csv) (18 rader). Plasseres i § 5.2 etter Tabell 5.2. Tabellblokk klar for innsetting:

| Input-kolonne | Handling | Output-kolonne | Begrunnelse |
| --- | --- | --- | --- |
| Sales | behold | Sales | Målvariabel for prognose. |
| Discount | behold | Discount | Numerisk forklaringsvariabel. |
| Category | behold | Category | Kategorisk feature med håndterbar kardinalitet. |
| Sub Category | behold | Sub Category | Kategorisk feature med håndterbar kardinalitet. |
| City | behold | City | Kategorisk feature med håndterbar kardinalitet. |
| Region | behold | Region | Kategorisk feature med håndterbar kardinalitet. |
| Order Date | behold | Order Date | Beholdes for sporbarhet og tidsbasert splitt. |
| Order Date | transformer | year | Utledet kalenderår etter remapping. |
| Order Date | transformer | month | Utledet måned. |
| Order Date | transformer | quarter | Utledet kvartal. |
| Order Date | transformer | weekofyear | Utledet uke i året. |
| Order Date | transformer | dayofweek | Utledet ukedag. |
| Order Date | transformer | dayofmonth | Utledet dag i måneden. |
| Order Date | transformer | is_weekend | Indikator for helg. |
| Order ID | ekskluder | – | ID-kolonne uten generaliserbar prediksjonsverdi. |
| Customer Name | ekskluder | – | Navn-kolonne med høy risiko for overtilpasning. |
| Profit | ekskluder | – | Ekskludert som potensiell lekkasjevariabel. |
| State | ekskluder | – | Kolonnen er konstant i datasettet og gir ingen forklaringskraft. |

<p align="center"><small><i>Tabell 5.3 Feature engineering-oppsett: input-kolonne, handling og resulterende output-kolonne med begrunnelse.</i></small></p>

### 2.5 Tabell 5.4 – Datarensing

Kilde: [tab_renselogg.csv](../006%20analysis/aktiviteter/04_dataprosessering/tab_renselogg.csv) (19 rader). Plasseres i § 5.2 etter Tabell 5.3. Tabellblokk klar for innsetting:

| Målepunkt | Verdi | Kommentar |
| --- | --- | --- |
| antall_rader_inn | 9 994 | Observasjoner i rådata |
| antall_kolonner_inn | 11 | Variabler i rådata |
| manglende_verdier_inn | 0 | Totalt manglende i rådata |
| dubletter_inn | 0 | Eksakte dublettrader i rådata |
| datoformat_dd_mm_yyyy | 4 042 | Tolket fra verdier med bindestrek |
| datoformat_mm_dd_yyyy | 5 952 | Tolket fra verdier med skråstrek |
| datoformat_annet | 0 | Verdier uten kjent mønster |
| ugyldige_datoer_etter_tolkning | 0 | Datoer som ikke lot seg parse |
| opprinnelig_periode_start | 2015-01-02 | Tidligste dato i original dataserie |
| opprinnelig_periode_slutt | 2018-12-30 | Siste dato i original dataserie |
| år_forskyvning | 7 | Kalenderforskyvning brukt for prosjektets arbeidsgrunnlag |
| prosjekt_periode_start | 2022-01-02 | Tidligste dato etter remapping |
| prosjekt_periode_slutt | 2025-12-30 | Siste dato etter remapping |
| rader_fjernet_manglende_kritisk_felt | 0 | Rader fjernet etter kontroll av dato og numeriske nøkkelfelt |
| dubletter_fjernet | 0 | Fjernet etter standardisering |
| antall_rader_ut | 9 994 | Observasjoner i renset datasett |
| manglende_verdier_ut | 0 | Totalt manglende etter rens |
| dubletter_ut | 0 | Eksakte dublettrader etter rens |

<p align="center"><small><i>Tabell 5.4 Datarensing – målepunkter, verdier og kommentarer som dokumenterer kvalitetskontrollen før modellering.</i></small></p>

## 3 Innsettingsrekkefølge i § 5.2 for 7.2.4

Rekkefølgen som 7.2.4 skal bruke når blokkene settes inn i [rapport.md](../005%20report/rapport.md) § 5.2 Data:

1. Figur 5.1 (tidlig i § 5.2, etter strukturbeskrivelsen).
2. Tabell 5.2 (etter Figur 5.1, før omtalen av feature engineering).
3. Tabell 5.3 (etter Tabell 5.2, som bindeledd mellom variabler og modelldata).
4. Tabell 5.4 (etter Tabell 5.3, oppsummerer datarensingen).
5. Figur 5.2 (etter Tabell 5.4 og før splittabellen om datasplitt).
6. Tabell 5.5 (splittabellen, renummerert fra tidligere Tabell 5.1 etter V1 i helhetsreviewen) beholdes som siste blokk i § 5.2.

## 4 Leveransebekreftelse

- Figur 4.1–4.3 er verifisert uendret og korrekt plassert i [rapport.md](../005%20report/rapport.md).
- Figur 5.1 og Figur 5.2 er klare som HTML-blokker med relativ sti til eksisterende PNG-er.
- Tabell 5.2 (11 unike variabler + målvariabel), Tabell 5.3 (18 rader) og Tabell 5.4 (18 innholdsrader + 1 periodisering) er skrevet ut som ferdige Markdown-tabeller med sentrert kursiv tabelltittel.
- Alle norske tegn `æ`, `ø`, `å` er bevart; ingen BOM; filen er ren UTF-8.
- Ingen endringer er gjort i [rapport.md](../005%20report/rapport.md); innsetting tilhører WBS 7.2.4.
