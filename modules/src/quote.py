import re
import requests

def process(input, entities=None):
    output = {}
    try:
        # Programming quotes
        r = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
        data = r.json()
        output['input'] = input
        output['output'] = data['quote'] + " - " + data['author']
        output['success'] = True
    except:
        output['success'] = False
    return output
