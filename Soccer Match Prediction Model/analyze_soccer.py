import pandas as pd

def analyze_soccer_data(csv_path="soccermatches.csv"):
    # Load dataset
    df = pd.read_csv(csv_path)

    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print(df.head())

    # Outcome distributions
    outcome_dist = {
        "Home Wins %": df["Hwins"].mean(),
        "Away Wins %": df["Awins"].mean(),
        "Draw %": df["IsDraw"].mean(),
        "Avg Goals per Match": (df["Hgoals"] + df["Agoals"]).mean(),
        "Avg Goals 1H": (df["Hgoals1H"] + df["Agoals1H"]).mean(),
        "Avg Goals 2H": df["goals2H"].mean()
    }

    print("\n--- Outcome Distributions ---")
    for k, v in outcome_dist.items():
        print(f"{k}: {v:.3f}")

    # Create per-match stats for last year
    df["HGpm_LY"] = df["HG_LY"] / df["HM_LY"]
    df["AGpm_LY"] = df["AG_LY"] / df["AM_LY"]
    df["HGApm_LY"] = df["HGA_LY"] / df["HM_LY"]
    df["AGApm_LY"] = df["AGA_LY"] / df["AM_LY"]

    # Correlation matrix
    corr = df[[
        "HGpm_LY", "AGpm_LY", "HGApm_LY", "AGApm_LY",
        "Hwins", "Awins", "IsDraw", "goals2H"
    ]].corr()

    print("\n--- Correlations ---")
    print(corr.round(3))

    return outcome_dist, corr


if __name__ == "__main__":
    analyze_soccer_data()



    
