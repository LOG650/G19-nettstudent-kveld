# Verifikasjonsreview av WBS 7.2 – Kontroll etter V1–V4 og F1–F4-rettelser

**Reviewer:** Claude (automatisk verifikasjonsreview)
**Dato:** 2026-04-19
**Omfang:** Bekrefte at tiltakene V1–V4 og F1–F4 fra [7_2_full_helhetsreview-CLAUDE.md](7_2_full_helhetsreview-CLAUDE.md) er gjennomført korrekt og konsistent i rapport, utvalgsdokument, leveransefiler og statusartefakter.
**Kontrollerte filer:** [rapport.md](../../005%20report/rapport.md), [rapport_fig_tab_utvalg.md](../rapport_fig_tab_utvalg.md), [rapport_7_2_2_artefakter.md](../rapport_7_2_2_artefakter.md), [rapport_7_2_3_artefakter.md](../rapport_7_2_3_artefakter.md), [status.md](../status.md)

---

## Sammendrag

Alle åtte tiltak (V1–V4 og F1–F4) er verifisert gjennomført i kjernefilen [rapport.md](../../005%20report/rapport.md). Tabellrekkefølgen er nå 5.2 → 5.3 → 5.4 → 5.5 → 6.1 → 6.2 → 7.1 → 7.2 → 8.1 → 8.2 → 8.3 → 8.4 → 9.1 → 9.2 → 9.3 (stigende per kapittel), Tabell 9.2 er beslutningsmatrisen og Tabell 9.3 er metodebegrensninger (ID-kolonne fjernet). Tabell 7.2 bruker norske segmentkoder med `ø`. Utvalgsdokumentet og leveransefilen for 7.2.3 er konsistent oppdatert.

Verifikasjonen avdekket tre mindre restfeil der oppdaterte tabellnumre ikke er trukket gjennom i eldre dokumentasjonstekst. Alle er lav alvorlighet og kosmetiske; de påvirker ikke rapporten i seg selv, men gir inkonsistens mellom dokumentasjonsartefaktene.

**Totalt:** 8 bekreftede tiltak, 3 nye lave funn (R1–R3), 0 blokkerende feil.

---

## Del 1 – Bekreftelse av V1–V4 og F1–F4

### V1 – Rekkefølgebrudd Tabell 5.1/5.5 og Tabell 9.2/9.3

**Status:** ✓ Bekreftet gjennomført.

Verifisert via `grep "Tabell [0-9]+\.[0-9]+ "` på [rapport.md](../../005%20report/rapport.md):

- Ingen forekomster av «Tabell 5.1» – Tabell 5.5 erstatter og ligger på linje 412 og 419 (sist i § 5.2).
- Tabell 9.2 ligger nå på linje 634 og 643 med tittel «Beslutningsmatrise og bruksregler».
- Tabell 9.3 ligger på linje 651 og 662 med tittel «Metodiske begrensninger».

Rekkefølgen 5.2 → 5.3 → 5.4 → 5.5 og 9.1 → 9.2 → 9.3 er stigende. Formkrav 1 er oppfylt.

### V2 – Generell regel i utvalgsdokumentet § 3

**Status:** ✓ Bekreftet gjennomført.

Utvalgsdokumentet § 3 har nå seks regler (regel 6 lagt til):

> «Når en seksjon får flere tabeller eller figurer fordelt over underseksjoner i ulike kapittelnumre, må tabell- og figurnummer settes i samme rekkefølge som underseksjonene – ikke etter underseksjonens interne navn. Rekkefølgen i teksten skal styre nummereringen.»

### V3 – Redundant «fordelingen»-formulering

**Status:** ✓ Bekreftet gjennomført.

Rapport.md linje 412: «Tabell 5.5 oppsummerer antallsfordelingen mellom trenings- og testperioden.» Tidligere formulering «den samlede fordelingen» er borte.

### V4 – «11 unike råvariablene»

**Status:** ✓ Bekreftet gjennomført.

Rapport.md linje 335: «Tabell 5.2 oppsummerer de 11 kolonnene i rådatasettet …» Tidligere «11 unike råvariablene» er borte.

### F1 – 7.3.1-subnote i status.md

**Status:** ✓ Bekreftet gjennomført.

[status.md](../status.md) linje 79–80 har ny sub-bullet under WBS 7.3.1-punktet:

> «Merk fra helhetsreview av 7.2 (F1): sjekk henvisninger «(jf. Tabell 8.2/8.3/8.4)» i kap. 7 – vurder å oppdatere til lokale Tabell 7.1/7.2 der det gir bedre lesbarhet.»

### F2 – Tabell 12.1 og 16 innholdstabeller

**Status:** ✓ Bekreftet gjennomført.

