---
name: review-act
description: >-
  Gjennomfør en systematisk review av en prosjektaktivitet.
  Bruk når en aktivitet skal reviewes og lukkes.
  Triggeres av «review aktivitet», «review ACT-X.Y» eller «/review-act».
argument-hint: "[aktivitets-ID, f.eks. 3.2]"
allowed-tools: Read, Glob, Grep, Bash, Agent, Write, Edit, AskUserQuestion
---

# Skill: Review av prosjektaktivitet

Du skal gjennomføre en systematisk review av en prosjektaktivitet i Dagligvare-prosjektet. Følg stegene nedenfor i rekkefølge.

## Steg 1 – Identifiser aktiviteten

Bruk argumentet (f.eks. `3.2`) til å slå opp aktiviteten i prosjektplanen.

- Les `012 fase 2 - plan/schedule.json` for å finne aktivitetens fulle navn, planlagte datoer og avhengigheter.
- Les `012 fase 2 - plan/requirements.json` for å finne tilknyttede krav (REQ-xxx) og ferdighetskriterier (ACT-X.Y-Cxx).
- Les `012 fase 2 - plan/status.md` for å finne aktivitetens nåværende status og sjekkliste.

Bekreft at aktiviteten finnes og at den er klar for review (dvs. at arbeidet er utført).

## Steg 2 – Les prosjektkontekst

- Les `CLAUDE.md` for rapportstruktur, figurformat og andre arbeidsregler.
- Les `012 fase 2 - plan/reviews/REVIEW-MAL.md` for å forstå review-malen du skal fylle ut.
- Sjekk om det finnes andre reviewer av samme aktivitet i `012 fase 2 - plan/reviews/`.

## Steg 3 – Utforsk artefakter

Finn aktivitetsmappen under `006 analysis/aktiviteter/`. Typisk navngiving: `X_Y_aktivitetsnavn/`.

- List alle filer i mappen (skript, figurer, resultater, README).
- Les hvert skript og forstå hva det gjør.
- Les genererte resultater (tabeller, CSV-filer) og sammenlign med rapportteksten.
- Kontroller at figurer har korrekt format og innhold.

## Steg 4 – Les rapportteksten

- Identifiser hvilke kapitler og seksjoner i `005 report/rapport.md` som tilhører aktiviteten.
- Les disse seksjonene grundig.
- Sjekk konsistens mellom genererte artefakter og rapporttekst (tall, figurnummer, tabellverdier).

## Steg 5 – Sjekk git-historikk

Kjør `git log --oneline` med relevante filbaner for å forstå arbeidsflyten og identifisere eventuelle uventede endringer.

## Steg 6 – Gjennomfør vurderingen

Vurder aktiviteten langs to akser:

### Del 1 – Metodikk (beregninger og kode)
- Er beregninger og formler korrekte?
- Er koden reproduserbar?
- Er datagrunnlaget behandlet riktig?
- Er det konsistens mellom genererte artefakter og rapporten?
- Er kravene i prosjektplanen oppfylt?

### Del 2 – Språk, innhold og figurer
- Språk: Skrivefeil, klarhet, norsk fagspråk.
- Innhold: Logisk sammenheng, faglig presisjon.
- Figurer: Titler, akselabeler, format per CLAUDE.md.
- Tabeller: Konsistens med genererte artefakter.
- Referanser: Figur- og tabellhenvisninger, kryssreferanser.

Identifiser:
- **Styrker** (S1, S2, …): Hva som er bra.
- **Svakheter** (V1, V2, …): Feil eller mangler som bør fikses. Angi alvorlighetsgrad (Høy/Middels/Lav).
- **Forbedringsforslag** (F1, F2, …): Forslag som kan vurderes. Angi alvorlighetsgrad.

## Steg 7 – Skriv review-filen

Opprett review-filen i `012 fase 2 - plan/reviews/` med filnavn etter mønsteret:
`X_Y_aktivitetsnavn-CLAUDE.md`

Bruk malen fra `012 fase 2 - plan/reviews/REVIEW-MAL.md` og fyll ut alle seksjoner. Slett hjelpetekst i HTML-kommentarer.

Inkluder:
- Sammendrag
- Styrker
- Del 1 – Metodikk
- Del 2 – Språk, innhold og figurer
- Svakheter og forbedringsforslag med alvorlighetsgrad
- Avhukningsliste med `[ ]` for hvert tiltak
- Samsvar med prosjektplan og krav
- Samlet vurdering med anbefalt prioritering

## Oppsummering

Gi brukeren en kort oppsummering av reviewen:
- Antall styrker, svakheter og forbedringsforslag
- De viktigste funnene
- Anbefalt prioritering videre
