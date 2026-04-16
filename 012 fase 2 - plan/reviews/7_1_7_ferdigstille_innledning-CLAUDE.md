# Review av aktivitet 7.1.7 – Ferdigstille innledning

**Reviewer:** Claude (automatisk review)
**Dato:** 2026-04-16
**Aktivitetsmappe:** `005 report/rapport.md` (kapittel 1)
**Planreferanse:** WBS 7.1.7 (planlagt Tue 14.04.26, fullført 2026-04-16, to dager etter planlagt slutt)

---

## Sammendrag

Innledningen er kalibrert mot ferdigskrevet rapport: F3 fra tidligere 7.1.1-review er lukket ved at detaljen «9 994 daglige salgsrader» er fjernet fra §1, avsnitt 2 er strammet til en ren metodemotivasjon, og avsnitt 3 (leserguide) er erstattet av en kort bro-setning inn mot §1.1. Strukturgapet 1.1 → 1.3 er lukket med ny §1.2 Delproblemer som eksplisitt gjør de to delspørsmålene i §1.1 synlige og peker framover mot kap. 9.1/9.2 og kap. 10. §1.3 Avgrensinger og §1.4 Antagelser er urørt — begge er allerede reviewgodkjente.

**Totalt:** 5 styrker, 1 svakhet (Lav), 1 forbedringsforslag (Lav).

---

## Styrker

- **S1.** F3-tiltaket fra 7.1.1-review er gjennomført: «9 994 daglige salgsrader over perioden 2022–2025» er fjernet fra §1 og erstattet med «et simulert dagligvarecase for perioden 2022–2025». Grep i rapport.md bekrefter at `9 994` fortsatt finnes i Sammendrag (linje 101) og kap. 5.2 (linje 324), men ikke lenger i §1.
- **S2.** Strukturgap 1.1 → 1.3 er lukket med ny §1.2 Delproblemer. Begge delproblemene speiler kap. 9.1 (modellvalg og prognoseytelse) og kap. 9.2 (variabelanalyse), og formuleringen bruker ikke tall eller vinnermodell — spoilerfritt.
- **S3.** Bro-setningen «Med dette som utgangspunkt formuleres problemstillingen som styrer metodevalg, analyse og tolkning videre i rapporten.» gir naturlig overgang fra motivasjon til §1.1, noe som tidligere manglet.
- **S4.** Avsnitt 2 er strammet ved å erstatte «komplekse mønstre» med «ikke-lineære mønstre», som er mer presist og kobler direkte til argumentet for RF i kap. 9.2. I tillegg er innledningen utvidet med «samtidig identifisere hvilke forklaringsvariabler som bærer mest prediksjonsverdi», slik at begge delspørsmålene i §1.1 er forvarslet i motivasjonen.
- **S5.** Grep bekrefter at §1 (linje 146–184) ikke inneholder WBS-numre, resultattallene `578,26`, `43,97`, formuleringer som «11 av 12», «13 av 14», eller «tuned Random Forest» som vinnermodell. Innledningen er derfor renskåret fra resultatspoiling.

---

## Del 1 – Metodikk (beregninger og kode)

WBS 7.1.7 er en ren rapportskriveaktivitet. Del 1 vurderer faktisk korrekthet i tallmateriale og konsistens mellom rapport og analyseartefakter.

### 1.1 Konsistens rapport ↔ analyseartefakter

Innledningen refererer ingen konkrete tall fra datasettet eller modellresultatene, bortsett fra perioden «2022–2025». Denne perioden er verifisert konsistent mot kap. 4.2 (linje 280), kap. 5.2 (linje 324) og Sammendrag (linje 101).

**Vurdering:** Ingen tallfestede påstander å kryssjekke. Konsistens er automatisk.

### 1.2 §1.2 Delproblemer ↔ kap. 9 og 10

Delproblem 1 i §1.2 refererer til sammenligning med RMSE/MAPE «samlet, månedlig og på tvers av segmenter som kvartal, rabattband, region og salgsnivå». Dette samsvarer med strukturen i kap. 8 (Tabell 8.1–8.4) og diskusjonen i kap. 9.1.

Delproblem 2 i §1.2 refererer til «rangeringen fra Random Forest» og «koeffisientene i den lineære benchmarken». Dette samsvarer med kap. 9.2 som bruker `tab_rf_tuned_feature_importance.csv` og `tab_lr_koeffisienter.csv`.

