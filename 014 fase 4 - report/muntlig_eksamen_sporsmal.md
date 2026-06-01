# Muntlig eksamen – mulige spørsmål med utfyllende svar (LOG650, gruppe G19)

Spørsmål vi kan få under spørrerunden, sortert i fire vanskelighetsgrader. Hvert
spørsmål har et **utfyllende svar** med begrunnelse, tall og henvisning til
rapportens kapitler/tabeller. Tallene er hentet fra den endelige rapporten
`rapport_post_review`.

**Kjernetall å kunne utenat:** RMSE tuned RF 578,26 · MAPE 43,97 % · vinner RMSE
i 11/12 måneder og 13/14 segmenter · Discount 11,48 % · kalender ~42 % av topp 10
· 9 994 transaksjoner · 67 features · trening 2022–2024 (6 682 rader) / test 2025
(3 312 rader).

---

## Grad 1 – Grunnleggende (forståelse av hva dere har gjort)

**1. Hva er problemstillingen i prosjektet?**

Problemstillingen er: *Hvordan kan multippel lineær regresjon og Random Forest
Regressor brukes til å forutsi salg for 2025 for en simulert dagligvarekjede, og
hvilke faktorer påvirker salget mest?* Den er todelt med vilje. Delproblem 1 er
**modellvalg og prognoseytelse** – hvordan de to modellklassene sammenlignes på
2025-data målt med RMSE (primær) og MAPE (sekundær), både samlet, månedlig og på
tvers av segmenter. Delproblem 2 er **variabelanalyse** – hvilke
forklaringsvariabler som har størst prediksjonsverdi, og hvordan
importance-rangeringen fra Random Forest samsvarer med koeffisientene i den
lineære modellen. Hele rapporten er bygget for å svare presist på disse to – verken
mer eller mindre.

**2. Hvilke modeller har dere brukt, og hvorfor akkurat disse to?**

Vi bruker multippel lineær regresjon og Random Forest Regressor. Lineær regresjon
er valgt som **tolkbar benchmark**: koeffisientene gir direkte retning og størrelse
på effektene, og den måler hvor langt en enkel, lineær spesifikasjon kommer på
dette caset. Random Forest er valgt som **fleksibel, ikke-lineær alternativmodell**
som kan fange opp mønstre og interaksjoner en lineær modell ikke ser, og som i
tillegg leverer en naturlig feature importance-rangering. Nettopp den rangeringen
besvarer delproblem 2 direkte. Kombinasjonen gir altså både et tolkbart
referansepunkt og et mål på hva man vinner ved en mer fleksibel modell.

**3. Hva er datagrunnlaget?**

Datasettet er `Dagligvare_Dataset.csv` med 9 994 daglige salgstransaksjoner fra
en simulert dagligvarekjede. Kjeden opererer i fem regioner (West, East, Central,
South, North), med syv produktkategorier fordelt på 23 subkategorier, og 24 byer.
Rådata dekket opprinnelig 2015–2018, men er remappet med en sjuårig
kalenderforskyvning til prosjektperioden 2022–2025. Datakvaliteten er god: 11
råkolonner, ingen manglende verdier og ingen dubletter. Det eneste reelle
rensebehovet var to ulike datoformater (4 042 rader med bindestrek, 5 952 med
skråstrek) som ble standardisert til ISO-format. Dette er dokumentert i Tabell 5.3.

**4. Hva er målvariabelen, og hva er de viktigste forklaringsvariablene?**

Målvariabelen er `Sales` – et heltall i spennet 500 til 2 500. Forklaringsvariablene
er `Discount` (desimaltall, 0,10–0,35), de kategoriske variablene `Category`,
`Sub Category`, `City` og `Region`, og sju kalendervariabler vi utledet selv fra
`Order Date`: `year`, `month`, `quarter`, `weekofyear`, `dayofweek`, `dayofmonth`
og `is_weekend`. Etter one-hot-koding av de kategoriske variablene endte
modellmatrisen på 67 features. Variabeloversikten ligger i Tabell 5.1 og
feature engineering-oppsettet i Tabell 5.2.

**5. Hvilken modell anbefaler dere, og hva er hovedfunnet?**

