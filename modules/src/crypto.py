import requests

from templates.text import TextTemplate


def process(entry, entities):
    output = {}

    class BittrexAPIException(Exception):
        error_message = 'I could not obtain the information.'
        error_message += '\nPlease try again later!'
        output['error_msg'] = error_message
        output['success'] = False

    try:
        market = entities['market'][0]['value'].upper()
        if 'to' in market:
            market = market.replace('to', '-').replace(' ', '')

        r = requests.get('https://bittrex.com/api/v1.1/public/getticker?market=' + market)
        data = r.json()

        if not data['success']:
            market += '-' + market[:market.find('-')]
            market = market[market.find('-')+1:]
            r = requests.get('https://bittrex.com/api/v1.1/public/getticker?market=' + market)
            data = r.json()

        if not data['success']:
            raise BittrexAPIException(data)
        else:
            bid = data['result']['Bid']
            ask = data['result']['Ask']
            last = data['result']['Last']

            ticker_details = '%s\n  - Bid: %.8f\n  - Ask: %.8f\n  - Last: %.8f' % (
                market, bid, ask, last)

            output['input'] = entry
            output['output'] = TextTemplate(ticker_details).get_message()
            output['success'] = True
    except:
        if not output['error_msg']:
            error_message = 'I couldn\'t find that ticker.'
            error_message += '\nPlease ask me something else, like:'
            error_message += '\n  - BTC to LTC'
            error_message += '\n  - BTC-LTC'
            error_message += '\n  - get ticker for BTC to ETH'
            error_message += '\n  - get market for BTC-LTC'
            output['error_msg'] = TextTemplate(error_message).get_message()
            output['success'] = False

    return output

