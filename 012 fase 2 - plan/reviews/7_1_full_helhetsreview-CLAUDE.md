# Helhetsreview av WBS 7.1 – Rapportkapitler og dokumentasjon

**Reviewer:** Claude (automatisk helhetsreview)
**Dato:** 2026-04-16
**Omfang:** Sammendrag, Abstract, §1–§12 i `005 report/rapport.md` (480 linjer)
**Planreferanse:** WBS 7.1.1–7.1.7 (alle fullført 2026-04-13 til 2026-04-16)

Denne reviewen er en tverr-kapittel-vurdering som bygger på og ikke duplikerer de syv delreviewene av 7.1.1–7.1.7. Fokus er helhetskonsistens, flyt, tverr-referanser, duplisering og tallintegritet på tvers av rapportens deler.

**Forutgående delreviewer:**

- [7_1_innledning_litteratur_casebeskrivelse-CLAUDE.md](7_1_innledning_litteratur_casebeskrivelse-CLAUDE.md) (7.1.1–7.1.3)
- [7_1_4_metode_og_data-CLAUDE.md](7_1_4_metode_og_data-CLAUDE.md) (7.1.4)
- [7_1_5_modellering_analyse_resultat-CLAUDE.md](7_1_5_modellering_analyse_resultat-CLAUDE.md) (7.1.5)
- [7_1_6_diskusjon_konklusjon_sammendrag-CLAUDE.md](7_1_6_diskusjon_konklusjon_sammendrag-CLAUDE.md) (7.1.6)
- [7_1_7_ferdigstille_innledning-CLAUDE.md](7_1_7_ferdigstille_innledning-CLAUDE.md) (7.1.7)

---

## Sammendrag

Rapportens syv skrivefaser er lukket med gjennomgående styrker i faglig presisjon, tallkonsistens og struktursamsvar med CLAUDE.md. Helhetsreviewen avdekker én middels svakhet (tolkningsbruk av `Region_North`-koeffisient som er basert på én observasjon, uten nyansering), to lave svakheter som gjelder dokumentformalia (§12 Vedlegg tom, forsideplaceholders ikke utfylt), én lav kapitaliseringsinkonsistens («Tuned»/«tuned» Random Forest) og ett lavt forbedringsforslag om å fylle §12 Vedlegg med supplerende materiale. Ingen blokkerende feil.

**Totalt:** 8 styrker, 4 svakheter (0 Høy, 1 Middels, 3 Lav), 3 forbedringsforslag (Lav).

---

## Styrker (tverr-kapittel)