Hovedfunnet er at **tuned Random Forest er den samlet beste modellen** på 2025
med RMSE 578,26 og MAPE 43,97 %, og den vinner RMSE i 11 av 12 måneder og 13 av 14
segmenter. Men anbefalingen er bevisst **differensiert**, ikke «én vinner tar alt».
Vi anbefaler tuned RF som standardprognose for innkjøp, lager og aggregert
ressursplanlegging; benchmark lineær som forklaringsstøtte og som supplement i
toppbelastningssituasjoner (der den faktisk er best); og baseline RF som kontroll
mot prosentfeil i perioder med høy rabatt. Dette er oppsummert i beslutningsmatrisen
i Tabell 9.2.

**6. Hva er RMSE og MAPE, og hvilken er primær?**

RMSE (Root Mean Squared Error) måler gjennomsnittlig størrelse på prognosefeilen i
samme enhet som salget. Fordi feilene kvadreres, straffes store avvik hardere enn
små. Vi bruker RMSE som **primær** metrikk fordi absolutt presisjon – å treffe
riktig salgsvolum – er det mest relevante for innkjøp og lagerstyring. MAPE (Mean
Absolute Percentage Error) måler gjennomsnittlig prosentvis avvik; den er
skalanøytral og lett å kommunisere, men blir ustabil når faktiske volum er nær null
(divisjon mot små tall). Derfor er MAPE **sekundær**. At de to målene vekter feil
ulikt, er nettopp grunnen til at de ikke alltid peker på samme vinner (kap. 3.3).

---

## Grad 2 – Middels (metodevalg og begrunnelser)

**7. Hvorfor splittet dere på tid i stedet for tilfeldig?**

Fordi en tilfeldig splitt ville latt observasjoner fra framtiden havne i
treningssettet. Modellen ville da «sett framover» under trening, noe som gir
kunstig god ytelse og ikke speiler den reelle oppgaven – å forutsi en periode man
ennå ikke kjenner. Med tidsbasert splitt trener vi på 2022–2024 og tester på 2025,
slik at evalueringen etterligner en ekte prognosesituasjon. At gjennomsnittlig
salgsnivå er nær identisk i de to periodene (1 493 i trening mot 1 503 i test)
støtter antakelsen om at historiske mønstre er overførbare til 2025 (kap. 5.2,
Tabell 5.4).

**8. Hvordan tunet dere Random Forest, og hvordan unngikk dere lekkasje der?**

Vi gjorde et rutenettsøk (grid search) der hver kandidatkonfigurasjon ble trent på
2022–2023 (4 095 rader) og validert på 2024 (2 587 rader). 2025 ble holdt helt
utenfor hele utvelgelsen – den tidsmessige isolasjonen er det som forhindrer
lekkasje mellom tuning og evaluering. Vinnerkonfigurasjonen ble `n_estimators=400`,
`max_depth=10`, `min_samples_leaf=4` og `max_features='sqrt'`, valgt med
validerings-RMSE som kriterium (577,27 mot baseline-kandidatens 590,30 på samme
valideringssett – en forbedring på 13,04 enheter). Deretter retrente vi vinneren på
hele treningsperioden 2022–2024 før vi evaluerte på 2025. Dette er beskrevet i
kapittel 6 med topp 5-kandidatene i Tabell 6.2.

**9. Hvorfor ekskluderte dere `Profit`?**

`Profit` er en lekkasjevariabel. Den er bare kjent **etter** at salget er
gjennomført, og ville derfor ikke vært tilgjengelig på det tidspunktet man faktisk
skal lage en prognose. Hadde vi tatt den med, ville modellen «jukset» ved å bruke
informasjon fra framtiden, og ytelsen ville blitt kunstig god uten å være brukbar
i praksis. Datalekkasje er nettopp det å inkludere variabler som ikke ville vært
kjent på prediksjonstidspunktet (kap. 3.4 og 5.2).

**10. Hvorfor ble `State`, `Order ID` og `Customer Name` tatt ut?**

`State` ble tatt ut fordi kolonnen er **konstant** i datasettet (kun én unik verdi)
og dermed ikke har noen forklaringskraft. `Order ID` har 9 994 unike verdier – én
per rad – og er en ren identifikator uten generaliserbar prediksjonsverdi.
`Customer Name` har høy kardinalitet (50 navn) og høy risiko for overtilpasning:
modellen ville lære navn i stedet for mønstre. Ingen av disse bidrar med noe
generaliserbart signal, og de er begrunnet i Tabell 5.1 og 5.2.

