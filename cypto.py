"""class to handle cypto attributes and methods to retrieve data for the given con"""
import pandas as pd
import datetime
import get_value
import config

class Cypto:
    """class to handle cypto actions and attributes across multiple exchanges"""
    def __init__(
            self, 
            symbol: str,
            ):
        """initialize the class"""
        self.symbol = symbol

        # get the attributes from the coin_info.csv file given the symbol
        coin_info = pd.read_csv("data/coin_info.csv")
        coin_info = coin_info[coin_info["symbol"] == self.symbol]
        self.name = coin_info["name"].values[0]
        self.kraken_id = coin_info["kraken_id"].values[0]
        #self.binance_id = coin_info["binance_id"].values[0]
        #self.coinbase_id = coin_info["coinbase_id"].values[0]

        self.log_file = f"logs/{self.symbol}.csv"
        self.plot_file = f"plots/{self.symbol}.png"
    
    def get_value(self, platform:str): 
        """get the current cypto value from the specifed platform in USD

        Args:
            platform (str): platform name (kraken, coin_base, binance)
        """        
        print(f"Get the current value of {self.name} from the {platform} platform")
        if platform == "kraken":
            value = get_value.get_value_kraken(self.name, self.symbol, self.kraken_id)
        #if platform == "coin_base":
        #    get_value.get_value_coinbase()
        #if platform == "binance":
        #    value = get_value.get_value_binace(self.name, )
        else:
            print("unknown platform")
            KeyError

        return value

    def update_history(self, platform:str):
        """create a new log entry for the platform

        Args:
            platform (str): _description_
        """ 


    def get_owned_value(self, platforms:list = config.platforms):
        for platform in platforms:
            value = 12
            print(f"currently own {value} of {self.name} on the {platform} platform")