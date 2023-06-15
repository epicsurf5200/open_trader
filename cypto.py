"""class to handle cypto attributes and methods to retrieve data from the class"""
import pandas as pd
import numpy as np
import datetime

class Cypto:
    """class to handle cypto attributes"""
    def __init__(
            self, 
            symbol: str,
            ):
        """initialize the class"""
        self.symbol = symbol

        # get the attributes from the coin_info.csv file given the symbol
        coin_info = pd.read_csv("coin_info.csv")
        coin_info = coin_info[coin_info["symbol"] == self.symbol]
        self.name = coin_info["name"].values[0]
        self.kraken_id = coin_info["kraken_id"].values[0]
        #self.binance_id = coin_info["binance_id"].values[0]
        #self.coinbase_id = coin_info["coinbase_id"].values[0]

        self.name = name
        self.log_file = f"logs/{self.symbol}.csv"
        self.plot_file = f"plots/{self.symbol}.png"
    
    def get_kraken_value(self, attribute):




    