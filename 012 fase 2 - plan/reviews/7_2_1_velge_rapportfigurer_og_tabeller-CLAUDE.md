# Review av aktivitet 7.2.1 – Velge rapportfigurer og tabeller

**Reviewer:** Claude (automatisk review)
**Dato:** 2026-04-19
**Aktivitetsmappe:** `012 fase 2 - plan/rapport_fig_tab_utvalg.md` (leveransen for 7.2.1)
**Planreferanse:** WBS 7.2.1 (planlagt Wed 15.04.26, fullført 2026-04-19, fire dager etter planlagt slutt)

---

## Sammendrag

Leveransen er et 234-linjers utvalgsdokument som låser 12 figurer, 15 innholdstabeller og 7 vedleggsreferanser, med full sporbarhet til analyseaktivitetene. Lærerens 9 formkrav er gjengitt ordrett og oversatt til sju konkrete konsekvenser. Dokumentet har en reell inkonsistens i figurnummereringen i kap. 8 (bryter mot lærerens formkrav 1), og to mindre plasseringsuklarheter. Totalt: 6 styrker, 3 svakheter (1 Middels, 2 Lav), 3 forbedringsforslag (alle Lav).

---

## Styrker

- **S1.** Komplett inventering: Utvalgsdokumentet dekker alle 57 CSV-tabeller og 4 PNG-figurer i [006 analysis/aktiviteter/](../../006%20analysis/aktiviteter/). Ingen artefakt er oversett – hver enkelt er enten valgt inn, valgt bort med begrunnelse, eller plassert som vedleggsreferanse (A1–A7).
- **S2.** Lærerens 9 formkrav er gjengitt ordrett i §2 og oversatt i §2 «Konsekvenser for dette prosjektet» til 7 operative punkter. Særlig eksplisitt er tolkningen «ingen kilde skal oppgis i figur-/tabelltekstene fordi alle er egenproduserte», som forhindrer feilaktig Kaggle-tilskrivning.
- **S3.** Alle foreslåtte figur-/tabelltekster i §5 og §6 er én–to setninger lange, oppgir enhet (kr, prosent) og hovedbudskap, og er dermed selvstendig forståelige i tråd med formkrav 5. Dette gir 7.2.2/7.2.3 entydige bestillinger.
- **S4.** Sporbarhet rapport → analyse → WBS er eksplisitt i §10. Tabellen kobler hvert rapportkapittel til både analyseaktivitet (01–18) og WBS-node (2.x–6.x), slik at sensor kan reprodusere hvilken aktivitet som har produsert hvilket tall.
- **S5.** Nummereringskonvensjonen (a) vs (b) er diskutert eksplisitt i §3, med fem operative regler og valg om å beholde kapittelbundet (b) som arbeidsantagelse. Dette eliminerer tvetydigheten som ellers ville dukket opp i 7.2.4.
- **S6.** Vedleggsliste A1–A7 adresserer formkrav 8 («stort eller detaljert datamateriale skal plasseres i vedlegg»). 3 312-rads detaljfiler og 37-rads tuning-kandidatgrid limes ikke inn; de refereres via relativ sti i repoet, slik at sensor kan åpne full versjon direkte.

---

## Del 1 – Metodikk (beregninger og kode)

WBS 7.2.1 er en beslutnings- og dokumentasjonsaktivitet uten egen kode. Del 1 vurderer faktisk korrekthet i sporbarhet, kildehenvisninger og plan-konsistens.

### 1.1 Kildefiler og aktivitetsmapper

Samtlige kildefiler som utvalgsdokumentet refererer til eksisterer i repoet. Eksplisitt verifisert:

- `tab_relevante_variabler.csv` (12 rader inkl. header) – samsvar med «12 rader» i §7.3.
- `tab_featurevalg.csv` (19 rader inkl. header, dvs. 18 datarader) – benyttes i Tabell 5.3.
- `tab_bias_maaned_modell.csv`, `tab_rmse_mape_maaned.csv`, `tab_rf_tuned_feature_importance.csv`, `tab_variabelgrupper_tuned_top10.csv`, `tab_rmse_mape_oversikt.csv` – alle tilstede som kildefiler for figurene 7.1, 7.2, 8.1, 8.2 og 8.3.
- Skriptene `start_wbs_5_2.py` (aktivitet 13), `start_wbs_5_4.py` (aktivitet 15), `start_wbs_6_1.py` (aktivitet 16) som §7.2 peker på som vertskript for nye plott eksisterer alle.

**Vurdering:** Ingen død lenke eller oppdiktet filsti. Utvalgsdokumentet er forankret i faktiske artefakter.

