# 02 Identifisere relevante variabler (WBS 2.3)

Denne aktiviteten foreslår hvilke variabler som skal tas videre til modellering.

## Kjøring

Kjør fra roten av `006 analysis`:

```bash
uv run python aktiviteter/02_identifisere_relevante_variabler/start_wbs_2_3.py
```

## Filer i mappen

- `start_wbs_2_3.py`: Lager anbefaling per variabel.
- `tab_relevante_variabler.csv`: Variabelvis anbefaling (`target`, `inkluder`, `vurder`, `ekskluder`) med begrunnelse.
- `tab_variabelregler.csv`: Regler/terskler brukt i vurderingen.
- `fig_variabelanbefalinger.png`: Oppsummert antall variabler per anbefalingskategori.

## Datakilde

- `004 data/Dagligvare_Dataset.csv`

## Merknad

Anbefalingene er et førsteutkast og bør kvalitetssikres faglig før modellutvikling (WBS 4.x).
