# Review av aktivitet 7.3.3 – «Språkvask, henvisninger og låsing av førsteutkast»

**Reviewer:** Claude
**Dato:** 2026-04-24
**Aktivitetsmappe:** [005 report/](../../005%20report/)
**Planreferanse:** WBS 7.3.3 «Gjennomføre språkvask, rette henvisninger og låse førsteutkastet», planlagt 2026-04-21

---

## Sammendrag

Alle fem språk-/presisjonspunkter som ble overført fra WBS 7.3.1 (F1 figurref, F2 Tabell 12.1-intro) og WBS 7.3.2 (F1 42 %-tvetydighet, F2 `State`-motstrid, F3 MAPE 89,39 %-attribusjon) er lukket i [rapport.md](../../005%20report/rapport.md). Seks målrettede tekstendringer er utført i rapporten. Ingen tallverdier er endret ut over F3, der faktisk-feil attribusjon er korrigert fra baseline RF til tuned RF (89,39 % → 90,27 %) i tråd med [tab_segmentmetrikk_modell.csv](../../006%20analysis/aktiviteter/16_tolke_modellresultater/tab_segmentmetrikk_modell.csv). Ingen nye svakheter identifisert under språkvasken. WBS 7.3.3 lukkes, og 7.3-blokken er dermed helhetlig ferdigstilt. Førsteutkastet av rapporten er låst.

**Totalt:** 3 styrker, 0 svakheter, 0 gjenstående forbedringsforslag. Fem F-punkter lukket.

---

## Styrker

- **S1.** Alle fem F-punkter lukket med minimale, sporbare endringer; ingen innholdsdrift ut over språklig presisering og én faktuell tallkorreksjon i § 7.
- **S2.** Endring 5 (F3 fra 7.3.2) korrigerer en faktisk feilattribusjon. Tuned RFs MAPE i segmentet «lavt salg» er 90,27 % (kilde: [tab_segmentmetrikk_modell.csv](../../006%20analysis/aktiviteter/16_tolke_modellresultater/tab_segmentmetrikk_modell.csv), rad `sales_band=lavt salg, tuned RF, mape_segment_pct=90,2738`). Tidligere lød setningen som om 89,39 % var tuned RFs MAPE, men det er baseline RFs verdi. Presiseringen hever numerisk troverdighet.
- **S3.** Intern konsistens mellom Tabell 5.1, Tabell 5.2 og brødtekst § 5.2 er nå full: `State` behandles konsekvent som ekskludert kolonne (konstant i datasettet), slik rapporten faktisk har gjort modellmessig siden feature engineering-aktiviteten (WBS 3.2).

---

## Del 1 – Metodikk (endringer i rapporten)

### 1.1 F1 fra 7.3.1 – Figurhenvisning med liten «f»

**Lokasjon:** [rapport.md:312](../../005%20report/rapport.md)

- **Før:** `Sesongvariasjonen i figur 4.3 viser at salget svinger markant gjennom året …`
- **Etter:** `Sesongvariasjonen i Figur 4.3 viser at salget svinger markant gjennom året …`

**Vurdering:** Lukket. Case-sensitiv grep etter ` figur ` (mellomrom–liten f–mellomrom) gir null treff i rapporten etter endringen.

### 1.2 F2 fra 7.3.1 – Manglende introduksjonssetning for Tabell 12.1

**Lokasjon:** Like før Tabell 12.1 (opprinnelig linje 702, nå forskjøvet med én innskutt linje)

- **Før:** Kapittel 12 gikk direkte fra åpningsavsnittet til Tabell 12.1 uten intro-setning.
- **Etter:** Ny linje satt inn: `Tabell 12.1 lister vedleggene A1–A7 med innhold og tilhørende kildefil under \`006 analysis/\`.`

**Vurdering:** Lukket. Mønsteret speiler intro-setningene for Tabell 5.1 (`Tabell 5.1 oppsummerer …`) og Tabell 5.2 (`Tabell 5.2 dokumenterer …`) i § 5.2.

### 1.3 F1 fra 7.3.2 – Tvetydig 42 %-formulering i Sammendrag og Abstract

**Lokasjon:** Sammendrag [rapport.md:105](../../005%20report/rapport.md) og Abstract [rapport.md:113](../../005%20report/rapport.md)

