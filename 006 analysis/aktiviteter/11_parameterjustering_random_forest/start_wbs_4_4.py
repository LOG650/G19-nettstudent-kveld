import time
from itertools import product
from pathlib import Path

import pandas as pd
from joblib import dump
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_percentage_error, root_mean_squared_error


TARGET_KOLONNE = "Sales"
AAR_KOLONNE = "year"
MODELLNAVN = "RandomForestRegressor"
INPUT_FEATURES = "06_datasplitt/X_train.csv"
INPUT_TARGET = "06_datasplitt/y_train.csv"
SOKETRENING_AAR = [2022, 2023]
VALIDERINGSAAR = 2024
SELECTION_METRIC = "RMSE"
FASTE_PARAMETRE = {
    "bootstrap": True,
    "random_state": 42,
    "n_jobs": -1,
}
PARAMETERGRID = {
    "n_estimators": [200, 400],
    "max_depth": [None, 10, 20],
    "min_samples_leaf": [1, 2, 4],
    "max_features": [1.0, "sqrt"],
}
BASELINE_PARAMETRE = {
    **FASTE_PARAMETRE,
    "n_estimators": 200,
    "max_depth": None,
    "min_samples_leaf": 1,
    "max_features": 1.0,
}


def les_dataset(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path, encoding="utf-8-sig")
    if df.shape[1] == 1:
        df = pd.read_csv(csv_path, sep=";", encoding="utf-8-sig")
    return df


