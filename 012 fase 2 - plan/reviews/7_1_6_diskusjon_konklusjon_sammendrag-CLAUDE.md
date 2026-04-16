# Review av aktivitet 7.1.6 – Diskusjon, konklusjon, sammendrag, abstract og bibliografi

**Reviewer:** Claude (automatisk review)
**Dato:** 2026-04-16
**Aktivitetsmappe:** `005 report/rapport.md` (Sammendrag, Abstract, kapittel 9, 10 og 11)
**Planreferanse:** WBS 7.1.6 (planlagt Sun 12.04.26 – Mon 13.04.26, fullført 2026-04-16, tre dager etter planlagt slutt)

---

## Sammendrag

Kapittel 9 Diskusjon er reorganisert fra praktisk-nytte-skisse til strukturert akademisk diskusjon med fem underkapitler (9.1–9.5), kapittel 10 Konklusjon er utvidet til et direkte tosvars-respons på problemstillingen, og Sammendrag og Abstract er skrevet fra bunnen av innenfor lengdemålet 250–300 ord. Konsistensen mellom kap. 7 og analyseartefaktene er rettet ved at segmentantallet nå oppgis som «13 av 14» inkludert salgsnivå. Alle tallfestede påstander i nye tekster er verifisert mot analyseartefaktene uten avvik.

**Totalt:** 6 styrker, 2 svakheter (0 Høy, 1 Middels, 1 Lav), 3 forbedringsforslag (Lav).

---

## Styrker