### 1.2 Konsistens med dagens rapport

Rapportens nåværende Tabeller 8.1–8.4 er sjekket i [005 report/rapport.md](../../005%20report/rapport.md) linje 369–423 og verifisert med kildene:

- Tabell 8.1: tall 580,39 / 589,28 / 578,26 og 44,18 / 44,12 / 43,97 % – stemmer med ambisjonen om å beholde tabellen.
- Tabell 8.2: 11/0/1 og 3/6/3 – stemmer med [tab_modellvinner_telling.csv](../../006%20analysis/aktiviteter/14_sammenligne_modellresultater/tab_modellvinner_telling.csv).
- Tabell 8.3: topp 10 med `Discount`, `dayofmonth`, `weekofyear`, `month`, …, `Region_Central` – stemmer med [tab_rf_tuned_feature_importance.csv](../../006%20analysis/aktiviteter/15_viktige_variabler/tab_rf_tuned_feature_importance.csv).
- Tabell 8.4: 14 segmenter, vinnermodell per segment – stemmer med [tab_segmentvinnere_tolkning.csv](../../006%20analysis/aktiviteter/16_tolke_modellresultater/tab_segmentvinnere_tolkning.csv). (Merk at tabelltittelen her er «14», mens kap. 7 i rapporten bruker «13 av 14 tolkningssegmenter»; dette er to forskjellige tellinger – alle 14 vs. kun de 13 hvor tuned RF vant. Ingen motsetning.)

**Vurdering:** Alle «beholdes»-poster er konsistente med dagens rapport.

### 1.3 Rekkefølge av figurer og tabeller i kap. 8 — V1

Utvalgsdokumentet foreslår i §5.4:

- Figur 8.1 plasseres «etter Tabell 8.3».
- Figur 8.2 plasseres «etter Tabell 8.1».
- Figur 8.3 plasseres «etter Figur 8.1».

Rapportens nåværende tabellrekkefølge i kap. 8 er Tabell 8.1 → 8.2 → 8.3 → 8.4 (verifisert i [rapport.md linje 365–423](../../005%20report/rapport.md)). Med de foreslåtte plasseringene vil leseren møte figurene i rekkefølgen **Figur 8.2 → Figur 8.1 → Figur 8.3**, selv om nummereringen tilsier 8.1 → 8.2 → 8.3. Dette bryter mot lærerens formkrav 1 («nummereres separat og i den rekkefølgen de omtales»), som §3 eksplisitt har tatt inn som regel 1.

**Vurdering:** Reell inkonsistens (V1, Middels). Løsning er å bytte nummer slik at figuren som kommer først i teksten heter 8.1, osv.

### 1.4 Samsvar med KR-006 (dokumentasjon og etterprøvbarhet)

KR-006 krever at «resultater, metodevalg og modellforutsetninger skal dokumenteres slik at analysen kan etterprøves». Utvalgsdokumentet dokumenterer eksplisitt hvilke artefakter som velges inn, hvilke som utelates (§8) og hvorfor, samt sporbarhet til analyseaktivitet. Dette bidrar positivt til KR-006.

**Vurdering:** I samsvar.

### Gjenstående metodiske observasjoner

- §12 flagger plan-glidning, men overlater oppføring i [endringslogg.md](../endringslogg.md) til «når 7.2-blokken faktisk lukkes». Siden omfanget er eksplisitt økt (fra implisitt minimum til 5 nye plott og 10 nye tabeller), er det et argument for å føre opp oppføringen nå, mens begrunnelsen er frisk. Se F2.
- §9 vedleggsliste A4 og A7 referer filer som *også* brukes som kilde til Tabell 8.3 (topp 10 av A4) og Tabell 7.2 (utvalg fra A7). Dette er ikke feil, men bør omtales i 7.2.4 slik at vedleggshenvisningene i kap. 12 gjør det klart at full versjon supplerer det reduserte utdraget i hovedteksten.

---

## Del 2 – Språk, innhold og figurer

### 2.1 Språk og faglig nivå i utvalgsdokumentet

Norsk fagspråk er gjennomgående. Termene er konsistente: «tuned Random Forest», «benchmark lineær», «baseline Random Forest», «egenprodusert», «variabelgruppe», «feature importance». Ingen skrivefeil oppdaget. Setningslengden i §2 (konsekvenser) er variert og instruktiv. `æ/ø/å` er bevart korrekt i hele dokumentet – `file -i` bekrefter UTF-8 uten BOM.

**Vurdering:** Språket holder god standard for styringsdokument.

### 2.2 Figurer – plassering og figurtekst

