def generate_features(df):
    df = df.copy()

    df["ma_20"] = df["Close"].rolling(20).mean()
    df["ma_50"] = df["Close"].rolling(50).mean()

    df["momentum"] = df["Close"] - df["Close"].shift(10)

    df["trend_signal"] = (df["ma_20"] > df["ma_50"]).astype(int)

    df = df.dropna()

    return df