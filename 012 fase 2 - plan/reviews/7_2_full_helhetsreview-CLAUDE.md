# Helhetsreview av WBS 7.2 – Figurer, tabeller og integrering i rapport

**Reviewer:** Claude (automatisk helhetsreview)
**Dato:** 2026-04-19
**Omfang:** WBS 7.2.1 (utvalg), 7.2.2 (case/data), 7.2.3 (analyse/resultat/diskusjon), 7.2.4 (innsetting i [rapport.md](../../005%20report/rapport.md))
**Leveranser:** [rapport_fig_tab_utvalg.md](../rapport_fig_tab_utvalg.md), [rapport_7_2_2_artefakter.md](../rapport_7_2_2_artefakter.md), [rapport_7_2_3_artefakter.md](../rapport_7_2_3_artefakter.md), oppdatert [rapport.md](../../005%20report/rapport.md) (706 linjer)

Denne reviewen dekker hele 7.2-blokken. Delreviewen av 7.2.1 ([7_2_1_velge_rapportfigurer_og_tabeller-CLAUDE.md](7_2_1_velge_rapportfigurer_og_tabeller-CLAUDE.md)) er allerede lukket; denne reviewen fokuserer på produksjonsstegene 7.2.2–7.2.4 og tverrsnittet (konsistens, rekkefølge, reproduserbarhet).

---

## Sammendrag

Fem nye figurer er produsert via utvidelser av eksisterende plotteskript, to figurer er kopiert inn via referanser, og ti nye Markdown-tabeller er lagt inn i rapporten med full sporbarhet til analyse-CSV-ene. Tallverdier i alle 10 nye tabeller matcher kildene eksakt. Hovedsvakheten er at to tabeller i rapporten bryter formkrav 1 «nummereres i rekkefølgen de omtales»: Tabell 5.1 kommer etter 5.2–5.4 i § 5.2, og Tabell 9.2 kommer etter 9.3 i kap. 9. Tre lave svakheter gjelder tekstpresisjon og redundans, og tre lave forbedringsforslag gjelder kolonnespråk, IDs og formateringsdetaljer.

**Totalt:** 9 styrker, 4 svakheter (0 Høy, 1 Middels, 3 Lav), 3 forbedringsforslag (Lav).

---

## Styrker

- **S1.** Fem nye PNG-er (Figur 7.1, 7.2, 8.1, 8.2, 8.3) er lagt inn som utvidelser av eksisterende `start_wbs_5_2.py`, `start_wbs_5_4.py` og `start_wbs_6_1.py`. Skriptene er ikke omskrevet; plottfunksjonene er nye og kalles fra eksisterende `main()`, slik at én `uv run python …`-kommando per aktivitet gir både CSV og PNG som ferdig leveranse. Dette bevarer ende-til-ende-reproduserbarheten fra tidligere WBS-trinn.
- **S2.** Konsistent visuell grammatikk på tvers av analysefigurene: LR, baseline RF og tuned RF bruker samme fargetriplett (`#1f77b4`, `#ff7f0e`, `#2ca02c`) i Figur 7.1, 7.2 og 8.1. Dette gjør at leseren gjenkjenner hver modell umiddelbart når figurene omtales i kap. 7, 8 og 9. Figur 8.2 og 8.3 bruker variabelgruppe-palett som er intern-konsistent innenfor sin egen sammenligning.
- **S3.** Alle 12 figurer bruker HTML-mønsteret fra CLAUDE.md (`<div align="center"> … width="80%"`, sentrert kursiv figurtekst i `<small><i>`), og alle 16 tabeller har sentrert kursiv tabelltittel rett under. Mønsteret som ble introdusert i § 4.1–4.3 i tidligere WBS-trinn er gjenbrukt uendret; ingen ny HTML-variant ble introdusert i 7.2.2 eller 7.2.4.
- **S4.** Tabellverdier i rapporten samsvarer eksakt med kildene i [006 analysis/aktiviteter/](../../006%20analysis/aktiviteter/): Tabell 5.2 har 11 rader fra `tab_relevante_variabler.csv`, Tabell 5.3 har 18 rader fra `tab_featurevalg.csv`, Tabell 5.4 har 18 rader fra `tab_renselogg.csv`, Tabell 6.2 har 5 rader fra `tab_rf_tuning_kandidater.csv` (sortert på RMSE i samsvar med reviewkrav F3 fra 7.2.1), Tabell 7.1 har 12 måneder fra `tab_rmse_mape_maaned.csv`, Tabell 7.2 har 14 segmenter fra `tab_segmentmetrikk_modell.csv`, Tabell 9.1–9.3 stemmer med `tab_modellprofil_6_2.csv`, `tab_metodebegrensninger_6_2.csv` og `tab_beslutningsmatrise_6_3.csv`. Ingen avrundingsfeil eller transkripsjonsfeil funnet.
- **S5.** Leveransefilene `rapport_7_2_2_artefakter.md` og `rapport_7_2_3_artefakter.md` gir sporbarhet fra kildeartefakt til rapportblokk i to trinn: utvalgsdokumentet peker på hvilke CSV-er som er kilder, og leveransefilene skriver ut de faktiske markdown-blokkene som er limt inn. Dette gjør 7.2.4 til et rent mekanisk steg og muliggjør enkel re-innsetting hvis rapporten må genereres på nytt.
- **S6.** Enkeltkilde-prinsippet er opprettholdt: PNG-ene kopieres ikke inn i `005 report/`, men refereres med relativ sti `../006 analysis/aktiviteter/…`. Dette er samme mønster som Figur 4.1–4.3 bruker fra før, og sikrer at analysefigurene og rapportfigurene aldri kan bli usynkroniserte.
- **S7.** Rapport.md er 706 linjer, UTF-8 uten BOM verifisert med `file`, alle norske tegn `æ`, `ø`, `å` er bevart gjennom alle edits. Ingen formatbrudd eller encoding-regresjoner i introdusert under produksjonen.
- **S8.** Endringsloggen er oppdatert umiddelbart ved 7.2.1-avslutning (F2 fra delreviewen av 7.2.1), og dokumenterer omfangsøkningen (12 figurer og 15 innholdstabeller vs. minimalt antall i Gantt-baseline). Dette gir et sporbart beslutningsgrunnlag før 7.2.2–7.2.4 starter.
- **S9.** Gantt-vinduet for 7.2-blokken (2026-04-15 til 2026-04-20) holder. 7.2.1 er fullført 2026-04-19 (forsinket fire dager), men 7.2.2–7.2.4 er akselerert og gjennomført samme dag, slik at 7.2-blokken samlet leverer innenfor det opprinnelige Gantt-vinduet. Endringsloggens forbehold om planforskyvning utløses dermed ikke.

