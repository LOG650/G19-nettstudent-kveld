# 015 Peer To Peer

Mappen inneholder G19s peer-review av G17s prosjektrapport i LOG650, samt grunnlagsmateriale.

## Oppgaven

Hver gruppe i LOG650 skal gi en peer-review av en annen gruppes prosjektrapport og levere tilbakemeldingen som en kort, skriftlig rapport (ca. 2–4 sider, PDF). Vurderingen følger sju områder fra Tabell 1 i veiledningen: innledning, litteratur og teori, metode, analyse og resultater, diskusjon, konklusjon, samt skriveflyt og formelle aspekter.

## Innhold

| Fil | Rolle |
| --- | --- |
| [veiledning peer-review LOG650.pdf](veiledning%20peer-review%20LOG650.pdf) | Veiledning og vurderingskriterier fra emneansvarlig. |
| [rapport_mal.md](rapport_mal.md) | G17s rapport «Finansiell logistikk og beslutningstøtte ved hjelp av KI» – kilden som vurderes. |
| [peer_review_G17.md](peer_review_G17.md) | G19s peer-review av G17 (kondensert versjon). Kilde for PDF-leveransen. |
| [peer_review_G17.pdf](peer_review_G17.pdf) | Ferdig PDF for innlevering. Forside + helhetsinntrykk + sju områdevurderinger. |
| [peer_review_G17_detaljert.md](peer_review_G17_detaljert.md) | Lengre arbeidsversjon med fyldigere begrunnelser per område. Beholdt som referanse, ikke leveres. |

## Bygg PDF på nytt

Fra denne mappen:

```bash
pandoc peer_review_G17.md -o peer_review_G17.pdf --pdf-engine=lualatex
```

YAML-blokken og `header-includes` i `peer_review_G17.md` styrer forside, marger, språk og Unicode-mapping (`≈` → `\approx`). Ingen ekstern `header.tex` eller Lua-filter trengs.
