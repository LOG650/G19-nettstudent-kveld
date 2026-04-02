from pathlib import Path

import pandas as pd


FELLES_INPUTFELT = [
    "input_features",
    "input_target",
    "antall_treningsrader",
    "antall_features",
    "target_kolonne",
]

MODELLKONFIGURASJONER = [
    {
        "modellnavn": "LinearRegression",
        "oversikt_fil": "08_lineaer_regresjon/tab_lr_modelloversikt.csv",
        "signal_fil": "08_lineaer_regresjon/tab_lr_koeffisienter.csv",
        "detaljtabell": "08_lineaer_regresjon/tab_lr_koeffisienter.csv",
        "markdown_fil": "08_lineaer_regresjon/lineaer_regresjon.md",
        "modell_fil": "08_lineaer_regresjon/model_lineaer_regresjon.joblib",
        "signal_metrikk": "abs_koeffisient",
        "signal_verdi_kolonne": "abs_koeffisient",
        "signal_rang_kolonne": "rang_abs",
        "fortegn_kolonne": "fortegn",
    },
    {
        "modellnavn": "RandomForestRegressor",
        "oversikt_fil": "09_random_forest_regressor/tab_rf_modelloversikt.csv",
        "signal_fil": "09_random_forest_regressor/tab_rf_feature_importance.csv",
        "detaljtabell": "09_random_forest_regressor/tab_rf_feature_importance.csv",
        "markdown_fil": "09_random_forest_regressor/random_forest_regressor.md",
        "modell_fil": "09_random_forest_regressor/model_random_forest_regressor.joblib",
        "signal_metrikk": "importance",
        "signal_verdi_kolonne": "importance",
        "signal_rang_kolonne": "rang_importance",
        "fortegn_kolonne": "",
    },
]


def les_csv(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path, encoding="utf-8-sig")
    if df.shape[1] == 1:
        df = pd.read_csv(csv_path, sep=";", encoding="utf-8-sig")
    return df


def les_pakrevd_csv(repo_aktiviteter: Path, rel_path: str) -> pd.DataFrame:
    csv_path = repo_aktiviteter / rel_path
    if not csv_path.exists():
        raise FileNotFoundError(f"Fant ikke påkrevd inputfil for WBS 4.3: {csv_path}")
    return les_csv(csv_path)


def valider_oversikt(oversikt_df: pd.DataFrame, modellnavn: str) -> pd.Series:
    if oversikt_df.empty:
        raise ValueError(f"Modelloversikten for {modellnavn} er tom.")

    if len(oversikt_df) != 1:
        raise ValueError(
            f"Modelloversikten for {modellnavn} skal ha nøyaktig én rad, men har {len(oversikt_df)}."
        )

    mangler = [felt for felt in ["modellnavn", *FELLES_INPUTFELT] if felt not in oversikt_df.columns]
    if mangler:
        raise ValueError(f"Modelloversikten for {modellnavn} mangler kolonner: {mangler}")

    rad = oversikt_df.iloc[0]
    if str(rad["modellnavn"]) != modellnavn:
        raise ValueError(
            f"Forventet modellnavn `{modellnavn}` i modelloversikten, men fant `{rad['modellnavn']}`."
        )

    return rad


def valider_signaler(signal_df: pd.DataFrame, modellkonfig: dict[str, str]) -> pd.DataFrame:
    if signal_df.empty:
        raise ValueError(f"Signaltabellen for {modellkonfig['modellnavn']} er tom.")

    paakrevde = {"feature", modellkonfig["signal_verdi_kolonne"], modellkonfig["signal_rang_kolonne"]}
    if modellkonfig["fortegn_kolonne"]:
        paakrevde.add(modellkonfig["fortegn_kolonne"])

    mangler = [kol for kol in paakrevde if kol not in signal_df.columns]
    if mangler:
        raise ValueError(
            f"Signaltabellen for {modellkonfig['modellnavn']} mangler kolonner: {sorted(mangler)}"
        )

    return signal_df