- **S1.** Rapportstrukturen følger CLAUDE.md-malen fullt ut: forside → erklæringer → Sammendrag → Abstract → innhold → kap. 1 Innledning → kap. 2 Litteratur → kap. 3 Teori → kap. 4 Casebeskrivelse → kap. 5 Metode og data → kap. 6 Modellering → kap. 7 Analyse → kap. 8 Resultat → kap. 9 Diskusjon → kap. 10 Konklusjon → kap. 11 Bibliografi → kap. 12 Vedlegg. Underkapittelstruktur (1.1–1.4, 3.1–3.4, 4.1–4.4, 5.1–5.2, 9.1–9.5) er konsistent og fyllestgjørende.
- **S2.** Tallkonsistens verifisert på tvers av Sammendrag (linje 99–103), Abstract (linje 107–111), kap. 5.2 (linje 324–335), kap. 6 (linje 345–347), kap. 7 (linje 353–361), kap. 8 (tabell 8.1–8.4), kap. 9.1–9.2 (linje 431–439) og kap. 10 (linje 463–465): 9 994 rader, 6 682/3 312 split, 67 features, RMSE 578,26, MAPE 43,97 %, «11 av 12 måneder», «13 av 14 segmenter», `Discount` 11,48 %, kalender ~42 %. Alle tallpåstander er sporbare til analyseartefakter (`tab_rmse_mape_oversikt.csv`, `tab_rf_tuned_feature_importance.csv`, `tab_modellvinner_telling.csv`, `tab_segmentvinnere_tolkning.csv`, `tab_split_oversikt.csv`, `tab_lr_koeffisienter.csv`).
- **S3.** Tverr-referanser mellom kapitler er korrekte: kap. 5.1 refererer til kap. 3.3 for metrikkbegrunnelse, kap. 6 refererer til kap. 3.1, 3.2, 3.4 og 5.2 for teori og datagrunnlag, kap. 7 refererer til Tabell 8.1–8.4, kap. 9.3 refererer tilbake til 9.1 og 9.2. Ingen broken referanser.
- **S4.** Figurer og tabeller følger CLAUDE.md-mønster uten avvik: alle figurer bruker HTML-blokk med `width="80%"`, sentrert justering og kursiv figurtekst i `<small>`-taggen. Alle tabeller har `<p align="center"><small><i>Tabell X.Y …</i></small></p>` som tekst.
- **S5.** Inline matte bruker `$...$`-notasjon konsekvent (verifisert i kap. 3.1, 3.3, 6, 7, 9.1, 9.2, 10). Ingen `\(...\)`-forekomster.
- **S6.** Inline-kode-konvensjonen for variabelnavn er forankret i en notasjonsboks i kap. 3 (linje 203) som dekker hele dokumentet. Boksen forklarer eksplisitt at Sammendrag og Abstract bruker prosa for tilgjengelighet, mens brødteksten bruker inline kode for modellfeatures. Samlebegrepet «forklaringsvariabel» og synonymene «prediktor», «signal», «feature» er dokumentert etter F5-tilføyelsen i 7.1.7.
- **S7.** Problemstillingens to delproblemer (§1.2) speiles nøyaktig i kap. 9.1 «det første delproblemet» (linje 433) og kap. 9.2 «det andre delproblemet» (linje 437), og besvares i kap. 10. Etter F1-harmoniseringen i 7.1.7 er terminologien «delproblem» konsekvent fra §1.2 og gjennom kap. 9 og 10.
- **S8.** Rapportflyten er logisk progresjon uten sprang: motivasjon og problemstilling (kap. 1) → faglig grunnlag (kap. 2–3) → caseforankring (kap. 4) → metodevalg og datagrunnlag (kap. 5) → konkret modellspesifikasjon (kap. 6) → analyse av resultater (kap. 7) → rå resultater i tabellform (kap. 8) → differensiert diskusjon (kap. 9) → direkte svar på problemstillingen (kap. 10). Overgangen fra «best samlet» til «men heterogent på tvers av måneder og segmenter» er særlig godt håndtert i 9.1.

---

## Del 1 – Metodikk (tverr-kapittel tallintegritet)

### 1.1 Nøkkeltall-matrise

Matrisen nedenfor viser at hovedtallene presenteres identisk på tvers av rapportens deler og samsvarer med analyseartefaktene:

| Tall | Sammendrag | Abstract | §5.2/Tab 5.1 | §6 | §7 | §8 | §9 | §10 | Kilde |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| 9 994 rader | ✓ L101 | ✓ L109 | ✓ L324 | — | — | — | — | — | `dataset_dokumentasjon.md` |
| 6 682 trening | ✓ L101 | ✓ L109 | ✓ Tab 5.1 | ✓ L345 | — | — | — | — | `tab_split_oversikt.csv` |
| 3 312 test | ✓ L101 | ✓ L109 | ✓ Tab 5.1 | ✓ L347 | — | ✓ L375 | — | — | `tab_split_oversikt.csv` |
| 67 features | ✓ L101 | ✓ L109 | ✓ L326 | ✓ L345 | — | — | — | — | `tab_lr_modelloversikt.csv` |
| RMSE 578,26 | ✓ L103 | ✓ L111 | — | — | — | ✓ Tab 8.1 | ✓ L431 | ✓ L463 | `tab_rmse_mape_oversikt.csv` |
| MAPE 43,97 % | ✓ L103 | ✓ L111 | — | — | — | ✓ Tab 8.1 | ✓ L431 | ✓ L463 | `tab_rmse_mape_oversikt.csv` |
| 11 av 12 mnd | ✓ L103 | ✓ L111 | — | — | ✓ L355 | ✓ Tab 8.2 | ✓ L431 | ✓ L463 | `tab_modellvinner_telling.csv` |
| 13 av 14 segm | ✓ L103 | ✓ L111 | — | — | ✓ L359 | — | ✓ L463 | ✓ L463 | `tab_segmentvinnere_tolkning.csv` |
| `Discount` 11,48 % | ✓ L103 | ✓ L111 | — | — | ✓ L361 | ✓ Tab 8.3 | ✓ L437 | — | `tab_rf_tuned_feature_importance.csv` |
| Kalender ~42 % | ✓ L103 | ✓ L111 | — | — | ✓ L361 | — | ✓ L437 | ✓ L465 | `tab_variabelgrupper_tuned_top10.csv` |

**Vurdering:** Fullstendig konsistens. Alle hovedtall er sporbare til kildeartefakter.

### 1.2 Kryssjekk av sekundære tall

Verifisering av tall som kun opptrer i enkelte kapitler:

| Tall | Kapittel/linje | Kilde | Status |
|:---|:---|:---|:---|
| Treningsgj.snitt 1 493 / test 1 503 | §4.2 L282, §5.2 L330 | `tab_eda_oversikt.csv` | OK |
| Oktober høyest / juni lavest | §4.3 L293 | `eda_visualisering.md` | OK |
| Konstantledd lineær $-3193{,}55$ | §6 L345 | `tab_lr_modelloversikt.csv` | OK |
| Validerings-RMSE tuned $577{,}27$ | §6 L347 | `tab_rf_tuning_vinner.csv` | OK |
| Bias august $-5{,}22\%$ / september $-2{,}77\%$ | §7 L357, §9.1 L433 | `tab_bias_maaned_modell.csv` | OK |
| `Region_North` koeffisient $-277{,}20$ | §9.2 L439 | `tab_lr_koeffisienter.csv` (−277,199368) | Teknisk OK, men se V1 |
| `Region_East` 2,04 %, `Region_West` 1,91 %, `Region_Central` 1,84 % | Tab 8.3 | `tab_rf_tuned_feature_importance.csv` | OK |

**Vurdering:** Alle sekundærtall er numerisk korrekte. Eneste tolkningsspørsmål gjelder `Region_North`-koeffisienten (V1 nedenfor).

### 1.3 Krav-matrise (KR-001 til KR-007)

| Krav | Dekning i rapporten | Status |
|:---|:---|:---|
| KR-001 Salgsprognoser 2025 fra 2022–2024 | §1.2, §5.1, §6, §8 Tab 8.1 | OK |
| KR-002 Minst to modeller (LR + RF) | §1.1, §1.2, §1.3, §3.1, §3.2, §6 | OK |
| KR-003 MAPE og RMSE | §3.3, §5.1, §8 Tab 8.1–8.2 | OK |
| KR-004 Identifisere og rangere variabler | §1.2, §8 Tab 8.3, §9.2 | OK |
| KR-005 Dokumentert datagrunnlag | §4, §5.2 Tab 5.1 | OK |
| KR-006 Dokumentasjon av resultater og metodevalg | §3, §5, §6, §8, §9 | OK |
| KR-007 Tids- og ressursrammer | Prosessuelt, ikke rapportinnhold | N/A |

Alle innholdsmessige krav er oppfylt.

---

## Del 2 – Språk, innhold og figurer (tverr-kapittel)

### 2.1 Flyt og duplisering

