from pathlib import Path

import pandas as pd


DATO_KOLONNE = "Order Date"
NUMERISKE_KOLONNER = ["Sales", "Discount", "Profit"]
KRITISKE_KOLONNER = [DATO_KOLONNE, *NUMERISKE_KOLONNER]


def les_dataset(csv_path: Path) -> pd.DataFrame:
    """Les CSV robust ved ukjent separator og eventuell BOM."""
    df = pd.read_csv(csv_path, encoding="utf-8-sig")
    if df.shape[1] == 1:
        df = pd.read_csv(csv_path, sep=";", encoding="utf-8-sig")
    return df


def standardiser_tekstkolonner(df: pd.DataFrame) -> pd.DataFrame:
    tekstkolonner = df.select_dtypes(include=["object", "string"]).columns
    for col in tekstkolonner:
        df[col] = df[col].astype("string").str.strip()
    return df


def tolk_dato(verdi: object) -> pd.Timestamp:
    if pd.isna(verdi):
        return pd.NaT

    tekst = str(verdi).strip()
    if not tekst:
        return pd.NaT

    if "-" in tekst:
        return pd.to_datetime(tekst, format="%d-%m-%Y", errors="coerce")

    if "/" in tekst:
        return pd.to_datetime(tekst, format="%m/%d/%Y", errors="coerce")

    return pd.to_datetime(tekst, format="mixed", errors="coerce")


def tell_datoformat(series: pd.Series) -> dict[str, int]:
    dato_tekst = series.astype("string")
    har_bindestrek = dato_tekst.str.contains("-", regex=False, na=False)
    har_skrastrek = dato_tekst.str.contains("/", regex=False, na=False)

    return {
        "dd-mm-yyyy": int(har_bindestrek.sum()),
        "mm/dd/yyyy": int(har_skrastrek.sum()),
        "annet": int((~har_bindestrek & ~har_skrastrek).sum()),
    }


def lag_kolonneprofil(df: pd.DataFrame) -> pd.DataFrame:
    profiler = []

    for col in df.columns:
        s = df[col]
        dtype = str(s.dtype)
        missing = int(s.isna().sum())
        missing_pct = round(float(s.isna().mean() * 100), 2)
        unique = int(s.nunique(dropna=True))

        if pd.api.types.is_numeric_dtype(s):
            min_val = s.min(skipna=True)
            max_val = s.max(skipna=True)
        elif pd.api.types.is_datetime64_any_dtype(s):
            min_val = s.min(skipna=True)
            max_val = s.max(skipna=True)
            if pd.notna(min_val):
                min_val = min_val.date().isoformat()
            if pd.notna(max_val):
                max_val = max_val.date().isoformat()
        else:
            min_val = ""
            max_val = ""

        eksempel = " | ".join(s.dropna().astype(str).head(3).tolist())

        profiler.append(
            {
                "kolonne": col,
                "datatype": dtype,
                "manglende_verdier": missing,
                "manglende_andel_pct": missing_pct,
                "antall_unike": unique,
                "min": min_val,
                "max": max_val,
                "eksempelverdier": eksempel,
            }
        )

    return pd.DataFrame(profiler)


def lag_renselogg(
    df_inn: pd.DataFrame,
    df_renset: pd.DataFrame,
    datoformat: dict[str, int],
    ugyldige_datoer: int,
    rader_fjernet_kritisk: int,
    dubletter_fjernet: int,
) -> pd.DataFrame:
    data = [
        ("antall_rader_inn", len(df_inn), "Observasjoner i rådata"),
        ("antall_kolonner_inn", len(df_inn.columns), "Variabler i rådata"),
        ("manglende_verdier_inn", int(df_inn.isna().sum().sum()), "Totalt manglende i rådata"),
        ("dubletter_inn", int(df_inn.duplicated().sum()), "Eksakte dublettrader i rådata"),
        ("datoformat_dd_mm_yyyy", datoformat["dd-mm-yyyy"], "Tolket fra verdier med bindestrek"),
        ("datoformat_mm_dd_yyyy", datoformat["mm/dd/yyyy"], "Tolket fra verdier med skråstrek"),
        ("datoformat_annet", datoformat["annet"], "Verdier uten kjent mønster"),
        ("ugyldige_datoer_etter_tolkning", ugyldige_datoer, "Datoer som ikke lot seg parse"),
        (
            "rader_fjernet_manglende_kritisk_felt",
            rader_fjernet_kritisk,
            "Rader fjernet etter kontroll av dato og numeriske nøkkelfelt",
        ),
        ("dubletter_fjernet", dubletter_fjernet, "Fjernet etter standardisering"),
        ("antall_rader_ut", len(df_renset), "Observasjoner i renset datasett"),
        ("manglende_verdier_ut", int(df_renset.isna().sum().sum()), "Totalt manglende etter rens"),
        ("dubletter_ut", int(df_renset.duplicated().sum()), "Eksakte dublettrader etter rens"),
    ]

    return pd.DataFrame(data, columns=["målepunkt", "verdi", "kommentar"])


