import requests

def process(input, entities=None):
    output = {}
    try:
        from_currency = entities['from_currency'][0]['value']
        to_currency = entities['to_currency'][0]['value']

        r = requests.get('http://api.fixer.io/latest?base=' + from_currency)
        data = r.json()
        conversion_rate = data['rates'][to_currency]

        output['input'] = input
        output['output'] = '1 %s = %s %s' % (from_currency, conversion_rate, to_currency)
        output['success'] = True
    except:
        output['success'] = False
    return output
