from pathlib import Path

import pandas as pd


INPUT_MODELLSAMMENLIGNING = "14_sammenligne_modellresultater/tab_modellsammenligning_oversikt.csv"
INPUT_MODELLVINNERE = "14_sammenligne_modellresultater/tab_modellvinner_telling.csv"
INPUT_VIKTIGE_VARIABLER = "15_viktige_variabler/tab_viktige_variabler_oversikt.csv"
INPUT_SEGMENTVINNERE = "16_tolke_modellresultater/tab_segmentvinnere_tolkning.csv"
INPUT_RENSELOGG = "04_dataprosessering/tab_renselogg.csv"
INPUT_FEATURE_MARKDOWN = "05_feature_engineering/feature_engineering.md"
INPUT_DATASPLITT_MARKDOWN = "06_datasplitt/datasplitt.md"
INPUT_LINEAER_MARKDOWN = "08_lineaer_regresjon/lineaer_regresjon.md"
INPUT_TUNING_MARKDOWN = "11_parameterjustering_random_forest/random_forest_tuning.md"
INPUT_PROSJEKTPLAN = "../../../012 fase 2 - plan/prosjektstyringsplan.md"

OUTPUT_MODELLPROFIL = "tab_modellprofil_6_2.csv"
OUTPUT_DISKUSJONSPUNKTER = "tab_diskusjonspunkter_oversikt.csv"
OUTPUT_METODEBEGRENSNINGER = "tab_metodebegrensninger_6_2.csv"
OUTPUT_MARKDOWN = "styrker_og_svakheter.md"

MODELLREKKEFOLGE = ["benchmark lineær", "baseline RF", "tuned RF"]
FORVENTET_ANTALL_MODELLRADER = 3
FORVENTET_ANTALL_SEGMENTRADER = 14
FORVENTET_DISKUSJONSRADER = 12
FORVENTET_BEGRENSNINGER = 6
FORVENTET_TOPPFEATURE = "Discount"
FORVENTET_ANBEFALT_MODELL = "tuned RF"


def les_dataset(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path, encoding="utf-8-sig")
    if df.shape[1] == 1:
        df = pd.read_csv(csv_path, sep=";", encoding="utf-8-sig")
    return df


def les_markdown(md_path: Path) -> str:
    return md_path.read_text(encoding="utf-8")


def modellorden() -> dict[str, int]:
    return {navn: indeks for indeks, navn in enumerate(MODELLREKKEFOLGE)}


def valider_modellsammenligning(df: pd.DataFrame) -> pd.DataFrame:
    krav = [
        "modellnavn",
        "modellrolle",
        "rmse_2025",
        "mape_2025_pct",
        "samlet_vurdering_5_3",
    ]
    mangler = [kol for kol in krav if kol not in df.columns]
    if mangler:
        raise ValueError(f"WBS 6.2 mangler kolonner i modellsammenligningen: {mangler}")

    if len(df) != FORVENTET_ANTALL_MODELLRADER:
        raise ValueError(
            f"WBS 6.2 forventer {FORVENTET_ANTALL_MODELLRADER} modellrader fra WBS 5.3, men fant {len(df)}."
        )

    df = df.copy()
    df["modellrekkefolge"] = df["modellrolle"].map(modellorden())
    if df["modellrekkefolge"].isna().any():
        ukjente = df.loc[df["modellrekkefolge"].isna(), "modellrolle"].tolist()
        raise ValueError(f"WBS 6.2 fant ukjente modellroller: {ukjente}")

    for kol in ["rmse_2025", "mape_2025_pct"]:
        df[kol] = pd.to_numeric(df[kol], errors="raise")

    anbefalte = df.loc[df["samlet_vurdering_5_3"] == "anbefalt"].reset_index(drop=True)
    if len(anbefalte) != 1:
        raise ValueError(f"WBS 6.2 forventer nøyaktig én anbefalt modell, men fant {len(anbefalte)}.")
    if anbefalte.iloc[0]["modellrolle"] != FORVENTET_ANBEFALT_MODELL:
        raise ValueError(
            "WBS 6.2 er planlagt rundt `tuned RF` som hovedmodell. "
            f"WBS 5.3 peker nå på `{anbefalte.iloc[0]['modellrolle']}`."
        )

    return df.sort_values("modellrekkefolge").reset_index(drop=True)


