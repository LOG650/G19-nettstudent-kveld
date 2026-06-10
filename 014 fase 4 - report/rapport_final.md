# Salgsprognoser for en dagligvarekjede: en sammenligning av lineær regresjon og Random Forest Regressor <!-- omit in toc -->

## Del av LOG650 Forskningsprosjekt: Logistikk og Kunstig Intelligens <!-- omit in toc -->

\begin{center}
\includegraphics{extracted_images/image_0.png}
\end{center}

Forfatter(e): Marthe Slåtta Bjerke, Erik Brendehaug, Joseph James, Pål Rånes

Totalt antall sider inkludert forsiden: 29

Molde, Innleveringsdato: 28.05.2026

\begin{center}
\includegraphics{extracted_images/image_1.png}
\end{center}

\newpage

## Obligatorisk egenerklæring/gruppeerklæring <!-- omit in toc -->

Den enkelte student er selv ansvarlig for å sette seg inn i hva som er lovlige hjelpemidler, retningslinjer for bruk av disse og regler om kildebruk.

Du/dere fyller ut erklæringen ved å klikke i ruten til høyre for den enkelte del 1–6:

<!-- markdownlint-disable MD033 -->
| Nr. | Erklæring | Avkryssing |
| --- | --- | --- |
| 1 | Jeg/vi erklærer at min/vår besvarelse er mitt/vårt eget arbeid. | ☒ |
| 2 | Jeg/vi erklærer videre at denne besvarelsen:<br>- ikke har vært brukt til annen eksamen<br>- ikke refererer til andres arbeid uten at det er oppgitt<br>- ikke refererer til eget tidligere arbeid uten at det er oppgitt<br>- har alle referanser oppgitt<br>- ikke er kopi eller duplikat | ☒ |
| 3 | Brudd på ovennevnte er fusk og kan medføre annullering. | ☒ |
| 4 | Oppgaven kan bli plagiatkontrollert i URKUND. | ☒ |
| 5 | Høgskolen vil behandle mistanke om fusk etter retningslinjene. | ☒ |
| 6 | Jeg/vi har satt oss inn i reglene for kildebruk. | ☒ |
<!-- markdownlint-enable MD033 -->
---

## Personvern <!-- omit in toc -->

### Personopplysningsloven <!-- omit in toc -->

| Spørsmål                          | Ja | Nei |
| --------------------------------- | -- | --- |
| Har oppgaven vært vurdert av NSD? | ☐  | ☒   |

- Hvis ja:  
  Referansenummer:

- Hvis nei:  
Jeg/vi erklærer at oppgaven ikke omfattes av Personopplysningsloven  ☒

---

### Helseforskningsloven <!-- omit in toc -->

| Spørsmål                                  | Ja | Nei |
| ----------------------------------------- | -- | --- |
| Har oppgaven vært til behandling hos REK? | ☐  | ☒   |

- Hvis ja:  
  Referansenummer:

---

## Publiseringsavtale <!-- omit in toc -->

| Felt        | Verdi                    |
| ----------- | ------------------------ |
| Studiepoeng | 15                       |
| Veileder    | Bård Inge Peterson (BIP) |

### Fullmakt til elektronisk publisering <!-- omit in toc -->

| Spørsmål                                                | Ja | Nei |
| ------------------------------------------------------- | -- | --- |
| Gjøre oppgaven tilgjengelig for elektronisk publisering | ☒  | ☐   |

| Spørsmål                              | Ja | Nei |
| ------------------------------------- | -- | --- |
| Er oppgaven båndlagt (konfidensiell)? | ☐  | ☒   |

- Hvis ja:

| Spørsmål                                 | Ja | Nei |
| ---------------------------------------- | -- | --- |
| Kan publiseres etter båndleggingsperiode | ☐  | ☐   |

Dato: 28.05.2026

---

## Antall ord <!-- omit in toc -->

Rapportens hovedtekst (kap. 1 Innledning til og med kap. 10 Konklusjon) er på omtrent 5 300 ord. Sammendrag, abstract, forside, litteraturliste og vedlegg er holdt utenfor tellingen.

## Forfattererklæring <!-- omit in toc -->

Gruppen har i fellesskap skrevet og godkjent denne rapporten.

---

## Sammendrag <!-- omit in toc -->

Dagligvarehandelens driftsrisiko er direkte knyttet til kvaliteten på etterspørselsprognosene: for høye bestillinger gir svinn og bundet kapital, mens for lave gir tomme hyller og tapte inntekter. Denne rapporten undersøker hvordan multippel lineær regresjon og Random Forest Regressor kan brukes til å predikere daglig salg for 2025 i en dagligvarekjede, og hvilke faktorer som påvirker salget mest.

Analysen bygger på et datasett med 9 994 daglige salgstransaksjoner fra perioden 2022–2025. Treningsperioden 2022–2024 dekker 6 682 rader og testperioden 2025 dekker 3 312 rader, med tidsbasert splitt for å unngå datalekkasje. Modellmatrisen består av 67 features som inkluderer rabatt, kategoriske dimensjoner som region, produktkategori og subkategori, samt sju utledede kalendervariabler. Tre modellspor evalueres på 2025: en benchmark multippel lineær regresjon, en Random Forest-baseline med standardparametere, og en tuned Random Forest der hyperparametere er valgt gjennom et rutenettsøk med 2022–2023 som søketrening og 2024 som valideringsår. Modellene sammenlignes med RMSE som primær metrikk og MAPE som sekundær metrikk, både samlet, per måned og per segment fordelt på kvartal, rabattband, region og salgsnivå.

Tuned Random Forest er den samlet beste modellen med RMSE 578,26 og MAPE 43,97 %, og vinner RMSE i elleve av tolv måneder og tretten av fjorten segmenter. Gapet til benchmark lineær er marginalt på totalnivå, og benchmark lineær er best i segmentet for høyt salgsnivå. De mest påvirkningsrike prediktorene er rabatt (11,48 %) og kalendervariablene, der kalendervariablene alene utgjør om lag 42 % av importance i topp 10. Rapporten anbefaler tuned Random Forest som standardprognose for innkjøp, lager og aggregert ressursplanlegging, benchmark lineær som forklaringsstøtte, og baseline Random Forest som kontroll mot prosentfeil i høyrabattperioder. Funnene er prediktive og ikke kausale, og gjelder innenfor dette caset.

## Abstract <!-- omit in toc -->

Operational risk in grocery retail is directly linked to forecast quality: over-ordering leads to waste and tied-up capital, while under-ordering causes stock-outs and lost revenue. This report examines how multiple linear regression and Random Forest Regressor can be used to predict daily sales for 2025 in a grocery chain, and which factors influence sales the most.

The analysis uses 9,994 daily sales transactions from 2022–2025. Training data covers 2022–2024 (6,682 rows) and test data covers 2025 (3,312 rows), with a time-based split to prevent data leakage. The model matrix contains 67 features, including discount, categorical dimensions such as region, product category and sub-category, and seven derived calendar variables. Three tracks are evaluated on 2025: a benchmark multiple linear regression, a Random Forest baseline with default parameters, and a tuned Random Forest whose hyperparameters are selected via grid search on 2022–2023 with 2024 as the validation year. RMSE is the primary metric and MAPE the secondary, both overall, by month and by segment across quarter, discount band, region and sales level.

The tuned Random Forest is the overall best model with RMSE 578.26 and MAPE 43.97 %, winning RMSE in eleven of twelve months and thirteen of fourteen segments. The gap to the benchmark linear model is marginal overall, and the benchmark linear model is the strongest in the high-sales segment. The most influential predictors are discount (11.48 %) and the calendar variables, where the calendar variables alone account for around 42 % of importance in the top ten. The report recommends the tuned Random Forest as the standard forecast for purchasing, inventory and aggregate resource planning, the benchmark linear model as explanatory support, and the Random Forest baseline as a check against percentage error during high-discount periods. The findings are predictive rather than causal and apply within this case.

\newpage

## Innhold <!-- omit in toc -->

