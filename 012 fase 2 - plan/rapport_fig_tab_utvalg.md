# Utvalg av figurer og tabeller i rapport.md

Opprettet: 2026-04-19 (WBS 7.2.1)

Dette dokumentet låser hvilke figurer og tabeller som skal ligge i [rapport.md](../005%20report/rapport.md), kobler hver artefakt til kilden i [006 analysis/aktiviteter/](../006%20analysis/aktiviteter/), og setter forslag til figur- og tabelltekst. Produksjonen av nye artefakter gjøres i WBS 7.2.2 (case/data) og WBS 7.2.3 (analyse/resultat/diskusjon). Innsetting, nummerering og formatering i rapporten gjøres i WBS 7.2.4.

## 1 Formål

- Beslutte det endelige utvalget av figurer og tabeller som skal inn i rapporten.
- Koble hver artefakt til en identifiserbar analyseaktivitet og kildefil.
- Spesifisere kort figurtekst/tabelltittel for hver post, slik at produksjonen i 7.2.2 og 7.2.3 har entydige bestillinger.
- Dokumentere hvilke analyseartefakter som bevisst er valgt bort og hvorfor.

## 2 Formkrav fra LOG650

Følgende prinsipper gjelder for forskningsprosjektet i LOG650 og er styrende for alt arbeid i 7.2 og 7.3:

- Figurer og tabeller nummereres separat og i den rekkefølgen de omtales.
- Titler plasseres under både figurer og tabeller.
- Alle visuelle elementer skal omtales eksplisitt i teksten før de vises.
- Figurer og tabeller skal være lesbare, konsistente i stil og tydelige i layout.
- Figur- og tabelltekster skal inneholde nok informasjon til at leseren forstår figuren eller tabellen uten å måtte konsultere hovedteksten.
- Dersom en figur eller tabell er egenprodusert, oppgis ingen kilde; manglende kilde betyr at studenten selv har laget den.
- Dersom figuren eller tabellen er hentet fra eller basert på en ekstern kilde, skal dette oppgis tydelig i figur- eller tabellteksten.
- Stort eller detaljert datamateriale skal plasseres i vedlegg.
- En god andel egenproduserte figurer og visualiseringer anbefales, fordi de viser selvstendig analyse og studentens egne faglige vurderinger.

**Konsekvens for dette prosjektet:** Alle figurer og tabeller i utvalget er produsert av prosjektgruppen basert på eget analysearbeid i [006 analysis/](../006%20analysis/). De skal derfor ikke ha kildehenvisning i figur-/tabellteksten. Datagrunnlaget (Kaggle-datasettet Supermart Grocery Sales) omtales i kap. 5.2 i rapporten, ikke i figurtekstene.

## 3 Nummereringskonvensjon

Kravet «nummereres separat og i den rekkefølgen de omtales» kan leses på to måter:

- **(a) Gjennomgående numre:** Figur 1, Figur 2, … og Tabell 1, Tabell 2, … uavhengig av kapittel.
- **(b) Kapittelbundne numre:** Figur 4.1, Figur 4.2, Figur 5.1 … og Tabell 5.2, Tabell 6.1, Tabell 8.1 …

Rapporten bruker i dag (b), og dette er konsistent med universitets- og høgskolemaler generelt. **Planen beholder (b) som arbeidsantagelse.** Det er dermed seks hovedregler i 7.2.4:

1. Figurer nummereres per hovedkapittel i rekkefølgen de omtales: 4.1 → 4.2 → 4.3 → 5.1 → 5.2 → 7.1 → 7.2 → 8.1 → 8.2 → 8.3.
2. Tabeller nummereres per hovedkapittel i rekkefølgen de omtales: 5.2 → 5.3 → 5.4 → 5.5 → 6.1 → 6.2 → 7.1 → 7.2 → 8.1 → 8.2 → 8.3 → 8.4 → 9.1 → 9.2 → 9.3.
3. Ingen hopp bakover i rekkefølgen innen samme kapittel.
4. Figurer og tabeller har hver sin sekvens – det samme nummer kan brukes for en figur og en tabell i samme kapittel (eks. Figur 7.1 og Tabell 7.1).
5. Spørsmålet om overgang til gjennomgående nummerering tas opp i WBS 7.3.1 (struktur- og kravsjekk), ikke i 7.2.1.
6. Når en seksjon får flere tabeller eller figurer fordelt over underseksjoner i ulike kapittelnumre, må tabell- og figurnummer settes i samme rekkefølge som underseksjonene – ikke etter underseksjonens interne navn. Rekkefølgen i teksten skal styre nummereringen.

