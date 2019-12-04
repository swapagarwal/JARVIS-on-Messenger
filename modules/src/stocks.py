import os

import requests
import requests_cache
import json

import config
from templates.text import TextTemplate

IEX_API_KEY = os.environ.get('IEX_API_KEY', config.IEX_API_KEY)


def process(input, entities):
    output = {}
    try:
        ticker = entities[0]['value']
        url = "https://cloud.iexapis.com/stable/stock/{0}/quote?token={1}".format(ticker, IEX_API_KEY)
        response = requests.get(url)
        if response.ok:
            output['input'] = input
            output['output'] = TextTemplate(
                'Price of ' + ticker.upper() + ': ' + '$' + str(json.loads(response.content)["iexRealtimePrice"])
                ).get_message()
            output['success'] = True
        else:
            raise Exception("Ticker symbol not found.")
    except:
        error_message = 'I couldn\'t find the price for that stock.'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
