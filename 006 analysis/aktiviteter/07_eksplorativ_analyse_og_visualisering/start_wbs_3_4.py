from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


DATO_KOLONNE = "Order Date"
TARGET_KOLONNE = "Sales"
PERIODE_KOLONNE = "periode"
TRAIN_YEARS = [2022, 2023, 2024]
TEST_YEARS = [2025]
KATEGORISKE_KOLONNER = ["Category", "Sub Category", "City", "Region"]
PÅKREVDE_KOLONNER = [DATO_KOLONNE, TARGET_KOLONNE, "year", "month", *KATEGORISKE_KOLONNER]
MÅNEDSNAVN = {
    1: "jan",
    2: "feb",
    3: "mar",
    4: "apr",
    5: "mai",
    6: "jun",
    7: "jul",
    8: "aug",
    9: "sep",
    10: "okt",
    11: "nov",
    12: "des",
}


def les_dataset(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path, encoding="utf-8-sig")
    if df.shape[1] == 1:
        df = pd.read_csv(csv_path, sep=";", encoding="utf-8-sig")
    return df


def valider_feature_dataset(df: pd.DataFrame) -> pd.DataFrame:
    mangler = [kol for kol in PÅKREVDE_KOLONNER if kol not in df.columns]
    if mangler:
        raise ValueError(f"WBS 3.4 mangler påkrevde kolonner fra feature-datasettet: {mangler}")

    dato = pd.to_datetime(df[DATO_KOLONNE], errors="coerce")
    if dato.isna().any():
        raise ValueError("Order Date inneholder ugyldige datoer. Kjør WBS 3.2 på nytt før WBS 3.4.")

    år = sorted(pd.to_numeric(df["year"], errors="coerce").dropna().astype(int).unique().tolist())
    if år != [2022, 2023, 2024, 2025]:
        raise ValueError("WBS 3.4 forventer feature-datasett med år 2022-2025.")

    df = df.copy()
    df[DATO_KOLONNE] = dato
    df["year"] = pd.to_numeric(df["year"], errors="raise").astype(int)
    df["month"] = pd.to_numeric(df["month"], errors="raise").astype(int)
    df[TARGET_KOLONNE] = pd.to_numeric(df[TARGET_KOLONNE], errors="raise")
    df[PERIODE_KOLONNE] = df["year"].apply(lambda årstall: "trening" if årstall in TRAIN_YEARS else "test")
    df["måned_start"] = df[DATO_KOLONNE].dt.to_period("M").dt.to_timestamp()
    df["måned_navn"] = df["month"].map(MÅNEDSNAVN)
    return df


def valider_split_oversikt(df: pd.DataFrame, split_path: Path) -> None:
    if not split_path.exists():
        return

    split_df = les_dataset(split_path)
    train_rader = int(split_df.loc[(split_df["delsett"] == "train") & (split_df["år"] == "alle"), "antall_rader"].iloc[0])
    test_rader = int(split_df.loc[(split_df["delsett"] == "test") & (split_df["år"] == "alle"), "antall_rader"].iloc[0])

    if train_rader != int((df[PERIODE_KOLONNE] == "trening").sum()) or test_rader != int((df[PERIODE_KOLONNE] == "test").sum()):
        raise ValueError("Split-oversikten stemmer ikke med feature-datasettet. Kjør WBS 3.3 på nytt før WBS 3.4.")


def lag_eda_oversikt(df: pd.DataFrame) -> pd.DataFrame:
    rader: list[dict[str, object]] = []

    grupper = [("hele_dataset", "alle", df)]
    for periode, gruppe_df in df.groupby(PERIODE_KOLONNE):
        grupper.append(("periode", periode, gruppe_df))
    for årstall, gruppe_df in df.groupby("year"):
        grupper.append(("år", str(årstall), gruppe_df))

    for nivå, gruppe, gruppe_df in grupper:
        rader.append(
            {
                "nivå": nivå,
                "gruppe": gruppe,
                "antall_rader": int(len(gruppe_df)),
                "sales_mean": round(float(gruppe_df[TARGET_KOLONNE].mean()), 2),
                "sales_median": round(float(gruppe_df[TARGET_KOLONNE].median()), 2),
                "sales_std": round(float(gruppe_df[TARGET_KOLONNE].std(ddof=1)), 2),
                "sales_min": round(float(gruppe_df[TARGET_KOLONNE].min()), 2),
                "sales_max": round(float(gruppe_df[TARGET_KOLONNE].max()), 2),
            }
        )

    return pd.DataFrame(rader)


