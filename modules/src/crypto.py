import requests

from templates.text import TextTemplate


def process(input, entities):
    output = {}
    try:
        market = entities['market'][0]['value'].upper()
        if 'to' in market:
            market.replace('to', '-').replace(' ', '')

        r = requests.get('https://bittrex.com/api/v1.1/public/getticker?market=' + market)
        data = r.json()

        if data['success'] == False:
            market += '-' + market[:market.find('-')]
            market = market[market.find('-')+1:]
            r = requests.get('https://bittrex.com/api/v1.1/public/getticker?market=' + market)
            data = r.json()

        bid = data['result']['Bid']
        ask = data['result']['Ask']
        last = data['result']['Last']

        ticker_details = '%s\n  - Bid: %.8f\n  - Ask: %.8f\n  - Last: %.8f' % (
        market, bid, ask, last)

        output['input'] = input
        output['output'] = TextTemplate(ticker_details).get_message()
        output['success'] = True
    except:
        error_message = 'I couldn\'t find that ticker.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - BTC to LTC'
        error_message += '\n  - BTC-LTC'
        error_message += '\n  - get ticker for BTC to ETH'
        error_message += '\n  - get market for BTC-LTC'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
