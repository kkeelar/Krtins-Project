import numpy as np
import pandas as pd

def softmax(x):
    """Numerically stable softmax"""
    x = np.asarray(x)
    e_x = np.exp(x - np.max(x, axis=1, keepdims=True))
    return e_x / e_x.sum(axis=1, keepdims=True)

def calc_pregame_probs(df):
    """
    Pregame prediction of P(Home win), P(Draw), P(Away win).
    Outputs columns: hProb, dProb, aProb
    """
    # Features from last year + team status
    X = pd.DataFrame({
        "HGpm_LY": df["HG_LY"] / df["HM_LY"],
        "AGpm_LY": df["AG_LY"] / df["AM_LY"],
        "HGApm_LY": df["HGA_LY"] / df["HM_LY"],
        "AGApm_LY": df["AGA_LY"] / df["AM_LY"],
        "Hrelegated": df["Hrelegated"],
        "Arelegated": df["Arelegated"],
        "Hpromoted": df["Hpromoted"],
        "Apromoted": df["Apromoted"]
    }).fillna(0)

    # Means & scales (from StandardScaler training)
    means = np.array([1.35976738, 1.35976738, 1.27786611, 1.27786611, 0., 0., 0., 0.])
    scales = np.array([0.38759675, 0.38759675, 0.29677894, 0.29677894, 1., 1., 1., 1.])

    # Normalize
    X_std = (X - means) / scales

    # Logistic regression coefficients & intercepts
    coeffs = np.array([
        [ 0.23668719, -0.16974876, -0.14097577,  0.13418577,  0., 0., 0., 0.],  # Home win
        [-0.04495236, -0.0425516 , -0.00664643, -0.00911919,  0., 0., 0., 0.],  # Draw
        [-0.19173483,  0.21230036,  0.14762221, -0.12506658,  0., 0., 0., 0.]   # Away win
    ])
    intercepts = np.array([ 0.33273514, -0.15180361, -0.18093153 ])

    # Linear predictor
    logits = (X_std @ coeffs.T + intercepts).to_numpy()

    # Convert to probabilities
    probs = softmax(logits)
    df["hProb"], df["dProb"], df["aProb"] = probs[:,0], probs[:,1], probs[:,2]
    return df

def calc_halftime_probs(df):
    """
    Halftime prediction of P(Home win), P(Draw), P(Away win).
    Outputs columns: hProbHT, dProbHT, aProbHT
    """
    # Features from last year + halftime goals + team status
    X = pd.DataFrame({
        "HGpm_LY": df["HG_LY"] / df["HM_LY"],
        "AGpm_LY": df["AG_LY"] / df["AM_LY"],
        "HGApm_LY": df["HGA_LY"] / df["HM_LY"],
        "AGApm_LY": df["AGA_LY"] / df["AM_LY"],
        "Hgoals1H": df["Hgoals1H"],
        "Agoals1H": df["Agoals1H"],
        "Hrelegated": df["Hrelegated"],
        "Arelegated": df["Arelegated"],
        "Hpromoted": df["Hpromoted"],
        "Apromoted": df["Apromoted"]
    }).fillna(0)

    # Means & scales
    means = np.array([1.35976738, 1.35976738, 1.27786611, 1.27786611, 
                      0.66408935, 0.49849656, 0., 0., 0., 0.])
    scales = np.array([0.38759675, 0.38759675, 0.29677894, 0.29677894, 
                       0.8151323, 0.71420742, 1., 1., 1., 1.])

    # Normalize
    X_std = (X - means) / scales

    # Coefficients & intercepts
    coeffs = np.array([
        [ 0.19497094, -0.15102268, -0.12523146,  0.10308809,  0.87939567,
         -0.71070504,  0., 0., 0., 0.],   # Home win
        [-0.02675711, -0.03152584, -0.0066285 ,  0.00626413, -0.08203648,
         -0.04519634,  0., 0., 0., 0.],   # Draw
        [-0.16821382,  0.18254852,  0.13185996, -0.10935222, -0.79735919,
          0.75590139,  0., 0., 0., 0.]    # Away win
    ])
    intercepts = np.array([ 0.35656914,  0.06203921, -0.41860835 ])

    # Linear predictor
    logits = (X_std @ coeffs.T + intercepts).to_numpy()

    # Convert to probabilities
    probs = softmax(logits)
    df["hProbHT"], df["dProbHT"], df["aProbHT"] = probs[:,0], probs[:,1], probs[:,2]
    return df

def calc_pred_goals(df):
    """
    Pregame prediction of total goals in the 2nd half.
    Outputs column: predGoals2H
    """
    # Features from last year + team status
    X = pd.DataFrame({
        "HGpm_LY": df["HG_LY"] / df["HM_LY"],
        "AGpm_LY": df["AG_LY"] / df["AM_LY"],
        "HGApm_LY": df["HGA_LY"] / df["HM_LY"],
        "AGApm_LY": df["AGA_LY"] / df["AM_LY"],
        "Hrelegated": df["Hrelegated"],
        "Arelegated": df["Arelegated"],
        "Hpromoted": df["Hpromoted"],
        "Apromoted": df["Apromoted"]
    }).fillna(0)

    # Linear regression coefficients & intercept
    coeffs = np.array([0.29155089, 0.13234765, 0.0395288 , 0.17062179,
                       0., 0., 0., 0.])
    intercept = 0.6523675527358783

    # Prediction
    preds = X.to_numpy() @ coeffs + intercept
    df["predGoals2H"] = preds
    return df

def main():
    # Load test dataset
    df = pd.read_csv("soccermatches.csv")
    
    # Apply models
    df = calc_pregame_probs(df)
    df = calc_halftime_probs(df)
    df = calc_pred_goals(df)
    
    # Save output
    output_file = "kkeelar_output.csv"
    df.to_csv(output_file, index=False)
    print(f"Submission saved to {output_file}")

if __name__ == "__main__":
    main()

