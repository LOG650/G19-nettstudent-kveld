# Review av aktivitet 7.3.1 – «Struktur- og kravsjekk av rapportutkast»

**Reviewer:** Claude
**Dato:** 2026-04-21
**Aktivitetsmappe:** [005 report/](../../005%20report/) og [012 fase 2 - plan/](../)
**Planreferanse:** WBS 7.3.1 «Gjennomføre struktur- og kravsjekk av rapportutkastet», planlagt 2026-04-21

---

## Sammendrag

Rapporten følger CLAUDE.md § Rapportstruktur og § Rapportsjekkliste på alle faglig-innholdsmessige punkter, og alle syv baselinekrav (KR-001 til KR-007) er dekket i teksten. Hovedsvakhet er at tittelsiden og de administrative forsideerklæringene (linje 1–93) fortsatt er mal-plassholdere uten utfylt innhold. Tre middels svakheter gjelder nummereringsgap i Tabell 5.x (starter på 5.2), manglende TOC-oppføringer for § 3.1–3.4, og inkonsistent overskriftsnivå i kap. 1 (`##` i stedet for `###` for 1.1–1.4). Tre lave forbedringsforslag gjelder språkdetaljer og kildegrunnlag. F1 fra 7.2-helhetsreviewen ble lukket 2026-04-21 før denne reviewen startet.

**Totalt:** 6 styrker, 4 svakheter (1 Høy, 3 Middels, 0 Lav), 3 forbedringsforslag (Lav).

---

## Styrker

- **S1.** Kapittelstrukturen i kap. 1–12 følger CLAUDE.md § Rapportstruktur presist: Sammendrag (linje 97, 277 ord), Abstract (linje 105, 298 ord), kap. 1 Innledning med §§ 1.1–1.4, kap. 2 Litteratur, kap. 3 Teori med §§ 3.1–3.4, kap. 4 Casebeskrivelse med §§ 4.1–4.4, kap. 5 Metode og data med §§ 5.1–5.2, kap. 6 Modellering, kap. 7 Analyse, kap. 8 Resultat, kap. 9 Diskusjon med §§ 9.1–9.5, kap. 10 Konklusjon, kap. 11 Bibliografi og kap. 12 Vedlegg.
- **S2.** Problemstillingen (linje 157) er formulert som «hvordan»-spørsmål og fanger inn både modellkomponenten og variabelkomponenten av prosjektet. § 1.2 Delproblemer (linje 159–164) splitter den i to presise delspørsmål som følges opp konsekvent gjennom kap. 7–10.
- **S3.** Avgrensinger (linje 166–174) og Antagelser (linje 176–183) er begge faglig begrunnet; antakelsene har eksplisitte `*Konsekvens:*`-ledd slik CLAUDE.md-sjekklisten krever.
- **S4.** Figur- og tabellnummereringen ble omnummerert i 7.2.4 slik at den matcher tekstrekkefølgen (formkrav 1) i kap. 8 og kap. 9. F1 fra helhetsreviewen av 7.2 er lukket 2026-04-21 ved å endre to henvisninger i kap. 7 til lokale Tabell 7.1/7.2 (jf. status.md linje 79).
- **S5.** Inline matematikk bruker konsekvent `$...$`-notasjon (linje 209, 215, 241, 247 m.fl.). Ingen forekomster av `\(...\)` i filen.
- **S6.** Rapporten er 706 linjer UTF-8 uten BOM; norske tegn `æ`, `ø`, `å` er bevart, og alle 10 figurer bruker HTML-mønsteret fra CLAUDE.md med `width="80%"` og sentrert kursiv figurtekst.

---

## Del 1 – Strukturvurdering mot CLAUDE.md

### 1.1 Rapportstruktur per § Rapportstruktur

