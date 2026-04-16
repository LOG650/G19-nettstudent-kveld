# Review av aktivitet 7.1.5 – Modellering, analyse og resultat

**Reviewer:** Claude (automatisk review)
**Dato:** 2026-04-16
**Aktivitetsmappe:** `005 report/rapport.md` (kapittel 6, 7 og 8)
**Planreferanse:** WBS 7.1.5 (planlagt Fri 10.04.26 – Sat 11.04.26, fullført 2026-04-16, seks dager etter planlagt slutt)

---

## Sammendrag

Kapittel 6 (Modellering), 7 (Analyse) og 8 (Resultat) er skrevet og oppfyller de sentrale kravene til aktiviteten: WBS-referater er erstattet med akademisk prosa, alle tre modellspor er spesifisert med hyperparametere og treningsgrunnlag, analysen knytter metrikker, bias og feature importance til tolkbare mønstre, og resultatkapitlet leverer fire kjernetabeller med korte introsetninger. Alle tall er verifisert mot analyseartefaktene uten avvik. Det er funnet én språklig upresishet, to strukturelle ujevnheter som bør ryddes i 7.1.6/7.3, og tre mindre forbedringsforslag.

**Totalt:** 7 styrker, 5 svakheter (0 Høy, 3 Middels, 2 Lav), 4 forbedringsforslag (Lav).

---

## Styrker

- **S1.** Kap. 6 er omformulert fra WBS-sekvensielt referat til strukturert akademisk prosa i tre avsnitt (modellstrategi → lineær regresjon → Random Forest), uten WBS-nummer i brødtekst.
- **S2.** Alle hyperparametere og tall i kap. 6 er verifisert mot CSV-artefaktene: intercept $-3193{,}55$ fra `tab_lr_modelloversikt.csv`, baseline-parametrene fra `tab_rf_modelloversikt.csv` og tuning-vinneren fra `tab_rf_tuning_vinner.csv` (`rf_tune_30`: `n_estimators=400`, `max_depth=10`, `min_samples_leaf=4`, `max_features='sqrt'`, val-RMSE $577{,}26775$, val-MAPE $43{,}5554$).
- **S3.** Kap. 7 følger en naturlig progresjon: samlet modelloppførsel → månedsnivå → bias/sesongavvik → segment og variabler. Dette gir leseren en tydelig innsnevring fra grovt til detaljert.
- **S4.** Kap. 8 bruker fire kompakte kjernetabeller (8.1–8.4) med korte introsetninger og tabelltekst i HTML-format i tråd med [CLAUDE.md](/home/erikb/himolde/log650/G19-nettstudent-kveld/CLAUDE.md). Ingen TODO-plassholdere gjenstår.
- **S5.** RMSE-vs-MAPE-uenigheten på månedsnivå (samme vinner bare 2 av 12 måneder) er eksplisitt tolket og koblet til metrikkenes ulike vekting av lavvolum-observasjoner. Dette er faglig presist og sporbart.
- **S6.** Bias-tolkning i kap. 7 er eksplisitt merket som antagelse («en mulig forklaring er …»), i tråd med prosjektets regel om å skille antagelser fra verifiserte fakta.
- **S7.** Kap. 6 begrunner hvorfor begge Random Forest-variantene inngår (baseline måler tuning-gevinst, benchmark lineær gir tolkbart referansepunkt). Dette er faglig ryddig og kobler seg til kap. 3.2.

---

## Del 1 – Metodikk (beregninger og kode)

WBS 7.1.5 er en ren rapportskriveaktivitet. Del 1 vurderer faktisk korrekthet i tallmateriale og konsistens mellom rapport og analyseartefakter.

### 1.1 Konsistens rapport ↔ analyseartefakter – kap. 6

Kryssjekk av alle tallfestede påstander i kap. 6:

| Påstand i rapporten | Kilde | Status |
|:---|:---|:---|
| 6 682 treningsrader, 67 features | `tab_lr_modelloversikt.csv` og `tab_split_oversikt.csv` | ✓ |
| Intercept $-3193{,}55$ | `tab_lr_modelloversikt.csv`: $-3193{,}5519\ldots$ | ✓ |
| Baseline RF: `n_estimators=200`, `min_samples_leaf=1`, `max_features=1.0`, `bootstrap=True`, `random_state=42` | `tab_rf_modelloversikt.csv` | ✓ |
| Tuned RF-vinner: `n_estimators=400`, `max_depth=10`, `min_samples_leaf=4`, `max_features='sqrt'` | `tab_rf_tuning_vinner.csv` | ✓ |
| 2022–2023 (4 095 rader) som søketrening, 2024 (2 587 rader) som intern validering | `random_forest_tuning.md` og `tab_rf_tuned_modelloversikt.csv` | ✓ |
| 2025 testperiode 3 312 rader | `tab_rmse_mape_oversikt.csv` | ✓ |
| Val-RMSE $577{,}27$, val-MAPE $43{,}56\%$ | `tab_rf_tuning_vinner.csv`: $577{,}26775$, $43{,}5554$ | ✓ |
| Baseline val-RMSE $590{,}30$, val-MAPE $44{,}22\%$ | `tab_rf_tuning_vinner.csv`: $590{,}303874$, $44{,}2211$ | ✓ |

**Vurdering:** Fullstendig konsistens. Ingen faktiske feil.

### 1.2 Konsistens rapport ↔ analyseartefakter – kap. 7

| Påstand i rapporten | Kilde | Status |
|:---|:---|:---|
| Tuned RF best samlet: RMSE og MAPE | `tab_rmse_mape_oversikt.csv` | ✓ |
| ~11 RMSE-enheter bedre enn baseline, ~2 enheter bedre enn benchmark lineær | 589,28 − 578,26 = 11,02 og 580,39 − 578,26 = 2,13 | ✓ |
| Tuned RF RMSE-vinner 11/12 mnd, MAPE-vinner 3/12 | `tab_modellvinner_telling.csv` | ✓ |
| Baseline RF MAPE-vinner 6/12 | `tab_modellvinner_telling.csv` | ✓ |
| Samme vinner juli og september | `tab_maanedlige_modellvinnere.csv`: `samme_vinner=True` for 2025-07 og 2025-09 | ✓ |
| August bias $-5{,}22\%$ ($-20\,548$), september $-2{,}77\%$ ($-16\,334$) | `tab_bias_maaned_modell.csv` (tuned RF) | ✓ |
| November $+1{,}05\%$, desember $+2{,}36\%$ | `tab_bias_maaned_modell.csv` (tuned RF) | ✓ |
| Tuned RF vinner RMSE i alle 4 kvartaler, 3 rabattband, 4 regioner | `tab_segmentvinnere_tolkning.csv` | ✓ |
| Høyt salg: benchmark lineær RMSE $699{,}10$, MAPE $30{,}31\%$ | `tab_segmentvinnere_tolkning.csv`: $699{,}100729$, $30{,}3127$ | ✓ |
| Lavt salg MAPE $89{,}39\%$ | `tab_segmentvinnere_tolkning.csv`: $89{,}3929$ | ✓ |
| Kalender ~42 % av topp 10 | `tab_variabelgrupper_tuned_top10.csv`: $41{,}9826$ | ✓ |
| Discount $11{,}48\%$, regioner ~$5{,}8\%$ | `tab_variabelgrupper_tuned_top10.csv`: $11{,}4781$, $5{,}783$ | ✓ |
| LR Discount-koeffisient $-166{,}35$ | `tab_lr_koeffisienter.csv`: $-166{,}350024$ | ✓ |

**Vurdering:** Fullstendig konsistens. Ingen faktiske feil.

### 1.3 Konsistens rapport ↔ analyseartefakter – kap. 8

Tabellene er direkte uttrekk fra artefaktene:

| Tabell | Kilde | Status |
|:---|:---|:---|
| 8.1 Samlet 2025-ytelse | `tab_rmse_mape_oversikt.csv` | ✓ |
| 8.2 Månedlig vinnertelling | `tab_modellvinner_telling.csv` | ✓ |
| 8.3 Topp 10 feature importance | `tab_rf_tuned_feature_importance.csv` | ✓ |
| 8.4 Segmentvinnere | `tab_segmentvinnere_tolkning.csv` | ✓ |