---

## Del 1 – Metodikk (produksjon og konsistens)

### 1.1 Figurproduksjon – skript og PNG-er

Alle fem nye PNG-er er verifisert på disk med riktig dato og størrelse:

| Figur | Fil | Størrelse | Skript |
|:------|:----|:----------|:-------|
| 7.1 | [fig_bias_maaned_modell.png](../../006%20analysis/aktiviteter/16_tolke_modellresultater/fig_bias_maaned_modell.png) | 309 KB | [start_wbs_6_1.py](../../006%20analysis/aktiviteter/16_tolke_modellresultater/start_wbs_6_1.py) |
| 7.2 | [fig_rmse_maaned_modell.png](../../006%20analysis/aktiviteter/13_rmse_og_mape/fig_rmse_maaned_modell.png) | 311 KB | [start_wbs_5_2.py](../../006%20analysis/aktiviteter/13_rmse_og_mape/start_wbs_5_2.py) |
| 8.1 | [fig_rmse_mape_samlet.png](../../006%20analysis/aktiviteter/13_rmse_og_mape/fig_rmse_mape_samlet.png) | 163 KB | [start_wbs_5_2.py](../../006%20analysis/aktiviteter/13_rmse_og_mape/start_wbs_5_2.py) |
| 8.2 | [fig_feature_importance_tuned_top10.png](../../006%20analysis/aktiviteter/15_viktige_variabler/fig_feature_importance_tuned_top10.png) | 190 KB | [start_wbs_5_4.py](../../006%20analysis/aktiviteter/15_viktige_variabler/start_wbs_5_4.py) |
| 8.3 | [fig_variabelgrupper_tuned_top10.png](../../006%20analysis/aktiviteter/15_viktige_variabler/fig_variabelgrupper_tuned_top10.png) | 107 KB | [start_wbs_5_4.py](../../006%20analysis/aktiviteter/15_viktige_variabler/start_wbs_5_4.py) |

Alle fem skripts er kjørt ende-til-ende via `uv run python aktiviteter/<mappe>/<skript>.py` og terminerte uten feil. Skriptoppdragene fra utvalgsdokumentet § 7.2 er gjennomført iht. plan.

**Vurdering:** Produksjonen er reproduserbar og skriptene er integrert ryddig med eksisterende WBS-kode.

### 1.2 Tabellkonsistens – kilder og rapport

Eksplisitt radsammenligning mellom kilde-CSV og rapporttekst:

