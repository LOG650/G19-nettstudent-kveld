from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


TARGET_KOLONNE = "Sales"
# Numeriske kolonner i fast, lesbar rekkefølge: target først, deretter rabatt og kalender.
# One-hot-kodede kategorier (by/region/kategori/underkategori) holdes utenfor fordi
# binære variabler gir lav og misvisende Pearson-korrelasjon.
NUMERISKE_KOLONNER = [
    "Sales",
    "Discount",
    "year",
    "quarter",
    "month",
    "weekofyear",
    "dayofweek",
    "dayofmonth",
    "is_weekend",
]


def les_dataset(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path, encoding="utf-8-sig")
    if df.shape[1] == 1:
        df = pd.read_csv(csv_path, sep=";", encoding="utf-8-sig")
    return df


def bygg_numerisk_treningssett(x_train_path: Path, y_train_path: Path) -> pd.DataFrame:
    if not x_train_path.exists():
        raise FileNotFoundError(f"Fant ikke X_train: {x_train_path}. Kjør WBS 3.3 (datasplitt) først.")
    if not y_train_path.exists():
        raise FileNotFoundError(f"Fant ikke y_train: {y_train_path}. Kjør WBS 3.3 (datasplitt) først.")

    x_train = les_dataset(x_train_path)
    y_train = les_dataset(y_train_path)

    if TARGET_KOLONNE not in y_train.columns:
        raise ValueError(f"y_train mangler målkolonnen '{TARGET_KOLONNE}'. Fant kolonner: {list(y_train.columns)}")
    if len(x_train) != len(y_train):
        raise ValueError(f"X_train ({len(x_train)} rader) og y_train ({len(y_train)} rader) har ulik lengde.")

    df = x_train.reset_index(drop=True).copy()
    df[TARGET_KOLONNE] = y_train[TARGET_KOLONNE].reset_index(drop=True)

    mangler = [kol for kol in NUMERISKE_KOLONNER if kol not in df.columns]
    if mangler:
        raise ValueError(f"Treningssettet mangler påkrevde numeriske kolonner: {mangler}")

    numerisk = df[NUMERISKE_KOLONNER].apply(pd.to_numeric, errors="raise")
    return numerisk


def lag_korrelasjonsmatrise(numerisk_df: pd.DataFrame) -> pd.DataFrame:
    return numerisk_df.corr(method="pearson")


def lag_fig_korrelasjon(corr: pd.DataFrame, fig_path: Path) -> None:
    plt.figure(figsize=(9, 7.5))
    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        center=0,
        vmin=-1,
        vmax=1,
        square=True,
        linewidths=0.5,
        cbar_kws={"label": "Pearson-korrelasjon"},
    )
    plt.title("Korrelasjon mellom numeriske variabler og salg (treningsdata 2022–2024)")
    plt.xticks(rotation=45, ha="right")
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig(fig_path, dpi=150)
    plt.close()


