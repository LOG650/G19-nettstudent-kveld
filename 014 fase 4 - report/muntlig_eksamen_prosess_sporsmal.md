# Muntlig eksamen – prosess-spørsmål (hvordan prosjektet ble utført)

Spørsmål sensor kan stille om **selve arbeidsprosessen** – prosjektstyring,
samarbeid, kvalitetssikring, reproduserbarhet og verktøybruk – ikke om
rapportinnholdet. Hvert spørsmål har svarstikkord forankret i de faktiske
prosjektartefaktene (prosjektstyringsplan, endringslogg, status.md, reviews,
git). Søsterfiler: [muntlig_eksamen_intro.md](muntlig_eksamen_intro.md) (intro)
og [muntlig_eksamen_sporsmal.md](muntlig_eksamen_sporsmal.md) (innhold).

> **Viktig før dere svarer:** Prosjektstyringsplanen beskriver en ganske formell
> styringsmodell (ukentlige møter, sponsor-gjennomganger, endringskontrollstyre,
> risikobudsjett). Deler av dette er malbasert og idealisert. **Svar ut fra det
> dere faktisk gjorde** – ikke les opp planen som om alt skjedde nøyaktig slik.
> To konkrete avvik å være forberedt på: (1) planen nevner *Gemini CLI* som
> KI-verktøy, mens arbeidet i praksis ble gjort med Claude (se `CLAUDE.md` og
> `.claude/`); (2) planen beskriver peer review *internt i gruppa*, men de
> dokumenterte reviewene er KI-assisterte. Vær ærlige på dette.

---

## Tema 1 – Prosjektorganisering og faseinndeling

**Hvordan var prosjektet organisert, og hvilke faser gikk dere gjennom?**

Fire faser med egne mapper: `011 fase 1 – proposal` (prosjektforslag),
`012 fase 2 – plan` (prosjektstyringsplan), `013 fase 3 – review` (peer review),
`014 fase 4 – report` (endelig rapport). Analysen ligger i `006 analysis` og
selve rapporten i `005 report`. Hver fase hadde en konkret leveranse koblet til
milepælene M1–M6.

**Hva er sammenhengen mellom WBS, analysemappene og rapporten?**

WBS-en (arbeidsnedbrytningsstrukturen) er ryggraden. De 18 aktivitetsmappene i
`006 analysis/aktiviteter/` er navngitt og nummerert etter WBS (f.eks. `08_lineaer_regresjon`
= WBS 4.1, `13_rmse_og_mape` = WBS 5.2). Rapportkapitlene henter tall og figurer
fra disse aktivitetene, og status.md sporer hver WBS-oppgave til den filen som
dokumenterer den. Slik er det full sporbarhet fra plan → analyse → rapport.

**Hvorfor delte dere arbeidet opp på denne måten?**

For styring og sporbarhet. Den opprinnelige grovinndelingen (7.1–7.3) ble for
upresis, så rapportfasen ble splittet i operative underaktiviteter 7.1.1–7.3.3
(dokumentert i endringsloggen 2026-04-12). Finere oppdeling gjorde det lettere å
følge fremdrift, fordele arbeid og oppdatere status uten å «late som» store deler
var ferdige.

---

## Tema 2 – Planlegging og styring

**Hvordan planla dere fremdriften?**

Med en formell prosjektstyringsplan (datert 2026-03-10): WBS med 8 hovedområder
(senere 39 oppgaver på nivå 3), et AOA-avhengighetsdiagram med hovedaktiviteter
A–I, en Gantt-plan og milepæler M1–M6. Planen er et levende dokument som skulle
oppdateres underveis.

**Hadde dere en kritisk vei?**

Ja. Alle hovedaktivitetene lå sekvensielt på kritisk linje: A (problem/plan) → B
(datainnsamling) → C (dataforståelse) → D (preprosessering) → E (feature
engineering) → F (modellbygging) → G (analyse/evaluering) → H (rapport) → I
(konklusjon/presentasjon). Enhver forsinkelse i én aktivitet forskyver hele
planen – noe vi merket på M5.

**Hvilke milepæler hadde dere, og holdt dere dem?**

M1 forslag godkjent (feb), M2 datagrunnlag (10. mars), M3 modelltesting (23.
mars), M4 optimalisering (22. april), M5 hovedutkast (8. april), M6 endelig
rapport (19. mai). De fleste ble nådd, men **M5 ble nådd 16 dager forsinket**
(utkastet låst 2026-04-24 i stedet for 8. april). M3 ble også dokumentert litt
forsinket (2026-04-07). Vær ærlige på forsinkelsene – de er dokumentert i
status.md.

**Hvordan håndterte dere risiko?**

Risikoregister med fem risikoer (R1–R5) med eier, utløser, tiltak og
beredskapsplan: R1 manglende/inkonsistente data, R2 lav prediksjonsnøyaktighet,
R3 manglende verktøy-/metodeerfaring, R4 tidsmangel mot slutten, R5 teknisk feil i
miljø. *(Merk: planen beskriver også et «risikobudsjett» i kroner – det er
malbasert og ikke reelt for et studentprosjekt; svar på de faktiske risikoene.)*

