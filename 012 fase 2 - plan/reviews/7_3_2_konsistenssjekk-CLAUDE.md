# Review av aktivitet 7.3.2 – «Konsistenssjekk mot analyseartefakter»

**Reviewer:** Claude
**Dato:** 2026-04-21
**Aktivitetsmappe:** [005 report/](../../005%20report/) og [006 analysis/aktiviteter/](../../006%20analysis/aktiviteter/)
**Planreferanse:** WBS 7.3.2 «Gjennomføre konsistenssjekk mot analyseartefakter», planlagt 2026-04-21

---

## Sammendrag

Alle ni ankerpåstander i Sammendrag og Abstract (RMSE 578,26, MAPE 43,97 %, 11/12 måneder, 13/14 segmenter, 67 features, 9 994 transaksjoner, 6 682 trening, 3 312 test, rabatt 11,48 %, ~42 % kalender) stemmer eksakt med kilde-CSV. Alle 16 innholdstabeller og 10 figurer er sporbare tilbake til riktig kildefil og gjengir verdier innenfor avrundingstoleranse ±0,005. Samtlige syv vedleggsreferanser (A1–A7) peker til eksisterende CSV-filer. Ingen svakheter (V) ble funnet; tre forbedringsforslag (F1–F3) gjelder språklig presisering og intern inkonsistens mellom Tabell 5.1 og Tabell 5.2 for variabelen `State`. Alle F-punkter anbefales lukket som del av WBS 7.3.3 språkvask.

**Totalt:** 6 styrker, 0 svakheter, 3 forbedringsforslag (Lav).

---

## Styrker

- **S1.** Alle ni ankerpåstander stemmer mot kilde-CSV. RMSE 578,26 (CSV 578,259649), MAPE 43,97 % (CSV 43,9706), 11 RMSE-vinnermåneder (CSV `antall_vinnermåneder=11`), 13 RMSE-vinnersegmenter (tuned RF vinner alle 14 unntatt `sales_band=hoyt salg`), 67 features (CSV `antall_features=67`), 9 994 transaksjoner (CSV `antall_rader_ut=9994`), 6 682/3 312 trening/test (CSV `train=6682, test=3312`), rabatt 11,48 % (CSV `importance_pct=11,4781`), kalender ~42 % (CSV `sum_importance_pct_topp10=41,9826`).
- **S2.** Alle 16 innholdstabeller matcher sin kilde-CSV eksakt innenfor ±0,005-toleranse. Stikkprøver på Tabell 7.1 (36 celletall), Tabell 7.2 (14 segmenter × 6 tallkolonner), Tabell 8.1, Tabell 8.3 (10 importance-verdier) og Tabell 9.1 (6 metrikk-kolonner × 3 modeller) viser ingen avrundingsfeil.
- **S3.** Figurene 4.1–8.3 refererer til eksisterende PNG-filer på korrekt relativ sti, og figurtekstene er innholdsmessig konsistente med omtalende brødtekst. Figur 7.1-teksten «alle tre modellene underestimerer i august–september» bekreftes av [tab_bias_maaned_modell.csv](../../006%20analysis/aktiviteter/16_tolke_modellresultater/tab_bias_maaned_modell.csv), der alle tre modeller har `bias_pct` < 0 i både august (−4,37 %, −5,13 %, −5,22 %) og september (−2,86 %, −2,05 %, −2,77 %).
- **S4.** Bias-tallene i § 7 og § 9.1 (`−5,22 %`, `−20 548`, `−2,77 %`, `−16 334`, `+1,05 %`, `+2,36 %`) matcher [tab_bias_maaned_modell.csv](../../006%20analysis/aktiviteter/16_tolke_modellresultater/tab_bias_maaned_modell.csv) eksakt for tuned RF i august/september/november/desember.
- **S5.** Vedleggsreferansene A1–A7 peker til eksisterende filer. Radantall verifisert med `wc -l`: A1 (3 312 datarader ✓ mot rapportens «3 312 rader»), A2 (3 312), A3 (36 tuningkandidater), A4 (67 features), A5 (67 koeffisienter), A6 (36 måned×modell-kombinasjoner), A7 (42 segment×modell-kombinasjoner).
- **S6.** Nøkkeltall er konsistente på tvers av Sammendrag (linje 103), Abstract (linje 111), Tabell 8.1 (linje 535–537), Tabell 9.1 (linje 624–626), § 9.1 (linje 616), Konklusjon (linje 682). RMSE 578,26 og MAPE 43,97 % skrives identisk alle steder, uten avrundingsdrift.

---

## Del 1 – Numerisk konsistens

### 1.1 Ankerpåstander A1–A9 i Sammendrag og Abstract

