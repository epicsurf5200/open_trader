"""interact with the openai api to act as a trader"""
import openai
import os
import json
import requests
import pandas as pd
import numpy as np

def research_cyptos(currencies):
    """analyze the crypto market by providing news data to openai"""
    news_url = f"/api/v1/posts/?auth_token=715764174bd8a25b6b536399e0da83f76002fe57&currencies={currencies}"
    news_response = requests.get(news_url)