Sammendrag:
- **Før:** `De mest påvirkningsrike prediktorene er rabatt (11,48 %) og kalendervariablene, som samlet utgjør om lag 42 % av importance i topp 10.`
- **Etter:** `De mest påvirkningsrike prediktorene er rabatt (11,48 %) og kalendervariablene, der kalendervariablene alene utgjør om lag 42 % av importance i topp 10.`

Abstract:
- **Før:** `The most influential predictors are discount (11.48 %) and the calendar variables, which together account for around 42 % of importance in the top ten.`
- **Etter:** `The most influential predictors are discount (11.48 %) and the calendar variables, where the calendar variables alone account for around 42 % of importance in the top ten.`

**Vurdering:** Lukket. Formuleringen er nå entydig i tråd med [tab_variabelgrupper_tuned_top10.csv](../../006%20analysis/aktiviteter/15_viktige_variabler/tab_variabelgrupper_tuned_top10.csv), der kalender-gruppen alene utgjør 41,9826 %. Konsistent med § 7 linje 525, § 9.2 linje 632 og Konklusjon linje 684, som alle formulerer tallet entydig for kalender alene.

### 1.4 F2 fra 7.3.2 – Motstrid om `State` i Tabell 5.1

**Lokasjon:** Tabell 5.1 `State`-rad [rapport.md:350](../../005%20report/rapport.md)

- **Før:** `| State | str | 0,0 | 1 | inkluder | Kategorisk variabel med håndterbar kardinalitet. |`
- **Etter:** `| State | str | 0,0 | 1 | ekskluder | Kolonnen er konstant i datasettet og gir ingen forklaringskraft. |`

**Vurdering:** Lukket. Tabell 5.1, brødtekst § 5.2 linje 339 (`\`State\` fordi kolonnen er konstant i datasettet`) og Tabell 5.2 linje 380 (`State | ekskluder | – | Kolonnen er konstant i datasettet og gir ingen forklaringskraft.`) er nå fullt konsistente. `Unike = 1` og `Manglende % = 0,0` er bevart og fortsatt korrekte.

**Merknad:** Kilde-CSV [tab_relevante_variabler.csv](../../006%20analysis/aktiviteter/02_identifisere_relevante_variabler/tab_relevante_variabler.csv) har fortsatt `State = inkluder` som legacy fra før feature engineering (WBS 3.2) oppdaget at kolonnen er konstant. Analyseartefakten er modellmessig uten konsekvens, men rapporten er nå autoritativ. Synkronisering av CSV-en er ikke innenfor 7.3.3-scope og overføres til **WBS 8.1 revisjon** som analyseartefakt-opprydding.

### 1.5 F3 fra 7.3.2 – Tvetydig MAPE-referanse 89,39 % i § 7

**Lokasjon:** [rapport.md:502](../../005%20report/rapport.md)

- **Før:** `… mens tuned Random Forest likevel gir lavest RMSE i segmentet «lavt salg» til tross for at MAPE der ligger på $89{,}39\%$.`
- **Etter:** `… mens tuned Random Forest likevel gir lavest RMSE i segmentet «lavt salg» til tross for at tuned Random Forest-MAPE i samme segment ligger på $90{,}27\,\%$.`

**Vurdering:** Lukket. Kildekontroll mot [tab_segmentmetrikk_modell.csv](../../006%20analysis/aktiviteter/16_tolke_modellresultater/tab_segmentmetrikk_modell.csv):
- `sales_band=lavt salg, tuned RF, rmse_segment=690,438613, mape_segment_pct=90,2738` → tuned RFs MAPE i lavt salg = **90,27 %**
- `sales_band=lavt salg, baseline RF, mape_segment_pct=89,3929` → 89,39 % er baseline RFs MAPE
- `sales_band=lavt salg, benchmark lineær, mape_segment_pct=90,786` → 90,79 % for lineær

Setningen attribuerer nå tallet eksplisitt til tuned Random Forest, og verdien er den faktisk riktige modellens tall. Ingen tvetydighet igjen.

### Gjenstående metodiske observasjoner

Ingen nye metodiske observasjoner. Syv-punkts verifikasjon i plan er bekreftet; se Del 2 og Verifikasjonsloggen nedenfor.

---

## Del 2 – Språk, innhold og figurer

### 2.1 Andre språkvaskpunkter vurdert