| Rapporttabell | Kilde-CSV | Antall rader (kilde) | Antall rader (rapport) | Status |
|:--------------|:----------|:---------------------|:------------------------|:-------|
| Tabell 5.2 | `tab_relevante_variabler.csv` | 11 data | 11 | OK |
| Tabell 5.3 | `tab_featurevalg.csv` | 18 data | 18 | OK |
| Tabell 5.4 | `tab_renselogg.csv` | 18 data | 18 | OK |
| Tabell 6.1 | sammenstilt fra tre modelloversikter | 3 | 3 | OK |
| Tabell 6.2 | `tab_rf_tuning_kandidater.csv` (topp 5 på RMSE) | 36 totalt, 5 vist | 5 | OK |
| Tabell 7.1 | pivot av `tab_rmse_mape_maaned.csv` | 36 rader, 12 måneder | 12 | OK |
| Tabell 7.2 | `tab_segmentmetrikk_modell.csv` pivotert | 42 rader, 14 segmenter | 14 | OK |
| Tabell 9.1 | `tab_modellprofil_6_2.csv` | 3 | 3 | OK |
| Tabell 9.2 | `tab_metodebegrensninger_6_2.csv` | 6 | 6 | OK |
| Tabell 9.3 | kompakt utdrag av `tab_beslutningsmatrise_6_3.csv` | 4 | 4 | OK |

Stikkprøver av tallverdier: Tabell 6.2 rad «rf_tune_30 (vinner)» viser RMSE 577,27 og delta −13,04 – stemmer med `tab_rf_tuning_vinner.csv` (577,26775, delta −13,036124 rundet). Tabell 7.1 rad 2025-06 viser MAPE tuned RF 42,79 % – stemmer med kilde 42,7886. Tabell 9.1 rad tuned RF viser 11 RMSE-vinnermåneder og 13 RMSE-vinnersegmenter – stemmer med kilde.

**Vurdering:** Alle verdier er transkribert korrekt. Ingen avrundings- eller formatkonflikter.

### 1.3 Rekkefølge av figurer og tabeller i rapporten — V1

Nummeringen i rapporten må matche rekkefølgen tabellene/figurene omtales i (formkrav 1, utvalgsdokumentet § 3 regel 1). Verifisert mot [rapport.md](../../005%20report/rapport.md):

| Kapittel | Tabeller i teksten | Rekkefølge OK? |
|:---------|:-------------------|:---------------|
| § 5.2 Data | 5.2, 5.3, 5.4, **5.1** | **Nei – 5.1 kommer sist** |
| § 6 | 6.1, 6.2 | OK |
| § 7 | 7.1, 7.2 | OK |
| § 8 | 8.1, 8.2, 8.3, 8.4 | OK |
| § 9 | 9.1 (i §9.1), **9.3 (i §9.3), 9.2 (i §9.4)** | **Nei – 9.2 kommer sist** |
| § 12 | 12.1 | OK |

| Kapittel | Figurer i teksten | Rekkefølge OK? |
|:---------|:------------------|:---------------|
| § 4 | 4.1, 4.2, 4.3 | OK |
| § 5.2 | 5.1, 5.2 | OK |
| § 7 | 7.1, 7.2 | OK |
| § 8 | 8.1, 8.2, 8.3 | OK |

To reelle rekkefølgebrudd. Se V1 nedenfor for rettetiltak.

**Vurdering:** Figurer er 100 % i rekkefølge; to tabeller er ute av rekkefølge.

### 1.4 Samsvar med KR-005 og KR-006

- **KR-005** (datagrunnlaget skal være strukturert, kvalitetssikret og dokumentert): Tabell 5.2 (variabeloversikt), Tabell 5.3 (feature engineering), Tabell 5.4 (renselogg) og Figur 5.1 (datatyper) dokumenterer datagrunnlaget eksplisitt i rapporten. Full sporbarhet er gitt til aktiviteter 01, 02, 04 og 05. **I samsvar.**
- **KR-006** (resultater, metodevalg og modellforutsetninger skal dokumenteres for etterprøving): Tabell 6.1 og 6.2 i kap. 6 dokumenterer modellforutsetningene; Tabell 7.1, 7.2, 8.1–8.4 dokumenterer resultatene; Tabell 9.1–9.3 dokumenterer tolkningen. Full feature importance ligger som vedlegg A4. **I samsvar.**

### Gjenstående metodiske observasjoner

