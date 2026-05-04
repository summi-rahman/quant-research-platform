import numpy as np


def calculate_metrics(df):
    returns = df["strategy_returns"]

    sharpe = 0 if returns.std() == 0 else (returns.mean() / returns.std()) * np.sqrt(252)

    cumulative_return = df["equity_curve"].iloc[-1] - 1

    max_drawdown = (df["equity_curve"] / df["equity_curve"].cummax() - 1).min()

    return {
        "Sharpe Ratio": float(sharpe),
        "Cumulative Return": float(cumulative_return),
        "Max Drawdown": float(max_drawdown)
    }