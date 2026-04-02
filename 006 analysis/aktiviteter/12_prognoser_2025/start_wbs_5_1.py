from pathlib import Path

import pandas as pd
from joblib import load
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression


TARGET_KOLONNE = "Sales"
TEST_AAR = 2025
FORVENTET_TESTRADER = 3312
FORVENTET_FEATURES = 67
INPUT_FEATURES_TEST = "06_datasplitt/X_test.csv"
INPUT_TARGET_TEST = "06_datasplitt/y_test.csv"
INPUT_FEATURES_TRAIN = "06_datasplitt/X_train.csv"
INPUT_TARGET_TRAIN = "06_datasplitt/y_train.csv"
FEATURE_DATASET = "05_feature_engineering/dataset_feature_engineered.csv"
DETAIL_COLS = [
    "Order Date",
    TARGET_KOLONNE,
    "Discount",
    "Category",
    "Sub Category",
    "City",
    "Region",
    "year",
    "month",
    "quarter",
    "weekofyear",
    "dayofweek",
    "dayofmonth",
    "is_weekend",
]
MATCH_COLS = ["Discount", "year", "month", "quarter", "weekofyear", "dayofweek", "dayofmonth", "is_weekend"]
MODELLSPOR = [
    {
        "modellnavn": "LinearRegression",
        "modellrolle": "benchmark lineær",
        "modellfil": "08_lineaer_regresjon/model_lineaer_regresjon.joblib",
        "oversikt_fil": "08_lineaer_regresjon/tab_lr_modelloversikt.csv",
        "prediksjonskolonne": "prognose_lineaer_regresjon",
        "modelltype": "linear_regression",
    },
    {
        "modellnavn": "RandomForestRegressor",
        "modellrolle": "baseline RF",
        "modellfil": "09_random_forest_regressor/model_random_forest_regressor.joblib",
        "oversikt_fil": "09_random_forest_regressor/tab_rf_modelloversikt.csv",
        "prediksjonskolonne": "prognose_random_forest_baseline",
        "modelltype": "random_forest",
    },
    {
        "modellnavn": "RandomForestRegressor",
        "modellrolle": "tuned RF",
        "modellfil": "11_parameterjustering_random_forest/model_random_forest_tuned.joblib",
        "oversikt_fil": "11_parameterjustering_random_forest/tab_rf_tuned_modelloversikt.csv",
        "prediksjonskolonne": "prognose_random_forest_tuned",
        "modelltype": "random_forest",
    },
]


def les_dataset(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path, encoding="utf-8-sig")
    if df.shape[1] == 1:
        df = pd.read_csv(csv_path, sep=";", encoding="utf-8-sig")
    return df


def parse_bool(value: object) -> bool:
    if isinstance(value, bool):
        return value
    if pd.isna(value):
        return False
    return str(value).strip().lower() == "true"


def parse_optional_int(value: object) -> int | None:
    if value is None or pd.isna(value) or str(value).strip() == "":
        return None
    return int(value)


def parse_float_or_string(value: object) -> float | str:
    if isinstance(value, str):
        stripped = value.strip()
        if stripped == "":
            raise ValueError("Forventet verdi i modelloversikt, men fant tom streng.")
        try:
            return float(stripped)
        except ValueError:
            return stripped
    if pd.isna(value):
        raise ValueError("Forventet verdi i modelloversikt, men fant tom/NaN.")
    return float(value)


