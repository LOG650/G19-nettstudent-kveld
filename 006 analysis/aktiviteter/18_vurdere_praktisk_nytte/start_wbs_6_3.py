from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


INPUT_MODELLSAMMENLIGNING = "14_sammenligne_modellresultater/tab_modellsammenligning_oversikt.csv"
INPUT_MODELLVINNERE = "14_sammenligne_modellresultater/tab_modellvinner_telling.csv"
INPUT_VIKTIGE_VARIABLER = "15_viktige_variabler/tab_viktige_variabler_oversikt.csv"
INPUT_SEGMENTVINNERE = "16_tolke_modellresultater/tab_segmentvinnere_tolkning.csv"
INPUT_MODELLPROFIL = "17_styrker_og_svakheter/tab_modellprofil_6_2.csv"
INPUT_STYRKER_MARKDOWN = "17_styrker_og_svakheter/styrker_og_svakheter.md"

OUTPUT_BESLUTNINGSMATRISE = "tab_beslutningsmatrise_6_3.csv"
OUTPUT_BRUKSREGLER = "tab_bruksregler_6_3.csv"
OUTPUT_MARKDOWN = "praktisk_nytte.md"

MODELLREKKEFOLGE = ["benchmark lineær", "baseline RF", "tuned RF"]
FORVENTET_ANBEFALT_MODELL = "tuned RF"
FORVENTET_TOPPFEATURE = "Discount"
FORVENTET_CASE = "Dagligvare"
FORVENTET_SEGMENTRADER = 14
FORVENTET_BESLUTNINGSRADER = 4
FORVENTET_BRUKSREGLER = 4


def les_dataset(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path, encoding="utf-8-sig")
    if df.shape[1] == 1:
        df = pd.read_csv(csv_path, sep=";", encoding="utf-8-sig")
    return df


def les_markdown(md_path: Path) -> str:
    return md_path.read_text(encoding="utf-8")


def les_json(json_path: Path) -> dict:
    return json.loads(json_path.read_text(encoding="utf-8"))


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
        raise ValueError(f"WBS 6.3 mangler kolonner i modellsammenligningen: {mangler}")

    if len(df) != 3:
        raise ValueError(f"WBS 6.3 forventer 3 modellrader i WBS 5.3, men fant {len(df)}.")

    df = df.copy()
    df["modellrekkefolge"] = df["modellrolle"].map(modellorden())
    if df["modellrekkefolge"].isna().any():
        ukjente = df.loc[df["modellrekkefolge"].isna(), "modellrolle"].tolist()
        raise ValueError(f"WBS 6.3 fant ukjente modellroller: {ukjente}")

    df["rmse_2025"] = pd.to_numeric(df["rmse_2025"], errors="raise")
    df["mape_2025_pct"] = pd.to_numeric(df["mape_2025_pct"], errors="raise")

    anbefalte = df.loc[df["samlet_vurdering_5_3"] == "anbefalt"].reset_index(drop=True)
    if len(anbefalte) != 1:
        raise ValueError(f"WBS 6.3 forventer nøyaktig én anbefalt modell, men fant {len(anbefalte)}.")
    if anbefalte.iloc[0]["modellrolle"] != FORVENTET_ANBEFALT_MODELL:
        raise ValueError(
            "WBS 6.3 er planlagt rundt `tuned RF` som hovedmodell. "
            f"WBS 5.3 peker nå på `{anbefalte.iloc[0]['modellrolle']}`."
        )

    return df.sort_values("modellrekkefolge").reset_index(drop=True)


def valider_modellvinnere(df: pd.DataFrame) -> pd.DataFrame:
    krav = ["metric", "modellrolle", "antall_vinnermåneder", "andel_vinnermåneder_pct"]
    mangler = [kol for kol in krav if kol not in df.columns]
    if mangler:
        raise ValueError(f"WBS 6.3 mangler kolonner i modellvinner-tabellen: {mangler}")

    if len(df) != 6:
        raise ValueError(f"WBS 6.3 forventer 6 rader i modellvinner-tabellen, men fant {len(df)}.")

    df = df.copy()
    df["modellrekkefolge"] = df["modellrolle"].map(modellorden())
    df["antall_vinnermåneder"] = pd.to_numeric(df["antall_vinnermåneder"], errors="raise").astype(int)
    df["andel_vinnermåneder_pct"] = pd.to_numeric(df["andel_vinnermåneder_pct"], errors="raise")
    return df.sort_values(["metric", "modellrekkefolge"]).reset_index(drop=True)


