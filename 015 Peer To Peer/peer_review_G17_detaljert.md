# Peer-review av G17

## Forsideopplysninger

| Felt | Innhold |
| --- | --- |
| Vurderende gruppe | G19 (nettstudent kveld) |
| Vurdert gruppe | G17 |
| Tittel på rapporten | *Finansiell logistikk og beslutningstøtte ved hjelp av KI* |
| Forfatter | Magnus Ødegård |
| Dato | 2026-05-04 |

## Helhetsinntrykk

Rapporten er metodisk solid og forankret i fagfellevurdert primærlitteratur (Appel et al., 2019; Schoonbee et al., 2022). CRISP-DM-strukturen, datadelingen, klassevektingen og hyperparameterjusteringen er ryddig dokumentert, og koblingen mellom litteratur, metode og resultat er gjennomgående tett. Diskusjonen er ærlig om at benchmarkene fra primærstudiene ikke nås, og forklaringen forankres i datasettets størrelse og syntetiske natur. Den praktiske beslutningsstøtteverdien fremstår tydelig, særlig gjennom risikotredelingen og recall-prioriteringen. Hovedutfordringene er at sammendrag, abstract, innholdsfortegnelse og forsideopplysninger ennå ikke er ferdigstilt, at datasettets syntetiske natur avsløres først i §9.1 (i stedet for i §1.4 eller §5.2), at risikoklassifiseringen i §8.3 evalueres på treningsdataene og dermed gir optimistiske separasjonstall, og at §7 og §8 inneholder tolkning som etter veiledningens skille hører hjemme i §9. Litteraturgrunnlaget er smalt (to artikler), forskningsgapet er ikke eksplisitt formulert, og veiledningens krav om validitet, reliabilitet og etiske hensyn er ikke direkte adressert. Hovedinntrykket er likevel et ryddig og lesbart fagarbeid med tydelig potensial: de fleste forbedringspunktene gjelder *plassering* og *eksplisittering* mer enn faglige feilgrep.

---

## 1 Innledning

### Styrker

Innledningen er kort og effektiv, og forankres i fagfellevurdert litteratur fra første avsnitt (Appel et al., 2019; Schoonbee et al., 2022). Bakgrunn og kontekst er konkret: tradisjonell beløpsbasert prioritering presenteres som problemet, og maskinlæringsbasert risikovurdering som det alternative grepet, med tydelige ytelsestall fra primærlitteraturen. Avgrensingene i §1.3 begrunnes faglig (overførbarhet, ikke tidsmangel), og §1.4 formulerer fire eksplisitte antagelser med konsekvenser for analysens gyldighet – det er ryddig håndverk.

### Forbedringspunkter

- **Eksplisitt forskningsmål mangler.** Veiledningens kriterieliste skiller mellom *problemstilling* og *forskningsmål eller forskningsspørsmål*. §1.1 leverer en god problemstilling, men et tilsvarende formulert mål («Målet med prosjektet er å …») er gjemt i siste avsnitt av §1.0 («Målet er å utvikle en maskinlæringsmodell …»). Det blir uklart om problemstillingen alene fungerer som forskningsspørsmål eller om målet er noe annet.
- **Sammenheng mellom mål og studiens betydning kan tydeliggjøres.** Innledningen presenterer relevansen på feltnivå (fakturapredikering generelt) mer enn på casenivå. Hvorfor *Bedriften* trenger akkurat denne studien – og hvilken praktisk verdi den vil få – står først i §4.0. En kort, eksplisitt setning i §1.0 om hva utfallet betyr for Bedriften ville bundet motivasjonen tettere til problemstillingen.
- **Spenning mellom antagelse A2 og §9.1.** A2 omtaler datasettet som anonymisert ekte data der «enkelte variabler er justert for å ivareta konfidensialitet». §9.1 avslører imidlertid at datasettet er *syntetisk generert*. Dette er to vesentlig forskjellige datagrunnlag og har ulike konsekvenser for studiens validitet. Avviket bør avklares allerede i §1.4 (eller senest i §5.2), ikke først i diskusjonen.
- **§1.2 Delproblem 2 leveres ikke.** «Forventet betalingsforsinkelse – estimert antall dager etter forfall» er formulert som en av tre beslutningsvariabler, men prosjektet gjennomfører kun binær klassifisering. Et regresjonselement på antall dager forsinket finnes ikke i analysen. Enten bør delproblemet fjernes eller eksplisitt parkeres med begrunnelse.
- **Problemstillingens «KI» er bredere enn det studien faktisk dekker.** «Hvordan kan KI brukes …» åpner for et stort metoderom, mens prosjektet i praksis tester logistisk regresjon, Random Forest og XGBoost – tre etablerte tabular-ML-metoder. En innstramming til *maskinlæring* eller *veiledet klassifisering* ville stemt bedre med metodevalget i §3.2.

