# Artefakter fra WBS 7.2.3 – Analyse-, resultat- og diskusjonsfigurer og -tabeller

Opprettet: 2026-04-19 (WBS 7.2.3)

Denne filen er leveransen fra WBS 7.2.3 og inneholder ferdige figur- og tabellblokker for kapittel 6 (Modellering), 7 (Analyse), 8 (Resultat) og 9 (Diskusjon) i [rapport.md](../005%20report/rapport.md), klare til innsetting i WBS 7.2.4. Utvalget følger [rapport_fig_tab_utvalg.md](rapport_fig_tab_utvalg.md). Alle figurer og tabeller er egenproduserte og skal ikke ha kildehenvisning i figur- eller tabellteksten.

## 1 Kapittel 6 – Modellering

### 1.1 Tabell 6.1 – Oversikt over modellsporene

Kilder: [tab_lr_modelloversikt.csv](../006%20analysis/aktiviteter/08_lineaer_regresjon/tab_lr_modelloversikt.csv), [tab_rf_modelloversikt.csv](../006%20analysis/aktiviteter/09_random_forest_regressor/tab_rf_modelloversikt.csv), [tab_rf_tuned_modelloversikt.csv](../006%20analysis/aktiviteter/11_parameterjustering_random_forest/tab_rf_tuned_modelloversikt.csv). Plasseres tidlig i kap. 6.

| Modellrolle | Algoritme | Treningsrader | Features | Sentrale hyperparametre | Rolle i prosjektet |
| --- | --- | --- | --- | --- | --- |
| benchmark lineær | LinearRegression | 6 682 | 67 | `fit_intercept=True`, ingen regularisering | Tolkbar benchmark med eksplisitt koeffisientretning. |
| baseline RF | RandomForestRegressor | 6 682 | 67 | `n_estimators=200`, `max_depth=None`, `min_samples_leaf=1`, `max_features=1.0` | RF-referanse uten tuning, for stabilitetssjekk mot tunet modell. |
| tuned RF | RandomForestRegressor | 6 682 | 67 | `n_estimators=400`, `max_depth=10`, `min_samples_leaf=4`, `max_features="sqrt"` | Anbefalt operativ modell etter tuning på 2024-validering. |

<p align="center"><small><i>Tabell 6.1 Oversikt over de tre modellsporene: antall features, treningsrader, sentrale hyperparametre og rolle i prosjektet.</i></small></p>

### 1.2 Tabell 6.2 – Topp 5 tuningkandidater for Random Forest

Kilder: [tab_rf_tuning_kandidater.csv](../006%20analysis/aktiviteter/11_parameterjustering_random_forest/tab_rf_tuning_kandidater.csv) (topp 5 etter `rang_rmse`) og [tab_rf_tuning_vinner.csv](../006%20analysis/aktiviteter/11_parameterjustering_random_forest/tab_rf_tuning_vinner.csv). Baseline i 2024-validering: `RMSE=590,30`, `MAPE=44,22 %`.

| Kandidat | n_estimators | max_depth | min_samples_leaf | max_features | RMSE validering | MAPE validering (%) | Delta RMSE vs. baseline |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rf_tune_30 (vinner) | 400 | 10 | 4 | sqrt | 577,27 | 43,56 | −13,04 |
| rf_tune_28 | 400 | 10 | 2 | sqrt | 577,29 | 43,57 | −13,02 |
| rf_tune_10 | 200 | 10 | 2 | sqrt | 577,36 | 43,58 | −12,94 |
| rf_tune_26 | 400 | 10 | 1 | sqrt | 577,65 | 43,60 | −12,65 |
| rf_tune_12 | 200 | 10 | 4 | sqrt | 577,81 | 43,61 | −12,50 |

<p align="center"><small><i>Tabell 6.2 Topp 5 parameterkombinasjoner fra tuning av Random Forest, sortert etter RMSE på 2024-valideringen.</i></small></p>

## 2 Kapittel 7 – Analyse

### 2.1 Tabell 7.1 – Månedlig RMSE og MAPE per modell

Kilde: [tab_rmse_mape_maaned.csv](../006%20analysis/aktiviteter/13_rmse_og_mape/tab_rmse_mape_maaned.csv), pivotert til én rad per måned. Plasseres først i kap. 7, før figurene.