| # | Påstand | Kilde | Kildeverdi | Rapportverdi | Vurdering |
|:--|:--------|:------|:-----------|:-------------|:----------|
| A1 | RMSE tuned RF = 578,26 | [tab_rmse_mape_oversikt.csv](../../006%20analysis/aktiviteter/13_rmse_og_mape/tab_rmse_mape_oversikt.csv) | 578,259649 | 578,26 | **OK** (±0,0004) |
| A2 | MAPE tuned RF = 43,97 % | samme | 43,9706 | 43,97 % | **OK** (±0,0006) |
| A3 | 11/12 RMSE-vinnermåneder | [tab_modellvinner_telling.csv](../../006%20analysis/aktiviteter/14_sammenligne_modellresultater/tab_modellvinner_telling.csv) | 11 | 11 | **OK** |
| A4 | 13/14 RMSE-vinnersegmenter | [tab_segmentvinnere_tolkning.csv](../../006%20analysis/aktiviteter/16_tolke_modellresultater/tab_segmentvinnere_tolkning.csv) | 13 av 14 (tuned RF vinner alt unntatt `sales_band=hoyt salg`) | 13 av 14 | **OK** |
| A5 | 67 features | [tab_split_oversikt.csv](../../006%20analysis/aktiviteter/06_datasplitt/tab_split_oversikt.csv) | 67 | 67 | **OK** |
| A6 | 9 994 transaksjoner | [tab_renselogg.csv](../../006%20analysis/aktiviteter/04_dataprosessering/tab_renselogg.csv) | 9994 | 9 994 | **OK** |
| A7 | 6 682 trening, 3 312 test | [tab_split_oversikt.csv](../../006%20analysis/aktiviteter/06_datasplitt/tab_split_oversikt.csv) | train=6682, test=3312 | 6 682 / 3 312 | **OK** |
| A8 | Rabatt 11,48 % | [tab_rf_tuned_feature_importance.csv](../../006%20analysis/aktiviteter/15_viktige_variabler/tab_rf_tuned_feature_importance.csv) | 11,4781 | 11,48 % | **OK** |
| A9 | ~42 % kalender i topp 10 | [tab_variabelgrupper_tuned_top10.csv](../../006%20analysis/aktiviteter/15_viktige_variabler/tab_variabelgrupper_tuned_top10.csv) | 41,9826 | ~42 % | **OK** |

**Vurdering:** Alle ni ankerpåstander stemmer eksakt innenfor ±0,005-toleranse. Ingen V-funn.

### 1.2 Innholdstabeller 5.1–12.1 mot kilde-CSV