**Vurdering:** Alle fire tabeller matcher kildene på to desimaler. Ingen avvik.

### Gjenstående metodiske observasjoner

- Baseline RF-beskrivelsen oppgir `max_features=1.0` direkte fra artefakten. Dette er sklearns internrepresentasjon for «alle features ved hver split», men kan misforstås som «én feature» av en leser som ikke kjenner sklearn-konvensjonen. Se V1.
- Kap. 9 (Diskusjon, pre-eksisterende) siterer «13 av 14 tolkingssegmenter» på RMSE, mens kap. 7 siterer «alle fire kvartaler, alle tre rabattband og alle fire regioner» (11 av 14). Begge er korrekte, men representerer ulik oppsummering av samme tall. Avviket krever en opprydding i kap. 9 under WBS 7.1.6. Se V3.

---

## Del 2 – Språk, innhold og figurer

### 2.1 Kap. 6 – Modellering

**Språk:** Ryddig akademisk prosa. Fagtermer (`LinearRegression`, `fit_intercept`, `n_estimators`, `max_depth`) er konsekvent merket med backticks. Setningslengden er innenfor rimelige rammer, men siste setning i avsnitt 3 er lang og innfører hele pipeline-tråden («retrenes … prognoser … grunnlaget»). Kan deles i to for bedre lesbarhet.

**Faglig innhold:** Modellstrategien er tydelig motivert. Begrunnelsen for tre spor (tolkbarhet + tuning-gevinst) er faglig solid. OLS er eksplisitt koblet til kap. 3.1. Én presisjonsutfordring: `max_features=1.0` står uforklart (se V1).

### 2.2 Kap. 7 – Analyse

**Språk:** Nyansert og presis. Overganger mellom avsnitt er glatte. Én upresishet: «vinner MAPE i halvparten av året» står rett ved siden av konkrete tall (11 av 12, 3 av 12) – konsistens krever «i 6 av 12 måneder». Se V2.

**Faglig innhold:** Tolkninger av RMSE-vs-MAPE-uenigheten og sesongbias er faglig solide. Segmentavsnittet er innholdsrikt (140+ ord) og kunne deles i to – ett om segmentvinnere, ett om feature importance – for bedre lesbarhet. Se F1. Den indirekte formuleringen «vinner RMSE i alle fire kvartaler, alle tre rabattband og alle fire regioner» utelater salgsnivå-dimensjonen i den generelle setningen og skaper en uoverensstemmelse med kap. 9. Se V3.

### 2.3 Kap. 8 – Resultat

**Språk:** Svært nøktern – hver tabell introduseres av én setning som beskriver hva tabellen viser. Ingen tolkning. Dette er akkurat det rapportmalen foreskriver.

**Faglig innhold:** Tabell 8.1 og 8.2 er komplette og direkte sporbare. Tabell 8.3 bruker norsk tusenskiller (komma) og prosenttegn konsistent. Tabell 8.4 viser bare vinnernavn, ikke selve metrikkverdiene – dette er en bevisst plan-avgjørelse («kompakt»), men betyr at tall som siteres i kap. 7 (RMSE $699{,}10$, MAPE $89{,}39\%$) ikke er gjengitt i kap. 8. Se F2.

### 2.4 Figurer – rapportklarhet

Aktiviteten produserer ingen figurer; dette er utsatt til WBS 7.2.3 per plan. Ingen vurdering.

### 2.5 Tabeller – konsistens og lesbarhet

Alle fire tabeller i kap. 8 er formatert som Markdown-tabeller med tabelltekst i HTML-kapsling (`<p align="center"><small><i>...</i></small></p>`) i tråd med [CLAUDE.md](/home/erikb/himolde/log650/G19-nettstudent-kveld/CLAUDE.md). Kolonneoverskriftene er tydelige og konsistente på norsk. Tabellnumre følger kapittelnummer (8.1–8.4). Tabellene har ikke eksplisitte kryssreferanser fra kap. 7, slik at leseren ikke alltid vet hvor tallene er dokumentert. Se F3.

### 2.6 Funn fra forrige review (7.1.4) som tilhører denne eller senere aktiviteter

