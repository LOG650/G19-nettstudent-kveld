import time
from pathlib import Path

import pandas as pd
from joblib import dump
from sklearn.ensemble import RandomForestRegressor


TARGET_KOLONNE = "Sales"
MODELLNAVN = "RandomForestRegressor"
INPUT_FEATURES = "06_datasplitt/X_train.csv"
INPUT_TARGET = "06_datasplitt/y_train.csv"
BASELINE_PARAMETRE = {
    "n_estimators": 200,
    "random_state": 42,
    "n_jobs": -1,
}


def les_dataset(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path, encoding="utf-8-sig")
    if df.shape[1] == 1:
        df = pd.read_csv(csv_path, sep=";", encoding="utf-8-sig")
    return df


def valider_input(x_train: pd.DataFrame, y_train: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    if x_train.empty:
        raise ValueError("X_train.csv er tom. Kjør WBS 3.3 på nytt før WBS 4.2.")

    if y_train.empty:
        raise ValueError("y_train.csv er tom. Kjør WBS 3.3 på nytt før WBS 4.2.")

    if len(x_train) != len(y_train):
        raise ValueError(
            f"Radantall matcher ikke mellom X_train ({len(x_train)}) og y_train ({len(y_train)})."
        )

    if y_train.shape[1] != 1:
        raise ValueError(f"y_train.csv skal ha én kolonne, men har {y_train.shape[1]}.")

    target_kolonne = y_train.columns[0]
    if target_kolonne != TARGET_KOLONNE:
        raise ValueError(f"Forventet target-kolonne `{TARGET_KOLONNE}`, men fant `{target_kolonne}`.")

    ikke_numeriske = [kol for kol in x_train.columns if not pd.api.types.is_numeric_dtype(x_train[kol])]
    if ikke_numeriske:
        raise ValueError(
            "Alle feature-kolonner må være numeriske i WBS 4.2. "
            f"Fant ikke-numeriske kolonner: {ikke_numeriske}"
        )

    if not pd.api.types.is_numeric_dtype(y_train[target_kolonne]):
        raise ValueError(f"Target-kolonnen `{target_kolonne}` må være numerisk.")

    x_train = x_train.apply(pd.to_numeric, errors="raise")
    y_train = y_train.copy()
    y_train[target_kolonne] = pd.to_numeric(y_train[target_kolonne], errors="raise")
    return x_train, y_train


def lag_modelloversikt(
    x_train: pd.DataFrame,
    fit_seconds: float,
    modell: RandomForestRegressor,
) -> pd.DataFrame:
    parametere = modell.get_params()
    return pd.DataFrame(
        [
            {
                "modellnavn": MODELLNAVN,
                "input_features": INPUT_FEATURES,
                "input_target": INPUT_TARGET,
                "antall_treningsrader": int(len(x_train)),
                "antall_features": int(x_train.shape[1]),
                "target_kolonne": TARGET_KOLONNE,
                "n_estimators": int(parametere["n_estimators"]),
                "random_state": int(parametere["random_state"]),
                "n_jobs": int(parametere["n_jobs"]),
                "bootstrap": bool(parametere["bootstrap"]),
                "max_depth": parametere["max_depth"],
                "min_samples_leaf": parametere["min_samples_leaf"],
                "max_features": parametere["max_features"],
                "fit_seconds": round(float(fit_seconds), 6),
            }
        ]
    )


def lag_importance_tabell(modell: RandomForestRegressor, kolonner: list[str]) -> pd.DataFrame:
    importance_df = pd.DataFrame(
        {
            "feature": kolonner,
            "importance": [float(verdi) for verdi in modell.feature_importances_],
        }
    )
    importance_df = importance_df.sort_values(["importance", "feature"], ascending=[False, True]).reset_index(drop=True)
    importance_df["importance_pct"] = importance_df["importance"] * 100
    importance_df["rang_importance"] = importance_df.index + 1
    importance_df["importance"] = importance_df["importance"].round(6)
    importance_df["importance_pct"] = importance_df["importance_pct"].round(4)
    return importance_df[["feature", "importance", "importance_pct", "rang_importance"]]


def skriv_markdown(
    md_path: Path,
    modelloversikt_df: pd.DataFrame,
    importance_df: pd.DataFrame,
) -> None:
    topp = importance_df.head(5)
    topp_liste = [
        f"- `{rad.feature}` (importance = {rad.importance:.6f}, {rad.importance_pct:.2f} %)"
        for rad in topp.itertuples(index=False)
    ]

    lines = [
        "# Random Forest Regressor (WBS 4.2)",
        "",
        "## Datagrunnlag",
        "",
        f"- Input features: `{INPUT_FEATURES}`",
        f"- Input target: `{INPUT_TARGET}`",
        f"- Antall treningsrader: {int(modelloversikt_df.loc[0, 'antall_treningsrader'])}",
        f"- Antall features: {int(modelloversikt_df.loc[0, 'antall_features'])}",
        "",
        "## Modellvalg",
        "",
        "- Benchmark-varianten er `RandomForestRegressor` fra `scikit-learn`.",
        "- Baseline-parametre er `n_estimators=200`, `random_state=42` og `n_jobs=-1`.",
        "- Øvrige parametre bruker `scikit-learn`-default for installert versjon i analysemiljøet.",
        f"- Treningstiden i denne kjøringen var `{float(modelloversikt_df.loc[0, 'fit_seconds']):.6f}` sekunder.",
        "",
        "## Produserte artefakter",
        "",
        "- `model_random_forest_regressor.joblib`",
        "- `tab_rf_modelloversikt.csv`",
        "- `tab_rf_feature_importance.csv`",
        "- `random_forest_regressor.md`",
        "",
        "## Foreløpige feature-signaler",
        "",
        "- De fem viktigste feature-signalene i denne baseline-modellen er:",
        *topp_liste,
        "",
        "## Avgrensning",
        "",
        "- WBS 4.2 dokumenterer kun implementering og trening av Random Forest på treningsdata.",
        "- Feature importance-verdiene er foreløpige modellinterne signaler og erstatter ikke senere evaluering og tolkning i WBS 5.4 og 6.1.",
        "- Aktiviteten produserer ikke testprediksjoner, `RMSE`, `MAPE`, prognoser eller modellsammenligning.",
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

    modell = RandomForestRegressor(**BASELINE_PARAMETRE)
    start_tid = time.perf_counter()
    modell.fit(x_train, y_train[TARGET_KOLONNE])
    fit_seconds = time.perf_counter() - start_tid

    modelloversikt_df = lag_modelloversikt(x_train, fit_seconds, modell)
    importance_df = lag_importance_tabell(modell, x_train.columns.tolist())

    modell_path = aktivitetsmappe / "model_random_forest_regressor.joblib"
    dump(modell, modell_path)

    oversikt_path = aktivitetsmappe / "tab_rf_modelloversikt.csv"
    oversikt_path.write_text(modelloversikt_df.to_csv(index=False), encoding="utf-8")

    importance_path = aktivitetsmappe / "tab_rf_feature_importance.csv"
    importance_path.write_text(importance_df.to_csv(index=False), encoding="utf-8")

    md_path = aktivitetsmappe / "random_forest_regressor.md"
    skriv_markdown(md_path, modelloversikt_df, importance_df)

    print("WBS 4.2 ferdig: Random Forest Regressor implementert")
    print(f"- Treningsrader: {len(x_train)}")
    print(f"- Features: {x_train.shape[1]}")
    print(f"- Fit-sekunder: {fit_seconds:.6f}")
    print(f"- {modell_path.name}")
    print(f"- {oversikt_path.name}")
    print(f"- {importance_path.name}")
    print(f"- {md_path.name}")


if __name__ == "__main__":
    main()