**Vurdering:** Delproblemene er i samsvar med det kap. 8–10 faktisk leverer.

---

## Del 2 – Språk, innhold og figurer

### 2.1 §1 Innledning – motivasjonsavsnittene

**Språk:** Begge avsnittene er i klar og presis akademisk prosa. Setningslengden er variert, og faguttrykk brukes riktig. Setningen «Behovet for mer presise etterspørselsprognoser er derfor sentralt når virksomheter skal fatte beslutninger om innkjøp, lager, kampanjer og ressursplanlegging.» er strammet fra tidligere «som ønsker å ta bedre beslutninger knyttet til».

**Faglig innhold:** Første avsnitt aktualiserer temaet med fokus på konsekvenser av dårlige prognoser i dagligvarehandel, i tråd med CLAUDE.md-kravet om at innledningen «skal aktualisere temaet og forklare hvorfor oppgaven er relevant». Andre avsnitt motiverer metodevalget (Random Forest som komplement til lineær regresjon) uten å røpe resultat, og forvarsler begge delspørsmålene i §1.1.

### 2.2 §1.1 Problemstilling – uendret

Beholdt uendret fra 7.1.1-reviewens S1. «Hvordan»-spørsmål med to klare delspørsmål.

### 2.3 §1.2 Delproblemer – ny

**Språk:** To nummererte punkter med fet ledetekst, samme stil som §1.4 Antagelser. Hvert punkt er én setning med klart spørsmål.

**Faglig innhold:** Delproblemene er avledet direkte fra §1.1 og peker framover mot kap. 9.1, 9.2, 10. Valget om å innføre §1.2 Delproblemer (framfor å renumere eller beholde gap) er gjort etter avklaring med bruker. CLAUDE.md sier §1.2 «brukes bare hvis hovedproblemstillingen trenger en tydelig oppdeling» — her gir det klar nytte siden kap. 9 og 10 eksplisitt er strukturert etter de samme to delspørsmålene.

### 2.4 §1.3 Avgrensinger og §1.4 Antagelser – urørt

Begge seksjoner er beholdt ord for ord fra 7.1.1-reviewen, hvor de fikk S2 og S3. Ingen endringer gjort.

### 2.5 Innholdsfortegnelsen

TOC (linje 117–121) oppdatert med ny lenke `[1.2 Delproblemer](#12-delproblemer)`. Anker-slug følger samme konvensjon som øvrige §1-lenker.

### 2.6 Avvik fra plan – leserguide på bunn av §1

Planen foreslo å flytte leserguide-avsnittet (dagens linje 152 før endring) til bunnen av §1 etter §1.4. Etter redigering ble dette avsnittet i stedet erstattet av en kort bro-setning inn mot §1.1, og leserguiden ikke reintrodusert. Begrunnelse: Innholdsfortegnelsen på linje 117–143 gir allerede full navigasjon, og en selvstendig leserguide-blokk mellom §1.4 Antagelser og `---` ville henge strukturelt løst etter antagelsene. Avviket strammer §1 uten informasjonstap.

### 2.7 Ordtelling §1

Hele §1 (linje 147–184) teller 516 ord (`sed -n '147,184p' rapport.md | wc -w`). Planen angav mål 350–450 ord. Avviket kommer av at §1.3 Avgrensinger (~190 ord) og §1.4 Antagelser (~220 ord) er bevart ordrett fra reviewgodkjent 7.1.1-tekst; strammingen ble derfor konsentrert til motivasjonsavsnittene og overgangen. 516 ord ≈ 1,5 side, fullt innenfor CLAUDE.md-regelen «normalt rundt 1–2 sider».

---

## Svakheter og forbedringsforslag

### V1. Ordtelling over opprinnelig planmål

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

§1 teller 516 ord mot planmålet 350–450. CLAUDE.md tillater 1–2 sider (ingen ordgrense), så dette bryter ingen prosjektregel, men er et dokumentert avvik fra detaljplanen. Videre stramming er mulig i 7.3.3 språkvask ved å kutte i §1.3/§1.4, men ingen konkrete svakheter i de to seksjonene er identifisert — så stramming ville gått på bekostning av presisjon.

### F1. Vurder eksplisitt referanse til delproblemene i kap. 9.1/9.2

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