**Avvikshåndtering for tabelltittel:** Markdown-tabellene i rapporten har i dag ingen egen tittel-linje. 7.2.4 skal sette inn en sentrert, kursiv tabelltittel under hver tabell etter samme HTML-mønster som brukes under figurer.

## 4 Status før utvalget

Rapporten inneholder per 2026-04-16 følgende innholdsbærende artefakter (forsidebilder utelatt):

| Nr i rapport | Type | Tittel/funksjon | Kilde |
|---|---|---|---|
| Figur 4.1 | figur | Gjennomsnittlig salg per kategori | [fig_sales_per_category.png](../006%20analysis/aktiviteter/07_eksplorativ_analyse_og_visualisering/fig_sales_per_category.png) |
| Figur 4.2 | figur | Månedlig totalsalg med trenings- og testperiode | [fig_sales_over_tid_train_test.png](../006%20analysis/aktiviteter/07_eksplorativ_analyse_og_visualisering/fig_sales_over_tid_train_test.png) |
| Figur 4.3 | figur | Gjennomsnittlig salg per måned (sesongmønster) | [fig_sales_per_month_split.png](../006%20analysis/aktiviteter/07_eksplorativ_analyse_og_visualisering/fig_sales_per_month_split.png) |
| Tabell 5.5 | tabell | Fordeling mellom trenings- og testdata | egen tekst i rapporten, basert på [tab_split_oversikt.csv](../006%20analysis/aktiviteter/06_datasplitt/tab_split_oversikt.csv) |
| Tabell 8.1 | tabell | Samlet prognoseytelse 2025 (RMSE/MAPE) | basert på [tab_rmse_mape_oversikt.csv](../006%20analysis/aktiviteter/13_rmse_og_mape/tab_rmse_mape_oversikt.csv) |
| Tabell 8.2 | tabell | Månedlig vinnertelling per metrikk | basert på [tab_modellvinner_telling.csv](../006%20analysis/aktiviteter/14_sammenligne_modellresultater/tab_modellvinner_telling.csv) |
| Tabell 8.3 | tabell | Topp 10 feature importance for tuned Random Forest | basert på [tab_rf_tuned_feature_importance.csv](../006%20analysis/aktiviteter/15_viktige_variabler/tab_rf_tuned_feature_importance.csv) |
| Tabell 8.4 | tabell | Vinnermodell per segment | basert på [tab_segmentvinnere_tolkning.csv](../006%20analysis/aktiviteter/16_tolke_modellresultater/tab_segmentvinnere_tolkning.csv) |

## 5 Figurutvalg per kapittel

Alle figurer er egenproduserte. Figurtekst plasseres under figuren og skal være selvstendig forståelig.

### 5.1 Kapittel 4 Casebeskrivelse

| Nr | Kilde | Beholdes/Ny | Plassering i rapport | Foreslått figurtekst |
|---|---|---|---|---|
| Figur 4.1 | [fig_sales_per_category.png](../006%20analysis/aktiviteter/07_eksplorativ_analyse_og_visualisering/fig_sales_per_category.png) | beholdes | 4.1 Dagligvare og beslutningssituasjonen | *Figur 4.1 Gjennomsnittlig salg per produktkategori i perioden 2022–2024. Høyere søyler viser kategorier med større gjennomsnittlig ordreverdi og tydeligere kampanje-/volumvariasjon.* |
| Figur 4.2 | [fig_sales_over_tid_train_test.png](../006%20analysis/aktiviteter/07_eksplorativ_analyse_og_visualisering/fig_sales_over_tid_train_test.png) | beholdes | 4.2 Historisk salgsutvikling | *Figur 4.2 Månedlig totalsalg 2022–2025. Treningsperioden 2022–2024 og testperioden 2025 er markert, slik at trend- og sesongforløp kan sammenlignes mellom de to periodene.* |
| Figur 4.3 | [fig_sales_per_month_split.png](../006%20analysis/aktiviteter/07_eksplorativ_analyse_og_visualisering/fig_sales_per_month_split.png) | beholdes | 4.3 Sesongmønster i salget | *Figur 4.3 Gjennomsnittlig salg per kalendermåned i trenings- og testperioden. Sammenligningen synliggjør sesongmønsteret og vurderer stabiliteten mellom trening og test.* |

### 5.2 Kapittel 5 Metode og data

