from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_percentage_error, root_mean_squared_error


TARGET_KOLONNE = "Sales_faktisk"
DATO_KOLONNE = "Order Date"
FORVENTET_TESTAAR = 2025
FORVENTET_RADER = 3312
FORVENTET_MAANEDER = 12
INPUT_PROGNOSE_DETALJ = "12_prognoser_2025/tab_prognoser_2025_detalj.csv"
INPUT_MODELLOVERSIKT = "12_prognoser_2025/tab_prognosemodeller_oversikt.csv"
KRAV_TIL_MODELLKOLONNER = ["modellnavn", "modellrolle", "prediksjonskolonne"]


def les_dataset(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path, encoding="utf-8-sig")
    if df.shape[1] == 1:
        df = pd.read_csv(csv_path, sep=";", encoding="utf-8-sig")
    return df


def valider_modelloversikt(modell_df: pd.DataFrame) -> pd.DataFrame:
    mangler = [kol for kol in KRAV_TIL_MODELLKOLONNER if kol not in modell_df.columns]
    if mangler:
        raise ValueError(f"Modelloversikten mangler nødvendige kolonner for WBS 5.2: {mangler}")

    if modell_df.empty:
        raise ValueError("Modelloversikten er tom. Kjør WBS 5.1 på nytt før WBS 5.2.")

    if modell_df["prediksjonskolonne"].duplicated().any():
        duplikater = modell_df.loc[modell_df["prediksjonskolonne"].duplicated(), "prediksjonskolonne"].tolist()
        raise ValueError(f"Modelloversikten inneholder dupliserte prediksjonskolonner: {duplikater}")

    return modell_df[KRAV_TIL_MODELLKOLONNER].copy().reset_index(drop=True)


def valider_prognosedata(detalj_df: pd.DataFrame, modell_df: pd.DataFrame) -> pd.DataFrame:
    base_kolonner = [DATO_KOLONNE, TARGET_KOLONNE, "month"]
    prognosekolonner = modell_df["prediksjonskolonne"].tolist()
    mangler = [kol for kol in [*base_kolonner, *prognosekolonner] if kol not in detalj_df.columns]
    if mangler:
        raise ValueError(f"Prognosedetaljene mangler nødvendige kolonner for WBS 5.2: {mangler}")

    if len(detalj_df) != FORVENTET_RADER:
        raise ValueError(
            f"WBS 5.2 forventer {FORVENTET_RADER} rader i prognosedetaljene, men fant {len(detalj_df)}."
        )

    detalj_df = detalj_df.copy()
    detalj_df[TARGET_KOLONNE] = pd.to_numeric(detalj_df[TARGET_KOLONNE], errors="raise")
    if (detalj_df[TARGET_KOLONNE] <= 0).any():
        raise ValueError("WBS 5.2 forventer positive faktiske salgsverdier for å kunne rapportere MAPE direkte.")

    if detalj_df[TARGET_KOLONNE].isna().any():
        raise ValueError(f"Target-kolonnen `{TARGET_KOLONNE}` inneholder NaN-verdier.")

    for kol in prognosekolonner:
        detalj_df[kol] = pd.to_numeric(detalj_df[kol], errors="raise")
        if detalj_df[kol].isna().any():
            raise ValueError(f"Prediksjonskolonnen `{kol}` inneholder NaN-verdier.")
        if not np.isfinite(detalj_df[kol]).all():
            raise ValueError(f"Prediksjonskolonnen `{kol}` inneholder ikke-endelige verdier.")

    datoer = pd.to_datetime(detalj_df[DATO_KOLONNE], format="%Y-%m-%d", errors="raise")
    if not (datoer.dt.year == FORVENTET_TESTAAR).all():
        raise ValueError(f"WBS 5.2 forventer at alle datoer tilhører {FORVENTET_TESTAAR}.")

    detalj_df[DATO_KOLONNE] = datoer.dt.strftime("%Y-%m-%d")
    detalj_df["år_måned"] = datoer.dt.strftime("%Y-%m")
    unike_maaneder = detalj_df["år_måned"].drop_duplicates().tolist()
    if len(unike_maaneder) != FORVENTET_MAANEDER:
        raise ValueError(
            f"WBS 5.2 forventer {FORVENTET_MAANEDER} unike måneder i prognosedetaljene, men fant {len(unike_maaneder)}."
        )

    forventet_maanedsliste = [f"{FORVENTET_TESTAAR}-{maaned:02d}" for maaned in range(1, FORVENTET_MAANEDER + 1)]
    if sorted(unike_maaneder) != forventet_maanedsliste:
        raise ValueError(
            "WBS 5.2 forventer full månedsdekning fra januar til desember 2025, "
            f"men fant {sorted(unike_maaneder)}."
        )

    detalj_df["month"] = pd.to_numeric(detalj_df["month"], errors="raise").astype(int)
    return detalj_df