Ingen figurer produseres i 7.2.1; dokumentet spesifiserer hva 7.2.2/7.2.3 skal produsere. Foreslåtte figurtekster er vurdert her:

| Figur | Foreslått figurtekst | Vurdering |
|:------|:---------------------|:----------|
| 4.1 | «Gjennomsnittlig salg per produktkategori …» | OK – selvstendig forståelig. |
| 4.2 | «Månedlig totalsalg 2022–2025 …» | OK – oppgir periode og hovedbudskap. |
| 4.3 | «Gjennomsnittlig salg per kalendermåned …» | OK. |
| 4.4 | «Fordeling av daglige salgsverdier i trenings- og testperioden …» | Teksten er god, men *plasseringen* i §4.3 Sesongmønster er inkonsistent med innholdet (salgsfordeling handler ikke om sesong). Se V2. |
| 5.1 | «Fordeling av datatyper i rådatasettet …» | OK – knytter figuren til forbehandlingsvalg. |
| 7.1 | «Månedlig bias per modell i 2025 … alle tre modellene underestimerer i august–september.» | Faktapåstanden er kontrollerbar og stemmer overens med analysen i [modelltolkning.md](../../006%20analysis/aktiviteter/16_tolke_modellresultater/modelltolkning.md). OK. |
| 7.2 | «Månedlig RMSE per modell i 2025 …» | OK. |
| 8.1 | «Topp 10 feature importance …» | OK. |
| 8.2 | «Samlet RMSE og MAPE …» | OK. |
| 8.3 | «Samlet feature importance per variabelgruppe …» | OK. |

### 2.3 Tabeller – foreslåtte tabelltitler

Alle 15 tabelltitler er kontrollert. De oppfyller kravet om selvstendig forståelighet (oppgir hva rader og kolonner viser). To små observasjoner:

- Tabell 6.2: «Topp 5 parameterkombinasjoner fra tuning …» – begrepet «topp 5» avhenger av sortering. §6.2 spesifiserer ikke om det er topp 5 på RMSE eller MAPE. 7.2.3 må avklare. Lav-grad forbedring (F3).
- Tabell 7.2: Plasseringen er angitt kun som «7 Analyse» uten «før/etter». Uklart om den kommer før eller etter Figur 7.1, Tabell 7.1, Figur 7.2. Se V3.

### 2.4 Konsistens med status.md

`status.md` linje 74 er oppdatert til `[x] WBS 7.2.1 … fullført 2026-04-19`, med lenke til [rapport_fig_tab_utvalg.md](../rapport_fig_tab_utvalg.md). Datolinjen øverst, aktivitet H-bullet, det løpende rapportskrivingspunktet og prosjektstatus-paragrafen er oppdatert konsistent. `wbs.json`-noden 7.2.1 er satt til `"percent_complete": "100%"` og JSON-filen validerer fortsatt.

**Vurdering:** Planartefaktene er i sync.

### 2.5 Funn fra andre reviewer

Ingen tidligere review av 7.2.1 eksisterer. Funn fra 7.1-reviewene er sjekket og ikke relevante for denne aktiviteten.

---

## Svakheter og forbedringsforslag

### V1. Rekkefølgebrudd i figurnummereringen i kap. 8

**Alvorlighetsgrad:** Middels
**Kategori:** Metodikk

Utvalgsdokumentet plasserer Figur 8.2 etter Tabell 8.1 (dvs. før Figur 8.1), slik at leseren møter figurene i rekkefølgen 8.2 → 8.1 → 8.3. Dette bryter direkte mot lærerens formkrav 1, som §3 eksplisitt har lagt som regel 1. Fikses ved å bytte nummerene slik at rekkefølgen 8.1 → 8.2 → 8.3 matcher tekstrekkefølgen:

- Figur 8.1 → «Samlet RMSE og MAPE» (tidligere 8.2), plasseres etter Tabell 8.1.
- Figur 8.2 → «Topp 10 feature importance» (tidligere 8.1), plasseres etter Tabell 8.3.
- Figur 8.3 → «Variabelgrupper i topp 10» (beholdes), plasseres etter Figur 8.2.

Oppdater §5.4, §7.2, §10 og §11 i utvalgsdokumentet samt skriptoppdragene i §7.2 (skriptene som produserer figurene må navngis riktig i aktivitet 13 og 15).

### V2. Figur 4.4 er plassert i feil underseksjon

**Alvorlighetsgrad:** Lav
**Kategori:** Metodikk / Språk og innhold