**11. Hva er feature engineering i deres prosjekt?**

Feature engineering er å utlede nye, mer informative variabler fra rådata. Hos oss
består det av to grep. For det første utledet vi sju kalendervariabler fra
`Order Date` (`year`, `month`, `quarter`, `weekofyear`, `dayofweek`, `dayofmonth`,
`is_weekend`), som gjør sesong-, uke- og kvartalsmønstre tilgjengelige for modellen
– mønstre man ikke kan lese direkte fra en rå dato. For det andre one-hot-kodet vi
de kategoriske variablene til binære dummyvariabler, fordi lineær regresjon krever
numerisk input, og vi brukte samme kodede matrise for Random Forest for å holde
sammenligningen konsistent. Resultatet er 67 features (kap. 3.4 og 5.2).

**12. Hvorfor er det 67 features?**

Antallet kommer hovedsakelig fra one-hot-kodingen. Hver kategori i en kategorisk
variabel blir en egen binær kolonne: 7 produktkategorier, 23 subkategorier, 24 byer
og 5 regioner gir til sammen mange dummyvariabler. I tillegg kommer `Discount` og
de sju kalendervariablene. Summen av alt dette er 67 features i den endelige
modellmatrisen, og samme matrise brukes for alle tre modellsporene (Tabell 6.1).

**13. Hvordan måler Random Forest hvilke variabler som er viktigst?**

Random Forest beregner feature importance som **gjennomsnittlig reduksjon i MSE**
(Mean Decrease in Impurity) på tvers av alle trærne og alle splittene i skogen. En
variabel som gang på gang brukes til å dele dataene på en måte som reduserer
prediksjonsfeilen, får høy importance. Det er verdt å merke seg at denne
importance-en ikke har fortegn – den sier *hvor mye* en variabel betyr, ikke i
*hvilken retning* den virker. Det er en viktig forskjell fra koeffisientene i lineær
regresjon (kap. 3.2).

**14. Hva betyr det at funnene er prediktive og ikke kausale?**

Det betyr at variabelrangeringene og koeffisientene forteller hvilke signaler som
er *nyttige for å forutsi* salget, men ikke *hvorfor* salget endrer seg. At
`Discount` er sterkt assosiert med salg, betyr ikke nødvendigvis at rabatt
forårsaker salgsendringen – det kan ligge bakenforliggende mønstre bak. Kausale
slutninger krever eksperimentelt design (f.eks. kontrollerte forsøk), som ligger
utenfor prosjektets ramme (avgrensning i kap. 1.3). Dette er et viktig forbehold
når resultatene oversettes til beslutninger, særlig i kampanje- og rabattarbeid.

---

## Grad 3 – Vanskelig (kritisk tolkning og nyanser)

**15. Tuned RF vinner 11 av 12 måneder, men gapet er «marginalt». Forklar.**

Dette er en tilsynelatende motsetning som vi mener er viktig å forstå. Samlet for
2025 er tuned RF bare ~2 RMSE-enheter bedre enn benchmark lineær (578,26 mot
580,39) og ~11 enheter bedre enn baseline RF. Når tuned RF likevel vinner 11 av 12
måneder, betyr det at den er *konsistent* litt bedre måned for måned, men at
forspranget i hver enkelt måned er lite. «Best samlet» handler i praksis om
absolutt presisjon i månedene med store salgsvolum, der RMSE straffer bom hardest.
At den vinner mange måneder er altså ikke det samme som å vinne stort – noe vi er
eksplisitte på i diskusjonen (kap. 9.1, Tabell 9.1).

**16. Hvorfor peker RMSE og MAPE ofte på forskjellig vinner?**

Fordi de to målene vekter feil helt ulikt. RMSE kvadrerer avvikene og straffer
dermed store absolutte bom hardt – den favoriserer modellen som treffer best på de
store salgsvolumene. MAPE måler prosentvis feil og blir derfor svært følsom på
lavvolumrader, der selv et lite absolutt avvik gir en høy prosent. En modell kan ha
lavt RMSE (treffer godt på store volum) uten å ha lavt MAPE (bommer prosentvis på
små volum), og omvendt. Konkret peker RMSE og MAPE på samme vinner kun i juli og
september i vårt materiale. Baseline RF vinner for eksempel MAPE i 6 måneder uten å
vinne RMSE en eneste måned (Tabell 7.1, 8.2).

