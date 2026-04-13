# Review av aktivitet 7.1.4 – Metode og data

**Reviewer:** Claude (automatisk review)
**Dato:** 2026-04-13
**Aktivitetsmappe:** `005 report/rapport.md` (kapittel 5)
**Planreferanse:** WBS 7.1.4 (fullført 2026-04-13)

---

## Sammendrag

Kapittel 5 (Metode og data) er skrevet og oppfyller de sentrale kravene til aktiviteten: 5.1 er omformulert fra WBS-logg til akademisk prosa, og 5.2 er komplett med datakilde, periode, variabler, datakvalitet, feature engineering og datasplitt med Tabell 5.1. Alle tall er verifisert mot analyseartefaktene. Det er funnet én grammatikkfeil og to ubehandlede strukturelle svakheter som ble utsatt fra forrige review (V2 og V4 i forrige reviewrunde). Ingen faktiske feil.

**Totalt:** 6 styrker, 4 svakheter (0 Høy, 2 Middels, 2 Lav), 1 forbedringsforslag (Lav).

---

## Styrker

- **S1.** Kap. 5.1 er omskrevet fra WBS-orientert sekvenslogg til akademisk prosa — ingen WBS-referanser, klar forskningsdesign-framing og begrunnet modellvalg.
- **S2.** Modellvalget er eksplisitt begrunnet: LR som benchmark fordi den er tolkbar, RF fordi den fanger opp ikke-lineære mønstre. Dette er faglig tilfredsstillende og kobler metodebeskrivelsen til teoridelen.
- **S3.** Kap. 5.2 dekker alle forventede elementer per CLAUDE.md-malen: datakilde, periode, observasjonstall, variabler, eksklusjoner, feature engineering og datasplitt.
- **S4.** Tabell 5.1 er verifisert mot `tab_split_oversikt.csv`: 6 682 (trening) og 3 312 (test) stemmer eksakt. Andelene ~67 % og ~33 % er korrekte (6682/9994 = 66,9 %).
- **S5.** Alle fire eksklusjoner er begrunnet per variabel — `Profit` som lekkasjevariabel, `State` som konstant, `Order ID` og `Customer Name` for overtilpasningsrisiko. Dette er solid og sporbart.
- **S6.** Datoformat-oppsplitting (4 042 `dd-mm-yyyy` + 5 952 `mm/dd/yyyy` = 9 994) stemmer med `tab_renselogg.csv` og er et konkret og sporbart kvalitetspunkt.

---

## Del 1 – Metodikk (beregninger og kode)

WBS 7.1.4 er en ren rapportskriveaktivitet. Del 1 vurderer faktisk korrekthet i tallmateriale og konsistens mellom rapport og analyseartefakter.

### 1.1 Konsistens rapport ↔ analyseartefakter

Kryssjekk av alle tallfestede påstander i kap. 5.2:

| Påstand i rapporten | Kilde | Status |
|:---|:---|:---|
| 9 994 daglige salgstransaksjoner | `tab_renselogg.csv`: antall_rader_ut = 9994 | ✓ |
| Rådata perioden 2015–2018 | `tab_renselogg.csv`: opprinnelig_periode_start = 2015-01-02, slutt = 2018-12-30 | ✓ |
| Syvårig kalenderforskyvning | `tab_renselogg.csv`: år_forskyvning = 7 | ✓ |
| 11 råkolonner | `tab_datakvalitet_etter_rens.csv`: 11 kolonner listet | ✓ |
| 0 manglende verdier, 0 dubletter | `tab_renselogg.csv`: manglende_verdier_ut = 0, dubletter_ut = 0 | ✓ |
| 4 042 rader `dd-mm-yyyy` | `tab_renselogg.csv`: datoformat_dd_mm_yyyy = 4042 | ✓ |
| 5 952 rader `mm/dd/yyyy` | `tab_renselogg.csv`: datoformat_mm_dd_yyyy = 5952 | ✓ |
| `Sales` spenn 500–2 500 | `tab_datakvalitet_etter_rens.csv`: min=500, max=2500 | ✓ |
| `Discount` 0,10–0,35 | `tab_datakvalitet_etter_rens.csv`: min=0.1, max=0.35 | ✓ |
| 67 features | `tab_split_oversikt.csv`: antall_features = 67 | ✓ |
| Treningsdata 6 682 rader | `tab_split_oversikt.csv`: train = 6682 | ✓ |
| Testdata 3 312 rader | `tab_split_oversikt.csv`: test = 3312 | ✓ |

**Vurdering:** Fullstendig konsistens mellom rapporten og analyseartefaktene. Ingen faktiske feil.

### 1.2 Tuning-oppsett i kap. 5.1 – presisjon

Kap. 5.1 beskriver tuning slik: «Random Forest ble i tillegg tunet ved å trene på de to første treningsårene og validere på det tredje.»

Beskrivelsen er korrekt i substans (2022–2023 for trening, 2024 som valideringsperiode), men er indirekte — «det tredje» krever at leseren trekker slutningen. Kap. 3.4 (allerede rettet i forrige reviewrunde) presiserer dette eksplisitt med årstall. Kap. 5.1 bør samsvare i konkrethet.