---

## Tema 3 – Roller, ansvar og kommunikasjon

**Hvordan fordelte dere ansvaret i gruppa?**

Matriseorganisering med fagansvar: **Erik** – prosjektleder og lead data
scientist, eier av lineær regresjon og datavasking. **Joseph** – teknisk
ansvarlig og fremdriftsplanlegger, eier av Random Forest og korrekt
tidshåndtering i trening/test. **Pål** – kvalitetsleder/logistikkanalytiker,
ansvarlig for RMSE/MAPE og overfitting-kontroll. **Marthe** – kommunikasjons- og
interessentkontakt, koordinering og oversettelse av tekniske resultater. **BIP**
er prosjektsponsor.

**Hvordan koordinerte dere arbeidet underveis?**

Per plan: ukentlige statusmøter (mandag kl. 09:00), månedlige
sponsor-gjennomganger ledet av BIP (første tirsdag kl. 13:00), et
endringskontrollstyre (CCB) ledet av Pål ved behov, og daglig koordinering via
Teams + GitHub (Joseph). *(Bekreft hvor formelt dette faktisk var hos dere –
svar på den reelle praksisen.)*

**Hvordan bidro alle fire når Erik står for nesten alle commits?**

Ærlig og viktig spørsmål: git viser at Erik står for ~97 av 104 commits, men det
gjenspeiler **hvem som pushet**, ikke hele arbeidsinnsatsen. Arbeidet ble fordelt
på fagområder (LR, RF, kvalitet/metrikker, kommunikasjon/rapport) og på
WBS-aktiviteter, og planlegging, analyse, skriving og gjennomlesing skjedde i
fellesskap. Vær konkrete på hva hver enkelt faktisk gjorde.

---

## Tema 4 – Endringshåndtering

**Endret planen seg underveis – hvordan dokumenterte dere det?**

Vi førte en egen endringslogg (`012 fase 2 – plan/endringslogg.md`) med fem
oppføringer, hver med *hva*, *hvorfor*, *konsekvens* og *beslutningsgrunnlag*.
Dette er knyttet til endringskontrollprosessen i styringsplanen (registrer →
vurder → analyser konsekvens → beslutt → implementer → dokumenter).

**Gi et eksempel på en endring og hvorfor dere tok den.**

To gode eksempler (begge 2026-04-02): WBS 4.4 ble **avgrenset til tuning av
Random Forest** fordi lineær regresjon allerede var dokumentert som fast
benchmark og videre tuning der ville utvidet modellomfanget mot regulariserte
varianter utenfor WBS. Samtidig ble WBS 4.3 «trene modellene» **omtolket til et
lett verifiseringssteg**, siden treningen allerede var gjort i 4.1 og 4.2 – en ny
runde ville vært redundant.

**Hadde dere andre dokumenterte endringer?**

Ja: figur-/tabellutvalget i 7.2.1 ble utvidet til maksimalt utvalg (2026-04-19)
for å utnytte analysegrunnlaget og møte lærerens anbefaling; og selskapsnavnet
ble rettet fra «PowerHorse» (mal-rest) til «Dagligvare» (2026-04-13). Poenget er
at endringene ble fanget og begrunnet, ikke gjort i det skjulte.

---

## Tema 5 – Analysearbeid og reproduserbarhet

**Hvordan er analysen organisert teknisk?**

Som 18 nummererte aktivitetsmapper under `006 analysis/aktiviteter/`, én per
WBS-oppgave, i ett felles `uv`-prosjekt (Python 3.12). Hver mappe har skript,
resultattabeller, figurer og en kort markdown-oppsummering + README. Vi brukte
`.py`-skript, ikke Jupyter-notebooks.

**Hvorfor skript fremfor notebooks?**

Skript gir batch-reproduserbarhet og rene diff-er i git, tvinger fram en ryddig
kjørerekkefølge (hver `start_wbs_*.py` validerer input før den kjører), og unngår
notebook-problemer som skjult tilstand og celler kjørt i feil rekkefølge. Det
passer en sporbar, etterprøvbar pipeline bedre.

**Hvordan sikret dere at resultatene kan reproduseres?**

Flere grep: faste seeds (`random_state=42`) for Random Forest; låst miljø via
`uv.lock` og `.python-version`; konsekvent navnekonvensjon (`fig_`, `tab_`,
`model_`); serialiserte modeller (`.joblib`) som gjenbrukes nedstrøms uten ny
trening; og inputvalidering i hvert skript. WBS 4.3 verifiserer eksplisitt at
begge modellene er trent på samme grunnlag (6 682 rader × 67 features) før
prognosene lages.

**Hvilke biblioteker brukte dere, og hvorfor?**