def valider_input(x_train: pd.DataFrame, y_train: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    if x_train.empty:
        raise ValueError("X_train.csv er tom. Kjør WBS 3.3 på nytt før WBS 4.4.")

    if y_train.empty:
        raise ValueError("y_train.csv er tom. Kjør WBS 3.3 på nytt før WBS 4.4.")

    if len(x_train) != len(y_train):
        raise ValueError(
            f"Radantall matcher ikke mellom X_train ({len(x_train)}) og y_train ({len(y_train)})."
        )

    if y_train.shape[1] != 1:
        raise ValueError(f"y_train.csv skal ha én kolonne, men har {y_train.shape[1]}.")

    target_kolonne = y_train.columns[0]
    if target_kolonne != TARGET_KOLONNE:
        raise ValueError(f"Forventet target-kolonne `{TARGET_KOLONNE}`, men fant `{target_kolonne}`.")

    if AAR_KOLONNE not in x_train.columns:
        raise ValueError(f"X_train.csv må inneholde `{AAR_KOLONNE}` for tidsbasert validering i WBS 4.4.")

    ikke_numeriske = [kol for kol in x_train.columns if not pd.api.types.is_numeric_dtype(x_train[kol])]
    if ikke_numeriske:
        raise ValueError(
            "Alle feature-kolonner må være numeriske i WBS 4.4. "
            f"Fant ikke-numeriske kolonner: {ikke_numeriske}"
        )

    if not pd.api.types.is_numeric_dtype(y_train[target_kolonne]):
        raise ValueError(f"Target-kolonnen `{target_kolonne}` må være numerisk.")

    x_train = x_train.apply(pd.to_numeric, errors="raise")
    y_train = y_train.copy()
    y_train[target_kolonne] = pd.to_numeric(y_train[target_kolonne], errors="raise")

    unike_aar = sorted(x_train[AAR_KOLONNE].astype(int).unique().tolist())
    forventede_aar = sorted([*SOKETRENING_AAR, VALIDERINGSAAR])
    if unike_aar != forventede_aar:
        raise ValueError(
            f"WBS 4.4 forventer treningsår {forventede_aar} i X_train.csv, men fant {unike_aar}."
        )

    if (y_train[TARGET_KOLONNE] <= 0).any():
        raise ValueError("WBS 4.4 forventer positive Sales-verdier for å kunne rapportere MAPE direkte.")

    return x_train, y_train


def format_param_verdi(verdi: object) -> str:
    if verdi is None:
        return "None"
    return str(verdi)


def bygg_kandidater() -> list[dict[str, object]]:
    kandidater: list[dict[str, object]] = []
    kombinasjoner = product(
        PARAMETERGRID["n_estimators"],
        PARAMETERGRID["max_depth"],
        PARAMETERGRID["min_samples_leaf"],
        PARAMETERGRID["max_features"],
    )

    for indeks, (n_estimators, max_depth, min_samples_leaf, max_features) in enumerate(kombinasjoner, start=1):
        parametre = {
            **FASTE_PARAMETRE,
            "n_estimators": n_estimators,
            "max_depth": max_depth,
            "min_samples_leaf": min_samples_leaf,
            "max_features": max_features,
        }
        kandidater.append(
            {
                "kandidat_id": f"rf_tune_{indeks:02d}",
                "grid_rekkefolge": indeks,
                "er_baseline": parametre == BASELINE_PARAMETRE,
                "parametre": parametre,
            }
        )

    return kandidater


def del_tuningdata(
    x_train: pd.DataFrame,
    y_train: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    sokemaske = x_train[AAR_KOLONNE].astype(int).isin(SOKETRENING_AAR)
    valideringsmaske = x_train[AAR_KOLONNE].astype(int) == VALIDERINGSAAR

    x_sok = x_train.loc[sokemaske].copy()
    y_sok = y_train.loc[sokemaske].copy()
    x_validering = x_train.loc[valideringsmaske].copy()
    y_validering = y_train.loc[valideringsmaske].copy()

    if x_sok.empty or x_validering.empty:
        raise ValueError("WBS 4.4 fikk tomt søke- eller valideringssett. Kontroller year-kolonnen i X_train.")

    return x_sok, y_sok, x_validering, y_validering


def evaluer_kandidat(
    parametre: dict[str, object],
    x_sok: pd.DataFrame,
    y_sok: pd.DataFrame,
    x_validering: pd.DataFrame,
    y_validering: pd.DataFrame,
) -> tuple[float, float, float]:
    modell = RandomForestRegressor(**parametre)
    start_tid = time.perf_counter()
    modell.fit(x_sok, y_sok[TARGET_KOLONNE])
    fit_seconds = time.perf_counter() - start_tid

    prediksjoner = modell.predict(x_validering)
    rmse = float(root_mean_squared_error(y_validering[TARGET_KOLONNE], prediksjoner))
    mape_pct = float(mean_absolute_percentage_error(y_validering[TARGET_KOLONNE], prediksjoner) * 100)
    return rmse, mape_pct, fit_seconds


def lag_kandidattabell(
    kandidater: list[dict[str, object]],
    x_sok: pd.DataFrame,
    y_sok: pd.DataFrame,
    x_validering: pd.DataFrame,
    y_validering: pd.DataFrame,
) -> pd.DataFrame:
    rader: list[dict[str, object]] = []

    for kandidat in kandidater:
        parametre = kandidat["parametre"]
        rmse, mape_pct, fit_seconds = evaluer_kandidat(
            parametre,
            x_sok,
            y_sok,
            x_validering,
            y_validering,
        )
        rader.append(
            {
                "kandidat_id": kandidat["kandidat_id"],
                "er_baseline": kandidat["er_baseline"],
                "n_estimators": int(parametre["n_estimators"]),
                "max_depth": format_param_verdi(parametre["max_depth"]),
                "min_samples_leaf": int(parametre["min_samples_leaf"]),
                "max_features": format_param_verdi(parametre["max_features"]),
                "train_år": ",".join(str(aar) for aar in SOKETRENING_AAR),
                "valideringsår": str(VALIDERINGSAAR),
                "train_rader": int(len(x_sok)),
                "valideringsrader": int(len(x_validering)),
                "rmse_validering": rmse,
                "mape_validering_pct": mape_pct,
                "fit_seconds": fit_seconds,
                "_grid_rekkefolge": kandidat["grid_rekkefolge"],
            }
        )

    kandidater_df = pd.DataFrame(rader)
    kandidater_df = kandidater_df.sort_values(
        ["rmse_validering", "mape_validering_pct", "_grid_rekkefolge"],
        ascending=[True, True, True],
    ).reset_index(drop=True)
    kandidater_df["rang_rmse"] = kandidater_df.index + 1
    kandidater_df["rmse_validering"] = kandidater_df["rmse_validering"].round(6)
    kandidater_df["mape_validering_pct"] = kandidater_df["mape_validering_pct"].round(4)
    kandidater_df["fit_seconds"] = kandidater_df["fit_seconds"].round(6)
    return kandidater_df.drop(columns=["_grid_rekkefolge"])


def finn_baseline_og_vinner(kandidater_df: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    vinnerrad = kandidater_df.iloc[0]
    baselinerader = kandidater_df.loc[kandidater_df["er_baseline"] == True]

    if len(baselinerader) != 1:
        raise ValueError(
            f"Forventet nøyaktig én baseline-rad i tuningtabellen, men fant {len(baselinerader)}."
        )

    return vinnerrad, baselinerader.iloc[0]


def lag_vinnertabell(vinnerrad: pd.Series, baselinerad: pd.Series) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "kandidat_id": vinnerrad["kandidat_id"],
                "n_estimators": int(vinnerrad["n_estimators"]),
                "max_depth": str(vinnerrad["max_depth"]),
                "min_samples_leaf": int(vinnerrad["min_samples_leaf"]),
                "max_features": str(vinnerrad["max_features"]),
                "rmse_validering": float(vinnerrad["rmse_validering"]),
                "mape_validering_pct": float(vinnerrad["mape_validering_pct"]),
                "baseline_rmse_validering": float(baselinerad["rmse_validering"]),
                "baseline_mape_validering_pct": float(baselinerad["mape_validering_pct"]),
                "delta_rmse_mot_baseline": round(
                    float(vinnerrad["rmse_validering"]) - float(baselinerad["rmse_validering"]),
                    6,
                ),
                "delta_mape_mot_baseline_pct": round(
                    float(vinnerrad["mape_validering_pct"]) - float(baselinerad["mape_validering_pct"]),
                    4,
                ),
                "selection_metric": SELECTION_METRIC,
            }
        ]
    )