Alle punkter fra 7.1.4-reviewen (V1–V4, F1) ble markert `[x] utført 2026-04-13` og gjelder ikke denne aktiviteten.

---

## Svakheter og forbedringsforslag

### V1. `max_features=1.0` uforklart i kap. 6

**Alvorlighetsgrad:** Lav
**Kategori:** Faglig presisjon

Kap. 6 oppgir baseline RF-parametere direkte fra artefakten, inkludert `max_features=1.0`. Dette er sklearns internrepresentasjon for «alle features ved hver split» (100 %). For en leser som ikke er fortrolig med sklearn kan dette se ut som «én feature per split», som ville vært en helt annen modellspesifikasjon. Kap. 3.2 definerer feature randomness, men sammenhengen er ikke gjort eksplisitt.

Anbefalt tiltak: Legg til en kort parentes, f.eks. «`max_features=1.0` (alle features vurderes ved hver split)», slik at overgangen til `'sqrt'` i tuned varianten blir tydelig som en bevisst reduksjon.

### V2. «Halvparten av året» stilt mot konkrete månedstall i samme avsnitt

**Alvorlighetsgrad:** Lav
**Kategori:** Språk

Kap. 7, avsnitt 2: «Baseline Random Forest vinner ikke en eneste måned på RMSE, men vinner MAPE i halvparten av året.» Uttrykket står rett ved siden av konkrete tellinger («11 av 12», «3 av 12»). Stilistisk inkonsistens.

Anbefalt tiltak: Endre til «vinner MAPE i 6 av 12 måneder».

### V3. Kap. 7 og kap. 9 oppsummerer segmentvinnere ulikt

**Alvorlighetsgrad:** Middels
**Kategori:** Intern rapportkonsistens

Kap. 7 (nyskrevet): «vinner RMSE i alle fire kvartaler, alle tre rabattband og alle fire regioner» – 11 av 14 segmenter, utelater salgsnivå-dimensjonen.
Kap. 9 (pre-eksisterende skisse): «vinner RMSE i 11 av 12 måneder og 13 av 14 tolkingssegmenter» – inkluderer salgsnivå (2 av 3 der).

Begge er tallmessig korrekte, men leseren må selv regne ut at 11 og 13 refererer til henholdsvis ulike universer. Kap. 9 skal uansett skrives om i WBS 7.1.6, men må da bringes i tråd med kap. 7 (enten ved å tilføye salgsnivå i kap. 7 eller ved å presisere i kap. 9). Dette er en arv fra skissen, ikke en feil introdusert i 7.1.5, men aktualiseres nå når kap. 7 står som ferdigskrevet tekst.

Anbefalt tiltak: Utsett til WBS 7.1.6. Avgjør da om kap. 7-setningen skal utvides med «(11 av 14 segmenter; utenfor dette vinner benchmark lineær i høyvolumssegmentet)», eller om kap. 9 skal omformuleres. Sistnevnte er det naturlige siden kap. 7 allerede behandler høyvolumssegmentet i neste setning.

### V4. Segmentavsnittet i kap. 7 er langt og pakker to tematiske enheter

**Alvorlighetsgrad:** Middels
**Kategori:** Lesbarhet

Kap. 7 avsnitt 4 (ca. 140 ord) dekker både segmentvinnere og feature importance. Disse to temaene har ulikt analytisk formål: segmenter viser hvor modellen vinner eller taper, mens feature importance forklarer hvorfor. Å holde dem i samme avsnitt gjør leseforløpet tyngre og gjør det vanskelig å sitere deler av analysen separat.

Anbefalt tiltak: Del i to avsnitt – først segmentvinnere + unntaket for høyt salg, deretter feature importance + lineær-RF-uenighet om `Discount`-fortegn.

### V5. Fraværende kryssreferanser fra kap. 7 til kap. 8-tabellene

**Alvorlighetsgrad:** Middels
**Kategori:** Rapportstruktur

Kap. 7 siterer konkrete tall (578,26; 589,28; 580,39; 11 av 12; 699,10; 89,39 %) uten å peke leseren til hvor tallene er dokumentert. Kap. 8 inneholder tabellene. I en ferdig rapport bør tolkning knyttes til presenterte funn gjennom eksplisitte referanser.