Figurene plasseres i §5.2 Data: Figur 5.1 tidlig i seksjonen (strukturbeskrivelse), Figur 5.2 etter diskusjonen av målvariabelen og datasplitten.

| Nr | Kilde | Beholdes/Ny | Plassering i rapport | Foreslått figurtekst |
|---|---|---|---|---|
| Figur 5.1 | [fig_datatype_fordeling.png](../006%20analysis/aktiviteter/01_dataforstaelse_og_variabler/fig_datatype_fordeling.png) | ny (eksisterer) – kopieres inn i 7.2.2 | 5.2 Data, tidlig i seksjonen | *Figur 5.1 Fordeling av datatyper i rådatasettet. Fordelingen viser hvor mange kolonner som er numeriske, kategoriske og datobaserte, og underbygger valg av forbehandling og feature engineering.* |
| Figur 5.2 | [fig_sales_fordeling_train_test.png](../006%20analysis/aktiviteter/07_eksplorativ_analyse_og_visualisering/fig_sales_fordeling_train_test.png) | ny (eksisterer) – kopieres inn i 7.2.2 | 5.2 Data, etter Figur 5.1 | *Figur 5.2 Fordeling av daglige salgsverdier i trenings- og testperioden. Overlappet i fordelingene tyder på at målvariabelen er stabil mellom periodene.* |

### 5.3 Kapittel 7 Analyse

Begge figurene må produseres i 7.2.3 som nye plotteskript, og lagres i respektiv aktivitetsmappe.

| Nr | Kilde (data) | Type plot | Plassering i rapport | Foreslått figurtekst |
|---|---|---|---|---|
| Figur 7.1 | [tab_bias_maaned_modell.csv](../006%20analysis/aktiviteter/16_tolke_modellresultater/tab_bias_maaned_modell.csv) | linjediagram, én linje per modell (LR, RF baseline, tuned RF), x = måned 2025-01…2025-12, y = bias i kroner | 7 Analyse, etter diskusjonen av systematiske feil | *Figur 7.1 Månedlig bias per modell i 2025. Positive verdier betyr at modellen overestimerer salget, negative at den underestimerer. Kurven viser at alle tre modellene underestimerer i august–september.* |
| Figur 7.2 | [tab_rmse_mape_maaned.csv](../006%20analysis/aktiviteter/13_rmse_og_mape/tab_rmse_mape_maaned.csv) | linjediagram, én linje per modell, x = måned 2025-01…2025-12, y = RMSE | 7 Analyse, etter Figur 7.1 | *Figur 7.2 Månedlig RMSE per modell i 2025. Tuned Random Forest har lavest RMSE i majoriteten av månedene, mens benchmark lineær slår gjennom i enkeltmåneder.* |

### 5.4 Kapittel 8 Resultat

Alle tre figurene produseres i 7.2.3. Rekkefølgen er valgt slik at figurnummeret matcher tekstrekkefølgen i kap. 8.

| Nr | Kilde (data) | Type plot | Plassering i rapport | Foreslått figurtekst |
|---|---|---|---|---|
| Figur 8.1 | [tab_rmse_mape_oversikt.csv](../006%20analysis/aktiviteter/13_rmse_og_mape/tab_rmse_mape_oversikt.csv) | gruppert søyleplot, tre søyler per metrikk, én metrikk per akse (RMSE i kroner; MAPE i prosent) | 8 Resultat, etter Tabell 8.1 | *Figur 8.1 Samlet RMSE og MAPE for benchmark lineær, Random Forest baseline og tuned Random Forest i 2025. Tuned Random Forest har lavest RMSE, mens MAPE er tettere fordelt mellom modellene.* |
| Figur 8.2 | [tab_rf_tuned_feature_importance.csv](../006%20analysis/aktiviteter/15_viktige_variabler/tab_rf_tuned_feature_importance.csv) (topp 10) | horisontalt søyleplot, sortert synkende | 8 Resultat, etter Tabell 8.3 | *Figur 8.2 Topp 10 feature importance for tuned Random Forest. Variablene er rangert etter normalisert viktighet og viser hvilke signaler modellen faktisk vektlegger.* |
| Figur 8.3 | [tab_variabelgrupper_tuned_top10.csv](../006%20analysis/aktiviteter/15_viktige_variabler/tab_variabelgrupper_tuned_top10.csv) | søyleplot, én søyle per variabelgruppe | 8 Resultat, etter Figur 8.2 | *Figur 8.3 Samlet feature importance per variabelgruppe i topp 10 for tuned Random Forest. Figuren oppsummerer hvilke grupper av signaler (tid, pris/rabatt, geografi, kategori) som dominerer modellens prediksjon.* |