### Foreslåtte endringer

1. Legg til et eksplisitt forskningsmål eller -spørsmål, gjerne som første setning i §1.1 eller som en egen kulepunktliste over forskningsspørsmål.
2. Avklar i §1.4 (eller §5.2) at datagrunnlaget er syntetisk generert med utgangspunkt i variabler primærlitteraturen identifiserer som prediktive, og oppdater A2 deretter.
3. Stryk delproblem 2 i §1.2 – eller behold det og dokumenter eksplisitt at regresjonsformuleringen ble vurdert, men ikke gjennomført, og hvorfor.
4. Vurder å erstatte «KI» med «maskinlæring» eller «veiledet klassifisering» i problemstillingen for å speile den faktiske metoden.
5. Legg til 1–2 setninger i §1.0 som binder studiens betydning konkret til Bedriftens situasjon (ikke bare feltet generelt).

---

## 2 Litteraturgjennomgang og teoretisk forankring

### Styrker

Litteraturkapitlet er tett koblet til metodevalgene: Appel et al. (2019) og Schoonbee et al. (2022) er nøye og fyldig presentert, og Tabell 2.1 gir en effektiv side-ved-side-sammenstilling av kontekst, datasett, problemtype, beste modell og featureviktighet. Begge studiene refereres systematisk videre i metode-, resultat- og diskusjonskapitlene (særlig featureviktigheten *AveDaysLate* og benchmarktallene), slik at primærlitteraturen faktisk brukes – ikke bare nevnes. Teorikapitlet introduserer relevante kjernebegreper (veiledet læring, binær klassifisering, AUC/F1, feature engineering, konseptdrift, DSS) i en logisk rekkefølge, og henter inn kanoniske referanser for algoritmene (Breiman, 2001; Chen & Guestrin, 2016).

### Forbedringspunkter

- **Smalt litteraturgrunnlag.** §2.1 oppgir at to artikler er gjennomgått i sin helhet. Selv om begge er svært relevante, er det lite triangulering mot tilgrensende felt (kredittrisiko, B2B trade credit, behavioral payment models, eller bredere accounts receivable-litteratur). Veiledningens kriterium «gjennomgang av relevant forskning innenfor det aktuelle området» ville stått sterkere om bildet var bredere enn IPPP-nisjen.
- **Identifikasjon av teoretisk/begrepsmessig hull mangler.** §2.4 sammenstiller likheter og forskjeller mellom de to primærstudiene, men formulerer ikke et eksplisitt forskningsgap som dette prosjektet adresserer. At datasettet er mindre og at konteksten er norsk offentlig sektor er kontekstuelle forskjeller, ikke et teoretisk hull. Veiledningen ber spesifikt om dette punktet.
- **Litteratursøkets prosess er underdokumentert.** §2.1 nevner to databaser og fire søkeord, men oppgir verken inklusjons-/eksklusjonskriterier, tidsavgrensning, antall treff eller screeningprosess. Dette gjør søket lite etterprøvbart og gjør det uklart om to artikler er utfallet av en grundig prosess eller en stikkprøve.
- **Teori-til-metode-koblingen er løs.** §3.2 introduserer tre algoritmer, men begrunnelsen for *hvorfor nettopp disse tre* (lineær baseline, bagging-ensemble, boosting-ensemble) kommer først i §5.1. Tilsvarende argumenteres recall som primærmetrikk for beslutningsstøtte først i §5.1 og §9.2 – ikke i §3.3 hvor metrikkene introduseres. Teorikapitlet kunne i større grad fungere som *forankring* for de metodiske valgene som senere gjøres.
- **DSS-delen er kort og smalt forankret.** §3.6 hviler i hovedsak på Appel et al. og Schoonbee et al. når det gjelder DSS-perspektivet. Når §1.0, §9.2 og §10.0 så tydelig begrunner prosjektet i beslutningsstøtteformål, er fraværet av en bredere DSS-forankring (f.eks. Power, Sprague & Carlson) merkbart.

### Foreslåtte endringer