| Element | Forventet (CLAUDE.md) | Funn i [rapport.md](../../005%20report/rapport.md) | Status |
|:---|:---|:---|:---|
| Tittel/forside | tittel, forfatter(e), sidetall, innleveringsdato | Linje 1–93: alle felt er mal-plassholdere og ikke utfylt | **V1 – Høy** |
| Sammendrag | kort norsk oppsummering | Linje 97–103, 277 ord, dekker problem/metode/funn/konklusjon | OK |
| Abstract | kort engelsk oppsummering | Linje 105–111, 298 ord | OK |
| Innhold | oppdatert innholdsfortegnelse | Linje 115–144: mangler §§ 3.1–3.4 | **V3 – Middels** |
| 1 Innledning | tema/relevans/problemstilling-overgang | Linje 147–153 | OK |
| 1.1 Problemstilling | presist hovedspørsmål | Linje 155–157 | OK |
| 1.2 Delproblemer | bare hvis trengs | Linje 159–164, to delspørsmål | OK |
| 1.3 Avgrensinger | faglig begrunnet | Linje 166–174 | OK |
| 1.4 Antagelser | med konsekvenser | Linje 176–183 | OK |
| 2 Litteratur | knyttet til problemstilling | Linje 187–197 | OK |
| 3 Teori | fagbegrep for senere bruk | Linje 201–261, §§ 3.1–3.4 | OK (innhold) |
| 4 Casebeskrivelse | bedrift + historiske fakta | Linje 265–308, §§ 4.1–4.4 | OK |
| 5 Metode og data | tilnærming + datasplitt | Linje 312–419, §§ 5.1–5.2 | OK |
| 6 Modellering | konkret modellvalg | Linje 423–451 | OK |
| 7 Analyse | modelloppførsel + tolkning | Linje 455–519 | OK |
| 8 Resultat | nøkterne funn | Linje 523–602 | OK |
| 9 Diskusjon | mot problemstilling + begrensninger | Linje 606–670, §§ 9.1–9.5 | OK |
| 10 Konklusjon | svarer på problemstilling | Linje 674–678 | OK |
| 11 Bibliografi | konsistent referanseliste | Linje 682–690 | OK (se F3) |
| 12 Vedlegg | supplerende materiale | Linje 692–706, Tabell 12.1 | OK (se F2) |

### 1.2 Rapportsjekkliste per § Rapportsjekkliste

| Sjekkpunkt | Vurdering | Kommentar |
|:---|:---|:---|
| Innledning kort og presis (1–2 sider) | OK | Linje 147–184, kompakt og poengtert |
| Innledning aktualiserer tema | OK | Linje 149–151 |
| Casebedriften kort nevnt, detaljer i kap. 4 | OK | «en simulert dagligvarekjede», ingen detaljer foregripes |
| Problemstilling som hvordan-spørsmål | OK | Linje 157 |
| Problemstilling presist avgrenset | OK | Dekker både modell og variabel uten å bli bred |
| Delproblemer brukt kun når trengs | OK | To delspørsmål matcher analysen i kap. 7–9 |
| Avgrensinger faglig begrunnet | OK | Ingen tidsargumenter |
| Antagelser med konsekvenser | OK | 4/4 har `*Konsekvens:*`-ledd |
| Litteratur knytter kilder til problemstilling | OK | Linje 195–197 diskuterer direkte modellvalg |
| Teori gir grunnlag for metode | OK | § 3.3 definerer RMSE/MAPE som senere brukes |
| Resultat nøkternt | OK | Kap. 8 presenterer funn uten vurdering |
| Diskusjon separat fra resultat | OK | Vurderinger samlet i kap. 9 |
| Konklusjon svarer direkte på problemstilling | OK | Linje 674 starter med «Problemstillingen spør …» |

### 1.3 TOC-konsistens — V3

TOC (linje 115–144) mangler oppføringer for alle fire underkapittel i kap. 3:

- § 3.1 Multippel lineær regresjon (linje 205)
- § 3.2 Random Forest Regressor (linje 221)
- § 3.3 Evalueringsmetrikker (linje 235)
- § 3.4 Feature engineering og dataoppsett (linje 253)

TOC listes §§ 1.1–1.4, 4.1–4.4, 5.1–5.2 og 9.1–9.5 fullstendig, men hopper over kap. 3 sine fire underkapittel. Dette er en TOC-inkonsistens og tilhører 7.3.1-scope.