- Internhenvisningene «(jf. Tabell 8.2)», «(jf. Tabell 8.3)» og «(jf. Tabell 8.4)» i kap. 7 (linje 355, 359, 361) peker på tabeller i kap. 8 selv om Tabell 7.1 og 7.2 nå inneholder samme tallgrunnlag. Teknisk korrekt, men kan med fordel oppdateres i 7.3.1 (planen la eksplisitt dette dit). Se F1 – ikke en svakhet i 7.2.4.
- Vedleggstabellen (Tabell 12.1) var ikke spesifisert som «tabell» i utvalgsdokumentet, bare som en «referanseliste». Valget om å sette den opp som nummerert tabell gir konsistent formalia, men øker tabelltellingen fra 15 (utvalget) til 16. Se F2.

---

## Del 2 – Språk, innhold og figurer

### 2.1 Rapporttekst – introduksjonssetninger

Alle 12 nye innsettinger (5 figurer og 10 tabeller) har fått kort introduksjonssetning før eller etter blokken, modellert etter mønsteret «Figur X viser …» / «Tabell Y oppsummerer …» som eksisterer for Figur 4.1–4.3 og Tabell 5.1 og 8.1–8.4.

**Språk:** Norsk fagspråk er konsistent gjennom alle introsetninger. Terminologien «tuned Random Forest», «benchmark lineær», «baseline Random Forest» holdes identisk med resten av rapporten. Ingen skrivefeil oppdaget.

**Flyt:** To observasjoner:

- § 5.2 har to nesten-identiske setninger i sekvens: «Figur 5.2 viser fordelingen av daglige salgsverdier i trenings- og testperioden» (linje 405) og umiddelbart etter Figur 5.2-blokken «Tabell 5.1 viser den samlede fordelingen mellom trenings- og testdata» (linje 412). Ordet «fordelingen» dominerer i to ulike betydninger på få linjer. Se V3.
- «Tabell 5.2 oppsummerer de 11 unike råvariablene i datasettet» (linje 335) er teknisk upresist – tabellen inneholder 1 målvariabel (`Sales`) og 10 forklaringsvariabler, dvs. 11 kolonner i datasettet. Se V4.

### 2.2 Figurer – titler og akselabeler

| Figur | Tittel i figur | Akselabeler | Vurdering |
|:------|:---------------|:------------|:----------|
| 7.1 | «Månedlig bias per modell i 2025» | «Måned i 2025» / «Bias (kroner, sum)» | OK, med nulllinje |
| 7.2 | «Månedlig RMSE per modell i 2025» | «Måned i 2025» / «RMSE (kroner)» | OK |
| 8.1 | «Samlet RMSE og MAPE for 2025» (subplot-titler «Samlet RMSE 2025» / «Samlet MAPE 2025») | Modellrolle (x) / RMSE (y) og MAPE (y) | OK, verdier er annotert |
| 8.2 | «Topp 10 feature importance – tuned Random Forest» | «Normalisert viktighet (%)» / feature-navn | OK, legend viser variabelgruppe |
| 8.3 | «Variabelgrupper i topp 10 – tuned Random Forest» | Variabelgruppe (x) / «Samlet importance i topp 10 (%)» (y) | OK, antall annotert |

Alle figurtekster oppgir hva som vises, enhet og hovedbudskap – i tråd med lærerens formkrav 5. Ingen har kildehenvisning (egenproduserte).

### 2.3 Tabeller – kolonner og lesbarhet

| Tabell | Antall kolonner | Norsk kolonnespråk? | Observasjoner |
|:-------|:----------------|:--------------------|:--------------|
| 5.2 | 6 | Ja | «Manglende %» er klart. |
| 5.3 | 4 | Ja | `–` for ekskluderte output-kolonner er lesbart. |
| 5.4 | 3 | Ja | Målepunkt-koder er tekniske men sporbare. |
| 6.1 | 6 | Ja | Kombinert tabell er kompakt. |
| 6.2 | 8 | Ja | Kolonnen «Kandidat» har lange navn med formatering «rf_tune_XX». |
| 7.1 | 7 | Ja | 12 rader × 7 kolonner – ganske bredt, men lesbart. |
| 7.2 | 8 | **Delvis** – «Dimensjon»-verdiene bruker engelske koder (`quarter`, `discount_band`, `Region`, `sales_band`) og segmentverdier bruker ikke-norske tegn (`lav`, `middels`, `hoy`). Se F3. |
| 9.1 | 10 | Ja | Svært bred tabell (10 kolonner) – kan være en utfordring for PDF-eksport. |
| 9.2 | 5 | Ja | ID-kolonnen «MB-6.2-01» osv. er interne koder som leseren ikke trenger. Se F4. |
| 9.3 | 5 | Ja | Kompakt og klar. |
| 12.1 | 3 | Ja | Lenke-kolonnen er lesbar i VS Code. |

