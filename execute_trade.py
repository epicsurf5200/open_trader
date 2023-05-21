"""use the binance api to execute trades"""
import requests
import json
import os
import pandas as pd
import numpy as np
import datetime
import time
import math
import matplotlib.pyplot as plt

def send_action(action):
    """send the action to the api"""
    url = "https://api.binance.com/api/v3/order/test"
    response = requests.post(url, data=action)
    json = response.json()
    return json

def execute_trade_binance(action):
    """execute the trade on binance"""
    url = "https://api.binance.com/api/v3/order"
    response = requests.post(url, data=action)
    json = response.json()
    return json