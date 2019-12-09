import json
import os
import config
import modules
from templates.quick_replies import add_quick_reply
import requests
from templates.text import TextTemplate

IEX_TICKER_API_KEY = os.environ.get('IEX_TICKER_API_KEY', config.IEX_TICKER_API_KEY)


def process(input, entities=None):
    output = {}
    try:
        ticker = entities[0]['value']
        URL = "https://cloud.iexapis.com/stable/stock/{}/quote?token={}".format(ticker, IEX_TICKER_API_KEY)
        r = requests.get(url=URL)
        if r.ok:
            data = r.json()
            message = TextTemplate("The current stock price of " + str(data['symbol']) + " is "
                                   + "$" + str(data['latestPrice'])).get_message()

            message = add_quick_reply(message, 'Another stock!', modules.generate_postback('stock'))
            output['input'] = input
            output['output'] = message
            output['success'] = True
        else:
            raise Exception("The stock you are searching was not found")

    except:
        output['success'] = False
    return output
