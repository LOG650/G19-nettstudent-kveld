from pathlib import Path

import numpy as np
import pandas as pd
from joblib import load


INPUT_MODELLSAMMENLIGNING = "14_sammenligne_modellresultater/tab_modellsammenligning_oversikt.csv"
INPUT_LR = "08_lineaer_regresjon/tab_lr_koeffisienter.csv"
INPUT_RF_BASELINE = "09_random_forest_regressor/tab_rf_feature_importance.csv"
INPUT_RF_TUNED_MODEL = "11_parameterjustering_random_forest/model_random_forest_tuned.joblib"
INPUT_X_TRAIN = "06_datasplitt/X_train.csv"
MODELLREKKEFOLGE = ["benchmark lineær", "baseline RF", "tuned RF"]
FORVENTET_FEATUREANTALL = 67
TOPP_N = 10
KALENDERFEATURES = {"year", "quarter", "month", "weekofyear", "dayofweek", "dayofmonth", "is_weekend"}


def les_dataset(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path, encoding="utf-8-sig")
    if df.shape[1] == 1:
        df = pd.read_csv(csv_path, sep=";", encoding="utf-8-sig")
    return df


def modellorden() -> dict[str, int]:
    return {navn: indeks for indeks, navn in enumerate(MODELLREKKEFOLGE)}


def variabelgruppe(feature: str) -> str:
    if feature == "Discount":
        return "pris/kampanje"
    if feature in KALENDERFEATURES:
        return "kalender"
    if feature.startswith("Region_"):
        return "region"
    if feature.startswith("City_"):
        return "by"
    if feature.startswith("Category_"):
        return "kategori"
    if feature.startswith("Sub Category_"):
        return "underkategori"
    raise ValueError(f"Ukjent featuregruppe for `{feature}` i WBS 5.4.")