def lag_kategorisk_fordeling(df: pd.DataFrame) -> pd.DataFrame:
    rader: list[dict[str, object]] = []
    perioder = [("alle", df)]
    perioder.extend((periode, gruppe_df) for periode, gruppe_df in df.groupby(PERIODE_KOLONNE))

    for variabel in KATEGORISKE_KOLONNER:
        for periode, gruppe_df in perioder:
            teller = gruppe_df[variabel].value_counts(dropna=False)
            total = max(len(gruppe_df), 1)
            for kategori, antall in teller.items():
                rader.append(
                    {
                        "variabel": variabel,
                        "periode": periode,
                        "kategori": str(kategori),
                        "antall": int(antall),
                        "andel_pct": round(float(antall / total * 100), 2),
                    }
                )

    fordeling_df = pd.DataFrame(rader)
    return fordeling_df.sort_values(["variabel", "periode", "antall", "kategori"], ascending=[True, True, False, True])


def lag_fig_sales_over_tid(df: pd.DataFrame, fig_path: Path) -> None:
    agg = (
        df.groupby(["måned_start", PERIODE_KOLONNE], as_index=False)[TARGET_KOLONNE]
        .sum()
        .sort_values("måned_start")
    )

    plt.figure(figsize=(11, 5))
    sns.lineplot(data=agg, x="måned_start", y=TARGET_KOLONNE, hue=PERIODE_KOLONNE, marker="o")
    plt.axvline(pd.Timestamp("2025-01-01"), color="gray", linestyle="--", linewidth=1)
    plt.title("Månedlig totalsalg for trening og test")
    plt.xlabel("Måned")
    plt.ylabel("Totalt salg")
    plt.tight_layout()
    plt.savefig(fig_path, dpi=150)
    plt.close()


def lag_fig_sales_fordeling(df: pd.DataFrame, fig_path: Path) -> None:
    fig, akser = plt.subplots(1, 2, figsize=(11, 4.5))

    sns.histplot(data=df, x=TARGET_KOLONNE, hue=PERIODE_KOLONNE, bins=25, kde=True, stat="density", common_norm=False, ax=akser[0])
    akser[0].set_title("Fordeling av salg")
    akser[0].set_xlabel("Sales")
    akser[0].set_ylabel("Tetthet")

    sns.boxplot(data=df, x=PERIODE_KOLONNE, y=TARGET_KOLONNE, ax=akser[1])
    akser[1].set_title("Boksplott for salg")
    akser[1].set_xlabel("Periode")
    akser[1].set_ylabel("Sales")

    plt.tight_layout()
    plt.savefig(fig_path, dpi=150)
    plt.close()


def lag_fig_sales_per_month(df: pd.DataFrame, fig_path: Path) -> None:
    agg = (
        df.groupby([PERIODE_KOLONNE, "month", "måned_navn"], as_index=False)[TARGET_KOLONNE]
        .mean()
        .sort_values("month")
    )

    plt.figure(figsize=(10, 5))
    sns.lineplot(data=agg, x="month", y=TARGET_KOLONNE, hue=PERIODE_KOLONNE, marker="o")
    plt.xticks(range(1, 13), [MÅNEDSNAVN[m] for m in range(1, 13)])
    plt.title("Gjennomsnittlig salg per måned")
    plt.xlabel("Måned")
    plt.ylabel("Gjennomsnittlig salg")
    plt.tight_layout()
    plt.savefig(fig_path, dpi=150)
    plt.close()


def lag_fig_sales_per_category(df: pd.DataFrame, fig_path: Path) -> None:
    agg = (
        df.groupby(["Category", PERIODE_KOLONNE], as_index=False)[TARGET_KOLONNE]
        .mean()
    )
    kategori_rekkefølge = (
        df.groupby("Category")[TARGET_KOLONNE]
        .mean()
        .sort_values(ascending=False)
        .index
        .tolist()
    )

    plt.figure(figsize=(10, 5))
    sns.barplot(data=agg, x="Category", y=TARGET_KOLONNE, hue=PERIODE_KOLONNE, order=kategori_rekkefølge)
    plt.title("Gjennomsnittlig salg per kategori")
    plt.xlabel("Kategori")
    plt.ylabel("Gjennomsnittlig salg")
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()
    plt.savefig(fig_path, dpi=150)
    plt.close()


