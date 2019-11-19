import requests

from templates.text import TextTemplate
import json
import config


def currency_symbol(currency):
    with open(config.CURRENCIES_SOURCE_FILE, 'r') as currencies_file:
        currencies = json.load(currencies_file)

    if currency in currencies:
        return currencies[currency]
    elif len(currency) > 1 and currency[:-1] in currencies:
        return currencies[currency[:-1]]
    return currency



def process(input, entities):
    output = {}
    try:
        from_currency = currency_symbol(entities['from_currency'][0]['value'].upper())
        to_currency = currency_symbol(entities['to_currency'][0]['value'].upper())
        r = requests.get('http://api.fixer.io/latest?base=' + from_currency)
        data = r.json()
        conversion_rate = data['rates'][to_currency]

        conversion_details = '1 %s = %.4f %s' % (from_currency, conversion_rate, to_currency)
        if 'number' in entities:
            amount = entities['number'][0]['value']
            if amount != 1:
                conversion_details += '\n%s %s = %.4f %s' % (
                amount, from_currency, amount * conversion_rate, to_currency)

        output['input'] = input
        output['output'] = TextTemplate(conversion_details).get_message()
        output['success'] = True
    except:
        error_message = 'I couldn\'t convert between those currencies.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - HKD to USD'
        error_message += '\n  - USD to EUR rate'
        error_message += '\n  - how much is 100 USD to INR'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