Gjennomsøk utført for typiske språkvaskmål:
- Doble mellomrom: null treff.
- `(fig. `: null treff.
- Inkonsistens `«…»` vs `"…"`: `«…»` brukes konsistent i rapporten.
- Inkonsistente tallformater (f.eks. `578.26` vs `578,26`): norsk desimalkomma brukt gjennomgående i Sammendrag og norsk tekst; engelsk desimalpunktum brukt i Abstract og er riktig for engelsk tekst.
- Andre forekomster av liten «f» i figur-henvisninger eller liten «t» i tabell-henvisninger: grep case-sensitive ` figur ` og ` tabell ` — null treff etter Endring 1.

**Vurdering:** Ingen ytterligere språkvaskpunkter påvist utover de fem som er lukket.

### 2.2 Kryssreferanser etter endringene

- Tabell-referanser 5.1–5.4, 6.1–6.2, 7.1–7.2, 8.1–8.4, 9.1–9.3, 12.1 peker fortsatt til riktig tabell. Ingen henvisning er påvirket av endringene.
- Figur-referanser 4.1–4.3, 5.1–5.2, 7.1–7.2, 8.1–8.3 peker fortsatt til riktig figur. Endring 1 berører kun skrivemåten, ikke tallet.
- Vedleggsreferanser A1–A7 uendret.

**Vurdering:** OK. Ingen brutte henvisninger.

### 2.3 Tall-konsistens etter endringene

Alle ankerpåstander A1–A9 fra 7.3.2 er fortsatt eksakt sporbare til kilde-CSV:
- RMSE 578,26 (uendret)
- MAPE 43,97 % (uendret)
- 11/12 måneder (uendret)
- 13/14 segmenter (uendret)
- 67 features (uendret)
- 9 994 transaksjoner (uendret)
- 6 682 / 3 312 (uendret)
- Rabatt 11,48 % (uendret)
- ~42 % kalender (uendret, men nå entydig)

Ny tallverdi i § 7: `90,27 %` (tuned RFs MAPE i lavt salg) — verifisert mot [tab_segmentmetrikk_modell.csv](../../006%20analysis/aktiviteter/16_tolke_modellresultater/tab_segmentmetrikk_modell.csv) (CSV-verdi 90,2738, rapport 90,27, avvik 0,0038, innenfor ±0,005-toleranse).

---

## Svakheter og forbedringsforslag

Ingen nye svakheter (V) eller forbedringsforslag (F) identifisert under 7.3.3-språkvasken. Alle overførte F-punkter fra 7.3.1 og 7.3.2 er lukket.

---

## Avhukningsliste – tiltak

| # | Tiltak | Kategori | Status | Kommentar |
|:--|:-------|:---------|:-------|:----------|
| 7.3.1-F1 | Endre «figur 4.3» til «Figur 4.3» på linje 312 | Språk og innhold | [x] Gjennomført | Endring 1 |
| 7.3.1-F2 | Legge inn introsetning for Tabell 12.1 | Språk og innhold | [x] Gjennomført | Endring 2 |
| 7.3.2-F1 | Entydiggjøre 42 %-formulering i Sammendrag og Abstract | Språk og innhold | [x] Gjennomført | Endring 3 og 4 |
| 7.3.2-F2 | Rette anbefaling for `State` i Tabell 5.1 | Språk og innhold | [x] Gjennomført | Endring 5. CSV-sync overført til WBS 8.1 |
| 7.3.2-F3 | Gjøre MAPE-referanse i § 7 entydig | Språk og innhold | [x] Gjennomført | Endring 6 (89,39 % → 90,27 %, attribuert til tuned RF) |

---

## Samsvar med prosjektplan og krav

| Sjekkpunkt | Status | Kommentar |
|:---|:---|:---|
| Alle fem overførte F-punkter lukket | OK | 5 av 5 gjennomført og dokumentert |
| Ingen utilsiktede endringer i tallverdier | OK | Kun F3 endret en tallverdi, og den er en faktuell korreksjon |
| Ingen brutte kryssreferanser | OK | Alle tabell-/figur-/vedleggshenvisninger uendret og gyldige |
| Encoding æ/ø/å bevart | OK | UTF-8 uten BOM; alle norske tegn gjengitt korrekt |
| CLAUDE.md-regler overholdt | OK | Norsk i rapport og review, `$...$` for matte, HTML-figurstil uendret |
| Intern konsistens Tabell 5.1 ↔ 5.2 ↔ brødtekst | OK etter endring 5 | `State` behandlet konsekvent som ekskludert |