### 1.4 Overskriftsnivå — V4

Alle underkapitler i hele rapporten unntatt kap. 1 bruker `### ` (H3):

- §§ 3.1–3.4, 4.1–4.4, 5.1–5.2, 9.1–9.5: alle `###`

I kap. 1 brukes derimot `## ` (H2) for §§ 1.1–1.4 (linje 155, 159, 166, 176). Dette gir H2 både for «1 Innledning» (linje 147) og for «1.1 Problemstilling» — samme nivå for overordnet kapittel og underkapittel. Bryter med den konsistente nesting-regelen i resten av rapporten og vil også gi feil TOC-innrykk hvis TOC regenereres.

---

## Del 2 – Formkrav (figurer og tabeller)

### 2.1 Figur- og tabellinventar

10 figurer:

| Figur | Kapittel | Linje tekst | Linje bildeblokk |
|:---|:---|:---|:---|
| 4.1 | § 4.1 | 273 | 275–278 |
| 4.2 | § 4.2 | 284 | 286–289 |
| 4.3 | § 4.3 | 295 | 297–300 |
| 5.1 | § 5.2 | 326 | 328–331 |
| 5.2 | § 5.2 | 405 | 407–410 |
| 7.1 | kap. 7 | 482 | 484–487 |
| 7.2 | kap. 7 | 489 | 491–494 |
| 8.1 | kap. 8 | 535 | 537–540 |
| 8.2 | kap. 8 | 569 | 571–574 |
| 8.3 | kap. 8 | 576 | 578–581 |

16 innholdstabeller:

| Tabell | Kapittel | Linje intro | Linje caption |
|:---|:---|:---|:---|
| **5.2** | § 5.2 | 335 | 351 |
| 5.3 | § 5.2 | 353 | 376 |
| 5.4 | § 5.2 | 378 | 401 |
| 5.5 | § 5.2 | 412 | 419 |
| 6.1 | kap. 6 | 427 | 435 |
| 6.2 | kap. 6 | 441 | 451 |
| 7.1 | kap. 7 | 461 | 478 |
| 7.2 | kap. 7 | 498 | 517 |
| 8.1 | kap. 8 | 525 | 533 |
| 8.2 | kap. 8 | 542 | 550 |
| 8.3 | kap. 8 | 552 | 567 |
| 8.4 | kap. 8 | 583 | 602 |
| 9.1 | § 9.1 | 614 | 622 |
| 9.2 | § 9.3 | 634 | 643 |
| 9.3 | § 9.4 | 651 | 662 |
| 12.1 | kap. 12 | (mangler) | 706 |

### 2.2 Formkrav 1 – nummerering følger omtalerekkefølge — V2

Figurene er i rekkefølge i alle kapittel. Tabellene er i rekkefølge **innenfor hvert kapittel**, men **nummereringen i kap. 5 starter på 5.2** (første tabell er Tabell 5.2 på linje 335). Dette gir et gap der Tabell 5.1 mangler, og bryter med «nummereres i den rekkefølgen de omtales».

Bakgrunn: I 7.2.4 ble den opprinnelige Tabell 5.1 (som sto sist i § 5.2) renummerert til Tabell 5.5 for å reparere rekkefølgebruddet. Renummereringen løste tekstrekkefølgen, men skapte et nytt gap i begynnelsen siden Tabell 5.2 ikke ble renummerert til 5.1 samtidig.

**Anbefalt tiltak:** Renummerer kjeden i kap. 5:

- Tabell 5.2 → Tabell 5.1
- Tabell 5.3 → Tabell 5.2
- Tabell 5.4 → Tabell 5.3
- Tabell 5.5 → Tabell 5.4

Påvirker caption- og introduksjonslinjer 335, 351, 353, 376, 378, 401, 412, 419. Andre kapitler refererer ikke til Tabell 5.x, så ingen kryssreferanser brytes.

### 2.3 Formkrav 2 – inline matematikk med `$...$`

