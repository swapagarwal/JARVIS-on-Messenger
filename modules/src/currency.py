import requests

def process(input, entities=None):
    output = {}
    try:
        from_currency = entities['from_currency'][0]['value'].upper()
        to_currency = entities['to_currency'][0]['value'].upper()
        amount = float(entities['number'][0]['value'])

        r = requests.get('http://api.fixer.io/latest?base=' + from_currency)
        data = r.json()
        conversion_rate = float(data['rates'][to_currency])

        conversion_details = '1 %s = %.4f %s' % (from_currency, conversion_rate, to_currency)
        amount_conversion = '%s %s = %.4f %s' % (amount, from_currency, conversion_rate*amount, to_currency)
        
        output['input'] = input
        output['output'] = conversion_details + '<br/>' + amount_conversion
        output['success'] = True
    except:
        output['success'] = False
    return output