### 5.5 Øvrige kapitler

Kapittel 1–3, 6, 9, 10 og 11 får ingen figurer i denne rapporten. Det er i tråd med anbefalt praksis (innledning, teori, modellering og diskusjon bæres av tekst og tabeller).

## 6 Tabellutvalg per kapittel

Alle tabeller er egenproduserte. Tabelltittel plasseres under tabellen i samme stil som figurtekst (sentrert, liten skrift, kursiv) i WBS 7.2.4.

### 6.1 Kapittel 5 Metode og data

| Nr | Kilde | Beholdes/Ny | Plassering | Foreslått tabelltittel |
|---|---|---|---|---|
| Tabell 5.2 | [tab_relevante_variabler.csv](../006%20analysis/aktiviteter/02_identifisere_relevante_variabler/tab_relevante_variabler.csv) | ny | 5.2 Data, tidlig | *Tabell 5.2 Variabeloversikt med datatype, manglende andel og anbefaling for videre bruk (target, inkluder, vurder, ekskluder).* |
| Tabell 5.3 | [tab_featurevalg.csv](../006%20analysis/aktiviteter/05_feature_engineering/tab_featurevalg.csv) | ny | 5.2 Data, etter Tabell 5.2 | *Tabell 5.3 Feature engineering-oppsett: input-kolonne, handling og resulterende output-kolonne med begrunnelse.* |
| Tabell 5.4 | [tab_renselogg.csv](../006%20analysis/aktiviteter/04_dataprosessering/tab_renselogg.csv) | ny | 5.2 Data, etter Tabell 5.3 | *Tabell 5.4 Datarensing – målepunkter, verdier og kommentarer som dokumenterer kvalitetskontrollen før modellering.* |
| Tabell 5.5 | eksisterende i rapporten | beholdes (renummerert fra Tabell 5.1) | 5.2 Data, sist i seksjonen | *Tabell 5.5 Fordeling mellom trenings- (2022–2024) og testdata (2025) med antall rader og antall features.* |

### 6.2 Kapittel 6 Modellering

| Nr | Kilde | Beholdes/Ny | Plassering | Foreslått tabelltittel |
|---|---|---|---|---|
| Tabell 6.1 | [tab_lr_modelloversikt.csv](../006%20analysis/aktiviteter/08_lineaer_regresjon/tab_lr_modelloversikt.csv) + [tab_rf_modelloversikt.csv](../006%20analysis/aktiviteter/09_random_forest_regressor/tab_rf_modelloversikt.csv) + [tab_rf_tuned_modelloversikt.csv](../006%20analysis/aktiviteter/11_parameterjustering_random_forest/tab_rf_tuned_modelloversikt.csv) | ny (sammenstilles i 7.2.3) | 6 Modellering | *Tabell 6.1 Oversikt over de tre modellsporene: antall features, antall treningsrader, sentrale hyperparametre og kort rolle i prosjektet.* |
| Tabell 6.2 | [tab_rf_tuning_vinner.csv](../006%20analysis/aktiviteter/11_parameterjustering_random_forest/tab_rf_tuning_vinner.csv) + topp 5 fra [tab_rf_tuning_kandidater.csv](../006%20analysis/aktiviteter/11_parameterjustering_random_forest/tab_rf_tuning_kandidater.csv) | ny | 6 Modellering | *Tabell 6.2 Topp 5 parameterkombinasjoner fra tuning av Random Forest, sortert etter RMSE på 2024-valideringen, med n\_estimators, max\_depth, min\_samples\_leaf, max\_features, valideringens RMSE/MAPE og delta mot baseline.* |

### 6.3 Kapittel 7 Analyse

| Nr | Kilde | Beholdes/Ny | Plassering | Foreslått tabelltittel |
|---|---|---|---|---|
| Tabell 7.1 | [tab_rmse_mape_maaned.csv](../006%20analysis/aktiviteter/13_rmse_og_mape/tab_rmse_mape_maaned.csv) | ny (kompakt – én rad per måned, kolonner LR/RF/tuned RF) | 7 Analyse, før Figur 7.2 | *Tabell 7.1 Månedlig RMSE og MAPE per modell i 2025. Tabellen underbygger figurene 7.1 og 7.2 med eksakte tall for hver måned.* |
| Tabell 7.2 | [tab_segmentmetrikk_modell.csv](../006%20analysis/aktiviteter/16_tolke_modellresultater/tab_segmentmetrikk_modell.csv) + [tab_segmentdefinisjoner.csv](../006%20analysis/aktiviteter/16_tolke_modellresultater/tab_segmentdefinisjoner.csv) | ny (utvalg: kvartal, rabattnivå, region, salgsbånd) | 7 Analyse, etter Figur 7.2 | *Tabell 7.2 RMSE og MAPE per modell i utvalgte segmenter (kvartal, rabattbånd, region, salgsbånd). Segmentinndelingen er definert ut fra dataene og gir et bilde av hvor prognosene er stabile.* |