- **S1.** Kap. 9 er reorganisert fra praktisk-nytte-skisse til akademisk prosa i fem underkapitler (9.1 Tolkning mot problemstilling, 9.2 Variablenes påvirkning, 9.3 Praktisk nytte for Dagligvare, 9.4 Metodiske begrensninger, 9.5 Videre arbeid) uten WBS-numre i brødtekst.
- **S2.** Alle tall i 9.x, 10, Sammendrag og Abstract er verifisert mot analyseartefaktene: RMSE 578,26 / MAPE 43,97 % fra `tab_rmse_mape_oversikt.csv`, deltaer (−2,13 RMSE, −0,21 pp MAPE) er korrekt utregnet, 11/12 måneder og 13/14 segmenter stemmer med `tab_modellvinner_telling.csv` og `tab_segmentvinnere_tolkning.csv`, og Discount 11,48 % samt kalender ~42 % er konsistent med `tab_variabelgrupper_tuned_top10.csv`.
- **S3.** Segmentkonsistens mellom kap. 7 og analyseartefaktene er rettet: kap. 7 ([rapport.md:332](../../005 report/rapport.md#L332)) beskriver nå «13 av 14 tolkningssegmenter – alle fire kvartaler, alle tre rabattband, alle fire regioner og to av tre salgsnivå», noe som stemmer med tellingen i Tabell 8.4 (4+3+4+2 = 13).
- **S4.** Kapittel 10 Konklusjon svarer eksplisitt på begge delspørsmålene i problemstillingen: først modellvalget med anbefaling for de tre bruksrollene, deretter variablenes påvirkning med kjerneforbehold om prediktivt ikke-kausalt rammeverk.
- **S5.** Sammendrag (277 ord) og Abstract (298 ord) ligger begge innenfor målet 250–300 ord, dekker problem, datagrunnlag, metode, hovedfunn, variabler og praktisk anbefaling i samme rekkefølge, og bruker konsistente tall på begge språk.
- **S6.** Kap. 9.2 kontrasterer eksplisitt lineær regresjons `Discount`-koeffisient ($-166{,}35$) mot Random Forests positive feature importance ($11{,}48\%$) og tolker forskjellen som ikke-lineær eller interaksjonssammenheng, i tråd med det reviewene av kap. 7 har pekt på som et diskusjonspunkt.

---

## Del 1 – Metodikk (beregninger og kode)

WBS 7.1.6 er en ren rapportskriveaktivitet. Del 1 vurderer faktisk korrekthet i tallmateriale og konsistens mellom rapport og analyseartefakter.

### 1.1 Konsistens rapport ↔ analyseartefakter – kap. 9

Kryssjekk av alle tallfestede påstander i kap. 9:

| Påstand i rapporten | Kilde | Status |
|:---|:---|:---|
| Tuned RF RMSE 578,26, MAPE 43,97 % | `tab_rmse_mape_oversikt.csv` | ✓ |
| Delta vs. benchmark lineær: −2,13 RMSE, −0,21 pp MAPE | 580,3943 − 578,2596 = 2,1347; 44,1840 − 43,9706 = 0,2134 | ✓ |
| Tuned RF RMSE-vinner 11/12 mnd, MAPE-vinner 3/12 | `tab_modellvinner_telling.csv` | ✓ |
| Baseline RF MAPE-vinner 6/12 | `tab_modellvinner_telling.csv` | ✓ |
| August bias $-5{,}22\%$, september $-2{,}77\%$ | `tab_bias_maaned_modell.csv` | ✓ |
| November $+1{,}05\%$, desember $+2{,}36\%$ | `tab_bias_maaned_modell.csv` | ✓ |
| Discount 11,48 %, dayofmonth 11,35 %, weekofyear 10,40 %, month 6,74 %, dayofweek 6,52 % | `tab_rf_tuned_feature_importance.csv` | ✓ |
| Kalender ~42 % av topp 10, region 5,8 % | `tab_variabelgrupper_tuned_top10.csv`: 41,9826; 5,783 | ✓ |
| Baseline RF og tuned RF deler 9 av 11 features i topp 10 | `tab_rf_stabilitet_topp10.csv` | ✓ |
| LR Discount-koeffisient $-166{,}35$, Region_North $-277{,}20$ | `tab_lr_koeffisienter.csv`: $-166{,}350024$, $-277{,}199368$ | ✓ |

**Vurdering:** Fullstendig konsistens. Ingen faktiske feil i kap. 9.

### 1.2 Konsistens rapport ↔ analyseartefakter – kap. 10

| Påstand i rapporten | Kilde | Status |
|:---|:---|:---|
| Tuned RF RMSE 578,26, MAPE 43,97 % | `tab_rmse_mape_oversikt.csv` | ✓ |
| 11 av 12 måneder på RMSE, 13 av 14 segmenter | `tab_modellvinner_telling.csv`, `tab_segmentvinnere_tolkning.csv` | ✓ |
| Benchmark lineær best i høyt-salg-segment | `tab_segmentvinnere_tolkning.csv` | ✓ |
| Discount sterkeste signal, kalender ~42 % av topp 10 | `tab_variabelgrupper_tuned_top10.csv` | ✓ |

**Vurdering:** Fullstendig konsistens. Ingen faktiske feil i kap. 10.

### 1.3 Konsistens rapport ↔ analyseartefakter – Sammendrag og Abstract

Sammendrag og Abstract bruker samme tallsett som kap. 9 og 10:

- 9 994 salgstransaksjoner → `dataset_dokumentasjon.md` ✓
- 6 682 treningsrader, 3 312 testrader → `tab_split_oversikt.csv` ✓
- 67 features → `tab_lr_modelloversikt.csv` ✓
- RMSE 578,26 / MAPE 43,97 %, 11/12 mnd, 13/14 segmenter → som i 1.1 ✓
- Discount 11,48 %, kalender ~42 % → som i 1.1 ✓

**Vurdering:** Fullstendig konsistens. Ingen faktiske feil.

### 1.4 Segmentfiks i kap. 7

Før fiksen: kap. 7 omtalte tuned RF som vinner i «alle fire kvartaler, alle tre rabattband og alle fire regioner» (11 av 14). Etter fiksen: «13 av 14 tolkningssegmenter – alle fire kvartaler, alle tre rabattband, alle fire regioner og to av tre salgsnivå». Telling mot Tabell 8.4: Kvartal 4/4, Rabatt 3/3, Region 4/4, Salgsnivå 2/3 (Lavt salg og Middels salg til Tuned RF; Høyt salg til Benchmark lineær) = 13 av 14. Konsistent med analyseartefakten `tab_segmentvinnere_tolkning.csv`.

**Vurdering:** Konsistensfeil er rettet.

---

## Del 2 – Språk, innhold og figurer

### 2.1 Rapporttekst – kap. 9 Diskusjon

**Språk:** Akademisk prosa i hele kapitlet. Setningslengde er variert, faguttrykk brukes presist (feature importance, bias-mønster, multikollinearitet, datalekkasje). Ingen WBS-numre i brødtekst. Inline kode brukes konsistent for variabelnavn (`Discount`, `Region_North`, `dayofmonth` osv.).

**Faglig innhold:** 9.1 leverer en differensiert tolkning av modellvalget der «best samlet» brytes opp mot månedlig MAPE-heterogenitet. 9.2 kobler variabelrangeringer til tolkningen, ikke bare lister dem. 9.3 beholder de fire praktiske bruksområdene, men strammet inn som akademisk prosa som refererer til 9.1 og 9.2 i stedet for å gjenta tall. 9.4 dokumenterer seks metodiske begrensninger og nevner planendringen for Random Forest-tuning. 9.5 foreslår fire typer videre arbeid koblet til de identifiserte begrensningene.

### 2.2 Rapporttekst – kap. 10 Konklusjon

**Språk:** To avsnitt, begge under 150 ord, faglig presis prosa. Ingen WBS-numre.

**Faglig innhold:** Første avsnitt besvarer det første delspørsmålet med modellvalg og rollefordeling (tuned RF som standard, benchmark lineær som forklaringsstøtte og toppbelastningssupplement, baseline RF som MAPE-kontroll). Andre avsnitt besvarer det andre delspørsmålet med rabatt og kalender som viktigste prediktorer, regionsignaler som sekundære, og avsluttes med prediktivt-ikke-kausalt-forbeholdet.

### 2.3 Rapporttekst – Sammendrag og Abstract

**Språk:** Sammendraget er på korrekt norsk med æ/ø/å bevart. Abstract er på engelsk med fagterminologi (grid search, feature importance, time-based split, data leakage). Begge holder lengdemålet (277 / 298 ord).

**Faglig innhold:** Begge dekker seks elementer i samme rekkefølge: problem/relevans, datagrunnlag, metodeopplegg, hovedfunn, viktigste variabler, praktisk anbefaling og forbehold. Tallene er identiske på tvers av språkene; bare tegnsetting er lokalisert (komma for desimalskille på norsk, punktum på engelsk).

### 2.4 Bibliografi

Kapittel 11 er uendret i denne aktiviteten. Ingen nye sitater er innført i 9.x, 10, Sammendrag eller Abstract. De fire eksisterende kildene (IBM u.å.-a, IBM u.å.-b, GeeksforGeeks 2026a, GeeksforGeeks 2026b) dekker fortsatt alle referanser i teksten.

### 2.5 Innholdsfortegnelse

TOC er oppdatert med underpunkter 9.1–9.5. Slugs følger samme konvensjon som eksisterende TOC (norsk tegn bevart, tall uten punktum i anker).

---

## Svakheter og forbedringsforslag

### V1. WBS-nummer i kap. 3.4 (ikke i 7.1.6-scope, men observert)

**Alvorlighetsgrad:** Middels
**Kategori:** Språk og innhold

Kap. 3.4 ([rapport.md:251](../../005 report/rapport.md#L251)) refererer fortsatt eksplisitt til «I WBS 4.4 brukes 2024 i tillegg som intern valideringsperiode …». Denne formuleringen stammer fra 7.1.2 og er utenfor scope for 7.1.6, men bryter med regelen om at WBS-numre ikke skal stå i brødtekst. Bør omformuleres i 7.3.x konsistenssjekk/språkvask.

### F1. Planendring for WBS 4.3 nevnes ikke eksplisitt i 9.4

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Planen for 7.1.6 nevnte at både WBS 4.3 (lett verifikasjon) og WBS 4.4 (kun RF-tuning) skulle omtales i 9.4. Rapporten nevner kun planendringen for tuning til Random Forest (4.4), uten å referere til verifiseringssteget (4.3). 4.3-endringen har mindre operativ konsekvens for analysen og kan argumentasjonsmessig hoppes over, men kunne styrket sporbarheten mot `endringslogg.md`.

### F2. Høstbias-forklaringen er hypotetisk og kan nyanseres videre

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Kap. 9.1 sier at bias-mønsteret «peker på en begrensning i sesongsignalet i datagrunnlaget snarere enn i den enkelte modellen». Påstanden bygger på at mønsteret er konsistent på tvers av alle tre modellsporene. Dette er en rimelig hypotese, men kunne i 9.5 vært nevnt som eksplisitt kandidat for utvidet valideringsvindu eller tidsrekkemetodikk. Er dekket delvis i 9.5 men kan skjerpes.

### F3. Sammendrag og Abstract bruker «rabatt»/«discount» framfor `Discount`-variabelnavn

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

I Sammendrag og Abstract er variabelnavnet `Discount` ikke inline-kodet, men skrevet som «rabatt» eller «discount» i normal prosa. Dette er en bevisst stilvalg for å gjøre oppsummeringene leservennlige for en bredere målgruppe, men avviker fra inline-kode-konvensjonen brukt i 9.x og 10. Stilvalget kan beholdes, men bør dokumenteres som valgt standard eller harmoniseres i 7.3.3 språkvask.

---

## Avhukningsliste – tiltak

| # | Tiltak | Kategori | Status | Kommentar |
|:--|:-------|:---------|:-------|:----------|
| V1 | Erstatte «I WBS 4.4» i kap. 3.4 med akademisk formulering | Språk og innhold | [x] | Rettet 2026-04-16: «I hyperparametertuningen av Random Forest brukes 2024 …» |
| F1 | Vurdere å legge til kort henvisning til WBS 4.3-endringen i 9.4 | Språk og innhold | [x] | Rettet 2026-04-16: 9.4 nevner nå begge planendringene (verifiseringssteget og tuning-avgrensningen) med henvisning til endringsloggen, uten WBS-numre i brødtekst |
| F2 | Utvide omtalen av høstbias som kandidat for tidsrekke-videre-arbeid i 9.5 | Språk og innhold | [ ] | Kan håndteres i 7.3.3 |
| F3 | Dokumentere eller harmonisere inline-kode-stil for variabelnavn i Sammendrag/Abstract | Språk og innhold | [x] | Løst 2026-04-16 etter alternativ (a): kort notasjonssetning lagt til etter `## 3 Teori` som forklarer at inline-kode refererer til faktiske features, mens Sammendrag/Abstract bevisst bruker prosa |

---

## Samsvar med prosjektplan og krav

| Sjekkpunkt | Status | Kommentar |
|:---|:---|:---|
| Kapittel 9 omskrevet til akademisk diskusjon med klar struktur | OK | 9.1–9.5 etablert, WBS-numre fjernet fra brødtekst |
| Kapittel 10 direkte svar på problemstillingen | OK | To avsnitt som dekker begge delspørsmålene |
| Sammendrag skrevet på norsk, 250–300 ord | OK | 277 ord |
| Abstract skrevet på engelsk, 250–300 ord | OK | 298 ord |
| Bibliografi verifisert | OK | Uendret, fire kilder dekker alle referanser |
| Segmentantall i kap. 7 rettet til 13 av 14 | OK | Inkluderer «to av tre salgsnivå» |
| Status.md og wbs.json oppdatert | OK | Oppdatert i samme sesjon |
| Krav KR-001 til KR-006 reflektert i Sammendrag/Konklusjon | OK | 2025-prognose, to modellklasser, MAPE/RMSE, variabelranking, dokumentert datagrunnlag |

---

## Samlet vurdering

### Metodikk

Alle tallfestede påstander i nye tekster (9.x, 10, Sammendrag, Abstract) er verifisert mot analyseartefaktene uten avvik. Segmentkonsistensen mellom kap. 7 og analyseartefaktene er rettet som del av 7.1.6. Ingen metodiske feil eller avvik.

### Språk, innhold og figurer

Kap. 9 er omformet fra skisse til akademisk diskusjon, kap. 10 svarer direkte på problemstillingen, og Sammendrag/Abstract holder måltallet for ordtelling med identisk struktur på begge språk. Én gjenværende WBS-referanse i kap. 3.4 (utenfor 7.1.6-scope) og tre mindre språkforbedringer bør ryddes i 7.3-fasen.

### Anbefalt prioritering videre

1. **(Bør)** Rydde kap. 3.4 for WBS-referanse (V1) – håndteres i 7.3.3.
2. **(Kan)** Vurdere tilleggsnevning av WBS 4.3-endringen i 9.4 (F1).
3. **(Kan)** Harmonisere inline-kode-stil for variabelnavn i Sammendrag/Abstract (F3).

---

## Definisjon av F3 – inline-kode-stil for variabelnavn

**Observasjon:** Rapporten har to ulike typografiske konvensjoner for de samme begrepene.

- I kap. 3–10 er variabelnavn fra modellmatrisen konsekvent skrevet som inline kode, f.eks. `Discount`, `Region_North`, `dayofmonth`, `weekofyear`, `month`, `quarter`. Dette etablerer et visuelt signal om at teksten refererer til en *konkret kolonne/feature i modellen*, ikke til et hverdagsbegrep.
- I Sammendrag og Abstract er de samme begrepene skrevet som vanlige ord i prosa: «rabatt», «discount», «kalendervariablene», «region». Det er gjort bevisst for å holde oppsummeringene lesbare for et bredt publikum som ikke nødvendigvis leser hele rapporten.

**Hva F3 spør om:** Skal denne forskjellen beholdes som en bevisst stilregel, eller skal den harmoniseres slik at én form brukes konsekvent?

**Tre mulige håndteringer:**

| Alternativ | Hva det innebærer | Fordel | Ulempe |
|:---|:---|:---|:---|
| **(a) Behold mixed style, dokumentér den** | La Sammendrag/Abstract stå som ren prosa. Legg til én setning i kap. 3.4 eller i en kort «Notasjon»-bolk som forklarer at inline-kode (`Discount`) henviser til en konkret feature i modellmatrisen | Leservennlig oppsummering for ikke-tekniske lesere; teknisk presisjon beholdes i brødteksten; ingen omskriving | Krever én ekstra forklaringssetning; fortsatt to typografiske registre i samme dokument |
| **(b) Bruk `Discount` overalt (kode-stil også i Sammendrag/Abstract)** | Endre «rabatt» → `Discount`, «discount» → `Discount`, «kalendervariablene» → `year`, `month`, `quarter` osv. også i oppsummeringene | Typografisk konsistens, ingen tvetydighet | Sammendrag/Abstract blir tettere og mindre tilgjengelig; engelsk Abstract får kode-stil på ett ord mens rundtliggende prosa er ren tekst |
| **(c) Bruk prosa overalt (fjern inline-kode i kap. 9–10)** | Endre `Discount` → rabatt, `Region_North` → nord-regionen, osv. i kap. 9 og 10 | Jevn prosa overalt | Mister et nyttig visuelt signal om at en variabel refererer til en konkret modellfeature; risiko for sammenblanding mellom «rabatt» (begrep) og `Discount` (datasettets faktiske kolonnenavn som ikke er norsk) |

**Min anbefaling: alternativ (a).** Den mixed styling er pedagogisk hensiktsmessig: Sammendrag og Abstract fungerer som «skannbare oppsummeringer» for bredt publikum, mens brødteksten i kap. 9 og 10 henvender seg til lesere som drar nytte av å kunne skille feature-navn fra hverdagsbegreper visuelt. En kort notasjonsbolk i kap. 3.4 – eller helt i starten av kap. 3 – vil gjøre valget eksplisitt og fjerner F3 som åpent punkt.

Valget er likevel et redaksjonelt spørsmål og kan tas når 7.3.3 språkvask gjennomføres.

---

## Uavhengig verifisering 2026-04-16 (andre pass)

Dette avsnittet dokumenterer en andre, uavhengig gjennomgang av 7.1.6 utført etter at arbeidet var committet (`2e12f06 Update project status and documentation for WBS 7.1.6 completion`). Verifiseringen kontrollerer ni spesifikke tallpåstander mot kildene i `006 analysis/aktiviteter/`.

| # | Kontrollpunkt | Kilde | Status |
|:--|:---|:---|:---|
| 1 | Delta tuned RF vs. benchmark lineær: $-2{,}13$ RMSE og $-0{,}21$ pp MAPE (kap. 9.1) | `tab_rmse_mape_oversikt.csv` (578,26 vs. 580,39; 43,97 % vs. 44,18 %) | OK |
| 2 | Bias-mønster konsistent for alle tre modellspor (aug/sept negativ, nov/des positiv) (kap. 9.1) | `tab_bias_maaned_modell.csv` viser samme fortegn for benchmark lineær, baseline RF og tuned RF i august, september, november og desember | OK |
| 3 | Feature importance: Discount 11,48 %, dayofmonth 11,35 %, weekofyear 10,40 %, month 6,74 %, dayofweek 6,52 % (kap. 9.2) | `tab_rf_tuned_feature_importance.csv` | OK |
| 4 | Kalendergruppe ~42 % av topp 10 (kap. 9.2) | `tab_variabelgrupper_tuned_top10.csv`: 41,9826 % | OK |
| 5 | «De ni øverste variablene i tuned RF gjenfinnes også i topp 10 for baseline RF» (kap. 9.2) | `tab_rf_stabilitet_topp10.csv`: 9 av 11 unike topp-10-features er i begge modeller (`quarter` kun tuned, `Region_South` kun baseline) | OK |
| 6 | 11 av 12 måneder på RMSE og 13 av 14 segmenter (kap. 10, Sammendrag, Abstract) | `tab_modellvinner_telling.csv` og `tab_segmentvinnere_tolkning.csv` | OK |
| 7 | 9 994 rader, 6 682 trenings- og 3 312 testrader, 67 features (Sammendrag, Abstract) | `Dagligvare_Dataset.csv`, Tabell 5.1 og `tab_lr_modelloversikt.csv` | OK |
| 8 | Benchmark lineær best i segment «høyt salg» på RMSE ($699{,}10$) og MAPE ($30{,}31\%$) (kap. 9.1) | `tab_segmentvinnere_tolkning.csv` | OK |
| 9 | Tabell 8.4-tellingen gir 13 av 14 for tuned RF (kap. 7 L332) | Manuell telling mot Tabell 8.4: 4 kvartaler + 3 rabattband + 4 regioner + 2 av 3 salgsnivå = 13 | OK |

**Funn fra andre pass:** Ingen nye avvik. Alle ni kontrollpunkter er verifisert mot kilde uten feil. Svakhetene V1 og forbedringsforslagene F1–F3 fra første pass står som før og skal håndteres i 7.3-fasen.

### Samlet vurdering etter andre pass

Aktiviteten WBS 7.1.6 anses som metodisk og innholdsmessig **godkjent**. De gjenværende tiltakene er alle kategorisert som 7.3-arbeid (språkvask og konsistenssjekk) og blokkerer ikke lukking av 7.1.6.
