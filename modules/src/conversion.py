import requests

from templates.text import TextTemplate

CONVERT_API_KEY = os.environ.get('CONVERT_API_KEY', config.CONVERT_API_KEY)

def process(input, entities):
    output = {}
    try:
        from_unit = entities['from_unit'][0]['value']
        to_unit = entities['to_unit'][0]['value']
        amount = entities['number'][0]['value']

        url = "https://community-neutrino-currency-conversion.p.rapidapi.com/convert"
        payload = "from-type={}&to-type={}&from-value={}".format(from_unit, to_unit, amount)
        headers = {
            'x-rapidapi-host': "community-neutrino-currency-conversion.p.rapidapi.com",
            'x-rapidapi-key': CONVERT_API_KEY,
            'content-type': "application/x-www-form-urlencoded"
            }

        r = requests.request("POST", url, data=payload, headers=headers)
        data = r.json()

        if data['valid']:
            conversion_details = "{} {} = {} {}".format(amount, from_unit, str(round(data['result-float'], 1)), to_unit)
            output['input'] = input
            output['output'] = TextTemplate(conversion_details).get_message()
            output['success'] = True
        else:
            raise Exception

    except:
        error_message = 'I couldn\'t perform that conversation.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - convert 50 kg to pounds'
        error_message += '\n  - what is 20 C in F'
        error_message += '\n  - 100 m in feet'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output