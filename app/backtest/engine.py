import pandas as pd


def run_backtest(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["position_shifted"] = df["position"].shift(1)
    df["strategy_returns"] = df["position_shifted"] * df["returns"]

    df["strategy_returns"] = df["strategy_returns"].fillna(0)

    df["equity_curve"] = (1 + df["strategy_returns"]).cumprod()

    return df