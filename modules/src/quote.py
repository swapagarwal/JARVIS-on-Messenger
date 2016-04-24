import requests
from templates.text import TextTemplate

def process(input, entities=None):
    output = {}
    try:
        # Programming quotes
        r = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
        data = r.json()
        output['input'] = input
        output['output'] = TextTemplate(data['quote'] + ' - ' + data['author']).get_message()
        output['success'] = True
    except:
        output['success'] = False
    return output
