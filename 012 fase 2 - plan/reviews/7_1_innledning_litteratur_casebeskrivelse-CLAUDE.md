# Review av aktivitet 7.1.1–7.1.3 – Innledning, litteratur og casebeskrivelse

**Reviewer:** Claude (automatisk review)
**Dato:** 2026-04-13
**Aktivitetsmappe:** `005 report/rapport.md` (kapittel 1–4)
**Planreferanse:** WBS 7.1.1 (fullført 2026-04-13), WBS 7.1.2 (fullført 2026-04-13), WBS 7.1.3 (fullført 2026-04-13)

---

## Sammendrag

Tre rapportkapitler er reviewet samlet: innledning med problemstilling, avgrensinger og antagelser (kap. 1), litteratur (kap. 2), teori (kap. 3) og casebeskrivelse (kap. 4). Arbeidet er solidt fundamentert: problemstilling, antagelser og teoripresentasjon er godt utført. Det er funnet én faktisk feil i kap. 3.4 (trenings-/testoppsett beskrevet feil) og én typografi-feil, som begge bør rettes. To middels svakheter gjelder grenseproblematikk mellom kap. 4 og kap. 5, og innholdsduplisering mellom kap. 1 og 4.4. Fire forbedringsforslag er identifisert, ingen av dem blokkerende.

**Totalt:** 7 styrker, 6 svakheter (1 Høy, 3 Middels, 2 Lav), 4 forbedringsforslag (1 Middels, 3 Lav).

---

## Styrker

- **S1.** Problemstillingen (kap. 1.1) er presist formulert som et «hvordan»-spørsmål, er avgrenset til to konkrete modelltyper og ett datasett, og er ikke bredere enn det rapporten faktisk kan svare på.
- **S2.** Antagelsene (kap. 1.4) er eksplisitt merket med konsekvenser for analysens gyldighet — dette er faglig sett godt utført og over forventet nivå for studentprosjekter.
- **S3.** Avgrensningene (kap. 1.3) er faglig begrunnet, ikke tidsbasert. Alle fem avgrensninger har en konkret begrunnelse.
- **S4.** Teorikapitlet (kap. 3.1–3.3) gir matematiske formler med presis norsk forklaring og kobler dem direkte til prosjektets brukstilfelle (f.eks. multikollinearitet knyttes til one-hot-kodede variabler).
- **S5.** RMSE vs. MAPE-diskusjonen (kap. 3.3) forklarer når metrikkene kan peke i ulik retning — dette er nyttig kontekst for tolkning av resultatene i kap. 7–8.
- **S6.** Figurene i kap. 4 er riktig formatert med HTML, `width="80%"`, sentrert figurtekst, liten skrift og kursiv, i tråd med CLAUDE.md.
- **S7.** Numeriske verdier i kap. 4 (gjennomsnitt 1 497, spenn 500–2 500, regionfordeling) er konsistente med `tab_eda_oversikt.csv` og `tab_kategorisk_fordeling.csv`.

---

## Del 1 – Metodikk (beregninger og kode)

Disse aktivitetene er rene rapportskriveaktiviteter uten analysekode. Del 1 vurderer faktisk korrekthet i tallmateriale og konsistens mellom rapport og analyseartefakter.

### 1.1 Konsistens rapport ↔ analyseartefakter

Tallene i kap. 1 og kap. 4 er kryssjekket mot `tab_eda_oversikt.csv`, `tab_kategorisk_fordeling.csv` og `eda_visualisering.md`.

- Gjennomsnitt 1 497, spenn 500–2 500, standardavvik 578: **stemmer** (`tab_eda_oversikt.csv`)
- Treningsgjennomsnitt 1 493, testgjennomsnitt 1 503: **stemmer**
- West 32 %, East 28 %, Central 23 %, South 16 %, North 0,01 %: **stemmer**
- Eggs, Meat & Fish høyest gjennomsnittlig salgsnivå: **stemmer** (`eda_visualisering.md`)
- Oktober høyest, juni lavest: **stemmer** (`eda_visualisering.md`)

**Vurdering:** God konsistens mellom rapport og artefakter.

### 1.2 Faktisk feil i kap. 3.4 – trenings-/testoppsett

Kap. 3.4 avsluttes med: *«Treningsdata er 2022–2023, valideringsdata er 2024 og testdata er 2025.»*

Dette beskriver kun tuning-oppsettet fra WBS 4.4, der 2024 brukes som intern valideringsperiode. Hovedmodellene (lineær regresjon og Random Forest baseline) trenes på **2022–2024** og testes på 2025. Å si at treningsdata er 2022–2023 er faktisk feil for det generelle oppsettet og kan forvirre leseren.

**Vurdering:** Høy alvorlighetsgrad — feil vil skape forvirring og bør rettes i neste skrivesteg.

