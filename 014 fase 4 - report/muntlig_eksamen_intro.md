# Muntlig eksamen – intro-runde (LOG650, gruppe G19)

Kort intro før spørrerunden. **~4 minutter totalt, ca. 1 minutt per person.**
Hver person har to alternativer: korte **stikkord** å snakke fritt ut fra, eller
et ferdig **manus** som kan leses tilnærmet ordrett. Velg det dere er mest
komfortable med – det er lov å blande. Rapporten det gjelder er den endelige
versjonen `rapport_post_review`.

**Tittel:** «Salgsprognoser for en simulert dagligvarekjede: en sammenligning av
lineær regresjon og Random Forest Regressor.»

## Rollefordeling og rekkefølge

| # | Person | Tema | Kapittel |
|---|--------|------|----------|
| 1 | Erik | Hva prosjektet handler om + problemstilling | 1, 4 |
| 2 | Joseph | Metode, data og modeller | 3, 5, 6 |
| 3 | Pål | Resultater og hva som driver salget | 7, 8 |
| 4 | Marthe | Anbefaling, begrensninger og konklusjon | 9, 10 |

Erik åpner med tittel/tema og gir ordet videre. Marthe avslutter og markerer at
gruppen er klar for spørsmål.

---

## 1 — Erik: Innledning og problemstilling (~1 min)

**Stikkord:**

- Tema: salgsprognoser i dagligvarehandel – etterspørsel svinger med sesong,
  kampanjer, rabatt og region.
- Hvorfor det er viktig: dårlige prognoser = svinn og bundet kapital (for høyt)
  eller tomme hyller og tapte inntekter (for lavt).
- Caset: «Dagligvare», en **simulert** dagligvarekjede, 5 regioner, 7
  produktkategorier, data 2022–2025.
- Problemstilling: *Hvordan kan multippel lineær regresjon og Random Forest
  Regressor brukes til å forutsi salg for 2025, og hvilke faktorer påvirker
  salget mest?*
- To delproblemer: (1) modellvalg/prognoseytelse, (2) variabelanalyse.

**Manus (kan leses ordrett):**

> «Hei, og velkommen. Prosjektet vårt handler om salgsprognoser i
> dagligvarehandel. Etterspørselen i en dagligvarekjede svinger mye – den
> påvirkes av sesong, kampanjer, rabatter og regionale forskjeller. Og når
> prognosene bommer, blir det fort dyrt: bestiller man inn for mye, ender man
> med svinn og kapital bundet opp i varer som ikke selger; bestiller man for
> lite, får man tomme hyller og taper både inntekt og kunder. Derfor er gode
> etterspørselsprognoser helt sentralt for innkjøp, lager og planlegging.
>
> Vi har jobbet med en simulert dagligvarekjede vi kaller Dagligvare. Den
> opererer i fem regioner med syv produktkategorier, og vi har daglige
> salgsdata fra 2022 til 2025. Problemstillingen vår er todelt: Hvordan kan
> multippel lineær regresjon og Random Forest brukes til å forutsi salget for
> 2025 – og hvilke faktorer påvirker salget mest? Det første delproblemet er
> altså selve modellsammenligningen, og det andre er en analyse av hvilke
> variabler som har størst betydning. Joseph skal nå si litt om metoden og
> dataene vi har brukt.»

---

## 2 — Joseph: Metode, data og modeller (~1 min)

**Stikkord:**

- Kvantitativ, prediktiv studie. Datasett: 9 994 daglige transaksjoner.
- **Tidsbasert splitt:** trening 2022–2024 (6 682 rader), test 2025 (3 312 rader)
  – for å unngå datalekkasje (ikke tilfeldig splitt).
- 67 features: rabatt, kategoriske (region, kategori, subkategori, by) +
  7 utledede kalendervariabler.
- Tre modellspor: benchmark **lineær regresjon**, **Random Forest baseline**,
  **tuned Random Forest** (hyperparametere valgt med 2024 som valideringsår).
- Evaluering: **RMSE** primær (absolutt presisjon), **MAPE** sekundær (relativ).

**Manus (kan leses ordrett):**

> «Takk, Erik. Jeg skal si litt om hvordan vi har gått fram. Dette er en
> kvantitativ og prediktiv studie, og datagrunnlaget er nesten 10 000 daglige
> salgstransaksjoner. Det aller viktigste metodegrepet vårt er at vi splitter
> dataene på tid og ikke tilfeldig: vi trener modellene på 2022 til 2024 og
> tester dem på 2025. På den måten ser modellen aldri framtiden mens den
> trenes, og vi unngår det som kalles datalekkasje – som ellers ville gitt
> kunstig gode resultater.
>
> Etter rensing og bearbeiding endte vi opp med 67 forklaringsvariabler. Det er
> blant annet rabatt, region og produktkategori, pluss sju kalendervariabler vi
> har utledet selv fra datoen, slik som måned, ukedag og kvartal. Vi
> sammenligner tre modeller: en multippel lineær regresjon som fungerer som en
> tolkbar referanse, en Random Forest med standardinnstillinger, og en tunet
> Random Forest der vi har optimalisert innstillingene mot 2024 som
> valideringsår. Modellene måler vi med to mål – RMSE som hovedmål, fordi
> absolutt presisjon betyr mest for innkjøp, og MAPE som tilleggsmål for å se
> den prosentvise feilen. Pål tar resultatene.»