`fig_sales_fordeling_train_test.png` viser fordeling av salgsverdier i trening vs. test, ikke sesongmønster. §5.1 plasserer den likevel i «4.3 Sesongmønster i salget (etter Figur 4.3)». Innholdsmessig hører figuren til enten §4.2 Historisk salgsutvikling (som del av beskrivelse av Y-variabelen) eller §5.2 Data (som argument for at trenings- og testperioden har sammenlignbar målvariabel). 

Anbefalt tiltak: Flytt Figur 4.4 til §5.2 Data og omnummerer slik at den blir Figur 5.1 (og dagens Figur 5.1 «Datatype-fordeling» blir Figur 5.2). Dette reduserer antall figurer i kap. 4 fra 4 til 3, og øker antall figurer i kap. 5 fra 1 til 2 – uten å endre totalantallet 10 innholdsfigurer.

### V3. Plassering av Tabell 7.2 er ikke spesifisert

**Alvorlighetsgrad:** Lav
**Kategori:** Metodikk

§6.3 oppgir plassering «7 Analyse» for Tabell 7.2 uten «før/etter»-anker. Det gir 7.2.3 rom for ulike tolkninger av rekkefølgen innen kap. 7. For å sikre at prinsippet «nummereres i rekkefølgen de omtales» holdes konsistent, bør plasseringen spesifiseres konkret (f.eks. «etter Figur 7.2, før oppsummeringsavsnittet»).

### F1. Lenker med mellomrom i filstier

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

Markdown-lenkene bruker stier som `../006 analysis/aktiviteter/…` med bokstavelig mellomrom. Dette rendres i VS Code, men enkelte Markdown-parsere og PDF-eksport kan tolke mellomrommet som linje-slutt og trunkere URL-en. Vurder å URL-kode mellomrommet (`%20`) i lenkene, eller minst sjekke ved første rapporteksport.

### F2. Endringslogg bør oppdateres umiddelbart, ikke utsettes

**Alvorlighetsgrad:** Lav
**Kategori:** Metodikk

§12 flagger plan-glidning (5 nye plott + 10 nye tabeller vs. det Gantt forutsatte da planen ble etablert), men overlater endringsloggen til «når 7.2-blokken faktisk lukkes». Dette er i strid med prosjektets endringskontrollprosess (prosjektstyringsplan §12, steg 1 «Registrering av endringsforslag» = umiddelbart). Begrunnelsen for omfangsøkningen er frisk nå og bør føres inn i [endringslogg.md](../endringslogg.md) samtidig med at 7.2.1 lukkes.

### F3. Sorteringskriterium for «Topp 5» i Tabell 6.2

**Alvorlighetsgrad:** Lav
**Kategori:** Metodikk

Tabelltittelen for 6.2 sier «Topp 5 parameterkombinasjoner fra tuning». Siden [tab_rf_tuning_kandidater.csv](../../006%20analysis/aktiviteter/11_parameterjustering_random_forest/tab_rf_tuning_kandidater.csv) har både RMSE og MAPE, bør det spesifiseres at utvalget sorteres på RMSE (som er hovedmetrikken for tuning ifølge [random_forest_tuning.md](../../006%20analysis/aktiviteter/11_parameterjustering_random_forest/random_forest_tuning.md)). Dette hindrer tvetydighet i 7.2.3.

---

## Avhukningsliste – tiltak

| # | Tiltak | Kategori | Status | Kommentar |
|:--|:-------|:---------|:-------|:----------|
| V1 | Bytt nummer på Figur 8.1 ↔ 8.2 slik at tekstrekkefølgen blir 8.1 → 8.2 → 8.3, og oppdater §5.4, §7.2, §10 og §11 i utvalgsdokumentet | Metodikk | [x] | Gjennomført 2026-04-19. Figur 8.1 = samlet RMSE/MAPE, Figur 8.2 = feature importance topp 10, Figur 8.3 = variabelgrupper. |
| V2 | Flytt Figur 4.4 til §5.2 og renumerere | Metodikk / Språk og innhold | [x] | Gjennomført 2026-04-19. Datatype-fordeling = Figur 5.1, salgsfordeling trening/test = Figur 5.2. Kap. 4 har nå tre figurer. |
| V3 | Spesifiser plassering av Tabell 7.2 («etter Figur 7.2» eller tilsvarende) i §6.3 | Metodikk | [x] | Gjennomført 2026-04-19. Plassering satt til «7 Analyse, etter Figur 7.2». |
| F1 | URL-kod mellomrom i Markdown-lenkene (`../006%20analysis/…`) eller verifiser i PDF-eksport | Språk og innhold | [x] | Gjennomført 2026-04-19. 64 URL-kodede lenker i utvalgsdokumentet og 10 i review-filen. |
| F2 | Før oppføring i [endringslogg.md](../endringslogg.md) for omfangsøkning i 7.2-blokken | Metodikk | [x] | Gjennomført 2026-04-19. Ny oppføring lagt øverst i endringsloggen. |
| F3 | Spesifiser sorteringskriterium i tabelltittelen til Tabell 6.2 (topp 5 på RMSE) | Metodikk | [x] | Gjennomført 2026-04-19. Tittelen presiserer nå «sortert etter RMSE på 2024-valideringen». |

