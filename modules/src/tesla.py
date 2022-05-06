import os

import requests
import yfinance as yf
from pandas_datareader import data as pdr
import pandas as pd
import config
from templates.text import TextTemplate

url = "https://yh-finance.p.rapidapi.com/auto-complete"

querystring = {"q":"tesla","region":"US"}

headers = {
	"X-RapidAPI-Host": "yh-finance.p.rapidapi.com",
	"X-RapidAPI-Key": "226a04e7dbmsh1f0ff16e1a0509ep12944ajsnd04a3c37ae7d"
}



def process(input, entities=None):
    output = {}
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        stock_data = response.json()
        news = stock_data["news"]
        formatted_string = ""
        for post in news:
            formatted_string += post["title"] + " (" +post["publisher"]+ ")\n"
        output['input'] = input
        output['output'] = TextTemplate(formatted_string).get_message()
        output['success'] = True
    except:
        error_message = 'I couldn\'t get current stock news you asked for.'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