§1.2 Delproblemer peker framover mot kap. 9, men kap. 9.1/9.2 refererer ikke tilbake til §1.2 med formulering som «det første delproblemet» / «det andre delproblemet». Kap. 9.1 bruker i dag «det første delspørsmålet i problemstillingen» (linje 425) og kap. 9.2 «det andre delspørsmålet» (linje 429). Harmonisering av terminologien til «delproblem» i kap. 9 kan vurderes i 7.3.3, men er ikke blokkerende.

---

## Avhukningsliste – tiltak

| # | Tiltak | Kategori | Status | Kommentar |
|:--|:-------|:---------|:-------|:----------|
| V1 | Vurdere ytterligere stramming av §1.3/§1.4 for å treffe 350–450 ord | Språk og innhold | [ ] | Kan håndteres i 7.3.3 hvis ønskelig; ikke blokkerende |
| F1 | Harmonisere «delspørsmål» i kap. 9.1/9.2 til «delproblem» for terminologisk samsvar med §1.2 | Språk og innhold | [ ] | Kan håndteres i 7.3.3 |
| F3 fra 7.1.1-review | Fjerne «9 994 daglige salgsrader» fra innledningen | Rapportstruktur | [x] | Utført i denne aktiviteten |

---

## Samsvar med prosjektplan og krav

| Sjekkpunkt | Status | Kommentar |
|:---|:---|:---|
| WBS 7.1.7 fullført: innledning ferdigstilt i lys av øvrig rapport | OK | Fullført 2026-04-16 |
| F3 fra 7.1.1-review lukket (datasett-detalj fjernet fra §1) | OK | Verifisert via grep |
| Ingen WBS-numre i §1 brødtekst | OK | Grep gir 0 treff |
| Ingen resultatspoiling i §1 | OK | Grep mot 578,26 / 43,97 / 11 av 12 / 13 av 14 / tuned Random Forest gir 0 treff i §1 |
| §1-struktur uten nummergap (1, 1.1, 1.2, 1.3, 1.4) | OK | Ny §1.2 Delproblemer innført |
| Innholdsfortegnelsen oppdatert med §1.2 | OK | Linje 119 |
| Problemstilling formulert som «hvordan»-spørsmål | OK | Uendret |
| Avgrensinger faglig begrunnet | OK | Uendret |
| Antagelser med eksplisitt konsekvens | OK | Uendret |
| Innledning kort og presis (1–2 sider) | OK | 516 ord ≈ 1,5 side |
| Status.md og wbs.json oppdatert | OK | Oppdatert i samme sesjon |
| KR-001 til KR-006 reflektert i innledning og delproblemer | OK | Delproblem 1 dekker KR-001/002/003, delproblem 2 dekker KR-004 |

---

## Samlet vurdering

### Metodikk

Ingen tallfestede påstander i §1, og delproblemene i §1.2 samsvarer med strukturen i kap. 8–10 og de aktuelle analyseartefaktene. F3 fra 7.1.1-review er verifisert lukket. Ingen metodiske avvik.

### Språk, innhold og figurer

Innledningen er kalibrert mot ferdig rapport uten å spoile resultater, strukturgapet 1.1 → 1.3 er lukket, og motivasjonsavsnittene er strammet ned til ren aktualisering og metodemotivasjon. Leserguide-flyttingen fra plan er erstattet av en kort bro-setning med dokumentert begrunnelse. Ordtellingen (516) ligger over detaljplanens 350–450, men innenfor CLAUDE.md-regelen 1–2 sider.

### Anbefalt prioritering videre

1. **(Kan)** Harmonisere terminologien «delspørsmål» → «delproblem» i kap. 9.1/9.2 (F1) — håndteres i 7.3.3.
2. **(Kan)** Vurdere ytterligere stramming av §1.3/§1.4 dersom ordtellingen skal mot 450 (V1) — håndteres i 7.3.3.

Hele 7.1-blokken (rapportkapitler) er dermed lukket. Neste steg er 7.2.1 (velge rapportfigurer og tabeller).

---

## Uavhengig verifisering 2026-04-16 (andre pass)

Dette avsnittet dokumenterer en andre, uavhengig gjennomgang av 7.1.7 utført etter at arbeidet var committet (`98bf9ee feat: Complete introduction section and update status for WBS 7.1.7`). Verifiseringen kontrollerer strukturelle og terminologiske forhold som ikke ble vurdert i første pass.

### Verifisering av tiltak fra første pass