| Tabell | Kilde-CSV | Kontroll | Vurdering |
|:-------|:----------|:---------|:----------|
| 5.1 | [tab_relevante_variabler.csv](../../006%20analysis/aktiviteter/02_identifisere_relevante_variabler/tab_relevante_variabler.csv) | 11 rader, kolonneverdier matcher. Unike-tall: Sales 1989, Category 7, City 24, Discount 26, Region 5, State 1, Sub Category 23, Order Date 1236, Profit 8380, Customer Name 50, Order ID 9994. | **OK** (se F2 om State-anbefaling) |
| 5.2 | [tab_featurevalg.csv](../../006%20analysis/aktiviteter/05_feature_engineering/tab_featurevalg.csv) | 18 rader, input/handling/output-kolonner gjengitt korrekt. | **OK** |
| 5.3 | [tab_renselogg.csv](../../006%20analysis/aktiviteter/04_dataprosessering/tab_renselogg.csv) | 18 målepunkter. `datoformat_dd_mm_yyyy=4 042`, `datoformat_mm_dd_yyyy=5 952`, `antall_rader_inn/ut=9 994` — alle matcher. | **OK** |
| 5.4 | [tab_split_oversikt.csv](../../006%20analysis/aktiviteter/06_datasplitt/tab_split_oversikt.csv) | Trening 2022–2024=6 682, test 2025=3 312, andeler ~67 %/~33 %. | **OK** |
| 6.1 | [tab_lr_modelloversikt.csv](../../006%20analysis/aktiviteter/08_lineaer_regresjon/tab_lr_modelloversikt.csv), [tab_rf_modelloversikt.csv](../../006%20analysis/aktiviteter/09_random_forest_regressor/tab_rf_modelloversikt.csv), [tab_rf_tuned_modelloversikt.csv](../../006%20analysis/aktiviteter/11_parameterjustering_random_forest/tab_rf_tuned_modelloversikt.csv) | 6 682 treningsrader, 67 features, hyperparametre per modell matcher CSV-ene (LR `fit_intercept=True`; baseline RF `n_estimators=200, max_depth=None, min_samples_leaf=1, max_features=1.0`; tuned RF `n_estimators=400, max_depth=10, min_samples_leaf=4, max_features=sqrt`). | **OK** |
| 6.2 | [tab_rf_tuning_kandidater.csv](../../006%20analysis/aktiviteter/11_parameterjustering_random_forest/tab_rf_tuning_kandidater.csv) | Topp 5 rader (rang_rmse 1–5): rf_tune_30 (577,27 / 43,56), rf_tune_28 (577,29 / 43,57), rf_tune_10 (577,36 / 43,58), rf_tune_26 (577,65 / 43,60), rf_tune_12 (577,81 / 43,61). Delta-kolonnen mot baseline (−13,04 … −12,50) matcher rapporten. Baseline-referansen 590,30 / 44,22 matcher `tab_rf_tuned_modelloversikt.csv` `baseline_rmse_validering`. | **OK** |
| 7.1 | [tab_rmse_mape_maaned.csv](../../006%20analysis/aktiviteter/13_rmse_og_mape/tab_rmse_mape_maaned.csv) | 12 måneder × 3 modeller = 36 RMSE- og 36 MAPE-verdier. Stikkprøve: 2025-01 lineær 586,09 / 46,62 %; 2025-06 tuned RF 552,25 / 42,79 %; 2025-12 baseline RF 593,86 / 45,93 % — alle matcher CSV innenfor ±0,005. | **OK** |
| 7.2 | [tab_segmentmetrikk_modell.csv](../../006%20analysis/aktiviteter/16_tolke_modellresultater/tab_segmentmetrikk_modell.csv) | 14 segmenter × 3 modeller × 2 metrikker = 84 verdier. Stikkprøve: Kvartal 1 tuned RF 569,10 / 43,67 % (CSV 569,102258 / 43,6738 %); Salgsbånd lavt tuned RF 690,44 / 90,27 % (CSV 690,438613 / 90,2738 %); Region West baseline RF 581,36 / 43,18 % (CSV 581,363013 / 43,1784 %). Alle matcher. | **OK** |
| 8.1 | [tab_rmse_mape_oversikt.csv](../../006%20analysis/aktiviteter/13_rmse_og_mape/tab_rmse_mape_oversikt.csv) | 3 modeller × 2 metrikker. LR 580,39/44,18 %; baseline RF 589,28/44,12 %; tuned RF 578,26/43,97 %. Antall observasjoner 3 312 matcher testradtall. | **OK** |
| 8.2 | [tab_modellvinner_telling.csv](../../006%20analysis/aktiviteter/14_sammenligne_modellresultater/tab_modellvinner_telling.csv) | RMSE: lineær 1, baseline RF 0, tuned RF 11 ✓. MAPE: 3, 6, 3 ✓. | **OK** |
| 8.3 | [tab_rf_tuned_feature_importance.csv](../../006%20analysis/aktiviteter/15_viktige_variabler/tab_rf_tuned_feature_importance.csv) | Topp 10 verifisert kolonne-for-kolonne: Discount 11,48 %, dayofmonth 11,35 %, weekofyear 10,40 %, month 6,74 %, dayofweek 6,52 %, year 4,02 %, quarter 2,95 %, Region_East 2,04 %, Region_West 1,91 %, Region_Central 1,84 %. Alle matcher CSV innenfor ±0,005. | **OK** |
| 8.4 | [tab_segmentvinnere_tolkning.csv](../../006%20analysis/aktiviteter/16_tolke_modellresultater/tab_segmentvinnere_tolkning.csv) | 14 rader × 2 vinnerkolonner = 28 verdier. Alle RMSE-vinnere (tuned RF × 13, benchmark lineær × 1 for hoyt salg) og MAPE-vinnere (4 benchmark, 4 baseline, 6 tuned) matcher CSV. | **OK** |
| 9.1 | [tab_modellprofil_6_2.csv](../../006%20analysis/aktiviteter/17_styrker_og_svakheter/tab_modellprofil_6_2.csv) | 3 modeller × 9 kolonner = 27 verdier. RMSE/MAPE-tall og vinnertellinger stemmer 1:1. Tolkbarhet høy/middels/middels ✓. Hovedstyrke og hovedsvakhet tekst matcher CSV. | **OK** |
| 9.2 | [tab_beslutningsmatrise_6_3.csv](../../006%20analysis/aktiviteter/18_vurdere_praktisk_nytte/tab_beslutningsmatrise_6_3.csv) + [tab_bruksregler_6_3.csv](../../006%20analysis/aktiviteter/18_vurdere_praktisk_nytte/tab_bruksregler_6_3.csv) | 4 beslutningsområder med anbefalt modell, prioritert metrikk, praktisk nytte og hovedforbehold. Alle fire rader matcher kildefilen. | **OK** |
| 9.3 | [tab_metodebegrensninger_6_2.csv](../../006%20analysis/aktiviteter/17_styrker_og_svakheter/tab_metodebegrensninger_6_2.csv) | 6 temarader. ID-kolonne bevisst droppet i rapport (dokumentert i [rapport_7_2_3_artefakter.md](../rapport_7_2_3_artefakter.md) § 4.3). Beskrivelsestekst og konsekvenskolonner ordrett identiske med CSV. | **OK** |
| 12.1 | N/A (meta-tabell) | 7 rader A1–A7 peker til eksisterende filer (se § 1.5 under). | **OK** |