1. Utvid §2.1 med inklusjons-/eksklusjonskriterier, tidsvindu og antall treff per søk, gjerne i punktform.
2. Legg til et kort avsnitt (i §2.4 eller ny §2.5) som eksplisitt formulerer det forskningsgapet prosjektet adresserer – f.eks. overførbarhet til små datasett, eller validering av IPPP-metodikken i en norsk offentlig sektor-kontekst.
3. Trekk inn 2–3 supplerende kilder fra tilgrensende felt for å brede ut forankringen, f.eks. kredittrisiko, B2B trade credit, eller accounts receivable management generelt.
4. Flytt argumentet om recall som primærmetrikk for beslutningsstøtte (i dag i §5.1) inn i §3.3 – det er en teoretisk vurdering som hører til i teorikapitlet.
5. Begrunn algoritmevalget eksplisitt i §3.2 (lineær baseline, robust bagging-ensemble, state-of-the-art boosting) og referer fram til at dette operasjonaliseres i §6.
6. Styrk §3.6 med 1–2 referanser til etablert DSS-litteratur for å forankre risikoscore-tilnærmingen ut over de to primærstudiene.

---

## 3 Metode

### Styrker

Metodekapitlet er strukturert rundt CRISP-DM (§5.1) og henter prosessrammeverket eksplisitt fra Schoonbee et al. (2022) – det gir en klar sammenheng mellom litteratur og framgangsmåte. Datadelingen er korrekt beskrevet: 80/20 stratifisert splitt (776 trening / 195 test), holdout-settet holdes tilbake gjennom hyperparameterjusteringen og brukes kun til endelig evaluering. Klassevektingen er differensiert per algoritme (`class_weight='balanced'` for log.reg og RF, `scale_pos_weight` for XGBoost) og forholdet 1,96 er regnet ut og oppgitt. Begrunnelsen for å prioritere recall (§5.1) er konkret og handlingsrettet: «mer kostbart å overse en forsinket faktura enn å flagge en feilaktig» – dette er nettopp den typen kobling mellom metrikk og beslutningskontekst veiledningen etterspør. Tabell 5.1 (variabelskjema) er ryddig og fullstendig, og avsnittet om bruk av KI-verktøy (Claude Code) er en god og åpen praksis.

### Forbedringspunkter

- **Validitet, reliabilitet og etiske hensyn er ikke eksplisitt forklart.** Veiledningen nevner dette som et eget kriterium. §5.1–§5.2 dekker delelementer (kryssvalidering, holdout, klassevekt, anonymisering), men begrepene *validitet*, *reliabilitet* og *etikk* forekommer ikke som ankerpunkter. Bruken av eksterne KI-verktøy (Claude Code) på datasett kunne også vært vurdert etisk, særlig hvis datasettet i prinsippet var ekte.
- **Datagrunnlagets natur er underkommunisert i metodekapitlet.** Først i §9.1 fremgår det at datasettet er syntetisk generert. For en metodevurdering er dette helt sentralt: det påvirker hvilke validitetstrusler som er relevante, og hvordan resultatene skal tolkes. Status burde vært avklart i §5.2 eller §1.4, ikke først i diskusjonen.
- **Splittstrategien drøftes ikke opp mot konseptdrift.** §3.5 og §9.3 erkjenner at konseptdrift er sentralt og at Appel et al. (2019) bruker en window size-parameter for å håndtere det. Likevel velger §5.1 stratifisert random split – ikke tidsbasert. Dette er et metodisk valg som krever begrunnelse: enten at tidsstrukturen i datasettet er for kort, eller at konseptdrift bevisst er parkert ut av scope.
- **Valg av binær framfor multiklasse-formulering er ubegrunnet.** Schoonbee et al. (2022) bruker fire-klasses formulering. §5.1 redegjør ikke for hvorfor binær er valgt – datavolum (971 fakturaer) er den åpenbare grunnen, men det bør stå eksplisitt og vurderes opp mot beslutningsstøttebehovet.
- **Casekapitlet (§4.0) er deskriptivt tynt.** Kapittelet er fire avsnitt uten figurer, tabeller eller deskriptive nøkkeltall (volum, omsetning, leverandørspredning på et aggregert nivå, andel forsinkede fakturaer historisk). Slik det står nå kunne kapittelet beskrevet nær sagt en hvilken som helst norsk offentlig virksomhet. Deskriptive figurer som ligger i §7.1 hører hjemme her – jf. veiledningens skille mellom case og analyse.
- **Hyperparametersøkets dekning er ikke drøftet.** §6.3 rapporterer 40 og 50 tilfeldige kombinasjoner for henholdsvis RF og XGBoost. Hvor stor andel av søkerommet dette utgjør, og hvor stabil beste modell er på tvers av seeds, kunne vært nevnt for å støtte reliabiliteten i resultatene.

