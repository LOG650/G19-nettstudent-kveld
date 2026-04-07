from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_percentage_error, root_mean_squared_error


INPUT_PROGNOSE_MAANED = "12_prognoser_2025/tab_prognoser_2025_maaned.csv"
INPUT_FEILDETALJ = "13_rmse_og_mape/tab_prognosefeil_2025_detalj.csv"
INPUT_RMSE_MAANED = "13_rmse_og_mape/tab_rmse_mape_maaned.csv"
INPUT_MODELLSAMMENLIGNING = "14_sammenligne_modellresultater/tab_modellsammenligning_oversikt.csv"
INPUT_MAANEDSVINNERE = "14_sammenligne_modellresultater/tab_maanedlige_modellvinnere.csv"
INPUT_VIKTIGE_VARIABLER = "15_viktige_variabler/tab_viktige_variabler_oversikt.csv"

MODELLREKKEFOLGE = ["benchmark lineær", "baseline RF", "tuned RF"]
FORVENTEDE_MAANEDER = [f"2025-{maaned:02d}" for maaned in range(1, 13)]
FORVENTET_FEILRADER = 3312
FORVENTET_SEGMENTRADER = 14
FORVENTET_SEGMENTMETRIKKRADER = 42
SEGMENTDIMENSJONER = ["quarter", "discount_band", "Region", "sales_band"]
SEGMENTORDEN = {
    "quarter": [1, 2, 3, 4],
    "discount_band": ["lav", "middels", "hoy"],
    "Region": ["Central", "East", "South", "West"],
    "sales_band": ["lavt salg", "middels salg", "hoyt salg"],
}
PREDIKSJONSKOLONNER = {
    "benchmark lineær": "prognose_lineaer_regresjon",
    "baseline RF": "prognose_random_forest_baseline",
    "tuned RF": "prognose_random_forest_tuned",
}
PROGNOSE_SUMKOLONNER = {
    "benchmark lineær": "prognose_lineaer_regresjon_sum",
    "baseline RF": "prognose_random_forest_baseline_sum",
    "tuned RF": "prognose_random_forest_tuned_sum",
}


def les_dataset(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path, encoding="utf-8-sig")
    if df.shape[1] == 1:
        df = pd.read_csv(csv_path, sep=";", encoding="utf-8-sig")
    return df


def modellorden() -> dict[str, int]:
    return {navn: indeks for indeks, navn in enumerate(MODELLREKKEFOLGE)}


def segmentorden(segmentdimensjon: str) -> dict[object, int]:
    return {verdi: indeks for indeks, verdi in enumerate(SEGMENTORDEN[segmentdimensjon])}


