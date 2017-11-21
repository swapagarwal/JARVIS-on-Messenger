import requests
import json

from templates.text import TextTemplate


def process(input, entities):
    output = {}
    try:
        stock_name = entities['stocks'][0]['value'].upper()

        r = requests.get('http://www.google.com/finance?q='+stock_name+'&output=json')
        data = json.loads(r.text[3:])
        stockprice = data[0]['l']

        returnString = 'The last price of ' + stock_name + ' is: USD '+ stockprice
        output['input'] = input
        output['output'] = TextTemplate(returnString).get_message()
        output['success'] = True
    except:
        error_message = 'I couldn\'t find a stock price for that company name.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - What is the price of Apple'
        error_message += '\n  - What is the price of Microsoft'
        error_message += '\n  - Show me the price of Apple'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