def valider_modellvinnere(df: pd.DataFrame) -> pd.DataFrame:
    krav = ["metric", "modellrolle", "antall_vinnermåneder", "andel_vinnermåneder_pct"]
    mangler = [kol for kol in krav if kol not in df.columns]
    if mangler:
        raise ValueError(f"WBS 6.2 mangler kolonner i modellvinner-tabellen: {mangler}")

    if len(df) != 6:
        raise ValueError(f"WBS 6.2 forventer 6 rader i modellvinner-tabellen, men fant {len(df)}.")

    df = df.copy()
    df["modellrekkefolge"] = df["modellrolle"].map(modellorden())
    df["antall_vinnermåneder"] = pd.to_numeric(df["antall_vinnermåneder"], errors="raise").astype(int)
    df["andel_vinnermåneder_pct"] = pd.to_numeric(df["andel_vinnermåneder_pct"], errors="raise")
    return df.sort_values(["metric", "modellrekkefolge"]).reset_index(drop=True)


def valider_viktige_variabler(df: pd.DataFrame) -> pd.DataFrame:
    krav = ["prioritet_5_4", "feature", "variabelgruppe"]
    mangler = [kol for kol in krav if kol not in df.columns]
    if mangler:
        raise ValueError(f"WBS 6.2 mangler kolonner i WBS 5.4-oversikten: {mangler}")

    df = df.copy()
    df["prioritet_5_4"] = pd.to_numeric(df["prioritet_5_4"], errors="raise").astype(int)
    topp = df.sort_values("prioritet_5_4").iloc[0]
    if topp["prioritet_5_4"] != 1 or topp["feature"] != FORVENTET_TOPPFEATURE:
        raise ValueError(
            "WBS 6.2 forventer at `Discount` står som prioritet 1 i WBS 5.4, "
            f"men fant `{topp['feature']}`."
        )

    return df.sort_values("prioritet_5_4").reset_index(drop=True)


def valider_segmentvinnere(df: pd.DataFrame) -> pd.DataFrame:
    krav = ["segmentdimensjon", "segmentverdi", "rmse_vinner", "mape_vinner", "samme_vinner"]
    mangler = [kol for kol in krav if kol not in df.columns]
    if mangler:
        raise ValueError(f"WBS 6.2 mangler kolonner i segmentvinner-tabellen: {mangler}")

    if len(df) != FORVENTET_ANTALL_SEGMENTRADER:
        raise ValueError(
            f"WBS 6.2 forventer {FORVENTET_ANTALL_SEGMENTRADER} rader i segmentvinner-tabellen, men fant {len(df)}."
        )

    return df.copy()


def valider_renselogg(df: pd.DataFrame) -> pd.DataFrame:
    krav = ["målepunkt", "verdi", "kommentar"]
    mangler = [kol for kol in krav if kol not in df.columns]
    if mangler:
        raise ValueError(f"WBS 6.2 mangler kolonner i renseloggen: {mangler}")

    oppslag = dict(zip(df["målepunkt"], df["verdi"]))
    forventede = {
        "antall_rader_inn": "9994",
        "antall_rader_ut": "9994",
        "manglende_verdier_inn": "0",
        "manglende_verdier_ut": "0",
        "dubletter_inn": "0",
        "dubletter_ut": "0",
    }
    for målepunkt, forventet in forventede.items():
        faktisk = str(oppslag.get(målepunkt, ""))
        if faktisk != forventet:
            raise ValueError(f"WBS 6.2 forventer `{målepunkt}={forventet}`, men fant `{faktisk}`.")

    return df


def krever_tekst(markdown: str, tekstbiter: list[str], navn: str) -> None:
    mangler = [tekst for tekst in tekstbiter if tekst not in markdown]
    if mangler:
        raise ValueError(f"WBS 6.2 fant ikke forventet tekst i {navn}: {mangler}")