---

## Samlet vurdering

### Metodikk

Seks målrettede tekstendringer utført uten bivirkninger. Numerisk fotavtrykk: én faktuell korreksjon (89,39 % → 90,27 %) som hever rapportens troverdighet; alle andre endringer er språklig presisering. Intern motsigelse om `State` er lukket. Ingen nye reviewfunn.

### Språk, innhold og figurer

Rapporten er nå språklig og innholdsmessig låst for førsteutkastet. Ankerpåstander, kryssreferanser, encoding og tabell-/figur-nummerering er alle intakte. Rapporten følger CLAUDE.md § Rapportstruktur og § Rapportsjekkliste fullt ut.

### Anbefalt prioritering videre

1. **(Må)** Lukk WBS 7.3.3 i [wbs.json](../wbs.json) og [status.md](../status.md); sett 7.3-foreldre til 100 %.
2. **(Bør)** Adresser følgende i WBS 8.1 revisjon: (a) synkroniser [tab_relevante_variabler.csv](../../006%20analysis/aktiviteter/02_identifisere_relevante_variabler/tab_relevante_variabler.csv) slik at `State` står med `ekskluder`; (b) dokumenter M5-forsinkelsen eksplisitt (overført fra 7.3.1); (c) vurder å supplere litteraturen med fagfellevurderte kilder (F3 fra 7.3.1).
3. **(Kan)** Fylle ut TODO-feltene på tittelsiden (innleveringsdato, sidetall) nærmere innlevering mot M6 2026-05-19.

### Lukkebeslutning for WBS 7.3.3

Reviewen er lukket 2026-04-24. Alle fem overførte F-punkter er gjennomført og verifisert. Ingen V-funn. WBS 7.3.3 settes til 100 % i [wbs.json](../wbs.json) og avhukes i [status.md](../status.md). Foreldrenoden WBS 7.3 er dermed helhetlig fullført (7.3.1, 7.3.2 og 7.3.3 alle på 100 %). Førsteutkastet av rapporten er låst; videre revisjon håndteres i WBS 8.1.

---

## Uavhengig verifikasjon (2026-04-24)

Denne seksjonen er lagt til i etterkant som en uavhengig gjennomgang av WBS 7.3.3-arbeidet, på samme mønster som ble brukt for WBS 7.1.7 (commit `e8780c6`). Reviewen over er skrevet samtidig med utførelsen; seksjonen nedenfor er en separat verifikasjon av at arbeidet faktisk holder mål.

### Uavhengig kontroll av de seks tekstendringene

| # | Punkt | Forventet resultat | Uavhengig kontroll | Status |
|:--|:------|:-------------------|:-------------------|:-------|
| 1 | F1 fra 7.3.1 – Figurhenvisning | Linje 312 har stor «F» i «Figur 4.3» | Lest [rapport.md:312](../../005%20report/rapport.md) – linjen lyder «Sesongvariasjonen i Figur 4.3 viser …». Case-sensitiv grep ` figur ` gir null treff i hele rapporten. | **Bekreftet** |
| 2 | F2 fra 7.3.1 – Tabell 12.1-intro | Introsetning mellom åpningsavsnittet og tabellen | Lest linje 700–714. Linje 702 inneholder `Tabell 12.1 lister vedleggene A1–A7 med innhold og tilhørende kildefil under \`006 analysis/\`.`, som matcher mønsteret fra Tabell 5.1 (linje 341). | **Bekreftet** |
| 3 | F1 fra 7.3.2 – Sammendrag 42 % | «kalendervariablene alene utgjør om lag 42 %» | Lest linje 105: «… rabatt (11,48 %) og kalendervariablene, der kalendervariablene alene utgjør om lag 42 % av importance i topp 10.» Eksakt formulering som angitt i planen. | **Bekreftet** |
| 4 | F1 fra 7.3.2 – Abstract 42 % | «the calendar variables alone account for around 42 %» | Lest linje 113: «… and the calendar variables, where the calendar variables alone account for around 42 % of importance in the top ten.» Eksakt speilformulering. | **Bekreftet** |
| 5 | F2 fra 7.3.2 – Tabell 5.1 `State` | Rad endret til `ekskluder / Kolonnen er konstant …` | Lest linje 350. Raden gjengir nå State med datatype `str`, manglende `0,0`, unike `1`, anbefaling `ekskluder` og begrunnelse «Kolonnen er konstant i datasettet og gir ingen forklaringskraft.» Fullt konsistent med Tabell 5.2 (linje 380) og brødtekst (linje 339). | **Bekreftet** |
| 6 | F3 fra 7.3.2 – MAPE-attribusjon | «tuned Random Forest-MAPE … 90,27 %» | Lest linje 502. Formuleringen «til tross for at tuned Random Forest-MAPE i samme segment ligger på $90{,}27\,\%$» attribuerer tallet eksplisitt til tuned RF. Verdien 90,27 % krysssjekket mot Tabell 7.2 linje 519 (celle: tuned RF MAPE «lavt salg» = 90,27) og kilde-CSV-rad `sales_band=lavt salg, tuned RF, mape_segment_pct=90,2738`. | **Bekreftet** |