### Gjenstående metodiske observasjoner

Litteraturkapitlet erkjenner selv at kildene er webbaserte oppslagsverk, ikke fagfellevurderte. Dette er ikke en feil, men en kjent begrensning som er dokumentert.

---

## Del 2 – Språk, innhold og figurer

### 2.1 Kap. 1 – Innledning, problemstilling, avgrensinger, antagelser

**Språk:** Setningene er klare og godt formulert. To minuspunkter:
- «metodetrandisjoner» (kap. 2, første setning) er trolig trykkfeil for «metodetradisjoner».
- «supervísert læringsmetode» (kap. 3.1) — aksentmerket «í» er et uvanlig trekk i norsk og trolig en autocorrect-artefakt. Bør skrives «supervisert» eller «veiledet».

**Faglig innhold:** Innledningen (kap. 1) omtaler «9 994 daglige salgsrader» — dette er detalj som egner seg bedre i kap. 4 og 5. Innledningen bør aktualisere temaet, ikke presentere datasettet. Setningene er ellers presise og velbegrunnede.

Kap. 1.4, antagelse 4, beskriver testsett-oppsettet korrekt («2025-dataene er holdt helt utenfor trening»), men er inkonsistent med kap. 3.4 som oppgir «treningsdata er 2022–2023» (se V1 nedenfor).

### 2.2 Kap. 2 – Litteratur

**Faglig innhold:** Litteraturen er knyttet direkte til problemstillingen og de valgte metodene — dette er i tråd med CLAUDE.md-kravet om at litteraturkapitlet skal knytte kilder til problemstillingen, ikke bare oppsummere referanser. Den siste avsnitt erkjenner kildenes begrensning, noe som er faglig ryddig.

Påstanden om at Random Forest «håndterer manglende data godt» (kap. 2) gjelder den generelle algoritmen men er ikke dekkende for scikit-learn-implementasjonen som krever fullstendige data. Dette er en nyanseringssvakhet, men ikke en kritisk feil siden datasettet i prosjektet allerede er komplett.

### 2.3 Kap. 3 – Teori

**Faglig innhold:** Teorien er presis og forklarer OLS, bagging, feature randomness, feature importance, RMSE, MAPE og tidsbasert oppsplitting på en faglig korrekt måte. Matematikken er riktig.

Kap. 3.4 avsluttes med et feil oppsett (se pkt. 1.2 over).

### 2.4 Kap. 4 – Casebeskrivelse

**Faglig innhold — grenseproblematikk mot kap. 5:**
Kap. 4.1 inneholder regionfordeling i prosent og antall byer (24) og antall observasjoner (9 994). Dette er primært datainformasjon som hører hjemme i kap. 5.2. Kap. 4.1 bør fokusere på bedriftsbeskrivelse og beslutningssituasjon; datasetttallene bør flyttes til kap. 5.2 (Data).

Kap. 4.2 inneholder setningen «Den stabile fordelingen mellom periodene er et gunstig trekk ved datasettet, da det indikerer at historiske mønstre trolig er relevante for å predikere 2025.» Dette er en metodebetraktning (begrunnelse for tidsbasert splitt) som hører hjemme i kap. 5 (Metode og data), ikke i casebeskrivelsen.

**Duplisering mellom kap. 1 og kap. 4.4:**
Begge omtaler svinn, bundet kapital og utsolgte varer i nesten samme ordlag. Innledningen sier: «for høye bestillinger fører til svinn og bundet kapital, mens for lave bestillinger gir utsolgte varer og tapte inntekter.» Kap. 4.4 sier: «For høye bestillinger fører til svinn av ferskvarer og bundet kapital i lager [...] For lave bestillinger gir utsolgte varer, tapte inntekter [...]». Kap. 4.4 bør differensieres fra innledningen, for eksempel ved å knytte utfordringene mer spesifikt til Dagligvare og de konkrete produktkategoriene.

### 2.5 Figurer – rapportklarhet

| Figur | Fil | Format | Figurtekst | Vurdering |
|:------|:----|:-------|:-----------|:----------|
| 4.1 | `fig_sales_per_category.png` | HTML, 80%, sentrert | Kursiv, nummerert | OK |
| 4.2 | `fig_sales_over_tid_train_test.png` | HTML, 80%, sentrert | Kursiv, nummerert | OK |
| 4.3 | `fig_sales_per_month_split.png` | HTML, 80%, sentrert | Kursiv, nummerert | OK |

Alle tre figurer er korrekt formatert. Figurstiene er relative fra `005 report/` og eksisterer i filsystemet.

---

## Svakheter og forbedringsforslag

### V1. Faktisk feil – trenings-/testoppsett i kap. 3.4