### 2.4 Plassering i forhold til utvalgsdokumentet

| Artefakt | Plan (utvalgsdokumentet) | Plassering i rapport | Samsvar |
|:---------|:--------------------------|:---------------------|:--------|
| Figur 5.1 | tidlig i § 5.2 | etter første avsnitt | OK |
| Figur 5.2 | etter Tabell 5.4 og før Tabell 5.1 | etter datasplitt-avsnittet, før Tabell 5.1 | OK |
| Tabell 5.2, 5.3, 5.4 | § 5.2 etter Figur 5.1 | etter målvariabel-avsnittet | OK |
| Tabell 6.1 | tidlig i kap. 6 | etter første avsnitt | OK |
| Tabell 6.2 | kap. 6, etter diskusjon av tuning | etter tredje avsnitt | OK |
| Tabell 7.1 | kap. 7, før Figur 7.1/7.2 | etter månedsnivå-avsnittet | OK |
| Figur 7.1, 7.2 | kap. 7, etter bias-avsnittet | etter bias-avsnittet, før segmentavsnittet | OK |
| Tabell 7.2 | kap. 7, etter Figur 7.2 | etter segmentavsnittet | OK |
| Figur 8.1 | kap. 8, etter Tabell 8.1 | etter Tabell 8.1 | OK |
| Figur 8.2, 8.3 | kap. 8, etter Tabell 8.3 | etter Tabell 8.3 | OK |
| Tabell 9.1 | § 9.1 | § 9.1 etter første avsnitt | OK |
| Tabell 9.2 | § 9.4 | § 9.4 etter første avsnitt | **OK lokalt, men skaper rekkefølgebrudd globalt – se V1** |
| Tabell 9.3 | § 9.3 | § 9.3 etter første avsnitt | **OK lokalt, men skaper rekkefølgebrudd globalt – se V1** |

### 2.5 Konsistens med status.md og wbs.json

Statusfilen er foreløpig **ikke oppdatert** for 7.2.2–7.2.4. Linje 74 viser fortsatt bare 7.2.1 som fullført, og sjekkpunktene for 7.2.2, 7.2.3 og 7.2.4 står som åpne. `wbs.json` viser fortsatt `percent_complete: "0%"` for task_id 30, 31, 32 (7.2.2, 7.2.3, 7.2.4).

Planen for 7.2.4 sa eksplisitt: «oppdateres først når 7.2.4 lukkes (ikke under denne aktiviteten)». Det er dermed i henhold til plan, men må lukkes nå når reviewen starter – dette er et åpent punkt for avslutning av 7.2-blokken. Se F5.

---

## Svakheter og forbedringsforslag

### V1. Tabell 5.1 og Tabell 9.2 bryter formkrav 1 «nummereres i rekkefølgen de omtales»

**Alvorlighetsgrad:** Middels
**Kategori:** Metodikk

I § 5.2 omtales tabellene i rekkefølgen 5.2 → 5.3 → 5.4 → 5.1. Tabell 5.1 (splittabell) ble liggende på opprinnelig plassering mens 5.2–5.4 ble lagt inn før den. Formkrav 1 (utvalgsdokumentet § 3 regel 1) krever at nummer og omtale-rekkefølge matcher. Samme brudd oppstår i kap. 9: Tabell 9.1 i § 9.1, Tabell 9.3 i § 9.3 og Tabell 9.2 i § 9.4 – med 9.3 før 9.2.

**Anbefalt tiltak (to alternativer):**

A) Omnummerer tabellene:

- § 5.2: dagens Tabell 5.1 (splittabell) omnummeres til Tabell 5.5 og plasseres til slutt i § 5.2. Utvalgsdokumentet oppdateres tilsvarende.
- Kap. 9: bytt tabellnummer slik at den som omtales først blir Tabell 9.1, andre 9.2, tredje 9.3.

B) Flytt rekkefølgen i teksten:

- § 5.2: flytt Tabell 5.1 til å komme før Tabell 5.2 (altså tidligst i § 5.2), og tilpass introsetninger.
- Kap. 9: flytt diskusjonen av metodebegrensninger (§ 9.4) før diskusjonen av praktisk nytte (§ 9.3), eventuelt behold rekkefølgen men bytt tabellnummer mellom 9.2 og 9.3 i tabellene.

Alternativ A er mer målrettet og gir mindre redigering i brødteksten. Alternativ B bryter med rapportstrukturen i CLAUDE.md der § 9.3 Praktisk nytte kommer før § 9.4 Metodiske begrensninger, så A anbefales.

