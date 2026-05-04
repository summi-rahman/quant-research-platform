from app.data.ingest import fetch_market_data
from app.data.preprocess import clean_data
from app.features.feature_engineering import generate_features


def test_full_pipeline():
    # Step 1: Fetch
    df = fetch_market_data()

    assert df is not None
    assert not df.empty
    assert "Close" in df.columns

    # Step 2: Preprocess
    df = clean_data(df)
    assert "returns" in df.columns
    assert "volatility" in df.columns

    # Step 3: Features
    df = generate_features(df)
    assert "ma_20" in df.columns
    assert "ma_50" in df.columns