| # | Kontrollpunkt | Kilde | Status |
|:--|:---|:---|:---|
| 1 | F3 fra 7.1.1 er lukket i rapport.md | Grep `9 994` gir treff kun på linje 101 (Sammendrag), 269 (kap. 4.1) og 324 (kap. 5.2) – ingen i §1 | OK |
| 2 | §1-struktur 1, 1.1, 1.2, 1.3, 1.4 sammenhengende | Grep `^## 1` i rapport.md | OK |
| 3 | Ingen WBS-referanser i §1 | Grep `WBS` i rapport.md: 0 treff i hele filen | OK |
| 4 | Ingen resultatspoiling i §1 | Grep `578,26` / `43,97` / `11 av 12` / `13 av 14` / `Tuned Random Forest` i linje 146–184: 0 treff | OK |
| 5 | TOC oppdatert med §1.2 Delproblemer | Linje 119 i rapport.md viser `[1.2 Delproblemer](#12-delproblemer)` | OK |
| 6 | status.md viser 7.1.7 fullført | Linje 3 og 73 i status.md | OK |
| 7 | wbs.json: 7.1.7 og 7.1 på 100 % | Linje 244 og 307 i wbs.json | OK |
| 8 | F3 merket utført i 7.1.1-reviewfilen | Linje 196 i `7_1_innledning_litteratur_casebeskrivelse-CLAUDE.md` | OK |
| 9 | Arbeidet er committet og git-tre er rent | `git status` gir «nothing to commit, working tree clean» | OK |

### Ordtellinger fra andre pass (presis)

Førstepass-anslagene for §1.3 Avgrensinger (~190 ord) og §1.4 Antagelser (~220 ord) var for høye. Reell telling:

| Seksjon | Linjer | Ord |
|:---|:---|:---|
| §1 Innledning (motivasjon + bro) | 147–153 | ~150 |
| §1.1 Problemstilling | 155–157 | ~33 |
| §1.2 Delproblemer | 159–164 | ~70 |
| §1.3 Avgrensinger | 170–174 | 122 |
| §1.4 Antagelser | 180–183 | 142 |
| **Totalt §1** | 147–184 | **516** |

Konsekvens: V1 fra første pass (om at §1.3/§1.4 er «lange» og bærer ordtellingen over 450) er delvis feilformulert. §1.3 og §1.4 er i realiteten begge konsise. Den totale ordtellingen 516 er ikke drevet av unødig lange avgrensninger eller antagelser, men av at dokumentet i sin helhet presenterer problemstilling, delproblemer, avgrensninger og antagelser på et tilstrekkelig detaljnivå. 7.3.3 bør ikke «stramme §1.3/§1.4» — de er allerede stramme.

**Oppdatering av V1:** V1 nedgraderes fra «stramming av §1.3/§1.4» til en ren konstatering om at 516 ord ≈ 1,5 side, innenfor CLAUDE.md-regelen 1–2 sider. Ingen tiltak anbefalt.

### Nye funn fra andre pass

**F2 (Lav) — Stilistisk: «og samtidig» i motivasjonsavsnittet.**
Linje 151 avslutter: «… med mål om å utvikle og evaluere prognosemodeller for salg i 2025, og samtidig identifisere hvilke forklaringsvariabler som bærer mest prediksjonsverdi.» Uttrykket «og samtidig» er akseptabelt, men kan strammes til «og identifisere» for kortere og mer direkte prosa. Håndteres i 7.3.3.

**F3 (Lav) — Terminologisk presisjon i delproblem 2.**
§1.2 punkt 2 bruker «Random Forest» (generisk), mens §1.1 bruker «Random Forest Regressor» (presis). Konsistent terminologi ville være «Random Forest Regressor» eller bruk av kortformen «Random Forest» etter at fullformen er introdusert i §1.1. Begge er akseptable etter introduksjon; ingen faktisk feil. Håndteres i 7.3.3 hvis konsekvens prioriteres.

**F4 (Lav) — Tidlig metodeprioritering i §1.2.**
Delproblem 1 forankrer «RMSE som primær og MAPE som sekundær metrikk». Denne prioriteringen motiveres først i kap. 3.3 og 5.1. Plasseringen i §1.2 er ikke feil – den gir leseren tidlig orientering og speiler at valget er baseline for hele analysen. Alternativt kunne §1.2 punkt 1 vært mer nøytralt formulert («målt med RMSE og MAPE») og prioriteringen introduseres først i kap. 5.1. Beholdes som valgfri 7.3.3-vurdering.