def valider_markdownkilder(
    feature_markdown: str,
    datasplitt_markdown: str,
    lineær_markdown: str,
    tuning_markdown: str,
    prosjektplan_markdown: str,
) -> None:
    krever_tekst(
        feature_markdown,
        [
            "Direkte features: `Discount, Category, Sub Category, City, Region`",
            "Utledede tidsfeatures: `year`, `month`, `quarter`, `weekofyear`, `dayofweek`, `dayofmonth`, `is_weekend`",
        ],
        "feature_engineering.md",
    )
    krever_tekst(
        datasplitt_markdown,
        [
            "Treningsår: 2022, 2023, 2024",
            "Testår: 2025",
            "Antall treningsrader: 6682",
            "Antall testrader: 3312",
            "Antall encoded feature-kolonner: 67",
        ],
        "datasplitt.md",
    )
    krever_tekst(
        lineær_markdown,
        [
            "uten skalering eller regularisering",
            "multikollinearitet i lineær regresjon",
        ],
        "lineaer_regresjon.md",
    )
    krever_tekst(
        tuning_markdown,
        [
            "Valideringsår: `2024`",
            "Antall kandidater testet: 36",
            "Valg av vinner gjøres på lavest `RMSE` på valideringsåret, med `MAPE` som sekundær metrikk ved likt resultat.",
        ],
        "random_forest_tuning.md",
    )
    krever_tekst(
        prosjektplan_markdown,
        [
            "Analysen fokuserer på prediksjon og ikke på kausal sammenheng mellom variabler.",
            "Eksterne makroøkonomiske faktorer (inflasjon, rente, konjunkturer osv.) inkluderes ikke i modellen.",
            "Prosjektet er avgrenset til én simulert virksomhet og ett datasett.",
            "Modellene som vurderes er begrenset til multippel lineær regresjon og Random Forest Regressor.",
        ],
        "prosjektstyringsplan.md",
    )


def hent_antall_vinnere(vinner_df: pd.DataFrame, kolonne: str) -> dict[str, int]:
    telling = vinner_df[kolonne].value_counts().to_dict()
    return {modell: int(telling.get(modell, 0)) for modell in MODELLREKKEFOLGE}


def bygg_modellprofil(
    sammenligning_df: pd.DataFrame,
    månedsvinnere_df: pd.DataFrame,
    segmentvinnere_df: pd.DataFrame,
) -> pd.DataFrame:
    måneds_rmse = {
        rad["modellrolle"]: int(rad["antall_vinnermåneder"])
        for _, rad in månedsvinnere_df.loc[månedsvinnere_df["metric"] == "RMSE"].iterrows()
    }
    måneds_mape = {
        rad["modellrolle"]: int(rad["antall_vinnermåneder"])
        for _, rad in månedsvinnere_df.loc[månedsvinnere_df["metric"] == "MAPE"].iterrows()
    }
    segment_rmse = hent_antall_vinnere(segmentvinnere_df, "rmse_vinner")
    segment_mape = hent_antall_vinnere(segmentvinnere_df, "mape_vinner")

    styrker = {
        "benchmark lineær": "Høy tolkbarhet og konkurransedyktig i enkelte segmenter.",
        "baseline RF": "Sterk lokal MAPE-ytelse og nyttig RF-sammenligningspunkt.",
        "tuned RF": "Best samlet 2025 og sterkest på absolutt feil.",
    }
    svakheter = {
        "benchmark lineær": "Multikollinearitet og manglende regularisering svekker robust koeffisienttolkning.",
        "baseline RF": "Svakest samlet og uten RMSE-seire i måneder eller segmenter.",
        "tuned RF": "MAPE er mer ujevn enn RMSE mellom måneder og segmenter.",
    }
    tolkbarhet = {
        "benchmark lineær": "høy",
        "baseline RF": "middels",
        "tuned RF": "middels",
    }

    rader = []
    for _, rad in sammenligning_df.iterrows():
        modellrolle = rad["modellrolle"]
        rader.append(
            {
                "modellnavn": rad["modellnavn"],
                "modellrolle": modellrolle,
                "samlet_vurdering_5_3": rad["samlet_vurdering_5_3"],
                "samlet_rmse_2025": round(float(rad["rmse_2025"]), 6),
                "samlet_mape_2025_pct": round(float(rad["mape_2025_pct"]), 4),
                "rmse_vinnermåneder": måneds_rmse[modellrolle],
                "mape_vinnermåneder": måneds_mape[modellrolle],
                "rmse_vinnersegmenter": segment_rmse[modellrolle],
                "mape_vinnersegmenter": segment_mape[modellrolle],
                "tolkbarhet_niva": tolkbarhet[modellrolle],
                "hovedstyrke": styrker[modellrolle],
                "hovedsvakhet": svakheter[modellrolle],
            }
        )

    return pd.DataFrame(rader)