def verifiser_felles_input(oversikter: list[pd.Series]) -> dict[str, str | int]:
    basis = {
        "input_features": str(oversikter[0]["input_features"]),
        "input_target": str(oversikter[0]["input_target"]),
        "antall_treningsrader": int(oversikter[0]["antall_treningsrader"]),
        "antall_features": int(oversikter[0]["antall_features"]),
        "target_kolonne": str(oversikter[0]["target_kolonne"]),
    }

    avvik: list[str] = []
    for rad in oversikter[1:]:
        for felt in FELLES_INPUTFELT:
            sammenligningsverdi = basis[felt]
            kandidatverdi = rad[felt]
            if felt in {"antall_treningsrader", "antall_features"}:
                kandidatverdi = int(kandidatverdi)
            else:
                kandidatverdi = str(kandidatverdi)

            if kandidatverdi != sammenligningsverdi:
                avvik.append(
                    f"{felt}: forventet `{sammenligningsverdi}`, fant `{kandidatverdi}` for `{rad['modellnavn']}`"
                )

    if avvik:
        raise ValueError(
            "WBS 4.3 krever felles treningsgrunnlag for begge modellene, men fant avvik i "
            + "; ".join(avvik)
        )

    return basis


def lag_oversiktstabell(
    repo_aktiviteter: Path,
    oversikter: list[pd.Series],
) -> pd.DataFrame:
    rader = []
    for modellkonfig, oversikt in zip(MODELLKONFIGURASJONER, oversikter, strict=True):
        modell_fil = repo_aktiviteter / modellkonfig["modell_fil"]
        rader.append(
            {
                "modellnavn": modellkonfig["modellnavn"],
                "input_features": str(oversikt["input_features"]),
                "input_target": str(oversikt["input_target"]),
                "antall_treningsrader": int(oversikt["antall_treningsrader"]),
                "antall_features": int(oversikt["antall_features"]),
                "target_kolonne": str(oversikt["target_kolonne"]),
                "detaljtabell": modellkonfig["detaljtabell"],
                "markdown_fil": modellkonfig["markdown_fil"],
                "lokal_modellfil_funnet": modell_fil.exists(),
                "felles_input_ok": True,
            }
        )

    return pd.DataFrame(rader)


def lag_signaltabell(signal_df_liste: list[pd.DataFrame]) -> pd.DataFrame:
    samlerader: list[dict[str, str | int | float]] = []
    for modellkonfig, signal_df in zip(MODELLKONFIGURASJONER, signal_df_liste, strict=True):
        rangkolonne = modellkonfig["signal_rang_kolonne"]
        verdikolonne = modellkonfig["signal_verdi_kolonne"]
        fortegnkolonne = modellkonfig["fortegn_kolonne"]

        topp_df = signal_df.sort_values(rangkolonne).head(5)
        for rad in topp_df.itertuples(index=False):
            rad_dict = rad._asdict()
            samlerader.append(
                {
                    "modellnavn": modellkonfig["modellnavn"],
                    "feature": str(rad_dict["feature"]),
                    "signal_metrikk": modellkonfig["signal_metrikk"],
                    "signal_verdi": round(float(rad_dict[verdikolonne]), 6),
                    "fortegn": str(rad_dict[fortegnkolonne]) if fortegnkolonne else "",
                    "rang": int(rad_dict[rangkolonne]),
                }
            )

    return pd.DataFrame(samlerader)