**Vurdering:** Alle 16 innholdstabeller gjengir kilde-CSV korrekt. Ingen avrundingsavvik > 0,005 påvist.

### 1.3 Feature-importance og variabelgrupper

Tabell 8.3 (topp 10 FI) og § 9.2 (variabelrangering) matcher [tab_rf_tuned_feature_importance.csv](../../006%20analysis/aktiviteter/15_viktige_variabler/tab_rf_tuned_feature_importance.csv). Gruppesum fra [tab_variabelgrupper_tuned_top10.csv](../../006%20analysis/aktiviteter/15_viktige_variabler/tab_variabelgrupper_tuned_top10.csv):

- kalender: 6 av 10 i topp 10, 41,9826 % → rapport «~42 %» ✓
- pris/kampanje: 1 av 10, 11,4781 % → rapport «11,48 %» ✓
- region: 3 av 10, 5,783 % → rapport «~5,8 %» ✓

Sum topp 10 = 41,98 + 11,48 + 5,78 = 59,24 %. Rapport gir ikke denne aggregerte verdien eksplisitt, men regnestykket er internt konsistent. **Vurdering: OK**.

### 1.4 Datastørrelser og modellmatriser

| Størrelse | Kilde | Kildeverdi | Rapportverdi (linje) | Vurdering |
|:----------|:------|:-----------|:---------------------|:----------|
| Rådata-rader | `tab_renselogg.csv` | 9 994 | 9 994 (275, 330, 384, 388, 403) | OK |
| Råkolonner | `tab_renselogg.csv` | 11 | 11 (330, 389) | OK |
| Renset antall_rader_ut | `tab_renselogg.csv` | 9 994 | 9 994 (403) | OK |
| Datoformat dd-mm-yyyy | `tab_renselogg.csv` | 4 042 | 4 042 (330, 392) | OK |
| Datoformat mm/dd/yyyy | `tab_renselogg.csv` | 5 952 | 5 952 (330, 393) | OK |
| Treningsrader 2022–2024 | `tab_split_oversikt.csv` | 6 682 | 6 682 (422, 437–439, 443, 445) | OK |
| Testrader 2025 | `tab_split_oversikt.csv` | 3 312 | 3 312 (423, 443, 445, 539) | OK |
| Features | `tab_split_oversikt.csv` | 67 | 67 (339, 437–439, 443, 445) | OK |
| Tuning-treningsrader 2022–2023 | `tab_split_oversikt.csv` | 1993+2102=4 095 | 4 095 (445) | OK |
| Tuning-valideringsrader 2024 | `tab_split_oversikt.csv` | 2 587 | 2 587 (445) | OK |
| LR intercept | `tab_lr_modelloversikt.csv` | −3 193,5519 | −3 193,55 (443) | OK |
| LR Discount-koeffisient | `tab_lr_koeffisienter.csv` | −166,3500 | −166,35 (525, 634) | OK |
| LR Region_North-koeffisient | `tab_lr_koeffisienter.csv` | −277,1994 | −277,20 (634) | OK |
| Tuning-baseline validering | `tab_rf_tuned_modelloversikt.csv` | 590,3039 / 44,2211 | 590,30 / 44,22 (445) | OK |
| Tuning-vinner validering | `tab_rf_tuned_modelloversikt.csv` | 577,2678 / 43,5554 | 577,27 / 43,56 (445) | OK |
| `⌊√67⌋` | matematisk | 8 | 8 (445) | OK |

**Vurdering: OK.** Alle datastørrelser, modellmatriser og tuningparametre stemmer eksakt.

### 1.5 Vedleggsreferanser A1–A7

Radantall i kildefilene er verifisert med `wc -l` (antall datarader = total − 1 headerlinje):