**F5 (Lav) — Terminologi på tvers av §1.1, §1.2 og §9.**
§1.1 bruker «faktorer», §1.2 «forklaringsvariabler», motivasjonen «forklaringsvariabler», kap. 9.2 veksler mellom «variabler», «prediktorer» og «signaler». Alle er akseptable synonymer i denne konteksten, men en bevisst felles ordliste (f.eks. «forklaringsvariabler» som hovedbegrep, med «prediktor»/«signal» som kontekstuelle varianter) kunne styrke lesbarheten. Dette er en gjennomgående stilvurdering som hører i 7.3.3 språkvask.

**F6 (Lav) — Harmonisering av delproblemer med §1.4 antagelse 4.**
§1.4 antagelse 4 knytter seg til at 2025 er holdt utenfor trening. Delproblem 1 refererer til «2025-data» uten å nevne at dette er ubrukt test. Sammenhengen er intuitiv for den som leser §1 sekvensielt, men en eksplisitt kobling i §1.2 punkt 1 ville være overarbeid – F6 er en observasjon, ikke et tiltak.

### Samsvar med krav (krav-matrise)

Ny kobling mellom §1-innhold og KR-001 til KR-007:

| Krav | Beskrivelse | §1-dekning | Status |
|:---|:---|:---|:---|
| KR-001 | Salgsprognoser for 2025 fra 2022–2024 | §1.1 + §1.2 punkt 1 | OK |
| KR-002 | Minst to modeller (LR + RF) | §1.1 + §1.2 punkt 1 + §1.3 punkt 5 | OK |
| KR-003 | MAPE og RMSE for ytelse | §1.2 punkt 1 | OK |
| KR-004 | Identifisere og rangere viktige variabler | §1.1 + §1.2 punkt 2 + motivasjon | OK |
| KR-005 | Strukturert, kvalitetssikret, dokumentert datagrunnlag | Ikke direkte i §1 (hører i kap. 5.2) | N/A for §1 |
| KR-006 | Dokumentasjon av resultater og metodevalg | Ikke direkte i §1 (hører i kap. 5.1/6/8) | N/A for §1 |
| KR-007 | Tids- og ressursrammer | Ikke relevant for §1 | N/A for §1 |

Alle forskningskrav (KR-001–KR-004) er reflektert i §1.

### Andre pass-sjekk av TOC-anker

IDE-diagnostikken viste tidligere en `MD051/link-fragments` warning for `#12-delproblemer` før §1.2-overskriften ble lagt til. Etter endringen peker lenken mot en eksisterende overskrift, og warningen skal være løst. En manuell sjekk i VS Code Markdown-preview er anbefalt som sluttverifisering.

### Samlet vurdering etter andre pass

Aktiviteten WBS 7.1.7 anses som metodisk og innholdsmessig **godkjent**. De gjenværende tiltakene (V1 nedgradert, F1 fra første pass, F2–F5 fra andre pass) er alle kategorisert som Lav alvorlighetsgrad og som 7.3-arbeid (språkvask og konsistenssjekk). Ingen tiltak blokkerer lukking av 7.1.7.

**Oppsummert lav-liste for 7.3.3 språkvask:**

1. ~~F1: Harmonisere «delspørsmål» → «delproblem» i kap. 9.1/9.2.~~ **Utført 2026-04-16** i kap. 9.1 og 9.2.
2. ~~F2: Stramme «og samtidig» → «og» i motivasjonsavsnittet.~~ **Utført 2026-04-16** i §1 avsnitt 2.
3. ~~F3: Vurdere «Random Forest Regressor» vs. «Random Forest» i delproblem 2.~~ **Utført 2026-04-16**: §1.2 punkt 2 bruker nå «Random Forest Regressor», konsistent med §1.1.
4. ~~F5: Etablere felles ordliste for forklaringsvariabler/prediktorer/signaler.~~ **Utført 2026-04-16**: kap. 3 (linje 195) utvidet med samlebegrepet «forklaringsvariabel» og kontekstuelle synonymer prediktor/signal/feature.
5. F4 (valgfri): Flytte RMSE-primær/MAPE-sekundær-betegnelsen fra §1.2 til kap. 5.1.

**Gjenstående tiltak etter 2026-04-16:** Kun F4 (valgfri) står åpent. Alle andre lav-funn fra første og andre pass er lukket.