**Begrunnelse:** Dette er det eneste forholdet i 7.2-blokken som bryter et eksplisitt formkrav, og det er blitt synlig først etter at 7.2.4 faktisk plasserte tabellene i rapporten. Delreviewen av 7.2.1 fanget ikke opp dette fordi utvalgsdokumentet plasserte tabell-numrene strukturelt (etter §-nummer) snarere enn etter tekstrekkefølge.

### V2. Innsettingsrekkefølgen i utvalgsdokumentet avgjorde nummereringen i rapporten uten å sjekke mot formkrav 1

**Alvorlighetsgrad:** Lav
**Kategori:** Metodikk

Utvalgsdokumentet § 5–6 spesifiserer plasseringen per §-nummer, ikke per tekstavsnitt. Dette fungerer bra når en seksjon bare har én tabell/figur, men blir sårbart når flere tabeller fordeles over flere underseksjoner i samme kapittel (som kap. 5 og kap. 9). 7.2.1-reviewen fanget opp tilsvarende tilfelle i kap. 8 (V1 der) og rettet det ved å bytte nummer; samme sjekkrutine burde vært gjennomført for kap. 5 og 9.

**Anbefalt tiltak:** Når V1 rettes, oppdater utvalgsdokumentet § 5.1/§ 6.1 og § 6.5 slik at nummereringen stemmer med endelig tekstrekkefølge. Legg gjerne inn en generell regel i utvalgsdokumentet § 3: «Når en seksjon får flere tabeller/figurer fordelt over underseksjoner i ulike kapittelnumre, må tabell-/figurnummer settes i samme rekkefølge som underseksjonene.»

### V3. Redundant bruk av ordet «fordelingen» i to nabosetninger i § 5.2

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Linje 405 (introsetning til Figur 5.2) og linje 412 (introsetning til Tabell 5.1) bruker begge ordet «fordelingen» i to tekstmessig nære posisjoner med ulik betydning. Det første refererer til fordelingen av salgsverdier; det andre til fordelingen mellom trening og test. Leseren kan bli usikker på om setningene refererer til samme fenomen.

**Anbefalt tiltak:** Omformuler introsetningen for Tabell 5.1 til f.eks. «Tabell 5.1 oppsummerer antallsfordelingen mellom trenings- og testperioden.» Alternativt skriv sammen Figur 5.2- og Tabell 5.1-introen i én flytende setning: «Figur 5.2 viser fordelingen av salgsverdier, mens Tabell 5.1 oppsummerer antallet rader i hver periode.»

### V4. «11 unike råvariablene» i introsetning til Tabell 5.2 er upresist

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Linje 335 sier «Tabell 5.2 oppsummerer de 11 unike råvariablene i datasettet». Tabellen inneholder 1 målvariabel (`Sales`) og 10 forklaringsvariabler. Begrepet «råvariabler» er ikke etablert i rapporten ellers, og utvalgsdokumentet § 6.1 beskriver tabellen som «variabeloversikt».

**Anbefalt tiltak:** Endre til «Tabell 5.2 oppsummerer de 11 kolonnene i rådatasettet med datatype, manglende andel og anbefaling for videre bruk.»

### F1. Internhenvisninger til Tabell 8.x i kap. 7 kan oppdateres

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Linje 355, 359 og 361 i rapport.md henviser «(jf. Tabell 8.2)», «(jf. Tabell 8.3)» og «(jf. Tabell 8.4)». Nå som Tabell 7.1 og 7.2 inneholder samme tallgrunnlag lokalt i kap. 7, kunne disse henvisningene peke internt. Planen for 7.2.4 la dette eksplisitt til 7.3.1, så dette er ikke en svakhet i 7.2.4 – men bør stå som åpent punkt i [status.md](../status.md) for 7.3.1-lista.

### F2. Tabell 12.1 (vedleggsreferanser) var ikke spesifisert i utvalget

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Utvalgsdokumentet § 9 beskriver A1–A7 som «vedleggsreferanser», uten å spesifisere tabellformat eller tabellnummer. 7.2.4 valgte å presentere dem som Tabell 12.1 med sentrert kursiv tabelltittel, noe som gir enhetlig formalia gjennom rapporten. Dette er en legitim formatering men avviker fra utvalgets teksttone.

**Anbefalt tiltak:** Enten (a) beholde Tabell 12.1-formatet og oppdatere utvalgsdokumentet § 9 og samsvarstellingen i status.md til «16 innholdstabeller» (de 15 opprinnelige + Tabell 12.1), eller (b) konvertere vedleggsrammen til en ren referanseliste uten tabellnummer. Alternativ (a) anbefales for konsistens.