Anbefalt tiltak: Legg til «(jf. Tabell 8.1)» etc. på 3–4 sentrale steder i kap. 7.

---

### F1. Kryssreferanse fra kap. 6/7 til kap. 3.2

**Alvorlighetsgrad:** Lav
**Kategori:** Struktur og lesbarhet

Kap. 6 nevner bagging implisitt («et strukturert søk», «standardkonfigurasjon»), og kap. 7 nevner at tuning demper varians. Kap. 3.2 definerer begge mekanismene. En parentes «(se kap. 3.2)» i kap. 6 eller 7 ville koble metodebeskrivelsen til teoridelen på samme måte som det ble gjort for kap. 5.1 → kap. 3.3 i forrige review.

### F2. Supplement til Tabell 8.4 eller ny tabell med segmentmetrikker

**Alvorlighetsgrad:** Lav
**Kategori:** Rapportstruktur

Tabell 8.4 viser vinnernavn men ikke metrikkverdier. Kap. 7 siterer tall (RMSE $699{,}10$, MAPE $89{,}39\%$) som ikke er dokumentert i kap. 8. En liten ekstra tabell («Tabell 8.5: RMSE og MAPE per segment») ville øke sporbarheten. Alternativt kan Tabell 8.4 utvides med metrikkverdier, men det kan gjøre tabellen tyngre å lese. Plan-avgjørelsen var bevisst å holde Tabell 8.4 kompakt, og supplementet kan vurderes i WBS 7.2.1 (valg av figurer og tabeller).

### F3. Numerisk månedstabell som supplement

**Alvorlighetsgrad:** Lav
**Kategori:** Rapportstruktur

Tabell 8.2 teller bare vinnere. En supplerende tabell med månedlig RMSE og MAPE per modell (fra `tab_rmse_mape_maaned.csv`) ville gi direkte numerisk grunnlag for flere av kap. 7s påstander, særlig bias-avsnittet. Kan utsettes til WBS 7.2.1.

### F4. Tydeligere framheving av hvorfor 2025-data aldri berører modellutvelgelsen

**Alvorlighetsgrad:** Lav
**Kategori:** Faglig presisjon

Kap. 6 nevner kort: «slik at 2025-data aldri brukes i modellutvelgelsen». Dette er en viktig metodisk disiplin som forhindrer data leakage på tvers av tuning og evaluering. Kunne fremheves mer eksplisitt som en kvalitetsmekanisme – for eksempel i en egen setning som knytter seg til kap. 3.4 (data leakage) og kap. 5.2 (tidsbasert splitt).

---

## Avhukningsliste – tiltak

| # | Tiltak | Kategori | Status | Kommentar |
|:--|:-------|:---------|:-------|:----------|
| V1 | Presiser `max_features=1.0` i kap. 6 | Faglig presisjon | [x] | Utført 2026-04-16: lagt til «(dvs. at alle 67 features vurderes ved hver split)» |
| V2 | «halvparten av året» → «6 av 12 måneder» i kap. 7 | Språk | [x] | Utført 2026-04-16 |
| V3 | Bring kap. 9 i tråd med kap. 7 i segmentoppsummering | Intern rapportkonsistens | [ ] | Utsatt til WBS 7.1.6 |
| V4 | Del kap. 7 avsnitt 4 i to (segment + variabler) | Lesbarhet | [x] | Utført 2026-04-16: segment og feature importance skilt i to avsnitt |
| V5 | Legg til kryssreferanser fra kap. 7 til Tabell 8.1–8.4 | Rapportstruktur | [x] | Utført 2026-04-16: alle fire tabeller referert fra kap. 7 |
| F1 | Kryssreferanse kap. 6/7 → kap. 3.2 | Struktur | [x] | Utført 2026-04-16: kap. 6 og kap. 7 peker nå til kap. 3.2 |
| F2 | Supplerende tabell med RMSE/MAPE per segment | Rapportstruktur | [ ] | Vurderes i WBS 7.2.1 |
| F3 | Supplerende månedstabell (RMSE/MAPE per mnd) | Rapportstruktur | [ ] | Vurderes i WBS 7.2.1 |
| F4 | Tydeligere framheving av at 2025 ikke berører tuning | Faglig presisjon | [x] | Utført 2026-04-16: lagt til eksplisitt setning om datalekkasje med referanse til kap. 3.4 og 5.2 |

