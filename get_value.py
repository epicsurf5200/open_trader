"""Fetch OHLCV candles from Binance's public API."""
import pandas as pd
import requests

BINANCE_URL = "https://api.binance.com/api/v3/klines"


def get_candles(symbol: str = "BTCUSDT", interval: str = "1h", limit: int = 100) -> pd.DataFrame:
    """Return a DataFrame of OHLCV candles for `symbol` (e.g. BTCUSDT)."""
    response = requests.get(
        BINANCE_URL,
        params={"symbol": symbol, "interval": interval, "limit": limit},
        timeout=10,
    )
    response.raise_for_status()
    rows = response.json()
    df = pd.DataFrame(
        rows,
        columns=[
            "open_time", "open", "high", "low", "close", "volume",
            "close_time", "quote_volume", "trades",
            "taker_base", "taker_quote", "ignore",
        ],
    )
    df = df[["open_time", "open", "high", "low", "close", "volume"]].copy()
    df["open_time"] = pd.to_datetime(df["open_time"], unit="ms")
    for col in ("open", "high", "low", "close", "volume"):
        df[col] = df[col].astype(float)
    return df
