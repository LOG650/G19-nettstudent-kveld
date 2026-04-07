from pathlib import Path

import numpy as np
import pandas as pd


INPUT_OVERSIKT = "13_rmse_og_mape/tab_rmse_mape_oversikt.csv"
INPUT_MAANED = "13_rmse_og_mape/tab_rmse_mape_maaned.csv"
MODELLREKKEFOLGE = ["benchmark lineær", "baseline RF", "tuned RF"]
FORVENTET_MODELLRADER = 3
FORVENTET_MAANEDSRADER = 36
FORVENTEDE_MAANEDER = [f"2025-{maaned:02d}" for maaned in range(1, 13)]
VALID_VURDERINGER = {"anbefalt", "sekundær", "ikke anbefalt"}


def les_dataset(csv_path: Path) -> pd.DataFrame:
    df = pd.read_csv(csv_path, encoding="utf-8-sig")
    if df.shape[1] == 1:
        df = pd.read_csv(csv_path, sep=";", encoding="utf-8-sig")
    return df


def modellorden() -> dict[str, int]:
    return {navn: indeks for indeks, navn in enumerate(MODELLREKKEFOLGE)}


def valider_oversikt(oversikt_df: pd.DataFrame) -> pd.DataFrame:
    krav = ["modellnavn", "modellrolle", "prediksjonskolonne", "rmse_2025", "mape_2025_pct"]
    mangler = [kol for kol in krav if kol not in oversikt_df.columns]
    if mangler:
        raise ValueError(f"WBS 5.3 mangler nødvendige kolonner i totaltabellen: {mangler}")

    if len(oversikt_df) != FORVENTET_MODELLRADER:
        raise ValueError(
            f"WBS 5.3 forventer {FORVENTET_MODELLRADER} modellrader i totaltabellen, men fant {len(oversikt_df)}."
        )

    oversikt_df = oversikt_df.copy()
    oversikt_df["rmse_2025"] = pd.to_numeric(oversikt_df["rmse_2025"], errors="raise")
    oversikt_df["mape_2025_pct"] = pd.to_numeric(oversikt_df["mape_2025_pct"], errors="raise")
    for kol in ["rmse_2025", "mape_2025_pct"]:
        if oversikt_df[kol].isna().any() or not np.isfinite(oversikt_df[kol]).all():
            raise ValueError(f"Kolonnen `{kol}` i totaltabellen inneholder NaN eller ikke-endelige verdier.")

    roller = oversikt_df["modellrolle"].tolist()
    if sorted(roller) != sorted(MODELLREKKEFOLGE):
        raise ValueError(
            "WBS 5.3 forventer modellrollene "
            f"{MODELLREKKEFOLGE} i totaltabellen, men fant {roller}."
        )

    oversikt_df["modellrekkefolge"] = oversikt_df["modellrolle"].map(modellorden())
    return oversikt_df.sort_values("modellrekkefolge").reset_index(drop=True)


def valider_maanedstabell(maaned_df: pd.DataFrame) -> pd.DataFrame:
    krav = ["år_måned", "month", "modellnavn", "modellrolle", "prediksjonskolonne", "rmse_maaned", "mape_maaned_pct"]
    mangler = [kol for kol in krav if kol not in maaned_df.columns]
    if mangler:
        raise ValueError(f"WBS 5.3 mangler nødvendige kolonner i månedstabellen: {mangler}")

    if len(maaned_df) != FORVENTET_MAANEDSRADER:
        raise ValueError(
            f"WBS 5.3 forventer {FORVENTET_MAANEDSRADER} rader i månedstabellen, men fant {len(maaned_df)}."
        )

    maaned_df = maaned_df.copy()
    maaned_df["month"] = pd.to_numeric(maaned_df["month"], errors="raise").astype(int)
    maaned_df["rmse_maaned"] = pd.to_numeric(maaned_df["rmse_maaned"], errors="raise")
    maaned_df["mape_maaned_pct"] = pd.to_numeric(maaned_df["mape_maaned_pct"], errors="raise")
    for kol in ["rmse_maaned", "mape_maaned_pct"]:
        if maaned_df[kol].isna().any() or not np.isfinite(maaned_df[kol]).all():
            raise ValueError(f"Kolonnen `{kol}` i månedstabellen inneholder NaN eller ikke-endelige verdier.")

    måneder = sorted(maaned_df["år_måned"].unique().tolist())
    if måneder != FORVENTEDE_MAANEDER:
        raise ValueError(
            "WBS 5.3 forventer månedene "
            f"{FORVENTEDE_MAANEDER}, men fant {måneder}."
        )

    per_maaned = maaned_df.groupby("år_måned")["modellrolle"].apply(list)
    for år_måned, roller in per_maaned.items():
        if sorted(roller) != sorted(MODELLREKKEFOLGE):
            raise ValueError(
                f"WBS 5.3 forventer modellrollene {MODELLREKKEFOLGE} for {år_måned}, men fant {roller}."
            )

    maaned_df["modellrekkefolge"] = maaned_df["modellrolle"].map(modellorden())
    return maaned_df.sort_values(["år_måned", "month", "modellrekkefolge"]).reset_index(drop=True)


