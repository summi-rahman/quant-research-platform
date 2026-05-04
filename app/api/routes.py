from fastapi import APIRouter

from app.data.ingest import fetch_market_data
from app.data.preprocess import clean_data
from app.features.feature_engineering import generate_features
from app.strategies.volatility import VolatilityStrategy
from app.strategies.mean_reversion import MeanReversionStrategy
from app.backtest.engine import run_backtest
from app.backtest.metrics import calculate_metrics

router = APIRouter()


@router.get("/run-strategy")
def run_strategy():
    try:
        df = fetch_market_data()
        df = clean_data(df)
        df = generate_features(df)

        # Volatility
        vol = VolatilityStrategy()
        df_vol = run_backtest(vol.generate_signals(df.copy()))
        metrics_vol = calculate_metrics(df_vol)

        # Mean Reversion
        mr = MeanReversionStrategy()
        df_mr = run_backtest(mr.generate_signals(df.copy()))
        metrics_mr = calculate_metrics(df_mr)

        return {
            "volatility_strategy": {
                "metrics": metrics_vol,
                "equity_curve": df_vol["equity_curve"].tolist()
            },
            "mean_reversion_strategy": {
                "metrics": metrics_mr,
                "equity_curve": df_mr["equity_curve"].tolist()
            },
            "market": df["Close"].tolist()
        }

    except Exception as e:
        return {"error": str(e)}