def beregn_metrikker(faktisk: pd.Series, prognose: pd.Series) -> tuple[float, float]:
    rmse = float(root_mean_squared_error(faktisk, prognose))
    mape_pct = float(mean_absolute_percentage_error(faktisk, prognose) * 100)
    return rmse, mape_pct


def lag_oversiktstabell(detalj_df: pd.DataFrame, modell_df: pd.DataFrame) -> pd.DataFrame:
    rader: list[dict[str, object]] = []
    faktisk = detalj_df[TARGET_KOLONNE]

    for modellrad in modell_df.itertuples(index=False):
        rmse, mape_pct = beregn_metrikker(faktisk, detalj_df[modellrad.prediksjonskolonne])
        rader.append(
            {
                "modellnavn": modellrad.modellnavn,
                "modellrolle": modellrad.modellrolle,
                "prediksjonskolonne": modellrad.prediksjonskolonne,
                "antall_observasjoner": int(len(detalj_df)),
                "rmse_2025": round(rmse, 6),
                "mape_2025_pct": round(mape_pct, 4),
            }
        )

    return pd.DataFrame(rader)


def lag_maanedstabell(detalj_df: pd.DataFrame, modell_df: pd.DataFrame) -> pd.DataFrame:
    rader: list[dict[str, object]] = []

    for år_måned, gruppe in detalj_df.groupby("år_måned", sort=True):
        month = int(gruppe["month"].iloc[0])
        faktisk = gruppe[TARGET_KOLONNE]
        for modellrad in modell_df.itertuples(index=False):
            rmse, mape_pct = beregn_metrikker(faktisk, gruppe[modellrad.prediksjonskolonne])
            rader.append(
                {
                    "år_måned": år_måned,
                    "month": month,
                    "modellnavn": modellrad.modellnavn,
                    "modellrolle": modellrad.modellrolle,
                    "prediksjonskolonne": modellrad.prediksjonskolonne,
                    "antall_rader": int(len(gruppe)),
                    "rmse_maaned": round(rmse, 6),
                    "mape_maaned_pct": round(mape_pct, 4),
                }
            )

    maaned_df = pd.DataFrame(rader)
    return maaned_df.sort_values(["år_måned", "month"]).reset_index(drop=True)


def lag_feildetaljer(detalj_df: pd.DataFrame, modell_df: pd.DataFrame) -> pd.DataFrame:
    detalj_med_feil = detalj_df.drop(columns=["år_måned"]).copy()

    for modellrad in modell_df.itertuples(index=False):
        suffix = modellrad.prediksjonskolonne.removeprefix("prognose_")
        feilkolonne = f"feil_{suffix}"
        abskolonne = f"abs_feil_{suffix}"
        apekolonne = f"ape_{suffix}_pct"

        feil = detalj_med_feil[modellrad.prediksjonskolonne] - detalj_med_feil[TARGET_KOLONNE]
        abs_feil = feil.abs()
        ape_pct = (abs_feil / detalj_med_feil[TARGET_KOLONNE]) * 100

        detalj_med_feil[feilkolonne] = feil.round(6)
        detalj_med_feil[abskolonne] = abs_feil.round(6)
        detalj_med_feil[apekolonne] = ape_pct.round(4)

    return detalj_med_feil