def parse_max_depth(verdi: str) -> int | None:
    if verdi == "None":
        return None
    return int(verdi)


def parse_max_features(verdi: str) -> float | str:
    if verdi == "sqrt":
        return verdi
    return float(verdi)


def bygg_vinnerparametre(vinnerrad: pd.Series) -> dict[str, object]:
    return {
        **FASTE_PARAMETRE,
        "n_estimators": int(vinnerrad["n_estimators"]),
        "max_depth": parse_max_depth(str(vinnerrad["max_depth"])),
        "min_samples_leaf": int(vinnerrad["min_samples_leaf"]),
        "max_features": parse_max_features(str(vinnerrad["max_features"])),
    }


def retren_modell(x_train: pd.DataFrame, y_train: pd.DataFrame, parametre: dict[str, object]) -> tuple[RandomForestRegressor, float]:
    modell = RandomForestRegressor(**parametre)
    start_tid = time.perf_counter()
    modell.fit(x_train, y_train[TARGET_KOLONNE])
    fit_seconds = time.perf_counter() - start_tid
    return modell, fit_seconds


def lag_modelloversikt(
    x_train: pd.DataFrame,
    vinnerrad: pd.Series,
    baselinerad: pd.Series,
    fit_seconds_full_train: float,
) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "modellnavn": MODELLNAVN,
                "input_features": INPUT_FEATURES,
                "input_target": INPUT_TARGET,
                "antall_treningsrader": int(len(x_train)),
                "antall_features": int(x_train.shape[1]),
                "target_kolonne": TARGET_KOLONNE,
                "n_estimators": int(vinnerrad["n_estimators"]),
                "max_depth": str(vinnerrad["max_depth"]),
                "min_samples_leaf": int(vinnerrad["min_samples_leaf"]),
                "max_features": str(vinnerrad["max_features"]),
                "bootstrap": FASTE_PARAMETRE["bootstrap"],
                "random_state": FASTE_PARAMETRE["random_state"],
                "n_jobs": FASTE_PARAMETRE["n_jobs"],
                "selection_metric": SELECTION_METRIC,
                "baseline_rmse_validering": float(baselinerad["rmse_validering"]),
                "baseline_mape_validering_pct": float(baselinerad["mape_validering_pct"]),
                "vinner_rmse_validering": float(vinnerrad["rmse_validering"]),
                "vinner_mape_validering_pct": float(vinnerrad["mape_validering_pct"]),
                "fit_seconds_full_train": round(float(fit_seconds_full_train), 6),
            }
        ]
    )