Grep etter `\(` eller `\)`: 0 forekomster. Alle matematiske uttrykk bruker `$...$` som CLAUDE.md krever.

### 2.4 Formkrav 3 – HTML-figurmønster

Alle 10 figurer bruker `<div align="center"> … width="80%" … <p align="center"><small><i>Figur X.Y …</i></small></p></div>`. Ingen avvik.

### 2.5 Tabelltittel – F2

Tabell 12.1 (linje 706) har caption, men **mangler introduksjonssetning** i stil med «Tabell 12.1 viser vedleggsreferanser …» som alle andre tabeller har (jf. CLAUDE.md § Tabeller: «Tabeller skal ha en kort introduksjonssetning i brødteksten før de settes inn»). Innledningen til kap. 12 (linje 694) beskriver innholdet generelt, men introduserer ikke tabellen ved nummer.

### 2.6 Figurhenvisning med liten bokstav – F1

Linje 306: «Sesongvariasjonen i figur 4.3 viser …» — bruker liten «f» mens alle andre henvisninger (linje 273, 284, 295, 326, 405, 482, 489, 535, 569, 576) bruker stor «F».

---

## Del 3 – Kravsjekk (KR-001 til KR-007)

| Krav | Beskrivelse | Dekkes i rapport | Status |
|:---|:---|:---|:---|
| KR-001 | Salgsprognoser for 2025 basert på 2022–2024 | § 5.1 metodebeskrivelse, kap. 6 modellering (Tabell 6.1), kap. 7 (Tabell 7.1), kap. 8 (Tabell 8.1), vedlegg A1 | **OK** |
| KR-002 | To modeller (MLR + RF) utviklet og evaluert | Tabell 6.1 (linje 427–435): lineær + baseline RF + tuned RF, evaluert kap. 7 og 8 | **OK** (leverer tre spor, oppfyller to-modell-kravet med margin) |
| KR-003 | MAPE og RMSE dokumentert | § 3.3 definisjon, Tabell 7.1 månedlig, Tabell 7.2 segmentvis, Tabell 8.1 samlet, Tabell 8.2 vinnertelling | **OK** |
| KR-004 | Identifisere og rangere variabler etter påvirkning | § 9.2, Tabell 8.3 (topp 10 feature importance), Figur 8.2 og 8.3, vedlegg A4 og A5 | **OK** |
| KR-005 | Strukturert, kvalitetssikret og dokumentert datagrunnlag | Tabell 5.2–5.5 (variabler, FE, rens, splitt), § 5.2 tekst, vedlegg A1–A7 | **OK** |
| KR-006 | Resultat, metodevalg og forutsetninger etterprøvbar | § 3.1–3.4 teori, § 5.1 metode, § 6 modelloversikt, [006 analysis/](../../006%20analysis/) med `uv`-oppsett, vedlegg A1–A7 | **OK** |
| KR-007 | Innen avtalte tids- og ressursrammer | Gantt-plan og status.md. M1, M2, M3 (forsinket), M4 og nå praktisk M5 er nådd. Formell M5 (8. april) ble nådd 19. april (11 dager forsinket). M6 (19. mai) ikke startet. | **Delvis – M5 dokumentert forsinket** |

**KR-007-forbehold:** M5-forsinkelsen er implisitt synlig i [status.md](../status.md) (milepælseksjonen), men det finnes ingen egen endringslogg-oppføring eller eksplisitt planavviksnotat. Dette er et oppfølgingspunkt mer enn et rapportfeil, men bør flyttes til eksplisitt dokumentasjon før prosjektavslutning.

---

## Svakheter og forbedringsforslag

### V1. Tittelsiden og forsideerklæringene er fortsatt mal-plassholdere

**Alvorlighetsgrad:** Høy
**Kategori:** Språk og innhold

Linje 1–93 er uendret fra malen:

- Linje 1: `# Tittel (norsk og/eller engelsk)` – tittel ikke fylt ut
- Linje 5: `Forfatter(e):` – tomt
- Linje 7: `Totalt antall sider inkludert forsiden:` – tomt
- Linje 9: `Molde, Innleveringsdato:` – tomt
- Linje 22–29: Egenerklæring/gruppeerklæring del 1–6, alle seks avkryssingsfelt er `☐`
- Linje 37–44: Personvern/NSD ikke fylt ut
- Linje 51–56: Helseforskningsloven/REK ikke fylt ut
- Linje 62–76: Publiseringsavtale ikke fylt ut (Studiepoeng, Veileder, publiseringsvalg)
- Linje 83: «Dato:» tomt
- Linje 89: «Antall ord» – placeholder-tekst
- Linje 93: «Forfattererklæring» – placeholder-tekst

**Konsekvens:** Rapporten kan ikke leveres i nåværende form. Tilhører formelle innleveringskrav snarere enn faglig innhold, men hører hjemme i struktur- og kravsjekken fordi den faller inn under § Rapportstruktur-«Tittel/forside»-kravet.

**Anbefalt tiltak:** Fyll ut alle feltene på forsiden. Prosjektleder og teammedlemmene er dokumentert i [prosjektstyringsplan.md](../prosjektstyringsplan.md) § Prosjektteam, og kan brukes som kilde for forfatterlisten. Studiepoeng og veileder må hentes fra studieplanen. Antall ord kan telles med `wc -w` på filen med forsidetekst ekskludert.

### V2. Tabell 5.x starter på Tabell 5.2 — bryter formkrav 1

**Alvorlighetsgrad:** Middels
**Kategori:** Språk og innhold / formkrav

Første tabell i kap. 5 er Tabell 5.2 (linje 335). Tabell 5.1 eksisterer ikke, slik at nummereringen har et gap i starten. Dette bryter «nummereres separat og i den rekkefølgen de omtales» i utvalgsdokumentet § 3 regel 1.

**Bakgrunn:** I 7.2.4 ble den opprinnelige Tabell 5.1 (tog/test-splittens antallsfordeling, sto sist i § 5.2) renummerert til Tabell 5.5 for å rette rekkefølgen. Renummereringen skulle samtidig flyttet 5.2→5.1, 5.3→5.2, 5.4→5.3 og 5.5→5.4, men det siste steget ble ikke utført.

**Anbefalt tiltak:** Renummerer kjeden i kap. 5 (se § 2.2 over). Påvirker åtte linjer i rapport.md (fire intro- og fire caption-linjer) og én linje i [rapport_fig_tab_utvalg.md](../rapport_fig_tab_utvalg.md) for konsistens i sporbarheten. Ingen kryssreferanser finnes fra andre kapittel.

### V3. TOC mangler oppføringer for §§ 3.1–3.4

**Alvorlighetsgrad:** Middels
**Kategori:** Språk og innhold

Innholdsfortegnelsen (linje 115–144) har `- [3 Teori](#3-teori)` uten underkapitler, selv om rapporten har fire tydelige underkapittel: § 3.1 Multippel lineær regresjon (linje 205), § 3.2 Random Forest Regressor (linje 221), § 3.3 Evalueringsmetrikker (linje 235), § 3.4 Feature engineering og dataoppsett (linje 253). Andre kapitler (1, 4, 5, 9) lister underkapitlene sine i TOC.

**Anbefalt tiltak:** Legg til fire linjer i TOC etter linje 123 (før «- [4 Casebeskrivelse]»):

```markdown
- [3 Teori](#3-teori)
  - [3.1 Multippel lineær regresjon](#31-multippel-lineær-regresjon)
  - [3.2 Random Forest Regressor](#32-random-forest-regressor)
  - [3.3 Evalueringsmetrikker](#33-evalueringsmetrikker)
  - [3.4 Feature engineering og dataoppsett](#34-feature-engineering-og-dataoppsett)
```

### V4. Inkonsistent overskriftsnivå i kap. 1

**Alvorlighetsgrad:** Middels
**Kategori:** Språk og innhold / formkrav

§§ 1.1–1.4 bruker `## ` (H2) i stedet for `### ` (H3) som resten av rapporten:

- Linje 155: `## 1.1 Problemstilling`
- Linje 159: `## 1.2 Delproblemer`
- Linje 166: `## 1.3 Avgrensinger`
- Linje 176: `## 1.4 Antagelser`

Dette gir `## 1 Innledning` og `## 1.1 Problemstilling` på samme nivå. §§ 3.1–3.4, 4.1–4.4, 5.1–5.2, 9.1–9.5 bruker derimot `### `. Konsekvensen er at automatiske TOC-genererings- og referanseverktøy (f.eks. markdownlint, VS Code outline) feilaktig behandler 1.1–1.4 som søskenkapitler til «1 Innledning».

**Anbefalt tiltak:** Endre `## ` til `### ` på linje 155, 159, 166 og 176.

### F1. Liten «f» i figurhenvisning

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Linje 306: «Sesongvariasjonen i figur 4.3 viser at …» bruker liten bokstav. Alle andre figurhenvisninger i rapporten bruker stor «F» (linje 273, 284, 295, 326, 405, 482, 489, 535, 569, 576).

**Anbefalt tiltak:** Endre «figur 4.3» til «Figur 4.3» på linje 306. Tilhører egentlig WBS 7.3.3 språkvask, men noteres her siden den ble oppdaget i strukturgjennomgangen.

### F2. Tabell 12.1 mangler introduksjonssetning

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Kap. 12 (linje 692–706) gir ingen introduksjonssetning for Tabell 12.1 i stil med «Tabell 12.1 oppsummerer vedleggsreferansene …». CLAUDE.md § Tabeller krever at tabeller skal ha en kort introduksjonssetning i brødteksten før de settes inn. Andre tabeller i rapporten følger dette mønsteret konsekvent (f.eks. linje 335, 353, 378, 412, 427, 441, 461, 498, 525, 542, 552, 583, 614, 634, 651).

**Anbefalt tiltak:** Legg til én setning før tabellen, f.eks. «Tabell 12.1 lister vedleggsreferansene A1–A7 med innhold og kildefil.»

### F3. Litteraturen bygger kun på ikke-fagfellevurderte kilder

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Bibliografien (linje 682–690) har fire oppføringer, alle fra IBM Think Topics eller GeeksforGeeks. Rapporten anerkjenner dette selv (linje 197): «De tilgjengelige kildene … er webbaserte oppslagsverk … ikke fagfellevurderte vitenskapelige artikler.»

**Anbefalt tiltak:** Ingen endring i 7.3-fasen; bør vurderes som et åpent punkt for eventuell revisjon i WBS 8.1 dersom akademisk dybde skal styrkes før endelig innlevering. Dette er allerede flagget i § 1.3 og i § 9.5 «Videre arbeid».

---

## Avhukningsliste – tiltak

| # | Tiltak | Kategori | Status | Kommentar |
|:--|:-------|:---------|:-------|:----------|
| V1 | Fyll ut forsiden (tittel, forfattere, dato, erklæringer, publiseringsavtale, ordtelling) | Formelle | [x] | Gjennomført 2026-04-21. Tittel, forfattere, studiepoeng (15), veileder (BIP), alle seks egenerklæringer, personvern/helseforskning (ikke omfattet), publisering (Ja) og båndlegging (Nei) er fylt ut. Innleveringsdato, sidetall og dato står som TODO til like før innlevering. Antall ord ca. 5 300 for hovedtekst kap. 1–10. |
| V2 | Renummerer Tabell 5.2→5.1, 5.3→5.2, 5.4→5.3, 5.5→5.4 | Formkrav | [x] | Gjennomført 2026-04-21. Åtte linjer i [rapport.md](../../005%20report/rapport.md) renummerert. Sporbarhet oppdatert i [rapport_fig_tab_utvalg.md](../rapport_fig_tab_utvalg.md) og [rapport_7_2_2_artefakter.md](../rapport_7_2_2_artefakter.md). |
| V3 | Legg til §§ 3.1–3.4 i TOC (linje 123 i rapport.md) | Struktur | [x] | Gjennomført 2026-04-21. Fire linjer lagt til etter «- [3 Teori]»-oppføringen. |
| V4 | Endre `##` til `###` for §§ 1.1–1.4 (linje 155, 159, 166, 176) | Formkrav | [x] | Gjennomført 2026-04-21. Alle fire overskrifter endret til H3. |
| F1 | Endre «figur 4.3» til «Figur 4.3» (linje 306) | Språk | [—] | Overført til WBS 7.3.3 språkvask. |
| F2 | Legg til introduksjonssetning for Tabell 12.1 (før linje 696) | Språk og innhold | [—] | Overført til WBS 7.3.3 språkvask. |
| F3 | Vurder fagfellevurdert kildegrunnlag | Språk og innhold | [—] | Utsatt til WBS 8.1 vurdering. |
| KR-007 | Dokumentere M5-forsinkelsen eksplisitt | Prosjektstyring | [—] | Overført til WBS 8.1. |