---

## Samsvar med prosjektplan og krav

| Sjekkpunkt | Status | Kommentar |
|:---|:---|:---|
| WBS 7.1.5 fullført: modellering, analyse og resultat | OK | Fullført 2026-04-16, seks dager etter planlagt slutt |
| Kap. 6 beskriver modellvalg, spesifikasjon og estimeringsopplegg uten WBS-referanser | OK | |
| Kap. 7 beskriver modelloppførsel, residualer, prognoseegenskaper og tolkning | OK | Bias dekker residualperspektivet |
| Kap. 8 presenterer resultater ryddig med tabeller og kort forklaring | OK | Figurer utsatt til WBS 7.2.3 per plan |
| Alle tall verifisert mot analyseartefakter | OK | Se Del 1 |
| KR-002 (to modeller evaluert) | OK | LR + RF baseline + RF tuned dekker kravet |
| KR-003 (RMSE og MAPE dokumentert) | OK | Tabell 8.1, 8.2 og kap. 7 |
| KR-004 (variabelrangering) | OK | Tabell 8.3 |
| KR-006 (resultater, metodevalg og forutsetninger dokumentert) | OK | Kap. 6 + kap. 8 |
| Ingen TODO-plassholdere i kap. 6, 7, 8 | OK | |
| Tabelltekst i HTML-format per CLAUDE.md | OK | `<p><small><i>…</i></small></p>` |
| Ingen WBS-numre i rapportbrødtekst i kap. 6, 7, 8 | OK | (Kap. 9 har pre-eksisterende WBS-referanser som ryddes i WBS 7.1.6) |
| Antagelser eksplisitt merket | OK | «En mulig forklaring er …» i bias-avsnittet |

---

## Samlet vurdering

### Metodikk

Kap. 6, 7 og 8 er faglig korrekte. Alle tall er verifisert mot artefaktene uten avvik. Modellspesifikasjon, hyperparametere og tuning-opplegg er gjengitt presist. Den eneste metodiske presisjonsmerknaden er at `max_features=1.0` bør forklares som «alle features» for lesere uten sklearn-bakgrunn.

### Språk, innhold og figurer

Teksten er akademisk og fri for WBS-referater. Strukturen er logisk og følger rapportmalen. Hoveutfordringene er mindre lesbarhetspunkter: én stilistisk upresishet («halvparten av året»), ett langt avsnitt som bør deles, og manglende kryssreferanser fra kap. 7 til kap. 8-tabellene. Ingen av disse er faktiske feil. Kap. 9 har pre-eksisterende uoverensstemmelse med kap. 7 i segmentoppsummeringen (11 vs. 13) som må ryddes i WBS 7.1.6.

### Anbefalt prioritering videre

1. ~~**(Bør)** Del kap. 7 avsnitt 4 i to for bedre lesbarhet (V4)~~ – utført 2026-04-16
2. ~~**(Bør)** Legg til kryssreferanser fra kap. 7 til Tabell 8.1–8.4 (V5)~~ – utført 2026-04-16
3. **(Bør)** Bring kap. 9-segmentoppsummeringen i tråd med kap. 7 under WBS 7.1.6 (V3)
4. ~~**(Kan)** Presiser `max_features=1.0` i kap. 6 (V1)~~ – utført 2026-04-16
5. ~~**(Kan)** Endre «halvparten av året» til «6 av 12 måneder» (V2)~~ – utført 2026-04-16
6. ~~**(Kan)** Kryssreferanse kap. 6/7 → kap. 3.2 (F1)~~ – utført 2026-04-16
7. **(Kan)** Supplerende tabeller for segment og måned – avgjøres i WBS 7.2.1 (F2, F3)
8. ~~**(Kan)** Tydeligere framheving av at 2025 er isolert fra tuning (F4)~~ – utført 2026-04-16