Sammendrag og kap. 10 Konklusjon gjentar nødvendigvis hovedtallene (RMSE 578,26, 11/12, 13/14, Discount 11,48 %, kalender 42 %). Denne duplikasjonen er forventet og akseptabel: Sammendrag er en skannbar oppsummering, mens kap. 10 svarer direkte på problemstillingen med rollefordeling for de tre modellene. Strukturen avviker (Sammendrag: problem → data → funn; kap. 10: problem → svar → anbefaling), så gjentakelsen føles ikke påtrengende.

Mellom §1 Innledning (svinn/bundet kapital) og §4.4 (planleggingsrisiko knyttet til Dagligvares sortiment) er tidligere V3 (duplisering) løst i 7.1.3: §4.4 er nå kategorispesifikk og skiller seg fra innledningens generiske konsekvensbeskrivelse.

### 2.2 Terminologi på tvers

Etter F1 og F5 i 7.1.7 er terminologien harmonisert:
- «Delproblem» i §1.2, §9.1, §9.2 (konsistent).
- «Forklaringsvariabel» som samlebegrep, med «prediktor», «signal», «feature» som kontekstuelle synonymer (dokumentert i notasjonsboks, kap. 3).
- «Random Forest Regressor» (fullform) i §1.1 og §1.2; «Random Forest» som kortform etter introduksjon i resten av rapporten. Akseptabel praksis.

Kapitalisering av modellsnavn er derimot inkonsistent (se V3).

### 2.3 Figur- og tabellreferanser

Alle figur- og tabellreferanser i brødtekst er faglig korrekte og matcher overskriftstekst:

| Referanse | Mål | Status |
|:---|:---|:---|
| Figur 4.1 per kategori | §4.1 L273 → `fig_sales_per_category.png` | OK |
| Figur 4.2 over tid | §4.2 L284 → `fig_sales_over_tid_train_test.png` | OK |
| Figur 4.3 per måned | §4.3 L295 + §4.4 L306 → `fig_sales_per_month_split.png` | OK |
| Tabell 5.1 split | §5.2 L330 | OK |
| Tabell 8.1 samlet ytelse | §7 L353, §8 L367 | OK |
| Tabell 8.2 månedlig vinner | §7 L355, §8 L377 | OK |
| Tabell 8.3 feature importance | §7 L361, §8 L387 | OK |
| Tabell 8.4 segmentvinner | §7 L359, §8 L404 | OK |

Ingen broken figur- eller tabellreferanser.

### 2.4 Bibliografi

Kun fire kilder (IBM u.å.-a, IBM u.å.-b, GeeksforGeeks 2026a, GeeksforGeeks 2026b). Alle fire brukes aktivt i kap. 2 og 3. Begrensningen (ingen fagfellevurderte artikler) er eksplisitt dokumentert i §2 siste avsnitt og i §9.4. Dette er en åpen debattpunkt som ikke er en feil, men fortsatt F3 fra 7.1.1 (ikke lukket).

### 2.5 Forsideformalia

Forsidelementer er placeholders:
- Tittel (linje 1): «Tittel (norsk og/eller engelsk)» — ikke fylt ut.
- Forfatter(e) (linje 5), sidetall (linje 7), innleveringsdato (linje 9): tomme.
- Sjekkbokser i egenerklæring, personvern og publisering (linje 24–81): alle ☐ umerket.
- «Antall ord» (linje 89) og «Forfattererklæring» (linje 93): begge inneholder placeholder-tekst.

Disse er utenfor 7.1-scope (fokus på rapportkapitler), men må håndteres før innlevering. Se V4.

---

## Svakheter og forbedringsforslag (nye tverr-kapittel-funn)

### V1. `Region_North`-koeffisient tolkes uten nyansering av minimalt datagrunnlag

**Alvorlighetsgrad:** Middels
**Kategori:** Faglig innhold (tolkningsvaliditet)