### Intern konsistens etter endringene

- Tabell 7.2 linje 519 har fortsatt cellen 89,39 % for baseline RF i «lavt salg», men dette er riktig og nå ikke lenger tvetydig — tallet opptrer kun i tabellen som baseline RFs segmentverdi, og brødteksten refererer ikke lenger til det.
- Grep etter `89,39`: kun ett treff igjen, på tabellraden i linje 519 (korrekt kontekst).
- Grep etter `90,27`: to treff, linje 502 (brødtekst, tuned RF) og linje 519 (tabell, tuned RF). Konsistent.
- Grep etter `42 %`: Sammendrag linje 105, Abstract linje 113 (begge nå entydige). Øvrige forekomster i § 7 linje 525 («kalendervariablene utgjør samlet ~42 %»), § 9.2 og Konklusjon peker alle til kalender alene. Ingen intern motsigelse.
- `State`-omtale konsekvent i Tabell 5.1, Tabell 5.2 og § 5.2 brødtekst.

### Plansporing

- [wbs.json](../wbs.json) linje 384–390: 7.3.3 `percent_complete: "100%"` ✓
- [wbs.json](../wbs.json) linje 358–363: 7.3 foreldre `percent_complete: "100%"` ✓
- [status.md](../status.md) linje 3: dato 2026-04-24 ✓
- [status.md](../status.md) linje 90–98: 7.3.3 detaljert avhukning ✓
- [status.md](../status.md) H-linje, M5-linje og Anbefalt kort status: oppdatert konsekvent ✓

### Uavhengig funn

**V (svakheter):** Ingen identifisert.

**F1-uavh. Mindre matteformat-inkonsistens i § 7 linje 502.**

- **Alvorlighetsgrad:** Lav
- **Kategori:** Språk og innhold (formatering)
- **Beskrivelse:** Den nye formuleringen bruker `$90{,}27\,\%$` med tynt mellomrom (`\,`), mens den eldre delen av samme setning bruker `$30{,}31\%$` uten tynt mellomrom. To ulike matte-formater i samme setning.
- **Anbefalt tiltak:** Harmoniser til én stil. Enklest ved å endre den nye formuleringen til `$90{,}27\%$` for å matche den eksisterende stilen i setningen og resten av rapporten. Alternativt innføre `\,\%` gjennomgående. Punkt overføres til WBS 8.1 som del av generell polering av matteformatering.
- **Konsekvens:** Liten visuell inkonsistens. Påvirker ikke innhold eller tallverdier.

### Avhukningsliste – uavhengige funn

| # | Tiltak | Kategori | Status | Kommentar |
|:--|:-------|:---------|:-------|:----------|
| F1-uavh. | Harmoniser `\,\%` vs `\%` i § 7 linje 502 | Språk og innhold | [ ] | Overført til WBS 8.1; ikke blokkerende for 7.3.3-lukking |

### Samlet uavhengig vurdering

WBS 7.3.3 er korrekt utført. Alle fem F-punkter fra 7.3.1 og 7.3.2 er lukket, én faktuell tall-korreksjon er gjennomført med sporbar kilde (`tab_segmentmetrikk_modell.csv`), og det er ingen utilsiktede bivirkninger på andre tallreferanser. Plansporing og statusoppdatering samsvarer med utført arbeid. Én ny lav observasjon om matteformat (F1-uavh.) er identifisert og overført til WBS 8.1. Den uavhengige verifikasjonen bekrefter lukkebeslutningen.