def skriv_markdown(
    md_path: Path,
    felles_input: dict[str, str | int],
    oversikt_df: pd.DataFrame,
    signal_df: pd.DataFrame,
) -> None:
    lokal_fil_status = [
        f"- `{rad.modellnavn}` lokal modellfil funnet: {'ja' if rad.lokal_modellfil_funnet else 'nei'}"
        for rad in oversikt_df.itertuples(index=False)
    ]
    topplinjer = [
        f"- `{rad.modellnavn}` rang {rad.rang}: `{rad.feature}` ({rad.signal_metrikk} = {rad.signal_verdi:.6f})"
        + (f", fortegn: {rad.fortegn}" if rad.fortegn else "")
        for rad in signal_df.itertuples(index=False)
        if rad.rang <= 3
    ]

    lines = [
        "# Felles treningsoppsummering (WBS 4.3)",
        "",
        "## Hva WBS 4.3 gjør",
        "",
        "- WBS 4.1 gjennomførte selve treningen av lineær regresjon.",
        "- WBS 4.2 gjennomførte selve treningen av Random Forest Regressor.",
        "- WBS 4.3 trener ikke modellene på nytt, men verifiserer at de bygger på samme treningsgrunnlag og samler de viktigste modellinterne signalene.",
        "",
        "## Verifisert felles treningsgrunnlag",
        "",
        f"- Input features: `{felles_input['input_features']}`",
        f"- Input target: `{felles_input['input_target']}`",
        f"- Antall treningsrader: {felles_input['antall_treningsrader']}",
        f"- Antall features: {felles_input['antall_features']}",
        f"- Target-kolonne: `{felles_input['target_kolonne']}`",
        "",
        "## Produserte artefakter",
        "",
        "- `tab_modelltrening_oversikt.csv`",
        "- `tab_modellsignaler_oversikt.csv`",
        "- `modelltrening_verifisering.md`",
        "",
        "## Lokal modellfilstatus",
        "",
        *lokal_fil_status,
        "",
        "## Utdrag av samlede modellsignaler",
        "",
        "- De fem sterkeste signalene per modell er samlet i `tab_modellsignaler_oversikt.csv`.",
        *topplinjer,
        "",
        "## Avgrensning",
        "",
        "- Aktiviteten produserer ikke nye prediksjoner, residualfiler, treningsmetrikker, testmetrikker, `RMSE`, `MAPE`, prognoser eller figurer.",
        "- Videre evaluering og modellvurdering er utsatt til WBS 5.x og WBS 6.1.",
        "",
    ]
    md_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    aktivitetsmappe = Path(__file__).resolve().parent
    repo_aktiviteter = Path(__file__).resolve().parents[1]

    oversikter: list[pd.Series] = []
    signal_df_liste: list[pd.DataFrame] = []

    for modellkonfig in MODELLKONFIGURASJONER:
        oversikt_df = les_pakrevd_csv(repo_aktiviteter, modellkonfig["oversikt_fil"])
        signal_df = les_pakrevd_csv(repo_aktiviteter, modellkonfig["signal_fil"])
        oversikter.append(valider_oversikt(oversikt_df, modellkonfig["modellnavn"]))
        signal_df_liste.append(valider_signaler(signal_df, modellkonfig))

    felles_input = verifiser_felles_input(oversikter)
    oversiktstabell_df = lag_oversiktstabell(repo_aktiviteter, oversikter)
    signaltabell_df = lag_signaltabell(signal_df_liste)

    oversikt_path = aktivitetsmappe / "tab_modelltrening_oversikt.csv"
    oversikt_path.write_text(oversiktstabell_df.to_csv(index=False), encoding="utf-8")

    signal_path = aktivitetsmappe / "tab_modellsignaler_oversikt.csv"
    signal_path.write_text(signaltabell_df.to_csv(index=False), encoding="utf-8")

    md_path = aktivitetsmappe / "modelltrening_verifisering.md"
    skriv_markdown(md_path, felles_input, oversiktstabell_df, signaltabell_df)

    print("WBS 4.3 ferdig: felles treningsgrunnlag verifisert")
    print(f"- Treningsrader: {felles_input['antall_treningsrader']}")
    print(f"- Features: {felles_input['antall_features']}")
    print(f"- Modeller verifisert: {len(oversiktstabell_df)}")
    print(f"- {oversikt_path.name}")
    print(f"- {signal_path.name}")
    print(f"- {md_path.name}")


if __name__ == "__main__":
    main()