### Foreslåtte endringer

1. Legg til en kort §5.3 «Validitet, reliabilitet og etiske hensyn» som dekker datagrunnlagets natur, splittstrategiens validitet, kryssvalideringens reliabilitet og konfidensialitet/KI-bruk som etiske vurderinger.
2. Flytt avklaringen om at datasettet er syntetisk generert (i dag §9.1) opp til §5.2, og oppdater antagelse A2 (§1.4) tilsvarende.
3. Begrunn valget av stratifisert random split eksplisitt i §5.1 – inkludert hvorfor tidsbasert split ikke benyttes, til tross for at konseptdrift er sentralt i primærlitteraturen.
4. Begrunn binær framfor multiklasse-formulering i §5.1 (datavolum, tolkbarhet, beslutningskontekst).
5. Utvid §4.0 med deskriptive nøkkeltall om Bedriftens fakturavolum, leverandørspredning og overordnet betalingsmønster, og flytt deskriptive figurer som §7.1 «Forsinkelsesdistribusjon» og «Andel per kategori/risiko» til casekapitlet hvor de hører hjemme.
6. Tilføy en kort kommentar i §6.3 om søkerommets størrelse og eventuell sensitivitet for seed/kombinasjonsantall.

---

## 4 Analyse og resultater

### Styrker

Modelleringsløpet er gjennomført metodisk: baseline → hyperparameterjustering → endelig evaluering på holdout, dokumentert i Tabell 8.1 med fem modeller side om side mot benchmarks fra Appel et al. (2019). Featureviktigheten i §8.2 bekrefter at «gjennomsnittlig antall dager forsinket per leverandør» er sterkeste prediktor – eksplisitt koblet til Schoonbee et al. (2022) sin *AveDaysLate* – og dette gir intern konsistens med teori- og litteraturkapitlet. Risikoscoren fra Appel et al. operasjonaliseres konkret som tredeling (lav/middels/høy, §8.3), og §8.3 viser tydelig hvordan resultatene oversettes til beslutningsstøtte. Visualiseringen er rik: ROC-kurver, AUC-sammenligning mot benchmark, presisjon/recall/F1, konfusjonsmatrise, featureviktighet og risiko-mot-beløp gir leseren et godt overblikk.

### Forbedringspunkter

- **Resultatevaluering på treningsdataene gir optimistiske tall.** §8.3 oppgir at sluttmodellen er «retrent på hele datasettet (971 fakturaer) for full dekning», og rapporterer deretter «faktisk forsinkelsesrate» per risikoklasse (7 % / 28 % / 55 %). Disse tallene er beregnet på fakturaer modellen har sett under trening – separasjonen «nær åtte ganger høyere» som §8.3 fremhever, er per definisjon optimistisk og ikke representativ for ny data. En ærlig evaluering ville brukt out-of-fold-prediksjoner fra kryssvalidering eller tallene fra holdout-settet (195 fakturaer).
- **§7 og §8 inneholder mye tolkning som hører hjemme i §9.** Veiledningens skille er at resultatkapittelet skal presentere funn nøkternt og diskusjonen skal vurdere dem. Eksempler på tolkning som er forskuttert: «noe som indikerer at leverandørkategori er en informativ prediktorvariabel» (§7.1), «bekrefter at variabelen er valid og informativ for modelltrening» (§7.1), «konsistent med Appel et al. (2019)» (§7.1, §8.2), «Logistisk regresjon utmerker seg som en overraskende sterk baseline … noe som indikerer at lineære sammenhenger er fremtredende» (§8.1). Dette er gode poenger – men de er diskusjon, ikke resultater.
- **EDA er plassert i analysekapitlet, ikke i datakapitlet.** §7.1 inneholder seks deskriptive figurer (klasseubalanse, forsinkelsesdistribusjon, andel per kategori/betingelse/risiko, korrelasjonsmatrise) som logisk hører hjemme i §5.2 eller §4.0 (case). Resultatet er at §7 fungerer som et halvt resultatkapittel og §8 som det andre – strukturen blir uklar.
- **Dobbel «Figur 1».** Figur 1 (klasseubalanse) settes inn både i §5.2 og §7.1 med samme bilde. Det forvirrer kryssreferansene og bryter med hovedregelen om at hver figur har ett unikt nummer.
- **Featureviktighet er underdrøftet.** §8.2 nevner kun den viktigste prediktoren. Hvilke features følger på 2.–5. plass? Hvor stor andel av total importance utgjør topp 5? For et beslutningsstøttesystem er dette nettopp det som forteller virksomheten hvilke datapunkter de bør samle.
- **Risikotersklene 0,30 og 0,55 er ad-hoc.** §8.3 introduserer tredelingen uten begrunnelse for nettopp disse tersklene. En kort kommentar – f.eks. om de er valgt slik at hver kategori har noenlunde like store grupper eller for å gi ønsket recall/presisjon-balanse – ville styrket validiteten.
- **Korrelasjons- og separasjonstall mangler i tekst.** §7.1 omtaler «sterkest lineær korrelasjon» og «tydelig separasjon» uten å rapportere koeffisientene eller forsinkelsesratene per kategori. Konkrete tall i brødteksten er nyttig for leseren, særlig når de allerede er beregnet for figurene.
- **Featureantallet er internt inkonsistent.** §6.1 oppgir at 15 råkolonner blir til 34 prediktorvariabler, men opptellingen i samme avsnitt (4 dato/betingelse + 27 OHE-kolonner + 2 historiske) summerer til 33. Dette er lett å rette, men nettopp slike små avvik svekker tilliten til at alle tall er kontrollert.

