from app.strategies.base import Strategy


class VolatilityStrategy(Strategy):
    def generate_signals(self, df):
        df = df.copy()

        df["position"] = 0

        df.loc[
            (df["volatility"] > df["volatility"].mean()) &
            (df["trend_signal"] == 1),
            "position"
        ] = 1

        return df