def valider_modellsammenligning(oversikt_df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    krav = ["modellnavn", "modellrolle", "samlet_vurdering_5_3"]
    mangler = [kol for kol in krav if kol not in oversikt_df.columns]
    if mangler:
        raise ValueError(f"WBS 6.1 mangler nødvendige kolonner i WBS 5.3-oversikten: {mangler}")

    oversikt_df = oversikt_df.copy()
    oversikt_df["modellrekkefolge"] = oversikt_df["modellrolle"].map(modellorden())
    if oversikt_df["modellrekkefolge"].isna().any():
        roller = oversikt_df["modellrolle"].tolist()
        raise ValueError(f"WBS 6.1 fant ukjente modellroller i WBS 5.3-oversikten: {roller}")

    anbefalte = oversikt_df.loc[oversikt_df["samlet_vurdering_5_3"] == "anbefalt"].reset_index(drop=True)
    if len(anbefalte) != 1:
        raise ValueError(f"WBS 6.1 forventer nøyaktig én anbefalt modell fra WBS 5.3, men fant {len(anbefalte)}.")

    anbefalt = anbefalte.iloc[0]
    if anbefalt["modellrolle"] != "tuned RF":
        raise ValueError(
            "WBS 6.1 er definert med `tuned RF` som tolkningsmessig hovedmodell. "
            f"WBS 5.3 peker nå på `{anbefalt['modellrolle']}` og planen må i så fall revideres eksplisitt."
        )

    return oversikt_df.sort_values("modellrekkefolge").reset_index(drop=True), anbefalt


def valider_viktige_variabler(viktige_df: pd.DataFrame) -> pd.DataFrame:
    krav = ["prioritet_5_4", "feature", "variabelgruppe"]
    mangler = [kol for kol in krav if kol not in viktige_df.columns]
    if mangler:
        raise ValueError(f"WBS 6.1 mangler nødvendige kolonner i WBS 5.4-oversikten: {mangler}")

    viktige_df = viktige_df.copy()
    viktige_df["prioritet_5_4"] = pd.to_numeric(viktige_df["prioritet_5_4"], errors="raise").astype(int)
    topp = viktige_df.sort_values("prioritet_5_4").iloc[0]
    if int(topp["prioritet_5_4"]) != 1 or topp["feature"] != "Discount":
        raise ValueError(
            "WBS 6.1 forventer at `Discount` er prioritet 1 i WBS 5.4, "
            f"men fant `{topp['feature']}` som toppvariabel."
        )

    return viktige_df.sort_values("prioritet_5_4").reset_index(drop=True)


def valider_prognose_maaned(prognose_df: pd.DataFrame) -> pd.DataFrame:
    krav = ["år_måned", "month", "sales_faktisk_sum", *PROGNOSE_SUMKOLONNER.values()]
    mangler = [kol for kol in krav if kol not in prognose_df.columns]
    if mangler:
        raise ValueError(f"WBS 6.1 mangler nødvendige kolonner i månedlige prognoser: {mangler}")

    if len(prognose_df) != 12:
        raise ValueError(f"WBS 6.1 forventer 12 månedsrader i prognoseoppsummeringen, men fant {len(prognose_df)}.")

    prognose_df = prognose_df.copy()
    prognose_df["month"] = pd.to_numeric(prognose_df["month"], errors="raise").astype(int)
    prognose_df["sales_faktisk_sum"] = pd.to_numeric(prognose_df["sales_faktisk_sum"], errors="raise")
    for kol in PROGNOSE_SUMKOLONNER.values():
        prognose_df[kol] = pd.to_numeric(prognose_df[kol], errors="raise")

    måneder = prognose_df["år_måned"].tolist()
    if måneder != FORVENTEDE_MAANEDER:
        raise ValueError(f"WBS 6.1 forventer månedene {FORVENTEDE_MAANEDER}, men fant {måneder}.")

    return prognose_df.sort_values(["år_måned", "month"]).reset_index(drop=True)


def valider_rmse_maaned(maaned_df: pd.DataFrame) -> pd.DataFrame:
    krav = ["år_måned", "month", "modellnavn", "modellrolle", "rmse_maaned", "mape_maaned_pct"]
    mangler = [kol for kol in krav if kol not in maaned_df.columns]
    if mangler:
        raise ValueError(f"WBS 6.1 mangler nødvendige kolonner i månedlig metrikkfil: {mangler}")

    if len(maaned_df) != 36:
        raise ValueError(f"WBS 6.1 forventer 36 rader i månedlig metrikkfil, men fant {len(maaned_df)}.")

    maaned_df = maaned_df.copy()
    maaned_df["month"] = pd.to_numeric(maaned_df["month"], errors="raise").astype(int)
    maaned_df["rmse_maaned"] = pd.to_numeric(maaned_df["rmse_maaned"], errors="raise")
    maaned_df["mape_maaned_pct"] = pd.to_numeric(maaned_df["mape_maaned_pct"], errors="raise")
    for kol in ["rmse_maaned", "mape_maaned_pct"]:
        if maaned_df[kol].isna().any() or not np.isfinite(maaned_df[kol]).all():
            raise ValueError(f"Kolonnen `{kol}` i månedlig metrikkfil inneholder NaN eller ikke-endelige verdier.")

    måneder = sorted(maaned_df["år_måned"].unique().tolist())
    if måneder != FORVENTEDE_MAANEDER:
        raise ValueError(f"WBS 6.1 forventer månedene {FORVENTEDE_MAANEDER}, men fant {måneder}.")

    maaned_df["modellrekkefolge"] = maaned_df["modellrolle"].map(modellorden())
    return maaned_df.sort_values(["år_måned", "month", "modellrekkefolge"]).reset_index(drop=True)


def valider_maanedsvinnere(vinnere_df: pd.DataFrame) -> pd.DataFrame:
    krav = ["år_måned", "month", "rmse_vinner", "mape_vinner", "samme_vinner"]
    mangler = [kol for kol in krav if kol not in vinnere_df.columns]
    if mangler:
        raise ValueError(f"WBS 6.1 mangler nødvendige kolonner i månedsvinnerfilen: {mangler}")

    if len(vinnere_df) != 12:
        raise ValueError(f"WBS 6.1 forventer 12 rader i månedsvinnerfilen, men fant {len(vinnere_df)}.")

    vinnere_df = vinnere_df.copy()
    vinnere_df["month"] = pd.to_numeric(vinnere_df["month"], errors="raise").astype(int)
    måneder = vinnere_df["år_måned"].tolist()
    if måneder != FORVENTEDE_MAANEDER:
        raise ValueError(f"WBS 6.1 forventer månedene {FORVENTEDE_MAANEDER}, men fant {måneder}.")

    return vinnere_df.sort_values(["år_måned", "month"]).reset_index(drop=True)


def valider_feildetalj(feil_df: pd.DataFrame) -> pd.DataFrame:
    krav = [
        "rad_id_2025",
        "Order Date",
        "Sales_faktisk",
        "Discount",
        "Region",
        "quarter",
        *PREDIKSJONSKOLONNER.values(),
        "feil_lineaer_regresjon",
        "abs_feil_lineaer_regresjon",
        "ape_lineaer_regresjon_pct",
        "feil_random_forest_baseline",
        "abs_feil_random_forest_baseline",
        "ape_random_forest_baseline_pct",
        "feil_random_forest_tuned",
        "abs_feil_random_forest_tuned",
        "ape_random_forest_tuned_pct",
    ]
    mangler = [kol for kol in krav if kol not in feil_df.columns]
    if mangler:
        raise ValueError(f"WBS 6.1 mangler nødvendige kolonner i detaljert feilfil: {mangler}")

    if len(feil_df) != FORVENTET_FEILRADER:
        raise ValueError(
            f"WBS 6.1 forventer {FORVENTET_FEILRADER} rader i detaljert feilfil, men fant {len(feil_df)}."
        )

    feil_df = feil_df.copy()
    feil_df["Order Date"] = pd.to_datetime(feil_df["Order Date"], errors="raise")
    for kol in [
        "Sales_faktisk",
        "Discount",
        "quarter",
        *PREDIKSJONSKOLONNER.values(),
        "feil_lineaer_regresjon",
        "abs_feil_lineaer_regresjon",
        "ape_lineaer_regresjon_pct",
        "feil_random_forest_baseline",
        "abs_feil_random_forest_baseline",
        "ape_random_forest_baseline_pct",
        "feil_random_forest_tuned",
        "abs_feil_random_forest_tuned",
        "ape_random_forest_tuned_pct",
    ]:
        feil_df[kol] = pd.to_numeric(feil_df[kol], errors="raise")
        if feil_df[kol].isna().any() or not np.isfinite(feil_df[kol]).all():
            raise ValueError(f"Kolonnen `{kol}` i detaljert feilfil inneholder NaN eller ikke-endelige verdier.")

    if (feil_df["Sales_faktisk"] <= 0).any():
        raise ValueError("WBS 6.1 forventer positive `Sales_faktisk`-verdier i detaljert feilfil.")

    feil_df["year_from_date"] = feil_df["Order Date"].dt.year
    if sorted(feil_df["year_from_date"].unique().tolist()) != [2025]:
        raise ValueError("WBS 6.1 forventer at detaljert feilfil kun dekker 2025.")

    return feil_df.drop(columns=["year_from_date"])


def rabattband(verdi: float) -> str:
    if verdi < 0 or verdi > 0.35:
        raise ValueError(f"WBS 6.1 forventer Discount i intervallet [0, 0.35], men fant {verdi}.")
    if verdi < 0.15:
        return "lav"
    if verdi < 0.25:
        return "middels"
    return "hoy"


def legg_til_segmenter(feil_df: pd.DataFrame) -> tuple[pd.DataFrame, float, float]:
    feil_df = feil_df.copy()
    feil_df["discount_band"] = feil_df["Discount"].map(rabattband)

    q1, q2 = feil_df["Sales_faktisk"].quantile([1 / 3, 2 / 3]).tolist()
    if not q1 < q2:
        raise ValueError("WBS 6.1 forventer stigende tertilgrenser for `Sales_faktisk`.")

    def sales_band(verdi: float) -> str:
        if verdi <= q1:
            return "lavt salg"
        if verdi <= q2:
            return "middels salg"
        return "hoyt salg"

    feil_df["sales_band"] = feil_df["Sales_faktisk"].map(sales_band)
    return feil_df, float(q1), float(q2)


def bygg_segmentdefinisjoner(q1: float, q2: float) -> pd.DataFrame:
    rader = [
        {"segmentdimensjon": "quarter", "segmentverdi": 1, "definisjon": "Rader der `quarter = 1` i testdata for 2025."},
        {"segmentdimensjon": "quarter", "segmentverdi": 2, "definisjon": "Rader der `quarter = 2` i testdata for 2025."},
        {"segmentdimensjon": "quarter", "segmentverdi": 3, "definisjon": "Rader der `quarter = 3` i testdata for 2025."},
        {"segmentdimensjon": "quarter", "segmentverdi": 4, "definisjon": "Rader der `quarter = 4` i testdata for 2025."},
        {
            "segmentdimensjon": "discount_band",
            "segmentverdi": "lav",
            "definisjon": "Rader med `0.00 <= Discount < 0.15`.",
        },
        {
            "segmentdimensjon": "discount_band",
            "segmentverdi": "middels",
            "definisjon": "Rader med `0.15 <= Discount < 0.25`.",
        },
        {
            "segmentdimensjon": "discount_band",
            "segmentverdi": "hoy",
            "definisjon": "Rader med `0.25 <= Discount <= 0.35`.",
        },
        {"segmentdimensjon": "Region", "segmentverdi": "Central", "definisjon": "Rader der `Region = Central`."},
        {"segmentdimensjon": "Region", "segmentverdi": "East", "definisjon": "Rader der `Region = East`."},
        {"segmentdimensjon": "Region", "segmentverdi": "South", "definisjon": "Rader der `Region = South`."},
        {"segmentdimensjon": "Region", "segmentverdi": "West", "definisjon": "Rader der `Region = West`."},
        {
            "segmentdimensjon": "sales_band",
            "segmentverdi": "lavt salg",
            "definisjon": f"Rader med `Sales_faktisk <= {q1:.1f}` basert på tertiler i hele 2025-testsettet.",
        },
        {
            "segmentdimensjon": "sales_band",
            "segmentverdi": "middels salg",
            "definisjon": f"Rader med `{q1:.1f} < Sales_faktisk <= {q2:.1f}` basert på tertiler i hele 2025-testsettet.",
        },
        {
            "segmentdimensjon": "sales_band",
            "segmentverdi": "hoyt salg",
            "definisjon": f"Rader med `Sales_faktisk > {q2:.1f}` basert på tertiler i hele 2025-testsettet.",
        },
    ]
    definisjoner_df = pd.DataFrame(rader)
    definisjoner_df["segmentdimensjon_rekkefolge"] = definisjoner_df["segmentdimensjon"].map(
        {navn: indeks for indeks, navn in enumerate(SEGMENTDIMENSJONER)}
    )
    definisjoner_df["segmentverdi_rekkefolge"] = definisjoner_df.apply(
        lambda rad: segmentorden(rad["segmentdimensjon"])[rad["segmentverdi"]],
        axis=1,
    )
    definisjoner_df = definisjoner_df.sort_values(
        ["segmentdimensjon_rekkefolge", "segmentverdi_rekkefolge"]
    ).reset_index(drop=True)
    return definisjoner_df.drop(columns=["segmentdimensjon_rekkefolge", "segmentverdi_rekkefolge"])


def bygg_bias_maaned_modell(
    prognose_df: pd.DataFrame,
    maaned_df: pd.DataFrame,
    vinnere_df: pd.DataFrame,
    modellsammenligning_df: pd.DataFrame,
) -> pd.DataFrame:
    modellnavn = modellsammenligning_df.set_index("modellrolle")["modellnavn"].to_dict()
    rader: list[dict[str, object]] = []

    for prognoserad in prognose_df.itertuples(index=False):
        vinnerrad = vinnere_df.loc[vinnere_df["år_måned"] == prognoserad.år_måned].iloc[0]
        maaned_subset = maaned_df.loc[maaned_df["år_måned"] == prognoserad.år_måned].copy()

        for modellrolle in MODELLREKKEFOLGE:
            sumkolonne = PROGNOSE_SUMKOLONNER[modellrolle]
            metrikkrad = maaned_subset.loc[maaned_subset["modellrolle"] == modellrolle].iloc[0]
            prognose_sum = float(getattr(prognoserad, sumkolonne))
            sales_sum = float(prognoserad.sales_faktisk_sum)
            bias_sum = prognose_sum - sales_sum
            if bias_sum > 0:
                retning = "positiv"
            elif bias_sum < 0:
                retning = "negativ"
            else:
                retning = "null"

            rader.append(
                {
                    "år_måned": prognoserad.år_måned,
                    "month": int(prognoserad.month),
                    "modellnavn": modellnavn[modellrolle],
                    "modellrolle": modellrolle,
                    "sales_faktisk_sum": round(sales_sum, 4),
                    "prognose_sum": round(prognose_sum, 4),
                    "bias_sum": round(bias_sum, 4),
                    "bias_pct": round((bias_sum / sales_sum) * 100, 4),
                    "retning_bias": retning,
                    "rmse_maaned": round(float(metrikkrad["rmse_maaned"]), 6),
                    "mape_maaned_pct": round(float(metrikkrad["mape_maaned_pct"]), 4),
                    "rmse_vinner": vinnerrad["rmse_vinner"],
                    "mape_vinner": vinnerrad["mape_vinner"],
                    "samme_vinner": bool(vinnerrad["samme_vinner"]),
                    "modellrekkefolge": modellorden()[modellrolle],
                }
            )

    bias_df = pd.DataFrame(rader)
    return bias_df.sort_values(["år_måned", "month", "modellrekkefolge"]).drop(columns=["modellrekkefolge"]).reset_index(
        drop=True
    )


def bygg_segmentmetrikk_modell(
    feil_df: pd.DataFrame,
    modellsammenligning_df: pd.DataFrame,
) -> pd.DataFrame:
    modellnavn = modellsammenligning_df.set_index("modellrolle")["modellnavn"].to_dict()
    rader: list[dict[str, object]] = []

    for segmentdimensjon in SEGMENTDIMENSJONER:
        orden = segmentorden(segmentdimensjon)
        for segmentverdi in SEGMENTORDEN[segmentdimensjon]:
            subset = feil_df.loc[feil_df[segmentdimensjon] == segmentverdi].copy()
            if subset.empty:
                raise ValueError(
                    f"WBS 6.1 forventer minst én rad for segment `{segmentdimensjon}={segmentverdi}`, men fant ingen."
                )

            for modellrolle in MODELLREKKEFOLGE:
                predkolonne = PREDIKSJONSKOLONNER[modellrolle]
                rmse = float(root_mean_squared_error(subset["Sales_faktisk"], subset[predkolonne]))
                mape_pct = float(mean_absolute_percentage_error(subset["Sales_faktisk"], subset[predkolonne]) * 100)
                rader.append(
                    {
                        "segmentdimensjon": segmentdimensjon,
                        "segmentverdi": segmentverdi,
                        "modellnavn": modellnavn[modellrolle],
                        "modellrolle": modellrolle,
                        "antall_rader": int(len(subset)),
                        "rmse_segment": round(rmse, 6),
                        "mape_segment_pct": round(mape_pct, 4),
                        "segmentdimensjon_rekkefolge": SEGMENTDIMENSJONER.index(segmentdimensjon),
                        "segmentverdi_rekkefolge": orden[segmentverdi],
                        "modellrekkefolge": modellorden()[modellrolle],
                    }
                )

    segment_df = pd.DataFrame(rader)
    segment_df = segment_df.sort_values(
        ["segmentdimensjon_rekkefolge", "segmentverdi_rekkefolge", "modellrekkefolge"]
    ).reset_index(drop=True)
    return segment_df.drop(columns=["segmentdimensjon_rekkefolge", "segmentverdi_rekkefolge", "modellrekkefolge"])


def bygg_segmentvinnere(segment_df: pd.DataFrame) -> pd.DataFrame:
    rader: list[dict[str, object]] = []

    for (segmentdimensjon, segmentverdi), gruppe in segment_df.groupby(["segmentdimensjon", "segmentverdi"], sort=False):
        gruppe = gruppe.copy()
        gruppe["modellrekkefolge"] = gruppe["modellrolle"].map(modellorden())
        rmse_vinner = gruppe.sort_values(["rmse_segment", "mape_segment_pct", "modellrekkefolge"]).iloc[0]
        mape_vinner = gruppe.sort_values(["mape_segment_pct", "rmse_segment", "modellrekkefolge"]).iloc[0]
        rader.append(
            {
                "segmentdimensjon": segmentdimensjon,
                "segmentverdi": segmentverdi,
                "rmse_vinner": rmse_vinner["modellrolle"],
                "rmse_verdi": round(float(rmse_vinner["rmse_segment"]), 6),
                "mape_vinner": mape_vinner["modellrolle"],
                "mape_verdi": round(float(mape_vinner["mape_segment_pct"]), 4),
                "samme_vinner": bool(rmse_vinner["modellrolle"] == mape_vinner["modellrolle"]),
                "segmentdimensjon_rekkefolge": SEGMENTDIMENSJONER.index(segmentdimensjon),
                "segmentverdi_rekkefolge": segmentorden(segmentdimensjon)[segmentverdi],
            }
        )

    vinnere_df = pd.DataFrame(rader)
    vinnere_df = vinnere_df.sort_values(
        ["segmentdimensjon_rekkefolge", "segmentverdi_rekkefolge"]
    ).reset_index(drop=True)
    return vinnere_df.drop(columns=["segmentdimensjon_rekkefolge", "segmentverdi_rekkefolge"])


def skriv_markdown(
    md_path: Path,
    bias_df: pd.DataFrame,
    segmentvinnere_df: pd.DataFrame,
    viktige_df: pd.DataFrame,
    q1: float,
    q2: float,
) -> None:
    tuned_bias = bias_df.loc[bias_df["modellrolle"] == "tuned RF"].copy()
    tuned_bias = tuned_bias.sort_values("month").reset_index(drop=True)
    størst_negativ = tuned_bias.sort_values("bias_sum").head(2).reset_index(drop=True)
    størst_positiv = tuned_bias.sort_values("bias_sum", ascending=False).head(2).reset_index(drop=True)
    rmse_vinnere = int((tuned_bias["rmse_vinner"] == "tuned RF").sum())
    mape_vinnere = int((tuned_bias["mape_vinner"] == "tuned RF").sum())

    quarter_vinnere = segmentvinnere_df.loc[segmentvinnere_df["segmentdimensjon"] == "quarter"].reset_index(drop=True)
    discount_vinnere = segmentvinnere_df.loc[segmentvinnere_df["segmentdimensjon"] == "discount_band"].reset_index(drop=True)
    region_vinnere = segmentvinnere_df.loc[segmentvinnere_df["segmentdimensjon"] == "Region"].reset_index(drop=True)
    sales_vinnere = segmentvinnere_df.loc[segmentvinnere_df["segmentdimensjon"] == "sales_band"].reset_index(drop=True)

    topp_discount = viktige_df.loc[viktige_df["feature"] == "Discount"].iloc[0]
    quarter_rad = viktige_df.loc[viktige_df["feature"] == "quarter"].iloc[0]
    region_features = viktige_df.loc[viktige_df["variabelgruppe"] == "region", "feature"].tolist()

    lines = [
        "# Tolkning av modellresultater (WBS 6.1)",
        "",
        "## Hva WBS 6.1 gjør",
        "",
        "- Aktiviteten tolker observerte modellmønstre på toppen av WBS 5.2, 5.3 og 5.4 uten å trene modeller på nytt eller lage nye prognoser.",
        "- `tuned RF` brukes som hovedmodell fordi den er anbefalt i WBS 5.3.",
        "- Tolkningen er avgrenset til observerte mønstre i månedsbias og segmenterte metrikker. Aktiviteten gjør ikke kausal analyse, diskuterer ikke generelle styrker og svakheter, og gir ikke forretningsanbefalinger.",
        "",
        "## Månedsbilde for anbefalt modell",
        "",
        f"- `tuned RF` vinner `RMSE` i `{rmse_vinnere}` av `12` måneder, men bare `MAPE` i `{mape_vinnere}` av `12` måneder.",
        (
            f"- Størst negativ månedsbias for `tuned RF` er `{størst_negativ.iloc[0]['år_måned']}` "
            f"(`bias_sum={float(størst_negativ.iloc[0]['bias_sum']):.4f}`, "
            f"`bias_pct={float(størst_negativ.iloc[0]['bias_pct']):.4f} %`), "
            f"etterfulgt av `{størst_negativ.iloc[1]['år_måned']}` "
            f"(`bias_sum={float(størst_negativ.iloc[1]['bias_sum']):.4f}`, "
            f"`bias_pct={float(størst_negativ.iloc[1]['bias_pct']):.4f} %`)."
        ),
        (
            f"- Størst positiv månedsbias for `tuned RF` er `{størst_positiv.iloc[0]['år_måned']}` "
            f"(`bias_sum={float(størst_positiv.iloc[0]['bias_sum']):.4f}`, "
            f"`bias_pct={float(størst_positiv.iloc[0]['bias_pct']):.4f} %`)."
        ),
        "- Månedsmønsteret viser at modellen følger totalnivået godt i absolutte termer, men at prosentfeilen svinger mer mellom måneder med ulikt salgsnivå.",
        "",
        "## Segmenter som forklarer metrikk-sprik",
        "",
        (
            f"- `quarter`: `tuned RF` vinner `RMSE` i alle fire kvartaler, mens `MAPE` vinnes av "
            f"`{quarter_vinnere.iloc[0]['mape_vinner']}` i Q1, `{quarter_vinnere.iloc[1]['mape_vinner']}` i Q2, "
            f"`{quarter_vinnere.iloc[2]['mape_vinner']}` i Q3 og `{quarter_vinnere.iloc[3]['mape_vinner']}` i Q4."
        ),
        (
            f"- `discount_band`: `tuned RF` vinner både `RMSE` og `MAPE` ved `lav` og `middels` rabatt, "
            f"mens `MAPE` ved `hoy` rabatt vinnes av `{discount_vinnere.iloc[2]['mape_vinner']}`."
        ),
        (
            f"- `Region`: `tuned RF` vinner `RMSE` i alle fire regioner, mens `MAPE` vinnes av "
            f"`{region_vinnere.iloc[0]['mape_vinner']}` i `Central`, `{region_vinnere.iloc[1]['mape_vinner']}` i `East`, "
            f"`{region_vinnere.iloc[2]['mape_vinner']}` i `South` og `{region_vinnere.iloc[3]['mape_vinner']}` i `West`."
        ),
        (
            f"- `sales_band`: `RMSE` vinnes av `{sales_vinnere.iloc[0]['rmse_vinner']}` for `lavt salg`, "
            f"`{sales_vinnere.iloc[1]['rmse_vinner']}` for `middels salg` og `{sales_vinnere.iloc[2]['rmse_vinner']}` for `hoyt salg`, "
            f"mens `MAPE` vinnes av `{sales_vinnere.iloc[0]['mape_vinner']}`, `{sales_vinnere.iloc[1]['mape_vinner']}` og "
            f"`{sales_vinnere.iloc[2]['mape_vinner']}` i de samme segmentene."
        ),
        (
            f"- Tertilgrensene for `sales_band` er `{q1:.1f}` og `{q2:.1f}`, slik at segmentene brukes som ren tolkningsstøtte for å forstå "
            "hvorfor absolutt feil og prosentfeil reagerer forskjellig."
        ),
        "",
        "## Kobling til viktige variabler fra WBS 5.4",
        "",
        (
            f"- `Discount` er prioritet `{int(topp_discount['prioritet_5_4'])}` i WBS 5.4 og støtter at rabattsegmentene er sentrale "
            "for å forklare forskjeller i prosentfeil mellom modellene."
        ),
        (
            f"- `quarter` er et toppsignal i `tuned RF` med rang `{int(quarter_rad['rang_tuned_rf'])}` i WBS 5.4 og støtter at kvartalsmønstre "
            "brukes som tolkningsakse i 6.1."
        ),
        (
            f"- Regionfeature-ene {', '.join(f'`{feature}`' for feature in region_features)} ligger høyt i WBS 5.4 og henger sammen med at "
            "MAPE-vinneren varierer mellom `Central`, `East`, `South` og `West`."
        ),
        "- `sales_band` er ikke en modellfeature, men et avledet tolkningssegment som brukes for å forklare hvorfor `RMSE` og `MAPE` ikke alltid peker på samme modell.",
        "",
        "## Produserte artefakter",
        "",
        "- `tab_bias_maaned_modell.csv`",
        "- `tab_segmentdefinisjoner.csv`",
        "- `tab_segmentmetrikk_modell.csv`",
        "- `tab_segmentvinnere_tolkning.csv`",
        "- `modelltolkning.md`",
        "",
        "## Avgrensning mot senere WBS-steg",
        "",
        "- WBS 6.1 beskriver observerte mønstre og kobler dem til signalene fra WBS 5.4.",
        "- WBS 6.2 tar videre diskusjon av styrker og svakheter.",
        "- WBS 6.3 tar videre vurdering av praktisk nytte for caset.",
        "",
    ]
    md_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    aktivitetsmappe = Path(__file__).resolve().parent
    repo_aktiviteter = Path(__file__).resolve().parents[1]

    prognose_df = les_dataset(repo_aktiviteter / INPUT_PROGNOSE_MAANED)
    feil_df = les_dataset(repo_aktiviteter / INPUT_FEILDETALJ)
    maaned_df = les_dataset(repo_aktiviteter / INPUT_RMSE_MAANED)
    modellsammenligning_df = les_dataset(repo_aktiviteter / INPUT_MODELLSAMMENLIGNING)
    vinnere_df = les_dataset(repo_aktiviteter / INPUT_MAANEDSVINNERE)
    viktige_df = les_dataset(repo_aktiviteter / INPUT_VIKTIGE_VARIABLER)

    modellsammenligning_df, anbefalt = valider_modellsammenligning(modellsammenligning_df)
    viktige_df = valider_viktige_variabler(viktige_df)
    prognose_df = valider_prognose_maaned(prognose_df)
    maaned_df = valider_rmse_maaned(maaned_df)
    vinnere_df = valider_maanedsvinnere(vinnere_df)
    feil_df = valider_feildetalj(feil_df)
    feil_df, q1, q2 = legg_til_segmenter(feil_df)

    bias_df = bygg_bias_maaned_modell(prognose_df, maaned_df, vinnere_df, modellsammenligning_df)
    definisjoner_df = bygg_segmentdefinisjoner(q1, q2)
    segment_df = bygg_segmentmetrikk_modell(feil_df, modellsammenligning_df)
    segmentvinnere_df = bygg_segmentvinnere(segment_df)

    if len(definisjoner_df) != FORVENTET_SEGMENTRADER:
        raise ValueError(
            f"WBS 6.1 forventer {FORVENTET_SEGMENTRADER} segmentdefinisjonsrader, men fant {len(definisjoner_df)}."
        )

    if len(segment_df) != FORVENTET_SEGMENTMETRIKKRADER:
        raise ValueError(
            f"WBS 6.1 forventer {FORVENTET_SEGMENTMETRIKKRADER} rader i segmentmetrikkfilen, men fant {len(segment_df)}."
        )

    if len(segmentvinnere_df) != FORVENTET_SEGMENTRADER:
        raise ValueError(
            f"WBS 6.1 forventer {FORVENTET_SEGMENTRADER} rader i segmentvinnerfilen, men fant {len(segmentvinnere_df)}."
        )

    bias_path = aktivitetsmappe / "tab_bias_maaned_modell.csv"
    definisjoner_path = aktivitetsmappe / "tab_segmentdefinisjoner.csv"
    segment_path = aktivitetsmappe / "tab_segmentmetrikk_modell.csv"
    segmentvinnere_path = aktivitetsmappe / "tab_segmentvinnere_tolkning.csv"
    markdown_path = aktivitetsmappe / "modelltolkning.md"

    bias_path.write_text(bias_df.to_csv(index=False), encoding="utf-8")
    definisjoner_path.write_text(definisjoner_df.to_csv(index=False), encoding="utf-8")
    segment_path.write_text(segment_df.to_csv(index=False), encoding="utf-8")
    segmentvinnere_path.write_text(segmentvinnere_df.to_csv(index=False), encoding="utf-8")
    skriv_markdown(markdown_path, bias_df, segmentvinnere_df, viktige_df, q1, q2)

    print("WBS 6.1 ferdig: modellresultater tolket")
    print(f"- Hovedmodell: {anbefalt['modellrolle']}")
    print(f"- Segmentrader: {len(segment_df)}")
    print(f"- Størst negativ bias i tuned RF: {bias_df.loc[(bias_df['modellrolle'] == 'tuned RF')].sort_values('bias_sum').iloc[0]['år_måned']}")
    print(f"- {bias_path.name}")
    print(f"- {definisjoner_path.name}")
    print(f"- {segment_path.name}")
    print(f"- {segmentvinnere_path.name}")
    print(f"- {markdown_path.name}")


if __name__ == "__main__":
    main()