def valider_viktige_variabler(df: pd.DataFrame) -> pd.DataFrame:
    krav = ["prioritet_5_4", "feature", "importance_tuned_rf_pct"]
    mangler = [kol for kol in krav if kol not in df.columns]
    if mangler:
        raise ValueError(f"WBS 6.3 mangler kolonner i WBS 5.4-oversikten: {mangler}")

    df = df.copy()
    df["prioritet_5_4"] = pd.to_numeric(df["prioritet_5_4"], errors="raise").astype(int)
    df["importance_tuned_rf_pct"] = pd.to_numeric(df["importance_tuned_rf_pct"], errors="raise")
    topp = df.sort_values("prioritet_5_4").iloc[0]
    if int(topp["prioritet_5_4"]) != 1 or topp["feature"] != FORVENTET_TOPPFEATURE:
        raise ValueError(
            "WBS 6.3 forventer at `Discount` er toppsignal i WBS 5.4, "
            f"men fant `{topp['feature']}`."
        )

    return df.sort_values("prioritet_5_4").reset_index(drop=True)


def valider_segmentvinnere(df: pd.DataFrame) -> pd.DataFrame:
    krav = ["segmentdimensjon", "segmentverdi", "rmse_vinner", "mape_vinner", "samme_vinner"]
    mangler = [kol for kol in krav if kol not in df.columns]
    if mangler:
        raise ValueError(f"WBS 6.3 mangler kolonner i segmentvinner-tabellen: {mangler}")

    if len(df) != FORVENTET_SEGMENTRADER:
        raise ValueError(
            f"WBS 6.3 forventer {FORVENTET_SEGMENTRADER} rader i segmentvinner-tabellen, men fant {len(df)}."
        )

    return df.copy()


def valider_modellprofil(df: pd.DataFrame) -> pd.DataFrame:
    krav = [
        "modellrolle",
        "samlet_vurdering_5_3",
        "samlet_rmse_2025",
        "samlet_mape_2025_pct",
        "rmse_vinnermåneder",
        "mape_vinnermåneder",
        "rmse_vinnersegmenter",
        "mape_vinnersegmenter",
        "tolkbarhet_niva",
    ]
    mangler = [kol for kol in krav if kol not in df.columns]
    if mangler:
        raise ValueError(f"WBS 6.3 mangler kolonner i modellprofilen fra 6.2: {mangler}")

    if len(df) != 3:
        raise ValueError(f"WBS 6.3 forventer 3 rader i modellprofilen fra 6.2, men fant {len(df)}.")

    df = df.copy()
    df["modellrekkefolge"] = df["modellrolle"].map(modellorden())
    for kol in [
        "samlet_rmse_2025",
        "samlet_mape_2025_pct",
        "rmse_vinnermåneder",
        "mape_vinnermåneder",
        "rmse_vinnersegmenter",
        "mape_vinnersegmenter",
    ]:
        df[kol] = pd.to_numeric(df[kol], errors="raise")

    tuned = df.loc[df["modellrolle"] == FORVENTET_ANBEFALT_MODELL].reset_index(drop=True)
    if len(tuned) != 1:
        raise ValueError("WBS 6.3 fant ikke nøyaktig én `tuned RF`-rad i modellprofilen fra 6.2.")
    if tuned.iloc[0]["samlet_vurdering_5_3"] != "anbefalt":
        raise ValueError("WBS 6.3 forventer at `tuned RF` er markert som anbefalt i modellprofilen.")

    return df.sort_values("modellrekkefolge").reset_index(drop=True)


