# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Status

`open_trader` is an **early-stage scaffold** for a crypto trading bot. Most modules are skeletons or contain partial/broken code — assume nothing works end-to-end until proven otherwise. The README is a single line and there is no dependency manifest (`requirements.txt`, `pyproject.toml`, `Pipfile`, etc.), no test suite, no lint/format config, and no CI.

When asked to extend functionality, prefer **finishing the existing skeletons** over adding new modules.

## Module Map

Four top-level Python files, each a single responsibility:

- `get_value.py` — Market data fetchers. `get_value_binace` (Binance), `get_value_coinbase` (Coinbase Pro), `get_value_kraken` (Kraken) each call the public klines/OHLC REST endpoint and return a pandas `DataFrame` of OHLCV candles. Also `plot_graph(df, ...)` using matplotlib. Note column-order differs per exchange (Coinbase returns `low, high, open, close`; Binance/Kraken return `open, high, low, close`) — callers cannot assume a uniform schema.
- `strategy.py` — Intended home for pattern detection / signal logic. **Currently does not parse**: line 18 uses `object bullish_pattern:` where Python requires `class`. Imports `get_value` as a sibling module (flat layout, no package). Any change here must first fix the syntax error or the file can't be imported.
- `open_ai_client.py` — Intended wrapper around the OpenAI API for interpreting market data. Currently only import statements, no functions.
- `output_to_discord.py` — Discord bot entrypoint (`run_discord_bot`) that listens for messages and replies via `send_message`. `send_message` calls `responses.handle_response(...)` but `responses` is never imported/defined — this will raise `NameError` at runtime. The file also contains a **hardcoded Discord bot token** (line 15); treat it as compromised and move to an environment variable (e.g. `DISCORD_TOKEN`) before doing anything else here.

There is no `main.py` or orchestrator wiring these together yet — the implied flow is `get_value → strategy → open_ai_client → output_to_discord`.

## Running Things

No package manifest exists, so install third-party deps ad-hoc into a venv:

```bash
python -m venv venv && source venv/bin/activate
pip install requests pandas numpy matplotlib openai discord.py
```

If you add new imports, also add a `requirements.txt` (or `pyproject.toml`) in the same change — dependency drift is the main risk in this repo.

Files are run directly (`python get_value.py`) since there is no package structure. Imports like `import get_value` in `strategy.py` rely on the repo root being on `sys.path`, which means scripts must be run from the repo root.

## Conventions Worth Preserving

- **Flat module layout.** All files sit at the repo root and import each other by bare module name. Don't introduce a `src/` package without also updating the imports in `strategy.py`.
- **DataFrame-first.** Market data moves between modules as pandas DataFrames, not dicts or dataclasses. New fetchers/strategies should match that shape.
- **Module-level docstring + stdlib-before-third-party imports.** Every existing file opens with a one-line `"""docstring"""` and then imports; keep that pattern.

## Known Issues to Watch For

Any task touching these files should account for the pre-existing breakage rather than assuming the file is runnable:

1. `strategy.py:18` — invalid `object` keyword, won't import.
2. `output_to_discord.py:9` — undefined `responses` symbol.
3. `output_to_discord.py:15` — hardcoded secret; rotate and externalize.
4. `open_ai_client.py` — empty module; functions need to be written from scratch.
