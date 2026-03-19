from pathlib import Path

import pandas as pd


def les_dataset(csv_path: Path) -> pd.DataFrame:
    """Les CSV robust ved ukjent separator."""
    df = pd.read_csv(csv_path)
    if df.shape[1] == 1:
        df = pd.read_csv(csv_path, sep=";")
    return df


def finn_periode(df: pd.DataFrame) -> tuple[str, str]:
    for kandidat in ["Order Date", "order_date", "date", "dato"]:
        if kandidat in df.columns:
            dato = pd.to_datetime(df[kandidat], errors="coerce")
            if dato.notna().any():
                return str(dato.min().date()), str(dato.max().date())
    return "ukjent", "ukjent"


def profiler_kolonne(df: pd.DataFrame, col: str) -> dict:
    s = df[col]
    dtype = str(s.dtype)
    missing = int(s.isna().sum())
    missing_pct = round(float(s.isna().mean() * 100), 2)
    unique = int(s.nunique(dropna=True))

    if pd.api.types.is_numeric_dtype(s):
        min_val = s.min(skipna=True)
        max_val = s.max(skipna=True)
    else:
        min_val = ""
        max_val = ""

    eksempel = ""
    for val in s.dropna().astype(str).head(3).tolist():
        if eksempel:
            eksempel += " | "
        eksempel += val

    return {
        "kolonne": col,
        "datatype": dtype,
        "manglende_verdier": missing,
        "manglende_andel_pct": missing_pct,
        "antall_unike": unique,
        "min": min_val,
        "max": max_val,
        "eksempelverdier": eksempel,
    }


def skriv_markdown(df: pd.DataFrame, tab_path: Path, md_path: Path) -> None:
    start, slutt = finn_periode(df)
    antall_rader = len(df)
    antall_kolonner = len(df.columns)

    mangler = int(df.isna().sum().sum())
    mangler_pct = round(float(df.isna().sum().sum() / max(df.size, 1) * 100), 2)

    lines = [
        "# Datasettdokumentasjon (WBS 2.4)",
        "",
        "## Kort oppsummering",
        "",
        f"- Antall observasjoner: {antall_rader}",
        f"- Antall variabler: {antall_kolonner}",
        f"- Periode (tolket fra dato): {start} til {slutt}",
        f"- Totalt manglende verdier: {mangler} ({mangler_pct}%)",
        "",
        "## Datagrunnlag",
        "",
        "- Kilde: `004 data/Dagligvare_Dataset.csv`",
        "- Variabelprofil: se `tab_dataset_dokumentasjon.csv`",
        "",
        "## Videre bruk",
        "",
        "- Bruk variabelprofilen i metode/data-kapittelet i rapporten.",
        "- Bruk denne dokumentasjonen som grunnlag for WBS 3.1 (rense data).",
        "",
    ]

    md_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    aktivitetsmappe = Path(__file__).resolve().parent
    repo_root = Path(__file__).resolve().parents[3]
    csv_path = repo_root / "004 data" / "Dagligvare_Dataset.csv"

    if not csv_path.exists():
        raise FileNotFoundError(f"Fant ikke datasett: {csv_path}")

    df = les_dataset(csv_path)

    profil = [profiler_kolonne(df, col) for col in df.columns]
    profil_df = pd.DataFrame(profil)

    tab_path = aktivitetsmappe / "tab_dataset_dokumentasjon.csv"
    profil_df.to_csv(tab_path, index=False)

    md_path = aktivitetsmappe / "dataset_dokumentasjon.md"
    skriv_markdown(df, tab_path, md_path)

    print("WBS 2.4 ferdig: dokumentert datasett")
    print(f"- Rader: {len(df)}, kolonner: {len(df.columns)}")
    print(f"- {tab_path.name}")
    print(f"- {md_path.name}")


if __name__ == "__main__":
    main()