def bygg_diskusjonspunkter() -> pd.DataFrame:
    rader = [
        {
            "nivå": "modell",
            "objekt": "benchmark lineær",
            "kategori": "tolkbarhet",
            "vurderingstype": "styrke",
            "påstand": "Lineær regresjon har høyest tolkbarhet fordi koeffisientene og retningen på sentrale signaler kan leses direkte.",
            "primær_evidens": "08_lineaer_regresjon/lineaer_regresjon.md: benchmark-modellen bruker LinearRegression og dokumenterer koeffisienter.",
            "sekundær_evidens": "15_viktige_variabler/tab_viktige_variabler_oversikt.csv: lineær regresjon brukes som støttespor for fortegn.",
            "konsekvens_for_diskusjon": "Dette styrker forklarbarheten i caset, men betyr ikke at lineær regresjon er best på prognosepresisjon.",
        },
        {
            "nivå": "modell",
            "objekt": "benchmark lineær",
            "kategori": "konkurransedyktig i enkelte segmenter",
            "vurderingstype": "styrke",
            "påstand": "Benchmark-modellen er fortsatt konkurransedyktig i enkelte segmenter, særlig på prosentfeil og i høyt salgsnivå.",
            "primær_evidens": "16_tolke_modellresultater/tab_segmentvinnere_tolkning.csv: benchmark lineær vinner MAPE i Q1, Q4, Central og hoyt salg, og vinner både RMSE og MAPE i hoyt salg.",
            "sekundær_evidens": "14_sammenligne_modellresultater/tab_modellvinner_telling.csv: benchmark lineær har 3 månedsseire på MAPE.",
            "konsekvens_for_diskusjon": "Diskusjonen bør derfor unngå å omtale benchmark som irrelevant selv om den ikke er samlet anbefalt.",
        },
        {
            "nivå": "modell",
            "objekt": "benchmark lineær",
            "kategori": "multikollinearitet og manglende regularisering",
            "vurderingstype": "svakhet",
            "påstand": "Koeffisienttolkningen i lineær regresjon er sårbar fordi modellen er kjørt uten regularisering og med dummykoding som kan gi multikollinearitet.",
            "primær_evidens": "08_lineaer_regresjon/lineaer_regresjon.md: modellen er kjørt uten skalering eller regularisering og koeffisientene må tolkes varsomt.",
            "sekundær_evidens": "06_datasplitt/datasplitt.md: feature-settet er one-hot-encodet i 67 kolonner.",
            "konsekvens_for_diskusjon": "Dette svekker påliteligheten i sterke årsaksnære tolkninger av enkeltkoeffisienter.",
        },
        {
            "nivå": "modell",
            "objekt": "baseline RF",
            "kategori": "sterk lokal MAPE-ytelse og nyttig RF-sammenligningspunkt",
            "vurderingstype": "styrke",
            "påstand": "Baseline RF har tydelig lokal styrke på prosentfeil og er samtidig et nyttig sammenligningspunkt for å se hva tuning faktisk tilfører RF-sporet.",
            "primær_evidens": "14_sammenligne_modellresultater/tab_modellvinner_telling.csv: baseline RF vinner 6 av 12 måneder på MAPE.",
            "sekundær_evidens": "16_tolke_modellresultater/tab_segmentvinnere_tolkning.csv + 11_parameterjustering_random_forest/random_forest_tuning.md: baseline RF vinner MAPE i flere segmenter og baseline-artefaktene er bevart som sammenligningspunkt.",
            "konsekvens_for_diskusjon": "Dette viser at prosentfeil reagerer annerledes enn absoluttfeil og at baseline-modellen gir et etterprøvbart RF-referansepunkt.",
        },
        {
            "nivå": "modell",
            "objekt": "baseline RF",
            "kategori": "svakest samlet og ingen RMSE-seire",
            "vurderingstype": "svakhet",
            "påstand": "Baseline RF er svakest samlet og har ingen seire på RMSE, verken per måned eller per segment.",
            "primær_evidens": "14_sammenligne_modellresultater/tab_modellsammenligning_oversikt.csv: baseline RF er rang 3 på samlet RMSE og ikke anbefalt.",
            "sekundær_evidens": "14_sammenligne_modellresultater/tab_modellvinner_telling.csv + 16_tolke_modellresultater/tab_segmentvinnere_tolkning.csv: 0 RMSE-seire i måneder og 0 RMSE-seire i segmenter.",
            "konsekvens_for_diskusjon": "Det gjør modellen mindre robust som hovedvalg når absolutt feil prioriteres i caset.",
        },
        {
            "nivå": "modell",
            "objekt": "tuned RF",
            "kategori": "best samlet 2025",
            "vurderingstype": "styrke",
            "påstand": "Tuned RF er best samlet i 2025 og er derfor det sterkeste operative modellvalget i prosjektet.",
            "primær_evidens": "14_sammenligne_modellresultater/tab_modellsammenligning_oversikt.csv: tuned RF er rang 1 på både RMSE og MAPE og merket som anbefalt.",
            "sekundær_evidens": "16_tolke_modellresultater/modelltolkning.md: tuned RF brukes som hovedmodell i videre tolkning.",
            "konsekvens_for_diskusjon": "Dette styrker påliteligheten i hovedkonklusjonen så lenge fokus er prediksjon innenfor samme datasett og oppsett.",
        },
        {
            "nivå": "modell",
            "objekt": "tuned RF",
            "kategori": "sterkest RMSE-stabilitet",
            "vurderingstype": "styrke",
            "påstand": "Tuned RF er klart sterkest på absolutt feil og følger totalnivået mest stabilt gjennom året og på tvers av segmenter.",
            "primær_evidens": "14_sammenligne_modellresultater/tab_modellvinner_telling.csv: tuned RF vinner 11 av 12 måneder på RMSE.",
            "sekundær_evidens": "16_tolke_modellresultater/tab_segmentvinnere_tolkning.csv: tuned RF vinner RMSE i 13 av 14 segmenter.",
            "konsekvens_for_diskusjon": "Dette gjør modellen robust når caset legger størst vekt på absolutte prognoseavvik.",
        },
        {
            "nivå": "modell",
            "objekt": "tuned RF",
            "kategori": "MAPE mer ujevn enn RMSE",
            "vurderingstype": "svakhet",
            "påstand": "Tuned RF er ikke like dominerende på prosentfeil som på absolutt feil, og MAPE varierer tydeligere mellom segmentene.",
            "primær_evidens": "14_sammenligne_modellresultater/tab_modellvinner_telling.csv: tuned RF vinner bare 3 av 12 måneder på MAPE.",
            "sekundær_evidens": "16_tolke_modellresultater/tab_segmentvinnere_tolkning.csv: MAPE-vinneren skifter mellom alle tre modeller på tvers av segmentene.",
            "konsekvens_for_diskusjon": "Diskusjonen må derfor skille tydelig mellom robusthet på absoluttfeil og robusthet på prosentfeil.",
        },
        {
            "nivå": "prosjekt",
            "objekt": "prosjekt",
            "kategori": "renset og sporbart datagrunnlag",
            "vurderingstype": "styrke",
            "påstand": "Datagrunnlaget er renset, dokumentert og sporbarheten er høy gjennom hele analyseflyten.",
            "primær_evidens": "04_dataprosessering/tab_renselogg.csv: 9994 rader inn og ut, 0 manglende verdier og 0 dubletter.",
            "sekundær_evidens": "06_datasplitt/datasplitt.md: tidsdelt train/test-oppsett med 2022-2024 som trening og 2025 som test.",
            "konsekvens_for_diskusjon": "Dette styrker prosjektets pålitelighet innenfor egen case og gjør resultatene etterprøvbare.",
        },
        {
            "nivå": "prosjekt",
            "objekt": "prosjekt",
            "kategori": "begrenset representativitet og ingen makrovariabler",
            "vurderingstype": "svakhet",
            "påstand": "Generaliserbarheten er begrenset fordi prosjektet bygger på én simulert virksomhet og utelater eksterne makroøkonomiske faktorer.",
            "primær_evidens": "012 fase 2 - plan/prosjektstyringsplan.md: prosjektet er avgrenset til én simulert virksomhet og ett datasett.",
            "sekundær_evidens": "012 fase 2 - plan/prosjektstyringsplan.md: eksterne makroøkonomiske faktorer inkluderes ikke i modellen.",
            "konsekvens_for_diskusjon": "Resultatene bør derfor generaliseres varsomt utover dette caset.",
        },
        {
            "nivå": "prosjekt",
            "objekt": "prosjekt",
            "kategori": "modellomfang og valideringsvindu er smalt",
            "vurderingstype": "svakhet",
            "påstand": "Prosjektets modellomfang og valideringsvindu er relativt smalt fordi kun lineær regresjon og Random Forest vurderes, og tuning bruker bare 2024 som intern validering.",
            "primær_evidens": "012 fase 2 - plan/prosjektstyringsplan.md: modellene er avgrenset til lineær regresjon og Random Forest.",
            "sekundær_evidens": "11_parameterjustering_random_forest/random_forest_tuning.md: tuning bruker 2024 som valideringsår og 36 kandidater.",
            "konsekvens_for_diskusjon": "Dette reduserer hvor bredt man kan hevde at valgt modell er best blant alternative modellfamilier og tidsoppsett.",
        },
        {
            "nivå": "prosjekt",
            "objekt": "prosjekt",
            "kategori": "ingen kausal analyse",
            "vurderingstype": "svakhet",
            "påstand": "Prosjektet er utviklet for prediksjon og gjør ingen kausal analyse av hva som faktisk driver salget.",
            "primær_evidens": "012 fase 2 - plan/prosjektstyringsplan.md: analysen fokuserer på prediksjon og ikke på kausal sammenheng.",
            "sekundær_evidens": "16_tolke_modellresultater/modelltolkning.md + 15_viktige_variabler/variabelanalyse.md: senere WBS-steg avgrenser seg eksplisitt mot kausal analyse.",
            "konsekvens_for_diskusjon": "Det begrenser hvor sterke beslutningspåstander som kan knyttes direkte til enkeltvariabler.",
        },
    ]

    diskusjon_df = pd.DataFrame(rader)
    if len(diskusjon_df) != FORVENTET_DISKUSJONSRADER:
        raise ValueError(
            f"WBS 6.2 forventer {FORVENTET_DISKUSJONSRADER} diskusjonspunkter, men bygget {len(diskusjon_df)}."
        )
    return diskusjon_df