**Alvorlighetsgrad:** Høy
**Kategori:** Faglig innhold

Kap. 3.4 sier «Treningsdata er 2022–2023, valideringsdata er 2024 og testdata er 2025.» Det generelle treningsoppsettet bruker 2022–2024 som treningsdata og 2025 som test. 2024 som valideringsperiode gjelder kun hyperparametertuning (WBS 4.4). Teksten bør skille mellom de to oppsettene, f.eks.: «Treningsdata er 2022–2024 og testdata er 2025. I WBS 4.4 brukes 2024 i tillegg som intern valideringsperiode for hyperparametertuning av Random Forest.»

### V2. Metodebetraktning plassert i casebeskrivelse (kap. 4.2)

**Alvorlighetsgrad:** Middels
**Kategori:** Rapportstruktur

Setningen «Den stabile fordelingen mellom periodene er et gunstig trekk ved datasettet [...] indikerer at historiske mønstre trolig er relevante for å predikere 2025» er en metodebegrunnet vurdering av train/test-splitten, ikke en historisk faktabeskrivelse av caset. Bør flyttes til kap. 5 (Metode og data).

### V3. Innholdsduplisering mellom kap. 1 og kap. 4.4

**Alvorlighetsgrad:** Middels
**Kategori:** Rapportstruktur

Konsekvensene av dårlige prognoser (svinn, bundet kapital, utsolgte varer) presenteres i tilnærmet lik ordlyd i både innledningen og kap. 4.4. Kap. 4.4 bør knytte utfordringene mer spesifikt til Dagligvare, for eksempel ved å nevne de sårbare produktkategoriene og sesongproblematikken som konkret kontekst, fremfor å gjenta innledningspunktene.

### V4. Datadetaljer i casebeskrivelse (kap. 4.1)

**Alvorlighetsgrad:** Middels
**Kategori:** Rapportstruktur

Regionfordeling i prosent (West 32 %, East 28 %, etc.), antall byer (24) og antall observasjoner (9 994) er datainformasjon som naturlig hører hjemme i kap. 5.2. Kap. 4.1 kan nevne at kjeden opererer i flere regioner og byer, men de konkrete prosenttallene hører til metode/data-kapitlet.

### V5. Typografifeil: «metodetrandisjoner»

**Alvorlighetsgrad:** Lav
**Kategori:** Språk

Kap. 2, første setning: «to metodetrandisjoner spesielt relevante» bør rettes til «to metodetradisjoner».

### V6. Encoding-artefakt: «supervísert»

**Alvorlighetsgrad:** Lav
**Kategori:** Språk

Kap. 3.1: «supervísert læringsmetode» — aksentmerket «í» er trolig en autocorrect-artefakt. Bør skrives «supervisert» (eller evt. «veiledet»).

---

## Forbedringsforslag

### F1. Flytt datasettdetaljer fra kap. 4.1 til kap. 5.2

**Alvorlighetsgrad:** Middels
**Kategori:** Rapportstruktur

Se V4. Regionfordeling, antall byer og observasjonstall bør flyttes til kap. 5.2 (Data) når det kapitlet skrives i WBS 7.1.4. Kap. 4.1 vil da fremstå mer som en ren casebeskrivelse.

### F2. Styrk litteraturen med minst én fagfellevurdert kilde

**Alvorlighetsgrad:** Lav
**Kategori:** Akademisk kvalitet

Rapporten erkjenner selv at kildene er webbaserte oppslagsverk. Én eller to fagfellevurderte artikler om maskinlæring for etterspørselspredikering i detaljhandel vil styrke den akademiske tyngden. Kan legges til ved ferdigstilling i WBS 7.1.6.

### F3. Fjern datasett-detalj fra innledningen

**Alvorlighetsgrad:** Lav
**Kategori:** Rapportstruktur

Kap. 1 nevner «9 994 daglige salgsrader» — dette er detalj som egner seg i kap. 4 og 5, ikke i innledningen. Innledningen bør aktualisere temaet og motivere prosjektet, ikke presentere datasettet. Kan justeres i WBS 7.1.7 (ferdigstille innledning).

### F4. Utvid kap. 4.4 med kategori-spesifikk planleggingsrisiko

**Alvorlighetsgrad:** Lav
**Kategori:** Faglig dybde

Kap. 4.4 er kortere enn de øvrige seksjonene og kan med fordel knyttes mer konkret til Dagligvares produktsortiment — for eksempel ved å peke på at ferskvarer som Eggs/Meat & Fish og Fruits & Veggies har kortere holdbarhet og dermed smalere feilmargin enn tørrvarer, noe som gjør presis prognose spesielt kritisk for disse kategoriene.

---

## Avhukningsliste – tiltak

