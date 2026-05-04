import yfinance as yf
import pandas as pd
from app.core.config import settings
from app.data.storage import save_data, load_data


def fetch_market_data(
    ticker: str = settings.DEFAULT_TICKER,
    start: str = settings.START_DATE,
    interval: str = settings.INTERVAL
) -> pd.DataFrame:

    # 🔥 Try loading from DB first
    df = load_data()
    if df is not None and not df.empty:
        return df

    # 🔥 Otherwise fetch from API
    df = yf.download(
        ticker,
        start=start,
        interval=interval,
        progress=False
    )

    if df is None or df.empty:
        raise ValueError("No data fetched from yfinance")

    # Handle MultiIndex
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df.columns = [str(col).capitalize() for col in df.columns]

    if "Close" not in df.columns:
        raise ValueError("Close column missing")

    df.reset_index(inplace=True)
    df["ticker"] = ticker

    # 🔥 Save to DB
    save_data(df)

    return df