def bygg_metodebegrensninger() -> pd.DataFrame:
    rader = [
        {
            "begrensning_id": "MB-6.2-01",
            "tema": "representativitet",
            "beskrivelse": "Prosjektet bygger på én simulert virksomhet og ett datasett, ikke flere virksomheter eller markeder.",
            "kildeartefakt": "012 fase 2 - plan/prosjektstyringsplan.md",
            "konsekvens_for_pålitelighet": "Påliteligheten innenfor dette caset kan fortsatt være god, men robustheten mot andre kontekster er ikke testet.",
            "konsekvens_for_generaliserbarhet": "Funnene kan ikke uten videre overføres til andre bedrifter, regioner eller produktmixer.",
        },
        {
            "begrensning_id": "MB-6.2-02",
            "tema": "eksterne faktorer",
            "beskrivelse": "Eksterne makroøkonomiske forhold som inflasjon, rente og konjunkturer er ikke modellert.",
            "kildeartefakt": "012 fase 2 - plan/prosjektstyringsplan.md",
            "konsekvens_for_pålitelighet": "Prognosene kan være mindre robuste hvis 2025 påvirkes av forhold som ikke finnes i feature-settet.",
            "konsekvens_for_generaliserbarhet": "Resultatene generaliserer dårligere til perioder der eksterne sjokk spiller en større rolle.",
        },
        {
            "begrensning_id": "MB-6.2-03",
            "tema": "modellomfang",
            "beskrivelse": "Prosjektet sammenligner bare lineær regresjon og Random Forest, ikke andre modellfamilier.",
            "kildeartefakt": "012 fase 2 - plan/prosjektstyringsplan.md",
            "konsekvens_for_pålitelighet": "Valgt modell er best i dette prosjektets kandidatfelt, men ikke nødvendigvis best mulig totalt sett.",
            "konsekvens_for_generaliserbarhet": "Det er begrenset grunnlag for å generalisere at samme modellfamilie vil være best i andre lignende problemer.",
        },
        {
            "begrensning_id": "MB-6.2-04",
            "tema": "koeffisienttolkning",
            "beskrivelse": "Lineær regresjon er kjørt uten regularisering, og dummykoding kan gi multikollinearitet i koeffisientene.",
            "kildeartefakt": "006 analysis/aktiviteter/08_lineaer_regresjon/lineaer_regresjon.md",
            "konsekvens_for_pålitelighet": "Dette svekker påliteligheten i sterke fortolkninger av enkeltkoeffisienter som om de var stabile effektmål.",
            "konsekvens_for_generaliserbarhet": "Koeffisientmønstre kan endre seg når datastruktur eller kategorifordeling endres i andre case.",
        },
        {
            "begrensning_id": "MB-6.2-05",
            "tema": "valideringsvindu",
            "beskrivelse": "Tuning av Random Forest bruker kun 2024 som intern valideringsperiode.",
            "kildeartefakt": "006 analysis/aktiviteter/11_parameterjustering_random_forest/random_forest_tuning.md",
            "konsekvens_for_pålitelighet": "Modellvalget er etterprøvbart, men sensitivitet for andre valideringsvinduer er ikke undersøkt.",
            "konsekvens_for_generaliserbarhet": "Det gir mindre grunnlag for å generalisere tuningvalgene til andre tidsperioder eller sesongmønstre.",
        },
        {
            "begrensning_id": "MB-6.2-06",
            "tema": "kausalitet",
            "beskrivelse": "Analysen er prediktiv og ikke kausal, slik at viktige variabler ikke kan tolkes som dokumenterte årsaker til salg.",
            "kildeartefakt": "012 fase 2 - plan/prosjektstyringsplan.md",
            "konsekvens_for_pålitelighet": "Det er mer pålitelig å bruke funnene som prognosestøtte enn som bevis for årsakssammenhenger.",
            "konsekvens_for_generaliserbarhet": "Beslutninger som krever kausal innsikt kan ikke generaliseres direkte fra disse prediktive mønstrene.",
        },
    ]

    begrensninger_df = pd.DataFrame(rader)
    if len(begrensninger_df) != FORVENTET_BEGRENSNINGER:
        raise ValueError(
            f"WBS 6.2 forventer {FORVENTET_BEGRENSNINGER} metodebegrensninger, men bygget {len(begrensninger_df)}."
        )
    return begrensninger_df


