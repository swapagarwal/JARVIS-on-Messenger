import re
import requests

def process(input, entities=None):
    output = {}
    try:
        r = requests.get('https://api.chucknorris.io/jokes/random')
        data = r.json()
        output['input'] = input
        output['output'] = data['value']
        output['success'] = True
    except:
        output['success'] = False
    return output