def valider_styrker_markdown(markdown: str) -> None:
    forventet = [
        "## Pålitelighet",
        "## Generaliserbarhet",
        "WBS 6.2 gir ikke operative anbefalinger.",
    ]
    mangler = [tekst for tekst in forventet if tekst not in markdown]
    if mangler:
        raise ValueError(f"WBS 6.3 fant ikke forventet tekst i styrker_og_svakheter.md: {mangler}")


def valider_core(core: dict) -> None:
    prosjekt = core.get("project", {})
    prosjektnavn = prosjekt.get("name", "")
    need = core.get("need", "")

    if FORVENTET_CASE not in prosjektnavn:
        raise ValueError(
            "WBS 6.3 forventer at case-navnet i core.json inneholder "
            f"`{FORVENTET_CASE}`, men fant `{prosjektnavn}`."
        )

    for tekstbit in ["innkjøp", "kampanjer", "ressursplanlegging"]:
        if tekstbit not in need:
            raise ValueError(f"WBS 6.3 fant ikke `{tekstbit}` i behovsbeskrivelsen i core.json.")


def hent_tall(df: pd.DataFrame, metric: str, modellrolle: str) -> int:
    rad = df.loc[(df["metric"] == metric) & (df["modellrolle"] == modellrolle)].reset_index(drop=True)
    if len(rad) != 1:
        raise ValueError(f"WBS 6.3 fant ikke entydig rad for metric={metric} og modellrolle={modellrolle}.")
    return int(rad.iloc[0]["antall_vinnermåneder"])


def hent_segmentrad(df: pd.DataFrame, dimensjon: str, verdi: str) -> pd.Series:
    rad = df.loc[(df["segmentdimensjon"] == dimensjon) & (df["segmentverdi"].astype(str) == verdi)].reset_index(drop=True)
    if len(rad) != 1:
        raise ValueError(f"WBS 6.3 fant ikke entydig segmentrad for {dimensjon}={verdi}.")
    return rad.iloc[0]