| Måned | RMSE lineær | RMSE baseline RF | RMSE tuned RF | MAPE lineær (%) | MAPE baseline RF (%) | MAPE tuned RF (%) |
| --- | --- | --- | --- | --- | --- | --- |
| 2025-01 | 586,09 | 597,82 | 585,73 | 46,62 | 46,51 | 46,52 |
| 2025-02 | 577,96 | 584,01 | 576,74 | 42,50 | 42,19 | 42,72 |
| 2025-03 | 552,52 | 565,11 | 550,33 | 42,14 | 42,86 | 42,30 |
| 2025-04 | 581,28 | 576,18 | 575,63 | 44,76 | 43,04 | 43,85 |
| 2025-05 | 591,70 | 594,57 | 589,74 | 45,46 | 44,36 | 45,00 |
| 2025-06 | 560,16 | 556,89 | 552,25 | 43,81 | 41,87 | 42,79 |
| 2025-07 | 569,61 | 582,87 | 569,23 | 42,90 | 42,67 | 42,33 |
| 2025-08 | 586,60 | 601,17 | 586,65 | 42,19 | 42,38 | 41,71 |
| 2025-09 | 582,61 | 591,60 | 581,47 | 42,41 | 42,86 | 42,36 |
| 2025-10 | 593,34 | 615,05 | 593,09 | 43,96 | 45,70 | 44,16 |
| 2025-11 | 597,86 | 600,90 | 595,25 | 47,87 | 47,46 | 47,78 |
| 2025-12 | 577,66 | 593,86 | 574,66 | 45,10 | 45,93 | 45,16 |

<p align="center"><small><i>Tabell 7.1 Månedlig RMSE og MAPE per modell i 2025.</i></small></p>

### 2.2 Figur 7.1 – Månedlig bias per modell

Plasseres etter Tabell 7.1 og før Figur 7.2. HTML-blokk klar for innsetting:

```html
<div align="center">
  <img src="../006 analysis/aktiviteter/16_tolke_modellresultater/fig_bias_maaned_modell.png" alt="Månedlig bias per modell i 2025" width="80%">
  <p align="center"><small><i>Figur 7.1 Månedlig bias per modell i 2025. Positive verdier betyr at modellen overestimerer salget, negative at den underestimerer. Kurven viser at alle tre modellene underestimerer i august–september.</i></small></p>
</div>
```

### 2.3 Figur 7.2 – Månedlig RMSE per modell

Plasseres etter Figur 7.1. HTML-blokk klar for innsetting:

```html
<div align="center">
  <img src="../006 analysis/aktiviteter/13_rmse_og_mape/fig_rmse_maaned_modell.png" alt="Månedlig RMSE per modell i 2025" width="80%">
  <p align="center"><small><i>Figur 7.2 Månedlig RMSE per modell i 2025. Tuned Random Forest har lavest RMSE i majoriteten av månedene, mens benchmark lineær slår gjennom i enkeltmåneder.</i></small></p>
</div>
```

### 2.4 Tabell 7.2 – RMSE og MAPE per segment

Kilder: [tab_segmentmetrikk_modell.csv](../006%20analysis/aktiviteter/16_tolke_modellresultater/tab_segmentmetrikk_modell.csv) og [tab_segmentdefinisjoner.csv](../006%20analysis/aktiviteter/16_tolke_modellresultater/tab_segmentdefinisjoner.csv). Plasseres etter Figur 7.2. Alle 14 segmenter fra fire segmentdimensjoner er inkludert.

