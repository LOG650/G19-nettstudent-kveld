# Endringslogg

## 2026-04-02 - WBS 4.3 omtolket til lett verifiseringssteg

- Hva ble endret: Aktiviteten `4.3 Trene modellene` er gjennomført i repoet som felles verifisering og treningsoppsummering, ikke som en ny full treningsrunde for begge modeller.
- Hvorfor: Selve modelltreningen er allerede dokumentert og utført i WBS 4.1 for lineær regresjon og i WBS 4.2 for Random Forest Regressor. En ny trening i 4.3 ville derfor vært redundant og gitt lite ny sporbar verdi.
- Konsekvens for videre arbeid: WBS 4.3 leverer felles kontroll av treningsgrunnlaget og en samlet oversikt over modellsignaler, mens parameterjustering fortsatt ligger i WBS 4.4 og evaluering ligger i WBS 5.x og WBS 6.1.
- Hvem/beslutningsgrunnlag: Endringen ble gjort i arbeidsøkten 2026-04-02 etter gjennomgang av eksisterende artefakter i `08_lineaer_regresjon` og `09_random_forest_regressor`, samt avklaring om at 4.3 skulle være et lett steg.
