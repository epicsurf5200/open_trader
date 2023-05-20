"""get the current value for the cypto currency"""
import requests
import json
import os
import pandas as pd
import numpy as np
import datetime
import time
import math
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def get_value_binace(crypto_currency, currency, interval, limit):
    """Returns the current value of the crypto currency."""
    url = f"https://api.binance.com/api/v3/klines?symbol={crypto_currency}{currency}&interval={interval}&limit={limit}"
    response = requests.get(url)
    json = response.json()
    df = pd.DataFrame(json)
    df = df.iloc[:, 0:6]
    col_names = ["time", "open", "high", "low", "close", "volume"]
    df.columns = col_names
    df["time"] = pd.to_datetime(df["time"], unit="ms")
    df["close"] = df["close"].astype(float)
    df["volume"] = df["volume"].astype(float)
    df["open"] = df["open"].astype(float)

    return df

def get_value_coinbase(crypto_currency, currency, interval, limit):
    """Returns the current value of the crypto currency."""
    url = f"https://api.pro.coinbase.com/products/{crypto_currency}-{currency}/candles?granularity={interval}&limit={limit}"
    response = requests.get(url)
    json = response.json()
    df = pd.DataFrame(json)
    df = df.iloc[:, 0:6]
    col_names = ["time", "low", "high", "open", "close", "volume"]
    df.columns = col_names
    df["time"] = pd.to_datetime(df["time"], unit="s")
    df["close"] = df["close"].astype(float)
    df["volume"] = df["volume"].astype(float)
    df["open"] = df["open"].astype(float)

    return df

def get_value_kraken(crypto_currency, currency, interval, limit):
    """Returns the current value of the crypto currency."""
    url = f"https://api.kraken.com/0/public/OHLC?pair={crypto_currency}{currency}&interval={interval}&since={limit}"
    response = requests.get(url)
    json = response.json()
    df = pd.DataFrame(json["result"][f"{crypto_currency}{currency}"])
    col_names = ["time", "open", "high", "low", "close", "volume", "vwap", "count"]
    df.columns = col_names
    df["time"] = pd.to_datetime(df["time"], unit="s")
    df["close"] = df["close"].astype(float)
    df["volume"] = df["volume"].astype(float)
    df["open"] = df["open"].astype(float)

    return df

def plot_graph(df, crypto_currency, currency):
    """Plots a graph of the crypto currency."""
    plt.plot(df["time"], df["close"])
    plt.xlabel("Date")
    plt.ylabel(f"{crypto_currency} price in {currency}")
    plt.title(f"{crypto_currency} price over time")
    plt.show()