def bygg_beslutningsmatrise(
    sammenligning_df: pd.DataFrame,
    modellvinnere_df: pd.DataFrame,
    viktige_df: pd.DataFrame,
    segmentvinnere_df: pd.DataFrame,
    modellprofil_df: pd.DataFrame,
) -> pd.DataFrame:
    tuned = modellprofil_df.loc[modellprofil_df["modellrolle"] == "tuned RF"].iloc[0]
    discount = viktige_df.loc[viktige_df["feature"] == "Discount"].iloc[0]
    rabatt_hoy = hent_segmentrad(segmentvinnere_df, "discount_band", "hoy")
    sales_hoy = hent_segmentrad(segmentvinnere_df, "sales_band", "hoyt salg")

    tuned_rmse_maaneder = hent_tall(modellvinnere_df, "RMSE", "tuned RF")
    tuned_rmse_segmenter = int(tuned["rmse_vinnersegmenter"])

    rader = [
        {
            "beslutningsomraade": "innkjøp og lager",
            "formaal": "Støtte overordnet nivåtreff i bestillings- og lagerplanlegging.",
            "anbefalt_modellrolle": "tuned RF",
            "prioritert_metrikk": "RMSE",
            "nokkeltallgrunnlag": (
                f"Samlet RMSE={tuned['samlet_rmse_2025']:.6f}, "
                f"{tuned_rmse_maaneder}/12 vinnermåneder på RMSE og "
                f"{tuned_rmse_segmenter}/14 vinnersegmenter på RMSE."
            ),
            "praktisk_nytte_niva": "høy",
            "anbefalt_bruk": "Bruk tuned RF som standardprognose i månedlig planlegging av innkjøp og lagernivå.",
            "hovedforbehold": "Dette er ikke lageroptimalisering, og prosentfeil kan fortsatt være ujevne i delsegmenter.",
        },
        {
            "beslutningsomraade": "kampanje og rabatt",
            "formaal": "Støtte vurdering av prognoser i rabattutsatte perioder og kampanjer.",
            "anbefalt_modellrolle": "tuned RF",
            "prioritert_metrikk": "RMSE med MAPE-kontroll",
            "nokkeltallgrunnlag": (
                f"Discount er toppsignal i 5.4 ({discount['importance_tuned_rf_pct']:.4f} %), "
                f"tuned RF vinner RMSE ved høy rabatt, mens {rabatt_hoy['mape_vinner']} vinner MAPE i segmentet."
            ),
            "praktisk_nytte_niva": "middels",
            "anbefalt_bruk": "Bruk tuned RF som hovedprognose, men kontroller prosentfeilen mot baseline RF når rabattnivået er høyt.",
            "hovedforbehold": "Rabattsignalene er prediktive, ikke kausale, og bør ikke brukes som bevis for kampanjeeffekt.",
        },
        {
            "beslutningsomraade": "bemanning og ressursplanlegging",
            "formaal": "Støtte aggregert planlegging av belastning over måneder og kvartaler.",
            "anbefalt_modellrolle": "tuned RF",
            "prioritert_metrikk": "RMSE",
            "nokkeltallgrunnlag": (
                f"Tuned RF vinner RMSE i alle fire kvartaler og {tuned_rmse_maaneder}/12 måneder, "
                f"mens {sales_hoy['rmse_vinner']} er best i segmentet hoyt salg."
            ),
            "praktisk_nytte_niva": "middels-høy",
            "anbefalt_bruk": "Bruk tuned RF til aggregert kapasitets- og ressursplanlegging, med ekstra kontroll når salgsnivået er svært høyt.",
            "hovedforbehold": "Dette er ikke butikk- eller skiftoptimalisering, og toppbelastning bør håndteres varsomt.",
        },
        {
            "beslutningsomraade": "ledelsesrapportering",
            "formaal": "Støtte ledelsesnivå med én hovedprognose og én forklaringsnær støttevisning.",
            "anbefalt_modellrolle": "tuned RF",
            "prioritert_metrikk": "RMSE med forklaringsstøtte",
            "nokkeltallgrunnlag": (
                f"Tuned RF er rang 1 på både RMSE og MAPE samlet, "
                f"mens benchmark lineær har tolkbarhet_niva={modellprofil_df.loc[modellprofil_df['modellrolle'] == 'benchmark lineær', 'tolkbarhet_niva'].iloc[0]}."
            ),
            "praktisk_nytte_niva": "middels",
            "anbefalt_bruk": "Rapporter tuned RF som hovedprognose og bruk benchmark lineær som støtte når retningen i sentrale signaler skal forklares.",
            "hovedforbehold": "Lineær modell skal ikke brukes som kausalt bevis for hvorfor salget endrer seg.",
        },
    ]

    beslutningsmatrise_df = pd.DataFrame(rader)
    if len(beslutningsmatrise_df) != FORVENTET_BESLUTNINGSRADER:
        raise ValueError(
            f"WBS 6.3 forventer {FORVENTET_BESLUTNINGSRADER} rader i beslutningsmatrisen, men bygget {len(beslutningsmatrise_df)}."
        )
    return beslutningsmatrise_df


