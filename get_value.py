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
import binance
import config
import csv
def get_value_binace(crypto_currency, currency):
    """Returns the current value of the crypto currency."""
    print("get_value_binace")
    binance_client = binance.client.Client(config.binance_api_key, config.binance_api_secret)
    coin_price = binance_client.get_symbol_ticker(symbol=f"{crypto_currency}{currency}")
    breakpoint()
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
    print("get_value_coinbase")
    url = f"https://api.pro.coinbase.com/products/{crypto_currency}-{currency}/candles?granularity={interval}&limit={limit}"
    response = requests.get(url)
    json = response.json()
    breakpoint()
    df = pd.DataFrame(json)
    df = df.iloc[:, 0:6]
    col_names = ["time", "low", "high", "open", "close", "volume"]
    df.columns = col_names
    df["time"] = pd.to_datetime(df["time"], unit="s")
    df["close"] = df["close"].astype(float)
    df["volume"] = df["volume"].astype(float)
    df["open"] = df["open"].astype(float)

    return df

def get_keys_kraken():
    """Return the pair names for kraken."""
    print("get pair names for kraken")
    pairs_url = f"https://api.kraken.com/0/public/AssetPairs"
    pairs_response = requests.get(pairs_url)
    pairs_data = pairs_response.json()
    pairs_data = pairs_data["result"]

    # extract the pair names
    pairs_names = [pair for pair in pairs_data.keys()]
    return pairs_names

def get_live_data_kraken(pairs_names: list):
    """Given a list of pair names, return the current price for each pair from the api. save the data to a csv file."""
    current_prices = {}
    for pair_name in pairs_names:
        # get the current price for the pair
        ticker_url = f"https://api.kraken.com/0/public/Ticker?pair={pair_name}"
        ticker_response = requests.get(ticker_url)
        ticker_data = ticker_response.json()
        pair_key = list(ticker_data["result"].keys())[0]

        current_price = ticker_data["result"][pair_key]["c"][0]
        current_prices[pair_name] = current_price

def get_history_data_kraken(cyptos: list):
    """Given a list of pair names, return the data for each pair from the api. Save the data to a csv file."""
    for cypto in cyptos:
        # get the historical data for the pair over a given time period
        historical_url = f"https://api.kraken.com/0/public/OHLC?pair={cypto['kraken_id']}&interval={config.kraken_history_interval}"
        historical_response = requests.get(historical_url)
        historical_data = historical_response.json()
        pair_key = list(historical_data["result"].keys())[0]

        historical_data = historical_data["result"][pair_key]
        historical_data = pd.DataFrame(historical_data)
        historical_data.columns = ["time", "open", "high", "low", "close", "vwap", "volume", "count"]
        historical_data["time"] = pd.to_datetime(historical_data["time"], unit="s")

        # save the data to a csv file in the log folder
        historical_data.to_csv(f"logs/{cypto['symbol']}.csv", index=False)


def plot_graph(coin_name):
    """Plot the graph of the crypto currency from the csv file."""
    # read the csv as a dictionary
    csv_file = f"logs/{coin_name}.csv"
    df = pd.read_csv(csv_file)
    # convert the time to a datetime object
    #df["time"] = pd.to_datetime(df["time"], unit="s")
    #df["high"] = df["high"].astype(float)
    #df["low"] = df["low"].astype(float)
    #df["open"] = df["open"].astype(float)
    #df["close"] = df["close"].astype(float)

    # plot the graph
    fig, ax = plt.subplots()
    ax.plot(df["time"], df["high"], label="high")
    ax.plot(df["time"], df["low"], label="low")
    ax.plot(df["time"], df["open"], label="open")
    ax.plot(df["time"], df["close"], label="close")
    ax.set_xlabel("time")
    ax.set_ylabel("price")

    # format the x axis
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d-%m-%Y"))
    fig.autofmt_xdate()

    # add the legend
    ax.legend()

    # save the graph
    fig.savefig(f"{csv_file}.png")


def get_combined_results(cypto_currenty, currency, interval, limit):
    """Returns the current value of the crypto currency."""
    #df_binance = get_value_binace(cypto_currenty, currency)
    #df_coinbase = get_value_coinbase(cypto_currenty, currency, interval, limit)
    df_kraken = get_data_kraken(pairs_names)
    #df = pd.concat([df_binance, df_kraken])
    #df = df.drop_duplicates(subset=["time"])
    #df = df.sort_values(by=["time"])
    #df = df.reset_index(drop=True)
    #return df

