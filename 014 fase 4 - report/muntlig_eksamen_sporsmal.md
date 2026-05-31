# Muntlig eksamen – mulige spørsmål med svarstikkord (LOG650, gruppe G19)

Spørsmål vi kan få under spørrerunden, sortert i fire vanskelighetsgrader. Hvert
spørsmål har korte **svarstikkord** – ikke et ferdig manus, men nok til å øve og
huske kjernen. Tallene er hentet fra den endelige rapporten `rapport_post_review`.

**Kjernetall å kunne utenat:** RMSE tuned RF 578,26 · MAPE 43,97 % · vinner RMSE
i 11/12 måneder og 13/14 segmenter · Discount 11,48 % · kalender ~42 % av topp 10
· 9 994 transaksjoner · 67 features · trening 2022–2024 (6 682 rader) / test 2025
(3 312 rader).

---

## Grad 1 – Grunnleggende (forståelse av hva dere har gjort)

1. **Hva er problemstillingen i prosjektet?**
   - Hvordan kan multippel lineær regresjon og Random Forest brukes til å forutsi
     salg for 2025 for en simulert dagligvarekjede, og hvilke faktorer påvirker
     salget mest? To delproblemer: modellsammenligning + variabelanalyse.

2. **Hvilke modeller har dere brukt, og hvorfor akkurat disse to?**
   - Lineær regresjon som tolkbar benchmark; Random Forest som fleksibel,
     ikke-lineær modell med naturlig feature importance. Lineær viser hvor langt
     en enkel modell kommer; RF svarer direkte på delproblem 2.

3. **Hva er datagrunnlaget?**
   - 9 994 daglige salgstransaksjoner, simulert kjede «Dagligvare», 2022–2025,
     5 regioner, 7 kategorier, 24 byer. Ingen manglende verdier/dubletter.

4. **Hva er målvariabelen, og hva er de viktigste forklaringsvariablene?**
   - Mål: `Sales` (500–2 500). Forklaring: `Discount`, kategoriske (region,
     kategori, subkategori, by) og 7 utledede kalendervariabler.

5. **Hvilken modell anbefaler dere, og hva er hovedfunnet?**
   - Tuned Random Forest som standardprognose (best samlet, RMSE 578,26). Men
     differensiert: lineær som forklaringsstøtte/toppbelastning, baseline RF som
     MAPE-kontroll ved høy rabatt.

6. **Hva er RMSE og MAPE, og hvilken er primær?**
   - RMSE = absolutt feil i salgsenheter (primær – innkjøp trenger absolutt
     presisjon). MAPE = prosentvis feil (sekundær – lettere å kommunisere, men
     ustabil ved små volum).

---

## Grad 2 – Middels (metodevalg og begrunnelser)

7. **Hvorfor splittet dere på tid i stedet for tilfeldig?**
   - Tilfeldig splitt ville latt framtidige observasjoner inngå i treningen →
     datalekkasje og kunstig god ytelse. Tidssplitt speiler reell prognose
     framover.

8. **Hvordan tunet dere Random Forest, og hvordan unngikk dere lekkasje der?**
   - Rutenettsøk med trening på 2022–2023 og validering på 2024. 2025 holdt helt
     utenfor. Vinner retrenes på hele 2022–2024 før testing på 2025.
   - Vinnerparametere: `n_estimators=400`, `max_depth=10`, `min_samples_leaf=4`,
     `max_features='sqrt'`.

9. **Hvorfor ekskluderte dere `Profit`?**
   - Lekkasjevariabel – kjent først etter at salget er gjennomført, ville ikke
     vært tilgjengelig på prognosetidspunktet.

10. **Hvorfor ble `State`, `Order ID` og `Customer Name` tatt ut?**
    - `State`: konstant kolonne, null forklaringskraft. `Order ID`/`Customer
      Name`: høy kardinalitet, ingen generaliserbar prediksjonsverdi, fare for
      overtilpasning.

