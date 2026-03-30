# Handoff: Lag prosjektspesifikk videreføringsstatus

## Mål

Lag et strukturert handoff-dokument som gjør at neste økt eller agent kan fortsette arbeidet uten å gjette hva som ble gjort, hva som gjenstår og hvilke valg som allerede er tatt. Dette er et `skriv + komprimer`-mønster: du lagrer øktens viktigste arbeidsminne i repoet og kutter det ned til det som faktisk er nyttig.

## Når brukes kommandoen

- Før du avslutter en lengre økt som skal videreføres senere
- Før kontekstvinduet blir fullt
- Når du går fra én prosjektfase til en annen, for eksempel analyse til rapportskriving
- Når arbeid skal overtas av et annet menneske eller en ny agentøkt
- Når du ikke vil stole på at muntlig kontekst alene er nok

## Prosess

### 1. Analyser den pågående økten

Gå gjennom hva som faktisk skjedde i økten:

- Hva var den opprinnelige oppgaven?
- Hva ble fullført?
- Hva er pågående eller blokkert?
- Hvilke viktige beslutninger ble tatt, og hvorfor?
- Hvilke filer ble lest, opprettet eller endret?
- Hvilke feil eller misforståelser oppstod, og hvordan ble de håndtert?
- Hvilke blindspor bør neste økt unngå?

### 2. Hent inn prosjektstatus

```bash
git status --short
git diff --stat HEAD
git log --oneline -5
git branch --show-current
```

Hvis økten berørte analysearbeid, les også relevante filer i `006 analysis/aktiviteter/...`.

Hvis økten berørte rapport eller prosjektstyring, kontroller også relevante deler av:

- `005 report/rapport.md`
- `012 fase 2 - plan/status.md`
- `012 fase 2 - plan/wbs.json`
- `012 fase 2 - plan/prosjektstyringsplan.md`

### 3. Skriv handoff-dokumentet

Lagre til: `HANDOFF.md` i repo-roten.

Bruk denne strukturen:

```
# Handoff: [Kort oppgavebeskrivelse]

**Dato:** [dagens dato]
**Gren:** [gjeldende branch]
**Siste commit:** [hash + melding, eller "ukommitterte endringer"]

## Mål

[1-2 setninger om hva som skal oppnås. Ta med brukeroppgaven eller relevant WBS-/planreferanse.]

## Ferdig

- [x] [Oppgave 1 — kort beskrivelse av hva som ble gjort]
- [x] [Oppgave 2 — kort beskrivelse]

## Pågår / Neste steg

- [ ] [Neste oppgave — konkret nok til at noen kan starte direkte]
- [ ] [Videre arbeid — med filstier og fokusområder]
- [ ] [Eventuelle blokkeringer — med forklaring]

## Viktige beslutninger

- **[Beslutning]**: [Hva som ble valgt] — [Hvorfor, gjerne med alternativ som ble forkastet]
- **[Beslutning]**: [Hva som ble valgt] — [Hvorfor]

## Blindspor (ikke gjenta disse)

- [Forsøk eller spor som ikke fungerte] — [Hvorfor]
- [Undersøkelse som viste seg irrelevant] — [Hva som viste seg å være riktig spor]

## Filer endret

- `sti/til/fil.md` — [hva som ble endret og hvorfor]
- `sti/til/ny_fil.py` — [NY: hva filen gjør]
- `sti/til/slettet_fil` — [SLETTET: hvorfor]

## Nåværende status

- **Tester/kjøring:** [hva som ble kjørt, og resultat]
- **Analyseartefakter:** [hva som ble generert eller verifisert]
- **Rapport:** [hvilke deler av `rapport.md` som ble oppdatert eller fortsatt henger etter]
- **Plan/status:** [om `status.md`, `wbs.json` eller andre planfiler ble oppdatert]
- **Manuell verifisering:** [kort resultat]

## Kontekst for neste økt

[2-4 setninger om den viktigste konteksten. Hva er situasjonen nå? Hva er den største risikoen? Hva bør gjøres først?]

**Anbefalt første handling:** [eksakt kommando eller første steg]
```

### 4. Prosjektspesifikke krav til handoff

- Skriv på norsk.
- Bruk eksplisitte datoer når fremdrift eller forsinkelse omtales.
- Merk antagelser som antagelser.
- Hvis analysearbeid er fullført uten at rapport eller plan/status er oppdatert, skriv dette tydelig som et gjenstående avvik.
- Hvis du fant rester fra eksempelprosjekter eller annen utdatert kontekst, skriv det under `Blindspor` eller `Viktige beslutninger`.
- Hold handoffet kort og operativt. Det skal være lett å skanne.

### 5. Bekreft og gi råd

Etter at `HANDOFF.md` er skrevet:

1. Bekreft full filsti til `HANDOFF.md`
2. Foreslå neste oppstartskommando:
   ```text
   Les HANDOFF.md og fortsett fra forrige økt.
   ```
3. Hvis det finnes ukommitterte endringer, foreslå også:
   ```text
   /commit
   ```

## Kvalitetskriterier

Et godt handoff-dokument skal:

- gjøre det mulig å fortsette uten avklaringsspørsmål
- være under 100 linjer
- forklare nok `hvorfor` til at neste økt tar samme beslutninger
- liste blindspor for å unngå dobbeltarbeid
- ha en konkret anbefalt første handling

## Unngå dette

- Ikke lim inn fulle filinnhold. Referer til filstier.
- Ikke gjengi hele samtalen eller rå debuglogger. Oppsummer funnene.
- Ikke vær vag. Skriv konkret hva som gjenstår og hvor.
- Ikke hopp over `Blindspor`.
- Ikke hopp over `Viktige beslutninger`.
- Ikke glem å nevne hvis rapport, analyse og plan/status er ute av sync.