def lag_maanedlige_vinnere(maaned_df: pd.DataFrame) -> pd.DataFrame:
    rader: list[dict[str, object]] = []

    for år_måned, gruppe in maaned_df.groupby("år_måned", sort=True):
        gruppe = gruppe.sort_values("modellrekkefolge").reset_index(drop=True)
        rmse_vinner = gruppe.sort_values(["rmse_maaned", "mape_maaned_pct", "modellrekkefolge"]).iloc[0]
        mape_vinner = gruppe.sort_values(["mape_maaned_pct", "rmse_maaned", "modellrekkefolge"]).iloc[0]
        rader.append(
            {
                "år_måned": år_måned,
                "month": int(gruppe["month"].iloc[0]),
                "rmse_vinner": rmse_vinner["modellrolle"],
                "rmse_vinner_verdi": round(float(rmse_vinner["rmse_maaned"]), 6),
                "mape_vinner": mape_vinner["modellrolle"],
                "mape_vinner_verdi": round(float(mape_vinner["mape_maaned_pct"]), 4),
                "samme_vinner": bool(rmse_vinner["modellrolle"] == mape_vinner["modellrolle"]),
            }
        )

    return pd.DataFrame(rader)


def lag_modellvinner_telling(vinnere_df: pd.DataFrame) -> pd.DataFrame:
    rader: list[dict[str, object]] = []

    for metric, kolonne in [("RMSE", "rmse_vinner"), ("MAPE", "mape_vinner")]:
        antall_per_modell = vinnere_df[kolonne].value_counts().to_dict()
        for modellrolle in MODELLREKKEFOLGE:
            antall = int(antall_per_modell.get(modellrolle, 0))
            rader.append(
                {
                    "metric": metric,
                    "modellrolle": modellrolle,
                    "antall_vinnermåneder": antall,
                    "andel_vinnermåneder_pct": round((antall / len(vinnere_df)) * 100, 4),
                    "modellrekkefolge": modellorden()[modellrolle],
                    "metric_rekkefolge": 0 if metric == "RMSE" else 1,
                }
            )

    telling_df = pd.DataFrame(rader)
    telling_df = telling_df.sort_values(["metric_rekkefolge", "modellrekkefolge"]).reset_index(drop=True)
    return telling_df.drop(columns=["modellrekkefolge", "metric_rekkefolge"])


def bygg_hovedrangering(oversikt_df: pd.DataFrame, telling_df: pd.DataFrame) -> tuple[pd.DataFrame, list[str]]:
    rmse_telling = telling_df.loc[telling_df["metric"] == "RMSE", ["modellrolle", "antall_vinnermåneder"]]
    rmse_telling = rmse_telling.rename(columns={"antall_vinnermåneder": "rmse_vinnermåneder"})
    sammenligning = oversikt_df.merge(rmse_telling, on="modellrolle", how="left")
    sammenligning["rmse_vinnermåneder"] = sammenligning["rmse_vinnermåneder"].fillna(0).astype(int)

    rangert = sammenligning.sort_values(
        ["rmse_2025", "mape_2025_pct", "rmse_vinnermåneder", "modellrekkefolge"],
        ascending=[True, True, False, True],
    ).reset_index(drop=True)

    vinner = rangert.iloc[0]
    tie_mask = (
        (rangert["rmse_2025"] == vinner["rmse_2025"])
        & (rangert["mape_2025_pct"] == vinner["mape_2025_pct"])
        & (rangert["rmse_vinnermåneder"] == vinner["rmse_vinnermåneder"])
    )
    toppvinnere = rangert.loc[tie_mask, "modellrolle"].tolist()
    return rangert, toppvinnere