**17. `Discount` har negativt fortegn i lineær regresjon, men er #1 i RF feature
importance. Er det en selvmotsigelse?**

Nei, og dette er et av de mest interessante funnene. RF-importance har ikke fortegn
– den sier bare at `Discount` (11,48 %) er det signalet modellen oftest bruker for
å redusere feilen. Den lineære koeffisienten er derimot negativ (−166,35), altså at
høyere rabatt isolert sett trekker prediksjonen ned. At de to «spriker» tolker vi
som et tegn på at sammenhengen mellom rabatt og salg er **ikke-lineær eller
betinget** – for eksempel at rabatteffekten avhenger av produktkategori eller
sesong. En lineær modell tvinges til å oppsummere alt dette med ett enkelt fortegn
og overkompenserer, mens Random Forest kan fange opp flere betingede mønstre
samtidig. Det er altså ikke motstridende funn, men to modeller som svarer ulikt på
det samme underliggende signalet (kap. 7 og 9.2).

**18. MAPE er ~44 %. Er ikke det en dårlig modell?**

Tatt ut av kontekst høres 44 % høyt ut – operative benchmarks i varehandel regner
gjerne under 20 % som brukbart for daglige prognoser. Men vi mener tallet må forstås
i lys av datagrunnlaget. På dagsnivå er variansen høy (standardavvik 578 på et snitt
på 1 497), og MAPE er per definisjon ustabil når faktiske volum er små, fordi man
deler på et lite tall. Det ser vi tydelig i segmentanalysen: i «lavt salg» er MAPE
~90 %, mens i «middels salg» er den bare ~11 %. Den praktiske verdien ligger derfor
mer i den **relative rangeringen** mellom modellene og i segmentanalysen enn i det
absolutte MAPE-nivået. For operativ bruk anbefaler vi dessuten å aggregere til uke-
eller månedsnivå, der enkeltdagers prosentavvik glattes ut (kap. 9.4).

**19. Alle tre modellene underestimerer i august–september. Hva betyr det?**

Det er et systematisk bias-mønster: tuned RF underestimerer august med −5,22 %
(−20 548 salgsenheter) og september med −2,77 %, mens november og desember er lett
overestimert (+1,05 % og +2,36 %). Det avgjørende poenget er at mønsteret er
**konsistent på tvers av alle tre modellsporene**. Det peker på en begrensning i
selve sesongsignalet i dataene, ikke på en svakhet ved én bestemt modell. Den mest
sannsynlige forklaringen er at vi bare har tre treningsår (2022–2024), noe som gir
lite rom for å lære årlige avvik i samme måned – hvis 2025 har en sterkere
høstoppgang enn treningsårene, vil kalendervariablene ikke fange den, og modellen
glatter ut nivået. En sekundær forklaring er at vi mangler eksplisitte kampanje-
eller eventvariabler utover `Discount` (kap. 7, Figur 7.1).

**20. Lineær regresjon er best i «høyt salg»-segmentet. Hvorfor er ikke det et
problem for anbefalingen?**

Det er ikke et problem, det er nettopp derfor anbefalingen er differensiert. I
segmentet for høyt salgsnivå er benchmark lineær best på begge metrikker (RMSE
699,10 og MAPE 30,31 %). I stedet for å overse dette har vi bygd det inn i
beslutningsmatrisen: tuned RF er standardvalget, men benchmark lineær trekkes inn
som kontroll/supplement når man planlegger for toppbelastning og de aller høyeste
salgsvolumene. Poenget er at modellvalg bør tilpasses bruksområdet, ikke at én
modell skal vinne alt (kap. 9.1 og 9.4, Tabell 9.2).

**21. Lineær regresjon ble kjørt uten regularisering på 67 features. Hvilken risiko
gir det?**

Den største risikoen er **multikollinearitet**. Med 67 features, der mange er
one-hot-kodede dummyvariabler, blir flere forklaringsvariabler innbyrdes korrelert.
Uten regularisering (ingen ridge/lasso) gjør det enkeltkoeffisientene ustabile og
vanskelige å tolke som rene effektmål – små endringer i data kan gi store endringer
i koeffisientene. Det svekker *tolkningsvaliditeten*, men ikke nødvendigvis
*prediksjonskraften*. Nettopp derfor bruker vi den lineære modellen til å indikere
retning og som forklaringsstøtte, ikke som et stabilt, kausalt effektmål (kap. 9.5,
Tabell 9.3).