### 6.4 Kapittel 8 Resultat

| Nr | Kilde | Beholdes/Ny | Plassering | Foreslått tabelltittel |
|---|---|---|---|---|
| Tabell 8.1 | eksisterende i rapporten, basert på [tab_rmse_mape_oversikt.csv](../006%20analysis/aktiviteter/13_rmse_og_mape/tab_rmse_mape_oversikt.csv) | beholdes | 8 Resultat | *Tabell 8.1 Samlet prognoseytelse 2025 for de tre modellene, målt som RMSE i kroner og MAPE i prosent.* |
| Tabell 8.2 | eksisterende i rapporten, basert på [tab_modellvinner_telling.csv](../006%20analysis/aktiviteter/14_sammenligne_modellresultater/tab_modellvinner_telling.csv) | beholdes | 8 Resultat | *Tabell 8.2 Månedlig vinnertelling 2025 per metrikk, med antall og andel vinnermåneder per modell.* |
| Tabell 8.3 | eksisterende i rapporten, basert på [tab_rf_tuned_feature_importance.csv](../006%20analysis/aktiviteter/15_viktige_variabler/tab_rf_tuned_feature_importance.csv) | beholdes | 8 Resultat | *Tabell 8.3 Topp 10 feature importance for tuned Random Forest, med normalisert viktighet i prosent og variabelgruppe.* |
| Tabell 8.4 | eksisterende i rapporten, basert på [tab_segmentvinnere_tolkning.csv](../006%20analysis/aktiviteter/16_tolke_modellresultater/tab_segmentvinnere_tolkning.csv) | beholdes | 8 Resultat | *Tabell 8.4 Vinnermodell per segment, med antall rader og beste modell på henholdsvis RMSE og MAPE.* |

### 6.5 Kapittel 9 Diskusjon

| Nr | Kilde | Beholdes/Ny | Plassering | Foreslått tabelltittel |
|---|---|---|---|---|
| Tabell 9.1 | [tab_modellprofil_6_2.csv](../006%20analysis/aktiviteter/17_styrker_og_svakheter/tab_modellprofil_6_2.csv) | ny | 9.1 Tolkning av hovedfunn | *Tabell 9.1 Modellprofil med samlet RMSE/MAPE, antall vinnermåneder og -segmenter, tolkbarhetsnivå samt hovedstyrke og hovedsvakhet per modell.* |
| Tabell 9.2 | [tab_beslutningsmatrise_6_3.csv](../006%20analysis/aktiviteter/18_vurdere_praktisk_nytte/tab_beslutningsmatrise_6_3.csv) + [tab_bruksregler_6_3.csv](../006%20analysis/aktiviteter/18_vurdere_praktisk_nytte/tab_bruksregler_6_3.csv) | ny (sammenstilt) | 9.3 Praktisk nytte for Dagligvare | *Tabell 9.2 Beslutningsmatrise og bruksregler: beslutningsområder, anbefalt modellrolle, prioritert metrikk, praktisk nyttegrad og hovedforbehold.* |
| Tabell 9.3 | [tab_metodebegrensninger_6_2.csv](../006%20analysis/aktiviteter/17_styrker_og_svakheter/tab_metodebegrensninger_6_2.csv) | ny | 9.4 Metodiske begrensninger | *Tabell 9.3 Metodiske begrensninger i studien, med tematisk kategori, beskrivelse og konsekvens for pålitelighet og generaliserbarhet. ID-kolonnen fra kildefilen droppes i rapporten for lesbarhet; IDs beholdes i kilde-CSV for sporbarhet.* |

## 7 Nye artefakter som må produseres

### 7.1 Kopieringsoppdrag (7.2.2)

Følgende figurer eksisterer allerede i analysen og skal kopieres inn / refereres fra rapporten. Ingen ny plotlogikk.

- Figur 5.1 – `fig_datatype_fordeling.png` fra aktivitet 01.
- Figur 5.2 – `fig_sales_fordeling_train_test.png` fra aktivitet 07.

