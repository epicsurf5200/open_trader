"""Fetch candles, compute a signal, and post the result to Discord."""
import os

import get_value
import open_ai_client
import output_to_discord
import strategy


def main() -> None:
    symbol = os.getenv("SYMBOL", "BTCUSDT")
    interval = os.getenv("INTERVAL", "1h")

    df = get_value.get_candles(symbol=symbol, interval=interval, limit=100)
    action = strategy.signal(df)
    last_price = float(df["close"].iloc[-1])

    lines = [f"**{symbol}** [{interval}] — signal: `{action}` — last close: {last_price}"]
    note = open_ai_client.commentary(symbol, action, last_price)
    if note:
        lines.append(note)

    output_to_discord.send("\n".join(lines))


if __name__ == "__main__":
    main()