### F3. Engelske segmentkoder i Tabell 7.2

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Tabell 7.2 bruker kildefilens tekniske kolonnenavn i «Dimensjon»-kolonnen: `quarter`, `discount_band`, `Region`, `sales_band`. Segmentverdier bruker `lav`, `middels`, `hoy` (uten `ø`), `lavt salg`, `middels salg`, `hoyt salg`. Dette er konsistent med kilde-CSV, men rapportteksten ellers bruker norske termer (Kvartal, Rabatt, Region, Salgsnivå).

**Anbefalt tiltak:** Oversett kolonneverdiene til norsk: `quarter` → `Kvartal`, `discount_band` → `Rabattbånd`, `sales_band` → `Salgsbånd`. Og bruk `høy`/`høyt salg` (med norsk `ø`). Kildeartefaktene trenger ikke endres; bare rapport-versjonen.

---

## Avhukningsliste – tiltak

| # | Tiltak | Kategori | Status | Kommentar |
|:--|:-------|:---------|:-------|:----------|
| V1 | Omnummerer Tabell 5.1 til 5.5 (splittabell sist) og bytt nummer mellom Tabell 9.2 og 9.3 slik at tekstrekkefølgen 9.1 → 9.2 → 9.3 stemmer. Oppdater utvalgsdokumentet og leveransefiler tilsvarende. | Metodikk | [x] | Gjennomført 2026-04-19. Tabell 5.1 → 5.5 i rapport og utvalg; Tabell 9.2 (beslutningsmatrise) og 9.3 (metodebegrensninger) byttet i rapport, utvalgsdokument og leveransefilene. |
| V2 | Legg inn generell regel i utvalgsdokumentet § 3 om nummering på tvers av underseksjoner | Metodikk | [x] | Gjennomført 2026-04-19. Regel 6 lagt til i utvalgsdokumentet § 3. |
| V3 | Omformuler introsetningen til Tabell 5.1 slik at «fordelingen» ikke dupliseres | Språk og innhold | [x] | Gjennomført 2026-04-19. Introsetning for Tabell 5.5 endret til «oppsummerer antallsfordelingen mellom trenings- og testperioden». |
| V4 | Endre «11 unike råvariablene» → «11 kolonnene i rådatasettet» i linje 335 | Språk og innhold | [x] | Gjennomført 2026-04-19. |
| F1 | Noter i [status.md](../status.md) WBS 7.3.1-liste: oppdater (jf. Tabell 8.x)-henvisninger i kap. 7 | Språk og innhold | [x] | Gjennomført 2026-04-19. Sub-bullet lagt til under WBS 7.3.1 i status.md. |
| F2 | Enten oppdater utvalgsdokumentet til 16 innholdstabeller, eller konverter Tabell 12.1 til ren referanseliste | Språk og innhold | [x] | Gjennomført 2026-04-19. Valgt (a): utvalgsdokumentet § 9, § 10 og § 11 oppdatert til 16 innholdstabeller med Tabell 12.1 eksplisitt nevnt. |
| F3 | Oversett segmentkoder i Tabell 7.2 til norsk (`quarter` → `Kvartal`, osv.) | Språk og innhold | [x] | Gjennomført 2026-04-19. Kvartal, Rabattbånd, Salgsbånd + høy/høyt salg med `ø` i rapport og leveransefil. |
| F4 | Vurder om ID-kolonnen (MB-6.2-01 …) i Tabell 9.2 skal droppes for bedre lesbarhet | Språk og innhold | [x] | Gjennomført 2026-04-19. ID-kolonnen droppet i rapport-versjonen av Tabell 9.3 (metodebegrensninger); kildefil beholder IDs. |
| F5 | Oppdater [status.md](../status.md) og [wbs.json](../wbs.json) når V1 er rettet og 7.2-blokken er formelt lukket | Metodikk | [x] | Gjennomført 2026-04-19. 7.2.2, 7.2.3 og 7.2.4 satt til `[x]` i status.md og `100%` i wbs.json (task_id 30, 31, 32). Datolinjen, H-raden og «Anbefalt kort prosjektstatus» oppdatert konsistent med tabell- og figurtellinger etter V1. |

---

## Samsvar med prosjektplan og krav