| Dimensjon | Verdi | RMSE lineær | RMSE baseline RF | RMSE tuned RF | MAPE lineær (%) | MAPE baseline RF (%) | MAPE tuned RF (%) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Kvartal | 1 | 570,43 | 580,73 | 569,10 | 43,58 | 43,73 | 43,67 |
| Kvartal | 2 | 578,10 | 576,41 | 573,05 | 44,69 | 43,11 | 43,90 |
| Kvartal | 3 | 580,18 | 591,95 | 579,59 | 42,48 | 42,67 | 42,17 |
| Kvartal | 4 | 589,94 | 602,59 | 587,87 | 45,85 | 46,46 | 45,89 |
| Rabattbånd | lav | 583,01 | 598,95 | 581,12 | 46,66 | 46,93 | 46,14 |
| Rabattbånd | middels | 577,89 | 587,10 | 577,11 | 44,51 | 44,63 | 44,37 |
| Rabattbånd | høy | 581,41 | 586,74 | 577,96 | 42,76 | 42,36 | 42,62 |
| Region | Central | 585,83 | 595,13 | 584,92 | 44,36 | 44,49 | 44,39 |
| Region | East | 579,39 | 587,92 | 575,30 | 44,19 | 44,26 | 43,86 |
| Region | South | 587,59 | 599,43 | 587,02 | 45,48 | 45,29 | 45,03 |
| Region | West | 573,90 | 581,36 | 571,78 | 43,44 | 43,18 | 43,27 |
| Salgsbånd | lavt salg | 695,06 | 694,19 | 690,44 | 90,79 | 89,39 | 90,27 |
| Salgsbånd | middels salg | 196,79 | 224,70 | 192,51 | 11,40 | 12,30 | 11,20 |
| Salgsbånd | høyt salg | 699,10 | 713,73 | 699,57 | 30,31 | 30,60 | 30,39 |

<p align="center"><small><i>Tabell 7.2 RMSE og MAPE per modell i utvalgte segmenter (kvartal, rabattbånd, region, salgsbånd). Segmentinndelingen er definert ut fra dataene og gir et bilde av hvor prognosene er stabile.</i></small></p>

## 3 Kapittel 8 – Resultat

### 3.1 Figur 8.1 – Samlet RMSE og MAPE

Kilde: [tab_rmse_mape_oversikt.csv](../006%20analysis/aktiviteter/13_rmse_og_mape/tab_rmse_mape_oversikt.csv). Plasseres etter Tabell 8.1. HTML-blokk klar for innsetting:

```html
<div align="center">
  <img src="../006 analysis/aktiviteter/13_rmse_og_mape/fig_rmse_mape_samlet.png" alt="Samlet RMSE og MAPE for 2025" width="80%">
  <p align="center"><small><i>Figur 8.1 Samlet RMSE og MAPE for benchmark lineær, Random Forest baseline og tuned Random Forest i 2025. Tuned Random Forest har lavest RMSE, mens MAPE er tettere fordelt mellom modellene.</i></small></p>
</div>
```

### 3.2 Figur 8.2 – Topp 10 feature importance

Plasseres etter Tabell 8.3. HTML-blokk klar for innsetting:

```html
<div align="center">
  <img src="../006 analysis/aktiviteter/15_viktige_variabler/fig_feature_importance_tuned_top10.png" alt="Topp 10 feature importance for tuned Random Forest" width="80%">
  <p align="center"><small><i>Figur 8.2 Topp 10 feature importance for tuned Random Forest. Variablene er rangert etter normalisert viktighet og viser hvilke signaler modellen faktisk vektlegger.</i></small></p>
</div>
```

### 3.3 Figur 8.3 – Variabelgrupper i topp 10

Plasseres etter Figur 8.2. HTML-blokk klar for innsetting:

```html
<div align="center">
  <img src="../006 analysis/aktiviteter/15_viktige_variabler/fig_variabelgrupper_tuned_top10.png" alt="Variabelgrupper i topp 10 for tuned Random Forest" width="80%">
  <p align="center"><small><i>Figur 8.3 Samlet feature importance per variabelgruppe i topp 10 for tuned Random Forest. Figuren oppsummerer hvilke grupper av signaler (kalender, pris/kampanje, region) som dominerer modellens prediksjon.</i></small></p>
</div>
```

## 4 Kapittel 9 – Diskusjon

### 4.1 Tabell 9.1 – Modellprofil

Kilde: [tab_modellprofil_6_2.csv](../006%20analysis/aktiviteter/17_styrker_og_svakheter/tab_modellprofil_6_2.csv). Plasseres i § 9.1 Tolkning av hovedfunn.

