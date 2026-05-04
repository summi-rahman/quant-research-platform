import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["returns"] = df["Close"].pct_change()
    df["volatility"] = df["returns"].rolling(20).std()

    df = df.dropna()

    return df