def bygg_bruksregler() -> pd.DataFrame:
    rader = [
        {
            "situasjon": "standard planlegging",
            "primarvalg": "tuned RF",
            "stottesjekk": "benchmark lineær ved behov for enkel forklaring",
            "begrunnelse": "Tuned RF er best samlet og mest stabil på RMSE gjennom året.",
            "anbefalt_handtering": "Bruk tuned RF som standardprognose og hent kun inn benchmark lineær når prognosen må forklares enkelt.",
        },
        {
            "situasjon": "hoy rabatt / prosentfoelsom situasjon",
            "primarvalg": "tuned RF",
            "stottesjekk": "baseline RF på MAPE i segmentet hoy rabatt",
            "begrunnelse": "Discount er toppsignal, og prosentfeilen spriker mer i høyrabatt-situasjoner enn absoluttfeilen.",
            "anbefalt_handtering": "Behold tuned RF som hovedprognose, men bruk baseline RF som ekstra kontroll når prosentfølsomheten er viktig.",
        },
        {
            "situasjon": "hoyt salgsnivaa / toppbelastning",
            "primarvalg": "tuned RF",
            "stottesjekk": "benchmark lineær som ekstra kontroll i hoyt salg",
            "begrunnelse": "Tuned RF er hovedmodell totalt, men benchmark lineær er best i segmentet hoyt salg.",
            "anbefalt_handtering": "Sammenlign tuned RF og benchmark lineær, og behandle tydelig sprik som varsel om høyere usikkerhet i toppbelastning.",
        },
        {
            "situasjon": "forklaringsbehov",
            "primarvalg": "benchmark lineær",
            "stottesjekk": "tuned RF som hovedprognose",
            "begrunnelse": "Benchmark lineær er mest tolkbar, mens tuned RF fortsatt er den beste rene prognosemodellen.",
            "anbefalt_handtering": "Bruk tuned RF for selve prognosetallet, men benchmark lineær for å forklare retningen i sentrale signaler uten å hevde kausalitet.",
        },
    ]

    bruksregler_df = pd.DataFrame(rader)
    if len(bruksregler_df) != FORVENTET_BRUKSREGLER:
        raise ValueError(
            f"WBS 6.3 forventer {FORVENTET_BRUKSREGLER} rader i bruksreglene, men bygget {len(bruksregler_df)}."
        )
    return bruksregler_df


def lag_markdown(beslutningsmatrise_df: pd.DataFrame, bruksregler_df: pd.DataFrame) -> str:
    innkjop = beslutningsmatrise_df.loc[
        beslutningsmatrise_df["beslutningsomraade"] == "innkjøp og lager"
    ].iloc[0]
    kampanje = beslutningsmatrise_df.loc[
        beslutningsmatrise_df["beslutningsomraade"] == "kampanje og rabatt"
    ].iloc[0]
    bemanning = beslutningsmatrise_df.loc[
        beslutningsmatrise_df["beslutningsomraade"] == "bemanning og ressursplanlegging"
    ].iloc[0]
    ledelse = beslutningsmatrise_df.loc[
        beslutningsmatrise_df["beslutningsomraade"] == "ledelsesrapportering"
    ].iloc[0]

    forklaring = bruksregler_df.loc[bruksregler_df["situasjon"] == "forklaringsbehov"].iloc[0]

    linjer = [
        "# Praktisk nytte (WBS 6.3)",
        "",
        "## Hva WBS 6.3 gjør",
        "",
        "- Aktiviteten oversetter eksisterende modellfunn fra WBS 5.3, 5.4, 6.1 og 6.2 til praktisk beslutningsstøtte for Dagligvare.",
        "- WBS 6.3 trener ikke modeller på nytt, lager ikke nye prognoser og beregner ikke nye evalueringsmetrikker.",
        "- Leveransen er semi-kvantitativ: den bruker eksisterende nøkkeltall og segmentmønstre til å si hvordan modellene kan brukes, men uten kroner, lageroptimalisering eller bemanningsalgoritmer.",
        "",
        "## Praktisk nytte per beslutningsområde",
        "",
        f"- **Innkjøp og lager:** `{innkjop['anbefalt_modellrolle']}` er standardvalget når nivåtreff prioriteres, fordi {innkjop['nokkeltallgrunnlag']}",
        f"- **Kampanje og rabatt:** `{kampanje['anbefalt_modellrolle']}` brukes som hovedmodell, men prosentfeilen må kontrolleres særskilt, fordi {kampanje['nokkeltallgrunnlag']}",
        f"- **Bemanning og ressursplanlegging:** `{bemanning['anbefalt_modellrolle']}` kan støtte aggregert kapasitetsplanlegging, fordi {bemanning['nokkeltallgrunnlag']}",
        f"- **Ledelsesrapportering:** `{ledelse['anbefalt_modellrolle']}` bør være hovedprognosen i rapportering oppover, mens `benchmark lineær` brukes som forklaringsstøtte, fordi {ledelse['nokkeltallgrunnlag']}",
        "",
        "## Anbefalt bruk av modellene",
        "",
        "- `tuned RF` bør være standardprognose i Dagligvare når absolutte avvik og stabilitet gjennom året er viktigst.",
        "- `baseline RF` beholdes som kontrollmodell når prosentfeil i høyrabatt-situasjoner er særlig viktig å følge opp.",
        f"- `benchmark lineær` bør brukes når forklaringsbehovet er viktigere enn maksimal prognosepresisjon. I denne situasjonen anbefales `{forklaring['anbefalt_handtering']}`",
        "- Ved svært høyt salgsnivå bør tuned RF sammenlignes med benchmark lineær før prognosen brukes som grunnlag for mer pressede planbeslutninger.",
        "",
        "## Viktige forbehold",
        "",
        "- WBS 6.3 vurderer praktisk nytte innenfor prosjektets faktiske scope og er ikke en operativ beslutningsmodell for lager eller bemanning.",
        "- Rabatt- og regionsignaler er prediktive og ikke kausale, så de kan ikke brukes som bevis for hvorfor salget endrer seg.",
        "- Generaliserbarheten er fortsatt begrenset til ett datasett og én simulert virksomhet, slik WBS 6.2 allerede har dokumentert.",
        "",
        "## Produserte artefakter",
        "",
        f"- `{OUTPUT_BESLUTNINGSMATRISE}`",
        f"- `{OUTPUT_BRUKSREGLER}`",
        f"- `{OUTPUT_MARKDOWN}`",
        "",
        "## Avgrensning mot videre rapportarbeid",
        "",
        "- WBS 6.3 dokumenterer hvordan dagens modellfunn kan brukes i praksis for Dagligvare.",
        "- Full rapportferdigstilling, mer helhetlig konklusjon og videre strukturarbeid ligger fortsatt i WBS 7.x og 8.x.",
    ]
    return "\n".join(linjer) + "\n"