**Vurdering:** Ikke en faktisk feil, men en upresishet. Se V4.

### Gjenstående metodiske observasjoner

Tabell 5.1 har tabelltekst i HTML-format (`<p align="center"><small><i>...</i></small></p>`), noe som er i tråd med CLAUDE.md-malen for figur- og tabellkapsler. Ingen avvik.

---

## Del 2 – Språk, innhold og figurer

### 2.1 Kap. 5.1 – Metode

**Språk:** Klar og akademisk. Tre avsnitt med god progresjon: forskningsdesign → modellstrategi → evaluering. Én grammatikkfeil:

- «gir en naturlig rangering av **variabelenes** prediksjonsverdi» → skal være **variablenes** (genitiv flertall av «variabler», ikke «variabeler»).

**Faglig innhold:** Beskrivelsen av evalueringsopplegget er presis og knytter RMSE til innkjøp/lagerstyring og MAPE til relativ prognose-kommunikasjon. Referansen til kap. 3 mangler — en enkel «som beskrevet i kapittel 3» ved omtale av RMSE og MAPE vil koble metodebeskrivelsen bedre til teoridelen, men er ikke kritisk.

### 2.2 Kap. 5.2 – Data

**Språk:** Ryddig og konsekvent. Variabelomtalen er systematisk og lett å følge.

**Faglig innhold:** Alle nødvendige elementer er på plass. Ett ubehandlet strukturproblem fra forrige review (V2/V4) gjenstår:

- Kap. 4.2, linje 259 inneholder fortsatt: «Den stabile fordelingen mellom periodene er et gunstig trekk ved datasettet, da det indikerer at historiske mønstre trolig er relevante for å predikere 2025.» Dette er en metodebetraktning om train/test-splittens gyldighet — den hører hjemme i kap. 5, ikke i casebeskrivelsen. Ble utsatt til WBS 7.1.4 men er ikke fjernet eller omfordelt.

- Kap. 4.1, linje 244 inneholder fortsatt regionfordeling i prosent (West 32 %, East 28 %, etc.). Disse prosenttallene er datastatistikk som er mer hjemmehørende i kap. 5.2. Det er ingen duplication siden kap. 5.2 ikke gjentar prosenttallene, men den prinsipielle plasseringen er fortsatt feil i tråd med V4 fra forrige review.

### 2.3 Tabell 5.1 – konsistens og lesbarhet

Tabellen er korrekt formatert som Markdown-tabell med fire kolonner og to datarader. Tabellteksten er plassert under tabellen med HTML-kapsling i tråd med CLAUDE.md. Kolonneoverskriftene er tydelige. Tallene stemmer med analyseartefaktene (se Del 1).

### 2.4 Funn fra forrige review (7.1.1–7.1.3) som tilhørte WBS 7.1.4

| # | Funn | Alvorlighetsgrad | Status | Håndtert i 7.1.4? |
|:--|:-----|:-----------------|:-------|:-------------------|
| V2 | Metodebetraktning i kap. 4.2 ikke fjernet | Middels | Åpen | Nei |
| V4 | Regionfordeling i kap. 4.1 ikke adressert | Middels | Åpen | Nei |
| F1 | Flytt datasettdetaljer fra kap. 4.1 til 5.2 | Middels | Åpen | Nei |

---

## Svakheter og forbedringsforslag

### V1. Grammatikkfeil: «variabelenes» i kap. 5.1

**Alvorlighetsgrad:** Lav
**Kategori:** Språk

«gir en naturlig rangering av variabelenes prediksjonsverdi» — genitiv flertall av «variabler» er «variablenes», ikke «variabelenes». Direkte retting.

### V2. Metodebetraktning om stabil fordeling i kap. 4.2 ikke fjernet

**Alvorlighetsgrad:** Middels
**Kategori:** Rapportstruktur

Setningen «Den stabile fordelingen mellom periodene er et gunstig trekk ved datasettet, da det indikerer at historiske mønstre trolig er relevante for å predikere 2025» (kap. 4.2, linje 259) er en metodebegrunnelse for tidsbasert splitt, ikke en historisk faktabeskrivelse. Den hører hjemme i kap. 5 og kan med fordel knyttes til begrunnelsen for tidsmessig splitt i kap. 5.2. Var utsatt fra forrige review til WBS 7.1.4 men er fortsatt ubehandlet.

Anbefalt tiltak: Flytt setningen eller tilsvarende innhold til slutten av det avsnitt i kap. 5.2 som omhandler datasplitt. Formulering kan for eksempel lyde: «Den stabile gjennomsnittlige salgsnivåfordelingen mellom trenings- og testperioden (1 493 vs. 1 503) styrker antakelsen om at historiske mønstre er overførbare til 2025.» Deretter fjernes setningen fra kap. 4.2.

### V3. Regionfordeling i kap. 4.1 hører delvis hjemme i kap. 5.2

**Alvorlighetsgrad:** Middels
**Kategori:** Rapportstruktur