**22. `Region_North`-koeffisienten er størst i tallverdi (−277). Hvorfor vektlegger
dere den ikke?**

Fordi North-regionen er representert med bare **én enkelt observasjon** i hele
datasettet. En koeffisient estimert på ett datapunkt er ekstremt usikker og kan
ikke tolkes som en reell, substansiell regioneffekt – den er i praksis støy. Vi
behandler den derfor som usikkerhet og bruker den ikke som analytisk poeng. Det er
også grunnen til at North ikke brukes som eget analysesegment i segmentanalysen
(kap. 5.2 og 9.2).

**23. Tuning brukte bare 2024 som valideringsår. Hva er svakheten?**

Svakheten er at modellvalget reflekterer mønstrene i **ett enkelt år**. Vi har ikke
gjort en mer robust kryssvalidering over flere perioder, så vi vet ikke hvor følsomt
valget av hyperparametere er for andre valideringsvinduer. Hadde vi for eksempel
validert mot 2023 i stedet, kunne en annen konfigurasjon vunnet. Modellvalget er
fullt etterprøvbart og dokumentert, men sensitiviteten for valg av valideringsperiode
er en reell begrensning – og vi har eksplisitt foreslått bredere validering som
videre arbeid (kap. 9.5 og 9.6).

---

## Grad 4 – Ekspert / utfordrende oppfølging

**24. Hva er forskningsbidraget – hva tilfører dere utover caset?**

Bidraget er en **kontrollert empirisk sammenligning** av to modellfamilier på ett
simulert dagligvaredatasett, der trening, validering og test er strengt adskilt i
tid, og der vi rapporterer ytelse på flere nivåer: samlet, per måned, per segment
(kvartal, rabattband, region, salgsnivå) og som bias-mønster. Det viktigste faglige
poenget er at vi dokumenterer at **ensemble-fordelen kan være marginal på totalnivå**
selv når Random Forest vinner det store flertallet av måneder og segmenter. Det
nyanserer en utbredt forventning om at maskinlæring «alltid» slår enklere metoder.
Forskningsgapet vi adresserer er beskrevet i kapittel 2 (litteratur).

**25. Hvorfor ble ensemble-gevinsten så liten her, og når ville den vært større?**

Fordi forutsetningene som gir Random Forest et stort fortrinn bare delvis er
oppfylt i dette caset. Datasettet har relativt lav strukturell ikke-linearitet,
moderat størrelse (~7 700 treningsrader når man teller 2022–2024) og domineres av
sterke, enkle signaler – rabatt og kalendervariabler. Ensemble-metoder gir størst
gevinst når mønstrene er komplekse og ikke-lineære og når datamengden er stor.
Carbonneau et al. (2008) finner tilsvarende at maskinlæring slår tradisjonelle
metoder tydeligst der etterspørselsmønsteret er komplekst og dataene rike. Vårt
bidrag er et empirisk eksempel der disse forutsetningene bare delvis holder, og der
gevinsten derfor blir liten på samlemålene (kap. 9.3).

**26. Hvordan ville dere validert at modellen faktisk er nyttig for Dagligvare i
praksis?**

Flere grep. For det første aggregere prognosene til uke- eller månedsnivå, der
prosentfeilen er mer stabil og mer relevant for innkjøp. For det andre teste
modellene mot **reelle** salgsdata fra en faktisk dagligvarekjede, ikke bare det
simulerte settet. For det tredje sammenligne mot en enkel, naiv baseline (for
eksempel «samme som fjorårets måned») for å vise at modellen gir reell merverdi.
For det fjerde kostnadsvekte feilene – over- og underbestilling har ulik kostnad –
og kombinere prognosene med lokal fagkunnskap før de blir operative beslutninger
(kap. 9.4 og 9.6).

**27. Hvis dere skulle videreutvikle – hva ville dere gjort først, og hvorfor?**

Førsteprioritet ville vært å angripe de to tydeligste svakhetene: det systematiske
høstbiaset (august–september) og den heterogene MAPE-en. Konkret ville vi utvidet
modellomfanget til tidsrekke- og gradient boosting-metoder, som kan håndtere
sesongstruktur og ikke-lineære mønstre mer presist. Deretter en sensitivitetsanalyse
av de viktigste signalene – særlig `Discount` og regionvariablene – og bredere
validering over flere år i stedet for bare 2024. Vi ville også supplert med
fagfellevurderte kilder innen etterspørselspredikering i dagligvare for å styrke
metodevalg og tolkning (kap. 9.6).