Utvalgsdokumentet § 9 nevner nå eksplisitt at vedleggslisten presenteres som Tabell 12.1. § 10 Sporbarhet og § 11 Sammendrag er oppdatert til 16 innholdstabeller.

### F3 – Norske segmentkoder i Tabell 7.2

**Status:** ✓ Bekreftet gjennomført.

Rapport.md Tabell 7.2 (linje 500–516) bruker nå `Kvartal`, `Rabattbånd`, `Region`, `Salgsbånd` og `høy`/`høyt salg` med norsk `ø`. Ingen gjenstående `quarter`, `discount_band`, `sales_band`, `hoy` eller `hoyt` i Tabell 7.2. Samme oppdatering er gjort i [rapport_7_2_3_artefakter.md](../rapport_7_2_3_artefakter.md) § 2.4. Kilde-CSV er uendret.

### F4 – ID-kolonnen MB-6.2-XX fjernet fra Tabell 9.3

**Status:** ✓ Bekreftet gjennomført.

Ingen forekomster av `MB-6.2-` i rapport.md. Tabell 9.3 har nå 4 kolonner (Tema, Beskrivelse, Konsekvens for pålitelighet, Konsekvens for generaliserbarhet). Leveransefilen [rapport_7_2_3_artefakter.md](../rapport_7_2_3_artefakter.md) § 4.3 dokumenterer at IDs beholdes i kildefilen for intern sporbarhet.

---

## Del 2 – Nye funn

### R1. Innsettingsrekkefølgen i [rapport_7_2_2_artefakter.md](../rapport_7_2_2_artefakter.md) § 3 refererer fortsatt til «Tabell 5.1»

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

[rapport_7_2_2_artefakter.md](../rapport_7_2_2_artefakter.md) linje 127–128 i «§ 3 Innsettingsrekkefølge i § 5.2 for 7.2.4» sier fortsatt:

> 5. Figur 5.2 (etter Tabell 5.4 og før den eksisterende **Tabell 5.1** om datasplitt).
> 6. **Tabell 5.1** beholdes uendret på dagens posisjon i § 5.2.

Dette er inkonsistent med V1-rettelsen der Tabell 5.1 ble renummerert til Tabell 5.5. Feilen er kosmetisk; rapporten er korrekt. Men leveransefilens §-hode («Innsettingsrekkefølge for 7.2.4») antyder at dette er sporbar dokumentasjon for hvordan 7.2.4 ble gjennomført, og da bør innholdet gjenspeile det faktiske resultatet.

**Anbefalt tiltak:** Erstatt «Tabell 5.1» med «Tabell 5.5» i begge linjene.

### R2. Utdatert oppsummering i [status.md](../status.md) «Anbefalt kort prosjektstatus»

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