[1 Innledning](#1-innledning)\
&nbsp;&nbsp;&nbsp;[1.1 Problemstilling](#11-problemstilling)\
&nbsp;&nbsp;&nbsp;[1.2 Delproblemer](#12-delproblemer)\
&nbsp;&nbsp;&nbsp;[1.3 Avgrensinger](#13-avgrensinger)\
&nbsp;&nbsp;&nbsp;[1.4 Antagelser](#14-antagelser)\
[2 Litteratur](#2-litteratur)\
[3 Teori](#3-teori)\
&nbsp;&nbsp;&nbsp;[3.1 Multippel lineær regresjon](#31-multippel-lineær-regresjon)\
&nbsp;&nbsp;&nbsp;[3.2 Random Forest Regressor](#32-random-forest-regressor)\
&nbsp;&nbsp;&nbsp;[3.3 Evalueringsmetrikker](#33-evalueringsmetrikker)\
&nbsp;&nbsp;&nbsp;[3.4 Feature engineering og dataoppsett](#34-feature-engineering-og-dataoppsett)\
[4 Casebeskrivelse](#4-casebeskrivelse)\
&nbsp;&nbsp;&nbsp;[4.1 Dagligvare og beslutningssituasjonen](#41-dagligvare-og-beslutningssituasjonen)\
&nbsp;&nbsp;&nbsp;[4.2 Historisk salgsutvikling](#42-historisk-salgsutvikling)\
&nbsp;&nbsp;&nbsp;[4.3 Sesongmønster i salget](#43-sesongmønster-i-salget)\
&nbsp;&nbsp;&nbsp;[4.4 Utfordringer dårlige prognoser medfører i bedriften](#44-utfordringer-dårlige-prognoser-medfører-i-bedriften)\
[5 Metode og data](#5-metode-og-data)\
&nbsp;&nbsp;&nbsp;[5.1 Metode](#51-metode)\
&nbsp;&nbsp;&nbsp;[5.2 Data](#52-data)\
&nbsp;&nbsp;&nbsp;[5.3 Validitet, reliabilitet og etiske hensyn](#53-validitet-reliabilitet-og-etiske-hensyn)\
[6 Modellering](#6-modellering)\
[7 Resultat](#7-resultat)\
[8 Analyse](#8-analyse)\
[9 Diskusjon](#9-diskusjon)\
&nbsp;&nbsp;&nbsp;[9.1 Tolkning av hovedfunn mot problemstillingen](#91-tolkning-av-hovedfunn-mot-problemstillingen)\
&nbsp;&nbsp;&nbsp;[9.2 Variablenes påvirkning](#92-variablenes-påvirkning)\
&nbsp;&nbsp;&nbsp;[9.3 Hvorfor presterer modellene så likt?](#93-hvorfor-presterer-modellene-så-likt)\
&nbsp;&nbsp;&nbsp;[9.4 Praktisk nytte for Dagligvare](#94-praktisk-nytte-for-dagligvare)\
&nbsp;&nbsp;&nbsp;[9.5 Metodiske begrensninger](#95-metodiske-begrensninger)\
&nbsp;&nbsp;&nbsp;[9.6 Videre arbeid](#96-videre-arbeid)\
[10 Konklusjon](#10-konklusjon)\
[11 Bibliografi](#11-bibliografi)\
[12 Vedlegg](#12-vedlegg)

\newpage

## 1 Innledning

Dagligvarehandel er preget av høy variabilitet i etterspørsel. Salget svinger med sesong, kampanjer, rabatter og regionale forhold, og konsekvensene av dårlige prognoser er direkte synlige i driften: for høye bestillinger fører til svinn og bundet kapital, mens for lave bestillinger gir utsolgte varer og tapte inntekter. Behovet for mer presise etterspørselsprognoser er derfor sentralt når virksomheter skal fatte beslutninger om innkjøp, lager, kampanjer og ressursplanlegging.

Maskinlæringsbaserte metoder som Random Forest Regressor gir nye muligheter for å fange opp ikke-lineære mønstre i historiske salgsdata sammenlignet med tradisjonelle lineære tilnærminger. Dette prosjektet analyserer et dagligvarecase for perioden 2022–2025 med mål om å utvikle og evaluere prognosemodeller for salg i 2025, og å identifisere hvilke forklaringsvariabler som bærer mest prediksjonsverdi.

Tilnærmingen kombinerer multippel lineær regresjon som tolkbar benchmark med Random Forest Regressor som ikke-lineær alternativmodell. Kombinasjonen er valgt fordi den både måler hvor langt en enkel lineær spesifikasjon kommer på dette caset, og samtidig vurderer hva som vinnes ved en mer fleksibel ensemble-modell som naturlig leverer feature importance — den rangeringen som direkte besvarer det andre delproblemet om hvilke variabler som påvirker salget mest.

Med dette som utgangspunkt formuleres problemstillingen som styrer metodevalg, analyse og tolkning videre i rapporten.

### 1.1 Problemstilling

Hvordan kan multippel lineær regresjon og Random Forest Regressor brukes til å forutsi salg for 2025 for en dagligvarekjede, og hvilke faktorer påvirker salget mest?

### 1.2 Delproblemer

Problemstillingen dekomponeres i to delproblemer som strukturerer analyse, diskusjon og konklusjon:

1. **Modellvalg og prognoseytelse.** Hvordan sammenlignes de to modellklassene på 2025-data, målt med RMSE som primær og MAPE som sekundær metrikk, både samlet, månedlig og på tvers av segmenter som kvartal, rabattband, region og salgsnivå?
2. **Variabelanalyse.** Hvilke forklaringsvariabler har størst prediksjonsverdi, og hvordan samsvarer rangeringen fra Random Forest Regressor med koeffisientene i den lineære benchmarken?

### 1.3 Avgrensinger

Analysen er avgrenset på følgende punkter:

1. **Prediksjon, ikke kausal analyse.** Prosjektet undersøker hvilke variabler som predikerer salget best, ikke hvorfor salget endrer seg. Kausale slutninger forutsetter eksperimentelt design og ligger utenfor prosjektets rammer.
2. **Ingen lageroptimalisering.** Rapporten dokumenterer ikke lageroptimalisering. Det krever kostnads- og volumparametere som ikke inngår i datasettet.
3. **Ingen makroøkonomiske faktorer.** Eksterne variabler som inflasjon, rente og konjunkturer er ikke inkludert. Datasettet gir ikke grunnlag for dette, og inkludering av slike variabler ville kreve egne datakilder.
4. **Én virksomhet og ett datasett.** Analysen begrenses til det tilgjengelige datasettet. Generalisering til andre virksomheter eller bransjer forutsetter eget datagrunnlag og ny validering.
5. **To modelltyper.** Modellvalget er begrenset til multippel lineær regresjon og Random Forest Regressor, i tråd med prosjektets faglige rammer og tilgjengelig treningsgrunnlag.

### 1.4 Antagelser

Analysen bygger på følgende eksplisitte antagelser:

1. **Representativitet.** Datasettet antas representativt for en realistisk dagligvarekjede med tanke på sesongmønstre, rabattbruk, regionfordeling og produktkategorier. *Konsekvens:* Funnene er gyldige innenfor dette caset, men ikke nødvendigvis overførbare til andre virksomheter eller reelle kjeder.
2. **Tidsmessig relevans.** Historiske mønstre fra 2022–2024 antas relevante for å predikere 2025. *Konsekvens:* Strukturelle brudd som betydelige prissjokk, atferdsendringer eller endringer i sortiment vil svekke prediksjonens gyldighet.
3. **Tilstrekkelig datakvalitet.** Datasettet antas å inneholde tilstrekkelig variasjon i nøkkeldimensjonene sesong, rabatt, region og produktkategori til å trene modellene. *Konsekvens:* Datasettet kan undervurdere virkelig støy og sjeldne hendelser sammenlignet med en faktisk driftssituasjon, noe som kan gi mer optimistiske målinger enn hva som er realistisk i produksjon.
4. **Testsett som fremtidig periode.** 2025-dataene er holdt helt utenfor trening og brukes som testperiode. *Konsekvens:* Evalueringen gir et realistisk bilde av prognosekvalitet under antakelsen om at 2025 ligner de foregående årene i mønster og struktur.

---

## 2 Litteratur

I salgsprognose og etterspørselspredikering er to metodetradisjoner spesielt relevante: klassisk statistisk regresjon og ensemble-basert maskinlæring. Begge er godt dokumenterte tilnærminger til prediktiv modellering i handels- og forretningskontekster, og dagligvare- og varehandelssektoren er et aktivt anvendelsesområde i forskningslitteraturen (Fildes et al., 2022).

Multippel lineær regresjon er en veletablert statistisk metode for å predikere en kontinuerlig utfallsvariabel fra flere forklaringsvariabler, og er et naturlig referansevalg fordi den er rask å estimere og gir tolkbare koeffisienter (James et al., 2021). Metoden bygger på flere antagelser – blant annet at residualene er normalfordelte og har konstant varians (homoskedastisitet), og at det ikke er perfekt multikollinearitet mellom forklaringsvariablene – og brudd på disse svekker tolkningsvaliditeten, men ikke nødvendigvis prediksjonskraften (James et al., 2021). Regresjonsbaserte tilnærminger har også vist seg nyttige spesifikt i dagligvarekontekst: Ulrich et al. (2021) bruker distribusjonell regresjon til å predikere daglig etterspørsel i netthandel med dagligvarer, og finner at regresjonsrammeverk som modellerer hele utfallsfordelingen – ikke bare gjennomsnittet – gir bedre beslutningsstøtte for lagerstyring.

Random Forest representerer en nyere og mer fleksibel tilnærming. Breiman (2001) introduserte metoden som et ensemble av beslutningstrær der bootstrap-aggregering og tilfeldig variabeluttrekk gjør trærne mindre korrelerte, slik at gjennomsnittet over trærne reduserer variansen sammenlignet med et enkelt tre. James et al. (2021) framhever at Random Forest håndterer ikke-lineære sammenhenger og samspill mellom variabler direkte, og at metoden gir en innebygd rangering av variabelviktighet (feature importance). I sammenlignende studier av etterspørselsprognoser i varehandel inngår Random Forest ofte som referansemodell: Mitra et al. (2022) sammenligner blant annet Random Forest, gradient boosting og nevrale nett for en flerkanals varehandelskjede og finner at tre-baserte ensemble-metoder gir lavere prognosefeil enn enklere baselinjer, særlig når etterspørselsmønsteret er sammensatt. Kang (2023) sammenligner nettopp lineær regresjon, Random Forest og gradient boosting på salgsdata fra et supermarked og finner at den lineære modellen underfitter, mens de tre-baserte modellene presterer best – men med liten innbyrdes margin.

Den empiriske litteraturen gir likevel ikke ett entydig svar på hvilken modellklasse som er best. Fildes et al. (2022) oppsummerer forskning og praksis innen varehandelsprognoser og påpeker at valg av metode avhenger sterkt av dataoppløsning, hierarkisk struktur og tilgang på forklaringsvariabler, og at enkle modeller ofte er overraskende konkurransedyktige på aggregert nivå. Spiliotis et al. (2022) studerer daglig etterspørsel på enkeltprodukt-nivå (SKU) i detaljhandel og viser at maskinlæring kan overgå statistiske metoder, men at fortrinnet er betinget av dataenes egenskaper og av hvordan modellene utnytter forklaringsvariabler. Makridakis et al. (2022) rapporterer fra M5-konkurransen, som baserte seg på daglige salgsdata fra varehandel, at gradient-boostede tremodeller systematisk slo både klassiske statistiske metoder og rene lineære modeller, men at gevinsten forutsatte rik feature-engineering og store datamengder. Samtidig viser Makridakis et al. (2018) at maskinlæring ikke automatisk er overlegen: på et bredt sett tidsrekker presterte enkle statistiske metoder bedre og krevde langt mindre beregning, et resultat senere arbeid nyanserer med at maskinlæringens fortrinn vokser med datamengden. Valget av evalueringsmetrikk påvirker også konklusjonen: RMSE og MAPE vektlegger henholdsvis absolutt og relativ feil ulikt, og MAPE er dessuten ustabil ved lave volum (Hyndman & Koehler, 2006), slik at de to målene ikke alltid peker på samme vinnermodell.

Forskningsgapet denne rapporten adresserer ligger i krysningen mellom to forhold. For det første er sammenlignende empirisk arbeid som isolerer nettopp multippel lineær regresjon mot Random Forest for daglige salgsprognoser i dagligvaresektoren fortsatt begrenset; mye av litteraturen vektlegger enten større modellpaneler (Mitra et al., 2022; Makridakis et al., 2022) eller rikere eksterne variabler (Ulrich et al., 2021; Carbonneau et al., 2008). For det andre er effekten av streng tidsbasert oppsplitting på sammenligningens utfall sjelden isolert (Cerqueira et al., 2020). Studien bidrar med en kontrollert sammenligning på ett datasett der trening, validering og test er strengt adskilt i tid, og hvor både samlede og segmentvise metrikker rapporteres.

---

## 3 Teori

Dette kapitlet gir det faglige grunnlaget for metodevalg, analyse og tolkning senere i rapporten. Notasjon: når en kolonne eller feature fra modellmatrisen refereres direkte, skrives navnet i inline kode, for eksempel `Discount`, `Region_North` eller `dayofmonth`. I Sammendrag og Abstract brukes vanlig prosa («rabatt», «discount», «kalendervariabler») for å holde oppsummeringene tilgjengelige for et bredere publikum. *Forklaringsvariabel* brukes som samlebegrep for alle input i modellene, mens *prediktor*, *signal* og *feature* opptrer som kontekstuelle synonymer der variasjonen understøtter lesbarheten.

### 3.1 Multippel lineær regresjon

Multippel lineær regresjon er en supervisert læringsmetode som modellerer forholdet mellom en avhengig variabel og to eller flere uavhengige forklaringsvariabler. Modellen uttrykkes som i ligning (3.1):

$$\hat{y} = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_n x_n \tag{3.1}$$

der $\hat{y}$ er predikert verdi, $\beta_0$ er konstantleddet og $\beta_1, \ldots, \beta_n$ er regresjonskoeffisientene som uttrykker endringen i $\hat{y}$ per enhet endring i den tilhørende forklaringsvariabelen, alt annet likt (James et al., 2021).

Koeffisientene estimeres med **Ordinary Least Squares (OLS)**, som minimerer summen av kvadrerte residualer i ligning (3.2):

$$\sum_{i=1}^{n}(y_i - \hat{y}_i)^2 \tag{3.2}$$

For at estimatene skal være gyldige krever metoden at fem antagelser er oppfylt (James et al., 2021): (1) linearitet mellom avhengig og uavhengige variabler, (2) uavhengige residualer, (3) homoskedastisitet — konstant varians i residualene på tvers av alle prediktornivåer, (4) normalfordelte residualer, og (5) ingen perfekt **multikollinearitet** mellom forklaringsvariablene. Multikollinearitet er særlig relevant i dette prosjektet fordi one-hot-kodede dummyvariabler kan skape høy innbyrdes korrelasjon og gjøre tolkning av enkeltkoeffisienter usikker.

Konsekvensene av brudd på antagelsene er ulike og bør holdes fra hverandre. Brudd på linearitet — for eksempel en utelatt ikke-lineær sammenheng — gir systematisk skjevhet (bias) i selve prediksjonene. Heteroskedastisitet og avhengige residualer gir derimot først og fremst feilestimerte standardfeil og dermed upålitelig statistisk inferens, uten nødvendigvis å ødelegge punktprediksjonen. Multikollinearitet blåser opp variansen til koeffisientestimatene, slik at fortegn og størrelse på enkeltkoeffisienter blir ustabile selv når modellens samlede prediksjonskraft er god.

Lineær regresjon brukes her som benchmarkmodell nettopp fordi den er tolkbar — koeffisientene gir direkte innsikt i retning og størrelse av variabeleffekter — og fordi enkle modeller ofte er overraskende konkurransedyktige i varehandelsprognoser (Fildes et al., 2022). Dens prinsipielle begrensning er at den forutsetter et i hovedsak lineært og additivt mønster i dataene, slik at betingede samspill mellom variabler ikke fanges opp uten at de spesifiseres eksplisitt.

### 3.2 Random Forest Regressor

Random Forest er en ensemble-metode basert på et sett med beslutningstrær som samlet gir mer stabile prediksjoner enn ett enkelt tre (Breiman, 2001). Algoritmen hviler på to grunnprinsipper:

**Bootstrap aggregation (bagging):** Hvert tre trenes på et tilfeldig utvalg med tilbakelegging fra treningsdataene. Dermed ser hvert tre en litt annerledes versjon av datasettet, og trærne korrelerer mindre med hverandre (Breiman, 2001).

**Feature randomness:** Ved hver splittingsbeslutning i et tre velges kun et tilfeldig subsett av features til vurdering — ikke alle tilgjengelige variabler. Dette reduserer korrelasjon mellom trærne ytterligere og gjør ensemblet mer robust mot overfitting (Breiman, 2001).

For regresjonsoppgaver er den endelige prediksjonen gjennomsnittet av alle trærnes individuelle prediksjoner. Dette reduserer overordnet varians og demper effekten av støy i enkelttrær.

Mekanismen kan forstås gjennom **bias–varians-avveiingen**. Et enkelt, dypt beslutningstre har lav bias, men høy varians: det tilpasser seg treningsdataene tett og blir ustabilt mot små endringer i datagrunnlaget. Ved å gjennomsnitte mange avkorrelerte trær reduserer Random Forest variansen kraftig uten å øke biasen tilsvarende, slik at forventet prediksjonsfeil på nye data går ned. Fordi hvert tre trenes på et bootstrap-utvalg, kan de observasjonene som ikke inngår i utvalget (*out-of-bag*) brukes som et innebygd valideringsmål uten et separat hold-out-sett. I motsetning til lineær regresjon modellerer trærne ikke-lineære terskler og betingede samspill mellom variabler direkte, fordi hver splitt deler dataene lokalt; dette er en hovedgrunn til at tre-baserte ensembler ofte gir lavere prognosefeil enn lineære modeller når etterspørselsmønsteret er sammensatt (Mitra et al., 2022; Makridakis et al., 2022).

**Feature importance** beregnes som gjennomsnittlig reduksjon i MSE (Mean Decrease in Impurity) på tvers av alle trær og splittinger for en gitt variabel. En variabel som konsekvent reduserer prediksjonsfeilen i mange trær, rangeres høyt (Breiman, 2001).

Modellens oppførsel styres av hyperparametere som `n_estimators` (antall trær), `max_depth` (maksimal dybde per tre), `min_samples_leaf` (minste antall observasjoner i et løvnode) og `max_features` (antall features vurdert per split). Disse tilpasses gjennom hyperparametertuning mot et valideringssett.

### 3.3 Evalueringsmetrikker

To metrikker brukes for å evaluere prognosemodellene i dette prosjektet.

**RMSE (Root Mean Squared Error)** måler den gjennomsnittlige størrelsen på prediksjonsfeilen i samme enhet som utfallsvariabelen, vist i ligning (3.3):

$$\text{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2} \tag{3.3}$$

Kvadreringen medfører at store avvik vektes tyngre enn små. RMSE brukes som primær metrikk i dette prosjektet fordi absolutt presisjon — å treffe riktig salgsvolum — er det mest relevante kravet for innkjøp og lagerstyring.

**MAPE (Mean Absolute Percentage Error)** måler det gjennomsnittlige prosentvise avviket, vist i ligning (3.4):

$$\text{MAPE} = \frac{1}{n}\sum_{i=1}^{n}\left|\frac{y_i - \hat{y}_i}{y_i}\right| \times 100 \tag{3.4}$$

MAPE er skalanøytral og enklere å kommunisere, men er ustabil når faktiske verdier er nær null (divisjon mot null), og overvekter dermed observasjoner med lavt volum. Metrikken brukes som sekundær metrikk. I prognosekonkurranser som M5 erstattes MAPE ofte av skalerte feilmål nettopp for å unngå denne ustabiliteten ved lave volum (Makridakis et al., 2022).

Når RMSE og MAPE peker på ulike vinnere, skyldes det at en modell kan ha lavt absolutt avvik på store volumer (lavt RMSE) uten å treffe proporsjonalt godt på små volumer (høy MAPE). Begge metrikkene (ligning (3.3) og (3.4)) er derfor nødvendige for å forstå modelloppførselen på tvers av ulike salgsnivåer (Hyndman & Koehler, 2006).

### 3.4 Feature engineering og dataoppsett

**Feature engineering** er prosessen med å utlede nye variabler fra rådata for å gjøre mønstre tilgjengelige for modellene. I dette prosjektet er kalendervariablene `year`, `month`, `quarter`, `weekofyear`, `dayofweek`, `dayofmonth` og `is_weekend` avledet fra den opprinnelige datovariabelen. Disse variablene fanger opp sesong-, uke- og kvartalsmønstre som ikke direkte kan leses fra en rådate (Fildes et al., 2022).

**One-hot encoding** konverterer kategoriske variabler — som Region, Category og Sub-Category — til binære dummyvariabler. For lineær regresjon er dette nødvendig fordi modellen krever numerisk input. Random Forest bruker her samme kodede matrise for konsistens i sammenligning (James et al., 2021).

**Data leakage** oppstår når variabler som ikke ville vært tilgjengelige på prediksjonstidspunktet inkluderes i modellen. I dette prosjektet er `Profit` ekskludert fordi den kun er kjent etter at salget er gjennomført.

**Tidsbasert oppsplitting** er valgt fremfor tilfeldig oppsplitting. Treningsdata er 2022–2024 og testdata er 2025. Tilfeldig oppsplitting ville tillate fremtidige observasjoner å inngå i treningen, noe som gir kunstig god ytelse og ikke reflekterer reell prediksjon fremover i tid; tidsbasert evaluering anbefales nettopp for å unngå slike for optimistiske ytelsesestimater (Cerqueira et al., 2020). I hyperparametertuningen av Random Forest brukes 2024 i tillegg som intern valideringsperiode, mens lineær regresjon beholdes med det fulle treningsgrunnlaget.

---

## 4 Casebeskrivelse

### 4.1 Dagligvare og beslutningssituasjonen

Dagligvare er en dagligvarekjede som opererer på tvers av fem regioner: West, East, Central, South og North. Kjeden fører syv produktkategorier – Snacks, Eggs/Meat/Fish, Fruits & Veggies, Bakery, Beverages, Food Grains og Oil & Masala – fordelt på 23 subkategorier. Datasettet som danner analysegrunnlaget inneholder 9 994 daglige salgstransaksjoner fra perioden 2022–2025, fordelt på 24 byer.

Dagligvares operative planlegging er avhengig av pålitelige etterspørselsprognoser. Salget varierer med sesong, rabatter og regionale forhold, og konsekvensene av dårlige prognoser er direkte synlige i driften: for høye bestillinger gir svinn og bundet kapital, mens for lave bestillinger fører til utsolgte varer og tapte inntekter. Behovet for mer presise prognoser er dermed sentralt for innkjøp, lager, kampanjevurdering og ressursplanlegging.

Figur 4.1 viser gjennomsnittlig salgsnivå per produktkategori. Eggs, Meat & Fish skiller seg ut med det høyeste gjennomsnittlige salgsnivået i datasettet.

<div align="center">
  <img src="../006 analysis/aktiviteter/07_eksplorativ_analyse_og_visualisering/fig_sales_per_category.png" alt="Gjennomsnittlig salgsnivå per produktkategori" width="80%">
  <p align="center"><small><i>Figur 4.1 Gjennomsnittlig salgsnivå per produktkategori.</i></small></p>
</div>

### 4.2 Historisk salgsutvikling

Gjennomsnittlig daglig salg for hele perioden 2022–2025 er 1 497 med et spenn fra 500 til 2 500 og standardavvik på 578. Salgsnivået er stabilt over tid: gjennomsnittsnivået i treningsperioden 2022–2024 er 1 493, mot 1 503 i testperioden 2025. Ingen tydelig veksttrend er synlig i perioden – nivået holder seg relativt konstant med lokal variabilitet.

Figur 4.2 viser salgsforløpet over tid med trenings- og testperioden markert.

<div align="center">
  <img src="../006 analysis/aktiviteter/07_eksplorativ_analyse_og_visualisering/fig_sales_over_tid_train_test.png" alt="Salgsutvikling over tid, trening og test" width="80%">
  <p align="center"><small><i>Figur 4.2 Daglig salg over perioden 2022–2025, med treningsperiode (2022–2024) og testperiode (2025) vist.</i></small></p>
</div>

### 4.3 Sesongmønster i salget

Månedsmønsteret viser at oktober er måneden med det høyeste gjennomsnittlige salgsnivået, mens juni er den svakeste måneden. Mønsteret er konsistent mellom trenings- og testperioden, noe som tyder på et stabilt sesongmønster i datasettet. Fjerde kvartal fremstår samlet som den sterkeste perioden, mens andre og tredje kvartal er relativt svakere.

Figur 4.3 viser gjennomsnittlig salg per måned for henholdsvis trenings- og testperioden.

<div align="center">
  <img src="../006 analysis/aktiviteter/07_eksplorativ_analyse_og_visualisering/fig_sales_per_month_split.png" alt="Gjennomsnittlig salg per måned" width="80%">
  <p align="center"><small><i>Figur 4.3 Gjennomsnittlig daglig salg per måned for treningsperioden (2022–2024) og testperioden (2025).</i></small></p>
</div>

### 4.4 Utfordringer dårlige prognoser medfører i bedriften

For Dagligvare forsterkes planleggingsrisikoen av et sortiment som spenner fra ferske varer med kort holdbarhet til tørrvarer med lengre holdbarhetsperiode. Overskuddsbestillinger fører til direkte svinn og bundet kapital – konsekvenser som er særlig kostbare i kategorier som Eggs, Meat & Fish og Fruits & Veggies. Underestimering gir tomme hyller, tapte inntekter og risiko for å svekke kundelojaliteten.

Sesongvariasjonen i Figur 4.3 viser at salget svinger markant gjennom året – med topp i oktober og bunnpunkt i juni. Kombinert med rabattavhengighet gjør dette at enkle tommelfingerregler for innkjøp gir dårlige resultater i perioder med høy kampanjeaktivitet eller sesongtopper.

Nøyaktige etterspørselsprognoser for 2025 kan gi Dagligvare et bedre grunnlag for innkjøpsplanlegging og lagerstyring, støtte vurderingen av kampanjeeffekter og bidra til mer presis ressursplanlegging i perioder med høy og lav etterspørsel.

---

## 5 Metode og data

### 5.1 Metode

Prosjektet er en kvantitativ, prediktiv studie der historiske salgsdata fra én dagligvarekjede brukes til å bygge og evaluere prognosemodeller. Datagrunnlaget er ikke samlet inn, men stilt til disposisjon som en del av prosjektets faglige rammer. Problemstillingen besvares gjennom en trinnvis analytisk prosess: datasettet ble renset og gjort klart for modellering, deretter ble relevante variabler valgt og nye kalendervariabler utledet, og til slutt ble datasettet delt i en treningsperiode og en testperiode basert på tid.

Lineær regresjon ble valgt som benchmark-modell fordi metoden er tolkbar og gir et stabilt sammenligningsgrunnlag. Random Forest Regressor ble valgt som alternativmodell fordi den kan fange opp ikke-lineære mønstre og gir en naturlig rangering av variablenes prediksjonsverdi. Random Forest ble i tillegg tunet ved å trene på 2022–2023 og validere på 2024, slik at hyperparametere ble valgt uten å bruke testdataene. Alle tre modellspor – lineær regresjon, Random Forest baseline og tuned Random Forest – ble evaluert på 2025-data.

Evalueringen benytter RMSE som primær metrikk fordi absolutt presisjon er mest relevant for innkjøp og lagerstyring, og MAPE som sekundær metrikk for å gi et relativt bilde av prognosefeilen (jf. ligning (3.3) og (3.4) i kap. 3.3). Modellene sammenlignes samlet for hele 2025 og per måned, og resultatene tolkes videre etter kvartal, rabattnivå, region og salgsnivå for å gi praktisk beslutningsstøtte til Dagligvare.

### 5.2 Data

Datagrunnlaget er filen `Dagligvare_Dataset.csv`, som inneholder 9 994 daglige salgstransaksjoner fra en dagligvarekjede. Rådata dekker opprinnelig perioden 2015–2018 og er remappet med en syvårig kalenderforskyvning til prosjektperioden 2022–2025. Datasettet har 11 råkolonner og ingen manglende verdier eller dubletter. To ulike datoformater i kildedata – 4 042 rader med `dd-mm-yyyy` og 5 952 rader med `mm/dd/yyyy` – ble standardisert til ISO-format under rensingen.

Figur 5.1 viser fordelingen av datatyper i rådatasettet og underbygger valget av forbehandling og feature engineering.

<div align="center">
  <img src="../006 analysis/aktiviteter/01_dataforstaelse_og_variabler/fig_datatype_fordeling.png" alt="Fordeling av datatyper i rådatasettet" width="80%">
  <p align="center"><small><i>Figur 5.1 Fordeling av datatyper i rådatasettet. Fordelingen viser hvor mange kolonner som er numeriske, kategoriske og datobaserte, og underbygger valg av forbehandling og feature engineering.</i></small></p>
</div>

Målvariabelen er `Sales` (heltall, spenn 500–2 500). Forklaringsvariablene som inngår i modellene er `Discount` (desimaltall, 0,10–0,35) og de kategoriske variablene `Category`, `Sub Category`, `City` og `Region`. Fra `Order Date` er det i tillegg utledet sju kalendervariabler: `year`, `month`, `quarter`, `weekofyear`, `dayofweek`, `dayofmonth` og `is_weekend`. Fire variabler ble ekskludert: `Profit` fordi den er en lekkasjevariabel som kun er kjent etter gjennomført salg, `State` fordi kolonnen er konstant i datasettet, og `Order ID` og `Customer Name` fordi de ikke har generaliserbar prediksjonsverdi. Kategoriske variabler ble one-hot-encoded til binære dummyvariabler, slik at den endelige modellmatrisen inneholder 67 features.

Tabell 5.1 oppsummerer de 11 kolonnene i rådatasettet med datatype, manglende andel og anbefaling for videre bruk.

| Variabel | Datatype | Manglende % | Unike | Anbefaling | Begrunnelse |
| --- | --- | --- | --- | --- | --- |
| Sales | int64 | 0,0 | 1 989 | target | Målvariabel for prognose. |
| Category | str | 0,0 | 7 | inkluder | Kategorisk variabel med håndterbar kardinalitet. |
| City | str | 0,0 | 24 | inkluder | Kategorisk variabel med håndterbar kardinalitet. |
| Discount | float64 | 0,0 | 26 | inkluder | Numerisk variabel egner seg direkte for modellering. |
| Region | str | 0,0 | 5 | inkluder | Kategorisk variabel med håndterbar kardinalitet. |
| State | str | 0,0 | 1 | ekskluder | Kolonnen er konstant i datasettet og gir ingen forklaringskraft. |
| Sub Category | str | 0,0 | 23 | inkluder | Kategorisk variabel med håndterbar kardinalitet. |
| Order Date | str | 0,0 | 1 236 | vurder | Middels/høy kardinalitet, vurder koding og nytte. |
| Profit | float64 | 0,0 | 8 380 | vurder | Kan være informativ, men bør sjekkes for lekkasje før modellering. |
| Customer Name | str | 0,0 | 50 | ekskluder | Navn-kolonne har høy kardinalitet og høy risiko for overtilpasning. |
| Order ID | str | 0,0 | 9 994 | ekskluder | ID-variabel gir vanligvis lite generaliserbar prediksjonsverdi. |

<p align="center"><small><i>Tabell 5.1 Variabeloversikt med datatype, manglende andel og anbefaling for videre bruk.</i></small></p>

Tabell 5.2 dokumenterer feature engineering-oppsettet: hvilke input-kolonner som beholdes, transformeres eller ekskluderes, og hvilke output-kolonner de gir.

| Input-kolonne | Handling | Output-kolonne | Begrunnelse |
| --- | --- | --- | --- |
| Sales | behold | Sales | Målvariabel for prognose. |
| Discount | behold | Discount | Numerisk forklaringsvariabel. |
| Category | behold | Category | Kategorisk feature med håndterbar kardinalitet. |
| Sub Category | behold | Sub Category | Kategorisk feature med håndterbar kardinalitet. |
| City | behold | City | Kategorisk feature med håndterbar kardinalitet. |
| Region | behold | Region | Kategorisk feature med håndterbar kardinalitet. |
| Order Date | behold | Order Date | Beholdes for sporbarhet og tidsbasert splitt. |
| Order Date | transformer | year | Utledet kalenderår etter remapping. |
| Order Date | transformer | month | Utledet måned. |
| Order Date | transformer | quarter | Utledet kvartal. |
| Order Date | transformer | weekofyear | Utledet uke i året. |
| Order Date | transformer | dayofweek | Utledet ukedag. |
| Order Date | transformer | dayofmonth | Utledet dag i måneden. |
| Order Date | transformer | is_weekend | Indikator for helg. |
| Order ID | ekskluder | – | ID-kolonne uten generaliserbar prediksjonsverdi. |
| Customer Name | ekskluder | – | Navn-kolonne med høy risiko for overtilpasning. |
| Profit | ekskluder | – | Ekskludert som potensiell lekkasjevariabel. |
| State | ekskluder | – | Kolonnen er konstant i datasettet og gir ingen forklaringskraft. |

<p align="center"><small><i>Tabell 5.2 Feature engineering-oppsett: input-kolonne, handling og resulterende output-kolonne med begrunnelse.</i></small></p>

Tabell 5.3 dokumenterer datarensingen fra 9 994 rader inn til 9 994 rader ut, uten at rader ble fjernet eller manglende verdier oppdaget.

| Målepunkt | Verdi | Kommentar |
| --- | --- | --- |
| antall_rader_inn | 9 994 | Observasjoner i rådata |
| antall_kolonner_inn | 11 | Variabler i rådata |
| manglende_verdier_inn | 0 | Totalt manglende i rådata |
| dubletter_inn | 0 | Eksakte dublettrader i rådata |
| datoformat_dd_mm_yyyy | 4 042 | Tolket fra verdier med bindestrek |
| datoformat_mm_dd_yyyy | 5 952 | Tolket fra verdier med skråstrek |
| datoformat_annet | 0 | Verdier uten kjent mønster |
| ugyldige_datoer_etter_tolkning | 0 | Datoer som ikke lot seg parse |
| opprinnelig_periode_start | 2015-01-02 | Tidligste dato i original dataserie |
| opprinnelig_periode_slutt | 2018-12-30 | Siste dato i original dataserie |
| år_forskyvning | 7 | Kalenderforskyvning brukt for prosjektets arbeidsgrunnlag |
| prosjekt_periode_start | 2022-01-02 | Tidligste dato etter remapping |
| prosjekt_periode_slutt | 2025-12-30 | Siste dato etter remapping |
| rader_fjernet_manglende_kritisk_felt | 0 | Rader fjernet etter kontroll av dato og numeriske nøkkelfelt |
| dubletter_fjernet | 0 | Fjernet etter standardisering |
| antall_rader_ut | 9 994 | Observasjoner i renset datasett |
| manglende_verdier_ut | 0 | Totalt manglende etter rens |
| dubletter_ut | 0 | Eksakte dublettrader etter rens |

<p align="center"><small><i>Tabell 5.3 Datarensing – målepunkter, verdier og kommentarer som dokumenterer kvalitetskontrollen før modellering.</i></small></p>

Fordelingen av kategoriske variabler viser at West-regionen utgjør 32 % av observasjonene, East 28 %, Central 23 % og South 16 %. North-regionen er representert med bare én observasjon og benyttes ikke som separat analysesegment. Produktkategoriene er jevnt fordelt med mellom 14 og 15 % av observasjonene hver, noe som betyr at ingen enkelt kategori dominerer datasettet.

Datasettet er delt tidsmessig slik at treningsdata dekker 2022–2024 og testdata dekker 2025. Tilfeldig splitt ble ikke brukt, fordi det ville tillate fremtidige observasjoner å inngå i treningen og dermed gi kunstig god ytelse. Det gjennomsnittlige salgsnivået er stabilt mellom periodene (1 493 i treningsdata og 1 503 i testdata), noe som styrker antakelsen om at historiske mønstre er overførbare til 2025. Figur 5.2 viser fordelingen av daglige salgsverdier i trenings- og testperioden.

<div align="center">
  <img src="../006 analysis/aktiviteter/07_eksplorativ_analyse_og_visualisering/fig_sales_fordeling_train_test.png" alt="Fordeling av daglige salgsverdier i trenings- og testperioden" width="80%">
  <p align="center"><small><i>Figur 5.2 Fordeling av daglige salgsverdier i trenings- og testperioden. Overlappet i fordelingene tyder på at målvariabelen er stabil mellom periodene.</i></small></p>
</div>

Tabell 5.4 oppsummerer antallsfordelingen mellom trenings- og testperioden.

| Delmengde | År | Antall rader | Andel |
| --- | --- | --- | --- |
| Treningsdata | 2022–2024 | 6 682 | ~67 % |
| Testdata | 2025 | 3 312 | ~33 % |

<p align="center"><small><i>Tabell 5.4 Fordeling av trenings- og testdata etter tidsmessig splitt.</i></small></p>

### 5.3 Validitet, reliabilitet og etiske hensyn

**Validitet.** Intern validitet styrkes gjennom tidsbasert oppsplitting (2022–2024 trening, 2025 test) som hindrer datalekkasje, og gjennom adskilt valideringsperiode (2024) for hyperparametertuning av Random Forest. Ekstern validitet er begrenset av at studien bygger på ett datasett fra én virksomhet, og generalisering til reelle dagligvarekjeder krever ny validering (jf. §1.3 og §9.5).

**Reliabilitet.** Analysen er organisert som aktivitetsbaserte skript med faste seeds for Random Forest og uten ad-hoc-manipulering av treningsgrunnlaget mellom aktiviteter. Pipeline fra rådata til endelige metrikker er reproduserbar.

**Etiske hensyn.** Datasettet inneholder ingen personopplysninger eller annen sensitiv informasjon. Studien reiser dermed ikke personvern- eller forskningsetiske problemstillinger. Bruken av kunstig intelligens som verktøy i analyse- og rapportarbeidet er åpen og dokumentert i prosjektets endringslogg og obligatoriske egenerklæring.

---

## 6 Modellering

Prosjektet evaluerer tre modellspor for å predikere daglig salg i 2025. Benchmark-modellen er en multippel lineær regresjon som gir et tolkbart sammenligningsgrunnlag. Random Forest inngår i to varianter: en baseline med standardparametere som viser hva en utuned ensemble-modell leverer på det samme datagrunnlaget, og en tuned variant der hyperparametere er valgt gjennom et strukturert søk. Sammenstillingen gir både et grunnlag for å måle gevinsten av tuning og et tolkbart referansepunkt som er robust mot overfitting.

Tabell 6.1 oppsummerer de tre modellsporene med antall features, treningsrader, sentrale hyperparametre og rolle i prosjektet.

| Modellrolle | Algoritme | Treningsrader | Features | Sentrale hyperparametre | Rolle i prosjektet |
| --- | --- | --- | --- | --- | --- |
| benchmark lineær | LinearRegression | 6 682 | 67 | `fit_intercept=True`, ingen regularisering | Tolkbar benchmark med eksplisitt koeffisientretning. |
| baseline RF | RandomForestRegressor | 6 682 | 67 | `n_estimators=200`, `max_depth=None`, `min_samples_leaf=1`, `max_features=1.0` | RF-referanse uten tuning, for stabilitetssjekk mot tunet modell. |
| tuned RF | RandomForestRegressor | 6 682 | 67 | `n_estimators=400`, `max_depth=10`, `min_samples_leaf=4`, `max_features="sqrt"` | Anbefalt operativ modell etter tuning på 2024-validering. |

<p align="center"><small><i>Tabell 6.1 Oversikt over de tre modellsporene: antall features, treningsrader, sentrale hyperparametre og rolle i prosjektet.</i></small></p>

Den multiple lineære regresjonen trenes som `LinearRegression` med `fit_intercept=True` og uten regularisering eller skalering. Modellen estimeres med OLS (jf. ligning (3.1) og (3.2)) på 6 682 rader og 67 features – det vil si alle kalendervariabler, `Discount` og de one-hot-kodede kategoriske variablene. Estimert konstantledd er $-3193{,}55$. Modellen er tolkbar gjennom sine koeffisienter, men forutsetter at salget kan beskrives som en lineær kombinasjon av forklaringsvariablene, og den har ingen mekanisme for å fange opp interaksjoner eller ikke-lineære effekter utover de som eksplisitt er kodet inn.

Random Forest Regressor trenes på samme treningsmatrise. Baselinen bruker standardkonfigurasjonen `n_estimators=200`, `max_depth=None`, `min_samples_leaf=1`, `max_features=1.0` (dvs. at alle 67 features vurderes ved hver split), `bootstrap=True` og `random_state=42`, jf. bagging og feature randomness i kap. 3.2. Den tunede varianten bygger på et rutenettsøk der hver kandidat trenes på 2022–2023 (4 095 rader) og valideres på 2024 (2 587 rader). 2025-data inngår ikke i modellutvelgelsen – denne tidsmessige isolasjonen forhindrer datalekkasje mellom tuning og evaluering (jf. kap. 3.4 og 5.2). Vinnerkonfigurasjonen ble `n_estimators=400`, `max_depth=10`, `min_samples_leaf=4` og `max_features='sqrt'` (som gir $\lfloor\sqrt{67}\rfloor = 8$ features per split), valgt med validerings-RMSE som primærkriterium. Vinnerkandidaten oppnådde validerings-RMSE $577{,}27$ og validerings-MAPE $43{,}56\%$, mot baseline-kandidatens $590{,}30$ og $44{,}22\%$ på samme valideringssett. Den tunede modellen retrenes deretter på hele treningsperioden (2022–2024) før evaluering på 2025. Alle tre modellene genererer prognoser på testperioden 2025 (3 312 rader), og det er disse prognosene som danner grunnlaget for analyse og resultat i de neste kapitlene.

Tabell 6.2 viser de fem beste parameterkombinasjonene fra rutenettsøket, sortert etter RMSE på 2024-valideringen og med delta mot baseline-kandidaten.

| Kandidat | n_estimators | max_depth | min_samples_leaf | max_features | RMSE validering | MAPE validering (%) | Delta RMSE vs. baseline |
| --- | --- | --- | --- | --- | --- | --- | --- |
| rf_tune_30 (vinner) | 400 | 10 | 4 | sqrt | 577,27 | 43,56 | −13,04 |
| rf_tune_28 | 400 | 10 | 2 | sqrt | 577,29 | 43,57 | −13,02 |
| rf_tune_10 | 200 | 10 | 2 | sqrt | 577,36 | 43,58 | −12,94 |
| rf_tune_26 | 400 | 10 | 1 | sqrt | 577,65 | 43,60 | −12,65 |
| rf_tune_12 | 200 | 10 | 4 | sqrt | 577,81 | 43,61 | −12,50 |

<p align="center"><small><i>Tabell 6.2 Topp 5 parameterkombinasjoner fra tuning av Random Forest, sortert etter RMSE på 2024-valideringen.</i></small></p>

---

## 7 Resultat

Tabell 7.1 oppsummerer den samlede ytelsen på 2025 for de tre modellsporene. Tuned Random Forest har lavest RMSE og MAPE, mens baseline Random Forest er svakest på RMSE og benchmark lineær er svakest på MAPE.

| Modell | RMSE | MAPE |
| --- | --- | --- |
| Benchmark lineær | 580,39 | 44,18 % |
| Baseline Random Forest | 589,28 | 44,12 % |
| Tuned Random Forest | 578,26 | 43,97 % |

<p align="center"><small><i>Tabell 7.1 Samlet prognoseytelse på 2025 (3 312 observasjoner).</i></small></p>

Figur 7.1 visualiserer den samlede ytelsen per modell.

<div align="center">
  <img src="../006 analysis/aktiviteter/13_rmse_og_mape/fig_rmse_mape_samlet.png" alt="Samlet RMSE og MAPE for 2025" width="80%">
  <p align="center"><small><i>Figur 7.1 Samlet RMSE og MAPE for benchmark lineær, Random Forest baseline og tuned Random Forest i 2025. Tuned Random Forest har lavest RMSE, mens MAPE er tettere fordelt mellom modellene.</i></small></p>
</div>

Tabell 7.2 viser hvor mange av de tolv månedene i 2025 hver modell vinner på henholdsvis RMSE og MAPE.

| Modell | RMSE-vinner (av 12) | MAPE-vinner (av 12) |
| --- | --- | --- |
| Benchmark lineær | 1 | 3 |
| Baseline Random Forest | 0 | 6 |
| Tuned Random Forest | 11 | 3 |

<p align="center"><small><i>Tabell 7.2 Månedlig vinnertelling per metrikk i 2025.</i></small></p>

\FloatBarrier

Tabell 7.3 viser de ti variablene med høyest feature importance i den tunede Random Forest-modellen, gruppert etter variabelgruppe.

| Rang | Variabel | Gruppe | Importance |
| --- | --- | --- | --- |
| 1 | Discount | Pris/kampanje | 11,48 % |
| 2 | dayofmonth | Kalender | 11,35 % |
| 3 | weekofyear | Kalender | 10,40 % |
| 4 | month | Kalender | 6,74 % |
| 5 | dayofweek | Kalender | 6,52 % |
| 6 | year | Kalender | 4,02 % |
| 7 | quarter | Kalender | 2,95 % |
| 8 | Region_East | Region | 2,04 % |
| 9 | Region_West | Region | 1,91 % |
| 10 | Region_Central | Region | 1,84 % |

<p align="center"><small><i>Tabell 7.3 Topp 10 feature importance for tuned Random Forest.</i></small></p>

\clearpage

Figur 7.2 visualiserer topp 10-rangeringen som horisontalt søyleplot.

<div align="center">
  <img src="../006 analysis/aktiviteter/15_viktige_variabler/fig_feature_importance_tuned_top10.png" alt="Topp 10 feature importance for tuned Random Forest" width="80%">
  <p align="center"><small><i>Figur 7.2 Topp 10 feature importance for tuned Random Forest. Variablene er rangert etter normalisert viktighet og viser hvilke signaler modellen faktisk vektlegger.</i></small></p>
</div>

Figur 7.3 aggregerer samme topp 10 etter variabelgruppe og viser hvilke typer signaler som dominerer prediksjonen.

<div align="center">
  <img src="../006 analysis/aktiviteter/15_viktige_variabler/fig_variabelgrupper_tuned_top10.png" alt="Variabelgrupper i topp 10 for tuned Random Forest" width="80%">
  <p align="center"><small><i>Figur 7.3 Samlet feature importance per variabelgruppe i topp 10 for tuned Random Forest. Figuren oppsummerer hvilke grupper av signaler (kalender, pris/kampanje, region) som dominerer modellens prediksjon.</i></small></p>
</div>

Tabell 7.4 oppsummerer vinnermodellen per segment på RMSE og MAPE, fordelt på kvartal, rabattband, region og salgsnivå.

| Segmentdimensjon | Verdi | RMSE-vinner | MAPE-vinner |
| --- | --- | --- | --- |
| Kvartal | Q1 | Tuned RF | Benchmark lineær |
| Kvartal | Q2 | Tuned RF | Baseline RF |
| Kvartal | Q3 | Tuned RF | Tuned RF |
| Kvartal | Q4 | Tuned RF | Benchmark lineær |
| Rabatt | Lav | Tuned RF | Tuned RF |
| Rabatt | Middels | Tuned RF | Tuned RF |
| Rabatt | Høy | Tuned RF | Baseline RF |
| Region | Central | Tuned RF | Benchmark lineær |
| Region | East | Tuned RF | Tuned RF |
| Region | South | Tuned RF | Tuned RF |
| Region | West | Tuned RF | Baseline RF |
| Salgsnivå | Lavt salg | Tuned RF | Baseline RF |
| Salgsnivå | Middels salg | Tuned RF | Tuned RF |
| Salgsnivå | Høyt salg | Benchmark lineær | Benchmark lineær |

<p align="center"><small><i>Tabell 7.4 Vinnermodell per segment på RMSE og MAPE.</i></small></p>

---

## 8 Analyse

Samlet for 2025 leverer den tunede Random Forest-modellen både lavest RMSE og lavest MAPE (jf. Tabell 7.1), marginalt foran benchmark lineær og tydeligere foran baseline Random Forest. Gapet mellom modellene er lite i absolutt forstand – tuned Random Forest forbedrer RMSE med omtrent $11$ enheter sammenlignet med baseline Random Forest og $2$ enheter sammenlignet med benchmark lineær. Tuningeffekten tolkes som en kombinasjon av dybdebegrensningen (`max_depth=10`) og redusert `max_features`, som demper variansen i de enkelte trærne og gir mer stabile ensemble-prediksjoner på nye data (jf. kap. 3.2).

Månedsnivået nyanserer bildet vesentlig (jf. Tabell 8.1). Tuned Random Forest vinner RMSE i 11 av 12 måneder, men vinner MAPE i bare 3 måneder. Baseline Random Forest vinner ikke en eneste måned på RMSE, men vinner MAPE i 6 av 12 måneder. RMSE og MAPE peker på samme vinner bare i juli og september. Mønsteret kan forklares med at absolutt feil og prosentfeil vekter observasjoner ulikt: RMSE straffer store avvik hardt og favoriserer dermed modellen som er mest treffsikker på de største salgsmålene, mens MAPE er mer sensitiv i måneder med mange lavvolumrader der små avvik gir utslag i høye prosenttall.

Tabell 8.1 viser eksakte månedlige RMSE- og MAPE-verdier per modell, med RMSE og MAPE gruppert under hver modell.

<div align="center" style="font-size:0.8em">

<table>
  <thead>
    <tr>
      <th rowspan="2">Måned</th>
      <th colspan="2">Benchmark lineær</th>
      <th colspan="2">Baseline RF</th>
      <th colspan="2">Tuned RF</th>
    </tr>
    <tr>
      <th>RMSE</th><th>MAPE&nbsp;(%)</th>
      <th>RMSE</th><th>MAPE&nbsp;(%)</th>
      <th>RMSE</th><th>MAPE&nbsp;(%)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>2025-01</td><td>586,09</td><td>46,62</td><td>597,82</td><td>46,51</td><td>585,73</td><td>46,52</td></tr>
    <tr><td>2025-02</td><td>577,96</td><td>42,50</td><td>584,01</td><td>42,19</td><td>576,74</td><td>42,72</td></tr>
    <tr><td>2025-03</td><td>552,52</td><td>42,14</td><td>565,11</td><td>42,86</td><td>550,33</td><td>42,30</td></tr>
    <tr><td>2025-04</td><td>581,28</td><td>44,76</td><td>576,18</td><td>43,04</td><td>575,63</td><td>43,85</td></tr>
    <tr><td>2025-05</td><td>591,70</td><td>45,46</td><td>594,57</td><td>44,36</td><td>589,74</td><td>45,00</td></tr>
    <tr><td>2025-06</td><td>560,16</td><td>43,81</td><td>556,89</td><td>41,87</td><td>552,25</td><td>42,79</td></tr>
    <tr><td>2025-07</td><td>569,61</td><td>42,90</td><td>582,87</td><td>42,67</td><td>569,23</td><td>42,33</td></tr>
    <tr><td>2025-08</td><td>586,60</td><td>42,19</td><td>601,17</td><td>42,38</td><td>586,65</td><td>41,71</td></tr>
    <tr><td>2025-09</td><td>582,61</td><td>42,41</td><td>591,60</td><td>42,86</td><td>581,47</td><td>42,36</td></tr>
    <tr><td>2025-10</td><td>593,34</td><td>43,96</td><td>615,05</td><td>45,70</td><td>593,09</td><td>44,16</td></tr>
    <tr><td>2025-11</td><td>597,86</td><td>47,87</td><td>600,90</td><td>47,46</td><td>595,25</td><td>47,78</td></tr>
    <tr><td>2025-12</td><td>577,66</td><td>45,10</td><td>593,86</td><td>45,93</td><td>574,66</td><td>45,16</td></tr>
  </tbody>
</table>

</div>
<p align="center"><small><i>Tabell 8.1 Månedlig RMSE og MAPE per modell i 2025.</i></small></p>

Bias-analysen av den tunede modellen viser et systematisk sesongavvik. August og september er underestimerte med henholdsvis $-5{,}22\%$ ($-20\,548$ salgsenheter) og $-2{,}77\%$ ($-16\,334$ salgsenheter), mens november og desember er lett overestimerte med $+1{,}05\%$ og $+2{,}36\%$. En mulig forklaring er at kalenderfeaturene ikke fullt ut fanger en høstoppgang som skiller seg fra tidligere år – antakelsen er at treningsperioden (2022–2024) inneholder en annen august–september-profil enn 2025, og at modellen dermed glatter ut det virkelige nivået i disse månedene. Mønsteret er konsistent på tvers av alle tre modellsporene og peker på en begrensning i det tilgjengelige sesongsignalet, ikke bare på den tunede modellen.

Bias-mønsteret kan ha flere mulige årsaker. Den mest sannsynlige er at sesongsignalet i kalendervariablene (`month`, `weekofyear`, `dayofweek`) ikke fanger en høstoppgang som er sterkere i 2025 enn i treningsårene 2022–2024 — med tre treningsår er rommet for å lære årlige avvik i samme måned begrenset. En sekundær forklaring er at modellene mangler kampanje- eller eventvariabler utover `Discount`: dersom august–september i datasettet inneholder etterspørselshendelser uten direkte rabattuttrykk, ville disse vises som systematisk underestimering uten å være modellerbare med tilgjengelige features. En tredje, mer teknisk forklaring er at gjennomsnittsegenskapen i Random Forest trekker prediksjonene mot sentrum av treningsperioden i måneder der 2025-nivået ligger over historisk gjennomsnitt.

Figur 8.1 illustrerer den månedlige biasen per modell.

<div align="center">
  <img src="../006 analysis/aktiviteter/16_tolke_modellresultater/fig_bias_maaned_modell.png" alt="Månedlig bias per modell i 2025" width="80%">
  <p align="center"><small><i>Figur 8.1 Månedlig bias per modell i 2025. Positive verdier betyr at modellen overestimerer salget, negative at den underestimerer. Kurven viser at alle tre modellene underestimerer i august–september.</i></small></p>
</div>

Figur 8.2 viser samme månedsforløp som Tabell 8.1, men med RMSE visualisert som linjediagram.

<div align="center">
  <img src="../006 analysis/aktiviteter/13_rmse_og_mape/fig_rmse_maaned_modell.png" alt="Månedlig RMSE per modell i 2025" width="80%">
  <p align="center"><small><i>Figur 8.2 Månedlig RMSE per modell i 2025. Tuned Random Forest har lavest RMSE i majoriteten av månedene, mens benchmark lineær slår gjennom i enkeltmåneder.</i></small></p>
</div>

Segmentanalysen (jf. Tabell 8.2) forsterker forskjellen mellom de to metrikkene. Tuned Random Forest vinner RMSE i 13 av 14 tolkningssegmenter – alle fire kvartaler, alle tre rabattband, alle fire regioner og to av tre salgsnivå – men må vike for benchmark lineær og baseline Random Forest i flere av MAPE-segmentene, særlig i høyrabattsegmentet, vest-regionen og lavvolumssegmentet. I segmentet «høyt salg» er benchmark lineær best på begge metrikker (RMSE $699{,}10$, MAPE $30{,}31\%$), mens tuned Random Forest likevel gir lavest RMSE i segmentet «lavt salg» til tross for at tuned Random Forest-MAPE i samme segment ligger på $90{,}27\,\%$.

Tabell 8.2 gir detaljert RMSE og MAPE per modell for alle 14 tolkningssegmentene, med RMSE og MAPE gruppert under hver modell.

<div align="center" style="font-size:0.8em">

<table>
  <thead>
    <tr>
      <th rowspan="2">Dimensjon</th>
      <th rowspan="2">Verdi</th>
      <th colspan="2">Benchmark lineær</th>
      <th colspan="2">Baseline RF</th>
      <th colspan="2">Tuned RF</th>
    </tr>
    <tr>
      <th>RMSE</th><th>MAPE&nbsp;(%)</th>
      <th>RMSE</th><th>MAPE&nbsp;(%)</th>
      <th>RMSE</th><th>MAPE&nbsp;(%)</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Kvartal</td><td>1</td><td>570,43</td><td>43,58</td><td>580,73</td><td>43,73</td><td>569,10</td><td>43,67</td></tr>
    <tr><td>Kvartal</td><td>2</td><td>578,10</td><td>44,69</td><td>576,41</td><td>43,11</td><td>573,05</td><td>43,90</td></tr>
    <tr><td>Kvartal</td><td>3</td><td>580,18</td><td>42,48</td><td>591,95</td><td>42,67</td><td>579,59</td><td>42,17</td></tr>
    <tr><td>Kvartal</td><td>4</td><td>589,94</td><td>45,85</td><td>602,59</td><td>46,46</td><td>587,87</td><td>45,89</td></tr>
    <tr><td>Rabattbånd</td><td>lav</td><td>583,01</td><td>46,66</td><td>598,95</td><td>46,93</td><td>581,12</td><td>46,14</td></tr>
    <tr><td>Rabattbånd</td><td>middels</td><td>577,89</td><td>44,51</td><td>587,10</td><td>44,63</td><td>577,11</td><td>44,37</td></tr>
    <tr><td>Rabattbånd</td><td>høy</td><td>581,41</td><td>42,76</td><td>586,74</td><td>42,36</td><td>577,96</td><td>42,62</td></tr>
    <tr><td>Region</td><td>Central</td><td>585,83</td><td>44,36</td><td>595,13</td><td>44,49</td><td>584,92</td><td>44,39</td></tr>
    <tr><td>Region</td><td>East</td><td>579,39</td><td>44,19</td><td>587,92</td><td>44,26</td><td>575,30</td><td>43,86</td></tr>
    <tr><td>Region</td><td>South</td><td>587,59</td><td>45,48</td><td>599,43</td><td>45,29</td><td>587,02</td><td>45,03</td></tr>
    <tr><td>Region</td><td>West</td><td>573,90</td><td>43,44</td><td>581,36</td><td>43,18</td><td>571,78</td><td>43,27</td></tr>
    <tr><td>Salgsbånd</td><td>lavt salg</td><td>695,06</td><td>90,79</td><td>694,19</td><td>89,39</td><td>690,44</td><td>90,27</td></tr>
    <tr><td>Salgsbånd</td><td>middels salg</td><td>196,79</td><td>11,40</td><td>224,70</td><td>12,30</td><td>192,51</td><td>11,20</td></tr>
    <tr><td>Salgsbånd</td><td>høyt salg</td><td>699,10</td><td>30,31</td><td>713,73</td><td>30,60</td><td>699,57</td><td>30,39</td></tr>
  </tbody>
</table>

</div>
<p align="center"><small><i>Tabell 8.2 RMSE og MAPE per modell i utvalgte segmenter (kvartal, rabattbånd, region, salgsbånd).</i></small></p>

Feature importance (jf. Tabell 7.3) støtter tolkningen av hvilke dimensjoner som driver variasjonen: kalendervariablene utgjør samlet $\sim 42\%$ av importance i topp 10, `Discount` er sterkeste enkeltvariabel med $11{,}48\%$, og regionvariablene bidrar med $\sim 5{,}8\%$. Den lineære modellen gir negativt fortegn på `Discount` (koeffisient $-166{,}35$), mens Random Forest rangerer samme variabel øverst. Forskjellen tolkes som et mulig tegn på en ikke-lineær eller interaktiv sammenheng mellom rabatt og salg som en lineær spesifikasjon ikke klarer å fange opp.

Figur 8.3 viser korrelasjonsstrukturen mellom de numeriske variablene og salget i treningsdataene. Salget har tilnærmet null lineær korrelasjon med samtlige numeriske prediktorer (ingen overstiger $0{,}02$ i tallverdi), mens kalendervariablene `quarter`, `month` og `weekofyear` er sterkt innbyrdes korrelert fordi de koder samme kalender på ulik oppløsning.

<div align="center">
  <img src="../006 analysis/aktiviteter/07_eksplorativ_analyse_og_visualisering/fig_korrelasjon_numerisk.png" alt="Korrelasjonsvarmekart for numeriske variabler og salg" width="80%">
  <p align="center"><small><i>Figur 8.3 Pearson-korrelasjon mellom numeriske variabler og salg (treningsdata 2022–2024). Ingen enkelt numerisk prediktor har en nevneverdig lineær sammenheng med salget, mens de mekanisk avledede kalendervariablene er sterkt innbyrdes korrelert.</i></small></p>
</div>

---

## 9 Diskusjon

### 9.1 Tolkning av hovedfunn mot problemstillingen

Problemstillingen spør hvordan multippel lineær regresjon og Random Forest Regressor kan brukes til å predikere salg i 2025, og hvilke faktorer som påvirker salget mest. Resultatene gir et differensiert svar. Tuned Random Forest er samlet best i 2025 med RMSE $578{,}26$ og MAPE $43{,}97\%$, men gapet til benchmark lineær er marginalt på totalnivå – $2{,}13$ enheter lavere RMSE og $0{,}21$ prosentpoeng lavere MAPE. Den samlede ytelsen underslår dermed et tydeligere månedsbilde: tuned Random Forest vinner RMSE i elleve av tolv måneder, men bare tre måneder på MAPE, mens baseline Random Forest vinner MAPE i seks måneder uten å vinne RMSE en eneste måned. Det betyr at «best samlet» i praksis handler om absolutt presisjon i måneder med store salgsvolumer, mens prosentfeilen fortsatt er heterogen på tvers av året.

Bias-mønsteret nyanserer dette ytterligere. Tuned Random Forest underestimerer systematisk i august og september (henholdsvis $-5{,}22\%$ og $-2{,}77\%$) og overestimerer svakt i november og desember ($+1{,}05\%$ og $+2{,}36\%$). Mønsteret er konsistent for alle tre modellsporene, noe som peker på en begrensning i sesongsignalet i datagrunnlaget snarere enn i den enkelte modellen. Samtidig viser segmentanalysen at benchmark lineær er bedre enn tuned Random Forest i segmentet for høyt salgsnivå på både RMSE og MAPE. Det første delproblemet bør derfor besvares med en differensiert anbefaling: tuned Random Forest er mest hensiktsmessig som hovedmodell når absolutt prognosepresisjon prioriteres, mens benchmark lineær bør brukes som supplement i toppbelastningssituasjoner og som forklaringsstøtte.

Tabell 9.1 sammenstiller modellprofilene og tydeliggjør differensieringen.

<div align="center" style="font-size:0.8em">

<table>
  <thead>
    <tr>
      <th rowspan="2">Modellrolle</th>
      <th colspan="2">Samlet 2025</th>
      <th colspan="2">Vinnermåneder</th>
      <th colspan="2">Vinnersegmenter</th>
      <th rowspan="2">Tolkbarhet</th>
      <th rowspan="2">Hovedstyrke</th>
      <th rowspan="2">Hovedsvakhet</th>
    </tr>
    <tr>
      <th>RMSE</th><th>MAPE&nbsp;(%)</th>
      <th>RMSE</th><th>MAPE</th>
      <th>RMSE</th><th>MAPE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>benchmark lineær</td><td>580,39</td><td>44,18</td><td>1</td><td>3</td><td>1</td><td>4</td><td>høy</td>
      <td>Høy tolkbarhet og konkurransedyktig i enkelte segmenter.</td>
      <td>Multikollinearitet og manglende regularisering svekker robust koeffisienttolkning.</td>
    </tr>
    <tr>
      <td>baseline RF</td><td>589,28</td><td>44,12</td><td>0</td><td>6</td><td>0</td><td>4</td><td>middels</td>
      <td>Sterk lokal MAPE-ytelse og nyttig referansepunkt for RF.</td>
      <td>Svakest samlet og uten RMSE-seire i måneder eller segmenter.</td>
    </tr>
    <tr>
      <td>tuned RF</td><td>578,26</td><td>43,97</td><td>11</td><td>3</td><td>13</td><td>6</td><td>middels</td>
      <td>Best samlet 2025 og sterkest på absolutt feil.</td>
      <td>MAPE er mer ujevn enn RMSE mellom måneder og segmenter.</td>
    </tr>
  </tbody>
</table>

</div>
<p align="center"><small><i>Tabell 9.1 Modellprofil med samlet RMSE/MAPE, antall vinnermåneder og -segmenter, tolkbarhetsnivå samt hovedstyrke og hovedsvakhet per modell.</i></small></p>

### 9.2 Variablenes påvirkning

Det andre delproblemet gjelder hvilke faktorer som påvirker salget mest. Rangeringen av feature importance i tuned Random Forest viser at rabatt og kalendervariabler dominerer bildet. `Discount` er det sterkeste enkeltsignalet med $11{,}48\%$, tett fulgt av kalendervariablene `dayofmonth` ($11{,}35\%$), `weekofyear` ($10{,}40\%$), `month` ($6{,}74\%$) og `dayofweek` ($6{,}52\%$). Kalendergruppen står samlet for om lag $42\%$ av importance i topp 10, mens regionvariablene bidrar med $5{,}8\%$. De ni øverste variablene i tuned Random Forest gjenfinnes også i topp 10 for baseline Random Forest, noe som styrker stabiliteten i rangeringen.

Lineær regresjon peker i samme retning, men med annen fortegning. `Discount` ($-166{,}35$) har den største meningsfulle koeffisientverdien; `Region_North`-koeffisienten er isolert sett størst i tallverdi ($-277{,}20$), men bygger på én enkelt observasjon (jf. kap. 5.2) og bør tolkes som usikkerhet snarere enn en substansiell regioneffekt. Det negative fortegnet for `Discount` i den lineære modellen står i kontrast til dens høye feature importance i Random Forest, der retningen ikke er fiksert. Det mest sannsynlige er at sammenhengen mellom rabatt og salg er ikke-lineær eller samspillende med andre variabler – for eksempel at rabatteffekten avhenger av produktkategori eller sesong – slik at en lineær spesifikasjon overkompenserer med ett fortegn mens et tremodellbasert ensemble fanger opp flere betingede mønstre. Forskjellen er derfor ikke motstridende funn, men et tegn på at modellene svarer ulikt på det samme underliggende signalet. Variabelsignalene er prediktive, ikke kausale, og bør tolkes som indikatorer på hvilke dimensjoner som bærer prognoseverdien.

### 9.3 Hvorfor presterer modellene så likt?

Et påfallende trekk ved resultatene er hvor like tuned Random Forest (RMSE $578{,}26$, MAPE $43{,}97\%$) og benchmark lineær (RMSE $580{,}39$, MAPE $44{,}18\%$) er på samlenivå. Den viktigste forklaringen ligger i hvordan den tunede modellen ble til: vinnerkonfigurasjonen strammet inn skogen framfor å gjøre den mer fleksibel, med `max_depth=10`, `min_samples_leaf=4` og `max_features=sqrt`. Baseline Random Forest med ubegrenset dybde presterte dårligere (RMSE $589{,}28$), slik at innstrammingen forbedret modellen. Det betyr at den ekstra fleksibiliteten i et fritt voksende tre i hovedsak fanget støy, ikke et reelt ikke-lineært signal. Gjennom bias–varians-avveiingen (jf. §3.2) virker disse hyperparametrene som variansdemping, og modellen som vinner er dermed den som ligger nærmest en glatt, regularisert sammenheng — nettopp derfor lander den tett opp mot den lineære modellen.

Begge modellene arbeider dessuten på det samme informasjonsgrunnlaget: et identisk sett på 67 features uten lag- eller autoregressive ledd som kunne gitt et tre-ensemble et fortrinn i å fange tidsavhengighet. At alle tre modellsporene viser det samme sesongavviket — systematisk underestimering i august–september (jf. §8) — understreker at begrensningen ligger i datagrunnlaget, ikke i den enkelte modellen. Når modellene deler både features og feilmønster, møter de også det samme feilgulvet. Den høye dagsvariasjonen i salget (standardavvik $578$ mot et snitt på $1\,497$) og en MAPE rundt $44\%$ (jf. §9.4) tilsier at en stor andel av variasjonen er irreduserbar støy som ingen av modellklassene kan forklare med de tilgjengelige variablene. Korrelasjonsstrukturen i treningsdataene (jf. Figur 8.3) underbygger dette: ingen enkelt numerisk prediktor har en nevneverdig lineær sammenheng med salget (alle korrelasjoner ligger under $0{,}02$ i tallverdi), slik at det er lite eksploaterbart bivariat signal for noen av modellklassene å gripe fatt i. Når støygulvet dominerer, betyr valg av modellklasse tilsvarende lite for samlet treffsikkerhet.

Det forklarbare signalet er i tillegg additivt av natur. `Discount` og kalendervariablene står samlet for om lag $42\%$ av feature importance (jf. §9.2), og dette er effekter en lineær spesifikasjon fanger uten videre. Det utelukker ikke at det finnes ikke-linearitet: det sprikende fortegnet for `Discount` mellom lineær regresjon og Random Forest (jf. §9.2) tyder på en betinget eller samspillende rabatteffekt. Men at denne ikke-lineariteten ikke gir noe målbart løft i samlet presisjon — selv for en modell som er bygget for å fange den — styrker tolkningen om at de ikke-lineære bidragene er for svake til å forskyve det samlede feilnivået nevneverdig.

Funnene gir et faglig bidrag utover Dagligvare-caset. At ensemble-gevinsten er marginal på samlemålene, men tydeligere på månedsnivå og i bestemte segmenter, illustrerer at fortrinnet til tre-baserte ensembler er sterkt kontekstavhengig. På et datasett med relativt lav strukturell ikke-linearitet, moderat størrelse (om lag $6\,700$ treningsrader) og dominerende kalender- og rabattsignaler nærmer ensemble-fordelen seg null på de samlede målene. Dette samsvarer med litteraturen: Carbonneau et al. (2008) finner at maskinlæring gir tydeligst forbedring når etterspørselsmønsteret er komplekst og dataene rike, mens Fildes et al. (2022) og Makridakis et al. (2018) viser at enkle modeller ofte er overraskende konkurransedyktige på aggregert nivå. For Dagligvare betyr dette at den marginale forskjellen ikke svekker anbefalingen om tuned Random Forest som hovedmodell (jf. §9.1, §9.4), men at den lineære modellen samtidig framstår som et fullverdig og mer tolkbart alternativ — et parsimoni-hensyn som taler for å beholde den som referanse og forklaringsstøtte snarere enn å forkaste den.

### 9.4 Praktisk nytte for Dagligvare

En MAPE på rundt 44 % er høyt sett opp mot operative benchmarks i varehandel, der prosentavvik under 20 % ofte regnes som brukbart for daglige prognoser. På dagsnivå med høy varians i datasettet (standardavvik 578 på salg med snitt 1 497) er prosentfeilen likevel forventet å være stor, og prosentfeil er per definisjon ustabil når faktiske volum er små (jf. ligning (3.4) i §3.3). Modellens praktiske verdi for Dagligvare ligger derfor mer i den relative rangeringen mellom modellsporene og i segmentanalysen enn i absolutt MAPE-nivå. For operativ innkjøpsbruk anbefales i tillegg aggregering til uke- eller månedsnivå, der enkeltdagers prosentavvik glattes ut.

Funnene har fire tydelige praktiske bruksområder i Dagligvare, alle forankret i modellvalget i 9.1 og variabelrangeringen i 9.2. For innkjøp og overordnet lagerstyring er tuned Random Forest det naturlige standardvalget fordi modellen er best samlet på absolutt presisjon og gir den mest stabile månedsytelsen. Analysen dokumenterer ikke lageroptimalisering i snever forstand, men gir et sterkere grunnlag for å treffe bedre på totalnivå i planlagte bestillinger og dermed redusere risiko for både over- og underbestilling.

Tabell 9.2 oppsummerer beslutningsmatrisen med anbefalt modellrolle, prioritert metrikk og hovedforbehold per bruksområde.

<div align="center" style="font-size:0.8em">

<table>
  <thead>
    <tr>
      <th>Beslutningsområde</th>
      <th>Anbefalt modell</th>
      <th>Prioritert metrikk</th>
      <th>Praktisk nytte</th>
      <th>Hovedforbehold</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Innkjøp og lager</td><td>tuned RF</td><td>RMSE</td><td>høy</td>
      <td>Ikke lageroptimalisering; prosentfeil kan være ujevn i delsegmenter.</td>
    </tr>
    <tr>
      <td>Kampanje og rabatt</td><td>tuned RF, med baseline RF som MAPE-kontroll ved høy rabatt</td><td>RMSE med MAPE-kontroll</td><td>middels</td>
      <td>Rabattsignalene er prediktive, ikke kausale.</td>
    </tr>
    <tr>
      <td>Bemanning og ressursplanlegging</td><td>tuned RF, med benchmark lineær-kontroll ved svært høyt salgsnivå</td><td>RMSE</td><td>middels–høy</td>
      <td>Ikke butikk- eller skiftoptimalisering; toppbelastning krever ekstra varsomhet.</td>
    </tr>
    <tr>
      <td>Ledelsesrapportering</td><td>tuned RF som hovedprognose, benchmark lineær som forklaringsstøtte</td><td>RMSE med forklaringsstøtte</td><td>middels</td>
      <td>Lineær modell skal ikke brukes som kausalt bevis for salgsendringer.</td>
    </tr>
  </tbody>
</table>

</div>
<p align="center"><small><i>Tabell 9.2 Beslutningsmatrise og bruksregler: beslutningsområder, anbefalt modellrolle, prioritert metrikk, praktisk nyttegrad og hovedforbehold.</i></small></p>

For kampanje- og rabattvurderinger anbefales tuned Random Forest som hovedmodell, men med en ekstra kontroll mot MAPE i segmentet for høy rabatt, der baseline Random Forest er best på prosentfeil. Dette gjenspeiler at `Discount` er det sterkeste enkeltsignalet i modellen, men at prosentavvik er mer følsomt enn absoluttavvik i rabattutsatte perioder. For aggregert bemannings- og ressursplanlegging gir tuned Random Forest et robust bilde av forventet aktivitetsnivå per måned og kvartal, men benchmark lineær bør trekkes inn når toppbelastning planlegges, siden den er sterkere i segmentet for høyt salgsnivå. For ledelsesrapportering fungerer tuned Random Forest som hovedprognose, mens benchmark lineær brukes som forklaringsstøtte når retningen i sentrale signaler må kommuniseres kortfattet for ikke-tekniske interessenter. I alle disse bruksområdene må analysens avgrensninger holdes eksplisitt: prognosene er prediktive, ikke kausale, og bør kombineres med lokal fagkunnskap før de omsettes til operative beslutninger.

### 9.5 Metodiske begrensninger

Flere metodiske forhold setter grenser for hvor langt funnene kan strekkes, og de påvirker både påliteligheten innenfor caset og generaliserbarheten utover det. Datagrunnlaget er representativt for caset, men består av ett datasett fra én virksomhet; påliteligheten innenfor caset kan fortsatt være god, mens robustheten mot andre kontekster ikke er testet, og funnene kan ikke uten videre overføres til andre dagligvarekjeder, regioner eller produktmixer uten eget datagrunnlag og ny validering. Analysen inkluderer heller ikke eksterne makroøkonomiske faktorer som inflasjon, rente eller konjunkturer, slik at prognosene kan være mindre robuste dersom 2025 påvirkes av forhold utenfor feature-settet, og resultatene generaliserer dårligere til perioder der slike eksterne sjokk spiller en større rolle. Modellomfanget er dessuten avgrenset til multippel lineær regresjon og Random Forest Regressor; den valgte modellen er best i prosjektets kandidatfelt, men ikke nødvendigvis best mulig totalt sett, og andre metodeklasser – tidsrekkemodeller, gradient boosting, nevrale nett – er ikke vurdert, noe som gir begrenset grunnlag for å generalisere at samme modellfamilie er best i andre lignende problemer.

De øvrige forholdene gjelder estimering og tolkning. Den lineære modellen brukes med uregularisert OLS (ligning (3.2)) på en modellmatrise med 67 features, inkludert mange one-hot-kodede dummyvariabler, noe som gir en betydelig risiko for multikollinearitet; dette svekker tolkningsvaliditeten av de enkelte koeffisientene selv om prediksjonskraften kan være upåvirket, og koeffisientmønstre kan endre seg når datastruktur eller kategorifordeling endres i andre case. Hyperparametertuningen av Random Forest er basert på ett valideringsår (2024), slik at valget av tuned konfigurasjon reflekterer mønstrene i ett år framfor en mer robust kryssvalidering over flere perioder, og sensitiviteten for andre valideringsvinduer er ikke undersøkt. To planendringer i modellutviklingsfasen er dokumentert i endringsloggen: det felles treningssteget ble gjort om til en verifisering av treningsgrunnlag og modellsignaler siden begge modellene allerede var trent i forutgående aktiviteter, og hyperparametertuningen ble avgrenset til Random Forest-sporet alene. Samlet styrket disse endringene sporbarheten i modellutviklingen, men innebærer at lineær regresjon ikke har gjennomgått tilsvarende optimalisering.

Funnene er i tillegg prediktive og ikke kausale. Variabelrangeringer og koeffisienter forteller hvilke signaler som er nyttige for å predikere salg, men ikke hvorfor salget endrer seg, og beslutninger som krever kausal innsikt kan ikke generaliseres direkte fra disse prediktive mønstrene. Denne avgrensningen er viktig å holde fast ved når resultatene oversettes til beslutningsstøtte, for eksempel når rabattsignalet skal tolkes i kampanjearbeidet.

### 9.6 Videre arbeid

Fire typer videre arbeid følger naturlig av disse begrensningene. Et første steg er supplering med fagfellevurderte kilder innen etterspørselspredikering i dagligvarehandel, som kan styrke både metodevalg og tolkning. Et andre steg er sensitivitetsanalyse av variabelsignalene – særlig `Discount` og regionvariablene – slik at tolkningen blir mer robust mot ikke-lineære sammenhenger. Et tredje steg er bredere validering, enten ved å bruke flere år som valideringsvinduer eller ved å teste modellene mot reelle salgsdata fra en dagligvarekjede. Et fjerde steg er utvidelse av modellomfanget til tidsrekke- og gradient-boosting-metoder som kan adressere både det systematiske høstbias-mønsteret og den heterogene MAPE-ytelsen på en mer presis måte.

---

## 10 Konklusjon

Problemstillingen spør hvordan multippel lineær regresjon og Random Forest Regressor kan brukes til å predikere salg i 2025 for en dagligvarekjede, og hvilke faktorer som påvirker salget mest. På tvers av de tre modellsporene er tuned Random Forest det samlet beste valget med RMSE $578{,}26$ og MAPE $43{,}97\%$ på 2025, og modellen vinner RMSE i elleve av tolv måneder og tretten av fjorten tolkningssegmenter. Gapet til benchmark lineær er likevel marginalt på totalnivå, og sistnevnte er best i segmentet for høyt salgsnivå. Anbefalingen er derfor at Dagligvare bruker tuned Random Forest som standardprognose for innkjøp, lager og aggregert ressursplanlegging, benchmark lineær som forklaringsstøtte og som supplement i toppbelastningssituasjoner, og baseline Random Forest som kontroll mot prosentfeil i perioder med høy rabatt.

Rabatt og kalendervariabler er de mest påvirkningsrike prediktorene, der `Discount` er det sterkeste enkeltsignalet og kalendergruppen samlet står for om lag $42\%$ av importance i topp 10 i den anbefalte modellen. Regionvariablene bidrar som sekundære prediktorer og driver samtidig variasjon i MAPE mellom markedene. Funnene gjelder innenfor dette caset og bør tolkes som prediktive signaler, ikke kausale forklaringer; operativ bruk forutsetter at Dagligvare kombinerer modellprognosene med lokal fagkunnskap og vurderer supplerende validering før de omsettes til beslutninger i innkjøp, kampanjestyring og ressursplanlegging.

Rapporten bidrar både praktisk og faglig. Praktisk leverer den Dagligvare en konkret beslutningsmatrise for modellvalg på tvers av innkjøp, kampanje, ressursplanlegging og ledelsesrapportering, samt et eksplisitt forbehold om hvilken metrikk som bør prioriteres når. Faglig leverer den en kontrollert empirisk sammenligning av to modellfamilier på ett dagligvarecase med streng tidsbasert oppsplitting, der både samlede mål, månedsnivå, segmentnivå og bias-mønstre er rapportert — og dokumenterer at ensemble-fordelen kan være marginal på totalnivå selv når modellen vinner det store flertallet av månedene og segmentene.

\newpage

## 11 Bibliografi

Breiman, L. (2001). Random forests. *Machine Learning*, 45(1), 5–32. <https://doi.org/10.1023/A:1010933404324>

Carbonneau, R., Laframboise, K., & Vahidov, R. (2008). Application of machine learning techniques for supply chain demand forecasting. *European Journal of Operational Research*, 184(3), 1140–1154. <https://doi.org/10.1016/j.ejor.2006.12.004>

Cerqueira, V., Torgo, L., & Mozetič, I. (2020). Evaluating time series forecasting models: An empirical study on performance estimation methods. *Machine Learning*, 109(11), 1997–2028. <https://doi.org/10.1007/s10994-020-05910-7>

Fildes, R., Ma, S., & Kolassa, S. (2022). Retail forecasting: Research and practice. *International Journal of Forecasting*, 38(4), 1283–1318. <https://doi.org/10.1016/j.ijforecast.2019.06.004>

Hyndman, R. J., & Koehler, A. B. (2006). Another look at measures of forecast accuracy. *International Journal of Forecasting*, 22(4), 679–688. <https://doi.org/10.1016/j.ijforecast.2006.03.001>

James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An introduction to statistical learning: With applications in R* (2. utg.). Springer. <https://doi.org/10.1007/978-1-0716-1418-1>

Kang, R. (2023). Sales prediction of Big Mart based on linear regression, random forest, and gradient boosting. *Advances in Economics, Management and Political Sciences*, 17, 200–207. <https://doi.org/10.54254/2754-1169/17/20231094>

Makridakis, S., Spiliotis, E., & Assimakopoulos, V. (2018). Statistical and machine learning forecasting methods: Concerns and ways forward. *PLOS ONE*, 13(3), e0194889. <https://doi.org/10.1371/journal.pone.0194889>

Makridakis, S., Spiliotis, E., & Assimakopoulos, V. (2022). M5 accuracy competition: Results, findings, and conclusions. *International Journal of Forecasting*, 38(4), 1346–1364. <https://doi.org/10.1016/j.ijforecast.2021.11.013>

Mitra, A., Jain, A., Kishore, A., & Kumar, P. (2022). A comparative study of demand forecasting models for a multi-channel retail company: A novel hybrid machine learning approach. *Operations Research Forum*, 3(4), 58. <https://doi.org/10.1007/s43069-022-00166-4>

Spiliotis, E., Makridakis, S., Semenoglou, A.-A., & Assimakopoulos, V. (2022). Comparison of statistical and machine learning methods for daily SKU demand forecasting. *Operational Research*, 22(3), 3037–3061. <https://doi.org/10.1007/s12351-020-00605-2>

Ulrich, M., Jahnke, H., Langrock, R., Pesch, R., & Senge, R. (2021). Distributional regression for demand forecasting in e-grocery. *European Journal of Operational Research*, 294(3), 831–842. <https://doi.org/10.1016/j.ejor.2019.11.029>

\newpage

## 12 Vedlegg

Dette kapitlet samler referanser til stort eller detaljert datamateriale som ikke er limt direkte inn i rapporten, men som følger som digitale vedlegg til rapporten. Vedleggene A1–A7 gir leseren tilgang til de underliggende analyseartefaktene.

Tabell 12.1 lister vedleggene A1–A7 med innhold og tilhørende kildefil.

| Vedlegg | Innhold | Kildefil |
| --- | --- | --- |
| A1 | Radvise prognoser for 2025 for alle tre modeller (3 312 rader) | `tab_prognoser_2025_detalj.csv` |
| A2 | Radvise prognosefeil og absoluttfeil for 2025 | `tab_prognosefeil_2025_detalj.csv` |
| A3 | Full tuning-kandidatgrid for Random Forest | `tab_rf_tuning_kandidater.csv` |
| A4 | Full feature importance for tuned Random Forest | `tab_rf_tuned_feature_importance.csv` |
| A5 | Full koeffisienttabell for lineær regresjon | `tab_lr_koeffisienter.csv` |
| A6 | Full RMSE og MAPE per måned i lang form | `tab_rmse_mape_maaned.csv` |
| A7 | Full segmentmetrikk per modell | `tab_segmentmetrikk_modell.csv` |

<p align="center"><small><i>Tabell 12.1 Vedleggsreferanser til stort datamateriale som hører til analysen.</i></small></p>