def lag_markdown(modellprofil_df: pd.DataFrame, begrensninger_df: pd.DataFrame) -> str:
    benchmark = modellprofil_df.loc[modellprofil_df["modellrolle"] == "benchmark lineær"].iloc[0]
    baseline = modellprofil_df.loc[modellprofil_df["modellrolle"] == "baseline RF"].iloc[0]
    tuned = modellprofil_df.loc[modellprofil_df["modellrolle"] == "tuned RF"].iloc[0]

    begrensningstema = ", ".join(f"`{tema}`" for tema in begrensninger_df["tema"].tolist())

    linjer = [
        "# Styrker og svakheter (WBS 6.2)",
        "",
        "## Hva WBS 6.2 gjør",
        "",
        "- Aktiviteten diskuterer styrker og svakheter oppå WBS 5.3, 5.4 og 6.1 uten å trene modeller på nytt eller beregne nye prognosemetrikker.",
        "- Diskusjonen er delt i modellnivå og prosjektnivå, med eksplisitt skille mellom `pålitelighet` innenfor dette datasettet og `generaliserbarhet` utover caset.",
        "- WBS 6.2 gir ikke operative anbefalinger. Videre vurdering av praktisk nytte ligger i WBS 6.3.",
        "",
        "## Modellstyrker",
        "",
        f"- `benchmark lineær` har høy tolkbarhet og er fortsatt konkurransedyktig i enkelte segmenter, med `RMSE`-/`MAPE`-seier i segmentet for `hoyt salg` og `MAPE`-seire i `4` segmenter totalt.",
        f"- `baseline RF` viser lokal styrke på prosentfeil med `MAPE`-seier i `6` av `12` måneder og `4` segmenter, og fungerer derfor som et nyttig sammenligningspunkt for å se hva tuning faktisk tilfører RF-sporet.",
        f"- `tuned RF` er samlet sterkest med `RMSE={tuned['samlet_rmse_2025']:.6f}`, `MAPE={tuned['samlet_mape_2025_pct']:.4f} %`, `11` månedsseire på `RMSE` og `13` segmentseire på `RMSE`.",
        "",
        "## Modellsvakheter",
        "",
        f"- `benchmark lineær` er sårbar for multikollinearitet og manglende regularisering, noe som gjør koeffisientene mindre robuste som grunnlag for sterke årsaksnære tolkninger.",
        f"- `baseline RF` er svakest samlet og har `0` seire på `RMSE` både per måned og per segment, selv om modellen gjør det bedre på enkelte prosentfeilsituasjoner.",
        f"- `tuned RF` er tydeligst på absoluttfeil, men mer ujevn på prosentfeil, med bare `{tuned['mape_vinnermåneder']}` månedsseire på `MAPE` og `{tuned['mape_vinnersegmenter']}` segmentseire på `MAPE`.",
        "",
        "## Pålitelighet",
        "",
        "- Påliteligheten i dette prosjektoppsettet styrkes av et renset og sporbart datagrunnlag: `9994` rader inn og ut, `0` manglende verdier, `0` dubletter og en tydelig tidsdelt train/test-splitt mellom `2022-2024` og `2025`.",
        "- Modellvalget fremstår robust når absolutte feil prioriteres, fordi `tuned RF` vinner nesten alle måneder og segmenter på `RMSE` og samtidig er rang `1` samlet i WBS 5.3.",
        f"- Samtidig viser `MAPE`-mønsteret at prosentfeilen er mer følsom for kvartal, rabatt, region og salgsnivå. Det betyr at påliteligheten er sterkest for nivåtreff og svakere for relative avvik i enkelte delmiljøer.",
        "",
        "## Generaliserbarhet",
        "",
        "- Generaliserbarheten er begrenset fordi prosjektet er avgrenset til ett datasett, én simulert virksomhet og et feature-sett uten eksterne makroøkonomiske faktorer.",
        "- Modellomfanget er også smalt: bare lineær regresjon og Random Forest er vurdert, og tuning av RF er gjort med ett internt valideringsår (`2024`).",
        "- Viktige variabler og segmentmønstre gir derfor god lokal innsikt i dette caset, men bør ikke tolkes som allmenne eller kausale sannheter om dagligvaresalg.",
        "",
        "## Metodebegrensninger oppsummert",
        "",
        f"- WBS 6.2 dokumenterer disse seks metodebegrensningene eksplisitt: {begrensningstema}.",
        f"- Dette betyr at `tuned RF` er et godt prediktivt valg i dette prosjektet, mens tolkning utover caset må gjøres varsomt og helst støttes av bredere datagrunnlag eller alternative modelloppsett.",
        "",
        "## Avgrensning mot WBS 6.3",
        "",
        f"- WBS 6.2 vurderer kvalitet, robusthet og begrensninger. Spørsmålet om hva dette betyr for beslutningsstøtte, lager, kampanjer og praktisk bruk i Dagligvare tas videre i WBS 6.3.",
    ]
    return "\n".join(linjer) + "\n"


