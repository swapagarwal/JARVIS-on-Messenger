"""
Currency Module

This module can take in queries to either return a set
conversion rate from one currency to another, or it will
return the appropriate converted result.

API used: https://exchangeratesapi.io/
"""
import requests

from templates.text import TextTemplate


def process(input, entities):
    # Official Currency Terms
    currencies = ['USD', 'JPY', 'BGN',
                  'CZK', 'DKK', 'GBP',
                  'HUF', 'PLN', 'RON',
                  'SEK', 'CHF', 'ISK',
                  'NOK', 'HRK', 'RUB',
                  'TRY', 'AUD', 'BRL',
                  'CAD', 'CNY', 'HKD',
                  'IDR', 'ILS', 'INR',
                  'KRW', 'MXN', 'MYR',
                  'NZD', 'PHP', 'SGD',
                  'THB', 'ZAR']

    # Colloquial Currency Terms
    layman_currencies = ['dollar', 'yen', 'lev', 'koruna',
                         'krone', 'sterling', 'forint', 'zloty',
                         'leu', 'swedish krona', 'franc', 'iceland krona',
                         'norway krone', 'kuna', 'rouble', 'lira',
                         'australian dollar', 'real', 'canadian dollar',
                         'yuan', 'hong kong dollar', 'rupiah', 'shekel',
                         'rupee', 'won', 'peso', 'ringgit',
                         'new zealand dollar', 'philippine peso', 'singapore dollar',
                         'baht', 'rand']
    output = {}
    try:
        # Get source and target currency from query data
        source_currency = entities['from_currency'][0]['value'].lower()
        target_currency = entities['to_currency'][0]['value'].lower()

        # Change from colloquial into offical currency term
        if source_currency in layman_currencies:
            src_index = layman_currencies.index(source_currency)
            source_currency = currencies[src_index]
        if target_currency in layman_currencies:
            tgt_index = layman_currencies.index(target_currency)
            target_currency = currencies[tgt_index]
        
        source_currency = source_currency.upper()
        target_currency = target_currency.upper()

        # Set Base Currency and get Base Rates
        resp = requests.get('https://api.exchangeratesapi.io/latest?base=' + source_currency)
        data = resp.json()

        # Get Conversion Rate output
        conversion_rate = data['rates'][target_currency]
        conversion_output = '%.4f' % conversion_rate

        curr_output = 'Conversion Rate from ' + source_currency + ' to '
        curr_output += target_currency + ':    ' + conversion_output

        # # Check if returning converted currency or rate
        if 'number' in entities:
            initial_amount = entities['number'][0]['value']
            converted_amount = float(initial_amount) * conversion_rate
            converted_output = '%.2f' % converted_amount

            curr_output = str(initial_amount) + ' ' + source_currency + ' is equal to '
            curr_output += converted_output + ' ' + target_currency

        # Set response parameters
        output['input'] = input
        output['output'] = TextTemplate(curr_output).get_message()
        output['success'] = True

    except:
        # Error message for failed GET request
        error_message = 'I couldn\'t convert between those currencies.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - HKD to USD'
        error_message += '\n  - USD to EUR rate'
        error_message += '\n  - how much is 100 USD to INR'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False

    return output
