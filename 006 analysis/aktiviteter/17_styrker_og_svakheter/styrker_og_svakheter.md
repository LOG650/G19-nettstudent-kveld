# Styrker og svakheter (WBS 6.2)

## Hva WBS 6.2 gjør

- Aktiviteten diskuterer styrker og svakheter oppå WBS 5.3, 5.4 og 6.1 uten å trene modeller på nytt eller beregne nye prognosemetrikker.
- Diskusjonen er delt i modellnivå og prosjektnivå, med eksplisitt skille mellom `pålitelighet` innenfor dette datasettet og `generaliserbarhet` utover caset.
- WBS 6.2 gir ikke operative anbefalinger. Videre vurdering av praktisk nytte ligger i WBS 6.3.

## Modellstyrker

- `benchmark lineær` har høy tolkbarhet og er fortsatt konkurransedyktig i enkelte segmenter, med `RMSE`-/`MAPE`-seier i segmentet for `hoyt salg` og `MAPE`-seire i `4` segmenter totalt.
- `baseline RF` viser lokal styrke på prosentfeil med `MAPE`-seier i `6` av `12` måneder og `4` segmenter, og fungerer derfor som et nyttig sammenligningspunkt for å se hva tuning faktisk tilfører RF-sporet.
- `tuned RF` er samlet sterkest med `RMSE=578.259649`, `MAPE=43.9706 %`, `11` månedsseire på `RMSE` og `13` segmentseire på `RMSE`.

## Modellsvakheter

- `benchmark lineær` er sårbar for multikollinearitet og manglende regularisering, noe som gjør koeffisientene mindre robuste som grunnlag for sterke årsaksnære tolkninger.
- `baseline RF` er svakest samlet og har `0` seire på `RMSE` både per måned og per segment, selv om modellen gjør det bedre på enkelte prosentfeilsituasjoner.
- `tuned RF` er tydeligst på absoluttfeil, men mer ujevn på prosentfeil, med bare `3` månedsseire på `MAPE` og `6` segmentseire på `MAPE`.

## Pålitelighet

- Påliteligheten i dette prosjektoppsettet styrkes av et renset og sporbart datagrunnlag: `9994` rader inn og ut, `0` manglende verdier, `0` dubletter og en tydelig tidsdelt train/test-splitt mellom `2022-2024` og `2025`.
- Modellvalget fremstår robust når absolutte feil prioriteres, fordi `tuned RF` vinner nesten alle måneder og segmenter på `RMSE` og samtidig er rang `1` samlet i WBS 5.3.
- Samtidig viser `MAPE`-mønsteret at prosentfeilen er mer følsom for kvartal, rabatt, region og salgsnivå. Det betyr at påliteligheten er sterkest for nivåtreff og svakere for relative avvik i enkelte delmiljøer.

## Generaliserbarhet

- Generaliserbarheten er begrenset fordi prosjektet er avgrenset til ett datasett, én simulert virksomhet og et feature-sett uten eksterne makroøkonomiske faktorer.
- Modellomfanget er også smalt: bare lineær regresjon og Random Forest er vurdert, og tuning av RF er gjort med ett internt valideringsår (`2024`).
- Viktige variabler og segmentmønstre gir derfor god lokal innsikt i dette caset, men bør ikke tolkes som allmenne eller kausale sannheter om dagligvaresalg.

## Metodebegrensninger oppsummert

- WBS 6.2 dokumenterer disse seks metodebegrensningene eksplisitt: `representativitet`, `eksterne faktorer`, `modellomfang`, `koeffisienttolkning`, `valideringsvindu`, `kausalitet`.
- Dette betyr at `tuned RF` er et godt prediktivt valg i dette prosjektet, mens tolkning utover caset må gjøres varsomt og helst støttes av bredere datagrunnlag eller alternative modelloppsett.

## Avgrensning mot WBS 6.3

- WBS 6.2 vurderer kvalitet, robusthet og begrensninger. Spørsmålet om hva dette betyr for beslutningsstøtte, lager, kampanjer og praktisk bruk i PowerHorse tas videre i WBS 6.3.