def skriv_markdown(
    md_path: Path,
    oversikt_df: pd.DataFrame,
    maaned_df: pd.DataFrame,
    feildetalj_df: pd.DataFrame,
) -> None:
    resultatlinjer = [
        f"- `{rad.modellrolle}`: `RMSE={rad.rmse_2025:.6f}` og `MAPE={rad.mape_2025_pct:.4f} %`"
        for rad in oversikt_df.itertuples(index=False)
    ]
    første_maaned = maaned_df.iloc[0]["år_måned"]
    siste_maaned = maaned_df.iloc[-1]["år_måned"]

    lines = [
        "# RMSE og MAPE for 2025 (WBS 5.2)",
        "",
        "## Hva WBS 5.2 gjør",
        "",
        "- Aktiviteten beregner test-`RMSE` og test-`MAPE` for de tre modellsporene fra WBS 5.1.",
        "- Resultatene dokumenteres både samlet for hele 2025, per måned og som detaljert feilgrunnlag på radnivå.",
        "- WBS 5.2 rangerer ikke modellene; selve sammenligningen og tolkningen er utsatt til WBS 5.3.",
        "",
        "## Datagrunnlag",
        "",
        f"- Input detaljtabell: `{INPUT_PROGNOSE_DETALJ}`",
        f"- Input modelloversikt: `{INPUT_MODELLOVERSIKT}`",
        f"- Antall 2025-observasjoner: {len(feildetalj_df)}",
        f"- Månedlig dekning: `{første_maaned}` til `{siste_maaned}`",
        "",
        "## Metrikkdefinisjon",
        "",
        "- `RMSE` beregnes som `root_mean_squared_error(faktisk, prognose)`.",
        "- `MAPE` beregnes som `mean_absolute_percentage_error(faktisk, prognose) * 100` og rapporteres i prosent.",
        "",
        "## Samlede 2025-resultater",
        "",
        *resultatlinjer,
        "",
        "## Produserte artefakter",
        "",
        "- `tab_rmse_mape_oversikt.csv`",
        "- `tab_rmse_mape_maaned.csv`",
        "- `tab_prognosefeil_2025_detalj.csv`",
        "- `rmse_mape.md`",
        "",
        "## Avgrensning mot senere WBS-steg",
        "",
        "- WBS 5.2 gjør ikke modellrangering, anbefaling, figurer eller tolkning av hvorfor en modell gjør det bedre enn en annen.",
        "- WBS 5.3 bruker metrikktabellene og feilgrunnlaget fra WBS 5.2 som input til selve sammenligningen av modellresultater.",
        "",
    ]
    md_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    aktivitetsmappe = Path(__file__).resolve().parent
    repo_aktiviteter = Path(__file__).resolve().parents[1]

    detalj_df = les_dataset(repo_aktiviteter / INPUT_PROGNOSE_DETALJ)
    modell_df = les_dataset(repo_aktiviteter / INPUT_MODELLOVERSIKT)

    modell_df = valider_modelloversikt(modell_df)
    detalj_df = valider_prognosedata(detalj_df, modell_df)

    oversikt_df = lag_oversiktstabell(detalj_df, modell_df)
    maaned_df = lag_maanedstabell(detalj_df, modell_df)
    feildetalj_df = lag_feildetaljer(detalj_df, modell_df)

    oversikt_path = aktivitetsmappe / "tab_rmse_mape_oversikt.csv"
    oversikt_path.write_text(oversikt_df.to_csv(index=False), encoding="utf-8")

    maaned_path = aktivitetsmappe / "tab_rmse_mape_maaned.csv"
    maaned_path.write_text(maaned_df.to_csv(index=False), encoding="utf-8")

    detalj_path = aktivitetsmappe / "tab_prognosefeil_2025_detalj.csv"
    detalj_path.write_text(feildetalj_df.to_csv(index=False), encoding="utf-8")

    markdown_path = aktivitetsmappe / "rmse_mape.md"
    skriv_markdown(markdown_path, oversikt_df, maaned_df, feildetalj_df)

    print("WBS 5.2 ferdig: RMSE og MAPE beregnet for 2025")
    print(f"- Observasjoner: {len(feildetalj_df)}")
    print(f"- Månedlige metrikkrader: {len(maaned_df)}")
    print(f"- Modellspor: {len(oversikt_df)}")
    print(f"- {oversikt_path.name}")
    print(f"- {maaned_path.name}")
    print(f"- {detalj_path.name}")
    print(f"- {markdown_path.name}")


if __name__ == "__main__":
    main()
