from pathlib import Path

import pandas as pd
from pandas.api.types import CategoricalDtype


TARGET_KOLONNE = "Sales"
DATO_KOLONNE = "Order Date"
TRAIN_YEARS = [2022, 2023, 2024]
TEST_YEARS = [2025]
KATEGORISKE_KOLONNER = ["Category", "Sub Category", "City", "Region"]
PÅKREVDE_KOLONNER = [
    DATO_KOLONNE,
    TARGET_KOLONNE,
    "Discount",
    "year",
    "month",
    "quarter",
    "weekofyear",
    "dayofweek",
    "dayofmonth",
    "is_weekend",
    *KATEGORISKE_KOLONNER,
]


def les_dataset(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path, encoding="utf-8-sig")
    if df.shape[1] == 1:
        df = pd.read_csv(csv_path, sep=";", encoding="utf-8-sig")
    return df


def valider_input(df: pd.DataFrame) -> None:
    mangler = [kol for kol in PÅKREVDE_KOLONNER if kol not in df.columns]
    if mangler:
        raise ValueError(f"WBS 3.3 mangler påkrevde kolonner fra WBS 3.2: {mangler}")

    år = sorted(pd.to_numeric(df["year"], errors="coerce").dropna().astype(int).unique().tolist())
    if år != [2022, 2023, 2024, 2025]:
        raise ValueError("WBS 3.3 forventer feature-datasett med år 2022-2025.")


def forbered_encoded_features(df_train: pd.DataFrame, df_test: pd.DataFrame, df_full: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    x_train = df_train.drop(columns=[TARGET_KOLONNE, DATO_KOLONNE]).copy()
    x_test = df_test.drop(columns=[TARGET_KOLONNE, DATO_KOLONNE]).copy()

    for kol in KATEGORISKE_KOLONNER:
        kategorier = sorted(df_full[kol].dropna().astype(str).unique().tolist())
        dtype = CategoricalDtype(categories=kategorier)
        x_train[kol] = x_train[kol].astype(str).astype(dtype)
        x_test[kol] = x_test[kol].astype(str).astype(dtype)

    x_train = pd.get_dummies(x_train, columns=KATEGORISKE_KOLONNER, dtype=int)
    x_test = pd.get_dummies(x_test, columns=KATEGORISKE_KOLONNER, dtype=int)

    alle_kolonner = sorted(set(x_train.columns).union(x_test.columns))
    x_train = x_train.reindex(columns=alle_kolonner, fill_value=0)
    x_test = x_test.reindex(columns=alle_kolonner, fill_value=0)
    return x_train, x_test


def lag_split_oversikt(df: pd.DataFrame, df_train: pd.DataFrame, df_test: pd.DataFrame, antall_features: int) -> pd.DataFrame:
    rader = [
        ("hele_dataset", "alle", len(df), antall_features),
        ("train", "alle", len(df_train), antall_features),
        ("test", "alle", len(df_test), antall_features),
    ]

    for år in sorted(df["year"].unique().tolist()):
        delsett = "train" if år in TRAIN_YEARS else "test"
        rader.append((delsett, str(år), int((df["year"] == år).sum()), antall_features))

    return pd.DataFrame(rader, columns=["delsett", "år", "antall_rader", "antall_features"])


def skriv_markdown(md_path: Path, df_train: pd.DataFrame, df_test: pd.DataFrame, antall_features: int) -> None:
    lines = [
        "# Datasplitt (WBS 3.3)",
        "",
        "## Kort oppsummering",
        "",
        f"- Treningsår: {', '.join(str(år) for år in TRAIN_YEARS)}",
        f"- Testår: {', '.join(str(år) for år in TEST_YEARS)}",
        f"- Antall treningsrader: {len(df_train)}",
        f"- Antall testrader: {len(df_test)}",
        f"- Antall encoded feature-kolonner: {antall_features}",
        "",
        "## Viktige valg",
        "",
        "- Datasplitt bygger direkte på `dataset_feature_engineered.csv` fra WBS 3.2.",
        "- `Order Date` brukes til sporbarhet i input, men fjernes fra modellmatrisene.",
        "- Kategoriske features one-hot-encodes i dette steget slik at modelleringen kan bruke filene direkte.",
        "",
    ]
    md_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    aktivitetsmappe = Path(__file__).resolve().parent
    repo_root = Path(__file__).resolve().parents[3]
    input_path = repo_root / "006 analysis" / "aktiviteter" / "05_feature_engineering" / "dataset_feature_engineered.csv"

    if not input_path.exists():
        raise FileNotFoundError(
            f"Fant ikke feature-datasett: {input_path}. Kjør WBS 3.2 før WBS 3.3."
        )

    df = les_dataset(input_path)
    valider_input(df)

    df["year"] = pd.to_numeric(df["year"], errors="raise").astype(int)
    df_train = df.loc[df["year"].isin(TRAIN_YEARS)].copy()
    df_test = df.loc[df["year"].isin(TEST_YEARS)].copy()

    if df_train.empty or df_test.empty:
        raise ValueError("Datasplitt ga tomt train- eller testsett. Kontroller årsmapping og feature-datasett.")

    x_train, x_test = forbered_encoded_features(df_train, df_test, df)
    y_train = df_train[[TARGET_KOLONNE]].copy()
    y_test = df_test[[TARGET_KOLONNE]].copy()

    x_train_path = aktivitetsmappe / "X_train.csv"
    x_test_path = aktivitetsmappe / "X_test.csv"
    y_train_path = aktivitetsmappe / "y_train.csv"
    y_test_path = aktivitetsmappe / "y_test.csv"

    x_train_path.write_text(x_train.to_csv(index=False), encoding="utf-8")
    x_test_path.write_text(x_test.to_csv(index=False), encoding="utf-8")
    y_train_path.write_text(y_train.to_csv(index=False), encoding="utf-8")
    y_test_path.write_text(y_test.to_csv(index=False), encoding="utf-8")

    tab_path = aktivitetsmappe / "tab_split_oversikt.csv"
    oversikt_df = lag_split_oversikt(df, df_train, df_test, x_train.shape[1])
    tab_path.write_text(oversikt_df.to_csv(index=False), encoding="utf-8")

    md_path = aktivitetsmappe / "datasplitt.md"
    skriv_markdown(md_path, df_train, df_test, x_train.shape[1])

    print("WBS 3.3 ferdig: datasplitt dokumentert")
    print(f"- Treningsrader: {len(df_train)}")
    print(f"- Testrader: {len(df_test)}")
    print(f"- Encoded feature-kolonner: {x_train.shape[1]}")
    print(f"- {x_train_path.name}")
    print(f"- {x_test_path.name}")
    print(f"- {y_train_path.name}")
    print(f"- {y_test_path.name}")
    print(f"- {tab_path.name}")
    print(f"- {md_path.name}")


if __name__ == "__main__":
    main()