| Modellrolle | RMSE 2025 | MAPE 2025 (%) | RMSE-vinnermåneder | MAPE-vinnermåneder | RMSE-vinnersegmenter | MAPE-vinnersegmenter | Tolkbarhet | Hovedstyrke | Hovedsvakhet |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| benchmark lineær | 580,39 | 44,18 | 1 | 3 | 1 | 4 | høy | Høy tolkbarhet og konkurransedyktig i enkelte segmenter. | Multikollinearitet og manglende regularisering svekker robust koeffisienttolkning. |
| baseline RF | 589,28 | 44,12 | 0 | 6 | 0 | 4 | middels | Sterk lokal MAPE-ytelse og nyttig RF-sammenligningspunkt. | Svakest samlet og uten RMSE-seire i måneder eller segmenter. |
| tuned RF | 578,26 | 43,97 | 11 | 3 | 13 | 6 | middels | Best samlet 2025 og sterkest på absolutt feil. | MAPE er mer ujevn enn RMSE mellom måneder og segmenter. |

<p align="center"><small><i>Tabell 9.1 Modellprofil med samlet RMSE/MAPE, antall vinnermåneder og -segmenter, tolkbarhetsnivå samt hovedstyrke og hovedsvakhet per modell.</i></small></p>

### 4.2 Tabell 9.2 – Beslutningsmatrise og bruksregler

Kilder: [tab_beslutningsmatrise_6_3.csv](../006%20analysis/aktiviteter/18_vurdere_praktisk_nytte/tab_beslutningsmatrise_6_3.csv) og [tab_bruksregler_6_3.csv](../006%20analysis/aktiviteter/18_vurdere_praktisk_nytte/tab_bruksregler_6_3.csv). Plasseres i § 9.3 Praktisk nytte for Dagligvare.

| Beslutningsområde | Anbefalt modell | Prioritert metrikk | Praktisk nytte | Hovedforbehold |
| --- | --- | --- | --- | --- |
| Innkjøp og lager | tuned RF | RMSE | høy | Ikke lageroptimalisering; prosentfeil kan være ujevn i delsegmenter. |
| Kampanje og rabatt | tuned RF, med baseline RF som MAPE-kontroll ved høy rabatt | RMSE med MAPE-kontroll | middels | Rabattsignalene er prediktive, ikke kausale. |
| Bemanning og ressursplanlegging | tuned RF, med benchmark lineær-kontroll ved svært høyt salgsnivå | RMSE | middels–høy | Ikke butikk- eller skiftoptimalisering; toppbelastning krever ekstra varsomhet. |
| Ledelsesrapportering | tuned RF som hovedprognose, benchmark lineær som forklaringsstøtte | RMSE med forklaringsstøtte | middels | Lineær modell skal ikke brukes som kausalt bevis for salgsendringer. |

<p align="center"><small><i>Tabell 9.2 Beslutningsmatrise og bruksregler: beslutningsområder, anbefalt modellrolle, prioritert metrikk, praktisk nyttegrad og hovedforbehold.</i></small></p>

### 4.3 Tabell 9.3 – Metodiske begrensninger

Kilde: [tab_metodebegrensninger_6_2.csv](../006%20analysis/aktiviteter/17_styrker_og_svakheter/tab_metodebegrensninger_6_2.csv). Plasseres i § 9.4 Metodiske begrensninger. ID-kolonnen (`MB-6.2-01`–`MB-6.2-06`) droppes i rapport-versjonen etter F4 i helhetsreviewen for å bedre lesbarheten; kildefilen beholder IDs uendret for intern sporbarhet.