def skriv_markdown(
    md_path: Path,
    df_inn: pd.DataFrame,
    df_renset: pd.DataFrame,
    datoformat: dict[str, int],
    ugyldige_datoer: int,
    rader_fjernet_kritisk: int,
    dubletter_fjernet: int,
) -> None:
    state_unike = int(df_renset["State"].nunique(dropna=True)) if "State" in df_renset.columns else -1

    lines = [
        "# Dataprosessering (WBS 3.1)",
        "",
        "## Kort oppsummering",
        "",
        f"- Antall observasjoner inn: {len(df_inn)}",
        f"- Antall observasjoner ut: {len(df_renset)}",
        f"- Rader fjernet på grunn av manglende kritiske felt: {rader_fjernet_kritisk}",
        f"- Dubletter fjernet: {dubletter_fjernet}",
        f"- Ugyldige datoer etter tolkning: {ugyldige_datoer}",
        "",
        "## Tolkningsregler",
        "",
        "- Verdier med `-` tolkes som `dd-mm-yyyy`.",
        "- Verdier med `/` tolkes som `mm/dd/yyyy`.",
        "- Renset datasett lagres med ISO-format `YYYY-MM-DD` i kolonnen `Order Date`.",
        "",
        "## Funn i rådata",
        "",
        f"- Datoer med `dd-mm-yyyy`: {datoformat['dd-mm-yyyy']}",
        f"- Datoer med `mm/dd/yyyy`: {datoformat['mm/dd/yyyy']}",
        f"- Datoer med annet mønster: {datoformat['annet']}",
        f"- Totalt manglende verdier i rådata: {int(df_inn.isna().sum().sum())}",
        f"- Eksakte dubletter i rådata: {int(df_inn.duplicated().sum())}",
        "",
        "## Merknad for videre modellering",
        "",
    ]

    if state_unike == 1:
        lines.append("- `State` har bare én unik verdi i datasettet og kan vurderes ekskludert i senere modellering.")
    else:
        lines.append("- Bruk kolonneprofilen til å vurdere variabler med lav variasjon før modellering.")

    lines.extend(
        [
            "- Bruk `dataset_renset.csv` som grunnlag for datasplitt og videre feature engineering.",
            "",
        ]
    )

    md_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    aktivitetsmappe = Path(__file__).resolve().parent
    repo_root = Path(__file__).resolve().parents[3]
    csv_path = repo_root / "004 data" / "Dagligvare_Dataset.csv"

    if not csv_path.exists():
        raise FileNotFoundError(f"Fant ikke datasett: {csv_path}")

    df_inn = les_dataset(csv_path)
    df_renset = standardiser_tekstkolonner(df_inn.copy())
    datoformat = tell_datoformat(df_renset[DATO_KOLONNE])

    for col in NUMERISKE_KOLONNER:
        df_renset[col] = pd.to_numeric(df_renset[col], errors="coerce")

    df_renset[DATO_KOLONNE] = df_renset[DATO_KOLONNE].map(tolk_dato)
    ugyldige_datoer = int(df_renset[DATO_KOLONNE].isna().sum())

    kritisk_mask = df_renset[KRITISKE_KOLONNER].notna().all(axis=1)
    rader_fjernet_kritisk = int((~kritisk_mask).sum())
    df_renset = df_renset.loc[kritisk_mask].copy()

    dubletter_før = int(df_renset.duplicated().sum())
    if dubletter_før:
        df_renset = df_renset.drop_duplicates().copy()

    df_renset = df_renset.sort_values([DATO_KOLONNE, "Order ID"]).reset_index(drop=True)

    profil_df = lag_kolonneprofil(df_renset)
    renselogg_df = lag_renselogg(
        df_inn=df_inn,
        df_renset=df_renset,
        datoformat=datoformat,
        ugyldige_datoer=ugyldige_datoer,
        rader_fjernet_kritisk=rader_fjernet_kritisk,
        dubletter_fjernet=dubletter_før,
    )

    dataset_path = aktivitetsmappe / "dataset_renset.csv"
    df_lagring = df_renset.copy()
    df_lagring[DATO_KOLONNE] = df_lagring[DATO_KOLONNE].dt.strftime("%Y-%m-%d")
    df_lagring.to_csv(dataset_path, index=False)

    tab_renselogg = aktivitetsmappe / "tab_renselogg.csv"
    tab_renselogg.write_text(renselogg_df.to_csv(index=False), encoding="utf-8")

    tab_datakvalitet = aktivitetsmappe / "tab_datakvalitet_etter_rens.csv"
    tab_datakvalitet.write_text(profil_df.to_csv(index=False), encoding="utf-8")

    md_path = aktivitetsmappe / "dataprosessering.md"
    skriv_markdown(
        md_path=md_path,
        df_inn=df_inn,
        df_renset=df_renset,
        datoformat=datoformat,
        ugyldige_datoer=ugyldige_datoer,
        rader_fjernet_kritisk=rader_fjernet_kritisk,
        dubletter_fjernet=dubletter_før,
    )

    print("WBS 3.1 ferdig: dataprosessering dokumentert")
    print(f"- Rader inn: {len(df_inn)}, rader ut: {len(df_renset)}")
    print(f"- Datoer med bindestrek: {datoformat['dd-mm-yyyy']}")
    print(f"- Datoer med skråstrek: {datoformat['mm/dd/yyyy']}")
    print(f"- {dataset_path.name}")
    print(f"- {tab_renselogg.name}")
    print(f"- {tab_datakvalitet.name}")
    print(f"- {md_path.name}")


if __name__ == "__main__":
    main()