[status.md](../status.md) linje 85 («Anbefalt kort prosjektstatus» oppsummerer situasjonen per 2026-04-19 slik den så ut ved lukking av 7.2.1. Den nevner «Tabell 5.1» og «14 innholdstabeller». Etter V1 og F2 er disse tallene utdaterte: Tabell 5.1 heter nå Tabell 5.5, og utvalget teller 16 innholdstabeller (15 i kap. 5–9 + Tabell 12.1).

**Anbefalt tiltak:** Oppdater setningen når hele 7.2-blokken formelt lukkes (F5). Det bør gjøres i samme edit som statusoppdateringen for 7.2.2, 7.2.3 og 7.2.4. Oppdateres:

- «5.2 Data med Tabell 5.1» → «5.2 Data med Tabell 5.2–5.5»
- «14 innholdstabeller (5 beholdes, 10 er nye), og i tillegg 7 vedleggsreferanser» → «16 innholdstabeller (5 beholdes, 10 er nye i kap. 5–9, og Tabell 12.1 i kap. 12), samt 7 vedleggsreferanser (A1–A7) samlet i Tabell 12.1».

### R3. Eksempel i utvalgsdokumentet § 3 bruker «Tabell 5.1» som illustrasjon

**Alvorlighetsgrad:** Lav
**Kategori:** Språk og innhold

[rapport_fig_tab_utvalg.md](../rapport_fig_tab_utvalg.md) linje 35 bruker «Tabell 5.1» som illustrerende eksempel for konvensjon (b) kapittelbundne numre. Siden rapporten ikke lenger har Tabell 5.1, er eksempelet lesevildende for noen som leser utvalgsdokumentet etter at V1 er utført.

**Anbefalt tiltak:** Bytt eksempelet til en tabell som faktisk finnes, f.eks. «Tabell 5.2, Tabell 8.1 …» eller «Tabell 6.1, Tabell 8.1 …».

---

## Avhukningsliste – tiltak

| # | Tiltak | Kategori | Status | Kommentar |
|:--|:-------|:---------|:-------|:----------|
| R1 | Erstatt «Tabell 5.1» med «Tabell 5.5» i [rapport_7_2_2_artefakter.md](../rapport_7_2_2_artefakter.md) linje 127–128 | Språk og innhold | [x] | Gjennomført 2026-04-19. Innsettingsrekkefølgen oppdatert til «Tabell 5.5 (splittabellen, renummerert fra tidligere Tabell 5.1 etter V1 i helhetsreviewen)». |
| R2 | Oppdater «Anbefalt kort prosjektstatus» i [status.md](../status.md) når 7.2-blokken formelt lukkes | Språk og innhold | [x] | Gjennomført 2026-04-19. Prosa oppdatert til 10 figurer, 16 innholdstabeller, Tabell 5.2–5.5 og Tabell 9.1–9.3 nevnt eksplisitt. |
| R3 | Bytt eksempeltabell i utvalgsdokumentet § 3 «(b) Kapittelbundne numre» fra «Tabell 5.1» til en eksisterende tabell | Språk og innhold | [x] | Gjennomført 2026-04-19. Eksempel endret til «Tabell 5.2, Tabell 6.1, Tabell 8.1 …». |

---

## Samsvar med prosjektplan og krav

| Sjekkpunkt | Status | Kommentar |
|:---|:---|:---|
| Lærerens formkrav 1 (nummereres i rekkefølgen de omtales) | OK | Verifisert i rapport.md: alle figur- og tabellsekvenser er stigende per kapittel. |
| Tabell 9.3 ID-kolonne fjernet | OK | Verifisert: ingen `MB-6.2-` i rapport.md; kildefilen beholder IDs. |
| Tabell 7.2 norsk kolonnespråk | OK | Verifisert: ingen `quarter/discount_band/sales_band/hoy` i rapport-Tabell 7.2. |
| Utvalgsdokument § 3 regel 6 | OK | Ny regel lagt til. |
| Utvalgsdokument 16 innholdstabeller | OK | § 11 oppdatert. |
| Tabell 12.1 dokumentert i § 9 | OK | Eksplisitt nevnt. |
| status.md F1-subnote under WBS 7.3.1 | OK | Lagt til. |
| Helhetsreview-avhukningsliste V1–V4, F1–F4 krysset av | OK | Alle `[x]` i [7_2_full_helhetsreview-CLAUDE.md](7_2_full_helhetsreview-CLAUDE.md). |
| UTF-8 uten BOM, `æ/ø/å` bevart i alle endrede filer | OK | `file`-kommando bekrefter UTF-8 for alle seks filer. |

---

## Samlet vurdering

### Metodikk

Alle åtte tiltak fra helhetsreviewen er korrekt gjennomført i kjernerapporten. Formkrav 1 er nå oppfylt både for figurer og tabeller; Tabell 9.3 har fått riktig antall kolonner og Tabell 7.2 bruker norsk kolonnespråk med `ø`. Reviewen finner ingen nye metodiske svakheter.

### Språk, innhold og figurer

De tre nye funnene (R1, R2, R3) er alle av kosmetisk karakter og gjelder tekst i støttedokumenter (leveransefil, status.md-prosa, eksempel i utvalgsdokument). Ingen av dem påvirker rapporten eller leseropplevelsen der. R2 lukkes naturlig sammen med F5 (formell avslutning av 7.2-blokken i status.md og wbs.json); R1 kan inkluderes i samme edit.

### Anbefalt prioritering videre

Alle gjenstående tiltak fra denne verifikasjonsreviewen og F5 fra helhetsreviewen er gjennomført 2026-04-19.

1. ~~**(Må)** Lukk F5 – oppdater [status.md](../status.md) og [wbs.json](../wbs.json) for 7.2.2, 7.2.3 og 7.2.4. Kombiner med R2 for å oppdatere «Anbefalt kort prosjektstatus» samtidig.~~ Gjennomført. 7.2.2, 7.2.3 og 7.2.4 satt til `[x]` i status.md og `100%` i wbs.json; datolinjen oppdatert til «WBS 7.2-blokken lukket»; «Anbefalt kort prosjektstatus» og H-raden oppdatert med korrekt figur-/tabelltelling.
2. ~~**(Bør)** Lukk R1 – erstatt «Tabell 5.1» med «Tabell 5.5» i [rapport_7_2_2_artefakter.md](../rapport_7_2_2_artefakter.md).~~ Gjennomført.
3. ~~**(Kan)** Lukk R3 – bytt eksempeltabell i utvalgsdokumentet § 3; lav prioritet, kan tas i 7.3.1.~~ Gjennomført.

Ingen blokkerende funn. Rapporten er klar for 7.3.x.