def skriv_markdown(
    md_path: Path,
    kandidater_df: pd.DataFrame,
    vinnerrad: pd.Series,
    baselinerad: pd.Series,
    fit_seconds_full_train: float,
) -> None:
    topp5_df = kandidater_df.head(5)
    toppliste = [
        f"- Rang {rad.rang_rmse}: `{rad.kandidat_id}` med `RMSE={rad.rmse_validering:.6f}` og `MAPE={rad.mape_validering_pct:.4f} %`"
        for rad in topp5_df.itertuples(index=False)
    ]

    winner_endret = "ja" if vinnerrad["kandidat_id"] != baselinerad["kandidat_id"] else "nei"

    lines = [
        "# Random Forest tuning (WBS 4.4)",
        "",
        "## Avgrensning og formål",
        "",
        "- WBS 4.4 justerer kun parametere for `RandomForestRegressor`.",
        "- Lineær regresjon beholdes uendret som fast benchmark fra WBS 4.1.",
        "- WBS 4.4 bruker ikke 2025-data i tuning eller modellvalg.",
        "",
        "## Valideringsoppsett",
        "",
        f"- Søketrening: `{', '.join(str(aar) for aar in SOKETRENING_AAR)}`",
        f"- Valideringsår: `{VALIDERINGSAAR}`",
        f"- Antall kandidater testet: {len(kandidater_df)}",
        "- Valg av vinner gjøres på lavest `RMSE` på valideringsåret, med `MAPE` som sekundær metrikk ved likt resultat.",
        "",
        "## Vinnerkonfigurasjon",
        "",
        f"- `n_estimators={int(vinnerrad['n_estimators'])}`",
        f"- `max_depth={vinnerrad['max_depth']}`",
        f"- `min_samples_leaf={int(vinnerrad['min_samples_leaf'])}`",
        f"- `max_features={vinnerrad['max_features']}`",
        f"- Validerings-`RMSE`: `{float(vinnerrad['rmse_validering']):.6f}`",
        f"- Validerings-`MAPE`: `{float(vinnerrad['mape_validering_pct']):.4f} %`",
        f"- Baseline endret: `{winner_endret}`",
        f"- Retrening på hele 2022-2024 tok `{fit_seconds_full_train:.6f}` sekunder.",
        "",
        "## Toppkandidater",
        "",
        *toppliste,
        "",
        "## Produserte artefakter",
        "",
        "- `model_random_forest_tuned.joblib`",
        "- `tab_rf_tuning_kandidater.csv`",
        "- `tab_rf_tuning_vinner.csv`",
        "- `tab_rf_tuned_modelloversikt.csv`",
        "- `random_forest_tuning.md`",
        "",
        "## Avgrensning mot senere WBS-steg",
        "",
        "- Tuningen er gjort mot 2024 som intern validering, mens 2025 fortsatt er reservert for videre prognoser og evaluering i WBS 5.x.",
        "- Aktiviteten produserer ikke prognosefiler for 2025 og beregner ikke endelige test-`RMSE` eller test-`MAPE`.",
        "- Baseline-artefaktene i `09_random_forest_regressor` er bevart uendret som sammenligningspunkt.",
        "",
    ]
    md_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    aktivitetsmappe = Path(__file__).resolve().parent
    repo_root = Path(__file__).resolve().parents[3]
    input_x_path = repo_root / "006 analysis" / "aktiviteter" / "06_datasplitt" / "X_train.csv"
    input_y_path = repo_root / "006 analysis" / "aktiviteter" / "06_datasplitt" / "y_train.csv"

    if not input_x_path.exists():
        raise FileNotFoundError(f"Fant ikke feature-matrise: {input_x_path}. Kjør WBS 3.3 først.")

    if not input_y_path.exists():
        raise FileNotFoundError(f"Fant ikke target-fil: {input_y_path}. Kjør WBS 3.3 først.")

    x_train = les_dataset(input_x_path)
    y_train = les_dataset(input_y_path)
    x_train, y_train = valider_input(x_train, y_train)

    kandidater = bygg_kandidater()
    if len(kandidater) != 36:
        raise ValueError(f"WBS 4.4 forventer 36 kandidater, men bygde {len(kandidater)}.")

    x_sok, y_sok, x_validering, y_validering = del_tuningdata(x_train, y_train)
    kandidater_df = lag_kandidattabell(kandidater, x_sok, y_sok, x_validering, y_validering)
    vinnerrad, baselinerad = finn_baseline_og_vinner(kandidater_df)
    vinnertabell_df = lag_vinnertabell(vinnerrad, baselinerad)

    vinnerparametre = bygg_vinnerparametre(vinnerrad)
    modell, fit_seconds_full_train = retren_modell(x_train, y_train, vinnerparametre)
    modelloversikt_df = lag_modelloversikt(x_train, vinnerrad, baselinerad, fit_seconds_full_train)

    modell_path = aktivitetsmappe / "model_random_forest_tuned.joblib"
    dump(modell, modell_path)

    kandidater_path = aktivitetsmappe / "tab_rf_tuning_kandidater.csv"
    kandidater_path.write_text(kandidater_df.to_csv(index=False), encoding="utf-8")

    vinner_path = aktivitetsmappe / "tab_rf_tuning_vinner.csv"
    vinner_path.write_text(vinnertabell_df.to_csv(index=False), encoding="utf-8")

    oversikt_path = aktivitetsmappe / "tab_rf_tuned_modelloversikt.csv"
    oversikt_path.write_text(modelloversikt_df.to_csv(index=False), encoding="utf-8")

    md_path = aktivitetsmappe / "random_forest_tuning.md"
    skriv_markdown(md_path, kandidater_df, vinnerrad, baselinerad, fit_seconds_full_train)

    print("WBS 4.4 ferdig: Random Forest-parametere justert")
    print(f"- Kandidater testet: {len(kandidater_df)}")
    print(f"- Valideringsår: {VALIDERINGSAAR}")
    print(f"- Vinner: {vinnerrad['kandidat_id']}")
    print(f"- Vinner-RMSE: {float(vinnerrad['rmse_validering']):.6f}")
    print(f"- {modell_path.name}")
    print(f"- {kandidater_path.name}")
    print(f"- {vinner_path.name}")
    print(f"- {oversikt_path.name}")
    print(f"- {md_path.name}")


if __name__ == "__main__":
    main()