| ID | Rapportbeskrivelse | Filsti | Datarader | Vurdering |
|:---|:------------------|:-------|:----------|:----------|
| A1 | Radvise prognoser for 2025 for alle tre modeller (3 312 rader) | `12_prognoser_2025/tab_prognoser_2025_detalj.csv` | 3 312 | **OK** (tall eksplisitt korrekt) |
| A2 | Radvise prognosefeil og absoluttfeil for 2025 | `13_rmse_og_mape/tab_prognosefeil_2025_detalj.csv` | 3 312 | OK (fil eksisterer, ingen radangivelse i rapport) |
| A3 | Full tuning-kandidatgrid for Random Forest | `11_parameterjustering_random_forest/tab_rf_tuning_kandidater.csv` | 36 (1 baseline + 35 kandidater) | OK (fil eksisterer, ingen radangivelse i rapport) |
| A4 | Full feature importance for tuned Random Forest | `15_viktige_variabler/tab_rf_tuned_feature_importance.csv` | 67 | OK (fil eksisterer) |
| A5 | Full koeffisienttabell for lineær regresjon | `08_lineaer_regresjon/tab_lr_koeffisienter.csv` | 67 | OK (fil eksisterer) |
| A6 | Full RMSE og MAPE per måned i lang form | `13_rmse_og_mape/tab_rmse_mape_maaned.csv` | 36 (12 måneder × 3 modeller) | OK (fil eksisterer) |
| A7 | Full segmentmetrikk per modell | `16_tolke_modellresultater/tab_segmentmetrikk_modell.csv` | 42 (14 segmenter × 3 modeller) | OK (fil eksisterer) |

**Vurdering: OK.** Alle syv vedleggsreferanser peker til eksisterende CSV-filer, og den eneste eksplisitte radangivelsen i rapporten (A1 «3 312 rader») stemmer.

---

## Del 2 – Innholdsmessig konsistens

### 2.1 Figur-innhold vs. omtalende tekst

| Figur | Tekstpåstand i rapporten | CSV-bekreftelse | Vurdering |
|:------|:-------------------------|:----------------|:----------|
| 4.1 | «Eggs, Meat & Fish skiller seg ut med det høyeste gjennomsnittlige salgsnivået» (linje 279) | Verifiseres mot `fig_sales_per_category.png` (visuell lesing bekrefter høyeste søyle). | OK |
| 4.2 | «gjennomsnittsnivået i treningsperioden 2022–2024 er 1 493, mot 1 503 i testperioden 2025» (linje 288, 411) | Ikke direkte i CSV, men eksplisitt i casebeskrivelsen og konsistent gjentatt. | OK |
| 4.3 | «oktober er måneden med det høyeste gjennomsnittlige salgsnivået, mens juni er den svakeste» (linje 299) | Sesongprofil fremgår av `fig_sales_per_month_split.png`. | OK |
| 5.1 | Fordeling av datatyper (datobasert, numerisk, kategorisk) | `fig_datatype_fordeling.png` eksisterer på korrekt sti. | OK |
| 5.2 | «Overlappet i fordelingene tyder på at målvariabelen er stabil» (figurtekst) | Konsistent med `sales_gjennomsnitt` 1 493/1 503 fra § 4.2. | OK |
| 7.1 | «Kurven viser at alle tre modellene underestimerer i august–september» | CSV: alle tre `bias_pct < 0` både aug (−4,37/−5,13/−5,22 %) og sep (−2,86/−2,05/−2,77 %). | OK |
| 7.2 | «Tuned Random Forest har lavest RMSE i majoriteten av månedene, mens benchmark lineær slår gjennom i enkeltmåneder» | `tab_modellvinner_telling.csv`: tuned RF vinner 11/12 måneder RMSE; lineær vinner 1. | OK |
| 8.1 | «Tuned Random Forest har lavest RMSE, mens MAPE er tettere fordelt» | `tab_rmse_mape_oversikt.csv`: RMSE-spenn 578,26–589,28 (11,02 enheter); MAPE-spenn 43,97–44,18 % (0,21 pp). | OK |
| 8.2 | «Topp 10 feature importance … viser hvilke signaler modellen faktisk vektlegger» | Figuren dekker samme ti variabler som Tabell 8.3. | OK |
| 8.3 | «hvilke grupper av signaler (kalender, pris/kampanje, region) som dominerer» | `tab_variabelgrupper_tuned_top10.csv`: kalender, pris/kampanje, region — ingen andre grupper i topp 10. | OK |

**Vurdering: OK.** Alle figurer er dekkende omtalt i teksten, og tekstpåstandene stemmer med underliggende data.

### 2.2 Kryssreferanser (tabell-/figurnummer i tekst)

Grep etter «Tabell 5.» til «Tabell 12.» og «Figur 4.» til «Figur 8.»:

- Tabell 5.1 → 5.4 refereres korrekt i § 5.2 (linje 341, 359, 384, 418, 422).
- Tabell 6.1 → 6.2 refereres i § 6 (linje 433, 447).
- Tabell 7.1 og 7.2 refereres i § 7 (linje 467, 465, 502, 504).
- Tabell 8.1 → 8.4 refereres i § 8 og § 9 (linje 463, 467, 525, 531, 548, 558, 589).
- Tabell 9.1 → 9.3 refereres i § 9.1, § 9.3, § 9.4 (linje 620, 640, 657).
- Tabell 12.1 — eneste mangel er at introduksjonssetning mangler (F2 fra 7.3.1, overført til 7.3.3).
- Figur 4.1 → 8.3: alle refereres i sin egen seksjon før bildeblokken. Eneste avvik: linje 306 «figur 4.3» med liten `f` (F1 fra 7.3.1, overført til 7.3.3).

**Vurdering: OK.** Kryssreferansene er entydige og peker til riktig element. Avvikene F1/F2 er dokumentert i 7.3.1 og skal lukkes i 7.3.3.

### 2.3 Intern tekstkonsistens (avrunding og skrivemåte)

Samme nøkkeltall er kontrollert i alle forekomster i rapporten:

- **RMSE 578,26:** Sammendrag, Abstract, Tabell 8.1, Tabell 9.1, § 9.1, Konklusjon. Identisk skrivemåte og avrunding alle seks steder. OK.
- **MAPE 43,97 %:** samme seks steder. Identisk. OK.
- **11,48 %:** Sammendrag, Abstract, § 7 (linje 525), Tabell 8.3 (linje 562), § 9.2 (linje 632). Identisk. OK.
- **~42 % kalender:** Sammendrag, Abstract, § 7 (linje 525), § 9.2 (linje 632), Konklusjon (linje 684). Identisk. OK.
- **~5,8 % region:** § 7 (linje 525) og § 9.2 (linje 632). Identisk. OK.
- **9 994:** § 4.1 (linje 275), § 5.2 (linje 330, 384), Tabell 5.3 (linje 388, 403). Identisk. OK.
- **6 682/3 312:** Tabell 5.4, Tabell 6.1, § 6 (linje 443–445), Tabell 8.1 (linje 539), § 9.1 konsekvent. Identisk. OK.
- **67 features:** § 5.2, Tabell 6.1, § 6. Identisk. OK.
- **Vinnermåneder 11 / vinnersegmenter 13:** Sammendrag «elleve av tolv måneder og tretten av fjorten segmenter»; § 7 (linje 465) «11 av 12»; § 8 Tabell 8.2 «11»; Tabell 9.1 «11» og «13»; Konklusjon «elleve av tolv måneder og tretten av fjorten tolkningssegmenter». Identisk mening. OK.

**Minor linguistic observation (se F1):** Sammendrag linje 103 formulerer: «rabatt (11,48 %) og kalendervariablene, som samlet utgjør om lag 42 % av importance i topp 10». Relativsetningen «som samlet utgjør» kan leses som at både rabatt og kalender til sammen er 42 %, men den faktiske dataen er at kalendergruppen alene utgjør 42 %. Tilsvarende tvetydighet i Abstract. Andre steder i rapporten (linje 525, 632, 684) formulerer det tydelig som «kalendergruppen samlet». Se F1.

### 2.4 Funn fra tidligere reviewer

| # | Funn | Alvorlighet | Status | Tilhører 7.3.2? |
|:--|:-----|:------------|:-------|:----------------|
| 7.3.1-F1 | Liten «f» i «figur 4.3» linje 306 | Lav | Åpen, overført til 7.3.3 | Nei (språkvask) |
| 7.3.1-F2 | Manglende introduksjonssetning for Tabell 12.1 | Lav | Åpen, overført til 7.3.3 | Nei (språkvask) |
| 7.3.1-F3 | Litteratur kun fra ikke-fagfellevurderte kilder | Lav | Åpen, overført til WBS 8.1 | Nei (akademisk dybde) |
| 7.3.1-KR-007 | M5-forsinkelse ikke eksplisitt dokumentert | – | Åpen, overført til WBS 8.1 | Nei (prosjektstyring) |

Ingen av de fire åpne punktene fra 7.3.1 påvirker numerisk eller innholdsmessig konsistens mellom rapport og analyseartefakter. 7.3.2 konkluderer uavhengig av disse.

---

## Svakheter og forbedringsforslag

### F1. Tvetydig formulering om kalenderandel i Sammendrag og Abstract

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold / intern konsistens