### Foreslåtte endringer

1. Erstatt evalueringen i §8.3 med out-of-fold-prediksjoner eller tall fra holdout-settet, eller gjør det helt eksplisitt at de rapporterte ratene gjelder treningsdataene og dermed er optimistiske.
2. Flytt tolkningssetninger fra §7.1, §7.2 og §8.1 til §9, og la resultatkapitlene rapportere tall og figurer nøkternt.
3. Flytt §7.1 (EDA) til §5.2 eller §4.0; behold §7 til leverandørprofil/risikoscore (eller integrer leverandøranalysen i §6).
4. Slett dupliseringen av Figur 1 mellom §5.2 og §7.1; la figuren stå én gang og kryssreferer der den trengs.
5. Utvid §8.2 med en kort tabell over topp 5–10 features og deres importance-andel.
6. Begrunn risikotersklene 0,30 / 0,55 i §8.3 (f.eks. lik gruppestørrelse, presisjons-/recall-mål, eller sammenligning med Appel et al.).
7. Legg til Pearson-koeffisienter for de sterkeste sammenhengene i §7.1 og forsinkelsesrater per kategori der det er relevant.
8. Verifiser featureantallet i §6.1 og oppdater tellingen.

---

## 5 Diskusjon

### Styrker

Diskusjonen er ærlig om benchmark-gapet (§9.1) og leverer to solide forklaringer som er forankret i datagrunnlaget: datasettets størrelse (971 mot 175 552 og 1 068 620 i primærstudiene) og at datasettet er syntetisk generert med komprimert varians. Koblingen til primærlitteraturen er gjennomgående: at XGBoost er beste modell speiler Appel et al. (2019), at ensemblemetoder slår logistisk regresjon støttes av begge primærstudier, og at *AveDaysLate* er sterkeste prediktor knyttes til Schoonbee et al. (2022). §9.2 etablerer den praktiske beslutningsstøtteverdien tydelig: prioriteringen rettes mot 419 høyrisikofakturaer fremfor å behandle alle 971 likt, og recall på 0,833 fortolkes konkret som «fanger 83 % av forsinkede fakturaer». §9.3 erkjenner relevante begrensninger (syntetisk data, konseptdrift, høy andel i høyrisikogruppen).

### Forbedringspunkter