def valider_split_input(
    x_train: pd.DataFrame,
    y_train: pd.DataFrame,
    x_test: pd.DataFrame,
    y_test: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    if len(x_train) != len(y_train):
        raise ValueError("Radantall matcher ikke mellom X_train og y_train.")

    if len(x_test) != len(y_test):
        raise ValueError("Radantall matcher ikke mellom X_test og y_test.")

    if y_train.shape[1] != 1 or y_test.shape[1] != 1:
        raise ValueError("y_train.csv og y_test.csv skal ha nøyaktig én kolonne hver.")

    if y_train.columns[0] != TARGET_KOLONNE or y_test.columns[0] != TARGET_KOLONNE:
        raise ValueError(f"Forventet target-kolonne `{TARGET_KOLONNE}` i både y_train og y_test.")

    if x_test.shape[0] != FORVENTET_TESTRADER or y_test.shape[0] != FORVENTET_TESTRADER:
        raise ValueError(
            f"WBS 5.1 forventer {FORVENTET_TESTRADER} testrader i 2025, "
            f"men fant {x_test.shape[0]} i X_test og {y_test.shape[0]} i y_test."
        )

    if x_test.shape[1] != FORVENTET_FEATURES:
        raise ValueError(
            f"WBS 5.1 forventer {FORVENTET_FEATURES} feature-kolonner i X_test, men fant {x_test.shape[1]}."
        )

    if x_train.shape[1] != FORVENTET_FEATURES:
        raise ValueError(
            f"WBS 5.1 forventer {FORVENTET_FEATURES} feature-kolonner i X_train, men fant {x_train.shape[1]}."
        )

    if x_train.columns.tolist() != x_test.columns.tolist():
        raise ValueError("X_train og X_test må ha identiske feature-kolonner i samme rekkefølge.")

    for df in [x_train, x_test]:
        ikke_numeriske = [kol for kol in df.columns if not pd.api.types.is_numeric_dtype(df[kol])]
        if ikke_numeriske:
            raise ValueError(f"Alle feature-kolonner må være numeriske. Fant: {ikke_numeriske}")

    if not pd.api.types.is_numeric_dtype(y_train[TARGET_KOLONNE]) or not pd.api.types.is_numeric_dtype(
        y_test[TARGET_KOLONNE]
    ):
        raise ValueError(f"Target-kolonnen `{TARGET_KOLONNE}` må være numerisk.")

    x_train = x_train.apply(pd.to_numeric, errors="raise")
    x_test = x_test.apply(pd.to_numeric, errors="raise")
    y_train = y_train.copy()
    y_test = y_test.copy()
    y_train[TARGET_KOLONNE] = pd.to_numeric(y_train[TARGET_KOLONNE], errors="raise")
    y_test[TARGET_KOLONNE] = pd.to_numeric(y_test[TARGET_KOLONNE], errors="raise")
    return x_train, y_train, x_test, y_test


def bygg_test_context(feature_df: pd.DataFrame) -> pd.DataFrame:
    mangler = [kol for kol in DETAIL_COLS if kol not in feature_df.columns]
    if mangler:
        raise ValueError(f"Feature-datasettet mangler kolonner som kreves for WBS 5.1: {mangler}")

    context_df = feature_df.loc[feature_df["year"] == TEST_AAR, DETAIL_COLS].copy().reset_index(drop=True)
    if len(context_df) != FORVENTET_TESTRADER:
        raise ValueError(
            f"WBS 5.1 forventer {FORVENTET_TESTRADER} rader for {TEST_AAR} i feature-datasettet, men fant {len(context_df)}."
        )

    return context_df


def valider_context_match(context_df: pd.DataFrame, x_test: pd.DataFrame, y_test: pd.DataFrame) -> None:
    for kol in MATCH_COLS:
        venstre = pd.to_numeric(context_df[kol], errors="raise").reset_index(drop=True)
        hoyre = pd.to_numeric(x_test[kol], errors="raise").reset_index(drop=True)
        if not venstre.equals(hoyre):
            raise ValueError(f"Rekkefølgen mellom 2025-kontekst og X_test matcher ikke for kolonnen `{kol}`.")

    sales_context = pd.to_numeric(context_df[TARGET_KOLONNE], errors="raise").reset_index(drop=True)
    sales_test = pd.to_numeric(y_test[TARGET_KOLONNE], errors="raise").reset_index(drop=True)
    if not sales_context.equals(sales_test):
        raise ValueError("Rekkefølgen mellom 2025-kontekst og y_test matcher ikke for faktisk Sales.")


def les_oversiktsrad(repo_aktiviteter: Path, rel_path: str) -> pd.Series:
    oversikt_path = repo_aktiviteter / rel_path
    if not oversikt_path.exists():
        raise FileNotFoundError(f"Fant ikke modelloversikt: {oversikt_path}")

    oversikt_df = les_dataset(oversikt_path)
    if oversikt_df.empty or len(oversikt_df) != 1:
        raise ValueError(f"Modelloversikten `{rel_path}` må ha nøyaktig én rad.")

    return oversikt_df.iloc[0]


def bygg_lineaer_regresjon_fra_oversikt(oversikt: pd.Series, x_train: pd.DataFrame, y_train: pd.DataFrame) -> LinearRegression:
    modell = LinearRegression(fit_intercept=parse_bool(oversikt["fit_intercept"]))
    modell.fit(x_train, y_train[TARGET_KOLONNE])
    return modell


def bygg_random_forest_fra_oversikt(
    oversikt: pd.Series,
    x_train: pd.DataFrame,
    y_train: pd.DataFrame,
) -> RandomForestRegressor:
    parametre = {
        "n_estimators": int(oversikt["n_estimators"]),
        "random_state": int(oversikt["random_state"]),
        "n_jobs": int(oversikt["n_jobs"]),
        "bootstrap": parse_bool(oversikt["bootstrap"]),
        "max_depth": parse_optional_int(oversikt["max_depth"]),
        "min_samples_leaf": int(oversikt["min_samples_leaf"]),
        "max_features": parse_float_or_string(oversikt["max_features"]),
    }
    modell = RandomForestRegressor(**parametre)
    modell.fit(x_train, y_train[TARGET_KOLONNE])
    return modell


def hent_eller_bygg_modell(
    modellspor: dict[str, str],
    repo_aktiviteter: Path,
    x_train: pd.DataFrame,
    y_train: pd.DataFrame,
    model_path_override: Path | None = None,
) -> tuple[object, bool, bool]:
    modell_path = model_path_override or (repo_aktiviteter / modellspor["modellfil"])
    lokal_fil_funnet = modell_path.exists()

    if lokal_fil_funnet:
        return load(modell_path), True, False

    oversikt = les_oversiktsrad(repo_aktiviteter, modellspor["oversikt_fil"])
    if modellspor["modelltype"] == "linear_regression":
        modell = bygg_lineaer_regresjon_fra_oversikt(oversikt, x_train, y_train)
    else:
        modell = bygg_random_forest_fra_oversikt(oversikt, x_train, y_train)

    return modell, False, True


def lag_detaljtabell(
    context_df: pd.DataFrame,
    y_test: pd.DataFrame,
    prediksjoner: dict[str, pd.Series],
) -> pd.DataFrame:
    detalj_df = context_df.copy().reset_index(drop=True)
    detalj_df.insert(0, "rad_id_2025", detalj_df.index + 1)
    detalj_df = detalj_df.rename(columns={TARGET_KOLONNE: "Sales_faktisk"})
    detalj_df["Sales_faktisk"] = y_test[TARGET_KOLONNE].reset_index(drop=True)

    for kolonne, verdier in prediksjoner.items():
        detalj_df[kolonne] = pd.Series(verdier).round(6)

    return detalj_df[
        [
            "rad_id_2025",
            "Order Date",
            "Sales_faktisk",
            "Discount",
            "Category",
            "Sub Category",
            "City",
            "Region",
            "year",
            "month",
            "quarter",
            "weekofyear",
            "dayofweek",
            "dayofmonth",
            "is_weekend",
            "prognose_lineaer_regresjon",
            "prognose_random_forest_baseline",
            "prognose_random_forest_tuned",
        ]
    ]


def lag_maanedstabell(detalj_df: pd.DataFrame) -> pd.DataFrame:
    maaned_df = detalj_df.copy()
    maaned_df["aar_maaned"] = pd.to_datetime(maaned_df["Order Date"], format="%Y-%m-%d").dt.strftime("%Y-%m")
    oppsummert = (
        maaned_df.groupby(["aar_maaned", "month"], as_index=False)
        .agg(
            antall_rader=("rad_id_2025", "count"),
            sales_faktisk_sum=("Sales_faktisk", "sum"),
            prognose_lineaer_regresjon_sum=("prognose_lineaer_regresjon", "sum"),
            prognose_random_forest_baseline_sum=("prognose_random_forest_baseline", "sum"),
            prognose_random_forest_tuned_sum=("prognose_random_forest_tuned", "sum"),
        )
        .sort_values(["aar_maaned", "month"])
        .reset_index(drop=True)
    )
    oppsummert["sales_faktisk_sum"] = oppsummert["sales_faktisk_sum"].round(6)
    oppsummert["prognose_lineaer_regresjon_sum"] = oppsummert["prognose_lineaer_regresjon_sum"].round(6)
    oppsummert["prognose_random_forest_baseline_sum"] = oppsummert["prognose_random_forest_baseline_sum"].round(6)
    oppsummert["prognose_random_forest_tuned_sum"] = oppsummert["prognose_random_forest_tuned_sum"].round(6)
    return oppsummert.rename(columns={"aar_maaned": "år_måned"})


def lag_modelloversiktstabell(modellrader: list[dict[str, object]]) -> pd.DataFrame:
    return pd.DataFrame(modellrader)[
        [
            "modellnavn",
            "modellrolle",
            "modellfil",
            "modellfil_funnet_lokalt",
            "autogenerert_i_5_1",
            "prediksjonskolonne",
        ]
    ]


def skriv_markdown(md_path: Path, detalj_df: pd.DataFrame, maaned_df: pd.DataFrame, modell_df: pd.DataFrame) -> None:
    modelllinjer = [
        f"- `{rad.modellrolle}`: `{rad.modellnavn}` via `{rad.prediksjonskolonne}` "
        f"(lokal modellfil funnet: {'ja' if rad.modellfil_funnet_lokalt else 'nei'}, "
        f"autogenerert i 5.1: {'ja' if rad.autogenerert_i_5_1 else 'nei'})"
        for rad in modell_df.itertuples(index=False)
    ]
    første_maaned = maaned_df.iloc[0]
    siste_maaned = maaned_df.iloc[-1]

    lines = [
        "# Prognoser for 2025 (WBS 5.1)",
        "",
        "## Hva WBS 5.1 gjør",
        "",
        "- Aktiviteten genererer 2025-prognoser for lineær regresjon, Random Forest-baseline og tuned Random Forest.",
        "- Tuned Random Forest er standardmodellen videre i Random Forest-sporet, men benchmark- og baseline-sporene beholdes for senere evaluering.",
        "- Faktisk `Sales` for 2025 er med i outputen for sporbarhet, men uten feilkolonner eller evalueringsmetrikker.",
        "",
        "## Datagrunnlag",
        "",
        f"- Antall 2025-observasjoner: {len(detalj_df)}",
        f"- Antall måneder i oppsummeringen: {len(maaned_df)}",
        f"- Testfeature-matrise: `{INPUT_FEATURES_TEST}`",
        f"- Testtarget: `{INPUT_TARGET_TEST}`",
        "",
        "## Modellspor brukt i prognosene",
        "",
        *modelllinjer,
        "",
        "## Månedlig dekning",
        "",
        f"- Første måned i oppsummeringen: `{første_maaned['år_måned']}`",
        f"- Siste måned i oppsummeringen: `{siste_maaned['år_måned']}`",
        "",
        "## Produserte artefakter",
        "",
        "- `tab_prognoser_2025_detalj.csv`",
        "- `tab_prognoser_2025_maaned.csv`",
        "- `tab_prognosemodeller_oversikt.csv`",
        "- `prognoser_2025.md`",
        "",
        "## Avgrensning mot senere WBS-steg",
        "",
        "- WBS 5.1 beregner ikke residualer, `RMSE`, `MAPE` eller modellrangering.",
        "- Selve evalueringen og sammenligningen av modellene er utsatt til WBS 5.2 og WBS 5.3.",
        "",
    ]
    md_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    aktivitetsmappe = Path(__file__).resolve().parent
    repo_aktiviteter = Path(__file__).resolve().parents[1]

    x_test = les_dataset(repo_aktiviteter / INPUT_FEATURES_TEST)
    y_test = les_dataset(repo_aktiviteter / INPUT_TARGET_TEST)
    x_train = les_dataset(repo_aktiviteter / INPUT_FEATURES_TRAIN)
    y_train = les_dataset(repo_aktiviteter / INPUT_TARGET_TRAIN)
    feature_df = les_dataset(repo_aktiviteter / FEATURE_DATASET)

    x_train, y_train, x_test, y_test = valider_split_input(x_train, y_train, x_test, y_test)
    context_df = bygg_test_context(feature_df)
    valider_context_match(context_df, x_test, y_test)

    prediksjoner: dict[str, pd.Series] = {}
    modellrader: list[dict[str, object]] = []

    for modellspor in MODELLSPOR:
        modell, lokal_fil_funnet, autogenerert = hent_eller_bygg_modell(
            modellspor,
            repo_aktiviteter,
            x_train,
            y_train,
        )
        prediksjoner[modellspor["prediksjonskolonne"]] = pd.Series(modell.predict(x_test))
        modellrader.append(
            {
                "modellnavn": modellspor["modellnavn"],
                "modellrolle": modellspor["modellrolle"],
                "modellfil": modellspor["modellfil"],
                "modellfil_funnet_lokalt": lokal_fil_funnet,
                "autogenerert_i_5_1": autogenerert,
                "prediksjonskolonne": modellspor["prediksjonskolonne"],
            }
        )

    detalj_df = lag_detaljtabell(context_df, y_test, prediksjoner)
    maaned_df = lag_maanedstabell(detalj_df)
    modell_df = lag_modelloversiktstabell(modellrader)

    detalj_path = aktivitetsmappe / "tab_prognoser_2025_detalj.csv"
    detalj_path.write_text(detalj_df.to_csv(index=False), encoding="utf-8")

    maaned_path = aktivitetsmappe / "tab_prognoser_2025_maaned.csv"
    maaned_path.write_text(maaned_df.to_csv(index=False), encoding="utf-8")

    modell_path = aktivitetsmappe / "tab_prognosemodeller_oversikt.csv"
    modell_path.write_text(modell_df.to_csv(index=False), encoding="utf-8")

    md_path = aktivitetsmappe / "prognoser_2025.md"
    skriv_markdown(md_path, detalj_df, maaned_df, modell_df)

    print("WBS 5.1 ferdig: prognoser for 2025 generert")
    print(f"- Observasjoner: {len(detalj_df)}")
    print(f"- Månedsrader: {len(maaned_df)}")
    print(f"- Modellspor: {len(modell_df)}")
    print(f"- {detalj_path.name}")
    print(f"- {maaned_path.name}")
    print(f"- {modell_path.name}")
    print(f"- {md_path.name}")


if __name__ == "__main__":
    main()
