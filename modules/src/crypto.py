import os

import requests
import requests_cache
import json

import config
from templates.text import TextTemplate

CRYPTO_API_KEY = os.environ.get('CRYPTO_API_KEY', config.CRYPTO_API_KEY)


def process(input, entities):
    output = {}
    try:
        from_symbol = entities[0]['value'].upper()
        url = "https://min-api.cryptocompare.com/data/price?fsym={0}&tsyms=USD&api_key={1}".format(from_symbol, CRYPTO_API_KEY)
        response = requests.get(url)
        if response.ok:
            output['input'] = input
            output['output'] = TextTemplate(
                "1 " + from_symbol + " = " + str(json.loads(response.content)["USD"]) +  " USD"
                ).get_message()
            output['success'] = True
        else:
            raise Exception("Ticker symbol not found.")
    except:
        error_message = 'I couldn\'t find the price for that cryptocurrency.'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
