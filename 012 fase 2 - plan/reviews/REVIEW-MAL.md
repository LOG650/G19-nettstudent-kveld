# Review av aktivitet X.X – «Aktivitetsnavn»

<!--
  Mal for aktivitetsreview i PowerHorse-prosjektet.
  Basert på erfaringer fra review av aktivitet 3.1.

  Bruk:
  1. Kopier denne filen og gi den navn etter aktiviteten:
     <aktivitetsnummer>_<aktivitetsnavn>-<REVIEWER>.md
     Eksempel: 3_2_velge_og_estimere_modell-CLAUDE.md
  2. Fyll ut alle seksjoner. Slett hjelpetekst (i HTML-kommentarer) når du er ferdig.
  3. Oppdater avhukningslisten etter hvert som tiltak gjennomføres.
-->

**Reviewer:**
**Dato:**
**Aktivitetsmappe:** `006 analysis/aktiviteter/...`
**Planreferanse:** Aktivitet «...», planlagt YYYY-MM-DD til YYYY-MM-DD

---

## Sammendrag

<!-- 2–3 setninger: Hva er hovedinntrykket? Hvor mange svakheter, forbedringsforslag og styrker? -->

---

## Styrker

<!-- List de viktigste styrkene. Bruk S1, S2, … som prefiks. Kort og konkret. -->

- **S1.** ...
- **S2.** ...

---

## Del 1 – Metodikk (beregninger og kode)

<!--
  Vurder det faglige og tekniske arbeidet:
  - Er beregninger og formler korrekte?
  - Er koden reproduserbar (kan kjøres fra tomt miljø og gi samme resultat)?
  - Er datagrunnlaget behandlet riktig (filtrering, aggregering, splitting)?
  - Er det konsistens mellom genererte artefakter og det som står i rapporten?
  - Er kravene i prosjektplanen oppfylt (REQ-xxx)?
-->

### 1.1 «Navn på tema/funksjon»

<!-- Beskriv hva som er vurdert, hva som er funnet, og gi en kort vurdering. -->

**Vurdering:** ...

### 1.2 «Neste tema»

**Vurdering:** ...

### Gjenstående metodiske observasjoner

<!-- Eventuelle observasjoner som ikke er svakheter, men som bør nevnes. -->

---

## Del 2 – Språk, innhold og figurer

<!--
  Vurder rapportteksten som hører til aktiviteten:
  - Språk: Skrivefeil, setningslengde, klarhet, norsk fagspråk.
  - Innhold: Logisk sammenheng, faglig presisjon, unødvendig repetisjon.
  - Figurer: Titler, akselabeler, oppløsning, norske tekster, konsistens mellom figurer.
  - Tabeller: Kolonneoverskrifter, formatering, konsistens med genererte artefakter.
  - Referanser: Figurhenvisninger (f.eks. «figur X.X»), tabellhenvisninger, kryssreferanser.
  - Struktur: Følger teksten rapportmalen i CLAUDE.md?
-->

### 2.1 Rapporttekst – «avsnitt/kapittel»

<!-- Siter den aktuelle teksten og vurder språk og faglig innhold. -->

**Språk:** ...

**Faglig innhold:** ...

### 2.2 Figurer – rapportklarhet

<!-- Vurder alle figurer som tilhører aktiviteten. -->

| Figur | Tittel i figur | Vurdering |
|:------|:---------------|:----------|
| X.X | «...» | ... |

### 2.3 Tabeller – konsistens og lesbarhet

<!-- Sjekk at tabeller i rapporten stemmer med genererte artefakter. Vurder kolonneoverskrifter. -->

### 2.4 Funn fra andre reviewer

<!--
  Hvis det finnes andre reviewer av samme aktivitet (f.eks. CODEX, peer review),
  ta inn funnene med status og vurder om de tilhører denne aktiviteten eller en senere.
  Slett denne seksjonen hvis det ikke finnes andre reviewer.
-->

| # | Funn | Alvorlighetsgrad | Status | Tilhører denne aktiviteten? |
|:--|:-----|:-----------------|:-------|:----------------------------|
| C1 | ... | Høy/Middels/Lav | Åpen/Lukket | Ja/Nei/Delvis |

---

## Svakheter og forbedringsforslag

<!--
  List alle identifiserte svakheter (V) og forbedringsforslag (F).
  Bruk alvorlighetsgrad: Høy / Middels / Lav.
  Kategoriser som V (svakhet/feil som bør fikses) eller F (forbedring som kan vurderes).
-->

### V1. «Kort beskrivelse»

**Alvorlighetsgrad:** Høy/Middels/Lav
**Kategori:** Metodikk / Språk og innhold

<!-- Beskriv problemet, konsekvensen og anbefalt tiltak. -->

### F1. «Kort beskrivelse»

**Alvorlighetsgrad:** Lav
**Kategori:** Metodikk / Språk og innhold

<!-- Beskriv forbedringsforslaget og hvorfor det er relevant. -->

---

## Avhukningsliste – tiltak

<!--
  Oppdater denne tabellen etter hvert som tiltak gjennomføres.
  Status: [ ] Ikke gjort / [x] Gjennomført / [—] Avslått (med begrunnelse)
-->

| # | Tiltak | Kategori | Status | Kommentar |
|:--|:-------|:---------|:-------|:----------|
| V1 | ... | Metodikk | [ ] | |
| F1 | ... | Språk og innhold | [ ] | |

---

## Samsvar med prosjektplan og krav

<!--
  Hent sjekkpunktene fra status.md-sjekklisten for denne aktiviteten.
  Vurder om hvert punkt er oppfylt.
-->

| Sjekkpunkt | Status | Kommentar |
|:---|:---|:---|
| ... | OK / Delvis / Gjenstår | ... |

---

## Samlet vurdering

### Metodikk

<!-- Oppsummer den faglige/tekniske vurderingen i 2–3 setninger. -->

### Språk, innhold og figurer

<!-- Oppsummer språk- og innholdsvurderingen i 2–3 setninger. -->

### Anbefalt prioritering videre

<!--
  Ranger gjenstående tiltak etter prioritet.
  Bruk (Må), (Bør) eller (Kan) som prefiks.
  Stryk over gjennomførte punkter med ~~strikethrough~~.
-->

1. **(Må)** ...
2. **(Bør)** ...
3. **(Kan)** ...