def skriv_markdown(md_path: Path, df: pd.DataFrame, oversikt_df: pd.DataFrame, fordeling_df: pd.DataFrame) -> None:
    train_mean = float(oversikt_df.loc[(oversikt_df["nivå"] == "periode") & (oversikt_df["gruppe"] == "trening"), "sales_mean"].iloc[0])
    test_mean = float(oversikt_df.loc[(oversikt_df["nivå"] == "periode") & (oversikt_df["gruppe"] == "test"), "sales_mean"].iloc[0])

    månedsmiddel = df.groupby("month")[TARGET_KOLONNE].mean().sort_values(ascending=False)
    topp_måned = int(månedsmiddel.index[0])
    bunn_måned = int(månedsmiddel.index[-1])

    kategori_middel = df.groupby("Category")[TARGET_KOLONNE].mean().sort_values(ascending=False)
    topp_kategori = str(kategori_middel.index[0])

    region_stats = df.groupby("Region")[TARGET_KOLONNE].agg(["count", "mean"]).sort_values("mean", ascending=False)
    regioner_med_volum = region_stats.loc[region_stats["count"] >= 30]
    topp_region = str(regioner_med_volum.index[0]) if not regioner_med_volum.empty else str(region_stats.index[0])

    north_antall = int(fordeling_df.loc[(fordeling_df["variabel"] == "Region") & (fordeling_df["periode"] == "alle") & (fordeling_df["kategori"] == "North"), "antall"].sum())

    lines = [
        "# Eksplorativ analyse og visualisering (WBS 3.4)",
        "",
        "## Datagrunnlag",
        "",
        "- Input: `05_feature_engineering/dataset_feature_engineered.csv`",
        "- Trening: 2022-2024",
        "- Test: 2025",
        f"- Antall observasjoner: {len(df)}",
        "",
        "## Hovedfunn",
        "",
        f"- Gjennomsnittlig salg er stabilt mellom trening og test, med `{train_mean:.2f}` i trening og `{test_mean:.2f}` i test.",
        f"- Det høyeste gjennomsnittlige månedsnivået ligger i `{MÅNEDSNAVN[topp_måned]}`, mens `{MÅNEDSNAVN[bunn_måned]}` ligger lavest.",
        f"- Kategorien `{topp_kategori}` har høyest gjennomsnittlig salgsnivå i datasettet.",
        f"- Regionen `{topp_region}` ligger høyest blant regionene med meningsfullt observasjonsvolum.",
        f"- `Region = North` er svært sparsom med bare `{north_antall}` observasjon og må tolkes varsomt i modellarbeidet.",
        "",
        "## Betydning for neste steg",
        "",
        "- Tidsmønsteret bør testes både i lineær regresjon og Random Forest gjennom de etablerte tidsfeature-kolonnene.",
        "- Kategori- og regionsignalene støtter at de kategoriske variablene bør beholdes i modellgrunnlaget.",
        "- Stabilt gjennomsnitt mellom trening og test tyder på at tidsbasert holdout er brukbar for videre modelltesting.",
        "",
    ]

    md_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    sns.set_theme(style="whitegrid")

    aktivitetsmappe = Path(__file__).resolve().parent
    repo_root = Path(__file__).resolve().parents[3]
    feature_path = repo_root / "006 analysis" / "aktiviteter" / "05_feature_engineering" / "dataset_feature_engineered.csv"
    split_path = repo_root / "006 analysis" / "aktiviteter" / "06_datasplitt" / "tab_split_oversikt.csv"

    if not feature_path.exists():
        raise FileNotFoundError(f"Fant ikke feature-datasett: {feature_path}. Kjør WBS 3.2 før WBS 3.4.")

    df = les_dataset(feature_path)
    df = valider_feature_dataset(df)
    valider_split_oversikt(df, split_path)

    oversikt_df = lag_eda_oversikt(df)
    fordeling_df = lag_kategorisk_fordeling(df)

    tab_oversikt_path = aktivitetsmappe / "tab_eda_oversikt.csv"
    tab_oversikt_path.write_text(oversikt_df.to_csv(index=False), encoding="utf-8")

    tab_fordeling_path = aktivitetsmappe / "tab_kategorisk_fordeling.csv"
    tab_fordeling_path.write_text(fordeling_df.to_csv(index=False), encoding="utf-8")

    fig_over_tid = aktivitetsmappe / "fig_sales_over_tid_train_test.png"
    lag_fig_sales_over_tid(df, fig_over_tid)

    fig_fordeling = aktivitetsmappe / "fig_sales_fordeling_train_test.png"
    lag_fig_sales_fordeling(df, fig_fordeling)

    fig_per_month = aktivitetsmappe / "fig_sales_per_month_split.png"
    lag_fig_sales_per_month(df, fig_per_month)

    fig_per_category = aktivitetsmappe / "fig_sales_per_category.png"
    lag_fig_sales_per_category(df, fig_per_category)

    md_path = aktivitetsmappe / "eda_visualisering.md"
    skriv_markdown(md_path, df, oversikt_df, fordeling_df)

    print("WBS 3.4 ferdig: eksplorativ analyse og visualisering dokumentert")
    print(f"- Rader analysert: {len(df)}")
    print(f"- {tab_oversikt_path.name}")
    print(f"- {tab_fordeling_path.name}")
    print(f"- {fig_over_tid.name}")
    print(f"- {fig_fordeling.name}")
    print(f"- {fig_per_month.name}")
    print(f"- {fig_per_category.name}")
    print(f"- {md_path.name}")


if __name__ == "__main__":
    main()