---

## 3 — Pål: Resultater og variabelanalyse (~1 min)

**Stikkord:**

- Vinner samlet: **tuned Random Forest**, RMSE 578,26 / MAPE 43,97 %.
- Vinner RMSE i **11 av 12 måneder** og **13 av 14 segmenter**.
- MEN: gapet til lineær er marginalt (~2 RMSE-enheter); lineær er best i
  segmentet «høyt salg».
- RMSE og MAPE peker ofte på ulik vinner – fordi de vekter store vs. små volum
  ulikt.
- Variabler: **rabatt (Discount)** sterkest enkeltsignal (11,48 %),
  kalendervariablene samlet ~42 % av topp 10. Region som sekundær.

**Manus (kan leses ordrett):**

> «Takk, Joseph. Da går vi til resultatene. Hovedfunnet vårt er at den tunede
> Random Forest-modellen er den samlet beste, med en RMSE på 578 og en MAPE på
> rundt 44 prosent. Den vinner på RMSE i elleve av tolv måneder og i tretten av
> fjorten segmenter når vi bryter ned på kvartal, rabattnivå, region og
> salgsnivå. Så på papiret er den en ganske tydelig vinner.
>
> Men vi vil nyansere det litt. Forspranget til den lineære modellen er faktisk
> ganske lite på totalnivå – vi snakker om noen få enheter i RMSE. Og i
> segmentet med aller høyest salg er det faktisk den lineære modellen som er
> best. Vi ser også at RMSE og MAPE ikke alltid peker på samme vinner, rett og
> slett fordi de to målene vekter store og små salgsvolum ulikt.
>
> På det andre delproblemet – hva som driver salget – er svaret tydelig: rabatt
> er det sterkeste enkeltsignalet, og kalendervariablene står til sammen for
> rundt 42 prosent av de ti viktigste variablene. Region kommer inn som en
> sekundær driver. Marthe oppsummerer hva dette betyr i praksis.»

---

## 4 — Marthe: Anbefaling, begrensninger og konklusjon (~1 min)

**Stikkord:**

- Anbefaling: **tuned RF som standardprognose** for innkjøp/lager/ressurs-
  planlegging; **lineær** som forklaringsstøtte + i toppbelastning; **baseline RF**
  som MAPE-kontroll ved høy rabatt.
- Praktisk: aggregere til uke/måned for innkjøp (dagsnivå har høy MAPE).
- Begrensninger: ett **simulert** datasett, ingen makrofaktorer, kun to
  modellfamilier, kun 2024 som valideringsår.
- Viktig forbehold: funnene er **prediktive, ikke kausale**.
- Konklusjon: differensiert modellvalg + en konkret beslutningsmatrise for
  Dagligvare.

**Manus (kan leses ordrett):**

> «Takk, Pål. Jeg skal runde av med hva vi anbefaler og hvilke forbehold vi tar.
> Konklusjonen vår er en differensiert anbefaling, ikke bare én vinnermodell.
> Dagligvare bør bruke den tunede Random Forest som standardprognose for
> innkjøp, lager og overordnet ressursplanlegging, fordi den er best på absolutt
> presisjon. Den lineære modellen bør brukes som forklaringsstøtte og som
> supplement når man planlegger for de aller høyeste salgstoppene, der den
> faktisk er sterkest. Og baseline-modellen kan brukes som en kontroll mot
> prosentfeil i perioder med høy rabatt. For innkjøp anbefaler vi i tillegg å
> aggregere prognosene til uke- eller månedsnivå, siden den prosentvise feilen
> på dagsnivå er ganske høy.
>
> Til slutt vil vi være tydelige på begrensningene. Funnene er prediktive og
> ikke kausale – de sier hva som forutsier salget, ikke hvorfor det endrer seg.
> Og det bygger på ett simulert datasett fra én virksomhet, vi har ikke med
> makroøkonomiske faktorer, og vi sammenligner bare to modellfamilier. Det
> setter grenser for hvor langt resultatene kan generaliseres. Med det er vi
> klare for spørsmål.»

---

## Praktiske tips til runden

- **Hold tiden:** ~1 min hver. Øv én gjennomkjøring høyt på forhånd så
  overgangene sitter.
- **Ingen overlapp:** Erik nevner caset kort, men detaljer om data/modeller
  hører til Joseph; tall hører til Pål; vurderinger til Marthe.
- **Overganger:** avslutt hver del med å gi ordet videre («…så lar jeg Joseph ta
  metoden»).
- **Vær trygg på kjernetallene:** RMSE 578,26 · MAPE 43,97 % · 11/12 måneder ·
  13/14 segmenter · rabatt 11,48 % · kalender ~42 %.

## Neste steg

- Lage testspørsmål med svar (egen runde). Forslag til kategorier: metodevalg
  (hvorfor tidssplitt), hvorfor RF vs. lineær, tolkning av negativ
  Discount-koeffisient, hvorfor MAPE er så høy, begrensninger og
  generaliserbarhet.