def main() -> None:
    aktivitetsmappe = Path(__file__).resolve().parent
    analyse_rot = aktivitetsmappe.parent

    sammenligning_df = les_dataset(analyse_rot / INPUT_MODELLSAMMENLIGNING)
    modellvinnere_df = les_dataset(analyse_rot / INPUT_MODELLVINNERE)
    viktige_df = les_dataset(analyse_rot / INPUT_VIKTIGE_VARIABLER)
    segmentvinnere_df = les_dataset(analyse_rot / INPUT_SEGMENTVINNERE)
    renselogg_df = les_dataset(analyse_rot / INPUT_RENSELOGG)

    feature_markdown = les_markdown(analyse_rot / INPUT_FEATURE_MARKDOWN)
    datasplitt_markdown = les_markdown(analyse_rot / INPUT_DATASPLITT_MARKDOWN)
    lineær_markdown = les_markdown(analyse_rot / INPUT_LINEAER_MARKDOWN)
    tuning_markdown = les_markdown(analyse_rot / INPUT_TUNING_MARKDOWN)
    prosjektplan_markdown = les_markdown(aktivitetsmappe / INPUT_PROSJEKTPLAN)

    sammenligning_df = valider_modellsammenligning(sammenligning_df)
    modellvinnere_df = valider_modellvinnere(modellvinnere_df)
    viktige_df = valider_viktige_variabler(viktige_df)
    segmentvinnere_df = valider_segmentvinnere(segmentvinnere_df)
    valider_renselogg(renselogg_df)
    valider_markdownkilder(
        feature_markdown,
        datasplitt_markdown,
        lineær_markdown,
        tuning_markdown,
        prosjektplan_markdown,
    )

    modellprofil_df = bygg_modellprofil(sammenligning_df, modellvinnere_df, segmentvinnere_df)
    diskusjon_df = bygg_diskusjonspunkter()
    begrensninger_df = bygg_metodebegrensninger()
    markdown = lag_markdown(modellprofil_df, begrensninger_df)

    modellprofil_df.to_csv(aktivitetsmappe / OUTPUT_MODELLPROFIL, index=False, encoding="utf-8")
    diskusjon_df.to_csv(aktivitetsmappe / OUTPUT_DISKUSJONSPUNKTER, index=False, encoding="utf-8")
    begrensninger_df.to_csv(aktivitetsmappe / OUTPUT_METODEBEGRENSNINGER, index=False, encoding="utf-8")
    (aktivitetsmappe / OUTPUT_MARKDOWN).write_text(markdown, encoding="utf-8")

    print("WBS 6.2 er gjennomført.")
    print(f"- Skrev {OUTPUT_MODELLPROFIL}")
    print(f"- Skrev {OUTPUT_DISKUSJONSPUNKTER}")
    print(f"- Skrev {OUTPUT_METODEBEGRENSNINGER}")
    print(f"- Skrev {OUTPUT_MARKDOWN}")
    print(
        "- Merk: faktiske segmenttellinger viser `MAPE`-seire på segmentnivå som "
        "`benchmark lineær=4`, `baseline RF=4` og `tuned RF=6`."
    )


if __name__ == "__main__":
    main()
