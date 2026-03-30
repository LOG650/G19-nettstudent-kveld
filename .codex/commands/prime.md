# Prime: Last inn Dagligvare-prosjektkontekst

## Mål

Bygg rask, korrekt arbeidskontekst for LOG650-prosjektet før du gjør noe annet. Dette repoet er ikke et generisk kodeprosjekt; det er et studentprosjekt for prognoseanalyse, rapportskriving og prosjektstyring rundt Dagligvare-caset.

## Arbeidsmåte

### 1. Les styrende regler først

Les `AGENTS.md` i fulltekst.

Les `CLAUDE.md` i fulltekst.

Merk spesielt:

- all rapporttekst, status og planfiler skal skrives på norsk
- norske tegn `æ`, `ø` og `å` skal beholdes
- `rapport.md`, `status.md` og genererte Markdown-tabeller er sårbare for encoding-feil
- når noe fullføres, skal både relevante planfiler og `status.md` oppdateres
- antagelser skal merkes eksplisitt som antagelser

### 2. Kartlegg prosjektstrukturen

List toppnivået i repoet: !`find . -maxdepth 1 -mindepth 1 | sort`

List alle filer i repoet: !`rg --files`

Forstå hovedområdene:

- `005 report/` inneholder rapporten
- `006 analysis/` inneholder analysearbeid organisert etter aktiviteter
- `012 fase 2 - plan/` inneholder prosjektstyringsplan, status, WBS og krav
- `004 data/` inneholder salgsdata
- `003 references/` og `000 templates/` inneholder kilder og maler

### 3. Les prosjektets nåværende status

Les disse filene i fulltekst:

- `012 fase 2 - plan/status.md`
- `012 fase 2 - plan/prosjektstyringsplan.md`
- `012 fase 2 - plan/wbs.json`
- `012 fase 2 - plan/requirements.json`
- `006 analysis/README.md`
- `005 report/rapport.md`

Les deretter bare relevante aktivitets-README-er og arbeidsfiler for oppgaven du faktisk får.

### 4. Forstå faktisk progresjon i repoet

Sjekk git-status: !`git status --short`

Sjekk siste commits: !`git log -8 --oneline`

Bruk dette sammen med plan-, status- og WBS-filene for å forstå hva som er fullført, hva som faktisk er pågående, hva som er forsinket i forhold til plan, og hva som er neste naturlige aktivitet.

### 5. Les bare relevante detaljer for oppgaven du får

Bruk neste steg avhengig av oppgaven:

- Ved rapportarbeid: les relevante deler av `005 report/rapport.md` og eventuelt malene i `000 templates/`
- Ved analysearbeid: les README, scripts, figurer og resultatfiler i riktig aktivitetsmappe under `006 analysis/aktiviteter/`
- Ved plan/status-arbeid: les også relevante filer i `012 fase 2 - plan/` som `wbs.json`, `requirements.json`, `Prosjekt Gantt v2.csv` eller review-filer
- Ved dataspørsmål: les relevante filer i `004 data/`

Ikke les alt ukritisk hvis oppgaven er smal, men sørg for at du forstår sammenhengen mellom analyse, rapport og plan.

## Faglig kontekst som alltid skal ligge fast

- Caset gjelder en simulert dagligvarekjede og datasettet i `004 data/Dagligvare_Dataset.csv`
- Prosjektets mål er å utvikle og evaluere prognosemodeller for salg i 2025 og identifisere hvilke variabler som påvirker salget mest
- Modellsporet i repoet er multippel lineær regresjon og Random Forest Regressor
- Evalueringsmålene som er forankret i planen er MAPE og RMSE
- Analysearbeidet er strukturert etter prosjektaktiviteter, ikke bare etter kodefiler
- Rapporten skal tydelig skille mellom casebeskrivelse, metode/data, analyse, resultat, diskusjon og konklusjon
- Beskrivende historiske figurer hører hjemme i casekapitlet, ikke i analysekapitlet

## Hva du skal rapportere tilbake etter priming

Gi en kort, skannbar oppsummering som dekker:

### 1. Prosjektoversikt

- hva prosjektet handler om
- hvor rapport, analyse, data og planfiler ligger
- hvilket språk og hvilke dokumentregler som styrer arbeidet

### 2. Nåværende status

- hva plan-, status- og WBS-filene sier er fullført
- hva som faktisk er pågående nå
- hva som er neste kritiske aktivitet
- om dagens dato tilsier at prosjektet ligger foran, på eller bak plan
- eventuelle avvik mellom plan, rapport og faktiske analyseartefakter

### 3. Arbeidskonsekvenser

- hvilke filer som mest sannsynlig må berøres for neste oppgave
- om status/plan må oppdateres når oppgaven er ferdig
- eventuelle risikopunkter som encoding, utydelige antagelser eller avvik mellom rapport og analyseartefakter

## Viktig

- Skriv oppsummeringen på norsk.
- Ikke lat som om noe er verifisert hvis det bare er en antagelse.
- Hvis `cmd` viser rare tegn, behandle det som mulig visningsproblem før du antar at filen er ødelagt.
- Hvis du endrer prosjektets innhold senere, hold analyse, rapport og plan/status i sync.
- Hvis du finner rester fra eksempelprosjekter eller eldre kontekst, pek på dem eksplisitt og bruk de faktiske prosjektfilene som fasit.
