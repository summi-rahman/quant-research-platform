from app.strategies.base import Strategy


class MeanReversionStrategy(Strategy):
    def generate_signals(self, df):
        df = df.copy()

        df["position"] = 0

        df.loc[df["Close"] < df["ma_20"], "position"] = 1

        return df