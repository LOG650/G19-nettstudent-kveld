from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


TARGET = "Sales"


def les_dataset(csv_path: Path) -> pd.DataFrame:
    """Les CSV robust ved ukjent separator."""
    df = pd.read_csv(csv_path)
    if df.shape[1] == 1:
        df = pd.read_csv(csv_path, sep=";")
    return df


def er_dato_kolonne(series: pd.Series) -> bool:
    if not pd.api.types.is_object_dtype(series):
        return False
    parsed = pd.to_datetime(series, errors="coerce")
    gyldig_andel = parsed.notna().mean()
    return float(gyldig_andel) >= 0.9


def vurder_variabel(df: pd.DataFrame, col: str) -> dict:
    s = df[col]
    dtype = str(s.dtype)
    unique = int(s.nunique(dropna=True))
    rows = max(len(s), 1)
    unique_ratio = unique / rows
    missing_pct = float(s.isna().mean() * 100)

    lower = col.lower()

    if col == TARGET:
        return {
            "variabel": col,
            "anbefaling": "target",
            "begrunnelse": "Målvariabel for prognose.",
            "datatype": dtype,
            "manglende_pct": round(missing_pct, 2),
            "unike": unique,
            "unik_andel": round(unique_ratio, 4),
        }

    if "id" in lower:
        anbefaling = "ekskluder"
        begrunnelse = "ID-variabel gir vanligvis lite generaliserbar prediksjonsverdi."
    elif "name" in lower:
        anbefaling = "ekskluder"
        begrunnelse = "Navn-kolonne har høy kardinalitet og høy risiko for overtilpasning."
    elif lower == "profit":
        anbefaling = "vurder"
        begrunnelse = "Kan være informativ, men bør sjekkes for lekkasje før modellering."
    elif missing_pct > 40:
        anbefaling = "vurder"
        begrunnelse = "Høy andel manglende verdier krever særskilt håndtering."
    elif er_dato_kolonne(s):
        anbefaling = "inkluder"
        begrunnelse = "Dato kan gi sesongtrekk etter feature engineering."
    elif pd.api.types.is_numeric_dtype(s):
        anbefaling = "inkluder"
        begrunnelse = "Numerisk variabel egner seg direkte for modellering."
    elif unique_ratio > 0.95:
        anbefaling = "ekskluder"
        begrunnelse = "Svært høy unik-andel gir lav generaliserbarhet."
    elif unique <= 50:
        anbefaling = "inkluder"
        begrunnelse = "Kategorisk variabel med håndterbar kardinalitet."
    else:
        anbefaling = "vurder"
        begrunnelse = "Middels/høy kardinalitet, vurder koding og nytte."

    return {
        "variabel": col,
        "anbefaling": anbefaling,
        "begrunnelse": begrunnelse,
        "datatype": dtype,
        "manglende_pct": round(missing_pct, 2),
        "unike": unique,
        "unik_andel": round(unique_ratio, 4),
    }


def main() -> None:
    aktivitetsmappe = Path(__file__).resolve().parent
    repo_root = Path(__file__).resolve().parents[3]
    csv_path = repo_root / "004 data" / "Dagligvare_Dataset.csv"

    if not csv_path.exists():
        raise FileNotFoundError(f"Fant ikke datasett: {csv_path}")

    df = les_dataset(csv_path)
    vurderinger = [vurder_variabel(df, col) for col in df.columns]
    vurdering_df = pd.DataFrame(vurderinger)

    sort_order = {"target": 0, "inkluder": 1, "vurder": 2, "ekskluder": 3}
    vurdering_df["_sort"] = vurdering_df["anbefaling"].map(sort_order)
    vurdering_df = vurdering_df.sort_values(["_sort", "variabel"]).drop(columns=["_sort"])

    tab_path = aktivitetsmappe / "tab_relevante_variabler.csv"
    vurdering_df.to_csv(tab_path, index=False)

    regler_df = pd.DataFrame(
        [
            ["target", "Målvariabel", "Sales settes som målvariabel."],
            ["ekskluder", "ID/navn", "Kolonner med id/name ekskluderes."],
            ["vurder", "Manglende > 40%", "Krever særskilt databehandling."],
            ["inkluder", "Dato (>=90% parsebar)", "Brukes til sesong/features."],
            ["inkluder", "Numerisk", "Brukes direkte som kandidatfeature."],
            ["ekskluder", "Unik-andel > 95%", "Svak generalisering."],
            ["inkluder", "Kategorisk <= 50 unike", "Håndterbar kardinalitet."],
        ],
        columns=["anbefaling", "regel", "beskrivelse"],
    )
    tab_regler = aktivitetsmappe / "tab_variabelregler.csv"
    regler_df.to_csv(tab_regler, index=False)

    plt.figure(figsize=(7, 4))
    counts = vurdering_df["anbefaling"].value_counts().reindex(["target", "inkluder", "vurder", "ekskluder"], fill_value=0)
    counts.plot(kind="bar")
    plt.title("Anbefaling per variabel")
    plt.xlabel("Kategori")
    plt.ylabel("Antall variabler")
    plt.tight_layout()
    fig_path = aktivitetsmappe / "fig_variabelanbefalinger.png"
    plt.savefig(fig_path, dpi=150)
    plt.close()

    print("WBS 2.3 ferdig: foreslått variabelutvalg")
    print(f"- Rader: {len(df)}, kolonner: {len(df.columns)}")
    print(f"- {tab_path.name}")
    print(f"- {tab_regler.name}")
    print(f"- {fig_path.name}")


if __name__ == "__main__":
    main()