def valider_modellsammenligning(oversikt_df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    krav = ["modellnavn", "modellrolle", "samlet_vurdering_5_3"]
    mangler = [kol for kol in krav if kol not in oversikt_df.columns]
    if mangler:
        raise ValueError(f"WBS 5.4 mangler nødvendige kolonner i WBS 5.3-oversikten: {mangler}")

    if len(oversikt_df) != len(MODELLREKKEFOLGE):
        raise ValueError(
            f"WBS 5.4 forventer {len(MODELLREKKEFOLGE)} modellrader i WBS 5.3-oversikten, men fant {len(oversikt_df)}."
        )

    oversikt_df = oversikt_df.copy()
    oversikt_df["modellrekkefolge"] = oversikt_df["modellrolle"].map(modellorden())
    if oversikt_df["modellrekkefolge"].isna().any():
        roller = oversikt_df["modellrolle"].tolist()
        raise ValueError(f"WBS 5.4 fant ukjente modellroller i WBS 5.3-oversikten: {roller}")

    anbefalte = oversikt_df.loc[oversikt_df["samlet_vurdering_5_3"] == "anbefalt"].reset_index(drop=True)
    if len(anbefalte) != 1:
        raise ValueError(f"WBS 5.4 forventer nøyaktig én anbefalt modell fra WBS 5.3, men fant {len(anbefalte)}.")

    anbefalt = anbefalte.iloc[0]
    if anbefalt["modellrolle"] != "tuned RF":
        raise ValueError(
            "WBS 5.4 er definert med `tuned RF` som hovedgrunnlag. "
            f"WBS 5.3 peker nå på `{anbefalt['modellrolle']}` og planen må i så fall revideres eksplisitt."
        )

    return oversikt_df.sort_values("modellrekkefolge").reset_index(drop=True), anbefalt


def valider_lr_signaler(lr_df: pd.DataFrame, forventede_features: list[str]) -> pd.DataFrame:
    krav = ["feature", "koeffisient", "abs_koeffisient", "fortegn", "rang_abs"]
    mangler = [kol for kol in krav if kol not in lr_df.columns]
    if mangler:
        raise ValueError(f"WBS 5.4 mangler nødvendige kolonner i lineær regresjon-tabellen: {mangler}")

    lr_df = lr_df.copy()
    lr_df["koeffisient"] = pd.to_numeric(lr_df["koeffisient"], errors="raise")
    lr_df["abs_koeffisient"] = pd.to_numeric(lr_df["abs_koeffisient"], errors="raise")
    lr_df["rang_abs"] = pd.to_numeric(lr_df["rang_abs"], errors="raise").astype(int)
    if lr_df["feature"].duplicated().any():
        raise ValueError("WBS 5.4 fant dupliserte feature-navn i lineær regresjon-tabellen.")

    featureliste = lr_df["feature"].tolist()
    valider_featuresett(featureliste, forventede_features, "lineær regresjon")
    lr_df["variabelgruppe"] = lr_df["feature"].map(variabelgruppe)
    return lr_df.sort_values("rang_abs").reset_index(drop=True)


def valider_rf_baseline(rf_df: pd.DataFrame, forventede_features: list[str]) -> pd.DataFrame:
    krav = ["feature", "importance", "importance_pct", "rang_importance"]
    mangler = [kol for kol in krav if kol not in rf_df.columns]
    if mangler:
        raise ValueError(f"WBS 5.4 mangler nødvendige kolonner i baseline RF-tabellen: {mangler}")

    rf_df = rf_df.copy()
    rf_df["importance"] = pd.to_numeric(rf_df["importance"], errors="raise")
    rf_df["importance_pct"] = pd.to_numeric(rf_df["importance_pct"], errors="raise")
    rf_df["rang_importance"] = pd.to_numeric(rf_df["rang_importance"], errors="raise").astype(int)
    if rf_df["feature"].duplicated().any():
        raise ValueError("WBS 5.4 fant dupliserte feature-navn i baseline RF-tabellen.")

    featureliste = rf_df["feature"].tolist()
    valider_featuresett(featureliste, forventede_features, "baseline RF")
    rf_df["variabelgruppe"] = rf_df["feature"].map(variabelgruppe)
    return rf_df.sort_values("rang_importance").reset_index(drop=True)


def bygg_tuned_rf_signaler(modell_path: Path, x_train_path: Path) -> tuple[pd.DataFrame, list[str]]:
    modell = load(modell_path)
    x_train = les_dataset(x_train_path)
    featureliste = x_train.columns.tolist()

    if len(featureliste) != FORVENTET_FEATUREANTALL:
        raise ValueError(
            f"WBS 5.4 forventer {FORVENTET_FEATUREANTALL} features i X_train, men fant {len(featureliste)}."
        )

    feature_importances = getattr(modell, "feature_importances_", None)
    if feature_importances is None:
        raise ValueError("Den tunede modellen mangler `feature_importances_` og kan ikke brukes i WBS 5.4.")

    if len(feature_importances) != len(featureliste):
        raise ValueError(
            "Lengden på `feature_importances_` matcher ikke kolonnene i X_train. "
            f"Fant {len(feature_importances)} importance-verdier og {len(featureliste)} feature-kolonner."
        )

    tuned_df = pd.DataFrame(
        {
            "feature": featureliste,
            "importance": pd.to_numeric(feature_importances, errors="raise"),
        }
    )
    if tuned_df["importance"].isna().any() or not np.isfinite(tuned_df["importance"]).all():
        raise ValueError("Tuned RF inneholder NaN eller ikke-endelige importance-verdier.")

    tuned_df["importance_pct"] = tuned_df["importance"] * 100
    tuned_df["variabelgruppe"] = tuned_df["feature"].map(variabelgruppe)
    tuned_df = tuned_df.sort_values(["importance", "feature"], ascending=[False, True]).reset_index(drop=True)
    tuned_df["rang_importance"] = tuned_df.index + 1
    tuned_df["importance"] = tuned_df["importance"].round(6)
    tuned_df["importance_pct"] = tuned_df["importance_pct"].round(4)
    return tuned_df, featureliste


def valider_featuresett(featureliste: list[str], forventede_features: list[str], navn: str) -> None:
    if len(featureliste) != FORVENTET_FEATUREANTALL:
        raise ValueError(f"WBS 5.4 forventer {FORVENTET_FEATUREANTALL} features i {navn}, men fant {len(featureliste)}.")

    if sorted(featureliste) != sorted(forventede_features):
        mangler = sorted(set(forventede_features) - set(featureliste))
        ekstra = sorted(set(featureliste) - set(forventede_features))
        raise ValueError(
            f"WBS 5.4 fant avvik mellom {navn} og X_train. Mangler: {mangler}. Ekstra: {ekstra}."
        )


def bygg_toppsignaler_per_modell(
    modellsammenligning_df: pd.DataFrame,
    lr_df: pd.DataFrame,
    baseline_df: pd.DataFrame,
    tuned_df: pd.DataFrame,
) -> pd.DataFrame:
    metadata = modellsammenligning_df.set_index("modellrolle")["modellnavn"].to_dict()
    kildeartefakter = {
        "benchmark lineær": INPUT_LR,
        "baseline RF": INPUT_RF_BASELINE,
        "tuned RF": INPUT_RF_TUNED_MODEL,
    }
    rader: list[dict[str, object]] = []

    for modellrolle in MODELLREKKEFOLGE:
        if modellrolle == "benchmark lineær":
            topp = lr_df.head(TOPP_N)
            for rad in topp.itertuples(index=False):
                rader.append(
                    {
                        "modellnavn": metadata[modellrolle],
                        "modellrolle": modellrolle,
                        "signal_metrikk": "abs_koeffisient",
                        "feature": rad.feature,
                        "variabelgruppe": rad.variabelgruppe,
                        "signal_verdi": round(float(rad.abs_koeffisient), 6),
                        "fortegn": rad.fortegn,
                        "rang_i_modell": int(rad.rang_abs),
                        "kilde_artefakt": kildeartefakter[modellrolle],
                    }
                )
        else:
            rf_df = baseline_df if modellrolle == "baseline RF" else tuned_df
            topp = rf_df.head(TOPP_N)
            for rad in topp.itertuples(index=False):
                rader.append(
                    {
                        "modellnavn": metadata[modellrolle],
                        "modellrolle": modellrolle,
                        "signal_metrikk": "importance_pct",
                        "feature": rad.feature,
                        "variabelgruppe": rad.variabelgruppe,
                        "signal_verdi": round(float(rad.importance_pct), 4),
                        "fortegn": "",
                        "rang_i_modell": int(rad.rang_importance),
                        "kilde_artefakt": kildeartefakter[modellrolle],
                    }
                )

    toppsignaler_df = pd.DataFrame(rader)
    toppsignaler_df["modellrekkefolge"] = toppsignaler_df["modellrolle"].map(modellorden())
    toppsignaler_df = toppsignaler_df.sort_values(["modellrekkefolge", "rang_i_modell"]).reset_index(drop=True)
    return toppsignaler_df.drop(columns=["modellrekkefolge"])


def bygg_rf_stabilitet_topp10(baseline_df: pd.DataFrame, tuned_df: pd.DataFrame) -> pd.DataFrame:
    baseline_top = baseline_df.head(TOPP_N)[["feature", "variabelgruppe", "rang_importance", "importance_pct"]].copy()
    baseline_top = baseline_top.rename(
        columns={
            "rang_importance": "rang_baseline_rf",
            "importance_pct": "importance_baseline_rf_pct",
        }
    )
    tuned_top = tuned_df.head(TOPP_N)[["feature", "variabelgruppe", "rang_importance", "importance_pct"]].copy()
    tuned_top = tuned_top.rename(
        columns={
            "rang_importance": "rang_tuned_rf",
            "importance_pct": "importance_tuned_rf_pct",
        }
    )

    stabilitet_df = baseline_top.merge(
        tuned_top[["feature", "rang_tuned_rf", "importance_tuned_rf_pct"]],
        on="feature",
        how="outer",
    )
    stabilitet_df["variabelgruppe"] = stabilitet_df["feature"].map(variabelgruppe)

    def status(rad: pd.Series) -> str:
        finnes_baseline = pd.notna(rad["rang_baseline_rf"])
        finnes_tuned = pd.notna(rad["rang_tuned_rf"])
        if finnes_baseline and finnes_tuned:
            return "topp10 i begge"
        if finnes_baseline:
            return "kun baseline topp10"
        return "kun tuned topp10"

    stabilitet_df["status_rf_topp10"] = stabilitet_df.apply(status, axis=1)
    stabilitet_df["sort_tuned"] = stabilitet_df["rang_tuned_rf"].fillna(999).astype(int)
    stabilitet_df["sort_baseline"] = stabilitet_df["rang_baseline_rf"].fillna(999).astype(int)
    stabilitet_df = stabilitet_df.sort_values(["sort_tuned", "sort_baseline", "feature"]).reset_index(drop=True)

    for kol in ["rang_baseline_rf", "rang_tuned_rf"]:
        stabilitet_df[kol] = stabilitet_df[kol].astype("Int64")
    for kol in ["importance_baseline_rf_pct", "importance_tuned_rf_pct"]:
        stabilitet_df[kol] = stabilitet_df[kol].round(4)

    return stabilitet_df[
        [
            "feature",
            "variabelgruppe",
            "rang_baseline_rf",
            "importance_baseline_rf_pct",
            "rang_tuned_rf",
            "importance_tuned_rf_pct",
            "status_rf_topp10",
        ]
    ]


def bygg_viktige_variabler_oversikt(
    lr_df: pd.DataFrame,
    baseline_df: pd.DataFrame,
    tuned_df: pd.DataFrame,
    stabilitet_df: pd.DataFrame,
) -> pd.DataFrame:
    topp_tuned = tuned_df.head(TOPP_N)[["feature", "variabelgruppe", "rang_importance", "importance_pct"]].copy()
    topp_tuned = topp_tuned.rename(
        columns={
            "rang_importance": "rang_tuned_rf",
            "importance_pct": "importance_tuned_rf_pct",
        }
    )
    baseline_info = baseline_df[["feature", "rang_importance", "importance_pct"]].copy().rename(
        columns={
            "rang_importance": "rang_baseline_rf",
            "importance_pct": "importance_baseline_rf_pct",
        }
    )
    lr_info = lr_df[["feature", "rang_abs", "koeffisient", "fortegn"]].copy().rename(
        columns={
            "rang_abs": "rang_lineaer_abs",
            "koeffisient": "koeffisient_lineaer",
            "fortegn": "fortegn_lineaer",
        }
    )
    status_info = stabilitet_df[["feature", "status_rf_topp10"]].copy()

    oversikt_df = topp_tuned.merge(baseline_info, on="feature", how="left")
    oversikt_df = oversikt_df.merge(lr_info, on="feature", how="left")
    oversikt_df = oversikt_df.merge(status_info, on="feature", how="left")
    oversikt_df["prioritet_5_4"] = oversikt_df["rang_tuned_rf"].astype(int)
    oversikt_df["rang_baseline_rf"] = oversikt_df["rang_baseline_rf"].astype("Int64")
    oversikt_df["rang_lineaer_abs"] = oversikt_df["rang_lineaer_abs"].astype("Int64")
    oversikt_df["importance_tuned_rf_pct"] = oversikt_df["importance_tuned_rf_pct"].round(4)
    oversikt_df["importance_baseline_rf_pct"] = oversikt_df["importance_baseline_rf_pct"].round(4)
    oversikt_df["koeffisient_lineaer"] = oversikt_df["koeffisient_lineaer"].round(6)
    return oversikt_df[
        [
            "prioritet_5_4",
            "feature",
            "variabelgruppe",
            "rang_tuned_rf",
            "importance_tuned_rf_pct",
            "rang_baseline_rf",
            "importance_baseline_rf_pct",
            "rang_lineaer_abs",
            "koeffisient_lineaer",
            "fortegn_lineaer",
            "status_rf_topp10",
        ]
    ].sort_values("prioritet_5_4").reset_index(drop=True)


def bygg_variabelgrupper_topp10(topp_tuned_df: pd.DataFrame) -> pd.DataFrame:
    gruppe_df = (
        topp_tuned_df.groupby("variabelgruppe", as_index=False)
        .agg(
            antall_i_topp10=("feature", "size"),
            sum_importance_pct_topp10=("importance_pct", "sum"),
        )
        .sort_values(["sum_importance_pct_topp10", "variabelgruppe"], ascending=[False, True])
        .reset_index(drop=True)
    )
    gruppe_df["sum_importance_pct_topp10"] = gruppe_df["sum_importance_pct_topp10"].round(4)
    return gruppe_df


def skriv_markdown(
    md_path: Path,
    anbefalt_rad: pd.Series,
    toppsignaler_df: pd.DataFrame,
    stabilitet_df: pd.DataFrame,
    viktige_df: pd.DataFrame,
    grupper_df: pd.DataFrame,
) -> None:
    lr_topp = toppsignaler_df.loc[toppsignaler_df["modellrolle"] == "benchmark lineær"].reset_index(drop=True)
    baseline_topp = toppsignaler_df.loc[toppsignaler_df["modellrolle"] == "baseline RF"].reset_index(drop=True)
    tuned_topp = toppsignaler_df.loc[toppsignaler_df["modellrolle"] == "tuned RF"].reset_index(drop=True)

    kun_tuned = stabilitet_df.loc[stabilitet_df["status_rf_topp10"] == "kun tuned topp10", "feature"].tolist()
    kun_baseline = stabilitet_df.loc[stabilitet_df["status_rf_topp10"] == "kun baseline topp10", "feature"].tolist()
    overlapp = int((stabilitet_df["status_rf_topp10"] == "topp10 i begge").sum())
    topp10_liste = viktige_df["feature"].tolist()
    kalender_gruppe = grupper_df.loc[grupper_df["variabelgruppe"] == "kalender"].iloc[0]
    pris_gruppe = grupper_df.loc[grupper_df["variabelgruppe"] == "pris/kampanje"].iloc[0]
    region_gruppe = grupper_df.loc[grupper_df["variabelgruppe"] == "region"].iloc[0]

    lines = [
        "# Analyse av viktige variabler (WBS 5.4)",
        "",
        "## Hva WBS 5.4 gjør",
        "",
        "- Aktiviteten identifiserer og rangerer viktige variabler med utgangspunkt i eksisterende modellartefakter fra WBS 4.x og den anbefalte modellen fra WBS 5.3.",
        f"- `{anbefalt_rad['modellrolle']}` brukes som hovedkilde fordi modellen er markert som `anbefalt` i WBS 5.3.",
        "- `baseline RF` brukes som stabilitetskontroll for Random Forest-signaler, mens lineær regresjon brukes som støttespor for fortegn og relativ plassering på overlappende variabler.",
        "",
        "## Prioritert variabelliste",
        "",
        f"- WBS 5.4 rangerer disse variablene høyest i `{anbefalt_rad['modellrolle']}`: {', '.join(f'`{feature}`' for feature in topp10_liste)}.",
        (
            f"- Topp 3 i `{anbefalt_rad['modellrolle']}` er "
            f"`{viktige_df.iloc[0]['feature']}` ({float(viktige_df.iloc[0]['importance_tuned_rf_pct']):.4f} %), "
            f"`{viktige_df.iloc[1]['feature']}` ({float(viktige_df.iloc[1]['importance_tuned_rf_pct']):.4f} %) og "
            f"`{viktige_df.iloc[2]['feature']}` ({float(viktige_df.iloc[2]['importance_tuned_rf_pct']):.4f} %)."
        ),
        (
            f"- Gruppeoppsummeringen viser at `kalender` dominerer topp 10 med "
            f"`{int(kalender_gruppe['antall_i_topp10'])}` variabler og "
            f"`{float(kalender_gruppe['sum_importance_pct_topp10']):.4f} %` samlet importance."
        ),
        (
            f"- `pris/kampanje` bidrar med én variabel (`Discount`) og "
            f"`{float(pris_gruppe['sum_importance_pct_topp10']):.4f} %`, mens `region` bidrar med "
            f"`{int(region_gruppe['antall_i_topp10'])}` variabler og "
            f"`{float(region_gruppe['sum_importance_pct_topp10']):.4f} %`."
        ),
        "",
        "## RF-stabilitet mot baseline",
        "",
        f"- `baseline RF` og `tuned RF` deler `{overlapp}` av `{len(stabilitet_df)}` features i unionen av topp 10-signalene.",
        f"- Kun i `tuned RF`-topp 10: {', '.join(f'`{feature}`' for feature in kun_tuned)}.",
        f"- Kun i `baseline RF`-topp 10: {', '.join(f'`{feature}`' for feature in kun_baseline)}.",
        f"- Toppsignal i `baseline RF`: `{baseline_topp.iloc[0]['feature']}` ({float(baseline_topp.iloc[0]['signal_verdi']):.4f} %).",
        f"- Toppsignal i `tuned RF`: `{tuned_topp.iloc[0]['feature']}` ({float(tuned_topp.iloc[0]['signal_verdi']):.4f} %).",
        "",
        "## Lineær regresjon som støttespor",
        "",
        (
            f"- Toppsignal i lineær regresjon er `{lr_topp.iloc[0]['feature']}` "
            f"med `{lr_topp.iloc[0]['fortegn']}` fortegn og `|koeff|={float(lr_topp.iloc[0]['signal_verdi']):.6f}`."
        ),
        "- `Discount` er høyt prioritert i både lineær regresjon og begge Random Forest-varianter, og lineær regresjon gir her et negativt fortegn.",
        "- `Region_East`, `Region_West` og `Region_Central` ligger høyt i `tuned RF` og har også positive koeffisienter i lineær regresjon.",
        "- Flere kalendervariabler ligger svært høyt i `tuned RF`, men lavere i lineær regresjon. Dette dokumenteres som modellforskjell, ikke som årsaksforklaring.",
        "",
        "## Produserte artefakter",
        "",
        "- `tab_rf_tuned_feature_importance.csv`",
        "- `tab_toppsignaler_per_modell.csv`",
        "- `tab_rf_stabilitet_topp10.csv`",
        "- `tab_viktige_variabler_oversikt.csv`",
        "- `tab_variabelgrupper_tuned_top10.csv`",
        "- `variabelanalyse.md`",
        "",
        "## Avgrensning mot senere WBS-steg",
        "",
        "- WBS 5.4 identifiserer og rangerer viktige variabler, men gjør ikke kausal analyse, SHAP, residualdiagnostikk eller full diskusjon av modellstyrker og svakheter.",
        "- Dypere faglig tolkning, diskusjon og praktisk vurdering ligger fortsatt i WBS 6.1, 6.2 og 6.3.",
        "",
    ]
    md_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    aktivitetsmappe = Path(__file__).resolve().parent
    repo_aktiviteter = Path(__file__).resolve().parents[1]

    modellsammenligning_df = les_dataset(repo_aktiviteter / INPUT_MODELLSAMMENLIGNING)
    lr_df = les_dataset(repo_aktiviteter / INPUT_LR)
    baseline_df = les_dataset(repo_aktiviteter / INPUT_RF_BASELINE)

    modellsammenligning_df, anbefalt_rad = valider_modellsammenligning(modellsammenligning_df)
    tuned_df, forventede_features = bygg_tuned_rf_signaler(
        repo_aktiviteter / INPUT_RF_TUNED_MODEL,
        repo_aktiviteter / INPUT_X_TRAIN,
    )
    lr_df = valider_lr_signaler(lr_df, forventede_features)
    baseline_df = valider_rf_baseline(baseline_df, forventede_features)

    toppsignaler_df = bygg_toppsignaler_per_modell(modellsammenligning_df, lr_df, baseline_df, tuned_df)
    stabilitet_df = bygg_rf_stabilitet_topp10(baseline_df, tuned_df)
    viktige_df = bygg_viktige_variabler_oversikt(lr_df, baseline_df, tuned_df, stabilitet_df)
    grupper_df = bygg_variabelgrupper_topp10(tuned_df.head(TOPP_N))

    tuned_output_df = tuned_df[["feature", "variabelgruppe", "importance", "importance_pct", "rang_importance"]]

    tuned_path = aktivitetsmappe / "tab_rf_tuned_feature_importance.csv"
    toppsignaler_path = aktivitetsmappe / "tab_toppsignaler_per_modell.csv"
    stabilitet_path = aktivitetsmappe / "tab_rf_stabilitet_topp10.csv"
    viktige_path = aktivitetsmappe / "tab_viktige_variabler_oversikt.csv"
    grupper_path = aktivitetsmappe / "tab_variabelgrupper_tuned_top10.csv"
    markdown_path = aktivitetsmappe / "variabelanalyse.md"

    tuned_path.write_text(tuned_output_df.to_csv(index=False), encoding="utf-8")
    toppsignaler_path.write_text(toppsignaler_df.to_csv(index=False), encoding="utf-8")
    stabilitet_path.write_text(stabilitet_df.to_csv(index=False), encoding="utf-8")
    viktige_path.write_text(viktige_df.to_csv(index=False), encoding="utf-8")
    grupper_path.write_text(grupper_df.to_csv(index=False), encoding="utf-8")
    skriv_markdown(markdown_path, anbefalt_rad, toppsignaler_df, stabilitet_df, viktige_df, grupper_df)

    print("WBS 5.4 ferdig: viktige variabler analysert")
    print(f"- Anbefalt modell fra WBS 5.3: {anbefalt_rad['modellrolle']}")
    print(f"- Topp 3 tuned RF: {', '.join(viktige_df.head(3)['feature'].tolist())}")
    print(f"- RF-overlapp i topp 10: {int((stabilitet_df['status_rf_topp10'] == 'topp10 i begge').sum())}")
    print(f"- {tuned_path.name}")
    print(f"- {toppsignaler_path.name}")
    print(f"- {stabilitet_path.name}")
    print(f"- {viktige_path.name}")
    print(f"- {grupper_path.name}")
    print(f"- {markdown_path.name}")


if __name__ == "__main__":
    main()