11. **Hva er feature engineering i deres prosjekt?**
    - Utledet 7 kalendervariabler fra `Order Date` (year, month, quarter,
      weekofyear, dayofweek, dayofmonth, is_weekend) + one-hot-koding av
      kategoriske → 67 features totalt.

12. **Hvorfor er det 67 features?**
    - One-hot-koding av kategoriske variabler (mange regioner/kategorier/
      subkategorier/byer) + kalendervariabler + Discount.

13. **Hvordan måler Random Forest hvilke variabler som er viktigst?**
    - Feature importance = gjennomsnittlig reduksjon i MSE (Mean Decrease in
      Impurity) over alle trær og splitter. Variabel som ofte reduserer feilen
      rangeres høyt.

14. **Hva betyr det at funnene er prediktive og ikke kausale?**
    - Variablene forteller hva som *forutsier* salg, ikke *hvorfor* det endrer
      seg. Kausalitet krever eksperimentelt design – utenfor prosjektets ramme.

---

## Grad 3 – Vanskelig (kritisk tolkning og nyanser)

15. **Tuned RF vinner 11 av 12 måneder, men gapet er «marginalt». Forklar.**
    - Samlet RMSE bare ~2 enheter bedre enn lineær. «Best» handler om absolutt
      presisjon i måneder med store volum. MAPE er fortsatt heterogen –
      tuned RF vinner bare 3 måneder på MAPE.

16. **Hvorfor peker RMSE og MAPE ofte på forskjellig vinner?**
    - RMSE straffer store absolutte avvik hardt (favoriserer treff på store
      volum). MAPE er sensitiv på lavvolumrader der små avvik gir store prosent.
      Ulik vekting → ulik vinner.

17. **`Discount` har negativt fortegn i lineær regresjon, men er #1 i RF
    feature importance. Er det en selvmotsigelse?**
    - Nei. RF-importance har ikke fortegn – den måler kun betydning. Negativt
      lineært fortegn tyder på at rabatt–salg-sammenhengen er ikke-lineær eller
      betinget (avhenger av kategori/sesong). Lineær overkompenserer med ett
      fortegn; RF fanger flere betingede mønstre.

18. **MAPE er ~44 %. Er ikke det en dårlig modell?**
    - Høyt mot operative benchmarks (<20 %), men forventet på dagsnivå med høy
      varians (std 578, snitt 1 497). MAPE er ustabil ved små volum. Verdien
      ligger i relativ rangering + segmentanalyse, og man bør aggregere til
      uke/måned for innkjøp.

19. **Alle tre modellene underestimerer i august–september. Hva betyr det?**
    - Systematisk bias konsistent på tvers av modeller → peker på begrensning i
      *sesongsignalet i dataene*, ikke i enkeltmodellen. Sannsynlig årsak: bare
      3 treningsår gir lite rom for å lære årlige avvik; mulig høstoppgang i 2025
      som kalendervariablene ikke fanger.

20. **Lineær regresjon er best i «høyt salg»-segmentet. Hvorfor er ikke det et
    problem for anbefalingen?**
    - Derfor er anbefalingen differensiert: lineær trekkes inn som supplement
      ved toppbelastning. Modellvalg tilpasses bruksområde, ikke én vinner for
      alt (jf. beslutningsmatrisen, Tabell 9.2).

21. **Lineær regresjon ble kjørt uten regularisering på 67 features. Hvilken
    risiko gir det?**
    - Multikollinearitet fra mange one-hot-dummyer → svekker tolkningsvaliditet
      av enkeltkoeffisienter (men ikke nødvendigvis prediksjonskraft). Derfor
      brukes lineær til retning/forklaring, ikke som stabilt effektmål.

22. **`Region_North`-koeffisienten er størst i tallverdi (−277). Hvorfor
    vektlegger dere den ikke?**
    - North har bare én observasjon i datasettet → usikkerhet, ikke en reell
      regioneffekt. Tolkes som støy.

