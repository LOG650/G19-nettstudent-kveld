from pathlib import Path

import pandas as pd
from joblib import dump
from sklearn.linear_model import LinearRegression


TARGET_KOLONNE = "Sales"
MODELLNAVN = "LinearRegression"
INPUT_FEATURES = "06_datasplitt/X_train.csv"
INPUT_TARGET = "06_datasplitt/y_train.csv"


def les_dataset(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path, encoding="utf-8-sig")
    if df.shape[1] == 1:
        df = pd.read_csv(csv_path, sep=";", encoding="utf-8-sig")
    return df


def valider_input(x_train: pd.DataFrame, y_train: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    if x_train.empty:
        raise ValueError("X_train.csv er tom. Kjør WBS 3.3 på nytt før WBS 4.1.")

    if y_train.empty:
        raise ValueError("y_train.csv er tom. Kjør WBS 3.3 på nytt før WBS 4.1.")

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
            "Alle feature-kolonner må være numeriske i WBS 4.1. "
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
    y_train: pd.DataFrame,
    modell: LinearRegression,
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
                "fit_intercept": bool(modell.fit_intercept),
                "intercept": float(modell.intercept_),
            }
        ]
    )


def fortegn(verdi: float) -> str:
    if verdi > 0:
        return "positiv"
    if verdi < 0:
        return "negativ"
    return "null"


def lag_koeffisienttabell(modell: LinearRegression, kolonner: list[str]) -> pd.DataFrame:
    koeff_df = pd.DataFrame(
        {
            "feature": kolonner,
            "koeffisient": [float(verdi) for verdi in modell.coef_],
        }
    )
    koeff_df["abs_koeffisient"] = koeff_df["koeffisient"].abs()
    koeff_df["fortegn"] = koeff_df["koeffisient"].apply(fortegn)
    koeff_df = koeff_df.sort_values(
        ["abs_koeffisient", "feature"], ascending=[False, True]
    ).reset_index(drop=True)
    koeff_df["rang_abs"] = koeff_df.index + 1
    koeff_df["koeffisient"] = koeff_df["koeffisient"].round(6)
    koeff_df["abs_koeffisient"] = koeff_df["abs_koeffisient"].round(6)
    return koeff_df[["feature", "koeffisient", "abs_koeffisient", "fortegn", "rang_abs"]]


def skriv_markdown(
    md_path: Path,
    modelloversikt_df: pd.DataFrame,
    koeff_df: pd.DataFrame,
) -> None:
    topp = koeff_df.head(5)
    topp_liste = [
        f"- `{rad.feature}` ({rad.fortegn}, |koeff| = {rad.abs_koeffisient:.6f})"
        for rad in topp.itertuples(index=False)
    ]

    lines = [
        "# Lineær regresjon (WBS 4.1)",
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
        "- Benchmark-modellen er `LinearRegression` fra `scikit-learn`.",
        "- Modellen er kjørt med `fit_intercept=True` uten skalering eller regularisering.",
        "- Feature-settet er identisk med den one-hot-kodede modellmatrisen fra WBS 3.3.",
        "",
        "## Produserte artefakter",
        "",
        "- `model_lineaer_regresjon.joblib`",
        "- `tab_lr_modelloversikt.csv`",
        "- `tab_lr_koeffisienter.csv`",
        "- `lineaer_regresjon.md`",
        "",
        "## Første observasjoner",
        "",
        f"- Modellens intercept er `{float(modelloversikt_df.loc[0, 'intercept']):.6f}`.",
        "- De fem største koeffisientene målt i absoluttverdi er:",
        *topp_liste,
        "",
        "## Avgrensning",
        "",
        "- WBS 4.1 dokumenterer kun implementering og trening av lineær regresjon på treningsdata.",
        "- Evaluering på 2025-testsettet samt `RMSE`, `MAPE`, prognoser og modellsammenligning er utsatt til senere WBS-steg.",
        "- Koeffisientene må tolkes varsomt fordi dagens dummykoding kan gi multikollinearitet i lineær regresjon.",
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

    modell = LinearRegression(fit_intercept=True)
    modell.fit(x_train, y_train[TARGET_KOLONNE])

    modelloversikt_df = lag_modelloversikt(x_train, y_train, modell)
    koeff_df = lag_koeffisienttabell(modell, x_train.columns.tolist())

    modell_path = aktivitetsmappe / "model_lineaer_regresjon.joblib"
    dump(modell, modell_path)

    oversikt_path = aktivitetsmappe / "tab_lr_modelloversikt.csv"
    oversikt_path.write_text(modelloversikt_df.to_csv(index=False), encoding="utf-8")

    koeff_path = aktivitetsmappe / "tab_lr_koeffisienter.csv"
    koeff_path.write_text(koeff_df.to_csv(index=False), encoding="utf-8")

    md_path = aktivitetsmappe / "lineaer_regresjon.md"
    skriv_markdown(md_path, modelloversikt_df, koeff_df)

    print("WBS 4.1 ferdig: lineær regresjon implementert")
    print(f"- Treningsrader: {len(x_train)}")
    print(f"- Features: {x_train.shape[1]}")
    print(f"- Intercept: {float(modell.intercept_):.6f}")
    print(f"- {modell_path.name}")
    print(f"- {oversikt_path.name}")
    print(f"- {koeff_path.name}")
    print(f"- {md_path.name}")


if __name__ == "__main__":
    main()