- **Eksplisitt kobling tilbake til problemstillingen mangler.** Veiledningen krever at funnene knyttes tilbake til forskningsmål/forskningsspørsmål. §9 diskuterer ytelse, beslutningsstøtteverdi og begrensninger, men siterer aldri problemstillingen fra §1.1 og besvarer den ikke punktvis. Et eksplisitt avsnitt («Tilbake til problemstillingen …») ville styrket strukturen.
- **Implikasjoner er nesten utelukkende praktiske.** Veiledningen nevner praksis, *teori* og *policy* som mulige implikasjonsdomener. §9 dekker praksis godt, men teoretiske implikasjoner (f.eks. at IPPP-metodikken ser ut til å være robust på små, syntetiske datasett, eller at lineære sammenhenger dominerer i denne typen data) og policy-implikasjoner (f.eks. for rapportering i offentlig sektor eller transparens om prioriteringskriterier) er ikke berørt.
- **Uventede funn er underdrøftet.** §8.1 påpeker at logistisk regresjon er en «overraskende sterk baseline» (AUC 0,706 mot XGBoost 0,720) og at RF baseline har påfallende lav recall (0,424). Veiledningen ber spesifikt om at uventede funn løftes fram og forklares. At log.reg nesten matcher XGBoost er metodisk interessant – det antyder at de prediktive sammenhengene i datasettet hovedsakelig er lineære, med implikasjoner både for modellvalg og for tolkningen av syntetisk-data-kritikken i §9.1. §9 går ikke i dybden på dette.
- **Alternative forklaringer på benchmark-gapet er fraværende.** §9.1 lander på datavolum og syntetisk data som «den mest sannsynlige forklaringen». Andre faktorer er ikke vurdert: feature engineering uten window size (anbefalt av Appel et al.), uutnyttede teknikker for klasseubalanse (SMOTE, threshold tuning), eller modeller som ikke ble testet (LightGBM, CatBoost). En balansert drøfting ville nevnt disse alternativene før konklusjonen om datagrunnlaget.
- **Mulig sirkulær validering ved syntetisk data er ikke fullt adressert.** Hvis datasettet er generert med utgangspunkt i variabler primærlitteraturen identifiserer som prediktive, og «Risikokategori leverandør» finnes som forhåndsdefinert variabel i rådata (jf. Tabell 5.1), er det mulig at modellen lærer mønstre som er bygget inn i datageneratoren. §9.3 berører dette overflatisk («syntetisk data har komprimert leverandørvariasjonen»), men sirkulariteten – at modellen kan «bekrefte» det som allerede ligger i datasettet – fortjener en eksplisitt drøfting.
- **Sammenligning med primærstudiene kunne vært tabulert.** §9.1 sammenligner G17s AUC 0,720 med Appel et al. (~0,77–0,80) og Schoonbee et al. (~0,79–0,84) i prosa. En kort tabell med AUC, F1, datasettstørrelse og kontekst på tvers av de tre studiene ville gjort sammenligningen lett å lese og styrket diskusjonens forankring.
- **Overlapp mellom §9.2 og §10.** Tallene 7 %/28 %/55 % per risikogruppe, recall 0,833, og argumentene om at «modellen tilbyr en tredje dimensjon» repeteres i §10. Diskusjonen bør utvikle og tolke; konklusjonen bør oppsummere. Slik det står nå leverer §9.2 mye av det §10 burde gjort.

### Foreslåtte endringer

1. Legg til et åpningsavsnitt eller eget delkapittel i §9 som siterer problemstillingen fra §1.1 og besvarer den punktvis – med klar henvisning til hvilke funn som støtter svaret.
2. Utvid implikasjonsdiskusjonen med teoretiske og policy-relaterte vinkler (f.eks. IPPP-metodikkens robusthet under datafattige forhold, eller transparenskrav i offentlig anskaffelse).
3. Utvid uventede funn til et eget delkapittel: hvorfor er log.reg nesten like god som XGBoost? Hva sier det om datasettet og om modellvalg ved tilsvarende caser?
4. Legg til 1–2 setninger om alternative forklaringer på benchmark-gapet (window size, SMOTE/threshold-tuning, modellvalg) før konklusjonen om datagrunnlaget.
5. Drøft eksplisitt risikoen for sirkulær validering når datasettet er syntetisk og inneholder en forhåndsdefinert «Risikokategori leverandør».
6. Tilføy en kort sammenligningstabell (AUC, F1, datasett, kontekst) for G17 vs. Appel et al. vs. Schoonbee et al.
7. Trim §9.2 slik at konkrete tall og praktiske implikasjoner kan stå i §10 uten å gjentas.

---

## 6 Konklusjon

### Styrker

