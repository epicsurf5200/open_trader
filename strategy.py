"""Simple moving-average crossover signal."""
import pandas as pd


def signal(df: pd.DataFrame, fast: int = 10, slow: int = 30) -> str:
    """Return 'buy', 'sell', or 'hold' based on fast/slow SMA crossover of `close`."""
    if len(df) < slow + 1:
        return "hold"
    fast_ma = df["close"].rolling(fast).mean()
    slow_ma = df["close"].rolling(slow).mean()
    if fast_ma.iloc[-2] <= slow_ma.iloc[-2] and fast_ma.iloc[-1] > slow_ma.iloc[-1]:
        return "buy"
    if fast_ma.iloc[-2] >= slow_ma.iloc[-2] and fast_ma.iloc[-1] < slow_ma.iloc[-1]:
        return "sell"
    return "hold"
