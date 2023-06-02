"""main application for open_trader"""
import os
import json
import requests
import execute_trade
import open_ai_client
import output_to_discord
import get_value
import config


def main():
    """main function"""
    # get the data from the api
    #df = get_value.get_combined_results("XBT", "USD", 1000, 1)
    get_value.get_history_data_kraken(config.cypto_currency)
    breakpoint()
    #data = open_ai_client.get_data()
    # get the response from the api
    #response = open_ai_client.get_response(data)
    # execute the trade
    #execute_trade.execute_trade(response)
    # send the response to discord
    #output_to_discord.send_message(response)

if __name__ == "__main__":
    main()