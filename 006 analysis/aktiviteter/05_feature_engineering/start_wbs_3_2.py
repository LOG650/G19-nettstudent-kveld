from pathlib import Path

import pandas as pd


DATO_KOLONNE = "Order Date"
TARGET_KOLONNE = "Sales"
KATEGORISKE_KOLONNER = ["Category", "Sub Category", "City", "Region"]
NUMERISKE_KOLONNER = ["Discount"]
EKSKLUDERTE_KOLONNER = {
    "Order ID": "ID-kolonne uten generaliserbar prediksjonsverdi.",
    "Customer Name": "Navn-kolonne med høy risiko for overtilpasning.",
    "Profit": "Ekskludert som potensiell lekkasjevariabel.",
    "State": "Kolonnen er konstant i datasettet og gir ingen forklaringskraft.",
}


def les_dataset(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path, encoding="utf-8-sig")
    if df.shape[1] == 1:
        df = pd.read_csv(csv_path, sep=";", encoding="utf-8-sig")
    return df


def valider_dataset(df: pd.DataFrame) -> None:
    påkrevde = [DATO_KOLONNE, TARGET_KOLONNE, *KATEGORISKE_KOLONNER, *NUMERISKE_KOLONNER, *EKSKLUDERTE_KOLONNER.keys()]
    mangler = [kol for kol in påkrevde if kol not in df.columns]
    if mangler:
        raise ValueError(f"Dataset mangler påkrevde kolonner for WBS 3.2: {mangler}")

    dato = pd.to_datetime(df[DATO_KOLONNE], errors="coerce")
    if dato.isna().any():
        raise ValueError("Order Date inneholder ugyldige datoer. Kjør WBS 3.1 på nytt før WBS 3.2.")

    år = sorted(dato.dt.year.unique().tolist())
    if år != [2022, 2023, 2024, 2025]:
        raise ValueError(
            "WBS 3.2 forventer remappet datasett med år 2022-2025. Kjør WBS 3.1 før WBS 3.2."
        )


def lag_feature_dataset(df: pd.DataFrame) -> pd.DataFrame:
    dato = pd.to_datetime(df[DATO_KOLONNE], errors="raise")

    feature_df = pd.DataFrame(
        {
            DATO_KOLONNE: dato.dt.strftime("%Y-%m-%d"),
            TARGET_KOLONNE: pd.to_numeric(df[TARGET_KOLONNE], errors="raise"),
            "Discount": pd.to_numeric(df["Discount"], errors="raise"),
            "Category": df["Category"].astype("string"),
            "Sub Category": df["Sub Category"].astype("string"),
            "City": df["City"].astype("string"),
            "Region": df["Region"].astype("string"),
            "year": dato.dt.year.astype("int64"),
            "month": dato.dt.month.astype("int64"),
            "quarter": dato.dt.quarter.astype("int64"),
            "weekofyear": dato.dt.isocalendar().week.astype("int64"),
            "dayofweek": dato.dt.dayofweek.astype("int64"),
            "dayofmonth": dato.dt.day.astype("int64"),
            "is_weekend": dato.dt.dayofweek.isin([5, 6]).astype("int64"),
        }
    )

    return feature_df.sort_values([DATO_KOLONNE, TARGET_KOLONNE]).reset_index(drop=True)


