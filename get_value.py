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

def get_value_coinbase(cypto_name, symbol, coinbase_id):
    """Return the current value in USD for the coin on coinbase."""
    print(f"accessing kraken api for {cypto_name}")
    value = 420
    return value

def get_value_binance(cypto_name, symbol, binance_id):
    """Return the current value in USD for the coin on binance."""
    print(f"accessing kraken api for {cypto_name}")
    value = 69420
    return value

def get_value_kraken(cypto_name, symbol, kraken_id):
    """Return the current value in USD for the coin on kraken."""
    print(f"accessing kraken api for {cypto_name}")
    value = 69
    print(f"Current value for {symbol} is {value}")
    return value

def get_history_data_kraken(kraken_id, interval):
    """Given a list of pair names, return the data for each pair from the api. Save the data to a csv file."""
        # get the historical data for the pair over a given time period
    historical_url = f"https://api.kraken.com/0/public/OHLC?pair={kraken_id}&interval={interval}"
    historical_response = requests.get(historical_url)
    historical_data = historical_response.json()
    pair_key = list(historical_data["result"].keys())[0]

    historical_data = historical_data["result"][pair_key]
    historical_data = pd.DataFrame(historical_data)
    historical_data.columns = ["time", "open", "high", "low", "close", "vwap", "volume", "count"]
    historical_data["time"] = pd.to_datetime(historical_data["time"], unit="s")

    # save the data to a csv file in the log folder
    historical_data.to_csv(f"logs/{cypto['symbol']}.csv", index=False)


def plot_graph(csv_file):
    """Plot the graph of the crypto currency from the csv file."""
    # read the csv as a dictionary
    df = pd.read_csv(csv_file)

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