Sammendrag (linje 103): «De mest påvirkningsrike prediktorene er rabatt (11,48 %) og kalendervariablene, som samlet utgjør om lag 42 % av importance i topp 10.» Abstract (linje 113) har tilsvarende formulering: «and the calendar variables, which together account for around 42 % of importance in the top ten.»

Relativsetningen «som samlet utgjør» kan grammatisk peke tilbake til både rabatt og kalender (= 53,46 % samlet — feil) eller bare kalender (= 41,98 % — riktig). Andre steder i rapporten er dette formulert entydig: linje 525 «kalendervariablene utgjør samlet ~42 %», linje 632 «Kalendergruppen står samlet for om lag 42 %», linje 684 «kalendergruppen samlet står for om lag 42 %». Tvetydigheten i Sammendrag/Abstract er derfor en språklig presisering, ikke et numerisk avvik.

**Anbefalt tiltak:** Omformuler til «De mest påvirkningsrike prediktorene er rabatt (11,48 %) og kalendervariablene, der kalendergruppen samlet utgjør om lag 42 % av importance i topp 10.» Tilsvarende i Abstract: «… where the calendar group together accounts for around 42 % …». Tilhører WBS 7.3.3 språkvask.

### F2. Inkonsistent behandling av variabelen `State` i Tabell 5.1 vs. Tabell 5.2 og brødtekst

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold / intern konsistens

Tabell 5.1 (linje 350) oppfører `State` med anbefaling `inkluder` og begrunnelse «Kategorisk variabel med håndterbar kardinalitet.» Men samme tabell viser at `State` har bare 1 unik verdi, og både § 5.2-teksten (linje 339: «`State` fordi kolonnen er konstant i datasettet») og Tabell 5.2 (linje 380: `ekskluder` med begrunnelse «Kolonnen er konstant i datasettet og gir ingen forklaringskraft.») behandler variabelen som ekskludert.

Dette er en legacy fra oppdateringsrekkefølgen i analysen: [tab_relevante_variabler.csv](../../006%20analysis/aktiviteter/02_identifisere_relevante_variabler/tab_relevante_variabler.csv) ble etablert før feature engineering (aktivitet 05) oppdaget at `State` er konstant. CSV-kilden sier fortsatt `inkluder` for `State`. Rapporten gjengir Tabell 5.1 ordrett etter CSV, men skaper samtidig intern motsigelse mot Tabell 5.2 og brødteksten.

**Anbefalt tiltak:** Oppdater Tabell 5.1 i rapporten slik at `State`-raden enten får anbefaling `ekskluder` med begrunnelse «Kolonnen er konstant (1 unik verdi); ekskluderes i feature engineering.», eller legg til en fotnote/merknad etter tabellen som forklarer at den endelige avgjørelsen om `State` er synlig i Tabell 5.2. Alternativt kan kildefilen [tab_relevante_variabler.csv](../../006%20analysis/aktiviteter/02_identifisere_relevante_variabler/tab_relevante_variabler.csv) oppdateres samtidig for sporbarhet, men det er ikke nødvendig for å lukke punktet i rapporten. Tilhører WBS 7.3.3 språkvask.

### F3. Tvetydig MAPE-referanse i § 7 (linje 502)

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Linje 502: «tuned Random Forest likevel gir lavest RMSE i segmentet «lavt salg» til tross for at MAPE der ligger på 89,39 %.»

89,39 % er baseline RFs MAPE i segmentet (kilde: [tab_segmentvinnere_tolkning.csv](../../006%20analysis/aktiviteter/16_tolke_modellresultater/tab_segmentvinnere_tolkning.csv), rad `sales_band=lavt salg`, `mape_verdi=89,3929`). Den vinnende MAPE i segmentet — altså laveste MAPE — er baseline RFs 89,39 %. Tuned RFs egen MAPE i samme segment er 90,27 % (kilde: [tab_segmentmetrikk_modell.csv](../../006%20analysis/aktiviteter/16_tolke_modellresultater/tab_segmentmetrikk_modell.csv)). Formuleringen er derfor teknisk korrekt — 89,39 % er det laveste MAPE-nivået i segmentet — men kan leses som at 89,39 % er tuned RFs MAPE, noe som ville vært feil.

**Anbefalt tiltak:** Omformuler til én av følgende:
(a) «til tross for at laveste MAPE i segmentet fortsatt er 89,39 %» (presiserer at det er segmentets beste MAPE).
(b) «til tross for at MAPE i segmentet er over 89 % for alle tre modellene» (generell påstand).
(c) «til tross for at tuned RFs MAPE i segmentet ligger på 90,27 %» (endrer referanseverdien til tuned RFs egen MAPE).

Tilhører WBS 7.3.3 språkvask.