| Tema | Beskrivelse | Konsekvens for pålitelighet | Konsekvens for generaliserbarhet |
| --- | --- | --- | --- |
| representativitet | Prosjektet bygger på én simulert virksomhet og ett datasett, ikke flere virksomheter eller markeder. | Påliteligheten innenfor dette caset kan fortsatt være god, men robustheten mot andre kontekster er ikke testet. | Funnene kan ikke uten videre overføres til andre bedrifter, regioner eller produktmixer. |
| eksterne faktorer | Eksterne makroøkonomiske forhold som inflasjon, rente og konjunkturer er ikke modellert. | Prognosene kan være mindre robuste hvis 2025 påvirkes av forhold som ikke finnes i feature-settet. | Resultatene generaliserer dårligere til perioder der eksterne sjokk spiller en større rolle. |
| modellomfang | Prosjektet sammenligner bare lineær regresjon og Random Forest, ikke andre modellfamilier. | Valgt modell er best i dette prosjektets kandidatfelt, men ikke nødvendigvis best mulig totalt sett. | Det er begrenset grunnlag for å generalisere at samme modellfamilie vil være best i andre lignende problemer. |
| koeffisienttolkning | Lineær regresjon er kjørt uten regularisering, og dummykoding kan gi multikollinearitet i koeffisientene. | Dette svekker påliteligheten i sterke fortolkninger av enkeltkoeffisienter som om de var stabile effektmål. | Koeffisientmønstre kan endre seg når datastruktur eller kategorifordeling endres i andre case. |
| valideringsvindu | Tuning av Random Forest bruker kun 2024 som intern valideringsperiode. | Modellvalget er etterprøvbart, men sensitivitet for andre valideringsvinduer er ikke undersøkt. | Det gir mindre grunnlag for å generalisere tuningvalgene til andre tidsperioder eller sesongmønstre. |
| kausalitet | Analysen er prediktiv og ikke kausal, slik at viktige variabler ikke kan tolkes som dokumenterte årsaker til salg. | Det er mer pålitelig å bruke funnene som prognosestøtte enn som bevis for årsakssammenhenger. | Beslutninger som krever kausal innsikt kan ikke generaliseres direkte fra disse prediktive mønstrene. |

<p align="center"><small><i>Tabell 9.3 Metodiske begrensninger i studien, med tematisk kategori, beskrivelse og konsekvens for pålitelighet og generaliserbarhet.</i></small></p>

## 5 Innsettingsrekkefølge for 7.2.4

Rekkefølgen som 7.2.4 skal bruke når blokkene settes inn i [rapport.md](../005%20report/rapport.md):

- **Kap. 6 Modellering**: Tabell 6.1 → Tabell 6.2.
- **Kap. 7 Analyse**: Tabell 7.1 → Figur 7.1 → Figur 7.2 → Tabell 7.2.
- **Kap. 8 Resultat**: Tabell 8.1 (beholdes fra før) → Figur 8.1 → Tabell 8.2 (beholdes) → Tabell 8.3 (beholdes) → Figur 8.2 → Figur 8.3 → Tabell 8.4 (beholdes).
- **Kap. 9 Diskusjon**: Tabell 9.1 i § 9.1, Tabell 9.2 i § 9.3 (beslutningsmatrise), Tabell 9.3 i § 9.4 (metodebegrensninger). Rekkefølgen ble renummerert etter V1 i helhetsreviewen slik at tekstrekkefølgen matcher nummereringen.

## 6 Leveransebekreftelse

- Fem nye PNG-filer produsert og verifisert på disk:
  - [fig_bias_maaned_modell.png](../006%20analysis/aktiviteter/16_tolke_modellresultater/fig_bias_maaned_modell.png)
  - [fig_rmse_maaned_modell.png](../006%20analysis/aktiviteter/13_rmse_og_mape/fig_rmse_maaned_modell.png)
  - [fig_rmse_mape_samlet.png](../006%20analysis/aktiviteter/13_rmse_og_mape/fig_rmse_mape_samlet.png)
  - [fig_feature_importance_tuned_top10.png](../006%20analysis/aktiviteter/15_viktige_variabler/fig_feature_importance_tuned_top10.png)
  - [fig_variabelgrupper_tuned_top10.png](../006%20analysis/aktiviteter/15_viktige_variabler/fig_variabelgrupper_tuned_top10.png)
- Syv nye Markdown-tabeller (Tabell 6.1, 6.2, 7.1, 7.2, 9.1, 9.2, 9.3) er skrevet ut med sentrert kursiv tabelltittel og norske kolonnenavn.
- Skriptene [start_wbs_5_2.py](../006%20analysis/aktiviteter/13_rmse_og_mape/start_wbs_5_2.py), [start_wbs_5_4.py](../006%20analysis/aktiviteter/15_viktige_variabler/start_wbs_5_4.py) og [start_wbs_6_1.py](../006%20analysis/aktiviteter/16_tolke_modellresultater/start_wbs_6_1.py) er utvidet med plotteblokker og kjørt ende-til-ende via `uv run` uten feil.
- Norske tegn `æ`, `ø`, `å` er bevart; ingen BOM; filen er ren UTF-8.
- Ingen endringer er gjort i [rapport.md](../005%20report/rapport.md); innsetting tilhører WBS 7.2.4.