def main() -> None:
    aktivitetsmappe = Path(__file__).resolve().parent
    analyse_rot = aktivitetsmappe.parent
    repo_rot = aktivitetsmappe.parents[2]

    sammenligning_df = les_dataset(analyse_rot / INPUT_MODELLSAMMENLIGNING)
    modellvinnere_df = les_dataset(analyse_rot / INPUT_MODELLVINNERE)
    viktige_df = les_dataset(analyse_rot / INPUT_VIKTIGE_VARIABLER)
    segmentvinnere_df = les_dataset(analyse_rot / INPUT_SEGMENTVINNERE)
    modellprofil_df = les_dataset(analyse_rot / INPUT_MODELLPROFIL)
    styrker_markdown = les_markdown(analyse_rot / INPUT_STYRKER_MARKDOWN)
    core = les_json(repo_rot / "012 fase 2 - plan" / "core.json")

    sammenligning_df = valider_modellsammenligning(sammenligning_df)
    modellvinnere_df = valider_modellvinnere(modellvinnere_df)
    viktige_df = valider_viktige_variabler(viktige_df)
    segmentvinnere_df = valider_segmentvinnere(segmentvinnere_df)
    modellprofil_df = valider_modellprofil(modellprofil_df)
    valider_styrker_markdown(styrker_markdown)
    valider_core(core)

    beslutningsmatrise_df = bygg_beslutningsmatrise(
        sammenligning_df,
        modellvinnere_df,
        viktige_df,
        segmentvinnere_df,
        modellprofil_df,
    )
    bruksregler_df = bygg_bruksregler()
    markdown = lag_markdown(beslutningsmatrise_df, bruksregler_df)

    beslutningsmatrise_df.to_csv(aktivitetsmappe / OUTPUT_BESLUTNINGSMATRISE, index=False, encoding="utf-8")
    bruksregler_df.to_csv(aktivitetsmappe / OUTPUT_BRUKSREGLER, index=False, encoding="utf-8")
    (aktivitetsmappe / OUTPUT_MARKDOWN).write_text(markdown, encoding="utf-8")

    print("WBS 6.3 er gjennomført.")
    print(f"- Skrev {OUTPUT_BESLUTNINGSMATRISE}")
    print(f"- Skrev {OUTPUT_BRUKSREGLER}")
    print(f"- Skrev {OUTPUT_MARKDOWN}")


if __name__ == "__main__":
    main()