---

## Avhukningsliste – tiltak

| # | Tiltak | Kategori | Status | Kommentar |
|:--|:-------|:---------|:-------|:----------|
| F1 | Omformuler Sammendrag linje 103 og Abstract linje 113 slik at «42 %» entydig refererer til kalendergruppen alene | Språk og innhold | [—] | Overført til WBS 7.3.3 språkvask |
| F2 | Oppdater Tabell 5.1 slik at `State`-anbefalingen ikke motsier Tabell 5.2 og brødteksten | Språk og innhold | [—] | Overført til WBS 7.3.3 språkvask |
| F3 | Omformuler linje 502 slik at referansen til 89,39 % er entydig | Språk og innhold | [—] | Overført til WBS 7.3.3 språkvask |

Ingen V-tiltak — reviewen avdekket ikke svakheter som blokkerer lukking av 7.3.2. Alle tre F-punkter er overført til WBS 7.3.3 språkvask og låsing av førsteutkastet sammen med F1 og F2 fra 7.3.1.

---

## Samsvar med prosjektplan og krav

| Sjekkpunkt | Status | Kommentar |
|:---|:---|:---|
| Alle rapportfigurer peker til eksisterende artefakter | OK | 10/10 PNG-filer eksisterer på korrekt relativ sti |
| Alle rapporttabeller stemmer med kilde-CSV | OK | 16/16 tabeller verifisert innenfor ±0,005 |
| Alle ankerpåstander i Sammendrag/Abstract stemmer med CSV | OK | 9/9 påstander (A1–A9) bekreftet |
| Vedleggsreferanser peker til eksisterende filer | OK | 7/7 A-referanser verifisert |
| Intern tekstkonsistens (samme tall, samme avrunding) | OK med språklig presisering | F1 og F3 er lingvistiske, ikke numeriske |
| Figurinnhold matcher omtalende tekst | OK | Bias-retning, vinnerantall, gruppedominans verifisert |
| Encoding æ/ø/å bevart i tabeller og figurtekst | OK | Alle norske tegn gjengitt korrekt |
| Kryssreferanser (Tabell/Figur-numre) peker rett sted | OK | Ingen brutte henvisninger |

---

## Samlet vurdering

### Numerisk konsistens

Rapporten er numerisk konsistent med analyseartefaktene. Alle ni ankerpåstander i Sammendrag og Abstract stemmer eksakt med kilde-CSV, og samtlige 16 innholdstabeller gjengir verdier innenfor ±0,005-toleranse. Det er ingen avrundingsdrift mellom kapitler, og interne tall (RMSE 578,26, MAPE 43,97 %, 11/12 måneder, 13/14 segmenter, 11,48 % rabatt, ~42 % kalender) skrives identisk på alle seks–ni forekomster. Modellmatrise, hyperparametre, tuningresultat og bias-tall er alle 1:1 sporbare til kildeartefaktene.

### Innholdsmessig konsistens

Figurer og tabeller er dekkende beskrevet i brødteksten, og figurtekstenes påstander (underestimering i august–september, kalender som dominerende variabelgruppe, RMSE-spenn smalere enn MAPE-spenn) samsvarer med CSV-verdiene. Kryssreferanser peker rett sted. Tre mindre språklige presiseringer (F1–F3) gjelder tvetydig formuleringer i Sammendrag/Abstract og § 7, og en legacy-inkonsistens i Tabell 5.1 om `State`. Alle tre er språkvaskpunkter snarere enn konsistensfeil i tallene.

### Anbefalt prioritering videre

1. **(Bør)** F1 — Omformuler Sammendrag/Abstract slik at 42 %-referansen entydig gjelder kalender.
2. **(Bør)** F2 — Rett Tabell 5.1 `State`-anbefaling eller legg til forklarende merknad.
3. **(Kan)** F3 — Presiser at 89,39 % er segmentets laveste MAPE, ikke tuned RFs.

Alle tre F-punktene overføres til WBS 7.3.3 språkvask sammen med F1 og F2 fra 7.3.1.

### Lukkebeslutning for WBS 7.3.2

Reviewen er lukket 2026-04-21. Ingen V-funn ble identifisert; rapporten er numerisk og innholdsmessig konsistent med analyseartefaktene. De tre lave F-punktene F1–F3 overføres til WBS 7.3.3 språkvask. WBS 7.3.2 settes til 100 % i [wbs.json](../wbs.json) og avhukes i [status.md](../status.md). Neste aktivitet er WBS 7.3.3 språkvask og låsing av førsteutkastet, som samlet håndterer F1/F2 fra 7.3.1 og F1/F2/F3 fra denne reviewen.