def skriv_markdown(md_path: Path, numerisk_df: pd.DataFrame, corr: pd.DataFrame) -> None:
    # Sales-korrelasjoner mot de øvrige variablene (eksklusiv seg selv).
    sales_korr = corr[TARGET_KOLONNE].drop(labels=[TARGET_KOLONNE]).sort_values(key=lambda s: s.abs(), ascending=False)
    sterkeste_var = str(sales_korr.index[0])
    sterkeste_verdi = float(sales_korr.iloc[0])
    svakeste_var = str(sales_korr.index[-1])
    svakeste_verdi = float(sales_korr.iloc[-1])

    # Maksimal innbyrdes korrelasjon mellom prediktorene (uten target og uten diagonalen).
    prediktorer = [kol for kol in NUMERISKE_KOLONNER if kol != TARGET_KOLONNE]
    pred_corr = corr.loc[prediktorer, prediktorer].copy()
    maks_par = None
    maks_verdi = 0.0
    for i, rad in enumerate(prediktorer):
        for kol in prediktorer[i + 1 :]:
            verdi = float(pred_corr.loc[rad, kol])
            if abs(verdi) > abs(maks_verdi):
                maks_verdi = verdi
                maks_par = (rad, kol)

    maks_sales_abs = float(sales_korr.abs().max())

    lines = [
        "# Korrelasjonsanalyse av numeriske variabler (Figur 8.3)",
        "",
        "## Datagrunnlag",
        "",
        "- Input: `06_datasplitt/X_train.csv` + `06_datasplitt/y_train.csv` (treningsdata 2022–2024)",
        f"- Antall observasjoner: {len(numerisk_df)}",
        f"- Variabler ({len(NUMERISKE_KOLONNER)}): " + ", ".join(f"`{kol}`" for kol in NUMERISKE_KOLONNER),
        "- One-hot-kodede kategorier er holdt utenfor (binære variabler gir misvisende Pearson-korrelasjon).",
        "",
        "## Hovedfunn",
        "",
        f"- Salget har tilnærmet null lineær korrelasjon med samtlige numeriske prediktorer. Sterkeste (i tallverdi) er `{sterkeste_var}` ({sterkeste_verdi:.2f}), svakeste er `{svakeste_var}` ({svakeste_verdi:.2f}); ingen overstiger {maks_sales_abs:.2f} i tallverdi.",
        f"- Blant prediktorene er kalendervariablene sterkt innbyrdes korrelert, sterkest `{maks_par[0]}` mot `{maks_par[1]}` ({maks_verdi:.2f}). Dette er en mekanisk multikollinearitet fordi `quarter`, `month` og `weekofyear` koder samme kalender på ulik oppløsning.",
        "",
        "## Betydning for tolkningen (jf. §9.3)",
        "",
        "- Den nær fraværende lineære koblingen mellom de numeriske prediktorene og salget understøtter at en stor andel av variasjonen er irreduserbart støygulv som ingen modellklasse kan forklare bort med de tilgjengelige variablene.",
        "- At ingen enkelt numerisk variabel bærer en sterk bivariat sammenheng med salget, er konsistent med at modellene møter det samme feilgulvet og dermed lander tett på hverandre på de samlede metrikkene.",
        "- Den sterke innbyrdes korrelasjonen mellom kalendervariablene er en multikollinearitet som svekker tolkbarheten av enkeltkoeffisienter i den lineære modellen (jf. forutsetningene i kap. 3.1 og begrensningene i §9.5), men som angår variabler som uansett bærer lite salgssignal her.",
        "",
    ]

    md_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    sns.set_theme(style="whitegrid")

    aktivitetsmappe = Path(__file__).resolve().parent
    repo_root = Path(__file__).resolve().parents[3]
    splitt_mappe = repo_root / "006 analysis" / "aktiviteter" / "06_datasplitt"
    x_train_path = splitt_mappe / "X_train.csv"
    y_train_path = splitt_mappe / "y_train.csv"

    numerisk_df = bygg_numerisk_treningssett(x_train_path, y_train_path)
    corr = lag_korrelasjonsmatrise(numerisk_df)

    tab_path = aktivitetsmappe / "tab_korrelasjon_numerisk.csv"
    corr.round(4).to_csv(tab_path, index=True, encoding="utf-8")

    fig_path = aktivitetsmappe / "fig_korrelasjon_numerisk.png"
    lag_fig_korrelasjon(corr, fig_path)

    md_path = aktivitetsmappe / "korrelasjon.md"
    skriv_markdown(md_path, numerisk_df, corr)

    print("Korrelasjonsanalyse ferdig: numeriske variabler vs salg")
    print(f"- Rader analysert: {len(numerisk_df)}")
    print(f"- {tab_path.name}")
    print(f"- {fig_path.name}")
    print(f"- {md_path.name}")


if __name__ == "__main__":
    main()
