"""Compare WHO Defined Daily Doses: J01 antibacterials vs comparator classes.

Source: WHO Collaborating Centre for Drug Statistics Methodology,
ATC Classification Index with DDDs, https://atcddd.fhi.no/atc_ddd_index/
Snapshot used here: fabkury/atcd, "WHO ATC-DDD 2026-04-25.csv".
"""

import pandas as pd
from scipy import stats

TO_MG = {"g": 1000.0, "mg": 1.0, "mcg": 0.001}

GROUPS = {
    "J01 antibacterials": lambda c: c.str.startswith("J01"),
    "C  cardiovascular":  lambda c: c.str.startswith("C"),
    "N  nervous system":  lambda c: c.str.startswith("N"),
    "L  antineoplastic":  lambda c: c.str.startswith("L"),
}


def load(path="./WHO ATC-DDD 2026-04-25.csv"):
    df = pd.read_csv(path, na_values=["NA"])
    df = df[df.atc_code.str.len() == 7]                 # level-5 substances
    df = df[(df.adm_r == "O") & df.ddd.notna()]         # oral, DDD assigned
    df = df[df.uom.isin(TO_MG)]                         # mass-convertible only
    df["ddd_mg"] = df.ddd * df.uom.map(TO_MG)
    return df


def summarise(df):
    rows = []
    for name, mask in GROUPS.items():
        g = df[mask(df.atc_code)]
        rows.append({
            "group": name, "n": len(g),
            "median_mg": g.ddd_mg.median(),
            "iqr_lo": g.ddd_mg.quantile(0.25),
            "iqr_hi": g.ddd_mg.quantile(0.75),
            "gmean_mg": stats.gmean(g.ddd_mg),
            "min_mg": g.ddd_mg.min(), "max_mg": g.ddd_mg.max(),
        })
    return pd.DataFrame(rows)


def main():
    df = load()
    print(f"oral level-5 codes with a mass-unit DDD: {len(df)}\n")
    s = summarise(df)
    print(s.to_string(index=False, float_format=lambda v: f"{v:,.2f}"))

if __name__ == "__main__":
    main()