**Observasjon:** §9.2 linje 439 sier: «De to variablene med størst tallverdi i koeffisientene er `Region_North` ($-277{,}20$) og `Discount` ($-166{,}35$).» Koeffisienten er numerisk korrekt ($-277{,}199368$ i `tab_lr_koeffisienter.csv`), men er basert på én enkelt observasjon. Dette er eksplisitt dokumentert i §5.2 linje 328: «North-regionen er representert med bare én observasjon og benyttes ikke som separat analysesegment.»

Konsekvens: En koeffisient estimert fra én observasjon har ekstremt lav presisjon og reflekterer sannsynligvis støy snarere enn en substansiell regionseffekt. Slik teksten står nå, kan leseren få inntrykk av at `Region_North` er en påvirkningsrik prediktor, mens i praksis er den en artefakt av datagrunnlagets skjevhet. Tolkningen i §9.2 trenger en kort kvalifisering.

**Forslag til formulering (for 7.3.3):** Bytt ut «størst tallverdi i koeffisientene er `Region_North` ($-277{,}20$) og `Discount` ($-166{,}35$)» med noe som «`Discount` ($-166{,}35$) er den variabelen med størst meningsfull tallverdi i koeffisientene; `Region_North`-koeffisienten ($-277{,}20$) er størst i absoluttverdi, men bygger på én enkelt observasjon (jf. §5.2) og bør tolkes som støy snarere enn en substansiell effekt.»

### V2. §12 Vedlegg er tom overskrift

**Alvorlighetsgrad:** Lav
**Kategori:** Rapportstruktur

**Observasjon:** Linje 479 har overskriften `## 12 Vedlegg` uten innhold. TOC-lenken (linje 143) peker til denne overskriften. Leseren som følger TOC-lenken lander på en tom seksjon.

**Forslag:** Enten (a) fyll §12 med supplerende materiale i 7.2.x (f.eks. utvidet feature importance-tabell, segmentdefinisjoner, tuning-kandidatmatrise), eller (b) legg til en kort note «Denne rapporten har ingen vedlegg.» eller (c) fjern §12 fra TOC og rapporten dersom vedlegg ikke skal inkluderes. Alternativ (a) er foretrukket siden prosjektet har mye supplerende analysemateriale.

### V3. Inkonsistent kapitalisering av modellnavn

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og stil

**Observasjon:** Kapitalisering av «Tuned Random Forest» / «tuned Random Forest» varierer:
- Tabell 8.1 (linje 373): «Tuned Random Forest» (stor T)
- Tabell 8.2 (linje 383): «Tuned Random Forest»
- Tabell 8.4 (linje 408–421): «Tuned RF» (kortform, stor T)
- Kap. 7 (linje 353, 355, 359, 361): «tuned Random Forest» (liten t)
- Kap. 9 (linje 431, 433, 437, 445): «tuned Random Forest» / «Tuned Random Forest» vekslende
- Kap. 10 (linje 463, 465): «tuned Random Forest»

Totalt 18 treff på `[Tt]uned [Rr]andom [Ff]orest`. Samme mønster for «Benchmark lineær» / «benchmark lineær» og «Baseline Random Forest» / «baseline Random Forest».

**Forslag:** Håndteres i 7.3.3 språkvask. Foretrukken praksis er liten forbokstav i brødtekst (modellrollen er en klassebeskrivelse, ikke et egennavn), og stor forbokstav kun i kolonneoverskrifter, tabellceller og kapittelstartsetninger.

### V4. Forsideplaceholders ikke utfylt

**Alvorlighetsgrad:** Lav
**Kategori:** Dokumentformalia

**Observasjon:** Tittel, forfattere, sidetall, innleveringsdato, egenerklæring, personvern, publiseringsavtale og «Antall ord»/«Forfattererklæring» er alle placeholders (linje 1–94).