| # | Tiltak | Kategori | Status | Kommentar |
|:--|:-------|:---------|:-------|:----------|
| V1 | Rett kap. 3.4: «Treningsdata er 2022–2024 og testdata er 2025. 2024 brukes i tillegg som valideringsperiode i WBS 4.4.» | Faglig innhold | [x] | Utført 2026-04-13 |
| V2 | Flytt metodebetraktning fra kap. 4.2 til kap. 5 | Rapportstruktur | [ ] | Utsatt til WBS 7.1.4 |
| V3 | Differenser kap. 4.4 fra innledningen | Rapportstruktur | [x] | Utført 2026-04-13 |
| V4 | Flytt regionfordeling/datatall fra kap. 4.1 til kap. 5.2 | Rapportstruktur | [ ] | Utsatt til WBS 7.1.4 |
| V5 | Rett «metodetrandisjoner» → «metodetradisjoner» | Språk | [x] | Utført 2026-04-13 |
| V6 | Rett «supervísert» → «supervisert» | Språk | [x] | Utført 2026-04-13 |
| F1 | Flytt datasettdetaljer fra kap. 4.1 til kap. 5.2 ved WBS 7.1.4 | Rapportstruktur | [ ] | |
| F2 | Vurder én fagfellevurdert kilde ved WBS 7.1.6 | Akademisk kvalitet | [ ] | |
| F3 | Fjern datasett-detalj fra innledningen ved WBS 7.1.7 | Rapportstruktur | [ ] | |
| F4 | Utvid kap. 4.4 med kategori-spesifikk risiko | Faglig dybde | [ ] | |

---

## Samsvar med prosjektplan og krav

| Sjekkpunkt | Status | Kommentar |
|:---|:---|:---|
| WBS 7.1.1 fullført: innledning, problemstilling, avgrensinger, antagelser | OK | Fullført 2026-04-13 |
| WBS 7.1.2 fullført: litteratur og teori | OK | Fullført 2026-04-13 |
| WBS 7.1.3 fullført: casebeskrivelse | OK | Fullført 2026-04-13 |
| Innledningen er kort og presis (1–2 sider) | OK | ~0,5 side |
| Problemstillingen er formulert som «hvordan»-spørsmål | OK | |
| Avgrensninger er faglig begrunnet | OK | |
| Antagelser er eksplisitte med konsekvenser | OK | |
| Litteraturen knyttes til problemstillingen | OK | |
| Teori gir grunnlag for metodevalg og tolkning | OK | |
| Casebeskrivelse er skilt fra analyse og metode | Delvis | Noen datadetaljer og metodebetraktninger er feilplassert (V2, V4) |
| Beskrivende figurer i casekapitlet, ikke i analysekapitlet | OK | Figur 4.1–4.3 er EDA-figurer, ikke analysefigurer |
| KR-005: Datagrunnlag dokumentert | OK | Kap. 4.1–4.3 |
| KR-006: Metodevalg og forutsetninger dokumentert | OK | Kap. 1.3, 1.4, 3.x |

---

## Samlet vurdering

### Metodikk

Det tekniske og faktuelle grunnlaget er solid. Tallene i kap. 4 er konsistente med analyseartefaktene. Kap. 3.1–3.3 presenterer teori korrekt og med presis matematikk. Eneste faktiske feil er i kap. 3.4 der trenings-/testoppsettet beskrives feil (kun tuning-oppsettet er oppgitt, ikke det generelle). Dette bør rettes før rapporten ferdigstilles.

### Språk, innhold og figurer

Språket er gjennomgående klart og faglig presist. To typografi-/encoding-feil er identifisert og er enkle å rette. Hoveutfordringen er strukturell: noe datainformasjon og metodevurderinger er plassert i casebeskrivelsen der de ikke hører hjemme. Innholdsdupliseringen mellom kap. 1 og 4.4 bør løses ved at kap. 4.4 differensieres og knyttes tettere til Dagligvares spesifikke sortiment og sesongmønster. Figurene er korrekt formatert.

### Anbefalt prioritering videre

1. **(Må)** Rett faktisk feil i kap. 3.4 om treningsoppsett (V1)
2. **(Bør)** Rett typografifeile: «metodetrandisjoner» og «supervísert» (V5, V6)
3. **(Bør)** Differensier kap. 4.4 fra innledningen ved å knytte utfordringene til Dagligvares faktiske kategorier (V3)
4. **(Bør)** Flytt regionfordeling/datatall og metodebetraktning fra kap. 4 til kap. 5.2 ved neste skrivesteg – WBS 7.1.4 (V2, V4)
5. **(Kan)** Fjern datasett-detalj fra innledningen ved WBS 7.1.7 (F3)
6. **(Kan)** Vurder fagfellevurdert kilde ved WBS 7.1.6 (F2)