def lag_oversikt_med_rangering(
    oversikt_df: pd.DataFrame,
    telling_df: pd.DataFrame,
    hovedrangering_df: pd.DataFrame,
    toppvinnere: list[str],
) -> tuple[pd.DataFrame, str]:
    anbefalt_modell = hovedrangering_df.iloc[0]["modellrolle"]
    benchmarkrad = oversikt_df.loc[oversikt_df["modellrolle"] == "benchmark lineær"].iloc[0]
    anbefaltrad = oversikt_df.loc[oversikt_df["modellrolle"] == anbefalt_modell].iloc[0]

    rmse_telling = telling_df.loc[telling_df["metric"] == "RMSE", ["modellrolle", "antall_vinnermåneder"]]
    rmse_telling = rmse_telling.rename(columns={"antall_vinnermåneder": "rmse_vinnermåneder"})
    oversikt_df = oversikt_df.merge(rmse_telling, on="modellrolle", how="left")
    oversikt_df["rmse_vinnermåneder"] = oversikt_df["rmse_vinnermåneder"].fillna(0).astype(int)

    rmse_ranked = oversikt_df.sort_values(
        ["rmse_2025", "mape_2025_pct", "rmse_vinnermåneder", "modellrekkefolge"],
        ascending=[True, True, False, True],
    )["modellrolle"].tolist()
    mape_ranked = oversikt_df.sort_values(
        ["mape_2025_pct", "rmse_2025", "rmse_vinnermåneder", "modellrekkefolge"],
        ascending=[True, True, False, True],
    )["modellrolle"].tolist()
    rank_rmse = {rolle: indeks for indeks, rolle in enumerate(rmse_ranked, start=1)}
    rank_mape = {rolle: indeks for indeks, rolle in enumerate(mape_ranked, start=1)}

    sorted_roles = hovedrangering_df["modellrolle"].tolist()
    sekundær_modell = None
    for rolle in sorted_roles:
        if rolle not in toppvinnere:
            sekundær_modell = rolle
            break

    vurderinger: list[str] = []
    for rolle in oversikt_df["modellrolle"]:
        if rolle in toppvinnere:
            vurdering = "anbefalt"
        elif sekundær_modell is not None and rolle == sekundær_modell:
            vurdering = "sekundær"
        else:
            vurdering = "ikke anbefalt"
        vurderinger.append(vurdering)

    if not set(vurderinger).issubset(VALID_VURDERINGER):
        raise ValueError("WBS 5.3 genererte en ugyldig samlet vurdering.")

    oversikt_df["rang_rmse_2025"] = oversikt_df["modellrolle"].map(rank_rmse)
    oversikt_df["rang_mape_2025"] = oversikt_df["modellrolle"].map(rank_mape)
    oversikt_df["delta_rmse_mot_benchmark"] = (
        oversikt_df["rmse_2025"] - float(benchmarkrad["rmse_2025"])
    ).round(6)
    oversikt_df["delta_mape_mot_benchmark_pctpoeng"] = (
        oversikt_df["mape_2025_pct"] - float(benchmarkrad["mape_2025_pct"])
    ).round(4)
    oversikt_df["delta_rmse_mot_anbefalt"] = (
        oversikt_df["rmse_2025"] - float(anbefaltrad["rmse_2025"])
    ).round(6)
    oversikt_df["delta_mape_mot_anbefalt_pctpoeng"] = (
        oversikt_df["mape_2025_pct"] - float(anbefaltrad["mape_2025_pct"])
    ).round(4)
    oversikt_df["samlet_vurdering_5_3"] = vurderinger

    return (
        oversikt_df[
            [
                "modellnavn",
                "modellrolle",
                "prediksjonskolonne",
                "rmse_2025",
                "mape_2025_pct",
                "rang_rmse_2025",
                "rang_mape_2025",
                "delta_rmse_mot_benchmark",
                "delta_mape_mot_benchmark_pctpoeng",
                "delta_rmse_mot_anbefalt",
                "delta_mape_mot_anbefalt_pctpoeng",
                "samlet_vurdering_5_3",
            ]
        ].sort_values("modellrolle", key=lambda s: s.map(modellorden())).reset_index(drop=True),
        anbefalt_modell,
    )