def lag_featurevalg() -> pd.DataFrame:
    rader = [
        (TARGET_KOLONNE, "behold", TARGET_KOLONNE, "Målvariabel for prognose."),
        ("Discount", "behold", "Discount", "Numerisk forklaringsvariabel."),
        ("Category", "behold", "Category", "Kategorisk feature med håndterbar kardinalitet."),
        ("Sub Category", "behold", "Sub Category", "Kategorisk feature med håndterbar kardinalitet."),
        ("City", "behold", "City", "Kategorisk feature med håndterbar kardinalitet."),
        ("Region", "behold", "Region", "Kategorisk feature med håndterbar kardinalitet."),
        (DATO_KOLONNE, "behold", DATO_KOLONNE, "Beholdes for sporbarhet og tidsbasert splitt."),
        (DATO_KOLONNE, "transformer", "year", "Utledet kalenderår etter remapping."),
        (DATO_KOLONNE, "transformer", "month", "Utledet måned."),
        (DATO_KOLONNE, "transformer", "quarter", "Utledet kvartal."),
        (DATO_KOLONNE, "transformer", "weekofyear", "Utledet uke i året."),
        (DATO_KOLONNE, "transformer", "dayofweek", "Utledet ukedag."),
        (DATO_KOLONNE, "transformer", "dayofmonth", "Utledet dag i måneden."),
        (DATO_KOLONNE, "transformer", "is_weekend", "Indikator for helg."),
    ]

    for kolonne, begrunnelse in EKSKLUDERTE_KOLONNER.items():
        rader.append((kolonne, "ekskluder", "", begrunnelse))

    return pd.DataFrame(rader, columns=["input_kolonne", "handling", "output_kolonne", "begrunnelse"])


def skriv_markdown(md_path: Path, feature_df: pd.DataFrame) -> None:
    periode_start = feature_df[DATO_KOLONNE].min()
    periode_slutt = feature_df[DATO_KOLONNE].max()
    lines = [
        "# Feature engineering (WBS 3.2)",
        "",
        "## Kort oppsummering",
        "",
        f"- Antall observasjoner: {len(feature_df)}",
        f"- Periode i arbeidsgrunnlaget: {periode_start} til {periode_slutt}",
        f"- Target: `{TARGET_KOLONNE}`",
        f"- Direkte features: `{', '.join(NUMERISKE_KOLONNER + KATEGORISKE_KOLONNER)}`",
        "- Utledede tidsfeatures: `year`, `month`, `quarter`, `weekofyear`, `dayofweek`, `dayofmonth`, `is_weekend`",
        "",
        "## Viktige valg",
        "",
        "- `Profit` er ekskludert som potensiell lekkasjevariabel.",
        "- `State` er ekskludert fordi kolonnen er konstant.",
        "- `Order ID` og `Customer Name` er ekskludert for å unngå overtilpasning.",
        "- `Order Date` beholdes i feature-datasettet for sporbarhet og brukes videre i WBS 3.3 datasplitt.",
        "",
        "## Videre bruk",
        "",
        "- `dataset_feature_engineered.csv` er eneste operative input til WBS 3.3.",
        "",
    ]
    md_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    aktivitetsmappe = Path(__file__).resolve().parent
    repo_root = Path(__file__).resolve().parents[3]
    input_path = repo_root / "006 analysis" / "aktiviteter" / "04_dataprosessering" / "dataset_renset.csv"

    if not input_path.exists():
        raise FileNotFoundError(f"Fant ikke renset datasett: {input_path}. Kjør WBS 3.1 først.")

    df = les_dataset(input_path)
    valider_dataset(df)
    feature_df = lag_feature_dataset(df)
    featurevalg_df = lag_featurevalg()

    dataset_path = aktivitetsmappe / "dataset_feature_engineered.csv"
    dataset_path.write_text(feature_df.to_csv(index=False), encoding="utf-8")

    tab_path = aktivitetsmappe / "tab_featurevalg.csv"
    tab_path.write_text(featurevalg_df.to_csv(index=False), encoding="utf-8")

    md_path = aktivitetsmappe / "feature_engineering.md"
    skriv_markdown(md_path, feature_df)

    print("WBS 3.2 ferdig: feature engineering dokumentert")
    print(f"- Rader: {len(feature_df)}")
    print(f"- Periode: {feature_df[DATO_KOLONNE].min()} til {feature_df[DATO_KOLONNE].max()}")
    print(f"- {dataset_path.name}")
    print(f"- {tab_path.name}")
    print(f"- {md_path.name}")


if __name__ == "__main__":
    main()