---

## Samsvar med prosjektplan og krav

| Sjekkpunkt | Status | Kommentar |
|:---|:---|:---|
| § Rapportstruktur – tittelside | Gjenstår | V1 |
| § Rapportstruktur – sammendrag/abstract/innhold | OK (innhold), Delvis (innhold-TOC) | V3 mangler 3.1–3.4 |
| § Rapportstruktur – kap. 1–12 til stede | OK | Alle kapitler funnet |
| § Rapportsjekkliste (13 punkter) | OK | Alle punkter passert |
| § Figurer HTML-mønster | OK | 10/10 figurer følger mønsteret |
| § Tabeller introduksjonssetning | Delvis | F2 for Tabell 12.1 |
| § Tabeller tabelltekst | OK | Alle 16 har caption |
| Formkrav 1 (nummerering) | Delvis | V2 Tabell 5.x |
| Formkrav 2 (`$...$`) | OK | 0 forekomster av `\(...\)` |
| KR-001 til KR-006 | OK | Kravmatrise i Del 3 |
| KR-007 | Delvis | M5 forsinket, ikke eksplisitt dokumentert |

---

## Samlet vurdering

### Struktur og innhold

Rapporten er faglig komplett og følger CLAUDE.md § Rapportstruktur og § Rapportsjekkliste på alle innholdsmessige punkter. De 13 punktene i sjekklisten er passert, og de 7 baselinekravene er dekket. Tittelsiden (V1) er det ene blokkerende gapet for formell innlevering.

### Formkrav

Tre formkravavvik identifisert: V2 (tabellnummerering 5.x), V3 (TOC mangler 3.1–3.4) og V4 (feil H2/H3-nivå i kap. 1). Alle er enkle å rette (≤15 linjer rediger totalt) og bør gjennomføres som del av 7.3.1 før 7.3.2 starter.

### Anbefalt prioritering videre

1. **(Må)** V1 – Fyll ut tittelsiden. Blokkerer innlevering.
2. **(Må)** V2 – Renummerer Tabell 5.x (bryter formkrav 1). Gjennomføres før 7.3.2 konsistenssjekk.
3. **(Må)** V3 – Oppdater TOC med 3.1–3.4.
4. **(Må)** V4 – Rett H2→H3 for §§ 1.1–1.4.
5. **(Bør)** F2 – Introduksjonssetning for Tabell 12.1.
6. **(Bør)** KR-007 – Dokumenter M5-forsinkelsen i endringsloggen.
7. **(Kan)** F1 – «Figur 4.3» med stor F; kan tas som del av 7.3.3 språkvask.
8. **(Kan)** F3 – Fagfellevurderte kilder; utsettes til WBS 8.1 vurdering.

### Lukkebeslutning for WBS 7.3.1

Reviewen er lukket 2026-04-21. V1–V4 er rettet og avhukningslista viser `[x]` for alle fire. F1 og F2 er overført til WBS 7.3.3 språkvask, og F3 og KR-007-notat er overført til WBS 8.1. WBS 7.3.1 er satt til 100 % i [wbs.json](../wbs.json) og avhuket i [status.md](../status.md).