def skriv_markdown(
    md_path: Path,
    oversikt_df: pd.DataFrame,
    vinnere_df: pd.DataFrame,
    telling_df: pd.DataFrame,
    anbefalt_modell: str,
    toppvinnere: list[str],
) -> None:
    rangert = oversikt_df.sort_values("rang_rmse_2025").reset_index(drop=True)
    første = rangert.iloc[0]
    andre = rangert.iloc[1]
    tredje = rangert.iloc[2]

    benchmark = oversikt_df.loc[oversikt_df["modellrolle"] == "benchmark lineær"].iloc[0]
    baseline = oversikt_df.loc[oversikt_df["modellrolle"] == "baseline RF"].iloc[0]
    tuned = oversikt_df.loc[oversikt_df["modellrolle"] == "tuned RF"].iloc[0]
    sprikmaaneder = vinnere_df.loc[~vinnere_df["samme_vinner"], "år_måned"].tolist()

    tell_rader = telling_df.copy()
    tell_rader["andel_vinnermåneder_pct"] = tell_rader["andel_vinnermåneder_pct"].map(lambda v: f"{float(v):.4f}")
    rmse_telling = tell_rader.loc[tell_rader["metric"] == "RMSE", ["modellrolle", "antall_vinnermåneder"]]
    mape_telling = tell_rader.loc[tell_rader["metric"] == "MAPE", ["modellrolle", "antall_vinnermåneder"]]

    if len(toppvinnere) > 1:
        anbefalingstekst = (
            "WBS 5.3 finner delt førsteplass etter sammenligningsregelen. "
            f"Delte vinnere: {', '.join(f'`{rolle}`' for rolle in toppvinnere)}."
        )
    else:
        anbefalingstekst = (
            f"WBS 5.3 anbefaler `{anbefalt_modell}` som samlet modell for videre analyse, "
            "fordi modellen er best på total `RMSE` og samtidig også best på total `MAPE`."
        )

    lines = [
        "# Sammenligning av modellresultater (WBS 5.3)",
        "",
        "## Hva WBS 5.3 gjør",
        "",
        "- Aktiviteten sammenligner modellresultatene fra WBS 5.2 uten å trene modeller på nytt eller beregne nye prognoser.",
        "- Samlet `RMSE` for hele 2025 brukes som hovedregel, mens samlet `MAPE` brukes som sekundær regel ved lik `RMSE`.",
        "- Månedlige vinnere brukes som støtteforklaring for å vise hvor stabil modellen er gjennom året.",
        "",
        "## Samlet anbefaling",
        "",
        f"- {anbefalingstekst}",
        f"- Rang 1 samlet: `{første['modellrolle']}` (`RMSE={float(første['rmse_2025']):.6f}`, `MAPE={float(første['mape_2025_pct']):.4f} %`)",
        f"- Rang 2 samlet: `{andre['modellrolle']}` (`RMSE={float(andre['rmse_2025']):.6f}`, `MAPE={float(andre['mape_2025_pct']):.4f} %`)",
        f"- Rang 3 samlet: `{tredje['modellrolle']}` (`RMSE={float(tredje['rmse_2025']):.6f}`, `MAPE={float(tredje['mape_2025_pct']):.4f} %`)",
        "",
        "## Viktigste deltaer",
        "",
        (
            f"- `tuned RF` mot `benchmark lineær`: "
            f"`delta RMSE={float(tuned['delta_rmse_mot_benchmark']):.6f}` og "
            f"`delta MAPE={float(tuned['delta_mape_mot_benchmark_pctpoeng']):.4f}` prosentpoeng."
        ),
        (
            f"- `baseline RF` mot `benchmark lineær`: "
            f"`delta RMSE={float(baseline['delta_rmse_mot_benchmark']):.6f}` og "
            f"`delta MAPE={float(baseline['delta_mape_mot_benchmark_pctpoeng']):.4f}` prosentpoeng."
        ),
        (
            f"- `tuned RF` mot `baseline RF`: "
            f"`delta RMSE={float(tuned['delta_rmse_mot_anbefalt'] - baseline['delta_rmse_mot_anbefalt']):.6f}` og "
            f"`delta MAPE={float(tuned['delta_mape_mot_anbefalt_pctpoeng'] - baseline['delta_mape_mot_anbefalt_pctpoeng']):.4f}` prosentpoeng."
        ),
        "",
        "## Månedsbilde",
        "",
        f"- Samme vinner på `RMSE` og `MAPE` forekommer i `{int(vinnere_df['samme_vinner'].sum())}` av `{len(vinnere_df)}` måneder.",
        f"- Måneder med metrikk-sprik: {', '.join(f'`{måned}`' for måned in sprikmaaneder)}.",
        "",
        "### Vinnermåneder per metrikk",
        "",
        *[
            f"- `RMSE`: `{rad.modellrolle}` vinner `{int(rad.antall_vinnermåneder)}` måneder."
            for rad in rmse_telling.itertuples(index=False)
        ],
        *[
            f"- `MAPE`: `{rad.modellrolle}` vinner `{int(rad.antall_vinnermåneder)}` måneder."
            for rad in mape_telling.itertuples(index=False)
        ],
        "",
        "## Produserte artefakter",
        "",
        "- `tab_modellsammenligning_oversikt.csv`",
        "- `tab_maanedlige_modellvinnere.csv`",
        "- `tab_modellvinner_telling.csv`",
        "- `modellsammenligning.md`",
        "",
        "## Avgrensning mot senere WBS-steg",
        "",
        "- WBS 5.3 sammenligner modeller, men går ikke inn i variabeltolkning, residualdiagnostikk eller årsaksforklaring.",
        "- WBS 5.4 og WBS 6.x tar videre arbeid med viktige variabler, faglig tolkning og diskusjon.",
        "",
    ]
    md_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    aktivitetsmappe = Path(__file__).resolve().parent
    repo_aktiviteter = Path(__file__).resolve().parents[1]

    oversikt_df = les_dataset(repo_aktiviteter / INPUT_OVERSIKT)
    maaned_df = les_dataset(repo_aktiviteter / INPUT_MAANED)

    oversikt_df = valider_oversikt(oversikt_df)
    maaned_df = valider_maanedstabell(maaned_df)

    vinnere_df = lag_maanedlige_vinnere(maaned_df)
    telling_df = lag_modellvinner_telling(vinnere_df)
    hovedrangering_df, toppvinnere = bygg_hovedrangering(oversikt_df, telling_df)
    sammenligning_df, anbefalt_modell = lag_oversikt_med_rangering(
        oversikt_df,
        telling_df,
        hovedrangering_df,
        toppvinnere,
    )

    oversikt_path = aktivitetsmappe / "tab_modellsammenligning_oversikt.csv"
    vinnere_path = aktivitetsmappe / "tab_maanedlige_modellvinnere.csv"
    telling_path = aktivitetsmappe / "tab_modellvinner_telling.csv"
    markdown_path = aktivitetsmappe / "modellsammenligning.md"

    oversikt_path.write_text(sammenligning_df.to_csv(index=False), encoding="utf-8")
    vinnere_path.write_text(vinnere_df.to_csv(index=False), encoding="utf-8")
    telling_path.write_text(telling_df.to_csv(index=False), encoding="utf-8")
    skriv_markdown(markdown_path, sammenligning_df, vinnere_df, telling_df, anbefalt_modell, toppvinnere)

    print("WBS 5.3 ferdig: modellresultater sammenlignet")
    print(f"- Anbefalt modell: {anbefalt_modell}")
    print(f"- Måneder med metrikk-sprik: {int((~vinnere_df['samme_vinner']).sum())}")
    print(f"- {oversikt_path.name}")
    print(f"- {vinnere_path.name}")
    print(f"- {telling_path.name}")
    print(f"- {markdown_path.name}")


if __name__ == "__main__":
    main()
