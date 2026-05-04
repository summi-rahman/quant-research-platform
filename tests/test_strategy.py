from app.data.ingest import fetch_market_data
from app.data.preprocess import clean_data
from app.features.feature_engineering import generate_features
from app.strategies.volatility import VolatilityStrategy
from app.strategies.mean_reversion import MeanReversionStrategy


def prepare_data():
    df = fetch_market_data()
    df = clean_data(df)
    df = generate_features(df)
    return df


def test_volatility_strategy():
    df = prepare_data()

    strategy = VolatilityStrategy()
    df = strategy.generate_signals(df)

    assert "position" in df.columns


def test_mean_reversion_strategy():
    df = prepare_data()

    strategy = MeanReversionStrategy()
    df = strategy.generate_signals(df)

    assert "position" in df.columns