Regionfordelingen i prosent (West 32 %, East 28 %, Central 23 %, South 16 %) og antallet byer (24) er datainformasjon som ble flagget i forrige review (V4/F1) som bedre egnet for kap. 5.2. Kap. 5.2 omtaler `Region` og `City` som kategoriske variabler, men gir ikke de konkrete fordelingstallene. Den prinsipielle avgjørelsen (beholde tallene i kap. 4.1, flytte dem til 5.2, eller ha dem begge steder) bør tas eksplisitt.

### V4. Indirekte beskrivelse av tuning-oppsett i kap. 5.1

**Alvorlighetsgrad:** Lav
**Kategori:** Faglig presisjon

«de to første treningsårene og det tredje» krever at leseren kjenner årstallene. Kap. 3.4 (allerede rettet) bruker eksplisitte årstall. Kap. 5.1 bør samsvare: «ved å trene på 2022–2023 og validere på 2024» er klarere enn «de to første... det tredje».

---

## Forbedringsforslag

### F1. Koble kap. 5.1 til kap. 3 med en kryssreferanse

**Alvorlighetsgrad:** Lav
**Kategori:** Struktur og lesbarhet

5.1 omtaler RMSE og MAPE uten å peke tilbake til kap. 3.3 der disse er forklart matematisk. En enkel parentetisk referanse («(se kap. 3.3)») vil hjelpe leseren navigere fra metodevalg til teorigrunnlaget.

---

## Avhukningsliste – tiltak

| # | Tiltak | Kategori | Status | Kommentar |
|:--|:-------|:---------|:-------|:----------|
| V1 | Rett «variabelenes» → «variablenes» i kap. 5.1 | Språk | [x] | Utført 2026-04-13 |
| V2 | Flytt/erstatt metodebetraktning fra kap. 4.2 til kap. 5.2 | Rapportstruktur | [x] | Utført 2026-04-13: setning fjernet fra kap. 4.2, integert i kap. 5.2 med salgstallene |
| V3 | Ta stilling til plassering av regionfordeling (kap. 4.1 vs. 5.2) | Rapportstruktur | [x] | Utført 2026-04-13: regionfordeling og kategorifordeling flyttet fra kap. 4.1 til kap. 5.2 |
| V4 | Presiser tuning-oppsett i kap. 5.1: «2022–2023 og 2024» | Faglig presisjon | [x] | Utført 2026-04-13 |
| F1 | Legg til kryssreferanse til kap. 3.3 ved omtale av RMSE/MAPE i kap. 5.1 | Struktur | [x] | Utført 2026-04-13 |

---

## Samsvar med prosjektplan og krav

| Sjekkpunkt | Status | Kommentar |
|:---|:---|:---|
| WBS 7.1.4 fullført: metode og data | OK | Fullført 2026-04-13 |
| 5.1 beskriver analyseopplegg og modellstrategi uten WBS-referanser | OK | |
| 5.2 inneholder periode, variabler, datakvalitet og trening/test-oppsett | OK | |
| Tabell 5.1 med splittoversikt | OK | Stemmer med tab_split_oversikt.csv |
| Ingen "Beskriv:"-plassholdere i kap. 5 | OK | |
| KR-005: Datagrunnlag strukturert, kvalitetssikret og dokumentert | OK | |
| KR-006: Metodevalg og forutsetninger dokumentert slik at analysen kan etterprøves | OK | |
| Ubehandlede punkter fra forrige review (V2, V4, F1) | Gjenstår | Var utsatt til WBS 7.1.4 men ikke gjennomført |

---

## Samlet vurdering

### Metodikk

Kap. 5 er faglig korrekt. Alle tall er verifisert mot analyseartefaktene uten avvik. Eksklusjoner er begrunnet, datasplitt er korrekt beskrevet og tuning-oppsettet er substansielt riktig. Eneste metodiske merknad er at tuning-beskrivelsen i 5.1 er noe indirekte og kan presiseres med årstall.

### Språk, innhold og figurer

Teksten er akademisk, klar og fri for WBS-logg-preg. Det er funnet én grammatikkfeil («variabelenes»). Hoveutfordringen er strukturell og ble arvet fra forrige review: metodebetraktningen i kap. 4.2 og regionfordelingen i kap. 4.1 er fortsatt ikke håndtert, og disse grensepunktene mellom case- og datakapitlet bør ryddes opp i senest ved WBS 7.1.7 (ferdigstille innledning og gjennomgå struktur).

### Anbefalt prioritering videre

1. **(Bør)** Fjern metodebetraktning fra kap. 4.2 og integrer i kap. 5.2 (V2)
2. **(Bør)** Ta stilling til regionfordeling i kap. 4.1 — flytt tallene til 5.2 eller behold dem bevisst i begge (V3)
3. **(Kan)** Rett «variabelenes» → «variablenes» i kap. 5.1 (V1)
4. **(Kan)** Presiser tuning-årstall i kap. 5.1 (V4)
5. **(Kan)** Legg til kryssreferanse til kap. 3.3 ved RMSE/MAPE i kap. 5.1 (F1)