**Forslag:** Utenfor 7.1-scope. Håndteres i slutten av 7.3.x eller i 8.1 (revisjon av rapport). Bør flagges som egen avkrysspunkt i sluttkvalitetssjekken.

### F1. Fyll §12 Vedlegg med relevant supplerende materiale

**Alvorlighetsgrad:** Lav
**Kategori:** Rapportstruktur

**Observasjon:** Prosjektet har mange detaljerte analyseartefakter som kan fungere som vedlegg:
- Full feature importance-tabell (utover topp 10 i Tabell 8.3), basert på `tab_rf_tuned_feature_importance.csv`
- Segmentdefinisjoner og grenser for rabattband og salgsnivå, basert på `tab_segmentdefinisjoner.csv`
- Tuning-kandidatmatrise med validerings-RMSE og MAPE, basert på `tab_rf_tuning_kandidater.csv`
- Månedlig prognosefeiltabell, basert på `tab_prognosefeil_2025_detalj.csv`

**Forslag:** Håndteres i 7.2.2 eller 7.2.3 når figurer og tabeller velges.

### F2. Vurder eksplisitt henvisning fra §9.2 til §5.2 om North-regionen

**Alvorlighetsgrad:** Lav
**Kategori:** Faglig innhold (navigerbarhet)

**Observasjon:** Relatert til V1. Hvis V1-kvalifiseringen implementeres, kan en eksplisitt tilbake-referanse («jf. §5.2 som dokumenterer at North-regionen har én observasjon») gjøre tolkningen sporbar uten at leseren må huske §5.2.

**Forslag:** Håndteres samtidig med V1 i 7.3.3.

### F3. Supplér bibliografien med minst én fagfellevurdert kilde

**Alvorlighetsgrad:** Lav
**Kategori:** Akademisk kvalitet

**Observasjon:** Begrensningen er dokumentert, men ikke fikset. Fire kilder (to IBM, to GeeksforGeeks) er alle webbaserte oppslagsverk. En eller to fagfellevurderte artikler om maskinlæring for etterspørselspredikering i detaljhandel vil styrke den akademiske tyngden.

**Forslag:** Håndteres i 7.3.3 dersom kravet om akademisk dybde prioriteres. Tidligere flagget i 7.1.1-review som F2.

---

## Avhukningsliste – tiltak

| # | Tiltak | Kategori | Status | Kommentar |
|:--|:-------|:---------|:-------|:----------|
| V1 | Nyansere `Region_North`-koeffisient i §9.2 med referanse til §5.2 | Faglig innhold | [x] | Utført 2026-04-16: §9.2 linje 439 omskrevet — `Discount` presenteres nå som størst meningsfull koeffisient, mens `Region_North`-koeffisienten er kvalifisert som usikker på grunn av én observasjon (jf. kap. 5.2) |
| V2 | Fylle eller fjerne §12 Vedlegg | Rapportstruktur | [ ] | Håndteres i 7.2.x eller 7.3.1 |
| V3 | Harmonisere kapitalisering av modellnavn | Språk og stil | [ ] | Håndteres i 7.3.3 |
| V4 | Fylle ut forsideplaceholders | Dokumentformalia | [ ] | Håndteres i 7.3.x eller 8.1 |
| F1 | Legg til supplerende vedleggsmateriale (kandidat: full FI-tabell, segmentdef., tuning-kandidatmatrise) | Rapportstruktur | [ ] | Håndteres i 7.2.2 eller 7.2.3 |
| F2 | Tilbakereferanse §9.2 → §5.2 for North | Faglig innhold | [x] | Utført 2026-04-16 sammen med V1: «jf. kap. 5.2» lagt inn i §9.2 |
| F3 | Supplér bibliografien med fagfellevurdert kilde | Akademisk kvalitet | [ ] | Håndteres i 7.3.3 |

Alle tidligere tiltak fra delreviewene (V1–V6 i 7.1.1; V1–V2 og F1–F3 i 7.1.6; V1, F1–F5 i 7.1.7) er dokumentert i respektive filer og refereres ikke på nytt her.