| Sjekkpunkt | Status | Kommentar |
|:---|:---|:---|
| WBS 7.2.1 – Velge figurer og tabeller | OK | Lukket 2026-04-19, review gjennomført. |
| WBS 7.2.2 – Lage case- og datakapitlets figurer og tabeller | **OK (venter på statusoppdatering)** | Leveranse `rapport_7_2_2_artefakter.md` foreligger; innsetting gjennomført i rapport.md. Status.md ikke oppdatert ennå. |
| WBS 7.2.3 – Lage analyse-, resultat- og diskusjonsfigurer og tabeller | **OK (venter på statusoppdatering)** | Leveranse `rapport_7_2_3_artefakter.md` + 5 PNG-er. Status.md ikke oppdatert ennå. |
| WBS 7.2.4 – Sette inn, nummerere og formatere | **Delvis – V1 bryter formkrav 1** | Innsetting fullført, men tabellrekkefølgen i kap. 5 og 9 må rettes. |
| KR-005 – Strukturert, kvalitetssikret og dokumentert datagrunnlag | OK | Tabell 5.2–5.4 og Figur 5.1 i rapporten. |
| KR-006 – Dokumentasjon for etterprøving | OK | Tabell 6.1–6.2, 7.1–7.2, 8.1–8.4, 9.1–9.3 og vedlegg A1–A7. |
| Lærerens formkrav 1 (nummeres i rekkefølgen de omtales) | **Delvis – V1** | Figurer OK; to tabeller ute av rekkefølge. |
| Lærerens formkrav 5 (selvstendig forståelige fig./tabelltekster) | OK | Alle 12 figurer og 16 tabeller har komplett tekst. |
| Lærerens formkrav 6 (egenprodusert → ingen kilde) | OK | Ingen kildehenvisning i figur-/tabelltekst. |
| Lærerens formkrav 8 (stort materiale i vedlegg) | OK | A1–A7 i Tabell 12.1 i kap. 12. |
| CLAUDE.md: norsk, UTF-8 uten BOM, `æ/ø/å` bevart | OK | `file` bekrefter UTF-8. `ø` i segmentkoder ikke brukt – se F3. |
| CLAUDE.md: figurmønster (`<div align="center"> … width="80%"`) | OK | Alle 7 nye figurer følger mønsteret. |
| Endringsloggen registrerer omfangsøkning | OK | Oppføring 2026-04-19 dekker hele 7.2-blokken. |

---

## Samlet vurdering

### Metodikk

Produksjonen i 7.2.2–7.2.4 er gjennomført ryddig og reproduserbart. Alle fem nye figurer genereres av utvidelser i eksisterende WBS-skript og er sporbare ende-til-ende. Alle tabellverdier er verifisert mot kilde-CSV. Hovedsvakheten er strukturell (V1): to tabeller er ute av rekkefølge ift. formkrav 1, som krever en målrettet omnummerering. Denne feilen er strukturell og må rettes før 7.2-blokken formelt kan lukkes.

### Språk, innhold og figurer

Rapportspråket er konsistent med resten av rapporten, norsk fagterminologi holdes gjennom, og figurer/tabeller har selvstendig forståelige tekster. To små språkjusteringer (V3 redundans og V4 presisjon) og en oversettelsesjobb i Tabell 7.2 (F3) gjenstår. Ingen av disse er blokkerende.

### Anbefalt prioritering videre

V1–V4 og F1–F5 er alle gjennomført 2026-04-19. Reviewen er lukket; 7.2-blokken er formelt avsluttet.

1. ~~**(Må)** Rett V1 – omnummerer Tabell 5.1 og bytt nummer mellom Tabell 9.2 og 9.3 slik at tekstrekkefølgen matcher nummereringen. Oppdater utvalgsdokumentet, leveransefilene 7.2.2/7.2.3 og rapport.md konsekvent.~~ Gjennomført.
2. ~~**(Må)** Lukk 7.2.2, 7.2.3 og 7.2.4 i [status.md](../status.md) og [wbs.json](../wbs.json) når V1 er rettet (F5).~~ Gjennomført.
3. ~~**(Bør)** Rett V3 (redundans) og V4 (upresis «råvariabler») i § 5.2 samt F3 (norske segmentkoder i Tabell 7.2).~~ Gjennomført.
4. ~~**(Bør)** Oppdater utvalgsdokumentet § 3 med generell regel om nummerering på tvers av underseksjoner (V2), og velg A eller B for Tabell 12.1 (F2).~~ Gjennomført (valg A: Tabell 12.1 beholdes, utvalget teller nå 16 innholdstabeller).
5. ~~**(Kan)** Vurder F4 (drop ID-kolonnen i Tabell 9.2) og F1 (intern-henvisninger i kap. 7) – begge hører naturlig til 7.3.1.~~ Gjennomført (F4 droppet i rapport, F1 notert i status.md under WBS 7.3.1).