**28. Dere mangler en naiv baseline (f.eks. «samme som i fjor»). Er sammenligningen
da rettferdig?**

Det er et betimelig poeng, og vi vil være ærlige på det. Lineær regresjon fungerer
som vår tolkbare referanse, og baseline Random Forest viser hva en utuned
ensemble-modell leverer. Men en ren naiv baseline – som å gjenta fjorårets nivå –
ville styrket vurderingen av om modellene faktisk gir merverdi utover det trivielle.
Vi mener fortsatt sammenligningen mellom de tre sporene er gyldig på sine egne
premisser, men en naiv referanse er en svakhet vi anerkjenner og som vi ville lagt
til ved videre arbeid. Det å eie denne begrensningen er bedre enn å overselge.

**29. Kunne dere ikke bare brukt en tidsrekkemodell (ARIMA o.l.) på et
salgsprognoseproblem?**

Vi avgrenset bevisst til to modellfamilier – lineær regresjon og Random Forest – i
tråd med prosjektets faglige ramme, og tidsrekkemodeller er nevnt eksplisitt som
videre arbeid. Det er også en strukturell grunn: oppsettet vårt er
tverrsnitts-/feature-basert, der hver rad er en transaksjon med rabatt, region og
kategori, ikke én aggregert tidsserie per dag. En klassisk ARIMA-modell forutsetter
en jevn, aggregert serie og utnytter ikke de kategoriske dimensjonene på samme måte.
Det ville altså vært en annen problemformulering, og et naturlig neste steg snarere
enn noe vi har utelatt ved en feil (kap. 1.3 og 9.6).

**30. Hvordan har dere brukt KI-verktøy i prosjektet, og hvordan sikrer dere faglig
integritet?**

Bruken av kunstig intelligens som verktøy i analyse- og rapportarbeidet er åpen og
dokumentert i prosjektets endringslogg og i den obligatoriske egenerklæringen.
Gruppen har skrevet og godkjent rapporten i fellesskap, og vi står faglig inne for
innholdet. På den tekniske siden er integriteten sikret gjennom reproduserbarhet:
analysen er organisert som aktivitetsbaserte skript med faste seeds, slik at
resultatene kan etterprøves. KI er altså et verktøy i prosessen, ikke en erstatning
for vår egen faglige vurdering (kap. 5.3).

**31. Hvor reproduserbart er arbeidet?**

Høyt. Analysen er organisert som aktivitetsbaserte skript under `006 analysis/`,
med faste seeds for Random Forest (`random_state=42`) og uten ad-hoc-manipulering
av treningsgrunnlaget mellom aktiviteter. Hele pipelinen – fra rådata via rensing,
feature engineering og modelltrening til de endelige metrikkene – kan kjøres på
nytt og gi de samme tallene. Detaljerte underlag (radvise prognoser, full
tuning-grid, full feature importance, koeffisienttabell) ligger som vedlegg A1–A7
(kap. 5.3 og 12).

---

## Tips til spørrerunden

- **Eier dere usikkerheten:** På kritiske spørsmål (naiv baseline, ett
  valideringsår, høy MAPE) er det styrke å innrømme begrensningen og vise at dere
  har tenkt på den – det er ofte nettopp det sensor leter etter. Forsøk ikke å
  bortforklare reelle svakheter.
- **Bruk tallene presist:** Et konkret tall (RMSE 578, 11/12 måneder) virker mer
  overbevisende enn «den var litt bedre». Men ikke bløff på desimaler – si «rundt
  44 prosent» hvis dere er usikre.
- **Pek tilbake til problemstillingen:** Knytt svaret til de to delproblemene når
  det passer – det viser at dere har en rød tråd.
- **Skill prediktivt fra kausalt:** Flere spørsmål kan «lokke» dere til å si at en
  variabel *forårsaker* salg. Hold fast ved at funnene er prediktive.
- **Fordel temaene:** Avtal gjerne på forhånd hvem som tar metode, hvem som tar
  resultater og hvem som tar tolkning/begrensninger – samme inndeling som intro.