### 7.2 Nye plotteskript (7.2.3)

Følgende fem figurer må produseres som nye `fig_*.png`. Skriptene legges i naturlig aktivitetsmappe og oppdaterer eksisterende `start_wbs_*.py`-struktur:

| Figur | Forslag til skript | Aktivitetsmappe |
|---|---|---|
| Figur 7.1 (bias per måned) | nytt plotteblokk i `start_wbs_6_1.py` | [16_tolke_modellresultater](../006%20analysis/aktiviteter/16_tolke_modellresultater/) |
| Figur 7.2 (RMSE per måned) | nytt plotteblokk i `start_wbs_5_2.py` | [13_rmse_og_mape](../006%20analysis/aktiviteter/13_rmse_og_mape/) |
| Figur 8.1 (samlet RMSE/MAPE) | nytt plotteblokk i `start_wbs_5_2.py` | [13_rmse_og_mape](../006%20analysis/aktiviteter/13_rmse_og_mape/) |
| Figur 8.2 (feature importance topp 10) | nytt plotteblokk i `start_wbs_5_4.py` | [15_viktige_variabler](../006%20analysis/aktiviteter/15_viktige_variabler/) |
| Figur 8.3 (variabelgrupper topp 10) | nytt plotteblokk i `start_wbs_5_4.py` | [15_viktige_variabler](../006%20analysis/aktiviteter/15_viktige_variabler/) |

Stil: sentrert, `width="80%"` i rapporten, PNG-filene lagres med prefiks `fig_` i respektiv aktivitetsmappe (jf. [CLAUDE.md](../CLAUDE.md) og [006 analysis/README.md](../006%20analysis/README.md)).

### 7.3 Nye tabellutdrag (7.2.2 og 7.2.3)

Tabellene 5.2, 5.3, 5.4, 6.1, 6.2, 7.1, 7.2, 9.1, 9.2 og 9.3 limes inn som Markdown-tabeller i rapporten, basert på CSV-kildene. For tabeller med mange rader (f.eks. 5.2 med 12 rader, 7.2 som er et segmentutvalg) holdes presentasjonen kompakt (kun nøkkelkolonner) med full kildefil som referanse i teksten.

## 8 Artefakter som er valgt bort