pandas/numpy (databehandling og numerikk), scikit-learn (LinearRegression,
RandomForestRegressor, RMSE/MAPE), matplotlib/seaborn (figurer). Alt er
open-source og gratis, valgt for utbredelse, stabilitet og etterprøvbarhet.

---

## Tema 6 – Kvalitetssikring: intern review og peer review

**Hvordan kvalitetssikret dere rapporten internt?**

Med en standardisert review-mal (`reviews/REVIEW-MAL.md`) og ~12 reviews. Hver
review lister styrker, svakheter (V) og forbedringsforslag (F) med alvorlighetsgrad
(Høy/Middels/Lav), tildeler ansvar og sporer at punktene lukkes. Funn som ikke ble
løst med en gang, ble eksplisitt overført til neste steg.

**Beskriv kvalitetssikringskjeden for rapporten.**

Tre trinn i WBS 7.3: **7.3.1 struktur- og kravsjekk** (mot CLAUDE.md og
sjekklisten, KR-001–KR-006), **7.3.2 konsistenssjekk** (alle nøkkeltall i
Sammendrag/Abstract kontrollert mot kilde-CSV innen ±0,005; 16 tabeller og 10
figurer verifisert), og **7.3.3 språkvask** (lukket de fem overførte F-punktene
med målrettede endringer). Deretter ble førsteutkastet **låst** 2026-04-24.

**Hva fanget konsistenssjekken konkret?**

Den bekreftet at ankertall som RMSE 578,26, MAPE 43,97 %, 11/12 måneder, 13/14
segmenter, 67 features og 9 994 transaksjoner stemte mot kildefilene. Den fanget
også en faktafeil: en MAPE-verdi i segmentanalysen var feilattribuert (89,39 %
var baseline RF, ikke tuned RF som skulle vært 90,27 %) – rettet i språkvasken.

**Hvordan fungerte peer review mot en annen gruppe?**

Gjensidig: G19 vurderte G17 sin rapport mot lærerens rubrikk med sju
vurderingsområder (innledning, litteratur/teori, metode, analyse/resultat,
diskusjon, konklusjon, skriveflyt/form), og fikk tilsvarende review tilbake fra
G17. Leveransene ligger i `013 fase 3 – review/015 Peer To Peer/` (vår review av
G17) og `016 Review From G17/` (deres review av oss).

**Var reviewene gjort av mennesker eller KI?**

Vær åpne: de interne reviewene er KI-assisterte (dokumentert som `*-CLAUDE.md`),
mens peer review mot G17 er gruppas faglige vurdering. Gruppa står faglig inne for
alle funn og rettelser uansett verktøy.

---

## Tema 7 – Verktøy og bruk av KI

**Hvilke verktøy formet arbeidsflyten?**

Git/GitHub for versjonskontroll og samarbeid; `uv` for et reproduserbart
Python-miljø; VS Code som utviklingsmiljø; pandoc + LaTeX for å bygge PDF av
rapporten; og prosjektregler i `CLAUDE.md` (norsk språk, æ/ø/å, løpende
rapportskriving, `fig_`/`tab_`-konvensjon) som styrte hvordan vi jobbet.

**Hvordan brukte dere kunstig intelligens, og hvordan sikrer dere faglig
integritet?**

KI ble brukt som verktøy i analyse-, review- og rapportarbeidet, åpent dokumentert
i endringslogg og i den obligatoriske egenerklæringen. Integriteten sikres ved at
gruppa har skrevet og godkjent rapporten i fellesskap og står faglig inne for
innholdet, og ved at pipelinen er reproduserbar med faste seeds og sporbare
artefakter. *(Merk avviket: styringsplanen nevner Gemini CLI, mens det faktiske
arbeidet ble gjort med Claude – svar på det dere faktisk brukte.)*

**Hva er igjen / hva er neste steg etter innleveringen?**

Per WBS gjenstår fase 8: revisjon (8.1), endelig konklusjon (8.2), forberede
presentasjon (8.3) og selve presentasjonen/prosjektslutt (8.4) – altså denne
muntlige eksamenen. Overført til 8.1 var bl.a. å synke en analyse-CSV
(`State = ekskluder`), dokumentere M5-forsinkelsen og vurdere fagfellevurderte
tilleggskilder.

---

## Tips til spørrerunden

- **Eie det reelle:** Skill mellom hva planen sier og hva dere faktisk gjorde.
  Sensor verdsetter ærlighet om forsinkelser (M5), KI-bruk og malbaserte deler av
  styringsplanen mer enn en glansbildeversjon.
- **Bruk artefakter som bevis:** Pek på endringsloggen, status.md, review-filene
  og WBS-mappene når dere forklarer prosessen – det viser sporbarhet.
- **Vis sammenhengen plan → analyse → rapport:** WBS-nummer går igjen i
  mappenavn, status og rapport. Det er den røde tråden.
- **Fordel temaene:** La den som eide et område svare på det (Erik styring/LR,
  Joseph teknisk/RF, Pål kvalitet/review, Marthe kommunikasjon/koordinering).