---

## Samsvar med prosjektplan og krav

| Sjekkpunkt | Status | Kommentar |
|:---|:---|:---|
| WBS 7.2.1: «Velge hvilke figurer og tabeller som faktisk skal inn i rapporten» (status.md linje 74) | OK | Lukket i status.md og wbs.json; leveranse foreligger som 234-linjers utvalgsdokument. |
| KR-005 «Datagrunnlaget skal være strukturert, kvalitetssikret og dokumentert» | OK (støttende) | Utvalget kobler tabellene 5.2–5.4 og Figur 5.1 til aktivitetene 01, 02, 04, 05 og 06 som dokumenterer datagrunnlaget. |
| KR-006 «Resultater, metodevalg og modellforutsetninger skal dokumenteres slik at analysen kan etterprøves» | OK (støttende) | §10 Sporbarhet og §8 Bortvalg gir fullstendig etterprøvbarhet for utvalgsprosessen. |
| Lærerens formkrav 1 (nummereres i rekkefølgen de omtales) | OK | V1 rettet 2026-04-19 – figurrekkefølgen i kap. 8 matcher nå nummereringen. |
| Lærerens formkrav 5 (selvstendig forståelige fig./tabelltekster) | OK | Alle foreslåtte tekster er sjekket og oppfyller kravet. |
| Lærerens formkrav 6 (egenprodusert → ingen kilde) | OK | §2 «Konsekvenser» slår dette fast eksplisitt. |
| Lærerens formkrav 8 (stort materiale i vedlegg) | OK | §9 Vedleggsliste A1–A7 dekker dette. |
| CLAUDE.md: norsk, UTF-8 uten BOM, `æ/ø/å` bevart | OK | `file -i` bekrefter UTF-8; ingen tegnfeil funnet. |
| Prosjektstyringsplan §12: Endringsforslag skal registreres | OK | F2 rettet 2026-04-19 – oppføring om omfangsøkning lagt inn i endringsloggen. |

---

## Samlet vurdering

### Metodikk

Utvalgsdokumentet er metodisk grundig og forankret i faktiske artefakter. Hovedsvakheten er at rekkefølgen av figurer i kap. 8 gir motstrid mellom nummer (8.1 → 8.2 → 8.3) og tekstrekkefølge (8.2 → 8.1 → 8.3), noe som bryter direkte mot lærerens formkrav 1. Plasseringen av Figur 4.4 er innholdsmessig skjev. Disse må rettes før 7.2.3 starter; hvis de skjer i 7.2.3 blir det mer omarbeid av skriptnavn og filplassering.

### Språk, innhold og figurer

Språket er presist og konsistent, æ/ø/å er bevart, figur- og tabelltekster er selvstendig forståelige og oppgir enhet og hovedbudskap. To mindre tekstpresiseringer (Tabell 6.2 sortering, Tabell 7.2 plassering) er identifisert som lav-grad forbedringer.

### Anbefalt prioritering videre

Alle seks tiltak gjennomført 2026-04-19 og verifisert mot utvalgsdokumentet, endringsloggen og review-filen. Reviewen er dermed lukket; ingen åpne funn før 7.2.2 starter.

1. ~~**(Må)** Rett V1 – omnummerer figurene i kap. 8 slik at tekstrekkefølgen matcher nummereringen, og oppdater §5.4, §7.2, §10 og §11 i utvalgsdokumentet.~~ Gjennomført.
2. ~~**(Må)** Før opp omfangsøkningen i [endringslogg.md](../endringslogg.md) (F2), siden 7.2.1 flytter planbaseline for 7.2.2–7.2.4.~~ Gjennomført.
3. ~~**(Bør)** Vurder V2 – flytt Figur 4.4 til §5.2 Data, med tilhørende renumerering av Figur 5.x.~~ Gjennomført (datatype først, salgsfordeling etter).
4. ~~**(Bør)** Spesifiser plassering av Tabell 7.2 (V3) og sortering av Tabell 6.2 (F3).~~ Gjennomført.
5. ~~**(Kan)** URL-kod mellomrom i Markdown-lenker (F1) som del av 7.3.1 kvalitetssikring.~~ Gjennomført (både utvalgsdokument og review-fil).
