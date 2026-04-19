# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

`open_trader` pulls recent Binance candles, runs a simple SMA-crossover strategy, optionally asks OpenAI for a one-line takeaway, and posts the result to a Discord webhook. It's intentionally small — five short files — and is meant to be run on a schedule (cron, GitHub Actions, etc.), not as a long-running process.

## Pipeline

`main.py` wires everything together in one pass:

```
get_value.get_candles  →  strategy.signal  →  open_ai_client.commentary (optional)  →  output_to_discord.send
```

Each step is one function in its own file. Keep it that way — if you're tempted to add a class, a framework, or an event loop, the answer is almost certainly "don't." New exchanges, strategies, or output channels should be siblings of the existing functions, not abstractions over them.

## Running It

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # fill in DISCORD_WEBHOOK_URL; OPENAI_API_KEY optional
set -a && source .env && set +a
python main.py
```

Run from the repo root — the modules import each other by bare name (flat layout, no package).

## Configuration

All runtime config is via environment variables, read in `main.py` and `open_ai_client.py`/`output_to_discord.py`:

- `DISCORD_WEBHOOK_URL` — **required**. A Discord channel webhook (not a bot token). `output_to_discord.send` raises `KeyError` if unset, which is intentional — fail loud.
- `OPENAI_API_KEY` — optional. If unset, `open_ai_client.commentary` returns `None` and the commentary line is skipped. Do not add a fallback model or silent retry here.
- `SYMBOL`, `INTERVAL` — optional; default `BTCUSDT` / `1h`. Must be valid Binance values.

There is no config file and no CLI parser. Keep it that way unless the option count grows past what env vars can reasonably handle.

## Conventions

- **Flat layout.** All modules sit at the repo root. Don't move them into a `src/` package without also rewriting every import site.
- **DataFrame in, scalar/string out.** `get_candles` returns a pandas DataFrame with columns `open_time, open, high, low, close, volume` (all floats except `open_time`). Downstream functions consume that shape and return primitives (`str` for signal, `str | None` for commentary). New strategies should follow the same contract.
- **Module-level docstring first, stdlib imports before third-party.** Every file opens with a one-line `"""..."""` docstring.
- **Let exceptions surface.** The HTTP calls use `raise_for_status` and fixed timeouts; don't wrap them in broad `try/except`. A loud failure in a scheduled job is easier to debug than a silent skip.

## Dependencies

`requirements.txt` is the source of truth — three packages (`requests`, `pandas`, `openai`). If you add an import, add it there in the same change. Notably **not** used: `numpy` (pandas is enough), `matplotlib` (no plotting), `discord.py` (webhooks are plain HTTP POSTs).

## History Note

A previous revision of `output_to_discord.py` contained a hardcoded Discord **bot** token (now removed in favor of a webhook URL). That token is still in git history — treat it as compromised and rotate it in the Discord developer portal if it hasn't been already.