Konklusjonen besvarer problemstillingen direkte og nøkternt: KI kan brukes til formålet, men forutsetter ekte data for produksjonsrelevant ytelse. Det viktigste funnet – at historisk betalingsatferd er sterkeste prediktor – er klart formulert og forankret eksplisitt i begge primærstudier (Appel et al., 2019; Schoonbee et al., 2022). Konkrete ytelsestall (AUC 0,720, recall 0,833) og separasjonen mellom risikogruppene presenteres ryddig, og avslutningen er praktisk handlingsrettet med tre nummererte anbefalinger til Bedriften: trening på ekte data, kontrollert innfasing og periodisk retrening.

### Forbedringspunkter

- **Begrensninger duplikerer §9.3.** Konklusjonen gjentar i hovedsak de tre punktene fra §9.3 (datasett, konseptdrift, høy andel i høyrisikogruppen) i utvidet form. Konklusjonens oppgave er å peke fremover, ikke re-presentere det diskusjonen allerede har levert.
- **«Bidrag til teori og praksis» er ujevnt utviklet.** Veiledningen ber om begge deler. Praksisbidraget er tydelig (datadrevet prioritering), men det teoretiske bidraget formuleres ikke. Hva har studien lært oss om IPPP-metodikken under datafattige forhold? At log.reg og XGBoost ligger nær hverandre på syntetisk data? At featureviktigheten replikerer Schoonbees funn i en helt annen kontekst? Disse er reelle teoretiske observasjoner som kunne stått eksplisitt.
- **Forslag til videre forskning er praktiske, ikke forskningsorienterte.** De tre anbefalingene er implementeringssteg for Bedriften – ikke forskningsspørsmål forankret i forskningsbakgrunnen. Konkrete forskningsspørsmål kunne vært: hvor lite data trengs for å nå benchmarknivå? Hvor robust er IPPP-metodikken når dataene er syntetiske vs. ekte? Hvilken effekt har klasseubalansetiltak (SMOTE, threshold-tuning, klassevekt) når datavolumet er begrenset?
- **Påstanden om bransjegeneralisering er for sterk.** Siste setning hevder at «tilnærmingen er overførbar til virksomheter på tvers av bransjer og sektorer som håndterer et betydelig fakturavolum». Avgrensingen i §1.3 sa eksplisitt det motsatte («en modell trent på én virksomhets historikk vil ikke uten videre være overførbar»). Generaliseringspåstanden bør modereres eller fjernes.
- **Recall fremheves uten å balansere mot presisjon.** Konklusjonen sier «recall på 0,833 betyr at modellen identifiserer 83 % av faktisk forsinkede fakturaer». Presisjon på 0,495 (Tabell 8.1) – som betyr at omtrent halvparten av flaggene er falske positive – er ikke nevnt. For en innkrever er dette en relevant ressursdimensjoneringsfaktor som bør stå med.
- **Anbefaling 2 er underspesifisert.** «Kontrollert innfasingsperiode» mangler kriterier: hvor lenge, hva som måles, hvilken minste ytelse modellen må oppnå før operativ bruk. Med litt mer konkretisering blir anbefalingen handlingsrettet i praksis.

### Foreslåtte endringer

1. Trim avsnittet om begrensninger til 1–2 setninger som peker tilbake til §9.3, og bruk den frigjorte plassen på fremoverpekende vurderinger.
2. Tilføy et kort delavsnitt som eksplisitt formulerer studiens teoretiske bidrag (overførbarhet av IPPP-metodikken, replikasjon av featureviktighet, observasjoner om lineære vs. ensemble-modeller på syntetisk data).
3. Erstatt deler av «videre forskning»-anbefalingene med faktiske forskningsspørsmål forankret i funnene – f.eks. minimum datavolum, effekten av klasseubalansetiltak, eller transfer learning fra tilstøtende domener.
4. Modererer eller stryk påstanden om bransjegeneralisering, slik at den er konsistent med avgrensingen i §1.3.
5. Suppler recall-formuleringen med presisjonen 0,495 og en kort kommentar om hva det betyr for ressursdimensjoneringen ved oppfølging av høyrisikofakturaer.
6. Konkretiser anbefaling 2 med evalueringskriterier (varighet, nøkkelmetrikker, akseptansegrenser).

---

## 7 Skriveflyt, formelle aspekter og helhetsvurdering

### Styrker