23. **Tuning brukte bare 2024 som valideringsår. Hva er svakheten?**
    - Modellvalget reflekterer mønstrene i ett år, ikke robust kryssvalidering
      over flere perioder. Sensitivitet for andre valideringsvinduer er ikke
      testet.

---

## Grad 4 – Ekspert / utfordrende oppfølging

24. **Hva er forskningsbidraget – hva tilfører dere utover caset?**
    - Kontrollert empirisk sammenligning av to modellfamilier på ett datasett
      med streng tidsbasert splitt, der både samlede, månedlige, segmentvise og
      bias-mål rapporteres. Viser at ensemble-fordelen kan være marginal på
      totalnivå selv når RF vinner de fleste måneder/segmenter.

25. **Hvorfor ble ensemble-gevinsten så liten her, og når ville den vært større?**
    - Datasettet har lav strukturell ikke-linearitet, moderat størrelse
      (~7 700 treningsrader) og dominerende kalender-/rabattsignaler. RF gir
      størst gevinst ved komplekse, ikke-lineære mønstre og rike/store data
      (jf. Carbonneau et al., 2008).

26. **Hvordan ville dere validert at modellen faktisk er nyttig for Dagligvare i
    praksis?**
    - Aggregere til uke/måned, teste mot reelle salgsdata, måle mot en naiv
      baseline (f.eks. fjorårets nivå), kombinere med lokal fagkunnskap,
      kostnadsvekte over-/underbestilling.

27. **Hvis dere skulle videreutvikle – hva ville dere gjort først, og hvorfor?**
    - Adressere høstbias og heterogen MAPE: utvide til tidsrekke-/gradient
      boosting-metoder, sensitivitetsanalyse av Discount/region, bredere
      validering over flere år, supplere med fagfellevurderte kilder.

28. **Dere mangler en naiv baseline (f.eks. «samme som i fjor»). Er
    sammenligningen da rettferdig?**
    - Ærlig svar: lineær regresjon fungerer som tolkbar referanse, men en ren
      naiv baseline ville styrket vurderingen av om modellene gir reell merverdi.
      Et godt punkt for videre arbeid.

29. **Kunne dere ikke bare brukt en tidsrekkemodell (ARIMA o.l.) på et
    salgsprognoseproblem?**
    - Avgrenset bevisst til to modellfamilier i tråd med faglig ramme.
      Tidsrekkemodeller er nevnt som videre arbeid. Vårt oppsett er
      tverrsnitts-/feature-basert (rabatt, region, kategori per transaksjon),
      ikke en ren aggregert tidsserie.

30. **Hvordan har dere brukt KI-verktøy i prosjektet, og hvordan sikrer dere
    faglig integritet?**
    - Åpent dokumentert i endringslogg og obligatorisk egenerklæring. KI brukt
      som verktøy i analyse-/rapportarbeid; gruppen har skrevet og godkjent
      rapporten i fellesskap. Reproduserbar pipeline med faste seeds.

31. **Hvor reproduserbart er arbeidet?**
    - Aktivitetsbaserte skript under `006 analysis/`, faste seeds for RF
      (`random_state=42`), ingen ad-hoc-manipulering mellom aktiviteter.
      Pipeline fra rådata til metrikker kan kjøres på nytt.

---

## Tips til spørrerunden

- **Eier dere usikkerheten:** På kritiske spørsmål (naiv baseline, ett
  valideringsår, høy MAPE) er det styrke å innrømme begrensningen og vise at
  dere har tenkt på den – det er ofte nettopp det sensor leter etter.
- **Bruk tallene presist:** Et konkret tall (RMSE 578, 11/12 måneder) virker mer
  overbevisende enn «den var litt bedre».
- **Pek tilbake til problemstillingen:** Knytt svar til de to delproblemene når
  det passer.
- **Fordel temaene:** Avtal gjerne på forhånd hvem som tar metode, hvem som tar
  resultater og hvem som tar tolkning/begrensninger – samme inndeling som intro.