| Artefakt | Begrunnelse for å holde utenfor rapporten |
|---|---|
| [tab_manglende_verdier.csv](../006%20analysis/aktiviteter/01_dataforstaelse_og_variabler/tab_manglende_verdier.csv) | Datasettet har ingen manglende verdier – poenget dekkes av én setning i kap. 5.2. |
| [tab_dataset_oversikt.csv](../006%20analysis/aktiviteter/01_dataforstaelse_og_variabler/tab_dataset_oversikt.csv), [tab_dataset_dokumentasjon.csv](../006%20analysis/aktiviteter/03_dokumentere_datasett/tab_dataset_dokumentasjon.csv) | Overlapper med Tabell 5.2; unngår duplikater. |
| [tab_variabelregler.csv](../006%20analysis/aktiviteter/02_identifisere_relevante_variabler/tab_variabelregler.csv), [fig_variabelanbefalinger.png](../006%20analysis/aktiviteter/02_identifisere_relevante_variabler/fig_variabelanbefalinger.png) | Beslutningsreglene er prosess-interne; sluttanbefalingen står i Tabell 5.2. |
| [tab_datakvalitet_etter_rens.csv](../006%20analysis/aktiviteter/04_dataprosessering/tab_datakvalitet_etter_rens.csv) | Dekkes av Tabell 5.4. |
| [tab_eda_oversikt.csv](../006%20analysis/aktiviteter/07_eksplorativ_analyse_og_visualisering/tab_eda_oversikt.csv), [tab_kategorisk_fordeling.csv](../006%20analysis/aktiviteter/07_eksplorativ_analyse_og_visualisering/tab_kategorisk_fordeling.csv) | Utdypende EDA – figurer i 4.1–4.4 dekker hovedbudskapene. |
| [tab_modelltrening_oversikt.csv](../006%20analysis/aktiviteter/10_felles_treningsoppsummering/tab_modelltrening_oversikt.csv), [tab_modellsignaler_oversikt.csv](../006%20analysis/aktiviteter/10_felles_treningsoppsummering/tab_modellsignaler_oversikt.csv) | Sammenstilt i Tabell 6.1 og Tabell 8.3. |
| [tab_lr_koeffisienter.csv](../006%20analysis/aktiviteter/08_lineaer_regresjon/tab_lr_koeffisienter.csv) | 41 rader – full versjon i vedlegg; topp signaler diskuteres i kap. 7. |
| [tab_rf_feature_importance.csv](../006%20analysis/aktiviteter/09_random_forest_regressor/tab_rf_feature_importance.csv) | Baseline-versjon; tuned-tabellen er relevant. Full versjon i vedlegg. |
| [tab_rf_tuning_kandidater.csv](../006%20analysis/aktiviteter/11_parameterjustering_random_forest/tab_rf_tuning_kandidater.csv) | 37 rader – for omfattende; topp 5 i Tabell 6.2, full versjon i vedlegg. |
| [tab_rf_stabilitet_topp10.csv](../006%20analysis/aktiviteter/15_viktige_variabler/tab_rf_stabilitet_topp10.csv), [tab_toppsignaler_per_modell.csv](../006%20analysis/aktiviteter/15_viktige_variabler/tab_toppsignaler_per_modell.csv), [tab_viktige_variabler_oversikt.csv](../006%20analysis/aktiviteter/15_viktige_variabler/tab_viktige_variabler_oversikt.csv) | Overlapper med Tabell 8.3 og Figur 8.1/8.3. |
| [tab_prognoser_2025_maaned.csv](../006%20analysis/aktiviteter/12_prognoser_2025/tab_prognoser_2025_maaned.csv), [tab_prognosemodeller_oversikt.csv](../006%20analysis/aktiviteter/12_prognoser_2025/tab_prognosemodeller_oversikt.csv) | Innholdet fremstår indirekte gjennom Figur 7.1/7.2 og Tabell 7.1. |
| [tab_prognoser_2025_detalj.csv](../006%20analysis/aktiviteter/12_prognoser_2025/tab_prognoser_2025_detalj.csv), [tab_prognosefeil_2025_detalj.csv](../006%20analysis/aktiviteter/13_rmse_og_mape/tab_prognosefeil_2025_detalj.csv) | 3 312 rader – klart vedleggsmateriale. |
| [tab_rmse_mape_maaned.csv](../006%20analysis/aktiviteter/13_rmse_og_mape/tab_rmse_mape_maaned.csv) lang form | Pivot-versjonen går inn som Tabell 7.1; lang form er utgangsdata. |
| [tab_modellsammenligning_oversikt.csv](../006%20analysis/aktiviteter/14_sammenligne_modellresultater/tab_modellsammenligning_oversikt.csv), [tab_maanedlige_modellvinnere.csv](../006%20analysis/aktiviteter/14_sammenligne_modellresultater/tab_maanedlige_modellvinnere.csv) | Dekkes av Tabell 8.2 og Figur 7.2 kombinert. |
| [tab_bias_maaned_modell.csv](../006%20analysis/aktiviteter/16_tolke_modellresultater/tab_bias_maaned_modell.csv) | Brukes som data til Figur 7.1; ikke som egen tabell i rapporten. |
| [tab_segmentvinnere_tolkning.csv](../006%20analysis/aktiviteter/16_tolke_modellresultater/tab_segmentvinnere_tolkning.csv) | Tilsvarer Tabell 8.4 i rapporten. |
| [tab_diskusjonspunkter_oversikt.csv](../006%20analysis/aktiviteter/17_styrker_og_svakheter/tab_diskusjonspunkter_oversikt.csv) | Brukes som tekstkilde i kap. 9, ikke som egen tabell. |

## 9 Vedleggsliste – stort datamateriale (kap. 12)

Kapittel 12 Vedlegg i rapporten skal ifølge lærerens formkrav bære stort eller detaljert datamateriale. 7.2.4 skal legge inn følgende referanseliste i kap. 12:

| Vedleggs-ID | Innhold | Kildefil |
|---|---|---|
| A1 | Radvise prognoser for 2025 for alle tre modeller (3 312 rader) | [tab_prognoser_2025_detalj.csv](../006%20analysis/aktiviteter/12_prognoser_2025/tab_prognoser_2025_detalj.csv) |
| A2 | Radvise prognosefeil og absoluttfeil for 2025 | [tab_prognosefeil_2025_detalj.csv](../006%20analysis/aktiviteter/13_rmse_og_mape/tab_prognosefeil_2025_detalj.csv) |
| A3 | Full tuning-kandidatgrid for Random Forest | [tab_rf_tuning_kandidater.csv](../006%20analysis/aktiviteter/11_parameterjustering_random_forest/tab_rf_tuning_kandidater.csv) |
| A4 | Full feature importance for tuned Random Forest | [tab_rf_tuned_feature_importance.csv](../006%20analysis/aktiviteter/15_viktige_variabler/tab_rf_tuned_feature_importance.csv) |
| A5 | Full koeffisienttabell for lineær regresjon | [tab_lr_koeffisienter.csv](../006%20analysis/aktiviteter/08_lineaer_regresjon/tab_lr_koeffisienter.csv) |
| A6 | Full RMSE/MAPE per måned i lang form | [tab_rmse_mape_maaned.csv](../006%20analysis/aktiviteter/13_rmse_og_mape/tab_rmse_mape_maaned.csv) |
| A7 | Full segmentmetrikk per modell | [tab_segmentmetrikk_modell.csv](../006%20analysis/aktiviteter/16_tolke_modellresultater/tab_segmentmetrikk_modell.csv) |

Filene limes ikke inn i rapporten. Vedlegget refererer til relativ sti i repoet, slik at leseren/sensor kan åpne full versjon direkte i analysemappen. Referanselisten presenteres i rapporten som **Tabell 12.1** med sentrert kursiv tabelltittel, slik at formalia er konsistent med øvrige kapitler.

## 10 Sporbarhet til analyseaktiviteter

| Kapittel i rapport | Figurer/Tabeller | Hovedkilde i WBS |
|---|---|---|
| Kap. 4 Casebeskrivelse | Figur 4.1–4.3 | WBS 3.4 (aktivitet 07) |
| Kap. 5 Metode og data | Figur 5.1–5.2; Tabell 5.2–5.5 | WBS 2.2, 2.3, 3.1, 3.2, 3.3, 3.4 (aktivitet 01, 02, 04, 05, 06, 07) |
| Kap. 6 Modellering | Tabell 6.1–6.2 | WBS 4.1, 4.2, 4.4 (aktivitet 08, 09, 11) |
| Kap. 7 Analyse | Figur 7.1–7.2; Tabell 7.1–7.2 | WBS 5.2, 6.1 (aktivitet 13, 16) |
| Kap. 8 Resultat | Figur 8.1–8.3; Tabell 8.1–8.4 | WBS 5.2, 5.3, 5.4, 6.1 (aktivitet 13, 14, 15, 16) |
| Kap. 9 Diskusjon | Tabell 9.1 (§9.1), Tabell 9.2 (§9.3), Tabell 9.3 (§9.4) | WBS 6.2, 6.3 (aktivitet 17, 18) |
| Kap. 12 Vedlegg | Tabell 12.1 (A1–A7) | WBS 4.1, 4.4, 5.1, 5.2, 5.4, 6.1 |

## 11 Sammendrag av utvalget

- **Figurer i rapporten:** 12 totalt. 5 beholdes fra dagens rapport (inkl. 2 forsidebilder), 2 kopieres inn fra eksisterende analyse-PNG, 5 produseres som nye plott.
- **Tabeller i rapporten:** 16 innholdstabeller (forside- og personverntabeller regnes ikke med her). 5 beholdes fra tidligere rapport (Tabell 5.5 renummerert fra 5.1 og Tabell 8.1–8.4), 10 legges inn i 7.2.2 (kap. 5: 5.2, 5.3, 5.4) og 7.2.3 (kap. 6, 7, 9: 6.1, 6.2, 7.1, 7.2, 9.1, 9.2, 9.3), og i tillegg Tabell 12.1 med vedleggsreferanser A1–A7 i kap. 12.
- **Kilder:** alle egenproduserte – ingen kildehenvisning skal oppgis i figur- eller tabelltekst.
- **Vedlegg:** 7 referanseoppføringer (A1–A7) samlet i Tabell 12.1. Kildefilene limes ikke inn; kun refereres via relativ sti.

## 12 Plan-glidning som må håndteres

Gantt-plan legger 7.2.1 på 2026-04-15 og 7.2.2 på 2026-04-16–17, 7.2.3 på 2026-04-18–19 og 7.2.4 på 2026-04-20. Utvalgsdokumentet fastsetter i praksis 10 nye tabeller og 5 nye plott, som er mer enn Gantt forutsatte da planen ble etablert. Dette må håndteres i [endringslogg.md](endringslogg.md) når 7.2-blokken faktisk lukkes, og Gantt oppdateres med realistiske datoer. Planglidningen registreres ikke her – dokumentet beskriver bare omfanget.