Språket er presist, fagteksten er gjennomgående lesbar, og den overordnede strukturen følger en logisk progresjon (innledning → litteratur → teori → case → metode → modellering → analyse → resultat → diskusjon → konklusjon). APA 7-formatet i §11 er konsistent og korrekt: forfatter-årstall i tekst, hengende innrykk, italic på tidsskrift- og verkstitler, fungerende DOI/URL-er. Tabellene er ryddige – Tabell 2.1, 5.1 og 8.1 er informative og lett lesbare, og Tabell 8.1 fremhever beste modell med fet skrift. Figurene har gjennomgående beskrivende captions som kobler innholdet til primærlitteraturen der det er relevant. Forkortelser som CRISP-DM, IPPP, DSS, EDA og OHE introduseres med full form ved første bruk.

### Forbedringspunkter

- **Sammendrag, Abstract og Innhold er ikke skrevet.** Begge sammendrag er markert «skrives til slutt», og innholdsfortegnelsen er kun en kommentar. Dette er strukturelt påkrevde elementer i en ferdig rapport og må fylles inn før innlevering.
- **Forsideopplysninger er ufullstendige.** Sidetall, innleveringsdato, studiepoeng og veileder er tomme. Disse må på plass for at forsiden skal fungere som identifikator.
- **Dobbel «Figur 1».** Samme figur (klasseubalanse) settes inn både i §5.2 og §7.1 med samme nummer – kryssreferansen blir tvetydig. Hver figur skal ha unikt nummer; gjenbruk håndteres ved kryssreferanse, ikke ny innsetting.
- **Inkonsistent figurnummerering.** Captions i §8 sier «Figur 12», «Figur 13», «Figur 14» for henholdsvis presisjon/recall/F1, konfusjonsmatrise og feature importance, men de underliggende filnavnene har et annet nummerskjema (`12_konfusjonsmatrise.png`, `13_feature_importance.png`, `14_presisjon_recall_f1.png`). Visningen i rapporten er konsistent, men avviket mellom captions og filnavn er en kilde til feil ved senere redigering.
- **Tabeller i §6.1 mangler nummerering.** «Datobaserte og betalingsbetingelsesfeatures» og «One-hot-enkoding»-tabellen står uten Tabell-nummer, mens andre tabeller (2.1, 5.1, 8.1) er nummerert. Konsistens krever at også disse får nummer (f.eks. Tabell 6.1 og 6.2).
- **Kapittellengden er ujevn.** §4.0 er fire korte avsnitt uten figurer/tabeller, mens §7 og §8 til sammen utgjør en stor del av rapporten. Casekapittelet bør utvides og deler av analysekapittelet kunne vært slått sammen med modellering/resultat for jevnere fordeling.
- **§6 og §7 har overlappende formål.** «Modellering» og «Analyse» er to kapitler som dels overlapper i hva de leverer (§6 beskriver feature engineering og hyperparametersøk, §7 EDA og leverandørprofil). En sammenslåing eller tydeligere arbeidsdeling ville gjort strukturen klarere.
- **Originaliteten er primært kontekstuell.** Studien anvender en etablert metodikk fra Appel et al. og Schoonbee et al. på et norsk syntetisk datasett. Det metodiske bidraget utover primærlitteraturen er begrenset og ikke eksplisitt formulert noe sted i rapporten. Dette er ikke en formell mangel – men det er noe en helhetsvurdering må erkjenne, og som §2 og §10 kan adressere ved å være tydelige på hva studien bidrar med.

### Foreslåtte endringer

1. Skriv Sammendrag (norsk) og Abstract (engelsk) på 8–15 linjer hver med problem, metode, hovedfunn og konklusjon.
2. Generer Innholdsfortegnelse fra strukturen.
3. Fyll inn forsideopplysninger: totalt antall sider, innleveringsdato, studiepoeng og veileder.
4. Slett dupliseringen av Figur 1 mellom §5.2 og §7.1 – la figuren stå én gang og kryssreferer fra det andre kapitlet.
5. Forny figurfilenes navn til å samsvare med caption-nummerering, eller endre captions slik at numrene matcher filnavnene (sistnevnte er mindre invasivt hvis filnavnene ligger i rapportkjeden).
6. Nummerer tabellene i §6.1 (Tabell 6.1 «Datobaserte features», Tabell 6.2 «One-hot-kategorier»).
7. Utvid §4.0 med deskriptive nøkkeltall og figurer fra §7.1 som hører hjemme i casekapitlet, slik at §7 frigjør plass til ren modell-/resultatpresentasjon.
8. Tydeliggjør studiens originalitet i §2.4 (forskningsgap) og i §10 (teoretisk bidrag) – ikke ved å overdrive bidraget, men ved å være eksplisitt på *hva* som er bidraget i konteksten.
