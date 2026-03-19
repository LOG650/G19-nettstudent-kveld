from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def les_dataset(csv_path: Path) -> pd.DataFrame:
    """Les CSV robust ved ukjent separator."""
    df = pd.read_csv(csv_path)
    if df.shape[1] == 1:
        # Fallback dersom datasettet bruker semikolon i stedet for komma.
        df = pd.read_csv(csv_path, sep=";")
    return df


def main() -> None:
    aktivitetsmappe = Path(__file__).resolve().parent
    repo_root = Path(__file__).resolve().parents[3]
    csv_path = repo_root / "004 data" / "Dagligvare_Dataset.csv"

    if not csv_path.exists():
        raise FileNotFoundError(f"Fant ikke datasett: {csv_path}")

    df = les_dataset(csv_path)

    print("Datasett lest:")
    print(f"- Rader: {len(df)}")
    print(f"- Kolonner: {len(df.columns)}")
    print("\nKolonner:")
    for col in df.columns:
        print(f"- {col}")

    oversikt = pd.DataFrame(
        {
            "kolonne": df.columns,
            "datatype": [str(df[c].dtype) for c in df.columns],
            "manglende_verdier": [int(df[c].isna().sum()) for c in df.columns],
            "manglende_andel_pct": [round(float(df[c].isna().mean() * 100), 2) for c in df.columns],
            "antall_unike": [int(df[c].nunique(dropna=True)) for c in df.columns],
        }
    )

    manglende = oversikt[["kolonne", "manglende_verdier", "manglende_andel_pct"]].copy()
    manglende = manglende.sort_values("manglende_verdier", ascending=False)

    tab_oversikt = aktivitetsmappe / "tab_dataset_oversikt.csv"
    tab_manglende = aktivitetsmappe / "tab_manglende_verdier.csv"
    oversikt.to_csv(tab_oversikt, index=False)
    manglende.to_csv(tab_manglende, index=False)

    dtype_counts = oversikt["datatype"].value_counts().sort_values(ascending=False)
    plt.figure(figsize=(8, 5))
    dtype_counts.plot(kind="bar")
    plt.title("Fordeling av datatyper")
    plt.xlabel("Datatype")
    plt.ylabel("Antall kolonner")
    plt.tight_layout()

    fig_path = aktivitetsmappe / "fig_datatype_fordeling.png"
    plt.savefig(fig_path, dpi=150)
    plt.close()

    print("\nGenererte filer:")
    print(f"- {tab_oversikt.name}")
    print(f"- {tab_manglende.name}")
    print(f"- {fig_path.name}")


if __name__ == "__main__":
    main()