---

## Samsvar med prosjektplan og krav

| Sjekkpunkt | Status | Kommentar |
|:---|:---|:---|
| WBS 7.1.1–7.1.7 alle fullført | OK | Per 2026-04-16 |
| CLAUDE.md rapportstrukturmal fulgt | OK | Alle obligatoriske kapitler finnes, i riktig rekkefølge |
| Figurformat per CLAUDE.md | OK | Alle tre figurer i §4 bruker HTML-blokk 80 % sentrert |
| Tabellformat per CLAUDE.md | OK | Alle fem tabeller med kursiv sentrert tabelltekst |
| Inline matte `$...$` | OK | Ingen `\(...\)`-forekomster |
| Inline kode for modellfeatures | OK | Notasjonsboks i kap. 3 |
| Tallkonsistens på tvers av kapitler | OK | Se matrise 1.1 |
| Alle KR-001–KR-006 dekket | OK | Se matrise 1.3 |
| Delproblem-struktur speiles i diskusjon og konklusjon | OK | Etter F1-harmonisering i 7.1.7 |
| Forsidelementer utfylt | Ikke OK | V4, utenfor 7.1-scope |
| §12 Vedlegg har innhold | Ikke OK | V2, plan for 7.2.x |
| Bibliografi har fagfellevurderte kilder | Delvis | F3, åpent siden 7.1.1 |

---

## Samlet vurdering

### Metodikk

Tverr-kapittel tallintegritet er fullstendig verifisert: hovedtallene (9 994, 6 682, 3 312, 67, 578,26, 43,97 %, 11/12, 13/14, 11,48 %, ~42 %) er konsistente på tvers av Sammendrag, Abstract, kap. 5.2, 6, 7, 8, 9 og 10, og alle er sporbare til kildeartefakter i `006 analysis/aktiviteter/`. Sekundærtall (bias, koeffisienter, kalenderbidrag, validerings-RMSE) stemmer med underliggende CSV-filer. Eneste tolkningssvakhet er bruken av `Region_North`-koeffisienten i §9.2 uten nyansering av at den estimeres fra én observasjon (V1, Middels).

### Språk, innhold og figurer

Rapportens flyt er akademisk og logisk progresjon fra problem til konklusjon. Overgangene mellom kapitler er tydelige og uten gjentakelser utover det som er naturlig i Sammendrag/Konklusjon-paret. Tverr-kapittel-harmoniseringen gjennom F1 og F5 i 7.1.7 har etablert konsistent terminologi. Gjenværende lav-svakheter gjelder formaliteter (§12 tom, forsideplaceholders, kapitaliseringsvariasjon) som hører i 7.2-figurfasen og 7.3-kvalitetssikringen.

### Anbefalt prioritering videre (for 7.2 og 7.3)

1. **(Må)** V1 — Nyansere `Region_North`-koeffisient i §9.2 (håndteres i 7.3.3 språkvask og konsistenssjekk).
2. **(Bør)** V2 og F1 — Fyll §12 Vedlegg med supplerende materiale (håndteres i 7.2.2 eller 7.2.3 ved valg av figurer og tabeller).
3. **(Bør)** V3 — Harmoniser kapitalisering av modellnavn (håndteres i 7.3.3 språkvask).
4. **(Må før innlevering)** V4 — Fyll ut forsideplaceholders (håndteres i 7.3.x eller 8.1).
5. **(Kan)** F2 — Tilbakereferanse fra §9.2 til §5.2 for North.
6. **(Kan)** F3 — Supplér bibliografien med fagfellevurdert kilde.

WBS 7.1 vurderes samlet som **godkjent**. Ingen funn blokkerer overgangen til 7.2. De fire gjenstående svakhetene er alle kategorisert som 7.2/7.3/8-arbeid og har tydelig eierskap i den videre planen.
